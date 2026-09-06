# C399/C400：既有正文与验证收据的原字节复用

日期：2026-09-05。此次动作是把已完成的两个研究稿登记到本批编号，
不是生成新数学内容、再做一次盲审或重复执行数值/构建。两稿均在提交
`1667dfc0c24e10a8a3627e80f93e301538d18012` 中已完整保存。

| 本批编号 | 实际交付 PDF | 页数 | PDF SHA-256 |
|---|---|---|---|
| C399 | [Boole](../research_c399_c403/boole/paper/main.pdf) | 9 | `5b4a42a5b16a06c496f5326a6cdd16abe550357a36f0b5b059c637f62e105f0a` |
| C400 | [harmonic δ-comb](../research_c399_c403/delta_comb/paper/main.pdf) | 14 | `ed580df6ca898434951fbad6aa0c91130af77e58537e5900fc634f4eaf4279b5` |

编号属于本轮 [冻结计划](BATCH_PLAN.md) 的外部登记，PDF 内“未编号研究稿”
文字是前轮冻结时的状态说明，保留而不回写历史。两份文件各自的完整
数学内容没有改变；未把这一登记称为两次新写作，也不把前轮仅两稿的
快照追认成当时已完成五篇。

## 已验收而未重复的检查

- C399：独立完整证明审查、全文/全部引文上下文审查、实际小修的定点
  hash 复核；两个新空目录确定性构建、PDF 字节相同、零终日志警告、
  21 个字体全嵌入/子集/Unicode，正文文本检查及 1–9 页逐页目视。
  真实命令、输入和日志哈希见 [原构建收据](../research_c399_c403/boole/BUILD_REPORT.md)。
- C400：独立完整证明/渐近复核、全文/5 条来源及 9 个引文上下文核对、
  实际摘要/元数据小修定点复核；两个新空目录确定性构建、同字节 PDF、
  零终日志警告、21 个字体全嵌入/子集/Unicode、文本检查及 1–14 页目视。
  见 [原构建收据](../research_c399_c403/delta_comb/BUILD_REPORT.md)。
- 既有精确/数值 sanity 检查仍仅是有限支持，不证明无限量词；没有
  为编号、Markdown 链接或本轮 Route 评估重跑这些程序。

这些是同一任务延续中真正执行并保留的收据，不声称本次又执行了两次
构建、又目视了全部 23 页，或又做了一轮完整审查。原始日志不作格式化。

## 本轮实际重核

从 `henon_dynamics/research_c399_c403/` 运行
`sha256sum -c MANIFEST.sha256`，退出状态 0，全部 58 个登记项通过：
57 个载荷及原 ledger 均未变，包括两稿的完整 TeX/Bib、PDF、审查和日志。
另实际计算旧 manifest 自身哈希和两个 PDF/构建收据哈希：

| 文件 | SHA-256 |
|---|---|
| 原 `MANIFEST.sha256` | `e1b707ed43cd04fc3f9daf142618f1364b42c51e85ac1cba4860b20520fe0750` |
| 原 `PAYLOAD_FILES.txt` | `4ad989f66a92b73ae70a7dae99193936b40a94acd5a5a4612c24fbc1409786d8` |
| Boole `BUILD_REPORT.md` | `dd94556c1b7cf5c8aaebcc486743f914883dabb782904a160705fc2e4c82bc04` |
| δ 梳 `BUILD_REPORT.md` | `7ece372f16a73867c6cdee972bac4cd6670db9f6cd2fad1e4df481aa9282f666` |

工具实际重新查询为 Latexmk 4.76、pdfTeX 1.40.22 / TeX Live 2022/dev/Debian、
Poppler 22.02.0，与原构建环境一致；本任务没有安装/更新 TeX、字体或系统包。
本轮查询到的执行文件哈希如下（原收据未登记这些二进制哈希，因此不
声称逐二进制进行了跨时点哈希比较）：

| 执行文件 | 本轮 SHA-256 |
|---|---|
| `/usr/bin/latexmk` | `22e2164fea826ee19ff234503ef807d2728541e10eb3563912169977a650c951` |
| `/usr/bin/pdftex` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `/usr/bin/pdftotext` | `7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d` |
| `/usr/bin/pdffonts` | `257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e` |
| `/usr/bin/pdftoppm` | `f09bac4b4bc5e08ef9d44620fb5a4f1dd61574a8ed9fe49f48575d45e6966165` |

依据本地 batch workflow 的“相关输入与环境未变可复用收据”和“不因
新会话/日期重启已验收工作”，这些检查不重复。任何以后正文变更须
重新进入受影响审查和 PDF 门槛；本轮新写的三稿仍各自做两新目录终构建。

本记录不改变来源所有权、不认证全球新颖性或投稿准备度。五篇完成
与否取决于本批其余三篇和最终封存，而不是单靠旧稿复用。
