# Batch 06 Paper 23 — Independent Candidate Review R2

## Immutable review scope

This is an offline, proof-adversarial candidate review written from an
independent recomputation of the proposed four-mode family.  It records no
public-search or global-priority score.  No literature lookup, build,
numerical certificate, parameter sweep, or project creation supports this
verdict.  The only uses of symbolic diagnostics during review were to locate
possible transcription errors; every conclusion retained below is reduced to
displayed algebra or inequalities that can be checked by hand.

The review asks whether the candidate survives the following attacks:

1. whether the gradient supports really give the stated phase matrices;
2. whether the complete-step direction is (B_gA_g), rather than (A_gB_g);
3. whether all four pure-versus-product selectors remain strict for every
   iterate;
4. whether an explicit cone containing the seed is genuinely invariant;
5. whether carried coordinates or leading-form cancellation can invalidate
   the matrix recurrence;
6. whether one fixed coordinate actually realizes the total degree;
7. whether the displayed characteristic polynomial is correct and its
   Perron root governs the first dynamical degree; and
8. whether the claimed mod-five quartic subfamily is irreducible by a
   source-level argument.

## Candidate and mandatory public headline

Let (K) be a field of characteristic zero, let (g\geq 10) be an integer,
and put

\[
V_g(q)=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},
\qquad
W_g(p)=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g.
\]

Define the positive-sign gradient shears

\[
S_g(q,p)=(q,p+\nabla V_g(q)),
\qquad
T_g(q,p)=(q+\nabla W_g(p),p),
\qquad
F_g=T_g\circ S_g.
\]

The public headline must be framed as a **break, or escape, from the Paper 22
cubic spectral collapse**.  The differentiating mechanism is that two
competing gradient rows in each phase remove the common covector-kernel that
forced Paper 22's identity eigenspace, and the surviving exact degree matrix
has a genuinely irreducible quartic Perron subfamily.  A general
support-profile rank obstruction is explanatory infrastructure only; it is
not by itself a Paper 23 headline or a novelty claim.

A suitable public-safe claim is therefore:

> A four-mode Hamiltonian product-shear family with two staggered spikes in
> each phase admits an exact four-face selector recurrence for every
> (g\geq10).  Its support profile escapes the identity-eigenspace mechanism
> behind Paper 22's cubic collapse, and for (g\equiv3\pmod5) its first
> dynamical degree is a quartic Perron number.

The product-shear construction, symplectic-gradient argument, weighted-support
method, Perron--Frobenius step, and general rank observation must be credited
as reused machinery rather than presented as new in isolation.

## Independent support and phase-matrix recomputation

Direct differentiation gives

\[
\nabla V_g=
\begin{pmatrix}
2q_1q_2^2q_3^2q_4^2+gq_1^{g-1}\\
2q_1^2q_2q_3^2q_4^2+(g-1)q_2^{g-2}\\
2q_1^2q_2^2q_3q_4^2\\
2q_1^2q_2^2q_3^2q_4
\end{pmatrix},
\]

\[
\nabla W_g=
\begin{pmatrix}
2p_1p_2^2p_3^2p_4^2\\
2p_1^2p_2p_3^2p_4^2\\
2p_1^2p_2^2p_3p_4^2+(g-1)p_3^{g-2}\\
2p_1^2p_2^2p_3^2p_4+gp_4^{g-1}
\end{pmatrix}.
\]

Selecting the two pure rows in each phase and the unique product row in every
rigid row gives

\[
A_g=
\begin{pmatrix}
g-1&0&0&0\\
0&g-2&0&0\\
2&2&1&2\\
2&2&2&1
\end{pmatrix},
\qquad
B_g=
\begin{pmatrix}
1&2&2&2\\
2&1&2&2\\
0&0&g-2&0\\
0&0&0&g-1
\end{pmatrix}.
\]

If (u_n) is the (q)-degree vector after (n) complete iterates and
(v_{n+1}) is the (p)-degree vector after the next (S_g)-phase, then the
only phase-consistent direction is

\[
v_{n+1}=A_gu_n,
\qquad
u_{n+1}=B_gv_{n+1}=B_gA_gu_n.
\]

Thus

\[
C_g=B_gA_g=
\begin{pmatrix}
g+7&2g+4&6&6\\
2g+6&g+6&6&6\\
2g-4&2g-4&g-2&2g-4\\
2g-2&2g-2&2g-2&g-1
\end{pmatrix}.
\]

The seed audit independently fixes the direction:

\[
A_g\mathbf1=(g-1,g-2,7,7)^{\mathsf T},
\]

\[
C_g\mathbf1=(3g+23,3g+24,7g-14,7g-7)^{\mathsf T}.
\]

These are the degrees obtained by applying (S_g) and then (T_g) directly;
the reversed product does not give the displayed first full step.

