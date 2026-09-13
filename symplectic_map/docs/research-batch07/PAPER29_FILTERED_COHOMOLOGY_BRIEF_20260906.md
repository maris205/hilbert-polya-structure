# Paper29 新候选：滤过多项式余同调与有限周期检验

日期：2026-09-06。候选 ID：`filtered_henon_cohomology_finite_period_tests_v1`。
这是与旧周期乘子迹坐标不同的新问题，不是第六候选的增补。
批次仍为2/5；本文件不是正式论文、科学锁或PDF验收。

## 1. 当前状态与统一问题

作者已交付两个完整证明报告，两个新独立数学检查也已完成。主控已全文
读取实际证明和最终检查稿，并核对输入身份；原稿没有需要修补的定理级
缺口。现将同一完整包提交两名新的独立候选评审。本候选目前没有新意、
价值或22–30页容量PASS；数学通过不是候选或产物通过。

拟题：**Filtered polynomial cohomology and finite periodic tests for
symplectic Hénon maps**。

问题是：给定一个辛Hénon复合与任意多项式观测量，如何完全刻画、定量计数
并由有限周期数据检测其全局加法余同调障碍？其应用是判定指定参数保持
辛扩张中额外有理积分的存在，得到完整固定域，而不是只找到几个积分。

三个互相依赖的核心是：普通次数滤过的严格控制、该滤过中的精确障碍
维数、完整周期概形给出的有效检测。scalar单变量刚性与四维固定域是同一
余边界方程的对象专属应用。它们不是从旧trace-chart、Galois或次数矩阵
报告拼入的补页材料。

## 2. 实际输入与归属

以下文件均在 `docs/research-batch07/` 下；哈希绑定本次读到的完整内容。

| 输入 | SHA256 |
| --- | --- |
| `PAPER29_CYCLIC_COHOMOLOGY_FINITE_PERIOD_PROBE_20260906.md`，408行 | `0f3ce169e3c62bcde926f3d0f5661dad80dab534394dddaab5f3d24bf8e767b6` |
| `PAPER29_HENON_COHOMOLOGY_PROBE_20260906.md`，447行 | `3f9a1be49ff07bbadd4636f55745d1e31572f2a8988a1402828429edd9ea92d0` |
| `PAPER29_POLYNOMIAL_COHOMOLOGY_LITERATURE_PREFLIGHT_20260906.md`，242行 | `290ae64e73f22d6b934cf476596e05a8a663d0834a9fea4f46178185146358ab` |
| `PAPER29_COHOMOLOGY_EXACT_CHECKS_20260906.md` | `725e3aa0cc2788f005a49b4942dd9d36ce4bcb1ac9aebbc41e043b4170d73e1c` |
| `probes/henon_cohomology_exact_probe_20260906.py` | `a5bdf33b092ca86e14800ebc30eff4dd609fdb875796741b46fe2fb66a15e142` |

两个证明作者与主控共同建立并相互核证，不因此冒称独立外审已完成。
新独立检查稿已在本文件第10节登记。两份作者报告中的重复scalar/multi
基础证明在候选中只占一个位置；不是把855行机械相加估算正文。

## 3. 固定数学对象

设 $K$ 为特征零域，$k\ge1$，$p_0,\ldots,p_{k-1}\in K[T]$，
$d_i=\deg p_i\ge2$。按周期$k$延拓这些数据。令
$$
H_i(x,y)=(p_i(x)-y,x),\qquad
F=H_{k-1}\circ\cdots\circ H_0,\qquad
\delta=\prod_{i=0}^{k-1}d_i,\qquad \sigma=F^*.
$$
全部首项系数任意非零，下阶系数任意，不加双曲、单根或泛型条件。
定义 $X_0=x,X_{-1}=y$，以及双向递推
$$p_i(X_i)=X_{i-1}+X_{i+1}.$$
宏映射作用是 $\sigma X_i=X_{i+k}$，不能换成shift-$1$。

设 $A=K[x,y]$，$V_D=A_{\le D}$，并令
$$
\mathcal H=A/(\sigma-1)A,\qquad
\mathcal H_D=\operatorname{im}(V_D\to\mathcal H),\quad
\mathcal H_{-1}=0.
$$
这是向量空间余商及其普通坐标次数滤过；$(\sigma-1)A$不是被宣称为理想。
不把它叫作新的坐标无关共轭不变量、de Rham或层上同调。

## 4. 核心I：完整障碍与保次数原函数

