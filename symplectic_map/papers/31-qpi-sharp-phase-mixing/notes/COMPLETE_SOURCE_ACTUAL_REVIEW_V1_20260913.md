# Paper31：完整实际英文源 V1 首次编译前独立审查

日期：2026-09-13 UTC。审查者：`/root/p31_complete_source_actual_review_v1`。
角色：fresh 非作者；未参与原证明、大纲、两锁或英文 TeX 写作；未再委派。
实际使用 secondary Codex xhigh，不冒称不可用的 GPT-5.4 MCP、跨模型或真人评审。
`route_applicability: NOT_APPLICABLE`；本件不是新的数学准入、查新、四门评分或 PDF 验收。

## 1. 完整实际源结论

`actual_complete_source_verdict: SCOPED_SOURCE_CORRECTION_REQUIRED`。
已亲自 FULL 读取当前 `paper/v1/` 全部 12 件、共 2,394 行／105,772 bytes，而非仅摘要、差分或作者报告。
实际数学转录、主定理量词、全部必要分析证明及英文叙事未发现新的必须修改项。
唯一必要修正 M1 是基础接口的来源归属：V1 把完整原映射 lift 一并归于 P30 §2，但该精确引文位置未给出此完整断言。
这属于实际稿件的引用支撑问题，不是反例，不否定已接受的原 lift，不重开旧科学或正式准入门。

- `critical: []`
- `major: [M1]`（基础接口引用范围；不表示发现主定理错误）
- `minor: []`
- `required_fixes: [M1]`
- `page_window_verdict: UNMEASURED`
- `pdf_verdict: NOT_REVIEWED / NO_PDF_INPUT`
- `compilation_verdict: NOT_RUN`

V1 保持原样；本审查者只新增本报告，没有修改正文、书目、锁、原证明、索引或任何旧产物。
不能将本结论改写为“V1 完整 source PASS”，也不能将唯一局部修正扩大为重写整篇或重新抽取正式四门票。

## 2. 唯一必须修正的问题

### M1 — 完整原映射 lift 的来源被归到并未承载它的 P30 §2

**位置：** `sections/02-real-surface-main-theorem.tex` 15–17、40–48、56–58 行，尤其是
“The surface, polar divisor, lift, and complete-fibre assertions are the geometric interface just cited”。
其精确引文是 `QPI30Local2026, Section 2`。引言 89–94 行及书目如因来源修正受到影响，应同步核对。

**实际依据：** 本人定向亲读 P30 V4 §2 的 1–226、336–445 行。
其 `geom:surface` 明确给八中心曲面、polar boundary、四 terminal 与非退化二形式；
`geom:poles` 和 `geom:pencil` 明确给极除子、无基点、proper pencil、几何连通与有限完整纤维。
但 189–214 行的 terminal 局部映射明确只在各 terminal 的 generic points 核正则性，目的是排除极点；
它们不等于所有合法点上的全局自同构证明。该节未找到可承载 V1 “lift” 归属的完整命题。
OMAP 90–128、208–223 行也把“全部合法状态正则同构”另定位到 R30 Step 1，而不是只列 S02。
本报告只亲读该定位，不冒称本轮重新审了 R30 全文或其 lift 证明。

**为什么必须修：** 后续在完整 U 上延拓不变式、使用 Koopman 酉性、控制 `f∘F^r` 的原有限范数，
均实际消费此自同构。允许把已接受模型作为合法引用输入，并不允许把不同来源的责任合并归到不支持它的精确章节。
正文已证明正则完整纤维上的真实 `+P`，但其 79–80 行又使用原 F 已正则，因此这段本身不能补足错误归属。

**最小修正：** 在明确 successor 中把 P30 §2 的曲面／pencil／有限纤维责任与原 F 完整 lift 的来源责任分开，
为后者给真实、已核且准确定位的原来源，或在本稿补上已接受的必要有限局部核验。
若采用新增原来源，只核该实际接口及真实书目／版本，不要求全面重新查新。
保留当前完整 U、四 terminal、原 F、真实 `+P` 与全部定理量词；不得以删去例外点、仅声明 torus 动力，
或把 lift 悄悄改成新假设来“修复”。不强制新增某个指定条目，也不把 root 正在核对的来源预先当作本报告已核证据。
修正后的复查只需覆盖这些变动及其实际影响；未变的 §§3–7 不需要重复首次 FULL 审查。

