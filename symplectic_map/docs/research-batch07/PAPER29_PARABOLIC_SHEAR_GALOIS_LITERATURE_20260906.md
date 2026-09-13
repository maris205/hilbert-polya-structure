# Paper29 新候选：平移不变面与梯度剪切非可积性的独立查新/价值预筛

日期：2026-09-06。任务：独立核查邻近一手文献的实际覆盖，以及本候选是否具有独立问题价值和自然的 22–30 页容量。本报告不拥有主证明文件，不建立正式 Paper29，不改变既有 STOP 记录。

## 1. 结论先行

**有独立数学价值，但当前证据不支持通过原 22–30 页合取门。** 与 P20 的次数增长问题相比，“某类二阶横向 Hamiltonian 信息强制所有正迭代非可积，且对任意三阶横向扰动稳定”是不同的问题；无扰动子族的可积性 iff 又给出了一个真实边界。因此不能把整个新结果贬作 P20 结论的改写。

但已核内容仍以一个短的多项式 companion 引理、成熟差分 Galois reduction、Casale–Roques 既有辛可积性障碍为主要证明链。参数个数无界、高阶项任意、结论覆盖每个正迭代，并不自动产生多个独立证明机制。连同现有分布约束和常数边界，独立估计自然正文约 **11–16 页**；22 页的实质下界尚无证据。这个估计不是排版测量，也不是新的页数标准。

查新结论必须分开说：

- 已明确发现同类线性 trace 方程的 $\mathrm{SL}_2$ 是经典结果，不能作为核心首创。
- 已找到二阶差分 Galois 的通用算法与 reduction 来源；这些是工具，不是本候选的新理论。
- 本轮没有找到与当前四维梯度剪切族、三阶扰动稳定性及全正迭代结论完全相同的已发表定理。
- 尚未核清“任意非恒定多项式 trace 均有 $\mathrm{SL}_2$”这一概括的最早出处；没有找到不等于未发表。论文定位应容许该辅助引理已知。

因此当前处置为 **保留新证明；STOP 作为满足现行长度要求的 Paper29 候选**。停止理由不是已发现反例，也不是证明包不存在，而是独立容量门尚未满足。

## 2. 本次核查的精确对象

在 $\mathbb A^4_{\mathbb C}$ 上用坐标 $(x,y,u,v)$ 和辛形式 $dx\wedge du+dy\wedge dv$。取

$$
V(x,y)=P(x)+\frac12 A(x)y^2+y^3R(x,y),\qquad
W(u,v)=\frac12 B(u)v^2+v^3S(u,v),
$$

其中均为多项式，$P'\not\equiv0$、$A\not\equiv0$、$\deg B\ge1$。令 $F=T_WS_V$ 为两个梯度剪切之积。

被评价的主张是：对每个 $m\ge1$，不存在两个独立、Poisson 对易的有理函数同时被 $F^m$ 保持；其成立不依赖 $R,S$。本报告不把它改写为“没有任何非平凡有理第一积分”，也不把它改写为“没有保持的有理纤维化”。后两项不是同一结论。

真实适应曲线位于 $M=\{y=v=0\}$ 上：

