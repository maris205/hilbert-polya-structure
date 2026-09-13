# Proof Package：共振端点缺陷的二周期延续与完整一阶矩阵

日期：2026-09-07。作者有界 probe；尚未独立数学审查。
Route applicability: `NOT_APPLICABLE`。
无候选评分、稿件、数值或实验；不改变 Paper30 未立项及 Batch07 3/5。

## Claim

对下述固定标量函数 $f$ 和每条长度 $N\ge2$ 的有限路径图：

1. 端点单缺陷二周期在同一个与 $N$ 无关的小 $\epsilon$ 邻域内，
   存在唯一的局部继续，且位置及其一阶导数有 $\ell^\infty$ 一致界。
2. 全部 $2N$ 个 Floquet 乘子由一个精确实 $N\times N$ 矩阵
   $W=C_bC_a-2I$ 的特征多项式决定。
3. $W=-I+\epsilon J_N+O(\epsilon^2)$ 的完整一阶项为实三对角矩阵：
   缺陷对角元为
   $\theta=13/6+7\alpha/4-16\beta/27$，
   背景对角元为 $-2\deg(i)$，背景邻边为 $2$，
   缺陷相邻边为 $-1/2$ 和 $1/3$。$\gamma$ 完全消去。
4. 对固定 $N$，简单非实／简单实的一阶根给出正确的小参数谱推论；
   特别 $N=2$ 的一阶失稳区间是
   $|\theta+2|<\sqrt{2/3}$。边界 Jordan 点不授予实际谱判定。

第 1、2、3 项的邻域／余项界可以与 $N$ 无关。
第 4 项下文只声称每个固定 $N$ 的 $\epsilon_N$，
不将一阶矩阵的存在误写成实际谱稳定性的一致大链定理。

## Status

`PROVABLE AS STATED`，指本文件明确列出的有限链数学命题。
这是作者证明状态，不是独立审查 `PASS`，也不是新意判定。
半无限链、完整相图、全部 $N$ 的统一失稳窗口和高阶 Jordan 展开未在此声明。

## Assumptions

- $f:\mathbb R\to\mathbb R$ 为 $C^3$；以下只有 $0,1,-1$ 的固定邻域
  $C^3$ 范数进入局部常数。多项式族是特别情形。
- 函数值及一阶导数为
  $$
  f(0)=0,\quad f'(0)=1,\quad f(1)=4,\quad f(-1)=-4,
  \quad f'(1)=8/3,\quad f'(-1)=7/2.
  $$
- 记 $\alpha=f''(1)$、$\beta=f''(-1)$、$\gamma=f''(0)$。
- 图为顶点 $1,\ldots,N$ 的未加权路径，$N\ge2$；缺陷在端点 $1$。
  正 Laplacian $L$ 的对角元为顶点度数，邻边元为 $-1$。
- 只研究实耦合 $\epsilon$ 充分接近零。

## Notation

映射为
$$
 F_\epsilon(q,p)=(q+p-f(q)-\epsilon Lq,\ p-f(q)-\epsilon Lq).
 \tag{1}
$$
$f$ 逐坐标作用。令 $e=(1,0,\ldots,0)^T$。
二周期的位置在时间 $0,1$ 分别记作 $a,b$，
故相应动量是 $a-b,b-a$；未耦合解为 $(a_0,b_0)=(e,-e)$。
下文 $u=a'(0)$、$v=b'(0)$ 指对 $\epsilon$ 的导数，不是时间差分。
两个切向 Hessian 和对应递推矩阵为
$$
 K_a=\operatorname{diag}f'(a)+\epsilon L,\qquad
 K_b=\operatorname{diag}f'(b)+\epsilon L,\qquad
 C_a=2I-K_a,\quad C_b=2I-K_b.
 \tag{2}
$$

## Proof Strategy

先直接在二周期位置方程上作维度一致收缩，
再用真实周期轨道上的二阶差分线性化作精确 Floquet 降维。
最后对该精确矩阵求导。这样周期位移与耦合 Hessian 同时进入，
不使用冻结轨道近似，也不需要假设某个有限矩阵近似完整 monodromy。

## Dependency Map

1. 梯度 kick 和自由 drift 给出真实辛映射及二周期方程。
2. 未耦合位置 Jacobian 的显式逆，加 $\|L\|_\infty\le4$，
   给出一致收缩、唯一性和导数。
