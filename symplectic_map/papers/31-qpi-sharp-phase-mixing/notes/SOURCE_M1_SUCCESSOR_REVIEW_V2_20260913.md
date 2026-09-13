# Paper31：M1 实际 successor V2 有界续查

日期：2026-09-13 UTC。审查者：`/root/p31_complete_source_actual_review_v1`。
角色沿用首次完整实际源审查的 fresh 非作者；未写本次 V2，未参与其 lift 修正或书目补充，未再委派。
本件只复查实际 M1 修正及影响，不将局部续查冒称为第二次 FULL 全稿阅读，不重开未变证明、正式准入或查新。
实际为 secondary Codex xhigh，不冒称 GPT-5.4 MCP、跨模型或真人评审。

## 1. 结论

`M1_verdict: CLOSED / PASS`。
`successor_source_verdict: PASS_WITH_PRIOR_FULL_V1_REVIEW_AND_VERIFIED_V2_DELTA`。
`critical: []`；`major: []`；`minor: []`；`required_fixes: []`。

当前 V2 已准确区分 P30 的曲面／pencil／有限纤维接口与 Joshi–Roffelsen 的原初值空间和 lift 描述，
并在正文补齐原已接受的完整 lift 局部核验。其合法状态、定义域与原实动力没有削弱，没有引入新科学假设。
唯一 M1 已关闭；首次 V1 全文报告中的其他内容结论结合本次实际差分和未变源身份，可以沿用到 V2。
这不是 PDF、页窗或确定性构建 PASS。

`page_window_verdict: UNMEASURED`；`pdf_verdict: NOT_REVIEWED / NO_PDF_INPUT`；`compilation_verdict: NOT_RUN`。
原 22–30 页硬窗不变，高端上溢与表宽／公式断行等实际排版风险留给首次完整自然构建核验。

## 2. 实际修正与逐项核对

完整目录差分实际只显示三件变化：`references.bib`、`sections/01-introduction.tex`、`sections/02-real-surface-main-theorem.tex`。
三项修改都服务于 M1；没有暗改 §2 主定理、必要分析证明、原系数、Fourier 量词、原范数或 §§3–7。

| 核对项 | V2 实际位置及结论 |
|---|---|
| 归属拆分 | §2:15–18、57–63 明确把 P30 §2 的 surface/polar/finite-fibre 与 JR §2.1 的 lift 描述分开，并说明 JR 原段处于 finite-field setting；不再把全部 lift 归于 P30 §2。 |
| 前三个完整邻域公式 | §2:65–82 的 1→2、2→3、3→4 全部有理式是 P30 V4 §2:189–214 在 s=1,t=T 的正确转录；不只给 terminal 剩余坐标。a=0 时分母对任意 b 均非零，限制分别为 T(1−b)、b、(b−T)/T，均是仿射直线同构。 |
| 第四 terminal 的所有点 | §2:83–88 先在 b≠0 写目标 torus，再在 (a,b)=(0,0) 用目标 chart1，得到 a'=−b/[T(1+ab)]、b'=Ta。直接代入原 F 与目标 chart 定义亦得该式，分母在遗漏点非零。 |
| 原 torus 分母例外 | §2:89–92 用目标 chart1 给 a'=(x−y)/T、b'=T/y，覆盖整个 torus 对角 x=y；不是删掉分母为零的原点。与各开图的 rational-map 表达在稠密开集相等，能粘合。 |
| 全域双射责任 | §2:94–100 列原 torus 非对角及其逆、torus 对角、三条 terminal、第四线去零点和最后零点；目标层两两不交并覆盖。各式在任意代数闭扩域中成立，提供几何点的普遍单射和满射，不只提供实点的双射。 |
| 正则逆与完整 lift | §2:101–105 的原 symplectic 恒等式延拓与 Ω 非退化给 étale；universally injective étale morphism 为开浸入，加上满射即同构。这与 R30 Step1 的已接受论证一致，没有把“几何点双射”单独当作同构。 |
| 与后段的衔接 | §2:107–156 保留原完整纤维的有理式、真实 +P 和四 terminal 表；前文新 lift 核验现在实际承担后段“both maps are regular”的前提，不产生循环引用。 |
| 引言及新书目 | intro:91–106 正确概括来源分工并说本稿检查 full real lift；bib:62–70 使用真实固定 arXiv:2508.18578v2，不把原有限域描述直接宣传为本文全实证明，不冒称 VOR 内容一致。 |

新增局部符号 w、A、B、C 在此核验段明确定义，没有改动后续 w_±、PF H、相位或主项含义。
新增证明是已接受 R30 完整局部接口的自足转录，不是对原 F 的另一构造，也不消费其 Picard 增长或任意阶回返结果。
已检查 s=1,t=T 的代入与 R30 的有限阶 r=1 条件相容；T>0 保证所有需要的非零参数。
原正文中后置的显式 Jacobian／symplectic 计算仍给同一 rational identity；新段先使用该直接恒等式并不依赖尚待证明的 lift 正则性来计算它。

## 3. 引用补充的实际使用边界

已亲自 FULL 读 `LIFT_SOURCE_CITATION_SUPPLEMENT_V1_20260913.md`，62 行。
该补充把 JR 的固定 arXiv v2 题录、§2.1 文字范围与官方出版元数据的搜索摘录层级分开，保留受限入口和未读 VOR 正文的边界。
当前 BibTeX 选择精确预印本身份：作者 Nalini Joshi／Pieter Roffelsen，题名 Arithmetic dynamics of a discrete Painlevé equation，
v2 日期 2026-01-16，arXiv DOI 与固定版本 URL，均与该实际补充记录一致。
其 year=2026 对应所引用 v2 的日期；没有把文章号或原 v1 年份误填为当前版本身份。

