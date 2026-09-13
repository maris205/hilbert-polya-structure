# 原自治 qPI 的 Manin—固定概形接口：fresh 非作者独立检查 V1

日期：2026-09-12 UTC。检查者：`/root/p31_manin_fixed_scheme_independent_v1`。
类型：`FRESH_NON_AUTHOR_BOUNDED_MATHEMATICAL_REVIEW`；`route_applicability: NOT_APPLICABLE`。
唯一受审新作者稿为 [A]，FULL 348 行，输入 SHA-256：
`401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7`。

## 1. 结论与准确 Claim

**三项有界结构命题按其实际假设成立；必要数学修正集合为空。**
作者的 `STOP_SHALLOW_INTERFACE` 是不以本浅接口扩篇的范围判断，不是数学否定。
本报告不授正式候选四门、新意分数、独立价值分数或正文容量通过，也不代表主控已作数学接受登记。

按 proof-writer 的分层状态：

- 原目标“单靠已接受的 $N_p$ 完成全部固定概形分类”：`NOT CURRENTLY JUSTIFIED`。
- [A] 实际写明的三项结构命题及式 (9)：`PROVABLE AS STATED`，须完整保留下述假设和基底范围。
- 作者将前者弱化为后者，故其总标题下的 `PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION` 与上述判定不冲突。

审查的准确数学对象为：代数闭域 $k$、$\operatorname{char}k=p>3$、固定 $T\in k^\times$、每个整数 $n\ge1$；
原自治八中心曲面的完整 $\mathcal U=S\setminus D$、原能级 $f=h=I_1:\mathcal U\to\mathbb A^1_h$ 和原完整同构 $F_T$。
带标记射影 Weierstrass 族为

$$
W:\ v^2+huv-Tv=u^3-Tu^2,\qquad O=[0:1:0],\quad P=(0,T).
$$

令 $\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$，
$C^{\mathrm{good}}=\operatorname{Spec}k[h,\delta^{-1}]$；
若 $T\ne-27/256$ 则 $C^{\mathrm{ss}}=\mathbb A^1_h$，否则
$C^{\mathrm{ss}}=\mathbb A^1_h\setminus\{9/8\}$。
在此半稳定基上令 $G=W^{\mathrm{sm}}$；$D_n=Z(nP)$ 是准确截面交除子，$i_n(h_0)$ 是其局部阶；无交点时定义为零。
它们是结构恒等式的输入，不是本件已计算的输出。

## 2. 独立性、技能与来源边界

本人先 FULL 读取工作区 AGENTS、WORKFLOW、research-review 和 proof-writer 技能，再读取 [A] 及下表输入。
research-review 用于核查真实新消费者、反例及量词；proof-writer 用于分离假设、依赖和可证明状态。
工具发现未找到该 research-review 文件指定的外部 Codex MCP 审查端点，故按本轮指定 scope 由本 fresh 非作者直接独查。
没有虚构 GPT-5.4 MCP 调用、threadId、多轮外部往返、跨模型认证或人类认证；也没有安装或配置新端点。

本人不是 [A] 作者或其只读 helper；未与作者沟通、校准判定或请求补证，未派 helper。
收到的主控任务包含风险检查清单和已接受输入定位，不包含一张应继承的 PASS 票。
本人将作者自己的停止扩篇判断与独立数学推理分开。
旧 [BASE]/[FP]/[MANIN] 的接受作为冻结接口消费，未重开其全部上游证明或旧审查。
本人 FULL 读取旧 [C]，核对本轮新使用的最小模型及局部等变接口条件。
主控另行研究的有限域充分条件不在本报告范围；本人没有消费、引入或评价它。

一手源实际读取：

