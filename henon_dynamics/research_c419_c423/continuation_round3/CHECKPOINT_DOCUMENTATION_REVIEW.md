# 第三轮检查点：静态代码与文档目标检查

日期：2026-09-07 UTC；终态扫描与状态核对于约 11:24 UTC 完成。审查范围为本轮检查点材料，不是论文评审、
独立数学认证、正式评价或新准入。本报告是本审查唯一写入的文件。

## 当前结论

- 四个指定 Python 文件：全文静态阅读及单次 AST／内存编译完成，
  `PASS_STATIC_SYNTAX_WITH_DOCUMENTED_RUNTIME_LIMITS`。
- 协调者明确“第三轮全局更新完成”后，终态简单 Markdown 本地目标检查
  完成：`PASS_LOCAL_TARGET_EXISTENCE_AFTER_ONE_FALSE_POSITIVE_TRIAGE`。
  26 个范围、140 处真实本地链接、65 个不同目标均存在；1 个正则误报
  经定点人工核对关闭，0 个真实缺失。
- 状态范围检查：`PASS_CHECKPOINT_STATUS_SCOPE`。保持本批 3/5 合同、
  仍缺 2 项，第三轮零新增准入，0 新稿/PDF/正式评价/逐项 C 编号；
  九个筛选条目不是九个新问题，这不是五篇交付。

## 1. 检查边界和独立性

本次完整静态读取以下四个本轮脚本，没有导入、执行或调用其函数：

1. [固定 McMillan 纤维诊断](cubic_recurrence/check_fixed_fibre.py)
2. [B1 整数除数图诊断](birational_arithmetic/exact_probe.py)
3. [B2 整数参数诊断](birational_arithmetic/b2_exact_probe.py)
4. [六层精确分母诊断](spectral_recursion/exact_denominators.py)

以标准库 `ast.parse` 解析源码字节，再对 AST 调用内存 `compile`，
`optimize=0`、`dont_inherit=True`。没有对产生的代码对象调用 `exec`，没有
目标模块导入，没有 `py_compile`／字节码文件写出。检查进程带 `-B`。
目标代码的第三方依赖是否安装、实际导入与运行是否成功不由此证明。

另为核对动态导入风险，只读查看旧
[构图依赖](../continuation_round2/solenoid_boundary/semigroup_probe.py)
的导入、状态 cap、identity 起始索引及主程序保护相关片段。
它不计入四个“全文＋AST”文件，也没有重新运行其 `main`、`analyze`
或旧数学验证。

这些脚本不是本审查者编写，故其静态阅读属于非作者代码检查。
但有限输出的真实性、图抽取算法的全功能正确性、证明与来源的适用性
没有在本次通过独立数学重建认证。PC3 的四份材料由同一审查者先前
编写，对它们的范围／文档检查明确属于自查，不能称为非作者证明审查。

## 2. 静态检查的真实计数与输入身份

首次且唯一一次 AST／内存编译检查：4 个文件，407 行，3375 个 AST
节点；4/4 解析与编译成功，0 个语法失败。每个文件在检查前后重新读取
并比较字节，4/4 未变。没有因此重跑数学程序。

| 文件 | 行数 | AST 节点 | `assert` 行号 | SHA-256 |
|---|---:|---:|---|---|
| `cubic_recurrence/check_fixed_fibre.py` | 124 | 922 | 无 | `88be3d20b4eadecc2d14d6c919ee7801872b2a1fe9890f3c36fe77831fc46882` |
| `birational_arithmetic/exact_probe.py` | 81 | 632 | 46、48 | `f51373a9c41f833b98beb7c88cc6a53b372379159bcef4b5511853faaccf0a15` |
| `birational_arithmetic/b2_exact_probe.py` | 68 | 572 | 23、25 | `9dcea18cdf2b4bae671f6c4cccdb245a05aaddd0e9fa6831bbda885c90c9e0ec` |
| `spectral_recursion/exact_denominators.py` | 134 | 1249 | 无 | `0e3f71a4b18a1db39617a6dcce37c32295da750df7743fe38b9963db8e48c255` |

四个源码摘要与现存作者收据／证明文档中的相应源码摘要一致。
本审查没有重新计算作者数学输出，因此这种一致性只绑定被查看的代码
版本，不能证明历史运行环境或输出结论正确。

