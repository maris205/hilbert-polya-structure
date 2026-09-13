# Paper30：第三 forcing 全部高系数首层消失的独立核查 V1

日期：2026-09-08。审查者：独立非作者代理 `negative_high_layer_review`。
本件按 `proof-writer` 核查已冻结输入的全部新证明；只写本报告，未编辑作者稿、
既有接受输入、状态文件或论文产物。作者稿全文 343 行已读取。

## Claim

审查对象是同一双谐波模型、实际规范及 SUM action 下，任意素数
$p\ge5$、整数 $a\ge2$ 的以下共同高系数结论及其商与根界应用。
令

$$m=(p-1)/2,\quad M=p^{a-1}m,\quad D=3m+1=p+m,\quad
e_*=M-D,\quad E=M-m,$$
$$S=h^{-D}p^2\mathcal B_3=\sum_j a_jL^j=P_{\rm cl}U_{\rm cl}.$$

原稿主张

$$p[L^j]\mathcal B_3\in h\mathcal O^+\quad(m<j\le D),$$
$$a_j\in h^{e_*+1}\mathcal O^+\quad(j>m),\qquad
U_{\rm cl}\equiv a_m\pmod{h^{e_*+1}\mathcal O^+[L]}.$$

写 $U_{\rm cl}=\sum_{r=0}^pu_rL^r$，结合既有
$v_h(u_p)\ge M-2m$，令

$$\delta_1=\min\left\{\frac{e_*+1}{p-1},\frac{M-2m}{p}\right\}.$$

则每个负簇根满足 $v_h(\beta)\le-\delta_1$，且任意有限扩域中的
非零参数满足

$$v_h(S(\ell))=m v_h(\ell)\qquad(-\delta_1<v_h(\ell)\le0).$$

这里审查的是下界、同余及开区间点值公式；不是任一下一层非零、
准确负 Newton 图、不可约性或简单性的证明。

## Status

**PROVABLE AS STATED。29 项限定核查全部 PASS；0 项 FAIL。**

原命题与全部量词无需修改，无阻断问题，无作者修订要求。
结论建立在原稿已明确调用的接受输入上，未补加新的整性、初值或非零假设。
本报告不是 Route 评价、候选容量票、论文立项或 PDF 验收。

## Assumptions and input identity

实际环为 $\mathcal O^+=\mathbb Z_p[h]$，其中
$h=2-\zeta-\zeta^{-1}$、$v_h(h)=1$、$v_h(p)=M$，剩余域为
$\mathbb F_p$。所有理想包含均逐 $L$ 系数解释；$L=\rho\lambda$、
$\rho=-h$ 及传播子负号沿用作者稿。

输入身份如下；首项为本次全文独审的唯一新作者稿，其余只读所需接受段落。

| 输入 | SHA256 | 实际读取与使用范围 |
| --- | --- | --- |
| [HIGH_LAYER PROOF V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_LAYER_PROOF_V1_20260908.md) | `0d3aa48f80052d8ee8da5a9808e873a6b63c0054a3b8a262c7596bf03558222a` | 全文第 1–343 行；本次全部审查结论绑定此字节版本 |
| [SECOND_FACTORIAL_BLOCK DISPOSITION](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_DISPOSITION_20260907.md) | `e3f46a7725f7f6354695c30613219a9df67f526ab559a832f0f2e9bbfe21c213` | 整块、实际初值及指数归一化整性；全文读取 |
| [SECOND_FACTORIAL RESPONSE_BRIDGE V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md) | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` | 第 114–182、196–427 行；式 (12)、(20)–(28) 及其准确误差论证 |
| [GENERAL_PRIME V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` | 第 183–246、277–374 行；非驻值 Euler 与真实缺陷首层 |
| [ROOT_CLUSTER_SEPARATION V1](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md) | `da834676ba00aa72e292acee6281b1a4ee4cd4dc8ebfab964a7fd28b503b7f2f` | 第 10–78 行的 Claim 与接受分解；第 336–377 行的精确模型次数论证 |
| [NEGATIVE_TOP DISPOSITION](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_DISPOSITION_20260908.md) | `322dabd596ed1055eb90b65729a83c2f825a2ed380208fd149059f2e7d0c353c` | 全文 98 行；只调用接受的 $v_h(u_p)\ge M-2m$ 与既有边界 |

