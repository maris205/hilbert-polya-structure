# Paper31：完整 V1 作者静态读回与源身份

日期：2026-09-13 UTC。主控：`/root`。
状态：`COMPLETE_DRAFT / AUTHOR_FULL_READBACK_DONE / FRESH_SOURCE_REVIEW_PENDING / NOT_COMPILED`。
这是完整作者稿的实际身份与集成记录，不是 PDF、页数或独立数学票。

## 1. 完整源集合

`paper/v1/` 包含以下 12 件，合计 2,394 行／105,772 bytes。八个编号正文节、独立摘要、
主文件、宏与六项实际消费书目已经齐备；没有空白证明、部分稿试排或先行编译。
主控已 FULL 读回全部实际源至 EOF；随后发生的下述有限集成修改也逐段实际读回。
这些最终身份为当前 fresh 内容审查的输入，审查期间停止源编辑。后续真实修订保留本版并另用明确新版本。

| 源文件（相对于 `paper/v1/`） | 行／bytes | SHA-256 |
|---|---:|---|
| main.tex | 41／1277 | `fcbfe0ac6f8ad6364728e7c86981bd1eef2d912c7d125c6d710a155d50cd53fa` |
| math_commands.tex | 17／577 | `d69b67aa41f2692a1df7c49de52a5299d4f6dcdec8e094d27eb603dc6fa3fc15` |
| references.bib | 60／2263 | `522103caab33d0ac629470d4fa9280590882ce4eeaa155a3fb91630daaa6fe6b` |
| sections/00-abstract.tex | 21／1383 | `6a9eb69e22ee7d7bb005081243c8921bf1bfeebc13017e6c48f1763b9d71e6d6` |
| sections/01-introduction.tex | 104／5531 | `8bcd15098686eb42542c25c703e88f63877e2410cb2757d5fc978e4c03fac5d0` |
| sections/02-real-surface-main-theorem.tex | 435／18906 | `19ee52e55e24ebc0d3287a91d97ea7f27e1b0cb6d1cd46a0e71afa11e209d2cf` |
| sections/03-picard-fuchs-forcing.tex | 174／7007 | `b812c308cce979012123edddf55704bab29a3311563aa5089ec7897f96ed72f2` |
| sections/04-global-frequency-geometry.tex | 430／18174 | `a5bcb49e7c47142e3bcf46fff6d4c3f4dada43a037170daf3b37eb74273e02d8` |
| sections/05-hyperbolic-fibre-estimates.tex | 490／22124 | `2b6c987becda66caf9c5e57e0ada24ca014043aba6a5db11bc7ee50ff90784e6` |
| sections/06-elliptic-jets-endpoints.tex | 341／14435 | `fc9a1d82c9d9d4b60bc680babde6afbeb7f9d6a3aff8286a9a99d9bf6ec686e6` |
| sections/07-global-asymptotics-sharpness.tex | 267／13318 | `57e8263b11320fe657f430d0af3b5eafdc1bb5a86ed8c3662ab2c6cbd33a25a2` |
| sections/08-conclusion.tex | 14／777 | `6cdce0e4e2c29c2f71417f55008b1281317d9f000e3c96ac812498fd561fd9c7` |

## 2. 实际证明责任与集成

| 责任 | 实际英文落点 |
|---|---|
| 完整原对象、真实 +P、实圆、terminal、测度／投影／原范数与完整主定理 | §2 四子节及 `prop:surface`、`prop:real-geometry`、`lem:coarea-projection`、`lem:regular-norms`、`thm:main` |
| 原 PF 还原、无穷 primitive 与移动端点、真实倍数 Wronskian | §3 的 `prop:pf` 及完整三段证明；G0/G1/G2 和全部 Leibniz 项实际排入 |
| 全参数严格频率图及两个中心 jets | §4 四子节；持续圆真实锚、中間存在性、实际2P／表观极点、两无穷端 C1 常数和分类全部实写 |
| 完整 saddle 原时间、原范数、混合 jets 和全模消边界 | §5 四子节；同一双侧 τ、全阶移动入口、外弧／开接缝、倒导数及真实边界分别有证 |
| 原中心 jets、全模有限范数及两类端点常数／余项 | §6 四子节；对称时间角、偶函数下降与有限原阶数、三次 IBP、紧支二次相位积分实际保留 |
| 完整全局相关与原奇偶／sharpness | §7 五子节；绝对可积交换、自足驻相余项、完整分割、两圆交叉配对及合法原实／复下界 |

