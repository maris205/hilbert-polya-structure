# Exact Mathematical Results and Controls

本文件区分新推导、来源定理和数值 sanity check。所有 \(p\) 均指 rational prime；“primitive geodesic”不写成“prime geodesic”。

## Theorem 1 — modular norm irrationality

令 \(\gamma\in\mathrm{PSL}_2(\mathbb Z)\) 为双曲元素，\(t=|\operatorname{tr}\gamma|\ge3\)，扩张特征值

\[
\lambda=\frac{t+\sqrt{t^2-4}}2>1.
\]

对应单位速闭测地线的长度和 norm 为

\[
\ell_\gamma=2\log\lambda,
\qquad N_\gamma=e^{\ell_\gamma}=\lambda^2.
\]

由 \(\lambda+\lambda^{-1}=t\)，

\[
N_\gamma+N_\gamma^{-1}=t^2-2,
\]

所以 \(N_\gamma\) 的非平凡 Galois 共轭是 \(N_\gamma^{-1}\)。若存在 \(r\ge1\) 使 \(N_\gamma^r\in\mathbb Q\)，则有理数在共轭下不变，故

\[
N_\gamma^r=N_\gamma^{-r},
\]

与 \(N_\gamma>1\) 矛盾。因此对所有 \(r\ge1\)，\(N_\gamma^r\notin\mathbb Q\)。特别地，对任意 rational prime \(p\) 和 \(r,k\ge1\)，

\[
r\ell_\gamma\ne k\log p.
\]

**证据标签：`PROVED`。** 结论只针对冻结的标准模曲面长度时钟，不能外推成所有 arithmetic flow 的 no-go theorem。

## Corollary — disjoint atomic supports

两套正长度支撑

\[
\{r\ell_\gamma:\gamma\text{ primitive},r\ge1\},
\qquad
\{k\log p:p\in\mathbb P,k\ge1\}
\]

完全不相交。因此不存在保持标准时钟的逐原子 Selberg-hyperbolic/Weil-prime-power 识别。

## The near-prime proxy trap

定义轨道的另一个内生整数不变量

\[
q_\gamma=t^2-2=\operatorname{tr}(\gamma^2)=N_\gamma+N_\gamma^{-1}.
\]

则

\[
q_\gamma-N_\gamma=N_\gamma^{-1},\qquad
\log q_\gamma-\ell_\gamma=\log(1+N_\gamma^{-2}).
\]

若 \(q_\gamma\) 偶然为素数，周期误差会按 \(N^{-2}\) 极快变小，形成危险的数值假象。但：

- \(t\) 偶数时 \(q=t^2-2>2\) 是偶合数；
- \(t\) 奇数且 \(q\) 为素数时，\(q\equiv7\pmod8\)；
- \(q\le X\) 要求 \(q+2=t^2\)，候选至多 \(O(\sqrt X)\)，相对 \(\pi(X)\) 覆盖率至多 \(O(\log X/\sqrt X)\to0\)；
- 同一 trace/norm 还可能对应多个闭轨类，产生 class-number multiplicity；
- \(t^2-2\) 是否取无穷多个素数本身是开放问题。

冻结实验扫到 \(t\le5000\)：在 \(p\le24,999,998\) 的 1,565,927 个素数中，仅 639 个满足 \(p=t^2-2\)，比例 \(4.08065\times10^{-4}\)；拟合 \(\log(\log q-\ell)\) 对 \(\log N\) 的斜率为 \(-1.9999589\)，与精确渐近 \(-2\) 一致。这些是 `NUMERICAL_OBSERVATION`，只用于展示假象，不承担 no-go 证明。

## Arithmetic trilemma for trace-based relabellings

1. 使用标准 \(N=e^\ell\)：指数尺度正确，但 \(N\) 从不是有理整数。
2. 令 rational prime label \(p=t\)：整数迹能取素数，但 \(N\sim t^2\)、\(\ell\sim2\log p\)，权重衰减为 \(p^{-r}\) 而非 \(p^{-r/2}\)。
3. 令 \(p=q=t^2-2\)：尺度和数值非常接近，但只覆盖 \(p+2\) 为平方的零密度子集，并留下所有合数 \(q\) 与闭轨重数。

因此任何这三种简单 relabelling 都不能同时满足 rational-prime coverage、正确时钟和正确 repetition amplitude。

## Selberg versus Ruelle versus Weil weights

固定 Fourier convention 后，对一个 primitive oriented hyperbolic conjugacy class，第 \(r\) 次重复的局部 Selberg 系数为

\[
A^{\rm Sel}_{\gamma,r}
=\frac{\ell_\gamma}{2\sinh(r\ell_\gamma/2)}
=\frac{(\log N_\gamma)N_\gamma^{-r/2}}{1-N_\gamma^{-r}}.
\]

本项目账本保留 \(\gamma\) 与 \(\gamma^{-1}\) 两个 oriented classes；若两者在群内共轭则只出现一个 self-reverse class。16-block 截断得到 8,798 个 oriented classes，对逆向取商后为 4,517 个几何类，其中 236 个 self-reverse，满足 \(8798=2\times4517-236\)。所有 trace multiplicity 仅是该 block cutoff 内的下界，不是完整 class-number multiplicity。

其横向 Poincaré multipliers 为 \(e^{\pm r\ell_\gamma}\)，故

\[
\sqrt{|\det(I-\mathcal P_\gamma^r)|}=2\sinh(r\ell_\gamma/2).
\]

Weil prime-power 核心权重是 \((\log p)p^{-r/2}\)。差异不只来自 \(N\ne p\)，还含 exact stability factor \((1-N^{-r})^{-1}\)。对于 direct-product conventions，

\[
R_\Gamma(s)=\frac{Z_\Gamma(s)}{Z_\Gamma(s+1)}
\]

的 log derivative 消掉该分母，留下 \((\log N)N^{-rs}\)。这是可保留到 Stage 2 的正面线索，但不修复支撑不相交、重数或 self-adjoint host。

## Constant-roof suspension obstruction

若映射 primitive cycle 的离散周期为 \(n\)，constant-roof \(\tau>0\) 的 suspension period 为 \(T=n\tau\)。假设两个不同素数 \(p\ne q\) 分别满足

\[
n_p\tau=\log p,\qquad n_q\tau=\log q,
\]

则 \(p^{n_q}=q^{n_p}\)，违背唯一分解。因此固定 constant roof 至多偶然精确命中一个 rational-prime logarithm，不可能承载全部 prime-period dictionary。该结论对 Hénon、cat map 或任意离散系统的 constant-roof suspension 都成立。
