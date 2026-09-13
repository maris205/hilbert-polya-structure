# Paper31：实旋转强来源逐定理包含关系补单 V1

日期：2026-09-12 UTC，按本席实际 clock 读数19:01:42；文件名沿用主控指定日期。
执行者：`/root/p31_real_strong_containment_supplement`；唯一文件所有权为本件。
状态：BOUNDED_SOURCE_SUPPLEMENT_TERMINAL / BR_LATE_SECTIONS_UNREAD / NO_RESCORE。
本件供完整单中心 brief 消费；不重开上一 A–D 评分、原数学验收或正式四门。

## 1. 可直接消费的结论

BR2005 的两个固定参数入口均满足其已知非负系数假设；不能再以“固定 T 不固定参数”排除它。
第一入口的 BR 标准能量是 $K_1=-h$；第二入口的标准能量是 $K_2=-h/\lambda$，$\lambda=T^{1/3}$。
后一个比例来自已接受 [Q] 的 $G_T=\lambda G_{\rm BR}$，不是新共轭或新数学 finding。
BR 的正域圆动力基础应扣除；其 §§6–9 后段定理、角度提升和 twist 结论本轮仍未取得。
因此没有形成足以断言“下外严格图已被完整包含”或“BR 已排除”的直接定理链。

新读到的 BMR2016 作者机构稿 Proposition 1 只在 $a,b>0$ 范围给 $2/5$ 无穷端。
其相同段落使用的三次不变量在 $b=0$ 形式代入时成为常数 $a^3$，不能由该表达式得到本零参数能量。
这仅排除对该具体正参数命题的直接零参数套用，不证明该文其它段落或其它旧文没有零边界结果。
CGM 的零参数 $5/8$ 仍按 [Z]/[D] 记为已有数值问题及本地严格传递；后续首证优先权未闭合。
Duistermaat 与 BC 未发现新的可消费合法正文，保持既有精确缺读边界。
当前结论是可组包的已知扣除加未决风险，不是新分数、正式新意 FAIL 或准入授权。

## 2. 技能、范围与实际输入

本人 FULL 读取 research-lit/SKILL.md 193行及 novelty-check/SKILL.md 86行。
采用文献核查与既有查新后的有界包含性补单；主控明确范围覆盖模板的全 A–D、重复跨模型和会议库扩检建议。
未使用 ARS；未调用外部模型、再委派或把本席计作正式独立评分席。
没有 Zotero／Obsidian 工具元数据命中；相关本地命名 PDF 与 arxiv_fetch.py 定向检索无命中。
实际检查 papers/、literature/、tools/、用户侧两个 arxiv 技能位置；未扫描全部 PDF 或旧构建树。
按技能降级至公开 web，arXiv 使用站点检索；ARXIV_DOWNLOAD=false，未保存或下载 PDF。

以下五件本人 FULL 阅读；首次组合回显中 B/Q 被截断，随后分别完整重读，不以截断稿报 FULL。

| 输入 | 行／bytes | SHA256 |
|---|---:|---|
| [D：最新处置][D] | 130／11107 | 0923e18bd1286daa421a5656cffe8f4bb31aaa3e1a7ffd2ba8030f0fbcd25ce1 |
| [B：Phase B][B] | 213／19024 | 059dc1df27a69f5227f449394137ca7ebb4d47e56eb8a41610194a2594b8a521 |
| [Q：正域接口][Q] | 140／8737 | 089df2e31231d3bf2288525dd2fd99f7c3a7fda0f01fb98d2fb7543715cb0c44 |
| [Z：零参数接口][Z] | 123／7175 | 3c5809411c9979b6d6702dbb867af85fce78dff15fb568fddabc204dbc2d5ceb |
| [S：全局合成][S] | 133／6753 | 63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24 |

[SRC] 仅定向读取43–105行的 BC／Duistermaat／继承来源，以及138–159行失败和交接段；不报 FULL。
原几何、源桥接与全局分类的接受状态消费 [D]；Q/Z 中旧 pending 是历史快照，不重新验收未变输入。

## 3. BR2005：旧假设 → 准确代入 → 结果边界

