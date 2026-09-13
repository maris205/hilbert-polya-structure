# Paper31 discovery：原首层切向类在尖点纤维的有界诊断 V1

日期：2026-09-09。作者：`/root`。用途：族内可行性与错误推广筛选，不是候选准入。
状态：`PROVABLE AS STATED`（下列准确命题的作者证明；尚待独立核查）。
不改变 Paper30 的完整光滑纤维定理；不宣布 Paper31 立项、新意分或正文容量。

## 1. 准确命题与假设

采用 Paper30 的原矩阵、原八中心曲面、单位时间、首层圆分环和两个状态方向。
设 $p\ge5$，$p\nmid m$，$s=\widetilde\eta\zeta_p$，$\pi=\zeta_p-1$，
$J=I_{m,\eta}(x,y;t_0)$，$T=t_0^m$，$\varepsilon=(-1)^{m+1}$，
$I=I_{mp,s}$，$\alpha=p^{-1}d_{\rm state}I$。
先在代数闭剩余域 $k$ 工作；这些几何结论可在定义所用有限数据的完美扩域上表述。
取

$$T=-27/256,\qquad h=9\varepsilon/8,\qquad X=(J=h).$$

则有以下作者命题。

1. 原完整有限纤维 $X$ 是尖点有理曲线；$H_p(T,h;\varepsilon)=0$，但不称其为光滑超奇异曲线。
2. 原边界 Bockstein 的限制仍给 $\kappa_J\ne0\in H^1(X,\mathcal O_X)$。
   原迹局部函数 $G_i=(I-F(j_i))/(p\pi)$ 的微分仍拼成
   $\nu=d(\bar G_i|_X)\in H^0(X,\Omega^1_{X/k})$。
3. 将 $X$ 识别为标准尖点三次曲线，取正规化参数 $r$，
   $U=\operatorname{Spec}A$，$A=k[\xi,\upsilon]/(\upsilon^2-\xi^3)=k[r^2,r^3]$，
   $V=\operatorname{Spec}k[r^{-1}]$，且 $\kappa_J=b[r]$，$b\ne0$。
   在固定 Čech 符号 $g_V-g_U$ 下，

   $$\nu|_U=-b^p d_A(r^p)
     =-\frac{b^p}{2}\xi^{(p-5)/2}\tau,
     \qquad \tau=2\xi\,d\upsilon-3\upsilon\,d\xi,\qquad \nu|_V=0.$$

   因此 $p=5,7$ 时 $\nu$ 为非零尖点扭微分；$p\ge11$ 时 $\nu=0$。
   对每个 $p\ge5$，它都在 $X$ 的整个光滑部分上为零。
4. 对 $X$ 的每个光滑几何点 $P$，原完整系数理想满足

   $$\pi\notin\mathfrak c(\alpha)_P.$$

   故把 Paper30 的 $(\pi,\widetilde H)$ 结论推广到“奇异完整纤维的光滑点”是错误的。
   本文没有求出这些点或尖点处的完整理想，也没有声称 $\pi$ 的最小幂次。

## 2. 输入与依赖图

已接受且不重开审查的输入如下。

- [实际有限纤维与同基模型的接受处置](PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md)，
  §2.1、§2.3：每个原完整有限纤维整约化；原有限基底 henselization 上有保持能量的模型同构，
  不是仅泛 Jacobian 同源。原模型为 $W:v^2+cuv-\varepsilon Tv=u^3-Tu^2$。
- [Paper30 接受源的 §6](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/06-first-layer.tex)：
  边界复形、原 Bockstein 计算、全图原 prime-trace 整数同余、Taylor 商及正则 $G_i$。
  本文重新核查了这些证明中哪些步骤需要光滑性，见步骤 2；不直接删除原命题中的限制。
- [接受源 §3](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex)：
  原 $W$ 的完整临界代数与坐标；本文另算指定尖点的显式坐标变换。

依赖顺序是：同基完整模型 → 指定尖点曲线；边界复形与完整有限除子序列 → 非零实际类；
原迹同余 → Frobenius 与 Hasse 标量关系；尖点 Čech 计算 → 实际扭微分；
光滑点的原相对余切基与局部代数 → $\pi$ 不属于完整系数理想。
后一步不调用任何未证的尖点完整理想或高层厚度。

## 3. 证明

### 步骤 1：指定参数确实给原完整尖点纤维

在 $c=h$ 的 $W$ 上作可逆仿射线性变换

$$\xi=u+9/64,\qquad \upsilon=v+(h/2)u-\varepsilon T/2.$$

配方后右端为

$$u^3+(h^2/4-T)u^2-(h\varepsilon T/2)u+T^2/4=(u+9/64)^3.$$

