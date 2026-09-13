# Paper31：素域好纤维 p-primary 初始交数独立审查 V1

日期：2026-09-12 UTC。审查者：`/root/p31_pprimary_good_independent_v1`。
状态：`FRESH_BOUNDED_MATHEMATICS_PASS`；`route_applicability: NOT_APPLICABLE`。
本件仅审查指定新证明的数学正确性，不是完整候选四门票、Route 评价、价值／容量判断或论文验收。

## 1. 结论与准确范围

对 [G] 的 (P1)、(P2) 给 **PASS；必要数学修正：∅**。
结论绑定以下全部量词，不能去掉其中的素域、好纤维和点阶条件：

$$
p>3,\quad T\in\mathbf F_p^\times,\quad h_*\in\mathbf F_p,
\quad\delta(h_*)\ne0,\quad p\mid d,
$$

其中保持原对象

$$
W_h:\ v^2+huv-Tv=u^3-Tu^2,\quad P=(0,T),\quad O=[0:1:0],
$$

$$
\delta=h^4-h^3-8Th^2+36Th+16T^2-27T,
\quad d=\operatorname{ord}P(h_*),\quad i_n=(nP.O)_{h_*}.
$$

交数沿原参数 $z=h-h_*$，不相交时为零。接受的准确输出为

$$
i_d=1+\mathbf1_{\{8h_*=9\}},\qquad
i_n=\begin{cases}
0,&d\nmid n,\\
p^{v_p(n/d)}(1+\mathbf1_{\{8h_*=9\}}),&d\mid n.
\end{cases}
$$

没有接受扩域参数的分类、prime-to-$p$ 初始交数、坏纤维、无穷远、全局 $D_n$ 或一般高阶积分公式。
本件也不由该数学 PASS 推出 Paper31 准入、足够新颖性或22–30页容量。

## 2. 独立性、输入及依赖身份

本人 FULL 读取新作者稿 [G]，随后 FULL 读取指定旧 [PF] 和接受处置 [D]。
旧稿只供应已接受的模型识别、泛非挠性、$j\notin k(h)^p$、点数同余和显式 $\lambda$ 接口；
未重新表决旧素域充要证明、F5证书或固定概形论证。

| 本人实际读取的输入 | 行数 | SHA-256 |
|---|---:|---|
| [G] | 254 | `38805df5657731f6698b3fcc3356269cb02da2e2c952779b5750ec6fe8442449` |
| [PF] | 325 | `de9cdb5ee8fef26b50365e6794e148f7206c4c167738143fc28e77159b0debef` |
| [D] | 176 | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |

工作入口 FULL 读取 `AGENTS.md`、`docs/WORKFLOW.md` 和 research-review 技能。
本席没有读取本轮新 PFforcing、good-contact、节点作者稿或任何其它 fresh 报告；
没有联系作者、作者 helper、旧审查者或其它审查席校准，也没有委派本人关键核验。
唯一向主控报告进度；本结论不继承作者的自评或来源读取层级。

research-review 技能所列 GPT-5.4 Codex MCP 未配置：按授权以当前可用 Codex xhigh 独立席完成。
不冒称已调用 GPT-5.4、跨模型复核或取得 MCP `threadId`。
技能的有据批评和逐项依赖核对用于本件；其通用 ML 评分／实验建议不扩张本次数学任务。

## 3. 逐项核验总表

| 核验义务 | 结论 | 核心依据 |
|---|---|---|
| $p\mid d$ 导出普通性和 $d=mp$，含 $p=5,d=10$ | PASS | 点数同余、Hasse 界；$m=1$ 或仅在 $p=5$ 时为2 |
| $FQ(h_*)$ 非零且生成 $\ker V$ | PASS | $Q=mP$ 准确阶 $p$；Frobenius 保持几何点的准确阶 |
| 实际有限 étale 的 Igusa 级结构提升 | PASS | $\ker V\setminus O$、准确四阶点分别为有限 étale 数据 |
| 所选 $Q_0$ 与 $\alpha$ 兼容 | PASS | UV §3.2；Broumas §3.2 的 $c_{\rm gal}$ 明确配对 |
| UV (3.1) 在原短模型的拉回及权重 | PASS | 权重 $-2$；$d(u^p)=0$；局部好模型缩放因子是单位 |
| $R^p$ 下降与移动平移的全可加性 | PASS | 水平导数同群律相容；两个变量切向量均计入 |
| 原点形式参数及单位微分因子 | PASS | 直接计算 $v'=w'^3U$、$H(0)=1$ |
| 低阶积分排除不可见 $p$ 次幂 | PASS | $\ell+1\le2<p$，故所有更低正指数可逆 |
| $V$ étale 保持原 $h$ 交数 | PASS | 原点形式映射线性项单位；基参数不变 |
| $q=0$ 普通点、特殊时间及全部倍数 | PASS | 原 $\lambda$ 的一阶零；特殊时间只删该坏点；普通形式群传播 |

