# P31 · Stage 4.5 Round4 · Recovery3 最终完整性报告

本轮审查产物的来源—定位交接已完成；论文完整性结论仍为 **FAIL**，总体合规决定为 **BLOCK**。这是同一次 Round4 审查的局部修复，不是新的全篇重审，也不授权改稿、科学执行或进入 Stage5／6。

当前稿为 `stage4_prime_revision_round6.tex`，SHA-256 `4bc1a960b5527a5d389b5c70e29fa0dc7b3199b93a808dd3f347616dd686d1a3`。

## 本次修复

7个来源的28行原先使用了重新取得来源的定位，未严格对应 E1 registry 保留的稿内 writer locator。现以新版本恢复忠实对应，不改原 registry、覆盖报告或稿件。

- S05、S06、S08、S09、S16、S17：从原 INPUT_LOCK 已保留的真实 Crossref 摘要中明确提取 held text，记录去标签／实体解码／空白处理及前后内容哈希。
- S19：只持有历史 source-finalization carrier 留下的75 UTF-8 bytes原文短摘录。JSON carrier 的哈希不冒充PDF响应哈希；原“PDF page 1”只作为历史记录中的定位保留，**未独立认证该页码或全文抽取**。既有普通浏览器所见印刷页182文本另列为措辞佐证，不偷偷替换原定位。
- 28项声明分别核对历史定位记录、限定摘录用途、登记角色、scope／禁止转用的边界。历史／项目登记事实与外部原文支持分开说明，不把短摘录提升为完整数学角色、项目定理、实现或执行证明。
- 官方 builder 仅重建28行，另375行对象及row hash原样保留；401项声明及语义判定均不变。375个未变证据行对应373个未变声明决定，二者不混计。

详见 [来源血缘及限制](stage4_5_round4_recovery3_source_provenance.json)、[限定语义依据](stage4_5_round4_recovery3_semantic_claim_review.json) 与 [完整Schema5报告](stage4_5_round4_recovery3_integrity_report_root.json)。

## 当前结果与复用边界

| 检查面 | 范围 | 结果与限制 |
|---|---|---|
| A 参考文献 | 24项 | 作品身份24项确立；S03、S22两个DOI字段仍缺严格一手绑定，不是作品不存在或已证伪 |
| B 引用用途 | 26处 | 26个有限用途已核对；本次明确七组来源持有层级，不增添全文或定理认证 |
| C 数据／执行对应 | 168项量化单位 | 167项受限核实；44−9=35−13=22聚合算术不证明原捕获、去重及筛选执行；后来的20查询、18保留／2排除记录是另一观察 |
| D 原创性 | 既有33/63正文块及全部38个修订内容块的审查 | 复用已完成的限定检索，无本次新增检索、相似度检测或完整作者语料清查 |
| E 声明 | 401项／403行 | 396 VERIFIED、3 UNVERIFIABLE、2 UNVERIFIABLE_ACCESS；VERIFIED限于实际记录、来源用途和保留条件的论证 |
| E1 | 原registry与当前稿 | 复用有效官方覆盖记录；原1个TeX注释词法候选及非声明解释保留，未改成0；语义提取完整性不可机器认证 |
| E4／E5 | 原已完成的限定范围／新颖性审查 | 复用；无新Route评价、科学可行性或全球优先权认证 |
| E6 | 六轮57项操作 | 复用完整语义审查和当前绑定；1项历史any→every漂移在R6已恢复，但历史发现不删除，新发现集处置未由“继续”替代 |

本次实际执行及精确输入绑定见仓库根目录的 `BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_VALIDATION.json`。新403行整份来源重放与本地严格有序tuple／跨字段检查分开记录；后者不是官方完整Schema5验证器。未变的覆盖、修订包、Schema12及其余四篇正式检查直接复用，不声称重新执行。

## 未决项

| ID | 严重度 | 未决事项 |
|---|---|---|
| IL-SERIOUS-1 | SERIOUS | B0003机构、地址及联系元数据的复合作者事实待原作者确认 |
| IL-SERIOUS-2 | SERIOUS | B0102无资金声明待原作者确认 |
| IL-SERIOUS-3 | SERIOUS | B0103无利益冲突声明待原作者确认 |
| IL-MEDIUM-1 | MEDIUM | S03 DOI字段缺严格一手验证 |
| IL-MEDIUM-2 | MEDIUM | S22 DOI字段缺严格一手验证 |
| IL-MEDIUM-3 | MEDIUM | B0036／B0041原筛选执行的事件级证据缺口；C／E表现不重复计数 |

S19持有层级限制随证据显示，不被静默提升为页码验证；当前正文说的是历史记录及有限使用，不因本次诚实重绑定制造新的科学正结论。

七种失败模式中，Mode2与Mode6为 INSUFFICIENT EVIDENCE，其他五种在既定限定范围内为 CLEAR。Mode2属于警告层级；Mode6独立阻断。没有将证据不可得认定为数据或作品造假。

[当前Schema12合规报告](stage4_5_round4_recovery2_compliance_report_root.json)原样复用：非SR `primary_research`／RAISE `principles_only`；人工监督、透明度、可复现性、适用性四原则均为 fail。RAISE贡献依规则封顶warn，但独立完整性及Mode6使总体block。这是原则延伸评估，不是官方RAISE认证。

## 保全与检查点

旧差异、旧失败产物、未授权API事件及隔离记录全部保留；未追认或使用被隔离的衍生结论。本次使用六个历史摘要及一个历史短片段的范围均来自原INPUT_LOCK允许的carrier，既有普通浏览资料仅作明确分层的补充。

稿件、书目、矩阵、human-read记录及科学目录未修改。作者事实、E6明确处置、出版权限和Stage5／6均未获得新授权。ARS要求保留未决事项并停留在当前完整性检查点；本轮交接完成不等于论文PASS或流程放行。

