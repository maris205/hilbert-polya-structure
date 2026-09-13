# Jacobi–Schur 桥接与真实正弦有限身份：独立数学核查

日期：2026-09-07。核查者：`p30_twist_root_counterexample_probe`，不是两份输入的作者。
使用本轮已完整读取的 `proof-writer` 技能；核查范围仅为下述恒等式及其明确推论。

## Claim and Scope

完整读取并核查：

1. `PAPER30_TWIST_JACOBI_BRIDGE_PROOF_V1_20260907.md`，共 $167$ 行：
   假设、零均值块正定性、非驻值相位的链式法则、总作用量 Schur 因子、
   首余弦系数及固定消失参数处的条件性推论与惯性。
2. `PAPER30_TWIST_SINE_STRUCTURE_PROBE_V2_20260907.md`，共 $271$ 行：
   真实 $s=4$ 的树／直接路径多项式尺度不变量、循环 Green 核、
   固定端点逆核及双线性／Hermitian 收缩身份。

输入 SHA-256，按上述顺序：

```text
0ade8082e78575a9306087b2d8d7b38b980acb424963344a08bd9b58a36d1a52
47b4ba9b09d37122bfbcaa6f4680d162a054eed2714b002595f3f9b8fa82f3b9
```

已接受的实际解析消元存在性和相位过滤作为输入使用，不重开旧证明包。
本次未读取或重算六例高精度根表，未扫描其他分母，未修改任何作者文件。
核查期间主控仅将 Jacobi 文末的“非循环的”澄清为“非事后拟合”，
已确认该处当前文本；此措辞避免误读为排除周期矩阵，不改变数学假设与公式。

## Status

`PASS — DECLARED IDENTITIES AND CONDITIONAL CONSEQUENCES`。

两份输入在下述限定范围内未发现数学错误。精确恒等式和有限身份核对通过，
但全分母实根／简单性及固定消失点后项的普遍非消失性仍未证明。
本报告不是正式候选评价、原创性评价、Route 评价、论文接收或产物验收。

## Assumptions and Dependency Map

- 固定互素 $0<r<s$、$s\ge3$；$\lambda$ 属于预定紧区间，$\epsilon$ 足够小。
- 所有对象取实配置，均可依赖固定 $r,s$ 与该紧区间；没有分母一致量词。
- 作用量是未除以 $s$ 的总和，$Q$ 是与参数无关的正交零均值基，
  $B=Q^THQ$ 是正交压缩，不是删去一个坐标的固定端点主子矩阵。
- 精确 Schur 身份只依赖投影驻值及 $B$ 可逆；正定性另由扰动界得到。
- 首系数提取额外使用已接受的 $W-\overline W$ 首项及相位导数余项控制。
- 消失点推论额外假定该点的真实首非恒定项、非零振幅及 $C^2$ 余项已经独立证明。

## Checks: Jacobi–Schur Bridge

### 1. 实际 Hessian 和 $B>0$：PASS

给定势项的二阶导数确为
$\epsilon\cos q_j+4\lambda\epsilon^2\cos2q_j$，因此

$$
H=L+\operatorname{diag}(\epsilon\cos q_j+4\lambda\epsilon^2\cos2q_j).
$$

实配置保证扰动算子范数不超过
$|\epsilon|+4\sup_J|\lambda|\epsilon^2$。
$L$ 的零均值特征值为 $4\sin^2(\pi k/s)>0$，$1\le k<s$。
把扰动界取为最小正特征值的一半以下，即得到作者声明的统一相位正定界。
此步不需要假定完整驻值，也不依赖 $u$ 的导数有界来估计余弦本身。

### 2. 非驻值相位切向量及二阶链式项：PASS

由 $Q^T\nabla\mathcal A=0$ 求导得 $Q^THq_\theta=0$。
采用 $e_0=\boldsymbol1/\sqrt s$ 及 $q_\theta=\sqrt s e_0+Qx$，得到
$x=-\sqrt s B^{-1}b$。
这一步没有使用 $W'=0$。

