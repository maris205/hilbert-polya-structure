# Independent review: full degree-2p resonant Hénon–Frobenius counts

2026-09-07. Reviewer: current-team agent `/root/scout_henon_arithmetic`,
not an author of this resonance extension. The coordinator requested a
non-author proof/source/substance gate because the coordinator contributed
to the proposed generalization. This is internal AI-assisted review, not
human peer review, publication approval, or a worldwide-priority certificate.

## Verdict and scope

**Mathematics: PASS; the minor analytic-domain wording correction is closed
in the confirmation below.** The all-odd-prime, all-`q=p^e` with `e>=3`, all-degree-`2p`
coefficient family is covered. I found no unresolved coefficient cancellation,
fractional-tail gap, denominator descent, period conversion, or substitution
of intersection length for ordinary geometric points.

**Substance: recommend one bounded full-family contract for the coordinator's
admission decision.** This recommendation applies to the entire exhaustive
support classification, after the deductions in Section 5. The strict-gap
lemma by itself remains an unadmitted companion. Neither the degree-six
precursor, the pure-pth-power face, nor the analytic corollary is another
independent paper. No formal admission or C-number is assigned by this review.

Actual inputs:

- [PROOF_NOTE.md](../positive_characteristic/PROOF_NOTE.md), 289 lines read;
  initial SHA256 `e9fa106663e5315fab16560785dd4e21034c99c094a3cadbd8174d9c8a9d641f`.
  The mathematical verdict here concerns its resonance Sections 1–4, which
  feed the full theorem. I did not independently factor its separate wild
  cubic fifth-iterate certificate in Section 5.
- [FULL_DEGREE_2P_PROOF.md](../positive_characteristic/FULL_DEGREE_2P_PROOF.md),
  all 284 initial lines read; initial SHA256
  `bd75264df2ef35f40a897c976ac9f4353bf269f3c3b5e998d37d74cf5b647f58`.
- [SOURCE_AUDIT.md](../positive_characteristic/SOURCE_AUDIT.md), all 80
  initial lines read; initial SHA256
  `91a0537fb27c04f1c2108c4edcbd47c4baa38b3f3b39b96a043e5fb65a19fc94`.
