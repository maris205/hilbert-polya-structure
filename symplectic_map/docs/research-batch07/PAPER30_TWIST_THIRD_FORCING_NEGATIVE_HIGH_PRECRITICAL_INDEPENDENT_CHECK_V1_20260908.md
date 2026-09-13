# Paper30：全部高系数预临界段加强的非作者独立审查

日期：2026-09-08。审查者：`negative_high_precritical_review`。
使用 `proof-writer`；本件只审查指定新增数学稿，不编辑作者稿、接受处置或批次状态。
主控与 `negative_subtop_author` 是本加强的作者，其协作核算不计入本独立审查。

## Claim

审查对象为
[全部高系数整个预临界段稿 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_PRECRITICAL_PROOF_V1_20260908.md)，
全文 304 行；读取时 SHA256 为
`7d869eff22fda9975b0da74233c2d93bc962d7ccb91e209e6fbdee32c8c91516`。

对每个素数 $p\ge5$ 和整数 $a\ge2$，固定稿件的实际双谐波规范，令

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=3m+1=m+p,
\qquad E=M-m,\qquad e_*=M-D.
$$

目标为

$$
p[L^j]\mathcal B_3\in h^m\mathcal O^+\quad(m<j\le D),
$$
$$
S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
U_{\rm cl}\equiv a_m=[L^m]S\pmod{h^{M-2m-1}\mathcal O^+[L]}.
$$

结合已经接受的最高商系数界 $v_h([L^p]U_{\rm cl})\ge M-2m$，
推出所有负簇根满足

$$
v_h(\beta)\le-\delta_{\rm pre},\qquad
\delta_{\rm pre}=(M-2m)/p,
$$

且在任意有限扩域内，非零参数 $\ell$ 的赋值满足
$-\delta_{\rm pre}<t=v_h(\ell)\le0$ 时，$v_h(S(\ell))=mt$。

## Status

**PASS — PROVABLE AS STATED。**

原稿的三个主结论原样保留；未发现需要附加假设、缩小量词或修正主张的阻断问题。
本审查不授予其他待审稿接受状态，也不确定共同下界层或最高系数下一层的非零性。

## Assumptions and notation

沿用 $h=2-\zeta-\zeta^{-1}$、$\mathcal O^+=\mathbb Z_p[h]$、
$v_h(h)=1$、$v_h(p)=M$、$L=-h\lambda$、实际辅助幅度 $b=1$。
所有误差为有限参数多项式的逐系数理想包含。

形式低块的实际代入为 $P$；$Y,Z$ 是零常数的单位三角模型；
$Y^{\rm act}_j=pV_{p+j}$、$Z^{\rm act}_j=p^2V_{2p+j}$；
$q=Y^{\rm act}_0$ 是完整的实际 $L$ 多项式，不是常数剩余。
$\mathcal N=x\partial_x$ 只作用于 $x$，因此与乘 $q(L)$ 交换。
正次数算子 $\mathcal D_k$ 的对角元为 $d_{kp+j}(h)$；
辅助方程对常数的零作用不替代真实内部传播子。

只调用以下已接受输入的所需内容：

1. [第二阶乘响应桥](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)：
   式 (12)、(20)—(28)，以及解释这些式子的单位、整性和代入定义。
   调用 $q\in h^E$、$Z^{\rm act}_0\in h^M$、正规化块整、
   实际正次数方程的 $p$ 倍整误差、模型差在 $h^E$、低块导数身份。
2. [一般素数第三 forcing](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)：
   式 (14)—(16)、(19)、(24) 及其紧邻定义，调用准确 Euler 身份和真实 Chebyshev 缺陷。
3. [根簇分离](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md)：
   Step 6—7 及其指向的分解式 (2)—(3)，调用精确模型次数界、
   $P_{\rm cl}\equiv L^m\pmod h$、$\deg U_{\rm cl}=p$ 和商常数为单位。
4. [负端最高项接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_DISPOSITION_20260908.md)：
   第 1—2 节，只调用已接受最高项高度 $M-2m$ 和对照用的旧 $\delta_+$。

没有调用同日 `NEGATIVE_HIGH_LAYER_PROOF` 的加强结论或终审状态；
本稿重述的准确 Euler 代数可由上述已接受身份直接核回。

