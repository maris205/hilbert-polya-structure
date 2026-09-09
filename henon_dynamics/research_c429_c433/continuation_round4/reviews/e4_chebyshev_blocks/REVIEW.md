# E4 Round 4 — Chebyshev blocks and the remaining global quotient

2026-09-09 UTC. Independent internal reviewer: `/root/c429_e4_cover_review`.

Reviewed artifact: [A4 REPORT.md](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round4/a4_global_quotient_after_full_inertia/REPORT.md), all 186 lines, bound to SHA-256:

```text
a1eeb7f2e2c1300a9354abc8406714acc6254d5e33bfd4bc3ecf8b9b18ae5dcc
```

The complete 308-line [E6 all-level local review](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round3/reviews/e6_full_local_inertia/REVIEW.md) was also read. Its bound local-proof hash, `0a4f4ff66b633de268d741142502c1b4244868b9eccd3eb040ae472e0b296250`, matches the actual proof file. E4 uses that theorem as an accepted input and does not claim another independent whole-proof review of it. The author's initial frozen conditional status is explicitly superseded by its outcome/dependency update at lines 36–37.

## Verdict

**PASS for (EQ), the coarse Chebyshev block calculation, (QB), Proposition 2 and its explicit pair, and the conditional derivative/smoothness criterion (TR). Zero must-fix defects found. Global PC424-D remains unresolved.**

The new local input gives the exact equivalence between geometric point irreducibility and the cycle quotient being a field. It does not prove either condition. The table distinguishes point-root multiplicities, numbers of characteristic-zero cycle sheets, and degrees of normalized special branches. The constructed group has the claimed proper two-sheet orbit, but is not identified with actual special-fiber monodromy.

The complete all-odd-prime/all-level question is not replaced by the prime-three block calculation. The report explicitly checks the other odd primes and finds that this Chebyshev mechanism has only singleton reduction blocks there. The method-specific output remains auxiliary, with no paper-admission or target-arithmetic conclusion.

## Full claim matrix

Line locators refer to the author hash above.

| Claim and locator | Status | Exact limitation or proof check |
| --- | --- | --- |
| Original object, native clock, and dependency update, lines 7–39 | Correct | The all-level local theorem is now reviewed input; the original global component problem remains separate. |
| Component formula application and `(EQ)`, lines 43–54 | Proved from accepted inputs | Full local rotation controls one `h_j`; if there is only one quotient factor, that is enough for point transitivity. It does not force a single quotient factor. |
| Descent to native parameter, line 56 | Valid | Coprime Hensel uniqueness identifies the pulled-back factor; a factorization over the native field would persist over the tame extension. |
| Prime-power Chebyshev partition, lines 60–65 | Valid classical input/application | Both signs are kept, proper periods are excluded, and inversion precedes native cycle counting. |
| All blocks singleton for `p>=5`, lines 69–73 | Proved | Neither root-of-unity group order is divisible by `p`; reduction preserves the point set and its native permutation. |
| Prime-three point multiplicities, lines 83–98 | Proved | The four cases give `1, n, 2n, 3n`, with the special inversion count at `xi=1` handled separately. |
| Residual periods, line 100 | Proved | Outside the lower prime-to-3 subgroup the residual period is exactly `n`; inside it the period divides `m`. |
| Quotient geometric points equal residual orbits, line 102 | Proved | Integral surjectivity supplies existence; a multiplicative invariant separates different orbits without averaging or nonflat invariant base change. |
| Block sizes and coarse germ ranks, lines 104–106 | Proved | The formula `ell=da/n` is an integer count of complete native cycles. It gives `1, 1, 2d, 3n`, not automatically individual normalized ramification indices. |
| Pure-3-power cycle and rank-one germ, line 108 | Proved | The order of 2 modulo `3^(e+1)` is `2n`; the rank-one quotient algebra is the base ring. |
| Plus-block count `(QB)`, lines 110–114 | Proved | Its summands count exact residual periods, and their integrality follows from free orbit counting. It is not a global component count. |
| Real-path labels and complement interchange, lines 119–129 | Valid | The path is unbranched up to the simple Chebyshev endpoint; nonzero real signs persist. Multiplier signs distinguish the two types. |
| Constructed maximal within-block group, lines 131–135 | Correctly delimited | It is a permutation model on the specified characteristic-zero sheet set, not a formula for special monodromy. |
| Proposition 2, `(PAIR)`, and cosine labels, lines 137–153 | Proved | Its orbits are exactly `B union iota(B)` over plus blocks at 3, or complement pairs at larger odd primes. The specified pair is proper for `e>=2`. |
| Derivative identity `(TR)`, lines 157–168 | Proved | The chain-rule sum has the correct indices and nonzero denominators; in characteristic 3 its leading multiplier is 1. |
| Smoothness and conditional branch degree, line 170 | Proved conditional statement | On this exact-period residual orbit the free cyclic quotient has the same completed local germ; nonvanishing implies one branch of degree `3n`. Vanishing does not decide unibranchness. |
| Transport/incidence gap, lines 172–176 | Correctly retained | No crossing primitive label or common-fiber special-monodromy identification is proved. |
| Source exclusions and disposition, lines 180–186 | Correctly limited | The cited component/gonality theorem does not establish irreducibility of the whole dynatomic polynomial. No comprehensive literature-absence claim is certified. |

