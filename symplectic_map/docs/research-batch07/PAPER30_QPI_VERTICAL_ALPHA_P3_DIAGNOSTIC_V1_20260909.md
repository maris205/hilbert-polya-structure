# Paper30 qPI P03：三次圆分整除微分的首垂直 jet 诊断 V1

日期：2026-09-09。类型：有限参数的作者诊断／可证引理，不是正式候选、评分或论文。
本件转入 P03，既有 C1–C3 及非单位时间参数文件均不修改、不重新投稿。

## Claim

取 $p=3,a=m=1$，令
$$\mathcal O=\mathbb Z[\zeta_3]_{(\zeta_3-1)},\qquad q=\zeta_3=1+\pi,$$
所以
$$q^2+q+1=0,\qquad \pi^2+3\pi+3=0,\qquad 3=-\pi^2/q.$$
只比较 $t_\delta=1+\delta\pi$，其中 $\delta\in\{0,1\}$。
对两种提升分别保留原八截面曲面及其完整开放部分 $\mathcal U_\delta$，固定
$$I_{3,t}=[z^3]\operatorname{tr}(A(q^2z)A(qz)A(z)),\qquad
\alpha_t=\frac13d_{\mathrm{state}}I_{3,t}.$$
微分只作用于两个状态方向，不作用于 $t,q,\pi$。

两模型的剩余开放曲面自然相同，记为 $U_0/\mathbb F_3$。
其原小阶积分与诊断曲线为
$$\bar J=y+x/y-x-1/x,\qquad X=(\bar J=1)\subset U_0.$$
$X$ 是已接受原模型中的光滑几何整有限能级；$H_3(1,h)=h^2-1$，故 $h=1$ 是简单超奇异根。

**P3.1（原三因子迹的精确短式）。** 令
$$
J_t=y+x/y-x-t/x,\quad F=x^2(y-1)^2/y,\quad G=xy(y-1),\quad E_t=ty-F-G.
$$
在原环面上有精确恒等式
$$I_{3,t}=J_t^3-3tJ_t+6t-9F+3\pi E_t, \tag{1}$$
$$\alpha_t=(J_t^2-t)dJ_t+\pi\,dE_t+\frac{\pi^2}{q}dF. \tag{2}$$

**P3.2（两个状态方向的实际局部理想）。** 对 $\delta=0,1$、任意 $P\in X$，
在允许定义该点的有限无分歧扩张后，取 $\mathcal U_\delta$ 在该点的完成局部环。
令 $z$ 为 $\bar J-1$ 的任一局部提升，则
$$\widehat{\mathfrak c(\alpha_{t_\delta})}_P=(\pi,z). \tag{3}$$
此处 $\mathfrak c$ 由相对二方向一形式的全部系数生成，不是先拉回到一维曲线再取系数。
结论覆盖原完整 $X$，因而包含四条末端仿射线上的全部交点。
它不是预设的正规形：首切向 $\pi$-jet 的非零性在下面证明。

**P3.3（提升依赖与理想不变必须区分）。** 在第一末端图
$$x=u^{-1},\qquad y=1+uv,$$
零截面点 $P_\infty:(u,v)=(0,0)$ 满足
$$\alpha_{1}(P_\infty)=-\pi\,dv,\qquad
\alpha_q(P_\infty)=q\pi\,du. \tag{4}$$
两系数向量不同，但其局部理想都为 (3)。因此本诊断中没有首厚度的状态／提升依赖，
不能从分量的变化推断局部零概形发生不同厚化。

## Status

PROVABLE AS STATED（仅对以上 $p=3$、两种 $t$ 提升和 $h=1$ 的作者结论；待独立核查）。
首诊断给出简单的 $(\pi,z)$，没有发现更高垂直厚度或沿纤维变化的首障碍支撑。
这不评价 P03 的全参数问题，也不把既有模 $\pi$ Hasse 公式当作本件新结论。

## Assumptions and Input Boundary

