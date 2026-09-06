# 算术谱侦察记录的独立只读交叉审计

日期：2026-09-06。审计者：当前团队非线性几何线。
最新状态：`F1_CLOSED / NO_REQUIRED_CORRECTIONS_REMAINING`；见文末定点复核。
对象：[arithmetic_spectral/SCOUT_REPORT.md](../arithmetic_spectral/SCOUT_REPORT.md)，
实际阅读的是以 “Arithmetic/spectral scout: decimation is not a new zero-spectrum bridge”
开头的 84 行快照。以下行号针对该快照。

这是协调者指定的有界来源/措辞审计，不是完整论文审稿、作者实际阅读行为的
历史认证、第三方人类同行评审或 Route-A 正式评价。未修改被审计文件，
未重跑或重新审查 C184 的数学包，未取得不可访问的订正文。

## 发现

### F1：无界模型的 hyperfunction 不应被统一归类为普通谱 Dirichlet 级数

优先级：需要局部澄清；不推翻“本轮无新契约”的决定。

原报告第 9–15 行将 prospect 的 observable 统一称为 spectral Dirichlet series，
但第 30 行引用 Lal–Lapidus 的无界 gasket 与半直线，并称其 factorization 已有
所有者。这一来源的摘要明确包含 Dirac delta hyperfunction，故把它和紧模型
在同一个普通解析 trace 类别中叙述不够准确。

