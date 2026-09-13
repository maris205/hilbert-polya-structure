# Research Question

## Candidate identity

- Candidate ID: henon_period3_residue_v1
- Safe title: **A Uniform Period-Three Residue Law on Exceptional Henon
  Families**
- Date and literature cutoff: 2026-08-16 UTC
- Intended paper type: exact algebraic-dynamics specialist note
- Batch gate: BATCH04_PAPER12_CANDIDATE_GATE_PASS
- Current state: source-lock v2 frozen after bounded R1 repair; fresh
  independent v2 review pending; no code, result, figure, or manuscript
  authorized
- Bound proof-package SHA-256:
  `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`
- Required eventual scientific certificate:
  HENON_PERIOD3_RESIDUE_LAW_CERTIFIED /
  QUARTIC_MINIMAL_SEPARATOR_CERTIFIED /
  UNIVERSAL_NONVANISHING_OPEN

## Problem anchor

For a polynomial automorphism, the multiplier traces of periodic points are
conjugacy invariants. Cantat--Dujardin prove that finitely many such invariants
give a finite-to-one map in each fixed degree, but their Noetherian argument
does not identify a sharp cutoff. Their quartic Jacobian-minus-one example
exhibits a normalized positive-dimensional family on which periods one and two
are completely blind.

Paper 12 asks for an effective answer on that exact obstruction fiber:

> Is formal period three the first trace level that separates normalized
> conjugacy classes on the complete quartic fiber whose formal fixed-point
> trace multiset is \(0^4\), and what
> uniform residue mechanism survives in every even degree?

The dominant contribution is the sharp quartic theorem. The supporting
contribution is a degree-uniform two-term residue law with an exact finite
coefficient certificate. The project does not assume or claim that the
coefficient is nonzero in every degree.

## Ambient category

Unless explicitly stated otherwise:

1. the base field is algebraically closed of characteristic zero;
2. a normalized Henon map has the form

   \[
   f_p(x,y)=(y+p(x),x),
   \]

   with \(p\) monic and centered;
3. conjugacy means polynomial conjugacy within the normalized
   Friedland--Milnor Henon moduli category;
4. periodic-point statements use zero-dimensional schemes and their
   multiplicities, not only reduced point sets;
5. a formal trace multiset records the trace of the relevant derivative on
   the formal periodic zero-cycle with scheme multiplicity.

The precise normalized conjugacy theorem is proved in the bound proof package,
Steps 1--2.
No unqualified classification of arbitrary plane polynomial automorphisms is
part of this project.

## Exceptional family

For every integer \(m\ge2\), define

\[
p_{m,a}(x)=(x^m-a)^2,
\qquad
f_{m,a}(x,y)=\bigl(y+p_{m,a}(x),x\bigr).
\]

Its algebraic degree is \(2m\) and its Jacobian determinant is \(-1\). Put

\[
q_{m,a}(x)=p'_{m,a}(x)
=2m x^{m-1}(x^m-a).
\]

At a point whose first coordinate is \(x\),

\[
Df_{m,a}=
\begin{pmatrix}
q_{m,a}(x)&1\\
1&0
\end{pmatrix}.
\]

## Formal periods one and two

A fixed point has \(x=y\) and \(p_{m,a}(x)=0\). The fixed scheme has length
\(2m\). In its coordinate algebra, \(q_{m,a}\) is generally a nonzero
nilpotent with \(q_{m,a}^2=0\); its multiplication operator nevertheless has
only eigenvalue zero. The proved period-one statement is therefore

\[
\operatorname{Trace}_1(f_{m,a})=0^{\times 2m}.
\]

The fixed scheme of \(f_{m,a}^2\) is

\[
p_{m,a}(x)=p_{m,a}(y)=0
\]

of length \((2m)^2\). In its coordinate algebra,

\[
\operatorname{tr}Df_{m,a}^2=q_{m,a}(x)q_{m,a}(y)+2.
\]

The product term is nilpotent, so the multiplication spectrum is entirely
\(2\). Subtracting the diagonal formal fixed cycle gives

\[
\operatorname{Trace}_2(f_{m,a})
=2^{\times((2m)^2-2m)}.
\]

These statements must remain valid at nonreduced parameters, including
\(a=0\), because they are scheme-theoretic.

## Normalized conjugacy quotient

The proved exact quotient statement is

\[
f_{m,a}\sim f_{m,b}
\quad\Longleftrightarrow\quad
a^{2m-1}=b^{2m-1}.
\]

The forward direction follows in Steps 1--2 from the uniqueness of normalized
Henon forms and the permitted diagonal root-of-unity action. The reverse
direction exhibits that action explicitly. The quotient coordinate is
\(a^{2m-1}\), not \(a\), \(a^m\), or a chosen root.

