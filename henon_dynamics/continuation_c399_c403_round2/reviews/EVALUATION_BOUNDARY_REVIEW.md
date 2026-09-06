# C399–C403 评价边界跨产物一致性审计

日期：2026-09-05。结论：**在指定的六个冻结产物之间未发现科学边界或状态矛盾；没有发现将源码证明完成提升为目标 A2/A3、Euler 因子、根数或 Hilbert–Pólya 结论的情形。**

本报告只核对 `EVALUATION_SCOPE.md` 与五份 `evaluations/route_a/HCS-C399..403/2026-09-05.yaml` 的跨产物一致性，不重新评定候选，不修改原 tuple、等级或 overall verdict，也不将“彼此一致”解释成评价内容已经由本审计独立重新证明。本次没有重读完整 evaluator、重做主证明/文献审查、运行数学或编译；沿用任务指定的冻结评价语义。采用 research-review 的只读、证据定位和范围诚实原则，不声称执行新的完整 ARS 流程、外部评审或人类审查。

## 输入范围与哈希绑定

实际完整读取：范围说明 97 行，五份评价各 174 行，共 967 行。五份 `.yaml` 的 JSON 内容均可实际解析；其 JSON/YAML 双重语法身份不是新建评价器的依据。

| 输入，路径相对于本批目录 | SHA256 |
| --- | --- |
| `EVALUATION_SCOPE.md` | `fb19707f640a00f1bd52105652f269be03d5d99c6477c94386ec64ee954d4e4c` |
| `evaluations/route_a/HCS-C399/2026-09-05.yaml` | `0bf8cc26331d801cc9c556e7951f9dcd6e432e61d22f425b3aac4c61a9f74e67` |
| `evaluations/route_a/HCS-C400/2026-09-05.yaml` | `762349e0834d1f48aaa7630a7c3ac4a4bb4f68fc878996a3246e01f29046be4d` |
| `evaluations/route_a/HCS-C401/2026-09-05.yaml` | `8ac4671bbc215370abf9e25e264295a282d3b925cc7e4fcc8e5983638a94a7b2` |
| `evaluations/route_a/HCS-C402/2026-09-05.yaml` | `53ed3cf4110b9f549eb5c93dd914a809326ace8d4231772381f7fd704a226d4b` |
| `evaluations/route_a/HCS-C403/2026-09-05.yaml` | `b988a439ad6e16917452c9df17c60baa34f45107ba41b6e3f5116d8dd8617902` |

