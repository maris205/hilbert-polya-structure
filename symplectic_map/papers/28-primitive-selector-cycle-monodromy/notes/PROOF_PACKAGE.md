# Paper 28 proof package

## Proof contract and notation

This package proves the exact V4 theorem.  It keeps separate:

- the general equal-total selector classification;
- the first strict-carry gate required by the actual polynomial lift;
- the incidence realization of an arbitrary primitive pair word;
- least selector period versus least quotient period;
- vector, support-pair, and literal-label decoder outputs; and
- position, coordinate, phase-subsequence, and complete-state recurrence
  domains.

Write \(\mathsf w\) for the selector word, \(u_n\) for the position
weighted-degree vector, and \(m_n\) for the momentum weighted-degree vector.
This avoids using the same symbol for the word and a momentum state.

No proof below uses a numerical experiment, computer algebra system, matrix
package, generic-coefficient sample, finite parameter search, or empirical
fit.

## Weighted-degree facts used

For a positive weight vector, the weighted degree of a monomial is its
exponent dot product.  The leading form is the sum of terms of maximal
weighted degree.  We use only:

1. \(\deg(fg)=\deg f+\deg g\) for nonzero polynomials over a domain;
2. a unique maximal support monomial cannot cancel against another support
   monomial;
3. the larger term in a strict degree comparison survives addition; and
4. products of nonzero leading forms remain nonzero in a polynomial ring
   over a field.

Every displayed support coordinate is at least two, so the selected monomial
appears in every gradient row.

## P1. Polynomial symplecticity and inverse

Let

\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p).
\]

Their Jacobians are

\[
 DS_V=\begin{pmatrix}I&0\\ \operatorname{Hess}V&I\end{pmatrix},
 \qquad
 DT_W=\begin{pmatrix}I&\operatorname{Hess}W\\0&I\end{pmatrix}.
\]

The Hessian blocks are symmetric, so these matrices preserve

