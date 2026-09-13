# Proof Package: qPI 高度二原 torus 的有限精确诊断 V1

日期：2026-09-09。执行席：`p31_qpi_height_two_diagnostic_v1`。
任务性质：有界独立数学诊断；非候选选定、非新意票、非 Route 评价。
`route_applicability: NOT_APPLICABLE`。

## Claim

固定 $p=2,a=2,m=1,s=i$、$\mathcal O=\mathbb Z_2[i]$、$\pi=i-1$，以及单位时间 $t$。
在原 torus $\operatorname{Spec}\mathcal O[x^{\pm1},y^{\pm1}]$ 上，使用原矩阵和原顺序
$$
I_4=[z^4]\operatorname{tr}A(i^3z)A(i^2z)A(iz)A(z),
\qquad \alpha_4=\tfrac14d_{\rm state}I_4.
$$
本报告证明其精确算式、模 $\pi^3/\pi^4$ 的有限展开，以及每个剩余态 $J=0$ 附近的完整**局部 torus** 系数理想。
允许为处理闭点作有限无分歧扩张；不改变原时间，不更换矩阵，不纳入四条末端线。

## Status

**PROVABLE AS STATED（上述有界命题）。**

结果不是“新 jet 使厚度增加”。精确形式确有模平方看不到的 $\pi^2$ 项，但完整局部理想已经等于
$$
\mathfrak c(\alpha_4)_P
=(\pi^2,j^3+\pi t,\pi j^2)_P
\qquad(\bar j(P)=0).
\tag{1}
$$
这里 $j=J_1(t)=y-x+x/y-t/x$ 是原函数。
式 (1) 是本报告新增推导，**不是把 Paper30 已接受的截断长度声明改写为完整长度声明**。
旧文只保守地没有确定完整厚度，并没有断言式 (1) 不成立；没有发现旧已接受定理的反例。

更强的“所有奇 $m$、完整八吹起模型的全部末端点”不在本报告证明对象内；其潜在升级在下文只列为有现成接口的直接代数推论待逐项核准。
所有高度、奇素数和奇异能级的完整临界概形仍 **NOT CURRENTLY JUSTIFIED** 于本任务。

## Assumptions

- $x,y,t$ 均为单位；微分只对两个状态变量取，固定 $t$。
- $P$ 是特征二剩余 torus 上满足 $J=\bar j=0$ 的点。
- 完成式涉及闭点时，先作足以承载其剩余域的允许无分歧扩张。
- 原矩阵严格取 Paper30 V4 §1 的公式，不以同谱矩阵替代。
- 本报告不依赖先有的完整理想结论，也不假设 CAS 给出的局部结构正确。

## Notation

$$
b=x(y-1),\quad u=t-b,\quad
j=y-x+x/y-t/x,\quad
r=(b-1)x-b=x(b-y),\quad
Q=t+\pi b+2ix.
$$
将原矩阵写成 $A(z)=C+zD+z^2E$，其中
$$
C=\begin{pmatrix}u&-x\\-(y-1)u&b\end{pmatrix},\quad
D=\begin{pmatrix}j-1&1\\j+b-1&1\end{pmatrix},\quad
E=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$
有 $\pi^2=-2i$ 和 $2=i\pi^2$。
$\mathfrak c$ 始终是原相对一形式两个系数所生成的理想，不是单方向系数、数值梯度或饱和理想。

## Proof Strategy

先按 19 个次数组合证明原迹系数恒等式，再微分。
用原函数 $(j,b)$ 的 Jacobian 证明其微分是局部可逆框架；把**实际两个系数**写出后，利用一条单位消元恒等式证明 $\pi^2$ 已在原理想中。
最后才讨论完成商及有限例外状态。

## Dependency Map

1. 精确 $I_4$：原矩阵、19 项次数分类、两个 $2\times2$ Cayley–Hamilton 恒等式。
2. 精确 $\alpha_4$ 和有限 jets：第 1 项的普通状态微分及 $i=1+\pi$。
3. 可逆框架：直接计算 $\det\partial(j,b)/\partial(x,y)$，仅使用 $txy\ne0$ 和 $J(P)=0$。
4. 完整局部理想：第 2–3 项给实际系数，随后执行下述两生成元引理。
5. 完成商：第 4 项加相对光滑局部坐标；不从 CAS 或旧截断长度直接推完整厚度。

