# Positive-characteristic candidate screen: C409–C413 research stage

2026-09-06. Five distinct source mechanisms were screened initially;
a separately authorized rational-map follow-up is recorded at the end.
This file is not a five-contract freeze or an admission record. The
fourth initial candidate remains the lane's substantial recommendation.
The rational follow-up has a complete proof and passed bounded checks,
but the coordinator rejected it as a separate paper on substance grounds;
it is retained as a companion mathematical note.
No old weighted-zeta note, period-12 census, or C404 resonance calculation
was promoted or rerun.

| Candidate | Exact object and observable | Decisive result | Disposition |
|---|---|---|---|
| PC-A | `f_b=x+(x^2+b)^p` over `overline(F_p(b))`, odd `p`, transcendental `b`; ordinary geometric fixed points at forward time `n` | Prime-to-`p` counts close, but the full local `p`-power tower does not. Direct minimally-ramified extrapolation fails. | Do not admit a partial-period paper. |
| PC-B | `F_(lambda,P)(x,y)=(x^p,y^p+lambda y+P(x))`, `lambda in F_p`, `P in F_p[x]`; ordinary geometric and finite-field fixed counts | Forcing is sheared away when `lambda!=0`; when `lambda=0`, counts depend only on the root counts of `P`. | Complete short collapse lemma, not a new substantial owner. |
| PC-C | Artin–Schreier correspondence `y^p-y=x^(p+1)+c`, all primes `p`, transcendental `c`; ordinary closed-chain counts at shift time `n` | Monic leading terms and the valuation at `c=infinity` give exactly `(p+1)^n` reduced closed chains for every `n`. | Complete short degree/transversality lemma, not a paper slot. |
| PC-D | `f_a=x^3+a x^2`, `char(k)=3`, every `a in k*`; generic inverse-image fields of `t`, their actual Galois tree action, ramification and genera | A mixed Kummer/Artin–Schreier induction is written in `WILD_CUBIC_PROOF.md`; equality with the classical group `E_n` is proved by ranks, not inferred from a sign upper bound. | Best candidate; bounded exact checks passed (`EXACT_CHECK_REPORT.md`); independent admission review is owned by the parent agent. |
| PC-E | `g(X)=X+X^2` on `t F_p[[t]]`, odd `p`, with ordinary finite-quotient cycles and orbit-closure metric | Complete displacement/cycle formulas are direct consequences of classical minimal ramification; the zero-dimensional procyclic closure is also classical. | Source/repository collision; no additional paper slot. |

## PC-A: derivative-one nonlinear polynomial

Parameters: odd prime `p`, transcendental `b`, algebraically closed field
`overline(F_p(b))`; degree `D=2p`. Clock: forward iterate `n`. Observable:
the number of distinct roots of `f_b^n(X)-X`, not scheme length and not
Jacobian-weighted counts. Classical inputs: characteristic-`p` iteration,
formal ramification theory, and Bridy's dynamically affine boundary.

Write

    R_n(X,b)=sum_{j=0}^{n-1}(f_b^j(X)^2+b).

Then `f_b^n-X=R_n^p`, `partial_b R_n=n`, and `partial_X^2 R_n=2n`.
For `p` not dividing `n`, these imply geometric squarefreeness of `R_n`.
Indeed a repeated irreducible factor in `F_p[b,X]` would divide its
`b`-derivative, a nonzero constant. Gauss's lemma excludes repeated
separable factors after passing to `F_p(b)`. Any inseparable irreducible
factor would produce geometric root multiplicity at least `p>=3`, which
is impossible when the second derivative is a nonzero constant. Thus

    #Fix(f_b^n) = D^n/p,    p not dividing n.

This does not determine the counts when `p` divides `n`. At a fixed point
`alpha^2+b=0`, the local return germ is

    g(u)=u+A u^p+u^(2p),    A=(2alpha)^p.

The finite exact probe `constant_derivative_jet_probe.py` found the
following initial orders for the displayed coefficient specializations:

| p | A | iterate indices | orders of `g^n-u` |
|---|---|---|---|
| 3 | 1 | 1,3,9,27 | 3,18,243,3888 |
| 3 | 2 | 1,3,9 | 3,18,243 |
| 5 | 1 | 1,5,25 | 5,250, at least 8000 in the fixed truncation |
| 7 | 1 | 1,7 | 7,1372 |

The generic-coefficient first-`p`-iterate probes gave leading terms
`2 A^6 u^18` for `p=3`, `A^60 u^250` for `p=5`, and
`3 A^196 u^1372` for `p=7`. A truncated zero is not an identity claim.
These are new local diagnostic inputs, not retests of frozen batches.

The missing lemma is the exact ramification sequence of every first
return germ at every periodic cycle, through every `p`-power iterate,
uniformly in the admitted parameters. The existence of non-isotrivial
constant-derivative PCF families and multiplier blindness is already in
Levy's work. Neither that classical phenomenon nor the prime-to-`p`
formula alone is a substantial closed contract. This branch is stopped.

