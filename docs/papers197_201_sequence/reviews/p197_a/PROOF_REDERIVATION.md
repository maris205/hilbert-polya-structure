# P197 Review A — independent proof reconstruction

Target: pinned Round0 main.tex, not the mutable author draft. Status:
**PROVABLE AS STATED** for the scoped theorems. No additional assumptions
or weakened main conclusions are required. This is an internal mathematical
review, not a priority or external-publication determination.

## 1. Literal rule and independent representation

Let L,H be the bit sets of negative and positive letters, and let Z be their
complement inside n labelled sites. Write R for cyclic right rotation of
bits, so bit i of R(L) records old site i+1. The new negative and positive
sets are respectively

$$L'=(H\cap\overline{R(H)})\cup(Z\cap R(L)),\qquad
H'=(L\cap\overline{R(L)})\cup(Z\cap R(H)).$$

Each formula enumerates exactly the two possible old-level cases for a
strict descent or ascent. They are disjoint and give the literal synchronous
map, including n=1. This is the verifier's transition, not a call to the
author's tuple comparator. The complete finite graphs are reconstructed by
Kahn indegree peeling. Vertices not peeled are the cycles; reversing the
peel order determines every tail and inherited cycle length. This differs
from the author's per-start orbit-path algorithm.

## 2. Local certificate and all-size attraction

The first identity has 96 admissible open words. Its middle-pair orbits
under negation and reversal have representatives -0 and -+, with orbit
sizes 4 and 2; each representative has 16 admissible outer extensions.
The second has 1,344 words. Reconstructing the manuscript's eight middle-
triple orbits gives disjoint coverage of all 24 nonconstant triples and
the stated extension counts and outputs. All words are checked directly,
not by comparing the eight displayed answers alone.

For any open word, negation commutes with successive comparisons and
reversal introduces a sign at each comparison. The first two sides have
odd comparison counts 5 and 1; the second pair have even counts 6 and 2.
Thus the representative symmetries really preserve each identity.
If a cyclic word has no equal neighbors, every repeated cyclic window
meets the first local hypothesis; if it has no constant triple, every
window meets the second. Repeated sites at n<6 or n<7 do not invalidate
these implications: a repeated-window word is still among the checked
open words. Constants are treated separately.

A zero output run of length q forces q+1 equal source letters. A nonzero
output run of length q forces a strict chain of q+1 levels, hence q<=2.
A constant output can only be zero, since cyclic strict inequalities
cannot hold. Consequently a nonconstant source with maximum run R>=3
reaches maximum run at most two in at most R-2 steps, followed by two
local-certificate steps. At R=1 the first certificate gives one step;
R=2 uses the second. If a constant is reached early it is zero and already
fixed. This proves tau<=R without assuming that every intermediate word
is nonconstant.

## 3. Core and exact clock

Shift-commutation makes K={D^4=rho^2} invariant under both D and rho.
For x in K, rho^(-2)D^3 is a two-sided inverse of D and preserves K.
Thus D restricts to a permutation of finite K. Every trajectory enters K
by the preceding argument, so a periodic point outside K is impossible.
The minimum local-equality time is therefore exactly the ordinary tail.
Iterating the core equality n/gcd(n,2) times gives the stated period
divisibility. It does not imply that each divisor occurs.

## 4. Sharpness, all small boundaries, and first entry

For strict alternating blocks of length l>=2, direct inspection of the
two junctions proves

$$D(0^r\operatorname{Alt}_l(s))=0^{r-1}\operatorname{Alt}_{l+1}(s)
\quad(r>=1).$$

At even n, the final strict alternating word is sent to its negative.
At odd n, the four one-zero phases printed in the manuscript give
D^4=rho^2, including n=3. The displayed discrepancy coordinates for
r>=4, r=3, r=2 and r=1/even n are valid. They show nonmembership in K at
every earlier phase, not just arrival at a recurrent endpoint. The
reviewer independently checks 1,104 such signed junction instances with
r=1,...,24 and l=2,...,24 using bitplanes.

For n>=4, the successor of a one-exception word is outside K until the
claimed endpoint. Invariance implies the original cannot already lie
in K. At n=2,3, not every one-exception pair is sharp: the pairs with
|a-b|=2 have tail zero, while the four adjacent-level pairs have tail one.
The chosen 0^(n-1)1 is valid throughout. At n=1 a nonzero letter has tail
one and zero has tail zero. Round0 explicitly states these corrections.