## Proof

### Step 1. 原四块系数的精确手算

次数四的组合分三类：一个 $(1,1,1,1)$，六个 $(2,2,0,0)$ 排列，十二个 $(2,1,1,0)$ 排列。
因乘积降序且相位为 $i^{3k_3+2k_2+k_1}$，循环迹合并后恰有
$$
I_4=-\operatorname{tr}D^4-4\operatorname{tr}(EC^2)
+2\operatorname{tr}(ECEC)+4\operatorname{tr}(EDCD)
+4i\operatorname{tr}\bigl(E(D^2C-CD^2)\bigr).
\tag{2}
$$
第一类相位是 $i^6=-1$。
第二类四个相邻的 $E$ 给 $-4\operatorname{tr}(EC^2)$，两个相对的 $E$ 给 $2\operatorname{tr}(ECEC)$。
第三类在固定一个 $E$ 后，三个 $C$ 位置的相位为 $i,1,-i$，各有四个循环平移，给式 (2) 最后两项。

原矩阵直接给
$$
C^2=tC,\qquad D^2=jD+bI,\qquad CD+DC=tD+jC.
\tag{3}
$$
第三式也可由 $\det A(z)=z^3$ 的一次系数为零及二维极化恒等式得到；该行列式在附带脚本中亦从原条目核对。
由式 (3) 乘 $D$ 并代入 $D^2$，得到
$$
DCD=tjD+tbI-bC.
$$
令 $K=(DC-CD)_{11}$，则
$$
\operatorname{tr}D^4=j^4+4bj^2+2b^2,\quad
(DCD)_{11}=tj(j-1)+b^2,\quad
K=t+(b+2x)j+2r.
$$
最后一式把原 $j$ 代入后直接展开即可验证，没有商掉任何状态关系之外的因子。
将这些式子代入式 (2)，先得
$$
I_4=-j^4+4(t-b)j^2-4tj+4ijK+4b^2-2t^2,
$$
进而得到原不变量的精确恒等式
$$
\boxed{I_4=-j^4+4Qj^2+4\pi tj+8irj+4b^2-2t^2.}
\tag{4}
$$
不变量本身没有被平移或重新规范化。

### Step 2. 精确微分及首个新项

式 (4) 在特征零中微分除四，得到整系数 Laurent 一形式
$$
\boxed{\begin{aligned}
\alpha_4={}&(-j^3+2Qj+\pi t+2ir)\,dj
+\pi j^2db+2ij^2dx+2ij\,dr+2b\,db.
\end{aligned}}
\tag{5}
$$
因此这里的除四整性由精确等式直接证明。
为明确更高有限 jet，定义
$$
\Psi_0=(tj+r)dj+j^2dx+j\,dr+b\,db,\qquad
\Psi_1=(bj+r)dj+j^2dx+j\,dr.
$$
利用 $i=1+\pi$，式 (5) 等价于另一个精确等式
$$
\alpha_4=-j^3dj+\pi(tdj+j^2db)
+2\Psi_0+2\pi\Psi_1+4ixj\,dj.
\tag{6}
$$
故模 $\pi^3$ 保留到 $2\Psi_0$，模 $\pi^4$ 再保留 $2\pi\Psi_1$；最后一项被 $\pi^4$ 整除。
这些公式保留实际 $t$，没有把整个时间 jet 换成其剩余值。

在固定这组原函数提升后，首个新的 $\pi^2$ 系数是 $\bar\Psi_0$。
其沿 $X=(J=0)$ 的**切向剩余微分**为
$$
\bar\Psi_0|_{\Omega_X^1}=b\,db.
\tag{7}
$$
这里是先除掉已知 $\pi^2$ 因子并取剩余，再限制到切向；不是把含 $\pi$ 的原一形式直接拉回特征二纤维而称其非零。
第 3 步证明 $db$ 在此处确为切向基，因此式 (7) 一般非零。

### Step 3. 原 torus 上的实际可逆框架