- [C404's proof package](../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md),
  all 320 lines read for exact inherited scope; SHA256
  `0c59a129ba1dfbb3f22c527c40f4065cf8748cc570a302f0b3ba801a98289ea6`.

I inspected no precursor as a substitute for the generalized proof. No
producer file, registry, manuscript, evaluation, or frozen package was
modified. No large census, GPU experiment, sealed test rerun, or external
model/API review was performed.

## 1. Existing strict-gap theorem: verified, but not independently substantial

The binomial first-index statement is correct for every positive integer
exponent `D`: writing `D=p^v d` with `p` not dividing `d` yields first
nonzero index `p^v`. Since `m<q`, subsequent indices have strictly lower
degree. This does not assume that the operator difference is a ring map.

In the two-term induction, `A_j` is zero or divisible by `q`; since
`m<q`, `v_p(A_j+m)=v_p(m)`. Also `A_j+ell` is nonzero modulo `p`.
The index-one image of the latter exponent creates both retained terms.
The first strict gap suppresses its higher indices, the second suppresses
the former exponent's first surviving index, and the entire bivariate
remainder has degree at most `q(A_j+ell-1)`. The coefficient recurrence
`C_(j+1)=c ellbar C_j` is nonzero over the whole field `F_q`, not just
its prime subfield. Thus the displayed top degree and coefficient hold at
every operator iterate.

The all-period conversion uses `w=p^(v_p(n))`, not `v_p(n)`, and the
remaining factor `s=n/w` is nonzero in the coefficient field. Both original
pullbacks preserve coefficients and multiply the degree of a unique pure
top monomial by `q`. The resulting coprime leading monomials give the
stated finite quotient basis, while `det DH^n=a^n` proves reducedness.
All these conversion steps are already present in C404 and are credited.

I also checked the separate degree-six comparison algebraically: the given
expansion of `delta^2(y)` for `g=y^6` follows from squaring the cubed
expression in characteristic three. The `2y^99` term has next first
binomial index nine and produces degree 2484; every other term is bounded
by degree 2268 after applying `delta`. For `g=y^6+y^5`, the strict-gap
formula gives degree 3030. The resulting different point counts really
refute coefficient blindness at fixed total degree. This finite comparison
does not establish the full-family theorem.

## 2. Full support partition and automatic high-branch bounds

For degree `2p`, each exponent strictly between `p+1` and `2p` is
nonzero modulo `p`. If any such coefficient is nonzero, its largest
exponent `ell` leaves only the top `2p` term above it; the polynomial is
exactly of the strict-gap form. Here `1<=h=2p-ell<=p-2`, and the worst
second-gap lower bound is

\[
p^3-2p(p-1)>p-2.
\]

This is strict already at `p=3`, and grows for larger odd primes. The
first gap is also strict under `q>=p^3`. Thus no tie or missing intermediate
coefficient stratum is silently omitted from the high-support branch.

If none of those coefficients is present, every remaining polynomial has
the exact form `b y^(2p)+c y^(p+1)+R_0`, `deg R_0<=p`, with `c` allowed
to vanish. The two cases are disjoint and exhaustive. In particular the
previously missing `y^4` boundary stratum in characteristic three is now
inside the low case, not disguised as a case of the old strict-gap lemma.

## 3. Perfected-ring invariant and coefficient descent

The concrete union of polynomial rings with p-power-root variables is an
integral ring of finite sums. It has unique monomial expressions and unique
pth roots. No convergence assumption or infinite formal expansion enters.
The two original ring maps extend uniquely, commute with Frobenius and its
inverse, and satisfy

\[
\delta(P^p)=(\delta P)^p,
\qquad \delta^j=L^j\mathcal D^j.
\]

Thus `Dcal=L^(-1)delta` is additive and `sigma`-semilinear; it is not
being treated as an `F_q`-linear polynomial-map difference. In particular,
the proof correctly keeps `sigma(c)=c^(1/p)` for non-prime-field
coefficients. For a mixed monomial of arbitrary denominator level, the
degree estimates for `V` and `W` imply `deg Dcal P <= Q deg P`, with
`Q=q/p`. This estimate is uniform in the level and support.

For an integer `E` congruent to two modulo `p`, the leading binomial
coefficient is exactly the nonzero field element two. The image of
`y^E` has the asserted two retained terms at exponents `E'` and
`E'-(p-1)/p`. All other index-one terms are at most `E'-1`; higher
indices are even lower because `Q-2>=7`.

The delicate term is `y^(E-(p-1)/p)`. I independently checked its
numerator `M=p(E-1)+1` and the finite root identity used in the proof.
Its first inner binomial index is one, so its image has exact degree

\[
\frac{Q(M-1)+2}{p}
=Q(E-1)+\frac2p
=E'-2+\frac2p<E'-1.
\]

This is strict for every allowed prime. In contrast, a crude total-degree
bound on that fractional term would not close the induction. The proof
therefore resolves the needed term explicitly rather than hiding it inside
the remainder. The old mixed remainder contributes at most
`Q(E-1)=E'-2`. Only the previous leading term can produce either newly
retained coefficient, so there is no cancellation with the fractional tail.

The recurrence preserves `E_j=2 mod p` and gives
`alpha_(j+1)=2 B sigma(alpha_j)`, with `alpha_j` always nonzero. Vanishing
`c` merely makes every secondary coefficient zero; no step divides by it.
Denominator levels grow by at most one under `Dcal`, and raising the
`j`th state to its `p^j`th power gives exactly the ordinary polynomial
`delta^j(y)`. The secondary and remainder degree bounds stay strictly
below the top after this descent.

The resulting leading coefficient satisfies

\[
c_{j+1}=2b^{p^j}c_j,\qquad
c_j=2^{j-1}b^{(p^j-1)/(p-1)}.
\]

Both the exponent sum and all coefficient twists are correct. The closed
degree formula is `p^j E_j`, equal to the stated expression with denominator
`q-p`; its integrality follows from the integer recurrence, not from formal
division inside `F_q`.

## 4. Every period, ordinary points, and the inherited analytic corollary

After descent all coefficients are again in `F_q` and the conversion uses
the original `T,U`, not the semilinear auxiliary maps. Their commuting
operator identity at `w=p^(v_p(n))` therefore applies exactly as written.
The unique top coefficient becomes `(n/w)c_w`, which cannot vanish.
Both class recurrences give `0<D_j<q^j`, including `j=1`, so the literal
fixed equations have the claimed actual degrees and coprime leading forms.

The rectangular standard-monomial basis establishes finite length and the
absence of a projective infinity correction. The derivative of the
Frobenius terms vanishes and `det DH^n=a^n!=0`, proving a finite reduced
scheme. Its geometric points, rather than only its intersection length,
are counted by `q^(2n-w) D_w`. Finally commutation of `H` with `Phi`
identifies the equalizer with fixed points of the single map `S^n`. Neither
perfection nor the operator index changes that clock.

I checked the stated triples `(A,B,theta)`: both classes have positive
`A,B`, `0<theta<1`, and `A+B theta=2p/q`. C404's logarithmic argument
then applies with `theta` in place of `1/q`; it only needs summability
and positivity of the exponents, not a new group interpretation. At a
primitive `p^a`th root with `a>=1`, the radial order is the positive
summable tail. It tends to zero as `a` grows, so any fixed positive
integer power has nonintegral orders on a dense set of those roots.

The one requested wording correction is to insert **`a>=1`** explicitly
in Section 7. At `a=0`, the root is one and the prefactor contributes to
the order, so the unqualified positive-tail statement should not include
that case. The intended natural-boundary proof already uses only `a>=1`
and is unaffected. This is an inherited consequence of the count theorem,
not a second independent contribution.

## 5. Ownership deduction and substantive judgment

The following distinction is essential to the recommendation:

| Component | Deduction / remaining contribution |
|---|---|
| Commuting pullbacks, characteristic-p binomial step, all-period clock, Gröbner quotient and Jacobian reducedness | Already supplied by C404; not new |
| High-support strict-gap block | Already supplied by this batch's companion note; not independently a paper |
| Pure-pth-power support and the formal use of perfection | Not a separate fresh theorem or source of novelty credit here |
| Mixed low support, including arbitrary nonzero `y^(p+1)` coefficient and arbitrary lower terms | Requires the new fractional two-term invariant and semilinear descent |
| Exhaustive high/low classification for every odd `p`, every allowed `q` and all coefficients | One coherent full-family conclusion assembled from the inherited and new pieces |
| Product expansion and natural boundary | C404's analytic mechanism, deducted rather than counted again |

The low-branch degree recurrence resembles C404 with parameters `(Q,2)`.
That resemblance does **not** make C404 directly applicable: the auxiliary
maps are semilinear over `F_q`, have fractional coordinate expressions,
and the exceptional term has degree strictly between `E-1` and `E`.
It violates the integer-remainder hypothesis used in C404's leading-term
lemma. The new fractional-tail estimate is exactly what repairs that
obstruction, without pretending to produce a polynomial conjugacy.

After those deductions, the surviving theorem describes the whole specified
inseparable-degree coefficient space with an explicit support threshold.
It closes the previously open mixed boundary stratum and proves stability
under every lower coefficient, at every height, uniformly across odd
characteristics. That is a meaningful complete classification question,
not a numerical table or a relabeled non-p-divisible degree. I therefore
recommend it as **one** bounded substantive contract. The recommendation
would not extend to submitting the high branch, pure face, degree-six
specialization, or analytic corollary separately.

The comparison is bounded, not a claim of universal novelty. I independently
opened Bridy's [published primary PDF](https://www.numdam.org/article/JTNB_2016__28_2_301_0.pdf)
and read its introduction, Theorems 1.2–1.3, Conjecture 1.4, and dynamically
affine setup. Its proved rational-map classification is one-dimensional;
it does not furnish this two-dimensional mixed-support leading-state
classification. I also read the [Stacks Frobenius lemma](https://stacks.math.columbia.edu/tag/0CC8),
which supplies classical radicial background, not the new counts.
The [Byszewski–Cornelissen–Houben v2 record](https://arxiv.org/abs/2209.00085v2)
was read only at metadata/abstract level. It concerns smooth algebraic-group
endomorphisms; it is not evidence that the present maps satisfy a hidden
group presentation, nor a proof that all such presentations are excluded.
No full reading of that 176-page work or later global-conjecture status is
claimed. The direct degree argument, not metadata or unsuccessful searching,
supports the mathematical verdict.

The initial source audit and strict-gap note document a historical missing
full-family theorem. That earlier limitation should remain visible as
history, with an explicit follow-up identifying the generalized proof and
its actual current review status; it should not be silently rewritten into
an earlier successful claim.

## 6. Allowed conclusions and review dialogue

Allowed: the stated full degree-`2p` classification and reduced counts on
the specified single-map clock, and the inherited source-zeta consequence
with the root-order qualifier above. Not allowed: every inseparable lower
degree, `p=2`, `e=1,2`, arbitrary coefficient fields, wild-cubic forward
multiplicity classification, hidden-group exclusion, or worldwide priority.
No target Euler factor, root number, automorphy, target divisor/zero bridge,
Hilbert–Pólya realization, or Route B entry follows.

Review sequence: the original strict-gap argument was checked first against
actual C404 ownership and retained as companion-level. The author then
provided the complete generalized artifact, which was read and checked
independently in full. The reviewer requested the single explicit `a>=1`
qualifier and preservation of historical source status. No mathematical
repair or additional census was needed. Formal admission and subsequent
five-contract planning remain the coordinator's responsibility.

## Revision confirmation — 2026-09-07

I checked the corrected Section 7 sentence: it now explicitly restricts the
primitive-root order to `a>=1`. The final proof SHA256 is
`683f4212a1f405fc4d2d5c67ba88e00a34595fb4172a25f1cdad9604841317f5`.
A read-only stream replacing just that sentence by its original wording
recovers the exact initial proof hash recorded above. Thus no other proof
bytes changed, and no renewed mathematical review or test rerun was needed.

I also read the complete appended source/ownership delta and the revised
scout introduction. They distinguish the initial missing theorem from the
new author proof, preserve the source-access limitations, and deduct the
classical/C404/companion inputs without making extra paper claims. The
revised source audit SHA256 is
`670b5e33dcee25b230589d68da750f737b2162616fd9b6b439bd3ec44e84630e`.
Those source-status requests are closed as well. The mathematical PASS and
the one-contract substantive recommendation stand; formal admission is
still the coordinator's decision.
