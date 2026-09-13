# Paper29 新问题预筛：全周期的加权边界与对称性破缺障碍

日期：2026-09-06。范围：P20 原四维梯度剪切族的复周期几何；新建本报告，其他项目和历史证明只读。

## 结论与决策

**决策：STOP，不创建正式 Paper29。** 原主问题“对所有周期，固定平面 $L$ 外的周期 scheme 是否有限”仍为 **NOT CURRENTLY JUSTIFIED**，本轮没有原映射的正维周期分量反例。

本轮有一个可完整核验、量词覆盖所有周期的新几何约束，而不只是重算原映射的 $n=2,3$：一个辛加权退化把原映射送到四次剪切边界；动量的精确缺陷给出整个周期族闭包的饱和理想方程。它排除 $g=6$ 时一个确切的非固定边界周期层，并对该层的全部偶数迭代同时成立。

同时，边界映射存在真实的 $\mathbb C^*$ 正维周期族，直接否定“该加权主部没有非固定正维周期层，因此自动得到紧性/横截性”的便捷机制。当 $8\mid g$ 时，新方程在这一边界族上恒等消失，第一层对称性破缺检测也确实失效。

这既不是全局有限性证明，也不是一个自然达到 22–30 页的定理包。保守估计本轮新增的独立证明内容约 **3–5 页**；生成函数表达式与已有实周期、局部固定 scheme 结果均不能再计作新篇幅。没有给新意、独立价值、正文容量或产物验收 PASS。

`route_applicability: NOT_APPLICABLE`。本报告没有 Route A/B、RH、算术动力行列式、熵等式或 PDF 验收主张。普通高度文献在这里仅用于检查可援引定理的适用条件，不提出算术轨道构造。

## 1. 输入、技能与已知边界

全文读取工作区 `AGENTS.md`、`docs/WORKFLOW.md`、`BATCH_07_CONTEXT.md`、[前轮结构预筛](PAPER29_NEXT_STRUCTURAL_VIABILITY_20260905.md)，以及 `idea-creator`、`research-lit`、`proof-writer` 的技能说明。已核读 P20 接受 PDF 的前三页和其参考文献，确认该论文处理次数而没有周期分类定理。

采用 `idea-creator` 的对象—假设—可证机制—价值筛选、`research-lit` 的本地优先和一手来源检查、`proof-writer` 的完整命题/证明/缺口区分。任务限定一个机制的有界纯数学预筛，故不机械生成 8–12 个候选，不运行 GPU，不扩张成完整查新或外部 LLM 审查；当前可调用工具中也没有该技能示例中的跨模型审查接口。没有把工具缺项解释为主问题的科学障碍。

旧报告已经证明以下内容，本轮不重开也不计新增：

- 复固定点集为 $L=\{q_1=p_2=0\}$；
- 所有实周期点均在 $L$；
- 对各个 $n$，$\operatorname{Fix}(F_g^n)$ 的理想在包含整个 $L$ 的开邻域内等于固定点理想，故其他周期分量与 $L$ 不交。

不复活旧 trace-coordinate、周期迹选取、取消或直积中心化子候选。不以本报告补充旧候选的正文页数。不声称得到新的中间动力次数模型。

相关输入的 SHA256：

| 输入 | SHA256 |
| --- | --- |
| `PAPER29_NEXT_STRUCTURAL_VIABILITY_20260905.md` | `9ea5943cfc3ae65c764f6ec59ed971e9452eeaeb64ab222f75c6829d4285fbd7` |
| P20 `paper/main.tex` | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| P20 `paper/main.pdf` | `ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9` |

## 2. 精确对象与真正待证主张

写
$$
(x,y,u,v)=(q_1,q_2,p_1,p_2),\qquad
\omega=dx\wedge du+dy\wedge dv.
$$
固定偶数 $g\ge6$。本轮以 $g=6$ 为最低成本试验，但下面引理保留明确的 $g$ 依赖。

原映射是 $F_g=T_{W_g}S_{V_g}$，其中
$$
V_g=x^2y^2+x^g,\qquad W_g=u^2v^2+v^g.
$$
所需全局主张为：对所有 $n\ge1$，
$$
Z_{g,n}=\operatorname{Fix}(F_g^n)|_{\mathbb A^4\setminus L}
$$
是有限 scheme。此处“有限”不仅是某个算出的点集有限，也不是一般定理对**已经孤立的点**提供指数增长上界。

