# 当前研究状态与恢复入口

核对日期：2026-09-05。适用主线：henon_dynamics，五篇完整论文一轮。
本文件用于中断、压缩与模型切换恢复；实际发布清单和复验结果优先。

## 最新授权与当前状态

最新用户确认授权 **C394–C398**，不是旧 C99–C103，也不是 C389–C393。
五个完整源系统证明与终稿 PDF 均已完成；所有五包最终 write 后的完整
nonwrite 均实际通过，包含 C394/C396 修补发布门后的最终复验。
233payload加五manifest、238物理文件、22页终稿已由两路独立审与root复核。
本批提交由 Git 历史中的 Add Route-A papers C394-C398 标识；精确提交哈希
与实际远端核对在用户交付信息中报告，避免文件自引用其所在提交。
不要根据快照虚构活动进程：恢复时核对真实Git历史和发布清单。
完成本轮五篇后等待用户确认，不得自行开始 C399–C403。

- 正确仓库：/root/autodl-tmp/hilbert-polya-structure，main 分支。
  环境 cwd /root/autodl-tmp/henon_zeta 不是本轮研究目录。
- 本轮冻结证据基线：697518b6db90458f86f7916fbf397b8ad5ef2372，
  即已完成并推送的 C389–C393。
- 本轮 fetch 发现三条远端提交，差异共421路径，只属于 SYMBOLIC_DYNAMICS_STATE.md、
  docs/ 与 papers/；与 henon_dynamics 和 evaluator 无重叠。
  已安全快进至9a394ee2c3ab171ba4341d77c439ba145e247a85，证据基线不变。
- 提交前再次 fetch，另有一笔符号动力学提交，新增差异130路径，仍仅属于
  SYMBOLIC_DYNAMICS_STATE.md、docs/、papers/与symbolic_dynamics/。
  已逐路径检查与本批246个暂存文件及evaluator无重叠，并安全快进至
  79e8729b5c25bbf3140482f7fd2ece7d32f09b79；冻结证据和五份manifest均未改变。
- epoch1788566400，障碍 HEN-O378–HEN-O382。
- root 负责 C397/C398及整合；原 C382/C379/C383代理分别负责 C394/C395/C396。
  代理名字不是论文编号。内部交叉审分工见批次审查，不宣称外部或人类评审。

入口：[本轮冻结计划](BATCH_PLAN_C394_C398.md)、
[选题及经典所有权](IDEA_REPORT_C394_C398.md)、
[本轮发布审查](BATCH_REVIEW_C394_C398.md)。

| 编号 | 单篇完整进展 | 终稿 | 发布状态 |
|---|---|---:|---|
| C394 | 非线性p-adic联合解析时间、全部最小轨道闭包、每个有限模层周期和代数命中集合 | 4页 | 最终write/nonwrite通过 |
| C395 | BCZ全部Farey周期层、无理非周期、精确物理屋顶及抛物返回矩阵 | 5页 | 最终write/nonwrite通过 |
| C396 | 全阻抗吸收弦PDE谱、精确消亡、空谱预解式及伪谱/算子理想边界 | 5页 | 必要发布门修复后最终write/nonwrite通过 |
| C397 | Salem全固定群与有理zeta、本原/累计反正弦波动、同宿平凡性和例外边界 | 4页 | 最终write/nonwrite通过 |
| C398 | 指数势完整贝塞尔谱及普通行列式、有界Weyl余项、热迹和全固定归一化不匹配 | 4页 | 最终write/nonwrite通过 |

实际233个payload加五份manifest，最终PDF合计22页。
最终篇数/文件数和哈希已由实际物理成员总审确认，不只按预期相加。
每包三个稿件版本是同一篇论文的实质修订，不是三篇论文。

## 用户长期原则

1. 优先 skills 路线图 A，尤其 A1/A2 的真实推进。
2. 五篇一轮，每篇闭合完整独立问题，不能把一篇拆成五个小步骤。
3. 允许大胆假设、扩大步幅及更换不成功的动力学子类型。
4. 实际输出论文 PDF，保留完整证明、独立复算、所有权与失败边界。
5. 批内连续完成，五篇后中文汇报并等待确认；额度重置不是无限开批授权。
6. 文件数、测试数、经典源系统重建与目标 A1/A2 突破必须区分。

