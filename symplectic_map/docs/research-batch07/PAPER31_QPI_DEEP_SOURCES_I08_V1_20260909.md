# Paper31：I08 指定点统计的深核来源与包含边界 V1

日期：2026-09-09 UTC；执行席：主控 `/root`。
状态：`NOVELTY_PHASE_B_COMPLETE_WITH_DISCLOSED_SOURCE_LIMITS / NO_PHASE_CD_SELF_VOTE`。
这是三个固定核心的来源合取，不是完整统计证明或Paper31准入。

## 1. 对象、已知输入与差额

对象保持 [Phase A §5](PAPER31_QPI_SURVIVOR_CLAIMS_PHASE_A_V1_20260909.md)：
$E_{T,h}:v^2+huv-Tv=u^3-Tu^2$，指定点 $P=(0,T)$，固定有限域时间参数 $T$，能级 $h$ 变化。
C1问准确全层仿射像及参数例外；C2问行列式 $q$ 陪集内真正点阶分布与有效误差；
C3问有限层尾项以及返回原时间／状态权重，不把一次可除性或固定层当成完整分布。

当前 [几何数学接受](PAPER31_QPI_KUMMER_MATHEMATICS_DISPOSITION_V1_20260909.md)只关闭C1的一个准确范围及正确有限层接口：
$p\ge5,T\ne0,-27/256,\ell\ge5,\ell\ne p$，全部 $n\ge1$ 的几何像为 $W_n\rtimes\operatorname{SL}_2(\mathbb Z/\ell^n)$。
C2、C3的完整计数、常数和统一尾项仍OPEN；本轮没有补写它们的证明。
这条短证明大部分已知机制十分明确，不能因其现已正确就提高全球新意判断。

共同本地基线已FULL读：十项生成、组合基线、两个接口接受、Phase A及三份首筛。
作者Kummer138行和非作者157行均FULL读，终态哈希见数学处置。
[周期首筛](PAPER31_QPI_QUICK_FILTER_PERIODS_V1_20260909.md)原SHA为 `4b28392b985bc3ecc56909570678b33541b435981b886193ea56915b3b5792f4`。
原P30自治共轭与完整闭纤维周期、P11模型识别后的一般群论循环清单全部先扣除。
不将特例 $T=1,h=2$ 的点塔当新对象：它经 $y=v+u-1$ 正好是Jones–Rouse Example5.4的 $y^2+y=x^3-x,P=(0,0)$。

## 2. 实际检索与读取边界

采用 `novelty-check` 每核心至少三个表达式，配合 `research-lit` 的一手定理核对。
下列20条为本轮实际问题／追索查询；首筛查询不重计，网页打开不计查询。
公开网页、arXiv、作者站与机构存档可用；没有配置Zotero、Obsidian或指定GPT-5.4 MCP。
Scholar／Semantic Scholar仅尝试公开域定位，无成功全库检索或API权限，不声称“全数据库查无”。
ML会议与此纯数论任务无主题适配；纯理论GPU0，无候选实验或大规模有限群枚举。
默认不向本地论文库下载PDF；指定原文通过网页或流式文本临时读取，未持久新增外部PDF。

| 查询 | 实际字符串 | 用途／结果限度 |
|---|---|---|
| Q01 C1 | `elliptic surface I8 four I1 monodromy Kummer section Galois representation` | 椭圆曲面和Kummer入口，未给原族现成统计定理 |
| Q02 C1 | `"Kummer" "elliptic" "function fields" "2025"` | 时间限定，噪声较多 |
| Q03 C1 | `"elliptic" "Kummer" "monodromy" "2026"` | 近期单值群线索，须分清Kummer曲面与点塔 |
| Q04 C2 | `"elliptic" "point" "order" "fixed determinant" distribution` | 固定乘子／群阶入口，返回较弱 |
| Q05 C2 | `"elliptic" "finite fields" "Kummer" "density" point 2024 2025 2026` | 当前密度文献，不将数域与固定有限域混同 |
| Q06 C2 | `"elliptic" "point order" "distribution" Frobenius` | 点阶与Frobenius机制 |
| Q07 C3 | `elliptic point order reduction density Lombardo Perucca valuation` | 定位S2及全局点阶尾项 |
| Q08 C2补 | `elliptic curve finite field group structure fixed determinant matrices Gekeler distribution` | S3，完整群结构与矩阵模型 |
| Q09 C3 | `finite fields Kummer covers point order effective Chebotarev error tail bound elliptic 2024 2026` | 函数域尾项和有效计数入口 |
| Q10 C3 | `effective Chebotarev finite field curves genus Galois cover conjugacy class square root q Murty Scherk` | 追到S4、S5的精确定理 |
| Q11补 | `"Kummer" "elliptic" "monodromy" site:scholar.google.com` | 未取得可核Scholar条目，不算排除性证据 |
| Q12补 | `"Reductions of points on algebraic groups" site:semanticscholar.org` | 未取得完整S2 API检索 |
| Q13补 | `"elliptic" "fixed determinant" Gekeler matrices probability` | S3、S4及S5附近函数域结果 |
| Q14补 | `Hall Voloch "function fields" "primitive points"` | 定位S5与作者目录 |
| Q15补 | `"elliptic" "Bh" "Chebotarev" "Hall"` | S5索引，不以片段当全文 |
| Q16补 | `"Chebotarev" "Σ" "Voloch" function fields primitive points` | S5及原始参考线索 |
| Q17补 | `"Towards Lang-Trotter" Hall Voloch pdf` | 作者独立公开PDF |
| Q18补 | `"Towards Lang-Trotter" site:web.ma.utexas.edu` | 确认作者入口 |
| Q19补 | `"Towards Lang-Trotter" site:arxiv.org` | 未取得该文arXiv版本 |
| Q20补 | `Akbary Ghioca Murty Reductions of points on elliptic curves pdf` | S6的作者PDF与正式刊行记录 |

