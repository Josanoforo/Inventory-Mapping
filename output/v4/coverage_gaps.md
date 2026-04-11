# Coverage Gaps — v4 (Round 1, 75 cards)

---

## GAP-001
**Gap name:** Perspectiva del comprador ausente del corpus
**Signal IDs that create expectation:** SC-R1-059
**Description:** No se encontraron cards con perspectiva directa del comprador (buyer) en Round 1. La única card con actor=buyer (SC-R1-059) documenta el impacto de reviews desde la perspectiva de un seller, no desde la perspectiva del comprador. El corpus documenta plataforma, sellers, y marketplace, pero no experiencias de compradores (proceso de compra, descarga, acceso a contenido, soporte post-compra, satisfacción).
**Why it limits reading of the inventory:** Múltiples TCs en este corpus (TC-002, TC-003, TC-004, TC-005) documentan fricciones y asimetrías que afectan a compradores (fee de 40% sin refunds en compras in-app, umbral de Discover que limita la visibilidad de productos para compradores, retención de fondos). Sin cards de compradores, no es posible evaluar si las políticas documentadas tienen impacto real en la experiencia del comprador ni en qué dirección. La lectura del inventario está sesgada hacia el lado del vendedor.

---

## GAP-002
**Gap name:** Experiencia de entrega y acceso post-compra desde la perspectiva del comprador
**Signal IDs that create expectation:** SC-R1-022
**Description:** No se encontraron cards que documenten la experiencia del comprador al descargar y acceder a productos comprados en Gumroad. SC-R1-022 documenta el mecanismo de entrega desde la plataforma (formatos requeridos, entrega automática al comprar). Los límites de tamaño de archivo (SC-R1-031, SC-R1-071) y la restricción del botón 'Download all' a 500MB están documentados en platform cards pero sin experiencia del comprador que haya encontrado esos límites.
**Why it limits reading of the inventory:** Las restricciones técnicas de entrega (límites de tamaño, formatos aprobados, botón 'Download all' solo <500MB) están documentadas como policy sin evidencia de su impacto en compradores. No es posible evaluar si estas restricciones generan soporte adicional para sellers ni si afectan la satisfacción del comprador.

---

## GAP-003
**Gap name:** Sellers en geografías con restricciones de payout no documentados
**Signal IDs that create expectation:** SC-R1-024, SC-R1-027, SC-R1-028
**Description:** No se encontraron cards de sellers en países donde las restricciones de payout documentadas (ausencia de direct deposit y PayPal) aplican. El corpus documenta la política de payout restrictiva para ciertas geografías pero no incluye ningún seller-actor card de esas geografías.
**Why it limits reading of the inventory:** La política de payout geográfico (SC-R1-024, SC-R1-027, SC-R1-028) queda sin contraparte humana. No es posible evaluar el alcance real de la exclusión ni el comportamiento de sellers afectados. FRI-003 fue rechazado por same_actor_discrepancy precisamente porque falta esta perspectiva.

---

## GAP-004
**Gap name:** Sellers con outcomes intermedios no documentados en Round 1
**Signal IDs that create expectation:** SC-R1-050, SC-R1-054, SC-R1-060, SC-R1-056, SC-R1-049, SC-R1-062
**Description:** No se encontraron cards de sellers con ingresos en rango intermedio en Round 1. Los seller outcome cards del corpus se concentran en extremos: outcomes muy altos ($61,411 en un año; ~$15,000 en 2025; $50-200/día declarado) o muy bajos/nulos ($139.96 en 3 años; $21 en una semana; zero tráfico). No hay cards de sellers con ingresos moderados entre estos extremos.
**Why it limits reading of the inventory:** La ausencia de casos intermedios limita la lectura del patrón de asimetría distributiva (TC-001, ASY-001). No es posible determinar si la distribución de outcomes es bimodal o simplemente top-heavy/bottom-heavy por efecto de selección de fuente (survivorship bias en casos altos; negativity bias en casos bajos). Esta limitación ya estaba documentada en TC-001's what_is_missing.
