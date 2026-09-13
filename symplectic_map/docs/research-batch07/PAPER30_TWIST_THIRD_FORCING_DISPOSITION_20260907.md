# Paper30：第三 forcing 的准确首层与三的幂局部根结构

日期：2026-09-07。
状态：TWIST_THIRD_FORCING_LOCAL_RESULTS_ACCEPTED_FULL_PRIME_POWER_OPEN。

本轮完成此前指定的第三 forcing 首个非零层，并提取三的幂五系数已确定的局部根结构。
一般素数与三的幂边界分别证明、分别审查，仍属于同一个实际双谐波分支；
没有拼接不同构造。此前第二阶乘带、前两个内部层及分母 $p,2p$ 的
已接受结论不重开。

## 1. 对象与统一规范

固定奇素数 $p$、$a\ge2$ 及任意本原 $p^a$ 次根 $\zeta$，沿用

$$
h=D_1=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,\quad
m=(p-1)/2,\quad M=p^{a-1}m,\quad \chi=(-1)^{m+1}.
$$

实际局部赋值为 $v_h(h)=1,v_h(p)=M$。
实际分支和传播子仍是
$V_n=\rho^nv_n(L/\rho)$、$d_n=-D_n/h$，
满足 $d_nV_n=-[x^{n-1}]e^V/2-L[x^{n-2}]e^{2V}$。

只用实际前缀 $n<3p$ 定义

$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}.
$$

此定义不需要 $V_{3p}$。若 $3p<p^a$，才可进一步用
$V_{3p}=\mathcal B_3/(2d_{3p})$。
所有首层同余均指整系数多项式的完整剩余，而不是有限参数采样。

## 2. 接受的三个准确端点

| 范围 | forcing 的准确首层 | 内部模态结论 |
| --- | --- | --- |
| $p\ge5,\ a\ge2$ | $\overline{h^{-(3m+1)}p^2\mathcal B_3}=-3\chi L^m/64$ | $\overline{h^{-(m+1)}p^2V_{3p}}=\chi L^m/384$ |
| $p=3,\ a\ge3$ | $\overline{h^{-7}\,9\mathcal B_3}=1+L$ | $\overline{h\,9V_9}=1+L$ |
| $p=3,\ a=2$ | $\overline{h^{-8}\,9\mathcal B_3}=1$ | $d_9=0$；真共振处不定义 $V_9$ |

每个被取剩余的归一化多项式均已证明整。
因此三个范围的 $\mathcal B_3$ 都不是零多项式。

当 $p\ge5$ 时，逐系数最小赋值恰为

$$
v_h^{\mathrm{coeff}}(\mathcal B_3)=3m+1-2M,\qquad
v_h^{\mathrm{coeff}}(V_{3p})=m+1-2M.
$$

对任意有限局部扩域中的整参数 $L$，若 $\bar L\ne0$，
两式也是点值的准确赋值；若 $\bar L=0$，仅无条件得到严格大于相应基线。
在分歧扩域中不能自动把严格不等式提升为整整一阶。

此外，由旧第一内部 forcing 的全部根均为整单位且满足
$\bar L^m=2$，新第三 forcing 在那些根处有非零剩余，故

$$
\boxed{\gcd(\mathcal B_1,\mathcal B_3)=1\qquad(p\ge5).}
$$

这不是 $\gcd(\mathcal B_2,\mathcal B_3)=1$，也不是完整周期首项的 $C,Q$ 互素。

当 $p=3,a\ge3$ 时，逐系数最小赋值分别为 $7-2M$ 与 $-2M-1$。
在 $\bar L\ne2$ 时点值达到这两个基线；$\bar L=2$ 类由第5节的距离公式完整表达。
当 $p=3,a=2$ 时，常数单位首层给出每个有限扩域整参数处
$v_h(\mathcal B_3(L))=2$，没有参数例外。

## 3. 一般素数的实际误差桥及高阶取消

[第二阶乘响应桥](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)
保留形式变量 $H$ 的全部依赖，证明完整第二阶乘带的误差属于 $p$ 倍形式整环。
实际第一、第二块分别是 $Y_j^{\rm act}=pV_{p+j}$、
$Z_j^{\rm act}=p^2V_{2p+j}$；实际内部初值没有置零。

零初值形式模型只用于比较，原始逐系数差为 $O(h^{M-m})$；
乘端点配对缺陷后才获得 $O(h^M)$。
不能把未乘缺陷的块误差直接写成 $O(h^M)$。

[一般第三端点证明](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)
从正号 action 的准确 Euler 身份出发，将端点重组为配对传播子缺陷与两个
耦合块响应的有限和。二、三阶展开同时保留低块自身的一阶 $H$ 响应。
普通层、候选 $m$ 与 $2m$ 层以及 $3m$ 层的取消均由身份承担；
首个留下的层是 $3m+1$，不是通过观察或目标零点拟合选定。

