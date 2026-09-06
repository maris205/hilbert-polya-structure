# C404–C408 round2 / wild dynamics scout

2026-09-06。状态：`ONE_PROVED_WEIGHTED_CANDIDATE_PENDING_NONAUTHOR_REVIEW`。
正式论文录取数仍为 0；本研究者不分配 C 号、不编译新 PDF、不改写旧轮目录。

本轮的实质进展不是继续拟合普通周期点数：已对一个整族证明有局部交数
所有者的首返加权全周期公式；同时给出真正本原周期上的额外重数反例，
明确显示该公式何时不能读作普通计数。完整论证在 `PROOF_PACKAGE.md`。

## 1. 候选与判断

| 分支 | 对象、观测量 | 已闭合内容 | 当前判断 |
|---|---|---|---|
| A | f_{a,b}=x+a x^p+b x^{p+1}, b≠0；普通几何周期点 | 完整幂共轭参数曲线 a^p=b^{p−1}；a,b≠0 时原点全期重数由现有定理确定 | 幂曲线排除；曲线外仅有局部推论，不作为独立论文 |
| B | f=xH(x)^p, H(0)=1；非零本原周期首返局部交长/p 为权 | 全参数、全周期局部倍增、显式加权 W_n、Euler product、超越与非 holonomic 性、log derivative 的单位圆亚纯自然边界 | 数学证明闭合，来源和论文级独立性待非作者审查；尚未正式录取 |
| C | g=x+x^{2p}, p odd；普通周期点 | 非动态仿射排除；所有有限乘子 1；最低第二 residue 为 0，故 B 的强制倍增机制失效 | 无全期普通计数证明；明确停止，不凭小例录取 |

A 的 a=0 切片与 B 的线性 H 切片相交；它们不计作两项独立成果。
B 的普通计数问题与加权结果也不拆成两篇。C 是保留 dx 的机制，B 是保留
dx/x 的机制，二者的局部重数增长确实不同。

## 2. A：先做完整幂映射归属排除

设 k 代数闭、char k=p、b≠0。令 r^p=−1/b，则 f'_{a,b}=1+b x^p
只在 r 处为零。直接展开（没有对非线性复合使用二项式）得

    f(r+u)−r = b u^{p+1}+(a+br)u^p+r^p(a+br).

有限临界点 r 固定当且仅当 a+br=0，亦即 a^p=b^{p−1}。此时平移到 r
后映射为 b u^{p+1}，再取尺度 s 满足 b s^p=1，就共轭到 u↦u^{p+1}。
反过来，幂映射 u^{p+1} 的两个临界点都固定、局部度都为 p+1；曲线外
有限临界点 r 的局部度恰为 p，因而不可能 Möbius 共轭到正或负幂映射。
这给出全参数曲线，不仅排除 a=b=1 的单例。

特别地 x+x^p+x^{p+1}=(x+1)^{p+1}−1 是幂映射的平移伪装。其 ordinary
zeta 性质属于 Bridy 的既有幂映射结果，不能重新包装为非群新论文。

若 p odd 且 a,b 都非零，原点首返阶为 p，且

    index_0(f)=−b^{p−1}/a^p,
    resit_0(f)=b^{p−1}/a^p≠0.

由 Nordqvist–Rivera-Letelier Theorem 2 直接得
ord_0(f^n−id)=p^{v_p(n)+1}。这只是现成局部定理的明确特化；曲线外其他
周期点的首返重数未由此决定，因此不得写出 d^n 减去原点修正就等于
ordinary N_n 的结论。这里没有声称 a^p≠b^{p−1} 已排除所有其他群商。

## 3. B：本轮提出的完整加权结果

设 k 代数闭、p odd，H∈k[x] 非常数且 H(0)=1；记 d=p deg H+1、
m0=ord_0(H−1)。对非零周期点 a，令 l(a) 是其最小正周期，定义

    w(a)=length O_{Fix(f^{l(a)}),a}/p.

局部环长度不依赖局部坐标，f 沿该周期是 étale，故 w 在周期上恒定。
该权是本原首返的交数除去一个强制 p；它不是对每个 n 任意重新选的权。
观察量、时钟及对象均已固定：

    W_n=Σ_{a≠0, f^n(a)=a} w(a).

完整证明所得公式为

    W_n=(d^n−1)/p
         −(p−1)/p Σ_{j=1}^{v_p(n)}(d^{n/p^j}−1)−m0.

非零本原周期上可允许任何 w≥1。源定理应用后的关键局部结论是

    ord_a(f^n−id)=p w(a) p^{v_p(n/l(a))}  whenever l(a)|n.

再将总固定点交长 d^n 在所有首返周期上分解，作 p-primary 的三角反演，
得到上述 W_n。这不是由有限数据猜得的线性递推。

源理论在此有清楚的所有权边界：小重数用 NR2020 Theorem 2，大重数用
Nordqvist2021 Theorem A，原点用 Sen 的 p|i0 恒等式。本轮的计算是
dx/x 强制最低第二 residue 为 −(ac)^{−p}≠0，随后的全局反演与显式
加权生成函数。不能把这描述成我们首次证明一般 wild ramification。