本轮本人没有重新打开 JR 外文网页／PDF或受限出版页；上述外部源身份核对依赖已明确提供的实际引用补充，
不冒领补充作者或 root 的独立阅读。本轮对全实 lift 的判断来自亲读 V2 与 R30/P30 对应原式，
不把 JR 有限域小节末句当作全实证明。补充记录中原第四 chart 的显示下标风险没有复制进 V2；V2 使用自己核定的第四坐标。
未新增检索、评分或权限要求，也未改旧六项引用记录、两锁与 V1。

## 4. 实际读取范围与身份

以下 line 范围按各实际文件计；本轮内容是有界续查，9件字节未变不等于本轮重新 FULL 读了它们。
本次亲读完整 V1→V2 目录差分、V2 §2:1–170、intro:71–106、bib:44–70；
R30 `docs/research-batch07/PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md` 1–18、54–70、107–160；
P30 V4 `sections/02-surface-pencil.tex` 189–214；上述引用补充 FULL 1–62。
首次完整 V1 及工作流／paper-write 指令阅读由保留的首次报告绑定，未因本次局部修正重跑未变阶段。

| 本轮输入 | 行／bytes（整件） | SHA-256 |
|---|---:|---|
| COMPLETE_SOURCE_ACTUAL_REVIEW_V1_20260913.md（先前本人 FULL 交付，本轮核身份） | 177／18603 | `c2f15cd1dbe8ee2ccb3dfe85dfd2ea408b608f3403a38dcb4417063835fa990b` |
| LIFT_SOURCE_CITATION_SUPPLEMENT_V1_20260913.md（本轮 FULL） | 62／5992 | `680f1016a6caa1b220591e41507b31c4637415202057f700b0adb5d8a024c6cb` |
| R30 PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md（上述 PARTIAL） | 368／16747 | `9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c` |
| P30 V4 sections/02-surface-pencil.tex（上述 PARTIAL） | 446／20456 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |

当前完整 V2 根为 `papers/31-qpi-sharp-phase-mixing/paper/v2/`，实际共12件、2,454行／108,337 bytes。
所有整件 SHA 均由本人本轮计算；“未变”是与首次报告所绑定 V1 的实际一致，不由文件名或父代理摘要推断。

| V2 相对源文件 | 行／bytes | 与V1关系／SHA-256 |
|---|---:|---|
| main.tex | 41／1277 | 未变；`fcbfe0ac6f8ad6364728e7c86981bd1eef2d912c7d125c6d710a155d50cd53fa` |
| math_commands.tex | 17／577 | 未变；`d69b67aa41f2692a1df7c49de52a5299d4f6dcdec8e094d27eb603dc6fa3fc15` |
| references.bib | 70／2606 | 实际变动；`692c0775a3dd14407937b0e5404d150cdecfd7cbabc10081d07f3607f3dba659` |
| sections/00-abstract.tex | 21／1383 | 未变；`6a9eb69e22ee7d7bb005081243c8921bf1bfeebc13017e6c48f1763b9d71e6d6` |
| sections/01-introduction.tex | 106／5632 | 实际变动；`37ebda239db6121018bec9c5cc49186a7e32d1e0d607b07fe77de33a8c220cdb` |
| sections/02-real-surface-main-theorem.tex | 483／21027 | 实际变动；`1c5ffc10366eef513b3fd8862018c06ee880fc7b4385ef23f00965bed6b4ed31` |
| sections/03-picard-fuchs-forcing.tex | 174／7007 | 未变；`b812c308cce979012123edddf55704bab29a3311563aa5089ec7897f96ed72f2` |
| sections/04-global-frequency-geometry.tex | 430／18174 | 未变；`a5bcb49e7c47142e3bcf46fff6d4c3f4dada43a037170daf3b37eb74273e02d8` |
| sections/05-hyperbolic-fibre-estimates.tex | 490／22124 | 未变；`2b6c987becda66caf9c5e57e0ada24ca014043aba6a5db11bc7ee50ff90784e6` |
| sections/06-elliptic-jets-endpoints.tex | 341／14435 | 未变；`fc9a1d82c9d9d4b60bc680babde6afbeb7f9d6a3aff8286a9a99d9bf6ec686e6` |
| sections/07-global-asymptotics-sharpness.tex | 267／13318 | 未变；`57e8263b11320fe657f430d0af3b5eafdc1bb5a86ed8c3662ab2c6cbd33a25a2` |
| sections/08-conclusion.tex | 14／777 | 未变；`6cdce0e4e2c29c2f71417f55008b1281317d9f000e3c96ac812498fd561fd9c7` |

## 5. 交付边界

本轮唯一新增文件为本报告；未改任何源、锁、索引、先前报告或已接受产物，没有编译、CAS、数值或外部操作。
可以据首次完整 V1 实读及本次 M1 successor 实际复查进入既定首次完整构建；后续实际页窗、日志、双根确定性、全页 PDF及终局完整性仍须各自真实证据。
交付前本人 FULL 读回本报告至 EOF，最终行数／bytes／SHA 在交付消息绑定。交付后停止编辑。
