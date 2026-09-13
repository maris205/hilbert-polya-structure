# Paper30 完整源稿静态审查 V1

日期：2026-09-09。审查者：`/root/p30_vertical_alpha_complete_draft_review_v1`。
对象：`paper/v1/` 的完整十一件源文件；本轮为首次编译前的 fresh 非作者静态审查。

## 1. 结论与权限边界

- `MATHEMATICAL_TRANSCRIPTION_AND_CONSUMER_COVERAGE: PASS`。
- `COMPLETE_SOURCE_STATIC_REVIEW: PASS_WITH_MINOR_CORRECTIONS`。
- `NEW_CRITICAL_OR_MAJOR_MATHEMATICAL_GAPS: NONE_IDENTIFIED`。
- `REQUIRED_SOURCE_CLARIFICATIONS: R1, R2, R3`，三项均为下文定位的 MINOR。
- `SUCCESSOR_SOURCE_FREEZE_READINESS: PENDING_MINOR_DIFF_RECHECK`。
- `COMPILATION / PHYSICAL_PAGE_COUNT / PDF_RENDERING / PDF_ACCEPTANCE: NOT_ASSESSED`。
- `FORMAL_CANDIDATE_REVOTE / NOVELTY_RESCORING / CAPACITY_FORECAST: NOT_PERFORMED`。
- `route_applicability: NOT_APPLICABLE`。

本人完整逐行读了下面七件控制文件及十一件实际源文件，逐个核对题目特有证明和实际消费者。
数学结论来自对新稿实际论证的检查，不来自已接受标签、清单存在、源行数、哈希或机械结构成功。
未发现须补入新数学引理、缩小量词或改变 V1–V3 结论的硬缺口。
三项小修完成后，只需检查实际 successor 差异及其直接关联，不应重开未变的候选四门票。
本结论不预先接受尚未审查的 successor 字节，也不授予任何实际 PDF 或最终论文接受。

本轮只新增本报告，没有改稿、改锁、改历史作者证明、更新索引、编译、测页或派生代理。
未重读共同科学包全部六十九件，也未声称重新全文审计二十份冻结作者原稿。
没有因真实可疑数学步骤而需要回读冻结作者／非作者段；本轮直接检查的是它们在完整稿中的实际消费者。
主控提供的终态通知仅用来确认停止写入；作者自检和主控阅读意见不替代本人的判断。

按要求全文读了 paper-write、proof-writer 及写作／引用纪律 references。
使用可用 Codex fresh 上下文 xhigh；技能指定 GPT-5.4 xhigh MCP 未配置。
`cross_model_verification: NOT_PERFORMED`；不声称跨模型、校准评分或人类审稿。
锁定的匿名英文、article 11pt、letter、四边 1 inch、八节完整证明正文 22–30 页且 refs 另计合同，
优先于技能默认的 ICLR 九页、证明附录和 ML 实验安排。这里不对物理页数作任何预测。

## 2. 完整实读文件及身份

### 2.1 七件控制文件

以下均为本人 FULL 阅读；行数与最终核对 SHA-256 如下。
项目路径以前缀 `papers/30-qpi-vertical-critical-ideals/` 表示，批次路径以前缀 `docs/research-batch07/` 表示。

