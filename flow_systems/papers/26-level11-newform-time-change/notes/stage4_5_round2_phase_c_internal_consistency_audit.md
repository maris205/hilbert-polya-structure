# Paper 26 — Stage 4.5 Round 2 Phase C audit

Registered experiment-backed claims checked: **17/17**. Registered Stage-4-prime protected surfaces checked: **17/17**.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

Fresh read-only execution evidence:

- `python -m unittest discover -s code -p 'test_*.py' -v`: 84 passed, 0 failed.
- verify-only replay tests: 28 passed, 0 failed.
- Existing results, receipts, source locks, and provenance were replayed; canonical results were not regenerated or refreshed.

| claim | exact span occurrence | provenance | verdict |
|---|---:|---|---|
| C-001 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-002 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-003 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-004 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-005 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-006 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-007 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-008 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-009 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-010 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-011 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-012 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-013 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-014 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-015 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-016 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |
| C-017 | 1 | P26-R8-EXACT-TAXONOMY-V1 | VERIFIED |

Failure-mode support: actual test logs/configuration/provenance support CLEAR findings for Modes 1, 3, 5, and 6; this is not an ARS rerun of the original scientific experiments.