本次没有重开旧正簇、最高项临界证明、既有 39 项审查或旧构建树。
工作区无 Git 元数据，使用上述文件哈希绑定，不生成提交号。

## Notation

采用作者稿的零常数形式块 $P(H,x),Y(H,x),Z(H,x)$，以及实际块
$Y^{\rm act}_j=pV_{p+j}$、$Z^{\rm act}_j=p^2V_{2p+j}$，
$0\le j<p$。$\Pi_{>m}$ 是精确删除 $L$ 次数不超过 $m$ 项的投影。

在 $\mathbb F_p[L][x]/(x^p)$ 中，记
$U=\overline{P(h,x)}$、$\mathcal N=x\partial_x$、
$T=1+\mathcal NU$、$\mathcal O=-\mathcal N^2+J_0$。
该环中 $\mathcal N$ 合法保留截断理想；所有指数只使用低于 $p$ 的系数。

$\eta=\overline{h^{-E}Y^{\rm act}_0}$ 是任意可能依赖 $L$ 的剩余多项式。
它不依赖 $x$，所以 $\mathcal N\eta=0$；这不要求 $\eta$ 是标量常数。

## Proof Strategy

从接受的准确实际方程而非旧端点同余出发，独立解出首层初值响应；
将两种配对误差同时展开，检查它们在 $h^M$ 层确实抵消。
再从精确 Euler 身份重新分组并估计每类余项，单独核查归一化 action
的剩余参数次数。最后检查先投影再除以 $p$、首一商的逆向系数比较和根界。

## Dependency Map

1. 实际初值和准确 $p$ 倍整误差给出 $h^E$ 层响应方程。
2. 缩放导数身份与单位三角唯一性确定完整响应；真实 Chebyshev 缺陷
   将其移至 $h^M$ 层，两种配对之和在该层为零。
3. 形式三角递推给出精确 $L$ 次数上界，故高次投影完全消去模型配对。
4. 非驻值 Euler 精确分组及指数响应桥分别控制余项与 action，
   从而投影后的 $1/p$ 操作仍留下至少一个 $h$ 因子。
5. 接受的首一因子分解、$a_m$ 单位及最高项更强下界，给出商同余和根界。

## Proof / independent reconstruction

### Step 1. 真实初值引出的完整首层响应

接受输入给出 $\Delta Y,\Delta Z\in h^E\mathcal O^+[L][x]/(x^p)$。
由于 $Z^{\rm act}_0\in h^M$，且 $M-E=m\ge2$，
首层常数为 $y_0=\eta$、$z_0=0$。实际方程中的误差除以 $h^E$
后仍属于 $h^m$；平方差的二次项除后属于 $h^E$。两者均可合法约化为零。
于是正次数上准确得到

$$\mathcal Oy=0,\qquad
\mathcal Oz=-2K_0(\bar Y-1/2)y.$$

独立对低块方程应用 $\mathcal N$，得到

$$\mathcal O\mathcal NU=-J_0,\qquad
\mathcal NJ_0=2K_0T,\qquad
\mathcal O\mathcal N^2U=-2K_0T^2.$$

因此 $\mathcal OT=0$、$\bar Y=-\mathcal NU/2$、
$\bar Z=\mathcal N^2U/8$。所需解为

$$y=\eta T,\qquad z=-\frac\eta2\mathcal N^2U.$$

第二式代入产生 $\eta K_0T^2$，恰是所需驱动；两式常数均正确。
各正次数的对角元为 $-j^2$，$1\le j<p$，故唯一性成立。
全部操作均为 $\mathbb F_p[L]$ 线性；没有对 $\eta$ 的参数次数作限制。

### Step 2. 配对误差的关键抵消确实提高一阶

真实缺陷均在 $h^m$，除后首层同为 $6\chi i$。令 $j=p-i$。
低／第二块贡献和中间配对的两个线性贡献分别为

$$-6\chi\eta i^2j^2U_iU_j,\qquad
-6\chi\eta i^3jU_iU_j.$$

其和为

$$-6\chi\eta i^2j(i+j)U_iU_j=0\quad\text{于 }\mathbb F_p[L],$$

因为 $i+j=p$。这是固定每个 $i$ 的两类贡献相消，不依赖全体下标求和
或特殊 $\eta$ 的取值。二次差至少在 $h^{2E+m}$，且
$2E+m=M+E\ge M+1$。把任一首层响应或缺陷换为其余项，也至少提高一阶。
由此得到

