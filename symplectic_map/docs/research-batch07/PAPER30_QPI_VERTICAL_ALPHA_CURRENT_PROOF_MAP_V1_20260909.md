# Paper30 qPI Vertical Alpha：当前完整必要证明图 V1

日期：2026-09-09。组织者：`/root/p30_qpi_nonunit_tau_layer1_v1`。
类型：完整 V1–V3 的当前证明责任与消费者映射；不是新作者定理或新审查票。
状态：`CURRENT_PROOF_DEPENDENCY_MAP`；`proof_status: NOT_A_NEW_PROOF`。
`route_applicability: NOT_APPLICABLE`。不授正式准入、正文容量或产物验收。

## 1. 使用合同：完整可见，准确调用

本图与 [完整候选 brief](PAPER30_QPI_VERTICAL_ALPHA_CANDIDATE_BRIEF_V1_20260909.md) 同用，
按 [两项复用接受](PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_DISPOSITION_V1_20260909.md) 接入 DB、SH。
[替换前依赖诊断](PAPER30_QPI_VERTICAL_ALPHA_PROOF_DEPENDENCY_AUDIT_V1_20260909.md) 原件保留；
它记录的 Ucoh/Ssplit 与 Ffib 旧供应不再覆盖本图已准确改接的两个消费者。
旧作者件中“待审”是当时快照；当前同字节数学状态由相应主控处置接续，不修改原件。

本图列出的二十份必要作者材料必须全文提供给正式评价者，并由评价者按共同输入要求实读。
下文的段落范围只标明哪些证明责任真正进入 V1–V3，不是授权只读摘录、删去前提或隐藏全文。
全文可见也不等于把每份历史文件的所有结论重新计为新命题、必要正文或新意。
本文没有页数估算；完整必要证明进入正文的容量责任仍待独立判断，不能由表格变短推定。
同字节身份由主控共同输入清单冻结；本图不另建一套源哈希清单或改动任何作者文件。

## 2. 原对象、量词与不可混同的输出

固定原八截面、原反典范八环 $D$、$L_n=\mathcal O_S(nD)$、完整开放模型 $U=S\setminus D$。
原矩阵及降序词积、单位时间、能级和两个状态方向均按 brief §2，不作谱等价替换。
令 $p$ 为素数、$m\ge1$、$a\ge1$、$p\nmid m$，取 brief §2.3 的无分歧 $\mathcal O_0$、
原 $\mathcal O_a=\mathcal O_0[\zeta_{p^a}]$ 与任意单位时间 $t_a$；置
$N=p^a$、$s_a=\widetilde\eta\zeta_{p^a}$、$\pi_a=\zeta_{p^a}-1$、$\eta=\bar s_a$，
$$\alpha_{mN}=p^{-a}d_{\rm state}I_{mN,s_a},\quad
J=I_{m,\eta}(x,y;\bar t_a),\quad T=\bar t_a^m,\quad
\varepsilon_m=(-1)^{m+1},\quad \sigma=(N-1)/(p-1).$$
该除法先在特征零中实施，正则性由 Ddiff/Gint 给出，不改成仅环面上的有理形式。
记 $H=H_p(T,J;\varepsilon_m)$，奇 $p$ 时
$$H_p(T,h;\varepsilon)=[Z^{p-1}]
\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},$$
而 $H_2(T,h;\varepsilon)=h$。不假设 Hasse 根简单。
首层 V1 保留完美剩余域范围；奇素数 TB 和高层实际理想保留各自有限剩余域范围。
P2 块恒等式允许完美域，不将它的范围未经另证赋给 PI 的全部几何结论。
完成、有限无分歧扩张及返回未完成局部 DVR 仅按作者原论证；不添额外分歧状态。

下表 $\mathfrak c$ 是秩二相对余切模中全部系数的理想，$[2]$ 表示模 $\pi_a^2$。
$\widetilde H,j$ 是指定剩余函数的任意局部提升，$\widetilde T$ 是常数单位提升。
记原完整光滑有限概形纤维为 $X=(J=h)$，闭能级的剩余域按允许扩张解释。
理想的几何结论均在这种原纤维的所有点，包含四条末端线。

