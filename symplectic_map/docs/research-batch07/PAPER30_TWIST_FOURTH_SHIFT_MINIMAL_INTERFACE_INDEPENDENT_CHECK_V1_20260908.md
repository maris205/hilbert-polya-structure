# Paper30：四次移位最小接口的独立数学检查 V1

日期：2026-09-08。结论：`SCOPED_MATH_PASS`。
证明状态：在本件明列、原已接受的输入条件下，`PROVABLE AS STATED`。
本件没有发现需改动作者证明的数学错误、额外假设或参数排除。
这是新替代证明及其 §5 实际接口的非作者检查，不是全部 C1–C3 的重新组合独审，
也不是全部 A10 消费者的依赖处置、新意／价值／容量票或论文验收。

## 1. 身份、实际调用和文件边界

- 检查者为 secondary Codex agent `/root/fourth_minimal_math_check`，未参与目标作者推导，
  也未参与旧 A10 的作者推导；收到的是有界审查任务，没有编辑作者源的权限。
- 主控确认实际派发参数为 `task_name=fourth_minimal_math_check`、
  `fork_turns=none`、`reasoning_effort=xhigh`；`model` 字段未设置，继承当前可用默认模型。
  不将技能中的常量冒称为实际模型，不声称调用了 `gpt-5.4`、跨模型接口或人类评审。
- 已完整读取 `AGENTS.md`、`docs/WORKFLOW.md`，定向读取 `BATCH_07_CONTEXT.md` 第 1–145 行；
  完整读取 `research-review` 的 MCP 版、secondary-agent 版和 `proof-writer` 技能。
  当前工具元数据中没有 `mcp__codex__codex`／`codex-reply`；没有进行该类 MCP 调用。
  本次使用已实际派发的独立代理路径，不再派生其他审查代理。
- 按项目和本次任务覆盖技能默认的 ML 会议评分、实验建议、稿件重写及其他输出位置。
  技能在本件中的实质作用是明确原量词、依赖、有限边界、反例检查和证明状态；
  不因技能建议扩大为新查新、Route、测页或外部操作。
- 实际操作只有指定本地文件的读取、定位、有关输入的 SHA256 核对和新增本报告。
  没有运行作者的小素数程序，没有新建数值实验；以下结论来自逐式代数推导和精度核对。
  没有改动作者稿、旧稿、接受处置、登记册或其他文件。

审查对象为 [四次移位最小全参数接口作者 V1](PAPER30_TWIST_FOURTH_SHIFT_MINIMAL_INTERFACE_PROOF_V1_20260908.md)，
全文 295 行，实际核验 SHA256：

`dec42cbb9d92e6f732983a01bf6d5519c72084e076796221a6e08fd2821063c2`。

## 2. 实际读取范围与接受输入

下列行号只定位输入，不作篇幅或工作量代理。

| 输入 | 实际读取范围 | 本次用途及审查边界 |
| --- | --- | --- |
| [目标作者 V1](PAPER30_TWIST_FOURTH_SHIFT_MINIMAL_INTERFACE_PROOF_V1_20260908.md) | 全文 1–295 | Claim、§§1–5 和边界全部核查 |
| [A10 原完整四次证明](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md) | 全文 1–320 | 对照同一形式端点及被替代的义务；不以其式 (2)、(17)、(22) 或已知常数倒证新引理，不重授旧全参数求值 PASS |
| [A07 一般第三端点](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) | 7–78、112–171、183–527 | 读取 Claim、工作环、Steps 1–4 全文和 Step 5；核对新证明使用的 action 误差、式 (18) 四项端点、式 (21)–(24) 有限移位，以及实际第一项的配对源 |
| [A06 两块响应桥](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md) | 1–106、141–181、328–428 | Claim 全文、记号、Steps 3–4；核准确两条耦合方程及 $h^{M-m}$ 原始块误差，条件采用原桥证明，不重审阶乘桥的全部历史推导 |
| [A09 全 $H$ 响应](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md) | 95–128、140–273 | Step 1 全文、Step 2 开头及记号；核完整 $\mathcal F_3$ 的定义与新三次系数吻合，不重审后续二阶矩及根平移 |
| [A13 统一正簇](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md) | 9–92、113–146、317–423 | Claim、记号及 Steps 4–5 全文；核新接口与原逐系数实际桥、单位商转移相容。Step 5 只核接口衔接，不重新授予全部局部域结论 |
| [有限替代接受处置](PAPER30_TWIST_POSITIVE_FINITE_REPLACEMENT_DISPOSITION_V1_20260908.md) | 全文 1–167 | 条件采用其中明确接受的 F2、O2 Steps 1–6、T 的三次输入，不再打开这三件及其已通过证明 |