| 文件 | 行数 | SHA-256 |
|---|---:|---|
| 项目 `PAPER_PLAN.md` | 127 | `12c824ec4f2b198ad28237fa6972a3747e1be1cf7557ead5115ca4b0764c3187` |
| 项目 `notes/SOURCE_SCOPE_LOCK_V2_20260909.md` | 99 | `66afedb5efe87a29250d24aa2ba275fe79b1ec6eee727e362b0fc7b2c48df5b2` |
| 项目 `notes/PUBLICATION_LOCK_20260909.md` | 72 | `e07f4bcb20f8aa445b41a5ceccd3d680036700fb63f26b9fc1379870c94573fa` |
| 项目 `notes/OUTLINE_SCOPE_DISPOSITION_V1_20260909.md` | 33 | `ed5134e43d928d009c51963b1023d86daf871c63eafc5c6d4ab8077c312d93a3` |
| 项目 `notes/CITATION_RECORDS_20260909.md` | 146 | `8c531f799e71f82f01039332b1d80eaa78ea15b20d6716ddb21924faf98cbf6e` |
| 批次 `PAPER30_QPI_VERTICAL_ALPHA_CANDIDATE_BRIEF_V1_20260909.md` | 251 | `168be8025f1c8215634306ebd02b5c16319781a57026f846240d3578a10a2bed` |
| 批次 `PAPER30_QPI_VERTICAL_ALPHA_CURRENT_PROOF_MAP_V1_20260909.md` | 261 | `790f29ea9f315bb8a532fe2c51b7c8a9284acd61295aed5b6c9ae4d5ebfc26ea` |

控制文件合计 989 行，仅作为阅读身份统计，不能解释为证明长度或容量证据。
旧 brief 中“尚未准入”等文字按当前 disposition 接续，没有据旧快照重开准入。
PLAN/PUB 的旧 source-V1 链接按 OUTLINE_SCOPE_DISPOSITION 接入有效 source-V2；本轮未回写旧锁。

### 2.2 完整稿十一件源文件

下面路径均相对于 `papers/30-qpi-vertical-critical-ideals/paper/v1/`。
每件均从第一行至末行本人 FULL 阅读；分段输出的接缝有重叠，没有用检索或摘要代替缺段。
§7–8 是收到终态停止写入及 SHA 通知后才开始完整阅读；核对值与通知一致。

| 文件 | 行数 | SHA-256 |
|---|---:|---|
| `main.tex` | 62 | `0631f6292b0dac00147be516ce28ae93ca5d466e285f90f0de81d33eaf8dc68e` |
| `macros.tex` | 9 | `b4831759010e67ff47811ba1346c0a8aea47d0e2fc1bfa6e3f8312828b6b5dc3` |
| `references.bib` | 183 | `418530c0bc71f2fbbf5aa0e65b8d2c984c5c68f7fca9dcbb65c2fa84550ab0ba` |
| `sections/01-introduction.tex` | 300 | `215fdcf263c75431a779280064ac01aff7b54721983a8c571581f1a976859537` |
| `sections/02-surface-pencil.tex` | 446 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| `sections/03-spectral-jacobian.tex` | 435 | `011c5415ac5d109c56cea3263ea9cad64db79a7f6102f12676c744bacb065b9b` |
| `sections/04-closed-hasse.tex` | 271 | `b86d47b01338cce11d63a37f1263fdc4b622c9c880f299d1e4776e9908d302af` |
| `sections/05-integral-trace.tex` | 244 | `d25e401b8b14d56ce1eb8d0eb91c56bac8849dd9be933c6dcf19ac47a254f190` |
| `sections/06-first-layer.tex` | 394 | `f4232d918c4d78bacfc7c7a9dea2fbbe0aa60e634fbf27354d1708e02d84792d` |
| `sections/07-odd-jets.tex` | 468 | `8a5d216f27ca6b9c41a6c911f1d572b6728682138a3d96874c82f33b60eff690` |
| `sections/08-two-jets.tex` | 666 | `5cfee2a607e6ff1ab52192bb5c9b1a73cef6635c3e5dcfe26aa73fe1192b42a9` |

十一件合计 3478 行。这是本次审查的源身份范围，不是 source-byte build manifest，也不是页数估计。
本报告内后续 `§n:行号` 均指本表的该节源文件，不是 TeX 渲染后的节／定理物理位置。

### 2.3 流程与技能实际阅读

