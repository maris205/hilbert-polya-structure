# BATCH 06 Paper 24 Candidate Review R1

Date scope: 2026-08-25 UTC.

Reviewer independence statement: I independently rederived the mathematics from the displayed candidate formulas, read the local governance/lineage files `BATCH_06_STATUS.md`, `BATCH_06_IDEA_REPORT.md`, and the Paper 20-23 proposal/review/novelty records, and performed a bounded public primary-source search through 2026-08-25 UTC. I did not inspect any excluded Paper 23 recovery roots, did not read any R2 review for this candidate, did not ask another agent, and made no external write, upload, or message.

## 1. Executive verdict

Verdict: PASS, but only for the corrected frozen package stated below.

What passes:

- the explicit exponent-support family
  \[
  V_m=Aq_1^m q_2^2 + B q_1 q_2^{2m},\qquad
  W_{m,s}=C p_1^{s(2m+1)+1}+D p_2^{sm+1},
  \]
  with integers \(m\ge 2\), \(s\ge 1\), nonzero coefficients \(A,B,C,D\), characteristic-zero field, and \(F_{m,s}=T\circ S\);
- the exact period-two selector alternation for the standard total-degree seed;
- the exact recurrence, exact first dynamical degree \(\lambda_1(F_{m,s})=sm(2m+1)\), exact wall-gap identities, and coefficient-robust characteristic-zero no-cancellation proof;
- the rigidity statement that within the two-binomial / two-pure-power ansatz with synchronous selector switching, global chamber exchange forces the pure-power exponent ratio, and for this family forces \((e:f)=(2m+1:m)\);
- the abstract period-\(k\) monodromy proposition, provided it is stated as a conditional exact-degree lemma with explicit carry, selector, and visibility hypotheses.

What does not pass as a headline novelty claim:

- any claim that the abstract period-\(k\) selector-to-monodromy principle is itself unprecedented;
- any claim of a complete/maximal selector fan or classification beyond the stated two-term binomial / two-pure-power ansatz;
- any claim on the wall \(r=2\);
- any period \(>2\) realization theorem, arbitrary automaton realization, inverse-degree theorem, entropy/integrability/genericity theorem, or literature-priority theorem.

My gate judgment is that the corrected package is now large enough and different enough from Papers 20-23 to support a standalone Paper 24, but only if the frozen theorem statement stays narrow and the structural lemmas are explicitly subordinated to the explicit \(m\)-family.

## 2. Complete rederivation of the explicit \(m\)-family

### 2.1 Family and symplecticity

Fix a characteristic-zero field \(K\), integers \(m\ge 2\), \(s\ge 1\), and nonzero coefficients \(A,B,C,D\in K^\times\). Set

\[
V_m(q)=Aq_1^m q_2^2 + B q_1 q_2^{2m},
\]
\[
W_{m,s}(p)=C p_1^{s(2m+1)+1}+D p_2^{sm+1}.
\]

Define

\[
S(q,p)=(q,p+\nabla V_m(q)),\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),\qquad
F_{m,s}=T\circ S.
\]

Both maps are polynomial automorphisms. Their Jacobians are block-triangular with symmetric off-diagonal Hessian blocks:

\[
DS=\begin{pmatrix} I & 0 \\ \nabla^2 V_m(q) & I \end{pmatrix},\qquad
DT=\begin{pmatrix} I & \nabla^2 W_{m,s}(p) \\ 0 & I \end{pmatrix},
\]

and symmetric Hessians imply preservation of

\[
\omega=dq_1\wedge dp_1+dq_2\wedge dp_2.
\]

The inverses are explicit:

\[
S^{-1}(q,p)=(q,p-\nabla V_m(q)),\qquad
T^{-1}(q,p)=(q-\nabla W_{m,s}(p),p).
\]

So \(F_{m,s}\) is an exact-gradient polynomial symplectomorphism.

### 2.2 Gradients and selector matrices

Differentiate:

\[
\partial_{q_1}V_m = mA q_1^{m-1}q_2^2 + B q_2^{2m},
\]
\[
\partial_{q_2}V_m = 2A q_1^m q_2 + 2mB q_1 q_2^{2m-1},
\]
\[
\partial_{p_1}W_{m,s} = (s(2m+1)+1)C\, p_1^{s(2m+1)},
\]
\[
\partial_{p_2}W_{m,s} = (sm+1)D\, p_2^{sm}.
\]

Let \(u=(u_1,u_2)\) be the \(q\)-degree vector after a full step, and let \(r=u_1/u_2\).