$$\mathcal F_{\rm act}-\mathcal F_{\rm mod}\in h^{M+1}\mathcal O^+[L].$$

作者稿没有把原来仅到 $h^M$ 的比较直接除以 $p$；本步提供了真实新增的一阶。

### Step 3. 模型低次数在实际代入后仍是精确身份

每个模型系数均由不含 $L$ 的单位传播子除出。低块递推与有限指数乘积中
的总 $x$ 指标保证

$$\deg_LP_i,\ \deg_LY_i,\ \deg_LZ_i\le\lfloor i/2\rfloor.$$

每个固定 $x$ 次数的 $L$ 次数界不依赖形式 $H$ 阶，因此完备代入
$H=h$ 后仍为有相同次数界的多项式。配对下标之和为奇数 $p$，所以

$$\lfloor i/2\rfloor+\lfloor(p-i)/2\rfloor=m.$$

由缺陷不含 $L$，得到 $\Pi_{>m}\mathcal F_{\rm mod}=0$，是特征零中的
精确消去，不是只在剩余域里次数下降。

### Step 4. Euler 身份和全部余项重算

有限 action 的 $V_i$ 偏导是
$(d_i-d_{3p-i})V_{3p-i}/2$，并非零。加权 Euler 所得作者稿式 (14)
保持该非驻值项。乘以 $p$ 后，按实际三个配对区间重组：

- 低／第二块成对权重为 $(2i-3p)/p=2i/p-3$，产生
  $\mathcal F_{\rm act}/p$ 的低块项及 $-3\delta_i^{\rm low}P_iZ^{\rm act}_{p-i}$。
- 中间块原求和权重为 $(p+i)/p=i/p+1$；作者稿的中间块求和已经保留
  每个 $1\le i<p$，没有再漏乘或重复增加二分之一。
- 内部 $p,2p$ 两项合计为
  $-(d_p-d_{2p})(pV_p)(pV_{2p})$。

因此作者稿式 (15)–(16) 是准确恒等式。前两类余项在 $h^m$；
内部传播子在 $h^{2m}$，且初值乘积在 $h^E$，内部余项至少在
$h^{2m+E}$。于是完整 $R\in h^m\mathcal O^+[L]\subset h\mathcal O^+[L]$。
实际上内部项只用传播子整性和 $E\ge1$ 即足以达到本步目标；稿中更强界不导致额外义务。

### Step 5. action 整性和剩余次数分别成立

动能乘 $p^2$ 后的非内部乘积是 $P_iZ^{\rm act}_{p-i}$ 或
$Y^{\rm act}_iY^{\rm act}_{p-i}$，内部乘积是
$(pV_p)(pV_{2p})$，全部整。势能所需次数为 $3p-1$、$3p-2$，均严格小于
$3p<p^2$；接受的准确指数桥同样给出整性。因此 $p^2\Phi$ 可合法约化。

非内部动能可换成模型剩余，其配对下标和为 $p$，故 $L$ 次数至多为 $m$。
内部动能乘积属于 $h^E$，剩余为零。

对势能，接受的准确桥为

$$p^2[x^{2p+j}]e^{\alpha V}
=[x^j]e^{\alpha P(h,x)}
\left(\alpha Z^{\rm act}+\frac{\alpha^2}{2}(Y^{\rm act}-1/2)^2\right)
+p\epsilon_{\alpha,j}.$$

其中 $\epsilon_{\alpha,j}$ 逐系数整，真实 $Y^{\rm act}_0$、
$Z^{\rm act}_0$ 已包括在公式内。约化后每个 $x^r$ 系数的参数次数至多
$\lfloor r/2\rfloor$。$j=p-1$ 时该界是 $m$；$j=p-2$ 时是 $m-1$，
再乘 action 外部的 $L$ 得 $m$。故

$$\deg_L\overline{p^2\Phi}\le m,\qquad
\Pi_{>m}p^2\Phi\in h\mathcal O^+[L].$$

这一步没有从未归一化的非整指数直接取剩余，也没有漏掉第二谐波的外部 $L$。

### Step 6. 投影、除法与首一商

精确高次投影给

$$\Pi_{>m}p\mathcal B_3=-6\Pi_{>m}p^2\Phi
+\frac1p\Pi_{>m}(\mathcal F_{\rm act}-\mathcal F_{\rm mod})+\Pi_{>m}R.$$

