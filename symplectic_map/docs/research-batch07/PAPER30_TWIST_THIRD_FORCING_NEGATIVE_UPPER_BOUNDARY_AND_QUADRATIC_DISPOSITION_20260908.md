# Paper30：上半高系数、分界系数及最高项二次临界边界的接受处置

日期：2026-09-08。
状态：`NEGATIVE_UPPER_BOUNDARY_AND_TOP_QUADRATIC_ACCEPTED; NEGATIVE_FACTOR_OPEN`。
主控已全文读取三份新作者稿及三份非作者独立报告。本件只接受下列数学结论，
不授予论文立项、PDF 验收或 Route 状态。

## 1. 本轮实际系数结论与准确范围

对所有素数 $p\ge5$、整数 $a\ge2$，保持同一双谐波实际分支、固定参数、
传播子负号与 SUM action。令

$$m=(p-1)/2,\quad M=p^{a-1}m,\quad D=p+m=3m+1,\quad e_*=M-D,$$
$$C_j=[L^j]\mathcal B_3,\qquad
S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
U_{\rm cl}=\sum_{r=0}^{p}u_rL^r.$$

这里 $v_h(h)=1$、$v_h(p)=M$；已接受的 $P_{\rm cl}$ 首一、次数 $m$，
全部系数整且剩余为 $L^m$；$U_{\rm cl}$ 次数 $p$，$u_0$ 为单位。
上一轮共同结论 $pC_j\in h^m\mathcal O^+$（$j>m$）保持接受。
三项新结论分别为

$$\boxed{
\begin{aligned}
pC_j&\in h^{2m}\mathcal O^+&& (p<j\le D),\\
pC_p&\in h^{2m}\mathcal O^+,\\
pC_D&\in h^{2m+1}\mathcal O^+=h^p\mathcal O^+.
\end{aligned}}$$

第一项不能自行包含边界 $j=p$；第二份证明保留新的辅助幅度带，才补上该边界。
$C_p$ 不是最高 forcing 系数 $C_D$，也不是商的最高系数 $u_p$。
第三项包含完整二次临界贡献，统一覆盖 $p=5$，不只是线性截断。

从最高次数向下比较 $S=P_{\rm cl}U_{\rm cl}$，第一、二项给
$u_r\in h^{e_*+2m}$ 对 $m+1\le r\le p$。
第三项另用首一性给 $u_p=h^{-D}p^2C_D\in h^{M-m}$。
因此当前共同已证界准确为

$$\boxed{v_h(u_r)\ge
\begin{cases}
M-p,&1\le r\le m,\\
M-m-1,&m+1\le r<p,\\
M-m,&r=p.
\end{cases}}$$

已接受同余 $U_{\rm cl}\equiv a_m=[L^m]S\pmod{h^{M-p}}$ 保持，
没有证明 $u_0=a_m$ 的精确等式。
上半商系数旧高度 $M-p$ 至 $M-m-2$ 的各层及最高项另至 $M-m-1$ 的各层均已消失；
若某一所述层区间为空，则不附加内容。
当前三个首个可能高度 $M-p$、$M-m-1$、$M-m$ 均未证明非零。

## 2. 统一负根界和点值范围

令

$$\delta_{\rm neg}=\frac{M-m}{p}.$$

因为 $e_*=M-p-m>0$，有

$$\frac{M-p}{m}-\delta_{\rm neg}
=\frac{(p-m)e_*}{mp}>0,\qquad
\frac{M-m-1}{p-1}-\delta_{\rm neg}
=\frac{e_*}{p(p-1)}>0.$$

所以对任意有限扩域中的非零 $\ell$，若 $t=v_h(\ell)>-\delta_{\rm neg}$，
全部非恒定项 $u_r\ell^r$ 的高度严格为正，而常数项为单位。于是

$$\boxed{v_h(U_{\rm cl}(\ell))=0\quad(t>-\delta_{\rm neg}),\qquad
v_h(\beta)\le-\frac{M-m}{p}\quad(U_{\rm cl}(\beta)=0).}$$

合并条件已在分界稿独审第 4 节核查；三项输入现均已独审并被主控接受。
不需要为 $(p,a)=(5,2)$ 另设分段，此时新界为 $\delta_{\rm neg}=8/5$。
对上一轮

