# Paper31：闭合候选之后 N07–N10 定向首筛 V1

日期：2026-09-10 UTC。执行席：`/root/p31_qpi_novelty_cd_i08_v1`。
状态：`PHASE3_FIRST_PASS_ONLY / NO_NEW_MATHEMATICS / NO_FORMAL_VOTE / NO_CANDIDATE_ADMISSION`。
`route_applicability: NOT_APPLICABLE`。只筛指定四题，不重新生成题目，不评正文容量。

## 1. 结论先行：当前投入建议，而非四项定理处置

| 题目 | 首筛建议 | 可行性／标准短推论风险 | So what 与当前决定 |
|---|---|---|---|
| N07：原末端覆盖的野模型 | `HOLD_UNRESOLVED`；三阶支 `STOP_SHORT_STANDARD` | 原递推可用；全素数分支类型未供给。短推论风险 HIGH | Zapponi 已直接处理度 p 非 Galois 多项式覆盖及可分尾；只重做三阶 Dickson 野缩放不足。未有原全 p 非标准机制，暂不进深核队列 |
| N08：增长截断与点阶尾界 | `HOLD_UNRESOLVED`，不作为当前幸存新方向 | 标准工具可行，独立价值风险 HIGH | 满像以后是固定行列式的有效概率消费者。真实目标未证，但“还缺尾界”不能自动算新机制；先有非短差额才值得深核 |
| N09：双能级共同塔 | `STOP_SHORT_STANDARD_CURRENT_FORM` | 独立性论证的投入门槛低；短推论风险 VERY_HIGH | 普通乘积像与概率相乘的叙事停止。未见已证明的原例外／新共同商；本判断不等于已经证明所有 δ 的全层仿射乘积像 |
| N10：状态临界阶与周期提升过滤 | `KEEP_FOR_DEEP_CHECK`，仅保留准确的原过滤桥 | 原模型与点可用；整数坐标比较未核，技术风险 HIGH | 有可能解释 P30 数据究竟保留多少动力信息；形式群估值、AGR 或域上平移本身都不够。保留不等于新意、可行性或论文准入通过 |

四项均为纯理论任务，预计 GPU 用量为 **0 GPU-hours**；本轮也没有 CPU 数学实验、有限域枚举、CAS 或证明诊断。
没有为了凑幸存数量把 N07/N08 的未决状态改成新意肯定。N09 的止投限于当前普通独立性中心，不声称相关问题已被全球解决。
若后续 N10 的整过滤比较只是一般逆函数／单位换元的短消费者，同样应停止，不以既有篇幅或第五篇目标补价值。

## 2. 阅读身份、权限与基线

采用本人已 FULL 读取的 `idea-creator` **Phase 3**：每题三条定向查询、可行性和 So what 首筛；`research-lit` 用于一手来源与阅读深度标注。
不执行该技能的另一次 Phase 1/2、Phase 4 正式查新／评分、Phase 5 pilot 或默认 `IDEA_REPORT.md` 写入。
本人另 FULL 读取 AGENTS.md、WORKFLOW。委派范围优先于技能默认流水线，不触发 Route A/B。
本席先前参与 I08 C/D 核查、后续非单位链的非作者检查，并撰写过 Fitting 来源补充；不是零接触盲审，也不是跨模型验证。
本轮不重用旧票作为新票，不重开已经接受的 Kummer 数学或完整 C1–C3 数学。后者正式新意／价值失败保持；Batch07 仍为 4/5。

