# E4 Round 3 — primitive collision-budget review

2026-09-09 UTC. Independent internal reviewer: `/root/c429_e4_cover_review`.

Reviewed final artifact: [A4 REPORT.md](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round3/a4_primitive_cut/REPORT.md), all 219 lines. Exact SHA-256:

```text
f09f87e1e294ce571a29c37be65ea4c1d880ebb79e9ca93eb2e232ec09bc15e9
```

The hash binds the reviewed text; it is not mathematical evidence. The author marked this hash frozen. Two small edits were observed before freezing: the outcome now says that CUT and GQ both remain unproved, and the general collision-count proof explicitly uses the appropriate geometric residue field. The review below is of the final text, not the earlier intermediate hash.

## Verdict

**PASS for the stated cut identities and the infinite-subfamily mechanism-exclusion theorem (NB). Zero must-fix defects found. Original CUT/GQ remains unproved.**

For every `n = 3^e >= 9`, the proof establishes

$$
M\geq \frac r2-\frac{b+1}{2}\geq2n,
\qquad |\mathcal K_{3,n}|\geq M>\lambda_n,
\qquad d\geq M-1\geq2n-1.
$$

Here `M` is primitive branch-polynomial multiplicity at `c = -2` modulo 3, `d` is the valuation of the discriminant of that polynomial, and `lambda_n` is a minimum finite-edge cut after contracting complement pairs. None is silently identified with a normalized special-fiber different, the multiplicity of an individual point root, or a target-arithmetic quantity.

The proved consequence is precisely that an upper bound on the total collision count, paired with resilience against arbitrary deletions up to that count, cannot establish CUT uniformly. The proof does not identify the colliding edge labels with a disconnecting edge set, does not refute CUT or GQ, and does not establish reducibility or bad reduction. The auxiliary disposition and lack of a paper-admission request are appropriate.

## Claim matrix

All line locators refer to the hash above.

| Claim and author locator | Status | Review finding |
| --- | --- | --- |
| Contract and outcome, lines 7–43 | Correctly scoped | The original incidence/transitivity question is distinguished from the selected total-budget mechanism. |
| Monic integral primitive polynomial, valuations, and splitting field, lines 47–55 | Valid accepted input | Odd-prime unit scaling preserves the discriminant valuation and reduction multiplicities. The valuation on the splitting field is normalized by `v_p(p)=1`. |
| Cut-support equivalences `(CS)`, lines 70–99 | Proved | They require every crossing root to collide, not just one positive product valuation. |
| Discriminant/resultant identities `(DR)`, lines 82–99 | Proved | The sign in the derivative-product identity and the squared cross-resultant in the discriminant identity are correct. |
| Non-descent and fractional valuations, line 99 | Correct safeguard | A necklace cut does not automatically define a ground-field factor. No unjustified integral charge per crossing root is used. |
| General collision bound `(CB)`, lines 101–105 | Proved, source-owned | The trace-corank argument gives `d >= h-t`; the cluster inequality gives `|K| <= 2d`. The control polynomial is not presented as a family counterexample. |
| Chebyshev root partition and cycle counts, lines 115–126 | Proved for the stated prime powers | Proper periods are removed correctly, cross-sign overlaps are excluded, and each type has `r/2` cycles in characteristic zero. |
| Minus-type reduction, line 128 | Proved | Prime-to-3 roots of unity and their inversion classes remain distinct; the native permutation is preserved. |
| Plus-type reduction, lines 130–134 | Proved upper bound | The valuation is `e+1`; residual inversion classes number `(b+1)/2`. Their native periods are not assumed to remain `n`. |
| Integral quotient-point bound `(F)`, lines 136–138 | Proved | Universal surjectivity of the integral quotient map and constancy on point orbits suffice. Nonflat invariant base change is not assumed. |
| Local model, line 150 | Applicable | Normality belongs to the two-dimensional integral model; finite flat rank `r`, reduced special fiber, and generic separability are retained. |
| Coarse discriminant equals `M`, lines 152–156 | Valid | The discriminant is that of `B_k/k[[u]]`, not of the normalization of `B_k`. |
| Trace-corank bound, line 158 | Proved | The nilradical lies in the trace-pairing radical, so rank is at most the number of geometric points. Wild trace degeneracy cannot reverse the inequality. |
| Ground-DVR cluster discriminant, lines 160–164 | Proved | This particular Hensel factor does descend, since it is selected by the rational residue factor `(c+2)^M`. |
| All-level inequality, lines 166–187 | Proved | The constants, denominator, monotonicity range, and factorization at the `n=9` boundary are correct. |
| Contracted-graph bound, lines 191–203 | Proved | Loops are excluded from cut degrees, multiple finite edges are counted, and `h < N/2` is a legitimate characteristic-zero degree comparison. |
| Mechanism exclusion, line 205 | Proved within the budget interpretation | Some cut fits inside the deletion allowance; the actual colliding labels need not contain that cut. |
| Source subtraction and remaining gap, lines 209–219 | Appropriately limited | Composite-period bounds do not borrow prime-period ramification formulas. No novelty certificate or paper closure is claimed. |

