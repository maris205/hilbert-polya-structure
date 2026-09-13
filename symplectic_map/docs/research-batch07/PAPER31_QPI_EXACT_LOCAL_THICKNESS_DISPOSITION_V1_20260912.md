# Paper31：准确局部厚度、原固定概形消费者与本轮处置 V1

日期：2026-09-12 UTC；主控数学合取记录。
route_applicability: NOT_APPLICABLE。
本件区分新数学接受、标准来源扣除、候选研究价值与最终产物状态。

## 1. 本轮实际改变

前轮[OLD]已接受素域切触支持的充要性和原完整固定理想，但其中初始交数仍未求出。
本轮真正新增的内容是原截面的准确初始交数、统一低阶切触和节点唯一二阶例外，
不是将相同支持判据改名为“厚度”，也没有扩展冻结F5采样。

主控已本人FULL核准四新作者稿[G]/[C]/[PP]/[NODE]与三份fresh非作者数学报告[RG]/[RP]/[RN]。
三报告均终态，逐项PASS，必要数学修正集合为空；当前接受§2的三组准确命题。
新合并作者[SYN]亦经[RS]254行新消费者独查，主控本人FULL核准；
准确命名的上游前提现已全部满足，故合并推论也获数学接受，不重开这三组已接受证明。
全倍数合并及研究价值的不同状态见后续§4–5；不得由作者自评代签。

这仍不是Paper31正式候选准入、正文22–30页容量判断、稿件或PDF验收。
Batch07保持Papers27–30本地接受、4/5；第五篇及跨论文统一审查未完成。

## 2. 已接受的新数学，按准确量词

### 2.1 原forcing、根重数及真实好切触

保持 $W_h:v^2+huv-Tv=u^3-Tu^2$、$P=(0,T)$、原局部参数 $z=h-h_*$。
记 $q=8h-9$、$H=32T+3h$、$\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$。
在 $q\delta\ne0$ 上，原特征零积分的完整Picard–Fuchs式为

