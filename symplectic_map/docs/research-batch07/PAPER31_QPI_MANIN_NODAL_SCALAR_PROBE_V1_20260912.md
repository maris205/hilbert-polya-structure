# Proof Package：原 qPI 有限节点的准确标量交数探查 V1

日期：2026-09-12 UTC。作者：`/root/p31_manin_nodal_scalar_probe_v1`。
类型：`AUTHOR_SIDE_BOUNDED_PROBE / EXACT_NODAL_SCALAR_CLAIM`。
`route_applicability: NOT_APPLICABLE`。不是数学接受处置、独立审查票、正式候选或论文。

## Claim

原问题是：对原族有限节点，已接受固定理想中的标量交数能否不再留作定义式输入？
本件给出全部有限节点、全部迭代次数的准确公式；不处理好纤维和尖点。
特别是，首次相交的准确交数不是任意未知数，而只有 $1,2$ 两种可能。

设 $k$ 代数闭、$\operatorname{char}k=p>3$、$T\in k^\times$，保持

$$
W_h:\ v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\quad O=[0:1:0].
\tag{1}
$$

任取有限节点能级 $h_0$。下文从原唯一奇点计算 $w$，满足

$$
T=w^3(w-1),\qquad h_0=w(3-2w),\qquad w\ne0,1,3/4.
\tag{2}
$$

令 $\zeta$ 是下列二次方程的任意一个根：

$$
(w-1)\zeta^2+(2w-1)\zeta+(w-1)=0.
\tag{3}
$$

两根互逆；它们表示原 $P$ 或 $-P$ 的节点乘法元素，不是任意更换回返点。
写 $n=p^a m$，其中 $a\ge0$、$p\nmid m$。则本件证明

$$
\boxed{
i_n(h_0)=
\begin{cases}
0,&\zeta^m\ne1,\\
2p^a,&\zeta^m=1,\ p>5,\ (T,h_0)=(3/16,-2),\\
p^a,&\zeta^m=1,\ (T,h_0)\ne(3/16,-2).
\end{cases}}
\tag{4}
$$

特征 $5$ 的 $(3/16,-2)$ 是尖点而不是节点，故 (4) 已穷尽原节点量词。
这里 $i_n=(nP.O)_{h_0}$，不相交时取零，沿原参数 $\epsilon=h-h_0$ 计算。
(2)–(4) 只需原奇点、一个二次根及有限次乘幂，不以未知 $i_d$ 或除法多项式赋值重述答案。

等价地，若 $\zeta$ 非根单位，则全部 $i_n=0$；若其精确阶为 $d$，则 $p\nmid d$，
$d\nmid n$ 时 $i_n=0$，$d\mid n$ 时 $i_n=p^{v_p(n)}i_d$，而 $i_d$ 已准确求为 $1$ 或 $2$。
本件不把最后这个标准传播公式充作求出 $i_d$。

## Status

`PROVABLE AS STATED`，仅指 (1)–(4) 的有界作者断言；下面供应完整证明。
原有限节点标量目标保持不变，没有静默缩成一般时间、素域能级或 $p\nmid n$。
数学接受仍须 fresh 非作者核查；本件不自授长文新意、价值、容量或完整准入 PASS。
Paper31 仍为正文22–30页及原完整准入，整批仍4/5；没有建立项目、锁、稿件或PDF。

## Assumptions and notation

- 只消费 [ACCEPT] 已接受的原模型、泛非挠性、全基标记共轭与节点固定理想；不重新证明这些接口。
- $S=(a_0,b_0)$ 是原唯一节点，$z_0=b_0/a_0$，$w=a_0/z_0$；这些符号只用于确定原参数。
- $q$ 是本证明引入的 Tate 平滑化参数，不是原映射乘数、原时间 $T$ 或有限域大小。
- $Z$ 是可变乘法坐标，$\zeta=Z(0)$；$R(Z)=Z^2+Z+1$。
- $t_O=-u/v$ 是原模型 $O$ 处的局部参数。取负是固定 $O$ 的同构，故不改变交数。
- $\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$ 是原有限坏值多项式。
- 所有 $O(q^r)$ 指 $q$ 进阶数；构造后将证明 $q$ 与原 $\epsilon$ 相差单位，无分歧换基。

## Prior collision boundary

