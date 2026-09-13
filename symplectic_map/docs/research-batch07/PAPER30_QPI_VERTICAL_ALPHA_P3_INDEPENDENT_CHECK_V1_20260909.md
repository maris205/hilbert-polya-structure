# Paper30 qPI P03：特征三首垂直 jet 的非作者数学检查 V1

日期：2026-09-09。检查者：`/root/p30_qpi_integral_cohomology_prior_art_v1`。
类型：固定作者字节的有界非作者数学检查，不是正式候选评审、Route 评价或新意评分。

## Claim

唯一待审作者件为 [P3 作者诊断 V1](PAPER30_QPI_VERTICAL_ALPHA_P3_DIAGNOSTIC_V1_20260909.md)，
全文 251 行、14,474 字节，SHA-256：
`2972929286938bd9f5d5f004f6eaf185c1293969fd4e62d6bad981f13d3a8b3a`。
主控发送最终哈希后才开始读取该件；本次核准不对应中途版本。

固定
$$\mathcal O=\mathbb Z[\zeta_3]_{(\zeta_3-1)},\quad q=\zeta_3=1+\pi,
\quad 3=-\pi^2/q,\quad t_\delta=1+\delta\pi,\quad\delta\in\{0,1\}.$$
保留原八截面曲面、原完整开放部分 $\mathcal U_\delta$ 和原有序积分
$$I_{3,t}=[Z^3]\operatorname{tr}(A(q^2Z)A(qZ)A(Z)),\qquad
\alpha_t=3^{-1}d_{\rm state}I_{3,t}.$$
两闭纤维识别为同一个 $U_0/\mathbb F_3$，其诊断曲线是
$$X=(\bar J=1),\qquad \bar J=y+x/y-x-1/x.$$
本次检查 P3.1 的精确迹短式、P3.2 的全部局部系数理想、P3.3 的端点提升差异，
以及它们实际使用的首切向 jet 粘接、完整末端覆盖和完成环解释。

## Status

**PROVABLE AS STATED；数学检查 PASS。**

在作者明列的已接受完整模型输入下，P3.1–P3.3 保持原范围，不需削弱到环面、
一般点、单个末端或单种时间提升。对每个 $P\in X$，结论为
$$\mathfrak c(\alpha_{t_\delta})_P=(\pi,z),\qquad
\mathfrak c(dI_{3,t_\delta})_P=(\pi^3,\pi^2z),\qquad
\bar z=\bar J-1.$$
等式先在实际局部环中成立，然后完成；不是仅有模 $\pi$ 理想等式。
本文下方补清完成微分、非闭点和状态评价的读法，不增加科学假设。

独立性披露：检查者不是这份作者证明的作者，但已撰写本方向的先例报告，
且在此前交流中知道作者的特征三正向进展；因此本次不称 fresh、盲审或设计隔离审稿。
核准来自本轮对冻结全文的亲读、独立代数展开及局部／全局证明复核，
不是引用作者消息、运行成功或既有查新判断代替数学责任。
本轮没有另一个成功受派的子检查者，也不将一次检查计为多票。

## Assumptions and Input Boundary

1. 原模型、八中心与因子顺序使用 [整数 brief §§2–3](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md)。
   该输入哈希为 `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13`。
2. 已接受 C3 的消费接口是完整 $\mathcal U_\delta/\mathcal O$ 光滑、
   $\alpha_t$ 全局正则和 $\bar\alpha=(\bar J^2-1)d\bar J$。
   本轮定向读取 [D 的固定对象、D1–D3 及先除步骤](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)
   （第 1–130 行），以及 [G Step 6](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)
   的完整末端延拓论证；[数学合取处置 §§1–3](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md)
   确认它们是已接受输入。不重开旧完整证明链。
3. 原小阶完整 pencil 的 $X$ 光滑、几何整与 $d\bar J|_X\ne0$ 沿用作者明列的已接受输入。
   本轮核读 [brief V2 的 T3](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md)，其实际判别多项式在
   $(h,T,\varepsilon)=(1,1,1)$ 的值是 $17\equiv2\pmod3$，确实排除奇异能级。
4. 原状态二形式 $\omega=dx\wedge dy/(xy)$ 的全模型非退化性，核读
   [辛与极除子入口 Steps 2–3](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md)，
   并独立对四个闭末端图再次求 Jacobian；没有把第一图的非退化外推为未经验证的假设。
