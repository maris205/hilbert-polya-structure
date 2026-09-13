# Paper30 V2→V3 普通编译修复差异复核 V1

日期：2026-09-09。复核者：`/root/p30_vertical_alpha_complete_draft_review_v1`。
状态：`TERMINAL`。对象前缀：`papers/30-qpi-vertical-critical-ideals/`。

## 1. 结论与本轮范围

- `BUILD_FIX_SOURCE_DELTA: PASS`。
- `MATHEMATICAL_CONTENT_UNCHANGED: PASS`。
- `OTHER_NINE_SOURCE_FILES_BYTE_IDENTICAL: PASS`。
- `NEW_REQUIRED_SOURCE_FIXES: NONE_IDENTIFIED`。
- `REBUILD_SUCCESS / PHYSICAL_PAGE_COUNT / PDF_ACCEPTANCE: NOT_ASSESSED`。
- `route_applicability: NOT_APPLICABLE`。

本轮是原完整稿审查之后的有界修复复核，不是重新审查完整证明或候选四门。
本人读取了 V2 与 V3 两源树的完整实际 diff，并逐件 `cmp` 全部十一件源文件。
另直接读取两版本 §5:55–95、§7:321–355，及 r0 日志两处相关上下文。
这不是重新全文读取两节或共同六十九件科学包；未据既有 PASS 标签代替实际差异检查。
仅新增本报告；未改任何源、锁、既有报告或构建现场，未编译、测页或打开 PDF。

## 2. 两项实际差异与对应原失败

### D1：§7 分段式中的第二行区间

r0 `work/main.log:1142–1146` 指向 `sections/07-odd-jets.tex:338`，
错误为 `Illegal unit of measure (pt inserted)`；该行原为 `\\[1,5]`。
实际 V3 仅在换行命令后添加空组，改为 `\\{}[1,5]`。
原相邻方括号会被换行命令读作可选行距；空组阻断该语法入口，并使 `[1,5]` 留作第二行数学内容。
两分支仍准确为 $m=1$ 时 $[1,4]$、$m\ge2$ 时 $[1,5]$。
支持包含关系、原 $\Gamma_m$ 与 $\gamma_m$、量词、后续证明及一般 $m$ 的第五次上界均未变。
这是一处 TeX 解析修复，不新增行距数值，也不修改数学分支。

### D2：§5 整数插入公式改为无编号陈列

r0 `work/main.log:885–890` 的实际警告是同段 `Overfull \hbox (50.51622pt too wide)`。
V2 第 72 行的行内公式在 V3 第 72–74 行改为 `\[ ... \]`，并将原句末点置于公式末尾。
公式仍逐项为 $\bar\alpha_r=m[z^{mN}]\operatorname{tr}(B^{N-1}C_0)$。
未改系数 $m$、提取次数、矩阵指数、原插入项或等号两边。
紧邻的 $dB=\sum_jC_j$、循环旋转的相位一、对 $m$ 项求和及后面的有编号式均未变。
新陈列不增加公式编号或 label，也没有删正文、改字号／边距／行距或将证明移出正文。
它是针对已出现溢出的自然断行；本轮静态复核不冒称已验证新 PDF 的实际消溢效果。

## 3. 实际字节身份与未变范围

完整递归 diff 恰有上述两处，没有其他文件差异。
逐件 `cmp` 相同的九件为 `main.tex`、`macros.tex`、`references.bib`、
`sections/01-introduction.tex`、`02-surface-pencil.tex`、`03-spectral-jacobian.tex`、
`04-closed-hasse.tex`、`06-first-layer.tex`、`08-two-jets.tex`；后六项均在 `sections/` 下。

| 实际读取对象 | SHA-256 |
|---|---|
| V2 §5 | `d25e401b8b14d56ce1eb8d0eb91c56bac8849dd9be933c6dcf19ac47a254f190` |
| V3 §5 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| V2 §7 | `8a5d216f27ca6b9c41a6c911f1d572b6728682138a3d96874c82f33b60eff690` |
| V3 §7 | `046f8cf808cc64de570605b316bcb5b0c6970f52492a585f97f97597ae2d74f5` |
| `build/natural-20260909-r0/work/main.log` | `c65328c029f3d14dc2134c3f16ef7a46bd7b3eecf6298c5ed388455be4d8cef8` |

结论仅覆盖这些真实修复及其直接消费者；不覆盖新构建日志、物理正文窗口、逐页图像或终局接受。
主控的新根运行消息没有用作本轮 PASS 的数学或渲染证据。原 r0 失败不被本报告改写。
