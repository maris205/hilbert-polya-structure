# Paper30：正弦环面族两级 Ruelle 共振的证明阶段接收

日期：2026-09-07。状态：`TWO_SCALE_RUELLE_THEOREM_MATHEMATICALLY_CHECKED`。
这里只接收完整数学结论，不授予候选立项、篇幅、稿件或 PDF 验收。
Batch07 仍为 Papers27–29 本地接受，计 3/5；Paper30 未立项，Paper31 未开展。
Route applicability: `NOT_APPLICABLE`。

## 1. 现在实际成立的单一动力谱定理

固定面积保持实解析族
$$
F_\kappa=A\circ S_\kappa,\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)),\qquad t=\pi\kappa.
$$
存在 $\tau_R>0$，对每个实 $0<|t|<\tau_R$，常数面积共振 $1$ 代数简单。
剔除它之后，Ruelle–Pollicott 共振多重集具有以下结构：

**第一谱簇。** 两条简单实共振具有关于 $t$ 的全纯延拓，分别位于频率反号的
偶、奇空间，且
$$
\lambda_{\rm ev}(t)=-t+\frac{11}{12}t^2+O(t^3),\qquad
\lambda_{\rm od}(t)=-t+\frac5{12}t^2+O(t^3).
\tag{1}
$$
实参数时它们为实数，因为矩阵 Taylor 系数为实数，各奇偶块内的简单分支在
复共轭后仍是同一条唯一分支。

**第二谱簇。** 写 $t=s^2$，在这个平方根覆盖上有八条简单分支
$$
\lambda_j(s^2)=s^3\bigl(\nu_j+O(s)\bigr),\qquad 1\le j\le8,
\tag{2}
$$
其中 $\nu_j$ 是四个不同非零数各自的两个平方根：
$$
\left\{
\frac{9+\sqrt{145}}{24},\ \frac{9-\sqrt{145}}{24},\quad
\frac{7+i\sqrt{15}}{24},\ \frac{7-i\sqrt{15}}{24}
\right\}.
\tag{3}
$$
正实 $t$ 可取 $s=\sqrt t$，负实 $t$ 可取 $s=i\sqrt{|t|}$。
换平方根仅重新排列同一个八元谱簇。第二簇本征值不被宣称严格正负成对，
成对的是其首项常数；非实首项也不保证有限参数下精确位于虚轴。

**全部余谱。** 删除上述十条、按代数重数计的共振后，剩余共振的最大模是
$$
o(|t|^{3/2}).
\tag{4}
$$
这控制整个剩余谱，不是有限截断或逐固定谱序号的结论。
因此全部非平凡共振为 $O(|t|)$，非平凡谱半径为 $|t|+O(|t|^2)$。
仍可能有更小的非零共振；没有证明其最优指数、全谱显式公式或有限参数全局结构。

## 2. 合成证明与精确参数交集

### 固定空间的解析核

令 $m=(r,s)$、$a=s$、$b=r+s$，输入状态为 $(a,b)$，输出为 $(b,c)$，
$k=a+c-3b$。参数权 $\omega(m)=|a|-|b|$ 给出固定
$\ell^2(\mathbb Z^2\setminus\{0\})$ 上的核
$$
B(t)_{(b,c),(a,b)}
=t^{|a|-2|b|+|c|-1}[z^k]e^{tb(z-z^{-1})}.
$$
已证明的整圆盘主控为
$$
\sum_{m,n}\sup_{|t|\le1/256}|B(t)_{n,m}|
\le23040+\frac{512}{65535}<23041.
$$
所以 $B$ 在零点迹范数全纯，不以单条边的形式阶数代替无限频率控制。

### 两级真实算子缩放

精确零阶矩阵为 $B_0=-P+N$，$P$ 秩二，$N$ 秩六，
$PN=NP=0$、$N^2=0$。频率反号对称把 $P$ 分成两个简单块，得到 (1)。
去掉该簇并以 Riesz 投影的有界局部平凡化固定其余空间后，算子为
$\mathcal A(t)=N+tM(t)$，其中 $M(0)=QB_1Q$。
对幂零链的六维源空间作 $s$ 缩放并令 $t=s^2$，
$$
K(s)=s^{-1}V_s^{-1}\mathcal A(s^2)V_s
$$
在零点迹范数全纯。它保留全部无限维耦合，极限的全部非零谱就是 (3) 的
八个简单平方根。局部解析谱投影给出 (2)，统一预解紧集估计给出 (4)。
这个矩阵定理有一个充分小的复圆盘 $0<|t|<\tau$。

### 原动力系统的谱识别

