# 当前研究状态与恢复入口

核对日期：2026-09-06。主线：`henon_dynamics`，C 系列。
长期规则见 [AGENTS.md](AGENTS.md)；本文件只保存当前状态和证据入口。

## 最新授权与恢复动作

用户在 C399–C403 完成封存、同步及五篇 PDF 交付后，于 2026-09-06 再次
明确“确认，下一轮”。本次新授权范围为 **C404–C408**；起点 Git 为
`5b2a654c4f0b82b0e2d5158146b377ee6bf4e804`，不是续补旧批次。
首轮保留 [新批次选题检查点](research_c404_c408/README.md)：四条线共九个
候选组，**0 份录取合同、0 篇新论文/PDF，C404–C408 未完成**。
Hénon 算术三组、非仿射正特征三组、非线性几何两组、算术/谱迭代一组，
各自保存明确的经典所有权、增量不足或证明未闭合理由；没有冻结五篇计划。
本次有共振计数外推反例（378≠486、176≠192）及 Hietarinta–Viallet
三周期普通点数 9 与理想长度 18 的区别，均不另算论文。协调者用 F5B
独立复核两项共振反例，见 [实际收据](research_c404_c408/ROOT_INDEPENDENT_CHECK.md)。
最具体的未解入口是非加性共振在任意周期、尤其 p 整除周期时的无穷远
抵消/交数理论；没有把“未证明”称为全族 no-go。独立交叉核查与最终
同步状态见检查点总览。不得从此处跳到 C409 或重复计入旧批次。

用户在该检查点交付后再次明确“确认，下一轮”。现从已同步的
`ae2fdc72c865a61369ef74d03d5b266a94ace86d` 续接
[第二轮研究计划](continuation_c404_c408_round2/SCOUT_PLAN.md)，状态为
`PARTIAL_THREE_PAPERS_SEALED`；用户随后“继续”续接
收尾，仍是 C404–C408，不重启已通过的研究门槛。当前三篇完整正文与
PDF 已完成，共 **33 页（10/10/13）**，见
[三个 PDF 与实际缺额](continuation_c404_c408_round2/README.md) 及
[准入决定与部分合同计划](continuation_c404_c408_round2/ADMISSION_AND_BATCH_PLAN.md)：
C404 非线性 Hénon–Frobenius 共振全周期计数、C405 临界整除 Gram
奇异型/强预解式二分、C406 调和 δ 链临界第二 Weyl 系数。三份正文均
通过非作者内部全文与实际引文审查，未留下必须修订的数学/引用问题；
每稿两次新空目录构建及与经审查初稿的 PDF 比较均同字节，全部 33 页
已实际逐页查看，详见 [终构建记录](continuation_c404_c408_round2/FINAL_BUILD_REPORT.md)。
野性动力学加权公式数学成立但不够独立成篇，只保留札记；几何候选
被经典归属或新边界重数反例淘汰。尚未凑齐五个合同，C407/C408 保持空缺。
新工作写入独立续接目录，不回写第一轮筛选记录。

三份 [正式评价及范围](continuation_c404_c408_round2/EVALUATION_SCOPE.md)
均保留目标 A2/A3 FAIL、三类算术对照 INCOMPLETE、27 项 false scope flags
及 27 项 NOT_TESTABLE 目标指标。C404/C405 为源机制 EXPLORATORY，C406
为 REJECTED；源 A1/A4 标签没有提升为目标结论，另有独立一致性核对。
不将这个三篇检查点表述为 C404–C408 五篇已完成，也不进入 C409。

本轮精确封存及最终只读核验已完成：177 个 payload，ledger 排除
自身与 manifest；manifest 包含 ledger 而自排除，共 178 项，树内
实际文件 179 个。`sha256sum -c MANIFEST.sha256` 退出 0、178 项全部
OK；另用独立集合比较核对实际文件等于 ledger 加两清单、也等于
manifest 加自身，无重复、额外/遗漏、符号链接或其他特殊文件，退出 0。
这只证明成员与字节一致，不替代数学正确性。未新增发布程序或篡改测试。
manifest SHA256：`30a886cb0103ff0a0d5f6dae09c7902aca9d794fb14de25571716da9429d59ef`；
ledger SHA256：`1a708210edc404f5a9083c7b8f2f89ac389167229ac70bafec6d6e849f6bdc28`。
封存后不再修改本轮 payload，也不回写首轮或其他旧冻结包。

