# qPI：特征二、全部奇剩余阶的块首 jet 引理 V1

日期：2026-09-09。作者：`/root/p30_qpi_nonunit_tau_layer1_v1`。
类型：新的有界作者证明，待非作者检查；不是旧作者件的自审。
`route_applicability: NOT_APPLICABLE`。0 GPU；唯一新增文件为本件。
主控提供了待核准的特征二思路；下文给出原对象上的完整推导，不以该思路消息代替证明。

## Claim

设 $m\geq1$ 为奇数，$\mathcal O_0$ 是混合特征 $(0,2)$ 的无分歧 $2$-进 DVR，
完美剩余域记为 $k$。假设它含准确 $m$ 阶单位根 $\widetilde\eta$，剩余记作 $\eta$。
对任意 $a\geq2$，置
$$N=2^a,\qquad q_a=\zeta_{2^a},\qquad
\mathcal O_a=\mathcal O_0[q_a],\qquad \pi_a=q_a-1,\qquad s_a=\widetilde\eta q_a.$$
固定任意单位时间 $t_a\in\mathcal O_a^\times$，在原八截面模型上取
$$\alpha_{mN}=N^{-1}d_{\rm state}I_{mN,s_a}.$$
微分固定时间、根单位、底环系数及谱变量，保留两个状态方向。
原积分仍由原降序乘积的 $z^{mN}$ 迹系数定义。

置
$$B=\mathcal O_a/(\pi_a^2)\simeq k[\epsilon]/(\epsilon^2),\qquad
\epsilon=\pi_a\bmod\pi_a^2.$$
将 $\mathcal O_2/(\pi_2^2)$ 同样识别为 $B$，选择 $t_2$ 使其像等于 $t_a$ 的像 $t$。
两层原八截面模型的 $B$-基变换因此相同，记作 $\mathcal U_B$。
$\alpha_{m4}^{[2]}$ 和 $\alpha_{mN}^{[2]}$ 分别指这些原整除微分在共同模型上的约化。
这是以 $a=2$ 为基准的首 jet 比较，不与 $a=1$ 的特征四商识别。

在原环面 $R=B[x^{\pm1},y^{\pm1}]$ 上，令
$$s=\eta(1+\epsilon),\quad
\mathsf B_s(z)=A(s^{m-1}z;t)\cdots A(z;t),\quad
j_*=[z^m]\operatorname{tr}\mathsf B_s(z),$$
$$\mathsf B_0(z)=A(\eta^{m-1}z;\bar t)\cdots A(z;\bar t),\quad
J=I_{m,\eta}(x,y;\bar t),\quad T=\bar t^m,\quad S(Z)=T+JZ+Z^2.$$
其中 $\bar j_*=J$；$j_*$ 只先定义为实际环面函数，不假设它是全局提升。
对标量或一形式系数多项式，定义共振投影
$$\mathcal P_m\left(\sum_i c_i z^i\right)=\sum_{j\geq0}c_{mj}Z^j.$$
在剩余环面上定义
$$\Gamma_m(z)=\operatorname{tr}\bigl(d\mathsf B_0[\mathsf B_0,z\partial_z\mathsf B_0]\bigr),
\qquad \gamma_m(Z)=\mathcal P_m\Gamma_m(z),$$
$$\beta_N=[Z^N]\gamma_m(Z)S(Z)^{N-3},$$
$$\chi_m=J\,dJ+[z^{2m}]\operatorname{tr}\bigl(d\mathsf B_0\,z\partial_z\mathsf B_0\bigr).$$
一形式的乘积只指以标量相乘；本文不对一形式取 Frobenius 幂。