For \(\partial_{q_1}V_m\), compare

- mixed row \((m-1,2)\), degree \((m-1)u_1+2u_2\),
- pure row \((0,2m)\), degree \(2m\,u_2\).

Their difference is

\[
(m-1)u_1+2u_2-2mu_2=(m-1)(u_1-2u_2).
\]

For \(\partial_{q_2}V_m\), compare

- mixed row \((m,1)\), degree \(mu_1+u_2\),
- pure row \((1,2m-1)\), degree \(u_1+(2m-1)u_2\),

with the same difference

\[
mu_1+u_2-(u_1+(2m-1)u_2)=(m-1)(u_1-2u_2).
\]

Hence the two coordinates switch synchronously at the common wall \(r=2\):

- for \(r<2\), both pure rows dominate:
  \[
  A_-=\begin{pmatrix}
  0 & 2m\\
  1 & 2m-1
  \end{pmatrix};
  \]
- for \(r>2\), both mixed rows dominate:
  \[
  A_+=\begin{pmatrix}
  m-1 & 2\\
  m & 1
  \end{pmatrix}.
  \]

The \(W\)-phase contributes the diagonal exponent matrix

\[
B_m=\operatorname{diag}(2m+1,m),
\]

and with the common scale \(s\),

\[
C_-=s\,B_mA_-,\qquad C_+=s\,B_mA_+.
\]

Explicitly,

\[
C_-=
s\begin{pmatrix}
0 & 2m(2m+1)\\
m & m(2m-1)
\end{pmatrix},
\qquad
C_+=
s\begin{pmatrix}
(m-1)(2m+1) & 4m+2\\
m^2 & m
\end{pmatrix}.
\]

### 2.3 Projective dynamics and strict chamber exchange

If \(r<2\), then

\[
r'=\frac{u_1'}{u_2'}=
\frac{s(2m+1)\cdot 2m\,u_2}{sm(u_1+(2m-1)u_2)}
=\frac{2(2m+1)}{r+2m-1}
=:h_m(r).
\]

If \(r>2\), then

\[
r'=\frac{s(2m+1)((m-1)u_1+2u_2)}{sm(mu_1+u_2)}
=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}
=:\ell_m(r).
\]

Now:

\[
h_m(r)>2
\iff
2(2m+1)>2(r+2m-1)
\iff
r<2,
\]

so \(h_m\) sends \(0<r<2\) strictly into \(r>2\).

Also

\[
\ell_m(r)-1
=
\frac{(m^2-1)r+3m+2}{m(mr+1)}
>0,
\]

and

\[
2-\ell_m(r)
=
\frac{(m+1)(r-2)}{m(mr+1)}
>0
\quad (r>2),
\]

so \(\ell_m\) sends \(r>2\) strictly into \(1<r<2\).

Therefore:

- every positive ray with \(r\neq 2\) alternates chambers forever;
- the standard total-degree seed \(u_0=(1,1)\), with \(r_0=1\), follows the strict itinerary
  \[
  -, +, -, +, \dots;
  \]
- the wall is never hit once the orbit starts off the wall, because
  \[
  h_m(r)=2 \iff r=2,\qquad \ell_m(r)=2 \iff r=2.
  \]

This is the key mechanism missing from Papers 20-23: the degree orbit does not stay in one invariant face region, but crosses the Newton wall every step in a rigid period-two pattern.

### 2.4 Carry domination and strict \(T\)-dominance

Base step: initially all coordinate degrees are \(1\). Since \(r_0=1<2\), the selected \(V\)-rows have degree

\[
2m>1,\qquad 1+(2m-1)=2m>1,
\]

so they beat the initial \(p\)-carry. Then the \(W\)-outputs have degrees

\[
2m(2m+1)s,\qquad 2m^2 s,
\]

both \(>1\), so they beat the old \(q\)-carry as well.

Induction step: for \(n\ge 1\), once the \(W\)-output dominates the old \(q\)-carry, the current \(p\)-degree vector is exactly

\[
\deg p_n = \left(\frac{u_{n,1}}{s(2m+1)},\frac{u_{n,2}}{sm}\right).
\]

Now check both chambers.

If \(r<2\), the newly selected \(V\)-degrees are

\[
v_1=2m\,u_2,\qquad v_2=u_1+(2m-1)u_2.
\]

They beat the carried \(p\)-degrees because

\[
2m\,u_2>\frac{u_1}{s(2m+1)}
\quad\text{(since }r<2\text{)},
\]
\[
u_1+(2m-1)u_2>\frac{u_2}{sm}
\quad\text{(obvious for }m\ge 2\text{)}.
\]