| 全文读取项 | 行数 | SHA-256 |
|---|---:|---|
| `docs/WORKFLOW.md` | 39 | `b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2` |
| `/root/autodl-tmp/.codex/skills/paper-write/SKILL.md` | 363 | `d8a6ca92d70b99280d9a4a256262d19aa295d267a0cfccad0d289db492132019` |
| `/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md` | 223 | `6d7b3094711f609814680ded62e19b8dd61801511a7d98b96c033894c939babe` |
| `/root/autodl-tmp/.codex/skills/shared-references/writing-principles.md` | 525 | `25c71f6b76fad1a198b47b4eae9b1d101561578cc0a8767e91706957829f0abe` |
| `/root/autodl-tmp/.codex/skills/shared-references/citation-discipline.md` | 431 | `591410ef10937e580293db238d5794548b0560bae95eb6693fec1a9cae62d9e4` |

另读当前提示中提供的 AGENTS 指令及 `BATCH_07_CONTEXT.md` 前 260 行作为批次定位。
后者是 PARTIAL，不声称全文读取或将其历史账本全部作为新审查输入。
未另行启动 research-review／ARS 的旧四门或多席流程；本任务是明确有界的实际稿件静态审查。

## 3. V1–V3 的实际证明覆盖

### 3.1 V1：原完整首层理想与真实箭头

主声明在 §1:121–150，完整证明在 §6:15–394。
原 $L_m$、$A_2$ 和乘 $\pi_1$ 的系数正合列先定义，不把首层特征四替换成高层双数。
§2:253–330 给出了真实常数映射及先在整数环固定的八节点单位消元，
§6:61–93 再以 $1-s^m\equiv-m\pi_1$ 计算指定边界 Bockstein。
所得核是实际 $k\langle1\rangle$，不是从一维性选出的未知标量比较。
§6:95–110 以原 $J-h\cdot1$ 和截面 $1$ 的实际平凡化得到 $\rho_X$，故 $\kappa_J\ne0$。

§6:152–218 的迹证明保留循环词轨道、大小一轨道的 $p=2$ 负相位、
非共振项重新落回共振时的额外 $p$ 因子，并形成真正的 $p\pi_1$ 同余。
§6:235–257 的 Taylor 先在整数环除法，保留 $\lambda\pi^{p-1}/p$，包括特征二的中间项。
§6:259–269 用模 $p\pi_1$ 的非约化限制单射把 $G_i$ 正则性延至四末端，未假定 $j_t$ 全局提升。

§6:292–340 直接验证本对象的 OC 前提，给出 $\bar G_j-\bar G_i=f_{ij}^p$ 于 Hasse 零层，
并证明 $\ker d=\mathcal O_X^p$ 和到像层的 Frobenius 是加性层同构。
因此 $\partial\nu=\operatorname{Fr}_*\kappa_J\ne0$ 的符号、类和目标均真实匹配。
它没有误称超奇异 $H^1(\mathcal O_X)$ 上的 Frobenius 可逆。
完整光滑亏格一曲线上的非零正则微分无零点，遂由 §6:362–375 的两系数基得到
原未截断理想 $(\pi_1,\widetilde H)$；不是只证明模平方。
多重根 $e_h$ 保留，完成式与允许状态的准确阶一／$p$ 有实际推导。
V1b 用于全部完整光滑有限层；V1c 明确只用于光滑超奇异层。

### 3.2 V2：奇素数全高层完整首 jet

主声明在 §1:152–178，完整证明在 §7。
§7:27–59 证明共同商和完整时间像，明确自然嵌入会把首层参数送到零，
不把指定 $\pi_1\mapsto\pi_a$ 误说成自然圆分嵌入。
§7:106–115 的全块循环插入先在特征零除 $N$，因此没有漏乘或多乘 $m$。
§7:131–214 保留实际时间、所有块内扰动及 $c_s,d_s,j_*$；共振投影仅按合法乘法规使用，
非共振消失由平方零和两项投影计算给出，不是将投影当环同态。

