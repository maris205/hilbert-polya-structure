# Proof Package：qPI 全有限闭纤维共轭与有限域自治回归约化 V1

日期：2026-09-08。作者：主控 `/root`。
这是泛回返点之后的新数学消费者，不是论文、正式四门票或候选 V1 的追溯修订。
所有冻结输入、已接受结果及新意失败记录保持不变。

## Claim

令 $k_0$ 为域，$s,t\in k_0^*$，$s$ 的精确有限阶为 $r\ge1$，
$T=t^r$，$\varepsilon=(-1)^{r+1}$。采用原八吹起曲面 $S_{t,s}$、
完整合法初值开曲面 $U_{t,s}$ 及原积分 $f=I_r:U_{t,s}\to\mathbb A^1_c$。
记实际完整纤维 $X_c=f^{-1}(c)$，一步与回返为

$$
F_t:U_{t,s}\longrightarrow U_{st,s},\qquad
F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad
\mathcal R=F_{s^{r-1}t}\circ\cdots\circ F_t.
\tag{1}
$$

有理式在四条末端直线上的含义是 R 已证明的完整同构，不删分母为零的合法状态。
令 $W_\varepsilon(c,T)$ 为带 $O=[0:1:0]$ 的射影三次曲线

$$v^2+cuv-\varepsilon Tv=u^3-Tu^2,\qquad P=(0,\varepsilon T).\tag{2}$$

记原参数上的首一坏值四次为

$$\delta(c,T)=c^4-\varepsilon c^3-8Tc^2+36\varepsilon Tc+16T^2-27T.$$

**C1：逐闭纤维指定共轭。** 对每个 $c_0\in k_0$，若 $X_{c_0}^{\rm sm}(k_0)$ 非空，
则存在 $k_0$-曲线同构

$$\phi_{c_0}:X_{c_0}\xrightarrow{\sim}W_\varepsilon(c_0,T),\qquad
\phi_{c_0}\mathcal R=\theta_{c_0}\phi_{c_0}.\tag{3}$$

这里 $\theta_c$ 是下式在整个射影三次曲线上的唯一自同构延拓：

$$
m=\frac{v-\varepsilon T}{u},\quad
u'=m^2+cm+T-u,\quad v'=-(m+c)u'.
\tag{4}
$$

式 (4) 首先定义于非空稠密开集 $u\ne0$；不把它当作遗漏点处的坐标公式。
在光滑纤维上 $\theta_c=\tau_P$，即准确加 (2) 的点 $P$。
在奇异纤维上 $\theta_c$ 固定唯一几何奇点，且 (3) 保留整个曲线和全部合法状态。
可指定任何 $q_0\in X_{c_0}^{\rm sm}(k_0)$ 使 $\phi_{c_0}(q_0)=O$。

**C2：所有有限域闭纤维。** 当 $k_0=\mathbb F_q$ 时，对每个 $c_0\in\mathbb F_q$，
C1 的光滑有理点假设自动成立。故 (3) 对全部光滑和奇异有限纤维成立，
没有 $q$、$t\ne0$、$r$、特征 $2,3$ 或奇异参数碰撞的额外例外。

**C3：回归置换的自治普适性。** 在 C2 条件下，令
$\mathcal A_T=F_T:U_{T,1}(\mathbb F_q)\to U_{T,1}(\mathbb F_q)$
为参数 $s=1,t=T$ 的原自治系统。存在集合双射

$$
\beta:U_{t,s}(\mathbb F_q)\xrightarrow{\sim}U_{T,1}(\mathbb F_q),
\quad \beta\mathcal R=\mathcal A_T\beta,
\quad I_1(\beta Q)=\varepsilon I_r(Q).
\tag{5}
$$

它逐纤维来自定义在 $\mathbb F_q$ 上的整个曲线同构。
因此完整回归置换的循环类型只依赖 $q,T=t^r$，不另外依赖 $s,r,t$ 的选择。
双射通常非典范；不宣称它来自整个曲面的有理映射或 $k_0(c)$ 上的 torsor 平凡化。

