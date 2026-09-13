# Paper30 qPI：垂直临界理想与完整首 jet 的 Phase A

日期：2026-09-09。主控 `/root`。
类型：新的问题范围和查新主张提取；不是正式候选 brief、四门票、立项或写稿。
使用 novelty-check 的 Phase A；route_applicability: NOT_APPLICABLE。
Batch07 保持 3/5；Paper30 未立项，Paper31 未开展。

## 1. 与旧失败及原诊断问题的关系

本轮中心是原整除状态微分的**两方向垂直临界理想**，
不是旧整数 C1–C3 的标题变更、更多模 $p$ Hasse 次幂，或有限域周期公式的重投。
旧整数 C3 只决定 $\bar\alpha=H^\sigma dJ$，没有决定其首切向系数或闭点提升阶。
现在出现原 $L_m$ 障碍到该切向类的实际箭头，以及全剩余阶的二阶理想。

旧整数完整 V1 两票新意 7.3 的 FAIL、旧 qPI T1–T7 完整 V2 的双份 FAIL 均保持。
旧数学接受不撤销，也不因作为本轮依赖而重新计作新发现。
本轮不是对相同字节重抽正式票；是否有足够独立价值与自然容量仍待新问题的完整查新和评价。

[发散 P03](PAPER30_QPI_POST_INTEGRAL_IDEATION_PROPOSALS_V1_20260909.md) 曾提出所有高度的完整厚度问题，
也允许找出最初的 jet 障碍。该发散不是用户锁定的待交付定理。
本件准确冻结目前已得或正在最终核查的边界：首层原完整理想与高层模平方理想。
**所有高度的完整厚度尚未解出**，不把它悄悄改称已解决；不能据本件完成五篇目标。
特征二实际混合项是非单项式首 jet，而不是已证明的全形式正规形分类。

## 2. 原对象及共同量词

沿用原八截面曲面 $S/R$、反典范八环 $D$ 与 $\mathcal U=S\setminus D$，
$R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$，末次四中心坐标为 $1,\tau,\tau,q$。
原矩阵、降序乘积及能级规范固定：
$$M_r(z)=A(s^{r-1}z)\cdots A(z),\qquad
I_{r,s}=[z^r]\operatorname{tr}M_r(z).$$
不使用只具有相同特征多项式的替代矩阵，不以新的谱曲线代替原完整能级。

令 $p$ 为任意素数、$m\ge1$ 且 $p\nmid m$，$a\ge1$，$N=p^a$。
取无分歧 $p$-进 DVR $\mathcal O_0$，含精确 $m$ 阶单位根 $\widetilde\eta$，
令
$$\mathcal O_a=\mathcal O_0[\zeta_{p^a}],\quad
\pi_a=\zeta_{p^a}-1,\quad s_a=\widetilde\eta\zeta_{p^a},\quad
t_a\in\mathcal O_a^\times,\quad \alpha_{mN}=p^{-a}d_{\rm state}I_{mN,s_a}.$$
高层比较的剩余域 $k$ 为有限域；首层 TH 另已证明完美剩余域版本。
允许完成、有限无分歧扩张及由忠实平坦性回到原圆分局部 DVR；不擅自增加有分歧状态。
微分只取两个原状态方向，固定时间、单位根和底环。

在同一剩余小阶模型上写
$$\eta=\bar s_a,\qquad J=I_{m,\eta}(x,y;\bar t_a),\qquad
T=\bar t_a^m,\qquad \varepsilon_m=(-1)^{m+1},\qquad
\sigma=(p^a-1)/(p-1).$$
原 Hasse 多项式为
$$H=H_p(T,J;\varepsilon_m),\qquad
H_p(T,h;\varepsilon)=[Z^{p-1}]
\bigl((T+hZ+Z^2)^2-4\varepsilon Z^3\bigr)^{(p-1)/2}$$
对奇 $p$ 成立；$H_2(T,h;\varepsilon)=h$。
称超奇异时必须保留原完整光滑能级与实际 Jacobian／Hasse 的已证明识别链。
仅仅看见相同四次式不是该识别；必要正文证明不能因此删除。

$\mathfrak c(\alpha)$ 是原秩二相对余切模的全部系数理想。
讨论局部理想时取原完整光滑有限能级 $X=(J=h)$ 的任一点，
包括四条末端线；若 $h$ 是 Hasse 的 $e_h$ 重根，不默认 $e_h=1$。
一形式因子分解本身的范围更广，不要求能级光滑或 ordinary。

