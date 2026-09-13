# Paper30：一般第三 forcing 第二层与七的幂正根簇

日期：2026-09-07。
状态：TWIST_THIRD_FORCING_GENERAL_SECOND_LAYER_AND_SEVEN_POWER_CLUSTER_ACCEPTED。

本轮从上一轮已接受的唯一根簇分离与五的幂局部结构接续：
完成一般 $p\ge7$ 的完整第二正规化层、加强的正根下界与点值区间；
另完成全 $p\ge5$ 的四次移位剩余，并以七的幂的同阶碰撞确定其整个正赋值三次根簇。
这些局部结果不等于完整素数幂首项或 Paper30 正式立项。

## 1. 同一实际对象与此前接受范围

继续固定双谐波模型、同一参数与 SUM action，取任意本原 $p^a$ 次根，$a\ge2$。
对本轮一般素数 $p\ge7$，记
$$
h=D_1=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,\quad
m=(p-1)/2,\quad M=p^{a-1}m,\quad \chi=(-1)^{m+1},
$$
$$
q_3=3m+1,\quad e_*=M-q_3,\quad v_h(h)=1,\quad v_h(p)=M.
$$
实际分支为 $V_n=\rho^n v_n(L/\rho)$、$d_n=-D_n/h$，且
$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V},\qquad
S=h^{-q_3}p^2\mathcal B_3.
$$

[上一轮根簇处置](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_AND_FIVE_POWER_DISPOSITION_20260907.md)
给出的实际次数 $3m+1$、常数非零、唯一分解
$S=P_{\rm cl}U_{\rm cl}$、正／负根数 $m,p$（计重数）继续接受。
特别是
$$
P_{\rm cl}\text{ 首一},\quad \deg P_{\rm cl}=m,\quad \bar P_{\rm cl}=L^m,\quad
U_{\rm cl}\equiv a_m=[L^m]S\pmod{h^{e_*}},
$$
以及 $j>m$ 的系数高度 $v_h([L^j]S)\ge e_*$，本轮不重证。
五的幂正簇、三的幂完整局部结果和更早的已接受范围不重开。

## 2. 一般素数的完整第二正规化层

[一般下一层证明](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md)
对全部 $p\ge7,a\ge2$ 给出逐系数身份
$$
\boxed{S=-\frac{3\chi}{64}L^m
+h\frac{\chi}{8192}(684L-41)L^{m-1}+O(h^2).}
$$

证明补齐的是完整二阶响应，不只补入一个矩。
精确算子 $\mathcal R=\mathcal T-H\partial_H$ 给出全 $H$ 的响应
$t=-\mathcal RP/2$、
$q=\mathcal R^2P/8-\mathcal RP/[4(H-4)]$。
第一端点项先准确配对；随后保留低块、传播子、两响应和交叉乘积的全部二阶项。

三个原来未求值的矩现在为
$$
A_2=-\frac{1488L^2-1992L+373}{294912}L^{m-2},\qquad
B_1=-\frac{816L^2-504L+67}{6144}L^{m-2},
$$
$$
C_0=-\frac{(4L-1)(8L-3)}{64}L^{m-2}.
$$
其中 $A_2$ 通过有限偶导数配对消去未知二阶低块解，再用两份明确有理证书消去积分；
正次数因子保证没有漏掉第 $p$ 阶积分分母。
$B_1,C_0$ 由有理系数和二次分母的 Frobenius 求值得到。
局部化只用于证明多项式身份，结论延伸回全部 $L$，包括 $L=0$、$4L=1$。
数值分母仅含 $2,3,5$，所以包含 $p=7$。

完整组合为 $E_2=(540L-41)L^{m-1}/65536$。
$r^3=8\chi H^{3m}(1-3H/8+O(H^2))$ 的自身修正也计入。
$p=7$ 的 $r^4$ 从 $H^{12}$ 起，恰在本一般层所需余项阶，
不影响目标 $H^{11}$；没有声称它从 $H^{13}$ 起。
原块误差仍为 $h^{M-m}$，乘入缺陷后才到 $h^M$，而 $M\ge3m+3$ 足够转回实际结论。

## 3. 加强的根界、开区间与根和

[一般根界 V2](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_ROOT_BOUND_PROBE_V2_20260907.md)
调用旧商的高精度常数性，正确消去最高项的一次修正后得到
$$
\boxed{P_{\rm cl}=L^m+\frac{41}{384}hL^{m-1}+O(h^2).}
$$

因此所有正根按重数满足
$$
\boxed{v_h(\alpha)\ge2/m,}
$$
而负根界 $v_h(\beta)\le-e_*/p$ 保持。
对任意有限局部扩域中的非零参数，包含非整参数，只要
$$
-\frac{e_*}{p}<t=v_h(\ell)<\frac2m,
$$
第 $m$ 项就是 $S(\ell)$ 的唯一最低项，故
$$
\boxed{v_h(\mathcal B_3(\ell))=q_3-2M+mt,\qquad
v_h(V_{3p}(\ell))=m+1-2M+mt.}
$$
两端不纳入；这不是把整参数处的商单位性外推到非整参数。

