# Paper 30：三的幂第三 forcing 的 Newton 与点值推论补充独审

日期：2026-09-07。审查者：late_nonnenmacher_source。按本轮完整读取的 proof-writer。
本件只审新增推论，不重开原 14 项，不重跑任何有限递推，不改冻结文件。

## Claim

基于未变的 [V2 五系数](PAPER30_TWIST_THIRD_FORCING_THREE_POWER_BOUNDARY_PROBE_V2_20260907.md)，
SHA256 `643417e53df99921f003d42763e021fc8abbe2c0ca6ae83eead8b1675fab42fd`，
审查两种 Newton 多边形、局部不可约性、平方自由性、根域分歧及参数点值推论。
原 [14 项独审](PAPER30_TWIST_THIRD_FORCING_THREE_POWER_BOUNDARY_INDEPENDENT_CHECK_20260907.md)
SHA256 `5fa612351b1ed2e7d685aa498edcdefb984a5c17c87a529e1f056fbdc4cde354` 保持不变。

## Status

PROVABLE AS STATED。下述新增推论全部成立；无新阻断，无旧证书复验。

## Assumptions and Notation

沿用 $K^+=\mathbb Q_3(h)$、$\mathcal O^+=\mathbb Z_3[h]$、
$v_h(h)=1$、$v_h(3)=M=3^{a-1}$、$L=-h\lambda$，
$G=9\mathcal B_3=\sum_{j=0}^4g_jL^j$。根与参数均在局部代数闭包中考虑。
$E/K^+$ 为有限局部扩域时，$e,f$ 分别指相对分歧指数和剩余次数，
仍以 $v_h(h)=1$ 规范；$\bar L$ 是模 $\mathfrak m_E$ 的像。
$a\ge3$ 时 $S=h^{-7}G$。$\mathcal B_2$ 指同一原分支的第六阶 forcing，
不是另一个构造，也不是指数插入 $Q$。

## Proof Strategy and Dependency Map

五系数高度确定下凸包；整首层给简单 Hensel 根及整商；
负根赋值和边剩余分别限制根域的 $e,f$，再以次数界证明不可约。
使用有限局部扩域的基本不等式 $ef\le[E:K^+]$；
它可由剩余域基的提升与素元的前 $e$ 次幂线性独立得到，无须预设分裂域。

## Proof

### Step 1. $a\ge3$ 的下凸包及根赋值

置 $\delta=(M-1)/3$。已接受高度为 $(7,7,M+6,M+5,M+6)$，
故下凸包准确为
$$
(0,7)\longrightarrow(1,7)\longrightarrow(4,M+6).
$$
第二条边在横坐标二、三处与实际点的高度差分别为
$2(M-1)/3$、$(M-4)/3$，均严格为正。
根赋值是边斜率的相反数：一根赋值零，三根赋值 $-\delta$，先按重数计。
也可直接检查：将根赋值记为 $t$，各项高度为 $v_h(g_j)+jt$；
非顶点项严格在边上方，故最低项能相遇仅在 $t=0,-\delta$。

### Step 2. 唯一整根与全扩域整参数的准确点值