[独立本地链接审计](continuation_c404_c408_round2/reviews/RELEASE_LINK_AUDIT.md)
覆盖 39 份 Markdown、59 处本地链接：审计时 57 处存在、两清单为
明确预留、0 意外断链。根协调者封存后已实际确认这唯二预留目标生成
并存在。三个主 PDF 的页数/大小/摘要均与终构建收据一致；未复查外部 URL。

Git 整合先后核对远端新变动仅限 symbolic 的 state、P207 与相关记录，
无本批写入路径或 evaluator 重叠，已安全快进至
`eee9dcc3b89e1b822ad4f711aa57be5d7bd1bfd4`。本轮科研提交由 Git 中
`Complete C404-C406 partial batch and seal three reviewed papers` 主题的
对象绑定；同步以真实 refs 为准，不在封存载荷中循环写入自身提交号。
精确暂存范围仅本续接目录、当前入口和两份 Hénon 注册表；八个继承
未跟踪目录保留，不进入本次提交。

## 最近完成：C399–C403

该批最初要求：先按最新官方指导审计优化仓库 AGENTS、skills 与 workflow，
“然后再继续”。前一批 C394–C398 已交付；研究续接范围为 C399–C403 五篇。
仓库 Astra 指令优化及独立场景检查已完成并推送：`b0cdadb9`。
[指令审计](../docs/agent_workflows/ASTRA_AUDIT_2026-09-05.md) 保存来源、范围和验证。
用户随后要求“继续”，并在两份研究稿交付后“确认，下一轮”。续接仍是未完成的
C399–C403，不跳到 C404。当前已冻结
[五篇合同计划](continuation_c399_c403_round2/BATCH_PLAN.md)：C399 Boole 有限实
稳定性乘积、C400 有限正耦合 harmonic delta-comb、C401 非共振 Hénon–Frobenius
双时钟交数、C402 多项式坐标权重全周期留数边矩阵、C403 非乘性慢变整除 Gram
的精确 Schatten 收敛。五篇完整研究稿及 PDF 均已完成，共 **59 页**；
[本轮交付总览与五个 PDF](continuation_c399_c403_round2/README.md) 为当前入口。
三份新正文均有完整非作者内部审查：C401 一句非共振条件澄清已定点闭合，
C402/C403 无需修订；全部书目与实际引用语境逐项核对，无未关闭数学问题。
Boole 9 页与 δ 梳 14 页的 [前轮研究快照](research_c399_c403/README.md) 保留原字节，
合计 23 页及既有正文审查、定点修订、双新目录同字节构建、全页 QA 收据均复用。
它原有“未编号/缺三合同”等状态仅描述该冻结时点，不回写旧 manifest。
本轮 [五份正式评估及范围记录](continuation_c399_c403_round2/EVALUATION_SCOPE.md)
已写：C401/C403 仅源机制 EXPLORATORY，其余 REJECTED；目标 A2/A3 全未通过，
三类算术对照门槛均如实记 INCOMPLETE；另经独立跨产物一致性审计，未发现
源结论被提升为目标结论。三篇新终稿各做两次新空目录构建，PDF 逐对同字节，
最终日志无警告、字体全嵌入、文本及全部 36 页目视通过，见
[最终构建收据](continuation_c399_c403_round2/FINAL_BUILD_REPORT.md)。
用户 2026-09-06 的“继续”续接最后的封存和同步，不重启已验收的数学/
编译门槛。批次封存与最终只读核验已完成：232 个 payload（173 个新载荷、
59 个原快照文件），manifest 233 项；`sha256sum -c MANIFEST.sha256` 退出 0，
全部 233 项 OK。另只读核对实际文件集合与 ledger/manifest 成员完全相等、
无重复/额外文件/符号链接，退出 0；原快照同一命令仍 58 项 OK、退出 0。
新 manifest SHA256：`7ea58a3d8f25ee7079084c3af06d57bc5334a2e242abf3b627a452a2bec213b2`；
ledger SHA256：`95364ffa81ca05d81a8bf71031aaf437370efa5ff6f8f974b0ee0ae42bc7caf9`。
该核验只证明字节和成员一致，不替代科学审查；没有新增发布程序或伪造
篡改测试。核验后未改封存 payload。原快照 manifest 自身仍为
`e1b707ed43cd04fc3f9daf142618f1364b42c51e85ac1cba4860b20520fe0750`。
独立只读链接核对覆盖本批及复用目录共 56 份 Markdown、136 处本地链接
（77 个唯一目标），全部存在；五个 PDF 实测页数 9/14/13/12/11，三个
新 PDF 的摘要和大小与终构建收据一致。未重查外部 URL 或重做数学。

