# CS07 — 执行与验证证据

Scope ID: `ASFS-DISCOVERY-20260919-CS07`。  
Status: `320-MODE FINITE STABILITY MET; TINY ORDER EFFECT; FIT BENEFIT NOT ESTABLISHED`。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-09-19（研究标签；UTC见实际记录）
- Verification Status: UNVERIFIED
- Version Label: exp_result_v1

## Experiment Result

- ID: `ASFS-DISCOVERY-20260919-CS07`
- Type: analysis（固定参数、非优化的有限谱诊断）
- Status: completed
- Working Directory: `/root/autodl-tmp/hilbert-polya-structure/arithmetic_symplectic_flow`
- Command: 见[冻结执行卡](../execution-card.md)，单次600秒硬限、10秒宽限。
- 授权：用户继续已授权的本地自动实现/运行；沿用授权，不另行扩大任务。
- 输入：[15项冻结锁](../input-locks.json)，原对象、数组、旧参考只读。
- 输出仅本包run-1；不上传、不安装、不提交、不推送、不生成PDF。
- Duration: 163.698625秒（程序主体）；Exit Code: 0；PID: 58753。
- UTC事件：2026-09-18 22:03:18.360至22:06:02.080，不改称9/19实际执行。
- 11传播/11完整SVD/5静态分解；无优化、目标生成、INVALID或重试。
- 峰值RSS370904KiB（362.21MiB）；41输出文件296378576字节（282.65MiB）。
- 30/60/90/120/150秒五次资源样本均未越提示/输出预算；无输出停滞或异常退出。
- 实际进程退出码与外部观察见[执行收据](execution-receipt.json)。

### 输出位置与内容

| 输出 | 内容 |
| --- | --- |
| [manifest](run-1/manifest.json) | 15输入锁、runner与锁清单哈希、PID、版本和角色 |
| [events](run-1/events.jsonl) | 实际顺序、计数、五次资源样本与完成事件 |
| [result](run-1/result.json) | 10角色/5静态/4复用对象及四窗口完整结果 |
| [comparisons](run-1/comparisons.json) | G与原始E差、E0/scale、Δ/ε所需配对 |
| [points](run-1/points.csv) | 6080行，19个对象各320项；不含63态解析控制 |
| [minimum cache](run-1/minimum-cache.json) | 192项连续势最低值及根账本，浮点非认证 |
| [file inventory](run-1/file-inventory.json) | 40个先前输出的大小；清单本身为第41文件 |

11个传播NPZ保存实际Ctilde/全sigma/E/前320左右态（控制为63态）、
样本、重复次序、势和占据/残差；5个静态NPZ保存全H_avg/全谱/前320态。
全部旧文件保持原哈希，B组静态源明确引用A1而不重算。

## 审查角色与复现边界

[形式审查](form-review.md)在执行前核对两卡；[代码审查](code-review.md)
由非作者任务完成；[保存结果审查](saved-result-review.md)只读取既有数组。
模型审查为同家族内部检查，不是外部同行评审；任务可能共享历史上下文。
作者的语法/guarded import检查不调用传播、SVD、eig、root或旧main。
保存结果复算仅限已有数组的算术、身份与指标，不是第二次研究运行。
未进行独立从头复现，因此运行标签不提升为VERIFIED。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: validate
- Origin Date: 2026-09-19研究标签
- Verification Status: ANALYZED（保存结果分析；非独立从头重跑）
- Version Label: validation_v1

## Validation Report

整体解释状态：CAUTION。研究输出是确定性有限矩阵诊断，没有随机抽样、
p值、置信区间、标准误或总体检验。2%和效应比10是冻结工程阈值，
不解释为显著性或严格误差控制。目标1–320全部已知，非新盲测。

结果解释：全部三个离散轴过冻结2%线；旧N767有利尾段未保留。
beta.20的全320次序效应5.510180e−6%仅是微小有限效应，尾段301–320
为UNRESOLVED；原beta.02差更小，且未领取另一beta的判别标签。
静态对照仍近似相同，没有实质拟合收益、无限谱或算术门结论。

### 11/11谬误类型覆盖

| 类型 | 本包处理及限制 |
| --- | --- |
| Simpson聚合反转 | 四窗口及所有角色分列；不以总MAPE隐藏高段变化 |
| Ecological生态推断 | 不从有限窗口推断每个无限编号或算术整体 |
| Berkson选择偏差 | S0047来自既有监督选择；固定后检不消除原选择偏差 |
| Collider碰撞变量 | 无因果调整模型；本项不适用，不据此给正确性证明 |
| Base-rate基率忽略 | 无分类/患病率推断；本项不适用 |
| Regression-to-mean均值回归 | 非重复随机测量，不作随机改善叙述；参数保持原值 |
| Survivorship幸存者偏差 | INVALID、未执行、超时及不利角色必须保留 |
| Look-elsewhere多处寻找 | 不新增赢家，所有预定比较完整报告；无显著性检验 |
| Forking-paths分析自由度 | 两卡先冻结，beta/排列/样本/r/主N/阈值不按结果修改 |
| Correlation/causation相关因果 | 有限次序敏感性不能推出时间排序造成拟合改善或算术机制 |
| Reverse-causality反向因果 | 目标曾参与原模型选择，不能倒推零点由该系统自然生成 |

复现方法：未重跑。Verdict: CANNOT_VERIFY independent reproduction。
本表是解释边界检查，不是统计认证、全部研究偏差排除或论文质量评分。

## 文档检查

2026-09-18 22:14 UTC最终集成检查：本包9份Markdown及两个总索引，
合计11份文档、565个本地链接/锚点，0缺失；当前结果状态在paper、
README、claim ledger、证据首页及两总索引一致，Scope ID一致。
候选卡/执行卡特意保持执行前冻结状态和原哈希，不伪装为事后预注册；
当前结果由上述结果文件承载。15项锁、runner身份与实际manifest相符。

两已跟踪索引的`git diff --check`通过，257注册行与256连续。
12个新文本文件另作全量空白检查：默认Git提示的10处尾空格均为
Markdown有意的双空格换行，除此之外无尾空白缺陷；不为消除格式提示
改写冻结卡。AST与执行前静态审查通过，没有重跑未变的研究计算。
保存结果审查读取全部数组，正文关键数值一致；run-1保持只读。
本轮未生成LaTeX/PDF或作任何Git提交、推送、外部上传。
