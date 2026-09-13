---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-galois-excess-four-block-incidence-ladder"
canonical_tex: "henon_dynamics/henon_galois_excess_four_block_incidence_ladder/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_galois_excess_four_block_incidence_ladder/paper/paper.pdf"
source_sha256: "727f7bffce40ea85abb8db4edc3a94a08ce8a895a1fe818b88b43b19c52be826"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Infinite Block-Incidence Ladder and a Four-Block Obstruction for Hénon Galois Excess

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_galois_excess_four_block_incidence_ladder>)
- [规范 TeX](<../../../../../henon_dynamics/henon_galois_excess_four_block_incidence_ladder/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_galois_excess_four_block_incidence_ladder/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_galois_excess_four_block_incidence_ladder/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_galois_excess_four_block_incidence_ladder/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a certified mixing symbolic survivor of the area-preserving Hénon map, the Mahler height of each primitive return multiplier splits into physical instability length and a nonnegative Galois excess $\mathcal E_\gamma$. An earlier finite test ruled out potentials depending on at most three symbols but left the required all-period structure unspecified. We construct two explicit primitive families $$A_m=0^{m-2}21,\qquad B_m=0^{m-3}231$$ and prove, for every $m\geq3$, the exact cyclic incidence identity $$\mathsf N_m(A_m)+\mathsf N_m(B_{m+2})
   =\mathsf N_m(A_{m+1})+\mathsf N_m(B_{m+1}).$$ Both differences reduce to the same signed three-atom insertion row. The first new member needed to test this ladder, $B_6$, has an exact radical orbit, trace $18062+5352\sqrt7$, and irreducible reciprocal degree-four multiplier polynomial. Its Galois excess is $\operatorname{arcosh}(9031-2676\sqrt7)$. Combining this with the shared period-five trace field yields a strict exact inequality opposite to the forced $m=4$ periodic-sum identity. Hence no locally constant potential of width at most four realizes all Galois excesses. A determinant-one seven-row minor shows that the same finite witness is interpolable at width five, so the obstruction is finite-level sharp. For a one-sided Hölder realization the infinite ladder gives the explicit necessary condition $|\Delta_m|\leq C(4m+4)\vartheta^{\alpha m}$. Determining the asymptotics of $\Delta_m$ is now the single remaining regularity gate; no general Hölder no-go or arithmetic spectral conclusion is claimed.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: 'An Infinite Block-Incidence Ladder and a Four-Block Obstruction for Hénon Galois Excess'
```

## Markdown 正文

# Introduction

Thermodynamic zeta functions turn periodic-orbit sums of a regular potential into an Euler product or transfer-operator determinant [@Bowen1975; @ParryPollicott1990]. This additive interface is essential: an arbitrary assignment of one number to every primitive orbit need not be the periodic data of any single observable.

For the certified H6 Hénon survivor, HCS-P54 decomposed the Mahler height of every algebraic return multiplier into $$\label{eq:intro-split}
 \mathcal H_\gamma=\ell_\gamma+\mathcal E_\gamma,
 \qquad \mathcal E_\gamma\geq0.$$ The physical roof $\ell_\gamma$ has a source-backed pressure pole, while a regular realization of the nonphysical term $\mathcal E_\gamma$ remains the completion gate [@WangP54]. HCS-P55 attacked its finite-memory forms. Five exact cycles gave a triple-block incidence relation whose corresponding excess identity failed, proving that width at most three is impossible [@WangP55]. More importantly, that paper showed why isolated finite counterexamples cannot settle unrestricted Hölder realizability: any finite orbit list can be interpolated on sufficiently long cylinders.

The present paper makes the next step nonlocal in the block width. We find two natural homoclinic-looking cycle families, prove one incidence relation for every width, and calculate the first new exact orbit required by the family. The result has three layers.

First, the symbolic relation is a theorem for all $m\geq3$, not a computer pattern. Increasing either family by one period inserts one zero into its long zero run. At width $m$, both insertions change the incidence vector by exactly the same signed three-atom row. Subtraction produces the infinite ladder.

Second, the first untested ladder equation, at $m=4$, fails by a wide exact margin. The new period-six orbit has a quadratic trace field and a degree-four multiplier field. A single nonphysical period-five embedding appears in the excess of each of the two period-five cycles, giving a clean lower bound. Elementary square and logarithm inequalities then prove the opposite of the forced identity without relying on decimal separation.

Third, a unimodular width-five minor interpolates all seven finite witness rows. Thus the conclusion is exactly scoped: no width-at-most-four local potential exists, but these seven rows do not obstruct width five. The infinite ladder instead supplies the concrete Hölder target $\Delta_m$: every one-sided Hölder realization forces exponential decay of this explicit sequence. Establishing or refuting that decay is a genuine all-period theorem, not another finite-rank calculation.

No rational-prime orbit law, completed determinant, trace formula or Hilbert--Pólya operator is constructed here. The advance is a sharper regularity obstruction and an exact reusable ladder inside Route A.

# Frozen survivor and cyclic incidence

We retain without refitting the area-preserving map $$\label{eq:henon}
 H_6(q,p)=(1-6q^2-p,q),\qquad \det DH_6=1,$$ and the certified mixing four-state survivor from HCS-P31 [@Henon1976; @WangP31]. Its labels and adjacency matrix are $$0={--},\quad1={-+},\quad2={+-},\quad3={++},
 \qquad
 A=\begin{pmatrix}
 1&0&1&0\\1&0&0&0\\0&1&0&1\\0&1&0&0
 \end{pmatrix}.$$

For a cyclic word $\gamma=(x_0,\ldots,x_{n-1})$, let $$\label{eq:block-count}
 \mathsf N_r(\gamma;w)
 =\#\{0\leq j<n:(x_j,\ldots,x_{j+r-1})=w\},$$ with indices modulo $n$. A width-$r$ potential $\varphi(x)=v(x_0,\ldots,x_{r-1})$ has periodic sum $$\label{eq:block-pairing}
 \mathsf S_\gamma\varphi
 =\sum_w v(w)\mathsf N_r(\gamma;w).$$ Consequently every linear relation among cyclic incidence rows forces the same relation among the periodic sums of every width-$r$ potential.

For a primitive orbit, let $M_\gamma\in\mathrm{SL}_2$ be its chronological monodromy and $\Lambda_\gamma>1$ its physical expanding modulus. If $f_\gamma$ is the monic minimal polynomial of the signed multiplier, then $$\label{eq:excess}
 \mathcal H_\gamma=\log M(f_\gamma),\qquad
 \ell_\gamma=\log\Lambda_\gamma,\qquad
 \mathcal E_\gamma=\mathcal H_\gamma-\ell_\gamma.$$ Reciprocity pairs the roots of $f_\gamma$; all expanding nonphysical pairs contribute nonnegative terms to $\mathcal E_\gamma$, as certified in HCS-P54.

# An infinite incidence ladder

Define two admissible cyclic families $$\label{eq:families}
 A_m=0^{m-2}21\quad(m\geq3),
 \qquad
 B_m=0^{m-3}231\quad(m\geq4).$$ Every displayed transition is allowed by $A$, including the cyclic return $1\to0$. Each word contains exactly one symbol $2$, so it cannot be a proper power. Thus all members are primitive.

Write $e_w$ for the coordinate vector of a block $w$.

[\[lem:insertion\]]{#lem:insertion label="lem:insertion"} For every $m\geq3$, $$\begin{aligned}
 \mathsf N_m(A_{m+1})-\mathsf N_m(A_m)
 &=e_{0^{m-1}2}+e_{10^{m-1}}-e_{10^{m-2}2},\label{eq:A-insertion}\\
 \mathsf N_m(B_{m+2})-\mathsf N_m(B_{m+1})
 &=e_{0^{m-1}2}+e_{10^{m-1}}-e_{10^{m-2}2}.\label{eq:B-insertion}\end{aligned}$$

In each comparison one extra zero is inserted at the beginning of the unique maximal zero run. List the cyclic width-$m$ windows by their start relative to the unique terminal symbol $1$. Windows that see the same part of the zero run cancel bijectively. The longer word adds the windows $0^{m-1}2$ and $10^{m-1}$, while the shorter word has the unmatched window $10^{m-2}2$. The symbols after $2$ distinguish the two families but lie in the portion common to both sides of each comparison, so the same three survivors remain. This gives both identities.

[\[thm:ladder\]]{#thm:ladder label="thm:ladder"} For every integer $m\geq3$, $$\label{eq:ladder}
 \mathsf N_m(A_m)+\mathsf N_m(B_{m+2})
 =\mathsf N_m(A_{m+1})+\mathsf N_m(B_{m+1}).$$

Subtract [\[eq:A-insertion\]](#eq:A-insertion){reference-type="eqref" reference="eq:A-insertion"} from [\[eq:B-insertion\]](#eq:B-insertion){reference-type="eqref" reference="eq:B-insertion"} and rearrange.

The cases $m=3$ and $m=4$ recover respectively the P55 relation and its first extension: $$\begin{aligned}
 \mathsf N_3(A_3)+\mathsf N_3(B_5)&=\mathsf N_3(A_4)+\mathsf N_3(B_4),\\
 \mathsf N_4(A_4)+\mathsf N_4(B_6)&=\mathsf N_4(A_5)+\mathsf N_4(B_5).\end{aligned}$$ The exact program checks the formula independently through $m=64$, but that finite check is evidence for the implementation, not the proof.

# Exact algebra of the new period-six orbit

The new word $B_6=000231$ has sign coordinates $---++-$. Set $$\label{eq:b6-coordinates}
 c=-\frac{\sqrt7}{6},\qquad
 D=\sqrt{25+4\sqrt7},\qquad
 a=\frac{-1-D}{12},\qquad d=\frac{-1+D}{12}.$$

[\[prop:b6\]]{#prop:b6 label="prop:b6"} The cyclic coordinate tuple $$(q_0,\ldots,q_5)=(a,a,c,d,d,c)$$ satisfies $q_{j+1}=1-6q_j^2-q_{j-1}$ exactly and has sign word $---++-$. Its monodromy trace and trace polynomial are $$\begin{aligned}
 T_6&=18062+5352\sqrt7,\label{eq:b6-trace}\\
 Q_6(T)&=T^2-36124T+125728516.\label{eq:b6-trace-poly}\end{aligned}$$ The signed unstable multiplier has irreducible reciprocal polynomial $$\label{eq:b6-multiplier}
 z^4-36124z^3+125728518z^2-36124z+1.$$ Its Galois excess is $$\label{eq:b6-excess}
 \mathcal E_{B_6}=\operatorname{arcosh}(9031-2676\sqrt7).$$

Substitution of [\[eq:b6-coordinates\]](#eq:b6-coordinates){reference-type="eqref" reference="eq:b6-coordinates"} into the six cyclic recurrence equations gives zero. Multiplying the derivative matrices $$DH_6(q_j,q_{j-1})=\begin{pmatrix}-12q_j&-1\\1&0\end{pmatrix}$$ gives determinant one and trace [\[eq:b6-trace\]](#eq:b6-trace){reference-type="eqref" reference="eq:b6-trace"}. Conjugating $\sqrt7\mapsto-\sqrt7$ yields [\[eq:b6-trace-poly\]](#eq:b6-trace-poly){reference-type="eqref" reference="eq:b6-trace-poly"}. Eliminating $T=z+z^{-1}$ gives [\[eq:b6-multiplier\]](#eq:b6-multiplier){reference-type="eqref" reference="eq:b6-multiplier"}; direct factorization over $\mathbb Q$ is irreducible. Concretely, modulo $13$ it becomes $$\bar f(z)=z^4+3z^3+6z^2+3z+1,$$ and $\gcd(\bar f,z^{13}-z)=\gcd(\bar f,z^{169}-z)=1$. Thus it has no linear or quadratic factor over $\mathbb F_{13}$, proving irreducibility over $\mathbb Q$. The nonphysical trace is $18062-5352\sqrt7$, so its expanding reciprocal pair contributes $\operatorname{arcosh}(|T'|/2)$, which is [\[eq:b6-excess\]](#eq:b6-excess){reference-type="eqref" reference="eq:b6-excess"}.

The conjugate half-trace is isolated without floating point: $$\label{eq:b6-isolation}
 1950<9031-2676\sqrt7<1951.$$ Indeed $$7081^2-7\cdot2676^2=13729>0,
 \qquad
 7\cdot2676^2-7080^2=432>0.$$ Numerically, $\mathcal E_{B_6}=8.26922881806116\ldots$; decimals are not used in the obstruction proof.

# The four-block obstruction

The two period-five words $A_5=00021$ and $B_5=00231$ belong to the same degree-six trace field certified in HCS-P55. Its polynomial is $$\begin{aligned}
\label{eq:q5}
 Q_5(T)={}&T^6+3300T^5-34165368T^4-7291075328T^3\notag\\
 &+26529205510272T^2+3609165326736384T
 -4266315336505009664.\end{aligned}$$ It has exactly one root in each interval $$\label{eq:q5-intervals}
 (-7607,-7606),\ (-711,-710),\ (-590,-589),\
 (390,391),\ (770,771),\ (4445,4446).$$ The physical roots for $A_5$ and $B_5$ lie in the first and last intervals respectively. Therefore the root in $(-711,-710)$ is nonphysical for both, and $$\label{eq:p5-lower}
 \mathcal E_{A_5}>\operatorname{arcosh}355,
 \qquad
 \mathcal E_{B_5}>\operatorname{arcosh}355.$$

For $A_4=0021$, the only nonphysical half-trace is $287-96\sqrt6\in(51,52)$, whence $$\label{eq:a4-upper}
 \mathcal E_{A_4}<\operatorname{arcosh}52.$$ Equation [\[eq:b6-isolation\]](#eq:b6-isolation){reference-type="eqref" reference="eq:b6-isolation"} gives $$\label{eq:b6-upper}
 \mathcal E_{B_6}<\operatorname{arcosh}1951.$$

[\[thm:four-block\]]{#thm:four-block label="thm:four-block"} No locally constant potential depending on at most four consecutive H6 states has periodic sums $\mathcal E_\gamma$ on every primitive orbit.

For $x>1$, $$\log(2x-1)<\operatorname{arcosh}x<\log(2x),$$ because $x-1<\sqrt{x^2-1}<x$. Moreover $$709^2=502681>405808=104\cdot3902.$$ Consequently $$2\operatorname{arcosh}355>2\log709
 >\log104+\log3902
 >\operatorname{arcosh}52+\operatorname{arcosh}1951.$$ Combining this with [\[eq:p5-lower\]](#eq:p5-lower){reference-type="eqref" reference="eq:p5-lower"}--[\[eq:b6-upper\]](#eq:b6-upper){reference-type="eqref" reference="eq:b6-upper"} proves $$\label{eq:strict-obstruction}
 \mathcal E_{A_5}+\mathcal E_{B_5}
 >\mathcal E_{A_4}+\mathcal E_{B_6}.$$ But Theorem [\[thm:ladder\]](#thm:ladder){reference-type="ref" reference="thm:ladder"} at $m=4$ forces equality for every width-four potential. A smaller-width potential is also a width-four potential after ignoring the extra coordinates, so every width at most four is excluded.

For scale only, the signed ladder discrepancy with left-minus-right convention is $$\mathcal E_{A_4}+\mathcal E_{B_6}-\mathcal E_{A_5}-\mathcal E_{B_5}
 =-55.5475038022260\ldots .$$ The theorem rests on the exact logarithmic chain, not this decimal.

# Finite sharpness at width five

The four-block relation is not a general finite-data obstruction in disguise. Consider the seven rows $$C_1=(0),\ A_3,\ A_4,\ B_4,\ A_5,\ B_5,\ B_6$$ and the seven width-five blocks $$\label{eq:selected-blocks}
 00000,\ 00021,\ 00023,\ 00210,\ 00231,\ 02102,\ 02310.$$ Their incidence minor, in the displayed row and column order, is $$\label{eq:width5-minor}
 M_5=\begin{pmatrix}
1&0&0&0&0&0&0\\
0&0&0&0&0&1&0\\
0&0&0&1&0&0&0\\
0&0&0&0&0&0&1\\
0&1&0&1&0&0&0\\
0&0&0&0&1&0&1\\
0&0&1&0&1&0&1
\end{pmatrix},\qquad \det M_5=1.$$

[\[prop:sharpness\]]{#prop:sharpness label="prop:sharpness"} Every prescribed real total on these seven cycles is realized by a width-five locally constant potential. In particular, the Galois-excess witness is sharp at width five.

The determinant in [\[eq:width5-minor\]](#eq:width5-minor){reference-type="eqref" reference="eq:width5-minor"} is one. More explicitly, for totals $(E_1,E_3,E_{4A},E_{4B},E_{5A},E_{5B},E_6)$, assign to the blocks in [\[eq:selected-blocks\]](#eq:selected-blocks){reference-type="eqref" reference="eq:selected-blocks"} the values $$E_1,\ -E_{4A}+E_{5A},\ -E_{5B}+E_6,\ E_{4A},\
 -E_{4B}+E_{5B},\ E_3,\ E_{4B},$$ and assign zero to all other width-five blocks. Multiplication by $M_5$ returns the desired totals.

The coefficients need not be nonnegative; the realization problem is for a real potential. Proposition [\[prop:sharpness\]](#prop:sharpness){reference-type="ref" reference="prop:sharpness"} forbids an overstatement: Theorem [\[thm:four-block\]](#thm:four-block){reference-type="ref" reference="thm:four-block"} does not itself disprove arbitrary finite-memory or Hölder realizations. It locates the first four-block failure and identifies the all-width sequence that must be studied next.

# The explicit Hölder discrepancy sequence

Let $\Sigma_A^+$ carry the metric $d_\vartheta(x,y)=\vartheta^{N_+(x,y)}$, where $0<\vartheta<1$ and $N_+$ is the common-prefix length. If $\varphi$ is $\alpha$-Hölder, approximation by a width-$m$ cylinder function has uniform error at most $C\vartheta^{\alpha m}$. Applying the incidence identity [\[eq:ladder\]](#eq:ladder){reference-type="eqref" reference="eq:ladder"} to that approximation yields the following specialization of the quantitative gate from HCS-P55.

[\[cor:holder\]]{#cor:holder label="cor:holder"} If one $\alpha$-Hölder potential on $\Sigma_A^+$ satisfies $\mathsf S_\gamma\varphi=\mathcal E_\gamma$ for every primitive cycle, then for all $m\geq3$, $$\label{eq:delta}
 \Delta_m:=\mathcal E_{A_m}+\mathcal E_{B_{m+2}}
 -\mathcal E_{A_{m+1}}-\mathcal E_{B_{m+1}}$$ satisfies $$\label{eq:holder-bound}
 |\Delta_m|\leq C(4m+4)\vartheta^{\alpha m}.$$

The locally constant approximation is killed exactly by [\[eq:ladder\]](#eq:ladder){reference-type="eqref" reference="eq:ladder"}. The four orbit lengths are $m,m+2,m+1,m+1$, whose sum is $4m+4$. Bounding the approximation error on each orbit gives [\[eq:holder-bound\]](#eq:holder-bound){reference-type="eqref" reference="eq:holder-bound"}.

This is the central upgrade over a vague search for "more relations." One fixed, closed-form family now tests every forward scale. To refute a one-sided Hölder realization it would suffice to prove that $\Delta_m$ fails every bound of the form $Cm\rho^m$ with $0<\rho<1$. Conversely, observed decay is not by itself a construction: one would still need a compatible extension producing a single potential on the whole subshift.

No two-sided conclusion is automatic. Forward block counts control a future-dependent representative. Applying the same condition to an arbitrary two-sided Hölder potential requires an explicit cohomological reduction to such a representative, in the spirit of Livšic theory [@Livshits1972]; periodic data alone do not supply that reduction.

The exact data presently give $\Delta_3>0$ and $\Delta_4<0$, both large in magnitude. Two values do not determine asymptotics. The next major theorem is therefore a recurrence, renormalization law, or certified asymptotic estimate for the Galois excesses along $A_m$ and $B_m$.

# Route status, reproducibility and conclusion

The primary exact producer locks seven upstream artifacts, enumerates all primitive symbolic cycles through period six, verifies the insertion formula through width 64, derives the period-six field, isolates the relevant period-five roots, checks the logarithmic obstruction and rejects twenty claim mutations. An independent program uses DFS and `Counter` incidence rows, recomputes the exact algebra and compares final invariants. Fifteen unit tests exercise the ladder, field, obstruction, interpolation and scope firewalls. Run the full certificate from the project directory with

    bash code/run_c56.sh

No prime table, zero table, fitted potential or post-hoc orbit choice enters the computation.

Under the Route-A evaluator the status remains $$\begin{aligned}
 A1&=\texttt{A1\_WEAK},\\
 A2&=\texttt{A2\_ANALYTIC\_DETERMINANT}
      \quad\text{(physical subsystem only)},\\
 A3&=\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\\
 A4&=\texttt{A4\_FORMAL\_HINT},
 \end{aligned}$$ with overall `ROUTE_A_EXPLORATORY`. The all-width ladder is a stronger structural diagnosis, but it does not give the full Galois-weighted candidate an analytic determinant. Route B is not authorized: no Hilbert space, operator domain, self-adjointness theorem, target spectral type, von-Mangoldt trace, or completed determinant is provided.

The strongest positive result is the infinite incidence ladder together with the exact degree-four multiplier field of $B_6$. The strongest obstruction is the strict failure of its $m=4$ excess identity. The reusable structure is the common three-atom insertion row. The open theorem is the asymptotic behavior of $\Delta_m$, and the most direct next experiment is exact continuation to $m=5,6,\ldots$ coupled to a search for a recurrence in the trace or excess fields.

Accordingly this paper advances the local regularity bridge but not the arithmetic bridge. It claims neither a rational-prime correspondence nor a Riemann-zero spectral realization.

# Exact and numerical ledger

For reproducibility, the principal certified values are

  quantity                     exact value or interval                    decimal value
  ---------------------------- ------------------------------------------ ------------------------
  $\operatorname{tr}M_{B_6}$   $18062+5352\sqrt7$                         $32222.0610\ldots$
  $\mathcal E_{B_6}$           $\operatorname{arcosh}(9031-2676\sqrt7)$   $8.2692288181\ldots$
  $\mathcal E_{A_4}$           $\operatorname{arcosh}(287-96\sqrt6)$      $4.6413895255\ldots$
  $\mathcal E_{A_5}$           period-five height minus physical root     $33.9605061148\ldots$
  $\mathcal E_{B_5}$           period-five height minus physical root     $34.4976160310\ldots$
  $\Delta_4$                   certified strictly negative                $-55.5475038022\ldots$

The exact strictness margin in the final logarithm comparison is $$709^2-104\cdot3902=96873.$$ The seven-by-seven width-five minor has determinant one. The machine-readable certificate records every matrix row, all exact polynomial coefficients, the 20 rejected mutations and the SHA-256 locks of all inherited artifacts.
