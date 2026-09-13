# Paper30：有限末项递推替代的非作者独立窄检查 V1

日期：2026-09-08。核查者：`positive_finite_moment_nonauthor_check`。
本件使用 `proof-writer`，只检查新的末项替代，不修改任何旧稿或旧独审。
核查者未参与该末项推导，未读取统一算子独审中的建议证明；
提出者对统一算子 V1 的审查不作为本次新增末项的独立证据。
已完成的有限矩检查保持冻结，本轮不重开其已通过且输入未变的证明。

## Claim

固定素数 $p\ge5$，令 $m=(p-1)/2$、$\chi=(-1)^{m+1}$，
$\mathfrak j=(H,L)$，并在 $\mathbb F_p[[H,L]]/\mathfrak j^{m+1}$ 中工作。
算子为

$$
\mathscr E=H\partial_H+L\partial_L,\qquad
\mathscr D=\mathscr E^2+
\frac{2(H-1)}{H-4}\mathscr E+\frac H{H-4},
$$

其中有理系数均是左乘。采用下列已绑定条件输入：

$$
\mathcal F_3\equiv\frac38\mathscr DW+\frac{3\chi}{16}H^m
\pmod{\mathfrak j^{m+1}},\tag{U1}
$$
$$
W\equiv V\pmod{\mathfrak j^m},\qquad
V(H)=\sum_{k=0}^{m-1}\beta_kH^k,\qquad
\beta_k=\frac{(k!)^2}{(2k+1)!}.\tag{U2}
$$

此外，$W$ 是真实单位三角低块的合法有限矩，所以其总阶 $m$ 部分
$W_m$ 已在 $\mathbb F_p$ 中定义；不假定 $W_m=0$ 或存在临界有理核。
唯一新增检查是：能否以精确有限多项式恒等式

$$
(H-4)\mathscr DV=m^2\beta_{m-1}H^m
$$

取代统一算子 V1 的 Step 7，并在不改变 U1/U2 的前提下推出

$$
\mathcal F_3\equiv\frac{3\chi}{32}H^m
\pmod{\mathfrak j^{m+1}}.\tag{T}
$$

## Status

- `PROVABLE AS STATED`：在明确列出的 U1/U2 和实际有限矩定义条件下，新末项替代成立。
- 新增末项证明：限定数学 `PASS`；不需要增加假设、引入 $\beta_m$ 或削弱素数范围。
- 原统一算子的 U1 全数学作为条件输入采用，本报告不以接口核对冒称重新证明 U1。
- 未发现本次新增推导的数学缺陷。范围外的完整候选、容量和实际桥不授予新的通过状态。

## Assumptions / Actual Inputs and Reading

| 输入 | 读取及调用范围 | SHA256 |
| --- | --- | --- |
| [有限末项替代 V1](PAPER30_TWIST_POSITIVE_TERMINAL_RECURRENCE_REPLACEMENT_V1_20260908.md) | 本轮全文第 1–122 行；唯一新增被审对象 | `25d6632541903ccd33267f66e430adc6eeb6ff7b42f2ca44954b1a7923fe866a` |
| [统一临界算子作者 V1](PAPER30_TWIST_POSITIVE_UNIFIED_CRITICAL_OPERATOR_PROBE_V1_20260908.md) | 本轮全文第 1–609 行；绑定定义、Steps 1–6 的输入接口，并识别旧 Step 7 的准确职责 | `0aceec6fc8bd89e93b4148a3745c3d3b7cfd74d13f8d19792b991df8d23fed58` |
| [有限矩作者 V1](PAPER30_TWIST_POSITIVE_FINITE_MOMENT_DIAGNOSIS_V1_20260908.md) | 前一项已全文读第 1–420 行；本轮哈希未变，仅采用其严格预临界结论作为 U2 | `f5c4c4ea81155dc97ccef1cfc5fc54936048b212def7911f97a9729267da70fe` |
| [本核查者已完成的有限矩独审 V1](PAPER30_TWIST_POSITIVE_FINITE_MOMENT_INDEPENDENT_CHECK_V1_20260908.md) | 已完成并冻结的第 1–357 行报告；本轮不修改、不重新计作新增末项的独立证明 | `d092b6438f42d158bb3d3f83f8e9262c4433fa5af0ff832139a3e5f3a2be5cf5` |