## 4. 点阶、普通性与真实局部提升

以 [PF] 的已接受同余 $\#E_{h_*}(\mathbf F_p)\equiv1-A_*\pmod p$ 为输入。
$p\mid d$ 强制 $A_*=1$，所以闭纤维普通，$A$ 在 $R=k[[z]]$ 为单位，
其中 $k=\overline{\mathbf F}_p$。常数扩张是平坦的，原有限交数不变。

对 $p\ge7$，$0<\#E(\mathbf F_p)<2p$，故点数为 $p$；
$p=5$ 时 Hasse 区间内的正5倍数为5或10。因此 $d=mp$，$m\in\{1,2\}$，
且 $m=2$ 仅可能为 $(p,d)=(5,10)$。没有把群阶为10误推成每个非零点皆为5阶。
原 $P$ 的一、二、三阶排除与旧输入一致，但此处已有 $p\mid d$，并不额外依赖它来排低阶。

令 $Q=mP$，则 $Q(h_*)$ 准确阶 $p$，$pQ=dP$。
相对 Frobenius 在几何点上单射，故 $FQ(h_*)$ 仍准确阶 $p$；
$VFQ(h_*)=[p]Q(h_*)=O$。它和 $Q(h_*)$ 都不是二挠点，
因而短模型仿射 $Y$ 坐标以及相应的 $Y'$ 坐标在闭点不为零。

普通好邻域上的 $V$ 有限 étale，$\ker V$ 秩 $p$。
严格 henselian 的 $R$ 把所选非零特殊点唯一提升为 $Q_0\in\ker V(R)$。
其倍点在闭点已是 $p$ 个不同点，故 $Q_0$ 确为整个有限 étale 核的生成元。
这不是任意超越形式截面：取 $\ker V\setminus O$ 中经过所选点的 étale 邻域即可代数化。

再对 $E[4]$ 中准确四阶点做同样提升；$4$ 与 $p$ 互素保证该数据有限 étale。
两数据的纤维积在所选点仍 étale。于是所得光滑代数邻域 $U$ 携带
椭圆曲线、准确四阶点和 $\ker V$ 生成元，正给出 UV §3.1 要求的
$\operatorname{Ig}_1(4)$ 级结构及普适曲线拉回。没有用纯形式点冒充函数域级结构。

$U\to\mathbb A^1_h$ 在所选点 étale 且几何剩余域为 $k$，故完成环仍是 $k[[z]]$。
另一方面 $U\to\operatorname{Ig}_1(4)$ 无需 étale：这两个映射不能混淆。
已接受 $dj\ne0$ 在有限可分扩张下保持，尤其模映射非恒定，泛点拉回适用。

## 5. 兼容生成元、原模型与 UV 微分

实际使用的来源接口仅是 UV §3.2 的 (3.1) 第一式及其级结构设置，
不是 Proposition 3.3 的局部估计或 Igusa 除子阶的直接移植。
本人另读 Broumas §3.2：Verschiebung 函数域扩张的 Artin–Schreier 生成元 $\zeta$
满足 $\zeta^p-A\zeta=YM(X)$，其平移差给

$$
c_{\rm gal}(S)=\zeta(B+S)-\zeta(B),\qquad S\in\ker V,
$$

且非零 $S$ 的值满足 $c_{\rm gal}(S)^{p-1}=A$，不依赖允许的测试点 $B$。
因此本文所需兼容根是所选 $Q_0$ 对应的 $\alpha=c_{\rm gal}(Q_0)$。
UV 明确沿用这一配对；并非从任意 Hensel 根推出对任意生成元均有同一等式。
若换 $Q_0$ 为 $rQ_0$，$r\in\mathbf F_p^\times$，则换根为 $r\alpha$；
微分速度也乘 $r$，总因子 $r^{p-1}=1$。这给出配对相容性的直接复核。

由来源得到原模型中

