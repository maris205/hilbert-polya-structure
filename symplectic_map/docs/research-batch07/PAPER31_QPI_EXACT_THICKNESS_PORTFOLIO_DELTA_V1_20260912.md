# Paper31：准确初始接触与固定厚度的组合内增量核查 V1

日期：2026-09-12 UTC。独立执行席：`/root/p31_exact_thickness_portfolio_v1`。
状态：`NET_LOCAL_DELTA_IDENTIFIED / NO_DIRECT_LOCAL_THEOREM_DUPLICATION_IN_READ_SCOPE`。
`route_applicability: NOT_APPLICABLE`。本件是有界本地非碰撞核查，不是全球查新结论、数学复审、正式四门票或容量认可。

## 1. 结论与一个必须扣除的旧项

以冻结[Phase A][A]的 V1–V3 为准确候选指纹，扣除已接受模型、指定点、支持判据、完整固定理想及一般传播后，仍存在实质本地增量：**固定原 $T$ 的指定截面初始交数现在在全部素域好点、全部有限节点上得到了准确求值，并供给同一原迭代的局部固定厚度**。
这不是 Paper30 垂直临界理想的改题，也不是把旧未知 $i_n$ 的结构式原样重投。
结论限于下文实际读取的最接近论文和旧 qPI 记录；不以定向检索宣称全工作区或全部文献绝无先例。

但有一项细节不能再计新：**正特征好点 $q=8h-9=0$ 不发生 prime-to-$p$ 切触，已经是旧结果**。
旧[Manin作者][M] Claim 3，71–72行，及证明354–365行已经明确排除；[旧接受][MA]9–10、62–68行接受了这一内容。
本轮在该点的新信息是 Hasse 零阶的准确求值，以及素域 $p\mid d$ 时 $c_*=2$ 的互补初始化，不是上述旧排除。
此项扣除指旧正特征范围，不把旧稿未处理的特征零范围冒称已经接受。
冻结[A]和旧[增量批评][CR]不回写；后继brief与处置应按这个准确新旧划分表述。

## 2. 原问题身份及逐主张净增量

始终固定

$$
F_T(x,y)=\left(\frac T{x-y},\frac xy\right),\qquad
W_h:v^2+huv-Tv=u^3-Tu^2,\quad P=(0,T),\quad z=h-h_*.
$$

原完整 $\mathcal U=S\setminus D$、四末端线、原零截面 $O$ 和 $T\ne0$ 不变。
令 $q=8h-9$、$H=32T+3h$、$i_n=(nP.O)_{h_*}$。
这里的 $H$ 是新 forcing 线性因子，不是 Paper30 用字母 $H$ 简写的 Hasse 多项式 $H_p$；也不把 $q$ 当作原时间乘数或域大小。

