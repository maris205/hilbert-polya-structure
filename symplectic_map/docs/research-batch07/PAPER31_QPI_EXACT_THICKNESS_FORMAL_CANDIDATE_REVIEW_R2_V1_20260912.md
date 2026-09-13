# Paper31 原固定 T 准确厚度完整候选：第二正式独立审查 V1

日期：2026-09-12 UTC（本席工具时钟）；评审席：/root/p31_exact_thickness_formal_v1_r2。
状态：FINAL_REVIEW；本次提交后冻结，不因另一席结论或事实澄清重新调分。
对象：共同冻结的 V1–V3 完整候选，不是仅评价新证明增量，也不是旧非单位时间候选。
route_applicability：NOT_APPLICABLE。score_calibration：NOT_CALIBRATED。

## 1. 结论、角色和不变门槛

本席完整合取为 **FAIL：目前不满足独立论文准入合同**。
这是对同一完整科学指纹的有效终态，不是数学否定，也不以缩小范围、追加票或改版面换取通过。

| 门 | 本席结论 | 原门槛 | 判断要点 |
|---|---:|---:|---|
| 新意 | 7.0/10，FAIL | ≥7.5 | 真实统一初始化尚有净增量，但方法几乎全部由强先例提供；最有特点的是唯一二阶节点例外 |
| 独立科学价值 | 7.3/10，FAIL | ≥7.5 | 原固定理想的未知标量已被实际求值，然而面向原项目之外的独立结论强度仍略不足 |
| 完整证明信心 | 9.1/10，PASS | ≥9 | 已读全部八份作者证明及必要旧原模型链；未发现尚未闭合的硬数学接口 |
| 自然完整实质正文容量 | PASS，超页风险高 | 22–30 页 | 低/中/高预测为 27.00/34.25/41.50 页；完整而统一的低端呈现可信，不把 central 在窗外自动判失败 |
| 四门合取 | FAIL | 四门同时 PASS | 前两门未过；不平均、不四舍五入、不与另一席拼门 |

我是本候选的 fresh 非作者正式审查席，不是 M/PF/FIX/G/C/PP/NODE/SYN 的作者，
不是既有数学独查、来源/CD、组合比较或 MAP 整理席，也没有在此任务前审过该候选。
我没有读取另一席的报告、评分、草稿或内部记录，没有与其通信，没有再委派评分或索取额外票。
共同来源呈现澄清记有读取进度；这不是另一席的科学意见或评分输入。
本包包含历史公开评价，因此本席不自称对历史分数盲审。

我本人完整读取 research-review 技能，并依其完整上下文、xhigh 和强反对意见要求执行；
指定 GPT-5.4 Codex MCP 在本会话不可用，实际工具检索没有该可调用入口。
因此执行的是任务已披露、已授权的可用 Codex xhigh 独立上下文 fallback。
没有 GPT-5.4 实际运行的 threadId，不声称跨模型复核、人类认证或形式化证明。
本任务的一次冻结四门审查、唯一报告文件和不互相校准要求，优先于技能的一般多轮对话及额外文件建议。
技能影响了证据与反对意见的组织，没有产生新实验、额外投票或范围扩张。

本席只新写本报告。没有改冻结原文、旧接受/失败、索引、项目、锁或论文；
没有试写英文正文、试排测页、编译、CAS、样本、GPU、外部写入或投稿动作。
公开原文读取、内存文字提取及内存页面渲染仅用于阅读，不落盘新科学材料。

## 2. 审查的完整主张，而非抽掉依赖后的短摘要

原对象始终是
\[
 F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
 h=-x+y+\frac{x}{y}-\frac{T}{x},\qquad T\ne0.
\]
使用原四簇 1+2+3+2 次吹起得到的 \(S_T\)，只删去原反典范八边形 \(D\)，
\(\mathcal U=S_T\setminus D\) 的四条完整末端线全部保留。
不能把分母不为零的环面替代这个完整原状态空间。

指定同基模型与标点为
\[
 W_h:\ v^2+huv-Tv=u^3-Tu^2,\quad O=[0:1:0],\quad P=(0,T),\quad t_O=-u/v,
\]
\[
 \phi(x,y)=\left(T/y,\;Tx(y-1)/y^2\right),\qquad \phi F_T=\tau_P\phi .
\]
取 \(z=h-h_*\)、\(i_n=(nP.O)_{h_*}\)、\(q=8h-9\)、\(H=32T+3h\)，并取
\[
 \delta=h^4-h^3-8Th^2+36Th+16T^2-27T,\quad
 s=h^2-4T,\quad b=2h^2-3h-8T .
\]
短式为 \(X=u+s/12,\ Y=v+(hu-T)/2,\ Y^2=f(X)=X^3+a_4X+a_6\)，
\(c_4=s^2+24hT,\ c_6=-s^3-36hTs-216T^2,\ a_4=-c_4/48,\ a_6=-c_6/864\)，
\(\Delta=T^3\delta\)。这里 q 不是 Tate 平滑参数，也不是域大小。
完整原 fixed-scheme 结论限定在特征 \(p>3\)；
其半稳定基 \(C^{\rm ss}=\mathbf A^1_h\)，仅当 \(T=-27/256\) 时删去尖点参数 \(h=9/8\)。
旧 FIX 已有 \(D_n=(nP)^*O\) 有限 Cartier 及
\(\mathcal I_{\operatorname{Fix}(F_T^n)}
=f_{\mathcal U}^*\mathcal I_{D_n}\operatorname{Fitt}_1\Omega^1_{\mathcal U/C^{\rm ss}}\)。
本次特征零范围仅为下述 V1 实际接触断言及 V3 有限阶节点边界，不外推全局固定理想或异常位置谱。

### 2.1 V1：forcing 与准确好接触