最近六个月另实际调用arXiv公开API，区间2026-03-09至09-09。
宽查询先定位；随后使用 `(cat:math.NT OR cat:math.AG OR cat:math.DS) AND (ti:elliptic OR ti:Kummer)` 与上述 submittedDate 区间。
按提交时间递减分页，主控完整读取100+38条的题名／id／日期元数据；不是138篇摘要或全文阅读。
这只穷尽该表达式返回页，不穷尽最近所有相关论文；不含题名关键词的近邻另由网页／宽查询补到。
各新稿的实际阅读层级如下，未把HTML重排日期当首次公开日期。

## 3. 六项强一手先例

### S1. Jones–Rouse：全局域点塔和点阶密度

[Galois theory of iterated endomorphisms，0706.2384v4](https://arxiv.org/pdf/0706.2384v4)，2009-11-07版本，2010刊行。
主控实读引言、Theorem3.2与3.4及其邻近证明、Lemmas3.6–3.7与Theorem3.8；另读Theorem5.2／Corollary5.3／Example5.4／Theorem5.5声明。
Theorem3.2在global field设置下把分点塔固定端点的测度对应到约化点阶素于 $\ell$ 的Dirichlet密度；函数域并非新使用场景。
Theorem3.4的不可约模与挠点域不可除性已经给满Kummer机制；Theorem3.8在满平移条件下积分 $\ell^{-v_\ell\det(M-I)}$。
椭圆Theorem5.2用 $\operatorname{GL}_2$ 满像，不能原字代入代数闭常数下的 $\operatorname{SL}_2$；原作者直接余循环证明已补此接口。
该文不直接给当前固定 $q$、变化 $h$ 的有效陪集计数，但机制、真正点阶目标与同一特例必须扣除。

### S2. Lombardo–Perucca：一般点阶积分、可计算性与尾项

[Reductions of points on algebraic groups，1612.02847v2](https://arxiv.org/pdf/1612.02847v2)，2017-08-01版本；
[作者最终刊版](https://arpi.unipi.it/bitstream/11568/1018879/6/Reductions-final.pdf)标明JIMJ 20(5), 2021, 1637–1669。
v2主控实读引言Theorems1–5、前置增长定义，§4末Remark25／Example26，§5 Theorem27与Lemmas28–29及证明。
最终刊版只实际网页读取引言Theorems1–7；命令行随后403，未称已读其§5修订正文，未绕过限制。
这是数域上的一般公式、密度有理性、椭圆有效可计算性；不是任意固定行列式陪集的统一定理。
Example26已把满Kummer条件解释为：给定局部群的 $\ell$ 部分，约化指定点按相应有限群均匀分布。
因此“从群结构分布加一个均匀标记点得到点阶分布”并非新的统计原理。
v2 §5的可见文本在 $\det(x-I)$ 事件与证明中的 $\det(\lambda r)$ 之间存在未消歧的不一致；本件不据它证明任何尾界。
即使改用最终有效版本，数域全像中的大量标量也不自动留在固定行列式陪集，当前尾项仍需实际核证。

### S3. Gekeler：有限椭圆群与矩阵余核

[The distribution of group structures on elliptic curves over finite prime fields，Documenta Math.11 (2006),119–142](https://ems.press/content/serial-article-files/25986?nt=1)。
主控实读引言与矩阵模型设置；定向读§2的Lemmas2.11–2.15及其证明、相邻Theorem2.3分类段；非全文。
核心包含是以Frobenius矩阵余核组织 $E(\mathbb F_p)[\ell^\infty]$ 并计算局部群结构频率。
主文有跨素数／椭圆同构类的加权模型；不能把其全 $\operatorname{GL}_2$ 测度直接替成固定 $T,q$ 族。
其引言已指向Howe的固定有限域加权计数及有限素数局部分布独立性；本件未另审Howe原作，不授该更强精确公式。
真正剩余最多是准确陪集算式及本族的有效实现，而非矩阵余核或群阶模型本身。

### S4. Cojocaru–Hall：固定行列式的函数域有效计数早已存在

[Uniform Results for Serre's Theorem for Elliptic Curves，IMRN 2005 No.50](https://www.alinacarmencojocaru.com/cojocaru-hall-IMRN-2005.pdf)。
主控实际读完整引言Theorems1.1–1.4、§2模曲线／子群亏格证明的相关部分、§3完整Theorem1.2证明与Proposition3.1。
Theorem1.1：非等常数椭圆曲线在给定函数域上，几何mod $\ell$ 群对超过仅依基曲线亏格阈值的 $\ell$ 为 $\operatorname{SL}_2$。
有理基曲线阈值常数15，所以 $\ell\ge17,\ell\ne p$ 已通用；本原族的 $5,7,11,13$ 需另外处理。
§3准确使用 $\det(g)=p$ 陪集；tame覆盖的共轭事件具有 $O_{K,Z}(|C^p|^{1/2}p^{1/2})$ 误差，常数只依基亏格与分歧支集次数。
所以“必须固定行列式”“函数域无需数域GRH”“对一个参数族用有效Chebotarev”都不是新方法。
它不是原指定点的全层仿射定理；要应用仍须核本族平移群、tame性、层大小和所取点阶事件。

### S5. Hall–Voloch：指定点的函数域仿射与陪集框架

[Towards Lang-Trotter for Elliptic Curves over Function Fields，作者PDF](https://web.ma.utexas.edu/users/voloch/Preprints/lang-trotter.pdf)，刊于PAMQ2(1),2006,163–178。
刊商PDF首次定位后403；转读独立作者公开版本（14页），未访问受限服务或规避权限。
主控实读全文引言、§2.1全部Kummer引理、§2.3共轭类计数、§2.4及§3，§4.1–4.2全部与§4.3至三段尾项切分。
§2.1 Lemmas1–2已经对含 $\operatorname{SL}_2(\mathbb F_\ell)$ 的像用中心元余上同调与点不可除性给满仿射像。
§2.3已经明确按行列式 $\delta=1$ 与 $\delta\ne1$ 计数带标记点／子群的Lang–Trotter事件。
§4.2 Lemma5以tame分歧支集控制覆盖亏格；Theorem6给常数Frobenius陪集和 $|C(q^n)|^{1/2}q^{n/2}/n$ 型误差。
这比只引用一般“Chebotarev可用”更贴近当前问题，必须从C1–C3的方法新意扣除。
其全素数primitive subgroup主定理要求rank $r\ge6$；本单点rank一不满足，不能说它已经解决原完整原始点密度。
其degree-$n$闭点极限也不直接等于任意固定域的degree-one计数；层级转换必须明确。
前述完整原始点的无界素数尾，与当前一个固定 $\ell$ 的幂次尾，是不同难题，不能拿rank条件宣告本C3不可能。

### S6. Akbary–Ghioca–Murty：真正点阶／指数的有限层检测

[Reductions of points on elliptic curves，作者PDF](https://personal.math.ubc.ca/~dghioca/papers/lt_revision.pdf)，Math.Ann.347(2),2010,365–394。
主控实读完整引言Theorems1.1–1.4及相关工作、§3 Lemmas3.3–3.4和3.3完整证明，另读3.2部分证明；非全文。
Lemma3.4在共同 $\ell^n$ 挠点／分点域中，用 $\ker(A-I)$ 大小及 $\ell^{n-c}b\in(A-I)W_n$ 精确检测 $\ell^n\mid[E(\mathbb F_p):\langle P\rangle]$。
这是指数而非本点阶，但与群阶合取后即决定点阶；“必须越过一次可除性”早已有严密解决机制。
该有限群／Kummer论证的机制可迁移至有限剩余域；数域GRH／AHC仅涉及之后的解析计数，不限制群论判据的本质。
该文主定理的高rank与条件性不能被拿来否定本固定 $\ell$ 的有限域统计，也不能把原点阶接口重新命名成新机制。

## 4. 最近六个月的相邻新稿

| 一手版本 | 实际阅读层级 | 与I08的关系 |
|---|---|---|
| [Lee–Sheen 2606.25067v2](https://arxiv.org/html/2606.25067v2)，6月初稿／7月修订 | 摘要、§1起始及Howe／Banks–Shparlinski相关工作Theorem2；非完整主定理审计 | 讨论群阶整除与Serre曲线密度，不是指定点阶；加强群阶基线 |
| [Fan 2608.24744v1](https://arxiv.org/html/2608.24744v1)，8月25日 | 摘要、§1前部定义与相关工作，明确核多种Frobenius扇区目标 | 固定有限域椭圆同源映射的商线置换；不是变化 $h$ 的 $\operatorname{SL}_2$ Kummer族 |
| [Fan 2608.27255v1](https://arxiv.org/html/2608.27255v1)，8月27日 | 摘要、引言TheoremsA–C与相邻边界；定向定义2.14–2.16 | genus-one Galois closure之 $\mathcal N\rtimes$ 循环群、算术形式与扩域支持；不同于原非循环线性像 |
| [Hamakiotes–Lee–Mayle–Wang 2603.24915v2](https://arxiv.org/abs/2603.24915v2)，3月26日／5月10日 | 官方摘要及版本记录 | 两条数域椭圆曲线群阶互素的猜想常数／Euler型展开，非单点有限域分布 |
| [Milner–Shotton 2604.21601v2](https://arxiv.org/abs/2604.21601v2)，4月23日／6月5日 | 官方摘要及版本记录 | 数域最小不变因子密度常数正性与分点域重合，非本标记点塔 |
| [Ozeki–Yoshida 2609.06554v1](https://arxiv.org/abs/2609.06554v1)，9月6日 | 完整官方摘要 | $\mathbb Q_p(E[p])$与上分歧跳跃，特征零局部／剩余特征挠点；不直接包含本 $\ell\ne p$ 几何族 |

另见Rollenske–Ulivi–Zanardini 2608.19970的摘要，主题为标记degree-two椭圆曲面／Halphen与Enriques；未据此作I08包含判断。
未发现近期稿直接写出本完整C1–C3，不是全球“没有人做过”的证据；强早期机制更关键。
近期Fan两篇的扇区权重和算术／几何像区分也不能因不同对象而完全忽略，独立席可核它们是否进一步降低定位价值。

## 5. 按核心的实际包含边界

| 核心 | 已被强先例或组合吸收 | 尚未供应／可检验的准确剩余 |
|---|---|---|
| C1 全层满像 | 通用大素数SL2、Tate惯性、同源高度、中心余循环Kummer；原谱式与点已知 | 指定范围内所有 $T,p,\ell,n$ 的短证明现已接受；是否有足够结构性发现，而不是参数代入 |
| C2 固定det真点阶 | 固定det陪集Chebotarev、群余核与标记点、有限层指数判据 | 给本族完整可计算点阶律与有效误差；若只是数页有限群计算，独立长文价值很弱 |
| C3 尾项及原周期 | tame亏格线性界、闭点计数框架、旧自治共轭和周期权重 | 固定det统一幂次尾界、层随域增长的误差平衡、参数例外影响；目前无完整证明 |

主控未给新意分或排名，避免把来源作者自票当Phase C独立核验。
最强审稿反对意见是：主要正确性已在短证明中关闭，而完整统计消费者可能仍只是成熟Kummer／Chebotarev的标准练习。
相反，若具体族出现非标准的例外层行为、统一全层规律或对原动力学真正新的统计障碍，需要实证后才能改变此判断。
不能拼接别的幸存方向的最好部分给I08凑容量，也不借重写旧共轭链自然增加正文页数。

## 6. 后续与冻结边界

交全新非作者Phase C/D：每核心分别评方法／发现新意、最接近先例、反对意见、是否值得最小纸面诊断。
原Kummer数学作者与独审不是该新意票；新席不因已有数学PASS预设PROCEED。
需要的最小诊断若只是固定det余核分布，应明确判断它是否标准可解、是否能改变投资决策，再决定是否实施。
纯理论无GPU pilot；未完成数学仍需验证，但不存在“缺GPU”阻塞。
P31未立项／未建锁／未试写测页；完整22–30页要求与未来独立完整双票不变，整批4/5。
本文件新增后全文自读、核本地直接链接与哈希；不重扫旧构建、不重评分旧失败，也无任何对外效力。
