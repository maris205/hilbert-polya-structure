# Paper30 qPI：全素数一层垂直理想的合取非作者检查 V1

日期：2026-09-09。检查者：`/root/p30_qpi_integral_cohomology_prior_art_v1`。
类型：三份冻结作者证明的完整数学责任及实际接口检查，不是新意评分或正式候选评审。
`route_applicability: NOT_APPLICABLE`。

## Claim

本次唯一写入本报告。完整读取并绑定以下三件作者输入，共 765 行、41,981 字节：

| 代号及作者件 | 全文行数／字节 | SHA-256 |
|---|---|---|
| V：[全素数一层主证明](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_HEIGHT1_PROOF_V1_20260909.md) | 255／14,768 | `ffdcfc37860477e990f836721898fc654537bb3254b7335876581990c2da4f74` |
| M：[首 jet 矩阵引理](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md) | 283／14,146 | `f3618fa1345804ce5d93acae4e6fdb2b3ee7761a87ae2de8bc453d24944971bd` |
| CP：[Cartier—留数配对引理](PAPER30_QPI_VERTICAL_ALPHA_CARTIER_PAIRING_LEMMA_V1_20260909.md) | 227／13,067 | `65dfd605af26e84b57289ef57380392c923b2b1c700b5a3c69731567f8a54e4c` |

另全文读取并实际执行 [有限符号脚本](qpi_vertical_alpha_endpoint_algebra_v1_20260909.py)，
其 SHA-256 为 `f939da5277ce5e6e09f6306d6530e190b2bcf193e3ff82ea4fc519d2326b0d1b`。
脚本不承担无限量词、Cartier 论证或全模型延拓。

V 的精确对象是任意素数 $p$、$q=\zeta_p$、$\pi=q-1$，
圆分 DVR $\mathcal O$ 及其允许的有限无分歧扩张／完成，任意 $t\in\mathcal O^\times$。
原 $m=a=1$ 小阶闭纤维函数与整除微分为
$$J=y+x/y-x-T/x,\quad T=\bar t,\qquad
\alpha_p=p^{-1}d_{\rm state}[Z^p]\operatorname{tr}
\bigl(A(q^{p-1}Z)\cdots A(Z)\bigr).$$
固定剩余 Hasse 多项式
$$H_p(T,h)=
\begin{cases}
[Z^{p-1}]\bigl((T+hZ+Z^2)^2-4Z^3\bigr)^{(p-1)/2},&p>2,\\
h,&p=2.
\end{cases}$$
对任一光滑有限原能级 $X_h=(J=h)$ 和所有 $P\in X_h$，V 声称
$$\mathfrak c(\alpha_p)_P=(\pi,\widetilde H_p(T,J)),\qquad
\mathfrak c(dI_p)_P=(\pi^p,\pi^{p-1}\widetilde H_p(T,J)),$$
其中波浪号指在实际局部环中的任意剩余 Hasse 函数提升，不是新的函数规范。
若 $h$ 是 Hasse 根且重数为 $e_h$，则完成理想是 $(\pi,z^{e_h})$，$\bar z=J-h$。
沿无分歧 DVR 状态提升，整除微分公共阶在超奇异／普通光滑层分别为一／零，
未整除微分分别为 $p$／$p-1$。

M 的完整责任另包括：所有奇素数及 $N=p^a$ 的普适矩阵恒等式，
其 $p^{-a}dI_{p^a}$ 首阶归一化接口与时间变化说明。
核准这些矩阵量词不等于核准 $a>1$ 的几何理想；V 只消费 M 的 $N=p$ 情形。
CP 的完整责任包括所有 $\operatorname{char}k\ne2$ 的固定配对值一，
以及所有奇特征中固定 $H,\Lambda$ 不同时消失。

## Status

**PROVABLE AS STATED；三件责任及接口合取 PASS。**

| 数学责任 | 结论 | 未被偷换的边界 |
|---|---|---|
| M 全文矩阵与实际归一化 | PASS | 包括其明确写出的所有 $p^a$；不推出高层几何非消失 |
| CP.1 精确配对及 CP.2 全奇素数非同时零 | PASS | 保留 $t\ne0$、四次式可分及特征不等于二 |
| V 实际 gauge、首系数与纯配对接口 | PASS | 原矩阵、原有序乘积、原能级常数未改变 |
| V 完整光滑纤维、特征二、全部提升与重根量词 | PASS | 只限 $a=m=1$；不包括奇异能级或有分歧状态扩张 |

