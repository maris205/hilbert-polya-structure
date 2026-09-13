# Paper31 Q2：完整原曲面的 sharp 相混合——候选 brief V1

日期标签：2026-09-13。组包作者：/root。
状态：COMPLETE_CANDIDATE_BRIEF_FROZEN / MATHEMATICS_ACCEPTED / COMMON_INPUT_MANIFEST_PENDING / NO_FORMAL_ADMISSION。
这是研究候选与必要证明图，不是论文正文、source lock、publication lock或页数PASS。
候选只有一个中心：原自治 qPI 映射在完整实曲面上，逐连通圆中心化后的最优长时相关。
Paper31仍22–30页；Paper30的22–40页例外不传递。批次4/5。

## 1. 对象与精确主断言

固定任意 $T>0$，原公共图上

$$F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
h=-x+y+x/y-T/x,\qquad \Omega=\frac{dx\wedge dy}{xy}.$$

使用原八中心完整曲面 $U=S\setminus D$，四条 terminal 全保留，$h:U\to\mathbb R$ proper。
原有限正则纤维为完整实椭圆曲线
$v^2+huv-Tv=u^3-Tu^2$，且原 $F_T$ 准确为 $+P$，$P=(0,T)$。
这些原模型与平移是P30及旧证明输入，不申报新构造。
以 $\mu=|\Omega|$ 和逐连通圆条件期望 $\Pi$ 定义

$$C_n(f,g)=\langle(f-\Pi f)\circ F_T^n,g-\Pi g\rangle,
\qquad f,g\in C_c^\infty(U).$$

允许观测跨两个临界点、临界能级的持续圆及全部terminal，不假定中心化后仍原光滑。
对每个固定紧支撑能窗和固定 $T$，常数由原 $C^{20}$ 范数乘积控制。
令 $n=2m+r$，$m\ge1$、$r=0,1$，主定理为

| 参数 | 完整相关渐近 | 最慢阶 |
|---|---|---|
| $T\notin\{3/16,1\}$ | $m^{-1/2}\mathcal A_r(m)+O(m^{-3/2})$ | $n^{-1/2}$ |
| $T=3/16$ | $m^{-1/2}\mathcal A_r(m)+m^{-1}\mathcal D_r(m)+O(m^{-3/2})$ | $n^{-1/2}$ |
| $T=1$ | $m^{-2}\mathcal B_r(m)+O(m^{-3})$ | $n^{-2}$ |

[G, (1.2)—(1.5)]准确定义全部振荡系数，不含拟合参数。
$\mathcal A_r$ 为所有驻点圆和全部非零 Fourier 模的绝对收敛驻相级数；
$\mathcal B_r,\mathcal D_r$ 只使用原椭圆中心一阶jet的 $k=\pm1$ 系数。
这里不是把全观测类改成有限Fourier：所有其他模式进入已有可求和余项。
每个固定参数均有真正原光滑实／复观测，使相应归一化绝对相关的limsup严格正。
$T=1$ 的非消失条件是一阶jet对中的开稠密条件；主jet消失至少改进为 $O(m^{-3})$，
本候选未申报全部高阶jet的最优分类。

另外，完整saddle邻域经固定平滑能量截断后的相关，对每个指定整数 $N\ge1$ 是 $O(m^{-N})$，
由原 $C^{N+2}$ 范数控制。这是主定理必要局部估计，不是另一篇独立中心。
不要求 $T\to0,1,\infty$ 一致，不要求每对函数或每个时刻有非零同号下界。

## 2. 三个审查主张及唯一中心

1. **原完整观测类的强率。** 原有限阶光滑范数经退化角坐标与无限Fourier进入完整相关，
   覆盖saddle、消失小圆、持续圆和terminal；不是一般正则紧能窗的驻相练习。
2. **两类特殊参数及准确主项。** $T=1$ 的泛型 $n^{-2}$ 与其余参数的 $n^{-1/2}$，
   以及 $T=3/16$ 同能两圆的 $n^{-1/2}+n^{-1}$ 两层，都有有余项的公式和合法下界。
3. **原离散动力接口。** 上外区间原单步换圆，必须保留偶／奇两列系数；
   原 $F^2$ 在saddle有能量依赖解析时间，不能换成全局常数时间摆流。

这三项属于同一个完整相关定理，不按局部引理拆文，也不将每个参数行算作独立创新。
逐圆均值不同于整纤维均值；后者留下原光滑 $+1/-1$ 本征函数，连相关趋零都不能保证[M]。
这限定正确问题，不将条件期望或消去零模称为新方法。

## 3. 新证明与必要旧证明：谁真正承担什么

