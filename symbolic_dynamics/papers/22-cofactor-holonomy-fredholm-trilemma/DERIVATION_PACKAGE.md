# Derivation Package — SD-C24

**Candidate:** SD-C24  
**Purpose:** freeze every formula from the symbolic source to the route
verdict, with the pure, endpoint-weighted, character, and regular-lift objects
kept distinct

## D1. From the full-shift skeleton to the edge cofactor

The semiring representatives satisfy

\[
 F_m\boxtimes F_n\cong F_{mn},
 \qquad
 S(F_n)=F_{n+1}.
\]

An allowed factorization

\[
 S(F_n)\cong F_d\boxtimes F_q
\]

is equivalent to

\[
 n+1=dq.
\]

Thus the graph and label are derived simultaneously:

\[
 n\to d\iff d\mid n+1, d\ge2,
 \qquad
 q(n,d)=\frac{n+1}{d}.
\]

No factor-existence oracle is hidden here: the relation is the explicit edge
equation, and the label is its unique quotient witness.

## D2. Cycle telescoping and positive holonomy

For a closed path \(n_r=n_0\),

\[
\begin{aligned}
 Q(\gamma)
 &=\prod_{j=0}^{r-1}\frac{n_j+1}{n_{j+1}}\\
 &=\frac{\prod_j(n_j+1)}{\prod_jn_{j+1}}\\
 &=\frac{\prod_j(n_j+1)}{\prod_jn_j}\\
 &=\prod_j\left(1+\frac1{n_j}\right)>1.
\end{aligned}
\]

Because the left side is a product of positive integer cofactors,

\[
 Q(\gamma)\in\{2,3,\ldots\}.
\]

Two consequences separate immediately:

- the base graph is recurrent;
- the neutral sector of its \(\Gamma\)-extension is not recurrent at all.

This is why the identity group trace cannot be read as a selective prime
filter: it returns zero for every period.

## D3. Gauge decomposition

Using \(dq=n+1\),

\[
 q=\frac{n+1}{d}
   =\frac nd\left(1+\frac1n\right).
\]

Taking logarithms gives

\[
 \log q=(\log n-\log d)+\log(1+1/n).
\]

The first term is a vertex coboundary.  Around a cycle it telescopes, leaving
the source-only periodic data

\[
 Q(\gamma)=\prod_{n\in\gamma}(1+1/n).
\]

For the power twist,

\[
\begin{aligned}
 D_u^{-1}L_{s,u}D_u(e_n)
 &=\sum_{d\mid n+1}
 d^{-u}(nd)^{-s}q^{-u}n^u e_d\\
 &=\sum_{d\mid n+1}
 (nd)^{-s}(1+1/n)^{-u}e_d.
\end{aligned}
\]

The conjugating diagonal is unitary only when \(\Re u=0\).  This prevents
an algebraic gauge identity from being overstated as a bounded-similarity
theorem.

## D4. Minimal and atomic holonomy classes

If \(Q=2\), the integer cofactor word contains one \(2\) and otherwise
only \(1\)'s.  Since \(q=1\) means \(n\to n+1\), rotate after the unique
\(2\)-edge and write

\[
 k\to k+1\to\cdots\to N\to k.
\]

The closing equation gives

\[
 \frac{N+1}{k}=2,
 \qquad N=2k-1.
\]

Therefore

\[
 C_k=(k,\ldots,2k-1),
 \qquad
 \ell(C_k)=k,
 \qquad
 M_k=\frac{(2k-1)!}{(k-1)!}.
\]

For any multiplicative atom \(p\), the same argument gives

\[
 C_{k,p}=(k,\ldots,pk-1),
\]

\[
 \ell(C_{k,p})=(p-1)k,
 \qquad
 M_{k,p}=\frac{(pk-1)!}{(k-1)!}.
\]

A repetition has holonomy \(Q^\nu\), so it cannot land in an atomic class
unless \(\nu=1\).

## D5. Endpoint and cofactor weights around cycles

Every vertex of a closed path occurs once as source and once as target, so

\[
 \prod_j(n_jn_{j+1})^{-s}=N(\gamma)^{-2s}.
\]

The combined cycle weight is

\[
 N(\gamma)^{-2s}Q(\gamma)^{-u}.
\]

For \(C_k\), this becomes

\[
 M_k^{-2s}2^{-u}.
\]

The two limiting choices are genuinely different objects:

- pure cofactor: \(s=0\), weight \(2^{-u}\) independent of \(k\);
- endpoint regularized: \(\Re s>0\), weight
  \(M_k^{-2s}2^{-u}\), factorially dependent on \(k\).

## D6. Group-algebra trace to connected coefficients

At period \(r\), confinement makes

\[
 \mathcal T_r(s)=
 \sum_{\gamma\in\operatorname{Fix}_r}
 N(\gamma)^{-2s}[Q(\gamma)]
\]

a finite group-algebra sum.  Define

\[
 \mathscr L_s(z)=\sum_{r\ge1}\frac{z^r}{r}\mathcal T_r(s).
\]

Character evaluation gives

\[
 \chi(\mathscr L_s(z))=-\log D_\chi(s,z)
\]

as a germ at zero.  Haar orthogonality yields

\[
 [m]\mathscr L_s(z)=
 \int_{\widehat\Gamma}\overline{\chi(m)}
 [-\log D_\chi(s,z)]\,d\chi.
\]

For \(m=2\), the \(k\) rooted rotations of \(C_k\) cancel the \(1/k\)
connected normalization:

\[
 \mathcal H_2(s,z)=
 \sum_{k\ge2}z^kM_k^{-2s}.
\]

