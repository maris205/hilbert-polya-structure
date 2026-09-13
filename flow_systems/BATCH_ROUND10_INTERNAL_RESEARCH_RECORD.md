# Round 10 内部研究记录：P29–P33

记录日期：2026-09-07 UTC。用途：整理已有研究工作，暂不发表。当前不继续逐项收集投稿相关作者声明，不启动新的审查、科学实验或论文构建。

本批已形成五套研究定义／证书方法架构；P32 另有条件引理及形式定义的证明文字，P33 留有有限合成样例诊断。它们可以作为内部研究产物保存，但不合并表述为已经完成的 owner 普查、物理行列式、覆盖恢复定理或算术性结果。

## 记录依据

现稿版本取自 [当前五篇输入索引](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_REPORT_INPUTS.json)：P29 R6、P30 R5、P31 R6、P32 R6、P33 R4。下面“已形成”指指定文本或本地材料已存在；本轮仅摘录与整理，不重新认证全部数学有效性、来源适用性、实验复现或新颖性。

工作范围变更及此前实际答复保存在 [处置草案 D 节](BATCH_ROUND10_STAGE4_5_ROUND4_DISPOSITION_DRAFT.md)。旧批次汇总、旧 PDF 或现稿中保留的历史阶段标签不替代上述输入索引，也不作为当前审查通过的依据。

## 五项工作的现有产物与开放问题

| 课题 | 已形成、可记录的工作 | 尚未建立的项目结果 |
| --- | --- | --- |
| P29：level-(3) Gaussian Bianchi 流 | 固定时钟、primitive owner 与一个字面高斯素理想的严格输出类型；把机制准入 Gate M 与商集完备 Gate Q 分开；列明五类账本／重播接口的职责。[现稿 B0009][p29-object]、[B0058–B0061 定位入口][p29-gates]、[接口规范][p29-interfaces] | 尚无已获准 owner 机制、完整商集、碰撞分离性能或科学重播结果。严格输出类型是压力测试，不是典范性证明；缺少机制也不证明普遍不可能。[结果边界][p29-limits] |
| P30：三圆盘物理屋顶与转移行列式 | 固定 `d=6a`、欧氏飞行时间及轨道记账；形成六模块架构，其中非转移模块尚未激活；将四项数值误差与几何／屋顶输入不确定性分开；明确单位屋顶、循环标签对称及邻近几何控制。[对象规范][p30-object]、[方法与误差架构][p30-gates]、[控制设计][p30-controls] | 尚无点态物理屋顶构造、算子定理、共同系数映射、行列式数值、误差包络或物理忠实度比较。预设比较窗与阈值不是运行结果；内部公式一致也不确认物理对象。[结果边界][p30-limits] |
| P31：有向 level-11 owner 账本 | 区分总处置函数 `delta`、已解决域上的 `kappa` 和全体闭合条件 `X_res=X`；明确规范化双条件目标及不同输出 `G/I/C`；9,453 个无序异输入对只承担派生字节／记账审计。[核心契约][p31-map]、[成对表限制][p31-pairs]、[G/I/C][p31-gic] | 138 个输入、55 个来源组是固定设计总体，不是 owner 普查结果。尚无规范化定理、完整 owner 分割或实际 `G/I/C` 表；同源规范字节产生的成对表不是独立语义真值。[现稿摘要与执行边界][p31-abstract] |
| P32：纯亏格二同调覆盖重整化 | 固定 `1/N` 时间缩放和 `1/N³` 对数乘积归一化；以高 content／零 content 为先；已有条件标量引理、形式载体／映射定义及兼容性证明文字。[固定框架][p32-frame]、[条件引理][p32-lemma]、[形式定义][p32-formal] | 项目覆盖因子仍未从 deck action、分量数和本原提升推导；尚无实际 ownerwise 比较、全局障碍、恢复结论、紧集上一致尾界或极限交换结果。形式载体已定义不等于项目因子已进入该载体。[应用边界][p32-limits] |
| P33：两固定亏格二曲面的共同证书 | 已写明共同 owner-certificate 语义和分别适用于 BP／CP 的枚举契约；允许不同内部 producer，要求共同证据接口；保留 14 个合成 fixture 的旧诊断记录。[共同接口][p33-interface]、[BP 契约][p33-bp]、[CP 契约][p33-cp] | 尚无生产版完整普查或 producer 完备性证书；固定 `Lambda=21/10` 下的目标空／控制非空仍是未完成证据链的条件方向。合成样例一致不能用于曲面间算术性比较。[科学结果边界][p33-limits] |

## P32：已有推导文字应单独保存

现稿给出的条件标量结论为：当 `ell > 0`、实数 `s > 0`、整数 `m >= 2` 时，

\[
\Phi_m(s)=\bigl(1-e^{-s\ell/m}\bigr)^{-m}
>
\bigl(1-e^{-s\ell}\bigr)^{-1}=B(s).
\]

现稿的短证明令 `x = exp(-s ell/m)`，从 `0 < x < 1` 和 `(1-x)^m < 1-x < 1-x^m` 取倒数得到比较。这里登记的是已有条件引理与证明文字，不是本轮新作的证明或重新审查；对应 [现稿 B0060][p32-lemma]。

形式部分已写出有限 owner／次数商 `R_{F,D}`、逆极限载体 `R_+`、单 owner 投影、局部化与有限标量映射，并将零 content 放在独立标记的 Hahn 纤维内。[定义与状态表][p32-formal]和[兼容性证明文字][p32-proof]可继续作为推导材料使用。

必须同时保留应用条件：只有项目覆盖因子另行导出，并进入所声明的载体与有限标量定义域后，该比较才能用于对应 owner 的因子检验。单 owner 投影不共同检测混合 owner 单项式，不能由局部投影相符推出全局乘积恢复；AN-1–AN-5 仍是解析义务。[投影及应用限制][p32-limits]、[解析义务][p32-analytic]。

## P33：既有有限合成诊断

以下数字摘自 2026-09-04 的 [fixture oracle][p33-oracle] 与 [保留的执行回执][p33-receipt]，本轮没有重跑 harness：

| 既有记录字段 | 数值／状态 |
| --- | --- |
| 合成样例总数 | 14：2 个 valid、12 个 invalid |
| 与预设 oracle 一致 | 14／14；记录中的 harness failures 为 0 |
| 实际终态 | 2 accepted、8 rejected、2 not_evaluable、2 bounded_incomplete |
| bounded_incomplete 对应文件 | `incomplete_coverage.json`、`unresolved_cutoff.json` |

该套 fixture、oracle、harness 来自同一生成谱系。记录只能说明这些有限样例与该预设规则相符，不证明契约正确、验证器独立、生产器可靠、候选总体完整或数学结果成立。BP／CP 契约均保留 `CONTRACT_ONLY_NO_PRODUCER_RUN`，不能把输入覆盖摘要当作本次观察输出。

## 研究待办，不是已执行结果

下面按课题列出已有契约中的下一类开放义务，不排序、不自动启动：

- P29：分别补全候选机制的准入论证和完整 primitive／conjugacy／inversion 商集证书，再谈性能指标。
- P30：从固定物理几何建立屋顶与对象映射，随后处理算子、共同系数和共同范数误差条件；控制比较须与这些前提对齐。
- P31：实现可重播的证书与规范化验证，并解决所有输入的闭合；不能用 9,453 对字节比较替代缺失的语义判定。
- P32：先推导正 content 与零 content 的覆盖因子，再检验局部比较；局部前提成立后，才处理 content-one 分支和全局／紧集一致分析。
- P33：先完成来源／假设充分的目标与控制证明链，再实现 producer 和独立 checker；合成诊断不能替代完整候选域与普查证书。

## 记录方式与保留事项

后续内部记录以“已有定义／推导、实际执行及输入、观察结果、证据限制、失败记录、开放问题”为主。没有执行的步骤写明未执行，没有建立的结论保留为目标或条件命题。不因暂不发表而抹去来源、方法或强度限制，也不再以资助、利益冲突、贡献声明的逐项确认打断普通内部整理。

当前正式审查仍以 [Recovery3 交接记录](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_STATUS.md) 和 [完成报告](BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_COMPLETION_REPORT.json)为准：审查产物已完成，五篇完整性仍为 `FAIL / BLOCK`。作者答复采集已有后续记录，但旧报告不回写；13 项证据／措辞建议与 5 项历史 E6 待处置保留。本次切换用途不是完整性放行、Route 评估、公开发布或 Stage 5／6 授权。

本轮产出仅为本内部记录及处置草案中的范围变更追加。未改现稿、文献库、报告、锁、回执、代码、实验或结果文件；未联网、重跑科学程序或构建论文。核对限于记录的文件定位、摘录关系、数字抄录和追加保全，不是科学复核。

[p29-object]: /root/autodl-tmp/flow_systems/papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round6.tex:54
[p29-gates]: /root/autodl-tmp/flow_systems/papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round6.tex:266
[p29-interfaces]: /root/autodl-tmp/flow_systems/papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round6.tex:353
[p29-limits]: /root/autodl-tmp/flow_systems/papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round6.tex:399
[p30-object]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round5.tex:54
[p30-gates]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round5.tex:460
[p30-controls]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round5.tex:504
[p30-limits]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round5.tex:676
[p31-map]: /root/autodl-tmp/flow_systems/papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round6.tex:511
[p31-pairs]: /root/autodl-tmp/flow_systems/papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round6.tex:662
[p31-gic]: /root/autodl-tmp/flow_systems/papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round6.tex:716
[p31-abstract]: /root/autodl-tmp/flow_systems/papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round6.tex:40
[p32-frame]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:102
[p32-lemma]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:531
[p32-formal]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:720
[p32-proof]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:811
[p32-limits]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:833
[p32-analytic]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:904
[p33-interface]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round4.tex:397
[p33-limits]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round4.tex:565
[p33-bp]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
[p33-cp]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[p33-oracle]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixture_oracle_manifest.json
[p33-receipt]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/serialized_fixture_validation_receipt.json