## PC-B: nonlinear triangular forcing and its exact collapse

Parameters and domain: any prime `p`, `lambda in F_p`, `P in F_p[X]`,
either `A^2(overline(F_p))` or `A^2(F_(p^r))`. Both the map-iterate clock
`n` and field-extension degree `r` are kept. The proposed new theorem was
a forcing-sensitive ordinary count, not a weighted trace. The minimal
failure condition was an explicit conjugacy or a count blind to `P`.

For `lambda!=0`, put `H(x,y)=(x,y+P(x)/lambda)`. Direct substitution gives

    H F_(lambda,P) H^(-1)(x,y) = (x^p,y^p+lambda y).

Thus the forcing disappears by a polynomial automorphism defined over
F_p, and all ordinary orbit data are those of a product of additive
maps. The finite-field count is the existing normal-basis/gcd formula

    #Fix(F^n on F_(p^r)^2)
       = p^(gcd(n,r)+deg gcd((T+lambda)^n-1,T^r-1)).

For `lambda=0`, direct iteration gives

    F^n(x,y)=(x^(p^n),y^(p^n)+n P(x)^(p^(n-1))).

Let `g=gcd(n,r)` and let `R_g` be the number of distinct roots of `P`
in `F_(p^g)` (so `R_g=p^g` for the zero polynomial). The additive Hilbert
90 trace criterion gives the complete finite-field formula

    #Fix(F^n on F_(p^r)^2) = p^(2g),    if p divides n*r/g,
                            p^g R_g, otherwise.

Proof: the base coordinate lies in `F_(p^g)`. The fiber equation has
kernel size `p^g` and is solvable exactly when the relative trace of
`-n P(x)^(p^(n-1))` is zero. This trace is `-n(r/g)` times that same
element of `F_(p^g)`. Over the algebraic closure every fiber equation has
`p^n` distinct roots, so the geometric count is always `p^(2n)`.

The actual finite-field map is a permutation, but its nonlinear forcing
contributes only the root portrait of `P` to these counts. This is a
short, completely quantified collapse, not a theorem classifying all
polynomial conjugacies of nonlinear maps. C384/C204 already own the
additive and finite-linear pieces. This branch is not promoted.

## PC-C: generic Artin–Schreier closed chains

Parameters: any prime `p` and transcendental `c`, over the algebraic
closure of `F_p(c)`. Object: the correspondence, or equivalently its
bi-infinite sequence space with shift. Clock: shift period `n`.
Observable: distinct ordered closed `n`-chains. This is not a rational
self-map of the line. Classical inputs: monic Gröbner bases, local
valuations, and the finite complete-intersection Jacobian criterion.

The closed-chain equations are, with cyclic subscripts,

    x_i^(p+1)-x_(i+1)^p+x_(i+1)+c=0.

Their leading monomials in a total-degree monomial order are the pairwise
coprime `x_i^(p+1)`. They form a monic Gröbner basis, giving scheme length
`(p+1)^n`. At any extension of the `c=infinity` valuation, let `M` be the
largest pole order of a chain coordinate. The equations imply first
`M=1/(p+1)` and then that every coordinate has this pole order: a larger
maximum would leave its degree-`p+1` term uncancelled, and at a smaller
coordinate the parameter's pole could not cancel.

The cyclic Jacobian determinant, using the opposite signs for the
equations if desired, is

    (-1)^n (product_i x_i)^p - 1.

Its two terms have different valuations, so it is nonzero at every
chain. The scheme is reduced and the count is exactly `(p+1)^n` for all
`n`; the source shift zeta is `1/(1-(p+1)T)`.

This closes the stated generic-parameter problem but supplies only a
short degree/transversality result. It says nothing uniform about
finite-field parameter specializations where the Jacobian can vanish.
The general correspondence/recursive-tower framework is classical.
It is therefore recorded as a failed paper-selection candidate, not
promoted to a formal no-go theorem about all correspondences.

## PC-D: mixed Kummer/Artin–Schreier wild inverse tower

Initial larger family: `X^p+aX^2`, odd `p`, generic target `t`. Its finite
critical point is fixed at zero and infinity is wildly ramified. The
first-level group is symmetric, but the repeated critical value forces
sign relations. A naive full-wreath induction already fails at level
two. No claim for `p>3` is carried forward.

Selected complete scope: `p=3`, every field `k` of that characteristic,
every `a!=0`, and all generic inverse-image heights. The identity
`f_a(a(z^2-1))=a^3(z^3-z)^2` exposes an exact mixed quadratic/AS structure.
The independent increment sought is a wild realization of the classical
`E_n`, all-level kernel ranks, geometric ramification, and genus—not
rediscovery of `E_n` as an abstract group.

