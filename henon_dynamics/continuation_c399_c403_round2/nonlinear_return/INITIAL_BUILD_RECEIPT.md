# C402 初稿编译与冻结收据

日期：2026-09-05。状态：`INITIAL_BUILD_PASS_SOURCE_FROZEN_FOR_REVIEW`。
本收据只报告作者初稿编译与自检；不替代独立全文审阅、终稿双新目录构建、
最终逐页 QA 或协调者的正式评价。C402 的 source theorem 与 target admission
分开：本有限边矩阵不推进目标算术实现，target 仍为 `REJECTED`；三类通用
算术控制的批次状态仍为 `INCOMPLETE`。这不是 source theorem 无效的断言。

## 实际编译

- 工作目录：由 `mktemp -d /tmp/c402-initial.XXXXXX` 实际创建的
  `/tmp/c402-initial.ZrqyET`；只复制本稿的 `main.tex`、`math_commands.tex`、
  `references.bib` 与 `sections/`。未在旧包中执行构建。
- 工具：latexmk 4.76；pdfTeX 3.141592653-2.6-1.40.22；BibTeX 0.99d；
  TeX Live 2022/dev/Debian。环境为 `SOURCE_DATE_EPOCH=1788566400`、
  `FORCE_SOURCE_DATE=1`、`TZ=UTC`。
- 执行命令：

  ```text
  env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC \
    latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
  ```

  实际通过 `set -o pipefail` 与 `tee` 保存 stdout；初次命令退出 0。
  自检和协调者均发现低次数 remark 的两处上标多了逗号，作者已定点把
  `q_{d-1}^{,n}` 改为 `q_{d-1}^{n}`；只复制这一改动到同一初编译目录，
  再执行同一命令，仍退出 0。该次为排印修正重编译，不是第二个独立构建，
  没有重跑数学检查。
- 最终 [PDF](paper/main.pdf)：12 页，A4，381728 bytes，PDF 1.5；
  SHA-256 `af77cd78166be37ca7629826038f0c2f48a0b52e85cac459e5972209edcba943`。
  日期采用正文固定字符串；`pdfinfo` 无 CreationDate/ModDate；主文件预置
  `pdfinfoomitdate=1`、空 `pdftrailerid` 和 pTeX 信息抑制。

原始证据保存于 [paper/initial_build/](paper/initial_build/)：

| 文件 | SHA-256 |
|---|---|
| `compile.stdout.log`（初次完整 latexmk 各轮） | `fdb1d4fbd6de7055cfedc3787fcddfd66426a4743fbaeb91320d9e9bd781e058` |
| `compile-after-typo.stdout.log`（排印修正） | `cd336f32ad074c01c552e773ea7499c74213a63cbff8de13fc63ca5a1ab600d5` |
| `main.log`（最终 TeX 日志） | `7c914545819833644a0a16bd6110110c14f8a5fa9c54e83da5c93ed5b1644df3` |
| `main.blg`（最终 BibTeX 日志） | `be97b1635710915660e16f70b82da0e23d6f246d7b4fde37f9eea701ebe2c95f` |
| `main.bbl`（实际生成书目） | `10ec119151eb8eef162679a5e7aa8b788b0b29dd98d81e59895fcfd4f112ed6e` |

首轮中间 pass 的 undefined citation 警告保留在原始 stdout 中，不隐藏；
latexmk 完成 BibTeX 和所需重编译后，最终 `main.log` 与 `main.blg` 搜索
`Warning|Overfull|Underfull|undefined|Error|Fatal` 无命中。全部 9 个引用语境
解析为 4 条书目；没有 orphan Bib 条目。`pdffonts` 列出的 22 项字体均
嵌入、子集化且有 Unicode 映射，均为 Type 1，无 Type 3 字体。

## 自检与正文定位

