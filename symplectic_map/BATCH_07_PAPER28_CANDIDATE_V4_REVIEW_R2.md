# Batch 07 Paper 28 candidate V4 formal review R2

review_outcome: PASS
review_role: fresh independent Batch07 Paper28 candidate V4 formal R2
candidate_id: primitive_selector_cycle_monodromy_v1
candidate_version_reviewed: V4, complete append-only candidate
consumed_authority: B07-E0169-P28-CANDIDATE-V4-AUTHOR-STOP-DUAL-REVIEW-AUTHORIZATION
controlling_gate: BATCH07_PAPER28_CANDIDATE_V4_DUAL_REVIEW_AUTHORIZED
paper_number_consumed: false
project_path: absent
scientific_execution: none
external_effect: none

## Independence, blindness, and restricted boundary

I am a new formal R2 reviewer.  I did not participate in candidate design,
V1--V3 review or correction, the manifest/action-history recovery, Paper 27,
or V4 R1.  I remained blind to V4 R1 and did not read, receive, cite, or infer
its reasoning or verdict.  I used no web access and no external reviewer.

The workspace evidence boundary consisted of exactly these four authorized
existing files: `BATCH_07_IDEA_REPORT.md`, `BATCH_07_STATUS.md`,
`BATCH_07_CHARTER_REVIEW.md`, and
`BATCH_07_PAPER28_V2_PRE_REVIEW_MANIFEST_ACTION_REVIEW.md`.  I performed no
listing, filename search, glob, wildcard expansion, recursion, symlink
traversal, absent/future-path test, project/build probe, historical ENOENT
retry, compiler or cache action, code or CAS computation, scientific run,
mutation, cleanup, message, upload, release, or other external effect.  The
derivations below are manual.  This PASS report is my sole authorized write.

## Exact authority and candidate binding

The complete candidate is a regular mode-`0644`, link-one file of 53,207
bytes and 1,350 LF, with SHA-256
`312e28bd2f8f3b5bed9fe26a17fa7150500d52079e4d61e64b8b513d7e094bc4`.
Its controlling terminal line is
`BATCH07_PAPER28_CANDIDATE_V4_AUTHOR_STOP`.  These values exactly match
B07-E0169.  The current status ledger measured 551,758 bytes and 9,634 LF,
mode `0644`, link one, with SHA-256
`1b40c3cbc736a48aa5a4f8c7db816c490bfeb44bb3b0ef2213d0e5a721e32021`,
and ends in the exact authorization line
`BATCH07_PAPER28_CANDIDATE_V4_DUAL_REVIEW_AUTHORIZED`.

B07-E0169 is event sequence 166.  It binds the self-excluding prospective
source/control boundary to 48 rows, 7,020 framing bytes, 48 LF, and SHA-256
`c564ef87723d68aa186e3135d31aae330eac1125fa85547208ad399f9b507983`.
It authorizes only the two named V4 PASS paths, requires new mutually blind
reviewers, leaves Paper 28 unconsumed and its project absent, and authorizes no
source, build, release, execution, or external effect.

The charter review is 20,209 bytes / 364 LF / mode `0644` / link one / SHA-256
`4ced8ab1e1b48d89ec088be40206bf3bbff3e23c77471c45672442883b322f73`.
The prospective recovery review is 18,669 bytes / 271 LF / mode `0644` / link
one / SHA-256
`b158aaea9b8b413e7ef4f872b26352368a695dde1d4ff5c3691fa619478f2902`
and ends in
`BATCH07_PAPER28_V2_PRE_REVIEW_MANIFEST_ACTION_HISTORY_REVIEW_PASS`.
I preserve its strictly prospective conclusion: it does not retroactively
validate or erase the disclosed manifest discontinuity, future-glob action,
or two historical ENOENT attempts.

## 1. Maps, inverse, and symplecticity

Let the coefficient field \(\Bbbk\) have characteristic zero, let
\(q,p\in\Bbbk^r\), and use
\(\omega=\sum_i dq_i\wedge dp_i\).  For

\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),
\]

their Jacobians are

