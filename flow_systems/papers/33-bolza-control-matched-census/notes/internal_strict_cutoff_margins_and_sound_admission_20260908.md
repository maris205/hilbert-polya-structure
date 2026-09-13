# P33 内部理论：严格 cutoff 余量与固定对象的可靠 admission

日期：2026-09-08 UTC。本轮只新增内部数学笔记，不运行数值矩阵程序、普查、实验、BP／CP producer 或 checker，不修改任何旧文件、冻结输入、正式状态或 Stage 5／6 边界。`Lambda=21/10`、两张真实曲面、曲率负一的基底测地长度、原磁场参数 `b=1/2` 和 owner 定义均保持不变。

核心增量是一个**固定对象的证书稳定性定理**：前轮两个真实短字不只满足严格 cutoff；它们还有显式有理数余量，足以保证所有正确绑定、正确包围且达到指定宽度的区间证书都给出同一正面 admission。另给出两因子矩阵近似的可核查误差预算。定理量化的是同一精确对象的证书表示，不是邻近曲面族；近似矩阵只是计算代理，不能替换真实群元素。

## 1. 复用的精确前提与证明责任

本轮复用[前轮分离笔记][previous]的 §2–5：

- Bolza 冻结矩阵与 Ebbens 等人的 `g=2` 模型逐项对应，其全局 systole 为 `2 arcosh(1+sqrt(2))`。来源是前轮实际核读的 [Bolza 作者稿][bolza-source] Theorem 2 及模型段落，本轮不重新访问。
- 控制的冻结参数为 `u=e^(-1/10)`、`x=u^2=e^(-1/5)`。S01 的参数域、几何构造及带标记群对应把精确矩阵识别为闭亏格二曲面群。来源是前轮实际核读的 [S01 作者稿][control-source] §2、Eqs. (10)–(18)，本轮不重新访问。
- 精确词 `w_1=g_0 g_3`、`w_2=g_1 g_2^(-1)` 已按矩阵乘法证明同迹，并由带标记群的整数同调向量 `(1,0,0,1)`、`(0,1,-1,0)` 证明本原、各自非自逆且属于两个不同的外部逆元配对 owner。

这些是本轮的精确语义前提，记为 `E_geom/word/owner`。特别是带标记群对应为外部几何输入，不是由有限精度矩阵、一个近似 relator，甚至一个精确 relator 单独推出的忠实性定理。

记正迹与 cutoff 迹为

\[
t=\operatorname{tr}(w_1)=\operatorname{tr}(w_2)
=\frac{2}{2x-1},\qquad
\tau=2\cosh(\Lambda/2),\qquad \Lambda=\frac{21}{10}.
\tag{1}
\]

上述正迹由精确公式确定。对这些精确 `SU(1,1)` 双曲元，`ell=2 arcosh(t/2)`；这里不把一个近似矩阵的实迹自动当成真实曲面闭轨道的长度。

## 2. 两侧的显式严格余量

### 2.1 控制短字的迹区间

令 `r=1/5`。Taylor 的 Lagrange 余项分别给出

\[
1-r+\frac{r^2}{2}-\frac{r^3}{6}
<e^{-r}<1-r+\frac{r^2}{2}.
\]

左式省略项的四阶余项为正，右式三阶余项为负。因此

\[
\frac{307}{375}<x<\frac{41}{50},\qquad
\frac{239}{375}<2x-1<\frac{16}{25},\qquad
\boxed{\frac{25}{8}<t<\frac{750}{239}.}
\tag{2}
\]

前轮的正项级数比较还给出

\[
\frac{16}{5}<\tau<\frac{1600}{359}<\frac92.
\tag{3}
\]

于是两种不同的余量都有明确下界：

\[
t-2>\frac98,\qquad
\tau-t>\frac{16}{5}-\frac{750}{239}
=\boxed{\gamma_C:=\frac{74}{1195}}>0.
\tag{4}
\]

实际上 `16/5-t>gamma_C`，所以控制 admission 可以使用精确有理数下栅栏 `16/5`，不必数值计算 `cosh(21/20)`。区间

