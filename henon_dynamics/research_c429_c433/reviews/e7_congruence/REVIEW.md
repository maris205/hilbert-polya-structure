# E7 — independent nonauthor proof/source audit of B1 and B2

2026-09-09 UTC. Reviewer: `c429_e7_congruence_review`, a current-session
nonauthor agent. This is a bounded mathematical/source audit, not human peer
review, a full ARS manuscript panel, a formal Route-A evaluation, or admission.

## Verdict

**AUXILIARY_ARGUMENTS_PASS; ZERO_SUBSTANTIVE_MUST_FIX;
LG4_UNCLOSED; NO_NEW_INDEPENDENT_PAPER_CONTRACT.**

B1's virtual-centralizer exclusion is proved under its displayed additional
target-location hypothesis. The return-ideal and reversing-symmetry controls
are valid all-time identities followed by exact finite separators. B2's
height criterion is an equivalence with the missing assertion, not a proof
of that assertion. Its discontinuity and finite-place escape-rate blindness
claims are correct within their explicitly stated scope.

Neither report supplies a full LG4 proof or an all-modulus false positive.
Their conservative `FULL_QUESTION_UNCLOSED` / `NOT_ADMITTED` dispositions are
appropriate. I found no mathematical or source-application defect requiring
revision before these results are retained as auxiliary material.

## Actual coverage and review boundary

The following complete submitted files were read, including their conclusions
and limitations, rather than relying on the coordinator's summary:

- [B1 REPORT](../../lanes/b1_congruence_separation/REPORT.md), all 329 lines.
- [B2 REPORT](../../lanes/b2_adelic_time/REPORT.md), all 189 lines.
- [B2 PROOF_PACKAGE](../../lanes/b2_adelic_time/PROOF_PACKAGE.md), all 241 lines.

Reviewed-file SHA-256 values, checked at final readback:

| File | SHA-256 |
| --- | --- |
| B1 REPORT | `3e4d2167fb53fa9c6e5f066dbeade050416cb0a6df89f84b931f9f9853a3dae7` |
| B2 REPORT | `babf312af3ff83546550aa9164cbeb4f27196a94580653b7d3478b092daf95fa` |
| B2 PROOF_PACKAGE | `dcbf9deaf55dc9b5bdc2c938c4200e81e8de8d75358e29111e5c050495a308d7` |

Imported local material actually checked:

- R4 arithmetic [PROOF_PACKAGE](../../../research_c424_c428/continuation_round4/arithmetic/PROOF_PACKAGE.md),
  all 322 lines, and its complete 69-line contract, 102-line source audit,
  and 36-line disposition. In particular, the valuation proof and the
  saturated-lattice argument were read, not just the theorem summaries.
- C394's complete `THEOREM_PACKAGE.md`, `SOURCE_AUDIT.md`, and 165-line
  [ANALYTIC_PROOF](../../../henon_padic_symplectic_analytic_interpolation_route_a/proof/ANALYTIC_PROOF.md).
  Its direct mathematical use here is local interpolation/ownership, not a
  new global height input.
- GR5 R5 arithmetic [proof](../../../research_c424_c428/continuation_round5/arithmetic/PROOF_PACKAGE.md),
  lines 1–146: exact map/model conventions, full theorem statement,
  assumptions, dependency map, Jacobian and leading-term proof passages.
  The whole class-group classification was not re-audited; B2's particular
  everywhere-good model is independently checked below without that theorem.

Only the five directly relevant external sources listed in the source section
were browsed. No source-discovery census or global novelty search was performed
by this reviewer. Prior authors' reported browsing/runs were not re-executed
or independently certified as historical events.

## B1: virtual-centralizer proof

### Exact claim and inherited profinite input

The claim at B1 lines 74–85 quantifies over the original integral plane
automorphisms and integer points, but adds

\[
Q=G(P),\qquad G\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2),
\qquad GF^k=F^kG\quad(k\ge1).
\]

It is essential that both the inverse of F and the inverse of G are integral,
as stipulated. The proof does not infer integrality from a Jacobian condition.

The R4 input is sound. Its coefficientwise near-identity calculation uses
\(z+p^2U(z)\), including at 2. The error valuation is at least \(s+2\),
so the single-step p-fold calculation increases displacement valuation by
exactly one. The scaled return map is affine modulo p coefficientwise;
raising it to the order of that finite affine map and then to p gives the
required coefficientwise form. This proves unbounded p-primary divisibility
of native point periods for every p. It does not discard the finite
prime-to-p part of an individual local return clock.

Using every native \(r_m\), the map \(\theta_P\) has compact image equal to
the full congruence orbit closure. Its kernel is zero because each p-component
is divisible by arbitrarily high powers of p. The all-modulus hypothesis
therefore gives one unique full profinite time for nonperiodic P; it does not
already give integer time. Mixed-modulus compatibility is retained throughout.

