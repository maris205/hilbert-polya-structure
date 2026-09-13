# Paper29 多因子二次 Hénon 迹微分 jet：精确查新与价值预筛

检索日期：2026-09-05；收束更新：2026-09-06，文件名沿既定分配保留。范围：实际作者证明的文献碰撞与成文价值预筛，不是完整独立证明验收、正式价值门槛审查或 Route A/B 评价。

## 1. 输入、执行边界与结论

完整阅读输入为 [作者证明 V1](PAPER29_CYCLIC_HENON_JET_PROOF_V1_20260905.md)，SHA-256：
d6da24f8aa6ada330612a10cf8974925450a3250c598b58cb405f12cef79c683。
随后核验 [作者证明 V2](PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md) 与 V1 的全部差异，V2 SHA-256：
f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0。
V2 仅修复式 (18) 的两处加号和式 (36) 后行列式引理等式的一处加号；结论、参数域和证明论证未变。以下以 V2 为当前输入。
据主控 2026-09-06 交付状态通知，主证明 V2 的完整数学独立审查已经通过；本轮不重开未变输入。该状态与本报告的新意/价值判断分开记录。随后完整阅读刚交付的边界作者补充，见 §5.1；其独立审查状态仍另计。

预筛结论：**没有找到精确覆盖“所有选字的最优必要 jet 阶 + 任意指定宏周期的显式达界 + 模 6 共振二阶补秩”的已有结果。该组合具有真实、可定位的专门结构新意，不应自动沿用已停止单因子短注的价值判断。**
但反可积轨道、乘子作坐标、循环矩阵 Fourier 谱、收缩与 Cauchy 估计均不是新方法；本稿也尚未解决一般 Hénon 谱重构或所有标记分量的独立性。主证数学审查已通过，不自动意味着达到项目要求的独立论文价值。

条件性检索新意评分：**7.5/10**；建议：**PROCEED WITH CAUTION，接续针对实际定理的独立价值审查**。此分数不是正式验收分，也不宣告任何既定高分门槛通过。新边界补充如纳入交付，应单独接受尚未完成的数学审查，不重做主证审查。
成文判断是“有独立专门结构论文的实质候选内容”，不是“已足以支撑任意预设篇幅的长论文”。

本轮仅新建本报告，未改旧稿、锁、项目或索引。采用 research-lit 与 novelty-check 的主张拆解、原始来源核查和经典工具扣除步骤；未配置独立 Codex 审稿 MCP，故未声称完成技能中的固定模型交叉审查。

## 2. 究竟在查什么

固定
\[
H_c(x,y)=(x^2+c-y,x),\qquad
F_{\epsilon,u}=H_{c_k}\circ\cdots\circ H_{c_1},
\qquad c_j=\epsilon^{-2}(u_j-1).
\]
参数维数是逐因子的 \(k\)，不是总次数 \(2^k\) 的完整多项式系数维数。
在 \(u=0\) 上，\(F=H_{-\epsilon^{-2}}^k\)；微分仍沿全部独立因子方向。
对宏周期 \(n_i\) 的标记循环，作者研究
\[
K_{ij}=\frac{1}{n_i\rho_i}\frac{\partial\rho_i}{\partial u_j},
\qquad \rho_i=\operatorname{tr}DF^{n_i}.
\]
因此目标不是轨道方程对状态变量的 Jacobian、不是 \(DF^n\)，也不是未经归一化的 \(D_c\rho\)。

| 主张 | 实际量词与内容 | 新意判断 |
|---|---|---|
| C1：普遍必要阶 | 任意 \(k\) 个周期分支、任意宏周期，在等尺度 power locus 有 \(\det K=O(\epsilon^{r_k})\)，其中 \(r_k=k-1\) 或 \(k+1\)，例外恰为 \(6\mid k\) | 具体迹参数微分的普遍 jet 约束未见精确 prior；单独的循环矩阵零模判断很初等 |
| C2：显式达界与补秩 | 每个正整数周期向量均有显式、互异、简单、精确周期的选字；\(\det K=-b_kP(a)\epsilon^{r_k}+O_k(\epsilon^{r_k+1})\)，共振缺失的两方向由二阶补回 | 最有辨识度的贡献，与 C1 合起来才构成最优性定理 |
| C3：周期一致的定量展开 | 误差、共同定义域和重标度后的奇异值比较常数只依赖 \(k\)；非共振固定 \(u\) 邻域，共振仅 \(u=\epsilon v\) 小域 | 分析工具经典，但对所有周期及退化方向同时统一的结论不是逐个 IFT 的自动推论 |
| C4：标记迹坐标推论 | 每个周期向量至少一个标记关联分量上 dominant、generically étale | 主要是 C2 的标准代数几何后果，不能单列为同等重量的新主定理 |