未发现需要修改作者公式、缩小原范围或补入新科学假设的硬缺口。
本报告补清证明中的规范和消费关系，不改动三份作者源。

独立性披露：检查者不是上述三件证明的作者，但参与过本方向先例工作及此前 p3 非作者检查，
已经方向知情；不称 fresh、盲审、设计隔离审稿或人类认证。
此次结论来自新一轮对实际 765 行的全读及下列证明复核，不由旧 p3 PASS 代签。
同一个检查者对三件分别承担责任后给合取，不计作三张独立新意票。

## Assumptions and Input Boundary

1. 原矩阵、乘积次序、八个中心及四末端图，消费已接受
   [整数 brief §2](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md)。
   除状态变量外，原 $A$ 的参数系数依赖只有实际时间 $t$；$q$ 的谱作用是 $Z\mapsto q^jZ$。
2. 原 $\alpha_p$ 在完整 $\mathcal U_t$ 上正则且
   $\bar\alpha_p=H_p(T,J)dJ$，消费旧 D/G 接口。
   本轮定向核读 [G3 与 Step 6](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)，
   不重开旧全参数整除及接受链。
3. 本轮定向核读 [brief V2 的 T1–T3 接口](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md)：
   有限小阶纤维完整包含在 $U_0$ 中，射影且几何整；所选光滑层亏格一且 $dJ$ 非零。
   这不是仅指环面上的仿射曲线；其射影性是后文常数论证的必要前提。
4. 原 $\Omega=dx\wedge dy/(xy)$ 的全开放曲面正则非退化性沿用已接受原几何，
   并对原四末端图作下文的独立符号复算。
5. 奇特征下谱四次式可分的实际接口亦核准：若
   $$\delta(h,T)=h^4-h^3-8Th^2+36Th+16T^2-27T,$$
   则有限整数多项式计算给
   $$\operatorname{disc}_Z\bigl((T+hZ+Z^2)^2-4Z^3\bigr)=256T^3\delta(h,T).$$
   原光滑层满足 $\delta\ne0$，且奇特征中 $256T^3$ 为单位，故 CP 的可分条件真实适用。
   这里没有重新证明旧实际 Jacobian 同构；Hasse 与普通／超奇异的几何解释继续消费已接受 C3。

## Notation

用 $Z$ 表示谱变量，$z$ 表示法向函数的局部提升，$j$ 表示 $J$ 的局部提升。
状态微分固定 $t,q,Z$；尤其 $t$ 即使具有非平凡 $\pi$ 展开，仍是状态方向的常数。
$\mathfrak c$ 是原秩二相对微分模的全部系数理想，完成时使用该有限模的完成／连续微分。
CP 的小写 $t$ 在与 V 接口时准确替换为剩余时间 $T$，其能级 $h$ 不作平移。

## Proof Strategy and Dependency Map

1. 普适带权矩阵恒等式及整数循环插入，给实际已整除微分的首谱缩放项。
2. 纯四次曲线的整数证书与局部极部给配对值一；$p$-基及全局留数排除两个 Cartier 像同时零。
3. 原第一末端正则 gauge 的直接求导和矩阵乘法，把实际首切向常数严格识别为 CP 的 $\Lambda$。
4. 内在切向类全局粘接且完整纤维射影，将单点非零变成所有点非零。
5. 特征二单独由原两因子迹处理；最后局部消元给原理想及其所有提升／重根后果。

## Proof

### Step 1. M 的全 $N$ 矩阵恒等式：PASS

对奇素数 $p$、$N=p^a$，先在通用多项式整环 $\mathbb F_p[X,Y]$ 中使用
$$X^N-Y^N=(X-Y)^N=(X-Y)\sum_{j=0}^{N-1}X^{N-1-j}Y^j.$$
只在该整环中约去 $X-Y$，再对 $Y$ 求导，得
$$\sum_{j=1}^{N-1}jX^{N-1-j}Y^{j-1}=(X-Y)^{N-2}.$$
此后才特化到含零因子的任意交换 $K$；不在实际 $K$ 中约分。
左右乘算子 $L_A(X)=AX,R_A(X)=XA$ 交换；记 $\operatorname{ad}_A=L_A-R_A$、$[A,B]=AB-BA$，
因此左边作用于 $B$ 等于 $\operatorname{ad}_A^{N-2}(B)$。

