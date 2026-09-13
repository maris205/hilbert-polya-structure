# Paper31：原映射提升来源的引用补充 V1

日期：2026-09-13。核查者：`/root/p31_q2_citation_scaffold`。
状态：BOUNDED_SOURCE_INTERFACE_CHECK_COMPLETE / NOT_A_REAL_LIFT_PROOF_REVIEW。
本件仅补充 Joshi–Roffelsen 的书目和 §2.1 来源接口；不修改旧引用记录、TeX、锁或索引。
根据主控本次任务，V1 的 M1 是完整原 F lift 的归属及本稿实际证明缺口；其修正由主控在 V2 完成，本件不替它验收。
本次 FULL 读 paper-plan 技能，仅使用 Step 5 的书目核准规则；未重开准入、科学查新或旧数学审查。

## 1. 书目身份与实际核准层级

| 字段 | 核准值与层级 |
|---|---|
| Authors | Nalini Joshi; Pieter Roffelsen |
| Title | Arithmetic dynamics of a discrete Painlevé equation |
| 固定科学版本 | `arXiv:2508.18578v2`，2026-01-16；v1 为 2025-08-26 |
| arXiv DOI | `10.48550/arXiv.2508.18578`，仅预印本标识 |
| 正式 journal / year | Journal of Physics A: Mathematical and Theoretical / 2026 |
| 正式 volume / article | 59 / 195201；195201 是文章号，不是起止页；本件不核期号或总页数 |
| 正式 DOI | `10.1088/1751-8121/ae67bf` |
| 官方日期元数据 | Received 2026-01-15；Revised 2026-04-07；Accepted 2026-05-01；Published 2026-05-13 |
| 拟 key | 正式书目可沿 `JoshiRoffelsen2026`；若固定预印本条目则可用 `JoshiRoffelsen2026v2`，二者不重复列作两篇成果 |

本次本人 actual 核准如下，不能把各层级合并成正式版全文阅读：

- [arXiv 固定版本题录](https://arxiv.org/abs/2508.18578v2)：PARTIAL 页内元数据行 8–27，题名、作者、提交历史及版本日期均亲读。
- [arXiv 固定版本 HTML](https://arxiv.org/html/2508.18578v2)：题录、原映射及有限域背景行 35–59，§2 开头行 156–161，以及 **§2.1 全部文字行 162–199**。这是小节文字 FULL、整篇 PARTIAL；Figure 2.1 只读 caption，未作图像阅读；未读整篇 PDF。
- [IOP 官方 DOI 来源](https://doi.org/10.1088/1751-8121/ae67bf)：本次精确 DOI／题名检索返回的官方来源可见内容明确给出上述作者、题名、期刊缩写、卷／文章号、DOI 和四个日期；本人读取了该返回元数据。这是 **publisher-source search-extract metadata 核准**，不是正式页完整 open 或 VOR 正文核读。
- 工具同时报告 `iopscience.iop.org` 的 robots.txt 限制，保留且不重试、不改工具绕取。主控此前 DOI open 的技术 Internal Error 仍是其原失败记录，本件不改称成功。上述可见官方搜索返回不授权访问受限正文。
- 本人 PARTIAL 读 [P30 V4 references.bib](../../30-qpi-vertical-critical-ideals/paper/v4/references.bib) 第 1–11 行的完整 `JoshiRoffelsen2026` 条目，与官方搜索返回的关键出版字段一致；旧 BibTeX 本身不是此次官方核准的替代证据。

检索意外返回的第三方摘录及机构出版列表不用于本件技术判定或补齐正式正文。本次没有下载镜像、调用书目 API、读取凭据或使用付费资源。

## 2. §2.1 真正给出的接口

[§2.1 原文](https://arxiv.org/html/2508.18578v2#S2.SS1) 在有限域对象 $X_{t,s}$ 下写出 Eq. (2.2) 的四个坐标：

| chart | 原文的 $(x,y)$ 表达 |
|---|---|
| 1 | $(x_1^{-1},\ 1+x_1y_1)$ |
| 2 | $(x_2(t+x_2y_2),\ x_2^{-1})$ |
| 3 | $(x_3(t+x_3y_3),\ x_3^2(t+x_3y_3))$ |
| 4 | $((x_4(s+x_4y_4))^{-1},\ x_4^{-1})$ |

Definition 2.1 以这些坐标及 $L_j=\{x_j=0\}$ 描述 torus 加四条 terminal 的初值空间。
同节给出奇异线 $sx-y=0$ 的像、$L_1\to\bar L_2\to\bar L_3\to\bar L_4$ 的逐点演化，并区分 $L_4$ 上 $y_4\ne0$ 返回 torus 与 $y_4=0$ 到 $\bar L_1$ 的分支。
末段明确声明演化可唯一提升为 $X_{t,s}\to X_{st,s}$ 的同构；已读文字没有逐项列全所有邻域的双向正则公式。以上原文接口不是本稿全实提升的完整证明。
原文显示有一个下标不一致：L4 段写成 $L_4=\{x_3=0\}$，而之前统一定义及第 4 chart 对应 $x_4=0$。本件仅标出转录风险，不把该显示不一致改写成新的科学否定；本稿应使用自己核定的第 4 坐标。

## 3. 本稿可消费与不可冒领的边界

可引用的先行接口是上述原 qPI 四 charts、terminal 演化及初值空间上的提升声明；在本稿自主情形取 $s=1,t=T$ 只说明形式对应。
原文 §2 与 Definition 2.1 明确围绕有限域；不能仅替换符号就声称原作者已经给出本稿 $T>0$ 全实空间的完整双向局部证明。
P30 已接受的曲面／有限纤维结论可以继续按实际命题消费，但不能把它与 JR 的原 lift 来源合并为一句“P30 §2 已证明全部提升”。
主控安排的 V2 自足局部核验应承担本稿实际域、开集覆盖、正则延拓及逆映射义务；本件没有读取或验收正在形成的 V2，也不以文献末句替它消除 M1。
本件不消费原文轨道枚举、Hasse 猜想、有限域统计、图像或后文积分构造；没有运行任何数值、参数／阶数枚举或构建。

## 4. 引用建议与终态

关键出版元数据已核至官方来源搜索返回层级，因此可使用正式 `@article` 身份并明确 note／正文定位为实际已读 arXiv v2 §2.1；不得宣称官方正文 open 或两个版本逐字一致。
若作者希望引用条目的身份严格等于本次成功打开并阅读的科学文本，采用固定 `arXiv:2508.18578v2` 的 `@misc` 同样准确，不需要为此恢复受限入口。本件不生成或改写 BibTeX，具体选择由主控在实际 V2 消费时落实。
不把新补充来源算成新意、重开评分或新验收门。本次核查者此前的六项 [引用记录 V1](CITATION_RECORDS_V1_20260913.md) 保持冻结；本件是明确新增的来源补充。
唯一写入为本件，完成后 FULL 读回并交付行数／bytes／SHA；没有修改任何其它项目文件，也未再委派。