## 1. The exact use of full local inertia

The accepted local theorem gives one global quotient component with `h_{j_*}=n`. In the already reviewed formula

$$\#\operatorname{Irr}(\Phi_n)=\sum_j n/h_j,$$

that component contributes one point factor, of degree `n r_{j_*}`. If `B_n` is a field, there is only this one quotient component, so the sum is one. Conversely, when the point algebra is a field its invariant algebra is a field: the inverse of any nonzero invariant is invariant. Monicity and the accepted generic separability identify this field assertion with geometric irreducibility of the reduced total curve. This proves `(EQ)` with every original odd-prime/level quantifier retained.

For the native-parameter statement, at `u=0` the local factor is `(x-1/2)^n`, coprime to its Hensel complement. It therefore lifts uniquely as a monic degree-`n` factor over `k[[u]]`. Under `u=-s^2/4` and the stated translation, uniqueness identifies it with the accepted canonical small factor. Irreducibility after this extension excludes a nontrivial factorization before it. Its root field contains the whole native orbit; separability and the commuting native action then give a cyclic Galois group of order `n`. This is descent of the local conclusion, not an assertion about the other global quotient components.

No step establishes `s=1` or `h_j=n` for every `j`. The author has not converted a local theorem into a global transitivity theorem.

## 2. Multiplicities, quotient points, and coarse block degrees

### Point lifts and residual periods

In the prime-three plus group, the prime-to-3 part has order `b_e` and the 3-primary part has order `3n`. The excluded lower group has the respective parts `b_{e-1}` and `n`. For a nontrivial residual `xi` in the lower subgroup, there are `2n` surviving lifts over `xi`; pairing these with the lifts over `xi^{-1}` leaves `2n` distinct point roots. For a new `xi`, the corresponding number is `3n`. At `xi=1`, inversion occurs within the `2n` surviving roots and gives `n` point roots. Minus roots have multiplicity one. No cross-type collision has been omitted, since the relevant prime-to-3 orders are coprime and the minus set excludes the identity.

The equality `xi+xi^{-1}=eta+eta^{-1}` implies `eta=xi` or `xi^{-1}`. A residual plus point has period dividing `m` precisely when `xi^(2^m)` equals one of those two possibilities. The positive-sign alternative forces the identity by the stated gcd, and the negative-sign alternative is exactly membership in the lower prime-to-3 subgroup. All other proper periods divide `m`. Thus the residual-period column is correct, including the exact period of the new row.

At `p>=5`, the congruences `2^n-1=1 mod p` and `2^n+1=3 mod p` make both root-of-unity groups prime to `p`. Injective equivariant reduction preserves all roots and their exact periods. The point cover is consequently étale at this fiber, and its free cyclic quotient is étale as well. There is no nontrivial quotient inertia from this specialization.

### Why the geometric quotient-point assertion is stronger than the Round 3 bound

The invariant extension is integral and universally surjective, so every geometric quotient point lifts to a point of the source fiber. If two different residual orbits are chosen, finite-set interpolation supplies a function with values zero on one and one on the other. Lifting it and multiplying its translates over the whole cyclic group produces an invariant with those same two values. Their quotient images cannot coincide.

This proves an exact bijection of geometric points with residual native orbits. It is a statement about points, not equality of special-fiber coordinate rings with a naively reduced invariant ring. The product construction uses neither division by `n` nor exactness of a Reynolds averaging operator; it remains valid when `p` divides `n`.

If a residual orbit has `d` points and each receives `a` characteristic-zero roots, all `da` lifts partition into complete cycles of length `n`. A characteristic-zero cycle reduces into just one residual orbit, and reduction commutes with iteration. Therefore the number of cycle sheets is exactly `da/n`. Division here counts finite sets in the integers, not an operation in characteristic `p`. Applying it gives the four coarse degrees `1, 1, 2d, 3n`.

