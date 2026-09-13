# P29 内部研究：零同调本原三轨道与闭形式时间密度障碍

记录日期：2026-09-09 UTC。持续内部研究目标的有界整理单元。
本笔记的三交换子、全群本原性、长度独立与时间密度推导来自上一轮
内部纸面论证，本次整理核验为自含文本，不伪称新实验或文献已有结论。
继承[代数单位长度笔记][units]的群与弧长归一化；
[已有本原族笔记][family]提供同群的迹同余方法，但本篇三交换子的
本原性在下文另证，不借用另一族的本原结论。

本轮只新增这份内部笔记。它不是正式稿、Route 评估、Stage 5／6
升级或解除旧 STOP 的回执；没有新 batch、科学程序、producer 或实验。

## 1. 对象、目标空间与主结论

固定

\[
\Gamma(3)=\{A\in SL_2(\mathbb Z[i]):A\equiv I\pmod3\},
\qquad \bar\Gamma(3)\subset PSL_2(\mathbb C),
\qquad M=\bar\Gamma(3)\backslash\mathbb H^3.
\tag{1}
\]

双曲曲率为 -1；相空间为单位切丛 \(S=SM\)，X 是单位速测地流
生成元，旧时间 t 就是弧长。记

\[
V_{\rm prime}=\operatorname{span}_{\mathbb Q}
 \{\log p:p\text{ 为有理素数}\},
\tag{2}
\]

其中只有有限组合。Gaussian 素理想范数为 \(p\) 或 \(p^2\)，
故其对数属于此空间；正整数重复和有限有理加权素数对数也包括在内。

**主结论。** 下文明确给出三个真实本原周期轨道 \(\gamma_1,\gamma_2,
\gamma_3\)，满足零整数同调及弧长 \(\ell_1,\ell_2,\ell_3\) 的
有理线性独立。对任意有限 d、实常数 c 与 \(a_1,\ldots,a_d\)，若

\[
\rho=c+Xu+\sum_{k=1}^d a_k\alpha_k(X)>0,
\tag{3}
\]

其中 u 为 S 上全局单值、沿流 C1 的实函数，\(\alpha_k\) 为 S 上
全局光滑闭实一形式，且 \(\rho\) 足够正则以定义所讨论的时间变换，
那么新时间 \(d\tau=\rho\,dt\) 的三个周期不可能全部属于
\(V_{\rm prime}\)。新生成元是 \(X/\rho\)，不是 \(\rho X\)。
基空间 M 上的闭一形式经拉回后也属于 (3)。

本结论只排除包含这三个 owner 的全覆盖精确周期要求；不把周期要求
添入本来仅要求等变性或判别式整除的标签规则。

## 2. 相空间拓扑与三个实际交换子

先核查 M 是流形而非在此处偷借曲面模型。若 \(B=I+3D\in\Gamma(3)\)，
由 \(1=\det(I+3D)=1+3\operatorname{tr}D+9\det D\) 得

\[
\tau:=\operatorname{tr}B=2-9\det D\in2+9\mathbb Z[i].
\tag{4}
\]

若 [B] 在 PSL 中有限阶，则 B 的特征值模为 1，所以 \(|\tau|\le2\)。
(4) 迫使 \(\tau=2\)；有限阶意味着 B 可对角化，两个特征值均为 1，
因此 B=I。又 \(-I\notin\Gamma(3)\)，故 \(\bar\Gamma(3)\) 无挠。
该矩阵群离散，点稳定子是离散群与紧稳定群的交，因而有限；无挠性
排除非平凡点稳定子。于是 M 是双曲三流形，基本群为 \(\bar\Gamma(3)\)。

投影 \(S^2\to SM\to M\) 的纤维连通且单连通，纤维丛同伦长正合列给
\(\pi_1(SM)\cong\pi_1(M)\)。所用一般拓扑事实见
[Hatcher, Theorem 4.41，正文 p.376][hatcher]；
同调与基本群交换化的关系见同书 Theorem 2A.1，正文 p.166。

取

\[
P=\begin{pmatrix}1&3\\0&1\end{pmatrix},\qquad
Q_n=\begin{pmatrix}1&0\\3n&1\end{pmatrix},\qquad n=1,2,3,
\]
\[
C_n=[P,Q_n]:=PQ_nP^{-1}Q_n^{-1}
=\begin{pmatrix}1+9n+81n^2&-27n\\27n^2&1-9n\end{pmatrix}.
\tag{5}
\]

直接相乘即得 (5)。两因子均在 \(\Gamma(3)\)，故 \(C_n\in\Gamma(3)\)；
也可直接核查其行列式为 1、模 3 为 I。迹为