\[
 DS_V=\begin{pmatrix}I&0\\ \operatorname{Hess}V&I\end{pmatrix},
 \qquad
 DT_W=\begin{pmatrix}I&\operatorname{Hess}W\\0&I\end{pmatrix}.
\]

The Hessian blocks are symmetric, so direct multiplication against
\(J=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)\) gives
\((DS_V)^T JDS_V=J\) and \((DT_W)^T JDT_W=J\).  Equivalently, the extra
\(dq_i\wedge dq_j\) and \(dp_i\wedge dp_j\) terms cancel pairwise.  A
permutation matrix satisfies \(P^TP=I\), hence
\(\Pi_P(q,p)=(Pq,Pp)\) is also symplectic.  Therefore

\[
 F=\Pi_P\circ T_W\circ S_V
\]

is a polynomial symplectomorphism.

The inverse order is literal, not inferred from degree matrices:

\[
 F^{-1}=S_V^{-1}\circ T_W^{-1}\circ\Pi_{P^{-1}},
\]

where \(S_V^{-1}(q,p)=(q,p-\nabla V(q))\) and
\(T_W^{-1}(q,p)=(q-\nabla W(p),p)\).  Thus, for output coordinates
\((Q,\mathsf P)\), putting \(\bar q=P^{-1}Q\) and
\(\bar p=P^{-1}\mathsf P\) gives

\[
 F^{-1}(Q,\mathsf P)=
 \bigl(\bar q-\nabla W(\bar p),
 \bar p-\nabla V(\bar q-\nabla W(\bar p))\bigr).
\]

## 2. Literal gradient matrices and their order

Give the current position and momentum coordinates positive weighted-degree
vectors \(u\) and \(w\).  If \(\alpha\) is the unique selected exponent of
\(V\), every row of \(\nabla(q^\alpha)\) has degree
\(\alpha^Tu-u_i\), because every \(\alpha_i\ge2\).  Hence

\[
 A_\alpha=\mathbf1\alpha^T-I,
 \qquad v=A_\alpha u.
\]

After the first shear, a uniquely selected \(\beta\) in \(W\) similarly
gives \(B_\beta=\mathbf1\beta^T-I\).  If the common totals are
\(\alpha^T\mathbf1=A\) and \(\beta^T\mathbf1=B\), then

\[
\begin{aligned}
 B_\beta A_\alpha
 &= (\mathbf1\beta^T-I)(\mathbf1\alpha^T-I)\\
 &= I+\mathbf1\bigl((B-1)\alpha-\beta\bigr)^T.
\end{aligned}
\]

Define

\[
 c_{\alpha,\beta}=(B-1)\alpha-\beta,
 \qquad \lambda=(A-1)(B-1).
\]

Then

\[
 c_{\alpha,\beta}^T\mathbf1
 =(B-1)A-B=\lambda-1.
\]

The permutation acts last.  Since \(P\mathbf1=\mathbf1\), the complete
position-degree matrix is exactly

\[
 C_{\alpha,\beta}=PB_\beta A_\alpha
 =P+\mathbf1c_{\alpha,\beta}^T,
\]

not a reversed product.  The simultaneous momentum degree after a complete
step is \(PA_\alpha u\).

## 3. Max/min sign and the normal-fan iff

For an exact selected orbit write

\[
 u_n=x_n+t_n\mathbf1,\qquad x_n=P^nu_0.
\]

This decomposition follows inductively because

\[
 C_n(x+t\mathbf1)
 =Px+\bigl(\lambda t+c_n^Tx\bigr)\mathbf1.
\]

Equal V totals imply

\[
 (\alpha-\gamma)^Tu_n=(\alpha-\gamma)^Tx_n,
\]

so the V selector is the unique maximizer of \(\alpha^Tx_n\).  Once
\(\alpha_n\) is selected,

\[
 v_n=A_{\alpha_n}u_n
 =\bigl(\alpha_n^Tx_n+(A-1)t_n\bigr)\mathbf1-x_n.
\]

For equal-total W exponents \(\beta,\eta\),

\[
 (\beta-\eta)^Tv_n=-(\beta-\eta)^Tx_n.
\]

