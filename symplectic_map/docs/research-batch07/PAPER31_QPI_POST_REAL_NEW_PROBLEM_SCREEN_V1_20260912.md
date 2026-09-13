# Paper31：全实正式双 FAIL 后的新问题与来源初筛 V1

日期：2026-09-12 UTC；主控 `/root`；本地有界研究，不是候选准入。
起点是 [FD] 的完整正式双 FAIL：两席新意7.2，其它三门通过；原证明接受保持。
本件记录12项具体问题、实际公开检索和纸面短解压力，不把同一全实表换名补分。
已落实的新数学试探另存 [BM] 与 [OD]；其独查和最终接受状态由后续处置给出。

## 1. 方法、权限与实际输入

采用 idea-creator 的景观、8–12项生成和初筛；research-lit／novelty-check 用于具体包含检索，
ARS 只选 fact-check 路径；proof-writer 用于明确新证明及其边界。没有启动完整研究到论文流水线。
纯理论工作跳过 GPU pilot；没有训练、数值、CAS、N 扫描、PDF下载落盘或对外效力。
不可用的指定 Codex MCP／Zotero 等接口不作已使用；使用可用 secondary Codex，不声称跨模型。
研究对象、批次顺序和完整准入要求已明确，不重开交互式选题、不要求用户重确认已有授权。

主控本轮 FULL 读当前 WORKFLOW、[FD]；背景 propose-symplectic-map.md 只读1–410行，非全文。
12问生成者 `/root/p31_post_real_new_problem_inventory` FULL 读 idea-creator、[FD]、[CB]、[S]、[PORT]，
背景只读1–83和220–247行；无网络、文件编辑或再委派。其文献背景继承旧报告，不算亲读一手正文。
查新者 `/root/p31_embedding_centralizer_source_screen` FULL 读 research-lit、novelty-check、[CB]、[PORT]，
只读 P30 当前V4指定曲面／Jacobian段和三个公共正文，另核一个近期官方摘要；无本地写入。
另一纸面代理 `/root/p31_periodic_detection_paper_test` 只核第3问的有限极点与单值化接口，不作正式票。
所有来源与数学工作均有明确文件所有权；批次论文仍串行，未建立 Paper31 项目、锁、稿件或PDF。

## 2. 先扣除的景观

固定椭圆曲线上的平移角、普遍族的 Betti 坐标及其沿纤维满秩是既有机制。
Gao 的普遍 Betti 映射就是实坐标投影，不能把本次固定 E 移动 P 的短论证包装成新一般满秩定理。[GAO]
ACZ、CDMZ、Ulmer–Urzúa、Mok–Ng 已系统处理扭值、切触和重数；它们的通用有限性／界不等于本件指定 b 的实点准确清单，
但“Betti／扭点／分歧建立联系”本身不能记作原创。[ACZ][CDMZ][UU][MN]
Pell–Betti 文献还把有理 Betti 值、指定分歧覆盖和置换表示相联；仅换成模函数语言不够形成新机制。[BCZ]

另一方面，Arreche–Babbitt 2025 已给椭圆差分求和的完整 orbital 与两项 panorbital 障碍，
且明确区分扭平移的有限迹判据和非扭平移；本题不能重新声称发明椭圆离散留数。[AB]
保铅笔的双有理对称则已有 Jacobian 平移／有限扩张框架；MW、高度和本原性需按实际曲面区分，不能混用“本原”一词。[CD]
这轮不是检索空白区：有八项主控实际读到的相关一手正文／引言和两项代理读到的一手正文，另有明确标注的综述定位。

## 3. 十二问的目标、最低试探与粗筛

时间只是理论工作量初估，不是已投入时间、执行授权或容量票；全部计算预算为0 GPU小时。
先被逻辑／独立中心条件淘汰的项不再为满足检索条数扩搜；其余才进入定向来源核查。

