---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--28-primitive-selector-cycle-monodromy"
canonical_tex: "symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/main.tex"
canonical_pdf: "symplectic_map/papers/28-primitive-selector-cycle-monodromy/build-capsule-ec-20260905/evidence/r0-01-latex/main.pdf"
source_sha256: "bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Primitive Newton-Selector Cycles in Permutation-Twisted Hamiltonian Shears: Normal-Fan Classification and Exact Monodromy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/28-primitive-selector-cycle-monodromy>)
- [规范 TeX](<../../../../../symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/28-primitive-selector-cycle-monodromy/build-capsule-ec-20260905/evidence/r0-01-latex/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/28-primitive-selector-cycle-monodromy/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every rooted primitive selector-pair word of length at least three, we construct one fixed autonomous polynomial symplectomorphism whose dimension grows with the word length. Its Hamiltonians have positive, equal-total collected supports and arbitrary nonzero coefficients over a characteristic-zero field. A general normal-fan theorem classifies strict position-weight selectors by a rational homogeneous open polyhedral cone: the first shear uses strict maximizers, whereas equal support totals turn the second comparison into a strict minimization on the residual position weight. A separate coordinatewise chamber is both the exact initial source-carry condition used by the lift and the input to a coefficient- uniform proof that the selected matrices are the actual polynomial weighted- degree transport. An incidence construction realizes every permitted word endogenously, including repeated labels and singleton component alphabets. The selector word and the position-weight orbit modulo the diagonal line have distinct least-period assertions, both equal to the word length. The ordered period product is an explicit rank-one perturbation of the identity, and its carry-free base expansion recovers the rooted digit-vector word. Recovering exponent-support pairs additionally requires the unlabelled support dictionary, and recovering literal labels requires its labelled version; without a marked phase, only a cyclic rotation class is intrinsic. The results concern weighted degree in the stated chamber, not periodicity of the polynomial state or an ordinary-degree or entropy invariant.
author:
- Anonymous
bibliography:
- references.bib
title: 'Primitive Newton-Selector Cycles in Permutation-Twisted Hamiltonian Shears: Normal-Fan Classification and Exact Monodromy'
```

## Markdown 正文

# Introduction and bounded positioning

## Question and contribution

An iterate of a polynomial map can expose different faces of its Newton supports as the weights of its coordinate polynomials evolve. That observation raises a concrete realization question. Given a finite rooted word of pairs of support labels, can one build a single autonomous polynomial symplectomorphism for which those pairs are selected strictly and repeatedly, with no external schedule choosing the active terms? A useful answer should do more than prescribe a formal product of degree matrices. It should identify the exact selector chamber, prove that carried coordinate terms do not spoil the formal leading terms, distinguish the relevant notions of period, and state precisely what the period product remembers.

These distinctions are essential. A support-selector word records which monomial of each Hamiltonian is active; it is not a periodic orbit of the polynomial state. A cycle of a max-plus state is not automatically a cycle of active supports. An externally switched matrix word does not become endogenous merely because its product is periodic. Likewise, a reduced word for an automorphism and a base expansion of a rank-one product carry different kinds of information. We therefore retain the support word, the weight orbit modulo diagonal translation, the full polynomial state, and the scalar weight sequences as separate objects throughout.

Our answer is family-wise. For every rooted primitive selector-pair word of length $\ell\geq3$, one explicit autonomous polynomial symplectomorphism on $2(\ell+1)$ affine coordinates realizes that word as its strict endogenous actual weighted-degree selector cycle for every nonzero coefficient tuple and every positive momentum seed in the exact first-carry chamber; it also admits a rational-polyhedral necessary-and- sufficient selector criterion, has separate least selector and quotient periods $\ell$, and has a marked period monodromy that recovers the rooted support-vector word, with literal labels requiring the labelled support dictionary. Thus there is one map per rooted word. There is not a single map for all words, a map determined by length alone, or a fixed-dimensional realization for unbounded length.

## Main theorem

The complete statement below separates the general fan classification from the particular incidence construction and from the polynomial leading-form lift. All inequalities between vectors are coordinatewise.

[\[thm:main\]]{#thm:main label="thm:main"} Let $\Bbbk$ be a field of characteristic zero, and let $$\mathsf{w}=((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1})),
 \qquad \ell\geq3,
 \label{eq:word}$$ be a rooted primitive pair word. Repeated labels are permitted, and either component alphabet may be a singleton. Put $r=\ell+1$. For every choice of integers $H\geq2$, $\rho\geq2$, and $K\geq1$, and for every choice of nonzero displayed coefficients in $\Bbbk$, the incidence construction of Section 4 defines a fixed autonomous polynomial map $F_{\mathsf{w}}$ on $\Bbbk^{2r}$, with the positive position seed $u_0=\mathbf{1}+(H-1)e_0$, all support coordinates at least two, and all support totals equal, having the following properties.

1.  The ordered composition of the two Hamiltonian gradient shears and the simultaneous permutation is a polynomial symplectomorphism. Its inverse is the explicit reverse-order composition stated in Proposition [\[prop:symplectic-inverse\]](#prop:symplectic-inverse){reference-type="ref" reference="prop:symplectic-inverse"}.

2.  More generally, for arbitrary positive equal-total V and W supports, a declared rooted residual selector word is strict exactly when its positive position seed lies in the pulled-back intersection of the strict V-max and strict W-min normal cones. This is a rational homogeneous open polyhedral cone. The equivalence classifies position-weight selectors; it does not by itself identify actual polynomial weighted degrees.

3.  The incidence supports realize the word $\mathsf{w}$ with a moving $\ell$-cycle and one fixed coordinate. The support data and coefficients are fixed before iteration. Every competitor that exists is separated by the exact positive gap $K(H-1)$. On a singleton side uniqueness is vacuous, its normal cone is the full positive weight space, and no finite competitor gap is assigned.

4.  If the positive initial momentum weight satisfies the strict chamber condition $0<m_0<A_{\alpha_{a_0}}u_0$, then the selected formal matrices are the actual polynomial weighted-degree transport for every nonzero coefficient tuple. The condition $0<m_0\leq u_0$ is a convenient sufficient subcone, but is not necessary. The asserted lift does not cover positive momentum seeds outside the strict chamber.

5.  With the literal order $Q_s=C_{s-1}\cdots C_0$, every prefix is a rank-one perturbation of $P^s$. Since $P^\ell=I$, the period monodromy $M_{\mathsf{w}}$ is a rank-one perturbation of the identity, with the exact characteristic polynomial, nonnegative powers, and phase-prefix formula of Theorem [\[thm:ordered-monodromy\]](#thm:ordered-monodromy){reference-type="ref" reference="thm:ordered-monodromy"}.

6.  Given $M_{\mathsf{w}},P,\lambda,\ell$, and marked phase zero, a coordinatewise carry-free base-$\lambda$ expansion recovers the rooted ordered digit-vector word. Adding the unlabelled support dictionary recovers the rooted exponent-support pairs, and adding its labels recovers the literal pair word. Without literal names, labels are determined only up to independent renaming of the two alphabets; without marked phase zero, only the cyclic rotation class is intrinsic.

7.  The selector word has least period $\ell$, and the position-weight orbit modulo $\mathbb R\mathbf{1}$ separately has least period $\ell$. Neither statement makes the polynomial state periodic.

8.  The position maximum $q_n$ obeys both the stated order-two annihilator and the length-$\ell$ annihilator for $n\geq0$. Each moving coordinate and the separately defined star coordinate obey the coordinate annihilator for $n\geq0$; every phase subsequence obeys its order-two annihilator for $m\geq0$. The complete-state maximum $d_n$ obeys the length-$\ell$ annihilator only for $n\geq1$, and its removed $n=0$ equation holds exactly when $\max_i(m_0)_i\leq\max_i(u_0)_i$. These relations are annihilators, not minimal recurrences, and no scalar trajectory decodes the word.

The theorem combines eight conclusions, but their proofs do not form a single linear calculation. Symplecticity is a map-level argument. The fan criterion and incidence construction form the selector branch. Strict carries and leading forms form the actual-degree branch. The two branches join only in Proposition [\[prop:leading-survival\]](#prop:leading-survival){reference-type="ref" reference="prop:leading-survival"}; monodromy, decoding, periods, and scalar consequences are derived after that join.

## Established neighbors and roadmap

Several individual ingredients have substantial precedents. Polynomial symplectomorphisms and polynomial-automorphism words are established subjects [@JaneczkoJelonek2008; @FriedlandMilnor1989]. Weighted degrees, leading parts, valuations, and inequality-defined regions occur in work on affine-triangular and tame automorphisms [@BlancVanSanten2022; @MeunierPreliminary; @ShaoSun2025]. Monomial maps provide degree chambers and recurrence phenomena; when invoking the precise degree-growth framework we keep the original and its corrigendum together [@HasselblattPropp2007; @HasselblattProppCorrigendum2007; @BedfordKim2008]. Nonlinear and max-plus dynamics exhibit long state cycles [@Gunawardena2003; @AkianGaubertLemmensNussbaum2006; @OhmoriYamazaki2024], and switched systems support periodic external schedules [@ZorzenonKomendaRaisch2024]. Cluster maps supply structured symplectic or Poisson dynamics, sign itineraries, tropical recurrences, and ordered presentation matrices [@FordyHone2011; @FordyHone2014; @IshibashiKano2021; @Kim2026]. Algebraic- entropy theory gives a broader degree-growth context [@BellonViallet1999; @HoneRagniscoZullo2016].

::: {#tab:neighbors}
  Established ingredient                                                                                                                               Separation in the present result
  ---------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  Polynomial symplectomorphisms and automorphism words [@JaneczkoJelonek2008; @FriedlandMilnor1989]                                                    Symplecticity and word decompositions do not provide the incidence selector construction, its fan criterion, or its decoder.
  Weighted degrees and chamber geometry [@BlancVanSanten2022; @MeunierPreliminary; @ShaoSun2025]                                                       Leading-part and inequality-region methods are background; the two-fan every-word theorem and strict carry lift are proved here.
  Monomial degree recurrences [@HasselblattPropp2007; @HasselblattProppCorrigendum2007; @BedfordKim2008]                                               A stationary monomial map has neither the endogenous support-pair word nor the marked support decoder constructed below.
  Max-plus state cycles and switched schedules [@Gunawardena2003; @AkianGaubertLemmensNussbaum2006; @OhmoriYamazaki2024; @ZorzenonKomendaRaisch2024]   A state period differs from a selector period, and an external schedule differs from selection by one fixed autonomous map.
  Cluster and tropical products [@FordyHone2011; @FordyHone2014; @IshibashiKano2021; @Kim2026]                                                         Their structured mutation or sign words do not give every prescribed primitive support-pair word in positive-support Hamiltonian shears.
  Degree-growth and entropy context [@BellonViallet1999; @HoneRagniscoZullo2016]                                                                       We derive exact chambered weighted-degree transport but draw no entropy, dynamical-degree, or integrability conclusion.

  : Established ingredients and the separation used here.
:::

The comparison is deliberately conjunctive. After a bounded search of public primary literature and official bibliographic records through 29 August 2026 UTC, we are unaware of a prior theorem that simultaneously combines realization of every rooted primitive selector-pair word of length at least three; one autonomous polynomial symplectomorphism per word; a rational-polyhedral necessary-and-sufficient strict-selector chamber; coefficient-uniform survival of the actual polynomial weighted-degree transport; separate least selector and diagonal-quotient periods; and exact marked monodromy recovery of the rooted support-pair word with the declared side information. This is a bounded positioning statement, not an absence proof, and no established ingredient in Table [1](#tab:neighbors){reference-type="ref" reference="tab:neighbors"} is claimed as new by itself.

Section 2 fixes the symplectic family and the formal selected matrices. Section 3 proves the general V-max/W-min fan equivalence. Section 4 gives the incidence construction for arbitrary primitive words. Section 5 proves strict carries and coefficient-uniform leading-form survival. Section 6 derives the ordered monodromy and decoder, and Section 7 separates periods and recurrence domains while recording sharp failures. Section 8 states the resulting scope. Every proof and counterexample needed for Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} appears in the main body.

# Symplectic family and exact weighted-degree transport

## Inputs, supports, and notation

Only labels that actually occur in $\mathsf{w}$ are used. Set $I_{\mathrm{mov}}=\{0,\ldots,\ell-1\}$, adjoin a separate symbol $\star$, and write $I=I_{\mathrm{mov}}\sqcup\{\star\}$. The standard basis of $\mathbb R^r$ is indexed by $I$. We use the permutation matrix specified by $$Pe_j=e_{j+1\pmod\ell},\qquad Pe_\star=e_\star,
 \qquad P^\ell=I,\qquad P\mathbf{1}=\mathbf{1}.
 \label{eq:permutation}$$ The phase-zero position weight is the positive spike $$u_0=\mathbf{1}+(H-1)e_0.
 \label{eq:spike}$$ For every used V label $a$ and W label $b$, let $S_a=\{j:a_j=a\}$ and $T_b=\{j:b_j=b\}$. These occurrence sets are nonempty, and distinct used labels have disjoint, hence distinct, occurrence sets. Repeated occurrences of one label are collected into one exponent. Define $$\begin{aligned}
 \alpha_a&=\rho\mathbf{1}+K\sum_{j\in S_a}e_j
       +K(\ell-|S_a|)e_\star,\\
 \beta_b&=\rho\mathbf{1}+K\sum_{j\notin T_b}e_j
       +K|T_b|e_\star.
 \end{aligned}
 \label{eq:incidence-exponents}$$ Every coordinate of these exponents is at least $\rho\geq2$. In both families the added $K$-mass is $K\ell$, so the common total is $$D=\rho r+K\ell.
 \label{eq:common-total}$$ With arbitrary displayed coefficients $\xi_a,\zeta_b\in\Bbbk^*$, use multi-index notation to set $$V_{\mathsf{w}}(q)=\sum_a\xi_a q^{\alpha_a},
 \qquad
 W_{\mathsf{w}}(p)=\sum_b\zeta_b p^{\beta_b}.
 \label{eq:hamiltonians}$$ A zero displayed coefficient would change the collected support and is not part of this definition.

::: {#tab:notation}
  Symbol                                                                              Meaning and domain
  ----------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  $\Bbbk$                                                                             Coefficient field of characteristic zero.
  $\mathsf{w}=((a_j,b_j))_{j=0}^{\ell-1}$                                             Rooted primitive selector-pair word, $\ell\geq3$.
  $r$                                                                                 $\ell+1$ symplectic coordinate pairs; ambient dimension $2r$.
  $I_{\mathrm{mov}},\star,I$                                                          Moving indices $\{0,\ldots,\ell-1\}$, fixed index, and their disjoint union.
  $P$                                                                                 Moving $\ell$-cycle fixing $\star$, with $P^\ell=I$ and $P\mathbf{1}=\mathbf{1}$.
  $H,\rho,K$                                                                          Integers with $H\geq2$, $\rho\geq2$, and $K\geq1$.
  $u_0,m_0$                                                                           Positive initial position and momentum weights; $u_0$ is the spike in [\[eq:spike\]](#eq:spike){reference-type="eqref" reference="eq:spike"}.
  $S_a,T_b$                                                                           Occurrence sets of used V and W labels.
  $\alpha_a,\beta_b$                                                                  Collected incidence exponents in [\[eq:incidence-exponents\]](#eq:incidence-exponents){reference-type="eqref" reference="eq:incidence-exponents"}.
  $D$                                                                                 Common exponent total $\rho r+K\ell$.
  $V_{\mathsf{w}},W_{\mathsf{w}}$                                                     Collected-support Hamiltonians with nonzero coefficients.
  $S_V,T_W,\Pi_P,F_{\mathsf{w}}$                                                      Gradient shears, simultaneous permutation, and their ordered composition.
  $A_\alpha,B_\beta$                                                                  Selected gradient matrices $\mathbf{1}\alpha^{\mathsf T}-I$ and $\mathbf{1}\beta^{\mathsf T}-I$.
  $c_{a,b},\lambda,C_{a,b}$                                                           Digit, base, and selected position matrix.
  $x_n,t_n$                                                                           Residual and diagonal parts of $u_n=x_n+t_n\mathbf{1}$.
  $\sigma_0,g,\mu$                                                                    Base score, existing-competitor gap, and scalar forcing.
  $Q_s,R_s,M_{\mathsf{w}}$                                                            Ordered prefix, rank-one row, and period monodromy.
  $q_n,d_n$                                                                           Position maximum and complete-state maximum.
  $y_n^{(i)},z_m^{(i,s)}$                                                             Position coordinate and phase subsequence; the star formula is separate.
  $\mathcal{N}_{V}^{+}(\alpha),\mathcal{N}_{W}^{-}(\beta),\mathcal{C}_{\mathsf{w}}$   Strict V-max cone, strict W-min cone, and pulled-back selector cone.

  : Notation used in the construction and its consequences.
:::

Definitions in Table [2](#tab:notation){reference-type="ref" reference="tab:notation"} are mnemonic. Whenever a hypothesis affects a result, it is repeated in that result. In particular, the same symbol $W$ is never used for the input word, and $m_n$ always denotes a momentum weight rather than a phase index.

## Symplectic shears and inverse

Define the two gradient shears and the simultaneous permutation. For later reference we display their Jacobians and the standard symplectic matrix in the same order as the maps: $$\begin{aligned}
 S_V(q,p)&=(q,p+\nabla V(q)),&
 T_W(q,p)&=(q+\nabla W(p),p),&
 \Pi_P(q,p)&=(Pq,Pp),
 \label{eq:shears}\\
 DS_V&=\begin{pmatrix}I&0\\ \operatorname{Hess}V&I\end{pmatrix},&
 DT_W&=\begin{pmatrix}I&\operatorname{Hess}W\\0&I\end{pmatrix},&
 J&=\begin{pmatrix}0&I\\-I&0\end{pmatrix},
 \notag\\
 F_{\mathsf{w}}&=\Pi_P\circ T_{W_{\mathsf{w}}}\circ S_{V_{\mathsf{w}}}.
 \label{eq:map-order}\end{aligned}$$

[\[prop:symplectic-inverse\]]{#prop:symplectic-inverse label="prop:symplectic-inverse"} The map $F_{\mathsf{w}}$ in [\[eq:map-order\]](#eq:map-order){reference-type="eqref" reference="eq:map-order"} is a polynomial symplectomorphism. For an output $(Q,\mathsf P)$, put $\bar q=P^{-1}Q$ and $\bar p=P^{-1}\mathsf P$. Its inverse is $$F_{\mathsf{w}}^{-1}(Q,\mathsf P)=
 \left(
  \bar q-\nabla W_{\mathsf{w}}(\bar p),
  \bar p-\nabla V_{\mathsf{w}}
     (\bar q-\nabla W_{\mathsf{w}}(\bar p))
 \right).
 \label{eq:inverse}$$

The two Hessians in [\[eq:shears\]](#eq:shears){reference-type="eqref" reference="eq:shears"} are symmetric. Direct block multiplication gives $(DS_V)^{\mathsf T}JDS_V=J$ and $(DT_W)^{\mathsf T}JDT_W=J$; equivalently, the additional $dq_i\wedge dq_j$ and $dp_i\wedge dp_j$ terms cancel in pairs. Because $P$ is a permutation matrix, $P^{\mathsf T}P=I$, and applying the same $P$ to the two halves also preserves $J$. Composition therefore proves symplecticity without appealing to a degree matrix.

Each factor is a polynomial automorphism. Starting from $(Q,\mathsf P)$, the inverse permutation gives $(\bar q,\bar p)$. The inverse W shear gives $(\bar q-\nabla W_{\mathsf{w}}(\bar p),\bar p)$, and the inverse V shear then subtracts the V gradient evaluated at that recovered position. This is exactly [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"}; substitution in the two directions verifies the identity. Acting with unrelated permutations on the q and p halves would not in general preserve the standard symplectic form, which is why the simultaneous permutation is part of the construction.

## Selected gradient matrices

For a positive weight vector $u$, the weighted degree of a monomial $q^\gamma$ is $\gamma^{\mathsf T}u$. A unique maximizing support exponent is its unique leading support monomial. In the derivative row indexed by $i$, differentiating subtracts $u_i$ from that degree. The assumption that every coordinate is at least two ensures that the derivative appears in every row, and characteristic zero ensures that its scalar is nonzero.

[\[lem:selected-matrices\]]{#lem:selected-matrices label="lem:selected-matrices"} If $\alpha$ and $\beta$ are the unique selected V and W exponents, then the rowwise gradient degree vectors are governed by $$A_\alpha=\mathbf{1}\alpha^{\mathsf T}-I,
 \qquad
 B_\beta=\mathbf{1}\beta^{\mathsf T}-I.
 \label{eq:selected-matrices}$$ If the V exponents have common total $A$ and the W exponents have common total $B$, then $$\begin{aligned}
 B_\beta A_\alpha
   &=I+\mathbf{1}\bigl((B-1)\alpha-\beta\bigr)^{\mathsf T},\\
 C_{a,b}:=PB_{\beta_b}A_{\alpha_a}
   &=P+\mathbf{1}c_{a,b}^{\mathsf T}
   \qquad\text{when }A=B=D.
 \end{aligned}
 \label{eq:rank-one-product}$$ For the incidence supports, $$c_{a,b}=(D-1)\alpha_a-\beta_b,
 \qquad
 \lambda=(D-1)^2,
 \qquad
 c_{a,b}^{\mathsf T}\mathbf{1}=\lambda-1.
 \label{eq:digit-definition}$$

The selected monomial in row $i$ has degree $\alpha^{\mathsf T}u-u_i$, which is row $i$ of $A_\alpha u$. The W calculation is identical. Multiplication of the two rank-one-minus- identity matrices gives an identity term and a rank-one row: the factor $\beta^{\mathsf T}\mathbf{1}=B$ supplies $(B-1)\alpha$, while the remaining W term supplies $-\beta$. Left multiplication by $P$ changes the identity part to $P$ and leaves $\mathbf{1}$ fixed. Finally, the sum of the coordinates of $(D-1)\alpha_a-\beta_b$ is $(D-1)D-D=(D-1)^2-1$, proving the last identity.

## Formal-versus-actual degree boundary

The matrices above record what a unique support selector would contribute. Weighted-degree and leading-part methods, including their chamber geometry, are established tools [@BlancVanSanten2022; @MeunierPreliminary; @ShaoSun2025], but those tools do not make a formal selector automatically survive all coordinate carries. Sections 2--4 classify strict position-weight selectors. Only Section 5 proves, under its exact gate, that these matrices are the actual polynomial weighted-degree transport. Nothing in this formal calculation is an ordinary-total-degree theorem, an unrestricted exact-degree invariant, or an algebraic- or dynamical-degree conclusion.

# Normal-fan iff

## Equal-total residual reduction

We first work with arbitrary nonempty finite supports $E_V,E_W\subset\mathbb Z_{\geq2}^{r}$, where every V exponent has total $A$ and every W exponent has total $B$. Fix a permutation satisfying $P\mathbf{1}=\mathbf{1}$, a declared residual return of length $\ell$, and a declared exponent word $((\alpha_0,\beta_0),\ldots,
(\alpha_{\ell-1},\beta_{\ell-1}))$. The strict cones for a candidate exponent are $$\begin{aligned}
 \mathcal{N}_{V}^{+}(\alpha)
  &=\{x>0:(\alpha-\gamma)^{\mathsf T}x>0
       \text{ for every competing }\gamma\in E_V\},\\
 \mathcal{N}_{W}^{-}(\beta)
  &=\{x>0:(\eta-\beta)^{\mathsf T}x>0
       \text{ for every competing }\eta\in E_W\}.
 \end{aligned}
 \label{eq:normal-fans}$$ Here a competing exponent means a distinct support element. The pulled-back cone associated with the rooted word is $$\mathcal{C}_{\mathsf{w}}
 =\mathbb R_{>0}^{r}\cap
  \bigcap_{j=0}^{\ell-1}P^{-j}
  \bigl(\mathcal{N}_{V}^{+}(\alpha_j)\cap\mathcal{N}_{W}^{-}(\beta_j)\bigr),
 \label{eq:selector-cone}$$ where $P^{-j}$ denotes inverse image: membership means that $P^ju_0$ belongs to the indicated cones.

For a selected pair at time $n$, write $C_n=P+\mathbf{1}c_n^{\mathsf T}$, with $c_n=((B-1)\alpha_n-\beta_n)$, and $\lambda=(A-1)(B-1)$. If the position weight is decomposed as $u_n=x_n+t_n\mathbf{1}$, literal multiplication gives $$C_n(x_n+t_n\mathbf{1})=Px_n+
 \bigl(c_n^{\mathsf T}x_n+\lambda t_n\bigr)\mathbf{1}.
 \label{eq:residual-step}$$ Thus diagonal translation remains diagonal and the residual evolves by $x_{n+1}=Px_n$. In particular, if $x_0=u_0$, then $x_n=P^nu_0$. This reduction uses equal totals but does not use the later incidence forcing or its closed form.

Equal V totals eliminate $t_n$ from every difference $(\alpha-\gamma)^{\mathsf T}u_n$. After V selects $\alpha_n$, its gradient weight is $A_{\alpha_n}u_n=(\alpha_n^{\mathsf T}x_n+(A-1)t_n)\mathbf{1}-x_n$. Consequently, for equal-total W exponents, the comparison reverses sign: $$(\beta-\eta)^{\mathsf T}A_{\alpha_n}u_n
 =-(\beta-\eta)^{\mathsf T}x_n.
 \label{eq:w-sign-reversal}$$ The W shear still selects its actual maximal weighted degree, but that maximization is equivalent to minimizing $\beta^{\mathsf T}x_n$ on the residual position weight. This is the source of the V-max/W-min asymmetry. Weighted-degree regions in polynomial-automorphism theory provide useful background for such comparisons [@BlancVanSanten2022; @MeunierPreliminary; @ShaoSun2025]; the equivalence below is proved directly from the displayed residual identities.

## Pulled-back V-max/W-min criterion

[\[thm:selector-fan\]]{#thm:selector-fan label="thm:selector-fan"} In the positive equal-total support class just described, the declared rooted exponent word is the strict selector word along the length- $\ell$ residual return if and only if $u_0\in\mathcal{C}_{\mathsf{w}}$, with $\mathcal{C}_{\mathsf{w}}$ defined by [\[eq:selector-cone\]](#eq:selector-cone){reference-type="eqref" reference="eq:selector-cone"}. The assertion is a classification of selectors from position weights. It is not an equivalence for the actual polynomial weighted-degree lift.

Suppose first that the declared word is selected strictly. At phase $j$, equal totals show that every V comparison can be made at $x_j=P^ju_0$. Strict selection of $\alpha_j$ therefore places $x_j$ in $\mathcal{N}_{V}^{+}(\alpha_j)$. Formula [\[eq:w-sign-reversal\]](#eq:w-sign-reversal){reference-type="eqref" reference="eq:w-sign-reversal"} shows that strict selection of $\beta_j$ by the second shear places the same residual weight in $\mathcal{N}_{W}^{-}(\beta_j)$. This is true for every $j$, so the seed belongs to every inverse image in [\[eq:selector-cone\]](#eq:selector-cone){reference-type="eqref" reference="eq:selector-cone"}.

Conversely, let $u_0\in\mathcal{C}_{\mathsf{w}}$. The $j$-th inverse-image condition says that $x_j=P^ju_0$ lies in the strict V cone of $\alpha_j$ and the strict W-min cone of $\beta_j$. Equal totals make the V inequalities unchanged by any diagonal part of $u_j$, so V selects $\alpha_j$ uniquely. Equation [\[eq:w-sign-reversal\]](#eq:w-sign-reversal){reference-type="eqref" reference="eq:w-sign-reversal"} turns every strict W-min residual inequality into the strict maximal weighted-degree inequality after the V shear. Thus W selects $\beta_j$ uniquely. The residual update [\[eq:residual-step\]](#eq:residual-step){reference-type="eqref" reference="eq:residual-step"} advances to $P^{j+1}u_0$, closing the induction through the declared return. No momentum carry or polynomial leading-form assertion is used in either direction.

[\[cor:rational-seed\]]{#cor:rational-seed label="cor:rational-seed"} The cone $\mathcal{C}_{\mathsf{w}}$ is rational, homogeneous, open, and polyhedral. If it is nonempty, it contains a positive rational point and hence, after positive scaling, a positive integer point.

Every support exponent and permutation matrix is integral. The cone is a finite intersection of strict rational homogeneous half-spaces with the positive orthant, proving the first assertion. An open nonempty subset of its real linear span contains rational points because rational vectors are dense there. The positive and strict inequalities persist under a common positive scaling, so clearing denominators produces a positive integer seed.

## Rationality, walls, and singleton supports

[\[cex:fan-wall\]]{#cex:fan-wall label="cex:fan-wall"} If at some phase either $(\alpha-\gamma)^{\mathsf T}P^ju_0=0$ or $(\beta-\eta)^{\mathsf T}P^ju_0=0$, two support exponents have equal weighted degree on the relevant side. The selector is not unique, so the strict theorem does not supply a tie-breaking rule.

This example explains why closure of the cone cannot replace the cone in Theorem [\[thm:selector-fan\]](#thm:selector-fan){reference-type="ref" reference="thm:selector-fan"}. The wall is not a harmless lower-dimensional case: choosing either tied exponent may alter the subsequent rank-one matrix and hence the entire ordered product. Strictness is therefore part of the statement, not merely a convenient proof device.

[\[rem:singleton\]]{#rem:singleton label="rem:singleton"} If one support contains a single exponent, its competitor family in [\[eq:normal-fans\]](#eq:normal-fans){reference-type="eqref" reference="eq:normal-fans"} is empty. The corresponding strict cone is the full positive weight space, and the sole support element is unique vacuously. There is no competitor against which to measure a finite gap. This permits a singleton V or W alphabet without weakening primitivity of the pair word.

Equal totals are also structural. If totals differ, a comparison between two exponents contains a multiple of the diagonal coordinate $t_n$. The residual dynamics then no longer determines the selector word, and the frozen normal-fan reduction need not hold. This is a boundary of the theorem rather than a claim about how unequal-total systems behave.

## Selector/carry separation

The logical separation used later can be stated compactly:

The momentum condition is intentionally absent from Theorem [\[thm:selector-fan\]](#thm:selector-fan){reference-type="ref" reference="thm:selector-fan"}. Conversely, satisfying a momentum inequality cannot repair a selector tie. Keeping these obligations separate prevents a formal matrix itinerary from being mistaken for an actual polynomial leading-degree statement.

# Incidence realization of primitive words

## Moving cycle, fixed star, and supports

We now specialize the general fan theorem to the supports in [\[eq:incidence-exponents\]](#eq:incidence-exponents){reference-type="eqref" reference="eq:incidence-exponents"}. Their form is dictated by two complementary incidence requirements. On the V side, the moving coordinates at which a label occurs receive an additional $K$. On the W side, the moving coordinates at which a label does not occur receive the additional $K$. The star coordinate receives exactly the amount needed to make the two families equal-total. This complementarity is responsible for selecting V by a maximum and W by a minimum at the same residual spike.

The moving cycle and fixed star serve different purposes. The cycle carries the unique height-$H$ entry of $u_0$ through the phases. The star never contains that spike, so later it detects whether two residual weights differ by a diagonal vector. The extra coordinate is therefore not an unused padding coordinate: it fixes total degrees and witnesses the least quotient period. Since $r=\ell+1$, its inclusion makes the affine symplectic dimension exactly $2(\ell+1)$.

For a used V label, the support vector records its complete occurrence set, not the current phase. If $a\neq a'$, then $S_a$ and $S_{a'}$ are nonempty disjoint subsets and hence give different exponent vectors. Likewise distinct W labels have distinct nonempty $T_b$. Repetition in the word is thus represented by revisiting one fixed support vector; it does not introduce duplicate monomials or time-dependent coefficients. A singleton component alphabet is also allowed: its one occurrence set is the entire phase set, while primitivity remains a property of the pair word.

All coordinates in [\[eq:incidence-exponents\]](#eq:incidence-exponents){reference-type="eqref" reference="eq:incidence-exponents"} are at least two, and the total calculation in [\[eq:common-total\]](#eq:common-total){reference-type="eqref" reference="eq:common-total"} is exact. These two features will be reused for nonvanishing derivatives and coefficient-uniform leading forms in Section 5. At this stage they merely place the supports in the positive equal-total class of Theorem [\[thm:selector-fan\]](#thm:selector-fan){reference-type="ref" reference="thm:selector-fan"}.

## Exact score table

At phase $j$, let $x_j=P^ju_0$. It has value $H$ in moving coordinate $j$, value one in every other moving coordinate, and value one at $\star$. Separate the contribution of the baseline $\rho\mathbf{1}$ from the incidence additions, and put $$\sigma_0=\rho(H+\ell)+K\ell,
 \qquad
 g=K(H-1)>0.
 \label{eq:score-constants}$$ The baseline dot product is $\rho(H+\ell)$, because there are $\ell$ entries equal to one in addition to the excess $H-1$ at the spike. On the V side the $K$-mass has baseline contribution $K\ell$. It gains an additional $K(H-1)$ exactly when the spike index belongs to $S_a$. On the W side the same reasoning uses the complement of $T_b$: it gains the additional amount exactly when the spike index does not belong to $T_b$. Thus $$\alpha_a^{\mathsf T}x_j
   =\sigma_0+g\mathbf1_{\{j\in S_a\}},
 \qquad
 \beta_b^{\mathsf T}x_j
   =\sigma_0+g\mathbf1_{\{j\notin T_b\}}.
 \label{eq:score-table}$$

At phase $j$, the selected V label satisfies $j\in S_{a_j}$, so its score is $\sigma_0+g$. Every different V label has a disjoint occurrence set, so, if a competitor exists, its score is $\sigma_0$. Hence $\alpha_{a_j}$ is the unique strict maximizer and selected-minus- competitor is exactly $g$. On the W side the selected label satisfies $j\in T_{b_j}$, so its score is $\sigma_0$. Any different W occurrence set omits $j$, and its score is $\sigma_0+g$. Hence $\beta_{b_j}$ is the unique strict minimizer and competitor-minus-selected is exactly $g$. These are precisely the signs required by Theorem [\[thm:selector-fan\]](#thm:selector-fan){reference-type="ref" reference="thm:selector-fan"}.

The phrase "against every competitor" is conditional on a competitor existing. If a component alphabet is a singleton, its one support is selected vacuously at every phase, its cone contributes no inequalities, and there is no finite pair of scores from which to report a gap. Formula [\[eq:score-table\]](#eq:score-table){reference-type="eqref" reference="eq:score-table"} remains true, but it is not converted into a fictitious margin.

## Endogenous every-word realization

[\[thm:incidence-realization\]]{#thm:incidence-realization label="thm:incidence-realization"} For every rooted primitive pair word $\mathsf{w}$ in [\[eq:word\]](#eq:word){reference-type="eqref" reference="eq:word"}, including words with repeated labels and with either component alphabet a singleton, the support construction [\[eq:incidence-exponents\]](#eq:incidence-exponents){reference-type="eqref" reference="eq:incidence-exponents"} and spike [\[eq:spike\]](#eq:spike){reference-type="eqref" reference="eq:spike"} realize the prescribed strict support-pair selector word indefinitely. The selected V exponent is a strict residual maximizer and the selected W exponent is a strict residual minimizer at each phase. Every competitor that exists has exact gap $g=K(H-1)$. All supports and coefficients are fixed before iteration; no phase-dependent Hamiltonian or external schedule supplies the word.

Formula [\[eq:score-table\]](#eq:score-table){reference-type="eqref" reference="eq:score-table"} proves the strict phase-$j$ comparisons for each $0\leq j<\ell$, and [\[eq:permutation\]](#eq:permutation){reference-type="eqref" reference="eq:permutation"} returns the residual spike after $\ell$ phases. Theorem [\[thm:selector-fan\]](#thm:selector-fan){reference-type="ref" reference="thm:selector-fan"} therefore places $u_0$ in the required selector cone and repeats the word on every residual period. The support vectors depend only on the complete occurrence sets, and the polynomials in [\[eq:hamiltonians\]](#eq:hamiltonians){reference-type="eqref" reference="eq:hamiltonians"} are formed once, so the selection is endogenous to one autonomous map.

The proof so far is a formal strict-selector proof. For the canonical choice $m_0=\mathbf{1}$, Lemma [\[lem:strict-growth\]](#lem:strict-growth){reference-type="ref" reference="lem:strict-growth"} below will show $0<m_0\leq u_0<A_{\alpha_{a_0}}u_0$. Theorem [\[thm:carry-lift\]](#thm:carry-lift){reference-type="ref" reference="thm:carry-lift"} and Proposition [\[prop:leading-survival\]](#prop:leading-survival){reference-type="ref" reference="prop:leading-survival"} then upgrade the selector itinerary to the actual polynomial weighted-degree itinerary. That upgrade is not used here, preserving the separation between fan selection and carry.

This autonomous feature differs from a periodically switched schedule, where the mode word is supplied as data at each step [@ZorzenonKomendaRaisch2024]. Here the current residual spike and the fixed Newton supports decide the active pair. The map depends on the rooted word, and its dimension grows with $\ell$; the theorem does not identify a universal map or a length-only map.

## Hand-derived audit fixture and sharp incidence boundaries

[\[ex:ell-three-fixture\]]{#ex:ell-three-fixture label="ex:ell-three-fixture"} Take $\mathsf{w}=((A,X),(B,X),(A,Y))$ and $(\ell,r,\rho,K,H)=(3,4,2,1,2)$, with coordinates $(0,1,2,\star)$. Directly from [\[eq:incidence-exponents\]](#eq:incidence-exponents){reference-type="eqref" reference="eq:incidence-exponents"}, the four support vectors are

$\alpha_A=(3,2,3,3),\quad \alpha_B=(2,3,2,4),\quad
\beta_X=(2,2,3,4),\quad \beta_Y=(3,3,2,3).$

Each has total $D=11$. The spike is $u_0=(2,1,1,1)$, and direct substitution gives $\sigma_0=13$, $g=1$, and $\lambda=100$. At the three phases the V maximizers are $A,B,A$, while the W minimizers are $X,X,Y$, exactly as the repeated-label word prescribes. This hand-derived fixture checks notation and illustrates collection of repeated labels; it is not evidence for the universal quantifier in Theorem [\[thm:incidence-realization\]](#thm:incidence-realization){reference-type="ref" reference="thm:incidence-realization"}.

The strict spike hypothesis is sharp for this incidence mechanism. When $H=1$, the seed is diagonal, $g=0$, all incidence distinctions in [\[eq:score-table\]](#eq:score-table){reference-type="eqref" reference="eq:score-table"} disappear, and selector ties arise whenever there is a competitor. The residual class is then fixed rather than tracing the moving cycle, so the quotient geometry collapses as well. This failure does not contradict the fan theorem; it says that the specific seed lies on its walls instead of in the strict cone.

# Strict carries and leading forms

## Strict growth in positive dimension

The fan criterion chooses support exponents but does not compare their gradient degrees with the carried coordinate terms. The following coordinate inequality supplies that comparison in dimension at least two.

[\[lem:strict-growth\]]{#lem:strict-growth label="lem:strict-growth"} Let $r\geq2$, let $u>0$, and let $\alpha\in\mathbb Z_{\geq2}^{r}$. Then $A_\alpha u>u$ coordinatewise. More precisely, $$(A_\alpha u)_i-u_i
  =(\alpha_i-2)u_i+\sum_{k\ne i}\alpha_k u_k>0.
 \label{eq:strict-growth}$$ The identical statement holds for $B_\beta$ when every coordinate of $\beta$ is at least two.

The $i$-th row of $A_\alpha u$ is $\alpha^{\mathsf T}u-u_i$. Subtracting another $u_i$ yields the identity in [\[eq:strict-growth\]](#eq:strict-growth){reference-type="eqref" reference="eq:strict-growth"}. Its first summand is nonnegative, and because $r\geq2$, the remaining sum contains at least one strictly positive term. The proof for B is the same.

The headline construction has $r=\ell+1\geq4$, but the lemma is stated at the natural general threshold. No coefficient sign occurs in this matrix inequality. Dimension one is excluded because the positive cross-coordinate sum on the right of [\[eq:strict-growth\]](#eq:strict-growth){reference-type="eqref" reference="eq:strict-growth"} would be empty.

## Exact first-carry chamber and induction

Let $u_n$ and $m_n$ denote, respectively, the position and momentum weighted-degree vectors before the $n$-th application of $F_{\mathsf{w}}$. Assume that the strict selector at phase zero is $\alpha_{a_0}$. The exact initial chamber used by the lift is $$0<m_0<A_{\alpha_{a_0}}u_0
 \qquad\text{coordinatewise}.
 \label{eq:first-carry-gate}$$

[\[thm:carry-lift\]]{#thm:carry-lift label="thm:carry-lift"} Suppose $r\geq2$, all selected exponent coordinates are at least two, the position selectors are strict, and [\[eq:first-carry-gate\]](#eq:first-carry-gate){reference-type="eqref" reference="eq:first-carry-gate"} holds. Then the selected gradient term strictly dominates the carried coordinate at every shear and every phase. In particular, $$m_{n+1}=PA_{\alpha_n}u_n,
 \qquad
 u_{n+1}=PB_{\beta_n}A_{\alpha_n}u_n
 \qquad(n\geq0).
 \label{eq:weight-transport}$$ Moreover $u_n>m_n$ for every $n\geq1$. The chamber [\[eq:first-carry-gate\]](#eq:first-carry-gate){reference-type="eqref" reference="eq:first-carry-gate"} is exactly the strict phase-zero source-carry condition used in this argument. The smaller chamber $0<m_0\leq u_0$ is sufficient but not necessary.

Put $v_0=A_{\alpha_{a_0}}u_0$. The first inequality in [\[eq:first-carry-gate\]](#eq:first-carry-gate){reference-type="eqref" reference="eq:first-carry-gate"} makes the V-gradient contribution strictly larger than the carried momentum coordinate in every row, so the intermediate momentum degree is exactly $v_0$. Lemma [\[lem:strict-growth\]](#lem:strict-growth){reference-type="ref" reference="lem:strict-growth"} applied to the selected W exponent gives $B_{\beta_0}v_0>v_0$, while the same lemma for V gives $v_0>u_0$. The W-gradient term therefore strictly dominates the carried position coordinate. After applying $P$, the new weights are $m_1=Pv_0$ and $u_1=PB_{\beta_0}v_0$, so $u_1>m_1$.

Assume inductively that $u_n>m_n$ for some $n\geq1$. Strict matrix growth gives $A_{\alpha_n}u_n>u_n>m_n$. Thus the V-gradient again wins the source carry. Applying strict growth once more gives $B_{\beta_n}A_{\alpha_n}u_n>A_{\alpha_n}u_n>u_n$, so the W-gradient wins the target carry. A permutation preserves coordinatewise inequalities, which proves both identities in [\[eq:weight-transport\]](#eq:weight-transport){reference-type="eqref" reference="eq:weight-transport"} and closes the induction.

At phase zero, strict dominance of the selected V-gradient over the carried momentum is literally the upper inequality in [\[eq:first-carry-gate\]](#eq:first-carry-gate){reference-type="eqref" reference="eq:first-carry-gate"}, establishing the claimed exactness for this strict source-carry mechanism. If instead $0<m_0\leq u_0$, then Lemma [\[lem:strict-growth\]](#lem:strict-growth){reference-type="ref" reference="lem:strict-growth"} gives $m_0<A_{\alpha_{a_0}}u_0$, so this is a sufficient subcone. It is not necessary because vectors larger than $u_0$ in some coordinates may still lie strictly below $A_{\alpha_{a_0}}u_0$.

For the incidence construction, $m_0=\mathbf{1}$ is always admissible: $0<\mathbf{1}\leq u_0<A_{\alpha_{a_0}}u_0$. More generally, every positive momentum seed in the full chamber [\[eq:first-carry-gate\]](#eq:first-carry-gate){reference-type="eqref" reference="eq:first-carry-gate"} produces the same selected position-weight transport. We make no assertion that a seed outside that chamber has the advertised actual-degree lift.

## Coefficient-uniform survival

The carry theorem compares degrees. To identify those degrees with actual polynomial leading terms, one must also exclude cancellation after repeated substitution. The required argument is algebraic and uniform over all nonzero displayed coefficients.

[\[prop:leading-survival\]]{#prop:leading-survival label="prop:leading-survival"} Assume the strict selectors of Theorem [\[thm:selector-fan\]](#thm:selector-fan){reference-type="ref" reference="thm:selector-fan"}, the carry hypotheses of Theorem [\[thm:carry-lift\]](#thm:carry-lift){reference-type="ref" reference="thm:carry-lift"}, a characteristic-zero field, and support exponents whose coordinates are at least two. Then for every coefficient tuple $$(\xi,\zeta)\in(\Bbbk^*)^{|E_V|+|E_W|},
 \label{eq:coefficient-domain}$$ the matrices in [\[eq:weight-transport\]](#eq:weight-transport){reference-type="eqref" reference="eq:weight-transport"} give the actual polynomial weighted-degree vectors at every iterate. No genericity or coefficient-sign hypothesis is needed.

We use four elementary facts about weighted leading forms over a polynomial ring. The weighted degree of a product of nonzero polynomials is the sum of their degrees. A unique maximal support monomial cannot cancel with a different support monomial. In a sum of two terms of strictly different degree, the larger term survives. Finally, the polynomial ring over a field is a domain, so a product of nonzero leading forms remains nonzero.

At a selected V phase, strictness isolates one exponent $\alpha_n$. In every gradient row its derivative scalar is $(\alpha_n)_i\xi_{a_n}$, which is nonzero because the coefficient is nonzero, the exponent coordinate is at least two, and the field has characteristic zero. After substitution, the leading form of that derivative monomial is a product of nonzero coordinate leading forms and is therefore nonzero. No other V support exponent has the same weighted degree. The strict source carry from Theorem [\[thm:carry-lift\]](#thm:carry-lift){reference-type="ref" reference="thm:carry-lift"} also places the carried momentum coordinate at lower degree. Hence the actual intermediate momentum vector is $A_{\alpha_n}u_n$.

The same reasoning applies to the uniquely selected W exponent after the V shear. Its derivative scalar and product leading form are nonzero, its support competitors have strictly lower degree, and the target carry is strictly lower than the W-gradient contribution. Applying the simultaneous permutation only reorders nonzero coordinate polynomials. This proves one step of [\[eq:weight-transport\]](#eq:weight-transport){reference-type="eqref" reference="eq:weight-transport"} at the level of actual polynomials. Induction starts from nonzero coordinate variables and repeats the same domain argument indefinitely.

No step requires avoiding an algebraic hypersurface in coefficient space: strict support degrees prevent cross-support cancellation, while the domain property prevents a selected product from vanishing. Thus the conclusion holds for every tuple in [\[eq:coefficient-domain\]](#eq:coefficient-domain){reference-type="eqref" reference="eq:coefficient-domain"}. Combining this proposition with Theorem [\[thm:incidence-realization\]](#thm:incidence-realization){reference-type="ref" reference="thm:incidence-realization"} completes the advertised endogenous actual weighted-degree realization.

This conclusion remains a chambered weighted-degree statement. It neither identifies ordinary total degrees of all iterates nor supplies an unrestricted algebraic-degree or dynamical-degree invariant. In particular, the formal rank-one matrices are not by themselves certificates of actual leading-term survival.

## Cancellation and support-boundary counterexamples

[\[cex:dimension-one\]]{#cex:dimension-one label="cex:dimension-one"} Over $\mathbb Q$, take $V(q)=q^2$ and $W(p)=-p^2/4$. The V shear sends $p$ to $p+2q$, but the next position coordinate after the W shear is $$q-\frac{p+2q}{2}=-\frac p2.
 \label{eq:dimension-one-cancellation}$$ The q contribution cancels even though the formal matrices are $A_2=B_2=[1]$. Thus the coefficient-uniform strict-lift theorem genuinely requires the higher-dimensional strict-growth mechanism.

Three further local hypotheses are equally visible in the proof. If an exponent coordinate is zero, differentiation in that row can delete the monomial entirely. In positive characteristic, a nonzero exponent may become a zero derivative scalar. If a displayed coefficient is zero, the collected support itself changes and so may its normal fan. The proposition does not classify cancellation after removing any of these hypotheses; it asserts survival exactly in the positive-support, characteristic-zero, nonzero-coefficient setting with strict carries.

# Ordered monodromy and decoding

## Constant scalar forcing

Return to the explicit incidence realization and abbreviate $c_j=c_{a_j,b_j}$ and $C_j=C_{a_j,b_j}$. The residual spike at phase $j$ is $x_j=P^ju_0$. The selected V score is $\sigma_0+g$, whereas the selected W score is $\sigma_0$. Hence the rank-one row has a phase-independent pairing with the current residual.

[\[lem:scalar-forcing\]]{#lem:scalar-forcing label="lem:scalar-forcing"} For the incidence construction, define $$\begin{aligned}
 \mu&=(D-1)(\sigma_0+g)-\sigma_0>0,\\
 u_n&=P^nu_0+t_n\mathbf{1},
 \qquad t_0=0,
 \qquad t_{n+1}=\lambda t_n+\mu.
 \end{aligned}
 \label{eq:scalar-forcing}$$ Then this decomposition holds for every $n\geq0$, and $$t_n=\mu\frac{\lambda^n-1}{\lambda-1}.
 \label{eq:t-closed}$$

By [\[eq:score-table\]](#eq:score-table){reference-type="eqref" reference="eq:score-table"}, the selected digit satisfies $c_j^{\mathsf T}x_j=(D-1)(\sigma_0+g)-\sigma_0=\mu$, independently of $j$. The quantity is positive because it can also be written $(D-2)\sigma_0+(D-1)g$, and all factors are positive. Substituting this value in the residual update [\[eq:residual-step\]](#eq:residual-step){reference-type="eqref" reference="eq:residual-step"} gives $u_{n+1}=P^{n+1}u_0+(\lambda t_n+\mu)\mathbf{1}$. Induction proves the decomposition and scalar recurrence. Summing its geometric progression gives [\[eq:t-closed\]](#eq:t-closed){reference-type="eqref" reference="eq:t-closed"}, since $\lambda=(D-1)^2>1$.

The constant scalar forcing is deliberate: it keeps the diagonal growth independent of the current letter pair while the residual spike selects the word. Consequently the scalar forcing carries no word information. The ordered vector digits, not this scalar sequence, retain the selector data.

## Ordered prefixes and period monodromy

Ordered tropical or presentation matrices also arise for structured cluster maps and sign-stable mutation loops [@FordyHone2011; @FordyHone2014; @IshibashiKano2021; @Kim2026]. Those settings motivate careful attention to multiplication order, but the formula and decoder below are specific to the present incidence supports. We use no general integrability assertion; in particular, conjectural statements for broad cluster families are not imported into the proof.

For $s\geq1$, define the prefix in chronological right-to-left order by $$Q_s=C_{s-1}\cdots C_1C_0,
 \qquad Q_0=I.
 \label{eq:prefix-definition}$$ Reversing this order would rotate different digits and would change the monodromy.

[\[thm:ordered-monodromy\]]{#thm:ordered-monodromy label="thm:ordered-monodromy"} For every $s\geq0$, $$\begin{aligned}
 Q_s&=P^s+\mathbf{1}R_s^{\mathsf T},\\
 R_s^{\mathsf T}
  &=\sum_{j=0}^{s-1}\lambda^{s-1-j}c_j^{\mathsf T}P^j,
 \qquad
 R_s^{\mathsf T}\mathbf{1}=\lambda^s-1.
 \end{aligned}
 \label{eq:prefix-rank-one}$$ Since $P^\ell=I$, the one-period monodromy is $$M_{\mathsf{w}}=Q_\ell
   =I+\mathbf{1}R_\ell^{\mathsf T}.
 \label{eq:monodromy}$$ Its characteristic polynomial and nonnegative powers are $$\chi_{M_{\mathsf{w}}}(z)
   =(z-1)^{r-1}(z-\lambda^\ell),
 \qquad
 M_{\mathsf{w}}^k=I+
 \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 \mathbf{1}R_\ell^{\mathsf T}
 \quad(k\geq0).
 \label{eq:monodromy-spectrum}$$ For $0\leq s<\ell$ and $k\geq0$, the phase-prefix orbit satisfies $$Q_sM_{\mathsf{w}}^ku_0=P^su_0+
 \left[
  R_s^{\mathsf T}u_0+
  \lambda^s\frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
  R_\ell^{\mathsf T}u_0
 \right]\mathbf{1}.
 \label{eq:phase-prefix}$$

The prefix formula is proved by induction. It is immediate for $s=0$ with $R_0=0$. Assuming the formula at $s$, multiply on the left by $C_s=P+\mathbf{1}c_s^{\mathsf T}$. The pure permutation terms give $P^{s+1}$. Because $P\mathbf{1}=\mathbf{1}$, the previous rank-one row survives; because $c_s^{\mathsf T}\mathbf{1}=\lambda-1$, its coefficient combines with that survival to give $\lambda R_s^{\mathsf T}$. The new digit contributes $c_s^{\mathsf T}P^s$. Thus $R_{s+1}^{\mathsf T}=c_s^{\mathsf T}P^s+\lambda R_s^{\mathsf T}$, whose iteration is the sum in [\[eq:prefix-rank-one\]](#eq:prefix-rank-one){reference-type="eqref" reference="eq:prefix-rank-one"}. Pairing that recurrence with $\mathbf{1}$ and using $c_s^{\mathsf T}P^s\mathbf{1}=\lambda-1$ yields $R_s^{\mathsf T}\mathbf{1}=\lambda^s-1$.

At $s=\ell$, the permutation part is the identity, which proves [\[eq:monodromy\]](#eq:monodromy){reference-type="eqref" reference="eq:monodromy"}. The rank-one update maps $\mathbf{1}$ to $\lambda^\ell\mathbf{1}$ and fixes every vector in $\ker R_\ell^{\mathsf T}$. Since $R_\ell^{\mathsf T}\mathbf{1}=\lambda^\ell-1\neq0$, that kernel has codimension one. The characteristic polynomial in [\[eq:monodromy-spectrum\]](#eq:monodromy-spectrum){reference-type="eqref" reference="eq:monodromy-spectrum"} follows. For powers, multiplication of $\mathbf{1}R_\ell^{\mathsf T}$ by itself contributes the scalar $\lambda^\ell-1$, so a geometric sum gives the displayed expression for all $k\geq0$, including $k=0$.

Finally, $Q_s\mathbf{1}=\lambda^s\mathbf{1}$. Apply the power formula to $u_0$, then the prefix formula, and collect the two diagonal terms. The residual term is $P^su_0$, and the scalar coefficient is exactly the bracket in [\[eq:phase-prefix\]](#eq:phase-prefix){reference-type="eqref" reference="eq:phase-prefix"}. This calculation retains every rotation and every power of $\lambda$.

The eigenvalue calculation is an exact finite-product identity. We attach no asymptotic spectral estimate, inverse reciprocity, algebraic-entropy identity, or integrability conclusion to it. Its role is to make the ordered period product explicit and to expose the digit row used next.

## Digit bounds and pair injectivity

The base-$\lambda$ argument requires two facts: every coordinate is a strict digit, and different support pairs have different digit vectors. Both facts follow from the incidence arithmetic rather than from the manual fixture.

[\[lem:digit-code\]]{#lem:digit-code label="lem:digit-code"} For every used pair $(a,b)$ and every coordinate $i\in I$, $$0<(c_{a,b})_i<\lambda.
 \label{eq:digit-bounds}$$ Moreover, $$(a,b)\longmapsto c_{a,b}
 \quad\text{is injective on the map-specific support dictionary.}
 \label{eq:pair-injectivity}$$

Every coordinate of $\alpha_a$ and $\beta_b$ lies between $\rho$ and $\rho+K\ell$. The common-total formula gives $D-1-(\rho+K\ell)=\rho\ell-1>0$. Hence $(D-1)(\alpha_a)_i-(\beta_b)_i$ is already positive if the first factor is bounded below by $D-1$ and the second coordinate is bounded above by $\rho+K\ell$. This proves the lower inequality. The same identity shows $(\alpha_a)_i<D-1$; since $(\beta_b)_i>0$, it follows that $(c_{a,b})_i<(D-1)^2=\lambda$. Both inequalities are strict and uniform.

Suppose $c_{a,b}=c_{a',b'}$. Rearranging gives $(D-1)(\alpha_a-\alpha_{a'})=\beta_b-\beta_{b'}$. If $a\neq a'$, choose a moving coordinate in the symmetric difference of the nonempty disjoint occurrence sets $S_a,S_{a'}$. At that coordinate the left side has magnitude $K(D-1)$, while a coordinate difference of two W exponents has magnitude at most $K$. Since $D-1>1$, equality is impossible. Thus $a=a'$. The displayed vector equality then forces $\beta_b=\beta_{b'}$. Distinct used W labels have distinct nonempty occurrence sets, and their moving-coordinate complement encodings differ, so $b=b'$. This proves injectivity.

For Example [\[ex:ell-three-fixture\]](#ex:ell-three-fixture){reference-type="ref" reference="ex:ell-three-fixture"}, the selected digit vectors are

$c_{A,X}=(28,18,27,26),\quad c_{B,X}=(18,28,17,36),\quad
c_{A,Y}=(27,17,28,27).$

They lie strictly between zero and $100$, illustrating the interval and the pair distinction. Their calculation is a notation check; the uniform inequalities and injectivity in Lemma [\[lem:digit-code\]](#lem:digit-code){reference-type="ref" reference="lem:digit-code"} do not depend on this finite instance.

## Three-level decoder

The row in the period product is an ordered base expansion: $$R_\ell^{\mathsf T}
  =\sum_{j=0}^{\ell-1}
    \lambda^{\ell-1-j}c_j^{\mathsf T}P^j.
 \label{eq:decoder-expansion}$$ Every row of $M_{\mathsf{w}}-I=\mathbf{1}R_\ell^{\mathsf T}$ equals $R_\ell^{\mathsf T}$. Lemma [\[lem:digit-code\]](#lem:digit-code){reference-type="ref" reference="lem:digit-code"} makes each coordinate in every rotated vector a base-$\lambda$ digit strictly between zero and the base. Therefore no coordinate carry occurs in [\[eq:decoder-expansion\]](#eq:decoder-expansion){reference-type="eqref" reference="eq:decoder-expansion"}.

[\[thm:decoder\]]{#thm:decoder label="thm:decoder"} Given $M_{\mathsf{w}},P,\lambda,\ell$, and a marked phase zero, the period product recovers the rooted ordered digit-vector word $(c_0,\ldots,c_{\ell-1})$. Adding the unlabelled map-specific support dictionary recovers the rooted ordered exponent-support pairs. Adding the labelled dictionary recovers the literal rooted label-pair word.

Read $R_\ell^{\mathsf T}$ from any row of $M_{\mathsf{w}}-I$. In each coordinate, uniqueness of the length-$\ell$ base-$\lambda$ expansion recovers, from most significant to least significant, the corresponding coordinates of $c_j^{\mathsf T}P^j$. Combining coordinates recovers each rotated vector in order. The permutation is known, so right multiplication by $P^{-j}$ removes the phase rotation and gives $c_j^{\mathsf T}$. The marked phase specifies which recovered digit is $j=0$.

At vector level this is all the monodromy itself supplies. Given the unlabelled support dictionary, the injectivity in [\[eq:pair-injectivity\]](#eq:pair-injectivity){reference-type="eqref" reference="eq:pair-injectivity"} matches every recovered digit to one exponent pair. If the dictionary also attaches the literal V and W labels to those supports, the same matches recover $(a_j,b_j)$ at every phase.

::: {#tab:decoder}
  Available data                                          Exact recoverable object
  ------------------------------------------------------- -------------------------------------------------------------
  $M_{\mathsf{w}},P,\lambda,\ell$, marked phase zero      Rooted ordered digit-vector word $(c_0,\ldots,c_{\ell-1})$.
  Preceding data plus the unlabelled support dictionary   Rooted ordered exponent-support pairs.
  Preceding data plus the labelled support dictionary     Literal rooted label-pair word.

  : Exact side-information ladder for monodromy decoding.
:::

Without literal names, the last line of Table [3](#tab:decoder){reference-type="ref" reference="tab:decoder"} weakens to labels up to independent bijective renaming of the V and W alphabets. Without marked phase zero, there is no intrinsic choice of a first phase, so only the cyclic rotation class is intrinsic. These are information losses, not failures of the base-expansion calculation.

## Missing-data boundary

[\[rem:decoder-boundary\]]{#rem:decoder-boundary label="rem:decoder-boundary"} The matrix $M_{\mathsf{w}}$ alone does not manufacture a support dictionary. An unmarked period product has no intrinsic phase-zero label, and the scalar forcing $\mu$ is identical for many different words. Consequently the construction supplies neither an unqualified literal-label decoder nor a scalar word decoder.

Even with a dictionary, literal names are external annotations of support vectors; permuting those names independently on the two sides does not alter the polynomial exponents. Likewise, moving the marked root cyclically changes the rooted presentation of the product. We do not assert that distinct rooted words must have unequal unmarked monodromy matrices. The positive claim is exactly the marked, side-informed ladder of Theorem [\[thm:decoder\]](#thm:decoder){reference-type="ref" reference="thm:decoder"}.

# Least periods, scalar boundaries, and counterexamples

## Two least periods

The selector period and the residual-geometry period agree numerically in the incidence construction, but for different reasons. The former is a property of the prescribed pair word. The latter is a property of the spike under the moving permutation after diagonal translation has been factored out.

[\[thm:least-periods\]]{#thm:least-periods label="thm:least-periods"} For the incidence realization, the strict selector word has least period $\ell$. Separately, the orbit of the position weights in $\mathbb R^r/\mathbb R\mathbf{1}$ has least period $\ell$.

The infinite selector itinerary repeats the input pair word. Because that rooted word is primitive, no positive shift smaller than $\ell$ fixes it; therefore its least selector period is $\ell$.

For the quotient statement, Lemma [\[lem:scalar-forcing\]](#lem:scalar-forcing){reference-type="ref" reference="lem:scalar-forcing"} gives $[u_n]=[P^nu_0]$. If a shift $d$ with $0<d<\ell$ fixed this quotient class, some scalar $c$ would satisfy $$P^du_0-u_0=c\mathbf{1},
 \qquad
 (P^du_0-u_0)_\star=0=c.
 \label{eq:quotient-obstruction}$$ The fixed star coordinate forces the diagonal displacement to vanish. But $P^d$ moves the unique height-$H$ spike from coordinate zero to a different moving coordinate, so $P^du_0\neq u_0$. This contradiction rules out every smaller positive quotient period. Since $P^\ell=I$, the least quotient period is exactly $\ell$.

If the pair word is nonprimitive, an $\ell$-step product can still be written, but its least selector period is a proper divisor. If the residual permutation or seed has a shorter quotient orbit, the quotient period can also shorten. These are distinct failure mechanisms, which is why the two clauses of Theorem [\[thm:least-periods\]](#thm:least-periods){reference-type="ref" reference="thm:least-periods"} are not merged. Neither clause asserts periodicity of the polynomial state: by [\[eq:t-closed\]](#eq:t-closed){reference-type="eqref" reference="eq:t-closed"}, $t_n$ grows strictly because $\lambda>1$ and $\mu>0$.

## Position maximum

Degree recurrences for monomial mappings provide useful context, with the original precise degree-growth analysis and its corrigendum cited together [@HasselblattPropp2007; @HasselblattProppCorrigendum2007; @BedfordKim2008]. The relations here are instead direct consequences of the incidence decomposition and are asserted only as annihilators.

[\[prop:recurrences\]]{#prop:recurrences label="prop:recurrences"} For the incidence realization, the position maximum, every moving or star position coordinate, every phase subsequence, and the complete-state maximum obey the formulas and index domains in [\[eq:q-order-two\]](#eq:q-order-two){reference-type="eqref" reference="eq:q-order-two"}--[\[eq:d-annihilator\]](#eq:d-annihilator){reference-type="eqref" reference="eq:d-annihilator"}. The complete-state formula begins at $n=1$, and its removed initial equation holds exactly under the condition in [\[eq:initial-residual\]](#eq:initial-residual){reference-type="eqref" reference="eq:initial-residual"}. None of these annihilators is claimed minimal.

The unique spike remains the maximum of $P^nu_0$, so $q_n:=\max_i(u_n)_i=H+t_n$. Substitution of the scalar recurrence in [\[eq:scalar-forcing\]](#eq:scalar-forcing){reference-type="eqref" reference="eq:scalar-forcing"} gives the order-two relation $$q_{n+2}-(1+\lambda)q_{n+1}+\lambda q_n=0,
 \qquad n\geq0.
 \label{eq:q-order-two}$$ The same sequence also obeys the period-spaced annihilator $$q_{n+\ell+1}-\lambda q_{n+\ell}-q_{n+1}+\lambda q_n=0,
 \qquad n\geq0.
 \label{eq:q-length-ell}$$

The closed form [\[eq:t-closed\]](#eq:t-closed){reference-type="eqref" reference="eq:t-closed"} is a constant plus a scalar multiple of $\lambda^n$. Hence the shift polynomial $(E-1)(E-\lambda)$ annihilates $q_n$, which is [\[eq:q-order-two\]](#eq:q-order-two){reference-type="eqref" reference="eq:q-order-two"}. Applying $(E^\ell-1)(E-\lambda)$ and expanding gives [\[eq:q-length-ell\]](#eq:q-length-ell){reference-type="eqref" reference="eq:q-length-ell"}. Both substitutions are valid starting at $n=0$. This argument establishes annihilation only; it does not assert that either displayed polynomial is minimal.

The scalar curve is intentionally independent of the current support label. Different words can therefore share it, reinforcing that neither [\[eq:q-order-two\]](#eq:q-order-two){reference-type="eqref" reference="eq:q-order-two"} nor [\[eq:q-length-ell\]](#eq:q-length-ell){reference-type="eqref" reference="eq:q-length-ell"} is a word decoder.

## Moving, star, and phase subsequences

For a moving coordinate, the spike appears exactly in its congruence class. The fixed coordinate never receives the spike and must be written separately: $$\begin{aligned}
 y_n^{(i)}&=1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n,
 \qquad i\in I_{\mathrm{mov}},
 \label{eq:moving-coordinate}\\
 y_n^{(\star)}&=1+t_n.
 \label{eq:star-coordinate}\end{aligned}$$ There is no congruence expression involving $\star$. For every $i\in I$, the periodic part and the affine scalar part are jointly annihilated by $$y_{n+\ell+1}^{(i)}-\lambda y_{n+\ell}^{(i)}
 -y_{n+1}^{(i)}+\lambda y_n^{(i)}=0,
 \qquad i\in I,\quad n\geq0.
 \label{eq:y-annihilator}$$

For a fixed phase $s\in I_{\mathrm{mov}}$, sample every $\ell$-th term. With $$\begin{aligned}
 z_m^{(i,s)}&=y_{s+m\ell}^{(i)},
 \qquad i\in I,\quad s\in I_{\mathrm{mov}},
 \label{eq:phase-subsequence}\\
 z_{m+2}^{(i,s)}-(1+\lambda^\ell)z_{m+1}^{(i,s)}
  +\lambda^\ell z_m^{(i,s)}&=0,
 \qquad m\geq0,
 \label{eq:z-annihilator}\end{aligned}$$ each phase subsequence has an order-two annihilator with base $\lambda^\ell$.

Equation [\[eq:moving-coordinate\]](#eq:moving-coordinate){reference-type="eqref" reference="eq:moving-coordinate"} follows from $u_n=P^nu_0+t_n\mathbf{1}$: the permutation places the excess $H-1$ in moving coordinate $n\bmod\ell$. Since $P$ fixes the star, [\[eq:star-coordinate\]](#eq:star-coordinate){reference-type="eqref" reference="eq:star-coordinate"} follows without a congruence. Shifting either formula by $\ell$ leaves its constant and periodic part unchanged, while the $\lambda^n$ part of $t_n$ scales by $\lambda^\ell$. Expansion of the resulting shift factors gives [\[eq:y-annihilator\]](#eq:y-annihilator){reference-type="eqref" reference="eq:y-annihilator"} from $n=0$.

Along a phase subsequence, the periodic indicator is constant and the geometric part is proportional to $(\lambda^\ell)^m$. The polynomial $(E-1)(E-\lambda^\ell)$ therefore gives [\[eq:z-annihilator\]](#eq:z-annihilator){reference-type="eqref" reference="eq:z-annihilator"} for $m\geq0$. Again, this proves an annihilator, not its minimality.

## Complete-state start index and residual

The complete-state maximum also includes the momentum weights. Define $$d_n=\max\{\max_i(u_n)_i,\max_i(m_n)_i\},
 \qquad d_n=q_n\quad\text{for }n\geq1.
 \label{eq:complete-maximum}$$ The second statement follows from the strict carry conclusion $u_n>m_n$ only after the first full step. Consequently, $$d_{n+\ell+1}-\lambda d_{n+\ell}-d_{n+1}+\lambda d_n=0,
 \qquad n\geq1.
 \label{eq:d-annihilator}$$ At the excluded initial index the exact residual and its vanishing condition are $$\begin{aligned}
 d_{\ell+1}-\lambda d_\ell-d_1+\lambda d_0
   &=\lambda(d_0-q_0),\\
 d_0=q_0
   &\Longleftrightarrow
   \max_i(m_0)_i\leq\max_i(u_0)_i.
 \end{aligned}
 \label{eq:initial-residual}$$

For every $n\geq1$, Theorem [\[thm:carry-lift\]](#thm:carry-lift){reference-type="ref" reference="thm:carry-lift"} gives $u_n>m_n$ coordinatewise, so the maximum over the complete state equals $q_n$. Substituting this equality in [\[eq:q-length-ell\]](#eq:q-length-ell){reference-type="eqref" reference="eq:q-length-ell"} proves [\[eq:d-annihilator\]](#eq:d-annihilator){reference-type="eqref" reference="eq:d-annihilator"} for $n\geq1$. At $n=0$, the three later terms already equal their q counterparts, while the last term is $\lambda d_0$ instead of $\lambda q_0$. Their difference is the first line of [\[eq:initial-residual\]](#eq:initial-residual){reference-type="eqref" reference="eq:initial-residual"}. The second line is simply the definition of the maximum at time zero. This completes the proof of all parts of Proposition [\[prop:recurrences\]](#prop:recurrences){reference-type="ref" reference="prop:recurrences"}.

[\[cex:initial-residual\]]{#cex:initial-residual label="cex:initial-residual"} Use $(\ell,r,\rho,K,H)=(3,4,2,1,2)$, $u_0=(2,1,1,1)$, and $m_0=(10,10,10,10)$. For the phase-zero exponent $\alpha_A=(3,2,3,3)$, one has $A_{\alpha_A}u_0=(12,13,13,13)$, so the strict first-carry gate still holds. Nevertheless $q_0=2$, $d_0=10$, $\lambda=100$, and the forbidden initial equation has residual $$d_4-100d_3-d_1+100d_0=100(10-2)=800.
 \label{eq:residual-800}$$ Thus admissibility for the actual weighted-degree lift does not imply the extra initial-maximum condition.

This hand calculation falsifies the unconditional $n=0$ extension; it does not support the general recurrence. The corrected domain is exactly $n\geq1$, with [\[eq:initial-residual\]](#eq:initial-residual){reference-type="eqref" reference="eq:initial-residual"} giving the necessary and sufficient condition for including the removed initial instance.

## Remaining structural boundaries and planar obstruction

The remaining boundaries can now be read beside the formulas they affect. Unequal support totals restore diagonal drift to the selector comparisons. The choice $H=1$ removes the spike and its incidence gap. A nonprimitive word shortens the selector period, while a residual permutation with a shorter orbit can shorten the quotient period. Removing a marked root or a dictionary weakens the decoder exactly as in Table [3](#tab:decoder){reference-type="ref" reference="tab:decoder"}. The scalar relations remain insensitive to the literal word and therefore do not identify it.

One elementary planar obstruction explains the use of a higher-dimensional finite-order residual twist. For a positive two-variable support and a pure-power second shear, let the support function be $H(r)=\max_{(a,b)}(ar+b)$. Only within this remark, $r$ denotes a projective coordinate and is unrelated to the ambient dimension. On a chamber with active exponent $(a,b)$, the induced map and its derivative have the form $$g(r)=\kappa\frac{(a-1)r+b}{ar+b-1},
 \qquad
 g'(r)=\kappa\frac{1-a-b}{(ar+b-1)^2}<0.
 \label{eq:planar-obstruction}$$ The chamber formulas join continuously at Newton walls, so the projective map is decreasing. Its square is increasing; an increasing interval map cannot possess a nontrivial periodic orbit, and hence the decreasing map has no orbit of least period greater than two.

[\[rem:planar-obstruction\]]{#rem:planar-obstruction label="rem:planar-obstruction"} The calculation in [\[eq:planar-obstruction\]](#eq:planar-obstruction){reference-type="eqref" reference="eq:planar-obstruction"} is explanatory only. It motivates the moving $\ell$-cycle plus fixed star used here, but it is not a priority statement, a classification of planar symplectic maps, or a theorem about all Newton-support dynamics.

Proposition [\[prop:symplectic-inverse\]](#prop:symplectic-inverse){reference-type="ref" reference="prop:symplectic-inverse"} proves the map and inverse clause. Theorem [\[thm:selector-fan\]](#thm:selector-fan){reference-type="ref" reference="thm:selector-fan"} and Corollary [\[cor:rational-seed\]](#cor:rational-seed){reference-type="ref" reference="cor:rational-seed"} prove the general selector equivalence and its rational-polyhedral properties, while Remark [\[rem:singleton\]](#rem:singleton){reference-type="ref" reference="rem:singleton"} fixes the singleton convention. Theorem [\[thm:incidence-realization\]](#thm:incidence-realization){reference-type="ref" reference="thm:incidence-realization"} supplies the autonomous every-word selectors, and Theorem [\[thm:carry-lift\]](#thm:carry-lift){reference-type="ref" reference="thm:carry-lift"} together with Proposition [\[prop:leading-survival\]](#prop:leading-survival){reference-type="ref" reference="prop:leading-survival"} upgrades them to actual polynomial weighted-degree transport for every permitted coefficient tuple and momentum seed. Theorem [\[thm:ordered-monodromy\]](#thm:ordered-monodromy){reference-type="ref" reference="thm:ordered-monodromy"}, Lemma [\[lem:digit-code\]](#lem:digit-code){reference-type="ref" reference="lem:digit-code"}, and Theorem [\[thm:decoder\]](#thm:decoder){reference-type="ref" reference="thm:decoder"} establish the ordered product and the three decoder levels. Finally, Theorem [\[thm:least-periods\]](#thm:least-periods){reference-type="ref" reference="thm:least-periods"} proves the two separate least periods, and Proposition [\[prop:recurrences\]](#prop:recurrences){reference-type="ref" reference="prop:recurrences"} proves every annihilator with its stated domain and initial residual. These results are exactly the eight clauses of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# Limitations and conclusion

## Scope and anti-claims

The construction gives one autonomous map for each rooted word and uses a dimension that grows with its length. It gives neither a universal map nor a fixed-dimensional realization for unbounded length. Its exact lift is for actual polynomial weighted degrees in the strict coordinatewise carry chamber; it is not an ordinary-total-degree realization or a free-standing exact-, algebraic-, or dynamical-degree theorem. Algebraic-entropy work provides context for this distinction [@BellonViallet1999; @HoneRagniscoZullo2016], but we prove no algebraic or topological entropy equality, integrability statement, generic nonconjugacy, inverse reciprocity, or cohomological spectrum. The scalar sequences neither separate nor decode words, and their displayed relations are not asserted minimal. Literal labels require a labelled support dictionary; a rooted output requires marked phase zero. The least-period statements do not make the polynomial state periodic. Finally, the proof does not extend to positive characteristic, zero support coordinates, zero displayed coefficients, or seeds outside the exact gate, and it does not classify cancellation after those hypotheses are removed.

The literature comparison is likewise bounded. Established weighted- degree, polynomial-automorphism, max-plus, monomial-map, cluster, and entropy mechanisms are not claimed as new individually. The dated conjunction statement in Section 1 records the scope of the comparison and does not certify exhaustive priority.

## Conjunctive contribution

Within those limits, the conclusions fit together tightly. The normal-fan theorem gives a necessary-and-sufficient strict-selector criterion on residual position weights. The incidence supports put every rooted primitive pair word inside such a cone using one fixed map. The strict carry chamber and domain argument then identify the formal selectors with actual polynomial weighted-degree transport uniformly over all nonzero coefficient tuples. The fixed star distinguishes diagonal displacement from a genuine quotient return, yielding a least-period statement separate from word primitivity. Finally, the ordered rank-one monodromy stores the rotated digit vectors without base carry, while the decoder ladder records exactly which support and labelling data must be supplied.

This combination, rather than any one familiar ingredient, is the content of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Every hypothesis that enforces the combination has a visible wall, counterexample, or information-loss boundary in the main body. In particular, selector feasibility is not conflated with leading- form survival, equality of two least periods is not conflated with equality of the underlying objects, and vector decoding is not promoted to scalar or unlabelled literal decoding.

## Proof-only evidence statement

Every result above is derived symbolically from the displayed supports, weighted-degree comparisons, strict carries, and ordered matrix products. The finite examples are hand-derived notation checks, counterexamples, or boundary illustrations. They do not serve as evidence for a universally quantified clause. The full mathematical argument, including the sharp failures and all decoder qualifications, is contained in the main text.
