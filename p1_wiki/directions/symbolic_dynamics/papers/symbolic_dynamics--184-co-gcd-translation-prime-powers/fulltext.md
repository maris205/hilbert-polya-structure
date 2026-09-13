---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--184-co-gcd-translation-prime-powers"
canonical_tex: "symbolic_dynamics/papers/184-co-gcd-translation-prime-powers/main.tex"
canonical_pdf: "symbolic_dynamics/papers/184-co-gcd-translation-prime-powers/main.pdf"
source_sha256: "6f11630dfbb68ff3ac30e652130497b3c473a45869c968fb0679136ba2b8b44a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Co-GCD Translation on Prime-Power Residues: Valuation Strata, Tail Ladders, and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/184-co-gcd-translation-prime-powers>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/184-co-gcd-translation-prime-powers/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/184-co-gcd-translation-prime-powers/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/184-co-gcd-translation-prime-powers/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/184-co-gcd-translation-prime-powers/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a prime power $N=p^a$, we determine the finite map $T(x)=x+N/\gcd(x,N)\pmod N$. The added integer is the additive order of the current residue, but the resulting functional graph is not a group translation. Valuation strata below $a/2$ are recurrent translations, while strata above $a/2$ fall to their complementary valuation in one step. When $a$ is even, the equality stratum is a conveyor: consecutive unit increments produce a uniformly populated tail ladder of depths $2,\ldots,p$. We obtain every cycle length and multiplicity, every tail population, and the sharp maximum tail. We also solve the inverse problem completely. Every target has zero, one, or two predecessors; the empty and double fibres both number $p^{\lfloor(a-1)/2\rfloor}$, and an explicit congruence parametrizes every double target. The proofs include $p=2$, $x=0$, and both parities of $a$. Exact enumeration on 27 prime-power carriers supplies 109,478 author-side regression assertions, not proof or novelty evidence. The manuscript remains `HOLD_EXTERNAL` pending a full owner audit.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Co-GCD Translation on Prime-Power Residues:\
  Valuation Strata, Tail Ladders, and Exact Fibres