$$
F|_M(x,u)=(x,u+P'(x)),\qquad
\gamma_a(t)=(a,0,t,0),\quad c=P'(a)\ne0,\quad\alpha=A(a)\ne0.
$$

法向方程可写为

$$
\eta(t+c)+\eta(t-c)=(2+\alpha B(t))\eta(t).
$$

正规化变量 $z=t/c$ 后，记 $Q(z)=2+\alpha B(cz)$，则 $Q$ 为非恒定多项式。使用向量 $(\eta(z),\eta(z-1))$ 时，正向矩阵中的 trace 是 $Q(z)$；改变状态向量或原点会产生等价的 $Q(z+1)$ 写法。文献比对不能把这种移位当作不同方程。

本报告另读了主证明代理在 [splitting preflight](PAPER29_SPLITTING_RIGIDITY_PREFLIGHT_20260906.md) §11 新增的精确边界：在 $R=S=0$、$P'\not\equiv0$、$A\not\equiv0$ 下，任意正迭代有理 Liouville 可积当且仅当 $B$ 为常数。常数 $B=b$ 时显式积分为

$$
x,\qquad I=A(x)y^2-bv^2-bA(x)yv.
$$

此 iff 不延伸到任意 $R,S$，也不分类 $P'=0$ 或 $A=0$。

## 3. 已核一手来源及其真实覆盖

### 3.1 差分非可积性框架：必须明确归于既有工作

Casale–Roques，*Dynamics of rational symplectic mappings and difference Galois theory*，IMRN 2008，rnn103。[作者预印本全文](https://arxiv.org/pdf/0803.3951)。已核主定理及 §§6–8：辛映射的完整可积结构给出沿适应曲线变分差分群单位分支交换的必要条件；全文实例是二维有理映射和相应可约/三角型方程，不是上述四维梯度剪切族。

其 rational embedding、junior parts 和 Ziglin 处理属于已有框架。沿不变面退化或有极点的积分不能仅凭“限制后看不见”逃过该定理；同时，也不能由此进一步排除任意单个有理积分。这一来源的作用是严格桥梁，不是本候选声称创立的新方法。

Casale–Roques，*Non-integrability by discrete quadratures*，J. Reine Angew. Math. 687 (2014)，87–112，在线发表于 2012。[出版记录与摘要](https://doi.org/10.1515/crelle-2012-0054)，[作者全文](https://perso.univ-rennes1.fr/guy.casale/research/Casale-Roques.pdf)。该文给出离散求积可积性的虚可解性必要条件，并应用于 $q$-Painlevé I/III。不是当前梯度剪切族的现成分类；若以后核定并增加“不可离散求积”的推论，它仍主要复用同一 Galois 障碍，不自然构成第二个大证明核心。

### 3.2 线性 trace 的 $\mathrm{SL}_2$ 已知，任意多项式的优先权未核清

Hardouin–Singer，*Differential Galois theory of linear difference equations*，Math. Ann. 342 (2008)，333–377。[全文](https://arxiv.org/pdf/0801.1493)，Example 3.13：

$$
Y(x+1)=\begin{pmatrix}0&-1\\1&x\end{pmatrix}Y(x)
$$

在 $\mathbb C(x)$ 上的普通差分 Galois 群为 $\mathrm{SL}_2$，且作者明确将此已知事实指向 van der Put–Singer 1997 专著第 42 页。不能将这个线性 trace 实例重报为新发现；这里所核的是普通差分群，不能与该文进一步研究的参数化/微分代数群混淆。

Arreche，*Computation of the difference-differential Galois group and differential relations among solutions for a second-order linear difference equation*，[作者预印本](https://arxiv.org/pdf/1606.07109)。已核 §3 的经典二阶算法回顾与 §9：Example 9.3 再次使用 $\sigma^2y+xy^\sigma+y=0$ 的 $\mathrm{SL}_2$，并指向已有证明；§9.1–9.2 分别是可约和 imprimitive 方程。没有在所核部分发现“任意非恒定多项式 trace”的完整陈述。

Hendriks，*An algorithm determining the difference Galois group of second order linear difference equations*，J. Symbolic Comput. 26 (1998)，445–461。[出版链接](https://doi.org/10.1006/jsco.1998.0223)，[作者机构书目记录](https://research.rug.nl/en/publications/an-algorithm-determining-the-difference-galois-group-of-second-or/)。其算法与 Riccati/primitive 检查是必须对照的旧技术。此次未取得可逐页核读的该文完整正文；因此本报告不声称其未覆盖当前多项式概括，也不虚构某条原文定理号。

Hendriks–Singer，*Solving Difference Equations in Finite Terms*，J. Symbolic Comput. 27 (1999)，239–259。[作者原文链接](https://singer.math.ncsu.edu/papers/finite.pdf)。主证明代理已核 Theorem 2.1 的有理 reduction 及有限分量处理并用于 §11。本代理阅读了该运用，但此次直接全文访问多次失败；它是已知 Galois 工具来源，不被本报告计入本候选首创。

**判断：** “所有正步长无有理不变直线”的统一初等证明有展示价值；它解决了一步不可约不够排除非连通/交换线逃逸的实际细节。然而，在成熟二阶算法背景下，除非查明独立历史位置，不宜把“任意多项式 trace 的 $\mathrm{SL}_2$”本身包装成主创新。即使后来找到完全同式的旧定理，真正待评价的新对象仍应是四维剪切族的可积性判据与精确边界。

### 3.3 Li–Shi 2012 近邻文献存在必须同时引用的勘误

Li–Shi，*Galoisian obstruction to the integrability of general dynamical systems*，JDE 252 (2012)，5518–5534。[原文 DOI](https://doi.org/10.1016/j.jde.2012.01.004)。作者公开上传的[全文与勘误合并副本](https://www.researchgate.net/publication/256749158_Galoisian_obstruction_to_the_integrability_of_general_dynamical_systems)中可核：唯一映射实例 Example 3 是二维三角 $q$-差分型映射，并非本族。

其 2017 [Corrigendum](https://doi.org/10.1016/j.jde.2016.10.007)，JDE 262，1253–1256，改正原 Theorem 7，并修改 Theorem 8 与相关推论；一般映射情形的原强结论不能照搬。当前候选采用 Casale–Roques 的辛完整可积性必要条件，不能换成 Li–Shi 旧版的更强说法去排除任意两个非对易积分。此警告不构成对当前正确辛判据的否定。

## 4. 与本地既有成果的独立性

已比对 [P20 正文](../../papers/20-coupled-shear-degree-matrix/paper/main.tex) 的对象、摘要、主结论和相应引用。P20 的主问题是耦合梯度剪切的精确次数递推/动力次数。本候选把其一个横向二阶信息抽象为一个带任意高阶项的族，并提出有理 Liouville 非可积性；这不是从“次数指数增长”直接换一句结论。

实例包含关系为

$$
P(x)=x^g,\quad A(x)=2x^2,\quad B(u)=2u^2,\quad R=0,\quad S(u,v)=v^{g-3}.
$$

P20 特例只是说明判据触及项目原对象，不能独占新论文的贡献清单。反过来，不能为了凑篇幅重新展开 P20 已有的次数、辛性及逆映射证明。

## 5. 科学价值：哪些是真增量，哪些只是同一机制的展开

| 内容 | 独立价值判断 | 不宜宣称的增强 |
|---|---|---|
| 从一般 $P,A,B$ 的二阶横向信息得到非可积性 | 是明确而不同于次数增长的科学问题 | 新发明离散 Morales–Ramis 理论 |
| 任意 $R,S$ 不改变实际法向变分方程 | 是精确代数稳定性，而非数值鲁棒性 | 一般扰动空间中的开放稠密非可积性 |
| 所有正迭代同时受阻 | 排除通过取有限幂恢复完整可积性的漏洞 | 自动排除所有有理半共轭与移动底纤维化 |
| 无扰动族 $B$ 常数 iff | 真正可证的可积/不可积边界 | 任意高阶扰动下的完整分类 |
| 不变 Lagrangian 分布在指定平面上必须奇异 | 是几何限制；应精确保留定义域条件 | 尚未证明的全局无纤维化 |
| $\mathrm{SL}_2$、无可解求积等表述 | 可作为相关推论 | 各自算一个新的大定理机制 |

“三阶横向扰动任意”来自二阶导数在平面上消失的直接事实，它确实扩大结论适用域，但证明复杂度不随可任取的项数增加。这里的稳定性是保持指定不变面与二阶横向数据的稳定性，不是对任意多项式扰动的稳定性。

对依赖外部一般定理的应用论文，短而准确未必没有发表价值。本报告只否定当前包已满足项目锁定的 22–30 页要求，不把“未过这个门”混同于“数学没有价值”。

## 6. 独立自然容量审计

按正常研究论文写法估算，包括必要自足说明，但不重新教授差分 Galois 理论、不重印 P20 旧证明：

| 自然部分 | 正文页估计 | 计数理由 |
|---|---:|---|
| 问题、对象、邻近文献和精确贡献界线 | 2–3 | 需说明为何次数增长不替代此问题 |
| 实际适应曲线、切向平凡化、法向 companion | 1.5–2 | 关键符号/移位和高阶项消失须写清 |
| 所有步长的初等不可约证明及分量处理 | 2–3 | 应保留真正排除非连通逃逸的论证 |
| 主非可积性准则、适用假设与全正迭代 | 1.5–2 | 精确应用旧定理，不重复完整外部理论 |
| $R=S=0$ 的常数 $B$ iff 与积分验证 | 1–1.5 | 结论有用但正向证明是短二次型计算 |
| 已有分布约束、P20 实例与局限 | 2–3 | 与主问题关系需清楚，不能冒充完整纤维化定理 |
| 简短结语与必要整理 | 0.5–1 | 不引入重复总结 |

合计约 10.5–15.5 页，取整给 **11–16 页正文**。参考文献页、大片背景、重复特例、展开高阶扰动任意参数及宽松排版不作为新增实质贡献计数。独立估计与主证明代理的 10–15 页略有差异，但两者都没有支持 22 页的下界。

这不是“再补几个常规推论就能 PASS”的建议。若后来有新定理，它必须改变问题的解决程度或提供独立机制，之后才重新做有界预筛。

## 7. 搜索覆盖和未核清事项

检索日期为 2026-09-06。多轮检索至少覆盖以下关键词族；不将搜索失败视为不存在证明：

1. `difference Galois polynomial Schrodinger`、`difference Galois nonconstant polynomial`。
2. `Galois Theory of Difference Equations Singer 42`、`Hendriks An algorithm determining pdf`。
3. `Galois y(x+1) y(x-1) polynomial`、`difference sigma polynomial SL2 Hendriks`。
4. `symplectic shear Galois nonintegrability`、`symplectic maps parabolic nonintegrability`。
5. `gradient shears nonintegrability`、`discrete Schrödinger Galois polynomial`。
6. `Galoisian obstruction to the integrability of general dynamical systems`，并追踪勘误与真实例子。
7. `Non-integrability by discrete quadratures`，追踪作者全文与正式书目信息。
8. `Solving Difference Equations in Finite Terms Theorem 2.1`，与当前证明中的 reduction 用法比较。

另读 Singer 的[作者讲义](https://singer.math.ncsu.edu/papers/CIMPA.pdf)的相关算法说明与例子；它是背景综述，不作为“没有更早工作”的证据。没有将搜索结果中的微分 Schrödinger 方程、Mahler 方程、谱论 Schrödinger 算子或通用数值非可积性结果误记成当前平移差分方程的直接覆盖。

尚未核清的文献项：Hendriks 1998 完整正文和 van der Put–Singer 1997 相邻页是否直接陈述任意非恒定多项式的统一结论。因此这里不给“全多项式 SL₂ 引理原创”的 PASS，也不给排他性首创断言。

这项优先权不确定性不会阻止保留已写出的自足证明，更不能靠把未核清项藏在文献清单中获得新颖性认证。建议的诚实定位是：以经典差分 Galois 方法证明一个明确的梯度剪切族判据，并把辅助 companion 引理的出处风险公开列明。

## 8. 交付边界

本报告只新增此文件；没有改动主证明 preflight、之前的周期几何 STOP、P20 或任何正式论文。没有投稿、上传、对外发信或使用付费计算资源。本报告不提供 Route A/B 评价，不把查新、证明状态、独立价值和 PDF 验收混为同一结果。

最终建议：保留 §11 的可检验证明与精确 iff；当前 Paper29 仍不过原 22–30 页门。若未来重新开启，应先提出实质不同的新机制并单独预筛，而不是把本报告的文献梳理计入新定理长度。
