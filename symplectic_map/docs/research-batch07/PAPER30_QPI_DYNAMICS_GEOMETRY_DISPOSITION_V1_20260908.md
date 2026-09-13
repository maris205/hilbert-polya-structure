# Paper30 qPI：实际纤维、Jacobian、准确坏值与全部轨道的接受处置 V1

日期：2026-09-08。主控：`/root`。
科学状态：`PROVED_AND_INDEPENDENTLY_CHECKED`，限于以下精确对象与量词。
候选／产物状态：`NOT_FORMALLY_EVALUATED / NO_PROJECT / NO_MANUSCRIPT / NO_PDF`。
Batch07 仍为本地验收 **3/5**；Paper30 未立项，Paper31 未开展。

## 1. 本轮数学结论

本轮从[已接受的四项基础](PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md)
继续，新增 F、J、R、O、B 五份完整证明及五份真正非作者报告。
十份文件均已由主控全文读取，最终身份逐项吻合；新论证没有未解决的硬缺口或必需修正。
原四项基础未变，没有重复开启数学审查。

在 JR 原模型和原积分上，本轮已经闭合：

1. 所有有限纤维的几何整性、约化性及奇异纤维的有理正规化；实际临界长度恰为四。
2. 泛动力纤维与循环谱商的准确 Jacobian／torsor 身份，不只是同亏格或未知核同源。
3. 真实紧曲面与完整初值空间上的同构、回返的泛非挠平移及所有有限光滑纤维上的平移。
4. 全部有限域、全部合法状态的 Hasse 上界及原始 ceiling 分箱，包含奇异状态。
5. 实际临界乘法特征多项式与 JR 四次式的强等式，包含重根和非约化局部长度。