## Period-three cyclic complete intersection

Introduce cyclic coordinates \(x_0,x_1,x_2\) and a deformation parameter
\(\varepsilon\). With indices modulo three, set

\[
F_i=(x_i^m-a)^2+\varepsilon(x_{i-1}-x_{i+1}).
\]

At \(\varepsilon=1\), the equations \(F_i=0\) encode
\(\operatorname{Fix}(f_{m,a}^3)\). Define

\[
q_i=2m x_i^{m-1}(x_i^m-a).
\]

The Jacobian determinant of the cyclic equations is

\[
t_\varepsilon
=\det\left(\frac{\partial F_i}{\partial x_j}\right)
=q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2).
\]

At \(\varepsilon=1\), this is
\(\operatorname{tr}Df_{m,a}^3\).

The leading monomials \(x_i^{2m}\) make

\[
\mathcal A_{m,a,\varepsilon}
=k[a,\varepsilon,x_0,x_1,x_2]/(F_0,F_1,F_2)
\]

a monic free \(k[a,\varepsilon]\)-module of rank \((2m)^3\). The raw
period-three moment is

\[
S_m(a,\varepsilon)
=\operatorname{Tr}_{\mathcal A_{m,a,\varepsilon}}
\left(t_\varepsilon^m\right).
\]

For a zero-dimensional complete intersection, the trace-residue formula gives

\[
S_m(a,\varepsilon)=\operatorname{Res}(t_\varepsilon^{m+1}).
\]

At \(\varepsilon=1\), the formal exact-period-three moment is obtained by
subtracting the formal fixed contribution. Step 10 proves that this fixed
contribution is zero for the chosen \(m\)-th trace power, so the raw and exact
moments coincide.

## Proved uniform theorem

Use the weights

\[
\mathrm{wt}(x_i)=1,\qquad
\mathrm{wt}(a)=m,\qquad
\mathrm{wt}(\varepsilon)=2m-1.
\]

Weighted freeness first allows

\[
\begin{aligned}
S_m(a,\varepsilon)
={}&c_{0,m}\varepsilon^{3m}
+c_{1,m}a^{2m-1}\varepsilon^{2m}\\
&+c_{2,m}a^{2(2m-1)}\varepsilon^m
+c_{3,m}a^{3(2m-1)}.
\end{aligned}
\]

The separated algebra at \(\varepsilon=0\) has \(q_i^2=0\), eliminating
\(c_{3,m}\). Steps 4--8 prove, by local Puiseux/trace analysis at the
double-root degeneration, order strictly greater than \(m\) for every branch
that could contribute to \(c_{2,m}\). Step 7 treats all three root-pattern
branches, while Step 10 supplies the exact diagonal nilpotence identity. The
resulting theorem is

\[
S_m(a,\varepsilon)
=C_m\varepsilon^{3m}
+D_m a^{2m-1}\varepsilon^{2m},
\]

and hence

\[
S_m(a)=C_m+D_m a^{2m-1}.
\]

Reversal of the cyclic coordinates proves

\[
C_m=0\qquad\text{for odd }m.
\]

The bound proof treats flatness, multiplicity, degeneration, and possible
contributions at infinity; the law is not inferred from interpolation.

## Proved exact coefficient certificate

Define

\[
H(r,k)=
\sum_{\substack{u+v=k\\2u\le r,\;2v\le r}}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v},
\]

\[
A_{m,r}=
\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
(-1)^{r+k}
\binom{m-1}{2(m-k)-1}H(r,k).
\]

The coefficient certificate proved in Step 9 is

\[
D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.
\]

If \(q=\lfloor m/2\rfloor\), the equivalent compressed form is

\[
E_m=\sum_{j=0}^{q}\binom{m+1}{j}
(2m)^{2(q-j)}A_{m,m-j},
\qquad
D_m=3(2m)^{3m+3-2q}E_m.
\]

The finite sum arises from the terminating recurrence (9.1)--(9.3), the
order-independent Laurent expansion and admissible-tuple sum (9.4)--(9.13),
the local binomial identity (9.14), and the distinguished-coordinate and
transfer-flow classification (9.17)--(9.26), including the separate \(j=0\)
flow. It is not a post hoc interpolation. Integrality is immediate from the
formula.
Nonvanishing for every \(m\) is a separate open combinatorial problem.

## Proved quartic theorem

For \(m=2\), consider every normalized quartic map

\[
f_p(x,y)=(y+p(x),x)
\]

with \(p\) monic and centered. If the formal fixed-point trace multiset is
\(0^4\), Step 11 proves that every root of \(p\) is multiple and hence

\[
p(x)=(x^2-L)^2
\]

