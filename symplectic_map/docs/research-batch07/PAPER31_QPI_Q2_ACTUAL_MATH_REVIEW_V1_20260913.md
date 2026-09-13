# Paper31 Q2：冻结 M／N 的 actual 独立数学审查 V1

日期：2026-09-13 UTC。审查者：/root/p31_q2_actual_math_review，独立非作者 secondary reviewer。
采用 proof-writer 的证明状态与 research-review 的独立 xhigh 审查流程；本轮为 actual Round 1。
主控已说明使用可用 secondary reviewer 回退，不冒称调用了不可用的 GPT-5.4／外部 MCP。
本件只审查两个冻结短证明；不是来源独查、新意／价值／容量票或正式 Route A/B 评价。
唯一写入文件是本报告；未改作者文件、锁、旧接受产物、项目稿件、索引或 PDF。
未使用 CAS、数值、参数枚举、阶数扫描或外部稿件上传。

## 1. 实际读取、冻结指纹与依赖范围

以下 FULL 均指本人实际读完文件正文，不是只读摘要或依赖主控转述。

| 代号 | 实际文件 | 读取范围 |
|---|---|---|
| M | PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md | FULL，128 行 |
| N | PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md | FULL，238 行 |
| G | PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md | FULL，208 行 |
| B | PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md | FULL，144 行 |
| S | PAPER31_QPI_Q2_STRONG_TARGET_SOURCE_SCREEN_V1_20260913.md | FULL，167 行；仅用于强目标边界 |
| P30 | papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex | PARTIAL，第 1–151、216–238、338–352、428–446 行 |

上述 M、N、G、B、S 均位于 docs/research-batch07/。
M 的 SHA-256：cdf173e47f86f4558ad125c5894f825441449bf4ea6c4c8801d31507e8c53700。
N 的 SHA-256：f50d3291694a6156cac21edfd47af7288ab4fef2b8615c82afe1778471b3d686。
G 的 SHA-256：f0c92b3d03bc1686deb63877777d36c6297efde779d2fc02f81cde4d86e8a196。
B 的 SHA-256：9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d。
S 的 SHA-256：dcee3c53f319f2ecc5b3b65fd021661bfd3d8ee0a7818ff4f5a44f176d5b0465。
P30 的 SHA-256：573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f。
M、N 指纹与本轮指定冻结值一致；P30 的 FULL 文件哈希不代表 FULL 阅读或重验。
本人 FULL 读 /root/autodl-tmp/.codex/skills/proof-writer/SKILL.md 与
/root/autodl-tmp/.codex/skills/skills-codex/research-review/SKILL.md。
消费已接受的原曲面、完整自同构和实分支几何；不重开 P30 构造或旧全局 twist 验收。
S 中外文来源仅为本地筛查记录，本审查没有将其读取冒记为本人外文原文读取。

## 2. 命题、假设、状态与证明依赖图

固定任意 $T>0$；对象始终为原完整实曲面 $U$、原映射 $F$ 与 $\mu=|\Omega|$。
$F(x,y)=(T/(x-y),x/y)$，$h=-x+y+x/y-T/x$，$\Omega=dx\wedge dy/(xy)$，以完整延拓解释缺图点。
$T=w_\pm^3(w_\pm-1)$，$w_-<0$、$w_+>1$，$h_\pm=3w_\pm-2w_\pm^2$，$s_w=(w^2,w)$。
记 $e=h-h_+$、$\varepsilon=h_--h$；$\iota_X\Omega=-dh$，正圆周期为 $L$，$\theta=t/L$。
逐圆均值为 $\Pi f=\int f\,d\theta$，$\mathsf Uf=f\circ F$，相关为 $\langle\mathsf U^n(I-\Pi)f,(I-\Pi)g\rangle$。
原光滑观测是 $C^\infty(U)$ 函数；用于全局范数及相关时取固定紧能窗，或原紧支撑观测。
M 的正交投影结论另对任意 $f\in L^2(\mu)$ 成立，不附加光滑性。
所有渐近均为固定 $T$ 下靠近所标临界值的单侧渐近，不声称参数端点的一致性。
“逐圆”指完整正则实纤维的每个连通圆，不是单仿射图内的开弧。

| 受审结论 | 状态 |
|---|---|
| M：测度、coarea 正号、proper 紧性、terminal 范数接口 | PROVABLE_AS_STATED |
| M：逐圆正交投影、与 Koopman 对易、整纤维中心化反例 | PROVABLE_AS_STATED |
| N：Hessian、乘子、单侧解析对数周期、原 $F^2$ 解析时间提升 | PROVABLE_AS_STATED |
| N：均值可微余项、全部非零 Fourier 双界与加权求和 | PROVABLE_AS_STATED |
| N：非-Hölder 例、面积尾、中心化尾及其截断阶尖锐性 | PROVABLE_AS_STATED |
| N：acnode 消失圆的 $O(\delta^2)$ 尾与持续圆排除项 | PROVABLE_AS_STATED |
| S：完整 Q2-P 最优相关率、振荡主项与全 Fourier 余项 | NOT_PROVED；不属于 M／N 的已证结论 |