5. 不假设 $J_t,E_t,F$ 在其他混合特征末端图全局正则；全局论证只使用正则 $\alpha_t$、
   剩余函数 $\bar J$ 及原 $\omega$。仅 $p=3,a=m=1,h=1,t\in\{1,q\}$ 在本次责任范围。

## Notation

用 $Z$ 表示谱变量，$z$ 表示剩余法向函数 $\bar J-1$ 的局部提升，避免同名字母混淆。
令
$$J_t=y+x/y-x-t/x,\quad F=x^2(y-1)^2/y,\quad
E_t=ty-F-xy(y-1),\quad J=J_1,\quad E=E_1.$$
$\mathfrak c(\alpha)$ 是秩二相对微分模中所有系数生成的理想；
标架的可逆变换不改变它。$M|_X$ 表示模的限制，不将相对二方向预先变成曲线一方向。

## Proof Strategy and Dependency Map

1. 原有序乘积系数 $\Rightarrow$ 精确短式 $\Rightarrow$ 特征零先除三后的整一形式。
2. 两时间提升的整一阶展开与实际 Laurent 恒等式 $\Rightarrow$ 环面首切向证书。
3. 局部提升选择独立性 $\Rightarrow$ 正则 $\nu\in\Gamma(X,\Omega_X^1)$；
   全局正则性及稠密环面 $\Rightarrow$ 完整曲线上 $\nu\wedge d\bar J=\omega|_X$。
4. 处处非零的 $\nu$ 与法向简单零 $\Rightarrow$ 两个系数分别生成 $\pi$、$z$。
5. 局部理想的完成及状态评价 $\Rightarrow$ 作者的准确厚度解释与原未整除理想。

## Proof

### Step 1. 原矩阵身份和先除三：PASS

从 brief 的实际 $A_0,A_1,A_2$ 重新构造多项式矩阵，直接乘
$A(q^2Z)A(qZ)A(Z)$ 后提取 $Z^3$ 系数，与作者短式比较。
完整乘法与按次数分类得到同一表达式
$$I_{3,t}=\operatorname{tr}(A_1^3)+3qT_++3q^2T_-,\quad
T_+=\operatorname{tr}(A_0A_1A_2),\quad T_-=\operatorname{tr}(A_0A_2A_1).$$
实际左中右次数 $(0,1,2),(1,2,0),(2,0,1)$ 的谱权指数模三均为一；
另三种排列均为二。使用的是迹循环性，不能在此交换任意两个矩阵。

设 $b=x(y-1)$、$a=t-b$，逐项确认
$$\det A_1=-b,\quad \operatorname{tr}A_1=J_t,\quad
T_+=(a-x)(J_t-1)-xb,\quad T_-=a(J_t-y).$$
两条必要代数式都在整数 Laurent 环中成立：
$$T_+-T_-=E_t,\qquad
T_+-2T_--(\det A_1)J_t=-tJ_t+2t-3F.$$
结合二阶 Cayley–Hamilton 和 $q^2=-2-\pi$，因此精确得到
$$I_{3,t}=J_t^3-3tJ_t+6t-9F+3\pi E_t.$$
这里 $6t$ 没有通过重定能级被删去。
对状态求微分，并在特征零中除以三，给出
$$\alpha_t=(J_t^2-t)dJ_t+\pi dE_t+\frac{\pi^2}{q}dF.$$
两个原 $dx,dy$ 系数均另行直接和原乘积系数的 $1/3$ 导数比较，通过圆分关系后余式为零。
式中的 $q$ 是单位，因此这是环面上的整表达式；不存在特征三除零。

### Step 2. 两时间提升、环面恒等式与指定起点：PASS

将 $t=1+\delta\pi$ 代入，而不固定状态，得到
$$\alpha_{t_\delta}=(J^2-1)dJ+\pi\beta_\delta+O(\pi^2),$$
$$\beta_\delta=dE-\delta(2J/x+1)dJ
  +\delta(J^2-1)x^{-2}dx.$$
本轮分别核对 $dx,dy$ 的零阶和一阶系数。
在 $X$ 上最后一项为零，时间提升引起的另一项是 $d\bar J$ 的倍数，故切向商类相同。
这一步不说全部双分量向量都相同。

