---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--196-cyclic-godel-implication"
canonical_tex: "symbolic_dynamics/papers/196-cyclic-godel-implication/main.tex"
canonical_pdf: "symbolic_dynamics/papers/196-cyclic-godel-implication/main.pdf"
source_sha256: "06cb66f5c784fe7521d4fe7a5777b8490e4f73f41ba968167f8ce58dbd54a97e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A One-Step Core, Rotation Spectrum, and Exact Fibres for Cyclic Gödel-Implication Dynamics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/196-cyclic-godel-implication>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/196-cyclic-godel-implication/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/196-cyclic-godel-implication/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/196-cyclic-godel-implication/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/196-cyclic-godel-implication/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $\mathcal A_q=\{0,\ldots,q-1\}$ be a finite chain and apply Gödel implication synchronously around a cyclic word: $T(x)_i=x_i\Rightarrow x_{i+1}$. We solve the resulting finite dynamical system. Its image is exactly the cyclic language in which every nontop letter is preceded by a strictly larger letter, and the restriction of $T$ to this image is the cyclic shift. Thus every tail has length at most one, while all recurrent periods divide the word length. A $q$-state transfer matrix gives every iterate-fixed count and hence the complete cycle census; its characteristic polynomial is $\lambda^q-(\lambda+1)^{q-1}$. The inverse problem is genuinely nonuniform: for every target we give a product of explicit binomial differences indexed by the cyclic gaps between its nontop sites. The all-top fibre has size $q$. Exact exhaustion through $q=5$ and length seven checks the image, clocks, spectra, and every labelled fibre. Classical finite-chain logic and transfer-matrix facts receive no contribution credit, and the bounded owner search leaves the manuscript `HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'A One-Step Core, Rotation Spectrum, and Exact Fibres for Cyclic Gödel-Implication Dynamics'
```

## Markdown 正文

# The map and the subtraction boundary

Fix integers $q\ge2$ and $m\ge1$, put $M=q-1$, and write indices modulo $m$. On the chain $\mathcal A_q=\{0,1,\ldots,M\}$, Gödel implication is $$\label{eq:implication}
 a\Rightarrow b=\begin{cases}M,&a\le b,\\ b,&a>b.\end{cases}$$ The finite self-map studied here is $$\label{eq:update}
 T_{q,m}(x)_i=x_i\Rightarrow x_{i+1}
 \qquad (x\in\mathcal A_q^m).$$ All coordinates in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} are read before the synchronous update.

Finite-chain Gödel logics and the truth function [\[eq:implication\]](#eq:implication){reference-type="eqref" reference="eq:implication"} are classical [@Dummett1959; @Hajek1998]; recent work also enumerates finite-chain implication values over bracketings [@Yildiz2026]. We use only the truth function, not a bracketing model. Transfer matrices, cyclic languages, and Möbius inversion are likewise standard [@LindMarcus1995; @Stanley2011]. Our residual object is the joint finite-dynamical statement for the synchronous cyclic map: its exact image, rotation spectrum, and target-resolved inverse product.

This map is not assigned novelty or priority. Internally, its carrier and rule differ from Rule 184 in P90, odd-run reversal in P117, cyclic equality feedback in P164, and the finite-set/composition maps P187--P191. The architecture "one step into a constrained language, then a shift" is generic and receives zero credit. A bounded exact-phrase and translated search found no literal cyclic Gödel-implication dynamics owner; a non-hit is not evidence of novelty, completeness, or freedom to operate.

# The recurrent language

Let $S$ denote left cyclic shift, $(Sy)_i=y_{i+1}$, and define $$\label{eq:language}
 \mathcal L_{q,m}=\{y\in\mathcal A_q^m:y_{i+1}<M\Longrightarrow y_i>y_{i+1}
 \text{ for every }i\}.$$ Thus each nontop letter has a strictly larger predecessor.

[\[thm:core\]]{#thm:core label="thm:core"} For every $q\ge2$ and $m\ge1$, $$\label{eq:image}
 \operatorname{im}(T_{q,m})=\mathcal L_{q,m},\qquad T_{q,m}|_{\mathcal L_{q,m}}=S.$$ Consequently a state has depth zero exactly when it belongs to $\mathcal L_{q,m}$ and depth one otherwise. Every recurrent period divides $m$. The unique fixed state is $M^m$.

Put $y=T(x)$. If $y_{i+1}<M$, then [\[eq:implication\]](#eq:implication){reference-type="eqref" reference="eq:implication"} gives $y_{i+1}=x_{i+2}$ and $x_{i+1}>x_{i+2}$. If $y_i=M$, then $y_i>y_{i+1}$; otherwise $y_i=x_{i+1}>x_{i+2}=y_{i+1}$. Hence $y\in\mathcal L_{q,m}$.

Conversely, if $y\in\mathcal L_{q,m}$, then a coordinate with $y_{i+1}<M$ satisfies $y_i>y_{i+1}$ and therefore $y_i\Rightarrow y_{i+1}=y_{i+1}$. If $y_{i+1}=M$, the same equality holds because every letter is at most $M$. Thus $T(y)=Sy$. The language is shift invariant, so $y=T(S^{-1}y)$ and every $y\in\mathcal L_{q,m}$ lies in the image. This proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

The shift is a permutation of the core. A periodic point of $T$ must lie in the image, so the depth statement follows. Shift periods divide $m$. Finally $Sy=y$ makes $y$ constant, and a constant word lies in $\mathcal L_{q,m}$ only when its letter is $M$.

The exact transient count is therefore $$\label{eq:transient-count}
 q^m-|\mathcal L_{q,m}|.$$

# Transfer spectrum and cycles

Index rows and columns by $0,\ldots,M$ and let $$\label{eq:matrix}
 A_{a,b}=\mathbf1\{b=M\text{ or }a>b\}.$$ A closed walk of length $m$ in this directed graph is precisely a word in $\mathcal L_{q,m}$.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} For every $r\ge1$, $$\label{eq:fixed-iterates}
 |\operatorname{Fix}(T_{q,m}^r)|=\operatorname{tr}
 \bigl(A^{\gcd(m,r)}\bigr).$$ In particular $|\mathcal L_{q,m}|=\operatorname{tr}(A^m)$. Moreover, $$\label{eq:charpoly}
 \det(\lambda I-A)=\lambda^q-(\lambda+1)^{q-1}.$$ If $d\mid m$, the number of points of least period $d$ and the number of $d$-cycles are respectively $$\label{eq:mobius}
 P_d=\sum_{e\mid d}\mu(d/e)\operatorname{tr}(A^e),
 \qquad C_d=P_d/d.$$

The trace statement for the language is the closed-walk formula. By Theorem [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"}, an iterate-fixed point is a core word fixed by $S^r$, hence the repetition of a closed word of length $\gcd(m,r)$. This proves [\[eq:fixed-iterates\]](#eq:fixed-iterates){reference-type="eqref" reference="eq:fixed-iterates"}. In $\lambda I-A$, subtracting each row from its successor and expanding along the resulting bidiagonal part gives $\lambda^q-(\lambda+1)^{q-1}$; equivalently the same identity follows by induction on $q$ from the last-row expansion. Finally $\operatorname{tr}(A^d)=\sum_{e\mid d}P_e$, and Möbius inversion gives [\[eq:mobius\]](#eq:mobius){reference-type="eqref" reference="eq:mobius"}.

The binomial coefficients in [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"} matter. For example, when $q=3$ the polynomial is $\lambda^3-\lambda^2-2\lambda-1$, not the tribonacci polynomial. Cayley--Hamilton yields the exact recurrence $$\label{eq:trace-recurrence}
 R_j=\sum_{h=0}^{q-1}\binom{q-1}{h}R_{j-q+h}
 \quad(j\ge q),\qquad R_j=\operatorname{tr}(A^j).$$

# Every-target inverse product

The recurrent dynamics is uniform rotation, but the incoming trees are not uniform. Fix $y\in\mathcal L_{q,m}$ other than $M^m$. List its nontop sites in cyclic order as $p_1,\ldots,p_s$, set $$a_j=y_{p_j},\qquad
 d_j=p_{j+1}-p_j\pmod m\in\{1,\ldots,m\},$$ where $p_{s+1}=p_1$. For $a,b<M$ and $d\ge1$, define $$\label{eq:gap-factor}
 G_d(a,b)=\binom{M-a+d-1}{d-1}
 -\mathbf1_{b\ge a}\binom{b-a+d-1}{d-1}.$$

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Every target $y\in\mathcal A_q^m$ has $$\label{eq:fibre}
 |T_{q,m}^{-1}(y)|=
 \begin{cases}
 0,&y\notin\mathcal L_{q,m},\\
 q,&y=M^m,\\
 \displaystyle\prod_{j=1}^sG_{d_j}(a_j,a_{j+1}),
   &y\in\mathcal L_{q,m}\setminus\{M^m\}.
 \end{cases}$$ For every $t\ge1$, fibres of $T^t$ are rotations of the same data: $$\label{eq:t-fibre}
 |(T^t)^{-1}(y)|=|T^{-1}(S^{1-t}y)|
 \quad(y\in\mathcal L_{q,m}).$$

Targets outside the image have empty fibre. If every target coordinate is $M$, the source inequalities are $x_1\le x_2\le\cdots\le x_m\le x_1$; the source is constant, giving $q$ choices.

Now fix consecutive nontop sites $p=p_j$ and $p'=p_{j+1}$ at cyclic gap $d=d_j$. The equation at $p$ fixes $x_{p+1}=a_j$. Every intervening top coordinate imposes a weak inequality, while the equation at $p'$ requires $x_{p'}>a_{j+1}$. Thus the variables along this gap satisfy $$a_j=x_{p+1}\le x_{p+2}\le\cdots\le x_{p'}\le M,
 \qquad x_{p'}>a_{j+1}.$$ There are $\binom{M-a_j+d-1}{d-1}$ weak chains before the last inequality. When $a_{j+1}\ge a_j$, exactly $\binom{a_{j+1}-a_j+d-1}{d-1}$ of them violate it; when $a_{j+1}<a_j$, none do. This is [\[eq:gap-factor\]](#eq:gap-factor){reference-type="eqref" reference="eq:gap-factor"}. Distinct cyclic gaps share only already fixed endpoints, so their choices are independent, proving the product.

On the core, $T^t=S^{t-1}T$. Taking inverse images gives [\[eq:t-fibre\]](#eq:t-fibre){reference-type="eqref" reference="eq:t-fibre"}.

For adjacent nontop sites $d=1$, the factor is one exactly under the strict descent already required by [\[eq:language\]](#eq:language){reference-type="eqref" reference="eq:language"}. Long top gaps instead produce binomially large and target-dependent factors. As a global check, finite-map edge mass and [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} give $$\label{eq:mass}
 \sum_{y\in\mathcal L_{q,m}}|T^{-1}(y)|=q^m.$$

# Exact controls and limitations

The paper-local script enumerates all states for $2\le q\le5$ and $1\le m\le7$. It independently constructs the map and checks image equality, the shift restriction, every labelled fibre, edge mass, all tested iterate-fixed counts, and the recurrence forced by [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}. The transcript is deterministic and hashed. These tests are falsifiers for indexing and boundary errors; the proofs above carry the all-parameter claims.

The result is deliberately narrow. It does not address asynchronous updates, noncyclic boundary conditions, other residuated implications, probabilistic perturbations, entropy limits, or logical expressivity. The transfer matrix and rotation census are standard once the core language is known. The paper's concrete progress is the exact one-step factorization through that core together with the nonuniform target-resolved inverse product. External status remains `HOLD_EXTERNAL`.
