# 双谐波真实约化：Jacobi–Schur 行列式桥接 V1

日期：2026-09-07。身份：主控作者证明；独立核查另存。
使用 `proof-writer` 区分一个完整恒等式与尚未获得的保根定理。
本文件不修改旧首项证明或其已接受审查。

## Claim

在既有实际解析零均值约化上，完整循环 Jacobi Hessian $H$ 与
零均值 Hessian $B$ 满足精确恒等式

$$\det H=\frac{\det B}{s}\,\partial_\theta^2 W.\tag{1}$$

此式不要求 $\partial_\theta W=0$。对未除以 $s$ 的总作用量规范，
首共振多项式 $C_{r,s}(\lambda)$ 满足

$$[\epsilon^s\cos(s\theta)]\det H=-s^3 C_{r,s}(\lambda).\tag{2}$$

方括号表示先作 $\epsilon$ 的 Taylor 展开，再取实 Fourier 余弦系数，
不是取 $e^{is\theta}$ 的单边系数。

## Status

上述两个恒等式：`PROVABLE AS STATED`。

“它们已经证明 $C_{r,s}$ 对全部分母具有正实单根”：
`NOT CURRENTLY JUSTIFIED`。本文件未将原全分母问题换成较弱验收标准。

## Assumptions and notation

固定互素整数 $0<r<s$、$s\ge3$，置 $\omega=2\pi r/s$。
$\lambda$ 在预先固定的紧实区间 $J$ 内，$\epsilon$ 为充分小的实数。
所有邻域及常数可依赖 $r,s,J$；没有分母一致性结论。
使用同一映射及总作用量：

$$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p',$$

$$\mathcal A(q)=\sum_{j=0}^{s-1}
\left\{\tfrac12(q_{j+1}-q_j)^2-\epsilon\cos q_j
-\lambda\epsilon^2\cos2q_j\right\}.$$

配置写作 $q_j=\theta+\omega j+u_j$，满足
$q_{j+s}=q_j+2\pi r$、$u_{j+s}=u_j$、$\sum_j u_j=0$。
令 $X=\boldsymbol1^\perp\subset\mathbb R^s$，$\Pi$ 为其正交投影。
$u=u(\theta,\epsilon,\lambda)$ 是从 $\epsilon=0,u=0$ 出发的唯一小解析解
$\Pi\nabla\mathcal A=0$，而 $W=\mathcal A(q(\theta,\epsilon,\lambda))$。
该实际解及其相位过滤已经由
[约化与奇偶证明](PAPER30_TWIST_REDUCTION_PARITY_NOTE_V1_20260907.md) 建立并接受。

定义循环 Laplacian $(Lx)_j=2x_j-x_{j-1}-x_{j+1}$。在上述实际配置上，

$$H=\nabla^2\mathcal A
=L+\operatorname{diag}_{j}
\left(\epsilon\cos q_j+4\lambda\epsilon^2\cos2q_j\right).$$

选择与所有参数无关的实正交基矩阵 $Q\in\mathbb R^{s\times(s-1)}$，
使 $Q^TQ=I$、$QQ^T=\Pi$。记

$$e_0=s^{-1/2}\boldsymbol1,\quad B=Q^THQ,\quad
a=e_0^THe_0,\quad b=Q^THe_0.$$

这里 $B$ 不是删去某一坐标的固定端点主子矩阵，而是 $X$ 上的正交压缩。
更换 $Q$ 为另一个正交基不改变 $\det B$。

## Proof strategy and dependency map

1. $L|_X>0$ 及连续性保证 $B$ 的局部可逆性与正定性。
2. 对真实投影驻值方程求导，得到消元切向量。
3. 约化的二阶链式法则消去完整梯度项，给出 Schur 补。
4. 正交分块行列式公式证明 $(1)$；单位根乘积及已接受的相位首项证明 $(2)$。

## Proof

### Step 1. 零均值块保持正定

在 $\epsilon=0$，$B=Q^TLQ$，其特征值为
$4\sin^2(\pi k/s)>0$，$1\le k<s$。
势 Hessian 的对角扰动算子范数不超过
$|\epsilon|+4\sup_{\lambda\in J}|\lambda|\epsilon^2$。
选取 $\epsilon$ 邻域使此界小于 $L|_X$ 最小特征值的一半，
则对任意 $x\in\mathbb R^{s-1}$，

$$x^TBx\ge\tfrac12\lambda_{\min}(L|_X)\|x\|^2.$$

因此 $B$ 对所有所述相位与参数可逆且正定。

### Step 2. 消元曲线的切向量

