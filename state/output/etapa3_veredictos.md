# Etapa 3 — Veredictos de adjudicación

**Muestra:** 60 casos, semilla `20260803`, estratos E1/E2/E3.
**Paquete aplicado:** R1–R3 (previas) + R4, R5, R6, R7, R8, R9(a)(c)(d), D1, D2.
**Caídas:** R9(b) — descriptor fuera de enum contradice la decisión de corregir el corpus hacia los enums. R10 — invertida; `snippet_needs_reopen` no existe en el enum de `uncertainties` del schema de ER, se usa `context_insufficient`.
**Orden de aplicación:** D1/D2 → R6 → R5, R7, R9 → R8 → R4.

---

## Cómo leer los veredictos

| Marca | Significado |
|---|---|
| **Sonnet** / **Fable** | Ese codificador tiene el valor correcto bajo la regla aplicada |
| **Construido** | Ninguno acertó; el valor correcto se deriva de la regla y se escribe |
| **Bloqueado** | La regla determina el valor pero el schema no lo admite hoy; espera reparación |
| **Residual** | Ninguna regla cubre; veredicto del operador |
| **Forma** | Divergencia solo ortográfica o de orden; no requiere adjudicación |

Cuando un veredicto de `platforms` dice "+ marca", significa: valor determinable desde el record completo (R2) con `platform_scope_unclear` en `uncertainties` porque el nombre no aparece en el snippet (R3).

**Bloqueos activos, por si se lee fuera de contexto:**
- `metric_type` es `required` sin rama `null` en ambos schemas, y `metric_type_unclear` no está en el enum de `uncertainties` de ninguno. R9(a) no tiene salida legal: los veredictos "sin magnitud" se registran y esperan.
- Bajo corregir-hacia-enums, las magnitudes sin destino legítimo en el enum no se fuerzan al valor cercano (R9(c)). Se marcan **bloqueado — sin destino en enum** y alimentan la revisión del eje del campo.
- `platform_scope_unclear` sigue en `phase_2_only` en `pipeline_vocabulary.yaml`, que es la fuente de autoridad. R3 está aplicada en los dos schemas pero no ahí. Las marcas de R5 dependen de que se complete.

---

## E1 — Casos 1 a 20

### Caso 1 — batch_001
- `uncertainties` — **Construido** (R4). Unión validada: `current_vs_historical_ambiguity`, `time_scope_unclear`, `source_date_unclear`, `methodology_unclear`, `net_vs_gross_ambiguity`. Las cinco aplican: captura de layout de Graphtreon, cifra etiquetada "Estimated" sin método, sin fecha de snapshot, payouts sin declarar si son antes o después de fees.
- `platforms` — **Sonnet** + marca (R5). El claim es sobre payouts de Patreon; Graphtreon es la fuente, no el sujeto.
- `metric_unit` — **Fable** (R8). "USD per month" declara denominador.
- Texto libre restante: sin adjudicación.

*Sustituye el veredicto previo "Fable — R1", que era correcto en dirección pero incompleto bajo R4.*

### Caso 2 — batch_002
- `platforms` — **Sonnet** + marca (R5). Etsy es el sujeto; no aparece en el snippet, sí en el record.
- `geography_if_explicit` — **Sonnet** + marca (R2/R3). México determinable desde el record (página Etsy MX), no desde la moneda. `geography_unclear`.
- `uncertainties` — **Fable** (R4). `source_date_unclear` + `context_insufficient` (la pregunta que el FAQ responde no fue capturada).
- `metric_unit` — **Fable** (R8).

*Confirma el veredicto previo "mixto — ninguno completo".*

### Caso 3 — batch_002
- `metric_type` — **Bloqueado — sin destino en enum**. Hay magnitud (cargo de $273.535,43 COP) pero es un cargo disputado, no el precio de un producto. `price` colapsa capas (R9c); `unknown` no describe. El enum no tiene destino legítimo.
- `uncertainties` — **Fable** (R4). `anecdotal_single_source` + `source_date_unclear`.
- `time_scope_raw` — **Fable** (R6). "casi un mes después de haber comprado; reclamo 'ayer'" — ambos son wording del claim.
- `metric_unit` — **Fable** (R8).