| 本地输入 | 本人本轮实际范围 | SHA-256 |
|---|---|---|
| [新基线][BASE] | FULL 1–210；首次合并输出截断，随后 1–110、111–210 分段完整读回 | `6c24c6cab58c899ef90f2369cb1bd83c8ff3de8668b77119351b684ac3df115e` |
| [冻结十题][IDEAS] | PARTIAL 1–37、103–233：共同扣除、N07–N10 全条目、关系边界、来源声明与引用；含 N06 邻接段，不称十题全文 FULL | `b18e8cea87cb85355628f738eaf2fe69e44b0c5b4e1f564bcaf08228c071999f` |
| [Kummer接受][KUM] | FULL 1–50 | `9db1f21b39b8e8df664fb27bd434fd02aed04b206ace4873de9834ff77d044e4` |
| [Kummer作者件][KA] | PARTIAL 1–78；另定向 Chebotarev／来源关键词命中 | `d297f6219bbd0e17062cf6f20e245c96f37e0f54ba84cc834990e56ec3154b38` |
| [原多截面][MULTI] | PARTIAL 55–158；含原递推、三阶全式、分支与最小性原范围、标准包含段 | `9e6a7f2f732c79f3a7d5a32e15d52da541adbb03f845c44572a775cf9f13bfb3` |
| [P30接受稿引言][INTRO] | PARTIAL 20–184；原映射、完整状态模型、标准化状态微分与首层／高层首 jet 陈述 | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| [P30接受稿首层][FIRST] | PARTIAL 380–398；另定向关键词命中，未重审首层证明 | `e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392` |
| [旧 I08 C/D][OLD8] | 本轮仅定向关键词／末尾来源地址命中；本人旧 FULL 身份不冒充本轮新读 | `88e9480fb14353836831af4a628cb319145e2ea46b6e6fc0c17c0a7c00a19946` |

共同扣除包括 P27–30 的完整曲面、原能量／Jacobian／指定回返点与有限域周期清单，P30 全首层完整理想和全高度首 jet，及已接受整层 Kummer 像和正确有限层商类。
N07 不能传给 N06 “覆盖无根所以全曲线无点”；N08 不解除 I10 跨素数密度失败；N09 不把同一算术行列式称作新相关；N10 不重投 I01 固定下降、也不以假截面解除 I09。

## 3. 实际查询账本：每题恰三条

以下为本轮公开 WebSearch 实际提交的字串，日期均为本件日期；引号是查询的一部分。随后打开命中／引用的一手页面不另充作新查询。

| 编号 | 实际 query | 可用命中与筛除 |
|---|---|---|
| N07-Q1 | `Dickson polynomial degree p stable reduction wildly ramified cover mixed characteristic` | Zapponi、野覆盖来源；不以混合的百科命中作数学证据 |
| N07-Q2 | `"Chebyshev" "stable reduction" cover` | Dickson/dihedral 入口与覆盖文献；不是原全 p 的包含定理 |
| N07-Q3 | `"polynomial covers" "degree p" "reduction" Lehr` | 直接命中 Zapponi 一手期刊 PDF／arXiv 元数据 |
| N08-Q1 | `elliptic curve family finite fields Kummer point order distribution effective Chebotarev l-adic` | 分点塔及显式 Kummer；数域有效像结果不代原有限域族统计 |
| N08-Q2 | `"Galois theory of iterated endomorphisms" point order density` | Jones–Rouse 一手 arXiv／作者 PDF |
| N08-Q3 | `"Chebotarev" "finite fields" "genus" effective cover Kowalski` | 有效覆盖计数入口；另从本人旧来源地址直接读回 Hall–Voloch／Gekeler 强碰撞 |
| N09-Q1 | `"Goursat" "elliptic" "ramification" independence` | 结果较散；没有据此宣称原双塔无先例 |
| N09-Q2 | `"Kummer" "independence" "function fields" elliptic` | 命中乘法群 Kummer 独立性；该对象不是两条椭圆曲线的仿射塔，不直接套用 |
| N09-Q3 | `"monodromy" "shifts" "Goursat" elliptic` | Kowalski 作者报告给平移层的 Goursat–Kolchin–Ribet 机制；另有相关论文入口，但未获可核完整相关定理 |
| N10-Q1 | `"p-adic" "periodic points" "smooth" "Hutz"` | 零散相关命中；本轮未取得 Hutz 的直接适用定理，不据空缺授新意 |
| N10-Q2 | `elliptic curve "formal group" "period" "modulo" prime powers dynamics` | Bhakta 等正式论文：明确群过滤、点阶定义、估值与 EDS 周期 |
| N10-Q3 | `"QRT" "p-adic" dynamics reduction` | Kanki 原论文；转到 SIGMA 官方卷目录再打开正式 PDF |