§7:272–299 证明带权交换子，包含 $p=3$ 的零指数边界且无判别式除法。
§7:311–330 保留块间速度 $m$ 与降序正号。
§7:343–385 给出原全 $m$ 支持界：$\gamma_m$ 在一般 $m$ 保留第五次的上界，而不声称该系数必非零，
$G$ 支持于 $[1,2p-1]$，故唯一最低数字是 $p$，其余各位是 $p-1$。
这与内部 $[0,2p-2]$ 的选择分别证明；没有拿 $m=1$ 推全 $m$。
§7:390–418 合并两完整形式，粘合 $p\mid(\sigma-1)$ 的提升幂并用非约化四图单射延拓。
§7:441–459 随后才消费 V1 两系数理想，给准确的加 $(\pi_a^2)$ 理想及多重根式。
高层超奇异状态只得至少二；正文未升格为准确二或全厚度。

### 3.3 V3：特征二、实际四块与混合商

主声明在 §1:180–217，完整证明在 §8。
§8:80–101 从 Eisenstein 与 $v_{\pi_a}(2)$ 得到高度至少二的特征二共同商，
保留完美域块代数范围，并与仅有限剩余域的后续几何结论区分。
§8:103–217 分别证明内部完整扰动、特征二交换子以及 $[1,7]$ 支持下唯一最低四次选择。
§8:219–285 用原状态常数行列式计算真实 $\beta_4=T\,dJ+J^2\chi_m$；
$\chi_m$ 在 §8:35–47 由环境原矩阵公式定义，而非沿纤维反定义。
§8:287–309 将整一形式乘 $J^{\langle N-4\rangle}$ 延到全部四末端，未假定环境 $\chi_m$ 全局正则。

§8:336–408 独立使用首层特征四，比较 $j_*dj_*+\pi_1K_0$ 与 $-j_*dj_*+\pi_1dG$，
保留 $2j_*dj_*=-\pi_1j_*dj_*$ 后才约化，准确认同原 $\nu$，没有任意标量替换。
§8:413–443 使用实际全局形式定义局部差商而非全局 $j_*$。
§8:457–483 在每个完整点的局部整环中先由素性除一次 $J$，再消去并第二次用素性除 $J$，
所以 $J^2$ 整除确实从泛点延至每点；不是以点集稠密或仅切向正则代替。
其切向系数为原无零点的 $\nu$，给局部单位。
§8:509–552 据此消去两系数，得到准确混合理想及任意局部提升独立性，普通层另作单位理想处理。

§8:578–590 消去 $\epsilon$ 给 $z^5=0$，同时保留原底参数 $\pi_2=z^3/T$。
这里五是横向截断长度，$w$ 尚存；没有宣称原完整临界商长度五或总 Artin 长度五。
§8:593–605 保留 $T$ 经允许扩张正规化及 Lubin–Tate 先例边界。
§8:626–654 由实际理想评价状态，再加 $a\varphi(p^a)$；高度二整除／未整除阶准确一／五，
高度至少三只得相应下界。额外分歧状态、奇异能级、全厚度仍明确开放。

## 4. 二十作者供应的实际 consumer 清单

本表核对的是当前 proof map 的二十个必要消费者，不声称新读或新裁决冻结作者全文。
重复通用引理的旧更长证明不自动成为正文义务；实际使用的前提没有随复用删除。