## Four selector faces and the exact threshold boundary

For a positive input weight write it in ordered-difference coordinates as

\[
u=(a,a+r,a+r+s,a+r+s+t),
\qquad a>0,quad r,s,t\geq0.
\]

The two first-phase and two second-phase pure-minus-product score gaps are

\[
M_{S,1}=(g-8)a-6r-4s-2t,
\]

\[
M_{S,2}=(g-9)a+(g-7)r-4s-2t,
\]

\[
M_{T,3}=(3g-29)a+(3g-21)r+(3g-15)s+(2g-8)t,
\]

\[
M_{T,4}=(3g-22)a+(3g-16)r+(3g-12)s+(g-6)t.
\]

The second-phase formulas were recomputed at (v=A_gu), not at (u).
At the seed (a=1), (r=s=t=0), the four margins are respectively

\[
g-8,qquad g-9,qquad 3g-29,qquad 3g-22.
\]

Hence (g\geq10) is sufficient for all four seed selectors.  At (g=9),
the earliest exact failure is the second row of the first (S_g)-phase:
the pure derivative (q_2^{g-2}) and the product derivative both have score
(7).  This is a selector tie at iteration zero, not a later numerical
instability.  The candidate may call (g=10) sharp only for this seed and
these selected faces; it may not call it a globally optimal threshold among
all possible cones or support descriptions.

## An explicit ordered-coordinate invariant polyhedral cone

The following homogeneous, partly open polyhedral cone contains the seed and
closes all required inequalities:

\[
\mathcal K_g=\left\{
\begin{array}{l}
a>0,\quad r,s,t\geq0,\\
R:=a-(g-1)r\geq0,\\
H:=7a+5r+3s-(g-3)t>0,\\
L:=(g-9)a+(g-7)r-4s-2t>0
\end{array}
\right\}.
\]

On this cone,

\[
M_{S,2}=L>0,
\qquad
M_{S,1}=L+R>0.
\]

For (g\geq10), every coefficient in (M_{T,3}) and (M_{T,4}) is
strictly positive, so both second-phase selectors are strict on the whole
cone.