### Centralizer, power relation, and arithmetic conclusion

The finite-by-cyclic centralizer theorem is applicable to dynamical degree
greater than one, not merely ordinary coordinate degree greater than one.
The source passage supplies a finite kernel for the signed axis-translation
homomorphism \(\ell:C(F)\to\mathbb Z\). B1 correctly avoids replacing a
semidirect product by a universally asserted direct product.

Here is the exact quotient step independently checked. Since F is central in
its own centralizer, \(\langle F\rangle\) is normal. Write \(K=\ker\ell\).
F has infinite order, so \(\ell(F)\ne0\). The quotient homomorphism

\[
C(F)/\langle F\rangle\longrightarrow
\ell(C(F))/\langle\ell(F)\rangle
\]

has finite target. If a coset lies in its kernel, choose b with
\(\ell(c)=b\ell(F)\); then \(cF^{-b}\in K\), so this kernel is an image
of K and is finite. Consequently every coset of G has finite order, giving
\(G^a=F^b\) for some positive a and integer b. No arithmetic model for the
source's chosen generators is needed.

When G commutes with F and \(GP=\theta_P(t)\), integral continuity and the
density of ordinary times give
\(G\theta_P(s)=\theta_P(s+t)\). Hence \(G^aP=\theta_P(at)\).
The power relation and injectivity yield \(at=b\) in
\(\widehat{\mathbb Z}\). Reducing this equation modulo a proves ordinary
integer divisibility \(a\mid b\); then multiplication by a is injective
on every \(\mathbb Z_p\), proving \(t=b/a\in\mathbb Z\).
There is no division of a general profinite element by a nonunit without
first checking divisibility.

For commutation only with \(F^k\), B1 lines 146–161 correctly select
\(j\in\{0,\ldots,k-1\}\) from the *full* time modulo k. The kernel of
\(\widehat{\mathbb Z}\to\mathbb Z/k\mathbb Z\) is exactly
\(k\widehat{\mathbb Z}\); injectivity of multiplication by k gives unique
u with \(t=j+ku\). Set \(A=F^k\), \(H=F^{-j}G\). Then H is integral
with integral inverse, HA=AH, and

\[
HP=\theta_P(ku)=\theta_{A,P}(u).
\]

The last identity holds on ordinary u and extends by continuity. P is still
nonperiodic for A, whose dynamical degree is greater than one. Applying the
commuting case gives ordinary u and finally the native time \(j+ku\).
This does not secretly restrict the orbit to the residue-zero subclock.

### Exhaustion of the periodic and bounded-degree branches

Periodic P has a finite integral orbit, so a single sufficiently large
modulus separates any other integer Q. The R4 periodic-target proof also
works by invariance of a finite cycle in a finite permutation.

For the bounded-degree branch, the R4 space W and saturated lattice
\(L=W\cap\mathbb Z[x,y]_{\le D}\) are invariant under both pullbacks.
The original coordinate functions belong to L, so the lattice evaluation
map is injective with an *integer* coordinate recovery map. Thus it passes
all congruences into an action of one matrix in \(\mathrm{GL}_N(\mathbb Z)\),
where Segal's theorem applies with \(M=\mathbb Z^N\) and \(G=\langle A\rangle\).
There is no denominator or excluded-prime gap.

The elementary/Hénon dichotomy can be used over C here without assuming an
integral conjugator. If \(F=T^{-1}ET\) with E elementary, then all positive
and negative iterates of E have bounded degree, and

\[
\deg F^n\le(\deg T^{-1})(\deg E^n)(\deg T)
\]

uniformly. R4 is then applied to the original integral F, not to an
arithmetically conjugated model. This validates the exhaustive branch step
at B1 lines 163–167. Conversely the Hénon branch has dynamical degree greater
than one, as required by the centralizer theorem.

### Return ideals and reversing symmetries: exact controls

B1 lines 177–197 correctly use polynomial difference divisibility in both
directions to prove \(I(FA,FB)=I(A,B)\). The argument applies to all integer
iterates. Same modular cycle implies simultaneous returns at every time;
prime-power divisibility determines the nonnegative ideal generator,
including generator zero. Thus equality of all return ideals is necessary.

For \(F(x,y)=(y,y^3-x)\), oddness of F and its inverse proves the identity
\(F^n(-P)=-F^n(P)\) for *every* integer n. It therefore proves all return
ideals equal for \(P=(1,2)\), \(Q=(-1,-2)\), without sampling n.
The claimed mod-7 cycle checks term by term: successive second coordinates
are \(8-1=7\), \(-2\), \(125\), \(216-5=211\), and \(1-6=-5\), reducing
to \(0,5,6,1,2\). The five displayed points are distinct and the next is
P. The target \((6,5)\) is absent, so the complete two-sided modular orbit
excludes Q. The increasing positive cubic recurrence proves nonperiodicity.

