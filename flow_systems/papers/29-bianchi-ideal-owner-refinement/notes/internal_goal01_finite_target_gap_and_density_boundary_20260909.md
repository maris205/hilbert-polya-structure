# P29 内部研究：有限目标间隙公式与稠密目标边界

记录日期：2026-09-09 UTC。持续内部研究目标的有界纸面推导整理。
本篇承接[零同调时钟笔记][clock]命题 3 与第 6 节，不重新构造轨道，
也不将精确不匹配擅自增强为完整素数对数空间上的统一数值间隙。
本轮只新增本文件；没有实验、科学／符号程序、producer 或旧记录修改。
本篇不是正式稿、Route 评估、Stage 5／6 升级或解除旧 STOP 的回执。

## 1. 上游输入与物理主情形

沿用上游三个实际零同调本原轨道的曲率 -1 弧长：

\[
L=(\ell_1,\ell_2,\ell_3),\qquad
\ell_i=2\log\lambda_i>0,
\]
\[
\lambda_1=\frac{83+9\sqrt{85}}2,\qquad
\lambda_2=163+18\sqrt{82},\qquad
\lambda_3=\frac{731+27\sqrt{733}}2.
\tag{1}
\]

记实数中的有理向量空间，其中只取有限组合：

\[
V_{\rm prime}=\operatorname{span}_{\mathbb Q}
 \{\log p:p\text{ 为有理素数}\}.
\tag{2}
\]

本篇采用的上游结论是

\[
cL\notin V_{\rm prime}^{\,3}\qquad
\text{对每个 }c\in\mathbb R\setminus\{0\}.
\tag{3}
\]

上游以三长度的有理独立、六指数定理及有理时钟的单位论证证明 (3)；
这些证明及六指数定理的来源定位保留在[该笔记][clock]第 4、5、8 节。
本篇只从 (3) 推导有限目标的几何距离结论，不增加超越数论下界定理。

物理主情形固定

\[
I=[c_{\min},c_{\max}],\qquad
0<c_{\min}\le c_{\max}<\infty,
\tag{4}
\]

以及任意非空有限集合 \(F\subset V_{\rm prime}\)。F 的元素可以为正、
负或零，并不额外假设 F 只含单个素数的对数或正整数重复。
F 和 I 一经选定，就定义一个有限目标合同及一个指定时钟窗口。
本篇的正间隙依赖这两项选择，不是对所有 F、所有精度或所有时钟
共同成立的单一正常数。

## 2. 一般紧区间的最小命题及零例外

为完整陈述边界，暂令 \(I=[a,b]\) 为任意非空实紧区间，
\(-\infty<a\le b<\infty\)，仍取非空有限 \(F\subset V_{\rm prime}\)。
定义 sup 范数距离与共同最优误差

\[
\operatorname{dist}_\infty(v,F^3)
 =\min_{f\in F^3}\max_{1\le i\le3}|v_i-f_i|,
\]
\[
\Delta(I,F)
 =\min_{\substack{c\in I\\f\in F^3}}
   \|cL-f\|_\infty
 =\min_{c\in I}\operatorname{dist}_\infty(cL,F^3).
\tag{5}
\]

**命题 1。** (5) 的最小值存在，并且

\[
\Delta(I,F)=0
\quad\Longleftrightarrow\quad
0\in I\ \text{且}\ 0\in F.
\tag{6}
\]

因而在 (4) 的物理主情形中，\(\Delta(I,F)>0\)。

**证明。** \(I\times F^3\) 非空紧，误差函数连续，故最小值被取得。
若最小值为零，则某 \(c\in I\)、\(f\in F^3\) 满足 \(cL=f\)。
由 (3) 必有 c=0；再由 \(\ell_i>0\) 得 \(f=(0,0,0)\)，即 \(0\in F\)。
反之，若 \(0\in I\) 且 \(0\in F\)，这个零时钟与零三元组使误差为零。□

这里 F 非空是定义有限且被取得的最小值所需的约定；空目标集可另用
距离 \(+\infty\) 的约定处理，但不属于本命题的有限目标合同。

## 3. 用配对差消去 c 的精确有限表达

对任意实三元组 \(f=(f_1,f_2,f_3)\)，定义

\[
D(f)=\max_{1\le i<j\le3}
 \frac{|\ell_jf_i-\ell_if_j|}{\ell_i+\ell_j},
\tag{7}
\]
\[
H_I(f)=
\max\left\{
0,\quad
\max_i(a\ell_i-f_i),\quad
\max_i(f_i-b\ell_i),\quad
D(f)
\right\}.
\tag{8}
\]

