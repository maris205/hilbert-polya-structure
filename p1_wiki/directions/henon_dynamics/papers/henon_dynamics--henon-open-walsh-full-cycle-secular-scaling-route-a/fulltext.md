---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-walsh-full-cycle-secular-scaling-route-a"
canonical_tex: "henon_dynamics/henon_open_walsh_full_cycle_secular_scaling_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_walsh_full_cycle_secular_scaling_route_a/paper/main.pdf"
source_sha256: "a2dd18153826e99bd6e9e820bb6e0dcdcfa3e9fb67fae98f2ecec0b3abc0222a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Full-Cycle Secular Scaling for an Open Walsh Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_walsh_full_cycle_secular_scaling_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_walsh_full_cycle_secular_scaling_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_walsh_full_cycle_secular_scaling_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_walsh_full_cycle_secular_scaling_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Open symbolic propagators often expose a natural cycle time, but finite tables alone do not identify their all-length secular law. We analyze the frozen three-symbol open Walsh shift with one deleted symbol and ask what happens exactly after one complete register cycle. The cycle identity turns the $k$-step propagator into the tensor power $A^{\otimes k}$. From the two nonzero one-site eigenvalues we derive the complete secular factorization, its degree $2^k$, and zero generalized-eigenspace dimension $3^k-2^k$. Sampling a surviving eigenvalue with algebraic-multiplicity weight makes its normalized log modulus an affine image of a fair binomial variable. Consequently its mean is $-\log(3)/4$, its variance is $\sigma^2/k$, it obeys a Hoeffding bound, converges weakly to a point mass, and has a Gaussian central-limit fluctuation. Exact field, Kronecker, and binomial ledgers provide finite implementation receipts rather than the all-$k$ proof. Closed, projector-order, and moved-hole controls separate rank, mean, and spectral spread. The conclusions concern only the source-side subunitary scattering model; they do not supply a phase limit, self-adjoint limit, or target-spectrum construction.
author:
- 'Route-A structural certificate C158'
title: 'Full-Cycle Secular Scaling for an Open Walsh Gate'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** open quantum maps; tensor-product spectra; secular determinant; binomial concentration; central limit theorem; subunitary scattering.

chinese-simplified

中文摘要

开放符号传播子在一个寄存器循环之后会显露怎样的长期谱尺度，是仅靠小尺寸数值表无法回答的问题。 本文固定一个删除单符号的三进制 [Walsh]{lang="en"} 门，直接追踪完整循环中的张量因子。 循环移位保证每个因子恰好通过单点门一次，因此 $k$ 步传播子严格等于该门的 $k$ 重张量积。 由两个非零单点特征值可同时得到 [secular]{lang="en"} 行列式的全部因子、二项式代数重数、 次数 $2^k$，以及零广义特征空间维数 $3^k-2^k$。若按代数重数均匀选取存活特征值， 并考察单位长度对数模，则所得经验律是公平二项变量的仿射像：中心恒为 $-\log(3)/4$， 方差以 $1/k$ 衰减，同时满足 [Hoeffding]{lang="en"} 指数集中和高斯中心极限定理。 包内的代数域、[Kronecker]{lang="en"} 与二项式台账只验证有限实现； 任意 $k$ 的结论来自张量恒等式。闭门、投影次序和移动孔洞三个对照进一步表明， 秩与均值不能单独决定谱展宽。本文只刻画源端次幺正散射动力学， 不讨论相位极限、自伴实现或目标谱匹配。

关键词：开放量子映射；张量积谱；[secular]{lang="en"} 行列式； 二项集中；中心极限定理；次幺正散射。

# Full-cycle factorization

Let $F_3$ be the normalized three-point DFT, $P=\operatorname{diag}(1,0,1)$, and $A=F_3^*P$. On $({\mathbb C}^3)^{\otimes k}$ define $$B_k(v_0,\ldots,v_{k-1})=(v_1,\ldots,v_{k-1},Av_0).$$ One application is one tick. After exactly $k$ ticks, every original factor has passed through $A$ once and returned to its position, hence $$C_k:=B_k^k=A^{\otimes k}.                          \tag{1}$$ The one-site characteristic polynomial is $$\chi_A(\lambda)=\lambda(\lambda^2-\tau\lambda+q),\quad
\tau=\frac{\sqrt3}{6}-\frac i2,\quad
q=-\frac12-\frac{\sqrt3}{6}i.$$ Its discriminant is $11/6+\sqrt3 i/2$, so the roots $0,\lambda_+,\lambda_-$ are distinct. Label the nonzero roots by $|\lambda_+|>|\lambda_-|$. Tensoring a diagonalization and counting binary words gives $$E_k(z):=\det(I-zC_k)=\prod_{j=0}^k
 (1-z\lambda_+^j\lambda_-^{k-j})^{\binom{k}{j}}. \tag{2}$$ Thus $\deg E_k=2^k$, and the zero generalized eigenspace has dimension $3^k-2^k$. If two displayed products coincide, their binomial algebraic multiplicities are retained and added; no distinct-value quotient is taken.

