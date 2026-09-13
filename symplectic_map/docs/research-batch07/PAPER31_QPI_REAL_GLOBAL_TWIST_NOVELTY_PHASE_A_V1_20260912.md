# Paper31：全实正则旋转／twist 查新 Phase A

日期：2026-09-12 UTC；主控：/root。
状态：CLAIMS_FROZEN_FOR_TARGETED_NOVELTY；没有新意评分、正式准入或论文产物。
上一目标轮属于实质进展：完整分类及两阶段非作者数学接受已改变研究输入，不是无进展等待。

## 1. 本轮精确问题和输入

待查的是：既有文献是否已经给出或直接包含原固定全部 T>0、全部有限实正则能级的实际分支回返旋转分类？
数学基线为 [接受处置][D] 全部135行及 [全局合成][S] 全部133行，主控本轮已重新FULL读取。
D 的SHA为 c3325516b39ad2595863de544f7db577c6a65f72511f379c1f566a8aae8c568b；
S 的SHA为63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24。
六份证明和两阶段数学报告不因查新重开；本轮针对方法／finding的既有性与独立价值风险。
强来源及访问边界使用 [上轮来源审计][SRC]，不把目录、搜索片段或访问失败变成全文排除。

原对象为

$$F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
h=-x+y+x/y-T/x,\quad T>0,$$

原完整曲面保留四条terminal线；有限正则曲线为

$$v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\qquad F_T=+P.$$

定向始终为 ω=du/(2v+hu−T) 正向。上外单步交换两圆，因此研究 F_T²=+2P，而前两区间是 F_T。
不以固定T非固定Lyness参数、原图分母缺点或重命名正常形本身作新意。

## 2. 三项核心查新断言（同一中心，不是三篇论文）

### C1：全正则实能级的准确五行 twist 图

令 h−<h+<1 为两个实坏值。三个区间的严格导数形态为：
T<3/16 时仅中间有唯一非退化极大；3/16<T<1 时仅下外有唯一非退化极大；T>1 时仅上外有唯一非退化极大。
T=3/16、1 无正则驻点能级；其余 T 恰一个。其余各区间的严格符号按 S §2 全表，不缩为局部、泛型或正象限。
这是主要 finding；方法包括原 forcing、真实锚定及一阶符号，应与 finding 分开扣除。
须特别搜索两阈值是否只是既有QRT/Lyness实定理的参数重写，以及原族是否具有其它常见递推名称。

### C2：同一完整原状态上的端点、值域与回返匹配

六端点为 (5/8,θ(T))、(θ(T),1/2)、(0,3/4)，θ(T)=1/2+π⁻¹arctan(1/√(3−4w−))，T=w−³(w−−1)。
极大值由唯一实积分确定，七行准确开闭值域见 S §3；不声称初等闭式。
h=1 的上外二次回返角为1/2，h=9/8 的真实导数严格正，四个terminal点未删。
实椭圆群的圆旋转、有限迭代回返、正常形和原模型识别可能均属已有工具或组合基线；只评价真正全局增量。
θ=5/8 的 T=(1+√2)/4 只改变值域较低端点，不包装成额外twist阈值。

### C3：有导数控制的真实边界常数

加权导数 J=(δ/q)Ω²ρ′，q=8h−9；两端极限准确为 logT/8、−logT/4，均有 O_T(log|h|/|h|) 余项。
完整对数积分的常数、短弧两移动尺度及可微余项均实际证明，T=1不由数值或未控小量求导决定。
这些分析用于C1中的真实严格边界，而不是另立“椭圆积分渐近方法”；标准K积分、Wronskian与Tate渐近须扣除。
旧forcing及acnode系数在3/16消失已是本地接受输入，不重复申报为新方法。

## 3. 有界检索和包含性策略

每项至少三种实际查询，覆盖可用公开索引、arXiv、Scholar／Semantic Scholar可用入口。
含2024–2026与最近六个月（2026-03-12至2026-09-12）检索，基础原文不设年代上限。
ML会议库只作技能要求的领域边界检查；无直接数学结果则明确NA/无相关命中，不以无关学习实验凑来源。
已有强入口：Beukers–Cushman1998；Duistermaat2010 §§8.2、8.4、11.4；GMX2012；CGM2008；Bastien–Rogalski相邻QRT系列；原Joshi–Roffelsen。
不重新尝试已拒绝的同一403／406入口，不绕付费或访问控制；可核独立公开作者版本及官方目录／书目，记录实际范围。
精确名称之外也检索 QRT recurrence、reciprocal biquadratic map、autonomous q-Painlevé I 与实 twist bifurcation。
需要比较实域、参数变化方向、映射迭代次数、定向和完整曲面，不能只比较题名或常数外观。
不同系统族的线索最多记ROUND2_CLUE，不改本中心、不扩旧HOLD/STOP或N阶扫描。

## 4. 执行路由与下一闸门

主控已FULL读 novelty-check 两个版本、research-lit、ARS router 与 fact-check 必要工作流/角色/质量参考。
当前没有匹配的Codex GPT-5.4、Zotero、Obsidian或学术专用MCP；非配置工具不造成功调用。
相关命名本地PDF及 arxiv_fetch.py 未找到；literature/、tools/及项目用户侧arxiv目录缺失，另一标准arxiv目录无匹配脚本。
按research-lit公开web降级，ARXIV_DOWNLOAD=false，不启用程序化resolver/API或外部模型上传。
Phase B 由独立来源作者保存新件，主控并行核最强新线索及本地非碰撞。
Phase B 冻结后，以完整实际结果给新非作者C/D；使用可用Codex xhigh，不冒称GPT-5.4或跨模型核验。
C/D必须分方法与finding，输出新意分数及PROCEED／CAUTION／ABANDON，强缺读和最强反对随包；不是正式四门。
Paper31仍未准入且22–30页；后继正式两席各全部四门门槛保持，不将本轮查新票替代它。

[D]: PAPER31_QPI_REAL_GLOBAL_TWIST_MATHEMATICS_DISPOSITION_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[SRC]: PAPER31_QPI_REAL_TWIST_STRONG_SOURCE_AUDIT_V1_20260912.md