设
$$
W=j_xb_y-j_yb_x=xj_x-(y-1)j_y.
$$
直接把 $j$ 的偏导代入并模二化简，得到恒等式
$$
\bar W=(1+y^{-1})J+\frac{t}{xy}.
\tag{8}
$$
在 $P\in X$ 上，$\bar W(P)=t/(xy)$ 是单位。
因此 $W\in\mathcal O_{\mathcal U,P}^{\times}$，$(dj,db)$ 是原相对 cotangent 模的可逆框架；这同时证明此 torus 能级的光滑性。
在该局部环内
$$
dx=\frac{x\,dj-j_y\,db}{W},\qquad
dr=(b-1)dx+(x-1)db.
$$
令 $\ell=j+b-1$，并定义实际正则函数
$$
\begin{aligned}
a_0&=Qj+ir+\frac{ij\ell x}{W},\\
b_0&=b+ij(x-1)-\frac{ij\ell j_y}{W}.
\end{aligned}
$$
式 (5) 在上述可逆框架中精确为 $\alpha_4=F\,dj+G\,db$，其中
$$
F=-j^3+\pi t+2a_0,\qquad G=\pi j^2+2b_0.
\tag{9}
$$
再用 $2=i\pi^2$，取
$$
A_0=i(a_0-j^3),\qquad B_0=ib_0,
$$
便得**实际两系数**的精确形式
$$
F=j^3+\pi t+\pi^2A_0,\qquad
G=\pi j^2+\pi^2B_0.
\tag{10}
$$
这里没有从“模 $\pi^2$ 理想恰有两生成元”反推一组未证明可逆的实际系数；式 (9) 是从原矩阵微分和原 Jacobian 直接得到的。

### Step 4. 两生成元单位消元引理

**引理。** 在局部环 $R$ 中，设 $\pi,j$ 属于极大理想、$\tau$ 是单位。
若实际两个元素为
$$
f=j^3+\pi\tau+\pi^2a,\qquad g=\pi j^2+\pi^2b,
$$
则
$$
(f,g)=(\pi^2,j^3+\pi\tau,\pi j^2).
\tag{11}
$$
**证明。** 精确相减给
$$
\pi f-jg=\pi^2(\tau+\pi a-jb).
$$
括号模极大理想等于非零的 $\bar\tau$，故可逆，因而 $\pi^2\in(f,g)$。
由 $f,g$ 减去其 $\pi^2$ 余项，得到右边另两个生成元；反向包含由给定表达式逐项成立。证毕。

对式 (10) 应用引理即证明式 (1)。
引理甚至不需要 $2=i\pi^2$；这一圆分关系只用于从原精确系数推得式 (10)。
“有更高项”与“更高项改变理想”在本例确实是两件不同的事。

### Step 5. 本次已证明的完成商和基参数作用

在闭点 $P$ 作允许无分歧扩张并完成，式 (8) 允许取 $z=j$ 以及沿曲线的参数 $w$。
因为本次已独立证明 $\pi^2\in\mathfrak c(\alpha_4)$，**本次有界对象的完整局部商**现可计算为
$$
\frac{\widehat R}{\mathfrak c(\alpha_4)}
\simeq
\frac{k(P)[[w,z,\epsilon]]}{(\epsilon^2,z^3+\epsilon T,\epsilon z^2)}
\simeq k(P)[[w,z]]/(z^5),
\qquad \pi\longmapsto z^3/T,
\tag{12}
$$
其中 $T=\bar t\ne0$。
后一同构由先消去 $\epsilon=z^3/T$ 得到：$\epsilon z^2$ 变成 $z^5/T$，而 $\epsilon^2$ 给出的 $z^6/T^2$ 已是其倍数。
因此它在本地沿 $w$ 自由秩五，$\pi$ 非零而 $\pi^2=0$。
这仍不是闭点总 Artin 长度（$w$ 仍在），不是全 torus 的全局直积同构，更不是四条末端线已独立检查的结论。
式 (12) 的完整性来自第 4 步新证明，而不是来自旧 Paper30 的长度措辞。

### Step 6. $t=1$ 和有限例外状态

式 (7) 的切向新系数仅在 $b=0$ 处消失。
在 torus 上 $b=0$ 等价于 $y=1$；此时 $J=1-t/x$，所以 $X$ 上唯一此类几何点是
$$
P_0=(\bar t,1).
$$
由于 $db$ 在 $X$ 上为局部基，$b$ 在 $P_0$ 的零是一阶零。
当 $t=1$，该点为 $(1,1)$。
这只是选择好的实际框架中第二阶切向系数的单点消失，**不是**完整临界理想、纵向厚度或两方向公共赋值的例外。
式 (1) 在该点和其他 $J=0$ torus 点完全相同。