二阶 Cayley–Hamilton 在整数系数下给
$$\operatorname{ad}_A^3(B)=(S^2-4D)[A,B],\qquad S=\operatorname{tr}A,\ D=\det A.$$
以下记 $\Delta=S^2-4D$。
本轮另对通用两个 $2\times2$ 矩阵逐条目展开核准这条整数恒等式。
由于 $N-2=2((N-3)/2)+1$，可递推得到 M 的完整式
$$\sum_{j=1}^{N-1}jA^{N-1-j}BA^{j-1}
=(S^2-4D)^{(N-3)/2}[A,B].$$
没有反演 $D$、判别式或任何特征根；标量矩阵、奇异矩阵及判别式为零／零因子都包括在内。
$N=3$ 时指数为零，右边直接为 $[A,B]$，与 $AB+2BA$ 一致。
左乘一个中心模值矩阵后取迹只用系数的交换作用，不产生两个一形式相乘的符号问题。

在降序的 $N-1$ 因子乘积中，第 $j$ 个谱缩放项左边有 $N-1-j$ 个 $A$，右边有 $j-1$ 个。
所以 $q=1+\epsilon,\epsilon^2=0$ 的首项确实是上述带权和，交换子符号为正。
这逐项证明 M 的 (1)–(4)；改变降序或改变 $\epsilon$ 定义都会改变相应符号，不能混用。

### Step 2. M 的零阶参照、实际先除与时间量词：PASS

由整数递推 $U_{-1}=0,U_0=1,U_n=SU_{n-1}-DU_{n-2}$，得到
$$\operatorname{tr}(dA\,A^{N-1})=U_{N-1}dS-U_{N-2}dD.$$
将 $S=u+v,D=uv$ 代入，通用对称多项式嵌入和前步 Frobenius 恒等式给
$$U_{N-1}(S,D)=(S^2-4D)^{(N-1)/2}\quad\text{in }\mathbb F_p[S,D].$$
这不是只在实际矩阵可对角化的稠密情形成立。
原矩阵的 $S=t+J_tZ+Z^2,D=Z^3$ 给 $dS=Z\,dJ_t,dD=0$，故零阶参照式准确为
$$[Z^{N-1}]\Delta^{(N-1)/2}dJ_t\pmod p.$$

实际圆分环中，$\Phi_{p^a}(1+X)$ 首一，常数为 $p$，模 $p$ 为 $X^{\varphi(p^a)}$，
因此 Eisenstein 给 $p=\text{unit}\cdot\pi^{\varphi(p^a)}$。
奇 $p$ 时 $\varphi(p^a)\ge2$，所以 $\mathcal O/(\pi^2)$ 确为特征 $p$ 的环。
但归一化必须先完成：在特征零对原有序乘积逐位置求状态微分，
循环移到最左后换谱变量 $w=q^kZ$；其余因子仍按原降序排列。
由于 $q^{kN}=1$，各位置的 $Z^N$ 系数相同，故
$$dI_N=N[Z^N]\operatorname{tr}\bigl(dA(Z)A(q^{N-1}Z)\cdots A(qZ)\bigr).$$
右边先识别 $N^{-1}dI_N$ 为整一形式，之后才约化。
M 的实际式 (12) 因而核准，且其 $a>1$ 归一化确为 $p^{-a}$，不是 $p^{-1}$。

零阶迹表达式与显示的判别式表达式之差在整数多项式意义下被 $p$ 整除，
所以在实际一阶厚化中差属于 $(\pi^2)$；没有借用一个未给出的剩余域到混合特征环的系数嵌入。
矩阵恒等式允许任意交换特征 $p$ 系数环，也允许实际 $t$ 在该商环中含幂零部分。
M 的 $F_N(A)$ 始终使用实际 $t$；若另选 $t=t_0+\epsilon t_1$ 作参照，
则其 (13) 的附加项 $t_1\partial_tF_N$ 必须同时微分 $J_t$ 和 $dJ_t$。
该 Taylor 公式正确，不能把纯谱项 $\beta_N$ 冒称全部参数一起变化时的完整首系数。