### Germ degree versus normalized branches

The accepted normal integral quotient model is finite over the two-dimensional regular parameter base. Its completed local factors are finite free; these are factors of the integral model before reducing to characteristic 3. Setting `c=-2` gives a finite free algebra over the Witt DVR. Its characteristic-zero fiber is étale, with precisely the cycle sheets reducing to the selected point. Its rank is therefore the block size `ell` just counted.

The special fiber is reduced and generically separable, but need not be normal. Its normalization can split into several branches. Their field degrees over `k((c+2))` sum to `ell`; the table supplies no individual branch degree until an additional one-branch statement is proved. The report consistently keeps this distinction. In particular, it does not identify the point-root multiplicity `2n` with the old plus block degree `2d`.

For the singleton pure-power block, a finite free rank-one unital algebra over the local base is the base itself: the unit generates after reduction and hence by Nakayama generates the module. Thus this quotient germ is genuinely trivial. This is compatible with a nontrivial degree-`n` point cover above it.

## 3. Counting blocks and identifying the pure cycle

With `a=2^(3^(j-1))`, one has

$$b_j/b_{j-1}=(a^2-a+1)/3.$$

The previous valuation calculation makes this an integer prime to 3. It is one at `j=1` and greater than one for `j>=2`. Hence the nested subgroups used in `(QB)` and the claimed existence of a non-pure block are justified.

The stratum `mu_(b_j) minus mu_(b_(j-1))`, after inversion, has `(b_j-b_(j-1))/2` elements, all of exact native period `3^j` by the preceding period argument. Its free orbit count is the corresponding summand of `(QB)`. Adding the identity orbit gives exactly `q_e`. The formula also respects the boundary `e=1`, where there is only the identity plus block.

Every root in `mu_(3n) minus mu_n` is primitive of order `3n`. The multiplicative order of 2 divides `2n` and is even. A smaller possible order would be `2*3^j` with `j<e`, contradicting `v_3(2^(2*3^j)-1)=j+1`. Thus 2 generates the units modulo `3^(e+1)`. Modulo inversion it has one orbit of size `n`, producing exactly the asserted pure-power cycle. Its reduced point is `x=2,c=-2`, equal in characteristic 3 to the parabolic point `x=1/2,c=1/4`.

The explicit cosine formula enumerates this cycle's signs, up to native cyclic shift. None is zero because an odd power of 3 cannot divide the required power of 2 for a cosine zero. A different primitive root is a power-of-2 translate, possibly followed by inversion, so it does not change the necklace. This is a uniform label, not a finite-period enumeration.

## 4. The actual infinity involution and the constructed group

For real `c<-2`, the critical orbit escapes, so this interval lies outside the Mandelbrot set. The characteristic-zero point cover has no branch point there. At `c=-2`, the Chebyshev periodic roots in question are simple, with multipliers `+2^n` or `-2^n`, neither equal to one. This justifies continuation to the endpoint. Starting near negative infinity, the roots are real and have the infinity sign-word labels. Continuation cannot leave the real line without a collision, and signs cannot change without a periodic root passing through zero. Zero is not periodic on this interval or at its endpoint.

Differentiation through `x=zeta+zeta^{-1}` gives the reported multiplier formula. Its denominator is nonzero on the two exact-period root sets. Since a native derivative is a product of the factors `2x_i`, the multiplier sign is exactly the product of itinerary signs. Complementing all signs changes this product when `n` is odd. Therefore the infinity permutation transported by the specified real path exchanges `C_+` and `C_-`. It remains one involution, not a set of independently selectable transpositions.

At 3, minus blocks are singletons. For any plus block `B`, the set `B union iota(B)` is invariant under every generator of `G_Ch,3`. The full symmetric action on `B` connects its plus vertices, and the involution reaches their minus partners, so that set is exactly one orbit. These sets are disjoint and exhaust the sheets. Thus the group has exactly `q_e` orbits. The pure block is a singleton, so its orbit is the specified two-sheet pair; it is proper for `e>=2`.

For `p>=5`, all blocks are singletons, leaving only the infinity involution. Its orbits are the `r/2` complement pairs. There is more than one pair for `n>=5`, as follows directly from the degree formula. The exceptional wild pair `(3,1)` has rank two and is correctly excluded from the nontransitivity assertion.