**P2.1：原环面的完整首 jet。** 对上述全部 $m,a,t_a$，
$$\boxed{\alpha_{mN}^{[2]}=j_*^{N-1}dj_*+\epsilon\beta_N,
\qquad \beta_N=J^{N-4}\beta_4.} \tag{P21}$$
特别地，原四块基准满足
$$\boxed{\beta_4=T\,dJ+J^2\chi_m,} \tag{P22}$$
$$\boxed{\alpha_{m4}^{[2]}=(j_*^3+\epsilon T)dj_*+\epsilon J^2\chi_m.} \tag{P23}$$
这里 $\epsilon$ 乘一个剩余一形式可使用其任意提升，结果不依赖提升。

**P2.2：整个原完整开放模型的因子分解。** 令 $\ell=N-4$。
$\ell=0$ 时定义 $J^{\langle0\rangle}=1$；$\ell>0$ 时，$J$ 的任意局部正则提升的 $\ell$ 次幂
彼此一致并粘成全局正则函数 $J^{\langle\ell\rangle}$。在整个共同模型上有
$$\boxed{\alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{m4}^{[2]}
\quad\text{in }\Gamma(\mathcal U_B,\Omega^1_{\mathcal U_B/B}).} \tag{P24}$$
包含原四条完整末端仿射线；不附加普通性、光滑能级、$J\ne0$ 或谱可分性条件。

## Status、Assumptions and Boundaries

**PROVABLE AS STATED（作者证明；待非作者检查）。**

本件只给模 $\pi_a^2$ 的完整一形式比较及环面的显式基准式。
它不证明 $\chi_m$ 在全部末端图正则、不证明其首切向值为单位，
也不从 (P23) 宣布 $a=2$ 的准确局部系数理想或任何更高厚度。
$a=1$ 不在比较范围；更高 $a$ 与 $a=2$ 的比较不是自然分歧嵌入的直接基变换。
时间仍为任意实际单位提升，不将 $t=t_0+\epsilon t_1$ 换成 $t_0$。

## Original Matrix and Dependency Map

为核准原矩阵规范，仅作记号缩写
$$b=x(y-1),\qquad c=y-1,\qquad \mathcal J(t)=y-x+x/y-t/x.$$
原矩阵准确为
$$A(z;t)=
\begin{pmatrix}t-b&-x\\c(b-t)&b\end{pmatrix}
+z\begin{pmatrix}\mathcal J(t)-1&1\\\mathcal J(t)+b-1&1\end{pmatrix}
+z^2E,\qquad E=\operatorname{diag}(1,0). \tag{1}$$
展开 (1) 恢复 brief 的 $A_0,A_1$；没有状态依赖共轭或能级重新规范。
保留整数身份 $\det A(z)=z^3$、$\operatorname{tr}A_0=t$、$\det A_0=0$。

证明责任顺序：

1. 高度至少二的圆分商与匹配时间给共同特征二模型。
2. 先在特征零循环插入并除以 $N$，再在共同商中保留全部块内变形。
3. 特征二的通用迹递推及加权交换子分别控制内部项和外部项。
4. 原块的实际次数界给唯一数字选择；特征二矩阵恒等式给基准 $\beta_4$。
5. 已接受 G 的原全局正则一形式、局部提升幂及四图限制单射给 (P24)。

步骤 2–4 在下文重新证明；不把奇素数作者式的半整数指数代入二。
G 仅提供原模型、$J$ 和整除微分的既有全局正则性，不提供 $\chi_m$ 或基准局部理想。

## Proof

### Step 1. 从 $a=2$ 开始的共同二阶商

圆分多项式
$$\Phi_{2^a}(1+X)=(1+X)^{2^{a-1}}+1$$
在 $\mathcal O_0$ 上对 $2$ Eisenstein：常数项为 $2$，其余非首项系数均被 $2$ 整除。
故 $\pi_a$ 是参数，且
$$v_{\pi_a}(2)=2^{a-1}\geq2.$$
因此 $2=0$ 于 $B$。$\mathcal O_0\to B$ 经 $\mathcal O_0/(2)=k$ 给系数域，
每个元素唯一写成 $u+v\pi_a$，$u,v\in k$；由此得到所声明的 $B$-同构。
$a=2$ 时同样成立，且 $\mathcal O_2=\mathcal O_0[i]$。
商映射满射，故可取所需单位时间 $t_2$。