1. 原对象、矩阵顺序和四个末端图固定于[整数 brief §§2–3](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md)。
   不用拟合多项式，不改变 $I_3$ 的能级常数规范。
2. 消费已接受 C3 的两个必要输入：$\alpha_t$ 在完整 $\mathcal U_t$ 正则，以及
   $$\bar\alpha_t=(\bar J^2-1)d\bar J.$$
   其环面整性和约化在[原整除微分证明 D](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)，
   完整末端延拓在[完整模型证明 G，Step 6](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)。
3. 消费原小阶完整 pencil 的 $X$ 光滑、几何整和 $d\bar J|_X\ne0$；
   此诊断能级的原小阶判别式模三为 $2$，不是奇异三次曲线。
4. 原状态二形式
   $$\omega=dx\wedge dy/(xy)$$
   在整个 $U_0$ 正则且处处非退化，包括四条末端线。
   这是原几何的已接受输入；第一图上直接为 $-du\wedge dv/(1+uv)$。
5. 不假设辅助 Laurent 函数 $E_t,F$ 在其他三个混合特征末端图分别正则。
   Step 5 的全局延拓使用原 $\alpha_t$ 和一个内在定义的切向 jet，不把 $E_t$ 虚构为全局函数。

## Notation

无横线的 $J=J_1$、$E=E_1$ 在环面及第一末端图是指定整提升；
$\bar J,\bar E$ 是相应剩余函数。其他图中只在需要时选取 $\bar J-1$ 的局部提升 $z$。
$O(\pi^2)$ 在本文表示 $\pi^2$ 乘该图上的一个正则相对一形式，不表示数值近似。
“点上值”指在固定相对基 $dx,dy$ 或 $du,dv$ 中评价两个系数，仍保留两方向。

## Proof Strategy and Dependency Map

1. 精确提取三因子乘积的 $z^3$ 项，利用迹的循环性而非交换矩阵，得到 (1)–(2)。
2. 提取两种 $t$ 提升的首 $\pi$-jet，并给一个整系数恒等式证明它沿 $X$ 的切向部分处处非零。
3. 第一完整末端图直接检查原式正则性、同一切向非零性和 (4)。
4. 用 $\bar\alpha=(\bar J^2-1)d\bar J$ 构造与局部能级提升无关的切向 jet $\nu$。
   它全局正则，环面恒等式遂延到完整光滑 $X$，覆盖剩余三个末端图。
5. 非零切向 jet 将系数理想中的一个生成元化成 $\pi$ 乘单位，另一个化成 $z$ 乘单位，证明 (3)。

## Proof

### Step 1. 保持原乘积顺序的精确迹恒等式

原矩阵写为 $A(z)=A_0+zA_1+z^2A_2$，其中
$$
A_0=\begin{pmatrix}t+x-xy&-x\\t+x-ty-2xy+xy^2&x(y-1)\end{pmatrix},
$$
$$A_1=\begin{pmatrix}y-x+x/y-1-t/x&1\\y-2x-1+xy+x/y-t/x&1\end{pmatrix},\qquad
A_2=\operatorname{diag}(1,0).$$
$z^3$ 的三种因子次数只能是 $(1,1,1)$ 或 $(0,1,2)$ 的六种排列。
对于循环次序 $(0,1,2)$，三个循环位置的 $q$ 权均为 $q$；
反向次序的三个权均为 $q^2$，因为 $q^3=1$。
故准确地有
$$I_{3,t}=\operatorname{tr}(A_1^3)+3qT_++3q^2T_-,\quad
T_+=\operatorname{tr}(A_0A_1A_2),\quad T_-=\operatorname{tr}(A_0A_2A_1). \tag{5}$$
这里仅用了迹的循环移位，没有把 $A_0,A_1,A_2$ 任意交换。

