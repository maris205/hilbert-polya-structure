# Paper30：高参数分界系数证明 V1 的非作者独立全文核查

日期：2026-09-08。审查者：独立非作者代理 `negative_boundary_high_review`。
本报告只审指定冻结稿及其必要输入；审查者未参与作者稿的撰写、修订或冻结，
不修改作者稿、当前状态文件或其他作者所有文件。

## 1. 冻结绑定与结论

目标文件：[分界高系数作者稿 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_PROOF_V1_20260908.md)。

- 行数：319。
- SHA256：`5d28cd8c32ca64fdcb4d762f4076218fc4dd77f07cd35b5c7b1155aa1c006a07`。
- 核查范围：从 Claim 至 Open risks 全文，及第一内部结构的准确形式身份、
  实际初值界与已接受首一分解中本稿实际引用的部分。
- 方法：按 `proof-writer` 的原主张、依赖、逐步推理与边界核查要求，
  独立重算主要算子式和阶乘正规化；有限符号检查仅作代数交叉检验。

**全文结论：PASS；`PROVABLE AS STATED`。** 对所有素数 $p\ge5$、整数 $a\ge2$，
原主张

$$p[L^p]\mathcal B_3\in h^{2m}\mathcal O^+,\qquad m=(p-1)/2$$

在冻结稿所列同一实际构造下成立；未替换为 $j>p$，也未替换为商的最高系数。
没有发现需要作者修订的实质缺口。本报告的 PASS 只绑定以上哈希，
不提前接受同轮其他稿，不授予新下界层非零、完整负 Newton 图或因子型。

## 2. 主张、输入与依赖边界

记 $M=p^{a-1}m$、$D=p+m$、$e_*=M-D$。审查采用作者规定的
$h=2-\zeta-\zeta^{-1}$、$v_h(p)=M$、$L=-h\lambda$ 及负号传播子
$d_n=(\zeta^n+\zeta^{-n}-2)/h$。辅助幅度仅用于按 $t=bx$、
$u=Lx^2/4$ 分层；实际分支仍取 $b=1$。

核对了[第一内部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
式 (3)、(15)：前者提供逐 $L$ 系数的 $h^mV_p$ 整性；后者准确为

$$\mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L),$$

其中 $R,T\in\mathbb Z_p[L][[H]]$。特别是 $L=0$ 不例外，模 $p$ 后
$\mathcal B_1(H,0)$ 在 $H^m$ 中。不是只读取实际代入后的整性再对 $h$ 微分。

核对了[最高项预临界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md)
中的纯偶规范和准确倍角缩放；本稿所需恒等式又在下文独立重算。
[当前接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_AND_POSTCRITICAL_DISPOSITION_20260908.md)
仅用于条件商转移的首一性、整系数性及已有共同界，不参与本次 $j=p$ 的证明。

依赖图为：实际初值界与支撑排除 $\Rightarrow$ 模 $h^{2m}$ 的辅助替换；
两条分别正规化的阶乘带 $+$ Chebyshev 移位 $\Rightarrow$ 两条 Ward 修正；
第一 forcing 的形式 $H^m$ 整性 $+$ 准确倍角 $\Rightarrow$ 两端点消失。
所有步骤均不依赖同轮上半段或新最高项结论。

## 3. 逐项核查

