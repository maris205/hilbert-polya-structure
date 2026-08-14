# Proof Package — SD-C24

**Candidate:** SD-C24  
**Proof status:** complete for every manuscript theorem  
**Primary family:** Symbolic Dynamics  
**External inputs:** only standard trace-ideal, Haar-orthogonality, and
semifinite-trace facts; all candidate-specific claims are proved here

## 0. Notation and conventions

Let

\[
 V=\{2,3,\ldots\},
 \qquad
 n\to d\iff d\mid n+1,\ d\ge2,
\]

and put

\[
 q(n,d)=\frac{n+1}{d}.
\]

A rooted length-\(r\) closed path is
\(\gamma=(n_0,\ldots,n_{r-1})\) with \(n_j\to n_{j+1}\), indices modulo
\(r\).  Define

\[
 Q(\gamma)=\prod_{j=0}^{r-1}q(n_j,n_{j+1}),
 \qquad
 N(\gamma)=\prod_{j=0}^{r-1}n_j.
\]

The operator on \(\mathcal H=\ell^2(V)\) is

\[
 L_{s,u}e_n=
 \sum_{d\mid n+1,\ d\ge2}(nd)^{-s}q(n,d)^{-u}e_d.
\]

Throughout, \(\sigma=\Re s\) and \(a=\Re u\).

## 1. Algebraic holonomy

### Theorem 1.1 — positive cycle holonomy

Every closed path satisfies

\[
 Q(\gamma)=
 \prod_{j=0}^{r-1}\left(1+\frac1{n_j}\right)
 \in\{2,3,\ldots\}.
\]

**Proof.**  Since every edge factor \(q(n_j,n_{j+1})\) is a positive
integer, \(Q(\gamma)\) is a positive integer.  Cyclicity gives

\[
\begin{aligned}
 Q(\gamma)
 &=\prod_j\frac{n_j+1}{n_{j+1}}
 =\frac{\prod_j(n_j+1)}{\prod_jn_{j+1}}\\
 &=\frac{\prod_j(n_j+1)}{\prod_jn_j}
 =\prod_j\left(1+\frac1{n_j}\right).
\end{aligned}
\]

Every real factor in the final product is strictly larger than one, so
\(Q(\gamma)>1\).  Being an integer, it is at least two. ∎

### Corollary 1.2 — neutral recurrence is empty

In the skew graph

\[
 (n,g)\longrightarrow(d,q(n,d)g),
 \qquad g\in\Gamma=\mathbb Q_{>0}^{\times},
\]

there is no periodic path.

**Proof.**  A lift of a base closed path closes in the group coordinate
exactly if \(Q(\gamma)=1\), which Theorem 1.1 forbids. ∎

Consequently the identity coefficient of every rooted group trace is zero.
On the semifinite trace domain this yields

\[
 \Phi(\mathbb L_s^r)=0,
 \qquad r\ge1.
\]

### Theorem 1.3 — exact gauge decomposition

For every edge,

\[
 q(n,d)=\frac nd\left(1+\frac1n\right).
\]

Thus \(\log q\) differs from the source potential
\(\log(1+1/n)\) by the coboundary \(\log n-\log d\).  On closed paths the
coboundary telescopes.  If \(D_ue_n=n^ue_n\), then on finitely supported
vectors

\[
 D_u^{-1}L_{s,u}D_u e_n
 =\sum_{d\mid n+1,\ d\ge2}
 (nd)^{-s}\left(1+\frac1n\right)^{-u}e_d.
\]

**Proof.**  The first identity follows from \(dq=n+1\).  For the operator
identity, the coefficient after conjugation is

\[
 d^{-u}(nd)^{-s}q^{-u}n^u
 =(nd)^{-s}\left(\frac{n}{dq}\right)^u
 =(nd)^{-s}\left(\frac n{n+1}\right)^u.
\]

This is the asserted source weight.  When \(u=it\), \(|n^u|=1\), so
\(D_u\) is unitary.  For \(\Re u\ne0\), one of \(D_u,D_u^{-1}\) is
unbounded, so no bounded infinite-dimensional similarity follows merely
from the algebraic calculation. ∎

## 2. Exact holonomy classifications

### Theorem 2.1 — classification of \(Q=2\)

A closed path has \(Q(\gamma)=2\) if and only if, up to rotation,

\[
 C_k=(k,k+1,\ldots,2k-1),
 \qquad k\ge2.
\]

It is simple, primitive, and has length \(k\).

