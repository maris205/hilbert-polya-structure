# Proof Package：原自治 qPI 的 Manin—固定概形接口探查 V1

日期：2026-09-12 UTC。作者：`/root/p31_manin_to_fixed_scheme_probe_v1`。
类型：`AUTHOR_SIDE_BOUNDED_PROBE / STOP_SHALLOW_INTERFACE`；`route_applicability: NOT_APPLICABLE`。
本件不是独立审查、数学接受处置、正式候选或论文。所有旧接受、失败、锁及正文要求保持。

## Claim

检验已接受的原 Manin 多项式 $N_p$ 能否给出原完整 $\operatorname{Fix}(F_T^n)$ 的概形分类，
而非仅给 Jacobian 上必要切触条件。结论是：**原对象到固定概形的结构接口可以闭合，但准确截面零除子仍未计算；这一步本身不足以形成新的长文中心。**

下面实际证明三个有界命题：

1. 原自治完整 $\mathcal U\to\mathbb A^1_h$ 与实际 $W$ 有显式的、随 $h$ 有理变化并延拓至整个有限基的指定动力同构。
2. 好纤维开集 $C^{\rm good}$ 上，作为原 $\mathcal U$ 中的闭概形，
   $\operatorname{Fix}(F_T^n)=\mathcal U\times_C Z(nP)$；纤维厚度为准确交数 $i_n$。
3. 有限节点处完成固定理想是 $a_n(h)(\xi,\eta)$，其中 $\xi\eta=h-h_0$，
   $(a_n)=Z(nP)$ 在基底的局部理想。对于全有限纤维半稳定的时间，得到下述全局结构式 (9)。

这些式子以 $Z(nP)$ 为输入，**不等于显式求出 $Z(nP)$、全部 $i_n$ 或完整异常谱**。
尖点不由节点证明覆盖；非单位原时间不在假设内。

## Status

`PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`。
弱化是由“用 $N_p$ 完成全部固定概形分类”改为“给出以准确截面零除子为输入的结构恒等式，且只在好纤维及节点上证明局部理想”。
下面证明全部声明的有界结构式；完整分类目标仍 `NOT CURRENTLY JUSTIFIED`。
`STOP_SHALLOW_INTERFACE` 指本接口不作为新候选中心继续扩篇，不是宣布原族耗尽或整批目标停止。

## Assumptions and notation

令 $k$ 代数闭、$\operatorname{char}k=p>3$、$T\in k^\times$ 固定，$n\ge1$。
保持原八中心曲面、反典范边界 $D$、完整 $\mathcal U=S\setminus D$ 及四条末端线。
原自治动力和能级为

$$
F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
h=I_1=-x+y+\frac{x}{y}-\frac{T}{x}.
\tag{1}
$$

这些环面公式的完整曲面延拓、$f:\mathcal U\to\mathbb A^1_h$ 的 proper/flat 性、
有限纤维几何整约化、原泛平移非挠性，均消费 [BASE]/[FP] 的已接受接口。
尤其“完整 $\mathcal U$”不是仅取公式无分母的环面。

实际带标记模型是

$$
W:\ v^2+huv-Tv=u^3-Tu^2,\qquad O=[0:1:0],\qquad P=(0,T),
\tag{2}
$$

其好纤维开集为 $C^{\rm good}=\operatorname{Spec}k[h,\delta^{-1}]$，其中
$\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$。
若 $T\ne-27/256$，所有有限坏纤维均为节点，令 $C^{\rm ss}=\mathbb A^1_h$；
若 $T=-27/256$，令 $C^{\rm ss}=\mathbb A^1_h\setminus\{9/8\}$。
这里删去的是节点命题不能处理的唯一尖点能级，不是修改原状态集；完整原状态集仍未分类。

在 $C^{\rm ss}$ 上令 $G=W^{\rm sm}$。下文核定 $G$ 的群结构及其对整个 $W$ 的作用。
定义

$$
D_n=Z(nP):=(nP)^{-1}(O)\subset C^{\rm ss},\qquad
\mathcal I_{D_n}=(nP)^*\mathcal I_O.
\tag{3}
$$