二阶链式法则中的附加项确实消失：
$\nabla\mathcal A=c\boldsymbol1$，但 $q_{\theta\theta}=u_{\theta\theta}$
的均值严格为零，因此
$\nabla\mathcal A^Tq_{\theta\theta}=0$，即使 $c\ne0$ 也成立。
不能把这个事实误写成“梯度已经为零”；作者没有这样做。

### 3. 总作用量 Schur 因子：PASS

上述切向量给出

$$
W''=s\left(a-b^TB^{-1}b\right).
$$

由于 $(e_0,Q)$ 是正交基，分块行列式没有额外体积因子，故

$$
\det H=\det B\left(a-b^TB^{-1}b\right)
=\frac{\det B}{s}W''.
$$

其中 $1/s$ 来自 $\theta$ 方向向量的平方范数 $s$；不能删除。
全式在非驻值相位同样成立。

### 4. 首实 Fourier 余弦系数：PASS

单位根乘积给出 $\det B|_{\epsilon=0}=s^2$。
这不同于固定端点路径 Laplacian 的行列式 $s$；两份作者文档中出现的
“正交压缩 $B$”与“固定端点逆核 $K$”不能混作同一个矩阵。

已接受的相位过滤保证 $W''$ 在次数小于 $s$ 时全部为零，并且其第 $s$ 阶为
$-s^2C_{r,s}\cos(s\theta)$。因此只有 $\det B$ 的常数项参与第 $s$ 阶，得到

$$
[\epsilon^s\cos(s\theta)]\det H
=\frac{s^2}{s}(-s^2C_{r,s})=-s^3C_{r,s}.
$$

这里取的是实余弦系数；若改成单边复 Fourier 系数会另有 $1/2$，
不能混用。作者对这一规范说明正确。

### 5. 固定消失参数与惯性：PASS，保持条件性

若独立给定固定 $\lambda_*$ 上的真实首非恒定项
$\epsilon^kA\cos(s\theta)$、$A\ne0$，且余项为 $C^2$ 中的
$o(\epsilon^k)$，则 $\det B/s=s+O(\epsilon)$ 与精确身份确实给出
$\det H=-s^3A\epsilon^k\cos(s\theta)+o(\epsilon^k)$。
此结论没有证明该首项一定存在、一定属于此谐波，或 $A$ 一定非零。

分块合同变换将 $H$ 化为
$\operatorname{diag}(a-b^TB^{-1}b,B)$，而 $B>0$。
因此 $W''>0$ 时全部特征值为正，$W''<0$ 时恰有一个负特征值，
$W''=0$ 时恰有一个零特征值且其余全部为正。
此代数结论本身甚至不要求完整驻值；作者只在实际驻值点陈述它，没有过度外推。
作者亦未据此直接宣布辛映射的椭圆／双曲稳定性，边界正确。

## Checks: Two Finite Sine Identities

### 6. $R_4$ 与直接路径 $T_4$：PASS

真实 $D_1,D_2,D_3=(2,4,2)$ 下，逐级精确计算得到

$$
R_4=\frac5{24}+\frac32a+\frac12a^2,
\qquad T_4=\frac1{16}+\frac12a+\frac14a^2.
$$

定义 $I(P)=b_1^2/(b_0b_2)$ 时，变换 $P(a)\mapsto AP(Ba)$
在 $A,B\ne0$ 下保持 $I$，而这里 $I(R_4)=108/5\ne16=I(T_4)$。
因此声明的总体尺度和参数乘法重标身份不存在。
固定一步／两步权的组合确实只给出 $b^sT_s(ca/b^2)$，故同一反例适用。
这并不排除依赖阶数权重、其他参数变化或更复杂的三对角表示；作者没有声称排除。

### 7. Green 核与两种收缩：PASS

直接二阶差分及求和验证

$$
g_j=\frac{s^2-1}{12s}-\frac{j(s-j)}{2s},\qquad
Lg=\delta_0-\boldsymbol1/s,\qquad \sum_jg_j=0.
$$

