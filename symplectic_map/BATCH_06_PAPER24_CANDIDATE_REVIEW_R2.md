# Paper 24 Candidate Review R2

## 1. Independence and forbidden-read declaration

I performed this review independently and offline inside the authorized local
workspace only.

- I did not read, list, stat, hash, glob, or otherwise inspect
  `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md` or any R1 correction artifact.
- I did not read, list, stat, glob, or touch the excluded roots
  `/tmp/paper23-r0-A.DyWKGR`, `/tmp/paper23-r0-B.dsQvTx`,
  `/tmp/paper23-r0-repair-A.BzlBNd`, `/tmp/paper23-r0-repair-B.TVRci7`,
  or `/tmp/paper23-r1-evidence-recovery.h8tfL9eu`.
- I used no web/network access and no external side effects.
- Local lineage consulted: `BATCH_06_STATUS.md`, `BATCH_06_IDEA_REPORT.md`,
  and selected proposal/proof/novelty files under `papers/20-*` through
  `papers/23-*`.

Verdict: candidate PASS. I found no theorem-critical defect in the frozen
statement once its scope is kept exactly as given.

## 2. Complete derivation

### 2.1 Geometry and exact family

Let

\[
V_m=Aq_1^m q_2^2+B q_1 q_2^{2m},
\qquad
W_{m,s}=C p_1^{s(2m+1)+1}+D p_2^{sm+1},
\]

with \(K\) characteristic zero, \(m\ge2\), \(s\ge1\), and
\(A,B,C,D\in K^\times\). Then

\[
S(q,p)=(q,p+\nabla V_m(q)),
\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),
\qquad
F_{m,s}=T\circ S.
\]

Literal derivatives:

\[
\partial_{q_1}V_m=mAq_1^{m-1}q_2^2+Bq_2^{2m},
\qquad
\partial_{q_2}V_m=2Aq_1^m q_2+2mBq_1q_2^{2m-1},
\]
\[
\partial_{p_1}W_{m,s}=(s(2m+1)+1)C\,p_1^{s(2m+1)},
\qquad
\partial_{p_2}W_{m,s}=(sm+1)D\,p_2^{sm}.
\]

Both shears are polynomial automorphisms with explicit inverses obtained by
subtracting the same gradients. Their Jacobians have the standard block forms

\[
J_S=\begin{pmatrix}I&0\\H_V&I\end{pmatrix},
\qquad
J_T=\begin{pmatrix}I&H_W\\0&I\end{pmatrix},
\]

with symmetric Hessians \(H_V,H_W\), hence both preserve
\(\omega=dq_1\wedge dp_1+dq_2\wedge dp_2\). So the exact polynomial
symplectomorphism claim passes.

### 2.2 The common selector wall and the branch matrices

Let \(u=(u_1,u_2)\in\mathbf R_{>0}^2\) be the current \(q\)-degree vector and
put \(r=u_1/u_2\).

For \(\partial_{q_1}V_m\), the competing weighted degrees are

\[
(m-1)u_1+2u_2
\quad\text{and}\quad
2m\,u_2.
\]

For \(\partial_{q_2}V_m\), the competing weighted degrees are

\[
mu_1+u_2
\quad\text{and}\quad
u_1+(2m-1)u_2.
\]

Both differences equal \((m-1)(u_1-2u_2)\), so the same wall
\(r=2\) governs both coordinates.

- If \(r<2\), the selected rows are

  \[
  A_-=
  \begin{pmatrix}
  0&2m\\
  1&2m-1
  \end{pmatrix}.
  \]

- If \(r>2\), the selected rows are

  \[
  A_+=
  \begin{pmatrix}
  m-1&2\\
  m&1
  \end{pmatrix}.
  \]

For the second shear there is no inner competition: each updated \(q_i\)
receives one pure power. Writing

\[
B_m=\operatorname{diag}(2m+1,m),
\]

the complete-step branch matrices are

\[
C_-^{(1)}=B_mA_-=
\begin{pmatrix}
0&2m(2m+1)\\
m&m(2m-1)
\end{pmatrix},
\]
\[
C_+^{(1)}=B_mA_+=
\begin{pmatrix}
(m-1)(2m+1)&2(2m+1)\\
m^2&m
\end{pmatrix}.
\]

