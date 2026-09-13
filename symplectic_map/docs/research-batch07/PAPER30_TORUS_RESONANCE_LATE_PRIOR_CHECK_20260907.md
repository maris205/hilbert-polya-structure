# Paper30 T 分支：三项晚命中文献的定点核对

核对日期：2026-09-07。范围仅限下表三项，不追引文链、不扩展查新，
不做实验、评分或容量评价；旧报告保持不变。

比较对象固定为
$$
F_\kappa=A\circ S_\kappa,\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)),\qquad t=\pi\kappa.
$$
只检查三类直接先例：本精确族的小参数次谱簇、$|t|^{3/2}$ 谱尺度，
以及两条主导支的二阶系数
$-t+(11/12)t^2+O(t^3)$、$-t+(5/12)t^2+O(t^3)$。

## 定点比较

| 一手来源与核对位置 | 实际模型及结论 | 与本次指定结论的关系 |
|---|---|---|
| Elizabeth Diane Keller，*Ruelle–Pollicott resonances of the perturbed cat map*，UCSB 物理博士论文，2007 年 9 月；§2.2，印刷页 10–13，式 (2.2.1)–(2.2.7)；§4.2，页 23–26；§5.2，页 28–31。[作者上传全文](https://www.researchgate.net/publication/252551822_Ruelle-Pollicott_resonances_of_the_perturbed_cat_map) | 实际采用 $A_K=\bigl(\begin{smallmatrix}3&1\\2&1\end{smallmatrix}\bigr)$ 与固定三段线性扰动，具体见下。主要比较周期迹截断与 Fourier 矩阵截断的数值共振；§5.2 提供分形维数背景下的非正式谱下界论述。 | 扣除为**不同的分片模型**。正文的正弦/余弦扰动仅为一般例子；“sine/cosine resonances”还指奇偶 Fourier 基，不表示采用纯正弦动力学。其 §5.2 的 $\kappa$ 是固定收缩因子，不是趋零的耦合参数。未给本次三类结论。 |
| A. Ostruszka、C. Manderfeld、K. Życzkowski、F. Haake，*Quantization of Classical Maps with tunable Ruelle–Pollicott Resonances*，Physical Review E **68**, 056201 (2003)；§II，式 (2)、(3)，PDF 页 2–4；§V，PDF 页 13–14；附录 A，PDF 页 16。[一手全文](https://arxiv.org/pdf/nlin/0301041) | 模型为正/负耦合的分片 baker 映射，随后转到球面。若干耦合值有 Markov 转移矩阵给出的次大共振，其他共振以小噪声有限矩阵近似。§V 的另一个简化模型确有精确可调共振 $\lambda=1-2\Theta/\pi$。 | 扣除为**不同系统族**，不能笼统说它“只有数值结果”。其可控共振与解析转移矩阵不对应本纯正弦 cat 族，也未提供指定的 $3/2$ 谱尺度或 $11/12,5/12$ 系数。 |
| S. Nonnenmacher，*Spectral properties of noisy classical and quantum propagators*，Nonlinearity **16**, 1685–1713 (2003)；§2.1.3，页 1688；§3.1，页 1690–1691；§4.3 定理 1，页 1700；§5.2(c) 与图 6，页 1708。[作者全文](https://www.imo.universite-paris-saclay.fr/~stephane.nonnenmacher/publis/Nonnen2003%28Nonlinearity%29.pdf) | 理论部分讨论一般 Anosov 映射的零噪声外环谱极限，以及固定噪声下的量子—经典谱极限。具体 perturbed-cat 数值例子采用 $\cos(2\pi q)-\cos(4\pi q)$ 双谐波项，固定 $\kappa=0.5/(2\pi)$、$N=40$，与既有七个经典共振比较。 | 一般噪声谱理论是背景，**不是耦合参数趋零的谱展开**；该具体数值例子也不是本纯正弦族。没有把 $\epsilon\to0$ 或 $N\to\infty$ 当作 $\kappa\to0$，未给本次指定三类结论。 |

## 模型与来源细节

Keller 的实际扰动在式 (2.2.3) 明确为
$$
f_K(q)=\begin{cases}
-q,&0<q<1/3,\\
2(q-1/2),&1/3<q<2/3,\\
1-q,&2/3<q<1,
\end{cases}
$$
边界按连续延拓解释；作用为 $A_K(q,p)^T+f_K(q)(1,1)^T\pmod1$。
式 (2.2.5) 的两块有效矩阵分别是
$\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ 和
$\bigl(\begin{smallmatrix}5&1\\4&1\end{smallmatrix}\bigr)$。
因此其中局部出现本项目的 $A$，不构成整族相同。
来源是作者在 ResearchGate 上传的博士论文完整正文文本；
读取了正文模型和结果段落，不只依赖摘要。页面显示的单位与月份元数据不替代论文封面上的 UCSB、2007 年 9 月信息。
[同一作者上传正文，§2.2](https://www.researchgate.net/publication/252551822_Ruelle-Pollicott_resonances_of_the_perturbed_cat_map)

Ostruszka 等的文献年份按期刊发表记为 2003；实际核对的是
arXiv:nlin/0301041v2，修订日期为 2004-01-19，共 18 页，
所列页码均为该 PDF 页码。两者并不矛盾。
[arXiv 作者提交记录与期刊元数据](https://arxiv.org/abs/nlin/0301041)

Nonnenmacher 的数值例子在印刷页 1708 原文所印为
$$
A_{\rm nl}(q,p)=
\bigl(2q+p,\ 3q+2p+\kappa[\cos(2\pi q)-\cos(4\pi q)]\bigr).
$$
这里按原文记录，不为它补改映射公式；仅双谐波与其线性部分已足以区分本次对象。
§2.1.3 虽列出 Arnold 矩阵及一般 $M=\phi_H^1\circ A$，
却没有由此给出指定纯正弦族的参数级数。
§3.1 的一般零噪声结果有外环条件；实解析情形向任意正半径推广在该文中仍标为猜想，
不能倒填为本文所需的已证明小耦合展开。
[同一作者全文，页 1688、1690–1691、1708](https://www.imo.universite-paris-saclay.fr/~stephane.nonnenmacher/publis/Nonnen2003%28Nonlinearity%29.pdf)

## 结论与覆盖边界

在这三项的一手模型、定理和相关结果范围内，未发现本纯正弦族指定小参数结论的直接先例。
这是有明确模型差异支撑的**三项来源排除记录**，不是穷尽文献证明，
不是新颖性 `PASS`，也不授予任何 Route 或候选评价。

本次实际使用 2 条定点搜索：Keller 的精确题名与年份、arXiv:nlin/0301041 的精确标识；
其余为指定来源的打开、全文定位和读取，未追加引文追链。
按 `research-lit` 技能区分了模型身份、解析结论、噪声极限与数值证据；
该技能的一般扩展检索建议服从本次三篇、最多六条查询的锁定范围。