| 冻结主张 | 已包含，必须扣除 | 扣除后的实际本地新增 |
|---|---|---|
| V1：原 forcing、真实好切触阶、Hasse与 $N_p$ 根阶 | [M]/[MA]已有指定短式、$\lambda=-q\,dh/\delta$、显式非零 $\mu(P)$、同一 $N_p=q^p\mu(P)$ 及必要支持；正特征 $q=0$ 排除也已有。PF/Manin一般构造与读阶机制不记本轮新方法 | 原 forcing $-H/(q\delta)$、独立正特征 $\mu(P)'=-AH/q^2$ 和 $N_p'=-q^{p-2}AH$；所列域中每个真实素于特征好切触的准确阶 $2+\mathbf1_{H=0}$；Hasse零点准确阶 $1+\mathbf1_{q=0}$，以及准确 $N_p$ 根阶。普通／超奇异的导数盲区已由接受的实际证明处理 |
| V2：全部 $\mathbf F_p$ 好点的首次阶与全部迭代 | 旧[PF]21–31行和[OLD]§2已有 $N_p=0\iff p\nmid d,\ i_d>1$；原闭有限群点阶 $d$、$d\mid n$ 的交点支持、素于 $p$ 倍保持正交数均扣除；旧[FIX]/[OLD]已给全好纤维equalizer | 本轮准确供应 $c_*=i_d$：$p\mid d$ 时 $1+\mathbf1_{q=0}$；其余两支为 $1$ 或 $2+\mathbf1_{H=0}$。由已求 $e_*=\operatorname{ord}A\in\{0,1,2\}$ 初始化全部倍数，实际包括 $p\mid d$、超奇异、好点 $q=0$ 及 $p=5,d=10$ |
| V3：全部有限节点的初始阶、唯一二阶例外与全部迭代 | [FP]78–101行已有正规化、指定乘法元素及有限域点阶；[FIX]/[OLD]已有节点完成理想 $z^{i_n}(\xi,\eta)$、无回返时约化孤立节点和正厚度时长度一嵌入部分；Tate与乘法传播不算新方法 | 固定原 $T$ 而非任意两参数形变，实际一阶系数 $d(2w+1)/(w(4w-3)^3)$；其唯一消失为 $p>5,(T,h_*)=(3/16,-2)$，且二阶系数 $-3d/3125\ne0$。原 $h$ 无分歧和带点符号使其确实成为原 $i_n$，在一般代数闭 $p>3$ 域覆盖全部有限节点 |

V2 的全倍数公式

$$
i_n=0\ (d\nmid n),\qquad
i_n=p^ac_*+e_*\frac{p^a-1}{p-1},\quad a=v_p(n/d)\ (d\mid n)
$$

不是新的一般传播定理；[SYN]176–200行及[DIS]§4已明确消费并扣除 Naskręcki Lemma 8.2。
V3 的 $p^a$ 倍传播和把准确 $i_n$ 代入旧理想，也不另计结构创新。
本件没有重新核对该外文原件；此处只核定当前候选已经怎样扣除标准输入，外部直接先例核验仍由本轮来源阶段承担。

准确 $d$ 保留为闭有限椭圆群的输入是诚实范围，并非将未知局部长度藏在答案里。
但不得把“已求初始交数”说成已求全素数统一点阶闭式、全几何挠化位置或扩域统计。
旧F5全部20参数和三个二阶接触已在[OLD]§4接受，有限证书本身也不能再计新。

## 3. 与真实最接近论文的对象比较

### 3.1 Paper30：共同几何基础，但不是同一个厚度问题

本人读实际接受 V4 的引言全文、闭纤维/Hasse节全文、有限临界代数和首层理想相关完整陈述/证明。
三个看似接近的对象须分别处理：

| 实际对象 | 原输入与输出 | 与当前 V1–V3 的关系 |
|---|---|---|
| Paper30 的相对临界概形 $Z_W$ | [P30-S]27–109行：$(F_u,F_v)$，代数 $k[s]/((T-s^2)^2-\varepsilon Ts)$，长度四并保留坏能级作用 | 这是曲线族的奇点/临界结构，不是指定 $nP$ 与 $O$ 的接触除子；没有变量 $n$ 或原 $P$ 的局部回返阶 |
| Paper30 的原圆分垂直临界理想 $C_a=\mathfrak c(p^{-a}d_{\rm state}I_{mp^a})$ | [P30-I]72–170行：混合特征圆分基 $\pi_a$，两个状态系数；首层 $(\pi_1,\widetilde H_p)$，高层只断言模 $\pi_a^2$ 的完整首jet | 它不是 $\operatorname{Fix}(F_T^n)$ 的equalizer。当前原 $z=h-h_*$ 厚度不解旧 $C_a$ 的高阶 $\pi_a$ 系数，也不升级其截断商为全商 |
| 当前原固定点理想 | [FIX]14–20、62–70、141–158行和[OLD]§3：好点 $(z^{i_n})$；节点 $z^{i_n}(\xi,\eta)$ | 结构形状在本轮之前已接受；当前只把此前未知的标量 $i_n$ 准确求值并代入，不能再宣称首次获得完整固定理想 |