3. 二周期 Jacobi 递推与 Schur 补给出精确特征多项式恒等式。
4. 第 2 步轨道导数进入第 3 步矩阵，产生 $J_N$。
5. 固定维数的简单根连续性给出小参数谱结论；重根不使用简单根推论。

## Proof

### Step 1. 辛性和二周期位置方程

取 $U'=f$，势函数
$$
 \mathcal V_\epsilon(q)=\sum_{i=1}^N U(q_i)+\frac\epsilon2 q^TLq.
$$
因为 $L$ 对称，$\nabla\mathcal V=f(q)+\epsilon Lq$。
先作 $p\mapsto p-\nabla\mathcal V(q)$，再作 $q\mapsto q+p$，
分别是势能与自由动能的精确 Hamiltonian 剪切。
两者有显式反向剪切，故 (1) 是全局辛微分同胚；
不要求势函数有下界或原点是势能最低点。

二周期条件等价于
$$
 \begin{aligned}
 2(a-b)-f(a)-\epsilon La&=0,\\
 2(b-a)-f(b)-\epsilon Lb&=0.
 \end{aligned}\tag{3}
$$
由 (3)，从 $(a,a-b)$ 作一步得到 $(b,b-a)$，第二步返回；
反过来任意二周期由 $q_{t+1}-q_t=p_{t+1}$ 满足这些动量关系及 (3)。
给定函数值说明 $(e,-e)$ 在 $\epsilon=0$ 满足 (3)。

### Step 2. 维度一致局部继续和导数

把 (3) 左边记作 $G(x,\epsilon)$，$x=(a,b)$、$x_0=(e,-e)$。
对位置的零阶 Jacobian $D=D_xG(x_0,0)$ 按顶点分成二阶块。
缺陷块及背景块分别为
$$
 D_* =\begin{pmatrix}-2/3&-2\\-2&-3/2\end{pmatrix},\qquad
 D_0=\begin{pmatrix}1&-2\\-2&1\end{pmatrix}.
$$
直接求逆给出
$$
 D_*^{-1}=\begin{pmatrix}1/2&-2/3\\-2/3&2/9\end{pmatrix},\qquad
 D_0^{-1}=-\frac13\begin{pmatrix}1&2\\2&1\end{pmatrix}.
 \tag{4}
$$
因此在所有位置分量的最大范数下
$$
 \|D^{-1}\|_\infty\le C:=7/6
 \tag{5}
$$
与 $N$ 无关。记 $\mathcal L=\operatorname{diag}(L,L)$。
路径图有 $\|\mathcal L\|_\infty\le4$；由于缺陷在端点，
$Le=(1,-1,0,\ldots,0)^T$，故 $\|\mathcal Lx_0\|_\infty=1$。

固定 $0<\rho\le1/4$，并令 $M_2$ 为 $f''$ 在 $0,1,-1$ 的
闭 $\rho$ 邻域并集上的绝对值上界。取
$$
 r=\min\left\{\rho,\frac1{4C\max(1,M_2)}\right\},\qquad
 \epsilon_* =\min\left\{\frac1{16C},\frac r{2C}\right\}.
 \tag{6}
$$
写 $x=x_0+h$。Taylor 展开给出
$$
 G(x_0+h,\epsilon)=Dh+R(h)-\epsilon\mathcal L(x_0+h),
$$
其中 $R(0)=0$，在 $\|h\|_\infty\le r$ 上
$$
 \|R(h)\|_\infty\le\tfrac12M_2\|h\|_\infty^2,
 \qquad \operatorname{Lip}(R)\le M_2r.
$$
等价不动点映射
$$
 \Phi_\epsilon(h)=D^{-1}\{\epsilon\mathcal Lx_0+
                       \epsilon\mathcal Lh-R(h)\}
$$
在该闭球上的 Lipschitz 常数至多
$C(4|\epsilon|+M_2r)\le1/2$。
又 $\|\Phi_\epsilon(0)\|_\infty\le C|\epsilon|\le r/2$，
故映射保持闭球。Banach 不动点定理给出唯一局部解，
并且
$$
 \|h\|_\infty\le2C|\epsilon|.
 \tag{7}
$$
由于 $r\le1/4$，$|a_1-b_1|\ge3/2$；该轨道不是固定点，最小周期确为二。

固定维数的隐函数定理还给出 $C^3$ 参数依赖，因为沿球内
$D_xG$ 与 $D$ 的相对扰动范数至多 $1/2$。
所需一致一阶展开不依赖隐函数定理常数：直接从不动点方程得
$$
 h=\epsilon D^{-1}\mathcal Lx_0+O_\infty(\epsilon^2),\qquad
 \|O_\infty(\epsilon^2)\|_\infty
 \le(8C^2+2M_2C^3)\epsilon^2.
 \tag{8}
