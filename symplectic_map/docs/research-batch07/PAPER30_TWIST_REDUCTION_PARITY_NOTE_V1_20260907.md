# 双谐波共振：约化规范、奇偶过滤与真实轨道接口 V1

日期：2026-09-07。身份：主控作者补充证明，不是非作者终审或候选票。

## Claim

固定互素整数 $0<r<s$、$s\ge3$，令 $\omega=2\pi r/s$，
$V(q)=\epsilon\cos q+\lambda\epsilon^2\cos2q$。
在 $q_j=\theta+\omega j+u_j$、$u_{j+s}=u_j$、$\sum_j u_j=0$ 下，
使用作用量

$$\mathcal A=\sum_{j=0}^{s-1}
\left\{\frac12(q_{j+1}-q_j)^2-V(q_j)\right\}.$$

本补充说明实际解析约化的定义、比原 $O(\epsilon^{s+1})$ 更精确的相位余项，
以及约化临界点和真实 primitive 周期之间的对应；不宣称全分母根分类。

## Status

以下接口命题：`PROVABLE AS STATED`。
原问题中全分母根的实性、重数和简单消失点之后的实际首分裂阶：
`NOT CURRENTLY JUSTIFIED`，不能用本补充代替。

## Assumptions and notation

$r,s$ 固定，$\lambda$ 在任意预先固定的紧实区间 $J$ 中。
所有小参数邻域和余项常数允许依赖 $r,s,J$；不声称分母一致性。
令 $X=\{u\in\mathbb R^s:\sum u_j=0\}$，$\Pi$ 为向 $X$ 的正交投影，
$Lu_j=2u_j-u_{j-1}-u_{j+1}$。
$W(\theta,\epsilon,\lambda)$ 为消去 $X$ 变量后的作用量，
$\overline W$ 为其对 $\theta\in[0,2\pi]$ 的平均。

## Proof strategy and dependency map

零均值 Hessian 的可逆性给出真实解析消元；循环移位、反射及
$(\theta,\epsilon)\mapsto(\theta+\pi,-\epsilon)$ 控制 Fourier 支撑。
次数／频率过滤加强余项，链式法则把约化临界条件还原为实际周期方程。
最后用循环轨道上的旋转数排除较短周期。

## Proof

### Step 1. 真实解析约化

由于 $\sum(u_{j+1}-u_j)=0$，动力学无关的交叉动能项消失，
动能等于 $s\omega^2/2+\langle u,Lu\rangle/2$。
限制在 $X$ 的驻值方程为

$$Lu+\Pi\{\epsilon\sin(\theta+\omega j+u_j)
+2\lambda\epsilon^2\sin(2\theta+2\omega j+2u_j)\}=0.\tag{1}$$

$L$ 在 $X$ 的特征值为 $4\sin^2(\pi k/s)>0$，$1\le k<s$。
解析隐函数定理给出从 $u=0,\epsilon=0$ 出发的唯一小解。
在紧参数集 $[0,2\pi]\times J$ 上，由同一个可逆线性化和有限覆盖可选共同的
$\epsilon$ 邻域；邻域交叠处的唯一性使这些局部解一致。
因此 $W$ 是实际解析函数，而不是仅有形式展开的记号。

### Step 2. 约化势的全部精确对称

将 $u_j$ 循环平移为 $u_{j+1}$，对应相位 $\theta+\omega$，并保持作用量。
由于 $\gcd(r,s)=1$ 及 $2\pi$ 周期，得到 $W(\theta+2\pi/s)=W(\theta)$。
反射 $u_j\mapsto-u_{-j}$、$\theta\mapsto-\theta$ 保持旋转数和作用量，
故 $W(-\theta)=W(\theta)$。这里的指标按周期延拓处理，
$q_j$ 的提升仍满足 $q_{j+s}=q_j+2\pi r$。

变换 $\theta\mapsto\theta+\pi$、$\epsilon\mapsto-\epsilon$ 不改变势函数
在配置上的取值或驻值方程，动能也不变。因此

$$W(\theta+\pi,-\epsilon,\lambda)=W(\theta,\epsilon,\lambda).\tag{2}$$

所有这些等式都由唯一小消元解保证，不要求原始周期族事先存在。