这里 \(a_i=1\)（\(n_i=1\)）或 \(1-1/n_i\)，
\(P(a)=\sum_i\prod_{j\ne i}a_j\)；
\(b_k=1-\cos(k\pi/3)\)（非共振）或 \(3k^2/32\)（共振）。
共振域 \(u=\epsilon v\) 只改变取值点，不改变求导变量；若改对 \(v\) 求导，行列式额外增加 \(k\) 阶。任何“最优阶”陈述都应保留这一坐标与归一化限定。

## 3. 最接近的原始来源

以下区分正式发表结果与本轮读取的预印本版本。来源核查针对与本稿相交的定理、定义或证明段落，不声称逐行审过每篇全文。

| 原始来源、年份/状态 | 本轮核查位置与已有内容 | 与实际候选的差别 |
|---|---|---|
| Gorbovickis, *Algebraic independence of multipliers of periodic orbits in the space of polynomial maps of one variable*, 2013 预印本 / ETDS 2016，[原文](https://arxiv.org/html/1305.0867v1) | Theorem 1.6、Lemma 2.1、§3 导数公式：任意指定周期的一元多项式乘子代数独立；同一个 \(z^d\) 基点可逐周期向量选满秩标记 | “同一基点、任意指定周期、选若干乘子作坐标”本身已有。这里的非零 Jacobian 二维可逆 \(k\) 因子子族及其最优退化阶不在该定理内 |
| Gorbovickis–Taflin, *Independence of multipliers in several variables complex dynamics*, 2024 / 本轮读 2025 v2，[原文](https://arxiv.org/html/2411.12856v2) | Theorem 1.1 与参数空间定义：正则多项式自映射的指定乘子独立性，周期有下界限制 | Hénon 自同构不是所用 \(\mathbb P^n\) 正则自映射空间的一员；环境空间独立性也不能直接限制到本稿特殊复合子族 |
| Cantat–Dujardin, *Multiplier rigidity for complex Hénon maps*, 2026 预印本，[原文](https://arxiv.org/html/2603.09445v1) | Theorems B、3.5、3.7：固定 multidegree 与 multi-Jacobian 的完整迹谱有限纤维，且存在统一有限周期截断；§5.3 给出正规形的有限歧义 | 已覆盖本稿族的完整谱刚性背景，故“存在某些谱局部信息”不是从零开始；但没有给出任意预定周期的恰好 \(k\) 个标记迹、power locus 的逐阶秩或精确前因子 |
| Bianchi–He, *A thermodynamic path metric for complex Hénon maps*, 2026 预印本，[原文](https://arxiv.org/html/2606.29363v1) | Introduction、Theorem 1.1、Proposition 3.4：复不稳定乘子 cocycle 的半正定协方差型及非退化路径距离 | 周期对数乘子平均与无穷谱微分背景已有；文中并未声称每一点的协方差型正定，更没有本稿指定有限谱的共振 jet 分解 |
| Sterling–Meiss, *Computing periodic orbits using the anti-integrable limit*, Phys. Lett. A 1998，[原文](https://arxiv.org/html/chao-dyn/9802014) | §2、Theorem 1、式 (5)–(10)：二符号反可积 Hénon 轨道的统一收缩延拓，阈值独立于符号序列 | 不能把“所有周期在同一小参数区间存在”当作本稿创新。新增对象是轨道已存在后，对逐相位系数的归一化迹微分及其秩分层 |
| Arai–Chen, *More on the Concept of Anti-integrability for Hénon Maps*, 2025 预印本，[原文](https://arxiv.org/html/2505.15346v1) | Introduction、§2：回顾固定 Jacobian 的经典反可积极限，并研究不同参数尺度的反可积状态 | 支持反可积机制属于成熟工具；未提供本稿的参数迹矩阵、模 6 最优阶或任意周期选字证书 |
| Cvitanović–Liang, *A chaotic lattice field theory in two dimensions*, 2025 v2 预印本，[原文](https://arxiv.org/html/2503.22972v2) | Introduction、§IV、§VIII：带状 orbit Jacobian、Bloch/Fourier 稳定性与 Hill 联系；式 (55)–(59) 的算子作用于状态扰动 | 同样有循环格点与乘子稳定性语言，但 Jacobian 是轨道方程/场方程对状态变量的导数，不是多条周期迹对 \(k\) 个参数的 Jacobian |
| 工作区 P18，*marked Hénon scalar boundary*，[研究问题](../../papers/18-marked-henon-scalar-boundary/notes/RESEARCH_QUESTION.md) | 已读 RQ4、A3/A4、查新记录及 PDF 前三页：单因子、标记关联空间与从退化点延拓到一般 Jacobian 切片 | C4 的关联簇操作、满秩见证方法与单因子框架有重复；P18 未给多因子 power locus 的最优阶/二阶共振恢复 |

### 三个最容易误判的关系

第一，完整谱有限纤维可结合特征零与局部标记，支持“某处可从谱中选出足够微分信息”的一般推断；这不是 Cantat–Dujardin 原文中的任意指定周期定理，也不能保证本稿的具体 power locus 点不分歧。因此本稿若只宣传“若干迹泛型独立”，价值会明显缩水；真正区别必须放在 C1–C3。

第二，格点 Hill 行列式可连接一个周期的状态稳定矩阵与其 return multiplier，但再对多个外部参数微分、比较不同周期并求 \(k\times k\) 行列式，是另一个问题。不能因为双方都有 cyclic、Jacobian、trace、periodic，就认定已有 theorem 覆盖；也不能因为问题不同，就把 Bloch/Fourier 计算据为新技术。

第三，\(u=0\) 的额外对称性并不制造一个连续 gauge 方向：逐因子正规形参数只有有限正规形歧义。另一方面，有限对称会置换周期标记；标记谱矩阵与无标记谱映射在对称点的微分行为不相同。特别是 \(n_i=1\) 的相位移位固定点可属于同一 elementary Hénon 周期，但它们仍是不同的 \(F\)-固定点，不能提前合并。

## 4. 经典工具扣除之后，还剩多少数学内容

| 作者证明模块 | 应扣除的标准内容 | 本稿实际需要证明的非自动部分 |
|---|---|---|
| §§3–4，轨道与 Riccati 分支 | 二符号收缩延拓、双曲乘子分裂、对数乘积、Cauchy 估计 | 对归一化迹微分的周期无关余项；穷尽所有周期分支，才能支持 C1 的全称量词 |
| §5，一阶 jet | \(I-S-S^{-1}\) 的 Fourier 对角化；\(1-2\cos\theta=0\) 的两根；\(6\mid k\) 的算术条件 | 从任意周期的相位平均得到同一个普遍一阶算子，而不只在若干测试词上观察它 |
| §§6–7，二阶 jet 与选字 | Taylor 展开、近邻相关函数与有限维线性代数 | Riccati 修正与轨道位移项共同给出的正确二阶压缩；任意宏周期 marker 选字产生统一正的频率系数 |
| §8，精确最优阶与奇异值 | 行列式引理、Chebyshev 乘积与矩阵扰动 | 非共振与共振的同一达界公式、精确 \(b_kP(a)\)、两条二阶方向和所有周期的一致下界 |
| §9，共同参数域 | 消去公共零阶行、参数依赖基变换与紧性 | 共振方向在 \(u=\epsilon v\) 中的正确阶数账本；不能以逐项 \(O(\epsilon^3)\) 冒充整个退化行列式误差 |
| §10，关联分量推论 | Jacobian criterion、简单标记覆盖与泛型 étale | 所需主要输入已经是 C2；不应重复计分 |

据此，真正可独立定位的成果不是“用了 AI 或 Riccati”，而是一个**谱参数微分在对称退化点附近的有限阶秩结构定理**：
共同的第一阶障碍限制了所有谱选取，而一个可计算的第二阶项恰好在例外模类补回两维，且这一最优界可由任意指定宏周期的显式标记达到。
这比“发现一个满秩样例”多出必要性和最优性两层，不能简单缩成已停止单因子结果的换记号版本。

反过来，新机制的普适范围仍有限：二次因子、各 Jacobian 为一、特定等尺度 power locus、给定归一化；尚无多次数/多 Jacobian 的分类，也无全局谱重构应用。没有必要为了成文把这些未做的问题列成已经得到的推论。

## 5. 检索覆盖与未解决的不确定性

本轮与紧邻的同一候选查新连续检查了以下方向，每组采用至少三种组合表述；不是仅搜索最终拟定标题：

- C1：Hénon trace jet / multiplier vanishing order / power locus / unfolding iterate / cyclic parameter Jacobian。
- C2：Hénon modulo six / mod 6 multiplier resonance / anti-integrable second-order rank / prescribed periods composition multipliers。
- C3：uniform multiplier independence / high escape trace coordinates / all periods anti-integrable derivatives / shrinking resonant parameter neighborhood。
- 碰撞补查：cyclic lattice Hill determinant / orbit Jacobian Bloch / composition fixed multi-Jacobian multipliers。

包含 2024–2026 年份限定及最近六个月（2026-03-05 至 2026-09-05）的定向查询，并使用 arXiv 及 Google Scholar、Semantic Scholar 域名限定的公开搜索。后两者域名检索未带来额外可核实的精确匹配；大量结果属于 Hénon–Heiles、数值 Lyapunov 指数或无关六阶共振，均未作为证据。该纯数学问题不因技能模板列出 ML 会议而把 ICLR/NeurIPS/ICML 当作核心数据库。

没有本地新增下载 PDF；外部判断只依据上述原始来源实际核查的位置。有限检索的“未找到”不是对所有已发表或未索引文献的不存在证明。尤其需要最终作者明确引用早期反可积/Hill 工作，避免审稿人把标准工具的重新推导误读为声称首创。

### 5.1 刚交付边界补充的准确增量

已完整读取 [共振边界作者补充](PAPER29_CYCLIC_HENON_RESONANCE_BOUNDARY_20260905.md)，544 行，SHA-256：
c43b33be00c0051e7f3cdb429221ff36a212b8e19aa6e3acd724a3cd229c2ef9。
它不是消息预告，也不是独立验收记录；本报告只按实际文本归类新增主张，不宣告其数学审查通过。

对每个 \(6\mid k\)，严格限定 \(n_i=1\) 的同一组单负号标记，补充在 \(u=\epsilon v\) 中得到
\[
\left.\epsilon^{-(k+1)}\det K_u(\epsilon,\epsilon v)\right|_{\epsilon=0}
=-\frac{3k^3}{32}\bigl(1-4\widehat v_+\widehat v_-\bigr),
\qquad
\widehat v_\pm=\frac1k\sum_{j=0}^{k-1}v_j e^{\mp2\pi i j/3}.
\]
实际推导包含移动公共零阶行的消去、两维共振块和其余方向的 Schur 项；不是只把 \(u=0\) 的矩阵投影后猜测。其 \(2\times2\) 极限块为对角元 \(3/4\)、非对角元 \(-3\widehat v_\pm/2\)。由此给出 leading critical cylinder \(\widehat v_+\widehat v_-=1/4\) 附近的实际全纯退化超曲面；在 \(v_j=t\cos(2\pi j/3)\) 上有 \(t_\pm=\pm1+O(\epsilon)\)，此处所选矩阵秩恰为 \(k-1\)，而固定点仍简单、互异。

这是 C3 的有意义边界补充：排除同一固定 tuple 在任何 \(\epsilon\)-无关 \(u\) 邻域内处处满秩。它既不否定换词恢复满秩，也不涵盖任意周期向量，不分类全部 critical scheme，更不证明缩小域具有唯一最优的各向异性形状。状态变量双曲性与谱参数映射临界性必须继续分开。

本轮已完成的相邻主题检索未见该具体公式的精确 prior；未为此重复启动同一轮泛关键词检索。它加强了“秩恢复何时再次退化”的可读结构，但依赖已算出的一、二阶 jet，不能按新增一个完整独立机制计分。因此保留上述 7.5/10 条件性查新判断，不凭文件长度或新增一个定理标题上调至 PASS。

## 6. 对后续独立审查的具体建议

以下前三项保留本报告识别的主证审查敏感点，供价值审稿理解实际技术负载；主证数学独立审查已经通过，不要求重开未变输入。第四项仍是价值审查的实质问题。边界补充的未完成审查另限于该补充实际增量。

1. **全称下界的完整性。** 统一符号模型穷尽所有周期分支；一阶 kernel 对任意周期相位平均成立；归一化余项独立于周期。
2. **二阶常数的来源。** Riccati 的 \(-\epsilon^2/w_{t-1}\) 项、跨宏块边界相关函数和共振压缩的 \(3/4\)；\(k=2\) 保留 \(S=S^{-1}\) 的重边效应。
3. **最优阶到共同域的过渡。** Fourier 列重标度、依赖 \(u\) 的零阶消去及奇异值比较；结论不能只由一个渐近行列式非零替代。
4. **价值是否在精确陈述后仍成立。** 独立审稿人应评价 C1–C3 组合，而不是单看“mod 6”或“generic étale”。若认为其只是一个可在既有论文中附加的短推论，应给出实际可替代的 theorem/lemma 链，而非仅以工具经典为由断言。

建议定位：**“Optimal trace-differential jet orders near quadratic Hénon powers”** 与当前证明一致。
不建议使用“完整 Hénon 谱局部坐标分类”“一般辛映射模 6 普适律”或“共振导致所有谱坐标失效”。
最终结论仍是：具体新意可信、价值候选成立；主证数学独立审查已完成，边界补充的独立审查和正式成文价值验收另计。本报告不创建 PASS、正式项目或论文锁。
