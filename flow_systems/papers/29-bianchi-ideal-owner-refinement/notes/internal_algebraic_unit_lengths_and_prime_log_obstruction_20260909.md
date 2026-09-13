# P29 内部研究：代数单位长度与素数对数的有理线性分离

记录日期：2026-09-09 UTC。第五次 P29–P33 五篇整轮内部论证。
承接[最小对称素理想集合][packets]：放宽标签类型可以解决一项集合值
选择问题，却没有给标签范数与真实周期之间的关系。本篇单独检查这个
周期问题，不改变原单素理想值域、不增加原机制公理，也不作 Route
评估或正式判定。

结论是一个精确的算术障碍：固定 Gaussian Bianchi 弧长的指数是正实
代数单位。因此这些弧长的有理线性包，与有理素数对数的有理线性包，
只在零点相交。尤其任何一个非零周期都不可能在有理常数缩放后，
精确成为一个 Gaussian 素理想范数的对数。

## 1. 对象、时钟与量词

群仍为完整 level-(3) Gaussian 群在 PSL 中的像；时钟是曲率 -1
双曲三空间中的单位速弧长。沿用[本原族笔记][family]的本原无向
owner 定义。证明实际适用于任意 loxodromic
\(A\in SL_2(\mathbb Z[i])\)，不要求先认证本原性；若 A 是真幂，
本篇的长度就是该次多重遍历的总长，不冒充本原 owner 的长度。

记 \(T=\operatorname{tr}A\)，选扩张特征值 \(\lambda\)，使

\[
\lambda^2-T\lambda+1=0,\qquad |\lambda|>1.
\tag{1}
\]

要使用的周期式为

\[
\ell(A)=2\log|\lambda|,\qquad
U(A)=e^{\ell(A)}=\lambda\bar\lambda>1.
\tag{2}
\]

这里的复共轭是固定复嵌入，不是任意数域自同构。为明确因子 2，
将 A 在 PSL 中共轭为 \(\operatorname{diag}(\lambda,\lambda^{-1})\)。
其上半空间作用是
\((z,t)\mapsto(\lambda^2z,|\lambda|^2t)\)。竖直轴上的弧长为
\(\int_t^{|\lambda|^2t}du/u=2\log|\lambda|\)。一般连接这两个
高度的路径长度至少为该值，因为双曲线元至少是 \(|dt|/t\)；竖直轴
达到下界，故确为 translation length。商流中的对应闭合遍历有同一
弧长。

把 A 换成 -A 只改变特征值的符号；共轭不变特征值；取逆后再选扩张
根也不变其模。故 (2) 是无向几何 owner 可用的量。对非零整数 m，
\(\ell(A^m)=|m|\ell(A)\)。没有使用盘字长、矩阵范数或标签范数
替代物理时间。

## 2. 指数长度的显式整系数互反多项式

写 \(T=a+bi\)，\(a,b\in\mathbb Z\)。考虑四个数

\[
\lambda\bar\lambda,\quad
\lambda/\bar\lambda,\quad
\bar\lambda/\lambda,\quad
(\lambda\bar\lambda)^{-1}.
\tag{3}
\]

它们的总和是
\((\lambda+\lambda^{-1})(\bar\lambda+\bar\lambda^{-1})=|T|^2\)，
乘积为 1；两两乘积之和是
\(\lambda^2+\lambda^{-2}+\bar\lambda^2+\bar\lambda^{-2}+2
=T^2+\bar T^2-2\)。三重乘积之和等于倒数之和，仍是 \(|T|^2\)。
因此四个数都是以下多项式的根（允许重根）：

\[
F_T(X)=X^4-(a^2+b^2)X^3
       +\bigl(2(a^2-b^2)-2\bigr)X^2
       -(a^2+b^2)X+1\in\mathbb Z[X].
\tag{4}
\]

