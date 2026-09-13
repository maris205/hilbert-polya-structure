# Paper31 actual source/PDF review V3

日期：2026-09-13。审查对象：完整冻结 `paper/v3/` 及实际 `natural-20260913-r2/r3` 最终 PDF。
角色：同一首轮 FULL source fresh 非作者审查者；实际为 secondary Codex xhigh，不冒称 GPT-5.4 或跨模型。
本报告是 V1 首次完整源审查、V2 唯一 M1 successor 审查、V3 两行实际变更及本次全部 31 页实际 PDF 的合成验收。
本轮未重新读取全部 12 件 TeX/BibTeX 正文源，亦不作这种声称；没有重开旧数学包、正式四门、评分或查新。
仅新增本报告；未编辑源、锁、构建脚本、日志、索引或旧报告，未编译、清理、覆盖构建根或委派。

## 1. 结论

- `composite_actual_source_pdf_verdict: PASS`
- `prior_M1_status: CLOSED / PASS`；V3 未改变已关闭的归属与全点 lift 修正。
- `actual_page_window: PASS`：31 总页，正文实际第 1–30 页，参考文献实际第 31 页；正文 30 位于锁定 22–30 窗内。
- `actual_render_and_transcription: PASS`：全部 31 页逐页图像及全部提取文字亲读，未见缺段、错排公式、错符号、裁切或未解引用。
- `same_source_two_root_pdf_identity: PASS`：r2/r3 最终 PDF 字节一致，各 528155 bytes。
- `critical: []`；`major: []`；`minor: []`；`required_fixes: []`。

这里的 PASS 只完成本报告负责的完整 actual 稿件/PDF 门，不代替后续另一位非作者的终局完整性审查、本地接受记录或批次完成状态。
页面不再是旧报告的 UNMEASURED：本次已有实际 PDF、全页图像、全文文字和准确正文末页标记支持测量；没有改变页窗或请求例外。

## 2. 审查链与本轮真实输入

此前由本审查者实际完成并保持不变的记录：

| 记录 | 行 / bytes | SHA-256 | 本轮如何使用 |
|---|---:|---|---|
| `COMPLETE_SOURCE_ACTUAL_REVIEW_V1_20260913.md` | 177 / 18603 | `c2f15cd1dbe8ee2ccb3dfe85dfd2ea408b608f3403a38dcb4417063835fa990b` | 沿用其中首次 FULL 12 源及原证明/合同实际读取记录；唯一 M1 由下一行关闭 |
| `SOURCE_M1_SUCCESSOR_REVIEW_V2_20260913.md` | 93 / 9156 | `1360aa0267dc69f76ecd3f58c2d56d27fda84b5410cd6edf3c60ef48edc23bfb` | 沿用已亲核 V1→V2 完整目录差分、实际 lift 上下文及准确来源接口 |

本轮亲读 `R0_DIAGNOSIS_AND_V3_RECOVERY_PROTOCOL_20260913.md` 全部 1–61 行（4707 bytes），SHA `32b8f727e4284af0b3427380f3c74daad95111f212bfc097661e860094b469b9`。
其中 r0 的后处理失败、保留现场及仅两处制作修复与实际差分一致；协议的执行前状态是历史记录，未将其改写为事后成功预言。
本轮 FULL 读 `PUBLICATION_LOCK_V1_20260913.md` 1–72 行，SHA `65cd1504f15890bbba0d9b9221062303f2daf17640d161f62e8841514f4e4a5c`。
科学锁未变，SHA `b056a664863e41cf778225118ea719a3e43b4a78c451d302703f423c931dd584`；其 FULL 阅读属于既有 V1 审查，本轮只核身份，不冒称再读。
本轮 FULL 读 `/root/autodl-tmp/.codex/skills/paper-compile/SKILL.md` 1–251 行，采用其字体、实际页面、页界及日志核验项；只读范围和项目锁覆盖默认清理/重编译、会议页数或附录移证建议。
此前 paper-write 及 writing-principles 的使用和 FULL 阅读沿用既有记录；本轮未触发另一个写作或跨模型改稿循环。

### 2.1 V3 完整 12 源身份

`notes/SOURCE_V3_20260913.sha256` 全部 12 条已实际读取，12 行 / 1164 bytes，SHA `4e1a98c1e273b8d2e138b91952a1c1e1ce2e00ac6006521714ddaf0dbd8beae8`。
V3 共 2454 行 / 108359 bytes。对 V3 原目录及两根工作副本分别执行清单校验，均 12/12 OK。

