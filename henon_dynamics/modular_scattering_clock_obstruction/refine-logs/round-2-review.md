# Verdict: REVISE — 48/60

审稿结论：**REVISE**。核心数学方向正确，而且很适合做 Route-A 的终止性证书；但当前版本的主 no-go 量词仍偏窄，标题性语言又略强。必须加入“任意 denominator-only \(F\) 的 repetition no-go”和“stable homogenization 恰好等于 Selberg length”，同时严格限定它没有排除 local cocycle、cohomological correction 或同时依赖 trace/word chronology 的构造。

评审对象：[round-0-initial-proposal.md](</root/autodl-tmp/hilbert-polya-structure/henon_dynamics/modular_scattering_clock_obstruction/refine-logs/round-0-initial-proposal.md>)

## 评分

| 维度 | 分数 | 评语 |
|---|---:|---|
| 问题忠实度 | 9/10 | 对经典输入、新意边界、RH 非目标和 source-lock 都交代得很好。 |
| 方法明确性 | 8/10 | 矩阵路线清楚，但“same return dynamics”“periodic roof”的范畴和允许的 normalization 类仍需正式定义。 |
| 贡献质量/新颖性 | 5/10 | 端点与主要恒等式都经典；价值主要是精确兼容性 obstruction，而非新散射或新算子理论。 |
| 可证性 | 9/10 | double coset、Chebyshev、divisor no-go 都可完全严谨证明；风险主要来自过度量化而非证明困难。 |
| 验证聚焦 | 8/10 | exact arithmetic controls 合理；高精度零点图示不是必要证据，且容易分散重点。 |
| Route-A 价值 | 9/10 | 能有效阻断“把经典散射 ζ-ratio 直接包装成周期轨道/Hilbert–Pólya”的错误升级。 |
| **总分** | **48/60** | **强 Route-A obstruction proposal；尚不足以 READY。** |

## 1. Double-coset 公式：基本准确，但需修正表述与归一化

第 69 行的分类是正确的，但正文必须明确采用的 PSL/SL 约定。

