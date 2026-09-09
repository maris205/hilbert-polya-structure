# Nonlinear geometry: three first-pass questions

2026-09-08 UTC. Research questions generated for bounded feasibility screening,
not admitted contracts, manuscript numbers, or worldwide novelty claims.
The definitions below are frozen before any new mathematical program. No
program, parameter census, or old mathematical rerun has been executed here.

## NL424-1 — integer two-slope plane return atlas

For every `(a,b) in Z²`, use

`T_(a,b)(x,y)=(f_(a,b)(x)-y,x)`,
`f_(a,b)(x)=a*x` for `x>=0`, and `b*x` for `x<0`.

The complete domain is `Z²`, including axes and the origin. The native clock
is one application of `T`, not the induced ray map. Classify every ordinary
periodic point, its least period and its integer parametrization for all
parameters. Positive rescaling and reversal are not quotient identifications.
Do not replace this by the smaller question of globally finite-order maps.
The arithmetic carrier is the integral unimodular branch action.

Closest sources: Beardon–Bullett–Rippon (1995), Lagarias–Rains Part I
(arXiv math/0301294v4), and Cairns–Nikolayevsky–Rossiter (1407.3364v1).
These already own the ray/global-periodicity theory and integer two-piece
finite-order restriction. The residual, if substantial, would be an explicit
all-integer atlas including the nonglobal neutral-ray cases, not a new proof
of their theorems. Cheap test: subtract those classifications and check
whether anything beyond their specialized linear algebra remains. Replace
the subtype if only a short source consequence survives.

## NL424-2 — all-dimensional forced Vieta cyclic dynamics

For every `n>=3` and `a in Z`, use the polynomial automorphism

`F_(n,a)(x_1,...,x_n)=(x_2,...,x_n,product_(j=2)^n x_j+a-x_1)`

on the full ordinary lattice `Z^n`, at one native application per time step.
Classify all periodic points and least periods, uniformly in `n,a`, including
zero coordinates, units, sign patterns and every singular invariant level.
The invariant is

`K_(n,a)=sum_j x_j²-product_j x_j-a*sum_j x_j`.

The carrier is integral dynamics on this invariant affine variety. No quotient
by the full Vieta group, positive chamber, smooth compactification or
fixed-period search is a substitute for the specified cyclic map.

C421 already closes the entire `n=3` problem. Hu–Tan–Zhang cover the
unforced Markoff–Hurwitz automorphism structure and dihedral locus;
Gamburd–Magee–Ronan count a different integer-point/group-orbit problem.
The prospective increment is a uniform all-dimensional exhaustion theorem,
not `n=4` examples or the old three-variable argument with a changed label.
Cheap test: try to isolate every unbounded periodic channel before claiming
a finite core. The explicit two-zero channel below is mandatory. Without a
proved exhaustion, no larger scan or manuscript is justified.

## NL424-3 — rational three-site Adler transfer classification

For every ordered parameter triple `beta in Q³`, define the two-site map

`R_(b,c)(u,v)=(v-(b-c)/(u+v),u+(b-c)/(u+v))`

and the three-site transfer `T_beta=R_(beta_1,beta_3)^{13}
after R_(beta_1,beta_2)^{12}`. Superscripts specify the coordinate sites;
the first transformation is on sites 1 and 2. Parameters remain attached to
their sites and are not permuted by a transfer iterate. Use the maximal
regular map: when `b=c`, `R` is the everywhere-defined swap, including
`u+v=0`; when `b!=c`, require `u+v!=0`.

The complete native two-sided domain is the set of points in `Q³` whose
forward and inverse transfer iterations, including each intermediate
two-site operation, remain regular. Freeze the polynomial invariant map
`I_beta=(S,H_beta)`, where `S=x_1+x_2+x_3` and

`H_beta=(x_1+x_2)(x_2+x_3)(x_3+x_1)
        +beta_1(x_2+x_3)+beta_2(x_1+x_3)+beta_3(x_1+x_2)`.

Classify every ordinary rational periodic point and least period, on every
full affine level `I_beta=(s,h)` with `(s,h) in Q²`, including singular
levels and their ordinary points that meet the native domain. These levels
are neither normalized nor asserted all to be elliptic. The formulas apply
unchanged for coincident parameters. One whole `R13 R12` transfer is one tick. An extended
transfer/root, a generic Jacobian translation or a resolved surface is not
silently substituted for it. The second invariant was made explicit during
nonauthor screening review; only mentioning `S` would not specify an elliptic
pencil, since its own fibres are affine planes. No mathematical program was
run before or after this clarification.

Veselov (math/0205335v2) owns the Yang–Baxter transfer construction and
factorization/isospectral mechanism; Kassotakis (SIGMA 2019/048) owns relevant
invariants, extended transfers and Painlevé reductions. C422 is a different
`H_III^B` transfer, not automatically an answer for this `H_V`/Adler map.
The residual would be a complete rational native-domain atlas. Cheap test:
deduct the source reductions and distinguish rational torsion restrictions
on smooth fibres from a sufficient all-fibre classification. If the latter
is missing, preserve the gap instead of counting a generic integrability
argument as a completed question.

## Shared limits

The earlier Somos-4, Hirota–Kimura Euler-top and pentagram envelopes were
discarded in a local-collision prescreen, before these three questions;
they are not three additional candidates or new experiments. Initial
source searches do not establish worldwide priority. No formal Route-A
evaluation, target Euler factor, root number, automorphy or Hilbert–Pólya
claim is made. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
