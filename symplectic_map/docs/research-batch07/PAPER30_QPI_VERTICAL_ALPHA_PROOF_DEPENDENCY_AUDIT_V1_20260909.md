# Paper30 qPI：垂直微分 V1–V3 的实际旧证明消费者核对

日期：2026-09-09。执行者：`/root/p30_qpi_nonunit_tau_layer1_v1`。
状态：`DEPENDENCY_MAPPING_COMPLETE`；`proof_status: NOT_A_NEW_PROOF`。
本件仅诊断现有证明箭头，不是新数学审查、正式评价、篇幅测算或统一论文证明。

## 1. 结论与范围

按下述已接受、同一原模型的现存证明，V1–V3 的必要上游消费者可以闭合；
本次没有发现为了执行这些箭头而必须新增证明的真实缺口。
这不意味着全部旧 C1–C3 或 T1–T7 都成为新结论的必要前提。
也不意味着可以把当前使用的强引理，未经另证就改写为更短的专用版本。

范围由全文实读的 [垂直微分 Phase A](PAPER30_QPI_VERTICAL_ALPHA_SCOPE_PHASE_A_V1_20260909.md)固定。
其 V3 尚待检查的文字是冻结快照；相同作者字节的当前接受状态由全文实读的
[全素数数学处置](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_JET_MATHEMATICS_DISPOSITION_V1_20260909.md)接续。
V1–V2 的同哈希接受另见全文实读的
[全 tame 数学处置](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md)。
本依赖报告不代替这些数学责任，尤其不对本人所写 P2 块引理自作独立验收。

保留原八截面、原矩阵降序乘积、单位时间、原小阶积分 $J$ 与
$\alpha_{mp^a}=p^{-a}d_{\rm state}I_{mp^a}$。
令 $p\nmid m$、$N=p^a$、$\pi_a=\zeta_{p^a}-1$、$\sigma=(N-1)/(p-1)$、
$T=\bar t^m$、$\varepsilon=(-1)^{m+1}$、$H=H_p(T,J;\varepsilon)$。
下表 $j,\widetilde H,\widetilde T$ 为相应剩余函数的局部提升，$\widetilde T$ 为常数单位提升。
局部理想结论仅在原完整光滑有限概形纤维附近：

| 新责任 | 实际结论 | 直接证明供应 |
|---|---|---|
| V1：所有 $p$、$a=1$ | $\mathfrak c(\alpha_{mp})=(\pi_1,\widetilde H)$；$H=0$ 时有实际 $\kappa_J=\rho_X\beta_{L_m}(J)$、$\partial\nu=\operatorname{Fr}_*\kappa_J$ | TH、prime trace、OC；旧 U2A、原完整模型 G3 和完整光滑纤维几何 |
| V2：奇 $p$、$a\ge2$ | 完整模平方一形式因子分解；理想原像为 $(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1})$ | TB 的全块证明加 V1；旧通用矩阵引理及二阶商／四图接口 |
| V3：$p=2$、$a\ge2$ | 原像为 $(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_a j^{N-2})$ | P2 块引理与 PI 实际几何接口；PI 再消费 V1 和 prime trace |

各作者的完美／有限剩余域及允许无分歧基变换范围分别保留，不把它们合并成更大量词。
“普通／超奇异”的原闭能级解释仍必须由实际 Jacobian 与完整闭纤维 Hasse 链支持。

## 2. 新证明与旧引理的直接连接

用 TH 表示 [全 tame 首层证明](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md)，
OC 表示 [障碍—Cartier 引理](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md)，
TB 表示 [全 tame 块首 jet](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md)，
PI 表示 [特征二高层实际理想](PAPER30_QPI_VERTICAL_ALPHA_P2_HIGHER_IDEAL_PROOF_V1_20260909.md)。