## 3. 实际证明转录核对

以下位置均为本人刚读完的 V1 实际正文；证据名称在 §6 绑定，不以旧报告的 PASS 替代阅读。

| 必要责任 | 实际落点与本轮核对结果 |
|---|---|
| 完整原对象与实 locus | §2:6–108 明列原 F/h/Ω、八中心、D、代数 `mathcal U_T` 与实 `U_T`；terminal 均保留。P30 曲面与 finite-fibre 部分忠实，lift 的单独来源只剩 M1。 |
| 原真实 `+P` | §2:61–80 有逆式、原能量代入、光滑几何连通纤维整性、射影曲线延拓与弦切核验；不是从正特征 fixed-scheme 结论外推实数。 |
| 全实圆与两坏值 | §2:112–211 包含全部实临界消元、Hessian、两个简单判别式零点、2/1/2 圆、h=1 的四阶点、component group 和孤立／split 两节点。未将同能两圆合成一圆。 |
| terminal 与测度 | §2:82–108、240–263、293–307 的四组密度、能量导数、正 coarea 和原图有限范数均匹配 M/GEO；properness来自有限基变换与实紧性，不从“纤维紧”猜出。 |
| 正确 Π | §2:233–286 真正定义逐连通圆均值并证正交／对易；明确不是 `ker(U−I)`，上侧 −1 与下侧 +1 的合法原光滑反例均在正文。不假设中心化仍原光滑。 |
| 完整主定理 | §2:311–435 保留所有 T>0、原 C_c∞、C20、固定能窗、全部 A/B/D 精确系数、全 k、圆重数、两奇偶及正 limsup；saddle 逐 N 的 C^(N+2) 单独量化。 |
| PF 原 forcing | §3:43–168 完整转录 G0/G1/G2、组合 Q 的 Q(O)=0、两次 Leibniz 全部移动项，特别保留 `2X'_P f_h(P)`；真实 +2P 的 forcing 乘二并解释固定周期差。 |
| 有限锚与阈值 | §4:24–189 给持续圆双侧解析参数化、真实 J(h−)=0、精确中心 β/γ、中间存在性、原 2P 有符号弧与 h=9/8 的解析代值。γ=−12/(3125 L0) 与 B 原公式一致。 |
| 可微无穷常数与完整分类 | §4:197–430 保留根方程、完整积分 log4 常数、两个移动短弧尺度与偏导控制；先求导再取 J 极限，不除 logT。T=1 严格性、全部非退化极大及五行按圆分类闭合。 |
| 同一原解析时间 | §5:14–138 与 N 一致：原线性化符号、上下穿箱次数、原 F² 的同一个双侧解析 τ、τ(0)>0、全圆传递延拓；没有不同象限任意拼提升。 |
| 投影正则性边界 | §5:142–194 有原时间积分与全非零模双界、可增长的加权范数，以及 separatrix bump 的非 Hölder 原路径例子。没有把所有 Fourier 范数都说成发散。 |
| 全圆混合符号 | §5:198–350 完整实现 K：移动入口所有阶的准确公式、Euler/angle 隐函数归纳、恢复 p/q 因子、固定短时外弧、开重叠与 θ=0=1 接缝，最后转换普通能量导数并周期分部积分。 |
| 倒导数与真实边界 | §5:360–490 的 R_hyp 极限、Q_inv=eL²/R_hyp、各阶能量符号、transpose 类保持与 `Q_inv T^j a_k→0` 边界准确。全 k 的 Σ|k|^(−N−2) 绝对求和保留，C20 没有越权控制任意 N。 |
| 正向椭圆角与原 jets | §6:13–181 的 Ω=−b dp∧dq、正 Hamilton 方向、零均值原函数、signed-radius 半周对称、偶函数下降积分、四阶 Taylor 除法和 2J+4+S 原范数均完整；d_{f,k} 的非首模明确为零。 |
| 两种精确端点 | §6:199–335 明确固定 cutoff 支撑，普通端点负号及 β²、二次端点 i/(2πkγ) 与余项正确；使用实际紧支积分而不是不收敛裸积分。全模余项分别由 C12/C10 控制。 |
| 全局交换与驻相 | §7:5–98 两次 Cauchy–Schwarz 给绝对可积 Fourier 表示，后续另用可求和导数界；自足 C_c4 一维驻相给正确 Jacobian、2π 规范和全 k 余项。 |
| 完整分割 | §7:102–147 的权重整圆常值且只乘一次；acnode 和持续圆分离，T=3/16 持续管作一次双侧驻相；G 不变足够，未要求上圆每个权重 F 不变。compact saturation 排除新空间端，terminal 未删。 |
| 原奇偶与 sharpness | §7:151–267 给准确上圆交叉配对与相位、负时共轭、单上圆奇数为零的限制；正则单模 bump 与原 Morse 线性 bump 均合法。实余弦及复两频率平方模论证给正 limsup，非所有时刻下界；generic 只限一阶 jet 对开稠密。 |