令 $b=x(y-1)$、$a=t-b$。原矩阵化为
$$A_0=\begin{pmatrix}a&-x\\-(y-1)a&b\end{pmatrix},\qquad
A_1=\begin{pmatrix}J_t-1&1\\J_t-1+b&1\end{pmatrix}.$$
因此 $\operatorname{tr}A_1=J_t$、$\det A_1=-b$，而
$$T_+=(a-x)(J_t-1)-xb,\qquad T_-=a(J_t-y).$$
直接展开，或使用 $b(J_t-y)=-F-t(y-1)$，得到
$$T_+-T_-=E_t,$$
$$T_+-2T_- - (\det A_1)J_t=-tJ_t+2t-3F. \tag{6}$$
二阶 Cayley–Hamilton 给 $\operatorname{tr}(A_1^3)=J_t^3-3(\det A_1)J_t$。
把 $q=1+\pi,q^2=-2-\pi$ 及 (6) 代入 (5)，得到 (1)。
在特征零先除以三，再取相对状态微分；$d(6t)=0$，且 $-3=\pi^2/q$，故得到 (2)。
这也在环面上直接展示 $\alpha_t$ 的整性；没有在特征三中除以零。

### Step 2. 两种提升的首 $\pi$-jet与切向证书

在共同环面上有
$$J_{t_\delta}=J-\delta\pi/x,\qquad E_{t_\delta}=E+\delta\pi y.$$
由 (2) 精确展开至模 $\pi^2$：
$$\alpha_{t_\delta}=(J^2-1)dJ+\pi\beta_\delta+O(\pi^2), \tag{7}$$
$$\beta_\delta=dE-\delta(2J/x+1)dJ+\delta(J^2-1)x^{-2}dx.$$
因此在 $X$ 上，$\bar\beta_\delta$ 的切向类与 $\delta$ 无关，且
$$\bar\beta_\delta\wedge d\bar J=d\bar E\wedge d\bar J.$$
这句话只比较切向类；(7) 的整个两分量向量仍可依赖 $\delta$。

令
$$Q=1/x-x(y-1)^2/y-y,$$
则下列是特征零中的整系数 Laurent 恒等式：
$$
xy(E_xJ_y-E_yJ_x)-J^3-(J^2-1)Q
=-3x(y-1)(2xy-2x-1). \tag{8}
$$
它可由 $J,E$ 的上述定义逐项微分并展开核对；右端明确含因子三。
模三再限制到 $X$，得到
$$d\bar E\wedge d\bar J=\frac{dx\wedge dy}{xy}\bigg|_X=\omega|_X. \tag{9}$$
右端在环面上是单位二形式，故首切向 $\pi$-jet 在该稠密开集处处非零。

### Step 3. 指定 $\mathbb F_9$ 起点的两状态检查

令 $\mathcal O'=\mathcal O[i]/(i^2+1)$，按剩余不可约二次多项式的素点局部化。
因为 $2i$ 为单位，这是有限无分歧二次扩张，剩余域为 $\mathbb F_9$。
取固定提升 $(x,y)=(1,i)$。在剩余域中 $\bar J=1$，并有
$$d\bar J=-i\,dx+2\,dy\ne0.$$
在该提升上 $J=-2$，$J_{t_\delta}=-2-\delta\pi$；
$J_{t_0}^2-t_0=3\in(\pi^2)$，而 $J_{t_1}^2-t_1=0$，后者正是圆分关系。
又有
$$E_x(1,i)=5+i,\qquad (E_{t_\delta})_y(1,i)=\delta\pi-2i,$$
$$F_x(1,i)=-4,\qquad F_y(1,i)=2.$$
代入 (2) 得两种提升都满足
$$\left.\frac{\alpha_{t_\delta}}{\pi}\right|_{(1,i)}\bmod\pi
=(i+2)\,dx+i\,dy. \tag{10}$$
这是先评价两个原系数，再除以 $\pi$，不是把 $d\bar J$ 置零后的曲线微分。
向量非零，所以此点额外公共 $\pi$ 阶准确为一；该点的首向量碰巧不依赖 $\delta$。