| 现存新证明位置 | 真正使用的旧出口 | 不能以什么替代 |
|---|---|---|
| TH Step 1，72–98 | 固定 $n=m$ 的 U2A；$\mathcal O,A_2=\mathcal O/(\pi^2),k$ 上同一个自然复形，真实常数为固定直和项 | 分别同构的上同调群、维数、Smith 长度，或通常 $H^0$ 非平坦基变换 |
| TH Step 2，99–123 | $n=0$ 的 $H^1(\mathcal O_S)=H^2(\mathcal O_S)=0$；小阶 $L_m$ 与原有限纤维 | 旧圆分大阶 pencil 的数值缺陷，或抽象一维空间间的未指定同构 |
| TH Steps 3–4，124–169 | 原迹／时间规范；Gint 的 $I_{mp}$ 正则、四末端图及其模 $p\pi$ 限制单射 | 仅剩余点集稠密、擅设 $J$ 有全局整提升 |
| TH Step 5，170–194 | 原曲面光滑、G3 的全局 $\alpha$ 与剩余式；完整光滑几何整亏格一纤维 | 环面非消失，或不同模型上另选的正则微分 |
| TB 输入表 61–72、Step 6，273–297 | 旧矩阵引理 Steps 1–3；旧全局首 jet 的商比较／提升幂／限制单射接口；D/G 原规范 | $m=1$ 的次数界、忽略实际时间 jet、假定非共振项为零 |
| PI 依赖 45–63 | TH 的处处非零首切向 $\nu$、prime trace 的特征四原同余、P2 原全局因子分解及 G3 | 单独的特征二块恒等式，或未知 $\chi_m$ 的全图正则性 |

TH 中 $\beta_{L_m}(J)\ne0$ 的具体理由是：$j<m$ 时 $1-s^j$ 为单位，
而 $1-s^m\equiv-m\pi\pmod{\pi^2}$；共同复形的 Bockstein 核恰是真实常数。
这个连接需要 U2A 的自然性，不需要把原 $J$ 强行认作某个人工直和基元。

限制箭头 $\rho_X$ 是 TH 的新消费者证明，不是旧 U 的现成结论。
原 $X=(J-h)$ 对应 $L_m$ 的截面，且 $1$ 在 $X$ 平凡化 $L_m|_X$，因为有限纤维不碰边界。
实际短正合列
$$0\longrightarrow\mathcal O_S\longrightarrow L_m\longrightarrow L_m|_X\longrightarrow0$$
结合上述 $n=0$ 消失，给 $H^1(S,L_m)\simeq H^1(X,\mathcal O_X)$。
TH 还检查原局部函数的差商 $(j_j-j_i)/\pi$ 正是这一限制类的代表。
后续 prime trace、整数 Taylor、四图延拓才核准 OC 的 A1–A4。
所以不能把这条实际类比较写成旧 C2 的数值等式的形式推论。

V2 的 TB 不以 V1 非消失作为代数证明输入；取得完整一形式恒等式后才与 V1 取系数理想合取。
V3 的 PI 则确实直接消费首层类：其特征四比较识别原 $\chi_m|_{T_X}=\nu$。
二者依赖方向不同。新全块数字论证由 TB/P2 自己完成，旧 $m=1$ 迭代文件仅作规范对照。

## 3. U2A 的实际证明供应：语义出口较小，当前支持证明不能跳过

下文别名 Ucoh 为 [通用上同调诊断](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md)，
Ssplit 为 [圆分扭子分裂探针](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md)，
P、Nbd 分别为 [原辛与极除子](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md)
与 [边界法丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)。

新 V1 只要求 $n=m$ 的共同复形和 $n=0$ 消失，未重新提出“全部 $n$、任意基变换”的新定理。
但 Ucoh 当前给出这个特例的证明依次使用以下完整步骤：

1. Ucoh 105–125：实际逐次吹起的结构层推前和 Leray／Čech，固定真实常数映射。
2. Ucoh 127–149：Nbd 的真实单位帧、八节点复形、边界短正合列及不预设分裂的过滤。
3. Ucoh 150–180，连同 Ssplit Steps 1–5（112–266）：对每个 $1\le j\le m$，
   在 $\mathbb Z[q^{\pm1},\tau^{\pm1}]/(1-q^j)$ 上构造原迹截面 $C_j$，证明其整体整性和边界单位性。
4. Ucoh 181–210：边界 Bockstein 的单位像给逐级分裂；随后用实际 $\operatorname{Ext}^2=0$
   分裂导出截断三角，保留真实常数。
5. Ucoh 211–218：在 proper、相干、底平坦前提下使用导出基变换，固定有限自由复形再张量。

其中 Ssplit 的整数截面步骤不能由域上极除子公式一句代替：
先将非正规根单位整数环嵌入所有特征零圆分分支；原重复块及 Cayley–Hamilton 给各分支上的截面。
允许极的商层有平坦过滤，才使逐分支消失下降为整数截面。
之后原负 $x$ 首项的幂等矩阵给单位系数，再由真实节点帧传播到整条边界。
P 的原极除子与 Nbd 的节点规范分别在这两处被实际消费。

