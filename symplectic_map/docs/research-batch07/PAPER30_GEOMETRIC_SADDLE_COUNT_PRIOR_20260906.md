# Paper 30：几何周期鞍点计数与 footprint 先验核对

日期：2026-09-06。范围：三篇原始研究文献的有界、公开来源核查；不审查主控提出的乘法秩证明，不创建实验或论文项目。使用 `research-lit` 技能，已完整读取技能和 `docs/WORKFLOW.md`。未保存 PDF、截图或文献语料，仅保存本报告。

## 结论

**固定映射所需的渐近鞍点计数已经直接成立。** 对任意固定复平面多项式自同构 \(F\)，只要动力次数 \(\delta>1\)，有

\[
\#\operatorname{SPer}_{n}(F)=\delta^n-o_F(\delta^n),\qquad n\longrightarrow\infty,
\]

其中 \(\operatorname{SPer}_n\) 是**最小周期恰为 \(n\) 的互异鞍点**，不是轨道数，也不是含重数长度；极限沿所有整数 \(n\)，不是子序列。直接依据是下面 BLS 原始作者稿 Corollary 1。

## 1. BLS：可直接引用的计数定理

E. Bedford, M. Lyubich, J. Smillie, *Distribution of periodic points of polynomial diffeomorphisms of C²*, **Inventiones mathematicae 114 (1993), 277–288**, DOI [10.1007/BF01232671](https://link.springer.com/article/10.1007/BF01232671)。出版社条目确认书目信息；该条目属于订阅预览，未尝试获取其付费全文。实际读取的是作者提交的 [arXiv:math/9301220v1](https://arxiv.org/abs/math/9301220v1)，提交日 1993-01-23、Stony Brook IMS 1993/1、[12 页 PDF](https://arxiv.org/pdf/math/9301220v1)。以下页码及定理编号均指此作者稿，不声称逐字核对过出版 PDF。

| 原文位置 | 精确内容 |
|---|---|
| §1，PDF p.1，定义与式 (1)–(2) | 固定 polynomial automorphism，动力次数 \(d>1\)；\(\mathrm{SPer}_n\subset\mathrm{Per}_n\subset\mathrm{Fix}_n\)。原文区分最小周期与周期整除。 |
| 同页 Theorem 1 | 对上述三种点集任取 \(P_n\)，\(d^{-n}\sum_{a\in P_n}\delta_a\to\mu\)。 |
| PDF p.2，Corollary 1 | \(d^{-n}\#\mathrm{SPer}_n\to1\)。这就是所需结论。 |
| PDF p.1，Theorem 1 前 | \(F^n\) 的含重数固定点数恰为 \(d^n\)，故互异固定点数不超过 \(d^n\)。作者将长度公式归于 Friedland–Milnor；本次没有另读该文。 |
| §3，PDF pp.8–9，Lemma 6 及证明 | 先定义 \(\mathrm{SFix}_n\) 为周期整除 \(n\) 的鞍点；再扣除不超过 \((n/2)d^{n/2}\) 个短周期点转为 \(\mathrm{SPer}_n\)。 |

已读 §1 全部定义及主要陈述、§2 的相关 Pesin box/shadowing 部分、§3 Lemmas 5–6 及 Theorem 1 证明。没有把前一篇 *Polynomial diffeomorphisms of C², IV* 的“鞍点闭包”结论误用作本计数定理。上述原文摘述不作长篇转录。

### 对当前映射的适用性（本报告的推论）

考虑有限复合 \(F=H_m\circ\cdots\circ H_1\)，各 \(H_i(x,y)=(y,p_i(y)-a_i x)\)、\(a_i\ne0\)、\(\deg p_i=d_i\ge2\)，并使用当前项目已建立的 \(\delta=\prod_i d_i\)。这属于 BLS 的对象范围：**允许任意复系数；不要求耗散、不要求 \(|\operatorname{Jac}F|<1\)、不要求整个映射一致双曲、不要求参数泛性。** 特别包括 \(\operatorname{Jac}F=1\)。若改换对象，仍须单独确认是多项式自同构且动力次数大于 1；单凭“辛”字样不足以套用。

若 \(z\in\mathrm{SPer}_n(F)\)，则 \(DF^n(z)\) 的两个特征值分别位于单位圆内外，故

\[
\det(DF^n(z)-I)\ne0.
\]

因此该点是 \(F^n-\mathrm{id}\) 的孤立简单零点。于是记 \(r_n=\#\mathrm{Fix}(F^n)(\mathbb C)\)、\(s_n=\#\mathrm{SFix}_n(F)\)，得到

\[
\delta^n-o_F(\delta^n)\le s_n\le r_n\le\delta^n,
\qquad \delta^n-r_n=o_F(\delta^n).
\]

此简单性和夹逼是本报告的初等推论，而不是给 BLS 添加新的定理编号。若按轨道计数，精确周期 \(n\) 的鞍轨道数才是 \(\#\mathrm{SPer}_n/n\)；当前长度比较不得除以 \(n\)。

## 2. 一致性及有效性：NOT_ESTABLISHED

本次确认的量词是

\[
\forall F\;\forall\varepsilon>0\;\exists n_0(F,\varepsilon)\;
\forall n\ge n_0:\quad \#\mathrm{SPer}_n(F)\ge(1-\varepsilon)\delta^n.
\]

没有在已读文献中建立以下增强版：

- 任意给定紧参数族上的统一 \(n_0(K,\varepsilon)\)；
- 固定任意 \(F\) 的可计算或显式 \(n_0\)；
- 一般性的 \(\delta^n-\#\mathrm{SPer}_n\le C_F\rho_F^n\)、\(\rho_F<\delta\)；
- 仅依赖次数或系数粗界的有效检测周期。

这是 **NOT_ESTABLISHED_IN_THIS_BOUNDED_AUDIT**，不是声称已有反例或穷尽最新文献。紧性和逐点收敛本身不能直接交换量词。BLS 证明中的指数 shadowing 距离及短周期扣除界，也不是整个非鞍点余项的指数估计。

第二篇实际核查：T.-C. Dinh, N. Sibony, *Equidistribution of saddle periodic points for Hénon-type automorphisms of Cᵏ*, [arXiv:1403.0070v2](https://arxiv.org/abs/1403.0070v2)，版本日期 2014-11-26；[PDF](https://arxiv.org/pdf/1403.0070v2) 的内部排版日期另为 July 19, 2018，不混同提交日。已读 Introduction pp.1–5、Definition 1.1、Theorem 1.2，并定向检索全文的 uniform/rate 相关位置。Theorem 1.2 为固定 regular/Hénon-type 自同构给出鞍周期点等分布，还允许指定的指数级乘子分离子集；它没有在陈述中提供本任务所需的参数族一致收敛或计数指数余项。指数混合/乘子分离不等于计数误差指数衰减。该文仅作范围和增强版交叉核查；当前二维计数无需依赖它。

## 3. Footprint：经典方法归属

O. Geil, T. Høholdt, *Footprints or generalized Bezout’s theorem*, **IEEE Transactions on Information Theory 46(2) (2000), 635–641**, DOI 10.1109/18.825832。书目已从[作者出版列表](https://people.math.aau.dk/~olav/publications.html)及[作者机构条目](https://orbit.dtu.dk/en/publications/footprints-or-generalized-bezouts/)确认。实际阅读的是作者列表直接链接的[公开 PDF](https://people.math.aau.dk/~olav/footorgenBez.pdf)：2000-06-16 作者收录版、22 页、内部章节编号 II.16；并非 IEEE 期刊分页。

该扫描 PDF 已实际以流式、内存渲染读取 PDF pp.1–6、22；正文 p.167（PDF p.5）**§II.16.4，Theorem II.16.4** 对任意域 \(k\) 及有限 footprint 的理想给出

\[
\#V_{\bar k}(I)\le\#\Delta_{\prec}(I),
\]

且 \(I\) 为 radical 时取等号。下一页 p.168 明确讨论加入方程、比较 leading-monomial ideal 及缩小 footprint 来估计共同零点。原文本身把此定理归为经典 Gröbner 理论，而非声称首次创造；本次未进一步展开其教材/1998 年参考文献。

对主控的用途：矩形标准单项式中剔除某首项倍数、以标准单项式数控制新增方程的商空间，是 **footprint/leading-ideal 类型的经典方法**。本次没有读到一条直接以“非约化周期环上的乘法秩”表述当前特定乘积式的原始定理，也没有审查主控的首项乘子构造；该专门引理应在项目中自行严格证明，不能把此文的点数定理当成已经验证的乘法秩引理。

## 主控接入边界

已关闭的外部输入只有：固定 \(F\) 的简单几何周期点占长度比例趋于 1，且对每个充分大整数 \(n\) 成立。若主控独立完成一个对固定次数界 \(D\) 的所有非零目标类统一成立的正比例乘法秩下界，文献计数的 \(\varepsilon\) 可以只依赖该比例，从而无需让周期阈值依赖单个可观测量。这个“若”仍以主控的代数证明为前提。本报告不授予整体定理或产物验收 PASS；不需要 Route A/B 评价。
