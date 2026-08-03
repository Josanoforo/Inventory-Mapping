#!/usr/bin/env python3
"""
Etapa 3 — paso 1: comparacion determinista de los dos corpus de re-extraccion.

Compara los extraction records producidos por dos codificadores sobre el mismo
conjunto de skeletons. El script NO adjudica: clasifica diferencias y produce
un muestreo reproducible para que el operador decida.

Determinismo:
  - misma entrada -> misma salida, byte a byte
  - ninguna decision depende de juicio de modelo
  - unica normalizacion aplicada: strip de whitespace de bordes en strings
  - NO se normaliza mayusculas, NO se agrupan sinonimos, NO se colapsan
    valores parecidos

Uso:
  python3 state/scripts/etapa3_compare.py \
      --sonnet <dir corpus sonnet> \
      --fable  <dir corpus fable> \
      --skeletons working/data_extraction/skeleton_batches \
      --out state/output
"""

import argparse
import json
import os
import random
import re
import sys
from collections import OrderedDict

# ---------------------------------------------------------------------------
# Constantes de configuracion (declaradas, no derivadas de entorno)
# ---------------------------------------------------------------------------

SEED = 20260803
TARGET_SAMPLE = 60

CODER_A = "Sonnet"
CODER_B = "Fable"

# Campos que provienen del skeleton. Deben ser identicos en ambos corpus.
# Cualquier divergencia aqui es bug de integridad, no desacuerdo de juicio.
MECHANICAL_FIELDS = [
    "extraction_id",
    "source_packet_id",
    "source_id",
    "source_type",
    "source_title",
    "source_ref",
    "source_date_if_available",
    "snippet_primary",
    "snippet_context_before",
    "snippet_context_after",
    "traceability_pointer",
    "_source_snippet_id",
]

# Estratos por batch de origen del skeleton.
STRATA = [
    ("E1", 1, 16),
    ("E2", 17, 40),
    ("E3", 41, 48),
]

# Campos mecanicos que ya declaran enum en el schema pero se comparan como
# integridad, no como elegibilidad de muestreo (vienen del skeleton).
ENUM_FIELDS_EXCLUDED_AS_MECHANICAL = ["source_type", "traceability_pointer"]

# Clases de diferencia
CLASS_A = "A"  # divergencia de valor: ambos con valor, valores distintos
CLASS_B = "B"  # presencia vs ausencia: uno con valor, el otro null/[]/ausente
CLASS_C = "C"  # orden en arrays: mismos elementos, distinto orden

ABSENT = object()  # centinela: la clave no existe en el record


# ---------------------------------------------------------------------------
# Normalizacion (minima y explicita)
# ---------------------------------------------------------------------------

def norm(value):
    """Normaliza SOLO whitespace de bordes en strings, recursivamente.

    No toca mayusculas, no reordena, no colapsa. Cualquier otra
    normalizacion introduciria juicio.
    """
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return [norm(v) for v in value]
    if isinstance(value, dict):
        return {k: norm(v) for k, v in value.items()}
    return value


def is_empty(value):
    """True si el valor cuenta como ausencia: ausente, null, [] o ''."""
    if value is ABSENT or value is None:
        return True
    if isinstance(value, (list, dict, str)) and len(value) == 0:
        return True
    return False


def freeze(value):
    """Representacion hashable y estable de un valor, para comparar conjuntos."""
    if isinstance(value, list):
        return ("list",) + tuple(freeze(v) for v in value)
    if isinstance(value, dict):
        return ("dict",) + tuple(
            (k, freeze(value[k])) for k in sorted(value.keys())
        )
    return ("scalar", type(value).__name__, repr(value))


def multiset(seq):
    """Multiconjunto de una lista, como dict congelado -> conteo."""
    out = {}
    for item in seq:
        key = freeze(item)
        out[key] = out.get(key, 0) + 1
    return out


# ---------------------------------------------------------------------------
# Clasificacion de una diferencia de campo
# ---------------------------------------------------------------------------

def classify(val_a, val_b):
    """Clasifica la relacion entre dos valores de un mismo campo.

    Devuelve None si son equivalentes, o una de CLASS_A / CLASS_B / CLASS_C.
    """
    a_empty = is_empty(val_a)
    b_empty = is_empty(val_b)

    if a_empty and b_empty:
        return None
    if a_empty != b_empty:
        return CLASS_B

    # Ambos con valor.
    if isinstance(val_a, list) and isinstance(val_b, list):
        if multiset(val_a) == multiset(val_b):
            # Mismos elementos: identicos, o solo cambia el orden.
            if freeze(val_a) == freeze(val_b):
                return None
            return CLASS_C
        # Los conjuntos difieren -> es (A) o (B) segun corresponda.
        # Un lado vacio ya se resolvio arriba, asi que aqui es (A).
        return CLASS_A

    if freeze(val_a) == freeze(val_b):
        return None
    return CLASS_A