\[
I_x^0=\left[\frac{307}{375},\frac{41}{50}\right],\qquad
I_t^0=\left[\frac{25}{8},\frac{750}{239}\right]
\tag{5}
\]

已经是本文以解析不等式证明的包围区间；它们不是一次未执行的 interval 程序的输出。

### 2.2 Bolza 的全局排除余量

记

\[
\beta=2\cosh\!\left(\frac{\operatorname{sys}(S_B)}2\right)
=2(1+\sqrt2).
\]

由于 `(7/5)^2<2<(3/2)^2`，

\[
\frac{24}{5}<\beta<5,\qquad
\boxed{\beta-\tau>\frac{24}{5}-\frac92
=\gamma_B:=\frac3{10}.}
\tag{6}
\]

这里 `beta` 是由全局 systole 定理得到的**所有非平凡闭测地线的绝对迹下界（或正迹 lift 的迹下界）**，不是某个生成元的迹。如果只验证若干矩阵的迹大于 cutoff，不可复用本节的全局结论。

### 2.3 换回真实长度的保守余量

这些迹余量还给出长度余量，而不需要浮点 `arcosh`。令 `F(z)=2 cosh(z/2)`，则 `F'(z)=sinh(z/2)`。对控制短字，`0<ell<Lambda`，故由前轮的 `cosh(21/20)<800/359` 及中值定理，

\[
\tau-t<\frac{800}{359}(\Lambda-\ell),\qquad
\boxed{\Lambda-\ell>\frac{359}{800}\gamma_C
=\frac{13283}{478000}.}
\tag{7}
\]

对 Bolza，`F'(z)<beta/2<5/2` 在 `[Lambda,sys(S_B)]` 上成立。因此

\[
\boxed{\operatorname{sys}(S_B)-\Lambda
>\frac25\gamma_B=\frac3{25}.}
\tag{8}
\]

它们只是保守的严格余量，不是最优 systole 估计，也不把原有 cutoff 改成一个可调参数。

## 3. 区间接口：包围、绑定与判断须分别成立

以下区间端点取精确有理数。所谓 `I_z=[L_z,U_z]` 是 `z` 的**有效证书**，要求两件事同时成立：

1. 对象绑定：`z` 指向本节明示的同一冻结几何、同一词及同一规范化下的精确实数，而非另一个接近的模型。
2. 包围证明：`L_z<=z<=U_z` 有可检查的数学或经验证的向外舍入依据。文件自报的误差、仅显示若干小数位、或一个 containing-zero residual 都不等于包围证明。

在 `E_geom/word/owner` 已成立时，可以采用以下严格分支：

\[
\begin{array}{ll}
\mathsf{Admit}:& 2<L_t\ \text{且}\ U_t<L_\tau,\\
\mathsf{Outside}:& L_t>U_\tau,\\
\mathsf{Undetermined}:& \text{其余情形。}
\end{array}
\tag{9}
\]

`Admit` 证明该精确词为 cutoff 内双曲元；连同精确 owner 责任才证明一个本原 owner 的正面存在性。`Outside` 证明这个精确词严格在 cutoff 外，不证明其他词都在外。`Undetermined` 是该接口尚未判定，不是负面结果。

当使用已证明的 `16/5<tau` 时，`U_t<16/5` 可直接替代第一行的 `U_t<L_tau`。因为原 cutoff 为 `ell<=Lambda`，真正等于边界的情况若要 admission，须有另行的精确等号证据；不能用微调 cutoff 或放松严格测试填补它。本轮两个词有正余量，故不涉及这个边界分支。

## 4. 固定对象的证书稳定性定理

**定理 1。** 固定 `E_geom/word/owner` 中的真实对象，不作任何几何扰动。对每个有效区间记其宽度 `d_z=U_z-L_z`。

**(a) 控制迹与阈值同时近似。** 若

\[
d_t+d_\tau\le\gamma_C,
\tag{10}
\]

则 (9) 必给出 `Admit`。若阈值直接使用有理下栅栏 `16/5`，只需 `d_t<=gamma_C`。

**证明。** 对任何包含 `t` 的区间，`U_t<=t+d_t`、`L_t>=t-d_t`；相同事实适用于 `tau`。由 (4)，

