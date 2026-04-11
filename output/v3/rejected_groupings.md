# Rejected Groupings — v3

Generated from: working/scans_v3/
Date: 2026-04-11

---

## From scan: contradictions

### CON-003 — Fee nominal oficial vs rango efectivo (demoted from needs_audit via pre-build filter — see TC-011 instead)
- **Pattern ID:** CON-003 (consolidated into CON-002 which became TC-011)
- **Signal IDs:** SC-R1-005, SC-R1-032, SC-R1-035, SC-R1-044
- **Reason:** Covered by CON-002 → TC-011. Not a separate grouping.

### CON-004 — Cobertura geográfica 160+ países vs sin método de pago
- **Pattern ID:** CON-004
- **Scan type:** contradictions
- **Signal IDs:** SC-R1-027, SC-R1-024, SC-R1-028
- **Reason:** same_actor_discrepancy — SC-R1-027 actor=platform, SC-R1-024 actor=platform, SC-R1-028 actor=platform. Todos los Signal IDs en ambos polos comparten actor=platform. La plataforma describe tanto su cobertura de aceptación como sus limitaciones de payout en el mismo actor.

### CON-003 — Política de reembolso web vs app (ventas finales)
- **Pattern ID:** CON-003
- **Scan type:** contradictions
- **Signal IDs:** SC-R1-034, SC-R1-038
- **Reason:** same_actor_discrepancy — SC-R1-034 actor=platform, SC-R1-038 actor=platform. Ambos polos son actor=platform describiendo políticas de dos canales distintos del mismo actor.

---

## From scan: asymmetries

### ASY-001 — Seller outcomes altos vs bajos en Gumroad
- **Pattern ID:** ASY-001
- **Scan type:** asymmetries
- **Signal IDs:** SC-R1-050, SC-R1-060, SC-R1-051, SC-R1-056, SC-R1-054, SC-R1-039
- **Reason:** same_actor_discrepancy — todos los Signal IDs tienen actor=seller. Además, TC-001 ya cubre la asimetría distributiva de seller income.

### ASY-002 — Fees por canal (10% vs 30% vs 40%)
- **Pattern ID:** ASY-002
- **Scan type:** asymmetries
- **Signal IDs:** SC-R1-005, SC-R1-006, SC-R1-036, SC-R1-038, SC-R1-032, SC-R1-035
- **Reason:** same_actor_discrepancy — todos los Signal IDs tienen actor=platform. La asimetría de fees por canal está documentada completamente por el mismo actor.

### ASY-004 — Payout disponible vs no disponible según geografía
- **Pattern ID:** ASY-004
- **Scan type:** asymmetries
- **Signal IDs:** SC-R1-011, SC-R1-024, SC-R1-025, SC-R1-028
- **Reason:** same_actor_discrepancy — todos los Signal IDs tienen actor=platform. La asimetría geográfica de payout está documentada completamente por el mismo actor.

---

## From scan: frictions

### FRI-001 — Fee 40% en app móvil como fricción de canal
- **Pattern ID:** FRI-001
- **Scan type:** frictions
- **Signal IDs:** SC-R1-036, SC-R1-038, SC-R1-005, SC-R1-047, SC-R1-061
- **Reason:** same_actor_discrepancy para el mecanismo bloqueador — SC-R1-036 actor=platform, SC-R1-038 actor=platform. No hay card de seller documentando específicamente el impacto del canal app. SC-R1-047 y SC-R1-061 se refieren a fees en general, no al canal app.

### FRI-003 — Límite de Download All (500 MB)
- **Pattern ID:** FRI-003
- **Scan type:** frictions
- **Signal IDs:** SC-R1-031, SC-R1-038
- **Reason:** same_actor_discrepancy — SC-R1-031 actor=platform, SC-R1-038 actor=platform. No hay card cross-actor que documente el impacto del límite en compradores.

### FRI-005 — Cobertura de aceptación vs ausencia de payout en algunos países
- **Pattern ID:** FRI-005
- **Scan type:** frictions
- **Signal IDs:** SC-R1-024, SC-R1-028, SC-R1-027
- **Reason:** same_actor_discrepancy — SC-R1-024 actor=platform, SC-R1-028 actor=platform, SC-R1-027 actor=platform. El bloqueador y el bloqueado están documentados por el mismo actor.

---

## From scan: co_occurrences

