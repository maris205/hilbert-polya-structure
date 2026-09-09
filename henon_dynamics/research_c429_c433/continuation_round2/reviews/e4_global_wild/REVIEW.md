# E4 Round 2 — independent review of the global wild cycle quotient

2026-09-09 UTC. Reviewer: `/root/c429_e4_cover_review`.

Reviewed artifact: [A4 REPORT.md](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round2/a4_wild_global_quotient/REPORT.md), all 184 lines of the finalized version. Line locators below refer to that version. This is an internal nonauthor proof review, not a formal Route-A evaluation or paper-admission decision.

## Verdict and scope

**PASS for the stated auxiliary results and the explicitly conditional bridge; no must-fix defect found. NOT A PROOF of uniform (GQ) or PC424-D.**

The report proves the finite-étale quotient interface, the component formula, the infinity parity constraint, the fixed-point satellite identity, and the graph-theoretic reduction. It correctly leaves uniform surviving-edge connectivity and uniform global quotient transitivity open. Its negative outcome is justified: the displayed satellite identity defeats one classical sufficient criterion, not the desired theorem itself and not every primitive-branch criterion.

The applicable batch and research-review workflows required a claim-by-claim audit, primary-source hypothesis checks, source subtraction, and explicit separation of proved statements from unresolved targets. No external-model review was requested or performed; the current-session nonauthor assignment supplies the internal review. No first-pass artifact was changed.

## Full claim matrix

| Claim and exact author locator | Review status | Reason or retained limitation |
| --- | --- | --- |
| Frozen object and native clock, lines 7–24 | Correct | The base is the generic field `F = k(c)`, `n = p^e`, and one application of `f_c` is one tick. The quotient-field assertion is distinguished from point-field irreducibility. |
| Lemma 1: generic separability, exact period, degree, lines 42–48 | Proved | The sign-word construction supplies the full number of distinct roots; deleting the words with period dividing `m` gives exactly the prime-power dynatomic roots. |
| Lemma 1: complement inertia, lines 50–52 | Proved, classical reconstruction | Odd word length excludes a necklace fixed by complementation. This is not claimed as a new irreducibility theorem. |
| Generic invariant algebra, rank, and torsor, lines 54–62 | Proved | Flat field extension and free finite-set orbits justify the quotient even when `p` divides the group order. |
| Generation by all orbit-polynomial coefficients, lines 64–68 | Proved | Different cycles have different monic root polynomials. No unsupported trace-generation claim is used. |
| Lemma 2 and `(CC)`, lines 72–87 | Proved | Stabilizer rotation order `h_j` gives `n/h_j` point factors of degree `r_j h_j` above the `j`th quotient factor. |
| Total-curve interpretation, line 87 | Correct | Monicity excludes vertical components; generic factors count geometric components of the reduced total curve, not a special parameter fiber. |
| Even `r_j` and infinity-point counts, lines 85–87 | Proved | Each global cycle orbit is a union of the inertia complement pairs. |
| Small-cycle invariant algebra and local/global interface, lines 91–97 | Proved from the stated accepted small-cycle input; full inertia remains conditional | A single local cycle supplies one quotient sheet. Full local rotation forces only `h_{j_*} = n`; it does not force `s = 1`. |
| Multiplier conventions and `(SAT)`, lines 101–120 | Correct and proved | The ordinary cyclotomic polynomial is kept distinct from the dynatomic polynomial; evaluation of the resultant at `U = 1` gives the stated exponent and parameter factor. |
| Failure of the full-discriminant hypothesis, line 122 | Correct | The satellite factor has a repeated factor at every odd-prime level. The conclusion does not assert failure of the primitive criterion. |
| Satellite collision versus quotient edges, line 124 | Correct | Rotation inside one cycle is trivial on its cycle label; primitive collisions require their own analysis. |
| Collision set and infinity convention, lines 128–135 | Correct | Collision is defined among primitive branch values. Infinity is one permutation with multiple two-element orbits, not separately available generators. |
| `(CUT)` and the graph equivalence, lines 139–151 | Exact conditional reduction | Proper invariant subsets are precisely the uncut unions of complement pairs. Uniform `(CUT)` is not proved. |
| Imported specialization, lines 153–155 | Applicable with the stated model and common-fiber hypotheses | This is a source-owned specialization input, not an unrestricted assertion about wild invariant-ring reduction. |
| Quantitative bound `(GB)`, lines 147–151 | Valid under that interface | The orbit partition of special monodromy coarsens the surviving-action orbit partition, so the inequality has the correct direction. |
| Collision-supported cut, lines 157–159 | Correct necessary obstruction only | Failure of `(GQ)` implies such a cut; finding a cut does not refute `(GQ)` because discarded clusters may connect it. |
| Ownership, admission, and final status, lines 161–184 | Appropriately limited | Auxiliary interface results and classical inputs are not counted as a paper. The original global assertion remains unproved. |

## Algebraic proof checks

### 1. Generic roots and the wild-order quotient

