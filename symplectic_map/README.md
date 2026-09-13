# Symplectic-map research session

当前执行入口：[AGENTS.md](AGENTS.md) · [研究工作流](docs/WORKFLOW.md) · [Batch07 当前接续](BATCH_07_CONTEXT.md)。

## 总体进展与 Route A 定位（2026-09-13）

本节归档本轮讨论的结论和建议，范围仅为 `symplectic_map`，不代表整个仓库其他研究流的进度。它是基于现有证据的进展盘点与研究优先级判断，不是新的正式 Route 评分、全球查新或成功概率估计；不回写历史评价，也不自动启动新候选、实验或下一批次。

**核心判断：结构研究已有扎实进展，但面向 RH／Hilbert–Pólya 的正面关卡推进仍有限。当前没有一个候选完成 Route A 的 A0＋A1；连续通关位置仍卡在 A0，而不是“所有系统都已通过 A1”。**

### 已探索的系统族

按合并同族参数变体的研究口径，至少实质探索了 **8 大类系统族**；其中7类进入编号论文／证明项目，标准／twist 映射另有未成篇的实质数学研究。31个编号项目不等于31个不同系统，也不等于31项独立且全部完成交付的成果。

| 系统族 | 对应研究 | 主要内容 |
|---|---|---|
| Logistic／PCF 二次母映射 | P3、P7及P1–2的母系统背景 | 素数乘子、指数时钟、2-adic 障碍 |
| Hénon及广义 Hénon、指定辛扩张 | P1、P4、P12–16、P18、P29 | 保守／耗散对照、周期覆盖、迹坐标、算术逃逸、上同调 |
| Markov–baker 分片辛映射 | P2 | 精确原始轨道账本、符号编码、有限记忆时钟障碍 |
| Cat 环面映射及其扰动 | P8–11及后续笔记 | 素数阶载体、轨道重数、中心化子商、等变结构 |
| 高维 shift-like 递推 | P17、P19 | 有限秩乘法群内的存活、环面平移维数与支撑障碍 |
| 多项式 Hamiltonian 梯度剪切 | P20–28及耦合 kick–drift 笔记 | 次数增长、支撑秩、选择切换、同步置换与 monodromy |
| q-Painlevé I（qPI）及其自治特化 | P30、P31及未成篇接口 | 算术临界结构、完整曲面、原始点阶、实旋转与精确相混合 |
| 标准／正弦及双谐波 twist 映射 | P30选题期间的未成篇研究 | 共轭时间、共振消去、小除数与内部算术结构 |

这个分类不是互不相交的严格数学分类。P5、P6是跨若干构造的通用障碍，不另算新系统；有限域／随机 Hénon并入Hénon，扰动cat并入cat，耦合多项式kick–drift并入多项式剪切。一维PCF母模型和一般shift-like推广不能一概称为辛系统；Hénon研究也包含耗散对照、反辛子族和退化边界。
未成篇不等于只查过文献：例如[正弦twist共轭面积律](docs/research-batch07/PAPER30_CONJUGATE_TIME_DISPOSITION_20260907.md)及[耦合kicked链](docs/research-batch07/PAPER30_RESONANT_LATTICE_SCREEN_DISPOSITION_20260907.md)已有数学接受记录，但不因此计为已交付论文。P12的结果已被P15吸收，P14被P16吸收，不能重复计作独立突破；P19、P23、P24、P26的内部／交付阻塞状态仍按下方索引保留。

### 五阶段研究计划不等于 A0–A4 通关