**C4：原一步置换的精确悬挂及循环频数。** 令

$$\Omega_{t,s}=\coprod_{j=0}^{r-1}U_{s^jt,s}(\mathbb F_q)$$

为一个非零时间轨道上的全部合法状态，时间标签保留。
原一步置换共轭于 $\{0,\ldots,r-1\}\times U_{T,1}(\mathbb F_q)$ 上

$$
\Sigma(j,z)=
\begin{cases}(j+1,z),&j<r-1,\\(0,\mathcal A_Tz),&j=r-1.\end{cases}
\tag{6}
$$

若 $a_{T,q}(n)$ 是完整自治置换中长度恰为 $n$ 的循环数，
则 $\Omega_{t,s}$ 上原一步长度恰为 $rn$ 的循环数准确为 $a_{T,q}(n)$，
不存在不被 $r$ 整除的完整周期。特别是循环数不再乘 $r$。
若再取全部非零时间 $\Omega_s=\coprod_{t\in\mathbb F_q^*}U_{t,s}(\mathbb F_q)$，
置 $H=(\mathbb F_q^*)^r$，则完整一步循环数为

$$
b_{s,q}(m)=
\begin{cases}
\displaystyle\sum_{T\in H}a_{T,q}(m/r),&r\mid m,\\
0,&r\nmid m.
\end{cases}
\tag{7}
$$

式 (7) 是精确有限置换分解，不是随素数变化的概率或渐近分布定理。

## Status

作者判断：PROVABLE AS STATED。以下证明 C1–C4；本新稿尚待独立非作者核查。
未宣称一般 torsor、最小模型唯一性、Weil 界或循环悬挂机制为新理论。
精确奇异乘法／加法群参数和点阶的独立证明由另一有界作者件处理，本稿不预消费它。

## Assumptions and frozen inputs

仅使用以下已接受身份；它们旧文中的待审文字是冻结时快照。