\[
 J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

Equivalently, the additional \(dq_i\wedge dq_j\) and
\(dp_i\wedge dp_j\) terms cancel pairwise.  A simultaneous permutation

\[
 \Pi_P(q,p)=(Pq,Pp)
\]

is symplectic because \(P^{\mathsf T}P=I\).  Therefore

\[
 F=\Pi_P\circ T_W\circ S_V
\]

is a polynomial symplectomorphism.  Its inverse is

\[
 F^{-1}=S_V^{-1}\circ T_W^{-1}\circ\Pi_{P^{-1}}.
\]

For an output \((Q,\mathsf P)\), put
\(\bar q=P^{-1}Q\), \(\bar p=P^{-1}\mathsf P\).  Then

\[
 F^{-1}(Q,\mathsf P)=
 \left(
 \bar q-\nabla W(\bar p),
 \bar p-\nabla V(\bar q-\nabla W(\bar p))
 \right).
\]

This fixes the inverse phase order literally.

## P2. Selected gradient matrices

Suppose \(\alpha\) is the unique maximizer of
\(\gamma^{\mathsf T}u\) over the collected V support.  In gradient row i,

\[
 \deg_u(\partial_iq^\alpha)=\alpha^{\mathsf T}u-u_i.
\]

Since \(\alpha_i\ge2\), the derivative coefficient is nonzero in
characteristic zero.  Thus the selected gradient degree vector is

\[
 A_\alpha u,\qquad A_\alpha=\mathbf1\alpha^{\mathsf T}-I.
\]

Likewise a uniquely selected W exponent \(\beta\) gives

\[
 B_\beta v,\qquad B_\beta=\mathbf1\beta^{\mathsf T}-I.
\]

If all V totals are A and all W totals are B, literal multiplication gives

\[
\begin{aligned}
 B_\beta A_\alpha
 &= (\mathbf1\beta^{\mathsf T}-I)
    (\mathbf1\alpha^{\mathsf T}-I)\\
 &=I+\mathbf1\bigl((B-1)\alpha-\beta\bigr)^{\mathsf T}.
\end{aligned}
\]

Define

\[
 c_{\alpha,\beta}=(B-1)\alpha-\beta,
 \qquad \lambda=(A-1)(B-1).
\]

Then

\[
 c_{\alpha,\beta}^{\mathsf T}\mathbf1
 =(B-1)A-B=\lambda-1.
\]

Because the permutation acts last and \(P\mathbf1=\mathbf1\), the complete
selected position-degree matrix is

\[
 PB_\beta A_\alpha=P+\mathbf1c_{\alpha,\beta}^{\mathsf T}.
\]

## P3. Strict growth requires r at least two

For \(u>0\), \(r\ge2\), and
\(\alpha\in\mathbb Z_{\ge2}^{,r}\),

\[
\begin{aligned}
 (A_\alpha u)_i-u_i
 &=\alpha^{\mathsf T}u-2u_i\\
 &=(\alpha_i-2)u_i+\sum_{k\ne i}\alpha_ku_k>0.
\end{aligned}
\]

Hence \(A_\alpha u>u\) coordinatewise.  The same calculation gives
\(B_\beta v>v\).  The restriction \(r\ge2\) is essential, not a genericity
convention.  The headline construction has \(r=\ell+1\ge4\).

## P4. Exact strict-carry lift

Assume \(\alpha_0\) is the phase-zero V selector and impose

\[
 0<m_0<A_{\alpha_0}u_0
\]

coordinatewise.  Put \(v_0=A_{\alpha_0}u_0\).  The gradient term strictly
dominates the carried momentum coordinates, so the actual intermediate
momentum degree is \(v_0\).  If \(\beta_0\) is the strict W selector, P3 gives

\[
 B_{\beta_0}v_0>v_0>u_0.
\]

Thus the target gradient strictly dominates the carried position term.  After
permutation,

\[
 m_1=Pv_0,\qquad u_1=PB_{\beta_0}v_0,qquad u_1>m_1.
\]

Inductively, if \(u_n>m_n\), then

\[
 A_{\alpha_n}u_n>u_n>m_n
\]

and

\[
 B_{\beta_n}A_{\alpha_n}u_n>A_{\alpha_n}u_n>u_n.
\]

Permutation preserves these inequalities.  Therefore, for every \(n\ge0\),

\[
 m_{n+1}=PA_{\alpha_n}u_n,
\]

\[
 u_{n+1}=PB_{\beta_n}A_{\alpha_n}u_n
 =Pu_n+\mathbf1c_{\alpha_n,\beta_n}^{\mathsf T}u_n.
\]

The phase-zero inequality is necessary and sufficient for the strict source
carry used by this lift.  The smaller chamber \(0<m_0\le u_0\) is sufficient
by P3, but not necessary.

## P5. Coefficient-uniform leading-form survival

At every phase, strict selector inequalities choose one support exponent.
Every exponent coordinate is positive and the field has characteristic zero,
so its derivative scalar in every row is nonzero.  After substitution, the
leading form of a selected derivative monomial is a product of nonzero
coordinate leading forms and is nonzero in the polynomial domain.  No other
support exponent has the same degree, and the carried coordinate has strictly
smaller degree by P4.

Induction therefore proves that the selected matrices are the actual
polynomial weighted-degree matrices for every coefficient tuple in

\[
 (\Bbbk^*)^{|E_V|+|E_W|}.
\]

There is no generic-coefficient, sign, or hidden noncancellation certificate.

## P6. Residual decomposition and normal-fan iff

Let

\[
 C_n=P+\mathbf1c_n^{\mathsf T}.
\]

If \(u_n=x_n+t_n\mathbf1\), with \(x_n=P^nu_0\), then

\[
 C_nu_n=Px_n+
 \bigl(c_n^{\mathsf T}x_n+\lambda t_n\bigr)\mathbf1.
\]

Thus the residual part is always \(x_{n+1}=Px_n=P^{n+1}u_0\).  For equal-
total V exponents,

\[
 (\alpha-\gamma)^{\mathsf T}u_n
 =(\alpha-\gamma)^{\mathsf T}x_n,
\]

so V chooses the unique maximizer of \(\alpha^{\mathsf T}x_n\).  After V
selects \(\alpha_n\),

\[
 A_{\alpha_n}u_n=
 \bigl(\alpha_n^{\mathsf T}x_n+(A-1)t_n\bigr)\mathbf1-x_n.
\]

For equal-total W exponents \(\beta,\eta\),

\[
 (\beta-\eta)^{\mathsf T}A_{\alpha_n}u_n
 =-(\beta-\eta)^{\mathsf T}x_n.
\]

Thus maximizing the actual W score is equivalent to minimizing
\(\beta^{\mathsf T}x_n\); this proves the W-minimizer sign.

Define

\[
 \mathcal N_V^+(\alpha)=
 \{x>0:(\alpha-\gamma)^{\mathsf T}x>0\ \forall\gamma\ne\alpha\},
\]

\[
 \mathcal N_W^-(\beta)=
 \{x>0:(\eta-\beta)^{\mathsf T}x>0\ \forall\eta\ne\beta\}.
\]

For a declared length-\(\ell\) residual return, the strict selector cocycle
has rooted exponent word \(((\alpha_0,\beta_0),\ldots,
(\alpha_{\ell-1},\beta_{\ell-1}))\) iff

\[
 u_0\in\mathcal C_{\mathsf w}
 =\mathbb R_{>0}^{,r}\cap
 \bigcap_{j=0}^{\ell-1}P^{-j}
 \bigl(\mathcal N_V^+(\alpha_j)\cap
       \mathcal N_W^-(\beta_j)\bigr).
\]

The cone is rational, homogeneous, open, and polyhedral.  If nonempty, it
contains a rational point; positive scaling gives a positive integer seed.

For the actual polynomial orbit, cone membership must be combined with P4's
first-carry gate.  These two statements are never compressed into one iff.
For a singleton support, the competitor family is empty, so its normal cone
is the full positive weight space and uniqueness is vacuous.

## P7. Incidence realization of every primitive pair word

Let

\[
 \mathsf w=((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1})),
 \qquad \ell\ge3,
\]