**Proof.**  Write \(Q=\prod_jq_j\) with all \(q_j\in\mathbb N_{\ge1}\).
If the product is two, exactly one factor is two and all others are one.
An edge has \(q=1\) precisely when its target is the source plus one.
Rotate the path so the unique \(q=2\) edge is the closing edge, with target
\(k\).  The remaining edges are successors, so the path has the form

\[
 k\to k+1\to\cdots\to N\to k.
\]

The closing equation is \((N+1)/k=2\), hence \(N=2k-1\).  Conversely,
\(C_k\) has \(k-1\) successor edges and the closing cofactor two.  Its
vertices are distinct, so it is simple and cannot be a temporal power. ∎

### Theorem 2.2 — classification of atomic holonomy

Let \(p\) be an atom of \((\mathbb N_{\ge1},\cdot)\).  Then
\(Q(\gamma)=p\) if and only if, up to rotation,

\[
 C_{k,p}=(k,k+1,\ldots,pk-1),
 \qquad k\ge2.
\]

This orbit is simple and primitive, its length is \((p-1)k\), and

\[
 N(C_{k,p})=M_{k,p}
 =\frac{(pk-1)!}{(k-1)!}.
\]

**Proof.**  Atomicity of \(p=\prod_jq_j\) forces one cofactor to equal
\(p\) and all others to equal one.  Rotate after the unique nontrivial edge.
The successor run beginning at \(k\) ends at \(N\), and the closing equation
\((N+1)/k=p\) gives \(N=pk-1\).  The converse is direct.  The vertex count is
\((pk-1)-k+1=(p-1)k\), and multiplying those consecutive vertices gives the
factorial ratio.  Simplicity implies primitivity. ∎

### Corollary 2.3 — repetitions do not enter an atomic class

If \(Q(\eta^\nu)=p\) is atomic, then \(\nu=1\).

**Proof.**  By Theorem 1.1, \(Q(\eta)\ge2\), while
\(Q(\eta^\nu)=Q(\eta)^\nu\).  An atom cannot be a nontrivial positive
power. ∎

## 3. Finite support and connected coefficient extraction

### Lemma 3.1 — fixed-period confinement

Every length-\(r\) closed path lies in \(\{2,\ldots,2r-1\}\).

**Proof.**  Let \(M\) be the maximum vertex.  The edge leaving an occurrence
of \(M\) cannot be the successor edge: that would visit \(M+1\).  Its target
\(d\) is therefore a proper divisor of \(M+1\), so

\[
 d\le\frac{M+1}{2}.
\]

Every edge satisfies \(d\le n+1\), so each of the remaining \(r-1\) steps
can increase its source by at most one.  To return to \(M\),

\[
 M\le d+r-1
 \le\frac{M+1}{2}+r-1,
\]

which rearranges to \(M\le2r-1\). ∎

Thus each rooted trace coefficient at fixed period is a finite sum even
before analytic convergence in \(r\) is discussed.

### Theorem 3.2 — exact connected holonomy coefficient

Let

\[
 \mathcal T_r(s)=
 \sum_{\gamma\in\operatorname{Fix}_r}
 N(\gamma)^{-2s}[Q(\gamma)]
\]

and

\[
 \mathscr L_s(z)=\sum_{r\ge1}\frac{z^r}{r}\mathcal T_r(s).
\]

On the trace-class, small-\(z\) domain, for every \(m\in\Gamma\),

\[
\begin{aligned}
 [m]\mathscr L_s(z)
 &=\int_{\widehat\Gamma}\overline{\chi(m)}
       [-\log D_\chi(s,z)]\,d\chi\\
 &=\sum_{\substack{[\gamma]\ \mathrm{primitive},\ \nu\ge1\\
                    Q(\gamma)^\nu=m}}
   \frac{z^{\nu\ell(\gamma)}}{\nu}
   N(\gamma)^{-2s\nu}.
\end{aligned}
\]

**Proof.**  Lemma 3.1 makes every fixed-period group-algebra trace a finite
sum.  Evaluate it at \(\chi\), expand the Fredholm trace logarithm, and use

\[
 \int_{\widehat\Gamma}\overline{\chi(m)}\chi(g)\,d\chi
 =\mathbf1_{\{g=m\}}.
\]

Regrouping rooted paths into primitive rotation classes and temporal powers
gives the second formula. ∎

### Corollary 3.3 — exact \(Q=2\) coefficient

Let

\[
 M_k=\prod_{n=k}^{2k-1}n=\frac{(2k-1)!}{(k-1)!}.
\]

Then

\[
 [2]\mathcal T_r(s)=rM_r^{-2s},
\]

