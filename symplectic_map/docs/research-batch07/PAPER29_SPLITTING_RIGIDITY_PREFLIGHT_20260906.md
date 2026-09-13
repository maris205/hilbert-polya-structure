# Paper29 新问题预筛：真实相空间分解与拉格朗日分布刚性

日期：2026-09-06。性质：有界查新与证明预筛；不是正式 Paper29，不是 Route 评价。

## 结论与处置

**作者预筛：STOP，不按当前材料创建论文。**

1. 非平方 $g\ge5$ 的 $F_g$ 不多项式共轭于两个平面多项式自同构的直积，已由 P20 的无理 $\lambda_1$ 加平面分类直接推出。这是必须扣除的短推论，不是新主问题。
2. 找到并完整证明了不同机制的结构引理：对每个 $g\ge5$、每个 $m\ge1$，任何 $F_g^m$ 不变的有理秩二拉格朗日分布，其 Grassmann 有理映射的不定集必须包含两张实际不变辛平面
   $$M=\{q_2=p_2=0\},\qquad N=\{q_1=p_1=0\}.$$
   证明利用真实不变曲线上的法向差分模，不使用 P20 的次数矩阵、已有共射线固定场或旧 trace/jet 结论。
3. **该引理没有证明全局无有理纤维化或 primitive。** 余维二不定集是实质缺口；§7 给出恰在 $M\cup N$ 退化的实际拉格朗日纤维化，说明不能把该缺口当作自动可去奇点。
4. 初始分布引理包的自然正文估计约 **7–11 页**。随后按主控提出的精确线索完成§11：一手 Galois reduction 桥给出三阶理想扰动稳定的非可积性准则，以及无扰动子族的可积性 iff。加入这些内容后，本代理的独立自然正文估计仍只有 **10–15 页**；没有可信的 22 页实质下界。原 22–30 页合取门保持不变。本报告不是把小引理追加到已停的 trace-charts 候选。

科学状态：§4–6 及§11 的明确命题为 `PROVED`；全局无曲面半共轭、全局无有理拉格朗日分布仍为 `OPEN / NOT CURRENTLY JUSTIFIED`。§11 不把“无完整第一积分组”偷换成“无不变叶状结构”。没有数值实验、PDF 构建或产物验收。

## 1. 输入、对象与技能范围

全文读取工作区 `AGENTS.md`、`docs/WORKFLOW.md`、`BATCH_07_CONTEXT.md` 及 `idea-creator`、`research-lit`、`proof-writer` 技能。最新任务继续保持原门，覆盖旧接续中的页数变更提请。

局部组合审计只使用 [P20–28 最近邻表](PAPER29_PORTFOLIO_AUDIT_20260905.md)、[P20 RQ](../../papers/20-coupled-shear-degree-matrix/notes/RESEARCH_QUESTION.md)，并阅读 P20、P21、P25 现存 PDF 的前三页。P21/P25 的高阶 Perron 值只作为已占据的次数研究基线，不据此构造虚假的相空间 quotient。

本任务只拥有此文件。没有修改旧稿、旧候选、锁、批次账本或正式项目。使用技能的影响是先扣除已知短推论、给出有界一手查新、最后将可证小引理与未证主结论分开。纯理论任务不启动 GPU pilot；当前工具不存在技能指定的外部 Codex review 接口，不声称完成该接口评审。下面的独立快查仅是同团队有界数学检查。

以下证明在 $\mathbb C$ 上进行。原 P20 以代数闭特征零域为背景；此报告不需要将文献中的复几何结果扩张到任意域。

固定
$$V_g(q_1,q_2)=q_1^2q_2^2+q_1^g,\qquad W_g(p_1,p_2)=p_1^2p_2^2+p_2^g,$$
$$S_g(q,p)=(q,p+\nabla V_g(q)),\qquad T_g(q,p)=(q+\nabla W_g(p),p),\qquad F_g=T_gS_g.$$
辛形式为
$$\omega=dq_1\wedge dp_1+dq_2\wedge dp_2.$$
为满足原筛选中的非平方偶数例子，可以取 $g=6$。新结构引理不需偶数或非平方，实际对每个整数 $g\ge5$ 成立。

## 2. 必须扣除的直接动态次数障碍

