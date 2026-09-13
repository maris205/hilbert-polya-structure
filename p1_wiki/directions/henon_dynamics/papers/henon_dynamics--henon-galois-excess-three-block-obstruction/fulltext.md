---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-galois-excess-three-block-obstruction"
canonical_tex: "henon_dynamics/henon_galois_excess_three_block_obstruction/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_galois_excess_three_block_obstruction/paper/paper.pdf"
source_sha256: "3591932533e157214884ff98e686f930ff9762acfc17739ddc521ede0dc358a9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Three-Block Obstruction to Local Galois-Excess Potentials in a Hénon Survivor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_galois_excess_three_block_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_galois_excess_three_block_obstruction/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_galois_excess_three_block_obstruction/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_galois_excess_three_block_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_galois_excess_three_block_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a certified mixing symbolic survivor of the area-preserving Hénon map, an earlier pressure theorem split the Mahler height of every primitive return multiplier into physical instability length and a nonnegative Galois excess $\mathcal E_\gamma$. Completing the full weighted zeta would require that the excess behave like periodic sums of one regular observable. We test the strongest finite-memory version of that requirement. Cyclic block incidence turns every width-$r$ locally constant potential into a linear functional on $r$-block counts. Five exact primitive cycles yield the shortest three-block relation $$\mathsf N_3(\gamma_3)+\mathsf N_3(\gamma_5)
   =\mathsf N_3(\gamma_{4a})+\mathsf N_3(\gamma_{4b}).$$ We derive a new degree-six trace polynomial and reciprocal degree-twelve multiplier polynomial for $\gamma_5$. Exact Sturm isolation gives $\mathcal E_{\gamma_5}>\mathcal E_{\gamma_{4a}}$, while $\mathcal E_{\gamma_3}>0$ and $\mathcal E_{\gamma_{4b}}=0$. The forced periodic-sum identity therefore fails, proving that no potential depending on at most three consecutive symbols realizes the Galois excess on all primitive orbits. The witness is sharp at the finite level: a nonnegative four-block potential interpolates all five rows. More generally, every finite set of periodic totals admits a locally constant interpolation, so finite data cannot refute an unrestricted Hölder realization. We replace that invalid inference by a quantitative higher-block condition on the one-sided H6 presentation: its discrepancies must decay exponentially for Hölder data. A corresponding two-sided conclusion would require an additional future-dependent cohomological reduction. Establishing or violating the one-sided all-period condition remains the next gate.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  A Three-Block Obstruction to Local Galois-Excess Potentials\
  in a Hénon Survivor