*Cierra el caso que quedó pendiente en la sesión anterior.*

### Caso 4 — batch_004
- `actor_level` — **Fable** (R7). El rol del hablante no es determinable desde el snippet → `unknown` + `actor_level_unclear`. El default contextual de Sonnet (instructor → seller) no está autorizado.
- `metric_type` — **Bloqueado — sin destino en enum**. Conteo de empleados; ningún valor cubre headcount.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Construido** (R4). Unión: `anecdotal_single_source`, `actor_level_unclear`, `methodology_unclear`.
- `time_scope_raw` — **Fable** (R6). "en muy poco tiempo … en año y medio".

### Caso 5 — batch_004
- `actor_level` — **Fable** (R7). Comentarista que relata haber oído de terceros: reporta sin ser parte ni tener interés → `source`.
- `time_scope_raw` — **Fable** (R6). "over the years" es wording del claim; "~2025" es fecha de fuente aproximada y no entra.
- `uncertainties` — **Construido** (R4). Unión: `context_insufficient`, `anecdotal_single_source`, `source_date_unclear`.

*Nota: este caso figuraba entre los residuales de truncamiento, pero ambos codificadores usaron `context_insufficient`. No hay conflicto R4/R10 aquí; cierra por regla.*

### Caso 6 — batch_005
- `uncertainties` — **Fable** (R4). `anecdotal_single_source` + `source_date_unclear`.
- `metric_unit` — **Fable** (R8). "percent commission on sales".
- `metric_value_raw`: Sonnet preserva el comparador de Amazon KDP (30%, umbral $10), Fable lo manda a parser_notes. Sin regla que gobierne dónde vive un comparador. **Sin adjudicación** — ver §Huecos.

*Confirma el veredicto previo.*

### Caso 7 — batch_006
- `uncertainties` — **Construido** (R4). Unión: `anecdotal_single_source`, `author_conflict_of_interest_possible`, `source_date_unclear`. Ninguno de los dos la tenía completa.
- `metric_unit` — **Fable** (R8).

### Caso 8 — batch_007
- `claim_type` — **Fable** (D1). Queja en primera persona en sitio de reseñas → `anecdotal_report`.
- `platforms` — **Sonnet** (R5, sin canonicalizar). Ambas entidades son sujeto del claim; se registra la forma que el snippet sostiene (`revid.ai`, no `Revid`).

### Caso 9 — batch_008
- `uncertainties` — **Fable** (R4). `source_date_unclear` aplica: política de privacidad sin fecha visible.

*Sin cambio respecto al veredicto previo.*

### Caso 10 — batch_008
- `metric_type` — **Bloqueado — sin destino en enum**. Retención fiscal del 30% impuesta por el gobierno de EE.UU. no es un fee de plataforma. `fee_rate` colapsa capas (R9c).
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4).
- `geography_if_explicit` — **Forma** ("US" / "the US").

### Caso 11 — batch_009
- `platforms` — **Construido** (R5). Solo `Payhip` + marca. Facebook, LinkedIn y Slack son canales de difusión mencionados de paso, no sujeto del claim → `local_qualifiers`. Sonnet los incluyó, Fable omitió Payhip; ninguno completo.
- `uncertainties` — **Construido** (R4). Unión: `anecdotal_single_source`, `product_type_unclear`, `source_date_unclear`.
- `time_scope_raw` — **Fable** (R6). "Within 24 hours … By day end".

### Caso 12 — batch_009
- `metric_type` — **Bloqueado — sin magnitud** (R9a). No hay cifra; la periodicidad no es magnitud.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Sonnet** (R4, validado). `source_date_unclear` **no aplica**: el claim trae su propia fecha explícita ("Since February 2024"). Ejemplo de la unión filtrada por aplicabilidad, no ciega.
- `time_scope_raw` — "Since February 2024" (R6, claim de estado con fecha propia).