| 编号 | 项目 | 结论 |
| --- | --- | --- |
| 01 | forcing 指标与商指标准确区分，$j=p$ 对应 $r=p-m=m+1$ | PASS |
| 02 | 齐次提取中的两个真实端点和系数 $-4^{-p}(1,8)$ | PASS |
| 03 | 新截断为 $t^{p+1}=0$，不是沿用 $t^p=0$ | PASS |
| 04 | 第一次实际内部初值全部满足 $v_h(q_{p,k})\ge-m$ | PASS |
| 05 | 第二次纯偶初值界 $-2m$ 与其余共同界 $-3m$ | PASS |
| 06 | 辅助低矩形 $k<p,r<p$ 的系数与所需指数整性 | PASS |
| 07 | 新 $t^p$ 非整带不能污染含实际初值的背景 | PASS |
| 08 | $u^p$ 非整带同样被权重排除，实际差只含一次 $q$ 或两个第一次 $q$ | PASS |
| 09 | 正规化实际差 $p\Delta e$ 的高度 $M-3m\ge2m$ | PASS |
| 10 | 形式整提升、先清 $p$ 后约化、再代入 $H=h$ 的合法性 | PASS |
| 11 | Chebyshev 导数身份与两个准确移位式 | PASS |
| 12 | 第一带的阶乘缺陷为 $1$，乘 $p$ 后高带整 | PASS |
| 13 | 第一带低块、$\mathcal N$ 和 $\mathcal S$ 的导数身份 | PASS |
| 14 | 第一带修正 $\tau=-\mathcal Nw+\lambda Z$ 与 $H^{2m}$ 误差 | PASS |
| 15 | 第一真实端点由 $\mathcal B_1(H,0)$ 的 $H^m$ 整性消去 | PASS |
| 16 | 新 $t^p$ 带的阶乘缺陷准确为 $1/2$ | PASS |
| 17 | 第二高带方程、初值 $\xi_0=0$，未误除 $d_p$ 或遗漏 $d_{2p}$ | PASS |
| 18 | 第二带修正 $\xi=-\Theta W+(\lambda/4)Z_e$ | PASS |
| 19 | 第二端点算子是 $1+\Theta$，而非 $1+2\Theta$ | PASS |
| 20 | 准确倍角缩放 $16/(4-H)$ 与第一 forcing 的连接 | PASS |
| 21 | 第二真实端点消去与原目标合并 | PASS |
| 22 | $H\partial_H$ 仅作用于整形式低块，导数不损失 $H^m$ | PASS |
| 23 | $p=5$、$a=2$ 的边界精度及全部单位分母 | PASS |
| 24 | 原稿末尾条件商转移与未决结论隔离 | PASS |

### 3.1 齐次端点与实际误差（01—09）

第一 forcing 项 $[x^{3p-1}]e^V$ 中取 $L^p$，由 $k+2p=3p-1$ 得
$k=p-1$，缩放为 $4^{-p}$。第二项已含外部 $2L$，所以内部取
$u^{p-1}t^p$，总缩放为 $2\cdot4^{-(p-1)}=8\cdot4^{-p}$。
因此原稿式 (4) 正确，且两端点的指数权重均小于 $3p$。

第一次初值的 $k$ 为奇数且至少为 $1$；由 $b,L$ 齐次性，它们只是
$V_p(1,L)$ 的相应 $L$ 系数乘一个 $4$ 的单位幂，故高度下界为 $-m$。
求第二次非纯偶初值的 forcing 时，指数权重小于 $2p$，不可能含两个第一次初值。
这些位置的幅度次数不超过 $p-1$，并且纯偶次数小于 $p$，背景指数整。
所以 forcing 高度至少为 $-m$，再除以 $d_{2p}$ 的高度 $2m$ 得 $-3m$。
纯偶第二初值的 forcing 本身整，故有更强的 $-2m$。

辅助低矩形的整性应按 $e^W e^{\widetilde V-W}$ 证明：提取 $u^r$ 的
纯偶部分最多用 $r!$，提取 $t^k$ 的另一部分最多用 $k!$，两者均为 $p$-单位。
原稿没有对整个新增 $t^p$ 带作不真实的整性声明。

独立核对其关键支撑：任何第一次初值项至少含一个 $t$，与背景 $t^p$ 带
相乘后不再满足 $k\le p$；第二次初值权重为 $2p$，与该背景相乘权重至少
为 $3p$。背景 $u^p$ 带权重至少 $2p$，也不能与第一次初值同处当前窗口。
两个第一次初值的乘积已有权重 $2p$，其余背景的权重必须小于 $p$，当然整。
这些排除对各次单位传播子的三角归纳保持成立。

因此在权重小于 $3p$ 的窗口内，实际减辅助的指数差可用

