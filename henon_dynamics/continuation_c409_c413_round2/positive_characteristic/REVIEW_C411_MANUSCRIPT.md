# Independent full-manuscript review: C411

Date: 2026-09-06. Reviewer: current-team non-author agent responsible for the
positive-characteristic branch. This is a review of the actual complete
manuscript, distinct from the previous bounded Hartogs-lemma review. It is
not a formal Route-A evaluation or an external/human peer-review certificate.

## Disposition

**PASS: no required mathematical, scope, or source-locator revision found.**
Theorem 2.1 retains the exact two-clock quantifiers and distinguishes the
initial convergence domain, the meromorphic domain and its joint boundary.
The polar components and their noncancellation are proved, and the joint-cap
argument is used only where its holomorphy hypothesis is available. I found
no counterexample or unresolved gap in the actual full manuscript.

The retained contribution is the unified all-base two-variable analytic
classification. The two arithmetic branches are not separate contributions;
the gcd bound, common-return objects, prior rectangular zeta functions,
diagonal conclusions and classical complex-analytic tools remain deducted.
The result is not a worldwide priority certification. Final deterministic
builds, all-page visual QA and formal evaluation remain the coordinator's
separate release work.

## What was actually read

I read the actual `main.tex`, all seven section sources, `references.bib`,
`PAPER_PLAN.md`, `CITATION_METADATA.md` and `BUILD_REPORT.md` under
`../papers/C411_two_clock/`. I read all 11 pages of the existing PDF text,
extracted in two bounded groups without truncation. The PDF contains the
complete theorem, Lemma 4.1, Proposition 5.1, Lemma 6.1, their proofs and
the seven-entry bibliography.

I also read the complete frozen `RECTANGULAR_RETURN_PROOF.md`,
`RECTANGULAR_SOURCE_AUDIT.md`, `RECTANGULAR_EXACT_CHECK_REPORT.md`,
`REVIEW_RECTANGULAR_ROOT.md` and
`positive_characteristic/REVIEW_HARTOGS_PROPAGATION.md` under
`research_c409_c413/`. The current full-draft review does not merely infer
correctness from those receipts. In particular, the regularized-tail proof
and the dependent-parameter split were checked in the actual new TeX and PDF.

No author file was changed by this review. No old 784-kernel,
24,624-coefficient or four-pole test was rerun. No experiment, numerical
pole plot, fresh paper build, registry update, formal evaluation or Git
operation was performed. Reading PDF text is not claimed as an all-page
visual inspection.

## Exact arithmetic input and convergence domains

The common circle kernel has the claimed gcd cardinality by Bézout's
identity. The optional localized realization does not lose finite common
kernel points, because the gcd is coprime to both bases. Neither statement
requires the two bases themselves to be coprime.

For dependent bases, the prime-valuation argument gives the unique integer
$c\geq2$ and coprime positive exponents $r,s$. Requiring $c$ to be
power-free would be wrong and is explicitly not imposed. The same-base gcd
identity follows by the exponent Euclidean algorithm.