因此对非零 Fourier 模，所采用的无归一化 Fourier 和确为 $1/D_n$，
没有缺少额外的 $s$ 因子。
固定端点逆核
$K_{ij}=\min(i,j)-ij/s$ 的差分、端点条件及实正定性均正确。

对于本原 $\zeta$ 和 $\phi_j=\zeta^j$，$s\ge3$ 保证
$\sum\phi_j=\sum\phi_j^2=0$；即使 $s$ 为偶数，$\zeta^2\ne1$ 仍成立。
于是 $u=(\phi-1)/D_1$ 满足 $u_0=0$、$Lu=\phi$，并给出

$$
f^TKf=0,\qquad f^*Kf=s/D_1>0.
$$

两种乘积确实不同：复解析正相位系数中的乘法不自动带共轭。
真实 $s=4$ 示例的精确值分别为 $0$ 和 $2$。
这只排除把该双线性收缩直接当作 Hermitian 正型的推理，
没有证明所有利用 Green 核的保根方法均不可能。

## Independent Exact Tests Actually Run

除执行结构作者附带的精确 $s=4$ 代码外，独立完成以下符号算例。

1. 在正交坐标 $(t,y,z)$ 中取
   $\mathcal A=(y-t^2)^2/2+(z-t^3)^2/2+t+2t^2$，
   以 $t=\sqrt3\theta$、$y=t^2$、$z=t^3$ 消去横向变量。
   消元曲线加速度非零，且 $W'=12\theta+\sqrt3$ 一般非零；
   精确得到 $\nabla\mathcal A^Tq_{\theta\theta}=0$、
   $\det H=4$、$\det B=1$、$W''=12$。
   这是抽象链式法则／Schur 压力测试，不被称为原辛映射的新例子。
2. 对实际模型仅取 $s=3,r=1,\theta=0$，直接从投影驻值方程求出
   $u=\epsilon u_1+\epsilon^2u_2+O(\epsilon^3)$，其中

   $$
   u_1=(0,-\sqrt3/6,\sqrt3/6)^T,
   \quad
   u_2=(0,\sqrt3(\lambda/3-1/36),-\sqrt3(\lambda/3-1/36))^T.
   $$

   代回完整 Hessian 再精确取行列式，得到
   $[\epsilon]\det H=[\epsilon^2]\det H=0$，以及
   $[\epsilon^3]\det H=9/8-27\lambda=-27(\lambda-1/24)$。
   这独立核对实际作用量的 $-s^3$ 因子，不是重新做旧根扫描。
3. 对 $s=3,4$ 的非零 Laplacian 特征值乘积，精确得到 $9,16$。

实际输出：

```text
NONSTATIONARY_EXACT: detH=4 detB=1 Wsecond=12 Wprime=12*theta+sqrt(3)
ACTUAL_S3_EXACT: det coefficient eps^3=9/8-27*lam=-27*(lambda-1/24)
LAPLACIAN_PRODUCT: 3 9
LAPLACIAN_PRODUCT: 4 16
EXACT_PASS: path identity fails; bilinear and Hermitian contractions differ
```

## Corrections or Missing Assumptions

没有要求修改两份作者输入。已有假设足以支持上述恒等式及明确条件推论。
本核查不替作者补造全根表示，也不把“实对称矩阵”误当成
“其某个 Fourier–Taylor 系数关于 $\lambda$ 必全实根”的定理。

## Open Risks

1. $H$ 的参数依赖包括真实非线性位移 $u(\theta,\epsilon,\lambda)$；
   精确 Schur 桥接尚未给出以 $\lambda$ 为线性谱参数的特征多项式身份。
2. 固定消失点处真实后项及非消失性只在额外假设下进入惯性推论。
3. 两个有限身份排除的是指定捷径，不是实际模型的全实根猜想。
4. 原全分母根数、实性、重数及后续分裂义务保持 OPEN；批次和论文状态未变。