作者五个分工分别只写 §§3–7，均真实交终态后停止编辑；主控亲读而非只读其摘要。
主控写 §2、首尾、框架与书目，并在全稿集成前作以下局部澄清：

- 将代数开曲面 `mathcal U_T` 与实流形 `U_T` 分开，几何纤维的归属与实 coarea 不混用。
- 将 Pi 的像与 `ker(U-I)` 的区别写为 fixed-point subspace，避免把对易稳定误说成不稳定；明确 G=G_T=F_T²。
- PF 重用已定义判别式，§4 重用 §2 的完成方 cubic，保留各自实际证明而不重复对象定义。
- 节点局部密度改为 H_box，不与全局 H=32T+3h 同名；中心 d_{f,k} 的非首模值明定为零。
- 主定理与 saddle 命题采用同一固定平滑 cutoff 量词；χ可在零附近等于1，但转置证明只需固定光滑紧支，未改变原已接受估计。
- 统一引用的预印本比较措辞；无额外查新、未经核准条目或外文全文阅读冒领。

这些均为冻结前的实际集成，不改变 source/publication locks 或已接受数学。
原必要旧模型可按明确本地未发表稿引用；旧未成篇 PF/twist 及新 K/E/G 不以内部文件引用替代正文证明。
完整原量词、三率、全部系数、C20／逐N的C^(N+2)、全k、两节点四terminal、原奇偶和limsup保持。

## 3. 静态、叙事与引用检查

一次有界只读脚本核12件：102个label唯一、71个被引用label均有定义；6个实际cite与6个BibTeX key恰相等；
逐文件环境栈及非转义花括号平衡。主文件实际输入全部9个section和宏；当前没有旧残留section。
定向文本检查没有TODO/FIXME/XXX/VERIFY、占位证明、附录移证、图片或正文强制分页／缩字命令。
搜索中的英文 small 仅为数学邻域叙述，不是 LaTeX 字号指令。
本检查不能预言 TeX 引擎零错误、引用实际收敛、表宽、自然页数或 PDF 字体。

按 paper-write 做反向叙事核对：引言三方面分别落在 §2/5/6/7 的原观测分析、§3/4/6 的参数分层、
§7 的真实离散奇偶与最优性；结果预览先于技术链，末节只给当前结论与限制。
没有实验、世界首创或普适新阻尼机制申报；最强 FHR／HRSS 先例被正面归属。
书目逐项来自已核[引用记录](CITATION_RECORDS_V1_20260913.md)，不是记忆生成：
FHR／MRVB正式书目附实际固定arXiv版本，HRSS和LLN仅用已核预印本身份，Markov保留扰动，P30为Anonymous本地未发表V4。
文章号071502、77按标准BibTeX的定位字段输出，并在note标明Article，不捏造起止页。

## 4. 下一门与未通过状态

当前 fresh 非作者 `/root/p31_complete_source_actual_review_v1` 正在 FULL 审实际英文稿，
不是重开正式准入四门，也未参与作者修改。其必要问题必须按实际报告处理。
源审查完成后再冻结生产所需完整源身份、真实本地工具／依赖与命令，之后才首次自然编译。
原正文22–30硬窗及全部必要证明保持；作者28.5页不是实测。当前无PDF、无build根或编译输出。
后续双新根字节确定性、真实全页PDF／页界／字体、fresh实际全稿和全页PDF、另一独立终局完整性分别验收。
当前仅完成稿件写作与作者静态读回，不计P31为成品；Batch07仍4/5，最终跨论文审计亦未开始。