Paper30 对 Hasse 根阶的处理还有一个直接可核的区别：[P30-I]103–104、129–131、169–170行明确将 $e_h$ 作为根重数输入；[P30-F]346–389行的完整理想证明只把
$H_p=(J-h)^{e_h}V$ 代入，没有求出 $e_h$ 是1还是2。
[P30-H]147–174行证明几何超奇异充要性并明确不假设简单根，未给当前准确零阶分类。
因此当前 V1 的 Hasse 零阶不是重抄这个旧输入。
它在匹配模型、微分规范与能级后可以给旧公式补数值，但不能未经这些接口核定，就宣称已扩张到任意非自治回返、全部小特征或原混合特征完整厚度。

### 3.2 Paper18：一般 Fitting 基变换已知，具体理想不同

P18本身也并非只有简单点集：[P18]373–408行的 universal ordered-loop 代数代表原 Hénon 完整固定点概形，有限自由秩为 $d^n$；442–461、488–505行保留任意参数特殊化后的非约化结构、低周期和碰撞。
这是应扣除的完整概形基线，但不是其下述标记迹分歧理想，也不计算当前原 qPI 的逐基点交数。
[P18]193–235行把对象限定在复数上的 simple-exact-disjoint 标记 Hénon incidence；588–616行的
$\operatorname{Fitt}_0\Omega_{\mathcal C/(\mathbb A^1\times\mathbb A^r)}$ 是标记迹坐标映射 $\Psi=(-b,\rho_1,\ldots,\rho_r)$ 的分歧理想。
其任意基变换和完整幂零保留由1055–1152行给出，泛边界分量重数由1228–1293行保留。
它没有原 qPI 截面 $P$、$h$ 向交数或全部 $p>3$ 初始阶；1470–1487行更明确不作正特征扩展。
所以一般 minor/微分基变换、完成与长度规则必须扣除，但不能以共同出现 Fitting 一词就把当前准确 $c_*,e_*$ 或节点首项归入 P18。
P18 的 $\operatorname{Fitt}_0$ 也不是当前旧节点结构中 $\operatorname{Fitt}_1\Omega_{\mathcal U/C}$ 的同一模。

### 3.3 Paper29 与 Paper11：不能把旧完整概形或计数消费者再算一次

[P29-O]167–236行确实已经有真正的 Hénon fixed equalizer
$J_N=(X_N-X_0,X_{N-1}-X_{-1})$，以及含全部幂零的总长度 $\delta^n$；不能声称组合内此前只有点集。
但其特征零对象是多项式 Hénon 复合，[P29-P]87–166行的消费者是足够长单个周期概形上的 coboundary 检测；[P29-E]113–168行给有效周期和整个检测代数长度。
它不提供原 qPI 固定 $T$ 的截面接触初始化，也没有椭圆/节点两分支的全部倍数局部阶。
“保留幂零”“完整固定概形”不是本轮独有的方法标签；本轮具体交数分类在该实际定理范围内未被吸收。

[P11]404–516行的一般有限阿贝尔群平移定理，已经给周期 $d_K$、循环数与形式zeta乘积。
加上旧[FP]的原状态、真实群及指定点识别，普通有限域循环求和是旧消费者。
该有限集合定理没有随原 $h$ 的无穷小参数，因而不决定 $(nP.O)_{h_*}$；当前也不应为新意添加一套重复循环/zeta章节。
不建立任何 Hénon/cat 到 qPI 的新跨族桥；此类想法只可记 `ROUND2_CLUE`，本件没有提出或启动它们。

## 4. 旧 I03 是先前的问题，不是先前的解答

本人直接读[IDEA]144–163及295–310行：旧 **P30-POSTV2-I03** 已明确提出原 $D_{n,T}=O^*([n]P)$、全阶好纤维异常三元组 $(h,d,i)$ 及实际固定概形实现。
它当时先取特征零、全部 $T\ne0,n\ge1$，粗筛保留方向B，并要求超出低阶除法多项式枚举与一般有限性/界。
所以“第一次提出研究原截面接触”“第一次区分 $dI$ 与 $nP$”没有新意。
但旧问题的存在不是旧定理的存在；该直接原文没有证明当前准确 $c_*$、forcing阶或节点例外。