本轮引入的系数参数是退化工具，不更换所研究的非零参数系统。令 $F_{g,\varepsilon}$ 的两个势为
$$
V_{g,\varepsilon}=x^2y^2+\varepsilon x^g,
\qquad W_{g,\varepsilon}=u^2v^2+\varepsilon v^g.
$$
明确记其一步更新为
$$
\begin{aligned}
U&=u+2xy^2+g\varepsilon x^{g-1},&
V&=v+2x^2y,\\
X&=x+2UV^2,&
Y&=y+2U^2V+g\varepsilon V^{g-1}.
\end{aligned}                                                    \tag{1}
$$
$F_{g,\varepsilon}(x,y,u,v)=(X,Y,U,V)$。在 $\varepsilon=0$ 时写 $F_0$；该边界映射与 $g$ 无关。

## 3. 完整引理包

### Claim

下列四条均成立。

1. 对 $t\in\mathbb C^*$，辛线性变换
   $$
   D_t(x,y,u,v)=(tx,t^{-1}y,t^{-1}u,tv)
   $$
   满足
   $$
   D_t^{-1}F_gD_t=F_{g,t^g}.                              \tag{2}
   $$
   因而所有非零参数的系统均与原映射共轭，$F_0$ 是这个确切加权图中的边界。
2. 设 $J=xu-yv$。对所有 $n\ge1$，在 $R=\mathbb C[\varepsilon,x,y,u,v]$ 中令
   $$
   z_k=F_{g,\varepsilon}^k(z),\qquad
   I_n=(F_{g,\varepsilon}^n(z)-z),
   $$
   $$
   B_{g,n,\varepsilon}(z)=
   \sum_{k=0}^{n-1}(x_k^g-v_{k+1}^g).
   $$
   则
   $$
   B_{g,n,\varepsilon}\in I_n:\varepsilon
   \ \subseteq\ I_n:\varepsilon^\infty.                  \tag{3}
   $$
   因此非零参数周期 scheme 在 $\mathbb A^1\times\mathbb A^4$ 中的 scheme-theoretic 闭包，其特殊纤维被 $B_{g,n,0}=0$ 所包含。
3. 每个满足 $a^4=-1$ 的 $a\in\mathbb C$ 都给出一个闭曲线
   $$
   C_a=\{xy=a,\quad u=-ay,\quad v=-ax\}\simeq\mathbb C^*.
                                                               \tag{4}
   $$
   $F_0$ 在 $C_a$ 上为 $z\mapsto-z$，故每个点的最小周期恰为 $2$。特别地，全部偶数 $n$ 的边界固定 scheme 均含有该正维曲线。
4. 若 $8\nmid g$，则对每个偶数 $n\ge2$，上述非零参数周期闭包的特殊纤维与每个 $C_a$ 都不相交。若 $8\mid g$，则方程 (3) 在每个 $C_a$ 上恒等消失，不能排除其成为退化极限。

### Status

**PROVABLE AS STATED**（仅指上列四条）。原全局有限性主张仍 **NOT CURRENTLY JUSTIFIED**。

### Assumptions、Notation 与依赖

底域为 $\mathbb C$，$g$ 是固定偶整数且 $g\ge6$，$n$ 是任意正整数；不要求 $n$ 为最小周期。$I_n$ 保留 scheme 理想而不先取根。饱和理想定义为
$$
I_n:\varepsilon^\infty
=R\cap I_nR[\varepsilon^{-1}].
$$
证明依赖只有：(1) 的直接代入、一个二次多项式的差属于坐标差理想、局部化后收缩给出开集 scheme 的闭包，以及 $a^4=-1$ 的根恰为本原八次单位根。没有使用周期点孤立性、紧性、泛型横截性或未算出的动力次数。

### Proof

**Step 1：精确共轭。** 每个辛配对 $(x,u)$、$(y,v)$ 的两个缩放因子乘积均为 $1$，所以 $D_t^*\omega=\omega$。把 $D_tz$ 代入第一剪切，得到
$$
U_{\mathrm{orig}}=t^{-1}(u+2xy^2+gt^g x^{g-1}),\qquad
V_{\mathrm{orig}}=t(v+2x^2y).
$$
再代入第二剪切，两个 $q$ 坐标分别为
$$
X_{\mathrm{orig}}=t(x+2UV^2),\quad
Y_{\mathrm{orig}}=t^{-1}(y+2U^2V+gt^gV^{g-1}),
$$
这里括号中的 $U,V$ 正是参数 $\varepsilon=t^g$ 的更新。应用 $D_t^{-1}$ 得到 (2)。任意非零 $\varepsilon$ 在 $\mathbb C$ 中有 $g$ 次根，所以非零纤维均共轭。