At infinity, the equations `u_i^2 - 1 = t u_{i+1}` have invertible residual Jacobian because `p` is odd. The Hensel solutions belonging to distinct sign words cannot share their first coordinate: forward iteration would then identify every coordinate and hence every residue. There are `2^n` solutions, equal to the degree of `f_c^n(x)-x`, so no roots or multiplicities are omitted.

For a prime power, every proper divisor of `n` divides `m`. Consequently the words removed by `f_c^m(x)-x` are exactly all words whose exact period is less than `n`. This validates both generic squarefreeness and the degree `N_n = 2^n - 2^m`. It does not say that all finite parameter specializations are squarefree.

After an algebraic closure of `F`, the algebra `A_n` is the function algebra of the geometric root set. Its invariant subalgebra consists exactly of functions constant on the free `C_n`-orbits. The constant group scheme `C_n` is étale in characteristic `p`; it must not be confused with `mu_n`. Thus a free action on this finite étale object gives a torsor of rank `n` even though averaging by `1/n` is unavailable. This proves the author's assertion without a semisimplicity assumption.

For completeness, the coefficient-generation argument is stronger than a trace argument for a precise reason. For any distinct cycles, at least one orbit-polynomial coefficient has different values. Over the algebraically closed scalar field, polynomial interpolation in these separating functions produces the indicator of each cycle. Therefore those coefficients generate the full cycle function algebra. Faithful flatness then descends equality of the subalgebra with `B_n`. No chosen individual coefficient is required to separate every pair.

### 2. Component counts and infinity

The stabilizer of one native cycle acts through the centralizer of its cyclic shift, which on that cycle is the cyclic rotation group itself. Its image of order `h_j` acts freely. For a point `omega` in the chosen cycle and a cycle `C = g C_j`,

$$G\omega\cap C = g(G_{C_j}\omega).$$

The intersection therefore has `h_j` elements in every one of the `r_j` cycles. Every point orbit over that quotient orbit has size `r_j h_j`; partitioning the `n r_j` points gives exactly `n/h_j` point factors. This proves `(CC)`, including all factors, not merely a divisibility bound.

Because the polynomial is monic over `k[c]`, an irreducible component cannot be supported over one parameter value. Generic separability prevents repeated horizontal factors. The passage to the reduced total curve in line 87 is consequently valid, and must not be replaced by a fiber-length or ordinary-multiplicity assertion.

The local sign complement is a fixed-point-free involution on the cycle sheets when `n` is odd. Every global orbit of cycles is invariant under this local inertia, hence has even size. Over algebraically closed `k`, the inertia orbits describe the points of the normalization above infinity, with no residue-field-degree factor. Thus the `j`th quotient component has `r_j/2` such points, each of ramification index two. These conclusions concern the normalized generic quotient; no smoothness assertion for every affine fiber follows.

### 3. What the small native cycle does and does not establish

The accepted small Hensel factor has `n` geometric roots forming one native cycle. Its invariants are therefore `K_s`, independently of whether its point algebra is a field. The latter would require transitivity of its local Galois action, not merely transitivity of iteration on its geometric roots.

If full local `C_n` inertia is supplied, its restriction is a subgroup of the global cycle stabilizer with the full possible rotation image. Hence `h_{j_*} = n`. Substituting into `(CC)` gives one point factor over that quotient component only. The argument cannot constrain the other quotient components. The exact joint implication is

$$\bigl(s=1\bigr)\quad+\quad\bigl(h_{j_*}=n\bigr)
\quad\Longrightarrow\quad\#\operatorname{Irr}(\Phi_n)=1.$$

Neither input is proved by the other. In particular, the review does not convert any bounded A3 calculation into an all-level local theorem, and does not treat LRL's small-cycle existence statement as a field-degree theorem.

## Satellite arithmetic and source applicability

The multiplier of a fixed point is `U = 2x`. Its fixed-point equation becomes `U^2 - 2U + 4c = 0`. In characteristic `p`, the ordinary cyclotomic polynomial for `p^e` reduces to `(U-1)^phi(p^e)`. Multiplicativity of the resultant gives

$$
\Delta_{p^e,1}(c)\bmod p
=\delta_1(1,c)^{\varphi(p^e)}
=(4c-1)^{p^{e-1}(p-1)}.
$$

The exponent is at least two, so the full multiplier polynomial has a repeated satellite factor after reduction. This is an exact all-level calculation, not a finite-sample extrapolation. It supplies no information on whether the separate primitive factor has repeated roots.

Primary-source checks made for this review:

