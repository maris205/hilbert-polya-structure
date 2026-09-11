# Bounded owner / priority search log

## Protocol and limits

- Search date: 2026-09-02 UTC.
- Scope: five strongest or most owner-sensitive scout systems (`A01`, `A02`, `A05`, `A06`, `A08`).
- Method: bounded exact-phrase and concept queries, followed where possible by an original paper, publisher page, author preprint, or authoritative repository record.
- External state: **HOLD_EXTERNAL**.  This was passive source inspection only; no author contact, posting, submission, or circulation occurred.
- A query non-hit means only “not found in this bounded pass.”  It is not evidence of novelty, absence, or priority.
- Historical P1--P156 collisions are a separate internal gate.  In particular, the literal translation--GCD proposal was removed because it is already P128, and the matrix Gram proposal was removed because it merely transported P102's `aa*` update to another star-algebra.

## A01 — Frobenius difference `x -> x^q-x`

### Queries

1. `"x^q-x" iteration finite field functional graph`
2. `nilpotent linearized polynomial functional graph finite field`
3. `"Frobenius minus identity" finite field dynamics`
4. `site:arxiv.org iterating additive polynomials finite fields`

### Primary / authoritative hits

- Lucas Reis, *Nilpotent linearized polynomials over finite fields and applications* (2016): https://arxiv.org/abs/1609.09379
  - **Supports:** compositional nilpotence of linearized polynomials over finite fields, constructions, and some explicit cycle structure.
  - **Does not by itself support:** the exact normal-basis `sigma-I` depth CDF written in the scout.
- Lucas Reis, *Counting distinct functional graphs from linear finite dynamical systems* (2021; later Linear Algebra and its Applications): https://arxiv.org/abs/2105.09814 and https://doi.org/10.1016/j.laa.2022.10.011
  - **Supports:** an established general functional-graph framework for finite linear maps.
  - **Does not by itself support:** a priority claim for this one specialization.
- Lucas Reis, *Iterating additive polynomials over finite fields* (2025): https://arxiv.org/abs/2502.19141
  - **Supports:** iteration of additive polynomials and explicitly includes `X^p-X` in the surrounding theory.
  - **Does not support:** any claim that the scout specialization is unowned.

### Decision

`DIRECT_GENERAL_OWNER / KILL`.  Even if the short depth formula is not printed verbatim in these records, it is an immediate cyclic-module specialization of a mature owner lane.  Generic linear algebra and linearized-polynomial iteration consume the contribution.

## A02 — derivative--GCD multiplicity descent

### Queries

1. `"gcd(f,f')" iteration finite field polynomial dynamics`
2. `gcd polynomial derivative iterate multiplicity finite field`
3. `square-free decomposition finite characteristic derivative gcd`
4. `bounded divisors gcd derivative self-map`

### Primary / authoritative hits

- David Y. Y. Yun, *On square-free decomposition algorithms*, SYMSAC 1976: https://doi.org/10.1145/800205.806320
  - **Supports:** the classical square-free-decomposition use of derivatives and polynomial GCDs; this primitive is directly owned and must be zero credit.
  - **Does not support:** the finite self-map on all divisors of `G^{p(L+1)-1}`, its complete iteration formula, depth layers, or every-target iterated fibres.
- *On square-free factorization of multivariate polynomials over a finite field*, Theoretical Computer Science 187 (1997): https://doi.org/10.1016/S0304-3975(97)00059-5 and https://www.sciencedirect.com/science/article/pii/S0304397597000595
  - **Supports:** finite-characteristic square-free factorization as an established algorithmic subject based on GCD machinery.
  - **Does not support:** the proposed temporal/fibre conjunction.
- MIT 18.783 finite-field arithmetic notes, lecture 3: https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/b6d0aef71278ad8c1d8b5144c4138cb7_MIT18_783S21_notes3.pdf
  - **Supports:** an authoritative modern exposition of the derivative--GCD multiplicity criterion and the finite-characteristic caveat.
  - **Does not support:** novelty or priority for a dynamical specialization.

### Bounded non-hit

No direct source was found in this pass for the exact self-map
`f -> gcd(f,f')` restricted to the complete bounded divisor box, together with all iterates, sharp depth CDF, and all target fibres.  The search is too small to turn that non-hit into a novelty claim.

### Decision

`CLOSE_PRIMITIVE_OWNER / KEEP_RESERVE_PENDING_SPECIALIST_SEARCH`.  A focused search must cover computational algebra, finite-ring dynamics, and multiplicity-poset operators before drafting.  The residual can only be the complete temporal/fibre conjunction; the GCD/derivative observation itself is zero credit.

## A05 — non-coprime substitution on `F_q[X]/(X^m-1)`

### Queries

1. `"f(x^k)" "x^m-1" functional graph`
2. `"f(x^k)" "x^n-1" cyclic code multiplier`
3. `"substitution" endomorphism "F_q[x]/(x^n-1)"`
4. `group algebra endomorphism x maps to x^k functional graph finite field`
5. `non-coprime multiplier cyclic code coefficient collapse`

### Primary / authoritative hits