作者集成的六项澄清另作了针对性核对：G=G_T、代数／实 U 分离、Π 的 fixed-point 术语、PF/频率复用定义、
H_box 避免 H 冲突、d_{f,k} 非首模置零均吻合原证据。saddle 从“χ 可取近零为1”写成任意固定平滑紧支 χ，
证明实际只消费其有界有限导数及外端消失；节点端仍由 Q_inv 的 e 因子消去，因此此表述不改变已接受估计的科学内容。
N 中不被 G 消费的精确空间薄层常数及 n=0 尖锐性没有被强行加入；这不是必要证明缺失。

## 4. 写作、反向提纲与引用核对

按 paper-write 与 writing-principles 作完整实际叙事检查；项目纯数学 article、原页窗和必要证明均在正文的锁覆盖默认 ICLR 9页、实验、固定一页 related work、hero 图与附录移证建议。
未执行这些不适用默认项。该技能要求的独立源审查导致本轮实际记录 M1；报告本身不修改作者文字。

标题和摘要直接讲 complete original-space projected correlation theorem；引言结果表先给三率，随后以三个从属方面解释同一中心。
按段落起句逆读，顺序为“为何 circlewise centering”→“本原系统的量化结果”→“原退化 regularity/参数/奇偶三方面”
→“已有 phase-mixing 分析与离散平均／随机机制的区别”→“几何依赖及证明路线”。各主张均有上表所列真实正文落点，未形成互不相干的论文拼接。
结论重述结果和明确不主张项，没有引入 CLT、全高阶 jet 最优分类或参数统一界。
英语叙述总体清楚、技术名词一致；未发现必须修的空泛宣传、无依据首次声明或流程元数据混入论文。

六项 bib 均有实际引用，与已 FULL 读的 CITATION_RECORDS 核对一致：FHR/MRVB 使用真实正式书目，具体比较明确绑定固定 arXiv 版本；
MRVB 的 C1/t^(−1/3) 没有误写成 sharp t^(−1/2)；HRSS 和 LLN 沿实际已核预印本身份；LLN 保留 Cesàro、Markov 保留随机机制；
P30 为 Anonymous、unpublished local manuscript v4，没有伪造期刊、作者身份、DOI或公开 URL。
071502、77 的 note 明确是文章号。M1 是 P30 的具体消费范围错误，不是其书目身份伪造。
本轮没有重新浏览这些外文全文或重做新意检索；对其出版及既有已读版本的核对限于冻结引用记录，不冒领此前读者的页码。

已 FULL 读 root 的 COMPLETE_DRAFT_STATIC_CHECK；其 12 件 hash 与本人独立核到的当前源一致。
作者的 label/cite/括号检查只作为静态记录；本轮完整内容审查独立于这些机械计数，没有把检查运行成功当作数学或 PDF 证据。

## 5. 页面与制作边界

当前输入没有任何实际 PDF。本报告没有运行 TeX、BibTeX、试排、容量探针或页数预测实验。
主源的 article 11pt/letter/1 inch、匿名块、结论后页界标记及参考文献另页均可静态看到；实际字号、边距、页数、字体嵌入、
表格宽度、公式断行与全页可读性仍须真实 PDF 检验，不能由源码字节或作者目标页数推出。
三张多列表及若干长显示公式存在待实测排版风险；高端超出30页的可能性保留，但本报告不据此预报失败或授 PASS。
原 22–30 页硬窗不变。M1 完成后按原协议进入首次完整自然构建；其后确定性双根、actual 全页 PDF 及另席终局完整性仍未验收。

## 6. 本人实际读取范围与输入身份

