# Source Lock — SD-C24

**Freeze date:** 2026-08-14  
**Primary family:** Symbolic Dynamics  
**Authority object:** the successor–divisor countable Markov shift, its
cofactor cocycle, endpoint/cofactor weighted vertex adjacencies, and their
same-object character and regular-group extensions  
**Target-zero data:** forbidden and unused  
**Route-B invocation:** forbidden

## 1. Full-shift semiring skeleton

For an \(n\)-letter alphabet \(A_n\), let

\[
 F_n=A_n^{\mathbb Z}
\]

up to topological conjugacy.  Freeze

\[
 F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn},
\]

\[
 F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n},
\]

\[
 S(F_n)=F_n\boxplus F_1\cong F_{n+1},
 \qquad h(F_n)=\log n.
\]

The operation \(\boxplus\) means alphabet disjoint union followed by the
full-shift functor.  It is not claimed to be the categorical coproduct of
subshifts or the topological disjoint union of \(F_m\) and \(F_n\).

## 2. Frozen graph and phase space

Let

\[
 V=\{2,3,\ldots\},
 \qquad
 n\to d\iff d\ge2\ \text{and}\ d\mid n+1.
\]

An edge is equivalently a factor witness

\[
 S(F_n)\cong F_d\boxtimes F_q,
 \qquad
 q=q(n,d)=\frac{n+1}{d}\in\mathbb N_{\ge1}.
\]

The one-sided phase space is

\[
 X_G^+=\{(n_0,n_1,\ldots):n_j\to n_{j+1}\}.
\]

Closed paths are directed.  Cyclic rotations are identified when speaking
of an orbit; reflections are not.  A primitive orbit is not a positive
temporal power of a shorter orbit.

No primality predicate, rational-prime table, Riemann-zero table, or target
Euler support enters the edge rule.

## 3. Frozen cocycle and coefficient group

Let

\[
 \mathsf M=(\mathbb N_{\ge1},\cdot),
 \qquad
 \Gamma=\operatorname{gp}(\mathsf M)=\mathbb Q_{>0}^{\times}.
\]

The edge voltage is the exposed cofactor

\[
 \kappa(n,d)=q(n,d)\in\mathsf M\subset\Gamma.
\]

For a closed path \(\gamma=(n_0,\ldots,n_{r-1})\), with
\(n_r=n_0\), freeze

\[
 Q(\gamma)=\prod_{j=0}^{r-1}q(n_j,n_{j+1}).
\]

The compact dual \(\widehat\Gamma\) carries normalized Haar measure with

\[
 \int_{\widehat\Gamma}\overline{\chi(m)}\chi(g)\,d\chi
 =\mathbf1_{\{g=m\}}.
\]

This transform extracts source-label coefficients; it is not a target
spectral transform.

## 4. Frozen roofs, operator, and function space

Freeze the endpoint roof and cofactor roof

\[
 \tau(n,d)=\log n+\log d,
 \qquad
 \rho(n,d)=\log q(n,d).
\]

On

\[
 \mathcal H=\ell^2(V)
\]

with basis \(e_n\), use the column-source convention

\[
 L_{s,u}e_n
 =\sum_{d\mid n+1,\ d\ge2}
   (nd)^{-s}q(n,d)^{-u}e_d.
\]

For a unitary character \(\chi\in\widehat\Gamma\), freeze

\[
 L_{s,\chi}e_n
 =\sum_{d\mid n+1,\ d\ge2}
   (nd)^{-s}\chi(q(n,d))e_d.
\]

These are weighted vertex adjacencies on \(\ell^2(V)\).  They are not
identified with Ruelle operators on a Hölder Banach space.

For a closed path, put

\[
 N(\gamma)=\prod_j n_j.
\]

Its full two-parameter weight is

\[
 w_{s,u}(\gamma)=N(\gamma)^{-2s}Q(\gamma)^{-u}.
\]

The endpoint factor two is frozen and may not be removed after target
comparison.

## 5. Frozen scalar determinant convention

The exact trace-class domain is

\[
 \Omega_1=\{(s,u):\Re s>1/2,\ \Re(s+u)>1/2\}.
\]

For \((s,u)\in\Omega_1\), freeze

\[
 D(s,u;z)=\det_{\mathcal H}(I-zL_{s,u}).
\]

For every unitary character and \(\Re s>1/2\), freeze

\[
 D_\chi(s,z)=\det_{\mathcal H}(I-zL_{s,\chi}).
\]

These determinants are entire in \(z\).  The connected expansion

\[
 -\log D_\chi(s,z)
 =\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_{s,\chi}^r
\]

is used first as the normalized germ at \(z=0\).  No global logarithm branch
through determinant zeros is asserted.