Let (u'=C_gu) and write

\[
u'=(a',a'+r',a'+r'+s',a'+r'+s'+t').
\]

Direct row subtraction gives the complete transformed-coordinate ledger

\[
\begin{aligned}
a'&=(3g+23)a+(2g+16)r+12s+6t,\\
r'&=a-(g-2)r,\\
s'&=(4g-38)a+(4g-28)r+(3g-18)s+(2g-10)t,\\
t'&=7a+5r+3s-(g-3)t.
\end{aligned}
\]

Thus (a'>0).  Since (R\geq0), one has
(r'=R+r>0).  All coefficients in (s') are positive for (g\geq10),
and (t'=H>0).

The target (R)-face has the exact positive expansion

\[
R'=a'-(g-1)r'
=(2g+24)a+(g^2-g+18)r+12s+6t>0.
\]

The target (H)-face has the exact positive expansion

\[
\begin{aligned}
H'&=7a'+5r'+3s'-(g-3)t'\\
&=(26g+73)a+(16g+53)r+(6g+39)s+(g^2+21)t>0.
\end{aligned}
\]

For the remaining target face,

\[
\begin{aligned}
L'={}&(g-9)a'+(g-7)r'-4s'-2t'\\
={}&(3g^2-19g-76)a+(g^2-9g-56)r-42s-20t.
\end{aligned}
\]

Because (s,t\geq0),

\[
42s+20t\leq\frac{21}{2}(4s+2t)
<\frac{21}{2}\bigl((g-9)a+(g-7)r\bigr),
\]

where the strict inequality is the input (L>0).  It follows that

\[
L'>P_ga+Q_gr,
\]

with

\[
P_g=\frac{6g^2-59g+37}{2},
\qquad
Q_g=\frac{2g^2-39g+35}{2}.
\]

Here (P_g>0) for (g\geq10).  If (Q_g\geq0), positivity follows
immediately.  If (Q_g<0), the input face (R\geq0) gives
(r\leq a/(g-1)), hence

\[
P_ga+Q_gr\geq
\frac{6g^3-63g^2+57g-2}{2(g-1)}a.
\]

Writing (g=10+h), the numerator becomes

\[
6h^3+117h^2+597h+268>0.
\]

Therefore (L'>0), and (C_g\mathcal K_g\subset\mathcal K_g) for every
integer (g\geq10).  This is a source-level cone proof; finite iteration
tables cannot substitute for it.

## Carried coordinates and leading-form survival

At the base step,

\[
A_g\mathbf1=(g-1,g-2,7,7)^{\mathsf T}>\mathbf1.
\]

Every entry of (C_g-I) is positive for (g\geq10).  Once the previous
full step is established,

\[
u_n-u_{n-1}=(C_g-I)u_{n-1}>0.
\]

The matrix (A_g) is nonnegative and every row has a positive entry, so the
fresh first-phase vector satisfies

\[
A_gu_n-A_gu_{n-1}>0.
\]

It therefore beats the carried (p)-vector row by row.  In the second phase,

\[
B_gA_gu_n-u_n=(C_g-I)u_n>0,
\]

so the fresh (q)-vector beats the carried (q)-coordinates row by row.
Internal selector choice and temporal carry choice are separate comparisons;
both are needed in the induction.

For the displayed positive-sign family, all starting coordinates and all
gradient coefficients lie in the positive integer semiring.  Substitution
therefore expresses every selected leading coefficient as a nonzero positive
integer sum.  Characteristic zero prevents that integer from vanishing in
(K).  Consequently no selected leading form cancels.  This proof does not
authorize arbitrary coefficient signs, subtraction shears without a separate
leading-form argument, or positive characteristic.

## Exact (q_4) visibility

For (u'=C_gu), the fourth row beats the first two rows by

\[
u'_4-u'_1=(4g-30)a+(3g-21)r+(3g-15)s+(g-7)t>0,
\]

\[
u'_4-u'_2=(4g-31)a+(4g-23)r+(3g-15)s+(g-7)t>0.
\]

The remaining internal comparison is precisely the cone face

\[
u'_4-u'_3=7a+5r+3s-(g-3)t=H>0.
\]

The fourth (q)-row also beats all four final (p)-rows (v=A_gu).  The
four fresh-minus-(p) coefficient vectors in the ((a,r,s,t)) coordinates
are

\[
(6g-6,5g-5,3g-3,g-1),
\]

\[
(6g-5,4g-3,3g-3,g-1),
\]

\[
(7g-14,5g-10,3g-6,g-3),
\]

\[
(7g-14,5g-10,3g-6,g-2),
\]

all strictly positive for (g\geq10).  Hence, for every (n\geq1), the
fourth (q)-coordinate is the unique maximum among all eight coordinate
degrees and

\[
\deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1.
\]

At (n=0) all coordinate degrees tie, although the same scalar expression
equals (1).  Public wording should state strict visibility only for
(n\geq1).

## Characteristic polynomial and quartic Perron subfamily

The trace, determinant, and principal-minor expansion give

\[
\operatorname{tr}C_g=4g+10,
\qquad
\det C_g=9(g-1)^2(g-2)^2,
\]

and

\[
\begin{aligned}
R_g(t)=\chi_{C_g}(t)
={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t\\
&+9(g-1)^2(g-2)^2.
\end{aligned}
\]

The coefficient of (t) can equivalently be written

\[
2(g-3)(2g-3)(3g-4),
\]

which is an independent expansion check.

For (g\equiv3\pmod5), reduction gives

\[
\overline R_g(t)=t^4-2t^3-t^2+1=:f(t).
\]

The values of (f) at (0,1,2,3,4) are (1,4,2,4,3), so there is no
linear factor.  If

\[
f=(t^2+at+b)(t^2+ct+d),
\]

then (bd=1), so

\[
(b,d)\in\{(1,1),(2,3),(3,2),(4,4)\}.
\]

For ((1,1)) and ((4,4)), the required equation (ad+bc=0) contradicts
(a+c=3).  For ((2,3)) or ((3,2)), those two equations force
(a=c=4), but then (ac+b+d=1\neq4), contradicting the (t^2)
coefficient.  Thus (f) is irreducible over (\mathbf F_5), and (R_g)
is irreducible over (\mathbf Q) for every (g\equiv3\pmod5).

The matrix (C_g) is entrywise positive, hence primitive.  Its spectral
radius is a simple positive eigenvalue strictly larger in modulus than every
other eigenvalue.  The exact visible-degree formula and Perron--Frobenius
asymptotics give

\[
\lambda_1(F_g)=\rho(C_g).
\]

For the infinite subfamily (g\geq10), (g\equiv3\pmod5), irreducibility
makes (R_g) the minimal polynomial of the spectral radius.  Therefore
(\lambda_1(F_g)) is a quartic Perron number.  The review does not claim
irreducibility or algebraic degree four for the other congruence classes.

## Support-profile rank obstruction and the escape mechanism

For arbitrary matrices

\[
A=-I+\sum_{i=1}^{p}u_iv_i^{\mathsf T},
\qquad
B=-I+\sum_{j=1}^{q}s_jt_j^{\mathsf T},
\]

put

\[
E=\bigcap_i\ker v_i^{\mathsf T}\cap\bigcap_j\ker t_j^{\mathsf T}.
\]

For (x\in E), one has (Ax=-x) and (B(-x)=x), so

\[
E\subseteq\ker(BA-I),
\qquad
\dim E\geq r-p-q.
\]

The sharper formulation uses the rank of the union of the two covector
profiles rather than merely (p+q).

For the present family,

\[
A_g+I
=g e_1e_1^{\mathsf T}+(g-1)e_2e_2^{\mathsf T}
+2(e_3+e_4)\mathbf1^{\mathsf T},
\]

\[
B_g+I
=2(e_1+e_2)\mathbf1^{\mathsf T}
+(g-1)e_3e_3^{\mathsf T}+g e_4e_4^{\mathsf T}.
\]

The combined covector profile

\[
\{e_1,e_2,\mathbf1,e_3,e_4\}
\]

spans the full four-dimensional dual space.  Hence the common kernel that
explains Paper 22's identity eigenspace is zero here.  Directly,

\[
R_g(1)=\det(I-C_g)
=3g(g-1)(3g^2-11g+4)\neq0
\]

for (g\geq10), so (1) is not an eigenvalue.  This is the precise
support-profile escape from cubic collapse.  The general rank lemma remains
an explanation of why the old collapse occurs and why this profile avoids it;
it is not a classification of all supports that yield quartic growth.

## Required proof spine

Any source-design package must contain, as explicit source-level lemmas:

1. the eight-row gradient-support ledger and the phase-indexed identities
   (v_{n+1}=A_gu_n), (u_{n+1}=B_gA_gu_n);
2. the four exact selector gaps, including evaluation of the second phase at
   (v=A_gu) and the (g=9) seed tie;
3. the ordered-difference cone (\mathcal K_g), all four transformed
   coordinates, and separate preservation of (R,H,L);
4. rowwise first-phase and second-phase carry inequalities;
5. characteristic-zero positive-leading-form survival;
6. strict (q_4) visibility against the other seven coordinate degrees;
7. the characteristic-polynomial derivation and support-profile escape; and
8. the hand proof of mod-five irreducibility followed by the primitive-matrix
   Perron argument.

A sampled orbit, numerical eigenvalue computation, computer factorization, or
finite modulus sweep may be used only as a private error-finding aid and may
not replace any item above.

## Anti-claims and failure boundaries

The candidate may not claim:

- validity for (g\leq9), or that the displayed recurrence survives the
  exact (g=9) selector tie unchanged;
- a globally optimal threshold, maximal selector cone, necessary cone, or
  classification of all selector chambers;
- arbitrary signs, arbitrary nonzero coefficients, subtraction shears, or
  positive-characteristic validity without a new cancellation proof;
- a quartic minimal polynomial for every (g\geq10);
- a general theorem that every full-rank support profile produces quartic
  degree growth;
- novelty of Hamiltonian gradient shears, weighted support propagation,
  Perron--Frobenius theory, or the abstract rank-kernel observation by itself;
- a new Paper 20 or Paper 21 theorem, or a restatement of Paper 22's cubic
  quotient as the principal contribution;
- entropy, integrability, conjugacy, periodic-point, genericity, or
  positive-characteristic conclusions;
- an absolute literature-priority statement from this offline review; or
- public release, submission, upload, external messaging, or any other
  external-effect authority.

The candidate stops if the public story is reduced to “one more mode gives a
larger matrix,” if the four selectors are inferred from samples, if the rank
obstruction replaces the explicit quartic escape theorem, or if the mod-five
claim is supported only by a computer factorization.

## Standalone-size and proof-confidence assessment

After predecessor material is charged against the candidate, a proof-first
article of approximately 24--28 content pages is credible within the required
22--30 page window.  A proportionate allocation is: 2--3 pages for the
Hamiltonian family and public boundary; 3--4 for the support-rank obstruction
and Paper 22 escape signature; 5--6 for the four selector faces and invariant
cone; 3--4 for carry and leading forms; 3 for visibility and exact degree;
4--5 for the quartic spectral and arithmetic argument; and 2--3 for sharp
boundaries, anti-claims, and comparison.  Governance, hashes, internal paths,
and discovery narrative are not counted as article content.

- Proof confidence: **9.4 / 10**.
- Standalone mathematical-size confidence: **8.4 / 10**.
- Twenty-two-to-thirty-page feasibility: **PASS**.
- Public novelty score: **NOT ASSIGNED BY THIS OFFLINE REVIEW**.

The residual proof risk is concentrated, and explicitly closed above, in the
(L')-face inequality and in preserving the phase labels through carried
coordinates.  No counterexample remains for the stated (g\geq10),
characteristic-zero, positive-sign family.  This verdict supports the
proof-feasibility side of a candidate gate only and creates no project,
publication, build, release, or external-effect authority.

PAPER23_CANDIDATE_GATE_PASS_R2