The actual one-step degree updates are \(u' = s C_\pm^{(1)}u\), i.e.
\(C_\pm=sC_\pm^{(1)}\).

### 2.3 Branch maps and strict period-two selector exchange

If \(r<2\), then after the complete step

\[
r'=\frac{u_1'}{u_2'}
=\frac{2(2m+1)}{r+2m-1}
=:h_m(r).
\]

Since \(0<r<2\),

\[
2m-1<r+2m-1<2m+1,
\]

so

\[
2<h_m(r)<\frac{2(2m+1)}{2m-1}.
\]

Thus \(h_m\) maps the open chamber \(0<r<2\) strictly into \(r>2\).

If \(r>2\), then after the complete step

\[
r'=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}
=:\ell_m(r).
\]

Two exact identities close the right branch:

\[
2-\ell_m(r)=\frac{r-2}{m(mr+1)}>0,
\]
\[
\ell_m(r)-1
=\frac{(m^2-m-1)r+3m+2}{m(mr+1)}>0.
\]

Hence

\[
1<\ell_m(r)<2
\qquad(r>2).
\]

Therefore the seed \(u_0=(1,1)\), with \(r_0=1\), has a primitive strict
period-two selector itinerary:

\[
r_{2j}\in(1,2),\qquad r_{2j+1}>2 \qquad(j\ge0).
\]

No later iterate can land on the wall \(r=2\).

### 2.4 Carry dominance: first step and all later steps

This is the main place where a selector-only argument could fail. It does not
fail here.

At the first \(S\)-step,

\[
A_-(1,1)^{\mathsf T}=(2m,2m)^{\mathsf T}>(1,1)^{\mathsf T},
\]

so the newly created \(p\)-degrees beat the carried degree-one \(p\)-seed.

For later steps, write \(v_n\) for the \(p\)-degree vector after applying the
\(n\)-th \(S\)-phase.

#### Later \(S\)-phase carry after an odd complete step

If \(u_n=sB_mv_n\) with \(r_n>2\), then the next \(S\)-phase uses \(A_+\), and

\[
A_+u_n-v_n
=
\begin{pmatrix}
\bigl(s(2m+1)(m-1)-1\bigr)v_{n,1}+2ms\,v_{n,2}\\
sm(2m+1)v_{n,1}+(sm-1)v_{n,2}
\end{pmatrix}.
\]

Every coefficient is positive for \(m\ge2\), \(s\ge1\), so this difference is
strictly positive componentwise.

#### Later \(S\)-phase carry after an even complete step

If the previous \(S\)-phase used \(A_+\), write \(w=A_+u\) with \(r=u_1/u_2>2\).
Then

\[
w_1=((m-1)r+2)u_2,
\qquad
w_2=(mr+1)u_2,
\]

and

\[
w_2-w_1=(r-1)u_2>0.
\]

So \(w_1<w_2\). Since \(u'=sB_mw\), the next \(S\)-phase uses \(A_-\), and

\[
A_-u'-w
=
\begin{pmatrix}
2m^2s\,w_2-w_1\\
s(2m+1)w_1+\bigl(m(2m-1)s-1\bigr)w_2
\end{pmatrix}.
\]

Because \(w_1<w_2\) and \(2m^2s\ge8\), the first coordinate is
\(>(2m^2s-1)w_2>0\); the second is obviously positive. So the first-phase
carry also closes on every later even step.

#### \(T\)-phase carry

This is easier because \(W_{m,s}\) is pure-power.

- If \(r<2\), then

  \[
  sB_mA_-u-u
  =
  \begin{pmatrix}
  2ms(2m+1)u_2-u_1\\
  ms(u_1+(2m-1)u_2)-u_2
  \end{pmatrix}
  \]

  is positive since \(u_1<2u_2\) and \(m\ge2\).

- If \(r>2\), then

  \[
  u_1'=s(2m+1)\bigl((m-1)u_1+2u_2\bigr)>u_1,
  \qquad
  u_2'=ms(mu_1+u_2)>u_2.
  \]

Thus strict carry dominance holds at the first step and at every later step.

### 2.5 Leading-form survival for arbitrary nonzero coefficients

The arbitrary-coefficient claim also passes.

The proof is not a positive-semiring argument; it is a polynomial-domain
argument.

Inductive hypothesis: each coordinate polynomial currently has a nonzero top
homogeneous part.

- In the \(S\)-phase, each updated \(p_i\) is
  \[
  p_i+\text{(one selected competitive derivative term)}+\text{(strictly lower-degree terms)}.
  \]
  Because the selector gaps are strict, the selected derivative term has
  strictly larger total degree than the carried \(p_i\) and than the losing
  derivative term. Its top homogeneous part is a nonzero scalar multiple of a
  product of the current top homogeneous parts of \(q_1,q_2\), hence is nonzero
  in the domain \(K[q_1,q_2,p_1,p_2]\).

- In the \(T\)-phase, each updated \(q_i\) is
  \[
  q_i+\kappa\,p_i^e
  \quad\text{or}\quad
  q_i+\lambda\,p_i^f
  \]
  with \(e=s(2m+1)\), \(f=sm\). The top homogeneous part of \(p_i^e\) or
  \(p_i^f\) is the corresponding power of the nonzero top homogeneous part of
  \(p_i\), hence nonzero.

Characteristic zero is exactly what keeps the scalar multipliers
\(m,2,2m,s(2m+1)+1,sm+1\) nonzero. If one moves to positive characteristic,
some derivative rows can collapse; that boundary is real and must remain a
nonclaim.

So arbitrary nonzero \(A,B,C,D\) do not create a theorem-critical cancellation.

### 2.6 Exact visibility of \(q_1\) among all four coordinates

This was another plausible failure mode. It also closes.

First, \(q_1\) beats \(q_2\) because \(r_n=u_{n,1}/u_{n,2}>1\) for every
\(n\ge1\):

- odd \(n\): \(r_n>2\);
- even \(n\): \(1<r_n<2\).

Now compare \(q_1\) with the two carried \(p\)-degrees.

If \(n\) is odd, then \(v_n=A_-u_{n-1}\), so

\[
\frac{v_{n,2}}{v_{n,1}}
=\frac{r_{n-1}+2m-1}{2m}
<\frac{2m+1}{2m}
<2m+1.
\]

Since \(u_{n,1}=s(2m+1)v_{n,1}\), we get \(u_{n,1}>v_{n,2}\), and trivially
\(u_{n,1}>v_{n,1}\).

If \(n\) is even, then \(v_n=A_+u_{n-1}\), so

\[
\frac{v_{n,2}}{v_{n,1}}
=\frac{mr_{n-1}+1}{(m-1)r_{n-1}+2}
<2
<2m+1,
\]

again giving \(u_{n,1}=s(2m+1)v_{n,1}>v_{n,2}\) and \(u_{n,1}>v_{n,1}\).

Therefore \(q_1\) is the unique total-degree coordinate among
\((q_1,q_2,p_1,p_2)\) for every \(n\ge1\). In particular,

\[
d_n:=\deg(F_{m,s}^n)=u_{n,1}.
\]

### 2.7 Two-step monodromy, spectrum, and exact recurrence

The two-step monodromy is

\[
P=C_+^{(1)}C_-^{(1)}
=
\begin{pmatrix}
2m(2m+1) & 2m(2m+1)(2m^2+m-2)\\
m^2 & m^2(4m^2+4m-1)
\end{pmatrix}.
\]

The exact degree vectors satisfy

\[
u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
\qquad
u_{2j+1}=s\,C_-^{(1)}(s^2P)^j(1,1)^{\mathsf T}.
\]

The trace and determinant are

\[
\operatorname{tr}(P)=H+L,
\qquad
\det(P)=HL,
\]

where

\[
H=m^2(2m+1)^2,
\qquad
L=2m(m+1).
\]

Indeed,

\[
P(2,1)^{\mathsf T}=H(2,1)^{\mathsf T},
\]

so \(H\) is an eigenvalue with positive eigenvector. Since
\(\det(P)=HL\), the second eigenvalue is \(L\). As \(H>L>0\), \(P\) is a
positive Perron matrix with \(\rho(P)=H\).

Consequently

\[
\lambda_1(F_{m,s})
=\sqrt{\rho(s^2P)}
=s\,m(2m+1).
\]

This spectral derivation is valid and exact.

### 2.8 Wall-gap identities

Let \(g=(1,-2)\). Then direct multiplication gives

\[
gC_-^{(1)}=-2m\,g,
\qquad
gC_+^{(1)}=-(m+1)\,g,
\qquad
gP=L\,g.
\]

Since \(gu_0=-1\), one gets

\[
u_{2j,1}-2u_{2j,2}
=g u_{2j}
=-(s^2L)^j,
\]
\[
u_{2j+1,1}-2u_{2j+1,2}
=s\,gC_-^{(1)}u_{2j}
=2ms(s^2L)^j.
\]

These identities are especially important because they prove the selector walls
stay strict forever:

- even steps stay in \(r<2\),
- odd steps stay in \(r>2\).

### 2.9 Scalar recurrence and initial data

Because both even and odd subsequences are obtained by applying fixed row
functionals to powers of \(s^2P\), Cayley--Hamilton yields the same order-two
recurrence in the two-step index, equivalently the same order-four recurrence
with stride two:

\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n.
\]

The initial values are

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
d_3=8m^4(m+1)(2m+1)s^3.
\]