| 供应别名 | 本稿真实位置 | 核对结论 |
|---|---|---|
| P | §2:47–226 | 八图／辛形式、八边界赋值运输、四末端实际局部映射、准确极除子与无基点均有证明。 |
| Nbd | §2:270–333 | 原节点 monomial 帧、四个比率、乘积 $q^{-1}$、整数单位消元与法丛精确阶均保留。 |
| Gfield | §2:338–446 | 截面维数、Stein 非复合性含不可分次数、几何连通及边界邻域排除泛准椭圆均真实写入。 |
| Ucoh 基础 | §2:253–268、311–330 | 真正常数及任意基变换节点基础被消费；未额外导入未用的全次数分裂。 |
| Bbad 纯 W | §3:17–110 | 先独立证明 W 射影平坦、总空间正则、几何整纤维及纯有限临界代数；未循环调用原曲面强临界结论。 |
| Wreuse V2 | §3:114–186、408–415 | 原谱两图、四端点、有限推下、全特征光滑与原域接口齐备。 |
| Jspec | §3:202–435 | 实际族谱模、常数共轭恢复、状态有理逆排除不可分度、固定 Picard 差、无核与 torsor 下降完整。 |
| SH | §4:30–48、50–145 | 仅消费选定已光滑完整纤维的连通性以得几何整性；未假设全部奇异纤维分类。 |
| Hloc L(a) | §4:50–131 | 同能级 henselian 截面、双方正则且相对最小、指定泛同构及逆双向延伸均在正文；精确引用小修见 R2。 |
| Ddiff Cartier | §4:147–254 | 完整谱微分含有限分支点与无穷远的正则性、正／逆 Frobenius 规范、奇素数及二的 Cartier 算式齐备。 |
| Ddiff 整数 | §5:22–159 | 原循环插入先除后约化、秩二整数递推、数字选择与 Hasse 乘数均自证，不用 Vlasenko 黑箱。 |
| Gint G3a/b | §2:6–110；§5:163–227 | 同一八截面模型、函数／形式全局正则性、全部非约化末端图限制单射均保留。 |
| DB | §6:15–110 | 整单位节点图的实际 Bockstein、真实常数核及原限制箭头闭合，包含 $m=1$ 空归纳和 $p=2$。 |
| prime | §6:115–271 | 原块定义、循环轨道与非共振项、$p\pi$ 同余、整数导数／Taylor、非约化延拓齐备。 |
| TH | §6:27–110、259–394 | 实际障碍及全光滑纤维限制、OC 具体输入、原两方向完整理想及状态结论均闭合。 |
| OC | §6:275–340 | 不借抽象已接受标签：实际 Čech 等式、像层 Frobenius、非消失与无零点推论直接证明。 |
| Matrix 通用 | §5:88–102；§7:94–115、253–299 | 整数插入、秩二递推和通用带权交换子均有一次完整证明供后节使用。 |
| TB | §7:117–418 | 全 $m$ 块内／块间项、实际支持、唯一数字选择与全图首 jet 因子分解齐备。 |
| GFI 接口 | §7:27–59、390–418；§8:80–101、287–309 | 准确共同商、全时间 jet、提升幂粘合及非约化限制，不消费旧 $m=1$ 结论冒充全称证明。 |
| P2／PI | §8:79–309／336–655 | 两份供应各自全部必要步骤被消费：全块代数与实际局部两方向几何没有相互替代。 |

表中 Ddiff 的两种消费者分行，而最后 P2／PI 同行，共覆盖 proof map 的二十个作者别名。
实际 Jacobian 链不是“同谱即同曲线”：§3:267–311 给出函数域有理逆，
§3:353–393 先用全群固定点排除几何拉回核，再用 $r$ 可逆排除非约化核，
§3:396–434 最后下降 torsor 作用而不下降几何选点。
闭 Hasse 链也不是“泛 Jacobian 相同即可”：§4 检查相同能级的两个局部模型，
分别延拓指定泛同构和其逆后，才运输完整谱微分的零性质。
此顺序没有用后节未证的理想、非消失或强临界结果作为前节前提。

## 5. 引用、结构与语言检查

### 5.1 书目身份及实际用途

本人逐项将全部十七条 BibTeX 与完整 CITATION_RECORDS 核对；作者、年份、题名、刊物、DOI／版本没有新发现的转写冲突。
JR 的刊本身份与所用作者 v2 定位有区分；JL 不扩造中间名；GHK 与 Cantat–Dolgachev 的刊年／期刊正确；
Achter–Howe 指向订正 v5；Vlasenko2024 说明 metadata／正文题名顺序差异；两篇 Dupuy 论文作者组未混同；
Shimada 仍是预印本；KS 书目与锁定记录相符。未将旧本地作者报告加入匿名外部书目。

十七条均有真实 consumer：JR/JL 为原对象；GHK/CD 为八环／Halphen 背景；Beauville/IVY 为谱方法归属；
Stacks 为直接通用引理；Achter–Howe 为 Cartier 规范；Vlasenko2018、BV2021、Vlasenko2024 为已有机制和适用边界；
DI、两篇 Dupuy、Shimada 为算术障碍背景；KS 为指定其他根单位系统先例；LT 为特征二高度二先例。
不是仅为凑引用数而保留十七条。JR 原矩阵／Laurent 身份明确列为来源输入；后续原对象运输由本文证明。

