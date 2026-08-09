# HCS-C22 T1--T3 derivation package

**Date:** 2026-08-09
**Status:** T1 and T3 proved; T2 exact-rational computer-assisted certificate
independently verified

## 1. Frozen object

Let

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad
a_0=\frac{59}{10},\quad a_1=\frac{61}{10},
\]

and let \(\Omega=\{0,1\}^{\mathbb Z}\).  The autonomous skew product is

\[
\mathcal F(\omega,z)
=\bigl(\sigma\omega,H_{a_{\omega_0}}z\bigr).
\]

The state and chronological conventions are

\[
z_i=(q_i,q_{i-1}),
\qquad
z_{i+1}=H_{a_{\omega_i}}z_i,
\]

and, for a protocol \(w=w_0\cdots w_{n-1}\),

\[
F_w=H_{a_{w_{n-1}}}\circ\cdots\circ H_{a_{w_0}}.
\]

Later symbols always act on the left.  No parameter or transition matrix is
averaged.

Set

\[
X_-=[-5/8,-1/3],\qquad X_+=[1/3,5/8],
\]

\[
Y_-=[-81/128,-5/16],\qquad
Y_+=[5/16,81/128],
\]

and \(N_{st}=X_s\times Y_t\).  In state order
\((--,-+,+-,++)\), put

\[
A=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.
\]

## 2. T1: common chronological survivor

### Theorem 1

For every two-sided parameter schedule
\(a_i\in[59/10,61/10]\) and every \(A\)-admissible two-sided state
itinerary, there exists exactly one complete Hénon orbit in the four-box
survivor with that joint itinerary, and its fibre tangent dynamics is
uniformly hyperbolic.  Restricting the parameter schedule to the two frozen
letters \(a_i\in\{59/10,61/10\}\), the resulting autonomous skew product has
a coding map which gives a topological conjugacy

\[
(\Lambda_{\mathcal F},\mathcal F)
\cong
(\Sigma_2\times\Sigma_A,\sigma\times\sigma).
\]

Consequently every primitive binary joint parameter--state necklace has
exactly one primitive periodic orbit.  For this full binary base,

