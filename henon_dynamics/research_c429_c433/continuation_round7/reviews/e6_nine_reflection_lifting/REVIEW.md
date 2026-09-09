# R7 E6 — Independent review of the 27 reflection candidates and lifting gap

2026-09-10 UTC. Bounded internal, nonauthor, hand-only mathematical review.

## 1. Verdict, evidence and scope

**PASS: zero mathematical or source-related must-fix findings.**

I read all 245 lines of the actual
[R7 C2 report](../../c2_nine_reflection_lifting/REPORT.md), including its final
cross-fiber tables and the clarified integral CRT selector construction.
The inspected complete-file SHA-256 is

98fc3d0ed9b30c38c6050fe41ae60392e7cb720c84cb6c0b1399dcf2346f78f3.

The following statements are proved:

- Every set-preserving integral tame conjugate of a triangular reflection
  restricts to the specified set \(\mathcal K\) of 27 candidate permutations.
- A tame nine-cycle on this particular \(C\) would realize at least nine
  distinct members of \(\mathcal K\) as reflection restrictions.
- All 27 candidates preserve the point-difference gcd ideals.
- The evaluation image of \(\mathbb Z[x,y]\) on \(C\) is exactly the lattice
  of integer values having equal parity within each of the three fibers.
- The displayed candidate \(\kappa\), if it has the required tame lift,
  yields the stated nine-cycle through the complete word \(KIA\).

Neither the existence of that lift nor the liftability of all 27 candidates
is proved. Polynomial interpolation here is not a global inverse or
Jacobian condition. The original integer-period-nine problem remains open.

The report is self-contained for these assertions; no R6 proof was reopened
or modified. The checks below use its actual points and formulas, not a
summary or a computational output. No mathematical program, new agent,
external-model/API call, source-query batch, Git operation or PDF was used.
The sole new write is this review; author and shared files remain unchanged.

## 2. Frozen data, reductions and exact class

The ordered points read from the author file are
\[
(0,0),(1,0),(1,1),(3,1),(0,2),(-1,-2),(-1,0),(1,-1),(2,2).
\]
The three nonempty modulo-two fibers, in their fixed internal orders, are
\[
B_0=(1,5,9),\qquad B_1=(2,6,7),\qquad B_2=(3,4,8).
\]
They lie over \((0,0),(1,0),(1,1)\); the class \((0,1)\) is absent.
The nine listed reductions modulo three are pairwise distinct and exhaust
\(\mathbb F_3^2\).

The actual maps are
\[
A(x,y)=(1-y,x-y),\qquad
I(x,y)=(x,q(x)-y),\quad q(t)=-t^4+4t^3-2t^2-3t+2.
\]
Their substitutions give
\[
a=(1\,2\,3)(4\,5\,6)(7\,8\,9),\qquad
i=(1\,5)(3\,8)(6\,7).
\]
The five values of \(q\) at \(-1,0,1,2,3\) are \(-2,2,0,4,2\),
respectively, giving every stated \(I\)-transition.
Conjugating its three transpositions by \(a\) and \(a^{-1}\) gives exactly
the other two known reflection restrictions in the report.

The class under review is
\[
\mathcal R=\{M^{-1}\rho_QM:
M\in\operatorname{TA}_2(\mathbb Z),\ Q\in\mathbb Z[t]\},\qquad
\rho_Q(u,v)=(u,Q(u)-v).
\]
Integral inverses exist for these maps. In particular, their reductions
modulo two and three are permutations, and every \(R\in\mathcal R\) is an
involution. No bound on the degree of \(M\) or \(Q\) enters the proofs.

## 3. Local fixed points: both parity branches and coordinate invariance

