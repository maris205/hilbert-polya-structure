# P29：有限全群共轭判定与人口无关 primitive-owner 规范代表

日期：2026-09-09 UTC。Goal 01 内部纸面理论推进。
本篇只新增一个研究笔记；不运行矩阵枚举、群程序、owner producer、
census、冻结输入 replay、实验或正式 Gate／Route／Stage 工作。

## 0. 结论与输入边界

对实际群
\[
\Gamma=\{A\in SL_2(\mathbb Z[i]):A\equiv I\pmod3\}
\tag{1}
\]
的任意两个 exact loxodromic 元素，本文给出完整群内共轭子的
显式有限 Gaussian 高度界。因此共轭与不共轭在数学上都有一个
有限完备的精确检验过程，不依赖预先猜定的词球。

结合[逐元素有限最大根定理][roots]，并补证不同幂指数下的正向
primitive-root 唯一性，得到定义在全部 admissible exact
loxodromic 矩阵上的有向和无向 primitive-owner 规范代表。
规范性相对于本文一次固定的数学全序，不依赖观测人口、遍历次数、
输入顺序或共轭见证。

这补的是[原稿 Gate Q][gate]的一部分抽象数学接口，不提供其实际
执行、逐行覆盖、serialization、owner bytes 或正式关卡结论。
历史笔记当时所列缺口仍保留原貌，不被本文回写。

## 1. 已有群事实及记号

沿用[最大根笔记，§1–3][roots]已展开的事实：
投影 \(\Gamma\to PSL_2(\mathbb C)\) 单射；
\(-I\notin\Gamma\)；\(\Gamma\) 无挠；每个元素满足
\[
\operatorname{tr}A\in2+9\mathbb Z[i].
\tag{2}
\]
若 A 为 loxodromic，则
\[
|\operatorname{tr}A|\ge7,\qquad
\ell_A\ge\delta:=2\operatorname{arcosh}(7/2),\qquad
\cosh\delta-1=45/2.
\tag{3}
\]
曲率固定为 -1，\(\ell_A\) 是 A 的平移长度。
这不是非紧商流形的全局 injectivity-radius 下界。

对任何 \(A=(a_{jk})\in SL_2(\mathbb C)\)，记
\[
S_A:=\sum_{j,k=1}^2|a_{jk}|^2.
\tag{4}
\]
对 Gaussian 整数矩阵 \(S_A\) 为正整数。对 loxodromic A，
另记
\[
N_A:=|\operatorname{Re}\operatorname{tr}A|
     +|\operatorname{Im}\operatorname{tr}A|\in\mathbb Z_{\ge0}.
\tag{5}
\]
若扩张特征值模长为 \(\rho_A=e^{\ell_A/2}>1\)，由特征方程
\(\lambda_A=\operatorname{tr}A-\lambda_A^{-1}\) 得
\[
e^{\ell_A/2}=\rho_A
<|\operatorname{tr}A|+1\le N_A+1.
\tag{6}
\]
(3)、(6) 是严格控制常数的输入，不计算复对数分支。

PSL 中的共轭等式提升后至多有一个中央负号；因为全部矩阵
及共轭子均约化为 \(I\pmod3\)，该负号不可能出现。因此
\[
[A]\sim_{\bar\Gamma}[B]\iff
\exists G\in\Gamma:\ GA=BG.
\tag{7}
\]
以下处理右侧的字面 exact matrix equality。

## 2. 矩阵高度、轴距与位移

### 2.1 基点位移的矩阵恒等式

取上半空间基点 \(o=(0,1)\in\mathbb H^3\)。对
\(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\)，令
\(D=|c|^2+|d|^2>0\)、\(v=a\bar c+b\bar d\)。
标准上半空间作用在此点给出
\[
Ao=(v/D,\,1/D).
\tag{8}
\]
由 \(ad-bc=1\) 的二维 Gram 行列式恒等式，
\[
|v|^2+1=(|a|^2+|b|^2)D.
\tag{9}
\]
上半空间距离公式于是直接给
\[
2\cosh d(o,Ao)
=\frac{|v|^2+1+D^2}{D}
=|a|^2+|b|^2+|c|^2+|d|^2=S_A.
\tag{10}
\]
这对任意 \(SL_2(\mathbb C)\) 矩阵成立，不需要 A 本原。

### 2.2 轴距公式及自含验证

设 \(L_A\) 为 loxodromic A 的轴，\(r_A=d(o,L_A)\)，
旋转角为 \(\theta_A\)。则
\[
\cosh d(o,Ao)
=\cosh\ell_A+
 (\cosh\ell_A-\cos\theta_A)\sinh^2r_A.
\tag{11}
\]
该公式也可在 Culler--Shalen 作者稿
[§2.5，式 (2.5.2)，印刷页 6][cs]核查。这里只使用这个局部
双曲几何恒等式，不使用该文的一尖点体积／同调主定理。