Except for the one-exception form, a nonconstant word has R<=n-2.
Together with constants and the one-exception calculation, this proves
the exact global upper bound at both parities. No l=1 junction argument
is used.

## 5. General de Bruijn formulas, including repeated windows

Let an overlap graph have vertices of length k>=1 and edges given by
allowed (k+1)-letter blocks. A based closed n-walk consists of windows
v_i with overlap v_i[j+1]=v_(i+1)[j] for j<k-1 and cyclic i modulo n.
Setting x_i=v_i[0] forces v_i[j]=x_(i+j) even if j>=n. Conversely a
labelled cyclic word supplies those windows and all n edges uniquely.
This is a bijection for n<k as well as n>=k; it does not multiply or
divide by spatial periods. Because k>=1, an ordered vertex pair specifies
at most one appended letter, so zero-one adjacency is correct.

Taking k=t+4 and imposing delta^(t+4)w=delta^t(w_2...w_(t+2)) counts
the exact core-entry inequality tau<=t. Taking k=p and imposing
delta^p w=w_0 counts Fix(D^p). Partitioning iterate-fixed points into
least-period classes and applying divisor Möbius inversion gives p times
the number of p-cycles. The independent verifier uses closed-walk dynamic
counting for t=0,...,3 and p=1,...,6, n=1,...,6, compared with graph-derived
CDFs and cycle counts. This explicitly includes repeated-window cases.
The all-parameter justification is the bijection, not this finite box.

The A0 graph rebuilt from the local rule has 81 vertices and 165 edges.
Samuelson–Berkowitz gives its complete 82 characteristic coefficients,
including all 74 trailing zeros. They equal the factorization in Eq.(12).
This is independent of the author's trace/Newton certificate and is not
a recurrence fitted to a few terms. For positive n, zero eigenvalues
contribute zero to traces. The degree-seven nonzero spectral polynomial
therefore yields the printed recurrence from n=8, using the seven printed
positive-length initial values. The independent core graph census through
n=12 agrees. Growing matrix dimension with t,p is explicitly disclosed.

## 6. Target inverse and sharp equality

Every source over a target is a closed assignment of levels 0,1,2 to the
vertices of its comparison cycle. Equality edges contract without choices.
If all edges are equality there are exactly three assignments. Otherwise
the strict cycle is impossible with one sign or three consecutive strict
comparisons in one direction. The reviewer's level-assignment counter
explicitly assigns successive levels after contraction; neither transfer
matrices nor Fibonacci numbers enter that counter.

A doubled positive run pins its endpoints to bottom and top levels, and
a doubled negative run pins top and bottom. Cutting there separates the
remaining singleton gaps, with no unassigned shared choices. In an
alternating gap the two available end-level counts evolve by adding the
previous two counts; equivalently grouping two comparisons updates
(u,v) to (u+v,u+2v), starting with (0,1). After a gap of g singleton runs
the pinned-to-pinned count is F_(g+1), including g=0,1 giving one.
With no pin, summing closed assignments around the even alternating cycle
gives F_(r-1)+F_(r+1)=L_r. This also reproduces the manuscript's rank-one
matrix derivation and establishes sufficiency of its image condition.

The number of cyclic strict-sign runs is even, so q has parity r. The
Fibonacci addition identity bounds the product by F_(r-2q+1), without
requiring every merge to be strict. At even r with q>0, q>=2 gives
F_(r-3)<L_r. At odd r, q=1 gives F_(r-1), whereas q>=3 gives a strictly
smaller value. Optimizing over strict lengths yields exactly the theorem's
two alternating targets at even n>=4 and 2n one-zero targets at odd n>=5.
The zero target ties only at n=2,3; n=1 is separate. The old `++--` merge
counterexample does not affect this argument and is explicitly retained
as a negative control.

## 7. Verification scope and proof status

The new verifier exhausts all 797,160 sources and all 797,160 targets for
n=1,...,12, including zero fibres; checks every maximum-equality target,
run bound, core membership, cycle bound and mass; and checks the core
inverse on all recurrent states. Pointwise first-entry equations are
also followed at every t=0,...,n+1 for every state at n<=6.
The local, determinant, junction and trace checks supplement the explicit
all-size reasoning above. SymPy 1.14.0 supplies exact determinant coefficients
and integer Möbius values; the dynamical and fibre checks use the Python standard library.
No author code or scouting module is imported. No open proof finding
remains within the stated claim ceiling.