有关旧输入的实际 SHA256：

| 输入 | SHA256 |
| --- | --- |
| A10 | `ec3f6de59e55176fe11a62b36d27da516bb8d620c438fdd0037ee6c099a260da` |
| A07 | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |
| A06 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |
| A09 | `3d0fea6035d33c11e912946a442278711f061bebde32724ad003a3b2f9994e6d` |
| A13 | `870d90ff0e9eb85f9ae174c0a2f79a624454ed248db0acbd546b44e7856b28f6` |
| 有限替代接受处置 | `c615bdaf83324eba92c6dc18db7d29635f0080855523afd68c0fd5b307ad6213` |

具体采用的已接受条件为：

1. 同一低块、SUM action、实际规范 $h=D_1$、$\rho=-h$、$L=\rho\lambda$，
   A07 四项真实端点、有限 $r$ 及其 $O(H^{4m+1})$ 精度，A06 的原两块误差。
2. A09 的完整三次系数定义，特别是其中已实际配对的第一端点项；不是删去该项的系数。
3. F2、O2 Steps 1–6、T 已接受地给出
   $$
   [L^j]\mathcal F_3\in H^{m-j+1}\mathbb F_p[[H]]\quad(1\le j<m),
   \qquad \mathcal F_3(H,0)=\frac{3\chi}{32}H^m+O(H^{m+1}).
   $$
4. A07 首层单位 $a_m=-3\chi/64+O(h)$，原整首一分离
   $S=P_{\rm cl}U_{\rm cl}$ 及 $U_{\rm cl}\equiv a_m\pmod{h^{e_*}}$。

这些条件并非本报告新加的假设；它们已明列于作者稿、原接受处置和原消费者。
本次逐项核查的是新证明是否正确调用它们，不将旧输入未变的证明算作又一次完整独审。

## 3. 准确 Claim 与依赖顺序

对每个素数 $p\ge5$，置 $m=(p-1)/2$、$\chi=(-1)^{m+1}$。
被审查的新结论准确为

$$
\mathcal E(H,L)=r(H)^3\mathcal F_3(H,L)+r(H)^4E_4(L)
                     +O(H^{4m+1}),
\qquad E_4\in\mathbb F_p[L],\quad E_4(0)=-\frac3{32}.
$$

不要求新证明求出 $E_4$ 的正 $L$ 系数、准确次数或原 A10 的完整闭式。
在全部 $a\ge2$ 的实际转移中，还检查作者 §5 的

$$
S(0)=-\frac34h^{m-1}+O(h^m),\qquad
[L^j]S\in h^{m-j}\mathcal O^+\quad(1\le j<m),
$$
$$
b_0=16\chi h^{m-1}+O(h^m),\qquad
b_j\in h^{m-j}\mathcal O^+\quad(1\le j<m).
$$

依赖顺序确为：全参数有限单位模型与实际第一项配对 → 四次多项式存在及精度 →
仅为算常数而取 $H=L=0$ → 有限标量配对 → 接受的三次输入与实际桥 → 首一系数。
没有用已接受的实际 $-3/4$ 或旧四次常数去倒证新标量。

## 4. §1：全参数存在与精度检查

**PASS。** 对应作者第 67–100 行。

对角元在 $H=\nu=0$ 为 $-i^2$，$1\le i<p$，与 $L$ 无关。
$J,K$ 无常数项，故低块及两个响应均逐 $x$ 次数作有限三角求解。
在任意所需 $H,\nu$ 系数上只作有限次参数多项式运算，并除以与 $L$ 无关的单位，
所以不会产生参数分母。若要明确统一界，递推还给出
$\deg_L P_i,\deg_L y_i,\deg_L Q_i\le\lfloor i/2\rfloor$；
端点乘积的两个正次数相加为 $p$，因此参数次数有统一有限界。
这只是核查有限性的内部界，不是对原 $E_4$ 准确次数的新主张。