已核可用工具中没有 Zotero／Obsidian；本地仅做相关 PDF／文本文件名筛选，命中的是 P30 构建产物而非外文库，没有读取旧 build 树内容。
未找到 `tools/` 或所装 research-lit/arxiv 目录中的 `arxiv_fetch.py`，使用网页 arXiv 入口；未下载 PDF 到工作区。
综述、聚合页、搜索片段只作发现；下列数学比较以本人打开的一手内容为准，不将搜索无命中转成“首次”。

## 4. 一手来源：真正读到什么

| 来源、身份 | 本轮实读深度 | 能用于哪一种包含判断 |
|---|---|---|
| [Z] Leonardo Zapponi，*Specialization of polynomial covers of prime degree*，Pacific J. Math. 214(1), 2004 | PARTIAL：印刷 pp.161–167 的对象／正规化与 Lemma 4.1；pp.169–170 的 Definition 6.1 与完整 Theorem 7.1；pp.174–176 的完整 Theorem 8.1、8.3 及邻接陈述。未 FULL 阅读所有证明或模型图 | 直接同属度 p 非 Galois 多项式覆盖；simple reduction、允许扩域和覆盖等价必须保留，正规闭包的具体完整模型没有被这次阅读代签 |
| [JR] Rafe Jones–Jeremy Rouse，*Galois theory of iterated endomorphisms*，arXiv v4／PLMS 2010 | PARTIAL：原塔表示定义、Proposition 3.1、Theorem 3.2 及完整证明（PDF pp.7–11，文本347–543）；Theorem 5.5 仅定向声明 | 已有指定点素于 ℓ 阶的分点树概率与坏事件尾机制；不是原固定 Q 陪集下全点阶分布的即成公式 |
| [HV] Chris Hall–José Felipe Voloch，*Towards Lang-Trotter for Elliptic Curves over Function Fields*，2006 来源记录／公开作者稿 | PARTIAL：引言、§2.1 至 Corollary 1 的声明与相关论证；§4.1–4.2 全部（含 Lemma 5、Theorems 5–6），以及 §4.3 增长截断起始。期刊卷页本轮未另核 | tame 亏格的线性度数界、真实常数域 Frobenius 陪集与有效误差已经标准；主定理的秩至少六及变素数尾不直接包含本题 |
| [G] Ernst-Ulrich Gekeler，*The Distribution of Group Structures on Elliptic Curves over Finite Prime Fields*，Documenta Math. 11 (2006),119–142 | PARTIAL：元数据／引言，§2 定义、Theorem 2.3 全部声明、2.4–2.11 的有限层／矩阵分类段；非全证明审计 | 矩阵余核分布及条件 `vℓ(det A−1)=r` 已算；该条件不是固定 `det A=Q`，不能不经比较偷换 |
| [KS] E. Kowalski（与 W. Sawin 联合工作），*The shape of exponential sums*，2015-05 作者报告 | PARTIAL：题页和 PDF pp.44–48 的平移 Kloosterman 层定理／解释；这是作者 slides，不是本席已核全部证明的期刊定理 | “各投影 SL₂ 满像＋排除秩一扭曲＋Goursat–Kolchin–Ribet”是明确先例。其线性代数单值群不等于原全部有限层仿射群 |
| [B] Subham Bhakta、Daniel Loughran、Simon L. Rydin Myerson、Masahiro Nakahara，*The elliptic sieve and Brauer groups*，PLMS126(6),1884–1922，2023 | PARTIAL：官方元数据；完整 §2（Definitions2.1–2.2、Lemmas2.3–2.4 与证明、Remark2.5）；§3.3 的周期开头与 Proposition3.7 上下文，非整篇 | Néron式群过滤、点阶和乘法估值是旧机制；这里明确底域 Q_p。EDS 周期上界不是原状态精确最小周期 |
| [K] Masataka Kanki，*Integrability of Discrete Equations Modulo a Prime*，SIGMA9 (2013),056 | PARTIAL：元数据／引言；§2 至 Proposition2.2；另定位 §3 的 qPIII／qPIV 范围，不审全部计算 | AGR 允许随点／时间改变迭代次数，弱于每步良约化；并非 qPI 原完整有限环可逆回返的认证，更没有 P30 临界阶桥 |

