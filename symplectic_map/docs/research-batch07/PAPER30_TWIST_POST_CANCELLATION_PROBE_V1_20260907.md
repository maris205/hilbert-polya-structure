# Proof Package：固定参数首项消失后的完整 Fourier 次项 V1

日期：2026-09-07。角色：独立作者次项推导，不是旧稿审核或候选评价。

## Claim

固定映射和未取平均的 SUM action：

$$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p',$$
$$\mathcal A(q)=\sum_{j=0}^{s-1}\left\{\frac12(q_{j+1}-q_j)^2
-\epsilon\cos q_j-\lambda\epsilon^2\cos2q_j\right\}.$$

固定互素 $0<r<s$、$s\ge3$，沿
$q_j=\theta+2\pi rj/s+u_j$、$\sum_j u_j=0$ 的小解消元。
本稿给出含正负 Fourier 模式的有限三角递推，严格确定
$\epsilon^{s+2}\cos(s\theta)$ 的系数 $Q_{r,s}(\lambda)$。
并在原样固定的首项零点，精确解决 $s=3$ 与 $s=4$ 的下一非恒定项及局部轨道几何。

## Status

完整递推、下面精确有限分母式及其局部动力结论：`PROVABLE AS STATED`。

“任意互素 $r,s$ 的每个简单实零点 $\lambda_*$ 均满足
$Q_{r,s}(\lambda_*)\ne0$”：`NOT CURRENTLY JUSTIFIED`，继续 OPEN。
没有把有限实例、一般性预期或参数调谐曲线当成全分母证明。

关键结果：

$$Q_{1,3}(\lambda)=\frac{\lambda^2}{2}-\frac\lambda8+\frac1{384},
\qquad Q_{1,3}(1/24)=-\frac1{576}\ne0.$$

因此固定 $\lambda=1/24$ 时真正的首次非恒定项为
$-\epsilon^5\cos(3\theta)/576$。
这不是只找到一个“下一可能阶”：系数已严格非零。

## Assumptions and notation

- $r,s$ 固定，$\lambda$ 位于固定紧集；所有解析余项允许依赖该数据。
- 采用已经证明的[实际解析约化及精确对称](PAPER30_TWIST_REDUCTION_PARITY_NOTE_V1_20260907.md)，
  不重证旧消元／奇偶结论。
- 下文所有消失点结论的 $\lambda=\lambda_*$ 都是常数，不随 $\epsilon$ 变化。
- $\omega=2\pi r/s$，$x=\theta+\omega j$，$z=e^{ix}$，$v=iu$。
- $D_m=4\sin^2(\pi rm/s)$；当 $s\nmid m$ 时 $D_m>0$。
  当 $s\mid m$ 时执行零均值投影，绝不除以 $D_m=0$。
- $[\epsilon^n z^m]$ 是双变量形式系数；所有固定阶运算是有限 Laurent 多项式运算。

## Proof strategy and dependency map

1. 实际解析消元的 Taylor 系数满足完整投影方程。
2. 以 $v=iu$ 同时保留两种正弦的正、负指数，逐阶反演非共振模式。
3. 由约化作用量导数提取共振模式，并用直接代入 SUM action 作精确代数交叉核算。
4. 固定零点处的非零 $Q$ 与已有解析余项给出真实局部周期。
5. 周期 Hessian 的 Schur 补及离散 Hill 恒等式区分双曲与线性椭圆轨道。

## Proof

### Step 1. 完整 Fourier 三角递推

写

$$v(\epsilon,z)=\sum_{n\ge1}\epsilon^n\sum_{m\in\mathbb Z}v_{n,m}z^m,
\qquad E^{(a)}_{n,m}=[\epsilon^nz^m]e^{av},\quad a\in\{1,-1,2,-2\}.$$

初值为 $E^{(a)}_{0,m}=\mathbf1_{m=0}$，负阶系数为零。
循环协变性使相位频率 $m$ 的指标向量为 $e^{im\omega j}$；
因此零均值条件恰给出 $v_{n,m}=0$ 当 $s\mid m$。
将原驻值方程乘以 $i$，完整的力为