这套证明已接受；Ucoh 冻结作者文字所对应的独查项目 S5/S7 待审由同哈希
[整数数学处置](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md)关闭。
本件没有另造只适用于 $n=m$ 的较短上同调引理。
若未来要绕开以上整数截面下降、扩张分裂或导出自然性，必须提供新的替代证明并单独核准，
不能仅因最终只取一个 $m$ 就删除供应该特例的证明。

## 4. 完整原模型、原泛 Jacobian 与闭纤维 Hasse 的必要链

### 4.1 原完整模型与完整光滑有限纤维

Gfield 为 [原始亏格一桥](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md)，
Ffib 为 [实际有限纤维证明](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md)，
Gint 为 [圆分完整模型](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)。

P 94–257、Nbd 68–269 给原八吹起、反典范边界、原 $I_m$ 精确极除子及法丛精确阶。
Gfield 95–253 在此基础上证明原完整 pencil、Stein 非复合性、泛可分和所有允许特征的几何泛光滑。
此处保留完整论证；算术亏格一不能单独排除小特征的准椭圆问题。

对新局部理想本身，$X$ 已限定为完整光滑纤维，不需要重证所有奇异纤维的分类。
但下述现存 Hloc 实际模型核对仍明确调用 Ffib Steps 1–2（128–245）的有限纤维几何整约化性。
因此保留其整数 Picard 格与有限分量排除的供应段；不把 Ffib 的节点／尖点分类、正规化、
Chern 临界长度或自治校验出口一起加入。
若将 Hloc 改成仅由“选定光滑纤维加连通性”验证前提，是可能研究的替代接口，
不是当前文件已实施的改接；本任务不新增这种版本。

Gint 的直接消费者更窄：1–40 的八个单位截面和四图，113–131 的光滑模型及原 $I_r$ 正则延拓，
以及 222–233 的 $\alpha$ 全局延拓与剩余恒等式。
四个末端图是相应的 $B[u,v]$ 单位局部化，单位分别为 $1+uv,t+uv,t+uv,s+uv$；
反演 $u$ 的映射在自由微分模上单射，即使 $B$ 非约化也如此。
TH 的模 $p\pi$ 同余和 TB/P2 的模平方一形式都需要这个接口。
Gint 的全部相对大阶 pencil 平坦、概形纤维重数、扭子过滤及 Fitting 数值等独立出口不由此自动进入。

### 4.2 原泛 Jacobian：完整谱模桥不能由谱方程替代

Jspec 为 [原 Lax Jacobian 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md)，
Wreuse 为已接受的 [共享 Weierstrass 复用 V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md)，
Bbad 为 [准确坏值桥](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md)。
当前采用 Wreuse 的无循环供应路线，不重开旧谱判别式的另一套长计算。

Wreuse 70–161 先以纯方程得到 $W$，再取得原谱商 $E$ 和原谱曲线 $C$ 的几何前提：
非端点开集由 Bbad 138–166 的互逆变换连接，四端点偏导为 $-T,T,-1,1$；
原两图有限平坦推下给亏格与几何连通性，实际循环不变量给商和四全固定端点。
任意原域接口由 V2 Step 2a 保留，不能只在代数闭常数域取得同构后声称自动下降。

随后 Jspec 214–454 的必要责任完整保留：原谱代数模的线丛族、端点系数恢复原状态的有理逆、
排除不可分次数、循环复合实际为乘 $\lambda$ 的固定除子差、不变 Picard 分支、
用全群固定点排除拉回核，以及在原 $k(c)$ 上的 torsor 作用下降。
所得是原动力泛纤维的真实 $E$-torsor 和 $\operatorname{Jac}(X_{k(c)})\simeq E$，
不是未知核同源；不要求原泛纤维有 $k(c)$-点。
谱曲线 $C$ 的亏格 $2m-1$、谱商亏格一及动力曲线亏格一也不能相互替代。