因此，所实际读取的 [JR 作者 v2](https://arxiv.org/html/2508.18578v2)
中 Conjecture 1.2.A/B 与 Conjecture 3.6 已在上述原对象上获得完整证明。
这不是宣称 JR 文中其他问题、后继不同方程或全部 Painlevé 猜想均被解决。
五个模块属于同一科学问题，不是五篇论文，也不是五张完整候选评价票。

内部算术包的[完整 V2 四门 FAIL](PAPER30_TWIST_INTERNAL_ARITHMETIC_FORMAL_CANDIDATE_DISPOSITION_V2_20260908.md)
保留，未重投或改写。本轮 qPI 是新的族内问题，不是旧内部算术的重新分组。

## 2. 精确对象、量词和接受范围

### 2.1 原曲面与全部有限纤维

设 $k$ 为任意特征代数闭域，$s,t\in k^*$，$s$ 的精确有限阶为 $r\ge1$。
正特征 $p$ 自动有 $p\nmid r$。原一步为

$$F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad t\mapsto st.$$

采用 JR 的原 Laurent 积分 $I_r$、实际八次吹起 $S=S_{t,s}$、
反典范八环 $D=-K_S$ 以及完整初值空间 $U=S\setminus D$。
此前接受的 $(I_r)_\infty=rD$、法丛精确阶 $r$、原完整 pencil 和泛光滑均保持。

本轮进一步证明每个有限概形纤维 $f^{-1}(c)$，$f=I_r$，均射影、几何整、约化、算术亏格一。
若它不光滑，恰有一个几何奇点，正规化是 $\mathbb P^1$；没有可约有限层或有限重纤维遗漏。
奇点为节点或尖点；小特征的临界概形长度保留其实际定义，不套用特征零计数表。

关键实际几何计算是在标记整数 Picard 格中求得边界正交格的完整秩二基，
Gram 矩阵为 $\left(\begin{smallmatrix}-8&8\\8&-8\end{smallmatrix}\right)$。
有限不可约分量的算术亏格非负迫使其类为正整数倍 $D$；
最小完整 pencil 排除小于 $r$ 的倍数，遂得到单一重数一分量，CM 排除嵌入分量。
这个论证对每个固定 $t\ne0$ 直接成立，不从一般参数稠密性推特殊参数。

### 2.2 谱商是实际泛 Jacobian

令 $K=k(c)$、$T=t^r$、$\varepsilon=(-1)^{r+1}$。原泛动力曲线 $X/K$ 的 Jacobian 是

$$E:\quad\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0,$$

以 $(Z,\lambda)=(0,0)$ 为原点取光滑射影模型；$X$ 在原 $K$ 上具有 $E$-torsor 结构。
此结论亦按作者 J 的下降证明适用于定义参数的非代数闭基域。
不假设或宣布 $X(K)\ne\varnothing$。

原 $z$ 谱曲线 $C$ 的亏格是 $2r-1$，不是实际 $X$ 的亏格。
循环商是 $Z=z^r$；$r>1$ 时有四个全分歧点，$r=1$ 为恒等覆盖。
J 补齐特征二的谱模型论证，因此当前泛 Jacobian 结论覆盖所有允许特征，
不再局限于旧 S 的非二特征四次平方模型。

实际谱线丛 $L$ 给 $X\to\operatorname{Pic}^{2r}(C)$；
端点系数 $M_{2r},M_{2r-1},M_0$ 恢复原动力坐标的有理逆，排除纯不可分次数漏洞。
$A:L\dashrightarrow\sigma^*L$ 的循环复合是乘以 $\lambda$，不是恒等线性化；
其固定除子差使像落入不变 Picard 的一个陪集。
全群固定点排除 $\pi^*$ 的核，tame 不变切空间给出正确维数，
从而得到实际 $K$-torsor 身份，而不是从相同亏格猜出同构。

### 2.3 准确坏值及非约化临界重数

在实际 $U$ 上令 $Z_{\rm act}=Z(dI_r)$，$A_{\rm act}=\Gamma(Z_{\rm act},\mathcal O)$。
它是长度四的有限概形。以形式变量 $C_0$ 区分原基底 $c$，则

$$
\begin{aligned}
R_{r,t,s}(C_0)&=\det(C_0\operatorname{id}-m_{I_r}\mid A_{\rm act})\\
&=\delta(C_0,T)\\
&=C_0^4-\varepsilon C_0^3-8TC_0^2+36\varepsilon TC_0+16T^2-27\varepsilon^2T.
\end{aligned}
$$

特别地，对每个有限 $c$，

$$f^{-1}(c)\text{ 光滑}\quad\Longleftrightarrow\quad\delta(c,t^r)\ne0.$$

非根处几何亏格一，根处正规化亏格零。无穷远概形纤维仍是 $rD$，不在此有限判据中。
此等式涵盖特征 $2,3$、所有特殊非零 $t$ 及临界碰撞。

B 在原 $c$ 上给出长 Weierstrass 模型

$$W:v^2+cuv-\varepsilon Tv=u^3-Tu^2,\qquad\Delta_W=T^3\delta(c,T).$$

$W$ 的总空间正则且每个有限纤维整约化。
在每个原有限 DVR 的 henselization 上，实际光滑点提升为截面；
结合 J 的泛 torsor 身份和双方最小正则性，得到保持原 $c$ 的模型同构。
这不是仅由泛 Jacobian 同构推断特殊纤维相同。

内禀 $\operatorname{Fitt}_1\Omega_{U/\mathbb A^1}$ 正是实际 $Z(dI_r)$ 的理想。
同基底模型同构及 henselization 的有限阶商不变，保留每个非约化 Artin 块和乘以 $c$ 的算子。
$W$ 的完整临界代数为

$$k[z]/((T-z^2)^2-\varepsilon Tz),\qquad c=\varepsilon-z-z^3/T.$$

四维乘法矩阵直接给 $\delta$。没有凭相同零集／四次次数补推重数，也不需要新建 $t$ 族平坦模块。
最小整 Weierstrass 判别式与实际临界多项式相差单位 $T^3$；二者定义不同。

### 2.4 真实回返与所有有限域轨道

令 $\mathcal R=F_{s^{r-1}t}\circ\cdots\circ F_t$。
一步已在全部 $U$ 和紧曲面上证明为同构，包含原环面分母零及四末端直线的全部出口。
整数 Picard 作用给

$$\deg_{(x,y)}\bigl((\mathcal R^{8m})_x\bigr)
=(16r^2m^2+2rm+1,\;16r^2m^2),\qquad m\ge1.$$

这里是整数交数，不在特征 $p$ 中取模。
故泛曲线上 $\mathcal R$ 为非挠平移；在每个有限光滑几何纤维上仍是平移。
非挠是函数域结论，不能误报为有限域中存在无限轨道。

现在取任意 $q=p^e$、$s,t\in\mathbb F_q^*$。
完整状态是 JR 的原环面及四条附加直线，并包含时间坐标；不删去奇异点。
任意最小一步周期 $m_\gamma$ 必被 $r$ 整除，
$\ell_\gamma=m_\gamma/r$ 恰是固定时间切片上的回返最小周期。

光滑层有 $\ell_\gamma=\operatorname{ord}(P_c)\mid\#\operatorname{Jac}(C_c)(\mathbb F_q)$。
奇异层的唯一奇点在原域上且被回返固定；其余实际周期经正规化保持不变，
于是 $\ell_\gamma\mid(q-1)$ 或 $\ell_\gamma\mid(q+1)$，或 $\ell_\gamma=p$。
尤其没有把非素域中的幺幂阶错误写成 $q$。

置

$$N_\pm=q+1\pm2\sqrt q,\qquad
M_q=\left\lceil(\sqrt q+q^{-1/2}-2)/4\right\rceil.$$

全部轨道都有 $\ell_\gamma\le N_+$，且恰落在原分箱之一：

$$B_j^{(q)}=\begin{cases}[N_-/j,N_+/j],&1\le j<M_q,\\
[1,N_+/M_q],&j=M_q.\end{cases}$$

相邻闭箱严格不交；$M_q=1$、特征二、$p\ne q$ 和唯一奇点轨道均已单列核查。
这是原 Conjecture 1.2.A/B 的全部合法状态范围，不是光滑层短推论。
O 的证明只消费 F 的纤维分类及 R 的动力结论，不依赖 J 或 B，整条链无循环。

## 3. 五对冻结证据与接受合取

| ID | 作者输入／行数 | 作者 SHA256 | 非作者报告／行数 | 报告 SHA256 |
|---|---|---|---|---|
| F | [实际有限纤维](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md)，466 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` | [F 独审](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_NON_AUTHOR_REVIEW_V1_20260908.md)，238 | `2b55ec53c0f677922eaf3d1f184c7066bd351ac5e5afd59f6d4a73f2b78f3bfb` |
| J | [泛 Jacobian 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md)，492 | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` | [J 独审](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md)，257 | `c7d355d420e966381dfc74fffbd033470e12158480a826e0d88e464a5fa40438` |
| R | [真实回返](PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md)，368 | `9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c` | [R 独审](PAPER30_QPI_RETURN_TRANSLATION_NON_AUTHOR_REVIEW_V1_20260908.md)，253 | `59ca105cc2a8a3d47218ede2fb85daaa261ae94f2d8988680edec9b2a69ec159` |
| O | [全部轨道及分箱](PAPER30_QPI_ALL_ORBIT_HASSE_BINS_ENTRY_V1_20260908.md)，298 | `78191a3faa7d2a867e45eccd708b106b722d43e6f5ea73d583e0385637be2469` | [O 独审](PAPER30_QPI_ALL_ORBIT_HASSE_BINS_NON_AUTHOR_REVIEW_V1_20260908.md)，159 | `83cb3658e51261497eff16decc48a3f6fef99d95f6ac5d63d84cb4d7e8e9076c` |
| B | [准确坏值强等式](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md)，488 | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` | [B 独审](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md)，259 | `1bb3d563bdb5a2c93aa517002f69ac72398688ee74429a8b4d8662965c229815` |

F 的五项主张、J 的完整泛桥及 R 的五项主张均经指定非作者核查 PASS。
O 的十七项消费者检查均 PASS；其中单列的 F/R 输入验收 `CONDITIONAL`
现由本表精确同哈希 F、R 的另两份真实独审关闭，不是尚缺一个数学假设。
B 的十六项新增检查全部 PASS，CONDITIONAL=0、FAIL=0；J/F/G 只消费既有接受合同。
主控全文阅读十份文件并作上述依赖合取，没有拿作者自评代替独立接受。

各报告由未参与对应目标稿的独立实例完成，不读取其他数学投票来产生自己的消费者判定。
当前实际工具为可用 Codex 独立代理，沿用 `research-review` 的 xhigh 要求；
不冒称未配置的 GPT-5.4 MCP、人类评审或跨模型认证。
作者稿最后的 regular／normal 术语统一及 CM 一句补充在 B 冻结独审前完成；
最终被审对象就是本表 488 行身份，不存在投票后替换作者字节。

旧 F 中 $r>1$ 的 $R=\delta$ 开放接口、旧 J 的有限坏值边界、
旧 O 不宣布 Conjecture 3.6 的快照、旧首关处置的下一项均完整保留。
它们的当前数学状态由本轮新证明与本处置接续，不追改旧文件或旧审查结论。

## 4. 查新已有实质证据，但尚不是候选通过

本轮完成[Phase A/B 定向来源包](PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md)
（268 行，SHA256 `4470af64294525bc4ae33b9b00fc38c44c38215290a36fa6f3a5b6bdf861f90e`）
及[准确坏值来源补充](PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md)。
主控已全文读取两件；查新后续独立核查另行进行，没有在本处置投正式新意票。

已明确必须扣除的强先例：

- JR 的原映射、初值空间、显式积分、谱方程、四次候选式及原分箱。
- JRV 2006 的光滑平移层 Hasse 周期窗口和同一个相邻窗口重叠阈值；
  Hasse 上界、有限群元素阶和 $\operatorname{PGL}_2$ 分类本身不是新理论。
- Cantat–Dolgachev 的全特征 Halphen／法丛阶理论、Carstea–Takenawa 的复数根单位机制，
  以及 Mizuno 2024 已列出的同型秩二边界正交格。
- Beauville 谱对应和 IVY 2015 的循环谱约化、商 Jacobian 与拉回单射性。
- 标准最小正则模型唯一性、局部截面、Fitting 基变换和 Weierstrass 判别式变换。

能够定位的候选差额是这些机制对实际 JR 曲面、原积分与原参数的完整识别，
覆盖全部有限阶、每个非零固定参数、全部特征和所有奇异／非奇异状态。
这仍须判断是否具有足够独立科学意义，不能仅凭“全特征”标签、模块数或证明通过来加分。

主控已定向读取 JRV §5、IVY §4.2–4.4、Mizuno 对应附录、
JR v2 原猜想及 2026-07-08 后继论文的相关工作。
后者仍称原 qPI 一般椭圆性为猜想，是近期一手线索而非全球无后继证明证书。
出版版 JR 全文未取得；Conjecture 3.7 更号和新增形式 Lax 警告只据公开索引。
Beauville 本轮不同作者／检索实例的实际可读范围也如各自文件记录，不能合并成每人均全文读过。
全球新意和完整引文覆盖仍为 `UNCERTAIN`。

## 5. 接续与产物边界

下一项是同一完整 qPI 候选的查新后续、组合内非碰撞、准确证明依赖图与正式双份四门判断。
在当前已接受输入不变的情况下，不重开这九项已通过数学模块；
若新组织产生真正的新推理或发现硬缺口，再针对实际变更审查。
独立查新意见和组合事实核查都不是两份完整候选票。

两位全新互盲完整评审各自仍须满足：新意至少 7.5、独立科学价值至少 7.5、
完整证明信心至少 9，并判断在既定匿名英文单栏 11pt、letter、四边 1 inch、标准行距下，
全部必要证明保留正文时，有可信的自然 22–30 页实质正文；参考文献另计。
容量须去重真实依赖、分别看上下界风险；低／中／高是预测，不是实测或严格下界。
不平均或拼接两票，不另加“central 必须落窗”的通用规则。

尚未立项、建 source/publication locks、写英文论文或试写测页；
Paper29 的特定实测许可不迁移。本轮不触发 Riemann／Hilbert–Pólya Route 评价。
所有成果仅本地，无投稿、上传、托管、push、发信或其他外部效力。
数学猜想关闭不计作第四篇论文完成；五篇目标继续保持，终局跨论文审查尚未到阶段。

本次静态验证仅覆盖十个新数学对象的行数／SHA256和新增处置的直接链接，
不重扫旧构建树。静态一致性不替代上述全文证明检查、查新或将来的真实 PDF 验收。
