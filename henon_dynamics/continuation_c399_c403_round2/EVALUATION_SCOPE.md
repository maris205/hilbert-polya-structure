# C399–C403 Route A 评估范围与来源路由

日期：2026-09-05。五份 [evaluation](evaluations/route_a/) 使用同一
[冻结计划](BATCH_PLAN.md) 与基线 `1667dfc0c24e10a8a3627e80f93e301538d18012`。
基线提交不含本轮新文件；本轮最终 manifest 才绑定新证明/评估字节。
本文件不是论文完成或发布收据。

## 固定权限和判定范围

协调者已完整读取 `flow_systems/skills/route-a-evaluator.md` v0.2.0；实际
SHA-256 为 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。
其完整输出 schema 保留；JSON 语法的 `.yaml` 是合法 YAML，不另造评估器。
源码证明的 `PROVED` 不自动变成目标 A1/A2/A3；目标不可检验值不是零误差。

| 候选 | 严格 tuple `(A0,A1,A2,A3,A4)` | 总体判断 |
|---|---|---|
| C399 | FAIL, WEAK, FAIL, FAIL, FORMAL_HINT | ROUTE_A_REJECTED |
| C400 | FAIL, FAIL, FAIL, FAIL, NATURAL_QUANTIZATION | ROUTE_A_REJECTED |
| C401 | WEAK_ARITHMETIC_RELATION, WEAK, FAIL, FAIL, FAIL | ROUTE_A_EXPLORATORY，仅本征有限特征源机制 |
| C402 | FAIL, WEAK, FAIL, FAIL, FAIL | ROUTE_A_REJECTED |
| C403 | WEAK_ARITHMETIC_RELATION, FAIL, FAIL, FAIL, FORMAL_HINT | ROUTE_A_EXPLORATORY，仅本征整除算术算子 |

完整带层级前缀的合法枚举见逐候选文件；本表缩写只为可读性。
EXPLORATORY 不是 primary HP candidate，也不是目标 A2 通过。
C400 自然量子化限于已有源 δ 相互作用算子；不赋予 Route B 权限。

## 实际参考路径和阅读范围

遵照 evaluator §7，按 README → papers → obstruction → candidate 的路径
读取；相对路径在 `flow_systems/` 下解析，而非误用 Hénon 的 v0.1 文件。
`flow_systems/docs/prior_work/README.md` 全文、48 行 obstruction registry
和 34 行 candidate registry 全文均已阅读；跨流文件只读，没有改写。
六份提供的 PDF 均实际作 `pdftotext` 定向阅读，而不只读 README 转述：

| PDF 序号 | 实际读取的物理页 | 此批提取的边界；不是重审其全部定理 |
|---|---|---|
| 1 | 1–3 | 源文将动力学筛同构标作猜想，数值现象不能转为本批算术定理。 |
| 2 | 1–3 | 有限阶段 MSS 反例与显式假设须保留；一维线索不能越过已知拓扑障碍。 |
| 3 | 1–3 | 正文 Theorem 1.2 依赖 uniform inducing，a.e. Corollary 1.3 需 β>1；不借摘要的较宽措辞作新证明。 |
| 4 | 1–4 | 原文明确按首零点锚定基线及 DE 参数优化，不能把这种目标拟合当本征算术来源。 |
| 5 | 1–3 | 源稿区分数值/heuristic 与证明，area preservation 或双 solver 不证明目标零点同一性。 |
| 6 | 1–5 | 读取其同一 Weil compression 两侧/trace-moment 的提议和限制，作为 evaluator 指定比较框架；不在本批独立认证其所宣称的 2/3 常数或完整证明。 |

本批五篇主定理均不依赖上述六份稿件中的新研究结论。指定来源的存在、
文字内容和读取范围，与独立验证其数学真伪不同；尤其不把仓库 README
或模型作者声明本身当作外部权威。没有在本批新增任何“2/3 已证明”的主张。
具体 PDF 路径为 `flow_systems/docs/prior_work/papers/` 下编号 1–6 的原文件。

| 序号 | SHA-256 |
|---|---|
| 1 | `78a65db26110ef8173c3d7dc50caf2b598e59b854e7b5afa3983891008cb953e` |
| 2 | `05044a54a6bde0bbd71dc7c7c6deb305638803afe36f8fe2d4167b88c5ad898d` |
| 3 | `6ad40b40e81a22266c1ca5baa34b5692e4e0b4dbc7f4764b57db190193731f9b` |
| 4 | `030c072bcec069ef1c3d87b84025ed830e40591970461e5195b2991adaedb0e3` |
| 5 | `23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9` |
| 6 | `6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72f` |

Hénon 侧定向阅读 `docs/candidate_registry.md`、`docs/obstruction_registry.md`
的相关源/目标及算子所有权边界，特别是 C380、C384、C393、C398；另有
C108 与 time-ordered 包的实际字面源码/定理检查，见来源审查及
[新 C108 缺陷记录](nonlinear_return/BUG_FINDING_C108.md)。旧冻结文件不改。
没有声称为本批通读所有历史论文。

## 对照门槛：显式未完成，不改规则

各源定理自带的全参数/母系统比较已经实际数学核对，逐候选记录了具体
对象及结果。它们最多覆盖“neighboring parameters”和“simpler parent”
两种 evaluator 列举的算术对照类别。同一类别的多个例子不拆成多个类别。
因此每篇的三类 A0 强制对照门槛均为 **INCOMPLETE**。

洗牌素数、密度匹配整数、合数/pseudoprime、随机算术标签及随机周期/
相位等没有运行；Davenport–Heilbronn、Epstein、planted-zero 数值对照也
没有运行。此处不为纯源理论造实验，不给这些未做项补 PASS。
所有目标 train/validation/sealed-test 数据集为空、无拟合；零点误差、
多余/缺失零数、argument-principle discrepancy、cutoff/precision drift
和 control margin 均标为 NOT_TESTABLE，而非记为零。

本轮确实执行的 proves-too-much 检查是解析层的适用范围比较：同一源
论证对非目标参数/母系统仍成立，故仅凭稳定性乘积、有限矩阵、正谱或
平均计数就推出 RH/目标匹配，会误认证这些无目标来源的对象。五篇均
拒绝这条推理，登记 `STOP_SCOPED`；这不是已完成数值敌对面板的同义词。

## 不能借用的对象

- C399：圆周算子的 Fredholm determinant 不等于在普通 Lp 中删除零测
  周期点后新获的物理算子；有限实乘积的补偿极限有自己的定义。
- C400：Dirichlet endpoint 的 `ζ(2s)^2` 不属于有限 κ 算子；本轮只有
  O(log k) 余项，不能套用 C398 的 bounded-residual 排除论证。
- C401：固定 n/Frobenius 变动切片、真正对角映射及 étale cohomological
  determinant 的时钟与边界项不同，不能拼接成一个目标对象。
- C402：带负号全局留数得到 `1/det(I−zW)`，不是普通物理转移算子的
  Fredholm determinant；退化留数不等于简单点分母式的字面替换。
- C403：经典 LCM 谱定律和整除矩阵极限不是动力学周期或目标零点。

所有九项目标/Route-B scope flags 均为 false，保持
`NO_BAD_EULER_OR_ROOT_NUMBER`。更新注册表仅记录新增源结论与当前缺口，
不改历史 verdict，也不将数学内部审查描述为同行评审。
