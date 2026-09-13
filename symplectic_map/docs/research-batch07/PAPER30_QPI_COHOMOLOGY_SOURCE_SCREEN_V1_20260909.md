# Paper30 qPI：完整圆分模型的上同调来源预筛 V1

日期：2026-09-09。执行者：主控 /root。
类型：有限问题定位与来源扣除，不是完整 novelty-check、正式票或全球先例排除。

## 1. 固定比较量与当前结论

对象为[完整模型 G1–G3 作者诊断](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)：
同一个圆分 DVR 上的八吹起曲面、原 $r=mp^a$ 阶 pencil 的平坦降阶、
$\mathcal T=H^1(\mathcal S,\mathcal O(r\mathcal D))_{\rm tors}$ 的过滤与长度，
以及其与原整除微分的准确数值对应。G 的非作者检查在本件写作时仍运行。
另一个有界任务正在判断过滤能否分裂，本件不使用其尚未提交的结论。

**本轮没有取得足以评价完整新问题新意的文献覆盖。**
已核的新近邻把一般复数 Okamoto–Painlevé 对的正则函数、纤维化与变形上同调明确纳入旧文献；
其实际已读量并不是本题圆分整数线丛上同调，也没有给出本题的 torsion elementary divisors。
后一句是阅读范围内的对象区别，不是排除其他章节、其他版本或其他文献的证明。

## 2. 实际检索及访问范围

使用 research-lit 的对象／来源分级；沿当前白名单做定向本地证明读取及公开网页查询，
不重扫旧论文库、不重新开启旧正式输入、未下载本地 PDF、未调用书目 API 或付费访问。
新提交八个主题查询及一个精确题名定位如下：

1. `"Halphen" "torsion" "cohomology" "reduction"`
2. `"Halphen" "mixed characteristic"`
3. `"genus one" "normal bundle" "DVR" cohomology`
4. `"Painlevé" "cohomology" "cyclotomic"`
5. `Halphen surfaces family anticanonical cohomology root unity torsion specialization`
6. `"Painlevé" "anticanonical" "cohomology"`
7. `"Halphen" "base change" "cohomology"`
8. `"rational surfaces" "cohomology" "1-q"`
9. `"Deformation of Okamoto-Painleve pairs" arxiv Saito Takebe Terajima`

搜索中出现的四维 qPI、其他 Painlevé 型、镜像与量子上同调仅是邻域线索；
未确认原系统身份者不作原 qPI 直接先例，跨族研究仍属 ROUND2_CLUE。
搜索无命中及不相关结果都不计新意正证据。

## 3. 新取得的一手原文与严格区别

Masa-Hiko Saito、Taro Takebe、Hitomi Terajima，
*Deformation of Okamoto–Painlevé Pairs and Painlevé equations*，
J. Algebraic Geom. 11 (2002), 311–362，DOI 10.1090/S1056-3911-01-00316-2。
[arXiv 元数据](https://arxiv.org/abs/math/0006026)确认作者 v2 为 2000-09-18；
正文实际读[该作者 v2 PDF](https://arxiv.org/pdf/math/0006026)，不是出版 PDF。
元数据称 38 页，当前在线 PDF 解析为 39 页；不据此完成 PDF 页数／视觉验收。
v2 HTML 返回 cache miss，沿元数据的公开 PDF 链接成功，不涉及访问限制绕行。

实际阅读：引言与 §1 的文字（含 Definition 1.3、Proposition 1.3 及其证明），
§2 开头至 Lemma 2.1 的返回文字；定点检索另带出 Proposition 2.1 及其证明；
再读 Proposition 2.2 的完整陈述／证明、§3 从开头到 Lemma 3.1 的陈述。
没有读取全文，没有解读图 1–2 的节点排布；本文比较不依赖那些图。

具体扣除与边界：

- §1 以复数广义有理 Okamoto–Painlevé 对为对象，Proposition 1.3 将非纤维化与开放面正则函数仅为常数联系起来；
  因而“积分存在与 Halphen 纤维化相关”不是本轮新一般机制。
- §2 的变形量为 $H^1(S,\Theta_S(-\log D))$，§3 的时间方向用
  $H_D^1(\Theta_S(-\log D))$ 描述；这与 $H^1(\mathcal S,\mathcal O(n\mathcal D))$ 的整数扭子是不同的 sheaf、底环和问题。
- 所读 §3 明确取非纤维化型，Theorem 3.1 再取 additive 型；不把这些条件移除后直接代入本题 multiplicative 八环。
- 本轮不讨论该文 Conjecture 3.1 的后续解决状态，不将其与本题新问题混为一谈。

标准几何事实另由 G 作者证明中实际核准的 Stacks 0AVB、039C 以及短正合列提供。
正常延拓、逐纤维平坦、节点环粘合、长正合列与 DVR 长度均是标准工具；
实例中算出了精确量，不意味着这些工具本身创新。

## 4. 对 Hasse 部分的主控核准

主控完整读取[整除微分来源差分](PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md)，
并亲读 [Vlasenko 作者 v3 §1 定义 (1)–(4)、Theorem 1(i)–(iii) 及半线性解释](https://arxiv.org/html/1605.06440v3)，
以及 [Achter–Howe 作者 v5 §3.1 和 §3.3](https://arxiv.org/html/1710.10726v5)。
来源差分 §3 的 Newton 面积／唯一内部点、倒数级数系数识别与 Frobenius 代入均经主控重算一致。
因此将 Hasse 几何级数次幂归入 Vlasenko Theorem 1(i) 是具体适用，而非仅按标题联想。
该定理的 (ii)–(iii) 要求 Hasse 可逆，不能补全本题超奇异处的下一阶。

## 5. 下一步边界

应先收口 G 独审及扭子分裂诊断，固定真正新增的完整数学主张，
再对该主张开展完整多来源查新和组合内非碰撞；当前不能据九条查询判定其新颖。
若最终只剩标准边界上同调的直接应用，应如实扣除，不把旧票失败变成提高分数的理由。
本件不创建 V3、source/publication lock、论文稿或 PDF，不修改旧评分与 T1–T7。