\[
L_\tau-U_t
\ge\tau-t-d_t-d_\tau>0.
\]

同时 `d_t<=gamma_C<9/8`，所以 `L_t>=t-d_t>25/8-gamma_C>2`。使用有理下栅栏时，`U_t<=t+d_t<750/239+gamma_C=16/5`。□

**(b) 参数区间足够精细。** 若 `I_x=[a,b]` 是同一精确 `x=e^(-1/5)` 的有效区间，且

\[
d_x\le\delta_x:=\frac{307}{375}-\frac{13}{16}
=\frac{37}{6000},
\tag{11}
\]

则

\[
\frac{13}{16}<a\le x\le b
<\frac{41}{50}+\frac{37}{6000}
=\frac{4957}{6000}<1.
\]

因 `f(y)=2/(2y-1)` 在 `(1/2,1)` 上严格递减，

\[
t\in\left[\frac{2}{2b-1},\frac{2}{2a-1}\right]
\subset\left(2,\frac{16}{5}\right).
\tag{12}
\]

因此两个词均通过严格 admission。这里区间中的其他数不是新的允许输入；(12) 只是用一个单调函数包围同一精确 `t`。证明中的端点界由 `a>=x-d_x`、`b<=x+d_x` 和 (2) 直接得到。□

**(c) Bolza 的全局排除。** 若 `I_beta` 是同一全局 systole 迹 `beta` 的有效区间，且

\[
d_\beta+d_\tau\le\gamma_B,
\tag{13}
\]

则 `L_beta>U_tau`。连同全局 systole 前提，可以排除该 Bolza 模型所有 cutoff 内的非平凡闭测地线。

**证明。** `L_beta-U_tau>=beta-tau-d_beta-d_tau>0`。每条非平凡闭测地线的绝对迹至少为 `beta`，所以不可能满足 `abs(trace)<=tau`。□

**(d) 证书收敛与细化。** 若同一精确对象的一系列有效区间宽度趋于零，则 (10)、(11)、(13) 的相应充分条件最终满足；这不要求区间嵌套。若另有嵌套细化，已经通过 (9) 的严格不等式会保持成立。前者给出有限精度后的必然判定，后者给出已接受判断的细化稳定性。两者都以每次包围及绑定有效为前提；不保证任意未实现的数值程序会产出这些区间。

本定理不提供全部候选的统一精度界，亦不承诺 cutoff 边界上的区间比较终止。它仅处理这里已证明具有严格余量的两个控制短字及 Bolza 的全局 systole 排除。

### 4.1 宽度不是半径

若报告形式为 `z_hat +/- e_z`，其区间宽度是 `2e_z`。于是得到以下无需硬件假设的充分预算：

| 证书形式 | 足够条件 | 所保证的判断 |
| --- | --- | --- |
| 固定 `x` 的中心与误差半径 | `e_x<=37/12000` | 经 (12) 对两个词作 admission |
| 固定 `t` 的中心与误差半径，使用 `16/5` 下栅栏 | `e_t<=37/1195` | 两个词的严格 admission |
| 同时近似 `t` 与 `tau` | `2e_t+2e_tau<=74/1195` | (9) 的严格 admission |
| 同时近似全局 `beta` 与 `tau` | `2e_beta+2e_tau<=3/10` | Bolza 全局排除 |

例如 `e_x<=1/512` 足够，因为区间宽度至多 `1/256<37/6000`。这些是**交付的已证误差界**，不是“某种硬件设置为若干位就自动正确”的承诺。将点估计误差直接当成整个区间的宽度会少计一个因子二。

## 5. 两因子矩阵近似如何进入同一预算

本节给出固定短字的符号误差传播，不执行数值矩阵程序。沿用前轮

\[
\Delta=(1-x)(2x-1),\qquad \nu=-\Delta^{-1/2},\qquad
A=x+i(1-x).
\]

由 (2)，

\[
\Delta>\frac9{50}\frac{239}{375}
=\frac{2151}{18750}>\frac19.
\tag{14}
\]

故 `abs(nu)<3`。又 `u<1`、`abs(A)^2=x^2+(1-x)^2<1`，所以 `g_0,g_1,g_3,g_2^(-1)` 的每个精确 entry 的绝对值均小于 3。