for some \(L\). This includes the quadruple-root case \(L=0\).

On this complete fiber, the exact identity to certify is

\[
S_2^{(3)}(L)
=-1296000-1572864L^3
=-384(3375+4096L^3).
\]

The formal fixed contribution vanishes by Step 10. Step 12 proves the quartic
slope independently of the all-\(m\) combinatorial collapse. Step 13 proves
that each fixed branch occurs in \(\operatorname{Fix}(f^3)\) with exactly its
fixed-scheme multiplicity; hence the exact-period-three pointwise zero-cycle
has length \(4^3-4=60\), and the cyclewise sum is

\[
\frac{S_2^{(3)}(L)}{3}
=-432000-524288L^3.
\]

Because periods one and two are constant and conjugacy on the fiber is
classified by \(L^3\), period three is the exact minimal separator on this
fiber.

## Exact research questions

### Q1. Full-fiber classification

Does formal fixed-point trace multiset \(0^4\) force every normalized monic-centered
quartic Henon map into the family \(p=(x^2-L)^2\)?

Source-package answer: yes, proved in Step 11 by a purely algebraic
root-multiplicity argument.

### Q2. Minimal quartic separator

Does the formal period-three second trace moment recover \(L^3\) exactly,
while periods one and two remain constant?

Source-package answer: yes, with the stated integer identity, the independent
Step-12 quartic calculation, and the Step-10/13 fixed-branch analysis.

### Q3. Uniform mechanism

For every \(m\ge2\), is the \(m\)-th trace moment on
\(\operatorname{Fix}(f_{m,a}^3)\) affine in the normalized quotient
coordinate \(a^{2m-1}\)?

Source-package answer: yes, proved in Steps 4--10 by weighted
complete-intersection residue and local degeneration, not finite interpolation.

### Q4. Exact certificate

Can the slope \(D_m\) be expressed by the frozen nested-binomial sum?

Source-package answer: yes, proved in Step 9 by the recurrence, Laurent fiber
sum, local binomial identity, and transfer-flow classification.

### Q5. Universal recovery

Is \(D_m\ne0\) for every \(m\ge2\)?

Source-package answer: open. Finite exact checks are only diagnostics.

### Q6. Scope

Does the theorem determine all quartic Henon maps, compute a global cutoff
\(P(4)\), or establish global multiplier rigidity?

Source-package answer: no.

## Frozen evidence policy

1. Proof establishes the all-\(m\) law; computation may only audit its
   implementation.
2. During source-proof repair, a proof subagent incidentally rechecked the
   already-designated local recurrence at \(m=2,\ldots,7\). This was an
   unregistered, non-evidentiary source-stage diagnostic. It is not a tracker
   run, is not an input or witness for the coefficient theorem or universal
   nonvanishing, and may not be loaded by either future engine. No resulting
   value table is stored in the source package.
3. The sole registered coefficient-diagnostic tuple, if later authorized, is
   \(T_{\mathrm{reg}}=(8,9)\). It may not be expanded after seeing output. It
   attacks parity-sensitive ceiling/range handling at an adjacent even/odd
   boundary; it does not validate the proved parity theorem, universal
   nonvanishing, or any trend.
4. No prime, modulus, Riemann-zero, numerical unstable-multiplier, or
   exploratory parameter data may enter the project.
5. Arithmetic is exact: integers, rational polynomials, and canonical symbolic
   normal forms only.
6. Two independent finite engines are required for the quartic identity and
   registered coefficient checks.
7. Development checks are disclosed separately and never counted as
   registered confirmation.
8. A failed universal nonvanishing check would not falsify the safe theorem; it
   would only settle or refute the open conjecture at the tested index.

## Required decision and nonclaims

The safe positive decision is:

> Periods one and two are blind on the normalized exceptional family. The
> formal period-three \(m\)-th trace moment is affine in its exact moduli
> coordinate with an explicit finite coefficient certificate. In the complete
> quartic fiber whose formal fixed-point trace multiset is \(0^4\),
> the coefficient is nonzero and period three is the minimal conjugacy
> separator.

Forbidden extensions include:

- universal \(D_m\ne0\);
- all-degree minimal period-three recovery;
- a theorem for all quartic Henon maps;
- a global equality \(P(4)=3\);
- novelty of the Cantat--Dujardin obstruction family or its period-one/two
  blindness;
- novelty of multidimensional residue or dynatomic machinery;
- classification of all exceptional multiplier fibers;
- any prime-zero, height, arithmetic-finiteness, saddle-spectrum, or global
  rigidity theorem.

No implementation may begin until a fresh independent source-lock review binds
this document, the proof, novelty, claims, citation, plan, tracker, refinement
sidecars, and source lock and returns SOURCE_LOCK_PASS.
