# Paper30：第三 forcing 的全部高系数首层消失

日期：2026-09-08。作者：主控。当前为待独立核查的作者证明。

本件使用 `formula-derivation` 固定端点 Euler 身份及实际误差的推导对象，
再使用 `proof-writer` 完成下面的精确命题。未修改任何已接受原稿。

## Claim / Target

固定任意素数 $p\ge5$、整数 $a\ge2$，在当前双谐波模型、实际规范和
同一 SUM action 下，令

$$m=(p-1)/2,\quad M=p^{a-1}m,\quad D=3m+1,\quad e_*=M-D.$$

则第三 forcing 的每一个高于正簇次数的系数均满足

$$\boxed{p[L^j]\mathcal B_3\in h\mathcal O^+\qquad(m<j\le D).}\tag{1}$$

等价地，设 $S=h^{-D}p^2\mathcal B_3=\sum_j a_jL^j$，则

$$a_j\in h^{e_*+1}\mathcal O^+\qquad(j>m).\tag{2}$$

已接受唯一分解 $S=P_{\rm cl}U_{\rm cl}$ 的商因此满足

$$\boxed{U_{\rm cl}\equiv a_m\pmod{h^{e_*+1}\mathcal O^+[L]}.}\tag{3}$$

若 $U_{\rm cl}=\sum_{r=0}^p u_rL^r$，结合已接受的最高项界
$v_h(u_p)\ge M-2m$，定义

$$\delta_1=\min\left\{\frac{e_*+1}{p-1},\frac{M-2m}{p}\right\}.$$

每个负簇根 $\beta$ 均有 $v_h(\beta)\le-\delta_1$，且

$$v_h(S(\ell))=m\,v_h(\ell)\qquad
(-\delta_1<v_h(\ell)\le0).\tag{4}$$

这里 $\ell$ 为任意有限扩域中的非零代数参数。新端点不包含在式 (4) 内。
本件不声称任何一个高系数在这个新的下界层非零。

## Status

证明分类：`PROVABLE AS STATED`。推导分类：`COHERENT AS STATED`。
这两项是作者状态，不替代真正非作者审查和后续接受处置。

## Assumptions and exact inputs

取本原 $p^a$ 次根 $\zeta$，令

$$h=2-\zeta-\zeta^{-1},\quad K^+=\mathbb Q_p(h),\quad
\mathcal O^+=\mathbb Z_p[h],\quad v_h(h)=1,\quad v_h(p)=M,$$
$$\rho=-h,\quad L=\rho\lambda,\quad\chi=(-1)^{m+1},\quad
d_n(h)=(\zeta^n+\zeta^{-n}-2)/h.$$

所有整性和理想均逐 $L$ 系数解释。剩余域为 $\mathbb F_p$。
实际分支 $V=\sum_{1\le n<3p}V_nx^n$ 满足

$$d_n(h)V_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},$$
$$\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}.\tag{5}$$

只调用下列已接受输入中与本件有关的部分；不重开未变证明：

1. [第二阶乘带处置](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_DISPOSITION_20260907.md)：
   $V_i$ 对 $i<p$ 整，$pV_{p+j}$、$p^2V_{2p+j}$ 对 $0\le j<p$ 整，
   $pV_p\in h^{M-m}\mathcal O^+[L]$，$pV_{2p}\in\mathcal O^+[L]$。
2. [第二阶乘带响应桥 V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)，
   式 (12)、(20)—(28)：准确的 $p$ 倍整误差、形式零常数模型和实际初值。
3. [一般奇素数第三 forcing V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)，
   式 (14)—(17) 及 Step 3：准确非驻值 Euler 身份、两种配对缺陷的首层。
4. [根簇分离 V1](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md)，
   固定次数唯一分解、$P_{\rm cl}$ 首一次数 $m$、$U_{\rm cl}$ 次数 $p$、
   $a_m$ 为单位以及形式模型的参数次数界。
5. [负端最高项处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_DISPOSITION_20260908.md)：
   只在根界应用中调用 $v_h(u_p)\ge M-2m$。