新三件作者证明为[K]292行、[E]377行、[G]358行；前置[M]128行、[N]238行已有短证数学接受[PD]。
三件新证明已由两份actual独查及主控FULL合取接受，见[AD]；本brief不能代替实际全文。

| 义务 | 实际证明承担者 | 性质与不可省略点 |
|---|---|---|
| 原完整曲面、proper能窗、真实 $+P$ | P30 §2及[OMAP] §4所列原段；[GEO] Step4；[M] | 必需旧输入；不能仅写两个分式冒领全曲面 |
| 原面积与terminal、逐圆投影 | [M] §§2—5 | 接口短证；不把非Hölder投影作原高阶光滑 |
| 真实两节点、周期穿箱次数、原解析短时间 | [GEO]；[N] §§1—3 | [N]用原 $F^2$，不是另一个流 |
| 全圆混合导数与移动接缝 | [K] Steps1—5 | $u=\log|p|$、Euler微分、归一化时间隐函数、重叠短时图 |
| 相位倒导数与无限Fourier反复分部积分 | [K] Step6；[G] §§3—4 | 边界是 $q\mathcal T^ja\to0$，不能误称所有迭代振幅趋零 |
| 全参数驻点分类与中心相位jet | [TW]、[B]及下述完整旧链 | 全部作为旧数学扣除；并非新Q2的独立发现 |
| 正时间对称角、中心jet与两个端点积分 | [E] §§4—8 | 真实 $\varepsilon$ 光滑、全k范数、准确负号和 $i/(2\pi k\gamma)$ |
| 驻相、全局分割、原奇偶与最优性 | [G] §§5—8；[E] §9 | 持续圆跨 $h_-$ 双侧一次驻相，不能删掉或重复 |

旧twist分类不是仅由[TW]133行概要自身证明。[OMAP]完整定位必要链：
[PF]的原非齐次方程及移动端点 → [B]的真实acnode锚值 → [MID]中区间端点、
[UP]上区间真实 $2P$／表观奇点 → [INF]两无穷端的可微常数 → [TW]的严格分类。
新Q2不需要旧值域表、每个极大值积分方程或来源桥接作为额外科学结论；
但全参数“有且仅有这些驻点”的真实必要证明不能借此删除。
P30一般阶法丛、正特征Hasse高层及P31扭点厚度链不被本相关定理消费，不能机械加入正文。

正式席应FULL读[M]/[N]/[K]/[E]/[G]以及[GEO]/[B]/[MID]/[UP]/[INF]/[TW]/[PF]；
用[OMAP]定位完整原曲面等必要旧段，准确区分FULL、PARTIAL与接受记录。
已接受且输入未变的旧数学不重新开票；正式完整性审查仍需知道实际结论依赖什么、正文要写什么。
新三件终态身份由[AD]绑定；旧链身份由[OMAP]绑定。没有Git，不能伪造commit。

## 4. 强先例与新旧贡献扣除

[S]和[CD]已就与这里相同的最强Q2目标完成主控18条、独审18条query及限定一手正文核验。
本轮不把未变检索阶段重新开做，不把这些数字写成36篇全文或穷尽数据库。
正式席仍应亲读约定的一手范围；本地作者报告不能替代其来源判断。