本轮额外打开过 Kowalski *Geometric Bunyakowsky Problem* 的入口及定向 Proposition 定位，但未采用其定理；没有据该标题扩大本题结论。
另一联合单值群论文的 Durham 入口返回 403；普通 DOI 转到出版商标题页，后续定向正文定位未成功，故不作为已读定理证据。没有绕过访问限制。
Kanki 的聚合 PDF 入口失败后，经正常 SIGMA 官网取得上表正式稿。两个作者目录入口也未成功，不据此推测其内容。
一个猜测的 P30 节文件名不存在；随后仅列当前 v4 的 sections 并从已存在的引言／首层指定段核准，没有扩扫历史构建。

## 5. N07：标准野覆盖已直撞，全 p 的原差额尚未定位

原对象保持为 $\mathcal O=W(k)[\zeta_p]$ 上单位 t 给出的 $c=b_p(w)$，不是任意可以更换的分裂覆盖。
[MULTI] 已给三阶 $b_3=-w^3+3tw-3t$、两有限分支及六次根式正规闭包；原特征零泛函数域的最小度数已扣除。

[Z] 的对象就是混合特征度 p、在无穷远全分歧的多项式覆盖，**不要求 Galois**。
其 simple reduction 指分支稳定模型的每条非原尾恰承载两个分支点；分支总数至多四时自动满足。
Theorems7.1、8.1/8.3 已明确产生纯不可分原分量与剩余可分尾，并按距离／分歧数据给厚度。因此“找到首个非 Frobenius 野尺度或可分尾”本身不能作为新中心。[Zapponi][Z]

准确对象映射只到：原 $b_p$ 是 degree-p polynomial cover、无穷远全分歧；三阶已知三分支进入上述标准覆盖范围。
但对原全部奇 p、全部允许单位 t，尚未从已接受递推取得 simple reduction 的全称判断；更未核原正规闭包每个分量与有限剩余域下降数据。
Zapponi 的源／目标 PGL₂(K) 等价及允许有限扩域会改变坐标表达；用于比较模型类型时必须回记原 c 标签，不能把归一化结果直接说成原能量像。
本件没有计算新的分支聚集或缩放，没有从“全 p 还没匹配”反推新意。

可行性：三阶材料足够作短核对，但它已无独立增量；原全 p 工作预计数周至数月，最大缺口是尚未陈述的非标准递推结构，不是计算设备。
So what：若只是将原递推输入标准分类，科研价值是准确接口；只有超出已知类型或给出实质统一原分类才可能改变理解，目前未供给。
建议：三阶支 `STOP_SHORT_STANDARD`，整题 `HOLD_UNRESOLVED`；不凭换 p=5,7 加样本续投，不从根域不同式推出所有曲线分裂域中的最优性。

## 6. N08：有效化的机制已成熟，不能混用两个不同尾事件

沿 $Q=q_0^a$ 的原光滑能级计 $v_\ell\operatorname{ord}(P_h)$；[KUM] 的整塔满像与有限层商类可直接消费，不再证明。
目标模型保留 `det A=Q`，亦保留除外的 $T,p,\ell$。没有选定行列式的 ℓ-adic 极限子序列时，不声称存在一个与 Q 无关的极限分布。

[HV] Lemma5 的 tame 亏格界及 Theorem6 的共轭事件有效陪集计数提供现成架构：误差显式含事件大小平方根和 $Q^{1/2}$，隐常数按其 §4.1 受底曲线／分支支撑等控制。
这是当前最强的“增长层截断可能只是标准消费者”压力。原有限层需要的 tame／分支与明确常数仍须实际核准；本件未计算它们，尤其不以 $p\nmid\ell$ 单独推出整个覆盖 tame。[Hall–Voloch][HV]