Git 整合已逐次只读确认远端变动限于 symbolic 研究流的 state、P204–P206
及相关记录，与本批无重叠；已安全快进到 `bad9dff9f11155a8ee8fd8ea7f40bdf5eb5f183d`。
本批科研提交由 Git 中 `Complete C399-C403 five-paper batch and seal reviewed artifacts`
主题的对象绑定；同步状态以实际 refs 为准，不为在 payload 内写入自身提交号
循环改写 manifest。五篇检查点停在 C403，未开始 C404。

发现并独立确认了 [C108 二周期源码缺陷](continuation_c399_c403_round2/nonlinear_return/BUG_FINDING_C108.md)：
producer 的方程并非其字面 Hénon 映射的二周期方程。旧 τ₂ 与直接依赖的
determinant 前缀停止作为通过证据使用；正确 τ₂=0。旧冻结文件原样保留，
不自动否定该包其他命题，也不将纠错另算新论文。
源文件的 Git 空白检查通过；原始编译日志自带的尾空白与末尾空行原样保留，
因此包含日志的全量空白检查会报告这些已知提示，未为消除提示改写原始证据。

正确仓库：`/root/autodl-tmp/hilbert-polya-structure`，分支 `main`。
环境初始 cwd `/root/autodl-tmp/henon_zeta` 不代表本主线工作目录。
恢复时查 Git、真实进程和当前产物，不根据聊天摘要虚构已完成步骤。

## 最近完成：C394–C398

提交并推送：`34c3781c7ad7231048ed01cc6ff174f3ded99433`。
交付时已实际核实本地 HEAD、origin/main 和远端 refs/heads/main 一致。
五篇终稿共 22 页；233 个载荷文件、5 份 manifest；最终发布复验均通过。
这些是该批实测结果，不是下一批必须达到的文件数或页数。

- [冻结计划与五篇合同](BATCH_PLAN_C394_C398.md)
- [选题、碰撞检索与经典所有权](IDEA_REPORT_C394_C398.md)
- [完整结果、修复、审查、PDF 与哈希](BATCH_REVIEW_C394_C398.md)

C394 仅局部 EXPLORATORY，其余四项 REJECTED；全部目标 A2/A3 未通过。
C398 的排除范围是固定正频率缩放及固定能量平移，不包括任意非线性重参数化。
此前 C389–C393 已交付 `697518b6db90458f86f7916fbf397b8ad5ef2372`，
见 [历史审查](BATCH_REVIEW_C389_C393.md)。不重做这些结果冒充新进展。

## 不变量与遗留材料

新 C 系列沿用 [Route A v0.2.0](../flow_systems/skills/route-a-evaluator.md)；
SHA256：`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。
保持 `NO_BAD_EULER_OR_ROOT_NUMBER`，没有目标算术晋级或 Route B 授权。
已冻结论文、evaluator、评估 YAML 和发布清单不因指令优化而改写。

八个既存未跟踪目录必须保留且排除本任务暂存：本目录下五个
`henon_mu3_yukawa_mark_*` 包，以及仓库根的
`henon_ermakov_pinney_isotonic_action_route_a/`、
`henon_flat_magnetic_torus_landau_route_a/`、
`henon_hysteretic_relay_oscillator_route_a/`。
精确旧清单在上一版 Git 状态和 C394–C398 批次记录；不要宽泛清理。
其他研究流只在用户本次仓库指令审计范围内审查，不推进其科研批次。