对 \(p>3\)，用
\[
 f(Z)^{(p-1)/2}=Z^pM(Z)+AZ^{p-1}+L(Z),\qquad \deg L<p-1
\]
定义实际 Hasse 系数 A 及 M、L。旧输入已经给出
\[
 \lambda=-q\,dh/\delta,\quad
 \mu(P)=\frac T2M(s/12)+(b/2q)^p-A(b/2q),\quad
 N_p=q^p\mu(P)=\tfrac12\{Tq^pM(s/12)+b^p-Abq^{p-1}\}.
\]
旧 M 已证明 \(j\notin k(h)^p\)、该 \(N_p\) 非零、次数至多 \(2p\)、必要支持及正特征好点 q=0 的素于 p 切触排除。
不能把这些再次计入本次发现。

新 G/C 给出特征零原归一化的
\[
 \mathcal L\int_O^P\frac{dX}{2Y}=-\frac H{q\delta},\qquad
 \mathcal L=\partial_h^2+\left(\frac{\delta'}{\delta}-\frac8q\right)\partial_h+
 \frac{8h^3-18h^2+9h-12T}{q\delta},
\]
以及独立正特征系数证明
\[
 \mu(P)'=-AH/q^2,\qquad N_p'=-q^{p-2}AH.
\]
在代数闭特征零，或代数闭特征 \(p>3\) 且 \(p\nmid n\) 时，每个实际有限好切触 \(i_n>1\)
有 \(q_*\ne0\) 且 \(i_n=2+\mathbf1_{H_*=0}\)。
原 \(t_O(nP)\) 的首项分别是 \(-nH_*z^2/(2q_*\delta_*)\) 和 \(-nz^3/(2q_*\delta_*)\)。
每个好 Hasse 零点的 A 阶为 \(1+\mathbf1_{q_*=0}\)；
在 \(q\delta\ne0\) 的每个 \(N_p\) 根，根阶为 \(1+\operatorname{ord}A+\mathbf1_{H_*=0}\le3\)。
这没有证明所有几何根都对应实际切触，也没有证明三阶好切触必定出现。

### 2.2 V2：所有素域好点的初始值与所有迭代

仅在 \(T\in\mathbf F_p^\times,\ h_*\in\mathbf F_p,\ \delta_*\ne0,\ p>3\) 的准确范围内，
令 \(d=\operatorname{ord}P(h_*)\) 是实际闭纤维有限群点阶，则
\[
 e_*=\begin{cases}0&A_*\ne0,\\1+\mathbf1_{q_*=0}&A_*=0,\end{cases}\qquad
 c_*=\begin{cases}
 1+\mathbf1_{q_*=0}&p\mid d,\\
 1&p\nmid d,\ N_p(h_*)\ne0,\\
 2+\mathbf1_{H_*=0}&p\nmid d,\ N_p(h_*)=0.
 \end{cases}
\]
这些是实际 \(e_*=\operatorname{ord}A,\ c_*=i_d\)，不再是未知交数的更名。
全部 \(n\ge1\) 的结论为
\[
 i_n=0\quad(d\nmid n),\qquad
 i_n=p^a c_*+e_*\frac{p^a-1}{p-1}\quad(d\mid n,\ a=v_p(n/d)).
\]
全好纤维形式邻域的原固定理想为 \((z^{i_n})\)；\(i_n=0\) 表示单位理想。
新 PP 补的是旧 prime-to-p 支持判据未供应的 p-primary 初始化，保留 \(p=5,d=10\)；
上式传播是已知低 Hasse 阶公式，原完整理想形状也是旧 FIX，均不得另外计功。
闭群点阶 d 仍作为有限代数输入是实质诚实的，并非隐藏交数；
但这不是全素数点阶闭式，也不向扩域好点外推。

### 2.3 V3：一般代数闭正特征的所有有限节点

对任意代数闭 \(k,\operatorname{char}k=p>3,T\in k^\times\)，每个有限节点由
\[
 T=w^3(w-1),\quad h_*=w(3-2w),\quad w\ne0,1,3/4
\]
描述。取
\[
 (w-1)\zeta^2+(2w-1)\zeta+(w-1)=0
\]
的任一互反根。写 \(n=p^am,\ p\nmid m\)，则
\[
 i_n=\begin{cases}
 0&\zeta^m\ne1,\\
 2p^a&\zeta^m=1,\ p>5,\ (T,h_*)=(3/16,-2),\\
 p^a&\zeta^m=1,\ (T,h_*)\ne(3/16,-2).
 \end{cases}
\]
有限阶 d 的原参数首项为 \(d(2w+1)z/[w(4w-3)^3]\)；
唯一例外的首项为 \(-3dz^2/3125\)。
特征五该例外是尖点，未漏掉一个合法节点。
一般 k 下 \(\zeta\) 可以不是根单位，此时所有 \(i_n=0\)；
而例外在 \(p>5\) 时确在有限域代数闭包中，确实实现有限阶二阶接触。
特征零的同一计算只断言有限阶节点回返均横截；
唯一二阶候选要求 \(\zeta+\zeta^{-1}=-4/3\)，与根单位的代数整数性不相容。

在原节点完成坐标 \(z=\xi\eta\) 下，旧 FIX 的完整理想被准确求值为
\[
 \widehat{\mathcal I}_{\operatorname{Fix}(F_T^n)}
 =z^{i_n}(\xi,\eta)\subset k[[\xi,\eta]].
\]
无回返时只有约化孤立节点；正厚度时另有长度一嵌入部分。
这两种概形结构都不是本轮新发现。\(H=w(2w+1)(4w-3)^2\) 说明三项同源，
但不构成第四个创新或一般退化定理。
尖点只从半稳定理想陈述的域删去，不从原曲面删去；无穷、T=0 和尖点固定理想仍未被声称。

## 3. 最强先例扣除与新意门

历史公开 CD 的完整意见是 6.8/10、PROCEED_WITH_CAUTION，三项方法 LOW、finding MEDIUM。
理由不是没有定理，而是强先例扣除之后，剩下经典带点正常形的精确专门切片计算；
节点二阶例外最清楚，仍未显示新一般机制。该意见及来源缺口均已进入本包。
本席不把 6.8 作为起始分、上限、下限或待校准目标；以下 7.0 是自己的完整候选判断。

| 先例或旧成果 | 本席实际扣除 | 尚存、但不自动高分的部分 |
|---|---|---|
| GMX Theorem 3、§2.2；CCRS §§2.1–2.2 | 原曲线就是 \(E(b,c)\)，\(b=T,c=1-h,(0,0)=-P\)；正常形、加法及固定 N 挠条件算法已知 | 固定 b 的整条切片的统一准确交数，不等同于某个固定 N 方程 |
| Voloch 1990 Theorem 6.1 | \(M\equiv a\delta\mu\bmod p,\ a\in K^\times\) 的一般导数桥已知 | 原规范的显式乘子与 Hasse/分歧点阶的实际求值；非零函数域乘子不自动是闭点单位 |
| UV §§2–3、Propositions 4.7、4.11、§4.12 | 下降、Igusa 兼容速度、complex-Betti 准确读阶、完整移动端点及三阶实例已知 | 原 forcing 和正特征局部控制的具体结果 |
| Broumas Theorem 4.1、§4.1、§4.6 | Frobenius 扭曲上的水平导数同态与规范已知 | 固定原切片的速度阶及 p-primary 初始阶 |
| Naskręcki Lemma 8.2 | 全部倍数公式直接属于低 Hasse 阶标准传播 | \(c_*,e_*\) 不再未知；不能用“所有 n”重复扩大贡献 |
| Tate 整数级数、乘法同态；形式隐函数 | 一般节点工具、乘法群、p 幂传播均已知 | 固定 T 的原 h 无分歧、唯一一阶消失和非零二阶值 |
| 旧 M/PF/FIX、P30 原几何与群接口 | 同一 \(N_p\)、素域支持充要性、完整理想、q=0 旧排除及非挠性均扣除 | 旧结构式的未知标量现在实际算出 |
| P18/P29/P11 | 完整 fixed equalizer、幂零、Fitting/基变换，以及有限群循环消费者都不是首次 | 这些实际所读定理并未供应本 qPI 截面的基方向准确初始交数 |

上述外部扣除分别由规定原文支持：
[GMX](https://arxiv.org/pdf/1004.5511)、
[CCRS](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/66737ACC99BC2D4F70EE3A2D38FF1EB6/S1461157014000072a.pdf/computation-on-elliptic-curves-with-complex-multiplication.pdf)、
[Voloch 1990](https://www.numdam.org/article/CM_1990__74_3_247_0.pdf)、
[UV 规定 HTML](https://arxiv.org/html/2508.06680v1)、
[Broumas](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/95814903A024FCB1B2C13CA8778759DA/S0010437X97000365a.pdf/effective-p-descent.pdf)、
[Naskręcki](https://nyjm.albany.edu/j/2016/22-46v.pdf) 与
[Tate](https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf)。
不从这些论文的标题、摘要或报告转述推定全部包含或全部不包含。

GMX 的共同图表给 \(h_L=-T/(1-h)^2,\ a_L=((1-h)^2+1-h-T)/(1-h)^2\)。
因此固定 T 通常移动两个 Lyness 参数：固定 Lyness 参数的结论不能直接覆盖该方向。
但方向不同不产生新椭圆模型，c=0、小阶及除掉的图表边界也不能消失。
UV 中实际相切的挠叶正是相关准确读阶的消费者；把“最优”改叫“指定”不能回避先例。

| 指纹 | 方法新意 | finding 新意 | 本席分析 |
|---|---|---|---|
| V1 | LOW | MEDIUM | 独立正特征系数恒等式与 supersingular 低阶控制有内容；char 0 的 forcing 及随后读阶不是两项方法突破 |
| V2 | LOW | MEDIUM | prime-field 的完整初始化确实补齐旧未知量，包括 p-primary；但 Igusa 速度后低于 p 的积分及标准传播不构成新一般下降理论 |
| V3 | LOW | MEDIUM | 唯一二阶节点及特征零/正特征差别是最可复述的发现；证明仍是带点 Tate 正规化和二阶 Taylor 求值 |

最强反对意见不是“都是代入所以零新意”，而是：
对一个已经完整辨认的通用带点正常形，先例已提供接触、导数、Igusa 与传播的组织框架，
余下的准确系数和唯一例外，虽然可靠且非空，尚不足以把完整候选提升到此合同的 7.5 新意线。
统一解掉旧 \(i_d\) 的意义可使它明显高于纯重述；但凝聚、计算量和公式数量不能消除专门化程度。
所以本席给 7.0/10，FAIL，不借未取得原文的空白提高分数。

## 4. 独立科学价值门

这个候选有明确的数学用处：过去知道完整固定理想应是怎样的，却仍必须输入未知的基方向交数；
现在在全部素域好点及一般代数闭正特征的全部有限节点，初始值可以直接由闭纤维代数数据取出。
特别是 p-primary 分支及确实发生的节点二阶例外，不是重复旧支持集合。
同一 \(W_h,P,T,z\) 被持续使用，三项不是跨系统拼接；这是真实的单一研究问题。
P30 的垂直临界理想和其原 Hasse 根阶输入，不是本原 fixed equalizer 的全厚度答案；
P18/P29 有完整幂零也不构成本次具体交数的直接包含。

然而，对于不了解本项目的读者，主要独立产出仍是一个特定参数方向的准确初始化表。
统一结果的深度来自把多个经典局部机制在同一模型中妥善对齐，而不是新的一般交数原理、
新的广泛可迁移不变量或由这份初始化推出的另一项实质定理。
节点例外提供良好的记忆点与算术差别；它还不足以独自承担全部独立价值门槛。
V1 给实际好切触的条件阶，而非全部位置或三阶实现；V2 的充分性依赖素域；
这些是现有结果影响范围的事实，不是我新增的“先解扩域/尖点/旧 I03 全部谱”的强制义务。
保留 d 为闭群输入不算偷换，也不因此把该结论扩成全局点阶分类。

旧 I03 提过问题不是已解决问题；反过来，本候选解决了明确的部分也不表示 I03 全部关闭。
我认可它作为有价值、完整的专门结果，而对这份完整结果现在是否够独立成文给 7.3/10，FAIL。
这不是以篇幅过长惩罚价值，也不是因为需要第五篇而调高或调低分数。
本报告不提出一个删分支的替代候选，不给“写短一点即可过门”的建议。

## 5. 完整证明信心：实际依赖、关键风险和本席检查

以下检查针对完整链和真正有风险的消费者；既有接受记录仅说明当前状态，
没有被当作 formal 证明门的自动 PASS，也没有因为制作本审查而自动撤销未变数学接受。

| 必要模块及责任 | 本席核查到的闭合证据 | 不能省略或偷换的点 |
|---|---|---|
| P302 原曲面/能量；F 有限纤维 | 四末端图、完整八边形极点与无基点；proper/flat、泛光滑；整数正交格和伴随公式把有限纤维限制为单个重数一分量 | 不是从仿射三次式反定义曲面；有限纤维整、约化及四条完整末端线必须在正文 |
| R 原映射/非挠；P302 相应原 Picard 数据 | 补齐末端原点及 \(x=y\) 状态，正反无曲线收缩；实际 Picard 拉回的幂给整数二次次数增长 | Picard 格不是模 p 后的线性代数；每个允许 T 和特征都需泛非挠，不可用样本 |
| P303、FIX 同基模型 | W 唯一无穷点光滑，有限纤维整，临界点处 \(F_h=uv\ne0\) 使总空间正则；直接 +P 恒等式及正则最小 proper 模型唯一性延拓 | 延拓先覆盖整个有限基，包括后续理想陈述删掉的尖点；不以有限点集双射代替模型同构 |
| FIX 广义作用与全理想 | 半稳定、几何整纤维、光滑 O 满足广义椭圆条件；好点 torsor equalizer；节点作用 \(\xi\mapsto\xi U,\eta\mapsto\eta U^{-1}\)，\(U-1=t\cdot\mathrm{unit}\) | 两个生成元及两包含、忠实平坦完成下降、Fitting 拼合都在；仅切表示不够 |
| M 实际 Manin 输入 | j 无穷极点阶八排除 p 次幂；原公式；q=0 极点与例外尖点多项式取值分别证明非零；局部消去与旧支持 | 尖点取值只证明多项式非零，不是把坏纤维当椭圆曲线使用 \(\mu\) |
| PF 素域充要性 | 返回局部一次系数在 \(\mathbf F_p\)，残值式保留 \(1-A_*\)；\(A_*=1\) 时有限群/函数极点次数证明非零字符及小核，排除 P 落核 | \(A_*=1\) 不能直接反演；Hasse 界与 p=5 的 5/10 两种阶均保留；没有扩域外推 |
| G 特征零与正特征独立证明 | 两个 Gauss–Manin 多项式恒等式、组合 primitive 的 O 极点消去和移动 P 端点；独立系数恒等式推出 \(\mu'\)、\(N_p'\) | \(Y(P)\) 常数不使移动端点项消失；不能把解析 forcing 直接模 p 化代替系数证明 |
| C 真正好接触及 Hasse 阶 | A/C 同时消失会给椭圆函数的 p 次根只有一阶极点，违背 Riemann–Roch；普通与 supersingular 两种局部主项分别控制 i | 先由估计使 \(i<p\)，再读非零系数；否则导数看不见的 p 次幂会使读阶循环 |
| PP p-primary 初始化 | 真正有限 étale \(\ker V\) 提升及 4 阶标记；由生成元固定兼容 \(\alpha^{p-1}=A\)；原模型权重、Frobenius 扭曲水平对数导数和 V 的 étale 比较 | 不是任取 A 的根；不是把相对微分拉回当成基微分；移动平移保持在正确下降结构中 |
| NODE 所有节点 | 整数 Tate 级数、指定 \(-P\) 的带点变换；固定 T 的隐函数；一阶消失的唯一因子、二阶非零、原 h 无分歧与 O 参数比较 | 无分歧是实算，不借任意基变换；既核 \(\zeta\) 非根单位，也核 p=5 变成尖点 |
| SYN 所有倍数与原理想消费者 | 原微分 Cartier 系数与形式 [p] 的 \(t^p\) 系数均为 A；整系数尾项；\(e_*\le2<p\) 给严格主项比较；代入既有全理想 | generic ordinary 不等于闭纤维处处 ordinary；不是只证第一 p 层或只代入支持集合 |

几处尤其影响 9 分门的具体核对如下。

1. 旧有限纤维证明不是仅有数值等价：正交格是实际整数格，
   其二次型给 \(p_a(C)=1-4(u-v)^2\ge0\)，故 \(u=v\)；
   再由正系数与 r=1 的总纤维关系迫使唯一重数一分量，CM 排除嵌入部分。
   原 Picard 幂的增长如 \((16m^2+2m+1,16m^2)\) 是整数次数，不随模 p 消失。
2. FIX 的节点 UFD 因子分解由保持 \(\xi\eta\) 的真实形式作用产生，
   \(U-1=t\cdot\mathrm{unit}\) 用了特殊纤维乘法群的非零无穷小作用。
   代入 \(t=a_n(z)\) 后才得到 \(z^{i_n}(\xi,\eta)\)，故长度一嵌入部分也有完整理想依据。
3. G 的系数关系给 \(A'=\alpha A+\beta C,\ \beta=-q/\delta\)，
   此处 \(C=[X^{p-2}]f(X)^{(p-1)/2}\) 是辅助系数，不是作者文件 ID；
   好 q=0 处 \(\beta'= -8/\delta\ne0\) 与 \(C_*\ne0\) 给 Hasse 二阶，而非笼统说“通常简单”。
4. C 在普通点先有 \(\operatorname{ord}\mu(nP)\ge i-1\)，在 supersingular 点先有 \(\ge i\)；
   \(\mu'=-AH/q^2\) 的低阶把 i 压到 2 或 3 后，
   supersingular 主系数中的 \(1-i\) 才确认非零。此顺序真正排除了不可见 p 次项。
5. PP 的 \(\lambda=\alpha^{p-2}dX'(Q_0)/(2Y'(Q_0))\) 与 Broumas 的 \(A/c\) 规范一致；
   以实际 \(\ker V\) 生成元定根并在原微分下核权重后，才把 \(\operatorname{ord}\lambda=0/1\)
   积分为 1/2 阶。阶小于 p 使未知 p 次常量不能抢先。p=5、d=10 使用 \(2P\) 没有遗漏。
6. NODE 的 \(T_0'=(\zeta-1)^3(\zeta^2+\zeta+1)^2/(\zeta+1)^9\)
   和固定 T 下 \(h'\) 都为单位；一阶零因子为 \(3\zeta^2+4\zeta+3\)。
   其上二阶计算含 \(-125/81\ne0\)（p>5），不是只列出一阶可能消失点。
   Tate 乘法同态与 O 附近 \(-X/Y=(V-1)\cdot\mathrm{unit}\) 足够，不消费未读满射证明。
7. SYN 的尾项均至少 \(t^{2p}\)。对 \(\operatorname{ord}t=b\ge1\)，
   \(e_*+pb<2pb\) 保证 A 主项不被抵消；故闭 supersingular 点仍由同一递推覆盖。

本席在已读完整链中未找到应报告的硬反例、错误量词或缺失引理。
主要剩余风险是长串显式恒等式、规范符号与写成英文后的转录，
以及仅有限范围原文核对所能保证的来源归属；这不是形式证明助手已认证。
因此给 9.1/10，PASS，而不是 10，也不是“数学先前接受所以自动 9”。

必要原模型及非挠证明保留，但实际消费者不要求一般 r 的 normal-bundle 阶、
未使用的谱 Jacobian/Weil 点选择/有限点集自治共轭/循环计数全链。
这些不计正文的原因是本固定 T、r=1 证明不消费它们，并非为页窗另造短证明。
同理，不计旧 F5 样本、可选数值例子或新跨族应用来凑容量。

## 6. 自然正文容量门：模块预测而非试排

标准严格采用匿名英文、普通单栏 11pt article、letter、四边 1 inch、普通行段间距。
摘要/引言/结论和全部题目特有必要证明都计正文，参考文献另起页另计。
下面按实际证明负担估计，不由源代码行数、文件数、旧 PDF 页数或投入工时换算。
低/中/高表示同一全部内容的三种自然说明密度，不是三种不同科学范围。

| 必要实质模块 | 低 | 中 | 高 | 页数负担来源 |
|---|---:|---:|---:|---|
| 问题定位、主断言、统一记号、边界及收束 | 2.00 | 2.50 | 3.00 | 需解释原厚度问题和限定域，不复述整个项目历史 |
| 原吹起曲面、四末端、极点/无基点、proper/flat/泛光滑 | 2.50 | 3.25 | 4.00 | 四图合列但保留验证与极点传播 |
| 整数正交格、伴随与有限纤维整约化 | 1.00 | 1.50 | 2.00 | r=1 消费的完整论证 |
| 原回返的全状态延拓、Picard 拉回及非挠性 | 2.50 | 3.00 | 3.75 | 真正末端检查、整数矩阵和幂增长 |
| W 的正则最小模型、指定 \(\phi,+P\)、广义椭圆结构 | 1.50 | 2.00 | 2.50 | 不能只写 birational identity |
| 全 good/node fixed equalizer、完成下降与嵌入部分 | 2.00 | 2.50 | 3.00 | 节点两包含及单位系数论证 |
| M 原规范、j 条件、非零多项式与局部消去 | 2.00 | 2.50 | 3.00 | 含例外 T 和旧 q=0 支持接口 |
| PF 素域两方向、字符/有限群与小特征分支 | 2.00 | 2.50 | 3.00 | 不能删去 \(A_*=1\) 困难分支 |
| G 两 Gauss–Manin 恒等式、完整端点及独立模 p 系数证明 | 3.00 | 3.75 | 4.50 | char 0 与 char p 证明不能互相代替 |
| C 普通/supersingular、Hasse 1/2 阶、真接触 2/3 阶 | 2.00 | 2.75 | 3.25 | 非循环低阶比较及各边界 |
| PP 实际 Igusa 提升、规范、水平导数与低阶积分 | 2.25 | 2.75 | 3.25 | 含兼容根与 p=5,d=10 |
| NODE 整数 Tate、固定 T 隐函数、一/二阶值及原参数比较 | 3.25 | 4.00 | 4.75 | 含所有节点域、非根单位和 char 0 边界 |
| SYN 原形式 Hasse、全倍数严格比较、已求理想总结 | 1.00 | 1.25 | 1.50 | 不重复证明经典一般传播理论 |
| 合计 | 27.00 | 34.25 | 41.50 | 同一完整 V1–V3 及全部必要旧证明 |

我的容量结论为 PASS，但不是低风险或实际 PDF 验收。
27–30 页的完整自然呈现有可信路径：一套记号和主表只定义一次，
四末端用同一个表给出而仍证明极点与延拓；Gauss–Manin、M/C/PP 共用已证明的同一规范，
全倍数与理想消费者各出现一次，而不是每个作者模块都重铺背景和再述一遍主结论。
这些是正常数学写作的消除重复，不是压字号、把必要证明换成“直接可得”、移附录或缩量词。
本席认为表中低端仍容得下每一个列明证明；没有把“只写新结论约二十页”当低端。

短端风险：若只剩 22 页附近甚至以下，最可疑的是删掉原模型/Picard、PF 的异常分支、
PP 的规范或 NODE 的二阶项，而不是内容自然不够；那些删法不符合本表。
所以本席不预测“极易写成 22 页”，也不以补应用或背景填满下限。
长端风险更显著：若把八份局部文本各自的设置、引理和来源解释逐段保留，
自然会到 34–42 页；尤其完整原模型约占 6–10 页，不能把它隐藏成一个旧结果引用。
本合同没有 central 必须在窗内的附加门槛，所以 34.25 本身不导致 FAIL；
但低端可信也绝不保证未来排版一定达标。Paper30 的 40 页例外在这里完全不用。
若未来实际完整正文超 30 页，不能拿本预测作为压版、删必要证明或扩页的权限。

## 7. 实际本地阅读与冻结核验账

下列全部范围由我本人读取，SHA 绑定整个文件而非节选。
21 份 FULL、14 份规定 PARTIAL 均完成；所有整文件行数、字节和 SHA 与 manifest 实际核验一致。
首次合并输出中 manifest 后段及 SA 小段有截断，分别续读 manifest 120–202 与 SA 90–145 补齐；
未把被截断的输出当 FULL。BRIEF/MAP 的之后复看属于同件重定位，不增输入身份。
表内 ID 以共同 manifest 的文件身份定义；以下提供实际路径链接，使报告不依赖会话才能定位。

| 入口/共同输入 | 本人范围；行数/字节 | 实际 SHA-256 |
|---|---|---|
| [AGENTS](../../AGENTS.md) | FULL 1–28；28/2766 | 73ff82bcf298285ef8c3b6a4d3e1dff80eedb7eeda93ea47a55334c862c43412 |
| [WORKFLOW](../WORKFLOW.md) | FULL 1–39；39/4901 | b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2 |
| research-review 技能，/root/autodl-tmp/.codex/skills/research-review/SKILL.md | FULL 1–106；106/4501 | 62859ebaa64be9915546b0ba8fb3464110bcfe015307fc33b15c97f03dc392a5 |
| [共同 manifest](PAPER31_QPI_EXACT_THICKNESS_REVIEW_INPUT_MANIFEST_V1_20260912.md) | FULL 1–202；202/24736 | cf58bbe0dc9cb66c550fb413aeac9088c2b9727f9d341155719dd67c6185027d |
| [UV 共同呈现澄清](PAPER31_QPI_EXACT_THICKNESS_UV_PRESENTATION_CLARIFICATION_V1_20260912.md) | FULL 1–42；42/2848；后续同样向两席开放的呈现记录，非新科学输入 | 9ebc81c392117f709660243d995507b2a4cb1cec8a9da2996ce7ff85722aa47c |

| FULL 输入 | 本人完整行段；总字节 | 实际 SHA-256 |
|---|---|---|
| [BRIEF](PAPER31_QPI_EXACT_THICKNESS_CANDIDATE_BRIEF_V1_20260912.md) | 1–360；24719 | 1d00acccbd1056f361ac2736cbe9c035c965a566167bf6f8b9efdc4da1ba01dd |
| [MAP](PAPER31_QPI_EXACT_THICKNESS_CURRENT_PROOF_MAP_V1_20260912.md) | 1–280；28884 | a1a4daf2dfb6f9b771f7724aa805af3e568242313f4043ae951ad474e65b4ae6 |
| [A](PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_A_V1_20260912.md) | 1–157；9522 | 171e8aa602d6431e76672c79cf6962c9269f73a6f91993ef7c131a697a4ac917 |
| [B](PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_B_V1_20260912.md) | 1–241；21119 | efa6763b9246b526a4b27fccc102afabcc382173b4fb0797de5a302410be1832 |
| [CD](PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_CD_V1_20260912.md) | 1–219；17998 | 3ad2744925bd44308a28f7c7a4486160e59130ace63bbf07061791e1a78e8f96 |
| [PORT](PAPER31_QPI_EXACT_THICKNESS_PORTFOLIO_DELTA_V1_20260912.md) | 1–180；17592 | 3c15b22b2ea418c28fd35c3d205be48fec6332fa057991aae058c1829351b5ba |
| [PRE](PAPER31_QPI_EXACT_THICKNESS_PREFLIGHT_DISPOSITION_V1_20260912.md) | 1–162；13252 | 003c9206ba5aee80f7cd1e8a9d9ae7e9a951fe5b06eab46fe7f2cafe4959b0a3 |
| [M](PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md) | 1–446；17913 | 48029bd31748637edaa6a9a123cd0d525406ea5b65f7eab53799606a5c97dbe2 |
| [PF](PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md) | 1–325；15155 | de9cdb5ee8fef26b50365e6794e148f7206c4c167738143fc28e77159b0debef |
| [FIX](PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md) | 1–348；20304 | 401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7 |
| [G](PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md) | 1–267；10608 | c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b |
| [C](PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md) | 1–281；12318 | 7ec721bfac1d43f214dc9c8b3906c8bab131fe53b67fd6c48e06eeaa752f27aa |
| [PP](PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md) | 1–254；11442 | 38805df5657731f6698b3fcc3356269cb02da2e2c952779b5750ec6fe8442449 |
| [NODE](PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md) | 1–346；16230 | 5b61cbc732fbd70d6edd1979d183d50081ea1cac3d849164422447c5c785cf27 |
| [SYN](PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md) | 1–245；10241 | 5400ed2775b3a91f85c814d9c8c8fb252dc91cf8577579f63da0cee87e7539d1 |
| [MA](PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md) | 1–148；9653 | 05a99ecd5cfd72315b8c4e0fc740062687824d4dcd8dc7cdcdb81f5f87bbb8fd |
| [OLD](PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md) | 1–176；11013 | 8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a |
| [MATH](PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md) | 1–234；13710 | 5340f77faa1354b1239240e3d7ba7068ae32e752e6d4550e32b2f243ea08bc99 |
| [SA](PAPER31_QPI_MANIN_CONTACT_ORDER_SOURCE_AUDIT_V1_20260912.md) | 1–192；12549 | 17b7f3175ce52b53c03a3c0540cadb00b59b5067205818a822a1c8d15b2502ed |
| [SI](PAPER31_QPI_EXACT_THICKNESS_SOURCE_INCREMENT_V1_20260912.md) | 1–169；14016 | 762643a7bed0a1d54fa074a823d28054811c26373441fc9d7e49e04cb508ded1 |
| [FP](PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md) | 1–167；11126 | 9a70cd2dd9656689dfeb26a6890e35ab1bf5dd10a5eab28a38306578b2767fce |

以下 PARTIAL 是规定段落读完，不声称全文；总行数/字节供整文件身份核验，不作容量依据。

| PARTIAL 输入 | 本人实际范围；总行数/字节 | 实际 SHA-256 |
|---|---|---|
| [P302](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex) | 1–226、388–415、432–437；446/20456 | 573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f |
| [P303](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex) | 1–111；438/19219 | 38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f |
| [F](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 7–26、66–92、128–245、362–389；466/22170 | 3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003 |
| [R](PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md) | 1–70、107–318；368/16747 | 9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c |
| [S](PAPER30_QPI_SINGULAR_CUBIC_GROUP_ENTRY_V1_20260908.md) | 182–288、594–619；683/28658 | 64cb688c586c8a82123c998dd23275539935fd3baed9c9e0f38d98c814f2dce7 |
| [P30I](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex) | 1–170；300/13903 | 9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e |
| [P30H](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/04-closed-hasse.tex) | 1–48、147–183；271/12079 | 68efcc6780280d7e06c107bc993fe4c431d8131b59f1f4f9e6b874dd96c6000e |
| [P30F](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/06-first-layer.tex) | 340–393；397/16400 | e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392 |
| [P18](../../papers/18-marked-henon-scalar-boundary/paper/main.tex) | 188–251、373–408、442–461、488–505、507–616、1055–1152、1228–1293、1470–1487；1602/69588 | 65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d |
| [P29O](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/2_orbit_algebras.tex) | 13–31、167–236；236/10354 | a36bebf59d412cc72ba52b38eb38da5f65cda0d0e79500642a7599004cb9520f |
| [P29P](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/5_periodic_detection.tex) | 80–166；166/7130 | 862d363763a2a0dc3491903539ff0f5b0c75df7c8aed56f4c5af9d10eb4e21a8 |
| [P29E](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/6_effective_periods.tex) | 111–168；353/13822 | fccfef37b05fafaff300a2f9a84f4796ca2ef902f365133c5069f459c89c271e |
| [P11](../../papers/11-cat-equivariant-clock/paper/manuscript.tex) | 390–518；1238/56201 | 2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958 |
| [IDEA](PAPER30_QPI_POSTV2_IDEATION_V1_20260909.md) | 130–170、290–310；339/27288 | e10bd508ff98acd6ed25fc01f05ccdace2f6efeab173d5aadb1fa6f2e7068aca |

## 8. 一手外文实读、视觉补足与未覆盖来源

本节每项均为 PARTIAL_REQUIRED_RANGE_COMPLETE，即规定范围本人读完，不自称整篇 FULL。
不是继承 B/CD/SA/SI 的外文阅读身份；以下内容是在本席任务中实际获得。

| 原件 | 本席实际范围与方法 | 与判断有关的核准 |
|---|---|---|
| [UV 规定 HTML](https://arxiv.org/html/2508.06680v1) | §§2–3 完整，§4.1–4.12 完整；另从原 HTML 读取 S2.E4、S4.E1 两个 table 至闭合标签的全部 inline SVG/MathML/TeX 源码 | 下降/消去、兼容 Igusa、准确读阶、完整端点和全部三个例子；图中标记箭头从 HTML 原图源补齐，不声称 HTML 渲染视觉验收 |
| [V90](https://www.numdam.org/article/CM_1990__74_3_247_0.pdf) | 印刷 257–258、§6；全文提取加本人实际看 p.257 原扫描图 | Theorem 6.1 与完整短证明，函数域非零乘子而非闭点常数单位 |
| [N16](https://nyjm.albany.edu/j/2016/22-46v.pdf) | 印刷 1003–1005 全文，PDF 文本；p.1004 另在内存渲染并实际视觉核式 | Lemma 8.2 两种 Hasse 阶分支及全证明；本候选只消费低阶分支 |
| [GMX](https://arxiv.org/pdf/1004.5511) | PDF 1–10 全文，分两次提取；Theorem 3、§2.2、§3.1 节点部分都读到 | 同一带点正常形、Lyness 参数方向及奇异分式动力学；不漏小阶/图表边界 |
| [CCRS](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/66737ACC99BC2D4F70EE3A2D38FF1EB6/S1461157014000072a.pdf/computation-on-elliptic-curves-with-complex-multiplication.pdf) | 印刷 509–513 全文，§§2.1–2.2 完整；页码初次误从 PDF 第2页起，随后补第1页509；初次输出还附带514页 | 正常形与固定 N 多项式及 Möbius 分解已知；附带514图表不用于新判断 |
| [TATE](https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf) | PDF 1–7 全文，整数级数、Theorem 1 的同态/核证明 | 没有读后段满射证明；当前 NODE 不依赖该未读部分 |
| [MIN](https://stacks.math.columbia.edu/tag/0C9Y) | Lemmas 55.10.1–2 的陈述和证明 | 正则 proper 模型、正亏格及相对最小性假设得到明确核对 |
| [NODAL](https://stacks.math.columbia.edu/tag/0CBY) | Lemma 53.21.1 陈述和第一证明；网页另自动显示第二证明 | étale 标准节点坐标及完成的来历；不能代替 FIX 全理想证明 |
| [CON](https://math.stanford.edu/~conrad/papers/kmpaper.pdf) | 印刷4–6全文；因 Remark 2.1.13 跨页，另读第7页开头该 remark 余段，提取顺带显示紧邻收缩定义开头 | 广义椭圆定义、标准一边形作用、Fitting 奇点理想以及不可约纤维/光滑截面保证唯一结构 |
| [B97](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/95814903A024FCB1B2C13CA8778759DA/S0010437X97000365a.pdf/effective-p-descent.pdf) | §4 开头、Theorem 4.1/证明、§4.1 全部；式30–31、§4.6 全部；PDF130–131、135–136定向全文，并视觉核 p.131/136 | 水平导数同态、cgal 兼容根、\(\omega_q\) 与模型变换的 \(u^{-2}\) 权、p>3 边界；不依首页 OCR 的 p>5 改范围 |

V90 使用 manifest 已给的未编辑阅读副本：
/tmp/p31-phasecd-source-iLAVGS/voloch1990.pdf，
SHA bb806b122429b3249b269202d9a04280fb0fb42d691d939098d38827b75c4cc2；
p.257 图 /tmp/p31-phasecd-source-iLAVGS/voloch1990-p257.png，
SHA 317b728e7d6859dcede36796b333cd1b875811a5bf761dbe9202cd1aa88fa6b3。
两哈希由本人核对，实际图由本人看过；不继承前人的看图身份。

实际技术失败及处置：

- CCRS 的网页工具打开原 PDF 返回 400/Timeout；同一公开 URL 经普通读取恢复，未换论文或绕过认证。
- B97/N16 网页截图工具返回“非 application/pdf/截图未启用”，没有取得图片；
  随后仅对同一公开原件做内存渲染，实际看到 B97 131/136 及 N16 1004。
  B97 OCR 有符号缺失，视觉确认式31中 \(-2x^2\) 及尺度 \(u^{-2}\)，未靠乱码定规范。
- UV 网页提取对图(2.4)、(4.1)空白。我最初还读取了同编号 PDF 的相关文字并实际看 PDF 第7/11页，
  后按两席共同呈现澄清，另本人核准该 PDF 首页内文为 August 12, 2025，
  而规定 HTML 内文是 August 24, 2026，页头 v1 提交仍是 August 8, 2025。
  PDF 旁读不算 HTML 的视觉补足，不用来补科学论证，也不宣称两呈现逐页或全文等价。
  最终补齐方式是本人读完规定 HTML 两张原 SVG 表：共同覆盖的 \(\pi_1,\pi_2\) 图，
  以及 \(\mathbb Z^2\)、\(\Gamma\ltimes\mathbb Z^2\) 商、同构、开嵌入和垂直投影图。
  没有全版本差分、臆造新版或借呈现差异改变候选。

Duistermaat 相关全文未取得，Scholar/Semantic Scholar 入口失败及其它覆盖缺口按 B/CD 继续保留；
它们是来源阶段的真实缺口，不伪称本席新尝试成功或失败。
Ulmer1991/勘误、Ulmer–Urzúa、Hone、Voloch2026 等十项以外资料只有冻结来源报告的覆盖信息，
本席没有把其正文认领为本人实读，亦未以摘要排除直接包含。
本席没有新增广泛搜索次数或宣称穷尽查新；目前给分承认未读固定 Tate 切片文献的直接包含风险。
十项规定范围的实际阅读已完成，当前无必须扩包才能评本候选的科学输入缺口。
未发现“来源未取得”应被转化为新意优势的理由。

## 9. 冻结交付判断

这是同一完整 V1–V3 的第一次正式四门评价中的本席完整一票：
\[
 \underbrace{\mathrm{FAIL}}_{\text{新意 }7.0<7.5}\ \land\
 \underbrace{\mathrm{FAIL}}_{\text{价值 }7.3<7.5}\ \land\
 \underbrace{\mathrm{PASS}}_{\text{证明 }9.1\ge9}\ \land\
 \underbrace{\mathrm{PASS}}_{\text{容量}}\ =\ \mathrm{FAIL}.
\]
合取要求四个门都满足；前两门已经使准入失败。
未过不抹去数学发现和既有接受，也不要求再做数学投票。
核心保留意见是：经典带点正常形上统一而准确的初始化，尚未跨过本合同的独立新意和科学价值线。
本席不建议因已投入工作或第五篇需求放宽阈值，不建议另找票替代，也不以这份容量预测授权建稿。
报告提交后冻结并停止编辑；行数、字节与最终 SHA 在交付消息中给出，不作文件自哈希。