[JR] Theorem3.2 证明中得到的 $m/\ell^n$ 尾，针对同时“仿射作用有不动点”且 $\det(A-I)=0\bmod\ell^n$ 的坏事件；利用的是给定线性部分时平移落入像的比例。
N08 所需 $v_\ell\#E_h\ge n$ 是整个线性行列式尾，**没有上述仿射不动点条件**；不能把该不等式原样搬来宣称群阶尾已证。[Jones–Rouse][JR]

[G] 已算 $\operatorname{coker}(A-I)$ 的 ℓ-primary 群结构，并按 $v_\ell(\det A-1)$ 条件分组。
它与“精确固定 $\det A=Q$”并非同一条件。即便最终可由短提升计数联系，也须交出映射与统一界；“看起来只依赖 $v_\ell(Q-1)$”还不是本轮证明。[Gekeler][G]

可行性：原覆盖输入已足，3–7 天有界纸面包含核对合理；精确常数、均匀尾和平衡全套约数周，尚无保证。0 GPU，不需要全层有限域枚举。
So what：一个 ℓ 的部分点阶分布可补原周期信息，但不是完整周期分布；单一固定族满像后主项主要由通用群决定，独立价值仍弱。
建议 `HOLD_UNRESOLVED`，不是 `KEEP`：尚无直接已证全目标，也尚无超越通用计数的原科学差额。只得固定层公式或把尾藏在常数里均不足；若完整目标是短标准平衡，应保存接口并停止长文中心。

## 7. N09：普通联合独立性中心止投，不冒称原整塔已被外文直接包含

原两因子是 $E_{T,h},P_h$ 和 $E_{T,h+\delta},P_{h+\delta}$，不是同一椭圆曲线上两个任意点；两投影满像已接受。
[KA] 已给四个互异有限坏值、各 $I_1$，以及无穷远 $I_8$ 和完整惯性根群。这些输入不能重新作为新发现计功。

[KS] 明确展示了平移层各有 SL₂ 像、排除秩一扭曲后由 Goursat–Kolchin–Ribet 得乘积单值群的机制。
因此“单塔满像但尚未算联合像”只是一项逻辑剩余，不能自动成为独立研究中心。[Kowalski–Sawin 作者报告][KS]
本轮还读到 [HV] Theorem2/Corollary1 的同一 E 上分点域交／多点独立性陈述；它的共同线性表示是同一 E，不能直接代本题两条移位 E 的比较。[Hall–Voloch][HV]

原对象仍要核的准确步骤是：分支集合平移后排除可导致共同商的情形；某处一侧惯性非平凡而另一侧无分歧时，核准它在相关共同商中的像；最后处理整个有限层仿射平移核及其兼容。
不同分支、分支相交或两个单投影满像，各自都不自动给最后结论。线性 ℓ-adic 代数群直积也不能无证明升级为每层有限仿射群直积。
本轮没有执行这些原对象证明，因此没有“所有非零 δ 均独立”的新数学接受。
但目前没有提供任何确实存在的原例外、同源对应或非平凡共同商；只要普通惯性／Goursat 检验即可结束，联合分布主项相乘也只是其消费者。

可行性：上述反对意见核对可在3–5天内尝试，原输入可用；若真出现例外再估量分类，而不是先预算一篇例外论文。
So what：真正的原相关机制可能有价值，增加第二个能级或同 det Q 的必然约束没有独立价值。
建议 `STOP_SHORT_STANDARD_CURRENT_FORM`：停止以普通乘积像为论文中心。该投资判断基于明确标准压力与尚无非平凡目标差额，不假装已获得外文对原整塔的一步包含定理。
只有实际发现而非预想的原共同商／例外，才是另行考虑的科学证据；本件不授权为救此题改变系统族、时间或 δ 的原分类目标。

## 8. N10：仅保留原过滤比较；一般估值与 AGR 均不足

锁定单位时间、完整圆分环和真实 $z\in\mathcal U(\mathcal O_a)$；$c=I_r(z)$ 已有原点，不能改成寻找无点曲线的问题。
[INTRO] 固定的是原两个状态方向的 $\alpha=p^{-a}d_{\rm state}I_r$ 与系数理想；[FIRST] 已给首层无分歧状态的阶结论。
这些已接受数据不能换成谱坐标下一个任意选择的导数，也不能未经比较叫作原回返形式群深度。

