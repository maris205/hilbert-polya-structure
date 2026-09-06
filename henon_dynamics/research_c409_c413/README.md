# C409–C413 选题检查点：四项研究候选，第五项仍缺

2026-09-06。状态：`SCOUT_CHECKPOINT_FOUR_READY_FIFTH_OPEN`。
用户授权的五篇任务**尚未完成**。当前产物是四份通过非作者
数学／实质核查的完整证明合同候选，以及两份不独立计篇的数学
札记；**零项正式 C 编号、零份论文正文／PDF、零份正式 Route-A
评价**。本目录不是五篇论文的替代品，也不授权进入 C414。

## 四项保留问题

| 完整问题 | 已闭合的范围与实际差额 | 证明与非作者核查 |
|---|---|---|
| 野性非双曲 FAD 的自然边界 | 有限素数、复相位和周期径向数据的精确 active-fibre 分类；先处理实际 Fourier 原子抵消，再证明全导子稠密网格。扣除既有 no-wild 分支；Salem 环面乘野性加性系统提供真实非双曲例子。 | [证明](arithmetic/PROOF_PACKAGE.md)、[真实例子](arithmetic/REALIZED_EXAMPLE.md)、[协调者审查](REVIEW_ARITHMETIC_ROOT.md) |
| 特征三三次映射的全逆像野塔 | `x^3+a*x^2, a!=0` 的全部 generic 逆像高度；混合 Kummer／AS 的全局独立和局部秩一同时归纳，得到群、分歧及亏格。经典抽象群 E 不计作新对象。 | [完整证明](positive_characteristic/WILD_CUBIC_PROOF.md)、[来源](positive_characteristic/SOURCE_SCREEN.md)、[协调者审查](REVIEW_WILD_CUBIC_ROOT.md) |
| 两个独立时钟的共同回返级数 | 对所有整数 `a,b>=2`，分类 `sum gcd(a^n-1,b^m-1)x^n y^m` 的开绝对收敛域、依赖情形内部极因子与完整联合亚纯边界。Ward/Miles 的矩形、体积 zeta、同步及已知对角结果均扣除。 | [完整证明](arithmetic/RECTANGULAR_RETURN_PROOF.md)、[来源差额](arithmetic/RECTANGULAR_SOURCE_AUDIT.md)、[协调者审查](REVIEW_RECTANGULAR_ROOT.md) |
| monic 整系数保面积二次 Hénon 的全部有理周期点 | 对 `H_{a,b}(x,y)=(y,y^2+by+a-x), a,b in Z`，完整分类全部参数及全部周期；只有 1–4 周期，精确点集及尖锐八点界。奇偶一次项合在同一合同中。 | [偶分支证明](nonlinear_geometry/PROOF_INTEGER_HENON.md)、[奇分支及合并](nonlinear_geometry/ADDENDUM_INTEGER_HENON_ODD.md)、[独立审查与有限补集重建](REVIEW_INTEGER_HENON_ROOT.md) |

“研究候选通过”只表示本次内部审查认为量词完整、证据足够且
扣除实际已读来源后仍有独立问题差额；不是全球优先权保证、
同行评议通过或已经写成论文。详细判断见
[逐项实质裁决](PROVISIONAL_ADJUDICATION.md)。

## 两项数学成立但不独立计篇

1. [对数 Dirichlet germ 的 Gram 谱转移](spectral/PROOF_DRAFT.md)：
   [独立模型证明](spectral/MODEL_MOMENT_PROOF.md) 与两份非作者
   数学核查均未发现缺口。但扣除经典模型及一般解析逼近后，
   当前应用未再闭合独立算术问题。
   [实质拒绝](nonlinear_geometry/REVIEW_SPECTRAL_MODEL.md)。
2. [`x^p+1/x, p>=5` 的有理逆像野塔](positive_characteristic/WILD_PSL_RATIONAL_PROOF.md)：
   全层数 group、精确惯性过滤和亏格论证数学成立。
   [全局审查](REVIEW_WILD_PSL_ROOT.md) 与
   [独立局部审查](arithmetic/REVIEW_PSL_LOCAL.md) 分别重推关键步骤。
   扣除 Serre 首层及一般复合方法后，剩余局部 AS 合成机制与
   已保留三次野塔关系过近；作者、非作者及协调者一致保留为
   配套札记。[来源与实质拒绝](nonlinear_geometry/PSL2_TOWER_SOURCE_AUDIT.md)。

