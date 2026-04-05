# Rejected Groupings

Patterns routed as rejected_grouping during the scanner pass over 1,560 Signal Cards. Each entry records the pattern, the reason for rejection, and the signal IDs involved.

Rejected groupings are patterns where co-occurrence frequency or lexical overlap was detected but no mechanical tension, friction, or structural gap was found between the co-occurring elements.

---

## COO-007 — Etsy fee accumulation (listing + transaction + payment + Offsite Ads)

**Pattern ID**: COO-007
**Scan type**: co_occurrences
**Rounds covered**: 9 rounds distintos (111 cards)

**Description**: co-ocurre en 9 rounds distintos (111 cards): Etsy fee accumulation (listing + transaction + payment + Offsite Ads).

**Reason for rejection**: Frecuencia de cards sobre el mismo tema sin fricción detectable entre ellas. Las 111 cards documentan la estructura de tarifas de Etsy desde múltiples ángulos (plataforma, vendedor, buyer), pero la co-ocurrencia es de cobertura temática, no de tensión mecánica. La fricción de tarifas Etsy está cubierta en TC-038 (FRI-003) y TC-066 (FRI-032) con evidencia más específica.

**Signal IDs (111 cards)**:
SC-R1-024, SC-R1-025, SC-R1-027, SC-R2-001, SC-R2-002, SC-R2-003, SC-R2-005, SC-R2-008, SC-R2-010, SC-R2-013, SC-R2-014, SC-R2-015, SC-R2-016, SC-R2-017, SC-R2-018, SC-R2-020, SC-R2-022, SC-R2-023, SC-R2-025, SC-R2-063, SC-R2-089, SC-R2-093, SC-R2-098, SC-R2-100, SC-R2-101, SC-R2-107, SC-R3-012, SC-R3-023, SC-R3-028, SC-R3-029, SC-R3-030, SC-R3-042, SC-R3-044, SC-R3-045, SC-R3-053, SC-R3-060, SC-R3-069, SC-R3-070, SC-R3-071, SC-R3-109, SC-R3-119, SC-R3-120, SC-R3-121, SC-R3-122, SC-R3-124, SC-R3-129, SC-R3-132, SC-R3-134, SC-R4-013, SC-R4-014, SC-R4-023, SC-R4-025, SC-R4-031, SC-R4-033, SC-R4-050, SC-R4-051, SC-R4-070, SC-R4-071, SC-R4-072, SC-R4-105, SC-R4-106, SC-R4-118, SC-R4-123, SC-R5-067, SC-R6-014, SC-R6-016, SC-R6-035, SC-R6-071, SC-R6-076, SC-R6-084, SC-R6-089, SC-R6-116, SC-R6-128, SC-R6-132, SC-R6-135, SC-R6-146, SC-R7-143, SC-R7-146, SC-R8-001, SC-R8-002, SC-R8-003, SC-R8-004, SC-R8-005, SC-R8-006, SC-R8-007, SC-R8-008, SC-R8-009, SC-R8-012, SC-R8-013, SC-R8-014, SC-R8-015, SC-R8-016, SC-R8-109, SC-R8-112, SC-R8-126, SC-R8-148, SC-R8-152, SC-R8-157, SC-R8-181, SC-R8-182, SC-R8-183, SC-R9-004, SC-R9-019, SC-R9-020, SC-R9-047, SC-R9-048, SC-R9-062, SC-R9-063, SC-R9-064, SC-R9-101, SC-R9-142

---

## LEX Patterns (needs_audit — lexical overlap)

The following 44 lexical overlap patterns (LEX-001 through LEX-044) were routed as `needs_audit` by the lexical overlap scanner. These patterns document co-occurrence of figures (dollar amounts, percentages, time ranges) across cards from different rounds.

All LEX patterns require human audit to verify whether the cards co-occurring around the same figure share the same source or are independent evidence. They do not constitute tension candidates and are not included in the tension candidate output.