最终系数化为 $-3L^m/512$，再乘规范化缺陷的立方首项得到
$-3\chi L^m/64$。自由符号身份只验证代数运算，
全部素数与指数的适用性由单位递推、有限次数和误差估计证明。
真实 $d_{3p}/h^{2m}$ 的剩余是 $-9$，因此模态首层的分母为 $384$。

## 4. 三的幂：有限证书、真共振及保留的失败

[三的幂边界 V2](PAPER30_TWIST_THIRD_FORCING_THREE_POWER_BOUNDARY_PROBE_V2_20260907.md)
从原递推完整保留 $V_3,V_6$，计算 $G(L)=9\mathcal B_3(L)$ 的五个有理系数。
当 $a\ge3$、$M=3^{a-1}\ge9$ 时，准确系数赋值为

$$
(v_h(g_0),\ldots,v_h(g_4))=(7,7,M+6,M+5,M+6).
$$

所有指数的结论来自完整分子的一致唯一最低项不等式，不是指数扫描外推。
此时 $v_h(d_9)=8$，不能沿用前两个内部传播子的高度二。

当 $a=2$ 时，在准确三次数域关系
$h^3-6h^2+9h-3=0$ 下约化，五系数赋值为 $(8,9,11,10,10)$。
正号 action 恒等式给出 $G=-162\Phi_9$；这不使零传播子变得可逆。

[V1 原稿](PAPER30_TWIST_THIRD_FORCING_THREE_POWER_BOUNDARY_PROBE_V1_20260907.md)
曾错误地把任意有限分歧扩域中的正赋值推成至少一。
非作者审查给出 $\tau^2=h,\ L=2+\tau$ 的实际代数反例，
使 $v_h(h^{-7}G(L))=1/2$。
V2 仅将全扩域例外剩余类的界修正为严格不等式；
未分歧扩域保留整阶加强。V1 与失败记录完整保留，
未把失败追记为通过，未重跑未变的五系数证书。

## 5. 五系数的直接 Newton／局部根推论

本节只读取上述已审系数，不新增递推或根扫描。
[限定独审补充](PAPER30_TWIST_THIRD_FORCING_THREE_POWER_NEWTON_INDEPENDENT_ADDENDUM_20260907.md)
核查了下列新推论；原14项报告及证书保持冻结；新补审推进其中保留的局部根问题，不追记为旧14项内容。

当 $p=3,a\ge3$ 时，$G=9\mathcal B_3$ 的完整 Newton 多边形为

$$
(0,7)\longrightarrow(1,7)\longrightarrow(4,M+6).
$$

因此一个根的 $L$ 赋值为零，另外三个为 $-(M-1)/3$，均计重数。
剩余 $1+L$ 的简单根提升为唯一整根 $\alpha\in\mathcal O^+$，
$\bar\alpha=2$。剩下的三次因子不可约：
任一根的赋值分母为三，因为 $3\nmid M-1$；
其根域的分歧度至少为三，最小多项式不可能有小于三的次数。
故原四次多项式分解为线性因子乘不可约三次因子，所有根简单。

更精确地，令 $S=h^{-7}G$，则
$S=(L-\alpha)\mathcal U(L)$，$\mathcal U\in\mathcal O^+[L]$、
$\overline{\mathcal U}=1$。对任何有限局部扩域中的整参数，

$$
v_h(\mathcal B_3(L))=7-2M+v_h(L-\alpha),\qquad
v_h(V_9(L))=-2M-1+v_h(L-\alpha),
$$

其中 $\alpha$ 处取 $+\infty$。
这补齐了整参数例外类的精确距离表达；不再把该类的根数、简单性或点值结构列为 OPEN。
它不提供 $\alpha$ 的进一步显式展开或与其他 forcing 根的关系。

当 $p=3,a=2$ 时，完整 Newton 多边形为

$$
(0,8)\longrightarrow(4,10).
$$

四个根均满足 $v_h(L)=-1/2$，没有整根。
冻结的 $g_4$ 最低项为 $(27\cdot47567/8)h$，
所以 $\overline{g_4/h^{10}}=1$；边剩余为 $1+Y^2$，在 $\mathbb F_3$ 上不可约。
对任一根 $\beta$，$Y=h\beta^2$ 的剩余满足此二次式；
赋值与剩余分别强制根域 $e\ge2,f\ge2$。
其次数至多四，故四次多项式不可约，每个单根生成的域有 $e=f=2$，
所有根简单。这里不声称整个分裂域也有同样的 $e,f$。

该真周期九子情形还满足
$\gcd(\mathcal B_2,\mathcal B_3)=1$：
原递推的参数次数界给出 $\deg_L\mathcal B_2\le3$，
旧第二 forcing 结论保证它非零，而 $\mathcal B_3$ 是不可约四次。
此论证不适用于一般 $p\ge5$ 或 $p=3,a\ge3$ 的同一互素问题。