作者全文回读 8 个 section 文件、主文件、宏与书目。全文检索上标逗号、
双逗号与 `TODO/FIXME/XXX/VERIFY` 均无命中；此次修正没有改变任何数学。
`pdftotext -layout` 成功；仅渲染查看了 PDF 第 1、8 页，确认摘要标题及
修正后的低次数公式、二次权重段落无可见裁切。这是初稿抽页检查，**未**
宣称已经逐页视觉 QA。最终逐页 QA 仍由协调者完成。

| 主张／依赖 | 完整正文 locator | 初稿 PDF 定位 |
|---|---|---|
| 固定方案、点和与退化留数定义 | `sections/2_setup.tex`，Definition `def:residue-trace`，式 (2.3)–(2.10) | 页 2–3 |
| 全周期主定理、参数量词与矩阵 | 同文件，Theorem `thm:main`，式 (2.11)–(2.15) | Theorem 2.2，页 3–4 |
| 有限完全交／纯幂正规形留数 | `sections/3_residues.tex`，Lemma `lem:normal-form` | Lemma 3.1，页 4 |
| Hill 负号及短周期重合项 | 同文件，Lemma `lem:hill` | Lemma 3.2，页 4–5 |
| 大圆 Laurent 展开、收敛与必要次数不等式 | 同文件，Lemma `lem:local-expansion` | Lemma 3.3，页 5–6 |
| 周期无关逐点流界，主增量 | `sections/4_flow.tex`，Lemma `lem:uniform-flow` | Lemma 4.1，页 6–7 |
| 边状态双射、幂迹、整系数与逆 determinant | 同文件，主定理完整证明，式 (4.9)–(4.12) | 页 7–8 |
| 经典低次数阈值 | 同文件，Remark `rem:threshold` | Remark 4.2，页 8 |
| 二次权重、显式裁剪与五状态块 | `sections/5_consequences.tex`，Proposition `prop:quadratic` | Proposition 5.1，页 8–9 |
| 非平凡／非约化两个精确例子 | 同文件，Examples `ex:nontrivial`、`ex:parabolic` | Examples 5.2–5.3，页 9–10 |
| 普通 trace-class 代表 iff 幂零 | 同文件，Proposition `prop:trace-class` | Proposition 5.4，页 10 |
| 所有范围限制和有限检查地位 | `sections/6_scope.tex` | §6，页 10–11 |
| 元数据待作者确认、AI 披露与全部书目 | `sections/7_declarations.tex`、`references.bib` | 页 11–12 |

上述 PDF locator 据此次实际 `.aux` 和文本抽取，后续版式变化可能移页。
全部 4 条 BibTeX、具体原稿版本、访问证据与 9 个引用语境逐项登记在
[BIBLIOGRAPHY_AUDIT.md](paper/BIBLIOGRAPHY_AUDIT.md)，不是抽样书目审核。

## 冻结及接管范围

11 个数学输入文件的逐文件 SHA-256 已保存为
[SOURCE_SHA256.txt](paper/SOURCE_SHA256.txt)。可从 `paper/` 执行
`sha256sum -c SOURCE_SHA256.txt` 逐项核验；此清单不把 PDF／日志算作 TeX 输入。
本次正式交接后暂停源编辑，等待非作者独立全文审阅及协调者指派的定点变更。

四项旧证据保持原摘要：

| 冻结旧证据 | SHA-256 |
|---|---|
| `CONTRACT_SCOUT.md` | `b8780f67d4a9a23e66d2d0fe3f5a2c3c77a50c53a5930697baa00b23e8c28dfb` |
| `exact_check.py` | `f84450460221084ec5a19bead703872105d8d6b6532a4274d8b9c5e25519fe9f` |
| `EXACT_CHECK_OUTPUT.json` | `ba0911e8be0ef4de0a50fee2b6079db8844809fa03ad5743ad1a40eb871f94af` |
| `BUG_FINDING_C108.md` | `04f42e7579ff8c64cbb7a61fea6d5ccc45b954b36b1be37499214bec51ea6dfa` |

没有新实验、没有重跑历史生产脚本、没有修改旧审阅、共享索引、CURRENT、
正式评估或 Git。独立全文审阅、目标判定、终稿双构建及逐页 QA 不在这份
初稿收据的已完成范围内。
