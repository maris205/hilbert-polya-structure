# Paper30 整系数候选 V1：qPI 反典范上同调与圆分特化

日期：2026-09-09。组织者：主控 `/root`。
类型：新整数问题的首次完整正式候选简报；不是旧T1–T7重评、论文稿、项目准入或PDF。
拟题：*Integral anticanonical cohomology and cyclotomic specialization of q-Painlevé I*。
本件完整保留[Phase A的C1–C3](PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md)，
具体必要证明另由同版证明图定位，冻结字节由共同清单绑定。

## 1. 一个中心问题及其与旧失败的关系

研究原qPI八截面曲面的反典范线性系，沿整个整数参数空间及根单位坏素位如何变化。
中心不是给旧有限域周期计数换标题，而是计算
$$R\Gamma(S,\mathcal O(nD))\quad\text{在}\quad
R=\mathbb Z[q^{\pm1},\tau^{\pm1}]\text{上对全部 }n\ge0$$
的真实整数结构，并把它落实到同一原pencil与原状态微分的圆分特化。

需要回答三个互相连接的问题：

1. 边界节点复形只给逐层商时，曲面推送中的扩张是否消失，能否控制任意非平坦／非约化基变换？
2. 原精确阶$mp^a$在$p$上降为$m$阶时，原完整pencil、所有纤维概形重数和原截面空间如何特化？
3. 已约化积分成为$p^a$次幂后，先在整数模型除以$p^a$再约化的状态微分是什么，是否在完整开放模型正则？

主控认为这些给出了值得完整评价的具体结构问题；这不是已通过独立科学价值门。
独立查新为**7.0/10、PROCEED_WITH_CAUTION**，三项finding均MEDIUM、method均LOW，C1最强。
该意见和全部来源扣除完整进入共同包；不以新量词的数量或证明正确性上调新意。

旧qPI完整V2的T1–T7数学接受、正式7.6／7.4双份合取FAIL，以及旧查新6.0／6.5全部保留。
本件不替旧V2授准入，也不删除其周期、原分箱或准确临界重数来把旧候选缩成可过稿。
它固定的是另一个完整问题；只消费旧结论中本整数问题真实需要的几何基础，且这些必要证明仍须全部正文给出。
不能把旧V2有利分项搬到本件、不能平均分数、不能将C1–C3拆成多篇。

## 2. 原对象、参数与规范

### 2.1 无关系整数族及四条末端线

在$\mathbb P^1_R\times_R\mathbb P^1_R$上按以下四簇截面顺序吹起，得到$S/R$。
其中$q,\tau$始终为单位，不满足根单位关系。

| 簇 | 实际中心次序 | 最后局部图 |
|---|---|---|
| 1 | $(x^{-1},y-1)=(0,0)$ | $x=u^{-1},\ y=1+uv$ |
| 2 | $(x,y^{-1})=(0,0)$；随后$xy=\tau$的例外截面 | $x=u(\tau+uv),\ y=u^{-1}$ |
| 3 | $(x,y)=(0,0)$；第一次例外与$y=0$的交截面；随后$x^2/y=\tau$ | $x=u(\tau+uv),\ y=u^2(\tau+uv)$ |
| 4 | $(x^{-1},y^{-1})=(0,0)$；随后$y/x=q$的例外截面 | $x=[u(q+uv)]^{-1},\ y=u^{-1}$ |

这等价于先做四次边界节点吹起，再在四个**不同分量**的单位坐标$1,\tau,\tau,q$处吹起。
不因坐标相等或剩余根单位降阶合并中心。总次数为$1+2+3+2=8$。
$D$是四条原坐标边界和四条中间节点例外的最终严格变换之和；
$D=-K_{S/R}$，每个几何纤维是八个$(-2)$分量的SNC环。
令$L_n=\mathcal O_S(nD)$、$\mathscr N=\mathcal O_D(D)$、$\mathcal V=S\setminus D$。
$\mathcal V$包含原环面及四条完整末端仿射线；后者不是被删除的边界状态。
完整环面补集$E$则包含$D$和四条末端例外曲线；$E$与$D$不可混用。

### 2.2 原矩阵、原积分与全共振系数

