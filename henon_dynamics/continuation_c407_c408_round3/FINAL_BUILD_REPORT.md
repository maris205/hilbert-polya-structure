# C407/C408：实际终构建与全部页面 QA

日期：2026-09-06。本报告只记本次新增两稿；C404–C406 的 179 个旧
封存文件不回写、不重建，其 33 页收据仍以原包为准。

## 正文与引文门槛

协调者完整读取 C407 的 10 个、C408 的 11 个 TeX 输入，连同完整
证明包、合同和相关已取得的主来源。两篇均有非作者全文／实际引文
审查：[C407](reviews/C407_MANUSCRIPT_REVIEW.md)、
[C408](reviews/C408_MANUSCRIPT_REVIEW.md)。当前必须修订的数学、
引用或范围问题为零；这不是人类同行评审或全球优先权认证。

C407 的 BC 2018 旧结论比较补上唯一主根及非 very-inseparable 分支
限制后复核关闭。C408 的两项一般引理补上必要前提：交数加法中的
因子在极大理想内；形式消元势满足 dP(0)=0。实际模型一直满足这两
条件，未改主定理。C408 初稿两个长文件名的 overfull box 改用可断行
路径，修正前后日志均留存：[初稿日志](cluster_boundary/paper/draft_build/initial/main.log)、
[修正日志](cluster_boundary/paper/draft_build/corrected/main.log)。

作者初构建记录分别为 [C407](arithmetic_candidate/DRAFT_BUILD_REPORT.md)
和 [C408](cluster_boundary/DRAFT_BUILD_REPORT.md)。C407 作者同一目录
的强制重编译不充当下述两个独立新目录。其独立中文摘要的术语修正
“螺线管群（solenoid）”在 TeX 输入以外，没有改变终稿 PDF。

## 四个实际新空目录

每个目录由 mktemp 独立生成，只复制对应 10 或 11 个已审查 TeX
输入及目录结构，没有复制 aux、旧 PDF 或格式缓存。

| 稿件 | 构建 a | 构建 b | 两次退出码 |
|---|---|---|---|
| C407 | `/tmp/c407-final-a.yLocTd` | `/tmp/c407-final-b.wGyQv0` | 0 / 0 |
| C408 | `/tmp/c408-final-a.l8K8TR` | `/tmp/c408-final-b.bCgV42` | 0 / 0 |

各目录实际执行同一命令：

```sh
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

工具为 latexmk 4.76、pdfTeX 3.141592653-2.6-1.40.22
（TeX Live 2022/dev/Debian，kpathsea 6.3.4/dev）。stdout/stderr
原样保存为 compile.stdout.log。每个 a/b 目录均保留 main.log、
main.aux、main.fls 与该 stdout；入口为
[C407 a](arithmetic_candidate/paper/final_build/a/compile.stdout.log)、
[C407 b](arithmetic_candidate/paper/final_build/b/compile.stdout.log)、
[C408 a](cluster_boundary/paper/final_build/a/compile.stdout.log)、
[C408 b](cluster_boundary/paper/final_build/b/compile.stdout.log)。

四组实际 cmp 均退出 0：每稿 a PDF 对 b PDF，以及 a PDF 对作者
已修正、已审查的初稿 PDF。最终保存的是各 a 构建的 PDF。这里是
同环境、明确输入与日期设置下的字节复现，不声称任意 TeX 环境复现。

## 最终 PDF 与输入绑定

| 稿件 | 页数 | 字节 | PDF SHA256 |
|---|---:|---:|---|
| C407 | 13 | 411706 | `12cecce888926bcce1b89999c043eeff5c182253dedcba0e7827d387e0d849be` |
| C408 | 12 | 374170 | `9d94e32bff36110a16822b7cc9c784ff1c200caa72f888ca71aa5c48b7620621` |

TeX 输入清单及实际 sha256sum -c 全项 OK、退出 0：

- [C407 十项输入](arithmetic_candidate/paper/final_build/SOURCE_INPUTS.sha256)，
  清单摘要 `87750e85461f2bf823831a67b28cd2f90f2dc02117fab2fabcdca569e1b90163`。
- [C408 十一项输入](cluster_boundary/paper/final_build/SOURCE_INPUTS.sha256)，
  清单摘要 `d4e34d0621b8fdcd4d7de4cb58f2156d58c0ee71aba1d2eb31467cdb14052632`。

另从最终 fls 的绝对 INPUT 路径去重后实际计算系统输入摘要，退出 0：
[C407 runtime](arithmetic_candidate/paper/final_build/RUNTIME_INPUTS.sha256)
151 项、[C408 runtime](cluster_boundary/paper/final_build/RUNTIME_INPUTS.sha256)
131 项。这是被记录的外部构建输入，不是整个操作系统或容器镜像摘要。

## 文本、字体与全页目视

四份最终 main.log 按 Warning、Overfull、Underfull、undefined、Error、
Fatal、Missing character 扫描均无匹配；没有把正常的 rg 无匹配状态
记为 TeX 失败。最终提取文本中的 `??`、`[?]`、`[VERIFY]`、TODO、
FIXME 均无匹配。保留
[C407 文本](arithmetic_candidate/paper/final_build/main.txt) 和
[C408 文本](cluster_boundary/paper/final_build/main.txt)。

两份 PDF 都是 A4、PDF 1.5，无表单、JavaScript、加密或日期字段。
实际逐行核对的字体表中，C407 的 24 个和 C408 的 21 个字体资源
全部为嵌入、子集化、带 Unicode 映射的 Type 1 字体；见
[C407 字体](arithmetic_candidate/paper/final_build/pdffonts.txt)、
[C408 字体](cluster_boundary/paper/final_build/pdffonts.txt)。

协调者用 pdftoppm -r 100 -png 渲染终稿，并实际打开查看 **C407
1–13 页与 C408 1–12 页，全部 25 页**。长公式、表格、分页、证明
末尾及参考文献均可读，未见裁切、重叠、遗漏字符或超出页边。
两套临时逐页 PNG 留在对应 a 构建目录，没有将临时图像存在性当作
目视检查。全部页面检查完成后未再修改任何 TeX 输入。

## 交付边界

上述构建和排版 QA 不替代证明正确性。独立数学复核、六项原关系
局部检查、C408 被终止的大例及正式目标评价分别保持原记录；未
通过重复旧检查增加数字。新稿共 25 页，加原三稿 33 页，五篇共
58 页。本批至 C408 停止。

本目录最终成员与摘要由 [payload ledger](PAYLOAD_FILES.txt) 和
[manifest](MANIFEST.sha256) 绑定；封存后的核验及真实 Git refs
在 [当前入口](../CURRENT_RESEARCH_STATE.md) 记录，不循环写入
本文件自身所属的提交号。
