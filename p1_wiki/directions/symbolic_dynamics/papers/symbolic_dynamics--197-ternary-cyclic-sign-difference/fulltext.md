---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--197-ternary-cyclic-sign-difference"
canonical_tex: "symbolic_dynamics/papers/197-ternary-cyclic-sign-difference/main.tex"
canonical_pdf: "symbolic_dynamics/papers/197-ternary-cyclic-sign-difference/main.pdf"
source_sha256: "3958fd63a7a7487bceb9720fb140426651d27fb51bab79dc03a30286eb4deda0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Fourth-Root-of-Shift Core and Exact Fibonacci Fibres\protect for Ternary Cyclic Sign Differences

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/197-ternary-cyclic-sign-difference>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/197-ternary-cyclic-sign-difference/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/197-ternary-cyclic-sign-difference/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/197-ternary-cyclic-sign-difference/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/197-ternary-cyclic-sign-difference/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the synchronous map $D(x)_i=\operatorname{sgn}(x_{i+1}-x_i)$ on labelled ternary cyclic words. Its recurrent set is exactly the local language $D^4x=\rho^2x$, where $\rho$ is left shift. The maximal transient is $n-1$ at even length and $n-2$ at odd length at least three, with a separate singleton boundary. Finite local certificates prove attraction for every length, and de Bruijn traces enumerate all depths and cycles. Independently, every one-step fibre is a comparison-walk trace. Contracting equality edges and cutting at doubled sign runs gives an explicit product of Fibonacci numbers. This yields the sharp Lucas maximum and all maximizing targets, including the additional ties at lengths two and three. The local rule, proof, and exact verifier are distinguished from generic cellular-automaton and transfer-matrix methods. The bounded source audit leaves this anonymous theorem note `OWNER_AMBER / HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: |
  A Fourth-Root-of-Shift Core and Exact Fibonacci Fibres\
  for Ternary Cyclic Sign Differences
```

## Markdown 正文

# The map and its claim boundary

Fix $n\ge1$, use indices in $\mathbb Z/n\mathbb Z$, and put $$\label{eq:map}
X_n=\{-1,0,1\}^n,\qquad D(x)_i=\operatorname{sgn}(x_{i+1}-x_i),\qquad
(\rho x)_i=x_{i+1}.$$ All coordinates are read before the update. The tail $\tau(x)$ is the first entrance time into a periodic orbit, so periodic points have tail zero. For an open word $w$, let $\delta w$ be its adjacent sign-difference word without wraparound; each application shortens the word by one.

Finite-alphabet cellular dynamics, shifts of finite type, trace enumeration, and Möbius inversion are standard tools [@LindMarcus1995; @Stanley2011]. Fukś studies solvable ternary rules induced by associative operations [@Fuks2026]. Our operation $d(a,b)=\operatorname{sgn}(b-a)$ is not associative: $d(d(-1,-1),0)=0$ whereas $d(-1,d(-1,0))=1$. Thus it is not an associative rule under a direct alphabet isomorphism or passage to the opposite operation. This argument does not exclude higher-block factors, time iterates, or other encodings.

The closest internal comparison is P164's cyclic equality front: at its three-letter input slice, $\mathbf1\{x_i=x_{i+1}\}=\mathbf1\{D(x)_i=0\}$ exactly. We concede this first-step projection, not a dynamical conjugacy of the full ternary evolution to the subsequent binary equality dynamics. P90's traffic rule, P117's run reversal, P187's positive valuation differences, P190's support erosion, and P196's one-step implication core are further occupied neighbors. Generic local erosion, cyclic traces and Fibonacci identities receive no contribution credit. The residual claim is the joint sharp temporal and target-resolved inverse theorem for [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}; no novelty or priority certification is asserted.

# The recurrent core and sharp attraction

Define $$\label{eq:core}
K_n=\{x\in X_n:D^4x=\rho^2x\}.$$ For a nonconstant cyclic word write $R(x)$ for its longest constant run.