当前实际回答了同一原问题的明确实质部分：全部素域好点的全部迭代初始化，以及一般代数闭正特征全部有限节点；另给特征零真实好切触的准确2/3条件阶与有限阶节点横截。
它**没有**求出旧特征零 I03 的全部真实异常能级/点阶三元组，也没有全局精确阶存在谱。
不得据此宣布 I03 全部关闭；同样，不能把未解决的旧更大量词自动添作当前已锁定三主张的新增硬条件。
本 I03 不是后来的 P31-I03 尖点，也不是 POST_CLOSED-N03 的 $q$ 方向形变；这三者不能合并账面状态。

## 5. 单一中心与必须保持的边界

V1 是原好点初始化的实际供给，V2补齐素域的 $p$-primary 分支并消费旧支持和传播，V3对同一原切片的节点补齐初始化；三个部分都回答“旧固定理想中的 $i_n$ 究竟是多少”。
它们保持同一 $W_h,P,T,z$，不是拼接不同构造的最好结果。节点代入
$H=w(2w+1)(4w-3)^2$ 将二阶节点例外和同一 forcing 因子联系起来；该简单一致性不另记第四项创新，也不构成新的一般退化理论。
因此从本地非碰撞角度看，有一个凝聚的原问题和真实净增量，可作为整体交给后续正式评价；本件不把“中心凝聚”升级为独立价值7.5、22–30页容量或准入通过。

- V2只对全部素域好点充分，不是所有有限扩域、任意闭点度数或全部几何好点的全迭代分类。
- V1正特征真实好切触断言保留 $p\nmid n$；$N_p$ 的一般代数根不能反推真实切触。
- V3保留任意代数闭 $k$、全部有限节点，不缩到素域；非根单位时没有回返，特征5所列例外为尖点而非节点。
- 三阶好切触条件不证明实际三阶实例存在。节点例外在 $p>5$ 的有限阶回返与此不同，不应混作同一存在性风险。
- 尖点、无穷、$T=0$、一般非自治原torsor上的全相对作用、全部几何异常位置及跨域点阶分布仍不在完整分类内。
- 最大外部风险仍是固定 $b=T$ 的有标点 Tate/Lyness 切片是否已经有同一准确分类。本地净增量不排除外部直接先例；本件没有读取并发Phase B或未来C/D来校准结论。

## 6. 本人实读、身份及执行边界

下表 SHA-256 绑定实际整个文件；PARTIAL 只表示列出的本人实读段落，不继承报告所列上游全文、外文或CAS身份。
数次合并读取发生输出截断，缺失段落已经分开补读；关键词命中不当全文。