I checked these directly from the branch matrices:

\[
u_1=sC_-^{(1)}(1,1)^{\mathsf T}
=\bigl(2m(2m+1)s,\;2m^2s\bigr)^{\mathsf T},
\]

\[
u_2=s^2P(1,1)^{\mathsf T}
=
\Bigl(
2m(m+1)(2m-1)(2m+1)s^2,\;
4m^3(m+1)s^2
\Bigr)^{\mathsf T},
\]

\[
u_3=sC_-^{(1)}u_2
=
\Bigl(
8m^4(m+1)(2m+1)s^3,\;
4m^2(m+1)(4m^2-1)s^3
\Bigr)^{\mathsf T}.
\]

So the recurrence and the displayed initial values pass exactly.

### 2.10 Supporting structural lemma

For

\[
V=Aq_1^a q_2^b+Bq_1^c q_2^d
\qquad(a>c\ge1,\ d>b\ge1),
\]

the common selector wall is indeed

\[
R=\frac{d-b}{a-c},
\]

because the two derivative comparisons have the same difference
\((a-c)r-(d-b)\).

Let \(L_{\mathrm{wall}}=aR+b=cR+d\). If the selected branch corresponds to the
monomial \(q_1^xq_2^y\) and

\[
W=Cp_1^{e+1}+Dp_2^{f+1},
\]

