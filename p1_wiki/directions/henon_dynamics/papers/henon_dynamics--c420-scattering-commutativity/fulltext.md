---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c420-scattering-commutativity"
canonical_tex: "henon_dynamics/research_c419_c423/papers/C420_scattering_commutativity/paper/main.tex"
canonical_pdf: "henon_dynamics/research_c419_c423/papers/C420_scattering_commutativity/main.pdf"
source_sha256: "44f5150ce545c5a6b801e848c9f85393eb6f5122608c6d74206bdb8d0415050f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# When do the cusp scattering matrices of $\Gamma_0(N)$ commute?

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c419_c423/papers/C420_scattering_commutativity>)
- [规范 TeX](<../../../../../henon_dynamics/research_c419_c423/papers/C420_scattering_commutativity/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c419_c423/papers/C420_scattering_commutativity/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c419_c423/papers/C420_scattering_commutativity/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c419_c423/papers/C420_scattering_commutativity/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify all positive integers $N$ for which the complete weight-zero, trivial-character cusp scattering matrices of $\Gamma_0(N)$, in fixed width-one cusp coordinates, commute at every pair of regular complex parameters. The criterion requires every primitive character whose conductor square divides $N$ to have real square. It also requires real character values at unramified divisor primes, but only when their exponents in $N$ are odd. We convert these conditions into explicit prime-exponent bounds and conditional congruences modulo five and eight. The proof starts from classical Eisenstein-series reconstruction formulas and uses a fixed Fourier transform on the cusp residue groups. A determinant quotient detects nonreal squares through a Dirichlet coefficient at a prime outside the level, even when the character square is imprimitive. For real squares, an explicit all-exponent principal basis reduces the remaining obstruction to the exchange of two central channels at odd exponent. A tensor lemma excludes cancellation between primes. In particular, the full family at level $50$ is noncommuting, whereas that at level $100$ commutes.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  When do the cusp scattering matrices of\
  $\Gamma_0(N)$ commute?
```

## Markdown 正文

# Introduction and classification {#sec:introduction}

Explicit scattering formulas do not by themselves give a basis of cusp channels that works at every spectral parameter. The usual changes from cusp Eisenstein series to character oldforms depend on that parameter; using such a change separately at two values does not preserve a commutator. This distinction is already visible in the contrast between levels $50$ and $100$. Both contain the same quartic conductor-five characters, but only the first has a noncommuting full scattering family.

For a positive integer $N$, let $\Phi_N(s)$ denote the complete cusp scattering matrix of $\Gamma_0(N)$, with weight zero, trivial nebentypus and width-one cusp scalings. We fix the cusp coordinates independently of $s$. A *regular parameter* is a point where every entry of the actual meromorphic matrix $\Phi_N$ is holomorphic. Our convention for its rows and constant terms is specified in [2](#sec:fixed){reference-type="ref" reference="sec:fixed"}.

[\[thm:levels\]]{#thm:levels label="thm:levels"} For every positive integer $N$, the identity $$[\Phi_N(s),\Phi_N(t)]=0$$ holds for every pair of regular complex parameters $s,t$ if and only if all three conditions below hold:

1.  $$v_2(N)\le9,\qquad v_3(N)\le3,\qquad v_5(N)\le3,\qquad
     v_p(N)\le1\quad(p\ge7).$$

2.  If $v_5(N)\ge2$, then every prime $p\ne5$ with odd $v_p(N)$ satisfies $p\equiv\pm1\pmod5$.

3.  If $v_2(N)\ge8$, then every odd prime $p$ with odd $v_p(N)$ satisfies $p\equiv\pm1\pmod8$.

The empty conditions include $N=1$.

The modulo-five restriction includes the prime two when its exponent is odd; neither congruence is imposed at an even exponent. The analytic form of the answer explains this asymmetry.

[\[thm:characters\]]{#thm:characters label="thm:characters"} The family $\Phi_N(s)$ is pairwise commuting at all regular parameters if and only if every primitive Dirichlet character $\chi$, of conductor $q$ with $q^2\mid N$, satisfies $$\begin{aligned}
 \chi^2&=\bar\chi^2,\label{eq:real-square-condition}\\
 \chi(p)&\in\{1,-1\}
 \quad\text{if }p\mid N,\ p\nmid q,\text{ and }v_p(N)\text{ is odd}.
 \label{eq:phase-condition}\end{aligned}$$ The character of conductor one is included. The first condition is equivalently $\chi^4=1$ on the unit group.

There are two distinct necessary conditions in this theorem. A nonreal square creates a scalar obstruction that persists at every larger level in which the primitive character occurs. When the square is real but the character has order four, an imaginary unramified value creates a matrix obstruction only at odd exponent. The proof establishes both statements on the full cusp space and then proves the converse. The explicit arithmetic reformulation is a finite unit-group calculation.

## Classical inputs and the remaining question

Huxley's congruence scattering calculations are the foundational provenance for the explicit formulas [@Huxley1984]. We use the cusp and character conventions and inversion formulas of @Young2019 [Sections 3, 6 and 7]; an independently derived reconstruction appears in @BookerLeeStrombergsson2020 [Section 2.7, Lemma 2.19 and Remark 2.20]. These sources own the Eisenstein-series machinery used below. In particular, the fixed character-weighted cusp sums are classical, as are the parameter-dependent oldform coefficient matrices.

For squarefree levels, the prime matrices and tensor formula already give fixed sum/difference channels; see @CakoniChanillo2019 [Theorem 2.8] and @LevitinStrohmaier2021 [equation (19)]. The squarefree conclusion is therefore a classical positive case, not the contribution of the present classification. An earlier squarefree channel argument in the surrounding project is deducted for the same reason. The present question retains every cusp at arbitrary level, rather than asking only about its principal sector. The distinction is summarized in [1](#tab:ownership){reference-type="ref" reference="tab:ownership"}.

::: {#tab:ownership}
  Classical input                                                                         Role and remaining question
  --------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  Full scattering reconstruction [@Huxley1984; @Young2019; @BookerLeeStrombergsson2020]   Supplies cusp/character changes and functional equations. The incoming oldform change depends on the spectral parameter.
  Squarefree local matrices [@CakoniChanillo2019; @LevitinStrohmaier2021]                 Give fixed sum/difference channels. They do not decide the effect of arbitrary conductor squares and unramified oldform exponents.
  Dirichlet functional equations and finite abelian duality                               Supply scalar and arithmetic tools. The full classification also needs the outside-level determinant obstruction and exact local parity test.

  : Ownership of the main inputs. The contribution is the complete fixed-coordinate criterion, not the formulas or individual elementary lemmas.
:::

The analysis below does not introduce new scattering formulas, a new Dirichlet functional equation or a new theory of character duality. Its content is the complete necessity-and-sufficiency test after those inputs are fixed: the nonreal-square obstruction, the exact quartic phase boundary, and the proof that tensor factors cannot conceal either obstruction. The small levels $50$ and $100$, and the principal diagonalization taken alone, are components of that answer.

The source comparison is bounded. Huxley's full chapter was not available during preparation; its role is credited through the inspected later primary derivations. Keil's dissertation [@Keil2007] is relevant broader matrix-structure context, but only its metadata and specified opening material in the source audit were inspected, not all chapters. No claim that those unread texts lack a consequence equivalent to the present criterion is made. We do not claim worldwide priority from a failed keyword search.

## Proof organization

Section [2](#sec:fixed){reference-type="ref" reference="sec:fixed"} identifies the actual scattering blocks by a fixed cusp Fourier transform. Section [3](#sec:principal){reference-type="ref" reference="sec:principal"} proves the principal all-exponent matrix lemma, including its two central eigenchannels at odd exponent. Section [4](#sec:nonreal){reference-type="ref" reference="sec:nonreal"} proves necessity of real squares without dropping imprimitive Euler factors. Section [5](#sec:parity){reference-type="ref" reference="sec:parity"} proves the exact phase test and assembles [\[thm:characters\]](#thm:characters){reference-type="ref" reference="thm:characters"}. Section [6](#sec:arithmetic){reference-type="ref" reference="sec:arithmetic"} proves [\[thm:levels\]](#thm:levels){reference-type="ref" reference="thm:levels"}, and Section [7](#sec:examples){reference-type="ref" reference="sec:examples"} treats the two boundary levels explicitly.

# Fixed cusp coordinates and exact character blocks {#sec:fixed}

Write $\Gamma=\Gamma_0(N)$. For each cusp $\mathfrak a$, choose a scaling matrix $\sigma_{\mathfrak a}\in\mathrm{SL}_2(\mathbb R)$ with $\sigma_{\mathfrak a}\infty=\mathfrak a$ and $$\sigma_{\mathfrak a}^{-1}\Gamma_{\mathfrak a}\sigma_{\mathfrak a}
 =\left\{\pm\begin{pmatrix}1&n\\0&1\end{pmatrix}:n\in\mathbb Z\right\}.$$ The standard incoming Eisenstein series, initially for $\Re s>1$, is $$E_{\mathfrak a}(z,s)=
 \sum_{\gamma\in\Gamma_{\mathfrak a}\backslash\Gamma}
       \bigl(\Im(\sigma_{\mathfrak a}^{-1}\gamma z)\bigr)^s .$$ Its constant term at $\mathfrak b$ is $$E_{\mathfrak a}(\sigma_{\mathfrak b}(x+iY),s)
 =\delta_{\mathfrak a\mathfrak b}Y^s+
   \Phi_N(s)_{\mathfrak a\mathfrak b}Y^{1-s}
   +\text{nonconstant Fourier terms}.$$ This defines the row convention used throughout. Changing the order of cusps or applying another fixed similarity preserves pairwise commutativity. Transposing the convention does too. An $s$-dependent renormalization is not part of the problem.

## The full finite Fourier transform

For $f\mid N$, put $g_f=(f,N/f)$. The cusps with denominator label $f$ can be represented as $1/(uf)$, where $u\in(\mathbb Z/g_f\mathbb Z)^\times$ is chosen coprime to $N$ [@Young2019 Section 5.2]. Fix a primitive character $\chi$ of conductor $q$, with $q^2\mid N$, and put $$L=N/q^2,\qquad d=\#\{B:B\mid L\}.$$ For $f=qg$, $g\mid L$, define $$\label{eq:Fourier}
 D_{\chi,f}(z,s)=
 \sum_{u\in(\mathbb Z/g_f\mathbb Z)^\times}\chi(-u)E_{1/(uf)}(z,s).$$ The character in this sum is the pullback of the primitive character to the indicated unit group.

[\[lem:full-Fourier\]]{#lem:full-Fourier label="lem:full-Fourier"} The rows in [\[eq:Fourier\]](#eq:Fourier){reference-type="eqref" reference="eq:Fourier"}, over all $q,\chi,f$ as above, form an invertible fixed coordinate change $T$ on the entire cusp space.

For a fixed $f$, each character of $(\mathbb Z/g_f\mathbb Z)^\times$ is induced by one and only one primitive character of conductor $q\mid g_f$. The condition $q\mid g_f$ is equivalent to $f=qg$ with $g\mid N/q^2$. Finite character orthogonality therefore says that the rows at this $f$ are exactly a full Fourier basis. Taking their direct sum over every divisor $f$ gives $T$. Its entries are character values, independent of $s$. Multiplication by the nonzero constants $\chi(-1)$ changes no invertibility statement.

## The incoming coefficient matrices

In Young's notation set $E_\chi=E_{\chi,\chi}$. This is the trivial nebentypus choice: the nebentypus of $E_{\chi_1,\chi_2}$ is $\chi_1\bar\chi_2$, while its completion contains $L(2s,\chi_1\chi_2)$. Define column vectors $$\mathcal E_\chi(s)=(E_\chi(Bz,s))_{B\mid L},\qquad
 D_\chi(s)=(D_{\chi,qg}(z,s))_{g\mid L}.$$ The classical inversion formula gives $$\label{eq:incoming}
 \mathcal E_\chi(s)=C_\chi(s)D_\chi(s).$$ For precision, the specialization of @Young2019 [equation (7.3)] used here writes $L=AB$ and sums over $d_0\mid A,\ e_0\mid B,\ (d_0,e_0)=1$. Its term has denominator and coefficient $$\label{eq:Young-summand}
 f=qBd_0/e_0,\qquad
 \frac{\chi(d_0)\chi(e_0)}{(d_0e_0)^s}
 \left(\frac{N}{(qBd_0/e_0,qAe_0/d_0)}\right)^s .$$ This explicitly imported formula, with its functional equation below, is the only scattering reconstruction needed for the argument.

[\[lem:local-incoming\]]{#lem:local-incoming label="lem:local-incoming"} Order the divisor labels multiplicatively. For $p\mid N$, set $a=v_p(q)$, $e=v_p(L)$, and let $0\le b,k\le e$ index $v_p(B)$ and $v_p(f/q)$. Then $$\label{eq:tensor-C}
 C_\chi(s)=\bigotimes_{p\mid N}C_{\chi,p}(s),$$ where the ramified factor is $$\label{eq:ramified-C}
 C_{\chi,p}(s)=
 \mathop{\mathrm{diag}}_{0\le b\le e}p^{s(a+\max(b,e-b))}
 \quad (a>0),$$ and, when $a=0$, the factor is $$\label{eq:unramified-C}
 C_{\chi,p}(s)_{b,k}
 =c^{|b-k|}p^{s(\max(k,e-k)-|b-k|)},\qquad c=\chi(p).$$ Every factor is generically invertible.

All parts of [\[eq:Young-summand\]](#eq:Young-summand){reference-type="eqref" reference="eq:Young-summand"} factor prime by prime. For the fixed pair $b,k$, coprimality forces $$v_p(d_0)=\max(k-b,0),\qquad
 v_p(e_0)=\max(b-k,0).$$ The gcd in [\[eq:Young-summand\]](#eq:Young-summand){reference-type="eqref" reference="eq:Young-summand"} has valuation $a+\min(k,e-k)$. Since $v_p(N)=2a+e$, its quotient contributes $p^{s(a+\max(k,e-k))}$. The denominator $(d_0e_0)^s$ contributes $p^{-s|b-k|}$.

If $a>0$, the character vanishes at $p$, so the term is zero unless $b=k$. This gives [\[eq:ramified-C\]](#eq:ramified-C){reference-type="eqref" reference="eq:ramified-C"}. If $a=0$, its character factor is $c^{|b-k|}$, giving [\[eq:unramified-C\]](#eq:unramified-C){reference-type="eqref" reference="eq:unramified-C"}. The prime choices are independent, which proves [\[eq:tensor-C\]](#eq:tensor-C){reference-type="eqref" reference="eq:tensor-C"}. Writing $T_e(z)_{b,k}=z^{|b-k|}$, the last matrix is $$T_e(cp^{-s})\mathop{\mathrm{diag}}_k p^{s\max(k,e-k)}.$$ Subtracting $z$ times row $j-1$ from row $j$, in descending order $j=e,\ldots,1$, gives $\det T_e(z)=(1-z^2)^e$. Its determinant is not identically zero. The diagonal factors in [\[eq:ramified-C\]](#eq:ramified-C){reference-type="eqref" reference="eq:ramified-C"} are everywhere nonzero.

The conductor powers in [\[eq:ramified-C\]](#eq:ramified-C){reference-type="eqref" reference="eq:ramified-C"} are retained. In particular, no $q^s$ factor is removed without being accounted for. For $N=1$, the empty tensor product is the one-by-one identity.

## Functional equations and actual scattering

Write $\tau(\chi)$ for the primitive Gauss sum; it is nonzero. The completion and functional equation in @Young2019 [completion before Proposition 4.1 and Proposition 4.2] specialize to $$\begin{aligned}
 A_\chi(s)&=\frac{(q/\pi)^s\Gamma(s)L(2s,\chi^2)}{\tau(\chi)},
 \label{eq:completion}\\
 A_\chi(s)\mathcal E_\chi(s)
 &=A_{\bar\chi}(1-s)\mathcal E_{\bar\chi}(1-s).
 \label{eq:FE}\end{aligned}$$ All identities are meromorphic. Set $$a_\chi(s)=\frac{A_{\bar\chi}(1-s)}{A_\chi(s)},\qquad
 U_\chi(s)=C_\chi(s)^{-1}C_{\bar\chi}(1-s).$$ Equations [\[eq:incoming\]](#eq:incoming){reference-type="eqref" reference="eq:incoming"} and [\[eq:FE\]](#eq:FE){reference-type="eqref" reference="eq:FE"} give $$\label{eq:fixed-FE}
 D_\chi(s)=a_\chi(s)U_\chi(s)D_{\bar\chi}(1-s).$$

[\[prop:paired-blocks\]]{#prop:paired-blocks label="prop:paired-blocks"} In the fixed coordinates $T$, each nonreal conjugate pair contributes the block $$\label{eq:paired-block}
 \mathcal B_\chi(s)=
 \begin{pmatrix}
 0&a_\chi(s)U_\chi(s)\\
 a_{\bar\chi}(s)U_{\bar\chi}(s)&0
 \end{pmatrix}.$$ A real character contributes the single block $$a_\chi(s)C_\chi(s)^{-1}C_\chi(1-s).$$ These are all blocks of $T\Phi_N(s)T^{-1}$.

At every width-one cusp, compare the $Y^{1-s}$ coefficients in [\[eq:fixed-FE\]](#eq:fixed-FE){reference-type="eqref" reference="eq:fixed-FE"}. On the left they form the corresponding rows of $T\Phi_N(s)$. On the right the incoming coefficients of $D_{\bar\chi}(1-s)$ are precisely the corresponding fixed rows of $T$. Therefore the coefficient matrix in [\[eq:fixed-FE\]](#eq:fixed-FE){reference-type="eqref" reference="eq:fixed-FE"} is the indicated block of $T\Phi_N(s)T^{-1}$, not a redefined scattering object. Combining the conjugate equations gives [\[eq:paired-block\]](#eq:paired-block){reference-type="eqref" reference="eq:paired-block"}. If $\chi=\bar\chi$, there is one sector and no second copy. Completeness follows from [\[lem:full-Fourier\]](#lem:full-Fourier){reference-type="ref" reference="lem:full-Fourier"}.

The matrices $C_\chi(s)$ in this proof depend on $s$. They compare incoming data in a functional equation and are never used as fixed similarities. The actual coordinate change throughout is $T$.

# A fixed basis for every principal oldform chain {#sec:principal}

We now prove the local algebra needed in the real-square sectors. Let $p>1$ be a prime, $e\ge0$, and $X\in\mathbb C^\times$. Put $Y=p/X$, $R=Y/X=p/X^2$, and $$\label{eq:principal-C}
 C_e(X)_{j,a}=X^{r_a-|j-a|},\qquad
 r_a=\max(a,e-a),\qquad 0\le j,a\le e.$$ Define the rational matrix family $$P_{p,e}(X)=C_e(X)^{-1}C_e(Y)$$ generically and then meromorphically. The variables $X,Y$ in this section may be arbitrary nonzero complex numbers with product $p$. This freedom will allow $X=p^s/\chi(p)$ in the phase calculation.

[\[prop:principal-basis\]]{#prop:principal-basis label="prop:principal-basis"} For every $p,e$, the family $P_{p,e}(X)$ has a full basis independent of $X$ that diagonalizes it at every regular value. The basis and its eigenvalues are given in the proof below.

## Invertibility, reversal and the difference channels

Let $\mathbf e_0,\ldots,\mathbf e_e$ be the coordinate vectors and let $J\mathbf e_a=\mathbf e_{e-a}$. Factoring [\[eq:principal-C\]](#eq:principal-C){reference-type="eqref" reference="eq:principal-C"} as $$C_e(X)=(X^{-|j-a|})_{j,a}\mathop{\mathrm{diag}}_a X^{r_a}$$ and using the row elimination of [\[lem:local-incoming\]](#lem:local-incoming){reference-type="ref" reference="lem:local-incoming"} gives $$\label{eq:principal-det}
 \det C_e(X)=X^{\sum_a r_a}(1-X^{-2})^e .$$ Also $C_e(X)J=JC_e(X)$ because both $r_a$ and the distance $|j-a|$ are preserved by simultaneous reversal.

Put $m=\lfloor e/2\rfloor$ and $d_a=\mathbf e_a-\mathbf e_{a+1}$. For $0\le b\le m-1$, define the fixed vectors $$\label{eq:difference-vectors}
 v_b^L=\sum_{a=0}^b p^a d_a,\qquad v_b^R=Jv_b^L.$$ Direct subtraction of columns, for $0\le a<m$, gives $$(C_e(X)d_a)_j=
 \begin{cases}
 (X^2-1)X^{e-2a+j-2},&0\le j\le a,\\
 0,&j>a.
 \end{cases}$$ Consequently $$\label{eq:difference-images}
 (C_e(X)v_b^L)_j=
 \begin{cases}
 (X^2-1)X^{e+j-2}\displaystyle\sum_{a=j}^b R^a,&0\le j\le b,\\
 0,&j>b.
 \end{cases}$$ Replacing $X$ by $Y$ replaces $R$ by $R^{-1}$, while $$\sum_{a=j}^b R^{-a}=R^{-(j+b)}\sum_{a=j}^b R^a .$$ Substitution in [\[eq:difference-images\]](#eq:difference-images){reference-type="eqref" reference="eq:difference-images"}, without division by any possibly vanishing finite sum, proves $$\label{eq:difference-eigenvalue}
 C_e(Y)v_b^L=\lambda_b(X)C_e(X)v_b^L,\qquad
 \lambda_b(X)=\frac{Y^2-1}{X^2-1}R^{e-2-b}.$$ The same identity holds for $v_b^R$ by reversal. These are the left and right difference eigenchannels of $P_{p,e}$.

## The even central channel

Suppose $e=2m$, $m\ge1$. Set $$\mu_a=\varphi(p^{\min(a,e-a)}),\qquad
 v^{\mathrm{cen}}=\sum_{a=0}^{2m}\mu_a\mathbf e_a,$$ where $\varphi(1)=1$. For $0\le j\le m$, the telescoping totient sum is $\sum_{a=0}^j\mu_a=p^j$. Summing the three ranges $a\le j$, $j<a\le m$, and $a>m$ in [\[eq:principal-C\]](#eq:principal-C){reference-type="eqref" reference="eq:principal-C"} therefore gives, for $0\le j<m$, $$\label{eq:even-Q}
 (C_e(X)v^{\mathrm{cen}})_j=p^jX^jQ_{m-j}(X),\qquad
 Q_h(X)=X^{2h}+(p-1)\sum_{b=1}^{h-1}p^{b-1}X^{2h-2b}+p^h.$$ At $j=m$, the image is $p^{m-1}(p+1)X^m$. The coefficients in [\[eq:even-Q\]](#eq:even-Q){reference-type="eqref" reference="eq:even-Q"} give the reciprocal identity $$Q_h(p/X)=p^hX^{-2h}Q_h(X).$$ Indeed the endpoint coefficients pair $1$ with $p^h$, and the interior coefficients pair by $(p-1)p^{h-b-1}=p^{h-2b}(p-1)p^{b-1}$. For every row $j\le m$, it follows that $$(C_e(Y)v^{\mathrm{cen}})_j
 =R^m(C_e(X)v^{\mathrm{cen}})_j .$$ Reversal gives the other rows. Thus the central eigenvalue is $R^m$. When $e=0$, the matrix is $(1)$ and the same conclusion holds with $m=0$ and $v^{\mathrm{cen}}=\mathbf e_0$.

## The two odd central channels

Now let $e=2m+1$, including $m=0$, and put $$\label{eq:odd-vectors}
 u_L=\sum_{a=0}^m\varphi(p^a)\mathbf e_a,\qquad
 u_R=Ju_L,\qquad v_\varepsilon=u_L+\varepsilon u_R
 \quad(\varepsilon=\pm1).$$ For $0\le j\le m$, set $h=m-j$. Range summation as above gives $$\begin{aligned}
 (C_e(X)v_\varepsilon)_j&=p^jX^jT_h^\varepsilon(X),
 \label{eq:odd-T}\\
 T_h^\varepsilon(X)&=
 X^{2h+1}+(p-1)\sum_{b=1}^h p^{b-1}X^{2h+1-2b}
       +\varepsilon p^h. \nonumber\end{aligned}$$ The sum is empty if $h=0$. Its value at $X=-\varepsilon$ is zero: the first two terms sum to $-\varepsilon p^h$. Hence $U_h^\varepsilon(X)=T_h^\varepsilon(X)/(X+\varepsilon)$ is a polynomial. Finite geometric summation also gives $$\label{eq:odd-U}
 U_h^\varepsilon(X)=
 \frac{X^{2h+2}-\varepsilon X^{2h+1}
       +\varepsilon p^hX-p^{h+1}}{X^2-p}.$$ Let the numerator be $Q(X)$. Directly, $$Q(p/X)=-p^{h+1}X^{-2h-2}Q(X),\qquad
 (p/X)^2-p=-pX^{-2}(X^2-p).$$ It follows that $$U_h^\varepsilon(p/X)=p^hX^{-2h}U_h^\varepsilon(X).$$ This is a polynomial identity after clearing powers of $X$; [\[eq:odd-U\]](#eq:odd-U){reference-type="eqref" reference="eq:odd-U"} does not introduce an exclusion at $X^2=p$. Restoring the factor $X+\varepsilon$ in [\[eq:odd-T\]](#eq:odd-T){reference-type="eqref" reference="eq:odd-T"} gives, first on the left half and then by reversal, $$\label{eq:central-eigenvalues}
 C_e(Y)v_\varepsilon
 =\lambda_\varepsilon(X)C_e(X)v_\varepsilon,\qquad
 \lambda_\varepsilon(X)=R^m\frac{Y+\varepsilon}{X+\varepsilon}.$$

## Completeness and fixed cusp normalization

We finish the proof of [\[prop:principal-basis\]](#prop:principal-basis){reference-type="ref" reference="prop:principal-basis"}. The vectors $v_b^L$ span the same space as $d_0,\ldots,d_{m-1}$: their coefficient matrix is triangular with nonzero diagonal entries $p^b$. The right-hand statement follows by reversal.

For $e=2m$, the left difference space consists of vectors supported on $[0,m]$ with coordinate sum zero. The right difference space has the analogous support $[m,2m]$. A vector in their intersection would be supported only at $m$ and have sum zero, so their intersection is trivial. Their sum has dimension $2m$, and $v^{\mathrm{cen}}$, whose coordinate sum is positive, lies outside it. These $e+1$ vectors form a fixed basis.

For $e=2m+1$, the support intervals $[0,m]$ and $[m+1,2m+1]$ are disjoint. Each difference space has codimension one on its interval. The respective vectors $u_L,u_R$, both of coordinate sum $p^m$, give the missing complements; their sum and difference are independent. Again there are $e+1$ fixed basis vectors. Equations [\[eq:difference-eigenvalue\]](#eq:difference-eigenvalue){reference-type="eqref" reference="eq:difference-eigenvalue"} and [\[eq:central-eigenvalues\]](#eq:central-eigenvalues){reference-type="eqref" reference="eq:central-eigenvalues"}, and the even central calculation, give all eigenvalues. Inverting $C_e(X)$ generically proves the diagonalization. Meromorphic continuation proves it at every regular value. Coincident eigenvalues do not affect independence of the explicit basis. This proves the proposition. $\square$

For clarity, this principal matrix has exactly the width-one normalization already present in [\[lem:local-incoming\]](#lem:local-incoming){reference-type="ref" reference="lem:local-incoming"}. A direct cusp calculation gives the same answer. At the cusp $u/p^a$, put $w_a=p^{e-\min(2a,e)}$ and choose $\gamma\in\mathrm{SL}_2(\mathbb Z)$ with first column $(u,p^a)^T$. Then $\sigma=\gamma\mathop{\mathrm{diag}}(\sqrt{w_a},1/\sqrt{w_a})$ is width-one. The dilation $z\mapsto p^jz$ has determinant-one matrix $\alpha_j=\mathop{\mathrm{diag}}(p^{j/2},p^{-j/2})$. With $g=p^{\min(a,j)}$, the first column of $\alpha_j\sigma$ is $g\sqrt{w_a/p^j}$ times the primitive column $(p^ju/g,p^a/g)^T$. Reducing that column by a matrix in $\mathrm{SL}_2(\mathbb Z)$ leaves an upper triangular matrix whose height multiplier is $$p^{e-\min(2a,e)+2\min(a,j)-j}
 =p^{r_a-|j-a|}.$$ Thus the incoming coefficient of the level-one oldform $E(p^jz,s)$ is $C_e(p^s)_{j,a}$; its outgoing coefficient is $\phi_1(s)C_e(p^{1-s})_{j,a}$, where $\phi_1$ is the level-one scattering scalar. This is also the principal specialization of @BookerLeeStrombergsson2020 [Lemma 2.19]; the different normalization of the primitive-pair series there is a common factor two that cancels.

The number of cusps in class $a$ is $\mu_a$. If the class sum of cusp series is divided by $\sqrt{\mu_a}$, then the reduced row scattering matrix becomes $$\phi_1(s)D_\mu^{-1/2}P_{p,e}(p^s)D_\mu^{1/2},
 \qquad D_\mu=\mathop{\mathrm{diag}}(\mu_0,\ldots,\mu_e).$$ Both normalizing matrices are fixed. At a composite principal level, $$C_N(s)_{d,c}
 =\left(\frac{N\gcd(d,c)^2}{d\gcd(c^2,N)}\right)^s
 =\bigotimes_{p\mid N} C_{v_p(N)}(p^s),$$ so the principal sector has the tensor product of the bases just proved. This statement concerns only that sector; it does not discard the nonprincipal blocks in [\[prop:paired-blocks\]](#prop:paired-blocks){reference-type="ref" reference="prop:paired-blocks"}.

# Why a nonreal square obstructs every larger level {#sec:nonreal}

We prove [\[eq:real-square-condition\]](#eq:real-square-condition){reference-type="eqref" reference="eq:real-square-condition"} is necessary. The main issue is that a primitive character can have an imprimitive square, and that extra oldform determinants can appear at primes dividing $N$. Neither effect can be omitted.

## The scalar ratio, including all missing Euler factors

Let $\chi$ be primitive of conductor $q$, with nonreal square $\eta=\chi^2$. Let $\xi$, of conductor $r$, be the primitive character inducing $\eta$, and set $$\mathcal P=\{p:p\mid q,\ p\nmid r\},\qquad
 d_0=\prod_{p\in\mathcal P}p.$$ The character $\xi$ is nonprincipal and even, since $\eta(-1)=1$. Define $$\label{eq:H-xi}
 H_\xi(s)=
 \prod_{p\nmid q}\frac{1-\xi(p)p^{-2s}}{1-\xi(p)p^{1-2s}}
 \prod_{p\in\mathcal P}
       \frac{1-\xi(p)p^{2-2s}}{1-\xi(p)p^{1-2s}}.$$

[\[lem:scalar-ratio\]]{#lem:scalar-ratio label="lem:scalar-ratio"} There is a nonzero constant $K_\chi$ such that $$\label{eq:scalar-ratio}
 \frac{a_\chi(s)}{a_{\bar\chi}(s)}
 =K_\chi\frac{H_\xi(s)}{H_{\bar\xi}(s)}.$$ Both products in [\[eq:H-xi\]](#eq:H-xi){reference-type="eqref" reference="eq:H-xi"} have absolutely convergent Dirichlet expansions in $n^{-2s}$ for $\Re s>1$, with constant coefficient one.

For a character induced from $\xi$, the missing-Euler-factor identity and primitive functional equation are the classical formulas in @DLMF2026 [equations 25.15.4--25.15.6]. Here they give $$L(u,\eta)=L(u,\xi)\prod_{p\in\mathcal P}(1-\xi(p)p^{-u}),$$ and, for the primitive even character, $$\left(\frac r\pi\right)^{u/2}\Gamma(u/2)L(u,\bar\xi)
 =\epsilon_{\bar\xi}
   \left(\frac r\pi\right)^{(1-u)/2}
   \Gamma((1-u)/2)L(1-u,\xi).$$ The constant $\epsilon_{\bar\xi}\ne0$ is its usual Dirichlet functional-equation constant.

From [\[eq:completion\]](#eq:completion){reference-type="eqref" reference="eq:completion"}, it is convenient to multiply the off-diagonal scalar by $q^{1-2s}$ and write $$\begin{aligned}
 h_\chi(s):=q^{1-2s}a_\chi(s)
 &=q^{1-2s}\frac{\tau(\chi)}{\tau(\bar\chi)}
   \left(\frac q\pi\right)^{1-2s}
   \frac{\Gamma(1-s)}{\Gamma(s)}
   \frac{L(2-2s,\bar\eta)}{L(2s,\eta)}.
 \label{eq:h-chi}\end{aligned}$$ Apply the primitive equation with $u=2-2s$. For each missing prime use the exact identity $$1-\bar\xi(p)p^{2s-2}
 =-\bar\xi(p)p^{2s-2}(1-\xi(p)p^{2-2s}).$$ The primitive quotient $L(2s-1,\xi)/L(2s,\xi)$, together with these factors, is precisely $H_\xi(s)$. All remaining $s$-dependent factors are independent of the choice of $\chi$ or $\bar\chi$. Explicitly, $$\begin{aligned}
 h_\chi(s)&=c_\chi V(s)H_\xi(s),\label{eq:h-factor}\\
 V(s)&=
 q^{1-2s}(q/\pi)^{1-2s}(r/\pi)^{2s-3/2}
 d_0^{\,2s-2}\frac{\Gamma(s-\tfrac12)}{\Gamma(s)},\nonumber\\
 c_\chi&=
 \frac{\tau(\chi)}{\tau(\bar\chi)}
 \epsilon_{\bar\xi}\prod_{p\in\mathcal P}(-\bar\xi(p)).
 \nonumber\end{aligned}$$ All constants in the last line are nonzero. Dividing the two identities [\[eq:h-factor\]](#eq:h-factor){reference-type="eqref" reference="eq:h-factor"} gives [\[eq:scalar-ratio\]](#eq:scalar-ratio){reference-type="eqref" reference="eq:scalar-ratio"}, since $q^{1-2s}$ cancels.

For $\Re s>1$, the infinite product over $p\nmid q$ is absolutely convergent: its first-order sizes are $O(p^{1-2\Re s})$. The remaining product is finite, and the geometric expansions of its denominators converge in the same half-plane. Their products therefore have absolutely convergent Dirichlet expansions, with constant coefficient one.

This computation retains every missing factor when $\eta$ is imprimitive. It does not apply a primitive functional equation directly to an imprimitive $L$-function. All separated gamma and $L$-factors are meromorphic identities, not instructions to evaluate a zero times a pole separately.

## The determinant obstruction

[\[prop:nonreal-obstruction\]]{#prop:nonreal-obstruction label="prop:nonreal-obstruction"} If $\Phi_N(s)$ is pairwise commuting, every primitive $\chi$ with $q^2\mid N$ has real square.

Suppose instead that such a $\chi$ has nonreal square. Put $L=N/q^2$ and $d=\#\{B:B\mid L\}$, as in [2](#sec:fixed){reference-type="ref" reference="sec:fixed"}. The upper-left block of the commutator in [\[eq:paired-block\]](#eq:paired-block){reference-type="eqref" reference="eq:paired-block"} must vanish: $$(a_\chi(s)U_\chi(s))(a_{\bar\chi}(t)U_{\bar\chi}(t))
 =
 (a_\chi(t)U_\chi(t))(a_{\bar\chi}(s)U_{\bar\chi}(s)).$$ Taking determinants and fixing a generic $t$ makes $$\label{eq:Delta}
 \Delta_\chi(s)=
 \left(\frac{a_\chi(s)}{a_{\bar\chi}(s)}\right)^d
 \frac{\det C_{\bar\chi}(s)\det C_{\bar\chi}(1-s)}
      {\det C_\chi(s)\det C_\chi(1-s)}$$ constant. Generic invertibility justifies the divisions; the result is a meromorphic identity.

For $p\mid L$, let $e_p=v_p(L)$. The determinant of the local factor in [\[eq:tensor-C\]](#eq:tensor-C){reference-type="eqref" reference="eq:tensor-C"} appears to the power $d/(e_p+1)$. Ramified factors [\[eq:ramified-C\]](#eq:ramified-C){reference-type="eqref" reference="eq:ramified-C"} cancel between conjugate characters. For $p\nmid q$, put $$c_p=\chi(p),\qquad n_p=\frac{e_pd}{e_p+1}\in\mathbb Z_{\ge0}.$$ The phase-sensitive part of its determinant contribution is $$\left[
 \frac{(1-\bar c_p^2p^{-2s})(1-\bar c_p^2p^{2s-2})}
      {(1-c_p^2p^{-2s})(1-c_p^2p^{2s-2})}
 \right]^{n_p}.$$ All powers from the diagonal coefficient factors cancel. Since $|c_p|=1$, removing a nonzero constant and setting $z=p^{-2s}$ changes this expression to $$\label{eq:finite-Euler}
 \left[
 \frac{(1-\bar c_p^2z)(1-c_p^2p^2z)}
      {(1-c_p^2z)(1-\bar c_p^2p^2z)}
 \right]^{n_p}.$$ Let $F_\chi(s)$ be their finite product. It is supported at primes dividing $N$ and has constant coefficient one. By [\[lem:scalar-ratio\]](#lem:scalar-ratio){reference-type="ref" reference="lem:scalar-ratio"}, $\Delta_\chi(s)$ is a nonzero constant times $$\label{eq:normalized-Delta}
 \left(\frac{H_\xi(s)}{H_{\bar\xi}(s)}\right)^d F_\chi(s).$$ For $\Re s>1$, this too has an absolutely convergent Dirichlet expansion in $n^{-2s}$, including the denominator expansions in [\[eq:finite-Euler\]](#eq:finite-Euler){reference-type="eqref" reference="eq:finite-Euler"}. It tends to one as real $s\to+\infty$. Its constancy forces it to equal one identically.

At a prime $\ell\nmid N$, the coefficient of $\ell^{-2s}$ in [\[eq:normalized-Delta\]](#eq:normalized-Delta){reference-type="eqref" reference="eq:normalized-Delta"} is $$\label{eq:outside-coefficient}
 d(\ell-1)\bigl(\xi(\ell)-\bar\xi(\ell)\bigr).$$ Indeed the factor at $\ell$ in $H_\xi$ begins $1+(\ell-1)\xi(\ell)\ell^{-2s}+\cdots$, and none of the finite level factors can contribute to this prime coefficient. Uniqueness of absolutely convergent Dirichlet series forces [\[eq:outside-coefficient\]](#eq:outside-coefficient){reference-type="eqref" reference="eq:outside-coefficient"} to vanish for every $\ell\nmid N$. For completeness, uniqueness follows by taking the least index with a nonzero coefficient in the difference of two series, multiplying by that index to the power $2s$, and letting real $s\to+\infty$. Absolute convergence in a fixed right half-plane controls the tail.

Choose a unit residue $a\bmod q$ with $\eta(a)$ nonreal. The Chinese remainder theorem supplies a positive integer $n$ with $$n\equiv a\pmod q,\qquad
 n\equiv1\pmod{\prod_{p\mid N,\ p\nmid q}p}.$$ It is coprime to $N$ and has $\eta(n)$ nonreal. At least one prime factor $\ell$ of $n$ has $\eta(\ell)=\xi(\ell)$ nonreal, since a product of real character values is real. That prime is outside $N$, contradicting [\[eq:outside-coefficient\]](#eq:outside-coefficient){reference-type="eqref" reference="eq:outside-coefficient"}. No theorem on the density of primes in residue classes is required.

# Real squares, local phases and tensor assembly {#sec:parity}

After [\[prop:nonreal-obstruction\]](#prop:nonreal-obstruction){reference-type="ref" reference="prop:nonreal-obstruction"}, every remaining character is real or has order four. We first isolate a tensor fact that prevents several noncommuting local factors from cancelling each other.

[\[lem:tensor\]]{#lem:tensor label="lem:tensor"} Let $A_1(s),\ldots,A_h(s)$ be meromorphic matrix families over $\mathbb C$, all generically invertible, and set $A(s)=\bigotimes_{j=1}^h A_j(s)$. Then $A(s)$ is pairwise commuting as a meromorphic family if and only if every $A_j(s)$ is pairwise commuting.

Sufficiency follows from multiplication of tensor products. For necessity, choose $s_0$ where all matrices are holomorphic and invertible, and work in a small connected neighborhood of $(s_0,s_0)$. Tensor commutativity gives $$\bigotimes_j R_j(s,t)=I,\qquad
 R_j(s,t)=A_j(s)A_j(t)\bigl(A_j(t)A_j(s)\bigr)^{-1}.$$ Taking the trace shows that each $\mathop{\mathrm{tr}}R_j$ is nonzero: their product is the positive dimension of the tensor space. Taking the partial trace over all factors except $j$ then makes $R_j$ scalar. Since $\det R_j=1$, that scalar belongs to the finite set of roots of unity of order dividing $\dim A_j$. It is continuous, so is constant on the chosen neighborhood. Its value at $(s_0,s_0)$ is one. Thus the local commutators vanish on an open set and therefore identically by meromorphic continuation.

## Real characters

If $\chi=\bar\chi$, each unramified value is $c=\pm1$. With $D_c=\mathop{\mathrm{diag}}(1,c,\ldots,c^e)$, the incoming factor satisfies $$C_{\chi,p}(s)=D_c C_e(p^s)D_c,
 \qquad D_c^2=I.$$ This follows from $c^{|j-a|}=c^{j+a}$. Hence the local scattering factor is a fixed conjugate of $P_{p,e}(p^s)$, and it commutes by [\[prop:principal-basis\]](#prop:principal-basis){reference-type="ref" reference="prop:principal-basis"}. Every ramified factor is diagonal by [\[eq:ramified-C\]](#eq:ramified-C){reference-type="eqref" reference="eq:ramified-C"}. The single character sector in [\[prop:paired-blocks\]](#prop:paired-blocks){reference-type="ref" reference="prop:paired-blocks"} is thus a scalar multiple of a commuting tensor product for every $L$. No restriction on the oldform exponents has been introduced.

## A constant reduction of the quartic paired sector

Suppose $\chi\ne\bar\chi$ but $\chi^2=\bar\chi^2$. Then $\chi$ has order four. The factors $a_\chi$ and $a_{\bar\chi}$ have a common meromorphic factor $k_\chi(s)$ and the reciprocal constants $$a_\chi(s)=k_\chi(s)\frac{\tau(\chi)}{\tau(\bar\chi)},\qquad
 a_{\bar\chi}(s)=k_\chi(s)\frac{\tau(\bar\chi)}{\tau(\chi)}.$$ This is immediate from [\[eq:completion\]](#eq:completion){reference-type="eqref" reference="eq:completion"} because the two square $L$-functions coincide. The common factor is not identically zero. Conjugation by the fixed block diagonal matrix $\mathop{\mathrm{diag}}(\tau(\chi)/\tau(\bar\chi)\,I_d,I_d)$ removes the two constant ratios from [\[eq:paired-block\]](#eq:paired-block){reference-type="eqref" reference="eq:paired-block"}.

For $p\nmid q$, put $$J_p=\mathop{\mathrm{diag}}_{0\le b\le e_p}(\chi(p)^2)^b,\qquad e_p=v_p(L);$$ for $p\mid q$, set $J_p=I$. Equations [\[eq:ramified-C\]](#eq:ramified-C){reference-type="eqref" reference="eq:ramified-C"} and [\[eq:unramified-C\]](#eq:unramified-C){reference-type="eqref" reference="eq:unramified-C"} give $$C_{\bar\chi,p}(s)=J_pC_{\chi,p}(s)J_p.$$ Here the parameter $s$ is not conjugated. With $J=\bigotimes_{p\mid N}J_p$, we have $U_{\bar\chi}(s)=JU_\chi(s)J$. The further fixed similarity $\mathop{\mathrm{diag}}(I_d,J)$ changes the paired block, after division by $k_\chi$, into $$\begin{pmatrix}0&\mathcal A_\chi(s)\\
                 \mathcal A_\chi(s)&0\end{pmatrix},$$ where $$\label{eq:global-A}
 \mathcal A_\chi(s)=U_\chi(s)J
 =C_\chi(s)^{-1}JC_\chi(1-s)
 =\bigotimes_{p\mid N}
       \bigl(C_{\chi,p}(s)^{-1}J_pC_{\chi,p}(1-s)\bigr).$$ A fixed two-block Walsh transform gives $\mathcal A_\chi(s)\oplus(-\mathcal A_\chi(s))$. Thus the quartic paired sector commutes exactly when $\mathcal A_\chi(s)$ does. Every factor in [\[eq:global-A\]](#eq:global-A){reference-type="eqref" reference="eq:global-A"} is generically invertible. All coordinate transformations used in this reduction are constant.

## The phase identity and its parity boundary

Fix an unramified prime. Write $e=v_p(L)$, $c=\chi(p)$, $x=p^s$, $y=p^{1-s}$, $r_a=\max(a,e-a)$, and $$C_c(x)_{j,a}=c^{|j-a|}x^{r_a-|j-a|}.$$ Since the square is real, $c\in\{1,-1,i,-i\}$. Define the constant diagonal matrices $$\kappa=c^2,\qquad
 D=\mathop{\mathrm{diag}}_j\kappa^j,\qquad
 H=\mathop{\mathrm{diag}}_a c^{r_a},\qquad
 F=\mathop{\mathrm{diag}}_a\kappa^{r_a+a}.$$ The local factor of [\[eq:global-A\]](#eq:global-A){reference-type="eqref" reference="eq:global-A"} is $A_c(s)=C_c(x)^{-1}DC_c(y)$.

[\[lem:phase-identity\]]{#lem:phase-identity label="lem:phase-identity"} With $X=x/c$, one has $$\label{eq:phase-identity}
 A_c(s)=H^{-1}P_{p,e}(X)F H.$$ If $c=\pm1$, or if $c=\pm i$ and $e$ is even, then $F=I$. If $c=\pm i$ and $e=2m+1$, then $F$ is minus the identity on coordinates $0,\ldots,m$ and the identity on $m+1,\ldots,2m+1$.

Put $V=y/c$. The entries give $$C_c(x)=C_e(X)H,\qquad C_c(y)=C_e(V)H.$$ Because $|j-a|\equiv j+a\pmod2$ and $\kappa=\pm1$, $$DC_e(V)=C_e(\kappa V)F.$$ Also $X\kappa V=p$. Substitution yields [\[eq:phase-identity\]](#eq:phase-identity){reference-type="eqref" reference="eq:phase-identity"}. If $\kappa=1$, $F=I$. If $\kappa=-1$, the exponent $r_a+a$ equals $e$ on the left half of the index interval and $2a$ on the right half. This gives the asserted even and odd cases.

[\[prop:local-parity\]]{#prop:local-parity label="prop:local-parity"} For real-square data, the local factor $A_c(s)$ is pairwise commuting except precisely when $c=\pm i$ and $e$ is odd.

When $F=I$, [\[lem:phase-identity,prop:principal-basis\]](#lem:phase-identity,prop:principal-basis){reference-type="ref" reference="lem:phase-identity,prop:principal-basis"} give a fixed diagonalizing basis, hence commutativity.

Let $c=\pm i$, $e=2m+1$. On the left and right difference eigenlines of [\[eq:difference-vectors\]](#eq:difference-vectors){reference-type="eqref" reference="eq:difference-vectors"}, $F$ acts by $-1$ and $+1$, respectively. On the central space [\[eq:odd-vectors\]](#eq:odd-vectors){reference-type="eqref" reference="eq:odd-vectors"}, it satisfies $$Fv_+=-v_-,\qquad Fv_-=-v_+.$$ Consequently the matrix of $P_{p,e}(X)F$ in the fixed central basis $(v_+,v_-)$ is $$\label{eq:odd-obstruction-block}
 \begin{pmatrix}0&-\lambda_+(X)\\
                 -\lambda_-(X)&0\end{pmatrix},\qquad
 \lambda_\pm(X)=\left(\frac{p}{X^2}\right)^m
                    \frac{p/X\pm1}{X\pm1}.$$ Neither off-diagonal entry is identically zero. Their ratio is $$\label{eq:rho}
 \rho_p(X)=\frac{(p+X)(X-1)}{(p-X)(X+1)}.$$ If this rational function were a constant $k$, comparison of quadratic coefficients would give $k=-1$, whereas comparison of linear coefficients would give $p-1=-(p-1)$. This is impossible for $p>1$. Since $X=p^s/c$ has nonzero derivative and takes values in an open set locally, the composed meromorphic ratio is nonconstant.

For an off-diagonal family $\left(\begin{smallmatrix}0&a(s)\\b(s)&0\end{smallmatrix}\right)$ with neither entry identically zero, pairwise commutativity is equivalent to $a(s)b(t)=a(t)b(s)$, or equivalently to constancy of $a/b$. Equation [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"} therefore proves noncommutativity on a fixed invariant two-dimensional subspace. The whole local factor cannot commute.

::: {#tab:parity}
  Local data                      Fixed residual operator   Commutativity
  ------------------------------- ------------------------- ----------------------------
  $p\mid q$                       Diagonal matrix           Yes
  $p\nmid q,\ c=\pm 1$            $P_{p,e}(X)$              Yes, every $e$
  $p\nmid q,\ c=\pm i,\ e$ even   $P_{p,e}(X)$              Yes
  $p\nmid q,\ c=\pm i,\ e$ odd    $P_{p,e}(X)F$             No: central pair exchanged

  : Local alternatives when $\chi^2$ is real. Here $c=\chi(p)$ and $e=v_p(N/q^2)$. The similarities used to reach the displayed operators are constant in the spectral parameter.
:::

## The full character criterion

If the full scattering family commutes, then [\[prop:nonreal-obstruction\]](#prop:nonreal-obstruction){reference-type="ref" reference="prop:nonreal-obstruction"} gives real squares for every primitive conductor. Real characters satisfy [\[eq:phase-condition\]](#eq:phase-condition){reference-type="eqref" reference="eq:phase-condition"} automatically. In a quartic sector, the constant reductions leading to [\[eq:global-A\]](#eq:global-A){reference-type="eqref" reference="eq:global-A"} preserve commutator vanishing; division by the common nonzero meromorphic scalar also preserves its being an identity. By [\[lem:tensor\]](#lem:tensor){reference-type="ref" reference="lem:tensor"}, each local factor must commute. Ramified factors are diagonal, while [\[prop:local-parity\]](#prop:local-parity){reference-type="ref" reference="prop:local-parity"} excludes exactly the imaginary unramified values at odd $e_p$. For $p\nmid q$, $e_p=v_p(N)$. This proves [\[eq:phase-condition\]](#eq:phase-condition){reference-type="eqref" reference="eq:phase-condition"}.

Conversely, assume [\[eq:real-square-condition\]](#eq:real-square-condition){reference-type="eqref" reference="eq:real-square-condition"} and [\[eq:phase-condition\]](#eq:phase-condition){reference-type="eqref" reference="eq:phase-condition"} for all primitive conductors. Each real sector commutes by the first part of this section. In a quartic sector, every local factor of [\[eq:global-A\]](#eq:global-A){reference-type="eqref" reference="eq:global-A"} commutes by [\[prop:local-parity\]](#prop:local-parity){reference-type="ref" reference="prop:local-parity"}, so their tensor product commutes. Reversing the constant similarities shows that the actual paired block commutes. The Fourier decomposition in [\[prop:paired-blocks\]](#prop:paired-blocks){reference-type="ref" reference="prop:paired-blocks"} exhausts the cusp space, proving commutativity of the whole family.

All arguments with inverses and quotients were made first on generic open sets. The resulting commutator is a meromorphic matrix identity in $(s,t)$. It therefore holds at every pair of regular values of the actual $\Phi_N$, including values at which an intermediate formula has a removable singularity. In the necessity direction, an assumed identity at all regular pairs is a meromorphic identity, so the same generic arguments apply. No exceptional regular parameter is excluded.

The tensor argument also explains why two odd-exponent imaginary phases cannot repair one another. It does not require independence of logarithms of distinct primes: generic invertibility, partial traces and the finite set of scalar roots of unity suffice.

# The elementary level conditions {#sec:arithmetic}

We convert [\[thm:characters\]](#thm:characters){reference-type="ref" reference="thm:characters"} to [\[thm:levels\]](#thm:levels){reference-type="ref" reference="thm:levels"}. Put $$M=\prod_p p^{\lfloor v_p(N)/2\rfloor},\qquad
 M^{(p)}=M/p^{v_p(M)},\qquad U_d=(\mathbb Z/d\mathbb Z)^\times,$$ with $U_1$ trivial. A conductor square divides $N$ exactly when its conductor divides $M$.

[\[lem:unit-exponent\]]{#lem:unit-exponent label="lem:unit-exponent"} Every primitive character of conductor dividing $M$ has fourth power one if and only if $$M=2^a3^b5^c,\qquad 0\le a\le4,\qquad b,c\in\{0,1\}.$$

Every character of $U_M$ has a unique primitive inducing character, and pullback preserves its image and order. The stated fourth-power condition is therefore that the dual of $U_M$ has exponent dividing four. A finite abelian group and its character dual have the same exponent: decompose the group into cyclic factors, on each of which the full group of roots-of-unity characters has the same order. Thus the condition is $\mathop{\mathrm{exp}}(U_M)\mid4$.

The Chinese remainder theorem decomposes $U_M$ into its prime-power unit groups. For odd $p$, the classical cyclic group $U_{p^a}$ has order $(p-1)p^{a-1}$. For $a\ge1$, this order divides four exactly when $a=1$ and $p=3$ or $5$. For powers of two, the groups for exponents $0,1$ are trivial, $U_4$ has order two, and $U_{2^a}\simeq C_2\times C_{2^{a-2}}$ for $a\ge3$. Their exponents divide four exactly for $a\le4$. Combining the factors proves the assertion.

Taking floors in the definition of $M$ gives exactly the prime-exponent bounds in [\[thm:levels\]](#thm:levels){reference-type="ref" reference="thm:levels"}; they are also recorded in [3](#tab:levels){reference-type="ref" reference="tab:levels"}. These familiar unit-group facts are arithmetic tools, not separate contributions.

::: {#tab:levels}
  Prime in the square-root level $M$   Allowed exponent in $M$   Equivalent bound in $N$
  ------------------------------------ ------------------------- -------------------------
  $2$                                  $0,\ldots,4$              $v_2(N)\le 9$
  $3$                                  $0,1$                     $v_3(N)\le 3$
  $5$                                  $0,1$                     $v_5(N)\le 3$
  $p\ge 7$                             $0$                       $v_p(N)\le 1$

  : The conductor-square part of the classification. The additional congruences in [\[thm:levels\]](#thm:levels){reference-type="ref" reference="thm:levels"} are imposed only at odd exponents in $N$.
:::

[\[lem:extra-prime\]]{#lem:extra-prime label="lem:extra-prime"} Fix a prime $p$ with odd $v_p(N)$. Condition [\[eq:phase-condition\]](#eq:phase-condition){reference-type="eqref" reference="eq:phase-condition"} for every permitted primitive character of conductor prime to $p$ is equivalent to $$\label{eq:p-square}
 p^2\equiv1\pmod{M^{(p)}}.$$

The primitive characters whose conductors divide $M$ and are coprime to $p$ correspond precisely to the full character dual of $U_{M^{(p)}}$. The prime $p$ is a unit in this group. All these characters have square value one at $p$ exactly when every character is one on $p^2$. Characters of a finite abelian group separate its elements, as can again be seen on each cyclic factor. This is exactly [\[eq:p-square\]](#eq:p-square){reference-type="eqref" reference="eq:p-square"}.

By [\[thm:characters,lem:unit-exponent\]](#thm:characters,lem:unit-exponent){reference-type="ref" reference="thm:characters,lem:unit-exponent"}, the conductor-square condition is equivalent to the displayed exponent bounds. Under these bounds, it remains to resolve [\[eq:p-square\]](#eq:p-square){reference-type="eqref" reference="eq:p-square"} only for primes with odd $v_p(N)$.

Every unit has square one modulo $3$, and every odd unit has square one modulo $2^a$ for $a\le3$. These factors impose no extra restrictions. If $5\mid M$, then for $p\ne5$, $$p^2\equiv1\pmod5
 \quad\Longleftrightarrow\quad p\equiv\pm1\pmod5.$$ Here $5\mid M$ is equivalent to $v_5(N)\ge2$. If $16\mid M$, the four odd classes modulo eight have square one modulo sixteen precisely for the classes $1$ and $7$. Thus, for odd $p$, $$p^2\equiv1\pmod{16}
 \quad\Longleftrightarrow\quad p\equiv\pm1\pmod8.$$ The hypothesis $16\mid M$ is equivalent to $v_2(N)\ge8$. These are exactly the two congruence clauses of the theorem. Conversely, those clauses settle every prime-power factor of $M^{(p)}$; the Chinese remainder theorem then gives [\[eq:p-square\]](#eq:p-square){reference-type="eqref" reference="eq:p-square"}. This proves both directions.

There is no condition at an even exponent, because such a prime was never selected in [\[lem:extra-prime\]](#lem:extra-prime){reference-type="ref" reference="lem:extra-prime"}. Nor does the argument ask for a nonzero value $\chi(p)$ at a prime dividing the conductor.

# The boundary levels 50 and 100 {#sec:examples}

gives a small exact comparison. It distinguishes the two obstructions without substituting a finite parameter grid for the all-level theorem.

::: {#tab:boundary}
  $N$     Primitive conductors   Quartic unramified data      Full family
  ------- ---------------------- ---------------------------- --------------
  $50$    $1,5$                  $\chi(2)=\pm i,\ v_2(N)=1$   Noncommuting
  $100$   $1,5$                  $\chi(2)=\pm i,\ v_2(N)=2$   Commuting

  : The same quartic phase has opposite outcomes at odd and even oldform exponent. Both statements are proved, not inferred from a level scan.
:::

At $N=50$, the only primitive conductors with $q^2\mid N$ are $1$ and $5$. Every character of conductor five has order dividing four, so real squares alone would predict commutativity incorrectly. Let $\chi(2)=i$. The unramified prime two has exponent one, so [\[thm:characters\]](#thm:characters){reference-type="ref" reference="thm:characters"} proves noncommutativity. We record an actual regular pair as a normalization check.

[\[prop:50\]]{#prop:50 label="prop:50"} The full width-one family satisfies $$[\Phi_{50}(2),\Phi_{50}(3)]\ne0.$$

For $q=5$, $L=2$, the denominator labels in the $\chi$ sector are $5,10$. Equations [\[eq:ramified-C\]](#eq:ramified-C){reference-type="eqref" reference="eq:ramified-C"} and [\[eq:unramified-C\]](#eq:unramified-C){reference-type="eqref" reference="eq:unramified-C"} give $$C_\chi(s)=10^s
 \begin{pmatrix}1&i2^{-s}\\i2^{-s}&1\end{pmatrix},
 \qquad
 C_{\bar\chi}(s)=10^s
 \begin{pmatrix}1&-i2^{-s}\\-i2^{-s}&1\end{pmatrix}.$$ The square character $\eta=\chi^2$ is primitive, even and quadratic modulo five. Remove the constant reciprocal Gauss ratios as in [5](#sec:parity){reference-type="ref" reference="sec:parity"}. The common scalar of the paired block is $$g(s)=10^{1-2s}k(s),\qquad
 k(s)=\left(\frac5\pi\right)^{1-2s}
 \frac{\Gamma(1-s)L(2-2s,\eta)}{\Gamma(s)L(2s,\eta)}.$$ The primitive even functional equation gives the meromorphic identity $$k(s)=\epsilon_\eta\sqrt{\frac\pi5}
       \frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
       \frac{L(2s-1,\eta)}{L(2s,\eta)}.$$ Thus $g(2)g(3)\ne0$, by absolute convergence and nonvanishing of the Euler products in $\Re u>1$. Both parameters are regular for the full cusp scattering matrix, since its Eisenstein series and constant terms are holomorphic in $\Re s>1$.

Apply the fixed matrix $W=\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)$ to each denominator pair and reorder coordinates to collect the two plus channels. After division by $g(s)$, the corresponding fixed invariant block is $$K_+(s)=\begin{pmatrix}0&R_i(s)\\R_{-i}(s)&0\end{pmatrix},
 \qquad
 R_{\pm i}(s)=\frac{1\mp i2^{s-1}}{1\pm i2^{-s}}.$$ Exact substitution gives $$R_i(2)=\frac{8-36i}{17},\qquad
 R_i(3)=\frac{32-264i}{65},$$ with the conjugate values for $R_{-i}$ at these real parameters. Direct multiplication yields $$[K_+(2),K_+(3)]
 =\mathop{\mathrm{diag}}\left(\frac{384i}{221},-\frac{384i}{221}\right).$$ The actual block commutator is this matrix times $g(2)g(3)\ne0$. A restriction of a commuting family to a fixed invariant subspace would commute, and fixed similarities preserve commutator vanishing. The full commutator is therefore nonzero.

At $N=100$, the divisors whose squares divide $N$ are $1,2,5,10$, but only $1$ and $5$ support primitive characters: the unit group modulo two is trivial, and reduction from the unit group modulo ten to that modulo five is an isomorphism. All conductor-five characters have real square. In a quartic sector, the only unramified prime is two, now with exponent two. The even case of [\[lem:phase-identity\]](#lem:phase-identity){reference-type="ref" reference="lem:phase-identity"} has $F=I$. The principal and real sectors also commute. The entire Fourier decomposition therefore commutes.

These examples show why both a criterion using only real squares and a criterion demanding real values at *every* unramified exponent would be wrong. The theorem imposes the phase condition only at odd exponent. For another direct consequence, $N=2^8 5^2$ satisfies the classification: both special congruence clauses have no offending odd exponent. This is a deduction from the theorem, not a newly sampled level.

# Scope and reproducibility {#sec:scope}

The classification concerns a fixed, complete cusp scattering family with weight zero and trivial nebentypus. It does not address an arbitrary parameter-dependent renormalization, other weights or nontrivial nebentypus. The spectral parameter is not an ordinary dynamical time. In particular, commutativity or its failure supplies no autonomous iteration, target Euler-factor dictionary, target root number or Hilbert--Pólya realization. The Dirichlet Euler factors and functional-equation constants occurring in the proof are classical source inputs.

Every new argument used for the two main theorems is typeset in this article. The explicitly imported analytic statements are the classical Eisenstein inversion and functional equations and the primitive Dirichlet identities, with their normalizations specified at the point of use. The supporting source dossier retains the precise inspected versions and access limits. Its existence is not a replacement for any central proof in the article.

No numerical experiment is a premise of the classification. Earlier principal-sector probes and an exact level-$50$ check were diagnostic evidence during development; they were not rerun for manuscript preparation and are not extrapolated to arbitrary levels. The displayed tables contain theorem data, and the explicit commutator in [\[prop:50\]](#prop:50){reference-type="ref" reference="prop:50"} is derived in the text.

#### Preparation disclosure.

The manuscript and supporting derivations were prepared with AI assistance and reviewed internally by AI-assisted agents. Such review is not human peer review, an editorial decision or a certification of worldwide priority. Formal review, release and reproducibility records are maintained separately from the mathematical claims.