[COLLISION] §5 和旧 [I03] 明确已有全阶交点问题；旧I03首先询问特征零好纤维，不能声称本件首次提出交数。
[SINGULAR] 已给节点正规化、原乘法元素、点阶与周期；[ACCEPT] 已给全部 $n$ 的固定理想。
这些旧输入全部扣除，本件不改名重证。新增声称仅是原固定 $T$ 切片的准确首阶系数、
唯一二阶例外及其二阶首项，从而去掉节点理想中尚未求值的 $i_d$。
[NASK] Lemma 8.2 已有特征 $p$ 的形式群传播，乘法约化时 Hasse 系数为单位；其标准后果不另计新意。
本件的 Tate 级数、标点归一化和局部逆函数法也均作为标准方法扣除；没有完成全球先例排除。

## Proof strategy and dependency map

1. 原奇点关系给 (2)，并选 (3) 的根；所有分母和节点边界先核定。
2. 对 Tate 曲线上的实际点作显式长 Weierstrass 变换，得到恰好 (1) 的两个参数函数。
3. 保持 $T$ 恒定，形式隐函数给 $Z(q)$；直接导数证明原 $h$ 参数没有分歧。
4. 两个准确 Taylor 系数给 $\operatorname{ord}(Z(q)-\zeta)=1$ 或 $2$；不是只检查必要一阶消失。
5. Tate 群同态及 $O$ 附近的局部参数把这个阶变成 $i_d$；最后做标准乘 $p$ 传播。

外部数学依赖只有 [TATE] 的整数系数级数与乘法群同态；使用于完备域 $k((q))$。
不依赖未读的全模空间变形定理，也不从节点切表示猜测全形式对角化。

## Proof

### Step 1. 从原节点计算参数，并排除全部危险分母

旧 [SINGULAR] 的原方程消元给
$a_0=T-z_0^2$、$a_0^2=Tz_0$、$h_0=T/z_0-3z_0$，且 $a_0z_0\ne0$。
其恒等式在任意代数闭常数域同样成立，证明只用原多项式偏导，不依赖有限域计数。
设 $w=a_0/z_0$，依次得到 $T=w^2z_0$、$z_0=w(w-1)$，从而得到 (2)。
原切向二次式的判别式为 $w^2(4w-3)$，所以节点准确排除 $w=3/4$；$T\ne0$ 排除 $0,1$。

(3) 的判别式为 $4w-3\ne0$，常数项非零，所以两根不同、非零且互逆。
$Z=-1$ 代入 (3) 得 $-1\ne0$；$Z=1$ 代入得 $4w-3\ne0$。
整理 (3) 得

$$
w=\frac{R(\zeta)}{(\zeta+1)^2},\qquad
R(\zeta)\ne0,\qquad \zeta\ne0,1,-1.
\tag{5}
$$

其中 $R(\zeta)\ne0$ 由 $w\ne0$ 得到。通用公式的分母除 $2,3$ 外只含这些已证单位；例外简式另限 $p>5$。

### Step 2. 显式构造原带点模型，固定平移符号

[TATE] 的曲线与点写为

$$
E_q:\ Y_c^2+X_cY_c=X_c^3+a_4(q)X_c+a_6(q),\qquad Q_Z=(X(Z,q),Y(Z,q)).
\tag{6}
$$

其 $Z$ 乘法给点加法；$a_4=-5q-45q^2+O(q^3)$、$a_6=-q-23q^2+O(q^3)$。
所需展开直接来自该源式 (4)、(11)、(14)：

$$
\begin{aligned}
X&=\frac{Z}{(1-Z)^2}+(Z+Z^{-1}-2)q
 +(2Z^2+Z+Z^{-1}+2Z^{-2}-6)q^2+O(q^3),\\
Y&=\frac{Z^2}{(1-Z)^3}+(1-Z^{-1})q
 +(Z^2-Z^{-1}-3Z^{-2}+3)q^2+O(q^3).
\end{aligned}
\tag{7}
$$

定义切线斜率、系数和单位缩放

$$
M=\frac{3X^2+a_4-Y}{2Y+X},\qquad A=3X-M-M^2,\qquad B=2Y+X,\qquad \lambda=B/A.
\tag{8}
$$

作 $X_c=X+\lambda^2u$、$Y_c=Y+M\lambda^2u+\lambda^3v$。
点方程消去常数项，切线方程消去一次 $u$ 项；其余长 Weierstrass 系数准确为

$$
\mathsf T(Z,q)=-A^3/B^2,\qquad
\mathsf H(Z,q)=(1+2M)A/B.
\tag{9}
$$

