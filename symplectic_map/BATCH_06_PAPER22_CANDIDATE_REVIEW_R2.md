# Batch 06 Paper 22 Candidate Review R2

## Independence and scope

This is a fresh proof-and-counterexample audit of the candidate stated in the
review assignment.  I did not inspect or wait for the sibling R1 review.  I
used no web or network access, created no paper project, ran no build, and ran
no scientific experiment.  A few exact symbolic substitutions were used only
as non-authoritative error probes; every accepted identity is derived below.

## Disposition

**Mathematical status:** `PROVABLE AS STATED UNDER THE EXPLICIT INDEX
CONVENTION BELOW`.

**Candidate gate:** pass.  The proof closes for every integer
\(r\ge 4\) and \(g\ge 2r+1\) over every characteristic-zero field.  The
threshold case \(g=2r+1\), every allowed equality \(x_i=1\), both carried
coordinate phases, leading-form survival, Perron visibility, the invariant
subspace, the quotient cubic, and the exact multiplicity of the eigenvalue
\(1\) all survive direct audit.

Two drafting conventions are mandatory:

1. The normalized variables are \(x_i=u_i/u_1\) for
   \(2\le i\le r\), and the cone sum is
   \(\sigma=\sum_{i=2}^r x_i\).  If the displayed sum were instead read as
   \(\sum_{i=1}^r x_i\), the claimed seed containment would be false at
   \(g=2r+1\), because that sum would be \(r>(2r-1)/2\).
2. The last \(q\)-coordinate strictly dominates the other coordinates for
   full iterates \(n\ge 1\).  At \(n=0\), all coordinate degrees equal one,
   although the exact degree formula still holds.

These are statement locks, not missing lemmas.  With them made explicit, no
mathematical repair remains.

## Normalized claim and notation

Let \(K\) be a field of characteristic zero, let \(r\ge4\), and let
\(g\ge2r+1\) be integers.  Set

\[
h=g-1,\qquad m=r-2,
\]

so that \(m\ge2\) and \(h\ge2m+4\).  On
\(K^r_q\times K^r_p\), put

\[
V(q)=\prod_{i=1}^r q_i^2+q_1^g,
\qquad
W(p)=\prod_{i=1}^r p_i^2+p_r^g,
\]

and define

\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),\qquad F=T\circ S.
\]

Let \({\bf 1}\in\mathbb R^r\) be the all-one column, let

\[
M=2{\bf 1}{\bf 1}^{\mathsf T}-I_r,
\]

let \(A\) be obtained from \(M\) by replacing its first row by
\(h e_1^{\mathsf T}\), let \(B\) be obtained from \(M\) by replacing its
last row by \(h e_r^{\mathsf T}\), and put \(C=BA\).

For a positive column \(u\), define

\[
x_i=\frac{u_i}{u_1}\quad(2\le i\le r),
\qquad
\sigma=\sum_{i=2}^r x_i,
\]

and use the open homogeneous cone

\[
\mathcal K=\left\{u>0:x_i\ge1\ (2\le i\le r),\quad
\sigma<\frac{g-2}{2}=\frac{h-1}{2}\right\}.
\]

## Dependency map

1. The gradient ledger gives exactly two competitive support rows and the
   phase matrices \(A\) and \(B\).
2. The first competitive row is selected by the defining height inequality of
   \(\mathcal K\); the second is selected by a separate optimized inequality.
3. Explicit row formulas for \(C\) prove all lower faces and the upper face of
   \(\mathcal K\) are strict after one full step.
4. Positivity of \(C-I\), \(C-A\), and all nonzero rows of \(A\) closes both
   carried-coordinate inductions.
5. A highest-homogeneous-form argument in the polynomial domain rules out
   cancellation and also validates the precisely stated arbitrary-nonzero-
   coefficient extension.
6. Row differences make \(e_r\) the unique degree-visible coordinate for
   \(n\ge1\); Perron--Frobenius then identifies the dynamical degree.
