---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-weight-clock-bifurcation"
canonical_tex: "henon_dynamics/henon_mu3_weight_clock_bifurcation/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_weight_clock_bifurcation/paper/main.pdf"
source_sha256: "6b1d6479fcf4ddada6f16bc99f9e0a694824c60c282f9658f112c4ae5730fa5e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Weight--Clock Bifurcation in Cohomological Hénon Moments

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_weight_clock_bifurcation>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_weight_clock_bifurcation/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_weight_clock_bifurcation/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_weight_clock_bifurcation/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_weight_clock_bifurcation/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We compare the cohomological structures of the second, third, and fourth chronological moments of a finite-field Fourier--cubic quantization of an area-preserving Hénon map. At every good split prime, projective radial cancellation expresses the normalized $n$-th moment as minus twice the sum of a pure weight-zero trace $E_n$ and a pure weight-one trace $O_n$. For a smooth source member their ranks are $(4^n+5)/3$ and $2(4^n-4)/3$, hence the total rank is $4^n-1$. The unchanged Galois normalization forces an exact leading extraction $$\exp(-\ell_n(s)/n)
   =\exp\!\left(\frac{2}{n}\operatorname{Log}_0
   L_K^{(S)}(E_n\oplus O_n,ns+1)\right)H_{n,S}(s),$$ where $S$ is the frozen finite bad set and $H_{n,S}$ is holomorphic and nonzero for $\operatorname{Re}s>0$. The prime denominator fixes the full clock $u=ns+j$, $j\ge1$. Its leading weight-one factors share center $s=0$, whereas the weight-zero centers are $-1/4,-1/6,-1/8$; higher denominator terms also split the odd rail. This mismatch is invariant under consistent Tate relabeling. Fractional leading powers at $n=3,4$ cannot arise from a semisimple direct source-native finite-rank $K$-compatible system retaining the two-weight decomposition and unchanged split-prime trace, although restriction of scalars and Galois counterpackets are not excluded. Clearing denominators leaves a formal odd expected-completion skeleton with exponents $6,4,3$. Finally, an exact $\chi_y$ calculation for the $n=4$ fivefold identifies a rank-two extreme Hodge piece as the next algebraic-projector gate. No $n=3,4$ Hasse--Weil functional equation or full Hénon completion is claimed.