$P$ 泛非挠，所以 $nP$ 不恒等于 $O$；$D_n$ 是有限有效 Cartier 除子，允许为空。
在 $R=k[[\tau]]$、$\tau=h-h_0$ 上写 $\mathcal I_{D_n}R=(\tau^{i_n(h_0)})$，
其中 $i_n=0$ 表示没有截面交点。交点存在时 $i_n=(nP.O)_{h_0}\ge1$。
$\tau$ 是局部基底参数，不是原时间 $T$；本件从未允许 $T=0$。

## Proof strategy and dependency map

1. 直接原坐标计算给指定 $+P$ 共轭；已接受正则最小模型加唯一性延拓到全部有限原纤维。
2. torsor 的作用图同构给好纤维 equalizer 恒等式；没有从几何点集合反推概形。
3. 半稳定整亏格一族加光滑零截面给广义椭圆作用；节点正规平滑化和其乘法切表示给完整固定理想。
4. 完成忠实平坦性将局部理想粘为全局结构式；最后只消费 [MANIN] 真正证明的必要条件。

新外部数学工具使用本人打开的 [Stacks 55.10][MIN]、[Stacks 53.21.1][NODE]、
[Conrad §2.1][CON]。这些是标准结构输入，不计作原 qPI 新理论。
不重新证明 Ulmer–Voloch 的 $\mu$ 公式，也不借其原全局半稳定命题扩大 [MANIN] 的接受范围。

## Proof

### Step 1. 实际原自治曲面上的显式带标记同构

在原环面取

$$
\phi(x,y)=(u,v)=\left(\frac{T}{y},\frac{Tx(y-1)}{y^2}\right),\qquad
x=\frac{Tu}{T-hu-v},\quad y=\frac{T}{u}.
\tag{4}
$$

这是本件给出的原有理坐标，不是把 [FP] 的有限域点集拼合升级为曲面共轭。
由 (1) 直接计算

$$
v+hu-T=-\frac{T^2}{xy},\qquad
v(v+hu-T)=\frac{T^3(1-y)}{y^3}=u^3-Tu^2.
$$

故 (4) 落在 (2)；其逆式代入还原 $x,y$，各分母在函数域非零。
于是它是原基 $k(h)$ 上光滑泛曲线的同构，也给整个曲面函数域的有理同构。
要核定平移符号，令 $m=(v-T)/u=x-x/y-y$，则 $m+h=-T/x$。
已接受的三次加 $P$ 公式给

$$
\tau_P(u,v)=\bigl(m^2+hm+T-u,-(m+h)(m^2+hm+T-u)\bigr)
=\left(\frac{Ty}{x},\frac{T^2y}{x^2}\right)=\phi F_T(x,y).
\tag{5}
$$

所以指定点是实际 $P=(0,T)$，不是 $-P$ 或未知自同构像。
辅助的精确符号化检查还逐项验证了能级不变、方程、两个逆式及 (5) 两坐标；
证明由上述恒等式承担，计算只排除转录错误，没有有限样本外推。

对每个有限 $h_0$，原 $\mathcal U$ 与 $W$ 在 $k[h]_{(h-h_0)}$ 上均为最小正则 proper 模型。
这些假设已经在 [C] Step 1 核定：原曲面光滑；$W$ 的相对奇点满足 $uv\ne0$，
故总方程的 $h$ 偏导非零；特殊纤维唯一整约化分量自交为零，因而没有可缩竖直 $(-1)$ 曲线。
泛曲线是光滑射影几何整亏格一曲线。[MIN] 的最小模型唯一性将 (4) 及其逆唯一延拓于每个该 DVR。
这也可由 [C] 的 henselian 模型论证取得；[C] 的 (10) 本身已是整个局部模型同构，不只是闭纤维。

这些局部延拓与同一个函数域同构相容。因模型有限呈示，DVR 上的态射及逆可向某个基底开邻域展开；
也可用无不定点的判据逐点检验这个有理映射。重叠上的态射在稠密泛纤维相等，目标分离，故相等并粘合。
因此 (4) 给

$$
\phi:\mathcal U\xrightarrow{\sim}W\quad\text{over }\mathbb A^1_h,
\qquad \phi F_T\phi^{-1}=\theta_P.
\tag{6}
$$