| 输入 | 本人实读范围／文件总行数 | 实际 SHA-256 |
|---|---|---|
| [A] | FULL 1–157 | `171e8aa602d6431e76672c79cf6962c9269f73a6f91993ef7c131a697a4ac917` |
| [SYN] | FULL 1–245 | `5400ed2775b3a91f85c814d9c8c8fb252dc91cf8577579f63da0cee87e7539d1` |
| [DIS] | FULL 1–234 | `5340f77faa1354b1239240e3d7ba7068ae32e752e6d4550e32b2f243ea08bc99` |
| [CR] | FULL 1–207 | `2023cc2066002009b46bb5d95bb6eb6333994cee1f707e908e2faf4f2e1b0c60` |
| [PORT] | FULL 1–121 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [MAP] | FULL 1–107 | `b7271644adec9357cde8e33d1c0b437d94bf4e72944b3b74c338a0458b1e6977` |
| [OLD] | FULL 1–176 | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |
| [M] | PARTIAL 1–123、335–390／446 | `48029bd31748637edaa6a9a123cd0d525406ea5b65f7eab53799606a5c97dbe2` |
| [MA] | PARTIAL 1–102／148 | `05a99ecd5cfd72315b8c4e0fc740062687824d4dcd8dc7cdcdb81f5f87bbb8fd` |
| [PF] | PARTIAL 1–78／325；另关键词定位 | `de9cdb5ee8fef26b50365e6794e148f7206c4c167738143fc28e77159b0debef` |
| [FIX] | PARTIAL 1–160／348 | `401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7` |
| [FP] | PARTIAL 1–125／167 | `9a70cd2dd9656689dfeb26a6890e35ab1bf5dd10a5eab28a38306578b2767fce` |
| [IDEA] | PARTIAL 130–170、290–310／339 | `e10bd508ff98acd6ed25fc01f05ccdace2f6efeab173d5aadb1fa6f2e7068aca` |
| [P30-I] | FULL 1–300 | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| [P30-S] | PARTIAL 1–146／438 | `38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f` |
| [P30-H] | FULL 1–271 | `68efcc6780280d7e06c107bc993fe4c431d8131b59f1f4f9e6b874dd96c6000e` |
| [P30-F] | PARTIAL 340–393／397 | `e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392` |
| [P11] | PARTIAL 390–518／1238 | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` |
| [P18] | PARTIAL 188–251、373–408、442–461、488–505、507–616、1055–1152、1228–1293、1470–1487／1602 | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |
| [P29-O] | PARTIAL 13–31、167–236／236 | `a36bebf59d412cc72ba52b38eb38da5f65cda0d0e79500642a7599004cb9520f` |
| [P29-P] | PARTIAL 80–166／166 | `862d363763a2a0dc3491903539ff0f5b0c75df7c8aed56f4c5af9d10eb4e21a8` |
| [P29-E] | PARTIAL 111–168／353 | `fccfef37b05fafaff300a2f9a84f4796ca2ef902f365133c5069f459c89c271e` |

另本人读 `docs/WORKFLOW.md` FULL、`BATCH_07_CONTEXT.md`1–55及 README 的当前入口和成果索引；P29项目README1–22用于定位接受的successor源，不把旧稿误作当前接受稿。
只读辅助席 `p18_p29_boundary_check` 独立定位并比较P18/P29，未写文件；本席随后本人读完上表准确段落并计算实际哈希，不继承辅助的额外阅读范围或另计一票。
使用 novelty-check 的主张／旧方法／finding分列纪律完成受托本地部分；未越权启动该技能完整外部B/C/D流程，也未使用未配置的MCP或声称跨模型。
数学接受身份按[DIS]/[OLD]/[MA]消费，本件未重新表决新证明、未复跑F5/CAS、未引用未读外文为新证据。
唯一写入为本文件，使用 `apply_patch`；不修改冻结Phase A、作者稿、旧失败、接受、锁、README、批次入口或既有论文产物。
无项目建立、试写测页、编译、GPU、联网检索、投稿、上传、发信或其他外部效力。终态读回并报告实际文件哈希，不把本地非碰撞当作Paper31完成。

[A]: PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_A_V1_20260912.md
[SYN]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md
[DIS]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md
[CR]: PAPER31_QPI_EXACT_THICKNESS_INCREMENT_CRITIQUE_V1_20260912.md
[PORT]: PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
[MAP]: PAPER31_QPI_NEW_INPUT_LOCAL_COLLISION_MAP_V1_20260912.md
[OLD]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[MA]: PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[FP]: PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md
[IDEA]: PAPER30_QPI_POSTV2_IDEATION_V1_20260909.md
[P30-I]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex
[P30-S]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex
[P30-H]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/04-closed-hasse.tex
[P30-F]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/06-first-layer.tex
[P11]: ../../papers/11-cat-equivariant-clock/paper/manuscript.tex
[P18]: ../../papers/18-marked-henon-scalar-boundary/paper/main.tex
[P29-O]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/2_orbit_algebras.tex
[P29-P]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/5_periodic_detection.tex
[P29-E]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/6_effective_periods.tex