7. A direct invariant decomposition \(K^r=U\oplus E\) reduces the spectral
   calculation to the stated \(3\times3\) matrix, whose three elementary
   invariants give the cubic and whose value at one gives the exact
   multiplicity \(r-3\).

## 1. Full gradient and support ledger

The gradients are

\[
\frac{\partial V}{\partial q_1}
=2q_1\prod_{j=2}^r q_j^2+gq_1^{g-1},
\]

\[
\frac{\partial V}{\partial q_i}
=2q_i\prod_{j\ne i}q_j^2
\quad(2\le i\le r),
\]

\[
\frac{\partial W}{\partial p_i}
=2p_i\prod_{j\ne i}p_j^2
\quad(1\le i<r),
\]

and

\[
\frac{\partial W}{\partial p_r}
=2p_r\prod_{j=1}^{r-1}p_j^2+gp_r^{g-1}.
\]

The mixed exponent in row \(i\) is the \(i\)-th row of \(M\): it has entry
one at \(i\) and entry two everywhere else.  The only extra exponents are
\(h e_1\) in the first \(V\)-row and \(h e_r\) in the last \(W\)-row.
Thus there are exactly two, and not merely at most two, nontrivial selector
comparisons.  Every other gradient row is a singleton.

The subtraction formulas give polynomial inverses for \(S\) and \(T\).  Their
Jacobians have the standard triangular blocks

\[
J_S=\begin{pmatrix}I&0\\ \nabla^2V&I\end{pmatrix},\qquad
J_T=\begin{pmatrix}I&\nabla^2W\\0&I\end{pmatrix}.
\]

Both Hessians are symmetric, so each shear preserves the standard symplectic
form.  No algebraic closure assumption is used.

## 2. The two selector margins

Let \(v=Au\).  Directly from the support rows,

\[
\frac{v_1}{u_1}=h,
\qquad
\frac{v_i}{u_1}=2+2\sigma-x_i\quad(2\le i\le r).
\]

### First shear

The pure first-row score minus the mixed first-row score is

\[
hu_1-\left(u_1+2\sum_{i=2}^r u_i\right)
=u_1(h-1-2\sigma).
\]

It is strictly positive on \(\mathcal K\).  Write
\(\delta=h-1-2\sigma>0\); this is the exact first selector margin divided by
\(u_1\).

### Second shear

The pure last-row score minus the mixed last-row score is

\[
\Delta_T=(h-1)v_r-2\sum_{j<r}v_j.
\]

Substitution and collection give

\[
\frac{\Delta_T}{u_1}
=(2h-4m)\sigma-(h+1)x_r-4m-2. \tag{2.1}
\]

Because the \(m\) middle normalized coordinates are at least one,
\(x_r\le\sigma-m\).  Put \(b_T=h-4m-1\).  From (2.1),

\[
\frac{\Delta_T}{u_1}
\ge b_T\sigma+m(h-3)-2. \tag{2.2}
\]

If \(b_T<0\), the strict upper bound
\(\sigma<(h-1)/2\) reverses in multiplication and yields

\[
\frac{\Delta_T}{u_1}
>\frac{(h+1)(h-2m-3)}2>0.
\]

If \(b_T\ge0\), then \(\sigma\ge m+1\), and (2.2) yields

\[
\frac{\Delta_T}{u_1}
\ge(2m+1)(h-2m-3)>0.
\]

The final factor is at least one because \(h\ge2m+4\).  Hence the second
selector is strict throughout the whole cone, including at the parameter
threshold.

## 3. Seed and strict cone invariance

At the seed \(u_0={\bf1}\), one has \(x_i=1\) and
\(\sigma=r-1=m+1\).  Since

\[
m+1<\frac{2m+3}{2}\le\frac{h-1}{2},
\]

the seed lies strictly in \(\mathcal K\), including when
\(g=2r+1\).

