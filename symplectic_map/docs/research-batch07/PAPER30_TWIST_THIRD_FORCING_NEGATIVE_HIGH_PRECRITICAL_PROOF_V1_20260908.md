# Paper30：全部高系数的整个预临界段消失

日期：2026-09-08。作者：主控。新增加强稿；不覆盖本日首层证明或旧记录。
使用 `formula-derivation` 和 `proof-writer`；当前仅为作者证明状态。

## Claim / Target

固定任意 $p\ge5$ 素数及 $a\ge2$，采用当前双谐波实际规范。令

$$m=(p-1)/2,\quad M=p^{a-1}m,\quad D=3m+1,\quad E=M-m,
\quad e_*=M-D.$$

证明全部高系数共同满足

$$\boxed{p[L^j]\mathcal B_3\in h^m\mathcal O^+
\qquad(m<j\le D).}\tag{1}$$

因而 $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$ 的实际商满足

$$\boxed{U_{\rm cl}\equiv a_m=[L^m]S
\pmod{h^{e_*+m}\mathcal O^+[L]},\qquad e_*+m=M-2m-1.}\tag{2}$$

结合此前已接受 $v_h([L^p]U_{\rm cl})\ge M-2m$，得到

$$\delta_{\rm pre}=\frac{M-2m}{p},\qquad
v_h(\beta)\le-\delta_{\rm pre}\quad
\text{对每个负簇根 }\beta.\tag{3}$$

在任意有限扩域中，非零 $\ell$ 满足
$-\delta_{\rm pre}<t=v_h(\ell)\le0$ 时有 $v_h(S(\ell))=mt$。
新端点仍未纳入；本件不声称共同下界层非零，不确定完整负 Newton 图。

## Status

证明分类 `PROVABLE AS STATED`；推导分类 `COHERENT AS STATED`。
独立审查尚待完成；作者协作检查不计非作者审查。

## Assumptions and notation

所有对象与
[同日全部高系数首层稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_LAYER_PROOF_V1_20260908.md)
相同。本件重述新增步骤所需定义，不依赖首层稿的结论来循环证明加强结论。

取本原 $p^a$ 次根 $\zeta$，$h=2-\zeta-\zeta^{-1}$，
$\mathcal O^+=\mathbb Z_p[h]$、$K^+=\mathbb Q_p(h)$，
$v_h(h)=1$、$v_h(p)=M$。参数 $L=-h\lambda$ 固定，实际辅助幅度为 $b=1$。
所有理想包含均逐 $L$ 系数解释，误差允许任意但有限的 $L$ 次数。

$$d_n(h)=\frac{\zeta^n+\zeta^{-n}-2}{h},\qquad
d_n(h)V_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},$$
$$V=\sum_{1\le n<3p}V_nx^n,\qquad
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}.$$

低块 $P(x)=\sum_{i=1}^{p-1}V_ix^i$ 是形式低块在 $H=h$ 的实际代入。
$\mathcal N=x\partial_x$，$J=xe^P/2+2Lx^2e^{2P}$、
$K=xe^P/4+2Lx^2e^{2P}$，只取 $x$ 次数小于 $p$。
模型 $Y,Z$ 均指零常数形式模型的实际代入，其正次数方程为

$$ (\mathcal D_1+J)Y=J/2,\qquad
(\mathcal D_2+J)Z=-K(Y-1/2)^2,\tag{4}$$

其中 $\mathcal D_kx^j=d_{kp+j}(h)x^j$ 对 $1\le j<p$ 定义，
常数的对角作用在本文辅助方程中定义为零。
这只是记录正次数方程的约定，不是令真实内部传播子为零。
实际块 $Y^{\rm act}_j=pV_{p+j}$、$Z^{\rm act}_j=p^2V_{2p+j}$。
记 $\Delta Y=Y^{\rm act}-Y$、$\Delta Z=Z^{\rm act}-Z$、
$q=Y^{\rm act}_0$。特别地，$q$ 是实际参数多项式，可能依赖 $L$。

## Exact inputs and dependency map

只使用既有接受输入的有关段落：

1. [第二阶乘带响应桥](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)，
   式 (12)、(20)—(28)：正规化块整，$q\in h^E$，$Z^{\rm act}_0\in h^M$，
   $\Delta Y,\Delta Z\in h^E$，真实正次数方程含 $p$ 倍整误差，以及缩放导数身份。
