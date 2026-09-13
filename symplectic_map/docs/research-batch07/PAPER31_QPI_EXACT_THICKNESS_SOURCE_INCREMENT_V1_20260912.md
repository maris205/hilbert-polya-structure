# Paper 31：固定 T 准确初始厚度的一手来源增量审计 V1

日期：2026-09-12。状态：有界来源审计；不授候选分，不授数学 PASS。
唯一新增产物为本文件；原 192 行 CONTACT_ORDER_SOURCE_AUDIT_V1 保持冻结。
本报告不使用、也未联系本轮三项 fresh 数学检查；四份新稿仅作为待比对的作者断言。

## 1. 本轮真正变化的输入

已按项目入口读取 AGENTS.md、WORKFLOW.md 及 BATCH_07_CONTEXT.md 前 20 行。
research-lit 技能已于本逻辑来源审计轮全文读取并实际使用：定向检索、原文核对、阅读层级和适用域分离。
不做论文 PDF 库存下载、索引、锁修改、外部写入、编译、GPU 或扩采样。
以下四稿均本人 FULL 读取；此前“初始交数尚未给出”的缺口不能原封不动套用到新输入。

| 新作者稿（均在 docs/research-batch07） | 行数 | 本轮待比对内容 |
| --- | ---: | --- |
| PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md | 267 | 固定 T 的 forcing；H=32T+3h；N_p 导数分解 |
| PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md | 281 | 实际 prime-to-p 好切触的准确 2/3 阶及首项；好点 Hasse 阶 |
| PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md | 254 | F_p、p 整除初始返回阶时的 i_d=1+1(q=0) |
| PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md | 346 | 全部有限节点的准确初始阶；唯一二阶异常及首项 |

固定对象为 W_h: v²+h u v−T v=u³−T u²，T≠0，P=(0,T)。
记 q=8h−9，H=32T+3h，δ=h⁴−h³−8Th²+36Th+16T²−27T。
这里 q 不等于节点稿中的 Tate 退化参数；以下使用 q_Tate 区分。
i_n 指原指定截面与 O 在指定底点的交数，而不是允许另选 Betti/Igusa 截面的最大接触阶。
以下“原文未见”只限定于报告列出的实读范围，不是无先例或新颖性的证明。

## 2. 结论矩阵：通用机制已知，原族数值须分开核验

| 新输入 | 最强已实读先例 | 本轮来源判定 |
| --- | --- | --- |
| Abel 积分的二阶算子、移动端点 correction | Ulmer–Voloch §4，特别 Prop. 4.7、4.11 | 一般微分读阶和端点修正已直接覆盖；不是新机制 |
| 原族 forcing −H/(qδ)，N_p′=−q^(p−2) A H | 同上给计算框架；§2–3 给正特征 Manin/Igusa 背景 | 在所读处未见原固定 T 的这两个显式分解 |
| 实际 prime-to-p 好切触 i_n=2+1(H=0) 及原坐标首项 | 特征零 Manin/Betti 精确阶关系；正特征下界 | 不能把一般最大接触阶关系直接等同原指定 nP；未见此原族分类 |
| F_p 好点 p∣d 时 i_d=1+1(q=0) | Ulmer–Voloch §3 的 compatible Igusa 速度公式与 Frobenius/Verschiebung 结构 | 结构输入已知；所读处未见该固定截面的准确初始数值 |
| 节点实际 prime-to-p 返回：仅 (3/16,−2) 可二阶（p>5）、其余一阶 | Tate 群均匀化、QRT/有标点正常形文献 | 乘法群及坐标工具已知；未见固定 T 切片的该异常与首项 |
| 初始 i_d 与局部 Hasse 阶已知后的全 n 传播 | Naskręcki Lemma 8.2 | 在局部条件成立时直接属于已有公式；不得独立计为新票 |

本轮没有找到可把“原族准确厚度全部已经逐字发表”作为结论的原文。
同样，也没有取得足以把该原族显式内容判为新颖的穷尽证据。
特别是通用正常形可覆盖本族，不等于文献已经计算过沿固定 T 的底参数接触阶。

