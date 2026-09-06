# Positive-characteristic continuation: stopped candidate screen

2026-09-06. This is a research screen, not a theorem admission or paper.
Four previously frozen research-ready contracts are unchanged. No old
script, frozen proof, manuscript, registry, or Git object was edited here.

## Disposition

**No fifth contract from this line.** Four concrete objects were screened.
Only the nonlinear additive cocycle survived the elementary reduction
tests, and its substantive all-forcing lemma remains unproved. At the
coordinator's instruction this line stops here, without further searches,
parameter tests, or promotion of the single-forcing conjecture. The author
now undertakes the independent finite-lattice-census review.

## The four objects

### PC2-A. Nonlinear formal-disc cocycles

For an odd prime p, put g(x)=x+x² and
F_P(x,y)=(g(x),y+P(x)), with x in t F_p[[t]], y in F_p[[t]],
and P in F_p[[x]] (or a polynomial). The intended clock is ordinary
integer iteration on every quotient modulo t^r, not merely prime-to-p
iteration. The observable is S_n(P)=sum_{j=0}^{n-1} P(g^j(x)).
On a base cycle of length p^e the additive fibre either keeps that length
or multiplies it by p, according as S_{p^e}(P) vanishes modulo t^r.

The genuine target would be a full forcing/cohomology or trace-filtration
classification, sufficient to determine these lift decisions for every
P,r,e. Merely restating the already classical ramification orders of g,
or proving one trace order for P=x, would not meet the independent-paper
threshold. On the completed disc itself, g has no nonzero finite-period
point; consequently this is a finite-quotient tower question, not a claim
of a rich geometric periodic-point count over an algebraic closure.