一手身份：G. Bastien、M. Rogalski，Advances in Difference Equations 2005:3，227–261，DOI10.1155/ADE.2005.227。
本轮新读 [BR官方页][BR] 的摘要、作者、出版日期及开放许可；数学原式另继承 [B] 对原文式(1.2)、(1.5)、(1.6)和 Theorem3.2 的读取。
旧式为
$$\mathcal F_{A,B,C,D}(p,q)=\left(\frac{A+Bp+Cp^2}{q(C+Dp+p^2)},p\right),$$
且 $A,B,C,D\ge0$、$A+B>0$、$B+C+D>0$，研究域为正象限。
其式(1.5)标准能量为
$$G_{A,B,C,D}=pq+D(p+q)+C(p/q+q/p)+B(1/p+1/q)+A/(pq).$$
此处大写系数避免与 [Q] 的倒数坐标 $a,b$ 混淆。

| 核对项 | 第一固定参数入口 | 第二固定参数入口 |
|---|---|---|
| 旧系数 | $(A,B,C,D)=(T,0,0,1)$ | $(\lambda,1,0,0)$，$\lambda^3=T$ |
| 假设代入 | $A+B=T>0$，$B+C+D=1$ | $A+B=\lambda+1>0$，$B+C+D=1$ |
| 文献标准能量 | $K_1=pq+p+q+T/(pq)=-h$ | $K_2=ab+1/a+1/b+\lambda/(ab)=-h/\lambda$ |
| 非平衡正域能量 | $K_1>-h_-$ | $K_2>-h_-/\lambda$ |
| 对应原实域 | $x>0,y<0$；完整下外无 terminal 圆 $C^1$ | 同一圆经双倒数正域坐标变换 |
| 迭代 | 一次 $\mathcal F$ 对应一次原 $F_T$ | 同为一次；不是原 $F_T^2$ |
| 原能量导数方向 | $dK_1/dh=-1$ | $dK_2/dh=-1/\lambda$ |
| 文献角度定向 | BR 后段约定未读 | 双倒数保平面方向；仍不能补造 BR 约定 |

表中的圆身份、双向共轭与定向事实全部继承 Q/Z/D，本席没有重做证明。
Z 已给原 $\omega$ 正向在 $(p,q)$ 平面为顺时针，双倒数仍为顺时针。
若 BR 使用逆时针，其所选连续提升须进一步核对补角；若使用顺时针，仍须核主值及整数选择。
故即使未来看到旧文的“递增／极大”，也须先处理能量反向和角度方向，不能直接抄到原 $h$ 表。
CGM 已接受的逆时针恒等式不能替代 BR 自己的角度约定。

| 已知旧实际所得 | 对本族应扣除 | 本轮仍不能从该结果推出 |
|---|---|---|
| 官方摘要及继承 Theorem3.2：正域持久有界、正组件与固定点动力基础 | 下外 $C^1$ 的经典正域圆动力背景 | 两阈值、严格导数符号及驻点唯一非退化 |
| 官方摘要：正组件上的圆旋转共轭，及周期／轨道分布研究 | 用经典四次递推取得圆旋转不是新方法 | 本文全部实域、terminal 及上外 $F^2$ 的量词覆盖 |
| B继承引言定位 Theorem6.11、§7、§8；Q继承表8.1在p257的索引片段 | 明确应优先检查的强包含位置 | 索引不是那些定理、表格或证明已读 |

精确缺口：BR §§6–9 的完整假设、例外、旋转公式和约定、端点、单调性及驻点结果均未获新正文核准。
不能把“原族正域只对应一个圆”误作全部旧文实域范围已经核清；也不能仅凭一般族包含就断言全五行表已知。
因此本节完成准确适用性与扣除矩阵，但没有伪称完成后段逐定理阅读。

## 4. CGM 零边界与一个实际读到的后续正参数命题

继承 [Z]/[D]：$\Phi_TF_T\Phi_T^{-1}=L_0\circ L_\lambda$，原一步对应两次交替更新。
继承能量 $E=-h$ 与准确逆时针提升 $\rho^{\rm CGM}_{0,\lambda}(E)=\rho_T(-E)$。
由此可严格传递已有下外端点及三段参数图，但是否首次证明不能由这条本地同一性决定。
[CGM][CGM] §5 的零参数 $5/8$ 数值问题、方向说明及末项数值文字差异，本席只继承 Z/B 的实读记录。
本轮发现 UPC 正式发表版本的机构 PDF 链接，但直接打开为403；停止该入口，未把 SERP 片段升级为新正文。

