# Paper30 qPI Integral V1：首次完整正式候选评审 R2

日期：2026-09-09。对象：冻结共同包的完整 C1–C3。
评审身份：新派发的非作者 R2；本件不是旧 T1–T7 重评，也不是只审整数增量。
执行：可用 Codex 同一继承模型家族，按 research-review 的 xhigh／证据链要求独立审查。
route_applicability: NOT_APPLICABLE。
校准状态：NOT_CALIBRATED；criteria_binding_unavailable。

## 1. 独立结论与四门合取

本席结论：完整候选未通过本轮准入。失败门是扣除强先例后的新意，不是发现了新的硬数学错误。
其余三门已经各自完成；不因首门失败省略，也不以其通过抵消首门。

| 门 | 本席独立判断 | 固定门槛 | 结果 |
|---|---:|---:|---|
| 新意 | 7.3 / 10 | 至少 7.5 | FAIL |
| 独立科学价值 | 8.1 / 10 | 至少 7.5 | PASS |
| 完整证明信心 | 9.2 / 10 | 至少 9 | PASS |
| 自然完整实质正文容量 | 22.9 / 28.5 / 34.6 页的低／中／高预测；22–30 页存在可信自然写法 | 可信 PASS / FAIL | PASS |
| 本席四门合取 | FAIL ∧ PASS ∧ PASS ∧ PASS | 四门同时通过 | FAIL |

7.3 不是把既有 7.0 加上工作量，也不是沿用旧正式票；8.1 与 9.2 不借自他席。
这里的数字是有界材料下的非校准学术判断，不是正确概率、期刊接受概率或区间端点。
不平均、不拼接旧票、不四舍五入。另一席本轮报告及其内部信息未读取，故本件不替主控计算双席合取。

最强正面事实是 C1：在原八截面曲面上构造整个共振整数基的真实单位边界截面，
并由它消去真实上同调扩张，而不只列出各域纤维的维数。
最强反面事实是：右侧对角复形、域上周期几何、原迹积分、全部 Hasse 迭代乘子及后续形式工具已有强先例。
扣除后，剩下的是扎实而具体的原模型整数实现及桥接，尚不足以令我把完整候选的新意评为至少 7.5。
这不等于要求每篇论文必须创造一种一般理论；此处评价的是本候选实际新增的数学距离。

## 2. 执行边界、阅读责任与证据层级

本人已全文读取三入口及 manifest §§2–6 的 52 件，共 55 件。
作者证明、12 份对应独审、真实纠错与接受、完整新旧来源、负面意见及失败处置均在本人 FULL 范围内。
逐件实际行数与 SHA-256 均与派发身份一致；完整台账见 §9。
FULL 来自分块正文阅读，不来自组织者的 RANGE、摘要、PASS 标签或仅运行哈希程序。
后续定向重读／导航检索不增加 FULL 件数，也不把一次截断的导航输出当作全文证据。

本轮阅读了允许的 AGENTS／WORKFLOW 和相关技能。
research-review 用于证据链、强反对意见和完整评价；
ARS 仅用于来源披露和审查思维，没有启用默认五席、ML 实验或期刊评分流程。
固定双份四门合同优先。GPT-5.4 MCP 未配置；没有调用或伪称调用该接口。
没有进行人类或跨模型认证，不声称两席错误分布独立；共同包已披露历史分数，不能称历史盲审。

只新增本报告。未改共同输入、作者件、旧报告、README／BATCH、项目、锁或冻结产物。
未创建英文正文、试排、PDF、实验、额外本地来源文件或通用基础设施。
未委派子席、未向另一席通信、未调用外部评审 API、未上传候选、未投稿或发信。
只按允许范围定向浏览公开一手入口；本人直接阅读范围与继承来源记录严格分开，见 §5。
没有用未取得全文来论证全球不存在先例。

旧接受及旧失败保持：旧 T1–T7 数学接受不撤销；旧完整 V2 的 7.6／7.4 双份合取 FAIL 不变。
旧 CD 6.0、点／周期 CD 6.5、当前整数 CD 7.0／PROCEED_WITH_CAUTION 是已披露背景，不是本席结论。
旧正式评分报告本身未打开；相关失败仅按共同包指定处置件全文读取。
W V1 的范围缺口按真实 V2 Step2a 修正及 V2 非作者复审处理，不回退为当前未补缺口。
U 报告中的历史条件措辞按同哈希 S 审查及 DI 的真实合取读取，不误判为现存作者自签。

## 3. 本席评判的完整数学对象

### 3.1 原整数模型与不能删去的末端状态

取无关系底环
\[
R=\mathbb Z[q^{\pm1},\tau^{\pm1}],
\qquad L_n=\mathcal O_S(nD),\qquad \mathcal V=S\setminus D.
\]
在原 \(\mathbb P^1\times\mathbb P^1\) 上实施 \(1+2+3+2\) 次吹起。
四次末端中心分属不同边界分量，单位坐标为 \(1,\tau,\tau,q\)；
参数的数值偶合或剩余阶下降不合并中心。
\(D=-K_{S/R}\) 是相对 SNC 八环；完整环面补集 \(E\) 还包含四条末端例外曲线，故 \(E\ne D\)。

| 末端簇 | 原坐标的最后图；取 \(u=0\) 得完整末端仿射线 |
|---|---|
| 1 | \(x=u^{-1},\ y=1+uv\) |
| 2 | \(x=u(\tau+uv),\ y=u^{-1}\) |
| 3 | \(x=u(\tau+uv),\ y=u^2(\tau+uv)\) |
| 4 | \(x=[u(q+uv)]^{-1},\ y=u^{-1}\) |

这些线属于 \(\mathcal V\)，不是可删的边界状态。
模型、极除子与法丛证明须涵盖它们；C3 的整微分和理想等式也须延伸到这里。

原矩阵 \(A(z)\) 固定为 BRIEF §2.2／JR 的矩阵，保持
\[
M_j(z)=A(q^{j-1}z)\cdots A(qz)A(z),\qquad \det A(z)=z^3.
\]
在精确 \(j\) 阶分支，\(I_j=[z^j]\operatorname{tr}M_j(z)\) 是原积分。
在整个 \(B_j=R/(1-q^j)\) 上只使用
\[
C_j=[z^j]\operatorname{tr}M_j(z).
\]
非本原分支上不能把它改成 \(\operatorname{tr}M_j(1)-(\tau^j+1)\)。

### 3.2 C1：完整上同调及同一派生复形

对每个 \(n\ge0\)，合同包含
\[
H^0(S,L_n)=R\langle1\rangle,\quad
H^1(S,L_n)\simeq\bigoplus_{j=1}^nR/(1-q^j),\quad
H^{i\ge2}(S,L_n)=0,
\]
并且边界过滤的每个真实短正合列分裂。
必要截面是整个 \(S_{B_j}\) 上的 \(C_j\in H^0(L_{j,B_j})\)，
其 \(x^{-j}\) 帧首系数为单位
\[
(-\tau)^j q^{j(j-1)/2}.
\]
存在保留真实常数项的非典范同构
\[
K_n:=R\Gamma(S,L_n)
 \simeq R[0]\oplus\bigoplus_{j=1}^n[R\xrightarrow{\,1-q^j\,}R],
\tag{1}
\]
两项复形在次数 \(0,1\)。
每个固定 \(n\) 选一次后，对所有交换 \(R\)-代数 \(A\) 派生拉回成立，包括非平坦、非约化、非 Noetherian 的 \(A\)。
因此 \(H^0\) 为 \(A\oplus\bigoplus_j\operatorname{Ann}_A(1-q_A^j)\)，
\(H^1\) 为 \(\bigoplus_j A/(1-q_A^j)\)；第一个 \(A\) 是实际常数子模。
另有
\[
\operatorname{Fitt}_0H^1(S,L_n)
=\left(\prod_{j=1}^n(1-q^j)\right)
=\left(\prod_{d=1}^n\Phi_d(q)^{\lfloor n/d\rfloor}\right).
\]
\(n=0\) 使用空直和及单位 Fitting 理想。
合同没有跨 \(n\) 的乘法／cup／动力／对偶兼容性，也不声称普通 \(H^0\) 总与非平坦基变换交换。