|号|目标命题与原动力消费者|最小试探／最强包含反对|本轮去向与风险|
|---|---|---|---|
|1|保留 terminal、两节点的完整实曲面上，F²能否是全局解析自治 Hamiltonian 时间一映射；奇次是否有障碍？|关键是跨节点单值解析时间，不是正则圆重标。DLM不直接覆盖，但相对指数映射可能短解。|有界解析接口问题；数周／中风险，不立独立长文。|
|2|原保能量铅笔双有理辛中心化子及 G^m=F 是否有非平凡有理根？|核 MW 中 P 本原、底作用；旧八边界＋高度公式已可能给3–5页短链。|降为标准结构消费者；不能冒充 b 覆盖不可分解。|
|3|极点限有限 jP 段的有理观测量，所有真实周期迹为零是否等价于泛纤维有理 coboundary，并控转移函数极点？|完整留数障碍已知；真正接口是周期特化检测两项泛余障碍。纸面检测有短单值化路线。|保留准确有限问题与未核接口，不把一般留数定理再写一遍；周级／中风险。|
|4|同一公式负T是否破坏正T的唯一 twist 驻点机制？|w=3/4给(T,h)=(-27/256,9/8)的真实 cusp，不能移植正T符号链。|只登记参数扩展线索，本轮不执行、不改正参数范围；月级／高风险。|
|5|M0、M−是否随T严格下降，M+是否严格上升，固定共振能否反复出现？|初提案要求直接求ρ_T符号；新固定E移动P已将其压成dρ≠0加边界问题。|已形成[BM]真实证明输入；不再沿用“尚缺新的积分符号机制”的旧初估。|
|6|T→1两侧驻点逃逸的双尺度率是否 h_m logT/[3log(1/abs(logT))]→1？|待证候选尺度，旧 O_T 不能直接换一致量词；主导尾积分可能短解。|伴随问题，未证该速率；本轮只证明逃逸与极值极限。|
|7|同频双圆在明确小辛kick下是否有互换稳定性的两组周期点？|标准共振正规形／Poincaré–Birkhoff已供应大部内容。|淘汰独立形式；数日级。|
|8|原坐标符号(sign x,sign y,sign(x−y))的旋转编码能否辨别同频圆？|有限轨道分割与标签合并必须核；一般旋转编码已强覆盖。|伴随诊断，淘汰目前独立形式；日到周级。|
|9|两个实节点的全部合法原轨道是否可由归一化乘法坐标分类？|已知节点群与 terminal 字典的直接消费。|淘汰独立形式；不自动开奇异轨道续篇。|
|10|固定T逐有理角能级重数及原最小周期清单？|严格表取原像＋上外F²组件因子；标准短推论。|伴随推论，不用来补旧失败包。|
|11|三个 h_m(T) 分支是否局部实解析？|ρ_hh非零直接IFT，唯一性拼接。|两行级伴随推论。|
|12|缓变组合F_{T(εn)}的可消首漂移和长时作用量？|仍缺真实参数导数、共振排除与统一误差；全实表未关闭旧义务。|旧非自治HOLD不重开；月级／高风险。|

这不是“12→若干篇通过”的筛选。当前没有一项被授予新意、价值、容量或完整候选PASS。
第4问仍同一代数公式，但不从纸面登记推定本轮可扩大锁定参数范围；无需为登记即暂停其它已授权工作。
若把第1问移成独立连续流理论、或另造量子算子／谱行列式，属于 ROUND2_CLUE，不列本轮执行项。

## 4. 第1／2问的实际短解压力：非接受定理

DLM 的 Thm3假设已有完备对称流和全局Poincaré截面，Thm9从不变量得到Hamiltonian对称场；
其Lyness例删去中心固定点，在正象限主层执行，不是本题保留两节点的完整曲面定理。[DLM]
第1问尚需在坏纤维平滑群中核2P的单位分量、相对指数映射的有限时间枝及两端匹配。
若有全底单值解析 a_T(h)，由 K_T'=a_T 即得生成场；旧terminal正则、有限完整实纤维紧致等须扣为旧输入。
“奇次不能交换圆”对任意自治Hamiltonian还需先由稠密轨道推出它局部只依赖h；不能省略该接口。