The complete proof and its induction-dependency audit are in
`WILD_CUBIC_PROOF.md`. The minimal failure tests are: a hidden extra
square-class relation, a vanishing AS character class, a mistaken
rescaling of the infinity valuation, or a circular use of the next
group's bottom permutations. These are isolated explicitly there.

No new manuscript or evaluation record should be generated before
non-author review of those points and the classical-owner difference.

## PC-E: equal-characteristic compact quadratic dynamics

Parameters: every odd prime `p`. Domain: `t F_p[[t]]`, with its native
`t`-adic metric, and its finite quotients modulo `t^r`, `r>=1`.
Object: the actual nonlinear polynomial `g(X)=X+X^2`; clock: ordinary
integer iteration. The initially sought increment was a complete metric
and finite-cycle classification distinct from the characteristic-zero
interpolation contract C394.

The cheap decisive test was source ownership, not a larger census.
Lindahl--Rivera-Letelier explicitly identify this polynomial as minimally
ramified. In their convention, for every `e>=0`,

    i_e = ord_X(g^(p^e)(X)-X)-1 = (p^(e+1)-1)/(p-1).

For `x!=0`, `s=v_t(x)>=1`, substitution of its leading term therefore
gives the exact elementary consequence

    v_t(g^m(x)-x) = s*(i_(v_p(m))+1),    m>=1.

Here replacing a `p`-power iterate by its `p`-prime multiple multiplies
the first nonzero coefficient by a nonzero element of `F_p`, so does not
change its order. Thus `0` is the only periodic point in the complete
domain. In the finite quotient, all points of valuation `s<r` have the
same period

    p^e,    e=min{j>=0 : s*(i_j+1)>=r}.

The number of cycles on that annulus is consequently
`(p-1)*p^(r-s-1-e)`. There is also the fixed zero residue. The orbit
closure of a nonzero point is `Z_p` with distance between clocks `u,v`
equal to `p^(-s*(i_(v_p(u-v))+1))`; its ordinary Hausdorff dimension is
zero. These formulas are deductions from the cited classical theorem,
not a newly established ramification theorem.

There is a second direct ownership check: evaluation of a Nottingham
series at `t` identifies the procyclic subgroup closure with this orbit
closure up to a constant metric scaling. Ershov's author paper,
Section 3, states that every abelian (indeed every nilpotent) Nottingham
subgroup has upper box dimension zero. Evaluation at a point of
valuation `s` only raises distances to the power `s`, preserving zero
dimension. Hence the geometric headline was already a classical
consequence independently of C394's nearby orbit-classification owner.

This is a completely quantified short corollary package. It is rejected
as an independent substantial contract, not left pending on a numerical
test, and no frozen local-dynamics experiment was rerun.

## Subsequently authorized rational-map follow-up

The rational map `X^p+1/X` was checked as a possible different source.
Its generic first fiber is `X^(p+1)-tX+1`, whose projective-special-linear
group is the classical Serre/Abhyankar example. The complete original
Serre appendix has now been read; the exact first-level owner is recorded
in `PSL_FIRST_LEVEL_SOURCE_AUDIT.md` and fully deducted from the increment.
The initial screen stopped at the missing all-height independence lemma.
The coordinator subsequently authorized a targeted attempt to close it.

That attempt produced `WILD_PSL_RATIONAL_PROOF.md`: for every prime
`p>=5`, every characteristic-`p` field, and all generic inverse heights,
the actual group is the full iterated natural wreath product of
`PSL_2(F_p)`. A leaf-stabilizer/simple-quotient lemma, separated pole
supports, and Goursat independence close the global composita. Exact
local AS stability closes the local degree induction. The same proof
determines the different, complete lower inertia filtration, regularity
over the constant field, and genus at every height.

The fixed small-prime diagnostics passed; see `PSL_EXACT_CHECK_REPORT.md`.
The independent local review found no mathematical gap, and the
coordinator's independent global review likewise reported no gap. The
source audit additionally identified general composition machinery in
König--Neftin--Rosenberg, Corollary 4.6/4.6.B. Its standing characteristic-
zero convention is retained accurately: the finite-group/Galois argument
adapts directly to this separable characteristic-`p` setting; the published
statement is not quoted as literally characteristic-free.

After that deduction, the author and independent source reviewer both
recommended **REJECT_SUBSTANCE** for a separate paper, and the coordinator
accepted that recommendation. The residual is a short AS stability
estimate and local induction; the different, filtration and genera are
then forced consequences. This repeats the local compositum-collapse
pattern already present in the cubic contract, without its independent
mixed global rank theorem. The result is retained as a fully quantified
companion note. This is not a claim of an exact literature owner for
every formula and not a retraction of the valid all-height theorem.

The characteristic-three first-cover genus-one observation from the
initial screen remains only a diagnostic, not a proved elliptic
conjugacy. It is outside the selected prime range and was not elevated
to a separate candidate or theorem.