$$
\lambda=\alpha^{p-2}\frac{dX'(Q_0)}{2Y'(Q_0)}.
$$

本人独核权重如下。两短 Weierstrass 模型在 $p>3$ 下的原点保留同构为
$X=u^2\widetilde X,Y=u^3\widetilde Y$；短模型条件排除了额外平移项。
在对应好最小模型上 $u$ 为单位，且

$$
A=u^{p-1}\widetilde A,\quad \alpha=u\widetilde\alpha,
\quad\lambda=u^{-2}\widetilde\lambda.
$$

最后一个等式也直接来自 $\lambda=(a_4/18a_6)dj/j$ 的权重。
Frobenius 坐标满足 $X'=u^{2p}\widetilde X',Y'=u^{3p}\widetilde Y'$，
取基微分时 $d(u^{2p})=0$，所以商微分恰乘 $u^{-p}$。
右侧总权重为 $u^{p-2-p}=u^{-2}$，与左侧一致。
这确认等式落在原 $X=u+s/12,Y=v+(hu-T)/2$，不是异模型中的阶数替代。

等式先在实际代数邻域的泛点成立，再以有理微分恒等式延至当前点；
$A,\alpha,Y'(Q_0),\delta$ 在这里均为单位。
全过程不除以 $\lambda$，因而不需要假定 $q(h_*)\ne0$。

## 6. 水平导数与原点计算的独核

