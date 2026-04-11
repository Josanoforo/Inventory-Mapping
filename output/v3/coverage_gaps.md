# Coverage Gaps — v3

Generated from: working/scans_v3/gaps.json
Date: 2026-04-11

---

## GAP-001 — Perspectiva de buyer prácticamente ausente

**Description:** El corpus de 75 cards tiene 1 sola card con actor=buyer (SC-R1-059). Las 74 cards restantes son de actores platform (47), seller (20), marketplace (4) y source (3). La perspectiva del comprador está prácticamente ausente.

**Reference cards (create the expectation):**
- SC-R1-059 (Única card con actor=buyer: blog documenta que sistema de ratings de Gumroad es público y una reseña 1-estrella degrada confianza del comprador)
- SC-R1-040 (Blog/source: screenshots de dashboard de Gumroad pueden ser manipulados — relevante para confianza del buyer)

**How this limits the inventory:**
Con solo 1 card de buyer, no se puede evaluar si las fricciones documentadas por sellers se traducen en problemas para compradores, ni si el diseño de la experiencia de compra tiene tensiones propias. Afecta interpretación de COO-004 (confianza) y cualquier análisis de post-purchase.

---

## GAP-002 — Ausencia de experiencia post-compra del buyer

**Description:** No se encontraron cards sobre proceso de descarga de producto digital desde la perspectiva del comprador, acceso a contenido después de la compra, o problemas de acceso post-compra.

**Reference cards (create the expectation):**
- SC-R1-031 (Gumroad help center: botón 'Download all' disponible solo cuando contenido < 500 MB; límites de tamaño por tier de precio)
- SC-R1-038 (Gumroad help center Discover app: ventas en app finales, sin reembolsos; proceso de acceso post-compra en app no documentado desde buyer)

**How this limits the inventory:**
No se puede evaluar si la limitación del botón 'Download all' a 500 MB genera problemas reales para compradores. Condiciona el alcance de TC-004 y cualquier análisis de experiencia de usuario post-compra.

---

## GAP-003 — Ausencia de datos comparativos con plataformas alternativas

**Description:** No se encontraron cards sobre plataformas alternativas a Gumroad con suficiente detalle comparativo. El corpus es casi exclusivamente sobre Gumroad.

**Reference cards (create the expectation):**
- SC-R1-057 (Blog: comparación entre dos plataformas no nombradas; ahorro de 30 centavos/venta y 5% en fees)
- SC-R1-061 (Seller blog: comparación con Lemon Squeezy; seller migró por fees percibidos como altos en Gumroad)

**How this limits the inventory:**
La concentración del corpus en Gumroad limita la evaluación de si las tensiones detectadas (fees, visibilidad, soporte) son específicas de Gumroad o patrones del mercado de plataformas de productos digitales. Afecta interpretación de TC-003 (asimetría Discover) y TC-011 (fees).

---

## GAP-004 — Ausencia de experiencias de sellers con moderación de contenido

**Description:** No se encontraron cards documentando sellers que hayan experimentado eliminación de productos, cambio de elegibilidad, o disputa de moderación en Gumroad. Las políticas están documentadas pero no las experiencias de activación.

**Reference cards (create the expectation):**
- SC-R1-012 (Gumroad policy: productos prohibidos por ley federal US, normas de redes de tarjetas, o procesadores)
- SC-R1-013 (Gumroad policy: item #19 prohíbe criptomonedas, NFTs y créditos digitales)
- SC-R1-014 (Gumroad policy: cambios en lista de prohibidos abruptos y sin aviso; efecto inmediato)
- SC-R1-016 (Gumroad ToS: discreción exclusiva de Gumroad para cambiar categorías elegibles en cualquier momento)

**How this limits the inventory:**
Limita la evaluación de TC-005: no se puede determinar si la fricción de cambio abrupto de reglas es teórica (solo política) o real (experimentada por sellers). El mecanismo está documentado pero sin instancias de activación.

---

## GAP-005 — Ausencia de datos de onboarding estructurado de nuevos sellers

**Description:** No se encontraron cards sobre tiempo hasta primera venta para nuevos sellers, tasa de conversión de setup a venta activa, o proceso de soporte durante la fase inicial.

**Reference cards (create the expectation):**
- SC-R1-055 (Seller: sin primera venta, sin exposición en Discover)
- SC-R1-058 (Seller: no ha ganado confianza para vender; incertidumbre sobre precio como barrera)
- SC-R1-051 (Seller: ~$21 en primera semana en Gumroad)

**How this limits the inventory:**
La ausencia de datos de onboarding estructurado limita la interpretación de TC-006 (facilidad de entrada vs dificultad de tráfico) y TC-002 (Discover visibility). No se puede determinar qué proporción de sellers pasan del setup a la primera venta ni en qué timeframe.

---

## GAP-006 — Ausencia de perspectiva hispanohablante

**Description:** No se encontraron cards sobre sellers hispanohablantes o el mercado hispanohablante de productos digitales en Gumroad. El corpus es en inglés con perspectiva de mercado angloparlante.

**Reference cards (create the expectation):**
- SC-R1-065 (Gumroad homepage Discover: lista de categorías/tags disponibles — sin representación hispanohablante identificada)
- SC-R1-067 (Gumroad Discover: 1.6 millones de productos en catálogo — distribución por idioma desconocida)

**How this limits the inventory:**
Sin cards de sellers hispanohablantes, no se puede evaluar si las barreras documentadas (fees, visibilidad, payout geográfico) operan de forma diferente en el mercado hispanohablante. Limita la generalización de las tensiones encontradas.