The \(W\)-outputs then beat the old \(q\)-degrees:

\[
s(2m+1)\,v_1 = 2m(2m+1)s\,u_2 > u_1
\quad (r<2),
\]
\[
sm\,v_2 = sm(u_1+(2m-1)u_2)>u_2.
\]

If \(r>2\), the selected \(V\)-degrees are

\[
v_1=(m-1)u_1+2u_2,\qquad v_2=mu_1+u_2.
\]

These beat the carried \(p\)-degrees because

\[
(m-1)u_1+2u_2>\frac{u_1}{s(2m+1)},
\]
\[
mu_1+u_2>\frac{u_2}{sm}.
\]

Then the \(W\)-outputs beat the old \(q\)-degrees:

\[
s(2m+1)v_1>u_1,\qquad sm\,v_2>u_2.
\]

Hence there is no hidden carry obstruction. All exact degree transport claims needed for the explicit family already hold at \(s=1\); no asymptotic \(s\to\infty\) argument is needed.

### 2.5 Coefficients and no-cancellation

The coefficient-robust claim survives.

Reason: once a chamber is fixed, each \(V\)-coordinate has one uniquely dominant monomial, not merely a dominant degree. Inductively each coordinate of \(q_n,p_n\) has a unique leading monomial. Then:

- the leading term of the selected gradient coordinate is a nonzero scalar times a product/power of existing leading monomials;
- the unselected gradient term has strictly smaller degree off the wall;
- the old carried coordinate has strictly smaller degree by the carry inequalities above;
- the \(W\)-phase is pure-power, so its leading term is just a nonzero scalar times a power of the selected leading monomial.

Because \(K\) is a domain and all coefficients \(A,B,C,D\) are nonzero, these leading monomials cannot vanish. Characteristic zero is needed because the derivative constants \(m,2,2m,s(2m+1)+1,sm+1\) must remain nonzero.

So arbitrary nonzero coefficients are admissible in characteristic zero. I found no sign-based obstruction.

### 2.6 Visibility: \(q_1\) is globally maximal

Within the \(q\)-block:

- if \(r<2\), then \(u_1'/u_2'=h_m(r)>2\), so \(u_1'>u_2'\);
- if \(r>2\), then \(u_1'/u_2'=\ell_m(r)\in(1,2)\), so \(u_1'>u_2'\).

Against the current \(p\)-coordinates:

- in the \(-\)-chamber,
  \[
  u_1'=s(2m+1)v_1>s m\, h_m(r)\,v_2>v_2,\qquad u_1'>v_1;
  \]
- in the \(+\)-chamber,
  \[
  u_1'=s(2m+1)v_1>v_1,
  \]
  and
  \[
  u_1'-v_2
  =
  s(2m+1)\bigl((m-1)u_1+2u_2\bigr)-(mu_1+u_2)>0
  \]
  for \(m\ge 2\), \(s\ge 1\), \(r>2\).

Thus for every \(n\ge 1\), the first \(q\)-coordinate is strictly maximal among all four coordinates of \(F_{m,s}^n\), hence

\[
d_n:=\deg(F_{m,s}^n)=u_{n,1}\qquad (n\ge 1).
\]

### 2.7 Monodromy, eigenvalues, exact recurrence, and wall-gap identities

For the standard seed, one full even-odd cycle uses

\[
P_m:=C_+C_- = s^2 P_m^{(1)},
\]

with

\[
P_m^{(1)}=
\begin{pmatrix}
2m(2m+1) & 2m(2m+1)(2m^2+m-2)\\
m^2 & m^2(4m^2+4m-1)
\end{pmatrix}.
\]

Its characteristic polynomial factors exactly:

\[
\chi_{P_m^{(1)}}(t)=
\bigl(t-m^2(2m+1)^2\bigr)\bigl(t-2m(m+1)\bigr).
\]

So the two eigenvalues are

\[
H=m^2(2m+1)^2,\qquad L=2m(m+1),
\]

and the monodromy eigenvalues for general \(s\) are \(s^2H\) and \(s^2L\).

Since \(H>L>0\) for \(m\ge 2\), the first dynamical degree is

\[
\lambda_1(F_{m,s})=\rho(P_m)^{1/2}=sm(2m+1).
\]

The parity subsequences obey

\[
u_{2j}=P_m^j(1,1)^T,\qquad
u_{2j+1}=C_-P_m^j(1,1)^T.
\]

Hence every fixed-parity scalar coordinate, in particular \(d_n\), satisfies

