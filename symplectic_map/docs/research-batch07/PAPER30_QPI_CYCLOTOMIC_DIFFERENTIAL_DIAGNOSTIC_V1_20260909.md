# Paper30 qPI：圆分降阶的整除微分与 Hasse 系数诊断 V1

日期：2026-09-09。作者：主控 /root，可用 Codex AI。
类型：新方向的有界作者证明／理论诊断，不是正式候选、论文稿或独立接受。
proof_status：PROVABLE AS STATED（作者判断，等待非作者检查）。
derivation_status：COHERENT AS STATED。

## 1. 固定目标、原对象与边界

目标不是重新证明现有 T1–T7，也不是给旧新意分数补差。
这里改变研究量词：沿特征零圆分整数的素点约化，允许剩余特征整除原根单位阶。
检验的顶层量是原积分的**相对状态微分**及其最大统一整除因子，
不是任意选择的能级重标定、普通线性 q-curvature 或未经构造的稳定模型。

设 $p$ 是任意素数，$a\ge1$、$m\ge1$、$p\nmid m$，并记
$$N=p^a,\qquad r=mN,\qquad s=\zeta_r.$$
令 $\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}$，其中 $\mathfrak p$ 是 $p$ 上方任一素理想。
这是特征零 DVR；取其任一参数 $\pi$，剩余域 $\kappa$，记 $e=v_\pi(p)$。
将 $s$ 的剩余记为 $\eta$，它的精确阶为 $m$。
后一个事实也可由
$$\Phi_{mp^a}(X)\bmod p=\Phi_m(X)^{p^{a-1}(p-1)}$$
及 $p\nmid m$ 时 $X^m-1$ 可分得到。

取
$$\mathcal B=\mathcal O[t^{\pm1},x^{\pm1},y^{\pm1}],\qquad
\Omega=\Omega^1_{\mathcal B/\mathcal O[t^{\pm1}]}=\mathcal B\,dx\oplus\mathcal B\,dy.$$
本件的 $d$ 只作用于 $x,y$，固定 $t,s,z$；不是关于 $t$ 或 $s$ 的全微分。
将 $t$ 特化为任何 $\mathcal O$-单位后，以下恒等式仍成立。
横线表示模 $\pi$ 约化，除以 $N$ 必须先在特征零中完成。

原矩阵、顺序与规范固定为 [brief V2 §2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md)：
$$A(z)=A_0+zA_1+z^2\operatorname{diag}(1,0),$$
$$A_0=
\begin{pmatrix}
t+x-xy&-x\\
t+x-ty-2xy+xy^2&x(y-1)
\end{pmatrix},$$
$$A_1=
\begin{pmatrix}
y-x+x/y-1-t/x&1\\
y-2x-1+xy+x/y-t/x&1
\end{pmatrix}.$$
对精确阶为 $n$ 的参数 $\xi$，记
$$M_{n,\xi}(z)=A(\xi^{n-1}z)\cdots A(\xi z)A(z).$$
使用 JR 原积分恒等式
$$\operatorname{tr}M_{n,\xi}(z)=t^n+I_{n,\xi}z^n+z^{2n},\qquad
\det M_{n,\xi}(z)=\varepsilon_n z^{3n},\quad
\varepsilon_n=(-1)^{n+1}.$$
它适用于特征零的 $(r,s)$ 及剩余特征中的 $(m,\eta)$。
以下简写 $I_r=I_{r,s}$、$J=I_{m,\eta}$、$T=t^m$、$\varepsilon=\varepsilon_m$，
$Z$ 是独立谱变量，不是状态坐标。
JR 的矩阵、积分与这两条恒等式是已有来源输入，不计本件新发现。

## 2. 准确命题

在上述全部参数下有：

**D1（零阶降阶）**
$$\overline{I_r}=J^N.$$
这是矩阵幂与 Frobenius 的直接结果，本身不提出新意主张。