FULL 意味着本轮本人读至 EOF；PARTIAL 只指下列准确闭区间。SHA 均由本轮只读命令对实际整件计算，
即使文件只 PARTIAL 阅读也不把其整件 hash 冒充 FULL 内容审查。没有 Git 元数据，commit 不伪填。

### 6.1 完整实际英文源

根为 `papers/31-qpi-sharp-phase-mixing/paper/v1/`。下列 12 件全部 FULL；开始读取和报告前再次核 SHA，全部未变。

| 相对文件 | 行／bytes | SHA-256 |
|---|---:|---|
| main.tex | 41／1277 | `fcbfe0ac6f8ad6364728e7c86981bd1eef2d912c7d125c6d710a155d50cd53fa` |
| math_commands.tex | 17／577 | `d69b67aa41f2692a1df7c49de52a5299d4f6dcdec8e094d27eb603dc6fa3fc15` |
| references.bib | 60／2263 | `522103caab33d0ac629470d4fa9280590882ce4eeaa155a3fb91630daaa6fe6b` |
| sections/00-abstract.tex | 21／1383 | `6a9eb69e22ee7d7bb005081243c8921bf1bfeebc13017e6c48f1763b9d71e6d6` |
| sections/01-introduction.tex | 104／5531 | `8bcd15098686eb42542c25c703e88f63877e2410cb2757d5fc978e4c03fac5d0` |
| sections/02-real-surface-main-theorem.tex | 435／18906 | `19ee52e55e24ebc0d3287a91d97ea7f27e1b0cb6d1cd46a0e71afa11e209d2cf` |
| sections/03-picard-fuchs-forcing.tex | 174／7007 | `b812c308cce979012123edddf55704bab29a3311563aa5089ec7897f96ed72f2` |
| sections/04-global-frequency-geometry.tex | 430／18174 | `a5bcb49e7c47142e3bcf46fff6d4c3f4dada43a037170daf3b37eb74273e02d8` |
| sections/05-hyperbolic-fibre-estimates.tex | 490／22124 | `2b6c987becda66caf9c5e57e0ada24ca014043aba6a5db11bc7ee50ff90784e6` |
| sections/06-elliptic-jets-endpoints.tex | 341／14435 | `fc9a1d82c9d9d4b60bc680babde6afbeb7f9d6a3aff8286a9a99d9bf6ec686e6` |
| sections/07-global-asymptotics-sharpness.tex | 267／13318 | `57e8263b11320fe657f430d0af3b5eafdc1bb5a86ed8c3662ab2c6cbd33a25a2` |
| sections/08-conclusion.tex | 14／777 | `6cdce0e4e2c29c2f71417f55008b1281317d9f000e3c96ac812498fd561fd9c7` |

### 6.2 指令、合同与辅助证明

指令 FULL：工作区 AGENTS.md 28行、docs/WORKFLOW.md 39行；
`/root/autodl-tmp/.codex/skills/paper-write/SKILL.md` 363行；同技能根 `shared-references/writing-principles.md` 525行及 `venue-checklists.md` 73行。
首次合并输出出现截断后，PAPER_PLAN 已按 1–100、100–220、221–306 补读；不把截断的返回当作全文。

下表前五个项目文件根为 `papers/31-qpi-sharp-phase-mixing/`；其后 `[G]` 等证明根为 `docs/research-batch07/`。
简名统一表示表中精确 basename，不依赖其他作者的同名摘要。

