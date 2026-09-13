# Paper30 T 分支：全有限支撑与形式全阶命题的一手文献有界查新

日期：2026-09-06。性质：独立查新探针；Paper30 未立项，本文件不是证明、Route 评价、容量评分或论文完成记录。

## 1. 结论先行

本次一手检索**未找到直接证明或否定下述 C1、C2、C3 的文献**。这只是有界检索结论，不是“世界首次”证书，也不是三个命题已经成立的证据。

与任务最接近、必须明确扣除的先例是：

- 对线性环面自同构，Fourier 频率轨道系数和刻画同调方程可解性的工作已经存在。
- 对圆周整数扩张映射，甚至已有“有限三角多项式目标＋可测原函数 ⇒ 原函数几乎处处为有限三角多项式”的明确代数化结果。
- 对负曲率测地流，已有有限球面谐波度目标强迫有限球面谐波度原函数的定理；它不是二维环面完整 Fourier 格点支撑的定理。
- Livšic 的 Hölder 存在性、光滑／解析正则性、参数正则性和逐阶同调递推都不能单独完成本问题的有限 Fourier 支撑结论。
- 对固定有限维目标空间，一旦已有足秩的实际周期矩阵见证，解析性产生离散参数例外；对可数个支撑取并得到可数例外。这段通用推论本身不能作为主要新贡献，也不能代替足秩见证。

本次不改变两个输入文件记录的科学状态，不重复有限原函数拉回分类、不重做七维周期检验、不新增小支撑清单。旧常量目标在三阶失败，不是一般形式全阶命题的反例。

## 2. 输入及三个精确 claim

已完整阅读：

1. [有限 Fourier 拉回分类与一次小支撑周期检验](PAPER30_TORUS_FOURIER_FIRST_PROBE_20260906.md)。
2. [形式尾部一般首阶判据与一次三阶障碍](PAPER30_TORUS_FORMAL_TAIL_OBSTRUCTION_PROBE_20260906.md)。

固定
\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad
F_\kappa=A\circ S_\kappa,\quad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)).
\]
令 \(\mathcal T\) 为复系数有限 Fourier 多项式，
\[
\mathcal B=\{f(q)-f(q-p):f\text{ 为一元有限 Fourier 多项式}\},
\quad
\mathcal P_\kappa=\left\{g\in\mathcal T:
\sum_{j=0}^{n-1}g(F_\kappa^jx)=0\ \forall n\ge1,\ F_\kappa^nx=x\right\}.
\]
以下 \(I\) 指含零的固定实 Anosov 参数小区间；不指定或估算其数值宽度。

| Claim | 本次查新的精确量词 | 不能替代它的弱结论 |
|---|---|---|
| C1：固定非零参数、全部有限支撑 | 对给定 \(\kappa_0\in I\setminus\{0\}\)，是否 \(\mathcal P_{\kappa_0}=\mathcal B\)？任意有限支撑、任意系数；要对全部小非零参数成立时，再量化 \(\kappa_0\)。 | 已假定原函数有限的拉回分类；一个七维空间；对每个支撑分别缩小参数邻域。 |
| C2：一般参数、全部有限支撑 | 是否存在至多可数 \(E\subset I\setminus\{0\}\)，使每个 \(\kappa\notin E\cup\{0\}\) 同时满足 \(\mathcal P_\kappa=\mathcal B\)？“generic”在这里明确取可数例外版本。 | 大函数空间中 generic observable 不是余边界；大映射空间中 residual 性；只知道固定 \(V\) 的周期秩在一般参数最大。 |
| C3：形式全阶刚性 | 对每个固定有限 Fourier 空间 \(V\)，若 \(G\in V[[t]]\)、\(H\in\mathcal T[[t]]\)，且 \(G=(F_{t/\pi}^*-1)H\)，是否 \(G\in\mathcal B[[t]]\)？每个 \(H_j\) 有限，但不要求统一支撑；不要求收敛。 | 有限阶障碍；固定常量目标的失败；原函数有统一有限支撑；解析收敛族的专门结果。 |

C2 比一个指定非零参数的 C1 弱；可数例外集完全可能包含该指定参数。C3 是不同类别的命题，不能直接在非零参数处代入形式级数。

## 3. 最近的基础一手来源：覆盖内容与精确差额

所有正式引文都链接原研究论文的期刊页、arXiv 作者稿或作者／机构保存稿。没有使用搜索聚合页、百科、自动文献综述或论坛作为定理依据。

