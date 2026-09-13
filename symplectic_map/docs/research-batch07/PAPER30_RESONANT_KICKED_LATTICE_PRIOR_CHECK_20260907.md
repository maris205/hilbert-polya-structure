# Paper30：共振 kicked lattice 的有界一手先例核对

日期：2026-09-07。性质：文献与量词核对；不是定理终审、实验、稿件、立项或评分。此前 Artin–Schreier 报告保持冻结，本文件与其科学问题无关。

## 结论先行

当前候选有很强的直接方法与现象覆盖，不能把以下内容单独作为新机制：

- 反连续极限的局域周期轨道延续；
- 弱耦合辛映射链中的 breather 及 Krein 复失稳；
- 局域模式进入相反 Krein 符号的连续频带后，在无限系统中仍然存在失稳；
- 一负方向 Jacobi 缺陷、半圆律 $m$ 函数、标量 Schur 方程和有限截断的带外特征值收敛。

特别地，给定候选半无限约化矩阵是 Derevyagin–Perotti–Wojtylak 的明确常系数专门化；候选闭式根及阈值可以从同一 $m$ 函数方程直接算出。

此次查读**未确认**以下精确组合已被直接给出：保持指定未耦合局部一阶 jet 与两步 Floquet 矩阵的实际多项式 kicked-map 族，同时证明大 $N$ 一致的小耦合延续、真实 Floquet quartet/增长率及外侧稳定相。这个“未确认”不是新颖性认证。其中 MacKay–Sepulchre 1998 的全文没有取得，相关最强直接覆盖核对仍有一个明确缺口。

## 1. 核对对象及证据身份

输入为路径图 $N$ 节点、一个端点激发的离散辛映射

$$
p'=p-f_\eta(q)-\varepsilon L_Nq,\qquad q'=q+p',
$$

其中 $f_\eta$ 按坐标作用，

$$
f_\eta(q)=q+\frac{5q^2+155q^3-5q^4-83q^5}{24}
              +\eta q^2(q^2-1)^2.
$$

主控给定的未耦合轨道为一个端点
$(1,2)\leftrightarrow(-1,-2)$，其余节点为 $(0,0)$；给定局部导数为

$$
f_\eta'(0)=1,\quad f_\eta'(1)=\frac83,\quad
f_\eta'(-1)=\frac72.
$$

背景与缺陷两步 trace 均为 $-1$，Krein 符号相反。主控正在建立的候选一阶 trace 约化为

$$
J_n(\theta)=
\begin{pmatrix}
\theta&-g e_1^*\\
g e_1&T_n
\end{pmatrix},\qquad
g=\frac1{\sqrt6},\qquad
\theta=-\frac{46331}{648}+\frac{250}{27}\eta,
$$

其中 $n=N-1$，$T_n$ 邻边为 $2$、对角通常为 $-4$，最后一项为 $-2$。本文件没有独立证明这一非线性轨道延续或一阶约化，不将输入公式登记为已证定理。

主控另给有限链候选

$$
m_n(z)=\frac12\frac{U_{n-1}(x)-U_{n-2}(x)}{U_n(x)-U_{n-1}(x)},
\qquad x=\frac{z+4}{4},
$$

以及 $n\ge55$ 时某导数符号、一整段失稳区间和阈值收敛的待核对结论。本文件只比较其量词与先例，不验证这些数字或导数估计。

术语须限定为“相同未耦合局部**一阶** jet / Floquet 矩阵”。因为
$R(q)=q^2(q^2-1)^2$ 在 $0,\pm1$ 处的值和一阶导数均为零，但

$$
R''(0)=2,\qquad R''(\pm1)=8.
$$

因此不能写成全部局部 jets、全部高阶正规形或所有耦合后 Floquet 导数都相同。

## 2. 搜索与正文读取边界

使用 research-lit 技能，仅核对公开一手来源。搜索查询共 **8 个**，未超额：

1. `MacKay Sepulchre 1998 linear stability discrete breathers l2 resonances maps`
2. `coupled symplectic maps breather stability Krein resonance impurity`
3. `site:arxiv.org Jacobi matrix one negative square complex eigenvalues rank one perturbation`
4. `"Stability of discrete breathers" "Sepulchre" pdf`
5. `"Abel" "Spicci" "maps" breathers`
6. `"Jacobi" "one negative square" eigenvalues`
7. `"Truncations of a class of pseudo-Hermitian operators"`
8. `"Finite size effects on instabilities of discrete breathers" pdf`

查询之后只打开已经定位的论文、精确 DOI 或作者页面，没有追加关键词查询。arXiv 采用公开 web 查询与正文读取；没有下载或保存论文副本，也没有扫描本地历史论文树。

实际读取了以下 **3 份一手正文**：