and

\[
 \mathcal H_2(s,z):=[2]\mathscr L_s(z)
 =\sum_{k\ge2}z^kM_k^{-2s}.
\]

**Proof.**  Theorem 2.1 gives exactly one primitive rotation class \(C_r\)
at period \(r\), hence \(r\) rooted rotations.  The factor \(1/r\) in the
connected ledger cancels that multiplicity.  Corollary 2.3 excludes temporal
repetitions. ∎

The series has infinite \(z\)-radius for \(\Re s>0\), radius one for
\(\Re s=0\), and radius zero for \(\Re s<0\), by the factorial growth of
\(M_k\).  Only \(\Re s>1/2\) is claimed to come from the whole Fredholm
operator.

### Corollary 3.4 — exact atomic coefficient

For every atom \(p\),

\[
 \mathcal H_p(s,z)=
 \sum_{k\ge2}z^{(p-1)k}M_{k,p}^{-2s}.
\]

No repeated primitive contributes.

## 4. Sharp trace-class phase diagram

### Theorem 4.1 — exact \(\mathcal S_1\) domain

\[
 L_{s,u}\in\mathcal S_1(\mathcal H)
 \quad\Longleftrightarrow\quad
 \sigma>\frac12
 \quad\text{and}\quad
 \sigma+a>\frac12.
\]

On this domain, \((s,u)\mapsto L_{s,u}\) is locally holomorphic in trace
norm, so \(D(s,u;z)\) is jointly holomorphic and entire in \(z\).

**Proof of sufficiency.**  Write every source entering output row \(d\) as
\(n=dq-1\).  Since \(n\ge2\), the lower endpoint is
\(q_0(2)=2\) and \(q_0(d)=1\) for \(d\ge3\).  Define

\[
 R_d(s,u)=\sum_{q\ge q_0(d)}
 [d(dq-1)]^{-s}q^{-u}E_{d,dq-1}.
\]

It is rank one.  Therefore

\[
 \|R_d(s,u)\|_1^2=
 \sum_{q\ge q_0(d)}
 d^{-2\sigma}(dq-1)^{-2\sigma}q^{-2a}.
\]

For every allowed \((d,q)\), \(dq\ge3\), and

\[
 \frac23dq\le dq-1<dq.
\]

Consequently the row square is comparable, with constants depending only on
\(\sigma\), to

\[
 d^{-4\sigma}
 \sum_{q\ge q_0(d)}q^{-2(\sigma+a)}.
\]

If \(\sigma+a>1/2\), the \(q\)-sum is finite and bounded above uniformly in
\(d\).  For \(d\ge3\), it is also bounded below by its \(q=1\) term.
Hence

\[
 \|R_d(s,u)\|_1\asymp_{\sigma,a}d^{-2\sigma}
 \qquad(d\ge3).
\]

If also \(\sigma>1/2\), then

\[
 \sum_{d\ge2}\|R_d(s,u)\|_1<\infty.
\]

The series \(\sum_dR_d\) converges in trace norm and equals the frozen
matrix on finitely supported vectors, proving trace class.

On a compact subset of the two strict half-planes, both exponent margins are
uniformly positive.  Derivatives introduce only powers of \(\log d\),
\(\log(dq-1)\), and \(\log q\), absorbed by a smaller positive margin.
Termwise differentiation of the trace-norm-convergent row series proves
local trace-norm holomorphy.  Standard Fredholm theory then gives the
determinant statement.

**Necessity of \(\sigma+a>1/2\).**  If the frozen matrix had a bounded
extension, every output-row coefficient vector would lie in \(\ell^2\).
For \(d=2\),

\[
 \sum_{q\ge2}|[2(2q-1)]^{-s}q^{-u}|^2
 \asymp
 \sum_{q\ge2}q^{-2(\sigma+a)}.
\]

This diverges when \(\sigma+a\le1/2\).  In that region the matrix is not
even bounded and hence cannot be trace class.

**Necessity of \(\sigma>1/2\).**  Let \(U_te_n=e^{int}e_n\).  The map

\[
 \mathcal P_1(T)=\frac1{2\pi}\int_0^{2\pi}
 e^{-it}U_tTU_t^{-1}\,dt
\]

is a contractive Fourier projection on \(\mathcal S_1\).  A matrix unit
\(E_{d,n}\) has phase \(e^{i(d-n)t}\); the multiplier above retains
\(d-n=1\), which in this graph is exactly \(d=n+1\), equivalently \(q=1\).
Thus