# ---------------------------------------------------------------------------
# Campos de elegibilidad, derivados del schema (no hardcodeados)
# ---------------------------------------------------------------------------

def derive_enum_fields(schema_path):
    """Recorre el schema y devuelve las propiedades top-level que declaran un
    enum en cualquier profundidad: directo, dentro de un oneOf, o en items de
    un array. No se hardcodea la lista de campos; se deriva del JSON Schema.
    """
    with open(schema_path, "r", encoding="utf-8") as fh:
        schema = json.load(fh)

    def declares_enum(node):
        found = []

        def walk(n):
            if not isinstance(n, dict):
                return
            if "enum" in n:
                found.append(n["enum"])
            if "items" in n:
                walk(n["items"])
            if "oneOf" in n:
                for sub in n["oneOf"]:
                    walk(sub)
            if "properties" in n:
                for sub in n["properties"].values():
                    walk(sub)

        walk(node)
        return found

    out = []
    for name, node in schema.get("properties", {}).items():
        if declares_enum(node):
            out.append(name)
    return out


def eligibility_fields(schema_path):
    """Campos de enum del schema, menos los que ya se comparan como
    integridad mecanica (vienen del skeleton, no del juicio del codificador).
    """
    enum_fields = derive_enum_fields(schema_path)
    excluded = set(ENUM_FIELDS_EXCLUDED_AS_MECHANICAL)
    return enum_fields, [f for f in enum_fields if f not in excluded]


# ---------------------------------------------------------------------------
# Carga de corpus
# ---------------------------------------------------------------------------