原[研究路线图](propose-symplectic-map.md#8-suggested-research-stages)中的 Stage 1–5 是课题安排；[Route A 关卡](.agents/skills/route-a-evaluator/references/rubric.md#4-route-a-layers)要求同一个候选的算术来源、轨道、时钟与归一化保持一致。**“高维结构做到 Stage 4”不等于“通过 A4”。**

| 原路线图 | 实际进展 | 未跨过的关键缺口 |
|---|---|---|
| Stage 1：保守／耗散结构基线 | 冻结Hénon候选完成有对照的否定检验；baker提供精确结构对照 | 没有筛出可贯穿后续阶段的强算术候选 |
| Stage 2：周期轨道与Zeta | 原始周期覆盖、轨道商、迹坐标与P29周期概形检测已深入 | 未建立被认可的算术Zeta／Fredholm候选；普通结构Zeta不等于目标行列式 |
| Stage 3：算术辛搜索 | P3–11的时钟／重数障碍明确；qPI已有真实算术—回返接口 | 尚无同一个对象内自然的素数选择、长度／权重和素数幂重复机制 |
| Stage 4：高维／耦合辛映射 | 精确次数递推、任意代数次数、选择周期与矩阵解码 | 结构子目标走得最远，但未由此得到算术容量、目标迹公式或零点计数 |
| Stage 5：量子化与迹接口 | 有辛结构、生成函数等局部启发 | 没有前序算术关卡支撑的正式推进，也未达到Route B就绪 |

正式记录中，P2是 **`A0_FAIL + A1_WEAK`**：周期20以内226条原始轨道核对准确，但冻结有限记忆标量时钟无法容纳全部素数对数，见[终评](evaluations/route_a/pcf_markov_baker/2026-08-13-final.yaml)。P1也因算术来源／冻结载体检验失败而[终评拒绝](evaluations/route_a/henon_homotopy/2026-08-13-final.yaml)；其中 `A4_FORMAL_HINT` 只是生成函数层面的启发，不是A4通过。最新P27–31的[统一审计](docs/research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md)明确为纯数学 `route_applicability: NOT_APPLICABLE`，不授Route A/B层级PASS；未评估不等于科学失败，也不能计作关卡晋级。

### 哪条最成熟，哪条最值得继续考察？

- **一般性结构成果最强：高维Hamiltonian线，P25是核心。** 对每个整数d≥2构造2d维辛多项式映射，所有迭代的普通次数有精确矩阵公式，第一动力次数的代数次数及可见标量序列的最小有理常系数递推阶都恰为d。P22的塌缩结果与P25的支撑秩结果共同说明，增加维数不自动增加有效复杂度。P27–28推进选择机制，但P28仍是每个指定词构造一个随词长增维的映射，不是固定映射生成全部任意长词。依据：[P25证明包](papers/25-hamiltonian-support-rank-unbounded-perron-degree/notes/PROOF_PACKAGE.md)、[P27–28精确边界](docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md)。这些次数矩阵的Perron谱不是Hilbert–Pólya能谱。
- **有效轨道工具最强：Hénon周期—上同调线，P29尤为重要。** 在其特征零Hénon假设下，余边界有保次数原函数，并能由一个足够长的完整周期概形检验；不要求双曲性或简单周期点。这对判断轨道和式是否只是可消去的余边界有价值，但不是素数权重或自然Fredholm行列式。依据：[P29主结果](papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/1_introduction.tex)。
- **后续综合研究优先考察：qPI。** 同一模型家族上已有算术几何与自治实动力学两组精确结果：P30的首层完整临界理想及高层模圆分参数平方的一阶信息，P31在 $T>0$ 范围内的逐圆去均值相关于固定 $T\ne1$ 时的sharp $n^{-1/2}$、$T=1$ 时的sharp $n^{-2}$，以及 $T=3/16$ 的额外 $n^{-1}$ 项与原单步奇偶。它们仅共享准确几何接口；P30没有证明P31衰减，后者不是未投影混合或Riemann谱。依据：[P30范围](papers/30-qpi-vertical-critical-ideals/README.md)、[P31结论](papers/31-qpi-sharp-phase-mixing/paper/v3/sections/08-conclusion.tex)、[跨文接口审计](docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md)。

因此，成果数量增长主要体现排除了若干错误机制、建立了结构工具和独立数学结果；后期研究重心确实转向系统内部问题，不能按篇数折算为RH主线的同等前进。目前没有证据充分的“A1成功概率领跑者”。

### 面向 A0→A1：qPI 是优先诊断对象，不是已接近通关的候选

若下一步只优先检查一个已有系统，建议选 **qPI的算术轨道／原始点阶接口**，而不是P31的相混合结果。这是低置信度的研究投入顺序，不是成功概率排序、新意评分或新候选准入。

理由是它已有可明确计算的算术—回返关系：适用光滑椭圆纤维上的回返为指定点平移，有限域回返周期由点阶决定；[完整回返与周期记录](docs/research-batch07/PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md)保留原时间、状态和重数。已有[Kummer接口](docs/research-batch07/PAPER31_QPI_KUMMER_MATHEMATICS_DISPOSITION_V1_20260909.md)在明确参数、素数及截断条件下由算术作用恢复点阶的部分信息。这比只有丰富周期或复杂次数谱更直接接触算术，但仍缺少：

1. **内生素数选择。** 先指定有限域特征p、再研究其中众多能级和轨道，不等于同一个固定对象自然给出p↔γ_p。P30先选p、m、a后研究圆分层，也不等于映射自行产生全部素数。
2. **自然时钟和重复权重。** 整数点阶不自动给出 $\log p$ 或等价算术权重；扩域到 $\mathbb F_{p^r}$ 不自动等于原轨道重复r次。算术Frobenius与原qPI回返是不同作用，尚无把二者Euler因子／轨道乘积识别的证明。
3. **轨道重数与稳定性权重。** 由自治实qPI光滑完整椭圆纤维上的平移结构可直接推出：平移点非挠时该纤维无周期点，阶为N时整条纤维都是N周期点。普通孤立周期轨道权重不能直接照搬，连续多重性需要内生处理。这不是整个qPI路线的反证。依据：[接受稿纤维平移接口](papers/31-qpi-sharp-phase-mixing/paper/v3/sections/02-real-surface-main-theorem.tex)；原研究的自治情形另见[Joshi–Roffelsen，Remark 1.3](https://arxiv.org/html/2508.18578v2)。

相较之下，Hénon的优势是轨道工具成熟，但正面算术来源仍缺失；cat、baker和PCF的已审计具体时钟有明确障碍；高维多项式剪切与twist目前未给出更直接的素数选择机制。以上不把某个冻结方案的失败扩大成整个系统族不可能成功。

**建议的最小下一步**是一次范围明确的A0→A1桥接诊断：先固定同一个原始动力对象、允许参数及算术来源，再写清候选素数对应、自然时钟／权重、原始与重复轨道规则及重数；按A0/A1要求检查非素数／邻参等适用对照，禁止外贴标签、逐素数另调参数、目标零点拟合或拼接不同系统的最好结果。
若输出仍只是各有限域中的点阶统计，则应如实记为算术动力系统成果，不能报告成A1突破。继续补充qPI参数过渡渐近或高维次数结果可以有独立价值，但不能替代这一桥接关口。旧有限秩时钟不因换参数或增加有限记忆而重开；[P6逃逸条件](papers/6-arithmetic-clock-escape-trichotomy/notes/PROOF_PACKAGE.md)是必要而非充分条件。后续建议尚未实施，本次只归档讨论并按用户要求同步Git。

## 当前批次交付

Batch07 已完成 **5/5本地交付及统一跨论文审计**，按约定汇报并暂停。见[最终总处置与完整交付索引](docs/research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md)：独立科学／交付两席通过，无未关闭必修项；十对非碰撞和五组同源双根身份已核。P27三条书目作者字段笔误已附[本地勘误](papers/27-positive-newton-translation-reciprocity/notes/BIBLIOGRAPHIC_ERRATA_V1_20260913.md)，原冻结PDF未改，不称无任何瑕疵。

| 论文 | 最终PDF | 正文＋参考文献 |
|---|---|---:|
| P27 正Newton平移与反射互易 | [PDF](papers/27-positive-newton-translation-reciprocity/build/final-20260905-r0/main.pdf)（连同上述勘误） | 27＋2 |
| P28 本原选择周期与monodromy | [PDF](papers/28-primitive-selector-cycle-monodromy/build-capsule-successor-20260905/r0/work/main.pdf) | 23＋2 |
| P29 Hénon滤过上同调 | [PDF](papers/29-filtered-henon-cohomology/build/natural-20260906-r0/work/main.pdf) | 26＋1 |
| P30 qPI竖直临界理想 | [PDF](papers/30-qpi-vertical-critical-ideals/build/natural-20260909-r4/work/main.pdf) | 39＋2 |
| P31 qPI sharp相混合 | [PDF](papers/31-qpi-sharp-phase-mixing/build/natural-20260913-r2/work/main.pdf) | 30＋1 |

P27保留其24–28页合同与用户已确认恢复；P30独有22–40页例外，其余三篇为22–30。历史FAIL和来源限界不改写，无投稿、上传或其它外部效力；不自动启动下一篇。

上述“本地效力”指论文验收与科研处置本身，不提供外部操作权限；用户其后已明确授权的Git归档同步不等于投稿、同行评审或Route通关，也不改写冻结稿与历史接受记录。

## 历史阶段记录

以下为按时间倒序保留的阶段记录；其中4/5、尚未建稿／验收等是当时状态，不覆盖上述当前入口与总体定位。

Paper31 最新[完整Q2正式双席处置](docs/research-batch07/PAPER31_QPI_Q2_FORMAL_CANDIDATE_DISPOSITION_V1_20260913.md)为**正式准入PASS，进入本地制作**。两个fresh非作者各自完整四门均通过：新意7.7／7.7、价值8.1／8.1、证明9.2／9.3、容量均PASS，必修项为空；主控FULL读回259／302行冻结终票，不互读、不校准、不拼票。两席各自亲读[共同清单](docs/research-batch07/PAPER31_QPI_Q2_FORMAL_REVIEW_INPUT_MANIFEST_V1_20260913.md)25件FULL＋13件PARTIAL及五项固定一手范围，38身份均MATCH。原完整观测类的全Fourier、跨节点、原F奇偶、T≠1的n^(−1/2)与T=1的n^(−2)最优率及3/16的n^(−1)次层保持；旧模型／twist／阈值与成熟机制全部扣除。容量预测中值28.75／27.25页，必要旧证明同计，上溢风险仍须实际稿件验证。接着source/publication locks、完整正文及确定性／独立PDF验收；P31仍22–30页，尚非成品，整批4/5。旧FAIL、CD定位建议、扫描禁界及本地效力保持。

前轮[Q8数学与独立中心处置](docs/research-batch07/PAPER31_QPI_Q8_MATHEMATICS_AND_CENTER_DISPOSITION_V1_20260912.md)为**短接口数学接受，强有效同时扭中心预核停止**。124／113行作者稿经155行fresh数学独查、主控FULL接受，无必要修正；证明不同正参数因子泛非同源／指定点泛非扭及乘积叶的局部代数块结构，同时扭有限性明确扣除BC先例。另一fresh非作者166行预核最强统一多项式界，条件性新意6.4、价值7.0、容量未确认，主控采纳停止当前独立中心；不是强Q8反证或正式双票。BIN附录新核到变参数增长尺度缺口，完整有效阶数界仍未证，不把定性实块排除当成已有效化。其下一项Q2现已由上方处置接续。无P31项目／锁／稿件／PDF／试排，原22–30页及N扫描禁界保持，整批4/5。

前轮[八问筛查与两项纸测处置](docs/research-batch07/PAPER31_QPI_POST_RAMIFICATION_IDEA_SCREEN_V1_20260912.md)为**两项短数学接受，尚无新长文候选**。逐精确行列式的统一尾界闭合旧单ℓ Kummer截断，给全部阶档误差O_ℓ(q^(21/22))；T=ε³近三周期弱版及acnode标量缺陷有短证，而“terminal极限保持分离且三步一致趋恒等”被条件性反例排除。109／131行作者稿与158行fresh非作者核查均主控FULL接受，无必要修正；不是正式准入或拼接补分。该轮指定的不同正代数T有效同时扭接口已由上方Q8处置完成预核。无P31项目／锁／稿件／PDF／试排，原22–30页及扫描禁界保持，整批仍4/5。

前轮[指定b正式双席处置](docs/research-batch07/PAPER31_QPI_REAL_B_RAMIFICATION_FORMAL_CANDIDATE_DISPOSITION_V1_20260912.md)为**完整正式双FAIL，未准入**：两席新意7.4／7.4未达7.5；价值7.8／7.8、证明9.1／9.2、自然完整正文容量均PASS，不抵消完整合取失败。两份实际冻结报告已主控FULL读回；扣除旧简单性、实值分离短链及标准模机制后，新M的准确范围与本原开窗仍被判不足高新意，未发现当前主定理硬数学缺口。旧7.6预核、twist7.2双FAIL及全部科学接受保留；不重抽、不改页数、不靠短推论补票。下一项回到原正参数族寻找真实改变输入的新问题，先做标准包含筛查。无P31项目／锁／稿件／PDF／试排，22–30页及N扫描禁界不变，整批仍4/5。

前轮[实Betti与奇惯性处置](docs/research-batch07/PAPER31_QPI_REAL_BETTI_AND_ODD_INERTIA_DISPOSITION_V1_20260912.md)为**新数学接受，未获论文准入**：202行证明及64行消费者由一位fresh非作者212行独查、主控FULL合取通过。新增三个极大旋转值的严格参数排序、全N指定b>0的全部实分歧点准确计数、各e=2且同阶实临界值互异；由共轭配对证明全部偶数N≥10在b>1有奇惯性，补出一个真实有限分支来源，但不证明单独二换位、不可分解或满群。[12问／来源初筛](docs/research-batch07/PAPER31_QPI_POST_REAL_NEW_PROBLEM_SCREEN_V1_20260912.md)明确标准短解压力，其指定的强包含与单中心下一项已由上方新处置完成。该轮没有正式评分；原全实正式双FAIL及所有旧FAIL／HOLD／STOP保持，P31仍22–30页，整批仍4/5。

Batch07：Papers27–30 已本地验收，共完成 **4/5**。最新 Paper30 为39页正文＋2页参考文献的确定性双根产物，完整实际稿件/PDF审查与独立终局完整性均通过（[PDF](papers/30-qpi-vertical-critical-ideals/build/natural-20260909-r4/work/main.pdf)、[验收记录](papers/30-qpi-vertical-critical-ideals/notes/LOCAL_ACCEPTANCE_20260909.md)）。Paper31及整批统一审查待串行完成。

Paper31 全实twist完整候选的[正式双席处置](docs/research-batch07/PAPER31_QPI_REAL_GLOBAL_TWIST_FORMAL_CANDIDATE_DISPOSITION_V1_20260912.md)为 **两份完整合取FAIL，仅新意未过**：两个fresh非作者各自审完全部四门，新意均7.2未达7.5，价值均7.8、证明信心9.2／9.3及可信22–30页容量均PASS；主控FULL核准298／399行终稿，不平均、拼票或重抽。已完成有限来源补单、[完整brief](docs/research-batch07/PAPER31_QPI_REAL_GLOBAL_TWIST_CANDIDATE_BRIEF_V1_20260912.md)、必要证明图和23件FULL／10件PARTIAL共同包；[全T三实区间数学接受](docs/research-batch07/PAPER31_QPI_REAL_GLOBAL_TWIST_MATHEMATICS_DISPOSITION_V1_20260912.md)与准确Q/Z桥接保持。经典同族、旧forcing及5/8先行问题扣除；BR后段、BC和Duistermaat强正文仍缺读，不能将失败归结为“取得PDF就必通过”，也未认定整表已知。下一项返回原族新实质问题筛选，不为当前包补分或凑页；旧CD6.5、厚度双FAIL、[指定b机制4.0原票](docs/research-batch07/PAPER31_QPI_B_ALL_N_MECHANISMS_PREFLIGHT_DISPOSITION_V1_20260912.md)、HOLD／STOP及扫描禁界不变。未建P31项目／锁／稿件／PDF、不试排，原22–30页及完整准入合同不变，整批仍4/5。

Paper31 准确厚度完整候选的[正式双席处置](docs/research-batch07/PAPER31_QPI_EXACT_THICKNESS_FORMAL_CANDIDATE_DISPOSITION_V1_20260912.md)为 **两份完整合取FAIL**：两位全新Codex xhigh非作者各审完全部四门，主控FULL核准404／443行报告及终态SHA。新意7.1／7.0、独立价值均7.3未达7.5；证明信心均9.1、容量均PASS，未发现新硬数学缺口。自然正文低／中／高24.50／30.00／36.50与27.00／34.25／41.50页均为预测，不是PDF验收。[完整候选包](docs/research-batch07/PAPER31_QPI_EXACT_THICKNESS_REVIEW_INPUT_MANIFEST_V1_20260912.md)、此前[6.8／谨慎查新](docs/research-batch07/PAPER31_QPI_EXACT_THICKNESS_PREFLIGHT_DISPOSITION_V1_20260912.md)、来源缺口及[数学接受](docs/research-batch07/PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md)保留；两席不互读、不校准、不平均或重抽，不称跨模型。准确初始化及节点二阶例外获认可，但扣除既有理论后独立贡献仍不足。下一项返回原族实质研究，不改名复投同包；未建项目／锁／稿件／PDF、不试排测页，P31原22–30页不变，整批4/5。

前轮Paper31完成[素域充要判据与完整固定概形接口的数学接受](docs/research-batch07/PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md)：全部 $p>3,T\in\mathbf F_p^\times$ 的有限素域好能级上，$N_p(h_*)=0$ 准确等价于存在 prime-to-$p$ 切触；原自治完整模型的半稳定固定理想及节点 $\tau^{i_n}(\xi,\eta)$ 也获证明。两项fresh独查374／297行及主控FULL合取通过，必要修正为空；F5全20参数、三个二阶切触亦完整精确独核。另101行独立增量批评承认上述新结果，但扣除既有下降／群作用后当时仍不支持独立长文中心；其未求初始交数的输入已由上方本轮结果实质改变，原报告不回写。P31原完整准入与22–30页不变。

前轮Paper31完成[新来源筛选与原 Manin 接口的有界接受](docs/research-batch07/PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md)：原指定回返点在全部 $p>3,T\ne0$ 下的显式 Manin 值非零、非 $p$ 可除性及次数至多 $2p$ 的必要切触多项式已由446行作者证明、271行fresh独查和主控FULL合取接受，特殊时间已覆盖。对全部 $p\nmid n$，加入坏纤维／无穷远后候选至多 $2p+5$，但不是准确分类或全部交点清单。JR来源专项和本地问题碰撞图已收束；两篇2026新文只作跨族线索，旧特征零全阶切触／原周期概形仍未解决。当前短接口不单独作长文中心，未建新候选、项目、锁、稿件或PDF，未试写测页；P31仍22–30页，批次仍4/5。

前轮[两诊断、独查与结果后处置](docs/research-batch07/PAPER31_QPI_POST_CLOSED_IDEA_REPORT_V2_20260912.md)保持：固定完整原曲线 $X_{-3+\pi^2}(\mathbb Q_3(\zeta_3))$ 无点及原自治特征零相对导出代数信息失明获数学接受，N01在积表前准备停止；该轮无存活长文题，不补第三题，不等于家族耗尽。原q=1非单位时间的[全次数算术数学接受](docs/research-batch07/PAPER31_QPI_NONUNIT_ALL_DEGREE_MATHEMATICS_DISPOSITION_V1_20260910.md)与同一完整C1–C3的[正式双票FAIL](docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_FORMAL_CANDIDATE_DISPOSITION_V1_20260910.md)均保持，不换名复投或重抽评分。此前局部接口、Kummer满像及其开放边界见[基线盘点](docs/research-batch07/PAPER31_QPI_POST_CLOSED_BASELINE_GAPS_V1_20260910.md)。

[Paper30](papers/30-qpi-vertical-critical-ideals/README.md) 已完成：原qPI首层完整两方向临界理想与全素数高层首jet，保留原八中心、四末端、实际Jacobian及完整光滑闭纤维Hasse证明。高层只到模平方，长度五只属带原基参数作用的截断横向商，状态准确阶与下界明确区分。原[正式双票准入](docs/research-batch07/PAPER30_QPI_VERTICAL_ALPHA_FORMAL_CANDIDATE_DISPOSITION_V1_20260909.md)、旧失败和来源限制不变。首次r2因39页正文超过30页而失败，随后用户明确批准**仅本篇**正文22–40页；[原失败](papers/30-qpi-vertical-critical-ideals/notes/FIRST_COMPLETE_NATURAL_BUILD_RESULT_V1_20260909.md)与[页数增补](papers/30-qpi-vertical-critical-ideals/notes/PUBLICATION_PAGE_ADDENDUM_V2_20260909.md)分开保留。V4只修两处实际溢出，双新根PDF字节相同；主控及fresh非作者各读完全部41页，184行[完整稿件/PDF审查](papers/30-qpi-vertical-critical-ideals/notes/V4_COMPLETE_MANUSCRIPT_PDF_REVIEW_V1_20260909.md)及其后142行[独立终局完整性](papers/30-qpi-vertical-critical-ideals/notes/FINAL_INTEGRITY_REVIEW_V1_20260909.md)均通过。并行[qPI接口盘点](docs/research-batch07/PAPER30_EXISTING_QPI_INTERFACE_INVENTORY_V1_20260909.md)与[P29/P30接口限界](docs/research-batch07/PAPER29_30_EXISTING_INTERFACE_LIMITS_V1_20260909.md)供后续接续，不新造定理或提前准入Paper31。

前一[非单位时间有界数学接受与预筛](docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_MATHEMATICS_AND_SCREEN_DISPOSITION_V1_20260909.md)保留：原八中心在 $\mathbb Z[q^{\pm1},\tau]$ 上的一阶上同调、零时间全次数几何、全次数实际 jet 复形及 $q=1$ 三阶混合块通过全文非作者检查。三阶首个非零 Fitting 为 $\tau^5(\tau,2)$；全素数规律仍未证明。Harbourne、相对近点簇和 Pascal 平移先例扣除后，具体实现不足以直接支持独立长文，故关闭有界预筛、不立正式候选；这不是数学失败或全素数反证。

Paper30 的[整系数新问题预审](docs/research-batch07/PAPER30_QPI_INTEGRAL_PREFLIGHT_DISPOSITION_V1_20260909.md)及[完整V1正式双审](docs/research-batch07/PAPER30_QPI_INTEGRAL_FORMAL_CANDIDATE_DISPOSITION_V1_20260909.md)均已完成。同一 qPI 八截面族的通用反典范上同调、原圆分 pencil 完整平坦降阶、全部扭子初等因子及全开放模型整除微分的数学接受保持；完整 C1–C3、实际Jacobian／原光滑闭能级Hasse及必要旧证明均进入两位各读55件全文的正式票。两票新意均 **7.3（FAIL）**、价值均8.1、证明信心9.1／9.2、容量均PASS，故**双份合取FAIL，仅新意未过**。自然正文低／中／高分别24.25／29.75／36.00与22.9／28.5／34.6页，均非实测；未发现新硬数学缺口。R2的旧接受计功措辞已作有界范围澄清，不改原票或重评分。查新7.0、q-Hodge／Hasse等先例扣除和旧完整V2失败全部保留；不重投相同C1–C3，继续实质族内问题筛选。未建项目、锁、稿件或PDF，批次仍为3/5。

Paper30 保留的旧完整候选为 root-of-unity qPI 的实际几何与有限域动力学。对所有有限阶 $s$、每个非零固定 $t$ 及全部允许特征（含2、3），原最小亏格一 pencil、全部有限纤维、准确谱 Jacobian、实际坏值及非约化临界重数、全状态 Hasse 界与原分箱均已证明并独立接受，见[统一数学处置](docs/research-batch07/PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md)。准确范围关闭 JR 作者 v2 Conjecture 1.2.A/B 与 Conjecture 3.6，不包括其他猜想。九对数学输入保持冻结；新增共享 Weierstrass 复用 V2 已通过针对性独审，旧 V1 条件及旧替代证明完整保留。

该完整 qPI 候选 V1 的正式双票现为 **FAIL（两票均仅新意未过）**，见[正式处置与完整报告](docs/research-batch07/PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md)。两票新意／价值／证明信心均为7.2／8.0／9.2，容量均PASS；自然正文低／中／高分别23.50／28.75／34.50页和22.7／27.0／31.6页，均为预测而非实测。31件完整共同输入、W V2必要链、旧查新6.0／PROCEED_WITH_CAUTION及其全部反对意见均实际进入两票；全球首创仍UNCERTAIN。两人未发现新硬数学缺口，但新意未达锁定7.5，不平均或重投相同内容；[原就绪快照](docs/research-batch07/PAPER30_QPI_FORMAL_READY_HANDOFF_V1_20260908.md)和失败原件保留。

正式输入之外的[准确泛回返点](docs/research-batch07/PAPER30_QPI_EXPLICIT_RETURN_POINT_DISPOSITION_V1_20260908.md)现已推进为[全闭纤维自治约化与精确周期接受](docs/research-batch07/PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md)：对全部有限域和合法状态，原 $r$ 步回返与同族自治系统 $\mathcal A_{t^r}$ 共轭，包含奇异层、末端线与特征2、3；其中 $r=\operatorname{ord}(s),T=t^r,\varepsilon=(-1)^{r+1}$。指定点为 $(0,\varepsilon T)$，奇异群元素、完整循环数及时间／状态权重均已证明，三项新增数学及合并独审通过。这些结果没有事后补入V1两票。新独立查新为6.5／PROCEED_WITH_CAUTION，仍不预授正式新意；组合增量核查明确，模型识别后的整套群论循环计数已由P11一般定理包含，须作同一几何链的推论，不另拆篇。新增[指定点／局部模型复用](docs/research-batch07/PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md)已获12项针对性独审接受，原T1–T4及新增T5–T7完整候选已冻结。[V2正式双票处置](docs/research-batch07/PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md)现为双份合取FAIL：两位各读同一47件全文输入、各审完整四门，新意分别7.6／7.4，R1完整PASS而R2仅新意未过；价值8.5／8.4、证明信心均9.2、自然容量均PASS。两位均未发现需修复的硬数学缺口，容量仍是预测。两正式任务已结束，原票及输入保留，不平均或重投相同内容。未立项、建锁、写稿测页或生成PDF，批次仍为3/5。

前一阶段[定向来源核查处置](docs/research-batch07/PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md)保留：JR 出版版公开授权网页全文已补读，相关断言仍为猜想（出版 Conjecture 3.7 对应作者 v2 的3.6）；Joshi–Lobb 已读正文 §§1–4，渐近自治极限不混同于当前有限阶回返。Ohyama、GRT11 真实全文仍有访问缺口；Ramani 讲义新增二阶 qPI 的具体对应，不充当 GRT11 全文。来源任务已结束、原 V2 FAIL 不变；后续已按上方当前入口推进实质整系数新问题，未重投同一候选。详尽阅读层级和未排除内容见处置所链三份记录。

以下内部算术结果与失败是保留分支，不是当前待重投候选。
Paper30 的内部算术定理已闭合：全部 $p\ge5,a\ge2$ 下，令 $m=(p-1)/2$、$M=p^{a-1}m$，第三内部 forcing 的正规化 $S$ 有完整两边 Newton 图 $(0,m-1)\to(m,0)\to(3m+1,M-m)$，恰有次数 $m,p$ 的两个不可约可分因子，首三个内部项两两互素。准确最高剩余为 $-3/16$；正簇循环分裂域与负簇单根野全分歧已确定，见[科学接受处置](docs/research-batch07/PAPER30_TWIST_THIRD_FORCING_NEGATIVE_COMPLETE_STRUCTURE_DISPOSITION_20260908.md)。完整野分裂域、负根间距、第二项完整图及最终 $C,Q$／全实根等仍开放；[查新](docs/research-batch07/PAPER30_TWIST_INTERNAL_ARITHMETIC_NOVELTY_PREFLIGHT_20260908.md)仅为已读范围内未见直接先例，全球新意仍UNCERTAIN。

Paper30 完整 V2 的正式候选合取为 **FAIL（容量两票未过，独立价值一票未过）**，见[完整双票与主控处置 V2](docs/research-batch07/PAPER30_TWIST_INTERNAL_ARITHMETIC_FORMAL_CANDIDATE_DISPOSITION_V2_20260908.md)。R1 的新意／价值／证明信心为7.7／7.6／9.1，自然正文低／中／高30.5／38／46.5页；R2为7.7／7.2／9.2、24.7／32.4／41.0页。两人未发现新的未闭合数学消费者，但预测容量均不能获得可信的22–30页判断，R2另认为内部jet截面的独立意义及已证可迁移性不足。页数不是实测或严格下界；不平均、不拼接、不给最终C,Q添加新验收义务。

已接受的[正簇有限替代](docs/research-batch07/PAPER30_TWIST_POSITIVE_FINITE_REPLACEMENT_DISPOSITION_V1_20260908.md)、[阶乘块／第三端点替代](docs/research-batch07/PAPER30_TWIST_BLOCK_ENDPOINT_REPLACEMENT_DISPOSITION_V1_20260908.md)和[负端有限伴随／矩复用](docs/research-batch07/PAPER30_TWIST_NEGATIVE_FINITE_ADJOINT_REPLACEMENT_DISPOSITION_V1_20260908.md)保持；V2两票已按完整当前链去重。[原V1容量失败](docs/research-batch07/PAPER30_TWIST_INTERNAL_ARITHMETIC_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md)、[作者范围预筛](docs/research-batch07/PAPER30_TWIST_POSTADJOINT_SCOPE_DISPOSITION_V1_20260908.md)、冻结输入和失败记录不改写。原R2的盲性事故没有形成票，全新实例独立接替的事实见[事故与接替记录](docs/research-batch07/PAPER30_TWIST_INTERNAL_ARITHMETIC_FORMAL_R2_SUCCESSION_V1_20260908.md)。主控已全文读取353行／381行有效报告，完成针对性范围核对和容量表复算；两项评审均结束。Paper30仍未立项，不试写测页、建锁或改验收。不能仅缩写或重分组现包后再投；当前真实新输入与下一步见上方 qPI 接续，无新稿件、PDF或外部效力。
以下是历史成果索引；旧终态不替代当前恢复进度。

30-qpi-vertical-critical-ideals - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 原首层完整垂直临界理想及奇素／特征二高层首jet，完整证明留在39页正文，另2页参考文献；仅本篇获准22–40页，双根PDF字节同一，全文实际PDF和独立终局完整性均通过，仅本地。

29-filtered-henon-cohomology - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对特征零辛Hénon映射证明普通次数滤过的精确余上同调计数、保次数原函数及单个完整周期概形的有效检测，并分类指定保参数辛扩张的完整有理固定域；26页正文＋1页参考文献的匿名PDF经同源双新根复现、完整独立PDF审查与最终完整性审查通过。原容量预评FAIL保留，后续获准的自然实测路径已完成；效力仅限本地。

1-symp-vs-diss - Route A / A0-A1 - 冻结 Hénon 保守-耗散同伦与禁止零点拟合规则，开始验证 Logistic 算术投影在光滑辛提升中的临界障碍及低周期轨道延续
1-symp-vs-diss - Route A / A0_FAIL - 封存测试显示辛端点暴露率仅1.17%、无存活轨道且邻参复现耗散结构；停止素数乘子、Zeta与量子化路线，形成可复现负结果
1-symp-vs-diss - Paper complete / ROUTE_A_REJECTED - 完成13页非匿名论文、三幅终版图、30项测试与80位轨道审计，固化“冻结载体不可用而非普遍算术反证”的结论
2-branch-baker - Design frozen / PRE_A0 - 选定后临界有限分支的紧致分片辛 Markov--baker 新候选；将已知母映射 zeta 降为复现基线，冻结有限局部常数乘子时钟的 prime-length no-go 检验
2-branch-baker - Route A / A0_FAIL_STRUCTURAL - 精确载体、226条低周期原始轨道、唯一边界商与三组各16777216次检查全部通过；证明固定有限记忆局部常数乘子时钟无法容纳全部素数对数，停止A2--A4与Route B
3-prime-multiplier-obstruction - Exact theorem / RAW-PRIME CLOCK REJECTED - 冻结PCF二次映射的全周期整除性排除全部有理素数原始乘子；保留周期至少二时指数时钟能否产生基素数2这一明确边界
4-integral-henon-multipliers - Route A / A0_FAIL - 证明积分辛Hénon周期乘子为代数单位、精确有理模长只能为1，并将S-整数推广的有理素因子限制在固定有限坏素数集
5-algebraic-action-clocks - Exact theorem / SCOPED CERTIFICATE - 由周期作用量的代数性与Hermite--Lindemann定理排除代数归一化作用量等于log p；不外推到log|A|、多值规范或超越归一化
6-arithmetic-clock-escape-trichotomy - Exact theorem / CAPACITY_BOUND_CERTIFIED - 对有限秩项、固定坏素数支撑与代数作用量的加法读出证明素数命中数不超过dim_Q(V)+|S_Q|，明确下一候选必须逃离至少一个有限性机制
7-base2-exponent-clock - Exact theorem / SCOPED 2-ADIC BOUNDARY - 证明冻结PCF二次映射的高周期点为2-adic单位、其有理乘子为2^n乘奇整数；排除n=2,3的±2^n并审计development-seen n=2--7，但n>=4的全周期等式问题保持OPEN
8-cat-torsion-capacity - Exact theorem / A0_FAIL_PROVES_TOO_MUCH - 用原始除子证明双曲环面自同构在所有n>12都有素数阶精确周期载体，并给出标准cat映射的N\{1,6,12}精确分类；阶数时钟却覆盖全部整数且非局部、非连续
9-cat-prime-shell-multiplicity - Exact obstruction / A0_FAIL_GLOBAL_NORMALIZATION_ONLY - 标准cat映射的p-torsion壳仅p=2有单一原始轨道，所有奇素数均有m_p>=p-1；纯标量Euler因子无法消除次数，分数权修复只是对素数与合数都成立的壳层全局归一化
10-cat-centralizer-quotient - Exact boundary / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC - 循环向量集是完整局部GL中心化子的torsor，但商后A的动力学为恒等；辛中心化子仍留下范数像分层，单类压缩依赖随模数变化的非辛伪对称与外贴q标签
11-cat-equivariant-clock - Exact boundary / EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF - Burnside、equivariant与stacky增强在源周期、子群、生成元和稳定子之间形成严格保留-压缩层级；带标签有效C x Z数据可恢复A模作用核，但不存在统一的内生模数时钟，q=2仅是明确披露的逐行例外
12-henon-period3-residue - Proof-only theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 在完整归一四次0^4纤维上证明周期三迹留数是最小共轭分离量；唯一注册R100在科学裁决前终止且禁止重跑，终版仅依赖冻结证明并通过独立终态完整性审计
13-henon-primitive-cycle-cover - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 证明退化 Hénon 族的归一原始周期覆盖、循环轨道商与轨道和/导数迹本原坐标；唯一R100仅为有界实现一致性证据，27页匿名PDF经双重确定性重构与独立终审通过，效力限于本地匿名发布
14-henon-four-step-torus-escape - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对单项式 Hénon 映射证明有限秩乘法环面四步存活集的一致显式界，并以秩一无限三步族证明窗口尖锐；17页匿名PDF经R0/R1与终态双重确定性重构、独立R2和终审通过，效力限于本地匿名发布
15-henon-quartic-trace-fibers - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对单因子正规四次 Hénon 空间证明纯固定迹的 Jacobian 候选界、周期一二的唯一正维坏纤维与尖锐周期三拟有限截断；24页主文/35页匿名PDF经R0/R1及终态双重确定性重构、独立R1/R2和终审通过，效力限于本地匿名发布
16-henon-support-size-torus-escape - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对实际非恒定支撑至少为二的广义 Hénon 映射证明有限秩乘法环面两步存活集的系数一致显式界，并以任意给定支撑上的秩一无限一步族证明窗口尖锐；完整吸收 Paper14 的支撑一四步有限/三步无限定理，27页匿名PDF经R0/R1和终态双重确定性重构、独立R1/R2与终审通过，效力限于本地匿名发布
17-shiftlike-torus-coset-decay - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对稀疏 type-ν shift-like 递推证明非零常数锚下 m 步存活簇中的连通环面平移维数至多 k−m，并构造逐窗取等族；同时完整分类零常数二维边界，22页匿名PDF经R0/R1及终态双净根确定性重构、独立R1/R2与终审通过，效力限于本地匿名发布
18-marked-henon-scalar-boundary - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对广义 Hénon 族唯一包含多项式边界的标记分支，证明由 −b 与选定标记周期迹组成的坐标映射占优且泛 étale，并给出临界方案在多项式边界上的精确基变换与Fitting理想控制；23页匿名PDF经R0/R1及终态双净根确定性重构、独立R1/R2与终审通过，效力限于本地匿名发布
19-shiftlike-translate-gcd-obstruction - Internal/reference theorem package / COMPLETE_BOUNDED_INTERNAL_SCOPE - 保留最大维环面平移、系数逐点模空间与支撑一GCD障碍的可重哈希内部源码和证明对象；15项外部来源声明仍被阻断，且明确不存在PDF构建、全局出版候选、终态构建、发布或任何外部效力
20-coupled-shear-degree-matrix - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对A4中的不对称耦合Hamiltonian梯度剪切证明精确两相次数矩阵与动力次数 λ₁=(√g+1)²；23页匿名候选是由main_round1.pdf逐字节复制的main_release_candidate.pdf，14页main.pdf仅为历史R0工件，终态双根重构与独立终审通过，效力限于本地匿名发布
21-three-mode-hamiltonian-cubic-degree - Proof-first theorem / COMPLETE_LOCAL_FINAL_REVIEW_PASS - 对A6中的三模耦合Hamiltonian剪切证明精确三阶次数递推、第三坐标可见性与模5给出的无限三次Perron子族；27页匿名候选经修复R0、无操作R1、双根终态重构和独立终审通过，效力限于本地匿名发布

## Batch 06 (Papers 22--26) aligned terminal index

The following five rows are the controlling pre-audit index for the batch.
They summarize the exact terminal dispositions in `BATCH_06_STATUS.md` and
`BATCH_06_IDEA_REPORT.md`; they do not grant submission, upload, hosting,
network, or other external authority.

| Paper | Candidate / project | Exact theorem or package scope | Terminal disposition and effect |
|---:|---|---|---|
| 22 | `hamiltonian_cubic_spectral_collapse_v1` / `papers/22-hamiltonian-cubic-spectral-collapse` | All-dimensional endpoint-spiked full-product Hamiltonian shears for (r\ge4, g\ge2r+1): an explicit selector cone, exact degree matrix, and cubic quotient/spectral collapse. | `COMPLETE_LOCAL_FINAL_REVIEW_PASS`; local anonymous release only, no external effect. |
| 23 | `hamiltonian_quartic_spectral_escape_v1` / `papers/23-hamiltonian-quartic-spectral-escape` | Four-mode Hamiltonian product shears with exact degree growth and quartic Perron subfamilies over characteristic zero. | `TERMINAL_LOCAL_EVIDENCE_RECOVERY_BLOCKED`; source/PDF bytes retained, no admissible R1 success or local release, no external effect. |
| 24 | `hamiltonian_period_two_selector_exchange_v2` / `papers/24-hamiltonian-period-two-selector-exchange` | Forced period-two Newton-selector exchange in two-mode shears, with exact two-step monodromy and degree law. | `TERMINAL_LOCAL_R1_BUILD_BLOCKED`; scientific/source/PDF bytes retained, no R1 success or release, no external effect. |
| 25 | `support_rank_sharp_unbounded_perron_v1` / `papers/25-hamiltonian-support-rank-unbounded-perron-degree` | Sharp support-rank characteristic factorization plus an explicit all-rank positive Hamiltonian family with exact Perron degree and minimal scalar recurrence order. | `COMPLETE_LOCAL_FINAL_REVIEW_PASS`; final 27-page local anonymous release only, no external effect. |
| 26 | `planar_newton_envelope_bidirectional_degree_v1` / `papers/26-hamiltonian-newton-envelope-contraction` | Planar Newton-envelope contraction for collected supports, bidirectional forward/inverse degree recurrences, selector rigidity, and explicit wall/carry anti-claims. | `TERMINAL_LOCAL_R0_AUTHORITY_BOUNDARY_BLOCKED`; profile/build contract and independent reviews pass, but permanent root no-access prevents any realized R0/PDF/terminal build or release; no external effect. |