这些旧输入不包含式 (1)：原实际／模型比较只到 $h^{M-m}$，
乘配对缺陷后只到 $h^M$，此前据此不能除以 $p$ 再得到零剩余。

## Invariant object, notation and strategy

推导对象始终为实际 $p\mathcal B_3$ 的高次投影
$\Pi_{>m}p\mathcal B_3$，其中 $\Pi_{>m}$ 删除 $L$ 次数不超过 $m$ 的项。
不是以形式模型的低次数代替实际多项式。

设 $E=M-m$。低块形式解记为
$P(H,x)=\sum_{i=1}^{p-1}P_i(H,L)x^i$，满足 $P_i(h,L)=V_i$。
它在 $\mathbb Z_{(p)}[L][[H]][x]/(x^p)$ 中定义。
令 $\mathcal N=x\partial_x$，并置

$$J=\frac x2e^P+2Lx^2e^{2P},\qquad
K=\frac x4e^P+2Lx^2e^{2P}\pmod{x^p},$$
$$\mathcal D_kx^j=d_{kp+j}(H)x^j\quad(1\le j<p;\ k=0,1,2).$$

模型 $Y,Z$ 的常数项为零，其正次数满足

$$ (\mathcal D_1+J)Y=J/2,\qquad
(\mathcal D_2+J)Z=-K(Y-1/2)^2\pmod{x^p}.\tag{6}$$

实际块则为 $Y^{\rm act}_j=pV_{p+j}$、$Z^{\rm act}_j=p^2V_{2p+j}$。
在本文的算子方程中，常数项单独指定；不向实际内部模式强加模型方程。
无常数项的乘法系数 $J,K$ 使其正次数递推为单位三角系统。

证明依赖链如下：

1. 求出实际／模型差在 $h^E$ 层的完整响应，包括实际非零初值。
2. 两类配对缺陷分别乘此响应；其 $h^{E+m}=h^M$ 层逐项抵消。
3. 在准确 Euler 身份中，先投影掉模型的低次数项，再除以 $p$。
4. 单独检查 action 的 $p^2$ 归一化剩余次数及全部精确余项。
5. 用首一因子作从高到低的系数比较，得到商和负根界。

下文每一步均为身份或命题及其证明，没有模型近似。

## Proof

### Step 1. 实际／模型差的首个可能层

响应桥给出 $\Delta Y=Y^{\rm act}-Y(h)\in h^E$、
$\Delta Z=Z^{\rm act}-Z(h)\in h^E$。令

$$\eta=\overline{h^{-E}Y^{\rm act}_0}\in\mathbb F_p[L],\quad
y=\overline{h^{-E}\Delta Y},\quad z=\overline{h^{-E}\Delta Z}.$$

这里不需要计算 $\eta$，也不假设它是常数。
因 $Z^{\rm act}_0\in h^M$、$M-E=m\ge2$，有 $y_0=\eta$、$z_0=0$。

令 $U=\overline{P(h,x)}$，$J_0=\overline{J(h,x)}$、$K_0=\overline{K(h,x)}$，
$\mathcal O=-\mathcal N^2+J_0$。所有这些对象先仅在 $x$ 次数小于 $p$ 内使用。
正次数上的三个传播子模 $h$ 均为 $-j^2$，因为 $p=0$ 于剩余域。

从响应桥的准确实际方程减去式 (6) 的实际代入，除以 $h^E$ 后约化。
其 $p$ 倍整误差高度为 $M$，高于 $E$，所以消失。
平方差中的 $\Delta Y^2/h^E$ 也消失，因为 $E\ge4m\ge8$。
因此正次数上有

$$\mathcal O y=0,\qquad
\mathcal O z=-2K_0(\bar Y-1/2)y,\tag{7}$$

其中 $\bar Y=\overline{Y(h)}=-\mathcal NU/2$，
$\bar Z=\overline{Z(h)}=\mathcal N^2U/8$。
这两个模型剩余由未移位低块的缩放导数身份和单位三角唯一性得到。