The group-algebra connected ledger is

\[
 \mathscr L_s(z)=
 \sum_{r\ge1}\frac{z^r}{r}
 \sum_{\gamma\in\operatorname{Fix}_r}
 N(\gamma)^{-2s}[Q(\gamma)].
\]

Coefficient extraction is performed on \(-\log D\), not on \(D\), because
the determinant coefficients mix products of distinct primitive cycles.

## 6. Frozen regular lift and trace distinction

Let \(\lambda\) be the left regular representation of \(\Gamma\).  On
\(\mathcal H\otimes\ell^2(\Gamma)\), freeze

\[
 \mathbb L_s(e_n\otimes\delta_g)
 =\sum_{d\mid n+1,\ d\ge2}
   (nd)^{-s}e_d\otimes\delta_{q(n,d)g}.
\]

Two notions must never be conflated:

1. **Ordinary Hilbert-space compactness.**  The nonzero lift is not compact
   on \(\mathcal H\otimes\ell^2(\Gamma)\), because the infinite deck
   coordinate supplies translation copies of every nonzero image.
2. **Semifinite integrability.**  In
   \[
   \mathcal N=B(\mathcal H)\bar\otimes L(\Gamma),
   \qquad
   \Phi=\operatorname{Tr}\bar\otimes\tau_\Gamma,
   \]
   one has \(\mathbb L_s\in L^1(\mathcal N,\Phi)\) exactly when
   \(\Re s>1/2\).

The normalized local semifinite determinant is

\[
 \det_\Phi(I-z\mathbb L_s)
 =\exp\left[-\sum_{r\ge1}\frac{z^r}{r}
                   \Phi(\mathbb L_s^r)\right].
\]

It is not an ordinary Fredholm determinant of the lifted Hilbert-space
operator.

## 7. Frozen gauge convention

The exact decomposition is

\[
 q(n,d)=\frac nd\left(1+\frac1n\right),
\]

so the cocycle is cohomologous to the source potential \(1+1/n\).  With
\(D_ue_n=n^ue_n\), the identity

\[
 D_u^{-1}L_{s,u}D_u e_n
 =\sum_{d\mid n+1,\ d\ge2}
   (nd)^{-s}\left(1+\frac1n\right)^{-u}e_d
\]

is an honest unitary conjugacy only for \(u\in i\mathbb R\).  If
\(\Re u\ne0\), it is an algebraic or finite-window identity; bounded
similarity in infinite dimension is not claimed.

## 8. Frozen theorem ledger

The manuscript may claim:

1. every closed path has integer holonomy \(Q\ge2\);
2. the regular skew graph has no periodic path and all neutral group traces
   vanish;
3. the exact gauge decomposition above;
4. \(Q=2\) exactly for the canonical \(C_k\) family;
5. for a multiplicative atom \(p\), \(Q=p\) exactly for
   \(C_{k,p}=(k,\ldots,pk-1)\);
6. repetitions do not contribute to an atomic holonomy class;
7. exact connected holonomy-class coefficients by Haar extraction;
8. \(L_{s,u}\in\mathcal S_1\) iff both strict half-plane inequalities hold;
9. \(L_{s,\chi}\in\mathcal S_1\) iff \(\Re s>1/2\);
10. the regular lift is semifinite \(L^1\) on the same base half-plane but
    ordinarily noncompact;
11. the neutral local \(\Phi\)-determinant equals one;
12. the pure-cofactor/endpoint/character Fredholm trilemma;
13. first-return induction and arbitrary positive inventories preserve the
    obstruction;
14. every statistic depending only on \(Q\) is blind to the index \(k\) on
    the canonical spine.

## 9. Forbidden claims

The manuscript must not claim:

- that \(D(s,u;z)\), \(D_\chi(s,z)\), or \(\det_\Phi\) equals a Riemann
  Euler determinant;
- that the whole determinant continues to \(\Re s\le1/2\);
- that the formal pure-cofactor series is a Fredholm determinant;
- that ordinary compactness follows from semifinite \(L^1\);
- that the neutral determinant \(1\) is an arithmetic success;
- a functional equation, Gamma factor, explicit formula, Riemann–von
  Mangoldt law, Weil compression, RH, or Hilbert–Pólya operator;
- that the bounded literature search proves absolute priority.

## 10. Control and route lock

Every positive inventory \(\mu:V\to(0,\infty)\) preserves the exact
holonomy-two support.  Transporting the full-shift skeleton together with
successor and tensor also preserves the theorem.  A cancellation visible
only after summing different holonomy classes receives no selectivity credit.

The strict tuple is

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}),
\]

with overall \(\mathrm{ROUTE\_A\_REJECTED}\).  Route B remains locked.