$$G(\epsilon,z)=\frac\epsilon2\left(ze^v-z^{-1}e^{-v}\right)
+\lambda\epsilon^2\left(z^2e^{2v}-z^{-2}e^{-2v}\right).\tag{1}$$

于是依次计算

$$G_{n,m}=\frac12\left(E^{(1)}_{n-1,m-1}-E^{(-1)}_{n-1,m+1}\right)
+\lambda\left(E^{(2)}_{n-2,m-2}-E^{(-2)}_{n-2,m+2}\right),\tag{2}$$

$$v_{n,m}=\begin{cases}-G_{n,m}/D_m,&s\nmid m,\\0,&s\mid m.\end{cases}\tag{3}$$

取得第 $n$ 阶 $v$ 后，用指数导数恒等式完成第 $n$ 阶指数系数：

$$E^{(a)}_{n,m}=\frac an\sum_{k=1}^n k\sum_{\ell\in\mathbb Z}
v_{k,\ell}E^{(a)}_{n-k,m-\ell}.\tag{4}$$

式 (2)只涉及小于 $n$ 阶的 $v$，故 (2)–(4)是真正三角递推。
第 $n$ 阶只需 $|m|\le n$、$m\equiv n\pmod2$；不存在无限模式截断误差。
实际解析消元的唯一 Taylor 系数满足同一递推，因此这些形式系数就是实际系数。
计算 $Q$ 只需取得 $v$ 至 $n=s+1$，再计算 $G_{s+2,s}$。

尤其保留 $E^{(-1)}$ 与 $E^{(-2)}$ 不是可选项。
首项正频对角法只计算 $n=m$；这里 $n-m=2$，不能把它复用为完整次项法。

### Step 2. 作用量系数和一般的可验证次项

记 $B_{n,\ell}$ 为 $\epsilon^n\cos(\ell s\theta)$ 在 $W$ 中的系数。
约化链式法则给出 $iW'=\sum_j G(\epsilon,e^{i(\theta+\omega j)})$。
右边频率 $\ell s$ 的系数为 $sG_{n,\ell s}$，左边为
$-\ell s B_{n,\ell}/2$。故

$$B_{n,\ell}=-\frac2\ell G_{n,\ell s},\qquad
C_{r,s}=-2G_{s,s},\qquad \boxed{Q_{r,s}=-2G_{s+2,s}}.\tag{5}$$

此公式维持 SUM action 规范，没有额外除以 $s$。
所有 $D_m$ 与 $\lambda$ 无关，递推有限，因此 $Q$ 是实系数多项式。
还可得次数上界

$$\deg Q_{r,s}\le\left\lfloor\frac{s+1}{2}\right\rfloor.\tag{6}$$

证明：完全展开递推时，每个基本力节点具有 $(n,m)$ 标签
$(1,\pm1)$ 或 $(2,\pm2)$；第二类另贡献一个 $\lambda$。
总阶 $s+2$、总频率 $s$ 的差为 $2$，故恰有一个 $(1,-1)$ 节点，
无 $(2,-2)$ 节点，其余节点频率均为正。
余下正节点总权重 $s+1$，最多含 $\lfloor(s+1)/2\rfloor$ 个第二谐波节点。
投影可以删除贡献，但不会提高该上界。这个计数不证明系数无抵消。

由既有频率界和奇偶性，$s\ge3$ 时 $s+2<2s$，并且

$$W-\overline W=\epsilon^sC_{r,s}(\lambda)\cos(s\theta)
+\epsilon^{s+2}Q_{r,s}(\lambda)\cos(s\theta)
+O_{C^a}(\epsilon^{\min(s+4,2s)}).\tag{7}$$

特别注意 $s=3$ 的余项是 $O_{C^a}(\epsilon^6)$，
因为 $\epsilon^6\cos(6\theta)$ 已被对称性允许；不能误写成 $O(\epsilon^7)$。

### Step 3. 三周期唯一零点：完整精确展开

对 $(r,s)=(1,3)$，所有非共振 $D_m=3$。由 (2)–(4)，
记 $a_{n,m}=v_{n,m}$、只在此表列正 $m$，负模式严格为 $v_{n,-m}=-v_{n,m}$：