### Caso 13 — batch_010
- `metric_type` — **Fable** (R9a). La magnitud presente es la suscripción de $20/mes → `price`. `payment_method_availability` describe el claim, no el número.
- `time_scope_raw` — **Fable** (R6). "Before joining Hotmart" es wording del claim; "monthly" es unidad, no alcance temporal.
- `metric_unit` — **Fable** (R8).

### Caso 14 — batch_010
- `claim_type` / `evidence_role` — **Residual**. Cita de creador mediada por periodista.
- `time_scope_normalized_if_safe` — **Fable** (R6). Claim de estado (qué métodos de pago acepta la plataforma) con fecha de publicación explícita → normaliza a 2023-06-19.
- `uncertainties` — **Fable** (R4, validado). `actor_level_unclear` **no aplica**: la hablante está identificada por nombre y rol.

### Caso 15 — batch_014
- `platforms` — **Sonnet** + marca (R5). Kash es la cuenta prepagada de la propia Kichink, mencionada como opción de pago → incidental, va a qualifiers.
- `uncertainties` — **Fable** (R4).

### Caso 16 — batch_015
- `uncertainties` — **Fable** (R4). Fecha de fuente solo con año → `source_date_unclear`.
- `metric_value_raw` — **Sonnet** (R9d). Claim comparativo sin dimensión dominante: las tres cifras (listing $0.20, transacción 6.5%, referral 15%) son el contenido. Preservarlas es correcto.

### Caso 17 — batch_015
- **Fuera de adjudicación — atomicidad.** El snippet mezcla caracterización de marketplace con una cifra de compradores activos; Sonnet leyó la cifra, Fable la caracterización. Es candidato a record que debió partirse, no desacuerdo de `claim_type`.
- **Advertencia registrada:** el corpus no tiene hoy marca de atomicidad — no existe campo ni valor de `uncertainties` que registre "record que debió partirse", ni en el vocabulario ni en los schemas. Si sale a fila propia, sale a una fila sin dónde anotarse.

### Caso 18 — batch_015
- `uncertainties` — **Fable** (R4). Cierra completo.

### Caso 19 — batch_016
- `uncertainties` — **Construido** (R10 invertida + R4). `anecdotal_single_source` + `context_insufficient`. `snippet_needs_reopen` de Fable no es legal en el enum de ER; se sustituye. Ninguno de los dos escribió `context_insufficient`.
- `metric_unit` — **Fable** (R8). "USD balance".

### Caso 20 — batch_016
- `platforms` — **Sonnet** + marca (R5).
- `geography_if_explicit` — **Fable** (R2). "outside the US" es alcance negado, no un lugar determinable → null + `geography_unclear`.
- `uncertainties` — **Fable** (R4).
- `metric_unit` — **Fable** (R8). "percent per payout".

---

## E2 — Casos 21 a 51

### Caso 21 — batch_017
- `claim_type` — **Fable** (D1).
- `uncertainties` — **Fable** (R4). `anecdotal_single_source`.

### Caso 22 — batch_018
- `actor_level` — **Fable** (R7). El texto dice "plataforma muy accesible y segura **para vender**": evidencia textual directa de que habla un vendedor. El `buyer` de Sonnet es error de lectura.
- `evidence_role` — **Fable**. `seller_self_claim` se sigue del actor.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4).

### Caso 23 — batch_018
- `uncertainties` — **Construido** (R10 invertida + R4). `anecdotal_single_source` + `context_insufficient`.
- `platforms` — **Sonnet** + marca (R5).

### Caso 24 — batch_019
- `claim_type` — **Fable** (D1).
- `evidence_role` — **Fable**. `anecdotal_example`: es una instancia personal concreta; `unknown` no está justificado.
- `platforms` — **Sonnet** (R5, sin canonicalizar). El claim es sobre el plan Individual de Envato Elements; se registra al nivel que el record sostiene.
- `uncertainties` — **Fable** (R4).
- `metric_unit` — **Fable** (R8).

### Caso 25 — batch_019
- `evidence_role` — **Residual**. Resumen agregado de reseñas.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4). Unión: `methodology_unclear` + `source_date_unclear`.