证明依赖：P30 原 proper pencil 与 G 的分支分类 $\to$ M 的完整测度／投影；
M 与临界点直接线性化 $\to$ N 的 Morse 周期和原离散位移；
局部积分分解 $\to$ 均值／Fourier 界 $\to$ 尾估计及反例。
B 仅提供持续圆跨 $h_-$ 的解析接口与 $T=3/16$ 的既定 twist jet。

## 3. M：方向、terminal 与真正的紧性

**步骤 M1：原辛形式。** 稠密 torus 上
$\det DF=T/[y^2(x-y)]$，$F_1F_2=Tx/[y(x-y)]$，故 $F^*\Omega=\Omega$。
结合原完整自同构，该恒等式延拓到 terminal；$h\circ F=h$ 亦同。
四图的 $\Omega$ 系数分别为 $-1/(1+ab),1/(T+ab),-1/(T+ab),-1/(1+ab)$。
逐图代入 $h$ 得 M 表内四式；$a=0$ 上 $h_b=-1,1/T,1/T,1$。
所以整条 terminal 都是正则点，包括其能量恰为 $h_\pm$ 的点。

**步骤 M2：相对微分符号。** 令 $A=x(y-1)-Ty/x$。
$\omega=-dy/A$ 且 $h_x=-A/(xy)$，所以 $dh\wedge\omega=dx\wedge dy/(xy)=+\Omega$。
在 $dh\ne0$ 处，相对一形式由此唯一确定，两个 lift 之差是 $q\,dh$。
收缩等式给 $\iota_X(dh\wedge\eta)=-\eta(X)dh$；
采用 $\iota_X\Omega=-dh$，得到 $\eta(X)=1$，没有隐藏的负时间或反向周期。
临界点处不存在满足该等式的光滑总空间 lift，M 已明确排除。
因此正向圆时间 $t$ 给 $d\mu=dh\,dt=L(h)\,dh\,d\theta$。
两圆由实群平移识别，保持 $\omega$，所以其正周期相等。

**步骤 M3：proper 与零测集。** P30 的实际无穷纤维支持恰为 $D$，
故 $U=\bar h^{-1}(\mathbb A^1)$，$h$ 是 proper 映射的基变换。
对实闭有限区间 $J$，$\bar h^{-1}(J)$ 是紧 $S_T(\mathbb R)$ 的闭子集且不交 $D$。
光滑密度在这个紧集上体积有限；这没有使用“每根纤维紧所以映射 proper”的错误推理。
临界纤维除孤立临界点外局部为一维子流形，故为 $\mu$-零集。
紧能窗耗尽也给出所需 $\sigma$-有限性，允许 coarea／Fubini 的 $L^2$ 构造。

**步骤 M4：terminal 坐标范数。** 从 $dh=h_a\,da+h_b\,db$ 得
$\Omega=-(c/h_b)dh\wedge da$，所以 $\eta=-(c/h_b)da$。
在四条 terminal 上准确为 $-da,-da,+da,+da$，与 Hamilton 方向一致。
$D_h=h_b^{-1}\partial_b$、$D_a|_h=\partial_a-(h_a/h_b)\partial_b$ 均正确。
在固定紧小邻域缩小到 $|h_b|$ 有正下界，有限阶范数的双向转换成立。
远离临界能量的紧带用 proper submersion 与非零 $X$ 构造逐分支平凡化；
该结论不提供跨 saddle 的统一归一化角度范数，M 没有越界使用。

## 4. M：投影、对易与反例

圆上的概率均值是常数子空间的正交投影；coarea 逐层积分得全局正交投影 $\Pi$。
Jensen 不等式给 $\|\Pi f\|_2\le\|f\|_2$；临界纤维上的赋值不影响此对象。
对紧支撑 $f$，其能量饱和支撑包含于 proper 原像 $h^{-1}(h(\operatorname{supp}f))$，确实紧。
$F$ 将圆 $c$ 保时间地送到圆 $\sigma(c)$，故两个次序的条件均值相同：
$\Pi\mathsf U f=\mathsf U\Pi f$；不需要假设每圆均被单步保持。
上区间两分支的 $\pm\chi(h)$ 是光滑紧支撑原函数，并有 $\mathsf U f=-f$。
等周期使整纤维均值为零，但相关等于 $(-1)^n\|f\|_2^2$。
下区间相同构造给 $+1$ 本征函数。故 $\Pi$ 的像不是 $F$-不变函数子空间，
“整纤维中心化足够”被反例否定，而逐圆投影正确消除此处两种零模。
$C_n$ 由酉 Koopman、正交投影与 Cauchy–Schwarz 定义良好；此处没有衰减结论。