有限支撑有界指数词 $M_e=\prod_iX_i^{e_i}$、$0\le e_i<d_i$构成基。
令 $w_0=w_{-1}=1$，
$$
w_i=\prod_{h=0}^{i-1}d_h\ (i\ge1),\qquad
w_i=\prod_{h=i+1}^{-1}d_h\ (i\le-2),\qquad
\mu(M_e)=\sum_i e_iw_i.
$$
基词的最高项由两条射线的唯一混合进位制编码，因此
$$\deg\sum_e c_eM_e=\max_{c_e\ne0}\mu(M_e).$$
这不是形式字长替代原坐标次数。

基被$\sigma$置换，非恒定基轨道无限。余边界条件是正规形常数系数为零，
且每个shift-$k$词轨道的系数总和为零。对满足条件的输入，沿每个轨道
累计系数得到唯一模常数的原函数。轨道次数的离散凸性进一步给出
$$
g\in V_D\cap(\sigma-1)A\quad\Longrightarrow\quad
g=\sigma f-f\text{ for some }f\in V_D.
$$
在scalar子族中，$f=y^D$、$g=x^D-y^D$证明这个统一次数界逐$D$可达；
不由此声称每个固定的多phase宏映射均具有同一达界例子。

整合时只需一个无极点引理：自由基轨道排除每个正迭代的非恒定
多项式特征函数，从而排除周期仿射曲线；有理函数若差分为多项式，其
有限仿射极除子必须被置换，故只能无极点。这将有理原函数降为多项式，
也给出 $K(x,y)^F=K$。这条多phase整合推论单列在独立检查中核证，
不是给scalar和multi各写一套同样的无周期曲线证明。

基、包裹、置换及轨道系数求和的既有部分必须扣除，见第8节。
本层待评价增量主要是严格普通次数滤过与保次数原函数，而不是重命名基。

## 5. 核心II：精确Hilbert级数