- W. C. Huffman, V. Job, and V. Pless, *Multipliers and generalized multipliers of cyclic objects and cyclic codes*, Journal of Combinatorial Theory A 62 (1993): https://doi.org/10.1016/0097-3165(93)90043-8 and https://www.sciencedirect.com/science/article/pii/0097316593900438
  - **Supports:** multiplier permutations `i -> ai mod n`, generalized multipliers, and their action on cyclic codes, especially in the coprime/permutation regime.
  - **Does not support:** the non-coprime coefficient-merging endomorphism, its stabilization height, every target fibre, the depth CDF, or the residual periodic-core fixed sequence.
- Lucas Reis, *Counting distinct functional graphs from linear finite dynamical systems*: https://arxiv.org/abs/2105.09814 and https://doi.org/10.1016/j.laa.2022.10.011
  - **Supports:** generic finite-linear functional-graph machinery.
  - **Does not support:** a direct owner for the arithmetic `gcd(k^t,m)` image staircase or its coupling to cyclic multipliers.
- Internal P102, `cyclic-group-algebra-involution-norm-dynamics`.
  - **Supports/owns internally:** the same ambient cyclic group algebra and general cautions about scalar power-map/zeta bookkeeping.
  - **Does not support:** A05's substitution update; P102 uses the nonlinear map `a -> aa*`.

### Bounded non-hit

No direct primary source was found for the conjunction:

`non-coprime substitution collapse + exact g_t image/fibres + sharp valuation height + depth CDF + periodic multiplier-core fixed sequence`.

This is only a bounded non-hit.  Search-result snippets and teaching notes were not treated as ownership evidence.

### Decision

`NO_DIRECT_OWNER_FOUND_BOUNDED / KEEP_PRIMARY_OWNER_GATE`.  Before any manuscript, search semigroup actions on cyclic modules, cellular automata on finite cyclic groups, modular group algebras, endomorphisms of cyclic codes, and finite-linear functional graphs.  Coprime multiplier facts and generic rank-nullity get zero credit.

## A06 — Cayley--Newton principal-unit dynamics

### Queries

1. `Newton iteration x plus inverse over 2 Cayley transform squaring`
2. `"(x+x^{-1})/2" Cayley squaring Newton`
3. `Newton sign iteration Cayley transform error squares`
4. `modular Newton sign iteration finite rings functional graph`

### Primary / authoritative hits

- J. D. Roberts, *Linear model reduction and solution of the algebraic Riccati equation by use of the sign function*, International Journal of Control 32 (1980): https://doi.org/10.1080/00207178008922881 and https://www.tandfonline.com/doi/abs/10.1080/00207178008922881
  - **Supports:** the Newton sign iteration as an established map.
  - **Does not support:** the exact finite principal-unit fibre census.
- N. J. Higham, *Functions of Matrices*, matrix-sign chapter: https://eprints.maths.manchester.ac.uk/1067/1/covered/MIMS_ep2008_39_Sample_chapter.pdf
  - **Supports:** the standard iteration `X_{k+1}=(X_k+X_k^{-1})/2`, its provenance, and its classical convergence theory.
- J. Banks, J. Garza-Vargas, A. Kulkarni, and N. Srivastava, *Pseudospectral Shattering, the Sign Function, and Diagonalization in Nearly Matrix Multiplication Time*: https://arxiv.org/abs/1912.08805
  - **Supports:** a modern rigorous treatment explicitly identifying Roberts' Newton iteration.

### Decision

`DIRECT_MAP_OWNER / KILL`.  The finite-ring valuation specialization is calculable, but the map and the error-squaring/Cayley mechanism are classical; the remaining fibre table is too thin.

## A08 — squaring on `S_n`

### Queries

1. `"squaring map" symmetric group functional graph permutation`
2. `square roots of permutations formula symmetric group primary paper`
3. `enumeration square permutations S_n`
4. `permutations admitting m-th root exponential generating function`

### Primary / authoritative hits

- *Enumeration of the square permutations in S_n*, Journal of Combinatorial Theory A 17 (1974): https://doi.org/10.1016/0097-3165(74)90002-8 and https://www.sciencedirect.com/science/article/pii/0097316574900028
  - **Supports:** direct enumeration of permutations in the image of the squaring map and efficient counting procedures.
  - **Does not necessarily print:** the whole pointed functional graph in the scout's notation.
- Nicolas Pouyanne, *On the Number of Permutations Admitting an m-th Root*, Electronic Journal of Combinatorics 9 (2002): https://doi.org/10.37236/1620 and https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i1r3
  - **Supports:** root existence/enumeration via exponential generating functions in the more general `m`th-root setting.
  - **Does not support:** a new priority claim for assembling the elementary 2-adic tail rule with those root counts.

### Decision

`DIRECT_SECOND_AXIS_OWNER / KILL`.  The transient rule follows immediately from squaring cycle lengths, while the fibre/root axis is directly classical.  There is no credible residual theorem package.

## Search conclusion

| candidate | bounded owner result | action |
|---|---|---|
| A01 | mature direct general theory | kill |
| A02 | direct primitive owner; no direct temporal-conjunction hit | reserve, specialist gate required |
| A05 | adjacent multiplier and generic-linear owners; no direct conjunction hit | primary, specialist gate required |
| A06 | direct classical map/conjugacy owner | kill |
| A08 | direct root-enumeration owner | kill |

Only A05 and A02 survive this bounded pass, and both remain **HOLD_EXTERNAL**.  Neither a bounded query log nor exact finite enumeration authorizes novelty, priority, release, or manuscript drafting.