本轮再次完整读取 `proof-writer/SKILL.md` 第 1–223 行。
未读取统一算子的独审文件，也未向其提出者索取答案。
主控已说明 U1 另有上游独审；本报告只把具体作者源和 U1 公式绑定为条件，
不把该说明或提出者身份作为本次新末项的数学证据。

输入接口没有变更：统一算子 Steps 1、3–5 提供实际低块自身整性、
平均权精确消元和非零临界反射修正；Step 6 使用的 U2 精度恰为总阶小于 $m$。
新的有限矩结论正好提供这一精度，不承诺总阶 $m$ 的取值。

## Proof Strategy / Dependency Map

U1 与合法有限矩、U2
$\longrightarrow$ 在总阶商中去掉未知 $W_m$
$\longrightarrow$ 左乘 $H-4$ 后逐系数消去 $V$ 的低项
$\longrightarrow$ 唯一最高项与 Wilson 配对
$\longrightarrow$ 合并保留的反射修正，得到 (T)。

本次不使用旧 Step 7 的伴随卷积、$B_m$ 有限和、$g_kt_k$ 望远镜或含 $p^{-1}$ 的终项。

## Itemized Evidence

| 核查项 | 结论 | 实际证据 |
| --- | --- | --- |
| U1/U2 与旧 Steps 1–6 接口一致 | PASS（绑定检查） | 同一真实 $W$、同一左乘算子、同一 $3\chi H^m/16$ 修正；U1 全数学不在本次重证范围 |
| 总阶商上的算子合法性 | PASS | Euler 算子保持单项式总次数；左乘的两个形式级数不降低总次数 |
| 未知 $W_m$ 可被消去 | PASS | $\mathscr EW_m=mW_m$，常数乘子 $m(m+1/2)=0$；余项多一个 $H$ |
| 左乘 $H-4$ 的次序 | PASS | 只乘算子输出，没有把 $\delta$ 移过该系数或对它误求导 |
| 常数项及全部低项 | PASS | 常数为零；第 $n$ 项为 $n^2\beta_{n-1}-2n(2n+1)\beta_n$ |
| 最高项及精确有限身份 | PASS | 次数至多 $m$，最高项唯一为 $m^2\beta_{m-1}H^m$，无隐藏高项 |
| 阶乘及递推分母 | PASS | 只到 $(p-2)!$；递推只用 $2(2n+1)$，$n<m$ 时为单位 |
| Wilson 与半区配对 | PASS | 逆元配对得 $(p-1)!=-1$；半区配对得 $(m!)^2=\chi$ |
| 除以 $H-4$ | PASS | 常数 $-4$ 非零；仅此单位的逆展开，不除以 $H$ 或 $p$ |
| 临界系数与最终符号 | PASS | $\mathscr DV\equiv-\chi H^m/4$，再与 U1 修正合成 $3\chi H^m/32$ |
| 正 $L$ 项和全部低阶消失 | PASS | 在总阶不超过 $m$ 的范围，$W_m$ 被整体消去，余下只含 $H^m$ |
| $p=5$ 最小边界 | PASS | $V=1+H$，$(H-4)\mathscr DV=4H^2$ 于 $\mathbb F_5$；最终 $\mathcal F_3=H^2$ 模总阶三 |
| 取代旧 Step 7 的完整性 | PASS（仅此用途） | 旧 Step 7 负责的唯一临界标量已准确重证；不再需要其临界卷积或望远镜 |
| 真实缺陷、$E_4$ 与实际误差桥 | 保留 / 不新增评价 | 新末项没有替代或重证这些前置及后续义务 |

目标范围内没有数学 `FAIL` 或未闭合的证明 `OPEN`。
U1 全数学的重新评价及整个候选的状态属于范围外，并非本次目标的开放证明债务。

## Proof / Independent Reconstruction

### Step 1. 总阶商与未知临界矩