两层均有 $q\mapsto1+\epsilon$、$s\mapsto\eta(1+\epsilon)$，以及同一个 $t$。
在不同原边界分量上的四个末次中心坐标 $1,t,t,s$ 逐一相同；
按原 $1+2+3+2$ 次序的标准吹起图及边界严格变换也相同，给共同 $\mathcal U_B$。
这一识别用实际标准图，不预设任意非平坦吹起基变换的通用结论。

当 $a>2$ 时，自然嵌入 $i\mapsto q_a^{2^{a-2}}$ 在当前商中将
$i-1$ 送到 $(1+\epsilon)^{2^{a-2}}-1=0$，不是 $\epsilon$。
当 $a=1$ 时，$\pi_1=-2$，二阶商为特征四。
因此两种不能使用的跨层识别均被排除。

### Step 2. 原整数块插入与实际块内变化

先在 $\mathcal O_a$ 的 Laurent 状态环中取 $r=s_a^m$，其准确阶为 $N$。
原长度 $mN$ 乘积准确分为
$$M_{mN,s_a}(z)=\mathsf B_{s_a}(r^{N-1}z)\cdots\mathsf B_{s_a}(rz)\mathsf B_{s_a}(z).$$
对迹作状态微分时，将第 $j$ 块微分循环移到首位，并令 $w=r^jz$。
其余块仍按 $N-1,\ldots,1$ 降序出现；$r^N=1$ 保证环绕处一致。
取 $z^{mN}$ 系数的变量替换因子为 $r^{jmN}=1$，所以每个块位置的该系数相同。
相加后先在特征零得到
$$dI_{mN,s_a}=N[z^{mN}]\operatorname{tr}\bigl(d\mathsf B_{s_a}(z)
\mathsf B_{s_a}(r^{N-1}z)\cdots\mathsf B_{s_a}(rz)\bigr).$$
除以 $N$ 后的右侧是整系数一形式，随后才可约化：
$$\alpha_{mN}^{[2]}=[z^{mN}]\operatorname{tr}\bigl(d\mathsf B_s(z)
\mathsf B_s(r^{N-1}z)\cdots\mathsf B_s(rz)\bigr). \tag{2}$$
$d\mathsf B_s$ 已含块内全部 $m$ 个微分位置，没有再乘或除一个 $m$。

现在在 $R$ 中工作，$t$ 仍为实际时间。令 $\mathsf A_j=A(\eta^jz;t)$。
由 $s^j=\eta^j(1+j\epsilon)$ 逐因子展开，有
$$\mathsf B_s=\mathsf B_\eta(z;t)+\epsilon\mathsf C(z),$$
$$\mathsf C(z)=\sum_{j=0}^{m-1}j\mathsf A_{m-1}\cdots\mathsf A_{j+1}
(z\partial_z\mathsf A_j)\mathsf A_{j-1}\cdots\mathsf A_0. \tag{3}$$
空乘积为单位矩阵。$\mathsf C$ 只需模 $\epsilon$ 的值；(3) 展示全部块内谱变化。
$m=1$ 时该和为零，但时间变化仍保留在 $A(z;t)$ 中。

记 $S_s=\operatorname{tr}\mathsf B_s$、$D_s=\det\mathsf B_s$。
循环迹与 $\eta$ 的准确阶给
$$\operatorname{tr}\mathsf B_\eta(z;t)=t^m+j^\circ z^m+z^{2m}.$$
这在当前非约化环中也成立：循环迹直接成立，非 $m$ 倍次数被单位 $\eta^i-1$ 杀掉；
首项由 $A_0^m=t^{m-1}A_0$ 得到，最高项由 $E^m=E$ 得到。
因此，令 $j_*=[z^m]S_s$ 后可写
$$S_s=S_*(z^m)+\epsilon V(z),\qquad
S_*(Z)=t^m+j_*Z+Z^2,\qquad \mathcal P_mV=0. \tag{4}$$
最高系数准确为 $s^{m(m-1)}=1$，因为 $m(m-1)$ 为偶数。
行列式仍须保留为
$$D_s=s^{3m(m-1)/2}z^{3m},\qquad dD_s=0. \tag{5}$$
该常数的首 jet 可能非零；只是后续特征二迹递推不依赖它，不能先验删除。