then the synchronous branch map is

\[
g(r)=\frac ef\,\frac{(x-1)r+y}{xr+y-1}.
\]

This formula is correct: after the first phase the two updated \(p\)-degrees
are
\[
((x-1)r+y)u_2,\quad (xr+y-1)u_2,
\]
and the pure second phase multiplies them by \(e\) and \(f\).

Moreover,

\[
g'(r)= -\frac ef\frac{x+y-1}{(xr+y-1)^2}<0
\]

for \(r>0\), since \(x,y\ge1\). Therefore global strict exchange of the two open
chambers is equivalent to the single fixed-point condition \(g(R)=R\). Using
\(xR+y=L_{\mathrm{wall}}\), this is exactly

\[
\frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
\]

So the structural lemma passes as a selector lemma. Its limits also pass:

- if \(R=1\), the standard seed \((1,1)\) lies on the wall, so no strict
  seed-based itinerary follows automatically;
- integral realization is separate from the chamber-exchange identity;
- chamber exchange alone does **not** prove exact polynomial degree transport:
  strict carry, no-cancellation, and visibility are still extra hypotheses.

### 2.11 Conditional period-\(k\) selector-to-monodromy lemma

The abstract period-\(k\) lemma is mathematically sound only in the stated
conditional form:

1. each phase has a unique strict selected face on the claimed domain;
2. every fresh selected face strictly beats all carried coordinates;
3. leading homogeneous parts survive in the polynomial domain;
4. the selected weighted maps are linear on that itinerary;
5. some coordinate or explicit row functional sees the true total degree; and
6. the relevant monodromy class has a visible Perron eigenvalue.

Under those hypotheses, the residue monodromy and Cayley--Hamilton conclusions
follow. Without those hypotheses, they do not. This candidate satisfies them
for \(k=2\).

## 3. Counterexample and boundary attempts