其中右侧是泛 $+P$ 的完整延拓；(5) 与分离性使动力等式也延拓。
四条末端线及奇点均在这个模型同构中，未删去或拼合成替代状态。
源 [F] Step 7 还明示原第一末端 chart 的能级限制 $h=1-b$，
因而自治情形确有全基截面；一般 $r$ 的泛 torsor 未平凡边界不能直接套作自治 $r=1$ 的阻断。
本证明不对一般 $r$ 声称这样的原曲面全局共轭。

### Step 2. 好纤维的 equalizer 是准确拉回

先给一般短引理。若 $X\to C$ 是群概形 $E\to C$ 的 torsor，$Q\in E(C)$，则

$$
\operatorname{Fix}(\tau_Q:X\to X)=X\times_C Z(Q)
\tag{7}
$$

作为 $X$ 内闭概形成立。torsor 条件使 $E\times_C X\to X\times_C X$，
$(g,x)\mapsto(gx,x)$，为同构；对角线对应零截面乘 $X$。
把此对应沿 $(Q,x)$ 拉回正得到 (7)。这个证明保留所有测试概形的幂零元，不要求 $n$ 在 $k$ 可逆。

在 $C^{\rm good}$ 上，(6) 直接供应实际原 $E$-torsor 作用与指定平移，故可取 $Q=nP$。
即使不使用新显式 (4)，[C] 的每个 henselian 等变模型同构也已足以逐局部检查同一理想恒等式；
所以原好纤维相对识别不是一个仍待新定理解决的缺口。
在 $h_0$ 处若 $i_n>0$，任一原纤维点的完成局部固定理想为 $(\tau^{i_n})$；
因此整个纤维统一具有基向厚度 $i_n$，不是各原状态可任意不同的厚度。

### Step 3. 半稳定整纤维确有相对作用

在 $C^{\rm ss}$ 上，$W$ 是 proper/flat 的半稳定亏格一族，每个几何纤维整且有光滑截面 $O$。
节点为 $1$-gon，光滑纤维的相对 dualizing sheaf 平凡；平面三次的 adjunction 也给相同的相对结论。
[CON] Remark 2.1.13 记述 Deligne–Rapoport 的存在唯一性定理：这些条件给唯一的广义椭圆结构，
其 smooth locus $G$ 是群概形并作用于完整 $W$。该源 Definition 2.1.4 明确作用定义域为 $G\times_C W$，不只 $G\times_C G$。
本件本人读取了该陈述及其周边定义；没有声称读完它所引 DR 原证明。

$P$ 在全部有限纤维相对光滑，因为 (2) 的 $v$ 偏导在 $P$ 为 $T\ne0$。
所以 $nP$ 是 $G$ 的实际截面。广义群作用给的平移与 (6) 的 $\theta_P$ 在泛纤维相等；
稠密性及分离性使两者在整个 $C^{\rm ss}$ 模型相等。这一步提供节点全形式计算所需的相对作用，
没有以闭纤维的群元素 $\kappa$ 代替相邻基方向的作用。

### Step 4. 节点处完整固定理想

固定一个有限节点 $q_0$，设其能级为 $h_0$。由 [NODE]，完成局部模型为
$R[[\xi,\eta]]/(\xi\eta-b(\tau))$。
总空间正则、特殊纤维为节点，强制 $b(\tau)$ 的阶为一：阶至少二会使总关系无一次项，
完成局部环的嵌入维数为三而维数为二，矛盾。
把 $\eta$ 乘适当基底单位后可取

$$
A=R[[\xi,\eta]]/(\xi\eta-\tau)\simeq k[[\xi,\eta]],\qquad
\mathfrak m=(\xi,\eta).
$$

先设 $(nP)_{h_0}\ne O$。节点特殊纤维的群是 $\mathbb G_m$，平移在两个分支的切表示是
$\operatorname{diag}(\kappa_n,\kappa_n^{-1})$，其中 $\kappa_n\ne1$。
这是节点正规化乘法群的作用，不调用“全局挠截面”的线性化定理。
完成自同构 $\sigma=\theta_{nP}^*$ 保持 $\xi\eta=\tau$ 且保留两个分支；
在 UFD $A$ 中必有 $\sigma(\xi)=\xi U$、$\sigma(\eta)=\eta U^{-1}$，$U$ 为单位。
其在节点的值是 $\kappa_n$ 或其逆，故 $U-1$ 为单位。
因此固定理想恰为 $\mathfrak m$；没有光滑固定点但有一个约化固定节点。

