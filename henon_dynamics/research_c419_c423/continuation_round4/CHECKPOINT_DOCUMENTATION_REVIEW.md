# 第四轮检查点：文档与静态代码审查

日期：2026-09-08 UTC。当前状态：`PASS_DOCUMENTATION_STATIC_ONLY; D1_D2_CLOSED`。
本文件是本次审查唯一允许写入的路径。最终索引和 D1/D2 修正已读回；
唯一最终本地链接扫描已完成，无剩余文档问题。此状态仅适用于
下述有界文档/静态检查，不提升数学、准入或独立复现状态。

## 角色与审查边界

主审者为当前团队的算术 scout，同时也是本轮 DH1/DH2 四份原始
交付的作者。这一关系在此披露：对这四份文件，本次是再次进行
文档一致性检查，**不是另一份非作者数学审查**。DH 的数学非作者
审查另由正特征 scout 完成；LY4 的辅助数学审查另由非线性 scout
完成。本次只核对它们的范围与收据，不重新裁决证明。

另外安排了一个只读收据交叉核对者，独立手工核对四条支线的
SOURCE_AUDIT、SCOUT_REPORT 和冻结条目。它不写文件、不浏览、
不读 JSON、不运行数学程序、不检查待建全局索引。本报告主审者
已完整阅读其返回结论，并与自己的逐文件阅读比对。

这是 AI 辅助内部文档/静态检查，不是人类同行评审、来源真实性
审计、全球查新证明、独立数学复现或正式 Route-A 评价。没有
外链重抓，没有扩大参数、域、时钟、有限字母表或周期范围。

## 已实际阅读的范围

已完整读回四条支线的全部现有 Markdown 及本轮 SCOUT_PLAN：

| 目录/文件 | 现有完整阅读范围 |
|---|---|
| `dissipative_henon/` | 5 份 Markdown：冻结合同、完整短证明、来源审计、scout 报告、非作者短证明审查 |
| `rational_trace_closure/` | 4 份 Markdown：冻结尝试、证明状态、来源审计、scout 报告 |
| `wild_native_returns/` | 4 份 Markdown：冻结合同、辅助证明、来源审计、scout 报告 |
| `third_order_lyness/` | 5 份 Markdown：冻结合同、辅助证明、来源审计、scout 报告、非作者辅助审查 |
| [SCOUT_PLAN.md](SCOUT_PLAN.md) | 当前轮的授权、分工、停止与状态边界 |

共 19 份已有 Markdown。还完整阅读了
[core_falsifier.py](third_order_lyness/core_falsifier.py) 的 106 行。
JSON 只读取既有字段、记录数组长度及文件字节摘要；未逐条复算
所有 cycle、重新计数周期分布、验证反例或重建有限图。

仓库根和 Hénon 的 AGENTS 已阅读；CURRENT 的恢复前缀先用于
识别本批，不以尚在更新的中间状态作最终裁决。CURRENT 的旧批次
正文、旧轮次数学、论文源码、正式评价与封存数据不在本次审查范围。

主协调者确认最终索引完成后，还完整读回以下最终范围：

- [本轮 README](README.md) 与 [COORDINATOR_REVIEW](COORDINATOR_REVIEW.md)。
- [批次 README](../README.md) 与 [ADMISSION_DECISIONS](../ADMISSION_DECISIONS.md)。
- [CURRENT 最新批次前缀](../../CURRENT_RESEARCH_STATE.md)：从文件开头到
  C414–C418 历史批次标题之前，不将后面的封存历史纳入扫描。

连同本报告，本轮完整 Markdown 范围为 22 份；加两个批次索引和
一个 CURRENT 前缀，共 25 个文档范围。批次索引中的历史摘要仅
按明确的历史口径读回，不重新审查它们链接的旧数学材料。

## 条目、来源和准入口径

四条支线的逐条列表与各 scout 报告一致。主审者和只读收据
交叉核对者分别手工得到：

| 支线 | 列出的实际 discovery 查询 | 183-day 查询 | 冻结 screen 条目 | 作者数学执行 |
|---|---:|---:|---:|---:|
| [DH](dissipative_henon/SOURCE_AUDIT.md) | 20 | 4 | 2：DH1、DH2 | 0 |
| [RT3-R4](rational_trace_closure/SOURCE_AUDIT.md) | 14 | 2 | 1：原 RT3 合同，比较两条桥接路线 | 0 |
| [W4](wild_native_returns/SOURCE_AUDIT.md) | 16 | 2 | 3：W4-A、W4-B、W4-C | 0 |
| [LY4](third_order_lyness/SOURCE_AUDIT.md) | 13 | 1 | 1：LY4 全分类，不拆辅助引理 | 1 |
| 合计 | **63** | **9** | **7** | **1** |

