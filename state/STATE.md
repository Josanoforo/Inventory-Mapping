# STATE.md

Generado: 2026-08-04T04:16:54Z (UTC), sobre HEAD `83a70a25162489763bb05d1d40878b27dec8c63e`.

Snapshot mecánico. Regenerado automáticamente por `.github/workflows/state-snapshot.yml` en cada push. Sin juicio, sin narrativa — solo lo que es extraíble determinísticamente de git, el ledger y los manifests del repo.

## main

- SHA: `83a70a25`

## Ramas remotas con commits en origin

- `claude/inventory-mapping-execution-kahq1i` — 2026-08-04T04:16:42Z — ledger: R4 agrega P-188 a Parqueados, R5 mide instancia S32/S34 de P-153
- `claude/etapa-2-extraccion-juicio-gwnfk4` — 2026-07-31T20:16:52Z — Etapa 2 fable: checkpoint_0006 final (1178/1178) + criterios K15-K16, manifest complete
- `claude/etapa-2-reextraccion-campos-cnb8bh` — 2026-07-30T07:06:04Z — Etapa 2: re-extracción independiente de campos de juicio (48/48 batches)
- `claude/etapa-2-field-extraction-jyqwwj` — 2026-07-30T06:02:23Z — Etapa 2: complete final batches 041-048 (1178/1178 processed)
- `legacy/s12-im-artifacts` — 2026-07-29T23:05:05Z — Restore legacy IM artifacts from preserve/s12-round1-75-cards (evidence only)
- `preserve/s12-round1-75-cards` — 2026-04-11T02:44:14Z — Add same-actor filter to scanners and actor composition block to builder
- `preserve/s12-round1-orphan-chain` — 2026-04-10T20:07:48Z — G1: generate signal_cards_round_1.md from 75 Signal Cards

## Ledger (`state/pendientes_ledger.md`)

- Grupo A (abiertas): 25
- Grupo B (abiertas): 43
- Grupo C (abiertas): 8
- Grupo D (abiertas): 0
- Total abiertas: 76
- Parqueadas: 6

## Últimas 5 decisiones registradas

Decisiones: no disponibles en repo

## Procesos largos en curso (re-extracción)

- `origin/claude/etapa-2-extraccion-juicio-gwnfk4` (`working_reextraction/fable/manifest.json`): status=complete, batch alcanzado=batch_048
- `origin/claude/etapa-2-field-extraction-jyqwwj` (`working_reextraction/sonnet/manifest.json`): status=complete, batch alcanzado=batch_048 final
- `origin/claude/etapa-2-reextraccion-campos-cnb8bh` (`working_reextraction/fable/manifest.json`): status=complete, batch alcanzado=batch_048

## Superficie congelada

Fuente: `state/pendientes_ledger.md`

```
superficie congelada (heading en `state/*.md`, nada lo lleva) estructuralmente vacías — lector sin escritor | decisión | ¿`find_decision_log_files()` encuentra candidatos, y algún `state/*.md` matchea `FROZEN_HEADING_RE`? | S5→E7 | verificado — `find_decision_log_files()` (`generate_state.py:181`) no encuentra candidatos en el repo; `FROZEN_HEADING_RE` (línea 296) no matchea ningún `state/*.md` |
| P-181 | P-122 vs árbol: cerrado en S28 como "retirado" y `signal_validation.schema.json` existe en `main` (:35) | decisión | Resolver la clase: cierre cuyo enunciado contradice el árbol (via sello S4 / I.13) | CC | verificado — `signal_validation.schema.json` existe en `main` (confirma la contradicción); DIFERIDA-SELLO — S4 no llegó pegado en este encargo, I.13 no se ejecutó |
| P-182 | Estados a nivel card (`pass`/`pass_with_flags`/`rework`/`reject`) declarados en 4 schemas y documentados en el validator, sin productor conocido | decisión | ¿Cuántos schemas declaran los 4 valores, y qué script los escribe? | liga P-097/P-151 | verificado: exactamente 4 schemas declaran los 4 valores (`signal_validation.schema.json`, `signal_inventory_gate.schema.json`, `source_intake_validation.schema.json`, `data_extraction_validator.schema.json`); 0 scripts los escriben |
| P-187 | Contradicción de registro sobre `verification_status`: la tabla de desincronizados (S23/S26) lo da por `deprecated` en los protocolos de DG; P-139 lo cita como enum vigente de Phase 0 desde el mismo protocolo | decisión | Resolver cuál registro tiene autoridad | DSC | |
| P-189 | Overhead como tiempo: comprometido desde S27, nunca medido; siete sesiones comparables | decisión | Medir, o aceptar sin medir | health check | |
| P-191 | Regla candidata: retirar un valor de vocabulario exige conteo en todas las capas (packets, records, cards, skeletons) — validada por E1: los tres valores reportados "0 usos" miden 2/35/355 en packets; tres retiros erróneos atrapados. Replicado por corrida independiente a segundo
```