### Caso 26 — batch_020
- `claim_type` — **Fable** (D1).
- `metric_type` — **Bloqueado — sin magnitud** (R9a). "3 months" es duración del episodio, no magnitud del sujeto.
- `metric_unit` / `metric_value_raw` — **Fable** (null). Consecuencia de lo anterior.
- `time_scope_raw` — **Fable** (R6). "for 3 months now" es wording temporal del claim.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4).

### Caso 27 — batch_022
- `metric_type` — **Bloqueado — sin magnitud** (R9a). El snippet enuncia tipos de fee sin ninguna cifra. `unknown` de Fable es el valor legal más cercano hoy.
- `platforms` — **Sonnet** + marca (R5).

### Caso 28 — batch_026
- `uncertainties` — **Fable** (R4).

### Caso 29 — batch_026
- `geography_if_explicit` — **Fable** (R2). "el mundo hispano" es descriptor de mercado, no lugar determinable → null + `geography_unclear`.
- `uncertainties` — **Fable** (R4). `source_date_unclear` + `methodology_unclear` (afirmación de desplazamiento de mercado sin cuantificar).

### Caso 30 — batch_026
- `uncertainties` — **Fable** (R4).

### Caso 31 — batch_027
- `metric_type` — **Bloqueado — sin destino en enum**. GMS es volumen transaccionado por terceros; `revenue` es ingreso de la plataforma. Misma unidad, capa económica distinta — el caso testigo de R9(c).
- `time_scope_normalized_if_safe` — **Sonnet** (R6). Es resultado de un periodo (Q4 2025), no claim de estado: la fecha de publicación no lo normaliza. El raw debe cargar el periodo del claim.
- `metric_unit` — **Fable** (R8).
- **Evidencia para la fila de agregación:** nivel (46% de GMS), cambio (creció 6.6% YoY) y share conviven en el mismo campo sin distinción.

### Caso 32 — batch_028
- `metric_type` — **Bloqueado — sin destino en enum**. Shares demográficos de audiencia.
- `time_scope_raw` — **Sonnet** (R6). "March 2026" es la etiqueta del dato, o sea el periodo del claim — no fecha de acceso.
- `uncertainties` — **Fable** (R4). `methodology_unclear`: estimación de SimilarWeb sin método declarado.
- `metric_unit` — **Fable** (R8).

### Caso 33 — batch_029
- `claim_type` — **Fable** (D1).
- `metric_type` — **Construido** (R9a/R9d). Hay magnitudes: $227.05 (precio de suscripción anual) y $75.63 (porción no usada, derivada). Dominante = `price`. `refund_policy` de Sonnet describe el claim, no el número; el `unknown` de Fable ignora dos cifras presentes.
- `metric_value_raw` / `metric_unit` — **Sonnet** en sustancia (las cifras se registran), con denominador a agregar por R8: "USD per year".
- `time_scope_raw` / `time_scope_normalized_if_safe` — **Sonnet** (R6). El claim trae fecha propia explícita.

### Caso 34 — batch_029
- `claim_type` — **Fable** (D1).
- `metric_value_raw` / `metric_unit` — **Sonnet** (R9a, R8). $39/mes es magnitud presente; "USD per month" ya declara denominador.

### Caso 35 — batch_029
- `claim_type` — **Fable** (D1).
- `metric_value_raw` / `metric_unit` — **Sonnet** (R9a, R8). $3 y £3 son magnitudes; unidades mixtas declaradas.
- `time_scope_raw` — **Fable** (R6). "currently" es wording del claim; normalized null por relativo.

### Caso 36 — batch_029
- `metric_type` — **Bloqueado — sin destino en enum**. Límite de tamaño de archivo (5GB) es magnitud sin cobertura.
- `metric_unit` — **Fable** (R8). "GB per file".
- `claim_type` — **Residual-lite**. `policy_statement` vs `availability_statement` para una página de help center que describe qué se soporta. Ver §Huecos.

### Caso 37 — batch_031
- `evidence_role` — **Fable** (D2). Página de marketing de features → `direct_claim`, no `official_policy`.
- `platforms` — **Sonnet** + marca (R5).

