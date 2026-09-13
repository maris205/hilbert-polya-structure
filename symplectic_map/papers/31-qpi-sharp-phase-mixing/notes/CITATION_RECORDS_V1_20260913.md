# Paper31：六项实际消费来源的引用核准记录 V1

日期：2026-09-13。核准者：`/root/p31_q2_citation_scaffold`。
状态：BIBLIOGRAPHIC_METADATA_CHECKED / CITATION_SCAFFOLD_ONLY / BIBTEX_NOT_FROZEN。
本件依 paper-plan Step 5 核准六项已选来源；不是新查新、评分、正文证明复核或完整论文计划。
唯一写入本件；未生成 BibTeX、稿件或 PDF，未调用程序化书目 API、外部模型、付费资源或凭据。

## 1. 入口与读取身份

本次本人 FULL 读 [正式准入处置] 126 行及 [共同清单] 178 行。
二者记录的既有科学实读是此前主控及两个 fresh 正式席各自的工作，不能改称本核准者重读了这些正文。
下列各项将本次实际元数据核准、此前固定正文核读范围、准许用途及不支持的主张分别记录。
网页定位行号只辅助说明本次返回内容；来源身份以正式 DOI、固定 arXiv 版本或明确本地路径为准。
正式席句柄为 `/root/p31_q2_formal_v1_r1`、`/root/p31_q2_formal_v1_r2`；其阅读范围由 [正式准入处置] §3 绑定。
本次没有重读 38 项数学输入，没有重跑此前来源检索阶段，也未把任何人的阅读改称真人或跨模型评审。

## 2. FHR：正式期刊身份，科学比较绑定 arXiv v1

| 字段 | 核准值 |
|---|---|
| 拟 key | `FaouHorsinRousset2021` |
| Authors | Erwan Faou; Romain Horsin; Frédéric Rousset |
| Title | On Linear Damping Around Inhomogeneous Stationary States of the Vlasov-HMF Model |
| Year / venue | 2021; Journal of Dynamics and Differential Equations |
| Volume / pages | 33; 1531–1577；期号本次不另填 |
| Published / VOR | 2021-08-06 / 2021-08-06；官方 issue date 为 September 2021 |
| DOI | `10.1007/s10884-021-10044-y` |
| 实际科学版本 | `arXiv:2105.02484v1`，2021-05-06 |

