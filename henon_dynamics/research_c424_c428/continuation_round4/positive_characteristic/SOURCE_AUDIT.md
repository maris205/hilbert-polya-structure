# ROUND4-PC424-L：实际来源访问与适用性核查

2026-09-08 UTC（按实际执行时钟校正日期）。使用 `research-lit` 的相关本地优先检索和主来源回退，
配合 `proof-writer` 区分原命题、辅助证明与未证引理。已完整读取本仓库
及 Hénon 的 AGENTS、当前状态最新入口、第四轮 PLAN、批次技能及完整
WORKFLOW、research-lit 与 proof-writer 入口。本文件不替代数学证明、
非作者审查或准入裁决；本 lane 没有执行 ARS 全流程、外部审稿或模型调用。

## 本地所有权和访问范围

实际完整读取：R3 本 lane 的合同／证明／来源核查；R2 主证明、来源核查
及协调者 PC-L 跟进；首轮冻结合同。已扣除正规形、集合转移、插值、
二进制支撑检测、nilradical／Frobenius 必要界、有理无极点和 R3 新素周期
定位。更早的辅助证明通过上述已读文档定位，未冒称重读整个前史。

另以 `rg` 检索 Hénon Markdown／TeX 的 coboundary、Livšic、重数界、
高切触、Jacobian／trace 等词；随后缩小到本批与 C402 残差迹目录，检索
trace pairing／annihilator。实际完整读取旧 C402 的
[第三节](../../../continuation_c399_c403_round2/nonlinear_return/paper/sections/3_residues.tex)：
它保留完全交长度、留数与重数，在简单点上才给普通分母解释。
其有限矩阵与全概形留数不是本合同的普通本原轨道和。常规有限代数的
迹核／对偶事实不主张为新所有权；本轮只给它们在剩余缺口上的精确适配。

工具目录未找到 Zotero、Obsidian、arXiv 或 Semantic Scholar 专用方法。
在仓库 `tools/` 与两处指定 arxiv 技能路径中未找到 `arxiv_fetch.py`，
遂按技能的缺脚本回退作 arXiv 定向网页检索。根 `papers/`／`literature/`
PDF 文件名筛选没有得到与本问题对应的主来源 PDF；不读取无关 symbolic
论文凑数。没有下载来源 PDF，也没有声称本地 PDF 页码锚点已核查。

## S1 刚性不等于横截性