## Proof strategy and dependency map

1. 从真实 Chebyshev 多项式得到实际 $h^m$ 单缺陷和 $h^{2m}$ 组合缺陷。
2. 用完整 $q(L)$ 及低块导数身份，将实际响应近似精度提高到 $h^M$。
3. 对实际端点的两类线性变化作特征零配对，将完整配对差推到 $h^{M+m}$。
4. 先消去次数至多 $m$ 的模型投影，再对已在 $h^{M+m}$ 的差除以 $p$。
5. 对实际首一分解作高次递降比较，再以单位常数的唯一最低赋值证明根界。

## Proof / itemized audit

### 1. 实际传播子与组合缺陷：PASS

原稿式 (5)—(7) 使用的是完整整数 Chebyshev 多项式。
在特征 $p$ 下令 $z=1+\eta$、$T=z^p$、$u=z^i$，直接相减得到

$$
\delta_i^{\rm low}-\delta_i^{\rm mid}
=-\frac{(T-1)^2(T^2+T+1)}{T^3H}
\left(u+\frac{T^2}{u}\right).
$$

其中 $v_\eta(T-1)=p$、$v_\eta(H)=2$，所以右端至少在 $\eta^{2p-2}$。
左端是 $H$ 多项式；非零最低 $H$ 次项的 $\eta$ 阶恰为其两倍，
故其模 $p$ 位于 $H^{p-1}=H^{2m}$。
整数提升写作 $H^{2m}A(H)+pB(H)$ 后代入 $H=h$，
第二项在 $h^M\subset h^{2m}$，没有将模 $p$ 恒等式当作特征零恒等式。
式 (5) 及两个单缺陷的 $h^m$ 界按相同规则成立。

内部缺陷也可直接核为

$$
d_p-d_{2p}
=-\frac{(T-1)^2(T^2+T+1)}{T^2H},
$$

其模 $p$ 的阶同样至少为 $H^{2m}$，实际提升合法。
以上两条自由有理式已用精确符号约分核验，残差均为零。

### 2. 完整实际初值与 $h^M$ 响应：PASS

低块递推及两次 $\mathcal N$ 导数给出

$$
(\mathcal D_0+J)(1+\mathcal NP)=0,\qquad
(\mathcal D_0+J)\mathcal N^2P=-2K(1+\mathcal NP)^2.
$$

所有恒等式只要求正次数方程；将常数的辅助对角作用设为零与真实初值不冲突。
正次数 $d_{kp+j}(h)$ 的剩余为 $-j^2\ne0$，故三角比较只除以单位。
先得模型近似

$$
Y=-\mathcal NP/2+O(h^m),\qquad
Z=\mathcal N^2P/8+O(h^m).
$$

在第一差方程中，$q(1+\mathcal NP)$ 与 $\Delta Y$ 的常数相同；
它的正次数残差为 $q\Delta_1\mathcal NP\in h^{E+m}=h^M$。
因此 $\Delta Y=q(1+\mathcal NP)+O(h^M)$。

第二差方程的驱动为

$$
-2K(Y-1/2)\Delta Y-K(\Delta Y)^2
=qK(1+\mathcal NP)^2+O(h^M),
$$

因为模型误差乘 $q$ 达到 $E+m=M$，二次差达到 $2E\ge M$。
候选 $-q\mathcal N^2P/2$ 的残差又在 $h^M$，
其零常数与 $\Delta Z_0=Z^{\rm act}_0\in h^M$ 在该理想内一致。
遂得原稿式 (12)。全过程保留 $q(L)$ 的所有系数与有限次数。

### 3. 两种线性配对及全部余项：PASS

固定 $j=p-i$，低／第二块线性差为
$-qi j^2\delta_i^{\rm low}P_iP_j$；
第一／第一块的两个线性交叉项合计为
$-qi^2j\delta_i^{\rm mid}P_iP_j$。
它们在特征零实际环中准确合并为

$$
-qijP_iP_j\bigl(jC_i+p\delta_i^{\rm mid}\bigr),
\qquad C_i=\delta_i^{\rm low}-\delta_i^{\rm mid},
$$

使用整数 $i+j=p$；没有额外外部 $i$，也没有提前置 $p=0$。
本合并式已作独立符号展开，残差为零。
$qC_i\in h^{E+2m}=h^{M+m}$；另一项因含 $p$ 具有更高高度。