| 输入／实际范围 | 整件行／bytes | SHA-256 |
|---|---:|---|
| PAPER_PLAN.md，FULL | 306／41485 | `00575af53a0e9b7bdbb733697ae7048d6806eb3e97fc5b7421b597dd94355d8c` |
| notes/SOURCE_SCOPE_LOCK_V1_20260913.md，FULL | 104／8906 | `b056a664863e41cf778225118ea719a3e43b4a78c451d302703f423c931dd584` |
| notes/PUBLICATION_LOCK_V1_20260913.md，FULL | 72／6208 | `65cd1504f15890bbba0d9b9221062303f2daf17640d161f62e8841514f4e4a5c` |
| notes/CITATION_RECORDS_V1_20260913.md，FULL | 142／13161 | `85be5a08f81484538fce6190d79901726a288a09060fb83dc528766732dd7947` |
| notes/COMPLETE_DRAFT_STATIC_CHECK_V1_20260913.md，FULL | 76／6845 | `677590c427efee40cec3bd23a6cf19cdd6612a1ebf5f3b0692feb96b4e07fb6a` |
| PAPER31_QPI_Q2_FORMAL_CANDIDATE_DISPOSITION_V1_20260913.md，FULL | 126／10187 | `8693108fec4c8aa35310d40fd86c19e36429f79a1f46f225b2415e97f93e5ef7` |
| PAPER31_QPI_Q2_COMPLETE_CANDIDATE_BRIEF_V1_20260913.md，FULL | 160／12249 | `2fc821378e667a068240518489a16f64e6c39661c277c530d204dede9940a1e9` |
| [G] PAPER31_QPI_Q2_GLOBAL_DECAY_PROOF_V1_20260913.md，FULL | 358／18193 | `48fff63450138a788e4442c7b94c90e454eeebee2c1960afd895d15577c0cf6f` |
| [M] PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md，FULL | 128／7241 | `cdf173e47f86f4558ad125c5894f825441449bf4ea6c4c8801d31507e8c53700` |
| [N] PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md，FULL | 238／12871 | `f50d3291694a6156cac21edfd47af7288ab4fef2b8615c82afe1778471b3d686` |
| [K] PAPER31_QPI_Q2_MIXED_NODE_SYMBOLS_V1_20260913.md，FULL | 292／15637 | `f01797fdfaf8bcff40881cac199ff9e06fc1484bc578a2fad2f3c599b129cb79` |
| [E] PAPER31_QPI_Q2_ELLIPTIC_JETS_V1_20260913.md，FULL | 377／17873 | `adaa676ad6fd049d65f2137eb52ee158a98604a652bcd7505c62f4ddf9aebfe6` |
| [GEO] PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md，FULL | 208／11847 | `f0c92b3d03bc1686deb63877777d36c6297efde779d2fc02f81cde4d86e8a196` |
| [B] PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md，FULL | 144／7701 | `9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d` |
| [MID] PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md，FULL | 115／6053 | `4b07925048eb416d431d1e924c7d54a46c90c1a9b08708b6647c4430a79860a3` |
| [UP] PAPER31_QPI_REAL_UPPER_RETURN_FINITE_TWIST_V1_20260912.md，FULL | 112／5614 | `beaff1ed89c8f99b71f241340c5833d74ab1debfebf0c408335d2e4ed3dd5bff` |
| [INF] PAPER31_QPI_REAL_INFINITY_C1_ASYMPTOTICS_V1_20260912.md，FULL | 215／11115 | `a6949cdae36598dd7b6d607e32f172321edeb046ebb08d1fab63dd9fa23191f6` |
| [TW] PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md，FULL | 133／6753 | `63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24` |
| [PF] PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md，PARTIAL 1–175；完整覆盖 Claim、规范与 Steps1–2 | 267／10608 | `c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b` |
| [OMAP] PAPER31_QPI_REAL_GLOBAL_TWIST_CURRENT_PROOF_MAP_V1_20260912.md，PARTIAL 90–180、202–225；另作定位搜索 | 265／22687 | `666bc9b73e7b98a270ed17138cbfa07392ec3e4efa451f088e11d80ab6dbe77e` |
| P30 V4 sections/02-surface-pencil.tex，PARTIAL 1–226、336–445；位于 papers/30-qpi-vertical-critical-ideals/paper/v4/ | 446／20456 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |

另对 P30 V4 `sections/01-introduction.tex` 与 `02-surface-pencil.tex` 做过 lift/isomorphism/automorphism 等定向词搜索；
前者仅看到搜索命中行，不将其记为正文 PARTIAL 连续阅读，更不是 FULL。未读 P30 PDF、其余整稿、R30 原件或38件祖先全包。
未作外部来源新检索、数值／CAS／参数或阶数枚举、生产构建、投稿、上传、发信或付费资源操作。

## 7. 交付与停止

唯一新增文件为本报告。交付前本人 FULL 读回该报告至 EOF；报告行数／bytes／最终 SHA 在交付消息中绑定，避免自引用哈希。
M1 以外 `required mathematical/prose fixes: []`；没有为了凑问题新增审查门或要求重扫已接受输入。
本件交付后停止编辑。后续若收到明确任务，只对真实 successor 变动或新实际 PDF 作相应续查；本轮不预授任何后续门 PASS。
