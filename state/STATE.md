# STATE.md

Generado: 2026-08-05T20:49:36Z (UTC), sobre HEAD `c3ea50f38e570b45efed92c49f4e1abbb2c24a06`.

Snapshot mecánico. Regenerado automáticamente por `.github/workflows/state-snapshot.yml` en cada push. Sin juicio, sin narrativa — solo lo que es extraíble determinísticamente de git, el ledger y los manifests del repo.

## main

- SHA: `c3ea50f3`

## Ramas remotas con commits en origin

- `preserve/benchmark-etapa2-extraccion-juicio` — 2026-07-31T20:16:52Z — Etapa 2 fable: checkpoint_0006 final (1178/1178) + criterios K15-K16, manifest complete
- `preserve/benchmark-etapa2-reextraccion-campos` — 2026-07-30T07:06:04Z — Etapa 2: re-extracción independiente de campos de juicio (48/48 batches)
- `preserve/benchmark-etapa2-field-extraction` — 2026-07-30T06:02:23Z — Etapa 2: complete final batches 041-048 (1178/1178 processed)
- `legacy/s12-im-artifacts` — 2026-07-29T23:05:05Z — Restore legacy IM artifacts from preserve/s12-round1-75-cards (evidence only)
- `preserve/s12-round1-75-cards` — 2026-04-11T02:44:14Z — Add same-actor filter to scanners and actor composition block to builder
- `preserve/s12-round1-orphan-chain` — 2026-04-10T20:07:48Z — G1: generate signal_cards_round_1.md from 75 Signal Cards

## Ledger (`state/pendientes_ledger.md`)

- Grupo A (abiertas): 14
- Grupo B (abiertas): 48
- Grupo C (abiertas): 9
- Grupo D (abiertas): 0
- Total abiertas: 71
- Parqueadas: 10

## Procesos largos en curso (re-extracción)

- `origin/preserve/benchmark-etapa2-extraccion-juicio` (`working_reextraction/fable/manifest.json`): status=complete, batch alcanzado=batch_048
- `origin/preserve/benchmark-etapa2-field-extraction` (`working_reextraction/sonnet/manifest.json`): status=complete, batch alcanzado=batch_048 final
- `origin/preserve/benchmark-etapa2-reextraccion-campos` (`working_reextraction/fable/manifest.json`): status=complete, batch alcanzado=batch_048