本次 actual 核准：[Springer 官方页面](https://link.springer.com/article/10.1007/s10884-021-10044-y) 的题名、作者、期刊及卷页（返回行 11–33）和 Cite this article／日期／DOI（174–191）；[arXiv 固定版本页](https://arxiv.org/abs/2105.02484v1) 的题名、作者、版本及提交记录（8–25）。未进入订阅正文。
此前正文核读身份：两正式席各自读取 [v1 PDF](https://arxiv.org/pdf/2105.02484v1) 第 1–6、25–32、34–40 页，共 21/42 页，含 Th2.2 与指定 §7 命题和证明。Lemma7.15 的证明仍未读，不能称整篇 FULL。
用途：引言／相关工作中明确扣除跨 separatrix、原光滑观测、无限 Fourier、节点任意有限幂与中心 jets 的既有分析技术；在节点与中心分析入口承认直接先行工作。
不支持：不能把本稿写成首次跨节点的相混合理论，也不能将 FHR 的 Vlasov-HMF 结论直接称为本 qPI 全参数 sharp 双相关定理。
未来可优先采用正式期刊书目，但定理编号与具体比较须明确来自已读的 arXiv v1；本次未核 VOR 与 v1 正文逐字或逐定理一致性。

## 3. MRVB：正式题名与 arXiv 题名确有差异

| 字段 | 核准值 |
|---|---|
| 拟 key | `MorenoRiosecoVanDenBosch2022` |
| Authors | Matías Moreno; Paola Rioseco; Hanne Van Den Bosch |
| 正式 Title | Mixing in anharmonic potential well |
| arXiv Title | Mixing in an anharmonic potential well |
| Year / venue | 2022; Journal of Mathematical Physics |
| Volume / issue / article | 63 / 7 / 071502；071502 是文章号，不是起止页 |
| Published / received / accepted | 2022-07-01 / 2022-03-10 / 2022-06-11 |
| DOI | `10.1063/5.0091016` |
| 实际科学版本 | `arXiv:2201.07019v2`，2022-03-10；v1 为 2022-01-18 |

本次 actual 核准：[arXiv v2 元数据](https://arxiv.org/abs/2201.07019v2) 行 8–28 给全名、题名、版本和关联 DOI。
普通 DOI 首次 open 返回工具级 “not safe to open (non-retryable error)”，不是已取得正文或明确的出版方 403；保留该失败。
随后经确切题名／DOI 搜索返回的 [AIP 官方 DOI 结果](https://doi.org/10.1063%2F5.0091016) 正常重定向到 [AIP 官方 metadata 页面](https://aipp.silverchair-cdn.com/article-minimal/2843589)，实际核读行 0–136：正式题名无 “an”，作者缩写、卷／文章号、日期及摘要均在可见页面。未请求付费正文。
第 7 期另由本次返回的 [UCL 机构库条目](https://discovery.ucl.ac.uk/id/eprint/10187704/) 元数据核准；该条目同时出现 Accepted Version 与 VOR 描述，未据此声称下载件版本一致，亦未下载其 PDF。其余技术判断不依赖机构库摘要。
此前正文核读身份：两正式席各自读取 [v2 PDF](https://arxiv.org/pdf/2201.07019v2) 第 1–4 页，共 4/12 页，含 Th1.1–1.3 完整声明；这些定理的证明不在该共同读取范围。
用途：相关工作比较非退化频率、有限退化频率与光滑非驻相情形的相混合结论；正式题名用于期刊书目，arXiv 题名保留用于版本定位。
不支持：Th1.2 的既有低正则率为 $t^{-1/3}$，不能误引成现成的 sharp $t^{-1/2}$；也不能把光滑作用域结果当成已覆盖本稿原空间的 saddle／acnode／换圆奇偶。
本次未比较正式版与 arXiv v2 的完整内容；后续具体定理定位应继续标明 v2，不能仅因关联 DOI 就宣称版本正文相同。

## 4. HRSS：保留已核固定预印本身份

| 字段 | 核准值 |
|---|---|
| 拟 key | `HadzicReinSchreckerStraub2024` |
| Authors | Mahir Hadžić; Gerhard Rein; Matthew Schrecker; Christopher Straub |
| Title | Quantitative phase mixing for Hamiltonians with trapping |
| Year / venue | 2024; arXiv preprint；未在本次核准期刊出版状态 |
| Volume / journal pages | 不适用／不填；arXiv comments 标 60 pages，不转换为期刊页码 |
| arXiv version | `2405.17153v2`，2024-06-04；v1 为 2024-05-27 |
| DOI | `10.48550/arXiv.2405.17153`，仅 arXiv-issued DOI，不是期刊 DOI |

本次 actual 核准：[arXiv v2 页面](https://arxiv.org/abs/2405.17153v2) 行 8–27 的题名、全名、版本、页数说明和 arXiv DOI。没有额外开展出版状态检索。
此前正文核读身份：两正式席各自读取 [v2 PDF](https://arxiv.org/pdf/2405.17153v2) 第 1–8、11–17 页，共 15/60 页，含主定理入口与假设及 Lemma2.1 完整证明；不是全部主定理证明核验。
用途：引言／相关工作与中心分析处说明 trapping、椭圆停滞点和原观测 Fourier 系数的先行处理；承认既有相混合方法。
不支持：其单调周期和宏观量／核结论不能直接替代本稿全参数 qPI 未平均双相关定理；未核出版状态不能表述成“尚未发表”或据此增加新意。

## 5. Liu–Zhang–Li：只采用实际可核的 arXiv v1 引用身份

| 字段 | 核准值 |
|---|---|
| 拟 key | `LiuZhangLi2025` |
| Authors | Xinyu Liu; Xinze Zhang; Yong Li |
| Title | The LLN and CLT for the statistical ensembles of discrete integrable Hamiltonian systems |
| Year / venue | 2025; arXiv preprint，引用固定 v1 |
| Volume / pages | 本引用不填期刊卷页；本次未核 PDF 总页数 |
| arXiv version | `2509.20690v1`，2025-09-25 |
| DOI | `10.48550/arXiv.2509.20690`，仅 arXiv-issued DOI；不填未经本次核准的正式期刊 DOI／卷页 |

本次 actual 核准：[arXiv v1 页面](https://arxiv.org/abs/2509.20690v1) 行 8–25，采用明确 Authors 三人栏；页面自动 “and 1 other authors” 文案不覆盖该署名栏。
此前正文核读身份：两正式席各自读取 [v1 HTML](https://arxiv.org/html/2509.20690v1) 的原确定性对象、全非共振假设、Th3.1 声明及完整证明至结束；共同清单的旧工具行 27–153 仅作辅助定位。后文随机 CLT 不消费。
用途：相关工作中区分离散可积系统的 Cesàro ensemble 极限定理与本稿未经时间平均的相关渐近。
不支持：不能把 Cesàro LLN 写成 raw correlation 衰减，也不能替原文弱化逐作用全非共振量词；未读随机 CLT 不能用于确定性结论。
旧 ScienceDirect 正式入口 `S100757042500869X` 的 403 原样保留，本次未重试、未借镜像绕取；没有把 arXiv 声明伪称为已核 VOR 同名定理或证明。

## 6. Liu Markov：正式期刊、文章号与两种日期分开

| 字段 | 核准值 |
|---|---|
| 拟 key | `Liu2026Markov` |
| Author | Xinyu Liu |
| Title | Weak Convergence to Equilibrium for Statistical Ensembles in Discrete Integrable Hamiltonian Systems with Markov Perturbations |
| Year / venue | 2026; Journal of Nonlinear Mathematical Physics |
| Volume / article | 33 / 77；77 是文章号，不是页码范围 |
| Published / VOR | 2026-05-18 / 2026-07-10 |
| Received / accepted | 2026-03-21 / 2026-04-23 |
| DOI / arXiv | `10.1007/s44198-026-00424-7` / 本次未核 arXiv 身份，不填 |

本次 actual 核准：[Springer 官方页面](https://link.springer.com/article/10.1007/s44198-026-00424-7) 行 11–41 的题名、作者、期刊、卷／文章号及摘要，和 895–909 的正式引用／日期／DOI。没有重读中间证明。
此前正文核读身份：两正式席各自读取同一官方页的摘要、完整 Conclusions 及发表／VOR 日期；并未核全部随机证明。本次不把该既有 Conclusion 阅读转算为本人的新读取。
用途：相关工作中区分 Markov 扰动及非零 twisted-mode 衰减假设产生的弱收敛，与本稿原确定性 qPI 的相位抵消。
不支持：不能去掉随机扰动仍保留其指数模阻尼结论，也不能用其摘要替代本稿 saddle／驻圆／acnode 的证明。

## 7. P30：匿名未发表本地接受稿，不虚构作者或出版身份

| 字段 | 核准值 |
|---|---|
| 拟 key | `QPI30Local2026` |
| Author 字段 | 源文件署名 `Anonymous`，源配置为 `pdfauthor={}`；未另检 PDF metadata，真实作者未提供，不推断身份 |
| Title | Vertical critical ideals and cyclotomic first jets of q-Painlevé I |
| Year / venue | 2026；unpublished local manuscript，无期刊／出版社身份 |
| Version / local status | `paper/v4/`；2026-09-09，`COMPLETE_LOCAL_FINAL_REVIEW_PASS`，仅本地接受 |
| Volume / pages | 无期刊卷页；接受记录的 39 正文＋2 参考文献页是本地 PDF 状态，不充当期刊页码 |
| DOI / arXiv | 无已提供或已核记录；不生成 |

本次 actual 核准：[V4 main.tex](../../30-qpi-vertical-critical-ideals/paper/v4/main.tex) 第 1–45 行，重点为第 11–22 行题名／作者／空日期；[LOCAL_ACCEPTANCE_20260909.md](../../30-qpi-vertical-critical-ideals/notes/LOCAL_ACCEPTANCE_20260909.md) 108 行 FULL，核准 accepted source、日期、版本、状态和仅本地效力。未打开 P30 PDF、未重扫构建树或重新验证其已接受阶段。
定向身份：`main.tex` 整件 62 行／2533 bytes，SHA-256 `1d1a47776586fc72aa7041eaaf1098615b4bb1adc373f62546cbf71d6b6679b4`；本次正文只读第 1–45 行。
接受记录整件 108 行／8513 bytes，SHA-256 `cfb2f9e034716545fd22d9e7024d7b9b62d89350c3eecc97852870b17f094a52`。
此前正文核读身份：正式 R1/R2 各自 FULL 读 P30 V4 引言 300 行，PARTIAL 读 surface 第 1–270、388–437 行与 spectral 第 1–270 行，详见 [共同清单]；不是本核准者本次完整读 V4。
用途：原八中心曲面、四 terminal、完整有限纤维及必要模型接口的已接受来源；在模型节写清所引命题及未发表本地稿身份。准确消费的正文段落由作者大纲／稿件落实。
不支持：本地接受不是同行评审出版、不能虚构 DOI、作者或投稿状态；P30 的算术临界理想／jets 结论不替代 P31 的实 twist／相关证明。其 22–40 页例外也不迁移至 P31。

## 8. 下一阶段的引用消费与冻结边界

建议的功能分组而非固定章节号：FHR／MRVB／HRSS 用于相混合先行工作及已知方法扣除；两项 Liu 来源用于离散确定性平均与随机扰动的对象边界；P30 用于必要原模型接口。
六项均只有拟 key。必须在实际章节出现相应消费并核对版本定位后，才冻结最终 BibTeX；不以本清单强制每节配额，不添加未消费或未读经典书目。
FHR 与 MRVB 可以优先用核准的正式书目，同时在具体比较处保留实际已读 arXiv 版本；本次没有证明两个版本内容等同。
HRSS 和 Liu–Zhang–Li 可按上述固定预印本身份引用，不把未核出版字段伪填完整，也不为冻结书目自行恢复已拒绝入口。
本稿全局证明 G 已有自足标量驻相论证；不因“标准方法”标签而强加未读经典定理作黑箱或堆引用。
本件不是新的来源充分性门、不改变正式双席准入或已接受数学；其影响仅是准确引文身份、阅读边界与后续消费记录。
全部交付限本地；无投稿、上传、托管、push、对外发信、数值实验、构建或再委派。

[正式准入处置]: ../../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_CANDIDATE_DISPOSITION_V1_20260913.md
[共同清单]: ../../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_REVIEW_INPUT_MANIFEST_V1_20260913.md
