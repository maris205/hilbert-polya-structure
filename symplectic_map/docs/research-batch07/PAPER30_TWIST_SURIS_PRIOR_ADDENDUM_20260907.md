# Paper30 双谐波 twist：Lomelí–Calleja / Suris 定点补核

日期：2026-09-07。仅新增本补记；接续
[先例预核](PAPER30_TWIST_RESONANCE_PRIOR_PREFLIGHT_20260907.md)，不改作者稿、
批次状态或新意判定。不涉及旧 Nonnenmacher 题目。

## 1. 来源与结论

H. E. Lomelí, R. Calleja, *Heteroclinic bifurcations and chaotic transport in the
two-harmonic standard map*, **Chaos** 16 (2006), 023117（8页），
DOI 10.1063/1.2179647。[作者 UNAM 主页](https://mym.iimas.unam.mx/renato/)
的完整出版表收录此文。

已读取[作者公开全文](https://www.researchgate.net/publication/6963059_Heteroclinic_bifurcations_and_chaotic_transport_in_the_two-harmonic_standard_map)
的正文 §I–V；该页明确标示全文由 Renato Calleja 上传，内容保留期刊页码和式号。
这次取得的是作者公开上传的全文文本，不是成功下载的出版社 PDF。
以下页码均为印刷页 `023117-n`。

判定：双谐波模型、异宿作用差零点及 Suris 双项截断机制已有明确先例；
本篇没有给出本题所有互素 \(r/s\) 的加权首项
\(C_{r,s}(\lambda)\) 全根／重数分类。后者仅是本篇范围核对，不是原创性认证。

## 2. 精确对象和关键定位

| 所读位置 | 文献中的对象／结论 |
| --- | --- |
| §I，p.1，(1)–(4)；§II，p.2，(5) | \(r'=r+a\sin(2\pi\theta)+b\sin(4\pi\theta),\ \theta'=\theta+r'\)。生成函数 \(S=\tfrac12(\theta-\theta')^2+V_{a,b}(\theta)\)，\(V_{a,b}=-\tfrac a{2\pi}\cos(2\pi\theta)-\tfrac b{4\pi}\cos(4\pi\theta)\)。 |
| §III，pp.4–5，(7)–(8)，图5–7 | \(\Lambda(a,b)=\sum_{j\in\mathbb Z}[S(w_j,w_{j+1})-S(z_j,z_{j+1})]\)，是两条异宿轨道的作用差。两类零点分别对应交角变号与叶瓣代数面积抵消；图7展示作用差为零而流形仍横截。 |
| §III，p.5，(9)–(10)；p.6，(11)–(12)；pp.6–7，图10 | 从可积 Suris 势导数提取前两正弦系数 \(d_1=-2\delta/\pi,d_2=\delta^2/\pi\)，得到 \(\gamma(\delta)=(-2\delta/\pi,\delta^2/\pi)\)。文中比较它与异宿作用差第一类零点曲线的数值相似性。 |
| §IV，pp.7–8；§V，p.8 | 继续研究异宿切触、作用差间断与输运；不是任意有理周期轨道的首项根定理。 |

以上均据[作者全文](https://www.researchgate.net/publication/6963059_Heteroclinic_bifurcations_and_chaotic_transport_in_the_two-harmonic_standard_map)。
不宜把全文简写成“只有 Melnikov”：其具体工作包含变分／reversor 数值方法、
异宿作用差及 Suris 近似；本补记不追读其引用。

## 3. 与当前规范的对应：独立坐标核算，不是旧文结论

当前预核约定

\[
p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p'.
\]

令 \(q=2\pi\theta,\ p=2\pi r\)，直接代入上表模型，得到

\[
a=\frac{\epsilon}{2\pi},\qquad b=\frac{\lambda\epsilon^2}{\pi}.
\]

因而沿文献的 Suris **前两项截断**曲线，
\(\epsilon=-4\delta\)，且当 \(\delta\ne0\) 时
\(\lambda=1/16\)。这是坐标和幅值的代数换算，不能升级为
\(C_{r,s}(1/16)=0\) 的断言；更不能把仅保留两个 Fourier 项的映射
与原始可积 Suris 映射视为同一映射。完整可积势的被删高谐波在
加权周期共振阶上是否贡献，必须在当前作者证明中另行核算。

本篇的异宿无穷作用和也不能直接认作固定 \(s\) 项周期作用量的相位约化，
其 first/second roots 不是多项式的简单根／二重根术语。

## 4. 本次访问与查询账单

使用 research-lit 技能的一手来源、版本和对象分层要求；限定单篇，未扩展查新。
恰使用两条查询：

1. `"Heteroclinic bifurcations and chaotic transport in the two-harmonic standard map" Lomeli Calleja`
2. `"Lomeli" "Calleja" "2179647" pdf`

第二条无结果。其余为打开已命中来源、作者主页和公开全文的操作。
作者主页的 AIP 链接遇到验证码，停止该入口；未绕过验证码或付费限制。
ResearchGate 公开作者全文可直接阅读；其 PDF 下载链接未成功，因此没有声称
取得 PDF 文件或视觉验收。未下载 arXiv PDF，未上传、发信或改动其他文件。