| 相对 `paper/v3/` 的路径 | 行 / bytes | SHA-256 |
|---|---:|---|
| `main.tex` | 41 / 1277 | `fcbfe0ac6f8ad6364728e7c86981bd1eef2d912c7d125c6d710a155d50cd53fa` |
| `math_commands.tex` | 17 / 577 | `d69b67aa41f2692a1df7c49de52a5299d4f6dcdec8e094d27eb603dc6fa3fc15` |
| `references.bib` | 70 / 2606 | `692c0775a3dd14407937b0e5404d150cdecfd7cbabc10081d07f3607f3dba659` |
| `sections/00-abstract.tex` | 21 / 1383 | `6a9eb69e22ee7d7bb005081243c8921bf1bfeebc13017e6c48f1763b9d71e6d6` |
| `sections/01-introduction.tex` | 106 / 5632 | `37ebda239db6121018bec9c5cc49186a7e32d1e0d607b07fe77de33a8c220cdb` |
| `sections/02-real-surface-main-theorem.tex` | 483 / 21027 | `1c5ffc10366eef513b3fd8862018c06ee880fc7b4385ef23f00965bed6b4ed31` |
| `sections/03-picard-fuchs-forcing.tex` | 174 / 7007 | `b812c308cce979012123edddf55704bab29a3311563aa5089ec7897f96ed72f2` |
| `sections/04-global-frequency-geometry.tex` | 430 / 18174 | `a5bcb49e7c47142e3bcf46fff6d4c3f4dada43a037170daf3b37eb74273e02d8` |
| `sections/05-hyperbolic-fibre-estimates.tex` | 490 / 22121 | `0fffb4535768e2688d36a93100bf60f4536b213ee0554af27dd4c92d43d634e4` |
| `sections/06-elliptic-jets-endpoints.tex` | 341 / 14460 | `c2d234ad91053f79609ee182f10815f939670f4a4db3d95465aa4e4bf1fb4661` |
| `sections/07-global-asymptotics-sharpness.tex` | 267 / 13318 | `57e8263b11320fe657f430d0af3b5eafdc1bb5a86ed8c3662ab2c6cbd33a25a2` |
| `sections/08-conclusion.tex` | 14 / 777 | `6cdce0e4e2c29c2f71417f55008b1281317d9f000e3c96ac812498fd561fd9c7` |

### 2.2 V2→V3 全目录差分及影响

亲自执行并 FULL 读 `diff -ru paper/v2 paper/v3`，只有以下两个单行替换；其余 10 件字节未变。

1. §5 源第 248 行：`They commute and have bounded coefficients and derivatives on the` 改为 `They commute, with bounded coefficients and derivatives on the`。本轮另亲读 V3 第 238–260 行实际上下文；第 19 页的向量场、交换性、有限阶系数界及随后全部移动入口式未改变。实际行落在正文框内，旧 0.75978pt overfull 不再出现。
2. §6 源第 276 行：小节标题中的 `$T=3/16$` 包装为 `\texorpdfstring{$T=3/16$}{T=3/16}`。本轮另亲读 V3 第 268–294 行；第 25 页仍显示正常数学标题，PDF 实际书签为 `The quadratic endpoint at T=3/16`，指向第 25 页。端点相位、坐标变换和系数未改。

这两处均是制作修正，没有删除原点、改变观察量/量词/常数、迁移证明、修改版式或重新选择页数版本。
M1 所在引言、§2 和新增 JR 书目在 V3 字节未变；实际第 2–4 页仍区分 P30 曲面/pencil 接口、JR 有限域描述与正文自己的全实 lift 核验。

## 3. 实际构建与显示来源核验