```

## Markdown 正文

# Introduction

Periodic-orbit zeta functions for hyperbolic systems are built from additive orbit data: a Hölder potential is summed along each primitive cycle and the resulting weights enter a transfer operator or Euler product [@Bowen1975; @ParryPollicott1990]. This additivity is not cosmetic. It is the interface that permits thermodynamic formalism to control an all-orbit series.

The certified H6 Hénon survivor studied in the preceding packages has a mixing four-state coding and an intrinsic instability roof [@WangP31]. For each primitive cycle $\gamma$, HCS-P54 split the Mahler height of its algebraic return multiplier as $$\label{eq:split-intro}
 \mathcal H_\gamma=\ell_\gamma+\mathcal E_\gamma,
 \qquad \mathcal E_\gamma\geq 0.$$ The physical length $\ell_\gamma$ already has a source-backed pressure pole. The full amplitude would inherit the weighted zeta machinery if one Hölder observable had periodic sums $\mathcal E_\gamma$, but that realization was left open [@WangP54]. The present paper subjects its most local forms to an exact adversarial test.

Our first contribution is a cycle-incidence compiler. A potential depending on $r$ consecutive states pairs linearly with the cyclic $r$-block count of every orbit. Any integer relation among those count vectors therefore forces the same relation among the proposed orbit totals. On the frozen H6 graph, the first three-block relation uses periods three, four, four and five.

The second contribution is new exact algebra for the required period-five orbit. Elimination produces a degree-six polynomial for its monodromy trace and a reciprocal irreducible degree-twelve polynomial for its unstable multiplier. All six trace conjugates are real and lie outside $[-2,2]$, so the Galois excess is an explicit sum of five positive reciprocal-pair lengths. A rational Sturm interval already makes this excess too large for the three-block relation.

The resulting theorem is deliberately finite-memory:

> No locally constant potential depending on at most three consecutive H6 states realizes $\mathcal E_\gamma$ on every primitive cycle.

It does not refute an arbitrary Hölder potential. Indeed, a finite family of disjoint periodic orbits can always be interpolated by a sufficiently long cylinder function. We prove that finite-interpolation firewall and then derive the correct one-sided all-period target: every forward high-block incidence relation must have exponentially small Galois-excess discrepancy if a Hölder realization on the one-sided H6 presentation exists. The unrestricted two-sided question remains open unless one supplies a future-dependent cohomological reduction. This quantitative condition is the reusable bridge to the next paper.

No rational primes or Riemann zeros enter the construction. The result strengthens a local obstruction inside Route A; it does not construct a full Galois-weighted determinant, a trace formula, or a Hilbert--Pólya operator.

# The frozen survivor and excess assignment

We use the area-preserving Hénon map, in the polynomial family introduced by Hénon [@Henon1976], $$\label{eq:henon}
 H_6(q,p)=(1-6q^2-p,q),
 \qquad \det DH_6=1.$$ The certified survivor is conjugate to the mixing subshift $\Sigma_A$ with state labels $$0={--},\qquad 1={-+},\qquad 2={+-},\qquad 3={++}$$ and adjacency matrix $$\label{eq:adjacency}
 A=
 \begin{pmatrix}
 1&0&1&0\\
 1&0&0&0\\
 0&1&0&1\\
 0&1&0&0
 \end{pmatrix}.$$ The state at time $j$ records the signs of $(q_j,q_{j-1})$. The symbolic object, rectangles and hyperbolicity data are inherited without refitting from HCS-P31 [@WangP31].

For a primitive orbit $\gamma$, let $M_\gamma\in\mathrm{SL}_2$ be the chronological monodromy and let $\Lambda_\gamma>1$ be the modulus of its physical unstable multiplier. If $f_\gamma$ is the monic minimal polynomial of the signed unstable multiplier, define $$\label{eq:height}
 \mathcal H_\gamma=\log M(f_\gamma),
 \qquad
 \ell_\gamma=\log\Lambda_\gamma,
 \qquad
 \mathcal E_\gamma=\mathcal H_\gamma-\ell_\gamma.$$ Reciprocity of $f_\gamma$ splits its roots into reciprocal pairs. The physical pair contributes $\ell_\gamma$; every other pair contributes a nonnegative logarithm. This gives [\[eq:split-intro\]](#eq:split-intro){reference-type="eqref" reference="eq:split-intro"} exactly [@WangP48; @WangP54].

We shall use five primitive symbolic cycles: $$\label{eq:witness-cycles}
\begin{aligned}
 \gamma_1&=(0),
 &\gamma_3&=(0,2,1),\\
 \gamma_{4a}&=(0,0,2,1),
 &\gamma_{4b}&=(0,2,3,1),\\
 \gamma_5&=(0,0,2,3,1).
\end{aligned}$$ Direct enumeration of [\[eq:adjacency\]](#eq:adjacency){reference-type="eqref" reference="eq:adjacency"} gives respectively one, zero, one, two and two primitive cycles in periods one through five, agreeing with the independently certified H6 orbit catalogue. Thus [\[eq:witness-cycles\]](#eq:witness-cycles){reference-type="eqref" reference="eq:witness-cycles"} does not select a best orbit from a larger same-period sample.

# The cyclic block-incidence compiler

For an admissible cyclic word $\gamma=(x_0,\ldots,x_{n-1})$ and an admissible word $w=(w_0,\ldots,w_{r-1})$, define $$\label{eq:block-count}
 \mathsf N_r(\gamma;w)
 =\#\{0\leq j<n:(x_j,\ldots,x_{j+r-1})=w\},$$ where indices are read modulo $n$. The vector of all these counts is denoted by $\mathsf N_r(\gamma)$.

A width-$r$ locally constant potential has the form $\varphi(x)=v(x_0,\ldots,x_{r-1})$. Its periodic sum is $$\label{eq:pairing}
 \mathsf S_\gamma\varphi
 =\sum_{j=0}^{n-1}\varphi(\sigma^j x)
 =\sum_w v(w)\mathsf N_r(\gamma;w).$$

[\[lem:incidence\]]{#lem:incidence label="lem:incidence"} If cycles $\gamma_i$ and integers $c_i$ satisfy $$\label{eq:incidence-relation}
 \sum_i c_i\mathsf N_r(\gamma_i)=0,$$ then every width-$r$ locally constant potential satisfies $$\label{eq:sum-relation}
 \sum_i c_i\mathsf S_{\gamma_i}\varphi=0.$$ Conversely, on any finite list of cycles, a prescribed vector of totals is realized by a width-$r$ potential precisely when it annihilates every linear relation among the corresponding incidence rows.

The forward statement follows by pairing [\[eq:incidence-relation\]](#eq:incidence-relation){reference-type="eqref" reference="eq:incidence-relation"} with the coefficient vector $v$. For the converse, the proposed totals define a linear functional on the span of the incidence rows exactly when every row relation is annihilated. Extend that functional to the ambient finite word space and read its coordinates as $v(w)$.

For widths one and two, the first nontrivial relation is already $$\label{eq:edge-relation}
 \mathsf N_r(\gamma_{4a})
 =\mathsf N_r(\gamma_1)+\mathsf N_r(\gamma_3),
 \qquad r=1,2.$$ At width two this simply says that the directed edges of $\gamma_{4a}$ are $$00,02,21,10,$$ the disjoint multiset union of the edge $00$ from $\gamma_1$ and the edges $02,21,10$ from $\gamma_3$.

The decisive next relation occurs at width three: $$\label{eq:triple-relation}
 \mathsf N_3(\gamma_3)+\mathsf N_3(\gamma_5)
 =\mathsf N_3(\gamma_{4a})+\mathsf N_3(\gamma_{4b}).$$ Indeed the two sides are the same multiset $$\{002,021,023,100,102,210,231,310\}.$$ The relation is exact symbolic homology; no numerical orbit data enter it.

# Exact period-four and period-five Galois data

The second period-four cycle has rational trace (578), so its multiplier polynomial is quadratic and $$\label{eq:E4b}
 \mathcal E_{4b}=0.$$ The other period-four cycle has coordinate sequence $$\label{eq:p4a-coordinates}
 (a,b,-a,b),\qquad
 a=-\frac{\sqrt{6+2\sqrt6}}6,\qquad b=-\frac{\sqrt6}{6}.$$ Substitution into the recurrence $q_{j+1}=1-6q_j^2-q_{j-1}$ gives zero identically. Multiplying the Jacobians in chronological order gives $$\label{eq:p4a-trace}
 \operatorname{tr}M_{4a}=-574-192\sqrt6,$$ and the signed unstable multiplier has minimal polynomial $$\label{eq:p4a-minpoly}
 z^4-1148z^3+108294z^2-1148z+1.$$ The nonphysical reciprocal pair therefore contributes $$\label{eq:E4a}
 \mathcal E_{4a}=\operatorname{arcosh}(287-96\sqrt6)
 =4.641389525467404250\ldots.$$

For $\gamma_5$, write the coordinate sequence as $$\label{eq:p5-pattern}
 (a,b,c,c,b),\qquad
 b=\frac12-3a^2,\qquad
 c=-54a^4+18a^2-a-\frac12.$$ The closing condition factors into the fixed-point factor and $$\label{eq:p5-coordinate-poly}
 F_5(a)=5832a^6-1944a^5-2268a^4+648a^3+144a^2-12a-1=0.$$ The physical root lies in $(-279433/500000,-111773/200000)$, an interval containing exactly one root of $F_5$. On this interval, Sturm counts show that the derivatives of $b(a)$, $c(a)$, and the reduced trace have no zeros; their signs at the midpoint are respectively $+,+,-$. Exact endpoint evaluation then gives the sign word $(-,-,+,+,-)$ and shows that the reduced trace is strictly decreasing. Thus this interval certifies the intended H6 cycle, not merely an unlabeled algebraic root. Reducing the chronological trace modulo $F_5$ and eliminating $a$ gives the irreducible polynomial $$\begin{aligned}
\label{eq:p5-trace-poly}
 Q_5(t)={}&t^6+3300t^5-34165368t^4-7291075328t^3\\
 &+26529205510272t^2+3609165326736384t\\
 &-4266315336505009664.\end{aligned}$$ Sturm isolation gives one root in each interval $$\label{eq:trace-intervals}
\begin{split}
 &(-7607,-7606),\quad(-711,-710),\quad(-590,-589),\\
 &(390,391),\quad(770,771),\quad(4445,4446).
\end{split}$$ Exact endpoint inequalities $4445<t(a_{\rm right})<t(a_{\rm left})<4446$ place the physical trace in the last interval. In particular every trace conjugate is real and has modulus greater than two.

The reciprocal multiplier polynomial is exactly $$\label{eq:p5-multiplier}
 G_5(z)=z^6Q_5(z+z^{-1}),$$ an irreducible monic polynomial of degree twelve. If $\theta_1<\cdots<\theta_6$ are the roots of $Q_5$, then $$\label{eq:p5-excess}
 \mathcal E_5=\sum_{j=1}^{5}
 \operatorname{arcosh}\!\left(\frac{|\theta_j|}{2}\right)
 =34.497616030977493114\ldots,$$ where $\theta_6$ is the physical embedding.

Only a coarse exact consequence is needed. The positive nonphysical root in $(390,391)$ gives $$\label{eq:E5-lower}
 \mathcal E_5>\operatorname{arcosh}(195).$$ On the other hand $287-96\sqrt6<52<195$; the first inequality follows from $96^2\cdot6-235^2=71>0$. Monotonicity of $\operatorname{arcosh}$ yields $$\label{eq:E5-E4a}
 \mathcal E_5>\mathcal E_{4a}.$$ All polynomial identities and root counts are recomputed independently in the certificate package.

# The three-block obstruction

The inherited period-three row is $$\label{eq:E3}
 \mathcal E_3=\operatorname{arcosh}(21\sqrt5-19)>0.$$

[\[thm:three-block\]]{#thm:three-block label="thm:three-block"} There is no locally constant potential on $\Sigma_A$, depending on at most three consecutive states, whose periodic sum equals $\mathcal E_\gamma$ for every primitive H6 orbit $\gamma$. In fact the five cycles in [\[eq:witness-cycles\]](#eq:witness-cycles){reference-type="eqref" reference="eq:witness-cycles"} already force the contradiction.

A potential depending on fewer than three coordinates can be regarded as a three-coordinate potential that ignores the extra symbols. Lemma [\[lem:incidence\]](#lem:incidence){reference-type="ref" reference="lem:incidence"} and [\[eq:triple-relation\]](#eq:triple-relation){reference-type="eqref" reference="eq:triple-relation"} would therefore force $$\label{eq:forced-excess}
 \mathcal E_3+\mathcal E_5=\mathcal E_{4a}+\mathcal E_{4b}.$$ But [\[eq:E4b\]](#eq:E4b){reference-type="eqref" reference="eq:E4b"}, [\[eq:E5-E4a\]](#eq:E5-E4a){reference-type="eqref" reference="eq:E5-E4a"} and [\[eq:E3\]](#eq:E3){reference-type="eqref" reference="eq:E3"} imply $$\mathcal E_3+\mathcal E_5>\mathcal E_{4a}+\mathcal E_{4b}.$$ This contradicts [\[eq:forced-excess\]](#eq:forced-excess){reference-type="eqref" reference="eq:forced-excess"}.

[\[cor:memory\]]{#cor:memory label="cor:memory"} Any locally constant realization of the full Galois-excess assignment must depend on at least four consecutive symbolic states.

The theorem is stronger than a scalar-roof no-go. It excludes every signed nearest-state, edge and triple potential, with no positivity assumption and without quotienting by coboundaries: periodic coboundaries sum to zero and cannot repair the failed identity. It also explains why thermodynamic formalism cannot simply be invoked after fitting a few orbit weights. The weight must first exist in a source-compatible regularity class.

# What a genuine Hölder test must prove

Livšic's theorem characterizes cohomological nullity through periodic orbit sums for hyperbolic and topological Markov systems [@Livshits1972]. Its use here requires a logical distinction: periodic sums determine the cohomology class of an observable that already exists; they do not assert that an arbitrary assignment $\gamma\mapsto\mathcal E_\gamma$ comes from a Hölder observable.

For the quantitative statement, pass explicitly to the one-sided H6 presentation $\Sigma_A^+$. Let $d_\vartheta(x,y)=\vartheta^{N_+(x,y)}$, with $0<\vartheta<1$, where $N_+(x,y)$ is the length of the common initial word. If $\varphi$ is Hölder with exponent $\alpha$, its variation on a forward $m$-cylinder is at most $C\vartheta^{\alpha m}$. This convention is exactly the one measured by the forward cyclic block counts $\mathsf N_m$.

[\[thm:holder-gate\]]{#thm:holder-gate label="thm:holder-gate"} Suppose $\mathcal E_\gamma=\mathsf S_\gamma\varphi$ for every primitive cycle and some $\alpha$-Hölder potential $\varphi:\Sigma_A^+\to\mathbb R$. If cycles $\gamma_i$ and integers $c_i$ satisfy $$\label{eq:m-relation}
 \sum_i c_i\mathsf N_m(\gamma_i)=0,$$ then $$\label{eq:holder-discrepancy}
 \left|\sum_i c_i\mathcal E_{\gamma_i}\right|
 \leq C\vartheta^{\alpha m}
 \sum_i |c_i|\,|\gamma_i|.$$

Choose one representative in every nonempty $m$-cylinder and let $\varphi_m$ be the locally constant function taking the representative value there. Then $\|\varphi-\varphi_m\|_\infty\leq C\vartheta^{\alpha m}$. The incidence relation kills $\sum_i c_i\mathsf S_{\gamma_i}\varphi_m$ by Lemma [\[lem:incidence\]](#lem:incidence){reference-type="ref" reference="lem:incidence"}. The remaining error on $\gamma_i$ is at most $|\gamma_i|\|\varphi-\varphi_m\|_\infty$, and summation gives [\[eq:holder-discrepancy\]](#eq:holder-discrepancy){reference-type="eqref" reference="eq:holder-discrepancy"}.

Thus a general one-sided Hölder no-go cannot come from one finite relation at fixed $m$. It requires a sequence of exact higher-block relations for which the normalized excess discrepancy does not admit any exponential decay. A positive result would instead establish a compatible exponent and constant, then still need an extension theorem producing one observable on all of $\Sigma_A$. Equation [\[eq:holder-discrepancy\]](#eq:holder-discrepancy){reference-type="eqref" reference="eq:holder-discrepancy"} is the correct all-period gate for either direction in this presentation. No claim about an arbitrary two-sided Hölder assignment is obtained without an additional cohomological reduction to a future-dependent representative.

# Finite sharpness and the interpolation firewall

The five-cycle witness is sharp with respect to block width. Consider the five four-blocks $$0000,\quad0021,\quad0023,\quad0210,\quad0231.$$ Their incidence columns on the row order $(\gamma_1,\gamma_3,\gamma_{4a},\gamma_{4b},\gamma_5)$ form $$\label{eq:width4-matrix}
 B_4=
 \begin{pmatrix}
 1&0&0&0&0\\
 0&0&0&1&0\\
 0&1&0&1&0\\
 0&0&0&0&1\\
 0&0&1&0&1
 \end{pmatrix},
 \qquad \det B_4=-1.$$ Assign the respective potential values $$\label{eq:width4-values}
 \mathcal E_1,\quad
 \mathcal E_{4a}-\mathcal E_3,\quad
 \mathcal E_5-\mathcal E_{4b},\quad
 \mathcal E_3,\quad
 \mathcal E_{4b},$$ and set all other four-block values to zero. This matches all five excesses. It is nonnegative: $\mathcal E_{4b}=0$, and $\mathcal E_{4a}>\mathcal E_3$ follows from $$287-96\sqrt6>51>28>21\sqrt5-19,$$ where the two radical comparisons square to positive integer margins.

This finite interpolation is not evidence for an all-orbit four-block model. It instead illustrates a general obstruction to finite falsification.

[\[prop:finite-interpolation\]]{#prop:finite-interpolation label="prop:finite-interpolation"} Let $\gamma_1,\ldots,\gamma_k$ be distinct periodic orbits of a subshift of finite type. For arbitrary real totals $a_1,\ldots,a_k$, there is a locally constant function $\psi$ such that $\mathsf S_{\gamma_i}\psi=a_i$ for every $i$.

The union of the selected orbits is finite. Around one chosen point of each orbit, take a sufficiently long cylinder containing no other point from this finite union and no other point of the same orbit. Let its indicator be $b_i$. Then $\mathsf S_{\gamma_j}b_i=\delta_{ij}$. The locally constant function $\psi=\sum_i a_i b_i$ has the required totals.

Consequently no finite orbit table, however exact, can disprove unrestricted Hölder realizability. The valid conclusion of Theorem [\[thm:three-block\]](#thm:three-block){reference-type="ref" reference="thm:three-block"} is the explicit locality lower bound. The valid next test is the quantitative sequence in Theorem [\[thm:holder-gate\]](#thm:holder-gate){reference-type="ref" reference="thm:holder-gate"}, not a larger finite interpolation followed by a Hölder claim.

# Route status, reproducibility and conclusion

The exact producer enumerates all primitive symbolic cycles through period five, derives both new trace fields, checks the Sturm intervals, verifies the block relations and rejects seventeen claim/interface mutations. A second program uses a DFS cycle enumeration and independently reconstructs the resultants and inequalities. Fourteen unit tests exercise the source locks, incidence matrices, algebraic rows, scope firewall and independent path. The complete finite audit is

    bash code/run_c55.sh

from the project directory. It uses no prime table, zero table, fitted potential or post-hoc orbit selection.

Under the Route-A evaluator, the status remains $$\begin{aligned}
 A1&=\texttt{A1\_WEAK},\\
 A2&=\texttt{A2\_ANALYTIC\_DETERMINANT}
       \quad\text{(physical subsystem only)},\\
 A3&=\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\\
 A4&=\texttt{A4\_FORMAL\_HINT},
 \end{aligned}$$ with overall `ROUTE_A_EXPLORATORY`. P55 strengthens the obstruction at the full Galois-weighted interface; it does not give that full candidate an A2 pass. Route B is not authorized because no Hilbert space, operator domain, self-adjointness theorem, target spectral type, von-Mangoldt trace or completed determinant is supplied.

The strongest positive result is an exact cycle-homology compiler together with a new period-five multiplier field. The strongest negative result is the width-three no-go. The open theorem is now precise: either construct an all-period Hölder or controlled asymptotically additive realization, or find forward higher-block relations whose normalized Galois-excess discrepancies violate every exponential bound in [\[eq:holder-discrepancy\]](#eq:holder-discrepancy){reference-type="eqref" reference="eq:holder-discrepancy"} on the one-sided presentation. The first new finite algebraic checkpoint is the shortest four-block relation, which involves periods four, five, five and six.

These conclusions advance the local regularity diagnosis but not the arithmetic bridge. No rational-prime orbit correspondence, completed Riemann divisor, Hilbert--Pólya realization or proof of the Riemann hypothesis is claimed.

# Exact elimination ledger

For auditability we record the full reciprocal polynomial associated with [\[eq:p5-trace-poly\]](#eq:p5-trace-poly){reference-type="eqref" reference="eq:p5-trace-poly"}: $$\begin{aligned}
G_5(z)={}&z^{12}+3300z^{11}-34165362z^{10}-7291058828z^9\\
&+26529068848815z^8+3609143453543400z^7\\
&-4266262278298981308z^6+3609143453543400z^5\\
&+26529068848815z^4-7291058828z^3-34165362z^2\\
&+3300z+1.\end{aligned}$$ Exact factorization over $\mathbb Q$ leaves one degree-twelve factor. The trace polynomial values at the endpoints of each interval in [\[eq:trace-intervals\]](#eq:trace-intervals){reference-type="eqref" reference="eq:trace-intervals"} have opposite signs, and Sturm counts equal one in all six intervals; the six counts exhaust its degree. The physical coordinate interval contains one root of $F_5$. Sturm counts for the derivatives of $b(a)$, $c(a)$, and the reduced trace are all zero, and their midpoint signs are $+,+,-$. Consequently the symbolic signs are $(-,-,+,+,-)$, and on that interval the reduced trace $$-4(174960a^5-6804a^4-53136a^3+4050a^2+2457a-76)$$ lies strictly between (4445) and (4446), identifying the physical embedding without a floating-point label.

The certificate stores the exact coordinate and trace polynomials, all six Sturm counts, the degree-twelve reciprocal polynomial, the five reciprocal pair contributions to $\mathcal E_5$, the block-incidence matrices and the unimodular width-four minor. Decimal values are reports of exact objects and are not used to prove the obstruction.
