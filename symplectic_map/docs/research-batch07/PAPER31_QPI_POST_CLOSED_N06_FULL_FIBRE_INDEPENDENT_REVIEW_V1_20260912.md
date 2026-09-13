# Paper31 N06：固定完整原纤维无点证书——fresh 非作者独立审查 V1

日期：2026-09-12；独审席：`/root/p31_post_closed_n06_full_fibre_independent_v1`。
唯一被审作者件：[A]，359 行，SHA-256 `e55759d00b076cb2d24c2fb2314c4f9453ca41c7cb5909aab8251871e5de4d97`。
类型：固定原对象的有界数学独审；不是新意、容量、四门或产物验收。
`route_applicability: NOT_APPLICABLE`；GPU 使用 0；未修改作者稿及任何旧接受输入。

## 1. Claim

固定
$$
K=\mathbb Q_3(s),\qquad s=\zeta_3,\qquad \pi=s-1,\qquad
t=1,\quad h=0,\quad c_0=-3,\quad c_1=-3+\pi^2.
$$
令 $X_{c_1}$ 是原八吹起曲面上原积分 $I_3=c_1$ 的完整纤维，原环面上的积分为
$$I_3=\operatorname{tr}\{A(s^2)A(s)A(1)\}-2,$$
矩阵采用 [BR] §2 的规范，只代入 $t=1$，不改变乘法次序或能级标签。
被审准确结论是
$$\boxed{X_{-3+\pi^2}(\mathbb Q_3(\zeta_3))=\varnothing.}$$
它不是仅末端曲线无根，不是 Jacobian 的有点性，也不是整个能量盘的分类。

## 2. Status

`PROVABLE AS STATED`。

原命题不需要削弱、不需要额外分裂假设；下述独立核查在明确列出的已接受原模型及整除微分前提上闭合。
固定结论的科学判断为 `PROVED — FIXED ORIGINAL FIBRE, INDEPENDENTLY CHECKED`，没有给正式分数或产物 `PASS`。
预定诊断信号为 `POSITIVE_FIXED_DIFFERENCE`；同时保留 `STOP_LONG_PAPER_STANDARD_CERTIFICATE`。

## 3. Assumptions / Notation

### 3.1 消费而不重审的上游前提

1. [INT] §§3.2–3.3 与 [G] G1/G3：$\mathcal O=\mathbb Z[s]_{(s-1)}$ 上的同一原八截面吹起曲面 $\mathcal S$ 光滑射影；原 $f=I_3$ 射影平坦，$f^{-1}(\infty)=3\mathcal D$；约化态射为 $f_1^3$。
2. [P30] 原图及完整覆盖段：$\mathcal U=\mathcal S\setminus\mathcal D$ 由环面及四条互异完整末端仿射线分层。图坐标正是 [A] §1.2；有限完整纤维是原环面方程的闭包，不漏末端点。
3. [INT] §3.3、[G] G3 给出整个 $\mathcal U$ 上的原相对微分等式 $dI_3=3\alpha$，$\alpha$ 正则，含四条末端及其开邻域；不是仅在环面泛点处成立的整除阶。
4. [BR] §2 给原矩阵、原积分及时间更新不变性；[L] Steps 1、2、4、6 给原图 1 的限制 $b_1(v;t)=-(v-s^2)^3+3t(v-s^2)-3t$ 和实际原点坐标。

这些是被审稿已经列明的接受依赖，不是本审查临时增加的假设。
[BR] T3 的判别式只用于核查作者的泛纤维光滑性旁注；无点证明本身不依赖该旁注。
本报告 $b_i(v;t)$ 的下标 $i$ 表示第 $i$ 条末端线上的 $I_3$ 限制；[L] 的 $b_3(w)$ 下标则表示积分阶数三，两者通过 $b_1(v;t)=b_3(v-s^2)$ 对应。

### 3.2 本席实际输入范围与身份

本人 FULL 读取 `AGENTS.md` 28 行、`docs/WORKFLOW.md` 39 行、`proof-writer/SKILL.md` 223 行及 `research-review/SKILL.md` 106 行。
根据任务的已指定替代安排，本席为可用 Codex xhigh 的 fresh 非作者席；工具搜索未发现技能指定的 GPT-5.4 Codex MCP 审查工具，没有实际 MCP 调用或 `threadId`，不称跨模型验证。
本席没有参与 [A] 写作，也不是作者只核五点覆盖的局部协助席；没有再委派审查。