\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n.
\]

Equivalently,

\[
d_{n+4}
=
s^2\bigl(m^2(2m+1)^2+2m(m+1)\bigr)d_{n+2}
-2s^4m^3(m+1)(2m+1)^2d_n.
\]

Initial values:

\[
d_0=1,
\]
\[
d_1=2m(2m+1)s,
\]
\[
d_2=2m(m+1)(2m-1)(2m+1)s^2,
\]
\[
d_3=8m^4(m+1)(2m+1)s^3,
\]
\[
d_4=4m^2(m+1)(2m+1)(4m^4+2m^3-1)s^4.
\]

This agrees with the original candidate at \(m=2\):

\[
1,\ 20s,\ 180s^2,\ 1920s^3,\ 18960s^4,\dots
\]

#### Exact wall-gap identities

Let \(\Delta_n=u_{n,1}-2u_{n,2}\). Then \([1,-2]\) is a left eigenvector for the phase matrices:

\[
[1,-2]C_-=-2ms[1,-2],
\]
\[
[1,-2]C_+=-(m+1)s[1,-2].
\]

Therefore

\[
\Delta_{2j+1}=-2ms\,\Delta_{2j},
\qquad
\Delta_{2j+2}=2m(m+1)s^2\,\Delta_{2j}.
\]

Since \(\Delta_0=1-2=-1\), we get the exact formulas

\[
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,
\]
\[
u_{2j+1,1}-2u_{2j+1,2}=2ms\,(s^2L)^j.
\]

For \(m=2,s=1\), this specializes to

\[
u_{2j,1}-2u_{2j,2}=-12^j,\qquad
u_{2j+1,1}-2u_{2j+1,2}=4\cdot 12^j,
\]

exactly as claimed.

These formulas prove a useful qualitative fact: the orbit approaches the wall \(r=2\) from alternating sides, but never lands on it.

### 2.8 Spectral closed form

A full explicit closed form exists, but the cleanest frozen statement is the spectral one:

- the even subsequence \(E_j=d_{2j}/s^{2j}\) is the unique linear combination of \(H^j\) and \(L^j\) matching \(E_0=1\), \(E_1=d_2/s^2\);
- the odd subsequence \(O_j=d_{2j+1}/s^{2j+1}\) is the unique linear combination of \(H^j\) and \(L^j\) matching \(O_0=d_1/s\), \(O_1=d_3/s^3\).

That is sufficient for the paper. The recurrence plus initial values already pin down the exact degree sequence.

## 3. Audit of the structural upgrade

### 3.1 General binomial wall-exchange lemma

Take

\[
V=Aq_1^a q_2^b + B q_1^c q_2^d,
\]

with integers \(a>c\ge 1\), \(d>b\ge 1\), and nonzero coefficients.

Set

\[
R=\frac{d-b}{a-c}>0,\qquad
L=aR+b=cR+d.
\]

Then the two \(V\)-gradient coordinates compare the same two weighted degrees:

\[
(a-1,b)\ \text{vs.}\ (c-1,d),
\qquad
(a,b-1)\ \text{vs.}\ (c,d-1),
\]

and both differences equal \((a-c)(r-R)\). Hence the switch is synchronous at the common wall \(r=R\):

- for \(r>R\):
  \[
  A_\alpha=
  \begin{pmatrix}
  a-1 & b\\
  a & b-1
  \end{pmatrix};
  \]
- for \(r<R\):
  \[
  A_\beta=
  \begin{pmatrix}
  c-1 & d\\
  c & d-1
  \end{pmatrix}.
  \]

Now let

\[
W=C p_1^{e+1}+D p_2^{f+1},
\qquad e,f\in \mathbf Z_{>0}.
\]

For a selected row pair \((x-1,y)\), \((x,y-1)\), the induced ratio map is

\[
g_{(x,y)}(r)=\frac{e}{f}\cdot\frac{(x-1)r+y}{xr+y-1}.
\]

Its derivative is

\[
g_{(x,y)}'(r)
=
\frac{e}{f}\cdot \frac{1-x-y}{(xr+y-1)^2},
\]

which is strictly negative because \(x+y>1\) in all allowed cases.

At the wall, both branches take the same value:

\[
g_\alpha(R)=g_\beta(R)
=
\frac{e}{f}\cdot \frac{L-R}{L-1}.
\]

Therefore the claimed strict global chamber exchange is correct, with the exact iff:

\[
r<R \implies g_\beta(r)>R,
\qquad
r>R \implies g_\alpha(r)<R
\]