## 3. 三个核心查新主张

### V1. 指定截面障碍控制全部首层完整临界理想

对所有 $p,m$、$a=1$、任意单位时间和上述每个 $P\in X$：
$$\mathfrak c(\alpha_{mp})_P=(\pi_1,\widetilde H)_P.$$
首层是**原完整理想**，不是只模平方。完成式为 $(\pi_1,z^{e_h})$；
无分歧超奇异和普通状态的公共阶分别准确为 $1$ 和 $0$，
未整除 $dI_{mp}$ 的对应阶分别为 $p$ 和 $p-1$。

其实际机制含两个不可混写的箭头：
$$0\ne\kappa_J=\rho_X\beta_{L_m}(J)\in H^1(X,\mathcal O_X),$$
$$\partial\nu=\operatorname{Fr}_*(\kappa_J)\ne0
\quad\text{in }H^1(X,\mathcal O_X^p).$$
$\beta$ 来自同一个实际 $L_m$、真实常数项及 $1-s^m\equiv-m\pi_1$；
$\rho_X$ 是每条完整纤维的实际限制同构。
$\nu$ 由原迹的 $p\pi_1$ 同余产生，确为原 $\alpha$ 的首切向类。
到像层的 $\operatorname{Fr}_*$ 不等于随后映入 $H^1(\mathcal O_X)$ 的 Frobenius 算子。

数学状态：由 [TH／prime trace 与独查的同哈希合取](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md) 接受。
一般 Bockstein、Čech、Cartier、Taylor 差商、亏格一无零微分及局部理想消元全部扣除。
需比较的严格剩余是原上同调—原迹—原完整曲面三者的指定识别及其闭点算术后果，
不是新的算术 Kodaira–Spencer 或晶体比较一般理论。

### V2. 奇素数的全块首 jet 自相似及准确截断理想

全部奇 $p$、$a\ge2$、$p\nmid m$ 和任意单位时间，
在两层实际参数与时间 jet 匹配的二阶商上：
$$\alpha_{mp^a}^{[2]}=
H^{\langle\sigma-1\rangle}\alpha_{mp}^{[2]}.$$
该恒等式保留全部块内变形，在整个原开放模型成立，含全部末端线。
二阶商识别为 $\pi_1\mapsto\pi_a$，不是自然根嵌入。
于是原光滑有限能级附近：
$$\mathfrak c(\alpha_{mp^a})+(\pi_a^2)
=(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1}).$$
完成式保留根重数：
$(\pi_a^2,z^{e_h\sigma},\pi_a z^{e_h(\sigma-1)})$。

数学状态：同一[全 tame 数学接受](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md)已接受。
模 $p$ 的 $\sigma$ 指数是旧 C3／Vlasenko 已知内容，不单计；
本轮比较的是含首切向方向、时间 jet、非共振块内项的完整一形式。
一般循环插入、Cayley–Hamilton、交换子、数字分解和系数理想乘法也是标准工具。
需核现有 higher Hasse／Dwork／形式群或根单位 $q$-差分定理是否直接包含**这个二阶对象**。
超奇异无分歧状态只推出公共阶至少二，不给准确首非零阶或全厚度。

### V3. 特征二的不同基准、混合理想与长度五截断商

全部奇 $m$、$p=2$、$a\ge2$，共同二阶商必须从 $a=2$ 开始，
不得把 $a=1$ 的特征四商与高层特征二商识别。
新原块恒等式为
$$\alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{4m}^{[2]},\qquad
\alpha_{4m}^{[2]}=(j_*^3+\epsilon T)dj_*+\epsilon J^2\chi_m.$$
其中 $j_*$ 为原块迹的中间系数提升；通过高度一的整数比较，
$\chi_m|_{\Omega_X}=\nu$，这里 $X=(J=0)$ 必须是原完整光滑能级。
因此对任意局部提升 $j,\widetilde T$，作者主张的准确截断理想为
$$\mathfrak c(\alpha_{mN})+(\pi_a^2)
=(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_a j^{N-2}).$$
特别 $a=2$ 时为 $(\pi_2^2,j^3+\pi_2\widetilde T,\pi_2j^2)$，
完成后的截断临界商为
$$k(P)[[w,z]]/(z^5),\qquad \pi_2\longmapsto z^3/T.$$
横向长度五只属于此截断商；原 $\alpha_{4m}$ 的无分歧超奇异状态阶准确一，
未整除 $dI_{4m}$ 准确五。$a\ge3$ 仍只有至少二的整除状态阶。