故方程准确变成 $\upsilon^2=\xi^3$；变换亦延拓为射影线性变换。
因 $p\ge5$，所用分母可逆，且 $T\ne0$。唯一尖点为 $(\xi,\upsilon)=(0,0)$，
正规化为 $r\mapsto(r^2,r^3)$，无穷点光滑。已接受的同基完整模型定理给 $X\simeq W_h$。
例如从原临界代数也得到
$z=-3\varepsilon/16$，$u=-9/64$，$v=27\varepsilon/1024$；未漏掉 $c=\varepsilon-z-z^3/T$ 的中间项。
任意允许 $m$ 都可在代数闭 $k$ 中选择满足指定 $T$ 的单位 $t_0$；不是空参数情形。

### 步骤 2：实际 Bockstein 在该奇异完整纤维上仍非零

Paper30 §6 的边界计算在 $S$、$D$、$L_m$ 上完成，尚未使用所选纤维光滑性。
它给 $\ker\beta_{L_m}=k\langle1\rangle$ 以及 $\beta_{L_m}(J)\ne0$。
原有限纤维是由 $J-h\cdot1$ 定义的 Cartier 除子，且与 $D$ 不交，因此仍有准确序列

$$0\longrightarrow\mathcal O_S\xrightarrow{J-h\cdot1}L_m
  \longrightarrow L_m|_X\longrightarrow0,\qquad L_m|_X\simeq\mathcal O_X$$

其中平凡化仍是原截面 $1$。$H^1(S,\mathcal O_S)=H^2(S,\mathcal O_S)=0$，
故实际限制 $H^1(S,L_m)\to H^1(X,\mathcal O_X)$ 仍是同构。
于是 $\kappa_J=[f_{ij}]\ne0$，$f_{ij}=\overline{(j_j-j_i)/\pi}|_X$。
这一步只消费完整有限除子，不把奇异曲线当作光滑曲线。

### 步骤 3：先推出 Hasse 值为零，再定义全曲线 Kähler 类

原整数 prime-trace 同余和全图正则性给出的 $G_i$ 不需要所选能级光滑。
原 Taylor 公式在 $X$ 上给

$$\bar G_j|_X-\bar G_i|_X=-H_p(T,h;\varepsilon)f_{ij}+f_{ij}^p.$$

在 $H^1(X,\mathcal O_X)$ 中左边为零，故
$\operatorname{Fr}_{\mathcal O,*}(\kappa_J)=H_p(T,h;\varepsilon)\kappa_J$。
此处 Frobenius 的目标确实是 $\mathcal O_X$，不同于 Paper30 光滑证明中的像层目标。
对标准尖点的两个仿射开集，$U\cap V=\operatorname{Spec}k[r,r^{-1}]$，因此

$$H^1(X,\mathcal O_X)=k[r,r^{-1}]/(k[r^2,r^3]+k[r^{-1}])=k[r].$$

右端表示由 Čech 类 $[r]$ 张成的一维向量空间，不是多项式环。
因 $r^p\in k[r^2,r^3]$，Frobenius 在该 $H^1$ 上为零。
结合 $\kappa_J\ne0$，得 $H_p(T,h;\varepsilon)=0$。
所以 $\bar G_j-\bar G_i=f_{ij}^p$，取 Kähler 微分后为零，$\nu$ 拼接成立。
这里未假设 $\ker d=\mathcal O_X^p$，因此没有偷用光滑 Cartier 精确列。

### 步骤 4：用实际 Čech 类确定微分，而非任取扭微分

写 $\kappa_J=b[r]$，$b\ne0$。在所需公共仿射细化上，$f_{ij}$ 与代表 $br$ 之差为一个 $\mathcal O_X$ 余边界。
将其局部零链取 $p$ 次幂并对 $\bar G_i$ 作对应调整，微分不变，
而新的 $G$ 差恰为 $b^p r^p$。标准一组原函数可取
$g_U=-b^p r^p\in A$，$g_V=0$。
调整后的实际原函数与这组原函数之差拼成全局正则函数；
$H^0(X,\mathcal O_X)=k$，其微分为零。故实际 $\nu$ 正是命题中的形式。
该论证只调整剩余原函数，不声称给出全曲面上 $J$ 的全局提升。

### 步骤 5：准确计算尖点扭微分及素数区别

有

$$\Omega^1_{A/k}=(A\,d\xi\oplus A\,d\upsilon)
 /( -3\xi^2\,d\xi+2\upsilon\,d\upsilon).$$