**命题 2（有界的两因子 trace 误差）。** 对上述任一个真实词写 `w=BC`。设近似因子 `B_hat,C_hat` 与同一精确 `B,C` 的每个 entry 的复数绝对误差均不超过 `epsilon`。设交付的实数 `t_hat` 与 `Re tr(B_hat C_hat)` 的误差不超过 `eta`，其中 `eta` 必须覆盖乘法、加法及输出的全部舍入误差。则

\[
|\widehat t-t|\le E:=24\epsilon+4\epsilon^2+\eta.
\tag{15}
\]

**证明。** `tr(BC)` 是四个乘积 `B_ij C_ji` 之和。每项的误差至多

\[
|B_{ij}|\epsilon+|C_{ji}|\epsilon+\epsilon^2
\le6\epsilon+\epsilon^2.
\]

四项相加，再加入 `eta` 即得 (15)。精确矩阵已属 `SU(1,1)`，故其迹为实数；取近似迹的实部不会增大误差。证明没有把近似因子本身假定为 `SU(1,1)` 元素。□

一个具体而保守的充分预算为

\[
\epsilon,\eta\le\frac1{1024}.
\]

因 `4epsilon^2<=epsilon`，

\[
E\le\frac{26}{1024}=\frac{13}{512}
<\frac{37}{1195}=\frac{\gamma_C}{2},
\tag{16}
\]

最后比较为 `13*1195=15535<18944=37*512`。因此有效区间 `[t_hat-E,t_hat+E]` 的宽度严格小于 `gamma_C`，定理 1(a) 保证 admission。该论证同时适用于两个词，不依赖具体浮点近似结果。

这里有三项不能省略：`epsilon` 必须是正确的 entry 包围界；`eta` 必须覆盖实际采用的运算路径；第二个词的第二因子必须绑定精确 `g_2^(-1)`。若仅输入 `g_2` 的近似再调用普通数值求逆，不能无证明地沿用相同的 `epsilon`。本节未选择 interval 库、实现向外舍入或产生生产证书；它规定实现若要使用本预算，至少必须证明什么。

## 6. 为什么数值接近不能补出模型责任

### 6.1 接近群元素，甚至严格属于 ambient 群，仍不足够

对某个真实正迹 `W=w_i`，取任意小的实数 `s>0`。矩阵 `W+sI` 任意接近 `W`，但

\[
\det(W+sI)=1+s\operatorname{tr}(W)+s^2>1.
\]

它不是 determinant-one 的精确元素。当 `2s<gamma_C` 时，其迹仍小于 `16/5`；因此一个很小的群条件 residual 加上短迹，不足以产生一个真实闭轨道。区间包含 `det=1` 也不表示区间内的所有矩阵都满足该等式。

即便另外精确强制 ambient `SU(1,1)` membership，仍未证明属于固定的离散曲面群 `Gamma_C`。令

\[
K_s=\begin{pmatrix}\cosh s&\sinh s\\\sinh s&\cosh s\end{pmatrix}.
\]

当非零 `s` 足够小时，由 `Gamma_C` 的离散性，`K_s` 的 projective 类不属于 `Gamma_C`；否则将有非平凡群元素趋近恒等元。于是 `K_s W` 不属于 `Gamma_C`，但仍精确属于 `SU(1,1)`，并因连续性保持迹在 `(2,16/5)` 内。这是固定对象周围的逻辑反例，不是对项目输入实施扰动。

因此，entry 区间只能包围一个已通过精确词／模型绑定指定的对象，不能自行回答固定 lattice membership。

### 6.2 精确 relator 仍不等于忠实标记

取一个纯逻辑反例

\[
H=\begin{pmatrix}\sqrt5/2&1/2\\1/2&\sqrt5/2\end{pmatrix}
\in\mathrm{SU}(1,1).
\]

向循环群 `<H>` 定义标记生成元的像：

\[
g_0\mapsto H^2,\quad g_1\mapsto H,\quad
g_2\mapsto H^{-1},\quad g_3\mapsto I.
\tag{17}
\]

这些像两两交换；前轮曲面 relator 中每个生成元指数和为零，所以 relator **精确**成立。但

