# Paper30 qPI Vertical Alpha 完整 V1：首次正式评审 R1

日期：2026-09-09（UTC）。执行者：/root/p30_qpi_vertical_alpha_formal_v1_r1。
对象：冻结 brief 的完整 V1–V3，不是旧整数 C1–C3 或旧 T1–T7 的再次投票。
终态：**本席四门合取 PASS，创新余量较小，容量超窗风险实质存在。**
本报告只给 R1 自身判断；不知道本轮另一席结论，不代作两席合取或项目准入。

| 固定门 | 本席结果 | 结论 |
|---|---:|---|
| 新意，至少 7.5/10 | 7.6/10 | PASS，余量小 |
| 独立科学价值，至少 7.5/10 | 8.3/10 | PASS |
| 完整证明信心，至少 9/10 | 9.2/10 | PASS |
| 自然 22–30 页完整实质正文 | 可信存在，详见 §8 | PASS，非页数保证 |
| 本席自身四门合取 | 四门均通过 | PASS |

分数为未校准的解释性判断，不具有小数实测精度；阈值仍按原数值严格应用。
本席没有平均、进位、借用旧有利分项，也不因任一旧票失败预设本轮失败。
数学接受、正式候选准入、正文/PDF 产物验收是不同状态。

## 1. 执行身份、权限与审查纪律

本席为本轮新任务、新上下文的实际可用 Codex xhigh 实例，未参与所评作者证明或输入组织。
本人完成同一完整对象的全部四门，没有再委派，没有按学科或门分摊评审。
提交前未读取本轮另一席的报告、消息或内部记录，未与另一席通信。
没有读取主控历史或私有记录；没有打开旧正式评分报告。
共同输入公开的旧失败处置、7.2 预筛及其他意见均已阅读，所以不声称对历史评分盲审。

本人完整读取 research-review 技能、ARS academic-research-suite 根，
以及其 reviewer WORKFLOW、review_quality_thinking、review_criteria_framework、
quality_rubrics 和 peer_review_report_template。
用户固定两席、各席完整四门的合同优先；没有运行 ARS 默认五席、期刊评分或 Sprint 拆分。
技能的实际作用是证据锚定、保留最强反对意见、只读边界和执行/校准披露，
没有据技能增设实验、另一个创新类别或不同验收门。

技能指定的 GPT-5.4 MCP 当前未配置；实际使用已披露的可用 Codex 新上下文替代，
未安装服务、调用其他模型、上传候选或外发审查请求。

- cross_model_verification: NOT_PERFORMED
- score_calibration: NOT_CALIBRATED
- criteria_binding_unavailable
- 本轮 peer-output：提交前不可见。
- 不声称人类同行评审、跨模型认证、统计独立错误过程或期刊接受概率。
- Route A/B：NOT_APPLICABLE；这是纯数学候选，不触发正式 Route 评分。

唯一工作区写入为本报告；科学输入、索引、锁、论文及旧失败记录均只读。
没有试写稿件、试排、编译、运行数值实验或创建论文项目。

## 2. 输入身份与 69 件本人 FULL 记录

共同输入为本清单及其绑定的另外 68 件，不存在本席秘密增加的本地科学材料。
69 件均由本人逐文件读至 EOF；长文件分段读取，工具截断部分已补读后才记 FULL。
下表的 FULL 指本人阅读，而不是沿用他人的 FULL、摘要或数学 PASS。
随后另作字节身份核对：69 件可读，清单绑定的 68 行行数和 SHA-256 全部相符。
身份检查不代替数学核查，也没有重扫旧论文或构建树。

三入口身份分别是：

- 清单：216 行，9011f6644a85a104051bbc95b462390ce9276101f04da230157b08dd266ac400。
- brief：251 行，168be8025f1c8215634306ebd02b5c16319781a57026f846240d3578a10a2bed。
- 当前证明图：261 行，790f29ea9f315bb8a532fe2c51b7c8a9284acd61295aed5b6c9ae4d5ebfc26ea。

下表 ID 与清单相同。全部文件位于 docs/research-batch07/；
后文使用 ID 引用时，准确文件、行数和哈希由本表确定。