特别是 U 与 \(U^{-1}\) 都满足首一整系数多项式，均为代数整数。
这就是 U 为代数单位的含义。这里的“单位”是代数整数环中可逆，
不是实数绝对值等于 1；本案 U 明确大于 1。

不需要证明 (4) 不可约或 U 的次数恰为四。实迹时中间两个根都为 1，
多项式通常降阶，但单位论证不受影响。

所需一般代数事实只有：有限个代数整数的和与积仍为代数整数。
[Milne, Algebraic Number Theory v3.08, Theorem 2.1][milne]
给出该环封闭性；本篇不使用单位群秩定理。也可直接用有限生成模
证明：若 \(\alpha_j\) 各满足首一多项式，将各幂约化到次数界内，
\(\mathbb Z[\alpha_1,\ldots,\alpha_r]\) 由有限个单项式生成。
对任意环元素的乘法保持此模，乘法矩阵的特征多项式给首一整关系。
模作为复数加法子群无挠，可选其有限自由 Z 基；它含 1，故矩阵关系
亦给该元素的关系。

还需一个初等事实：若有理数 \(c/d\)（互素、\(d>0\)）是代数整数，
将它代入首一 n 次整系数方程并乘以 \(d^n\)，得到 \(d\mid c^n\)，
所以 d=1。故一个正有理代数单位及其倒数都为正整数，只能等于 1。

## 3. 有限乘法组合与有理对数空间的分离

**命题 1。** 对任意有限个 loxodromic 元素 \(A_1,\ldots,A_r\)
和整数 \(n_1,\ldots,n_r\)，若

\[
\prod_{j=1}^r U(A_j)^{n_j}\in\mathbb Q_{>0},
\quad\text{则}\quad
\prod_{j=1}^r U(A_j)^{n_j}=1.
\tag{5}
\]

证明。每个 U 及其倒数为代数整数；有限乘积及其倒数仍为代数整数。
若该乘积是正有理数，上一节事实迫使它等于 1。负指数也已包括。□

令

\[
V_{\rm geo}=\operatorname{span}_{\mathbb Q}
 \{\ell(A):A\in SL_2(\mathbb Z[i])\text{ loxodromic}\},
\qquad
V_{\rm prime}=\operatorname{span}_{\mathbb Q}
 \{\log p:p\text{ 为有理素数}\}.
\tag{6}
\]

线性包只含有限线性组合，不引入完备化或无限级数。

**命题 2。**

\[
\boxed{V_{\rm geo}\cap V_{\rm prime}=\{0\}.}
\tag{7}
\]

证明。设同一个实数 x 可写为两侧有限有理组合，取一个正整数 D
消去全部分母，则

\[
e^{Dx}=\prod_j U(A_j)^{n_j}=\prod_p p^{m_p}\in\mathbb Q_{>0}.
\tag{8}
\]

由 (5)，\(e^{Dx}=1\)。实指数函数单射，故 x=0。□

这不是在断言不同闭轨道长度彼此有理线性独立：几何侧内部可以有
非平凡关系。它只排除跨两个线性空间的共同非零值。

## 4. 对素理想范数、重复与集合标签的具体含义

由[Gaussian 素理想分类][classification]，任一非零素理想范数为
\(p^f\)，其中 \(f=1\) 或 2。因此
\(\log N\mathfrak p=f\log p\in V_{\rm prime}\)，且严格为正。
对任意非零有理 c 和任意 loxodromic A，(7) 给

\[
\boxed{c\,\ell(A)\ne\log N\mathfrak p.}
\tag{9}
\]

这包括单位速原时钟 c=1，以及全部正有理统一换算因子。更一般地，
对非零有理 c、正整数 m、n，
\(cm\ell(A)\ne n\log N\mathfrak p\)。重复遍历或将惯性次数吸入
右侧系数都不能取得等号。

同样，任意有限有理加权素理想对数和，只要其总和非零，就不可能
等于有限有理加权几何长度和。因此把一对共轭素理想的共同范数取
一次，或把它们的范数相乘，都没有消除这个精确周期障碍。实分支
与复分支、共轭不动 owner 与二点 owner 也不影响此证明。

