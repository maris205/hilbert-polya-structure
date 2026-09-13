# Paper29 自然成稿验证：独立 dossier / plan 检查

日期：2026-09-06。结论：**PASS（仅限新 dossier、大纲及测量协议）**。
未发现阻断写作的 GAP；不要求修改当前八节大纲，不要求新定理或实验。
本结论不是候选重新评分、正文页数 PASS、正式论文验收或外部发布许可。

## 1. 本次任务、独立性和技能执行

本审查由未参与该新 dossier / plan 编写的独立代理完成。先全文读取
`/root/autodl-tmp/.codex/skills/research-review/SKILL.md`（106 行），
采用其上下文汇集、针对性批评和自含结论记录步骤。实际工具目录未提供
指定的 Codex MCP `codex` / `codex-reply` 审查通道，故使用本任务明确允许的
新独立代理 fallback；没有冒称调用指定外部模型、配置 xhigh 或拥有 threadId。

检查对象是用户已确认的一次自然成稿和本地测量例外。用户在紧邻提案后回复
“继续”的授权由新范围修订明载；旧 brief / 接续中的待决状态是历史快照，
不要求再次许可。原 R1 PASS、R2 FAIL 和原合取 FAIL 均保留，不改评分。

已通过且输入未变的数学、查新、新意和研究价值不重开。本轮只核对新内容
组织的范围忠实性、必要证明覆盖、引用用途、去重及冻结格式/测量流程。
未作页数估计、容量投票、新文献搜索、数值运行或正文编写。

## 2. 实际输入及读取范围

以下项目路径相对于 `papers/29-filtered-henon-cohomology/`。
表内各输入全文读取，行数和 SHA256 均由本轮实际文件核对。

| 输入 | 行数 | SHA256 |
| --- | --- | --- |
| `notes/SCOPE_AMENDMENT_20260906.md` | 24 | `8cc21363a4c52e319fc5c7c87037031c7eb3384057b3a3aa427ac7feedc416c8` |
| `notes/SOURCE_SCOPE_LOCK_20260906.md` | 63 | `87f8e7d4b4f28010ffbd689aa2e9b7c15e3c75240e1611f1b26f125cb4adbcc5` |
| `notes/PUBLICATION_LOCK_20260906.md` | 48 | `237f047b12c80ca6eef218539ec84a1c7432302d3df3e0b9d88ed7a114408258` |
| `PAPER_PLAN.md` | 155 | `8283fdd364d216f5208b3cadd2c6a6219fc02c432f345baaf1f57680c5ae9406` |
| `refine-logs/EXPERIMENT_PLAN.md` | 18 | `f391e4e3d9ac32ccf589b7b678fc30a5b2a57193dbe5d961df1749fdf167c2ee` |
| `refine-logs/EXPERIMENT_TRACKER.md` | 13 | `9f2e64f987bc78ee510c62dffcf7370ff4f4bec575f6194c5f56e2698fb93783` |
| `refine-logs/FINAL_PROPOSAL.md` | 38 | `80822c0f56a3b3f36edbbaa679af4e1cec5e3be271b37ccde8368786867611a6` |
| `refine-logs/PIPELINE_SUMMARY.md` | 12 | `b9789cc787a6eeaf1336011033864ee929197e1b0a589cf5ac72f9bac3e883c4` |
| `refine-logs/REFINEMENT_REPORT.md` | 14 | `e7d97de1c63c6c59bc87b47fa08b218a8d14f5b04b82262a28238ea20ed544a6` |
| `refine-logs/REVIEW_SUMMARY.md` | 16 | `2ae3b5e51a505d955a0499062c937231eb50e9a5e08dc3ce8b620a565ef407f1` |

以下路径均相对于工作区 `docs/research-batch07/`。M、S、IM、IS 沿用大纲
中的证据缩写；定向读取不是再次声称全文审查旧证明。