独立求导并展开验证作者的整系数余式
$$xy(E_xJ_y-E_yJ_x)-J^3-(J^2-1)
\left(1/x-x(y-1)^2/y-y\right)
=-3x(y-1)(2xy-2x-1).$$
所以模三且限于 $X$ 后
$$d\bar E\wedge d\bar J=\omega|_X.$$
右边的符号与作者选择的 $dx\wedge dy$ 顺序一致。
该非零首切向项是本次实际构造计算的输入，不能只从 $\bar\alpha$ 的 Hasse 零因子推出。

指定点 $(x,y)=(1,i)$ 满足 $i^2=-1$，剩余点定义于 $\mathbb F_9$。
$i^2+1$ 的剩余多项式不可约且导数 $2i$ 为单位，所用 DVR 扩张无分歧。
直接核得 $J=-2$、$d\bar J=-i\,dx+2\,dy$，以及
$$E_x=5+i,\quad E_y=-2i,\quad F_x=-4,\quad F_y=2.$$
对 $\delta=0$ 有 $J_t^2-t=3\in(\pi^2)$，对 $\delta=1$ 该量由圆分关系精确为零。
两次原系数评价均给
$$\left.(\alpha_{t_\delta}/\pi)\right|_{(1,i)}\bmod\pi
=(i+2)dx+i\,dy\ne0.$$
这里除 $\pi$ 是在评价后的两个整系数上进行；不将 $d\bar J$ 先设为零。

### Step 3. 第一完整末端图及原端点值：PASS

在 $x=u^{-1},y=W=1+uv$ 上重新代入，得到正则函数
$$J_t=W-v/W-tu,\qquad F=v^2/W,\qquad E_t=tW-v^2/W-vW.$$
开放环取 $\mathcal O[u,v,W^{-1}]$，包含整条 $u=0$ 末端线；分母不排除其中任何有限状态。
其整 jet 是
$$\beta_\delta=dE-\delta(2uJ+1)dJ-\delta(J^2-1)du,$$
负号来自 $x^{-2}dx=-du$，与环面表达式一致。
直接对本图的 $J,E$ 求偏导，并清除单位分母后在模三多项式环核准
$$E_uJ_v-E_vJ_u=-1/W+(J-1)Q_\infty/W^2,$$
$$Q_\infty=u^2v^3-u^2v^2+uv-v^2-v-1.$$
因此在本图 $X$ 上确实得到 $-1/W$，而非只检验某一个末端点。

第一末端线上 $\bar J=1-v$，故与 $X$ 的唯一交点是 $u=v=0$。
原公式在那里精确给出
$$\alpha_t=-t(1-t)du+(t-1-\pi)dv,$$
因而
$$\alpha_1=-\pi\,dv,\qquad \alpha_q=q\pi\,du.$$
首向量差为 $du+dv=-d\bar J$；它正是法向差，不改变切向类。

### Step 4. 内在切向 jet 的定义及选择独立性：PASS

此步单独在局部代数中核算，不依赖 $E_t,F$ 的全局提升。
任取 $P\in X$，令 $A=\mathcal O_{\mathcal U_\delta,P}$、$M=\Omega^1_{\mathcal U_\delta/\mathcal O,P}$。
$A$ 平坦，$M$ 为自由秩二模，故乘 $\pi$ 在 $M$ 上单射。
选取 $z,G\in A$，分别提升 $\bar J-1,\bar J+1$。
由准确的约化式，$\alpha-zGdz\in\pi M$；存在唯一的
$$\gamma=(\alpha-zGdz)/\pi\in M.$$
“唯一”针对给定的 $z,G$，并不误称不同选择得到同一个 $\gamma$。

