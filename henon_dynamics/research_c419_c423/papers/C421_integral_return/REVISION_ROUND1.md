# C421 round 1：三项精确化修订与真实构建

2026-09-08 UTC。状态：**ROUND1_REVISIONS_IMPLEMENTED_AND_BUILT;
SECOND_MANUSCRIPT_REVIEW_PENDING**。

## 1. 结果与版本

协调者完整阅读 [第一轮非作者审查](../../manuscript_reviews/round1/C421_REVIEW.md)
后明确采纳其中 O1/O2/O3。该审查结论为 PASS、必改项 0；本次是三项
已获采纳的精确化建议，不把它们改称发现了数学错误，也不虚构分数
提升。作者已完整读完该审查并按授权逐项修改。

- [实际 round 1 PDF](build_round1/main.pdf)：**18 页，473,670 字节**。
- [便于审查的相同 PDF 副本](main_round1.pdf)。
- [round 1 TeX/Bib 快照](round1_source/main.tex)及
  [17 项源码摘要清单](ROUND1_SOURCE_SHA256SUMS.txt)。
- [完整构建控制台日志](build_round1/compile_console.log)、
  [最终 TeX 日志](build_round1/main.log)、
  [最终 BibTeX 日志](build_round1/main.blg)、
  [实际 PDF 提取文本](build_round1/main.txt)。

新 PDF 的 SHA256：

```text
c497c8f2efc4d6a22f28153ef27178040c3af8d099fa610ea564d1e1a7df575b
```

`main_round1.pdf` 与 `build_round1/main.pdf` 的摘要及 `cmp` 均一致。
这只是同一真实构建的便利副本，不计作第二个独立构建。

原 [round 0 PDF](main_round0_original.pdf)、`build_baseline/`、
`baseline_source/` 和 `BASELINE_SOURCE_SHA256SUMS.txt` 均未改动。
包根的 `main.pdf` 也暂保留原基线字节；**本轮与第二轮审查应使用
上述 `main_round1.pdf` 或 `build_round1/main.pdf`，不要误取旧别名。**
原基线报告保留其历史时点的陈述，不反改为修订后版本。

## 2. 逐项回应

### O1：把移位后的中心系数显式写出——已落实

修改位置：[第 4 节](sections/04_large_difference.tex)，当前第 78–85 行，
PDF 第 5 页。原文的两个中心仍是 `u+a+1` 和 `v+a+1`；新增明确
应用参数无关差分恒等式后的不等式：

$$
|2a(u+a+2)|\le2D,\qquad |2a(v+a+2)|\le2D.
$$

随后指出两移位系数相差 `D`，至少一个绝对值不小于 `D/2`，
所以 `|a|≤2`，包括 `a=0`。这消除了“中心”与“中心加一”的
紧缩措辞歧义。没有改变后续 `a=1,2,-2` 的排除、`F_8/F_12`
的存留、任何参数范围或原有编号。

### O2：有限核心章节开头限定剩余轨道——已落实

修改位置：[第 5 节](sections/05_finite_certificate.tex)，当前第 4–5 行，
PDF 第 7 页。开头现在明确先排除已列出的通道，才对剩余轨道使用
`D≤100` 的定理结论。没有将有限幅度界施加给无界符号族，也没有
改变实际有限枚举任务、种子范围、停止规则、历史结果或复现边界。

### O3：正层 F5 的反向轨道对使用精确结论——已落实

修改位置：[第 7 节](sections/07_level_counts.tex)，当前第 80–87 行，
PDF 第 12 页。把 `generally the two reversed oriented cycles`
改成明确的 `the two distinct reversed oriented cycles`。这里仍在
`k>0` 且平方测试成功的分支，两整数根不是退化的 `0,-1`，第 6 节
的唯一性证明保证它们对应不同的反向有向周期。`k=0` 合并为同一
循环字的表述仍原样保留，计数公式没有改变。

## 3. 改动范围与身份核对

本次仅修改以上三个生产 section 文件。其余 14 个 TeX/Bib 文件
逐字保持基线，包括主文件、宏、摘要、引言、分类表、所有最小周期
证明、计数命题本身、声明边界、参考文献与附录。`diff -qr` 对
`baseline_source/` 与 `round1_source/` 只报告这三个文件不同；三份
逐项 `diff -u` 已检查，变化恰为第 2 节所列内容。

| 输入 | 基线 SHA256 | round 1 SHA256 |
| --- | --- | --- |
| `sections/04_large_difference.tex` | `4e37506f595f0d071aec7750e86e77a139a20270f391dfc08795ae6078d70a0a` | `233dfd38be1cfa4de0d0f480bd394528adb117fd811fb7290922fbc843917110` |
| `sections/05_finite_certificate.tex` | `c4db267df7da3398fae89f4fbc3da3a8335f62a93fb87abfaa70ed6170c39f9a` | `59a9d1d7589832f31a6e9ad846d1a67a6e13f4f4ed68c4073c68b4b84907dde5` |
| `sections/07_level_counts.tex` | `f765363a097e6229df9d21155662bb4b718c6f6bd10a1a247e9d510fa304932a` | `b894422375088db417ae3a815832a3caa2295ab34b0472c396dc956665abfa71` |