2. [一般素数第三 forcing](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)，
   式 (14)—(16)、(19)、(24)：准确 Euler 身份和真实 Chebyshev 缺陷。
3. [根簇分离](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md)，
   Step 6—7：实际固定次数分解以及形式模型的精确 $L$ 次数界。
4. [负端最高项处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_DISPOSITION_20260908.md)：
   仅在最终根界调用已接受最高项下界 $M-2m$。

依赖链为：传播子与配对缺陷的整段界 → 保留完整 $q$ 的实际响应近似身份
→ 两种端点误差的 $h^{M+m}$ 界 → action 与 Euler 余项的高次投影
→ 商的首一递降比较。所用近似身份均写成实际理想包含，不作启发式替换。

## Proof

### Step 1. 实际缺陷的三个整段界

令 $\mathcal D_0x^j=d_j(h)x^j$，$\Delta_k=\mathcal D_k-\mathcal D_0$。
在 $1\le j<p$ 上，接受的真实移位式给

$$\Delta_k(j)\in h^m\mathcal O^+\quad(k=1,2).\tag{5}$$

对 $1\le i<p$ 设

$$\delta_i^{\rm low}=d_i-d_{3p-i},\quad
\delta_i^{\rm mid}=d_{p+i}-d_{2p-i},\quad
C_i=\delta_i^{\rm low}-\delta_i^{\rm mid}.$$

则

$$\delta_i^{\rm low},\delta_i^{\rm mid}\in h^m\mathcal O^+,
\qquad C_i\in h^{2m}\mathcal O^+.\tag{6}$$

最后一项是本次加强所需的额外精度，不能只由两项各在 $h^m$ 推出。
为核对它的实际适用性，回到已接受的特征 $p$ Chebyshev 身份：
在 $z=1+\eta$、$H=-\eta^2/z$、$T=z^p=1+\eta^p$、$u=z^i$ 下，

$$C_i(H)=-\frac{(T-1)^2(T^2+T+1)}{T^3H}
\left(u+\frac{T^2}{u}\right).\tag{7}$$

右侧的 $\eta$ 赋值至少为 $2p-2=4m$。
完整左侧是 $H$ 多项式，故其模 $p$ 属于 $H^{2m}\mathbb F_p[H]$。
以整数系数提升并代入 $H=h$ 后，附带的 $p$ 倍系数至少在 $h^M$；
$M\ge5m\ge2m$，所以确有式 (6) 的实际界。
式 (5) 和两种单缺陷的 $h^m$ 界以同一实际提升规则解释。

### Step 2. 保留完整初值的响应，精度到 $h^M$

设 $T_0=1+\mathcal NP$。低块在实际环中准确满足

$$ (\mathcal D_0+J)T_0=0,\qquad
(\mathcal D_0+J)\mathcal N^2P=-2KT_0^2\pmod{x^p}.\tag{8}$$

这些是低块递推的两次 $\mathcal N$ 导数身份；
$\mathcal N$ 与传播子交换，且 $\mathcal NJ=2KT_0$。
全部常数按本文约定处理，式 (8) 的正次数是准确的。

由式 (5)、(8) 及单位三角比较，模型本身满足

$$Y=-\frac12\mathcal NP+O(h^m),\qquad
Z=\frac18\mathcal N^2P+O(h^m).\tag{9}$$

前式的残差为 $\Delta_1\mathcal NP/2$，后式的残差由
$\Delta_2\mathcal N^2P/8$ 和前式平方差组成，均在 $h^m$。
初值都为零，各正次数传播子均为单位，故这两个包含合法。

现在从准确实际方程减去模型方程：

$$ (\mathcal D_1+J)\Delta Y=p\varepsilon_1,$$
$$ (\mathcal D_2+J)\Delta Z
=-2K(Y-1/2)\Delta Y-K(\Delta Y)^2+p\varepsilon_2,\tag{10}$$

其中 $\varepsilon_1,\varepsilon_2$ 的正次数全部整。
第一式的初值是 $q$，而 $qT_0$ 具有相同初值，其正次数残差为
$q\Delta_1\mathcal NP\in h^{E+m}=h^M$。
因此单位三角比较给

$$\Delta Y=qT_0+O(h^M).\tag{11}$$

在第二式中，利用式 (9)、(11) 和 $2E\ge M$：

$$-2K(Y-1/2)\Delta Y-K(\Delta Y)^2
=qKT_0^2+O(h^M).$$