再设 $(nP)_{h_0}=O$。在 $G$ 的零截面形式邻域选参数 $z$，把 $nP$ 写成
$z=a_n(\tau)\in\tau R\setminus\{0\}$；按定义 $(a_n)=(\tau^{i_n})$。
在零截面和节点附近完成广义群作用。其作用环为
$R[[z,\xi,\eta]]/(\xi\eta-\tau)\simeq k[[z,\xi,\eta]]$。
它是 UFD，作用保持 $\xi\eta$，且模 $z$ 为恒等，故

$$
\alpha^*(\xi)=\xi U(z,\xi,\eta),\qquad
\alpha^*(\eta)=\eta U(z,\xi,\eta)^{-1},\qquad U(0,\xi,\eta)=1.
$$

分支不能交换：模 $z$ 是恒等，而 $\xi,\eta$ 是不同素因子。
特殊节点群的参数 $\chi-1$ 与 $z$ 相差非零线性系数；其分支作用为 $\chi$ 及 $\chi^{-1}$。
所以 $\partial U/\partial z$ 在 $(0,0,0)$ 非零。于是
$U-1=zV$，其中 $V$ 是单位。令 $z=a_n(\tau)$ 后，$V$ 仍为单位；
$U^{-1}-1=-U^{-1}(U-1)$ 给两个生成元共享完全相同的标量因子。
由两个坐标差生成的完整 equalizer 理想因此为

$$
\boxed{\widehat{\mathcal I}_{\operatorname{Fix}(F_T^n),q_0}
=a_n(\tau)(\xi,\eta)=\tau^{i_n(h_0)}(\xi,\eta).}
\tag{8}
$$

把无交点时的 $a_n$ 取为单位，(8) 也包含第一种情形。
本证明得到的是理想的准确相等；它没有声称能够选择使整个自同构准确写成
$\xi\mapsto b_n(\tau)\xi,\eta\mapsto b_n(\tau)^{-1}\eta$ 的 Tate 坐标。
$U$ 可以依赖状态变量；其与截面参数相差的单位已足以决定固定理想。
该推导对每个 $n$ 有效，包括 $p\mid n$；后者的困难留在 $a_n$ 的准确阶，不被这句话消除。

若 $i_n\ge1$，这个固定概形不是只有一条厚度 $i_n$ 的 Cartier 纤维。
由 $\tau=\xi\eta$ 及整域性有准确短正合列

$$
0\longrightarrow k\longrightarrow A/\bigl(\tau^{i_n}\mathfrak m\bigr)
\longrightarrow A/(\tau^{i_n})\longrightarrow0,
$$

因为核是 $(\tau^{i_n})/(\tau^{i_n}\mathfrak m)\simeq k$。
所以节点另有长度一的嵌入部分；不能把此非 Artin 局部商的总长度称为一。
这是 (8) 的初等理想后果，不是新增算术厚度公式。

### Step 5. 全半稳定有限原模型的结构表达

记 $\mathcal I_{\operatorname{Sing}(f)}$ 为原相对非光滑概形的理想，
即 $\operatorname{Fitt}_1(\Omega^1_{\mathcal U/C})$：光滑点处为单位理想，节点完成处为 $(\xi,\eta)$。
在 $C^{\rm ss}$ 上，Step 2 同样应用于坏纤维的光滑点群，给固定理想 $f^*\mathcal I_{D_n}$；
Step 4 给所有节点的理想。Noetherian 局部环完成忠实平坦，故这些局部等式推出

$$
\boxed{\mathcal I_{\operatorname{Fix}(F_T^n)}
=\bigl(f^{-1}\mathcal I_{D_n}\cdot\mathcal O_{\mathcal U}\bigr)
\mathcal I_{\operatorname{Sing}(f)}\quad\text{on }f^{-1}(C^{\rm ss}).}
\tag{9}
$$