修订前，工作源码对基线摘要 17/17 通过；修订后，新的摘要清单在
工作源码与 `round1_source/` 各核验 17/17 通过。原 `baseline_source/`
仍对基线清单核验 17/17 通过。两份清单各自 SHA256：

```text
baseline: 41fbb8062fbd91e57d04a34bd5082ada3990b8d81257e44410fcf9cb3e0daf53
round 1:  d25c04662e738dae4e753f5c9f33cc11cadbc3c09a9195e1c12d2a118591dfef
```

原 `main_round0_original.pdf`、`main.pdf`、`build_baseline/main.pdf`
在本次完成后仍均为：

```text
7fcfe7c00da4590cc44565d2343a5d3e37f233c5ece4798971891e9f145b5e1d
```

17 项源码快照含表格索引，但不再次复制或运行数学补充材料。
从快照复现需在包根使用对应 TeX/Bib 字节，或向工作副本提供同一
`supplement/`；快照并未被冒称是缺少补充材料仍可独立构建的包。
附录读取的历史主认证程序摘要仍为
`750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330`。
其源码、原始输出和旧证明树均未修改。

## 4. 实际构建与受影响检查

构建从包根运行，预先确认 `build_round1` 不存在后新建该目录，
不调用 `latexmk -C`，不清理旧构建。实际命令为：

```bash
bash -o pipefail -c 'env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build_round1 main.tex 2>&1 | tee build_round1/compile_console.log'
```

一次命令退出 **0**，无需修补后重试。latexmk 在该次调用内自动执行
3 次 `pdflatex`、2 次 `bibtex`；这是正常的交叉引用收敛，不是五次
独立构建。全部过程写入控制台日志，早期 pass 的未解析引用警告
未被删除。最终 `main.log` 与 `main.blg` 定向扫描中，Warning、
Overfull、Underfull、undefined、LaTeX/Package Error 均无匹配。

仍使用已记录的 latexmk 4.76、pdfTeX 3.141592653-2.6-1.40.22
和 BibTeX 0.99d；无依赖安装。无期刊模板或人为主文页数限制。
新 PDF 为 18 页：正文 1–13、参考文献 14、附录 15–18，与基线
分区相同。`pdffonts` 的 24 个字体记录均嵌入、子集化且有 Unicode
映射；PDF 未加密，letter 页面，大小为 473,670 字节。

实际提取新 PDF 全文后，检查了三段修改在成品文本中的落实，并
扫描全提取文本，未找到 `??`、`[?]`、`VERIFY`、`TODO` 或
`PLACEHOLDER`。本轮没有把该自动扫描称作第二次非作者全文阅读。

新渲染并逐页目视检查 **第 5、6、7、8、12、13 页**，对应三个
改动页及其后的重排页。新增不等式、有限节限定、F5 反向措辞都
完整可见，附近公式、页尾、停止证明、原生 zeta 与范围声明没有
截断或重叠。图片保存在 `build_round1/visual/`。本轮仅声明这
六页作者复查，不冒称已对修订后的全部 18 页作最终独立目视验收。

构建附件摘要：

```text
f62f9aa6d8cf6e0747297e062964dad894072ef6cb9bd127f7faf72158b1473f  build_round1/main.log
e0cb180bcc81f43e446ca8fcdab0b427863ef212e4c8bbb18b89069ff3a062c1  build_round1/compile_console.log
7b472eb62ec017ae4fc8a2457fe74a58d32871218a8d0bc891c0a69b54adffa7  build_round1/main.txt
```

## 5. 流程边界与第二轮交接

`paper-write` 及其完整阅读的数学写作／精确措辞参考支持本次三处
局部修改；`paper-compile` 导致新目录真实构建、引用／字体／PDF
检查。原稿件格式、定理范围、来源归属和内部 AI 审查披露保持不变，
没有套用技能示例的 ML 会议页数、外部模型或新增实验要求。

本次数学程序、有限核心重建、符号验证、旧诊断重跑、新来源检索、
GPU、外部模型调用、正式评价、Git 写操作均为 **0**。LaTeX 只把
未变的 Python 文件作为文字排版；没有执行其认证逻辑。构建、
摘要与静态比较不计作新的数学 PASS。

三项均已由作者落实并完成受影响生产检查；是否完成非作者修订
闭环由协调者／第二轮审者判断。接下来应读取本轮实际新 PDF 和
相应完整 TeX/Bib，作第二轮真实稿件审查。正式评价、最终双目录
字节复现、全部最终页独立视觉审查、封存及同步尚未在本报告完成。
没有宣告 C421 最终发布或五篇批次完成。
