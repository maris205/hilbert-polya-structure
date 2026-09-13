---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-brieskorn-quasiregular-reeb-route-a"
canonical_tex: "henon_dynamics/henon_brieskorn_quasiregular_reeb_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_brieskorn_quasiregular_reeb_route_a/paper/main.pdf"
source_sha256: "e58834140268cdc7623d7ef94df78e3480c97e64cd5c32b347624646a745d46f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Quasiregular Reeb Dynamics on Pairwise-Coprime Brieskorn Three-Manifolds

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_brieskorn_quasiregular_reeb_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_brieskorn_quasiregular_reeb_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_brieskorn_quasiregular_reeb_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_brieskorn_quasiregular_reeb_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every pair of odd coprime integers $3\leq p<q$, we close the normalized Reeb dynamics of the Brieskorn link $\Sigma(2,p,q)$. There are exactly three exceptional simple orbit circles, of periods $2p,2q,pq$, and a principal period $2pq$. A divisibility rule gives every fixed-time component and proves it is Morse--Bott. Missing-coordinate trivializations give the transverse rotations, return determinants, first degeneracies, and all pre-degeneracy Conley--Zehnder indices. The orbit space is $S^2(2,p,q)$, and a declared Milnor-fiber capping convention gives $\mu_{\mathrm{RS}}=2(2pq)\chi_{\rm orb}=-2pq+4p+4q$; this is positive only for $(p,q)=(3,5)$ and never zero. Exhaustive exact computation is a regression receipt, not the proof.
author:
- 'HCS-C370 theorem package'
date: 4 September 2026
title: |
  Quasiregular Reeb Dynamics on Pairwise-Coprime\
  Brieskorn Three-Manifolds