而由式 (8)，候选 $-q\mathcal N^2P/2$ 满足

$$ (\mathcal D_2+J)\left(-\frac q2\mathcal N^2P\right)
=qKT_0^2-\frac q2\Delta_2\mathcal N^2P
=qKT_0^2+O(h^M).$$

其常数为零，与实际 $\Delta Z_0=Z^{\rm act}_0\in h^M$ 的差在目标理想中。
再次作单位三角比较，得到完整实际估计

$$\boxed{\Delta Y=q(1+\mathcal NP)+O(h^M),\qquad
\Delta Z=-\frac q2\mathcal N^2P+O(h^M).}\tag{12}$$

这里 $q$ 未被约化为零或某个常数；余项整性保持为逐参数系数陈述。

### Step 3. 配对误差在 $h^{M+m}$ 中

定义

$$\mathcal F(A,B)=\sum_{i=1}^{p-1}
\left(2i\delta_i^{\rm low}P_iB_{p-i}
+i\delta_i^{\rm mid}A_iA_{p-i}\right),$$

记 $\mathcal F_{\rm act}=\mathcal F(Y^{\rm act},Z^{\rm act})$，
$\mathcal F_{\rm mod}=\mathcal F(Y,Z)$。
固定 $i$、置 $j=p-i$。代入式 (9)、(12)，两种线性差的和为

$$-q ij^2\delta_i^{\rm low}P_iP_j
-q i^2j\delta_i^{\rm mid}P_iP_j
=-q ijP_iP_j\left(jC_i+p\delta_i^{\rm mid}\right).\tag{13}$$

此身份在特征零实际环中成立，使用的是整数 $i+j=p$，不是提前令 $p=0$。
作者协作核算在冻结前纠正了草式多写的一个外部 $i$；高度论证未改变。
其中 $qC_i\in h^{E+2m}=h^{M+m}$；
$qp\delta_i^{\rm mid}\in h^{E+M+m}$，也在该理想中。

所有被式 (13) 略记的误差逐类如下：

- 响应式 (12) 的 $h^M$ 余项乘 $h^m$ 缺陷，在 $h^{M+m}$。
- 模型 $Y+\mathcal NP/2\in h^m$ 乘 $q$、再乘缺陷，
  高度至少 $E+2m=M+m$。
- 二次差 $(\Delta Y_i)(\Delta Y_j)$ 乘缺陷，高度至少
  $2E+m\ge M+m$，因为 $2E\ge M$。

故

$$\boxed{\mathcal F_{\rm act}-\mathcal F_{\rm mod}
\in h^{M+m}\mathcal O^+[L].}\tag{14}$$

另一方面，精确次数界
$\deg_LP_i,\deg_LY_i,\deg_LZ_i\le\lfloor i/2\rfloor$ 给

$$\deg_L\mathcal F_{\rm mod}\le m.\tag{15}$$

该次数界来自模型递推，所有传播子与 $L$ 无关；代入 $H=h$ 后仍为精确界。

### Step 4. 高次投影后的 action 与 Euler 余项

令 $\Pi=\Pi_{>m}$，并令

$$\Phi=[x^{3p}]\left(\frac12V\mathcal D_hV+
\frac x2e^V+\frac L2x^2e^{2V}\right).$$

准确加权 Euler 身份及低／第二块的配对权重给

$$p\mathcal B_3=-6p^2\Phi+\frac1p\mathcal F_{\rm act}+R,\tag{16}$$
$$R=-3\sum_{i=1}^{p-1}\delta_i^{\rm low}P_iZ^{\rm act}_{p-i}
+\sum_{i=1}^{p-1}\delta_i^{\rm mid}Y^{\rm act}_iY^{\rm act}_{p-i}
-(d_p-d_{2p})(pV_p)(pV_{2p}).\tag{17}$$

式 (17) 的前三类项保留真实内部配对；本式也可直接从一般稿 Euler
式的权重 $2i-3p$、$p+i$、内部合计 $-p$ 重算得到。

在 $R$ 的前两项中用模型替换实际块，所得两个模型多项式次数均至多为 $m$。
实际／模型差在 $h^E$，再乘缺陷使高次投影在 $h^{E+m}=h^M$。
内部项中 $d_p-d_{2p}\in h^{2m}$、$pV_p=q\in h^E$、$pV_{2p}$ 整，
所以它本身在 $h^{M+m}$。因此