\[
T_n=2+81n^2\in\{83,326,731\}>2.
\tag{6}
\]

所以三个元素都是实 hyperbolic，也都是本案 loxodromic。它们的轴给出
M 中闭测地线及 S 中闭速度轨道。作为基本群交换子，\(C_n\) 在 M 的
整数一阶同调中为零；上述基本群同构及交换化的自然性进一步给出

\[
[\gamma_n]=0\in H_1(S;\mathbb Z).
\tag{7}
\]

这里尚未以正迹代替本原性；本原性须由下一节核实。取逆改变定向但
不改变零同调与弧长，因此下文也适用于其无向 owner。

## 3. 完整 \(\bar\Gamma(3)\) 中的本原性

**命题 1。** (5) 的三个 [C_n] 均不是真幂。

设 \(B\in\Gamma(3)\)、整数 \(r\ge2\) 且 \([B]^r=[C_n]\)。
SL 提升给 \(B^r=\pm C_n\)；模 3 后只能取正号，故 \(B^r=C_n\)。
若只是共轭于真幂，可先共轭其根，仍归到这个等式。

由 (4)，\(\tau=\operatorname{tr}B\in2+9\mathbb Z[i]\)。\(\tau=2\)
时 B 的各幂迹均为 2，不可能；其余情形 \(|\tau|\ge7\)。
由 \(B^r=C_n\) 可选 B 的特征值 \(\mu,\mu^{-1}\)，使
\(R=|\mu|>1\)。于是

\[
R+R^{-1}\ge|\tau|\ge7,
\qquad R\ge(7+\sqrt{45})/2>6.
\tag{8}
\]

若 \(r\ge4\)，反三角不等式给

\[
|\operatorname{tr}B^r|
 =|\mu^r+\mu^{-r}|\ge R^r-R^{-r}>6^4-1=1295>731,
\]

与 (6) 矛盾。因此只需排除 r=2、3。

若 r=2，由 Cayley–Hamilton 恒等式得
\(\tau^2=T_n+2\in\{85,328,733\}\)。Gaussian 整数的平方若为正实数，
其虚部必须为零：写 \(\tau=a+bi\)，先由 \(2ab=0\)，再排除纯虚数
平方非正的情形。故 \(\tau\in\mathbb Z\)。但

\[
9^2<85<10^2,\qquad18^2<328<19^2,\qquad27^2<733<28^2,
\]

所以 r=2 不成立。

若 r=3，则 \(\operatorname{tr}B^3=\tau^3-3\tau\)。当 \(\tau\) 非实时，
(4) 给 \(|\tau|\ge\sqrt{85}\)。函数 \(s^3-3s\) 在 \(s>1\) 严格递增，故

\[
|\tau^3-3\tau|\ge|\tau|^3-3|\tau|
 \ge82\sqrt{85}>738>731.
\]

当 \(\tau\) 为实数时，\(\tau\in2+9\mathbb Z\)。排除 \(\tau=2\) 后，
要么 \(\tau=-7\)，给 \(\tau^3-3\tau=-322\)，不等于正迹 (6)；
要么 \(|\tau|\ge11\)，给 \(|\tau^3-3\tau|\ge11^3-33=1298>731\)。
r=3 同样不成立，命题得证。□

该证明允许潜在根 B 为复 Gaussian 矩阵，不只在实子群搜根，也没有
有限词球或最大幂次截断假设。相应闭速度轨道遂为真实本原轨道；若
存在更短返回，沿同一轴的返回变换会给群中真幂分解，与命题 1 矛盾。

## 4. 三条弧长的单位指数与有理独立

由 (6)，扩张根及弧长是

\[
\lambda_n=\frac{T_n+\sqrt{T_n^2-4}}2,
\qquad \ell_n=2\log\lambda_n,
\qquad e^{\ell_n}=U_n=\lambda_n^2>1.
\tag{9}
\]

因子 2 来自曲率 -1 上半空间：对角矩阵
\(\operatorname{diag}(\lambda_n,\lambda_n^{-1})\) 把轴高度 t 变为
\(\lambda_n^2t\)，轴上距离为 \(\int_t^{\lambda_n^2t}ds/s\)。
这沿用原弧长，不把词长度或标签范数当成物理时间。

具体地，

\[
\lambda_1=\frac{83+9\sqrt{85}}2,\qquad
\lambda_2=163+18\sqrt{82},\qquad
\lambda_3=\frac{731+27\sqrt{733}}2.
\tag{10}
\]