be rooted and primitive.  To avoid collision between a W label and the
baseline exponent, denote the latter by \(\rho\ge2\).  Put \(r=\ell+1\), let

\[
 I_{\mathrm{mov}}=\{0,\ldots,\ell-1\},
 \qquad I=I_{\mathrm{mov}}\sqcup\{\star\},
\]

and choose P so that

\[
 Pe_j=e_{j+1\pmod\ell},\qquad Pe_\star=e_\star.
\]

Choose \(H\ge2\), \(K\ge1\), and

\[
 u_0=\mathbf1+(H-1)e_0.
\]

For the used label sets define

\[
 S_a=\{j:a_j=a\},\qquad T_b=\{j:b_j=b\},
\]

\[
 \alpha_a=\rho\mathbf1+K\sum_{j\in S_a}e_j
 +K(\ell-|S_a|)e_\star,
\]

\[
 \beta_b=\rho\mathbf1+K\sum_{j\notin T_b}e_j
 +K|T_b|e_\star.
\]

Every coordinate is at least two.  The added K-mass of either kind of
exponent is \(K\ell\), so every total is

\[
 D=\rho r+K\ell.
\]

At phase j, \(x_j=P^ju_0\) has value H in moving coordinate j and value one
elsewhere.  Put

\[
 C_0=\rho(H+\ell)+K\ell,
 \qquad g=K(H-1)>0.
\]

Direct incidence counting gives

\[
 \alpha_a^{\mathsf T}x_j
 =C_0+g\mathbf1_{\{j\in S_a\}},
\]

\[
 \beta_b^{\mathsf T}x_j
 =C_0+g\mathbf1_{\{j\notin T_b\}}.
\]

Therefore \(\alpha_{a_j}\) is the unique V maximizer and \(\beta_{b_j}\) is
the unique W minimizer.  Every existing competitor is separated by exactly
g.  If a component alphabet is a singleton, selection on that side is unique
vacuously and no finite competitor margin is assigned.  The spike seed lies
in the required normal-fan cone.

Choose arbitrary nonzero coefficients and form

\[
 V_{\mathsf w}(q)=\sum_a\xi_aq^{\alpha_a},\qquad
 W_{\mathsf w}(p)=\sum_b\zeta_bp^{\beta_b},
\]