所有记录使用相同 evaluator 版本 `0.2.0`、evaluator 哈希 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` 和 Git 基线 `1667dfc0c24e10a8a3627e80f93e301538d18012`，与范围说明第 4、10–12 行一致。评价第 7、23 行明确该提交只是本批之前的基线，新文件由最终 manifest 绑定；范围说明第 5 行也作相同限制。本审计核对这些标识的相互一致性，没有重新认证 evaluator 内容或最终 manifest。

## Tuple 与总体结论

下表保持评价文件中的完整枚举。各文件的 `tuple`（143–149 行）与 `a0` 至 `a4` 的各级 `verdict`（41、66、81、101、115 行）逐项相同；也与范围说明 17–21 行的缩写表一一对应。

| 候选 | 冻结 tuple `(A0,A1,A2,A3,A4)` | 冻结 overall verdict | 一致性 |
| --- | --- | --- | --- |
| C399 | `A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT` | `ROUTE_A_REJECTED` | 一致 |
| C400 | `A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` | 一致 |
| C401 | `A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL` | `ROUTE_A_EXPLORATORY` | 一致 |
| C402 | `A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL` | `ROUTE_A_REJECTED` | 一致 |
| C403 | `A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT` | `ROUTE_A_EXPLORATORY` | 一致 |

这不是本审计产生的新评价表。范围说明第 24 行明确 EXPLORATORY 不等于 primary HP candidate 或 A2 通过；五份记录的 A2/A3 均为 FAIL。C400 的源自然量子化与整体 Route A 拒绝并不矛盾：范围说明第 25 行和该评价第 117–121 行均限定为同一源算子，且否认目标谱身份和 Route B 权限。

## Source/target 分离与不能借用的对象

五份评价的 `source_lock` 对象、来源、时钟、规范化、行列式约定、cutoff 和 precision 与其顶层相应字段逐字一致。`a0`、`a1` 的 `evidence_status: PROVED`（42、67 行）描述各自源证据；并没有令目标 `a2`、`a3` 的证据状态脱离 `NOT_TESTABLE`（82、102 行）。`a3.analytic_structure` 分列源与目标，目标均保留 `OPEN; no target theorem claimed`（105–109 行）。范围说明第 13 行与每份评价第 150 行的 `claim_boundary` 明确禁止从源证明、有限检验或内部审查推成目标算术或期刊接受。

| 候选 | 范围说明位置 | 评价中的对应边界 | 核查结果 |
| --- | --- | --- | --- |
| C399 | 85–86 行 | 第 11、18、84、117–118、156、158 行：有限实域、源稳定性乘积与普通圆周/Lp 物理算子不混同 | 没有把删除零测周期点后的形式乘积当成新自然物理算子；补偿极限不变成目标行列式。 |
| C400 | 87–88 行及第 25 行 | 第 13、15、18、48、84、117–118 行：有限耦合、不同的无穷耦合端点、源谱 zeta 和 ordinary determinant 分开 | 没有借用端点 `zeta(2s)^2` 为有限耦合 Euler 数据，也没有把 `O(log k)` 余项改成 C398 的 bounded residual。 |
| C401 | 89–90 行 | 第 16、18、69、83–84、103–109、156 行：双时钟切片、真正对角迭代与上同调对象分开 | 本征有限特征不被推广为跨特征有理素数装配；没有直接乘接固定 `q` 切片生成目标对象。 |
| C402 | 91–92 行 | 第 17–18、68–69、83–84、103–104、117–118 行：负号全局留数、退化概形和有限矩阵身份分开 | `1/det(I-zW)` 没有误写为 `det(I-zW)`，也没有等同于普通物理转移 Fredholm determinant。 |
| C403 | 93 行 | 第 15–18、69、83–84、104、117–118、156 行：矩阵截断、源 LCM 谱和目标轨道/零点分开 | 正紧算子或其逆没有被称作已导出的目标 HP 量子化；截断指标不被称作动力学素轨道时钟。 |

本表核对这些已记录边界的相互一致性，不重新证明其中引用的源数学结论。范围说明第 33–47 行还将指定六份历史 PDF 的“实际读取内容”与“独立验证数学真伪”分开；它明确没有新增“2/3 已证明”的主张。五份评价没有出现相反的提升。本次不追认那些历史 PDF 的完整证明或阅读记录。

## 九项 scope flags 与 Route B 权限

每份评价 162–172 行恰有以下九项，且全部是 JSON 布尔值 `false`，不是字符串、空值或缺项。五份合计 45 个 false，与范围说明 95–97 行一致：

1. `claims_target_arithmetic_local_data`
2. `claims_target_euler_factors`
3. `claims_root_number`
4. `claims_automorphy`
5. `claims_target_divisor_or_counting_law`
6. `claims_target_functional_equation`
7. `claims_target_zero_match`
8. `claims_hilbert_polya_operator`
9. `invokes_route_b`

每份的 `route_b_invocation_allowed`（160 行）与 `a4.metrics.route_b_authority`（121 行）也均为 false，`target_lift`（120 行）均为 OPEN；`scope_literal`（161 行）均为 `NO_BAD_EULER_OR_ROOT_NUMBER`。C401/C403 的弱本征算术关系与 `claims_target_arithmetic_local_data: false` 并不冲突，因为字段明确以 target 为限定。

## NOT_TESTABLE 指标及未运行数据

范围说明 74–76 行与五份评价第 21 行都说明没有目标训练、validation 或 sealed-test 数据及拟合。每份 `a2.metrics`（85–95 行）恰有以下九个目标指标，五份合计 45 项全部明确为 `NOT_TESTABLE: no target match or target data used; not zero and not PASS`：

`zero_error_train`、`zero_error_validation`、`zero_error_test`、`extra_zero_count`、`missing_zero_count`、`root_count_discrepancy`、`cutoff_drift`、`precision_drift`、`control_margin`。

没有用数值 0、空值或 PASS 代替未检验状态。额外的 `a1.metrics.target_owner_count`（72 行）均为 NOT_TESTABLE；`a3.weil_compression`（109 行）均为 NOT_TESTABLE，并注明没有手工插入自然同一对象 Weil form。已保存源检查的数量仅出现于 cutoff/precision 或源证据说明，不充当任何目标误差或 control margin。

## INCOMPLETE controls 与 STOP_SCOPED

范围说明 66–73 行说明每篇只列至多两个强制算术对照类别，不能按同一类别中多个例子的数量凑足三类。五份评价的 `a0.arithmetic_controls.analytic_categories`（46–49 行）各有两项，其内容与 `adversarial_controls.controls_used`（128–131 行）逐字相同；`mandatory_minimum_three`（50 行）全部为 `INCOMPLETE: at most two distinct listed categories; no A0 promotion based on controls`。

各篇额外例子的身份均被保留：C399 临界补偿/共振、C400 两端点与两个迭代前导系数、C401 六点共振反例、C402 C108 代码定义纠错、C403 对数/振荡慢变例子，都没有被计成第三类强制算术对照。特别是 C400 的 free 与 Dirichlet 两个母对象仍只算一个 simpler-parent 类别。

每份第 51–57 行列出未运行的素数洗牌、密度匹配随机整数、合数、pseudoprime/sieve-matched 和随机算术标签；第 73 行保留 A1 随机周期/权重/相位/长度对照为 NOT_RUN；第 133–136 行保留 Davenport–Heilbronn、Epstein 和 planted-zero 数值面板未运行。没有据源理论伪造实验通过。

`STOP_SCOPED`（139 行）在五份记录中都由第 138、140 行限定为解析层的 source-versus-target 反证范围检查，不是已完成三类算术或数值敌对面板；与范围说明 78–81 行相符。故它不抵消 INCOMPLETE，不提升 A0，也不构成目标 A2/A3 通过。

## 复核方式、结论与后续边界

除逐文阅读外，本次只读解析并核对了 tuple/逐级 verdict、范围表/overall、九 flags、九目标指标、源/目标证据状态、重复 source-lock 字段、两处对照类别列表、Route B 权限、冻结标识及返回范围说明的相对路由。所有这些一致性关系在五份记录中均匹配。该机械检查没有重新运行 evaluator，也没有产生或改写评价等级。

发现的真实矛盾：**0**。需要协调者修正的边界项：**0**。可以继续按已有冻结评价语义汇总本批记录；本报告不授权目标结论提升。

“五篇源码证明和稿件完成”与“目标算术已建立”仍是不同命题：本批目标 A2/A3 全部 FAIL，目标数值指标 NOT_TESTABLE，强制对照 INCOMPLETE，九项目标/Route B flags 全 false。该边界不会因 PDF 构建、内部数学审查、发布索引或 Git 提交完成而改变。除本报告外，没有修改评价、索引、CURRENT、旧稿或任何作者文件。