- Derevyagin–Perotti–Wojtylak：arXiv:1503.04314v2，正文 I–III，常系数 Example III.5，结论与 Appendix A。
- Koukouloyannis–Ichtiaroglou：作者托管的六页 *Localized periodic motions in systems of coupled oscillators*，全文，含弱耦合映射模型、延续、稳定性讨论与参考文献。
- Aubry：1998 年 Annales IHP 原文，重点 §9.2、印刷 pp. 414–418；另核对相邻局域化讨论和参考文献。

出版社摘要另用于核对 MacKay–Sepulchre 1998、2002 年 coupled integrable maps 论文以及 Stöber–Bäcker 2021 的书目信息。摘要未冒充全文。访问失败、订阅提示或不可用接口均未绕过；未使用账号、付费访问或额外权限。

## 3. 最强先例与直接覆盖表

| 一手来源 | 实际核对依据 | 应扣除的范围 | 不能据此直接推出的内容 |
|---|---|---|---|
| [Derevyagin, Perotti, Wojtylak, arXiv:1503.04314v2](https://arxiv.org/html/1503.04314)，2015；后发表于 JMAA 438(2), 2016, 738–758，DOI 10.1016/j.jmaa.2016.01.013 | (I.1)–(I.2)、(II.3)–(II.4)、III.3、(III.9)、III.5、Appendix A | 与候选同型的一负方向 Jacobi 算子；常系数半圆律例；简单带外非正型特征值的有限截断指数收敛 | 当前 $N$ 依赖末端条件、全 $\theta$ 相图、非线性 kicked-map 约化及 $N$ 一致 $\varepsilon$ 范围 |
| [Koukouloyannis–Ichtiaroglou，作者六页正文](https://mathweb.aegean.gr/vkouk/publications/breather_maps_proceedings.pdf)；相关正式论文 *Existence of localized periodic motions in systems of coupled integrable symplectic maps*, Chaos, Solitons & Fractals 13(6), 2002, 1317–1331，DOI 10.1016/S0960-0779(01)00140-0 | 作者正文 §2–3 全部；正式论文题名、年份、页码核对出版社记录 | 无限弱耦合辛映射链、局域周期解延续、Krein 稳定性条件；有限链的复失稳演示 | 其单站可积共振圆不是本题非退化两周期与相反符号背景的精确重合；未见当前统一双极限合同 |
| [S. Aubry, *Discrete breathers in anharmonic models with acoustic phonons*, Ann. IHP Phys. Théor. 68(4), 1998, 381–420](https://www.numdam.org/item/AIHPA_1998__68_4_381_0.pdf) | §9.2，尤其 pp. 417–418 | 相反 Krein 频带碰撞、有限尺寸效应；局域振子特征值进入相反符号连续弧时无限系统失稳持续这一物理/谱现象 | 该节部分一般重叠弧陈述是预期或猜想，不能统一当作严格定理；未给本题离散 map 族 |
| [R. S. MacKay–J.-A. Sepulchre, *Stability of discrete breathers*, Physica D 119(1–2), 1998, 148–162](https://www.sciencedirect.com/science/article/pii/S0167278998000736) | 本次仅获得出版社摘要 | 一般振子网络、一般耦合与弱耦合 $\ell^2$ 线性稳定性已经有严格理论，不能再声称“首次无限格点稳定桥” | 未取得正文，不能确认或排除其具体假设是否已经覆盖本题共振及等一阶 jet 族 |
| [J. Stöber–A. Bäcker, *Geometry of complex instability and escape in four-dimensional symplectic maps*, Phys. Rev. E 103, 042208 (2021)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.103.042208) | 本次只使用公开摘要 | 两个耦合 standard maps 中稳定到复失稳转变及其正规形/输运图像已有研究 | 固定四维研究不能直接充当全 $N$、无穷格点与一致小耦合结论 |

MacKay–Aubry 1994 的反连续延续为已知基线，不作为候选新意。此次未重新审查其完整定理；其准确引用为 *Proof of existence of breathers for time-reversible or Hamiltonian networks of weakly coupled oscillators*, Nonlinearity 7, 1623–1643，DOI 10.1088/0951-7715/7/6/006。该文在已读的作者正文及 Aubry 原文中均列为存在性来源。

## 4. 最直接的数学重叠：常系数半无限缺陷

### 4.1 参数映射是严格的，不只是外观相似

以下仅对**给定约化矩阵**做代数比较；不证明它确实来自原始映射。

半无限背景为对角 $-4$、邻边 $2$。令

$$
\widehat J=\frac{J_\infty+4I}{2},\qquad
\alpha=\frac{\theta+4}{2},\qquad
\beta=\frac{1}{2\sqrt6}.
$$

则

$$
\widehat J=
\begin{pmatrix}
\alpha&-\beta&0&\cdots\\
\beta&0&1&\cdots\\
0&1&0&\ddots\\
\vdots&\vdots&\ddots&\ddots
\end{pmatrix}.
$$

这就是上述一负方向 Jacobi 先例中的常系数半圆律分支，参数对应为

$$
a_0=\alpha,\quad b_0=\beta,\quad a_j=0,\quad b_j=1\quad(j\ge1).
$$

不能因为本题把矩阵称为“Floquet trace 约化”就忽略这个直接重叠。

### 4.2 候选闭式根是同一 self-energy 方程的专门化

记标准半无限背景为 $S$，并取

$$
m(w)=\langle e_1,(S-w)^{-1}e_1\rangle
=\frac{-w+\sqrt{w^2-4}}{2},
$$

平方根分支在无穷远与 $w$ 同阶，使 $m(w)\sim-1/w$。也可不引用积分公式，而直接由尾部自相似性得

$$
m(w)=\frac{1}{-w-m(w)}.
$$

对给定块矩阵取 Schur 补，特征值条件为

$$
w-\alpha-\beta^2m(w)=0.
$$

代入 $\beta^2=1/24$ 后平方消根号，得到

$$
(1+\beta^2)w^2-(2+\beta^2)\alpha w+\alpha^2+\beta^4=0.
$$

再用 $z=2w-4$，得到主控候选的同一对代数根

$$
z_\pm=\frac{49\theta-4}{50}
\pm\frac{1}{50}\sqrt{(\theta+4)^2-\frac{50}{3}}.
$$

因此其非实判别阈值

$$
|\theta+4|<\sqrt{50/3}=\frac{5\sqrt6}{3}
$$

不是一种新 self-energy 机制。这里的具体有理参数或这个整理后的公式不一定在先例中逐字写出；但它们属于已经指定的常系数模型的明确专门化。

平方后的**实根**仍需核对原 $m$ 函数分支与特征向量的 $\ell^2$ 条件，不能把所有代数实根自动算作实际特征值。本文只用上述计算辨识先例重叠，不用它完成全部稳定侧证明。

### 4.3 有限截断定理的真实量词

已读先例的 III.3 针对一个固定、有界系数的无限 Jacobi 算子及其主截断。若指定非正型特征值简单并位于背景谱包络区间之外，给出截断特征值的指数收敛率；实而简单的带外极限还给出最终实性。非实极限的最终非实性也由收敛得到。

该结论的常数依赖固定算子和复平面邻域；不能不加证明地交换成对全部 $\theta$ 一致。Appendix A 显示的显式界首先把截断特征值排到相应椭圆/背景区间之外；本记录不把该显示式未经额外局部圆盘论证就加强为“同一数值界保证非实”。

## 5. 当前有限端点与完整相图：需要补的是哪些量词

候选 $T_n$ 的最后对角元为 $-2$。在上述平移缩放后，有限背景最后对角元为 $1$，其余为 $0$。它不是一个固定无限常系数矩阵的所有主截断：对每个新 $n$，修改发生在新的末端。

因此直接援引先例 III.3 不足以逐字覆盖本题。这个差别的正确处理是一个有限远端边界引理，例如端点 resolvent 恒等式、二阶差分递推或给定 Chebyshev 公式。由于扰动位于远端，其算子范数并不趋于零；应证明缺陷处的 $m$ 函数在所选复轮廓上收敛，而不是声称整矩阵在算子范数下逼近。

不过，该边界修正仍属于 Jacobi 边界条件与 resolvent 的成熟方法范围，不能只凭“端点是 $-2$”断言新机制。

主控提出的“每个 $n\ge55$ 都只有一个完整 $\theta$ 失稳区间”与固定 $\theta$ 的截断收敛不是同一量词。若前者最终成立，必须单独核对：

- 所有背景谱隙中的导数符号，不能只处理带外或有限几个参数；
- 端点与二重根的临界情况，不能从严格不等式内部自动延拓；
- 每个 $n$ 的完整区间结构，而不仅是 $n\to\infty$ 的某条非实根；
- “阈值随 $n$ 收敛”与“整个参数区间上的一致谱间隔”之间的区别。

此次阅读未找到上述特定有限边界、特定耦合强度和完整参数区间的一句现成定理；也未做其独立证明或穷尽查新。

## 6. 已有局域模式—连续谱现象不能遗漏

作者版 coupled-map 文本研究的是可积单站映射在有理旋转数圆上的非孤立周期点，背景停在稳定固定点；因单位乘子存在，需另选可延续的相位。其有限链演示中，局域振子乘子与其他乘子碰撞后离开单位圆。因此“把 flow 改成 map”“存在局域周期轨道”和“出现 Krein quartet”本身都不是可保留的新意。

Aubry 1998 §9.2 的一个重要区分是：两条相反符号的连续弧重叠，与一个局域振子特征值进入相反符号连续弧，不应混为同一个极限问题。该节对后者明确指出无限系统失稳的持续性，并归引 Mariñ–Aubry 的研究；对若干一般重叠弧情况则使用预期/猜想措辞。这里分别保留证据等级，不把整节都当成已证的统一谱定理。[Aubry 原文，pp. 417–418](https://www.numdam.org/item/AIHPA_1998__68_4_381_0.pdf)

由此推断，当前“端点局域模式＋相反 Krein 背景＋大 $N$ 仍然失稳”的现象已经有很强先例。其是否由连续 flow、DNLS 或 kicked map 实现，不会消除这种现象层面的覆盖；模型实现层与统一误差层仍需逐项比较。

原文归引的最直接邻接文献是 J. L. Mariñ–S. Aubry, *Finite size effects on instabilities of discrete breathers*, Physica D 119, 163–174 (1998)，DOI 10.1016/S0167-2789(98)00077-3。本次未取得该篇全文，故不虚构它的定理编号、常数或小参数一致性结论。

## 7. 真正尚需查证或证明的组合，而非新颖性保证

若继续当前候选，科学内容应落实为下列明确陈述；本表不是评分或实施授权。

| 待完成内容 | 必须写清的量词/边界 | 为什么不能由上面先例自动替代 |
|---|---|---|
| 实际 $f_\eta$ 族的等数据实现 | 固定轨道、局部一阶 jet、两步矩阵，而非全部高阶 jet | 已有谱模型可调 $a_0$，但这不自动实现为保留指定局部数据的同一非线性 map 族 |
| 全 $N$ 周期延续 | 同一邻域、同一 $\varepsilon_0$、局部唯一性；不要写全局唯一周期轨道 | 逐个 $N$ 的有限维隐函数定理不够；背景二步无乘子 $1$ 可能提供统一逆界，但必须落实 |
| 一阶 trace 约化 | 在选定规范下证明系数与余项，尤其是 $N$ 一致的算子范数控制 | 本文只是拿输入矩阵比对文献，未证明它确由 map 产生 |
| 真实 Floquet quartet | 对紧含于失稳参数区的集合，是否存在共同 $N_0,\varepsilon_0$；乘子远离单位圆的阶数 | 矩阵 $J_n$ 的复根不是未经误差控制的真实非线性延续轨道结论 |
| 增长率 | 明确按单次 kick 还是按两步 return 归一化；给误差是否一致 | 两者相差周期因子，不能混用线性谱根和物理增长率 |
| 外侧稳定相 | 谱稳定、幂有界线性稳定或非线性稳定需分开；说明临界点排除范围 | “一阶特征值实”不足以自行控制多重根、Jordan 块或 $N$ 增大时谱隙缩小 |

尤其外侧稳定性不能逐个区分越来越密的同符号背景特征值后，默认所得小耦合范围仍与 $N$ 无关。应说明使用的是统一 Krein 定号子空间控制、谱分离或等价的统一估计。这个方法本身同样属于一般 Krein/Pontryagin 理论；候选的贡献若存在，应是完成具体量词与非线性实现，而不是重新命名该方法。

## 8. MacKay–Sepulchre 1998 的明确缺口

出版社摘要确实宣告：对可非同质振子网络和一般耦合，利用辛符号理论给出弱耦合 $\ell^2$ 线性稳定条件。这足以扣除“此前没有无限维/一般耦合 breather 稳定性理论”的宽泛主张。[出版社摘要](https://www.sciencedirect.com/science/article/pii/S0167278998000736)

但摘要不足以决定以下问题：

1. 文中所用拓扑、算子正则性与网络一致性假设是否直接包含离散 kicked maps，还是需通过 stroboscopic map 作一次改写；
2. 相反 Krein 符号在反连续极限精确重合时，是否有已经完成的高阶分裂判据；
3. 是否已有保持未耦合局部一阶 jet 而稳定相改变的参数族；
4. 文中“弱耦合”的常数是否按当前有限路径图族统一，及是否支持所需参数区间。

本次正文访问未成功，不能写成“该文没有这些结果”。主控已收到这一缺口；未用检索未命中代替排除证明。

## 9. 交付状态

- 查询数：8；一手正文实际读取：3；另有公开摘要级核对，等级分别披露。
- 最强直接覆盖已经确定：一负方向常系数 Jacobi/半圆律模型与截断谱收敛；候选根公式属于其明确专门化。
- 一般共振缺陷的无限系统失稳现象也已有早期覆盖，不能只因离散 map 实现不同而忽略。
- 当前精确非线性族的 $N$ 一致真实 Floquet 稳定—失稳定理：本记录未证明；其先例是否完全覆盖亦未完成穷尽排除。
- 未给世界新颖性、论文容量或立项结论；未实验、未编译、未新增稿件或改动旧报告。
- 唯一新增本地文件为本记录，SHA-256 在交付消息提供。