具体地，低块满足 $-\mathcal N^2U+xe^U/2+Lx^2e^{2U}=0$。
对它施加 $\mathcal N$，再利用
$\mathcal N(xe^U/2+Lx^2e^{2U})=J_0(1+\mathcal NU)$，得到

$$\mathcal O\mathcal NU=-J_0.$$

令 $T=1+\mathcal NU$，则 $\mathcal O T=0$。
又由 $\mathcal NJ_0=2K_0T$ 得到

$$\mathcal O\mathcal N^2U=-2K_0T^2.\tag{8}$$

$\bar Y-1/2=-T/2$，所以式 (7) 的解为

$$\boxed{y=\eta T,\qquad z=-\frac\eta2\mathcal N^2U.}\tag{9}$$

前式的常数为 $\eta$，后式常数为零；式 (8) 检查方程的右侧为
$\eta K_0T^2$。每个正次数对角元 $-j^2$ 可逆，故这确是唯一解。
对 $1\le i<p$，记 $U_i=[x^i]U$，从而

$$\bar Y_i=-\frac i2U_i,\quad\bar Z_i=\frac{i^2}{8}U_i,
\quad y_i=\eta iU_i,\quad z_i=-\frac\eta2 i^2U_i.\tag{10}$$

### Step 2. 两种端点配对的实际误差提高一阶

定义实际整系数缺陷

$$\delta_i^{\rm low}=d_i(h)-d_{3p-i}(h),\qquad
\delta_i^{\rm mid}=d_{p+i}(h)-d_{2p-i}(h),\quad1\le i<p.$$

已接受的真实 Chebyshev 缺陷计算给

$$\delta_i^{\rm low},\delta_i^{\rm mid}\in h^m\mathcal O^+,
\qquad\overline{h^{-m}\delta_i^{\rm low}}
=\overline{h^{-m}\delta_i^{\rm mid}}=6\chi i.\tag{11}$$

额外的 $p$ 倍系数高度至少为 $M>m$，不影响此实际约化。
对整块 $A,B$ 定义

$$\mathcal F(A,B)=\sum_{i=1}^{p-1}
\left(2i\delta_i^{\rm low}P_i(h)B_{p-i}
+i\delta_i^{\rm mid}A_iA_{p-i}\right).$$

记 $\mathcal F_{\rm act}=\mathcal F(Y^{\rm act},Z^{\rm act})$，
$\mathcal F_{\rm mod}=\mathcal F(Y(h),Z(h))$。
原界已给 $\mathcal F_{\rm act}-\mathcal F_{\rm mod}\in h^M$。
现在计算除以 $h^M=h^{E+m}$ 后的剩余。

固定 $i$ 并置 $j=p-i$。低／第二块的线性差贡献是

$$2i(6\chi i)U_i\left(-\frac\eta2j^2U_j\right)
=-6\chi\eta i^2j^2U_iU_j.$$

中间配对的两个线性差贡献之和是

$$i(6\chi i)\left[
\left(-\frac i2U_i\right)(\eta jU_j)
+(\eta iU_i)\left(-\frac j2U_j\right)\right]
=-6\chi\eta i^3jU_iU_j.$$

两者之和为 $-6\chi\eta i^2j(i+j)U_iU_j=0$，因为 $i+j=p$。
二次差贡献至少在 $h^{2E+m}$，而 $2E+m\ge M+1$。
各首层响应或缺陷的余项也至少在 $h^{M+1}$。
因此逐系数得到新的准确理想包含

$$\boxed{\mathcal F_{\rm act}-\mathcal F_{\rm mod}
\in h^{M+1}\mathcal O^+[L].}\tag{12}$$

此取消不依赖 $\eta$ 的取值，也未把实际内部模式改为零。

### Step 3. 模型配对的参数次数界是精确界

低块递推给 $\deg_LP_i(H,L)\le\lfloor i/2\rfloor$。
可直接逐阶核查：$xe^P$ 的第 $i$ 项次数至多 $\lfloor(i-1)/2\rfloor$，
$Lx^2e^{2P}$ 的第 $i$ 项次数至多 $1+\lfloor(i-2)/2\rfloor$；
传播子不依赖 $L$，故单位除法保持界。