$$e^{\alpha\widetilde V}
\left(\alpha\Delta+\frac{\alpha^2}{2}\Delta^2\right),\qquad\alpha=1,2,$$

处理，每个含初值的项都是整系数的初值多项式；只允许一次初值，
或两个第一次初值。最低可能高度分别为 $-3m$ 与 $-2m$，故整体至少为 $-3m$。
清 $p$ 后高度至少 $M-3m\ge2m$，原稿式 (7) 适用于两个实际端点。

### 3.2 形式环、准确移位与阶乘正规化（10—12、16）

对 $p\nmid n$，$d_n(0)=-n^2$ 为 $p$-单位，故其逆在
$\mathbb Z_p[[H]]$ 中。将内部初值指定为零后，低矩形整性和两条高带的
乘 $p$ 整性都能在这个形式环中三角证明，之后才进入
$\mathbb F_p[H]/(H^{2m})$。整数提升的差属于 $p\mathbb Z_p[[H]]$，
实际代入后在 $h^M$ 中；不存在把一个仍含 $p^{-1}$ 的未整量直接约化的问题。

独立重算如下。令 $X=z-z^{-1}$，则 $X^2=H(H-4)$，特征 $p$ 下
$z^p-z^{-p}=X^p$。因而

$$\frac{(z^p-z^{-p})(z-z^{-1})}{H}
=\chi H^m(4-H)^{m+1}=\lambda.$$

与 $C_p=2-H^p$、$C_{2p}=2-4H^p+H^{2p}$ 代入加法公式，得到

$$d_{p+n}-d_n=\frac\lambda2S_n-H^{p-1}-\frac{H^p}{2}d_n,$$
$$d_{2p+n}-d_n=\lambda(1-H^p/2)S_n
+(-2H^{p-1}+H^{2p-1}/2)(2+Hd_n).$$

与冻结稿式 (9)、(10) 一致。另由 $C_n'=-nS_n$ 得
$d_n+Hd_n'=-nS_n$。模 $H^{2m}=H^{p-1}$ 时两个移位分别只余
$\lambda S_n/2$ 与 $\lambda S_n$，同时 $\lambda^2$ 为零。

阶乘正规化的共同依据是：在每个端点所需的整低部分中，指数因子数小于 $2p$。
项数小于 $p$ 时乘 $p$ 后为零；项数为 $p+s$ 时，
$p/(p+s)!\equiv-1/s!\pmod p$。第一带的普通次数至多
$k+p+r<2p$（因 $k+2r<p$）；第二带至多 $p+r<2p$。
因此没有第二个尚未清除的阶乘 $p$。

第一带在 $t^p=0$ 中，相关 Frobenius 项只有纯偶线性项的 $p$ 次幂：
$[u]W=4/(4-H)$，其 $p$ 次幂模 $H^{2m}$ 为 $1$，缺陷即 $u^p$。
第二带在 $u^p=0$ 中，只有 $[t]T=1/2$ 的 $p$ 次幂留下，
其系数模 $p$ 为 $1/2$，缺陷即 $t^p/2$。$\alpha=1,2$ 均满足
$\alpha^p=\alpha$。一次高带响应分别给出

$$p[t^ku^{p+r}]e^{\alpha\widetilde V}
=[t^ku^r]\alpha e^{\alpha w}(\tau-1),$$
$$p[t^pu^r]e^{\alpha\widetilde V}
=[u^r]\alpha e^{\alpha W}(\xi-1/2).$$

以上是先乘 $p$ 后的带恒等式，未预设 $\tau$ 或 $\xi/p$ 的非正规化整性。
单位三角递推从 $\tau_0=\xi_0=0$ 给出所需的 $\tau,\xi$ 整性。

### 3.3 第一带 Ward 修正与端点（13—15）

设 $F=t e^w/2+4u e^{2w}$、$J=t e^w/2+8u e^{2w}$，低方程为
$\mathcal Dw=-F$。直接对低方程作用 $\mathcal N$、$\mathcal S$ 及
$H\partial_H$，分别得到