\[
h_{\mathrm{top}}(\mathcal F|_{\Lambda_{\mathcal F}})
=\log(2\varphi),
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

### 2.1 Signed-root self-map

Write \(\varepsilon_i=\operatorname{sgn}q_i\).  The recurrence is equivalent
on the sign box to

\[
(T_{a,\varepsilon}q)_i
=\varepsilon_i
\sqrt{\frac{1-q_{i-1}-q_{i+1}}{a_i}}.
\]

The \(A\)-rule says the two neighbors of a coordinate are not both positive.
Thus the numerator \(N_i=1-q_{i-1}-q_{i+1}\) lies in

\[
\left[\frac53,\frac94\right]
\quad\text{or}\quad
\left[\frac{17}{24},\frac{31}{24}\right].
\]

Requiring \(1/9<N_i/a_i<25/64\) in both cases gives the exact strict
self-map window

\[
\boxed{\frac{144}{25}<a_i<\frac{51}{8}}.
\]

At the frozen interval the worst squared-output bounds are

\[
\frac{85}{732}\le\frac{N_i}{a_i}\le\frac{45}{118},
\]

with exact margins

\[
\frac{85}{732}-\frac19=\frac{11}{2196},
\qquad
\frac{25}{64}-\frac{45}{118}=\frac{35}{3776}.
\]

### 2.2 Uniform contraction

For either neighboring coordinate,

\[
\left|\partial_u\sqrt{\frac{1-u-v}{a_i}}\right|
=\frac1{2\sqrt{a_i(1-u-v)}}.
\]

Adding the two contributions in the sup norm gives

\[
\operatorname{Lip}(T_{a,\varepsilon})
\le
\frac1{\sqrt{(59/10)(17/24)}}
=\sqrt{\frac{240}{1003}}
<\frac12.
\]

The same bound holds for periods one and two: coincident neighbor indices
produce two derivative contributions which add, rather than one contribution
being overwritten.  Banach's theorem gives one fixed sequence for every
finite cyclic or two-sided joint itinerary.

### 2.3 Six common coverings

For \(F_a(x,y)=1-ax^2-y\), the four face ranges are obtained from

\[
F_a(1/3,Y_-),\quad F_a(5/8,Y_-),\quad
F_a(1/3,Y_+),\quad F_a(5/8,Y_+).
\]

The three distinct crossing-margin types are

\[
m_{--}(a)=
\min\left\{\frac{50a-289}{128},\frac{237-16a}{144}\right\},
\]

\[
m_{-+}(a)=
\min\left\{\frac{150a-499}{384},\frac{99-16a}{144}\right\},
\]

\[
m_{+-}(a)=
\min\left\{\frac{25a-84}{64},\frac{807-128a}{1152}\right\}.
\]

Their common strict window is exactly

\[
\boxed{\frac{289}{50}<a<\frac{99}{16}}.
\]

On \([59/10,61/10]\), the three uniform margins are

\[
\frac3{64},\qquad \frac7{720},\qquad \frac{131}{5760}.
\]

Hence the minimum exit margin is \(7/720\).  The entry coordinate is
\(y'=x\), so \(X_s\subset\operatorname{int}Y_s\) with minimum margin
\(1/128\).  The eight entry-sign mismatches and two remaining positive-exit
transitions are uniformly excluded; the smallest forbidden gap is
\(217/720\).

### 2.4 Uniform cones

With half widths

\[
r_x=\frac7{48},\qquad r_y=\frac{41}{256},
\qquad \kappa=\frac12,
\]

the normalized derivatives are

\[
D\widehat H_a=
\begin{pmatrix}
-2ax&-123/112\\
112/123&0
\end{pmatrix},
\]

\[
D\widehat H_a^{-1}=
\begin{pmatrix}
0&123/112\\
-112/123&-2ay
\end{pmatrix}.
\]

The worst case is \(a=59/10\).  The forward and backward dominance bounds
are

\[
d_u=\frac{11371}{3360},
\qquad
d_s=\frac{6361}{1968}.
\]

The outgoing slopes obey

\[
s_u=\frac{125440}{466211}<\frac12,
\qquad
s_s=\frac{15129}{44527}<\frac12,
\]

while the squared expansion bounds are

\[
E_u^2=\frac{129299641}{14112000}>1,
\qquad
E_s^2=\frac{40462321}{4841280}>1.
\]

Thus the fibre cones are strictly invariant and uniformly expanded in the
appropriate time direction.

### 2.5 Completion of the proof

The contraction fixed point satisfies

\[
a_iq_i^2+q_{i-1}+q_{i+1}-1=0,
\]

so \((q_i,q_{i-1})\) is the required Hénon orbit.  Its coordinates lie in
the specified boxes.  Conversely, any complete survivor orbit determines a
unique parameter and state itinerary and is a fixed sequence of the same
contraction.  If two joint codes agree on indices \([-N,N]\), locality of the
signed-root map and the contraction bound give, at the central coordinate,

\[
|q_0-q'_0|\le \frac54\theta^N,
\qquad \theta=\sqrt{240/1003}.
\]

Thus cylinder convergence implies orbit convergence.  Conversely, the
positive gaps between the disjoint parameter letters and state boxes make
each finite code block locally constant on the survivor.  These two facts
give continuity of the coding and its inverse.  The cone bounds give uniform
fibre hyperbolicity.  This proves Theorem 1.

The unweighted extended adjacency is \(J_2\otimes A\).  Therefore the exact
local symbolic control is

\[
\zeta_{\mathrm{local,bare}}(z)
=\frac1{\det(I-z(J_2\otimes A))}
=\frac1{1-2z-8z^3-16z^4}.
\]

This rational factor measures the chosen base extension and is not an
arithmetic signal.

## 3. T2: complete local chronology separation

### 3.1 Joint orbit convention

For a parameter word \(w\) and sign word \(\varepsilon\), cyclic phase acts
simultaneously:

\[
\rho^k(w,\varepsilon)=(\rho^kw,\rho^k\varepsilon).
\]

Primitivity is tested on the paired word
\(((w_i,\varepsilon_i))_{i=0}^{n-1}\).  The two components are never
canonicalized separately.  Reversal is stored as symmetry metadata and is
not quotiented from the Euler orbit set.

The exact fixed and primitive counts through period ten are reproduced by

\[
C_n=2^n\operatorname{tr}(A^n),
\]

\[
J_n=\frac1n\sum_{d\mid n}\mu(d)
2^{n/d}\operatorname{tr}(A^{n/d}).
\]

The certified primitive counts are

\[
(J_1,\ldots,J_{10})
=(2,1,10,35,70,165,530,1550,4320,12355).
\]

### 3.2 Oriented protocol sectors

If \(w\) is a primitive parameter word of length \(n\), every admissible
marked sign word gives a joint primitive orbit, and the canonical parameter
phase selects exactly one representative.  Define

\[
Q_w(1)
=\sum_{\varepsilon\in\mathcal E_n}
\frac1{|\Lambda_u(w,\varepsilon)|}.
\]

This aggregate is encoded as the negative linear coefficient of the oriented
conditional Euler sector

\[
P_w(X,s)=
\prod_{\varepsilon\in\mathcal E_n}
\left(1-X|\Lambda_u(w,\varepsilon)|^{-s}\right).
\]

Precisely, \(Q_w(1)=-[X]P_w(X,1)\); it is the negative of the linear
coefficient, not a separate Euler multiplicity.

It is a local-real-survivor quantity.  It is not the global all-complex flat
trace of Section 4.

### Theorem 2: exact-rational certified separation

For the minimal primitive same-cyclic-bigram, non-dihedral pair

\[
u_7=0000101,\qquad v_7=0001001,
\]

all \(\operatorname{tr}(A^7)=29\) state branches are present and

\[
Q_{u_7}(1)-Q_{v_7}(1)
\in
[-1.370858310696174854665141696288886015678305787250140153991,
\]
\[
\hspace{36mm}
-1.370858310696174854665141696288886015678305787250140153933]
\times10^{-8}.
\]

For the minimal non-dihedral same-cyclic-trigram comparison

\[
u_8=00101011,\qquad v_8=00101101,
\]

all \(\operatorname{tr}(A^8)=49\) branches are present and

\[
Q_{u_8}(1)-Q_{v_8}(1)
\in
[1.70852115874693342426703891614550117061904074322013820002,
\]
\[
\hspace{36mm}
1.70852115874693342426703891614550117061904074322013820100]
\times10^{-9}.
\]

Both intervals exclude zero.  The corresponding absolute-flat and local
signed-flat aggregates also have disjoint rational enclosures.

### 3.3 Certification method

For each of the 78 matched branch pairs---156 distinct local orbit
enclosures---the producer constructs rational centers \(\widetilde q\).
Exact integer-square-root bounds enclose
\(T(\widetilde q)\), giving a rational residual upper bound \(\delta\).
The fixed point then obeys

\[
\|q^*-\widetilde q\|_\infty
\le\frac{\delta}{1-49/100}.
\]

Rational interval matrix multiplication encloses the chronological
monodromy

\[
M=J_{n-1}\cdots J_0,
\qquad
J_i=\begin{pmatrix}-2a_iq_i&-1\\1&0\end{pmatrix}.
\]

Every trace interval lies outside \([-2,2]\), certifying hyperbolicity.
Monotonicity of

\[
|\Lambda_u|
=\frac{|\operatorname{tr}M|+
\sqrt{(\operatorname{tr}M)^2-4}}2
\]

then gives rational enclosures of \(|\Lambda_u|^{-1}\).  The branch
intervals are summed with outward rounding.  The final difference widths are
\(5.8\times10^{-64}\) and \(9.8\times10^{-64}\), respectively.

The independent checker imports no producer code.  It reconstructs the
Banach residual, coordinate boxes, monodromy intervals, aggregates, joint
counts, and symmetry mappings from the serialized artifact.  It reports zero
branch failures.

### 3.4 Cyclic and reversal controls

With \(R(q,p)=(p,q)\),

\[
RH_aR=H_a^{-1}.
\]

Therefore

\[
F_{w^{\mathrm{rev}}}=RF_w^{-1}R.
\]

For sign words, reversal is

\[
(w,\varepsilon)\longmapsto
(w^{\mathrm{rev}},\varepsilon^{\mathrm{rev}}).
\]

In four-state notation this is

\[
s_i^{R}=\operatorname{swap}(s_{-i}).
\]

Since \(\det M=1\),

\[
\operatorname{tr}(M^{-1})=\operatorname{tr}M,
\qquad
\det(I-M^{-1})=\det(I-M).
\]

All eight branchwise cyclic/reversal control families pass.  This proves
order memory only modulo the forced cyclic and reversal equivalences; it does
not produce a time arrow.

For the trigram bucket, \(u_8\) has a distinct reversed oriented necklace,
whereas \(v_8\) is achiral.  The comparison is therefore made between single
oriented sectors.  Summing dihedral classes without orbit-size normalization
would create a spurious two-to-one multiplicity.

## 4. T3: universal global collapse

### Theorem 3: fixed scheme length

Let \(w\) be any length-\(n\) protocol with all \(a_i\ne0\).  Its cyclic
fixed-orbit scheme has length \(2^n\), counted with scheme multiplicity.  Its
cyclic projective closure has no point at infinity.

For \(n\ge3\), the equations are

\[
f_i=a_ix_i^2+x_{i-1}+x_{i+1}-1.
\]

For \(n=1\) and \(n=2\), repeated neighbor incidences give

\[
f_0=a_0x_0^2+2x_0-1,
\]

and

\[
f_0=a_0x_0^2+2x_1-1,
\qquad
f_1=a_1x_1^2+2x_0-1.
\]

Under a degree-compatible monomial order,
\(\operatorname{LT}(f_i)=a_ix_i^2\).  These leading monomials are pairwise
coprime, so the equations form a Gröbner basis.  The quotient basis is

\[
\left\{x_0^{e_0}\cdots x_{n-1}^{e_{n-1}}:
e_i\in\{0,1\}\right\},
\]

of size \(2^n\).  In the homogenized cyclic-orbit closure in
\(\mathbb P^n\), setting the coordinate \(T=0\) reduces the equations to
\(a_iX_i^2=0\), forcing all \(X_i=0\); hence there is no projective point at
infinity.

The length statement is false if a letter \(a_i=0\).  A naive unsaturated
\(\mathbb P^2\) homogenization of the two composite fixed-point equations is
a different scheme and can introduce spurious infinity intersections; it is
not used here.

### Lemma 4: cyclic Hill identity

Put

\[
b_i=2a_ix_i,
\qquad
A_i=\begin{pmatrix}-b_i&-1\\1&0\end{pmatrix},
\qquad
M=A_{n-1}\cdots A_0.
\]

Let \(C=(\partial f_i/\partial x_j)\), with the doubled incidences retained at
periods one and two.  Then

\[
\boxed{\det C=(-1)^{n+1}\det(I-M)}.
\]

Indeed, \(Cu=0\) is the periodic recurrence

\[
u_{i+1}=-b_iu_i-u_{i-1},
\]

whose transfer product is \(M\).  For \(n\ge3\), let \(K_{[i,j]}\) be the
determinant of the path tridiagonal matrix on indices \(i,\ldots,j\), with
diagonal \(b_i,\ldots,b_j\) and unit off-diagonals.  Deleting a cyclic edge
and applying the path-continuant recurrence gives

\[
\det C=K_{[0,n-1]}-K_{[1,n-2]}+2(-1)^{n-1},
\]

while direct induction in the \(2\times2\) transfer product gives

\[
\operatorname{tr}M
=(-1)^n\bigl(K_{[0,n-1]}-K_{[1,n-2]}\bigr).
\]

Combining the two formulas gives

\[
\operatorname{tr}M-2=(-1)^n\det C.
\]

The low-period matrices are \([b_0+2]\) and
\(\left(\begin{smallmatrix}b_0&2\\2&b_1\end{smallmatrix}\right)\), so the
same sign convention holds.  The symbolic checker verifies the polynomial
identity independently through period eight.

### Theorem 5: global residue collapse

Assume first that all \(2^n\) fixed points are nondegenerate.  The top
homogeneous system \((a_ix_i^2)\) has no projective common zero, so the global
Grothendieck residue theorem applies.  Its critical degree is

\[
\sum_i(\deg f_i-1)=n.
\]

Thus the global residue of a polynomial of degree below \(n\) is zero.  At
degree \(n\), only the coefficient of \(x_0\cdots x_{n-1}\) in the leading
part contributes, divided by \(\prod_i a_i\).

Taking the numerator \(1\) gives residue zero.  The unique degree-\(n\) term
in \(\operatorname{tr}M\) is

\[
(-2)^n\left(\prod_i a_i\right)x_0\cdots x_{n-1},
\]

so its residue is \((-2)^n\).  Lemma 4 therefore gives

\[
\boxed{
\sum_{x\in\operatorname{Fix}F_w}
\frac1{\det(I-DF_w(x))}=0,
}
\]

and

\[
\boxed{
\sum_{x\in\operatorname{Fix}F_w}
\frac{\operatorname{tr}DF_w(x)}{\det(I-DF_w(x))}
=-2^n.
}
\]

For a multiple root, a pointwise quotient is undefined.  Define instead the
signed scheme-residue sum

\[
S_w^{\mathrm{res}}(h)
=(-1)^{n+1}\sum_{\xi}
\operatorname*{Res}_{\xi}
\frac{h(x)\,dx_0\wedge\cdots\wedge dx_{n-1}}
 {f_0\cdots f_{n-1}}.
\]

This agrees with the displayed pointwise sums when the fixed scheme is
reduced and nondegenerate.  In all cases the local-residue identities are

\[
S_w^{\mathrm{res}}(1)=0,
\qquad
S_w^{\mathrm{res}}(\operatorname{tr}M)=-2^n.
\]

Apply the first residue identity to every repeated protocol \(w^r\), whose
cyclic equation has length \(nr\).  The unit-numerator all-complex signed
residue determinant

\[
D_w^{\mathrm{res}}(z)
=\exp\left[-\sum_{r\ge1}\frac{z^r}{r}
S_{w^r}^{\mathrm{res}}(1)\right]
\]

therefore satisfies

\[
\boxed{D_w^{\mathrm{res}}(z)\equiv1.}
\]

If every repeated fixed scheme of \(F_w^r\), \(r\ge1\), is reduced and
nondegenerate, this residue determinant equals the ordinary pointwise signed
flat determinant.  Nondegeneracy at \(r=1\) alone is not sufficient for that
identification.

Likewise, summing the length-\(n\) scheme multiplicity \(2^n\) over all
\(2^n\) protocol words gives the formal full-shift bare scheme zeta

\[
\boxed{Z_{\mathrm{bare,glob}}(z)=\frac1{1-4z}.}
\]

These are global complex cancellations.  They do not imply that the local
real survivor's signed sum vanishes.  Absolute denominators and the
nonpolynomial weight \(|\Lambda_u|^{-s}\) are not holomorphic polynomial
residues and are not killed by Theorem 5.

## 5. What has and has not survived

The answer to the frozen research question is now two-level.

1. **Survives locally:** complete intrinsic instability aggregates distinguish
   oriented protocols even after matching cyclic bigram or trigram counts and
   after quotienting cyclic phase.  Reversal remains an exact equality.
2. **Collapses globally:** bare all-complex counts are universal, and the
   unit-numerator all-complex signed residue determinant is identically one.
   The ordinary pointwise flat determinant has the same conclusion only
   under all-repetition nondegeneracy.

This does not prove that the instability potential has infinite memory, is
not Livšic-cohomologous to some higher finite-memory potential, or supports a
nuclear operator.  It proves only that parameter-only locally constant
statistics through cyclic trigram order are insufficient for the certified
comparisons.

## 6. Next theorem gate

The only positive continuation justified by T1--T3 is the local
absolute/instability branch:

- one common complex pinning domain for both parameters;
- exact one-step branch operators on one named Banach space;
- nuclearity and a uniform tail bound;
- a trace formula reproducing the local absolute/instability weights.

Failure of any item closes the positive operator lane under the predeclared
work budget.  The unit-numerator all-complex signed **residue** route is
already closed by Theorem 5 and must not be revived through a finite matrix
or sign repair.  The same statement holds for the ordinary pointwise flat
route only under all-repetition nondegeneracy.  The theorem does not close
determinants with nonpolynomial intrinsic potentials, higher-degree
insertions, or representation-valued weights.