每个 \(\lambda_n\) 和 \(\lambda_n^{-1}\) 都满足
\(X^2-T_nX+1=0\)，故为代数整数；\(U_n\) 及其倒数也是代数整数，
即 \(U_n\) 是代数单位。各二次域共轭把 \(\lambda_n\) 变成其倒数。

**命题 2。** \(\ell_1,\ell_2,\ell_3\) 在 \(\mathbb Q\) 上线性独立。

先证明平方类 85、82、733 独立。若
\(85^a82^b733^e\) 为有理平方，\(a,b,e\in\{0,1\}\)，取素数 5、2
的赋值依次得 a=b=0；再由 \(27^2<733<28^2\) 得 e=0。
因此

\[
K=\mathbb Q(\sqrt{85},\sqrt{82},\sqrt{733})
\tag{11}
\]

是八次多二次域，三个平方根可以独立变号。这里的域次数事实也可
逐步核查：\(\mathbb Q(\sqrt{85},\sqrt{82})\) 有基
\(1,\sqrt{85},\sqrt{82},\sqrt{85\cdot82}\)。若其非零元素 z 的平方
在 \(\mathbb Q\)，每个变号自同构都将 z 变成 ±z；比较上述基的四个
不同变号特征，z 只能是其中一个基元的有理倍。733 的平方类不在这
四类中，所以再加入 \(\sqrt{733}\) 确实使次数翻倍。

设 \(\sum q_n\ell_n=0\)，清分母得到
\(\prod_n\lambda_n^{m_n}=1\)，\(m_n\in\mathbb Z\)。对 K 施以仅改变
第 n 个平方根符号的自同构，再与原式比较，得
\(\lambda_n^{2m_n}=1\)。因为 \(\lambda_n>1\)，必有 \(m_n=0\)。□

这里只证明三条明列长度的有理独立，不声称全部几何长度独立。
这也保证三个无向 owner 不会通过共轭、取逆或 PSL 符号而合并。

## 5. 任意固定实数共同时钟的三轨道障碍

所需外部结果是六指数定理：若 \(x_1,x_2,x_3\) 有理线性独立，且
\(y_1,y_2\) 有理线性独立，则六个 \(e^{x_i y_j}\) 中至少一个超越。
[Waldschmidt 作者讲稿，正文 p.4，“Six exponentials theorem”段][six]
给出一般条件 \(d\ell>d+\ell\)，这里取 3×2。使用的是该段的超越性
定理，而非紧随其后仅讨论有理值的证明草图。

**命题 3。** 对每个 \(c\in\mathbb R\setminus\{0\}\)，至少一个
\(c\ell_n\notin V_{\rm prime}\)。

若 c 为无理数，取 \(x_i=\ell_i\)、\((y_1,y_2)=(1,c)\)。命题 2
及 c 无理保证两组各自独立；\(e^{\ell_i}=U_i\) 都代数，所以六指数
定理迫使至少一个 \(e^{c\ell_i}\) 超越。另一方面，任何
\(y\in V_{\rm prime}\) 均有某正整数 D 使 \(e^{Dy}\in\mathbb Q_{>0}\)，
故 \(e^y\) 代数。因此三个 \(c\ell_i\) 不可能都属于此空间。

若 \(c=a/b\ne0\)，\(a\in\mathbb Z,b\in\mathbb Z_{>0}\)，假设任意一条
\(c\ell_i=y\in V_{\rm prime}\)。取 D 使 \(R=e^{Dy}\in\mathbb Q_{>0}\)，
则 \(U_i^{aD}=R^b\)。左侧是代数单位，右侧为正有理数，所以它只能
等于 1：一个有理代数整数是整数，其倒数亦为整数便只能是 ±1。
但 \(U_i>1,aD\ne0\)，矛盾。此分支实际上排除每一条匹配。□

两个分支不能混写：无理 c 排除三个指数全为代数；有理 c 的指数
本来可以代数，单位论证只排除这里的非零素数对数匹配。
同样，不声称任意超越 c 都有 \(cV_{\rm geo}\cap V_{\rm prime}=\{0\}\)：
对单条轨道事后选 \(c=\log p/\ell\) 即可匹配。命题 3 使用同一 c
同时作用于三个明确 owner，不通过 RH 目标表调定义。

## 6. 闭形式与周期余边界项的消去

按 (3) 沿任一旧周期轨道积分，得到

\[
T_\rho(\gamma)=\int_0^{\ell(\gamma)}\rho(\phi_t x)\,dt
=c\ell(\gamma)+u(\phi_{\ell(\gamma)}x)-u(x)
 +\sum_k a_k\int_\gamma\alpha_k.
\tag{12}
\]