## 后续内部笔记

- 2026-09-07：[P32 候选覆盖因子到条件比较的推导链](papers/32-homology-cover-renormalization-uniformity/notes/internal_factor_derivation_chain_20260907.md)。已将候选阶数、分量数、周期、归一化指数、有限标量域与 AN-1–AN-5 的前提逐项对应；保持正／零 content 分离和固定阶乘序列。此项是现有材料的衔接整理，不是新完成的覆盖因子推导、实验或障碍结论。
- 2026-09-07（后续）：[P32 纯同调覆盖局部因子的条件推导](papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md)。新增从规定覆盖的纤维返回到循环／本原提升轨道、最小周期、原始有限乘积、两项归一化及有限形式代表的条件证明，正／零 content 分开；在这些假设下接上有限条件比较。尚未落实具体 owner、输入证书或全局分析义务，不改变旧稿与正式审查状态。
- 2026-09-08：[P32 显式非真幂代表族与本原测地线的连接](papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md)。给出 `g_d=a_1^d[a_1,b_1]` 的群论与同调证明，连接固定度量下的本原轨道和符号最小周期，并在既有覆盖／因子约定下推得 `g_2`、`g_0` 的局部因子及同 owner 形式系数差异。没有执行冻结 panel、认证数值长度或建立全局障碍，也不改变论文及正式审查状态。
- 2026-09-08（后续）：[P32 形式产品构造与阶乘序列的两类极限行为](papers/32-homology-cover-renormalization-uniformity/notes/internal_formal_product_limits_20260908.md)。在既有 `R_+` 中明确构造正 content 产品，证明沿 `N_k=k!` 收敛到非基准形式极限；在固定零 content owner 的既有 Hahn 赋值拓扑中证明相应阶乘序列非柯西。结果不扩展为全 owner 标量产品或解析尾界结论，论文、锁定材料及正式审查状态不变。
- 2026-09-08（再续）：[P32 辅助分量记录与连续读出下的恢复极限障碍](papers/32-homology-cover-renormalization-uniformity/notes/internal_componentwise_recovery_obstruction_20260908.md)。新增只并列保留既有分量的辅助拓扑空间，证明其固定阶乘记录序列没有极限，并给出向其他空间传递这一障碍所需的固定、精确、连续读出条件。该辅助判准尚未等价于原项目的全部解析恢复目标；不新增跨零 owner Euler 乘法、全局标量映射或正式放行。
- 2026-09-08（标量桥梁）：[P32 有限标量求值的形式拓扑不连续性与延拓障碍](papers/32-homology-cover-renormalization-uniformity/notes/internal_scalar_topology_bridge_obstruction_20260908.md)。在明确的继承形式拓扑与通常复数拓扑下，用合法多项式序列证明非空正有限域、固定零 owner／模数域的求值不连续，排除整个指定有限域上的连续延拓；以有理常数另证精确反向读出的障碍。保留空正 owner 集例外和特定有限因子序列的稳定性，不把拓扑反例当作数值 Euler 产品发散或正式 Route 结论。
- 2026-09-08（零分支标量增长）：[P32 零 content 局部因子的显式标量增长界](papers/32-homology-cover-renormalization-uniformity/notes/internal_zero_content_scalar_growth_20260908.md)。对同一个零 owner 的明确实函数直接证明沿模数增长（尤其冻结阶乘序列）趋于正无穷，给出 `exp(s ell/2)(N/(s ell))^N` 的精确渐近及正实紧区间上的显式相对／绝对误差。保留覆盖与因子约定前提，不改变冻结归一化，不声称全 owner 产品发散或正式放行。
- 2026-09-08（零分支复求值）：[P32 零 content 有限因子的复求值与紧集增长](papers/32-homology-cover-renormalization-uniformity/notes/internal_zero_content_complex_growth_20260908.md)。对同一个零 owner 的既有有限复求值，证明右半平面固定紧集上的模长发散及无复对数分支的统一相对渐近；保留复相位，并单列其他复因子可能模小于一的传递限制。未建立几何复对数归一化、全 owner 乘积或 AN-1–AN-5，正式状态不变。
- 2026-09-08（有限层整合）：[P32 有限 owner 标量层的复对数连接与分类](papers/32-homology-cover-renormalization-uniformity/notes/internal_finite_owner_scalar_classification_20260908.md)。完成条件有限几何乘积的全纯对数连接、固定有限集合的 content-one／高 content／零 content 分类及混合渐近误差；在正实轴进一步证明保留指定零 owner 的任何有限截断族均发散，保留指定 content-two owner 的相对比值则有统一正差距。仍限于明列有限公式及条件输入，不构造全 owner 乘积、不改变冻结方案或正式审查状态。
- 2026-09-08（正族穷尽与无限接口）：[P32 正 content 见证族的长度控制与穷尽障碍](papers/32-homology-cover-renormalization-uniformity/notes/internal_positive_content_exhaustion_obstruction_20260908.md)新增基点环路到物理周期的线性上界，证明无需零 owner、只要最终保留既有全部正 content 族成员，有限截断就沿阶乘层数在正实紧区间上绝对及相对发散；并给出稳定正乘积普通截断求值与全正对数统一 majorant 的障碍。[标量无限乘积接口](papers/32-homology-cover-renormalization-uniformity/notes/internal_scalar_infinite_product_interfaces_20260908.md)另行建立允许无穷的实序对象和两极限关系、带明确可求和假设的全纯产品及增长集合的条件复域估计。未认证实际 owner 枚举或求和前提，不改变归一化、论文、AN 状态或正式审查结论。
- 2026-09-08（几何前提落实）：[P32 几何同调覆盖塔、长度截断与固定层乘积](papers/32-homology-cover-renormalization-uniformity/notes/internal_geometric_tower_and_length_cutoff_20260908.md)从固定真实标记双曲曲面证明 H1 抽象覆盖及整除塔，建立长度截断有限性、共尾性、粗计数与指数尾界；在 `Re(s)>N` 构造固定层非零全纯产品并接通全部覆盖本原轨道的几何对数归一化。既有正 content 族的实轴障碍由此适用于任意趋向无穷的数学长度截断。未认证具体矩阵、数值常数或规范枚举，不声称共同固定参数域、精确收敛边界或谱行列式，正式状态不变。
- 2026-09-08（精确阈值与移动参数）：[P32 未缩时覆盖乘积、精确阈值与移动参数主项](papers/32-homology-cover-renormalization-uniformity/notes/internal_unscaled_cover_products_and_moving_parameter_limit_20260908.md)初等证明全体正 content 的统一物理长度界；借用指定外部素测地线定理，确定完整普通乘积的精确阈值及相对产品的 `N=1` 例外。在移动参数 `s=Nw`、`Re(w)>1` 下证明正分支指数趋一、全乘积具有零同调子乘积 `B_0(w)^N` 的统一相对主项，并给出有限字符分解、Haar 日志平均及两种长度截断精度条件。辅助覆盖度数归一化不替换冻结方案，未构造谱行列式、数值证书或固定参数恢复，正式状态不变。
- 2026-09-08（零同调临界边界）：[P32 零同调临界边界、正分支发散与对数偏移渐近](papers/32-homology-cover-renormalization-uniformity/notes/internal_homology_zero_critical_boundary_20260908.md)核对并导入固定零同调类计数展开，证明零函数在 `w=1` 的有限值、一阶连续性、二阶对数奇性及局部非亚纯延拓障碍；补齐正／零分支精确有限值区域和 `N=1` 相对例外。证明正分支层数／临界极限不交换；在充分条件 `K>2M` 下给出 `s=N+K log N` 的指数乘幂次主项，并证明纯零分支临界截断相对精度的平方根尺度判准。未将充分偏移阈值称为最优、未判定整条自然边界、未把纯零截断用于临界完整无穷乘积；保留固定几何常数范围、原归一化、冻结输入及正式状态。
- 2026-09-08（收缩临界层与分数阶）：[P32 收缩临界层、最大重数分支与分数阶奇性](papers/32-homology-cover-renormalization-uniformity/notes/internal_shrinking_critical_layer_and_fractional_singularity_20260908.md)定位正分支临界困难于非零 `NZ^4` 同调的最大重数单重复项；在新核对的 Sharp 全同调类一致局部极限定理支持下，证明固定 `u>0` 的 `s-N>=u/sqrt N` 移动半平面相对主项，得到固定／趋零偏移实轴渐近，并将旧对数偏移结论扩展到全部固定 `K>0`。另从每个固定覆盖曲面的 PGT 余项导出原归一化产品的 `1/N^3` 临界发散阶及 `N>=2` 局部非亚纯延拓障碍，精确保留 `N=1` 的完整简单极点、正分支非延拓和相对恒一例外。未把充分收缩尺度称为最优，未将固定层常数用于任意对角线，未改冻结对象、论文或正式状态。
- 2026-09-08（指数临界过渡）：[P32 全局同调 Gaussian 界与指数临界过渡](papers/32-homology-cover-renormalization-uniformity/notes/internal_exponential_critical_crossover_20260908.md)以小同调锥一致相对渐近、加权原始轨道固定窗指数率及几何支持界闭合全局 Gaussian 上界，再由格点和与稠密格点一致计数证明移动半平面零同调主项的充要判准 `log_+(1/epsilon_N)=o(N^3)`。在实轴临界量 `N^(-3)log_+(1/(epsilon_N N^2))` 趋于有限 `lambda>=0` 时，正分支比值趋于 `exp(lambda)`；尤其 `s_N=N+N^(-1)exp(-lambda N^3)` 的完整／相对原乘积除以 `B_0(1)^N` 均趋于 `exp(lambda)`。保留实轴与复域区别、量发散时仅日志等价、未知误差速率和精确临界点发散；不偷换固定覆盖渐近常数，不认证数值或谱行列式，不改冻结归一化、论文与正式状态。
- 2026-09-08（复临界与相位）：[P32 复临界过渡、零分支相位与切向限制](papers/32-homology-cover-renormalization-uniformity/notes/internal_complex_critical_crossover_and_tangential_limits_20260908.md)区分正分支的径向主项和法向误差，证明有界法向指数域中的一致相对轮廓及双指数逼近的 `exp(min(a,b))` 极限；把零同调展开推进到闭右半圆的 `z^2 Log z` 形式，得到固定非零原虚偏移的 `exp(i D_*theta)` 相位及相应非交换极限。用明确标记的抽象余项诊断说明任意极端切向不能仅由误差大小控制推出，并列出尚未建立的加权可积性义务；不将该诊断当作真实流反例，不更改原归一化、冻结输入、论文或正式状态。
- 2026-09-08（可积字符尾项与全径向轮廓）：[P32 字符计数可积尾项与全右半圆径向轮廓](papers/32-homology-cover-renormalization-uniformity/notes/internal_integrable_character_tail_and_global_radial_profile_20260908.md)以 Sharp Lemma 3 的全字符统一逆幂余项为新输入，完成 sharp 本原无权转换、有限字符平均与零类扣除，证明实际 `N^{-3}int_{N³}^infinity |r_N(t)|dt/t=O(N^{-5})`。在 `N²` 处分割后取得全部 `Re z>0, |z|<=1` 上的 `O(N^{-3})` 径向相对轮廓，解除法向指数限制并将径向量趋于无穷时的日志等价升级为乘积相对等价；同时得 `log(kappa_N/B_*^N)=-2log N/N³+O(N^{-3})`。旧抽象诊断与失败记录保留，未把内部证明或机械保全当作正式认证；不含精确临界点，不改冻结方案、论文、Route 或正式状态。
- 2026-09-08（扩散 theta 轮廓与有限部分）：[P32 扩散尺度 theta 轮廓与临界有限部分](papers/32-homology-cover-renormalization-uniformity/notes/internal_diffusive_theta_profile_and_critical_finite_part_20260908.md)将实际模 `N` 同调计数在 `t=N²u` 下的极限推进到全正轴加权 L1 收敛，证明 `N³log(kappa_N/B_*^N)+2log N->C_D`，以绝对收敛 theta 积分和明确标量格点 zeta 导数表达常数。另取得全右半单位圆盘上的 `N^{-3}` 阶复 Laplace 精细轮廓及 `o(N^{-3})` 相对误差，不丢失首阶相位。常数在整数换基下不变，但没有数值认证、跨曲面族统一性或更高阶速率；不构造谱算子，不改原时钟、归一化、冻结输入、论文或正式状态。

