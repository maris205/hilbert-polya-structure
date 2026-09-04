# P185--P186 Round2 终端视觉 QA

日期：2026-09-03（UTC）

## 方法与冻结绑定

- 对每篇论文先以 `cmp -s` 核对 live `main.pdf` 与冻结的 `main_round2.pdf`，两篇均为 byte-identical；下表 SHA-256 同时绑定两份文件。
- 仅从 `main_round2.pdf` 使用 `pdftoppm -png -r 220` 生成逐页 PNG。A4 页面均为 1819 x 2573、8-bit RGB。
- 6/6 个页面均以 `view_image` 原始分辨率逐页检查。检查项包括：页面/版心裁切、对象重叠、空白或截断页、公式和表格、字体字形、可见引用标记与参考文献、页眉页脚和页码。
- `pdffonts` 显示两份 PDF 的全部列出字体均已嵌入并子集化；文本哨兵扫描未发现 `??`、`[?]`、`undefined` 或未解析 citation/reference 字样。

## 结果

| 论文 | live/Round2 SHA-256 | 页数 | 逐页结论 | 渲染证据路径 |
|---|---|---:|---|---|
| P185, *Pointwise Clocks and All-Time Fibres for Prefix-Diversity Delay* | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` | 3 | **PASS**。第 1--3 页内容完整、清晰且均在页面边界内；分段公式、乘积公式、引用、声明、参考文献、页眉与页码均正常。第 3 页下部留白为正文及参考文献自然结束，并非空白或截断页。 | `papers/185-prefix-diversity-delay/qa_final/visual/page-1.png` 至 `page-3.png` |
| P186, *Gap Erosion and All-Time Fibres for Rank-Compression Support Dynamics* | `449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48` | 3 | **PASS**。第 1--3 页内容完整、清晰且均在页面边界内；长求和上限、生成函数、二项式公式、引用、声明、参考文献、页眉页脚与页码均正常，无重叠或字形异常。 | `papers/186-rank-compression-support/qa_final/visual/page-1.png` 至 `page-3.png` |

总结果：**PASS（2/2 篇，6/6 页；未发现终端渲染异常）**。未修改任何论文源码或 PDF。