LY4 另有一条 730-day 查询，不能加入近半年栏。63 是支线记录的
实际 discovery 查询条目，不是去重文献数、所有网页访问数，或
独立复查过的浏览记录总数。直接打开原文和定理查找不在此计数。
本次文档审查没有重新执行任何检索，也没有新增来源查询。

7 是筛选条目，不是 7 个新独立问题：RT3 是原合同续接，W4-A 是
PC3-A 再入口，W4-C 是机制变体，W4-A/W4-C 仅浅筛。辅助定理、
反例族、特殊素数或两个桥接路线没有单独占用新合同。
五个深筛为 DH1、DH2、RT3-R4、W4-B、LY4。最终索引中 7/5/0
分别是 screen/deep/admission 计数，不是同一计数口径的矛盾。

文档保持以下区分：

- DH1/DH2 数学短证明闭合，但实质准入仍为零；可选深定理的
  来源核查不是两项初等证明的依赖，更不构成额外合同。
- RT3 两条桥接失败不等于全有理分类被推翻，也不证明已知短曲线
  的完备性；原全量词保持不变。
- W4 辅助证书不是全部普通计数和野返回 tower；特征三的经典
  Lattès 归属与其余素数的缺口没有混算。
- LY4 辅助引理和无界反例族不等于全整数 atlas；有限字母表内
  无周期截断，不等于所有高度或所有原始周期都已分类。

四条支线均为 **0 新准入、0 新稿/PDF、0 新编号、0 新正式评价**。
本次审查不改变 M1/AS2/IR1 的既有 3/5 状态，不宣告五篇完成。

## 唯一作者数学运行与既有 JSON

[LY4 作者回执](third_order_lyness/SCOUT_REPORT.md) 记录的唯一命令为
从仓库根执行 `python3 -B .../third_order_lyness/core_falsifier.py`。
本审者没有执行该命令或导入该模块。现有 JSON 字段与回执一致：

| 既有字段/字节核对 | 实际读取结果 |
|---|---|
| 状态 | `EXACT_FINITE_ALPHABET_ONLY` |
| 输出内时间 | `2026-09-08T02:35:53.970015+00:00` |
| 输出内 Python / optimization | `3.12.3` / `0` |
| 输出内 elapsed_seconds | `0.04612024128437042` |
| alphabet | 非零整数 −8 至 8，共 16 个值 |
| states / retained_edges | 65,536 / 20,800 |
| `cycles` 数组既有记录数 | 363 |
| `core_hypothesis_counterexamples` 既有记录数 | 72 |
| `cycle_period_counts` 既有字典 | 1:16，2:120，3:14，4:120，5:1，6:84，8:8 |
| period_cutoff | `null` |
| full_height_classification_claimed | `false` |
| independent_reconstruction_claimed | `false` |

脚本 SHA-256 与 JSON 内 `script_sha256` 完全一致：
`62fdbd8aa099ce8b9d0fc8a069a086c26a30f32d18ce6c8b5493d84de9a80773`。
JSON 当前字节 SHA-256 与作者回执及 LY4 辅助审查一致：
`a4250ab11dd4f85afa3e57064bdf0298b0e7239d86b5835ef7015a922fa0bfab`。

这些是保存结果的字段/摘要一致性，不是独立实测其时间、运行环境
或数学数值。尤其 363 和 72 只是在数已有记录，未重新提取周期、
判定最小周期或验证全部 counterexamples。作者代码里的原递推、
最小周期与参数不变性检查仍是 producer-side validation；它们
不因另一个审者读了代码或 JSON 就成为 independent reconstruction。

## 实际静态代码检查

使用 Python 3.12.3、`python3 -B -`，只对 106 行源文本执行
`ast.parse` 和 `compile(tree, filename, 'exec')`，不执行编译结果。
随后以标准库只读 JSON 和摘要；没有导入目标模块、调用 `main`、
生成 pyc、写 JSON 或输出任何新的数学结果。此次返回退出码 0。

静态阅读核对了冻结范围与实现表达的一致性：

- 字母表字面值只含 −8 至 −1 和 1 至 8；四元状态枚举没有
  独立参数区间，后继离开字母表即标为退出。