### Caso 38 — batch_031
- `metric_type` — **Bloqueado — sin magnitud** (R9a).
- `platforms` — **Construido** (R5). Solo `Etsy` + marca. "payhip template" es etiqueta de categoría de producto, no mención de la plataforma como tal; Payhip queda fuera. Sonnet incluyó Payhip, Fable dejó vacío.
- `product_type_if_explicit` — **Bloqueado**. "payhip template" no tiene destino en el enum. Va con el brazo de recuperación, no con esta adjudicación (ver §Campo roto).

### Caso 39 — batch_031
- `actor_level` — **Sonnet** (R7). Es el escaparate del propio vendedor: quien habla es el seller. `third_party` correspondería a alguien reportando sobre la tienda.
- `claim_type` — **Fable**. Listado con precios visibles → `pricing_statement`.
- `platforms` — **Sonnet** + marca (R5).

### Caso 40 — batch_031
- `metric_type` — **Bloqueado — sin destino en enum**. Conteo de empresas usuarias; `active_buyers` colapsaría empresas con compradores.
- `uncertainties` — **Fable** (R4). `methodology_unclear`: estimación de 6sense.
- `geography_if_explicit` — **Forma**.

### Caso 41 — batch_032
- `metric_type` — **Sonnet en forma, parcialmente bloqueado en contenido** (R9d). Cuatro dimensiones sin dominante → array es la estructura correcta. La legalidad de cada miembro del array depende de la revisión del enum.
- `metric_unit` — **Sonnet** (R8). Mixtas declaradas explícitamente.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4). `methodology_unclear`.

### Caso 42 — batch_032
- `metric_type` — **Sonnet en forma** (R9d). Tabla de distribución sin dominante → array. El descriptor libre de Fable cae con R9(b).
- `time_scope` — **Construido** (R6). `normalized` = 2026-03-21 (claim de estado con fecha de página explícita, Sonnet acierta); `raw` = null (la fecha de página no entra al raw, Fable acierta). Ninguno de los dos lo tiene completo.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4).
- `metric_value_raw` (condensado vs completo) — **Residual**.

### Caso 43 — batch_032
- `evidence_role` — **Residual**. `database_fact` vs `reported_event` para cifra sin atribución en nota de prensa.
- `metric_type` — **Bloqueado — sin destino en enum**. Distribución de compras por dispositivo.
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4). `methodology_unclear`: cifras sin atribución ni método.

### Caso 44 — batch_032
- `claim_type` — **Fable** (D1).
- `platforms` — **Sonnet** + marca (R5).

### Caso 45 — batch_033
- `product_type_if_explicit` — **Bloqueado**. "curso" no tiene destino en el enum. Ver §Campo roto.
- `time_scope_raw` — **Fable** (R6). "há alguns meses" es wording del claim; normalized null por relativo.
- `uncertainties` — **Fable** (R4, validado). `subject_ambiguity` de Sonnet **no aplica**: el sujeto es claro. `anecdotal_single_source` sí.

### Caso 46 — batch_034
- `evidence_role` — **Fable** (D2). Página de categoría de marketplace = copy de plataforma → `direct_claim`.
- `metric_type` — **Bloqueado — sin destino en enum**. Conteo de catálogo (64,100 templates).
- `time_scope_raw` — **Fable** (R6). Fecha de acceso nunca entra → null.
- `platforms` — **Sonnet** + marca (R5).
- `claim_type` — **Residual-lite**. `availability_statement` vs `statistical_data`.

### Caso 47 — batch_038
- `metric_type` — **Bloqueado — sin destino en enum**. Lista de keywords rankeadas.
- `metric_value_raw` — **Fable** (R9d). La lista completa se preserva; el null de Sonnet pierde el contenido.
- `time_scope` — **Construido** (R6). `normalized` = 2026-04-06 (snapshot de ranking = claim de estado, Sonnet acierta); `raw` = null (fecha de post no entra al raw, Fable acierta).
- `platforms` — **Sonnet** + marca (R5).
- `uncertainties` — **Fable** (R4).