### Step 3. 内部项准确为 $j_*^{N-1}dj_*$

对通用二阶矩阵 $M$，写 $S_M=\operatorname{tr}M$、$D_M=\det M$。
Cayley–Hamilton 及行列式微分给
$$\operatorname{tr}(dM\,M^{N-1})
=U_{N-1}(S_M,D_M)dS_M-U_{N-2}(S_M,D_M)dD_M,$$
其中 $U_{-1}=0,U_0=1,U_n=SU_{n-1}-DU_{n-2}$。
特征二且 $N=2^a$ 时，通用对称变量中的多项式恒等式
$$U_{N-1}(u+v,uv)=\frac{u^N-v^N}{u-v}=(u+v)^{N-1}$$
经对称多项式环的单射下降为 $U_{N-1}(S,D)=S^{N-1}$。
这里商是多项式，不要求实际矩阵有不同特征根；该恒等式可代入含平方零元的 $R$。
由 (5)，内部项是
$$F_N:=[z^{mN}]\operatorname{tr}(d\mathsf B_s\mathsf B_s^{N-1})
=[z^{mN}]S_s^{N-1}dS_s.$$

投影只使用准确性质
$$\mathcal P_m(Q(z^m)P(z))=Q(Z)\mathcal P_m(P(z)), \tag{6}$$
不把它当作一般环同态。由 (4) 和 $\epsilon^2=0$，相对 $S_*(z^m)$ 的差项只有
$\epsilon(N-1)S_*^{N-2}VdS_*$ 与 $\epsilon S_*^{N-1}dV$；
两者投影均为零，因为 $\mathcal P_mV=\mathcal P_m(dV)=0$。
故
$$F_N=[Z^{N-1}]S_*(Z)^{N-1}\,dj_*.$$
在特征二中 $S_*^{N-1}=\prod_{i=0}^{a-1}S_*^{2^i}$。
每一因子的原指数只可为 $0,1,2$；要凑成 $2^a-1$，最低位须为奇数，故只能取 $1$。
减去一再除以二，逐位都只能取一，取得
$$\boxed{F_N=j_*^{N-1}dj_*.} \tag{7}$$
$t^m$、$j_*$ 和 $dj_*$ 仍包含原时间的完整首 jet；没有遗漏 $t_1\partial_t(dJ)$。

### Step 4. 特征二加权交换子与外部项

在任意特征二交换环中，二阶矩阵满足
$$\operatorname{ad}_M^2(X)=S_M\operatorname{ad}_M(X). \tag{8}$$
事实上 $M^2=S_MM+D_M\mathrm{id}$，而
$[M,[M,X]]=M^2X+XM^2$；行列式标量的两个贡献相消，得到 (8)。

标量恒等式
$$\sum_{j=0}^{N-1}U^{N-1-j}V^j=(U+V)^{N-1}$$
来自 $N-1$ 的全部二进制位为一。对 $V$ 微分，得
$$\sum_{j=1}^{N-1}jU^{N-1-j}V^{j-1}=(U+V)^{N-2}.$$
代入彼此交换的左乘、右乘算子，$N\geq4$ 时再用 (8)，得到
$$\sum_{j=1}^{N-1}jM^{N-1-j}XM^{j-1}
=\operatorname{ad}_M^{N-2}(X)=S_M^{N-3}[M,X]. \tag{9}$$
不除以 $S_M$、$D_M$ 或判别式；$S_M=0$ 的状态也在恒等式中。