| 一手论文；状态 | 已核实的内容与定位 | 对三个 claim 的覆盖／差额 |
|---|---|---|
| A. N. Livšic, **Cohomology of dynamical systems**, Math. USSR-Izv. 6 (1972), 1278–1301；已发表。[原刊记录](https://www.mathnet.ru/eng/im2373) | 周期障碍刻画适当双曲系统上的同调平凡性。复数值 Hölder 版本在下列 Navas–Ponce 原研究稿 Theorem 3 中有完整表述和证明。 | 是 C1 的原函数存在性基础，不是有限支撑代数化。 |
| R. de la Llave, J. M. Marco, R. Moriyón, **Canonical perturbation theory of Anosov systems and regularity results for the Livsic cohomology equation**, Ann. Math. 123 (1986), 537–611；已发表。[原刊记录](https://annals.math.princeton.edu/1986/123-3/p03) | 原刊无摘要，本次未取得该刊全文；其正则性与参数工具通过作者后续 de la Llave–Windsor 论文的明确 Proposition 2 及论证核对。不假称已逐条阅读 1986 全文。 | Anosov 扰动与同调正则性不是新问题；不据题名推断其证明 C3。 |
| R. de la Llave, **Analytic regularity of solutions of Livsic's cohomology equation and some applications to analytic conjugacy of hyperbolic dynamical systems**, ETDS 17 (1997), 649–662；已发表。[原刊摘要](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/analytic-regularity-of-solutions-of-livsics-cohomology-equation-and-some-applications-to-analytic-conjugacy-of-hyperbolic-dynamical-systems/4CE577B65DA918DF51661B55B6CBC90E) | 摘要明确：解析 Anosov 向量场与解析右端的连续解为解析，并有微分同胚的对应结果。本次访问层级为原刊摘要，未虚构定理编号。 | 即便取得解析原函数，仍可能有无限 Fourier 尾部；不直接覆盖 C1，更不覆盖无收敛假设的 C3。 |
| A. Dehghan-Nezhad, A. El Kacimi Alaoui, **Équations cohomologiques de flots riemanniens et de difféomorphismes d'Anosov**, JMSJ 59 (2007), 1105–1134；已发表。[原刊全文](https://www.jstage.jst.go.jp/article/jmath/59/4/59_4_1105/_pdf/-char/en) | §5、Theorem 5.1：对双曲、可对角化且特征值实正的整数行列式一矩阵，按转置矩阵的格点轨道定义 Fourier 系数和 \(\ell_m\)；这些条件刻画光滑同调方程像，构造解算子。这里的 \(A\) 满足其线性假设。 | 直接覆盖 \(\kappa=0\) 的频率轨道障碍机制；有限序列离散求和是其有限支撑特例。不能将线性 Fourier 轨道搬成 \(F_\kappa\) 的频率轨道。 |
| Yu. I. Lyubich, **Axiomatic theory of divergent series and cohomological equations**, Fund. Math. 198 (2008), 263–282；已发表。[原刊全文](https://www.impan.pl/shop/en/publication/transaction/download/product/88685)、[作者元数据](https://arxiv.org/abs/0705.1578) | Corollary 4.9：整数 \(q\ge2\)，若有限三角多项式 \(\theta\) 的方程 \(\psi(x)-\psi(qx)=\theta(x)\) 有可测解，则 \(\psi\) 几乎处处为有限三角多项式。Theorem 4.10 给出乘 \(q\) 频率链上的系数和分类。 | **确有有限 Fourier 原函数代数化先例**。但底映射是非可逆线性圆周扩张，不是本二维可逆非线性剪切 cat；不能直接覆盖 C1/C2/C3。 |
| R. de la Llave, A. Windsor, **Smooth dependence on parameters of solutions to cohomology equations over Anosov systems with applications to cohomology equations on diffeomorphism groups**, DCDS 29 (2011), 1141–1154；已发表。[原刊](https://www.aimsciences.org/article/doi/10.3934/dcds.2011.29.1141)、[作者稿全文](https://arxiv.org/html/0809.1235v1) | Proposition 2：固定传递 Anosov 底映射 \(f\)，每个参数均满足周期障碍，并在一个周期点施加平滑参数规范，右端的相应混合 Hölder／参数正则性传给解。§1.1.2 解释对周期障碍求导及随后证明真导数。 | 固定 \(f\)、预有全参数可解性；不能直接改为 \(f=F_\kappa\) 并维持原坐标有限 Fourier 空间。参数正则性也不产生有限支撑。 |
| A. Navas, M. Ponce, **A Livšic type theorem for germs of analytic diffeomorphisms**, Nonlinearity 26 (2013), 297–305；已发表。[作者稿全文](https://arxiv.org/html/1110.1911v1) | Main Theorem：紧度量空间上传递且满足 closing property 的底同胚，Hölder 的原点解析微分同胚芽值 cocycle 满足周期障碍，则有同类别 Hölder 转移函数。§1.3 先逐阶解标量同调方程，再用 majorant 控制得到正收敛半径。 | 与 C3 的“逐阶解＋必须另控全阶”机制最近；其展开变量是纤维芽坐标，系数是底空间 Hölder 函数，非本 \(\mathcal T[[t]]\) 的固定目标支撑问题。 |
| C. Guillarmou, G. P. Paternain, M. Salo, G. Uhlmann, **The X-ray transform for connections in negative curvature**, CMP 343 (2016), 83–127；已发表。[作者元数据](https://arxiv.org/abs/1502.04720)、[机构全文](https://api.repository.cam.ac.uk/server/api/core/bitstreams/5b41fa20-152b-4512-93d8-2ad9d1f082da/content) | Theorems 4.1、4.6：紧负截面曲率流形、Hermitian 联络（4.6 另有 skew-Hermitian Higgs 场），光滑 \(u\) 解 \((X+\Phi)u=f\)，\(f\) 有有限球面谐波度，则 \(u\) 亦有限度；有边界时要求 \(u\) 边界零。 | 同是尾部刚性，但分解是 \(SM\) 的速度球面纤维谐波，证明靠负曲率 Pestov 能量估计。不能把“Anosov”单词或“Fourier degree”名称相同当作 C1 覆盖。 |
| F. Naud, **On the rate of mixing of circle extensions of Anosov maps**, arXiv:1612.05011 (2016)；本次按预印本处理。[作者元数据](https://arxiv.org/abs/1612.05011)、[全文](https://arxiv.org/html/1612.05011v1) | Theorem 1、§4.2：底映射为保体积实解析线性 Anosov 小扰动，对足够大的固定 Laplace 截断，Gaussian 随机三角多项式 roof 几乎必然给 rapid mixing 圆周扩张。 | 底映射类别可含本族，但随机量是 roof **系数**，不是指定剪切参数 \(\kappa\)。不刻画全部 exceptional coboundaries，因此不推出 C2 的核恰好为 \(\mathcal B\)。 |

### 3.1 为什么 Livšic 正则性没有完成 C1

有限 Fourier 是强于解析性的代数限制；一般解析周期函数有无限 Fourier 支撑。原函数仅在环面附近的复带中解析，也不等于它能在整个 \((\mathbb C^*)^2\) 上延拓并满足 Laurent 多项式增长界。

因此，即使应用解析 Livšic 得到解析 \(h\)，首作者记录中“按纵向频率分组得到 Laurent 多项式，再作复射线增长矛盾”的步骤仍缺关键假设：无限 Fourier 原函数的分组系数不再是 Laurent 多项式。用结构稳定共轭把 \(F_\kappa\) 变回线性 \(A\) 同样不保留原坐标中的有限 Fourier 支撑。以上是本报告的适用性分析，不是对 C1 的新证明。

## 4. C2 必须扣除的通用参数论证

以下是基本有限维线性代数、周期点的解析隐函数延拓及一变量解析函数零集性质的条件性分析，不作为新研究定理登记。

固定有限 Fourier 空间 \(V\)，设 \(B_V=V\cap\mathcal B\)，\(d=\dim(V/B_V)\)。每条实际延拓周期轨道给出 \(V/B_V\) 上的解析参数线性泛函。若已经证明存在 \(d\) 条这样的轨道，使商矩阵某个 \(d\times d\) 行列式不是恒零，那么该行列式的零集在解析延拓区间内部离散；零集外已能检测 \(V/B_V\)。这不需要新 Livšic 存在性定理。

若**对每个有限格点支撑**都完成了这种非恒零足秩见证，支撑集合可数，对支撑例外集取可数并便给出 C2 型共同例外集。得到的是可数例外，不保证例外集仍离散，也不保证存在一个对全部支撑统一的零附近穿孔区间。

真正没有自动得到的是：每个 \(V\) 的最大周期秩等于 \(d\)。通用解析论证只说“最大秩在一般参数出现”，却不说明这个最大秩有多大。一个余维仍然不足的核分支完全可能对整个参数族持续存在；排除它正是新的科学义务。不能从七维空间的见证推到所有 \(V\)，也不能把大函数空间或大映射空间中的 generic 结论限制到预先固定的一维族而不查横截性。

Naud 的随机 roof 结果进一步说明：即使“几乎每个有限 Fourier observable 非余边界”已知，也只说明余边界构成的子空间不占满系数空间；这与识别那个子空间究竟是否恰为 \(B_V\) 不同。

## 5. C3：现成变形方法实际覆盖到哪里

输入文件已证明的递推
\[
\delta_0H_n=G_n-\sum_{j<n}T_{n-j}H_j,
\qquad
\Pi(G_n)=\Pi\!\left(\sum_{j<n}T_{n-j}H_j\right)
\]
与标准“逐阶解同调方程、把下一阶残差投影到余核”的方法一致。线性余核的来源可由 2007 年环面论文精确定位；参数导数与障碍的兼容见 de la Llave–Windsor；三角型逐阶构造以及另加收敛控制见 Navas–Ponce。不能仅因本例出现第三阶而把整套递推机制认作新方法。

未被这些文献替代的是同一个量词：**目标全部阶次固定在任意给定有限 \(V\)，原函数各阶有限但支撑可增长，仍只有 \(\mathcal B[[t]]\) 能无限继续。**现成参数平滑定理不强迫 \(H_n\in\mathcal T\)，正收敛半径定理不自动给有限支撑，有限阶零障碍也不自动保证全形式解存在。

本次只保留一个同族的定理级入口：排除固定 \(V/B_V\) 中能在所有阶次持续存在的非零分支。若用它连接 C2，还须明确建立所用“形式周期核／形式同调解”桥梁并检查函数类别；不能只引用参数 Livšic 或形式级数可求导。这里是在定位缺失义务，不新增支撑筛查、实验或证明任务。

## 6. 2024–2026 与最近六个月核对

近两年检索显式包含 2024、2025、2026；最近六个月按 **2026-03-06 至 2026-09-06** 处理。日期以期刊发表记录和 arXiv submission history 为准，不使用搜索引擎的 crawled 日期或 HTML 自动生成的 “Date” 作为论文新发表日期。

| 一手近期来源 | 已核对内容 | 本任务的覆盖判断 |
|---|---|---|
| C. Dilsavor, J. Marshall Reber, **A positive proportion Livshits theorem**, Proc. AMS 152 (2024), 4729–4744；2023 预印本、2024 已发表。[作者稿](https://arxiv.org/html/2304.01372v2)、[DOI](https://doi.org/10.1090/proc/16880) | Theorem 1.1：传递 Anosov 微分同胚，实 Hölder observable 的零周期集具有某 Hölder 权重下正渐近上密度，则它是 Hölder 余边界。 | 减少需要检查的周期条件；不增加原函数 Fourier 支撑性，也不是固定有限数量轨道检测任意支撑。 |
| L. Backes, D. Dragičević, Y. Hafouta, **Livšic regularity for random and sequential dynamics through transfer operators**, arXiv:2508.08972；2025-08-12 首稿，2025-11-25 v2。[元数据](https://arxiv.org/abs/2508.08972)、[全文](https://arxiv.org/html/2508.08972v2) | 非自治、随机和 sequential 系统的余边界正则性；§5 包含双曲映射小扰动及符号编码。 | 类别接近但结论是正则性与方差增长判据；没有本单参数族的有限 Fourier 核分类。 |
| S. N. Simić, **The Livšic equation on differential forms over Anosov flows and applications**, arXiv:2511.05678；2025-11-07。[元数据](https://arxiv.org/abs/2511.05678)、[全文](https://arxiv.org/html/2511.05678v1) | Lie 导数作用于微分形式；asymmetric Anosov 流的特定次数连续可解性、像闭包与可积性。 | 既不是离散二维环面标量方程，也没有固定 Fourier 支撑形式变形的结论。 |
| J. Santana C. Costa, F. Micena, **A generalized Livšic–Sinai Theorem for endomorphisms**, arXiv:2606.15542；2026-06-14，在六个月窗内。[元数据](https://arxiv.org/abs/2606.15542)、[全文](https://arxiv.org/html/2606.15542v1) | Theorem B：传递 Anosov endomorphism 上 \(C^1\) 实函数的全部周期和零，存在模常数唯一的 \(C^1\) 原函数。Theorem A 另要求非游荡集完全不变及周期 Jacobian 条件。 | 实质是可微正则性与非可逆系统；没有有限 Fourier 或 C3。不得将摘要的简述替代正文附加假设。 |

近期结果没有消除本任务中“正则性不等于有限支撑”的差额。有关高秩 Abelian KAM 刚性、Anosov representations 或微局部谱的搜索命中，因为对象、作用秩或方程不同，未展开为新方向；本次未把它们纳入本族候选。

## 7. 实际检索表述与范围

下表记录实际执行过的核心查询表述；每个 claim 不少于三种。查询中的引号、英文转写 Livsic／Livšic、year 与 date filter 用来交叉校验，搜索无结果本身不证明不存在文献。

| Claim | 基础／同义查询 | 2024–2026 与六个月查询 |
|---|---|---|
| C1 | `Livsic trigonometric polynomial coboundary nonlinear perturbation cat map finite Fourier support`；`Anosov torus analytic cohomological equation polynomial coboundary Livsic rigidity`；`"perturbed cat" "cohomological"`；`"Livsic" "finite Fourier"`；`"Livsic" "algebraization"`；`"trigonometric coboundaries" nonlinear` | `site:arxiv.org Anosov Livsic "Fourier" 2024 2025 2026`；`site:arxiv.org "cat map" "cohomological" 2024 2025 2026`；`"Anosov" "trigonometric polynomial" after:2026-03-06 before:2026-09-07` |
| C2 | `"Anosov" "coboundaries" "generic" analytic family parameter`；`"cat map" "coboundary" nonlinear perturbation generic`；`"generic" "coboundary" "analytic family" Anosov`；`"circle extensions" "Anosov" "trigonometric polynomial"` | `site:arxiv.org Livsic generic analytic parameter coboundary 2024 2025 2026`；`"Livsic" "analytic family" after:2026-03-06 before:2026-09-07`；另以 arXiv 域和 184 天 recency 查 `Livsic formal parameter analytic rigidity 2026` |
| C3 | `"formal" "cohomological" "Anosov" deformation obstructions`；`"finite Fourier" "cohomological equation" deformation`；`"Anosov" "formal power series" cohomology`；`"Livsic" "holomorphic germs"` | `site:arxiv.org Anosov formal deformation cohomology 2024 2025 2026`；`"Anosov" "deformation" "Fourier" 2024 2025 2026`；`"Anosov" "formal" "cohomological equation" after:2026-03-06 before:2026-09-07` |

另逐年搜索 `"Livšic" "2024"`、`"Livsic" "2025"`、`"Livšic" "2026"`，并核验上述近期论文。已读取可能重叠论文的摘要、导言与相关定理／方法段；没有声称把所有远程全文逐页读完。

检索使用公开网页、arXiv 作者稿与期刊／作者页面。当前无 Zotero、Obsidian 或指定 reviewer MCP 接口；未检出技能示例的本地 `arxiv_fetch.py`，按技能允许的 arXiv 网页搜索降级。未登录或完整遍历 Google Scholar／Semantic Scholar 数据库，故不声称覆盖其完整索引。纯数学问题没有为满足通用 ML 模板而堆入 ICLR／ICML／NeurIPS 无关论文。

## 8. 独立性、置信边界与停止

本次已完整阅读 `AGENTS.md`、`docs/WORKFLOW.md`、`research-lit/SKILL.md`、`novelty-check/SKILL.md`。技能使查新按 claim 分解、补足近期窗口、逐项比较一手定理条件，并明确区分“没有直接命中”与“已证新颖”。用户明确禁止评分／容量，所以不使用 novelty-check 模板中的分数或立项推荐。

指定的 `gpt-5.4` reviewer MCP 在当前工具中不可调用。实际核查由主代理另起的 **secondary xhigh 独立代理**完成（独立输入、显式 xhigh）；不是调用了 GPT-5.4 MCP，也不冒称跨模型双审。没有派生子代理；未取得未配置接口的审查结果。

置信边界：对已引用定理的类别差异和通用工具扣除，有可追溯文本依据；对不存在直接先例，只能给**有界未命中**。尤其不能排除未索引文献、其他语言术语、未公开稿件或可由已有一般定理进一步推演得到的覆盖。

输入身份（本次只核对这两个对象）：

```text
cc81f9015c60ce4ab0810fcb911bae6899c99cbdc0764fe80d1e000df88e4230  PAPER30_TORUS_FOURIER_FIRST_PROBE_20260906.md
da8f89945a4e81dc8d44a9935123f8737e3f4ff623bd8e6ca830e8c2e81ef1c7  PAPER30_TORUS_FORMAL_TAIL_OBSTRUCTION_PROBE_20260906.md
```

仅新增本报告；没有改旧稿／登记册／状态／构建树，没有实验、PDF 本地下载、投稿、上传、发信或其他外部写入。到此停止。