$J_i,K_i$ 的次数至多 $\lfloor i/2\rfloor$。
式 (6) 的三角递推因而给
$\deg_LY_i,\deg_LZ_i\le\lfloor i/2\rfloor$：
每个乘积中各 $x$ 下标之和为 $i$，相应次数的向下取整之和不超过该界。
平方 $ (Y-1/2)^2$ 的常数项不会改变此性质。

配对的两个正下标之和为奇数 $p=2m+1$，所以

$$\left\lfloor\frac i2\right\rfloor+
\left\lfloor\frac{p-i}{2}\right\rfloor=m.$$

缺陷不依赖 $L$，从而有精确身份

$$\deg_L\mathcal F_{\rm mod}\le m,
\qquad\Pi_{>m}\mathcal F_{\rm mod}=0.\tag{13}$$

这里不是模 $h$ 的次数界；在完备实际环中代入 $H=h$ 后仍精确成立。

### Step 4. 保留 Euler 身份的全部实际余项

定义有限 action 的实际值

$$\Phi=[x^{3p}]\left(\frac12V\mathcal D_hV
+\frac x2e^V+\frac L2x^2e^{2V}\right),\qquad
\mathcal D_hx^n=d_n(h)x^n.$$

准确的非驻值加权 Euler 身份为

$$\mathcal B_3=-6p\Phi+
\sum_{n=1}^{3p-1}n(d_n-d_{3p-n})V_nV_{3p-n}.\tag{14}$$

本件将式 (14) 乘 $p$，而不是仅调用旧的模 $h^M$ 端点同余。
低／第二块成对权重为 $2i-3p$；中间块权重为 $p+i$。
代入真实正规化块，得到特征零准确身份

$$p\mathcal B_3=-6p^2\Phi+\frac1p\mathcal F_{\rm act}+R,\tag{15}$$
$$R=-3\sum_{i=1}^{p-1}\delta_i^{\rm low}P_i(h)Z^{\rm act}_{p-i}
+\sum_{i=1}^{p-1}\delta_i^{\rm mid}Y^{\rm act}_iY^{\rm act}_{p-i}
-(d_p-d_{2p})(pV_p)(pV_{2p}).\tag{16}$$

前两类余项属于 $h^m\mathcal O^+[L]$，由式 (11) 和正规化整性给出。
内部配对没有删除：$d_p,d_{2p}\in h^{2m}\mathcal O^+$，
$pV_p\in h^E$、$pV_{2p}$ 整，所以最后一项至少在 $h^{2m+E}$。
故

$$R\in h^m\mathcal O^+[L]\subset h\mathcal O^+[L].\tag{17}$$

### Step 5. 归一化 action 的高次剩余为零

先确认 $p^2\Phi\in\mathcal O^+[L]$。
动能的非内部配对归一化后分别为整的 $P_i(h)Z^{\rm act}_{p-i}$
或 $Y^{\rm act}_iY^{\rm act}_{p-i}$；内部配对为
$(pV_p)(pV_{2p})$，也整。传播子整。
势能的所需指数系数小于 $3p$，其 $p^2$ 归一化整性已由阶乘带证明。

模 $h$ 时，非内部动能配对可用模型剩余替换，因实际差在 $h^E$。
式 (10) 和低块次数界说明每个配对的 $L$ 次数至多 $m$。
内部配对在 $h^E$ 中，故剩余为零。

势能使用响应桥的准确公式（$\alpha=1,2$，$-2\le j<p$）：

$$p^2[x^{2p+j}]e^{\alpha V}
=[x^j]e^{\alpha P(h,x)}
\left(\alpha Z^{\rm act}+\frac{\alpha^2}{2}(Y^{\rm act}-1/2)^2\right)
+p\epsilon_{\alpha,j},\qquad\epsilon_{\alpha,j}\in\mathcal O^+[L].\tag{18}$$