$m$ 为奇数，故在 $B$ 中 $r=s^m=1+\epsilon$。
每个外部块因而为
$$\mathsf B_s(r^jz)=\mathsf B_s(z)+\epsilon j\,z\partial_z\mathsf B_0(z).$$
在 (2) 的降序乘积中展开，用 (9)，全部外部修正已乘 $\epsilon$，
所以其中其他块与微分只取剩余值。于是
$$\alpha_{mN}^{[2]}=F_N+\epsilon[z^{mN}]\Gamma_m(z)S(z^m)^{N-3}
=F_N+\epsilon\beta_N. \tag{10}$$
这里外部速度是整数 $m$ 的剩余值 $1$；这与 (2) 不再乘 $m$ 的归一化是不同事实。

### Step 5. 原次数界与唯一数字选择

原剩余块的最高谱系数为 $E$，与状态无关，所以
$$\deg_z d\mathsf B_0\leq2m-1.$$
特征二中最高项 $z^{2m}E$ 的 $z\partial_z$ 导数为零，故
$$\deg_z(z\partial_z\mathsf B_0)\leq2m-1.$$
交换子因而次数至多 $4m-1$，得到
$$\deg_z\Gamma_m\leq6m-2,\qquad [z^0]\Gamma_m=0. \tag{11}$$
所以 $\gamma_m$ 仅可能支持于 $Z^1,\ldots,Z^5$；$m=1$ 时实际至多到 $Z^4$。
$\gamma_mS$ 因而仅可能支持于 $Z^1,\ldots,Z^7$。

对 $a\geq2$，有准确分解
$$\gamma_mS^{N-3}=(\gamma_mS)\prod_{i=2}^{a-1}S^{2^i}.$$
要贡献 $Z^N$，第一因子的指数 $n_0\in[1,7]$ 必须被四整除，故只能为 $4$。
减去四并除以四后，剩下目标 $2^{a-2}-1$，每个原指数仍在 $\{0,1,2\}$。
按 Step 3 的二进制理由，各位只能取一；其系数贡献为 $J^{4+8+\cdots+2^{a-1}}=J^{N-4}$。
$a=2$ 时后续积为空，同样成立。因此
$$\boxed{\beta_N=J^{N-4}[Z^4](\gamma_mS)=J^{N-4}\beta_4.} \tag{12}$$
这里仅对标量 $S$ 作 Frobenius 幂；$\gamma_m$ 中的两个状态方向都保留。

### Step 6. 特征二的 $\Gamma_m$ 恒等式与基准系数

暂记 $M=\mathsf B_0(z)$，$R_z=z\partial_zM$，
$\mathcal S(z)=\operatorname{tr}M=S(z^m)$，$\mathcal D(z)=\det M=z^{3m}$。
原 $m$ 为奇数，且 $\eta^{3m(m-1)/2}=1$，所以该行列式规范准确。
状态方向满足 $d\mathcal D=0$。

对 $M^2+\mathcal SM+\mathcal D\mathrm{id}=0$ 求状态微分，移项并利用特征二，得到
$$M\,dM+dM\,M=(d\mathcal S)M+\mathcal S\,dM.$$
乘 $R_z$ 并取迹，使用仅含一个一形式的循环迹，得
$$\Gamma_m=d\mathcal S\operatorname{tr}(MR_z)+\mathcal S\operatorname{tr}(dM\,R_z).$$
行列式的谱微分恒等式 $\operatorname{adj}(M)=\mathcal S\mathrm{id}+M$ 又给
$$z\partial_z\mathcal D=\mathcal S(z\partial_z\mathcal S)+\operatorname{tr}(MR_z).$$
故准确有
$$\boxed{\Gamma_m=(z\partial_z\mathcal D)d\mathcal S+\mathcal S K_m,} \tag{13}$$
$$K_m=d\mathcal S(z\partial_z\mathcal S)+\operatorname{tr}(dM\,R_z).$$
这一步必须使用实际 $d\mathcal D=0$；对任意有状态变行列式的矩阵不能省去对应的附加项。