- [Stacks 55.10, 0C9Y][MIN]：Lemma 55.10.1–2 的陈述与完整页面所载证明。
- [Stacks 53.21.1, 0CBY][NODE]：陈述、第一证明及第二证明草图；使用其中分裂节点的完成局部模型。
- [Conrad, Arithmetic Moduli of Generalized Elliptic Curves][CON]：本人打开 PDF 并读取印刷 pp.4–6 的正文，
  含 Definitions 2.1.2、2.1.4，标准多边形作用 (2.1.2)，Example 2.1.7 及 Remark 2.1.13；
  另读后者在 p.7 开头的承接句。源定理在这里归属 DR II.2.7；本人未读取 DR 原证明，不冒称读完 DR。
- [Stacks 10.97.3, 00MC][FF]：Noetherian 局部环完成忠实平坦的陈述与证明。

没有消费 Conrad §2.5、Tate 全形式一致化、Miranda–Persson 全局挠截面线性化或 Duistermaat §7.4 作为新证明前提。
本次有界核查不是这些文献的完整查新，也没有继承作者对这些其他段落的阅读身份。
另打开 Stacks §55.1 引言仅作定位，不作为证明依赖。
浏览器 PDF 的文本阅读不记作本地全文 PDF 文件或其字节哈希认证。

## 3. 逐命题判定

| 新命题／义务 | 独立判定 | 必须保留的边界 |
|---|---|---|
| (4) 原有理坐标与双向逆式 | PASS | $T\ne0$；最初是函数域公式，不按分母删状态 |
| (5) 指定平移符号为 $+P$ | PASS | 不是 $-P$、未知 torsor 位移或未标记自同构像 |
| (6) 全有限基 $\mathcal U\simeq W$ 与动力等式 | PASS | 消费已接受 proper/flat、正则、几何整约化最小模型；仅自治 $r=1$ |
| 四末端线与有限奇点覆盖 | PASS | 模型同构不删末端；本报告又直接核对四末端像 |
| (7) 光滑开集的概形 equalizer | PASS | 保留基向幂零元；不以闭点集合相等代替 |
| Step 3 整个半稳定模型上的广义椭圆作用 | PASS | 几何纤维不可约及光滑零截面是实际满足的源条件；尖点删出此作用证明 |
| 节点正规平滑化与分支 UFD 因式分解 | PASS | 原总空间正则，故平滑化阶恰为一；未宣称任意分歧底变换后仍正则 |
| $U-1=z\cdot\mathrm{unit}$ 与 (8) 完整理想 | PASS | 参数属于群在零截面的形式邻域；状态依赖单位无须消掉 |
| $i_n=0$ 及 $i_n\ge1$ 的节点概形结构 | PASS | 前者是约化孤立节点；后者另有长度一嵌入部分，整个商不是长度一 |
| (9) Fitting 理想与忠实平坦粘合 | PASS | 等式仅在 $f^{-1}(C^{\mathrm{ss}})$，两侧均为确定的 coherent 理想 |
| Step 6 的 Manin 必要筛选消费者 | PASS | 仅 $p\nmid n$ 的有限好能级；不计算 $D_n$ 或候选点准确阶 |
| 完整异常谱／全部准确交数已求出 | NOT CURRENTLY JUSTIFIED | [A] 没有作此强断言；不能把结构公式或 $N_p$ 零集升级为该输出 |

## 4. Proof Strategy 与依赖图

审查策略为直接重算新有理恒等式、逐项匹配标准定理条件，并独立展开最脆弱的节点理想证明。

1. [BASE]/[FP]/[C] 的原对象和最小模型前提，加直接坐标计算及 [MIN]，给全基指定动力同构。
2. 同构加 torsor 作用图的 Cartesian 描述，给好纤维固定概形。
3. [CON] 的实际存在唯一性定理，给在奇异点附近也有定义的相对作用。
4. [NODE] 加原总空间正则性给二维 UFD；作用恒等元、分支保持及乘法切角色给准确标量因子。
5. 局部完整理想、相对余切 Fitting 理想及 [FF]，给全局理想等式。
6. 只代入 [MANIN] 已接受的必要条件，得到好能级的基向约化性筛选。