中间项属于 $h\mathcal O^+[L]$，因为 $v_h(p)=M$；其余两项也在该理想。
不需要假设 $\mathcal F_{\rm mod}/p$ 的低系数整。由
$S=(p/h^D)(p\mathcal B_3)$，逐系数得到高度 $M-D+1=e_*+1$。

首一 $P_{\rm cl}$ 的递降系数比较中，将 $u_s=0$ 对 $s>p$ 作通常的
有限多项式系数约定，则

$$a_{m+r}=u_r+\sum_{i<m}b_i u_{m+r-i}.$$

求和下标严格大于 $r$，故从 $r=p$ 递降至 $1$ 给出全部
$u_r\in h^{e_*+1}$。比较 $L^m$ 系数只能并且确实给出
$u_0\equiv a_m\pmod{h^{e_*+1}}$。原稿未误写成两者相等。

### Step 7. 根界、点值和边界

$e_*+1=M-3m\ge2m>0$，故 $u_0$ 是单位。若
$-\delta_1<t=v_h(\ell)<0$，对 $1\le r<p$ 有

$$v_h(u_r\ell^r)\ge e_*+1+rt
\ge e_*+1+(p-1)t>0,$$

最高项则有 $v_h(u_p\ell^p)\ge M-2m+pt>0$。
$t\ge0$ 时这些非恒定项赋值仍为正。故上述区域内 $U_{\rm cl}(\ell)$
是单位，并给出全部负根的所述上界。有限扩域只改变允许的有理赋值，
不影响唯一最低项论证。

在 $-\delta_1<t\le0$，$P_{\rm cl}$ 的第 $i<m$ 项与首一项的赋值差至少为
$1+(i-m)t>0$，所以 $v_h(P_{\rm cl}(\ell))=mt$。
原稿准确排除新端点，那里非恒定商项可能与常数项同高。

独立检查还给出：当 $a=2$ 时，$\delta_1=m-1$，第二个候选值比它大
$1/p$；当 $a\ge3$ 时，新旧最小值均可由保留的最高项界控制，
实际有 $\delta_1=\delta_+$。后一断言可直接由

$$\frac{e_*}{p-1}-\frac{M-2m}{p}
=\frac{M-m(p+2)-p}{p(p-1)}>0$$

看出：$M\ge p^2m$ 时，分子至少为 $m(p-2)(p+1)-p>0$，
因为 $m\ge2,p\ge5$。这验证原稿不声称对上一轮所有 $a$ 严格改善的边界。
相对最早的 $e_*/p$，两个候选值均严格更大，故原稿所述严格改善成立。

## Itemized verification

以下行号均指哈希绑定的 343 行作者稿。