所有有限扩域整参数处的准确距离式仍为
$$
v_h(S(\ell))=\sum_{j=1}^m v_h(\ell-\alpha_j),
$$
计重数，根处允许 $+\infty$。基线分别加上 $q_3-2M$、$m+1-2M$。
正簇根和为
$$
\sum_j\alpha_j=-41h/384+O(h^2).
$$
$p\ne41$ 时根和赋值恰为一；$p=41$ 时只知至少为二。
这既不确定单根赋值，也不单独决定不可约性或单根的域迹。
同一有限展开可以兼容不同斜率或重根，因此一般下界不冒充准确 Newton 多边形。

## 4. 四次移位：一个全素数组成量

[四次移位剩余证明](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md)
从全 $p\ge5$ 单位耦合方程直接证明
$$
\mathcal E=r^3\mathcal F_3(H,L)+r^4E_4(L)+O(H^{4m+1}),
$$
$$
\boxed{E_4(L)=-\frac3{32}
+\frac3{64}\sum_{k=1}^{m-1}(2k-1)(4L)^k.}
$$
$\mathcal F_3$ 在这里必须是完整 $H$ 响应，不能替换成旧的一次截断。
$E_4$ 的次数恰为 $m-1$、常数为 $-3/32\ne0$。

新响应 $a,b$ 经两次偶导数配对消去，留下奇权矩
$J_1=-1-\frac12\sum_{k=1}^{m-1}(4L)^k$，且
$E_4=\frac3{16}(-L\partial_L+1/2)J_1$。
这不是从五的幂表外推一般素数。
四次组成量不等于实际 $H^{4m}$ 总层：同阶的 $r^3\mathcal F_3$ 仍须计算。

## 5. 七的幂：完整正赋值三次根簇

[七的幂新证明](PAPER30_TWIST_THIRD_FORCING_SEVEN_POWER_NEXT_LAYER_PROBE_V1_20260907.md)
在固定特征七、$L=0$ 的精确有限环中给出
$$
\mathcal F_3(H,0)=6H^3+O(H^4),\qquad E_4(0)=1.
$$
$r^3,r^4$ 的相应首系数分别为一、二，所以端点 $H^{12}$ 的常数系数为
$6+2=1$ 于 $\mathbb F_7$。
有限证书明确列出真实 Chebyshev 权重、低块及两响应的短表，
由单位三角递推和四项求和证明，不是参数点拟合或根扫描。

对全部 $a\ge2$，$M=3\cdot7^{a-1}\ge21$ 保证实际误差不碰撞。
结合一般层，得到
$$
S(0)=h^2+O(h^3),\quad
P_{\rm cl}=L^3+b_2L^2+b_1L+b_0,
$$
$$
b_2=h+O(h^2),\qquad b_1=O(h^2),\qquad b_0=2h^2+O(h^3).
$$
故 Newton 下边是 $(0,2)\to(3,0)$，三个正根赋值都恰为 $2/3$，
三次因子不可约且可分。

取 $\kappa^3=-2h^2$。在 $E=K^+(\kappa)$ 中，
$P_{\rm cl}(\kappa y)/h^2$ 的剩余为 $2(1-y^3)$，
在 $\mathbb F_7$ 有三个简单根 $1,2,4$。
三次简单根提升给全部正根位于 $E$；每个根的赋值分母三又保证它各自生成 $E$。
因此
$$
\boxed{K^+(\beta_1)=K^+(\beta_2)=K^+(\beta_3)
=K^+(\sqrt[3]{-2h^2}),\qquad e=3,\ f=1.}
$$
这个域也是该三次因子的分裂域，不是整个十次 forcing 的分裂域。
根号指任选一个三次根生成的域；不是把单位 $-2$ 擅自删掉。

选取 $K^+$ 中的三个三次单位根 $\omega_j$ 并按剩余标签对应，还得到
$
\beta_j=\omega_j\kappa-h/3+O(h^{4/3}),\qquad
v_h(\beta_j-\beta_k)=2/3\quad(j\ne k).
$
分数阶只是延拓赋值界。由不同根的准确距离，在参数边界
$v_h(\ell)=2/3$ 时，三距离之和进一步等于
$4/3+\max_jv_h(\ell-\beta_j)$，仍保留根附近的全部额外抵消。
该三次扩张还是循环 Galois 扩张；未将其外推为一般素数的分裂结论。

任意有限扩域整参数处
$$
v_h(\mathcal B_3(\ell))=10-2M+\sum_{j=1}^3v_h(\ell-\beta_j),\qquad
v_h(V_{21}(\ell))=4-2M+\sum_{j=1}^3v_h(\ell-\beta_j).
$$
若 $0\le v_h(\ell)<2/3$，距离和为 $3v_h(\ell)$；
若 $v_h(\ell)>2/3$（包括零参数），距离和为二。
边界 $v_h(\ell)=2/3$ 保留准确距离公式。
另外七个负赋值根的准确斜率、因子型、简单性仍未完成。