Wreuse 泛光滑的当前证明确实使用 W0 的纯临界有限代数。
Bbad 217–251 先给纯 $W$ 的射影平坦、有限纤维几何整约化及总空间正则；
305–311 给谱侧相对 hypersurface 临界理想；329–365 给完整消元
$$Z_W\simeq\operatorname{Spec}k[z]/((T-z^2)^2-\varepsilon Tz).$$
四次首一关系使临界概形有限，泛化后为空，故原 $W_{k(c)}$ 几何光滑。
新链消费的是这个有限性出口；本次保留当前证明该出口的纯代数段，不另造更短泛光滑引理。
它不消费 Bbad 后续乘 $c$ 的 $4\times4$ 矩阵、特征多项式、
实际动力临界代数长度四，或把非约化临界块搬回原曲面的强 T3 出口。
有限谱侧临界代数与全部实际临界代数是两个不同消费者，不能因名称相近混并。

### 4.3 从真实泛数据到每条原完整光滑闭纤维

Hloc 为 [指定点／局部模型复用](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md)。
只消费其 L(a)，193–212、224–257，以及实际前提核对 278–299；
不消费动力共轭 L(b) 或临界 Artin 块 L(c) 的独立出口。

在原能级参数 $c=h$ 作普通 henselization，剩余域不改变；
对原完整光滑纤维的几何点取光滑点提升，得到局部截面，而非原全局泛域上的截面。
Jspec 给真实泛 torsor，Bbad 的原点检查给带原点 $E\simeq W_{k(c)}$。
两模型的 proper、flat、正则、几何整约化特殊纤维及几何泛亏格一前提逐项核实后，
Hloc 用唯一竖直主纤维自交数零证明相对最小性，并双向延伸指定泛同构。
这样才得到同一 $c=h$、同一剩余域上的完整原闭纤维与 $W_h$ 的同构。
几何核查可先到代数闭域选择点，不需要有限域 Weil 选点、指定动力点或回返定理。

Ddiff 为 [圆分整除微分](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)。
其 206–233 在实际光滑谱模型的指定正则微分上计算
$$\mathcal C(\omega)=H_p(T,h;\varepsilon)^{1/p}\omega,$$
特征二为 $h^{1/2}\omega$，并检查有限分支点与无穷远图的正则性。
结合上述完整闭纤维识别，才把该 Hasse 零点解释为原 $X_h$ 的超奇异性。
仅有泛 Jacobian 身份或相同四次方程不够；原完整闭纤维识别和 Cartier 计算均须保留。
零点性质在几何基变换下检测，不要求选择得到的模型同构或微分标量具有额外典范性。

主控指出的特征二 $h=0$ 检验与现有链相容：原 $W_0$ 的仿射偏导 $F_v=T\ne0$，
无穷远点亦光滑；若使用上述完整 $X_0\simeq W_0$，便已包含该层光滑性。
本报告不据此修改 Phase A／PI 中“完整光滑概形纤维”的冻结前提，也不新增作者定理。

## 5. 保留、非消费者与需要另证的改接

| 对象或动作 | 本次处置与理由 |
|---|---|
| Ddiff 111–192 的先除后约化、循环插入、迹递推、Hasse 数字恒等式 | 保留；定义原 $\alpha$、全 $p,m,a$ 的剩余式以及 TB/P2 的原规范需要 |
| Ddiff 194–204 的全曲面统一阶 | 原非零首项可作整除归一化依据；旧“统一阶等于扭子长度”不成为新局部状态准确阶的证明 |
| Ssplit 112–266、Ucoh 105–218 | 当前 U2A 特例仍实际需要；不以局部理想范围较窄为由自行替换 |
| Ssplit 后部 DVR 分裂路线、Smith 初等因子与总长度；Ucoh 的完整 Fitting 产品出口 | 不消费这些独立结果；保留冻结文件，不做删改 |
| Gint 的完整大阶 pencil 特化、全部重纤维和扭子／Fitting 出口 | 只保留上列实际模型、函数／形式正则性及剩余同模型接口；不机械继承整个 C2 |
| Ffib 全部奇异分类、Chern／GRR 临界长度；Bbad 强实际临界长度与乘法特征多项式 | 不消费；Ffib 前两步及 W0 的纯有限性供应段仍按 §4 保留 |
| 原回返、非挠平移、所有周期、奇异群、有限域轨道分箱 | 无箭头进入 V1–V3；旧轨道 Hasse 上界与本处 Cartier–Hasse 不是同一消费者 |
| 旧 $m=1$ 配对、一般 $m$ 配对 $m^2$ 猜想、N9 有限诊断和非单位时间探针 | 不构成新 TH／TB／PI 的证明输入；不用它们补新全称量词 |
| 用更短 $L_m$ 专用证明替换 Ucoh/Ssplit，或不用 W0 临界有限性证明泛光滑 | 当前未实施；需要新证明和相应核查，不能在依赖报告里视为已完成 |
| 将 Hloc 对全部有限层的供应改为仅光滑层，或删掉原泛谱模桥 | 前者需明确改接并核准；后者直接遗漏锁定身份责任，不可由“同亏格／同方程”代替 |