**Step 2：动量缺陷。** 第一剪切的动量变化为
$$
xU-yV-(xu-yv)=g\varepsilon x^g,
$$
因为两个四次项相消。第二剪切给出
$$
XU-YV-(xU-yV)=-g\varepsilon V^g.
$$
故整个映射满足多项式恒等式
$$
J(F_{g,\varepsilon}z)-J(z)
=g\varepsilon(x^g-V^g).                                \tag{5}
$$
将 (5) 沿 $n$ 步轨道相加，即得
$$
J(F_{g,\varepsilon}^nz)-J(z)
=g\varepsilon B_{g,n,\varepsilon}(z).                  \tag{6}
$$
左边属于 $I_n$；例如对 $x_nu_n-xu$ 用
$(x_n-x)u_n+x(u_n-u)$，对 $y_nv_n-yv$ 用相同的两项展开即可。由于 $g$ 在底域中可逆，$\varepsilon B_{g,n,\varepsilon}\in I_n$，证明 (3)。

**Step 3：闭包与特殊纤维。** 在 $\varepsilon\ne0$ 上的周期 scheme 的闭包理想是
$K_n=I_n:\varepsilon^\infty$。由 (3)，$B_{g,n,\varepsilon}\in K_n$；在特殊纤维理想
$(K_n+(\varepsilon))/(\varepsilon)$ 中因此有 $B_{g,n,0}$。这证明的是 scheme 包含，而非只对一组已找到的周期点成立。

特别地，若某个形式弧 $z(s)\in\mathbb C[[s]]^4$、非零 $\varepsilon(s)\in s\mathbb C[[s]]$ 满足
$F_{g,\varepsilon(s)}^nz(s)=z(s)$，则 $B_{g,n,0}(z(0))=0$。这也直接由 (6) 在整环 $\mathbb C[[s]]$ 中消去 $\varepsilon(s)$ 得到，不要求闭包光滑或该弧是约化分支。

**Step 4：边界周期族。** 在 $C_a$ 中，$x\ne0$ 且
$$
y=a/x,\qquad u=-a^2/x,\qquad v=-ax.
$$
在 $\varepsilon=0$ 时，(1) 的第一剪切给
$$
U=a^2/x=-u,\qquad V=ax=-v.
$$
第二剪切给
$$
X=x+2a^4x=-x,\qquad
Y=a/x+2a^5/x=-a/x=-y,
$$
其中用了 $a^4=-1$。故 $F_0z=-z$，且 $-z\in C_a$。由于 $x\ne0$，没有点满足 $z=-z$，最小周期恰为 $2$。

**Step 5：全部迭代的边界排除和失效。** 对偶数 $n$，$C_a$ 上轨道只是 $z,-z$ 的重复。因 $g$ 偶，
$$
B_{g,n,0}|_{C_a}=n x^g(1-a^g).                          \tag{7}
$$
每个 $a^4=-1$ 都具有精确阶 $8$，所以 $a^g=1$ 当且仅当 $8\mid g$。若 $8\nmid g$，(7) 在 $C_a\simeq\mathbb C^*$ 的坐标环中是一个单位：$n(1-a^g)\ne0$ 且 $x$ 可逆。因此特殊纤维与 $C_a$ 的 scheme 交为空。若 $8\mid g$，(7) 恒为零；这一方程没有排除力，但并不证明曲线真的提升。

对奇数 $n$，$C_a$ 本来就与 $\operatorname{Fix}(F_0^n)$ 不交；无需以 (7) 讨论它。因此在 $g=6$ 时，这一具体非固定边界层被所有周期的非零纤维闭包排除。四条命题全部得证。$\square$

### 精确几何含义

取 $t\to0$ 且归一化坐标趋于 $C_a$ 上一点，则原坐标 $D_tz$ 满足
$$
q_1,p_2=O(t),\qquad q_2,p_1=O(t^{-1}).
$$
这确实是原相空间的一个无穷远方向，而非固定平面上有限点的邻域。上述引理说明：$g=6$ 时，一个原映射的 $n$ 周期分支不能通过这个精确缩放图，以 $C_a$ 为归一化非固定极限。

**该图没有被证明覆盖所有无穷远分支。** 其 $t=0$ 纤维也不只有 $C_a$；对其他 $F_0$ 周期轨道，$B_{g,n,0}$ 是否消失尚未分类。故“排除这一层”不蕴含“$L$ 外周期分量有限”。

## 4. 为什么生成函数和加权主部不能直接补齐主问题