## 6. 真正非作者核查、窄勘误与输入绑定

[联合非作者独审](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_AND_SEVEN_POWER_INDEPENDENT_CHECK_20260907.md)
已完成，当前四稿对应的39项限定检查全部通过，无剩余修订要求。
当前版本为一般层 V1、一般根界 V2、四次移位 V1、七的幂 V1；
根界 V1 的对应文字项保持 FAIL，不追记成全通过。
主控已全文读取761行一般层、228行根界 V1、232行窄修 V2、
320行四次移位、363行七的幂稿，以及614行联合报告，接受其明确范围。

独审者自行实现自由有理环，核对两张完整证书、积分边界、六矩算子与一般系数提取；
再独立正向生成七的幂的权重和两响应短表。
其独立四次移位与真实 Chebyshev 原端点至 $H^{12}$ 的重建也分别得到相同碰撞。
局部域、根修正、距离与分歧扩域量词另由数学论证核查，不以程序退出码替代。

根界 V1 的一句“不是任何单根的域迹”确实过强：
不可约时，根和可能就是任一根的域迹。
V1 和独审发现完整保留；V2 只改为“未据此认定”并记录勘误，
没有更改公式、证明、比较多项式或新层依赖，没有重跑未变检查。
七的幂后来证明不可约，正好说明需要这项区别。

主控及参与推导的代理均属于作者证据。
历史名称带 independent 的根界／七的幂作者不计本轮独审票。
本轮真正非作者独立重建有理证书与新增有限边界，没有把作者代码运行计作独审。
按 proof-writer，将精确证明、有限身份、一般根界与特殊根域分开验收；
技能要求明确暴露并修正过强表述，未放宽正文容量或批次验收要求。

| 本轮冻结输入 | 主控全文读取 | SHA256 |
| --- | --- | --- |
| [一般下一层 V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md) | 761行 | `3d0fea6035d33c11e912946a442278711f061bebde32724ad003a3b2f9994e6d` |
| [根界 V1（保留措辞失败）](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_ROOT_BOUND_PROBE_V1_20260907.md) | 228行 | `2405b379df4aecb1e23532153b95dc219f9f23ee441bd5e0b5734189a21ed6ff` |
| [根界 V2（当前接受）](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_ROOT_BOUND_PROBE_V2_20260907.md) | 232行 | `a275effecae69305269fcd549e37992add3101c1f824f6a6af18a804b1b2a577` |
| [四次移位剩余 V1](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md) | 320行 | `ec3f6de59e55176fe11a62b36d27da516bb8d620c438fdd0037ee6c099a260da` |
| [七的幂下一层 V1](PAPER30_TWIST_THIRD_FORCING_SEVEN_POWER_NEXT_LAYER_PROBE_V1_20260907.md) | 363行 | `0e31fa70be8e92a39ce15d43c8411a3ce6f8ae40da2486ef8cb5eeca8f073b9e` |
| [联合非作者独审](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_AND_SEVEN_POWER_INDEPENDENT_CHECK_20260907.md) | 614行 | `7dc7c1a1c7741af7480cec9fa456c5128b40605877149ef82ad54867692da594` |

## 7. 下一缺口与批次状态

一般 $p\ge7$ 的第二正规化层、三个二阶矩、$2/m$ 正根下界及扩大点值区间不再 OPEN。
全 $p\ge5$ 的 $E_4$ 组成量亦不再 OPEN。
七的幂的正赋值三次根簇及根域已确定；五的幂已接受的二次正簇保持。

下一一般对象是 $p\ge11$ 正簇的更深 Newton 层及分裂／简单性，
需要控制三次响应更高 $H$ 层与四次组成量的合并，不能只收集特殊素数结果。
全部 $p\ge5$ 的负赋值 $p$ 次因子仍缺准确斜率、因子型与简单性。
一般 $p\ge5$、非真共振三的幂的第二／第三 forcing 互素仍未解决。

[此前第三首层与三的幂局部结果](PAPER30_TWIST_THIRD_FORCING_DISPOSITION_20260907.md)
保持接受：一般首层与实际响应桥、$p\ge5$ 的第一／第三 forcing 互素；
三的幂两支的完整局部结构与真周期九的第二／第三 forcing 互素。
前两个内部层、第二阶乘带、全部奇素数及两倍奇素数的已接受范围不重开。

完整素数幂 $C,Q$、其他合数和实际参数根全实性仍未证明。
全局新意与自然正文容量尚未最终认证。
不估页、不投正式候选票、不试写测页；没有 Paper30 项目、PDF、Route 或对外操作。
Batch07 仍为 **3/5**，Paper30 未立项，Paper31 未开展，22–30页实质正文及独立验收要求不变。