[B] §2 已以 $E_i$ 定义点阶模 $p^i$，并给局部坐标与点估值、乘法估值的标准关系；其明写底域为 Q_p，不能略去额外分歧就套到任意 $\mathcal O_a$。
§3.3 的 EDS 周期性也是先例，但数列周期上界既不是原 $\Psi$ 的最小状态周期，也未给原状态坐标与群过滤的比较。[Bhakta 等][B]
[K] 的 AGR 只要求某个依赖点／时间的迭代与模 p 约化相容，且覆盖的是其指定 QRT／qPIII／qPIV 等映射。
它不是每个 N 上原完整 $\mathcal U(\mathcal O_a/\pi^N)$ 的可逆自映射，更不保证每个点有最小正周期或给出临界阶预测公式。[Kanki][K]

准确待核差额只有三项：

1. 原 $\Psi$ 在使用的整数模型及有限商上的定义／逆映射与轨道稳定范围；完整域曲线上平移的身份不足以代签。
2. 同一原状态邻域至好约化 Jacobian／Néron 邻域的整映射及逆映射、允许阈值和过滤深度损失；微分系数的阶不自动控制所有较浅层高阶项。
3. 在固定原时间、同样候选临界数据与标记能级数据下，深度损失是否真的由这些数据决定；正面给正确比较式，负面给同对象下的实际不足性，而不是更换普通／超奇异标签。

可行性：1–2周有界原对象核对合理；当前尚未供给桥，不能估成已可完成的一篇论文。无数据集／GPU障碍，难点是整数模型和同余过滤本身。
So what：若桥确有非标准损失，或能证明原临界阶遗漏决定周期提升的信息，会给 P30 一个真实动力消费者；若只是一般形式群递推与单位换元，则没有独立长文中心。
建议 `KEEP_FOR_DEEP_CHECK` 仅限这项判别问题。后续深核首先应主动寻找最短标准包含，不重做形式群理论，不将“存在足够深盘”包装成锐原公式。
本件没有给出任何正面公式、负面反例、整回返存在定理或新数学分数。

## 9. 交付与停止边界

本件只有 Phase3 首筛；不把任何 HOLD 或 KEEP 当正式准入，不增加 P31 目录、锁、稿件、PDF，也不估22–30页容量。
唯一写入是本新文件；冻结输入、旧接受、失败、README、索引和批次入口全部不改。无外部写入、上传、投稿、付款或对外通信。
保存后本人全文读回，核本文全部直接本地引用及所列输入 SHA；终态行数、字节数和 SHA 另交主控。
本轮最值得传递的是准确包含边界，而不是“还没搜到”或把原科学缺口命名成新方法。

[BASE]: PAPER31_QPI_POST_CLOSED_BASELINE_GAPS_V1_20260910.md
[IDEAS]: PAPER31_QPI_POST_CLOSED_IDEA_GENERATION_V1_20260910.md
[KUM]: PAPER31_QPI_KUMMER_MATHEMATICS_DISPOSITION_V1_20260909.md
[KA]: PAPER31_QPI_KUMMER_FEASIBILITY_V1_20260909.md
[MULTI]: PAPER30_QPI_TORSOR_MULTISECTION_DIAGNOSTIC_V1_20260909.md
[INTRO]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex
[FIRST]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/06-first-layer.tex
[OLD8]: PAPER31_QPI_NOVELTY_CD_I08_V1_20260909.md
[Z]: https://msp.org/pjm/2004/214-1/pjm-v214-n1-p10-p.pdf
[JR]: https://arxiv.org/pdf/0706.2384v4
[HV]: https://web.ma.utexas.edu/users/voloch/Preprints/lang-trotter.pdf
[G]: https://ems.press/content/serial-article-files/25986?nt=1
[KS]: https://people.math.ethz.ch/~kowalski/katz-conference.pdf
[B]: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.12520
[K]: https://sigma-journal.com/2013/056/sigma13-056.pdf