因为 $m$、$3m$ 均为奇数，
$$d\mathcal S=z^m dJ,\qquad z\partial_z\mathcal S=Jz^m,\qquad z\partial_z\mathcal D=z^{3m}.$$
因此 (13) 成为
$$\Gamma_m=z^{4m}dJ+S(z^m)K_m,$$
$$K_m=J\,dJ\,z^{2m}+\operatorname{tr}(d\mathsf B_0\,z\partial_z\mathsf B_0). \tag{14}$$
由 Step 5，迹项次数至多 $4m-2$，且常数项为零。
对于全部 $m\geq1$，$2m\leq4m-2$，故 $K_m$ 同样无常数、次数至多 $4m-2$。
令 $\kappa_m(Z)=\mathcal P_mK_m$，则其支持至多为 $Z^1,Z^2,Z^3$；
$m=1$ 时至多到 $Z^2$，且 $[Z^2]\kappa_m=\chi_m$。
由 (6)、(14)，
$$\gamma_m=Z^4dJ+S\kappa_m.$$
特征二中 $S^2=T^2+J^2Z^2+Z^4$。提取 $Z^4$，利用
$[Z^0]\kappa_m=[Z^4]\kappa_m=0$，取得
$$\beta_4=[Z^4](\gamma_mS)=T\,dJ+J^2[Z^2]\kappa_m
=T\,dJ+J^2\chi_m.$$
结合 (7)、(10) 以及 $\epsilon dJ=\epsilon dj_*$，证明 (P21)–(P23)。

作为 $m=1$ 的原式边界核准，$\mathsf B_s=A(z;t)$、$j_*=\mathcal J(t)$，无块内谱修正。
此时 $z\partial_z\mathsf B_0=zA_1$，且 (1) 直接给
$$\operatorname{tr}(dA_1A_1)=J\,dJ+db.$$
因此 $\chi_1=db=d[x(y-1)]$，从而
$$\beta_4=T\,dJ+J^2d[x(y-1)].$$
这只是同一公式的显式边界，不作末端单位推断。

### Step 7. 因子分解跨过全部原末端线

若 $\ell=N-4>0$，则 $\ell$ 为偶数；任意两个 $J$ 的局部提升相差 $\epsilon f$，故
$$ (j+\epsilon f)^2=j^2,\qquad (j+\epsilon f)^\ell=j^\ell.$$
所以这些幂确实粘合为全局正则函数，不需要 $J$ 有全局提升。
在共同环面上，由 (10)、(12) 得
$$\alpha_{mN}^{[2]}
=j_*^{N-1}dj_*+\epsilon J^{N-4}\beta_4
=j_*^{N-4}\bigl(j_*^3dj_*+\epsilon\beta_4\bigr),$$
即 (P24) 的环面式；$N=4$ 时为恒等边界。

由已接受 G，两个原整除微分均在共同 $\mathcal U_B$ 上正则，乘数也已正则。
在 G 的四张实际末端图上，坐标环分别为 $B[u,v]$ 关于
$1+uv,t+uv,t+uv,s+uv$ 的相应局部化，环面交再求逆 $u$。
即使 $B$ 非约化，按 $u$ 的幂比较系数可知乘 $u$ 单射；局部化保留此性质。
相对余切模在这些图上自由，所以它到环面交的限制也单射。
两边差在环面为零，因而在四张末端图也为零，证明完整的 (P24)。
此论证未使用 $\chi_m$ 或 $\beta_4$ 的未知全图正则性。证毕。

## Finite Exact Verification

本次仅运行内存 `python -B` 精确有限域计算，退出码为 0，未新增脚本或数据文件。
实现直接以原矩阵构造块，使用 $k[\epsilon]/(\epsilon^2)$ 并自动保留 $dx,dy,\epsilon dx,\epsilon dy$，
再直接计算 (2) 的原降序插入，不从特征二的 $dI=0$ 反除 $N$。
同时独立计算内部项、$\Gamma_m$、$K_m$、$\chi_m$、$\beta_N$ 和两个完整一形式系数。

