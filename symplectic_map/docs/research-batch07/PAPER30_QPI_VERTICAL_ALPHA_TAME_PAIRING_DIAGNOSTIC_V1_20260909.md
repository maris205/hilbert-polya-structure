# Paper30 qPI：原 tame monodromy 第一末端的配对诊断 V1

日期：2026-09-09。作者：`/root/p30_qpi_nonunit_tau_layer1_v1`。
类型：有界作者数学诊断。`route_applicability: NOT_APPLICABLE`。0 GPU。
唯一新增文件是本件；不修改任何旧作者件、检查或脚本，不建立候选或论文。

## Claim Being Tested

设 $k$ 为奇特征 $p$ 的域，$m\ge1$ 为整数，$p\nmid m$，$\eta\in k$ 精确为 $m$ 阶，$t\in k^\times$。
必要时扩域定义 $\eta$ 和谱根；这不改变所检验的恒等式。
以下有限证书也先在相应整数圆分系数环中成立，再于可分参数下降到这些域。

保持原第一末端图
$$W=1+uv,\qquad J_t=W-v/W-tu,$$
以及原正则矩阵
$$\widehat A(z)=A_0+zA_1+z^2E,$$
$$A_0=\begin{pmatrix}t-v&-1\\-v(t-v)&v\end{pmatrix},\quad
A_1=\begin{pmatrix}J_t-1&u\\v-t+v^2/W&1\end{pmatrix},\quad E=\operatorname{diag}(1,0). \tag{1}$$
定义原降序 monodromy
$$B_m(z)=\widehat A(\eta^{m-1}z)\cdots\widehat A(\eta z)\widehat A(z),\qquad
\mathcal J_m(u,v)=[z^m]\operatorname{tr}B_m(z).$$
先对完整 $u,v$ 状态求导，再在 $u=0$ 评价，记
$$h=\mathcal J_m|_{u=0},\qquad h_u=(\partial_u\mathcal J_m)|_{u=0},\qquad
h_v=(\partial_v\mathcal J_m)|_{u=0},\qquad V=-h_v\partial_u+h_u\partial_v.$$
这里 $h_u$ 不是对已经限制到 $u=0$ 的函数作微分。
第一末端的原状态二形式为 $-du\wedge dv$，所以该 $V$ 与指定方向及符号一致。