第2问的纸面路线：原 I8 八边界、O/P所在 terminal 的相对位置可能给分量距离3与P·O=0，
从而高度为2−3·5/8=1/8；若四有限坏纤维全为I1，秩一与NS判别式将强迫P生成几何MW。
这还需正式核对截面接点、光滑模型与系数域；本轮只认为短解压力强，未授MW定理数学PASS。
代理读到的 Schütt–Shioda 是综述定位，不冒充其引用的 Oguiso–Shioda 1991 原始分类实读。[SS]
P30 V4中“complete primitive pencil”不是MW本原；定向关键词未命中也不能等价于全文不存在该结论。

允许移动能量底亦有短排除路线：j唯一八阶极点在∞，其它四极点简单，令底作用φ(h)=Ah+B。
有限极点根和为1给B=(1−A)/4；比较j在∞的h8、h7给A^8=1、B=(A−1)/8，故φ=id。
应使用正确归一化 c4=(h²−4T)²+24Th、Δ=T³δ、j=T^−3(h8+h7+O(h6))。
代理初稿误写T²与T^−2；主控按b8=−T³指出，代理无工具重新展开确认勘误。
该常因子不改变相对系数比较，但此处保留错误与修正来源，不把未审推演记为正式证明。

## 5. 第3问的最小非平凡接口：仍是纸面可行性

对象锁为固定T>0，K=R(h)，τf(z)=f(z+P)；全部几何极点支撑于预先有限区间 aP,…,bP，不只是K有理极点。
在无坏特化的实torsion纤维，要求全部避开极点的实周期轨道和为零；不是只测试一条选定轨道。
每个固定小阶只有有限好参数，故稠密真实torsion特化可选阶大于b−a；这使有限支撑中的点不碰撞。
纸面代理用迹主部系数Σ_j c_{j,k}(h)在无限特化消失，推到各orbital残数在K中为零；已有求和理论把剩余压到两个相邻简单极点的二维空间。[AB]
本模型该余项有直接有理代表

$$Z_P(z)=\zeta(z+p)-\zeta(z)-\zeta(p)=\frac{v-T}{u}+\frac h2,$$

其微分规范为ω=du/(2v+hu−T)，wp(z)=u+(h²−4T)/12，wp'(z)=2v+hu−T。
不能总假定实P在单位分支：写p=α(h)ω1+βω2，β为固定有理数，实torsion时α有理。
余项A+B Z_P的迹除N等于A+B(αη1+βη2−ζ(p))；稠密特化使之成为实开区间恒等式。
若B不为零，就要求该归一化ζ值等于K中的有理函数；对具有非零非对角项的周期单值化使用Legendre关系，
预期将迫使α为有理常数，与P泛非扭矛盾。非等模代数椭圆族的单值群有限指数是标准背景，[UU]§2.2有明确说明。
纸面代理还给出K上主部构造：d_{j,k}=Σ_{i=a}^{j−1}c_{i,k}，以W(z)=Z_P(z−(a+1)p)消掉唯一总残数障碍，
再用K上的Riemann–Roch主部精确列，可取转移函数极点限于(a+1)P,…,bP且极点阶数不增；a=b单独迫f=0。
该转移支撑界依赖本件τ作用方向，不得倒置。其修正后的单值化差为

$$Q'-Q=\frac{\eta_1\omega_2-\eta_2\omega_1}{\omega_1\omega_1'}
\left[b_0(p-\beta\omega_2)+(b_0m-a_0n+\beta(1-a_0))\omega_1\right],$$

其中ω1'=a0ω1+b0ω2、p'=p+mω1+nω2；b0≠0使α为有理常数。
代理终态认为短证明路径未见缺口，但未形成独立核准的数学稿；本报告不据此登记accepted theorem或无先例认证。
剩余应独查的是精确定义、主部方向／支撑界、半周期公式和引文接口，而非已识别的新增科学假设。
尤其AB已有一般求和完整障碍和Riemann–Roch型维数公式；本题若成立，增量只能是实周期特化检测接口。
不把这一可能短引理拼到失败全实包凑页；若后续要消费，应先闭合并核真正区别于AB的命题。

## 6. 本轮新实 Betti 试探为什么是实际新输入