数学状态：两份作者件已冻结，全文非作者合并检查正在进行，
未由本 Phase A 预授接受；主控已全文实读作者件。
输入为 [P2 块引理](PAPER30_QPI_VERTICAL_ALPHA_P2_BLOCK_FIRST_JET_LEMMA_V1_20260909.md)
与 [P2 实际几何理想](PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_PROOF_V1_20260909.md)。
不是把 V2 代入 $p=2$，但也不能将每个小特征代数步骤拆成独立发现。
比较重点是实际混合项和底参数作用，是否为已知提升理论的直接实例；
不以形式上非单项式就先授予高新意。

## 4. 必要依赖、非贡献项与明确不含范围

必要链保留原矩阵与八截面模型、完整小阶亏格一 pencil、
原实际 Jacobian／光滑闭能级 Hasse 识别、原整数整除及全图正则性、
实际 $L_m$ 上同调与限制同构，以及本轮 prime trace／OC／TB／P2 证明。
旧正确替代证明允许按已有接受去重，但真正消费者的证明不能删去或移出正文来凑页。
后续应从实际箭头确定必要链，而非把所有旧作者稿无差别并成新贡献。

旧通用全次数上同调、全部扭子初等因子、有限域完整周期清单，
不因本件引用它们而重复宣传为新结果。具体 $N=9$ 的点值和四阶 jet 接受保持，
它既不代签全高度厚度，也不作为三个主张之外另一个独立发现。
旧 $m=1$ 配对路线不再承担 V1 的必要责任；不用尚未证明的一般 $m$ 配对常数。

本件不含奇异能级的局部理想、任意额外分歧状态的准确阶、
全高度完整厚度、全初始理想、稳定约化、晶体模同构、跨系统族推广或 RH 主张。
这些开放边界不在正式准入前被隐藏，也不把不同模型的最好结果拼接。

## 5. Phase B–D 与组合检查的下一项责任

1. V3 必须以两份最终字节和非作者报告完成实际合取后，才能进入声称数学接受的共同包。
2. 对 V1–V3 各用至少三个不同准确查询表述，覆盖 arXiv、Scholar／Semantic Scholar 可用检索，
   包含 2024–2026 及截至当日近六个月；已读基础 primary 和真实全文缺口继续保留。
   本问题不属 ICLR／NeurIPS／ICML，不把无关会议查询列成覆盖证据。
3. 旧 [首层来源差分](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_SOURCE_DELTA_V1_20260909.md)
   与 [障碍—Cartier 来源差分](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_SOURCE_DELTA_V1_20260909.md)
   必须进入比较；已有明确扣除不因换主张标题而忘记。
4. Phase C/D 由非作者在 Phase B 完成后执行。技能指定的 GPT-5.4 MCP 本轮未配置，
   若使用可用独立 Codex 代理须准确披露同家族替代，不称跨模型验证。
   它不替代以后锁定的两份 fresh 完整四门票。
5. 定向核 Papers1–29 的真正定理与消费者，尤其 P18 的局部临界／Fitting、
   P27–29 的上同调和算术近邻；不把术语相同当碰撞或把系统名不同当非碰撞。
6. 只有准确剩余和独立价值支持继续，才准备正式新候选和完整必要正文证明图。
   每席新意、价值至少 7.5，完整证明信心至少 9，完整自然正文 22–30 页不变。
   不预建项目、source/publication locks、稿件、试排或 PDF，不平均、进位或拼接旧票。

## 6. 本件绑定的新增主要输入

| 作者输入 | SHA-256 |
|---|---|
| TH | `43049d8688f59f57eb3362246d06507ff397ee9e150d18a3443ae8a18990be75` |
| prime trace | `07361a2516b8e891d037a59826e0e789119db93eb78332dc41783f075f15dca9` |
| OC | `81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa` |
| 奇素数 TB | `6546720ecf39f667f09d45235dc0c7be340032b4c3f7c809e9d1cb60257396e9` |
| P2 block | `c5fc4192822733993f361363f194832aee872ab25ce598c39e76be3b1ae62897` |
| P2 ideal | `1d2ff70c69cb26ec2009055f3161cb44758338db8912b9654ab8c53b5d7c59d3` |

本文件只固定可查新的新对象和责任；不对新意、价值或容量给作者自评分。
全部动作仅本地，旧锁、冻结稿、失败和已接受产物不改。