置 $T=t^m$、$e_m=(-1)^{m+1}$、$Z=z^m$，并令
$$f_m(Z)=(T+hZ+Z^2)^2-4e_mZ^3,$$
$$R_{\rm raw}(z)=\operatorname{tr}\bigl((VB_m)[B_m,z\partial_zB_m]\bigr)\big|_{u=0},$$
$$R_m(Z)=\sum_j[z^{jm}]R_{\rm raw}(z)\,Z^j,\qquad g_m(Z)=R_m(Z)/Z.$$
当 $f_m$ 可分时，目标是判断
$$\mathcal P_m:=\sum_{f_m(r)=0}\frac{4g_m(r)}{f_m'(r)^2}\stackrel{?}{=}m^2. \tag{2}$$
根和在代数闭包中解释，结果属于原系数域。

## Status

**NOT CURRENTLY JUSTIFIED（全 $m$ 恒等式 (2)）。**

本件已完成的严格内容是：

1. 全 $m$ 的原迹／行列式规范和 $R_m$ 支持 $Z^1$ 至 $Z^5$ 的次数界。
2. $m=2,\eta=-1$ 的全部 $t,v$ 参数上，给定可分性后 $\mathcal P_2=4$，有无分母整数证书。
3. 仅一次允许的 $m=3$ 特化：$t=1,v=0$，给出精确圆分证书并得到 $\mathcal P_3=9$。
4. 明确说明“若 (2) 成立则得到 Cartier 不同时消失”的纯曲线推论，以及仍未证明的唯一标量余式目标。

没有从 $m=1,2,3$ 的值推断所有 $m$，也没有继续增加样本。

## Assumptions and Boundary

- 所有微分只作用于原状态 $u,v$；$t,\eta,z$ 固定。
- 两状态导数、原因子次序和原谱系数规范不替换。
- $p$ 奇、$p\nmid m$，且使用配对公式时 $f_m$ 必须可分。重复判别根处不允许代入分母。
- 本件不使用任何未完成的乘积 cocycle、Krichever–Phong 框架或其他新路线作为已证定理。
- 原 $m=1$ 配对引理保留冻结；本件的新全参数计算仅为 $m=2$。

## Proof Strategy and Dependency Map

1. 原二次矩阵及循环迹给规范与全 $m$ 次数界。
2. $m=2$ 直接对两个原矩阵求导、相乘并投影，给 $4g_2=f_2'P_2+f_2C_2$。
3. 在可分根处将配对化成 $P_2(r)/f_2'(r)$；首一四次式的 Lagrange 插值读取三次系数四。
4. 单个 $m=3$ 参数用同一方法给完整可核证书，只作有限排错。
5. 对全 $m$，次数界把问题缩成一个三次余式的首系数；本文没有证明该首系数恒为 $m^2$。

## Proof and Exact Certificates

### Step 1. 全 $m$ 的准确规范与次数界

由原矩阵直接有
$$\operatorname{tr}\widehat A=t+J_tz+z^2,\qquad \det\widehat A=z^3.$$
迹的循环性给 $\operatorname{tr}B_m(\eta z)=\operatorname{tr}B_m(z)$。
因 $\eta$ 精确为 $m$ 阶且 $p\nmid m$，只可能保留 $m$ 的倍数次。
最高次矩阵系数为
$$\eta^{2(0+1+\cdots+m-1)}E^m=E,$$
而 $A_0^m=t^{m-1}A_0$，其迹为 $t^m$。所以在原图准确有
$$\operatorname{tr}B_m=t^m+\mathcal J_m z^m+z^{2m},\qquad
\det B_m=e_m z^{3m}. \tag{3}$$
行列式的相位为 $\eta^{3m(m-1)/2}=(-1)^{m-1}=e_m$。
式 (3) 没有重定义 $\mathcal J_m$，也不需要先除以 $m$ 来恢复它。

$B_m$ 的 $z^{2m}$ 系数为状态无关的 $E$，所以
$$\deg_z(VB_m)\le2m-1.$$
$[B_m,z\partial_zB_m]$ 的 $z^{4m}$ 项是 $[E,2mE]=0$，故其次数至多 $4m-1$；它的常数项为零。
因此
$$\operatorname{supp}_z R_{\rm raw}\subset[1,6m-2].$$
投影到 $m$ 倍次后，对 $m\ge2$ 得
$$\operatorname{supp}_Z R_m\subset[1,5],\qquad \deg_Z g_m\le4. \tag{4}$$
$m=1$ 时同一估计给 $[1,4]$，也符合 (4) 的较宽范围。
若某最高项在某特征中消失，只会缩小支持，不破坏该界。

只对迹可以立即使用循环不变性；不能据此声称 $R_{\rm raw}$ 只含 $m$ 倍次。
下面的 $m=2$ 实算给出其一次项
$$[z]R_{\rm raw}=-2t^4(v-1)(v+1)(t-v^2-v), \tag{5}$$
它作为整数多项式非零。因此题设中的谱次数投影确实不可省略。

### Step 2. $m=2$ 从原矩阵得到的有限恒等式

在 $u=0$ 记
$$A_*(z)=\begin{pmatrix}t-v&-1\\-v(t-v)&v\end{pmatrix}
 +z\begin{pmatrix}-v&0\\v-t+v^2&1\end{pmatrix}+z^2E,$$
$$U_*(z)=(\partial_u\widehat A)|_{u=0}
 =z\begin{pmatrix}v+v^2-t&1\\-v^3&0\end{pmatrix},\qquad
W_*(z)=(\partial_v\widehat A)|_{u=0}=\partial_vA_*(z). \tag{6}$$
所以原两个有序因子和导数是
$$B_2=A_*(-z)A_*(z),$$
$$B_{2,u}=U_*(-z)A_*(z)+A_*(-z)U_*(z),\qquad
B_{2,v}=W_*(-z)A_*(z)+A_*(-z)W_*(z). \tag{7}$$
由 (7) 取 $z^2$ 迹系数，准确得到
$$h=2t-v^2-2v-1,\qquad
h_u=-2(v-1)(t-v^2-v),\qquad h_v=-2(v+1). \tag{8}$$
因此 $VB_2=-h_vB_{2,u}+h_uB_{2,v}$；两个状态方向都已进入本计算。
原 $\det B_2=-z^6$，故
$$f_2(Z)=(t^2+hZ+Z^2)^2+4Z^3.$$

定义下列具体多项式：
$$\begin{aligned}
P_2(Z)=4\bigl(&Z^3+(3t-v^2-4v+1)Z^2\\
 &+(3t^2-tv^2-2tv-5t+4v^2+4v)Z\\
 &+t(t^2+2tv-2t-2v^3+2v)\bigr),
\end{aligned} \tag{9}$$
$$\begin{aligned}
C_2(Z)=-8\bigl(&2Z^2+4Zt-Zv^2-6Zv+Z\\
 &+2t^2-tv^2+tv-4t-v^3+2v^2+3v\bigr).
\end{aligned} \tag{10}$$
使用 (6)–(8) 的原矩阵，先计算 $R_{\rm raw}$，再只保留 $z^{2j}$ 系数，得到如下**整数多项式证书**：
$$\boxed{\quad4g_2(Z)=f_2'(Z)P_2(Z)+f_2(Z)C_2(Z)\quad}
\quad\text{in }\mathbb Z[t,v,Z]. \tag{11}$$
式 (6)–(10) 给了核查 (11) 所需的全部有限矩阵及标量因素；本次独立逐项展开后差多项式为零。
其最高实际投影系数为
$$[Z^5]R_2=2(v+1)(t-v^2-v),$$
与 (4) 的五次界相符；原未投影式的谱次数从一至十一般都有贡献。

若 $f_2$ 可分，在根 $r$ 处 (11) 给
$$\frac{4g_2(r)}{f_2'(r)^2}=\frac{P_2(r)}{f_2'(r)}.$$
对任意次数至多三的 $P$，首一可分四次式的 Lagrange 插值为
$$P(Z)=\sum_{f_2(r)=0}P(r)\frac{f_2(Z)}{(Z-r)f_2'(r)}.$$
比较三次项即可得 $\sum P(r)/f_2'(r)=[Z^3]P$。
式 (9) 的三次系数为四，所以
$$\mathcal P_2=4. \tag{12}$$
证书没有参数分母，故在所有奇特征的可分参数上原样成立；不是只在若干 $t,v$ 值成立。

### Step 3. 唯一一次 $m=3$ 精确特化

这里只取 $t=1,v=0$、$\eta^2+\eta+1=0$，不继续扫描其他参数。
从三个原有序因子及其两个状态导数计算，得到
$$h=1+3\eta,\qquad h_u=0,\qquad h_v=3-3\eta,$$
$$R_3(Z)=9(1-\eta)Z^5-36\eta Z^4+(81\eta+144)Z^3-45\eta Z^2. \tag{13}$$
置 $f_3=(1+(1+3\eta)Z+Z^2)^2-4Z^3$、$g_3=R_3/Z$。
以下是该单个特化的完整证书：
$$P_3=9Z^3+(54\eta-9)Z^2-(18\eta+36)Z+9\eta,$$
$$C_3=-36Z^2+(18-162\eta)Z+36\eta+54,$$
$$4g_3=f_3'P_3+f_3C_3\quad\text{in }\mathbb Z[\eta,Z]/(\eta^2+\eta+1). \tag{14}$$
直接展开的判别式为
$$\operatorname{disc}_Z(f_3)=48384\eta+36608\ne0$$
于 $\mathbb Q(\eta)$，所以本特化确实可分，(14) 与同一插值论证给
$$\mathcal P_3=9. \tag{15}$$
式 (14) 也可降到其判别式非零且 $p\ne3$ 的奇特征；它仍只证明这一参数特化，不证明全部 $m=3$ 参数。

### Step 4. 若全 $m$ 配对成立，Cartier 推论没有新增次数障碍

由 (4)，在光滑谱曲线 $Y^2=f_m(Z)$ 上令
$$\omega=\frac{dZ}{Y},\qquad \theta_m=\frac{g_m(Z)dZ}{Y^3}.$$
简单分歧点的 $Y$-参数展开给 $\theta_m$ 至多二阶极点且无留数。
无穷远令 $s=1/Z$、$W=Ys^2$，则
$$\theta_m=-s^4g_m(1/s)W^{-3}ds,$$
因为 $\deg g_m\le4$ 而正则；比 $m=1$ 多出的一次谱次数不造成新无穷远极点。
采用 $-\sum_r\operatorname{res}_r(Q_r\omega)$ 的次序，其中局部极部原函数为
$$Q_r=-2g_m(r)/(f_m'(r)Y).$$
简单根处 $dZ=(2Y/f_m'(r)+O(Y^3))dY$，故该配对就是 (2) 的左端。

在代数闭包中，由 $Y=Y^p/f_m^{(p-1)/2}$ 及 $dZ\ne0$，曲线函数域的 $p$-基为 $1,Z,\ldots,Z^{p-1}$。两个表示
$$\omega=Y^{-p}f_m^{(p-1)/2}dZ,\qquad
\theta_m=Y^{-p}g_m f_m^{(p-3)/2}dZ$$
的分子次数均不超过 $2p-2$，故 Cartier 只读取指数 $p-1$。
因此它们的像分别为 $H^{1/p}\omega$、$\Lambda_m^{1/p}\omega$，其中
$$H=[Z^{p-1}]f_m^{(p-1)/2},\qquad
\Lambda_m=[Z^p]R_m f_m^{(p-3)/2}.$$
这一范围包括 $p=3$。

若两个系数同时为零，函数域 $p$-基逐项积分给 $\omega=dF$、$\theta_m=dG$。
在每个点，$dF$ 正则迫使 $F$ 的负主部只含 $p$ 的倍数次幂。
去掉该负主部与常数得到正则局部原函数 $F_P$，且
$$(F-F_P)\theta_m=d((F-F_P)G)$$
留数为零。于是局部配对之和等于全局 $F\theta_m$ 的留数之和，为零。
这里仍未把“有理恰当”单独误当成 de Rham 零类。
因此**若** (2) 已证明，由 $p\nmid m$、$m^2\ne0$ 可推出 $H,\Lambda_m$ 不同时为零。
本步只是准确的条件推论，不填补下一节的全 $m$ 缺口。

## Exact Remaining Gap

在可分参数函数域 $K$ 中，$f_m'$ 在 $K[Z]/(f_m)$ 可逆。令 $P_m$ 是
$$4g_m(f_m')^{-1}\pmod{f_m}$$
的唯一次数至多三的代表。插值严格给
$$\mathcal P_m=[Z^3]P_m.$$
所以全 $m$ 目标的准确最小缺口是
$$\boxed{[Z^3]\operatorname{rem}_{f_m}(4g_m(f_m')^{-1})=m^2} \tag{OPEN}$$
对于原所有 $m$、全部允许的 $t,v,\eta$ 尚未证明。
等价地，需要构造原矩阵导出的全 $m$ Bezout 证书
$$4g_m=f_m'P_m+f_mC_m,\qquad \deg P_m\le3,\quad [Z^3]P_m=m^2,$$
其分母至少应在判别式可逆的参数环中受控，然后才能下降到所有允许的奇特征。

曾考虑的乘积／谱留数路线需要证明相应二维留数在原有序乘积下的准确 cocycle 公式，并控制从 $z$ 到 $Z=z^m$ 的因子。
本件没有证明这种公式。
尤其 $B_m(\eta z)$ 虽与 $B_m(z)$ 共轭，但共轭矩阵依赖状态与谱参数；
对 $V$ 和 $z\partial_z$ 求导会出现额外共轭导数项。式 (5) 已显示不能以循环迹不变性直接删掉这些项或省略投影。
重复行列式根 $z=0$ 处的极部也没有由一般框架的名称自动得到控制。
因此没有使用“每个因子贡献一个单位”或“谱覆盖再乘 $m$”作为未经证明的计数。

## Actual Verification and Handoff

- 完整使用 proof-writer，明确将全 $m$ 原目标标为未闭合，同时保留已证明的有限恒等式和全 $m$ 次数引理。
- $m=2$ 使用原矩阵 (6)–(7) 和两个状态导数，从头独立计算；(8)、(11)、行列式及实际投影次数均作整数精确检查。
- $m=3$ 只用一次 $t=1,v=0$ 特化；对该同一特化补写 (14) 的显式证书，没有增加参数样本。
- 全部计算为只读内存 `python -B` 精确符号运算，正常 exit 0；无浮点拟合、GPU、新脚本或数据文件。
- 未改任何旧作者／检查文件；未消费其他尚未核准的路线来把 (OPEN) 改写为已证。
- 不评分、不建立候选或论文；本件按“全 $m$ 配对仍 OPEN，$m=2$ 全参数与一次 $m=3$ 特化已严格核准”终态交付。