$$
将 $(Le,-Le)$ 代入 (4) 得
$$
 \begin{array}{c|ccc}
  &i=1&i=2&i\ge3\\ \hline
  u_i&7/6&-1/3&0\\
  v_i&-8/9&1/3&0
 \end{array}\tag{9}
$$
$N=2$ 时最后一栏为空；唯一邻点的顶点度数虽为一，
(9) 仍成立，因为右边只由 $Le$ 决定。

### Step 3. 完整 Floquet 问题的精确降维

对真实周期轨道的线性扰动 $\xi_t$，位置递推为
$$
 \xi_{t+1}+\xi_{t-1}=C_t\xi_t,
 \qquad C_0=C_a,\quad C_1=C_b.
 \tag{10}
$$
位置对坐标 $(\xi_t,\xi_{t-1})$ 和 canonical 扰动坐标
$(\delta q_t,\delta p_t)$ 由
$\xi_t=\delta q_t$、$\xi_{t-1}=\delta q_t-\delta p_t$
作固定可逆线性变换，故两种 monodromy 相似。
位置对的两步矩阵是
$$
 \mathcal P=\begin{pmatrix}C_b&-I\\I&0\end{pmatrix}
             \begin{pmatrix}C_a&-I\\I&0\end{pmatrix}
 =\begin{pmatrix}C_bC_a-I&-C_b\\C_a&-I\end{pmatrix}.
 \tag{11}
$$
对 $\lambda\ne-1$ 作 Schur 补，然后用多项式恒等性补上 $-1$，得到
$$
 \det(\lambda I_{2N}-\mathcal P)
  =\det\big((\lambda+1)^2I_N-\lambda C_bC_a\big)
  =\det\big(\lambda^2I_N-\lambda W+I_N\big),
 \quad W=C_bC_a-2I_N.
 \tag{12}
$$
这个恒等式保留全部代数重数，不是仅对一部分特征向量的关系。
在 $\lambda\ne0,-1$ 时，特征向量具体满足
$$
 W\xi_0=(\lambda+\lambda^{-1})\xi_0,
 \qquad \xi_{-1}=\frac{C_a\xi_0}{\lambda+1}.
 \tag{13}
$$

零耦合时
$$
 C_{a,0}=\operatorname{diag}(-2/3,1,\ldots,1),\qquad
 C_{b,0}=\operatorname{diag}(-3/2,1,\ldots,1),
 \qquad W_0=-I.
 \tag{14}
$$
由 (7) 和 $\|L\|_2\le4$，
$\|C_a-C_{a,0}\|_2\le(2CM_2+4)|\epsilon|$，
$C_b$ 有同样形式的界。
故缩小一个与 $N$ 无关的参数邻域后，$C_a$ 可逆且恰有一个负特征值，
同时 $\|W+I\|_2<1/2$。后一个界使 $W$ 的实特征值全部位于 $(-2,2)$，
使全部 Floquet 乘子远离 $\pm1$。

由于 $C_a,C_b$ 对称，有精确关系
$$
 W^TC_a=C_aW=C_aC_bC_a-2C_a.
 \tag{15}
$$
这说明 $W$ 对一个负指标为一的非退化实双线性型自伴，
不是对欧氏内积自伴。不能从 (15) 单独推出实谱。

在上述小邻域内，(12) 给出以下严格结论：

- $W$ 的全部特征值实，当且仅当全部 Floquet 乘子在单位圆上。
- 每个非实共轭 $W$ 根对给出离开单位圆的 reciprocal-conjugate 四重组。
- 只有在 $W$ 还可对角化时，才能进一步推出 Floquet monodromy 可对角化。
  反向也成立：由 (13)，每个 $W$ 特征空间分别提升到两个不同的
  Floquet 根，其几何重数等于原特征空间维数；再用 (12) 比较代数重数。
  因此非平凡 Jordan 块不能由“谱在单位圆”掩盖。

### Step 4. 完整一阶矩阵与 $\gamma$ 消去

设
$$
 A_1=K_a'(0)=L+\operatorname{diag}\big(f''(a_0)u\big),\qquad
 B_1=K_b'(0)=L+\operatorname{diag}\big(f''(b_0)v\big).