为使本篇不依赖外部公式的未展开推论，取 Lorentz 度量
\(-dx_0^2+dx_1^2+dx_2^2+dx_3^2\)。适当等距变换后，可使轴
位于 \((x_0,x_3)\) 平面，最近轴点为 \((1,0,0,0)\)，而
\[
o=(\cosh r_A,\sinh r_A,0,0),
\]
\[
Ao=(\cosh r_A\cosh\ell_A,\,
     \sinh r_A\cos\theta_A,\,
     \sinh r_A\sin\theta_A,\,
     \cosh r_A\sinh\ell_A).
\tag{12}
\]
取负 Lorentz 内积即得
\(\cosh^2r_A\cosh\ell_A-\sinh^2r_A\cos\theta_A\)，
展开 \(\cosh^2r_A=1+\sinh^2r_A\) 得 (11)。
旋转角符号改变不影响等式。

由 (3)、(10)、(11)，
\[
\sinh^2r_A
=\frac{S_A/2-\cosh\ell_A}
       {\cosh\ell_A-\cos\theta_A}
\le \frac{S_A}{45}.
\tag{13}
\]
分母正且至少 \(45/2\)。写 \(u=\sinh r_A\ge0\)，利用
\(\sqrt{1+u^2}\le1+u\) 与 \(2u\le1+u^2\)，得到
\[
e^{r_A}=\sqrt{1+u^2}+u
\le2+u^2
\le2+S_A/45
\le S_A+2.
\tag{14}
\]
最后取了较松的整数表达，以免检验阶段需要近似轴距。

## 3. 共轭子的显式有限高度界