拒绝独立计篇不等于撤回有效定理，也不声称已经找到整篇同结果的
既有出版物。保存完整证明使以后可以直接复用，不需因换批次重做。

## 实际验证与访问限制

- 所有四份保留证明均有非作者全文数学审查；两份札记也经过
  实质审查，没有用程序成功替代证明。
- Hénon 无限参数由统一六符号逻辑覆盖；协调者另从完整界内
  整数图重建布尔传递闭包，独立核对两个奇偶分支留下的
  **13+17 个有限补集的全部点集**。实际命令、Python 版本、
  退出码与脚本哈希记录在对应审查中。
- 三次野塔、有理野塔和双时钟的作者精确诊断有各自
  [三次记录](positive_characteristic/EXACT_CHECK_REPORT.md)、
  [有理记录](positive_characteristic/PSL_EXACT_CHECK_REPORT.md)、
  [双时钟记录](arithmetic/RECTANGULAR_EXACT_CHECK_REPORT.md)。
  它们是有界符号／群论／系数检查，不是无限定理或文献优先权证书。
  关闭阶段不重跑输入未变且已通过的数学检查。
- 主来源比较以实际读到的版本为限：BCH 的公开 v2、BHN 的
  公开稿及出版社元数据不能冒称已取得其最终全文；Silverman
  1994 的订阅全文未取得；两篇旧 Abhyankar 相关全文存在访问缺口。
  KNR 全文的特征零约定保留，不将其附录冒称字面任意特征定理。
- 没有外部稿件上传、付费 API 审稿、GPU 实验、期刊投稿或
  人类同行评议。当前团队审查始终标为内部。

## Route-A 与技能范围

保持 `NO_BAD_EULER_OR_ROOT_NUMBER`。这里没有证明目标 Euler
因子、根数、素数轨道时钟、零点／除子对应或 Hilbert–Pólya
实现；源系统的自然边界、分歧群或有理周期分类不自动升级目标。
generic 逆像高度、两个独立回返时钟和普通周期必须分开。
另一研究者另完成
[独立 owner／clock 范围建议](arithmetic/ROUTE_SCOPE_RECOMMENDATIONS.md)，
逐项区分源计数、源有限置换行列式和未建立的目标 A2–A4，并明确
三类必要算术对照仍未完成。该建议不是正式评分文件。

协调者已完整读取固定 Route-A v0.2.0；其 SHA256 为
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。
已读所需 prior-work README、六份 PDF 各自页 1–3 及 flow 的两份
注册表，并检索本流相关碰撞。PDF 先核对页数／结构；第一份有
`Suspects object is wrong type` 的元数据提示但提取正常。
这只是参考路由，不构成对既有文稿中未经复核的 RH／零点声明的
认可，也没有据此发布正式评价或更改版本化 evaluator。

本仓 `henon-route-a-batch` 要求五个独立实质合同成立后才冻结
五篇计划；因此本次停在缺一项的选题检查点。已准备后续
`paper-plan`、`paper-write`、`paper-compile` 的相关指令，但没有
开始写稿、套用 ML 会议篇幅或生成论文框架充数。检索、查新与
证明技能所要求的来源扣除，实际促成了两项不计篇决定。

## 续接和保存

下一次续接仍在 **C409–C413**：保留四个已核合同，寻找独立
第五个完整问题；不要重做本目录已完成的证明检查，不拆两份
札记或四份合同的推论，也不进入 C414。凑齐后再冻结编号／写作
计划，完成正文审查、正式评价、双新目录 PDF 构建、全页视觉
检查及论文封存交付。

原批 round2/round3 的 179/93 个冻结文件和八个继承未跟踪目录
均不改动。本目录当前检查点将以精确 payload ledger 和自排除
manifest 保存；成员、字节和实际 Git 同步的关闭收据写在
[检查点保存记录](CHECKPOINT_RECORD.md)。它们只证明保存一致性，
不替代研究结论。清单尚未生成前，不将这句计划描述为已封存。