| 输入 | 本轮读取范围 | SHA256 |
| --- | --- | --- |
| `PAPER29_FILTERED_COHOMOLOGY_BRIEF_20260906.md` | 全文，281 行 | `046cb40117c6c77f6fb61e5caf93f7ab52cbc8d219827dd731547663a83c1248` |
| `PAPER29_COHOMOLOGY_CITATION_RECORDS_20260906.md` | 全文，181 行；复用已核书目和 claim 对照 | `7a4f27383c07cd50b8e31ad92d3547e3a75d787fa76e9d74ffcfea30f8987b69` |
| M：`PAPER29_CYCLIC_COHOMOLOGY_FINITE_PERIOD_PROBE_20260906.md` | 63–110、243–279、291–393 行 | `0f3ce169e3c62bcde926f3d0f5661dad80dab534394dddaab5f3d24bf8e767b6` |
| S：`PAPER29_HENON_COHOMOLOGY_PROBE_20260906.md` | 29–126 行 | `3f9a1be49ff07bbadd4636f55745d1e31572f2a8988a1402828429edd9ea92d0` |
| IM：`PAPER29_COHOMOLOGY_MULTIPHASE_INDEPENDENT_CHECK_20260906.md` | 95–166、211–281 行；含完整 §8 | `af20049ae1cdf6163a78b24a4a4a66f8f9f3ffe09e73274b6d5d21dc0ac85c39` |
| IS：`PAPER29_COHOMOLOGY_SCALAR_INDEPENDENT_CHECK_20260906.md` | 135–185 行；含完整 §7.2 | `f87d3a19aee0bbc363c588e44e7a90e7a7ba853c314fc8ef18e13f0ce3096abd` |

另全文读取当前 `docs/WORKFLOW.md`（39 行）和 `BATCH_07_CONTEXT.md`
（113 行）以理解本地交付边界；没有重扫历史账本、旧构建树或 Papers27/28。
上表全部已给定身份与实际哈希一致；未修改任何这些输入。

## 3. 新结构的范围与证明覆盖

| 八节结构 | 本次覆盖检查 | 结论 |
| --- | --- | --- |
| 1. Introduction | 问题为普通次数滤过的向量空间余商与完整单周期概形；只预告精确正文结果，先例用途与贡献扣除明确 | PASS |
| 2. Orbit algebras | 有限支撑输入的终止性、公共倍数歧义的合流性、两向同构、shift-k、独立的固定概形识别及长度均在计划内；N=kn≥3 保留 | PASS |
| 3. Filtered primitives | 双射最高单项式排除相消，轨道系数和与累计原函数、两处中间二阶差、无次数损失均列明；IM §8 有理归约只证明一次 | PASS |
| 4. Hilbert series | W_D 与严格像给维数恒等式；rho 两个明确编码式及方向、三个计数区域、关联分次公式均列明；scalar 为短推论，(2,2)/(4) 为单例 | PASS |
| 5. Periodic detection | 个别词直径、唯一大间隙、宏相位、完整 n 项轨道范数及常数 n c_0 均有位置；不重复有限基证明，不将概形零改作点值零 | PASS |
| 6. Effective periods | 精确端点费用与可达性、scalar 平衡距离、n_eff、代数长度、d≥3 次数尺度反例及完整最终阈值量词均列明；binary 小周期和宏相位反例保留 | PASS |
| 7. Univariate rigidity | 调用统一有理归约后，只保留 r 不变环/最高项锥及 f、f_xy 交换反对称性；删除旧反不变环和无曲线 detour 不破坏实际必要性证明 | PASS |
| 8. Symplectic lift | 辛性、底域变换、加性扩张整个固定域、首项系数比、最高两阶系数与多项式平移、全局辛坐标和 Poisson 边界均列明 | PASS |

C1–C4 没有出现证据到正文的孤立主张。全篇仍是一个普通多项式余边界问题，
固定域是同一方程的对象专属应用。没有插入旧 trace-chart、Galois、中心化子、
全碰撞积分或次数取消候选。正文预览、统一基础和后续调用的分工合理。

特别确认：§7 删除的是不再需要的 scalar 基础证明，不是删除单变量刚性
所需的最高项锥。S 中对 C=f_y 的关键链条仍由计划完整保留；而关于常数
不变量、任意正迭代半不变量及有理极点的前提已由 §3 / IM §8 提供。

## 4. 引用覆盖与归属边界

五条计划引文足以覆盖当前大纲实际讨论的背景，没有明显必需引文遗漏。
该判断核对本地已核引用记录，不冒称本轮再次核过各出版社原文。