周期方程的有限维作用量确实可写成
$$
\mathcal A_{g,n,\varepsilon}
=\sum_{k=0}^{n-1}\left[
(q_{k+1}-q_k)\cdot p_{k+1}
 +V_{g,\varepsilon}(q_k)-W_{g,\varepsilon}(p_{k+1})
\right],                                                \tag{8}
$$
其中所有指标模 $n$。对 $q_k$、$p_{k+1}$ 的偏导分别是
$$
p_k-p_{k+1}+\nabla V_{g,\varepsilon}(q_k),\qquad
q_{k+1}-q_k-\nabla W_{g,\varepsilon}(p_{k+1}).
$$
所以临界 scheme 与带标记周期序列 scheme 相同；由确定性的更新逐次消去变量，又与 $\operatorname{Fix}(F_{g,\varepsilon}^n)$ 同构。这一表达不提供临界点孤立性。环境有 $4n$ 个变量和 $4n$ 个偏导，不能据此把临界 scheme 当作零维完全交；正维分量正是需要证明排除的对象。

沿 $D_t$ 同时缩放全部时刻时，(8) 的动力学配对项和四次势项不变，只有
$\varepsilon\sum_k(x_k^g-v_{k+1}^g)$ 具有权重 $g$。因此 (3) 也可以看成精确的对称性破缺方程；这不是一个新的“生成函数存在定理”。

边界临界 scheme 包含 (4) 的曲线，故“边界临界点全部孤立”在这里明确为 **REFUTED**。另一方面，特殊纤维出现额外周期曲线，并不证明这些曲线能提升到非零参数；(7) 在 $g=6$ 时恰好说明这类推断是错误的。

## 5. 有界一手文献核对

检索日期：2026-09-06。先核对 P20 本地 PDF 与参考文献；外部检索覆盖高维多项式自同构周期子簇、孤立周期点增长、正则自同构高度、Hénon-like 周期交和 generating families，使用超过五种查询表达。当前任务限于适用性/潜在覆盖预筛，未将“未搜索到相同公式”解释为优先权或完整新颖性认证。