Nearest primary ownership: Lindahl–Rivera-Letelier,
[*Generic parabolic points are isolated in positive characteristic*](https://arxiv.org/abs/1501.03965),
and their
[*Optimal cycles in ultrametric dynamics and minimally ramified power series*](https://arxiv.org/abs/1311.4478).
The abstract/metadata were checked in this continuation; they explicitly
own the minimally ramified base and its first significant iterate terms.
This report does not claim a fresh full-text review of these papers or
priority for the cocycle. Targeted cocycle/Nottingham/cohomology searches
did not identify an exact owner, which is not a novelty certificate.

The exact diagnostics and their strict finite limits are recorded below.
**Missing lemma:** describe the image/cokernel of g*−1 on F_p[[x]], or an
equivalent complete trace filtration, with uniform all-height control.
No such lemma has been proved. Higher-pole Laurent changes and more
general conjugacies have not been excluded.

### PC2-B. Frobenius–multiplicative skew products

For nonzero P in F_p[x] and d≥2 with p not dividing d, consider
F(x,y)=(x^p,P(x)y^d) on A² over an algebraic closure of F_p.
For every n≥1, put R_n=# {a in F_{p^n}:P(a)=0} and
M_n=(d^n−1)/p^{v_p(d^n−1)}. Directly from the fibre equation,

    #Fix(F^n)=p^n+(p^n−R_n) M_n.

Indeed x must lie in F_{p^n}; a zero of P gives only y=0, while
each nonzero fibre has y=0 plus M_n distinct nonzero solutions.
This is a complete elementary calculation, not numerical evidence.
Away from P=0, adjoining u with u^{p−d}=P(x), interpreting a negative
exponent in the function field if necessary, and putting y=uz gives
the product lift (x,u,z)↦(x^p,u^p,z^d). The coupling is therefore a
finite-cover product construction, not an independently new mechanism.

Nearest general primary context is Bridy's
[*The Artin–Mazur Zeta Function of a Dynamically Affine Rational Map in Positive Characteristic*](https://www.numdam.org/article/JTNB_2016__28_2_301_0.pdf)
(the source discusses dynamically affine examples), together with the
already excluded FAD direction. This is context, not a claim that Bridy
states this exact A² formula. **Rejected:** elementary cover/product
reduction and insufficient increment; no all-extension-field character
sum theorem was proposed or proved.

### PC2-C. Matrix-power dynamics

For q a prime power and a≥2, consider A↦A^a on SL₂(F_q), asking for
ordinary cycles for all n and q. Its fixed set is exactly
{A:A^{a^n−1}=I}; the standard conjugacy classes reduce counting to split
and nonsplit tori and the unipotent classes. Over an algebraic closure,
these sets generally have positive-dimensional conjugacy families, so
they are not finite geometric fixed-point counts.

An exact-topic primary owner was found: Matt Larson,
[*Power maps in finite groups*](https://mattlarson2399.github.io/Papers/Powermaps2019.pdf),
Integers 19 (2019), A58, published 4 November 2019. The primary title page
and abstract explicitly list SL₂(F_q); no complete paper reading is
claimed here. **Rejected:** already studied power-map mechanism and
elementary conjugacy-class counting, with no new theorem isolated.

### PC2-D. Generic nonconstant polynomial parameters

Let c be transcendental over F_p, let d≥2 with p not dividing d, and
f_c=x^d+c over the algebraic closure of F_p(c). Every point on a finite
cycle has pole order 1/d at c=∞: a larger pole escapes under x↦x^d+c,
and a smaller one maps to a pole of order 1, which then escapes.
Consequently the multiplier of an n-cycle has nonzero pole order
n(d−1)/d, and cannot equal 1. Hence f_c^n−x has exactly d^n distinct
roots for every n, and the affine ordinary zeta function is 1/(1−dT).

**Rejected:** elementary escape and transversality, not a substantial
new contract. No exact-owner or global-priority claim is made; no claim
is transferred to constant specializations c in an algebraic finite
field. This object received only the displayed analytic feasibility
test, not an exhaustive literature review.

## Prespecified exact diagnostic receipt for PC2-A

The local script [cocycle_probe.py](cocycle_probe.py) uses exact
F_p polynomial arithmetic and truncation, not floating point. Its first
run used precisely p=3 at precision 128, p=5 at precision 256, forcings
x^k for 1≤k≤p+2, and n=1,p,p². The x² forcing was checked at every
step against the exact telescoping identity S_n(x²)=g^n−x. All these
assertions passed. The observed trace orders at the two nontrivial
heights were:

| p | n | k=1,2,...,p+2: orders of S_n(x^k) |
|---|---|---|
| 3 | 3 | 3, 5, 9, 6, 8 |
| 3 | 9 | 12, 14, 36, 15, 17 |
| 5 | 5 | 5, 7, 8, 9, 25, 10, 12 |
| 5 | 25 | 30, 32, 33, 34, 150, 35, 37 |

For P=x, these four cases begin −x^{h_e}+x^{h_e+1}, with
h_e=p+⋯+p^e. This remains finite evidence, **not** an all-p/all-e theorem.
It also shows why the valuation of the first monomial of an arbitrary
forcing alone cannot safely replace a trace-filtration argument.

A second diagnostic, run only for its newly added function (not by
rerunning the first test), solved the truncated coefficient system

    Q(g(x))−Q(x)=x+c (mod x^64), ord_x Q≥−1.

The p=3 system was consistent, coefficient rank 61; the p=5 system was
inconsistent, coefficient rank 62. Consistency at a finite cutoff does
not prove a compatible formal solution. The p=5 obstruction can also
be verified without the script: writing Q=x^{-1}+sum_{j≥1}q_j x^j,
the x²,x³,x⁴,x⁵ equations force q₁=1,q₂=2,q₃=3,q₄=0 in F₅.
The coefficient of x⁶ is then −1+q₃+6q₄+5q₅=2, a contradiction.
The x coefficient forces the x^{-1} coefficient to be 1; the free
constant on the right absorbs its constant difference. This only rules
out this explicitly bounded-pole shear, not every conjugacy.

No further diagnostic was run after the coordinator's stop instruction.
No source claim, all-height assertion, or fifth-paper admission follows
from the finite computations in this file.