# Surviving log-modulus scaling

Choose a nonzero eigenvalue $\rho$ with algebraic-multiplicity weight and fix the convention $$X_k=k^{-1}\log|\rho|.$$ We do not replace this by an inverse secular-zero radius or by a phase. Formula (2) makes $$X_k=\frac{J_k a+(k-J_k)b}{k},\qquad
J_k\sim\operatorname{Bin}(k,1/2),$$ where $a=\log|\lambda_+|$ and $b=\log|\lambda_-|$. Since $|\lambda_+\lambda_-|=|q|=3^{-1/2}$, $${\mathbb E}X_k=\mu=-\frac{\log3}{4},\qquad
\operatorname{Var}(X_k)=\frac{\sigma^2}{k},\quad
\sigma^2=\frac14\log^2\!\frac{|\lambda_+|}{|\lambda_-|}. \tag{3}$$ The Bernoulli concentration estimate gives, for $\epsilon>0$, $$\Pr(|X_k-\mu|\geq\epsilon)
 \leq2\exp\!\left(-\frac{k\epsilon^2}{2\sigma^2}\right). \tag{4}$$ Therefore the empirical measures converge weakly to $\delta_\mu$. For the fluctuation law, let $Y_\ell$ be independent fair signs. Then $\sqrt{k}(X_k-\mu)=(a-b)(2\sqrt{k})^{-1}\sum_{\ell=1}^kY_\ell$, whose characteristic function is $\cos(t(a-b)/(2\sqrt{k}))^k\to e^{-\sigma^2t^2/2}$. Hence $$\sqrt{k}(X_k-\mu)\Longrightarrow N(0,\sigma^2).   \tag{5}$$

The moduli are genuinely unequal. Writing $p_\pm=|\lambda_\pm|^2$, direct algebra gives $$p_++p_-=\frac{1+\sqrt{37}}6,\quad p_+p_-=\frac13,\quad
(p_+-p_-)^2=\frac{\sqrt{37}-5}{18}>0.$$

# Exact receipts and boundary

Exact $\mathbb Q(\sqrt3,i)$ Newton coefficients are frozen through $k=5$, direct Kronecker receipts through $k=3$, and binomial moments through $k=24$. The independent checker, SymPy path, replay, and hostile mutations reconstruct these finite sentinels; the all-$k$ theorem comes from (1)--(5). The dimension ledger begins $$\begin{array}{c|rrrrr}
k&1&2&3&4&5\\ \hline
3^k&3&9&27&81&243\\
\deg E_k=2^k&2&4&8&16&32\\
\dim G_0(C_k)&1&5&19&65&211
\end{array}$$ For the event $|X_k-\mu|\geq|\log(|\lambda_+|/|\lambda_-|)|/4$, exact binomial tail numerators over $2^k$ are $$\begin{array}{c|rrrr}
k&8&16&32&64\\ \hline
\text{tail numerator}&74&5034&30066346&1426500901314218
\end{array}$$ and each is below the corresponding $2e^{-k/8}$ bound. These tables test coefficient, multiplicity, and concentration implementations separately from the all-parameter proofs.

Three controls separate the conclusion. For $P=I_3$, the closed parent is unitary, the degree is $3^k$, and the log-modulus law is $\delta_0$. Moving the projector to the other side gives $A_{\rm right}=F_3AF_3^*$, hence exact isospectrality. Moving the hole to $P_0=\operatorname{diag}(0,1,1)$ gives nonzero roots $-i$ and $-1/\sqrt3$. Rank, degree, and the mean $-\log(3)/4$ remain unchanged, but the variance coefficient becomes $(\log3)^2/16$, different from (3). Thus rank and mean do not determine spectral spread.

# Scope and limitations

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_UNITARY\_OR\_SCATTERING\_CANDIDATE})$. We claim no phase, inverse-secular-zero, self-adjoint, or antiunitary limit; no target divisor, functional equation or counting law; arithmetic/local factor, Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data availability.** The package contains all finite evidence in `results/`, including `c158_full_cycle_evidence.json`, and the producer and validation scripts in `code/`. No external dataset was used.

**Ethics.** This algebraic study involves no human participants, animals, interventions, or sensitive personal data.

**Author contributions (CRediT).** This is an anonymous technical certificate, and individual authorship is not assigned. Package provenance records Conceptualization, Formal analysis, Software, Validation, Writing -- original draft, and Writing -- review and editing as workflow roles rather than personal attributions.

**Conflict of interest.** No conflict of interest is known.

**Funding.** No external funding was reported for this certificate.

**AI-use disclosure.** An AI coding assistant supported mathematical drafting, code generation, and consistency review. The package scripts reproduce every finite receipt. The assistant was not an external reviewer, and this disclosure does not claim external peer review.