### Step 3. 加权过滤和两阶余项

在 $(1)$ 的递归展开中，基本势／力项分别有 $\epsilon$ 次数与 Fourier 频率
$(1,\pm1)$、$(2,\pm2)$。乘法将两者相加，$L^{-1}\Pi$ 不提高频率。
归纳得到每个 $\epsilon^k$ 系数的频率绝对值不超过 $k$。
动能中的系数是两个 $u$ 系数的乘积，因此代入作用量后仍有同一界。

Step 2 迫使非恒定频率属于 $s\mathbb Z$，且只能出现余弦。
所以 $k<s$ 时没有非恒定项，$k=s$ 时只有 $\cos(s\theta)$。
由 $(2)$，频率为 $m$ 的项还必须满足 $k\equiv m\pmod2$。
在 $k=s+1$ 时，$2s>s+1$，唯一可能的非恒定频率仍为 $s$，
但它违反奇偶限制。故对任意固定有限导数阶 $a\ge0$，

$$W-\overline W
=\epsilon^s C_{r,s}(\lambda)\cos(s\theta)
+O_{C^a(\theta)}(\epsilon^{s+2}),\tag{3}$$

余项对 $\lambda\in J$ 一致。任意固定的 $\lambda$ 导数也可纳入同一估计，
因为解析消元对 $\lambda$ 同时成立。
这只排除 $s+1$ 阶，**不证明** $C(\lambda_*)=0$ 后 $s+2$ 阶必非零。

### Step 4. 与实际周期的对应

在约化点，完整作用量梯度垂直于 $X$，故为某个常数向量 $c\mathbf1$。
又 $\sum_j\partial_\theta u_j=0$，链式法则给出 $W'=sc$。
因此 $W'=0$ 当且仅当完整梯度为零，即

$$q_{j+1}-2q_j+q_{j-1}
=\epsilon\sin q_j+2\lambda\epsilon^2\sin2q_j.$$

设 $p_j=q_j-q_{j-1}$，便得到题设映射的真实周期提升，满足
$(q_{j+s},p_{j+s})=(q_j+2\pi r,p_j)$。
若圆柱状态的最小周期为 $m$，则 $m\mid s$，并有某个整数 $k$ 使
$q_{j+m}-q_j=2\pi k$。从而 $r=(s/m)k$；互素性迫使 $m=s$。
所以约化临界点不暗含非 primitive 的短周期污染。

若固定 $\lambda$ 满足 $C_{r,s}(\lambda)\ne0$，则对充分小的
$0<|\epsilon|$，$(3)$ 在 $C^2$ 中保证每个相位基本区间
$[0,2\pi/s)$ 恰有两个临界点，且均非退化：
在 $\sin(s\theta)$ 的两个零点外用一致非零下界排除临界点；
在各零点小邻域内，二阶导数的固定符号保证唯一零点，
零点存在由邻域两端的一阶导数异号得到。
相位平移 $\omega$ 恰遍历同一轨道的 $s$ 个根，因此它们给出两个实际周期。
恰好两个的断言仅限上述小 $u$ 约化分支，不排除远处的其他周期；
$\epsilon=0$ 则保留整圈退化周期，不能包含在该非退化断言内。
这是约化的标准非退化接口，不是本题全根分类的新机制。$\square$

## Corrections or missing assumptions

原 $O(\epsilon^{s+1})$ 写法正确但不尖锐；$(3)$ 是同一规范下的加强，
不改写旧记录、不假称旧稿错误。作用量不除以 $s$；若另改用平均作用量，
整个 $C$ 也要除以 $s$，不可混用。
非作者核查时将末段适用范围显式补写为 $0<|\epsilon|$ 及局部小 $u$ 分支，
没有改动 $(1)$–$(3)$ 或实际 primitive 对应。

## Open risks

首项 $C$ 的准确递推、次数和符号见
[并行作者诊断](PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.md)。
全实根、简单性和固定简单消失点后的首非恒定项没有在本补充中证明。
允许把 $\lambda$ 改成依赖 $\epsilon$ 的调谐曲线也不能回答原固定参数问题。
没有正式候选评价、容量估计、PDF或新Paper30项目。