## 3. 量词、样本范围与运行限制

### 3.1 固定 McMillan 纤维

代码固定 $A=-5$、$K=4$、一个 rational seed 与一个 elliptic seed；
循环仅检查 $[n]P$、$1\le n\le12$。Birational inverse 检查只对
非零 $Y$ 的点执行，计数另行输出，并非代码自动宣称每个参数均已验证。
原始 rational seed 与其三个不同轨道点的回归使用精确 `Fraction`。

`PASS_FIXED_FIBRE_ONLY`、`full_parameter_atlas_claimed=false` 与
`independent_review_claimed=false` 均限制正确。全参数 rational atlas
在[部分证明](cubic_recurrence/PARTIAL_PROOF.md)中仍明确未闭合。
十二个有限点如何与经典 torsion 定理、whole-fibre identity 结合，不是
这次语法／文档检查独立认证的数学内容。

所有判错使用显式 `require` 抛出异常，不受 `-O` 删除断言影响。
`main` 有保护；脚本自身仅打印 JSON，读取自身源码以计算摘要，无固定
输出文件覆盖。例外或恒等元在相关除法前处理；本结论仅针对固定输入，
不把无类型约束的 helper 当作通用 elliptic arithmetic API 认证。

### 3.2 B1 除数图

`range(1,513)` 对应恰好 512 个正整数参数。每个参数使用所有 signed
nonzero square divisors 和 ordered pairs，遍历有限 successor graph，
没有人为设置周期上限。循环词只取 cyclic rotation 的最小代表，不把
反转或变号等同于同一 native orbit。代码状态、sample 字段与
[冻结范围](birational_arithmetic/FROZEN_CONTRACTS.md)相符；对所有整数
参数的全局刚性在报告中仍未证明。

第 46、48 行的两条输出-cycle 再检查是 `assert`，在 `python -O`、
`-OO` 或有效 `PYTHONOPTIMIZE` 下会被移除。现有作者收据的命令没有
显式 `-O`，但没有记录 `sys.flags.optimize`，本次不能独立确认历史
断言是否开启。不将这个限制虚报为已观察到的失败，也不以重跑补证。

执行 `main` 会用 `write_text` 覆盖同目录固定
[B1 输出](birational_arithmetic/B1_EXACT_PROBE_OUTPUT.json)，不是
exclusive-create 或 atomic replace；中断可能留下不完整文件。
当前审查未执行该写入。`fixed_only_guess_survives_sample` 只是一项有限
样本布尔结果，且空集合时也会为真，不能作全参数证据。

### 3.3 B2 参数矩形

两个 `range(-8,9)` 排除 $b=0$，对应 $17\times16=272$ 个参数对。
每对仅在冻结高度 $2|a|+|b|+1$ 中取整数、排除 $x=0$ 和 $x+b=0$，
再用 `divmod` 的余数零条件保留精确边。有限图无额外周期截断；它对
所述范围的完整性依赖报告中的高度引理，不是本次 AST 检查证明的结论。

该脚本导入 B1 的 `graph_cycles`，所以两个诊断不构成图抽取部分的
独立实现。B1 的主程序有 `__main__` 保护，正常 sibling import 不调用
其主程序；本次仍未进行导入。

第 23、25 行另有两条 optimization-sensitive `assert`；同样保留
上述历史优化环境未记录的限制。执行会覆盖固定
[B2 输出](birational_arithmetic/B2_EXACT_PROBE_OUTPUT.json)。标准输出是
去除 `all_cycles_in_sample` 的摘要，不能代替完整 JSON。
`period_at_most_three_guess_survives` 明确仅是有限样本观察；另外的手推
三周期族不能被改写为通过扩大样本获得，也没有闭合全参数分类。

### 3.4 六层标量分母

`main` 固定 $k=1,\ldots,6$，构图调用硬编码 state cap 250000。
导入旧构图代码发生在模块顶层的 `spec.loader.exec_module(prior)`，
因此仅导入本文件也会执行该依赖的顶层内容；不能把它称作无导入副作用
的纯库。当前依赖的旧数学入口有 `__main__` 保护。本次不触发该路径。