| 一手来源 | 已核实内容与本题边界 |
| --- | --- |
| Shu Kawaguchi, *Local and global canonical height functions for affine space regular automorphisms*, Algebra & Number Theory 7 (2013), 1225–1252，[正式全文](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-p.pdf)，尤其 Definition 2.1、Theorem 6.3、Corollary 7.3 | 假设正逆无穷远不定集不交；建立 canonical height 和周期点高度有界。本映射不满足该正则性，不能直接援引。 |
| Tien-Cuong Dinh、Nessim Sibony, *Equidistribution of saddle periodic points for Hénon-type automorphisms of $\mathbb C^k$*, Mathematische Annalen 366 (2016), 1207–1251，[作者预印本](https://arxiv.org/abs/1403.0070) | 研究 Hénon-type/regular 自同构。未给出从本非正则四维剪切到该类别的模型，故不是剩余周期交有限性的即用定理。 |
| Tien-Cuong Dinh、Viet-Anh Nguyen、Tuyen Trung Truong, *Growth of the number of periodic points for meromorphic maps*, Bulletin of the London Mathematical Society 49 (2017), 947–964，[作者预印本](https://arxiv.org/abs/1601.03910) | 一般紧 Kähler 情形下对**孤立周期点计重数**给指数增长上界。这个结论不能消除正维周期分量；若将来证明有限，上界本身也不应包装成独立新贡献。 |
| Tien-Cuong Dinh、Guolei Zhong, *Periodic points for meromorphic self-maps of Fujiki varieties*, 2023 预印本，[原文摘要](https://arxiv.org/abs/2312.02533) | 一般情形仍控制孤立点的增长；精确渐近部分要求拓扑次数严格支配其他动力次数。本自同构的拓扑次数为 $1$ 而已有 $\lambda_1>1$，该支配条件不可能成立。 |
| Muhan Luo、Qi Zhou, *Equidistribution of saddle periodic points for Hénon-like maps*, 2025 预印本，[原文 §1–2](https://arxiv.org/html/2502.20103v1) | Theorem 1.1 要求有实际的水平/垂直 Hénon-like 定义域与条件 $d>\max(d_{p-1}^+,d_{k-p-1}^-)$。本轮没有构造覆盖所有剩余周期点的此类定义域，也没有验证该条件。 |
| Long Wang, *Periodic points and arithmetic degrees of certain rational self-maps*, 2022 预印本（核读 v4），[Theorem 1.1](https://arxiv.org/html/2201.12750v4) | 需要 cohomological hyperbolicity，并移去一个 proper closed subset、要求整条周期轨道避开它，才得到高度有界。本题缺支配中间动力次数的证明，也没有理由认定其例外集合恰为 $L$。 |
| Yohsuke Matsuzawa、Kaoru Sano, *On the height boundedness of periodic and preperiodic points of dominant rational self-maps on projective varieties*, 2026 预印本，[原文引言及 §2](https://arxiv.org/html/2603.09010v1) | 作者给出三维仿射自同构的孤立周期点高度无界反例。故“任意高维多项式自同构的孤立周期点高度有界”不是可用普遍定理。该反例不是本 $F_g$ 的反例，也不否定固定次数扩域上的其他有限性陈述。 |
| Marc Chaperon, *Singularities in contact geometry*, Banach Center Publications 62 (2003), 39–55，[作者全文 §2.2](https://webusers.imj-prg.fr/~marc.chaperon/Varsovie.pdf)，[出版社卷页记录](https://www.impan.pl/pl/wydawnictwa/banach-center-publications/pl/wydawnictwa/banach-center-publications/all/62) | 通过增加中间变量构造复合辛映射的 generating family 已是既有机制。生成族的辅助变量横截性与固定点/周期临界交横截性不是同一命题；不能把式 (8) 的存在算作解决全局周期几何。 |

对第一、第二条适用性障碍可在原坐标直接核验，无须新建模型：$g\ge6$ 时 $\deg F_g=\deg F_g^{-1}=3g-3$；最高齐次坐标分别只有 $q_2$ 方向的非零常数倍 $(x^2y)^{g-1}$ 和 $p_1$ 方向的非零常数倍 $(uv^2)^{g-1}$。因此在 $H_\infty\simeq\mathbb P^3$ 上
$$
I^+=\{xy=0\},\qquad I^-=\{uv=0\},
$$
两者都包含 $L_\infty=\{x=v=0\}$。这里只是核查已知“非正则”阻断，不计为新的动力次数结果。

文献结论：既有生成族方法和孤立点增长定理确实覆盖一些容易误报的“成果”；正则/高度/Hénon-like 定理则有未满足的具体假设。本轮没有发现可直接消除全部剩余周期分量的现成定理，也没有据此认证主问题世界性开放。

## 6. 验证、未决风险与自然价值

### 实际检查

- 式 (2)–(7) 给出符号证明，覆盖指定的全部 $g,n$ 量词。
- 另作只读精确代数核验：在 $g=6,8$ 时展开式 (5) 的差，结果均为零；把 $y=a/x,u=-a^2/x,v=-ax$ 代入 $F_0+\mathrm{id}$ 并对 $a^4+1$ 取余，四坐标结果均为零。这是排错而非量词证明。
- 未计算原映射 $F_g^2$ 或 $F_g^3$ 的解集，未运行数值轨道拟合，未改任何阈值，也没有把退化极限的曲线计作原系统周期曲线。

### Open Risks

1. 尚未分类 $F_0$ 的所有非固定周期轨道以及 $B_{g,n,0}=0$ 在这些轨道上的零集。即使固定 $g=6$，也只排除了 (4) 的一个边界层。
2. 尚未证明所有周期曲线在无穷远都能被本次权重图或某个已控制的有限图集捕获。曲线可具有不同赋值，不能以本图替代完整紧化。
3. $8\mid g$ 时，本必要条件对 (4) 完全失效；需要更高阶的饱和条件或别的机制。不能把 $g=6$ 的局部有效性写成全 $g$ 有效。
4. 零维性、scheme 长度递推、非约化周期点分类和长度增长率全部未完成。式 (3) 只有包含方向，不能将其升级成完整饱和理想生成元。
5. 未证明该障碍在文献中全新。式 (5) 是短的离散 Noether 缺陷；式 (3) 的 scheme 版本比“周期求和”更适合控制退化，但自身尚不具备独立长文容量。

### 决策边界

本轮的实际增量是一个全周期边界约束、一个边界非孤立族以及一个精确的 $8\mid g$ 失效条件。它们比“尚可研究周期点”更具体，但仍不足以把 P29 从选题推进到正式写作。

**因此保持 STOP。** 不另立一个只研究上述短引理的小论文，不拼接已停止的 tracecharts 内容，也不重新提出没有新模型的 $\lambda_2$。如果主控继续其他真正新问题，本报告仅作为避免错误紧性/高度论证的有界研究记录。

要在本主问题上改判，至少必须新证一个覆盖所有剩余周期分量的全周期几何命题，或给出原 $F_g$ 的明确正维周期反例及有实质容量的结构分类；不能以更多低周期计算或重复现有局部引理替代。