在完整形式参数环中写 $W=V+W_m+R$，其中 $W_m$ 齐次总阶为 $m$，
$R\in\mathfrak j^{m+1}$。对每个单项式 $H^kL^j$，
$\mathscr E(H^kL^j)=(k+j)H^kL^j$，所以 $\mathscr E$、$\mathscr E^2$
均保持 $\mathfrak j^{m+1}$。
$H-4$ 的逆是非负 $H$ 次数的形式级数，故 $\mathscr D R\in\mathfrak j^{m+1}$。

两个左乘系数准确满足

$$
\frac{2(H-1)}{H-4}=\frac12+\frac{3H}{2(H-4)},
\qquad \frac H{H-4}\in(H).
$$

由 $\mathscr EW_m=mW_m$ 得

$$
\mathscr DW_m=
m(m+1/2)W_m+\left(\frac{3m}{2}+1\right)\frac H{H-4}W_m.
$$

第一项的系数为 $m(2m+1)/2=mp/2=0$ 于 $\mathbb F_p$；
第二项属于 $\mathfrak j^{m+1}$。因此
$\mathscr DW\equiv\mathscr DV\pmod{\mathfrak j^{m+1}}$。
整个推论只用 $W_m$ 已是合法有限矩系数，不为它指定数值或引入除以 $p$。

### Step 2. 精确有限多项式身份

$V$ 与 $L$ 无关，故 $\mathscr E V=\delta V$，其中 $\delta=H\partial_H$。
在 $\mathbb F_p(H)$ 中，左乘 $H-4$ 给

$$
(H-4)\mathscr DV
\;=\;\bigl\{H(\delta+1)^2-2\delta(2\delta+1)\bigr\}V.
$$

右边属于 $\mathbb F_p[H]$，次数至多 $m$；这是精确身份，不是事后丢弃高阶项。
作用于单项式 $\beta_kH^k$ 时，第一部分贡献
$(k+1)^2\beta_kH^{k+1}$，第二部分贡献
$-2k(2k+1)\beta_kH^k$。因此：

- 常数项只有 $k=0$ 的第二部分，而其系数为零。
- 对 $1\le n<m$，系数恰为 $n^2\beta_{n-1}-2n(2n+1)\beta_n$。
- 第 $m$ 项只来自 $k=m-1$ 的第一部分，为 $m^2\beta_{m-1}$。
- 不存在次数大于 $m$ 的贡献。

由阶乘定义，在所需有限范围内

$$
\frac{\beta_n}{\beta_{n-1}}
=\frac{n^2}{(2n)(2n+1)}
=\frac{n}{2(2n+1)},\qquad 1\le n<m.
$$

由于 $n\le m-1$、$2n+1\le p-2$，这里的分母和 $\beta_{n-1}$ 均非零。
全部低次系数准确消去，故

$$
(H-4)\mathscr DV=m^2\beta_{m-1}H^m
\quad\text{作为 }\mathbb F_p[H]\text{ 中的精确身份}.
$$

这里仅使用 $\beta_0,\ldots,\beta_{m-1}$；最高阶乘是
$(2m-1)!=(p-2)!$，所以没有 $\beta_m$、$p!$ 或需要先消 $p$ 的量。

### Step 3. 末项标量与单位除法

在 $\mathbb F_p^\times$ 中，除 $1,-1$ 外，元素与其不同的逆元配成对，每对乘积为一。
自逆元素只可能满足 $(z-1)(z+1)=0$，所以只有上述两个。
因此 $(p-1)!=-1$。又由 $(p-1)!=(p-1)(p-2)!$、$p-1=-1$，得到 $(p-2)!=1$。

另一方面，$1,\ldots,p-1$ 恰可分成 $r,p-r$ 这 $m$ 对，其中 $1\le r\le m$，故

$$
(p-1)!=\prod_{r=1}^{m}r(p-r)=(-1)^m(m!)^2=-1.
$$

于是 $(m!)^2=(-1)^{m+1}=\chi$，并且

$$
m^2\beta_{m-1}=\frac{(m!)^2}{(p-2)!}=\chi.
$$

由于 $p\ge5$，$H-4$ 的常数是非零单位；其形式逆为
$-\tfrac14\sum_{r\ge0}(H/4)^r$。所以精确地