author:
- Hénon Zeta Research Program
bibliography:
- references.bib
date: 14 August 2026
title: 'Weight--Clock Bifurcation in Cohomological Hénon Moments'
```

## Markdown 正文

# Introduction

A dynamical-zeta candidate can possess an exact Euler germ and an operator determinant without yet possessing the analytic structure relevant to a Hilbert--Pólya program. The missing data include a source-native archimedean completion, a functional equation, and a coherent reflection center. Classical Selberg and Ruelle zeta functions acquire such data from trace formulas or geometric spectral identities [@Selberg1956; @Ruelle1976]. The present arithmetic Hénon construction does not have an analogous global trace formula.

The preceding Hénon sequence retained a genuine chronological Fourier--cubic kernel, descended it through a normalized Galois trace, and obtained a normalized-semifinite regularized determinant. Its second, third, and fourth logarithmic moments were then identified with a genus-four curve, a Fano threefold packet, and a fivefold packet, respectively. Those identifications moved the normalized Euler object successively to $\operatorname{Re}s>1/3$, $\operatorname{Re}s>1/4$, and $\operatorname{Re}s>1/5$. The second moment was additionally resummed into modular elliptic factors. This paper asks the next large question: *do the three cohomological moments admit one standard completion without changing their prime clock?*

The answer has a positive and a negative part. The positive structure is a uniform pair of pure-weight packets. If $S_n$ is the Fermat cubic and $X_n$ is the source-ordered $(2,3)$ complete intersection, then $$E_n=\mathbf Q_\ell(0)\oplus H^{2n-2}_{\mathrm{prim}}(S_n)(n-1),
 \qquad
 O_n=H^{2n-3}(X_n)(n-2)$$ have weights zero and one, and the exact moment trace is their sum. Their total rank is $4^n-1$. This identity is a smooth-family theorem; the Hénon source is used only for $n=2,3,4$, where smoothness away from finite bad sets is inherited.

The negative structure comes from the clock rather than from a failure of purity. Field-degree normalization contributes $$\frac1{p-1}=\sum_{j\ge1}p^{-j},$$ so a standard factor is evaluated at $u=ns+j$. A pure weight-$w$ reflection consequently has center $$s_{n,j}(w)=\frac{(w+1)/2-j}{n}.$$ The leading odd factors align at zero, but the leading even factors do not, and later denominator terms split the odd factors. The exact second-moment factorization already proves this bifurcation with factors whose functional equations are known. Thus the obstruction does not rely on conjectural analytic continuation in the higher moments.

Three qualifications are essential. First, center zero is not itself incompatible with an RH normalization: recentering the completed Riemann $\xi$-function produces a reflection about zero [@DLMF]. Our obstruction is the *mismatch* of factorwise centers under one frozen clock. Second, the powers $2/3$ and $1/2$ are canonical $\operatorname{Log}_0$-germs in a nonvanishing Euler domain, not meromorphic roots. Third, the finite-rank no-go concerns a direct source-native $K$-compatible packet preserving the same split-prime trace. It does not classify restriction of scalars, Galois-orbit counterpackets, or the normalized-semifinite determinant already constructed.

The standard ingredients of the proof are classical. We use Deligne purity [@Deligne1974], weak Lefschetz [@SGA2], the hypersurface Jacobian-ring description [@Griffiths1969II], and Hirzebruch--Riemann--Roch [@Hirzebruch1995]. Serre and Deligne provide the motivic local-factor, Tate-shift, and expected-completion conventions [@Serre1970; @Deligne1979]. Buzzard--Gee and the automorphic normalization literature explain why half-sum shifts are legitimate in a different normalization category [@BuzzardGee2010; @SST2014]; they do not supply an ordinary half Tate motive preserving our coefficients. Regularized-product approaches to Gamma and local factors [@Quine1993; @Deninger1991; @Deninger1992] are close conceptual neighbors, but no full Hénon archimedean determinant is constructed here.

Our new contribution is the source-locked synthesis of these ingredients: the exact two-weight trace and rank identity, the forced exponent $2/n$, the complete center tower, a scoped direct-compatible-system obstruction, and an explicit Hodge projector gate. Standard product stability in motivic $\lambda$-rings [@Heinloth2007] explains why denominator-cleared products are natural, but it does not prove the functional equations of the present $n=3,4$ packets.

The paper is organized as follows. states the source and main theorem. proves the point-count and rank identities. extracts the leading cohomological logarithm. proves the weight--clock bifurcation and twist invariance. gives the rank obstruction and the surviving odd skeleton. computes the fivefold Hodge ledger, and records the Route-A status and claim boundary.

# The source and the main theorem {#sec:source}

Let $$K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0.$$ For $p>3$, $p\equiv1\pmod3$, choose one reduction of $\rho$ in $\mathbf F_p$. For $n\in\{2,3,4\}$, the source is the ordered $2n$-variable phase $$\label{eq:phase}
 \Phi_{p,n}(x_0,\ldots,x_{2n-1})
 =2\sum_{i=0}^{2n-1}x_i^3+
   \sum_{i=0}^{2n-2}x_ix_{i+1}+\rho x_{2n-1}x_0.$$ The last term is the chronological closing edge. We do not average it or replace it by a cyclic transition matrix.

Set $$Z_{p,n}=\#\Phi_{p,n}^{-1}(0),\qquad
 C_{p,n}=2p^{-(n-1)}Z_{p,n}-2p^n,$$ $$\label{eq:normalization}
 d_p=\frac{p-1}{2},\qquad c_{p,n}=\frac{C_{p,n}}{d_p}.$$ In $\mathbf P^{2n-1}$, write $$\mathcal C_n=\sum_{i=0}^{2n-1}x_i^3,\qquad
 \mathcal Q_{n,\rho}=\sum_{i=0}^{2n-2}x_ix_{i+1}
               +\rho x_{2n-1}x_0,$$ $$S_n=V(\mathcal C_n),\qquad Q_n=V(\mathcal Q_{n,\rho}),\qquad
 X_n=S_n\cap Q_n.$$ The predecessor source calculations prove the required smoothness for $n=2,3,4$ outside finite bad sets. Whenever we state a family formula for arbitrary $n$, smoothness of the displayed member is an explicit hypothesis.

We use geometric Frobenius and the convention that it acts by $p$ on $\mathbf Q_\ell(-1)$. Define $$\label{eq:packets}
 E_n=\mathbf Q_\ell(0)\oplus
 H^{2n-2}_{\mathrm{prim}}(S_{n,\overline K},\mathbf Q_\ell)(n-1),
 \qquad
 O_n=H^{2n-3}(X_{n,\overline K},\mathbf Q_\ell)(n-2).$$ Fix $S$ once and for all as the finite set of rational primes that ramify in $K$ or occur in the inherited source-defined bad-reduction sets for $n=2,3,4$.

[\[thm:main\]]{#thm:main label="thm:main"} At every good split prime and for $n=2,3,4$, the following statements hold.

1.  The packets $E_n$ and $O_n$ are pure of weights $0$ and $1$, respectively, and $$\label{eq:trace-main}
     C_{p,n}=-2\{\operatorname{Tr}(F_p\mid E_n)+\operatorname{Tr}(F_p\mid O_n)\}.$$

2.  For any smooth member of the displayed family, $$\operatorname{rank}E_n=\frac{4^n+5}{3},\qquad
     \operatorname{rank}O_n=\frac{2(4^n-4)}{3},\qquad
     \operatorname{rank}(E_n\oplus O_n)=4^n-1.$$

3.  Put $$\ell_n(s)=\sum_{p\equiv1(3)}c_{p,n}p^{-ns},\qquad
     F_n(s)=\exp(-\ell_n(s)/n).$$ There is a canonical holomorphic nonzero $H_{n,S}$ on $\operatorname{Re}s>0$ such that, initially for $\operatorname{Re}s>1/(2n)$, $$\label{eq:main-extraction}
     F_n(s)=
     \exp\!\left(\frac2n\operatorname{Log}_0
     L_K^{(S)}(E_n\oplus O_n,ns+1)\right)H_{n,S}(s).$$

4.  The exact denominator tower is $u_{n,j}=ns+j$, $j\ge1$. A pure weight-$w$ standard reflection maps to the center $$s_{n,j}(w)=\frac{(w+1)/2-j}{n}.$$ Consequently, the leading odd centers all equal $0$; the leading even centers and the higher odd centers are, respectively, $$\begin{gathered}
      \bigl(s_{2,1}(0),s_{3,1}(0),s_{4,1}(0)\bigr)
        =\bigl(-\tfrac14,-\tfrac16,-\tfrac18\bigr),\\
      s_{n,j}(1)=-\frac{j-1}{n}\qquad (j\ge2).
     \end{gathered}$$

5.  These centers are invariant under every consistent Tate relabeling. No semisimple finite-rank $K$-system in the direct source category can realize the factorwise fractional leading roots at $n=3,4$ while both retaining the $E_n/O_n$ weight decomposition and preserving the split-prime trace.

The final clause is categorical only within its stated source class. Restriction of scalars and Galois-orbit counterpackets change that class and are not excluded. The inherited normalized-semifinite determinant is also not excluded.

For $n=2$, the exact predecessor factorization is $$\label{eq:n2-factor}
 F_2(s)=\zeta_K(2s+1)^7
 L(H^1(C/K),2s+1)H_2(s).$$ The elliptic factors of $H^1(C)$ are modular over $K=\mathbf Q(\sqrt{-3})$ by [@CaraianiNewton2025 Theorem 1.1]; their standard automorphic analytic package follows from [@GodementJacquet1972 Global Theory, pp. 136--184]. These are the complete $n=2$ factors. On the initial Euler domain, passing between them and the incomplete factors in [\[eq:main-extraction\]](#eq:main-extraction){reference-type="eqref" reference="eq:main-extraction"} changes the residual only by the fixed standard local units, which are holomorphic and nonzero there. No corresponding theorem is invoked for $O_3$ or $O_4$.

The invariant packet is $$E_3=\mathbf Q_\ell(0)\oplus H^4_{\mathrm{prim}}(S_3)(2).$$ Over $K$, the primitive term has twenty normalized Tate lines and one rank-two non-Tate Jacobi packet. The extra trivial line gives twenty-one Tate lines in $E_3$. This is the classical Fermat/Jacobi decomposition [@Weil1952; @Brunjes2003]; it is not a claim that the entire primitive cohomology is Tate.

# Projective cancellation, weights, and ranks {#sec:weights}

## The four radial strata

For a nonzero direction $[x]\in\mathbf P^{2n-1}(\mathbf F_p)$, $$\Phi_{p,n}(tx)=t^2\{2t\mathcal C_n(x)+\mathcal Q_{n,\rho}(x)\}.$$ The nonzero roots are counted by four disjoint cases: $$\begin{array}{c|c}
\text{condition on }[x]&\text{number of nonzero }t\\ \hline
\mathcal C_n\ne0,\ \mathcal Q_{n,\rho}\ne0&1\\
\mathcal C_n\ne0,\ \mathcal Q_{n,\rho}=0&0\\
\mathcal C_n=0,\ \mathcal Q_{n,\rho}\ne0&0\\
\mathcal C_n=\mathcal Q_{n,\rho}=0&p-1.
\end{array}$$ It follows that $$\label{eq:radial}
\begin{aligned}
 Z_{p,n}
 &=1+\#\{\mathbf P^{2n-1}\setminus(S_n\cup Q_n)\}+(p-1)\#X_n\\
 &=1+P_{2n-1}-\#S_n-\#Q_n+p\#X_n,
\end{aligned}$$ where $P_m=1+p+\cdots+p^m$.

The quadric $Q_n$ is split in the source rows. Write $$\#S_n=P_{2n-2}+A_{p,n},\qquad
 \#Q_n=P_{2n-2}+p^{n-1},$$ $$\#X_n=P_{2n-3}-B_{p,n}.$$ Substitution in [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"} cancels every projective Tate polynomial: $$\label{eq:z-cancel}
 Z_{p,n}=p^{2n-1}-p^{n-1}-A_{p,n}-pB_{p,n}.$$ Therefore $$\label{eq:c-cancel}
 C_{p,n}=-2-\frac{2A_{p,n}}{p^{n-1}}
              -\frac{2B_{p,n}}{p^{n-2}}.$$

The two degree-one primes above a split $p$ give the same data. Indeed, $$x_0=\rho^2y_{2n-1},\qquad x_i=y_{i-1}\quad(1\le i\le2n-1)$$ preserves $\mathcal C_n$ and sends the $\rho$-closing quadric to the $\rho^2$-closing quadric.

## Purity and the trace identity

Because $S_n$ has even dimension $2n-2$, its primitive middle trace enters its point count with positive sign. Because $X_n$ has odd dimension $2n-3$, its middle trace enters with negative sign. Hence $$A_{p,n}=\operatorname{Tr}(F_p\mid H^{2n-2}_{\mathrm{prim}}(S_n)),\qquad
 B_{p,n}=\operatorname{Tr}(F_p\mid H^{2n-3}(X_n)).$$ After the twists in [\[eq:packets\]](#eq:packets){reference-type="eqref" reference="eq:packets"}, $$e_{p,n}=1+\frac{A_{p,n}}{p^{n-1}},\qquad
 o_{p,n}=\frac{B_{p,n}}{p^{n-2}}$$ are the traces of $E_n$ and $O_n$. Deligne's theorem [@Deligne1974 Theorem 1.6] makes the packets pure of weights zero and one. Equation [\[eq:c-cancel\]](#eq:c-cancel){reference-type="eqref" reference="eq:c-cancel"} becomes $$C_{p,n}=-2(e_{p,n}+o_{p,n}),$$ proving [\[eq:trace-main\]](#eq:trace-main){reference-type="eqref" reference="eq:trace-main"}. In particular, $$e_{p,n}=O(1),\qquad o_{p,n}=O(p^{1/2}).$$

## A conditional family identity

For a smooth cubic hypersurface in $\mathbf P^{2n-1}$, the primitive Hodge pieces are computed by the Jacobian ring $$R_n=\mathbf C[x_0,\ldots,x_{2n-1}]/(x_0^2,\ldots,x_{2n-1}^2),$$ whose Hilbert series is $(1+t)^{2n}$ [@Griffiths1969II §10, especially Theorem 10.8]. The resulting primitive middle Betti number is $$\label{eq:cubic-rank}
 b^{\mathrm{prim}}_{2n-2}(S_n)=\frac{4^n+2}{3}.$$

For a smooth $X_n=(2,3)\subset\mathbf P^{2n-1}$, the normal sequence gives $$c(TX_n)=\frac{(1+H)^{2n}}{(1+2H)(1+3H)},\qquad \deg X_n=6.$$ Thus $$\chi(X_n)=6[H^{2n-3}]
 \frac{(1+H)^{2n}}{(1+2H)(1+3H)}.$$ Using $$\frac1{(1+2H)(1+3H)}
 =-\frac2{1+2H}+\frac3{1+3H},$$ two finite binomial sums give $$[H^{2n-3}]
 \frac{(1+H)^{2n}}{(1+2H)(1+3H)}
 =\frac{3n+1-4^n}{9}.$$ Consequently, $$\chi(X_n)=\frac{2(3n+1-4^n)}3.$$ Weak Lefschetz [@SGA2 Exposé XIV, Corollaire 4.6] leaves only the odd middle Betti number undetermined and gives $$\label{eq:intersection-rank}
 b_{2n-3}(X_n)=(2n-2)-\chi(X_n)
 =\frac{2(4^n-4)}3.$$ Equations [\[eq:cubic-rank\]](#eq:cubic-rank){reference-type="eqref" reference="eq:cubic-rank"}--[\[eq:intersection-rank\]](#eq:intersection-rank){reference-type="eqref" reference="eq:intersection-rank"}, together with the trivial line in $E_n$, prove the rank assertions in .

    $n$   $\operatorname{rank}E_n$   $\operatorname{rank}O_n$   total
  ----- -------------------------- -------------------------- -------
      2                          7                          8      15
      3                         23                         40      63
      4                         87                        168     255

The computation can be replayed symbolically for larger $n$, but it is not a smoothness proof for the corresponding Hénon source members.

# The forced logarithmic $L$-extraction {#sec:logl}

Let $$L_K^{(S)}(V,u)=\prod_{\mathfrak p\nmid S}
 \det(1-F_{\mathfrak p}N\mathfrak p^{-u}
 \mid V^{I_{\mathfrak p}})^{-1}$$ be the incomplete standard cohomological Euler product for the frozen set $S$. An omitted standard factor may be restored only if it is holomorphic and nonzero on the stated domain; we do not absorb arbitrary rational local factors.

For every good split $p\notin S$, [\[eq:normalization\]](#eq:normalization){reference-type="eqref" reference="eq:normalization"} and [\[eq:trace-main\]](#eq:trace-main){reference-type="eqref" reference="eq:trace-main"} give $$\label{eq:cp-denominator}
 c_{p,n}=-\frac{4(e_{p,n}+o_{p,n})}{p-1}.$$ Let $$\ell_n^{(S)}(s)=
 \sum_{\substack{p\equiv1(3)\\p\notin S}}c_{p,n}p^{-ns}.$$ The finite source correction $$\label{eq:bad-source}
 B_{n,S}(s)=-\frac{\ell_n(s)-\ell_n^{(S)}(s)}n
 =-\frac1n\sum_{\substack{p\in S\\p\equiv1(3)}}
 c_{p,n}p^{-ns}$$ is an entire Dirichlet polynomial. For the good-prime sum, $$\label{eq:ell-expand}
 -\frac{\ell_n^{(S)}(s)}n
 =\frac4n\sum_{\substack{p\equiv1(3)\\p\notin S}}
 (e_{p,n}+o_{p,n})
 \sum_{j\ge1}p^{-ns-j}.$$ At a good split prime $p\notin S$, the two degree-one primes of $K$ have equal traces. The first Euler-logarithm term of $$\frac2n\operatorname{Log}_0L_K^{(S)}(E_n\oplus O_n,ns+1)$$ is hence $$\frac4n(e_{p,n}+o_{p,n})p^{-ns-1},$$ exactly the $j=1$ term of [\[eq:ell-expand\]](#eq:ell-expand){reference-type="eqref" reference="eq:ell-expand"}.

[\[prop:residual\]]{#prop:residual label="prop:residual"} The difference $$R_n(s)=-\frac{\ell_n(s)}n
 -\frac2n\operatorname{Log}_0L_K^{(S)}(E_n\oplus O_n,ns+1)$$ extends holomorphically to $\operatorname{Re}s>0$. Thus $H_{n,S}(s)=\exp(R_n(s))$ is holomorphic and nonzero there.

For $j\ge2$, the weight-one part left in [\[eq:ell-expand\]](#eq:ell-expand){reference-type="eqref" reference="eq:ell-expand"} is $$O(p^{-n\operatorname{Re}s-3/2}),$$ and the weight-zero part is smaller. For a split-prime Euler-logarithm power $m\ge2$, the worst weight-one term is $$O(p^{-mn\operatorname{Re}s-m/2}).$$ The $m=2$ prime sum is normally convergent for $\operatorname{Re}s>0$, and higher $m$ are better. At an inert rational prime outside $S$, the norm is $p^2$, so even its degree-one term satisfies the same boundary. Normal convergence proves the first assertion, and an exponential has no zeros. The remaining term $B_{n,S}$ in [\[eq:bad-source\]](#eq:bad-source){reference-type="eqref" reference="eq:bad-source"} is entire, and its exponential is also nonzero.

The original term in $\ell_n$ is $$O(p^{-n\operatorname{Re}s-1/2}),$$ so $\ell_n$ converges absolutely for $\operatorname{Re}s>1/(2n)$. Exponentiating the identity in proves [\[eq:main-extraction\]](#eq:main-extraction){reference-type="eqref" reference="eq:main-extraction"}.

For $n=3,4$, the notation suggested by [\[eq:main-extraction\]](#eq:main-extraction){reference-type="eqref" reference="eq:main-extraction"}, $$L_K^{(S)}(E_n\oplus O_n,ns+1)^{2/n},$$ means only $\exp((2/n)\operatorname{Log}_0L_K^{(S)})$ on the nonvanishing Euler domain. A local divisor need not be divisible by the denominator, so no single-valued meromorphic root or ordinary rational determinant is inferred.

At $n=2$, the exponent is integral and $E_2\simeq\mathbf Q_\ell(0)^7$, while $O_2=H^1(C)$. This gives the exact factorization [\[eq:n2-factor\]](#eq:n2-factor){reference-type="eqref" reference="eq:n2-factor"}. It will provide a theorem-level witness for the center obstruction in the next section.

# The weight--clock center tower {#sec:center}

For a pure weight-$w$ motive, the standard completed reflection is expected to relate $u$ and $w+1-u$ [@Serre1970 §1.3]. Deligne's conventions place the completed functional equation and Tate shifts in equations (1.2.3) and (3.1.2), respectively [@Deligne1979]. We use those conventions only to compute the *forced center*. Except at $n=2$, we do not promote the expected reflection to a theorem.

## The canonical index begins at one

Equation [\[eq:cp-denominator\]](#eq:cp-denominator){reference-type="eqref" reference="eq:cp-denominator"} contains the exact identity $$\frac1{p-1}=p^{-1}+p^{-2}+p^{-3}+\cdots.$$ Thus the canonical index is $$\label{eq:clock}
 j\ge1,\qquad u_{n,j}=ns+j.$$ If $ns'+j=w+1-(ns+j)$, then $$s'=\frac{w+1-2j}{n}-s.$$ The center of this reflection is $$\label{eq:center-map}
 s_{n,j}(w)=\frac{(w+1)/2-j}{n}.$$

For $j=1$, the three rows are:

   weight   $n=2$    $n=3$    $n=4$
  -------- -------- -------- --------
   $w=0$    $-1/4$   $-1/6$   $-1/8$
   $w=1$     $0$      $0$      $0$

For $w=1$ and $j\ge2$, $$s_{n,j}(1)=-\frac{j-1}{n}.$$ Therefore the leading odd rail aligns, the leading even rail bifurcates, and the full tower has no common factorwise standard pure-motive center.

## An unconditional two-factor witness

The factorization [\[eq:n2-factor\]](#eq:n2-factor){reference-type="eqref" reference="eq:n2-factor"} contains two completed factors whose analytic equations are known. The Dedekind zeta factor has weight zero and standard center $u=1/2$; under $u=2s+1$, its center is $$s=\frac{1/2-1}{2}=-\frac14.$$ The curve $H^1$ factor has weight one and standard center $u=1$; under the same clock its center is $s=0$. Thus a factorwise mismatch is already a theorem at $n=2$, independent of any conjectural $O_3$ or $O_4$ functional equation.

The completed Riemann function satisfies $\xi(s)=\xi(1-s)$; writing $\Xi(z)=\xi(1/2+z)$ gives a reflection about $z=0$ [@DLMF §§25.4 and 25.10]. A zero-centered variable is therefore entirely compatible with an RH formulation. The obstruction here is the simultaneous presence of distinct factorwise centers under the same locked clock.

## Tate and half-shift invariance

Let $V(k)$ be an integral Tate twist. It has weight $w-2k$. To preserve the same local source coefficient, the variable intercept changes from $j$ to $j-k$, because $L(V(k),u)=L(V,u+k)$. Hence $$\label{eq:twist-invariance}
 \frac{(w-2k+1)/2-(j-k)}n
 =\frac{(w+1)/2-j}{n}.$$ The center is invariant.

Automorphic unitary normalization and $C$-group conventions legitimately use half-sum shifts [@BuzzardGee2010; @SST2014]. Formally setting $k=1/2$ in [\[eq:twist-invariance\]](#eq:twist-invariance){reference-type="eqref" reference="eq:twist-invariance"} still leaves the center fixed. If one changes the weight but holds $u$ fixed, however, the eigenvalue is multiplied by $p^{\mp1/2}$. That operation changes the frozen Hénon coefficient and is not a repair of the same object.

[\[cor:center-no-go\]]{#cor:center-no-go label="cor:center-no-go"} No combination of consistent Tate relabelings gives the complete $E_n/O_n$ tower a common factorwise standard pure-motive center.

The corollary does not exclude a nonfactorwise identity in which additional source-derived factors cancel or reorganize the separate completions.

# Direct compatible systems and the odd survivor {#sec:compatible}

## A scoped finite-rank obstruction

The leading logarithmic factor in [\[eq:main-extraction\]](#eq:main-extraction){reference-type="eqref" reference="eq:main-extraction"} occurs with exponent $2/n$. Suppose it were the standard $L$-function of a semisimple direct source-native $K$-compatible system $W_n$ that preserved the same split-prime trace and retained the weight decomposition $E_n\oplus O_n$. Degree-one primes have density one in $K$. Equality of the leading traces there, Chebotarev density, and Brauer--Nesbitt give [@Serre1981] $$n[W_n]=2[E_n\oplus O_n]$$ in the semisimple representation ring. Purity separates the two weights, so the weightwise dimensions of $W_n$ would have to be $$\frac2n\operatorname{rank}E_n,\qquad \frac2n\operatorname{rank}O_n.$$ At $n=3$, these are $$\frac23(23,40)=\left(\frac{46}{3},\frac{80}{3}\right),$$ and at $n=4$, even the total dimension would be $$\frac12(87+168)=\frac{255}{2}.$$ Since the rank of an ordinary compatible system is an integer, the proposed direct $K$-packets do not exist.

This is not a universal compatible-system no-go. Restriction from $K$ to $\mathbf Q$ doubles ranks and changes the organization of primes and local traces. After that change the bare $n=4$ parity obstruction disappears: the half-multiplicities become $87$ and $168$. At $n=3$, the corresponding dimensions $92/3$ and $160/3$ remain nonintegral. Galois-orbit counterpackets, nonfactorwise identities, and the inherited normalized-semifinite determinant are outside the theorem.

## Denominator clearing

The leading odd exponents for $n=2,3,4$ are $$1,\qquad \frac23,\qquad \frac12.$$ Multiplication by their least common denominator $6$ gives the integer exponents $6,4,3$. Let $\Lambda(O_n,u)$ denote a standard completed weight-one factor whenever such a completion is known. Define the formal expected-completion skeleton $$\label{eq:odd-skeleton}
 \mathcal O_6(s)=
 \Lambda(O_2,2s+1)^6
 \Lambda(O_3,3s+1)^4
 \Lambda(O_4,4s+1)^3.$$ If all three factors satisfy their expected standard reflections $$\Lambda(O_n,u)=\varepsilon_n\Lambda(O_n,2-u),$$ then $$\mathcal O_6(s)=\varepsilon\,\mathcal O_6(-s).$$ This implication is exact, but its premise is proved here only for $O_2$. Equation [\[eq:odd-skeleton\]](#eq:odd-skeleton){reference-type="eqref" reference="eq:odd-skeleton"} is therefore a denominator-cleared formal skeleton, not a new Hasse--Weil theorem.

Product stability is natural in motivic $\lambda$-ring settings [@Heinloth2007 Proposition 6.1], but it presupposes factors that already possess the relevant rationality and functional equations. It does not construct the missing $O_3,O_4$ analytic packages.

## Why a formal Gamma product is insufficient

Serre's Hodge-theoretic Gamma ledger and Deligne's expected completion specify which finite products would accompany an individual pure motive [@Serre1970; @Deligne1979]. The complete Hénon denominator tower, however, produces an infinite list of shifted centers. Turning that list into a regularized product requires a spectral zeta function with a meromorphic continuation at the regularization point and fixed branch and multiplicity data. These are part of the definition of a zeta-regularized product [@Quine1993].

Deninger expressed motivic Gamma and local factors through regularized determinants [@Deninger1991; @Deninger1992]. This is an important structural precedent, but it does not license a determinant for an unconstructed Hénon archimedean spectrum. We therefore stop at the finite odd skeleton [\[eq:odd-skeleton\]](#eq:odd-skeleton){reference-type="eqref" reference="eq:odd-skeleton"}.

# The fivefold Hodge ledger and the next gate {#sec:hodge}

The primitive cubic Hodge pieces follow from the Jacobian ring, while the odd complete-intersection pieces follow from weak Lefschetz and Hirzebruch--Riemann--Roch. After the twists in [\[eq:packets\]](#eq:packets){reference-type="eqref" reference="eq:packets"}, the three rows are: $$\begin{array}{c|l}
E_2&(0,0)^7\\
O_2&(1,0)^4+(0,1)^4\\
E_3&(1,-1)^1+(0,0)^{21}+(-1,1)^1\\
O_3&(1,0)^{20}+(0,1)^{20}\\
E_4&(1,-1)^8+(0,0)^{71}+(-1,1)^8\\
O_4&(2,-1)^1+(1,0)^{83}+(0,1)^{83}+(-1,2)^1.
\end{array}$$ At the unique complex place of $K$, the corresponding expected Deligne--Serre Gamma ledger in the present motivic normalization is $$\Gamma_{\mathbf C}(u)=2(2\pi)^{-u}\Gamma(u),$$ and $$\begin{array}{c|l}
E_2&\Gamma_{\mathbf C}(u)^7\\
O_2&\Gamma_{\mathbf C}(u)^8\\
E_3&\Gamma_{\mathbf C}(u)^{21}\Gamma_{\mathbf C}(u+1)^2\\
O_3&\Gamma_{\mathbf C}(u)^{40}\\
E_4&\Gamma_{\mathbf C}(u)^{71}\Gamma_{\mathbf C}(u+1)^{16}\\
O_4&\Gamma_{\mathbf C}(u)^{166}\Gamma_{\mathbf C}(u+1)^2.
\end{array}$$ This is an expected sector Gamma ledger obtained from the Hodge types [@Serre1970; @Deligne1979]. It neither proves the $n=3,4$ functional equations nor defines an infinite Gamma product for the full Hénon denominator tower.

We give a finite independent derivation of the last line.

## The $\chi_y$ calculation

For $X_4=(2,3)\subset\mathbf P^7$, define the Hirzebruch characteristic series $$Q_y(x)=\frac{x(1+ye^{-x})}{1-e^{-x}}.$$ Hirzebruch--Riemann--Roch [@Hirzebruch1995] gives $$\label{eq:chiy-coefficient}
 \chi_y(X_4)=6[H^5]\,
 \frac{Q_y(H)^8}{(1+y)Q_y(2H)Q_y(3H)}.$$ Only terms through degree five contribute. The finite expansion $$Q_y(x)=(1+y)+\frac{1-y}{2}x+\frac{1+y}{12}x^2
 -\frac{1+y}{720}x^4+O(x^6)$$ in [\[eq:chiy-coefficient\]](#eq:chiy-coefficient){reference-type="eqref" reference="eq:chiy-coefficient"} yields $$\label{eq:chiy-value}
 \chi_y(X_4)=1-82y^2+82y^3-y^5.$$

Weak Lefschetz and Hodge symmetry leave two middle Hodge numbers $$a=h^{4,1}=h^{1,4},\qquad b=h^{3,2}=h^{2,3}.$$ In terms of $a,b$, the same genus is $$1+(a-1)y+(1-b)y^2+(b-1)y^3+(1-a)y^4-y^5.$$ Comparing with [\[eq:chiy-value\]](#eq:chiy-value){reference-type="eqref" reference="eq:chiy-value"} gives $$a=1,\qquad b=83.$$ Twisting $H^5(X_4)$ by $2$ proves the displayed $O_4$ row.

## The C52 projector gate

The types $(2,-1)$ and $(-1,2)$ show that $O_4$ is not itself the $H^1$ of an abelian variety. Its Hodge ledger nevertheless suggests a rank-two extreme part and a rank-166 level-one part: $$O_4^{\mathrm{ext}}:\ (2,-1)+(-1,2),\qquad
 O_4^{\mathrm{lev1}}:\ (1,0)^{83}+(0,1)^{83}.$$ A Hodge decomposition does not imply an algebraic splitting over $K$. Nor does a numerical projector at one prime define a compatible system.

[\[prop:c52-gate\]]{#prop:c52-gate label="prop:c52-gate"} The next positive route requires a $K$-rational algebraic correspondence whose induced projectors on all $\ell$-adic realizations are compatible and separate $O_4^{\mathrm{ext}}$ from $O_4^{\mathrm{lev1}}$. Absent such a construction, the appropriate negative target is a monodromy or endomorphism theorem obstructing that algebraic splitting.

is a research gate, not an existence theorem. It is large enough to change the analytic route: a rank-two extreme factor could be tested for a Hecke or automorphic realization, while the level-one factor could be compared with an abelian-type motive. Additional unstructured prime counting would not decide algebraicity.

# Route-A evaluation and Hilbert--Pólya scope {#sec:route}

C51 changes the structural evaluation, not the analytic half-plane. The normalized Euler object remains the one continued in the predecessor to $\operatorname{Re}s>1/5$. Its operator realization remains a tenth-order graded regularized determinant relative to the normalized faithful semifinite trace. The regularized-determinant background is standard [@Simon2005 Chapter 9]; the source-specific Schatten thresholds and counterterms are inherited rather than reproved here.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Gate   Verdict                      C51 evidence and boundary
  ------ ---------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A1     weak                         The four-, six-, and eight-step source chronology is exact, but split primes are arithmetic fibres rather than primitive orbits of one real map.

  A2     analytic determinant         The C50 continuation to $\operatorname{Re}s>1/5$ and $\operatorname{Det}_{10,\tau,\mathrm{gr}}$ are inherited; fractional cohomological powers are only $\operatorname{Log}_0$-germs.

  A3     partial analytic structure   Leading odd centers align and the $n=2$ component equations are proved; the even rail and higher tower do not align, and the full equation is open.

  A4     natural quantization         The unitary finite-place blocks, prime clock, and normalized trace are source-native; no self-adjoint global generator is constructed.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The exact evaluator tuple is $$\begin{gathered}
 \mathrm{A1\_WEAK},\qquad
 \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\\
 \mathrm{A4\_NATURAL\_QUANTIZATION}
\end{gathered}$$ with overall status $\mathrm{ROUTE\_A\_EXPLORATORY}$.

The A3 delta can be summarized without changing the enum: $$\begin{array}{ll}
\text{leading odd \(j=1\) center alignment}&\text{proved},\\
\text{full factorwise standard center}&\text{refuted},\\
\text{full denominator-tower alignment}&\text{refuted},\\
\text{direct \(K\)-packet repair at \(n=3,4\)}&\text{refuted in scope},\\
\text{\(n=2\) extracted factor equation}&\text{proved},\\
\text{\(n=3,4\) odd equations}&\text{open},\\
\text{full H\'enon functional equation}&\text{open}.
\end{array}$$

The paper proves no new zero-free region, no continuation through $\operatorname{Re}s=1/5$, no full Hénon Gamma factor, no Riemann divisor, and no Riemann--von Mangoldt law. The normalized-semifinite determinant is not a classical Fredholm determinant on the claimed half-plane. Route B is not authorized.

The next large door is . It is deliberately sharper than a request to compute more primes: construct a $K$-rational algebraic projector with $\ell$-compatible realizations, or prove a monodromy or endomorphism obstruction to it.

# Declarations and limitations {#declarations-and-limitations .unnumbered}

## Data and code availability {#data-and-code-availability .unnumbered}

The source equations, theorem and derivation packages, exact producer, independent checker, mutation tests, Route-A records, and compiled manuscript are released together in the repository directory *henon\_dynamics/henon\_mu3\_weight\_clock\_bifurcation*. No proprietary data, Riemann-zero table, or floating-point fit is used. Machine certificates replay finite symbolic identities and schema semantics; they do not replace the cited purity, Lefschetz, modularity, or Riemann--Roch theorems.

## Ethics statement {#ethics-statement .unnumbered}

This mathematical study involved no human participants, personal data, animals, clinical intervention, or biological material. Ethics approval and informed consent were not applicable.

## Author contributions (CRediT) {#author-contributions-credit .unnumbered}

The Hénon Zeta Research Program performed conceptualization, methodology, formal analysis, software, validation, investigation, data curation, and writing of the original draft and revisions. Claim promotion followed independent mathematical red-team, source-audit, producer/checker, and mutation-testing procedures.

## Funding {#funding .unnumbered}

No external funding was reported for this study.

## Conflict of interest {#conflict-of-interest .unnumbered}

The authoring research program reports no financial or nonfinancial conflict of interest.

## AI-use statement {#ai-use-statement .unnumbered}

AI systems were used for mathematical exploration, exact-code generation, primary-source triage, adversarial review, and manuscript drafting. AI output was not accepted as proof by itself. Theorem-level computational claims are backed by exact arithmetic and replayable certificates, and external mathematical inputs are assigned to cited primary sources. No AI system is listed as a human author.

## Limitations {#limitations .unnumbered}

The construction has six principal limitations. First, split primes index arithmetic fibres, not primitive cycles of one classical Hénon map. Second, the common-center result applies only to the leading odd rail; the even rail and later denominator terms bifurcate. Third, the $n=3,4$ odd functional equations are expected rather than proved. Fourth, the finite-rank obstruction applies only to semisimple direct source-native $K$-packets retaining the two-weight decomposition and trace. Restriction of scalars, Galois counterpackets, and nonfactorwise identities remain open. Fifth, the inherited continuation may have zeros and stops at $\operatorname{Re}s>1/5$. Sixth, no full archimedean completion, self-adjoint operator, Riemann divisor, or zero-counting law is constructed.

# Finite exact replay formulas {#app:replays}

This appendix records the finite algebra required by the release checker. It does not replace the external geometric theorems cited in the text.

## Rank controls

For a smooth family member, the exact rank formulas are $$\begin{array}{c|ccc}
n&b^{\mathrm{prim}}(S_n)&b^{\mathrm{mid}}(X_n)&
\operatorname{rank}(E_n\oplus O_n)\\ \hline
2&6&8&15\\
3&22&40&63\\
4&86&168&255.
\end{array}$$ The general identities $$b^{\mathrm{prim}}(S_n)=\frac{4^n+2}{3},\qquad
 b^{\mathrm{mid}}(X_n)=\frac{2(4^n-4)}{3}$$ may be checked by finite polynomial arithmetic. Symbolic controls for $n>4$ certify the formula conditional on smoothness; they do not certify source smoothness.

## Center controls

With $j\ge1$, $$s_{n,j}(w)=\frac{(w+1)/2-j}{n}.$$ The leading center spectrum is exactly $$\left\{-\frac14,-\frac16,-\frac18,0\right\}.$$ The mutation $j=0$ changes the source denominator expansion and must be rejected. The consistent twist mutation $$(w,j)\mapsto(w-2k,j-k)$$ must leave every center unchanged, while a fixed-clock half-weight mutation must change the local coefficient and be rejected.

## Hodge control

Truncate $$Q_y(x)=(1+y)+\frac{1-y}{2}x+\frac{1+y}{12}x^2
 -\frac{1+y}{720}x^4+O(x^6)$$ at degree five and evaluate $$6[H^5]\frac{Q_y(H)^8}{(1+y)Q_y(2H)Q_y(3H)}.$$ The exact output is $$1-82y^2+82y^3-y^5.$$ Comparing with the weak-Lefschetz template recovers $$h^{4,1}=1,\qquad h^{3,2}=83.$$

## Checker scope

The independent checker is required to fail closed on altered trace signs, rank formulas, tower indexing, center values, Tate shifts, fractional-root scope, Hodge coefficients, unknown schema keys, and overclaim fields. It does not rederive Deligne purity, weak Lefschetz, the modularity theorem, or an $n=3,4$ Hasse--Weil functional equation.