下表 SHA 绑定整文件字节；`PARTIAL` 只代表本人实际消费所列精确范围，不冒称整件 FULL，也不继承其外文阅读身份。

| 输入 | 本人实际阅读范围 | SHA-256 |
|---|---|---|
| [A] 作者证书 | FULL 1–359 行 | `e55759d00b076cb2d24c2fb2314c4f9453ca41c7cb5909aab8251871e5de4d97` |
| [DEC] 事前边界 | FULL 1–66 行 | `1c899e1a7c3793c24ed568f843ff56e5cb337e391fea049edf265c9ea3163840` |
| [INT] 接受处置 | PARTIAL 69–101 行（§§3.2–3.3） | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` |
| [G] 原整模型 | PARTIAL 7–63、83–98 行（准确假设、G1/G3） | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| [P30] 原曲面章节 | PARTIAL 1–111、189–227、427–445 行（原图、末端时间图、完整纤维覆盖） | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| [BR] 原对象简报 | PARTIAL 35–113、159–187 行（§2 与 T3） | `b8f1ca66927b977b05a2996e42d299390d6a895d1a3378119d1be5415d70a00f` |
| [L] 原末端多截面 | PARTIAL 24–76、96–125、140–146 行；仅消费原 $b_3$ 公式与实际图坐标 | `9e6a7f2f732c79f3a7d5a32e15d52da541adbb03f845c44572a775cf9f13bfb3` |

## 4. Proof Strategy / Dependency Map

反证法，依赖顺序如下：

1. 同一原模型完备化并沿 $c_1$ 拉回；properness 把任意原 $K$ 点唯一延拓为 $R$ 点，其中 $R=\mathcal O_K$。
2. 剩余态射与原图分层把所有整提升限定在恰好五个剩余邻域；每个邻域使用完整开图，允许 $u=0$。
3. 全开空间上的 $dI_3=3\alpha$ 推出每个邻域内 $I_3$ 模 $\pi^3$ 恒定。这一步是无限整邻域证明，不由有限 CAS 提供。
4. 直接原矩阵恒等式及实际末端时间图确定五个代表能量均同余于 $-3$；固定 $c_1$ 不满足此必要同余。

## 5. Proof / 逐步独立核查

### Step 1. 原曲线身份、完备化与 proper 点覆盖

$\pi^2+3\pi+3=0$ 在 $\mathbb Z_3$ 上为 Eisenstein 多项式，因此 $R=\mathbb Z_3[\pi]=\mathbb Z_3[s]$，剩余域 $k=\mathbb F_3$，$v_\pi(3)=2$。
圆分整数局部环 $\mathcal O$ 的完备化就是 $R$；$\mathcal O\to R$ 为 DVR 的平坦完备化。
原底环映射保持 $q\mapsto s$、$\tau\mapsto1$，没有把根单位先约化成 $1$ 再建模型。

将 [G] G1 的原 $f:\mathcal S\to\mathbb P^1_{\mathcal O}$ 基变换到 $R$，再沿 $c_1:\operatorname{Spec}R\to\mathbb P^1_R$ 拉回，得到射影平坦 $\mathscr X_{c_1}/R$。
其泛纤维是原完整能级，不是任意选择的另一亏格一模型；[P30] 432–445 行明确有限纤维仍射影、是原环面方程的闭包，并保留所有末端点。
因为射影态射 proper 且 separated，DVR 赋值判据给出存在且唯一的延拓
$$X_{c_1}(K)=\mathscr X_{c_1}(R).$$
此处只需 $R$ 是以 $K$ 为分式域的赋值环和模型 proper，不要求特殊纤维光滑。

由于 $c_1\equiv0\pmod\pi$，特殊纤维为 $J^3=0$，其中
$$J=I_{1,1}(x,y;1)=y-x+x/y-1/x.$$
其支撑是 $J=0$；三重结构不产生额外 $k$ 点。有限纤维与 $\mathcal D$ 不交，故所有闭点像位于 $\mathcal U_k$。
每个 $R$ 截面的闭点剩余域是 $k$ 本身，不能产生另一个剩余域扩张上的约化类型。

旁注核验：对 $r=3$ 有 $\varepsilon=1,T=t^3=1$，[BR] T3 给 $\delta(c,1)=c^4-c^3-8c^2+36c-11$。
$\delta(c_1,1)\equiv-11\equiv1\pmod\pi$，所以作者所称原泛纤维光滑正确；不能由此称三重特殊纤维或整模型相对光滑。

### Step 2. 五个剩余点及整邻域确实穷尽

环面的单位对只有 $(1,1),(1,2),(2,1),(2,2)$，直接代入 $J$ 得 $0,2,2,2$。
约化后四图分母统一写 $d=1+uv$，直接代入并消去可去的 $u$ 极点得到
$$
\begin{array}{c|c|c}
i&J\text{ 的约化图表达}&J|_{u=0}\\\hline
1&1+uv-u-v/d&1-v\\
2&v/d-ud+u^2d&v\\
3&v/d-ud+u^2d&v\\
4&(v+1)/d-ud&v+1
\end{array}.
$$
例如图 2、3 同时使用 $u^{-1}-(ud)^{-1}=v/d$；图 4 的原分母是 $s+uv$，只在剩余模型中成为 $1+uv$。
所以闭点恰为环面 $(1,1)$，以及图 1 的 $(0,1)$、图 2 的 $(0,0)$、图 3 的 $(0,0)$、图 4 的 $(0,-1)$。
图 2、3 属于不同吹起簇的互异末端线，不合并为一点；四条末端的边界点均在已排除的 $\mathcal D$。
[P30] 47–109 行与 [BR] 90–104 行给出分层穷尽性，因此不存在第六种约化位置。

取五个代表 $Q_T=(1,1)$ 及上述四个 $(u,v)$ 坐标本身作为 $R$ 点。
若一个整截面约化到 $Q_i\bmod\pi$，它落入该点对应的完整原开图：该开图的逆像包含 $\operatorname{Spec}R$ 的闭点，而局部谱中任何包含闭点的开集均为全集。
坐标分别满足环面 $x,y\in1+\pi R$，或末端 $u\in\pi R$、$v-v(Q_i)\in\pi R$。
各图分母模 $\pi$ 等于 $1$，原图 4 的分母在 $u=0$ 等于单位 $s$；因此分母在整个剩余邻域均可逆。
允许 $u=0$，且同时包括任意非零的 $u\in\pi R$。这既不是只查末端线，也没有删掉真正末端 $K$ 点。
代表是原曲面 $R$ 点，不必位于待判纤维上；其用途只是同余比较。

### Step 3. 整除微分足以控制整个无限邻域

基变换后的相对微分仍满足
$$dI_3=3\alpha,\qquad \alpha\in\Gamma(\mathcal U_R,\Omega^1_{\mathcal U_R/R}).$$
这里使用的是 [INT] 91–97 行、[G] 85–96 行的整正则一形式，而不是仅知道剩余微分消失。
末端图的坐标环是 $R[u,v,(1+uv)^{-1}]$（前三图）或 $R[u,v,(s+uv)^{-1}]$（第四图）；环面坐标环是 $R[x^{\pm1},y^{\pm1}]$。
这些是多项式坐标环的局部化，相对微分自由，分别以 $du,dv$ 或 $dx,dy$ 为基。
故 $dg\in3\Omega^1$ 在此确实表示两个坐标偏导数均是 $3$ 倍正则函数。

在选定代表 $Q$ 处，将坐标差记为 $\xi,\eta$。
任一图分母 $d$ 满足 $d(Q)\in R^\times$；写成 $d(Q)+r(\xi,\eta)$ 后，$r\in(\xi,\eta)$，逆元由
$$d^{-1}=d(Q)^{-1}\sum_{n\ge0}\bigl(-r/d(Q)\bigr)^n$$
给出整形式幂级数，在 $\xi,\eta\in\pi R$ 时收敛。这同时说明没有隐含的 $\pi$ 分母。
于是正则函数 $g$ 有展开
$$g=g(Q)+\sum_{i+j\ge1}e_{ij}\xi^i\eta^j,\qquad e_{ij}\in R.$$
由于展开与相对求导相容，两个偏导数的所有展开系数均在 $3R$。
一次系数 $e_{10},e_{01}$ 因而属于 $3R$；二次系数满足 $2e_{20},e_{11},2e_{02}\in3R$。
$2\in R^\times$，故这三个二次系数也属于 $3R=\pi^2R$。
这逐项核实了作者“至少一个指数为可逆的 $1$ 或 $2$”的推理，不需要除以 $3$ 或使用有分母的 Taylor 阶乘公式。

在任意同剩余点 $P$ 处，$\xi,\eta\in\pi R$：一次项在 $\pi^3R$，二次项在 $\pi^4R$，所有总次数至少三的项在 $\pi^3R$。
每个次数只有有限项，总次数增大时赋值趋向无穷；$R$ 完备且 $\pi^3R$ 闭，故无限尾和仍属于 $\pi^3R$。
所以对整个剩余邻域而非有限截断点集，有
$$g(P)\equiv g(Q)\pmod{\pi^3}.$$
应用于 $g=I_3$ 得五个邻域各自恒值的必要同余。该证明不假设任何特殊点能够 Hensel 提升。

### Step 4. 原 trace 顺序、四末端与五个代表能量

从 [BR] §2 原矩阵直接有 $\operatorname{tr}A_0=1$、$\det A_0=0$、$\operatorname{tr}A_1=J$、$\det A_1=x(1-y)$。
在 $A(s^2)A(s)A(1)$ 中展开时，总 $z$ 次数不是 $3$ 倍数的非恒定三元组按循环迹成组，系数和为 $1+s+s^2=0$。
总次数 $0,6$ 分别给 $\operatorname{tr}A_0^3=1$ 和 $\operatorname{tr}P^3=1$，恰与原定义中的 $-2$ 抵消。
总次数 $3$ 的 $(1,1,1)$ 项给 $\operatorname{tr}A_1^3$；Cayley–Hamilton 将它化为 $J^3-3x(1-y)J$。
对含三个不同次数的项，顺序 $(P,A_0,A_1)$ 的系数是 $s^4=s$，$(P,A_1,A_0)$ 的系数是 $s^5=s^2$；各自三个循环排列保留同一系数。
因此原次序确实给出
$$I_3=J^3-3x(1-y)J+3s\operatorname{tr}(PA_0A_1)+3s^2\operatorname{tr}(PA_1A_0).$$
若反转矩阵次序，这两个系数不能默认为不变；作者没有犯该错。

图 1 的原限制由 [L] 给出。为独立核后三图，使用 [P30] 189–215 行的实际原时间图，而非从多项式外形猜测：
将目标时间记为 $t'$，前三步的源坐标依次为 $s^2(1-v/t')$、$s^2v$、$t'(v+s)$，源时间均为 $s^2t'$。
它们由目标末端坐标 $st(1-sv)$、$sv$、$s(sv-t)/t$ 逐项解得，且原 $I_3$ 随时间更新保持。
代入第一图原公式并顺次传播，得到
$$
\begin{aligned}
b_2(v;t')&=v^3/(t')^3-3sv-3s^2t',\\
b_3(v;t')&=v^3/(t')^3-3v-3st',\\
b_4(v;t')&=(v+s)^3-3t'(v+s)-3t'.
\end{aligned}
$$
这里只将 $t'$ 用作核对固定图身份的辅助符号，不增加待判参数。取 $t'=1$ 即 [A] 式 (5)。
它们先在末端泛点上由实际图映射成立，再因两侧都是同一末端线上的正则多项式而处处成立，故也涵盖特殊的代表坐标。

环面代表 $(1,1)$ 的 $J=0$、$\operatorname{tr}(PA_0A_1)=0$、$\operatorname{tr}(PA_1A_0)=-1$，能量为 $-3s^2$。
四末端公式在 $v=1,0,0,-1$ 的值依次为 $-3s,-3s^2,-3s,-3s^2$。
其中第一值可用 $(1-s^2)^3=3(s-s^2)$ 手算，第四值用 $(s-1)^2=-3s$ 手算。
因此五个代表都满足
$$I_3(Q_i)\equiv-3\pmod{\pi^3},$$
因为 $3(s-1)\in\pi^3R$、$3(s^2-1)=3\pi(s+1)\in\pi^3R$。

### Step 5. 全纤维矛盾及固定差异

假设存在 $P\in X_{c_1}(K)$。Step 1 的 proper 延拓和 Step 2 的完整覆盖将它放入一个上述整邻域。
Step 3–4 给出 $I_3(P)\equiv-3\pmod{\pi^3}$，但
$$I_3(P)+3=c_1+3=\pi^2\notin\pi^3R.$$
故无此 $P$，原命题成立。$\square$

参数恒等式也保持准确：$\pi^2=s^2-2s+1=-3s$，所以 $c_1=-3-3s=3s^2$。
旧 $c_0=-3$ 的原点是图 1 的 $(u,v)=(0,s^2)$，对应 [L] 的 $w=0$，其存在与本次无点一起只给这两个固定原曲线的差异。
不把旧点的存在重新计为本件的新定理。

## 6. 有限恒等式执行证据及其限度

本人执行了 [A] 303–330 行所列第二个内联 SymPy 核对，保持原矩阵、图和代表坐标，不运行数值点搜索。
实际启动该相同有限命令两次：第一次调用包装只转出尚为空的正文，没有保留后台会话号，因此不将该次当作完成证据；第二次完整捕获会话 `77921` 的结束，退出码为 0。
没有改写脚本文件或作者稿；这一转录重试不是扩大参数或重跑冻结实验。
捕获输出为：

```text
matrix identity residual: 0
terminal 1 identity residual: 0 representative value: -3*s
terminal 2 identity residual: 0 representative value: 3*s + 3
terminal 3 identity residual: 0 representative value: -3*s
terminal 4 identity residual: 0 representative value: 3*s + 3
torus representative: 3*s + 3
c1 - 3s^2 residual: 0
pi^2 + 3s residual: 0
```

$3s+3=-3s^2$，所以输出与上述手算一致。
该有限检查仅核原 trace 恒等式、四末端限制、五个代表及两个参数恒等式；正则延拓身份由原模型和手算传递说明，无限邻域排除由 Step 3 证明。
CAS 退出码不能证明覆盖穷尽、无限同余、新意或产物接受。

## 7. Corrections or Missing Assumptions

硬缺口：未发现。没有需要增加的假设、删掉的图或改动的参数，也没有仅凭有限搜索补签无点的环节。

必须小修：无。
可选说明：作者局部引理可显式列出五个坐标环及 $e_{10},e_{01},2e_{20},e_{11},2e_{02}\in3R$，减少读者核对“可逆指数”的负担；本审查 Step 3 已写出。这是可读性说明，不是修复原证明缺口，不要求为此重开冻结作者件。

## 8. Open Risks / 准确限界与交付状态

本固定结论没有剩余数学闭合风险；其上游模型及整除微分按已接受状态消费，没有在本席重新授予它们接受票。
没有推出一般参数、共同光滑能量盘、全部能量像、$\Sigma$、$N_{\rm sol}$、锐决定精度或长文容量。
没有重跑来源检索或全面查新；本报告不对外文来源的当前性作新的断言。

[DEC] 37–41 行预先规定：严格原全曲线无点是固定差异的正信号；若由标准短链得到，则停止长文投入。
此次新增对象级事实确实是原 $X_{c_1}(K)=\varnothing$，但实际机制只使用旧 $dI_3=3\alpha$、五点枚举、properness 和低阶 Taylor 同余。
因此 `POSITIVE_FIXED_DIFFERENCE` 与 `STOP_LONG_PAPER_STANDARD_CERTIFICATE` 应同时保留；数学正确不自动获得新意或容量准入。
Papers27–30 的接受、Batch07 的 4/5、P31 正文 22–30 页及正式双非作者完整四门要求均未改变。

本席唯一新建文件为本报告；不改作者稿、索引、冻结证明、锁或 PDF，不启动 P31 稿件、Route 评价或任何外部发布。
完成后本人 FULL 读回本报告，定向核验本件七个直接本地引用及输入身份，输出终态行数/SHA 给主控后冻结；自哈希不写入文件以免循环。

[A]: PAPER31_QPI_POST_CLOSED_N06_FULL_FIBRE_DIAGNOSTIC_V1_20260912.md
[DEC]: PAPER31_QPI_POST_CLOSED_IDEA_REPORT_V1_20260912.md
[INT]: PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md
[G]: PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md
[P30]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[BR]: PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md
[L]: PAPER30_QPI_TORSOR_MULTISECTION_DIAGNOSTIC_V1_20260909.md