遗漏项的完整分类为：响应 $h^M$ 余项乘缺陷；
模型 $h^m$ 误差乘 $q$ 再乘缺陷；两块响应差的二次项乘缺陷。
对应高度分别为 $M+m$、$E+2m=M+m$、$2E+m\ge M+m$。
故 $\mathcal F_{\rm act}-\mathcal F_{\rm mod}\in h^{M+m}$。

模型的精确次数界给
$\deg_L(P_iZ_{p-i}),\deg_L(Y_iY_{p-i})\le m$，
因为 $p$ 为奇数且
$\lfloor i/2\rfloor+\lfloor(p-i)/2\rfloor=m$。
所以 $\Pi_{>m}\mathcal F_{\rm mod}=0$ 是准确恒等式，不只是剩余消失。

### 4. 准确 Euler 重组与保留内部项：PASS

从已接受的 Euler 恒等式乘以 $p$，低／第二块的合并权重
$2i-3p$ 给出 $2i/p-3$；第一块权重 $p+i$ 给出 $i/p+1$。
内部两个指标 $p,2p$ 的总贡献为

$$
-(d_p-d_{2p})(pV_p)(pV_{2p}).
$$

这逐项重现原稿式 (16)—(17) 的 $p^{-1}\mathcal F_{\rm act}+R$，
系数、符号与正规化因子均一致。
前两类 $R$ 在换成模型后被高次投影准确消去，
替换误差为 $h^E$ 乘 $h^m$，在 $h^M$。
内部项没有删除真实传播子；它自身至少在
$h^{2m+E}=h^{M+m}$，只需 $pV_{2p}$ 整。
所以 $\Pi_{>m}R\in h^M$。

### 5. Action 的高次投影：PASS

在 $p^2\Phi$ 的动能中，非内部配对正是 $P_iZ^{\rm act}_{p-i}$
或 $Y^{\rm act}_iY^{\rm act}_{p-i}$ 乘整传播子，模型配对次数至多 $m$。
其高次投影由模型差控制在 $h^E$。
内部配对含 $q(pV_{2p})$，本身就在 $h^E$。

势能所需指数次数为 $3p-1$、$3p-2$，均严格低于 $3p$，
可使用已接受的第二阶乘桥；桥的额外误差为 $p$ 乘整多项式。
实际块换成模型的平方差仍在 $h^E$。
两个模型系数的次数分别至多 $m$、$m-1$；第二个乘外部 $L$ 后至多 $m$。
因此原稿较强结论 $\Pi_{>m}(p^2\Phi)\in h^E$ 得证，
没有沿用仅模 $h$ 的弱界冒充所需高度。

### 6. 先投影、后除 $p$ 的精度：PASS

准确等式在分式域中允许应用 $L$ 的高次投影。
投影先消去整个模型多项式，然后才对已知实际误差除以 $p$：

$$
\Pi_{>m}(p\mathcal B_3)
=-6\Pi_{>m}(p^2\Phi)
+\frac1p\Pi_{>m}(\mathcal F_{\rm act}-\mathcal F_{\rm mod})
+\Pi_{>m}R.
$$

三项高度分别至少为 $E$、$(M+m)-M=m$、$M$。
由于 $E=M-m\ge4m$，主结论成立。
既不需要 $\mathcal F_{\rm mod}/p$ 的低次系数整，
也不对尚未证明整的该低次表达式作剩余约化。

### 7. 首一商的共同高度：PASS

从 $p[L^j]\mathcal B_3\in h^m$ 得
$[L^j]S\in h^{M+m-D}=h^{M-2m-1}$，$j>m$。
在 $S=P_{\rm cl}U_{\rm cl}$ 中，$P_{\rm cl}$ 首一，所有系数整。
依次比较次数 $m+p,m+p-1,\ldots,m+1$，每一步的其他贡献都含已经证明
在该理想内的更高商系数，故全部非恒定商系数继承共同高度。
比较次数 $m$ 得 $u_0-a_m$ 也在该理想内。
这一论证没有将 $u_0$ 与 $a_m$ 写成精确相等。

### 8. 根界、有限扩域和最小参数：PASS