Thus maximizing the actual W score \(\beta^Tv_n\) is exactly minimizing
\(\beta^Tx_n\).  This verifies the candidate's V-max/W-min sign.

Consequently

\[
 \mathcal N_V^+(\alpha)
 =\{x>0:(\alpha-\gamma)^Tx>0\ \forall\gamma\ne\alpha\},
\]

\[
 \mathcal N_W^-(\beta)
 =\{x>0:(\eta-\beta)^Tx>0\ \forall\eta\ne\beta\}
\]

are exactly, respectively, the strict V-max and W-min regions.  At phase
\(j\), selection of \((\alpha_j,\beta_j)\) is equivalent to
\(P^ju_0\) lying in their intersection.  Therefore, assuming the declared
quotient return,

\[
 \mathcal C_{\mathsf w}
 =\mathbb R_{>0}^r\cap\bigcap_{j=0}^{\ell-1}
 P^{-j}\bigl(\mathcal N_V^+(\alpha_j)
 \cap\mathcal N_W^-(\beta_j)\bigr)
\]

is necessary and sufficient for the rooted strict selector word.  The
inequalities are homogeneous and rational; a nonempty cone contains a
rational point and hence, after positive scaling, a positive integer seed.
Word primitivity, the first-carry gate, and quotient phase separation are
correctly kept as separate conditions.

If a support is a singleton, the universal family of competitor inequalities
is empty, so its strict normal cone is the entire permitted positive weight
space \(\mathbb R_{>0}^r\).  This is consistent with both directions of the
iff and introduces no artificial second label.

## 4. Incidence realization, repeated labels, and singleton margins

Let \(\ell\ge3\), \(r=\ell+1\), and let
\(P e_j=e_{j+1\bmod\ell}\) while \(Pe_\star=e_\star\).  Take

\[
 u_0=\mathbf1+(H-1)e_0,
 \qquad H\ge2,\quad b_0\ge2,\quad K\ge1.
\]

For the distinct labels actually used in the word, the occurrence sets
\(S_a=\{j:a_j=a\}\) and \(T_{\mathfrak b}=\{j:b_j=\mathfrak b\}\)
are nonempty; sets belonging to distinct labels are disjoint.  The exponents
are

\[
 \alpha_a=b_0\mathbf1+K\sum_{j\in S_a}e_j
 +K(\ell-|S_a|)e_\star,
\]

\[
 \beta_{\mathfrak b}=b_0\mathbf1
 +K\sum_{j\notin T_{\mathfrak b}}e_j
 +K|T_{\mathfrak b}|e_\star.
\]

Every coordinate is at least two and both totals are

\[
 D=b_0r+K\ell,qquad \lambda=(D-1)^2.
\]

At phase \(j\), \(x_j=P^ju_0\) has value \(H\) at moving coordinate
\(j\) and value one elsewhere.  With

\[
 C_0=b_0(H+\ell)+K\ell,qquad g=K(H-1)>0,
\]

direct incidence counting gives

\[
 \alpha_a^Tx_j=C_0+K(H-1)\mathbf1_{\{j\in S_a\}},
\]

\[
 \beta_{\mathfrak b}^Tx_j
 =C_0+K(H-1)\mathbf1_{\{j\notin T_{\mathfrak b}\}}.
\]

Thus \(\alpha_{a_j}\) uniquely maximizes the V score and
\(\beta_{b_j}\) uniquely minimizes the residual W score.  Repeated labels
cause no collision: the same incidence support is correctly selected at each
of its occurrence phases, while every other used label has the opposite
incidence at that phase.  Against each actually existing competitor the
score difference is exactly \(g\).

If the V alphabet is a singleton, its sole exponent is the unique maximizer
vacuously and there is no finite V competitor gap; likewise for a singleton
W alphabet.  An extended-real best-competitor margin may be \(+\infty\), but
it is not identified with \(g\).  A primitive pair word can have one
singleton component because the other component can carry period \(\ell\).
Both components cannot be singleton for a primitive word of length
\(\ell\ge3\).  This closes the singleton quantifier without changing any
matrix or carry proof.

## 5. Exact first gate, later carries, and coefficient-uniform survival