\[
 \mathcal P_1(L_{s,u})e_n=[n(n+1)]^{-s}e_{n+1}.
\]

Its singular values are the moduli of its weights, and therefore

\[
 \|\mathcal P_1(L_{s,u})\|_1
 =\sum_{n\ge2}[n(n+1)]^{-\sigma}.
\]

This series converges exactly for \(\sigma>1/2\).  If \(L_{s,u}\) were
trace class, its contractive image would be trace class, proving necessity.
∎

### Corollary 4.2 — unitary character fibers

For every \(\chi\in\widehat\Gamma\),

\[
 L_{s,\chi}\in\mathcal S_1
 \iff \Re s>\frac12.
\]

**Proof.**  Unitary phases do not alter the row norms, and \(\chi(1)=1\)
leaves the successor Fourier extraction unchanged. ∎

## 5. Regular lift: ordinary and semifinite statements

### Theorem 5.1 — semifinite \(L^1\) threshold

Let

\[
 \mathbb L_s(e_n\otimes\delta_g)=
 \sum_{d\mid n+1,\ d\ge2}
 (nd)^{-s}e_d\otimes\delta_{q(n,d)g}.
\]

In

\[
 (\mathcal N,\Phi)=
 (B(\mathcal H)\bar\otimes L(\Gamma),
  \operatorname{Tr}\bar\otimes\tau_\Gamma),
\]

one has

\[
 \mathbb L_s\in L^1(\mathcal N,\Phi)
 \iff \Re s>\frac12.
\]

**Proof.**  Decompose by output row:

\[
 \mathbb R_d=
 \sum_{q\ge q_0(d)}[d(dq-1)]^{-s}
 E_{d,dq-1}\otimes\lambda(q).
\]

Distinct \(q\) have distinct input matrix units.  Hence

\[
 \mathbb R_d\mathbb R_d^*
 =\left(\sum_{q\ge q_0(d)}
 |d(dq-1)|^{-2\sigma}\right)E_{dd}\otimes1.
\]

It follows that

\[
 \|\mathbb R_d\|_{L^1(\Phi)}
 =\left(\sum_q|d(dq-1)|^{-2\sigma}\right)^{1/2}
 \asymp d^{-2\sigma}
\]

whenever \(\sigma>1/2\).  Summation over \(d\) proves sufficiency.  The
matrix-diagonal Fourier projection is trace preserving on the semifinite
\(L^1\) space and retains the same successor shift.  Its \(L^1\) norm is
\(\sum_n[n(n+1)]^{-\sigma}\), proving necessity. ∎

### Theorem 5.2 — ordinary noncompactness

For every \(s\) in the preceding half-plane, the nonzero operator
\(\mathbb L_s\) is not compact on
\(\mathcal H\otimes\ell^2(\Gamma)\).

**Proof.**  The lift commutes with the right regular representation on the
deck coordinate.  Choose a unit vector \(\xi\) with
\(\mathbb L_s\xi\ne0\), and a sequence \(g_j\to\infty\) in the discrete
group.  The translates \(\rho(g_j)\xi\) are bounded and weakly null after
passing to an escaping sequence; their images are
\(\rho(g_j)\mathbb L_s\xi\), all of the same nonzero norm.  A compact
operator sends weakly null bounded sequences to norm-null sequences, a
contradiction. ∎

### Corollary 5.3 — neutral semifinite determinant

For \(\Re s>1/2\),

\[
 \det_\Phi(I-z\mathbb L_s)=1
\]

as the normalized local trace-series determinant.

**Proof.**  Corollary 1.2 makes every trace coefficient
\(\Phi(\mathbb L_s^r)\) zero.  Substitution in the defining exponential
gives one.  The statement is semifinite and local; it says nothing about an
ordinary Fredholm determinant of the noncompact lifted operator. ∎

## 6. Fredholm trilemma and no-go

### Theorem 6.1 — pure cofactor noncompactness

At \(s=0\), the pure cofactor matrix

\[
 Q_ue_n=\sum_{d\mid n+1,\ d\ge2}q(n,d)^{-u}e_d
\]

is never trace class.  Whenever it is bounded, it is noncompact.

**Proof.**  Theorem 4.1 already excludes trace class because it would require
\(0>1/2\).  More directly, the successor Fourier projection is the
unweighted unilateral shift \(e_n\mapsto e_{n+1}\), which is noncompact.
Fourier averaging preserves compactness, so a bounded \(Q_u\) cannot be
compact. ∎