for all positive \(r\neq R\)

if and only if the common wall value equals \(R\), i.e.

\[
\frac{e}{f}\cdot \frac{L-R}{L-1}=R,
\]

equivalently

\[
\frac{e}{f}=\frac{R(L-1)}{L-R}.
\]

This is not just sufficient; it is necessary because the two branches are continuous, monotone, and meet at the common wall value.

### 3.2 Primitive integral pair and the \(m\)-family

Because \(R\) and \(L\) are rational, the forced ratio \(e/f\) is rational. Hence there is a primitive positive integer pair \((e_0,f_0)\), and every admissible integer realization is a common multiple \((se_0,sf_0)\).

For

\[
a=m,\ b=2,\ c=1,\ d=2m,
\]

one gets

\[
R=2,\qquad L=2m+2,
\]

so

\[
\frac{e}{f}=\frac{2(2m+1)}{2m}=\frac{2m+1}{m}.
\]

Thus the explicit family is exactly the wall-fixing corollary of the general binomial exchange lemma, and the old candidate is the case \(m=2\).

### 3.3 Carry and \(T\)-dominance in the structural statement

The candidate's quoted large-\(s\) inequalities are valid as crude sufficient bounds, but they are not the sharp statement and should not be frozen as the theorem.

The correct theorem-level formulation is:

- check the chamberwise inequalities directly on the actual open chambers;
- then state the explicit family where those inequalities are automatic.

For the frozen \(m\)-family, all carry and \(T\)-dominance inequalities already hold at \(s=1\), as shown in Section 2.4.

For the abstract binomial lemma, the safest wording is:

> Under the wall-fixing ratio and the stated positivity assumptions on the exponents, the phase maps are strictly exchanging on the open chambers. Exact polynomial degree transport follows after separately verifying carry domination and visibility for the chosen family.

That is enough. No asymptotic \(s\)-only headline is needed.

### 3.4 The abstract period-\(k\) monodromy proposition

The abstract proposition is mathematically correct in the following form.

Let a polynomial automorphism be factored into finitely many exact-gradient phases. Suppose along a periodic selector word of length \(k\):

1. each selected face in each phase is unique and has a strict degree gap over every unselected term;
2. selected new terms strictly beat the old-coordinate carry in the target coordinates;
3. leading forms are nonzero over a domain;
4. the selected face data produce linear degree maps \(C_0,\dots,C_{k-1}\);
5. a visible coordinate or coordinate functional \(\ell\) dominates the actual total degree on the residue class under study.

Then the exact degree-vector orbit obeys

\[
u_{km+j}=D_j M^m u_0,\qquad
M=C_{k-1}\cdots C_0,
\]

for suitable residue matrices \(D_j\), every visible residue subsequence satisfies Cayley-Hamilton for \(M\), and

\[
\lambda_1=\rho(M)^{1/k}
\]

once the Perron class is actually visible to \(\ell\) (for example by positivity/primitivity plus a coordinate-visibility argument).

I do not credit this proposition as a novelty headline. The closest public literature already uses tropical or piecewise-linear monodromy ideas in cluster settings. What is new enough here is the exact polynomial realization with carry control, no-cancellation over a domain, and a forced wall-fixing exponent ratio inside a symplectic product-shear family.

### 3.5 Qualification on “every positive initial degree ray”

This phrase needs one clarification:

- it is correct for the abstract \(q\)-degree transport system off the wall;
- it is not a statement about multiple distinct standard total-degree seeds for the actual automorphism, because the actual map still has the ordinary seed \(u_0=(1,1)\).

So the paper may state the abstract ray-exchange lemma, but the automorphism theorem should stay anchored to the standard seed.

## 4. Counterexample attempts and boundary probes

I actively looked for the following failure modes.

### 4.1 Wall tie at \(r=2\)

At \(r=2\), both \(V\)-gradient coordinates tie exactly. So the wall is a genuine excluded boundary, not a removable nuisance. No theorem should be stated on that wall.

This is not fatal because the standard seed has \(r_0=1\), and the exact chamber-gap identities show the orbit alternates around the wall without hitting it.

### 4.2 Near-wall degeneration

The orbit approaches the wall from alternating sides. So the proof cannot rely on a uniform gap bounded away from zero. It must use exact strict inequalities on open chambers. The candidate does this correctly.

### 4.3 Zero-exponent or vanishing-derivative cases

The structural lemma needs \(c\ge 1\) and \(b\ge 1\), otherwise a gradient coordinate can vanish. The frozen package already assumes that.

