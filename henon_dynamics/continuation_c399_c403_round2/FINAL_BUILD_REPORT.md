# C401–C403 最终构建与逐页 QA

日期：2026-09-05。三篇新稿均已通过最终双新目录构建和全部 36 页逐页 QA。
C399/C400 不在本次构建范围内，其未变输入及原收据复用见
[REUSE_C399_C400.md](REUSE_C399_C400.md)。没有用初稿抽页检查替代最终全页检查。

## 最终输入及真实修改

- C401：正文独立审查确认主定理一句措辞需要显式沿用非共振条件。
  `sections/1_introduction.tex:51` 的 `More precisely` 改为
  `Under the same nonresonance condition`，未改证明或程序。修正后该文件
  SHA256 为 `b8a7f05bd2fbbfd6c5af28f3845854975d62e7c2ea709aa3093b9897a724af93`。
  非作者已对这一句作定点复核。最终 11 个输入由
  [FINAL_SOURCE_INPUTS.sha256](henon_arithmetic/paper/FINAL_SOURCE_INPUTS.sha256) 绑定。
- C401 原 11 个 TeX/Bib 和原输入清单全部复制到
  `henon_arithmetic/paper/initial_build/source/`；原 PDF 保存为
  `initial_build/initial.pdf`，SHA256 为
  `fcd14059ed2504dae82188c585d8bc2a05f040fc27775251728d72c5408e891a`。
  原初稿收据及原 `SOURCE_INPUTS.sha256` 保留原字节，描述的是这一初稿版本；
  从 `initial_build/source/` 运行原清单校验全部通过。不能用原清单断言
  经过该句修正的当前正文仍完全相同。
- C402：独立正文审查 0 blocking、0 actionable minor，无需修稿。
  [SOURCE_SHA256.txt](nonlinear_return/paper/SOURCE_SHA256.txt) 的全部 11 项
  保持不变并通过核验；两个最终构建也与已冻结初稿 PDF 同字节。
- C403：独立正文审查 0 blocking、0 actionable minor，无需修稿。
  [SOURCE_SHA256SUMS.txt](spectral_regular_variation/paper/SOURCE_SHA256SUMS.txt)
  的全部 12 个输入原样通过。最终 PDF 也与初稿同字节。

## 两次新空目录构建

每个目录均由单独的 `mktemp -d /tmp/cNNN-final-{a,b}.XXXXXX` 实际分配。
仅复制该稿 `main.tex`、`math_commands.tex`、`references.bib`、`sections/*.tex`，
不复制 `.aux/.bbl/.pdf` 或第一次构建的缓存。分别在两个目录内执行：

```sh
env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex \
  > compile.stdout.log 2>&1
```

外层使用 `set -euo pipefail`，两个目录的构建均返回 0 后才执行 `cmp`。
这里的“一次构建”包含 latexmk 所需的 LaTeX/BibTeX 多个内部 pass，
不是把同一目录内的内部 pass 计为两次独立构建。

| 稿件 | 独立目录 a | 独立目录 b | 两构建 / 字节比较 | 页数 / bytes |
|---|---|---|---|---|
| C401 | `/tmp/c401-final-a.sz3MTf` | `/tmp/c401-final-b.LSAQAJ` | 0 / 0 / 0 | 13 / 397003 |
| C402 | `/tmp/c402-final-a.iH3mdS` | `/tmp/c402-final-b.9gpKr8` | 0 / 0 / 0 | 12 / 381728 |
| C403 | `/tmp/c403-final-a.9pkDJ1` | `/tmp/c403-final-b.JRplxW` | 0 / 0 / 0 | 11 / 350553 |

| 最终 PDF | SHA256 |
|---|---|
| [C401](henon_arithmetic/paper/main.pdf) | `7d39b29270015df61f0a286835d2f5c91084b91962bfd40d5c00086d4a8d4375` |
| [C402](nonlinear_return/paper/main.pdf) | `af77cd78166be37ca7629826038f0c2f48a0b52e85cac459e5972209edcba943` |
| [C403](spectral_regular_variation/paper/main.pdf) | `83ed1a84dffe7696596b31d3752c620e472a959afae4aed8faaee044379501fd` |

工具为 Latexmk 4.76、pdfTeX 1.40.22 / TeX Live 2022/dev/Debian、BibTeX 0.99d、
Poppler 22.02.0。本轮未安装或更换工具/字体。正文日期固定，三稿主文件均
启用可用的 `pdfinfoomitdate=1`、空 `pdftrailerid`、`pdfsuppressptexinfo=15`。
三个最终 PDF 均无 CreationDate/ModDate，无加密、JavaScript 或表单，A4、PDF 1.5。

## 原始证据和输出检查

每稿 `paper/final_build/a/` 与 `b/` 各保存实际 `compile.stdout.log`、
`main.log`、`main.blg`、`main.bbl`、`main.aux`、`main.fls`。顶层保存
`pdfinfo.txt`、`pdffonts.txt`、`main.txt` 及 `RUNTIME_INPUTS.sha256`。
日志是生成文件的原始复制，未删掉初次内部 pass 的普通未解析引用提示，
未为 Git 空白提示改写日志。最终 `main.log/main.blg` 则分别检查：

```text
Warning|Overfull|Underfull|undefined|Error|Fatal|Missing character
```

| 稿件 | 两构建最终 TeX/BibTeX 日志 | 字体资源 | 最终逐页目视 |
|---|---|---|---|
| C401 | 四份均无命中 | 23，均嵌入/子集/Unicode，Type 1 | 1–13，每页实际查看 |
| C402 | 四份均无命中 | 22，均嵌入/子集/Unicode，Type 1 | 1–12，每页实际查看 |
| C403 | 四份均无命中 | 21，均嵌入/子集/Unicode，Type 1 | 1–11，每页实际查看 |

每稿用 `pdftotext -layout` 实际抽取全文。逐页检查由协调者将最终 a 目录 PDF
以 `pdftoppm -r 100 -png` 渲染后逐张打开，检查标题、表格、公式上下标、
页边界、引文及书目。全部 36 页均可读，无裁切、覆盖、缺字或未解析引用；
C401 第 2 页显式看到修正后的非共振条件，C403 第 8 页看到正确的 q 次幂，
C402 第 8–9 页的阈值上标、五状态矩阵和全部精确示例排印正常。
渲染图保留于相应临时构建目录的 `render/`，不作为新的论文或提交载荷。

最终 `.fls` 中不同的绝对 `INPUT` 路径逐项 SHA256 保存：C401 为 146 项，
C402 为 148 项，C403 为 141 项。这是实际读取到的系统输入集合，不是宣称全部操作系统环境
均被封闭重建；稿件本地输入另由上述清单绑定。全部输出字节由批次 manifest
进一步绑定，不以哈希替代数学审查。

本次仅 C401 一句条件澄清影响最终正文。没有重跑既有精确或数值程序，
没有因为编号映射而重做前两篇已通过的构建，也没有新增所谓外部模型评审。