- [Morton, 1996, Theorem 15 and Propositions 17–18, pp. 345–348](https://www.numdam.org/article/CM_1996__103_3_319_0.pdf): the original statements and relevant proofs were read. Theorem 15 requires hypothesis `(H)` and distinct roots modulo `p` of both `f(x,1)` and the full multiplier polynomial at multiplier one. Proposition 17 also imposes a fixed-point satellite discriminant condition excluding `p | n`; Proposition 18 retains a squarefree fixed-point satellite requirement. None supplies the missing wild-level conclusion.
- [Morton, corrigendum, pp. 332–334](https://doi.org/10.1112/S0010437X1000480X): the full corrective argument was read. The repair upgrades formal Hensel factors to polynomial factors using a uniform degree bound. It does not remove the distinct-root hypotheses or establish them at the present parameters. The report therefore uses the corrected scope rather than the uncorrected proof gap.
- [Doyle et al., accepted manuscript, §§3, 5–6, 8–9](https://api.repository.cam.ac.uk/server/api/core/bitstreams/17388c5b-06f8-4235-afed-8ae9a331c5f3/content): Proposition 3.25 distinguishes primitive quotient branching from satellite rotation. Propositions 6.2–6.4 and 8.1, with Corollary 8.3, give the quadratic model and isolated-branch specialization used here: finite flat cover, reduced special fiber, generically separable special map, separated branch sections, and compatible fiber identifications. The proof of Proposition 8.1 identifies the surviving inertia actions, supporting the author's orbit-count deduction. Theorem 9.1 supplies two-edge resilience, not arbitrary resilience; Proposition 8.6 requires its larger deletion-connectivity hypothesis. Proposition 6.15's tame point/quotient comparison excludes `p | n` and is not used to supply full wild inertia.

The Doyle statements and the relevant model/specialization proofs were read; its long combinatorial proof of Theorem 9.1 was not independently reconstructed. Bousch's thesis, Morton's 1998 low-period arguments, and the complete LRL proof were not freshly re-audited in this round. Their role here is source ownership or a declared accepted input, not an independently verified new theorem. This review does not certify that every source in the author's access ledger was itself reread by E4.

## Why the graph deduction has the stated scope

### The invariant-set argument

For a transposition, a subset is invariant exactly when the associated edge does not cross its boundary. For the single infinity permutation, invariance is equivalent to containing either both or neither vertex of each complement pair. It follows that the invariant subsets of the generated group `H` are exactly the unions of graph components. This establishes the graph/group correspondence without asserting that the individual infinity transpositions belong to `H`.

Under the imported common-fiber interface, let `G_sp` denote the special monodromy action on that identified sheet set. Its orbits are unions of `H`-orbits. The number `s` of quotient factors is the number of `G_sp`-orbits, giving

$$s\leq\#(H\backslash\mathcal C_n)=\#\pi_0(\Gamma_{p,n}^{\rm sep}).$$

This is an orbit-partition argument. It neither establishes an unrestricted specialization injection between fundamental groups nor identifies the surviving subgroup with the full special monodromy group. The compatible identification in lines 128 and 153 matters: independently relabeling each branch action would not justify this argument.

### Identification with the generic invariant algebra

The report's open-locus qualification is sufficient for the particular algebra `B_n`. One may restrict the integral point family to an open where `f_c^n(x)-x` is étale. Its discriminant is not identically zero after reduction by the infinity calculation already checked. On the prime-power dynatomic part of that open, the cyclic action is free in both relevant characteristics. The finite étale quotient there commutes with base change, so its generic special-fiber algebra is exactly the invariant algebra under review.

This argument concerns a finite étale free-action locus. It does not invoke an averaging operator, an arbitrary nonflat base change of invariants, or smoothness of the whole wild affine quotient. Completion/normalization for branch analysis must be kept distinct from that algebra identification, as the report does.

### One-way obstruction and the remaining uniform task

If special monodromy has more than one orbit, choose one proper nonempty orbit. It is invariant under every surviving action, including infinity, and hence is a union of complement pairs crossed by no surviving primitive edge. Every primitive crossing edge must therefore have been discarded. This proves the stated necessary obstruction.

The converse would require showing that discarded colliding clusters contribute no connecting monodromy. Nothing in the satellite identity, local small-cycle slope, or a primitive discriminant valuation establishes that assertion. The report explicitly avoids it.

The unresolved original question is still: for every odd `p` and every `e >= 1`, is `B_{p^e}` a field? A valid next closing input would be a proof of `(CUT)` with the actual primitive collision labels, or another uniform transitivity mechanism that also accounts for colliding clusters. Neither a uniform collision description nor either transitivity proof is present. The original target remains open in this package.

## Must-fix register and handoff

**Must-fix count: 0 for the finalized artifact and its stated scope.** The unresolved assertions at lines 139–144 and 159 are already marked as unresolved; they are not concealed proof gaps in a claimed theorem. They remain mandatory proof obligations before any upgrade to uniform `(GQ)` or point irreducibility.

Safe reusable outputs are `(CC)`, the even-degree/infinity constraint, the local `h_{j_*}` versus global `s` distinction, `(SAT)`, and the conditional surviving-action bound `(GB)`. Do not export `(CUT)` or `(GQ)` as proved, or export a collision-supported cut as a counterexample certificate. This review makes no paper-admission recommendation beyond preserving the author's auxiliary, not-closed disposition.

Verification consisted of full author-file reading, hand proof checking, and read-only primary-source retrieval. No mathematical program, old rerun, extra subagent, author edit, shared-index edit, Git operation, PDF build, formal evaluation, or external-model upload was performed. Only this new review file was written. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