若构图返回 cap failure，新程序立即抛 `RuntimeError`，不会给这层写出
`EXACT_FINITE_LAYER`。代码还显式检查 recurrence order、normalization、
所有可用 residual、dimension-sufficient residual count 以及 polynomial
gcd；这些检查不是 `assert`，不受 `-O` 删除。其 Cayley–Hamilton 数学
认证理由由[本层证明文档](spectral_recursion/PROOF_PACKAGE.md)承担，
此次不重复或声称独立证明。

程序每层直接打印 stdout，并无整次运行最后的 SUCCESS 记录。若后续层
异常，已有的若干 JSON 行只是部分输出；六层完成还需完整六行、退出码
及作者收据。state cap 不是时间／内存预算：SymPy exact factorization
与整数系数增长仍可耗时。只有现有固定六层范围在本次查看范围内。

该脚本需要已有 SymPy，AST／内存编译不验证其可导入性或版本。没有
安装任何依赖。固定六层 scalar denominators 不等于 all-layer recursion，
更不等于 infinite weighted sum 的整圆周非消去；文档维持未准入状态。

## 4. 终态 Markdown 目标检查

只在协调者的明确完成通知后执行了一次全范围扫描。使用无字节码标准库
检查进程，剔除 fenced code／inline code，抽取简单行内 Markdown
显式目标及 reference definitions，按每份文档所在目录解析本地路径。
检查阶段只读，退出码为 0；是否存在缺失由结果字段和人工分类判定，
不是把进程退出码 0 本身视为全部链接成功。

实际范围：本轮所有 23 份 `.md`（包括[本报告](CHECKPOINT_DOCUMENTATION_REVIEW.md)）、
批次根 [README](../README.md)、[准入裁决](../ADMISSION_DECISIONS.md)，
以及 [CURRENT 状态](../../CURRENT_RESEARCH_STATE.md) 的最新 C419–C423
前缀第 1–79 行，截止下一个 C414–C418 历史批次标题前，共 26 个范围。
不是全部历史状态扫描。扫描期间 26 份文件字节与 round3 Markdown
清单均未发生变化；报告在扫描后仅作本次检查结果的终态记载。

原始抽取计数为 204 处候选行内目标：141 个候选本地目标与 63 个
HTTP(S) 目标，0 个 reference definitions。原始候选本地目标中唯一
“缺失”是 `positive_charp_new/PROOF_PACKAGE.md` 第 103 行的公式
`E[d_i](k)`，被简单正则误识别为路径 `k`。定点读取原行确认它在
display math 中，是 elliptic torsion points 的记号，不是链接。
因此不应创建文件 `k`、修改公式或把它记为真实文档缺陷。

人工分类后真实计数为：**140 处本地链接、65 个不同本地目标、0 个
缺失；63 处 HTTP(S) 明确跳过**。共 203 处真实显式行内链接。
这是一轮扫描加一次误报定点核查，不是先失败后偷偷重跑到 PASS。
为缺失目标所作的代码／文档修复为零；没有第二轮全范围扫描。

| 扫描范围（相对本轮目录，另行注明者除外） | 真实本地链接 | 跳过 HTTP(S) |
|---|---:|---:|
| `CHECKPOINT_DOCUMENTATION_REVIEW.md` | 14 | 0 |
| `COORDINATOR_REVIEW.md` | 5 | 0 |
| `INDEPENDENT_HELPER_REVIEW.md` | 3 | 0 |
| `README.md` | 17 | 0 |
| `SCOUT_PLAN.md` | 2 | 0 |
| `birational_arithmetic/FROZEN_CONTRACTS.md` | 0 | 4 |
| `birational_arithmetic/RUN_RECEIPT.md` | 0 | 0 |
| `birational_arithmetic/SCOUT_REPORT.md` | 6 | 5 |
| `birational_arithmetic/SOURCE_AUDIT.md` | 0 | 19 |
| `cubic_recurrence/FROZEN_CONTRACTS.md` | 5 | 1 |
| `cubic_recurrence/PARTIAL_PROOF.md` | 3 | 1 |
| `cubic_recurrence/SCOUT_REPORT.md` | 5 | 0 |
| `cubic_recurrence/SOURCE_AUDIT.md` | 9 | 10 |
| `positive_charp_new/FROZEN_CONTRACTS.md` | 0 | 0 |
| `positive_charp_new/PROOF_PACKAGE.md` | 1 | 4 |
| `positive_charp_new/SCOUT_REPORT.md` | 3 | 0 |
| `positive_charp_new/SOURCE_AUDIT.md` | 0 | 10 |
| `rational_trace/FROZEN_CONTRACT.md` | 0 | 0 |
| `rational_trace/PROOF_PACKAGE.md` | 2 | 0 |
| `rational_trace/SOURCE_AUDIT.md` | 2 | 4 |
| `spectral_recursion/FROZEN_CONTRACT.md` | 2 | 0 |
| `spectral_recursion/PROOF_PACKAGE.md` | 2 | 0 |
| `spectral_recursion/SOURCE_AUDIT.md` | 2 | 5 |
| batch 根 `README.md` | 23 | 0 |
| batch 根 `ADMISSION_DECISIONS.md` | 22 | 0 |
| `CURRENT_RESEARCH_STATE.md` 最新前缀 | 12 | 0 |
| **合计** | **140** | **63** |