def load_records(records_dir):
    """Carga todos los records de un directorio, indexados por extraction_id."""
    out = {}
    for name in sorted(os.listdir(records_dir)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(records_dir, name)
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        eid = data.get("extraction_id")
        if eid is None:
            eid = name[:-len(".json")]
        out[eid] = {k: norm(v) for k, v in data.items()}
    return out


def load_rejected_ids(rejected_dir):
    """Devuelve el conjunto de extraction_id en rejected_archive."""
    out = set()
    if not os.path.isdir(rejected_dir):
        return out
    for name in sorted(os.listdir(rejected_dir)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(rejected_dir, name)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            eid = data.get("extraction_id")
        except (ValueError, OSError):
            eid = None
        if not eid:
            eid = name[:-len(".json")]
        out.add(eid)
    return out


def load_batch_map(skeleton_root):
    """Mapea extraction_id -> batch de origen, leyendo los skeleton_batches.

    Fuente unica de verdad para el batch: el arbol de skeletons, no los
    manifests de cada codificador.
    """
    out = {}
    for batch in sorted(os.listdir(skeleton_root)):
        bdir = os.path.join(skeleton_root, batch)
        if not os.path.isdir(bdir):
            continue
        for name in sorted(os.listdir(bdir)):
            if not name.endswith(".json"):
                continue
            eid = name
            if eid.startswith("skeleton_"):
                eid = eid[len("skeleton_"):]
            eid = eid[:-len(".json")]
            out[eid] = batch
    return out


def batch_number(batch_label):
    """'batch_017' -> 17. Devuelve None si no parsea."""
    m = re.search(r"(\d+)", batch_label or "")
    return int(m.group(1)) if m else None


def stratum_of(batch_label):
    n = batch_number(batch_label)
    if n is None:
        return None
    for name, lo, hi in STRATA:
        if lo <= n <= hi:
            return name
    return None


# ---------------------------------------------------------------------------
# Criterios vigentes por batch
# ---------------------------------------------------------------------------

def parse_criteria_sonnet(path):
    """Extrae las adiciones de criterio de Sonnet.

    Formato: bloques '--- Agregado tras batch_NNN: <texto> ---'.
    Se etiquetan S1..Sn en orden de aparicion.
    """
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    items = []
    pattern = re.compile(
        r"---\s*Agregado tras (batch_\d+)\s*:\s*(.*?)---", re.DOTALL
    )
    for idx, m in enumerate(pattern.finditer(text), start=1):
        batch = m.group(1)
        body = " ".join(m.group(2).split())
        items.append(
            {
                "id": "S%d" % idx,
                "batch": batch,
                "batch_n": batch_number(batch),
                "text": body,
            }
        )
    return items


def parse_criteria_fable(path):
    """Extrae las adiciones de criterio de Fable.

    Formato: encabezado '## [batch_NNN] ...' seguido de items 'KN. <texto>'.
    """
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    items = []
    cur_batch = None
    cur = None
    header = re.compile(r"^##\s*\[(batch_\d+)\]")
    item = re.compile(r"^(K\d+)\.\s*(.*)$")
    for line in lines:
        hm = header.match(line.strip())
        if hm:
            if cur:
                items.append(cur)
                cur = None
            cur_batch = hm.group(1)
            continue
        im = item.match(line.strip())
        if im and cur_batch:
            if cur:
                items.append(cur)
            cur = {
                "id": im.group(1),
                "batch": cur_batch,
                "batch_n": batch_number(cur_batch),
                "text": im.group(2).strip(),
            }
            continue
        if cur is not None and line.strip() and not line.strip().startswith("#"):
            cur["text"] = (cur["text"] + " " + line.strip()).strip()
    if cur:
        items.append(cur)
    for it in items:
        it["text"] = " ".join(it["text"].split())
    return items


def criteria_in_force(items, batch_label):
    """Criterios formulados ANTES de procesar este batch.

    Una adicion registrada 'tras batch_N' / '[batch_N]' rige desde el batch
    N+1 en adelante. Ambos criteria.md declaran las adiciones como no
    retroactivas, asi que no se aplican al batch en que se formularon.
    """
    n = batch_number(batch_label)
    if n is None:
        return []
    return [it for it in items if it["batch_n"] is not None and it["batch_n"] < n]


# ---------------------------------------------------------------------------
# Render de valores para markdown legible (sin JSON crudo)
# ---------------------------------------------------------------------------

def render_value(value):
    if value is ABSENT:
        return "_(campo ausente)_"
    if value is None:
        return "_(null)_"
    if isinstance(value, list):
        if len(value) == 0:
            return "_(lista vacia)_"
        return " · ".join(render_scalar(v) for v in value)
    if isinstance(value, dict):
        if len(value) == 0:
            return "_(objeto vacio)_"
        return " · ".join(
            "%s = %s" % (k, render_scalar(value[k])) for k in sorted(value)
        )
    return render_scalar(value)


def render_scalar(value):
    if value is None:
        return "_(null)_"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (list, dict)):
        return render_value(value)
    text = str(value)
    text = text.replace("|", "\\|")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\n", "<br>")
    return text


# ---------------------------------------------------------------------------
# Comparacion
# ---------------------------------------------------------------------------

def compare(records_a, records_b, batch_map, eligibility_field_set):
    """Compara el universo comun y devuelve la estructura de resultados.

    eligibility_field_set: campos de enum (menos los mecanicos) usados para
    decidir si un record entra a la muestra (paso 3 revisado). No afecta el
    conteo por campo, que sigue reportando TODOS los campos.
    """
    universe = sorted(set(records_a) & set(records_b))

    # Campos de juicio: los que aparecen en cualquiera de los dos corpus,
    # menos los mecanicos. Derivados de los records, no hardcodeados.
    seen_a, seen_b = set(), set()
    for eid in universe:
        seen_a.update(records_a[eid].keys())
        seen_b.update(records_b[eid].keys())
    mechanical = set(MECHANICAL_FIELDS)
    judgment_fields = sorted((seen_a | seen_b) - mechanical)
    mechanical_present = [f for f in MECHANICAL_FIELDS if f in (seen_a | seen_b)]
    mechanical_absent = [f for f in MECHANICAL_FIELDS if f not in (seen_a | seen_b)]

    # Campos presentes en un corpus y no en el otro (hallazgo aparte).
    only_a = sorted(seen_a - seen_b)
    only_b = sorted(seen_b - seen_a)

    per_field = OrderedDict()
    for field in mechanical_present + judgment_fields:
        per_field[field] = {CLASS_A: 0, CLASS_B: 0, CLASS_C: 0}

    integrity_bugs = []
    cases = []

    for eid in universe:
        ra, rb = records_a[eid], records_b[eid]
        batch = batch_map.get(eid)
        diffs = []

        for field in mechanical_present:
            va = ra.get(field, ABSENT)
            vb = rb.get(field, ABSENT)
            cls = classify(va, vb)
            if cls:
                per_field[field][cls] += 1
                integrity_bugs.append(
                    {
                        "extraction_id": eid,
                        "batch": batch,
                        "field": field,
                        "class": cls,
                        "value_a": va,
                        "value_b": vb,
                    }
                )

        for field in judgment_fields:
            va = ra.get(field, ABSENT)
            vb = rb.get(field, ABSENT)
            cls = classify(va, vb)
            if cls:
                per_field[field][cls] += 1
                diffs.append(
                    {
                        "field": field,
                        "class": cls,
                        "value_a": va,
                        "value_b": vb,
                        "is_eligibility_field": field in eligibility_field_set,
                    }
                )

        if diffs:
            has_ab_any = any(d["class"] in (CLASS_A, CLASS_B) for d in diffs)
            has_ab_eligible = any(
                d["class"] in (CLASS_A, CLASS_B) and d["is_eligibility_field"]
                for d in diffs
            )
            cases.append(
                {
                    "extraction_id": eid,
                    "batch": batch,
                    "stratum": stratum_of(batch),
                    "diffs": diffs,
                    "has_ab": has_ab_any,
                    "has_ab_eligible": has_ab_eligible,
                    "snippet_primary": ra.get("snippet_primary", ABSENT),
                }
            )

    return {
        "universe": universe,
        "judgment_fields": judgment_fields,
        "mechanical_present": mechanical_present,
        "mechanical_absent": mechanical_absent,
        "fields_only_a": only_a,
        "fields_only_b": only_b,
        "per_field": per_field,
        "integrity_bugs": integrity_bugs,
        "cases": cases,
    }


# ---------------------------------------------------------------------------
# Muestreo estratificado
# ---------------------------------------------------------------------------

def eligibility_counts_by_stratum(cases, key):
    """Cuenta, por estrato, cuantos casos cumplen `key` (funcion sobre case).
    Usado para reportar el contraste entre el criterio de elegibilidad
    anterior (cualquier campo) y el nuevo (solo campos de enum).
    """
    out = OrderedDict((name, 0) for name, _, _ in STRATA)
    for c in cases:
        if c["stratum"] is not None and key(c):
            out[c["stratum"]] += 1
    return out


def sample(cases, seed=SEED, target=TARGET_SAMPLE):
    """Muestra estratificada proporcional, con semilla fija.

    Elegibilidad (paso 3 revisado): un record entra a la muestra si tiene al
    menos un desacuerdo (A) o (B) en un CAMPO DE ENUM (elegibilidad), no en
    cualquier campo. Los desacuerdos en campos de texto libre no hacen
    elegible a un record por si solos, pero se siguen mostrando en su bloque
    de adjudicacion si el record entro por otra via. Los de tipo (C) puro
    tampoco entran.
    """
    eligible = [c for c in cases if c["has_ab_eligible"] and c["stratum"] is not None]
    by_stratum = OrderedDict((name, []) for name, _, _ in STRATA)
    for c in eligible:
        by_stratum[c["stratum"]].append(c)
    for name in by_stratum:
        by_stratum[name].sort(key=lambda c: c["extraction_id"])

    total = len(eligible)
    quotas = OrderedDict()
    if total == 0:
        for name in by_stratum:
            quotas[name] = 0
    else:
        # Reparto proporcional con mayor-resto: determinista y sin sesgo de
        # redondeo acumulado.
        raw = OrderedDict(
            (name, target * len(by_stratum[name]) / float(total))
            for name in by_stratum
        )
        for name in by_stratum:
            quotas[name] = int(raw[name])
        remainder = target - sum(quotas.values())
        order = sorted(
            by_stratum.keys(),
            key=lambda n: (-(raw[n] - int(raw[n])), n),
        )
        for i in range(remainder):
            quotas[order[i % len(order)]] += 1

    rng = random.Random(seed)
    picked = []
    deficits = OrderedDict()
    for name in by_stratum:
        pool = by_stratum[name]
        quota = quotas[name]
        if len(pool) <= quota:
            chosen = list(pool)
            deficits[name] = quota - len(pool)
        else:
            chosen = rng.sample(pool, quota)
            deficits[name] = 0
        chosen.sort(key=lambda c: (c["batch"] or "", c["extraction_id"]))
        picked.extend(chosen)

    return {
        "eligible_total": total,
        "eligible_by_stratum": OrderedDict(
            (n, len(by_stratum[n])) for n in by_stratum
        ),
        "quotas": quotas,
        "deficits": deficits,
        "picked": picked,
    }


# ---------------------------------------------------------------------------
# Salidas
# ---------------------------------------------------------------------------

def write_summary(path, result, samp, rejects, corpus_meta, eligibility_meta):
    L = []
    w = L.append

    w("# Etapa 3 — resumen de comparacion determinista")
    w("")
    w("Generado por `state/scripts/etapa3_compare.py`. El script compara; no adjudica.")
    w("")
    w("## Procedencia")
    w("")
    w("| | %s | %s |" % (CODER_A, CODER_B))
    w("|---|---|---|")
    w("| Rama | `%s` | `%s` |" % (corpus_meta["branch_a"], corpus_meta["branch_b"]))
    w("| Commit | `%s` | `%s` |" % (corpus_meta["sha_a"], corpus_meta["sha_b"]))
    w("| Records | %d | %d |" % (corpus_meta["n_a"], corpus_meta["n_b"]))
    w("| Rechazos | %d | %d |" % (len(rejects["a"]), len(rejects["b"])))
    w("")

    universe = result["universe"]
    cases = result["cases"]
    n_ab = len([c for c in cases if c["has_ab"]])
    n_c_only = len([c for c in cases if not c["has_ab"]])

    w("## Universo comparado")
    w("")
    w("Universo = extraction_id presentes como record en AMBAS ramas.")
    w("Los rechazos quedan fuera del universo y se reportan aparte.")
    w("")
    w("| Metrica | N |")
    w("|---|---|")
    w("| Universo comparado (records en ambas ramas) | %d |" % len(universe))
    w("| Solo en %s | %d |" % (CODER_A, corpus_meta["only_a"]))
    w("| Solo en %s | %d |" % (CODER_B, corpus_meta["only_b"]))
    w("| Records identicos campo a campo | %d |" % (len(universe) - len(cases)))
    w("| Records con al menos una diferencia | %d |" % len(cases))
    w("| — con al menos un desacuerdo (A) o (B) | %d |" % n_ab)
    w("| — solo diferencias de orden (C) | %d |" % n_c_only)
    w("")

    w("## Normalizacion aplicada")
    w("")
    w("Unicamente `strip` de whitespace de bordes en strings, recursivo en")
    w("listas y objetos. Sin normalizacion de mayusculas, sinonimos ni")
    w("agrupacion de valores parecidos.")
    w("")
    w("Categorias, contadas por separado y sin mezclarse:")
    w("")
    w("- **(A) divergencia de valor** — ambos con valor, valores distintos.")
    w("- **(B) presencia vs ausencia** — uno con valor, el otro null / `[]` / ausente.")
    w("- **(C) orden en arrays** — mismos elementos (multiconjunto identico), distinto orden.")
    w("")
    w("Para arrays: si los multiconjuntos coinciden y el orden difiere, es (C);")
    w("si los multiconjuntos difieren, es (A), o (B) si un lado esta vacio.")
    w("")

    w("## Integridad — campos mecanicos")
    w("")
    w("Campos que vienen del skeleton y deben ser identicos en ambos corpus.")
    w("Cualquier divergencia aqui es bug de integridad, no desacuerdo de juicio.")
    w("")
    bugs = result["integrity_bugs"]
    w("**Bugs de integridad: %d**" % len(bugs))
    w("")
    w("| Campo mecanico | (A) | (B) | (C) |")
    w("|---|---:|---:|---:|")
    for f in result["mechanical_present"]:
        c = result["per_field"][f]
        w("| `%s` | %d | %d | %d |" % (f, c[CLASS_A], c[CLASS_B], c[CLASS_C]))
    w("")
    if result["mechanical_absent"]:
        w("Campos mecanicos declarados pero ausentes en ambos corpus (no comparables):")
        for f in result["mechanical_absent"]:
            w("- `%s`" % f)
        w("")
    if bugs:
        w("### Detalle de bugs de integridad")
        w("")
        w("| extraction_id | batch | campo | clase | %s | %s |" % (CODER_A, CODER_B))
        w("|---|---|---|---|---|---|")
        for b in bugs:
            w(
                "| `%s` | %s | `%s` | (%s) | %s | %s |"
                % (
                    b["extraction_id"],
                    b["batch"] or "—",
                    b["field"],
                    b["class"],
                    render_value(b["value_a"]),
                    render_value(b["value_b"]),
                )
            )
        w("")

    w("## Campos de juicio — conteo por campo")
    w("")
    w("Lista derivada de los propios records (todos los campos observados")
    w("menos los mecanicos), no hardcodeada.")
    w("")
    w("| Campo | (A) valor | (B) presencia | (C) orden | total |")
    w("|---|---:|---:|---:|---:|")
    for f in result["judgment_fields"]:
        c = result["per_field"][f]
        tot = c[CLASS_A] + c[CLASS_B] + c[CLASS_C]
        w("| `%s` | %d | %d | %d | %d |" % (f, c[CLASS_A], c[CLASS_B], c[CLASS_C], tot))
    tot_a = sum(result["per_field"][f][CLASS_A] for f in result["judgment_fields"])
    tot_b = sum(result["per_field"][f][CLASS_B] for f in result["judgment_fields"])
    tot_c = sum(result["per_field"][f][CLASS_C] for f in result["judgment_fields"])
    w("| **TOTAL** | **%d** | **%d** | **%d** | **%d** |"
      % (tot_a, tot_b, tot_c, tot_a + tot_b + tot_c))
    w("")

    if result["fields_only_a"] or result["fields_only_b"]:
        w("### Campos presentes en un corpus y no en el otro")
        w("")
        for f in result["fields_only_a"]:
            w("- `%s` — aparece solo en %s" % (f, CODER_A))
        for f in result["fields_only_b"]:
            w("- `%s` — aparece solo en %s" % (f, CODER_B))
        w("")
    else:
        w("### Campos presentes en un corpus y no en el otro")
        w("")
        w("Ninguno: ambos corpus usan el mismo conjunto de claves.")
        w("")

    w("## Elegibilidad de muestreo — campos de enum")
    w("")
    w("Criterio revisado (paso 3): un record es elegible para la muestra si")
    w("tiene al menos un desacuerdo (A) o (B) en un CAMPO DE ENUM, no en")
    w("cualquier campo. Los campos de enum se derivan del schema")
    w("`%s`," % eligibility_meta["schema_path"])
    w("recorriendo cada propiedad top-level en busca de `enum` directo, dentro")
    w("de `oneOf`, o en `items` de un array.")
    w("")
    w("**Campos de enum declarados por el schema:**")
    w("")
    for f in eligibility_meta["all_enum_fields"]:
        tag = " _(excluido: mecanico)_" if f in eligibility_meta["excluded_mechanical"] else ""
        w("- `%s`%s" % (f, tag))
    w("")
    w("**Campos de elegibilidad (enum, menos mecanicos):**")
    w("")
    for f in eligibility_meta["eligibility_fields"]:
        w("- `%s`" % f)
    w("")
    w("Los desacuerdos en campos de texto libre (`subject_exact`,")
    w("`local_qualifiers`, `metric_value_raw`, `metric_unit`, `time_scope_raw`,")
    w("`time_scope_normalized_if_safe`, `geography_if_explicit`,")
    w("`parser_notes`, `platforms`, `author_or_actor_if_available`) no hacen")
    w("elegible a un record por si solos, pero se siguen mostrando en su")
    w("bloque de adjudicacion si el record entro por otra via.")
    w("")
    w("**Contraste: elegibles bajo el criterio anterior (cualquier campo) vs")
    w("el criterio de enum, por estrato:**")
    w("")
    w("| Estrato | Elegibles — criterio anterior | Elegibles — criterio enum |")
    w("|---|---:|---:|")
    for name, lo, hi in STRATA:
        w(
            "| %s | %d | %d |"
            % (
                name,
                eligibility_meta["old_by_stratum"][name],
                eligibility_meta["new_by_stratum"][name],
            )
        )
    w(
        "| **TOTAL** | **%d** | **%d** |"
        % (
            sum(eligibility_meta["old_by_stratum"].values()),
            sum(eligibility_meta["new_by_stratum"].values()),
        )
    )
    w("")

    w("## Muestreo estratificado")
    w("")
    w("**Semilla: `%d`** (fija y declarada; la muestra es reproducible).")
    L[-1] = L[-1] % SEED
    w("")
    w("Muestra objetivo: ~%d casos. Solo entran extraction_id con al menos un" % TARGET_SAMPLE)
    w("desacuerdo (A) o (B) en un CAMPO DE ENUM (elegibilidad). Los de tipo (C)")
    w("y los desacuerdos exclusivamente en campos de texto libre no entran a")
    w("la muestra. Reparto proporcional por mayor-resto sobre los elegibles de")
    w("cada estrato.")
    w("")
    w("| Estrato | Batches | Elegibles (enum A/B) | Cuota | Tomados | Deficit |")
    w("|---|---|---:|---:|---:|---:|")
    for name, lo, hi in STRATA:
        elig = samp["eligible_by_stratum"][name]
        quota = samp["quotas"][name]
        taken = quota - samp["deficits"][name]
        w(
            "| %s | batch_%03d–batch_%03d | %d | %d | %d | %d |"
            % (name, lo, hi, elig, quota, taken, samp["deficits"][name])
        )
    w(
        "| **TOTAL** | | **%d** | **%d** | **%d** | **%d** |"
        % (
            samp["eligible_total"],
            sum(samp["quotas"].values()),
            len(samp["picked"]),
            sum(samp["deficits"].values()),
        )
    )
    w("")
    if sum(samp["deficits"].values()) > 0:
        w("Hay deficit: al menos un estrato tiene menos casos elegibles que su")
        w("cuota. Se tomaron todos los disponibles y el deficit se reporta sin")
        w("redistribuir.")
        w("")

    w("## Rechazos (fuera del universo comparado)")
    w("")
    w("Solo IDs y de que lado. Sin analisis.")
    w("")
    both = sorted(rejects["a"] & rejects["b"])
    only_a = sorted(rejects["a"] - rejects["b"])
    only_b = sorted(rejects["b"] - rejects["a"])
    w("| Categoria | N |")
    w("|---|---:|")
    w("| Rechazados por ambos | %d |" % len(both))
    w("| Rechazados solo por %s | %d |" % (CODER_A, len(only_a)))
    w("| Rechazados solo por %s | %d |" % (CODER_B, len(only_b)))
    w("")
    w("| extraction_id | %s | %s |" % (CODER_A, CODER_B))
    w("|---|:---:|:---:|")
    for eid in both:
        w("| `%s` | rechazado | rechazado |" % eid)
    for eid in only_a:
        w("| `%s` | rechazado | record |" % eid)
    for eid in only_b:
        w("| `%s` | record | rechazado |" % eid)
    w("")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


def write_adjudication(path, samp, crit_a, crit_b):
    L = []
    w = L.append

    w("# Etapa 3 — casos para adjudicacion del operador")
    w("")
    w("Muestra estratificada reproducible. Semilla `%d`. %d casos."
      % (SEED, len(samp["picked"])))
    w("")
    w("Cada bloque muestra solo los campos en desacuerdo, de tipo (A)")
    w("divergencia de valor o (B) presencia vs ausencia. Las diferencias de")
    w("solo orden (C) se listan aparte al final de cada bloque cuando existen,")
    w("y no motivan la inclusion del caso.")
    w("")
    w("Elegibilidad del caso (paso 3 revisado): un record entra a la muestra")
    w("si tiene al menos un desacuerdo (A) o (B) en un **campo de enum**")
    w("(marcado 🔒 en la tabla de cada caso). Los campos de **texto libre**")
    w("(marcados 📝) no hacen elegible a un record por si solos, pero se")
    w("muestran igual si el record entro por un campo de enum.")
    w("")
    w("El veredicto lo escribe el operador. El script no adjudica.")
    w("")
    w("---")
    w("")

    for idx, case in enumerate(samp["picked"], start=1):
        eid = case["extraction_id"]
        batch = case["batch"] or "—"
        w("## Caso %d — `%s`" % (idx, eid))
        w("")
        w("- **Batch de origen:** %s" % batch)
        w("- **Estrato:** %s" % case["stratum"])
        w("")
        w("**snippet_primary:**")
        w("")
        snippet = case["snippet_primary"]
        if snippet is ABSENT or snippet is None:
            w("> _(sin snippet_primary en el record)_")
        else:
            for line in str(snippet).splitlines() or [""]:
                w("> %s" % line)
        w("")

        ab = [d for d in case["diffs"] if d["class"] in (CLASS_A, CLASS_B)]
        c_only = [d for d in case["diffs"] if d["class"] == CLASS_C]

        w("| Campo | %s | %s |" % (CODER_A, CODER_B))
        w("|---|---|---|")
        for d in ab:
            marker = "🔒 enum" if d["is_eligibility_field"] else "📝 texto libre"
            w(
                "| `%s` _(%s · %s)_ | %s | %s |"
                % (
                    d["field"],
                    d["class"],
                    marker,
                    render_value(d["value_a"]),
                    render_value(d["value_b"]),
                )
            )
        w("")

        if c_only:
            w("Diferencias de solo orden (C) en este record, no motivan inclusion:")
            for d in c_only:
                w("- `%s`" % d["field"])
            w("")

        in_a = criteria_in_force(crit_a, batch)
        in_b = criteria_in_force(crit_b, batch)
        w("**Criterios vigentes en este batch:**")
        w("")
        if in_a:
            w("- %s — %s" % (CODER_A, ", ".join(
                "%s (desde %s)" % (it["id"], it["batch"]) for it in in_a)))
        else:
            w("- %s — ninguna adicion formulada aun; solo criterios base." % CODER_A)
        if in_b:
            w("- %s — %s" % (CODER_B, ", ".join(
                "%s (desde %s)" % (it["id"], it["batch"]) for it in in_b)))
        else:
            w("- %s — ninguna adicion formulada aun; solo criterios base." % CODER_B)
        w("")
        w("**Veredicto:**")
        w("")
        w("")
        w("---")
        w("")

    w("## Apendice — texto de las adiciones de criterio referenciadas")
    w("")
    w("Derivado de `criteria.md` de cada rama. Una adicion registrada 'tras")
    w("batch_N' rige desde batch_N+1: ambos criteria.md declaran las adiciones")
    w("como no retroactivas.")
    w("")
    w("### %s" % CODER_A)
    w("")
    for it in crit_a:
        w("- **%s** (formulada tras %s, vigente desde batch_%03d): %s"
          % (it["id"], it["batch"], (it["batch_n"] or 0) + 1, it["text"]))
    w("")
    w("### %s" % CODER_B)
    w("")
    for it in crit_b:
        w("- **%s** (formulada tras %s, vigente desde batch_%03d): %s"
          % (it["id"], it["batch"], (it["batch_n"] or 0) + 1, it["text"]))
    w("")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sonnet", required=True, help="dir corpus Sonnet")
    ap.add_argument("--fable", required=True, help="dir corpus Fable")
    ap.add_argument("--skeletons", required=True, help="dir skeleton_batches")
    ap.add_argument("--out", required=True, help="dir de salida")
    ap.add_argument("--branch-a", default="")
    ap.add_argument("--branch-b", default="")
    ap.add_argument("--sha-a", default="")
    ap.add_argument("--sha-b", default="")
    ap.add_argument(
        "--schema",
        default="phases/01-source-intake/data-extraction/schemas/"
        "data_extraction_record.schema.json",
        help="schema del extraction record, para derivar campos de enum",
    )
    args = ap.parse_args()

    recs_a = load_records(os.path.join(args.sonnet, "records"))
    recs_b = load_records(os.path.join(args.fable, "records"))
    rej_a = load_rejected_ids(os.path.join(args.sonnet, "rejected_archive"))
    rej_b = load_rejected_ids(os.path.join(args.fable, "rejected_archive"))
    batch_map = load_batch_map(args.skeletons)

    crit_a = parse_criteria_sonnet(os.path.join(args.sonnet, "criteria.md"))
    crit_b = parse_criteria_fable(os.path.join(args.fable, "criteria.md"))

    all_enum_fields, elig_fields = eligibility_fields(args.schema)
    required = {
        "actor_level", "claim_type", "metric_type",
        "evidence_role", "product_type_if_explicit",
    }
    missing = required - set(elig_fields)
    if missing:
        sys.stderr.write(
            "PARADA: el schema no declara enum para: %s. El schema no "
            "coincide con lo esperado; entender por que antes de seguir.\n"
            % ", ".join(sorted(missing))
        )
        return 1

    result = compare(recs_a, recs_b, batch_map, set(elig_fields))
    samp = sample(result["cases"])

    old_by_stratum = eligibility_counts_by_stratum(
        result["cases"], lambda c: c["has_ab"]
    )
    new_by_stratum = eligibility_counts_by_stratum(
        result["cases"], lambda c: c["has_ab_eligible"]
    )
    eligibility_meta = {
        "schema_path": args.schema,
        "all_enum_fields": all_enum_fields,
        "excluded_mechanical": ENUM_FIELDS_EXCLUDED_AS_MECHANICAL,
        "eligibility_fields": elig_fields,
        "old_by_stratum": old_by_stratum,
        "new_by_stratum": new_by_stratum,
    }

    meta = {
        "branch_a": args.branch_a,
        "branch_b": args.branch_b,
        "sha_a": args.sha_a,
        "sha_b": args.sha_b,
        "n_a": len(recs_a),
        "n_b": len(recs_b),
        "only_a": len(set(recs_a) - set(recs_b)),
        "only_b": len(set(recs_b) - set(recs_a)),
    }

    if not os.path.isdir(args.out):
        os.makedirs(args.out)

    write_summary(
        os.path.join(args.out, "etapa3_comparison_summary.md"),
        result, samp, {"a": rej_a, "b": rej_b}, meta, eligibility_meta,
    )
    write_adjudication(
        os.path.join(args.out, "etapa3_adjudication.md"),
        samp, crit_a, crit_b,
    )

    n_bugs = len(result["integrity_bugs"])
    sys.stderr.write(
        "universo=%d  casos_con_diferencia=%d  elegibles_criterio_anterior=%d  "
        "elegibles_enum=%d  muestra=%d  bugs_integridad=%d\n"
        % (
            len(result["universe"]),
            len(result["cases"]),
            sum(old_by_stratum.values()),
            samp["eligible_total"],
            len(samp["picked"]),
            n_bugs,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