若 $T\ne-27/256$，此式覆盖完整原 $\mathcal U$ 的全部有限能级；若时间为例外值，式中不包括尖点能级。
(9) 是原固定概形对截面交除子的精确消费者，不是 $D_n$ 的准确求值算法或全部异常谱。
从 (7) 到 (9) 的论证只用了普通 torsor、广义椭圆作用和节点局部代数，必须整体扣作标准机制。

### Step 6. 新 Manin 输入准确能消费到哪里

[MANIN] 对所有 $T\ne0$ 已证明 $N_p\ne0$、$\deg N_p\le2p$；
对 $p\nmid n$、有限好能级，其结论准确是

$$
i_n(h_0)>1\ \Longrightarrow\ N_p(h_0)=0.
\tag{10}
$$

借 (7)，(10) 可以合法改写为原固定概形的陈述：当 $p\nmid n$ 且
$\delta(h_0)N_p(h_0)\ne0$ 时，原固定概形在该纤维的形式邻域内，
不是空就是由理想 $(\tau)$ 定义的约化完整纤维；这里不是只把固定概形拉回剩余纤维后检验约化性。
出现厚度大于一的好纤维最多位于 $2p$ 个必要候选能级。
空／非空仍需 $nP(h_0)=O$，候选点的准确厚度仍需 $i_n$。
$N_p$ 的根重数没有被证明等于 $i_n-1$，也没有给出 $N_p=0$ 的充分切触意义。
坏节点处 (8) 中的标量 $a_n$ 没有由 (10) 算出；$p\mid n$ 时也不能引用 (10)。

## Corrections or missing assumptions

- **原相对接口。** 一般 $r$ 的有限域点集共轭确实不足；但本件只取 $r=1$，已直接给 (4)–(6)。
  另且旧 [C] 的 henselian 模型同构足以消费局部概形，不能继续把“原模型识别全缺”当研究成果。
- **节点、重根与参数。** $T\ne-27/256$ 时有限坏点为节点且原总空间正则，故平滑化参数阶为一。
  不能把任意 $\delta$ 重根自动解释成同样的 $\xi\eta=\tau$；例外时间有尖点。
  若另作真正底变换 $\tau=\rho^e$，已证明的等式可以随该同一模型及作用拉回，
  但这时局部方程为 $\xi\eta=\rho^e$，交数及参数须明确重标，不能沿用“原正则总空间”的 UFD 论证。
- **原非单位时间。** $T=0$ 时 (4) 的逆、$P$ 的相对光滑性和原 $F_T$ 的同构性均失去本证明的前提；
  原非单位时间接受包延续曲面与层，不提供塌缩映射的这个平移概形接口。
- **尖点。** $T=-27/256,h=9/8$ 的加法群元素和闭点周期已有接受结果，
  但尖点不是广义椭圆意义下的节点 $1$-gon，完成式也不是 $\xi\eta=\tau$。
  尤其 $p$ 次迭代的野厚度不从节点非零线性系数推导。本件没有计算尖点全形式固定理想。
- **无穷远。** 原 $\mathcal U$ 已去掉无穷边界；(9) 不分类紧化曲面上 $D$ 的固定理想。
  [MANIN] 将无穷远留在候选集合中，并不向本件自动供应边界交数。

## Open risks and nonstandard increment

对本件写出的有界证明，仍须由 fresh 非作者核对后才可称数学接受；本作者报告不预授接受。
关键可审点是：原 (4) 的标记符号、全基最小模型延拓、广义作用的准确假设、
形式作用中 $U-1=z\cdot\text{unit}$ 的两个方向，以及固定理想与仅线性化的区别。

真实新书面内容是原自治坐标 (4) 与其全基说明，以及将标准节点局部代数明确接至完整原 $\mathcal U$。
其构造来自旧谱三次代换／取负及已用过的最小模型方法；(7)–(9) 是标准群作用消费者。
即便全部数学核查通过，也不能把它与 $N_p$ 的必要条件相加便宣布得到足够新的独立长文中心。
本轮因此判断 `STOP_SHALLOW_INTERFACE`，不要求扩篇、试写测页、补票或建立 P31 项目。