For \(\Re u>1\), Schur's test proves boundedness: every row and column sum
is bounded by a constant multiple of \(\sum_{q\ge1}q^{-\Re u}\).  No full
boundedness classification in the remaining strip is needed.

### Theorem 6.2 — pure and regularized class series

For \(|z|<1\), the formal pure-cofactor holonomy-two connected series is

\[
 \mathcal H_2^{\mathrm{cof}}(u,z)
 =2^{-u}\frac{z^2}{1-z}.
\]

It diverges at \(z=1\).  With endpoint regularization,

\[
 \mathcal H_2(s,u;z)
 =2^{-u}\sum_{k\ge2}z^kM_k^{-2s},
\]

which is entire in \(z\) on the honest trace-class domain.

**Proof.**  Each \(C_k\) has \(Q=2\).  With only the cofactor roof it has
the constant weight \(2^{-u}\), giving the geometric series.  The endpoint
roof multiplies it by \(M_k^{-2s}\); factorial growth gives infinite
\(z\)-radius whenever \(\Re s>0\), in particular throughout the honest
Fredholm domain. ∎

### Proposition 6.3 — first-return collapse

Induce on edges with \(q>1\).  Every \(C_k\) becomes one fixed return branch
indexed by \(k\ge2\).  Its diagonal entry is

\[
 2^{-u}z^k
\]

for the pure cofactor-time marking, and

\[
 2^{-u}z^kM_k^{-2s}
\]

for the endpoint-regularized system.  At \(s=0,z=1\), the first diagonal has
constant nonzero infinite multiplicity and is noncompact.  Endpoint
regularization restores summability only by retaining the factorial
\(k\)-ledger.

**Proof.**  Theorem 2.1 says each \(C_k\) contains exactly one nontrivial
cofactor edge, so it is one first-return branch.  Multiplying its edge weights
gives the displayed entries.  The compactness and summability conclusions
are then immediate for diagonal operators. ∎

### Theorem 6.4 — abelian-holonomy blindness

For any map \(F:\Gamma\to\mathcal A\), the orbit statistic
\(\gamma\mapsto F(Q(\gamma))\) is constant on the entire family
\(\{C_k:k\ge2\}\).

**Proof.**  Theorem 2.1 gives \(Q(C_k)=2\) for every \(k\), so the common
value is \(F(2)\). ∎

In particular, no scalar character, Fourier combination, or holonomy-only
mask can select prime values of \(k\).  This conclusion concerns functions
of the abelian product and does not preclude a genuinely new ordered-word
cocycle.

### Proposition 6.5 — positive-inventory persistence

Let \(\mu:V\to(0,\infty)\) and weight an edge by
\([\mu(n)\mu(d)]^{-s}\).  Then the \(Q=2\) primitive support is still exactly
\(\{C_k:k\ge2\}\), and its connected coefficient is

\[
 \sum_{k\ge2}z^k
 \left(\prod_{n=k}^{2k-1}\mu(n)\right)^{-2s}.
\]

**Proof.**  Positive weights do not change admissibility or holonomy.  On
\(C_k\), every vertex occurs once as a source and once as a target, producing
the square of the inventory product. ∎

## 7. Dependency and claim audit

| Claim | Depends on | External theorem used | Status |
|---|---|---|---|
| \(Q>1\) | edge equation | none | proved |
| neutral sector empty | \(Q>1\) | group-trace coefficient rule | proved |
| gauge decomposition | edge equation | none | proved |
| \(Q=2\), \(Q=p\) classes | integer factorization | none | proved |
| connected coefficient | confinement and class theorem | Haar orthogonality, Fredholm trace-log | proved |
| sharp \(\mathcal S_1\) domain | row decomposition, successor extraction | trace-ideal ideal property | proved |
| character domain | sharp theorem | none beyond above | proved |
| semifinite \(L^1\) domain | row decomposition | standard semifinite \(L^1\) calculus | proved |
| ordinary noncompact lift | deck translations | compact maps weakly null to norm-null | proved |
| pure cofactor obstruction | successor extraction | compact-ideal closure | proved |
| inventory persistence | class theorem | none | proved |

## 8. Explicitly unproved statements

The proof package does not assert:

- boundedness of \(Q_u\) throughout \(1/2<\Re u\le1\);
- continuation of the whole Fredholm determinant outside the sharp
  trace-class domain;
- a global logarithm of a determinant through its zeros;
- ordinary compactness or ordinary Fredholm determinants for the regular
  lift;
- a Riemann Euler identity, explicit formula, functional equation, RH, or
  Hilbert–Pólya mechanism;
- absolute novelty priority.