## 5. N：局部线性化与解析周期

**步骤 N1：直接微分。** N 所列 Hessian 的行列式为 $(3-4w)/w^4$。
在 $w_-<0$ 时首对角元与 $2/w_-$ 都负且行列式正，故为严格局部极大。
在 $w_+>1$ 时行列式负，故为非退化 saddle。
从原符号直接得 $X=(x^2/y-xy,-xy+x+Ty/x)$，其临界线性化正是 N 的矩阵。
该矩阵平方为 $w^2(4w-3)I$，给 $\kappa=w\sqrt{4w-3}>0$。
$w=w_+$ 时记 $\mathfrak a=\operatorname{arcosh}((2w-1)/(2(w-1)))>0$。
恒等式 $DF=(\operatorname{tr}DF)I/2-DX/[2w(w-1)]$ 逐项成立。
在 $DX$ 的 $+\kappa,-\kappa$ 方向，乘子为 $-e^{\mathfrak a},-e^{-\mathfrak a}$；
两者均为负，不能漏掉单步半支翻转。中心频率也确为 $|w_-|\sqrt{3-4w_-}$。

**步骤 N2：对数及其可微余项。** 解析 Morse 坐标取 $e=pq$、
$\Omega=-a\,dp\wedge dq$ 后，$X=(p\partial_p-q\partial_q)/a$。
选择 $p$ 为非稳定轴固定 $a(0)=1/\kappa>0$；$dt=a\,dp/p$ 与正时间相符。
穿箱幂级数中对角项是 $a_{jj}e^j\log(r^2/|e|)$。
非对角项积分的两个端点只产生非负整数次 $e$，在固定符号一侧解析。
取 $r$ 严格小于收敛半径后，系数以几何级数控制，分离出的解析级数及有限阶导数可求和。
外弧无临界点且紧，横截面端点解析，解析流与隐函数定理给外弧时间解析。
G 的 split normalization 去掉两个节点原像后是两条开弧，不存在遗漏的远离节点闭圆。
结合上侧两圆／下侧一圆，上侧每圆穿箱一次、下侧唯一圆穿箱两次。
这证明 $L_\Gamma=m\mathcal A(e)\log(1/|e|)+\mathcal B_\Gamma(e)$，
$m=1,2$ 及 $L'_\Gamma=-m/(\kappa e)+O(\log(1/|e|))$，不是直接微分裸 $O(1)$。

## 6. N：原 $F^2$ 的共同解析时间提升

$F_*X=X$ 来自原两项保持恒等式；完整圆上的 $X$ 无零点，故其流传递且完备。
在 $p=p_0>0$ 的横截面，$p_1(0)>0$；缩小 $p_0$ 使两点和连接正轴弧留在图内。
积分 $\tau(e)=\int_{p_0}^{p_1(e)}a(s,e/s)\,ds/s$ 的分母远离零，真正双侧解析。
它先在二维开流盒上给 $F^2=\phi_X^{\tau(e)}$，而不只在一条曲线上相等。
由于 $X(0)=0$，任意固定有界时间段的流在足够小原点邻域存在；
缩小 $p_0$ 并限制能量，可取包含原点与该流盒的共同连通开域。
两个映射在该域解析，解析恒等定理因此延至原点邻域全部象限，条件满足。
再用与流对易延到每条完整圆；两上侧圆均进此邻域，不能另给它们任意不同的时间提升。
在原点非稳定方向微分，$e^{\kappa\tau(0)}=e^{2\mathfrak a}$，
实指数单射给 $\tau(0)=2\mathfrak a/\kappa>0$；非零整周期添加会发散。
于是 $\alpha=\tau/L$ 的导数主项为 $2\mathfrak a/[m e\log^2(1/|e|)]$，符号正确。
下侧取 $p=\sqrt{|e|},q=-\sqrt{|e|}$：负乘子使 $F$ 换象限，而任意固定有界时间的流仍留在原象限。
因此单步相位的半整数分支为 $1/2+\tau/(2L)$，不能误取仅 $\tau/(2L)$。
本结论是能量依赖时间，未推出常数时间的全局 Hamilton 嵌入。

## 7. N：均值余项、全 Fourier 与投影失正则