### Caso 48 — batch_038
- `actor_level` — **Fable** (R7). Koalanda es proveedor de analítica reportando sobre Etsy: reporta sin ser parte del hecho → `source`.
- `metric_type` — **Bloqueado — sin destino en enum**. Conteo de catálogo rastreado.
- `time_scope_raw` — **Fable en principio** (R6): "currently" es wording del claim. El "(as of access, April 2026)" de Sonnet contamina el campo con fecha de acceso. El calificador "last 30 days" se preserva como segundo elemento.
- `uncertainties` — **Fable** (R4).

### Caso 49 — batch_039
- `time_scope_raw` — **Fable** (R6). "Last updated September 27, 2022" es fecha de página, no entra al raw; sí normaliza (claim de estado sobre qué contiene el reporte).
- `claim_type` — **Residual-lite**. `explicit_claim` vs `availability_statement`.

### Caso 50 — batch_039
- `metric_type` — **Bloqueado — sin destino en enum**. Comisión de afiliado (50%) es dinero pagado *al* partner, no cobrado *por* la plataforma. `fee_rate` colapsa capas (R9c). `payout` de Sonnet describe el mecanismo, no la magnitud.
- `time_scope_raw` — **Fable** (R6). "Undated" no es wording del claim → null.
- `metric_unit` — **Fable** (R8).
- `claim_type` — **Residual-lite**. `pricing_statement` vs `policy_statement`.

### Caso 51 — batch_039
- `metric_type` — **Bloqueado — sin magnitud** (R9a). El snippet describe protección ante chargebacks sin cifra.
- `time_scope_raw` — **Fable** (R6). Fecha de página fuera del raw; normaliza a 2024-04-10 por ser claim de estado.
- `platforms` — **Sonnet** + marca (R5).

---

## E3 — Casos 52 a 60

### Caso 52 — batch_042
- `metric_type` — **Bloqueado — sin magnitud** (R9a). La cláusula establece que existe un fee per-transaction pero no enuncia tasa.
- `uncertainties` — **Sonnet** (R4). `net_vs_gross_ambiguity` aplica: Gumroad Fee deducido del precio del comprador vs Supplier Fee pagado al vendedor son dos lados de la misma resta. Caso invertido — Sonnet aporta lo que Fable no tiene.
- `time_scope_raw` — **Fable** (R6). Effective Date fuera del raw; normaliza a 2025-01-01.

### Caso 53 — batch_042
- `metric_type` — **Bloqueado — sin magnitud** (R9a). No hay calendario concreto.
- `time_scope_raw` — **Fable** (R6). Normaliza a 2025-01-01.

### Caso 54 — batch_042
- `metric_type` — **Bloqueado — sin destino en enum**. Umbral mínimo de payout es una condición, no un monto pagado. `payout` es el vecino más cercano pero otra capa.
- `geography_if_explicit` — **Sonnet** (R2). Thailand y Korea son nombres de lugar explícitos dentro del claim, no inferencia desde moneda.
- `platforms` — **Sonnet** + marca (R5).
- `time_scope_raw` — **Fable** (R6). Normaliza a 2024-07-23.
- `metric_unit` — **Fable** (R8). "mixed: USD, THB, KRW".

### Caso 55 — batch_043
- `evidence_role` — **Residual-lite**. `comparative_commentary` vs `direct_claim` para un forista comparando plataformas que usa.
- `time_scope_raw` — **Fable** (R6). "~2025-05" es fecha de fuente aproximada, no wording del claim → null.
- `uncertainties` — **Fable** (R4, validado). `actor_level_unclear` **no aplica**: el autor está eligiendo plataforma para vender, el rol es determinable. `source_date_unclear` sí, por fecha aproximada.

### Caso 56 — batch_043
- `evidence_role` — **Fable** (D2). Página de comparación contra competidor alojada por la propia plataforma → `direct_claim`.
- `uncertainties` — **Fable** (R4). `author_conflict_of_interest_possible`.
- `time_scope_raw` — **Fable** (R6). "not dated" no es wording del claim → null.
- `metric_unit` — **Fable** (R8).