## 2026-09-08：五篇完整一轮的内部论证增量

本轮按用户“尽量还是5个论文一整轮，搞完一轮再交互”的最新要求，
将 P29–P33 作为一轮共同推进和集中交接。“五篇完成一轮”指五项有界
内部论证均有新增笔记及复核，不是全部研究目标已完成，也不是新开五篇
论文、正式审查通过或投稿准备恢复。此前针对 P32 的逐次细分记录全部保留。

| 课题与本轮笔记 | 这轮实际形成的结论 | 保留的关键边界 |
| --- | --- | --- |
| [P29：真实本原 owner 上的条件分裂选择障碍](papers/29-bianchi-ideal-owner-refinement/notes/internal_fixed_owner_split_selector_obstruction_20260908.md) | 对旧精确见证矩阵 \(\left(\begin{smallmatrix}1&3\\3&10\end{smallmatrix}\right)\) 新证完整 level-(3) 群内本原性；其 \(D_9=13\) 只有 \((3+2i),(3-2i)\) 两个被 Gaussian 共轭交换的素理想因子。真实共轭不动 owner 排除同时满足“Gaussian 共轭等变”及“从 \(D_9\) 选一个素因子”的规则。 | 两条选择条件是额外前提，不冒充冻结 Gate M 的通用公理；不排除所有字面素理想机制，没有候选登记、Gate M 运行或完整 owner 商。 |
| [P30：两个几何周期与常数 roof 障碍](papers/30-three-disk-nonconstant-roof-determinant/notes/internal_geometric_period_witnesses_20260908.md) | 验证坐标、无阻挡和镜面反射，构造本原周期 \(T_2=8a\)、\(T_3=(18-3\sqrt3)a\)。同一逐碰撞映射上，物理 roof 不共调于任何常数；五个见证状态上的最佳常数加 coboundary 误差为 \((2-\sqrt3)a/2\)。 | 主对象仍取冻结 \(a=1,d=6\)；不推出一般算子不相似或行列式不等，不激活 Gate 6。二碰撞自反向只提示 reverse-link 的条件性实现澄清，不自行变更 owner 规则。 |
| [P31：有限分割证书与 G/I/C 下降](papers/31-level11-conjugacy-owner-ledger/notes/internal_certified_partition_and_gic_descent_20260908.md) | 证明区块内正关联／区块间语义分离与受限 pair-evidence 模型的尖锐证据数界；给出有限整数递推本原根判定，并以模 11 平方剩余排除 hyperbolic owner 自逆共轭；精确构造 \(I\to G,C\) 及 cell-owner 细商。 | 未读取并重新处理 138 个实际输入，没有 9,453 行执行结果。一般代表间非共轭、实际 inverse links、全域 canonical bytes 及生产 verifier 仍待建立；有限数据集标签不替代冻结契约。 |
| [P32：压力偶对称与 theta 定量误差](papers/32-homology-cover-renormalization-uniformity/notes/internal_quantitative_theta_error_and_pressure_symmetry_20260908.md) | 从唯一实极点推出 \(s(-\theta)=s(\theta)\)，以四阶字符格点估计及端点分割证明 \(\rho_N=O(N^{-2}(\log N)^3)\)。临界振幅对数和完整右半单位圆盘的精细产品相对误差推进到 \(O(N^{-5}(\log N)^3)\)。 | 使用同一固定曲面的既有 Gaussian、PGT 与有限部分输入；不声称对数因子必要、误差最优、数值常数认证或跨曲面族统一性。不包含精确临界点，不构造谱算子。 |
| [P33：固定截止值分离与两个控制短字](papers/33-bolza-control-matched-census/notes/internal_cutoff_separation_proof_obligations_20260908.md) | 将冻结矩阵与公开几何原文逐项对应；结合 Bolza systole 定理与精确有理数比较，证明 \(\mathcal O_B(21/10)=\varnothing\)。控制词 \(g_0g_3\)、\(g_1g_2^{-1}\) 同迹、长度严格小于 \(21/10\)，但本原同调向量互非正负，故 \(\#\mathcal O_C(21/10)\ge2\)。 | 外部曲面构造／标记和 systole 定理是明列输入，不宣称本轮重证。控制下界不是完整 census 或精确 systole；不运行 BP／CP、填覆盖摘要或提高 P33-RC-1 实现数，不用于算术性或磁性推断。 |

### 两项需要明确记录的解析／几何结果

P32 沿用上一轮已经确定的 \(C_D\)、\(B_*\)、\(\kappa_N\)，得到

\[
\log\frac{\kappa_N}{B_*^N}
=\frac{-2\log N+C_D}{N^3}
+O\!\left(N^{-5}(\log N)^3\right).
\]

同一误差阶适用于完整复 Laplace 轮廓归一化后的产品相对误差，
而不是把复对数换成模长后的径向近似。实解析唯一极点来自本轮核读的
[Sharp 作者稿 Proposition 1](https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/gauss.pdf)；
明确 N 速率是本笔记的推导，并非该来源的原陈述。

P33 的 Bolza 模型及 systole 输入来自
[Ebbens 等作者稿 §2.4、Theorem 2](https://arxiv.org/pdf/2103.05960)；
控制的参数域、曲面群标记和生成元来自
[Nazarenko 作者稿 §2、Eqs. (10)–(18)](https://arxiv.org/pdf/1301.5446)。
新笔记分别列出来源陈述、冻结输入的公式对应和本轮自含代数／同调推导，
不沿用历史“已证控制 systole”的状态标签来代替本原性证明。

Bolza 作者 PDF 的 Lemma 9 文本提取有一个因子二不一致，
相关截图请求及 DOI 出版页打开各失败一次，均保留且未换通道重试。
该局部计算未用于本轮证明；采用 Theorem 2 的明示陈述，
不宣称逐页重证或出版版核验。原 S02 的访问缺口不被本轮其他来源清除。

### 本轮动作、复核和保全范围

主线程负责 P29、P32 与批次整合；三个分工分别只写 P30、P31、P33 的
一份新笔记。主线程阅读全文并核对核心推导；另对 P29 的本原性／条件障碍、
P32 的误差估计和 P33 的短字／来源桥作跨分工只读复核。
代理间的相符意见不是独立科学证据或正式证明认证。

实际工作为本地只读定位、纸面推导、按需普通公开一手浏览、五份新笔记，
以及向本入口追加本节。没有运行数值或符号代数程序、科学枚举、fixture、
历史 artifact writer、论文构建、正式审查或 Route evaluator。
工作区的 git status 返回非 Git 仓库；没有修改 Git 配置或发起同步。
一次旧 P24 candidate_lock.md 路径查询无该文件，随后直接读取实际现稿的
群定义与旧代码中的明确矩阵常量，没有建立新锁或执行该代码。
首次入口追加请求因编排字符串中的反引号触发 JavaScript 解析错误，
在任何工具执行及文件写入前失败；修正字符串后重试，失败记录保留。

写入前于 **2026-09-08 14:00:43.399 UTC** 对五篇目录及根目录
BATCH_ROUND10* 文件建立了 **3,327 个原文件**的只读字节快照。
本轮交接检查覆盖五份新笔记的链接、数学环境、文本完整性和全部原文件保全；
其中本入口唯一允许的旧文件变更是保持原 **23,901 bytes** 前缀的追加。
这些检查用于检验改动范围与可读性，不建立数学有效性。

旧稿、书目、协议、输入锁、正式状态及失败记录不回写；
此前正式五篇 FAIL / BLOCK 和 Stage 5／6 边界保持不变。
这轮完成后仍按五篇一轮组织后续内部研究，不因其中一篇走得更快
而默认把其余四篇跳过；也不为凑齐数量把未证前提写成结果。

## 2026-09-08：第二次五篇整轮内部论证——无限族、有限判定与首修正

本轮由用户“确认，下一轮”启动，继续遵守“五篇一整轮完成后集中交接”。
范围仍是 P29–P33 的有界内部理论、按需普通公开一手浏览、各一份新笔记，
以及向本入口追加记录；不是新的实验授权、正式审稿恢复或 Stage 5／6 放行。

| 课题与新增笔记 | 本轮闭合的具体问题 | 保留的边界 |
| --- | --- | --- |
| [P29：无限本原分裂障碍族](papers/29-bianchi-ideal-owner-refinement/notes/internal_infinite_primitive_split_obstruction_family_20260908.md) | 对所有 \(n\ge1\)，矩阵 \(A_n=\left(\begin{smallmatrix}1&3\\3n&1+9n\end{smallmatrix}\right)\) 在完整 level-(3) 群内本原。取 \(n=25^k\) 得无限多个不同的共轭不动 owner，每一个的 \(D_9\) 都无 Gaussian 共轭不动素理想因子，故逐点排除 E+D 选择。子族计数为 \(L/(2\log25)+O(1)\)。 | E（Gaussian 共轭等变）与 D（选择 \(D_9\) 素因子）仍是额外条件；不是任意字面素理想机制的普遍不可能，不改冻结公理，不给全体 owner 密度或 Gate M／Q 执行结果。 |
| [P30：无共同时间格与真实 roof 正则性](papers/30-three-disk-nonconstant-roof-determinant/notes/internal_nonlattice_periods_and_roof_regularity_20260908.md) | 从两条精确周期证明所生成加法群稠密及无共同时间格；给出二次范数整数差下界和 \(1/|\omega|\) 两周期相位下界。首撞域的几何排他性使显式平方根确为真实 roof，并在非擦边子域给实解析性与有效全阶角导数界。 | 稠密的是允许正负系数的加法群，不是实际长度谱。仍存在任意大的近似同时共振频率；不推出完整符号编码、全被困集非擦边界、mixing、谱隙或 determinant，也不改 reverse_id。 |
| [P31：环境共轭到十二状态子群判定](papers/31-level11-conjugacy-owner-ledger/notes/internal_finite_coset_conjugacy_reduction_20260908.md) | 在已证环境共轭 \(H_0PH_0^{-1}=Q\) 及环境本原根 R 下，全部共轭子为 \(\pm H_0R^n\)；level-11 membership 等价于 \(\mathbb P^1(\mathbb F_{11})\) 的至多 12 状态闭合轨道命中。给出精确正／负证书、本原指数关系与两手算防错例；一个手造环境共轭类恰分成 12 个子群共轭类。 | 12 是不同状态数上界，不要求周期整除 12。环境本原根不可用子群本原元代替；尚未实现环境共轭决策、完整 verifier、138 输入或 9,453 pairs，手造类的 12 不冒充冻结人口结果。 |
| [P32：首 theta 修正与无对数损失速率](papers/32-homology-cover-renormalization-uniformity/notes/internal_first_theta_correction_and_log_free_rate_20260908.md) | 由六阶压力余项与固定 p=5 字符 PGT，识别零类次系数及首修正 H；其连续积分项恰被实际零类扣除。证明全正轴加权展开余项 \(O(N^{-4}(\log N)^4)\)，并得 \(\rho_N\sim N^{-2}\|H\|_{1,*}>0\) 意义下的明确首系数；临界振幅出现 \(N^{-5}K_{D,P}\)，全复域二阶产品轮廓误差为 \(O(N^{-7}(\log N)^4)\)。 | 范数常数为正，不代表有符号 \(K_{D,P}\) 非零；只对指定 \(\rho_N\) 证明精确幂次，不宣称所有产品误差或二阶余项最优。常数未数值认证，不改变固定几何、归一化或精确临界点定义。 |
| [P33：严格余量与固定对象证书稳定性](papers/33-bolza-control-matched-census/notes/internal_strict_cutoff_margins_and_sound_admission_20260908.md) | 控制迹截止余量 \(>74/1195\)，Bolza 全局绝对迹余量 \(>3/10\)，并有真实长度余量。证明同一精确对象的有效区间达到指定宽度后必给严格 admission／全局排除；两因子 entry 及运算误差各 \(\le1/1024\) 是一个充分预算。 | 区间宽度不等于误差半径，近似矩阵不替换真实群元素。精确 ambient 群条件和 relator 也不单独建立固定群忠实标记；局部可靠入选、候选零命中和完整 census 是不同责任。未运行 BP／CP、interval checker 或提高实际实现数。 |

### P32 的新增系数与更高阶轮廓

新笔记使用原压力函数
\(s(\theta)=1-\tfrac12\theta^{\mathsf T}D\theta+s_4(\theta)+O(|\theta|^6)\)，
记 \(q(x)=2\pi^2x^{\mathsf T}Dx\)、\(P(x)=s_4(2\pi x)\)。同一个
Haar 字符平均确定真实零类次系数

\[
c_1=\int_{\mathbb R^4}(1+q(x)+P(x))e^{-q(x)}\,dx,
\qquad
H(u)=\sum_{k\in\mathbb Z^4}
(q(k)+uP(k)+u^{-1})e^{-uq(k)}-c_1u^{-3}.
\]

对多项式 Gaussian 使用 Poisson 求和，零 Fourier 项恰为
\(c_1u^{-3}\)，所以 H 在零端指数小；在无穷远
\(H(u)=u^{-1}-c_1u^{-3}+O((1+u)e^{-bu})\)。
因此 \(\|H\|_{1,*}\) 有限且严格为正，而
\(K_{D,P}=\int_0^\infty H(u)\,du/u\) 绝对收敛但可能为零。

本轮主式是

\[
\int_0^\infty|F_N-F_D-N^{-2}H|\,\frac{du}{u}
=O(N^{-4}(\log N)^4),
\]

\[
\log\frac{\kappa_N}{B_*^N}
=\frac{-2\log N+C_D}{N^3}
+\frac{K_{D,P}}{N^5}
+O(N^{-7}(\log N)^4).
\]

原全开右半单位圆盘的二阶复轮廓含
\(\mathcal L_{D,P}(a)=\mathcal J_H(a)+a\mathcal J_D(a)\)，
\(a=N^2z\)。第二项不可漏掉，它来自精确计数积分的 \(1+z\) 前因子。
对 \((H/u)'\) 单独证明绝对可积后，交叉项
\(N^{-4}a\mathcal J_H(a)\) 也能在任意切向逼近中统一控制。
只保留旧首阶复轮廓时，相对误差已经改进为无对数的 \(O(N^{-5})\)。

外部基础输入仍是
[Sharp 作者稿的实解析极点及既有字符估计](https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/gauss.pdf)
和 [DLMF Poisson 公式 1.8.14](https://dlmf.nist.gov/1.8#E14)；
本轮的系数识别、四维余项和 N 速率是新增推导，不冒称为来源原定理。
本轮首次 Sharp 作者稿打开成功并读到 Proposition 1；
其后 open／find 的段落定位出现工具 Internal Error，失败保留，
未重新取 PDF、截图、出版页或换通道重试。p=5 的使用依赖此前已记录的
“每个固定 p”字符转换，而不是将这次定位失败报成新核验成功。

### 五篇的复核、实际动作与保全范围

主线程写 P29、P32 和本追加节，三个分工各自只写 P30、P31、P33
的一份新笔记。主线程完整核读全部新文及核心推导；
交叉只读复核分工是 P30 检查 P29、P31 检查 P32、P33 检查 P30。
这些意见用于检错，不构成独立科学证据或正式同行认证。

ARS 有界论证流程促使本轮明确保留额外条件、环境／子群之别、
零类系数的来源、固定对象的区间语义以及完整性责任。
只做本地只读定位、纸面证明、普通公开来源浏览和六个精确目标的编辑。
未运行矩阵／符号代数程序、科学枚举、数值积分、实验、历史 artifact
writer、fixture、论文构建、正式审查、Route evaluator 或远程写入。

P30 分工的一次旧技能路径少写目录查询失败及非 Git 工作区查询，
已在其新笔记保留；定位实际路径后完整读取，未修复 Git 或改配置。
P33 不新增来源请求，保留前轮 systole 局部 PDF 提取／截图／DOI 失败，
不重试并不使用有争议段落；实际采用的全局定理及模型绑定仍按前轮明列。
没有任何失败被回填为成功，没有刷新科学 receipt 掩盖状态差异。

本轮写入前于 **2026-09-08 14:59:02.328 UTC** 对五篇目录及根目录
BATCH_ROUND10* 普通文件建立 **3,332 个原文件**的字节／SHA-256 快照。
交接检查范围为：五篇恰各新增一份笔记，全部 **3,331 个其他原文件**
保持字节不变；本入口只允许保留原 **31,009 bytes** 前缀的追加；
另检查新文的本地链接、数学环境、控制字符、文本完整性及末尾换行。
这些机械检查不建立来源充分性或数学有效性。

旧稿、书目、冻结输入、protocol、正式回执、失败记录和原有
FAIL / BLOCK 均不回写；不改变 Route 判定，不恢复 Stage 5／6。
本轮完成只表示五项有界内部论证均已形成可核读增量，不表示五篇
总目标、生产证书、正式审查或投稿资格已经完成。

## 2026-09-08：第三次五篇整轮内部论证——选择判准、全局正则性与有限覆盖

本轮由用户再次“确认，下一轮”启动，仍以五篇全部形成有界增量后集中交接。
授权只覆盖内部理论、按需普通公开一手浏览、五份新笔记及本入口追加；
不是实验、生产证书、正式审查恢复、Route 改判或 Stage 5／6 放行。

| 课题与新增笔记 | 本轮闭合的具体问题 | 仍保留的边界 |
| --- | --- | --- |
| [P29：不动素理想分类与选择判准](papers/29-bianchi-ideal-owner-refinement/notes/internal_fixed_prime_classification_and_selector_criterion_20260908.md) | 完整分类 Gaussian 共轭不动素理想：ramified 的 \((1+i)\) 与 \(p\equiv3\pmod4\) 的 \((p)\)。对任意共轭稳定 owner 子域 Y，抽象 E+D 选择存在，当且仅当每个不动 owner 的 \(D_9\) 有这类素因子。对 \(n=m^2\)、m 为奇数的已证本原族，判准恰为 m 含一个 \(3\bmod4\) 素因子。 | 只谈额外 E+D 条件；抽象良序选择不等于已登记、可计算或自然机制。坏族仍阻断全体 owner 上的 E+D，允许子族不改冻结定义或正式 verdict。 |
| [P30：全被困碰撞上的统一非擦边](papers/30-three-disk-nonconstant-roof-determinant/notes/internal_uniform_nongrazing_on_trapped_collisions_20260908.md) | 不预设非擦边，从真实双向被困碰撞的入／出射方向锥推出 \(\chi\ge\kappa_*=(2\sqrt6-1)/6>1/2\)。由此将旧局部全阶 roof 导数界统一化，并在 \(d_a((q,v),(\tilde q,\tilde v))=\lVert q-\tilde q\rVert+a\lVert v-\tilde v\rVert\) 下证明全碰撞被困集上 roof 的 Lipschitz 常数可取 105。 | 明确区分真实首撞分支、被困子集与开解析域；不声称整个被困集是解析流形，不自动推出 symbolic Hölder、mixing、谱隙或 determinant，reverse_id 不改。 |
| [P31：环境群 normal form 与共轭正负证书](papers/31-level11-conjugacy-owner-ledger/notes/internal_ambient_normal_forms_and_conjugacy_certificates_20260908.md) | 构造带严格递减终止量的矩阵 Euclidean transcript，保留 SL lift 的中心符号；自含证明 \(PSL_2(\mathbb Z)=C_2*C_3\) normal form。双曲循环约化词共轭当且仅当互为循环移位，给出有限否定检验及精确共轭子重建。接上既有环境本原根与十二状态下降，得到理论上的完整有限子群共轭判定链。 | 标准群论本身不宣称新颖。仅有理论证书格式，没有编写 verifier、绑定 138 输入或运行 pairs；十二状态界只约束最后的子群下降，不能冒充整个算法复杂度上界。 |
| [P32：四次调和投影与对偶格有限部分](papers/32-homology-cover-renormalization-uniformity/notes/internal_harmonic_quartic_finite_part_and_dual_lattice_series_20260908.md) | 完整二阶轮廓中普适二次／Li 项精确抵消，剩下四次加权 theta 有限部分的 Laplace 变换。临界系数 K 消去所有 \(qR_2\) 项，仅依赖四次 Q-调和投影；导出绝对收敛的对偶格级数、显式 \(M^{-2}\) 截尾界及整数基变换不变性。 | K 可以为零；调和投影非零也不单独推出 K 非零。非临界轮廓一般不消去 \(qR_2\)。没有算实际 D、压力四次项、K 的数值或符号，也不提高前轮 N 误差阶。 |
| [P33：短轴到有限 guard 的覆盖](papers/33-bolza-control-matched-census/notes/internal_axis_to_center_coverage_and_finite_guards_20260908.md) | 轴点移入半径 R 的真基本域，给每个长度 \(\le\Lambda\) 的 owner 一个 \(C_{\Lambda+2R}\) 代表。通过线段所交闭 tiles 与顶点完整 star，证明 \(C_S\subseteq C_T^0\) 在 \(T\ge S+R\) 时成立。对冻结 CP 参数，纸面验证 \(R=3\)、\(\Lambda=21/10\) 和原 \(\lvert\alpha\rvert^2\le20000\) guard 满足充分界。 | 覆盖结论依赖真基本域、face-to-face 铺砌及字母完整对应侧邻接；这些输入版本尚未得到实际证书。没有运行 BFS，没有认证历史 18,533 states／depth 11 或完成 owner 商；BP 不改 strict-systole empty-stream 路线。 |

### P32：临界系数的可求和结构

沿用原压力四次齐次项 \(P(x)=s_4(2\pi x)\)，置
\(Q=2\pi^2D\)、\(q(x)=x^{\mathsf T}Qx\)、
\(c_D=\int_{\mathbb R^4}e^{-q(x)}\,dx\) 和
\(\Delta_Q=\sum_{i,j}(Q^{-1})_{ij}\partial_i\partial_j\)。
新的四次调和投影是

\[
P_{\mathrm h}
=P-\frac{q\,\Delta_QP}{16}
+\frac{q^2\,\Delta_Q^2P}{384},
\qquad \Delta_QP_{\mathrm h}=0.
\]

若 \(p_0=\int_{\mathbb R^4}P(x)e^{-q(x)}\,dx\)，则前轮的完整轮廓
\(\mathcal L_{D,P}(a)=\mathcal J_H(a)+a\mathcal J_D(a)\) 恰为

\[
\mathcal L_{D,P}(a)
=\int_0^\infty e^{-au}
\left(\sum_{k\in\mathbb Z^4}P(k)e^{-uq(k)}-p_0u^{-4}\right)\,du.
\]

这里的零 Fourier 项扣除使积分在零端指数小，无穷远为可积幂尾。
在 \(a=0\) 时，\(qR_2\) 的贡献是端点为零的全导数，故
\(K_{D,P}=K_{D,P_{\mathrm h}}\)。将调和四次 Gaussian 的 Fourier
变换逐项积分，得到普通意义下绝对收敛的公式

\[
K_{D,P}
=24c_D\pi^4
\sum_{m\in\mathbb Z^4\setminus\{0\}}
\frac{P_{\mathrm h}(Q^{-1}m)}
     {(\pi^2m^{\mathsf T}Q^{-1}m)^5}.
\]

每项为 \(O(\lVert m\rVert^{-6})\)，四维格点求和绝对收敛。
笔记还给出以可认证系数界和正定性下界表述的
\(32/M^2+4/M^4\) 显式截尾预算；未执行这一级数或提供数值认证。
该公式识别的是前轮临界 \(N^{-5}\) 系数，不是新的 N 速率定理，
也不支持将原格点积分未经论证交换成非绝对可积级数。

### P33：原 guard 的条件性充分性

记 \(C_t=\{g:d(o,go)\le t\}\)，\(C_T^0\) 为以完整侧邻接字母表、
在 \(C_T\) 内可从 identity 到达的分量。所证链是

\[
\{\text{长度不超过 }\Lambda\text{ 的 owner}\}
\longrightarrow C_{\Lambda+2R}
\subseteq C_T^0,\qquad T\ge\Lambda+3R.
\]

关键是保留线段交 tiles 的 \(S+R\) 中心距离界：
顶点退化通过该顶点完整有限 star 内的边邻接路径补齐，不多损失一个 R。
短 translation length 不直接控制原来任意代表的 based displacement，
因此首先共轭移轴这一步不可删去。

在明确的固定 S01 几何／侧邻接前提下，本轮有理估计给出

\[
S=\frac{81}{10},\qquad S+R=\frac{111}{10},\qquad
\cosh^2(111/20)<\frac{159501}{8}<20000.
\]

所以旧 guard 有严格余量，不需要放大 guard 或替换对象。
新文另证明：若有已认证的非恒等元中心分离常数 \(\delta>0\)，
packing 可以给 guard 内状态数、路径长度及边检查数的有限上界。
这仍不提供冻结实际数据上的 \(\delta\)、精确状态身份、所有边展开记录、
一般 root／conjugacy／inverse 证书或最终 census；也不证明任意边界近似
guard 判定都会终止。前轮两因子 entry 误差预算不推广为长字统一预算。

### 来源、复核与保全范围

本轮普通公开来源核对限于
[Keith Conrad 的 SL(2,Z) 讲义](https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf)
中 Theorem 1.1 的生成元与 Appendix C 的 normal-form 背景，
以及 [DLMF §1.8 的 Poisson 公式](https://dlmf.nist.gov/1.8#E14)。
本轮推导与来源背景分别标明，不将新增模型结论冒称为来源原定理。
主线据 PDF 作者栏将 P31 新文中的 Kevin 更正为 Keith。
Appendix C 的 n=1 证明段文本提取出现与 \(x\ne1\) 不一致的句子；
该句不用作论据，P31 的长度一排除由新文自含证明完成。
这里只记录提取问题，不断言原出版文字有误，也不发起截图／重取重试。
旧 Sharp、Bolza 等来源缺口及失败记录没有被本轮请求清除。

主线程写 P29、P32 和本追加节；三个分工分别只写 P30、P31、P33
各一份新笔记。主线程全文核读五篇及核心推导，交叉只读复核为：
P30 检查 P29 与 P31，P31 检查 P32，P33 检查 P30。
分工相符意见用于检错，不作为独立科学证据或正式同行认证。
ARS 的有界 argument-builder 流程促使每篇明确列出数学前提、
构造／证书语义、来源支持和没有完成的实际接口。

实际动作是本地只读定位、纸面推导、上述普通公开浏览、
五份新笔记与本入口追加；只读 Node 检查用于文件／文本／链接完整性，
不是数值或符号代数实验。未运行科学枚举、数值积分、producer、
fixture、历史 artifact writer、论文构建、正式审查、Route evaluator
或远程写入。P31 的非 Git 工作区查询没有改变 Git 配置或触发同步。
没有改写旧稿、书目、冻结输入、协议、正式 receipt 或失败记录。

写入前于 **2026-09-08 15:35:34.868 UTC** 对五篇目录及根目录
BATCH_ROUND10* 普通文件建立了 **3,337 个原文件**的只读字节／SHA-256
快照。交接检查的范围是：恰好各新增一份笔记；
全部 **3,336 个其他原文件**保持字节不变；本入口保留原
**39,212 bytes** 前缀且只追加本节；并检查新文的本地链接、
数学环境、公式编号、文本完整性、控制字符及末尾换行。
这些机械检查不建立数学有效性，也不代替来源或生产证书责任。

此前五篇正式 FAIL / BLOCK、D06 Recovery 3 的停止边界、
Route 判定及 Stage 5／6 限制全部保持不变。
本轮完成表示五项有界内部增量均已落盘，不表示总目标、实际程序、
正式审查或投稿资格已经完成。后续仍按五篇一轮，不自动启动下一轮。

交接检查的技术说明：首次“精确追加”比较器在写入前保存的正文后，
额外假定了第二个末尾换行，因而报出不相等。直接比较实际后缀与
原保存正文，二者逐字相同，旧前缀也完整；修正的是比较器预期，
未改写任何已检查正文、输入或科学回执。本段作为后续追加保留该记录。

## 2026-09-09：第四次五篇整轮内部论证——有限实现、词根与临界解析结构

用户“继续吧”启动本轮，继续按五篇全部形成有界增量后集中交接。
范围仍为内部理论、按需普通公开一手浏览、各一份新笔记及本入口追加。
没有授权或启动实验、producer、正式稿修订、审查恢复、Route 改判、
Stage 5／6、远程同步或公开发布。

| 课题与新增笔记 | 本轮的具体增量 | 不可扩大成的结论 |
| --- | --- | --- |
| [P29：最小对称集合与随机选择](papers/29-bianchi-ideal-owner-refinement/notes/internal_minimal_symmetry_packets_and_randomized_selectors_20260909.md) | 全 owner 域上可给至多两个合法素理想的等变集合；给出仅依赖判别式的逐点最小基数构造及有限整数求值办法。在不动坏 owner 上，任何等变概率分布的最大原子质量至多 1/2、熵至少一比特，等号恰为一个共轭对上的均匀分布。 | 输出类型已从单个素理想改为集合／概率，因而不是原单值 E+D 的解。没有登记新机制、筛选 owner 或取得信息量保证；一比特抽样熵不等于一比特 owner 信息。 |
| [P30：有限周期盘字的唯一真实实现](papers/30-three-disk-nonconstant-roof-determinant/notes/internal_periodic_itinerary_realization_and_primitive_counts_20260909.md) | 对每个有限合法循环盘字，在闭盘积上最小化总长度，证明极小点存在、唯一、满足正确反射且每段确为首撞。再证明任意真实反射实现必为该极小点，得到完整唯一性；本原循环字因此与本原物理轨道模时间平移一一对应，并有精确碰撞数计数。 | 不等于完整无限编码或其定量连续性；不推出 symbolic Hölder、mixing、谱隙、算子跡或 determinant。无向反转不是这里另加的商，reverse_id 与冻结 owner 字节不改。 |
| [P31：循环词本原根与逆向兼容](papers/31-level11-conjugacy-owner-ledger/notes/internal_cyclic_word_roots_and_inverse_class_separation_20260909.md) | 从循环核心的最短重复偶长前缀构造唯一正向环境本原根，给出覆盖全部 proper roots 的有限 mismatch 证书；接模 11 最小返回周期 d 得子群根、遍历指数及全部正次根分类。证明该构造与取逆兼容。 | 不自逆引理是已有结果的重证，不作为新发现。尚未实现 verifier、处理 138 输入／9,453 pairs、证明 observed image 逆向封闭或生成 canonical bytes；最短词长不是物理时间。 |
| [P32：三次对数阈值与亚纯正则部分](papers/32-homology-cover-renormalization-uniformity/notes/internal_cubic_log_threshold_and_analytic_remainder_20260909.md) | 二阶轮廓精确分成 \(-p_0a^3\operatorname{Log}a/6\) 与在零点解析的部分，得到三次展开及明确常数。解析穿过零点当且仅当 \(p_0=0\)；若不为零，延伸只有两阶连续导数而无有限第三阶一侧导数。去对数部分有指数加权格点表示及亚纯延拓。 | 临界 K 为零不代表轮廓解析，实际 p_0、K 和层留数均未数值判定。延拓只属于辅助二阶轮廓，不是原 Euler 产品、全局 determinant equality 或新 N 误差阶。 |
| [P33：内切球、中心分离与明确容量](papers/33-bolza-control-matched-census/notes/internal_inradius_separation_and_explicit_guard_capacity_20260909.md) | 核对 S01 实际交替顶点后，自含证明 Klein 八边形凸且支撑线距原点大于 2/3，故含双曲半径 \(\log(5/3)>1/2\) 的中心球。在同一真基本域前提下得中心分离大于 1；旧 CP guard 内相异群元素数严格小于 533,312。 | 未认证实际群／基本域版本绑定或运行 BFS；不把此数当历史 18,533 states／depth 11 的回放。边数量界不约束判定精度、位元成本或墙钟时间；BP 空流路线、guard 与 cutoff 不变。 |

### P29：输出放宽的最小代价，不是单值机制恢复

Gaussian 素理想的范数只有 ramified 的 2、inert 的 p² 和 split 的 p；
同一范数层最多两个理想，双元素层必为一个共轭对。这使最小范数层
自动给出全域至多二元素集合。进一步区分非实判别式、实判别式且有
不动素因子、实判别式且没有不动素因子，得到数据局部规则的逐点
最小基数，分别为 1、1、2。

数据不动与 owner 不动是两件事。本篇没有构造“真正二点 owner 轨道
却具有实坏判别式”的实例，不能把条件讨论摘要成已经证明实际存在
额外的数据局部代价。对已知不动坏 owner，下界则适用于全部 owner
等变规则：共轭对总质量为 w_j 时，熵恰为 \(1+H_2(w)\)。

真实坏族 \(x_{25^k}\)、\(k\ge1\) 在所构造规则下全部输出
\(\{(2+i),(2-i)\}\)，概率分布也完全相同。它达到最小熵，却不能
区分这无限多个 owner；没有因此取得 Gate M／Q 或自然算术机制。

### P30：从有限变分问题接到物理本原轨道

证明没有把“唯一极小点”直接等同于“唯一反射轨道”。
先用 no-eclipse 排除可行组态的每个零梯度；单侧变分给出正确法向
乘子符号，进而推出反射与首撞性。再以圆盘支撑半平面和范数凸支撑
不等式，反向证明任意真实实现都是全局极小点，完成唯一性的另一半。

最小碰撞数为 n 的本原物理周期轨道数为

\[
N_n=\frac1n\sum_{d\mid n}\mu(d)
\left(2^{n/d}+2(-1)^{n/d}\right),\qquad n\ge2.
\]

先去除短周期重复，再除以本原起点数 n。纸面核对
\(N_2=3,N_3=2,N_4=3\)；不能将所有轨道再统一除以二。
每条对应本原轨道满足 \(4an\le L_\gamma\le8an\)，从而得到物理长度
截止的有限和上下界；非本原字的总长仍明确是多次遍历时长。
没有执行极小点求解、轨道枚举或物理时间下的渐近计数。

### P31：词根证书接合环境／子群责任

任意 k 次根经过循环约化，其 k 次幂没有 syllable 消去；旧循环共轭
判准再说明 P 的核心是该幂的旋转。一个幂的旋转仍是同次数的幂，
所以只查当前起点的偶长重复前缀已经穷尽所有根。

最短块 v、重复次数 m 和旧共轭词 C 给出
\(r=CvC^{-1}\)；必须保留 SL raw evaluation 的中心符号，再取正迹
lift R，才有 exact \(P=R^m\)。模 11 的 infinity 最小返回周期 d
给 \(R_\Gamma=R^d\)、\(\nu_\Gamma=m/d\)；子群本原恰为 m=d。
十二状态界只约束这一步。

已有 level-11 不自逆引理被明确标为重证；本轮接上
\(R_\Gamma(P^{-1})=R_\Gamma(P)^{-1}\) 和相同遍历指数。
实际 observed 集合的逆向闭合性及另一行的 inverse target 仍需证据，
不能由全体类上的无不动点对合直接推出 frozen 人数或完成 inverse ledger。

### P32：唯一局部对数项与辅助系数的延拓

沿用 \(\mathsf Q=2\pi^2D\)、\(q(x)=x^{\mathsf T}\mathsf Qx\)、
\(P(x)=s_4(2\pi x)\) 与
\(p_0=\int_{\mathbb R^4}P(x)e^{-q(x)}dx\)。
将 \(G_P=\Theta_P-p_0u^{-4}\) 在 u=1 分开，得到
\(\mathcal L=\mathscr B-p_0E_4\)；其中 \(\mathscr B\) 在
\(\operatorname{Re}a>-q_*\) 全纯，
\(q_*=\min_{k\ne0}q(k)>0\)。

由指数积分递推及 E1 幂级数，精确得到

\[
\mathcal L_{D,P}(a)
=-\frac{p_0}{6}a^3\operatorname{Log}a+\mathscr A(a),
\qquad \mathscr A\text{ 在 }a=0\text{ 解析}.
\]

新文给出有限矩 \(M_0,M_1,M_2\)、第三矩的明确有限部分、
三次 Taylor 常数、任意分割点 U 的抵消以及零点二阶导数的差商。
因此“有两阶连续导数但无第三阶一侧导数”的结论不是只依据
邻域内三阶导数无界。

保留指数权后的合法格点表示还将 \(\mathscr A\) 亚纯延拓至复平面，
候选简单极点为 \(-q(k)\)，同一层的留数是该层所有 P(k) 之和。
层总权重为零时极点可消。若 \(p_0\ne0\)，单值亚纯的是
\(\mathscr A\)，不是含对数的 \(\mathcal L\)。

径向测试 \(P=\alpha q^2\) 给 K=0 却有
\(p_0=6\alpha c_D\)，从而仍出现 \(-\alpha c_Da^3\operatorname{Log}a\)。
这只区分两个函数条件，不假定真实 P 为径向，不判定其非消失性。
原产品的 N 余项、精确临界点定义及未构造算子的边界继续保留。

### P33：由内切球消去额外的分离常数假设

本轮核对的固定顶点半径是
\(u=e^{-1/10}\) 与 \(b_{\rm geom}=(\sqrt2u)^{-1}\)，相邻极角差
\(\pi/4\)。Klein 变换的直线多边形证明给
\(\overline B_{\mathbb H^2}(0,\log(5/3))\subset\operatorname{int}D_C\)。

若这个同一八边形确为固定群的真基本域，不同 translates 的内部
互不相交，内切球的 translates 也互不相交，故中心分离大于 1。
原 \(\lvert\alpha_g\rvert^2\le20000\) guard 对应
\(\cosh T=39999\)，面积比较及有理界给

\[
\#C_T<
\frac{66665-1}{1/8}=533312.
\]

取保守 \(N_{\max}=533312\)，完整八字母有向边分类数最多
4,266,496，简单路径长最多 533,311。这些计数已经包括恒等元，
但不界定未去重字串、outside 拒绝项的储存或任何实现的重复工作。

另外证明有限列表的“全部域内可达＋每点全部八边正确分类”足以刻画
恰好 \(C_T^0\)，而不是整个 guard 必然连通。精确状态身份、闭 guard
等号、发现树、FIFO、digest、零 unresolved、owner 商和独立 replay
仍是实际证书责任。没有生成该列表或修改合同空槽。

### 来源、实际动作、复核与保全

P32 普通浏览核对
[DLMF §8.19 的指数积分定义与递推](https://dlmf.nist.gov/8.19)
及 [§6.6 的 E1 幂级数](https://dlmf.nist.gov/6.6)。
P33 普通浏览核对
[Nazarenko 作者 v1 的 §2 顶点与参数公式](https://arxiv.org/pdf/1301.5446v1)，
并与冻结矩阵 definition 的 \(e^{-1/10}\)、\(\pi/4\) 和 b 公式对照。
来源的模型陈述与本轮新增推导分别报告，不把远端可读 PDF 冒称为
旧本地来源字节的 SHA replay，也不把来源存在当作实例证书。

主线程写 P29、P32 及本追加节，三个分工各只写 P30、P31、P33
的一份新笔记。主线程完整核读五篇及核心证明；交叉只读复核为
P30 检查 P29 和 P32、P31 检查 P33、P33 检查 P30 和 P31。
这些意见只用于检错，不构成独立科学证据或正式同行认证。
ARS 有界 argument-builder 用于明确输出类型、标准旧引理、
证明前提与实际可执行证书之间的区别。

实际只做本地只读定位、纸面推导、上述普通公开浏览、五份新笔记
及本入口追加。没有运行科学／符号程序、概率抽样、数值积分、
极小点求解、BFS、轨道枚举、producer、fixture、历史 artifact
writer、论文构建、正式 reviewer、Route evaluator 或远程写入。
只读 Node 仅用于文件、链接和文本完整性检查。

P32 的首次新文件补丁因一条数学行缺少新增标记而在验证时被拒，
只读确认没有产生文件后修正补丁格式并重试，失败记录保留在新文。
P33 的 Git 检查因工作区不是 repository 而不可用，未改 Git 配置；
P30 交叉复核 P32 时一次错误目录查询返回 ENOENT，随后用
rg --files 找到正确目录完成只读检查。无失败被回填为科学成功，
未重取或绕过此前 Sharp／Bolza／Conrad 的失败来源通道。

本轮写入前于 **2026-09-09 05:05:50.855 UTC** 对五篇目录及根目录
BATCH_ROUND10* 普通文件建立 **3,342 个原文件**的字节／SHA-256 快照。
交接检查范围为：恰好五篇各新增一份笔记；其余 **3,341 个原文件**
字节不变；本入口保留原 **49,116 bytes** 前缀且只追加本节；
另检查本地链接、引用定义、数学环境、连续公式编号、控制字符、
文本完整性及末尾换行。机械检查不建立数学有效性或来源充分性。

原现稿、书目、冻结输入、协议、正式回执及失败记录不回写；
五篇正式 FAIL / BLOCK、D06 Recovery 3、Route 及 Stage 5／6
边界保持不变。本轮完成仍只表示五份有界内部增量已形成，
不等于总目标、实际 census、生产证书或投稿资格完成。

交接检查技术记录：首次检查将全量文件散列、正文和链接一起返回时，
工具输出被截断，JSON 无法完整解析，故未将该次检查报为完成。
后续改为在只读进程内汇总文本结果、紧凑返回散列行；该编排的首次
字符串因反引号造成 JavaScript 解析拒绝，在工具执行及写入前失败，
修正后继续。两次失败均保留，不修改研究输入，不刷新科学回执，
也不把截断输出拼接成成功记录。

引用检查补注：初始正则式将 P31 显示公式中矩阵类相乘的方括号误识别
为一个未定义引用。排除数学环境和行内代码后，五篇实际文字引用均有
对应定义；这是解析范围修正，不是实际链接缺失，也没有为迎合检查器
改写该公式或研究正文。

## 2026-09-09：第五次五篇整轮内部论证——无限编码、提升分类与精确判定

用户“继续”启动本轮，继续五篇全部形成有界内部增量后集中交接。
范围为内部数学推导、按需普通公开来源核对、各一份新笔记和本入口
追加；不启动实验、producer、正式稿修订、审查恢复、Route 评估、
Stage 5／6、远程同步或公开发布。

| 课题与新增笔记 | 本轮具体增量 | 仍未建立的部分 |
| --- | --- | --- |
| [P29：代数单位长度与素数对数障碍](papers/29-bianchi-ideal-owner-refinement/notes/internal_algebraic_unit_lengths_and_prime_log_obstruction_20260909.md) | 固定 Bianchi 弧长的指数满足显式整系数互反多项式，因而是正实代数单位；全部几何长度的有理线性包与素数对数的有理线性包只交于零。集合标签或重复遍历不能自动提供精确素数时钟。 | 不对任意实数缩放、近似配对、无限消去或所有行列式作不可能性声明。原 E+D 标签公理未要求周期等式，故不偷加该公理或改 Route verdict。 |
| [P30：完整双向编码与 roof 局部性](papers/30-three-disk-nonconstant-roof-determinant/notes/internal_biinfinite_coding_and_roof_locality_20260909.md) | 在全部闭盘配置上构造统一收缩更新，证明每个双向合法盘字恰有一个真实被困实现，并覆盖全部被困碰撞。给出指数局部性、指定符号度量下状态／原 roof 的 Hölder 界及逐碰撞拓扑共轭。 | 证明用更新不是物理碰撞映射；没有由其收缩推出物理切向双曲性、转移算子谱隙、混合、跡或 determinant，也没有执行数值迭代。 |
| [P31：陪集周期提升与有向类拆分](papers/31-level11-conjugacy-owner-ledger/notes/internal_coset_cycle_lifts_and_oriented_class_splitting_20260909.md) | 十二个左陪集上的周期与全部正幂中的子群本原提升类一一对应；固定 R 的 m 次幂仅收周期长度整除 m 的那些类。给出六种 mod-11 周期型，以及有环境反向共轭子时的无不动点逆向配对。 | 几何长度的 d 倍关系不是原时间变换周期的无条件 d 倍关系；没有处理 138 输入、实际周期分割、规范字节、G/I/C 或 observed inverse links。 |
| [P32：层留数可识别性与对称核](papers/32-homology-cover-renormalization-uniformity/notes/internal_shell_residue_identifiability_and_symmetry_kernel_20260909.md) | 完整辅助轮廓恒零当且仅当全部格点层权重总和为零；整数等距平均保留全部可见量。明确非共振条件下，至多 69 个精确层留数重建 35 维四次项；标准欧氏测试型却只有 2 维可见、33 维不可见。 | 未为真实 D、P 认证非共振或任何实际对称性；精确唯一性不是稳定数值反演，不改变 N 误差阶、原临界产品定义或算子证据。 |
| [P33：精确矩阵身份与 guard 可判定](papers/33-bolza-control-matched-census/notes/internal_exact_state_identity_and_guard_decidability_20260909.md) | 将冻结八字母放入具有单射实嵌入的二次函数域，给整体正负号一致的 PSU 身份判定。清分母多项式的非零常数项排除全部有限字的 guard 等号，并排除 hyperbolic 字恰在几何长度 21/10；有理区间比较必有限终止。 | 没有生成或回放 BFS、state codec、全边流和 owner 商；真基本域与完整侧／顶点邻接仍是有限覆盖前提。可计算的理论精度界不等于旧十进位精度已足够。 |

### P29：标签可选性与固定时钟的精确关系分开

对任意 loxodromic \(A\in SL_2(\mathbb Z[i])\)，令
\(T=\operatorname{tr}A=a+bi\)，扩张特征值为 \(\lambda\)。
上半空间的高度缩放给 \(\ell=2\log|\lambda|\)。于是
\(U=e^\ell=\lambda\bar\lambda>1\) 满足

\[
U^4-(a^2+b^2)U^3+
\bigl(2(a^2-b^2)-2\bigr)U^2-(a^2+b^2)U+1=0.
\]

同一互反多项式还包含 \(U^{-1}\)，故两者都是代数整数。
有限个 U 的任意整数幂乘积若是正有理数，它及其倒数都为整数，
只能等于 1。清除有理系数的分母后得到

\[
\operatorname{span}_{\mathbb Q}\{\ell(A)\}
\cap\operatorname{span}_{\mathbb Q}\{\log p:p\text{ 为素数}\}
=\{0\}.
\]

因此对任何非零有理 c、任何非零 Gaussian 素理想，
\(c\ell(A)\ne\log N\mathfrak p\)。这包括原时钟和有理统一换算，
但不涉及任意实数换算或量化的近似误差。先前的集合／概率标签存在
结论保持；它们没有因此成为精确周期标识，也没有被新加的时钟公理
重新定义。

### P30：从闭盘收缩到全部真实被困动力学

把每个配置点更新为所在圆盘上朝向两邻点射线和的边界点。
全部闭盘三点配置的方向锥，而非仅真实反射点，给出
\(\kappa_*=(2\sqrt6-1)/6>1/2\)。沿可行线段直接求差商，得到
统一收缩率

\[
\rho=\frac1{2\kappa_*}=\frac3{2\sqrt6-1}<1.
\]

中心初值的 m 次纸面更新与极限距离至多 \(a\rho^m\)，且第 i 个
m 次近似只看 \([i-m,i+m]\) 盘字。因而两字在 \([-m,m]\) 相同时，

\[
|q_0-\widetilde q_0|\le2a\rho^m,\qquad
d_a(H(s),H(\widetilde s))\le3a\rho^{m-1},\qquad
|\tau(s)-\tau(\widetilde s)|\le4a\rho^{m-1}\quad(m\ge1).
\]

证明逐项核对固定点的法向符号、镜面反射、出发盘／终点盘／第三盘
的首撞排除及双向无碰撞累积；反向还证明每个真实被困轨道必为该
固定点。故完整唯一性不只来自一个抽象收缩结论。
紧致符号空间加定量连续双射再给拓扑共轭，物理 roof 仍是两次首撞
之间的欧氏距离。没有用这个辅助更新替换真正的时间演化。

### P31：全部提升与固定幂共轭类不是同一总体

使用 \(h\Gamma\mapsto h\infty\) 的左陪集 convention。环境本原 R
的一个长度 d 周期给子群本原元素 \(H^{-1}R^dH\)，完整双射由
\(\langle R\rangle\backslash G/\Gamma\) 控制。固定 \(R^m\) 的类则对应
d 整除 m 的周期，给该本原提升的 \(m/d\) 次遍历。尤其固定点集合
应模去 \(\langle\bar R\rangle\)，不能模去在该集合上处处不动的
\(\langle\bar R^m\rangle\)。

determinant-one 的有限域线性代数限制周期型为
\(1^{12},1\cdot11,1^2 5^2,2^6,3^4,6^2\)。
若另有环境反向共轭子 J，\(h\Gamma\mapsto Jh\Gamma\) 保持周期长度
并代表 inverse owner；level-11 的不自逆引理使该配对无不动周期，
所以每个长度的周期数都是偶数，排除这种前提下的 \(1\cdot11\)。

标准几何长度满足
\(\ell_{\rm geo}(P_{\mathcal O})=d_{\mathcal O}\ell_{\rm geo}(R)\)，
总和为 \(12\ell_{\rm geo}(R)\)。原流 \(X_{\rm geo}/\rho_\epsilon\)
的周期则为 \(\int_{\gamma_P}\rho_\epsilon ds\)：只有同一子群轨道
重复遍历的倍乘在这里无条件成立。不同提升或逆轨道的周期关系需要
额外证据；\(\rho_\epsilon\) 从环境基底下降是一个充分条件，不是
这些有限轨道积分偶然相等的必要条件。

### P32：完整函数、临界值与压力项非零是三件事

前轮已有候选简单极点的留数
\(W_P(\lambda)=\sum_{q(k)=\lambda}P(k)\)。
本轮将它与零点对数阈值、零 Fourier 极限和恒等定理接合，证明

\[
\mathcal L_P\equiv0
\iff W_P(\lambda)=0\ \text{对全部层成立}
\iff\Theta_P\equiv0
\iff\mathscr A_P\text{ 的全部极点可消}.
\]

这些条件实际都迫使 \(p_0=0\)、\(\mathscr A_P=0\)。
“全部留数决定完整函数”只对规定的 theta／积分族成立，
不否认一般亚纯函数可以自由加入整函数。

一般整数等距平均 \(\Pi_q\) 给
\(\ker\Pi_q\subseteq\ker\mathcal L\)，不擅自写成等号。
若另外确证每个非零格点层只有 \(\{k,-k\}\)，则留数等于 2P(k)；
四阶有限差分给出至多 69 点的完整系数重建。
在不代表实际 D 的测试 \(q=\sum_i x_i^2\) 中，平均四次项只有
\(A\sum_i x_i^4+B\sum_{i<j}x_i^2x_j^2\)；两个层分别给
\(8A\) 与 \(48A+24B\)，所以可见维数恰为二。
非零调和项 \((x_1^2-x_2^2)(x_3^2-x_4^2)\) 在这个测试型中完全
不可见。没有由此判定真实压力项、K 或任一实际层留数。

### P33：固定超越参数不妨碍精确比较

设 \(u=e^{-1/10}\)、\(D(U)=(1-U^2)(2U^2-1)\)、
\(Y^2=D(U)\)。固定正分支 \(Y\mapsto\sqrt{D(u)}>0\) 后，
八字母都形如 \(-H_a(u)/\sqrt{D(u)}\)，其中 H_a 为 Gaussian
整数多项式矩阵。D 在 U=1 有单零而不是有理函数平方；u 的经典
超越性使该二次函数域向实际矩阵域的代入单射。因此有限字的矩阵
身份可精确判断，PSU 判等需对全部 entries 使用同一个整体 ± 号。

对 n 字的上左多项式 p_w，guard 清分母为
\(\Phi_w=p_w\bar p_w-20000D^n\)。纯形式地令 U=0，各字母矩阵都是
Gaussian-unit 反对角矩阵，故

\[
\Phi_w(0)=
\begin{cases}-19999,&n\text{ 偶数},\\20000,&n\text{ 奇数}.\end{cases}
\]

所以 \(\Phi_w\) 永不为零多项式，且 \(\Phi_w(u)\ne0\)。
这排除实际 guard 等号，不改变闭 guard。对长度 21/10 的清分母式，
常数项同样为 \((-1)^{n+1}\)，故所有 hyperbolic 有限字都不在
该长度等号上；但 trace²=4 仍需先保留精确零分支。

有理 Taylor 区间及多项式导数界给每次严格比较的有限停止证书。
新文还给 \(\deg\Phi_w\le4n\)、
\(\|\Phi_w\|_1\le16^n+20000\,6^n\)，并从有限系数多项式集合构造
一个可计算但未求值的统一细化步数函数。这不是实用复杂度估计，
更不认证旧 110／140 位小数。结合前轮真正有限中心域的几何前提，
可支持理论上会终止的去重遍历；本轮并未实现、执行或认证该遍历。

### 来源、复核、实际动作与保全

P29 普通浏览核对
[Milne 作者讲义 v3.08 的 Theorem 2.1](https://www.jmilne.org/math/CourseNotes/ANT.pdf)
及其代数整数环封闭性证明；正文版本日期是 2020-07-19，不采用搜索
抓取日期作为出版日期。P32 核对
[DLMF §1.8(iv) 的 Poisson 公式背景](https://dlmf.nist.gov/1.8#E14)，
具体加权四维公式仍由前轮推导承担。P33 核对
[Waldschmidt 作者章节 §1.1、印刷页 144、Theorem 4](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SurveyTrdceEllipt2006.pdf)
的 Hermite–Lindemann 定理；取非零代数数 -1/10 得 u 超越。
同页 Theorem 1 的 e 超越性其实已足够，因为 \(u^{-10}=e\)。
没有依赖未给出的有效超越测度或新参数的代数独立性。
来源背景与本轮模型推论分别登记，不声称新颖性或来源字节 replay。

主线程全文核读五份新文及核心证明；交叉只读检错为 P31 检查 P29、
P30 检查 P32 与 P31、P31 检查 P33、P33 检查 P30。
P31 新文两处上标的多余逗号被修正，时间变换下降条件改成充分条件
措辞；原数学对象及旧输入没有因此改变。同伴意见只用于检错，
不算独立科学证据、正式同行评审或形式化认证。
ARS 有界 argument-builder 具体用于分开构造与反向桥接、精确输入
与试验模型、定理量词与运行证书，不启动正式写作或审查流程。

实际动作限于只读文件定位、纸面证明、上述公开浏览、五份新笔记和
本入口追加。未运行科学或符号程序、数值迭代、积分、格点／矩阵／
多项式／陪集枚举、BFS、producer、fixture、历史 artifact writer、
论文构建、Route evaluator、正式 reviewer 或远程写入。
只读 Node 仅用于文件、文本、链接及字节保全检查。

技术记录：首次快照命令的 shell 引号使换行转义进入 Node 源码，
在解析时失败，未发生写入；改为正确的单引号传参后完成只读快照。
主线及 P30 分工各有一次旧 P31 文件名查询失败，随后依 rg 定位或
新文真实引用读到正确旧文。没有将失败回填为科学成功，也没有重试
旧 Sharp／Bolza／Conrad 的失败来源通道或刷新任何科学回执。
P33 的初次文字引用检查误把代码中的方括号当引用，修正检查范围时
另有一次 shell 引号失败；限定到非代码／非公式正文并修正传参后
通过，技术记录保留于该新笔记，未改数学正文来迎合检查器。

本轮写入前于 **2026-09-09 10:42:35.534 UTC** 对五篇目录及根目录
BATCH_ROUND10* 普通文件建立 **3,347 个原文件**的字节／SHA-256 快照。
交接保全范围为：恰好五篇各新增一份笔记；其余 **3,346 个原文件**
保持字节不变；本入口保留原 **62,164 bytes** 前缀且只追加本节；
另检查新文／追加节的本地链接、文字引用、数学环境、连续公式编号、
控制字符、冲突标记、行末空白与末尾换行。
这些机械检查不证明数学有效性、来源充分性或 producer 可靠性。

旧稿、书目、冻结输入、协议、正式回执及失败记录不回写；
五篇正式 FAIL / BLOCK、D06 Recovery 3、Route 与 Stage 5／6
边界全部保持。本轮完成只表示五份有界内部理论增量已形成，
不表示实际 census、全局行列式、正式完整性或投稿资格完成。
后续仍按五篇一轮，不自动启动下一轮。