## 路线评估与严格边界

权威：[Route-A evaluator](../flow_systems/skills/route-a-evaluator.md)，v0.2.0。
SHA256：6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c。
这次远端同步后实际重新核对哈希未变。

| 候选 | A0 | A1 | A2 | A3 | A4 | 整体 |
|---|---|---|---|---|---|---|
| C394 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | EXPLORATORY |
| C395 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C396 | FAIL | FAIL | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C397 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C398 | FAIL | FAIL | FAIL | FAIL | NATURAL_QUANTIZATION | REJECTED |

C394的探索性仅指原生局部非线性算术机制，不是主要HP候选或目标A2突破。
C398证明允许固定正频率缩放及能量平移后的计数不匹配，使用明示的无条件
S(T)振荡外部定理，不是“已匹配T log T所以目标成功”。
evaluator没有唯一自动tuple到overall算法；理由及源系统边界均在冻结YAML。
所有权保持Poonen、BCZ/Athreya–Cheung、Driscoll–Trefethen、
Lind/Waddington/Lindenstrauss–Schmidt及Pólya/Lagarias/Selberg–Tsang–Dobner。

共同边界 NO_BAD_EULER_OR_ROOT_NUMBER：九项目标/Route-B flags和独立
route_b_invocation_allowed均false。不声称目标局部算术、Euler因子、
根数、自守性、目标零点/除子/函数方程或Hilbert–Pólya算子。无Route B。

## 本轮重要修复与验收

C396旧发布清单忽略__pycache__内文件，内部独立审在临时副本实际复现。
已改为完整物理文件集合，并在所有分支前拒symlink、核live evaluator字节。
C394/C397/C398也补显式symlink早拒绝和实际write攻击；当前实际包无symlink。
C397修两个排版溢出；C398修SymPy未展开cosh(log(r))的检查器表示问题。
数学证据和所有最终PDF不受发布门修补影响。不要把工程修复包装成新定理。

C397/C398评估采用完整semantic hard lock加manifest raw-byte ledger，
不是“raw YAML完全不可改”；授权write可以重封语义相同的格式改写。
C394/C396有更严格raw/semantic锁。各包均禁止数值字段bool/float替代，
并实测恶意输入到真正release write入口，不只比较摘要哈希。

实际使用ARS、idea-creator、proof-writer、paper-write与paper-compile适用流程。
以用户五篇后确认替代批内反复许可；当前团队内部审，不调用外部GPT-5.4。
未声称完整ARS运行时、GPU训练、形式证明助手、外部同行评审或新颖性认证。

## 已完成历史与遗留材料

C389–C393已提交并推送697518b6db90458f86f7916fbf397b8ad5ef2372：
238payload加五manifest、22页。[历史批次审查](BATCH_REVIEW_C389_C393.md)。
C384–C388亦已完成；不要重做这些批次冒充当前增量。

本轮前存在并必须保留、排除暂存的八个未跟踪目录：

- 本目录下五个henon_mu3_yukawa_mark包：generating_polynomial、
  minmax_aggregation、triple_coupling、triple_orbit_quotient、pair_dependence_geometry。
- 仓库根henon_ermakov_pinney_isotonic_action_route_a/。
- 仓库根henon_flat_magnetic_torus_landau_route_a/。
- 仓库根henon_hysteretic_relay_oscillator_route_a/。

三个根目录共有12个遗留文件。不能宽泛清理，也不能声称全worktree为空。

## 恢复到交付的最短流程

1. 核实Git历史、当前代理和真实清单；五包已冻结，不重做已完成数学。
2. 需要复验时核所有233payload哈希、五manifest和238物理文件，实际PDF22页。
3. 最终收口以批次审查、实际write/nonwrite、独立审和root复核共同支撑。
4. 若提交交付因中断尚未完成，只暂存五包和八个相关全局文件，检查真实index。
5. cached diff --check；fetch检查路径，安全同步后commit/push，不强推或覆盖。
6. 核实远端真实HEAD和本批无跟踪残留，中文报告；已交付后等待下一次确认。

模型更换不意味着历史全文无损继承。本文件通过工作区与发布证据复核恢复，
未修改应用记忆设置、删除会话或手动触发压缩。