- 两个输入 PDF 均是 `build/natural-20260913-r2/work/main.pdf`、`build/natural-20260913-r3/work/main.pdf`；SHA 同为 `fc5d4419b6ddd2d9faf9ebb08b5319a3e249432c332944eb506f645857257640`，各 528155 bytes。
- 两根 `logs/absolute-inputs.sha256` 各 144 行 / 17535 bytes，SHA 同为 `b463baff29948284177c09370c2e0d93aade3745f487d57c95b2a7578b69978b`。本轮实际逐项校验各清单，均 144 OK、0 非 OK；并未声称 FULL 阅读全部依赖文件的源码。
- 144 项的边界是 final TeX recorder 的绝对路径 INPUT；它不自动成为独立 BibTeX 全输入捕获。本报告不据此声称超出该记录范围的完整依赖 capsule。
- FULL 读 `scripts/build_natural_v2.sh` 1–64 行，SHA `016eb9530c36ec27b3c6bc17b1988b4ddbab1bd426009e282a785efd861b297f`。实际源根 V3、清单 V3、r2/r3 absent-root 约束和四遍序列与恢复协议一致；本轮没有运行该脚本。
- 实际读两根全部八个单行命令记录及八个退出码记录：pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX；各退出码 0。命令使用 `-fmt=pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder`。
- FULL 读 r2 `logs/environment.txt` 全部 8 行：`SOURCE_DATE_EPOCH=0`、`FORCE_SOURCE_DATE=1`、`TZ=UTC`、`LC_ALL=C` 及固定输入/格式路径。完整脚本同样约束两根；没有联网获取依赖。
- 对两根 final TeX log 与 BibTeX log 实际检索 `Warning|Error|Overfull|Underfull|Missing|undefined`，均无命中。这里只声称针对性诊断扫描，不把扫描声称为逐行 FULL 阅读所有历史日志。
- 对 r2 PDF 重新执行 `pdfinfo`、`pdffonts`：letter 612×792pt，31 页，无加密；26 个字体记录全部 embedded/subset/Unicode=yes，均 Type 1，无 Type 3；Author 元数据为空。
- 亲读实际 `main.tex` 全部 1–41 行：11pt article、1 inch 四边、标准正文，无压字/缩边距/调行距命令；唯一正文后 `\clearpage` 用于单独起参考文献。
- 两根实际 `main.aux` 的 `LastBodyPage` 均为 30，七个 `bibcite` 对应实际编号 [1]–[7]。实际 PDF 图像和文字都显示第 30 页为结论、第 31 页开始 References。
- 实际 PDF 有 29 个大纲项、141 个链接注释；读取解析后内部页目标未见越界。5 个去重外部 URL 均为本稿注明的固定 arXiv 版本，正文引用没有 `?` 或未定义编号。

显示来源不是按文件名推定：本轮将 r2 PDF 的每一页重新用 `pdftoppm -singlefile -r 130 -png` 渲染到 stdout，与已有 `inspection-root/page-01.png` … `page-31.png` 分别 `cmp`。
31/31 页 PNG 字节完全相同；没有生成或覆盖新图文件。已看图像实际为 1105×1430、130 dpi 的完整单页，不是拼图、局部裁切或源摘要。
全文阅读直接来自该 PDF 的 `pdftotext -layout ... -`，按真实 form-feed 分页完整输出 1–31 页；两根重新提取结果也分别与其保存的 `logs/main-layout.txt` 字节一致。

## 4. 全部 31 页实际阅读账本

以下每一页均亲自显示并阅读完整原图，同时 FULL 阅读该页全部提取文字；列出的重点不是仅仅读到该重点。
所有页共同检查标题层级、正文/数学字号、上下标及共轭横线、分式/根号/矩阵/积分符号、编号、左右边界、行间/表格重叠、页脚及跨页证明衔接。

| 实际页 | 内容与对应审查重点 | 结果 |
|---:|---|---|
| 1 | 匿名题名、完整摘要、引言开头、三率 Table 1；长题名与表格均未越界 | PASS |
| 2 | 原正则性/全模/奇偶贡献；已核文献的范围与版本；P30/JR 来源及证明组织 | PASS |
| 3 | §2 原 map/integral/Ω、八次 blowup、代数开曲面与实 locus 区别；Prop.2.1；首三完整 lift 公式 | PASS |
| 4 | 第四终端例外点、环面对角、全几何分层与 étale 结尾；+P；完整 Table 2 | PASS |
| 5 | 两临界能量及实圆计数、临界点 Hessian、判别式和 cubic 实根论证 | PASS |
| 6 | 上区间真实 2P/order-four 锚；节点型；正测度、properness、Π 定义及交换性 | PASS |
| 7 | Π image 与 fixed-point space 的区别；原范数；G=F²、真实 lifts、全 k stationary 系数 | PASS |
| 8 | 全部 A/B/D 定义、β/γ、Theorem 2.5 三率与 C²⁰、逐 N 范数、sharpness 精确量词 | PASS |
| 9 | §3 PF operator、实际 j∈{1,2}、Wronskian、marked reduction 两个多项式恒等式 | PASS |
| 10 | 精确 Q_PF 原函数、O 处极点抵消、全部移动端点项、forcing 与真实返回因子 | PASS |
| 11 | q₀ 表观极点衔接；persistent circle 的正向解析参数与准确有限锚/中心 jets | PASS |
| 12 | 锚定积分常数、H_* 因式分解、单零界、中区间存在性及上返回参数开头 | PASS |
| 13 | 实际 2P 有符号参数、h=1 与 q₀=0 的解析延拓；无穷常数 lemma | PASS |
| 14 | 无穷根的可微余项、完整椭圆积分常数与导数界、两个不同移动尺度 | PASS |
| 15 | 先可微后取限、T=1 不除 logT、严格全参数分类证明 | PASS |
| 16 | Table 3 五参数区间、按圆计数与同能两种圆区别；鞍点原 Jacobian/线性化 | PASS |
| 17 | 一/二 passage 完整周期、两侧同一解析 τ、局部积分构造；跨页末句完整接续 | PASS |
| 18 | τ 等式跨象限/全圆延拓、不是全局常时模型；原范数及 Π 的 Hölder 损失 | PASS |
| 19 | 全阶 mixed symbol、固定截面、H_box、已修语法行、全部移动入口 Leibniz 公式 | PASS |
| 20 | 高阶链式归纳、外弧 bounded-time、重叠/周期接缝、整个非零 Fourier 家族 | PASS |
| 21 | 同一 τ/L 的倒导数、R_hyp 正下界、固定完整 χ、全模振幅与转置算子 | PASS |
| 22 | 真正 boundary 因子、逐 N 原 C^(N+2)、完整两侧求和；正向椭圆 Morse 图 | PASS |
| 23 | 正向解析对称角、signed-radius identity、原 first jets、全 k 可和余项与准确范数 | PASS |
| 24 | 有限范数偶函数下降、四阶余项除法、准确两 jet 系数；完整端点相关定义 | PASS |
| 25 | 两 endpoint 准确负系数/i 系数、全模余项；三次分部；修后数学标题及二次坐标 | PASS |
| 26 | 紧支撑二次端点的真实积分/误差；同能 persistent 圆分离；global Fubini 全模式 | PASS |
| 27 | scalar stationary phase 完整 C⁴ 证明、全 k 统一余项；完整原曲面的单一分割 | PASS |
| 28 | persistent 两侧只计一次、无新增空间端点、C²⁰ 汇总；原奇偶两上圆交叉配对 | PASS |
| 29 | 合法原 smooth complex/real sharpness 例、T=1 开稠密 first-jet 条件及非平均量词 | PASS |
| 30 | 完整结论，范围与引言/定理一致；自然分页的短结论页，不是人为插入空页 | PASS |
| 31 | 全七条文献、作者重音、卷页/文章号、固定预印本版本、分行 URL 与引用编号 | PASS |