仍未供应的最小非形式数学对象是实际 $D_n$，例如在一个允许的好候选点上确定实际截面阶 $d$ 后，
算出 $z(dP)$ 的首个非零基向系数并证明其在参数／特征上的准确量词；
坏节点则需原乘法特化阶及对应 $a_d$，尖点另需不同的完整局部作用。
这个对象不是 $N_p$ 的零集改名，也不是把 $i_n$ 留作输入后再求和。
本件不预设这些更强断言成立、有新意或足以支撑长文，也不启动旧 N03/N10 或能量盘。

## Prior-art boundary and actual reading

本人 FULL 阅读 proof-writer 技能及下表四件 FULL 输入；其余仅列本人实际读段，不继承主控或 helper 的阅读为本人 FULL。
proof-writer 使本件把“结构恒等式”与“标量除子分类”分开，并显式保留尖点／非单位时间／特征 $p$ 的未供义务。

| 输入 | 本人实读范围 | 当前 SHA-256 |
|---|---|---|
| [MANIN] | FULL 1–148 | `05a99ecd5cfd72315b8c4e0fc740062687824d4dcd8dc7cdcdb81f5f87bbb8fd` |
| [BASE] | FULL 1–121 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [FP] | FULL 1–167 | `9a70cd2dd9656689dfeb26a6890e35ab1bf5dd10a5eab28a38306578b2767fce` |
| [C] | FULL 1–372 | `734b3f218bc3f16c8565ebb688d82c66252367d28e3e6a0e38f3aa571094c72a` |
| [F] | 350–405；含 Step 7 原积分及四末端表 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` |
| [R] | 295–345；含 Step 6 相对光滑平移证明 | `9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c` |

本人打开并阅读 [MIN] Lemmas 55.10.1–2 陈述及证明；[NODE] Lemma 53.21.1 陈述、第一证明及第二证明草图；
[CON] 印刷 pp.4–6 的广义椭圆定义／标准多边形作用及 Remark 2.1.13，
另定向阅读 §2.5 pp.16–18 的形式环带构造、(2.5.3) 与周边说明。
Tate 原源全文没有读完；本件 (8) 不依赖未读的全曲线 Tate 一致化或全形式对角化。
另打开 Conrad 的 `genpaper.pdf`，只用于定位形式 Tate 背景，没有据此增添证明依赖。

主控提示的 Miranda–Persson 1989 [MP]，本人打开合法 Numdam 原文并读印刷 p.252 的 §2 设置、Lemma 2.1 及其 proof 指向。
该条是**全局挠截面**的节点固定点／线性化结果，证明转引其 [M-P1]；
本件没有读取 [M-P1]，也不把 Lemma 2.1 当作非挠截面单个特化的全形式理想定理。
它仍明确要求扣除半稳定节点乘法切表示这一旧机制。
主控另外提示 Duistermaat 2010 §7.4 的带重数周期纤维；本人只打开官方 ETH 目录入口元数据，后续取段超时，
没有读到该书 §7.4 正文，因此不将其当作本件定理依赖或完整先例比对。
这里没有以搜索摘要、目录标题或转引替代定理证明。

只读 helper `original_r1_relative_action_check` 给出原自治坐标和旧局部模型定位；
本作者本人随后读取上述必要原段并逐式重证 (4)–(5)。所有 helper 贡献归作者侧，不是独立审查票。

本件唯一新增此文件；未改任何旧稿、索引、锁、失败或接受处置，未建立 P31 项目，未编译／投稿／上传／发信。
终态 SHA 在交付时单独报告，文件本身不自载递归哈希。

[MANIN]: PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md
[BASE]: PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
[FP]: PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md
[C]: PAPER30_QPI_CLOSED_FIBRE_RETURN_CONJUGACY_ENTRY_V1_20260908.md
[F]: PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md
[R]: PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md
[MIN]: https://stacks.math.columbia.edu/tag/0C9Y
[NODE]: https://stacks.math.columbia.edu/tag/0CBY
[CON]: https://math.stanford.edu/~conrad/papers/kmpaper.pdf
[MP]: https://www.numdam.org/article/CM_1989__72_3_249_0.pdf
