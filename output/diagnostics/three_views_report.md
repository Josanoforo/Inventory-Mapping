# Three Views Diagnostic Report

**Dataset:** `working/data_gathering/findings/` — 1178 findings

## Vista 1 — Plataforma × source_type

*Plataforma inferida del dominio raíz del campo `source`. 'otros' = fuentes externas (Trustpilot, blogs, Medium, etc.)*

| Plataforma    | help_center | blog | buyer_review | article | policy_page | platform_doc | unknown | pricing_page | product_listing | search_results_page | otros st. | Total |
| ------------- | ----------- | ---- | ------------ | ------- | ----------- | ------------ | ------- | ------------ | --------------- | ------------------- | --------- | ----- |
| Domestika     | 28          | —    | —            | —       | 29          | 11           | —       | 5            | 10              | 2                   | 4         | 89    |
| Envato        | 16          | 3    | 5            | —       | 1           | 6            | —       | 4            | —               | 2                   | 2         | 39    |
| Etsy          | 32          | 2    | —            | —       | 29          | 9            | —       | 2            | 2               | 6                   | 9         | 91    |
| Gumroad       | 17          | —    | —            | —       | 11          | 10           | —       | 12           | —               | 5                   | 3         | 58    |
| Hotmart       | 36          | 12   | —            | 5       | 10          | 3            | —       | 6            | 1               | —                   | —         | 73    |
| Kichink       | —           | —    | —            | —       | 20          | 4            | —       | 6            | 6               | 3                   | —         | 39    |
| Lemon Squeezy | 30          | 2    | —            | 1       | —           | 8            | —       | 3            | 5               | —                   | —         | 49    |
| Patreon       | 30          | 13   | —            | —       | —           | 4            | —       | 3            | —               | 1                   | —         | 51    |
| Payhip        | —           | 7    | —            | 10      | —           | 8            | —       | 7            | 14              | 7                   | 52        | 105   |
| otros         | —           | 148  | 111          | 89      | —           | 2            | 63      | 4            | 8               | 18                  | 141       | 584   |
| **TOTAL**     | 189         | 187  | 116          | 105     | 100         | 65           | 63      | 52           | 46              | 44                  | 211       | 1178  |

### Totales de columna (source_type global)

| source_type         | Total findings |
| ------------------- | -------------- |
| help_center         | 189            |
| blog                | 187            |
| buyer_review        | 116            |
| article             | 105            |
| policy_page         | 100            |
| platform_doc        | 65             |
| unknown             | 63             |
| pricing_page        | 52             |
| product_listing     | 46             |
| search_results_page | 44             |
| otros st.           | 211            |
| **TOTAL**           | 1178           |

## Vista 2 — Plataforma × verification_status

*Cada celda: conteo (% del total de esa plataforma). Plataforma = dominio raíz del campo `source`.*

| Plataforma    | direct_verified | blocked_url_index_verified | Total |
| ------------- | --------------- | -------------------------- | ----- |
| Domestika     | 59 (66%)        | 30 (34%)                   | 89    |
| Envato        | —               | 39 (100%)                  | 39    |
| Etsy          | 57 (63%)        | 34 (37%)                   | 91    |
| Gumroad       | 33 (57%)        | 25 (43%)                   | 58    |
| Hotmart       | 65 (89%)        | 8 (11%)                    | 73    |
| Kichink       | —               | 39 (100%)                  | 39    |
| Lemon Squeezy | 1 (2%)          | 48 (98%)                   | 49    |
| Patreon       | 7 (14%)         | 44 (86%)                   | 51    |
| Payhip        | 97 (92%)        | 8 (8%)                     | 105   |
| otros         | 352 (60%)       | 232 (40%)                  | 584   |
| **TOTAL**     | 671 (57%)       | 507 (43%)                  | 1178  |

## Vista 3 — Concentración temática por plataforma (bag-of-words del campo `what`)

*Tokenización: split en no-alfanuméricos, lowercase, tokens ≥4 chars, sin stopwords EN/ES, sin nombres de plataforma. Top 10 términos por plataforma.*

### Domestika (89 findings)

| Término  | Frec. |
| -------- | ----- |
| cursos   | 24    |
| local    | 16    |
| states   | 15    |
| user     | 12    |
| methods  | 12    |
| plus     | 12    |
| currency | 11    |
| exchange | 10    |
| price    | 10    |
| bank     | 10    |

### Envato (39 findings)

| Término   | Frec. |
| --------- | ----- |
| templates | 11    |
| author    | 10    |
| video     | 8     |
| authors   | 7     |
| buyer     | 7     |
| market    | 6     |
| plan      | 6     |
| month     | 6     |
| pricing   | 5     |
| assets    | 5     |

### Etsy (91 findings)

| Término   | Frec. |
| --------- | ----- |
| sellers   | 44    |
| seller    | 31    |
| payoneer  | 21    |
| countries | 16    |
| year      | 16    |
| bank      | 15    |
| orders    | 15    |
| buyers    | 14    |
| deposits  | 13    |
| listing   | 13    |

### Gumroad (58 findings)

| Término   | Frec. |
| --------- | ----- |
| sales     | 18    |
| discover  | 11    |
| design    | 9     |
| paypal    | 9     |
| positions | 9     |
| help      | 8     |
| sale      | 8     |
| product   | 7     |
| states    | 7     |
| filter    | 7     |

### Hotmart (73 findings)

| Término   | Frec. |
| --------- | ----- |
| purchase  | 10    |
| sales     | 10    |
| account   | 10    |
| sale      | 10    |
| dollars   | 9     |
| creators  | 8     |
| bank      | 8     |
| ventas    | 8     |
| productor | 8     |
| users     | 7     |

### Kichink (39 findings)

| Término   | Frec. |
| --------- | ----- |
| tienda    | 18    |
| productos | 11    |
| pago      | 11    |
| tiendas   | 7     |
| página    | 7     |
| comisión  | 5     |
| días      | 5     |
| monto     | 5     |
| muestra   | 5     |
| presenta  | 4     |

### Lemon Squeezy (49 findings)

| Término      | Frec. |
| ------------ | ----- |
| payout       | 21    |
| payouts      | 12    |
| sales        | 10    |
| bank         | 9     |
| seller       | 8     |
| paypal       | 8     |
| additional   | 7     |
| platform     | 7     |
| products     | 7     |
| transactions | 6     |

### Patreon (51 findings)

| Término    | Frec. |
| ---------- | ----- |
| creator    | 26    |
| creators   | 19    |
| payout     | 18    |
| platform   | 15    |
| currency   | 15    |
| positions  | 14    |
| platforms  | 9     |
| processing | 8     |
| standard   | 7     |
| conversion | 6     |

### Payhip (105 findings)

| Término     | Frec. |
| ----------- | ----- |
| products    | 22    |
| product     | 13    |
| pricing     | 12    |
| store       | 12    |
| marketplace | 12    |
| digital     | 10    |
| seller      | 10    |
| buyer       | 10    |
| paypal      | 9     |
| countries   | 9     |

### otros (584 findings)

| Término  | Frec. |
| -------- | ----- |
| buyer    | 172   |
| reports  | 169   |
| seller   | 141   |
| states   | 117   |
| sales    | 81    |
| products | 80    |
| product  | 66    |
| month    | 65    |
| refund   | 61    |
| platform | 59    |