P20 已证明
$$\lambda_1(F_g)=g+1+2\sqrt g.$$
若 $H$ 是平面多项式自同构，则平面分类给出 $\lambda_1(H)=1$ 或一个至少为 $2$ 的整数；后者是循环约化 Hénon 字的次数乘积。参见 Friedland–Milnor, *Dynamical properties of plane polynomial automorphisms*, ETDS 9 (1989), 67–99，[原文](https://www.math.stonybrook.edu/~ebedford/PapersForM655/FriedlandMilnor.pdf)，§2。

若 $G=H_1\times H_2$，则逐次有
$$\deg G^n=\max\{\deg H_1^n,\deg H_2^n\},\qquad \lambda_1(G)=\max\{\lambda_1(H_1),\lambda_1(H_2)\}\in\mathbb Z.$$
多项式共轭改变迭代次数至多一个与 $n$ 无关的乘法因子，故保持 $\lambda_1$。非平方 $g$ 的上述无理值给出矛盾。

**贡献扣除：** 这一论证所需篇幅少于一页。将“显示支撑耦合”改成“坐标无关非直积”虽然量词变强，但这里不产生独立长文内容。以下真正新引理与该论证没有依赖关系。

## 3. 有界一手文献：不能越过的定理边界

检索日期 2026-09-06。使用六组以上检索式，覆盖 primitive polynomial automorphisms、rational fibrations、product formula、twisted rational maps、invariant foliations、difference Galois。仅把一手来源作为数学依据；未下载外部 PDF 到工作区，也没有做穷尽性优先权声明。

| 来源 | 与本问题直接相关的内容 | 本次不能据此声称的内容 |
| --- | --- | --- |
| Friedland–Milnor (1989), ETDS，[原文](https://www.math.stonybrook.edu/~ebedford/PapersForM655/FriedlandMilnor.pdf) | 平面自同构约化字与次数乘积，消除上节短推论的新颖性 | 四维任意纤维化或分布刚性 |
| Dinh–Nguyên (2011), CMH 86, 817–840，[出版原文](https://ems.press/content/serial-article-files/43270) | 保持纤维化时绝对与相对动态次数的乘积公式 | 已知 $\lambda_1$ 自动等于底曲面的 $\lambda_1$ |
| Dinh–Nguyên–Truong, *On the dynamical degrees of meromorphic maps preserving a fibration*，[一手预印本](https://arxiv.org/abs/1108.4792) | 紧 Kähler 设置中的相对动态次数框架 | 将三维中特定 primitive 推论不加验证搬到四维 |
| Blanc–Cantat (2016), JAMS 29, 415–471，[作者原文](https://algebra.dmi.unibas.ch/blanc/articles/dynamdegree.pdf) | 普通曲面双有理变换 $\lambda_1>1$ 的 Pisot/Salem 限制 | 对被底动力学扭转的泛纤维直接套用普通自映射结论 |
| Abboud–Xie (2026-08), *Dynamical degrees of twisted rational maps*, arXiv:2608.09275v1，[原文](https://arxiv.org/html/2608.09275v1) | Theorem B 识别泛纤维 twisted 动态次数；Theorem C 的仿射曲面结论只给代数次数至多二 | 把 P20 的二次无理数从该上界排除；或声称原文已给所需 twisted Pisot/Salem 定理 |
| Casale–Roques, *Dynamics of rational symplectic mappings and difference Galois theory*, [原文](https://arxiv.org/pdf/0803.3951) | 沿实际适应曲线的差分变分方程与辛映射非可积性障碍；本文是既有方法框架 | 把本报告的法向不可约性直接说成全 Galois 群 $\mathrm{SL}_2$，或直接说成无全部有理第一积分 |

### 3.1 泛曲面纤维化的真实缺口

设 $\pi:X\dashrightarrow Y$ 为四维双有理动力系统到曲面的保持纤维化，且 $\pi F=h\pi$。乘积公式在相应光滑射影模型上只给
$$\lambda_1(F)=\max\{\lambda_1(h),\lambda_1(F\mid\pi)\}.$$
即使已知 $h$ 为双有理、并能利用普通曲面的 Pisot/Salem 约束排除 $\lambda_1(h)=g+1+2\sqrt g$，仍可能是相对项实现最大值。

对非平方 $g\ge5$，其另一个代数共轭
$$g+1-2\sqrt g=(\sqrt g-1)^2>1,$$
所以它不是 Pisot 或 Salem 数。问题在于泛纤维的映射是基域自同构扭转的，而不是普通 $\mathbb C(Y)$-自映射。Abboud–Xie 的 Theorem C 只给仿射曲面代数次数至多二，与本例恰好兼容。此处是经过文献核对的逻辑缺口，不是已经证明存在纤维化。

此外，P20 已有坐标次数矩阵不能取外幂后充当 $\lambda_2(F_g)$。没有在本次计算高阶动态次数，也不授予 cohomological hyperbolicity 或 primitive 标签。

## 4. 新引理 A：所有步长下的多项式 companion 不可约性

### Claim

令 $P\in\mathbb C[z]$ 为非恒定多项式，
$$B(z)=\begin{pmatrix}P(z)&-1\\1&0\end{pmatrix},\qquad \sigma(z)=z+1.$$
对于每个 $m\ge1$，系统
$$v(z+1)=B(z)v(z)$$
的 $m$ 步半线性作用没有 $\mathbb C(z)$-有理不变直线。

状态：`PROVABLE AS STATED / PROVED`。这里没有声称 companion 系统或差分不可约判据本身是普遍新方法；新增应用对象在§5–6。

### Assumptions and notation

定义
$$B_m(z)=B(z+m-1)\cdots B(z).$$
不变直线是一个秩一 $\mathbb C(z)$ 子空间，存在非零有理生成向量 $v$ 与 $r\in\mathbb C(z)^*$ 使
$$B_m(z)v(z)=r(z)v(z+m).$$
令 $d=\deg P>0$；零多项式次数约定为 $-\infty$。

### Proof strategy and dependency map

依赖链：多项式 unimodularity 保持 primitive 向量 → 周期线的比例因子为常数 → 所有正负一步轨道次数有界 → 两种次数排序至少一向严格增长，矛盾。

### Proof

**Step 1. Primitive normalization.** 清去生成向量的分母，再除去两分量的最大公因子，得到互素多项式向量 $v=(u,w)^{\mathsf T}$。每个 $B_m$ 都在 $\mathrm{SL}_2(\mathbb C[z])$ 中，且逆矩阵也有多项式系数。因此 $B_mv$ 仍 primitive：若不可约多项式同时整除其两分量，乘 $B_m^{-1}$ 后也会同时整除 $u,w$。

向量 $v(z+m)$ 也 primitive。若 $r(z)=A(z)/D(z)$ 且 $A,D$ 互素，则 $r(z)v(z+m)$ 两分量均为多项式迫使 $D$ 为常数；其两分量仍互素又迫使 $A$ 为常数。故 $r=c\in\mathbb C^*$。

**Step 2. A two-sided bounded degree orbit would follow.** 在多项式向量上定义可逆半线性作用
$$\mathcal T v(z)=B(z-1)v(z-1).$$
上式 $B_mv=c\,v(z+m)$ 等价于 $\mathcal T^m v=cv$。由于 $\mathcal T$ 固定复常数，所有 $\mathcal T^n v$ 的两个分量次数，当 $n$ 在全部整数中变化时，都被有限组 $n=0,\ldots,m-1$ 的次数统一控制。

**Step 3. The bounded orbit is impossible.** 若 $\deg u\ge\deg w$，则
$$\mathcal T(u,w)^{\mathsf T}
=\big(P(z-1)u(z-1)-w(z-1),\ u(z-1)\big)^{\mathsf T}.$$
第一分量次数恰为 $d+\deg u$，严格大于第二分量次数；不存在相同次数项可取消。重复后正向每一步最大次数增加 $d$。

若 $\deg u<\deg w$，则
$$\mathcal T^{-1}(u,w)^{\mathsf T}
=\big(w(z+1),\ -u(z+1)+P(z)w(z+1)\big)^{\mathsf T}.$$
第二分量次数恰为 $d+\deg w$，严格大于第一分量次数；重复后反向每一步最大次数增加 $d$。

非零向量必落入这两种情形之一，均与 Step 2 矛盾。于是任意 $m$ 步作用无有理不变直线。$\square$

### Boundary check

$P$ 非恒定是必要假设；常数矩阵在 $\mathbb C$ 上有特征直线。$m$ 无上界，且证明没有把“一步不可约”未经证明地提升为“所有步长不可约”。

## 5. 新引理 B：实际不变曲线的切向—法向刚性

### Claim

固定 $g\ge5$ 和 $a\in\mathbb C^*$，令
$$c=g a^{g-1},\qquad \gamma_a(t)=(q_1,q_2,p_1,p_2)=(a,0,t,0).$$
则 $F_g\gamma_a(t)=\gamma_a(t+c)$。沿这条曲线，$DF_g^m$ 的有理差分模中，任意秩二不变子模恰为切向平面 $TM$ 或其辛正交法向平面 $TM^{\perp_\omega}$，其中 $M=\{q_2=p_2=0\}$。这两个平面都不是拉格朗日的。

状态：`PROVABLE AS STATED / PROVED`。

### Assumptions and notation

切向坐标为 $(\delta q_1,\delta p_1)$，法向坐标为 $(\delta q_2,\delta p_2)$。两块上的辛形式分别为 $d(\delta q_i)\wedge d(\delta p_i)$。虽然 $\gamma_a$ 是一维曲线，所谓“切向模”指 $TM|_{\gamma_a}$，不是秩一的 $T\gamma_a$。

### Dependency map

实际梯度与 Hessian → 沿 $\gamma_a$ 的块对角导数 → 切向模为有理平凡模、法向模经多项式 gauge 成引理 A → 简单模的投影与图像论证。

### Proof

**Step 1. Actual invariant curve and derivative.** 在 $M$ 上，映射严格为
$$F_g(q_1,0,p_1,0)=(q_1,0,p_1+gq_1^{g-1},0).$$
沿 $\gamma_a$ 的导数是切向块与法向块的直和：
$$U=\begin{pmatrix}1&0\\k&1\end{pmatrix},\qquad k=g(g-1)a^{g-2},$$
$$A(t)=\begin{pmatrix}
1+4a^2(t+c)^2&2(t+c)^2\\
2a^2&1
\end{pmatrix}.$$
这是 $DS$ 与在中间动量 $(t+c,0)$ 处的 $DT$ 相乘所得；纯 $p_2^g$ 项的二阶导数沿该曲线为零。这里没有把 Hessian 当成次数转移矩阵。

**Step 2. Tangent block.** 设 $z=t/c$。令
$$G(z)=\begin{pmatrix}1&0\\kz&1\end{pmatrix}.$$
则 $UG(z)=G(z+1)$，所以在基 $G(z)$ 下切向差分模为平凡秩二模。此结论也适用于每个 $m$ 步作用。

**Step 3. Normal block.** 写 $b=2a^2\ne0$，法向状态为 $(x,y)=(\delta q_2,\delta p_2)$。方程为
$$y(t+c)=y(t)+b x(t),\qquad
x(t+c)=x(t)+2(t+c)^2y(t+c).$$
消去 $x$ 得到
$$y(t+c)+y(t-c)=(2+4a^2t^2)y(t).$$
取
$$P(t)=2+4a^2t^2,\qquad
H(t)\binom{x}{y}
=\binom{y}{(P(t)-1)y-bx}.$$
$H(t)$ 是多项式矩阵且 $\det H=b\ne0$；其第二分量正是 $y(t-c)$。因此它把法向系统 gauge 成
$$\binom{y(t+c)}{y(t)}
=\begin{pmatrix}P(t)&-1\\1&0\end{pmatrix}
\binom{y(t)}{y(t-c)}.$$
归一 $z=t/c$ 后的多项式为
$$P_a(z)=2+\alpha z^2,\qquad \alpha=4a^2c^2=4g^2a^{2g}\ne0.$$
引理 A 证明法向秩二模对每个 $m$ 步作用均简单，即无秩一不变子模。

**Step 4. Rank-two submodules.** 记切向模为 $E_T$，法向简单模为 $E_N$，并固定 $m$。若 $E\subset E_T\oplus E_N$ 是秩二不变子模，其投影到 $E_N$ 的像只能是零或整个 $E_N$。

若像为零，则 $E=E_T$。若像为整个 $E_N$，秩数迫使投影为同构，故 $E$ 是某个模同态 $\varphi:E_N\to E_T$ 的图。非零 $\varphi$ 的核因 $E_N$ 简单而为零，进而它在秩二情况下是同构；但 $E_T$ 为平凡模，含不变直线，与 $E_N$ 简单矛盾。因此 $\varphi=0$，且 $E=E_N$。

两种平面上 $\omega$ 的限制均非退化，所以没有拉格朗日秩二不变子模。$\square$

### The second plane, without an omitted symmetry argument

对 $b_0\ne0$，另取
$$\eta_{b_0}(t)=(0,t,0,b_0),\qquad c_0=gb_0^{g-1}.$$
严格有 $F_g\eta_{b_0}(t)=\eta_{b_0}(t+c_0)$。切向 $(\delta q_2,\delta p_2)$ 是常数幺幂块，可按上式的转置形式平凡化。

法向 $(x,y)=(\delta q_1,\delta p_1)$ 满足
$$y(t+c_0)=y(t)+2t^2x(t),\qquad
x(t+c_0)=x(t)+2b_0^2y(t+c_0).$$
令 $d_0=2b_0^2\ne0$，则 $x(t-c_0)=x(t)-d_0y(t)$。因此
$$x(t+c_0)+x(t-c_0)=(2+4b_0^2t^2)x(t).$$
多项式 gauge $(x,y)\mapsto(x,x-d_0y)$ 的行列式是 $-d_0\ne0$。归一后仍是引理 A 的非恒定 companion。故整个引理 B 也适用于 $N=\{q_1=p_1=0\}$。

## 6. 主结构结论：不变拉格朗日分布的强制不定平面

### Exact claim

设 $g\ge5$、$m\ge1$。令
$$\mathcal D:\mathbb A^4_{\mathbb C}\dashrightarrow \mathrm{Gr}(2,4)$$
是有理映射，表示有理秩二分布。假设在一个稠密开集上
$$DF_g^m(x)\mathcal D_x=\mathcal D_{F_g^m(x)},\qquad \omega|_{\mathcal D_x}=0.$$
令 $U_{\mathcal D}$ 为该 Grassmann 有理映射的最大定义开集。则
$$U_{\mathcal D}\cap(M\cup N)=\varnothing.$$
换言之，完整的 $M\cup N$ 都包含在其不定集中。不要求分布 involutive；结论因而也适用于有理拉格朗日叶状结构。

状态：`PROVABLE AS STATED / PROVED`。

### Proof

若 $U_{\mathcal D}\cap M$ 非空，它是不可约平面 $M$ 中的非空开集，故与 $q_1\ne0$ 的开集相交。选取一个 $a\ne0$，使 $\gamma_a$ 与 $U_{\mathcal D}$ 相交。则 $\mathcal D$ 限制到 $\gamma_a$ 给出一个有理秩二子模。

$F_g^m$ 在 $\gamma_a$ 上是无限阶平移 $t\mapsto t+mc$。定义域与其平移逆像在该曲线上都是稠密开集。全空间中的有理不变等式在两侧均定义的地方成立，因此在该曲线的共同稠密定义域上也成立。拉格朗日性是 Grassmann 簇中的闭条件，故限制仍为拉格朗日。

这与引理 B 矛盾。所以 $U_{\mathcal D}\cap M$ 为空。使用 $\eta_{b_0}$ 及上节对第二平面的显式计算，得到 $U_{\mathcal D}\cap N$ 也为空。$\square$

### Immediate geometric consequence, with its exact qualifier

若 $Y$ 为光滑曲面，$\pi:\mathbb A^4\dashrightarrow Y$ 为 dominant 有理映射，泛纤维是拉格朗日的，且
$$\pi F_g^m=h\pi$$
对某个 dominant 有理 $h$ 成立，则 $\ker d\pi$ 在函数域上构成上述不变分布。

于是任何 $\pi$ 已定义且 $d\pi$ 满秩二的点都不能属于 $M\cup N$。即
$$M\cup N\subset \operatorname{Indet}(\pi)\cup\operatorname{Crit}(\pi).$$
特别地，不存在处处光滑、处处满秩的保持拉格朗日纤维化。但这里**没有**排除所有 dominant rational surface semiconjugacies：未假设纤维拉格朗日时不能使用此结论；即使是拉格朗日泛纤维，也仍允许这两张平面整体落入坏集。

## 7. 真实失败证据：余维二奇点并不自动可去

考虑与动力学无关的具体多项式映射
$$\pi_0(q_1,q_2,p_1,p_2)=(q_1p_1,q_2p_2).$$
两个分量 Poisson 对易，且在稠密开集上 $d\pi_0$ 秩为二；非零一般值的纤维为 $(\mathbb C^*)^2$，是连通有理拉格朗日曲面。

其核分布由两个向量张成：
$$X_1=q_1\partial_{q_1}-p_1\partial_{p_1},\qquad
X_2=q_2\partial_{q_2}-p_2\partial_{p_2}.$$
分布的 Grassmann 映射在 $M\cup N$ 上不定。在 $M$ 的一般点，分别沿 $q_2\ne0,p_2=0$ 与 $q_2=0,p_2\ne0$ 趋近时，第二条线趋于 $\partial_{q_2}$ 与 $\partial_{p_2}$，给出不同二维极限平面；$N$ 上同理。原点处也可选择不同方向得到不同极限。因此该不定现象不是仅由一个不良生成组引起的可去零点。

这个例子**不是** $F_g$ 保持纤维化的候选证明，也不调用旧共射线固定场结论。它只反驳如下错误推理：“一张有理拉格朗日分布不可能在这两张平面上同时不定，因此§6 已经是全局 no-fibration。”

真正还缺的内容，是利用 $F_g$ 在 $M,N$ 邻域的非线性项，排除这种允许的奇异情形，或找到别的全局机制。对这些余维二平面 blow up 后，叶状结构、例外除子及其引出的变分作用都需要新的证明；本次没有把“做 blow-up”当作已解决步骤。

## 8. 独立检查与自然篇幅判断

同团队另一独立子任务作了只读快查，确认：

- 引理 A 中 primitive 向量经 $B_m$ 仍 primitive，比例因子确为非零常数；所有正负一步作用的次数有界与 forward/backward 严格增度矛盾。
- $E_T\oplus E_N$ 的秩二不变子模投影论证没有漏掉非平凡图像：$\operatorname{Hom}(E_N,E_T)=0$。
- 从 Grassmann 最大定义域限制到一般 $\gamma_a$ 合法；必须保留“全部 $M\cup N$ 可为余维二不定集”这一限定。

该快查不是新颖性评分、论文候选双盲评审或最终证明/PDF 验收。

**独立于主控意愿的自然篇幅预判：** 值得保留的新增核为“全部步长 companion 不可约 + 两类真实变分方程 + 强制奇异平面”，合理证明展开约 4–6 页；对象、文献边界、纤维化推论与反例约 3–5 页，总计约 7–11 页正文。把平面分类、一般差分 Galois 理论或 P20 次数证明重写进来，不能计作新增实质内容。即使§6完全通过数学检查，它仍不满足当前 22–30 页独立论文门。

因此当前结论为 **保留新证明，但 STOP 作为 Paper29 候选**。不因该小结果重开已停的 trace-charts 包，也不追加其短推论。

## 9. 最多两条未解决精确问题

1. **全局拉格朗日刚性。** 对 $F_6$，是否不存在任何 $m\ge1$ 和 $F_6^m$ 不变的有理秩二拉格朗日分布，即能否排除其 Grassmann 不定集包含 $M\cup N$ 的剩余情形？本报告只证明若存在就必须在这两张平面上全部不定。
2. **无拉格朗日假设的曲面半共轭。** 是否存在光滑射影曲面 $Y$、dominant rational $\pi:\mathbb A^4\dashrightarrow Y$（几何一般纤维不可约）及 $m\ge1$、双有理 $h:Y\dashrightarrow Y$，满足 $\pi F_6^m=h\pi$？本报告没有排除；$\lambda_1$ 的非 Pisot/Salem 性只控制 ordinary base，不自动控制 twisted generic fiber。

这两条是精确缺口，不是获准启动的新项目或完成篇数。没有其它被名字掩盖的开放主张。

## 10. 输入身份与报告哈希

工作区无 Git 元数据；不初始化仓库。针对实际读取的近邻源绑定如下 SHA256：

| 输入 | SHA256 |
| --- | --- |
| `AGENTS.md` | `73ff82bcf298285ef8c3b6a4d3e1dff80eedb7eeda93ea47a55334c862c43412` |
| `docs/WORKFLOW.md` | `b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2` |
| `PAPER29_PORTFOLIO_AUDIT_20260905.md` | `e6699e6d8ce81952ee906a8cabb925373b9a5a9d8d97f7115b95980e07aac9f3` |
| P20 `notes/RESEARCH_QUESTION.md` | `eee1350eeefb818f240328493a16d3036df7bdb028a86016594bb8e26d956b86` |
| P20 `paper/main.tex` | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| P21 `paper/main.tex` | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| P25 `paper/main.tex` | `4d8ac64803ecae76809461e183c72349e7bcab1ad1fac3e4167fe9735860eea2` |

本报告自身 SHA256 在保存完毕后的交付消息中给出，避免自引用哈希。没有扫描旧构建树。

## 11. 后续有界推导：完整第一积分组的障碍与一个精确 iff

本节在初始 STOP 结论之后，按主控提出的 Casale–Roques 桥与具体扰动族继续检查。它增加一个完整证明，不追溯改变§7的全局 fibration 缺口，也不自动把整个包变成通过原页数门的候选。这里的 Hamiltonian 横向二阶信息，与已停止的周期迹微分/jet 包不是同一数学对象。

### 11.1 精确的一手 Galois 桥，不省略非连通问题

新增一手来源：Hendriks–Singer, *Solving Difference Equations in Finite Terms*, J. Symbolic Computation 27 (1999), 239–259，[作者原文](https://singer.math.ncsu.edu/papers/finite.pdf)。Theorem 2.1（原文第241页）针对 $K=\mathbb C(z)$、$\sigma(z)=z+1$ 给出两点：差分 Galois 群 $G$ 的分量群 $G/G^0$ 有限循环；系统存在 $K$-有理 gauge，使其系数矩阵取值于 $G(K)$。第244页明确使用有限步产品落入 $G^0(K)$ 的论证。

**Lemma C.** 若一个秩二差分模在 $K$ 上的每个正步长作用都没有有理不变直线，则其差分 Galois 群 $G$ 的单位分支 $G^0$ 不是可解群，因而不是交换群。

**Proof.** 假设 $G^0$ 可解。用上述定理作有理 gauge，把系数矩阵写成 $\widetilde B(z)\in G(K)$。令 $r=|G/G^0|$。因为 $G/G^0$ 是定义在代数闭常数域上的有限常数群，$\widetilde B$ 的分量类为一个常数类，所有 $\sigma^j(\widetilde B)$ 的分量类相同。因此
$$\widetilde B_r(z)=\widetilde B(z+r-1)\cdots\widetilde B(z)\in G^0(K).$$
连通可解线性代数群的 Lie–Kolchin 定理给出一个常数基，使 $G^0$ 保持一条常数直线。这条线于是被 $r$ 步系统保持；将它经原有理 gauge 拉回，得到原模的 $r$ 步有理不变直线，矛盾。$\square$

此处显式消除了非连通群通过交换两条线逃避“一步不可约”的可能。没有只依据一步 Riccati 无解就声称 $G^0$ 非交换。

引理 A 的假设因而足够推出其 Galois 单位分支非交换。若需要还可由 $\mathrm{SL}_2$ 的代数子群分类加强成全群 $\mathrm{SL}_2$，但本节没有使用也不需要这个加强。

### 11.2 扰动稳定非可积性准则

**Exact claim.** 在坐标 $(x,y,u,v)$、辛形式 $dx\wedge du+dy\wedge dv$ 下，取
$$V(x,y)=P(x)+\frac12 A(x)y^2+y^3R(x,y),$$
$$W(u,v)=\frac12 B(u)v^2+v^3S(u,v),$$
其中 $P,A,B$ 为复系数多项式，$R,S$ 为任意二元复多项式。假设
$$P'\not\equiv0,\qquad A\not\equiv0,\qquad \deg B\ge1.$$
令 $F=T_WS_V$ 为相应的两个 Hamiltonian 梯度剪切之积。则对每个 $m\ge1$，不存在两个有理函数 $H_1,H_2$ 同时满足
$$H_i\circ F^m=H_i,\quad dH_1\wedge dH_2\not\equiv0,\quad\{H_1,H_2\}=0.$$
也不存在 Casale–Roques 所定义的有理非交换完全可积结构。后一结论仅使用该文精确的完整积分与辛梯度生成条件，不泛称一切“非交换可积性”。

状态：`PROVABLE AS STATED / PROVED`。

**Assumptions and proof dependency.** 只需任选一个 $a\in\mathbb C$ 使 $c=P'(a)\ne0$ 且 $\alpha=A(a)\ne0$。这样的 $a$ 存在，因为两者都是非零多项式。依赖为：梯度剪切辛性 → 实际平移曲线 → 法向 companion → 引理 A、C → Casale–Roques 的适应曲线必要条件。

**Step 1. Exact curve and jets.** 平面 $M=\{y=v=0\}$ 不变，且
$$F(x,0,u,0)=(x,0,u+P'(x),0).$$
故 $\gamma_a(t)=(a,0,t,0)$ 满足 $F\gamma_a(t)=\gamma_a(t+c)$。由于 $y^3R$ 与 $v^3S$ 在相应平面上的全部二阶偏导均为零，沿该曲线的变分方程完全不受任意 $R,S$ 影响。

**Step 2. Tangent and normal blocks.** 切向 $(\delta x,\delta u)$ 的矩阵为
$$U_a=\begin{pmatrix}1&0\\P''(a)&1\end{pmatrix},$$
它通过§5同样的平移 gauge 在 $\mathbb C(t)$ 上平凡化。法向 $(\xi,\eta)=(\delta y,\delta v)$ 满足
$$\eta(t+c)=\eta(t)+\alpha\xi(t),\qquad
\xi(t+c)=\xi(t)+B(t+c)\eta(t+c).$$
于是
$$\eta(t+c)+\eta(t-c)=(2+\alpha B(t))\eta(t).$$
这里 companion 的系数是当前时刻的 $B(t)$，不是把正向法向矩阵中的 $B(t+c)$ 原样放入二阶标量方程。多项式 gauge 为
$$\binom{\xi}{\eta}\longmapsto
\binom{\eta}{(1+\alpha B(t))\eta-\alpha\xi},$$
其行列式为 $\alpha\ne0$。将 $z=t/c$ 后，companion 多项式为
$$Q(z)=2+\alpha B(cz),$$
由 $c\alpha\ne0$ 与 $\deg B\ge1$ 可知 $Q$ 非恒定。

**Step 3. Every iterate retains the Galois obstruction.** 引理 A 排除法向模的所有正步长有理不变直线。固定任意 $m$ 后，$m$ 步法向模的所有正步长也具有此性质，因为它们就是原模的 $mr$ 步作用；将底平移 $z\mapsto z+m$ 再归一后，引理 C 适用。因此每个 $m$ 步法向差分 Galois 单位分支非交换。

完整秩四变分模为这个法向模与一个有理平凡秩二模的直和。一个完整基本解矩阵可取为有理切向 gauge 与法向基本解矩阵的块直和；切向块不产生新的 Picard–Vessiot 元素。因此完整变分模的 Galois 群与法向群同构，单位分支也非交换。

**Step 4. Apply the correct existing integrability theorem.** Casale–Roques 的 [一手原文](https://arxiv.org/pdf/0803.3951) §6.1 Definition 14 允许有理嵌入 $\mathbb P^1\dashrightarrow V$，并不要求存在从完备 $\mathbb P^1$ 到仿射空间的非恒定全局态射。当前 $\gamma_a$ 正是这样的嵌入；对 $F^m$ 的底作用是非周期 Möbius 平移 $t\mapsto t+mc$。

该文 §7.1 Theorem 4 规定：若辛映射具有其所定义的完整可积结构，则沿适应曲线的变分差分 Galois 单位分支必须交换。§6.2 的 generic junior parts 和 Ziglin 引理处理原积分沿曲线退化或有极点的情形，因此这里不额外假设 $dH_1,dH_2$ 在 $M$ 上独立或正则。与 Step 3 矛盾，所断言的完整积分组不存在。$\square$

**P20 instance.** 取
$$P(x)=x^g,\quad A(x)=2x^2,\quad B(u)=2u^2,\quad R=0,\quad S(u,v)=v^{g-3}.$$
即恢复 P20 的 $V_g,W_g$。所以全部 $F_g^m$ 都没有两个独立、Poisson 对易的有理第一积分。这不声称每个单独有理第一积分都为常数，也不排除底动力学非恒等的保持纤维化。

### 11.3 无三阶扰动子族的精确可积性分类

现在另外固定 $R=S=0$，保留 $P'\not\equiv0$、$A\not\equiv0$，但允许 $B$ 为任意多项式。对每个 $m\ge1$，有
$$F^m\text{ 在有理 Liouville 意义下可积}\quad\Longleftrightarrow\quad B\text{ 为常数}.$$

**Nonconstant direction.** 当 $\deg B\ge1$ 时，§11.2 已经给出每个正迭代的否定结论。

**Constant direction.** 设 $B=b\in\mathbb C$。映射严格满足
$$x'=x,\quad u'=u+P'(x)+\tfrac12 A'(x)y^2,$$
$$v'=v+A(x)y,\qquad y'=y+bv'.$$
定义
$$I(x,y,v)=A(x)y^2-bv^2-bA(x)yv.$$
因为 $x'=x$，验证 $I$ 的不变性时可固定 $a=A(x)$。此时 $y'=(1+ab)y+bv$、$v'=ay+v$，三个系数分别为
$$[y^2]I'=a(1+ab)^2-ba^2-aba(1+ab)=a,$$
$$[v^2]I'=ab^2-b-ab^2=-b,$$
$$[yv]I'=2ab(1+ab)-2ab-ab(1+2ab)=-ab.$$
故 $I'=I$。函数 $x$ 与 $I$ 都不依赖 $u$，所以 $\{x,I\}=0$。并且
$$dI\equiv (2A(x)y-bA(x)v)\,dy+(-2bv-bA(x)y)\,dv\pmod{dx}.$$
由于 $A$ 非零，$dx\wedge dI\not\equiv0$；这也包含 $b=0$。因此 $(x,I)$ 是两个独立对易有理第一积分，并被每个 $F^m$ 保持。$\square$

**Quantifier boundary.** 此 iff 仅针对 $R=S=0$ 子族。任意 $R,S$ 的版本在 $B$ 非恒定时给出统一非可积性充分条件，不宣称 $B$ 恒定时任意高阶扰动都可积；$P'=0$、$A=0$ 也不在分类内。

### 11.4 价值与篇幅重新判断

本节使研究内容从“有强制奇异集的分布引理”增加为“二阶法向信息控制、对三阶理想扰动稳定的非可积性准则，以及精确无扰动可积性边界”。它比单个 P20 非积分推论实质更强，但其核心证明仍依赖一个很短的 companion 次数引理与两条既有 Galois 定理。

本代理独立估计，整个§4–7与§11包的自然论文正文约 10–15 页；这不是固定排版后的验收测量，但目前没有独立支持 22 页的实质内容。本节不制造额外未解决问题，仍只保留§9的两条精确全局问题。暂不探索或宣称恒定 $B$ 边界上的完整有理固定场分类。

**更新后处置仍为 STOP 作为 Paper29 候选，保留可检验的新证明。** 若主控后来获得真正新增的分类机制，应单独建立新证据和重新预筛，不把本报告的证明闭合作为已通过价值或页数门的替代。