[BM] 并非再证明既有固定T表。它增加dρ(T,h)≠0、三个M的严格参数排序与准确端点，
实际补出正紧T窗上的C¹余项量词，并求固定h=κ√T的大T真实积分极限。
随后用已接受尖点不分歧，把正则实角条件接成全X1(N)正实点分歧清单。
这些都已写成202行作者证明，而非数值观察或问题列表；其非作者检查是另一件工作。
[OD] 给每个所数实临界值的奇惯性；N=2n≥10以m=n−1统一供给上外见证，不作阶数枚举。
它只改变旧“缺一个有限奇惯性来源”的具体义务，不解决任意中间域、复分支碰撞或满群。

这里须分别扣除：dρ的模空间短推论、IFT、精确阶翻译、共轭配对群论，均不是新一般理论。
真正待定向比较的对象，是指定b实分歧的全阶准确结果及其所必需的新参数边界控制。
“旧文通用界不同于准确清单”不足以自动给7.5；也不能承诺把此附到失败包就会升分。

## 7. 本轮外文实读账：范围，不是全文认证

|来源|阅读者与实际范围|允许消费／不可越级|
|---|---|---|
|[ACZ] 1802.03204v1|主控，PDF文字0–112，摘要及引言第一部分|Betti与torsion背景；未读§9全实超椭圆证明，不能排除其中更强实结论。|
|[GAO] 1810.12929v6|主控，摘要／引言至Thm1.1；§3.2–3.3与§4，核心文字544–830|普遍Betti自然投影及沿纤维群同构；不称全36页。|
|[MN] 2206.09405v1|主控，摘要、引言及Thm1.1所显示部分，文字0–145|重数已有研究与框架；未把未完整读完的定理作新证明依赖。|
|[CDMZ] 1909.01253v2|主控，摘要与§1至1.2.1，文字0–92|torsion分布与重数先例；非全文45页或全部主定理认证。|
|[UU] 2002.01906v2|主控，§1完整、§2.1–2.2，文字0–269|切触界已有；非等模单值群有限指数的精确标准接口。|
|[BCZ] FMS2022 e84|主控，官方HTML摘要、§1至Thm1.3后，文字483–585|Betti、Pell、分歧表示近邻；未读后半单值群／本原性证明，不套作本b投影结论。|
|[BAB] 2503.22770v1|主控，论文身份、摘要与引言至1.2.1开头，文字0–247|博士论文早版本及求和背景；非89页全文。|
|[AB] 2508.18247v1|主控，摘要、§1至末、Lemma2.1；重点文字45–294、352–357|完整求和障碍主张、扭平移迹、二维余项与应用范围；未读全部§4证明，不据此给新泛定理证明PASS。|
|[DLM] 1111.3887v2|查新代理，§§2.1–2.2、Thm3含证明、§2.7、Thm9含证明及Lyness例|提升与正则主层；不覆盖两节点全曲面。|
|[CD] 1106.0930v2|查新代理，§2.4、Thm2.10及平移延拓部分、Remark2.11，印页12–14|保Halphen铅笔与平移；不套unnodal的Z8特例。|
|[SS] 0907.0298v3|查新代理，Cor6.13、§7.6、§§11.4–11.11.1，印页29、33–34、50–53|明确是综述定位；不是原始1991分类全文。|
|[GV] 2026官方摘要|查新代理，只摘要|近恒等近似嵌入不等于精确全域嵌入；不称正文实读。|

主控一次并列web输出总量截断，截断落在AB引言前段；该段45–92已由较早单次输出读过，
所消费的158–294完整显示。Gao核心544–830亦完整显示；不把输出标签“long”当作全文。
研究网、百科、自动综述和镜像命中仅作发现或无关结果，未作为定理证据；没有重试旧受限入口。
旧BR后段／BC／Duistermaat缺读仍保留，不以这轮换主题浏览自动关闭其包含缺口。

## 8. 实际查询清单与停止规则

主控23条query，按实际顺序：

