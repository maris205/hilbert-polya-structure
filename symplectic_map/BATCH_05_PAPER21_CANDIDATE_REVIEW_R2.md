# Paper21 repaired candidate — independent R2 gate

## Verdict

**GO / PASS**, subject to the corrected visibility coordinate and the explicit
coefficient-semiring induction below. Recommended score triple:

| Novelty | Standalone | Proof |
|---:|---:|---:|
| 8.4/10 | 8.8/10 | 9.3/10 |

The candidate is materially distinct from Papers 12–20 when framed narrowly:
it is a canonical two-shear family on \(\mathbb A^6\), with a genuinely coupled
three-variable support and a cubic Perron characteristic polynomial. It should
not be presented as a classification, a generic all-dimensional extension, or
an unconditional non-product/non-conjugacy theorem.

## Frozen theorem audited

Let \(K\) be algebraically closed of characteristic zero and \(g\ge 8\). Set
\[
 V=q_1^2q_2^2q_3^2+q_1^g,\qquad
 W=p_1^2p_2^2p_3^2+p_3^g,
\]
\[
 S(q,p)=(q,p+\nabla V(q)),\qquad
 T(q,p)=(q+\nabla W(p),p),\qquad F=T\circ S.
\]
These are canonical Hamiltonian shears; they are not affine-triangular maps in
the Blanc–van Santen/Shao–Sun ordering sense. The selected matrices are
\[
 A=\begin{pmatrix}g-1&0&0\\2&1&2\\2&2&1\end{pmatrix},\quad
 B=\begin{pmatrix}1&2&2\\2&1&2\\0&0&g-1\end{pmatrix},\quad
 C=BA=\begin{pmatrix}g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1\end{pmatrix}.
\]
For \(u=(u_1,u_2,u_3)\), write \(x=u_2/u_1\), \(y=u_3/u_1\), and
\[
 \mathcal K_g=\{u_i>0:x\ge1,\ y\ge1,\ x+y<R\},\qquad R=(g-3)/2.
\]

## Independent algebra audit

### First selector \(S\)

The three gradient weights are
\[
 (g-1)u_1,\quad 2u_1+u_2+2u_3,\quad 2u_1+2u_2+u_3.
\]
For the only two-term competition,
\[
 (g-1)u_1-(u_1+2u_2+2u_3)
 =u_1[(g-2)-2(x+y)]>u_1,
\]
because \(x+y<R\). At the base step the carried-coordinate gaps are
\((g-2)u_1\), \(2u_1+2u_3\), and \(2u_1+2u_2\), respectively.

### Second selector \(T\)

With \(v=Au\) and \(u_1=1\),
\[
 v_1=g-1,\qquad v_2=2+x+2y,\qquad v_3=2+2x+y.
\]
The \(p_3^{g-1}\) term in the third row beats the mixed term by
\[
 (g-2)v_3-2v_1-2v_2
   =(2g-6)x+(g-6)y-6\ge 6
\]
for \(g\ge8\), \(x,y\ge1\). The old \(q\)-coordinate gaps are
\(Bv-u=(C-I)u>0\) entrywise.

### Old-term induction and no cancellation

At full step \(n\), let \(u_n=\deg q^{(n)}\). For \(n\ge1\),
\(\deg p^{(n)}=Au_{n-1}\). Since \(C-I>0\),
\(u_n=Cu_{n-1}>u_{n-1}\), and hence \(Au_n>Au_{n-1}\); this handles all
carried \(p\)-terms in \(S\). After \(S\), the carried \(q\)-terms in \(T\)
 are dominated by \((C-I)u_n>0\). The base \(n=0\) gaps are the direct
ones above, with \(u_0=(1,1,1)\in\mathcal K_g\).

All forward-iterate coefficients belong to the semiring \(\mathbb N\subset K\):
the only new coefficients are \(2\) and the positive integer \(g\). Thus
coincident monomials add nonzero characteristic-zero coefficients; they cannot
cancel. The strict selector inequalities therefore give exact, not merely
upper-bound, degree vectors and the recurrence \(u_{n+1}=Cu_n\).

## Cone invariance and boundaries

