# Round 1 Review

- 问题忠实：9
- 方法：8
- 贡献：当前 4 / 强化后 7
- 可证性：9
- 验证：8
- 总体：7.5
- Verdict：REVISE

结论：这个 obstruction 的核心判断是对的，但按目前表述只能算一个很好的“错误路线终止引理”，不能单独撑起论文。最大的问题不是公式错误，而是 \(g^k\) 并不是同一 open channel 的第 \(k\) 次重复；若据此声称“\(c\) 不能进入任何动力系统”，会被反例式地反驳。真正有价值的升级是：

> parabolic double-coset clock 不能成为精确的 closed-orbit homogeneous clock；但其稳定齐次化恰好等于 Selberg 闭轨长度。

这比单纯说“不满足 repetition”更强，也更准确。

## 1. 哪些部分成立

设

\[
P=\Gamma_\infty,\qquad
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in \mathrm{PSL}_2(\mathbb Z).
\]

固定 \(c>0\) 后，\(PgP\) 还由 \(d\bmod c\)、\((c,d)=1\) 参数化，因此有 \(\varphi(c)\) 个有向 double cosets，给出

\[
\sum_{c\ge 1}\frac{\varphi(c)}{c^{2s}}
=\frac{\zeta(2s-1)}{\zeta(2s)}.
\]

所以 \(c\) 确实是 parabolic double-coset／有向 cusp channel 参数，而不是 hyperbolic conjugacy-class 参数。无向 scattering geodesics 还会有反向识别，计数不一定恰为 \(\varphi(c)\)。

对 hyperbolic \(g\)，取 \(\operatorname{tr}g=t>2\) 的 lift，则 Cayley–Hamilton 给出

\[
c(g^n)=c(g)\,U_{n-1}(t/2).
\]

而 \(c\) 不共轭不变也有最小显式例子：

\[
g=\begin{pmatrix}2&1\\3&2\end{pmatrix},
\qquad |c(g)|=3,
\]

但用 \(S\) 共轭后 lower-left entry 的绝对值为 \(1\)。因此 \(2\log|c(g)|\) 不能直接定义 hyperbolic conjugacy class 上的闭轨长度。

## 2. 必须修正的三个漏洞

### 漏洞一：\(g^n\) 不是 open channel 的“重复”

\(PgP\) 是 cusp-to-cusp scattering arc。double-coset 空间没有一个与群乘法兼容的、单值的 primitive/power 结构；一般不能把

\[
Pg^nP
\]

解释为将 open channel \(PgP\) 串联 \(n\) 次。

因此 \(c(g^n)\neq c(g)^n\) 首先说明“把 open double coset 强塞进 closed repetition monoid”是类型错误，而不是 open clock 本身有矛盾。

### 漏洞二：roof 本身不需要共轭不变

符号动力学中的局部 roof \(r(x)\) 可以依赖截面和 coding。必须共轭不变的是周期和

\[
r_n(x)=\sum_{j=0}^{n-1}r(T^jx),
\]

而不是每个局部项。因此“\(c(g)\) 不共轭不变”只能排除

\[
\ell_{\rm orbit}([g])=2\log|c(g)|
\]

这种直接定义，不能排除用 endpoint、projective state 或 matrix cocycle 把 denominator growth 编入更大的动力系统。

### 漏洞三：两个 clock 在稳定极限中会合

若

\[
\lambda=\frac{t+\sqrt{t^2-4}}2,\qquad
\ell(g)=2\log\lambda,
\]

则有精确公式

\[
\begin{aligned}
2\log|c(g^n)|
={}&n\ell(g)
+2\log\frac{|c(g)|}{\sqrt{t^2-4}}\\
&+2\log\bigl(1-\lambda^{-2n}\bigr).
\end{aligned}
\]

所以

\[
\boxed{
\lim_{n\to\infty}\frac{2\log|c(g^n)|}{n}
=\ell(g)
}.
\]

这意味着 open clock 不是与 closed clock 完全无关；它是带有 conjugacy-和 cusp-gauge-dependent \(O(1)\) 缺陷的非齐次版本，其稳定齐次化正是 Selberg length。

此外，几何 scattering sojourn time 还依赖 horocycle truncation。模曲面的精确形式通常是

\[
\tau_Y(g)=2\log(|c(g)|Y),
\]

或等价规范，因此 \(2\log|c|\) 应称为 renormalized sojourn time，而不是绝对规范长度。

## 3. 文献碰撞很强

这个 open 几何解释本身已经是成熟的 scattering-geodesic 理论：