I attacked the most likely failure points.

### 3.1 Small exact tests used only as falsification attempts

These are not theorem evidence; they are hostile sanity checks.

- \(m=2,s=1\):
  \[
  u_0=(1,1),\quad
  u_1=(20,8),\quad
  u_2=(180,96),\quad
  u_3=(1920,936).
  \]
  Ratios:
  \[
  1,\ \frac52,\ \frac{15}8,\ \frac{80}{39}.
  \]
  Gaps:
  \[
  -1,\ 4,\ -12,\ 48.
  \]
  This matches the claimed branch pattern and wall-gap formulas.

- \(m=3,s=1\):
  \[
  u_1=(42,18),\quad
  u_2=(840,432),\quad
  u_3=(18144,9000).
  \]
  Ratios are
  \[
  \frac73,\ \frac{35}{18},\ \frac{252}{125},
  \]
  again alternating across the wall and remaining \(>1\).

No contradiction appeared.

### 3.2 Genuine boundaries

- On the wall \(r=2\), both \(V\)-selectors tie in both coordinates. The
  candidate correctly makes no theorem on the wall.
- In positive characteristic, some derivative coefficients may vanish, so the
  characteristic-zero hypothesis is essential.
- If any of \(A,B,C,D\) vanishes, the support profile changes and the theorem
  collapses.
- The structural selector lemma with \(R=1\) puts the standard seed exactly on
  the wall, so it does not automatically generate a strict itinerary.

I found no hidden theorem-critical boundary beyond these stated ones.

## 4. Exact formula ledger

| Item | Verdict | Reason |
|---|---|---|
| Exact polynomial symplectomorphism | PASS | symmetric-Hessian shear argument is literal |
| Common wall \(r=2\) | PASS | both selector differences equal \((m-1)(u_1-2u_2)\) |
| \(A_-\), \(A_+\) | PASS | exact derivative rows |
| \(B_m=\mathrm{diag}(2m+1,m)\) | PASS | pure-power second phase |
| \(h_m(r)=2(2m+1)/(r+2m-1)\) | PASS | exact from \(sB_mA_-\) |
| \(\ell_m(r)=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}\) | PASS | exact from \(sB_mA_+\) |
| \(h_m:(0,2)\to(2,\infty)\) | PASS | denominator \(<2m+1\) |
| \(\ell_m:(2,\infty)\to(1,2)\) | PASS | exact formulas for \(2-\ell_m\) and \(\ell_m-1\) |
| Seed \((1,1)\) gives strict period-two itinerary | PASS | \(r_0=1<2\), branches alternate forever |
| First-step carry | PASS | \(A_-(1,1)>(1,1)\), pure-power \(T\)-carry obvious |
| Later \(S\)-carry | PASS | explicit positive differences above |
| Later \(T\)-carry | PASS | explicit positive differences above |
| Arbitrary nonzero coefficient survival | PASS | polynomial-domain top-homogeneous-part argument |
| \(q_1\) visibility among all four coordinates | PASS | \(r_n>1\) and \(u_{n,1}>v_{n,i}\) for \(n\ge1\) |
| \(u_{2j}=(s^2P)^j(1,1)^T\) | PASS | exact branch monodromy |
| \(u_{2j+1}=sC_-^{(1)}(s^2P)^j(1,1)^T\) | PASS | exact odd-step formula |
| \(P\) as above | PASS | direct multiplication |
| Eigenvalues \(H=m^2(2m+1)^2\), \(L=2m(m+1)\) | PASS | \(P(2,1)^T=H(2,1)^T\), trace/determinant close |
| \(\lambda_1=s\,m(2m+1)\) | PASS | \(\lambda_1=\sqrt{\rho(s^2P)}\) |
| Recurrence \(d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n\) | PASS | Cayley--Hamilton on \(s^2P\) |
| Initial values \(d_0,d_1,d_2,d_3\) | PASS | direct computation |
| Wall gaps \(u_{2j,1}-2u_{2j,2}=-(s^2L)^j\) | PASS | \(gP=Lg\), \(gu_0=-1\) |
| Wall gaps \(u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j\) | PASS | \(gC_-^{(1)}=-2mg\) |
| Supporting structural selector lemma | PASS | fixed-point condition at wall is necessary and sufficient |
| Conditional period-\(k\) monodromy lemma | PASS | valid only with strict selector/carry/visibility hypotheses |