$\bar S=1+L$ 在 $\bar L=2$ 有简单根，$\overline{S'}=1$。
$\mathcal O^+$ 是完备离散赋值环，简单根 Hensel 引理给
$\alpha\in\mathcal O^+$、$\bar\alpha=2$、$S(\alpha)=0$。
以首一多项式 $L-\alpha$ 作整系数除法得
$$
S(L)=(L-\alpha)U(L),\qquad U\in\mathcal O^+[L],\qquad \bar U=1.
$$
最后一式由 $(L-2)\bar U=L+1=L-2$ 在 $\mathbb F_3[L]$ 中消去得出。
因此对任意有限扩域及任意整参数 $L$，$U(L)$ 始终为单位。
$\alpha$ 是局部代数闭包中唯一的整根，也是简单根，赋值为零。
使用已接受的 $V_9=\mathcal B_3/(2d_9)$、$v_h(d_9)=8$ 得
$$
\boxed{\begin{aligned}
v_h(\mathcal B_3(L))&=7-2M+v_h(L-\alpha),\\
v_h(V_9(L))&=-2M-1+v_h(L-\alpha).
\end{aligned}}
$$
$\alpha$ 处两式取 $+\infty$。公式允许分数赋值，不假设扩域未分歧；
它严格限定整参数，不能把 $U(L)$ 的单位性外推至非整参数。

### Step 3. 其余三根与平方自由性

$G=(L-\alpha)H$，其中 $H\in K^+[L]$ 次数三。
任一 $H$ 根 $\beta$ 满足 $v_h(\beta)=-(M-1)/3$。
因 $M\equiv0\pmod3$，该分数既约分母为三；
所以 $3\mid e(K^+(\beta)/K^+)$，而根的次数至多为三。
基本不等式迫使根次数恰为三、$e=3,f=1$，故 $H$ 不可约。
特征零中的不可约多项式可分，且 $\alpha$ 与三次根赋值不同；
因此整个四次 $G$ 平方自由。这里的线性乘三次分解是在局部域 $K^+$ 上，
没有声称 $\alpha$ 属于未完备的原数域 $\mathbb Q(h)$。

### Step 4. $a=2$ 的边剩余、不可约性及每个根域

已接受高度 $(8,9,11,10,10)$ 给唯一边 $(0,8)\to(4,10)$；
中间三点严格在该边上方，故四根均满足 $v_h(\beta)=-1/2$。
直接从冻结式 (21) 读取
$$
g_4=-\frac{305181}{4}h^2+\frac{1284309}{8}h-\frac{467451}{8}.
$$
唯一最低项为 $(27\cdot47567/8)h$；用已接受的 $\overline{3/h^3}=1$ 得
$$
\overline{g_4/h^{10}}
=\overline{\frac{47567}{8}\left(\frac3{h^3}\right)^3}=1.
$$
又 $\overline{g_0/h^8}=1$。令 $E=K^+(\beta)$、$Y=h\beta^2$，则 $Y$ 为单位。
在 $G(\beta)/h^8=0$ 中，中间三项赋值分别为 $1/2,2,1/2$，故
$$
1+\bar Y^2=0.
$$
$1+Y^2$ 在 $\mathbb F_3$ 上不可约，于是 $2\mid f(E/K^+)$；
$v_h(\beta)=-1/2$ 又迫使 $2\mid e(E/K^+)$。
由于 $ef\le[E:K^+]\le4$，必有
$$
[E:K^+]=4,\qquad e(E/K^+)=f(E/K^+)=2.
$$
故 $G$ 及其非零常数倍 $\mathcal B_3$ 在 $K^+[L]$ 上不可约，
并由特征零而平方自由。上述 $e=f=2$ 针对每个单根生成域，
不是对分裂域或 Galois 闭包的断言。

### Step 5. $a=2$ 时与第二内部 forcing 互素

已接受的 [第二内部 forcing](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md)
给 $\overline{h^{-2}3\mathcal B_2}=2$，故 $\mathcal B_2\ne0$，此处不重证该输入。
原递推的参数权重归纳给 $\deg_LV_n,\deg_LE_n,\deg_LF_n\le\lfloor n/2\rfloor$：
每个指数系数中的分拆保持总下标，乘一个 $L$ 同时降低强迫下标二。
于是 $\mathcal B_2=-E_5-2LF_4$ 的次数至多三。
四次不可约的 $\mathcal B_3$ 不可能整除该非零多项式，因此
$$
\gcd_{K^+[L]}(\mathcal B_2,\mathcal B_3)=1\qquad(a=2).
$$
所有新增结论得证。$\square$

## Corrections or Missing Assumptions

无。分歧扩域中的分数赋值已保留；仅根域而非分裂域的 $e,f$ 已明确。
这里补充的是从冻结系数推出的新结论，不把原独审未审的推论追记为旧 14 项内容。

## Open Risks and Delivery Boundary

本票已确定上述 Newton、局部因子、平方自由和整参数距离公式；
不将它们继续列为未定。尚未给 $\alpha$ 的显式闭式或分裂域分类，
也不追加完整 $C/Q$、复嵌入下的全实性或一般 $p\ge5$ 的第三端点结论。
仅新建本补充文件；未重跑递推、未扫描素数或根、未修改冻结 V2 或原独审。