For an atom \(p\),

\[
 \mathcal H_p(s,z)=
 \sum_{k\ge2}z^{(p-1)k}M_{k,p}^{-2s}.
\]

The coefficient must be extracted from \(-\log D\).  Extracting it from
\(D\) would mix products of separate primitive factors.

## D7. Output-row decomposition

Fix an output \(d\).  Every source in that row is

\[
 n=dq-1.
\]

The constraint \(n\ge2\) gives

\[
 q_0(2)=2,
 \qquad
 q_0(d)=1\quad(d\ge3).
\]

Thus

\[
 R_d(s,u)=\sum_{q\ge q_0(d)}
 [d(dq-1)]^{-s}q^{-u}E_{d,dq-1}.
\]

It is rank one, so its sole singular value is the \(\ell^2\)-norm of the row:

\[
 \|R_d\|_1^2=
 \sum_{q\ge q_0(d)}
 d^{-2\sigma}(dq-1)^{-2\sigma}q^{-2a}.
\]

Because \(dq-1\asymp dq\),

\[
 \|R_d\|_1^2
 \asymp
 d^{-4\sigma}\sum_{q\ge q_0(d)}q^{-2(\sigma+a)}.
\]

The inner series is finite exactly when

\[
 \sigma+a>\frac12.
\]

When it is finite,

\[
 \|R_d\|_1\asymp d^{-2\sigma},
\]

and the outer nuclear sum is finite exactly when

\[
 \sigma>\frac12.
\]

This derives the sufficient domain.

## D8. Independent necessity mechanisms

The second half-plane is necessary even for boundedness.  At output row
\(d=2\),

\[
 \|R_2\|_2^2\asymp
 \sum_{q\ge2}q^{-2(\sigma+a)},
\]

which diverges if \(\sigma+a\le1/2\).

The first half-plane is forced by the cofactor-one successor spine.  Fourier
projection onto the first superdiagonal gives

\[
 e_n\mapsto[n(n+1)]^{-s}e_{n+1},
\]

whose trace norm is

\[
 \sum_{n\ge2}[n(n+1)]^{-\sigma}.
\]

This is finite exactly for \(\sigma>1/2\).  Therefore

\[
 \boxed{
 L_{s,u}\in\mathcal S_1
 \iff
 \Re s>\frac12,
 \ \Re(s+u)>\frac12.
 }
\]

For a unitary character, row magnitudes are the base magnitudes and the
successor phase is \(\chi(1)=1\).  Hence

\[
 L_{s,\chi}\in\mathcal S_1
 \iff \Re s>\frac12.
\]

## D9. Ordinary lift versus semifinite lift

The regular group lift has row blocks

\[
 \mathbb R_d=
 \sum_q[d(dq-1)]^{-s}E_{d,dq-1}\otimes\lambda(q).
\]

Their products satisfy

\[
 \mathbb R_d\mathbb R_d^*
 =\left(\sum_q|d(dq-1)|^{-2\sigma}\right)
 E_{dd}\otimes1.
\]

Thus the semifinite \(L^1\) row norm is the scalar row \(\ell^2\)-norm and

\[
 \mathbb L_s\in L^1(\mathcal N,\Phi)
 \iff \Re s>\frac12.
\]

This does not imply ordinary compactness.  Right deck translations commute
with \(\mathbb L_s\), generating infinitely many weakly escaping copies of
any nonzero image.  Hence the ordinary Hilbert-space operator is noncompact.

The group trace extracts identity holonomy.  Since no closed path has
\(Q=1\),

\[
 \Phi(\mathbb L_s^r)=0
\]

and the normalized local semifinite determinant is

\[
 \det_\Phi(I-z\mathbb L_s)=1.
\]

The three statements—ordinary noncompactness, semifinite \(L^1\), and
trivial neutral trace—are compatible and must be reported separately.

## D10. The trilemma

### Pure cofactor

At \(s=0\), the successor component is the unweighted unilateral shift.
Therefore the whole matrix is noncompact whenever bounded and never trace
class.  Formally,

\[
 \mathcal H_2^{\mathrm{cof}}(u,z)
 =2^{-u}\sum_{k\ge2}z^k
 =2^{-u}\frac{z^2}{1-z},
\]

which diverges at \(z=1\).

### Endpoint regularized

In the honest two-half-plane domain,

\[
 \mathcal H_2(s,u;z)
 =2^{-u}\sum_{k\ge2}z^kM_k^{-2s}
\]

is entire in \(z\), but the mass \(M_k\) is factorial.

### Unitary characters

Every canonical primitive contributes the factor

\[
 1-z^kM_k^{-2s}\chi(2).
\]

All \(C_k\) share the same phase and none is removed.

Therefore the same source object does not supply a point with all three
properties:

1. a pure atomic weight \(p^{-u}\);
2. an honest whole-operator Fredholm determinant;
3. one primitive representative per atom with the target repetition ledger.

## D11. Target comparison and route tuple

The target connected marked Euler ledger is

\[
 \sum_{r\ge1}\frac{z^r}{r}\sum_p p^{-rs}.
\]

SD-C24 instead has, for each atom \(p\), the infinite grid

\[
 \{C_{k,p}:k\ge2\},
\]

periods \((p-1)k\), and endpoint masses \(M_{k,p}^2\).  Pure cofactor
weight eliminates the mass but makes the unmarked class infinitely
multiplicitous and the whole operator non-Fredholm.

Hence the frozen tuple is

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}),
\]

and the overall decision is \(\mathrm{ROUTE\_A\_REJECTED}\).