## 6. 独立核查与交付身份

[一般素数端点与响应桥联合独审](PAPER30_TWIST_THIRD_FORCING_GENERAL_AND_BRIDGE_INDEPENDENT_CHECK_20260907.md)
完成 **18 项限定检查，全 PASS，无新增假设或修订要求**。
非作者审查独立重建准确 $Q$ 耦合、正 action、四项端点、下一 $H$ 响应、
非零 $p[x^p]w$ 边界和完整同阶项，并核实所有实际误差及点值量词。
主控已全文读取640行响应桥、843行一般作者稿及465行联合独审。

[三的幂非作者核查](PAPER30_TWIST_THIRD_FORCING_THREE_POWER_BOUNDARY_INDEPENDENT_CHECK_20260907.md)
完成 14 项检查：V2 全部通过，无剩余阻断；V1 的分歧扩域量词项明确 FAIL。
审查者独立生成实际前八模态、逐项核对五个完整有理身份、
全部最低点与三次数域约化，并核对真周期九 action；
不是执行作者代码后转述状态。

主控与一般端点作者共推的身份属于作者证据，不计作独立审查或多个贡献。
本轮按 proof-writer 分离了实际误差桥、准确首层、参数点值与真共振边界。
没有新增素数、本原根、分母或参数根扫描，没有重跑旧诊断，
没有目标拟合、参数偷换、Route 评价或对外操作。

主控另已全文读取714行三的幂 V2、384行原独审及135行新推论补审。
三的幂新推论来自已核系数，未再次运行有限递推。
新补审确认了根域而非分裂域的分歧／剩余次数、全扩域整参数距离公式，
以及仅限真周期九的第二／第三 forcing 互素。

| 本轮冻结输入 | SHA256 |
| --- | --- |
| SECOND_FACTORIAL_RESPONSE_BRIDGE V1 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |
| THIRD_FORCING_GENERAL_PRIME V1 | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |
| GENERAL_AND_BRIDGE INDEPENDENT_CHECK | `7615f13eb979bf6d2e893fcfdfe7aca785e4419c763a6055198c2eb72ce17f80` |
| THREE_POWER_BOUNDARY V1（保留失败） | `c5b0fd1dbe4c69859f7bb209a1d6f437b1d5267588955a1eededde14e085ec79` |
| THREE_POWER_BOUNDARY V2 | `643417e53df99921f003d42763e021fc8abbe2c0ca6ae83eead8b1675fab42fd` |
| THREE_POWER_BOUNDARY INDEPENDENT_CHECK | `5fa612351b1ed2e7d685aa498edcdefb984a5c17c87a529e1f056fbdc4cde354` |
| THREE_POWER_NEWTON INDEPENDENT_ADDENDUM | `dbb0f3fedaaab5110ecdbb376776af349d8fed34137839cd90cae72575bc3361` |

## 7. 下一准确缺口与批次状态

第三 forcing 的首个非零层及第二阶乘响应桥不再 OPEN。
三的幂两支的完整 Newton 多边形、所述局部因子型与简单性也不再 OPEN；
$a\ge3$ 的全部整参数点值已有精确距离公式，真周期九与第二 forcing 已互素。

下一有界对象是一般 $p\ge5$ 第三 forcing 的零剩余根簇：
确定下一 Newton 层、分裂与简单性，并补齐非整参数根分支。
一般 $p\ge5$ 与非真共振三的幂的 $\mathcal B_2,\mathcal B_3$ 互素性仍待证明；
三的幂根的进一步展开、与其他 forcing 的实际根关系及实嵌入下结构另行区分。
这些局部结论不完成后续内部／非内部层，也不证明完整周期首项的全局结论。

完整 $C_{r,p^a}$ 的结构、简单性与 $C,Q$ 互素，
其他合数分母及实际参数根的全实性仍未完成。
[前两个内部层](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_DISPOSITION_20260907.md)、
[第二阶乘带](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_DISPOSITION_20260907.md)、
[全部奇素数](PAPER30_TWIST_PRIME_COMPLETE_NONVANISHING_DISPOSITION_20260907.md)与
[全部两倍奇素数](PAPER30_TWIST_TWO_PRIME_COMPLETE_DISPOSITION_20260907.md)
按各自原范围保持接受，不将内部结果代替完整首项。

整体新意和自然正文容量尚未最终认证。不估页、不投正式候选票、不试写测页；
没有 Paper30 项目或 PDF。Batch07 仍为 **3/5**，
Paper30 未立项，Paper31 未开展；22–30 页实质正文、完整证明与独立验收要求不变。
本处置仅更新当前范围与下一缺口，保留所有冻结作者稿、失败记录和旧接受产物。