For \(r\ge2\), positive \(u\), and \(\alpha_i\ge2\),

\[
 (A_\alpha u)_i-u_i
 =(\alpha_i-2)u_i+\sum_{k\ne i}\alpha_ku_k>0.
\]

The same calculation gives \(B_\beta v>v\).  The explicit construction has
\(r=\ell+1\ge4\), so it is inside this range.

Fix the phase-zero V selector and put \(v_0=A_{\alpha_{a_0}}u_0\).  The exact
strict source-carry condition is the coordinatewise gate

\[
 0<w_0<v_0.
\]

It is necessary and sufficient for the strict domination used by this lift.
The smaller chamber \(0<w_0\le u_0\) is sufficient because
\(A_\alpha u_0>u_0\), but is not necessary.  Under the exact gate,

\[
 w_1=Pv_0,qquad u_1=PB_{\beta_{b_0}}v_0,qquad u_1>w_1.
\]

If \(u_n>w_n\) for \(n\ge1\), then

\[
 A_{\alpha_{a_n}}u_n>u_n>w_n
\]

and

\[
 PB_{\beta_{b_n}}A_{\alpha_{a_n}}u_n
 >PA_{\alpha_{a_n}}u_n.
\]

This proves every later source and target carry by induction and yields the
exact degree recurrence

\[
 u_{n+1}=Pu_n+(c_{a_n,b_n}^Tu_n)\mathbf1,
 \qquad w_{n+1}=PA_{\alpha_{a_n}}u_n.
\]

The actual polynomial-degree statement is coefficient-uniform.  Strict
selector inequalities leave one highest-weight support monomial in every
gradient row.  Every derivative scalar is nonzero in characteristic zero
because every support coordinate is positive.  The leading form of a product
of nonzero coordinate leading forms is nonzero in the polynomial domain.
All carried terms have strictly smaller degree.  Hence no two top terms can
cancel, and the result holds for every coefficient tuple in
\((\Bbbk^*)^{|E_V|+|E_W|}\), with no genericity certificate.

For the incidence realization,

\[
 c_{a_j,b_j}^Tx_j=(D-1)(C_0+g)-C_0=:\mu>0.
\]

Since \(c_j^T\mathbf1=\lambda-1\), the decomposition is exact with

\[
 t_0=0,qquad t_{n+1}=\lambda t_n+\mu,qquad
 u_n=P^nu_0+t_n\mathbf1.
\]

The forcing is constant; the word is carried by the phase-resolved matrices,
not by distinct scalar growth curves.

## 6. Prefix products, monodromy, spectrum, and powers

Put \(c_j=c_{a_j,b_j}\), \(C_j=P+\mathbf1c_j^T\), and for
\(s\ge0\),

\[
 Q_s=C_{s-1}\cdots C_0.
\]

Writing \(Q_s=P^s+\mathbf1R_s^T\), with \(R_0=0\), literal left
multiplication gives

\[
\begin{aligned}
 Q_{s+1}
 &=(P+\mathbf1c_s^T)(P^s+\mathbf1R_s^T)\\
 &=P^{s+1}+\mathbf1
 \bigl(c_s^TP^s+\lambda R_s^T\bigr),
\end{aligned}
\]

because \(P\mathbf1=\mathbf1\) and
\(1+c_s^T\mathbf1=\lambda\).  Therefore

\[
 R_s^T=\sum_{j=0}^{s-1}\lambda^{s-1-j}c_j^TP^j,
 \qquad R_s^T\mathbf1=\lambda^s-1.
\]

As \(P^\ell=I\), the ordered period monodromy is

\[
 M_{\mathsf w}=Q_\ell=I+\mathbf1R_\ell^T,
\]

\[
 R_\ell^T=\sum_{j=0}^{\ell-1}
 \lambda^{\ell-1-j}c_j^TP^j,qquad
 R_\ell^T\mathbf1=\lambda^\ell-1.
\]

The rank-one update acts by \(\lambda^\ell\) on \(\mathbf1\) and by one on
the \((r-1)\)-dimensional kernel of \(R_\ell^T\).  Hence