固定 $\epsilon,\lambda$ 对 $Q^T\nabla\mathcal A(q)=0$ 求 $\theta$ 导数，
得到 $Q^THq_\theta=0$。因为 $u_\theta\in X$，可写成
$q_\theta=\boldsymbol1+Qx=\sqrt{s}e_0+Qx$。
于是 $\sqrt{s}b+Bx=0$，即

$$q_\theta=\sqrt{s}\left(e_0-QB^{-1}b\right).\tag{3}$$

这个求导没有假定完整驻值条件；投影驻值对所有 $\theta$ 成立即已足够。

### Step 3. 二阶链式法则与精确行列式

链式法则给出

$$W''=q_\theta^THq_\theta+(\nabla\mathcal A)^Tq_{\theta\theta}.$$

投影驻值使 $\nabla\mathcal A=c\boldsymbol1$，某个实数 $c$ 允许非零。
又 $q_{\theta\theta}=u_{\theta\theta}\in X$，因此最后一项等于零。
代入 $(3)$ 并用 $Q^THQ=B$，得到

$$W''=s\left(a-b^TB^{-1}b\right).\tag{4}$$

在正交基 $(e_0,Q)$ 中，$H$ 的矩阵为
$\begin{pmatrix}a&b^T\\ b&B\end{pmatrix}$。
由于 $B$ 可逆，分块高斯消元给出
$\det H=\det B\,(a-b^TB^{-1}b)$。
结合 $(4)$ 即为 $(1)$。整个证明允许 $W'\ne0$。

### Step 4. 首项的归一化因子

在 $\epsilon=0$，由本原单位根 $\eta=e^{2\pi i/s}$ 有

$$\det B\big|_{\epsilon=0}
=\prod_{k=1}^{s-1}(1-\eta^k)(1-\eta^{-k})=s^2.$$

最后等号来自对 $(z^s-1)/(z-1)=\prod_{k=1}^{s-1}(z-\eta^k)$
代入 $z=1$，两组因子各给出 $s$。
既有约化证明在任意固定有限相位导数范数中给出

$$W-\overline W=\epsilon^s C_{r,s}(\lambda)\cos(s\theta)
+O(\epsilon^{s+2}).$$

因而 $W''$ 在低于 $s$ 阶的所有 Taylor 系数均为零，
第 $s$ 阶为 $-s^2C_{r,s}(\lambda)\cos(s\theta)$。
在 $(1)$ 中，第 $s$ 阶只能乘以 $\det B|_{\epsilon=0}/s=s$，
故得到 $(2)$。$\square$

## Consequence at a fixed cancellation parameter

若某个固定 $\lambda_*$ 满足 $C_{r,s}(\lambda_*)=0$，
并且独立证明了首非恒定项确为
$\epsilon^k A\cos(s\theta)$，$A\ne0$、$k>s$，
且余项在 $C^2$ 中为 $o(\epsilon^k)$，则同一恒等式推出

$$\det H=-s^3 A\epsilon^k\cos(s\theta)+o(\epsilon^k).$$

这里的假设必须另证，不能从 $(1)$ 倒推 $A\ne0$。
在实际驻值点，$B>0$ 时 $H$ 的惯性由 $(4)$ 的单个 Schur 补控制：
$W''>0$ 时 $H>0$；$W''<0$ 时恰有一个负特征值；$W''=0$ 时
恰有一个零特征值，其余 $s-1$ 个为正。这是分块合同变换的直接结果。
本文件没有再把惯性声明转换成未经检查的映射稳定性分类。

## Corrections or missing assumptions

这确实是来自原映射实际配置的实对称循环 Jacobi 矩阵恒等式，
不是按数值根拟合的矩阵。但它**不是**所需的关于 $\lambda$ 的线性谱参数表示：

- $H$ 中 $q_j=\theta+\omega j+u_j(\theta,\epsilon,\lambda)$ 本身随 $\lambda$ 非线性变化。
- $C$ 是行列式的一个 Fourier–Taylor 系数，不是已被识别出的整条特征多项式。
- 实对称性约束固定参数时的矩阵特征值，并不自动约束其某个展开系数作为
  $\lambda$ 多项式的全部零点。

因此若想用 Jacobi 理论关闭全根命题，仍需一个非事后拟合、从递推直接证明的
精确多项式表示及相应实性与不可约性条件；冻结 $u=0$ 也不能代替实际消元。

## Open risks

全分母根的实性、简单性及固定消失点的首非恒定阶仍需各自证明。
本恒等式不自动关闭其中任何全分母量词；它只建立精确矩阵接口。
没有论文立项、正式候选票、容量估计、Route 评价或 PDF 产物。
