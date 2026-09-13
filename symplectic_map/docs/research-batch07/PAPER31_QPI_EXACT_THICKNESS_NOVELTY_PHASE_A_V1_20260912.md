# Paper31：固定原 T 切片的准确回返厚度——查新 Phase A V1

日期：2026-09-12 UTC；主控撰写。
状态：SCOPE_FOR_CLAIMWISE_NOVELTY_CHECK；不是正式候选准入或项目source/publication lock。
route_applicability: NOT_APPLICABLE。
采用novelty-check的Phase A：将实际已证内容提炼为三项可被先例直接反驳的核心断言，
分别比较方法与发现；不把论文页数、公式数量或独立数学PASS视作新意证据。

## 1. 唯一中心、原对象和不变验收

拟研究中心只有一个：固定原 $T$ 切片的指定截面初始交数，及其在规定基点范围的原迭代固定厚度。
三项断言是同一问题的互补局部部分，不是三个独立论文提案。
沿用原自治映射

$$
F_T(x,y)=\left(\frac T{x-y},\frac xy\right),\qquad T\ne0,
$$

完整八中心曲面去反典范八环的 $\mathcal U$，以及已接受的同基底指定共轭到

$$
W_h:v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\quad O=[0:1:0].
$$

固定原 $z=h-h_*$、$i_n=(nP.O)_{h_*}$，不相交时为零。
不得换回返点、只保留环面点集、用分歧基参数重计长度，或将原时间随变形自由移动。
本阶段不扩展为一般非自治有限阶回返的全相对torsor作用。
Paper31仍需完整正式两席各自四门：新意至少7.5、独立价值至少7.5、完整证明信心至少9，
且可信的22–30页实质英文正文；最后仍需实际完整证明、确定性构建、稿件/PDF独查及终局验收。
当前仅数学输入已接受，不授任一门，不继承Paper30的40页例外。

## 2. 核心断言 V1：原 forcing 控制真实好切触的准确低阶

记 $q=8h-9$、$H=32T+3h$，
$\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$。
保持[G]的原短模型和Hasse系数 $A$、前轮同一 $N_p=q^p\mu(P)$。

在特征零的 $q\delta\ne0$ 上，完整二阶PF算子给原积分的 forcing
$-H/(q\delta)$；正特征另以系数证明

$$
\mu(P)'=-AH/q^2,\qquad N_p'=-q^{p-2}AH.
$$

对任意代数闭特征零域，或代数闭特征 $p>3$、$p\nmid n$，
每个真实有限好切触 $i_n>1$ 准确有 $i_n=2+\mathbf1_{\{H(h_*)=0\}}$。
原 $t_O=-u/v$ 的二／三阶首项也已给出；好点 $q=0$ 不发生此种切触。
全部有限好点的Hasse零阶在其零点上准确为 $1+\mathbf1_{\{q(h_*)=0\}}$；
$q\delta\ne0$ 的 $N_p$ 根阶准确为 $1+\operatorname{ord}_{h_*}A+\mathbf1_{\{H(h_*)=0\}}\le3$。

**需要比较的新发现**：固定本带点切片的显式因子，以及普通／超奇异下消除导数盲区后的准确原接触阶。
**不能申报的新方法**：Manin/PF一般构造、Gauss–Manin还原、移动端点公式、Riemann–Roch、
UV一般complex-Betti精确读阶或正特征局部下界。
**边界**：不定位char0全部真实切触；一般代数闭正特征的 $N_p$ 根未获充分性；
$H=0$ 并非三阶实例的存在证明。
证明供应：[G]267行、[C]281行、[RG]331行；均有准确数学接受。

## 3. 核心断言 V2：全部素域好点的初始交数与全部迭代厚度

对所有 $p>3$、$T\in\mathbf F_p^\times$、$h_*\in\mathbf F_p$、$\delta(h_*)\ne0$，
以闭有限椭圆群点阶 $d=\operatorname{ord}P(h_*)$ 为输入，初始交数已准确确定：

$$
c_*=
\begin{cases}
1+\mathbf1_{\{q(h_*)=0\}},&p\mid d,\\
1,&p\nmid d,\ N_p(h_*)\ne0,\\
2+\mathbf1_{\{H(h_*)=0\}},&p\nmid d,\ N_p(h_*)=0.
\end{cases}
$$

令 $e_*=\operatorname{ord}_{h_*}A\in\{0,1,2\}$，由V1实际给出。
对所有 $n\ge1$，$d\nmid n$ 时 $i_n=0$；否则

$$
i_n=p^{v_p(n/d)}c_*+e_*\frac{p^{v_p(n/d)}-1}{p-1}.
$$

原完整好纤维形式邻域的固定理想就是 $(z^{i_n})$。
**需要比较的新发现**：旧支持充要性之外，固定原截面的 $c_*$ 已被求值；
$p\mid d$ 分支、好点 $q=0$、超奇异及 $p=5,d=10$ 均准确包含。
**必须扣除**：前轮素域充要性、闭有限群点阶/点数作为旧输入；
UV/Broumas兼容Igusa速度、Frobenius/Verschiebung和低阶积分作为标准方法；
Naskręcki Lemma8.2的全倍数传播，以及旧完整equalizer理想。
**边界**：$d$ 未获统一闭式，但未知局部交数不再作答案；
不把“全部素域好点”偷换为所有扩域、任意闭点度数或整个几何基。
证明供应：[C]、[PP]254行、[RP]254行、[SYN]245行、[RS]254行及旧[PF]/[FIX]接受。

## 4. 核心断言 V3：全部有限节点的唯一二阶例外与完整原厚度