These are statements about the defined permutation group on the chosen characteristic-zero sheet set. The formal integral decomposition explains why local actions within that neighborhood preserve reduction blocks, so allowing all within-block permutations grants at least their possible connecting power. It does not supply transport to a special characteristic-3 generic fiber that preserves every chosen label and the infinity action. Nor does it include all primitive inertia elsewhere. E4 therefore does not export the two-sheet pair as invariant under actual special monodromy, or as a certificate that every crossing primitive edge collides.

## 5. Derivative and smoothness criterion

Put `x_j=f_c^j(x)`, `Q_j=partial_c x_j`, and `D_j=partial_x x_j`. The recurrences are

$$Q_{j+1}=2x_j Q_j+1,\qquad D_{j+1}=2x_jD_j,\qquad Q_0=0,\ D_0=1.$$

When the `D_j` are nonzero, division and telescoping give

$$Q_n=D_n\sum_{j=1}^{n}D_j^{-1}.$$

At the new plus residual points, the derivative formula in terms of `xi` makes all denominators nonzero: `xi` has nontrivial odd order, so no repeated squaring produces an element of order two. Moreover `xi^(2^n)=xi^{-1}`, and in characteristic 3, `D_n=-2^n=1`. Substitution yields exactly `(TR)`, including its sign and index range.

The lower-period denominator in `Phi_n` is a unit at these exact-period-`n` points. The partial derivatives of `Phi_n` therefore equal those of `f_c^n(x)-x` multiplied by this unit's inverse. Its `x`-derivative vanishes; its `c`-derivative is nonzero exactly when `(TR)` is nonzero. The plane-curve Jacobian criterion over the perfect residue field gives the claimed equivalence with smoothness of the special point germ.

The constant cyclic group acts freely on this exact-period residual orbit. On an invariant neighborhood its quotient is a finite étale torsor, even though the group order is divisible by the characteristic. After choosing the geometric point, the completed quotient germ is isomorphic to that point germ. Thus it has the same smoothness test. If `(TR)` is nonzero, the special complete local ring has one normalized branch. Its degree is `3n`, the already established coarse degree of this row. If `(TR)` vanishes, singularity is proved but unibranchness is undecided. The report claims no uniform nonvanishing result.

## 6. Primary-source applicability and remaining gap

[Doyle–Poonen](https://math.mit.edu/~poonen/papers/dyn_gonality.pdf) defines its dynatomic curves using irreducible factors. Theorem 1.1(a), Remark 1.3, and the positive-characteristic proof in §4 were checked: geometric irreducibility is asserted for those components, while irreducibility of the customary whole factors is expressly not assumed. This source cannot supply `(GQ)` here. Its gonality and component assertions retain their source ownership; no claim of current literature-wide absence is made by E4.

The actual labeling statements were checked in [Doyle et al., accepted manuscript, §§8–9](https://api.repository.cam.ac.uk/server/api/core/bitstreams/17388c5b-06f8-4235-afed-8ae9a331c5f3/content): the finite branch locus lies in the Mandelbrot set, itineraries label point/cycle sheets outside it, and Proposition 9.7 gives infinity complementation. The integral model and Chebyshev inputs remain those source-owned results already audited in Rounds 2–3. The present proof does not import the source's prime-period ramification formulas for composite levels. The accepted text was read through a read-only stream when browser retrieval was unavailable.

The original unresolved obligation is still global quotient transitivity. A closing proof must provide compatible common-label transport and enough additional branch actions to connect the displayed pair and then the other classes, or use a different global argument. The report provides neither those primitive labels nor a valuation assertion about their crossing polynomial. Even a proof of unibranchness of every Chebyshev block would not turn the defined group into a transitive group. The earlier scalar-budget obstruction is not being reused as a new result or silently overcome.

## Must-fix register and final handoff

**Zero must-fix items for the bound final report.** The open statements in lines 172–176 are correctly marked as open and are not concealed dependencies of a claimed global theorem.

Safe auxiliary exports are `(EQ)` from the reviewed local input, the four coarse block degrees, `(QB)`, the exact orbit description of `G_Ch,p`, the uniformly labeled proper pair for `p=3,e>=2`, and the conditional `(TR)` test. Do not export a normalized branch degree without its one-branch hypothesis, a special-fiber monodromy identification, or closure/refutation of CUT/GQ/PC424-D.

The repository batch and research-review workflows required the full claim matrix, source-hypothesis checks, and explicit separation between accepted input, proved auxiliary statements, and the remaining target. This is current-session internal nonauthor review, not an external-model review, formal evaluation, or paper-admission decision. No mathematical execution, census, old rerun, extra subagent, author/shared edit, Git operation, manuscript/PDF build, or external-model upload occurred. Only this allocated review file was written. All prior-round artifacts remain read-only. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