**D2（整除微分及其非零首项）**
$$\alpha_r:=N^{-1}dI_r\in\Omega,$$
并在 $\overline\Omega$ 中严格满足
$$\boxed{\quad
\overline{\alpha_r}
=H_p(T,J;\varepsilon)^{\,1+p+\cdots+p^{a-1}}\,dJ.\quad} \tag{1}$$
这里的多项式为
$$H_p(T,h;\varepsilon)=
\begin{cases}
[Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
h,&p=2.
\end{cases} \tag{2}$$
其系数取在 $\kappa$ 中。它关于 $h$ 首一、次数 $p-1$。
因此 $\overline{\alpha_r}\ne0$，$dI_r$ 的全体 Laurent 系数的最小 $\pi$-赋值准确为 $ae$。
这不是每一个闭点上都具有同一赋值的断言。

**D3（光滑能级上的含重数零概形）**
在剩余状态环中，写 $dJ=J_xdx+J_y dy$。则
$$\operatorname{coeffideal}(\overline{\alpha_r})
=(H_p(T,J;\varepsilon)^{(N-1)/(p-1)})\,(J_x,J_y). \tag{3}$$
在原 $m$ 阶系统的光滑能级开集，$dJ$ 不消失，所以 (3) 正是拉回 Hasse 零除子
并将其重数乘 $(N-1)/(p-1)$ 的理想。
光滑谱曲线
$$E_{T,h}:\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3=0$$
上的指定微分 $\omega=dZ/(2\lambda-(T+hZ+Z^2))$ 将 (2) 识别为 Hasse 不变量；
特征二解释为 $\omega=dZ/(T+hZ+Z^2)$。
在光滑层，$H_p=0$ 等价于椭圆曲线超奇异；本句不将奇异三次曲线称为超奇异。

## 3. 依赖与证明策略

1. D1 只用模 $\pi$ 的重复矩阵块与迹的 Frobenius。
2. D2 的整性来自完整长度 $r$ 的循环插入，不在特征 $p$ 中直接除以 $r$。
3. 将已整除的表达式约化后，先沿长度 $m$ 求和，再用 $2\times2$ Cayley–Hamilton；
   不通过约化后已为零的 $d(J^N)$ 猜出首项。
4. 指数 $(N-1)/(p-1)$ 来自精确系数提取；Cartier 的半线性规范另行说明。
5. D3 的理想等式直接来自 (1)；只在调用“原光滑能级”时使用既有 T1–T3。

## 4. 证明

### Step 1. 零阶并不是新的小阶 pencil

剩余参数 $\eta$ 的阶为 $m$，故
$$\overline{M_{r,s}(z)}=B(z)^N,\qquad B(z):=M_{m,\eta}(z).$$
在任意特征 $p$ 交换系数环上，$2\times2$ 矩阵满足
$\operatorname{tr}(B^{p^a})=(\operatorname{tr}B)^{p^a}$；
可在通用矩阵的分裂域中用特征根证明，再由整系数多项式恒等式下降。
比较 $z^r$ 的系数得到 D1。
因而约化后的函数本身是小阶积分的纯不可分复合；不据此将其称为最小完整 pencil。

### Step 2. 循环插入给出特征零中的整除

令
$$Q_r(z)=\operatorname{tr}
\big(dA(z)A(s^{r-1}z)\cdots A(sz)\big)\in\Omega[z].$$
对 $\operatorname{tr}M_{r,s}(z)$ 求微分时，在第 $j$ 个因子处插入 $dA(s^jz)$。
将该项的迹循环移位，使微分因子置于最左边，再把谱变量变为 $w=s^jz$，
其余因子依次为 $A(s^{r-1}w),\ldots,A(sw)$。
这里用 $s^r=1$，但没有交换两个矩阵因子。
所以该项就是 $Q_r(s^jz)$。

由于 $s^{jr}=1$，每一项的 $z^r$ 系数均为 $[z^r]Q_r(z)$。
相加得到整系数恒等式
$$dI_r=r[z^r]Q_r(z). \tag{4}$$
特别地 $dI_r/r$ 已在 $\Omega$ 中；$\alpha_r=m[z^r]Q_r(z)$。
这一步先于剩余约化，故不存在“在特征 $p$ 除以零”的问题。

### Step 3. 约化后保留导数插入的位置

设 $A_j=A(\eta^jz)$，并记
$$C_j=A_{m-1}\cdots A_{j+1}\,dA_j\,A_{j-1}\cdots A_0,
\qquad dB=\sum_{j=0}^{m-1}C_j.$$
空乘积取单位矩阵，故 $m=1$ 同样适用。
将式 (4) 的插入放回最右位置可得
$$\overline{\alpha_r}=m[z^{mN}]\operatorname{tr}(B^{N-1}C_0).$$
对 $j=0,\ldots,m-1$，$\operatorname{tr}(B^{N-1}C_j)$
是长度 $r=mN$ 的同一循环中第 $j$ 个位置的导数插入。
沿 Step 2 的循环移位与 $z\mapsto\eta^jz$，它们的 $z^{mN}$ 系数相同。
因此
$$\overline{\alpha_r}
=[z^{mN}]\operatorname{tr}(B^{N-1}dB). \tag{5}$$
这里仅相加 $m$ 项，并没有消去一个在剩余域为零的 $N$。

### Step 4. 秩二迹递推

定义整系数多项式
$$U_{-1}=0,\quad U_0=1,\quad
U_n(S,D)=S U_{n-1}(S,D)-D U_{n-2}(S,D)\quad(n\ge1).$$
若 $S=\operatorname{tr}B$、$D=\det B$，Cayley–Hamilton 和
$dD=\operatorname{tr}(\operatorname{adj}(B)dB)$ 给出
$$\operatorname{tr}(B^{N-1}dB)
=U_{N-1}(S,D)dS-U_{N-2}(S,D)dD. \tag{6}$$
例如 $N=2$ 时，右侧为 $S\,dS-dD=\operatorname{tr}(B\,dB)$。
一般情形用 $B^{N-1}=U_{N-2}B-DU_{N-3}\mathrm{id}$ 代入，
再用 $S U_{N-2}-D U_{N-3}=U_{N-1}$ 得到；$N\ge2$ 已由 $a\ge1$ 保证。

在本题
$$S=T+JZ+Z^2,\qquad D=\varepsilon Z^3,\qquad dD=0,\quad dS=Z\,dJ.$$
式 (5)、(6) 因而变成
$$\overline{\alpha_r}
=[Z^{N-1}]U_{N-1}(T+JZ+Z^2,\varepsilon Z^3)\,dJ. \tag{7}$$
这是恒等式，不是对大 $p$ 的近似。

### Step 5. Frobenius 幂与系数的唯一数字展开

在对称变量 $u,v$ 中有
$$U_{N-1}(u+v,uv)=\frac{u^N-v^N}{u-v}.$$
这表示多项式恒等式，右式在 $u=v$ 处也由多项式延拓定义。
特征 $p$ 且 $N=p^a$ 时它等于 $(u-v)^{N-1}$。
对称多项式嵌入 $\mathbb F_p[S,D]\hookrightarrow\mathbb F_p[u,v]$
说明这不是只在某些可对角化矩阵上成立。
因此
$$U_{N-1}(S,D)=
\begin{cases}
(S^2-4D)^{(N-1)/2},&p\ne2,\\
S^{N-1},&p=2.
\end{cases}$$

若 $p\ne2$，记 $f(Z)=((T+hZ+Z^2)^2-4\varepsilon Z^3)^{(p-1)/2}$，
其次数不超过 $2p-2$。则
$$((T+hZ+Z^2)^2-4\varepsilon Z^3)^{(N-1)/2}
=\prod_{i=0}^{a-1}f(Z)^{p^i}.$$
在任一贡献到 $Z^{p^a-1}$ 的项中，最低位指数须与 $p-1$ 模 $p$ 同余，
而 $0\le n_0\le2p-2$，故只能为 $n_0=p-1$。
去掉该位后逐位重复，全部 $n_i=p-1$。
系数因此是
$$[Z^{N-1}]\prod_i f(Z)^{p^i}
=\prod_i([Z^{p-1}]f)^{p^i}
=H_p^{1+p+\cdots+p^{a-1}}.$$
特征二改取 $f(Z)=T+hZ+Z^2$，次数为二，最低位须奇数，仍只能取一；
同一逐位论证给 $h^{1+2+\cdots+2^{a-1}}$。
代入 (7) 证明 (1)，含 $p=2,3$、$m=1$ 与全部 $a\ge1$。

### Step 6. 非零性与准确统一赋值

奇特征时，(2) 的 $h^{p-1}$ 项只能来自 $(h^2Z^2)^{(p-1)/2}$，系数为一；
其他项的 $h$ 次数更低。特征二的结论由定义成立。
而 JR 的原 Laurent 首项为
$$J=-t^m x^{-m}+O(x^{-m+1}).$$
因 $p\nmid m$、$t\ne0$，$J_x$ 的首项为 $m t^m x^{-m-1}\ne0$。
于是 $dJ\ne0$，且首一的 $H_p(T,J;\varepsilon)\ne0$。
这证明 $\overline{\alpha_r}\ne0$。
以自由基 $dx,dy$ 取全体 Laurent 系数的最小赋值，式 $dI_r=p^a\alpha_r$
给出准确值 $a v_\pi(p)$。单位 $t$ 的任意特化不改变上述非零首项论证。

### Step 7. Cartier 解释与完整理想而非根集

先在完美底域上的光滑能级曲线验证 Hasse 解释；
一般剩余域参数可基变换至代数闭域检验零点性质。
奇特征令 $Y=2\lambda-(T+hZ+Z^2)$，则
$$Y^2=(T+hZ+Z^2)^2-4\varepsilon Z^3,\qquad \omega=dZ/Y.$$
对非奇异四次亏格一模型，$\omega$ 是全局正则非零微分。
由 Cartier 规则 $\mathcal C(g^p\nu)=g\mathcal C(\nu)$
及只保留指数同余 $p-1$ 的项，
$$\mathcal C(\omega)
=Y^{-1}\mathcal C\big(Y^{p-1}dZ\big)
=H_p(T,h;\varepsilon)^{1/p}\omega.$$
因 $\deg(Y^{p-1})=2p-2$，只有 $Z^{p-1}$ 项贡献。
特征二有
$$\omega=\frac{dZ}{T+hZ+Z^2}
=\frac{(T+hZ+Z^2)dZ}{(T+hZ+Z^2)^2},$$
故 $\mathcal C(\omega)=h^{1/2}\omega$。
其正则性可在有限光滑图用方程的残差微分，
在无穷远图 $w=1/Z,\ \mu=\lambda/Z^2$ 用
$-dw/(2\mu-(Tw^2+hw+1))$ 验证；两个无穷远点分母为单位。
在有限处 $f_\lambda=0$ 时用 $-d\lambda/f_Z$ 的等价表达，光滑性保证至少一个偏导为单位。

这里 Hasse 系数取 $H_p$，Cartier–Manin 一维矩阵取 $H_p^{1/p}$；
不把二者或半线性迭代混称为同一数。
椭圆曲线的 Cartier 为零恰对应超奇异，给 D3 的光滑层解释。
最后，在 $\overline\Omega$ 的自由基中逐项取系数，(1) 直接给 (3)。
既有 T1–T3 说明光滑能级上 $(J_x,J_y)$ 是单位理想；
故那里得到含重数的 Hasse 拉回理想，不是仅比较几何根集。证毕。

## 5. 动力学解释与不能推出的东西

模 $\pi$ 后原 $r$ 步有理回返是原 $m$ 步回返的 $N$ 次迭代：
时间参数按长度 $m$ 重复。此句可直接在各映射共同定义的稠密开集逐项验证。
依已有原域 torsor 平移身份，泛纤维上的作用是平移 $[N]P_m$。
这不是把点坐标施以 Frobenius，也不是将回返误写成次数 $N^2$ 的乘法同源。
本件不建立混合特征八吹起模型上的全闭纤维回返延拓。

D1 与 D2 是不同层级：$d(\overline I_r)=d(J^N)=0$，
但先在整模型中除以 $p^a$ 再约化得到非零 (1)。
超奇异能级只说明该**已约化整除微分**再消失；
没有指定能级提升或下一阶模型，不能由此断言每个提升点的下一项赋值、
完整稳定约化、Vanishing cycles、野导子或全 ramified jet 已经计算。
式 (3) 在坏能级仍保留乘积理想，不把它简化成互不相交的两个零集合。

## 6. 来源、实际验证与新意边界

原 $A,M,I$、迹／行列式与 Laurent 首项归属
[JR 作者 v2 Theorem 3.1、Remarks 3.2/3.4](https://arxiv.org/html/2508.18578v2)；
本件从已接受本地 brief §2 消费这些固定输入，没有重审旧九对数学模块。
Cartier 的定义、半线性和奇特征四次公式按本人本轮实际读到的
[Achter–Howe，作者 v5 §§2.2–2.4、3.1](https://arxiv.org/html/1710.10726v5)核准；
超奇异／普通与 Hasse 的定义按本人实读
[Voloch 1990，Conventions，p.248](https://www.numdam.org/article/CM_1990__74_3_247_0.pdf)核准。
未声称通读这些外部论文；上述标准工具不是新贡献。
本件为作者完整代数推导，未运行数值拟合或以样本替代全 $p,m,a$ 证明。

本件使用 formula-derivation 固定相对微分这个对象，再用 proof-writer 分离整性、约化、
非零性与 Hasse 解释。它不提供新意分数，也未通过独立数学审查。
另行开展的圆分／q-curvature 来源核查可能指出更近包含关系，不能预先排除。
即使 D1–D3 正确，也不自动满足独立论文价值或自然正文 22–30 页要求。
需要下一步判断的实质剩余是：精确整除微分识别相对最近先例是否独立，
以及超奇异处下一阶信息或完整几何退化是否能带来非直接的新增结论。
这些后续问题均保持 OPEN，不因本件结果自动加入旧候选、重开两票或创建 V3。