本节 $s=s_{w_+}$，令 $b=f-f(s)$；局部 $|b|\le C(|p|+|q|)$，穿箱时间积分及外弧积分均一致有限。
这对任意固定 $r_1\ge1$ 给 $\int|b|^{r_1}dt=O(1)$，从而均值差为 $O(1/L)$。
中心化 $L^1(dt)$ 界用三角不等式，$L^2(dt)$ 界用精确方差恒等式，复值函数也适用。
对 $Q=ba$，Hadamard 分解 $Q(p,q)=Q(p,0)+Q(0,q)+pqR(p,q)$ 精确成立。
轴上两项缺失的小尾长为 $O(|e|)$，导数有界；余项为 $e\int R\,ds/s$。
微分它给 $O(\log(1/|e|))$ 的积分项，以及有界的移动端点项和
$e\int O(1)\,ds/s^2$ 项。因此 $B_f=B_f(0)+O(|e|\log)$、$B_f'=O(\log)$ 成立。
此处只用光滑性，未将光滑观测错误升级为解析观测。
全部 $k\ne0$ 有 $|\widehat f_k|\le C/L$；这来自同一个时间 $L^1$ 界，常数不依赖 $k$。
$X^jf(s)=0$，同一局部估计及周期分部积分给 $|\widehat f_k|\le C_jL^{j-1}|k|^{-j}$。
选整数 $j>s+1$，在 $|k|\le L$ 与 $|k|>L$ 分拆求和，分别得到
$\sum|k|^s|\widehat f_k|=O(L^s)$、$\sum|k|^{2s}|\widehat f_k|^2=O(L^{2s-1})$。
例如相应 $C^{j+1}$ 原坐标范数已足以控制所用常数；没有无限阶范数或固定模量词偷换。
所以 Wiener 范数可一致有界，而角向正整数阶 Sobolev 范数确可由正则弧 bump 实现增长。
非负非零 separatrix bump 给 $B_f(0)>0$；结合上述可微余项得到 N(5.1) 的导数等价式。
在 $p=q=\pm r$ 的对应上侧象限，中心化函数为 $1/\log(1/r)$ 阶，
大于任意 $r^\beta$ 阶；给节点取连续极限零也不能获得正阶 Hölder。
这否定的是投影后保留原光滑类，不是否定投影作为 $L^2$ 算子的合法性。

## 8. N：全能带尾、尖锐性与 acnode 分支

每侧每能量总穿箱次数为二，故总周期密度为 $(2/\kappa)\log(1/|e|)+O(1)$。
两侧积分得到准确全能带系数 $(4/\kappa)\delta\log(1/\delta)+O(\delta)$。
M 的 proper 性保证这是整个原能带，不是删去仿射无穷远后的局部面积。
对中心化原光滑观测，每圆未归一化 $L^2(dt)$ 有界；
$F^n$ 保时间且只可能换圆，逐圆 Cauchy–Schwarz 后对能量积分给所有整数 $n$ 一致的 $O(\delta)$。
一个因子中心化原光滑、另一因子仅有界时，使用前者 $L^1(dt)$ 界也成立。
有界零均值的 $\operatorname{sgn}\cos(2\pi\theta)$ 在 $n=0$ 恢复全面积尾，说明原光滑前像条件不能删除。
正则弧非零 bump 在 $n=0$ 的未归一化方差趋于正平方积分，故给正数乘 $\delta+o(\delta)$。
这只证明对全部 $n$ 一致的截断阶不能改为 $o(\delta)$，并非大 $n$ 相关率下界。
在 acnode，解析 Morse 密度的角积分消去奇次项，给 $L=2\pi/\omega_-+O(\varepsilon)$。
加权平均的一阶观测项角积分消失，故 $\Pi f=f(s_{w_-})+O(\varepsilon)$；
点态偏差为 $O(\sqrt\varepsilon)$，每圆方差为 $O(\varepsilon)$，再积分得 $O(\delta^2)$。
G 保证此消失小圆被原 $F$ 保持。持续的另一圆未被纳入该估计，也不能纳入。
G／B 的持续圆解析延拓及 $T=3/16$ 二次驻点与上述局部尾结论相容。

## 9. Required fixes、余留风险与交付结论

Required fixes：无。M、N 原命题均保持，不需弱化、额外假设或修改作者冻结文件。
本报告将共同解析域、全模求和与可微余项的核验细节写出；这些是原证明已有步骤的闭合，不是新增科学条件。
独立数学结论：M、N 在既定原曲面／已接受几何输入下均为 PROVABLE_AS_STATED。
仍未完成混合能量—角度导数的全 Fourier 估计、截断补区统一常数、完整强相关率、振荡主项及最优性。
薄层尾选取 $\delta(n)$ 不能独自填补这些义务；本轮数学通过不改变 S 中强目标的 NOT_PROVED 状态。
本报告不赋新意、价值、22–30 页内生容量或正式准入票；P31 未准入、旧 FAIL 与批次 4/5 不因本件改变。