| ID | 完整文件 | 本人读取 | 行数 | SHA-256 |
|---|---|---|---:|---|
| MANIFEST | [PAPER30_QPI_VERTICAL_ALPHA_REVIEW_INPUT_MANIFEST_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_REVIEW_INPUT_MANIFEST_V1_20260909.md) | FULL | 216 | `9011f6644a85a104051bbc95b462390ce9276101f04da230157b08dd266ac400` |
| P | [PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | FULL | 275 | `61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3` |
| Nbd | [PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | FULL | 284 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| Gfield | [PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | FULL | 270 | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |
| Jspec | [PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | FULL | 492 | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` |
| Wreuse | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md) | FULL | 213 | `21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2` |
| Bbad | [PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | FULL | 488 | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` |
| Hloc | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md) | FULL | 637 | `0a6624550ed0f8765b51b01a1a481fd9a545d1791e10c3431effbf3f25428a3e` |
| Ddiff | [PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | FULL | 268 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| Gint | [PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | FULL | 254 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| Ucoh | [PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | FULL | 255 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| Mjet | [PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md) | FULL | 283 | `f3618fa1345804ce5d93acae4e6fdb2b3ee7761a87ae2de8bc453d24944971bd` |
| GFI | [PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_FACTORISATION_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_FACTORISATION_V1_20260909.md) | FULL | 185 | `9d53bee5abf8026dfa09d2bcb38713e0ace28ff082d9e87b3efa595ab5955a86` |
| DB | [PAPER30_QPI_VERTICAL_ALPHA_DIRECT_BOUNDARY_BOCKSTEIN_REUSE_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_DIRECT_BOUNDARY_BOCKSTEIN_REUSE_V1_20260909.md) | FULL | 173 | `a9422fb7f580b1c44e94075181211e1c110245703b4004a8011ae16dfc82ec7c` |
| SH | [PAPER30_QPI_VERTICAL_ALPHA_SMOOTH_CLOSED_HASSE_REUSE_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_SMOOTH_CLOSED_HASSE_REUSE_V1_20260909.md) | FULL | 242 | `7fc2edb5e5200e499293effb569b328cdd974c3d01119f3aec948e72ee58e4af` |
| TH | [PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md) | FULL | 219 | `43049d8688f59f57eb3362246d06507ff397ee9e150d18a3443ae8a18990be75` |
| PT | [PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md) | FULL | 269 | `07361a2516b8e891d037a59826e0e789119db93eb78332dc41783f075f15dca9` |
| OC | [PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md) | FULL | 177 | `81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa` |
| TB | [PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md) | FULL | 335 | `6546720ecf39f667f09d45235dc0c7be340032b4c3f7c809e9d1cb60257396e9` |
| P2 | [PAPER30_QPI_VERTICAL_ALPHA_P2_BLOCK_FIRST_JET_LEMMA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_P2_BLOCK_FIRST_JET_LEMMA_V1_20260909.md) | FULL | 334 | `c5fc4192822733993f361363f194832aee872ab25ce598c39e76be3b1ae62897` |
| PI | [PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_PROOF_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_PROOF_V1_20260909.md) | FULL | 227 | `1d2ff70c69cb26ec2009055f3161cb44758338db8912b9654ab8c53b5d7c59d3` |
| P-R | [PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_NON_AUTHOR_REVIEW_V1_20260908.md) | FULL | 237 | `edbf54720c0bd0624d8f6eb53d06db43965d66436b6b9a52ba67c4ef1b6f4dd0` |
| N-R | [PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_NON_AUTHOR_REVIEW_V1_20260908.md) | FULL | 287 | `769c34ec3302e8f91bce13c86add8930f1ba032c5ec8a3490dcc49963af70597` |
| Gf-R | [PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | FULL | 348 | `0964f6f0a6eb543402e0f2b2096fd5325d4eaf9912a7d8cd056b9d8193920972` |
| J-R | [PAPER30_QPI_LAX_JACOBIAN_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | FULL | 257 | `c7d355d420e966381dfc74fffbd033470e12158480a826e0d88e464a5fa40438` |
| W-R | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md) | FULL | 124 | `0db56630eab29ed89952f28dd2fd8038fa3c724040f99afbec527dd0e42c70f2` |
| B-R | [PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | FULL | 259 | `1bb3d563bdb5a2c93aa517002f69ac72398688ee74429a8b4d8662965c229815` |
| H-R | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260909.md](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260909.md) | FULL | 413 | `10122ea2a617203dcf0ef7d9755ce0ae22ec7906c70ab141891998f94294093b` |
| D-R | [PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md) | FULL | 306 | `7c0ecd10991f80f0614713f344ab600a4eb69fd7356135fcfc927ed71a95d0bb` |
| Gi-R | [PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md) | FULL | 286 | `ec49d4eaadbf4c0d53603cf6c902df375e2b1c779b6f243897521d786b206a0b` |
| M-R | [PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_INDEPENDENT_CHECK_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_INDEPENDENT_CHECK_V1_20260909.md) | FULL | 417 | `ea71b1e45228ccf00b0668f6a7015b90f0776f1beb2fe219f78b62158ad58efc` |
| GFI-R | [PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_INDEPENDENT_CHECK_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_INDEPENDENT_CHECK_V1_20260909.md) | FULL | 222 | `3465766d223fdbf244a0a361fa539a828d1e19e398697b9038d14c913d3bc3c9` |
| Reuse-R | [PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_INDEPENDENT_CHECK_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_INDEPENDENT_CHECK_V1_20260909.md) | FULL | 284 | `1dfb909f696c01dc5fd5fe69bf8c5ae774d364327bc8dca2dc7736e17ef28271` |
| TH-PT-R | [PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_INDEPENDENT_CHECK_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_INDEPENDENT_CHECK_V1_20260909.md) | FULL | 286 | `26b01f26f16837f6fd13c4492a46115eeab2cd5c9ac2278bc85f39d1483bf6f5` |
| OC-R | [PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_INDEPENDENT_CHECK_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_INDEPENDENT_CHECK_V1_20260909.md) | FULL | 222 | `cb5ec4eda57c74584a03c1aca4d78fa43ee898b8b6d73619f417d0d2bdd3083e` |
| TB-R | [PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_INDEPENDENT_CHECK_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_INDEPENDENT_CHECK_V1_20260909.md) | FULL | 360 | `caaf7de60b9bda61db9ea413dab736aa06f71eb6e94cc2f2c939774dd8572a88` |
| P2-PI-R | [PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_INDEPENDENT_CHECK_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_INDEPENDENT_CHECK_V1_20260909.md) | FULL | 481 | `2e9f067368bac092cf821ad8824143b4a1a244273fd9d039d43048e2d3998b1b` |
| DG | [PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md](PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md) | FULL | 173 | `ed09aadb40752ed579bc45edb7b3531c1f78f6c7f7413072cd120315f2b22245` |
| DD | [PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md](PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md) | FULL | 224 | `0bfbde8003d049d80523a2001d410dfa4f38ab2f14838d2dbbe4c1363f7155a7` |
| DH | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md) | FULL | 87 | `40e4fa6460d34ebff7cfc0e20d614f3a2050590f10c58605819cba867e65dad7` |
| DI | [PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md) | FULL | 162 | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` |
| DM | [PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_MATHEMATICS_DISPOSITION_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_MATHEMATICS_DISPOSITION_V1_20260909.md) | FULL | 135 | `8a9395f73647cb309921702abd52088b788be8c565686c453a419cd5bb57b5d8` |
| DGFI | [PAPER30_QPI_VERTICAL_ALPHA_HIGHER_JET_MATHEMATICS_DISPOSITION_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_HIGHER_JET_MATHEMATICS_DISPOSITION_V1_20260909.md) | FULL | 98 | `fb90b364abf5a629b86faf2260930efb71f655b4b0f1d0b9e6066489c8270575` |
| DT | [PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md) | FULL | 108 | `a71577e3bbced32f05b1546b9a6373a4d977ce1f60bcb5dce7e7e8ce5f3e8302` |
| DA | [PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_JET_MATHEMATICS_DISPOSITION_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_JET_MATHEMATICS_DISPOSITION_V1_20260909.md) | FULL | 127 | `e1d2897841fa89b95f8339a9af64f0901183cef47d49be75076f7a18b6ab5cc8` |
| DR | [PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_DISPOSITION_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_DISPOSITION_V1_20260909.md) | FULL | 67 | `9656193743a15267572a4e10e7c80686338fdff44acf843a6a42576c8ea32fb9` |
| V-A | [PAPER30_QPI_VERTICAL_ALPHA_SCOPE_PHASE_A_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_SCOPE_PHASE_A_V1_20260909.md) | FULL | 179 | `ca6a8e6695709c2eaaff4707bcb94ccfd86367afb492d5ea87da6a1d90396f2f` |
| V-B | [PAPER30_QPI_VERTICAL_ALPHA_NOVELTY_PHASE_B_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_NOVELTY_PHASE_B_V1_20260909.md) | FULL | 351 | `6d12a7496a70b59ce1596559d75395540fc7d78f138d36d181552b46490a9f21` |
| V-CD | [PAPER30_QPI_VERTICAL_ALPHA_NOVELTY_PHASE_CD_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_NOVELTY_PHASE_CD_V1_20260909.md) | FULL | 356 | `0e0ac2e0a9c01012d6edb4c29f0ae0a0fc3edb6376d7476f67b1a71e77ddc667` |
| V-PF | [PAPER30_QPI_VERTICAL_ALPHA_PORTFOLIO_DELTA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_PORTFOLIO_DELTA_V1_20260909.md) | FULL | 314 | `03219910add96d998bb3636f1d77e830be688d8852b437da7c8d01be9f3e6499` |
| V-srcH | [PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_SOURCE_DELTA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_SOURCE_DELTA_V1_20260909.md) | FULL | 215 | `6d7bbe36569a110c68c181d1ae70857760ac5b1d062ab10cba295f368e412990` |
| V-srcOC | [PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_SOURCE_DELTA_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_SOURCE_DELTA_V1_20260909.md) | FULL | 200 | `6cb9ec0d8039d6b86c841a94b860e7b19cf1c7716ec57aab70f1324181e3af7d` |
| V-PRE | [PAPER30_QPI_VERTICAL_ALPHA_PREFLIGHT_DISPOSITION_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_PREFLIGHT_DISPOSITION_V1_20260909.md) | FULL | 117 | `7f00218963b74c70640c4096e6f3da0342f8cef2512f5eea11f57a4d57f10a1e` |
| V-DEP | [PAPER30_QPI_VERTICAL_ALPHA_PROOF_DEPENDENCY_AUDIT_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_PROOF_DEPENDENCY_AUDIT_V1_20260909.md) | FULL | 249 | `b44ff43bf81163bb8f5a08e8a58f54bc8c3b32a81d78440b0d35c63ae3ef3672` |
| I-srcD | [PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md](PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md) | FULL | 168 | `8d24144c5e49ba30402a2749536ec0b66ca6170d6dcf9a85273330829c22a88f` |
| I-B | [PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md) | FULL | 295 | `44f628fbc07cad422f83c136cf1dd3fb2bae9d7a7782db3798a073b5ab1bdf41` |
| I-CD | [PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md) | FULL | 267 | `d76e5e71001cd8033608a76673f61169f264caee57cb37aab4f86d1390dd8f02` |
| I-FAIL | [PAPER30_QPI_INTEGRAL_FORMAL_CANDIDATE_DISPOSITION_V1_20260909.md](PAPER30_QPI_INTEGRAL_FORMAL_CANDIDATE_DISPOSITION_V1_20260909.md) | FULL | 125 | `da3b7365053cbf7a1e4ab5817aac45ce9baee8f6162307ce25f0875b3cea6b6c` |
| Old-AB | [PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md](PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md) | FULL | 268 | `4470af64294525bc4ae33b9b00fc38c44c38215290a36fa6f3a5b6bdf861f90e` |
| Old-B | [PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md](PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md) | FULL | 112 | `2aae448ca17022aa7b51990b84058e57ee455ab0e4c0a4127d8e0ec7fc39c898` |
| Old-CD | [PAPER30_QPI_NOVELTY_PHASE_CD_V1_20260908.md](PAPER30_QPI_NOVELTY_PHASE_CD_V1_20260908.md) | FULL | 247 | `8dadbaf066979a17ac87620ad5017e8e732c52ee81a68e4fc2ff545a249ecb82` |
| Old-FAIL1 | [PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md](PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md) | FULL | 136 | `0452b7aa8f28107ae65f3fa840647806b50eab2502340d1c609a0ca6c545ce90` |
| Old-FAIL2 | [PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md](PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md) | FULL | 116 | `fb490d26321a3077b839d1e3505979150b7ad02bf59c6f5beba93a9977003584` |
| Src-JR | [PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md](PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md) | FULL | 98 | `ab82c19d1bd6a182323b033f7d8c48e47de4e0839a9d5bebd2e4ead456ad4475` |
| Src-OH | [PAPER30_QPI_OHYAMA_SOURCE_GAP_CHECK_V1_20260909.md](PAPER30_QPI_OHYAMA_SOURCE_GAP_CHECK_V1_20260909.md) | FULL | 137 | `2cc3fa6636ff0bf878d54b5f32feb36755054a586dc1ba1f6e484dafdfd715e6` |
| Src-GRT | [PAPER30_QPI_GRT11_SOURCE_GAP_CHECK_V1_20260909.md](PAPER30_QPI_GRT11_SOURCE_GAP_CHECK_V1_20260909.md) | FULL | 133 | `67b27d4662f3f51a9552795676b5294e9eacd400d8ca1a38820a5a1b9c183356` |
| Src-D | [PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md](PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md) | FULL | 73 | `34985ed628bfc2185f9674490f41766d6ce11a0d63da018962791d833d6d1c01` |
| BRIEF | [PAPER30_QPI_VERTICAL_ALPHA_CANDIDATE_BRIEF_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_CANDIDATE_BRIEF_V1_20260909.md) | FULL | 251 | `168be8025f1c8215634306ebd02b5c16319781a57026f846240d3578a10a2bed` |
| MAP | [PAPER30_QPI_VERTICAL_ALPHA_CURRENT_PROOF_MAP_V1_20260909.md](PAPER30_QPI_VERTICAL_ALPHA_CURRENT_PROOF_MAP_V1_20260909.md) | FULL | 261 | `790f29ea9f315bb8a532fe2c51b7c8a9284acd61295aed5b6c9ae4d5ebfc26ea` |


合计：3 入口、20 作者、16 非作者、9 责任合取、21 来源/范围/反对意见，69 件。
全文可见不等于消费所有历史出口；当前必要责任按 MAP 及以下逐项判断。
阶段 A 的 pending、作者稿旧待审和替换前依赖诊断不自行撤销 DA/DR 的同字节接续。
本席仍自行检查实际推理，不将这些处置直接当作本轮证明票。

## 3. 所评完整命题及量词

固定原八截面吹起、反典范八环 D、L_n=O(nD) 和 U=S\D；
U 包含环面和四条完整末端仿射线。
原状态映射为 F_t(x,y)=(st/(sx-y),sx/y)，时间变为 st。
原矩阵 A 与降序积保持 brief §2.2 的规范，不换谱等价矩阵或重新归一化能级。
特别取
\[
 M_{r,s}(z)=A(s^{r-1}z;t)\cdots A(z;t),\qquad
 I_{r,s}=[z^r]\operatorname{tr}M_{r,s}(z).
\]
取含精确 m 阶根 \widetilde\eta 的无分歧 p-进 DVR O_0，
置 O_a=O_0[ζ_{p^a}]。令 p∤m，a≥1，N=p^a，s_a=\widetilde\eta\zeta_{p^a}，
π_a=ζ_{p^a}−1，t_a 为任意单位时间。先在特征零中定义
\[
 \alpha_{mN}=p^{-a}d_{\rm state}I_{mN,s_a},\quad
 J=I_{m,\eta}(x,y;\bar t_a),\quad T=\bar t_a^m,\quad
 \varepsilon_m=(-1)^{m+1},\quad \sigma=(N-1)/(p-1).
\]
d 只沿原两个状态方向。Ddiff/Gint 给它在完整原 U 上的正则性。
H=H_p(T,J;ε_m)，准确规范为
\[
 H_p(T,h;\varepsilon)=
 \begin{cases}
 [Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
 h,&p=2.
 \end{cases}
\]
\mathfrak c 指秩二相对余切模中全部系数生成的理想，与局部标架无关。

V1 允许完美剩余域；TB 及高层实际几何理想保留有限剩余域范围。
P2 的纯块恒等式允许完美域，不将这一量词自动赋予 PI。
完成、有限无分歧扩张及返回未完成局部 DVR，仅在原证明范围内使用。
以下 X 均为原完整光滑有限概形纤维，而非环面部分或任意同亏格曲线。

### 3.1 V1：原完整理想与实际障碍

对每个 p,m、a=1、每条 X=(J=h) 及其所有点，有
\[
 \mathfrak c(\alpha_{mp})=(\pi_1,\widetilde H).
\]
这是原完整理想，不只是模 π_1² 的等式。
若 h 是 H_p 的 e_h 重根，完成后是 (π_1,z^{e_h})，\bar z=J−h；
不添加简单根假设。

每条完整光滑 X 上均有实际非零类
\[
 0\ne\kappa_J=\rho_X\beta_{L_m}(J)\in H^1(X,\mathcal O_X).
\]
β 来自同一圆分首层厚化，ρ 使用原截面 1 的指定平凡化。
在 H_p(T,h;ε_m)=0 的光滑层，原迹构造的首切向类满足
\[
 \partial\nu=\operatorname{Fr}_*\kappa_J\ne0
       \quad\hbox{in }H^1(X,\mathcal O_X^p).
\]
这不是把像层再包含进 O_X 后的 H¹ Frobenius 算子。
因此没有“超奇异曲线 H¹ Frobenius 仍可逆”的矛盾。
ν 在完整 X 上处处非零，既不是任选补基，也不是未知非零标量下的替代。

### 3.2 V2：奇素数全块首 jet

对奇 p、a≥2，匹配完整时间二阶像后，在整个 U 上有
\[
 \alpha_{mp^a}^{[2]}=H^{\langle\sigma-1\rangle}\alpha_{mp}^{[2]}.
\]
比较使用 π_1↦π_a 的共同双数商，不是自然圆分根嵌入。
恒等式含全部块内非共振变形和实际时间 jet；
其本身不要求 X 光滑、H≠0 或 Hasse 根简单，并跨四末端线。

在完整光滑层附近，
\[
 \mathfrak c(\alpha_{mp^a})+(\pi_a^2)
 =(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1}).
\]
根重数 e_h 仍保留，完成式为
(π_a²,z^{e_hσ},π_a z^{e_h(σ−1)})。
没有从这个截断理想推出全厚度或高层准确公共阶。

### 3.3 V3：特征二不同基准及混合结构

p=2、m 奇、a≥2 时，比较从 a=2 开始，π_2↦π_a，
并选 t_2 与 t_a 在共同双数商中同像。
首层 a=1 的商是特征四，不可以识别到这里。
整个原 U 上有
\[
 \alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{4m}^{[2]}.
\]
原环面基准为
\[
 \alpha_{4m}^{[2]}=(j_*^3+\epsilon T)dj_*+\epsilon J^2\chi_m,\qquad
 \chi_m=J\,dJ+[z^{2m}]\operatorname{tr}
       (d\mathsf B_0\,z\partial_z\mathsf B_0).
\]
这里 s=η(1+ε)、t=t_a mod π_a²，
\mathsf B_s(z)=A(s^{m-1}z;t)\cdots A(z;t)，j_*=[z^m]tr \mathsf B_s；
\mathsf B_0(z)=A(η^{m-1}z;\bar t)\cdots A(z;\bar t) 是原剩余 m 块。
不假定 j_* 在全 U 有正则提升，不将环境 χ_m 的全局正则性作为前提。
PI 给 χ_m 在完整 X=(J=0) 上的切向限制恰为 V1 的 ν。

于是每个所要求的完整光滑层点上，
\[
 \mathfrak c(\alpha_{mN})+(\pi_a^2)
 =(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_a j^{N-2}).
\]
这里 j 为任意局部提升，\widetilde T 为常数单位提升。
a=2 的允许完成/无分歧剩余扩张后，
\[
 k(P)[[w,z,\epsilon]]/(\epsilon^2,z^3+\epsilon T,\epsilon z^2)
 \simeq k(P)[[w,z]]/(z^5),\qquad \pi_2\mapsto z^3/T.
\]
五是截断商沿曲线的横向长度，不是闭点总 Artin 长度、
原完整临界商长度、平坦性或全高度厚度。
单位 T 经允许的剩余扩张可正规化，不另外计为新形式模量。

### 3.4 状态阶不是超出理想的额外猜测

沿允许的无分歧光滑超奇异状态：

| 分支 | α 公共阶 | 未整除 dI 公共阶 |
|---|---|---|
| 所有 p，a=1 | 准确 1 | 准确 p |
| 奇 p，a≥2 | 至少 2 | 至少 aφ(p^a)+2 |
| p=2，a=2 | 准确 1 | 准确 5 |
| p=2，a≥3 | 至少 2 | 至少 a2^{a−1}+2 |

普通光滑状态分别准确为 0 与 aφ(p^a)。
这些数值来自同一理想取状态像再乘回 p^a，
不是旧扭子长度或有限实验的推论，也不把“至少二”改成“准确二”。

## 4. 完整证明核查：必要链、实际证据及保留风险

本席未发现可定位的新硬数学缺口或反例，故没有强制补证明项。
此结论不是形式化证明或零错误保证。
下列判断覆盖原模型和几何旧链，非只审新增 V1–V3 末端公式。

### 4.1 原模型、极除子、完整 pencil 与整数延拓

P Steps 1–6 的原中心/末端图、辛形式和原 Laurent 首项，
以及 Nbd Steps 1–7 的真实单位帧与节点传播，给原极除子及法丛精确阶。
参数相等发生在不同边界分量时不合并中心；
四末端线上的局部式不是被删掉的例外集合。

Gfield 的 h⁰=2、Stein 分解次数一及几何连通性是实际原 pencil 的论证。
无穷远 SNC 分量的互素重数阻止水平临界分量，
这一步承担 p=2,3 中不能默认排除的泛非光滑问题。
本席没有用特征零 Halphen 口号代替其全部允许特征证明。

Ucoh 105–149 的真实常数及整节点计算保留；
DB 只改接本次首层消费者，不恢复 Ucoh/Ssplit 的所有导出分裂出口。
Ddiff 111–192 先作整数循环插入 dI=r[z^r]Q，再除 p^a；
不能把特征 p 中的零微分除以 p。
Gint 的正规模型、余维一正则性和自由相对余切模
将实际 α 延至全 U。其 G2 大阶扭子及 G3c 长度比较不被调用。

### 4.2 W0、谱族和原域 Jacobian：没有用同谱式偷换对象

Bbad 的纯 W 段首先独立提供射影平坦、总空间正则和有限纤维几何前提。
实际双向消元给
\[
 Z_W\simeq\operatorname{Spec}k[z]/((T-z^2)^2-\varepsilon_mTz).
\]
这里 T 为单位；首一四次式给有限临界性，从而供给 W 的泛光滑。
这条供应不反向调用旧原动力临界长度四或其特征多项式。

Wreuse V2 的原谱两图、端点、有限推下和 Step 2a 原域接口保留。
Jspec 236–454 的实际链逐项核查如下：

1. 光滑谱曲线使实际谱代数模逐纤维循环，故构成线丛族；
   不是只在若干几何点构造特征向量。
2. 有限推下及谱线丛同构恢复矩阵的常数共轭类。
3. 原最高投影、次高系数和常数矩阵恢复原 x,y 的有理函数；
   这是真实有理逆，排除正特征纯不可分次数，不是点集单射冒充双有理。
4. 原 A 的循环复合为乘 λ，其支集处各点被全循环群固定，
   给固定除子差 3P_0−2Q_2−Q_1，因而差落在不变 Picard 分支。
5. 循环覆盖全群固定点排除非平凡拉回核；核是 tame 挠 étale 部分，
   加上不变切空间维数一，识别的是完整 J_E，不是未知核同源。
6. 稠密像、完整 genus-one 曲线及原域定义的数据，
   给原 k(c) 上 J_E-torsor 作用和实际 Jacobian 身份；
   并未凭空产生全局原域有理点。

上述是当前完整候选的实际贡献与必要证明。
它们曾在本地较早接受，不等于已公开发表的先例，不能因此将其新意自动归零；
但 Beauville/IVY 的一般谱-Picard机制仍须实质扣除。

### 4.3 每条完整光滑闭层的 Hasse 身份

SH Steps 1–2 从已光滑 X 加原 pencil 的几何连通性得到几何整约化、亏格一。
这替换的是当前选定光滑纤维前提，而非证明全部奇异纤维分类。
因此不消费 Ffib 全部旧出口，却仍消费上述原泛谱身份。

Hloc L(a)、L.1–L.3 与 SH Steps 3–4 在同一个 c=h 的 henselization：
先在几何剩余域上选光滑点并提升局部截面，再平凡化泛 torsor；
两边 proper、flat、正则及几何整约化特殊纤维均实际核准。
竖直主纤维自交零给相对最小性，指定泛同构及其逆都作最小模型延伸，
才得到同一闭层完整曲线同构。

SH Steps 5–6、Ddiff 206–233 对完整谱曲线的指定正则微分作 Cartier 运算，
包括分支点、无穷远及特征二，得到 H_p(T,h;ε_m) 的零性质。
只把这项零性质下降回原剩余域；不要求几何选点或所选同构典范下降。
故这里“超奇异”确指原完整闭层，不能用另一同名谱方程替代。

### 4.4 DB、prime、TH、OC：原完整理想的关键非零证书

DB 的节点复形先在整单位帧上固定，再约化至 A_2=O_1/(π_1²) 和 k。
1≤j<m 时边界无上同调，j=m 时限制映射 r_1 为同构且 ker r_0=k〈1〉。
实际连接的自然性
r_1β_L=β_Dr_0，与 1−s_1^m≡−mπ_1，
给 Bockstein 的核恰为真实常数。
原 J 非常数，所以 β_L(J)≠0；不能仅凭两个空间一维得到这一结论。

随后原 1 平凡化的限制序列和 H¹/H²(O_S)=0
给 ρ_X 的真实同构，适用于每条完整光滑层。
DB 改接未删掉这些指定箭头。

prime §§2–6 的循环词轨道区分长度 1 与 p；
非共振项相乘可重新共振，但整数多项式的 p 因子恢复所需 pπ 同余。
由原迹递推得到 F，局部同余是 I_{mp}−F(j_i)∈pπ_1O，
不是仅 I≡J^p mod p。符号 λ 在奇 p 和 p=2 不同，
p=2 的特征四项必须在除 pπ 前保留。
TH 在非约化底环用四末端图的 u 非零因子落实全图同余。

OC 的 G_i=(I−F(j_i))/(pπ_1)、实际 Taylor 及差商
给 G_j−G_i 在 X 上等于 f_ij^p，局部 dG_i 粘成 ν。
像层连接的 Čech 计算得到 ∂ν=Fr_*κ_J；
到 O_X^p 的 Fr_* 为加性层同构，故该类非零。
proper 光滑 genus-one 曲线的非零正则微分处处非零，
这才与法向 dJ 合取为原秩二系数理想 (π_1,\widetilde H)。
这个推理没有用任选第二类补基来替换本题固定类。

### 4.5 奇素数全 m、全高度与全部时间 jet

Mjet 的通用秩二插入和带权交换子接口保留，
但 TB 105–299 自行承担全 m 的支持界，不从旧 m=1 检查外推。

TB 先按完整 m 块插入得到 dI=N[z^{mN}]Q，没有多余的 m 除数。
平方零展开分开块内项和块间谱缩放项；
内部投影只使用 P_m(Q(z^m)V)=Q(Z)P_m(V)，从未把 P_m 当环同态。
实际 j_*、首尾单位系数及时间 jet 均留在内部项 H_*^σdj_* 中。
外部交换子 Γ 的最高可能项真实抵消，次数处于 1 至 6m−2，
共振投影再给 1 至 5 的支持范围；
与低位四次幂的支持合起来，迫使唯一基 p 数字选择。
这才得到外部项 H^{σ−1}β_p，不由标量模 p 迭代自动得到。

共同商、p∣σ−1 的提升幂独立性及 GFI/Gint 的非约化限制单射
使完整等式跨四末端线。最后乘 V1 的原系数理想得到 V2。
因此它确实含两个状态方向，而非仅切向限制或某个矩阵特征值。

### 4.6 特征二基准、局部整除和准确状态结论

P2 94–286 在特征二使用 ad²=S ad；
从 a≥2 的共同特征二双数商出发，不能拿 a=1 的特征四替代。
内部项与外部 ΓS^{N−3} 分开，真实支持界给最低二进位 4，
从而以 α_{4m} 而非 α_{2m} 为基准，并产生 εT 项。

PI 81–123 的首层特征四比较保留 2j_*dj_*，
识别 χ_m 在 X 上的限制为同一 ν。
PI 124–166 用局部正则形式差商和 lift 变换，
先在素除子泛点得到 J² 整除，再由 J 在每个光滑层点的素 Cartier 参数性质
逐次推出局部两次整除；没有因环面稠密就宣称全曲面环境 χ_m 正则。
除后切向类是 ν 的单位系数，故可消去实际两方向系数。

PI 167–212 的混合理想、局部提升独立性和高层乘数随后成立。
a=2 消 ε 得 z^5 且原 π_2 作用为 z³/T；
无分歧状态上 j∈(π_2)，混合生成元的 π_2T 项给 α 阶准确一。
a≥3 及奇 p 高层只保留所证下界。
这些是同一模型的逻辑消费者，没有拼接不同构造的最好结果。

### 4.7 证明信心的范围

给 9.2/10，PASS。依据是上述实际关键步骤和同一量词的闭合，
不是“16 份报告通过”或“文件哈希一致”。
非作者报告用于交叉检查风险点，责任合取用于辨别旧快照；
本席没有把任一标签当作缺失证明。

剩余风险是较长的谱模族/下降链、整数符号及全块支持计算的人工核查误差，
以及未来写作可能误删关键前提；不是目前已定位的失败推理。
未作形式证明器验证、未重跑历史有限样本，也未要求纯数学候选增加 ML 实验。
需要特别防止转录时把 V2/V3 截断说成全厚度、把无分歧状态说成任意分歧状态。

## 5. 先例扣除：本人原文阅读与继承证据分开

本轮公开原文访问截至 2026-09-09，仅定向复核四个关键来源。
没有另起无界检索、重试 Scholar/S2 的既有失败入口、绕过 IOP/Euclid 限制、
付费取文或联系作者。没有取得新的本地科学输入。

### 5.1 本席实际亲读的一手范围

| 来源及版本 | 本席实际可见/读取范围 | 支持的扣除与限制 |
|---|---|---|
| [Joshi–Roffelsen arXiv:2508.18578v2](https://arxiv.org/html/2508.18578v2)，2026-01-16 | §3.1 原矩阵、积分、迹谱恒等式及证明；§3.2 全节、§4 | 原对象、整系数积分、Laurent 首项、谱式及几何问题已有；所读版的 genus-one/坏值仍是猜想。不称本席亲读出版全文或证明其全球未解。 |
| [Vlasenko, Higher Hasse–Witt matrices v3](https://arxiv.org/html/1605.06440v3)，2018-04-17 | §1 定义(1)–(4)、Theorem 1(i)–(iii) 条件及半线性解释；Theorem 2 和邻接 formal-group 定义/条件。未重读 §§2–4 全证明 | 模 p Hasse 连乘不需 ordinary；可逆前提仅约束相关极限/导数项。Theorem 2 的形式群整性不是 ordinary 定理；不能以超奇异为由排除该先例。 |
| [Lubin–Tate, Formal moduli for one-parameter formal Lie groups](https://www.numdam.org/article/BSMF_1966__94__49_0.pdf)，BSMF 94 (1966) | p49 设置、Prop1.1 陈述与证明；Theorem3.1 及返回的完整证明文字、§§3.2–3.5。未通读中间全部 cohomology 引理 | 除一般 h−1 参数提升外，§3.5 已有特征二高度二具体椭圆族 Y²+tXY+Y=X³；不能只扣抽象模空间。未核其高次 formal-group OCR 系数，不据之建立原 qPI 模型同构。 |
| [Deligne–Illusie 1987 原 PDF](https://publications.ias.edu/sites/default/files/Number57.pdf)，Invent. Math.89,247–270 | §§1.1–1.6、Theorem1.2、Theorem2.1(a)–(d) 证明、Remarks2.2(i)–(iii)，约 pp249–254，及前言有关局部构造段 | 除 p 的局部 Frobenius 微分、提升差的同伦及 Čech 粘合是经典机制。PDF 为文字抽取阅读；图式没有另作可见图像验收，未通读 §3 全证明。 |

LT 曾请求相关页截图，但本席输出中没有形成可据以核读公式的可见图像，
故没有将该请求算成视觉复核。所用结论限于上述可辨认正文。
本表四源不是“全部文献亲读”；Vlasenko 的定理陈述阅读也不冒称全证明复审。

### 5.2 从共同报告继承的来源及实际剩余

| 来源组 | 必须扣除 | 当前原对象还需做什么；本席证据边界 |
|---|---|---|
| JR 出版版、Joshi–Lobb、Ohyama、GRT11 | JR 原积分/谱式；JL 八点初值空间与 Picard；根单位具体 qPI 先例 | Src-JR 的出版授权网页全文子缺口已关闭，不能重写成仍完全未读；但这是继承而非本席出版全文亲读。Ohyama/GRT11 真实全文及引文图仍 OPEN，讲义或首面索引不替代全文。 |
| GHK、Friedman、Cantat–Dolgachev、Carstea–Takenawa、Halphen 背景 | 反典范边界、法丛周期/index、pencil 及根单位椭圆化机制 | 原八中心的单位帧、原 J 的实际极除子/完整 pencil 与所有允许特征仍需核对。继承 V-B、I-B/CD、Old-AB/CD，不称本席通读这些原文。 |
| Beauville、IVY 循环谱-Picard | 谱线丛、循环不变 Picard、商 Jacobian 及拉回核的一般框架 | 实际原矩阵有理逆、不可分次数、固定差、任意 tame m 与原域 torsor 的识别有实质剩余；不是新的一般谱对应。原文阅读身份继承 Old-AB/CD、Jspec 的具名来源范围。 |
| Vlasenko、Mellit–Vlasenko、Dwork crystals I/讲义、higher Hasse | 标量 H^σ、Frobenius 数字规则、非ordinary形式群整性；普通可逆分支的更高导数/同余不应隐去 | 原 α 的两个系数、块内与时间 jet 以及非普通层的指定一形式比较未由所列现成定理直接给出。除上一表 v3 外，本席依 V-B/CD、I-srcD 继承。 |
| Deligne–Illusie、Shimada、Dupuy–Zureick-Brown、四作者 total p-differentials、Buium/Hurlburt 线索 | 提升障碍、连接/扩张、局部差商、除 p 微分与 cup product 已有；分歧 π 形式模型也有先例 | 目标 whole Frobenius 障碍与本题 L_m 中固定 J 的障碍不是未经比较的同一对象。DB/prime/OC 明确给同一 κ_J 和原首切向类。除上一表 DI 指定段外均继承 V-srcOC/V-CD；Buium/Hurlburt 具体公式未穷尽。 |
| Fonseca、Movasati、Katz；Achter–Howe 订正版、Cartier 背景 | 辛/Hodge 补基、Cartier 商满射、非共零线性代数、标准 Hasse 运算 | 任选补基存在不证明原 χ/ν 的身份。当前 TH 用实际障碍路线，不能把旧 m=1 配对常数改作全 m 证明。继承 V-srcH 和 V-CD 的实际范围及订正。 |
| Koroteev–Smirnov、Bai–Lee、Wagner q-Witt/q-Hodge/Habiro | 根单位差分乘积、首非零分歧层、曲率/Adams、对角 q 差分和完成/分级结构 | 这些不是原秩二状态余切模及其双系数理想的已给同构。谱相等不等于完整 jet 相等。继承 V-srcH/V-B/CD；未自行核后文图式，不将未读部分排除。 |
| Lubin–Tate、Ditters、Henrio、Saïdi | 非ordinary提升、具体二进椭圆族、有限 torsor/Hurwitz different 的背景 | 未建立原 I 的状态 pencil 是其有限 torsor，也没有已给原混合系数身份。数字五可在单项式商出现，T 可正规化；二者不独立加分。LT 亲读范围如上，其余继承且 Ditters 全文仍未补齐。 |
| P18、P29、P11 及 Portfolio 其他作品 | P18 局部微分/Fitting；P29 差分/数字选取；P11 在既有群结构后的完整循环公式为直接包含，不只是“类似” | V-PF 的实读范围内没有给本次指定 κ_J—原迹—全 U 首 jet 身份；本席没有打开这些旧论文，不能称独立完成全 Portfolio 排除。P11 消费者不进入当前科学贡献。 |
| 其他近邻：Rezchikov、Wu、Bouis–Gazda、Alonso–Suris–Wei、FHHO、Schuler、Urbanik–Yang 等 | 按 V-B/CD 与 I-B/CD 所列已读定理扣除同调曲率、ordinary分支、整曲线/调节器等相关机制 | 继承来源层级，不把标题或仅陈述阅读当成完整排除。没有已给跨系统模同构；跨族可能联系只为 ROUND2_CLUE。 |

标准 Bockstein、Čech、Taylor、Cayley–Hamilton、Fitting、局部消元、
最小模型唯一性及光滑点提升全部按工具处理。
“没有直接包含”只区分现成定理能否免去指定证明，不是全球首创证书。

新 Phase B 的十五条查询、Scholar/S2 六次精确入口失败、近期窗口及 OCR/图式缺口
均按 V-B/CD 继承；本席未重做这些数据库任务。
Ohyama/GRT11、Ditters、GHK 全文与未穷尽前向引文等不确定性没有被四源定向复读消除。
仍为有界查新判断，不声明截至某日全球不存在同结果。

## 6. 新意门：7.6/10，PASS，余量小

本席评价完整对象，而不是仅给新增三个公式打分。
原实际 Jacobian 和完整闭 Hasse 识别保留为当前科学内容；
本地旧接受不是公开先例，也不因耗费证明篇幅而另计贡献。
另一方面原矩阵/谱式已有，Halphen/谱-Picard/最小模型均强烈压低方法新意。

本席将最重要的准确剩余放在 V1：
同一原圆分厚化中，八环斜率固定的非零 κ_J
被原矩阵迹的 pπ 同余送到原 α 的首切向系数，
从而在每条完整光滑超奇异层的每一点得到原完整两方向理想。
一般障碍/Cartier理论说明这种路线如何工作，
但没有自动选出这个 J、这个厚化、这个原整数迹或这个 ν。
指定身份和对所有原点的理想结论，比任选非零类或在谱模型上做一次 Hasse 计算更强。

V2 的 H^σ 本身不新；真正剩余是任意 tame 块中全部内部非共振/时间变形
和外部谱缩放在同一形式层面的运输。
V3 也不以“特征二高度二存在”“五”或“单位 T”为贡献，
而在于同一原 α 的基准变为四块、其两个系数带原底参数的混合关系，
并通过同一首层 ν 落实到完整原模型。
这些高层结果是 V1 同一问题的结构性延伸，不按公式数另加三次分数。

因此我的判断是：一般方法仍主要 LOW，
但扣除后保留了一个有具体识别内容、可检验且统一的“实际障碍控制垂直临界首层”发现，
并有完整原模型和不同特征高层行为作为非平凡验证。
已读先例尚不能将这一整套结果缩成一个已给命题的直接代入。
这足以以小余量越过本席 7.5 的门；不要求每篇论文另创通用理论才可通过。

最强反对意见仍成立：一旦实际几何、trace congruence 和非零边界类给定，
末段主要是标准长正合列、Cartier、Cayley–Hamilton/数字支持和局部消元；
原族外的统一适用定理、全厚度及更高非普通整结构没有得到。
所以我不评为高幅度方法突破，也不把没有取得某篇先例当成加分理由。

V-CD 的 7.2/PROCEED_WITH_CAUTION、method LOW/finding MEDIUM、
I-FAIL 的旧整数两票 7.3 FAIL、Old-FAIL1/2 的失败及分歧保持原样。
本席 7.6 不是改写这些意见或认为其“错误”，
而是在本人完整证据上，对上述指定关系与原几何身份的发现幅度给出较高权重。
没有用 DB/SH 两处短证明复用加新意，没有用数学已接受或工作量提分，
也没有按“补足 0.1/0.3”设计评分。未校准不允许自动进位或乐观外推。

## 7. 独立科学价值门：8.3/10，PASS

这是一个完整且可独立使用的问题：
原离散可积积分在圆分退化后其状态微分何时失去首项，
两方向共同零理想是什么，超奇异性如何通过实际提升障碍进入下一层，
以及不同素数/高度何以产生不同基准和状态阶。
答案不只给若干孤立计算，而是连接原状态空间、完整闭曲线几何和实际整数矩阵。

主要价值有三点：

1. 明确区分 mod p 的 Hasse 零和原双系数理想，
   解释普通/超奇异状态的准确首层阶，避免把零微分简单理解为更高整除。
2. 保留原单位时间、任意 tame m、完整末端线与所有光滑能级，
   并通过实际 Jacobian/闭模型证明“超奇异”确为原动力纤维性质。
3. 给可直接引用的高层截断理想及特征二反常基准，
   同时精确保留尚未求出的全厚度和准确高层阶边界。

上述仍是特定 qPI 族的精细定理，而非所有 q-difference 系统的新一般原理。
没有提供奇异能级的同样理想、任意额外分歧状态阶或新的有限域周期统计；
这些未做事项限制适用面，但不使当前完整问题变成零碎附录。
不因三块数量、篇幅需求、批次目标或潜在发表收益评分。
V1、V2、V3 相互服务于同一问题，适合一个自足数学叙述，而非三篇拼接。

## 8. 自然正文容量门：PASS，超 30 风险较明显

固定版式：匿名英文、单栏 11pt、letter、四边 1 inch、标准行距；
本题全部必要证明在正文，参考文献另计。
没有试写、试排或编译。下列为逻辑内容的低/中/高预测，
不是实测、统计区间、严格上下界或以后 PDF 验收保证。
没有用文件行数、件数、工作量、旧票页数或源码换算作估计。

| 必要正文块 | 必须实际写出的内容 | 低 | 中 | 高 |
|---|---|---:|---:|---:|
| 1. 问题、原规范、定理及边界 | 原矩阵/模型定义，完整 V1–V3，允许基变换、状态阶口径与先例定位 | 1.75 | 2.25 | 2.75 |
| 2. 原几何与边界供应 | 八中心/四末端图，极除子与法丛单位帧，真实常数/节点计算，完整 pencil、Stein 与小特征泛光滑 | 4.00 | 4.75 | 5.75 |
| 3. 纯 W0 与实际泛 Jacobian | W0 有限临界代数；谱两图/端点/有限推下；实际谱模族、原状态有理逆、固定差、无核和原域 torsor 下降 | 5.00 | 6.00 | 7.00 |
| 4. 完整闭层 Hasse | 已光滑层的几何整性；同能级 henselian 提升、双向最小模型延伸；完整谱微分及 Cartier 运输 | 2.00 | 2.50 | 3.00 |
| 5. 整数除法与原 α 正则 | 整数循环插入、除 p^a 规范、零阶迹递推，以及原 U 全图/余维一延拓 | 1.50 | 2.00 | 2.50 |
| 6. 首层实际障碍与完整理想 | DB 连接及限制、原 prime trace pπ 同余、Taylor/特征四、OC 指定类、两方向理想 | 4.00 | 5.00 | 6.00 |
| 7. 奇 p 全块首 jet | 通用带权矩阵接口；内部非共振及时间项、外部支持和数字选择；共同商与全图分解 | 2.50 | 3.25 | 4.00 |
| 8. 特征二基准与实际混合理想 | 独立 char2 交换子/数字选择；特征四切向比较；逐点 J² 整除、混合理想和截断商 | 3.00 | 3.75 | 4.50 |
| 9. 状态推论及范围收束 | 原理想的状态像、准确阶/下界、不能推广的范围 | 0.75 | 1.00 | 1.25 |
| 合计 | 所有必要块均在正文 | **24.50** | **30.50** | **36.75** |

PASS 的含义是可信存在自然 22–30 页的完整写法，
不是要求中预测必须落窗；本席没有增设这一规则。
具体的可读组织是：原图/节点帧只写一次，通用迹插入/交换子也只写一次，
分别在首层和两种高层引用；把闭 Hasse 作为一个有完整实际前提的命题。
第 2–8 块分别采用约 4.25、5.50、2.25、1.75、4.50、3.00、3.50 页，
加引入约 2 页、结尾约 1 页，总计约 27.75 页，
在本席看来仍允许完整证明而不需要删量词、压缩版式或将必要证明移附录。
该数字同样只是有内容支撑的组织预测，不是写稿后测得。

实际泛 Jacobian 的谱模族/有理逆/无核/下降通常需要约五至七页，
不能压成“应用 Beauville”一句；W0 四次有限代数也必须给出。
闭层的 henselian 同能级比较和完整 Cartier 微分核查另占真实空间。
这些是上端风险的主要来源，其后还有整数 prime trace 的符号与特征二两次整除。
若为可读性分别展开所有标准接口、重复每个原图或增加独立示例，
自然超过 30 页相当可能；36.75 并非严格最大值。
因此容量通过不应被转录成“轻松可放下”或未来 PDF 预先通过。

低于 22 页的风险也不是逻辑上不可能：极简英文、很少重复定理和高度熟悉标准工具的读者
可能使实际表达短于低预测。但完整谱族/原域、四末端与实际障碍链本身
有足够独立实质，不需要为达到下限增加例子或灌水。
本席认为下端风险小于上端风险；若以后真实自然正文不足 22 页，仍须按原合同处理，
不能以本预测豁免，也不能补冗余文字造页数。

不双计的是有明确替代证明的 DB/SH 重复供应与已不消费的历史出口：
Ssplit、Ffib 全奇异分类、旧大阶扭子长度、回返/全周期和旧 m=1 配对路线。
这不是删去当前问题的必要责任；其余完整证明均已在表中有位置。
本报告不授权开始试排、拆篇、缩版或改动容量锁。

## 9. 本席结论、限制与终态

本席四门为：新意 7.6 PASS、独立价值 8.3 PASS、
完整证明信心 9.2 PASS、自然完整正文容量 PASS；自身合取 PASS。
这是本次同一完整 V1–V3 的首次正式 R1 票，不更改旧整数或 T1–T7 的失败。

没有新硬数学缺口，因此没有需要作者为本席补证的强制返修项；
来源未穷尽、评分未校准、同模型错误相关以及未来文字转录风险仍在。
任何更强公开先例可能改变将来的知识判断；
这不表示允许对当前同一对象反复调整分数或重抽本席。

最重要的边界仍是：高层仅首 jet/截断理想；
五仅为规定截断横向长度；高层“至少二”不能写成准确二；
几何选点/同构不任意下降；原四末端线、实际 Jacobian 与闭 Hasse 不可省略。
这些限制已经计入本席价值、证明与容量判断，而非通过之后追加的新条件。

本报告完成后全文读回并交付最终行数与 SHA-256，作为单次终态提交停止修改。
未知另一席结果，不代作双份合取、准入、论文/PDF 完成或 Batch07 状态管理。
没有论文项目、锁、稿件、PDF、GPU、投稿、上传、托管、push、外发消息或付费操作。