Positive characteristic is excluded for a real reason: derivative coefficients such as \(m\), \(2m\), \(s(2m+1)+1\), \(sm+1\) may vanish mod \(p\), breaking the selected support rows.

### 4.4 Coefficient-sign cancellation

I tried to break the proof with arbitrary nonzero signs. I found no obstruction, because the argument is not a positive-semiring argument; it is a unique leading monomial argument in a domain.

### 4.5 Alternative pure-power ratios

Inside the two-binomial / two-pure-power ansatz with synchronous wall exchange, the ratio \(e:f\) is forced by wall fixing. For the \(m\)-family this gives \((2m+1):m\). So the exponent ratio is rigid, not decorative.

### 4.6 Standalone-size failure

The original \(m=2\) candidate was close to being “another Paper 20 style matrix calculation.” The upgraded \(m\)-family plus the wall-fixing rigidity lemma fixes that concern. It is now a support-family theorem with a new proof mechanism, not just one extra computed matrix.

## 5. Local portfolio collision matrix against Papers 20-23

| Prior paper | Owned object/mechanism | Paper 24 candidate delta | Collision verdict |
|---|---|---|---|
| Paper 20 | Two-mode \(A^4\) Hamiltonian product shears with one invariant selector chamber and one fixed complete-step matrix; \(\lambda_1=(\sqrt g+1)^2\) | Same ambient dimension, but a different support family, a genuine wall at \(r=2\), forced period-two chamber exchange, monodromy \(C_+C_-\), parity laws, and rigid exponent ratio \((2m+1):m\) | Nearest predecessor, but not absorbed |
| Paper 21 | Three-mode family, one fixed selector regime, one cubic recurrence, third-coordinate visibility, mod-5 cubic subfamilies | Different dimension, different support, no period-two wall crossing there | Distinct |
| Paper 22 | Arbitrary-mode endpoint-spiked family with one explicit invariant cone and cubic spectral collapse to a 3D quotient | Candidate does the opposite kind of story: fixed two-mode family, no collapse claim, but rigid wall-crossing monodromy and exact parity laws | Distinct |
| Paper 23 | Four-mode quartic escape from Paper 22's collapse, fixed four-selector regime, quartic visible matrix | Candidate stays in two modes but uses alternating chamber exchange every step; not a quartic escape paper and not a larger-matrix lift | Distinct |

Local absorption charge:

- cite Paper 20 as the direct methodological predecessor;
- cite Papers 21-23 as internal neighboring exact-degree papers;
- do not describe Paper 24 as merely “another Perron example” or “another larger matrix.”

The new paper's internal signature is:

\[
\text{forced wall fixing}
\Longrightarrow
\text{period-two selector exchange}
\Longrightarrow
\text{monodromy } C_+C_-
\Longrightarrow
\text{exact parity laws and } \lambda_1=sm(2m+1).
\]

That signature is genuinely different from Papers 20-23.

## 6. Primary-source literature ledger

Bounded external search topics: algebraic entropy / exact degree growth, monomial and affine-triangular dynamical degrees, cluster/tropical degree recurrences, sign-stable mutation loops, polynomial symplectomorphisms, and dimension-four affine-triangular bounds. I found no direct public collision with the explicit \(m\)-family or with this exact canonical symplectic period-two wall-exchange package through 2026-08-25 UTC.