\[
 F_{\mathsf w}=\Pi_P\circ T_{W_{\mathsf w}}
 \circ S_{V_{\mathsf w}}.
\]

The canonical momentum seed \(m_0=\mathbf1\) satisfies

\[
 0<m_0\le u_0<A_{\alpha_{a_0}}u_0.
\]

P4--P6 then show that the actual polynomial weighted-degree selectors follow
the requested pair word indefinitely.  The map is assembled once from the
occurrence sets; no phase-dependent map or external schedule is used.  This
is one autonomous map per word, not one universal map.

## P8. Constant scalar forcing

For the explicit realization, write

\[
 c_j=(D-1)\alpha_{a_j}-\beta_{b_j},
 \qquad \lambda=(D-1)^2.
\]

The score table gives

\[
 c_j^{\mathsf T}x_j=(D-1)(C_0+g)-C_0=: \mu,
\]

independent of j.  Moreover

\[
 \mu=(D-2)C_0+(D-1)g>0.
\]

It follows that

\[
 u_n=P^nu_0+t_n\mathbf1,
 \qquad t_0=0,
 \qquad t_{n+1}=\lambda t_n+\mu,
\]

and

\[
 t_n=\mu\frac{\lambda^n-1}{\lambda-1}.
\]

The constant scalar forcing is deliberate and does not encode the selector
word.

## P9. Ordered prefixes and period monodromy

Put

\[
 C_j=P+\mathbf1c_j^{\mathsf T},
 \qquad Q_s=C_{s-1}\cdots C_0.
\]

We prove

\[
 Q_s=P^s+\mathbf1R_s^{\mathsf T},\qquad R_0=0.
\]

Indeed,

\[
\begin{aligned}
 Q_{s+1}
 &=(P+\mathbf1c_s^{\mathsf T})
   (P^s+\mathbf1R_s^{\mathsf T})\\
 &=P^{s+1}+\mathbf1
   \bigl(c_s^{\mathsf T}P^s+\lambda R_s^{\mathsf T}\bigr).
\end{aligned}
\]

Thus

\[
 R_{s+1}^{\mathsf T}=c_s^{\mathsf T}P^s+
 \lambda R_s^{\mathsf T},
\]

\[
 R_s^{\mathsf T}=\sum_{j=0}^{s-1}
 \lambda^{s-1-j}c_j^{\mathsf T}P^j,
 \qquad R_s^{\mathsf T}\mathbf1=\lambda^s-1.
\]

Since \(P^\ell=I\),

\[
 M_{\mathsf w}=Q_\ell=I+\mathbf1R_\ell^{\mathsf T}.
\]

The rank-one update acts by \(\lambda^\ell\) on \(\mathbf1\) and by one on
\(\ker R_\ell^{\mathsf T}\), hence

\[
 \chi_{M_{\mathsf w}}(z)=
 (z-1)^{r-1}(z-\lambda^\ell).
\]

For \(k\ge0\),

\[
 M_{\mathsf w}^k=I+
 \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 \mathbf1R_\ell^{\mathsf T}.
\]

Since \(Q_s\mathbf1=\lambda^s\mathbf1\), for \(0\le s<\ell\),

\[
 Q_sM_{\mathsf w}^ku_0=P^su_0+
 \left[
 R_s^{\mathsf T}u_0+
 \lambda^s\frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 R_\ell^{\mathsf T}u_0
 \right]\mathbf1.
\]

These are exact ordered formulas, not asymptotic spectral estimates.

## P10. Digit bounds and pair injectivity

Every coordinate of \(\alpha_a\) and \(\beta_b\) lies between \(\rho\) and
\(\rho+K\ell\).  Since

\[
 D-1-(\rho+K\ell)=\rho\ell-1>0,
\]

we have

\[
 (c_{a,b})_i\ge(D-1)\rho-(\rho+K\ell)>0.
\]

Also \((\alpha_a)_i<D-1\) and \((\beta_b)_i>0\), so

\[
 (c_{a,b})_i<(D-1)^2=\lambda.
\]