$$\delta_{\rm old}=\min\{(M-p)/(p-1),(M-p+2)/p\},$$

有 $\delta_{\rm old}\le(M-p+2)/p$，且
$\delta_{\rm neg}-(M-p+2)/p=(m-1)/p>0$。
因此对全部允许参数，新界均严格加强上一轮。

合并既有正簇距离式，令 $t_*=(m-1)/m$、正簇根为 $\alpha_1,\ldots,\alpha_m$。
完整点值式现在对 $t>-\delta_{\rm neg}$ 有效：

$$v_h(S(\ell))=
\begin{cases}
mt,&t<t_*,\\
(m-1)t_*+\max_jv_h(\ell-\alpha_j),&t=t_*,\\
m-1,&t>t_*.
\end{cases}$$

$\ell=0$ 时为 $m-1$；根处允许无穷值。
历次旧负端点，包括最初的 $-e_*/p$ 和上一轮的 $-\delta_{\rm old}$，现在均已包含；
新端点 $-\delta_{\rm neg}$ 仍排除。在新端点，常数与最高项可能同阶，不能由上述论证判定单位性。
实际换算保持 $v_h(\mathcal B_3)=D-2M+v_h(S)$、
$v_h(V_{3p})=m+1-2M+v_h(S)$。正簇根、距离与循环分裂域没有改变。

## 3. 新证明机制和独立证据

上半段证明在辅助幅度次数小于 $p$ 的有限区域工作，保留第一次内部初值的
$-m$ 界与第二次内部初值的 $-3m$ 界。实际与零初值辅助分支的正规化差
达到 $M-3m\ge2m$；只在证明该差足够小后使用辅助方程。
准确 Chebyshev 移位和形式 Ward 恒等式将整个线性移位端点压缩到第一 forcing
的形式 $H^m$ 整除身份，得到全部 $p<j\le D$ 的 $h^{2m}$。

分界稿另保留辅助幅度次数恰为 $p$ 的带。两个真实端点为
$t^{p-1}u^p$ 与 $t^pu^{p-1}$，正规化阶乘缺陷分别为 $1$ 与 $1/2$；
相应 Ward 修正因子分别为 $\lambda$ 与 $\lambda/4$。
第二端点的低带算子是 $1+\Theta$，准确倍角缩放为 $16/(4-H)$。
完整支撑排除保证新增非整带不会使实际比较失去高度，最小参数的等号误差边界也合法。

最高项稿先把完整线性端点写成
$-\lambda(H\partial_H-m)B_{\rm low}$；第一 forcing 的形式身份
使它落在 $H^{2m+1}$。随后保留准确移位中的 $-4H^{2m}$ 和线性响应的二次反馈，
求解两条有限响应并计算完整端点。其一般有限和身份为

$$\mathfrak c_2=2p\{p^2H_2-4pH_1+8pH_o-4m\},$$

其中 $H_1=\sum_{k=1}^m1/k$、$H_2=\sum_{k=1}^m1/k^2$、
$H_o=\sum_{r=0}^{m-1}1/(2r+1)$，全部分母均为 $p$ 单位。
故二次临界端点也消失。有限参照和全部实际误差控制恰覆盖模 $h^p$，
不因该形式闭式额外含 $p$ 就外推更高实际高度。

| 新证据 | 非作者独审与处置 |
| --- | --- |
| [上半高系数稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_HIGH_CRITICAL_PROBE_V1_20260908.md)及[独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_HIGH_INDEPENDENT_CHECK_V1_20260908.md) | 544 行作者稿、296 行全文独审；PASS，原范围 $p<j\le D$ 不变 |
| [分界高系数稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_PROOF_V1_20260908.md)及[独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_INDEPENDENT_CHECK_V1_20260908.md) | 319 行作者稿、300 行独审；24 项 PASS，另核条件商转移与统一根界 |
| [最高项二次边界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md)及[独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_INDEPENDENT_CHECK_V1_20260908.md) | 658 行作者稿、502 行独审；30 项 PASS，接受模 $h^p$ 的原样主张 |