令 $A=M-2m-1$、$B=M-2m$。
对 $1\le j<p$，最保守比值是 $A/(p-1)$；最高项比值为 $B/p$。
两者的差为

$$
\frac{M-2m-p}{p(p-1)}
\ge\frac{2m^2-3m-1}{p(p-1)}>0,
$$

最后一个分子在 $m=2$ 时为 $1$，此后严格递增。
因此允许的半径参数确为 $\delta_{\rm pre}=B/p$。
在 $t>-\delta_{\rm pre}$ 且 $t\le0$ 时，商的所有非恒定项赋值严格正，
单位常数唯一最低，故 $v_h(U_{\rm cl}(\ell))=0$。
又因 $P_{\rm cl}\equiv L^m\pmod h$，其低次项相对 $L^m$ 的赋值差
至少为 $1+(j-m)t>0$；故 $v_h(P_{\rm cl}(\ell))=mt$。
论证适用于任意延拓值群，不要求参数赋值为整数或扩域未分歧。

最小参数 $(p,a)=(5,2)$ 给 $m=2$、$M=10$、$E=8$、$A=5$、$B=6$。
两比值为 $5/4$ 和 $6/5$，故 $\delta_{\rm pre}=6/5$。
所需的 $M\ge2m$、$E+m=M$、$2E\ge M$ 均成立，
正次数传播子均为单位，无临界指标遗漏。新端点仍被正确排除。

## Conditional combined application — 不授予新最高项接受状态

若另一独立审查之后接受最高商系数进一步满足
$v_h([L^p]U_{\rm cl})\ge M-2m+1$，则本件已核实的共同高度可与它合并为

$$
\delta_{\rm new}
=\min\left\{\frac{M-2m-1}{p-1},\frac{M-2m+1}{p}\right\}
=\min\left\{\frac{M-p}{p-1},\frac{M-p+2}{p}\right\}.
$$

相应的无根区间与 $v_h(S(\ell))=mt$ 结论仅需将开放边界换为
$t>-\delta_{\rm new}$；端点仍不包含。
两个候选比值的差为

$$
\frac{M-3p+2}{p(p-1)}.
$$

唯一由第一个比值控制的允许参数是 $(p,a)=(5,2)$，此时
$\delta_{\rm new}=5/4$：若 $p=5,a\ge3$ 则 $M\ge50>13$；
若 $p\ge7$，则 $M\ge p(p-1)/2$，从而
$M-3p+2\ge(p^2-7p+4)/2>0$。
故其他参数均由第二个比值控制。写成上面的最小值公式即可完整涵盖边界。

与已接受旧界

$$
\delta_+=\min\left\{\frac{e_*}{p-1},\frac{M-2m}{p}\right\}
$$

相比，第一个候选增加 $m/(p-1)>0$，第二个增加 $1/p>0$。
因此在这一条件前提成立时，所有允许 $p,a$ 均有
$\delta_{\rm new}>\delta_+$，不需要判断旧最小值由哪一项控制。
这只是两项已给定高度的应用核查，未审核或接受所假设的新最高项证明。

## Exact checks actually run

独立符号核验包括组合 Chebyshev 缺陷、内部缺陷和特征零线性配对，
均以有理式约分或多项式展开得到零残差。
另以精确分数核对 $(p,a)=(5,2),(5,3),(7,2),(11,2)$ 的三种根界；
这些只是代数与边界检查，不替代上述任意素数证明。

核验命令曾在比较两个等价有理式时使用表达式结构相等而触发一次断言失败；
改为约分其差后两条比值差恒等式的残差均为零。
该失败是核验判等方式的问题，没有据此变更作者稿、阈值或数学结论。

## Corrections or missing assumptions

无阻断性修正或新增假设要求。原稿的初值规范、投影顺序、系数层级与开放端点一致。

## Open risks and delivery boundary

- 本件只接受下界与由下界推出的开区间，不证明任何新下界层非零。
- 完整负 Newton 图、准确根赋值、简单性、不可约性与分裂域仍不由本稿推出。
- 条件合并应用必须等待其新最高项输入另审接受，不能倒过来充当该输入的证明。
- 本件不重开未变旧数学，不涉及 Route A/B、论文立项、PDF 或任何外部交付状态。