| 责任 | 必须保留的准确输出 | 直接供应 |
|---|---|---|
| V1a，全部 $p,m$、$a=1$ | 原完整理想 $\mathfrak c(\alpha_{mp})=(\pi_1,\widetilde H)$；根重数 $e_h$ 处完成式为 $(\pi_1,z^{e_h})$，$\bar z=J-h$ | TH + DB + prime + OC + 原完整模型 |
| V1b，全部完整光滑层 | 实际 $0\ne\kappa_J=\rho_X\beta_{L_m}(J)\in H^1(X,\mathcal O_X)$ | DB 与 TH Step 2 |
| V1c，仅 $H_p(T,h;\varepsilon_m)=0$ 的光滑层 | 原首切向类 $\partial\nu=\operatorname{Fr}_*\kappa_J\ne0$，目标是 $H^1(X,\mathcal O_X^p)$；$\nu$ 处处非零 | prime + TH 实际 A1–A4 + OC |
| V2a，奇 $p$、$a\ge2$ | 整个 $U$ 上的完整形式 $\alpha_{mp^a}^{[2]}=H^{\langle\sigma-1\rangle}\alpha_{mp}^{[2]}$ | TB；此恒等式本身不要求光滑能级或 $H\ne0$ |
| V2b，同上且完整光滑层附近 | $\mathfrak c(\alpha_{mp^a})+(\pi_a^2)=(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1})$ | TB 与 V1 的系数理想合取 |
| V3a，$p=2$、奇 $m$、$a\ge2$ | 整个 $U$ 上 $\alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{4m}^{[2]}$ | P2；从高度二而非高度一作基准 |
| V3c，同上且完整光滑层附近 | $\mathfrak c(\alpha_{mN})+(\pi_a^2)=(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_a j^{N-2})$ | PI + P2 + V1 的实际切向类；普通层两边均为单位理想 |

奇 $p$ 的比较是 $\pi_1\mapsto\pi_a$ 的共同双数商，并匹配完整时间二阶像。
特征二高层比较是 $\pi_2\mapsto\pi_a$，选 $t_2$ 与 $t_a$ 在共同 $k[\epsilon]/(\epsilon^2)$ 中相同。
两者都不是自然圆分根嵌入；特征二首层的 $\mathcal O_1/(\pi_1^2)$ 是特征四，不能替换成该双数商。
V2 根处完成式保留 $e_h$：$(\pi_a^2,z^{e_h\sigma},\pi_a z^{e_h(\sigma-1)})$。
V3 的原四块基准 V3b 见 §7；V3d 在高度二取 $\bar z=J$，其截断完成商为
$$k(P)[[w,z,\epsilon]]/(\epsilon^2,z^3+\epsilon T,\epsilon z^2)
\simeq k(P)[[w,z]]/(z^5),\qquad \pi_2\longmapsto z^3/T.$$
这里五是截断横向长度，不是闭点总 Artin 长度、全厚度或平坦性声明；$T$ 不是新增形式模量。
普通状态的 $\alpha$ 阶准确为零；超奇异无分歧状态首层准确为一，奇 $p$ 高层仅至少二。
特征二高度二准确为一、高度至少三仅至少二；乘回 $p^a$ 分别加上 $a\varphi(p^a)$。
所以 $dI$ 的首层超奇异阶为 $p$、特征二高度二为五，其余高层只给相应下界。

## 3. 二十份全文可见的作者材料与实际责任

表中范围是当前必要证明定位；一个文件可以同时含不被本候选消费的其他已接受出口。
缩写 Bbad 的当前出口是纯 W0 几何与有限临界代数，不等于旧实际强临界结论。