$$
由于 $C_a'=-A_1$、$C_b'=-B_1$，由 (14) 得
$$
 J_N:=W'(0)=-B_1C_{a,0}-C_{b,0}A_1.
 \tag{16}
$$
缺陷处
$A_{1,11}=1+7\alpha/6$、$B_{1,11}=1-8\beta/9$，故
$$
 J_{11}=\frac23\left(1-\frac{8\beta}9\right)
       +\frac32\left(1+\frac{7\alpha}6\right)
       =\frac{13}6+\frac{7\alpha}4-\frac{16\beta}{27}
       =:\theta.
 \tag{17}
$$
对任意背景顶点 $i\ge2$，(9) 给出 $u_i+v_i=0$，因此
$$
 J_{ii}=-2\deg(i)-\gamma(u_i+v_i)=-2\deg(i).
 \tag{18}
$$
非对角元只来自 $L$。逐项代入 (16)：
$$
 J_{12}=-(-1)\cdot1-(-3/2)(-1)=-1/2,\qquad
 J_{21}=-(-1)(-2/3)-1(-1)=1/3.
 \tag{19}
$$
其余相邻背景顶点有 $J_{i,i+1}=J_{i+1,i}=2$，
其他非邻接非对角元为零。跨缺陷边乘积为 $-1/6$。
对 $N=2$，背景对角元是 $-2$，不是 $-4$。