\[
w_1\mapsto H^2,\qquad w_2\mapsto H^2,\qquad
\operatorname{tr}(H^2)=(\operatorname{tr}H)^2-2=3<\frac{16}{5}.
\]

两个不同抽象同调向量在此表示下成为同一个 proper power。由此可见，“精确群条件 + 精确 relator + 短迹”也不能替代忠实的几何／标记对应，不能把抽象同调的本原性直接转到任意表示的像。

此反例不是锁定模型，也不声称接近锁定模型；它仅反驳删除 `E_geom/word/owner` 前提后的错误推论。

## 7. 未命中、未判定与完整普查仍不等价

在**同一真实控制模型**中，考虑一个仅含两个词 `w_1^2,w_2^2` 的假设性候选集，不实际执行它。由 determinant-one 恒等式及 (2)，

\[
\operatorname{tr}(w_i^2)=t^2-2
>\frac{497}{64}>\frac92>\tau.
\tag{18}
\]

若只筛选这两个原字本身，一个正确的长度分类器会拒绝候选集的全部元素；它们另也是 proper powers。然而前轮已证明真实 cutoff owner 集至少有两个元素。这说明，即使对给定候选全部得到确定的负判断，“零命中”仍不能证明真实 owner 集为空。若 producer 另行取根并纳入候选，须明确这一步及其覆盖证明；那不再是只筛选上述两个原字的情形。反例不否认正确取根算法的作用。

本轮的证明责任分工如下：

| 层 | 本轮提供的数学增量 | 未完成的具体义务 |
| --- | --- | --- |
| 模型与标记 | 明示复用的精确几何前提，并给出删除前提的反例 | 正式源／定理版本绑定和既有合同要求的独立 replay；S02 的历史一手访问缺口不变 |
| 局部长度 admission | 有理迹与长度余量；区间稳定性；两因子误差预算 | 实际 interval 实现、运算路径误差证明、parser、proof adapter 及 checker 执行 |
| 本原与 owner 分离 | 精确保留前轮两个词的同调证明；数值精度不改变该责任 | 一般候选的完整群 root／conjugacy／inverse 分类 |
| 全局覆盖与输出 | Bolza 全局 systole 的条件排除；明确正面见证只给下界 | BP／CP 生产输出、控制中心 guard、FIFO 覆盖、边分类、完整 owner 流与零 unresolved ledger |

这些义务仍由[现有 BP 合同][bp-contract]和 [CP 合同][cp-contract]约束。本笔记不给 observed digest，不把数学条件稳定性记成一次生产通过，不把两个见证改写成恰有两个 owner，不改变算术性判断、Route 状态、systole 混杂结论或 Stage 5／6 停止条件。

## 8. 实际动作与来源限制

本轮按 ARS argument-builder 分开来源输入、本文推导、反例及未完成义务；没有开启 full pipeline、正式审稿或外部模型调用。开始前读取当前 `AGENTS.md`、`docs/workflow.md`、所选 ARS 入口／workflow／角色，以及前轮笔记；取得前轮笔记、当前稿件、两个合同和三个冻结输入共七项 SHA-256 快照。

本轮没有新增网络访问、API 请求或上传。前轮 Bolza Lemma 9 的 PDF 文本提取不一致、截图失败及 DOI 打开失败均按[前轮记录][previous]保留；本轮不重试、不把它们改写成成功访问，也不使用那段未图像核对的局部计算。

本地写入仅为 `apply_patch` 新增和修订本文件。写后只读比对确认上述七项 SHA-256 与写前一致；`node -e` 文本检查确认五个引用定义、六处引用使用、全部本地引用目标、29 对显示数学分隔符、连续 (1)–(18) 公式标签和控制字符检查均通过。只读定位、字节保全及文本结构检查不等于数学或独立科学认证。没有运行数值矩阵、长度、枚举、旧 fixture、历史 artifact writer 或生产实验；数学结论交接主线只读复核。

[previous]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_cutoff_separation_proof_obligations_20260908.md
[bp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
[cp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[bolza-source]: https://arxiv.org/pdf/2103.05960
[control-source]: https://arxiv.org/pdf/1301.5446