| 别名及完整文件 | 当前必要证明段／责任 |
|---|---|
| DB：[直接八环 Bockstein](PAPER30_QPI_VERTICAL_ALPHA_DIRECT_BOUNDARY_BOCKSTEIN_REUSE_V1_20260909.md) | 全部 DB.1–DB.3、Steps 1–5；替换首层 U2A 特例及 $n=0$ 供应，保留实际类 |
| SH：[完整光滑闭 Hasse](PAPER30_QPI_VERTICAL_ALPHA_SMOOTH_CLOSED_HASSE_REUSE_V1_20260909.md) | 全部 SH.1–SH.3、Steps 1–6；只改接选定已光滑完整纤维的几何整性前提 |
| TH：[全 tame 首层](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md) | 全命题及 Steps 1–5；Steps 1–2 的已指定供应按 DB 改接，其余原证明保留 |
| prime：[素数迹同余](PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md) | §§1–6 的原块、词轨道、整数迹递推、导数及分歧 Taylor；$p=2$ 不例外 |
| OC：[障碍—Cartier](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md) | A1–A4 和全部 Steps 1–5；抽象条件须由实际 TH/DB/prime 供应 |
| TB：[全 tame 块首 jet](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md) | 全部全称命题、Steps 1–6，105–299；全 $m$ 内外部项及全图粘合 |
| P2：[特征二块首 jet](PAPER30_QPI_VERTICAL_ALPHA_P2_BLOCK_FIRST_JET_LEMMA_V1_20260909.md) | 全部命题、Steps 1–7，94–286；特征二内部项、交换子、数字选择和全图分解 |
| PI：[特征二高层实际理想](PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_PROOF_V1_20260909.md) | 全部命题、Steps 1–5，81–212；原切向识别、每点两次整除及实际混合理想 |
| P：[辛与极除子](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | 原矩阵／Laurent 首项 47–67，完整 Steps 1–6，94–257；原小阶非恒定及准确极除子 |
| Nbd：[边界法丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | Steps 1–7，68–269；原节点单位帧、传播比、边界法丛精确阶与完整截面责任 |
| Gfield：[原始亏格一](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | Steps 1–6，95–253；完整 pencil、Stein 非复合性、几何连通及全允许特征泛光滑 |
| Jspec：[原 Lax Jacobian](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | 原两图／端点 119–182，有限推下及 Steps 2–7，214–454；实际谱模到原域 torsor 的完整链 |
| Wreuse：[共享 Weierstrass V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md) | 70–161 的 W0、原谱商／谱曲线几何、全特征接口及任意原域 Step 2a |
| Bbad：[准确坏值桥](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | 138–166 原互逆变换与原点；217–251 纯 W 模型；305–311、329–365 纯有限临界代数的实际证明 |
| Hloc：[指定点／局部模型复用](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md) | L(a) 193–212 与 L1–L3，224–257；原实际前提 278–299 中选定光滑层的几何整性按 SH 改接 |
| Ddiff：[先除后约化微分](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 原规范及 111–192 的整数除法／插入／迹递推／剩余式；206–233 指定谱微分的全曲线 Cartier |
| Gint：[圆分完整模型](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 1–40 八截面四图，113–131 原模型与积分延拓，222–233 全局 $\alpha$／剩余式；仅 G3a/b |
| Ucoh：[通用上同调](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | Steps 1–2，105–149 的真实常数和整单位节点计算；DB 重述其准确计算，不消费后部通用分裂 |
| Matrix：[首 jet 矩阵引理](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md) | Steps 1–3，104–164 的秩二插入、Cayley–Hamilton 及加权交换子接口；不继承其 $m=1$ 结论作为全 $m$ 证明 |
| GFI：[旧全局首 jet](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_FACTORISATION_V1_20260909.md) | Steps 1–2，87–117，及 Step 4，134–145；共同商、时间 jet、提升幂与非约化四图限制单射 |

## 4. 拓扑顺序及主结论的合取位置

下列是证明责任顺序，不是文件生成日期顺序。末项状态阶只消费已经证明的实际理想。
prime 对 TB 的引用仅为原块定义／首尾系数且已在 prime §§2–3 重证；不是依赖 TB 的奇素数结论。

1. P、Nbd、Gfield、Gint 的原模型、pencil 与原矩阵固定对象；Ucoh 基础图计算固定真实常数和边界帧，Ddiff/Gint 给原整除形式的全局正则性。
2. W0/Bbad、Wreuse/Jspec、Hloc 与 SH/Ddiff 给实际闭 Hasse 身份；内部顺序详见下段及 §6。
3. DB 的实际层连接经原完整 pencil 限制到 $X$，给全部光滑层的 $\kappa_J\ne0$。
4. Ddiff 加 prime 给原迹 $p\pi$ 同余、整数导数和 Taylor；Gint 将同余延到完整原开放模型。
5. 第 2–4 项与 TH 的实际局部提升核准 OC A1–A4；OC 给超奇异层的 $\nu$ 非消失和 V1 完整理想。
6. Matrix、Ddiff 和原块恒等式进入 TB；GFI/Gint 负责全图接口，TB 与 V1 合取得 V2 理想。
7. P2 独立完成特征二全部块代数及全图分解；PI 将 prime/TH 的实际首切向类接回 P2，给 V3。
8. V1、V2、V3 的局部理想取允许状态像，最后乘回 $p^a$；不是由旧扭子长度推出。

第 1 项中先有 P 的原极除子，再有 Nbd/Gfield 的边界与完整 pencil；Gint 保持同一整数模型。
第 2 项先取 Bbad 的纯 W0 段，再经 Wreuse 的原谱几何段进入 Jspec 的实际谱模证明；
随后将真实泛 torsor 与 SH 的选定光滑层前提代入 Hloc L(a)，最后作闭谱微分的 Cartier 运输。
这是一条可拓扑排序的子链，不把 Bbad/Wreuse 后部原动力强临界出口反向作为 W0 前提。
第 2 项为第 5–7 项中“普通／超奇异是原完整闭能级”的必要身份供应。
仅把 $H=0$ 当作形式上的多项式条件不能卸下这项责任。
DB 与 SH 两条短接口是同对象已核准替代证明，不是删去不同科学目标的许可。

## 5. V1 的实际类：DB、prime、TH 与 OC

### 5.1 不能以维数代替的 Bockstein

DB Steps 1–2 在实际 $A_2=\mathcal O_1/(\pi_1^2)$ 和 $k$ 上重述吹起图的常数上同调，
以及原八环单位帧的同一个边界复形 $[A\xrightarrow{1-s_1^j}A]$。
节点消元和次数一单位缩放先在整环固定，再同时约化，与乘 $\pi_1$ 和连接同态相容。
$1\le j<m$ 时边界复形无上同调；$j=m$ 的原限制给 $r_1$ 同构与 $\ker r_0=k\langle1\rangle$。
原层短正合列的自然性给 $r_1\beta_L=\beta_Dr_0$，且
$$1-s_1^m\equiv-m\pi_1\pmod{\pi_1^2},\qquad \beta_D=-\bar m.$$
故 Bockstein 核恰为真实常数；P 给原 $J$ 非常数，遂得 $\beta_L(J)\ne0$。
不把 $J$ 人为认作某个边界基元，不把普通 $H^0$ 基变换或一维性代替真实连接。
$p=2$ 的特征四和 $m=1$ 空归纳都在 DB 内处理；任意单位时间未冻结成剩余值。

DB Step 5 与 TH Step 2 使用原有限纤维及原截面 $1$ 的指定平凡化：
$$0\longrightarrow\mathcal O_{S_k}\xrightarrow{J-h\cdot1}L_{m,k}
\longrightarrow L_{m,k}|_X\longrightarrow0,\qquad L_{m,k}|_X\simeq\mathcal O_X.$$
真实常数的 $H^1,H^2$ 消失给 $\rho_X$ 同构，实际局部差商 $(j_j-j_i)/\pi_1$ 给同一 $\kappa_J$。
这个限制箭头仍是必须保留的实际证明，不能压成旧上同调数值结论的形式推论。
由此改接后不再消费 Ucoh 的全部次数通用导出分裂，也不消费 Ssplit 的整数截面下降。
但 Ucoh 105–149 的基础计算仍明示可见，不能宣称完全不用 Ucoh。

### 5.2 原迹同余、非约化延拓与像层 Frobenius

prime §§2–6 保留降序原块、循环词轨道、非共振项相乘返回共振的 $p$ 因子和整数迹递推。
记 $F$ 为 prime 中原整数迹递推产生的多项式，$j_i$ 为原 $J$ 的局部正则提升。
所需同余是 $I_{mp}-F(j_i)\in p\pi_1\mathcal O_{U}$ 的局部理想，不是仅模 $p$ 或剩余函数相等。
整数 Taylor 除 $p\pi_1$ 后的 Frobenius 项、符号及特征二中间项不能提前约化掉。
TH Steps 3–4 在原四末端图延伸此实际同余：模 $p\pi_1$ 底环可非约化，
每图是单位局部化的 $B[u,v]$，$u$ 非零因子，反演 $u$ 后的限制单射是代数事实。
仅在剩余点集上稠密为真，不足以证明该同余。

TH Step 5 以全局正则 $\alpha$、原完整光滑亏格一纤维及上述实际类核准 OC A1–A4。
OC 的 Taylor、$\ker d=\mathcal O_X^p$、像层短正合列和 Čech 符号全部保留：
$$\partial\nu=\operatorname{Fr}_*\kappa_J\in H^1(X,\mathcal O_X^p).$$
这里到像层的 Frobenius 为加性层同构；再映入 $H^1(X,\mathcal O_X)$ 的箭头可以杀掉该类。
不能把它误说成超奇异曲线上 $H^1(\mathcal O_X)$ 的 Frobenius 可逆。
proper 光滑亏格一曲线上的非零正则微分处处非零；与法向 $dJ$ 一起给原秩二系数理想。
这一步不是把环面单位结论直接推广到全曲面，也不要求 Hasse 根简单。

## 6. 实际原 Jacobian 与每条完整光滑闭纤维 Hasse

### 6.1 选定光滑纤维的前提改接，泛谱身份不动

P/Nbd/Gfield 的完整 pencil、Stein 非复合性和几何泛光滑仍保留，包括小特征问题。
SH Steps 1–2 对原先已假设光滑的完整 $X_h$ 使用几何连通性；光滑分量互不相交，
故几何连通迫使几何整约化，反典范类与伴随公式给亏格一。
这只替换 Hloc 此消费者中原由 Ffib 前两步提供的几何整性；不声称覆盖未假设光滑的层。
因此 Ffib 的全部奇异纤维分类无需进入当前 V1–V3，也不修改其旧已接受结论。

原泛 Jacobian 仍须完整经过 Wreuse 70–161 与 Jspec 119–182、214–454：
原两图、四端点、有限推下、实际谱代数模的线丛族、端点恢复状态的有理逆，
排除不可分次数、循环复合为乘 $\lambda$ 的固定除子差、不变 Picard 分支、
全群固定点排除拉回核，以及任意原 $k(c)$ 上的 torsor 作用下降，均是必要正文责任。
Wreuse V2 Step 2a 保留原域接口；不以代数闭域同构一句替代下降。
结论是原动力泛纤维的真实谱商 torsor 和 Jacobian 同构，不是未知核同源。
谱曲线亏格 $2m-1$、谱商亏格一与动力曲线亏格一不能互代；也不假设原泛纤维有有理点。

### 6.2 W0 的纯有限代数仍在主链

Wreuse 当前泛光滑供应还实际使用 Bbad 的纯 W 模型及有限临界概形证明。
Bbad 217–251 核准射影平坦、总空间正则和纯 W 有限纤维几何整约化；
305–311、329–365 的双向消元给
$$Z_W\simeq\operatorname{Spec}k[z]/\big((T-z^2)^2-\varepsilon_mTz\big).$$
首一四次关系给有限性，从而泛临界概形为空；这就是当前原谱泛光滑的实际供应。
不能因最终只用“泛光滑”便删掉该证明，也不把它误归到已移出的 Ffib。
此处不消费乘能级的 $4\times4$ 矩阵、特征多项式或原动力全部临界 Artin 代数长度四。
Wreuse 后部将全部奇异／实际临界结果搬回原曲面的强出口不进入本候选。

### 6.3 同能级局部模型、双向延伸与 Cartier 运输

SH Steps 3–4 仍完整核准 Hloc L(a) 的 proper、flat、正则、几何泛亏格一和特殊纤维几何整约化。
先在所需几何剩余域上选完整光滑纤维的点，再对原能级 $c=h$ 作普通 henselization。
光滑点的 étale 坐标提升给局部截面；这不制造原全局泛域上的点，也不用有限域 Weil 选点。
真实泛 torsor 和带原点谱商／W 识别给指定泛同构；唯一竖直主纤维自交零给两侧相对最小性。
最小正则模型定理同时延伸该同构及其逆，才得到同一 $h$ 上的完整 $X_h\simeq W_h$。
这些责任不能被同一四次方程、同亏格或泛 Jacobian 身份直接替代。

SH Step 5 核完整闭谱商的两图、四端点和指定正则微分，Step 6 接 Ddiff 206–233 的计算：
$$\mathcal C(\omega)=H_p(T,h;\varepsilon_m)^{1/p}\omega,$$
特征二为 $h^{1/2}\omega$。有限分支点及无穷远的正则性都是这一公式的前提。
沿所选几何同构运输后，Hasse 零性质可由原剩余域检测；不要求同构或微分标量典范下降。
这才解释 V1–V3 中原完整闭能级的超奇异性，而非另一个同名谱模型的性质。

## 7. 全部高层：代数、全图与实际理想分别负责

TB Steps 1–5 从原整除循环插入重做全 $m$ 证明，保留全部块内非共振变形与实际时间 jet。
共振投影不是环同态；真实次数界及唯一基 $p$ 数字选择负责全称因子分解。
Matrix 的通用秩二身份不是 $m=1$ 外推许可证；TB 自己承担全块内外项证明。
TB Step 6 与 GFI Steps 1–2、4 比较共同二阶商、粘合 $p$ 倍指数提升幂，
再用 Gint 自由微分模的非约化限制单射跨过四末端线。
取得完整一形式后才与 V1 合取两方向理想；不调用 GFI Step 5 的旧 $m=1$ 首层路线。

P2 Steps 1–7 独立处理特征二共同商、内部迹项、加权交换子和二进制唯一选择。
它给原环面四块基准
$$\alpha_{4m}^{[2]}=(j_*^3+\epsilon T)dj_*+\epsilon J^2\chi_m,$$
其中 $s=\eta(1+\epsilon)$、$t=t_a\bmod\pi_a^2$，且
$j_*=[z^m]\operatorname{tr}(A(s^{m-1}z;t)\cdots A(z;t))$ 为实际块中间系数，
$$\chi_m=J\,dJ+[z^{2m}]\operatorname{tr}(d\mathsf B_0\,z\partial_z\mathsf B_0),\quad
\mathsf B_0=A(\eta^{m-1}z;\bar t)\cdots A(z;\bar t).$$
P2 不独自证明该环境形式沿完整 $X=(J=0)$ 处处非零，也不保证 $j_*$ 有全图整提升。
PI Step 1 用首层特征四的 prime/TH 比较识别 $\chi_m|_{\Omega_X}=\nu$；不能提前置二为零。
PI Steps 2–3 用局部全局形式差商、素 Cartier 参数及两次整除落实到全部完整点，
不擅称 $\chi_m$ 在整个剩余曲面正则；Steps 4–5 才消去两方向系数并得到混合商和状态阶。
因此 V3 不是 P2 单独的代数推论，也不是把奇素数公式代入二。
所有有限精确样本只作排错，不供应全 $m$、全高度、任意单位时间或末端线量词。

## 8. 不进入当前消费者的旧出口及同字节接受

| 不进入本候选的出口 | 准确边界 |
|---|---|
| Ssplit 整数截面下降、全部扩张分裂、U2A 通用自然复形、Smith/Fitting 总表 | DB 已核准替换本处首层供应；仅保留 Ucoh 基础图计算，不否定旧定理 |
| Ffib 全部有限纤维证明、节点／尖点分类、Chern/GRR | SH 仅用已光滑层加几何连通性核准当前 Hloc 前提；不是新的全部奇异层定理 |
| Gint 的完整大阶 pencil 重纤维、扭子过滤及 G3c 长度比较 | 当前只用模型／函数／形式正则和 G3a/b；新状态阶不由旧长度推出 |
| Wreuse 后部全部奇异与实际临界、Hloc L(b)/(c)、Bbad 强实际 Artin 结论 | Hloc L(a)、原泛谱模与 W0 纯有限代数仍保留，不能一并删去 |
| 旧 $m=1$ 迭代／首层配对、一般 $m$ 配对 $m^2$ 猜想、N9 与非单位时间探针 | 无证明箭头进入新 TH/TB/P2/PI；未闭旧猜想不是本链缺口或新结论 |
| 原回返、非挠平移、周期、奇异群、有限域轨道分箱 | 不消费；轨道 Hasse 上界不是本处完整微分的 Cartier–Hasse 身份 |

数学接受的来源按下表合取；它们是已存在状态记录，不是本文新投票。

| 责任组 | 当前接受记录 |
|---|---|
| TH、prime、OC、TB 及奇素数首层／高层合取 | [全 tame 数学处置](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md) |
| P2、PI 与完整 V1–V3 | [全素数数学处置](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_JET_MATHEMATICS_DISPOSITION_V1_20260909.md) |
| DB、SH 的准确替换及无隐藏旧分裂／Ffib 出边 | [两项复用接受](PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_DISPOSITION_V1_20260909.md) |
| P、Nbd、Gfield | [域上入口处置](PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md) |
| Jspec、Bbad；Wreuse V2 的无循环替换 | [动力几何处置](PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md)、[Wreuse V2 非作者接受](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md) |
| Hloc L(a) 与实际接口 | [局部模型复用处置](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md)；当前光滑层的前提供应再按 SH |
| Ddiff、Gint、Ucoh 基础责任 | [整数数学处置](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md)；不整包继承旧整数结论 |
| Matrix 的完整通用矩阵量词 | [DM：首层数学处置](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_MATHEMATICS_DISPOSITION_V1_20260909.md)，135 行；其中旧 $m=1$ 几何／配对不作为本链供应 |
| GFI 的共同商／非约化全图接口 | [DGFI：高层 jet 数学处置](PAPER30_QPI_VERTICAL_ALPHA_HIGHER_JET_MATHEMATICS_DISPOSITION_V1_20260909.md)，98 行；不消费其 N9 或旧首层理想的额外责任 |

Matrix 与 GFI 的实际独查分别按 DM、DGFI 绑定，再与全 tame／全素数处置合取；
Phase A 冻结快照中的待审字样不撤销后来相同作者字节的接受，也不扩大原范围。
正式评价仍需自己判断完整候选；不能拼接旧票、把既有数学接受折算成新意或容量。

## 9. 组织件的核对与交付边界

作者已按实际消费者亲读本图必要证明；二十件全文与段落使用责任在共同输入中分别列清。
此前本人写过 P2、SH，独查过 TH/prime、OC；本图不冒称盲审，不自作这些作者件的独立票。
proof-writer 的影响限于保留准确命题、量词、依赖、已核准替换和未调用出口，不生成新定理。
本图仅组织已接受证明，不修订 brief 的科学合同，不提高来源预审分数，不改变任何旧失败。
只新增此文件；没有论文、试排、锁、索引改写、旧产物删除或外部写入。
下一步冻结共同输入并接受新的完整独立判断；本文本身不授该判断的任何结果。
