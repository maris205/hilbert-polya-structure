# Round10 · Stage 4.5 Round4 · Recovery3 最终交接

**五篇的本轮审查产物和最终交接检查现已完成；五篇论文完整性均为 FAIL，总体仍为 BLOCK。** P31的28行来源—定位交接问题已在明确授权下用新版本解决。其余四篇复用已完成、输入未变的报告及验证，没有重启审查。

## 当前结果

| 论文／当前稿 | 主张／受限 VERIFIED | 证据行 | 普通问题组（严重／中等／轻微） | 主要未决项 |
|---|---:|---:|---:|---|
| [P29 R6](papers/29-bianchi-ideal-owner-refinement/notes/stage4_5_round4_recovery2_final_integrity_report_root.md) | 375／372 | 375 | 3／1／0 | 3项作者事实；两段接近来源措辞合为1项 |
| [P30 R5](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round4_recovery2_final_integrity_report_root.md) | 441／435 | 441 | 5／0／1 | 5项作者事实；S13摘要句号定位；既有reader例外未被清除 |
| [P31 R6](papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round4_recovery3_final_integrity_report_root.md) | 401／396 | 403 | 3／3／0 | 3项作者事实；原筛选执行记录；2个DOI字段缺口 |
| [P32 R6](papers/32-homology-cover-renormalization-uniformity/notes/stage4_5_round4_recovery2_final_integrity_report_root.md) | 438／433 | 476 | 3／5／1 | 3项作者事实；5个DOI字段缺口；两处历史矩阵“当前”称谓合为1项 |
| [P33 R4](papers/33-bolza-control-matched-census/notes/stage4_5_round4_recovery2_final_integrity_report_root.md) | 459／452 | 464 | 4／1／1 | 4项作者事实；S02六字段合为1项一手访问缺口；fixture终态措辞 |
| 合计 | 2,114／2,088 | 2,159 | 18／10／3 | 20个UNVERIFIABLE语义单位分为18组作者事项；另2个访问受限单位及4个轻微失真单位 |

VERIFIED限于实际来源／本地记录忠实性、声明用途和保留条件的论证，不是全部来源全文、数学定理、研究可行性、个人身份、语义提取完整性或出版许可认证。问题组与语义单位不混计；RAISE原则和历史E6另列，不重复累加成普通文本问题。

## P31局部修复和限制

只重建7组×4项的28行官方 evidence rows，原样保留另外375行对象及row hash、373个不受影响的语义决定；401项声明的判定全未改变。E1 registry、稿内writer locator、原覆盖报告和稿件均未修改。

六组来源从原INPUT_LOCK中真实保留的Crossref摘要显式提取文本并记录原始／转换后哈希。S19只有历史载体保留的75-byte短摘录；**未声称旧PDF全文、页面抽取或page 1映射已验证**。既有普通浏览器所见印刷页182文字仅单列为措辞佐证；S09仍是同一旧摘要，不称为独立网页来源。

每组的历史定位记录、有限摘录用途、登记角色、项目范围和禁止转用边界分开核对。官方builder及来源重放只验证摘录的字节来源，不认证页码、角色全义或科学结论。[原暂停记录](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY2_P31_HANDOFF_STOP.json)保留，当前对应关系解决见[新验证记录](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_VALIDATION.json)。

## 实际验证与复用

- 本次首次且仅一次调用官方builder重建28行。完整P31报告403行官方来源重放PASS。
- P31本地跨字段检查PASS：严格有序selected tuples、原稿跨度、完整数组、distinct claim计数、覆盖绑定、修订包／E6当前绑定、正式E6 schema及非SR决定聚合。这不是官方完整Schema5验证器，也不提供科学或作者认证。
- 其余四篇的1,756行正式重放及跨字段检查直接复用；五份当前Schema12的有效结构检查直接复用。未变的P31覆盖及修订包验证也未重跑。
- P31原1个注释词法候选、P32原4个词法候选及既有逐项语义解释均保留，未为获得clean输出改成0。
- 独立只读提取回放核对了七份源文本的carrier→JSON字段→明确转换→held text关系，以及既有补充文本。这是来源血缘检查，不是独立科学证明。探针中的语法／字段形状错误如实留在来源说明，没有覆盖旧产物。

完整命令、实际返回、时间和输入哈希见[本次验证记录](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_VALIDATION.json)与[28行构建执行记录](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_P31_BUILD_EXECUTION.json)。全部当前报告入口见[五篇输入索引](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_REPORT_INPUTS.json)。旧四篇的详细检查仍以其原Recovery2收据为准，不冒称本次重做。

## 作者事实、E6与合规检查点

[18组作者事项](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_AUTHOR_PENDING.json)均未得到原作者的具体事实确认；本次只把P31的报告绑定状态从候选暂停更新为已检查，未替代资金、利益冲突、机构／联系方式或贡献事实确认。

E6完整修订链审查已完成：P29一项、P30两项、P31一项、P32一项，共5项历史漂移；当前文字已恢复或收窄，P33未检出。本轮不重复要求恢复已经恢复的文字，但旧处置不能自动绑定新发现集，新发现集的明确作者处置仍待提供。

RAISE遵守当前非SR原则延伸规则：贡献封顶WARN不代表总体可过；独立完整性／失败模式使总体BLOCK。缺少监督、提示词／参数、可复现记录或验证等事实未被推定补足，不声称官方RAISE认证。

## 保全及下一步边界

本次最终保全比较Recovery3冻结的1,301个文件和15棵科学目录树；精确结果见[保全记录](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_PRESERVATION.json)。该记录自身不纳入自身哈希，以免循环绑定。

全部旧来源、旧版本、差异、失败尝试和未授权API隔离记录保留；没有追认或使用隔离衍生结论。未修改稿件、书目、矩阵、human-read记录、科学文件、canonical状态或远程内容；没有新增网络访问、科学实验、论文构建或Route评估。

**按ARS完整性检查点要求，停留在当前阶段。** 本轮是Round4审查内的第三次限定产物恢复，不是第五轮审查；本轮产物完成不构成Stage4.5的PASS／例外放行，也不授权Stage5／6。下一步需对所列作者事实、证据／措辞问题和新E6发现集提供具体处置；笼统“继续”不视作事实证明或例外批准。