固定辅助规范$w=1$，原矩阵为
$$
A(z)=A_0+zA_1+z^2\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
A_0=\begin{pmatrix}
\tau+x-xy&-x\\
\tau+x-\tau y-2xy+xy^2&x(y-1)
\end{pmatrix},
$$
$$
A_1=\begin{pmatrix}
y-x+x/y-1-\tau/x&1\\
y-2x-1+xy+x/y-\tau/x&1
\end{pmatrix},\qquad \det A(z)=z^3.
$$
乘积次序固定为$M_j(z)=A(q^{j-1}z)\cdots A(qz)A(z)$，不交换矩阵因子。
在任意域中，令$q=\xi$精确阶为$j$、$\tau=t\ne0$，JR原积分由
$$\operatorname{tr}M_j(z)=t^j+I_{j,\xi}z^j+z^{2j},\qquad
\det M_j(z)=(-1)^{j+1}z^{3j}$$
固定，等价于$I_{j,\xi}=\operatorname{tr}M_j(1)-(t^j+1)$。
原首项为$I_{j,\xi}=-t^jx^{-j}+O(x^{-j+1})$。
这些是JR的已知输入，不是本件首次构造的积分或谱恒等式。

在整个$B_j=R/(1-q^j)$上则使用
$$C_j=[z^j]\operatorname{tr}M_j(z).$$
它在非本原分支可以有不同的其他谱系数，不能偷换为$\operatorname{tr}M_j(1)-(\tau^j+1)$。
这一区别对坏素数相交的共振整数基是必要的。

原方程的一步为$F_t(x,y)=(qt/(qx-y),qx/y)$、$t\mapsto qt$，
这里只用于标定原qPI对象，不附加新回返、周期或全闭纤维动力结论。

## 3. 完整科学合同 C1–C3

### C1. 通用整数上同调与全共振扩张分裂

对每个整数$n\ge0$，在无关系$R$上
$$
H^0(S,L_n)=R\langle1\rangle,\qquad
H^1(S,L_n)\simeq\bigoplus_{j=1}^n R/(1-q^j),\qquad H^{i\ge2}(S,L_n)=0.
\tag{C1a}
$$
边界递增产生的每个短正合列
$$0\longrightarrow H^1(S,L_{j-1})\longrightarrow H^1(S,L_j)
\longrightarrow R/(1-q^j)\longrightarrow0$$
均分裂。必要的具体截面结论是：$C_j$在$S_{B_j}$上延拓为$L_{j,B_j}$的完整截面，
其边界限制处处生成$\mathscr N^j_{B_j}$；在真实$x^{-j}$标架中的系数为
$$(-\tau)^j q^{j(j-1)/2}\in B_j^*.$$
不能只在特征零正规化分支或约化点集上验证这一结论。

存在保留真实常数项的非典范派生同构
$$R\Gamma(S,L_n)\simeq R[0]\oplus
\bigoplus_{j=1}^n[R\xrightarrow{1-q^j}R],\tag{C1b}$$
每个两项复形放在上同调次数$0,1$。
对每个固定$n$选取一次这样的同构后，对所有交换$R$-代数$A$自然得到
$$R\Gamma(S_A,L_{n,A})\simeq A[0]\oplus
\bigoplus_{j=1}^n[A\xrightarrow{1-q_A^j}A].\tag{C1c}$$
包括非平坦、非约化和非Noetherian的$A$，因此
$$H^0(S_A,L_{n,A})\simeq A\oplus\bigoplus_{j=1}^n\operatorname{Ann}_A(1-q_A^j),
\quad H^1(S_A,L_{n,A})\simeq\bigoplus_{j=1}^n A/(1-q_A^j),\quad H^{i\ge2}=0.$$
第一个$A$是真实常数子模，不声称普通$H^0$非平坦基变换总是同构。
同一模的直接推论为
$$\operatorname{Fitt}_0H^1(S,L_n)=
\left(\prod_{j=1}^n(1-q^j)\right)=
\left(\prod_{d=1}^n\Phi_d(q)^{\lfloor n/d\rfloor}\right).\tag{C1d}$$
$n=0$的直和为空、Fitting理想为单位理想。
非典范选择不附加跨$n$的派生过滤相容、乘法、cup product、动力作用或相对对偶同构。
C1b–d的形式工具与后果不各算一次方法创新。

### C2. 圆分原完整pencil与全部扭子模