分页事实：第 2 页引言结尾有自然余白，第 30 页仅包含结论并有自然大块余白。两者没有隐藏内容、空页或人为正文分页指令，不构成本锁下的必要修改。
三张表分别位于第 1、4、16 页；表头、每一行和表注完整，无浮动表遮蔽正文。全文无图或实验产物，不存在待补的图例/实验门。
个别 pdftotext 结果将复合数学符号拆成多行或控制字符，这是提取顺序现象；对应原图上共轭、花体/黑板体、上下标、绝对值和根号均正常，并未将文本提取畸形误判为 PDF 缺字。

## 5. 合成内容、书目与剩余风险

本次 FULL 实际 PDF 与既有 FULL 源审查的论证责任、V2 实际修正及验证后的构建源逐项对应：没有从已准入证明转录后再丢掉必要步骤的迹象。
尤其原完整曲面与终端点、+P 和正 measure/proper 接口、circlewise Π、全参数 stationary 分类、全部主系数/全模余项、鞍点真正边界、两个端点常数、完整分割和原奇偶 sharpness 均有上表所列实际正文落点。
没有把摘要/引言的主张留给不存在的附录；无内部 FAIL/PASS、代理名、流程编号、TODO、占位证明、虚构实验或不相关旧研究结果混入论文。
引言贡献维持单一具体离散映射的完整 sharp correlation theorem；清楚承认已有 separatrix/phase-mixing 方法，未夸称首次或新的普适 damping 机制。

书目本轮另 FULL 读 `paper/v3/references.bib` 1–70 行并逐条对照第 31 页。
[1] 如实标 Anonymous、unpublished local manuscript/version 4，未捏造公开出版身份；[4] 如实为 Joshi–Roffelsen 精确 arXiv:2508.18578v2，未冒称读过 VOR。
[2] 与 [7] 区分正式期刊题录和实际用于比较的固定预印本版本；[3]/[6] 为所列固定预印本，[5] 为已核正式题录。
七条均在实际正文使用；作者、来源、正式/预印本身份与此前核准记录一致。本轮不新做文献检索，外部文献内容的亲读范围沿用此前报告和引用补充，不冒称本轮重新读过七篇全文。

本次无新增 critical/major/minor，没有为了形式凑问题或要求重证明既有接口。M1 仍关闭，两项制作修复已验证，页窗、字体、完整显示与实际同源双根身份均有实证。
后续只剩本锁安排的另一位独立非作者终局完整性门及其后的主控本地处置；本报告不替该审查预授结果。

## 6. 完成与停止

末次复核已确认 V3 清单、两根 PDF/输入清单和两锁身份未变。报告最终版本的亲自 FULL 读回至 EOF，以及自身最终行数、bytes、SHA，由交付消息确认，避免自指哈希。
停止后不再编辑本报告或其他文件，除非收到明确的后续实际变化审查任务。