令
\[
\Gamma_\infty=\langle T\rangle,\qquad
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
左乘 \(T^m\) 不改变底行，右乘 \(T^n\) 将
\[
(c,d)\longmapsto(c,d+nc).
\]
由 \(ad-bc=1\) 得 \(\gcd(c,d)=1\)。在 PSL 中 \(\gamma\sim-\gamma\)，选择 \(c>0\) 消除符号，于是非恒等 double cosets 与
\[
\{(c,\bar d):c\ge1,\ \bar d\in(\mathbb Z/c\mathbb Z)^\times\}
\]
一一对应。\(c=0\) 是单独的 identity cusp double coset；\(\varphi(1)=1\) 按通常约定处理。

需要修改三点：

- “nontrivial parabolic double cosets”容易被理解成“由 parabolic elements 构成”。建议改成“nonidentity double cosets relative to the parabolic cusp subgroup”或“cusp double cosets in the big Bruhat cell”。
- 必须注明
  \[
  \sum_{c\ge1}\frac{\varphi(c)}{c^{2s}}
  =\frac{\zeta(2s-1)}{\zeta(2s)}
  \]
  初始成立于 \(\Re s>1\)，其余区域依赖解析延拓。
- 这只是散射系数的有限算术部分。完整标准系数是
  \[
  \Phi(s)
  =\sqrt{\pi}\frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
   \frac{\zeta(2s-1)}{\zeta(2s)}
  =\frac{\Lambda(2s-1)}{\Lambda(2s)}.
  \]
  第 15–18 行不应把裸 ζ-ratio 写成完整 scattering coefficient。

因此 double-coset 部分不是错误，但目前略有概念压缩。

## 2. \(c\)-entry 障碍：对 literal denominator 成立，但尚不足够一般

\(|c(\gamma)|\) 不具有完整共轭不变性是正确的。可以给一个很小的 PSL witness：
\[
\gamma=
\begin{pmatrix}1&1\\2&3\end{pmatrix},
\qquad
S^{-1}\gamma S=
\begin{pmatrix}3&-2\\-1&1\end{pmatrix}.
\]
两者在 \(\mathrm{PSL}_2(\mathbb Z)\) 中共轭、trace 都是 \(4\)，但 \(|c|\) 分别为 \(2\) 和 \(1\)。

正 Gauss word 的 cyclic witness 需谨慎：单个 Gauss branch matrix 通常行列式为 \(-1\)，所以长度二 word 的单 digit shift 只直接给出 PGL 共轭。若声称 PSL 共轭，建议使用偶数长度且 shift 偶数个 digits。例如令
\[
A_a=\begin{pmatrix}0&1\\1&a\end{pmatrix}.
\]
则
\[
\gamma=A_1A_1A_1A_2=
\begin{pmatrix}2&5\\3&8\end{pmatrix},
\]
而 two-digit cyclic shift 为
\[
\gamma'=A_1A_2A_1A_1=
\begin{pmatrix}3&5\\4&7\end{pmatrix}.
\]
以
\[
P=A_1A_1=\begin{pmatrix}1&1\\1&2\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z)
\]
有
\[
\gamma'=P^{-1}\gamma P,
\]
但 \(|c(\gamma)|=3\)、\(|c(\gamma')|=4\)。

更重要的逻辑限制是：

> 一个 roof function 本身不必是 monodromy 矩阵某个 entry 的共轭不变量；必须共轭/循环不变的是沿整个周期的 Birkhoff sum。

因此 \(c\)-entry witness 只排除
\[
R(\gamma)=F(|c(\gamma)|)
\]
这类由最终 monodromy denominator 单独定义的 total period。它没有排除：

- 依赖每一步 denominator increment 的 local cocycle；
- cyclic symmetrization；
- cohomologous roof；
- 同时依赖 \(c,t\) 或完整 word chronology 的函数；
- 经过 stable homogenization 后的 class function。

第 94 行已经试图限缩，但第 27 行的“unique standard repair”及若干 headline 仍比实际证明更强。

## 3. Chebyshev/repetition：公式正确；当前结论只覆盖 \(2\log|c|\)

对任意 \(\gamma\in\mathrm{SL}_2\) 和 \(k\ge1\)，
\[
\gamma^k
=U_{k-1}(t/2)\gamma-U_{k-2}(t/2)I,
\qquad t=\operatorname{tr}\gamma,
\]
因此
\[
c(\gamma^k)=c(\gamma)U_{k-1}(t/2).
\]
此处需注明选择 SL lift；若工作在 PSL，则最好固定 \(t>2\) 的 hyperbolic lift，或始终使用绝对值。

第 77 行的 \(k=2,3\) 反证是对的：
\[
c(\gamma^2)=ct,\qquad
c(\gamma^3)=c(t^2-1).
\]
若
\[
2\log|c(\gamma^k)|=k\,2\log|c(\gamma)|
\]
对 \(k=2,3\) 同时成立，则
\[
|t|=|c|,
\qquad
|t^2-1|=|c|^2=t^2,
\]
不可能。

但这只证明 literal choice
\[
F(x)=2\log x
\]
失败。建议升级成真正一般的 denominator-only theorem。

### 必须加入的强化：任意 denominator-only \(F\) 只能平凡

令 \(\alpha>0\) 表示任意 cusp scaling，且
\[
F:\alpha\mathbb N_{>0}\to\mathbb R.
\]
若对所有 hyperbolic \(\gamma\in\mathrm{SL}_2(\mathbb Z)\) 都要求
\[
F(\alpha|c(\gamma^2)|)=2F(\alpha|c(\gamma)|),
\]
那么 \(F\) 在 \(\alpha\mathbb N\) 上必为零。

证明只需正矩阵族
\[
\gamma_{m,n}
=
\begin{pmatrix}
1&m\\
n&1+mn
\end{pmatrix},
\qquad m,n\ge1.
\]
它满足
\[
c(\gamma_{m,n})=n,\qquad
\operatorname{tr}\gamma_{m,n}=2+mn,
\]
从而
\[
c(\gamma_{m,n}^2)=n(2+mn).
\]

取 \(n=1\)，得到
\[
F(\alpha(m+2))=2F(\alpha)
\]
对所有 \(m\ge1\) 成立，因此 \(F(\alpha r)=2F(\alpha)\) 对所有 \(r\ge3\) 成立。再取 \(n=r\ge3,m=1\)，有
\[
F(\alpha r(r+2))=2F(\alpha r).
\]
左侧等于 \(2F(\alpha)\)，右侧等于 \(4F(\alpha)\)，故 \(F(\alpha)=0\)，继而 \(F(\alpha r)=0\) 对 \(r\ge3\)。最后取 \(n=2,m=1\)，由
\[
F(8\alpha)=2F(2\alpha)
\]
得 \(F(2\alpha)=0\)。

这个结果：

- 不需要连续性、单调性或对数形式；
- 只用 \(k=2\)；
- 自动对任意固定 cusp scaling \(\alpha\) 稳定；
- 比当前“\(2\log c\) 在 \(k=2,3\) 失败”显著更有 theorem delta。

它仍然只排除 final-denominator-only \(F\)，这一范围必须在标题和摘要中明确。

## 4. 必须加入：stable homogenization 恰好恢复 Selberg length

这是本 proposal 最漂亮、也最能避免“只是显然”的强化。

对 hyperbolic \(\gamma\)，选择 \(t>2\) 的 lift，并令
\[
\lambda=\frac{t+\sqrt{t^2-4}}2>1.
\]
由
\[
U_{k-1}(t/2)
=\frac{\lambda^k-\lambda^{-k}}{\lambda-\lambda^{-1}},
\]
得到
\[
\begin{aligned}
\lim_{k\to\infty}\frac{2}{k}\log|c(\gamma^k)|
&=
\lim_{k\to\infty}
\frac{2}{k}
\left(
\log|c(\gamma)|
+\log|U_{k-1}(t/2)|
\right)\\
&=2\log\lambda\\
&=\ell(\gamma).
\end{aligned}
\]

这给出非常精确的正反结论：

- literal denominator height 不具 exact repetition；
- 它的 canonical stable homogenization 存在；
- homogenization 不产生 Riemann scattering clock，而恰好坍缩为 Selberg geodesic length。

这比“contrast with geodesic length”强得多，也真正解释了为什么任何自然的 power-stable repair 回到 Mayer–Selberg 端点。

不过不要称其为“unique repair”。你只证明了**该 denominator height 的 canonical stable homogenization**是 \(\ell\)，没有证明所有可能的 conjugacy-invariant homogeneous repairs 都唯一。PSL\(_2(\mathbb Z)\) 上还存在其他 homogeneous class functions/quasimorphism 现象。

建议把第 27 行改为：

> the literal denominator height is neither cyclically invariant nor power additive, while its canonical stable homogenization is exactly the hyperbolic translation length and hence returns to the Selberg–Mayer clock.

## 5. Zero-free normalization no-go：正确，但必须正式定义允许类

第 82–86 行的基本结论正确。以
\[
\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)
\]
为约定，对每个非平凡零点 \(\rho\)：

- \(\Phi\) 在 \(s=\rho/2\) 有与 \(\rho\) 同重数的极点；
- 分子在该点为 \(\Lambda(\rho-1)\neq0\)，故无 cross-cancellation；
- \(\Phi\) 在 \(s=(1+\rho)/2\) 有相应零点。

若采用整 Riemann xi，
\[
\xi(u)=\tfrac12u(u-1)\Lambda(u),
\]
则应提醒读者
\[
\Phi(s)=\frac{s}{s-1}\frac{\xi(2s-1)}{\xi(2s)}.
\]

一 cusp 坐标缩放 \(y'=r y\)，并重新把 incoming coefficient 归一化为 \(1\) 后，散射系数按约定变为
\[
\Phi_r(s)=r^{2s-1}\Phi(s)
\]
或其逆；无论方向如何，因子都是 zero-free exponential。更一般的零自由 Eisenstein basis normalization 也只引入 zero-free ratio。

因此对 \(a\neq0\)，任何 entire zero-free \(h\) 都不能使
\[
h(s)\Phi(as+b)
\]
成为整个 \(\xi(s)\)，因为非平凡 poles 仍然存在。

必须补充的限定：

- 这是全平面 meromorphic identity 的 no-go，不是局部半平面 identity。
- 明确定义“allowed normalization”：cusp scaling、zero-free scalar renormalization，还是更一般的 \(h(s)/h(1-s)\)。
- 若允许带零的 meromorphic compensator，则当然可以取消 poles；但那正是“插入 compensating zeta divisor”，必须明确排除。
- 要求 \(a\neq0\)。
- elementary poles/factors 与 nontrivial divisor 分开陈述。

此 no-go 非常干净，但本质上是“zero-free 因子不能消极点”，数学上过于直接，只适合作为 supporting corollary，不能承担主要新颖性。

## 6. 是否只是过于显然的经典事实？

以当前版本看，风险真实存在。

经典输入包括：

- cusp double-coset/totient Dirichlet series；
- scattering coefficient 的 completed ζ-ratio；
- \(c(\gamma^k)\) 的 Cayley–Hamilton/Chebyshev 公式；
- hyperbolic translation length 的共轭不变与 power additivity；
- Mayer–Selberg Fredholm identity；
- zero-free factor不改变 divisor。

因此，如果最终结果只写成“\(c\) 不共轭不变、\(2\log c\) 不 power-additive、散射 quotient 不是 \(\xi\)”——这很可能只够做一节清理性说明或内部路线裁决，不足以支撑独立高水平论文。

加入以下组合后，贡献会清晰不少：

1. 精确的 open-double-coset 与 closed-conjugacy category separation；
2. 无正则性假设的 denominator-only \(F\equiv0\) theorem；
3. normalization-stable 版本；
4. stable homogenization \(=\ell_{\rm Selberg}\)；
5. 明确列出 theorem 没有排除的更广路线。

即便如此，贡献定位仍应是“sharp obstruction/synthesis theorem”，而不是新 transfer/scattering theory。它的 **Route-A 价值高于外部论文新颖性**。

## 必须修改项

1. **重写主定理的量词。** 明确对象是 final-monodromy denominator-only total clock \(R(\gamma)=F(\alpha|c(\gamma)|)\)，而非所有 cusp-derived roofs。

2. **加入 universal \(F\) no-go。** 使用 \(\gamma_{m,n}\) 族证明只要满足 square repetition，\(F\) 就在 \(\alpha\mathbb N\) 上恒零。

3. **加入 stable homogenization theorem。**
   \[
   \lim_{k\to\infty}\frac{2}{k}\log|c(\gamma^k)|=\ell(\gamma).
   \]
   把它提升为主结果，而非普通 positive control。

4. **删除或弱化“unique standard repair”。** 改为“canonical stable homogenization”；除非另行证明唯一性。

5. **修正 double-coset 术语和完整 scattering factor。** 写清 PSL sign、\(c=0\) identity coset、\(\Re s>1\) 和 Gamma factor。

6. **Gauss cyclic witness 必须留在 PSL。** 使用四 digit/even shift witness，或明确说明单 digit shift只在 PGL coding 中共轭。

7. **正式定义 allowed normalization。** 给出 cusp coordinate scaling 下 \(\Phi_r(s)\) 的确切变换式，并将 zero-free entire normalization 与禁止的 divisor-carrying compensator区分。

8. **列出未被排除的候选。** 至少包括 local denominator cocycles、cyclic sums、trace-dependent clocks、cohomological corrections 和 non-zero-free compensators。

9. **降低数值图示地位。** 零点高精度 residual 只能是 regression illustration；主证书应是 symbolic identities、exact matrices 和 formal divisor argument。

10. **将新颖性声明改为内部兼容性裁决。** 若目标是独立论文，需要在 literature comparison 中解释为何 universal \(F\) no-go 与 stable homogenization identification 未被既有 Mayer/Series/scattering 文献直接表述。

完成这些修改后，我会倾向于给出 **READY 作为 Route-A obstruction project**；若仍以当前较窄的 \(2\log c\) 反例作为主要 theorem，则应降为内部技术备注，而非完整研究路线。
