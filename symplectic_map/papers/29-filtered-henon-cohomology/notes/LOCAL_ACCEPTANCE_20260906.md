# Paper29 本地接受记录

日期：2026-09-06。状态：**COMPLETE_LOCAL_FINAL_REVIEW_PASS**。
route_applicability: NOT_APPLICABLE。效力仅限本地匿名交付。

论文：*Filtered polynomial cohomology and finite periodic tests for
symplectic Hénon maps*。本次获准的一次自然成稿验证已完成，实际正文及
内容、构建、独立 PDF 审查和终局完整性均通过。Paper29 现计入 Batch07，
本地已接受为 Papers27–29，共 **3/5**；Paper30、31 及跨论文统一审查未完成。

## 接受的明确产物

- [接受的匿名 PDF](../build/natural-20260906-r0/work/main.pdf)：438693 字节，
  SHA256 `774865fa38e7d6f053daf57a48a03da3eb52edf940694f1fa6c116287bd966e0`。
- [接受的源入口](../paper-successor-20260906-transcription-v1/main.tex)：
  完整目录为 `paper-successor-20260906-transcription-v1/`，共十二个源文件。
- [源身份清单](SOURCE_BUILD_MANIFEST_20260906.sha256)：SHA256
  `958dd5be31db838485feff5512ac675960ce7caa296f02c1f05b82b6b87e01ee`。
- [第二新根 PDF](../build/natural-20260906-r1/work/main.pdf)：相同大小、
  相同 SHA256，实际 `cmp` 退出 0。

正文为物理页 1–26，参考文献仅物理页 27；没有附录或致谢。第 26 页有
三个势函数例子的比较、结语及明确未证边界，不是空白或标签页。该实测
26 页满足原有 22–30 页锁，不能把 27 页总页数当作正文页数。

## 实际验证闭环

| 验收项 | 真实结果与证据 |
| --- | --- |
| 科学与范围 | [科学输入锁](SOURCE_SCOPE_LOCK_20260906.md)绑定两份证明、两份独立数学检查及已核引用；C1–C4 无未解决的定理级缺口。 |
| 新计划 | 八节大纲的独立检查 PASS，见[计划接收](PLAN_ACCEPTANCE_20260906.md)。共同基础只写一次，不以旧停止候选补篇幅。 |
| 完整源与转写 | [完整源审查](SOURCE_TRANSCRIPTION_INDEPENDENT_REVIEW_20260906.md)只有摘要 D≥1 限定一项 MINOR；[独立修复接收](SOURCE_TRANSCRIPTION_FIX_RECEIPT_20260906.md)已关闭。 |
| 实际首次构建 | r0 的 pdfLaTeX、BibTeX、pdfLaTeX、pdfLaTeX 四阶段均 exit 0，首次完整正确产物即为 26＋1 页。 |
| 同环境复现 | 首次页数门通过后才运行 r1；四阶段均 exit 0，同源、双根 PDF 逐字节相同。见[实际构建结果](NATURAL_BUILD_RESULT_20260906.md)。 |
| 实际完整 PDF | 主控和独立审查员分别看完全部 27 张单页；独立人另读全十二文件及完整 PDF 文本，内容、公式、匿名、归属、正文实质性均 PASS。 |
| 最终完整性 | 独立终审实际核验四套源清单、源差异、两根日志/输入、PDF 身份、字体与边界；无未闭合的验收义务。 |

[实际 PDF 独立报告](ACTUAL_PDF_INDEPENDENT_REVIEW_20260906.md)为 197 行，
SHA256 `58ffb3387012441260413262035b8b5be183ab9896842b77223f4a2694e5a457`；
[最终独立完整性报告](FINAL_INTEGRITY_REVIEW_20260906.md)为 281 行，
SHA256 `293299c0022ea8cd50138ccb8ea50c91849fc9ced5b123d86bfeba5c3d01471b`。
主控已全文读取并核对两份报告身份；两轮均 CRITICAL 0、MAJOR 0、MINOR 0。
全部二十个字体嵌入，最终 TeX/BibTeX 日志无未定义引用、版面框警告或错误。
早期多遍引用解析提示保留，未冒称每个中间 PDF 都是完整接受产物。

## 版本、科学及权限边界

原 `paper/`、原清单、全部原证明/评审/处置均保留。唯一源修复发生在
首次编译之前：摘要补充正文原定理已有的 D≥1 条件，其余十一文件不变。
首次实测后没有扩写正文、增加结果、重复证明或改变字号、页边距及间距。
完整[质量审查与修复记录](PAPER_IMPROVEMENT_LOG_20260906.md)另行保留。

数学结论限于锁定特征零 Hénon 系统的普通次数滤过、保次数余边界原函数、
精确 Hilbert 计数、完整周期概形检测和指定保参数辛扩张的有理固定域。
概形零不等于仅几何点取值零；四次代数长度上界不等于最优计算复杂度。
结尾公开的未证几何点边界不属于本次已经证明的主张。

[范围修订](SCOPE_AMENDMENT_20260906.md)只授权此次自然实测路径。
原 R2 容量 FAIL、原候选合取 FAIL 和所有旧停止结果不追溯改写，也不把
此例外自动推广给下一篇。此前冻结接收文档中的 pending 是当时阶段快照，
其后继义务已由本记录绑定的实际证据闭合，不修改旧快照来制造通过。

所述确定性限于当前本地同环境双新根，不承诺跨平台字节相同或 hermetic
依赖封装。审查使用实际可用的独立代理 fallback，未冒称 GPT-5.4 MCP 调用。
没有投稿、上传、托管、push、外部发信或付费资源操作；纯数学论文不赋予
Route A/B 层级 PASS，也没有虚构实验。下一项按批次串行约定为 Paper30。