若 $z'=z+\pi f$、$G'=G+\pi g$，首差逐项为
$$\frac{z'G'dz'-zGdz}{\pi}
\equiv fGdz+zgdz+zGdf\pmod\pi.$$
限制到 $X$ 后后两项为零，第一项属于 $\mathcal O_Xd\bar J$。
因此
$$\nu=[\bar\gamma|_X]\in
\Omega^1_{U_0/\mathbb F_3}|_X/(\mathcal O_Xd\bar J)=\Omega^1_{X/\mathbb F_3}$$
确实与 $z,G$ 的所有允许选择无关。
商的识别来自闭浸入的余切序列；$d\bar J|_X\ne0$ 保证其法向子模是线子丛。
所用基本序列见 [Stacks, Lemma 10.131.9](https://stacks.math.columbia.edu/tag/00RM)。

在重叠图上两个 $z$ 都提升同一个正则函数 $\bar J-1$，差属于 $\pi A$；
因此上述计算就是实际 Čech 重叠的比较，不需要额外的全球函数提升。
任意标架变换仅改变 $\gamma$ 的坐标，商类不变；固定 $z,G$ 后也没有另一个分解自由度，
因为乘 $\pi$ 单射。故 $\nu$ 在整个 $X$ 正则粘接。
固定参数 $\pi$ 是定义的一部分；本文不声称换任意 DVR 参数后标量完全不变。

### Step 5. 稠密环面的证书覆盖整条曲线及全部四末端：PASS

严谨地定义商线丛映射
$$\Phi:\Omega_X^1\longrightarrow\Omega_{U_0/\mathbb F_3}^2|_X,
\qquad[\eta]\longmapsto\eta\wedge d\bar J.$$
增加法向倍数不改变像；在局部基 $(d\bar J,\theta)$ 中，
$\Phi([\theta])=\theta\wedge d\bar J$ 为二形式生成元，故 $\Phi$ 是同构。
作者的 $\nu\wedge d\bar J$ 表示此映射，不是在一维曲线上取恒为零的 $\Omega_X^2$。

在环面选取 $z=J-1,G=J+1$，Step 2 给 $\nu=[d\bar E|_X]$，
从而 $\Phi(\nu)=\omega|_X$ 在该稠密开集成立。
两边已经分别由 Step 4 与原辛几何定义为整个 $X$ 上的正则线丛截面。
$X$ 几何整，因此截面差若在稠密开集为零，则在函数域中为零，局部自由模的无扭性使其处处为零。
于是
$$\Phi(\nu)=\omega|_X\quad\text{on all }X.$$
$\omega$ 处处非退化，所以 $\nu$ 处处非零。两时间提升的类也因此全局相同。

为核实这里的“全模型”身份，本轮对原四个闭末端图分别直接代入。
因闭纤维 $\bar t=\bar q=1$，令每图的 $W=1+uv$，得到：

| 原末端图编号 | 该闭图的 $\bar J$ | $u=0$ 上的值 | $X$ 的末端交点 $v$ | $\omega/(du\wedge dv)$ |
|---|---|---|---|---|
| 1 | $W-v/W-u$ | $1-v$ | $0$ | $-1/W$ |
| 2 | $v/W+u(u-1)W$ | $v$ | $1$ | $1/W$ |
| 3 | $v/W+u(u-1)W$ | $v$ | $1$ | $-1/W$ |
| 4 | $(v+1)/W-uW$ | $v+1$ | $0$ | $-1/W$ |

四条线都不包含一整个能级分量；它们与 $X$ 的交点均包含在相应正则图中。
这些交点的 $\partial\bar J/\partial v$ 分别为 $-1,1,1,1$，且 $W=1$。
它们不是被删除的边界点，也没有需要另补的有限 $v$ 状态。
这里未假称逐一展开其他三个混合特征图的 $E_t,F$；它们不需要成为正则辅助函数。

### Step 6. 实际理想、所有点与连续完成微分：PASS

由于 $dz$ 在 $M\otimes\kappa(P)$ 中非零，可在局部将其补为自由基 $(dz,\theta)$。
此写法对非闭点也成立，不要求将非闭点误说成有限域有理点。
写
$$\gamma=c_1dz+c_2\theta,\qquad
\alpha=(zG+\pi c_1)dz+\pi c_2\theta.$$
$G$ 在 $P$ 的剩余为 $2$，故为单位；$\nu(P)\ne0$ 说明 $c_2$ 也是单位。
因此
$$\mathfrak c(\alpha)=(zG+\pi c_1,\pi c_2)=(zG+\pi c_1,\pi)=(z,\pi).$$
这个等式先在实际局部环中成立，已覆盖每个 $P\in X$。
若另换 $z'=z+\pi f$，则 $(\pi,z')=(\pi,z)$，故“任一局部提升”量词正确。

在闭点处，$\kappa(P)/\mathbb F_3$ 有限且可分，允许的有限无分歧扩张可使其成为剩余有理点。
记扩张后选定闭点的局部环和微分模为 $A',M'$。
光滑性允许选取相对局部参数 $(z,w)$，完成后有
$$\widehat {A'}\simeq\widehat{\mathcal O'}[[z,w]],\qquad
\widehat {M'}=\widehat {A'}\otimes_{A'} M'
\simeq\widehat {A'}\,dz\oplus\widehat {A'}\,dw.$$
这里使用的是连续相对微分；不把形式幂级数环的未完成代数 Kähler 模直接宣称为自由秩二。
对有限阶商，微分的完成兼容可由
[Stacks, Lemma 10.131.11](https://stacks.math.columbia.edu/tag/00RM)
的 $d(\mathfrak m^{n+1})\subset\mathfrak m^nM$ 逐阶识别后取逆极限。
完成的是原两方向模及其有限生成系数理想，故上述理想等式原样成立。
非闭点不需任何有限无分歧“定义域”措辞：使用前段的局部环等式再完成即可。

对于剩余落在 $X$ 的任一无分歧 DVR 状态提升 $s$，$s^*z\in(\pi)$，
因而系数理想的环同态像为 $(\pi,s^*z)=(\pi)$。
这是将两个系数评价到 DVR 中，不是对一形式施行到 $\Omega^1_{\mathcal O'/\mathcal O}=0$ 的微分拉回。
其最小公共 $\pi$ 赋值准确为一。原微分满足 $dI_3=3\alpha$，所以
$$\mathfrak c(dI_3)=3(\pi,z)=(\pi^3,\pi^2z),$$
沿上述状态提升公共阶准确为三；沿整个剩余曲面泛点的公共阶二并未被改写。
因此局部零概形与“分量提升依赖、理想不变”的解释成立。证毕。

## Corrections or Missing Assumptions

- 没有发现需要作者改动公式、缩小参数范围或补入新科学假设的缺口。
- 作者的“完成坐标”在此明确按连续微分解释；这是其先计算原局部系数理想再完成的准确展开。
- 有限无分歧定义域用于闭点；对任意非闭点，原局部自由模证明直接适用。
  因而不用把“任意 $P$”削弱为只检查闭点。
- $\nu\wedge d\bar J$ 的目标是环境二形式模的限制，不是曲线自身的二形式模。
  此处将作者已使用的环境限制记号写成显式线丛同构，排除了潜在的记号误读。

## Actual Verification and Open Risks

本轮亲读 proof-writer 全文，按其要求拆开假设、精确命题、依赖链与未覆盖量词。
对冻结作者件全文阅读一次后进行独立核算；本报告交付前再全文回读。
没有创建或修改计算脚本，运行的 Python/SymPy 仅做内存中的精确有理式／多项式计算：

1. 原三因子完整矩阵乘法、循环迹分组、两条作者式 (6)、精确原积分和两个整除微分系数。
2. 两状态方向的整零阶／首阶 jet、整 Laurent 余式 (8)、第一末端模三余式 (13)。
3. 指定 $\mathbb F_9$ 点的导数值和首系数、第一末端两种提升的精确值、四闭末端的函数和二形式。

一个初版自检断言曾错误地要求圆分余式在形式多项式意义上显含 $\pi$，
忽略其常数项 $3$ 已属于 $(\pi^2)$；该断言不是作者反例。
改用准确商环 $\mathcal O[i]/(\pi^2)=\mathbb F_9[\pi]/(\pi^2)$ 后全部目标首阶检查通过。
报告中的证明以整数恒等式及局部代数为依据，不以修正后的计算成功取代证明。

浏览仅用于核对上述微分基本序列及完成的术语接口；另查看 Stacks 的完成余切讨论，
未将其不同的限制幂级数完成情形当作这里极大理想完成的直接适用定理。
本轮不是新查新任务，也没有扩张到其他素数或一般 ramified jets。

仍然不接受为本次结论的事项：其他 $p$、$a>1$、$m>1$、$h=-1$、其他时间提升、
非简单 Hasse 根、奇异能级，以及形式群／晶体解释或独立长论文价值。
已接受旧 C3、pencil 与辛几何是消费输入，不因这次 PASS 被重新授予新意。
所有作者源、旧失败和接受记录保持原样；唯一新写文件是本非作者检查报告。