Vlasenko2018 的勘误一手正文在既有记录中仍未实读，影响仍为 `CORRECTION_IMPACT_UNKNOWN`。
稿件 §1:263–268 明确限制到所用 author-v3，并说明其定理不作下文证明前提；§5–8 的所需代数确实自足。
稿件没有说勘误无关，也没有将原版定位冒充勘误后完整结论。本审查不关闭该来源缺口。
Beauville 本轮原正文、Ohyama／GRT11／Garcia–Tafazolian 等旧缺口也不因引文表匹配而关闭。
本文没有据这些未读原文作全球优先权或强排除声明。

### 5.2 本轮有界一手引用核对

只因稿中实际标准引用的精确定位而访问公开 Stacks 官方页；没有重跑查新或十七来源全文复审。
访问日期均为 2026-09-09，读取网页正文，不称 PDF／图像审计：

- [03H0，Theorem 37.53.4](https://stacks.math.columbia.edu/tag/03H0)：实读陈述及证明，支持 §2 的 proper Stein 分解与几何连通纤维。
- [0AVB，Lemma 15.24.18](https://stacks.math.columbia.edu/tag/0AVB)：实读陈述及证明，支持有限反身模的余维一交；稿中局部自由模满足其条件。
- [0C2V，Definition 55.8.4](https://stacks.math.columbia.edu/tag/0C2V)：实读定义，稿中以无第一类例外曲线核相对最小性。
- [0C6B，Lemma 55.10.1](https://stacks.math.columbia.edu/tag/0C6B) 与 [0C9Z，Lemma 55.10.2](https://stacks.math.columbia.edu/tag/0C9Z)：实读两条陈述及证明；同一正亏格泛曲线和双方 regular proper minimal 前提在稿中明确。
- [07LW，§15.9 Lifting](https://stacks.math.columbia.edu/tag/07LW)：实读该节可见正文，确认它是整节，包含一般光滑提升至 étale 扩张的 Lemma 15.9.14；它不是本处 henselian 回缩的准确 lemma tag。
- [04GG，Lemma 10.153.3](https://stacks.math.columbia.edu/tag/04GG)：实读完整等价条件，特别 (8)，以及 (1)⇒(8) 的标准 étale 局部化／简单根提升证明。稿中 $A$ 已 henselian，所构造 étale $A$-scheme 的指定点剩余域等于 $A$ 的剩余域，故 (8) 直接给保持该点的回缩。其余长等价证明不是此消费者所需，未用来扩张本轮数学范围。

上述核对没有遇到权限／付费门，也没有重试既有被封锁的文献入口。
R2 的建议基于这里实际读到的 04GG 条件，而非凭记忆更换标签。

### 5.3 源结构与叙述

源静态机械复核得到 135 个不同 label、97 个被引用 label、17 个 cited keys、17 个 bib keys。
没有缺失 label、重复 label、缺 bib key、未引用 bib 条目或 begin/end 环境计数失衡。
检索没有 TODO／FIXME／XXX／VERIFY／PLACEHOLDER／localdoc 占位；十一件源的每一节都被 main 输入。
这些只是辅助结构事实，不替代前面的数学阅读，也不保证 TeX 引擎已成功编译。

main 的源配置是 article 11pt letter、1 inch margin、标准未压缩行距、匿名署名与空 PDF author；
只有正文末尾的 `LastBodyPage` 和 references 前 `clearpage`，未见正文人为分页、空白填充或附录转移证明。
定理环境和公式按节计数，所用宏／环境在静态读取中未见未定义接口。
文本从缺失的首切向信息进入原对象、几何、整数迹、首层和两类高层，反向大纲连贯。
公式前大多先定义对象；source 的原输入与本文运输责任有区分；状态表没有把下界写成等式。
下述三项之外，没有发现需要强制语言修复的泛化措辞。未提出按页数删科学、缩版或移附录建议。

## 6. 必要小修：严重度、位置、原因与最小修复

### R1 — MINOR：摘要中的首层理想句缺少就地范围限定

位置：`main.tex` 第 35–37 行。
现句从“every prime and every tame block size”直接说 full first-layer coefficient ideal 的生成元，
没有在该句说是在每条完整光滑有限纤维附近。全文主定理 §1:123–126 和 §6:345–350 已正确限定，
摘要末尾也排除 singular-level ideals，所以这不是正文定理扩大或新数学缺口。
但摘要可被独立读取，该句本身容易被读为整个原曲面的完整理想等式，需恢复就地限定。

最小修复：在该句的 ideal 后补 `near every complete smooth finite fiber`，或等价语序。
可用完整句：`For every prime and every tame block size, the full first-layer coefficient ideal near every complete smooth finite fiber is generated by the cyclotomic parameter and the Hasse polynomial.`
影响仅摘要范围陈述；不改定理、证明、素数／tame／域量词或理想。

### R2 — MINOR：henselian 点提升的精确标准引用

位置：`sections/04-closed-hasse.tex` 第 80–87 行，尤其第 87 行。
07LW 是整节的一般 lifting 背景，不能作为本处已经构成 étale 点后回到同一 henselian 底环的精确条目。
这里的问题是定位过宽，而非援引了一个相反或不可用的定理；稿中实际几何构造和结果均正确。
直接匹配的官方 [04GG](https://stacks.math.columbia.edu/tag/04GG)，Lemma 10.153.3(8)，
要求 henselian local ring、étale algebra 及相同剩余域的指定点，稿中条件逐项满足。

最小修复：把 `\cite[Tag 07LW]{StacksProject2026}` 改为
`\cite[Lemma 10.153.3(8), Tag 04GG]{StacksProject2026}`。
不需改 BibTeX 总条目，不需增加新定理或重做已成立的局部截面／最小模型论证。
该修复的引用依据和实际访问范围已在 §5.2 保存。

### R3 — MINOR：反典范幂及“不提升”的主语

位置：`main.tex` 第 32–34 行；`sections/01-introduction.tex` 第 13–16 行。
这里分别写 `the anticanonical line bundle` 和 `a section of an anticanonical line bundle that does not lift`。
全 tame 情形实际使用的是 $L_m=\mathcal O_S(mD)$，即反典范线丛的第 $m$ 次幂，非仅 $L_1$。
而且 $L_m$ 本身已定义在圆分厚化上；不能提升的是指定截面 $J$，不是该线丛。
正文 §1:60–62 和 §6:15–110 完全正确，故这是前置说明的指称／语法精度问题，不是 Bockstein 证明错误。

最小修复：摘要改为 `the actual Bockstein for the relevant anticanonical power`；
引言改为 `The original small-order invariant is a section of an anticanonical power, and this section does not lift across the first infinitesimal cyclotomic thickening.`
这也避免在共同记号定义之前插入新的未定义 $m,D,S$ 记号。
影响只在摘要和引言说明语句；不改 $\beta_{L_m}$、$\rho_X$、$\kappa_J$、$\nu$ 的实际定义或箭头。

三项为源定稿前应完成的明确小修，不是新的科学验收门。
没有另加必须执行的风格建议或要求重新评价未变化的数学。

## 7. 交接

原 v1 源保持不动。本轮结论是：所有必要正文证明已经真实写入，且未识别新硬数学缺口；
三项 MINOR 在明确的新 successor 中修复后，核对实际差异及相应源身份即可关闭本轮遗留。
届时无需重读未变六十九件、重打新意分、再预测容量，或重新证明未变化的二十个消费者。
正式完整 source-byte manifest、第一次自然构建、实际正文窗口、逐页 PDF 阅读、同源双根确定性与独立终局验收仍是后续工作。
本报告没有执行或预授这些产物阶段，也不把 Paper30 计为第四篇完成。