| $n$ | 正模式的非零系数 |
| --- | --- |
| $1$ | $v_{1,1}=-1/6$ |
| $2$ | $v_{2,2}=1/36-\lambda/3$ |
| $3$ | $v_{3,1}=1/432-\lambda/18$ |
| $4$ | $v_{4,2}=7\lambda/108-17/7776$；$v_{4,4}=2\lambda^2/9-5\lambda/108+7/7776$ |

将这张有限表代回 (1)即可逐项核算

$$C_{1,3}=\lambda-\frac1{24},\qquad
Q_{1,3}=\frac{\lambda^2}{2}-\frac\lambda8+\frac1{384}.\tag{8}$$

固定 $\lambda_*=1/24$ 时 $C'=1$ 且 $Q=-1/576$。
因此由实际解析余项，

$$W(\theta,\epsilon,1/24)-\overline W
=-\frac{\epsilon^5}{576}\cos(3\theta)+O_{C^a}(\epsilon^6).\tag{9}$$

未改变 $\lambda$ 的含义，也未用拟合数值推断五阶幂。
$r=2$ 的各 $D_m$ 与 $r=1$ 相同，故同一系数结论覆盖另一个三分母互素代表。

### Step 4. 四周期两个零点

对 $(r,s)=(1,4)$，按 $m\bmod4$ 的非共振分母依次为 $2,4,2$。
完整递推给出

$$C_{1,4}=\lambda^2-\frac34\lambda+\frac5{192},\qquad
Q_{1,4}=-\frac32\lambda^2+\frac14\lambda-\frac{11}{1920}.\tag{10}$$

令 $\lambda_\pm=3/8\pm\sqrt{66}/24$。二根均为简单根；多项式余式为

$$Q_{1,4}\bmod C_{1,4}=\frac1{30}-\frac78\lambda,$$
$$Q(\lambda_-)=-\frac{283}{960}+\frac{7\sqrt{66}}{192}>0,\qquad
Q(\lambda_+)=-\frac{283}{960}-\frac{7\sqrt{66}}{192}<0.\tag{11}$$

第一个严格正号来自 $(35\sqrt{66})^2-283^2=761>0$。
另外 $\operatorname{Res}_\lambda(C,Q)=-761/921600\ne0$。
故各固定 $\lambda_\pm$ 的首次非恒定项都是
$\epsilon^6Q(\lambda_\pm)\cos(4\theta)$，余项 $O_{C^a}(\epsilon^8)$。
$r=3$ 的分母相同，亦覆盖。

### Step 5. 固定消失点后的真实局部轨道几何

一般地，只要固定 $\lambda_*$ 满足 $C(\lambda_*)=0$、$Q(\lambda_*)\ne0$，
式 (7)除以 $\epsilon^{s+2}$ 后在 $C^2$ 中趋于 $Q\cos(s\theta)$。
因此对充分小 $0<|\epsilon|$，每个相位基本圆恰有两个非退化临界点。
它们实际上恰位于 $\theta=0,\pi/s$：偶性与 $2\pi/s$ 周期性强制两处为临界点，
导数控制排除其他点。已有真实周期接口给出小 $u$ 分支内两条不同 primitive
周期轨道；此处不排除远处周期。简单性 $C'(\lambda_*)\ne0$ 不是这一接口的额外必要条件。

还可判定线性稳定类型。沿真实轨道，作用量 Hessian $H$ 的对角元为
$2+\epsilon\cos q_j+4\lambda\epsilon^2\cos2q_j$，周期相邻非对角元为 $-1$。
其 $X$ 块记为 $H_X$。对充分小参数，$H_X$ 正定。
常数单位向量为 $\mathbf1/\sqrt s$，Schur 补直接给出

$$\det H=\det H_X\,\frac{W''}{s}.\tag{12}$$

令 $M$ 为该轨道一周期导数矩阵。线性差分方程的转移矩阵为
$T_j=\begin{pmatrix}H_{jj}&-1\\1&0\end{pmatrix}$，其周期乘积与 $M$ 共轭。
设 $K_n(a_0,\ldots,a_{n-1})$ 为对角 $a_j$、邻接 $-1$ 的非周期三对角行列式，
$K_0=1$。从 $K_n=a_{n-1}K_{n-1}-K_{n-2}$ 展开转移矩阵乘积及周期行列式，
分别得到

