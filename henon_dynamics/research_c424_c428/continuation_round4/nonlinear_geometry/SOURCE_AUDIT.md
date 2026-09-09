# R4 全维 Vieta：来源适用与局部所有权

2026-09-08 UTC。ARS-Codex 只用于本文件的有界来源核验；数学作者
证明和篇级判断另见 [PROOF_PACKAGE.md](PROOF_PACKAGE.md)。这是
AI 辅助主来源核查，不是独立数学审查，也不是全球查新保证。

## 实际读取的主来源

1. Hu–Tan–Zhang，*Polynomial automorphisms of C^n preserving the
   Markoff–Hurwitz polynomial*。
   [arXiv 元数据](https://arxiv.org/abs/1501.06955)，
   [v2 正文](https://arxiv.org/pdf/1501.06955v2)，
   [出版社记录](https://link.springer.com/article/10.1007/s10711-017-0235-z)。
   元数据核实 v2 为 2015-05-06；期刊在线日期 2017-03-29，
   *Geometriae Dedicata* 192 (2018), 207–243。
   本轮实读：引言的对象／群作用开头、§2.6 dihedral 定义、
   §2.7–2.12 的相关定义及 Lemma 2.2 的全部陈述与证明。
   核心所有权：两零 dihedral 子域、fork 的乘积≤2 估计。
   对象没有本题线性 forcing。其适当不连续区域并非全部整数周期点；
   未从未读的后续区域定理导入逐层显式 R。
   一条聚合检索结果把本标题附近混入 withdrawn 文字；两份实际
   主元数据没有该标记，因此不把聚合片段写成撤稿事实。

2. Eunju Shin，*Fundamental domain for the Markoff-Hurwitz equation*。
   [版本记录](https://arxiv.org/abs/2312.07890)，
   [v2 HTML](https://arxiv.org/html/2312.07890v2)，2023-12-17。
   实读引言／Theorem 1.1、§2.1 图和等价关系、§2.2 的 Lemma 2.1
   及其证明，和 Lemma 2.2 的陈述、证明与随后 remark。
   原文的 a 是最高次乘积系数，不是本题的加性 forcing；定理在
   involutions、排列和双符号变换生成的群商上给基本域。
   `a_source=1` 仅匹配本题 `a_forcing=0`，不能替换单一 F 时钟。
   Lemma 2.1 陈述的 HTML 出现 `|x_j|<|x_j|`，其证明实际得到
   `|x_j|<|x_i|`；这里仅据证明读懂界，不抄排印错误。
   图形未逐幅视觉核验，后续完整 fundamental-domain 证明未读完。

3. Maloni–Palesi–Tan，*On the character variety of the four-holed sphere*。
   [EMS 期刊记录](https://ems.press/journals/ggd/articles/13338)，
   [期刊 PDF](https://ems.press/content/serial-article-files/29746)，
   [arXiv v1](https://arxiv.org/pdf/1304.5770v1)。
   *Groups Geom. Dyn.* 9 (2015), 737–782，DOI 10.4171/GGD/326。
   期刊 PDF 初次正文提取成功，读了引言／定义的实际三变量有线性项
   cubic 与 involutions；后续定位及 p.750 截图因超时失败，不称
   成功视觉检查。备用 arXiv 版本实际只有 v1（2013-04-21）；先前
   对不存在的 v3 请求返回 404，随元数据改正，无该版本证据。
   v1 实读相关对象定义、§3 开头与 Lemma 3.3 全证明；它通过两条
   含加性参数的三角不等式相加，已经给出 forcing fork 机制。
   因此本地 H2 不能被包装为新方法。本文三变量区域理论不是本题
   所有维数的原生周期高度界；未读后部不能用来声称来源绝对没有此界。

以上为三项实读来源，不人为将同一论文两个版本当两个独立支持者。
数学命题的证明来自本地完整推导，不靠来源篇数投票。临床等级、
实验样本、付费索引和 COI 调查均非本次数学适用核验，未伪造完成状态。
无本地 PDF 页码引用或下载，因此未声称执行了本地 PDF 结构预检。

## 本地碰撞和需扣除的内容

- 全文读本批第一轮 `nonlinear_geometry/FROZEN_SCOUTS.md` 中原问题，
  原 scout 报告的数学和来源部分；第二轮同支线的合同、
  `PROOF_AND_GAPS.md` 与来源报告。两零控制和高阶差分不计新结果。
- 读取 C421 的 `research_c419_c423/continuation_round2/integral_return/`
  下 `SOURCE_AUDIT.md` 全文和 `IR1_PROOF.md` 前 200 行；完整 n=3
  分类的所有权保持，不重跑其程序或改写其证书。
- 阅读第三轮 NG2-F 已准入裁决及本批当前状态，扣除整个 n=3 分支。
  既有 Fricke 的跨所有层直线／有限核心穷尽不能直接推出高维结果，
  本次逐层 R 也没有反过来覆盖那个更强的跨层结构。
- 相关目录检索 `fork|height bound|Markoff.Hurwitz|全维|全維`。
  空命中或缺某题名不是新颖性证据。

扣除以上来源后，本轮实际增量应按其本身判断：固定原生循环时钟的
全局最大 h 给两侧更新；用 forcing 符号控制边界 Q=2，并用紧接的
第三个坐标更新排除 Q=±2 退化方向；得到全 n,a,D 的显式完整逐层
高度界。它没有自称方法革命。零乘积全子域的圆周覆盖描述是简单
有限组合推论，不应另计篇。

## 实际查询和访问限制

```text
"Markoff Hurwitz" periodic points cyclic automorphism integral
"Hu" "Tan" "Zhang" Markoff Hurwitz varieties
"Markoff Hurwitz" "linear terms"
"Markoff-Hurwitz" "periodic" automorphism height bound
"Markoff-Hurwitz" "forced" recurrence
"Markoff" "linear" "n variables" involutions
Maloni Palesi Tan four holed sphere fork lemma linear parameters 2015 pdf
"cyclic" "Markoff–Hurwitz" periodic
"Markoff-Hurwitz" "bounded" "periodic points"
```

不相关统计学／线性代数、聚合评论、有限域计数和群图连接性检索结果
未作为支持。Gamburd–Magee–Ronan 的本轮摘要／搜索文本只作背景定位，
其完整新读取未进行；旧轮的实际阅读范围保持，不放大。
初次尝试不存在的第二轮 `PROOF_PACKAGE.md` 返回读错，随后读取
实际 `PROOF_AND_GAPS.md`；不是漏失证明内容或数学执行。

Zotero／Obsidian／arXiv／Semantic Scholar 专用工具本轮目录中未找到；
使用普通主站网页检索。无付费模型、外部稿件上传、GPU、数学程序
或旧认证重跑。源文件存在与适用核查不能代替非作者证明审查。
`NO_BAD_EULER_OR_ROOT_NUMBER` 始终保持。
