# 首项根简单性：有限系数变分与参数导数规约 V1

日期：2026-09-07。作者：`p30_twist_root_counterexample_probe`。
已完整读取 `proof-writer` 技能及当前
`PAPER30_TWIST_POST_CANCELLATION_AND_BRIDGE_DISPOSITION_20260907.md`。
本轮选择首项 $C$ 的参数导数与有限系数变分，不计算次项 $Q$，不扫描根数。

## Claim

实际待解命题不变：真实双谐波映射的全部互素分母首项多项式是否具有
$\lfloor s/2\rfloor$ 个正实单根。

本报告证明以下严格规约，而不把规约误认为该命题的证明：

1. 正频指数递推是一个明确有限维系数泛函的唯一临界点方程。
2. 临界值 $G_s$ 满足 $R_s=-sG_s$，且
   $R_s'(a)=(s/2)F_{s-2}(a)$。
3. 根简单性等价于两个明确系数多项式无共同根：
   $\gcd(R_s,R_s')=1$ 当且仅当 $\gcd(E_{s-1},F_{s-2})=1$。
4. 该系数泛函的 Hessian 行列式恒为非零常数，
   但其惯性恒为 $(\lfloor s/2\rfloor,\lfloor(s-1)/2\rfloor,0)$。
   因此该有限维规约是鞍点规约，不是正定最小化原理。

## Status

上述有限规约与 Hessian／导数身份：`PROVABLE AS STATED`。

实际全分母实根／简单性：`NOT CURRENTLY JUSTIFIED`。
没有证明 $E_{s-1}$ 与 $F_{s-2}$ 对实际三角传播子永无共同根。
将此问题改写成 gcd 条件没有消除原本的证明义务。

## Assumptions and Notation

固定互素 $0<r<s$、$s\ge3$，实际传播子为

$$
D_n=4\sin^2(\pi rn/s),\qquad1\le n<s.
$$

它们满足 $D_n>0$ 和 $D_n=D_{s-n}$。
以下有限代数证明事实上只用这两条性质；这既是可用范围，也是能力边界。
没有重开已接受的任意正反射对称辅助反例。

引入系数变量 $v_1,\ldots,v_{s-1}$、两个形式驱动参数 $b,a$，定义

$$
v(t)=\sum_{n=1}^{s-1}v_nt^n,
\qquad \mathcal D(t^n)=D_nt^n,
\qquad E_n=[t^n]e^{v(t)},\quad F_n=[t^n]e^{2v(t)}.
$$

负下标系数为零，$E_0=F_0=1$。对 $1\le n<s$，规定

$$
v_n=\frac{bE_{n-1}+aF_{n-2}}{D_n}.
\tag{1}
$$

该递推的唯一解记为 $v^*(b,a)$，其终端阻碍为

$$
R_s(b,a)=bE_{s-1}(v^*)+aF_{s-2}(v^*),\qquad R_s(a)=R_s(1,a).
$$

这里 $b$ 只用于加权齐次性证明，不改变实际系统；实际正树规范取 $b=1$、
$a=-4\lambda$，已接受的作用量关系是

$$
C_{r,s}(\lambda)=2(-1/2)^sR_s(-4\lambda).
\tag{2}
$$

本报告中的有限系数 Hessian 不叫作旧实际配置 Hessian $H$ 或零均值块 $B$。
这里的变量是正频形式级数系数，所用配对为 $[t^s]fg$，不引入复共轭。
它首先是复系数空间上的全纯多项式泛函；限制在实系数上时为实鞍点泛函。
它不等同于原实际相位空间的正定横向 Hessian。

## Proof Strategy and Dependency Map

1. $D_n=D_{s-n}$ 保证 $[t^s]f\mathcal Dg$ 的双线性对称性。
2. 以此构造有限系数泛函，逐个系数求导得到正频三角方程。
3. 先验证加权齐次性，再由临界值包络求导得到 $R_s'$。
4. Hessian 的反三角支撑给出固定行列式；实对称连续同伦给出固定惯性。
5. 根简单性只归约为系数非零条件；不从鞍点非退化性推断参数横截性。

## Proof

### Step 1. 有限系数泛函及唯一临界点

定义

$$
\Phi_s(v;b,a)=[t^s]\left\{
\frac12v\mathcal Dv-bt e^v-\frac a2t^2e^{2v}\right\}.
\tag{3}
$$

$v$ 的常数项为零，因此提取 $t^s$ 时指数只贡献有限项，
$\Phi_s$ 是 $s-1$ 个系数变量及 $b,a$ 的真正多项式。
对任意两个没有常数项的截断级数 $f,g$，

$$
[t^s]f\mathcal Dg
=\sum_{i+j=s}f_iD_jg_j
=\sum_{i+j=s}D_if_ig_j=[t^s](\mathcal Df)g.
$$

中间等号使用反射对称性，不能只用 $D_n>0$ 替代。
所以一阶变分为

$$
\delta\Phi_s=[t^s]\delta v\bigl(\mathcal Dv-bt e^v-at^2e^{2v}\bigr).
$$

取 $\delta v=t^i$、$1\le i<s$，相应临界点方程为残差的第 $s-i$ 系数为零。
这恰好逐一覆盖 $(1)$ 的所有阶数，且没有除以共振的 $D_s$。
$(1)$ 的第 $n$ 式只涉及先前 $v_1,\ldots,v_{n-1}$，
所以对每个 $b,a$ 存在唯一临界点，而且 $v_n^*$ 是 $b,a$ 的多项式。
这里的唯一性是有限形式系数命题，不是新增的全局真实轨道唯一性命题。

### Step 2. 加权 Euler 恒等式和临界值

给 $b$ 权重 $1$、$a$ 权重 $2$。递推归纳给出

$$
v_n^*(\rho b,\rho^2a)=\rho^nv_n^*(b,a).
$$

于是临界值
$G_s(b,a)=\Phi_s(v^*(b,a);b,a)$ 是权重 $s$ 的多项式。
Euler 恒等式因此为

$$
sG_s=b\,\partial_bG_s+2a\,\partial_aG_s.
$$

临界点方程使所有隐含的 $v^*$ 导数项消失，故

$$
\partial_bG_s=-E_{s-1},\qquad
\partial_aG_s=-\frac12F_{s-2}.
$$

结合上述两式得到

$$
\boxed{R_s(b,a)=-sG_s(b,a)},\qquad
\boxed{\partial_aR_s(b,a)=\frac{s}{2}F_{s-2}(v^*(b,a))}.
\tag{4}
$$

第二式中的导数是包括临界系数响应在内的总参数导数；
不能通过把 $v$ 冻结后直接对终端 $R_s=bE+aF$ 求导来替代它。

### Step 3. 实际 $\lambda$ 规范与根简单性

令 $h=-1/2$，在 $b=1$ 下由 $(2)$、$(4)$ 得到

$$
C_{r,s}'(\lambda)=-4s h^sF_{s-2}(-4\lambda).
\tag{5}
$$

若改用原始正频变量 $X=\epsilon e^{i\theta}$、记
$F^{\mathrm{orig}}_{s-2}=h^{s-2}F_{s-2}(-4\lambda)$，则因为 $h^2=1/4$，
该式等价于

$$
\boxed{C_{r,s}'(\lambda)=-sF^{\mathrm{orig}}_{s-2}(\lambda)}.
\tag{6}
$$

可从实际作用量包络独立检查这个 $s$ 因子：
投影驻值和 $\sum_j u_{j,\lambda}=0$ 给出
$\partial_\lambda W=-\epsilon^2\sum_j\cos2q_j$；
提取第 $s$ 阶纯正频系数，再换回实余弦系数，正好得到 $(6)$。
这里没有重推次项 $Q$，也没有借包络身份假定任何非消失性。

对任意复数 $a_*$，由 $R_s=E_{s-1}+aF_{s-2}$ 和 $(4)$，

$$
R_s(a_*)=R_s'(a_*)=0
\quad\Longleftrightarrow\quad
E_{s-1}(a_*)=F_{s-2}(a_*)=0.
\tag{7}
$$

等价地，作为首一 gcd，有
$\gcd(R_s,R_s')=\gcd(E_{s-1},F_{s-2})$。
这是根简单性的确切有限消元规约，不是该 gcd 已等于 $1$ 的证明。
在根可能出现的 $a<0$ 区域，$F$ 的正系数会发生符号抵消；
不能把 $a\ge0$ 上的系数正性带入该区域。

### Step 4. 系数 Hessian 的固定行列式

以 $\mathscr H=\partial_v^2\Phi_s$ 表示系数 Hessian。逐项求导得到

$$
\mathscr H_{ij}
=D_j\,\boldsymbol1_{i+j=s}
-bE_{s-i-j-1}-2aF_{s-i-j-2},\qquad1\le i,j<s.
\tag{8}
$$

这对任意系数向量 $v$ 成立，不只在临界点成立。
若 $i+j>s$，三个项全部为零；若 $i+j=s$，只剩 $D_j$。
因此 $\mathscr H$ 是反三角矩阵，反对角元依次为 $D_{s-i}$。
把列顺序反转即可得到三角矩阵，故

$$
\boxed{\det\mathscr H
=(-1)^{(s-1)(s-2)/2}\prod_{n=1}^{s-1}D_n\ne0.}
\tag{9}
$$

对实际正弦传播子，已知单位根乘积给出 $\prod D_n=s^2$，
所以其绝对值恒为 $s^2$。该常数行列式不是 $R_s$ 的谱多项式表示。

### Step 5. 系数 Hessian 的固定鞍点惯性

限制 $v,b,a$ 为实数。令 $\mathscr A_{ij}=D_j\boldsymbol1_{i+j=s}$。
由于 $D_j=D_{s-j}$，$\mathscr A$ 实对称；每对 $i,s-i$ 的二维块为
$\begin{pmatrix}0&D_i\\D_i&0\end{pmatrix}$，具有一个正、一个负特征值。
若 $s$ 为偶数，另有中央的一维正块 $D_{s/2}$。
因此其正／负／零特征值数为

$$
\left(\left\lfloor\frac s2\right\rfloor,
\left\lfloor\frac{s-1}{2}\right\rfloor,0\right).
$$

沿实对称线性路径
$\mathscr A+\tau(\mathscr H-\mathscr A)$、$0\le\tau\le1$，
反三角支撑和反对角元保持不变，故 $(9)$ 保证没有特征值穿过零。
实对称矩阵特征值连续，从而整条路径惯性不变。于是

$$
\boxed{\operatorname{inertia}(\mathscr H)
=\left(\lfloor s/2\rfloor,\lfloor(s-1)/2\rfloor,0\right).}
\tag{10}
$$

特别地 $s\ge3$ 时至少有一个负方向。唯一临界点始终非退化，
不意味着其临界值随参数 $a$ 穿过零时一定横截；后者正是 $(7)$ 中尚未解决的条件。

### Step 6. 可选的二阶响应身份及其边界

在临界点定义
$\beta_i=F_{s-i-2}$，负下标仍取零。
由 $\Phi_{va}=-\beta$ 和临界点求导得
$\partial_a v^*=\mathscr H^{-1}\beta$。
因为 $\Phi$ 对 $a$ 线性，临界值二阶导数为
$\partial_a^2G_s=-\beta^T\mathscr H^{-1}\beta$，因此

$$
\partial_a^2R_s=s\,\beta^T\mathscr H^{-1}\beta.
\tag{11}
$$

这是双线性而非 Hermitian 收缩；即使所有系数取实数，
$(10)$ 也阻止把右边直接当作正定二次型。∎

## Exact Checks Actually Run

没有运行根数扫描。只作两个低阶精确代数一致性检查：

- 实际 $s=4$、$D=(2,4,2)$，保留形式 $b$：
  $R_4=a^2/2+3ab^2/2+5b^4/24$，
  $G_4=-a^2/8-3ab^2/8-5b^4/96$；直接核对驻值、$(4)$，
  并对独立系数变量求 Hessian，得到 $\det\mathscr H=-16$。
- 在主控建议不必追加凸性例之前，已执行实际 $s=6$ 的一次精确代数核对：
  $R_6=2a^3/3+39a^2/4+127a/12+99/80$，故 $R_6''=4a+39/2$。
  在固定参数 $a=0,-5$，$(11)$ 分别精确给出 $39/2,-1/2$，
  且 $\det\mathscr H=36$。没有求根或增加分母；随后没有追加算例。
  这一有限检查不承担全分母惯性证明，后者已在 Step 5 独立完成。

## Corrections or Missing Assumptions

没有改变实际模型、旧首项定义、既有诊断或后项 $Q$ 的工作分配。
有限系数变分的成立需要传播子反射对称性；只写正性会遗漏关键假设。
但正性与反射对称性仍不足以证明实根，已接受的辅助反例继续有效，未在本轮重算。

当前缺少的是利用真实三角结构证明 $(7)$ 中共同根不存在，或给出可认证实际共同根。
常数非零的系数 Hessian 行列式不能替代这个参数消元义务。

## Open Risks and Handoff

1. $R_s=-sG_s$ 是鞍点临界值身份，不是 $R_s$ 的实对称线性谱参数行列式身份。
2. $\gcd(E,F)$ 只是更明确的消元目标，尚无对全部实际 $r,s$ 的非零证书。
3. 未证明全分母全部根实、根单或次项 $Q$ 在其上非零。
4. 本轮没有查新、正式评价、篇幅估计、论文立项或 PDF 产物。