任取素数$p$、整数$a,m\ge1$、$p\nmid m$；记$N=p^a$、$r=mN$、$s=\zeta_r$。
令$\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}$、$\mathfrak p\mid p$，
$\pi$为任一DVR参数、$e=v_\pi(p)$、$\kappa=\mathcal O/(\pi)$。
任取$t\in\mathcal O^*$，令$q=s,\tau=t$特化得到相同的$(\mathcal S,\mathcal D)$。
$\eta=\bar s$精确阶为$m$，$J=I_{m,\eta}(x,y;\bar t)$，$\mathcal L_n=\mathcal O(n\mathcal D)$。

$\mathcal S/\mathcal O$光滑射影、相对维数二；原$1,I_r$生成无基点pencil，给射影平坦态射
$$f_r:\mathcal S\longrightarrow\mathbb P^1_{\mathcal O},\qquad
f_r^{-1}(\infty)=r\mathcal D.$$
其泛纤维上是原完整最小$r$阶pencil，剩余态射严格为
$$\bar f_r=\operatorname{Pow}_N\circ f_m,\qquad f_m=J,\quad
\operatorname{Pow}_N([b_0:b_1])=[b_0^N:b_1^N].\tag{C2a}$$
幂态射保持$\kappa$常数，不混同绝对Frobenius。
每个有限几何剩余能级$c=h^N$的概形纤维为$N f_m^{-1}(h)$，
其中小阶完整纤维几何整且约化；无穷纤维准确为$r\bar D$。

原截面空间和实际特化像分别为
$$H^0(\mathcal S,\mathcal L_r)=\mathcal O\langle1,I_r\rangle,\qquad
H^0(\bar{\mathcal S},\bar{\mathcal L}_r)=\kappa\langle1,J,\ldots,J^N\rangle,$$
$$\operatorname{im}\bigl(H^0(\mathcal S,\mathcal L_r)\otimes\kappa
\longrightarrow H^0(\bar{\mathcal S},\bar{\mathcal L}_r)\bigr)
=\kappa\langle1,J^N\rangle.\tag{C2b}$$
特化余核维数为$N-1$，不把它当成DVR模长度。
有非典范模同构
$$H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus\mathcal T,
\qquad\mathcal T\simeq\bigoplus_{j=1}^{r-1}\mathcal O/(1-s^j)
\simeq\bigoplus_{b=0}^{a-1}
\left(\mathcal O/(\pi^{e/\varphi(p^{a-b})})\right)^{\oplus\varphi(p^{a-b})}.\tag{C2c}$$
因此$\operatorname{length}\mathcal T=ae$、最少生成元数为$N-1$，
$\operatorname{Fitt}_0\mathcal T=(r)=(p^a)$。
分裂不能由总长度猜出；当前完整证明从C1特化，保留S的独立DVR证明为正确替代。
完整Smith数据是C1的消费者，不与通用分裂重复计为另一种上同调方法。

### C3. 原整除状态微分及完整Hasse解释