```

## Markdown 正文

# Frozen contact system and main result

Put $a=(a_0,a_1,a_2)=(2,p,q)$ and $$f(z)=z_0^2+z_1^p+z_2^q,\qquad
 \Sigma_{p,q}=f^{-1}(0)\cap S^5\subset\mathbb C^3.$$ The origin is the only critical point of $f$, so $\Sigma_{p,q}$ is a smooth closed three-manifold. We freeze the scale $$\alpha=\frac{i}{4\pi}\sum_{j=0}^2a_j
 (z_jd\bar z_j-\bar z_jdz_j).$$ This is the standard weighted Brieskorn contact form in the normalization used throughout this paper.

The Reeb vector field and its flow are $$R=2\pi i\sum_{j=0}^2\frac1{a_j}
 (z_j\partial_{z_j}-\bar z_j\partial_{\bar z_j}),\qquad
 \Phi_t(z_j)=e^{2\pi it/a_j}z_j.$$ There are three exceptional simple circles, with support and primitive period $$\{0,1\}:2p,\qquad \{0,2\}:2q,\qquad \{1,2\}:pq,$$ whereas the principal period is $d=2pq$. For real $T$, let $J_T=\{j:T/a_j\in\mathbb Z\}$. The fixed set is empty for $|J_T|<2$, the corresponding exceptional circle for $|J_T|=2$, and all of $\Sigma_{p,q}$ for $|J_T|=3$. Every nonempty component is Morse--Bott.

In the ambient missing-coordinate complex-line trivializations, the three transverse rotation numbers are $$\rho_{01}=\frac{2p}{q},\qquad \rho_{02}=\frac{2q}{p},\qquad
 \rho_{12}=\frac{pq}{2}.$$ Thus $\det_{\mathbb R}(I-P)=4\sin^2(\pi\rho)$, and first degeneracy occurs at covers $q,p,2$. Before that cover, $$\mu_{\mathrm{CZ}}(\gamma^r)=2\lfloor r\rho\rfloor+1.$$

The common-period orbit space is $S^2(2,p,q)$, with $$\chi_{\rm orb}=\frac12+\frac1p+\frac1q-1.$$ In the standard Milnor-fiber capping trivialization, the principal family has $$\mu_{\mathrm{RS}}=2d\chi_{\rm orb}=-2pq+4p+4q.$$ Both quantities are positive exactly at $(p,q)=(3,5)$, negative otherwise, and never zero.

# Normalization and primitive orbit types

The weighted ambient two-form is positive, and its contact-type restriction to the link is $d\alpha$. Direct evaluation gives, coordinate by coordinate, $$\alpha(R)=\sum_j|z_j|^2=1,\qquad
 \iota_Rd\alpha=-d\|z\|^2,\qquad df(R)=2\pi i f.$$ Therefore $R$ is tangent to both defining hypersurfaces, and $\iota_Rd\alpha$ vanishes on the tangent of the link. This proves the stated normalization rather than fixing it only up to a positive constant.

A link point cannot have only one nonzero coordinate. On a two-coordinate locus of weights $a_i,a_j$, the moduli are the unique positive solution of $$r^{a_i}=s^{a_j},\qquad r^2+s^2=1.$$ The phase equation cuts out a connected one-dimensional subtorus because $\gcd(a_i,a_j)=1$. Hence each such locus is one embedded circle and one Reeb orbit. A point of support $S$ returns first at $\operatorname{lcm}(a_j:j\in S)$. Pairwise coprimality of $2,p,q$ now gives

           support            $01$   $02$   $12$   $012$
  -------------------------- ------ ------ ------ -------
            period            $2p$   $2q$   $pq$   $2pq$
        isotropy order        $q$    $p$    $2$     $1$
   orbit-quotient dimension   $0$    $0$    $0$     $2$

The final entry is the structural obstruction to treating all primitive orbits as a discrete ledger.

\>0

# All fixed times and the Morse--Bott kernel

A point $z$ is fixed by $\Phi_T$ exactly when $e^{2\pi iT/a_j}=1$ for every nonzero $z_j$. Since at least two coordinates are nonzero, this proves the asserted $J_T$ classification for arbitrary real $T$, not just for the finite evidence window.

It remains to prove cleanness. Along an exceptional two-coordinate circle, varying the missing coordinate is tangent to $f^{-1}(0)$ to first order: the missing partial derivative $a_kz_k^{a_k-1}$ vanishes at $z_k=0$. It is also tangent to the sphere there. This complex line is the contact-normal plane to the Reeb orbit. At a time fixing exactly the active coordinates, the derivative is the identity on the orbit tangent and a nonidentity rotation on the missing line. Hence $$\ker(d\Phi_T-I)=T\operatorname{Fix}(\Phi_T).$$ At a common-period time the derivative is the identity on the whole link, so the same equality holds. All nonempty fixed sets are therefore Morse--Bott.

For one pair, in the integer window $1\leq T\leq2pq$, the exact counts are $$\begin{array}{c|ccccc}
\text{fixed class}&\varnothing&01&02&12&\Sigma_{p,q}\\ \hline
\text{count}&2pq-p-q&q-1&p-1&1&1.
\end{array}$$ For example, the $01$ times are the nonprincipal multiples of $2p$, hence $q-1$ of them. The other entries follow identically, and their sum is $2pq$.

# Transverse rotations, determinants, and CZ indices

The derivative on the missing $k$-coordinate line over an orbit of period $T_0$ is multiplication by $e^{2\pi iT_0/a_k}$. With the constant ambient coordinate vector as the declared complex trivialization, its rotation number is $T_0/a_k$. This yields $2p/q,2q/p,pq/2$ without an unstated framing change.

For the real rotation matrix through angle $2\pi\rho$, $$\det_{\mathbb R}(I-P)=2-2\cos(2\pi\rho)=4\sin^2(\pi\rho).$$ The fractions are reduced because $p,q$ are odd and coprime. Their denominators $q,p,2$ are exactly the first degenerate covers; multiplying each by its primitive period gives $2pq$. Before degeneracy the standard planar rotation formula is $\mu_{\mathrm{CZ}}(\gamma^r)=2\lfloor r\rho\rfloor+1$. We make no CZ assignment at the degenerate common-period cover; it belongs to the RS calculation below.

\>1

# Seifert quotient and principal Robbin--Salamon index

The quasiregular circle action has three exceptional fibers with isotropy orders $2,p,q$. The pairwise-coprime Brieskorn three-manifold has genus-zero Seifert base, so its orbit orbifold is $S^2(2,p,q)$. Therefore $$\chi_{\rm orb}=2-(1-\tfrac12)
 -(1-\tfrac1p)-(1-\tfrac1q)
 =\frac12+\frac1p+\frac1q-1.$$

We now make the principal index normalization explicit. Use the standard Milnor-fiber capping trivialization employed for Brieskorn Reeb orbits in \[1,2\]. Over $[0,d]$, the ambient diagonal complex path contributes $$2d(\tfrac12+\tfrac1p+\tfrac1q).$$ Passing to the contact distribution removes the complex normal block supplied by the hypersurface and radial/Reeb directions. In the standard Brieskorn capping calculation \[1, §5.3, formula (14), Proposition 5.9\], this two-plane block splits into a defining-polynomial line and a stationary radial/Reeb line. The identity $df(R)=2\pi if$ shows that the first winds $d$ times and contributes $2d$; the second contributes zero. The Milnor-fiber complex volume trivializes the determinant line, so this capping convention is well defined. Consequently $$\mu_{\mathrm{RS}}=2d(\tfrac12+\tfrac1p+\tfrac1q-1)
 =-2pq+4p+4q.$$ This is an analytic derivation of the standard formula under a named trivialization, not an inference from the finite table.

The sign classification is elementary and sharp. If $p\geq5$, then $q\geq7$ and $1/p+1/q\leq1/5+1/7<1/2$. If $p=3$, positivity forces $q<6$, leaving only $q=5$. Equality would require the excluded even value $q=6$. Since $\mu_{\mathrm{RS}}=2d\chi_{\rm orb}$, the same trichotomy holds for the index.

# Exact receipt, limitations, and Route-A boundary

The canonical artifact exhausts all 1,003 coprime odd pairs $3\leq p<q\leq101$. It recomputes 5,469,178 integer-time cells, 4,012 orbit types, 3,009 transverse rotations, 103,749 nondegenerate CZ values, and 1,003 Seifert/index rows. A producer and a code-independent checker agree on every row and streaming digest. SymPy independently verifies the normalization, tangent identities, determinant identity, lcm and denominator statements, count identity, and RS formula. Isolated replay and repaired-hash hostile mutations test serialization and claim locks. These are finite regression checks; the preceding proofs establish the unbounded family.

Kwon and van Koert \[1\] own the standard Brieskorn contact background. Van Koert \[2\] records the periodic-stratum and index framework. We claim no literature priority. We do not compute contact homology, and we do not replace the principal Morse--Bott continuum by an isolated orbit ledger.

Integer weights, lcm periods, Seifert orders, and indices give only a weak arithmetic relation. There is no target arithmetic local datum, Euler factor, root number, automorphy assertion, target divisor, target functional equation, target-zero match, or Hilbert--Pólya operator. Route B is false. The result is $$\begin{gathered}
(\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},\mathrm{A1\_WEAK},
\mathrm{A2\_FAIL},\\
\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\qquad \mathrm{ROUTE\_A\_EXPLORATORY}.
\end{gathered}$$ Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### References.

\[1\] M. Kwon and O. van Koert, *Brieskorn manifolds in contact topology*, Bull. Lond. Math. Soc. 48 (2016), [DOI 10.1112/blms/bdv088](https://doi.org/10.1112/blms/bdv088). \[2\] O. van Koert, *Contact homology of Brieskorn manifolds*, Forum Math. 20 (2008), [DOI 10.1515/FORUM.2008.016](https://doi.org/10.1515/FORUM.2008.016).

round zero contact normalization and period atlas round one fixed strata and transverse index atlas round two Seifert sign theorem and Route A closure