在独立移位模型中，由正负下标的 $\mathsf S,\mathsf U$ 奇性及 $\mathsf T$ 偶性，
后三项需要的缺陷为

$$
\delta_i^{\rm low}=3\nu\mathsf S_i-9\nu^2\mathsf T_i+27\nu^3\mathsf U_i,
\qquad
\delta_i^{\rm mid}=3\nu\mathsf S_i-3\nu^2\mathsf T_i+9\nu^3\mathsf U_i,
$$
$$
C_i=-6\nu^2\mathsf T_i+18\nu^3\mathsf U_i.
$$

准确耦合式给 $y=O(\nu)$、$Q=O(\nu^2)$，故后三项确从三次移位起。
其三次系数分别为 A09 式 (15) 后三项；加上实际已配对的第一项，
得到的是同一个完整 $\mathcal F_3$。

第一项必须单独处理。A07 的实际配对为

$$
\frac18\sum_{i=1}^{p-1}i^3(C_i-C_{p-i})P_iP_{p-i}
=\frac{3r^3H}{8(H-4)}\sum_{i=1}^{p-1}i^3\mathsf S_iP_iP_{p-i}
 +O(H^{4m+1}).
$$

这里的 $1/8$ 来自原 $1/4$ 与奇权配对的一半，符号一致。
由 A07 式 (20)–(24)，若 $v=T-1$，被舍弃的误差最早属于
$v^4/H=O(\eta^{4p-2})$；反演不变性将其放回 $O(H^{4m+1})$。
因此新稿没有用独立 $\nu$ 下未经实际配对的第一项替换真实端点，
也没有遗漏一个可能处在 $H^{4m}$ 的第一项贡献。

设后三项的四次系数为 $E_4(H,L)$。上述单位性证明
$E_4(H,L)\in\mathbb F_p[L][[H]]$，其 $H^0$ 截面才定义 $E_4(L)$。
三种误差分别为

| 误差 | 代回 $\nu=r(H)$ 后的最低高度 |
| --- | --- |
| 四次系数的正 $H$ 修正 | $4m+1$ |
| 五次及更高移位 | $5m\ge4m+1$ |
| 真实传播子与有限移位模型的差 | $4m+1$，单位三角比较及整端点运算不降阶 |

$m\ge2$ 时全部满足目标精度；$m=2$ 时 $5m=10>9=4m+1$。
整个多项式存在论证先于常数截面，不依赖 $L=0$ 的求解，亦未使实际参数幂零。

## 5. §2：常数截面与四个响应

**PASS。** 对应作者第 102–162 行。

取 $H=L=0$ 仅用于求常数，$\mathcal D=-\mathcal N^2$。
令 $z=x/4$，则对 $1\le n<p$，

$$
U_n=\frac{2}{n4^n},\qquad f_n=\frac{2}{4^n},\qquad
g_n=\frac{2n}{4^n},\qquad F=g=J,\qquad K=F/2.
$$

$U=-2\log(1-z)$ 的使用范围严格为 $n<p$，相应 $n$ 及有限指数中的阶乘均为单位。
$\mathcal N^2U=xe^U/2$ 与 $U_1=1/2$ 验证了同一低块，单位三角唯一性排除模型替换。
没有定义或约化可能含 $1/p$ 的 $U_p$。

从 $\mathcal NF=F(1+f)$、$\mathcal Nf=g=F$ 直接得到

$$
\mathscr Lf=-F,\qquad
\mathscr Lg=-F-2Ff-Ff^2,\qquad
\mathcal N^2f=F+Ff,
\qquad \mathscr L=-\mathcal N^2+F.
$$

独立提取准确耦合式的 $\nu$ 系数，得到

$$
\mathscr Lt=F/2,\qquad
\mathscr La=-f/8-\mathcal Nt,
$$
$$
\mathscr Lq=F/16+\mathcal N^2t/2-Kt^2,
$$
$$
\mathscr Lb=\mathcal N^2a/2-3\mathcal Nt/8-2Kta-2\mathcal Nq.
$$

