---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--9-packet-separation"
canonical_tex: "flow_systems/papers/9-packet-separation/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/9-packet-separation/paper/paper.pdf"
source_sha256: "24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Indiscrete Prime Packets in Deninger's Rational-Witt Flow: Simultaneous Approximation and a Topological Corrigendum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/9-packet-separation>)
- [规范 TeX](<../../../../../flow_systems/papers/9-packet-separation/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/9-packet-separation/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/9-packet-separation/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/9-packet-separation/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Deninger's rational-Witt construction gives equivariant set coordinates for a prime packet, but those coordinates need not be homeomorphisms for the topology inherited from the suspension quotient. We fix a rational prime $p$, the genuine finite-kernel $E_f$ prepacket, and its exact restricted quotient topology. A constructive Chinese-remainder argument proves that $D_p=\mathbb{Z}[1/p]_{>0}$ is diagonally dense in $\mathbb{R}_{>0}\times\prod_{\ell\ne p}\mathbb{Z}_\ell$. For unit endpoints, the resulting character sequence has finite kernel and converges pointwise inside one fixed raw $E_f$ fibre, before passage through the Galois quotient and the initial colimit inclusion. These two facts imply universal specialization: for every ordered pair of packet points, the constant sequence at the first converges to the second. Consequently the packet, each inherited periodic orbit, and the orbit quotient are nontrivial indiscrete spaces; moreover, the restricted orbit relation is not closed. The analogous prime orbit with the inherited double-quotient topology in $\mathbb{Q}^\times\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb Z}^\times$ is likewise indiscrete, and the corrected Morishita comparison is an actual-to-actual homeomorphism between indiscrete spaces. This does not alter the intrinsically topologized Hausdorff circle in the Connes--Consani scaling site, nor an explicitly imposed standard-circle proxy. It instead withdraws the actual-topology ownership previously assigned to standard-circle calculations. We prove no general obstruction for non-Hausdorff groupoids, traces, or spectral constructions.

  **Keywords:** arithmetic dynamics; rational Witt vectors; suspension quotient; simultaneous approximation; indiscrete topology; nonclosed orbit relation; Deninger flow
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology (HUST)\
  <wangliang.f@gmail.com>
bibliography:
- references.bib
date: 14 August 2026
title: |
  **Indiscrete Prime Packets in Deninger's Rational-Witt Flow:\
  Simultaneous Approximation and a Topological Corrigendum**
```

## Markdown 正文

**中文摘要**

Deninger 的有理 Witt 动力系统为素数包给出了保持作用的集合坐标，但这些坐标一般不能自动成为关于悬挂商继承拓扑的同胚。本文固定一个有理素数 $p$、真实有限核 $E_f$ 预素数包及其严格的限制商拓扑。通过构造性的中国剩余定理逼近，我们证明 $D_p=\mathbb{Z}[1/p]_{>0}$ 在 $\mathbb{R}_{>0}\times\prod_{\ell\ne p}\mathbb{Z}_\ell$ 中对角稠密。对单位端点，由此得到的特征序列均具有有限核，并先在同一个原始 $E_f$ 纤维中逐点收敛，再合法地通过 Galois 商及初始余极限嵌入。两部分结合给出普遍特化定理：对素数包中任意有序点对，恒等于第一个点的常值序列都收敛到第二个点。因此，该素数包、其中每条继承周期轨道以及轨道商都是非平凡不可分拓扑空间，限制轨道关系也不是闭关系。带有双重商继承拓扑的朴素阿代尔素轨道同样不可分；修正后的 Morishita 对应是两个真实不可分空间之间的同胚。这一结论不改变 Connes--Consani scaling site 中由其自身定义的 Hausdorff 圆，也不改变显式赋予标准拓扑的圆代理；它只撤回此前将标准圆计算归属于真实继承拓扑的说法。本文不主张一般非 Hausdorff 群胚、Haar 系统、完备化、迹或谱构造不可能存在。

**中文关键词：** 算术动力系统；有理 Witt 向量；悬挂商；同时逼近；不可分拓扑；非闭轨道关系；Deninger 流

# Introduction

Periodic trajectories indexed by primes are a central organizing motif in arithmetic dynamics. Deninger's rational-Witt construction makes this motif unusually concrete: a finite-kernel subsystem carries a positive-real suspension flow, and the closed point $(p)\subset\operatorname{Spec}\mathbb{Z}$ determines a packet of trajectories with set-theoretic clock $\log p$ [@Deninger2026 Section 6 and Theorem 6.1, physical pp. 38--39]. The construction also supplies product-like coordinates involving away-from-$p$ units and the time circle. A coordinate bijection, however, does not determine the topology of its source. Deninger explicitly distinguishes continuous bijections from homeomorphisms in the relevant colimit and quotient analysis [@Deninger2026 Propositions 7.4 and 7.6--7.9, Theorem 7.10 and Remark 2, physical pp. 43--47]. The question addressed here is therefore elementary to state but consequential: what topology does the genuine fixed-prime packet inherit from the actual suspension quotient?

The answer is maximally nonseparated. Every point specializes to every other point. Equivalently, for arbitrary $x,y$ in the packet, the sequence that is constantly equal to $x$ converges to $y$. The proof is not an abstract appeal to a dense group action. It has two exact ingredients. First, positive rationals whose denominators are powers of $p$ approximate simultaneously a prescribed positive real number and an arbitrary element of the prime-to-$p$ profinite product. Second, when the profinite endpoints are units, this approximation induces pointwise convergence of finite-kernel characters within one fixed raw $E_f$ fibre. The second step is essential: a convergence statement in a larger character space would not by itself certify convergence inside the finite-kernel object used in the suspension.

The resulting topology changes the type of several familiar descriptions. The packet still has its set/action parametrization, and an inherited orbit still has stabilizer $p^{\mathbb{Z}}$ and set period $\log p$. Yet neither is a standard Hausdorff circle in its inherited topology. The time-orbit subspace is nontrivial and indiscrete, and the packet modulo time is the nontrivial indiscrete quotient $U_p/H_p$ as a set. The exact restricted orbit relation is not closed. Thus a standard locally compact Hausdorff transformation-groupoid construction cannot be attached to these actual unit spaces under its usual hypotheses. This is a failure of a named prerequisite, not a universal theorem against future non-Hausdorff groupoids or their analytic structures.

There is a parallel topological distinction on the adelic side. The prime orbit inside the double quotient $\mathbb{Q}^\times\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb Z}^\times$, when equipped with the topology inherited from that exact double quotient, is also nontrivial indiscrete. On the genuine $E_f$ domain, the character-to-adele comparison developed by Morishita can be repaired by retaining finite-kernel nonvanishing and unit normalization; it then identifies two actual indiscrete spaces [@Morishita2026 Eq. (1.1.5), physical p. 5; Remark 2.1.13, p. 13; Lemmas 3.4--3.5 and Theorem 3.6, pp. 23--25]. By contrast, the prime circle intrinsic to the Connes--Consani scaling site has its own source-defined Hausdorff topology [@ConnesConsani2016 Lemma 6.3(i), physical p. 5]. A canonical set comparison is not a license to transport topology from one owner to another.

This distinction also corrects the ownership assigned in the preceding project, Paper 8. The algebraic, Floquet, fixed-proxy normality, and character calculations carried out on an ordinary standard circle remain internally valid after explicit retyping to a standard-circle proxy. What is withdrawn is their attribution to an actual inherited Deninger orbit. The positive-time coefficient-one scalar ledger is independent of this topology and remains unchanged. Historical Paper 8 bytes are not rewritten; the versioned matrix in [7](#sec:corrigendum){reference-type="ref" reference="sec:corrigendum"} records exactly what is corrected and what survives.

## Results and claim boundary

The proof is organized around the following ledger. Each row names its exact topology owner so that a set model cannot silently become a topological product.

P0.12P0.25Y Target & Result & Boundary\
C-01--C-02 & The restricted quotient topology is exact, and $D_p$ is constructively dense in $\mathbb{R}_{>0}\times A_p$. & Density is proved with positive numerators and residues imposed on $q_j$, not only on its numerator.\
C-03--C-05 & Finite-kernel convergence, unit normalization, and the exact equivalence relation hold. & Raw characters, Galois orbits, and colimit points remain distinct.\
C-06--C-10 & Universal specialization, three indiscreteness results, and nonclosedness of $\mathcal R_p$. & No conclusion is drawn for the full global suspension.\
C-11--C-14 & Set coordinates, the naive adelic orbit, the repaired Morishita map, and the intrinsic scaling circle are separated by owner. & No topology is transported through a set bijection.\
C-15--C-18 & The standard LCH--Hausdorff actual branches fail at their unit-space prerequisite; Paper 8 computations survive on proxy owners. & No general non-Hausdorff no-go; the scalar ledger cannot be spliced into another owner.\
C-19--C-20 & Twenty finite controls pass; all eight Route objects remain exploratory. & Controls are not proofs; $A2,A3,A4$ all fail and Route B is not invoked.\

The literature search supporting the comparison and novelty statement was bounded at 14 August 2026. It covered the retained Deninger, Morishita, Connes--Consani, Le Bruyn, and Jüstel sources and exact metadata/full-text searches. Within that bounded search, we did not locate a source proving the universal-specialization theorem for the genuine rational-Witt $E_f$ packet or the exact inherited adelic prime orbit. This is a report of a documented search, not an absolute priority claim. The simultaneous-approximation tools, quotient topology, and elementary properties of indiscrete spaces are standard mathematics; novelty is asserted only for their exact conjunction on these named source objects.

No target zero, fitted parameter, determinant, analytic continuation, functional equation, quantization, or Hilbert--Pólya claim appears. We do not construct a principal bundle, transverse measure, Haar system, completion, or trace for the actual non-Hausdorff packet. We also do not infer a universal obstruction to such future constructions.

# The exact source object and restricted quotient topology {#sec:source}

## Objects and topology owners

Fix a rational prime $p$. Let $$A_p=\prod_{\ell\ne p}\mathbb{Z}_\ell,\qquad
 U_p=A_p^\times=\prod_{\ell\ne p}\mathbb{Z}_\ell^\times,
 \qquad H_p=p^{\widehat{\mathbb Z}}\subset U_p,
 \qquad D_p=\mathbb{Z}[1/p]_{>0}.$$ Here $H_p$ is the continuous image of $\widehat{\mathbb Z}$ under the prime-to-$p$ power map $n\mapsto p^n$. Let $$\check X=\check X_0(\mathbb{C})_{E_f}$$ be Deninger's finite-kernel rational-Witt pre-suspension space. Its source construction and Frobenius action are the ones surrounding equations (35), (38), and (39) in [@Deninger2026 physical pp. 32--33]. Put $$Y=\check X\times\mathbb{R}_{>0},
 \qquad (P,u)q=(F_qP,q^{-1}u),\quad q\in\mathbb{Q}_{>0},$$ and write $\rho:Y\to Y/\mathbb{Q}_{>0}$ for the orbit map.

The fixed-prime raw characters are denoted $\widetilde P_a$, their Galois-orbit points by $P_a$, and their images under the initial colimit inclusion by $j(P_a)$. These are three different levels. Let $C_p^{E_f}\subset\check X$ be the fixed-prime prepacket and set $$Z_p=C_p^{E_f}\times\mathbb{R}_{>0},\qquad
 \Gamma_p=\rho(Z_p).$$ The relation $\mathcal R_p\subset Z_p\times Z_p$ is the restriction of the $\mathbb{Q}_{>0}$-orbit relation: $$(z,z')\in\mathcal R_p\quad\Longleftrightarrow\quad
 z'=zq\ \text{for some }q\in\mathbb{Q}_{>0}.$$ We equip $\Gamma_p$ with the subspace topology inherited from $Y/\mathbb{Q}_{>0}$. This owner specification is part of the definition.

P0.23P0.35Y Object & Topology owner & Permitted use\
$Z_p$ & product subspace of $\check X\times\mathbb{R}_{>0}$ & restricted relation and convergent representatives\
$\Gamma_p$ & subspace of $Y/\mathbb{Q}_{>0}$, equivalently $Z_p/\mathcal R_p$ & actual packet theorem\
actual inherited orbit & subspace of $\Gamma_p$ & indiscrete orbit with set stabilizer $p^{\mathbb{Z}}$\
$Q_p=\Gamma_p/K_p$ & quotient topology, $K_p=\mathbb{R}_{>0}/p^{\mathbb{Z}}$ as set/action time quotient & nontrivial indiscrete set model $U_p/H_p$\
$C_p^{\mathrm{naive}}$ & prime-orbit subspace of $\mathbb{Q}^\times\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb Z}^\times$ & inherited double-quotient theorem\
intrinsic scaling $C_p$ & Connes--Consani source topology & ordinary Hausdorff circle only\
standard-circle proxy & topology imposed by the proxy definition & proxy algebra, Floquet, and trace formulas only\

## The restricted quotient is the inherited packet

[\[lem:open\]]{#lem:open label="lem:open"} The global orbit map $\rho:Y\to Y/\mathbb{Q}_{>0}$ is open. The subset $Z_p\subset Y$ is saturated. Consequently the restricted map $$\rho_p:Z_p\longrightarrow\Gamma_p$$ is open and quotient, and the canonical bijection $Z_p/\mathcal R_p\to\Gamma_p$ is a homeomorphism.

For an open subset $O\subset Y$, its saturation is $$\rho^{-1}(\rho(O))=\bigcup_{q\in\mathbb{Q}_{>0}}Oq.$$ Each right translation by $q$ is a homeomorphism: the inverse is right translation by $q^{-1}$. The displayed union is therefore open. By the definition of the quotient topology, $\rho(O)$ is open; hence $\rho$ is open.

The prime label is invariant under the rational Frobenius action defining the packet, so $C_p^{E_f}$, and hence $Z_p=C_p^{E_f}\times\mathbb{R}_{>0}$, is a union of full $\mathbb{Q}_{>0}$-orbits. Thus $Z_p=\rho^{-1}(\Gamma_p)$ is saturated. If $O\subset Z_p$ is open in the subspace topology, write $O=V\cap Z_p$ for $V\subset Y$ open. Saturation gives $$\rho_p(O)=\rho(V)\cap\Gamma_p,$$ which is open in the inherited subspace topology on $\Gamma_p$. Hence $\rho_p$ is an open continuous surjection and therefore a quotient map. Its fibres are exactly the classes of $\mathcal R_p$, so the induced bijection $Z_p/\mathcal R_p\to\Gamma_p$ is a homeomorphism.

This lemma prevents a frequent ambiguity. We do not declare a topology on a displayed coordinate set and then identify it with the packet. We first retain the actual global quotient, restrict to a saturated prepacket, and recover exactly the inherited topology. All later convergence arguments therefore take place in $Z_p$ before being pushed through the named quotient map.

The source's compactness language does not close a separation gate. Deninger's survey calls the prime packet and its orbit fibres compact in the open-cover sense, but does not add Hausdorffness, local triviality, or a product topology [@Deninger2024 Theorem 4.2, physical pp. 11--12]. Its Theorem 4.4 again supplies a continuous bijection and immediately warns that this bijection need not be a homeomorphism [@Deninger2024 Theorem 4.4 and following sentence, physical pp. 12--13]. The quotient topology in [\[lem:open\]](#lem:open){reference-type="ref" reference="lem:open"}, rather than compact-to-Hausdorff reasoning, therefore owns the argument below.

# Simultaneous approximation in the fixed-prime channel {#sec:crt}

The arithmetic engine of the proof is a diagonal density theorem with three constraints that must be satisfied together: the numerator is positive, the real approximation has the correct sign, and the congruence is imposed on the rational number $q_j=m_j/p^{k_j}$ in the prime-to-$p$ completion.

[\[thm:density\]]{#thm:density label="thm:density"} The diagonal image of $D_p=\mathbb{Z}[1/p]_{>0}$ is dense in $$\mathbb{R}_{>0}\times A_p.$$ More explicitly, for every $c\in\mathbb{R}_{>0}$ and $a\in A_p$, there is a sequence $q_j=m_j/p^{k_j}\in D_p$ such that $q_j\to c$ in $\mathbb{R}_{>0}$ and $q_j\to a$ in $A_p$.

Enumerate the primes different from $p$ as $\ell_1,\ell_2,\ldots$, and define the cofinal prime-to-$p$ moduli $$M_j=\prod_{i=1}^{j}\ell_i^j.$$ Let $a_j\in\mathbb{Z}/M_j\mathbb{Z}$ be the image of $a$ under the natural projection $A_p\to\mathbb{Z}/M_j\mathbb{Z}$. Since $p$ is invertible modulo $M_j$, choose $k_j\ge0$ large enough that $$\frac{M_j}{2p^{k_j}}<\frac1j,
 \qquad cp^{k_j}>M_j.$$ We impose the residue condition $$m_j\equiv a_jp^{k_j}\pmod{M_j}.$$ Among the integers in this residue class, choose $m_j$ nearest to $cp^{k_j}$. The second inequality ensures that a positive representative can be chosen, and nearest-point selection gives $$|m_j-cp^{k_j}|\le \frac{M_j}{2}.$$ For $q_j=m_j/p^{k_j}$, therefore, $$|q_j-c|\le\frac{M_j}{2p^{k_j}}<\frac1j.$$ Thus $q_j\to c$ in the real coordinate. Moreover $$q_j=m_jp^{-k_j}\equiv a_j\pmod{M_j},$$ where $p^{-k_j}$ is interpreted modulo $M_j$. For a fixed $\ell_i\ne p$ and exponent $r\ge1$, every sufficiently large $j$ has $i\le j$ and $j\ge r$, so $\ell_i^r\mid M_j$. It follows that $q_j\equiv a\pmod{\ell_i^r}$ eventually. Hence $q_j\to a$ in every $\mathbb{Z}_{\ell_i}$, which is convergence in the product $A_p$.

[\[rem:twist\]]{#rem:twist label="rem:twist"} Requiring merely $m_j\equiv a_j\pmod{M_j}$ would force the profinite residue of $q_j$ to be $a_jp^{-k_j}$, not $a_j$. The factor $p^{k_j}$ in the numerator congruence is therefore structural. Likewise, approximating $c$ by $-m_j/p^{k_j}$, or using $q_j^{-1}u$ with the wrong real target, reverses the suspension sign and misses the desired endpoint. The finite controls in [8](#sec:controls){reference-type="ref" reference="sec:controls"} include both negative cases, but the theorem rests on the symbolic CRT construction.

The moduli $M_j$ are not unique. Their only role is to be cofinal among prime-to-$p$ congruence moduli while allowing the denominator exponent to dominate the real mesh. The proof also shows why positivity is compatible with a prescribed residue: once $cp^{k_j}>M_j$, the nearest member of the residue class lies strictly above zero.

# Finite-kernel convergence and normalization {#sec:finite}

The density theorem takes place in $\mathbb{R}_{>0}\times A_p$. To use it in Deninger's packet, the profinite convergence must be lifted to the finite-kernel character space without changing fibre or confusing raw characters with their later quotients.

## Convergence inside one raw finite-kernel fibre

Let $G_p$ be the torsion residue group on which the fixed-prime raw characters are evaluated, and let $\chi$ be the reference character. For an admissible exponent $a$, write $\chi^a$ for the raw character and $\widetilde P_a$ for the corresponding raw point. Every $\zeta\in G_p$ has finite order prime to $p$. Evaluation on $\zeta$ therefore factors through a finite congruence quotient of $A_p$. This is the fixed-stage mechanism behind the next lemma; Deninger's equation (35) owns the finite-kernel parametrization, while equations (38)--(39) own the later Galois and balanced-product set descriptions [@Deninger2026 physical pp. 32--33, equations (35), (38), and (39)].

[\[lem:character\]]{#lem:character label="lem:character"} Let $b,d\in U_p$, and let $q_j\in D_p$ converge to $d$ in $A_p$. Then every raw character $\widetilde P_{bq_j}$ has finite kernel and $$\widetilde P_{bq_j}\longrightarrow\widetilde P_{bd}$$ pointwise inside the same raw $E_f$ fibre. The convergence passes continuously first to the Galois-orbit points $P_{bq_j}\to P_{bd}$, and then through the named initial colimit inclusion $j(P_{bq_j})\to j(P_{bd})$.

We first verify membership in $E_f$ for each approximant; $q_j$ need not be a unit of $A_p$. Write $$q_j=\frac{m_j}{p^{k_j}},\qquad m_j=p^{s_j}m'_j,\qquad (m'_j,p)=1.$$ Multiplication by $b$, $p^{s_j}$, and $p^{-k_j}$ are automorphisms of $G_p$. Multiplication by $m'_j$ has kernel equal to the finite group of $m'_j$-torsion elements. Hence the exponent endomorphism $bq_j$, and therefore $\chi^{bq_j}$, has finite kernel. Every $\widetilde P_{bq_j}$ belongs to the same initial fixed-$p$, finite-kernel raw fibre. Since $bd\in U_p$, the limit exponent is an automorphism and its character is also in $E_f$.

Now fix $\zeta\in G_p$ and put $N=\operatorname{ord}(\zeta)$. Because $p\nmid N$, convergence $q_j\to d$ in $A_p$ gives $$q_j\equiv d\pmod N$$ for all sufficiently large $j$. Multiplication by the fixed unit $b$ preserves this congruence, so $$\chi(\zeta)^{bq_j}=\chi(\zeta)^{bd}$$ eventually. This is pointwise convergence of the raw characters in one fixed fibre; no colimit stage varies, since rational powers of $p$ act as inverse Frobenius on the same residue group.

Only after establishing raw convergence do we apply the continuous Galois quotient and then Deninger's continuous open initial-stage inclusion into $\check X$, as supplied by Proposition 7.4 and the Section 7 $E_f$ extension [@Deninger2026 Proposition 7.4, physical p. 43; finite-kernel discussion, physical p. 47]. This gives $$P_{bq_j}\longrightarrow P_{bd},
 \qquad
 j(P_{bq_j})\longrightarrow j(P_{bd}),$$ and equivariance gives $j(P_{bq_j})=F_{q_j}j(P_b)$ at the source-action level.

The eventual equality above is an equality of raw character values at one $\zeta$. At the Galois and packet levels we assert convergence of images. Although $F_{m/p^k}(P_b)=F_m(P_b)$ is valid at the Galois/packet point because $p^{\mathbb{Z}}$ is the exact stabilizer, it is not used for convergence; the generally false raw identity $\chi^{bmp^{-k}}=\chi^{bm}$ is nowhere asserted. If a profinite target lies outside $U_p$, [\[thm:density\]](#thm:density){reference-type="ref" reference="thm:density"} still applies, but this lemma supplies no $E_f$ endpoint unless finite kernel is independently proved.

## Unit representatives and exact equivalence

The fixed-prime parametrization permits exponents in the prime-to-$p$ profinite product. For the convergence lemma we need unit exponents. The next two statements isolate the set-theoretic normalization and the remaining equivalence.

[\[lem:normalization\]]{#lem:normalization label="lem:normalization"} Every class of $\Gamma_p$ has a representative of the form $$[j(P_a),u],\qquad a\in U_p,\quad u\in\mathbb{R}_{>0}.$$

Deninger's equation (35) represents every finite-kernel character in the fixed fibre by an exponent $a\nu$, with $a\in U_p$ and $\nu\in\mathbb N$ [@Deninger2026 equation (35), physical p. 32]. Any power of $p$ in $\nu$ may be absorbed into the unit $a$, so $\nu$ may be taken prime to $p$. At the exact source-action level, $$P_{a\nu}=F_\nu(P_a),\qquad
 (j(P_a),\nu u)\nu=(j(P_{a\nu}),u).$$ Therefore $$[j(P_{a\nu}),u]=[j(P_a),\nu u].$$ Equations (38)--(39) and the suspension set bijection show that these normalized representatives exhaust $\Gamma_p$ [@Deninger2026 equations (38)--(39), physical p. 33]. This is a set/action normalization; it transports no topology through those bijections.

[\[lem:equiv\]]{#lem:equiv label="lem:equiv"} For $a,b\in U_p$ and $u,v\in\mathbb{R}_{>0}$, $$[j(P_a),u]=[j(P_b),v]$$ if and only if $$ba^{-1}\in H_p=p^{\widehat{\mathbb Z}}
 \qquad\text{and}\qquad
 u/v\in p^{\mathbb{Z}},$$ with the two conditions coupled by the same rational orbit relation. Consequently $$\Gamma_p\ \cong_{\mathrm{set}}\ (U_p/H_p)\times(\mathbb{R}_{>0}/p^{\mathbb{Z}}),$$ but this display is only a set/action model and is not a product-homeomorphism theorem.

Equality of suspension classes means that for some exact $q\in\mathbb{Q}_{>0}$, $$F_qj(P_a)=j(P_b),\qquad q^{-1}u=v.$$ The second equality gives $q=u/v$. Because both endpoint characters are injective, the image of $q$ in every $\mathbb{Z}_\ell$, $\ell\ne p$, must be a unit. A positive rational with zero valuation at every $\ell\ne p$ is $p^n$ for some $n\in\mathbb{Z}$. Hence $u/v=q\in p^{\mathbb{Z}}$. At the raw level the rational Frobenius action gives the exponent relation; after the Galois quotient, the remaining ambiguity is exactly $H_p=p^{\widehat{\mathbb Z}}$, so $ba^{-1}\in H_p$.

Equivalently, this is precisely the class relation in Deninger's $\mathbb{Q}_{>0}$-equivariant balanced-product bijection (38), rewritten as (39) [@Deninger2026 equations (38)--(39), physical p. 33]. That colimit-level set theorem is the decisive check; it does not identify raw characters. Conversely, the same Galois identification together with the exact $p^{\mathbb{Z}}$ time stabilizer produces the required rational orbit relation, so the two displayed conditions are sufficient.

Choosing cosets yields the displayed bijection of sets. No step equips $U_p/H_p$ or $\mathbb{R}_{>0}/p^{\mathbb{Z}}$ with a topology and no step proves that a coordinate bijection is open. The actual topology remains the one fixed by [\[lem:open\]](#lem:open){reference-type="ref" reference="lem:open"}.

# Indiscrete packets and nonclosed relations {#sec:main}

We now combine simultaneous approximation with fixed-stage convergence. The orientation of the real target follows from the right action $(P,u)q=(F_qP,q^{-1}u)$: to move $u$ toward $v$, one must take $q\to u/v$.

[\[thm:universal\]]{#thm:universal label="thm:universal"} For every ordered pair $x,y\in\Gamma_p$, the constant sequence with value $x$ converges to $y$ in the actual inherited topology of $\Gamma_p$.

By [\[lem:normalization\]](#lem:normalization){reference-type="ref" reference="lem:normalization"}, choose representatives $$x=\rho_p(j(P_b),u),\qquad
 y=\rho_p(j(P_a),v),
 \qquad a,b\in U_p,\quad u,v>0.$$ Apply [\[thm:density\]](#thm:density){reference-type="ref" reference="thm:density"} with the real target $c=u/v$ and the profinite target $d=ab^{-1}\in U_p$. It gives $q_j\in D_p$ such that $$q_j\longrightarrow u/v\quad\text{in }\mathbb{R}_{>0},
 \qquad q_j\longrightarrow ab^{-1}\quad\text{in }A_p.$$ Define $$z_j=(j(P_b),u)q_j
     =(F_{q_j}j(P_b),q_j^{-1}u)\in Z_p.$$ By [\[lem:character\]](#lem:character){reference-type="ref" reference="lem:character"}, the first coordinate converges to $j(P_a)$; by the real convergence, $q_j^{-1}u\to v$. Hence $$z_j\longrightarrow (j(P_a),v)$$ in the product subspace $Z_p$. On the other hand, every $z_j$ lies in the same rational orbit as $(j(P_b),u)$, so $$\rho_p(z_j)=x\qquad\text{for all }j.$$ Continuity of $\rho_p$ now gives $x,x,\ldots\to y$. Since the ordered pair $x,y$ was arbitrary, the assertion follows.

The proof is sequential but its conclusion determines the entire topology, not merely its sequentialization. Indeed, if $O\subset\Gamma_p$ is nonempty and open, choose $y\in O$. For arbitrary $x\in\Gamma_p$, the constant sequence at $x$ converges to $y$; eventual membership in $O$ forces $x\in O$. Thus $O=\Gamma_p$.

[\[cor:packet\]]{#cor:packet label="cor:packet"} The inherited packet $\Gamma_p$ is an indiscrete space. It has at least two points and is therefore not $T_0$, not $T_1$, and not Hausdorff.

The preceding open-set argument proves indiscreteness. To prove nontriviality independently, take normalized representatives with the same unit exponent but time ratio $u/v\notin p^{\mathbb{Z}}$. Such positive reals exist because $p^{\mathbb{Z}}$ is a proper discrete subset of $\mathbb{R}_{>0}$. By [\[lem:equiv\]](#lem:equiv){reference-type="ref" reference="lem:equiv"}, the representatives determine distinct packet points. A nontrivial indiscrete space fails all three stated separation axioms.

## Inherited periodic orbits and the time quotient

The word "periodic" describes the action and stabilizer as a set. It does not force the orbit's inherited topology to be the standard topology of a circle.

[\[cor:orbit\]]{#cor:orbit label="cor:orbit"} Every actual $\mathbb{R}_{>0}$-orbit in $\Gamma_p$, equipped with the subspace topology, is a nontrivial indiscrete space. Its set stabilizer is $p^{\mathbb{Z}}$, and hence its set-theoretic primitive logarithmic period is $\log p$.

Fix an exponent class and choose any two points of its time orbit, represented by $[j(P_a),u]$ and $[j(P_a),v]$. In [\[thm:universal\]](#thm:universal){reference-type="ref" reference="thm:universal"}, the profinite target is then $1\in U_p$; the same construction yields constant-class convergence between arbitrary ordered points while staying in the orbit subset. Thus the subspace is indiscrete. It is nontrivial because choosing $u/v\notin p^{\mathbb{Z}}$ gives distinct points by [\[lem:equiv\]](#lem:equiv){reference-type="ref" reference="lem:equiv"}. The stabilizer and clock are the source set/action data of Deninger's fixed-prime suspension [@Deninger2026 Theorem 6.1, physical pp. 38--39].

Let $K_p=\mathbb{R}_{>0}/p^{\mathbb{Z}}$ denote the time-quotient group at the level of sets and actions, and define $$Q_p=\Gamma_p/K_p$$ with the quotient topology. By normalized equivalence, $Q_p\cong_{\mathrm{set}}U_p/H_p$.

[\[cor:Qp\]]{#cor:Qp label="cor:Qp"} The quotient $Q_p$ is a nontrivial indiscrete space. Set-theoretically it is $U_p/H_p$, but this does not identify it with a pre-existing standard topological group $B_p$.

Every quotient of an indiscrete space is indiscrete: the inverse image of a nonempty open subset is nonempty and open, hence the whole source. It remains to show that the quotient is not a singleton. The procyclic group $H_p=p^{\widehat{\mathbb Z}}$ has at most one element of order two. In $U_p=\prod_{\ell\ne p}\mathbb{Z}_\ell^\times$, choose two odd prime coordinates different from $p$. Independent sign choices in those coordinates give at least three distinct nonidentity elements of order two. At least one lies outside $H_p$, so $U_p/H_p$ has more than one element. The set identification follows from [\[lem:equiv\]](#lem:equiv){reference-type="ref" reference="lem:equiv"}. Since no independent topology on the symbol $B_p$ has been specified or compared, no topological promotion is made.

## The restricted relation is not closed

For a Hausdorff quotient one ordinarily expects a closed equivalence relation under suitable compactness hypotheses. Here the failure can be seen directly at the prequotient level.

[\[thm:nonclosed\]]{#thm:nonclosed label="thm:nonclosed"} The relation $\mathcal R_p\subset Z_p\times Z_p$ is not closed.

Choose $b\in U_p$ and $u,v>0$ with $u/v\notin p^{\mathbb{Z}}$. Set $$w=(j(P_b),u),\qquad w'=(j(P_b),v).$$ By [\[thm:density\]](#thm:density){reference-type="ref" reference="thm:density"}, choose $q_j\in D_p$ such that $q_j\to u/v$ in $\mathbb{R}_{>0}$ and $q_j\to1$ in $A_p$. Then [\[lem:character\]](#lem:character){reference-type="ref" reference="lem:character"} gives $$wq_j=(F_{q_j}j(P_b),q_j^{-1}u)\longrightarrow(j(P_b),v)=w'.$$ Every pair $(w,wq_j)$ belongs to $\mathcal R_p$, and $$(w,wq_j)\longrightarrow(w,w')$$ in $Z_p\times Z_p$. But $(w,w')\notin\mathcal R_p$, because normalized equivalence would require $u/v\in p^{\mathbb{Z}}$. Hence $\mathcal R_p$ is not closed.

P0.27P0.18P0.18Y Owner & Nontrivial & Topology & Consequence\
$\Gamma_p$ inherited packet & yes & indiscrete & non-$T_0$, non-$T_1$, non-Hausdorff\
inherited time orbit & yes & indiscrete & set period $\log p$ does not supply circle topology\
$Q_p=\Gamma_p/K_p$ & yes & indiscrete & $U_p/H_p$ is a set model only\
$\mathcal R_p\subset Z_p^2$ & --- & nonclosed & standard closed-relation quotient arguments are unavailable\

None of these statements concerns every orbit in the full global suspension. The proof is fixed-prime and finite-kernel: it uses both the $A_p$ approximation and the $E_f$ character convergence. The global topology is outside the theorem.

# Adelic comparison and topology ownership {#sec:adelic}

The source literature presents closely related circle-shaped sets in several categories. This section separates four owners: Deninger's actual inherited orbit, a naive inherited adelic orbit, the intrinsic scaling-site circle, and an explicitly retopologized standard-circle proxy.

## The naive inherited adelic prime orbit

Consider the double quotient $$\mathbb{Q}^\times\backslash\mathbb{A}_{\mathbb{Q}}/\widehat{\mathbb Z}^\times$$ with its quotient topology from the adele ring. For $r>0$, let $e_p(r)\in\mathbb{A}_{\mathbb{Q}}$ have $p$-component $0$, every finite component away from $p$ equal to $1$, and infinite component $r$. Let $C_p^{\mathrm{naive}}$ be the subspace consisting of the double-quotient classes of the $e_p(r)$. This is a deliberately literal definition: the adjective "naive" marks the inherited double-quotient owner and prevents confusion with the intrinsically topologized scaling-site point.

[\[thm:adelic\]]{#thm:adelic label="thm:adelic"} The space $C_p^{\mathrm{naive}}$ is nontrivial indiscrete. Its equality relation on the displayed representatives is $$[e_p(r)]=[e_p(s)]\quad\Longleftrightarrow\quad s/r\in p^{\mathbb{Z}}.$$

Fix $r,s>0$. Apply [\[thm:density\]](#thm:density){reference-type="ref" reference="thm:density"} to the real target $s/r$ and any prescribed unit target in $A_p$; for the displayed normalization it is convenient to use $1$. Thus choose $q_j\in D_p$ with $q_j\to s/r$ in $\mathbb{R}_{>0}$ and $q_j\to1$ away from $p$. Multiplication by $q_j$ leaves every $q_je_p(r)$ in the same left $\mathbb{Q}^\times$-class as $e_p(r)$. In the adele ring it converges to an adele $\alpha$ whose $p$-component is zero, whose infinite component is $s$, and whose away-from-$p$ components are units. Right multiplication by an element of $\widehat{\mathbb Z}^\times$ normalizes those away components to $1$ without changing the zero $p$-component. Hence the double-quotient image of the sequence is constantly $[e_p(r)]$ and converges to $[e_p(s)]$. The same open-set argument as after [\[thm:universal\]](#thm:universal){reference-type="ref" reference="thm:universal"} proves indiscreteness.

For equality, a rational scaling that preserves a zero $p$-component and can be canceled by an integral unit at every other finite place has valuation only at $p$. It is therefore a power of $p$, and its positive infinite component gives $s/r\in p^{\mathbb{Z}}$. Conversely a power of $p$ gives the equality. Choosing $s/r\notin p^{\mathbb{Z}}$ proves nontriviality.

The same phenomenon is visible in arithmetic-site topology warnings. Le Bruyn's published correction retracts an earlier overstrong trivial-topology statement and stresses the need to track the exact topology owner [@LeBruyn2016 Theorem 1, printed p. 2/physical p. 3; correction acknowledgement, printed p. 9/physical p. 10]. We do not use that source as a proof of [\[thm:adelic\]](#thm:adelic){reference-type="ref" reference="thm:adelic"}; the theorem above is an explicit argument for the exact adelic subspace named here.

## Repairing the actual-to-actual Morishita comparison

Morishita constructs a relation between Deninger's character side and Connes--Consani adelic spaces and records flow anti-equivariance [@Morishita2026 Eq. (2.2.7) and surrounding theorems, physical pp. 14--17]. Two domain details matter for the present fixed-prime result. First, Remark 2.1.13 notes a character refinement that is not part of a coarser printed identification. Second, at the genuine $E_f$ level one must retain finite-kernel nonvanishing rather than permit a character limit to leave the fibre [@Morishita2026 Remark 2.1.13, physical p. 13; Lemmas 3.4--3.5 and Theorem 3.6, pp. 23--25].

[\[prop:morishita\]]{#prop:morishita label="prop:morishita"} After restricting to the genuine fixed-prime $E_f$ orbit, imposing finite-kernel nonvanishing, and applying unit normalization, the Morishita character-to-adele map induces a flow-anti-equivariant homeomorphism from an actual inherited Deninger orbit to $C_p^{\mathrm{naive}}$. Both sides are nontrivial indiscrete spaces.

Deninger's equation (35) writes a point of the exact $E_f$ orbit with exponent $a\nu$, where $a=(a_\ell)_{\ell\ne p}\in U_p$ and $\nu\in\mathbb N$. Under Morishita's continuous character-to-adele map, the component at every finite $\ell\ne p$ is $\nu a_\ell$, and is therefore nonzero. This is the finite-kernel nonvanishing check missing from a coarser full-character reading. Diagonal multiplication by $\nu^{-1}\in\mathbb{Q}^\times$, followed by multiplication by the away-from-$p$ integral unit used in [\[thm:adelic\]](#thm:adelic){reference-type="ref" reference="thm:adelic"}, normalizes the image to the displayed class of some $e_p(r)$. Thus the map lands in the exact inherited object $C_p^{\mathrm{naive}}$, not merely in an ambient adelic quotient.

Morishita's Lemmas 3.4--3.5 supply continuity and flow anti-equivariance on this domain [@Morishita2026 physical pp. 23--24]. Orbitwise surjectivity follows from the normalization just described. Both the Deninger orbit and the adelic orbit have the same exact stabilizer $p^{\mathbb{Z}}$, so the induced map is injective as well and hence bijective. By [\[cor:orbit,thm:adelic\]](#cor:orbit,thm:adelic){reference-type="ref" reference="cor:orbit,thm:adelic"}, both actual inherited spaces are nontrivial indiscrete. Every bijection between indiscrete spaces is a homeomorphism, proving the claim. No topology from an ordinary circle is used or transported.

The proposition corrects the earlier compact-to-Hausdorff shortcut. An orbit set with period $\log p$ need not be compact Hausdorff in the inherited topology, and a continuous bijection to a set carrying a different topology says nothing until the codomain owner is fixed.

## Intrinsic scaling circle and standard proxy

Connes and Consani's scaling site assigns to its prime point a periodic orbit isomorphic, with its intrinsic topology, to the ordinary circle $\mathbb{R}_{>0}/p^{\mathbb{Z}}$ [@ConnesConsani2016 Lemma 6.3(i), physical p. 5]. Their later knot/prime comparison likewise operates with a specifically defined adelic/scaling object [@ConnesConsani2026 physical p. 9 and Proposition 3.4, pp. 11--12]. We preserve these source-owned statements. The canonical set comparison from an intrinsic scaling point to a naive adelic double-quotient orbit is not declared to be a homeomorphism.

We also retain a modeling object $$\mathsf C_p^{\mathrm{std}}=(\mathbb{R}_{>0}/p^{\mathbb{Z}})_{\mathrm{standard}},$$ the standard Hausdorff circle with topology imposed by definition. It is useful for the algebraic and Floquet calculations of Paper 8, but it is not an actual inherited Deninger orbit. The four-way owner split is summarized in [\[fig:owners\]](#fig:owners){reference-type="ref" reference="fig:owners"}.

This distinction does not make the intrinsic scaling circle "wrong," nor does it disprove calculations on $\mathsf C_p^{\mathrm{std}}$. It states that topology is part of an object's type. Equal underlying sets, identical stabilizers, and matching action formulas do not erase different topologies.

# Consequences for Paper 8 and Route A {#sec:corrigendum}

## A scoped groupoid consequence

Standard results for transformation groupoids and Zak transforms assume a locally compact Hausdorff setting; for example, Jüstel's strongly proper $G$-space framework begins with explicit topological hypotheses before deriving the transform and decomposition [@Justel2018 Definition 2.1, Lemma 2.3, and Theorem 2.4, physical pp. 3--6]. The actual inherited Deninger packet and orbit fail the Hausdorff unit-space prerequisite by [\[cor:packet,cor:orbit\]](#cor:packet,cor:orbit){reference-type="ref" reference="cor:packet,cor:orbit"}. Therefore the particular standard LCH--Hausdorff transformation-groupoid branches previously proposed for these actual unit spaces do not start.

This is deliberately narrower than a no-go theorem. Non-Hausdorff groupoids have their own theories, and a future construction could conceivably provide a Haar system, a completion, or a trace after adding new hypotheses and proofs. We neither construct nor rule out such an object. In particular, nonclosedness of $\mathcal R_p$ and indiscreteness of the quotient do not by themselves prove that every analytic realization is impossible.

## Versioned Paper-8 corrigendum and retyping

Paper 8 treated an actual inherited orbit as a compact Hausdorff standard circle. The present theorem refutes that premise for the genuine fixed-prime $E_f$ owner. The error propagated to owner labels on a standard-circle groupoid, not to the internal computations once their domain is changed to $\mathsf C_p^{\mathrm{std}}$. Table [\[tab:corrigendum\]](#tab:corrigendum){reference-type="ref" reference="tab:corrigendum"} is the authoritative versioned correction; historical files remain immutable.

P0.26P0.31P0.33

\
Paper-8 statement or branch & Paper-9 correction & Surviving content\
Paper-8 statement or branch & Paper-9 correction & Surviving content\
actual inherited orbit is a compact Hausdorff standard circle & Refuted: the inherited orbit is nontrivial indiscrete. & orbit set, stabilizer $p^{\mathbb{Z}}$, action sign, prime label, and clock $\log p$\
actual one-orbit standard LCH--Hausdorff groupoid & Refuted at the topology prerequisite. & abstract formulas after explicit proxy retyping only\
P8-2--P8-6 owned by the actual orbit & Owner attribution superseded. & internal standard-circle theorems on the proxy identified in [\[tab:routes\]](#tab:routes){reference-type="ref" reference="tab:routes"}\
regular trace on the actual orbit & Retyped to the proxy. & $\mathrm{T}_L(a_f)=Lf(0)$; actual-source transport withheld\
trivial-character trace on the actual orbit & Retyped to the proxy. & $\tau_0(a_f)=L\sum_{r\in\mathbb{Z}}f(rL)$;fixed proxy only\
proxy no-normal-extension theorem & Preserved on the proxy. & exact proxy corner/representation statement only\
packet standard LCH--Hausdorff groupoid & Refuted at the topology gate. & no universal non-Hausdorff no-go\
$Q_p$ quotient properties & Preserved and sharpened. & exact quotient nontrivial indiscrete; no $B_p$ promotion\
actual packet normal extension & Remains not testable. & no analytic refutation inferred\
positive-time scalar Radon ledger & Unchanged; no reissue. & independent typed scalar statement only\

The failed premise is recorded in the Paper-8 evidence chain at , especially lines 232--239. Its propagation appears at and . These locators document provenance; the mathematical correction is proved independently in [\[sec:crt,sec:finite,sec:main\]](#sec:crt,sec:finite,sec:main){reference-type="ref" reference="sec:crt,sec:finite,sec:main"}.

The coefficient-one positive-time scalar ledger counts each rational closed point once and remains a separate scalar measure statement. Its owner does not use a packet topology, groupoid completion, or character trace. It therefore survives unchanged, but it cannot be combined with proxy Floquet data or actual-packet topology as though they were one construction.

## Route A status after the topology correction

The topology theorem supplies a decisive prerequisite failure but no spectral promotion. All eight frozen Stage-9 candidates retain the exploratory verdict shown in [\[tab:routes\]](#tab:routes){reference-type="ref" reference="tab:routes"}. In every row, $A2$, $A3$, and $A4$ fail; Route B is false and is not invoked.

P0.36P0.36Y Candidate & Exact $(A0,A1)$ head & Exact $(A2,A3,A4)$ tail\
`DEN-EF-PACKET-``QUOTIENT-TOPOLOGY-P` & `A0_ANALYTIC_``ARITHMETIC_ORIGIN``A1_WEAK` & `A2_FAIL``A3_FAIL``A4_FAIL`\
`DEN-EF-ORBIT-INHERITED-``TOPOLOGY-P` & `A0_ANALYTIC_``ARITHMETIC_ORIGIN``A1_WEAK` & `A2_FAIL``A3_FAIL``A4_FAIL`\
`DEN-EF-PACKET-ORBIT-``QUOTIENT-Q-P` & `A0_WEAK_ARITHMETIC_``RELATION``A1_FAIL` & `A2_FAIL``A3_FAIL``A4_FAIL`\
`DEN-EF-PACKET-``ACTION-GRPD-P` & `A0_ANALYTIC_``ARITHMETIC_ORIGIN``A1_FAIL` & `A2_FAIL``A3_FAIL``A4_FAIL`\
`DEN-EF-ORBIT-``ACTION-GRPD` & `A0_ANALYTIC_``ARITHMETIC_ORIGIN``A1_FAIL` & `A2_FAIL``A3_FAIL``A4_FAIL`\
`DEN-EF-ORBIT-STD-``CIRCLE-PROXY` & `A0_WEAK_ARITHMETIC_``RELATION``A1_WEAK` & `A2_FAIL``A3_FAIL``A4_FAIL`\
`DEN-EF-ORBIT-STD-CIRCLE-``PROXY-REG-TRACE` & `A0_WEAK_ARITHMETIC_``RELATION``A1_FAIL` & `A2_FAIL``A3_FAIL``A4_FAIL`\
`DEN-EF-ORBIT-STD-CIRCLE-``PROXY-TRIVCHAR-TRACE` & `A0_WEAK_ARITHMETIC_``RELATION``A1_PASS_ANALYTIC` & `A2_FAIL``A3_FAIL``A4_FAIL`\

Gate $A2$ fails because no dynamical zeta function, Fredholm or trace-log determinant, or divisor-comparison test has been defined. Gate $A3$ fails because no global analytic structure, completed divisor, Riemann--von Mangoldt law, or intrinsic Weil-form compression has been supplied. Gate $A4$ fails because there is no natural self-adjoint quantization. The lone $A1$ analytic pass belongs to a proxy trivial-character formula and cannot be transplanted to the actual packet. No tuple licenses a determinant, continuation, functional equation, target-zero comparison, or Hilbert--Pólya statement.

# Reproducibility, controls, and limitations {#sec:controls}

## Deterministic finite controls

The repository contains a deterministic control suite for the constructive steps. The release manifest is $$\texttt{\detokenize{results/packet_separation_manifest.json}},$$ with SHA-256 $$\seqsplit{52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668}.$$ It records 20 of 20 passing tests, eight CSV artifacts, and 240 data rows. The controls use no target zero, fitted parameter, random seed, or empirical acceptance chosen after observation.

Y P0.23 Y Control & Recorded extremum & Interpretation\
positive CRT real approximation & maximum error $6.5383536556262208\times10^{-6}$ & finite instances follow the correct real target\
finite character stabilization & maximum error $0$ & tested finite-order evaluations become exactly constant\
correct suspension sign & maximum time error $7.7964676432670538\times10^{-5}$ & $q_j\to u/v$ drives $q_j^{-1}u\to v$\
wrong-sign negative control & minimum error $10.285714282849066$ & the reversed convention stays separated in tested cases\
$p^{\mathbb{Z}}$ distinctness control & minimum separation $0.31481073984003327$ & chosen time ratios remain outside the tested stabilizer mesh\
artifact integrity & 8 CSVs, 240 rows, 20/20 tests & manifest counts and hashes reproduce\

The executable entry point is ``. A clean rerun regenerates the CSVs and manifest and checks residues, positivity, real convergence, finite-character stabilization, sign orientation, quotient distinctness, and negative controls. The controls are finite witnesses to transcription and implementation consistency. They do not prove density in an infinite product, pointwise convergence on every torsion element, indiscreteness, or nonclosedness. Those are theorems in [\[sec:crt,sec:finite,sec:main\]](#sec:crt,sec:finite,sec:main){reference-type="ref" reference="sec:crt,sec:finite,sec:main"}.

## Evidence and source integrity

The proof was independently audited before composition. The final proof audit, SHA-256 $$\seqsplit{c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8},$$ records `` with zero critical, major, or minor findings. The independent Phase-3 peer review, SHA-256 $$\seqsplit{447a6d575a27c87e3874591dfa3eae5f71ea1714819ada43263ffac44c53a678},$$ records [pass]{.smallcaps} with the same zero-finding counts. The source audit and retained-source manifest bind exact versions and physical-page locators; the 14-file source checksum ledger passes 14/14. These hashes identify the evidence used to compose this version, not external mathematical authorities.

Primary citations in the manuscript bind claims to exact manifestations. Deninger's journal article is cited through arXiv version 4 for technical pagination; the journal DOI identifies the published manifestation. Morishita is cited as arXiv version 5. The Connes--Consani, Le Bruyn, and Jüstel locators identify the retained published or author versions. Local source PDFs support auditability but are excluded from public synchronization; the public release contains bibliographic metadata, locators, hashes, code, results, source, and the built paper, not redistributed publisher files.

## Limitations

First, the theorem is fixed-prime and finite-kernel. It does not classify the topology of the full global rational-Witt suspension, nor does it assert that every other packet-like subspace is indiscrete. Both simultaneous approximation in $A_p$ and legal convergence inside the exact $E_f$ fibre are used.

Second, indiscreteness is a negative separation result, not a constructed analytic theory. We do not provide a non-Hausdorff groupoid, Haar system, convolution completion, regular representation, or trace on the actual packet. Conversely, we prove no universal impossibility theorem for such objects. The only analytic failure asserted is the frozen standard LCH--Hausdorff branch at its Hausdorff unit-space prerequisite.

Third, the intrinsic scaling-site circle and the standard-circle proxy remain valid on their own topologies. The paper does not assign a topology to a generic symbol $B_p$, and it does not transport topology through a canonical set bijection. The Paper-8 corrigendum changes owner attribution, not internal standard-circle algebra.

Fourth, the bounded source search cannot establish absolute historical priority. Its role is to locate the exact source constructions, identify topology ceilings, and check that no direct theorem was found by the cutoff date. The bibliography is intentionally small because only sources used in the mathematical and ownership argument are included.

Finally, the controls are finite and target-free. They detect residue mistakes, wrong signs, loss of positivity, failed stabilization, and accidental equality in selected cases. They neither replace the symbolic proof nor supply evidence for determinant, analytic-continuation, functional-equation, zero-fitting, spectral, or quantization claims.

# Conclusion

For every rational prime $p$, the positive diagonal $\mathbb{Z}[1/p]_{>0}$ simultaneously approximates real scale and prime-to-$p$ profinite character data. Because unit-endpoint approximants remain finite-kernel characters in one raw $E_f$ fibre, this approximation lifts to Deninger's actual fixed-prime prepacket. The resulting sequence stays in a single rational orbit class upstairs while approaching an arbitrary target representative. Downstairs, a constant sequence at any point converges to every other point.

Thus the genuine inherited packet, every inherited periodic orbit, and the time-orbit quotient are nontrivial indiscrete spaces, and the restricted orbit relation is not closed. The naive adelic prime orbit with the exact double-quotient subspace topology has the same separation type, so the repaired Morishita comparison is a homeomorphism between actual indiscrete owners. Neither conclusion changes the independently topologized Connes--Consani scaling circle or a standard-circle proxy.

The correction is therefore one of type discipline: set coordinates, action formulas, stabilizers, and the clock $\log p$ survive, while actual-topology ownership of Hausdorff-circle calculations is withdrawn. The next mathematical question is constructive rather than spectral: whether a useful, explicitly defined non-Hausdorff groupoid or sheaf-theoretic framework can be built on the actual packet without importing the topology of a proxy. That question remains open here.

# Frozen evidence and Route record hashes {#app:hashes}

The manuscript was composed against the following exact records. Hashes make the release auditable and prevent later notes from silently changing the claim envelope.

P0.43P0.48

\
Artifact & SHA-256\
Artifact & SHA-256\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\

The eight Stage-9 YAML SHA-256 values, in the row order of [\[tab:routes\]](#tab:routes){reference-type="ref" reference="tab:routes"}, are:

1.  ;

2.  ;

3.  ;

4.  ;

5.  ;

6.  ;

7.  ;

8.  .

The route audit is the canonical eight-record checksum ledger; this appendix reproduces every bound value for release-level verification.

# Declarations {#declarations .unnumbered}

**Data and code availability.** All manuscript source, native TikZ figures, deterministic control code, generated CSV results, and machine-readable manifest needed to reproduce the reported controls and PDF are included in the Paper-9 project directory. The public synchronization boundary excludes local source PDFs under ``; their bibliographic identities, exact locators, preflight records, and checksums remain available.

**Ethics statement.** This mathematical and computational study involved no human participants, personal data, animals, clinical intervention, or biological material. Institutional ethics approval and informed consent were not applicable.

**Author contributions.** Provisional CRediT record for author confirmation: Liang Wang---conceptualization, methodology, formal analysis, software, validation, investigation, data curation, visualization, writing---original draft, writing---review and editing, and project administration. The final submission metadata must be confirmed by the author.

**Competing interests.** No competing-interest information entered the research analysis. The journal-facing declaration must be confirmed by the author before submission.

**Funding.** No funding information was supplied to or used by this research workflow. The final funding declaration must be confirmed by the author before submission.

**Acknowledgements.** Provisional acknowledgement, subject to author confirmation before submission: thanks are due to the maintainers of the cited open scholarly archives and metadata services that made exact-version source verification possible.

**AI-assistance disclosure.** AI-assisted tools were used for exact-byte comparison, proof drafting, deterministic-control generation, adversarial review, consistency checking, code assistance, and language editing. These tools supplied no authorship credit and assume no responsibility for the work. The human author must verify every theorem, citation, computation, disclosure, and final submission and retains full responsibility upon submission.
