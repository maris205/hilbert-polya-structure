# 双谐波首共振根结构：定点文献桥接检查

日期：2026-09-07。身份：主控一手检索与对象辨析，非数学终审或新意票。
使用 research-lit 技能；其来源和证据分层要求决定了下面的未匹配限定。

## 1. 结果

本轮找到必须核对的更强结构类比：双谐波 **线性 Hill 算子** 的小振幅谱隙
首系数已经有全阶乘积公式和对应的路径组合恒等式。
但它不是本题非线性周期作用量的系数；本轮没有证明二者身份，不能借用
该公式宣称本题全实根，也不能把已有乘积公式改记号作为新发现。

| 一手材料 | 实际阅读及结果 | 本题边界 |
| --- | --- | --- |
| P. Djakov、B. Mityagin，*Asymptotics of instability zones of the Hill operator with a two term potential*，2005 arXiv 作者预印本 math-ph/0509034 | [官方元数据](https://arxiv.org/abs/math-ph/0509034)及[作者 HTML](https://arxiv.org/html/math-ph/0509034)的引言、§3 Theorem 7 与证明、§4 Theorem 8 与证明 | 给出固定谱阶的小振幅首系数乘积、正步长路径和及非邻接位点恒等式。未给出本题 $C_{r,s}$ 的身份。 |
| Daniel Tsodikovich／Corentin Fierobe，*Local rigidity of the Suris potential as an integrable standard twist map*，2026-02-03 学术报告公告 | [Roma Sapienza 官方公告](https://www.mat.uniroma1.it/it/local-rigidity-suris-potential-integrable-standard-twist-map)的摘要 | 公告涉及可积 Suris 势的局部刚性；不是已读证明，不提供加权双谐波截断的共振根定理。 |
| H. E. Lomelí、R. Calleja，*Heteroclinic bifurcations and chaotic transport in the two-harmonic standard map*，Chaos 16 (2006), 023117 | 定点代理已读作者公开上传全文 §I–V，主控全文读取[独立补核](PAPER30_TWIST_SURIS_PRIOR_ADDENDUM_20260907.md) | 其根属于异宿全作用差，不是任意旋转分母首项多项式的根；Suris 双项截断也不等于完整可积映射。 |

前两项的文献身份不同：第一项为实际读到内容的作者预印本；第二项仅为
官方学术报告摘要。二者都不是本题的新意认证。

## 2. Hill 谱隙桥接为何尚未成立

Djakov–Mityagin 的 Theorem 7 研究
$-y''-[4\alpha t\cos2x+2\alpha^2\cos4x]y$ 的谱隙，
其小振幅首项在偶数谱阶含 $\prod(t^2-(2k-1)^2)$，奇数谱阶有相应偶数根。
证明先将 Fourier 展开化为从 $-n$ 到 $n$、步长为 $2,4$ 的正向路径；
再利用 Hill 方程的指数规范变换及谱重数得到根。
这些是该线性谱问题中已经存在的结构结果。
[作者全文，§3–4](https://arxiv.org/html/math-ph/0509034#S3)

以下区别由本轮实际公式比较得到，而非原作者对本模型的评价：

- 该路径和的传播子分母为 $n^2-j^2$，端点是两个共振 Fourier 模式。
- 本题先消去非线性配置变量，递推含 $e^v$ 和 $e^{2v}$，传播子为
  $4\sin^2(\pi rk/s)$；其展开有任意分叉的有根树，不是仅有步长1、2的路径。
- $r/s$ 的分子改变本题小除数序列；不能把线性谱阶 $n$ 单独换成轨道分母 $s$。

所以从已知自伴 Hill 算子推出“本题也是对称 Jacobi 特征多项式”的步骤仍缺失。
需要一个明确且保留参数根的恒等变换；本轮没有找到这样的证明。
无关模型的定理记为方法背景／待检验类比，不与本题证明拼接。

本轮补核将该 Suris 双项截断换到当前幅值规范，得到 $\lambda=1/16$。
结合实际三周期系数 $C_{1,3}=\lambda-1/24$，有
$C_{1,3}(1/16)=1/48\ne0$；这是本轮两条已核对公式的代数推论，
并非旧文的结论。因此不能把完整 Suris 势的可积性移植给双项截断，
再据此假定它使所有分母的首共振都消失。

## 3. 查询与本地来源范围

主控先执行以下八条主题查询，再对命中的一篇论文做一条准确题名查询：

1. `"standard map" "resonance" "polynomial" "roots"`
2. `"Whittaker-Hill" "gaps" "polynomial" Djakov Mityagin`
3. `"generalized standard map" "two" "resonance" cancellation`
4. `"discrete" "Whittaker-Hill" polynomial`
5. `site.arxiv.org "Asymptotics of instability zones" "two term"`
6. `"standard map" "resonance" "real roots"`
7. `"Suris" "integrable" "Fourier" standard map`
8. `"semistandard" "polynomial" "zeros"`
9. `"Heteroclinic bifurcations and chaotic transport in the two-harmonic standard map"`
   （限定 AIP、作者／机构域名；只取得后续论文参考文献中的准确作者书目，
   不以这些二手引用代替原文内容）。

Zotero／Obsidian 工具未配置，技能指定 arXiv 脚本所在工具目录不存在，
故用官方 arXiv 网页回退。工作区无独立 `literature/`；按相关文件名排除
构建／依赖树后的本地 PDF 筛选只命中无关的 cat 图，没有将其作为文献。
没有重新遍历旧构建，没有下载 arXiv PDF，没有外部写入。

## 4. 当前结论

Berretti–Gentile 的通用递推／树系数覆盖沿用
[已读一手预核](PAPER30_TWIST_RESONANCE_PRIOR_PREFLIGHT_20260907.md)，不重开。
本次新增的 Hill 乘积公式是强背景，但精确对象身份仍 `OPEN`。
搜索未匹配不等于世界范围不存在；全球新意保持 `UNCERTAIN`。
没有正式四门评分或自然正文容量结论，不按这份文献笔记为论文增加篇幅。