但 (9) 不反驳一个根本不要求周期等于素范数对数的标签函数。前轮
E+D 是共轭等变与判别式整除的特定输入条件；本篇没有把 (9) 的
等式要求偷偷添加到它们中。集合／概率值规则的前轮存在结论保持，
本轮只是证明该类标签不能自动充任固定时钟下的精确素数周期。

### 4.1 单个真实本原例子的手算

[已有完整群本原性证明][family]中的
\(A_1=\left(\begin{smallmatrix}1&3\\3&10\end{smallmatrix}\right)\)
有 T=11、判别式数据 d=13；其两个合法 split 标签是
\((3+2i),(3-2i)\)，范数均为 13。由 (1)–(2)，

\[
\lambda=\frac{11+3\sqrt{13}}2,\qquad
U=\frac{119+33\sqrt{13}}2,
\qquad U^2-119U+1=0.
\tag{10}
\]

这给 \(\ell=\log U\)，而不是 \(\log13\)；不仅数值不同，
\(\ell/\log13\notin\mathbb Q\)。该不公度性来自单位证明，
不是浮点近似或一次长度拟合。例子只作既定对象的纸面核算，未运行
本原根、矩阵或素数程序。

## 5. 论证链、反例边界及开放问题

| 子论证 | 证据与推理 | 最强相关异议及处理 |
| --- | --- | --- |
| 物理周期指数是代数单位 | 上半空间弧长推导 (2)，显式互反多项式 (4) | 不能混淆 holonomy 角、扩张根模及因子 2；均单列推导 |
| 几何／素数对数空间只交于零 | 单位乘法封闭、正有理单位只有 1、清分母 (8) | 不声称几何长度内部无关系，不涉及无限求和 |
| 标签放宽不提供精确素数时钟 | 范数是 p 或 p²，故 (9) | 标签公理未含时钟等式，因此不扩大原机制反驳范围 |

对任意实数缩放 c，本篇没有给统一不可能性。事实上对单个已选
owner 和素理想，可事后设 \(c=\log N\mathfrak p/\ell\) 得到一条
等式；这改变了原时钟，且没有给全 owner 上同一个 c 的关系。
本篇不研究这种重定义，更没有允许按 owner 逐项拟合速度。

也没有证明误差下界或排除近似配对；有理线性分离并不自动给有效
Diophantine 距离。没有推断任意解析变换、无限消去、带权跡公式或
全局行列式都不可能。那些问题须先明确等式类型、收敛域与权重。
本轮只解决固定弧长下的有限精确周期关系，不改 Route verdict。

## 6. 来源、实际动作与保全

ARS 的有界 argument-builder 用于分别处理几何归一化、代数证据、
量词和不允许的外推。普通浏览核对 Milne 作者站的 v3.08（正文
日期 2020-07-19），Theorem 2.1 与紧随其后的证明，只用于代数整数
环封闭性的标准背景。本案的互反多项式、周期式和空间分离由本篇
逐项证明；不将它们归给该来源，也不作新颖性声明。搜索结果显示的
抓取时间不作为书稿出版日期。

实际仅新增本笔记，主线程另追加总记录。未运行科学计算、符号
代数、枚举、fixture、producer、历史 writer、论文构建或正式审查；
未改旧稿、书目、锁、协议、回执、失败记录或原标签类型。
正式 FAIL / BLOCK、D06 Recovery 3、Route 与 Stage 5／6 边界不变。

[packets]: internal_minimal_symmetry_packets_and_randomized_selectors_20260909.md
[family]: internal_infinite_primitive_split_obstruction_family_20260908.md
[classification]: internal_fixed_prime_classification_and_selector_criterion_20260908.md
[milne]: https://www.jmilne.org/math/CourseNotes/ANT.pdf
