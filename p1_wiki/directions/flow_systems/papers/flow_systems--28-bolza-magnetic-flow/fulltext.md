---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--28-bolza-magnetic-flow"
canonical_tex: "flow_systems/papers/28-bolza-magnetic-flow/stage5_finalization/manuscript.tex"
canonical_pdf: "flow_systems/papers/28-bolza-magnetic-flow/stage5_finalization/paper.pdf"
source_sha256: "14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Systole and Finite Enumeration Certificate for a Nonarithmetic Genus-Two Octagon

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/28-bolza-magnetic-flow>)
- [规范 TeX](<../../../../../flow_systems/papers/28-bolza-magnetic-flow/stage5_finalization/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/28-bolza-magnetic-flow/stage5_finalization/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/28-bolza-magnetic-flow/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/28-bolza-magnetic-flow/stage5_finalization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the systole of a specific compact nonarithmetic genus-two hyperbolic surface and give a replayable certificate that the underlying search is complete below a frozen geometric cutoff. The surface is the octagon with parameter $u=e^{-1/10}$ in the $\alpha=\pi/4$ one-parameter slice of Nazarenko's two-parameter family. Its side pairings are represented in $\operatorname{PSU}(1,1)$ by four explicit matrices. Because $u$ is transcendental, every enumerated matrix admits an exact normal form whose entries are Gaussian-integer polynomials in $u$, divided by a controlled power of $\Delta=(1-u^2)(2u^2-1)$. Equality, inversion, the surface relator, and length comparisons can therefore be decided without floating-point tolerances.

  The geometric part of the certificate converts a closed-geodesic bound $\ell\leq21/10$ into a tile-centre bound. A geodesic segment through the fundamental octagon supplies a side-adjacent chain that remains inside $\lvert\alpha\rvert^2\leq20000$, where $\alpha$ is the upper-left matrix entry. Exact breadth-first enumeration of the identity-connected sublevel component then yields 18,533 group elements and a closed boundary of 108,616 distinct rejected states. A polynomial sign test over all 18,532 nonidentity included states proves $$\operatorname{sys}(S)=2\operatorname{arcosh}\!\left(\frac{1}{2e^{-1/5}-1}\right)
    =2.043026655880296214455945667\ldots .$$ The word $g_0g_3$ is an exact primitive witness. The certificate contains 144 equality-achieving group elements; this number is deliberately not interpreted as a count of conjugacy classes or geometric systoles. The work establishes a target-blind control theorem for a Route-A research pipeline; it does not perform either surface census, a magnetic comparison, or an A2 evaluation.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology,\
  Luoyu Road 1037, 430070, Hubei, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 'August 28, 2026'
title: |
  An Exact Systole and Finite Enumeration Certificate\
  for a Nonarithmetic Genus-Two Octagon
```

## Markdown 正文

**Keywords:** hyperbolic surface; systole; Fuchsian group; exact arithmetic; certified enumeration; nonarithmetic lattice

本文精確決定一個緊緻、非算術的虧格二雙曲曲面之收縮長度， 並提供可重播的有限枚舉完備性證書。 研究對象為 Nazarenko 雙參數八邊形族的 $\alpha=\pi/4$ 單參數切片， 並取 $u=e^{-1/10}$； 四個邊配對以明確的 $\operatorname{PSU}(1,1)$ 矩陣表示。 利用 $u$ 的超越性， 我們將每個矩陣化為高斯整係數多項式除以 $\Delta=(1-u^2)(2u^2-1)$ 之受控半整次冪， 從而在不採用浮點容差的情況下判定相等、逆元、曲面關係式與長度不等式。 幾何上，任何長度不超過 $21/10$ 的閉測地線皆可共軛成其軸穿過基本八邊形； 沿線段所形成的相鄰鋪砌鏈， 其中心均落在 $\lvert\alpha\rvert^2\leq20000$ 的界內。 精確廣度優先搜尋得到恆等元連通分量中的 18,533 個群元素， 以及 108,616 個互異的邊界拒絕狀態。 對 18,532 個非恆等元素逐一施行整係數多項式符號證明後， 得到收縮長度 $$2\operatorname{arcosh}\!\left(\frac{1}{2e^{-1/5}-1}\right)
=2.043026655880296214455945667\ldots .$$ 詞 $g_0g_3$ 為精確且本原的見證。 證書中的 144 個等號狀態是互異群元素， 並非共軛類、反向等價類或幾何收縮線的數目。 此成果只建立路線 A 所需、與目標資料無關的控制曲面定理； 本文沒有執行 Bolza 對照普查、磁流比較、A2 判定或路線 B。

**關鍵詞：** 雙曲曲面；收縮長度；富克斯群；精確算術；認證枚舉；非算術格

# Introduction

For a compact hyperbolic surface, the systole is the least length of a noncontractible closed geodesic. Its definition is short, but an exact determination from a polygonal presentation has two logically different parts. One must first exhibit an element with the proposed translation length. One must then rule out every shorter conjugacy class. A bounded word search does not by itself accomplish the second task: conjugation can make a short geodesic appear as a long word, relations can produce many representatives of one element, and a floating-point equality threshold can hide a near-boundary failure.

This article resolves both parts for one explicit member of the genus-two octagon family described by Nazarenko [@Nazarenko2013 eqs. (10)--(18)]. The parameter is $u=e^{-1/10}$. The choice is useful for certification because it is transcendental, yet it can be enclosed by elementary rational Taylor bounds. It also makes the resulting cocompact Fuchsian group nonarithmetic. The surface is not the classical maximally symmetric Bolza surface. The peer-reviewed genus-two octagon literature provides useful family-level context [@AigonDupuyEtAl2005 abstract], but none of the cited sources states the systole or the finite certificate proved here.

The main result is the following exact formula: $$\label{eq:main-systole}
 \operatorname{sys}(S)=\ell_*
 :=2\operatorname{arcosh}\!\left(\frac{1}{2u^2-1}\right),
 \qquad u=e^{-1/10}.$$ The word $g_0g_3$ realizes this value. The global lower bound is established by a finite theorem rather than by a raw word cap. Every conjugacy class of translation length at most $\Lambda=21/10$ has a conjugate that is reached in an exact breadth-first search under the centre guard $\lvert\alpha\rvert^2\leq20000$. The cutoff $\Lambda$ was frozen before the enumeration and does not depend on target-surface or magnetic data.

Three design choices make the result auditable. First, all group elements are reduced to canonical polynomial matrix states in $\operatorname{PSU}(1,1)$, so deduplication is exact. Second, a tile-chain argument proves that the particular identity-connected centre sublevel component contains a conjugate of every class relevant to the cutoff. We do not claim that every element whose centre happens to satisfy the guard lies in that component. Third, each length comparison is reduced to the sign of an integer polynomial at the transcendental number $u$, and its sign is enclosed using rational arithmetic. The computation classifies 18,532 nonidentity elements: 18,388 are strictly longer than [\[eq:main-systole\]](#eq:main-systole){reference-type="eqref" reference="eq:main-systole"}, while 144 attain equality.

The integer 144 requires a prominent qualification. The enumeration is of canonical group elements. It performs no quotient by conjugacy, inversion, orientation, cyclic re-marking, or centralizer action. Hence 144 is neither an owner-class count nor a count of unoriented geometric systoles. Such a census would be a separate calculation and is outside the present claim.

The article proceeds from the source-locked octagon to exact normal forms, then to the geometric completeness theorem and the systole proof. It closes with implementation details, certificate hashes, adversarial checks, Route-A interpretation, and limitations. Statements proved symbolically are marked *PROVED*; facts obtained by exhaustive exact computation over the certified finite component are marked *NUMERICALLY CERTIFIED*. Decimal values are displays only and carry no inferential burden.

# The source-locked genus-two octagon {#sec:surface}

## Disk model and side pairings

Let $$\mathbb D=\{z\in\mathbb C:|z|<1\},\qquad
 d_{\mathbb D}(z,w)=2\operatorname{artanh}
 \left|\frac{z-w}{1-\overline z w}\right|.$$ We represent an orientation-preserving disk isometry by $$A=\begin{pmatrix}\alpha&\beta\\
 \overline\beta&\overline\alpha\end{pmatrix}\in\operatorname{SU}(1,1),
 \qquad |\alpha|^2-|\beta|^2=1,$$ acting as $z\mapsto(\alpha z+\beta)/(\overline\beta z+
\overline\alpha)$. The matrices $A$ and $-A$ determine the same element of $\operatorname{PSU}(1,1)$. For a hyperbolic element $A$, $$\label{eq:length-trace}
 \ell(A)=2\operatorname{arcosh}\frac{|\operatorname{tr}A|}{2},
 \qquad
 \cosh\frac{d_{\mathbb D}(0,A0)}{2}=|\alpha|.$$

Set $$\label{eq:parameters}
 u=e^{-1/10},\qquad x=u^2=e^{-1/5},\qquad
 \Delta=(1-u^2)(2u^2-1)>0,
 \qquad N=-\Delta^{-1/2}.$$ The source-locked octagon has alternating vertex moduli $u$ and $b=(\sqrt2\,u)^{-1}$, with successive angular positions separated by $\pi/4$. In particular, it is not being silently replaced by a regular Bolza octagon. The side-pairing matrices used throughout this article are $$\begin{aligned}
 g_0&=N\begin{pmatrix}
 u&u^2+i(1-u^2)\\ u^2-i(1-u^2)&u
 \end{pmatrix},
 &
 g_1&=N\begin{pmatrix}
 u&(1-u^2)+iu^2\\ (1-u^2)-iu^2&u
 \end{pmatrix},\label{eq:g01}\\
 R&=\begin{pmatrix}e^{i\pi/4}&0\\0&e^{-i\pi/4}\end{pmatrix},
 &g_2&=Rg_0R^{-1},\qquad g_3=Rg_1R^{-1}.
 \label{eq:g23}\end{aligned}$$ The determinant identity $$u^2-\bigl(u^4+(1-u^2)^2\bigr)=\Delta$$ shows directly that all four matrices lie in $\operatorname{SU}(1,1)$. The published side-pairing convention gives the eight-factor relation $$\label{eq:relator}
 g_0g_1^{-1}g_2g_3^{-1}g_0^{-1}g_1g_2^{-1}g_3=I.$$ Equations [\[eq:g01\]](#eq:g01){reference-type="eqref" reference="eq:g01"}--[\[eq:relator\]](#eq:relator){reference-type="eqref" reference="eq:relator"}, together with the vertex data, are a transcription of the fundamental octagon construction and pairing relations in [@Nazarenko2013 eqs. (10)--(18)]. They are treated as a source lock: the computation verifies them exactly before enumerating and does not estimate a new polygon from decimal coordinates.

By the polygon construction, the quotient $$S=\Gamma\backslash\mathbb D,
 \qquad \Gamma=\langle g_0,g_1,g_2,g_3\rangle<\operatorname{PSU}(1,1),$$ is a closed oriented hyperbolic surface of genus two. In particular, $\Gamma$ is discrete, cocompact, and torsion-free; every nonidentity element is hyperbolic and corresponds to a closed-geodesic free homotopy class.

## What the source lock fixes

The identifier used in the machine artifacts is `NAZARENKO-EXP-OCTAGON-G2`. It binds four kinds of input that should not be conflated. The first is the analytic specialization $(u,\pi/4)=(e^{-1/10},\pi/4)$. The second is the ordered set of four side-pairing generators, including the published convention for which side is paired by a generator rather than its inverse. The third is the relator [\[eq:relator\]](#eq:relator){reference-type="eqref" reference="eq:relator"}. The fourth is the alternating-radii fundamental polygon used in the radius proof. Changing any one of these objects would define a different computational problem even if a few decimal traces happened to agree.

This separation also explains the role of $R$. Conjugation by $R$ multiplies the two off-diagonal entries by $i$ and $-i$, respectively, so $g_2$ and $g_3$ remain in the same Gaussian-polynomial coefficient ring as $g_0$ and $g_1$. The negative choice of $N$ is harmless projectively, but it is retained to reproduce the source convention. The implementation does not normalize generators individually by a floating-point sign rule; it constructs the published matrices and only then applies one deterministic global $\operatorname{PSU}$ canonicalization to every state.

There are also two deliberately separate evidentiary layers. Nazarenko's equations support the octagon and side-pairing input at the cited locator. They are not cited for the finite ball, the 18,533-state count, the polynomial length test, or formula [\[eq:main-systole\]](#eq:main-systole){reference-type="eqref" reference="eq:main-systole"}. Those are project-derived claims. Conversely, the project computation is not used to replace the polygon theorem that makes the quotient a closed genus-two surface. This two-way boundary prevents a numerical relator residual from being presented as a new proof of discreteness, and prevents a literature citation from being presented as if it already contained the systole certificate.

## The geometric radius guard

Let $F$ be the closed fundamental octagon containing $0$. Since $u^4=e^{-2/5}>1/2$, one has $b<u$. Hyperbolic distance from the origin is monotone in Euclidean radius, so the maximum vertex radius is $u$. Convexity of the distance function along hyperbolic sides gives $$\label{eq:DF}
 D_F:=\max_{z\in F}d_{\mathbb D}(0,z)=2\operatorname{artanh}(u)<3.$$ The two strict inequalities used here are certified from rational Taylor enclosures: $$u^4\in(0.6703200460356393007444329250,
        0.6703200460356393007444329252)$$ and $$u<0.9048374180359595731642490595
   <0.9051482536448664382423036964<\tanh(3/2).$$ These decimals merely render the rational intervals legible; the checked certificate stores their exact fractional endpoints.

## A nonarithmeticity check

The word "nonarithmetic" in the title can be verified without a decimal trace test. The trace of $g_0$ satisfies $$\label{eq:t2}
 t^2:=\operatorname{tr}(g_0)^2
 =\frac{4x}{(1-x)(2x-1)}.$$ The Lindemann--Weierstrass theorem implies that $x=e^{-1/5}$ is transcendental [@Popescu2024 Cor. 3.2]. If $t^2$ were algebraic, then $x$ would satisfy $$\label{eq:quadratic-x}
 -2t^2x^2+(3t^2-4)x-t^2=0,$$ a nonzero polynomial over the algebraic numbers, which is impossible. Consequently $t^2$ and $\operatorname{tr}(g_0^2)=t^2-2$ are transcendental.

Takeuchi's characterization requires the invariant trace field of an arithmetic cofinite Fuchsian group to be an algebraic number field [@Takeuchi1975 Thm. 1 and condition (i)]. That field contains $\operatorname{tr}(g_0^2)$, so $\Gamma$ cannot be arithmetic. Equivalently, the square subgroup is finite index---the quotient by it is a finitely generated elementary abelian $2$-group---and arithmeticity is invariant under commensurability, while its trace field already contains the displayed transcendental element. This argument is *PROVED*; no heuristic arithmetic label is inferred from a numerical spectrum.

For later use, each generator is primitive. Abelianizing the standard genus-two presentation gives $\Gamma_{\mathrm{ab}}\cong\mathbb Z^4$, and $g_j$ maps to a basis vector. A proper power would map to a vector divisible by an integer greater than one. The same observation distinguishes these four elements modulo inversion, although the systole witness below is a different word.

# Related exact-computation setting and claim boundary

Algorithms for exact or certified work with Fuchsian groups have several nearby, but distinct, objectives. Voight develops algorithms for computing fundamental domains of cofinite Fuchsian groups in an arithmetic-algebraic input setting [@Voight2009 Secs. 1--4]. Despré et al. study the computation of Dirichlet domains from a hyperbolic polygon and its side pairings [@DespreEtAl2023 Secs. 2--3]. These works motivate the demand for explicit inputs and termination arguments. Their hypotheses and output contracts, however, do not supply the transcendental polynomial normal form, the radius lemma, or the systole certificate proved here.

The geometric family itself comes from Nazarenko's octagon equations [@Nazarenko2013 eqs. (10)--(18)]. Independent work on geodesic octagons and genus-two Teichmüller space supplies family-level corroboration [@AigonDupuyEtAl2005 abstract]. We use these sources only for the claims attached to the cited locators. All finite-count, hash, sign, and systole assertions in this article are new project results supported by the checked-in certificate, not attributed to the literature.

The present scope is deliberately narrower than a surface-to-surface comparison. We prove a theorem about one nonarithmetic control surface and freeze a common geometric cutoff. We do not enumerate a Bolza target, do not enumerate conjugacy or owner classes on this control surface, do not attach a magnetic flow to either surface, and do not compare multiplicities. We also do not evaluate the A2 criterion of the surrounding Route-A program and do not invoke Route B. Those exclusions matter because a correct control systole is a prerequisite for a comparison, not the comparison itself.

The present interface can be written as the typed map $$\bigl(S_{\mathrm{ctrl}},[A]_{\operatorname{PSU}(1,1)},\Lambda=21/10\bigr)
 \longmapsto
 \bigl(\ell([A]),\Lambda\bigr).$$ Here $S_{\mathrm{ctrl}}$ is the fixed hyperbolic control surface, $[A]_{\operatorname{PSU}(1,1)}$ is an exact group-element state, $\ell([A])$ is its geodesic translation length, and $\Lambda$ is the target-blind frozen cutoff. A magnetic Hamiltonian or flow, a magnetic clock or action, an owner quotient and its multiplicities, determinant weights, analytic continuation, and a spectral realization are separately typed inputs, constructions, or proofs and are not constructed by this map. It therefore yields no A2, A3, A4, or Route-B result; in particular, the 144 equality-achieving outputs remain exact group-element records rather than owners or multiplicities.

# Exact polynomial normal forms in $\operatorname{PSU}(1,1)$ {#sec:normal-form}

## Coefficient ring and denominator parity

Let $\mathcal R=\mathbb Z[i][U]$, where $U$ is an indeterminate, and put $$\delta(U)=(1-U^2)(2U^2-1)\in\mathbb Z[U].$$ After replacing $u$ by $U$, every numerator entry in [\[eq:g01\]](#eq:g01){reference-type="eqref" reference="eq:g01"}--[\[eq:g23\]](#eq:g23){reference-type="eqref" reference="eq:g23"} belongs to $\mathcal R$, while every generator or inverse contributes one factor $\sqrt{\delta(U)}$ to the denominator. Products can therefore be represented in the form $$\label{eq:state-form}
 A(U)=\frac{P(U)}{\delta(U)^q\sqrt{\delta(U)}^{\,p}},
 \qquad P(U)\in M_2(\mathcal R),\quad q\geq0,\quad p\in\{0,1\}.$$ Complex conjugation in the $\operatorname{SU}(1,1)$ pattern is coefficient-wise conjugation of Gaussian integers. Thus no approximate algebraic-number package or symbolic exponential simplifier is required.

After every multiplication, the implementation cancels a common factor $\delta$ from all four numerator entries as often as possible. It then chooses one of $P$ and $-P$ by comparing their ordered integer coefficient vectors and retaining the one whose first nonzero entry is positive. This last operation passes from $\operatorname{SU}(1,1)$ to a canonical $\operatorname{PSU}(1,1)$ state. The identity has $q=p=0$ and numerator $I$.

[\[lem:key\]]{#lem:key label="lem:key"} Two canonical states of the form [\[eq:state-form\]](#eq:state-form){reference-type="eqref" reference="eq:state-form"} represent the same element of $\operatorname{PSU}(1,1)$ at $U=u=e^{-1/10}$ if and only if their stored parity, exponent, and canonical numerator coincide.

Suppose first that the denominator parities agree. Clearing powers of $\delta(u)$ turns equality of corresponding entries into polynomial identities evaluated at $u$. Because $u$ is transcendental, a polynomial in $\mathbb Z[i][U]$ that vanishes at $u$ is identically zero. Removing all common $\delta$-factors makes the exponent unique, and the global sign rule removes the remaining $\operatorname{PSU}$ ambiguity.

If the parities differ, clearing the integral powers and then squaring a nonzero entry would imply an identity of the form $P(U)^2=\delta(U)Q(U)^2$ in $\mathbb Q(i)(U)$. But $\delta(U)$ is not a square in that rational-function field: its roots occur with odd multiplicity. Hence opposite parities cannot represent the same nonzero matrix. The converse direction is immediate from the construction.

Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"} turns a group search into dictionary operations on finite integer tuples. It also ensures that the 18,533 included states reported later are 18,533 distinct elements of $\operatorname{PSU}(1,1)$, rather than distinct words accidentally representing fewer elements.

## Canonicalization invariants

It is useful to make the state update more explicit. Store the denominator exponent as $e=2q+p$. Before cancellation, multiplication of exponent-$e$ and exponent-$f$ states produces numerator $P(U)Q(U)$ and exponent $e+f$. Cancelling one common factor $\delta(U)$ from all entries lowers the exponent by two and therefore preserves its parity. Repetition stops when at least one numerator entry is not divisible by $\delta$. Polynomial division is over $\mathbb Z[i][U]$, so the test has no numerical branch. Matrix inversion swaps the diagonal entries, negates the off-diagonal entries, and applies coefficient conjugation in the usual $\operatorname{SU}(1,1)$ formula; it leaves the denominator exponent unchanged.

Three invariants are checked after each conceptual stage. The numerator retains the $\operatorname{SU}(1,1)$ conjugate pattern. Its determinant equals the stored denominator squared as a polynomial identity. Finally, normalization is idempotent: applying common-factor cancellation and projective sign selection to an already normalized state returns the identical tuple. The unit tests exercise these properties indirectly through all inverse pairs, the surface relator, repeated multiplication, and frozen state hashes. The executed Stage-4 direct regression tests additionally verify that two consecutive common $\Delta$ factors cancel to the identity fixed point, that a globally negated numerator normalizes to the same state and remains idempotent, and that both $g_jg_j^{-1}$ and $g_j^{-1}g_j$ reduce to the identity for all four generators. Enumeration of all 585 words through length three produced 457 canonical states and nine collision buckets, including nine distinct sampled words that normalize to the identity. These tests import the audited certificate builder; they do not independently reimplement the eight-transition closure checker, and no independent-closure claim is made.

The exact provenance pointer for these bounded assertions is , , and ; the current evidence bundle binds their exact digest values and the read-only replay. This pointer is limited to same-builder canonicalization regressions. It neither upgrades transition-closure independence nor supplies a magnetic-flow, owner, Route, or spectral result.

The canonical word saved with a discovered state is not part of its identity. It is only the first breadth-first witness under a fixed generator order. Two words that reduce to the same polynomial matrix share one state even when neither is freely reducible to the other. Conversely, two matrices whose decimal evaluations are visually indistinguishable remain distinct whenever their exact tuples differ. This is important near the systolic boundary: deduplication and length comparison use the same symbolic parameter $U$, but they are separate predicates. Equality of group states is decided by Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}; equality of translation lengths is decided by the trace polynomial in Section [6](#sec:systole){reference-type="ref" reference="sec:systole"}.

The representation is exact but not claimed to be an optimal normal form for arbitrary surface-group words. Coefficient degrees and sizes can grow, and the method relies on the finite geometric component proved below. Its virtue for this theorem is narrower: within that component, every transition, collision, inverse, and comparison has a finite integer representation that can be serialized and replayed.

## Exact group and metric predicates

The same representation makes the prerequisite identities failure-closed. Each $g_jg_j^{-1}$ reduces to the identity key, and the eight factors in [\[eq:relator\]](#eq:relator){reference-type="eqref" reference="eq:relator"} do so as well. If either test failed, enumeration would stop before any geometric conclusion was emitted.

For the centre guard, write the upper-left entry as $\alpha(U)=A(U)/(\delta(U)^q\sqrt{\delta(U)}^p)$, with $A\in\mathbb Z[i][U]$. Then $$\label{eq:center-poly}
 |\alpha(u)|^2\leq C
 \quad\Longleftrightarrow\quad
 |A(u)|^2-C\delta(u)^{2q+p}\leq0.$$ The expression on the right is a polynomial with integer coefficients. Likewise, $\operatorname{tr}A(u)$ has a real integer-polynomial numerator $T(u)$ over the same denominator. Every branch in the breadth-first search is therefore decided by an exact zero identity or by the certified sign of an integer polynomial at $u$.

Signs are enclosed as follows. The alternating Taylor series for $e^{-1/10}$ gives rational lower and upper bounds. Polynomial interval evaluation propagates these bounds using exact fractions. When an interval straddles zero, the Taylor order is increased. A nonzero integer polynomial cannot vanish at the transcendental $u$, so this adaptive procedure has a mathematically isolated target sign. In the reported execution order 24 resolved every nonzero centre and systole comparison; exact zero polynomials were recognized symbolically before interval evaluation.

# From a length cutoff to a finite tile ball {#sec:completeness}

The search must contain at least one representative of every short conjugacy class, not every short word. This section supplies the missing geometric implication.

[\[lem:recenter\]]{#lem:recenter label="lem:recenter"} Let $\gamma\in\Gamma\setminus\{1\}$ have translation length $\ell(\gamma)\leq\Lambda=21/10$. Some conjugate $h$ of $\gamma$ satisfies $$d_{\mathbb D}(0,h0)\leq2D_F+\Lambda<81/10.$$

Choose a point on the invariant axis of $\gamma$. The translates of $F$ tile $\mathbb D$, so conjugating by a suitable group element makes the axis of a conjugate $h$ meet $F$, say at $z$. Since $h$ translates points on its axis by $\ell(h)=\ell(\gamma)$, the triangle inequality gives $$d(0,h0)\leq d(0,z)+d(z,hz)+d(hz,h0)
 \leq D_F+\ell(h)+D_F.$$ Equation [\[eq:DF\]](#eq:DF){reference-type="eqref" reference="eq:DF"} yields the strict numerical bound.

Consider now the geodesic segment from $0$ to $h0$. List in order the tiles whose interiors the segment crosses, resolving a passage through a vertex by either adjacent ordering. Consecutive tiles share a side, hence their labels differ by one of $g_0^{\pm1},\ldots,g_3^{\pm1}$. If the segment meets a tile $kF$ at $y$, then $d(y,k0)\leq D_F$. Every point $y$ on the segment has $d(0,y)\leq d(0,h0)$, so $$\label{eq:chain-radius}
 d(0,k0)\leq d(0,h0)+D_F<81/10+3=111/10.$$ Thus the crossed tiles furnish a Cayley-graph path from the identity to $h$ whose every vertex obeys the same radius bound.

By [\[eq:length-trace\]](#eq:length-trace){reference-type="eqref" reference="eq:length-trace"}, radius $111/10$ is equivalent to $|\alpha|^2<\cosh(111/20)^2$. Rational positive-series enclosures give $$\label{eq:guard}
\begin{aligned}
 \cosh(111/20)^2
 &\in(16543.29004587223200052996283,\\
 &\hspace{2.5em}16543.29004587223200052996285)<20000.
\end{aligned}$$ The deliberately rounded-up integer 20000 is the centre guard used by the enumerator.

Let $\mathcal C$ be the identity-connected component in the induced Cayley subgraph on canonical elements $k\in\Gamma$ satisfying $|\alpha(k)|^2\leq20000$, with edges given by right multiplication by the eight side-pairing letters.

[\[thm:complete\]]{#thm:complete label="thm:complete"} Every conjugacy class in $\Gamma$ with translation length at most $21/10$ has a representative in $\mathcal C$. Moreover, $\mathcal C$ is finite and is exhausted by breadth-first search that expands precisely its included states and records every distinct adjacent rejected state.

For a class of length at most $21/10$, Lemma [\[lem:recenter\]](#lem:recenter){reference-type="ref" reference="lem:recenter"} supplies a conjugate $h$. The crossed-tile construction gives an edge path from the identity to $h$, and [\[eq:chain-radius\]](#eq:chain-radius){reference-type="eqref" reference="eq:chain-radius"}--[\[eq:guard\]](#eq:guard){reference-type="eqref" reference="eq:guard"} put every vertex of that path inside the centre guard. Hence $h\in\mathcal C$.

The orbit $\Gamma0$ is discrete because $\Gamma$ is discrete and the stabilizer of $0$ is finite; it is trivial here because the surface group is torsion-free. A closed hyperbolic ball is compact, so it contains only finitely many orbit points. Consequently the guarded vertex set, and hence $\mathcal C$, is finite. Exact state keys from Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"} prevent duplicate expansion. Standard breadth-first induction discovers every vertex joined to the identity by a guarded path. When the queue is empty, all edges leaving included vertices have either an included endpoint or an explicitly recorded rejected endpoint, which closes the component boundary.

The wording "identity-connected component" is essential. The theorem does not assert that a guard-induced subgraph is globally connected. It asserts the stronger fact actually needed for short classes: the geometric tile chain places a suitable representative in the particular component that the search exhausts. This avoids an unjustified leap from a metric inequality to an arbitrary word-length cutoff.

## Why the tile-chain implication is the completeness step

A word-radius argument cannot replace Theorem [\[thm:complete\]](#thm:complete){reference-type="ref" reference="thm:complete"}. If $\eta$ is short, the conjugates $a^n\eta a^{-n}$ have the same translation length while their freely reduced lengths can grow with $n$. Relations can also make the shortest representative of an element much shorter than a word first encountered in an unguided search. Consequently, checking all words through depth $m$ does not imply that all geodesics through length $\Lambda$ were checked without an additional geometric theorem.

The proof supplies exactly that theorem in two stages. Axis recentering first chooses a conjugate on geometric, not lexical, grounds. The crossed-tile sequence then manufactures a generator path to that conjugate whose intermediate orbit points remain bounded. Degenerate crossings cause no gap. If the segment lies on a side or passes through a vertex, one may perturb it while fixing endpoints, record either limiting adjacent sequence, and remove repeated tiles. Every retained consecutive pair still shares a side, and the distance estimate uses closed tiles, so it survives the limit.

Nor is the integer guard 20000 tuned to the observed state cloud. It is a one-sided consequence of the pre-enumeration inequalities $D_F<3$, $2D_F+\Lambda<81/10$, and $\cosh(111/20)^2<20000$. The slack between approximately 16543.29 and 20000 protects the proof from an equality-at-the-boundary convention; it does not weaken the certified length cutoff. An element on $|\alpha|^2=20000$ is included, whereas the required tile chain is already strictly inside.

Finally, boundary closure has a graph-theoretic meaning. Every generator edge from every included state is classified. A rejected endpoint is recorded but not expanded, because a path leaving the induced subgraph cannot certify membership in its identity component. Queue exhaustion plus this full edge classification proves that no undiscovered guarded state is adjacent to the component. Compactness proves that exhaustion must occur; the reported counts show where it occurred in this instance.

# The exact systole {#sec:systole}

## Polynomial comparison with the candidate

Let a canonical state have denominator exponent $e=2q+p$, so its real trace can be written $$\operatorname{tr}A(u)=\frac{T(u)}{\Delta^{e/2}},\qquad T\in\mathbb Z[U].$$ Since all nonidentity elements are hyperbolic, equations [\[eq:length-trace\]](#eq:length-trace){reference-type="eqref" reference="eq:length-trace"} and [\[eq:main-systole\]](#eq:main-systole){reference-type="eqref" reference="eq:main-systole"} show that $\ell(A)\geq\ell_*$ exactly when $$\label{eq:H}
 H_A(u):=T(u)^2(2u^2-1)^2-4\Delta(u)^e\geq0.$$ Here $H_A\in\mathbb Z[U]$. If it is the zero polynomial, equality is exact. If it is nonzero, transcendence of $u$ excludes equality and rational interval evaluation determines a strict sign. There is no tolerance parameter and no rounding-dependent equality bucket.

Direct normal-form multiplication for $$\label{eq:witness}
 w=g_0g_3$$ produces $H_w(U)\equiv0$. Thus $w$ is hyperbolic and $\ell(w)=\ell_*$. Separately, rational enclosures verify $$\frac{1}{2u^2-1}<\cosh(21/20),$$ or equivalently $$\label{eq:candidate-cutoff}
 \ell_*<21/10.$$ The displayed decimal value is $$\ell_*=2.043026655880296214455945667098983993563924909550827545587792351028918\ldots.$$

## Global lower bound and primitivity

[\[thm:systole\]]{#thm:systole label="thm:systole"} For the surface $S=\Gamma\backslash\mathbb D$ specified in Section [2](#sec:surface){reference-type="ref" reference="sec:surface"}, $$\operatorname{sys}(S)=2\operatorname{arcosh}\!\left(\frac{1}{2e^{-1/5}-1}\right).$$ The element $w=g_0g_3$ is a primitive witness.

The exact finite execution described in Section [7](#sec:implementation){reference-type="ref" reference="sec:implementation"} exhausts $\mathcal C$. For each of its 18,532 nonidentity elements, it computes [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"}. There are 18,388 strict positive signs and 144 exact zero polynomials; no negative sign occurs. Hence every nonidentity element of $\mathcal C$ has length at least $\ell_*$.

Suppose a closed geodesic on $S$ had length below $\ell_*$. By [\[eq:candidate-cutoff\]](#eq:candidate-cutoff){reference-type="eqref" reference="eq:candidate-cutoff"} its class would have length below $21/10$, so Theorem [\[thm:complete\]](#thm:complete){reference-type="ref" reference="thm:complete"} would place a conjugate in $\mathcal C$. Translation length is conjugacy invariant, contradicting the finite sign classification. Thus $\operatorname{sys}(S)\geq\ell_*$. The exact identity $H_w\equiv0$ gives the reverse inequality.

If $w=v^m$ for a nonidentity $v\in\Gamma$ and an integer $m\geq2$, then hyperbolic translation lengths satisfy $\ell(w)=m\ell(v)$. This would give $0<\ell(v)<\ell_*$, contradicting the global lower bound just proved. Therefore $w$ is primitive.

Every one of the 144 equality-achieving states is a primitive group element, but the certificate determines no conjugacy-class or owner-class count.

The root argument in Theorem [\[thm:systole\]](#thm:systole){reference-type="ref" reference="thm:systole"} applies to any element of translation length $\ell_*$. On the other hand, the state key quotients only the global $\operatorname{SU}(1,1)$ sign. It does not quotient conjugation, inversion, cyclic marking, or orientation. Therefore an element-level count cannot be relabelled as a class-level count.

This distinction prevents the most tempting overinterpretation of the certificate. The 144 equality states may contain multiple conjugates and both orientations of the same geometric geodesic. Determining their orbits would require a separate, explicitly specified finite conjugacy or owner census. No such census is run or claimed here.

# Implementation and replayable certificate {#sec:implementation}

## Failure-closed enumeration

Every proof-decision branch in the implementation uses Python standard-library integer and `Fraction` arithmetic. The program also imports `mpmath` solely to render decimal displays; no state inclusion, equality, sign, or theorem-status decision depends on it. At a high level the implementation performs the following steps.

1.  Construct the eight generator and inverse normal forms and verify all inverse pairs and the relator [\[eq:relator\]](#eq:relator){reference-type="eqref" reference="eq:relator"}.

2.  Initialize a FIFO queue with the identity. For each dequeued state, right-multiply by the eight letters, normalize by common-$\Delta$ cancellation and the global $\operatorname{PSU}$ sign, and deduplicate by the exact coefficient tuple.

3.  Evaluate the polynomial predicate [\[eq:center-poly\]](#eq:center-poly){reference-type="eqref" reference="eq:center-poly"} with $C=20000$. Queue a new included state; otherwise store its canonical key as a rejected boundary state. Rejected states are never expanded.

4.  After the queue empties, evaluate [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"} for every nonidentity included state. Abort if any sign is negative or unresolved.

5.  Verify the exact witness, proof guards, totals, histograms, and deterministic sorted-state hashes before writing the certificate.

Every potentially theorem-changing predicate is failure-closed. An unresolved interval, invalid inverse, failed relation, negative systole sign, resource cap, or unclosed boundary prevents a passing artifact. No raw word length cap is present. Breadth-first depth is recorded only as a diagnostic of the completed component.

## Finite results

Table [1](#tab:results){reference-type="ref" reference="tab:results"} summarizes the certificate. The evidence status is *NUMERICALLY CERTIFIED*: the theorem reducing the task to a finite component is proved symbolically, while the exhaustive finite execution and its exact arithmetic are machine-replayed.

::: {#tab:results}
  Quantity                                Value
  ----------------------------------- ---------
  Included exact group elements          18,533
  Included nonidentity elements          18,532
  Distinct rejected boundary states     108,616
  Maximum shortest discovery depth           11
  States strictly above $\ell_*$         18,388
  States exactly equal to $\ell_*$          144
  States below $\ell_*$                       0
  Resource cap reached                       no

  : Exact finite-component and systole results.
:::

The shortest-discovery-depth histogram, including the identity, is $$\begin{array}{c|rrrrrrrrrrrr}
d&0&1&2&3&4&5&6&7&8&9&10&11\\\hline
N_d&1&8&56&392&1632&3976&5104&4168&2260&752&176&8.
\end{array}$$ All 18,388 nonzero systole signs and all centre-boundary signs were resolved at Taylor order 24; the 144 equality cases were polynomial identities and therefore used order zero.

Deterministic serialization makes accidental changes visible. The SHA-256 digest of the sorted included-state stream is

> 814f72badce2cc90e8e26edc2a7db18d52c4c334c0f5dfc5bf7d8e4a90dcf545,

and that of the distinct rejected-boundary stream is

> 3017c21285daad5a1173b076c9b5700975f67cdbbdaa8a6218e80d4bc89da6f4.

The canonical certificate JSON has digest

> c1bf68a8a1485665680dba01d0012fb691c7ca1a795e36334639e34bbbdbcb1f.

The frozen source/theorem note bound into the artifact has digest

> b2655431dcc27c471e8da3c092435dbe30c6a483e2244f78543adcd2a3141528.

The checked reproducer executes the builder twice in fresh temporary directories and requires byte-identical trees. Its recorded core-artifact hash is $\texttt{0a0ae16b}\ldots\texttt{e48e6512}$, and both tree hashes are $\texttt{c30beebd}\ldots\texttt{f60919ac}$. The separate manuscript audit reports a fresh replay, unit-test totals, software versions, and the final PDF digest. Hashes establish identity of artifacts, not mathematical truth by themselves; their role is to bind a reviewed proof argument to the exact finite output that was inspected.

## Independent replay obligations

A successful replay has more obligations than reproducing the headline number 18,533. In each fresh temporary directory, the builder first runs the proof guards and finite traversal that reconstructs all canonical states. The subsequent `build_validation` step checks the freeze, upstream source locks, source matrix, theorem fields, and output bindings. It requires the included and rejected stream hashes, depth histogram, sign histograms, witness key, source matrix, validation object, and standard-output summary to match. Two runs must produce byte-identical artifact trees. Default verify-only mode then compares these temporary products with the checked-in canonical files and has no write path to the canonical result directory. Canonical files can change only after validation passes and through the separate explicit refresh path.

Semantic checks are performed before digest checks. In particular, the included total must equal one identity plus the strict and equality sign counts; every included state must have all eight outgoing transitions classified; the resource-cap flag must be false; and all proof guards must pass. The witness state is rebuilt from $g_0g_3$, rather than trusted as a stored decimal trace. The validation artifact also requires the negative scope flags for both censuses, comparison, A2, and Route B. Thus copying an old hash into a malformed result cannot produce a passing validation.

The artifact is compact rather than a dump of every large polynomial tuple. Its deterministic stream hashes bind the complete sorted classifications, while the builder is the executable procedure for reconstructing them. This tradeoff keeps the reviewed package manageable but means long-term reproducibility depends on retaining the source-locked builder, Python's specified integer semantics, and the upstream input bytes. The manuscript audit therefore records both code hashes and a fresh end-to-end replay, not only the JSON certificate hash.

# Adversarial checks and Route-A interpretation

The certificate was designed against four plausible but invalid shortcuts.

First, a bounded word search could miss a short conjugate represented by a long word. The axis-recentering and tile-chain proof replaces word length by a geometric path whose every intermediate state satisfies an exact guard. Second, floating-point matrix hashing could split one element or merge two nearby elements. Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"} makes equality a polynomial identity question. Third, a decimal trace tolerance could manufacture or suppress equalities. Equation [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"} separates exact zero polynomials from strict rational interval signs. Fourth, a successful run chosen after viewing target data could encode a hidden target-dependent cutoff. Here $\Lambda=21/10$, the centre guard, and all proof obligations are frozen in the source-bound note, and the certificate states that target data were not used.

A "proves too much" audit is equally important. If the finite component contained many shortest elements, that fact would not determine how many unoriented closed geodesics exist. If the control is nonarithmetic, that fact would not label any target surface. If its exact systole is known, that fact would not compare control and target multiplicities. The artifact therefore records negative execution facts alongside positive ones: no Bolza census, no control conjugacy census, no magnetic comparison, no arithmetic target labels, no A2 evaluation, and no Route-B invocation.

Within the surrounding Route-A roadmap, the result should be read as a control-side infrastructure theorem. It validates an exact nonarithmetic surface, proves its shortest scale, and fixes a common length window that a later two-surface protocol may use. It does not alter the previously frozen formal status of a full candidate, which remains unassigned. The bounded exploratory proxy remains $$(\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},
  \mathrm{A1\_WEAK},
  \mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL}),$$ and is not promoted by the present theorem. In particular, "A2\_FAIL" is historical proxy state, not an A2 computation performed in this study.

**Route-A obligation legend (non-ranking).** For this paper, A0 denotes the arithmetic-relation qualification of the source-locked objects; A1 denotes a matched control--target finite census at a common frozen cutoff, with a declared owner quotient and multiplicities; A2 denotes the signed-field comparison on that matched census; A3 denotes the weighted determinant and analytic-continuation obligation; and A4 denotes spectral realization. These labels name successive evidence obligations, not levels of merit. The formal full P28 tuple remains unassigned. The historical exploratory proxy remains $$(\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},
  \mathrm{A1\_WEAK},
  \mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL}),$$ and is neither updated nor promoted here. The exact control systole and target-blind cutoff supplied by this theorem are A0--A1 infrastructure only, and the 144 equality-achieving records are group elements only. This study has not run a matched Bolza/control census, owner quotienting or a multiplicity ledger, a magnetic Hamiltonian/flow or clock/action construction, a signed-field comparison or A2 evaluation, determinant weights or analytic continuation, A3/A4 or other spectral work, or Route B.

The result is nevertheless substantial. A later comparison no longer needs to assume a control systole, infer completeness from a word cap, or retune a window after observing the target. Those are precisely the dependencies that an exact control certificate can remove while remaining neutral about the downstream scientific conclusion.

# Limitations

The theorem concerns one fixed parameter $u=e^{-1/10}$. Although the normal-form construction extends formally to other transcendental parameters, the numerical guard, finite-state counts, and polynomial sign distribution are parameter-specific. No uniform theorem over Nazarenko's whole octagon family is claimed.

The finite search proves completeness for conjugacy classes of length at most $21/10$, because that interval contains the candidate systole. It is not a complete length spectrum beyond that cutoff. Nor does it establish global connectivity of all group elements satisfying the centre guard; it exhausts the identity-connected component and proves that this component contains a representative of every class relevant to the stated cutoff.

The 144 equality-achieving states remain intentionally unclassified under conjugacy, inversion, and orientation. Therefore the paper supplies neither the number of primitive systolic conjugacy classes nor the number of unoriented systolic geodesics. It also supplies no marked cyclic census and no owner ledger at the systolic length.

Finally, the work is a control-surface theorem, not evidence of a magnetic universality mechanism. It contains no Bolza-control census, no target surface computation, no magnetic Hamiltonian or flow comparison, no spectral determinant, no A2 evaluation, and no Route-B argument. Any of those would require new definitions, frozen protocols, computations, and review.

# Conclusion

For the genus-two octagon with $u=e^{-1/10}$, we have proved the exact systole $$2\operatorname{arcosh}\!\left(\frac{1}{2e^{-1/5}-1}\right)$$ and supplied the primitive witness $g_0g_3$. The lower bound is global because a geometric tile-chain theorem places every class below the frozen cutoff $21/10$ inside a finite, exactly enumerated component. Polynomial normal forms and rational interval signs remove matrix-equality and length-comparison tolerances. The resulting certificate contains 18,533 group elements, a closed rejected boundary of 108,616 states, and no element shorter than the witness.

The central methodological outcome is the separation of geometry, exact algebra, and finite execution: each has an explicit proof obligation, and the hash-bound artifact can be replayed. Equally, the conclusion stays at the level the evidence supports. The 144 equality records are group elements, not a census of geometric systoles, and the certified control theorem is a Route-A prerequisite rather than an A2 or magnetic-comparison result.

# Declarations {#declarations .unnumbered}

## Funding {#funding .unnumbered}

This research received no external funding.

## Conflict of interest {#conflict-of-interest .unnumbered}

The author declares no conflict of interest.

## CRediT author statement {#credit-author-statement .unnumbered}

Liang Wang: Conceptualization; Methodology; Software; Validation; Formal analysis; Investigation; Data curation; Writing---original draft; Writing---review and editing; Visualization; Project administration.

## Data and code availability {#data-and-code-availability .unnumbered}

The source code, tests, source matrices, exact certificate, validation report, and reproducibility receipts used in this study are contained in the accompanying project repository under <https://github.com/maris205/hilbert-polya-structure/tree/main/flow_systems/papers/28-bolza-magnetic-flow>. The principal machine-readable artifact is ; its SHA-256 digest is reported in Section [7](#sec:implementation){reference-type="ref" reference="sec:implementation"}. No restricted or personal data are used.

## Ethics statement {#ethics-statement .unnumbered}

This mathematical and computational study involved no human participants, personal data, animals, or biological materials. Institutional ethics approval and informed consent were therefore not applicable.

## AI-Assisted Research Disclosure {#ai-assisted-research-disclosure .unnumbered}

OpenAI Codex was used under the author's direction to assist with manuscript drafting, language editing, LaTeX formatting, consistency checks, and verification of bibliographic metadata. The author specified the research scope, reviewed the mathematical claims and source attributions, and remains fully responsible for the proofs, computations, interpretations, and final text. AI systems are not listed as authors and were not used as primary evidence.