## 3. 微分 forcing 与实际 2/3 阶：先例覆盖到哪里

[Ulmer–Voloch, New unlikely intersections on elliptic surfaces](https://arxiv.org/html/2508.06680v1) 的 §4 是本轮最强直接先例。
本人新增实读 §4 的 4.4–4.11 编号段落，包括 Prop. 4.7 与 Prop. 4.11 的完整证明；§§2–3 已于前一审计 FULL 读。
Prop. 4.7 在其特征零正规化及排除集 S 之外，给出 Manin 值零阶 J 与最优 complex-Betti 接触阶 I 的 J=I−2。
Prop. 4.11 明列移动积分端点的导数项，故“二阶非齐次 Picard–Fuchs 算子控制接触阶”不能再作为独立新机制。
其 I 是可选择水平/Betti 对象的接触量；不能未经论证替换成本稿固定 nP 的 i_n。
Remark 4.8 的例外位置也不允许删去后声称任何底点均有同一精确等式。

新 forcing 稿主张 L I_P=−H/(qδ)，并以原族 Gauss–Manin 约化和完整端点项计算它。
正特征稿另以有限系数计算主张 μ(P)′=−A H/q²、N_p′=−q^(p−2) A H。
这不是仅引用 char 0 解析积分后直接模 p 约化；来源比对应保留两种论证的区别。
在上述实读原文中未见 q=8h−9、H=32T+3h 或此固定 T 的 N_p′ 分解。

新好切触稿的待核作者结论是：实际发生的 prime-to-p 好切触 i_n>1 满足 q≠0，且 i_n=2+1(H=0)。
原参数 t_O=−u/v 的二、三阶首项分别为 −nH/(2qδ) 与 −n/(2qδ)。
报告没有把任意 N_p 根都当成代数闭域上的实际返回，也不补加“所有根均实现”的断言。
正特征中先排除导数不可见的高阶分支、再读取准确阶，是作者证明必须承担的步骤。
旧的 Manin 下界和 Cartier 限制本身不完成这一上界论证。

[Ulmer–Urzúa, Transversality of sections on elliptic surfaces](https://dlulmer.github.io/research/papers/2022.pdf) 本人读 PDF 第 1–5 页，包括定理陈述而非全部证明。
Thm. 1.7 对 very general Weierstrass 系数与指定点给 prime-to-p 横截性、I_1 坏纤维等结论。
“very general”不能转换为所有固定 T 切片；其小有限域适用限制尤其不可省略。
它是强横截性背景，不直接排除或计算本族特殊参数处的 2/3 阶。

## 4. F_p 的 p-primary 初始交数：结构先例与原族输入

新作者稿主张：F_p 好点若 p∣d，则 i_d=1+1(q=0)，而非仅给传播式。
其路径使用真实有限 étale Igusa 邻域、与 Hasse 根兼容的 ker V 生成元，以及 F(mP)−Q_0 的水平速度。
Ulmer–Voloch §3，尤其式 (3.1)，已给 compatible Igusa 截面的速度微分表达；这部分不是新的下降结构。
Frobenius 扭曲曲线的群律定义在 p 次幂常数上、V 在普通地方 étale，也属于此标准背景。
新稿真正需要原族计算的是：该速度在本切片的零阶为 1(q=0)，并确实对应原指定截面的初始返回。
在所读 UV 原文中未见此 q 因子结论及 i_d=1+1(q=0) 的原族公式。
有限素域给出的 A(h_*)=1、局部普通性和可能的 d 范围，是新稿的适用条件，不能删去后宣称代数闭域一般充分性。
以上仅登记作者的具体数学任务，不引用本轮独立检查结果替它验收。

## 5. 全 n 传播：Naskręcki 的标准公式足够强

[Naskręcki, Divisibility sequences of polynomials and heights estimates](https://nyjm.albany.edu/j/2016/22-46v.pdf)，NYJM 22 (2016), 989–1020，Lemma 8.2。
本人在同逻辑审计前段已 FULL 读印刷页 1003–1005 的引理、条件及证明；本轮沿用未变原文，不伪报重读全文。
设 E 的泛纤维普通，m 是该地方首次正交数的指标，h_v 是最小模型 Hasse 系数的局部阶。
在所评地方 h_v≤p−1 时，m∣n、e=v_p(n/m) 给

    i_n = p^e i_m + ((p^e−1)/(p−1)) h_v；m∤n 时 i_n=0。

这里的 ordinary 是泛纤维条件，不要求每个特殊纤维都普通。
例如非恒定 j 的特征 p 椭圆曲线具有普通泛纤维；特殊超奇异点仍可由 h_v>0 进入公式。
应用某一有限地方的低阶分支，不必先证明包括无穷远在内的整条曲面处处 tame。
故不能因无穷远尚未分析就抹掉该局部传播先例，也不能由有限地方结论声称全曲面所有地方已覆盖。

若新作者稿的好点 Hasse 阶 h_v=0、1、2 及节点 h_v=0 均经数学核验，则 p>3 时这些地方直接满足条件。
此时全 n 的几何级数传播是已有结果的代入；新增负担是原族 h_v、m、i_m 的准确输入。
超奇异处 h_v>0 时不可擅自简化成 i_n=p^e i_m；p-primary 好点和节点 h_v=0 才有该简化。
本引理不计算首次交数，因此不能反向声称它已包含本族 2/3、1+1(q=0) 或节点例外。

## 6. 节点准确阶：Tate 工具与固定 T 消去必须分离

[Tate, A review of non-archimedean elliptic functions](https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf) 是本轮直接读取的均匀化来源。
本人读 PDF 第 1–7 页：整数系数的 x、y 与曲线系数展开，以及乘法群映入 Tate 曲线的群同态证明；未读完全文。
其中 q_Tate 展开和群同态足以覆盖“n 倍点在乘法参数中取 n 次幂”的通用机制。
特征 p 中 (Z^m−1)^(p^a) 的乘数效应不属于新局部动力学结论。

新节点稿沿固定 T 反解 Z(q_Tate)，而不是让 T 随 q_Tate 自由变化。
作者通过一阶系数的 3ζ²+4ζ+3 消去定位唯一二阶参数 (3/16,−2)。
该处二阶非零量为 −125/81，原 t_O(dP) 的 ε² 首项为 −3d/3125；适用 p>5。
p=5 时该参数是尖点而非节点，不能套用节点二阶结论。
在 T=w³(w−1)、h=w(3−2w) 的节点参数化下，一般首项 d(2w+1)/(w(4w−3)^3) 及特征零该异常不对应有限阶乘法点，也是作者的新具体断言。
上述 Tate 实读范围没有直接给出这些固定 T 消去、异常参数或原坐标首项。
因此应扣除工具与 prime-to-p/p-primary 传播机制，但不能把来源中的通用展开直接标为已发表的原族结果。

## 7. 同一有标点正常形的直接先例及边界

[Gasull–Mañosa–Xarles, Rational periodic sequences for the Lyness recurrence](https://arxiv.org/pdf/1004.5511) 本人读 PDF 第 1–9 页，特别 Thm. 3 与 §2.2。
§2.2 使用 E(b,c): Y²+(1−c)XY−bY=X³−bX²，指定点 R=(0,0)，并给出到 Lyness 曲线的显式变换。
其参数关系为 h_L=−b/c²、a=(c²+c−b)/c²；在适用开集上，本族对应 b=T、c=1−h、P=−R。
因此“有标点 Tate 正常形与 QRT/Lyness 的联系”已有直接先例，不应作为本轮新发现。
但固定 b=T 随 h 变化对应 Lyness 的 a 与 h_L 同时变化，不是固定 Lyness 映射参数 a 的同一纤维切片。
c=0 及小阶点还需尊重该文 n≥5 正常形陈述的开集条件，不能无条件跨过。
所读部分研究周期、参数化和奇异有理曲线动力学，未见上述固定 T 初始交数及唯一二阶异常的计算。

[Hone, ECM Factorization with QRT Maps](https://arxiv.org/pdf/2001.09076) 本人读 PDF 第 7–10 页的 §§4–6 与 Thm. 1；只读代理报告不能算本人阅读全文。
其中 Somos-4、Somos-5、Lyness 曲线及有标点 Weierstrass 变换直接覆盖一般 QRT 表示和倍点算法背景。
所读内容没有给本轮固定 T 的准确初始厚度分类；算法和正常形覆盖不等于沿特定底参数的交数计算。

Duistermaat, Discrete Integrable Systems: QRT Maps and Elliptic Surfaces 的相关 §§7.4–7.7 本轮未取得正文。
代理对官方书/章节及目录入口的尝试失败；未绕过访问限制，也未把旧目录线索伪称 FULL 阅读。
这是有界覆盖缺口，不能宣称已排除该书的直接先例；不因此扩大到全领域搜索。

## 8. 实际阅读层级与定向查询账

本来源审计代理本人：四份新作者稿全部；UV §§2–3（前段沿用）与 §4 中 4.4–4.11 编号段落（本轮）；Ulmer–Urzúa PDF 1–5 页；Tate PDF 1–7 页。
本人另读 Naskręcki 引理及证明（前段沿用）、Gasull 等 PDF 1–9 页、Hone PDF 7–10 页；均未声称整篇 FULL。
只读来源子代理 exact_thickness_qrt_primary：Hone PDF 1–10 页；Carstea–Takenawa arXiv:1005.3586v2 的摘要及指定词段，非全文。
后一材料中的重数涉及判别式、基点或 Halphen 指数，不直接充当本轮 i_n 的先例；本人未追加全文读取。
Carstea–Takenawa 仅为候选筛查记录：[arXiv 原始入口](https://arxiv.org/abs/1005.3586)。
未把不同族 Igusa 样例、very general 曲面或普遍正常形等同本固定 T 指定截面。

本轮共 12 条定向查询，8 条本人、4 条只读代理；不追加原 192 行报告的旧有限表。

1. `"Tate normal form" "Picard-Fuchs"`
2. `"Tate normal form" "tangencies"`
3. `"elliptic" "32" "3h" "Manin"`
4. `"q-Painlevé I" "intersection" multiplicity`
5. `"Tate normal form" "ramification" "b"`
6. `"elliptic" "8h-9"`
7. `"Tate normal form" "32" "3" "differential"`
8. `"Rational periodic sequences for the Lyness recurrence" arxiv`
9. `Duistermaat "Discrete Integrable Systems" "7.4" "7.7"`
10. `QRT "3/16" "multiplicity" elliptic`
11. `Duistermaat Discrete Integrable Systems QRT Maps Elliptic Surfaces Springer periodic points singular fibres`
12. `site:arxiv.org QRT "intersection" "multiplicity" nodal`

查询命中不自动构成阅读证据；其余不相关命中未扩展为综述条目。
UV v1 入口的提交时间与正文显示时间不同，本报告用明确版本入口，不擅自统一成新版本出版日期。
Tate 文本最终期刊书目信息未在本轮核定；只给实际读取的作者托管文本，不补造年份卷页。

## 9. 输入指纹与交付边界

四稿 SHA-256，顺序同第 1 节：

    c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b
    7ec721bfac1d43f214dc9c8b3906c8bab131fe53b67fd6c48e06eeaa752f27aa
    38805df5657731f6698b3fcc3356269cb02da2e2c952779b5750ec6fe8442449
    5b61cbc732fbd70d6edd1979d183d50081ea1cac3d849164422447c5c785cf27

原冻结 192 行来源审计 SHA-256：17b7f3175ce52b53c03a3c0540cadb00b59b5067205818a822a1c8d15b2502ed。
本轮可交接的准确结论是：一般微分/Igusa/Tate/传播结构已有强先例；四稿现已提出具体原族初始交数，必须按实际新输入检查。
固定 T 显式内容未在列明实读处找到直接陈述；其数学正确性、可实现性与研究增量仍分别需要证据，不能由检索空白替代。