```

## Markdown 正文

# Literal system and contribution boundary

Let $p$ be a prime, $a\geq1$, and $N=p^a$. We use the representatives $0,1,\ldots,N-1$ and define $$\label{eq:map}
 T(x)=x+\frac{N}{\gcd(x,N)}\pmod N,
 \qquad \gcd(0,N)=N.$$ The quotient $N/\gcd(x,N)$ is the order of $x$ in the additive cyclic group, but it is inserted as a new residue rather than used as an iteration count. Put $\nu_p(0)=a$ and use the ordinary $p$-adic valuation for $x\ne0$.

Finite dynamics over rings and $p$-adic state spaces are established subjects [@XuZou2009; @AnashinKhrennikov2009]; functional-graph analysis over finite algebraic carriers is likewise standard [@KonyaginEtAl2016]. Those sources do not state the valuation-switched map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. We assign cyclic-group arithmetic, generic valuation stratification, and generic functional-graph bookkeeping zero contribution credit. The retained object is the conjunction, for the literal map, of the middle-layer conveyor, full cycle/tail atlas, fibre cap, image defect, and explicit double-target set. A bounded exact-formula search found no primary owner, but a non-hit is not a novelty certificate; a later literal or equivalent owner triggers withdrawal.

Internally, P142 maps prime-power *divisors* by a valuation--gcd rule, whereas [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} acts on all $p^a$ residue classes and translates within each low valuation stratum. P128 takes polynomial gcds, and P166 uses a Hamming-weight-selected phase translation on a cyclic cube. None has the even-exponent conveyor or the $0/1/2$ residue-fibre atlas below. This is an internal proof-transfer subtraction, not an external priority claim.

For a finite map, the *tail* $\mu(x)$ is the least $m\geq0$ for which $T^m(x)$ is periodic, and $\lambda(x)$ is the period of that eventual cycle.

# Pointwise valuation dynamics

[\[thm:strata\]]{#thm:strata label="thm:strata"} Let $v=\nu_p(x)$.

(i) If $2v<a$, then $\mu(x)=0$ and $\lambda(x)=p^v$.

(ii) If $2v>a$, including $x=0$, then $\mu(x)=1$ and $\lambda(x)=p^{a-v}$.

(iii) Suppose $a=2h$ and $v=h$. Write $x=p^hu$ with $1\leq u<p^h$ and $p\nmid u$, and put $$\label{eq:rs}
             r=p-(u\bmod p),\qquad s=\nu_p(u+r).$$ Here $1\leq r\leq p-1$ and $1\leq s\leq h$, with $s=h$ allowed when $u+r=p^h$. Then $$\label{eq:middle-orbit}
             \mu(x)=r+1,\qquad \lambda(x)=p^{h-s}.$$

First take $x\ne0$ and write $x=p^vu$ with $p\nmid u$. Equation [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} gives $$\label{eq:stratum-step}
 T(x)=p^vu+p^{a-v}\pmod {p^a}.$$ If $2v<a$, division by $p^v$ turns the action on the unit coordinate modulo $p^{a-v}$ into translation by $p^{a-2v}$. The added term is divisible by $p$ unless $v=0$, where it is zero modulo $p^a$; in either case the coordinate remains a unit. The additive order of the translating element is $p^{a-v}/p^{a-2v}=p^v$. This proves (i), including the fixed unit stratum.

If $2v>a$, factor [\[eq:stratum-step\]](#eq:stratum-step){reference-type="eqref" reference="eq:stratum-step"} as $$\label{eq:high-fall}
 T(x)=p^{a-v}\bigl(1+p^{2v-a}u\bigr).$$ The parenthesis is a unit, so the next valuation is $a-v<a/2$ and (i) gives the period $p^{a-v}$. The old high valuation cannot lie on that low invariant cycle, so the tail is exactly one. For $x=0$, equation [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} gives $0\mapsto1$, and $1$ is fixed; this agrees with (ii).

It remains to handle equality. Modulo $p^h$, the middle unit coordinate evolves by $u\mapsto u+1$. For $0\leq k<r$, the integer $u+k$ is not divisible by $p$, while $u+r$ is. After $r$ steps the state is high. If $u+r<p^h$ its valuation is $h+s$; if $u+r=p^h$, the state is zero and our convention gives the same value $h+s=2h$. One further step invokes (ii) and lands at valuation $h-s$, whose period is $p^{h-s}$ by (i). The successive middle states and the high state cannot belong to the low invariant cycle, proving the exact tail $r+1$ and (iii).

For $p=2$, the middle layer has $r=1$ for every unit $u$, so all its states have tail two. No odd-prime assumption is hidden in the theorem.

# Cycle and tail censuses

[\[thm:census\]]{#thm:census label="thm:census"} For every integer $v$ with $0\leq v<a/2$, the map has $$\label{eq:cycles}
 (p-1)p^{a-2v-1}$$ cycles of length $p^v$. The recurrent population is $$\label{eq:recurrent}
 p^a-p^{\lfloor a/2\rfloor}.$$ The positive-tail populations are as follows.

(a) If $a=2h+1$, exactly $p^h$ states have tail one and no state has a larger tail.

(b) If $a=2h$, exactly $p^{h-1}$ states occur at each tail depth $1,2,\ldots,p$, and no other positive depth occurs.

In particular, the sharp maximum tail is one for odd $a$ and $p$ for even $a$.

The stratum of exact valuation $v<a$ has $(p-1)p^{a-v-1}$ states. For $2v<a$, Theorem [\[thm:strata\]](#thm:strata){reference-type="ref" reference="thm:strata"} partitions it into cycles of common length $p^v$, giving [\[eq:cycles\]](#eq:cycles){reference-type="eqref" reference="eq:cycles"}. The union of the low strata is the complement of the multiples of $p^{\lceil a/2\rceil}$, whose number is $p^{\lfloor a/2\rfloor}$; this proves [\[eq:recurrent\]](#eq:recurrent){reference-type="eqref" reference="eq:recurrent"}.

For $a=2h+1$, the high region is exactly the set of multiples of $p^{h+1}$, including zero. It has $p^h$ elements, all of tail one by Theorem [\[thm:strata\]](#thm:strata){reference-type="ref" reference="thm:strata"}(ii). For $a=2h$, the strict high region consists of the $p^{h-1}$ multiples of $p^{h+1}$ and has tail one. In the middle stratum, each nonzero residue class of $u$ modulo $p$ occurs $p^{h-1}$ times. The quantity $r=p-(u\bmod p)$ runs once through $1,\ldots,p-1$, so Theorem [\[thm:strata\]](#thm:strata){reference-type="ref" reference="thm:strata"}(iii) gives $p^{h-1}$ states at each depth $2,\ldots,p$. This accounts for every state.

# Exact fibres and image defect

Put $$\label{eq:defect}
 d=p^{\lfloor(a-1)/2\rfloor}.$$ Define the double-target set $$\label{eq:double-set}
 \mathcal D=\{1\}\ \cup\!
 \bigcup_{1\leq w<a/2}
 \left\{p^w\bigl(1+p^{a-2w}u\bigr):
       1\leq u<p^w,\ p\nmid u\right\}.$$ All displayed representatives in [\[eq:double-set\]](#eq:double-set){reference-type="eqref" reference="eq:double-set"} lie strictly below $p^a$. Define the empty-target set by $$\label{eq:empty-set}
 \mathcal Z=
 \begin{cases}
 \{y:\nu_p(y)>h\},&a=2h+1,\\
 \{p^hz:0\leq z<p^h,\ z\equiv1\pmod p\},&a=2h.
 \end{cases}$$

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} For every target $y\in\{0,\ldots,p^a-1\}$, $$\label{eq:fibre-size}
 \#T^{-1}(y)=
 \begin{cases}
 0,&y\in\mathcal Z,\\
 2,&y\in\mathcal D,\\
 1,&y\notin\mathcal Z\cup\mathcal D.
 \end{cases}$$ Moreover $\mathcal Z$ and $\mathcal D$ are disjoint and $$\label{eq:fibre-census}
 |\mathcal Z|=|\mathcal D|=d.$$ Consequently $$\label{eq:image}
 |\operatorname{im}T|=p^a-d,$$ and the counts of zero-, one-, and two-element fibres are respectively $d,p^a-2d,d$.

On every low stratum, the translation in the proof of Theorem [\[thm:strata\]](#thm:strata){reference-type="ref" reference="thm:strata"}(i) is a bijection. Each low target therefore has one low predecessor. A strict high source of valuation $a-w$ has the unique form $p^{a-w}u$ with $1\leq u<p^w$ and $p\nmid u$, and [\[eq:high-fall\]](#eq:high-fall){reference-type="eqref" reference="eq:high-fall"} sends it to $$\label{eq:high-image}
 p^w\bigl(1+p^{a-2w}u\bigr).$$ The zero source maps to $1$. Valuation $w$ and then $u$ are recoverable from [\[eq:high-image\]](#eq:high-image){reference-type="eqref" reference="eq:high-image"}, so high sources inject into exactly $\mathcal D$. Every member of $\mathcal D$ already has its low predecessor, and no other target receives a high predecessor. This proves the double-fibre part and the fibre cap.

If $a$ is odd, there is no middle stratum. Low sources target low strata and high sources also target low strata, so precisely the high targets have no predecessor. They form the first case of $\mathcal Z$.

Let $a=2h$. On the middle stratum, the unit coordinate map is $u\mapsto u+1\pmod {p^h}$. A high or zero target coordinate is divisible by $p$ and has the unique unit predecessor $u=z-1$. A middle target coordinate $z$ is hit exactly when $z-1$ is also a unit, which fails exactly for $z\equiv1\pmod p$. Thus the missed targets are precisely the second case of $\mathcal Z$. All targets outside $\mathcal Z\cup\mathcal D$ have the one predecessor already described, proving [\[eq:fibre-size\]](#eq:fibre-size){reference-type="eqref" reference="eq:fibre-size"}.

For $a=2h+1$, $|\mathcal Z|=p^h=d$. For $a=2h$, $|\mathcal Z|=p^{h-1}=d$. Finally, $$|\mathcal D|=1+\sum_{1\leq w<a/2}(p-1)p^{w-1}=d$$ for either parity, with an empty sum allowed. The two sets lie in high or middle versus low strata, so they are disjoint. Equations [\[eq:fibre-census\]](#eq:fibre-census){reference-type="eqref" reference="eq:fibre-census"} and [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} follow.

Equivalently, a target other than $1$ is double precisely when, for $w=\nu_p(y)<a/2$, the quotient $y/p^w$ is congruent to $1$ modulo $p^{a-2w}$ and the resulting coefficient is a nonzero unit modulo $p$.

# Exact control, limitations, and conclusion

The paper-local standard-library verifier follows every orbit and reconstructs every fibre on 27 prime-power carriers. Selected rows appear in Table [1](#tab:control){reference-type="ref" reference="tab:control"}. Exhaustion is regression pressure only; the proofs establish the formulas for arbitrary primes and exponents.

::: {#tab:control}
   $p$   $a$     $N$   recurrent   image   zero/one/two fibres
  ----- ----- ------ ----------- ------- ---------------------
    2     6       64          56      60                4/56/4
    3     4       81          72      78                3/75/3
    5     4      625         600     620               5/615/5
    7     4     2401        2352    2394              7/2387/7

  : Selected author-side exhaustive controls, including even exponents and the binary case.
:::

The paper treats prime-power moduli only. It does not claim that Chinese remaindering makes the state-dependent additive-order translation factorwise, and it gives no composite-modulus atlas or asymptotic random-start law. The external owner search is bounded. These limitations keep the manuscript at `HOLD_EXTERNAL`.

# Declarations {#declarations .unnumbered}

#### Data availability.

No external data were used. Exact source code and its canonical stdout accompany the manuscript.

#### Ethics.

The work studies finite arithmetic maps and raises no human-subject, personal-data, or deployment issue.

#### CRediT.

Anonymous author(s) performed conceptualization, formal analysis, software, validation, original drafting, and review and editing.

#### Competing interests.

No competing interests are declared.

#### Funding.

No external funding is declared for this manuscript.

#### AI-use statement.

Generative AI tools assisted with ideation, drafting, and code scaffolding. The author-side verifier checks finite cases; responsibility for every definition, proof, citation, and disclosure remains with the human author(s).

#### Release status.

External circulation, posting, and submission are not authorized while `HOLD_EXTERNAL` remains active.
