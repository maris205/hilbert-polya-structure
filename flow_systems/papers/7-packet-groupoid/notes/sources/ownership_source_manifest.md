# Paper 7 Deninger-ownership source manifest

Frozen: 2026-08-14 (Asia/Shanghai)  
Scope: the four full texts used by `../source_audit.md`; operator/trace sources
belong to the separate operator-source manifest.

| ID | File | Canonical retrieval URL | Retrieved/verified | Physical pages | PDF SHA-256 | Preflight sidecar SHA-256 | Verdict |
|---|---|---|---|---:|---|---|---|
| `DEN-DYN-v4` | `deninger-dynamical-systems-arithmetic-schemes-v4.pdf` | <https://arxiv.org/pdf/1807.06400v4> | local Paper-2 copy re-hashed and re-preflighted 2026-08-14 | 119 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `e1d48da27567747dd880666d881ddd211021800cdde99c195e5434b114e42626` | `PASS` |
| `DEN-SURVEY-v1` | `deninger-primes-knots-periodic-orbits.pdf` | <https://arxiv.org/pdf/2301.11643v1> | local Paper-2 copy re-hashed and re-preflighted 2026-08-14 | 16 | `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | `74a0ccb32aa1f22ea3b93c3b9fc65b362c8072f4bc7d50526a8d10489a375ff6` | `PASS` |
| `DEN-SHEAF-v1` | `deninger-rational-witt-vectors-associated-sheaves-v1.pdf` | <https://arxiv.org/pdf/2508.05329v1> | acquired and verified 2026-08-14 | 31 | `19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002` | `810b5e253ab86b16e8197ae36efa5ef49889221b0202c94ec3fe2aeae562b75f` | `PASS` |
| `MOR-v5` | `morishita_2025_dynamical_systems_arithmetic_topology_v5.pdf` | <https://arxiv.org/pdf/2508.15971v5> | acquired and verified 2026-08-14 | 26 | `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | `1ca5ab980f477868a0600a8b53c2d04ea2a10e9702973c92e6c8177b8277d75f` | `PASS` |

The sidecars were produced with ARS `pdf_read_preflight/1.0.0` under a
temporary Python environment containing `pypdf`.  For every file, declared,
enumerated, and reader page counts agree and the warning array is empty.

Publisher metadata for the journal manifestation of `DEN-DYN-v4` was checked
at <https://www.sciencedirect.com/science/article/pii/S0019357724000491>:
Indagationes Mathematicae 37(1), January 2026, pp. 25--136,
DOI `10.1016/j.indag.2024.05.007`.  No separate publisher PDF was used for
physical-page locators.

The audit file itself had SHA-256
`a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53`
immediately before this manifest was written.  If the audit is amended, that
hash must be recomputed rather than treated as a permanent self-lock.