### 3.3 C2：同一圆分模型、准确特化像及全部初等因子

任取 \(p\)（包括 2、3）、\(a,m\ge1\)、\(p\nmid m\)，置 \(N=p^a,\ r=mN\)。
在 \(\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}\)、\(\mathfrak p\mid p\) 上，
\(s=\zeta_r,\ t\in\mathcal O^\times,\ e=v_\pi(p)\)，剩余 \(\eta=\bar s\) 精确阶为 \(m\)，
\(J=I_{m,\eta}(x,y;\bar t)\)。
原 \(1,I_r\) 给同一光滑射影相对曲面上的无基点、射影平坦 pencil，
\[
f_r^{-1}(\infty)=r\mathcal D,\qquad
\bar f_r=\operatorname{Pow}_N\circ f_m,\qquad f_m=J.
\]
这里的幂态射固定剩余域常数，不是绝对 Frobenius。
有限几何纤维准确为 \(Nf_m^{-1}(h)\)，其中小阶纤维几何整且约化；无穷纤维为 \(r\bar D\)。

完整截面与实际特化像分别为
\[
H^0(\mathcal S,\mathcal L_r)=\mathcal O\langle1,I_r\rangle,\quad
H^0(\bar{\mathcal S},\bar{\mathcal L}_r)=\kappa\langle1,J,\ldots,J^N\rangle,\quad
\operatorname{im}=\kappa\langle1,J^N\rangle .
\]
由同模型 C1 特化，
\[
H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus\mathcal T,\quad
\mathcal T\simeq\bigoplus_{b=0}^{a-1}
\left(\mathcal O/(\pi^{e/\varphi(p^{a-b})})\right)^{\oplus\varphi(p^{a-b})}.
\tag{2}
\]
故 \(\operatorname{length}\mathcal T=ae\)，最少生成元数 \(N-1\)，
\(\operatorname{Fitt}_0\mathcal T=(r)=(p^a)\)。
特化余核维数 \(N-1\) 不等于该 DVR 模长度的定义。

### 3.4 C3：先整除后约化、完整理想及真实 Hasse 接口