$E'$ 的方程、群律和零截面定义于 $R^p=k[[z^p]]$；
连续 $k$-导数 $D=d/dz$ 杀掉 $R^p$，因而产生作者所用的水平提升 $D_h$。
对截面 $S$，$D\circ S^*-S^*\circ D_h$ 是基上为零的相对切向量。
用不变微分配对后，在 $Y'(S)$ 为单位的图上确为 $DX'(S)/(2Y'(S))$。
这不是把相对微分沿截面错误拉成基微分。

设 $m$ 是群加法。因 $m$ 下降至 $R^p$，有
$\theta_D(m(S_1,S_2))=dm(\theta_D(S_1),\theta_D(S_2))$。
不变微分对这两个切向量的配对相加，故

$$
L_D(S_1+S_2)=L_D(S_1)+L_D(S_2),\qquad L_D(-S)=-L_D(S).
$$

此推导包含两个移动点，而非仅对固定平移的相对微分不变性作引用。
$FQ$ 的坐标是 $p$ 次幂，故 $L_D(FQ)=0$；对于 $Z=FQ-Q_0$，有

$$
Z(0)=O,\quad VZ=dP,\quad
L_D(Z)=-L_D(Q_0),\quad
\operatorname{ord}_zL_D(Z)=\operatorname{ord}_{h_*}\lambda=\ell.
$$

原模型已接受的 $\lambda=-(8h-9)\delta^{-1}dh$ 给 $\ell=0$ 或1。
$dh=dz$，$8\ne0$ 且 $\delta$ 是单位，故 $q=0$ 时是准确一阶，不是下界。

在 $O$ 附近改用 $w'=-X'/Y',v'=-1/Y'$，直接代方程得到

$$
v'=w'^3+a_4^pw'v'^2+a_6^pv'^3=w'^3U(w'),
\quad U\in R^p[[w']],\quad U(0)=1.
$$

隐函数方程对 $v'$ 的线性系数为单位，递归解确实只用 $R^p$ 系数。
再用 $X'=w'/v',Y'=-1/v'$ 直接求微分得到

$$
\frac{dX'}{2Y'}=-\frac12dw'+\frac{w'}{2v'}dv'
=\left(1+\frac{w'U'(w')}{2U(w')}\right)dw'.
$$

故 $H(w')=1+w'U'/(2U)$ 是单位，$L_D(Z)=H(w'(Z))D(w'(Z))$。
此式在原点有效，不在原点非法使用仿射单位 $Y'$ 的论证。

写 $f=w'(Z)=\sum_{j\ge1}c_jz^j$。
$\operatorname{ord}Df=\ell\le1$ 强制 $(\ell+1)c_{\ell+1}\ne0$；
所有 $1\le j<\ell+1$ 均小于 $p$，所以 $jc_j=0$ 强制 $c_j=0$。
导数不可见的正指数至少为 $p$，大于 $\ell+1$，不能藏一个更低首项。
因此 $\operatorname{ord}f=\ell+1$，且该论证没有推广至 $\ell+1\ge p$。

最后 $V$ 在原点 étale 给 $w(VS)=c\,w'(S)+O(w'(S)^2)$，$c\in R^\times$；
各系数虽可随 $z$ 变化，但不会降低正赋值首项，故
$(VZ.O)_{h_*}=(Z.O)_{h_*}=\ell+1$。
广义模型和短模型的零截面局部理想都由其形式参数生成，故这就是原 $i_d$。

## 7. 特殊分支、传播与来源扣除

$p=5,d=10$ 时用 $Q=2P$ 后闭点准确阶5，以上全部单位和 étale 条件仍成立。
没有增设 $d=p$、$m=1$ 或 $p\ge7$ 等隐藏假设。

对 $q=0$，本人直接核对
$\delta(9/8)=16T^2+(27/8)T+729/4096=(256T+27)^2/4096$。
因此只在 $T=-27/256$ 时该能级本身是坏点而被排除；没有整体删去特殊时间。
其它 $q=0$ 好点若同时 $p\mid d$，其普通性由 $A_*=1$ 保证，交数准确为2。
Igusa 上普通点的微分无零与这里无冲突：其向原基的拉回可以因模映射分歧而有零；
实际保持原参数的是另外的 étale 邻域映射。本证明使用显式拉回微分，不移植源除子阶。

传播另可直接验证：$d\nmid n$ 时特殊点不为 $O$，故 $i_n=0$。
对 $n=drp^e$、$p\nmid r$，$[r](w)=rw+O(w^2)$ 保持正赋值。
由 $[p]=VF$ 且 $w'\circ F=w^p$，普通点有
$[p](w)=c_pw^p+O(w^{2p})$，$c_p$ 为单位。
因此每次乘 $p$ 准确把赋值乘 $p$，不需额外全局条件。

Naskręcki Lemma 8.2 的 $m(v)=d,h_{E,v}=0$ 特例正是该 $p^e$ 传播因子。
本件实读其原陈述及证明，明确扣除它，不把传播计为新理论；
作者自足普通证明亦已独核，所以不靠未检查的全局适用性传递局部结论。
UV/Broumas 微分、Igusa 级结构、Hensel、群律切映射与形式群都是来源或标准机制。
本件不评价这些扣除后剩余的研究价值／容量。

## 8. 实际来源读取与执行边界

- [UV]：本人实读官方 arXiv HTML §2 模型权重、(2.2)、Example 2.6、Remark 2.8，
  以及 §3.1–3.2 全部至 Corollary 3.5（网页逻辑行261–354）。使用范围限于级结构及 (3.1) 第一式。
  保留页头 `v1 / 08 Aug 2025` 与正文日期 `August 24, 2026` 的差异，不推断另一个版本。
- [B]：本人读取 Cambridge 官方 PDF 的首页范围说明，并定向实读 pp.127–131，
  包括 §2.4–2.6、§3.1–3.2、Theorem 4.1 及证明、§4.1 的 (12)–(13)。
  它使 $c_{\rm gal}$ 兼容和水平加法机制可核验；$p>3$ 的本件公式接口仍以 UV 明确设置为准，
  不由旧首页文本中的 $p>5$ 猜测扩大范围。没有冒称本轮读完17页原件。
- [N]：本人实读官方 PDF 文本 pp.1003–1005，含 §8 设置、Lemma 8.2 全陈述及证明。
  截图调用未在本席输出可读图像，不声称完成视觉 PDF 验收；所需公式依据可读正文核对。

本轮未把搜索摘要当作证明，也未消费未读的 Igusa 原始专著或其他转引证明。
Numdam／候选链接访问未成功后已通过实际检索找到并读取 [B] 官方原件；失败响应不作证据。
未运行任何新质数、扩域、有限参数采样或数值实验；上面的多项式及形式局部计算是书面独核。
仅以 `apply_patch` 新增本报告；其余本地输入只读，未修改冻结稿、接受处置或索引。
未创建项目／锁／论文／PDF，未编译，亦无投稿、上传、托管、push、发信或付费资源操作。
终态本人 FULL 自读本报告，行数与 SHA-256 在交付时外报，不将自哈希递归写入正文。

[G]: PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[D]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1#S3
[B]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/95814903A024FCB1B2C13CA8778759DA/S0010437X97000365a.pdf/effective-p-descent.pdf
[N]: https://nyjm.albany.edu/j/2016/22-46v.pdf