For \(U=Cu\), after normalizing \(u_1=1\),
\[
 U_1=g+7+6x+6y,\quad U_2=2g+4+5x+4y,\quad
 U_3=(g-1)(2+2x+y).
\]
The required margins are
\[
 U_2-U_1=g-3-x-2y>1,
\]
since \(x+2y<(x+y)+(R-1)=g-4\), and
\[
 U_3-U_1=g-9+(2g-8)x+(g-7)y\ge8
\]
at the worst case \(g=8,x=y=1\). The sum margin is
\[
 H=RU_1-U_2-U_3
 =\tfrac12[g^2+2gx+4gy-4g-24x-24y-25].
\]
For \(8\le g\le11\), the coefficient of \(x\) is negative; using
\(x<R-y\) gives
\[
 H>g^2+gy-\tfrac{19}{2}g+\tfrac{11}{2}
 \ge \tfrac{2g^2-17g+11}{2}\ge\tfrac32.
\]
For \(g\ge12\), \(H\) is increasing in both \(x,y\), and
\(H\ge(g^2+2g-73)/2>0\). Hence \(\mathcal K_g\) is strictly \(C\)-invariant,
including the delicate \(g=8\) endpoint limits.

## Degree visibility

\[
 C-A=\begin{pmatrix}8&6&6\\2g+2&4&2\\2g-4&2g-4&g-2\end{pmatrix}>0,
\]
so every \(q\)-degree dominates its corresponding carried \(p\)-degree.
The visible total-degree coordinate is **the third coordinate**, not the second:
\[
 U_3-U_2=(2g-7)x+(g-5)y-6\ge6.
\]
For example, at \(g=8\), \(C(1,1,1)=(27,29,35)\). Therefore
\[
 \deg(F^n)=e_3^{\mathsf T}C^n(1,1,1)^{\mathsf T}
\]
(with equality of all coordinates at \(n=0\)); any manuscript claiming
\(e_2\)-visibility must be corrected.

## Perron and characteristic checks

Direct expansion gives
\[
 P_g(t)=t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2.
\]
The matrix is strictly positive, so Perron–Frobenius applies and the positive
functional \(e_3^{\mathsf T}\) sees the Perron class. Moreover,
\[
 P_g((g-1)^2)=g^3(g-6)(g-1)^2>0,
\]
and the row sums \(g+19,2g+13,5(g-1)\) are all strictly below \((g-1)^2\)
for \(g\ge8\); hence \(\rho(C)<(g-1)^2\). The latter row-sum argument is the
actual bound, not the sign of a cubic alone.

Optional degree-three lemma: for \(g\equiv2,3,4\pmod5\), the reductions are,
respectively,
\[
 t^3+t+1,\qquad t^3-2t^2-1,\qquad t^3+t^2+t-1.
\]
Each has no root in \(\mathbb F_5\), hence is irreducible as a cubic and gives
degree exactly three over \(\mathbb Q\). This optional arithmetic statement is
not needed for the degree recurrence.

## Novelty and primary-source boundary

Blanc–van Santen prove weak-Perron realization and classify the relevant
affine-triangular regimes in low dimension; see their primary arXiv paper
[`1912.01324`](https://arxiv.org/abs/1912.01324). Shao–Sun prove that
affine-triangular dynamical degrees in dimension four have algebraic degree at
most four and discuss their affine-triangular reductions; see
[`2509.14584`](https://arxiv.org/abs/2509.14584). Neither source treats this
canonical two-shear \(\mathbb A^6\) family, its three-variable Newton selectors,
or the displayed cubic recurrence. The candidate is therefore materially
distinct, while its priority claim must remain narrow.

Against Papers 12–20, the object boundary is disjoint from arithmetic clocks,
periodic-cycle covers, torus escape/trace fibers, and the earlier \(\mathbb A^4\)
two-variable shear matrix. The relationship to Paper20 is an identifiable
methodological predecessor, so the paper should emphasize the new cubic
three-way coupling and proof obligations rather than claim a generic extension.

## Required anti-claims

Do not claim: a classification of polynomial or symplectic automorphisms; a
generic theorem for arbitrary potentials, shear words, or dimensions; a finite
Newton fan for all maps; universal non-conjugacy to a product; equality with
topological, measure-theoretic, arithmetic, or other entropy notions; positive
characteristic validity; or computational/CAS certification. The strict
comparison \(\rho(C)<(g-1)^2\) is only for this displayed family and its two
elementary shear degrees.

PAPER21_CANDIDATE_GATE_PASS_R2