| ID | 作者输入 | SHA256 | 本件消费范围 |
|---|---|---|---|
| V | [准确泛回返点](PAPER30_QPI_EXPLICIT_RETURN_POINT_ENTRY_V1_20260908.md) | 2ca0b56081c76be343c0b8d86c6a5463533802d4aee8baed7068d992d830a0e7 | 固定 J 的原域 torsor 作用后，原泛回返准确为加 $P$；不预消费闭纤维 |
| J | [原谱模与 Jacobian](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f | Claim、Step7 的指定 $E$-torsor 及原域作用；任意域接口按已接受共享 V2 |
| B | [原基底 Weierstrass 模型](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | 1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1 | Step1 带原点代换、Step3 总空间正则及几何整约化；不把其代数闭域截面选择直接用于有限域 |
| R | [实际完整同构](PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md) | 9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c | Step1–2 的全部合法状态／曲面同构，保持原能级 |
| F | [实际有限纤维](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003 | 有限纤维几何整约化、算术亏格一；坏纤维唯一奇点、几何正规化亏格零、至多双支 |
| G | [原始亏格一 pencil](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace | 原 $f$ proper、flat、几何泛光滑亏格一，$U=f^{-1}(\mathbb A^1)$ |

实际吹起中心、映射及积分都定义在 $k_0$，光滑性、几何整约化等几何性质
由原域构造及向 $\overline{k_0}$ 的忠实平坦检验得到；没有只从几何同构猜测原域同构。
共享 [W V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md)
Step2a 补齐 J 所需的任意原域接口，其输入保持不变。
该共享输入 SHA256 为 `21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2`。

## Notation and source scope

$W$ 总指 (2) 的射影三次族，$W^{\rm sm}_c$ 指曲线的光滑点开集。
$\mathcal R$ 是动力回返；下面的 $A_0,A$ 是局部环，避免同一字母兼指两者。
$N_{T,h}=\#W_1(h,T)(\mathbb F_q)$ 在光滑处可用于点阶周期公式，
但本稿不把所有奇异点也算进光滑群的阶。

主控已定向读取以下一手资料的实际相关段落：

- [Stacks §55.10, 0C9Y](https://stacks.math.columbia.edu/tag/0C9Y)，
  Lemmas 55.10.1–2 的陈述与证明：任意 DVR 上，光滑射影几何整正亏格泛曲线的
  最小正则 proper 模型唯一；给定泛同构唯一延伸。
- [Stacks §15.46, 07QL](https://stacks.math.columbia.edu/tag/07QL)，
  henselization 的 DVR、正则性及剩余域保持；
  [§15.9, 07LW](https://stacks.math.columbia.edu/tag/07LW)，Lemma 15.9.14 的光滑点提升。
- [Milne, Algebraic Geometry, Chapter 11, 2024](https://www.jmilne.org/math/CourseNotes/AG11.pdf)，
  §d 末尾 pp.37–38：从曲线自对应的交数不等式推出任意光滑射影几何整曲线的
  $|\#C(\mathbb F_q)-(q+1)|\le2g\sqrt q$。
  此处使用的是一般曲线 Weil 界，不是预先要求原点的椭圆曲线版本。

以上均为标准数学工具的归属，不是本件新意证据；未宣称全文读完所列书籍或所有章节。
JR 的原映射、积分和状态来源沿用冻结作者件；新普适性主张的全球查新另行进行。

## Proof strategy and dependency map

1. 实际与 Weierstrass 模型的正则、最小性加光滑剩余点提升，给原域局部模型同构。
2. 在已指定的泛 torsor 上选原点，使该同构等变；唯一延伸把准确回返送至 (4)。
3. 一般曲线 Weil 界保证有限域每条实际纤维有光滑有理点，关闭 C1 的局部条件。
4. $v\mapsto\varepsilon v,c\mapsto\varepsilon c$ 去掉唯一的 $r$ 奇偶符号，
   两次 C1 与自治情形合成，得到全状态回归共轭。
5. 保留时间标签，用有限置换的显式坐标构造悬挂，最后对时间轨道作不重不漏求和。

## Proof

### Step 1. 保持原剩余域的最小正则模型

先在任意 $k_0$ 上固定 C1 的 $c_0,q_0$，令

$$A_0=k_0[c]_{(c-c_0)},\qquad A=A_0^h,\qquad L=\operatorname{Frac}(A).\tag{8}$$

$A$ 是 henselian DVR，uniformizer 为 $c-c_0$，剩余域仍为 $k_0$。
令 $\mathscr X=S_{t,s}\times_{\mathbb P^1_c}\operatorname{Spec}A$。
由 G，它 proper、flat、finite type，泛纤维光滑几何整且亏格一。
实际 $S_{t,s}$ 是在 $k_0$ 上八个光滑有理中心依次吹起得到的光滑曲面；
局部化及 ind-étale henselization 保持这里的正则性，所以 $\mathscr X$ 正则。
其特殊纤维是原 $X_{c_0}$，由 F 几何整约化；唯一竖直整分量就是完整主纤维，
其自交数为零。因此没有第一类例外曲线，$\mathscr X$ 是最小正则 proper 模型。

对 $\mathscr W=W\times_{\mathbb A^1_c}\operatorname{Spec}A$ 逐项作相同判据。
B Step3 已给每条几何纤维整约化、$O$ 相对光滑；
在仿射方程 $F=v^2+cuv-\varepsilon Tv-u^3+Tu^2$ 的相对奇点处 $uv\ne0$，
所以 $F_c=uv\ne0$。这也在任意原域上给总空间光滑，从而 $\mathscr W$ 正则。
它 projective、flat，特殊纤维唯一分量自交数零，故亦为最小正则 proper 模型。
泛光滑性由 $\Delta=T^3\delta(c,T)\ne0$ 给出，其中 $\delta$ 是首一四次。
这一步不使用短 Weierstrass 公式，也不需要除以 $2$、$3$ 或 $r$。

### Step 2. 指定原域等变平凡化与整个闭纤维延伸

因为 $q_0$ 是特殊纤维的 $k_0$-光滑点且 $\mathscr X\to\operatorname{Spec}A$ 平坦，
该态射在 $q_0$ 附近光滑。取相对一维的局部 étale 坐标并使剩余坐标为零；
沿零截面拉回得到具有该 $k_0$-点的 étale $A$-概形。
henselian 提升给截面 $e:\operatorname{Spec}A\to\mathscr X$，且 $e(k_0)=q_0$。
这里未扩张剩余域，更未假设 $X(k_0(c))$ 非空。

固定 V/J 的 torsor 作用后，由 $e_L$ 得到唯一等变同构

$$
\phi_L:X_L\xrightarrow{\sim}E_L\xrightarrow{\sim}W_L,
\quad \phi_L(e_L)=O,
\quad \phi_L(Q+N)=\phi_L(Q)+N.
\tag{9}
$$

末式中的 $N$ 通过 B Step1 的带原点识别表示于 $W_L$。
因此 V 给出指定等式 $\phi_L\mathcal R\phi_L^{-1}=\tau_P$，
不是“某个平移”或允许再乘单位／复乘自同构的未知点。

双方模型的泛曲线均光滑、射影、几何整，$H^0=L$，亏格一。
Step1 的正则、proper、最小性核定了 Stacks 55.10.1–2 的全部假设。
于是 (9) 唯一延伸为 $A$-模型同构

$$\phi_A:\mathscr X\xrightarrow{\sim}\mathscr W.\tag{10}$$

泛自同构 $\tau_P$ 及其逆也由同一定理延伸为 $\mathscr W$ 的互逆自同构；
记前者为 $\theta_A$。R 的完整曲面同构保持 $c$，因而给 $\mathscr X$ 的自同构。
两个 $\mathscr W$ 的 $A$-自同构 $\phi_A\mathcal R\phi_A^{-1}$ 和 $\theta_A$
在泛纤维相同。模型平坦且整，泛纤维稠密，目标分离，故它们处处相同。
特殊纤维遂得 (3)，且 $\phi_{c_0}(q_0)=O$。

### Step 3. 无遗漏的指定坐标公式

在泛光滑三次上，过 $P=(0,\varepsilon T)$ 与 $(u,v)$ 的直线为
$v=m u+\varepsilon T$，$m=(v-\varepsilon T)/u$。
代入三次并用三根之和得第三交点的横坐标 $m^2+cm+T-u$。
长 Weierstrass 负元是 $(u,v)\mapsto(u,-v-cu+\varepsilon T)$，
故取负后的纵坐标为 $-(m+c)u'$；得到准确 (4)。

这些式子在 $\mathscr W$ 的仿射开集 $u\ne0$ 上分母为单位，
且代入目标方程所得恒等式在泛纤维成立。
该开集的坐标环无 $A$-挠，故恒等式在整个开集成立，给到仿射 $\mathscr W$ 的态射。
它与 $\theta_A$ 泛纤维相等，分离性再次给整个开集上的相等。
每条特殊纤维几何整且非包含于 $u=0$，所以此开集在每条特殊纤维上非空稠密。
这证明 $\theta_{c_0}$ 的限制正是 (4)，不只是未知自同构的存在。

特殊纤维上的自同构延拓唯一，因为两个曲线态射在稠密开集相等即处处相等。
光滑时这是以 $O$ 为零元的三次群律加 $P$；$P$ 在所有纤维都光滑，
其 $F_v$ 为 $\varepsilon T\ne0$。
奇异时由 F/B 至多一个几何奇点，任何曲线自同构保持光滑性，故固定该奇点。
并未把正规化上的稠密有理式未经下降检验就当作奇异曲线自同构。
C1 得证。

### Step 4. 有限域每条实际纤维均有光滑有理点

现令 $k_0=\mathbb F_q$。光滑 $X_c$ 是光滑射影几何整亏格一曲线，
一般曲线的 Weil 界直接给

$$\#X_c(\mathbb F_q)\ge q+1-2\sqrt q=(\sqrt q-1)^2>0.\tag{11}$$

这里 $q\ge2$，所计点全光滑；不预先使用椭圆原点，也不循环地引用 C1。
若 $X_c$ 奇异，则 F 给唯一几何奇点及几何亏格零。
有限域完美，其正规化 $\nu:\widetilde X_c\to X_c$ 是光滑射影几何整亏格零曲线，
与代数闭基变换相容。Weil 界在亏格零给

$$\#\widetilde X_c(\mathbb F_q)=q+1.\tag{12}$$

唯一奇点的几何逆像至多有两个点，故至多删去两个有理点。
在其余开集上正规化为同构，因而

$$\#X_c^{\rm sm}(\mathbb F_q)\ge q-1\ge1.\tag{13}$$

奇点唯一性也保证它在有限域上有理，但 (13) 只需逆像的上界。
因此所有 $c$ 都满足 C1 的假设，包括 $q=2$、非分裂结点和尖点。
C2 得证。

### Step 5. 去掉奇偶符号并与原自治系统共轭

置 $h=\varepsilon c$，定义曲线同构

$$
\sigma_c:W_\varepsilon(c,T)\xrightarrow{\sim}W_1(h,T),
\qquad (u,v)\longmapsto(u,\varepsilon v).
\tag{14}
$$

代入方程且用 $\varepsilon^2=1$ 即得目标方程；$O$ 不变，$P$ 送到 $(0,T)$。
对 (4) 新斜率为 $m_1=\varepsilon m$，故新横坐标不变，新纵坐标乘 $\varepsilon$。
这在稠密开集给 $\sigma_c\theta_c=\theta^{(1)}_h\sigma_c$，
两边是完整曲线态射，遂在整个曲线上成立，奇异点也包括在内。

对原自治参数 $s'=1,t'=T$ 使用 C2，精确阶为 $r'=1$，符号为 $1$。
每个 $h\in\mathbb F_q$ 有完整曲线同构

$$\psi_h:X^{\rm aut}_h\xrightarrow{\sim}W_1(h,T),\qquad
\psi_h\mathcal A_T=\theta^{(1)}_h\psi_h.\tag{15}$$

对每个 $c$ 选 C2 的 $\phi_c$ 并置

$$\beta_c=\psi_{\varepsilon c}^{-1}\sigma_c\phi_c.
\tag{16}$$

这是定义在 $\mathbb F_q$ 上的整个曲线同构，
将原能级 $c$ 送至自治能级 $\varepsilon c$，且等变于准确回返／自治一步。
由于所有合法状态都在 $U=f^{-1}(\mathbb A^1)$，
每个 $\mathbb F_q$-点具有唯一 $c\in\mathbb F_q$；两侧纤维均不交且遍历全部状态。
把有限多个 $\beta_c$ 在有理点集上并合即得 (5)。
四条末端直线上的点没有删除或识别，纤维奇点也保留。
C3 得证。

### Step 6. 保留实际时间的显式悬挂

定义 $H_0=\mathrm{id}$，对 $1\le j\le r$ 置

$$H_j=F_{s^{j-1}t}\circ\cdots\circ F_t.
\tag{17}$$

R 保证这些是完整状态同构；$H_j$ 从初始切片映向第 $j$ 时间切片，$H_r=\mathcal R$。
在 $Q\in U_{s^jt,s}(\mathbb F_q)$ 上定义

$$\Xi(Q)=(j,\beta H_j^{-1}Q).\tag{18}$$

$s$ 精确阶为 $r$ 且 $t\ne0$，故这 $r$ 个时间标签互异。
因此 (18) 是到乘积集合的双射。若 $j<r-1$，则
$H_{j+1}^{-1}F_{s^jt}H_j=\mathrm{id}$；若 $j=r-1$，则
$F_{s^{r-1}t}H_{r-1}=\mathcal R$。结合 (5) 得 $\Xi F\Xi^{-1}=\Sigma$。

从第零切片出发，回到该切片的步数必被 $r$ 整除；
第 $rn$ 步回到原状态等价于 $\mathcal A_T^n z=z$。
自治一条长度恰为 $n$ 的循环，连同全部 $r$ 个时间标签，
在 (6) 下恰构成一条长度 $rn$ 的循环，不分裂成 $r$ 条。
所以 C4 的一个时间轨道结论及无其他周期均成立。

最后，$\mathbb F_q^*$ 是阶 $q-1$ 的循环群且 $r\mid q-1$。
幂映射 $t\mapsto t^r$ 的核恰有 $r$ 个元素，等于 $\langle s\rangle$，像为 $H$。
因此非零时间轨道由 $T\in H$ 一一标记，且每个轨道只求和一次，得到 (7)。
完整状态数校验为

$$
\#U_{t,s}(\mathbb F_q)=(q-1)^2+4q=(q+1)^2,
\quad \#\Omega_{t,s}=r(q+1)^2,
\quad \#\Omega_s=(q-1)(q+1)^2.
\tag{19}
$$

它们来自原环面与四条不交末端仿射线，而不是替代状态集。C1–C4 得证。$\square$

## Consequences and precise limits

对于 $\delta(c,T)\ne0$ 的有限域纤维，(3) 立即给准确周期公式

$$
d_c=\operatorname{ord}_{W_\varepsilon(c,T)(\mathbb F_q)}(0,\varepsilon T),
\qquad \text{全部回归循环长度}=d_c,
\qquad \text{循环数}=\frac{\#W_\varepsilon(c,T)(\mathbb F_q)}{d_c}.
\tag{20}
$$

证明是群中平移作用的陪集分解，每个轨道都是 $Q+\langle P\rangle$。
这条一般椭圆周期／循环数机制已有 JRV 等强先例，不单独计作新意。
奇异处本件给整个曲线上的准确共轭和唯一固定奇点；
完整奇异群参数、分裂型与数目公式须由单独的群律证明接入，不从 (20) 硬套。

C3 只给逐闭纤维曲线同构拼成的有限点集共轭。
未证明原 $k_0(c)$ 泛 torsor 有点、$U_{t,s}$ 与自治曲面全局双有理共轭，
也未证明存在同时随 $c$ 有理变化的 $\beta_c$；不得作这种扩大。
本件不计算各 $a_{T,q}(n)$ 的跨素数闭式或统计极限，不声称一般周期枚举免于点阶计算。

## Non-proof diagnostic

主控直接枚举 R Step1 的原环面加四末端线状态，用完整一步公式组成精确 $r$ 步回返，
与同一域参数 $T=t^r$ 的原自治一步比较完整循环类型。
枚举全部 $s,t\ne0$，域为
$q=2,3,5,7,11,13,17,19,23,29,31$，无拟合参数或可调阈值。
输出：3049 个参数对、2164105 个状态回返比较全部相符；
$q=2$ 的两个循环长度为 $5,4$，覆盖 $(q+1)^2=9$ 个状态。
每个比较先验证回返确为该完整状态集上的置换。
这只是有限范围的转录／反例检查，不证明任意素数域、扩域或本件的曲线同构。
没有生成实验项目、结果文件、编译产物或改变任何既有锁。

## Corrections or missing assumptions

C1 明示实际闭纤维须有光滑 $k_0$-点；该条件仅在 C2 的有限域情形被证明自动成立。
不把代数闭域上的选点句子原封不动移到任意域，也不对任意域删去此条件。

## Open risks

本稿的新独立审查应检查：原域局部点提升、指定 torsor 等变性、最小模型假设、
稠密坐标式在奇异纤维的确切延伸、Weil 界是否循环、自治符号和时间循环计数。
未变基础不是新审查的重开对象；本稿作者判断不替代非作者消费者核查。
普适性结论的先例扣除仍在进行；不得据此预授新意 7.5、论文资格或正文容量 PASS。
本件不启动 Route A/B；纯 qPI 几何与有限置换结构，无 Riemann 行列式或算子声明。