于是 $t=-f/2$。代入 $q=g/8+f/16$ 后，两侧均为
$-3F/16-Ff/4-Ff^2/8$，故此 $q$ 是相同有限方程的唯一解。
后两条准确化为作者式 (7)、(8)：

$$
\mathscr La=-f/8+g/2,\qquad
\mathscr Lb=\mathcal N^2a/2+\mathcal Nf/16+Kfa-\mathcal Ng/4.
$$

尤其 $\mathcal Nf/16$ 来自 $3\mathcal Nf/16-\mathcal Nf/8$，
$Kfa$ 的正号来自 $-2Kta$；没有漏掉传播子左侧的 $2\mathcal Nq$。
这完成对四个响应的独立核算，不借用旧 A10 的最终标量身份。

## 6. §3：有限配对、真实端点与常数

**PASS。** 对应作者第 164–235 行。

### 6.1 配对的定义域

$B(v,w)=[x^p]vw$ 指两个零常数、次数小于 $p$ 的有限代表的通常乘积取系数；
不是先在 $\mathbb F_p[x]/(x^p)$ 内乘完再提取已被杀掉的第 $p$ 项。
更换代表的 $x^p$ 及以上项，只会与另一因子的零常数相乘或产生更高次数，
故该定义不依赖那些未指定系数。

乘积法则与特征 $p$ 给出
$B(\mathcal Nv,w)=-B(v,\mathcal Nw)$。
两次应用后，$-\mathcal N^2$ 自伴；$F$ 的乘法也自伴。
截断 $Fv$ 所舍的次数至少为 $p$，仍不进入与零常数 $w$ 的配对。
因此作者式 (9) 合法，不触及 $U_p$ 或响应的第 $p$ 方程。

### 6.2 从真实后三项重新提取四次端点

$H=L=0$ 时 $\mathsf S_i=i$、$\mathsf T_i=-1/4$、$\mathsf U_i=0$，故
$C_i=3\nu^2/2$、$\delta_i^{\rm low}=3i\nu+9\nu^2/4$、
$\delta_i^{\rm mid}=3i\nu+3\nu^2/4$。
分别代入 A07 式 (18) 的第二、三、四项，四次系数为

$$
\frac32 B(F,a),\qquad
6B(F,b)+\frac92B(f,q),\qquad
6B(\mathcal N^2t,a)+\frac34B(\mathcal Nt,t).
$$

最后一项为零，因为奇权同因子配对反对称且 $2$ 可逆。
偶权的两个 $t,a$ 混合项相等，得到系数 $6$。
这恰是新稿式 (10)，没有从旧式 (17) 逆推端点。

### 6.3 两个未知响应的消去

用 $B(F,b)=-B(f,\mathscr Lb)$，再代入 $t,q$，所得各项逐一为

$$
\begin{aligned}
E_4(0)={}&B(3F/2-6\mathcal N^2f-6Kf^2,a)
+\frac32B(f,\mathcal Ng)\\
&-\frac38B(f,\mathcal Nf)+\frac9{16}B(f,g)+\frac9{32}B(f,f).
\end{aligned}
$$

其中 $-6\mathcal N^2f$ 的两半分别来自消去 $b$ 和原 $t,a$ 端点。
恒等式

$$
3F/2-6\mathcal N^2f-6Kf^2=\mathscr L(3g+3f/2)
$$

两侧均等于 $-9F/2-6Ff-3Ff^2$，故作者式 (12) 的系数和符号成立。
再以自伴性及 $\mathscr La=-f/8+g/2$，第一项成为

$$
\frac32B(g,g)+\frac38B(f,g)-\frac3{16}B(f,f).
$$

由 $g=\mathcal Nf$，有 $B(f,g)=B(f,\mathcal Nf)=0$，
$B(f,\mathcal Ng)=-B(g,g)$，因此全部 $B(g,g)$ 抵消，剩下

$$
E_4(0)=\frac3{32}B(f,f).
$$

最后，不调用全参数奇矩，直接用有限系数算出

$$
B(f,f)=\sum_{i=1}^{p-1}\frac{4}{4^p}
=\frac{4(p-1)}{4^p}=-1\quad\text{于 }\mathbb F_p,
$$