令 $M_3$ 为固定邻域内的 $|f'''|$ 上界。
由 (8) 对 $f'(a),f'(b)$ 再作 Taylor 展开，
每个对角余项的最大绝对值为 $O(\epsilon^2)$，常数只依赖
$C,M_2,M_3$。矩阵的非对角余项来自有限个乘积与 $L$，
而 $\|L\|_2\le4$。于是
$$
 W=-I+\epsilon J_N+O_2(\epsilon^2)
 \tag{20}
$$
中的算子范数常数与 $N$ 无关。这里没有把
$\ell^\infty$ 向量余项乘以 $\sqrt N$；它只以对角算子的范数进入。

对 (15) 求导，由 $W_0=-I$ 消掉所有 $C_a'$ 项，得到
$$
 J_N^TC_{a,0}=C_{a,0}J_N.
 \tag{21}
$$
令 $S=\operatorname{diag}(\sqrt{3/2},1,\ldots,1)$、$n=N-1$，则
$$
 S^{-1}J_NS=
 \begin{pmatrix}\theta&-g e_1^T\\g e_1&T_n\end{pmatrix},
 \quad g=1/\sqrt6,\quad
 T_n=-2L_{\mathrm{path},n}-2e_1e_1^T,
 \tag{22}
$$
并且 $S^TC_{a,0}S=\operatorname{diag}(-1,I_n)$。
当 $n=1$ 时 $L_{\mathrm{path},1}=0$，因此 $T_1=(-2)$，
公式包括最短链，不需要另设虚构邻边。

### Step 5. 所提多项式族的实际参数

对
$$
 f_\kappa(x)=x+\frac{5x^2+155x^3-5x^4-83x^5}{24}
             +\kappa x^2(x^2-1)^2,
 \tag{23}
$$
直接求导给出
$$
 \alpha=-65/2+8\kappa,\qquad
 \beta=85/3+8\kappa,\qquad
 \gamma=5/12+2\kappa.
$$
代入 (17)：
$$
 \theta(\kappa)=-\frac{46331}{648}+\frac{250}{27}\kappa.
 \tag{24}
$$
其中常数项为
$13/6-455/8-1360/81=-46331/648$。
改变 $\kappa$ 保持所有指定函数值和一阶导数，
却真实改变精确 Floquet 约化的一阶缺陷参数。
这说明耦合响应不能仅由未耦合周期的 Floquet 谱决定。

### Step 6. 正确的固定 $N$ 谱量词；最短链的完整一阶窗口

对 $\epsilon\ne0$ 记
$$
 H_\epsilon=(W(\epsilon)+I)/\epsilon.
$$
它连续延伸到 $H_0=J_N$，并有 $H_\epsilon=J_N+O_2(\epsilon)$。
因此对每个固定 $N$，其全部特征值按代数重数作为多重集合趋向
$\operatorname{spec}J_N$。
若 $\nu$ 是 $J_N$ 的简单根，有限维特征多项式的简单根隐函数定理给出
$$
 w_\nu(\epsilon)=-1+\epsilon\nu+O(\epsilon^2).
 \tag{25}
$$
若 $\nu$ 非实，则该根继续保持非实；若 $\nu$ 实且简单，则其继续为实：
实系数多项式的共轭根与该简单根附近唯一根必须相同。
因此 $J_N$ 全部根实且简单时，实际 monodromy 在某个
$0<|\epsilon|<\epsilon_N$ 内谱稳定且可对角化。
简单非实根给出相应实际四重组。
这里 $\epsilon_N$ 可以依赖最小根间距，不声称与 $N$ 无关。

令 $\lambda_0=e^{2\pi i/3}$。由 $\lambda_0-\lambda_0^{-1}=i\sqrt3$
和 (12)，简单根对应的上半圆簇有
$$
 \lambda_\nu(\epsilon)=\lambda_0
       \left(1+\frac{\epsilon\nu}{i\sqrt3}+O(\epsilon^2)\right).
 \tag{26}
$$
若 $\nu$ 有重数或 Jordan 块，仍有带代数重数的首阶簇极限，
但余项一般只能记为 $o(\epsilon)$，不套用 (25) 的 $O(\epsilon^2)$。

当 $N=2$，
$$
 J_2=\begin{pmatrix}\theta&-1/2\\1/3&-2\end{pmatrix},\qquad
 \det(zI-J_2)=(z-\theta)(z+2)+1/6.
$$
判别式为 $(\theta+2)^2-2/3$。因此：

- 若 $|\theta+2|<\sqrt{2/3}$，$J_2$ 有两个简单非实共轭根，
  对该固定 $f$ 的全部充分小非零实 $\epsilon$，
  实际四维 monodromy 恰有一个离开单位圆的四重组。
- 若 $|\theta+2|>\sqrt{2/3}$，两个根实且简单；
  对全部充分小非零实 $\epsilon$，实际四维 monodromy 的四个乘子
  均在单位圆上且可对角化。
- 等号处 $J_2$ 有一个二阶 Jordan 块，因为它不是标量矩阵。
  第一次约化不足以决定实际谱；此处只报告重根，不断言稳定或失稳。

对 (23)，这个严格失稳区间等价于
$$
 \left|\kappa-\frac{9007}{1200}\right|<\frac{9\sqrt6}{250}.
 \tag{27}
$$
区间内的每个 $\kappa$ 都保持相同的未耦合局部 Floquet 数据；
在区间外的非边界参数，最短链的一阶类型相反。
这里说的是实际有限链的线性谱，不是非线性 Lyapunov 稳定性。
至此各项 Claim 得证。$\square$

## Corrections or Missing Assumptions

- 必须使用真实继续轨道；若冻结 $a=e,b=-e$ 后只加入 $\epsilon L$，
  会漏掉 $7\alpha/4-16\beta/27$，得到错误的缺陷对角元。
- $N=2$ 的背景顶点度数为一，不能照抄长链内部对角元。
- $C^3$ 的局部控制用于一致二阶余项；若只给函数值和一阶 jet，
  需要增加相应光滑性假设后才能声称该余项阶。
- 全 $N$ 一致的是局部周期继续、精确降维的可用邻域及矩阵余项界，
  不是第 6 步从简单根间距取得的实际谱窗口。

## Open Risks

1. 本文件尚须新的独立数学审查；作者计算不自行构成通过。
2. 一般 $N$ 的完整谱相图、半无限链 Weyl 函数和阈值边界均未证明；
   这部分由主控另行探索，不能从 (22) 借入未验证结论。
3. 一阶 Jordan 参数需要高阶数据；一般谱稳定不等于可对角化，
   可对角化也不等于非线性稳定。
4. 创新性仍需扣除既有反连续极限、Krein、band／Jacobi reduction 与
   缺陷矩阵文献；本文件的完整性不能替代文献与价值判断。
   主控在本稿完成期间报告了 DPW 2015/2016 对 index-one Jacobi 模型与闭式根的
   直接先例，以及 Aubry 1998 的相关缺陷／band 失稳先例；
   本代理没有另外扩检，不能把该主控反馈伪称为本稿亲读的查新结论。
   有限链公式本身不预支新意；链长一致的实际非线性谱响应还需另证、另审。

## 执行记录

已亲自完整读取 `proof-writer/SKILL.md`，按其要求分离假设、依赖、
完整证明及未关闭义务。仅新增本作者 probe，未改筛选报告以外的旧输入。
未运行数值或 symbolic-computation pilot，以上为直接代数和有限维证明。
没有 GPT-5.4 MCP 接口；这是实际 secondary 作者证明，非指定模型审稿。