对负向数字写 $B=\delta Q+R$，$0\le R<\delta$。
若 $e_j=e_{-j}$、$1\le j\le k$，则
$$
R=\sum_{j=1}^k e_j\prod_{h=1}^{j-1}d_{k-h},\qquad
\rho(R)=\sum_{j=1}^k e_j\prod_{h=0}^{k-j-1}d_h.
$$
空乘积为一。$\rho$是在$\{0,\ldots,\delta-1\}$上的置换；不同基数时
不假设它为对合。基词及宏平移后的普通次数分别是
$$\mu=A+\delta Q+R,\qquad \mu'=\delta A+Q+\rho(R).$$
定义 $C_\rho(t)=\sum_{R=0}^{\delta-1}t^{\max(R,\rho(R))}$。保次数
原函数使余边界像在滤过上严格，通过计数$\max(\mu,\mu')$得到
$$
\operatorname{Hilb}_{\operatorname{gr}\mathcal H}(t)
=1+\frac1{(1-t)^2}
-\frac{C_\rho(t)+2t^\delta/(1-t)}{1-t^{\delta+1}}.
$$
这是关联分次维数的级数，不是累计维数级数。scalar只作短特例：
$$
\operatorname{Hilb}_{\operatorname{gr}\mathcal H}(t)
=1+\frac{t(1+t+\cdots+t^{d-2})}{(1-t)(1-t^{d+1})},
\qquad
\dim\mathcal H_D=\frac{d-1}{2(d+1)}D^2+O_d(D).
$$
$(d_0,d_1)=(2,2)$与单因子$d=4$具有相同宏次数，但其Hilbert级数之差为
$$(t-t^2)/(1-t^5)\ne0.$$
结论仅是指定坐标滤过可以区分这两个构造；不主张完整恢复multidegree。

## 6. 核心III：单周期概形检测及尖锐稳定阈值

对 $N=kn\ge3$，完整固定点概形环为
$$
A_N=K[Z_i:i\bmod N]/(p_i(Z_i)-Z_{i-1}-Z_{i+1}),
\qquad \dim_KA_N=\delta^n.
$$
周期数据是 $S_ng=\sum_{j=0}^{n-1}g\circ F^j$在此环中的元素。
定义$L(g)$为正规形每个非恒定词支撑直径的最大值，不是不同词之间的距离。
若 $N>2L(g)$，则
$$
S_ng=0\text{ in }A_N
\quad\Longleftrightarrow\quad
g=(\sigma-1)f\text{ with }f\in A.
$$
有理版本使用第4节的无极点整合推论。唯一大循环间隙保证不同无限
shift-$k$轨道不混叠；这一点是有限周期证书的关键，不是仅重述wrapping。

精确最坏跨度为
$$L_{\rm ph}(D)=\max\bigl(\{b-a:a<b,\ w_a+w_b\le D\}\cup\{0\}\bigr).$$
端点词$X_aX_b$给出可达性。于是每个满足$kn\ge3$、$kn>2L_{\rm ph}(D)$
的宏周期对全部$\deg g\le D$都有效。可选
$$
n_{\rm eff}(D)=\left\lceil\frac{\max\{3,2L_{\rm ph}(D)+1\}}k\right\rceil,
\qquad \delta^{n_{\rm eff}(D)}\le\delta^4D^4\quad(D\ge1).
$$
scalar时对$D\ge2$，$h=\lfloor\log_d(D/2)\rfloor$给精确公式
$$L_d(D)=1+2h+\mathbf1_{\{D\ge(d+1)d^h\}}.$$
$D=0,1$时跨度为零。简单但非最小的统一选择为
$n=4\lfloor\log_dD\rfloor+3$，代数长度$\le d^3D^4$。

当$d\ge3$时，令
$$g_r=X_{-r-1}X_r^2-X_{-r-1}^2X_r,\quad r\ge1.$$
其次数$D_r=3d^r$，不是余边界，但在$n=4r+2$上通过概形零测试。
因此对“所有$n\ge N(D)$都统一检测全部次数至多$D$输入”的最终阈值，
$4\log_dD+O(1)$中的首项常数$4$不能一般降低。这不排除特别挑选的
更短单周期、多个短周期联合检测，更不是算法下界。

scalar二次可用$n\ge\max\{3,2L\}$；临界双点词的稳定子只带来非零倍数。
其$n=2L-1$失败例子只取$L\ge2$、$n\ge3$，不丢失小周期范围。
多phase不自动享有这一改进：$k=2,N=6,L=3$时，
$X_0X_3-X_3X_6$非宏余边界却包裹为零。一般定理保留严格不等式。

不把概形零升级为仅几何点值零，也不称$n=1$幂零例子为长周期反例。
$D^4$只计检测代数长度。保次数原函数另给$O(D^2)$未知数的直接线性法，
所以不得宣称周期方案为最小或最快求解算法。

## 7. 同一余边界问题的scalar刚性与辛扩张应用

对 $H_p(x,y)=(p(x)-y,x)$、$\deg p\ge2$，完整分类为
$$
f\circ H_p-f=R(x),\quad f\in K(x,y),\ R\in K[x]
\quad\Longleftrightarrow\quad
f=c(x-y)+c_0,\ R=c(p(x)-2x).
$$
无极点归约之后，用两个反射与导数最高次支撑约束证明必要性。
这不是有界次数Ansatz；特征零和保面积系数$-1$均为精确范围。

应用取$V\in\mathbb C[t,a]$、$\deg_tV\ge3$，
$$
a'=a,\qquad s'=s+V_t(t,a),\qquad t'=t+s',\qquad r'=r+V_a(t,a),
\qquad\omega=dt\wedge ds+da\wedge dr.
$$
在$K=\mathbb C(a)$上，$x=t,y=t-s$使底映射成为$H_{2x+V_t}$。
Karr的加性扩张常数域判据把额外积分转为上述单变量余边界条件，得到
$$
\mathbb C(t,s,a,r)^F=
\begin{cases}
\mathbb C(a,r-A'(a)s),&V(t,a)=W(t+A(a)),\ A\in\mathbb C[a],\ W\in\mathbb C[t],\\
\mathbb C(a),&\text{否则}.
\end{cases}
$$
自含系数证明将互素分子分母各自首一化后，还须保留首项系数比；
同一个半不变量倍数使该比属于底常数域。这一完整补句已在独立检查
§7.2核证，不把它省去后误称只证明了首一部分。
由$V_a=c(a)V_t$比较最高两阶系数，严格推出$c=A'$与多项式平移形式。
例外的$(u,\rho)=(t+A(a),r-A'(a)s)$是实际全局多项式辛解耦。
但$\{a,\rho\}=1$，两种情况下均不存在两个独立、Poisson对易的有理积分。
这最后一句只是完整固定域的短推论，不另算一项大创新。

平移可消掉底族参数，不等于整个lift出现额外积分。纯参数势项$+a$
便可能把$\rho'=\rho$改为$\rho'=\rho+1$。缩放isotrivial底族也不必落入
平移例外；不把本结果称为全部isotriviality或任意辛扩张的分类。

## 8. 前作扣除与本地非碰撞

Bousch的1992未发表作者稿已由主控与查新代理全文核读。二次有限/无限
基、非约化意识、包裹与shift都已有；轨道系数求和是其直接线性代数应用。
一般次数和多phase基的推广是本题必要工具，不能仅凭参数变多占据一项主创新。

Karr/Schneider的扩张常数判据与Cerveau–Déserti的次高系数降维机制均归前作。
mixed-radix reversal本身也是既有工具，候选增量是它控制的精确次数滤过计数。
已有有限Livšic文献研究近似余边界；2026年官方报告还宣布指数精度改进，
不得错误声称该领域只知多项式误差。当前差别在精确函数类别、完整单周期
概形及严格零，而不是一个术语或渐近尺度名称。

有界一手检索未定位当前Hilbert公式、保次数原函数、有效单概形iff及
所述尖锐稳定阈值的直接覆盖。这不是穷尽性首创证明。候选评审仍须判断
它们扣除已有机制后是否有独立新意与研究价值。

本地组合比较沿用Papers1–28范围审计，SHA256
`e6699e6d8ce81952ee906a8cabb925373b9a5a9d8d97f7115b95980e07aac9f3`，
并由主控定向核对README、P13实际轨道和/有限覆盖函数域段、P20问题书和
P27/P28已接受源中的主张。P13的有限原始周期覆盖及其轨道函数域生成
不是$K[x,y]/(F^*-1)K[x,y]$；P20–28的次数矩阵、权空间selector与monodromy
不是原相空间余边界或固定域。旧六个P29候选的全碰撞动量纤维、次数取消、
中心化子与乘子迹jet问题均不被复用为这里的贡献。

## 9. 不重复的拟写组织与容量审查规则

拟写以下完整结构，但尚未排版，不预定或冒充实际页数：

1. 问题、主定理与确切先例差分；定义函数类别、滤过与周期数据。
2. 多phase轨道代数与有限概形：只证明一次统一基与双向同构。
3. 普通次数的混合进位制、轨道离散凸性、完整障碍及保次数原函数。
4. 多phase Hilbert计数；scalar简化与同总次数差异作为短例子。
5. 无混叠及单概形检测；不是重新证明第2节的有限基。
6. 精确跨度、对数周期量化、尖锐最终阈值与binary相位反例。
7. scalar单变量必要性；使用已建立的无极点引理而不重证全部基础。
8. 参数保持辛lift的全固定域、精确平移例外及必要边界；简短结语。

这是否自然达到22–30页仍须独立判断。不得把scalar和multi通用证明各写
一遍、把所有中间等式单开章节、扩写Bousch/Karr背景、重复反例或CAS表，
也不得拼入已停止的非可积性或trace图表。必要已知工具可以自含但不冒充新增。

评审版式假设是匿名英文单栏 `article`，11pt、letterpaper、四边1英寸，
常规行距、定理与陈列公式间距；参考文献另起页且不计正文。不能用缩放、
额外空白或大字号调整证据容量。估计不是PDF测量，也不是不能达到某页数的定理。

每份新独立候选报告必须对**同一完整包**分别满足：新意至少7.5/10、研究
价值至少7.5/10、证明可信度至少9/10，且能可信支持22–30页实质正文。
两个报告均要满足全部条件，不能混合各自最好的分项。通过只准予下一阶段
正式研究细化/写作；实际本地构建和独立PDF终审仍未执行。

## 10. 独立检查接收栏

两名未参与作者构造的新审查员互不读取或交流对方结论，分别完整核读实际
scalar与multi输入。主控现已全文读取两份最终报告：

| 独立输入 | SHA256 | 数学结论 |
| --- | --- | --- |
| PAPER29_COHOMOLOGY_SCALAR_INDEPENDENT_CHECK_20260906.md，193行 | f87d3a19aee0bbc363c588e44e7a90e7a7ba853c314fc8ef18e13f0ce3096abd | 全部所列scalar命题PASS；无需定理级修正 |
| PAPER29_COHOMOLOGY_MULTIPHASE_INDEPENDENT_CHECK_20260906.md，281行 | af20049ae1cdf6163a78b24a4a4a66f8f9f3ffe09e73274b6d5d21dc0ac85c39 | 原稿21项与有理整合推论均PASS；无需定理级修正 |

整合只落实已核证的三项明确书写：向量空间而非商环、Karr首项系数比、
binary小周期与最终统一阈值的完整量词。第4节multi有理推论由第二报告
§8完整独立证明；以后不用重复scalar反射无曲线证明凑页。
这些非阻断澄清均不改原证明输入，也不需要重跑未变的有限矩阵案例。

本次采用技能所允许的实际可用独立代理fallback，理由是指定Codex MCP
审查通道不可用；没有冒称调用特定外部模型或拥有外部threadId。
本文件及全部绑定输入在两份候选评价期间保持不变。候选评价应检查实际
新增证据和仍未裁定的新意、价值、凝聚性、22–30页容量，而非重开旧停止项目。

Route A/B：`NOT_APPLICABLE`。本题没有Riemann动力行列式、素数时钟或
Hilbert–Pólya主张。全部操作限于本地研究与公开文献阅读，不产生外部发布效力。
