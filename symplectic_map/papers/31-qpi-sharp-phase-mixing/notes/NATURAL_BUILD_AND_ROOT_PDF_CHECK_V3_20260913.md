# Paper31：V3 同源双根与主控全页实际核验

日期：2026-09-13 UTC。主控：`/root`。
状态：`DETERMINISTIC_BUILD_PASS / BODY_WINDOW_PASS / ROOT_ALL_PAGES_PASS / INDEPENDENT_PDF_REVIEW_PENDING`。
这是制作与作者全页读回记录，不替代 fresh actual 内容验收或另席终局完整性；Batch07仍4/5。

## 1. 完整冻结源与执行

完整源为 `paper/v3/`，12件2454行／108359 bytes；[SHA清单](SOURCE_V3_20260913.sha256)
SHA `4e1a98c1e273b8d2e138b91952a1c1e1ce2e00ac6006521714ddaf0dbd8beae8`。
主控完整源阅读由 [V2源处置](COMPLETE_SOURCE_DISPOSITION_V2_20260913.md) 与 V2→V3 两行真实制作差分接续；
后者已逐行实际读回，十件未变逐字节核同；全部数学、引用、字号/边距/行距及原22–30页锁不变。

首次 r0 的后处理失败及三份依赖记录的实际定位见 [诊断与恢复前置协议](R0_DIAGNOSIS_AND_V3_RECOVERY_PROTOCOL_20260913.md)，
61行／4707 bytes，SHA `32b8f727e4284af0b3427380f3c74daad95111f212bfc097661e860094b469b9`，主控 FULL 读回。
r0源、PDF、日志、诊断复制件、格式目录原件及脚本V1均保留；r1未执行。
按该前置协议，实际分别从 absent 新根 r2、r3复制完整V3，运行固定脚本V2；每根均pdfLaTeX→BibTeX→pdfLaTeX→pdfLaTeX。
两次脚本退出0，无额外收敛遍次或隐藏重跑。全部逐遍命令、退出码、stdout/stderr、日志及辅助产物快照在各根logs。
正确格式名与固定TEXFORMATS仍消费原冻结格式，没有生成/安装/替换格式或改全局配置。

## 2. 实测成品与确定性

| 实际对象 | 结果 |
|---|---|
| [r2 PDF](../build/natural-20260913-r2/work/main.pdf) | 31页，528155 bytes，SHA `fc5d4419b6ddd2d9faf9ebb08b5319a3e249432c332944eb506f645857257640` |
| [r3 PDF](../build/natural-20260913-r3/work/main.pdf) | 31页，528155 bytes，同一SHA |
| PDF字节比较 | `cmp`退出0；不是视觉近似或只比提取文字 |
| 完整源清单 | 两根 source.sha256相同；复制前、复制后及构建结束逐件hash校核通过，原V3未编辑 |
| recorder | 两根work/main.fls真实存在，r2为842行；每次TeX的当时.fls均在对应logs保留 |
| 实际绝对依赖 | 两根各144个去重实际路径，SHA清单字节相同，清单SHA `b463baff29948284177c09370c2e0d93aade3745f487d57c95b2a7578b69978b` |
| 依赖当前核验 | root实际对r2清单执行严格hash核验：checked144，failures0；r3同一清单不重复扫描 |
| BibTeX额外输入 | 实际main.blg为plainnat.bst与references.bib，7条使用；二者身份与冻结inventory/源一致，warning计数0 |

依赖清单位于两根 `logs/absolute-inputs.sha256`；记录了实际TeX传递包、配置、字体/映射及格式，
并不将它冒称为操作系统全部动态库清单。BibTeX的bst不由TeX recorder涵盖，已另核为
SHA `21eefa76f1c967f5074776fcef096c0f8f2b9e42347e84b62e1dbb121dcae486`；bib为固定V3中的同一完整条目集。

## 3. 页窗、版式、日志与字体

r2完成后，root先亲核LastBodyPage=30、结论/参考文献逐页文本及第30/31实际页图，正文窗通过后才执行r3。
实际正文为第1–30页，参考文献第31页，均无附录；不是按字数、表格预算或formal容量票估计。
最后结论自然落第30页；没有人为正文分页、移证、缩水字体/边距或填页。原硬窗保持22–30。

pdfinfo实际letter612×792 pt、PDF1.5、Author空、无CreationDate/ModDate；页面标题作者块为Anonymous。
main及实际geometry记录为11pt、单栏、四边1inch；没有制作时换模板。
两根最终main.log均无Warning/Error/Overfull/Underfull/Missing，也无未定义引用、缺字或不收敛。
中间第一遍的未定义引用属于正常四遍收敛过程并完整保留，未被抹去。
root对最终layout text定向查 `??`、`[?]`、`[VERIFY]`、TODO无命中；实际文献编号1–7与正文引用一致。
pdffonts实际列26项Type1字体，全部emb/sub/uni为yes；root亲读完整字体表。

## 4. 主控全部31页实际阅读

root从实际r2 PDF使用pdftoppm渲染，亲自查看每一页，而非只读文本或缩略拼图。
第1–29页用 `r2/inspection-root/page-01.png` 至29的130dpi全页图；第30/31页先用同PDF100dpi边界图实际读完。
r2/inspection-root另存完整31件130dpi图供独立审查；原PDF本身未改。r3字节相同，不另冒称重复读了一套不同PDF。

| 实际页段 | 核验重点 |
|---|---|
| 1–2 | 题名/匿名/摘要、三率结果表、有限与随机先例的准确比较、七项引用责任；无裁切 |
| 3–8 | 全局lift新增局部式、四terminal表、完整曲面/measure/Pi、全参数原C20和精确A/B/D主定理，公式与表宽正常 |
| 9–16 | 完整PF moving-endpoint还原、锚点/中心jets/两无穷常数/严格五行分类，跨页自然，表3包含额外persistent说明 |
| 16–22 | 原双侧时间、范数、全圆混合符号、全部k与真实边界；19页的局部溢出已消除，没有裁字或公式重叠 |
| 22–26 | 正向signed-radius角、原jet与余项、两类端点完整证明；25页标题数学显示保持，书签有准确纯文本 |
| 26–29 | 全局交换、驻相、单次完整分割、实际奇偶和原实/复sharpness；长公式和共轭/符号均清楚 |
| 30–31 | 结论非空、与正文连续；参考文献独立一页，7项真实身份与预印本版本说明，链接折行可读 |

主控本次全页 `required fixes: []`。没有新增数学/范围问题；旧数学与正式准入不重新抽票。
fresh非作者正在对真实V3差分与全部31页作actual验收；之后须另席独立终局完整性，均不由本报告预授PASS。
仅本地制作，无对外提交、上传、托管、push、发信、付费资源或数值/CAS/参数阶数扫描。