仅检查简单 Markdown 显式目标的本地文件／目录是否存在。HTTP(S)、
其他外部 scheme 及纯 fragment 均不能计为已验证；带 fragment 的本地
目标也只核对文件部分，不验证 anchor。不会声称链接可达性、引用内容、
PDF 正确性或完整 Markdown 解析器级覆盖。本轮抽取到的其他 scheme、
纯 fragment、带 fragment 或 query 的本地目标均为 0。没有 HTTP 请求。

## 5. 最终状态与证据口径

完整读取本轮 README、协调者裁决、SCOUT_PLAN、batch 根 README 和
ADMISSION_DECISIONS，以及 CURRENT 的第 1–79 行，另对本轮 Markdown
作状态词定向检索。辅助审查文档仅为独立性与最终处置口径读取了开头
及末尾；不声称本审查者全文重新认证其中数学。各主入口一致：

- M1、AS2、IR1 保留三项准入，第三轮无第四或第五项。原来 2/5 的
  首轮处置明确位于历史段落，不能与当前 3/5 混淆。
- 新全局状态为 `ROUND3_SCIENTIFIC_SHORTFALL_CHECKPOINT`，计划也已
  标明其初始 scouting 描述是历史冻结范围，不是仍待执行的现态。
- 九个筛选条目包括旧 AS1 的新尝试及浅筛 B3，不等于九个新独立问题。
- 全轮数学执行收据是四个新程序各一次；本次 AST、读取和路径检查
  不是第五次数学实验，也没有重复其中任何一个作者运行。
- B1 的现有 JSON 已完整只读查看，其 `retained_edges` 为 **407**，
  与作者收据、支线报告及协调者裁决相符；没有使用 4078 的笔误。
- 六层全长度 recurrence 认证仍只覆盖固定层；十二个 elliptic multiples、
  512 个 HV 参数和 272 个 Bedford–Kim 参数保持各自冻结样本范围。
- 辅助审查的有限结论已经协调者采纳，无待改项；其 reviewer 与 IR1
  的既有作者关系披露，不称盲审或独立数值复现。B1/B2 旧 author-run
  receipt 中的 pending 文句明确带有“at the time of this receipt”，
  是保留的历史状态，不覆盖最新协调者裁决。
- 无新稿、PDF、正式评价或逐项 C 编号；本轮目录中 `.tex`、`.pdf`、
  `.bib` 文件实际清单为空。这个文件检查只覆盖本轮，不据此声称全仓库
  没有旧论文。A2、目标 Euler 因子、根数及零点对应均未晋升。

协调者随后明确的两处清晰化仅把 README 的两种全图提取点名为 HV／
Bedford–Kim、CURRENT 的“现启动”改为“当前续接批次为”。不改链接、
代码或准入状态；按指示没有为此重扫链接或重做 AST。终态报告的
自链接另作定向存在性确认，不增加上述 140 处的独立验证计数。

## 6. 最终交付

本检查任务完成，没有需要作者修复的文档目标或状态冲突。
第 3 节运行限制仍成立，不能把本报告推广为安全执行器、全数学 PASS
或发布门槛完成。仅修改本报告；没有修改四个源码、其他文档、生成 JSON、
全局状态或 Git，没有依赖安装、数学重跑、第三方请求或未知路径清理。
最终检查点仍是 **3/5、缺两项、0 新稿**，不是五篇目标完成。