For \(F(x,y)=(y,y^5-y-x)\), direct inversion gives
\(F^{-1}(x,y)=(x^5-x-y,x)=RFR(x,y)\). Modulo 5 the map is exactly
\((y,-x)\). Starting at \((1,2)\), it successively reaches
\((2,4),(4,3),(3,1),(1,2)\), never \(RP=(2,1)\).
Thus reversibility alone does not imply modular incidence.

If a reverser *also* preserves the relevant orbit closure, its action is
\(s\mapsto t-s\); squaring imposes no restriction on t. This shows only
that the commuting torsion argument cannot be reused unchanged. Neither
this observation nor the example proves that a reversing-symmetry approach
to LG4 is universally impossible.

The displayed separators are prime moduli, which already suffice for an
all-modulus assertion. If a literally mixed modulus is desired, 14 separates
the cubic example by reduction to 7, and 10 separates the quintic example
by reduction to 5. No mixed-modulus cycle computation is required.

## B2: height compatibility and finite-place blindness

### Height criterion and product formula

In B2 Proof §1, every nonempty hitting set is exactly
\(C_m=a+r_m\mathbb Z\), for negative as well as positive times. The minimum
\(\mu_m\) exists by well-ordering of positive integer heights; no effective
minimization algorithm is asserted.

Under all-modulus incidence, all four conditions in that section are
equivalent as written. Bounded heights along factorial-modulus hits produce
one repeated point R in a finite integer box; unbounded factorial divisors
of each coordinate of R−Q force equality. A true hit provides one bounded
representative for every modulus. The single-representative condition
\(\|F^nP-Q\|_\infty<m\) also forces equality coordinatewise.

This is a correct reformulation of the missing global rigidity assertion.
It supplies no independent bound, effective height estimate, or contraction
of the original quantifiers. The report explicitly acknowledges this at
lines 99–104. Its source-subtracted mathematical progress toward a *proof*
of LG4 is therefore not the equivalence itself.

Proof §2 correctly obtains a lower bound at least m on a nonzero coordinate
difference divisible by m. These differences vary with m. The product
formula does not make them one fixed integer divisible by unbounded moduli,
nor does it supply the needed upper bound for the same representatives.

### Discontinuity statement

For nonperiodic P, injectivity of \(n\mapsto F^nP\) and finiteness of every
integer height box imply \(H(F^{a+kr}P)\to\infty\) as \(|k|\to\infty\),
for every ordinary a and positive r. Every nonempty relatively open subset
of the congruence orbit closure contains the orbit points in some residue
coset, so ordinary height is unbounded there.

It follows that a real-valued extension agreeing with height on the ordinary
orbit cannot be continuous at even one point. A continuous real-coordinate
orbit interpolation on compact \(\widehat{\mathbb Z}\) is likewise impossible.
The chosen \(n_j\), divisible by both \(j!\) and \(r_{j!}\), really tend to
zero in full profinite time while their orbit points tend to P in the finite
adelic product and their ordinary heights tend to infinity.

This is a universal no-go for that *continuous-extension mechanism* on
infinite integral orbits. It is not a no-go for height-small choices in each
hitting coset, discontinuous selections, stronger arithmetic estimates, or
LG4. In particular, for Q=P the small representative n=0 survives every
modulus despite the existence of other arbitrarily large representatives.

### Escape rates and the mod-2 countercontrol

Proof §4 needs no unproved good-reduction implication. Integral F and its
integral inverse preserve \(\mathbb Z_p^2\), so every logarithmic escape
numerator on that locus is zero. Both normalized limits vanish for any
\(D>1\); where standard Green functions are defined, these are their values.
After any fixed affine change over \(\mathbb Q_p\), the orbit lies in the
bounded image of \(\mathbb Z_p^2\), which still gives zero normalized rates.
This does not erase other local invariants such as displacement valuations.

For the concrete map \(F=(y,y^2-x)\), the projective maps are
\([YZ:Y^2-XZ:Z^2]\) and \([X^2-YZ:XZ:Z^2]\). Their indeterminacy points
are respectively \([1:0:0]\) and \([0:1:0]\) over every residue field.
Both maps retain degree two and have integral coefficients and unit
Jacobian. The identity model is therefore regular-good everywhere,
including at 2. GR5's notation indeed has \(a=b=1\) and \(q=Y^2-Y\).

The recurrence from \((0,2)\) begins \(0,2,4\) and is strictly increasing
thereafter by the displayed inequality, proving nonperiodicity. Modulo 2,
P is \((0,0)\), fixed under F; \(Q=(0,3)\) is \((0,1)\), so it is absent
from the full modular orbit. The two points nevertheless have identical
all-zero finite-place Green vectors. Projection also gives separation
modulo 6 if a mixed modulus is wanted. This disproves sufficiency of this
observable, not all-modulus orbit separation.