保留C2全部参数。相对微分$d$只作用于原状态$x,y$，固定$s,t$。
在完整$\mathcal U=\mathcal S\setminus\mathcal D$上，先在特征零除以$p^a$得到
$$\alpha=p^{-a}dI_r\in\Gamma(\mathcal U,\Omega^1_{\mathcal U/\mathcal O}),\qquad
\bar\alpha=H_p(T,J;\varepsilon)^{\sigma}dJ,\quad
T=\bar t^m,\ \varepsilon=(-1)^{m+1},\ \sigma=(N-1)/(p-1).\tag{C3a}$$
准确多项式为
$$H_p(T,h;\varepsilon)=
\begin{cases}
[Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
h,&p=2.
\end{cases}\tag{C3b}$$
它关于$h$首一、次数$p-1$，故$H_p(T,J;\varepsilon)dJ\ne0$。
一形式的局部自由系数生成与标架无关的理想$\mathfrak c(\nu)$，并在整个$\bar{\mathcal U}$有
$$\overline{\mathfrak c(\alpha)}=(H_p(T,J;\varepsilon)^\sigma)\mathfrak c(dJ).\tag{C3c}$$
横线指理想在剩余结构层中的像。该等式含四条末端线和坏能级，保留理想重数而非只比较根集。
原$dI_r$沿整个剩余曲面泛点的准确公共$\pi$阶为
$$\operatorname{ord}_{\bar{\mathcal U}}(dI_r)=ae
=\operatorname{length}_{\mathcal O}\mathcal T,\qquad
\operatorname{Fitt}_0\mathcal T=(p^a).\tag{C3d}$$
这不是每个提升闭点的赋值，也不是$\pi$-饱和或已构造的典范模同构。

保留原光滑能级及**实际Jacobian**的几何解释，不仅给多项式同名：
谱曲线
$$E_{T,h}:\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3=0$$
在谱纤维光滑的能级，取原双图给出的完整光滑射影曲线，并用指定微分
$$\omega=dZ/(2\lambda-(T+hZ+Z^2))$$
及特征二的$\omega=dZ/(T+hZ+Z^2)$，$H_p$为Hasse系数；
完美域上的Cartier一维矩阵为$H_p^{1/p}$，不混同二者。
实际泛Jacobian由J的原域谱模／torsor识别给出；原光滑闭能级由同底完整模型同构接到该谱曲线。
经这些真实同构运输指定微分后，Hasse零点恰对应原光滑亏格一能级Jacobian超奇异；
C3c在光滑能级开集给该零除子的拉回并将重数乘$\sigma$。
不把奇异三次曲线称为超奇异，也不把微分平凡化下的标量称为无规范的绝对数。

## 4. 必要证明与接受链

新增[数学合取接受](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md)包含D/G/S/U四对实际输入。
U独审只接受其新增步骤，S5/S7责任由同哈希S独审的实际PASS合取关闭；不是用消息或作者判断代签。
这些局部接受支持候选组织，不替正式评审对完整证明信心负责。

完整必要结构如下；文件内历史OPEN／CONDITIONAL按实际后续接受对接，不倒退成新失败：

| 必要模块 | 真实消费者和不能删的内容 |
|---|---|
| P、N原几何 | 原八中心／帧／边界及末端线、精确极除子、法丛阶；单位公式用于无关系整数族 |
| 旧primitive-genus-one桥及F | 原最小完整pencil、Stein与投影公式、全特征泛光滑、有限几何纤维整约化；C2两侧阶$r,m$均消费 |
| S Steps1–5 | 原$C_j$在整个共振整数基的平坦允许极点商下降、真实单位边界；不能用非正规Hartogs或逐域计数替代 |
| U | 实际常数推前、节点复形、不预设分裂的过滤、Bockstein有限阶生成元、Ext二阶消失及任意基变换 |
| 新G与S的赋值段 | 同一完整相对模型、无基点与平坦、精确特化像、全部初等因子的标准圆分赋值 |
| D及新G末段 | 原矩阵整数循环插入、秩二递推、系数提取、非零首项、Cartier小特征解释及跨四末端线延拓 |
| W V2及纯B前提 | 先由纯谱有限临界代数和完整双图建立泛谱光滑、亏格、循环固定点；任意定义域接口保留 |
| J Step2–7 | 真实谱模族、常数共轭重构和原坐标有理逆、不可分次数、固定Picard差、无核及原域torsor下降 |
| H.L(a)、B纯模型及实际前提 | 完整闭能级的光滑点提升、两侧相对最小性及同底模型同构；最小正则模型不混同最小整方程 |

旧强T3的Artin块和完整临界特征多项式、旧R/V/C/Q/I/O的动力／周期／点数分箱均原样保存。
它们不是C1–C3的全部直接消费者，不因为保留旧结果就倒灌成新claim；
其中W泛光滑实际消费的纯谱有限性证明则不能删。
当前图将共同常数／边界计算和U的特化只计算一次；不引入未经审查的短证明。
所有本题特有必要证明仍须在未来正文完整给出，不能以本地研究文件的链接代替正文证明。

## 5. 来源、独立意见与组合内扣除

完整来源依据是四份前置有界记录、最终Phase B、独立C/D及组合报告；
它们全部作为共同科学输入，不只摘取支持候选的结论。

| 已有工作／机制 | 必须扣除 | 实际剩余或边界 |
|---|---|---|
| JR原积分／谱矩阵／圆分整数式 | 原对象与原规范、Laurent首项、原根单位积分 | 原完整整数曲面、共振截面与全模型特化并非由题名自动给出 |
| GHK、Friedman、Halphen背景 | 近邻八环、通用周期族、节点粘合与域上pencil判据 | 已读复数／reduced analytic理论不直接给本整数曲面扩张消失 |
| Wagner q-Hodge及Habiro工作 | $T^j\mapsto(q^j-1)T^{j-1}dT$的对角形状、已有根单位cohomology理论 | 有限矩阵同形不等于识别原$R\Gamma L_n$；不主张额外q-Hodge兼容或典范性 |
| Stacks、Bockstein、Ext、Fitting、DVR赋值 | perfectness／任意派生基变换、分裂工具及形式推论 | 原曲面中的具体扩张类必须由实际截面处理 |
| VlasenkoTheorem1(i) | **直接包含**C3的Hasse全部迭代乘子，无ordinary前提 | 原$p^{-a}dI_r$到该系数的整数桥与全开放空间仍是实际对象识别 |
| KS／Smirnov等q-difference先例 | 首非零分歧项、$p^s$根单位特化、Frobenius及Dwork联系 | 它们的对象／归一化不自动等于原qPI状态微分，亦不可称前人只做零阶 |
| Beauville／谱Picard、最小模型、Cartier | 谱模方法、模型唯一性、Hasse定义与小特征工具 | 本题仍须给真实原域Jacobian和闭能级接口，不能靠同亏格声明 |
| 组合内P18／P29 | 相对微分Fitting基变换、另一种特征零差分cohomology的通用工具 | 实读接受源范围内未见直接包含完整C1–C3；不是全作品全文排除 |
| C1的C2特化／理想与长度后果 | Smith模、Fitting乘积、公共阶与长度相等不重复计分 | 不能将一个主定理和若干形式消费者包装成多套一般方法 |

[独立C/D](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md)的7.0与最强反对意见保留：
矩阵形状和多数后果已有标准模型，独立于C1的新概念范围有限，尚非一般理论突破。
其正面理由是曲面级全共振扩张的具体消失，不能由域上维数或边界复形直接读出。
正式评审应独立权衡这些证据；不机械复制7.0，也不为越过7.5而调分。

近期检索截至2026-09-09，具体日期、版本及实读范围以B为准。
Scholar/S2入口受限，arXiv搜索部分失败；一般整数Halphen扩张分类、历史原文及完整引文图未穷尽。
Ohyama／GRT11真实全文缺口继续保留；主控已补读JR出版授权网页全文的子缺口不重开。
全球首创为UNCERTAIN，不采用“全球首次”“新q-Hodge理论”等定位。
跨系统族可能联系仅为ROUND2_CLUE，不进入本件已证明的量词或价值。

## 6. 双份完整四门与不可改变的边界

两位全新非作者各读同一完整共同包，各自独立评价：

1. 新意0–10，至少7.5。
2. 独立科学价值0–10，至少7.5。
3. 完整证明信心0–10，至少9。
4. 匿名英文单栏11pt、letter、四边1 inch、标准行距、必要证明全部正文时，
   对自然22–30页实质正文给可信PASS/FAIL判断；参考文献另计。

即使首门未过，也须评价其余三门。两位各自完整合取后再取两票合取；不平均、不拼接、不用旧票替代。
容量须逐必要块给低／中／高预测及总和，说明低于22与高于30的风险；
它们不是实测或严格界，不另加central必须在窗口的规则，不从行数或文件数估页。
不得删全量词、末端线或实际Jacobian／闭能级接口，不拆篇、缩版、灌水、移必要证明至附录或试写测页。
不预支Paper29的特定实测许可；未获双份完整准入前不建项目／source/publication locks、不写论文或编译PDF。

使用可用Codex的fresh独立上下文、xhigh，彼此本轮报告提交前不可见；
共同包公开的旧失败和查新意见可见，不声称对这些历史盲审。
GPT-5.4 MCP未配置，不伪称调用或跨模型认证；NOT_CALIBRATED、criteria_binding_unavailable。
本合同来自用户既定科学／容量要求，不声称期刊适配、接受概率或人类认证。
ARS只帮助证据映射与意见保真，不启动默认五席期刊panel，不替换本项目数值合同。

本件没有新数学证明、外部模型上传、实验、投稿、托管、push、对外发信或付费资源操作。
完整五篇目标仍为3/5，Paper30未立项、Paper31及跨论文统一审查未完成。