为确认这不是仅凭标题的意见，本审计追加核读了
[Lal–Lapidus v2 的 §2.1、Lemma 2.7、Theorems 2.8–2.9](https://arxiv.org/pdf/1202.4126)。
其无界模型涉及双向尺度和

\[
\sum_{k\in\mathbb Z}5^{-ks/2}.
\]

正向尾要求 \(\Re s>0\)，反向尾要求 \(\Re s<0\)；在 \(\Re s=0\) 项也不趋零。
所以这不是在某个共同收敛半平面定义的通常级数。原文用圆上的 Dirac
hyperfunction 解释该因子，定理 2.9 再将其与有界 gasket 的谱 zeta 配合。
这里不能据“已有 factorization”推成“已有普通 trace Dirichlet 级数的同类延拓”。

建议仅作两处收窄：

- 开头明确紧模型使用普通谱 Dirichlet 级数，无界模型文献另使用 hyperfunction 解释；二者不被默认为相同 analytic owner。
- Lal–Lapidus 行把 “factorization” 补全为 “hyperfunction factorization in the unbounded case”，并仍保留“原 scout 只读摘要”的访问级别。

我的追加主文核读不应回填成原 scout 在此前已经读过这一证明。需要时可另标为
本次交叉审计提供的主文证据。修正后，原报告仍可合理拒绝只把旧构造搬进项目
的拟议论文；本审计没有找到替代的新定理。

### F2：两个低优先级表述可以更精确

1. 第 43–51 行宜写明区间是 \((0,1)\) 且采用 \(-d^2/dx^2\) 的 Dirichlet
   实现。此时 \(\lambda_n=\pi^2n^2\)、\(\sum\lambda_n^{-s/2}=\pi^{-s}\zeta(s)\)
   完全正确。\(\lfloor T/\pi\rfloor\) 是
   \(N_{\sqrt\Delta}(T)=\#\{n:\sqrt{\lambda_n}\le T\}\)，而非
   \(N_\Delta(T)\)。原文已经写了 frequency，不构成现有数学错误；加符号可
   防止后续引用时丢失这个限定。
2. 第 31 行 “A generic regularized-determinant proposal is also already occupied”
   最好限定为本轮所列的例子/重构。出版社的正文引言明确研究 diamond、double
   gasket、double pq 三类具体模型，并非一句话覆盖所有分形的全部行列式定理。
   原报告最终段已经要求具体新定理才能重开，所以这只是局部措辞收窄建议。
   [Chen–Teplyaev–Tsougkas，出版社正文 §1](https://link.springer.com/article/10.1007/s11005-017-1027-y)。

## 已核查且未发现实质问题的部分

| 审计项 | 本次独立核查 | 结论 |
|---|---|---|
| Teplyaev 的已有 quadratic/有限尺度极限所有者 | 访问作者 PDF 的引言、Definition 2.1、Theorem 3、Theorem 6；后两项确分别含 Riemann-zeta 的二次多项式表示和 gasket 分解 | 原报告第 28 行的数学归属有相应主文，不是只据题名推断；不认证原作者读过整篇 |
| Derfel–Grabner–Vogl 的全平面延拓 | [arXiv 摘要](https://arxiv.org/abs/math/0508315) 确称在其 spectral-decimation 类中得到亚纯延拓、极点/留数/特殊值及计数振荡结果 | 原报告第 29 行明确 “abstract, not full proof”，访问级别没有被伪装成全证明阅读 |
| Lal–Lapidus 的多变量与 Lebesgue 特例 | [arXiv 摘要](https://arxiv.org/abs/1202.4126) 确含这些主张，同时明确 hyperfunction 因子 | 已有主题归属成立；但 analytic object 须按 F1 区分 |
| 正则化行列式论文与 correction 警告 | 出版社正文页确列 2018 correction；引言确列三个例子以及离散/正则化行列式关系 | 原报告没有采用未读 correction 的具体修正式，因此不以该访问限制阻断其有界所有权筛查 |
| 经典碰撞是否被说成全族不可能 | 首段、第 53 行、末段明确限制为 reconstruction proposal 与 definition-level check | 未把来源碰撞提升成全局不可能性定理 |
| \(s\) 是否被偷换成谱值 | 第 48–53 行明确区分特征值索引、幂指数及函数零点 | 核心区分正确；未声称 \(\zeta(s)\) 的零点已经是该 Laplacian 的谱 |

Teplyaev 的本次核读依据是
[作者预印本 v2](https://www2.math.uconn.edu/~teplyaev/research/arxiv0505546.pdf)。
没有重新演算其中整个谱极限、没有复制其所有常数，也没有把不同文献的
\(\lambda^{-s}\) 与 \(\lambda^{-s/2}\) 约定混用。尤其 Chen–Teplyaev–Tsougkas
采用前一约定、此处区间 sanity check 采用后一约定；原报告没有直接搬用
其极点坐标，因此当前未发生二倍尺度错误。

## 总结

审计决定：`ONE_ANALYTIC_OBJECT_CLARIFICATION + TWO_MINOR_PRECISION_NOTES`。
对“0 个新契约”的结论无反对意见。建议落实 F1 后收束；无须因此启动
全论文 review、重做旧 C184 或宣告新的目标谱障碍定理。

## 定点复核及关闭记录

协调者收到 F1 后追加核读 Lal–Lapidus 原文指定段落，并修改了报告开头与
来源表对应行。本审计实际重新读取了这两处修订：

- 开头已经把 compact/discrete-spectrum 模型的收敛半平面 Dirichlet 级数，
  与无界替代模型的 hyperfunction regularization 分开，且明确后者不是
  ordinary convergent trace Dirichlet series。
- Lal–Lapidus 行已经点明 Dirac hyperfunction 因子、访问范围是收到反馈后的
  追加段落阅读，并明确未读整篇。因此没有将本次补查倒填成初次全文阅读。

结论：`F1_CLOSED`。两个 F2 措辞建议仍是非阻断性建议，本审计未将其升级为
必须修正；没有其余必要修正，也没有重新审查已排除的 C184。

为保留原意见和版本对应关系，首次完整读取的 84 行原文本已另存为
[修订前快照](ARITHMETIC_SPECTRAL_PREAUDIT_SNAPSHOT.md)。该文件是本次闭环时
按已读原文本保存的审计快照，不是新研究结论，也不冒充一份 Git 历史提交。
两个指纹均在闭环时核算：

| 状态 | SHA-256 |
|---|---|
| 修订前 84 行快照 | `ccc8eebf17adc4f1bd420b12c9e06bc909f8b2ee14dc28fe15c781e7850f2245` |
| 修订后被审计报告 | `fee36724ac32ff68811bd9d3be6ddd5f12cda25e67aa2736d2ee0cc1ee5febf6` |

此关闭结论只覆盖上述修订后指纹；后续编辑需要重新确认对应文本，而不能
把此次有界审计扩写为全论文或全代码认证。

## F2 措辞修订的最终定点确认

协调者随后采纳了两个非阻断性 F2 建议。本次只读核对三处：

1. Chen–Teplyaev–Tsougkas 行已限定为重构所列的具体例子不构成新契约，
   并明确不对所有分形的行列式作全称断言。
2. 区间算子已明确为 \((0,1)\) 上带 Dirichlet 边界条件的
   \(\Delta=-d^2/dx^2\)。
3. 频率计数已经标明 \(N_{\sqrt{\Delta}}(T)=\lfloor T/\pi\rfloor\)，
   不再仅依赖散文中的 frequency 限定。

三处均与原建议一致。未重新读取来源、复跑 C184、重做数学或全文审查。
保留此前 F1 关闭记录；本次新增状态为
`F1_CLOSED / F2_CLOSED / NO_REMAINING_FINDINGS`。

本次定点确认的报告 SHA-256：
`15150ed5ab93df8d4e303652ec35387f1612eb2d443997af07d09cc71627979e`。
它接续而不覆盖此前的 `fee36724…` F1 修订版本记录。
至此该有界审计闭环；审计者不再改动本报告。