### Step 4. 一张完整末端图的实际理想

使用第一末端图 $x=u^{-1},y=W=1+uv$，其相关开放环为
$\mathcal O[u,v,W^{-1}]$。整条末端仿射线是 $u=0$、$v$ 任意；没有删去有限的 $v$ 状态。
原辅助量在此直接化为
$$J_t=W-v/W-tu,\qquad F=v^2/W,\qquad E_t=tW-v^2/W-vW. \tag{11}$$
全都正则，没有隐藏的 $u^{-1}$ 项。(2) 因而是本完整图中的正则二方向一形式。

置 $J=J_1,E=E_1$。此图的 (7) 为
$$\alpha_{t_\delta}=(J^2-1)dJ+\pi\beta_\delta+O(\pi^2),$$
$$\beta_\delta=dE-\delta(2uJ+1)dJ-\delta(J^2-1)du. \tag{12}$$
以下给本图独立的整系数余式证书。在特征三中，令
$$Q_\infty=u^2v^3-u^2v^2+uv-v^2-v-1.$$
对 (11) 微分后有
$$E_uJ_v-E_vJ_u=-\frac1W+(J-1)\frac{Q_\infty}{W^2}\quad\text{in }\mathbb F_3[u,v,W^{-1}]. \tag{13}$$
故在 $X$ 的本图部分，切向楔积系数是单位 $-1/W$，与 $\delta$ 无关。
本图上的末端交点唯一为 $u=v=0$，因为 $\bar J|_{u=0}=1-v$。
在固定零截面点 $P_\infty$ 直接由 (11) 得
$$J_t=1,\quad dJ_t=-t\,du-dv,\quad dF=0,\quad dE_t=-dv.$$
代入 (2)，得到
$$\alpha_t(P_\infty)=-t(1-t)\,du+(t-1-\pi)\,dv,$$
从而证明 (4)。
第一提升首向量为 $-dv$，第二为 $du$；这与 (10) 一起展示分量提升依赖会随状态点改变。
但 (13) 的单位性质没有改变，下面据此以及内在延拓证明理想一致。

### Step 5. 不假设 $E$ 全局正则的内在切向 jet

这是把有限图计算接到所有末端点的必要步骤。
固定一种 $t_\delta$，在 $X$ 的任一点附近取 $z$ 提升 $\bar J-1$，并取 $G$ 提升 $\bar J+1$。
由已接受的完整约化式
$$\bar\alpha=\bar z(\bar J+1)d\bar z,$$
以及 $\mathcal U_\delta/\mathcal O$ 光滑、相对一形式局部自由，可唯一除去 $\pi$，写成
$$\alpha=zG\,dz+\pi\gamma. \tag{14}$$
定义
$$\nu=\bigl[\bar\gamma|_X\bigr]\quad\text{in }\Omega^1_X
=\Omega^1_{U_0}|_X/\mathcal O_X\,d\bar J.$$

这个类与上述局部选择无关。
若 $z'=z+\pi f$，$G'=G+\pi g$，则
$$z'G'\,dz'-zG\,dz
\equiv\pi(fG\,dz+zg\,dz+zG\,df)\pmod{\pi^2}.$$
限制到 $X$ 后，后二项消失，第一项是 $d\bar J$ 的倍数，故不改变 $\nu$。
不同图的 $z$ 都提升同一个剩余函数 $\bar J-1$，所以其差必为 $\pi f$。
改变一形式标架也只改变同一商线丛的表示，因而 $\nu$ 在整个 $X$ 上粘成正则一形式。
固定 $\pi$ 是本定义的一部分；这里没有更换 DVR 参数。