- Guillemin 已将非紧双曲曲面上 cusp-to-cusp scattering geodesics 的 sojourn times 与 scattering matrix 的高频结构联系起来。[Guillemin](https://ems.press/journals/prims/articles/3998)
- Ji–Zworski 将其推广到 \(\mathbb Q\)-rank one 局部对称空间，并把 scattering matrix Fourier 变换的奇性与 sojourn times 对应起来。[Ji–Zworski](https://doi.org/10.1016/S0012-9593(01)01065-5)
- 更直接的是 2025 年 Pujahari–Satpathy 已在模曲面上按有理端点／denominator \(q\) 分类 scattering geodesics，给出 sojourn time \(2\log(qT_0)\) 并研究其计数。[Pujahari–Satpathy](https://arxiv.org/abs/2505.04973)

因此，“\(c\) 是 open-channel clock，而 eigenvalue 是 closed-orbit clock”作为事实陈述，novelty 很低。审稿人很可能把它视为 Guillemin scattering geodesics 与标准 Selberg closed geodesics 的直接并置。

## 4. 一个更强、可精确证明的 scoped theorem

建议命名为：

**Denominator-clock non-homogenization and stable closure theorem**

其 modular 版本可包含四部分。

### A. Double-coset 与 conjugacy 的不兼容

\[
\tau_P(PgP)=2\log|c(g)|
\]

在 \(P\backslash\Gamma/P\) 上良定义，但不下降到 hyperbolic conjugacy classes。

### B. denominator-only repetition no-go

可以证明一个比指定 \(2\log c\) 强得多的结论：

> 若 \(F:\mathbb N\to\mathbb R\) 满足
> \[
> F(|c(g^n)|)=nF(|c(g)|)
> \]
> 对所有 hyperbolic \(g\in\mathrm{SL}_2(\mathbb Z)\) 和所有 \(n\ge1\) 成立，则 \(F\equiv0\)。

证明很短但完全刚性。取

\[
A_m=\begin{pmatrix}m&-1\\1&0\end{pmatrix},\qquad m\ge3.
\]

由平方公式得

\[
F(m)=2F(1).
\]

又对 \(m=3\) 取三次方，\(c(A_3^3)=8\)，于是

\[
F(8)=3F(1),
\]

而平方关系已给 \(F(8)=2F(1)\)，故 \(F(1)=0\)，从而 \(F(m)=0\) 对所有 \(m\ge3\)。

再取

\[
B_k=\begin{pmatrix}1&1\\k&k+1\end{pmatrix}.
\]

其 \(c(B_k)=k\)，而

\[
c(B_k^2)=k(k+2)\ge3.
\]

所以

\[
0=F(k(k+2))=2F(k),
\]

得到所有 \(k\ge1\) 上 \(F(k)=0\)。

这准确地排除了“任何只看 denominator 的非平凡 exact closed clock”，而不仅是排除 \(2\log c\)。

### C. 稳定齐次化刚性

上述精确 Chebyshev 公式给出

\[
\overline{\tau}_P(g)
:=\lim_{n\to\infty}\frac{\tau_P(g^n)}n
=\ell(g).
\]

进一步，若 \(L\) 是 power-homogeneous，并满足

\[
L(g^n)-\tau_P(g^n)=o(n),
\]

则必有

\[
L(g)=\ell(g).
\]

换言之，在“只允许次线性修正”的条件下，唯一可能的 closed homogenization 就是 Selberg translation length。

### D. Euler-product corollary

由此可以得到一个明确限制：

> 不存在以 \(c(g)^2\) 为 local norm、同时以 primitive hyperbolic conjugacy classes 为 primitives，并满足标准 repetition law 的非平凡 Euler product。

任何成功构造必须二选一：

- 保留 \(P\backslash\Gamma/P\) 的 open scattering/groupoid 类型，此时得到 Dirichlet/scattering series，而非闭轨 Euler product；
- 做稳定齐次化，此时 clock 自动变为 \(\ell(g)\)，回到 Selberg/Mayer。

这个结论应明确限定为 denominator-only、exact repetition、hyperbolic-conjugacy Euler product；不要声称排除 matrix cocycles、subadditive pressures 或带 boundary state 的 open transfer operators。

## 5. 怎样才接近论文级

单独 modular lemma 只有短注价值。要升格，至少再做以下两项中的一项：

1. 推广到任意有限面积 Fuchsian surface及多 cusp：

   \[
   \tau_{ij}:P_i\backslash\Gamma/P_j\to\mathbb R
   \]

   是带入口／出口 cusp 标签、且随 horosphere 选择发生 gauge shift 的 open clock；证明其任何次线性 homogeneous closure 都是 marked closed length。

2. 与 two-cusp finite-memory collapse 合并：

   - open channels 本身没有 primitive power monoid；
   - 有限状态记忆若将它们闭合成周期系统，只产生 finite-dimensional twisted Selberg；
   - 保留完整 open chronology 则应属于 scattering groupoid，而不是 Selberg Euler product。

第二种组合最契合 HCS-C17，因为它把“clock 类型错误”和“有限记忆无法修复类型错误”连成一个统一 no-go theorem。

## 6. 与 two-cusp memory-collapse 的取舍

我的判断是：

| 方向 | 数学可靠性 | 新颖性 | 独立成文潜力 |
|---|---:|---:|---:|
| modular open–closed obstruction，当前版 | 高 | 低，约 2–3/10 | 低 |
| 加 denominator-only no-go 与稳定齐次化 | 很高 | 中低，约 4/10 | 可作强 section／短注 |
| two-cusp memory-collapse | 中高 | 中，约 5/10 | 更高，但需越过 twisted Selberg 既有理论 |
| 二者合并成有限记忆 open-to-closed no-go | 中高 | 最高，约 6/10 | 本轮最值得 |

所以本轮不建议把 modular obstruction 单独当主候选。最合理的是：先把上面的 B、C 两个定理快速写成严格 kill gate，再把它嵌入 two-cusp memory-collapse。若只能选一个主项目，选 two-cusp；若追求最快得到一个完全正确的负面结果，则先完成 modular no-go，但应把它定位为支撑定理而非旗舰贡献。未修改文件。