$$\Pi R\in h^M\mathcal O^+[L].\tag{18}$$

对 action 有更强于仅模 $h$ 的包含

$$\Pi(p^2\Phi)\in h^E\mathcal O^+[L].\tag{19}$$

为证明式 (19)，动能的非内部归一化配对为 $P_iZ^{\rm act}_{p-i}$
或 $Y^{\rm act}_iY^{\rm act}_{p-i}$ 乘与 $L$ 无关的整传播子。
它们与次数至多 $m$ 的模型配对之差在 $h^E$。
归一化内部配对为 $(pV_p)(pV_{2p})$ 乘整传播子，也在 $h^E$。

势能的准确响应桥为（$\alpha=1,2$，$j=p-1,p-2$）

$$p^2[x^{2p+j}]e^{\alpha V}
=[x^j]e^{\alpha P}
\left(\alpha Z^{\rm act}+\frac{\alpha^2}{2}(Y^{\rm act}-1/2)^2\right)
+p\epsilon_{\alpha,j},\quad\epsilon_{\alpha,j}\in\mathcal O^+[L].\tag{20}$$

其实际块换成模型后，误差在 $h^E$；额外 $p$ 倍误差在 $h^M\subset h^E$。
对应两个模型的次数分别至多 $m$、$m-1$，后者乘外部 $L$ 后也至多 $m$。
这证明了式 (19)，同时验证了所有 action 正规化项的整性。

### Step 5. 投影与除法的顺序及结论

先将式 (16) 作高次投影，使用式 (15) 消去模型，得到

$$\Pi(p\mathcal B_3)=-6\Pi(p^2\Phi)
+\frac1p\Pi(\mathcal F_{\rm act}-\mathcal F_{\rm mod})+\Pi R.\tag{21}$$

三个右端项分别在 $h^E$、$h^m$、$h^M$ 中。
因为 $E=M-m\ge4m$，全体都在 $h^m$ 中，得到式 (1)。
没有要求 $\mathcal F_{\rm mod}/p$ 的低次系数整；
消去它的步骤发生在除以 $p$ 后作任何约化之前。

式 (1) 给 $[L^j]S\in h^{e_*+m}$ 对 $j>m$。
由 $P_{\rm cl}$ 首一，比较 $L^{m+p},L^{m+p-1},\ldots,L^{m+1}$ 的系数，
逐级得到每个非恒定商系数均在 $h^{e_*+m}$。
再比较 $L^m$ 系数得到 $u_0\equiv a_m\pmod{h^{e_*+m}}$。
这证明式 (2)，并未把实际 $u_0$ 写成与 $a_m$ 相等。

### Step 6. 根界与最小素数边界

商常数为单位。中间系数有共同高度 $M-2m-1$，最高系数有接受高度 $M-2m$。
对非恒定项逐一比较，允许的无根开区间由

$$\min\left\{\frac{M-2m-1}{p-1},\frac{M-2m}{p}\right\}$$

决定。前一比值减去后一比值为

$$\frac{M-2m-p}{p(p-1)}.$$

因为 $a\ge2$ 给 $M\ge pm=(2m+1)m$，分子至少为
$2m^2-3m-1$。当 $m=2$ 时它为 $1$；对整数 $m\ge2$，它随 $m$ 严格递增。
故最小值确为式 (3) 的 $\delta_{\rm pre}=(M-2m)/p$。
在 $t>-\delta_{\rm pre}$ 时，商的所有非恒定项赋值严格为正，
常数项唯一最低；因而没有负簇根落在此开区间。
当 $t\le0$ 时，正簇首一因子的最高项唯一最低，给 $v_h(S(\ell))=mt$。

最小素数 $p=5$ 对应 $m=2$、$M\ge10$、$E\ge8$。
本文全部估值不等式成立，各正次数传播子都是单位，没有边界丢项。
$p=3$ 不在声明范围。证毕。

## Boundaries and open risks

- 共同高度从 $e_*$ 提升为 $e_*+m$；不是证明新首层非零。
- 最高项继续保留其更强的已接受高度；本文没有处理其下一层。
- $\delta_{\rm pre}$ 相对于旧最初界严格改进，但不在所有 $a$ 上声称
  相对于上一轮 $\delta_+$ 再次严格改进。
- 完整负因子的 Newton 下凸包、准确赋值、简单性和分裂域仍待新证据。
- 这是数学加强稿，未重审未变旧阶段，未触发论文立项或外部效力。