新来源为 Bastien–Mañosa–Rogalski，[BMR2016作者机构稿][BMR16]，书章 DOI10.1007/978-3-662-52927-0_22。
PDF封面说明卷180、pp321–335、2016；搜索抓取日期不作出版日期，未另核最终出版社年栏。
实际消费：所返印刷pp2–5（web行39–229），含 $a,b>0$ 范围、映射、不变量、Theorems1–2、Proposition1与Corollary1完整陈述。
另返回的pp6–9起始只作上下文；未读整篇、完整证明或附录，也未执行其算法／Magma代码。
Proposition1给正二参数的固定点角与 $\lim_{h\to\infty}\theta_{b,a}(h)=2/5$，并引用旧文 Proposition13。
它的参数空间明确为 $a,b>0$；本次目标 $(b,a)=(0,\lambda)$ 不满足其假设。
该稿显示不变量 $(bx+a)(ay+b)(ax+by+ab)/(xy)$；直接令 $b=0$ 得常数 $a^3$。
这是对旧公式适用性的简单代入说明，不是新零边界不变量、正常形或全族推导。
因此不能把这个正参数公式的极限和能量参数直接搬到零参数；需要另证的边界论证，或另一个实际定理。
本轮未取得这样的后续定理；有限查询无可消费命中不作“没有后续证明”的结论。

## 5. 对完整 brief 的扣除与风险接口

| 内容 | brief 可作的有限陈述 | 必须保留的风险 |
|---|---|---|
| C1 全参数全实严格表 | 只作为已接受本地数学及唯一主 finding 候选 | BR后段／Duistermaat强章可能含直接或易代入等价结果 |
| C2 端点和值域／回返 | 经典圆旋转与回返方法、CGM已有5/8问题均扣除 | 下外端点首证优先权、BR角度提升尚未读清 |
| C3 可微边界常数 | 原真实 $J$ 常数与余项只消费本地已接受证明 | 通用积分渐近不是新方法；旧文等价精确常数仍未排除 |

BC 保持 [SRC] 的未读四项：完整参数量词／例外、实域和能量端点、角度定向、原证明边界与正性条件。
Duistermaat 保持目录定位：§8.2 pp384–390、§8.4 pp395–399、§8.5 pp400–404、§11.4 pp518–545。
这些区间终止页继承目录推定，不是本席或旧席逐页实读；本轮未获新合法正文，不重搜整书镜像。
纯数学设计等级为 NA；可用性按定理假设与目标实域判断，不套临床证据等级。
没有开展 COI、撤稿、作者资助或期刊可靠性专项核查，不提供清白证明；开放许可不等于数学正确性。

## 6. 恰12条实际 query 与终止边界

基线不限年代；Q8为 arXiv 站点降级，Q12为近期窄补检，均不冒称数据库原生或全面覆盖。
Q12照实际发出字符串记录；其日期窗按环境日期选择，不把它说成 clock 日期下完美的六个月全库检索。
以下恰12条，无第13条；同调用汇总结果不虚报每条精确命中数。