$$
\mathscr DV=\frac{\chi H^m}{H-4},\qquad
\mathscr DV\equiv-\frac\chi4H^m\pmod{H^{m+1}}.
$$

后一余项也属于双参数的 $\mathfrak j^{m+1}$；没有把较弱的单参数同余误当成任意双参数结论。

### Step 4. 合并 U1；确认替代职责

代入 Step 1 和 Step 3 的结果，U1 给出

$$
\mathcal F_3\equiv
\left(\frac38\left(-\frac\chi4\right)+\frac{3\chi}{16}\right)H^m
=\frac{3\chi}{32}H^m
\pmod{\mathfrak j^{m+1}}.
$$

分母 $2,4,8,16,32$ 都是单位。该同余同时确定纯临界系数，
并给出全部 $k+j\le m$、$j>0$ 的消失，以及全部纯 $H$ 预临界项的消失。
这正是原 Step 7 与其 Step 6 接口合并后所需的结论，不只核对一个数值样例。
所以新的有限末项论证可完整替代旧 Step 7 在此证明链中的职责。∎

### Step 5. 最小边界的直接计算

当 $p=5$ 时，$m=2$、$\chi=-1=4$ 于 $\mathbb F_5$，
$\beta_0=1$、$\beta_1=1/6=1$，故 $V=1+H$。
直接展开得到

$$
\{(H-4)\delta^2+2(H-1)\delta+H\}(1+H)
=4H^2-5H=4H^2\quad\text{于 }\mathbb F_5.
$$

这与 $m^2\beta_{m-1}=4=\chi$ 相符。
$H-4=H+1$，所以 $\mathscr DV=4H^2\pmod{H^3}$。
再由 $3/8=1$、$3\chi/16=2$ 于 $\mathbb F_5$，得到
$\mathcal F_3=(4+2)H^2=H^2\pmod{\mathfrak j^3}$，
正好等于 $3\chi H^2/32$。此处没有借用只对 $p\ge7$ 有效的次首层。
该算例是对一般证明的边界核对，不是按素数扫描或外推。

## Precisely Replaced / Still Retained

采用本新证明后，原统一算子 V1 Step 7 中为求唯一临界标量而使用的
伴随系数卷积、$B_m$ 有限和、$g_kt_k$ 望远镜和终项先消 $p$ 均不再需要。
它们的旧文件不删除，本检查也不对其作错误判定。

必须保留 U1 的全部实际来源：完整四项端点、精确响应、平均权消元，
尤其是非零反射修正 $3\chi H^m/16$。若漏掉该修正，得到的会是
$-3\chi H^m/32$，而非所需结果。
U2 仍需真实有限矩证明；本次末项计算不能仅从三角低块的存在推出 U2。

四次移位 $E_4(0)=-3/32$、实际模 $h^M$ 误差桥、正簇因子及后续局部域证明均保留。
只在这些原输入已到位时，才可合并实际同阶常数：

$$
(2\chi)^3\frac{3\chi}{32}
+(2\chi)^4\left(-\frac3{32}\right)
=\frac34-\frac32=-\frac34,
$$

其中使用 $\chi^2=1$。本报告核对了该纯代数组合，但不把它视为实际误差桥的重新证明。
形式 $\mathcal F_3$ 的临界系数与实际最终常数是两层不同的量，不能互相代替。

## Corrections or Missing Assumptions

未发现新增末项证明的数学缺陷；无需数学修复或额外假设。
新稿第 102 行的“全部正 $L$ 次数”应始终按紧邻式 (7) 的范围理解，
即总阶不超过 $m$；可补写该限定以免脱离上下文后被读成全阶消失。
这不是当前公式或证明的量词错误，本核查没有扩大该结论。

## Open Risks / Limited Overall Conclusion

新增末项在绑定 U1/U2 后已独立闭合，限定结论为 `PASS`。
没有用提出者的独审替代本次检查，也没有重新打开旧有限矩报告。
总阶高于 $m$、U1 的全数学再审、其他 forcing 分支及完整 $C1$–$C3$ 不在本次范围。
不评价新意、容量、页数或稿件，不改变原正式容量失败、立项状态及任何冻结产物。
