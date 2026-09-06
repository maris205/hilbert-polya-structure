# C403 paper plan: regular-variation limits for divisibility Gram matrices

Date: 2026-09-05. Status: authorized manuscript implementation of the single
contract frozen in `../BATCH_PLAN.md`; not a new theorem-discovery round.

## Exact question and scope

For `sigma<1/2`, `rho=1-2sigma`, and positive measurable slowly varying
`L:[1,infinity)->(0,infinity)` bounded above and away from zero on compact
intervals, set `a(k)=k^(-sigma)L(k)` and let `T_N` be the zero-extended
divisibility matrix with entry `a(r/m)` when `m|r<=N`. Prove that
`rho T_N^*T_N/(N^rho L(N)^2)` converges to the classical LCM kernel
`E_sigma(m,n)=(mn)^sigma/lcm(m,n)` in every Schatten ideal `S_q` exactly
when `q rho>1`, including `0<q<1`. Below or at the threshold the difference
is not in the ideal for any finite `N`.

This is one paper. Uniform `N`-independent spectral tails and normalized
singular-value consequences support that question; they are not separate
contracts. No claim about target Euler factors, root numbers, zeta zeros,
automorphy, or a Hilbert--Polya realization is made.

## Frozen inputs

| Input | SHA-256 |
|---|---|
| `PROOF_PACKAGE.md` | `0f8e436657de4207087137502236b2d48f69dae947f368b5d586039b7a282fee` |
| `CONTRACT_SCOUT.md` | `4735232a16d895dab8c450416a9dbbc22863e61293b1b60adbf48b580771d493` |
| `SOURCE_AUDIT.md` | `3f21874bdc23d8fe70fb7b0b15708a25782b3564750d8775e01908f0a139c64e` |
| `../reviews/SPECTRAL_REGULAR_VARIATION_REVIEW.md` | `3c1de5f3a52d0e0249459343cab00329609fbad72c6a52e4190fb4464f9c0f10` |
| `../BATCH_PLAN.md` | `7531976dcfe2464bc8018f8f31b9b35a502044623f40242aecf4ae3dc832536c` |

The original three lane files and independent review are read-only inputs.
The manuscript corrects the proof package's descriptive phrase
"period-independent" to "N-independent" without changing the frozen file.

## Claims, dependencies, and ownership

| Manuscript claim | Required argument | Ownership boundary |
|---|---|---|
| Full nonmultiplicative slowly varying family and exact ideal range | Exact Gram identity; uniform Potter estimate; truncated Riemann sums; positive congruence; finite-head/tail norm convergence; singular-value dominated convergence | The manuscript's single proposed increment; global priority is not certified by the bounded source audit |
| Uniform bounds `lambda_j <= C_eta j^(-eta)` for every `eta<rho` | Finite-dimensional positive congruence and boundedness of a shifted classical LCM kernel | No endpoint uniform `j^(-rho)` claim |
| Cumulative normalization, individual singular values, and spectral moments | Scalar normalization asymptotic; operator-norm convergence and the same summable tail | Consequences of the main theorem, not separate novelty claims |
| Exact failure when `q rho<=1` | Classical LCM eigenvalue asymptotics and finite-rank perturbations | Hilberdink--Pushnitski own the spectral asymptotics and their prime-tensor analysis |

## Modular manuscript structure

1. Introduction: state the exact result early and distinguish it from
   completely multiplicative, multiplicative, and pure-power antecedents.
2. Framework: all hypotheses, zero extensions, ideal conventions, precise
   classical spectral input, and elementary singular-value facts.
3. Gram entries: exact identity, global Potter bounds, domination, and
   the small-index tail needed for entrywise convergence.
4. Uniform spectral control: positive congruence, min--max, and
   finite-head/tail operator-norm convergence.
5. Full ideal range: counting-measure dominated convergence, including
   quasi-Banach ideals, and the sharp negative statement.
6. Consequences and examples: cumulative normalization, fixed-index
   asymptotics, spectral moments, and nonmultiplicative/oscillatory factors.
7. Scope and declarations: no arbitrary-arithmetic-function extension,
   no universal rate, no current-open-problem claim, and truthful draft
   metadata/disclosure boundaries.

All substantive proofs appear in the body. No figure or numerical experiment
is needed for these statements. A compact provenance table in the introduction
clarifies the genuinely different coefficient hypotheses.

## Sources and citation checks

Four sources are sufficient: Hilberdink (2017), Hilberdink--Pushnitski
(published 2023; theorem locators checked in arXiv:2110.14323v1, 2021),
Bingham--Goldie--Teugels (1987), and Simon (second edition, 2005).
The manuscript must bind the even-integer comparison to the accessed 2021
version and must not assert that this restriction remains open today.
Hilberdink's 2017 regular-variation hypotheses and multiplicativity are
reported separately, not conflated with the pointwise family proved here.
`paper/BIBLIOGRAPHY_CHECK.md` records consulted primary records, access
scope, and online/print-year discrepancies.

## Writing and verification workflow

Use `paper-plan`, then `paper-write`, then `paper-compile`, with ARS writing
fidelity and completeness checks. This is a general mathematical article,
not a venue-calibrated submission (`NOT_CALIBRATED`;
`criteria_binding_unavailable`). The batch overrides ML experiment/page
quotas, external-model/API calls, and unrelated pipeline stages. No
external upload or journal submission is authorized.

First produce the complete modular TeX, verified bibliography, and one
real successful compilation in a fresh temporary build directory. Record
actual commands, exit status, PDF inspection, and input/output hashes in
`INITIAL_COMPILE_RECEIPT.md`. Then freeze the source hash ledger and hand
off for non-author full-manuscript review. The coordinator owns the final
two-fresh-directory deterministic build, all-page visual gate, shared
indexes, formal evaluation, and Git operations. Initial compilation is
not represented as that final gate.