| 引文 | 当前合法用途及必须保持的限度 |
| --- | --- |
| Bousch1992HenonAlgebras | 二次有限/无限基、wrapping、shift 与非约化意识；§2 构造前归属。1992 未发表稿，不虚构期刊信息，不把本稿新公式全部归给它 |
| Schneider2016DifferenceRings | Karr 型加性扩张判据的直接可读入口；§8 自含证明仍承认已知机制。精确编号若使用，须明确 arXiv v2 |
| CerveauDeserti2018Contact | 接触 lift 次高系数机制的邻近先例，不作为任意四维辛 lift 分类定理 |
| PollicottSharp2004FiniteLivsic | Anosov/Hölder 有限周期近似背景，不支持一般系数 Hénon 的精确概形 iff；不混用旧稿/作者稿/正式版编号 |
| GouezelLefeuvre2021FiniteLivsic | finite approximate Livšic 的流版本，不把 2021 误差率称为当前最佳，也不混淆误差参数与本稿次数 D |

不讨论 Hénon-like 可测正则性，故不引用 BHN 不构成 GAP。显式定义 rho
也无需为 FFT 数字反转增加文献。五条记录应按正文实际使用处引用；没有
最低参考文献数量，更不能借背景综述补页。引言不宣称领域目前仅有多项式误差。

## 5. 新授权、冻结格式与停止条件

新范围修订、publication lock、proposal 和 tracker 一致：仅允许一次完整
自然稿件解决原估计分歧，仍以实际 22–30 页实质正文和独立终审验收。
原 R2 FAIL 不被改写；这不是先把旧候选判 PASS 再写作。

版式为匿名英文单栏 article、11pt、letterpaper、四边 1 英寸及标准间距。
标题到 §8 结语计实际正文，参考文献另起页排除；没有附录、感谢、章节强制
分页、缩放或人工空白。八节无分节页数配额，scalar/multi 共有证明只出现一次。
唯一比较例、边界反例和短应用例均有具体数学作用，不是额外容量承诺。

计划要求先完成一版所有内容并封存源身份，再在新根正确编译、测量；
正文不足 22 页即保存并停止，不按缺页扩写。超过 30 页同样记录失败。
正常编译缺陷只在保留失败的 successor 源/新根作最小修复，不改变内容范围。
页数门内再进行第二新根同源复现、实际全部页面/字体/引用检查及独立终审。
这些要求与已授权窄例外一致，也没有重新引入 Paper28 旧基础设施。

## 6. 必须最小修正与转写检查点

**必须先改动 dossier / plan / lock 的事项：无。** 以下都是现有计划已要求
的转写义务，不是新 GAP、新定理或补页建议；无需因此重新修订原证明。

1. §3 的 pole 论证须写“仿射极除子”，任意正迭代及扩域下无半不变量；
   不能把射影无穷远极点也声称消除。§7/§8 调用这个同一个归约。
2. §4 明确 W_D 的定义和 (sigma-1)W_D 的严格像；rho 只是明确置换，
   异基数不假定对合。结果是关联分次维数级数，不是累计级数或商环不变量。
3. §6 先定义“每个 n≥T(D)、每个 deg g≤D”的最终统一阈值，再写
   d≥3、D_r=3d^r、T(D_r)≥4r+3 的锐性。不得改称最短单次可选周期
   或算法下界。binary 反例的 L≥2、N=2L-1≥3 及主结论 N≥3 要保留。
4. §8 首一化后保留原分子/分母的首项系数比；同一半不变量倍数推出该比
   属于底常数域，因此才得到整个固定域。纯参数势项不可偷偷删去。
5. “没有有理 Liouville 对”要保留完整固定域上 Jacobian 非零的短论证，
   不仅检查展示的两个生成元；不升级到其他函数类别、特殊纤维或全部 isotrivial 族。

## 7. 有界结论与交接

新 dossier、八节组织、引用计划和冻结测量协议：PASS；阻断 GAP：无。
可以按这些已经确认的输入开始一次完整自然源稿，不再进行页数估计投票。
科学范围、原候选 FAIL 历史、22–30 页门及独立终审要求均保持不变。

实际稿件内容、编译结果、实质页数、可复现 PDF 和最终接受状态尚未由本轮
检查；任何一项不得从本 PASS 推出。批次完成数仍为 2/5，Paper30/31 不提前。
本轮仅新增本报告；未编辑他人文件、未重跑旧测试、未产生外部效力。