约化后，$j=p-1$ 的式 (18) 具有 $L$ 次数至多 $m$；
$j=p-2$ 时次数至多 $m-1$，再乘 action 中的外部 $L$ 后至多为 $m$。
这里全部剩余乘积只用低于 $p$ 的指数系数，阶乘分母为单位。
因此

$$\deg_L\overline{p^2\Phi}\le m,\qquad
\Pi_{>m}p^2\Phi\in h\mathcal O^+[L].\tag{19}$$

### Step 6. 必须先作高次投影，再除以 $p$

将 $\mathcal F_{\rm act}=\mathcal F_{\rm mod}
+(\mathcal F_{\rm act}-\mathcal F_{\rm mod})$ 代入式 (15)，先施加 $\Pi_{>m}$。
式 (13) 精确消去模型部分，得到

$$\Pi_{>m}p\mathcal B_3
=-6\Pi_{>m}p^2\Phi
+\frac1p\Pi_{>m}(\mathcal F_{\rm act}-\mathcal F_{\rm mod})
+\Pi_{>m}R.\tag{20}$$

中间项属于 $h\mathcal O^+[L]$，因为式 (12) 的高度为 $M+1$，
而 $v_h(p)=M$。其余两项由式 (17)、(19) 属于同一理想。
这证明式 (1)，进而由 $e_*=M-D$ 证明式 (2)。

不单独声称 $\mathcal F_{\rm mod}/p$ 的所有低系数整；
先投影是避免非法逐项约化所必需的操作。

### Step 7. 实际商、负根与端点

写 $P_{\rm cl}=L^m+\sum_{i<m}b_iL^i$、$U_{\rm cl}=\sum_{r=0}^pu_rL^r$，
所有系数整且 $b_i\in h\mathcal O^+$。最高系数有 $u_p=a_{m+p}\in h^{e_*+1}$。
从 $r=p-1$ 到 $r=1$ 递降，比较 $L^{m+r}$ 系数：

$$a_{m+r}=u_r+\sum_{i<m}b_i u_{m+r-i}.$$

求和中的商下标均大于 $r$，故归纳给 $u_r\in h^{e_*+1}$。
再比较 $L^m$ 系数给 $u_0\equiv a_m\pmod{h^{e_*+1}}$，证明式 (3)。
这里是同余，不将真实 $u_0$ 与 $a_m$ 写成相等。

因此 $u_0$ 为单位；当 $t=v_h(\ell)>-\delta_1$ 时，
$1\le r<p$ 的非恒定项满足
$v_h(u_r\ell^r)\ge e_*+1+rt>0$，最高项满足
$v_h(u_p\ell^p)\ge M-2m+pt>0$。
当 $t\ge0$ 时同样均为正。于是 $U_{\rm cl}(\ell)$ 为单位。
所有根 $\beta$ 必须满足 $v_h(\beta)\le-\delta_1$。
在 $-\delta_1<t\le0$ 内，$P_{\rm cl}(\ell)$ 的首一最高项唯一最低，
故 $v_h(P_{\rm cl}(\ell))=mt$，得到式 (4)。

在 $t=-\delta_1$ 处可能有同高项相消，本文不处理该新端点。
因两个新比值均大于原 $e_*/p$，有 $\delta_1>e_*/p$。
相对于上一轮 $\delta_+=\min\{e_*/(p-1),(M-2m)/p\}$，仅自动得
$\delta_1\ge\delta_+$，不在所有 $a$ 上声称严格改善。证毕。

## Corrections, boundaries and open risks

- 原命题没有增加假设；$p=5$ 时 $m=2$、$M\ge10$、$E\ge8$，
  所有单位除法、余项及次数论证仍成立，无需例外计算。
- 式 (1) 是全部高系数共同下界，不计算它们下一层的准确剩余。
- 最高项保留上一轮更强的 $M-2m$ 下界，本文没有把它降回共同界。
- 全负因子的 Newton 下凸包、准确斜率、因子型、简单性和分裂域仍未由本件闭合。
- 没有目标根拟合、逐素数外推或新的全局有理核整性假设。
- 科学作者证明、独立审查、论文立项及实际 PDF 验收保持分离。