对任意允许无分歧状态提升，$j\in(\pi)$。
式 (9) 中 $F$ 的 $\pi t$ 项阶为一，其余 $-j^3$ 和 $2a_0$ 的阶至少三、二；故两方向公共阶恰为一。
通常 $\bar b\ne0$ 时，$G$ 的阶恰为二，因为 $\bar b_0=b$；在 $P_0$ 上 $G$ 的阶至少三，但 $F$ 仍为一阶。
例如原精确提升 $t=x=y=1$ 满足
$$
\alpha_4|_{(1,1)}=(i\pi)\,dx+0\,dy=(-1-i)\,dx,
$$
其公共阶仍是一，未整除微分 $dI_4$ 的公共阶为五。

## Corrections or Missing Assumptions

没有修改原问题或原矩阵。
必须纠正的推论方式是：“看到模平方商的长度五”本身不授权声称完整长度五。
本报告先证明原实际两系数的可逆框架和 $\pi^2$ 包含，才得到有界局部完整结论。

## Paper30 首 jet 接口核查（不是本报告的全模型定理）

本人全文读取 V4 `sections/01-introduction.tex` 和 `sections/08-two-jets.tex`。
后者实际准确文件名不是 `08-characteristic-two.tex`。
§8 第 510–525 行不仅列出了截断理想，也给出实际截断一形式
$$
(j_i^3+\epsilon\widetilde T+\epsilon j_i^2A_i)\,dj_i
+\epsilon j_i^2B_i\,\theta,\qquad B_i\text{ 为单位}.
$$
若该处框架和 $A_i,B_i$ 在所考察原局部环中取提升，实际原系数记为 $f,g$，则
$$
G=B_i^{-1}g,\qquad F=f-A_iG
$$
是行列式为 $B_i^{-1}$ 的可逆行变换。
其模平方恰为 $(j_i^3+\pi\widetilde T,\pi j_i^2)$，所以第 4 步引理适用。
这说明“可逆提升”需要的并非凭空补充的生成元基假设：§8 已显示了足够的实际形式级接口。

不过，本任务没有再次逐项审核全部奇 $m$ 的上游 form regularity、完整相对 cotangent 框架及四个末端局部环的同对象输入。
因此这里只标为：**全模型/全奇 $m$ 高度二升级有一个直接的标准局部消元路线，需原接口逐项核准；本报告独立定理仍限 $m=1$ 原 torus。**
它不因本次短引理自动获得新意票；即使全接口核准，也应先从第31篇潜在“完整高度二厚度”增量中扣除这一直接推论。

## Exact Computation Evidence

附带脚本：[exact_alpha4.py](p31-height-two-diagnostic-v1/exact_alpha4.py)。
执行命令：`python -u docs/research-batch07/p31-height-two-diagnostic-v1/exact_alpha4.py`。
实际退出码为 0，精确检查全部通过：原行列式、19 项原迹系数、两份压缩式、两个状态微分系数、原 Jacobian、实际框架、单位消元恒等式、模三/模四余项、$(1,1)$ 精确点值。
脚本不用浮点、不拟合、不读写数据、不安装、不联网；使用现有 SymPy，小型 CPU 运行。
早先一次临时全展开后通用因式分解预探索约一分钟仍未完成，已定点终止该自有进程；随后用手算的压缩恒等式核验，没有把未完成尝试报作成功。
CAS 只重复验证有限恒等式；局部框架、单位消元和完成商的论证全部在上文。

## Open Risks

- 本报告无新意判断，无全球先例排除，无论文容量判断；独立来源席另行负责。
- 没有证明全高度、奇素数、任意 $m$、奇异纤维、额外分歧状态或全局 critical scheme。
- 四条末端线未在此任务重审；不可把局部 torus 证明升级为完整八吹起模型的证明。
- 单点 $P_0$ 只影响一条具体框架中的新切向系数，不构成新的局部理想类型。
- 本次结果的核心方法是标准两生成元消元。更高 $\pi$ 系数虽真实非零，在当前完整理想中已经被吸收；不支持凭这一方向单独建立第31篇候选。

有界任务完成后停止。未创建 `papers/31`，未编译，未修改任何已接受源或冻结记录。