\[
 \chi_{M_{\mathsf w}}(z)
 =(z-1)^{r-1}(z-\lambda^\ell).
\]

For every integer \(k\ge0\),

\[
 M_{\mathsf w}^k=I+
 \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 \mathbf1R_\ell^T.
\]

Since \(Q_s\mathbf1=\lambda^s\mathbf1\), for
\(0\le s<\ell\) and \(k\ge0\),

\[
 Q_sM_{\mathsf w}^ku_0=P^su_0+
 \left[R_s^Tu_0+\lambda^s
 \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 R_\ell^Tu_0\right]\mathbf1.
\]

These are exact prefix and phase formulas, rather than asymptotic spectral
statements.

## 7. Digit bounds, injectivity, and decoder side information

Every coordinate satisfies

\[
 b_0\le(\alpha_a)_i,(\beta_{\mathfrak b})_i\le b_0+K\ell.
\]

Moreover

\[
 D-1-(b_0+K\ell)=b_0\ell-1>0.
\]

Thus, coordinatewise,

\[
 (c_{a,\mathfrak b})_i
 \ge (D-1)b_0-(b_0+K\ell)>0,
\]

while \((\alpha_a)_i<D-1\) and \((\beta_{\mathfrak b})_i>0\) give

\[
 (c_{a,\mathfrak b})_i<(D-1)^2=\lambda.
\]

Hence every rotated \(c_j^TP^j\) is an ordinary base-\(\lambda\) digit
vector with no coordinate carry.

The pair map is injective.  If