对固定非零实参数，将 $f_m=t^{\omega(m)}E_m$ 声明为 $H_t$ 的正交归一基，
得到实际拉回的迹类延拓 $C_t=1\oplus tB(t)$。
整解析周期核心的 Fourier 截断同时在 $H_t$ 和实环面上收敛，且该核心保持于
全部实际复合，因此 $C_t^nE_m=E_m\circ F_{t/\pi}^n$。
自伴热对角右正则化在迹范数下收敛，Poisson 核定位给出全部固定点迹。
与 Faure–Roy 的已识别实现 $R_t$ 比较所有幂迹，得到整个恒等式
$$
\det(I-zR_t)=\det_{H_t}(I-zC_t)
=(1-z)\det(I-ztB(t)),\qquad z\in\mathbb C.
\tag{5}
$$
因此非零谱及代数重数完全相同。这不是原 $L^2$ 上未经证明有界的对角相似。
该识别有实范围 $0<|t|<t_A$；用粗范数排除额外常数共振可取
$t_*\le\min\{t_A,1/(2\cdot23041)\}$。
最终取 $\tau_R\le\min\{\tau,t_*\}$ 就同时满足所有前提，证明第 1 节的合成定理。
复参数用于矩阵解析扰动，不被称为本实动力系统的物理共振。

## 3. 全部实际输入与独立检查

以下文件均已由主控全文读取；独立检查针对最终实际输入，而非早期猜测。

| 文件 | 行数 | SHA-256 |
| --- | ---: | --- |
| [解析核作者证明](PAPER30_TORUS_REWEIGHTED_NUCLEAR_OPERATOR_PROBE_20260906.md) | 320 | `c85dfa0ed29f1c6eb7d29d0898984bf9e2536da5ec89868c4582db9ea7381826` |
| [两级矩阵谱作者证明 V1](PAPER30_TORUS_TWO_SCALE_MATRIX_PROOF_V1_20260906.md) | 363 | `a5cc67aad167207330a98f88ff45c26e4977285df1e14c8aaabf727eb2483d2c` |
| [动力谱识别作者证明](PAPER30_TORUS_WEIGHTED_TRACE_IDENTIFICATION_20260906.md) | 395 | `ccdcb4bb0cd1ebaabfd65c6069cd47b1bcab7e94c2e524aa77c22dcdea209cd6` |
| [独立有限层代数检查](PAPER30_TORUS_SECOND_STRATUM_ALGEBRA_CHECK_20260906.md) | 430 | `88b045f78a3e3fe9f57c868a62d26ea29dc003380d35547c3825c95dc04953ec` |
| [独立完整矩阵算子检查](PAPER30_TORUS_TWO_SCALE_OPERATOR_INDEPENDENT_CHECK_20260906.md) | 388 | `a47442b6721d005590bbbf368165c86da6f4360279fc34881913af03b3cd57e6` |
| [独立动力谱识别检查](PAPER30_TORUS_TRACE_IDENTIFICATION_INDEPENDENT_CHECK_20260906.md) | 401 | `519b4e997b04dac1226f5ac80bdec30f6276460f0de8fb9a971a8e12ad446762` |

三份检查均为所述范围内的 `PROVABLE AS STATED`。
完整矩阵检查覆盖核性及无限维谱扰动；动力识别检查复用未变的核性输入，
没有重复审查其已通过证明。低阶独立检查验证完整 20 条零阶边与 58 条一阶边。
无定理级修订；早期错误首项符号已在最终核性作者稿中更正，
早期三频率 $\sqrt{2/3}$ 猜测不属于任何被接收的定理。

配置的 GPT-5.4 MCP 审稿接口不可用；实际是如实标记的独立协作审查，
其中完整矩阵审查明确使用 xhigh。没有冒称指定模型调用、人类审稿或物理实验。

## 4. 先例扣除与下一关

[已完成查新报告](PAPER30_TORUS_SMALL_COUPLING_RESONANCE_PRIOR_PROBE_20260906.md)
为 271 行，SHA-256
`d80892c27c79fbbfdcabee116e6aeb17dd2832048fb2cac5dd01b9b035871694`，主控全文已读。
精确模型及 leading 单模衰减已有 Thiffeault–Childress 的直接先例；
一般核性、共振存在和迹识别框架分别受到 Faure–Roy、Adam 等的直接覆盖。
SBJ 的一阶相切 Blaschke 族已有精确负双首项，Pollicott–Sewell 的不同有理族
已有严格分数幂谱。主控已亲读 TC03 §II/IV、FR §2.2、SBJ 模型和定理 1.1、
PS 定义 3.1 和引理 3.7，不把这些一般机制当作本轮新发现。

现在的候选增量只能围绕本纯正弦族完整的两级渐近、显式奇偶修正及八元次谱簇。
阴性检索不等于新颖性认证。三个新命中旧来源的窄核对随后也已完成并由主控全文读取，
见 [晚命中核对](PAPER30_TORUS_RESONANCE_LATE_PRIOR_CHECK_20260907.md)：69 行，SHA-256
`4e61cd20dfe19619638cef09957c26a8e45720f60c7946cb62892d4da38aabca`。
它们没有直接覆盖所述精确族渐近；此三项排除不是世界新颖性证明。
完整包下一步做两份全新互盲候选评价，仍为四门逐份合取。
22–30 页实质正文要求未改变，Paper29 的自然成稿例外不继承。

未创建正式项目、锁、稿件、数值实验或构建。
任意支撑的旧环面上同调主问题仍为 OPEN；本谱定理不解决它，也不与已停止的
随机多点混合、作用量或形式共轭结果拼接凑篇幅。完成篇数仍是 3/5。