[\[lem:local\]]{#lem:local label="lem:local"} If $w$ has length six and no equal adjacent letters, then $\delta^5(w)_0=\delta(w_2w_3)_0$. If $w$ has length seven and no constant factor of length three, then $$\label{eq:local}
\delta^6(w)_0=\delta^2(w_2w_3w_4)_0.$$ Consequently $R(x)=1$ implies $Dx\in K_n$, and $R(x)\le2$ implies $D^2x\in K_n$.

These are finite local identities, independent of the cyclic length. Negation and reversal reduce the middle pair in the first identity to $-0$ or $-+$, whose symmetry orbits have sizes four and two. Each admits 16 outer extensions with no adjacent equality; direct successive comparison gives $+$ in all 32 representative extensions. This covers $96=3\cdot2^5$ words. Here and below $-$ and $+$ mean $-1$ and $1$.

For the second identity, the complete representative calculation is

   middle triple    orbit size   outer extensions  both sides of [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"}
  --------------- ------------ ------------------ --------------------------------------------------------------------------------------
       $--0$                 4                 48                                          $+$
       $--+$                 4                 48                                          $+$
       $-0-$                 2                 64                                          $-$
       $-00$                 4                 48                                          $-$
       $-0+$                 2                 64                                          $0$
       $-+-$                 2                 64                                          $-$
       $-+0$                 4                 64                                          $-$
       $0-0$                 2                 64                                          $+$

For each row, range the four outer letters over the three-letter alphabet, discard constant triples, and successively replace adjacent pairs by their sign difference. The displayed output is constant on exactly the indicated extensions. The orbit-weighted count is 1,344, all length-seven words with no constant triple. Negation and reversal transform both sides identically, so the table proves the identity. Applying the identities at each cyclic position proves the conclusions, even when a window wraps repeatedly. The exact verifier reproduces the entire finite certificate, not just sample cyclic words.

[\[thm:tail\]]{#thm:tail label="thm:tail"} For every $n\ge1$, $K_n$ is exactly the recurrent set. On this set, $D^{-1}=\rho^{-2}D^3$, and $$\label{eq:clock}
\tau(x)=\min\{t\ge0:D^{t+4}x=\rho^2D^t x\}.$$ For every nonconstant $x$, $\tau(x)\le R(x)$. Moreover $$\label{eq:height}
\max_{x\in X_n}\tau(x)=
\begin{cases}1,&n=1,\\n-1,&n\text{ even},\\n-2,&n\ge3\text{ odd}.
\end{cases}$$ Every recurrent period divides $4n/\gcd(n,2)$.

A zero run of $Dx$ of length $q$ comes from $q+1$ equal old letters. A nonzero constant run comes from a strictly monotone chain in three levels, so has length at most two. Thus $$\label{eq:run}
R(Dx)\le\max\{R(x)-1,2\}$$ whenever the new word is nonconstant. If it is constant, it must be zero, because cyclic strict increase or decrease is impossible. Combining [\[eq:run\]](#eq:run){reference-type="eqref" reference="eq:run"} with Lemma [\[lem:local\]](#lem:local){reference-type="ref" reference="lem:local"} gives entrance into $K_n$ in at most $R(x)$ steps. A constant word maps immediately to zero.

The map commutes with $\rho$, so $K_n$ is invariant. Equation [\[eq:core\]](#eq:core){reference-type="eqref" reference="eq:core"} makes $\rho^{-2}D^3$ a two-sided inverse there. It is therefore a permutation of this finite set, and every orbit enters it. This proves the recurrence and pointwise-tail claims. On the core, $D^{4n/\gcd(n,2)}=\rho^{2n/\gcd(n,2)}=\mathrm{id}$.

For sharpness, choose $x=0^{n-1}1$. More generally, for a one-exception word $a^{n-1}b$ put $s=\operatorname{sgn}(b-a)$, where $a\ne b$. Then $Dx=0^{n-2}s(-s)$. Write $\operatorname{Alt}_l(s)=(s,-s,s,\ldots)$ and observe, for $r\ge1$, $l\ge2$, that $$\label{eq:witness}
D(0^r\operatorname{Alt}_l(s))=0^{r-1}\operatorname{Alt}_{l+1}(s).$$ At even length, the fully alternating word is mapped to its negative and belongs to $K_n$. At odd length $n=2m+1$, the one-zero endpoint $w=0\operatorname{Alt}_{2m}(s)$ has the four phases $$\begin{aligned}
Dw&=\operatorname{Alt}_{2m+1}(s),&D^2w&=\operatorname{Alt}_{2m}(-s)0,\\
D^3w&=\operatorname{Alt}_{2m}(s)(-s),&D^4w&=\operatorname{Alt}_{2m-1}(-s)0s=\rho^2w.\end{aligned}$$ The last two letters of $D^3w$ agree; these formulas include $m=1$.

None of the earlier phases $z=0^r\operatorname{Alt}_l(s)$ enters the core. For $r\ge4$, $(D^4z)_{r-4}=s$ but $(\rho^2z)_{r-4}=0$. At $r=3$ the discrepancy is $-s$ versus zero at coordinate zero. At $r=2$ it is a nonzero sign versus zero at coordinate $n-2$, since $D^2z$ is fully alternating. At $r=1$ and even $n$, $D^4z$ is nonzero at $n-2$, whereas $\rho^2z$ is zero there. Thus the first entrance occurs at $n-1$ for even $n$ and $n-2$ for odd $n\ge3$. The original one-exception word cannot already be recurrent unless its successor is; for $n=2,3$ directly checking the chosen $0^{n-1}1$ supplies the one-step lower bound. Not every choice of $a,b$ is sharp at these small lengths.

For the global upper bound, all nonconstant words except the one-exception form have $R\le n-2$, and all constants have tail at most one. This proves [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"} for $n\ge2$. At $n=1$, both nonzero letters map to the unique fixed letter zero, giving the separate boundary.

# Depths and cycles as exact finite traces

For $t\ge0$ define the zero-one de Bruijn matrix $A_t$ on words of length $t+4$. An overlap edge associated with $w=w_0\cdots w_{t+4}$ is allowed exactly when $$\label{eq:At}
\delta^{t+4}(w)_0=\delta^t(w_2\cdots w_{t+2})_0.$$ For $p\ge1$ define $C_p$ on words of length $p$ by allowing an edge $w_0\cdots w_p$ exactly when $\delta^p(w)_0=w_0$.

[\[thm:trace\]]{#thm:trace label="thm:trace"} For all $n\ge1,t\ge0,p\ge1$, $$\begin{aligned}
\#\{x:\tau(x)\le t\}&=\operatorname{tr}(A_t^n),\label{eq:cdf}\\
\#\operatorname{Fix}(D^p)&=\operatorname{tr}(C_p^n).\label{eq:fix}\end{aligned}$$ The depth-$t$ count is the difference of consecutive CDF values (with previous value zero at $t=0$). The number of least-period-$p$ cycles is $$\label{eq:cycles}
\frac1p\sum_{d\mid p}\mu(p/d)\operatorname{tr}(C_d^n),$$ where $\mu$ is the number-theoretic Möbius function.

A closed overlap walk of length $n$ uniquely specifies its labelled cyclic word, including when $n$ is shorter than a window. The local constraint [\[eq:At\]](#eq:At){reference-type="eqref" reference="eq:At"} is precisely the equality in [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} at every coordinate. The analogous statement for $C_p$ is $D^px=x$. This proves both traces; partitioning iterate-fixed points by least period and applying Möbius inversion proves [\[eq:cycles\]](#eq:cycles){reference-type="eqref" reference="eq:cycles"}.

For explicit core counts, $A_0$ has 81 vertices, 165 edges, and $$\label{eq:charpoly}
\det(zI-A_0)=z^{74}(z-1)(z^3-z^2-2z-1)(z^3+z^2+2z+1).$$ This is a finite exact matrix calculation from [\[eq:At\]](#eq:At){reference-type="eqref" reference="eq:At"}. A short reproducible certificate computes $s_j=\operatorname{tr}(A_0^j)$ for $1\le j\le81$, sets $c_0=1$, and uses Newton's identity $jc_j=-\sum_{i=1}^j c_{j-i}s_i$. It gives $(c_1,\ldots,c_7)=(-1,-1,-3,-2,2,3,1)$ and $c_8=\cdots=c_{81}=0$, which is [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}. Integer matrix multiplication and exact divisions suffice; the verifier checks all 81 coefficients, not a fitted short recurrence. Therefore, writing $R_n=|K_n|$, $$\begin{gathered}
(R_1,\ldots,R_7)=(1,3,13,27,41,93,225),\\
R_n=R_{n-1}+R_{n-2}+3R_{n-3}+2R_{n-4}
-2R_{n-5}-3R_{n-6}-R_{n-7}\quad(n\ge8).\end{gathered}$$ The dimensions of $A_t$ and $C_p$ grow with $t,p$. These are exact finite algorithms, not efficient fixed-size formulas; the divisibility bound is not a claim that every divisor occurs.

# Every target fibre and its exact gap product

Index the three levels increasingly and set $$\label{eq:matrices}
U=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix},\qquad
V=U^{\mathsf T},\qquad M_+=U,\quad M_-=V,\quad M_0=I.$$ Let $F_0=0,F_1=1$ and $L_0=2,L_1=1$ denote Fibonacci and Lucas numbers. For a target $y$, its strict skeleton is obtained by deleting all zeros, retaining cyclic order. Its length is denoted $r$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} For every $y\in X_n$, including targets outside the image, $$\label{eq:fibre}
|D^{-1}(y)|=\operatorname{tr}(M_{y_0}\cdots M_{y_{n-1}}).$$ An all-zero target has fibre three. A nonempty skeleton is realizable exactly when it contains both signs and each cyclic sign run has length at most two. If all runs have length one, its fibre is $L_r$. Otherwise let $q$ be its number of doubled runs, and $g_j$ the number of singleton runs between doubled runs $j$ and $j+1$, cyclically. Then $$\label{eq:gap}
|D^{-1}(y)|=\prod_{j=1}^q F_{g_j+1},\qquad
r=2q+\sum_jg_j,\qquad q\equiv r\pmod2.$$

The entry $M_s(a,b)$ is the indicator of $\operatorname{sgn}(b-a)=s$. Multiplication and trace count precisely all closed level assignments, proving [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Identity matrices may be deleted. A single-sign skeleton gives a strictly triangular product with zero trace. Also $U^2=E_{13}$, $V^2=E_{31}$ and $U^3=V^3=0$, so a cyclic run of length at least three has zero fibre. A realizable nonconstant skeleton has an even number of runs, giving the parity relation in [\[eq:gap\]](#eq:gap){reference-type="eqref" reference="eq:gap"}.

Each doubled run is rank one. For successive blocks $u_jv_j^{\mathsf T}$ and intervening products $B_j$, their cyclic trace factors as $$\operatorname{tr}(u_1v_1^{\mathsf T}B_1\cdots u_qv_q^{\mathsf T}B_q)
=\prod_j v_j^{\mathsf T}B_ju_{j+1},\qquad u_{q+1}=u_1.$$ Starting at $U^2$, a gap of $g=2a$ singleton runs contributes $e_3^{\mathsf T}(VU)^ae_3=F_{2a+1}$; a gap of $g=2a+1$ contributes $e_3^{\mathsf T}(VU)^aVe_1=F_{2a+2}$. Indeed the lower-right block of $(VU)^a$, for $a\ge1$, is $$\begin{pmatrix}F_{2a-1}&F_{2a}\\F_{2a}&F_{2a+1}\end{pmatrix};$$ induction proves this identity, and at $a=0$ both required scalars are one. Reversing the level order treats a starting $V^2$. This proves [\[eq:gap\]](#eq:gap){reference-type="eqref" reference="eq:gap"}, whose factors are positive, establishing sufficiency of the image condition. With no doubled run the even alternating product has trace $\operatorname{tr}((UV)^{r/2})=F_{r-1}+F_{r+1}=L_r$.

[\[thm:max\]]{#thm:max label="thm:max"} For $n\ge2$, the maximal fibre is $L_{2\lfloor n/2\rfloor}$. For even $n\ge4$ exactly the two fully alternating targets maximize. For odd $n\ge5$ exactly the $2n$ targets with one zero and alternating remaining signs maximize. At $n=2,3$ the all-zero target also ties, giving three and seven maximizers respectively. At $n=1$ the only image target is zero and its fibre is three.

For $a,b\ge1$, $F_{a+b-1}=F_aF_b+F_{a-1}F_{b-1}\ge F_aF_b$. Thus a skeleton with $q>0$ satisfies $$\prod_jF_{g_j+1}\le F_{1+\sum_jg_j}=F_{r-2q+1}.$$ If $r$ is even, then $q\ge2$ and this is at most $F_{r-3}<L_r$. Hence only alternating skeletons maximize at even strict length. If $r\ge3$ is odd, then $q$ is odd: at $q=1$ the value is exactly $F_{r-1}$, while at $q\ge3$ it is at most $F_{r-5}<F_{r-1}$. We do not require each individual Fibonacci merge to be strict.

Optimize over $0\le r\le n$, remembering the all-zero value three and the impossible one-sign skeletons. At even $n\ge4$, $L_n$ strictly dominates every smaller strict length. At odd $n\ge5$, $L_{n-1}$ strictly dominates $F_{n-1}$ and every smaller strict length. The asserted targets and small ties follow immediately.

# Exact evidence and limitations

The exact verifier exhausts all sources and targets for $1\le n\le12$, including zero fibres, testing the core, clocks, periods, gap formula and every maximizer. It also reproduces both local certificates, all coefficients of [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}, and the witness junctions. Its frozen transcript records 3,998,247 assertions and is replayed byte for byte. These finite checks supplement the all-length local and matrix proofs.

    $n$   image size   recurrent states   maximal tail   maximal fibre
  ----- ------------ ------------------ -------------- ---------------
      1            1                  1              1               3
      2            3                  3              1               3
      3           13                 13              1               3
     10       15,123              2,093              9             123
     11       39,601              4,533              9             123
     12      103,681              9,621             11             322

No all-time inverse atlas is claimed. Source checking is bounded; missing P51--P56 manuscripts prevent a complete historical reread. Independent paper reviews and ownership are separate gates. The note remains `OWNER_AMBER / HOLD_EXTERNAL`, not cleared for public circulation.
