# GR5 来源先行与适用边界

2026-09-08 UTC。首版与合同一起写入。AI 辅助的有界来源核查，不是
人类同行评审、整库穷尽或全球优先权认证；ARS-Codex 仅作 source
fact-check，纯数学按命题/证明适用性核验，不套用医学试验等级。

## 冻结前实际主来源

| 来源 | 实际访问范围 | 所有权/不适用边界 |
| --- | --- | --- |
| Shu Kawaguchi, [Local and global canonical height functions for affine space regular automorphisms](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf), ANT 7 (2013), 1225–1252 | 出版社 PDF：摘要/引言及 Definition 4.1、Propositions 4.2–4.3 的陈述和正文证明；§6 相关陈述部分，非 31 页完整通读 | regular good reduction 定义、Green 函数及几乎处处好约化；不直接给全仿射归约和非主理想全局判据 |
| Nils Bruin, Alexander Molnar, [Minimal models for rational functions in a dynamical setting](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3294C6C9B556A6D2D1EC553E168BAD5D/S1461157012001131a.pdf/minimal_models_for_rational_functions_in_a_dynamical_setting.pdf), LMS J. Comput. Math. 15 (2012), 400–417, DOI 10.1112/S1461157012001131 | 出版社 PDF：引言、Propositions 2.9–2.12/Corollary 2.13 的原文，§6 的命题与 Example 6.4 完整论证；非整篇算法/实验通读 | 一维有理映射局部最小化、仿射与全 PGL_2 最小模型的差别和非主理想例子均先扣除。其 Aff_2 是一维射影直线的上三角矩阵记法，不是本题二维 Aff(A²) |
| Clayton Petsche, Brian Stout, [Global minimal models for endomorphisms of projective space](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.889/), JTNB 26 (2014), 813–823, DOI 10.5802/jtnb.889；[作者版 arXiv:1303.5783v1](https://arxiv.org/pdf/1303.5783v1) | 冻结前：期刊 metadata/摘要及 PDF 初始定义；两次按行打开与两次 find 返回 Internal Error。冻结后：改读作者 v1，已读引言/Theorem 1/Corollary 2、§2 Proposition 3 与 Lemmas 4–5、§3 Proposition 6/Lemma 7、§4 主定理及推论证明，均含正文证明；分两次实际覆盖该 11 页作者版全部提取文本。未声称完整通读期刊最终 PDF | PID 上格拼接与射影态射模型定理属已有方法；不能延伸成任意类群或 Hénon 双有理紧化结论。作者版的格自由性依赖 PID；本文另给一般理想平方自由性的直接构造 |

Petsche–Stout 卷年为 2014，主站另列 2015-03-09 上线日期；不混作
两个不同版本。所有 PDF 都是网页远程读取，没有在仓库下载或生成 PDF。

## 本地检索和工具范围

完整读根/henon AGENTS、最新 R5 状态入口、R5 PLAN、批次 skill/workflow、
idea-creator、research-lit、proof-writer，以及 ARS source-fact-check
所需入口/引用。部分合并返回截断后已分段补读所选技能说明。
只读 CURRENT 的最新与相关快照段，不称其整部历史全读。

先以 rg 在 candidate/obstruction registry 查 number field、integral
point、good/bad reduction、ideal class/class group 等，再在 henon 的
Markdown/TeX 中窄查 minimal model、potential/everywhere good reduction、
Steinitz、projective module、affine conjugacy。没有命中同一 GR5 完整题。
AM1 有理仿射变换命中只涉及既有周期分类；不以关键词交集证明不碰撞。

可用工具目录没有 Zotero/Obsidian/arXiv/Semantic Scholar 专用接口。
相关 henon papers/literature 及 arxiv_fetch.py 检索未发现可直接使用
的相关本地 PDF/脚本；未扫描另一研究流的根 papers/。
使用公开网页和主站原文；没有程序化 S2/DOI 验证、付费 API、外部模型
上传或专业索引订阅核查，不虚报这些检查已完成。

## 实际网页查询（冻结前 12 条）

均无 domains/recency 过滤，返回长度 long；原样字串如下。
未检索到相同定理不等于新颖性成立。后续新增查询若有另列。

| # | 原样查询 |
| --- | --- |
| 1 | "polynomial automorphisms" "good reduction" "number field" |
| 2 | "Hénon" "minimal models" |
| 3 | "Hénon" "ideal class" reduction |
| 4 | "polynomial automorphism" "potential good reduction" |
| 5 | "global minimal models" "affine" dynamics |
| 6 | "Hénon" "models" "reduction" arithmetic |
| 7 | "polynomial automorphisms" "Dedekind" |
| 8 | "minimal models" "ideal class" dynamics |
| 9 | "Hénon" "good reduction" "conjugate" |
| 10 | "Henon" "Steinitz" |
| 11 | "polynomial" "good reduction" "class group" 2025 2026 |
| 12 | "Global minimal models for endomorphisms of projective space" Petsche Stout arxiv |

## 冻结后核验与实质性边界

冻结后没有新增网页查询；新增的是同一 Petsche–Stout 作者版正文
的定向读取。协调者自行进行的补充检索应以其独立来源文件为准，
不混入上述 12 条作者查询数。

`PROOF_PACKAGE.md` 已写出冻结题的完整作者手证。所有权先行扣除：
regular good reduction 定义与一般局部 Green 结构、一维好约化
圆盘的经典逃逸判据、一维仿射最小模型的既有非主理想现象、
加法逼近及一般格/Steinitz 行列式机制，均不是本题单独的新贡献。

请求非作者审查的残余是正逆最高项不定点强制的**全部二维仿射
格局部刚性**，及其对任意数域、全部单因子系数族给出的完整模型
分类与精确平方障碍。显式例子展示二阶类可由混合坐标修复而
三阶类不能，但例子不是另加的新合同；经典理想也不是新发现。

状态：作者 `PROVABLE AS STATED`，未非作者准入。来源存在、原命题
适用、作者推导成立、实质性准入与 Route-A 目标算术各自分账。
没有声称全球优先权或专业索引穷尽。NO_BAD_EULER_OR_ROOT_NUMBER。