| 项 | 位置与对象 | 结果 | 核查结论 |
| --- | --- | --- | --- |
| 01 | 第 10–58 行，规范、量词与逐系数对象 | PASS | $p\ge5,a\ge2$ 与实际 $\mathcal B_3$ 固定，无规范切换 |
| 02 | 第 62–73 行，接受输入 | PASS | 实际块整性、初值、精确桥和最高项界均明确列出 |
| 03 | 第 84–100 行，形式代入及三角系统 | PASS | 传播子单位不依赖 $L$，常数项独立指定 |
| 04 | 第 119–123 行，实际 $\eta$ | PASS | 可依赖 $L$，没有误当标量或设零 |
| 05 | 第 129–135 行，差方程与 $p$ 倍误差 | PASS | 除 $h^E$ 后误差仍至少在 $h^m$，平方项消失合法 |
| 06 | 第 137–150 行，导数身份与模型剩余 | PASS | 符号、系数与截断次数合法 |
| 07 | 第 152–161 行，完整响应与唯一性 | PASS | $y=\eta T,z=-\eta\mathcal N^2U/2$ 同时匹配方程及初值 |
| 08 | 第 165–176 行，两类真实缺陷 | PASS | 首层均为 $6\chi i$，模 $p$ 与实际模 $h$ 精度衔接正确 |
| 09 | 第 179–186 行，原乘积误差层 | PASS | $E+m=M$，不存在提前丢失实际初值 |
| 10 | 第 188–200 行，两类线性项抵消 | PASS | 完整和含 $i+j=p$，逐 $i$ 消失 |
| 11 | 第 201–206 行，所有剩余提高一阶 | PASS | 二次差及首层余项均至少在 $h^{M+1}$ |
| 12 | 第 212–215 行，低块参数次数 | PASS | 两谐波外部 $x,L$ 权重均正确 |
| 13 | 第 217–221 行，$Y,Z$ 参数次数 | PASS | 零常数模型及平方常数项不突破次数界 |
| 14 | 第 223–233 行，精确模型投影 | PASS | 奇数配对使次数至多 $m$，不是仅模 $h$ 的结论 |
| 15 | 第 239–246 行，非驻值 Euler | PASS | 保留全部传播子缺陷偏导项 |
| 16 | 第 248–255 行，低／第二块权重 | PASS | $(2i-3p)/p=2i/p-3$ |
| 17 | 第 248–255 行，中间及内部权重 | PASS | $(p+i)/p=i/p+1$，内部负号及两个 $p$ 正确 |
| 18 | 第 257–262 行，全部 $R$ | PASS | 前两类在 $h^m$，内部在 $h^{2m+E}$ |
| 19 | 第 266–270 行，$p^2\Phi$ 整性 | PASS | 每类动能与所需势能均先归一化再约化 |
| 20 | 第 272–274 行，动能剩余次数 | PASS | 非内部配对次数至多 $m$，内部剩余零 |
| 21 | 第 276–281 行，准确势能桥 | PASS | 完整保留 $\alpha^2(Y^{\rm act}-1/2)^2/2$ 及 $p\epsilon$ |
| 22 | 第 283–289 行，势能剩余次数 | PASS | 两个端点为 $p-1,p-2$；外部 $L$ 已计入 |
| 23 | 第 291–307 行，先投影再除 $p$ | PASS | 只对高度 $M+1$ 的投影误差除 $p$，不约化非整低项 |
| 24 | 第 304、311–319 行，$S$ 与商同余 | PASS | 高度转移和首一递降正确，$u_0$ 仅声明同余 |
| 25 | 第 321–326 行，负根界 | PASS | 低于最高项部分使用分母 $p-1$，最高项保留更强界 |
| 26 | 第 327–330 行，点值及新端点 | PASS | 首一项唯一最低，仅覆盖严格开端点范围 |
| 27 | 第 331–333 行，新旧根界比较 | PASS | 对原最弱界严格改善，对上一轮不虚称始终严格 |
| 28 | 第 337–338 行，$p=5$ 边界 | PASS | $m=2,M\ge10,E\ge8$；单位分母、三角解与指数带均合法 |
| 29 | 第 337–343 行，科学及产物边界 | PASS | 不声称首层非零、完整 Newton 图、因子型、简单性或 PDF 完成 |

## Exact verification actually run

审查中实际运行一次仅含自由符号的 SymPy 核算，没有逐素数或根扫描。
它独立展开两类配对响应，所得完整和为

$$-6U_iU_j\chi\eta i^2j(i+j).$$

代入 $j=p-i$ 后与 $-6U_iU_j\chi\eta i^2(p-i)p$ 的差为零。
低块、中间块、内部块三个精确 Euler 权重的核算残差均为零。
另检查 $a=2$ 时第一个新根界比值为 $m-1$，第二个比值与其差为
$1/(2m+1)$。这些有限代数核算只防止符号和常数笔误，
一般量词、整性、逐系数高度及根界由上文证明核查承担。

## Corrections or Missing Assumptions

无。没有发现须修改作者稿方能成立的数学错误，也未通过改写作者稿后追认原文。
有限商中超出次数的 $u_s$ 按零系数理解，是正常多项式约定，不是附加假设。

## Open Risks and delivery boundary

- 全部高系数只获得共同下一下界；本件没有计算该层是否存在非零项。
- 最高项更强的 $M-2m$ 界是接受输入，不是本稿重新证明或确定的准确赋值。
- 新端点可能抵消，完整负因子的下凸包、斜率、因子型、简单性及野分裂域仍未闭合。
- 本件审查与其他高系数或最高项作者任务独立；没有读取或拼接并行作者的未接受成果。
- 仅新增本地独审文件；冻结原稿、接受输入、状态文件和 Papers27–29 产物未更改。

最终判定：本次绑定的 HIGH_LAYER PROOF V1 原文可以无修订通过此限定独立审查。
