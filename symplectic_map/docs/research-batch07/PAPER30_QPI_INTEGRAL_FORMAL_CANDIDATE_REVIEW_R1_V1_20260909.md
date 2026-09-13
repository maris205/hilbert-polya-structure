# Paper30 qPI Integral V1：首次完整正式候选评审 R1

日期：2026-09-09。评审对象为冻结的 Integral V1 完整 C1–C3，不是旧 T1–T7 的重投，也不是仅审 U、S 或整数增量。

## 1. 本席结论与执行身份

| 门 | 本席结果 | 固定阈值 | 判定 |
|---|---:|---:|---|
| 新意 | 7.3 / 10 | 至少 7.5 | FAIL |
| 独立科学价值 | 8.1 / 10 | 至少 7.5 | PASS |
| 完整证明信心 | 9.1 / 10 | 至少 9 | PASS |
| 自然完整实质正文 22–30 页 | 可信；低／中／高预测 24.25／29.75／36.00 页 | 指定版式、全部必要证明在正文 | PASS |
| 本席四门合取 | — | 四项同时通过 | **FAIL** |

失败原因是实质扣除后新意未达 7.5；不是发现 C1–C3 错误，不是以来源检索缺口代替反例，也不是以新意失败省略其它三门。
容量 PASS 是存在可信自然写法的判断，不是已测页数、严格上界或完成论文验收；超过 30 页的风险实质存在。

执行者为新派发的非作者 Codex R1 独立上下文，采用继承的可用模型家族与 xhigh 证据审查要求。
没有调用未配置的 GPT-5.4 MCP，没有调用外部评审 API，没有上传候选内容。
本人先全文读三个入口，再全文读 MANIFEST §§2–6 的全部 52 件；共 55 件。
逐件实际核对行数和 SHA-256，末次有界复核仍为 55/55 MATCH，完整记录见 §9。
分批读取中出现的输出截断均另行补读；FULL 表示本人读取 1 至末行，不是继承组织者的 RANGE/FULL 标签。
全部十二件作者证明、十二件对应非作者报告、六件纠错／处置、九件整数来源及意见、十三件旧来源／负面意见都包括在内。

未读本轮另一席报告、对话或内部记录，未向另一席通信，未再次委派。
未读 README、BATCH 或旧正式评分报告；旧评分与失败原因只通过共同输入的冻结处置披露。
没有修改共同输入、旧票、作者证明或工作区索引，没有建项目、锁、英文稿、试排、PDF 或实验。
本次唯一新增工作区文件就是本报告；提交后停止修改。

采用 research-review 的证据链和高强度反驳要求；ARS 的研究评审材料只用于来源分层、最强反对意见及局限披露。
用户固定的双份四门合同优先于默认五席、期刊等级或 ML 评审流程。本报告不是 Route A/B 评价。
状态为 NOT_CALIBRATED、criteria_binding_unavailable；未做人类或跨模型认证。
“独立”仅指本席任务上下文、读证和判断独立，不声称两席错误统计独立，不估计期刊接受概率。
共同包公开了历史失败与查新分数，因此不声称对这些先验盲审。

## 2. 评审的完整科学对象

工作基为无根单位关系的 \(R=\mathbb Z[q^{\pm1},\tau^{\pm1}]\)。
在同一个八截面吹起模型 \(S/R\) 上，\(D=-K_{S/R}\) 为八个 \((-2)\) 分量的相对 SNC 环，\(L_n=\mathcal O(nD)\)。
原环面补集 \(E\) 与反典范边界 \(D\) 不同；\(\mathcal V=S\setminus D\) 保留四条完整末端仿射线。
四簇吹起次数为 \(1+2+3+2\)，最后四中心位于不同分量，其单位坐标为 \(1,\tau,\tau,q\)；坐标相等不合并中心。
原矩阵次序、原迹积分及全共振系数 \(C_j=[z^j]\operatorname{tr}M_j(z)\) 全部固定。

C1 是对所有 \(n\ge0\) 的实际整数上同调与全共振扩张消失：
\[
H^0(S,L_n)=R\langle1\rangle,\quad
H^1(S,L_n)\simeq\bigoplus_{j=1}^nR/(1-q^j),\quad H^{\ge2}=0,
\]
并有保留真实常数项的非典范派生分裂
\[
R\Gamma(S,L_n)\simeq R[0]\oplus\bigoplus_{j=1}^n[R\xrightarrow{1-q^j}R].
\]
固定 \(n\) 后选取一次分裂，对每个交换 \(R\)-代数的派生基变换都有效，含非平坦、非约化和非 Noetherian 基。
这不是普通 \(H^0\) 任意基变换定理，也未要求跨 \(n\) 的过滤、乘法或动力相容。
两项复形位于次数 \(0,1\)，从而对任意这样的 \(A\)，
\[
H^0(S_A,L_{n,A})\simeq A\oplus\bigoplus_{j=1}^n\operatorname{Ann}_A(1-q_A^j),\quad
H^1(S_A,L_{n,A})\simeq\bigoplus_{j=1}^nA/(1-q_A^j),\quad H^{\ge2}=0.
\]
第一个 \(A\) 是真实常数子模；原 \(R\) 上的 \(\operatorname{Fitt}_0H^1=(\prod_{j=1}^n(1-q^j))\)。

C2 固定任意 \(p,a,m\)，其中 \(a,m\ge1,\ p\nmid m\)，令 \(N=p^a,r=mN\)，在原圆分 DVR 与任意时间单位 \(t\) 上研究同一完整模型。
这里 \(p\) 为任意素数，\(s=\zeta_r\)，\(\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}\)、\(\mathfrak p\mid p\)，
\(\pi\) 为 DVR 参数，\(\kappa=\mathcal O/(\pi)\)，\(e=v_\pi(p)\)，且 \(t\in\mathcal O^\times\)。
保留原 \(1,I_r\) 完整最小 pencil、射影平坦态射、\(\bar I_r=J^N\)、概形重数、原截面基和实际特化像。
其中剩余参数的精确阶是 \(m\)，\(J=I_{m,\bar s}\)，不是继续用 \(r\) 当剩余阶。
完整扭子模的全部初等因子、长度 \(ae\)、生成元数 \(N-1\) 及 Fitting 理想均为合同内容。
具体为
\[
H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus\mathcal T,\qquad
\mathcal T\simeq\bigoplus_{b=0}^{a-1}
\left(\mathcal O/(\pi^{e/\varphi(p^{a-b})})\right)^{\oplus\varphi(p^{a-b})}.
\]