$$
\mathcal L\int_O^P\frac{dX}{2Y}=-\frac{H}{q\delta},\qquad
\mathcal L=D^2+\left(\frac{\delta'}{\delta}-\frac8q\right)D
+\frac{8h^3-18h^2+9h-12T}{q\delta}.
$$

独立正特征逐系数证明另给全部 $p>3,T\ne0$ 的

$$
\mu(P)'=-\frac{AH}{q^2},\qquad N_p'=-q^{p-2}AH.
$$

没有把特征零积分方程简单模 $p$ 作为证明。
这里 $A$ 是原短式Hasse系数、$N_p=q^p\mu(P)$ 仍是前轮同一多项式。
所有有限好点的Hasse零阶准确为
$\operatorname{ord}_{h_*}A=1+\mathbf1_{\{q(h_*)=0\}}$（以 $A(h_*)=0$ 为前提）。
在 $q\delta\ne0$ 的每个实际 $N_p$ 根上，

$$
\operatorname{ord}_{h_*}N_p
=1+\operatorname{ord}_{h_*}A+\mathbf1_{\{H(h_*)=0\}}\le3.
$$

对任意代数闭特征零域，或特征 $p>3$ 且 $p\nmid n$，每个真实有限好切触 $i_n>1$ 都有

$$
i_n=2+\mathbf1_{\{H(h_*)=0\}},
$$

原参数 $t_O=-u/v$ 的首项分别为
$-nH_*z^2/(2q_*\delta_*)$ 或 $-nz^3/(2q_*\delta_*)$。
普通与超奇异的Manin最低阶不同；[C]先证明 $i_n<p$ 再读非零首项，独查已核非循环性。
好点 $q=0$ 没有被删去；它不发生所述prime-to-characteristic切触。
本接受不把一般代数闭域的 $N_p$ 根当作真实切触的充分条件，也未证明三阶好切触必存在。

### 2.2 素域好点的全部初始交数

对全部 $p>3,T\in\mathbf F_p^\times,h_*\in\mathbf F_p$、$\delta(h_*)\ne0$，
令 $d=\operatorname{ord}P(h_*)$。已接受初始交数准确为

$$
i_d=
\begin{cases}
1+\mathbf1_{\{q(h_*)=0\}},&p\mid d,\\
1,&p\nmid d,\ N_p(h_*)\ne0,\\
2+\mathbf1_{\{H(h_*)=0\}},&p\nmid d,\ N_p(h_*)=0.
\end{cases}
$$

$p\mid d$ 分支由实际有限étale Igusa标记、兼容生成元和Frobenius扭曲上的水平对数导数证明。
不是把相对微分沿截面误拉为基微分；移动平移两项和 $q=0$ 的一阶零均已核对。
特征5的 $d=10$ 取 $Q=2P$ 后完全包含，没有删去该边界。
闭有限群点阶 $d$ 仍为代数输入，但未知交数 $i_d$ 已从答案中消去。
这不是所有扩域参数或全部几何好能级的充分分类。

### 2.3 所有有限节点的全倍数标量

取任意代数闭 $k$、$p>3,T\in k^\times$，不要求素域。
原节点参数满足 $T=w^3(w-1)$、$h_*=w(3-2w)$、$w\ne0,1,3/4$。
取 $(w-1)\zeta^2+(2w-1)\zeta+(w-1)=0$ 的任意根；
写 $n=p^am$、$p\nmid m$。则

$$
i_n=
\begin{cases}
0,&\zeta^m\ne1,\\
2p^a,&\zeta^m=1,\ p>5,\ (T,h_*)=(3/16,-2),\\
p^a,&\zeta^m=1,\ (T,h_*)\ne(3/16,-2).
\end{cases}
$$

例外特征5是尖点，不在节点域；一般 $k^\times$ 中非根单位时全部交数为零。
若 $\zeta$ 有限阶，以下首项中的 $d$ 为其准确阶，即原节点光滑群中 $P(h_*)$ 的阶。
固定原 $T$ 的Tate展开、$Q_Z=-P$ 的符号及原 $h$ 参数无分歧已获独立核对。
首次相交在非例外节点的首项为
$d(2w+1)z/[w(4w-3)^3]$；
唯一例外处为 $-3dz^2/3125$，二次项确实非零。
特征零的有限阶节点均横截，因为例外根单位将要求
$\zeta+\zeta^{-1}=-4/3$ 是代数整数，矛盾。
这不解决特征零好纤维的全部切触位置。

## 3. 数学身份与实际冻结输入

| 本轮对象 | 行数 | SHA-256 |
|---|---:|---|
| [G] forcing作者 | 267 | c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b |
| [C] 好切触作者 | 281 | 7ec721bfac1d43f214dc9c8b3906c8bab131fe53b67fd6c48e06eeaa752f27aa |
| [PP] p-primary作者 | 254 | 38805df5657731f6698b3fcc3356269cb02da2e2c952779b5750ec6fe8442449 |
| [NODE] 节点作者 | 346 | 5b61cbc732fbd70d6edd1979d183d50081ea1cac3d849164422447c5c785cf27 |
| [RG] forcing／好切触独查 | 331 | 7f7d6f659b69af334a32dca24ae4335ff98965a4de01f4643a56032aeea6b0e1 |
| [RP] p-primary独查 | 254 | a98b8b051cd84952e96b37258570bf926c4e4747fb958b97f2eebcccbf4bc1bc |
| [RN] 节点独查 | 338 | 5db42f335643153a0f97a739b8158a0a6e0de96dbeac35e0a431628fa8d6bfb3 |
| [SYN] 全倍数消费者作者 | 245 | 5400ed2775b3a91f85c814d9c8c8fb252dc91cf8577579f63da0cee87e7539d1 |
| [RS] 新消费者独查 | 254 | ab7282f6ac401239f3c1adad964f76bdeffb1605ec13d5fc4bbaf5de0ba60400 |
| [SA] 第一来源审计 | 192 | 17b7f3175ce52b53c03a3c0540cadb00b59b5067205818a822a1c8d15b2502ed |
| [SI] 新数学来源增量 | 169 | 762643a7bed0a1d54fa074a823d28054811c26373441fc9d7e49e04cb508ded1 |
| [CR] 新增量独立批评 | 207 | 2023cc2066002009b46bb5d95bb6eb6333994cee1f707e908e2faf4f2e1b0c60 |
| [A] 三核心断言查新Phase A | 157 | 171e8aa602d6431e76672c79cf6962c9269f73a6f91993ef7c131a697a4ac917 |

主控对前三份终态独查均本人FULL读取，并以实际文件复核前七项SHA，均与派发／终态一致。
三席互不读取另两组新作者和fresh报告，不同作者辅助不代独立票。
research-review所列GPT-5.4 MCP未配置，实际使用可用Codex xhigh非作者fallback；
没有冒称外部MCP、跨模型复核或正式候选双票。
已有输入[M]/[PF]/[FIX]及旧模型接受只按准确接口消费，不为旧证明再抽票。

## 4. 新消费者与标准来源扣除

[SYN]及[RS]现已主控FULL合取接受：在§2.2全部素域好点范围，令
$c_*=i_d$ 为上面的准确分支，$e_*=\operatorname{ord}_{h_*}A\in\{0,1,2\}$。
$d\nmid n$ 时 $i_n=0$；$d\mid n$ 时准确有

$$
i_n=p^{v_p(n/d)}c_*+
e_*\frac{p^{v_p(n/d)}-1}{p-1}.
$$

好纤维整个形式邻域的原固定理想为 $(z^{i_n})$；
节点处代入§2.3得到完整 $z^{i_n}(\xi,\eta)$，其中原基 $z=\xi\eta$。
$i_n=0$ 在好纤维给单位理想、在节点给约化孤立节点；
$i_n>0$ 在节点另有准确长度一的嵌入部分。
独查只检查新的Cartier／通用对数规范、整系数形式群最低项和合并量词／理想消费者；
其所列[C] C3–C4、[PP] P1、[NODE] Claim及[FIX]前提现由本轮与旧接受完整供应。
没有把有条件消费者票误充对上游的第二次整包认证，也没有遗留未满足的条件。

[SA]192行来源审计已主控FULL核准：Naskręcki Lemma8.2已有精确 $p$ 倍传播；
UV/Broumas已有Manin/Igusa消去及相关局部界，Voloch已有导数桥的通用先例。
主控又本人实读UV Proposition4.7的完整证明和§4.10–4.11的完整移动端点推导；
其一般Manin零阶与最优complex-Betti接触阶关系也须扣除，不能报成新的通用理论。
主控本人实读Naskręcki官方PDF pp.1003–1005的全部Lemma8.2；
其局部低Hasse阶条件不要求先宣布原整个曲面（含尖点／无穷）全局tame。
Tate原文所需整数级数和同态证明已本人实读至PDF第7页相关证明末，不消费未读满射证明。

另本人定向读Gasull–Mañosa–Xarles arXiv1004.5511 §2.2全部Tate正常形换参。
原 $b=T$、$c=1-h$ 可对应Lyness参数
$h_L=-T/(1-h)^2$、$a_L=((1-h)^2+1-h-T)/(1-h)^2$；
固定原 $T$ 不是固定Lyness $a_L$，且该表达有明确被除去的参数，不能据其周期陈述直接冒充本族厚度分类。
仅这段来源比较不解决完整查新，其未读部分不当“无先例”证据。
[SI]169行新增来源补充已主控FULL核准，12条定向查询（其本人8条、只读辅助4条），
未读取本轮fresh数学票。UV/Igusa/Tate/正常形和传播机制覆盖清楚；
上述原族具体因子、初始值和例外在其列明实读范围未见直接陈述，不据此证明首创。
其Duistermaat相关章节正文缺口保持，主控也未取得该正文；
来源席额外读的Ulmer–Urzúa前5页及Hone指定段落不继承为主控FULL阅读。

## 5. 研究价值和下一入口

本轮数学确实改变了前轮批评所依据的输入：在所列范围内，准确初始交数不再缺失。
旧101行批评对旧包的结论保持，但不能直接冒称它已经评价本轮新增厚度定理。
新fresh有界增量批评[CR]207行已主控FULL核准及终态SHA绑定。
其结论为推荐进入定向正式查新及完整brief准备，而非继续停留在旧短接口定位。
主控接受这一有限推进建议：本轮在明列范围中实际消去未知初始交数，
而原参数与同一完整固定概形给出凝聚的单一研究中心。
节点上直接代入 $H=w(2w+1)(4w-3)^2$ 的恒等式还联系两类例外；
此简短核对不另计第四份新定理，也不宣称一般退化理论。
最大的剩余风险是固定 $b=T$ 的有标点Tate/Lyness切片是否已有直接分类，
以及扣除通用机制后是否达到独立研究价值门，不由“计算正确”或“没查到”解决。
[CR]没有读本轮fresh数学报告或[SI]、没有与作者／其它审查者校准。
它不是完整候选四门票，不给新意分或容量PASS，不改原门槛。

已实际新增并本人FULL读回[A]157行，将该唯一中心固定为V1好切触、V2素域初始厚度、V3节点例外。
每项均明列旧输入和通用机制扣除；传播及固定理想消费者不拆成额外创新。
下一未完成项是按[A]执行逐主张Phase B和独立C/D查新、组合增量核对；
之后才准备完整候选brief／必要证明图／共同输入并执行原正式双席四门。
这不是旧包改名复投，亦不代表Phase B或正式准入已经完成。
不建项目、source/publication locks、稿件或PDF，不试写测页；
新数学接受不因后续查新阶段重新表决。
数学工作及有界核查继续使用已有授权；没有新资源、外部协调或用户选择阻塞。

## 6. 阅读、执行及未覆盖边界

主控本轮FULL读取四新作者、三新数学独查、[SYN]、[RS]、[SA]、[SI]、[CR]、[A]、旧[M]446／[PF]325／[OLD]176行，
组合基线121与碰撞图107行；只按问题读取旧接口，不重扫历史构建或总账。
本人外文范围仅以上实际范围及UV §§2–3，不继承代理额外的Ulmer/Broumas/GMX全文身份。
四组新作者／独查的精确CAS属于各执行者；主控书面核准，不冒称本人运行那些调用。
本件不依赖新增有限采样，原F5全部20参数证书及锁保持。

proof-writer使本轮先排除导数不可见首项再读交数，并明确原基参数；
research-lit使一般传播与Manin/Tate机制明确扣除；
research-review提供新证明与新消费者的独立核查，不授研究价值捷径。
novelty-check用于提炼三项实际可查断言并固定后续逐项来源比较，不提前制造查新分数。
所有文件使用apply_patch；一次构造补丁的JavaScript语法错误发生于调用前，未写入半份文件，
随后成功新增[SYN]；一个错误的基线文件名由实际索引更正，未据失败读取作判断。

尚未声称：全部几何好点的充分性、所有扩域、char0全阶异常位置、
尖点全形式理想、无穷边界、一般非自治原torsor的同基作用、$T=0$或新全局点阶分布。
这些不是已接受命题内部缺证，不要求本轮同时闭合所有方向。
无Git初始化、远端同步、投稿、上传、托管、push、发信、付费资源或GPU操作。
冻结作者、旧失败／锁、Papers27–30接受产物均保留。

[OLD]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[G]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[C]: PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md
[PP]: PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md
[NODE]: PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md
[RG]: PAPER31_QPI_GOOD_CONTACT_INDEPENDENT_V1_20260912.md
[RP]: PAPER31_QPI_PPRIMARY_GOOD_INDEPENDENT_V1_20260912.md
[RN]: PAPER31_QPI_NODAL_SCALAR_INDEPENDENT_V1_20260912.md
[SYN]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md
[RS]: PAPER31_QPI_EXACT_THICKNESS_CONSUMER_INDEPENDENT_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[SA]: PAPER31_QPI_MANIN_CONTACT_ORDER_SOURCE_AUDIT_V1_20260912.md
[SI]: PAPER31_QPI_EXACT_THICKNESS_SOURCE_INCREMENT_V1_20260912.md
[CR]: PAPER31_QPI_EXACT_THICKNESS_INCREMENT_CRITIQUE_V1_20260912.md
[A]: PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_A_V1_20260912.md