Alon Levy，arXiv:1201.1969v2，2012-11-30。
[arXiv 记录](https://arxiv.org/abs/1201.1969v2) 的标题为
*An Algebraic Proof of Thurston's Rigidity for a Polynomial*；
[正文标题](https://arxiv.org/html/1201.1969v2) 为
*An Algebraic Proof of Thurston's Rigidity for Maps With a Superattracting Cycle*。
保留二者差异，不把它们混成两篇文章。

实际正文访问：完整 Introduction 的定义 1.1--1.6、Theorems 1.4、1.7、
Conjecture 1.8、Theorems 1.9--1.10、Corollaries 1.11、1.13、Theorem 1.12
及其相邻限定；Section 2 开头和 Lemma 2.1 证明。没有读完完整有限性证明。

正文明确以固定临界 portrait 的有限性区别于横截性，并指出正特征二次
族的横截性可以失败。文章的有限性不是本合同所需的新本原周期接触阶
全局上界。本轮仅据此排除该未经证明的推论，不否定刚性定理。

最初作者 KTH PDF 路径 `https://people.kth.se/~alonlevy/rigidity4.pdf`
打开返回 404。搜索缓存片段只作定位；后来的上述主 arXiv 正文才是
实际正文证据。没有声称失败 PDF 已读。

## S2 固定中心的 p-adic 离散性不是所需重数上界

Manfred Einsiedler、Graham Everest、Thomas Ward，
*Periodic points for good reduction maps on curves*，
arXiv:math/0307089v1，2003-07-08；访问
[主 arXiv HTML 正文](https://arxiv.org/html/math/0307089v1)。

实际读取 Introduction 的域／度量定义、Theorems 1、3、Corollary 2；
Section 2 的良约化定义、Proposition 9／Corollary 11 的前引陈述、
Lemma 5、Remark 6、Lemma 7 及其完整显示证明、随后 Theorems 1、3 的
显示证明。Section 4 支撑引理的完整证明未核读。

定理工作在 $\overline{\mathbb Q}_p$，离散性是固定中心、每个 $r<1$
的结论。它不提供移动周期中心、整个开单位残差圆盘内的统一总数。
因此不能直接变成本合同在 $\overline{\mathbb F}_p$ 上的新素周期最大
根重数界；特征零的重复重数陈述也不能直接搬到特征 $p$。

## S3 Hilbert 90 的字段时钟不是原生二次时钟

S. P. Glasby，*Hilbert's Theorem 90, periodicity, and roots of
Artin-Schreier polynomials*，arXiv:2505.00346v1，2025-05-01，预印本。
[记录](https://arxiv.org/abs/2505.00346v1)，
[主 HTML 正文](https://arxiv.org/html/2505.00346v1)。

实际读取 Introduction、Theorem 2.1、Lemma 2.2 及其显示证明；
Section 3 的 Theorem 3.1、证明和相邻 Lemma 3.2／Remark 3.3；
Section 4 开头、Corollaries 4.1--4.2 与后者证明。后面的完整根公式表
及其全部证明未作审计。

所用算子是有限循环 Galois 字段扩张的生成元，特殊情形为 Frobenius。
这里的 $x\mapsto x^2+c$ 在 $k(x)$ 上诱导非满的次数二嵌入，不是有限阶
字段自同构；有限轨道上的循环作用也不产生一个全局 $Q\in k[x]$。
因此本来源不是原合同的正则性定理，也不据此另开第二题。

## 实际新查询记录

以下 **16 条** 是本轮真正提交的搜索字符串，分四批，每批四条；
没有 recency 或额外 domains 过滤。`site:` 属于所列字符串本身。
直接打开、find、失败定位和本地检索不算搜索字符串。

1. `site:arxiv.org polynomial dynamics positive characteristic periodic point multiplicity uniform bound`
2. `quadratic polynomial finite field multiplicity periodic points high contact dynatomic discriminant`
3. `algebraic Livsic theorem finite characteristic polynomial cohomological equation`
4. `polynomial additive cocycle periodic orbit sums Artin Schreier`
5. `"characteristic" "multiplicity" "periodic points" "bound" polynomial dynamics`
6. `"positive characteristic" "Fatou-Shishikura" inequality`
7. `"finite fields" "parabolic cycles" quadratic`
8. `"quadratic" "periodic points" "multiplicity" "p" ramification`
9. `"dynatomic" "multiplicity" "singular" "characteristic"`
10. `"quadratic" "transversality" "positive characteristic"`
11. `"periodic points" "good reduction" "multiplicity" postcritically finite`
12. `"polynomial" "high multiplicity" "iterate" finite field`
13. `"An Algebraic Proof of Thurston" Levy arxiv`
14. `"polynomial" "trace pairing" "periodic points" finite fields`
15. `"dynatomic" "transversality" "multiplicity" positive characteristic`
16. `site:arxiv.org "polynomial" "coboundary" "finite field"`

搜索另出现旧局部 ramification、复杂动力学、特征零 split-map、
Artin–Schreier L-function、dynatomic 及程序项目条目。除上述实际读取的
主正文以外，它们都是 leads，不把摘要／缓存片段升级为适用定理。
无世界文献穷尽、优先权清白、发表准备或期刊／撤稿全审计声明。

## 来源角色结论

三项来源均未在实际核读范围内供应原完整正则性或式 (8) 的全参数上界。
这个结论是有限访问范围的结果，不是不存在此类定理的证据。
本轮辅助代数命题由作者直接证明，未以临近引用替代证明或伪称非作者审查。
`NO_BAD_EULER_OR_ROOT_NUMBER` 保持；没有目标算术或 Route-B 结论。