**命题 2。** 对一般紧区间 I 及任意实三元组 f，

\[
\min_{c\in I}\|cL-f\|_\infty=H_I(f).
\tag{9}
\]

因此有限目标的精确表达为

\[
\boxed{\displaystyle
\Delta(I,F)=\min_{f\in F^3}
\max\left\{
0,\quad
\max_i(a\ell_i-f_i),\quad
\max_i(f_i-b\ell_i),\quad
\max_{i<j}\frac{|\ell_jf_i-\ell_if_j|}{\ell_i+\ell_j}
\right\}.}
\tag{10}
\]

**证明。** 对 \(\varepsilon\ge0\)，误差不超过 \(\varepsilon\) 等价于

\[
c\in [a,b]\cap
\bigcap_{i=1}^3
\left[
 \frac{f_i-\varepsilon}{\ell_i},
 \frac{f_i+\varepsilon}{\ell_i}
\right].
\tag{11}
\]

有限个实闭区间有共同交点，当且仅当其最大下端点不大于最小上端点。
在 (11) 中展开这个充要条件，得到

\[
\varepsilon\ge a\ell_i-f_i,\qquad
\varepsilon\ge f_i-b\ell_i
\quad(1\le i\le3),
\]
\[
\varepsilon\ge
\frac{|\ell_jf_i-\ell_if_j|}{\ell_i+\ell_j}
\quad(1\le i<j\le3).
\tag{12}
\]

这些条件与 \(\varepsilon\ge0\) 合并，恰好是
\(\varepsilon\ge H_I(f)\)。特别地，取等号时 (11) 仍有交点，
从而 (9) 的下界被达到；再对有限个 f 取最小即得 (10)。□

配对差也可直接核查：若 \(e_i=c\ell_i-f_i\)，则

\[
\ell_jf_i-\ell_if_j=\ell_i e_j-\ell_j e_i,
\qquad
|\ell_jf_i-\ell_if_j|
\le(\ell_i+\ell_j)\|e\|_\infty.
\tag{13}
\]

故 (7) 是消去共同 c 后的必要下界；(11) 则证明加上端点项后，
这些下界已经充分，而不只是方便但可能不紧的估计。

若 I 的端点具有可计算表示，且 F 以有限有理系数素数对数组合明确给出，
(10) 是有限个可计算实数的绝对值、最小值和最大值表达。
若端点只作为任意实数存在，则 (10) 仍是精确数学表达，不能无条件
称为可执行的数值输入。本轮没有实际计算 (10)，也没有给出固定小数值、
统一运算量或 F 无关的超越数论估计。

## 4. 完整目标空间中的距离为零，但没有精确匹配

\(\mathbb Q\log2\subset V_{\rm prime}\)，而 \(\log2\ne0\)；
有理数的稠密性因此给出 \(V_{\rm prime}\) 在 \(\mathbb R\) 中稠密。
坐标分别逼近便得 \(V_{\rm prime}^{\,3}\) 在 \(\mathbb R^3\) 中稠密。
所以对每个固定实数 c，

\[
\inf_{v\in V_{\rm prime}^{\,3}}\|cL-v\|_\infty=0.
\tag{14}
\]

当 \(c\ne0\) 时，由 (3) 这个零下确界不被任何目标三元组取得。
因此“没有精确匹配”和“可以任意精度逼近”同时成立，并不矛盾。
F 的有限性不能在 (5) 中被悄悄替换为完整 \(V_{\rm prime}\)：
后一目标集不闭，前述紧性取得最小值的论证不再适用。

这里仅讨论完整有理张成空间的距离；不自动把其稠密性归给某个更窄、
另有整数系数、范数范围或 owner 约束的具体目标集合。

## 5. 即使每个目标集最多三个元素，也无 F 一致间隙

固定物理窗口 (4) 中的任意 \(c_*>0\)。对整数 \(N\ge1\)，纸面定义

\[
q_{i,N}
=2^{-N}\left\lfloor\frac{2^N c_*\ell_i}{\log2}\right\rfloor,
\qquad
F_N=\{q_{1,N}\log2,q_{2,N}\log2,q_{3,N}\log2\}.
\tag{15}
\]

每个 \(q_{i,N}\) 有理，因此 \(F_N\subset V_{\rm prime}\)，且
\(1\le|F_N|\le3\)。取整性质直接给出