### Caso 57 — batch_044
- `claim_type` — **Residual**. `explicit_claim` vs `policy_statement` para un email de anuncio.
- `metric_value_raw` — **Sonnet** (null). El texto que Fable puso ahí no es una magnitud.
- `time_scope` — **Sonnet** (R6). El email *es* el claim y su fecha es la fecha del claim: raw = October 16, 2024; normalized = 2024-10-16.
- `platforms`: PayPal se incluye por R5 (actor del hecho, no método de pago incidental). No estaba en disputa.

### Caso 58 — batch_046
- `claim_type` — **Fable** (D1).
- `platforms` — **Sonnet** + marca (R5). "THIS COMPANY" sin nombrar en el snippet, determinable desde el record. Mastercard queda fuera: red de tarjetas, incidental.
- `time_scope` — **Sonnet** (R6). La reseña trae fecha propia.
- `uncertainties` — **Fable** (R4).

### Caso 59 — batch_046
- `claim_type` — **Fable** (D1).
- `metric_value_raw` / `metric_unit` — **Sonnet** (R9a, R8). $17 es magnitud presente.
- `platforms` — **Sonnet** + marca (R5). "chrome" queda fuera: está dentro de la etiqueta del producto.
- `time_scope` — **Sonnet** (R6).
- `uncertainties` — **Fable** (R4).

### Caso 60 — batch_047
- `claim_type` / `evidence_role` — **Residual**. Consejo entre pares en foro.
- `platforms` — **Sonnet** (R5). Reddit, Hacker News y Slack son lugares donde viven links mencionados de paso, no sujeto del claim → qualifiers.
- `time_scope_raw` — **Fable** (R6). Fecha de acceso nunca entra; el post está sin fechar.

---

## Recuento

**Unidad: el caso, clasificado por lo que le queda pendiente.** Las categorías son excluyentes y suman 60. Un caso "con residual" tiene el resto de sus campos cerrados por regla — C42, por ejemplo, cierra `metric_type`, `time_scope`, `platforms` y `uncertainties`, y es residual solo en el formato de `metric_value_raw`.

| Estado del caso | Casos |
|---|---|
| Íntegramente cerrado por regla | 48 |
| Con un campo residual pleno (veredicto del operador) | 6 — C14, C25, C42, C43, C57, C60 |
| Con un campo residual-lite (`claim_type`/`evidence_role` sin cobertura) | 5 — C36, C46, C49, C50, C55 |
| Fuera de adjudicación | 1 — C17 (atomicidad) |

**Bloqueos que impiden escribir, no adjudicar:**

| Motivo | Casos |
|---|---|
| `metric_type` sin magnitud (R9a sin salida legal) | C12, C26, C27, C38, C51, C52, C53 |
| `metric_type` sin destino en enum (R9c) | C3, C4, C10, C31, C32, C36, C40, C43, C46, C47, C48, C50, C54 |
| `metric_type` array, legalidad de miembros pendiente | C41, C42 |
| `product_type_if_explicit` sin destino en enum | C38, C45 |

**Escribibilidad.** Hay dos clases de bloqueo y no se solapan del todo:

| Clase | Casos |
|---|---|
| Schema — `metric_type` (7 sin magnitud + 13 sin destino + 2 array) y `product_type_if_explicit` (C45; C38 cae en ambos) | 23 |
| Autoridad — la marca de R5 depende de `platform_scope_unclear`, aún `phase_2_only` en `pipeline_vocabulary.yaml`, que overridea a los schemas | 26 |
| Intersección | 13 — C4, C10, C12, C26, C27, C38, C41, C42, C43, C46, C47, C51, C54 |
| **Unión — al menos un veredicto no escribible hoy** | **36 (60%)** |
| Libres de ambos bloqueos | 24 |

Las dos clases no cuestan lo mismo de levantar. Completar R3 en el vocabulario —mover `platform_scope_unclear` de `phase_2_only` a `core`, una línea en el archivo de autoridad, reflejando lo que ambos schemas ya aceptan— baja el bloqueo de 36 a 23 casos sin decidir nada sobre el eje de `metric_type`. Los 23 restantes exigen tocar los schemas: rama null, o el rediseño que la sección final plantea.