$$ (\mathcal D+J)\mathcal Nw=-J,\qquad
(\mathcal D+J)\mathcal Sw=-F,$$
$$ (\mathcal D+J)H\partial_Hw=-H\mathcal D'w.$$

所以 $Z=(H\partial_H-\mathcal S)w$ 满足

$$ (\mathcal D+J)Z=-(\mathcal D+H\mathcal D')w
=\mathcal N S_{\mathcal N}w.$$

把 $-\mathcal Nw+\lambda Z$ 代入高带方程
$(\mathcal D_2+J)\tau=J$，由
$\mathcal D_2-\mathcal D=\lambda S_{\mathcal N}$，两个一阶移位项准确抵消；
只余含 $\lambda^2$ 的误差。基带的非恒定权重为 $1,\ldots,p-1$，
对角元为单位，两边常数均为零，三角唯一性合法。

指数回代准确给出

$$-(\alpha+\mathcal N)e^{\alpha w}
+\lambda(H\partial_H-\mathcal S)e^{\alpha w}.$$

在 $\alpha=1,k=p-1,r=0$，基带乘子为 $p$。
余项作用于 $b(H)=[t^{p-1}]e^{w(H,t,0)}=-\mathcal B_1(H,0)$；
模 $p$ 下 $b\in H^m$，$H\partial_H-(p-1)$ 保持此理想，
再乘 $\lambda\in H^m$ 得 $H^{2m}$。第一端点单独通过。

### 3.4 新 $t^p$ 带、倍角及第二端点（17—22）

在 $u$ 次数小于 $p$ 的区域，$p[t^{p-1}u^r]e^{\widetilde V}$ 是 $p$
乘整量，因此在目标精度中为零。第二带递推准确化为

$$ (\mathcal D_{p,e}+8uF_2)\xi=4uF_2,\qquad F_2=e^{2W}.$$

常数由第一次内部初值置零给出，未倒置 $d_p$。对 $1\le r<p$，
$p+2r$ 不被 $p$ 整除，故没有遗漏第二个内部位置。

从纯偶低方程 $\mathcal D_eW=-4uF_2$ 独立求导得

$$ (\mathcal D_e+8uF_2)(-\Theta W)=4uF_2,$$
$$ (\mathcal D_e+8uF_2)(H\partial_H-\Theta)W
=2\Theta S_{2\Theta}W.$$

而 $\mathcal D_{p,e}-\mathcal D_e=\lambda S_{2\Theta}/2$，
所以修正必须是 $\lambda/4$：候选

$$\xi=-\Theta W+\frac\lambda4(H\partial_H-\Theta)W$$

的两项一阶残差为 $-\lambda\Theta S_{2\Theta}W/2$ 与其相反数。
剩余误差含 $\lambda^2$，初值和单位对角元均匹配。对 $\alpha=2$ 回代，
因 $\Theta F_2=2F_2\Theta W$，基带项为 $-(1+\Theta)F_2$。
该算子的 $1$ 来自阶乘缺陷 $1/2$，不能改成另一方向的常数。

准确倍角 $d_{2r}(H)=(4-H)d_r(H(4-H))$ 与单谐波源项 $-x e^{P_0}/2$
给出

$$W(H,u)=\frac12P_0\!\left(H(4-H),\frac{16u}{4-H}\right)\pmod{u^p}.$$

系数 $16/(4-H)$ 由 $(4-H)c/4=4$ 唯一核准，不能混为纯偶线性系数
$4/(4-H)$。全部 $r<p$ 的低偶传播子为单位，于是

$$[u^{p-1}]F_2=-\left(\frac{16}{4-H}\right)^{p-1}
\mathcal B_1(H(4-H),0)\in H^m\mathbb F_p[[H]].$$

取 $r=p-1$ 后，$1+\Theta$ 的端点乘子为 $p$；余项是
$\lambda/4$ 乘保持 $H^m$ 的 $H\partial_H-(p-1)$。
第二端点因此也在 $H^{2m}$ 中。两端点与实际误差合并，得到原 forcing 主张。
所有形式微分只涉及已经证明整的低块；没有在实际商环中定义 $h$ 微分。

### 3.5 最小素数、误差边界和条件商转移（23—24）

当 $p=5,m=2,a=2$ 时，$M=10$，实际替换误差的最低高度是
$M-3m=4=2m$；它足以证明本稿，但不能额外提高一阶。
其他允许参数满足 $M\ge pm\ge5m$。全部常数分母 $2,4$ 是单位；
两个带中用于递推的传播子均已分别核对为单位。

原稿条件应用也通过：若另审接受 $p[L^j]\mathcal B_3\in h^{2m}$ 对
$p<j\le D$，则与本稿合并给 $[L^j]S\in h^{e_*+2m}$ 对 $j\ge p$。
在已接受的 $S=P_{\rm cl}U_{\rm cl}$ 中，$P_{\rm cl}$ 首一且整，次数 $m$。
从最高项向下比较，

$$[L^{m+r}]S=u_r+\sum_{i<m}[L^i]P_{\rm cl}\,u_{m+r-i}$$

中的其余 $u$ 均为已经处理的更高指标。因此对
$m+1\le r\le p$ 得 $u_r\in h^{e_*+2m}=h^{M-m-1}$。
本报告不据此认定条件前提已经通过其他独审。

## 4. 额外有界条件核查：若再合并新最高项，统一负根界

此节是主控另行要求的条件推论核查，不是冻结作者稿的新增无条件结论。
假设除了本稿外，同轮上半段独审接受 $pC_j\in h^{2m}$ 对 $p<j\le D$，
且另一新最高项独审接受 $pC_D\in h^p$，其中 $C_j=[L^j]\mathcal B_3$。
再结合当前已接受的共同下界和单位常数，得到

$$v_h(u_r)\ge
\begin{cases}
M-p,&1\le r\le m,\\
M-m-1,&m+1\le r<p,\\
M-m,&r=p,
\end{cases}
\qquad v_h(u_0)=0.$$

因 $e_*=M-p-m>0$，独立化简给

$$\frac{M-p}{m}-\frac{M-m}{p}
=\frac{(p-m)(M-p-m)}{mp}>0,$$
$$\frac{M-m-1}{p-1}-\frac{M-m}{p}
=\frac{M-m-p}{p(p-1)}>0.$$

所以三个区间的高度/指标比值均受最高项候选
$\delta=(M-m)/p$ 控制，不需为 $p=5$ 另设分段。
若 $t=v_h(\ell)>-\delta$，则每个非恒定项满足
$v_h(u_r\ell^r)>0$，而常数是单位，故 $U_{\rm cl}(\ell)$ 为单位。
于是所有负商根在这些条件成立后满足

$$v_h(\beta)\le-\frac{M-m}{p}.$$

在新端点 $t=-\delta$，常数和最高项仍可能同阶，不能把不等式改为严格根界，
也不能把开区间单位值结论延伸到该端点。此节没有假定新最高层非零。

## 5. 独立符号交叉检查及证据强度

审查者另以整数 Chebyshev 递推生成 $C_n,S_n,d_n$，对
$p\in\{5,7,11,13\}$、所有 $1\le n<3p$ 核查：

- $d_n+Hd_n'=-nS_n$ 在有理多项式环中准确成立；
- 原稿式 (9)、(10) 乘单位 $2$ 后在 $\mathbb F_p[H]$ 中的完整残差为零，
  并非仅截断至本稿精度后为零。

本次检查全部通过，执行过程退出码为 $0$。它验证有限代数样本，
不是全部素数结论、形式整性或实际误差估值的替代；后者由前述一般推导核查。

## 6. 未决项与最终处置建议

没有需要修正的数学缺口，建议接受冻结稿的原样主张
$p[L^p]\mathcal B_3\in h^{2m}\mathcal O^+$。
仍未证明新高度层非零、准确负 Newton 图、负因子分解或简单性。
条件应用须等待各自条件输入的独立审查和主控处置，不能从本报告自动取得接受状态。
本报告不修改既有失败记录、冻结稿、锁或已接受产物，也不产生任何外部效力。