| Source | Claim supported / exact proximity | Difference from the candidate |
|---|---|---|
| Bellon-Viallet, *Algebraic Entropy*, Comm. Math. Phys. 204 (1999), DOI: 10.1007/s002200050652, link: https://link.springer.com/article/10.1007/s002200050652 | Baseline source for algebraic entropy / degree-growth viewpoint | General rational-map entropy framework, not an exact symplectic product-shear recurrence |
| Hasselblatt-Propp, *Degree-growth of monomial maps*, ETDS 27 (2007), DOI: 10.1017/S0143385707000168, link: https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/degreegrowth-of-monomial-maps/65EAA0AB8DF478FC75A9D89EEFD82DA8 | Exact degree-growth context and caution that general degree sequences need not satisfy a linear recurrence with constant coefficients | Monomial rational maps, not canonical polynomial symplectomorphisms; no present wall-switching degree proof |
| Fordy-Hone, *Symplectic Maps from Cluster Algebras*, SIGMA 7 (2011), DOI: 10.3842/SIGMA.2011.091, link: https://sigma-journal.com/2011/091/ | Closest public “symplectic + piecewise/tropical recurrence” neighbor | Birational cluster maps, not polynomial exact-gradient automorphisms; no present carry/no-cancellation theorem |
| Fordy-Hone, *Discrete Integrable Systems and Poisson Algebras From Cluster Maps*, Comm. Math. Phys. 325 (2014), DOI: 10.1007/s00220-013-1867-y, link: https://link.springer.com/article/10.1007/s00220-013-1867-y | Very close conceptual neighbor for tropical/cluster entropy and monodromy-type degree mechanisms | Again cluster birational maps, not the explicit Hamiltonian product-shear family here |
| Ishibashi-Kano, *Algebraic entropy of sign-stable mutation loops*, Geom. Dedicata 214 (2021), DOI: 10.1007/s10711-021-00606-1, link: https://link.springer.com/article/10.1007/s10711-021-00606-1 | Closest public sign-stable / wall-crossing conceptual comparison; supports the warning not to oversell the abstract period-\(k\) lemma | Cluster \(\mathcal A/\mathcal X\) transformations and stretch factors, not exact polynomial symplectic product shears |
| Janeczko-Jelonek, *Polynomial symplectomorphisms*, Bull. Lond. Math. Soc. 40 (2008), DOI: 10.1112/blms/bdm112, DOI link: https://doi.org/10.1112/blms/bdm112 | Primary-source background that polynomial symplectomorphism groups are rich and natural objects | Does not study exact degree recurrences or this wall-switching family |
| Blanc-van Santen, *Dynamical degrees of affine-triangular automorphisms of affine spaces*, ETDS 42 (2022), DOI: 10.1017/etds.2021.90, link: https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/dynamical-degrees-of-affinetriangular-automorphisms-of-affine-spaces/AC289A185EFECC01805D09B2ED113D7D | Supports the “no Perron realization priority” warning; weak Perron realization already exists in affine-triangular settings | Different class; candidate should claim no realization novelty |
| Dang-Favre, *Spectral interpretations of dynamical degrees and applications*, Ann. of Math. 194 (2021), DOI: 10.4007/annals.2021.194.1.5, link: https://annals.math.princeton.edu/2021/194-1/p05 | Spectral context for dynamical degrees and why exact matrix visibility matters | General spectral framework, not the specific selector/carry proof here |
| Shao-Sun, *Dynamical degrees of affine-triangular automorphisms in dimension four*, arXiv:2509.14584 (2025), link: https://arxiv.org/abs/2509.14584 | Most relevant current dimension-4 affine-triangular neighbor | Different class and theorem target; no direct collision with the present canonical product-shear family found |

External novelty conclusion:

- closest public mechanism: cluster/tropical/sign-stable degree transport;
- closest algebraic-dynamics class comparison: affine-triangular dynamical degrees;
- no direct public collision found with the exact frozen package.

So the safe novelty sentence is:

> I found no direct collision in a bounded primary-source search through 2026-08-25 UTC with the explicit characteristic-zero \(m\)-family of canonical product shears, its forced wall-fixing exponent ratio, and its exact period-two degree monodromy.

## 7. Claim-by-claim novelty verdict and recommended frozen theorem

### 7.1 Claim-by-claim verdict

1. Explicit \(m\)-family exact degree theorem in two modes: PASS.
2. Arbitrary nonzero coefficients over characteristic zero: PASS.
3. Forced exponent ratio \((2m+1):m\) inside the wall-exchange ansatz: PASS.
4. Exact period-two wall-gap identities: PASS.
5. Abstract binomial wall-exchange classification inside the two-term / two-pure-power ansatz: PASS, but only as a bounded lemma, not the novelty headline.
6. Abstract period-\(k\) selector-to-monodromy principle: PASS as a conditional technique statement, not as a novelty headline.
7. Any claim of priority for periodic selector monodromy in the abstract: FAIL; exclude.
8. Any claim on the wall \(r=2\): FAIL; exclude.
9. Any claim of full/maximal selector fan, arbitrary automaton realization, or period \(>2\) realization theorem: FAIL; exclude.

### 7.2 Recommended frozen title

**Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears**

This title is better than a generic “degree growth” title because it foregrounds the actual mathematical delta.

### 7.3 Recommended frozen theorem statement

Let \(K\) be a characteristic-zero field, let \(m\ge 2\), \(s\ge 1\), and let \(A,B,C,D\in K^\times\). Define

\[
V_m=Aq_1^m q_2^2 + B q_1 q_2^{2m},
\qquad
W_{m,s}=C p_1^{s(2m+1)+1}+D p_2^{sm+1},
\]
\[
S(q,p)=(q,p+\nabla V_m(q)),\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),\qquad
F_{m,s}=T\circ S.
\]

