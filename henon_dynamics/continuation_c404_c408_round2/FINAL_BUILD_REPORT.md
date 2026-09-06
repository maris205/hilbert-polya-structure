# C404–C406 最终构建与全部 33 页 QA

日期：2026-09-06。三篇完整正文均已接受非作者内部全文审查，未留下
必须修改的数学、引用或范围问题。最终输入不需改动，三份终稿均与
经审查的初稿 PDF 同字节。本报告不将初稿抽页预览计作最终全页检查。

## 实际构建及输入

每稿分别使用两个由 `mktemp -d` 创建的新空目录，仅复制 `main.tex`、
`math_commands.tex`、`references.bib` 和八个 `sections/*.tex`，合计
11 个 TeX/Bib 输入。不复制辅助文件、旧 PDF 或第一次构建的缓存。
两个目录分别执行以下命令，外层使用 `set -euo pipefail`：

```sh
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex \
  > compile.stdout.log 2>&1
```

随后实际执行 `cmp a/main.pdf b/main.pdf`，并将 a 与包中经审查的
`paper/main.pdf` 比较。一次 latexmk 作业内的多个 LaTeX/BibTeX pass
不算多次独立构建。

| 稿件 | 新目录 a | 新目录 b | 构建 a / b / 两 PDF 比较 / 初稿比较 | 页数 / bytes |
|---|---|---|---|---|
| C404 | `/tmp/c404-final-a.kHCAi6` | `/tmp/c404-final-b.2KkW2Z` | 0 / 0 / 0 / 0 | 10 / 373654 |
| C405 | `/tmp/c405-final-a.c0yZ1m` | `/tmp/c405-final-b.2tgmvr` | 0 / 0 / 0 / 0 | 10 / 355317 |
| C406 | `/tmp/c406-final-a.MMAHZn` | `/tmp/c406-final-b.G5iaDp` | 0 / 0 / 0 / 0 | 13 / 403808 |

| 最终 PDF | SHA256 |
|---|---|
| [C404](henon_resonance/paper/main.pdf) | `99c58e5805bb4e5b70e5f86505dc60dd8f79df76ea0011ac901127456e10a3cc` |
| [C405](arithmetic_forms/paper/main.pdf) | `9b6801db5237ef523fded18797ec7508a06762bd79fd1c32f0074ddbfa9290c3` |
| [C406](critical_delta/paper/main.pdf) | `43f04734234a9e21e41ad0eaff5e199c642935228475c4207e7a4cee14bec1a9` |

各稿最终 11 个输入另由 `paper/final_build/SOURCE_INPUTS.sha256` 绑定，
路径相对于该稿 `paper/`。初稿清单、失败尝试和原收据保留原字节；其中
“等待终构建/非作者正文审查”等文字仅描述初编译时点，已完成门槛以
本报告及三份正文审查记录为准。

实际工具为 Latexmk 4.76、pdfTeX 1.40.22 / TeX Live 2022/dev/Debian、
BibTeX 0.99d、Poppler 22.02.0；未安装或更换工具、字体。主文件均启用
可用的 `pdfinfoomitdate=1`、空 `pdftrailerid`、`pdfsuppressptexinfo=15`。
最终 PDF 均为 A4、PDF 1.5，无 CreationDate/ModDate、加密、JavaScript
或表单。C405 的 PDF 元数据标题/作者字段为空，但印刷页有标题与匿名
作者栏；这不作为未核验的作者身份声明。

## 原始输出与检查范围

每稿 `paper/final_build/a/` 和 `b/` 各保留原始 `compile.stdout.log`、
`main.log`、`main.blg`、`main.bbl`、`main.aux`、`main.fls`；顶层另存
`main.txt`、`pdfinfo.txt`、`pdffonts.txt` 和 `RUNTIME_INPUTS.sha256`。
没有删掉 stdout 中前期 pass 的临时未解析引用提示。最终 TeX/BibTeX
日志按以下大小写敏感模式检查，所有四份最终日志均无命中：

```text
Warning|Overfull|Underfull|undefined|Error|Fatal|Missing character
```

C406 首次诊断误用了不区分大小写模式，命中了 `warning$ -- 0`、
`file:line:error style messages enabled` 和包说明文字；检查命令退出 1。
核对这些均为非诊断元数据后，使用上述模式检查通过，未改正文或日志。
C405 首次复制收据时，临时目录没有保存 `pdfinfo.txt`，复制中途退出 1；
已从同一最终 PDF 直接生成 metadata/font 收据补齐，不涉及编译失败。

| 稿件 | 字体记录 | 文本检查 | 最终目视 |
|---|---|---|---|
| C404 | 24，全部嵌入/子集/Unicode，Type 1 | 无 `??`、`[?]`、`[VERIFY]` | 第 1–10 页，全部实际查看 |
| C405 | 19，全部嵌入/子集/Unicode，Type 1 | 同上 | 第 1–10 页，全部实际查看 |
| C406 | 24，全部嵌入/子集/Unicode，Type 1 | 同上，亦无 TODO/FIXME | 第 1–13 页，全部实际查看 |

使用 `pdftotext -layout` 抽取全文，用 `pdftoppm -r 100 -png` 渲染
最终 a 目录 PDF，协调者逐页打开全部 33 张图。标题、表格、公式
上下标、矩阵、页边界、引文和书目均可读，无裁切、重叠、缺字或未解析
引用。重点包括 C404 的差分主项及真实 F4 示例，C405 第 9 页的二分
表格及失败控制，第 8 页的最大定义域变分论证，C406 第 8 页累计误差
与第 9–12 页积分/端点/定义域比较。渲染图留在临时目录，不计为论文
或发布载荷；C406 原有两张初稿预览图仍保留在原初稿记录中。

`.fls` 所列不同绝对 INPUT 文件逐项计算 SHA256：C404 为 145 项、
C405 为 142 项、C406 为 147 项。它们绑定实际系统输入，不宣称封闭
重建全部操作系统。本地源码由 11 项最终输入清单和批次 manifest 绑定。

## 审查与科学证据边界

[C404 正文审查](reviews/C404_MANUSCRIPT_REVIEW.md)、
[C405 正文审查](reviews/C405_MANUSCRIPT_REVIEW.md)、
[C406 正文审查](reviews/C406_MANUSCRIPT_REVIEW.md) 均针对实际全文和
实际引用，不是对作者摘要的打分。协调者亦读完全部三稿源码、宏、
书目、引用审计和初编译收据。C405/C406 的协调者检查不冒充其本人
上游证明的独立审查；各自另有非作者审查记录。

本轮没有因未变正文而重跑数学代码，没有新增发布程序、外部模型
评审或人为实验配额。字节一致及排版通过不等于全球新颖性、人类
同行评审、期刊录用或目标算术通过。C407/C408 不在完成计数内。