I found no FAIL item in the frozen theorem package.

## 5. Portfolio check against Papers 20--23

This candidate is close to Paper 20 in ambient dimension and proof grammar, so
the collision test has to be strict.

### 5.1 Why it is not a direct rewrap

- Paper 20 fixes one mixed monomial and one pure monomial in each phase and
  obtains one persistent selector pair and one fixed \(2\times2\) complete-step
  matrix.
- This candidate fixes **two mixed monomials in the first phase and two pure
  powers in the second**, with a genuine common wall and a forced strict
  period-two selector exchange.
- The headline object is therefore not “another two-mode matrix” but the
  selector-exchange mechanism, its exact wall dynamics, and the resulting
  two-step monodromy.

### 5.2 Why it is not a Papers 21--23 rewrap

- It is not a mode lift of Paper 21.
- It is not the arbitrary-mode cubic-collapse mechanism of Paper 22.
- It is not the four-mode quartic-escape support profile of Paper 23.
- It does not rely on Paper 23's common-kernel/escape story, except in the
  weak sense that both projects reuse matrix-recursion proof grammar.

### 5.3 Portfolio verdict

Bounded internal noncollision: PASS, but narrowly. This passes only if the
public framing stays exactly at “forced period-two selector exchange in the
two-mode Hamiltonian product-shear ansatz.” Any broader framing such as
“general two-mode degree theory,” “arbitrary period,” “full chamber
classification,” or “coefficient/sign generality beyond the fixed supports”
would collapse into overclaiming.

## 6. Frozen theorem and nonclaims

The theorem I judge actually proved is:

For characteristic-zero \(K\), integers \(m\ge2\), \(s\ge1\), and arbitrary
nonzero \(A,B,C,D\in K\), the exact-gradient shear map
\(F_{m,s}=T\circ S\) attached to
\[
V_m=Aq_1^m q_2^2+B q_1 q_2^{2m},
\qquad
W_{m,s}=C p_1^{s(2m+1)+1}+D p_2^{sm+1}
\]
is a polynomial symplectomorphism. Starting from the standard seed
\((1,1)\), the actual degree vectors follow a strict period-two selector
itinerary across the common wall \(r=2\), with visible coordinate \(q_1\),
two-step monodromy \(P\), Perron growth
\(\lambda_1=s\,m(2m+1)\), exact wall-gap formulas, and the stride-two scalar
recurrence above.

The nonclaims that must remain frozen are correct:

- no theorem on the wall \(r=2\);
- no classification beyond this two-binomial / two-pure-power ansatz;
- no maximal fan or arbitrary-period automaton theorem;
- no positive-characteristic result;
- no inverse-degree, entropy-equality, integrability, genericity,
  periodic-point, or priority claim;
- the abstract period-\(k\) lemma is technique, not the public headline.

## 7. Scores

Required PASS thresholds: proof confidence \(\ge 9.0\), standalone value
\(\ge 7.5\).

- Proof confidence: **9.3 / 10**
  - all selector, carry, noncancellation, visibility, spectral, and boundary
    checks close exactly;
  - I found no unresolved theorem-critical gap.

- Standalone value: **7.8 / 10**
  - this is narrower than Papers 21--23 and close to Paper 20 in grammar,
    but the forced selector-exchange mechanism is still a distinct proof-first
    article if kept tightly framed.

Gate result from this review: **PASS**.

## 8. Blockers vs downstream fixes

### Theorem-critical blockers

None.

### Downstream fixes that are advisable but non-blocking

1. Define \(d_n\) explicitly as the total degree seen by \(q_1\); do not leave
   the observable coordinate implicit.
2. Present the arbitrary-coefficient corollary via top homogeneous parts in a
   domain, not by positivity language.
3. State clearly that the seed-based theorem is strict only because the seed is
   off the wall; the structural selector lemma with \(R=1\) does not give an
   analogous strict seed result.
4. Keep the public story on the period-two selector exchange and its monodromy;
   do not sell this as a general two-mode classification.
5. Keep the period-\(k\) lemma conditional and technical.

PAPER24_CANDIDATE_GATE_PASS_R2
