# Paper30 qPI P03：纯四次曲线的 Cartier—留数配对引理 V1

日期：2026-09-09。类型：独立有界纯曲线作者引理，待非作者核查。
本件只处理下面明确给定的 $f,R$，不证明 $R$ 来自原 qPI 的矩阵 gauge、首垂直 jet 或状态微分。
已冻结的 $p=3$ 诊断不修改；本件不是评分、候选合同或论文。

## Claim

设 $k$ 为特征不等于二的域，$t\in k^\times$，$h\in k$，并设
$$f(z)=(t+hz+z^2)^2-4z^3$$
可分。令 $C/k$ 为 $Y^2=f(z)$ 的光滑射影模型，且
$$R(z)=r_4z^4+r_3z^3+r_2z^2+r_1z,$$
其中
$$r_4=h^2-3h-t+2,$$
$$r_3=-2h^3+14h^2+6ht-24h-8t+12,$$
$$r_2=-h^4+3h^3-2h^2+5ht+3t^2-4t,$$
$$r_1=-h^3t+3h^2t+ht^2-2ht.$$
置
$$g(z)=R(z)/z\in k[z],\qquad \omega=\frac{dz}{Y},\qquad
\eta=\frac{g(z)\,dz}{Y^3}.$$

**CP.1（精确配对）。** $\omega$ 在 $C$ 上正则，$\eta$ 只在四个有限分歧点有至多二阶极点，且无留数。
采用下文明确固定的 de Rham 留数配对次序，有
$$\langle\omega,\eta\rangle
=\sum_{f(r)=0}\frac{4g(r)}{f'(r)^2}=1. \tag{1}$$
根的和在代数闭包中计算，结果属于 $k$。因 $f(0)=t^2\ne0$，这里的 $g(r)=R(r)/r$ 均有意义。

**CP.2（所有奇素数上的不同时消失）。** 若 $\operatorname{char}k=p>2$，定义
$$H=[z^{p-1}]f(z)^{(p-1)/2},\qquad
\Lambda=[z^p]R(z)f(z)^{(p-3)/2}.$$
则在 $f$ 可分的上述参数上，$H$ 与 $\Lambda$ 不能同时为零。
该断言包括 $p=3$，不隐含 $p\ge5$。

## Status

PROVABLE AS STATED（采用 (1) 所示配对次序；作者证明完成，待独立核查）。
证明给出 $\mathbb Z[h,t,z]$ 中无分母的多项式证书，因而不是从有限参数例子推断恒等式。

## Assumptions

1. 参数与 $R$ 精确采用 Claim 中的定义，不允许修改能级常数或系数规范。
2. $t\ne0$、$2\ne0$ 且 $f$ 可分。可分性保证 $f'(r)\ne0$，并保证该四次模型的光滑射影完备化是光滑曲线。
3. CP.2 证明可先扩到代数闭包：多项式系数是否为零和 (1) 的恒等式均忠实保留。
   因而使用 $p$ 次根时是在完美域中进行，并非默认为任意原域上的 Frobenius 可逆。
4. 不使用任何原 qPI 积分、完整吹起曲面、圆分扩张或已接受 C3 作为本件证明前提。

## Notation

$C$ 的函数域记为 $K$。$\operatorname{res}_P$ 表示在局部参数 $u$ 的 Laurent 展开中 $u^{-1}du$ 的系数。
配对约定如下：对 $\eta$ 的每个极点取具有至多一阶极点、只有负幂的局部极部原函数 $Q_P$，使 $\eta-dQ_P$ 正则，定义
$$\langle\omega,\eta\rangle=-\sum_P\operatorname{res}_P(Q_P\omega). \tag{2}$$
这是用 $\eta$ 的局部正则化表示 de Rham 类、再与正则 $\omega$ 作杯积的留数表示；此处明确固定该次序和负号。
交换配对的两个槽会得到相反数。
本件的极点阶至多二，故 $Q_P$ 只需一阶极部，不会出现需要除以 $p$ 的积分。
非零一阶主部的微分必有非零二阶主部，故这样的 $Q_P$ 模正则函数唯一；更换局部参数只改变正则项，不改变 (2)。
这里不允许任意额外添加更高阶的 $p$ 次负主部来另选 de Rham 类。
等价地，若 $F_P\in u k[[u]]$ 满足 $dF_P\equiv\omega\pmod{u\,du}$，则
$$\langle\omega,\eta\rangle=\sum_P\operatorname{res}_P(F_P\eta). \tag{3}$$
这里只需 $F_P$ 的一次项；一般情形下没有假设 $\omega$ 存在完整形式原函数。

## Proof Strategy

先逐点确定两个微分的极部，并把配对化成四根之和。
然后用一个整数系数恒等式，把该根和化为首一三次多项式的 Lagrange 插值首项。
最后明确算出两个 Cartier 像；若它们同时为零，就得到两个有理原函数。
逐点处理第一个原函数可能具有的 $p$ 次负主部，证明此时配对必须为零，与 (1) 矛盾。

## Dependency Map

1. CP.1 依赖 Step 1 的极部分析、Step 2 的整数多项式证书与可分根插值。
2. CP.2 依赖 Step 3 的函数域 $p$-基、Cartier 系数提取，以及 Step 4 的精确局部负主部／全局留数论证。
3. 特征三在 Step 3 的指数及次数界中已包括；Step 5 再给直接边界检查。
4. 本文只借用 Cartier 的命名及坐标无关规范；核为恰当微分、所需系数公式及配对消失均在正文证明。

## Proof

### Step 1. 极部、无穷远与配对的符号

先扩到代数闭包。每个简单根 $r$ 上只有一个点 $P_r$，而 $u=Y$ 是其局部参数。
由 $u^2=f(z)$ 和 $f'(r)\ne0$，形式隐函数展开给出
$$z=r+\frac{u^2}{f'(r)}+O(u^4),\qquad
\omega=\left(\frac{2}{f'(r)}+O(u^2)\right)du,$$
$$\eta=\left(\frac{2g(r)}{f'(r)}u^{-2}+O(1)\right)du. \tag{4}$$
展开中的 $z$ 只含偶次 $u$，因此 $\eta$ 没有 $u^{-1}du$ 项；这些论证仅需二为单位。
取
$$Q_r=-\frac{2g(r)}{f'(r)}u^{-1}.$$
则 $dQ_r$ 恰消去 (4) 的极部。代入 (2)，单点贡献为
$$-\operatorname{res}_{P_r}(Q_r\omega)=\frac{4g(r)}{f'(r)^2}. \tag{5}$$
若取 $F_r=(2/f'(r))u+O(u^2)$，也得到相同的 $\operatorname{res}(F_r\eta)$。
更一般地，$\operatorname{res}d(F_rQ_r)=0$，且 $(dF_r-\omega)Q_r$ 正则、$F_r(\eta-dQ_r)$ 正则，故 (2) 与 (3) 一致。

有限点上 $Y\ne0$ 时两个微分都正则。无穷远令 $s=1/z$、$W=Ys^2$，则
$$W^2=1+(2h-4)s+(h^2+2t)s^2+2hts^3+t^2s^4.$$
因二为单位，在 $s=0$ 有两个互异的点 $W=\pm1$，且
$$\omega=-\frac{ds}{W},\qquad
\eta=-\frac{s^4g(1/s)}{W^3}\,ds.$$
$\deg g\le3$，所以后一式至少含一个因子 $s$，两个无穷远点均无极点。
这证明所有局部贡献都已列入 (5)，也证明 $\eta$ 确实定义上述第二类／de Rham 配对。

### Step 2. 无分母整数证书与四根之和

定义首一三次多项式
$$B(z)=z^3+(h-2)z^2+(2h+t-2)z-2(h^2-3h-t+2),$$
以及
$$T(z)=4z^2+2(h-2)z.$$
关键证书是在 $\mathbb Z[h,t,z]$ 中的精确恒等式
$$4g(z)=f'(z)B(z)-T(z)f(z). \tag{6}$$
为使证书可以直接逐项核查，写
$$f=z^4+2(h-2)z^3+(h^2+2t)z^2+2htz+t^2,$$
$$f'=4z^3+6(h-2)z^2+2(h^2+2t)z+2ht.$$
把这两式与 $B,T$ 相乘，$z^6,z^5,z^4$ 的系数全部相消，剩余 $z^3,z^2,z,1$ 的系数分别为 $4r_4,4r_3,4r_2,4r_1$，这正是 (6)。
这没有使用 $f$ 的可分性，也没有用到任何参数分母。

在可分根 $r$ 上，(6) 给出
$$\frac{4g(r)}{f'(r)^2}=\frac{B(r)}{f'(r)}.$$
Lagrange 插值等式为
$$B(z)=\sum_{f(r)=0}B(r)\frac{f(z)}{(z-r)f'(r)}.$$
每个 $f(z)/(z-r)$ 都是首一三次式，故比较 $z^3$ 系数得到
$$\sum_{f(r)=0}\frac{B(r)}{f'(r)}=[z^3]B=1.$$
结合 Step 1 得到 CP.1。
由于 (6) 的系数是整数，此证明在每个奇特征中原样成立，只要求 $f'$ 在根处可逆。
等价地，在可分参数环上，它是有限 étale 代数 $k[z]/(f)$ 中
$$\operatorname{Tr}\!\left(4g(f')^{-2}\right)=1$$
的证书；这里不需要先在 $\mathbb Q(h,t)$ 求逆再尝试不受控地降模。

### Step 3. 函数域 $p$-基、恰当微分核与两个 Cartier 系数

以下 $\operatorname{char}k=p>2$，且已经扩到代数闭包，故 $k$ 完美。
记 $n=(p-1)/2$。从 $Y^p=Yf(z)^n$ 得到
$$K=K^p(z),\qquad Y=Y^p/f(z)^n.$$
$z\notin K^p$：确实，在 $K$ 上存在 $k$-导子
$$\partial(z)=1,\qquad \partial(Y)=\frac{f'(z)}{2Y},$$
它保持关系 $Y^2=f(z)$，而所有 $p$ 次幂的导数都为零。
因为 $z^p\in K^p$，$z$ 在 $K^p$ 上的次数只能是一或 $p$；前者已排除。
于是 $1,z,\ldots,z^{p-1}$ 是 $K/K^p$ 的基。

因此任意有理微分唯一写成
$$\theta=\left(\sum_{j=0}^{p-1}a_j^p z^j\right)dz,$$
并可用该分离变量表示 Cartier 算子为
$$\mathcal C(\theta)=a_{p-1}dz. \tag{7}$$
这采用 rational Cartier 的通常规范，坐标无关性与半线性规范可参见
[Achter–Howe，§§2.1–2.2](https://arxiv.org/html/1710.10726v5#S2.SS2)；下面需要的核性质不依赖省略证明的引用。

若 $a_{p-1}=0$，显式有理函数
$$A=\sum_{j=0}^{p-2}\frac{a_j^p z^{j+1}}{j+1}$$
满足 $dA=\theta$，因为 $1,\ldots,p-1$ 均可逆。
反过来，把任意 $A\in K$ 按同一 $p$-基展开后求导，得到的 $dz$ 系数只有 $z^0,\ldots,z^{p-2}$，故 $\mathcal C(dA)=0$。
所以此处完整证明了
$$\ker\mathcal C=dK. \tag{8}$$

现在
$$\omega=\frac{f(z)^{(p-1)/2}}{Y^p}dz,\qquad
\eta=\frac{g(z)f(z)^{(p-3)/2}}{Y^p}dz. \tag{9}$$
两个分子多项式的次数分别为 $2p-2$ 和至多 $2p-3$。
在区间 $0\le j\le2p-2$ 中，与 $p-1$ 模 $p$ 同余的唯一指数是 $p-1$；第二个分子也满足同一结论。
由 (7)、(9) 及 $p^{-1}$-半线性，得到
$$\mathcal C(\omega)=H^{1/p}\omega,\qquad
\mathcal C(\eta)=\Lambda^{1/p}\omega, \tag{10}$$
其中
$$\Lambda=[z^{p-1}]g(z)f(z)^{(p-3)/2}
=[z^p]R(z)f(z)^{(p-3)/2}.$$
这正是 Claim 中的两个系数，没有出现移位或转置约定。

### Step 4. 两个 Cartier 像同时为零必使配对为零

反设 $H=\Lambda=0$。由 (8)、(10)，存在 $A,D\in K$ 满足
$$dA=\omega,\qquad dD=\eta. \tag{11}$$
这里不宣称“有理恰当微分就是零 de Rham 类”：在正特征中，原函数可有导数为零的负主部，必须处理这项差别。

固定 $C$ 的任一点 $P$ 和局部参数 $u$，把 $A$ 展开为 Laurent 级数
$$A=\sum_{j\ge-N}a_j u^j.$$
因 $dA=\omega$ 正则，每个 $j<0$ 都满足 $j a_j=0$。
所以非零负幂项的指数只能是 $p$ 的倍数。令
$$N_P=\sum_{j<0}a_j u^j,$$
则 $N_P$ 是有限负主部，且 $dN_P=0$；在完美域上，它也确为某个 Laurent 多项式的 $p$ 次幂。
取
$$F_P=A-N_P-a_0\in u k[[u]],\qquad dF_P=\omega.$$
此时完整形式原函数的存在是由 (11) 导出的，而非在 Cartier 未消失时预先假设。

由 $d(N_P+a_0)=0$ 及 $\eta=dD$，在 $k((u))$ 中有
$$ (A-F_P)\eta=(N_P+a_0)dD=d\bigl((N_P+a_0)D\bigr). \tag{12}$$
任意 Laurent 级数的导数都没有 $u^{-1}du$ 项：该项只能来自 $u^0$ 的导数，其系数为零。
因此 (12) 证明
$$\operatorname{res}_P(A\eta)=\operatorname{res}_P(F_P\eta). \tag{13}$$
这同时处理了所有 $p$ 次负主部、常数项，以及 $D$ 可能另有的 $p$ 次极部；没有忽略极点支撑。
在 $\eta$ 正则的点，右边为零；在四个分歧点，右边正是 (3) 的局部贡献。
故
$$\langle\omega,\eta\rangle=\sum_{P\in C}\operatorname{res}_P(A\eta). \tag{14}$$

为完整说明所用的全局留数结论，可在本二次覆盖上直接降到射影直线。
对任意有理微分 $\theta\in\Omega_K^1$，写 $\theta=(a(z)+b(z)Y)dz$。
在非分歧底点，两个上方点的留数和等于 $2a(z)dz$ 的底点留数。
在分歧点，对合 $Y\mapsto-Y$ 保留留数，故反不变部分的留数等于其相反数，因二可逆而为零；
不变部分 $a(z)dz$ 的留数是底点留数的二倍，因为局部覆盖分歧指数为二。
无穷远有两个非分歧点，已在 Step 1 确认。
因而
$$\sum_{P\in C}\operatorname{res}_P\theta
=\sum_{Q\in\mathbb P^1}\operatorname{res}_Q\bigl(2a(z)dz\bigr)=0.$$
最后一个等号由有理函数的部分分式展开得到：无穷远留数是全部有限留数之和的相反数。
将其应用于 $\theta=A\eta$，(14) 为零，与 Step 2 的配对值一矛盾。
故 $H,\Lambda$ 不同时为零，CP.2 得证。

### Step 5. 特征三的显式边界核查

$p=3$ 时 $(p-3)/2=0$，故 Step 3 没有负指数或除以三。
直接约化得到
$$H=h^2-t,\qquad \Lambda=h^3-h^2+t.$$
若 $H=0$，则 $t=h^2$，于是 $\Lambda=h^3$。
因 $t\ne0$，必有 $h\ne0$，所以 $\Lambda\ne0$。
这给该边界的额外直接检查，与全奇素数证明一致。CP.1–CP.2 证毕。

## Corrections or Missing Assumptions

- 原配对值一与不同时消失结论均保留；没有增加 $p\ge5$ 或特定参数的假设。
- 为排除符号歧义，(2) 显式固定配对次序。若另一个文件采用相反杯积次序，对应值是负一；不同时消失结论不受影响。
- 不把 $\mathcal C(\eta)=0$ 单独解释为 $[\eta]=0$。Step 4 使用两个微分同时恰当，并逐点消去 $p$ 次负主部后才得配对为零。
- $t=0$、特征二及 $f$ 不可分不在本件范围内；特别是分歧点公式不允许把 $f'(r)=0$ 的奇异参数直接代入。

## Actual Verification and Open Risks

- 主作者完整使用 proof-writer；精确符号计算在 $\mathbb Z[h,t,z]$ 中核对了 (6)，并直接核对 Step 5 的模三系数。
- 符号计算只作有限恒等式的复核；Step 2 的证书与插值、Step 3–4 的函数域和留数论证构成证明本身。
- 独立查阅了上述 primary Cartier 规范；没有把文献中的一般半线性或对偶关系误当作本件特殊配对恒等式。
- 唯一新文件是本作者引理；未新建辅助脚本，未更改 $p=3$ 作者件或其他冻结文件，未调用 GPU。
- 仍待非作者对 (2)–(3) 的配对规范、(6) 的全部系数、(10) 的指数以及 (12)–(14) 的负主部处理作定向核查。
- 不证明 $R$ 的 actual qPI 来源，也不证明垂直 jet 与该纯曲线配对的接口；这些必须由独立对象识别证明承担。
- 未据此给出新意、评分、立项或论文价值判断。