**定理 1。** 对任意 loxodromic \(A,B\in\Gamma\)，定义正整数
\[
K(A,B):=(S_A+2)(S_B+2)(N_B+1).
\tag{15}
\]
若存在 \(G\in\Gamma\) 使 \(GAG^{-1}=B\)，则存在另一个这样的
共轭子 \(G'\in\Gamma\)，满足
\[
\boxed{S_{G'}<2K(A,B).}
\tag{16}
\]

**证明。** 取 o 到两条轴的最近点 \(x_A\in L_A\)、
\(x_B\in L_B\)。G 把 \(L_A\) 送到 \(L_B\)，故 \(Gx_A\in L_B\)。
B 在自己的轴上是长度 \(\ell_B\) 的平移；可选某个
\(k\in\mathbb Z\) 使
\[
d(B^kGx_A,x_B)\le\ell_B/2.
\tag{17}
\]
令 \(G'=B^kG\)。仍有 \(G'AG'^{-1}=B\)，且 \(G'\in\Gamma\)。
沿 \(o,x_B,G'x_A,G'o\) 的路径并用等距性，有
\[
d(o,G'o)\le r_B+\ell_B/2+r_A.
\tag{18}
\]
由 (6)、(14)，
\[
e^{d(o,G'o)}
\le e^{r_A}e^{r_B}e^{\ell_B/2}
<(S_A+2)(S_B+2)(N_B+1)=K(A,B).
\tag{19}
\]
再由 (10) 及 \(2\cosh t\le2e^t\)（\(t\ge0\)），得
\(S_{G'}\le2e^{d(o,G'o)}<2K(A,B)\)。证毕。

(17) 只用 B 的整幂，不需要 B 已为本原，也不需要完整中心化子
生成元。旋转 holonomy 在轴上没有额外位移。全证明不要求商流形
紧、选择基本域的数值顶点、群生成词长界或预先得到一个小共轭子。

## 4. 有限精确判定与否定证书的含义

定义
\[
\mathcal C_{A,B}:=
\{G\in M_2(\mathbb Z[i]):
 S_G\le2K(A,B),\ \det G=1,\ G\equiv I\pmod3\}.
\tag{20}
\]
每个条目的实、虚部分都在一个有限整数区间内：
例如使用较松的 \([-2K,2K]\) 即足够；或用整数平方根
\(\lfloor\sqrt{2K}\rfloor\) 缩小候选盒。再按 (20) 过滤即可。
所有运算是 Gaussian 整数加乘、比较及同余，不需浮点轴线运算。

于是有精确等价
\[
\boxed{A\sim_\Gamma B
\iff \exists G\in\mathcal C_{A,B}:\ GA=BG.}
\tag{21}
\]
向右由定理 1，向左由 \(\det G=1\) 的 exact inverse。
若 \(\operatorname{tr}A\ne\operatorname{tr}B\)，可先直接排除；
迹相等本身不是共轭充分条件。

(20)–(21) 给出数学上的有限完备决策：
找到一项即可给正共轭见证；全部有限候选都检验完且均失败才给
完整否定结论。只检查部分盒、只搜索有限时间或只处理若干词，
都不构成此处的否定证书。
本文没有执行任何候选枚举，也没有声称这个粗界实用或计算复杂度低。

输入域严格为 exact loxodromic \(A,B\in\Gamma\)。
后文调用时会显式保持这个前提，不把本判定器未经证明地用于
identity、parabolic 或群外候选。

## 5. 跨幂指数的正向 primitive-root 唯一性

[最大根笔记][roots]已给有限完备的全部正整数根检验，
并证明最大指数根本原、同指数根唯一。
为让 owner 对任意正遍历不变，这里补上不同指数之间的命题。

**引理 2。** 若 \(P,Q\in\Gamma\) 均本原，且
\[
P^m=Q^n=A,\qquad m,n\in\mathbb Z_{>0},
\tag{22}
\]
其中 A 为 loxodromic，则 \(P=Q\) 且 \(m=n\)。

**证明。** P、Q 均交换 A；在 A 的不同特征线基中都对角，
故 \(PQ=QP\)。写 \(d=\gcd(m,n)\)、\(m=dm'\)、\(n=dn'\)。
则
\[
(P^{m'}Q^{-n'})^d=I.
\]
由无挠性，\(P^{m'}=Q^{n'}\)。取整数 u、v 使
\(um'+vn'=1\)，并定义 \(R=P^vQ^u\in\Gamma\)。交换性给
\[
R^{n'}=P^{vn'}Q^{un'}
=P^{vn'+um'}=P,
\]
\[
R^{m'}=P^{vm'}Q^{um'}
=Q^{vn'+um'}=Q.
\tag{23}
\]
本原性迫使 \(n'=m'=1\)，故 P=Q、m=n=d。证毕。

因此可无歧义地记最大根笔记得到的唯一正向本原根为 \(P(A)\)。
对于全部 \(k\ge1\)、\(G\in\Gamma\)，引理给
\[
P(A^k)=P(A),\qquad
P(GAG^{-1})=GP(A)G^{-1},\qquad
P(A^{-1})=P(A)^{-1}.
\tag{24}
\]
例如 \(A^k=P(A)^{mk}\)，与 \(A^k\) 自身的本原根应用引理；
另两式中，共轭或取逆均保持本原性，并提供对应的正幂分解。
这不是在所有交换子群上未经证明地假设一个循环参数化。

## 6. 固定全序与有限取得的全局最小代表

对每个 Gaussian 矩阵 \(M=(m_{jk})\)，定义整数元组
\[
\begin{aligned}
J(M)=(&S_M,\operatorname{Re}m_{11},\operatorname{Im}m_{11},
\operatorname{Re}m_{12},\operatorname{Im}m_{12},\\
&\operatorname{Re}m_{21},\operatorname{Im}m_{21},
\operatorname{Re}m_{22},\operatorname{Im}m_{22}).
\end{aligned}
\tag{25}
\]
按这个元组的通常字典序排序。
虽然整数条目自身没有下界，首坐标 \(S_M\) 为非负整数，
每个固定高度层只有有限个 Gaussian 矩阵；所以 (25) 在
\(\Gamma\) 上是一个全序且每个非空子集都有最小元。
完整条目元组也保证不同矩阵的键不同。

给 loxodromic input A，令 \(P=P(A)\)，定义
\[
\mathcal O_+(P)=\{GPG^{-1}:G\in\Gamma\},
\]
\[
\mathcal O_\pm(P)=
\{GP^\epsilon G^{-1}:G\in\Gamma,\ \epsilon\in\{1,-1\}\},
\tag{26}
\]
及
\[
C_+(A):=\min_J\mathcal O_+(P),\qquad
C_\pm(A):=\min_J\mathcal O_\pm(P).
\tag{27}
\]

(27) 不只是一个无穷集合的非构造选择。因为 \(P\in\mathcal O_+(P)\)，
两个最小值的高度都至多 \(S_P\)。因此只需考虑有限集合
\[
\mathcal F_P:=
\{M\in\Gamma:S_M\le S_P,\ \operatorname{tr}M=\operatorname{tr}P\}.
\tag{28}
\]
这里的**迹过滤不可省去其逻辑作用**：
它使每个 M 满足 \(|\operatorname{tr}M|=|\operatorname{tr}P|\ge7\)，
从而 M 必为 loxodromic；单位模特征值、parabolic 或 identity
的迹都不满足这个界。故可合法地对每个候选调用 (21)。

用 (21) 分别检验 \(M\sim_\Gamma P\) 与
\(M\sim_\Gamma P^{-1}\)，再取通过集合的最小 J，就得到 (27)。
原共轭类及其逆类都具有同一迹，故 (28) 不漏掉任何可能的
最小代表。一次外层有限候选和每项一次或两次内层有限共轭
检验的复合仍然有限。最大根步骤亦已由[roots]证明有限。

(25) 是本篇的数学约定，不是对旧 owner bytes 的编码提案、
版本迁移或实现选择。其它预先固定且具有有限高度初段的全序
可以给不同代表，不能混称为同一套未版本化的数据身份。

## 7. 全域 owner 分类、方向与人口无关性

**定理 3。** 对全部 admissible exact loxodromic \(A,B\in\Gamma\)，
\[
C_+(A)=C_+(B)
\iff P(A)\sim_\Gamma P(B),
\tag{29}
\]
\[
C_\pm(A)=C_\pm(B)
\iff P(A)\sim_\Gamma P(B)
\ \text{或}\ P(A)\sim_\Gamma P(B)^{-1}.
\tag{30}
\]

同一个轨道集合显然有同一最小元。反过来，若最小元相同，
则两个共轭类（或并入逆类的轨道）相交，群作用的轨道性质
使它们相同，给 (29) 或 (30)。整个定义只用输入、固定群与
固定全序；没有使用某个有限人口作为取最小值的范围。
由 (24)，也对正遍历次数和共轭见证不变。

本群中正向 primitive owner 与其逆向 owner 总不同。
若 \(GPG^{-1}=P^{-1}\)，G 必交换 P 的两条不同特征线。
在 P 特征基中 G 是
\[
G=\begin{pmatrix}0&u\\v&0\end{pmatrix},
\qquad -uv=1,\qquad G^2=-I.
\tag{31}
\]
但 \(G\in\Gamma\) 会使 \(G^2\in\Gamma\)，与
\(-I\notin\Gamma\) 矛盾。PSL 共轭的中央符号已由 (7) 排除。
故
\[
C_+(A^{-1})\ne C_+(A),\qquad
C_\pm(A^{-1})=C_\pm(A).
\tag{32}
\]
不声称 \(C_+(A^{-1})=C_+(A)^{-1}\)：
(25) 的字典序未被证明在取逆下保序。

有向 primitive class 的 inverse 操作是无不动点的 involution，
(30) 每个无向 owner 恰对应两个有向 owners。
(27) 仍不能把两条有向周期轨道在有向 Ruelle／Selberg Euler
产品中随意合并；计数方向约定必须由实际目标定义决定。

## 8. 已补齐的数学接口与不能越过的执行边界

本篇与[roots]合起来，针对全部 exact loxodromic 群元素给出：

- 有限完备的正向最大根判定与跨幂指数唯一性；
- 完整 level-(3) 群内的共轭／不共轭有限判定；
- 无向关系的取逆与传递闭包的精确定义；
- 相对固定数学全序的人口无关有向／无向规范代表。

仍然没有完成[Gate Q][gate]所需的全部实际工作：

- frozen IDs／words 到 exact matrices 的版本化 binding；
- 给定全部输入行及排除、重复、Attach／Separate 的覆盖；
- 候选过程的真实执行、耗时可行性、独立实现 replay；
- 可审计的负证书数据、injective serializer 和 owner bytes；
- 原 fixtures、locks、hash receipts 的批准集成或迁移。

这里的有限性是数学终止证明，不是已执行的有限 census。
Gate M 的素理想机制、机制登记与 owner law 不由规范共轭代表
自动产生；更不产生指定素数周期、目标零点、量子算子或全局
量子 determinant identity。正式 Gate、Route 和 Stage 均保持原状。

## 9. 来源与实际动作

主代理完整读审[最大根笔记][roots]及其 §7 的历史边界，并以
[自然返回振幅笔记][amplitude]的实际迹同余／曲率约定核对常数。
本篇对 (10)–(14)、有限共轭界、Bézout 根唯一性及规范化逐步推导。
Culler--Shalen 作者稿 §2.5 式 (2.5.2) 的实际公式段落已核读；
来源仅支持 (11) 的通用几何身份，(15)–(32) 是本案推导，
不冒称为原作者的本群算法或 Gate 结论。

本篇使用 ARS 的有界论证／反方核查方法，区分数学证明、
独立来源支持和实际输入检验。两个有界同模型逻辑校对不是
独立科学证据。实际动作仅为只读材料核查、apply_patch 新文件、
完整回读及一次必要的局部文字静态检查。
没有枚举、科学／符号程序、producer、census、实验、旧输入修改、
正式 build 或 Route／Stage 晋升。静态文本检查也不证明本定理。

[roots]: internal_goal01_finite_maximal_root_decision_for_fixed_element_20260909.md
[amplitude]: internal_goal01_geometric_return_amplitude_and_laplace_bound_20260909.md
[gate]: stage4_prime_revision_round6.tex
[cs]: https://homepages.math.uic.edu/~shalen/cusp1.pdf

