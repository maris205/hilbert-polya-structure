# Nonlinear geometry: exact second-round deductions and limits

2026-09-08 UTC. Coordinator-authored work on the two
[frozen questions](FROZEN_QUESTIONS.md). No mathematical program was run.
These deductions are not admissions or a full periodic atlas.

## 1. NG2-V: the actual all-dimensional difference equation

Let `(x_i)` be a bi-infinite periodic scalar word for the retained map:

`x_(i+n)+x_i = a + product_(j=1)^(n-1) x_(i+j)`.

Put `u_i=x_(i+1)-x_i` and
`p_i=product_(j=2)^(n-1) x_(i+j)`. Subtract the recurrence at `i`
from the recurrence at `i+1`. The two products have the common factor
`p_i`, so this gives, without dividing by any coordinate,

`u_(i+n)+u_i = p_i*(x_(i+n)-x_(i+1))`

`                 = p_i*sum_(j=1)^(n-1) u_(i+j)`.                 (V1)

This identity is valid for every sign, every zero coordinate, every
parameter and every period. It genuinely eliminates `a`. At
`U=max_i |u_i|`, however, it only gives

`|p_i * sum_(j=1)^(n-1) u_(i+j)| <= 2U`.                       (V2)

This bounds a product times a possibly cancelling sum. It does not
bound each coordinate, nor does it force one of the individual
differences to vanish merely because a coordinate is large.

To locate the special three-variable argument precisely, put
`d_i=x_(i+n-1)-x_i`. Subtraction at `i` and `i-1` instead gives

`d_(i+1)+(x_(i+1)-x_(i-1))`

`    = (1+product_(j=1)^(n-2) x_(i+j))*d_i`.                   (V3)

For `n=3`, the second term on the left equals `d_(i-1)`, and the
coefficient is `x_(i+1)+1`. This is exactly C421's homogeneous
tridiagonal identity. For general `n`, neither replacement is valid.
Thus applying C421's extremal-center case split verbatim would be an
algebraic error, not an incomplete exposition of the same proof.

The already established two-zero locus at `a=0` must still be retained.
For example, when `n=4`, the periodic word

`(0,t,0,s,0,-t,0,-s)`

has arbitrarily large coordinates. In (V1), every `p_i` is zero, so
the equation reduces to `u_(i+4)=-u_i`. This illustrates why the new
identity does not itself exhaust exceptional supports. This family is
an inherited control, not a new result of the present round.

**Exact remaining gap.** No uniform classification of the cancelling
sums, small-product supports and their propagation in (V1)–(V3) has
been proved. In particular there is no all-dimensional exhaustive list
of unbounded periodic channels and no proved residual finite core.
The full NG2-V question remains `UNCLOSED`; no program or paper is
justified by this route alone. This is not a theorem that no different
exhaustion argument can work.

## 2. NG2-F: clock, elementary structure and a strict group distinction

Each of the three factors interchanges the two roots of the invariant
quadratic in its changed coordinate. Hence it is an involution of
`Z^3` preserving `K`, including all singular points. The inverse of the
native map is `s_x after s_y after s_z`; no chart or resolution is
substituted for these ordinary affine maps.

Writing `x_0,x_1,x_2` for a state, the successive scalar updates obey

`x_(i+3)+x_i = x_(i+1)*x_(i+2)+a_i`,

where `a_(3j)=A`, `a_(3j+1)=B`, `a_(3j+2)=C`.
Three updates form one tick of `T`. In the equal-forcing slice this is
`T=F_(3,a)^3`, and an `F`-cycle of least period `r` splits into
`gcd(r,3)` native `T`-cycles of least period `r/gcd(r,3)`.

The same adjacent subtraction, now with `d_i=x_(i+2)-x_i`, yields

`d_(i+1)+d_(i-1)=(x_(i+1)+1)*d_i+(a_i-a_(i-1))`.             (F1)

Consequently a C421 homogeneous estimate has an additional forcing
term bounded by `max(|A-B|,|B-C|,|C-A|)`. Its old parameter-free
extremal classification is not an established result for this system.
Equation (F1) is a possible additional reduction, not a completed
classification.