### COO-002 — Co-ocurrencia de cards sobre fees de Gumroad
- **Pattern ID:** COO-002
- **Scan type:** co_occurrences
- **Signal IDs:** SC-R1-005, SC-R1-006, SC-R1-007, SC-R1-032, SC-R1-035, SC-R1-036, SC-R1-038, SC-R1-044, SC-R1-047, SC-R1-061
- **Reason:** Co-ocurrencia sin pregunta DT nueva. La variación de fees por canal ya está cubierta en TCs existentes. No es frecuencia con fricción propia.

---

## From scan: lexical_overlap

### LEX-001 — Cards sobre fee 10% desde múltiples fuentes
- **Pattern ID:** LEX-001
- **Scan type:** lexical_overlap
- **Signal IDs:** SC-R1-005, SC-R1-032, SC-R1-035, SC-R1-047
- **Reason:** Mismo hecho (10% fee) desde fuentes distintas. Possible dedup: SC-R1-032 y SC-R1-035 cubren el mismo artículo de help center. Sin fricción explícita entre cards.

### LEX-002 — Cards sobre fee 40% en app desde dos artículos distintos
- **Pattern ID:** LEX-002
- **Scan type:** lexical_overlap
- **Signal IDs:** SC-R1-036, SC-R1-038
- **Reason:** Mismo dato (40% fee en app) desde dos artículos de help center distintos. Señal de deduplicación. Sin fricción entre cards.

### LEX-003 — Cards sobre restricciones de payout desde múltiples artículos de help center
- **Pattern ID:** LEX-003
- **Scan type:** lexical_overlap
- **Signal IDs:** SC-R1-024, SC-R1-025, SC-R1-028
- **Reason:** Tres artículos de help center sobre el mismo tema (restricciones de payout geográfico). Sin fricción entre ellas. Señal de deduplicación.

### LEX-004 — Overlap léxico entre docs de Discover y experiencias de seller
- **Pattern ID:** LEX-004
- **Scan type:** lexical_overlap
- **Signal IDs:** SC-R1-069, SC-R1-073, SC-R1-074, SC-R1-055, SC-R1-062
- **Note:** Este patrón fue detectado como tension_candidate (fricción explícita entre cards de platform y seller). Fue mergeado con CON-001 para producir TC-002. Registrado aquí como referencia de deduplicación.
- **Reason para no producir TC separado:** >70% de overlap con CON-001, mismo mecanismo (Discover eligibility contradiction). Consolidado en TC-002.

### LEX-005 — Cards de seller outcomes en Gumroad (mismo territorio, outcomes dispares)
- **Pattern ID:** LEX-005
- **Scan type:** lexical_overlap
- **Signal IDs:** SC-R1-050, SC-R1-060, SC-R1-056
- **Reason:** Mismo territorio (seller outcomes auto-reportados en Gumroad) sin fricción entre las cards. Asimetría distributiva ya cubierta en TC-001. Possible dedup con TC-001.

### LEX-006 — Cards sobre refund/chargeback y control de Gumroad
- **Pattern ID:** LEX-006
- **Scan type:** lexical_overlap
- **Signal IDs:** SC-R1-016, SC-R1-018, SC-R1-034, SC-R1-037
- **Reason:** Mismo territorio (control de Gumroad sobre reembolsos/chargebacks) desde fuentes distintas. Todos actor=platform. Señal de deduplicación: SC-R1-018 (ToS), SC-R1-034 y SC-R1-037 (help center) cubren el mismo mecanismo.

---

## From scan: opposite_directions

### OPP-003 — Mecanismos de plataforma para aumentar ventas vs incertidumbre de seller para empezar
- **Pattern ID:** OPP-003
- **Scan type:** opposite_directions
- **Signal IDs:** SC-R1-033, SC-R1-074, SC-R1-058
- **Reason:** Polo B (SC-R1-058, actor=seller) tiene soporte de una sola card. Insuficiente para establecer una dirección opuesta documentada. Demotido por polo seller con 1 card.

---

## Pre-build filter results

### Needs-audit patterns processed:
- **CON-002** (contradictions, needs_audit): 4 Signal IDs — passed filter. Built as TC-011 with "minimal support" for Polo B noted in classification_risk. Source: contradictions scan, Polo B has 1 card (actor=source).

### Count verification:
- needs_audit patterns received: 1 (CON-002)
- Passed pre-build filter and built as TC: 1 (TC-011)
- Written to rejected_groupings by filter: 0
- Total: 1 = 1 ✓