### 4.1 原坐标和四末端没有换对象

本人在 $k(x,y)$ 中重算，取

$$
h=-x+y+x/y-T/x,\quad u=T/y,\quad v=Tx(y-1)/y^2.
$$

直接得到 $v+hu-T=-T^2/(xy)$，从而满足 $W$ 方程；
$Tu/(T-hu-v)=x$、$T/u=y$。这些等式不需要额外可分性或从有限点数推断次数一。
过 $P$ 的斜率 $m=(v-T)/u=x-x/y-y$ 满足 $m+h=-T/x$。
长 Weierstrass 负元为 $(u,v)\mapsto(u,-v-hu+T)$，弦切加法遂给

$$
(u',v')=\bigl(m^2+hm+T-u,-(m+h)u'\bigr)
=\left(Ty/x,T^2y/x^2\right)=\phi F_T(x,y).
$$

故指定符号确为 $+P$。我另运行无写文件的符号计算，能级不变、三次方程、两逆式及两动力坐标共六个差均恒为零。
这只是有理恒等式转录校验，不是有限特征或有限状态采样证明。

为明确四末端，以下 $a$ 是横向 chart 参数、$b$ 是沿末端的参数，互不等同于节点的 $\tau$ 或群参数 $z$。
从本人实读的 [F] Step 7 代入新坐标：

| [F] 的末端 chart | $a=0$ 的能级 | $W$ 上像 |
|---|---|---|
| $x=a^{-1},\ y=1+ab$ | $h=1-b$ | $(T,Tb)=(T,T(1-h))=-2P$ |
| $x=a(T+ab),\ y=a^{-1}$ | $h=b/T$ | $(0,0)=-P$ |
| $x=a(T+ab),\ y=a^2(T+ab)$ | $h=b/T$ | $[0:1:0]=O$ |
| $x=[a(1+ab)]^{-1},\ y=a^{-1}$ | $h=1+b$ | $(0,T)=P$ |

第三行用射影 chart $[u/v:1:1/v]$，两个非恒定坐标在 $a=0$ 都为零。
其余三行在仿射 chart 正则；$T\ne0$ 使表中基底参数均有效。
$2P=(T,0)$ 来自 $P$ 处切线斜率 $-h$，故第一行的标记也已核对。
这张表是同一已证模型同构的附加校验，不是用四个曲线极限替代模型延拓证明。

### 4.2 最小模型定理确实覆盖全有限基

本人读取 [C] 全文，尤其其 Step 1–2：原 $\mathcal U$ 是原 proper pencil 的有限基逆像，原曲面光滑；
$W$ 的仿射相对奇点有 $uv\ne0$，所以总方程的 $h$ 偏导 $uv$ 非零，$O$ 也光滑。
双方 finite type、proper、flat、regular，特殊纤维几何整且约化，唯一竖直分量自交为零。
因此在每个 $k[h]_{(h-h_0)}$ 上均不存在第一类例外曲线；泛曲线光滑、射影、几何整、亏格一且全局函数仅为泛底域。
这些正是正亏格最小模型唯一性的使用条件。[MIN]

给定新函数域同构后，定理将它和逆唯一延拓，而不是仅断言存在某个未标记模型同构。
局部模型与态射有限呈示，因而 DVR 上的同构和逆可展开到某个基底邻域；重叠上因泛纤维概形稠密及目标分离而相同。
同样的唯一性将动力等式延拓到全基。尖点不妨碍这一步的正则最小模型同构；它只不属于后面的节点作用计算。
一般 $r$ 的 torsor 可能未平凡不构成本自治论证的反例。[C] 的旧 (10) 本身又已给局部完整模型同构，不能重新列为缺失。

### 4.3 torsor equalizer 保留全部基向厚度

对 $E$-torsor $X$，作用图
$E\times_C X\to X\times_C X$、$(g,x)\mapsto(gx,x)$ 是同构；
对角线对应 $O\times_C X$。沿截面图 $(Q,x)$ 拉回，即得到
$\operatorname{Fix}(\tau_Q)=X\times_C Z(Q)$ 的闭概形恒等式。
它对任意测试概形成立，未要求 $n$ 可逆。

取 $Q=nP$ 后，$P$ 泛非挠使 $D_n$ 不是整个基底；光滑零截面是 Cartier，正则一维基底上的非零拉回理想给有限有效 Cartier 除子，允许为空。
于是交点处固定理想为 $(\tau^{i_n})$；$i_n=0$ 时为单位理想。
它描述整个原纤维及各状态相同的基向厚度，而非仅描述剩余纤维的固定点集。

### 4.4 相对作用的源条件没有漏掉

$W/C^{\mathrm{ss}}$ 为 proper、flat、有限呈示的连通半稳定亏格一族，几何纤维不可约；
平面三次 adjunction 给纤维 dualizing sheaf 平凡，$O$ 是光滑截面。
Conrad Definition 2.1.2 与 Remark 2.1.13 的条件因此逐项满足。
其存在唯一性给的结构确实是 $G\times_C W\to W$，并非只有光滑群上的加法。[CON]

在 $P$ 处 $\partial F/\partial v=T\ne0$，所以 $P$ 及 $nP$ 是相对光滑群的截面。
这个作用与先前延拓的动力在泛纤维相同，故在完整半稳定模型相同。
节点 $1$-gon 的光滑群为 $\mathbb G_m$，标准正规化上为乘法，两个节点切角色是 $\chi$ 和 $\chi^{-1}$。
这里不需要假设原 $P$ 全局挠，也没有套用全局挠截面的线性化结论。

### 4.5 节点完整理想的独立核对

设 $R=k[[\tau]]$，节点的完成局部环由 [NODE] 为
$R[[\xi,\eta]]/(\xi\eta-b(\tau))$。
若 $b\in(\tau^2)$，关系属于三变量极大理想的平方，二维商的嵌入维数为三，与总空间正则相矛盾。
故 $b=\tau\cdot\mathrm{unit}$，调整一个分支参数后

$$ A=R[[\xi,\eta]]/(\xi\eta-\tau)\simeq k[[\xi,\eta]],\qquad \mathfrak m=(\xi,\eta). $$

以下 $Q=nP$，$\sigma=\theta_Q^*$ 为相应完成局部自同构。若 $Q(h_0)\ne O$，相对作用保持 $\xi\eta$，乘法群作用不交换两分支。
因此 UFD 中 $\sigma(\xi)=\xi U$、$\sigma(\eta)=\eta U^{-1}$。
其常数角色为非一的 $\kappa$ 或 $\kappa^{-1}$，所以 $U-1$ 为单位；完整差理想为 $\mathfrak m$。

若 $Q(h_0)=O$，在群的零截面选形式参数 $z$。
完成作用的定义域环为 $k[[z,\xi,\eta]]$，仍为 UFD，且
$\alpha^*(\xi)\alpha^*(\eta)=\xi\eta$、模 $z$ 为恒等。
因式分解不只排除交换，也排除其中一个像是单位或含两个分支因子：这些情形模 $z$ 均不可能分别成为 $\xi,\eta$。
故

$$ \alpha^*(\xi)=\xi U,\quad \alpha^*(\eta)=\eta U^{-1},\quad U(0,\xi,\eta)=1. $$

后一等式先给 $U-1=zV$ 的准确可除性，而非仅给一个线性 jet。
特殊节点的群参数 $z$ 与 $\chi-1$ 都是零点 uniformizer；乘法切角色的导数为非零标量，
所以 $V(0,0,0)\ne0$，即 $V$ 为单位。这里既有可除方向，也有“商为单位”的反向控制。
代入实际 $Q=nP$ 的 $z=a_n(\tau)$ 后，单位保持为单位；
$U^{-1}-1=-U^{-1}(U-1)$ 使两个坐标差具有同一准确标量因子。

因此

$$
\widehat{\mathcal I}_{\operatorname{Fix},q_0}
=(\xi(U-1),\eta(U^{-1}-1))
=a_n(\tau)(\xi,\eta)=\tau^{i_n}\mathfrak m.
$$

任意形式函数的差属于由坐标差生成的闭理想；Noetherian 完成环中的该有限生成理想是闭的，
所以这里确实是整个 equalizer 理想，不止切空间固定理想。
完全不必把 $U$ 的状态变量依赖消去。

当 $i_n\ge1$，乘 $\tau^{i_n}$ 识别
$(\tau^{i_n})/(\tau^{i_n}\mathfrak m)\simeq A/\mathfrak m=k$，给作者所写短正合列。
商 $A/(\tau^{i_n})$ 是一维 Cohen–Macaulay 环，无零维嵌入部分；核准确为节点新增的长度一部分。
当 $i_n=0$，没有 Cartier 纤维部分，商直接是 $k$。
对 $p\mid n$，以上仍适用，因为 $z$ 是群参数，不是把 $[n]$ 冒当可逆参数变化；
不可分性会改变 $a_n$ 的阶，本公式不计算这个阶。

### 4.6 从完成理想到原全局概形

在半稳定模型的全部光滑点，torsor 计算给理想 $\mathcal I_{D_n}\mathcal O_{\mathcal U}$。
在每个节点，余切呈示的关系为 $\eta\,d\xi+\xi\,d\eta=0$，
故 $\operatorname{Fitt}_1(\Omega^1_{\mathcal U/C})$ 的完成理想为 $(\xi,\eta)$；光滑点处则为单位理想。
这也与 Conrad Example 2.1.7 相符。[CON]

两侧理想 coherent；节点局部环 Noetherian，完成忠实平坦。[FF]
所以在完成环的准确相等可以降回局部环，并与光滑开集上的相等粘成

$$
\mathcal I_{\operatorname{Fix}(F_T^n)}
=(\mathcal I_{D_n}\mathcal O_{\mathcal U})\,
\operatorname{Fitt}_1(\Omega^1_{\mathcal U/C})
\quad\text{on } f^{-1}(C^{\mathrm{ss}}).
$$

不需另作未指定的形式坐标粘合；全局候选理想已经内蕴定义，完成只用于检验它与固定理想相等。

### 4.7 Manin 消费及所有边界

本人 FULL 读取 [MANIN]：接受出口准确为 $N_p\ne0$、$\deg N_p\le2p$，以及
$p\nmid n$ 的有限好点上 $i_n>1\Rightarrow N_p=0$。
因此若 $\delta(h_0)N_p(h_0)\ne0$，固定概形在该纤维形式邻域中要么空，要么理想准确为 $(\tau)$。
共同的厚纤维必要候选位置至多 $2p$ 个；存在性、准确厚度及节点标量未由此求出。

边界核查结论：

- $i_n=0$：好点无固定概形，坏节点仍有约化固定点，不误删它。
- $p\mid n$：结构式仍有效，Manin 必要条件没有跨越这个限制。
- $T=-27/256$：全基模型同构仍有效；节点公式仅在去掉 $h=9/8$ 的半稳定基上。
- 尖点的加法群闭点周期不决定其全形式固定理想，不能由本节点论证推出野厚度。
- $T=0$：原动力和坐标的本轮前提失效，不由非单位时间曲面／层的旧接受补足。
- 无穷边界 $D$：不在原 $\mathcal U$；没有给它的固定理想或交数。
- 真正分歧底变换 $\tau=\rho^e$：同一模型的理想等式可以拉回，但新环未必正则，不能重新冒用上述 UFD 证明。

## 5. Corrections、标准机制扣除与 Open Risks

**必要修正：无。** 本报告对四末端像、UFD 因子分配及完成理想生成的展开是独立核查细节，
不是发现后补上的额外科学假设，也无需为此改动冻结作者件。

必须扣除的标准数学机制包括：最小正则模型唯一性与稠密延拓、torsor equalizer、
不可约半稳定亏格一族的广义椭圆作用、节点乘法切角色、二维正则局部 UFD、
参数差为单位倍的形式代数、Fitting 非光滑理想及完成忠实平坦。
实际新书面增量是原自治显式带标记坐标及上述标准机制接到完整原 $\mathcal U$ 的清楚接口。
不能把所有这些标准环节与已接受的 $N_p$ 必要条件相加便宣布新的长文中心。
此判断支持当前不扩篇的范围处置；它不是全球先例穷尽、正式新意 FAIL 或整个原族耗尽证明。

在本报告限定的结构恒等式内没有未关闭数学 gap。
仍未供应的数学对象是实际 $D_n$、各允许候选点的准确截面阶／首非零系数，以及另行处理的尖点全形式作用。
本轮不计算这些对象，不扩展其他特征／参数，不启动旧候选、能量盘、论文项目、评分或试写测页。

## 6. 本人实际完整阅读与输入 SHA-256

FULL 指本人本轮读完全件；分段显示最终覆盖全件，不将初次工具输出截断算作全文。
局部阅读项的 SHA 绑定整文件，不冒称已读整件。

| 输入 | 本人实读 | SHA-256 |
|---|---|---|
| 工作区 AGENTS.md | FULL 1–28 | `73ff82bcf298285ef8c3b6a4d3e1dff80eedb7eeda93ea47a55334c862c43412` |
| docs/WORKFLOW.md | FULL 1–39 | `b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2` |
| research-review/SKILL.md | FULL 1–106 | `62859ebaa64be9915546b0ba8fb3464110bcfe015307fc33b15c97f03dc392a5` |
| proof-writer/SKILL.md | FULL 1–223 | `6d7b3094711f609814680ded62e19b8dd61801511a7d98b96c033894c939babe` |
| [A] | FULL 1–348 | `401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7` |
| [BASE] | FULL 1–121 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [FP] | FULL 1–167 | `9a70cd2dd9656689dfeb26a6890e35ab1bf5dd10a5eab28a38306578b2767fce` |
| [C] | FULL 1–372 | `734b3f218bc3f16c8565ebb688d82c66252367d28e3e6a0e38f3aa571094c72a` |
| [MANIN] | FULL 1–148 | `05a99ecd5cfd72315b8c4e0fc740062687824d4dcd8dc7cdcdb81f5f87bbb8fd` |
| [F] | 局部 350–405，含 Step 7 原积分与四末端表 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` |
| [R] | 局部 295–345，含 Step 6 相对光滑平移 | `9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c` |

## 7. 交付边界

唯一新增本文件；没有改 [A]、旧输入、索引、锁、失败、接受处置或其他作者稿。
未建立 P31 项目，未编译／投稿／上传／外发信件／付费调用；公开一手浏览和无文件输出的精确符号校验仅服务本限定独查。
终态复读和 SHA 校验后，报告文件行数及最终哈希向主控单独报告，不在文件内嵌自指哈希。

[A]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[BASE]: PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
[FP]: PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md
[C]: PAPER30_QPI_CLOSED_FIBRE_RETURN_CONJUGACY_ENTRY_V1_20260908.md
[MANIN]: PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md
[F]: PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md
[R]: PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md
[MIN]: https://stacks.math.columbia.edu/tag/0C9Y
[NODE]: https://stacks.math.columbia.edu/tag/0CBY
[CON]: https://math.stanford.edu/~conrad/papers/kmpaper.pdf
[FF]: https://stacks.math.columbia.edu/tag/00MC