Thus every coordinate of every rotated vector
\(c_j^{\mathsf T}P^j\) is a valid base-\(\lambda\) digit and no coordinate
carry occurs.

Suppose \(c_{a,b}=c_{a',b'}\).  Then

\[
 (D-1)(\alpha_a-\alpha_{a'})=\beta_b-\beta_{b'}.
\]

If \(a\ne a'\), their nonempty disjoint occurrence sets have a moving
coordinate in their symmetric difference.  At that coordinate the left side
has magnitude \(K(D-1)\), while the right side has magnitude at most K, a
contradiction.  Hence \(a=a'\).  Then \(\beta_b=\beta_{b'}\), and distinct
used W labels have distinct nonempty occurrence sets, so \(b=b'\).  Therefore

\[
 (a,b)\longmapsto c_{a,b}
\]

is injective on the map-specific support dictionary.

## P11. Exact decoder ladder

From

\[
 M_{\mathsf w}-I=\mathbf1R_\ell^{\mathsf T}
\]

one reads \(R_\ell^{\mathsf T}\) as any row of the rank-one difference.
Given P, \(\lambda\), \(\ell\), and a marked phase zero, coordinatewise
base-\(\lambda\) expansion uniquely recovers, in order, the digits

\[
 c_j^{\mathsf T}P^j.
\]

Right multiplication by \(P^{-j}\) recovers every ordered \(c_j\).  The
decoder has three levels:

1. `vector level`: \(M_{\mathsf w},P,\lambda,\ell\) and the marked root
   recover \((c_0,\ldots,c_{\ell-1})\);
2. `support-pair level`: adding the unlabelled support dictionary of
   \(F_{\mathsf w}\) recovers the ordered exponent pairs; and
3. `literal-label level`: adding the labelled dictionary recovers the ordered
   label pairs.

If supports are known without literal names, labels are recovered only up to
independent bijective renaming of the two alphabets.  If phase zero is
unmarked, only the cyclic rotation class is intrinsic.  No equality of the
monodromy matrices for different roots is asserted.

## P12. Least selector and quotient periods

The selector word has least period \(\ell\) because it is the prescribed
primitive pair word.  Modulo the diagonal line

\[
 L=\mathbb R\mathbf1,
\]

we have \([C_ju]=[Pu]\), hence \([u_n]=[P^nu_0]\).  Suppose
\(0<d<\ell\) and

\[
 P^du_0-u_0=c\mathbf1.
\]

The star coordinate is fixed, so its difference is zero and therefore c=0.
But the unique H-spike has moved to a different moving coordinate, so
\(P^du_0\ne u_0\), a contradiction.  The quotient orbit has least period
\(\ell\).

These are two separate least-period statements.  Neither implies that the
polynomial state is periodic; \(t_n\) grows because \(\lambda>1\) and
\(\mu>0\).

## P13. Exact scalar and coordinate recurrence domains

By P8,

\[
 q_n:=\max_i(u_n)_i=H+t_n.
\]

Therefore

\[
 q_{n+2}-(1+\lambda)q_{n+1}+\lambda q_n=0
 \qquad(n\ge0),
\]

and also

\[
 q_{n+\ell+1}-\lambda q_{n+\ell}-q_{n+1}+\lambda q_n=0
 \qquad(n\ge0).
\]

For \(i\in I_{\mathrm{mov}}\), define

\[
 y_n^{(i)}=(u_n)_i
 =1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n,
\]

while the fixed coordinate is

\[
 y_n^{(\star)}=(u_n)_\star=1+t_n.
\]

There is no expression \(n\equiv\star\pmod\ell\).  For every \(i\in I\),

\[
 y_{n+\ell+1}^{(i)}-\lambda y_{n+\ell}^{(i)}
 -y_{n+1}^{(i)}+\lambda y_n^{(i)}=0
 \qquad(n\ge0).
\]

For \(i\in I\), \(s\in I_{\mathrm{mov}}\), and

\[
 z_m^{(i,s)}=y_{s+m\ell}^{(i)},
\]

we obtain

\[
 z_{m+2}^{(i,s)}-(1+\lambda^\ell)z_{m+1}^{(i,s)}
 +\lambda^\ell z_m^{(i,s)}=0
 \qquad(m\ge0).
\]

Define the complete-state maximum

\[
 d_n=\max\{\max_i(u_n)_i,\max_i(m_n)_i\}.
\]

P4 gives \(u_n>m_n\) only for \(n\ge1\), so \(d_n=q_n\) from that point and

\[
 d_{n+\ell+1}-\lambda d_{n+\ell}-d_{n+1}+\lambda d_n=0
 \qquad(n\ge1).
\]

At \(n=0\),

\[
 d_{\ell+1}-\lambda d_\ell-d_1+\lambda d_0
 =\lambda(d_0-q_0).
\]

Thus the initial instance holds iff

\[
 d_0=q_0
 \iff \max_i(m_0)_i\le\max_i(u_0)_i.
\]

Every recurrence above is an annihilator only.  No minimality or scalar word
decoding is inferred.

## Exact failure fixtures

### F1. Dimension-one cancellation

Over \(\mathbb Q\), take

\[
 V(q)=q^2,\qquad W(p)=-p^2/4.
\]

Then \(S_V(q,p)=(q,p+2q)\), and the next q-coordinate after W is

\[
 q-\frac{p+2q}{2}=-\frac p2.
\]

The q contribution cancels although the formal matrices are
\(A_2=B_2=[1]\).  Dimension one is therefore outside the coefficient-
uniform strict-lift theorem.

### F2. The complete-state recurrence cannot start unconditionally at zero

Take

\[
 \ell=3,\quad r=4,\quad \rho=2,\quad K=1,\quad H=2,
\]

\[
 u_0=(2,1,1,1),\qquad m_0=(10,10,10,10).
\]

For a phase-zero singleton V occurrence,

\[
 \alpha_{a_0}=(3,2,2,4),\qquad
 A_{\alpha_{a_0}}u_0=(12,13,13,13),
\]

so the strict first gate holds.  Nevertheless
\(q_0=2\), \(d_0=10\), \(\lambda=100\), and \(\mu=127\).  The forbidden
initial recurrence has residual

\[
 d_4-100d_3-d_1+100d_0=100(10-2)=800.
\]

### F3. Equality walls

If

\[
 (\alpha-\gamma)^{\mathsf T}P^ju_0=0
\]

or

\[
 (\beta-\eta)^{\mathsf T}P^ju_0=0,
\]

the selector is not unique.  No tie-breaking theorem is claimed.

### F4. Spike collapse and shorter quotient

When \(H=1\), the seed is diagonal, g=0, incidence scores tie, and the
quotient period collapses.  Replacing P by a permutation with a shorter
quotient orbit likewise shortens the phase geometry.

### F5. Unequal totals and missing support hypotheses

Unequal exponent totals reintroduce \(t_n\) into selector differences.
Zero support coordinates can delete gradient monomials; positive
characteristic can annihilate derivative scalars; and a zero displayed
coefficient changes the collected support.  Each lies outside the theorem.

### F6. Missing decoder data

Monodromy without the support dictionary does not determine arbitrary
alphabet names.  An unmarked period product has no intrinsic phase-zero
label.  The scalar forcing is identical for many different words.

## Retained planar obstruction

For a positive two-variable support and pure-power second shear, let

\[
 H(r)=\max_{(a,b)}(ar+b).
\]

On a chamber the projective map has the form

\[
 g(r)=\kappa\frac{(a-1)r+b}{ar+b-1},
\]

with

\[
 g'(r)=\kappa\frac{1-a-b}{(ar+b-1)^2}<0.
\]

It is continuous across Newton walls and decreasing.  Its square is
increasing, so it has no orbit of least period greater than two.  The present
construction genuinely uses the higher-dimensional finite-order residual
twist; it is not a disguised planar period-three extension.

## Proof dependency DAG

The logical dependencies are:

1. P1 is the independent map-level symplectic branch.
2. P2 feeds P3; P3 feeds P4; P4 feeds P5.
3. P2 also feeds P6; P6 feeds P7.
4. P4--P7 establish the arbitrary primitive-word actual-degree realization.
5. P7 and P6 feed P8; P2 and P8 feed P9.
6. P7 feeds the digit bounds and injectivity in P10.
7. P9 and P10 feed the decoder P11.
8. P6, spike geometry, and word primitivity feed the two periods in P12.
9. P8 and P4 feed every recurrence and starting index in P13.

No dependency originates in a literature miss, scientific run, or finite
fixture.

## Main-body placement and mass

| Proof block | Target pages |
|---|---:|
| P1--P2: map and selected matrices | 2.5 |
| P6: normal-fan iff | 3.0 |
| P7: arbitrary-word construction | 4.0 |
| P3--P5: carries and leading forms | 3.0 |
| P8--P11: cocycle, monodromy, decoder | 4.5 |
| P12--P13: periods and recurrences | 2.5 |
| Failure fixtures and boundaries | 2.0 |

Together with introduction, bounded positioning, abstract, and conclusion,
this supports 25.5--26.0 anonymous content pages.  Every theorem-critical
argument belongs in the main body; no proof appendix or computation
supplement is needed.

## Locked anti-claims

The package proves no universal map, fixed dimension, ordinary total-degree
selector theorem, periodic polynomial state, scalar word decoder, minimal
recurrence, entropy or dynamical-degree equality, integrability, generic
nonconjugacy, cohomological spectrum, reciprocity, zero-coordinate
cancellation classification, positive-characteristic extension, or absolute
literature priority.

BATCH07_PAPER28_PROOF_PACKAGE_FROZEN

## Controlling append-only typography and page-mass correction

Authority: `B07-E0174-P28-SOURCE-DESIGN-REVIEW-FAIL-CORRECTION-AUTHORIZATION`.
This packet changes no theorem, hypothesis, proof step, recurrence, fixture,
or anti-claim.  It supersedes only two malformed superscripts and one page-
mass range.

The exact domain in P3 is

\[
 \alpha\in\mathbb Z_{\ge2}^{r}.
\]

The exact positive cone in P6 is

\[
 \mathcal C_{\mathsf w}\subset\mathbb R_{>0}^{r}.
\]

The malformed historical renderings with exponent `,r` carry no authority.

The proof blocks in this package total 21.5 pages.  Adding the exact 5.0-page
allocation for abstract, introduction/positioning, limitations, and
conclusion frozen in `FINAL_PROPOSAL.md` gives the controlling anonymous
content mass

\[
 21.5+5.0=26.5\ \text{pages}.
\]

The earlier 25.5--26.0 range in this file is superseded.  The distinct 25.5
and 26.0 candidate-review estimates remain historical reviewer estimates and
are not changed.

BATCH07_PAPER28_PROOF_PACKAGE_CORRECTION_FROZEN

## Controlling second page-mass reconciliation

Authority:
`B07-E0177-P28-CORRECTED-SOURCE-DESIGN-REVIEW-FAIL-MASS-CORRECTION-AUTHORIZATION`.
All earlier bytes and markers remain historical.  This packet supersedes only
the first correction packet's erroneous claim that `FINAL_PROPOSAL.md`
contains an exact 5.0-page peripheral allocation.

The controlling page arithmetic is taken entirely from the final proposal's
single section table.  Its six mathematical core entries are

\[
 3.0+4.0+4.0+3.5+4.0+3.5=22.0,
\]

for the symplectic family/degree transport, normal-fan iff, incidence
realization, carries/leading forms, monodromy/decoding, and least-period/
recurrence/boundary sections.  Its three peripheral entries are

\[
 0.5+2.5+1.5=4.5,
\]

for the abstract, introduction/bounded positioning, and limitations/
conclusion.  Hence the exact anonymous total is

\[
 22.0+4.5=26.5\ \text{pages}.
\]

The 21.5-page table earlier in this proof package is a distinct approximate
proof-placement subtotal with different grouping conventions.  It remains a
useful internal allocation, but it is not an addend in the controlling final-
proposal arithmetic and must not be combined with the 4.5-page peripheral
subtotal.  No theorem, proof, citation, mapping, or manuscript claim changes.

BATCH07_PAPER28_PROOF_PACKAGE_MASS_RECONCILIATION_FROZEN