| 来源 | 必须扣除 | 不可误报的范围 |
|---|---|---|
| [FHR摆定理](https://arxiv.org/pdf/2105.02484)，Th2.2、§7 | 跨separatrix的原光滑观测、逐轨道均值、全Fourier；双曲端任意有限幂率、椭圆jet控制率 | 不是原qPI、twist驻点与换圆奇偶的同一定理；不能包装“首次跨节点” |
| [MRVB](https://arxiv.org/pdf/2201.07019)，Th1.1—1.3 | 一般能量—角度相混合与简单频率驻点框架 | 其C¹驻点率是 $t^{-1/3}$，不是现成sharp $t^{-1/2}$；标准驻相本身仍非新方法 |
| [HRSS](https://arxiv.org/pdf/2405.17153)，Lemma2.1及主定理 | 原光滑中心观测的Fourier消失阶、椭圆trapping技术 | 主定理的单调周期／宏观核对象不直接包含本题saddle和任意光滑双相关 |
| [Liu–Zhang–Li](https://arxiv.org/html/2509.20690v1)，Th3.1 | 原确定性离散系综的Cesàro均值框架 | 不是未平均相关的sharp渐近；逐作用全非共振不直接适用于本能窗 |
| [Liu2026 Markov](https://link.springer.com/article/10.1007/s44198-026-00424-7) | 随机扰动下的模衰减 | 不能删掉随机机制仍引用指数阻尼 |

各人实际一手阅读的页码与缺读，完整保存于[S]/[CD]；不冒称全篇FULL。
最接近的FHR必要范围为PDF1—6、25—32、34—40；其余部分、含Lemma7.15证明不是原报告的FULL范围。
MRVB主定理PDF1—4，HRSS主定理入口及原Lemma2.1以[S]/[CD]分别实际范围为准。
已知403／权限拒绝保留，不能绕过访问边界；不因缺读断言无先例。

旧全实twist正式新意7.2双FAIL完整保留；旧原曲面、forcing、两个阈值、全局频率图都从本候选创新账扣除。
新的本地差额是这个原完整系统的sharp相关定理，而非再次发现那些几何结果。
[CD]对最强目标的条件新意7.6、价值8.2、容量MID及STOP定位建议均不改写。
[PD]已澄清该STOP不是容量FAIL、正式FAIL或新权限门；也不产生准入保证。
本候选最强反对仍是：扣除旧频率图后，这是FHR式节点技术、标准驻相、原jet及有限迭代的具体系统组合。
实际证明成立只处理科学可行性，不自动使该反对失效或提高分数。

## 5. 组合内非碰撞和完整正文容量

本轮独立定向组合检查[PORT]已终态确认可辨认的本地增量；它不是全球新意或完整四门票。
P27–29的权重、循环字与多项式周期测试不提供这里的原光滑相关渐近；
P30大量原几何基础必须扣除。不得因题名不同或“circle/periodic”术语相同便判非碰撞／碰撞。

自然容量是未决硬门，不从1,027行新证明、文件字节数或其他论文页数折算。
正式席须按必要正文模块给低／中／高预测，并各自回答是否可信落在22–30页。
必须同时计入新的完整分析和上述未成篇旧twist链所需的真实正文负担；
不得把内部接受记录当成公开已发表定理，从而用一行引用规避必要证明。
反过来，共享基础只写一次，已可合法引用的标准定理与P30成果不为填页重复长抄。
不得把必要证明外移附录、补充材料或不可用的本地笔记；不改字号、边距、量词或页数门槛。
容量有可能太短，也有可能因必要旧证明而超30页；两种真实风险都须保留，作者不自授PASS。
尚不试写、试排或创建TeX项目。

## 6. 正式准入的下一步与边界

[AD]已作实际数学接受，[PORT]已冻结，本brief现在冻结。
下一步将本brief第3—4节的必要FULL／PARTIAL／一手来源范围汇成双方相同的明确共同清单并绑定终态身份，再启动完整正式审查。
两位fresh非作者必须各自评完全部四门：新意≥7.5、独立价值≥7.5、完整证明信心≥9、可信22–30页容量PASS。
不以两位数学审查者当成本次已经取得的正式四门票，不平均、拼票或重抽同包。
research-review指定GPT-5.4端点当前不可用；若采用secondary Codex xhigh须如实说明，不冒称跨模型。
通过全部正式合取后才进入source/publication locks及实际正文／确定性构建／PDF验收。
未通过则按真实门槛保留失败，不弱化完整原类、复活旧twist包或添加小推论补分。

不主张原未投影系统混合、单圆混合、CLT、谱统计、Hilbert–Pólya、Riemann行列式或一般常数时间嵌入。
route_applicability: NOT_APPLICABLE。无新数值、CAS、参数／阶数枚举或N≥10扫描。
Q3继续后备，不因本候选组包自动启动。当前交付只本地，无投稿、上传、托管、push、对外发信或付费资源操作。

[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[K]: PAPER31_QPI_Q2_MIXED_NODE_SYMBOLS_V1_20260913.md
[E]: PAPER31_QPI_Q2_ELLIPTIC_JETS_V1_20260913.md
[G]: PAPER31_QPI_Q2_GLOBAL_DECAY_PROOF_V1_20260913.md
[GEO]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[MID]: PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md
[UP]: PAPER31_QPI_REAL_UPPER_RETURN_FINITE_TWIST_V1_20260912.md
[INF]: PAPER31_QPI_REAL_INFINITY_C1_ASYMPTOTICS_V1_20260912.md
[TW]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[PF]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[OMAP]: PAPER31_QPI_REAL_GLOBAL_TWIST_CURRENT_PROOF_MAP_V1_20260912.md
[PD]: PAPER31_QPI_Q2_MATHEMATICS_AND_PREFLIGHT_DISPOSITION_V1_20260913.md
[S]: PAPER31_QPI_Q2_STRONG_TARGET_SOURCE_SCREEN_V1_20260913.md
[CD]: PAPER31_QPI_Q2_STRONG_CENTER_PREFLIGHT_CD_V1_20260913.md
[AD]: PAPER31_QPI_Q2_DECAY_MATHEMATICS_DISPOSITION_V1_20260913.md
[PORT]: PAPER31_QPI_Q2_PORTFOLIO_DELTA_V1_20260913.md