1. real Betti map elliptic curves torsion ramification modular curve Tate normal form b
2. Lyness rotation number maximum parameter monotonicity bifurcation torsion
3. modular curve X1 N real critical points Tate normal form b ramification
4. Betti map submersion universal elliptic curve real torsion section
5. elliptic curve difference summation discrete residues rational functions translation coboundary periodic torsion
6. Lyness map Hamiltonian embedding time one map disconnected invariant curves
7. elliptic Betti map critical points torsion sections tangencies real Corvaja Demeio Masser Zannier
8. "Summability of Elliptic Functions via Residues"
9. "Lyness" "Hamiltonian" "flow" embedding
10. "Tate" "b" "real" "ramification" modular curves
11. "Lyness" "maximum" "parameter" rotation number 2025 2026
12. "Panorbital residues and elliptic summability"
13. "Symmetry Reduction by Lifting for Maps" arxiv
14. "Lyness" "rotation number" "maxima"
15. "elliptic" "summability" "specialization" torsion
16. "elliptic" "periodic orbit" "coboundary" rational
17. "modular unit" "real critical points"
18. "Tate normal form" "critical" "b"
19. "real" "b" "X_1(N)" "ramification"
20. "Tate normal form" "critical points"
21. "Lyness" "Betti"
22. Ulmer Urzua torsion multisections sections elliptic surfaces Betti tangencies 2021
23. real ramification Tate normal form modular units b van Hoeij Smith

查新代理另6条（不算成主控本人检索）：

1. "Lyness" "embedding" "Hamiltonian" map global singularities 2024 2025 2026
2. "Symmetry Reduction by Lifting for Maps" Lyness complete flow
3. "integrable" "map" "autonomous Hamiltonian" embedding separatrix analytic 2025 2026
4. "QRT" "centralizer" "Mordell" roots
5. "rational elliptic surface" "centralizer" "translation" primitive
6. site:arxiv.org "QRT" "root" "Mordell" 2024 2025 2026

部分精确词查询只出无关结果；这是检索阴性，不是不存在先例。近期命中日期以原文／官方版本为准，不采用爬取器相对日期。
本轮初筛在这些问题和来源范围停止，不重复扩搜旧FAIL包，不把每个短消费者都启动完整A–D或正式双席。
原22–30页完整合同不变：任何真正新候选仍须两位fresh非作者各自完整四门，不拼票、不平均或改阈值。
下一工作先看 [BM]/[OD] 的独查终态，再按真实新命题进行针对性包含比较／单中心可行性判断；
若仅是短消费者，则回到原问题，不将“有数学进展”写成“有Paper31”。
全批本地接受4/5、第五篇及统一审计未完成；这里没有目标完成或阻塞声明。

[FD]: PAPER31_QPI_REAL_GLOBAL_TWIST_FORMAL_CANDIDATE_DISPOSITION_V1_20260912.md
[CB]: PAPER31_QPI_REAL_GLOBAL_TWIST_CANDIDATE_BRIEF_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[PORT]: PAPER31_QPI_REAL_GLOBAL_TWIST_PORTFOLIO_DELTA_V1_20260912.md
[BM]: PAPER31_QPI_REAL_BETTI_MODULAR_FEASIBILITY_V1_20260912.md
[OD]: PAPER31_QPI_REAL_BRANCH_ODD_INERTIA_COROLLARY_V1_20260912.md
[ACZ]: https://arxiv.org/pdf/1802.03204
[GAO]: https://arxiv.org/pdf/1810.12929
[MN]: https://arxiv.org/pdf/2206.09405
[CDMZ]: https://arxiv.org/pdf/1909.01253
[UU]: https://arxiv.org/pdf/2002.01906
[BCZ]: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/betti-maps-pell-equations-in-polynomials-and-almostbelyi-maps/999A05A799D0BC64A35C64D4AA955166
[BAB]: https://arxiv.org/pdf/2503.22770
[AB]: https://arxiv.org/pdf/2508.18247
[DLM]: https://arxiv.org/pdf/1111.3887
[CD]: https://arxiv.org/pdf/1106.0930
[SS]: https://arxiv.org/pdf/0907.0298
[GV]: https://www.aimsciences.org/article/doi/10.3934/dcds.2026004