有限域采用二进制幂基标签：整数 $\sum b_i2^i$ 表示 $\sum b_i\theta^i$，
不是将整数标签当作素域元素。以下每个 $\eta$ 均另外检验准确阶为 $m$。

| $k$ 及 $\theta$ 的多项式 | $(m,\eta,a)$ | $(t_0,t_1,x,y)$，$t=t_0+\epsilon t_1$ | 检查结果 |
|---|---|---|---|
| $\mathbb F_4$，$\theta^2+\theta+1$ | $(1,1,3)$ | $(3,2,3,2)$ | 内部项、(13)–(14)、基准式、$\beta$ 及完整因子分解全部通过 |
| 同上 | $(3,2,2)$、$(3,2,3)$、$(3,2,4)$ | $(3,2,2,3)$ | 同上；实际块内非共振项非零 |
| $\mathbb F_8$，$\theta^3+\theta+1$ | $(7,2,3)$ | $(4,6,2,5)$ | 同上；实际块内非共振项非零 |
| $\mathbb F_{16}$，$\theta^4+\theta+1$ | $(5,8,3)$ | $(2,5,3,7)$ | 同上；实际块内非共振项非零 |

这些时间和状态均为单位，并含非素域 tame 根与非平凡时间首 jet。
样本只承担排错，全部 $m,a,t_a$ 的量词由 Steps 1–7 证明。

## Actual Inputs and Ownership

| 输入 | 本次实读与使用范围 | SHA-256 |
|---|---|---|
| [整数 brief](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | §2，第 32–86 行；原矩阵、积分规范、八截面 | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` |
| [整除诊断 D](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 全文 268 行；仅消费已接受整数插入、原迹／行列式与二阶递推接口；本件重写所需代数 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| [完整模型 G](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 第 1–123、222–233 行；原模型、$J$ 及整除微分全局正则性、四末端图 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| [奇素数 tame-block 作者件](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md) | 第 105–230 行及定向定义／边界检索；对照块插入与完整块内变化，不消费奇素数结论来覆盖二 | `6546720ecf39f667f09d45235dc0c7be340032b4c3f7c809e9d1cb60257396e9` |
| [旧全局首 jet 作者件](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_FACTORISATION_V1_20260909.md) | Steps 1、2、4 的第 87–115、134–145 行及定向定义检索；对照模型识别／限制单射，不消费首层理想 | `9d53bee5abf8026dfa09d2bcb38713e0ace28ff082d9e87b3efa595ab5955a86` |

主控的特征二提案与作者的推导已明确区分；没有读取其他新独立审查。
使用 `proof-writer` 的准确命题、依赖图、分步证明及边界结构；未新增外部来源、新意或 Route 判断。

## Corrections or Missing Assumptions

上述原首 jet 断言无需弱化。
特征二的矩阵恒等式 (13) 明确使用原 $d\mathcal D=0$，不可推广为任意状态变行列式矩阵的无条件式。
字母 $z$ 是谱变量，而末端图的 $u,v$ 是状态坐标；谱微分与状态微分始终分开。
基准必须是 $a=2$，且两层时间的完整二阶像必须一致。

## Open Risks and Delivery Boundary

作为新的作者证明，本件全部新特征二接口仍待非作者核查。
尚未证明 $\chi_m$ 的全图正则性、首切向非零、基准 $a=2$ 的准确局部理想、
全高度准确厚度、额外分歧状态赋值或完整初始理想。
因子分解本身不消除这些证明责任，不将模 $\pi_a^2$ 的等式升为整数局部环中的等式。
不创建 Paper30 项目、稿件、source/publication locks、PDF、GPU 任务、外部效力或新评分。
旧作者件、审查、索引及锁保持冻结；只新增本文件，全文回读并交付 SHA 后停止修改。