其中 $4^p=4$。故 $E_4(0)=-3/32$，对每个 $p\ge5$ 成立。
全部抵消只用正次数有限乘积，不需要能量积分、全参数奇矩、分裂根或第 $p$ 低模态。
作者的小素数检查未被计入这项无限量词证明。

## 7. §§4–5：全参数系数与实际首一转移

**PASS。** 对应作者第 237–280 行。

§1 的结论是 $E_4(L)\in\mathbb F_p[L]$，不是只在 $L=0$ 定义的数值。
所以每个 $[L^j]E_4$ 都可整提升，既没有参数极点，也没有被假定为零。
令 $D=3m+1$。对 $1\le j<m$，三类形式项除以 $H^D$ 后依次属于

$$
H^{m-j},\qquad H^{m-1}\subseteq H^{m-j},\qquad H^m.
$$

第二个包含方向由 $m-1\ge m-j$ 给出。
因此得到的全部中间低参数系数界确实不需要 $E_4$ 正系数的闭式。
此处没有对 $j\ge m$ 另造强系数界；对这些系数保留的是完整形式分解与整性。

常数项必须合并两个同阶来源。由 $\chi^2=1$，

$$
(2\chi)^3\frac{3\chi}{32}=\frac34,\qquad
(2\chi)^4\left(-\frac3{32}\right)=-\frac32,
$$

总和为 $-3/4$，而不是单独的四次贡献。
$r$ 的更高 $H$ 修正及三次常数的下一层均只进入 $O(H^{4m+1})$。

实际桥仍使用 A06 的原块误差 $h^{M-m}$，只在乘上 A07 已核过的
至少 $h^m$ 的真实端点缺陷后，才获得模 $h^M$ 的端点精度。
没有把未乘缺陷的块误差擅自升级。
对 $a\ge2$，

$$
M\ge pm=(2m+1)m,\qquad
pm-(4m+1)=2m^2-3m-1\ge1\quad(m\ge2).
$$

因此形式目标层可转回实际 $h$，不同整提升的 $p$ 倍差也落入所需误差以上。
除以 $h^D$ 后，桥误差为 $h^{e_*}$，其中

$$
e_*=M-D\ge m.
$$

最小边界 $p=5,a=2$ 给 $m=2,M=10,D=7,e_*=3$，
故模 $h^9$ 的未归一化精度及归一化后的模 $h^2$ 精度都合法。
得到 $S(0)=-3h^{m-1}/4+O(h^m)$ 及全部指定中间系数界。

原整分离与单位商同余进一步给
$S\equiv a_mP_{\rm cl}\pmod{h^{e_*}}$。
因 $a_m=-3\chi/64+O(h)$ 是单位，

$$
\frac{-3/4}{-3\chi/64}=16\chi.
$$

$e_*\ge m$ 保留常数下一阶误差，也保留所有 $h^{m-j}$ 界，
所以作者的 $b_0,b_j$ 恰接回 A13 Step 4 的原输出。
A13 Step 5 接收的非零端点与严格中间高度没有改变；本件不重证或扩大其后续域论结论。

## 8. 结论、无需修订项与剩余边界

目标作者 Claim 及 §5 接口在原全部 $p\ge5,a\ge2$、同一 $h=D_1$／SUM／$L$ 规范下保留，
本次限定结论为 `SCOPED_MATH_PASS`；未发现需要作者补加假设、删去参数或修正符号的步骤。
报告中列出的驱动展开、有限配对定义域和误差数值，是对原步骤的核算说明，
不是未经作者知情而另改原证明。

新证明足以承担本件选定的内部义务：全参数四次分解、四次常数以及既定实际正簇系数接口。
它未重证原 A10 的完整显式多项式、准确次数或其他可能需要正参数闭式的结论。
其他当前消费者是否全部只需这个较小接口，应由另行的限定依赖检查回答；
本报告不据局部 PASS 自行宣布 A10 从整个 C1–C3 必要链删除。

没有重新评价已通过且未变的 F2／O2／T 数学，没有全 C1–C3 新组合票、
新意／价值／容量评分、稿件、测页、Route、根扫描或外部操作。
原稿、旧显式结果、独审、失败和接受状态均完整保留。