加权 zeta 是对非零本原周期的整数幂 Euler product。其 log derivative
在 |t|<1 中所有 d^{−1/p^j} μ_{p^j} 上有不可消去的极点；zeta 本身对应
的局部分支指数为 (p−1)/p^{j+1}，因此超越且不满足有理系数线性 ODE。
单位圆是 log derivative 的亚纯自然边界，不是说原 zeta 在 |t|<1
全域单值全纯。其初始 Taylor 半径为 1/d。

整族包含非动态仿射映射：H=1+x、任意奇 p 时 f=x+x^{p+1} 的 degree
排除 Ga，临界局部度排除幂映射，临界点数排除 Chebyshev，总不变的
∞ 排除 separable Lattès。四类排除的完整细节在证明包 §6。
不声称所有 H 都非动态仿射。p=2 的 x+x³ 正是 D3，应明确排除。

## 4. 普通计数与加权计数的决定性区分

p=3、H=1+x+x² 时 f=x+x⁴+x⁷。证明包给出的完整因式分解为

    f²−x=x⁴(x²+2x+2)^6 Q_11(x)^3,
    gcd(x²+2x+2,f−x)=1.

所以恰有两个真正二周期点的首返权为 2。对 f² 的非零固定点，

    ordinary count =13,     first-return weighted count W_2=15.

这不是 fixed 点额外重数的重复计入：该二次因子的根在 f 下不固定。
所有非零固定点自身的首返权在这个例子中都是 1。

H=1+x 的 bounded probes（初始探索 p=3,n≤9；p=5,n≤6；p=7,n≤5）
没有发现 w>1，但这不证明所有 n 都无额外首返重数。该分支的普通
Artin–Mazur zeta 仍未由本轮证明包决定。

## 5. C：常导数非加性映射的不同障碍

取 p odd，g=x+x^{2p}。g'=1，所以 g 保留 dx，所有有限周期乘子都是
1。这种常导数等谱机制已见于 Levy Example 1.4，不作为新贡献。
g 本身不是 Ga 动态仿射映射，因为 degree 2p 不是 p 的幂。它是
separable，而 degree 2p 的幂及 Chebyshev 映射在特征 p 下都是
inseparable。它也不能是 separable Lattès 多项式：同证明包 §6 的
总不变点反像增长论证排除（此时 lift 的 separability 由 quotient
的 separability 与 f∘pi=pi∘psi 推出，而非由 degree 与 p 互素推出）。

在原点 q=i0=2p−1，最低第二 residue 为

    Res u^p/(u−g(u))=Res(−u^{−p})=0.

因此 Nordqvist 的 generic minimal-growth 条件明确不成立。它没有
B 中来自 1/(a+u) 的关键非零 residue。新做的精确小检查如下：

| p | n | 原点 mult(g^n−id) | 固定方程 squarefree-degree / multiplicity |
|---|---|---|---|
| 3 | 1 | 6 | (1,6) |
| 3 | 2 | 6 | (1,6),(10,3) |
| 3 | 3 | 36 | (1,36),(60,3) |
| 5 | 1 | 10 | (1,10) |
| 5 | 2 | 10 | (1,10),(18,5) |
| 5 | 5 | 1000 | (1,1000),(19800,5) |

这些数据仅反驳将 B 的倍率照搬到 C；不外推 36、1000 的闭式规律。
g=x+x^{2p} 非线性尾项不是加性算子，不能写 g^p=id+(x^{2p})^p 的
算子二项式。C 没有全周期计数证明，当前不保留为论文合同。

## 6. 检查证据与下一道门槛

`exact_probe.py` 是精确 F_p 多项式程序，不枚举固定有限域的点。
`EXACT_RESULTS.json` 保存 5 个 H 案例、19 个 n 的输出：每个固定方程都
从 squarefree 分解重建，gcd 去掉较短周期因子，再按首返交长独立累加
权，并检查所有已有本原因子的后继重数。所有断言通过，退出码 0。
这些 bounded checks 支持实现无误，不承担全期证明职责。

科学门槛尚未自动通过。B 虽有完整数学证明和非群对象，但局部定理到
全局权重的推论相当短，可能只够一则有用 corollary。需要非作者审查
它是否已有直接来源归属、observable 是否足够自然、与现有 tame-zeta
框架是否只是换记号。未完成该门槛前，保留正式计数为 0，而不是用
“全期”二字自动计入一篇。没有将 A/B/C 拆成多篇的计划。

`NO_BAD_EULER_OR_ROOT_NUMBER` 保持：本轮的 Euler product 仅对本原
动力周期。未建立算术坏素数局部因子、函数方程符号、目标零点对应。
不进行 Route-A evaluator，不上传第三方模型、不调用付费 API/GPU。
只写本 owned lane；不修改 sealed 第一轮、不进行 Git 写入/提交。