三份冻结稿均无需数学修订。最高项稿一处引用标签写首内部稿式 (2)，
本轮实际需要且各审查者直接读取的是该稿式 (15) 的形式整除身份；
原独审第 11—12 项也已确认此身份。本件澄清定位，不改写冻结稿。
作者协作、主控推导、自由符号核算与固定五边界表不计非作者独审；
符号核算也不替代一般证明、整性或真实误差。

本轮直接证据 SHA256：

| 文件 | SHA256 |
| --- | --- |
| UPPER_HIGH 作者稿 | `a1788d54a7e400c688c47af00e4f6bbab413b56fbfc1f137a446f17c1492ec77` |
| UPPER_HIGH 独审 | `32559226f73277901893d73dd6cc8b93b3b22f3294d18dd0c4a2a780563f6f33` |
| BOUNDARY_HIGH 作者稿 | `5d28cd8c32ca64fdcb4d762f4076218fc4dd77f07cd35b5c7b1155aa1c006a07` |
| BOUNDARY_HIGH 独审 | `fe3eb5e989825996b08c155e7548269e1934a10b2ffc208bd04e13360c6a36a3` |
| TOP_SECOND_POSTCRITICAL 作者稿 | `e754946905524581d55cbf1d893c8141db7fc69a1aa33050d778c1754bf789a2` |
| TOP_SECOND_POSTCRITICAL 独审 | `456c84b54febc0b37e379eb966d3ccb623509f6f54caf46ff3618188ba25de01` |

## 4. 下一项的充分条件与尚未完成的证明

下一步优先确定实际剩余 $\overline{h^{-p}pC_D}$。这是当前未知，不是假定的非零锚点。
下述仅为条件推论，并已另经非作者有界只读核查：如果该剩余非零，则
$v_h(u_p)=M-m$；上面两个严格比值不等式使全部中间点严格高于端点连线。
于是完整负 Newton 图恰为

$$\text{条件：}\quad (0,0)\longrightarrow(p,M-m),\qquad
v_h(\beta)=-(M-m)/p.$$

由于 $p\mid M$ 且 $0<m<p$，有 $\gcd(p,M-m)=1$。
若存在次数 $0<d<p$ 的 $K^+$ 因子，其常数项与首项的赋值差是整数，
却又是全部 $d$ 个根的赋值之和 $-d(M-m)/p$，矛盾。
故在同一非零条件下，$U_{\rm cl}$ 不可约；特征零再给可分。
这说明非零最高层足以闭合单边、准确根赋值与不可约性，不必预先求完每个中间系数。
目前该条件未证明，不能把这些条件结论登记为已闭合；根间距与野分裂域亦不随之自动得到。

下一精度需要重计有限参照从 $h^p$ 起的实际误差、准确移位中的非恒定二次项，
以及同精度的响应。已经消失的 $h^{2m}$ 二次边界包括 $p=5$ 在内，不再列为 OPEN。
全局 $R_{m+1,0}$ 极部仍未求出，但已不是本次有限端点证明的必要依赖。
若最高层继续消失，再依据相关低段 $M-p$、上段 $M-m-1$ 与最高项新高度决定下一条边。

## 5. 保留证据与交付边界

[上一轮共同高项及后临界处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_AND_POSTCRITICAL_DISPOSITION_20260908.md)
及全部原证明、独审保持不变；其被加强的下界不等于原结果失败。
[更早最高项处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_DISPOSITION_20260908.md)
中原模 $h$ 稿的非整约化错误、原稿字面 FAIL 与后继修复保留，不追认原稿全文 PASS。
旧次高替代推导仍是作者状态，本轮新自含证明不依赖其取得全文独审。
[原负因子边界处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_FACTOR_DISPOSITION_20260907.md)
的 DVR 反例仍说明：只给下界不能无条件确定完整 Newton 图。

负因子的准确赋值、完整 Newton 图、因子型、简单性、根间距与野分裂域仍未无条件闭合。
一般第二／第三 forcing 互素、完整素数幂 $C,Q$、其他合数与全实根也未因此完成。
Papers27–29 的已接受产物、正文 22–30 页及新意／容量要求不变；
Batch07 本地验收仍为 **3/5**，Paper30 未立项，Paper31 未开展。
本轮没有投稿、上传、对外消息、Route 评分、论文试写或旧构建重跑。