Lo que sí es escribible hoy en la capa de extraction record, en los casos libres: nulls de tiempo, geografía, unidad y valor, y la unión de `uncertainties` cuando no incluye la marca.

Hay una tercera clase que no entra en esa tabla porque no vive en la capa de extraction record: **bloqueo descendente**. C4 recibe `actor_level` → `unknown` por R7, valor legal en extraction record y en Signal Card, pero ausente del enum de `card_record.actor` en Phase 3 (`buyer, seller, product, marketplace, platform, source, third_party, mixed`). El veredicto se escribe sin problema y muere al cruzar. Es el único de los cinco veredictos de `actor_level` de la muestra que lo hace: C5 y C48 (`source`) y C22 y C39 (`seller`) tienen destino en las tres capas.

No mueve las cifras de arriba —C4 ya está bloqueado por `metric_type` y la unión sigue en 36— pero sí importa para la re-codificación del corpus, donde R7 se aplicaría sin el paraguas de otro bloqueo. Las 29 cards actuales tienen 0 `unknown` en `actor_level`, y ésa es precisamente la condición que les permite mapear a `card_record`. R7 aplicada al corpus produce el primer valor sin destino en el único campo de la llave que Phase 3 ya consume — y lo consume en el filtro que rutea a `rejected_grouping` por `same_actor_discrepancy`. Hoy afecta a 1 caso de 60; escala con la re-codificación.

**Distribución de aciertos** (solo campos con veredicto atribuible a un codificador):

Fable domina en `uncertainties` (R4/R1), `time_scope_raw` (R6) y `metric_unit` (R8). Sonnet domina en `platforms` (R5) y en preservación de magnitudes presentes (R9a). No hay un codificador mejor: **cada uno acertó sistemáticamente en la mitad del esquema que el otro descuidó**, lo cual es el resultado esperado de dos codificadores con criterios formulados en momentos distintos, y es la razón por la que el veredicto correcto es con frecuencia construido y no elegido.

---

## Huecos detectados durante la adjudicación

1. **`claim_type` / `evidence_role` sin regla general.** D1 y D2 cubren dos fronteras; los otros valores del enum no tienen criterio. Cinco casos caen a residual-lite por esta causa estructural, no por rareza individual.
2. **Dónde vive un comparador.** C6, C16: cifras de una plataforma competidora dentro de un claim sobre otra. Un codificador las pone en `metric_value_raw`, el otro en `parser_notes`. Sin regla.
3. **Formato de preservación de bloques.** C42: tabla condensada a extremos vs preservada completa. R9(d) decide el tipo, no la forma del valor.
4. **Marca de atomicidad inexistente.** C17 no tiene dónde registrarse.

## Campo roto que esta adjudicación no toca

`product_type_if_explicit` no valida en 849 de 1,178 records: 642 en `null` (no admitido por el schema) más 207 fuera de enum. Sumando los 326 con `unknown` puesto por `bulk_extract.py:458` **hardcodeado, sin heurística**, el campo está sin poblar en 968 de 1,178 records (82,2%). "Nunca se pobló" es literal. Corregirlo hacia el enum no es corrección sino primera extracción: va con el brazo de recuperación. Los veredictos de C38 y C45 quedan bloqueados a la espera.

## Lo que esta adjudicación deja probado para el rediseño de `metric_type`

De los 22 bloqueos de `metric_type`, quince traen magnitud real (13 sin destino en enum + 2 de array) y trece de esos quince son magnitudes bien capturadas sin lugar donde vivir: conteos de empleados, de catálogo, de empresas; shares demográficos y de dispositivo; volumen transaccionado; umbrales; retenciones fiscales; comisiones a terceros. El enum actual mezcla magnitudes económicas (`fee_rate`, `price`, `revenue`, `payout`) con cosas que no son magnitudes (`search_discovery`, `payout_method_availability`, `activation_requirement`). El problema no es que falten valores: es que el eje del campo no está definido. Ampliar por acumulación reproduciría el desorden; corregir hacia el enum actual forzaría exactamente los colapsos de capa que R9(c) prohíbe.