V1 的处处非零性由真实 Čech 类及 proper 亏格一曲线承担；
V2/V3 的完整模平方延拓由当前原四图或 PI 的实际局部整除论证承担。
上同调自然性、非约化底上的限制单射、完整闭纤维和两方向系数理想是不同责任，不相互替代。
沿允许无分歧状态的准确阶／下界由已接受局部理想取像，再乘回 $p^a$ 得到；
不需要旧 Smith 列表，也不能由数值点算代替。

## 6. 实读责任、同哈希与交付边界

本任务已全文读 proof-writer，并用其要求区分命题、现存供应证明、使用前提和未实施替代。
本人此前独查过 TH／prime trace 与抽象 OC，也写过 P2 块作者件，因此不是盲审。
本次不重审这些数学结论，也未读取新的 TB 独查或 P2 合并独查来产生自己的数学票；
P2 的接受仅由最新主控处置记录。PI 本次只读 45–73 的依赖与记号，不冒称全文复核。

当前任务已按所列段落亲读必要旧作者文本；Wreuse V2 全文，P、Nbd、Gfield 的完整相关证明，
Ffib 前两步、Jspec 实际谱模链、Hloc L(a) 及前提、Ssplit Steps 1–5、Ucoh 实际分裂与导出基变换均实读。
Ddiff 全文及 Gint 所需段落还在紧邻前一作者／审查任务中亲读，本次再次定位实际消费者。
旧整数 proof map 只作检索索引，不作为 V1–V3 的全图继承命令。
接受记录实读范围为：域上处置 1–145；动力几何处置 8–75、151–185；
Wreuse 非作者 V2 全文；Hloc 接受处置全文；整数数学处置全文；两份新数学处置全文。
没有重扫旧构建树、读取整份历史账本、联网查新或执行数值实验。

下列 SHA-256 在本次结束前只对实际引用对象作定向核对；不是新审查或新正式 manifest。

| 作者别名 | SHA-256 |
|---|---|
| P | `61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3` |
| Nbd | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| Gfield | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |
| Ffib | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` |
| Jspec | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` |
| Wreuse V2 | `21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2` |
| Bbad | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` |
| Hloc | `0a6624550ed0f8765b51b01a1a481fd9a545d1791e10c3431effbf3f25428a3e` |
| Ucoh | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| Ssplit | `2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac` |
| Gint | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| Ddiff | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| 旧首 jet 矩阵引理 | `f3618fa1345804ce5d93acae4e6fdb2b3ee7761a87ae2de8bc453d24944971bd` |
| 旧全局首 jet | `9d53bee5abf8026dfa09d2bcb38713e0ace28ff082d9e87b3efa595ab5955a86` |

| 范围或已接受状态记录 | SHA-256 |
|---|---|
| 新 Phase A | `ca6a8e6695709c2eaaff4707bcb94ccfd86367afb492d5ea87da6a1d90396f2f` |
| 全 tame 数学处置 | `a71577e3bbced32f05b1546b9a6373a4d977ce1f60bcb5dce7e7e8ce5f3e8302` |
| 全素数数学处置 | `e1d2897841fa89b95f8339a9af64f0901183cef47d49be75076f7a18b6ab5cc8` |
| 域上入口处置 | `ed09aadb40752ed579bc45edb7b3531c1f78f6c7f7413072cd120315f2b22245` |
| 动力几何处置 | `0bfbde8003d049d80523a2001d410dfa4f38ab2f14838d2dbbe4c1363f7155a7` |
| Wreuse V2 非作者接受 | `0db56630eab29ed89952f28dd2fd8038fa3c724040f99afbec527dd0e42c70f2` |
| Hloc 接受处置 | `40e4fa6460d34ebff7cfc0e20d614f3a2050590f10c58605819cba867e65dad7` |
| 整数数学处置 | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` |

唯一新增文件就是本报告。没有更改作者件、旧证明图、brief、索引、锁或接受产物；
没有给新意／价值／证明信心分数，没有估页、立项、写稿、试排或外部写入。
本次停止点是已闭合的实际消费者映射，不是实施任何删减或重新组织论文的授权。