归一化方程是 $v^2+\mathsf Huv-\mathsf Tv=u^3-\mathsf Tu^2$，没有另换族。
原 Tate 点 $Q_Z$ 映到 $(0,0)=-P$，另一点 $(0,\mathsf T)$ 才是原指定 $P$。
所以原 $nP$ 对应乘法参数 $Z^{-n}$；零交数与接触阶可等价用 $Z^n$ 计算，但首项符号须取负。

在 $q=0$，直接代入 (7)–(9) 得

$$
\begin{gathered}
A_0=\frac{ZR}{(Z-1)^2(Z+1)^2},\quad
B_0=-\frac{Z(Z+1)}{(Z-1)^3},\quad
\lambda_0=-\frac{(Z+1)^3}{(Z-1)R},\\
\mathsf T_0=-\frac{ZR^3}{(Z+1)^8},\qquad
\mathsf H_0=\frac{R(Z^2+4Z+1)}{(Z+1)^4}.
\end{gathered}
\tag{10}
$$

由 (5)，$\mathsf T_0(\zeta)=w^3(w-1)=T$、$\mathsf H_0(\zeta)=w(3-2w)=h_0$。
因此闭纤维确为原方程及原标点，且 $A,B,\lambda$ 均为单位。此处没有未指定的标点同构。

### Step 3. 固定原时间后的准确一、二阶系数

将 $\mathsf T=\mathsf T_0+\mathsf T_1q+\mathsf T_2q^2+O(q^3)$ 展开，(7)–(9) 给

$$
\begin{aligned}
\mathsf T_0'&=\frac{(Z-1)^3R^2}{(Z+1)^9},\\
\mathsf T_1&=\frac{(Z-1)^4R^3(3Z^2+4Z+3)}{Z^2(Z+1)^8},\\
\mathsf T_2&=-\frac{(Z-1)^4R^3 K(Z)}{Z^5(Z+1)^8},\\
K(Z)&=3Z^8-12Z^7-15Z^6-19Z^5-4Z^4-19Z^3-15Z^2-12Z+3,\\
\mathsf H_1&=-\frac{(Z-1)^4(Z^2+1)R(Z^2+3Z+1)}{Z^3(Z+1)^4}.
\end{aligned}
\tag{11}
$$

为使二阶计算可直接重做，(8) 中还可用

$$
\begin{gathered}
A_1=-\frac{(Z-1)^2R}{Z^2},\quad
A_2=-\frac{(Z-1)^2R(2Z^4+2Z^3+Z^2+2Z+2)}{Z^4},\\
B_1=\frac{(Z-1)(Z+1)}Z,\quad
B_2=\frac{(Z-1)(Z+1)(4Z^2+Z+4)}{Z^2},\\
\frac{\mathsf T_2}{\mathsf T_0}
=\frac{3A_2}{A_0}+\frac{3A_1^2}{A_0^2}+\frac{3B_1^2}{B_0^2}
-\frac{2B_2}{B_0}-\frac{6A_1B_1}{A_0B_0}.
\end{gathered}
\tag{12}
$$

这些是有理函数恒等式，不是有限参数拟合。所有系数在 (5) 的整数局部化中，故可直接降模。
由于 $\mathsf T_0'(\zeta)\ne0$，形式隐函数递推给唯一 $Z(q)\in k[[q]]$，
$Z(0)=\zeta$ 且 $\mathsf T(Z(q),q)=T$。每一步只除同一单位 $\mathsf T_0'(\zeta)$。
于是