Let \((u_0,v_0)\) and \((u_0+2s,v_0+2t)\) be integral fixed points of
\(\rho_Q\). The integer Taylor coefficients \(q_j\) give, after subtracting
the equations \(2v=Q(u)\) and dividing by two,
\[
2t=sQ'(u_0)+2q_2s^2+4q_3s^3+\cdots.
\]
If \(Q'(u_0)\) is odd, reduction modulo two forces \(s=0\).
Thus every normalized difference lies in the line with first coordinate zero.
If \(Q'(u_0)\) is even, division by two is legitimate in the integer equation,
and subsequent reduction modulo two gives
\[
t=(Q'(u_0)/2+q_2)s,
\]
because \(s^2=s\) in \(\mathbb F_2\). This again is a line through zero.
The argument also covers constant or linear \(Q\), with absent Taylor
coefficients zero, and all signs of \(s,t\).
Hence three fixed points in one modulo-two class cannot have two independent
normalized difference vectors over \(\mathbb F_2\).

For an integral polynomial automorphism \(M\),
\[
\frac{M(P+2z)-M(P)}2\equiv DM(P)z\pmod2.
\]
Terms of degree at least two in \(2z\) become even after the division.
Differentiating \(M^{-1}M=1\) shows that \(DM(P)\) has an inverse modulo two.
The images of congruent points are congruent, and their normalized
independence is therefore preserved in the required coordinates.

For the three actual fibers, the normalized difference matrices anchored
at labels \(1,2,3\), respectively, are
\[
W_0=\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad
W_1=\begin{pmatrix}-1&-1\\-1&0\end{pmatrix},\quad
W_2=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Direct coordinate subtraction gives these matrices, each of determinant
\(-1\). If \(R=M^{-1}\rho_QM\) fixed an entire fiber, its images under \(M\)
would be three fixed points contradicting the preceding line constraint.
This proves the prohibition on fixing all three points of any \(B_s\).

## 4. The exact fixed-point count yields an upper set of 27

Over \(\mathbb F_3\), for each of the three values of \(u\) the equation
\(2v=Q(u)\) has one and only one solution. Thus \(\overline{\rho_Q}\), and
its automorphism conjugate \(\overline R\), have exactly three fixed points.
Since \(R(C)=C\) and reduction \(C\to\mathbb F_3^2\) is a bijection, a fixed
residue is a fixed actual point of \(C\). Hence \(R\vert_C\) has exactly
three fixed points, not merely three possible fixed residue classes.

Modulo two, the occupied fibers are permuted by an involution. Its action
is either trivial or interchanges two fibers. In the latter case, all three
fixed points in \(C\) would lie in the third fiber, fixing it pointwise and
contradicting Section 3. Therefore every fiber is preserved individually.

An involution on a three-element fiber has either one or three fixed points.
Their total is three, so each fiber has one fixed point and one transposition.
Choosing its fixed label independently in the three fibers gives precisely
\(3^3=27\) distinct formal permutations \(\mathcal K\). This proves the
inclusion of all actual reflection restrictions in \(\mathcal K\).
It proves no converse inclusion.

## 5. A nine-cycle would supply nine distinct actual reflections

If \(\tau=T\vert_C\) is a nine-cycle, the induced permutation of the three
fibers has order dividing nine and is transitive, since \(\tau\) is transitive
on \(C\). It is therefore a three-cycle, not a transposition or the identity.
Consequently \(\tau^3\) preserves each fiber and acts there as a three-cycle:
as the cube of a nine-cycle it fixes no point.

For \(0\le j\le8\), the maps
\[
R_j=T^jIT^{-j}=(T^{-j})^{-1}\rho_q(T^{-j})
\]
are genuine members of \(\mathcal R\) and preserve \(C\).
Equality of two restrictions would make \(i\) commute with \(\tau^d\) for
some \(1\le d\le8\). The subgroup generated by \(\tau^d\) contains \(\tau^3\),
since \(\gcd(d,9)\) is one or three. It follows that \(i\) would commute
with \(\tau^3\).

But \(i\) has exactly one fixed point in each fiber, namely \(9,2,4\).
Commutation would fix the entire three-cycle of this point under \(\tau^3\),
contradicting the transposition in that fiber. All nine restrictions are
therefore different, and Section 4 places all of them in \(\mathcal K\).
Since three distinct candidates are already realized, a nine-cycle would
require at least six further liftable candidates. This is only necessary.

## 6. Complete gcd-ideal check

For \(P,Q\in\mathbb Z^2\), every coordinate difference of an integral
polynomial map belongs to
\(\mathfrak d(P,Q)=(P_x-Q_x,P_y-Q_y)\).
This follows by splitting a monomial difference one coordinate at a time.
Applying an integral inverse supplies the reverse ideal inclusion, hence
equality for an integral polynomial automorphism.

Within each fiber, the three absolute difference pairs are a permutation
of \((0,2),(2,0),(2,2)\). Thus all nine within-fiber ideals are \(2\mathbb Z\).
Independently subtracting the displayed coordinates gives the following
complete cross-fiber tables, in the fixed orders \(B_0,B_1,B_2\):
\[
\begin{array}{c|ccc}
B_0\text{ against }B_1&(1,0)&(1,2)&(1,0)\\
&(1,2)&(1,4)&(1,2)\\
&(1,2)&(3,4)&(3,2)
\end{array}
\]
\[
\begin{array}{c|ccc}
B_0\text{ against }B_2&(1,1)&(3,1)&(1,1)\\
&(1,1)&(3,1)&(1,3)\\
&(1,1)&(1,1)&(1,3)
\end{array}
\qquad
\begin{array}{c|ccc}
B_1\text{ against }B_2&(0,1)&(2,1)&(0,1)\\
&(2,3)&(4,3)&(2,1)\\
&(2,1)&(4,1)&(2,1)
\end{array}.
\]
Each entry has gcd one. These are all \(3\cdot3\cdot3=27\) cross-fiber
pairs: three unordered pairs of blocks, with nine pairs per block pair.
No pair is omitted or counted as an additional arithmetic restriction.
Every candidate preserves the fibers, so it preserves exactly this pattern
of gcd ideals. The test excludes none of the 27.

## 7. Exact evaluation image: integral affine interpolation and CRT

Let \(v_j\) be prescribed integer values. Congruence preservation immediately
requires equal parity inside each \(B_s\).
Conversely, assuming those parities, the following actual affine polynomials
interpolate each fiber separately:
\[
\begin{aligned}
h_0(x,y)&=v_1+\frac{v_9-v_5}{2}x+\frac{v_5-v_1}{2}y,\\
h_1(x,y)&=v_2+\frac{v_2-v_7}{2}(x-1)+\frac{v_7-v_6}{2}y,\\
h_2(x,y)&=v_3+\frac{v_4-v_3}{2}(x-1)
                  +\frac{v_3-v_8}{2}(y-1).
\end{aligned}
\]
All coefficients are integers under the stated parity assumptions.
Substituting the three points of each fiber gives its three prescribed
values. These formulas independently verify the author's unimodular-system
argument. The matrices have determinant \(\pm1\) over \(\mathbb Z\);
mere invertibility modulo two would not by itself suffice here.

Put \(S=\mathbb Z[x,y]\) and
\(\mathfrak m_P=(x-P_x,y-P_y)\), the kernel of integer evaluation at \(P\).
These are point-evaluation ideals; no maximal-ideal assumption is needed.
For points in different fibers, \(\mathfrak m_P+\mathfrak m_Q\) contains
their two integer coordinate differences. Section 6 gives an integer
Bezout combination equal to one, so the sum is \(S\).

For a finite family of ideals \(U_j\) each comaximal with \(J\), choose
\(a_j\in U_j\) with \(a_j\equiv1\pmod J\).
Their product lies in \(\bigcap_jU_j\) and is still one modulo \(J\).
Thus \((\bigcap_jU_j)+J=S\).
First applying this to all points of one fiber against a point of another,
then to all points of the other fiber, proves that
\[
J_s=\bigcap_{P\in B_s}\mathfrak m_P
\]
are pairwise comaximal. The finite-intersection step is therefore justified
on both sides, rather than assumed from notation.

For \(t\ne s\), choose \(a_{s,t}\in J_t\) with
\(a_{s,t}\equiv1\pmod{J_s}\), and put \(e_s=\prod_{t\ne s}a_{s,t}\).
Then \(e_s-1\in J_s\) and \(e_s\in J_t\) for every other \(t\).
Thus \(e_s\) takes the exact integer value one on \(B_s\) and zero elsewhere
in \(C\), not just those values modulo some integer.
The integral polynomial \(\sum_s e_sh_s\) realizes all nine values.
This proves precisely
\[
\operatorname{im}\bigl(S\longrightarrow\mathbb Z^C\bigr)
=\{(v_j):v_j\equiv v_k\pmod2\text{ within every }B_s\}.
\]

CRT applied indiscriminately to all nine point ideals would not work:
the within-fiber point ideals are not comaximal. The separate fiber
interpolants and cross-fiber grouping are essential and correctly used.

If a permutation preserves the fiber partition, its target \(x\)-values
and \(y\)-values each satisfy the required parity condition on an input
fiber. Applying the proved image formula to both coordinates realizes that
permutation on \(C\) by an integral polynomial map. The inverse permutation
can be interpolated separately for the same reason.
The resulting two maps are inverses only on this finite set; their
compositions need not be identity polynomial maps. Nothing imposes a
constant unit Jacobian, an integral polynomial inverse, or membership in
\(\operatorname{TA}_2(\mathbb Z)\).

## 8. Conditional nine-cycle target and final boundary

The candidate
\[
\kappa=(5\,9)(3\,8)(6\,7)
\]
fixes \(1,2,4\), hence belongs to \(\mathcal K\), and differs from the
three explicitly known restrictions. On the last two fibers its
transpositions cancel those of \(i\); on the first fiber multiplication
gives \(\kappa i=(1\,9\,5)\).
Applying \(a\) first and then this three-cycle yields, step by step,
\[
1\longmapsto2\longmapsto3\longmapsto9\longmapsto7
\longmapsto8\longmapsto5\longmapsto6\longmapsto4\longmapsto1 .
\]
All nine labels occur once. Therefore an actual set-preserving
\(K\in\mathcal R\) with restriction \(\kappa\) would make \(KIA\) a native
least-period-nine tame map on the displayed set. One application of the
complete word, not one factor or an augmented phase, is the tick.

No such \(K\), conjugating \(M\), or polynomial \(Q\) has been constructed.
Passing the gcd test and finite evaluation conditions does not establish
one, and failure of this one lifting target would not itself exclude every
possible tame nine-cycle.

All newly reviewed reasoning is explicit elementary algebra and finite
set arithmetic in the author file. No external tame-extension theorem is
claimed or needed. The research-review and henon-route-a-batch skills were
used for actual-file checking and exact claim boundaries, without external
review, additional agents, integration or release actions.
The finite lemmas and evaluation-image result may be accepted as bounded
auxiliary results. The full integer-nine-period and full-spectrum questions
remain unresolved, with no new contract or completed-paper count.