The independent branch uses the correct two-exponent arithmetic theorem.
I directly read Corollary 1, inequality (1.3), the introductory integer
formulation and the corollary proof in
[Corvaja–Zannier arXiv:math/0311030v2](https://arxiv.org/pdf/math/0311030v2).
The finite-exception quantifier ranges over multiplicatively independent
pairs in the fixed finitely generated group, not just one diagonal
sequence. Applying it to $(a^n,b^m)$ is valid for every positive $n,m$;
finite exceptions can be absorbed in one $K_\epsilon$. The subsequent
product-geometric majorant proves normal convergence on every compact
sub-bidisc. No unexamined translated-subtorus exception or effective
threshold is silently discarded.

For dependent bases, the exponent-slack inequality in Section 3.3 has the
correct direction because $0<u,v<1$. It gives absolute convergence on
$\Omega_{r,s,c}$ and uniform convergence on slightly larger closed
polydiscs still satisfying the strict inequality. Axis points inside
$\Omega$ are handled by taking a small positive radius for their zero
coordinate, not merely by observing that individual terms vanish there.

The ray $(n,m)=(sk,rk)$ proves divergence at equality as well as beyond
the curved condition: its terms fail to tend to zero. Fixed rows or
columns prove divergence when a nonzero coordinate has modulus at least
one. The pointwise-zero outer axes have no open convergence neighborhood.
Thus the claimed *open* absolute-convergence domains, including all axis
conventions, are exact. This does not prove that every curved convergence
boundary point is singular, and the manuscript does not claim that.

## The actual dependent polar divisor

The primitive-ray resummation is justified first on the original absolute
domain. The valuation identity
$h_{i,j}=\gcd(r,j)\gcd(s,i)\mid rs$ is proved with both coprimality
conditions used. This bound makes the large-ray tail normally convergent
on compact sub-bidiscs; only finitely many local terms can have a pole.
It therefore constructs an actual meromorphic function throughout $\D^2$,
not merely a formal list of denominators.

For each primitive positive vector, the monomial coordinate change makes
its nonzero level smooth and irreducible in the algebraic torus. The added
annular parameterization also checks that the portion inside the bidisc is
connected. The displayed positive point proves nonemptiness. Distinct
primitive vectors give distinct hypersurfaces, so local finiteness and
discrete intersections supply generic points with a genuine simple pole.
Pole order one here is the divisor order on each component, not a claim
that a two-variable crossing has only one branch.

The slice residue calculation is especially useful: every coincident
summand contributes $-x_0/i$, and only finitely many contribute locally.
Thus the total is $-x_0\sum 1/i\ne0$ for arbitrary complex nonzero
$x_0,y_0$, not only for positive real parameters. The positive objects
are the weights $1/i$ after the common factor $-x_0$ is removed; the
complex residues themselves need not be positive real. The manuscript
states the signed formula correctly. It prevents cancellation at all
component intersections used later.

## Positive slices and their genuine dense singularities

For real $0<t<1/b$, the coefficient bound by $b^m-1$ makes the slice
coefficients uniformly bounded. The totient/order formula includes exactly
the divisors common to the two return integers, with the $d=1$ convention
stated. The measure in (11) is positive and has finite mass.

Choose a prime $\ell\nmid ab$. Every power $\ell^j$ occurs at a suitable
second-clock time, while the orders of $a$ modulo these powers are
unbounded: a bounded-order counterexample would force the nonzero integer
$a^N-1$ to be divisible by arbitrarily high powers of $\ell$. Consequently
the support contains complete root grids of unbounded orders. Positivity
ensures that these are actual nonzero atoms despite any repeated frequencies.

The radial kernel bound permits dominated convergence against this finite
measure and extracts each atom exactly. Dense nonzero inverse atom points
exclude holomorphic continuation, and a meromorphic cap would require a
dense set of poles in its open domain. This proves Proposition 5.1 without
a Diophantine bound and without extending its positivity claim to complex
parameters.

## The Hartogs step in the actual manuscript

Lemma 6.1 assumes joint holomorphy on $\D\times V$ with $V$ connected
and one distinguished interior parameter with a full-circle slice boundary.
Those assumptions are sufficient; no nonpolar set of distinguished
parameters is needed. The draft supplies a complete proof rather than
quoting an unspecified multivariable extension principle.

The Taylor center $z_c=(1-\delta)x_0$ has distance exactly $\delta$
from the unit circle. Cauchy estimates on compact parameter neighborhoods
give local uniform upper bounds for
$u_n=n^{-1}\log|a_n|$. The proof uses

$$
V_N=\left(\sup_{n\geq N}u_n\right)^*,\qquad
V_\infty=\lim_N V_N,
$$

not an unsupported subharmonicity assertion about the raw pointwise
limsup. Upper-envelope regularization and the decreasing-limit theorem
apply; the improved and unimproved Cauchy bounds survive regularization
because they were taken on compact neighborhoods first. These are the
classical inputs in [Korevaar–Wiegerinck, Section 4.8 and Properties 8.4.3](https://staff.science.uva.nl/j.j.o.o.wiegerinck/edu/scv/scvboek.pdf),
which I checked in the existing primary text after a fresh browser fetch
failed.

Cauchy–Hadamard at the distinguished slice gives radius exactly
$\delta$, forcing $V_\infty(t)=-\log\delta$. The connected-domain
maximum principle then gives that value everywhere. The hypothetical cap
contains the closed disc of radius $2\delta$ about $z_c$, producing the
strictly smaller envelope bound on an open parameter disc and the required
contradiction. The proof does not assert equality of raw and regularized
limits at every exceptional slice.

For a meromorphic cap $A/B$, the denominator cannot vanish on an entire
unit-circle arc times an open parameter disc: the one-variable identity
theorem in $x$ would force it to vanish identically. A nearby point with
$B\ne0$ therefore supplies the already excluded holomorphic cap. The
example $(y-y_0)h(x)$ correctly explains why the lemma is a joint claim
despite its entire zero slice.

## Dependent strip, pole range, thresholds and zero axes

The independent branch is jointly holomorphic on all $\D^2$, so Lemma 6.1
applies with $V=\D$. The dependent branch has interior poles and does not
satisfy that hypothesis there. The manuscript explicitly applies the lemma
only on $\D\times\D_{1/b}$, where the elementary count bound gives
normal convergence and hence joint holomorphy. This includes $y=0$ and
therefore excludes joint caps on the zero-axis boundary even though the
individual zero slice is entire.

For $1/b<|y|<1$, primitive vectors $(sk,r)$ with $\gcd(k,r)=1$ have
$h=rs$. Their actual slice poles form full root grids with radii
$(c^{rs}|y|^r)^{-1/(sk)}<1$ tending to one. The residue result proves that
none is removed by a collision. Distinct growing $k$ yield infinitely
many distinct poles tending to every point of the first unit-circle face.

Crucially, the cap-denominator contradiction is made for **each** parameter
in an open disc lying in this range. It does not rely on one exceptional
slice on which the cap denominator might itself vanish identically.
One-variable identity forces $B(\cdot,y)=0$ for every such $y$, hence
$B=0$ on the product, a contradiction. Threshold points $|y|=1/b$ and
corner points are excluded by restricting a hypothetical neighborhood cap
to nearby face points already ruled out. Symmetry handles the other face.
All of $\partial(\D^2)$, with its axes, thresholds and corners, is covered.

The concluding point $(\mathrm i/\sqrt2,\mathrm i/\sqrt2)$ for $a=b=2$
is a correct exact illustration: it lies on the curved convergence boundary
but on none of the locally finite polar components, so the continuation
is holomorphic near it. This reinforces the domain distinction without
adding an experiment or a separate theorem.

## Nearest-owner and version checks

The cited comparisons match their stated source objects. I checked the
actual rectangular-period definition and Example 3.1 in the
[Ward 1992 institutional manuscript](https://ueaeprints.uea.ac.uk/18593/1/pp2.pdf),
and the relevant definition on printed page 59 of the existing downloaded
[Ward 1989 thesis](https://wrap.warwick.ac.uk/id/eprint/73322/1/WRAP_THESIS_Boulton_1989.pdf).
The source already uses native rectangular times and volume-weighted
one-variable zeta objects; the draft gives that credit.

The [Miles 2015 accepted manuscript](https://shura.shu.ac.uk/17220/1/Miles-NaturalBoundaryForTheDynamicalZetaFunction%28AM%29.pdf)
defines the full finite-index-subgroup zeta and includes rectangular
subgroups as a special family. The
[Miles 2013 author-uploaded manuscript text](https://www.researchgate.net/publication/260059770_Synchronization_points_and_associated_dynamical_invariants)
defines weak/strong synchronization and ordinary generating functions with
one common time; I checked those actual definitions, not just repository
metadata. The current draft does not relabel either invariant as new.

Theorem 1.1 of [Nguyen-Dang v2](https://arxiv.org/pdf/2606.07959v2), directly
checked, gives the stated diagonal recurrence classification including
eventual recurrence. The manuscript does not count the diagonal
natural-boundary or inherited non-D-finiteness deductions as extra results.
It also keeps that source a preprint. Missing final typeset versions of
other works are not certified identical to the original/accepted texts.

These are bounded locator/scope checks supplementing the fully read frozen
audit, not a new exhaustive literature search or a claim to have reread
every page of every cited source. No unavailable final publication was
silently substituted for an inspected version.

## Build observations and reviewed snapshot

Read-only searches of `main.log` and `main.blg` found no Warning,
undefined-reference/citation, multiply-defined-label, overfull or underfull
match. `pdfinfo` reports 11 pages, 318522 bytes, letter size and blank Author
metadata. These agree with the author first-build receipt. I did not perform
the coordinator's pending independent two-directory build or final visual QA.

```text
c8da445d09c3b9cae43650b7668c7a00f984b9f269fa030249b3638b5f751b8c  main.tex
296c459bb6e3ef2029fe3128617fd81674f4ead1d1e998fb144bae4e1a31f8d8  main.pdf
2d00c9175cf75d7d9c3344cfd6520b5dddf39408c2e0c3f6c0b695c2cd31b8d3  references.bib
4fe5392e499feb5d31755882f4b63fb0e9d1998a6c1c1508d0363af1bd12326e  sections/01_introduction.tex
4af790ec234c7c3ec5883fb3d86e6808e105b31e8d6e7a491130203ac136e31a  sections/02_statement.tex
269d1ad52fd7b33b91eb9582a6a6f618dc5a2a52f83608818f92a3dec1aa0bb2  sections/03_convergence.tex
1cf96252a54906be243ef0ba7e48c44b7b628b16b424069a325163ae168ab019  sections/04_poles.tex
eab9ab41d434fb1b5246e99685ad0adccb616540f0649c3170d1f727c84a0c39  sections/05_slices.tex
ee6206f0ed52291d8f1ca3f5f3412671fd2d5e656be6cf60271d57b847c0b5f5  sections/06_joint_boundary.tex
9769db2b7fb6f8dd7ce73d36c0c5224efb5af53f475c0c6480abee63b53ddceb  sections/07_scope.tex
```

Final internal disposition: the full current manuscript can proceed to
the coordinator's release gates without a reviewer-requested source edit.
It establishes native common-return analytic geometry, not a target Euler
factor, prime-labelled orbit system, root number, zero/divisor comparison
or Hilbert–Polya construction.