Then \(F_{m,s}\) is a polynomial symplectomorphism. For the standard total-degree seed \(u_0=(1,1)\), the \(q\)-degree ratio alternates strictly between the chambers \(r<2\) and \(r>2\), with exact phase matrices

\[
A_-=\begin{pmatrix}0&2m\\1&2m-1\end{pmatrix},\qquad
A_+=\begin{pmatrix}m-1&2\\m&1\end{pmatrix},\qquad
B_m=\operatorname{diag}(2m+1,m),
\]

so

\[
u_{2j}= (s^2 B_mA_+B_mA_-)^j(1,1)^T,\qquad
u_{2j+1}= sB_mA_-(s^2 B_mA_+B_mA_-)^j(1,1)^T.
\]

For every \(n\ge 1\), the first \(q\)-coordinate is strictly maximal among all coordinates, hence \(d_n:=\deg(F_{m,s}^n)=u_{n,1}\). If

\[
H=m^2(2m+1)^2,\qquad L=2m(m+1),
\]

then

\[
\lambda_1(F_{m,s})=sm(2m+1),
\]

and

\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n.
\]

Moreover,

\[
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,\qquad
u_{2j+1,1}-2u_{2j+1,2}=2ms\,(s^2L)^j.
\]

### 7.4 Recommended nonclaims

The paper should explicitly not claim:

- a theorem on the wall \(r=2\);
- any classification beyond the two-term binomial / two-pure-power ansatz;
- a maximal or necessary selector fan;
- arbitrary period words or arbitrary finite automata;
- arbitrary-support or arbitrary-shear-word generality;
- positive-characteristic validity;
- inverse-degree, entropy equality, integrability, genericity, periodic-point, or non-conjugacy results;
- novelty of the abstract period-\(k\) monodromy principle itself;
- any literature-priority claim beyond bounded noncollision.

## 8. Scores

Using the required candidate-gate scales:

- novelty: **7.9 / 10**
- standalone scope: **8.0 / 10**
- proof plausibility: **9.4 / 10**

Explanation:

- Novelty 7.9: the explicit family is close enough to cluster/tropical wall-crossing literature and to local Papers 20-23 that the score should stay below the mid-8s, but the forced period-two exchange and rigid exponent ratio are enough to clear the threshold.
- Standalone 8.0: once upgraded from the single \(m=2\) instance to the full \(m\)-family plus bounded wall-fixing lemma, the project comfortably supports a 22-30 content-page proof-first paper.
- Proof 9.4: the proof spine is short, exact, and auditable; I found no unstable carry or cancellation step after the coefficient-robust induction is written correctly.

If the authors tried to headline the abstract period-\(k\) selector proposition as the main novelty, I would drop the novelty score below threshold. The PASS assumes the frozen theorem/title above.

## 9. Mandatory fixes

### 9.1 Gate-blocking fixes

These are blocking only if the broader wording is kept. The PASS in this review assumes they are adopted immediately in the frozen package.

1. Freeze the headline to the explicit \(m\)-family; do not headline the abstract period-\(k\) proposition as a novelty theorem.
2. State the wall-fixing classification only inside the two-term binomial / two-pure-power ansatz with explicit hypotheses.
3. Clarify that “every positive initial degree ray off the wall” refers to the abstract degree transport system, while the automorphism degree theorem uses the standard seed.
4. Keep \(r=2\) as an explicit excluded boundary.

### 9.2 Downstream authoring fixes

1. Write the unique-leading-monomial induction cleanly, because that is what justifies arbitrary nonzero coefficients.
2. Include the exact wall-gap identities; they are both a proof tool and a useful boundary explanation.
3. Cite Paper 20 as the direct predecessor and explicitly differentiate from Papers 21-23.
4. Cite the cluster/sign-stable sources narrowly, as conceptual neighbors rather than collision claims.
5. Avoid any Perron-realization or “first periodic selector monodromy” language.

## 10. Final gate judgment

I recommend opening Paper 24 on the corrected frozen package above.

The core reason is not “one more matrix example.” It is that this family gives a rigid, exact, canonical polynomial symplectic realization of period-two selector exchange, with forced pure-power exponent ratio, explicit monodromy, exact parity laws, and a clean coefficient-robust proof. That is enough mathematical delta over Papers 20-23 and enough separation from the public cluster/affine-triangular literature to justify a standalone paper, provided the authors keep the scope disciplined.

PAPER24_CANDIDATE_GATE_PASS_R1