| Pattern ID | Figure | Platform context | Cards | Rounds | Reason |
|------------|--------|-----------------|-------|--------|--------|
| LEX-001 | $250 | Gumroad | SC-R1-014, SC-R4-108 | 2 | <3 IDs — insufficient support |
| LEX-002 | $2.50 | Etsy | SC-R1-023, SC-R4-119 | 2 | <3 IDs — insufficient support |
| LEX-003 | $0.20 | Etsy | SC-R1-024, SC-R2-063, SC-R4-105, SC-R5-067, SC-R6-116, SC-R8-001 | 6 | 3+ IDs — lexical overlap without explicit friction |
| LEX-004 | 6.5% | Etsy | SC-R1-024, SC-R2-063, SC-R4-050, SC-R4-105, SC-R5-067, SC-R6-116, SC-R8-002, SC-R8-004, SC-R8-012, SC-R8-182 | 6 | 3+ IDs — lexical overlap without explicit friction |
| LEX-005 | , sales | Etsy | SC-R2-014, SC-R2-022 | 1 | <3 IDs — insufficient support |
| LEX-006 | $0.25 | Etsy | SC-R2-063, SC-R5-067, SC-R6-116, SC-R8-003 | 4 | 3+ IDs — lexical overlap without explicit friction |
| LEX-007 | 6 months | Etsy | SC-R2-066, SC-R2-068, SC-R3-044, SC-R4-020, SC-R4-033, SC-R6-103 | 4 | 3+ IDs — lexical overlap without explicit friction |
| LEX-008 | $280,000 | Etsy | SC-R2-070, SC-R2-092 | 1 | <3 IDs — insufficient support |
| LEX-009 | $25, | Etsy | SC-R2-071, SC-R6-081 | 2 | <3 IDs — insufficient support |
| LEX-010 | 30 templates | Etsy | SC-R2-072, SC-R6-099 | 2 | <3 IDs — insufficient support |
| LEX-011 | $29.99 | Gumroad | SC-R10-019, SC-R10-038, SC-R2-078 | 2 | 3+ IDs — lexical overlap without explicit friction |
| LEX-012 | $17.93 | Etsy | SC-R3-037, SC-R3-056 | 1 | <3 IDs — insufficient support |
| LEX-013 | $68.95 | Etsy | SC-R3-056, SC-R3-065 | 1 | <3 IDs — insufficient support |
| LEX-014 | $2,000 | Notion | SC-R4-011, SC-R5-098 | 2 | <3 IDs — insufficient support |
| LEX-015 | 12 months | Notion | SC-R4-011, SC-R5-113 | 2 | <3 IDs — insufficient support |
| LEX-016 | 10/month | Etsy | SC-R4-014, SC-R8-010 | 2 | <3 IDs — insufficient support |
| LEX-017 | 1,000 sales | Etsy | SC-R4-017, SC-R8-128 | 2 | <3 IDs — insufficient support |
| LEX-018 | $500 | Etsy | SC-R4-018, SC-R6-080 | 2 | <3 IDs — insufficient support |
| LEX-019 | $10k | Notion | SC-R4-027, SC-R5-117 | 2 | <3 IDs — insufficient support |
| LEX-020 | $5,000/month. | Etsy | SC-R4-034, SC-R6-080 | 2 | <3 IDs — insufficient support |
| LEX-021 | 18 months | Etsy | SC-R4-034, SC-R6-102 | 2 | <3 IDs — insufficient support |
| LEX-022 | $1,500 | Etsy | SC-R4-044, SC-R9-023 | 2 | <3 IDs — insufficient support |
| LEX-023 | $400 | Etsy | SC-R4-064, SC-R4-135 | 1 | <3 IDs — insufficient support |
| LEX-024 | $5,000 | Etsy | SC-R4-065, SC-R6-083, SC-R8-065 | 3 | 3+ IDs — lexical overlap without explicit friction |
| LEX-025 | $2,000 | Gumroad | SC-R4-067, SC-R8-107 | 2 | <3 IDs — insufficient support |
| LEX-026 | $200 | Gumroad | SC-R4-079, SC-R8-191 | 2 | <3 IDs — insufficient support |
| LEX-027 | $99/month) | Gumroad | SC-R4-082, SC-R5-071 | 2 | <3 IDs — insufficient support |
| LEX-028 | 99/month | Payhip | SC-R10-016, SC-R10-017, SC-R4-082, SC-R8-042 | 3 | 3+ IDs — lexical overlap without explicit friction |
| LEX-029 | $0.30 | Gumroad | SC-R10-010, SC-R4-083, SC-R7-066, SC-R8-024 | 4 | 3+ IDs — lexical overlap without explicit friction |
| LEX-030 | $0.30 | Payhip | SC-R4-083, SC-R8-043 | 2 | <3 IDs — insufficient support |
| LEX-031 | 3 years | Etsy | SC-R4-125, SC-R6-088, SC-R8-070 | 3 | 3+ IDs — lexical overlap without explicit friction |
| LEX-032 | $0.40 | Notion | SC-R5-024, SC-R8-028, SC-R8-033 | 2 | 3+ IDs — lexical overlap without explicit friction |
| LEX-033 | $0.50 | Gumroad | SC-R10-007, SC-R10-009, SC-R5-048, SC-R5-059, SC-R8-017, SC-R8-021 | 3 | 3+ IDs — lexical overlap without explicit friction |
| LEX-034 | $250 | Notion | SC-R5-093, SC-R8-139 | 2 | <3 IDs — insufficient support |
| LEX-035 | $500 | Notion | SC-R5-100, SC-R5-116 | 1 | <3 IDs — insufficient support |
| LEX-036 | $1,000 | Notion | SC-R5-104, SC-R5-110 | 1 | <3 IDs — insufficient support |
| LEX-037 | 000/month | Notion | SC-R5-110, SC-R5-123 | 1 | <3 IDs — insufficient support |
| LEX-038 | $7.22 | Etsy | SC-R6-001, SC-R6-069 | 1 | <3 IDs — insufficient support |
| LEX-039 | 1.4k reviews | Etsy | SC-R6-013, SC-R6-075 | 1 | <3 IDs — insufficient support |
| LEX-040 | 238 reviews | Etsy | SC-R6-019, SC-R6-089 | 1 | <3 IDs — insufficient support |
| LEX-041 | $9.99 | Canva | SC-R6-031, SC-R6-042 | 1 | <3 IDs — insufficient support |
| LEX-042 | $6.27 | Canva | SC-R6-041, SC-R6-072 | 1 | <3 IDs — insufficient support |
| LEX-043 | 29/month | Canva | SC-R6-057, SC-R6-059 | 1 | <3 IDs — insufficient support |
| LEX-044 | 000/month | Canva | SC-R6-080, SC-R6-096, SC-R6-112 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-045 | 3 years | Canva | SC-R6-088, SC-R6-093 | 1 | <3 IDs — insufficient support |
| LEX-046 | $1,000 | Canva | SC-R6-096, SC-R6-112 | 1 | <3 IDs — insufficient support |
| LEX-047 | 30 templates | Canva | SC-R6-099, SC-R6-112 | 1 | <3 IDs — insufficient support |
| LEX-048 | $19,000+/month | Etsy | SC-R6-100, SC-R6-101 | 1 | <3 IDs — insufficient support |
| LEX-049 | $35,000 | Canva | SC-R6-108, SC-R6-111 | 1 | <3 IDs — insufficient support |
| LEX-050 | $500/month | Canva | SC-R6-110, SC-R6-112, SC-R6-114, SC-R6-115 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-051 | $200 | Canva | SC-R6-114, SC-R6-115 | 1 | <3 IDs — insufficient support |
| LEX-052 | 130,000 prompts | PromptBase | SC-R7-003, SC-R7-004 | 1 | <3 IDs — insufficient support |
| LEX-053 | $1.99 | PromptBase | SC-R7-005, SC-R7-008, SC-R7-011, SC-R7-014 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-054 | $9.99 | PromptBase | SC-R7-005, SC-R7-008, SC-R7-011 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-055 | $4.99 | PromptBase | SC-R7-006, SC-R7-007, SC-R7-009, SC-R7-010, SC-R7-012, SC-R7-013, SC-R7-095 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-056 | $2.99 | PromptBase | SC-R7-007, SC-R7-010, SC-R7-013, SC-R7-017, SC-R7-098 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-057 | $3.99 | PromptBase | SC-R7-007, SC-R7-010, SC-R7-013, SC-R7-095, SC-R7-100 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-058 | $5.99 | PromptBase | SC-R7-007, SC-R7-010, SC-R7-013, SC-R7-017 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-059 | $6.99 | PromptBase | SC-R7-007, SC-R7-010, SC-R7-013 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-060 | 11,000 users | PromptBase | SC-R7-022, SC-R7-025 | 1 | <3 IDs — insufficient support |
| LEX-061 | 3 prompts | PromptBase | SC-R7-033, SC-R7-035, SC-R7-095 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-062 | $29+. | Gumroad | SC-R7-056, SC-R7-058 | 1 | <3 IDs — insufficient support |
| LEX-063 | $185M | Gumroad | SC-R7-062, SC-R7-064 | 1 | <3 IDs — insufficient support |
| LEX-064 | 2.9% | Gumroad | SC-R7-066, SC-R8-167 | 2 | <3 IDs — insufficient support |
| LEX-065 | $16.5 | Gumroad | SC-R7-068, SC-R7-072 | 1 | <3 IDs — insufficient support |
| LEX-066 | $100M | Gumroad | SC-R7-070, SC-R7-074 | 1 | <3 IDs — insufficient support |
| LEX-067 | 2 months | Gumroad | SC-R10-148, SC-R7-101 | 2 | <3 IDs — insufficient support |
| LEX-068 | 2.5% | Etsy | SC-R8-008, SC-R8-012 | 1 | <3 IDs — insufficient support |
| LEX-069 | 3.5% | Gumroad | SC-R10-010, SC-R8-024 | 2 | <3 IDs — insufficient support |
| LEX-070 | 29/month | Payhip | SC-R10-016, SC-R10-017, SC-R8-042 | 2 | 3+ IDs — lexical overlap without explicit friction |
| LEX-071 | 10 sales | Etsy | SC-R8-068, SC-R8-128 | 1 | <3 IDs — insufficient support |
| LEX-072 | 30 days | Gumroad | SC-R8-082, SC-R8-172, SC-R8-173, SC-R9-066 | 2 | 3+ IDs — lexical overlap without explicit friction |
| LEX-073 | $9.99 | Amazon | SC-R10-001, SC-R10-003, SC-R10-028 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-074 | $39/month | Shopify | SC-R10-011, SC-R10-014 | 1 | <3 IDs — insufficient support |
| LEX-075 | $29/month | Payhip | SC-R10-016, SC-R10-017 | 1 | <3 IDs — insufficient support |
| LEX-076 | $39.99 | Gumroad | SC-R10-019, SC-R10-038, SC-R10-056 | 1 | 3+ IDs — lexical overlap without explicit friction |
| LEX-077 | 30 Days | Gumroad | SC-R10-038, SC-R10-142 | 1 | <3 IDs — insufficient support |
