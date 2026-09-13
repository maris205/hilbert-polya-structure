---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--74-dyck-motzkin-context-complexity"
canonical_tex: "symbolic_dynamics/papers/74-dyck-motzkin-context-complexity/main.tex"
canonical_pdf: "symbolic_dynamics/papers/74-dyck-motzkin-context-complexity/main.pdf"
source_sha256: "d168f97d1e528c09fb14bd452bc42f24dac28885e0829e2f73ff9bb8aa947816"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Follower, Predecessor, and Extender Complexity of Dyck--Motzkin Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/74-dyck-motzkin-context-complexity>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/74-dyck-motzkin-context-complexity/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/74-dyck-motzkin-context-complexity/main.pdf>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/74-dyck-motzkin-context-complexity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $M\geq2$ bracket types, we compute the complete finite follower, predecessor, and extender-set sequences of the Dyck shift and of every Motzkin extension with at least one neutral symbol. At word length $n$, the follower and predecessor counts are $$\sum_{j=0}^n M^j.$$ The Dyck extender count is $$\sum_{\substack{0\leq r\leq n\\r\equiv n\pmod2}}(r+1)M^r,$$ whereas the Motzkin count is $\sum_{r=0}^n(r+1)M^r$. Hence all three context entropies equal $\log M$, strictly below the topological entropy. The proof uses the complete polycyclic-monoid normal form and a separation lemma showing that, when $M\geq2$, distinct stacks give distinct contexts. Exact enumeration for $M=2,3$ guards the parity and neutral-symbol cases.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: 'Exact Follower, Predecessor, and Extender Complexity of Dyck--Motzkin Shifts'
```

## Markdown 正文

# Introduction

Dyck shifts are canonical nonsofic coded systems: their local alphabet is finite, but admissibility remembers an unbounded coloured stack. Motzkin shifts add neutral symbols without removing that memory. Their zeta functions, periodic points, and topological entropies have been studied in detail [@Inoue2010; @KriegerMatsumoto2011]. We do not revisit those owner results. Instead we measure exactly how many different one-sided and two-sided contexts are visible at each finite word length.

Follower, predecessor, and extender entropies were developed as context-growth quantities by French and Pavlov [@FrenchPavlov2019]; they do not all have the same conjugacy-invariance status. The underlying follower/extender set sequences were studied earlier by @French2016, and the coloured-stack presentation of Dyck past classes already appears in the Cantor-horizon $\lambda$-graph of @KriegerMatsumoto2003. The present calculation specializes these frameworks to exact word-length-indexed sequences for the Dyck--Motzkin family. The normal form of a legal word contains a left stack of unmatched closing brackets and a right stack of unmatched opening brackets. A follower set remembers exactly the right stack, a predecessor set exactly the left stack, and an extender set the ordered pair. Counting which normal-form lengths can arise gives the formulas.

The distinction between the Dyck and Motzkin extender sequences is a parity effect. Dyck reduction removes letters in pairs, while even one neutral symbol fills an arbitrary length deficit. The context entropies nonetheless coincide and exhibit a strict gap from ordinary word entropy.

# Dyck--Motzkin languages and contexts

Fix $M\geq2$. Let $$\mathcal A_M=\{\alpha_1,\ldots,\alpha_M,
                    \beta_1,\ldots,\beta_M\},$$ where $\alpha_i$ opens and $\beta_i$ closes a bracket of colour $i$. Adjoin an identity $1$ and an absorbing zero $0$, with relations $$\label{eq:polycyclic}
 \alpha_i\beta_j=\begin{cases}1,&i=j,\\0,&i\neq j.\end{cases}$$ For the Motzkin version, add $N\geq1$ neutral symbols $\gamma_1,\ldots,\gamma_N$, each evaluated as $1$.

The language $\mathcal L(X_{M,N})$ consists of finite words whose product under [\[eq:polycyclic\]](#eq:polycyclic){reference-type="eqref" reference="eq:polycyclic"} is nonzero. Here $N=0$ is the Dyck shift and $N\geq1$ is a Motzkin shift. This finite-block definition determines the usual two-sided subshift; the normal-form lemma below also verifies that every such word is globally extendible.

For $w\in\mathcal L(X)$ define its finite follower, predecessor, and extender sets by $$\begin{aligned}
 \mathcal F_X(w)&=\{v:wv\in\mathcal L(X)\},\\
 \mathcal P_X(w)&=\{u:uw\in\mathcal L(X)\},\\
 \mathcal E_X(w)&=\{(u,v):uwv\in\mathcal L(X)\}.\end{aligned}$$ The empty word is allowed as a context. Let $F_X(n)$, $P_X(n)$, and $E_X(n)$ denote the numbers of distinct such sets among words of length $n$. These finite-context definitions give the same equivalence classes as infinite one-sided contexts.

# Normal forms and syntactic separation

[\[lem:normal-form\]]{#lem:normal-form label="lem:normal-form"} Every nonzero product has a unique reduced form $$\label{eq:normal}
 \beta_{i_1}\cdots\beta_{i_k}
 \alpha_{j_1}\cdots\alpha_{j_\ell}.$$ Every finite word with nonzero product occurs in a point of $X_{M,N}$.

Scan a word from left to right while storing an unmatched-closing list $L$ and an opening stack $R$. An opening is pushed onto $R$. A closing pops a matching top entry, produces zero if its colour mismatches a nonempty top, and is appended to $L$ if $R$ is empty. Neutral letters do nothing. Induction on the scanned prefix shows that the surviving product is exactly $\beta_L\alpha_R$; the deterministic procedure and the standard partial action on coloured stacks show that two different pairs $(L,R)$ are distinct. This proves existence and uniqueness of [\[eq:normal\]](#eq:normal){reference-type="eqref" reference="eq:normal"}.

Finally, a nonzero word $w$ is embedded in the bi-infinite sequence $$\cdots\beta_1\beta_1\,w\,\alpha_1\alpha_1\cdots .$$ Every finite factor has a nonzero reduction: left-tail closings remain unmatched, right-tail openings only enlarge the stack, and factors internal to $w$ are nonzero because zero is absorbing. Thus the finite nonzero-product language is precisely the block language of the two-sided shift.

The first word records closing brackets that had no opening bracket to their left; the second records the surviving opening stack. Neutral symbols and matched pairs disappear. We write $L(w)=(i_1,\ldots,i_k)$ and $R(w)=(j_1,\ldots,j_\ell)$.

[\[lem:one-sided\]]{#lem:one-sided label="lem:one-sided"} For legal words $w,w'$, $$\mathcal F_X(w)=\mathcal F_X(w')\iff R(w)=R(w'),
 \qquad
 \mathcal P_X(w)=\mathcal P_X(w')\iff L(w)=L(w').$$

When a word is appended to $w$, a zero can be created at the interface only by a closing bracket that mismatches the top of $R(w)$. The left unmatched closings cannot participate. Thus equal right stacks give equal follower sets.

Conversely, compare two unequal right stacks from their tops. Close their common top suffix. If the next colours differ, a closing bracket matching one of them makes one product legal and the other zero. If one stack is exhausted first, choose a closing colour different from the next colour in the longer stack. It is an allowed unmatched close for the empty stack and a forbidden mismatch for the longer stack. This last step uses $M\geq2$. The predecessor assertion is the reflected argument.

[\[lem:extender\]]{#lem:extender label="lem:extender"} For legal words $w,w'$, $$\mathcal E_X(w)=\mathcal E_X(w')
 \iff (L(w),R(w))=(L(w'),R(w')).$$

Equal normal forms represent the same nonzero monoid element and therefore have identical behaviour under multiplication on both sides. Conversely, an extender set determines its follower set by restricting to pairs with empty left context, and determines its predecessor set by restricting to pairs with empty right context. Apply [\[lem:one-sided\]](#lem:one-sided){reference-type="ref" reference="lem:one-sided"}.

The $M=1$ exclusion is structural, not cosmetic: the spare colour used for syntactic separation is unavailable. In fact there are no mismatches, so the language is the full shift and $F_X(n)=P_X(n)=E_X(n)=1$ for every $n$.

# Exact finite context sequences

[\[thm:one-sided-count\]]{#thm:one-sided-count label="thm:one-sided-count"} For every $M\geq2$, every $N\geq0$, and every $n\geq0$, $$\label{eq:fp}
 F_{X_{M,N}}(n)=P_{X_{M,N}}(n)
 =\sum_{j=0}^nM^j=\frac{M^{n+1}-1}{M-1}.$$

By [\[lem:one-sided\]](#lem:one-sided){reference-type="ref" reference="lem:one-sided"}, follower sets are indexed by right stacks. For each $0\leq j\leq n$, all $M^j$ colour words of length $j$ occur. Indeed, prefix the desired opening stack by $n-j$ unmatched closing brackets; the result is a legal length-$n$ word. No longer stack can occur. Reflection proves the predecessor formula.

[\[thm:extender-count\]]{#thm:extender-count label="thm:extender-count"} For the Dyck shift $X_{M,0}$, $$\label{eq:dyck-extender}
 E_{X_{M,0}}(n)=
 \sum_{\substack{0\leq r\leq n\\r\equiv n\pmod2}}(r+1)M^r.$$ For every Motzkin shift $X_{M,N}$ with $N\geq1$, $$\label{eq:motzkin-extender}
 E_{X_{M,N}}(n)=\sum_{r=0}^n(r+1)M^r.$$

Fix total reduced length $r=k+\ell$. There are $r+1$ possible split points $k$, and then $M^kM^\ell=M^r$ colourings of the two stacks. By [\[lem:extender\]](#lem:extender){reference-type="ref" reference="lem:extender"}, all of these normal forms give different extender sets.

In a Dyck word, every reduction deletes two letters. Hence $r\leq n$ and $r\equiv n\pmod2$. Conversely, every normal form of such a length is realized at length $n$ by inserting $(n-r)/2$ adjacent matched pairs. This proves [\[eq:dyck-extender\]](#eq:dyck-extender){reference-type="eqref" reference="eq:dyck-extender"}. When a neutral symbol is available, append $n-r$ neutral letters to realize every $0\leq r\leq n$, which proves [\[eq:motzkin-extender\]](#eq:motzkin-extender){reference-type="eqref" reference="eq:motzkin-extender"}.

The number $N$ of distinct neutral symbols changes word growth but not the context counts: every neutral symbol represents the same identity at the two interfaces.

# Context entropy gap

French and Pavlov define follower and predecessor entropy using a limsup and extender entropy using the corresponding exponential growth limit [@FrenchPavlov2019]. The finite formulas immediately give the following.

[\[cor:entropy\]]{#cor:entropy label="cor:entropy"} For $M\geq2$ and $N\geq0$, $$h_F(X_{M,N})=h_P(X_{M,N})=h_E(X_{M,N})=\log M.$$ In contrast, the established topological entropy is $$h_{\rm top}(X_{M,N})=\log(M+N+1).$$ Consequently every Dyck--Motzkin system in this range has the strict gap $$h_{\rm top}-h_E=\log\frac{M+N+1}{M}>0.$$

The sums in [\[eq:fp\]](#eq:fp){reference-type="eqref" reference="eq:fp"}, [\[eq:dyck-extender\]](#eq:dyck-extender){reference-type="eqref" reference="eq:dyck-extender"}, and [\[eq:motzkin-extender\]](#eq:motzkin-extender){reference-type="eqref" reference="eq:motzkin-extender"} are bounded above and below by polynomial factors times $M^n$. Their exponential rate is therefore $\log M$. The topological entropy formula belongs to the established Dyck--Motzkin word-count theory [@Inoue2010; @KriegerMatsumoto2011].

The gap quantifies a familiar phenomenon: ordinary entropy counts all legal words, while context entropy quotients out the internal matched structure and retains only the information exposed at the two interfaces.

# Finite audit, negative control, and scope

The accompanying exact enumerator reduces every legal word for the four parameter pairs $$(M,N)\in\{(2,0),(3,0),(2,1),(3,2)\}.$$ It verifies all three formulas through $n=8$ for $M=2$ and through $n=7$ for $M=3$. At the largest checked sizes it finds, for example, $$(F_8,E_8)=(511,2845)\quad\text{for }X_{2,0},$$ and $$(F_8,E_8)=(511,4097)\quad\text{for }X_{2,1}.$$ Those high-horizon checks count normal forms. As a separate implementation gate, the script also groups small words by directly enumerated legal right, left, and two-sided context signatures; these groups reproduce the formulas without using the stored normal-form pair as the class label.

The audit preserves a failed shortcut as a negative control. Counting only the number of closing symbols does not determine a context: at length two with exactly one closing symbol there are $M$ legal matched open--close words and $M^2$ legal close--open words. Their combined word count is $M+M^2$, not the previously tested single-bin expression.

This note claims neither the set-sequence/context-entropy frameworks, the Dyck stack presentation, nor new zeta, periodic-point, or topological-entropy formulas. Those are assigned to their owners [@French2016; @FrenchPavlov2019; @KriegerMatsumoto2003; @Inoue2010; @KriegerMatsumoto2011]. The residual advance is the complete word-length-indexed follower/predecessor/extender sequence for this family and the resulting explicit entropy gap. The source search was bounded; no global priority claim or external-release authorization is made.