- `divmod` 后以零余数判断整除，使用精确整数操作；没有
  浮点容差或把零坐标延拓进入 ordinary domain。
- 遍历有显式已访问标记，未见周期上限参数；规范化只取旋转。
- 记录前的要求使用抛出异常的 `require`，不是可被优化模式
  关闭的 `assert`；反例谓词与冻结的高度四假说一致。
- 结果路径固定在作者目录，采用独占创建模式 `"x"`；没有
  覆盖既有输出、执行网络请求、启动外部进程或写入其他目录。

以上不重新证明图算法的数学完备性，也不把内存语法编译写成
数学执行或独立有限图认证。静态编译未改变作者代码/结果字节。

## 发现及关闭记录

**D1 — CLOSED：审查行数/锚点定向修正。**
[DH 非作者短证明审查](dissipative_henon/INDEPENDENT_SHORT_PROOF_REVIEW.md)
把完整覆盖记为 `Lines 1–382`，而当前证明文件为 390 行；同一
行记录的 SHA-256 `ed5b16b86d5bece35da20c0953f779809570f71d2ce12b32b0a35deb6a0da9a0`
恰与当前文件一致。这不是数学输入哈希失配；它是审查覆盖行数/
锚点的文档错误。

原审者保留同一输入哈希，补读当前证明 300–390 行，将全文范围
改为 1–390，并将依赖分离引文定位到 360–361 行；追加了定向
关闭回执。主审者已读回修改的表格、锚点和整个关闭段，核对
390 行文件与记录哈希一致。没有修改作者证明、数学结论或来源
核查范围。本审者没有修改他人的审查文件，也没有要求重跑。

**D2 — CLOSED：Git 暂存措辞精确化。** 最终索引初版的“索引为空”/
`empty index` 不准确：`git diff --cached --name-only` 无输出表示
无已暂存差异，不是 Git index 没有已跟踪条目。主协调者仅改
本轮 README 为“无已暂存差异”、COORDINATOR 为 `no staged changes`。
已定向读回这两处。没有变更链接、Git 状态或其他事实。

## Git 与未提交/同步边界

只读 `git status --porcelain=v1 --untracked-files=normal` 显示
CURRENT 为未暂存修改，整个研究批次为未跟踪目录；八个继承
未跟踪目录仍在。`git diff --cached --name-only` 为空。
HEAD 与本地 `refs/remotes/origin/main` 均为
`2974f8ea5f9e7cb0f8146cae017add38a6939da0`。

这些命令没有 fetch、stage、commit 或 push。本地 tracking ref
相同不证明远端服务器现时 tip 相同；未作新远端查询。文档应继续
标明本批仍在工作树，未提交或推送。本次只允许写本报告，不执行
任何 Git 改动，不动八个继承目录、旧轮次或正式封存树。

## 最终状态及一次链接扫描

最终索引一致保持 `ROUND4_CHECKPOINT`、M1/AS2/IR1 为 3/5、仍缺
两项、零稿/PDF/评价/编号、7 个 screen、5 个 deep、63 条支线
查询和 1 次作者数学执行。它们没有把短证明或 helper-review PASS
改写为新增准入，没有宣告五篇目标完成。

**唯一最终本地链接扫描已完成，退出码 0。** 在最终索引和 D1/D2
修正读回后，使用只读脚本抽取简单行内 Markdown 链接并核对本地
路径存在性；范围包括本报告，不包含 CURRENT 的历史批次正文。

| 实际扫描收据 | 结果 |
|---|---:|
| 本轮完整 Markdown 文件 | 22 |
| 文档范围总数 | 25 |
| CURRENT 最新批次前缀行数 | 100 |
| 本地链接出现次数 | 151 |
| 去重本地目标路径 | 69 |
| 跳过的外链 | 44 |
| 纯 fragment 链接 | 0 |
| 不存在的本地目标 | 0 |
| 扫描造成的外部请求 / 数学运行 / 文件写入 | 0 / 0 / 0 |

这是简单行内链接的本地文件存在性检查，不是完整 Markdown
渲染验证；没有抓取外链、验证 heading anchors，或递归审查链接
指向的全部历史内容。在索引完成前未对待建链接报告假断链。
本报告扫描后仅补入实际计数与关闭状态，未增改链接，也未重扫。

`NO_BAD_EULER_OR_ROOT_NUMBER` 保持：来源算术、局部辅助结果、
文档通过或有限诊断均不推出目标 Euler 因子、根数、automorphy、
目标零点或 Hilbert–Pólya 实现。