对 $\nu$ 的任意局部提升再楔 $d\bar J$，所得二形式与提升无关。
在稠密环面部分，(7) 给它正是 $d\bar E\wedge d\bar J$，由 (9) 得
$$\nu\wedge d\bar J=\omega|_X. \tag{15}$$
两边现在都已在完整 $X$ 上正则。$X$ 几何整、环面部分稠密，
故线丛截面在稠密开集相等就全局相等；这一步不需要 $E$ 本身在其他末端图正则。
原 $\omega$ 处处非退化，而 $d\bar J$ 沿光滑 $X$ 非零，所以 (15) 证明 $\nu$ 在整个 $X$ 处处非零。
两种 $t$ 提升得到的 $\nu$ 在环面上相同，故在整个 $X$ 上相同。
这完成所有四末端的覆盖接口，不用另一种曲面替代原模型。

### Step 6. 从非零切向 jet 到两个系数的准确理想

在任一点 $P\in X$，$z$ 的剩余微分非零，可补为相对局部／完成坐标 $(z,w)$。
把 (14) 写成
$$\alpha=(zG+\pi A)\,dz+\pi B\,dw.$$
$G|_X=2$ 是单位；Step 5 的 $\nu$ 处处非零说明 $B|_X$ 是单位，故 $B$ 在该局部环也是单位。
于是系数理想包含 $\pi$，再由第一个系数及 $G$ 为单位得到它包含 $z$。
反向包含由显示公式立即成立，所以
$$\mathfrak c(\alpha)_P=(\pi,z),$$
完成后仍相等，证明 (3)。
这是两方向系数理想的计算；若过早将 $dz$ 拉回成零，将丢失生成元 $z$，只剩一个 $\pi$ 系数。

因而已整除微分的零概形在 $X$ 附近是约化的余维二闭纤维曲线，没有更高 $\pi$ 厚度。
对于任意取值于无分歧扩张 DVR、约化到此 $X$ 的状态提升，(3) 拉回后就是 $(\pi)$。
所以两实际系数的最小赋值准确为一，不依赖该状态提升如何选择。
未整除原微分的理想则为
$$\mathfrak c(dI_3)=3\mathfrak c(\alpha)=(\pi^3,\pi^2z), \tag{16}$$
等式中的单位因子不影响理想；其沿上述 DVR 状态提升的最小公共阶为三。
这与全剩余曲面泛点原来只有公共阶 $v_\pi(3)=2$ 不矛盾。P3.1–P3.3 证毕。

## Corrections and Interpretation

- 本诊断的 Hasse 根重数为一，并无 $z^2$ 的先验依据。
  实际算出的正规形是 $(\pi,z)$，不是猜测的更高厚度式。
- 首 $\pi$-jet 的两分量在末端点对 $t$ 提升敏感，但这种变化落在法向部分；
  内在切向类及全部系数理想不变。因此“分量不同”不等于“零概形不同”。
- (15) 把首切向信息识别为原状态辛形式除以 $d\bar J$ 所给的曲线一形式；
  它在此有限诊断中没有额外状态零点或支撑。没有另行声称形式群、晶体或全参数识别。
- C3 的模 $\pi$ 公式、原完整光滑模型、全局正则性及辛形式均作为已知输入扣除。
  新算出的有限首 jet 可以据此判断该首诊断是否值得继续，但不授予新意或独立论文价值。

## Actual Verification and Open Risks

- 亲读 proof-writer、P03 的共同对象及目标、整数 brief §§2–3、原 D 证明，并定向实读 G 的完整末端延拓 Step 6。
- 本地只读 SymPy 精确计算核对了 (6)、(8)、(13) 及两个状态点的系数；未使用浮点拟合或 GPU。
  正文保留精确矩阵恒等式、整除证书与局部理想证明，计算成功不替代这些推导。
- 未新建辅助脚本；唯一产物是本作者文件。未改任何旧证明、失败、接受记录或候选合同。
- 仍需针对本件完整非作者检查，特别是 (14) 的局部选择独立性和 (15) 的全模型接口。
- 本件不分类其他素数、$a>1$、$m>1$、非简单 Hasse 根或奇异能级，亦不把主控的其他探针作为本证明前提。
- 未评分、立项、建锁、写稿或编译 PDF；没有重新提交旧 C1–C3。
