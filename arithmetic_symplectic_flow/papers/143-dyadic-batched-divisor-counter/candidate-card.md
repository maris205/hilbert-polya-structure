# Broadened carrier card — ANG-20260915-DDC01

**Version:** 1, 2026-09-15; frozen before theorem claims or computations.  
**Initial status:** BROADENED HYPOTHESIS — T0--T3 OPEN.

This is a new batch-processing action, not a roof change on 140. Every
integer is included and no prime-specific period is supplied.

Define K_n=max(1,floor(log_2(n-1))) for n>=2, equivalently from the binary
length of the positive integer n-1. The state space is

\[
Y=\coprod_{n\geq2}\{n\}\times\{1,\ldots,K_n\}\times\mathbb Z/n\mathbb Z.
\]

For batch phase k, let the finite divisor-witness block be

\[
B(n,k)=\{d:2^k\leq d<2^{k+1},\ d<n\},\qquad
b(n,k)=\sum_{d\in B(n,k)}1_{\{d\mid n\}}.
\]

Freeze exactly the map

\[
F(n,k,c)=(n,k^+,c+b(n,k)\bmod n),
\]

where k^+=k+1 unless k=K_n, when k^+=1. For n=2 the sole block is empty.
The sum is part of this finite, explicitly batched update rule; its computational
cost is not falsely declared constant on a sequential machine.

| Field | Frozen content |
| --- | --- |
| Source lineage | Prime/composite divisor exclusion -> local witness accumulation -> autonomous dyadic-block sequential deformation retaining phase and counter |
| New architecture | One update processes the entire current dyadic block; no microstep equivalence or physical-clock transfer from 140 is assumed |
| Carrier / owner | Full discrete Y and F; transformation groupoid by Z if invertibility is proved |
| Permitted inputs | Integer divisibility, binary partition, all n, all phases and counter states; no prime word, fitted period or zero data |
| Arithmetic observable | Complete-counter displacement at the first return of the batch phase |
| Clock / flow | Unit roof for this macro-update, (z,1) identified with (Fz,0); no roof changed after audit |
| Primitive packets | All full least-period orbits modulo cyclic phase; complete multiplicity including all counter states and composites |
| Analytic proposal | Ordinary unweighted product if full packet and convergence audit succeeds; operator/domain/trace OPEN |
| Early checks | Inverse; every proper divisor processed exactly once per batch cycle; prime/composite full return; actual macro-period growth and full multiplicity |
| Critical clock control | Compare macrosteps with the number of elementary divisor tests; distinguish logarithmic schedule depth from a derived geometric or physical elapsed time |
| Further controls | Suppress b; replace it by block cardinality; serial scan comparator 140 and alternate fixed blocking schedules, all separate owners |
| PROVES_TOO_MUCH risk | Batching may assign a desired complexity-scale clock without new arithmetic geometry; no claim of canonical prime-log time from binary notation alone |
| Classical fields | Finite-dimensional symplectic / Hamiltonian / contact / quantum owner NOT APPLICABLE or NOT SUPPLIED |
| Decision boundary | Preserve exact arithmetic returns if proved; stop promotion if clock is only an externally chosen batching convention. Do not change blocks, roof or packet subset to repair it |
| Route | Broadened T0--T3 research labels only; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

The geometric and timing owners of 141 are not imported. A logarithmic
asymptotic comparison, if later proved, is not on its own an endogenous
geometric clock or a prime-power trace identity.

## Audit addendum — 2026-09-15; no object change

**Current status:** STOP PROMOTION — EXACT MARKED RETURNS; BATCH CLOCK NOT GEOMETRICALLY JUSTIFIED.

The [paper](paper.md) proves the exact marked first-scan prime selector,
complete cycles of multiplicity g(n)=gcd(n,a(n)) and length K_n n/g(n),
and the same ordinary product on Re(s)>2 log2. Prime p has p cycles
with exact macroperiod K_p=log_2 p+O(1). These positive results remain
attached to the frozen macro-action, not to comparator 140.

A full scan still processes n-2 individual divisor tests. The mathematical
macroclock is well defined, but its canonical geometric or physical meaning
is OPEN. Promotion stops at that distinction; the blocks, roof and full
packet ledger are unchanged. No classical or formal Route coordinates
are assigned; Route B remains NOT INVOKED.

See [claim ledger](claim-ledger.md), [summary](README.md) and
[evidence](evidence/README.md).