\[
 (D-1)(\alpha_a-\alpha_{a'})
 =\beta_{\mathfrak b}-\beta_{\mathfrak b'},
\]

and \(a\ne a'\), a moving coordinate in the nonempty symmetric difference
of the disjoint occurrence sets has left magnitude \(K(D-1)\), whereas the
right magnitude is at most \(K\), impossible.  Hence \(a=a'\).  Then the
right side is zero, and distinct nonempty disjoint W occurrence sets likewise
force \(\mathfrak b=\mathfrak b'\).

From \(M_{\mathsf w}\), one reads \(R_\ell^T\) as any row of
\(M_{\mathsf w}-I\).  Given \(P,\lambda,\ell\), and a marked phase zero,
coordinatewise base-\(\lambda\) expansion uniquely recovers the ordered
digits \(c_j^TP^j\), and multiplication by \(P^{-j}\) recovers every
ordered \(c_j\).  Given additionally the labelled support dictionary, or the
injective table \((a,\mathfrak b)\mapsto c_{a,\mathfrak b}\), this recovers
the literal rooted label-pair word.  With unlabelled supports, it recovers the
rooted support-pair word, equivalently labels only up to independent bijective
renaming.  Without a marked phase, only the cyclic rotation class is
intrinsic.  No scalar-sequence decoder and no equality of rotated monodromy
matrices is claimed.

## 8. Primitive selector and quotient periods

Let \(L=\mathbb R\mathbf1\).  Since

\[
 [C_ju]=[Pu]\quad\text{in }\mathbb R^r/L,
\]

the quotient orbit is \([u_n]=[P^nu_0]\).  Suppose
\(0<d<\ell\) and \(P^du_0-u_0=c\mathbf1\).  The fixed star coordinate has
zero difference, so \(c=0\).  The unique \(H\)-spike has moved, so
\(P^du_0\ne u_0\), a contradiction.  The quotient orbit therefore has least
period \(\ell\).

The exact selector sequence is the prescribed primitive pair word, so its
least selector period is also \(\ell\).  For \(0<d<\ell\), the induced
quotient action of \(P^d\) is not the identity; hence no shorter prefix is a
period monodromy.  These statements do not assert a periodic polynomial state:
the diagonal component grows because \(\lambda>1\) and \(\mu>0\).

## 9. Coordinate and scalar recurrence audit

The affine recurrence has the closed form

\[
 t_n=\mu\frac{\lambda^n-1}{\lambda-1}.
\]

The position maximum is

\[
 q_n=\max_i(u_n)_i=H+t_n,
\]

and therefore, for \(n\ge0\),

\[
 q_{n+2}-(1+\lambda)q_{n+1}+\lambda q_n=0
\]

and

\[
 q_{n+\ell+1}-\lambda q_{n+\ell}-q_{n+1}+\lambda q_n=0.
\]

For moving coordinates \(i\in I_{\rm mov}=\{0,\ldots,\ell-1\}\), and only
for those indices,

\[
 y_n^{(i)}=(u_n)_i
 =1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n.
\]

The fixed coordinate is separately

\[
 y_n^{(\star)}=(u_n)_\star=1+t_n.
\]

There is no expression \(n\equiv\star\pmod\ell\).  A periodic term plus a
constant and a \(\lambda^n\) term is annihilated by
\((E^\ell-1)(E-\lambda)\), so for every named coordinate
\(i\in I_{\rm mov}\sqcup\{\star\}\),

\[
 y_{n+\ell+1}^{(i)}-\lambda y_{n+\ell}^{(i)}
 -y_{n+1}^{(i)}+\lambda y_n^{(i)}=0\qquad(n\ge0).
\]

For fixed \(i\in I\), \(s\in I_{\rm mov}\), and
\(z_m^{(i,s)}=y_{s+m\ell}^{(i)}\), the periodic indicator is constant in
\(m\) and the exponential ratio is \(\lambda^\ell\).  Thus

\[
 z_{m+2}^{(i,s)}-(1+\lambda^\ell)z_{m+1}^{(i,s)}
 +\lambda^\ell z_m^{(i,s)}=0\qquad(m\ge0).
\]

This scalar \(z\) notation is distinct from the residual vector
\(x_n=P^nu_0\).

For the complete-state maximum

\[
 d_n=\max\{\max_i(u_n)_i,\max_i(w_n)_i\},
\]

the carry induction gives \(u_n>w_n\) only for \(n\ge1\).  Hence
\(d_n=q_n\) for \(n\ge1\), and

\[
 d_{n+\ell+1}-\lambda d_{n+\ell}-d_{n+1}+\lambda d_n=0
 \qquad(n\ge1).
\]

At \(n=0\), all terms except \(d_0\) equal their q counterparts, so the
exact defect is

\[
 d_{\ell+1}-\lambda d_\ell-d_1+\lambda d_0
 =\lambda(d_0-q_0).
\]

Therefore the \(n=0\) instance holds if and only if

\[
 d_0=q_0
 \iff \max_i(w_0)_i\le\max_i(u_0)_i.
\]

For \(\ell=3,r=4,b_0=2,K=1,H=2\), with
\(u_0=(2,1,1,1)\) and \(w_0=(10,10,10,10)\), one has
\(A_{\alpha_{a_0}}u_0=(12,13,13,13)\), so the strict first gate holds,
but \(d_0=10\ne q_0=2\).  Here \(\lambda=100\), \(\mu=127\), and the
forbidden initial recurrence has exact residual

\[
 d_4-100d_3-d_1+100d_0=100(10-2)=800.
\]

This verifies both the corrected range and the numeric boundary.

## 10. Adversarial boundary table

| Attack | Exact consequence | Disposition |
|---|---|---|
| \(r=1\) | \(A_2=B_2=[1]\) need not create strict carries; with \(V=q^2\), \(W=-p^2/4\), the target can cancel to \(-p/2\) | Excluded; general strict-lift theorem is \(r\ge2\), headline has \(r\ge4\) |
| \(w_0\not<A_{\alpha_{a_0}}u_0\) | Phase-zero strict source carry fails | Excluded by the exact gate; \(w_0\le u_0\) is only sufficient |
| Equality in a V or W fan inequality | Selector is not unique | Exact wall boundary; no tie-breaking claim |
| Singleton support | No competitor and no finite gap | Vacuous uniqueness; normal cone is the full positive weight domain |
| \(H=1\) | All incidence scores tie and the quotient spike collapses | Excluded by \(H\ge2\) |
| Shorter quotient permutation orbit | Selector and quotient return cannot have the claimed least \(\ell\) phase | Excluded by phase separation; explicit P passes |
| \(P=I\) | Residual direction is stationary | No long primitive selector cycle |
| Unequal exponent totals | Diagonal \(t_n\) re-enters score differences | Equitotality is structural |
| A zero exponent coordinate | A derivative row may disappear and reopen cancellation | Excluded; all coordinates are at least two |
| Positive characteristic | A derivative exponent scalar may vanish | Excluded; field has characteristic zero |
| Zero displayed coefficient | Collected support changes and the uniqueness proof no longer applies | Excluded; every displayed coefficient is nonzero |
| Nonprimitive pair word | Selector least period is a proper divisor | Outside the primitive headline |
| Missing dictionary or phase mark | Literal labels or root cannot be decoded | Exact decoder side information is stated |
| Complete-state recurrence at \(n=0\) without \(d_0=q_0\) | Residual equals \(\lambda(d_0-q_0)\), including the value 800 above | Explicitly not claimed |
| Polynomial-state periodicity | \(t_n\) grows | Explicit anti-claim |

The killed planar extension is also algebraically sound.  On a chamber where
\(H(r)=ar+b\),

\[
 g(r)=\kappa\frac{(a-1)r+b}{ar+b-1},\qquad
 g'(r)=\kappa\frac{1-a-b}{(ar+b-1)^2}<0.
\]

Continuity across max walls makes the projective map decreasing, so its
square is increasing and it has no orbit of least period greater than two.
This justifies the higher-dimensional permutation twist rather than a planar
period-three claim.

## 11. Quantifiers, allowed claims, anti-claims, and article mass

The proved headline quantifiers are exact: for every rooted primitive
selector-pair word of length \(\ell\ge3\), including repeated labels and one
singleton component alphabet, the construction gives one autonomous
polynomial symplectomorphism \(F_{\mathsf w}\) on
\(2(\ell+1)\) variables.  It uses finite collected supports in
\(\mathbb Z_{\ge2}^r\), equal totals, positive weights, the declared
permutation, a characteristic-zero field, and arbitrary nonzero coefficient
tuples.  The normal-fan criterion is an iff for strict selectors; the strict
actual-degree lift additionally uses the exact first momentum gate; selector
and quotient least periods use word primitivity and phase separation; and
literal label decoding uses \(P,\lambda,\ell\), marked phase zero, and the
labelled support dictionary.

The candidate correctly makes no claim of one universal map, fixed dimension
as \(\ell\) grows, ordinary total-degree realization, a periodic polynomial
state, absolute priority, a first long tropical/max-plus cycle, generic
nonconjugacy, unequal-total or zero-coordinate validity, positive-
characteristic validity, tie breaking, inverse-degree reciprocity,
cohomological spectra, entropy or integrability, scalar word decoding,
minimal scalar recurrence, or release/external effect.

The bounded source dossier and collision matrix support a conservative
novelty score without an absolute priority statement.  After removal of
governance, hashes, paths, and discovery narrative, the proof package supports
a credible 26.0-page anonymous article: approximately 2.5 pages for
positioning, 3 for the map and degree transport, 4 for the fan iff, 4 for the
incidence realization, 3.5 for carries and leading forms, 4 for monodromy and
decoding, 3.5 for periods/recurrences/boundaries, and 1.5 for conclusion.
This lies inside the required 22--30-page interval without an empirical or
appendix dependency.

## Finding census and scores

| Category | Count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

| Gate | R2 score |
|---|---:|
| Bounded-search novelty | 8.0 / 10 |
| Standalone mathematical value | 8.1 / 10 |
| Proof confidence | 9.6 / 10 |
| Credible anonymous content | 26.0 pages |

## Decisive disposition

PASS, unconditionally.  The complete V4 append-only candidate satisfies every
formal R2 algebra, field, support, coefficient, selector, singleton,
coordinate, scalar-index, monodromy, decoding, period, failure-boundary,
anti-claim, novelty, standalone-value, proof-confidence, and article-mass
gate.  The census is exactly Blocker 0, Major 0, Minor 0, Ambiguity 0.  This
review creates no Paper 28 project, consumes no paper number, and grants no
source, build, release, or external-effect authority.

BATCH07_PAPER28_CANDIDATE_V4_PASS_R2