A fixed point of `T` is fixed by all three factors: the final value
of its first coordinate is the value immediately after `s_x`, and
no subsequent factor changes it; then the same reasoning applies to
the second and third coordinates. Thus the fixed-point equations are

`2x=A+yz`, `2y=B+xz`, `2z=C+xy`.

Conversely these equations plainly suffice. This is only the period-one
stratum. For another elementary boundary, when `A=B=0`, every point
`(0,0,t)` is sent to `(0,0,C-t)`. Its native least period is one when
`2t=C`, otherwise two. At fixed `C` the global heights are unbounded;
on a fixed invariant level they satisfy `t²-Ct=D` and are finite.

### A periodic native point with an infinite full Vieta orbit

The distinction from a finite group orbit can be demonstrated within
this same family, not only by an abstract group-action analogy.
Set `A=B=C=0` and `P=(-1,3,-1)`. The scalar cyclic map has the word
`(-1,3,-1,-2)` of least period four. Since `T=F^3`, `P` has native
`T`-period four as well, on `K=8`.

But applying `s_x` and then `s_z` to `P` gives `(-2,3,-5)`.
Keep `z=-5` and repeatedly apply `s_x` and then `s_y`. If the current
first two coordinates are `(-u,v)` with `0<u<v`, they become

`(-u',v')`, where `u'=5v-u` and `v'=5u'-v`.

Then `u'>4v` and `v'>4u'>16v`, so `0<u'<v'` and the heights grow
without bound. Starting from `(u,v)=(2,3)` produces infinitely many
distinct points. The full Vieta-group orbit of `P` is therefore infinite.
Replacing fixed-word periodicity by finiteness of the group orbit would
reject this actual periodic point. Group-orbit equivalence is itself a
different predicate and has not supplied the missing return criterion.

## 3. A source-owned finiteness consequence, not an effective atlas

Under `z -> -z`, our family becomes the plus-`xyz` family with
coefficients `(A,B,-C,D)`. Cantat's Section 2.3 represents the three
involutions by matrices

`r_x=[[-1,-2],[0,1]]`, `r_y=[[-1,0],[0,1]]`,
`r_z=[[1,0],[-2,-1]]`.

Their product for our word is

`r_z r_y r_x = [[1,2],[-2,-5]]`,

with determinant `-1`, trace `-4` and spectral radius `2+sqrt(5)>1`.
The word is cyclically reduced and uses all three factors. The checked
Proposition 2.2 therefore applies on every complex parameter fibre.

Cantat's Theorem 3.1 and the proof of Corollary 3.3 provide forward
and inverse attracting neighborhoods covering the triangle at infinity.
Their complement on the projective cubic is compact and affine; a
two-sided bounded orbit cannot enter those neighborhoods. Thus all
periodic points on any one fixed fibre lie in a compact affine set.
Its intersection with `Z^3` is finite. These source mechanisms also
apply to singular affine fibres, since their boundary is smooth.
[Checked primary version](https://arxiv.org/pdf/0711.1727v2).

The matrix substitution and the compact-set/lattice deduction are
coordinator inferences from the cited statements, not a new finiteness
theorem attributed to this batch. No explicit effective radius, uniform
least-period bound, or finite residual graph for the full coefficient
class has been extracted here. Existence of a compact set does not by
itself supply a terminating enumeration algorithm with a known cutoff.
Even an effective specialization of this familiar escape argument must
pass a separate substantive-increment gate before it can be a paper.

## 4. Second-round disposition

| Question | Mathematical result of this attempt | Paper disposition |
| --- | --- | --- |
| NG2-V, original continuation | Exact higher-order identities; the full exceptional-support and finite-core exhaustion remains unproved. | `UNCLOSED / NOT_ADMITTED`. |
| NG2-F | Native clock and elementary strata checked; explicit separation from finite group orbits; fibrewise finiteness follows from a classical source. The all-parameter effective atlas remains unproved. | `UNCLOSED_ATLAS / SOURCE_OWNED_HELPERS_ONLY / NOT_ADMITTED`. |

Neither question is a new independent theorem package. The Fricke
question is not labelled an exact source-owned full atlas: only the
specified helper is source-owned. No manuscript is produced, no C
number is assigned, and neither question increases the batch's admitted
count. Source search is bounded and does not establish worldwide novelty.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