令 \(d\) 仅对原状态 \(x,y\) 微分，固定 \(s,t\)。
在完整 \(\mathcal U=\mathcal S\setminus\mathcal D\) 上，
\[
\alpha=p^{-a}dI_r\in\Gamma(\mathcal U,\Omega^1_{\mathcal U/\mathcal O}),\qquad
\bar\alpha=H_p(T,J;\varepsilon)^\sigma\,dJ,
\quad T=\bar t^m,\ \varepsilon=(-1)^{m+1},\ \sigma=\frac{N-1}{p-1},
\tag{3}
\]
其中
\[
H_p(T,h;\varepsilon)=
\begin{cases}
[Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
h,&p=2.
\end{cases}
\]
\(H_p\) 关于 \(h\) 首一、次数 \(p-1\)。
系数理想在整个剩余开放模型上满足
\[
\overline{\mathfrak c(\alpha)}
=(H_p(T,J;\varepsilon)^\sigma)\mathfrak c(dJ),
\quad
\operatorname{ord}_{\bar{\mathcal U}}(dI_r)=ae
=\operatorname{length}_{\mathcal O}\mathcal T.
\tag{4}
\]
横线是理想在剩余结构层中的像；等式保留坏能级和四条末端线的概形重数。
公共阶是沿剩余曲面泛点的阶，不是所有提升闭点的赋值。
除公共因子不等于 \(\pi\)-饱和，数值相等不等于构造了典范模同构。

谱曲线
\[
E_{T,h}:\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3=0
\]
采用原双图的完整光滑模型及指定微分
\(\omega=dZ/(2\lambda-(T+hZ+Z^2))\)，特征二采用分母 \(T+hZ+Z^2\)。
在光滑能级上，\(H_p\) 是该规范的 Hasse 系数；
完美域上 Cartier 一维矩阵为 \(H_p^{1/p}\)，二者不混同。
实际泛 Jacobian 与原光滑闭能级的同底完整模型识别是合同的一部分，
不能用“都是亏格一”或重命名多项式代替。

## 4. 本人完整证明审读：必要链与危险接口

以下结论来自作者正文及对应实际复审的全文审读，再核对消费者；既有接受只作证据，不替代判断。
行号均对应 §9 绑定的字节版本。这里没有发现新的硬数学反例或缺失量词。

### 4.1 共同几何底座：P、Nbd、Gfield、Ffib

P Steps2–6（116、150、165、196、242 行起）逐个恢复八中心和反典范八环，
由实际动态传递计算八个边界赋值，并用四个完整局部映射检查末端例外无额外极点。
不能只从一个 Laurent 首项推断整个极除子；当前证明确有后续传播和末端图。
域上光滑曲面正规，余维一正则性到全截面的延拓适用；这不被误用到非正规共振底环。

Nbd Steps1–7，尤其 180、205、249 行起的单位标架，给四个非平凡传播比
\(-1/t,-1,-1/s,-t\)，总乘积 \(s^{-1}\)。
这里使用实际单位公式替换 \(s,t\) 为无关系 \(q,\tau\)，不是把域上线丛分类无证明推广至整数环。
四中心在不同分量且参数全为单位，特征 2、3 或阶下降不产生中心碰撞。

Gfield Steps1–5（95–238）先由边界序列和 Riemann–Roch 得最小阶截面数与原 \(1,I_r\)。
Stein 分解及投影公式排除的是全部复合次数，包括纯不可分次数；
不能从几何点上的泛单射或仅计算亏格代替该步骤。
其 SNC 无穷纤维局部式及 \(r\) 在所在域可逆，排除横向临界集，再由 properness 得泛光滑。
此处域上的阶分别是泛特征零的 \(r\) 和剩余特征的 \(m\)，不把 \(r\) 在剩余域错误当作单位。

Ffib Steps1–2（128–246）实际解八边界类的整数正交格，所得秩二 Gram 矩阵为
\(\left(\begin{smallmatrix}-8&8\\8&-8\end{smallmatrix}\right)\)。
伴随与非负算术亏格迫使有限纤维不可约分量的类为正倍数 \(lD\)；
最小 pencil 的约束迫使总纤维只能有一个分量且重数一。
Cartier／Cohen–Macaulay 性排除隐藏嵌入分量。
因此 C2 消费的是所有有限几何纤维整约化，不只是泛纤维。
Ffib 后续 Chern 长度四、完整临界值多项式等旧正确出口已全文可见，但不是把它们全部计入新正文的理由。

### 4.2 C1 的非形式核心：整个共振基上的真实截面

Ssplit Steps1–5（112 行起；重点 131–227）没有用非正规 Hartogs。
完整环面补集 \(E\) 是相对 SNC Cartier 除子，且 \(E\) 对底环平坦；
它包含末端例外曲线，故允许极点商没有漏掉四条末端线。
对足够 \(k\)，
\[
Q_k=L_{j,B_j}(kE)/L_{j,B_j}
\]
有以 \(E\) 上可逆层为商的过滤，因而对 \(B_j\) 平坦。

随后使用 \(B_j\) 到所有 \(d\mid j\) 的特征零本原分支域之积的注入。
在每一分支，令 \(j=d\ell\)，把 \(M_j\) 识别为重复的 \(d\) 块，再以 Cayley–Hamilton 写成
\(C_j=I_d^\ell+\) 较低次的 \(I_d\) 多项式。
这给该分支上的 \(L_j\) 截面，不只处理 \(d=j\)。
平坦的 \(Q_k\) 使极点类可由全部这些分支检测为零，遂得到整个 \(S_{B_j}\) 上的截面。
该论证保留坏素数处相交分支的整数概形信息，不能由各闭点维数替代。

首项计算使用原矩阵的 \(x^{-1}\) 秩一幂等部分，得到
\((-\tau)^j q^{j(j-1)/2}\)，不先除非单位。
实际 \(x^{-j}\) 帧中的系数是单位，节点传播比也是单位且循环乘积 \(q^{-j}=1\)，
因而在整个八环处处生成 \(\mathscr N^j_{B_j}\)。
这是 C1 中最实质的对象特有步骤，不能删成“存在某个抬升”。

### 4.3 C1 的真实扩张、常数项和任意基变换

Ucoh Step1（105–125）实际计算每次吹起的常数层推前；
局部 \(\mathcal O(-1)\) 总空间／两图 Čech 计算和 Leray 给 \(R\Gamma(S,\mathcal O_S)=R\)。
因此常数 \(R\) 的身份不是只从秩一猜出的。

Step2（127–148）先写节点正规化差值复形，消去七个可逆对后得到
\([R\xrightarrow{1-q^{-j}}R]\)。
利用 \(1-q^{-j}=-q^{-j}(1-q^j)\)，推得未预设分裂的真实过滤
\(0\to T_{j-1}\to T_j\to B_j\to0\)，并得 \(H^0=R\)、\(H^{\ge2}=0\)。
这一步本身不允许宣布 \(T_j\) 为对角直和。

Step4（181–197）对整个 \(B_j\) 的真实 \(C_j\) 作 Bockstein，
产生被 \(1-q^j\) 杀死的 \(v_j\in T_j\)，其在边界商中的像是单位。
在 \(B_j\) 内乘该单位的逆便给实际分裂；
没有要求此单位在非局部 \(R\) 中存在单位提升，也没有只拿抽象有限阶向量代替边界生成元。

Step5（199–209）继续检查派生对象，而非从上同调同构直接宣布 (1)。
每个 \(R/(1-q^j)\) 有长度一自由分解，故
\(\operatorname{Ext}^2_R(T_n,R)=0\)；
截断三角的障碍消失，且保留来自真实常数层的映射。
Step6（211–223）以 proper、coherent、对 \(R\) 平坦为假设应用任意派生基变换；
底环 \(R\) Noetherian，不要求目标 \(A\) Noetherian。
本人直接核对了精确来源 Stacks Lemma 30.22.1／tag 07VK 的陈述和证明，支持这一量词。
C1d 是所得直接和的形式 Fitting 消费者，不另算一次几何发现。

### 4.4 C2：整模型不是逐域拼接，模长度不是截面余核维数

Gint Steps1–2（113–148）在同一个 DVR 光滑模型上构造原 \(I_r\)。
总空间正规；水平余维一处由原域上极除子保证整性，
唯一剩余纤维泛点落在原环面，原 Laurent 整系数排除额外垂直极点。
以向量丛／线丛的余维一延拓得到完整截面。
原约化 \(\bar I_r=J^N\) 与两侧已证无基点 pencil，
通过纤维检测及 Nakayama 给全模型生成；再用纤维平坦性判据得相对 pencil 平坦。
精确极除子保证 \(f_r^{-1}(\infty)=r\mathcal D\)，不是只给其支集。

Ucoh 固定 \(n=r\) 后沿 \(R\to\mathcal O\) 基变换：
\(j<r\) 的非零 \(1-s^j\) 给 torsion，\(j=r\) 的零微分给一个自由 \(H^1\)。
这已给同一模型的 C2c 分裂；Ssplit 的 DVR 另证保存为正确替代，不重复作为必要方法。
但 Ssplit 最后的圆分赋值绝不能因此删除：
仅 \(m\mid j\) 时 \(1-s^j\) 非单位，写 \(j=mk\)，由 \(v_p(k)=b\)
得阶 \(e/\varphi(p^{a-b})\)，该组恰有 \(\varphi(p^{a-b})\) 项。
各组长度 \(e\)，共 \(a\) 组；最少生成元总数 \(p^a-1\)；
乘积 \(\prod_{j=1}^{r-1}(1-s^j)=r\) 给 Fitting 理想。
这里 \(m\) 是 DVR 单位，故 \((r)=(p^a)\)。

Gint 的真实基识别／Step5（207–220）仍必要：
边界单位使原 \(1,I_r\) 是整基，而不只是某个秩二自由模有基。
在剩余小阶完整 \(f_m\) 上，\(f_{m*}\mathcal O=\mathcal O_{\mathbb P^1}\) 及投影公式给
\(1,J,\ldots,J^N\)；原基的实际像严格为 \(1,J^N\)。
这些身份不是仅凭 C1 的抽象模秩推出的。
有限能级的 \(N\) 倍重数由 \((J-h)^N\) 的 Cartier 纤维直接给出，包含坏能级。

### 4.5 C3：整除先于约化，完整理想先于零点集合

Ddiff Steps2–3（111–142）按原矩阵顺序对乘积作循环插入，
在特征零整数代数中先得到 \(dI_r=r[z^r]Q_r\)。
因为 \(r=mp^a\)，这首先证明 \(p^{-a}dI_r\) 整，
而不是在特征 \(p\) 中从 \(d(J^N)=0\) 反推一个“除后导数”。
约化时保留 \(m\) 个插入位置；求和成为 \(\operatorname{tr}(B^{N-1}dB)\)。
这里没有在剩余域取消零数 \(N\)，空乘积也覆盖 \(m=1\)。

Steps4–5（144–192）用秩二 Cayley–Hamilton 将它化为
\(U_{N-1}(S,D)dS-U_{N-2}(S,D)dD\)，其中相对状态微分下 \(dD=0\)。
Frobenius 分解与系数的唯一进位约束给 \(H_p^\sigma dJ\)；
低一位的次数界为 \(2p-2\)，只有数字 \(p-1\) 能进入目标系数，
故这不是略去混合项的猜测。
\(p=2\) 给 \(H=h\)，\(p=3\) 给 \(H=h^2-T\)；不使用在这些特征非法的除以 2、3。
这一全部迭代乘子的已知性按 Vlasenko 强扣除，见 §5；证明可正确而非新的一般结果。

Step6（194–204）以 \(J\) 的原首项 \(-T x^{-m}\) 及 \(p\nmid m\) 保证 \(dJ\ne0\)；
\(H_p\) 首一保证乘子非零，任意单位 \(t\) 不破坏结论。
也可从原 \(I_r\) 首项的微分看到除后 \(x^{-r-1}dx\) 系数为 \(m t^r\)，是单位。
因此准确公共阶为 \(ae\)，不仅是下界。

Gint Step6（222–240）将 \(\alpha\) 视为正规光滑总空间上局部自由微分层的有理截面：
水平余维一处可除 \(p\)，垂直泛点在环面上已有整性，故延拓到全部 \(\mathcal U\)。
两边约化后在稠密环面上一致，局部自由性使其在整个剩余曲面一致。
取系数理想得到的是理想像等式 (4)，不是抽象张量后自动注入，
也不是只说明 Hasse 根集相同。
D-R 所举小特征个别闭点可有更高赋值，与此“公共阶”没有矛盾。

### 4.6 实际泛 Jacobian：不能由谱曲线同亏格跳过

Wreuse V2 Steps1–2（70–146）先走纯谱路线。
此处区分 \(Z=z^r\) 的循环覆盖 \(C_{\rm sp}\to E\)：大谱曲线承载 J 的谱模，谱商 \(E\) 才是拟识别的椭圆曲线。
Bbad Step1 的原变换
\(u=\varepsilon TZ/\lambda,\ v=\varepsilon T^2/\lambda\)
给稠密开同构；Bbad Step3 检查完整三次族的唯一无穷远点光滑、
有限纤维整约化和总空间正则。
Bbad Step6 的双向概形消元使临界代数由首一四次
\[
(T-z^2)^2-\varepsilon Tz
\]
控制，且 \(c=\varepsilon-z-z^3/T\)，故临界概形在参数上有限，泛三次族几何光滑。
这只需有限性及消元的双向合法性；不先调用原临界长度四，
也不必为此出口再搬入乘 \(c\) 的完整四维矩阵或 Artin 块。
W 的原双图补齐端点，证明谱商 \(E\) 光滑且亏格一、大谱曲线 \(C_{\rm sp}\) 光滑及循环覆盖的固定端点。

V2 Step2a（148–161）是实际修正而非标签：
在任意原域 \(k_0\) 上基变换到 \(\bar k_0(c)\)，核定同一谱前提，
然后通过忠实平坦下降回 \(k_0(c)\)。
这里允许该扩张含不可分部分；没有偷换为原域已有点。

Jspec Steps2–7 必须完整保留：

- Step2（236–267）由实际谱代数作用在 \(\mathcal O^2\) 上构造谱模族；
  谱曲线光滑和非标量性质给局部循环向量，从而是真正的线丛族及 Picard 态射。
- Step3（269–288）用推前恢复常数共轭类，不把点上的特征线当成族。
- Step4（290–334）使用 \(M_{2r}=P,\ (M_{2r-1})_{12}=w,\ M_0=t^{r-1}A_0\)，
  从两个 \(12\) 元的比和 \(22\) 元有理恢复原 \(x,y\)；
  剩余对角共轭不改比值，所以函数域同构，包含不可分次数恰为一。
- Step5（336–384）原 \(A\) 给 \(L\dashrightarrow\sigma^*L\)，循环复合是乘 \(\lambda\)，不是恒等线性化。
  \(\operatorname{div}\lambda=3rP_0-2rQ_2-rQ_1\) 给固定差
  \(D_A=3P_0-2Q_2-Q_1\)，故差线丛落在不变 Picard 核。
- Step6（386–423）范数使拉回核含于可逆阶 \(r\) 的 étale torsion；
  全循环群固定的 \(P_0\) 杀掉几何核的字符，排除整个核；
  tame 平均及切空间一维再给不变单位分支恰为拉回 \(J_E\)，不是仅有一个同源关系。
- Step7（425 行起）proper 连通像是整个陪集，有理逆使原光滑射影曲线同构于该陪集；
  已在原域定义的作用忠实平坦下降为原曲线的 \(E\)-torsor，进而识别实际 Jacobian。
  并未假定全局原域有点。

剩余特征解释应用这些步骤时使用小阶 \(m\)，故 tame 平均合法。
以上链同时保留原矩阵、原坐标、谱模族、固定差、无核和原域身份，不能以同亏格替代。

### 4.7 原光滑闭能级：H.L(a) 的完整模型接口

Hloc Step2 的 L(a) 及实际前提核定（191–299）使用原参数局部环的普通 henselization，
保留剩余域；一般原域上要求真实的光滑 \(k_0\)-点。
选点通过 étale 坐标和 henselian 提升给局部截面，
不是先去严格 henselization 再无条件声称原域有点。

两侧总模型正则、proper、flat，唯一剩余纤维几何整且约化；
其作为主纤维自交为零，没有可收缩的纤维内 \((-1)\) 分量，故是相对最小正则模型。
指定 torsor 作用和提升截面固定泛同构，
由正亏格最小正则模型唯一性延伸为同底的完整模型同构。
这里区分最小正则模型与最小整 Weierstrass 方程；
本人直接核对 Stacks 55.10.1–2 的陈述和证明来复核延伸条件。

对几何闭域上的原光滑能级，非空光滑开集确可选点，
所以该接口充分把指定谱微分及 Hasse 零点解释运输到实际光滑能级的 Jacobian。
一般原域无点的情形不冒称原曲线本身已被有点同构平凡化。
\(H_p\) 的零点意味着光滑 Jacobian 超奇异；奇异三次曲线不冠以超奇异名称。
光滑能级上 \(\mathfrak c(dJ)\) 为单位理想，故 (4) 给 Hasse 零除子的拉回及 \(\sigma\) 重数。
这没有附加新动力、周期、点数或 H.L(c) 的全部旧出口。

## 5. 来源分层、定向亲读与强先例扣除

### 5.1 本人本轮直接阅读的一手入口

下表是本席自己的公开原文定向阅读，不把包内他人的 FULL 合并算为本人外文全文。
未做新的 Scholar／S2 全库查新或完整引文图；没有付费、绕过访问限制或向作者索取。

| 本人直接入口 | 本人实际范围与证据用途 | 未宣称的范围 |
|---|---|---|
| [Joshi–Roffelsen，作者 v2](https://arxiv.org/html/2508.18578v2#S3.SS1) | §3.1 全部：Theorem 3.1、Remarks 3.2–3.5、\(I_1\)–\(I_4\)、原矩阵／乘积／首项证明；扣除原对象、原积分及谱式 | 不是本席读完作者全文或出版全文 |
| [Wagner，q-Witt v5](https://arxiv.org/html/2410.23078v5) | 元数据、摘要，Introduction 1.1–1.9；核对 Jackson／q-Hodge 对角形、Bockstein 和相关函子性限制 | 不宣称全部正文及证明 FULL；1.9 不被夸大成禁止一切函子 |
| [Wagner，Habiro v2](https://arxiv.org/html/2510.04782v2) | Definition 1.6，Theorem 1.11 的可读文字尤其 (b)，Definition 1.12／Remark 1.13，Theorem 1.15／1.16 相关文字；核对过滤和底环条件 | 1.11(a) 的图未渲染，未宣称核对其图中各映射或全文证明 |
| [Gross–Hacking–Keel，作者 v5 PDF](https://paulhacking.github.io/mlp.pdf) | §1 起首及 Definition 1.1；Example 5.6、Construction 5.7、Remarks 5.8–5.9、Lemma 5.10／Corollary 5.11 及其相关证明 | 不是 PDF 全文、版面验收或整数坐标同构认证 |
| [Vlasenko，作者 v3](https://arxiv.org/html/1605.06440v3) | §1 的定义 (1)–(4)、Theorem 1(i)–(iii) 和半线性说明；核对 (i) 无 ordinary 假设 | 本席未在该外文中通读定理证明或 Lemma 7 |
| [Stacks Lemma 30.22.1，07VK](https://stacks.math.columbia.edu/tag/07VK) | 精确 lemma 的陈述及完整证明；任意目标代数的派生基变换 | 不冒称通读整章；07VJ 是节入口而非该精确 lemma |
| [Stacks 55.10.1–2，0C9Y](https://stacks.math.columbia.edu/tag/0C9Y) | 两项陈述及完整证明；最小正则模型的延伸与唯一性 | 不递归宣称所有引用引理均本人外文 FULL |

### 5.2 继承证据、已关闭子缺口和仍 OPEN 的范围

本人 FULL 读取 I-src1–4、I-A／B／CD／PF／PRE、Old／Pt 各来源和意见件、
Src-JR／OH／GRT／D。以下是这些记录的证据，不是本席重新取得每篇外文全文。

| 来源组或负面意见 | 实质保留与边界 |
|---|---|
| JR 出版接续及 JRV／JL | Src-JR／Src-D 已关闭出版后文的公开授权网页文本子缺口，出版 Conjecture 3.7 对应作者 v2 的 3.6，仍是猜想；不因本席未读出版全文重新标 OPEN。JRV 的精确旧定位及 JL 的八点／Picard 正文实读范围保留，后者不扩成全附录 |
| Ohyama、GRT11 | 真实全文仍 OPEN。可取得的目录、相关讲稿和稠密开变量对照不是目标论文全文；不据此全球排除更强同型整数结果 |
| Halphen、GHK、Friedman | 域上最小 pencil／周期与节点理论已有；GHK Example 5.6 是八个 \((-2)\) 分量、rootless 正交格的强近邻，不能略去；其复数底与本无关系整数坐标的精确同构未完成核定。Friedman 的相关约化解析底范围不能自动覆盖 \(B_j\) |
| q-Hodge／Habiro、Stacks 等 | 右侧复形形状和常用同调工具已有；Habiro 自有 q-Hodge 过滤与底环条件，既不能直接当作本曲面的几何识别，也不能宣称本曲面发现了它们 |
| Vlasenko、Koroteev–Smirnov／Smirnov 等来源链 | 按包内 KS／Smirnov 的准确来源身份保留首非零项、根单位特化及 Frobenius／Dwork 联系；不能说前人只有零阶。Vlasenko 的全部迭代乘子扣除见下 |
| 其他 q-difference／圆分背景 | Di Vizio–Hardouin 已处理非约化 q-curvature；Vargas-Montoya 的强 Frobenius 结构有自身前提，Bai–Lee 涉及圆分完成／关联分级。不能把这些不同系统和前提拼成直接包含全部原 \(mp^a\) 微分的定理，也不能宣称非约化／高阶问题无人研究 |
| 系数、半线性及递推工具 | Mellit–Vlasenko 常数项、Hesselholt–Madsen Witt ghost 微分、Pain 的 Dickson／Cayley–Hamilton 背景及 Achter–Howe 的 Cartier 半线性订正均作为既有工具扣除；特别不把 Hasse 系数与 Cartier 矩阵混同 |
| 近期近邻而非直接包含 | Bouis–Gazda 的 étale 整数底及反转判别式条件不保留本题全部坏素位；Franco–Hanson–Horn–Oliveira 的 integral nodal curve 是整曲线而非整数系数底；Schuler 的两分量 log/open 条件及 Alonso–Suris–Wei 的其他 pencil 表述不能只凭术语套入 C1–C3。Vlasenko 近期讲义线索按已有实读范围保留，不将目录升级为已核全部高阶定理 |
| Tsuda／QRT、Tate／Sutherland 等旧点模型来源 | 标准平移、Tate 型式及原点模型的旧先例完整扣除；不把旧位移点与循环出口重新计入 C1–C3 |
| P18／P29、P11 与组合意见 | 相关工具的项目内重复扣除保留；Pt-PF 中识别后的整个循环公式已被 P11 的有限群乘积／核计数包含。组合非碰撞只在实读接受源范围内成立，非 Papers1–29 全部全文或全球排除 |

KS 指 Koroteev–Smirnov；其根单位 quantum K-theory 归一化和 Smirnov 的特定 q-difference 系统不等于本原 qPI 状态微分，故保留强方法扣除而不声称直接复制了完整 C3。
既有 Scholar／S2 未成功、部分 arXiv 取得失败、一般整数 Halphen 分类及引文图未补齐等边界保持。
未检得直接同一定理不是“已证明无先例”；这些缺口主要限制新意排除强度，不是自动数学反例。

### 5.3 对完整 C1–C3 的逐项新意净额

| 候选部分 | 必须扣除 | 本席承认的准确剩余 |
|---|---|---|
| 原八点空间、原 Lax 积分、原谱式 | JR／既有 qPI 几何和域上 Halphen／周期背景 | 本题没有首次发明这些对象；它们是整数实现需要绑定的输入 |
| C1 的式 (1) 右侧形状 | Wagner 的 q-Hodge 对角模型已有 \(q^j-1\) 形；标准节点复形解释单个边界商 | 原曲面左侧 \(R\Gamma\) 与该形状的几何识别；整个非正规共振基上的原 \(C_j\) 截面、真实单位和实际扩张消失 |
| C1 的派生／基变换／Fitting | Bockstein、投射维数一、\(\operatorname{Ext}^2\)、Stacks 派生基变换、乘积 Fitting 均为标准工具 | 工具假设在原模型上真实满足、真实常数项保留；不另算新一般上同调方法 |
| C2 的退化和完整 torsion | \(\bar I_r=J^{p^a}\)、C1 特化、标准圆分赋值和 Smith／Fitting 算法强扣除 | 同一完整模型的无基点平坦 pencil、准确概形重数、原 \(1,I_r\) 基和实际特化像；不是另一套独立分裂发明 |
| C3 的 Hasse 迭代指数 | Vlasenko Theorem 1(i) 直接包含全部乘子，不需要 ordinary；首非零项研究的先例不能抹掉 | 原矩阵先整除后约化的微分桥、非零性、全开放模型延拓和准确系数理想，再接真实 Jacobian／闭能级 |
| C2–C3 的共同整数 \(ae\) | 同一 \(p^a\) 因子的赋值和上述标准长度消费者 | 有用的一致性识别，但未构造 torsion 与微分之间的典范模同构，不是第三种一般机制 |
| 旧实际 Jacobian／完整闭能级 | 谱模、Picard、最小模型、既有旧接受和标准理论 | 当前整数解释不可省的严肃对象身份桥；不把旧已接受的证明再次计为整数新发现 |

Vlasenko 的扣除不是泛泛“相似”：
取 \(F=\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3\)，Newton 多边形唯一内部格点为 \((1,1)\)，
其一维 higher Hasse–Witt 系数映到当前 \(U_{N-1}\) 的目标系数。
采用 \(T,h\mapsto T^p,h^p\) 的 Frobenius 提升，Theorem 1(i) 给当前全部 \(H_p^{1+p+\cdots+p^{a-1}}\)。
该对应不要求 \(H_p\) 可逆；需要可逆性的后续逆矩阵结论不能混到 (i)。
因此指数 \(\sigma\) 不能作为新的普通／超奇异一般定理。见 [Vlasenko，Theorem 1](https://arxiv.org/html/1605.06440v3)。

另一方面，GHK 的复数通用族不能凭名称直接推出这里的坏素数共振下降；
Wagner 的右侧同形也不能凭矩阵相同证明左侧来自这张原八截面曲面。
我没有将这两项强近邻夸大为已找到完整 C1 的直接重复。
当前剩余确实非零，尤其 Ssplit 的平坦极点商下降及 Ucoh 的真实 Bockstein 消扩张。

## 6. 各门完整理由

### 6.1 新意：7.3，FAIL

支持接近门槛的理由是：完整 \(R\)-模型上的全部 \(n\)、相交共振基上的原截面、
真实扩张和非常规基变换并非域上 \(h^i\) 表的形式抄写。
§4.2 的下降实际绕开非正规 Hartogs 陷阱，§4.3 没有把过滤当直和，
§4.4–4.7 把原基、完整模型及 Jacobian 身份保持到整数消费者。
这些是认真解决的对象特有数学问题，不应因使用标准工具而记为零新意。

但在强扣除后，本候选没有三个相互独立的发现：
C2 的模结构主要是 C1 的同模型特化，C3 的全部 Hasse 迭代乘子已有直接一般先例，
且原 Lax 及相关域上曲面／谱几何本已给定。
最强 C1 贡献是把已知边界复形和已知迹系数有效连接，得到一个漂亮的几何实现；
其全共振提升确有内容，但证明机制仍是平坦性检测、单位 Bockstein 与标准二阶扩张消失的具体组合。
C3 的先除后约化与模型延拓补上重要身份桥，却不改变已有 Hasse 递推的核心算术机制。

因此本席给“具有明显新结果、但扣除后新数学距离仍略低于本轮高新意线”的 7.3。
不是以“没新方法所以必失败”作一票否决，也不是因量词多而加分；
是把发现新对象、已有机制的新实例、以及非形式桥接分别计权后的总体判断。
仍 OPEN 的近邻全文使我不能把“目前未见完整重复”提升为很强的排除证据，
但即使这些缺口暂不作为额外负面，本席也不把已见净额评到 7.5。
这不是要求当前评审继续搜索到某个有利分数；本轮结论保持 FAIL。

### 6.2 独立科学价值：8.1，PASS

值得独立回答的统一问题是：
原 qPI 反典范族在整数共振时，哪些上同调类真正出现、它们怎样带 torsion，
原完整 pencil 怎样退化，以及失去可分性后的原状态微分留下什么完整几何信息。
C1 给一个可任意基变换使用的实物复形，
C2 识别抽象复形在同一原 pencil 上的真实像与重数，
C3 再说明首个整除后的微分及其光滑 Jacobian 解释。
这条问题线有内在依赖，不是把三个不相干算例装订起来。

独立价值尤其体现在区分传统域上讨论易混淆的四件事：
过滤与直和、特化余核维数与 DVR 长度、幂化 pencil 与最小 pencil、公共微分阶与逐闭点赋值。
保留坏素数 2、3、末端线和实际 Jacobian，使结果确有可复用的研究内容。
即使把全部标准工具和已知 Hasse 乘子清楚归还先例，
“同一原整数模型的完整可计算退化”仍值得一个完整数学叙述。

8.1 不是发表承诺，也不由篇幅或投入推断。
局限是尚无跨模型族定理、没有新的典范结构或独立应用被证成；
这些限制新意及外延，但不抹去本对象完整问题的科学价值。
不以缺少实验扣分：本合同是纯数学证明，数值不能替代上述结论。

### 6.3 完整证明信心：9.2，PASS

评分针对完整 C1–C3 及 §4 的全部必要链，不只是 D/G/S/U 新件。
决定性支持是四种潜在“看似形式、实则可能错误”的跳步都已实质处理：

- 共振整数环非正规：改用平坦允许极点商和所有本原分支，而非域上延拓硬套。
- 上同调有过滤不等于分裂：原 \(C_j\) 的真实 Bockstein 给有限阶单位提升，继而另证派生障碍消失。
- 约化 \(d(J^{p^a})=0\) 不能反推除后导数：原有序矩阵先整除，再保留插入位置并约化。
- 同亏格／同源不等于实际 Jacobian：有完整谱模族、有理逆、固定差、无核、原域 torsor 及闭模型延伸。

所有 \(n\ge0\)、\(a,m\ge1\)、\(p=2,3\)、单位 \(t\)、
任意非平坦／非约化／非 Noetherian 基变换的适用理由均有明确位置。
P／N 的末端图、S 的完整 \(E\)、Gint 的微分延拓、W V2 原域接口和 H.L(a) 点条件共同封住范围偷换。
未发现需缩小合同的新硬数学问题，故不给一个虚构“待补引理”作为保留条件。

未给更高分的原因是：证明链较长，若写成论文时把对象身份替换为摘要，
最容易丢掉上述非形式接口；本席不是形式化证明核验器。
外部定理仅按 §5 的实读／继承层级验证，没有声称逐个引用递归审完；
也未独立运行作者所述全部符号检查。
这些是信心边界，不是把运行成功或旧标签当作定理证明。
本报告没有新硬缺口，因而没有授权范围外的自行修稿或削减量词。

### 6.4 正文容量：可信 PASS

固定版式为匿名英文、单栏、11pt、letter、四边 1 inch、标准行距，
必要证明全部正文，参考文献另计。
下表按数学叙述任务、公式密度与必要证明结构预测，不由文件行数、文件数、工作时长或外部 PDF 页数推出。
没有试写、试排或实测。低／中／高不是严格界，也不新设“中值必须落窗”的门。

| 必要正文块 | 低 | 中 | 高 | 必须保留的具体内容 |
|---|---:|---:|---:|---|
| 统一问题、原矩阵规范、C1–C3 与强先例定位 | 1.4 | 1.8 | 2.2 | 完整量词、非典范边界及已有／新增区分 |
| 八中心、边界极除子、四末端图与法丛单位帧 | 3.4 | 4.1 | 4.9 | P／N 的真实坐标和全部末端检查，不只列八环 |
| 域上最小完整 pencil、Stein／不可分检查、有限几何纤维 | 2.4 | 3.0 | 3.6 | Gfield 及 Ffib 整数格／伴随的必要部分 |
| 整个共振基的原 \(C_j\) 延拓与单位边界 | 2.0 | 2.6 | 3.2 | 平坦极点商、所有 \(d\mid j\) 分支、真实首项与传播 |
| 常数上同调、节点复形、实际扩张及派生／任意基变换 | 2.2 | 2.8 | 3.4 | U 的非预设分裂、Bockstein、Ext、常数与量词 |
| 同一圆分模型的 pencil／实际像／全部初等因子 | 1.7 | 2.1 | 2.6 | Gint 的原基与平坦性，加 S 的完整圆分赋值 |
| 原整除微分、迹递推、Hasse 系数及非零阶 | 2.7 | 3.3 | 4.0 | D 的先除后约化、全部 \(a\)、特征 2／3 与 Cartier 规范 |
| 纯谱三次模型及有限临界代数的必要前提 | 1.5 | 1.9 | 2.3 | B 的双向消元和 W V2 双图／任意原域接口 |
| 实际泛 Jacobian 完整识别 | 4.5 | 5.5 | 6.6 | J 谱模族、常数共轭、有理逆／不可分、固定差、无核、原域 torsor |
| 原光滑闭能级完整模型与全开放微分／理想接口 | 1.1 | 1.4 | 1.8 | H.L(a) 提升与最小性、指定微分运输、四末端线延拓和理想像 |
| 合计 | 22.9 | 28.5 | 34.6 | 必要证明均在正文；参考文献不计 |

可信 PASS 的依据是一种具体而自然的组织：
原模型和单位帧只定义一次；C1 先完成通用分裂，
C2 直接消费这个同模型复形但独立证明原基／实际像；
纯 W 谱前提置于 J 之前，J 全链只证明一次，
H.L(a) 随后用于原闭能级；D 的系数证明与已有 Vlasenko 先例同时清楚交代。
这样约 26–30 页的完整正文是可信的，不需要删任何量词或必要证明。
这仍是结构预测，不是保证未来成稿恰为 28.5 页。

低于 22 页的风险在于极度紧凑叙述、外部标准工具引用密度或估计误差；
22.9 不是硬下界。
但若通过只写 Jacobian“标准”、省掉四末端线或把共振截面限到正规化分支来降页，
那不是本候选的合格低端写法，也不能用更短文件证明容量通过。
高于 30 页的风险真实存在：谱模族和有理逆逐项展开、四端图与原域下降的解释性细节、
以及所有小特征公式若均采用最高展开量，总量会到 34.6 页附近。
因此不能承诺任何合格写法都落窗；本门要求的是可信自然写法存在，而非强制整段预测区间入窗。

没有把旧正确替代证明重复计入必要正文：
S 的独立 DVR 分裂另证不与 U 特化双计；
旧强 T3 的完整乘 \(c\) 矩阵／Artin 长度与动力／全周期／点数出口不倒灌为 C1–C3。
但 B 的概形双向消元、S 的全共振下降和圆分赋值、
J 的完整实际识别及 H.L(a) 都已留出实质篇幅。
不通过拆篇、缩版、灌水、附录转移或试写测页取得 PASS。

## 7. 残余风险及禁止外推

本轮没有新硬数学问题。以下限制保留，不用未来工作给当前评分补票：

- 来源：Ohyama／GRT11 全文及一般整数 Halphen／引文图等仍 OPEN；JR 网页文本子缺口已经关闭，不倒退标记。
- 身份：不得从 q-Hodge 右侧同形推出新 q-Hodge／Habiro 结构或其过滤、乘法、函子性。
- 量词：C1 的 \(q,\tau\) 是单位；C2／C3 的 \(t\) 为单位。未证明非单位参数、另一整数紧化或任意奇异基的相同 pencil 结论。
- 特化：剩余精确阶是 \(m\)，不是 \(r\)；幂态射不是把剩余常数也作用一次的绝对 Frobenius。
- 微分：公共 \(ae\) 不是逐闭点赋值，理想像不是未经核定的张量注入，除因子不是饱和。
- 模结构：长度相等未给典范 torsion—微分同构，也未给跨 \(n\) 的统一兼容分裂。
- 几何：实际 Jacobian 不能用同亏格或任意同源替换；一般原域的闭模型平凡化保留光滑点前提。
- Hasse：只把光滑 Jacobian 的零点解释为超奇异；标量依赖指定微分规范，不当作无规范绝对数。
- 产物：数学信心及容量预测不是英文稿、编译、PDF 或发表验收；本件没有为创建项目、锁或投稿产生授权。

## 8. 本席最终处置

完整 C1–C3 是一个有价值且目前未见硬证明缺口的整数研究问题；
最强新增在原曲面全共振截面及真实上同调扩张的几何实现。
在强先例与项目内重复扣除后，本席新意为 7.3，低于 7.5。
独立价值 8.1、完整证明信心 9.2、自然 22–30 页容量可信 PASS 均不能抵消该失败。

本席四门合取：FAIL。
不改旧数学接受或旧 V1／V2 FAIL，不拆分 C1–C3，不降低合同，不改分追求与他席一致。
本报告提交后停止修改；后续若主控提出具体事实澄清，另按有界请求处理，不自行反复重评分。

## 9. 本人 FULL 与实际身份台账（55 件）

每件“1–N，本人 FULL”包含正文、正确旧替代段、管理记录及文件内已经写出的负面意见；
不表示自动打开文件外链。
表中行数按实际换行计，SHA-256 为本人对实际文件字节计算的值；
MATCH 表示与派发／manifest 身份一致，而非自动证明数学、来源全球覆盖或篇幅。
台账共三入口、十二作者、十二对应报告、六纠错接受、九整数来源意见、十三旧来源负面接续。

| ID | 实际输入文件 | 本人正文阅读范围 | 实际行数 | 实际 SHA-256 | 身份 |
|---|---|---|---:|---|---|
| BRIEF | [PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | 1–270，本人 FULL | 270 | 59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13 | MATCH |
| MAP | [PAPER30_QPI_INTEGRAL_CURRENT_PROOF_MAP_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_CURRENT_PROOF_MAP_V1_20260909.md) | 1–463，本人 FULL | 463 | 2be7d61d083c39d8268f212f0a0e0d3bed23ba40feb29469c920f146f715b0d1 | MATCH |
| MANIFEST | [PAPER30_QPI_INTEGRAL_REVIEW_INPUT_MANIFEST_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_REVIEW_INPUT_MANIFEST_V1_20260909.md) | 1–210，本人 FULL | 210 | 597ca2b5c6402ea93305d3ceade369b6cc373d9c84cfa73be0675e4c22ac3b6e | MATCH |
| P | [PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | 1–275，本人 FULL | 275 | 61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3 | MATCH |
| Nbd | [PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 1–284，本人 FULL | 284 | 8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469 | MATCH |
| Gfield | [PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 1–270，本人 FULL | 270 | 0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace | MATCH |
| Ffib | [PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 1–466，本人 FULL | 466 | 3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003 | MATCH |
| Jspec | [PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | 1–492，本人 FULL | 492 | a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f | MATCH |
| Bbad | [PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | 1–488，本人 FULL | 488 | 1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1 | MATCH |
| Wreuse | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md) | 1–213，本人 FULL | 213 | 21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2 | MATCH |
| Hloc | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md) | 1–637，本人 FULL | 637 | 0a6624550ed0f8765b51b01a1a481fd9a545d1791e10c3431effbf3f25428a3e | MATCH |
| Ddiff | [PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 1–268，本人 FULL | 268 | e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652 | MATCH |
| Gint | [PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 1–254，本人 FULL | 254 | 59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0 | MATCH |
| Ssplit | [PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md) | 1–418，本人 FULL | 418 | 2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac | MATCH |
| Ucoh | [PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | 1–255，本人 FULL | 255 | a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b | MATCH |
| P-R | [PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_NON_AUTHOR_REVIEW_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_NON_AUTHOR_REVIEW_V1_20260908.md) | 1–237，本人 FULL | 237 | edbf54720c0bd0624d8f6eb53d06db43965d66436b6b9a52ba67c4ef1b6f4dd0 | MATCH |
| N-R | [PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_NON_AUTHOR_REVIEW_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_NON_AUTHOR_REVIEW_V1_20260908.md) | 1–287，本人 FULL | 287 | 769c34ec3302e8f91bce13c86add8930f1ba032c5ec8a3490dcc49963af70597 | MATCH |
| Gf-R | [PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | 1–348，本人 FULL | 348 | 0964f6f0a6eb543402e0f2b2096fd5325d4eaf9912a7d8cd056b9d8193920972 | MATCH |
| F-R | [PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_NON_AUTHOR_REVIEW_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_NON_AUTHOR_REVIEW_V1_20260908.md) | 1–238，本人 FULL | 238 | 2b55ec53c0f677922eaf3d1f184c7066bd351ac5e5afd59f6d4a73f2b78f3bfb | MATCH |
| J-R | [PAPER30_QPI_LAX_JACOBIAN_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_LAX_JACOBIAN_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | 1–257，本人 FULL | 257 | c7d355d420e966381dfc74fffbd033470e12158480a826e0d88e464a5fa40438 | MATCH |
| B-R | [PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_NON_AUTHOR_REVIEW_V1_20260908.md) | 1–259，本人 FULL | 259 | 1bb3d563bdb5a2c93aa517002f69ac72398688ee74429a8b4d8662965c229815 | MATCH |
| W-R | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md) | 1–124，本人 FULL | 124 | 0db56630eab29ed89952f28dd2fd8038fa3c724040f99afbec527dd0e42c70f2 | MATCH |
| H-R | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_POINT_MODEL_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260909.md) | 1–413，本人 FULL | 413 | 10122ea2a617203dcf0ef7d9755ce0ae22ec7906c70ab141891998f94294093b | MATCH |
| D-R | [PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md) | 1–306，本人 FULL | 306 | 7c0ecd10991f80f0614713f344ab600a4eb69fd7356135fcfc927ed71a95d0bb | MATCH |
| Gi-R | [PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md) | 1–286，本人 FULL | 286 | ec49d4eaadbf4c0d53603cf6c902df375e2b1c779b6f243897521d786b206a0b | MATCH |
| Ss-R | [PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_CHECK_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_CHECK_V1_20260909.md) | 1–413，本人 FULL | 413 | ae768ae89301af115dc917e9a4b075b401258fb563628e1238b01844a30da941 | MATCH |
| U-R | [PAPER30_QPI_UNIVERSAL_COHOMOLOGY_CHECK_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_UNIVERSAL_COHOMOLOGY_CHECK_V1_20260909.md) | 1–284，本人 FULL | 284 | 9f54da405b8a40f58e34dc372fad7200452871171a92a0e0063edf1742e3cd55 | MATCH |
| W-old | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V1_20260908.md) | 1–196，本人 FULL | 196 | ec978801e842ce21a54ae7fd4982cd5b7fec449644c10cea49dc02b4b502eb16 | MATCH |
| W-old-R | [PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260908.md) | 1–242，本人 FULL | 242 | bb70f7c39c91d7b719f18c8358481c8ebe6bea009fe20718741ae4c8784b2949 | MATCH |
| DG | [PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md) | 1–173，本人 FULL | 173 | ed09aadb40752ed579bc45edb7b3531c1f78f6c7f7413072cd120315f2b22245 | MATCH |
| DD | [PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md) | 1–224，本人 FULL | 224 | 0bfbde8003d049d80523a2001d410dfa4f38ab2f14838d2dbbe4c1363f7155a7 | MATCH |
| DH | [PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md) | 1–87，本人 FULL | 87 | 40e4fa6460d34ebff7cfc0e20d614f3a2050590f10c58605819cba867e65dad7 | MATCH |
| DI | [PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md) | 1–162，本人 FULL | 162 | 1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af | MATCH |
| I-src1 | [PAPER30_QPI_CYCLOTOMIC_DEGENERATION_PRIOR_ART_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_CYCLOTOMIC_DEGENERATION_PRIOR_ART_V1_20260909.md) | 1–178，本人 FULL | 178 | 1c7ba39e3c2d6d661626e736b16f6d9a9599e0a8d07c0b2ead9e41f798da0cf8 | MATCH |
| I-src2 | [PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md) | 1–168，本人 FULL | 168 | 8d24144c5e49ba30402a2749536ec0b66ca6170d6dcf9a85273330829c22a88f | MATCH |
| I-src3 | [PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md) | 1–81，本人 FULL | 81 | 12628cbef7904732212424ee545451e709438d4d2a23909d6f2d3e69117ae6ad | MATCH |
| I-src4 | [PAPER30_QPI_INTEGRAL_COHOMOLOGY_PRIOR_ART_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_COHOMOLOGY_PRIOR_ART_V1_20260909.md) | 1–148，本人 FULL | 148 | 26e901d014f553773838f20b1b3ea46b607deffbcf9d73a503cab3ef24570450 | MATCH |
| I-A | [PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md) | 1–107，本人 FULL | 107 | bb463d1e1c27f543e4a0fe1bda17b584ffce28148e49ab1e1f3c3b1fce6b7ad5 | MATCH |
| I-B | [PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md) | 1–295，本人 FULL | 295 | 44f628fbc07cad422f83c136cf1dd3fb2bae9d7a7782db3798a073b5ab1bdf41 | MATCH |
| I-CD | [PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md) | 1–267，本人 FULL | 267 | d76e5e71001cd8033608a76673f61169f264caee57cb37aab4f86d1390dd8f02 | MATCH |
| I-PF | [PAPER30_QPI_INTEGRAL_PORTFOLIO_DELTA_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_PORTFOLIO_DELTA_V1_20260909.md) | 1–245，本人 FULL | 245 | a99af060d92829a6412f283ba2affb3dedab04a864d567a426de82ed98ca91f3 | MATCH |
| I-PRE | [PAPER30_QPI_INTEGRAL_PREFLIGHT_DISPOSITION_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_PREFLIGHT_DISPOSITION_V1_20260909.md) | 1–133，本人 FULL | 133 | 1ff8473c05956d88075dacc9705d79d621b2e9db059b59f5b13f06c72326641e | MATCH |
| Old-AB | [PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md) | 1–268，本人 FULL | 268 | 4470af64294525bc4ae33b9b00fc38c44c38215290a36fa6f3a5b6bdf861f90e | MATCH |
| Old-B | [PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md) | 1–112，本人 FULL | 112 | 2aae448ca17022aa7b51990b84058e57ee455ab0e4c0a4127d8e0ec7fc39c898 | MATCH |
| Old-CD | [PAPER30_QPI_NOVELTY_PHASE_CD_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NOVELTY_PHASE_CD_V1_20260908.md) | 1–247，本人 FULL | 247 | 8dadbaf066979a17ac87620ad5017e8e732c52ee81a68e4fc2ff545a249ecb82 | MATCH |
| Old-PF | [PAPER30_QPI_PORTFOLIO_NONCOLLISION_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_PORTFOLIO_NONCOLLISION_V1_20260908.md) | 1–258，本人 FULL | 258 | 5e89a61ab4386912d1cb2280ab4e314486ec8a3c9161585e5a26e302875065bc | MATCH |
| Pt-AB | [PAPER30_QPI_POINT_PERIOD_PRIOR_ART_SEARCH_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_POINT_PERIOD_PRIOR_ART_SEARCH_V1_20260908.md) | 1–321，本人 FULL | 321 | 75a1324e1fbefba2251f412435b4a76c180d9525dddb4b4f341c9c8344e1ccba | MATCH |
| Pt-CD | [PAPER30_QPI_POINT_PERIOD_NOVELTY_PHASE_CD_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_POINT_PERIOD_NOVELTY_PHASE_CD_V1_20260908.md) | 1–301，本人 FULL | 301 | 48bdccfe07f05fb669cce9d188908b9a16988488146023534d19209b774d1fa7 | MATCH |
| Pt-PF | [PAPER30_QPI_POINT_PERIOD_PORTFOLIO_DELTA_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_POINT_PERIOD_PORTFOLIO_DELTA_V1_20260908.md) | 1–243，本人 FULL | 243 | 7216525bf1226d4d0512eb7ca0e7b94a8573a4c18520e27afa6f0fefaa28c65d | MATCH |
| FAIL-V1 | [PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md) | 1–136，本人 FULL | 136 | 0452b7aa8f28107ae65f3fa840647806b50eab2502340d1c609a0ca6c545ce90 | MATCH |
| FAIL-V2 | [PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md) | 1–116，本人 FULL | 116 | fb490d26321a3077b839d1e3505979150b7ad02bf59c6f5beba93a9977003584 | MATCH |
| Src-JR | [PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md) | 1–98，本人 FULL | 98 | ab82c19d1bd6a182323b033f7d8c48e47de4e0839a9d5bebd2e4ead456ad4475 | MATCH |
| Src-OH | [PAPER30_QPI_OHYAMA_SOURCE_GAP_CHECK_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_OHYAMA_SOURCE_GAP_CHECK_V1_20260909.md) | 1–137，本人 FULL | 137 | 2cc3fa6636ff0bf878d54b5f32feb36755054a586dc1ba1f6e484dafdfd715e6 | MATCH |
| Src-GRT | [PAPER30_QPI_GRT11_SOURCE_GAP_CHECK_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_GRT11_SOURCE_GAP_CHECK_V1_20260909.md) | 1–133，本人 FULL | 133 | 67b27d4662f3f51a9552795676b5294e9eacd400d8ca1a38820a5a1b9c183356 | MATCH |
| Src-D | [PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md) | 1–73，本人 FULL | 73 | 34985ed628bfc2185f9674490f41766d6ce11a0d63da018962791d833d6d1c01 | MATCH |

台账结论：55 / 55 本人 FULL；55 / 55 实际行数与 SHA-256 MATCH。
本席没有读取另一席当前报告、旧正式评分报告或未获准的本地出链对象。