$$\operatorname{tr}(T_{s-1}\cdots T_0)
=K_s(a_0,\ldots,a_{s-1})-K_{s-2}(a_1,\ldots,a_{s-2}),$$
$$\det H=K_s(a_0,\ldots,a_{s-1})-K_{s-2}(a_1,\ldots,a_{s-2})-2.$$

第二式的最后 $-2$ 来自两个绕周期闭合的排列。因此
$\operatorname{tr}M-2=\det H$。结合 (12)，$W''>0$ 的轨道双曲，
$W''<0$ 的轨道在线性意义下椭圆：后者迹小于 $2$ 且趋于 $2$，故仍大于 $-2$。
这里不将“线性椭圆”升级为非线性稳定或 KAM 稳定。

三周期固定 $\lambda=1/24$ 时，$H_X\to L|_X$ 的行列式为 $9$，
所以由 (9)、(12)，

$$\operatorname{tr}M-2=\frac3{64}\epsilon^5\cos(3\theta)+O(\epsilon^6).\tag{13}$$

当 $\epsilon>0$，$\theta=0$ 轨道双曲，$\theta=\pi/3$ 轨道线性椭圆；
$\epsilon<0$ 时类型交换。其配置从

$$q_j=\theta+\frac{2\pi j}{3}
-\frac\epsilon3\sin\left(\theta+\frac{2\pi j}{3}\right)
+\frac{\epsilon^2}{36}\sin\left(2\theta+\frac{4\pi j}{3}\right)+O(\epsilon^3)$$

展开，$p_j=q_j-q_{j-1}$ 给出实际映射轨道。
四周期在 $\lambda_-$ 时 $\theta=0$ 线性椭圆、$\pi/4$ 双曲；
在 $\lambda_+$ 时相反，且 $\epsilon^6$ 使正负小参数的类型相同。$\square$

## Exact computation and reproducibility

- [完整正负 Fourier 脚本](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.py)
  仅计算 $s=3$ 至五阶、$s=4$ 至六阶，向标准输出打印精确 JSON，不修改文件。
- [保存的精确结果摘要](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907_RESULTS.json)
  记录 $C,Q$、固定根代入、余式、resultant 与两种提取方式的差。
- 脚本不仅从 (5)提取系数，还直接代入 SUM action：对共振总模式 $m$，
  动能中 $(e^{i\ell\omega}-1)(e^{i(m-\ell)\omega}-1)=D_\ell$。
  利用 $u=-iv$ 计算动能及两个余弦势，所得余弦系数与力法严格相同；
  两个案例的全部目标阶差值均为零。这是代数交叉核算，不是另一位审查者的独立审查。
- 全部运算在有理数及 $\mathbb Q(\sqrt{66})$ 中进行，没有浮点求根扫描。

复现命令：

```bash
python docs/research-batch07/PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.py
```

## Corrections or missing assumptions

没有把 $\lambda$ 换成依赖 $\epsilon$ 的曲线；没有以纯正频扇区替代完整次项；
没有声称 $s=3$ 的后续余项跳过允许的六阶二倍谐波。
所有“恰两条”均限充分小非零参数和既有小 $u$ 分支。

## Open risks

1. 递推给出每个固定 $r,s$ 的可核算 $Q$，但没有给出统一的
   $C(\lambda_*)=0,C'(\lambda_*)\ne0\Rightarrow Q(\lambda_*)\ne0$ 证明。
2. 即使另有作者证明 $C$ 的全部根实且简单，也不自动排除 $C,Q$ 共享根。
   需要统一非零 resultant、共同根排除机制或等价的严格论证；目前未取得。
3. 若某个其他分母确有 $Q(\lambda_*)=0$，必须继续完整递推下一允许阶及高次谐波，
   不能引用本稿的两个有限案例越过该问题。
4. 本稿不评新意、容量或项目状态；不改任何旧稿、冻结记录或其他代理文件。
   使用 proof-writer 技能明确区分已证明有限结论、实际动力接口与全分母 OPEN。