u 全局单值且轨道闭合，故中间差为零。每个闭一形式的圈积分在同伦
下不变并对圈连接可加，因此是基本群到 \(\mathbb R\) 的同态，在
交换子上为零；等价地，它通过一阶同调因子化。Stokes 与同伦积分
公式可见 [Eliashberg, Proposition 12.1、Lemma 12.8][forms]。
结合 (7)，三条轨道满足

\[
T_\rho(\gamma_n)=c\ell_n.
\tag{13}
\]

因为 \(\rho>0\)、\(\ell_n>0\)，(13) 还迫使 c>0；c=0 或 c<0 的
表示不可能在这些轨道上给正时间密度。此后命题 3 即证明主结论。
不需要知道 \(b_1(M)\)，也不要求 \(a_k\) 有理或代数；闭形式项在
这些周期上分别为零，所以任意有限个实系数都消失。

特别地，\(\rho=c+Xu\) 在所有周期上给 \(c\ell\)，可直接继承固定
时钟障碍。本篇只使用这一正向积分结论，没有在非紧流形上援引未经
核查的 Livšic 逆定理。一般闭形式项可能区分正反向轨道，但 (13)
在这三条零同调见证的两个方向上相同，因此无向 owner 边界没有歧义。

## 7. 证据边界、反例检查与下一最小单元

本次增量是实际 \(\Gamma(3)\) 中的零同调本原三轨道证书及 (3) 类的
周期障碍，不是将抽象曲面或别的格的同调结论移植进来。

- 不排除任意正函数 \(\rho\)：非闭形式、非余边界的动力学项可能改变
  这些周期，须另给精确定义与独立证据；不能把 (3) 当成所有自然时钟。
- 不允许多值／带奇点的 u、只局部定义的闭形式或不合法的跨奇点积分
  偷用 (12) 的消去。有限形式族不是任意无限级数及其逐项积分结论。
- \(\rho>0\) 保证三条紧周期上的时间变换有效；未证明整个非紧相空间
  上的新流完备，也不声称这由正性单独保证。
- 没有近似配对误差下界、无限消去、跡公式或全局行列式不可能性结论；
  不更改任何原标签值域、协议、FAIL／BLOCK 或 Stage／Route 状态。

下一最小单元是独立核对三交换子的本原性与时间积分证书，再核对所选
候选的周期合同是否确实覆盖这三个 owner、时间密度是否确属 (3)。
本笔记自身不授权该后续行动，也不将多 agent 同意作为独立科学证据。

## 8. 来源、实际动作与保全

ARS 有界 argument-builder 用于区分对象、三个证明子链、反例边界与
来源支持；没有运行完整论文 pipeline、正式审查或新颖性判定。
矩阵乘法、有限幂次排除、平方类及时间积分均为 AI 辅助纸面推导；
外部定理被准确引用，不把本案构造归给这些作者。

普通网页浏览核对如下作者来源与命题定位，没有发送私有稿或笔记：

1. Michel Waldschmidt, *Extrapolation with interpolation determinants*，
   首页面题为 Madras, IMSc, 1997-01-20 workshop；正文 p.4 的
   “Six exponentials theorem”段。本案用其标准定理陈述，不声称完整
   重证六指数定理。该作者讲稿没有在此被冒称为原始发表论文。
2. Allen Hatcher, *Algebraic Topology*，作者在线书稿，Theorem 2A.1
   （正文 p.166）与 Theorem 4.41（正文 p.376）。只用于一般同调／
   基本群与纤维丛事实，不用于替代本案的具体群核查。
3. Yakov Eliashberg, *Multilinear algebra, differential forms and Stokes'
   theorem*，扉页 April 2018；Proposition 12.1（正文 p.191）、
   Lemma 12.8（正文 p.195）。只用于闭形式积分的标准背景。

页码均为在线 PDF 的正文印页，以定理／段名一并定位；抓取时间不作为
出版日期。此前 Ramachandra 原始论文仅核到出版社身份，PDF 获取失败，
故这里不用它承担已读原文证明的声明。实际本地动作仅为读取指令和
既有材料、以 apply_patch 新建本文件及对本文件作只读静态检查。
没有科学／符号程序、枚举、实验、producer、构建、旧文件改写或状态升级。

[units]: internal_algebraic_unit_lengths_and_prime_log_obstruction_20260909.md
[family]: internal_infinite_primitive_split_obstruction_family_20260908.md
[six]: https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/EID.pdf
[hatcher]: https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
[forms]: https://math.stanford.edu/~eliash/Public/math177/177-diff-forms.pdf