## 1. Exact cut algebra

All roots of monic `D` are integral, and characteristic-zero simplicity makes every root difference in `D'(alpha)` nonzero. Consequently

$$v_p(D'(\alpha))=\sum_{\beta\ne\alpha}v_p(\alpha-\beta)$$

is positive exactly when another root has the same residue. Reduction of evaluation then proves the radical/gcd condition. The finite residue field of the splitting field is perfect; its radical means distinct irreducible factors, not division by a derivative that might vanish identically. Thus `(CS)` remains valid when some residual multiplicities are divisible by `p`.

For `a = deg H`, the product of the within-`H` derivatives is `(-1)^{a(a-1)/2} disc H`, while the product of `J(alpha)` over the roots of `H` is `Res(H,J)`. This gives the stated sign. Pairing all cross-factor differences gives the square of the resultant in `disc D`. All three identities in `(DR)` follow without any assumption that `H` or `J` descends to the ground DVR.

In particular, positivity of the product valuation is an existential statement about crossing roots; `(CS)` is universal. Fractional positive valuations in the splitting field cannot be replaced with one integer unit per root. The report correctly blocks that invalid inference.

For `(CB)`, the rank of the trace form on the finite algebra obtained by reduction modulo `p` is at most its number of distinct geometric points. Hence the discriminant valuation over an unramified ground extension is at least the sum of the cluster deficits `a-1`. Each nontrivial cluster contributes `a <= 2(a-1)` colliding roots. This establishes the bound independently of edge incidence. For the stated quadratic control, the discriminant is `4p`, so the factor-two example has the claimed normalized valuation at odd `p`.

## 2. Chebyshev geometry and the quotient-point count

For odd prime-power `n = 3^e`, every proper period dividing `n` divides `m = n/3`. The two groups of roots of unity for `f_{-2}^n(x)=x` therefore lose precisely the indicated subgroups at level `m`. With `a=2^m`, both cross-sign gcds reduce to a divisor of 2 and are odd, so equal 1. Inversion has no fixed points on either remaining set. Each contributes `N/2` distinct point roots; all have exact native period `n`, giving `r/2` cycles per type. This argument uses the full root sets, not only primitive roots of unity.

For the minus type, reduction is injective because the group order is prime to 3. Equality of two sums `z+z^{-1}` determines `z` up to inversion in any field. The induced reduction on the inversion classes is therefore injective and equivariant for squaring. This proves preservation of its `r/2` native cycles without assuming good reduction of the entire dynatomic curve.

For the plus type, the displayed induction correctly gives `v_3(2^{3^e}+1)=e+1`, so the residual roots lie in the prime-to-3 group of order `b=(2^n+1)/(3n)`. That order is odd, and inversion has exactly one fixed point there. There are therefore `(b+1)/2` inversion classes. Counting these as an upper bound on residual native orbits is deliberately conservative and valid even if some periods shorten.

The integral quotient map is finite and surjective: a finite-group invariant extension is integral, and lying over applies. Its surjectivity persists under passage to the geometric closed fiber. Each source orbit maps to a single target point, and every target point has a source point above it. Therefore

$$t\leq \#\{\text{geometric native orbits in the point fiber}\}
\leq r/2+(b+1)/2.$$

Monicity ensures that all special point roots occur as reductions of the characteristic-zero integral roots, with multiplicities. This is sufficient for the inequality. The argument never needs a bijection between special quotient points and orbits, nor equality of invariants before and after a nonflat reduction. Completion at the base closed point leaves this geometric closed fiber, and hence `t`, unchanged.

## 3. Audit of the integral model and discriminant conservation

The report uses the correct integral quotient, not the normalization of the special curve. The local base is `R[[u]]` with `R=W(overline F_3)` and `u=c+2`. Source assumptions involving the degree parameter of the quadratic map use degree 2, not the report's separate symbol `m=n/3`; no condition `3` not dividing `n` is imported here.

There are also direct algebraic checks of the delicate quotient properties. If `Q=A^{C_n}`, then `3A intersect Q = 3Q`: if `3a` is invariant, the absence of 3-torsion in the point algebra forces `a` to be invariant. Thus `Q/3Q` injects into the reduced point algebra modulo 3. Its generic algebra embeds into a separable point algebra. Reducedness and generic separability do not require exactness of the invariants functor on arbitrary modules.

The finite normal quotient is torsion-free and dominant over the two-dimensional regular base. Its local rings of dimension two are Cohen–Macaulay, and the base parameters form systems of parameters; equivalently its finite module is maximal Cohen–Macaulay over the regular local base. It is therefore free. This justification uses the actual dominant integral model: “finite normal algebra” without dominance or the dimension qualification would not be a general flatness theorem. Normality is preserved in the relevant excellent completions. Its rank is the accepted generic quotient rank `r`.

At characteristic-zero primitive branch values, there is one simple ramification point of the quotient, so each contributes one to the trace discriminant. The integral discriminant has no vertical factor because its special generic trace form is nonsingular. One can see the conservation step directly in this setting: write its determinant in `R[[u]]` as a unit times a distinguished polynomial. The distinguished degree is the order of its reduction in `u`; its geometric roots count the characteristic-zero discriminant contributions in this disk. The primitive roots reducing to `-2` are exactly that disk's branch roots, so this degree is `M`.

Nothing in this argument replaces the special order `B_k` by its normalization. That replacement could lower the discriminant and change the point count. The report explicitly excludes it at lines 150 and 156.

For a finite free `k[[u]]`-algebra of rank `r`, reduction of a trace matrix gives the trace form on `C=B_k/uB_k`. Its nilradical has dimension `r-t` and is in the radical of that form: multiplication by `ab` is nilpotent when `a` is nilpotent. Thus the matrix modulo `u` has rank at most `t`. Smith normal form yields at least `r-t` positive elementary-divisor valuations, proving

$$M=\operatorname{ord}_u\operatorname{disc}(B_k/k[[u]])\geq r-t.$$

The inequality does not assume tameness, separability of the closed fiber, or normality of the special fiber. Generic separability is used to ensure that the discriminant is nonzero.

The factor `D_{-2}` is different from a necklace-selected factor `H_S`: its residual support is the ground-field point `-2`, so coprime Hensel factorization over `Z_3` legitimately isolates it. Its degree is `M`, its reduction has one geometric point, and the same trace-rank argument gives `v_3 disc D_{-2} >= M-1`. The complementary resultant is a unit; the complementary polynomial has nonnegative discriminant valuation. This proves `d >= M-1` without confusing an order discriminant with a field different.

## 4. Uniform arithmetic and the finite-edge cut

The algebraic simplification of the fiber deficit is correct:

$$\frac r2-\frac{b+1}{2}
=\frac{2^{n+1}-3\,2^{n/3}-1-3n}{6n}.$$

For `n>=9`, `2^{n/3} <= 2^n/64`. The ratio `2^n/n^2` increases at every integer `n>=3` because `2n^2>(n+1)^2`; starting at 9 gives the stated lower bound with `512/81`. Substitution leaves exactly

$$\frac{28}{81}n^2-3n-1
=\frac{(n-9)(28n+9)}{81}\geq0.$$

The constants and the denominator `6n` therefore establish `M>=2n` throughout the claimed family, including its boundary. Since `M>=18`, every primitive root in this residue cluster really is colliding; no singleton cluster is being counted. Hence `|K_{3,n}| >= M`.

Contracting the fixed-point-free infinity complement pairs leaves `q=r/2` vertices, with `q>=2`. A singleton-vertex cut has its nonloop degree, so the minimum cut is at most the average nonloop degree. The nonloop finite-edge count is at most `h`, including multiplicities. Therefore `lambda_n <= 4h/r`.

The infinity expansion gives each cycle multiplier a nonzero leading term of order `t^{-n}`. The leading product in `delta_n(1,c)` cannot cancel, so its degree in `c=-t^{-2}` is `N/2`. The satellite factor `Delta_{n,1}` has positive degree `phi(n)` in characteristic zero, making `h<N/2`. This is a valid degree subtraction, not a satellite-based estimate of primitive collisions. Consequently `lambda_n<2n`.

Combining the estimates proves `(NB)`. A minimum cut is an actual finite-edge set with size below `|K|`. Since `|K|<=h`, it can even be enlarged to exactly `|K|` finite edges without restoring connectivity. For the larger `2d` allowance, the budget statement means deletion of any set of at most that allowance; when an allowance exceeds all available edges, deletion of all finite edges is permitted. This avoids a vacuous reading of “exactly more edges than exist.”

The proof says nothing about whether the particular colliding labels contain a cut. Thus it invalidates the arbitrary-deletion-budget certificate, not the incidence condition or the surviving-action specialization theorem.

## 5. Primary-source audit and ownership

The source's Proposition 5.3 was read with its full setup: normal finite flat integral algebra, reduced special fiber, and generically étale special map. Propositions 6.2–6.3 supply the odd-characteristic model inputs. Lemma 10.3 and its proof describe the Chebyshev roots for general `n`. Lemmas 10.5–10.6 distinguish the normalized special discriminant from the integral-model discriminant and identify primitive cluster multiplicity. Lemmas 10.9 and 10.11 impose prime-period hypotheses and are not used here. Relevant statements and proofs were read in [Doyle et al., arXiv v2](https://arxiv.org/html/1703.04172v2); the model and discriminant passages were also checked in the [accepted manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/17388c5b-06f8-4235-afed-8ae9a331c5f3/content). The latter was retrieved through a read-only text stream after browser fetches timed out.

The prior reviewed two-edge result and conditional `2d` criterion remain accepted source inputs; this round does not reconstruct the long graph theorem or the underlying Green–Matignon proof cited by Proposition 5.3. The derivative/gcd test, trace-corank inequality, Chebyshev description, and discriminant conservation are classical ingredients. The report's submitted increment is their uniform mechanism-exclusion comparison, not ownership of those ingredients. E4 makes no comprehensive novelty certificate or independent-paper assessment.

## Must-fix register and final disposition

**Zero must-fix items for the final hash and the stated claims.** In particular, no repair is required at the high-risk quotient/discriminant interface in lines 136–164. The proof retains all hypotheses needed there and never substitutes the normalized special fiber.

Safe handoff: `(CS)/(DR)` with their descent warning, `(F)`, `(PM)`, the all-level comparison, and `(NB)` are accepted as auxiliary results. CUT and GQ remain unresolved. A continuation of this branch must use actual edge incidence or additional cluster monodromy; a sharpened total collision-count upper bound by itself cannot revive the ruled-out uniform arbitrary-deletion certificate.

The batch and research-review skills determined this claim matrix, source-hypothesis audit, and explicit scope separation. This was current-session internal nonauthor review, not external-model review, a formal Route-A evaluation, or paper admission. No mathematical program, old rerun, isolated-period enumeration, extra subagent, author edit, first-pass/Round-2 edit, shared-file edit, Git operation, API upload, or PDF build was performed. File reads, primary-source retrieval, and SHA-256 integrity checks were the only diagnostic operations. Only this allocated review file was written. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