对于 $a\in A$，$a\tau=0$ 等价于存在 $g\in A$ 使
$a(-3\upsilon,2\xi)=g(-3\xi^2,2\upsilon)$。
在 $k(r)$ 中后一个等式准确给 $g=a/r$；因特征不为 $2,3$，它也满足前一坐标。
由半群 $\{0,2,3,4,\ldots\}$ 可知

$$\operatorname{Ann}_A(\tau)=\{a\in A:a/r\in A\}=(\upsilon,\xi^2).$$

特别地 $\tau\ne0$，$\xi\tau\ne0$，$\xi^2\tau=0$。
令 $n=(p-3)/2$。$r^p=\xi^n\upsilon$，且 $n=-3/2$ 于 $k$，所以

$$d_A(r^p)=n\xi^{n-1}\upsilon\,d\xi+\xi^n\,d\upsilon
        =\tfrac12\xi^{(p-5)/2}\tau.$$

这证明 $p=5,7$ 时非零及 $p\ge11$ 时为零；其支撑仅可能是尖点。
另外，所有 $p\ge5$ 时正规化拉回 $\nu$ 都为全局正则微分于 $\mathbb P^1$，故为零；
正规化在光滑部分为同构，与上述支撑结论一致。
在 $p\ge11$，$r^p\in\ker d_A$ 但 $r^p\notin A^p$：否则函数域中唯一的 $p$ 次根 $r$ 将属于 $A$。
故此时 $\ker d_A$ 严格大于 $A^p$，不能用像层短正合列证明 $\nu\ne0$。
在 $p=5,7$，这里不额外宣布整个核层分类；本诊断只需已算出的具体微分。

### 步骤 6：原完整系数理想不包含圆分参数

取 $X$ 的一个光滑点 $P$。原剩余表面上 $dJ$ 在 $P$ 非零；
于是某个局部提升 $j$ 的 $dj$ 可扩充为原相对余切模的局部基 $(dj,\theta)$。
由原全图精确公式 $\alpha=\widehat H(j)dj+\pi dG$ 写成

$$\alpha=A_0dj+\pi B_0\theta,\qquad A_0=\widehat H(j)+\pi A_1.$$

剩余值 $H(h)=0$ 给 $A_0\in\mathfrak m_P$；$\nu|_{X_{\rm sm}}=0$ 给 $B_0\in\mathfrak m_P$。
同时 $\bar A_0=H_p(T,J;\varepsilon)$ 在原剩余表面的局部整环中不是零元：
$H_p$ 是非零首一多项式，$J$ 非常值且在 $P$ 是光滑参数。
若 $\pi=r_0A_0+s_0\pi B_0$，模 $\pi$ 后得 $\bar r_0\bar A_0=0$，因此 $r_0=\pi r_1$。
原局部环对 $\pi$ 无挠，除去 $\pi$ 得 $1=r_1A_0+s_0B_0\in\mathfrak m_P$，矛盾。
所以 $\pi\notin(A_0,\pi B_0)=\mathfrak c(\alpha)_P$。
证明不要求 $H$ 在 $h$ 为简单根，且不忽略四末端线上属于 $X_{\rm sm}$ 的点。

## 4. 与已知机制及下一步的区别

本证明主要使用标准正规化、Čech 上同调、尖点 Kähler 扭微分与局部环代数；
其新发现候选仅是这些机制对原迹产生的指定 $\nu$ 及原系数理想的实际消费。
这不能直接转换成独立论文新意或 22–30 页容量；目前更像排除错误推广的有界接口结果。
原尖点处完整两方向理想、光滑部分纵向厚度、参数变形中的分裂、高层自然塔关系均未解决。
没有从此拼出全素数奇异纤维完整分类，也没有重新启动旧容量失败的几何包。

本轮一手来源核对：
[Ohashi–Harashita, arXiv:2105.11436v3](https://arxiv.org/html/2105.11436v3)，主控实读摘要和引言：
研究奇异模型的 dualizing/regular differential module，不以名称相近就替代本证明的 Kähler 模。
[Terzi, arXiv:2309.06901](https://arxiv.org/abs/2309.06901)，主控实读摘要及出版入口引言：
研究正规化、广义 Jacobian、$p$-rank 和 $a$-number；不据摘要判定已包含或未包含上述原迹接口。
独立文献席另外核原文必要段；其阅读不记作主控全文阅读。
本文件的六步代数论证不以这两篇的未读定理作黑箱，且尚未完成正式查新。

## 5. 开放风险与交付状态

待非作者核查：原有限模型消费者、Čech 调整符号、奇异曲线上原 $G_i$ 全图消费、理想非包含证明。
本文件只新增本地发现阶段作者诊断；未改已接受源或锁，未编译，未提交外部服务。