Let \(U'=Cu\), and divide all row formulas by \(u_1\).  Direct multiplication
of \(B A\) gives

\[
D:=\frac{U'_1}{u_1}
=h+4m+4+(4m+2)\sigma, \tag{3.1}
\]

\[
\frac{U'_i}{u_1}
=2h+4m+2+4m\sigma+x_i
\quad(2\le i<r), \tag{3.2}
\]

and

\[
\frac{U'_r}{u_1}=h(2+2\sigma-x_r). \tag{3.3}
\]

### Middle lower faces

Subtracting (3.1) from (3.2) gives

\[
\frac{U'_i-U'_1}{u_1}
=h-2-2\sigma+x_i
=\delta+(x_i-1)>0. \tag{3.4}
\]

Thus every normalized middle coordinate of \(U'\) is strictly larger than
one, even when its input value equals one.

### Last lower face

Subtracting (3.1) from (3.3) gives

\[
L_1:=\frac{U'_r-U'_1}{u_1}
=h-4m-4+(2h-4m-2)\sigma-hx_r. \tag{3.5}
\]

Using \(x_r\le\sigma-m\) and putting \(b_1=h-4m-2\),

\[
L_1\ge(m+1)(h-4)+b_1\sigma. \tag{3.6}
\]

If \(b_1<0\), then

\[
L_1>\frac{(h+2)(h-2m-3)}2>0;
\]

if \(b_1\ge0\), then

\[
L_1\ge2(m+1)(h-2m-3)>0.
\]

Hence the last normalized coordinate is also strictly larger than one.

### Upper height face

Let

\[
H_2=(h-1)U'_1-2\sum_{i=2}^rU'_i.
\]

Equations (3.1)--(3.3) give

\[
\frac{H_2}{u_1}
=h^2-h-8m^2-8m-4+c\sigma+2(h+1)x_r, \tag{3.7}
\]

where

\[
c=(4m-2)h-8m^2-4m-4.
\]

At the smallest allowed \(h=2m+4\),
\(c=8m-12>0\) because \(m\ge2\), and \(c\) increases with \(h\).
Therefore (3.7) is minimized on the allowed lower faces at
\(\sigma=m+1\) and \(x_r=1\).  The resulting exact value factors as

\[
\frac{H_2}{u_1}
\ge(h-2m-3)(h+4m^2+4m+2)>0. \tag{3.8}
\]

Consequently

\[
\sum_{i=2}^r\frac{U'_i}{U'_1}<\frac{h-1}{2}.
\]

Equations (3.4), (3.6), and (3.8) prove the strict inclusion
\(C\mathcal K\subset\mathcal K\).  At \(g=2r+1\), the common factor
\(h-2m-3\) equals one, so no threshold equality is being hidden.

## 4. Every carried coordinate

The row formulas above show directly that \(C-I\) is entrywise positive:

- row one has entries \(h+4m+4\) and \(4m+2\);
- a middle row has first entry \(2h+4m+2\), entries \(4m\) off its
  middle diagonal, and entry \(4m+1\) on that diagonal;
- the last row is \((2h,\ldots,2h,h)\).

After subtracting the identity, every listed entry remains positive.  Hence
\(Cu>u\) for every positive \(u\).

At the seed,

\[
A{\bf1}=(h,2r-1,\ldots,2r-1)^{\mathsf T}>{\bf1}.
\]

If \(u_n>u_{n-1}\), then every nonnegative nonzero row of \(A\) gives
\(Au_n>Au_{n-1}\).  This proves that each fresh \(S\)-gradient coordinate
strictly beats its carried \(p\)-coordinate.  In the \(T\)-phase,

\[
BAu_n-u_n=(C-I)u_n>0,
\]

so each fresh \(T\)-gradient coordinate strictly beats its carried
\(q\)-coordinate.  These are row-by-row comparisons; no aggregate-degree
shortcut is used.

It follows inductively that, with \(u_0={\bf1}\),

\[
v_{n+1}=Au_n,\qquad u_{n+1}=Cu_n\quad(n\ge0), \tag{4.1}
\]

provided the selected leading forms survive.  That remaining point is closed
next.

## 5. Leading forms and arbitrary nonzero coefficients

Let \(\operatorname{LH}(f)\) denote the highest total-degree homogeneous form
of a nonzero polynomial.  Since a polynomial ring over a field is an integral
domain,

\[
\operatorname{LH}(fg)=\operatorname{LH}(f)\operatorname{LH}(g)\ne0,
\qquad
\deg(fg)=\deg f+\deg g.
\]

If \(\deg f>\deg g\), then
\(\operatorname{LH}(f+g)=\operatorname{LH}(f)\).  The two selector margins
and the two carried-coordinate margins proved above are all strict, so every
coordinate update has exactly one higher-degree source term before its factors
are multiplied.  Its leading form is a nonzero scalar times a product of
previous nonzero leading forms.  Induction in the polynomial domain therefore
proves survival without requiring coefficient positivity.

This also answers the coefficient question.  The following extension is safe:

\[
V_{a,b}=a\prod q_i^2+bq_1^g,
\qquad
W_{c,d}=c\prod p_i^2+dp_r^g,
\qquad a,b,c,d\in K^\times.
\]

The relevant derivative scalars are \(2a,gb,2c,gd\), all nonzero in
characteristic zero.  The supports, strict degree comparisons, matrices, and
domain argument are unchanged.  Thus arbitrary signs or phases of these four
nonzero coefficients cannot cancel the strictly selected leading form.

The safe statement is limited to these fixed two-monomial potentials with all
four displayed coefficients nonzero.  It should not be inflated into a claim
about arbitrary added support terms or positive characteristic.

## 6. Last-coordinate visibility and exact degree

First, \(C-A=(B-I)A\) is entrywise positive.  For a row \(i<r\), the
corresponding row of \(B-I\) has coefficient two in every position except a
zero at \(i\), so it forms twice the sum of all other rows of \(A\); this is
positive in every column.  Its last row is \((h-1)\) times the positive last
row of \(A\).  Hence

\[
Cu>Au\quad\text{coordinatewise for every }u>0. \tag{6.1}
\]

Thus every full-step \(q_i\)-degree exceeds its corresponding
\(p_i\)-degree.

Equation (3.5) already proves \(U'_r>U'_1\).  For a middle index
\(2\le i<r\), put \(s=\sum_{j=2}^{r-1}x_j\), so that
\(s\ge m\), \(\sigma=s+x_r\), and
\(x_r<(h-1)/2-s\).  Direct row subtraction gives

\[
L_i:=\frac{U'_r-U'_i}{u_1}
=(2h-4m)\sigma-hx_r-x_i-4m-2. \tag{6.2}
\]

Put \(b_i=h-4m\).  If \(b_i<0\), then the strict upper bound for \(x_r\)
in (6.2) gives

\[
L_i>hs-x_i+b_i\frac{h-1}{2}-4m-2
\ge\frac{(h+2)(h-2m-3)}2>0. \tag{6.3}
\]

Here \(hs-x_i\ge hm-1\) follows by assigning the lower value one to all
middle variables.  If \(b_i\ge0\), all relevant coefficients are minimized
at the lower faces, and

\[
L_i\ge(2m+1)(h-2m-3)>0. \tag{6.4}
\]

Therefore the last \(q\)-coordinate strictly exceeds all other
\(q\)-coordinates after every full step.  Combining this with (6.1) shows
that it strictly exceeds all \(2r-1\) other coordinate degrees for every
\(n\ge1\).

The complete exact statements are consequently

\[
\deg_q(F^n)=u_n=C^n{\bf1},
\qquad
\deg_p(F^n)=A C^{n-1}{\bf1}\quad(n\ge1),
\]

and

\[
\deg(F^n)=e_r^{\mathsf T}C^n{\bf1}\quad(n\ge0). \tag{6.5}
\]

Since \(C\) is entrywise positive, Perron--Frobenius and (6.5) give

\[
\lambda_1(F)=\rho(C).
\]

Both the seed and the visible functional are positive on the Perron direction,
so there is no spectral visibility gap.

## 7. Invariant subspace, quotient matrix, cubic, and multiplicity

Define

\[
U=\left\{z\in\mathbb Q^r:z_1=z_r=0,\quad
\sum_{i=2}^{r-1}z_i=0\right\}.
\]

Its dimension is \(r-3\).  For \(z\in U\), the mixed matrix sends the
middle coordinates to their negatives, while both endpoint coordinates stay
zero.  More explicitly, \(Az=-z\) and then \(B(-z)=z\).  Hence

\[
Cz=z\qquad(z\in U). \tag{7.1}
\]

Let

\[
E=\{(a,b,\ldots,b,c)^{\mathsf T}:a,b,c\in\mathbb Q\}.
\]

Because the characteristic is zero and \(m\ne0\), one has the direct sum
\(\mathbb Q^r=U\oplus E\).  The space \(E\) is invariant.  In the basis
\(e_1,\sum_{i=2}^{r-1}e_i,e_r\), equivalently in the coordinates
\((a,b,c)\mapsto(a,b,\ldots,b,c)\), the restriction of \(C\) is

\[
Q=
\begin{pmatrix}
h+4m+4 & 2m(2m+1) & 2(2m+1)\\
2h+4m+2 & 4m^2+1 & 4m\\
2h & 2mh & h
\end{pmatrix}. \tag{7.2}
\]

The trace is

\[
\operatorname{tr}Q=2h+4m^2+4m+5.
\]

The three principal \(2\times2\) minors are

\[
h\bigl(1-4m(m+1)\bigr)+4,
\qquad h(h-4m),
\qquad h(1-4m^2),
\]

whose sum is

\[
h^2-8hm(m+1)+2h+4.
\]

The restrictions of \(A\) and \(B\) to \(E\) each have determinant
\(-h(2m+1)\), so

\[
\det Q=h^2(2m+1)^2.
\]

Therefore

\[
P(t)=t^3-(2h+4m^2+4m+5)t^2
+(h^2-8hm(m+1)+2h+4)t-h^2(2m+1)^2 \tag{7.3}
\]

is exactly the characteristic polynomial of \(Q\), and

\[
\chi_C(t)=(t-1)^{r-3}P(t). \tag{7.4}
\]

Substitution at one gives

\[
P(1)=-4m(m+1)(h+1)^2\ne0. \tag{7.5}
\]

Thus the algebraic multiplicity of the eigenvalue \(1\) is exactly, not just
at least, \(r-3\).

The seed \({\bf1}\) belongs to \(E\).  Hence the exact degree sequence
\(d_n=e_r^{\mathsf T}C^n{\bf1}\) is controlled by the cubic alone.  If

\[
T_0=2h+4m^2+4m+5,
\quad S_0=h^2-8hm(m+1)+2h+4,
\quad D_0=h^2(2m+1)^2,
\]

then Cayley--Hamilton gives the exact scalar recurrence

\[
d_{n+3}=T_0d_{n+2}-S_0d_{n+1}+D_0d_n\quad(n\ge0), \tag{7.6}
\]

with \(d_0=1\) and \(d_1=h(2m+3)\).  The matrix \(Q\) is positive, and the
Perron eigenvector of \(C\) is fixed by every permutation of the middle
coordinates, so it lies in \(E\).  Therefore \(\rho(C)=\rho(Q)>1\), and the
Perron root is a root of the displayed cubic.

## 8. Sharp boundary and the Paper 21 reduction

At the seed, the first pure-minus-mixed score is

\[
h-(2r-1)=g-2r.
\]

Thus \(g=2r\) gives an exact selector tie.  At the same parameter,
\(\sigma=r-1=(g-2)/2\), so the seed also lies on the open cone's height
boundary.  At \(g=2r+1\), the selector margin is one and the cone-height slack
is one half.  This proves that \(g\ge2r+1\) is sharp for this particular
strict-face proof and seed.  It does **not** prove that every possible degree
description must fail at \(g=2r\); the manuscript should not make that stronger
claim.

Formally setting \(r=3\), hence \(m=1\), turns (7.2) into

\[
\begin{pmatrix}
g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1
\end{pmatrix},
\]

and (7.3) into

\[
t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2,
\]

exactly the matrix and cubic of Paper 21.  That specialization is predecessor
consistency, not a new contribution.  Paper 22's standalone claim must remain
the \(r\ge4\) uniform family, the \(r-3\) invariant eigenspace, and its
three-dimensional quotient.  It should not advertise a new \(r=3\) theorem or
silently import a different threshold statement into Paper 21.

## 9. Adversarial boundary ledger

| Attack | Result |
|---|---|
| Literal sum includes \(x_1\) | False seed claim at \(g=2r+1\); exclude \(x_1\) explicitly. |
| Input lower face \(x_i=1\) | Allowed; (3.4), (3.6), and (3.8) return strict output inequalities. |
| Input height approaches equality | The negative-coefficient cases use the open inequality with the correct reversed sign and retain a positive factored margin. |
| Parameter equality \(g=2r+1\) | All decisive factors reduce to positive quantities because \(h-2m-3=1\). |
| Parameter \(g=2r\) | Exact first-selector tie and seed height equality; strict selected-face proof cannot cross this boundary. |
| Full iterate \(n=0\) | Exact degree formula holds, but strict global-coordinate dominance does not; state dominance for \(n\ge1\). |
| Old \(p\)-coordinates | Beaten row by row by \(Au_n-Au_{n-1}>0\). |
| Old \(q\)-coordinates | Beaten row by row by \((C-I)u_n>0\). |
| Arbitrary nonzero coefficients | Safe for the four displayed support coefficients by the leading-form domain proof; unsafe to generalize to added supports or positive characteristic. |
| Hidden extra \(1\)-eigenvalue | Excluded by \(P(1)\ne0\); multiplicity is exactly \(r-3\). |
| Perron root hidden from the cubic | Excluded because the positive Perron vector is middle-permutation invariant and lies in \(E\). |
| \(r=3\) novelty inflation | Algebraically identical to Paper 21; explicitly predecessor-only. |

## 10. Conservative scores

These scores are assigned only after the proof audit above has closed.

- **Proof completeness and correctness: 9.3/10.**  This clears the required
  \(9.0\) threshold.  The deductions are exact and cover the threshold and
  all carried coordinates.  The residual risk is editorial transcription in a
  long index-heavy proof, not an unproved mathematical step.
- **Standalone paper viability: 8.5/10.**  The uniform high-dimensional
  theorem, exact degree recurrence, visible Perron root, invariant
  \(r-3\)-space, and fixed cubic quotient form a coherent proof paper.  It
  still needs disciplined exposition so that the quotient mechanism is the
  main structural contribution rather than a long re-run of Paper 21.
- **Novelty within the audited local sequence: 7.2/10.**  The invariant
  eigenspace and dimension-independent cubic quotient are meaningful new
  structure for \(r\ge4\), but the family is a natural permutation-symmetric
  lift of Paper 21.  No external literature-priority score is warranted
  because this review was deliberately offline.

## Required claim locks for drafting

1. Write \(\sigma=\sum_{i=2}^r x_i\) every time the cone is introduced.
2. State strict global visibility only for \(n\ge1\), while keeping (6.5) for
   \(n\ge0\).
3. Describe \(g=2r+1\) as sharp for the chosen strict selected face and seed,
   not as an absolute optimality theorem.
4. State the arbitrary-coefficient extension only for four nonzero
   coefficients on the displayed two supports.
5. Treat \(r=3\) solely as exact reduction to Paper 21.
6. Make no positive-characteristic, arbitrary-support, classification,
   genericity, or literature-priority claim.

PAPER22_CANDIDATE_GATE_PASS_R2