### Step 3. CP.1 的整数证书、全部极点及配对规范：PASS

在这一节令 $t$ 表示 CP 的独立参数。设
$$f=(t+hZ+Z^2)^2-4Z^3,\qquad g=R/Z,$$
其中 $R$ 是 CP 原 Claim 固定的多项式，其全部四系数在本报告 Step 8 再次逐项列出。
令 $C$ 为 $Y^2=f$ 的光滑射影模型，$\omega=dZ/Y$、$\eta=g\,dZ/Y^3$；设
$$B=Z^3+(h-2)Z^2+(2h+t-2)Z-2(h^2-3h-t+2),$$
$$L=4Z^2+2(h-2)Z.$$
独立乘开全部整数系数，核得
$$f'B-Lf=4g\quad\text{in }\mathbb Z[h,t,Z].$$
左边的六、五、四次项全部相消，三、二、一次及常数项恰为 $4r_4,4r_3,4r_2,4r_1$。
证书不是在 $\mathbb Q(h,t)$ 中求逆后再不受控约化，因此包括全部奇特征及零掉的个别系数。

当 $f$ 可分且二可逆，每个根 $r$ 上取局部参数 $u=Y$，有
$$Z=r+u^2/f'(r)+O(u^4),\qquad
\omega=(2/f'(r)+O(u^2))du,$$
$$\eta=(2g(r)/f'(r)\,u^{-2}+O(1))du.$$
$Z$ 的级数只含 $u$ 的偶次，所以不存在未记录的一阶留数项。
取一阶负主部 $Q_r=-2g(r)/(f'(r)u)$，即可使 $\eta-dQ_r$ 正则。
在有限非分歧点无极点；$g$ 是真正的多项式，故 $Z=0$ 不产生人为分母极点。
无穷远取 $s=1/Z,W=Ys^2$，两个点为 $W=\pm1$，并有
$$\omega=-ds/W,\qquad \eta=-s^4g(1/s)ds/W^3.$$
$\deg g\le3$，所以两个无穷远点的 $\eta$ 都正则。

接受 CP 明确固定的次序
$$\langle\omega,\eta\rangle=-\sum_r\operatorname{res}_{P_r}(Q_r\omega).$$
逐点贡献为 $4g(r)/f'(r)^2$，故符号为正。
在“极部原函数至多一阶”的约束内，两个可选 $Q_r$ 的差若有一阶极点，其导数必有二阶极点，
与正则性矛盾；故其差正则。此规范不允许随意附加更高阶、导数为零的 $p$ 次负主部。
只需一次项的 $F_r$ 满足 $dF_r\equiv\omega\pmod{u\,du}$，同样给
$\operatorname{res}(F_r\eta)$；这一等价式没有预设一般正则微分在正特征中可完全积分。

在根上整数证书化成 $4g(r)/f'(r)^2=B(r)/f'(r)$。
$f$ 首一四次、$B$ 首一三次，Lagrange 插值比较三次首项给
$$\sum_r\frac{B(r)}{f'(r)}=1.$$
因此 CP.1 完整成立，包括其约定的配对值一。相反配对次序改变整体符号，不影响 CP.2。

### Step 4. CP.2 的 $p$-基、Cartier 系数与精确核：PASS

可先扩到代数闭包；原域上的两个系数是否为零由此忠实保留。
于是底域完美，$K=k(Z,Y)$ 满足
$$Y^p=Yf^{(p-1)/2},\qquad K=K^p(Z).$$
导子 $\partial Z=1,\partial Y=f'/(2Y)$ 保持方程，故 $Z\notin K^p$。
因 $Z^p\in K^p$，最小纯不可分次数是 $p$；于是 $1,Z,\ldots,Z^{p-1}$ 是 $K/K^p$ 的基。
同一关系的微分给 $dY=f'dZ/(2Y)$，且该导子证明 $dZ\ne0$，所以所有有理微分均唯一写成
$$\theta=\left(\sum_{j=0}^{p-1}a_j^p Z^j\right)dZ.$$
在此基下 $\mathcal C(\theta)=a_{p-1}dZ$。
本轮核读 [Achter–Howe v5 §2.2](https://arxiv.org/html/1710.10726v5#S2.SS2)
的有理 Cartier 延拓与逆 Frobenius 半线性规范；它与此处的 $p$ 次根方向一致。

若 $a_{p-1}=0$，逐项构造
$$A=\sum_{j=0}^{p-2}a_j^p Z^{j+1}/(j+1)$$
给 $dA=\theta$；所有分母均可逆。
反向对任意按此 $p$-基展开的 $A$ 求导，不出现 $Z^{p-1}dZ$ 分量。
因此 CP 不是黑箱引用，而是确实证明了所用的 $\ker\mathcal C=dK$。

由
$$\omega=f^{(p-1)/2}dZ/Y^p,\qquad
\eta=g f^{(p-3)/2}dZ/Y^p,$$
两个分子次数分别为 $2p-2$ 和至多 $2p-3$。
这一范围中与 $p-1$ 模 $p$ 同余的唯一指数是 $p-1$，因而
$$\mathcal C(\omega)=H^{1/p}\omega,\qquad
\mathcal C(\eta)=\Lambda^{1/p}\omega,$$
$$\Lambda=[Z^{p-1}]g f^{(p-3)/2}=[Z^p]R f^{(p-3)/2}.$$
这核准了指数、$R/Z$ 的系数移位和半线性，没有将 Cartier 标量误写成 $H$ 或 $\Lambda$ 本身。
$p=3$ 时指数零合法；直接式 $H=h^2-t,\Lambda=h^3-h^2+t$ 也吻合。

### Step 5. CP 同时恰当时的负主部及全局留数：PASS

这是纯配对证明的关键义务，不能用“有理恰当所以 de Rham 类为零”略去。
反设 $H=\Lambda=0$，前步给出有理函数 $A,D\in K$，满足 $dA=\omega,dD=\eta$。
在任一点的 Laurent 展开 $A=\sum a_j u^j$ 中，$dA$ 正则迫使每个负指数的非零项满足 $p\mid j$。
所以有限负主部 $N_P=\sum_{j<0}a_j u^j$ 有 $dN_P=0$。
令 $F_P=A-N_P-a_0\in u k[[u]]$，则 $dF_P=\omega$。
只有在当前同时消失的假设下才得到这个完整形式原函数。

局部直接计算
$$ (A-F_P)\eta=(N_P+a_0)dD=d\bigl((N_P+a_0)D\bigr).$$
Laurent 级数导数的留数总为零，故
$$\operatorname{res}_P(A\eta)=\operatorname{res}_P(F_P\eta).$$
该等式不要求 $D$ 的极点支撑只在四个分歧点，已同时处理额外的 $p$ 次极部及常数。
在 $\eta$ 正则处右端为零；在分歧点右端就是 CP.1 的局部配对贡献。
于是配对等于有理微分 $A\eta$ 在完整 $C$ 上的全部留数和。

CP 给出的全局留数证明在这个二次覆盖上适用：将任意有理微分写为
$(a(Z)+b(Z)Y)dZ$。
非分歧点的两个留数相加就是底部 $2a(Z)dZ$ 的留数；
在分歧点，反不变部分的留数由 $Y\mapsto-Y$ 等于自身相反数，因二可逆而为零，
不变部分的拉回留数则乘分歧指数二。无穷远确有两个非分歧点，已在前步列出。
所以全曲线留数和等于 $\mathbb P^1$ 上有理微分 $2a(Z)dZ$ 的留数和；
部分分式展开及无穷远项给出该和为零。
这与配对值一矛盾，证明 CP.2 的所有奇素数及全部可分参数量词。
没有采用 ordinary 前提，也没有把两个恰当微分中的任意一个单独当作零 de Rham 类。

### Step 6. V 的内在切向类与完整纤维常数：PASS

在光滑 Hasse 零层 $X_h$ 附近，选择 $j$ 提升 $J$，以及 $H_p(T,\cdot)$ 的系数提升 $\widehat H$。
原正则微分模平坦且乘 $\pi$ 单射，因此
$$\gamma_j=(\alpha_p-\widehat H(j)dj)/\pi$$
是给定选择下唯一的正则一形式。
换 $j'=j+\pi f$ 后，首差为
$$\pi\bigl(f\widehat H'(j)dj+\widehat H(j)df\bigr)\pmod{\pi^2}.$$
在 $X_h$ 上第二项消失，第一项是法向 $dJ$ 的倍数；换系数提升也仅增加法向倍数。
于是 $\nu_h=[\bar\gamma_j|_{X_h}]\in\Omega^1_{X_h}$ 与这些选择、标架和局部邻域无关，
并在全部原图上粘接。这里没有除以 $H'$，故没有悄加简单根条件。

环境楔积 $[\eta]\mapsto\eta\wedge dJ$ 是
$\Omega^1_{X_h}\simeq\Omega^2_{U_0}|_{X_h}$ 的线丛同构。
所以 $\Phi_h(\nu_h)/\Omega|_{X_h}$ 是整个 $X_h$ 上的正则函数。
在定义 $h$ 的底域扩张后，$X_h$ 射影几何整，故它是底域中的常数。
若仅在环面仿射曲线上做这一论证，常数结论没有依据；V 使用的恰是已接受完整纤维。
本步骤也说明只需在一个真实末端点核算常数，不需要假设辅助 gauge 在其余末端图存在。

### Step 7. V 的原正则 gauge 与重新循环插入：PASS

在 $x=u^{-1},y=W=1+uv$ 的实际第一末端图，将原矩阵直接共轭得到 V 的
$\widehat A$；其全部条目在 $\mathcal O[u,v,W^{-1}]$ 正则，
迹为 $t+J_tZ+Z^2$，行列式为 $Z^3$。
$G=\operatorname{diag}(u,1)$ 在 $u=0$ 不可逆，故不能在那里将其称为原标架的可逆变换。
正确论证是先在 $u\ne0$ 得到有序乘积的迹相等，再利用两侧正则性延到完整图。
由于 $G$ 不依赖谱变量，各因子间的 $G^{-1}G$ 才能按原次序消去。

本轮独立求导验证
$$\partial_u\widehat A
=G(\partial_u A_{\rm chart})G^{-1}+[K_u,\widehat A],
\qquad K_u=(\partial_uG)G^{-1}=\operatorname{diag}(u^{-1},0).$$
纠正项的 $(1,2)$ 条目为 $Z-u^{-1}$，并非零；不能逐项省略状态 gauge 导数。
V 没有这样做，而是对已经正则的 $\widehat A$ 重新证明
$$dI_p=p[Z^p]\operatorname{tr}
\bigl(d\widehat A(Z)\widehat A(q^{p-1}Z)\cdots\widehat A(qZ)\bigr).$$
$d\widehat A$ 包含上述纠正项，重新循环插入的证明不要求 $G$ 在末端可逆。
先除 $p$ 后的右边在该图正则，原 $I_p$ 的规范未变；这完成 M 到 V 的实际归一化接口。

奇 $p$ 时，将 M 应用于该商环及实际 $t$，得到
$$\alpha_p\equiv\widehat H_p(t,J_t)dJ_t+
\pi[Z^p]\Delta^{(p-3)/2}
\operatorname{tr}\bigl(d\widehat A[\widehat A,Z\partial_Z\widehat A]\bigr)
\pmod{\pi^2}.$$
零阶参照项使用实际时间，乘 $\pi$ 的系数才只取剩余值；任意时间提升的首影响没有被遗漏。
这也不要求将混合特征的 $t$ 写成某个未经构造的全局常数截面加 $\pi$ 项。

### Step 8. V 的全部 $R$ 系数及 CP 接口：PASS

在第一末端真实点 $u=0,v=1-h$，有
$$dJ=a_vdu-dv,\quad a_v=v+v^2-T,\qquad \Omega=-du\wedge dv.$$
从原共轭矩阵直接求导而非预设纯谱结果，核得
$$A_u=Z\begin{pmatrix}a_v&1\\-v^3&0\end{pmatrix},\qquad
A_v=\partial_v A_*.$$
若首谱项为 $\beta_u du+\beta_vdv$，其楔 $dJ$ 再除 $\Omega$ 的值是
$\beta_u+a_v\beta_v$，所以 V 的正号及切向组合正确。
由此得到的实际多项式
$$R=\operatorname{tr}\bigl((A_u+a_vA_v)[A_*,Z\partial_ZA_*]\bigr)\big|_{v=1-h}$$
没有常数项，且次数至多四；其四个系数独立核算为
$$\begin{aligned}
[Z^4]R&=h^2-3h-T+2,\\
[Z^3]R&=-2h^3+14h^2+6hT-24h-8T+12,\\
[Z^2]R&=-h^4+3h^3-2h^2+5hT+3T^2-4T,\\
[Z]R&=-h^3T+3h^2T+hT^2-2hT.
\end{aligned}$$
因此与 CP 的 $t\mapsto T$ 对应逐项完全相同，包括能级常数 $h$ 的规范和 $R/Z$ 的系数移位。
原 $dJ$、原 $\Omega$、原因子次序共同确定
$$c_h=[Z^p]R(T,h,Z)f(T,h,Z)^{(p-3)/2}=\Lambda_p(T,h).$$
因为光滑层 $f$ 可分，CP.2 使 $H_p(T,h)=0$ 时 $c_h\ne0$。
这不是声称 $\Lambda$ 在普通层也总非零；例如有限校验 $p=5,T=h=1$ 给 $\Lambda=0$ 而 $H=3$，
完全符合“不同时消失”的准确量词。

由 Step 6 的常数性，$\nu_h$ 在完整原 $X_h$ 的所有点非零。
另外，本轮对一般单位 $T$ 的四个原闭末端图直接代入，得到：

| 原图 | $u=0$ 上的 $J$ | 与 $X_h$ 的交点 $v$ | $\partial_vJ$ 在末端 | $\Omega/(du\wedge dv)$ |
|---|---|---|---|---|
| 1 | $1-v$ | $1-h$ | $-1$ | $-1/(1+uv)$ |
| 2 | $v/T$ | $Th$ | $1/T$ | $1/(T+uv)$ |
| 3 | $v/T$ | $Th$ | $1/T$ | $-1/(T+uv)$ |
| 4 | $1+v$ | $h-1$ | $1$ | $-1/(1+uv)$ |

这些都是完整末端仿射线上的有限点；$T\ne0$ 保证分母在末端为单位。
没有任何末端能级分量被删去或未覆盖，也没有把第一图的矩阵 gauge 冒称四图共用。

### Step 9. V 的特征二独立证明：PASS

直接从原 $q=-1$ 两因子乘积提取二次谱系数，有
$$I_2=\operatorname{tr}(A_0A_2+A_2A_0-A_1^2)
=2t-4b-J_t^2,\qquad b=x(y-1).$$
在特征零先除二，$\pi=-2$，故
$$\alpha_2=-J_t\,dJ_t+\pi\,db.$$
为对接 Step 6，可选 $H_2(T,J)=J$ 的整数系数提升 $\widehat H(j)=-j$，
此时 $\gamma=db$。若选 $+j$，得到 $\gamma=db+j\,dj$，额外项仍是法向项，切向类不变。
所以不能简单地将奇素数模 $\pi^2$ 的步骤照搬到此处，但 V 的独立式没有该问题。

本轮在整数 Laurent 环重新核准完整证书
$$xy\bigl(b_x(J_t)_y-b_y(J_t)_x\bigr)-t-x(y+1)J_t
=2x(xy-x-y).$$
模二并限制到唯一 Hasse 根 $J=0$，得 $db\wedge dJ=T\Omega$。
$T$ 为单位，故 $\nu_0$ 的常数非零；正则两侧的恒等式延到整个光滑几何整纤维。
无需假设 $b$ 在其他混合特征末端图正则，也没有半整数指数或特征二除零。

### Step 10. V 的理想、重根、完成及所有提升量词：PASS

在任意 $P\in X_h$ 处，$dj$ 的剩余非零，因而可补为实际局部自由基 $(dj,\theta)$。
在 Hasse 零层写
$$\alpha_p=(\widehat H(j)+\pi c_1)dj+\pi c_2\theta.$$
首切向类非零说明 $c_2$ 在该局部环为单位，因此
$$\mathfrak c(\alpha_p)_P
=(\widehat H(j)+\pi c_1,\pi c_2)=(\pi,\widehat H(j)).$$
若换成剩余函数的任一其他局部提升，两者之差在 $(\pi)$ 中，理想相同。
普通光滑层的 $H_p(T,J)dJ$ 在该点非零，故至少一个原系数已经是单位；V1 也成立。

定义 $h$ 的剩余域扩张后，在根附近可分解
$$H_p(T,J)=(J-h)^{e_h}U(J),\qquad U(h)\ne0.$$
对任意 $z$ 提升 $J-h$，选择 $U$ 的局部单位提升后，给
$$(\pi,\widehat H(j))=(\pi,z^{e_h}).$$
不要求 $H'$ 为单位、不约去 $z$，所以多重 Hasse 根并未被遗漏。
普通点不使用这一根分解。

等式先在实际局部环成立，包括非闭点；之后延伸到完成环。
在闭点处允许有限无分歧扩张将剩余点定义下来，再选相对完成坐标，
所用微分为原有限自由模的完成，等价于相应形式幂级数环的连续微分。
没有将其未完成代数 Kähler 模当成自由秩二，也没有要求非闭点由有限域扩张定义。

任意两种时间提升若具有相同剩余 $T$，奇特征中的 $c_h=\Lambda_p(T,h)$ 和特征二的 $c_0=T$ 相同，
故它们在自然识别的剩余曲线上的内在切向类相同。
各自实际局部环的理想都是剩余理想 $(H_p(T,J))$ 在约化映射下的逆像。
这给准确的提升不依赖描述，不声称两个不同混合特征模型的局部环已被额外同构，
更不声称实际一形式或法向首项相同。

最后，对约化到光滑 Hasse 零层的任一无分歧 DVR 状态提升，$\widetilde H$ 的评价属于 $(\pi)$，
且 $\pi$ 仍为参数，故整个系数理想的像准确为 $(\pi)$；普通层的像为单位理想。
这评价原两个系数，不是向 DVR 的零相对微分模拉回一形式。
乘上 $p=\text{unit}\cdot\pi^{p-1}$，原未整除理想与准确阶数 V3 立即得到。
因此 V 的全部原范围及与 M、CP 的实际接口合取成立。证毕。

## Corrections or Missing Assumptions

- 未发现硬缺口；三份作者输入及其全部被声称的数学量词保持原样。
- CP 的配对符号按其明确的负留数定义核准；不得移用相反槽次序后仍机械写正一。
- 在正特征中必须保留 CP Step 4 的负主部处理；删去它就不能以“有理恰当”替代 de Rham 类论证。
- V 的常数延拓依赖完整射影纤维，不是仿射环面；状态 gauge 导数必须保留。
- $a>1$ 在本报告中只核准 M 自己明确写出的矩阵恒等式及归一化接口，不扩张为 V 的几何结论。

## Actual Verification and Open Risks

本轮亲读 proof-writer 全文，据此拆开三个精确命题、各自假设、实际消费者及证明责任。
三件冻结输入均完整阅读；既有 p3 通过记录只作身份／范围背景，不作为新的全素数证明。
另完整读取固定脚本并运行 `python -B`，正常 exit 0，未创建数据文件。
独立只读内存计算另覆盖：

1. 通用整数二阶矩阵的 $\operatorname{ad}_A^3=\Delta\operatorname{ad}_A$ 全部条目。
2. 整数 Bezout 证书的全部系数、精确特征二 Laurent 证书、四次式判别式接口。
3. 从原矩阵直接共轭再求导的非零 gauge 纠正项、全部末端导数及 $R$ 的四个系数。
4. 一般 $T$ 的四个闭末端函数／二形式；有限 $p=3,5,7$ 的原降序双数乘积与常数系数匹配。
5. 若干 $N=p^a$ 的通用标量带权式样本，只检查符号与转录；无限量词由 Step 1 的证明承担。

所有数学通过判定依赖正文的整数恒等式、函数域／留数证明与局部／全局几何接口，
不把脚本成功、有限素数样本或符号系统输出独立等同于定理证明。
未新写或修改脚本、旧证明、失败记录、锁或接受源；交付前核对指定输入哈希保持不变。

本次未读取或评价三件之外的高层迭代／高 jet 探索。
不核准 $a>1$ 的垂直理想、$m>1$ 的块内变形、奇异能级、有分歧状态基变换的重新赋值、
稳定约化、晶体比较、野导子、全参数新意或独立长论文价值。
旧 C3、完整 pencil 与原辛几何继续作为已接受输入扣除；本次 PASS 不重投旧 C1–C3，
不启动候选、评分、稿件、PDF 或外部操作。