对任意代数闭 $k$、$p>3$、$T\in k^\times$、任意有限节点 $h_*$，
从原节点取 $w$ 满足 $T=w^3(w-1)$、$h_*=w(3-2w)$、$w\ne0,1,3/4$。
令 $\zeta$ 是 $(w-1)\zeta^2+(2w-1)\zeta+(w-1)=0$ 的任意根。
若 $\zeta$ 有限阶，以下首项中的 $d$ 指其准确阶，即原 $P(h_*)$ 的乘法阶。
当 $n=p^am$、$p\nmid m$ 时，$\zeta^m\ne1$ 给 $i_n=0$；
相交时 $i_n=p^a$，唯一例外 $p>5,(T,h_*)=(3/16,-2)$ 给 $i_n=2p^a$。
原首项分别为 $d(2w+1)z/[w(4w-3)^3]$、$-3dz^2/3125$。
全部原节点完成理想为 $z^{i_n}(\xi,\eta)$，$z=\xi\eta$；
交数为零时孤立约化节点，正时厚纤维另有长度一嵌入部分。
同一计算在特征零给有限阶节点全部横截，因为二阶候选不是根单位。

**需要比较的新发现**：固定原 $T$ 而非任意两参变形的一／二阶准确系数、唯一例外、
原 $h$ 无分歧性与原带点符号的实际相容。
**必须扣除**：旧节点正规化、乘法群点阶与固定理想；Tate整数级数、标点正常形、形式隐函数和乘法传播。
**凝聚性核对，不另计第四项**：代入节点参数直接得到
$H=w(2w+1)(4w-3)^2$，故节点唯一例外与V1同一原forcing因子相容。
**边界**：特征5该例外为尖点，节点命题不覆盖它；一般 $k^\times$ 中非根单位时全部交数为零；
节点命题不因V2较窄而被缩成素域。
证明供应：[NODE]346行、[RN]338行、[SYN]/[RS]及旧[FIX]。

## 5. 事前比较基线及需要正面处理的最强先例

已有本轮[SA]与[SI]作为来源入口，但Phase B仍须按三核心断言逐项执行，不把旧搜索次数自动挪算。

| 一手先例／本地基线 | 必须扣除／核对的问题 |
|---|---|
| UV，New unlikely intersections on elliptic surfaces，§§2–3、4.7/4.11 | 一般Manin/Igusa/PF的构造、局部界、准确complex-Betti阶与全部端点 |
| Voloch 1990；Broumas 1997；Ulmer 1991 | 正特征显式下降与导数关系、兼容生成元、局部形式机制 |
| Naskręcki 2016 Lemma8.2 | 原 $e_*,c_*$ 已知后的全部倍数公式是标准代入；无需先假设全曲面tame |
| Tate，所用整数级数及同态原文 | 乘法参数、标点归一化及形式隐函数是标准工具，不等于已算原固定T的首项 |
| Gasull–Mañosa–Xarles arXiv1004.5511 §2.2；Hone arXiv2001.09076 | 有标点Tate/Lyness/QRT正常形与群算法已有直接先例；固定T对应两Lyness参数一起变 |
| Ulmer–Urzúa横截性结果 | very general条件及相应域限制，不能用来断言每个固定T切片均横截 |
| Duistermaat QRT/椭圆曲面相关章节 | 目前正文覆盖缺口保留；不得将目录或没找到的章节当排除直接先例 |
| 本地组合基线、碰撞图和[OLD] | 模型、指定点、周期计数、前轮素域充分性、完整固定理想及旧I03原问题均已存在 |

方法新颖性可能低，原族具体发现是否足够非标准仍待查新评价；两者必须分列。
不存在“写出准确系数所以自动高新意”的推论。

## 6. Phase B 与独立评价的固定执行边界

每项至少三种不同查询表述，覆盖可用Web/arXiv、Scholar及Semantic Scholar入口；
最新六个月与2024–2026范围均核对，历史最强先例仍保留。
ML会议数据库与本纯数学问题无关，注明不适用，不造伪检索。
只使用一手论文／作者或官方来源支持数学先例；摘要命中后读实际相关陈述及适用条件。
无需为未访问正文购买资源、绕过权限或下载一份大论文库存；访问失败如实记，不当新意加分。
Phase C/D依技能使用xhigh独立审查；GPT-5.4 MCP未配置时如实使用已授权可用Codex fallback，
不称跨模型验证，不让数学PASS影响新意评分。

本轮三数学独查与合并接受不因这一来源阶段重开。
本Phase A不是正式共同输入manifest，也没有建立论文项目、稿件或任何锁。
source/publication locks、写作、试写测页及PDF构建均仍在完整候选准入之后。
本件只固定这三项实质断言；后续真实新证据若改变其范围，使用明确后继版本，不修改冻结原稿。

[G]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[C]: PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md
[PP]: PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md
[NODE]: PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md
[RG]: PAPER31_QPI_GOOD_CONTACT_INDEPENDENT_V1_20260912.md
[RP]: PAPER31_QPI_PPRIMARY_GOOD_INDEPENDENT_V1_20260912.md
[RN]: PAPER31_QPI_NODAL_SCALAR_INDEPENDENT_V1_20260912.md
[SYN]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md
[RS]: PAPER31_QPI_EXACT_THICKNESS_CONSUMER_INDEPENDENT_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[SA]: PAPER31_QPI_MANIN_CONTACT_ORDER_SOURCE_AUDIT_V1_20260912.md
[SI]: PAPER31_QPI_EXACT_THICKNESS_SOURCE_INCREMENT_V1_20260912.md
[OLD]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