$$
Z(q)=\zeta+c_1q+c_2q^2+O(q^3),\qquad
c_1=-\frac{\mathsf T_1(\zeta)}{\mathsf T_0'(\zeta)}.
\tag{13}
$$

令 $h(q)=\mathsf H(Z(q),q)$。由 (11) 的直接消元，

$$
L:=h'(0)=\mathsf H_1-\mathsf H_0'\frac{\mathsf T_1}{\mathsf T_0'}
=-\frac{(\zeta-1)^6R(\zeta)}{\zeta^3(\zeta+1)^2}\ne0.
\tag{14}
$$

所以 $\epsilon=h(q)-h_0=Lq+O(q^2)$。其形式逆给 $k[[\epsilon]]=k[[q]]$，
将 (9) 得到的整个带点族识别为原固定 $T$ 族；交数不被分歧放大。
这是本证明构造的无分歧参数校准，不以 Tate 模空间的泛存在断言替代。

若 $f(\zeta):=3\zeta^2+4\zeta+3\ne0$，则 $c_1\ne0$，故 $\operatorname{ord}_q(Z-\zeta)=1$。
若 $f(\zeta)=0$，则 $c_1=0$，二阶隐函数等式准确化为 $c_2=-\mathsf T_2(\zeta)/\mathsf T_0'(\zeta)$。
在 $\mathbb Z[1/6,Z]/(f)$ 的相关单位局部化中，(10)–(11) 的余式为

$$
\mathsf T_0=3/16,\qquad \mathsf H_0=-2,\qquad \mathsf T_2=-125/81.
\tag{15}
$$

当 $p=5$ 时 $f(Z)=3(Z-1)^2$，与 (5) 冲突；所以节点不可能出现这个一阶消失。
当 $p>5$ 时 (15) 非零，故 $c_2\ne0$，准确得到 $\operatorname{ord}_q(Z-\zeta)=2$。
又由 (5)，$f(\zeta)=0$ 等价于 $w=-1/2$，给原参数 $(3/16,-2)$。
反过来，$h_0=-2$ 给 $(w-2)(2w+1)=0$；$w=2$ 时 $T=8$，
与 $3/16$ 的差为 $125/16$，在 $p>5$ 不为零。所以原参数条件也充分。
另直接核验 $\delta_h(3/16,-2)=-125/4$；这与 $p=5$ 的尖点碰撞和其它特征的节点一致。

### Step 4. 从乘法坐标的准确阶到原 $i_d$

取 $K=k((q))$。由 [TATE] 的整数系数乘法同态，$[n]Q_Z$ 的参数为 $Z(q)^n$。
在单位参数 $V$ 的 $V=1$ 邻域，其级数有
$X(V,q)=V/(1-V)^2+qF$、$Y(V,q)=V^2/(1-V)^3+qG$，
其中 $F,G$ 在 $V=1$ 正则。故

$$
-\frac{X(V,q)}{Y(V,q)}
=\frac{V-1}{V}
\frac{1+qF(1-V)^2/V}{1+qG(1-V)^3/V^2}
=(V-1)\cdot\mathrm{unit}.
\tag{16}
$$

式 (8) 的坐标变换在 $O$ 附近使原 $t_O$ 等于此参数乘一个单位，首系数为 $\lambda$。
因此原交数准确为 $\operatorname{ord}_q(Z(q)^n-1)$，若 $\zeta^n\ne1$ 则为零。
这一步保留 $O$ 截面的局部理想，不是仅作剩余点集比较。

若 $\zeta$ 的有限阶为 $d$，则 $p\nmid d$，因为特征 $p$ 的乘法群无非平凡 $p$ 次单位根。
函数 $V^d-1$ 在 $V=\zeta$ 的导数为 $d\zeta^{-1}\ne0$，故
$i_d=\operatorname{ord}_q(Z-\zeta)$。Step 3 因而准确给 $i_d=1$ 或 $2$。
还有可直接检验的原参数首项：

$$
t_O(dP)=d\frac{2w+1}{w(4w-3)^3}\epsilon+O(\epsilon^2);
\quad
\left.t_O(dP)\right|_{(T,h_0)=(3/16,-2)}
=-\frac{3d}{3125}\epsilon^2+O(\epsilon^3)\quad(p>5).
\tag{17}
$$

第一式由 $-\lambda_0d\zeta^{-1}c_1/L$ 化简；第二式由
$-\lambda_0d\zeta^{-1}c_2/L^2=\lambda_0d\zeta^{-1}\mathsf T_2/(\mathsf T_0'L^2)$
模 $f$ 化简。负号来自本件始终保持的 $Q_Z=-P$，没有交换原指定点后遗漏符号。
这些首项的系数分别在非例外、例外节点非零，排除了更高阶接触的隐藏可能。

### Step 5. 全部迭代次数与算术边界

令 $n=p^a m$、$p\nmid m$。若 $\zeta^m\ne1$，则 $\zeta^n\ne1$，所以 $i_n=0$。
若 $\zeta^m=1$，则 $V^m-1$ 在 $\zeta$ 有单根，而且

$$
Z(q)^n-1=(Z(q)^m-1)^{p^a}.
\tag{18}
$$

所以 $i_n=p^a\operatorname{ord}_q(Z-\zeta)$，与 Step 3 合并得到 (4)。证毕。
传播 (18) 是标准乘法形式群机制，亦为 [NASK] Lemma 8.2 的乘法约化情形，不作新贡献。
一般 $k$ 中 $\zeta$ 可以非挠，此时 (4) 自动给全部零；不能假设代数闭域中每个元素都是根单位。
唯一例外的 $\zeta$ 则属于 $\overline{\mathbb F}_p$，所以在 $p>5$ 确实有有限阶 $d$ 并实现 $i_d=2$。
其两根的阶相同；求它随全部素数的阶分布不是本件结论，也不是交数公式留下的未求标量。

同一证明还给一个不扩展问题范围的特征零边界：所有有限节点的有限阶回返均横截。
因为唯一候选要求 $\zeta+\zeta^{-1}=-4/3$，而根单位与其逆之和为代数整数，
不可能等于非整数有理数。因此特征零的二阶参数只是非挠特化，不贡献任何有限 $d$ 的 $i_d$。
这不是旧I03的好纤维全阶异常谱，不能据此宣布旧I03已解决。

## Corrections, consumers, and open risks

[ACCEPT] 的节点理想 $\epsilon^{i_n}(\xi,\eta)$ 可直接代入 (4)，现在节点标量不再未知。
这只是已接受理想的消费者，不重证共轭、群作用、嵌入部分或全局 Fitting 表达。
没有求好纤维 $D_n$、扩域 Manin 充分性、尖点全理想、无穷边界或非单位时间；$T=0$ 未纳入。
审查应针对 (11)–(17) 的实际新恒等式、原标点符号、无分歧逆函数与全部特征边界。
作者侧已逐项核过所有除法、量词及非零系数；fresh 数学核查和直接先例核查仍未完成。
本件不从一个短的准确节点分类推出独立22–30页长文价值，也不宣称存在剩余权限阻塞。

## Actual reading and verification record

本人 FULL 阅读 `AGENTS.md`、`docs/WORKFLOW.md`、proof-writer 技能；批次入口只读1–20行。
proof-writer 使本件将完整节点命题、准确首项、标准传播、未供给范围及作者状态分开。
以下 FULL 均为本人实际读取；首次合并输出截断后，原接口已分段补读，不继承代理实读身份。

| 本地输入 | 本人范围 | SHA-256（必要身份） |
|---|---|---|
| [ACCEPT] | FULL 1–176 | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |
| [FIX] | FULL 1–348 | `401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7` |
| [RETURN] | FULL 1–368 | `9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c` |
| [COLLISION] | FULL 1–107 | `b7271644adec9357cde8e33d1c0b437d94bf4e72944b3b74c338a0458b1e6977` |
| [SINGULAR] | PARTIAL 1–155、290–450 | 原节点关系、群参数及标点方向 |
| [INVENTORY] | PARTIAL 1–130 | 旧点阶与闭纤维周期边界 |
| [I03] | PARTIAL 130–170 | 旧I03准确原量词及其停止浅版本条件 |

外文 [TATE] 本人实读PDF pp.1–7 的公式、Theorem 1陈述与同态／普遍恒等式证明部分，
以及pp.21–23的更一般底环、局部参数与模观点；未读完其全部满射证明或全文。
本证明只需实读的同态及整数级数，(16) 的局部阶直接推导，不依赖满射部分。
[NASK] 本人实读印刷pp.1003–1005的设定、Lemma 8.2完整陈述和证明；仅作标准传播扣除。
另打开Conrad `kmpaper.pdf` 引言定位，未用于新增证明；Silverman镜像502与Tate Harvard镜像超时均未当来源实读。
公开搜索只用于定位上述标准一手源，没有完成广泛查新，不把搜索摘要当定理证明。

有界 SymPy 精确有理式计算核对 (10)–(17)、例外多项式余式及判别式导数；没有有限域新采样。
作者侧只读 helper `nodal_firstjet_helper` 另从原节点的微分与有理一阶群特征推得 (17) 第一式，
固定 $T$、原 $t_O$ 的符号与例外相同；其未核二阶结论，不作独立审查或数学接受票。
全部数学写入仅本文件；未扩冻结F5表、未启动统计、GPU、编译、项目、锁、外部写或联系旧审查者。
终态哈希在交付时报告；冻结原稿、失败、接受处置、README和批次入口均不修改。

[ACCEPT]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[RETURN]: PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md
[COLLISION]: PAPER31_QPI_NEW_INPUT_LOCAL_COLLISION_MAP_V1_20260912.md
[SINGULAR]: PAPER30_QPI_SINGULAR_CUBIC_GROUP_ENTRY_V1_20260908.md
[INVENTORY]: PAPER30_QPI_FULL_CYCLE_INVENTORY_ENTRY_V1_20260908.md
[I03]: PAPER30_QPI_POSTV2_IDEATION_V1_20260909.md
[TATE]: https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf
[NASK]: https://nyjm.albany.edu/j/2016/22-46v.pdf