## External source verification and ownership subtraction

All following access was on 2026-09-09 UTC. No private report was uploaded.

| Source and actual inspected passage | Verified input and limitation |
| --- | --- |
| [Lamy, *L'alternative de Tits pour Aut[C²]*](https://www.math.univ-toulouse.fr/~slamy/stock/lamy_algebra.pdf), pp. 414–415, Corollary 4.6, complete Lemma 4.7 and Proposition 4.8 statements/proofs, Remark 4.9 | The degree convention is dynamical. The centralizer has a finite cyclic axis-fixing subgroup and cyclic translation quotient. The finite-by-cyclic property is sufficient; the review does not need a direct-product assertion. The parsed product glyph is degraded, so the readable generator/relation proof and introductory wording were used, not a guessed symbol. No successful visual screenshot inspection is claimed. |
| [Segal, *Some aspects of profinite group theory*](https://www.math.auckland.ac.nz/~obrien/segal-survey.pdf), Theorem 7.2.3(i) and adjacent §7.2.2–7.2.6 discussion | The exact theorem covers a virtually polycyclic automorphism subgroup acting on a virtually polycyclic group. Both hypotheses hold in R4's matrix reduction. Segal's original book proof is cited by the survey but was not rederived or read here. This audit verifies the authoritative stated input and its application, not the entire classical theorem from first principles. |
| [Amerik–Kurlberg–Nguyen–Towsley–Viray–Voloch, author-hosted 19-page version](https://kurlberg.github.io/eprints/dbm.pdf), Theorems 4.2–4.3 statements and §4.6, complete Proposition 4.9/proof | Invariant/preperiodic target assumptions remain material. The predecessor-point obstruction concerns forward time; it is a genuine two-sided orbit point. The positive singleton condition involving nonperiodic reductions cannot apply to these finite permutations. This version's Proposition 4.9 is not silently relabelled as the fixed arXiv-v2 numbering. |
| [Poonen, *p-adic interpolation of iterates*](https://math.mit.edu/~poonen/papers/p-iteration.pdf), Theorem 1, complete proof, Remarks 2–4 | The threshold is coefficientwise \(c>1/(p-1)\). The dyadic issue is genuine. This is a local restricted-analytic interpolation theorem, not a real extension or a classification of diagonal integer times. |
| [Kawaguchi, *Local and global canonical height functions for affine space regular automorphisms*](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf), Proposition 4.3/proof, complete Theorem 6.3 statement, Proposition 7.5/proof | The height decomposition includes all places. Proposition 7.5 uses finite-place bounds outside a finite set and boundedness at the remaining places, including archimedean ones, to obtain a finite height box. It does not supply a bound for the varying congruence-hitting representatives. The entire canonical-height theorem proof was not audited. |

The source subtraction is decisive. B1 VC combines imported full profinite
time with classical centralizer structure. Its invariants and controls are
useful elementary route exclusions. B2 contributes elementary compatibility
diagnostics and explicit controls; HC is a new presentation of the same
missing implication. None is shown to close a substantial independent new
question at the batch's paper-admission threshold. No worldwide openness,
priority, or literature-novelty conclusion follows from this bounded review.

## Must-fixes, optional precision, and allowed claims

**Substantive must-fixes: none.** No author-source files were changed.

Two optional presentation improvements, not proof blockers:

1. B1 lines 163–167 could include the explicit complex-conjugacy degree
   bound above, making it unmistakable that integral conjugacy is not used.
2. B2 REPORT line 71 could say “No **continuous** real orbit interpolation”
   within the table cell itself. The row heading and proof already supply
   this qualifier; discontinuous set-theoretic maps are not excluded.

Allowed claims for coordinator integration:

- B1 VC holds with the displayed integral virtual-centralizer hypothesis,
  including periodic P, the bounded-degree branch, and the original native
  clock for k>1.
- Equality of all return ideals is necessary but insufficient; reversibility
  by itself does not force even one-prime cycle incidence.
- B2 HC is equivalent to the missing LG4 implication. It is not established
  under the all-modulus premise.
- Ordinary height has no continuous extension at any point of an infinite
  integral profinite orbit; all finite-place forward/backward escape rates
  vanish on the integral locus and remain zero after fixed affine changes.
- These are specific method/observable boundaries. General LG4 is neither
  proved nor refuted, and no auxiliary item should be promoted into a paper
  merely to fill a batch slot.

Review execution: zero mathematical programs, old reruns, builds, formal
evaluations, Git/shared-index mutations, extra agents, or external model/API
uploads. The only created deliverable is this assigned review file.
Research-review/ARS guidance supplied evidence anchoring and explicit source
limits; no full-panel, external-model, or human-review process is claimed.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains intact.