\[
0\le c_*\ell_i-q_{i,N}\log2<2^{-N}\log2.
\tag{16}
\]

在 (5) 中使用 c 和 f 的这一特定选择，再结合命题 1，得到

\[
0<\Delta(I,F_N)\le2^{-N}\log2\longrightarrow0.
\tag{17}
\]

故即使集合基数一直不超过 3，仅增加有理系数的位数，也可让每一轮
仍为正的最优误差趋于零。若要求目标集嵌套，改取
\(\widehat F_N=\bigcup_{m=1}^N F_m\)，则每个集合仍有限，
\(\Delta(I,\widehat F_N)\) 单调不增且同样趋于零。

(15) 是反驳“对任意有限 F 有统一正间隙”的数学反例，不是允许研究者
根据几何周期事后拟合 owner、时间或目标表的模型设计规则。
本轮也没有执行取整、生成这些数值集合或作任何数值拟合。

## 6. 零时钟边界与不能反推的必要条件

若把正窗口换成 \(c\in(0,b]\)、\(b>0\)，并取 \(F=\{0\}\)，则

\[
\inf_{0<c\le b}\|cL\|_\infty
=\inf_{0<c\le b}c\max_i\ell_i=0.
\tag{18}
\]

在紧区间包含零时，命题 1 已准确指出同一例外是否出现；若 \(0\notin F\)，
区间含零本身并不会破坏正间隙。
也不能反称所有非紧时钟区间都失败：固定有限 F 时，
\(\operatorname{dist}_\infty(cL,F^3)\to\infty\) 随 \(|c|\to\infty\)。
因此例如在 \([a,\infty)\)、\(a>0\) 上仍能截回某个紧区间取得正最小值。
本篇采用紧正窗口是清楚、充分的合同条件，而不是声称其每一项都必要。

## 7. 闭形式时钟及有条件扰动下界

沿用上游相空间与正则性条件。对

\[
\rho=c+Xu+\sum_{k=1}^{d}a_k\alpha_k(X)>0,
\qquad d<\infty,
\tag{19}
\]

u 全局单值，\(\alpha_k\) 为全局闭一形式，且时间约定是
\(d\tau=\rho\,dt\)。上游零同调积分证书给这三条轨道的周期向量

\[
T_\rho=cL.
\tag{20}
\]

因此只要 (19) 的 c 在固定正窗口 I 中，同一个 \(\Delta(I,F)\)
统一覆盖其允许的 u、实系数 \(a_k\) 和闭形式选择：
\(\operatorname{dist}_\infty(T_\rho,F^3)\ge\Delta(I,F)>0\)。
这不是任意正时间密度的间隙结论。

若另外给出一个实际周期向量

\[
T=cL+e,\qquad c\in I,\qquad \|e\|_\infty\le\eta,\quad \eta\ge0,
\tag{21}
\]

则对每个 \(f\in F^3\) 用三角不等式，再取最小，得到

\[
\operatorname{dist}_\infty(T,F^3)
\ge\operatorname{dist}_\infty(cL,F^3)-\|e\|_\infty
\ge\Delta(I,F)-\eta.
\tag{22}
\]

只有独立确证 \(\eta<\Delta(I,F)\) 才由此得到严格正的扰动后下界。
若没有 (21) 的证据，或只有 \(\eta\ge\Delta(I,F)\)，本推导不提供
严格正结论；后者也不表示已经构造出精确匹配。
没有把数据误差、时间密度的函数范数或一般动力学扰动未经推导地当作
这个三周期向量的 \(\eta\)。

## 8. 证据层级与实际动作

本篇新增的是 (3) 的有限合同推论、精确的单变量 sup 误差公式、
稠密性与增位数反例，以及条件明确的三角不等式扰动界。
这些是内部 AI 辅助纸面推导，不是新实验、已测数值误差或独立发表结果。
ARS 的有界 argument-builder 用于分开前提、证明、量词和反例边界；
没有启动完整论文 pipeline、审稿、来源新颖性判断或状态升级。

本轮实际动作限于读取指令与上游材料、以 apply_patch 新建本文件，
以及对本文件进行文字读回、行数、引用文件存在性和尾空白检查。
没有运行科学／符号程序、枚举、producer、构建或实验；
没有改动旧笔记、协议、锁、回执、正式稿或任何 Route／Stage 状态。
若后续需要具体数值下界，必须先给出确切 F、时钟窗口和待比较的误差界；
本篇自身不授权这些后续计算或合同改写。

[clock]: internal_goal01_null_homology_clock_obstruction_20260909.md