1. `"10.1155/ADE.2005.227" "EMIS" -site:kurims.kyoto-u.ac.jp -site:math.ethz.ch -site:researchgate.net -site:scribd.com -site:nzdr.ru`
2. `"Global behavior of the solutions" "elliptic quartics" Bastien Rogalski pdf -site:kurims.kyoto-u.ac.jp -site:researchgate.net -site:scribd.com -site:nzdr.ru`
3. `"948567.pdf" "Bastien" -site:kurims.kyoto-u.ac.jp -site:researchgate.net -site:scribd.com -site:nzdr.ru`
4. `"Bastien" "Rogalski" "c = d = 0" -site:kurims.kyoto-u.ac.jp -site:math.ethz.ch -site:www2.math.ethz.ch -site:researchgate.net -site:scribd.com -site:nzdr.ru`
5. `"ADE" "Volume2005_3" "261" -site:math.ethz.ch -site:www2.math.ethz.ch -site:kurims.kyoto-u.ac.jp`
6. `"Bastien" "Rogalski" "elliptic quartics" site:emis.de -site:researchgate.net -site:nzdr.ru -site:dokumen.pub`
7. `"Lyness" "5/8" "zero" proof -site:researchgate.net -site:nzdr.ru -site:dokumen.pub`
8. `site:arxiv.org "2-periodic" "Lyness" "zero"`
9. `"elliptic quartics" "2005" "plane" -site:researchgate.net -site:nzdr.ru -site:dokumen.pub -site:scispace.com`
10. `"Lyness" "rotation number" "5/8" proof -site:researchgate.net -site:nzdr.ru -site:dokumen.pub`
11. `"Bastien" "Rogalski" "elliptic quartics" pdf -site:link.springer.com -site:math.ethz.ch -site:www2.math.ethz.ch -site:kurims.kyoto-u.ac.jp -site:researchgate.net -site:nzdr.ru -site:dokumen.pub -site:scribd.com -site:scispace.com`
12. `site:arxiv.org "Lyness" "rotation" "zero" after:2026-03-13 before:2026-09-14`

Q1–2定位官方页、新www2 ETH/EMIS入口及BMR2016；Q3–5未提供可新读BR后段。
Q6–8返回中有无关Lyness人名／数值分析与旧文线索；没有可消费的零边界新定理。
Q9–10定位CGM两个机构版本与已知EuDML记录；Q11–12未产生BR后段或近期直接包含定理。
SERP自动出现的非作者整书镜像和聚合全文未打开、未消费；没有凭长片段拼成旧文定理。

## 7. 本轮读取、失败和安全终态

| 本轮实际动作 | 实际结果 | 处置 |
|---|---|---|
| 新 `www2.math.ethz.ch/EMIS/journals/HOA/ADE/Volume2005_3/261.pdf` | 明确404 | 一次打开后停止；不是旧math.ethz路径重试，不作正文阴性 |
| BR官方landing及定向再显示 | 摘要、身份、许可正常读取 | 不把landing当35页全文 |
| BMR2016 UAB作者机构PDF初次open | 正常返回上述有限正文 | 实读段可消费；不报整篇阅读 |
| 同BMR稿从行0补取封面 | 400 Timeout fetching | 未恢复该次请求，未继续重试；不撤销首轮已读正文 |
| CGM UPC新机构PDF | 明确403 | 停止该入口，不换身份或工具绕取 |
| EMIS官方首页单次open，意在查正常公开镜像导航 | 明确403 | 停止；未枚举镜像主机或继续目录探测 |

继承而未重试：BC机构／出版社403、BR Wiley／Kyoto及书页 non-retryable safety、DCDIS406、旧ETH404。
Springer BR PDF后段旧失败是技术timeout，不是订阅／许可拒绝；本轮未机械重复其旧open/find/screenshot序列。
本席没有宣称新工具恢复该PDF，也没有配置API、代理、身份、凭据或外部模型。
没有截图视觉核验、CAS、数值、N枚举、原几何重推、稿件／锁／项目／BATCH／README改动或外部发布。
本有界补单已终态；下一步可携实际缺口继续完整brief，不要求主控因缺读停止已授权的本地组包。
只有新正常可访问一手正文或用户提供文本才能改变上述缺读；本件不预约无界检索或补造新意票。

[D]: PAPER31_QPI_REAL_GLOBAL_TWIST_PREFLIGHT_DISPOSITION_V1_20260912.md
[B]: PAPER31_QPI_REAL_GLOBAL_TWIST_NOVELTY_PHASE_B_V1_20260912.md
[Q]: PAPER31_QPI_REAL_GLOBAL_TWIST_SOMOS_QRT_SOURCE_PROBE_V1_20260912.md
[Z]: PAPER31_QPI_REAL_ZERO_LYNESS_SOURCE_BRIDGE_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[SRC]: PAPER31_QPI_REAL_TWIST_STRONG_SOURCE_AUDIT_V1_20260912.md
[BR]: https://link.springer.com/article/10.1155/ADE.2005.227
[CGM]: https://arxiv.org/pdf/0912.5031
[BMR16]: https://ddd.uab.cat/pub/caplli/2016/221036/BasManRog2016.Preprint.pdf