C3 固定状态微分，先在特征零除 \(p^a\)，再约化原 \(\alpha=p^{-a}dI_r\)。
记 \(T=\bar t^m\)、\(\varepsilon=(-1)^{m+1}\)；指定的多项式是
\[
H_p(T,h;\varepsilon)=
\begin{cases}
[Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
h,&p=2.
\end{cases}
\]
在整个 \(\mathcal U=\mathcal S\setminus\mathcal D\) 上保留
\[
\bar\alpha=H_p(T,J;\varepsilon)^{(N-1)/(p-1)}dJ,
\]
全局局部自由系数理想等式、准确公共 \(\pi\)-阶 \(ae\)，以及实际泛 Jacobian 和原光滑闭能级的 Hasse 解释。
不将同亏格、同谱方程、同判别式或同根集替代所需同构。
不将公共阶解释为每个闭点提升的赋值，不把除公共因子叫作 \(\pi\)-饱和，也不声称已构造典范上同调／微分模同构。

## 3. 全必要证明链审读

下文 ID 对应 §9 的冻结对象；行号只定位证据，不表示本人仅做 RANGE 审读。

### 3.1 原几何与域上接口

P 94–257、Nbd 68–269 给出真实八中心、四末端图、八边界极阶传播和正规丛粘合。
我检查了四个单位中心不碰节点／不因坏素数而碰并这一点；它使同一个整数模型光滑，且 \(E\) 可用于之后的平坦极点商下降。
P 的末端计算不是把环面坐标式在缺失点处作形式代入：各末端附近给出正则映射或实际局部式，从而原积分在四条线无额外极点。
八边界赋值与原非零首项一起固定极除子为精确阶乘 \(D\)，不能仅从 bidegree 推出。

Nbd 的节点乘子是定向后的 \(q^{-1}\)；四局部比值为 \(-1/\tau,-1,-1/q,-\tau\)，总乘积为 \(q^{-1}\)。
这些是单位，故边界消元适用于整数基；把正反方向交换只将非零因子乘以单位，不改变商模，但原标架规范必须一致。
P-R、N-R 的接受与我对上述局部环／节点计算的检查相符，并未用标签替代计算。

Gfield 95–253 从边界精确阶与实际极除子得到完整最小 pencil，再处理 Stein 分解的总次数。
该次数包括纯不可分部分；只说一般点一一对应不足以得到这里的完整结论。
泛光滑论证用无穷纤维的 tame 重数与 SNC 局部微分，排除水平临界分量；因此没有默认在特征 2、3 排除 quasi-elliptic 情形。
Ffib 128–245 直接算出与八边界正交的格，并用交叉形式和伴随公式限制有限纤维分量。
该秩二格的交矩阵 \(\left(\begin{smallmatrix}-8&8\\8&-8\end{smallmatrix}\right)\) 的退化方向是 \(D\)，分量只能落在相应倍数方向；配合 pencil 最小性和总重数得有限几何纤维整且约化。
这一实际纤维结论是 C2 概形纤维及 H.L(a) 的前提，不由泛亏格一自动推出。
Gf-R、F-R 与 DG、DD 的责任合取未留下本合同所需的未证前提。

### 3.2 C1：全共振截面不是只在本原分支存在

Ssplit Steps 1–5（112–266）是 C1 的实质接口；Ucoh 没有另行绕过它。
对 \(B_j=R/(1-q^j)\)，我检查了其约化、\(\mathbb Z\)-平坦性以及嵌入所有 \(d\mid j\) 的特征零分支的论证。
这些分支在坏素数上相交，故不能把分支上无极点直接当作非正规基上的 Hartogs 延拓。

在精确阶 \(d\) 的分支，原 \(j\) 项矩阵块重复 \(j/d\) 次。
Cayley–Hamilton 给 \(C_j\) 关于原 \(I_d\) 的首一多项式，次数 \(j/d\)；因此从域上 \(dD\) 极除子可得 \(jD\) 的允许极点界。
必须使用所有约数分支，不只是本原 \(j\) 分支；也不能在全 \(B_j\) 上偷换 \(C_j\) 为 \(\operatorname{tr}M_j(1)-(\tau^j+1)\)。

真正的下降步骤是取足够的 \(k\)，把潜在坏项放进 \(L_j(kE)/L_j\)。
该商由支撑在相对 SNC Cartier 边界上的可逆层有限过滤，故对 \(B_j\) 平坦。
张量分支嵌入保持单射，分支上坏项全为零才推出原商中的坏项为零。
这处理了非正规整数共振基的接合，不是“特征零点稠密所以截面存在”的跳步。

原矩阵的负 \(x\) 首项给
\[
[x^{-j}]C_j=(-\tau)^j q^{j(j-1)/2}\in B_j^\times.
\]
我检查了这里需要“单位”而不仅是“非零”；Nbd 的全八环单位标架传播使限制在整个边界上生成 \(\mathscr N^j_{B_j}\)。
它在后续非约化商上仍是单位。Ss-R 的对应检查覆盖了实际最终 418 行版本，DI 已关闭先前所有权措辞条件。

### 3.3 C1：真实扩张、派生分裂与任意基变换

Ucoh 114–148 的常数项从逐次吹起的相对计算出发：例外上的相应 \(\mathcal O(-1)\) 高次上同调消失，配合 Leray／Čech 得 \(R\Gamma(\mathcal O_S)=R[0]\)。
边界正规化的单位节点消元得到 \([R\xrightarrow{1-q^{-j}}R]\)。
由于 \(1-q^j\) 在无关系 \(R\) 中是非零因子，\(H^0(L_n)\) 的唯一常数项和高次消失可逐级得到，剩下的是实际 \(H^1\) 扩张，而不是仅关联分次模。

Ucoh 181–197 使用 \(C_j\) 的 Bockstein 类。
自然性把此类送到 \(B_j\) 商的单位生成元，并且该类本身被 \(1-q^j\) 杀死；这足以构造商模到扩张模的截面。
我特别检查了非局部 \(R\) 的单位问题：只在被 \(1-q^j\) 杀死的子模内用商环单位的逆，不需要它能提升成 \(R\) 中的单位。
因此这一步消去了真实扩张，而不是由长度、Fitting 理想或 Smith 预期倒推分裂。

Ucoh 199–209 再检查派生障碍。
每个 \(R/(1-q^j)\) 有长度一自由分解，故 \(T_n=\bigoplus_jR/(1-q^j)\) 的 \(\operatorname{Ext}^2_R(T_n,R)=0\)。
截断三角因而可分裂且保留真实常数映射；上同调模分裂与派生分裂并非被混作同一结论。
Ucoh 211–236 的任意派生基变换适用，因为原 \(R\) Noetherian、模型 proper、\(L_n\) 对基平坦；目标代数不须 Noetherian。
这与本人亲读的 [Stacks 07VK 的陈述及 Čech 证明](https://stacks.math.columbia.edu/tag/07VK) 条件一致。
核、余核与 Fitting 公式随后是形式推论，\(n=0\) 为空和／空积。
U-R、Ss-R、DI 的最终合取使 S 的截面供给与 U 的扩张供给接上；没有将 S 的另一套 DVR 分裂倒用为 U 的前提。

### 3.4 C2：同模型、原基、实际像与全部初等因子

Gint 113–148 用上述同一八截面族特化到圆分 DVR；不是另选一个在好素数有效的模型。
原 \(I_r\) 的水平无极点性与垂直系数整性在正常模型的余维一处检查，给出完整整截面。
原 \(1,I_r\) 在几何纤维上生成，推出全模型无基点；平坦性使用实际纤维维数和相应平坦判据，不从无基点一词直接推出。
其无穷纤维准确为 \(r\mathcal D\)，包括剩余纤维的概形重数。

Ddiff 101–109 的原矩阵重复块给 \(\bar I_r=J^N\)。
故剩余态射是保持底域常数的坐标幂态射 \(\operatorname{Pow}_N\circ f_m\)，不误用绝对 Frobenius。
每条有限几何剩余纤维为 \(Nf_m^{-1}(h)\)，而 Ffib 供给的小阶完整纤维几何整、约化。

Gint 191–198 的原 \(1,I_r\) 基依赖单位边界限制和真实常数，不能由自由秩二替代。
Gint 207–220 用 \(f_{m*}\mathcal O=\mathcal O\) 与投影公式得到剩余基 \(1,J,\ldots,J^N\)，实际像为 \(1,J^N\) 的张成。
因此余核维数确为 \(N-1\)，并且这个维数不是 DVR 扭子长度。

本轮的模分裂直接由 C1 在相同模型上的派生特化给出；原 DVR 分裂段作为正确替代保留，不重复计算必要证明。
Ssplit 360–387 的赋值段仍不可删：若 \(m\nmid j\)，\(1-s^j\) 为单位；若 \(j=ml,\ v_p(l)=b<a\)，
\[
v_\pi(1-s^j)=e/\varphi(p^{a-b}),
\]
而这类 \(l\) 的数目是 \(\varphi(p^{a-b})\)。
我检查了所有 \(b=0,\ldots,a-1\) 的重数求和给 \(N-1\)，每层长度为 \(e\)，总长度 \(ae\)。
\(j=r\) 的零微分提供一个自由项；\(\prod_{j=1}^{r-1}(1-s^j)=r\) 给 \(\operatorname{Fitt}_0\mathcal T=(r)=(p^a)\)。
没有把总长度等于 \(ae\) 当成初等因子分布的证明；\(p=2\)、\(a=1\)、\(m=1\) 都在同一公式中。

### 3.5 W V2 与实际泛 Jacobian：两种不同义务

Wreuse 70–161 先提供谱几何前提。Bbad 的纯三次族变换与临界概形双向消元给一个首一四次式，临界概形因而有限。
我检查了反向代换所除的 \(u,v,z,T\) 在指定临界开集确为单位；因此不是只比较临界点集合。
这一路足以推出原参数泛点的几何光滑，含特征 2、3；不需要倒用实际临界总长度四或旧强 T3 的完整 \(4\times4\) 乘法特征多项式／Artin 出口。
谱双图的四端点、有限平坦推送 \(\mathcal O\oplus\mathcal O(-2\ell)\) 以及小曲线的 \(\mathcal O\oplus\mathcal O(-2)\) 都须保留。
这里 \(\ell\) 是域上精确阶；正特征自动 tame，C3 中取 \(\ell=m\)。

W-old-R 对任意原域的条件曾是真条件，不能用它自己的接受字样抹掉。
Wreuse V2 的 Step 2a 通过到 \(\bar k_0(c)\) 的忠实平坦扩张检验几何前提，再在原 \(k_0(c)\) 上执行谱模构造；W-R V2 对此复审。
即使常数扩张不可分，几何前提的下降与“原域上构造实际映射”这两步也不混同。
故旧 V1 缺口已被真实新增内容关闭，不在本轮重开为未解决数学问题。

Jspec 236–453 的实际 Jacobian 链我按下列义务逐一检查：

1. 原矩阵赋予谱双覆盖代数在秩二向量丛上的模作用。谱曲线光滑时不能出现所需局部标量障碍，局部循环向量使该模成为谱曲线上的线丛。
2. 构造对参数成为线丛族，而不只是每个几何点各选一个特征向量。推送平凡秩二丛固定次数 \(2\ell\)，Picard 刚性化处理代表的标量歧义。
3. 同一线丛恢复乘法矩阵到常数 \(\mathrm{GL}_2\) 共轭。原 \(M_{2\ell}=P\)、\((M_{2\ell-1})_{12}=w\) 和 \(M_0=t^{\ell-1}A_0\) 的规范／比值恢复原 \(x,y\)，给出实际有理逆。
4. 有理逆控制函数域总次数为一，包含不可分次数；这不是“在闭点上单射所以双有理”。
5. \(A:L\to\sigma^*L\) 的循环乘积是 \(\lambda\)，不是恒等。结合 \(\operatorname{div}\lambda=3\ell P_0-2\ell Q_2-\ell Q_1\) 得固定 Picard 差。
6. 循环商的拉回满足 norm–pullback \(=[\ell]\)。tame 使核为有限 étale；全群固定分歧点消灭可能的非平凡 character／核，不能仅以维数一断言无核。
7. 固定切空间的平均给恒等分量维数一；实际像为完整余类。原坐标有理逆把像识别为该余类，原域上定义的张量作用下降成 torsor，因此得到真正 Jacobian 同构，并不假定原域有点。

J-R 的相应论证及 DD 的接受与此相符。这部分虽长，却是 C3 的必要数学内容；不能降成两句“谱曲线也是亏格一”。

### 3.6 C3：先除后约化、公共阶与全开放模型理想

Ddiff 111–204 的循环插入保留原矩阵非交换次序。
对原迹微分，循环共轭使各插入的目标系数一致，先在整环上得到 \(dI_r=r[z^r]Q_r\)，再令 \(\alpha=m[z^r]Q_r\)。
这一先整除证明不能由特征 \(p\) 下 \(\bar I_r=J^N\) 的微分为零推出。

约化后把 \(m\) 个位置重新归组为重复块 \(B\) 的 \(dB\)，得到 \(\operatorname{tr}(B^{N-1}dB)\) 的对应谱系数。
Cayley–Hamilton 的 \(U_{N-1}(S,D)\) 递推与 \(d\det B=0\) 消去另一项。
\[
U_{N-1}(u+v,uv)=(u^N-v^N)/(u-v)
\]
被当作多项式恒等式使用，不要求矩阵可对角化或 \(u\ne v\)。
在奇特征得到四次式的 \((N-1)/2\) 次幂；特征二得到 \(S^{N-1}\)。
逐位系数论证利用次数界 \(2p-2\)（特征二为二），目标指数的每一位只能取 \(p-1\)，故得到完整 \(H_p^{1+p+\cdots+p^{a-1}}\)。
这里指数是标准 Hasse–Witt 迭代乘子；本报告在 §4、§5 实质扣除其先例，而不因作者自行给证明便把它变成新定理。

\(H_p\) 关于能级首一且次数 \(p-1\)，同时
\(J_x=m\bar t^m x^{-m-1}+\text{较低极阶项}\ne0\)。
故任何允许时间单位特化后 \(\bar\alpha\ne0\)；这才把整除下界提升为准确公共阶 \(ae\)。
\(m\) 不被 \(p\) 整除是此处不可删的理由，不能误写成对 \(r\) 求导仍有非零首项。

Gint 222–233 在光滑、正常的完整开放模型上对局部自由微分层做余维一延拓。
水平除子由特征零正则性处理，垂直泛点由上述整除处理；局部自由层的正常延拓把 \(\alpha\) 带到四条末端线。
约化等式在稠密环面成立后，由剩余完整模型上局部自由微分层的无扭性扩到所有开集。
因此系数理想是
\[
\overline{\mathfrak c(\alpha)}
=(H_p(T,J;\varepsilon)^{(N-1)/(p-1)})\,\mathfrak c(dJ),
\]
含坏能级和重数，而不仅是零点集合。
公共 \(\pi\)-阶是剩余曲面泛点处阶；Hasse 零层或状态临界点上的额外消失不与此矛盾。

### 3.7 原光滑闭能级与 Hasse：H.L(a) 的完整消费者

Hloc 193–257 的 L(a) 不能由一般泛点 Jacobian 同构直接替代。
对一个给定有光滑有理点的闭纤维，在保持剩余域的普通 henselization 上用 étale 光滑坐标提升该点。
该截面平凡化实际 torsor，给保持原能级参数的泛纤维同构。
两边总空间 regular、proper、flat；特殊纤维几何整且约化，作为唯一主纤维分量自交零，故都没有可收缩的第一类例外曲线。
正亏格最小正规模型唯一性于是把同一个泛纤维同构延拓成同底模型同构。
这一输入和 [Stacks 的正亏格最小模型唯一性](https://stacks.math.columbia.edu/tag/0C9Y) 条件吻合；[普通 henselization 保持剩余商及 DVR](https://stacks.math.columbia.edu/tag/07QL) 也已亲读核对。
Hloc 278–299 把本系统的 P/G/F、纯 W 模型和 J 的实际前提接入该引理，不只是陈述一个抽象引理。

对 C3 的几何闭能级，可先到代数闭域选光滑点，故这里没有把“任意原域有点”悄悄当成假设。
同构运输的是指定微分；奇特征的 Cartier 系数为 \(H_p^{1/p}\)，特征二用相应残差微分，Hasse 系数为 \(H_p\)。
Ddiff 206–233 在有限与无穷双图核查正则性，有限处分母为零时改用等价的另一偏导表达。
因此“原光滑能级 Jacobian 超奇异”等价于相应 Hasse 消失是实际对象上的结论。
没有把奇异三次曲线命名为超奇异；H.L(b)、L(c)、旧动力／全周期出口不被偷偷并入本 C1–C3 计分或容量。

## 4. 来源层级与最强先例扣除

### 4.1 本席直接公开亲读的外部范围

以下是本轮定向条件核查，不是外部文献全文综述。未下载或声称验收出版 PDF；不把自动打开页面等同全文读取。

| 来源 | 本席实际亲读范围 | 本轮用途／边界 |
|---|---|---|
| [Joshi–Roffelsen，arXiv 2508.18578v2](https://arxiv.org/html/2508.18578v2) | HTML §3.1 全段，含 Theorem 3.1、Remarks 3.2–3.5 及证明；§3.2 Conjecture 3.6 至谱式和相关说明 | 原矩阵、积分、圆分整数性、谱式与首项已有；不把猜想当定理 |
| [Gross–Hacking–Keel，Moduli of surfaces with an anti-canonical cycle](https://paulhacking.github.io/mlp.pdf) | 作者公开 PDF 的 Example 5.6、Construction 5.7、Remarks 5.8–5.9、Lemma 5.10 及紧邻段 | 八个 \((-2)\) 环及周期族是强近邻；未声称已核完本整数坐标等同 |
| [Wagner，arXiv 2410.23078v5](https://arxiv.org/html/2410.23078v5) | HTML §§1.4–1.8 的相关定义、Theorems 1.5、1.7、编号段 1.6 及边界说明 | 明确已有 \(T^j\mapsto(q^j-1)T^{j-1}\) 的对角形；完成／framing 条件仍保留 |
| [Wagner，arXiv 2510.04782v2](https://arxiv.org/html/2510.04782v2) | HTML Definition 1.6 的显示部分、编号段 1.7–1.10、Theorem 1.11、编号段 1.12–1.14、Theorem 1.15 的陈述与紧邻说明；未读其全部证明 | Habiro 下降依赖选定 q-Hodge 过滤；光滑规范存在结果有小素数条件，不能直接填本几何识别 |
| [Vlasenko，Higher Hasse–Witt matrices，1605.06440v3](https://arxiv.org/html/1605.06440v3) | HTML §1 的定义、Theorem 1(i)–(iii)、半线性解释与显示的其余 §1；未读 §3 完整证明 | Theorem 1(i) 已包含全部迭代乘子，不要求 ordinary |
| [Stacks 07VK](https://stacks.math.columbia.edu/tag/07VK) | Lemma 30.22.1 全陈述与证明 | Noetherian 源基上的 proper／flat 层给任意目标环派生基变换 |
| [Stacks 0C9Y](https://stacks.math.columbia.edu/tag/0C9Y) | Lemmas 55.10.1、55.10.2 全陈述与证明及 genus 0 反例 | 保持既定泛同构的正亏格最小模型唯一性 |
| [Stacks 07QL](https://stacks.math.columbia.edu/tag/07QL) | Lemmas 15.46.1–15.46.11 显示的陈述和证明，并读紧邻 12–13 | henselization 的剩余商、Noetherian、regular、DVR 性质；不是重做一般理论 |

### 4.2 继承证据及仍开放范围

§9 全文来源记录是本席直接读到的“本地证据”，其中对外部原文的获取／阅读仍属于相应来源实例，不能合并冒称本人通读。

Src-JR、Src-D 已关闭 JR 出版后文未读的“公开授权网页文本”子缺口，并把出版 Conjecture 3.7 对到作者 v2 的 3.6。
本席的额外作者版核对不撤销该关闭，也不把网页文本检查升级为出版 PDF 验收。
Src-OH 的 Ohyama 真正全文及 Src-GRT 的 GRT11 文章全文仍 OPEN；没有绕过访问限制或由摘要推断全文没有结果。
Ramani 讲义的低阶 qPI 精确坐标近邻、JL 的实读渐近段落、IVY 的循环谱商／Jacobian 框架均按共同来源记录扣除；本席没有声称这些原文全部亲读。
GHK/Friedman 的一般周期／节点理论、KS／Smirnov 的根单位与首非零分歧项、Frobenius/Dwork 联系同样保留，不说前人只看到零阶退化。

I-PF、Old-PF、Pt-PF 的组合扣除仅在其中实读的近邻接受源范围内有效。
P18 的相对 Kähler/Fitting 工具、P29 的多项式差商工具不能算新发明；P11 在模型群识别之后已直接包含旧完整循环公式。
旧循环不是 C1–C3 的 claim；承认其先例包含并不等于删掉旧周期来改判旧候选。
未进行 Papers 1–29 逐篇全文排除。Scholar/S2、部分 arXiv 获取与一般整数 Halphen 分类／引文图缺口保留。
“已读来源未见同一定理”仅支持有界非碰撞判断，不支持全球首次断言。

### 4.3 对当前主张逐项扣除后的准确剩余

| 当前内容 | 必须扣除的已有部分 | 仍实际需要本候选证明的部分 |
|---|---|---|
| 原对象及域上几何 | JR 原矩阵／积分／谱式；Halphen 与 GHK/Friedman 周期背景、近邻八环；谱模／循环商方法框架 | 全合同仍计入原坐标／完整模型与实际 Jacobian 的精确识别贡献；不因其在本地较早接受就扣成零，也不把已有背景与方法重新计新 |
| C1 对角模形状 | q-Hodge 的 \(q^j-1\) 对角微分已有；边界正规化与节点消元是标准工具 | 原无关系整数曲面的实际 \(R\Gamma\) 左侧、全共振 \(C_j\) 整下降和真实扩张消失 |
| C1 任意基变换／派生／Fitting | Stacks 派生基变换、Bockstein、长度一分解及 Ext、Fitting 形式运算 | 核实这些工具的本模型输入；不能每添一个任意量词或推论算一次方法创新 |
| C2 几何与扭子 | 迹的 Frobenius、Smith／圆分赋值与 C1 的形式特化 | 同一完整模型的原 pencil、原基／实际像与全概形重数精确识别；完整扭子分布是同一 C1 的消费者 |
| C3 乘子与 Hasse | Vlasenko Theorem 1(i) 直接含迭代乘子，且不须 ordinary；Cartier 规范及超奇异准则标准 | 从原非交换矩阵求导的整数先除桥接、四末端延拓、实际系数理想以及由真实 Jacobian／闭模型同构运输几何解释 |
| 公共阶与长度相等 | 两边一旦算出 \(ae\)，等式本身是同一参数的数值后果 | 本题给的是精确而有用的共同退化量；未证明新的典范同调比较或一般统一机制 |

Vlasenko 的扣除不是只扣“思想相似”：在准确谱系数识别后，其 Theorem 1(i) 已给出全部 \(1+p+\cdots+p^{a-1}\) 乘子。
具体复核 I-src2 §3 的比较映射：对 \(F(Z,\lambda)=\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3\)，Newton 多边形唯一内部整点为 \((1,1)\)，故其矩阵为秩一系数
\[
G_a=[Z^{N-1}\lambda^{N-1}]F^{N-1},\qquad
\bar G_a=[Z^{N-1}]U_{N-1}(T+hZ+Z^2,\varepsilon Z^3).
\]
后一式由 \([\lambda^{N-1}](\lambda^2-S\lambda+D)^{N-1}=U_{N-1}(S,D)\pmod p\) 得到，且 \(\bar G_1=H_p\)。
取参数的 \(p\) 次幂 Frobenius lift，Theorem 1(i) 就给所需乘子；可逆性仅属于该文随后 (ii)、(iii) 的更强结论。
这是本地比较映射与本人亲读定理条件的合用，不声称 Vlasenko 原文已有 qPI 整除微分定理。
同样，Wagner 的扣除不是只扣名字相近：有限单项式截断的右侧矩阵形状本来已在那里。
但这些先例没有在本席实际证据范围内直接给出本 \(S/R\) 的左侧识别、全共振几何截面与四末端上的原积分微分理想。
这两种判断必须同时保留，不能走向“全是旧定理”或“矩阵形状也是首次发现”的任一极端。

## 5. 第一门：新意 7.3 / 10，FAIL

最强正面理由是 C1：这不是对几个圆分 DVR 分别测秩，而是把原 qPI 几何在所有整数共振交会处的真实扩张一次消掉。
S 的全分支下降与单位边界把原积分系数真正嵌入 U 的 Bockstein 证明，C2 和 C3 又在同一模型上有明确算术消费者。
原坐标的先除后约化与实际闭能级解释也不是从相同谱方程自动得到的。这些足以使新意明显高于单纯重写 JR 或机械列推论。
完整合同所需的原坐标有理逆、任意 tame 精确阶的实际 Jacobian 识别及全特征几何接口也计入本席正面评价。
现有有界先例证据未直接包含其全部原对象识别；它们虽在本地旧批次已经接受，却不是因时间先后而被本席排除的贡献。本轮分数评价的是完整合同，不是只给新增四件的增量打分。

最强反对意见是：目标对象、周期八环和谱方法均已有强先例；核心对角结果的右侧形状已知。
剩下最实质的新增是“已知矩阵给出的明确截面使一个具体有理曲面族的扩张障碍消失”这一精确识别。
分支平坦下降、单位消元、Bockstein、Ext 和正常延拓的做法本身均为标准；C2 的完整 Smith 数据主要消费 C1，C3 的 Hasse 迭代更被直接一般先例包含。
公共阶与长度相等尚未升级为比较映射或结构性解释，故不能把这些相关输出累加成三套独立高新意方法。

我对反对意见的裁决是：确有值得论文报告的问题级剩余，但扣除后仍属强的模型特定算术识别，尚未给出足够突出的新机制或足够意外的新现象，使本席认可 7.5 的门槛。
这不是要求必须证明一条适用所有 Halphen 族的一般定理；一个足够锋利、非直接可预期的特例也可以过门。
本合同现有证据里，最强一环是 C1，其余两环的独立增量受强包含和共享消费者限制，因而本席给 7.3，而非 7.5 或更高。

该数值为本席综合判断，不是以 I-CD 的 7.0 为起点按工时、量词数或证明信心加分，也不由旧正式 7.6／7.4 平均。
I-CD 的 PROCEED_WITH_CAUTION、旧 CD 6.0／6.5 的方法扣除全部保留。
开放来源缺口限制“全球首次”的可信度，但我的 FAIL 主要基于已经实际看到的强先例及目前剩余的性质，不依赖想象一篇未读论文中必定有答案。
不能靠删除 Jacobian、弱化基变换量词、拆篇或换标题来把本评审改成 PASS。

## 6. 第二门：独立科学价值 8.1 / 10，PASS

这篇候选有一个完整问题，而非三组碰巧共享记号的计算：根单位参数在整数基上接近坏特征时，原系统哪些数据仍平坦延续，哪些线性系／微分信息真正退化？
C1 给出所有反典范阶的精确障碍模，C2 将其解释为原完整 pencil 特化的实际线性系跳跃与非约化纤维，C3 则表明原微分在零阶完全消失之后保留下来的首项受到 Hasse 控制。
\(N-1\)、\(ae\)、完整初等因子及超奇异除子各回答不同但相接的问题，不能仅凭相同数值互换。

其价值超过“已有定理再代一次参数”：只知域上 Halphen pencil，不能识别原截面特化像；只知 Frobenius 幂，不能知道整除微分在四末端如何延续；只知谱式，不能给原光滑闭能级的 Jacobian 解释。
候选把这些容易混淆的对象同时固定，并明确区分普通上同调基变换失败、派生基变换有效以及非典范分裂的边界。
因此即使方法新意未到本项目的 7.5 门槛，它仍有独立算术几何内容，值得作为一个自足研究问题保存。

不给更高价值分的原因是适用对象仍为单一 qPI 族，完整比较结构、过滤／乘法相容和一般机制未建立。
旧全周期、动力分箱或完整临界多项式不被当作额外卖点搬回本候选。
价值 PASS 与新意 FAIL 并不矛盾；本席不将价值分拿来补新意门。

## 7. 第三门：完整证明信心 9.1 / 10，PASS

本席没有发现新的硬数学反例或尚未接上的必要接口。
该判断覆盖完整 C1–C3、四末端、全共振、任意基变换、全部初等因子、真实泛 Jacobian 和原光滑闭能级模型，而不只是最短增量。
支持超过 9 的具体依据是：

- 非正规共振基的下降有平坦极点商的实质论证，非零首项被提升成全边界单位；不是稠密点集推断。
- 常数、边界、Bockstein 有限阶、非局部商单位和 \(\operatorname{Ext}^2\) 五个容易断开的步骤已分别接上。
- C2 的抽象自由秩与原 \(1,I_r\) 基、剩余基与实际像、余核维数与 DVR 长度明确区分。
- 小素数没有被静默排除；剩余精确阶 \(m\) 与原 \(r\) 分开，泛光滑、Cayley–Hamilton 和 Cartier 都给相应处理。
- J 的家族性／有理逆／不可分次数／固定差／无核／原域 torsor 都有证明，H.L(a) 再提供闭能级需要的同底模型接口。
- W V1 的原域条件经 V2 实际更改关闭；S/U 的历史待合取经最终哈希的 Ss-R 与 DI 关闭。不是把错误旧件覆盖成无失败历史。
- 公开一手条件核查与现有局部证明所需的 Stacks、Vlasenko 等条件相符。

9.1 不是形式化证明证书，也不是把十二份既有非作者 PASS 当作独立概率相乘。
仍有人工长链审读的普通漏检风险，尤其是原矩阵规范、谱 Picard 家族与模型同构在正式正文转写时的保持。
现有证明为中文研究底稿而非已排版英文稿；未来若转写省略必要论证，会改变论文层面的完整性，但那不是本次冻结底稿已经存在的数学缺口。
本次不重新打开已通过且输入未变的阶段来追求形式上的更多票数，不新增未授权证明修订。
若后续取得新的直接包含先例，那会影响新意和来源归属，不能倒推本轮已核证明必然错误。

## 8. 第四门：自然完整正文 22–30 页，PASS

估计针对匿名英文单栏、11pt、letter、四边 1 inch、标准行距，必要证明全部在正文，参考文献另计。
未写英文正文、未试排、未运行 LaTeX、未用文件数／源文件行数／投入工时换算页数。
低／中／高是对正常论证密度、连接文字和公式展开幅度的编辑预测，不是数学上下界或统计置信区间。

| 必要正文块 | 必须保留的实质内容 | 低 | 中 | 高 |
|---|---|---:|---:|---:|
| 问题、规范与主定理 | C1–C3 完整量词、原积分及全共振区别、最强先例定位 | 1.75 | 2.25 | 2.75 |
| 原曲面与极除子／周期 | 八中心、四末端图及无极点、八环、精确极阶、节点单位粘合 | 3.50 | 4.00 | 4.75 |
| 域上完整 pencil 与有限纤维 | 最小性、Stein 总次数、全特征泛光滑、Picard 格与整约化分量证明 | 2.00 | 2.50 | 3.00 |
| 全共振整数截面 | S Steps 1–5：全部约数分支、重复块、平坦极点商下降、单位边界 | 3.00 | 3.75 | 4.50 |
| 通用上同调与派生基变换 | 逐吹起常数、节点复形、真实 Bockstein 分裂、Ext²、任意基及 Fitting | 2.25 | 2.75 | 3.25 |
| 圆分完整模型与 Smith 消费者 | 原整截面／平坦 pencil、幂特化、原基／实际像、全部圆分赋值与重数 | 2.25 | 2.75 | 3.25 |
| 纯谱几何与 W V2 前提 | 三次变换、临界概形双向消元及有限性、双图端点、推送、循环商、Step 2a | 1.50 | 2.00 | 2.50 |
| 实际泛 Jacobian | 家族谱模、常数共轭、原坐标有理逆及不可分次数、固定差、无核、原域 torsor | 4.00 | 4.75 | 5.75 |
| 原整除微分与全理想 | 循环插入、先除、CH、逐位系数、非零首项、四末端延拓、公共阶及系数理想 | 2.25 | 2.75 | 3.50 |
| 闭模型与 Hasse 解释 | H.L(a) 完整前提和证明、实际应用、指定微分／Cartier、原光滑层与限制 | 1.75 | 2.25 | 2.75 |
| 合计 | 参考文献另计；无必要证明外置 | **24.25** | **29.75** | **36.00** |

可信的窗内写法来自真实共用，不来自删证：八截面／节点结构只证明一次，C2 通过同模型 C1 特化，不另抄 S 的 DVR 分裂替代证；W 的谱前提只论证一次供 J 与 H 消费。
S 的全共振截面和完整赋值段仍分别留在第四、六块；J 与 H.L(a) 分别得到独立篇幅，未缩成“由标准理论可知”。
旧强 T3 的全乘法矩阵／Artin 输出和不属于 C1–C3 的完整动力／周期出口不反灌，不是删除本合同必要内容。

低于 22 页的风险不大：只要四末端、全共振下降、实际 Jacobian 和闭模型接口都完整书写，它们本身提供足够实质内容。
若被压到明显少于 22 页，最应怀疑的是这些接口被引用名称代替，而不是需要加无关背景灌水。
超过 30 页的风险较明显：谱线丛家族与有理逆、全共振下降、H.L(a) 的前提说明都会膨胀；高值 36 页保留了这种可能。
中值 29.75 靠近上沿，不能当作“稳在 30 页以内”的承诺。

本席仍判 PASS，因为去除重复替代证明后，约 27–30 页的正常完整表达有实质可信度，低预测也无需异常紧排或删除义务。
这不是附加“中值必须在窗内”的新门；判定依据是存在自然、完整、同一科学合同的窗内组织方式。
没有通过移必要证明至附录、缩版、减字、拆篇、删量词或先试写测页获取该结论。
没有声称英文稿或 PDF 已被验收。

## 9. 55 件共同输入：本人 FULL 与实际身份核对

以下文件均位于本报告同目录。每行 FULL 明确指本人读取 1–所列末行；MATCH 为实际行数和 SHA-256 均与冻结清单／任务所给身份一致。
十二作者＋十二非作者＋六纠错＋九整数来源＋十三旧／负面／缺口＋三入口＝55。
本表由末次实际只读身份检查结果填写，不以来源文件内的自述哈希替代实测。

| ID | 文件 | 实际行数 | 实际 SHA-256 | 本人实读 | 身份 |
|---|---|---:|---|---|---|
| P | [PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | 275 | `61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3` | FULL 1–275 | MATCH |
| Nbd | [PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 284 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` | FULL 1–284 | MATCH |
| Gfield | [PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 270 | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` | FULL 1–270 | MATCH |
| Ffib | [PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 466 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` | FULL 1–466 | MATCH |
| Jspec | [PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | 492 | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` | FULL 1–492 | MATCH |
| Bbad | [PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | 488 | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` | FULL 1–488 | MATCH |
| Wreuse | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md) | 213 | `21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2` | FULL 1–213 | MATCH |
| Hloc | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md) | 637 | `0a6624550ed0f8765b51b01a1a481fd9a545d1791e10c3431effbf3f25428a3e` | FULL 1–637 | MATCH |
| Ddiff | [PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 268 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` | FULL 1–268 | MATCH |
| Gint | [PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 254 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` | FULL 1–254 | MATCH |
| Ssplit | [PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md) | 418 | `2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac` | FULL 1–418 | MATCH |
| Ucoh | [PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | 255 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` | FULL 1–255 | MATCH |
| P-R | [PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_NON_AUTHOR_REVIEW_V1_20260908.md) | 237 | `edbf54720c0bd0624d8f6eb53d06db43965d66436b6b9a52ba67c4ef1b6f4dd0` | FULL 1–237 | MATCH |
| N-R | [PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_NON_AUTHOR_REVIEW_V1_20260908.md) | 287 | `769c34ec3302e8f91bce13c86add8930f1ba032c5ec8a3490dcc49963af70597` | FULL 1–287 | MATCH |
| Gf-R | [PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | 348 | `0964f6f0a6eb543402e0f2b2096fd5325d4eaf9912a7d8cd056b9d8193920972` | FULL 1–348 | MATCH |
| F-R | [PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_NON_AUTHOR_REVIEW_V1_20260908.md) | 238 | `2b55ec53c0f677922eaf3d1f184c7066bd351ac5e5afd59f6d4a73f2b78f3bfb` | FULL 1–238 | MATCH |
| J-R | [PAPER30_QPI_LAX_JACOBIAN_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | 257 | `c7d355d420e966381dfc74fffbd033470e12158480a826e0d88e464a5fa40438` | FULL 1–257 | MATCH |
| B-R | [PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | 259 | `1bb3d563bdb5a2c93aa517002f69ac72398688ee74429a8b4d8662965c229815` | FULL 1–259 | MATCH |
| W-R | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md) | 124 | `0db56630eab29ed89952f28dd2fd8038fa3c724040f99afbec527dd0e42c70f2` | FULL 1–124 | MATCH |
| H-R | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260909.md](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260909.md) | 413 | `10122ea2a617203dcf0ef7d9755ce0ae22ec7906c70ab141891998f94294093b` | FULL 1–413 | MATCH |
| D-R | [PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md) | 306 | `7c0ecd10991f80f0614713f344ab600a4eb69fd7356135fcfc927ed71a95d0bb` | FULL 1–306 | MATCH |
| Gi-R | [PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md) | 286 | `ec49d4eaadbf4c0d53603cf6c902df375e2b1c779b6f243897521d786b206a0b` | FULL 1–286 | MATCH |
| Ss-R | [PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_CHECK_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_CHECK_V1_20260909.md) | 413 | `ae768ae89301af115dc917e9a4b075b401258fb563628e1238b01844a30da941` | FULL 1–413 | MATCH |
| U-R | [PAPER30_QPI_UNIVERSAL_COHOMOLOGY_CHECK_V1_20260909.md](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_CHECK_V1_20260909.md) | 284 | `9f54da405b8a40f58e34dc372fad7200452871171a92a0e0063edf1742e3cd55` | FULL 1–284 | MATCH |
| W-old | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V1_20260908.md](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V1_20260908.md) | 196 | `ec978801e842ce21a54ae7fd4982cd5b7fec449644c10cea49dc02b4b502eb16` | FULL 1–196 | MATCH |
| W-old-R | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260908.md](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260908.md) | 242 | `bb70f7c39c91d7b719f18c8358481c8ebe6bea009fe20718741ae4c8784b2949` | FULL 1–242 | MATCH |
| DG | [PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md](PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md) | 173 | `ed09aadb40752ed579bc45edb7b3531c1f78f6c7f7413072cd120315f2b22245` | FULL 1–173 | MATCH |
| DD | [PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md](PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md) | 224 | `0bfbde8003d049d80523a2001d410dfa4f38ab2f14838d2dbbe4c1363f7155a7` | FULL 1–224 | MATCH |
| DH | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md) | 87 | `40e4fa6460d34ebff7cfc0e20d614f3a2050590f10c58605819cba867e65dad7` | FULL 1–87 | MATCH |
| DI | [PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md) | 162 | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` | FULL 1–162 | MATCH |
| I-src1 | [PAPER30_QPI_CYCLOTOMIC_DEGENERATION_PRIOR_ART_V1_20260909.md](PAPER30_QPI_CYCLOTOMIC_DEGENERATION_PRIOR_ART_V1_20260909.md) | 178 | `1c7ba39e3c2d6d661626e736b16f6d9a9599e0a8d07c0b2ead9e41f798da0cf8` | FULL 1–178 | MATCH |
| I-src2 | [PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md](PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md) | 168 | `8d24144c5e49ba30402a2749536ec0b66ca6170d6dcf9a85273330829c22a88f` | FULL 1–168 | MATCH |
| I-src3 | [PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md](PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md) | 81 | `12628cbef7904732212424ee545451e709438d4d2a23909d6f2d3e69117ae6ad` | FULL 1–81 | MATCH |
| I-src4 | [PAPER30_QPI_INTEGRAL_COHOMOLOGY_PRIOR_ART_V1_20260909.md](PAPER30_QPI_INTEGRAL_COHOMOLOGY_PRIOR_ART_V1_20260909.md) | 148 | `26e901d014f553773838f20b1b3ea46b607deffbcf9d73a503cab3ef24570450` | FULL 1–148 | MATCH |
| I-A | [PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md](PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md) | 107 | `bb463d1e1c27f543e4a0fe1bda17b584ffce28148e49ab1e1f3c3b1fce6b7ad5` | FULL 1–107 | MATCH |
| I-B | [PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md) | 295 | `44f628fbc07cad422f83c136cf1dd3fb2bae9d7a7782db3798a073b5ab1bdf41` | FULL 1–295 | MATCH |
| I-CD | [PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md) | 267 | `d76e5e71001cd8033608a76673f61169f264caee57cb37aab4f86d1390dd8f02` | FULL 1–267 | MATCH |
| I-PF | [PAPER30_QPI_INTEGRAL_PORTFOLIO_DELTA_V1_20260909.md](PAPER30_QPI_INTEGRAL_PORTFOLIO_DELTA_V1_20260909.md) | 245 | `a99af060d92829a6412f283ba2affb3dedab04a864d567a426de82ed98ca91f3` | FULL 1–245 | MATCH |
| I-PRE | [PAPER30_QPI_INTEGRAL_PREFLIGHT_DISPOSITION_V1_20260909.md](PAPER30_QPI_INTEGRAL_PREFLIGHT_DISPOSITION_V1_20260909.md) | 133 | `1ff8473c05956d88075dacc9705d79d621b2e9db059b59f5b13f06c72326641e` | FULL 1–133 | MATCH |
| Old-AB | [PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md](PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md) | 268 | `4470af64294525bc4ae33b9b00fc38c44c38215290a36fa6f3a5b6bdf861f90e` | FULL 1–268 | MATCH |
| Old-B | [PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md](PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md) | 112 | `2aae448ca17022aa7b51990b84058e57ee455ab0e4c0a4127d8e0ec7fc39c898` | FULL 1–112 | MATCH |
| Old-CD | [PAPER30_QPI_NOVELTY_PHASE_CD_V1_20260908.md](PAPER30_QPI_NOVELTY_PHASE_CD_V1_20260908.md) | 247 | `8dadbaf066979a17ac87620ad5017e8e732c52ee81a68e4fc2ff545a249ecb82` | FULL 1–247 | MATCH |
| Old-PF | [PAPER30_QPI_PORTFOLIO_NONCOLLISION_V1_20260908.md](PAPER30_QPI_PORTFOLIO_NONCOLLISION_V1_20260908.md) | 258 | `5e89a61ab4386912d1cb2280ab4e314486ec8a3c9161585e5a26e302875065bc` | FULL 1–258 | MATCH |
| Pt-AB | [PAPER30_QPI_POINT_PERIOD_PRIOR_ART_SEARCH_V1_20260908.md](PAPER30_QPI_POINT_PERIOD_PRIOR_ART_SEARCH_V1_20260908.md) | 321 | `75a1324e1fbefba2251f412435b4a76c180d9525dddb4b4f341c9c8344e1ccba` | FULL 1–321 | MATCH |
| Pt-CD | [PAPER30_QPI_POINT_PERIOD_NOVELTY_PHASE_CD_V1_20260908.md](PAPER30_QPI_POINT_PERIOD_NOVELTY_PHASE_CD_V1_20260908.md) | 301 | `48bdccfe07f05fb669cce9d188908b9a16988488146023534d19209b774d1fa7` | FULL 1–301 | MATCH |
| Pt-PF | [PAPER30_QPI_POINT_PERIOD_PORTFOLIO_DELTA_V1_20260908.md](PAPER30_QPI_POINT_PERIOD_PORTFOLIO_DELTA_V1_20260908.md) | 243 | `7216525bf1226d4d0512eb7ca0e7b94a8573a4c18520e27afa6f0fefaa28c65d` | FULL 1–243 | MATCH |
| FAIL-V1 | [PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md](PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md) | 136 | `0452b7aa8f28107ae65f3fa840647806b50eab2502340d1c609a0ca6c545ce90` | FULL 1–136 | MATCH |
| FAIL-V2 | [PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md](PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md) | 116 | `fb490d26321a3077b839d1e3505979150b7ad02bf59c6f5beba93a9977003584` | FULL 1–116 | MATCH |
| Src-JR | [PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md](PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md) | 98 | `ab82c19d1bd6a182323b033f7d8c48e47de4e0839a9d5bebd2e4ead456ad4475` | FULL 1–98 | MATCH |
| Src-OH | [PAPER30_QPI_OHYAMA_SOURCE_GAP_CHECK_V1_20260909.md](PAPER30_QPI_OHYAMA_SOURCE_GAP_CHECK_V1_20260909.md) | 137 | `2cc3fa6636ff0bf878d54b5f32feb36755054a586dc1ba1f6e484dafdfd715e6` | FULL 1–137 | MATCH |
| Src-GRT | [PAPER30_QPI_GRT11_SOURCE_GAP_CHECK_V1_20260909.md](PAPER30_QPI_GRT11_SOURCE_GAP_CHECK_V1_20260909.md) | 133 | `67b27d4662f3f51a9552795676b5294e9eacd400d8ca1a38820a5a1b9c183356` | FULL 1–133 | MATCH |
| Src-D | [PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md](PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md) | 73 | `34985ed628bfc2185f9674490f41766d6ce11a0d63da018962791d833d6d1c01` | FULL 1–73 | MATCH |
| BRIEF | [PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | 270 | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` | FULL 1–270 | MATCH |
| MAP | [PAPER30_QPI_INTEGRAL_CURRENT_PROOF_MAP_V1_20260909.md](PAPER30_QPI_INTEGRAL_CURRENT_PROOF_MAP_V1_20260909.md) | 463 | `2be7d61d083c39d8268f212f0a0e0d3bed23ba40feb29469c920f146f715b0d1` | FULL 1–463 | MATCH |
| MANIFEST | [PAPER30_QPI_INTEGRAL_REVIEW_INPUT_MANIFEST_V1_20260909.md](PAPER30_QPI_INTEGRAL_REVIEW_INPUT_MANIFEST_V1_20260909.md) | 210 | `597ca2b5c6402ea93305d3ceade369b6cc373d9c84cfa73be0675e4c22ac3b6e` | FULL 1–210 | MATCH |


另亲读了用户提供的 AGENTS、工作流及相关技能指令；这些是执行规范，不计入 55 件科学共同输入。
本轮外部定向亲读限于 §4.1；§4.2 的继承／开放来源状态没有被篡改。

## 10. 残余风险、禁止外推与冻结结论

本轮没有新硬数学缺口需要给出反例或新增证明义务；主要残余是已披露的直接先例覆盖不足、非形式化人工审读和自然篇幅上沿风险。
开放的 Ohyama／GRT11 全文及一般整数 Halphen 比较可改变原创性定位，但不能由“未取到”推成有／无包含。
以后若继续研究，首先应区分“新增直接科学内容”和“补齐归属证据”，而不能把更多整理、更多同模型票数或证明的英文转写算成新意增量。
本报告不授权为过门改变 C1–C3，也不提出删必要接口或改阈值的建议。

旧 qPI T1–T7 数学接受保持；旧完整 V2 的 7.6／7.4 双份合取 FAIL 保持。
本席没有借旧票有利分项、没有与另一席平均、没有将 7.3 四舍五入成 7.5。
本 Integral V1 的本席四门结论是 **FAIL ∧ PASS ∧ PASS ∧ PASS = FAIL**。
该结论只是一席完整正式审查，不推断另一席结果，不自行作两席最终处置，不建立 Paper30 或解除后续产物边界。

到此完成本席有界任务；报告提交后冻结。
