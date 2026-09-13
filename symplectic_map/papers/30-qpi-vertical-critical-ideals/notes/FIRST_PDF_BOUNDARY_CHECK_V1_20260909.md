# Paper30 first successful full natural PDF: independent boundary check V1

日期：2026-09-09。检查者：独立非编译代理 `p30_first_pdf_boundary_check_v1`。
结论：`PAGE_WINDOW_FAIL`；这是页数／构建边界记录，不是整篇科学或 PDF 接受记录。

## 1. 范围与产物绑定

已全文阅读 [PUBLICATION_LOCK](PUBLICATION_LOCK_20260909.md)，未修改其中任何要求。
锁 SHA-256：`e07f4bcb20f8aa445b41a5ceccd3d680036700fb63f26b9fc1379870c94573fa`。
被检 PDF：[r2/work/main.pdf](../build/natural-20260909-r2/work/main.pdf)。
PDF SHA-256：`06a4e848e177b6b69a6593b7894286f55babb1ba09d64b29a1263d926c075d91`。
文件大小：546638 bytes；PDF 1.5；612 × 792 pt，letter。
输入还包括同根 `work/main.aux`、`work/main.log`、`work/main.blg`，
以及根目录 `pdfinfo.txt`、`pdffonts.txt`、`main.layout.txt`。
未读源码或旧论文集；未编译、改源、覆盖构建根、重评分或进行外部操作。
首次成功完整自然构建的身份由主控提供；本检查独立确认该 r2 产物的实际边界。

## 2. 物理页数与正文／文献分界

重新运行 `pdfinfo` 得到物理总页数 **41**，与已保存的 `pdfinfo.txt` 一致。
`main.aux` 同时记录 `LastBodyPage` 为 **39**、`\@abspage@last` 为 **41**。
`main.layout.txt` 按 form feed 划分得到 41 个非空物理页面文本块。
对全部 41 个文本块检查末尾印刷页码，均与物理页序号一致；无错位或重置。
标题、摘要与引言从物理第 1 页开始，因而正文计数没有封面扣除。
重新用 `pdftotext -f 39 -l 41 -layout` 提取 PDF，边界内容与保存文本一致。
第 39 页含 Corollary 8.6、其证明及范围限制的结尾段，仍是正文。
正文最后一句止于原 eight-blowup model 与 complete terminal charts 的说明。
第 40 页以独立的 **References** 标题起始，列文献 [1]–[13]。
第 41 页续列文献 [14]–[17]，此后 PDF 结束；参考文献合计 **2 页**。
故实测为 **39 页正文 + 2 页参考文献 = 41 页总 PDF**。

## 3. 边界页实际看图

用 `pdftoppm -f 39 -l 41 -scale-to 1300 -png` 生成三个独立检查图。
输出只写入新建的 `notes/first-pdf-boundary-check-v1-20260909.m8Ne0l/`。
已逐张实际查看 [第 39 页](first-pdf-boundary-check-v1-20260909.m8Ne0l/boundary-39.png)、[第 40 页](first-pdf-boundary-check-v1-20260909.m8Ne0l/boundary-40.png)、[第 41 页](first-pdf-boundary-check-v1-20260909.m8Ne0l/boundary-41.png)。
图像确认 39 页正文结束与 40 页 References 另页起始，中间没有空白页。
本次仅作上述三页的边界视觉确认，不扩张为全部 41 页的公式／排版阅读通过。

## 4. 最终日志与字体证据

最终 `main.log` 记载 `Output written on main.pdf (41 pages, 546638 bytes)`。
检索未发现 undefined references/citations、Missing character、LaTeX Font Warning 或终止错误。
最终日志仍有 **2 个 Overfull hbox**，没有 Underfull 告警；不能称为零告警构建。
第一处：9.96825 pt，日志指向 `sections/03-spectral-jacobian.tex` 的 313–321 行。
第二处：6.8397 pt，日志指向 `sections/06-first-layer.tex` 的 46–51 行。
两处仅由日志定位；其实际溢出检查／最小修订由主控另行处理，本报告不宣称已修复。
`main.blg` 记录使用 17 个条目，`warning$ -- 0`，未见缺文献或 BibTeX 错误。
重新运行 `pdffonts` 与保存清单一致：23 个字体资源行全部 `emb=yes`，均为 Type 1。
字体嵌入及最终引用收敛是构建证据，不等于所有页面可读性或科学证明正确性。

## 5. 锁定裁决与保留边界

合同要求正文 **22–30 页**、参考文献另起页另计；本次 **39 > 30**，超上限 **9 页**。
参考文献另页条件通过，正文窗口条件失败；总页数 41 不能用来替代正文页数 39。
不得因本次实测值把上限自动改为 39，不删科学结论／必要证明、不缩版或移证明入附录。
`PAGE_WINDOW_FAIL` 不推翻已有科学／静态检查，也不新增或重做其通过判定。
整篇实际 PDF 验收、同源双根字节确定性、fresh 完整审查与终局接受均不由本报告授予。
按锁，正文窗口未通过，不启动其以通过为前提的第二根确定性／后续接受阶段。
保留冻结 V1/V2/V3、r0 失败现场和 r2 成功产物；本检查未触碰这些历史对象。
可继续已授权的错误定位与证据保存；修改锁定科学范围或页数合同须用户明确决定。
终态：该 SHA 绑定的首次成功完整自然 PDF 已确认 **PAGE_WINDOW_FAIL**，不计为论文完成。
