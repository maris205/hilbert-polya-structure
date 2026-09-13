# P32 内部研究：实际对称接口、可见商空间与显式 35 点插值

记录日期：2026-09-09 UTC。持续主控研究的 P32 第一份限定笔记。
本篇承接[层留数与对称核][shell]、[压力偶对称][even]及
[首个 theta 修正][quartic]；只新增本文件，不改旧笔记、正式稿或状态。

预先限定主张：证明真实几何对称如何传到字符压力，分离两种核障碍，
给有限完整层的精确秩证书，并在明确条件类中给出恰好 35 点的插值。
不宣称实际 D 的系数独立，不替换实际压力 P，不提供稳定误差或条件数；
有限噪声与观测误差属于另一个研究单元。所有新增公式均为纸面推导。

## 1. 实际输入与继承结论

[既定几何输入][geometry]是固定、带标记、曲率负一的闭双曲亏格二曲面，
使用单位速度测地流和整数同调基。全部有向本原 owner 保持原口径，
反向不合并，原覆盖时钟及归一化不变。这里不另选高对称曲面。

沿用

\[
\mathsf Q=2\pi^2D>0,\quad q(x)=x^{\mathsf T}\mathsf Qx,\quad
P(x)=s_4(2\pi x),\quad \dim\mathcal P_4=35.
\tag{1}
\]

\(\mathcal P_4\) 是四变量实齐次四次多项式空间。考察其中测试方向，
不表示可以自由修改真实压力函数。已有

\[
W_R(\lambda)=\sum_{q(k)=\lambda}R(k),\qquad
\mathcal N_q=\bigcap_{\lambda\in\mathcal E}\ker W_\lambda,
\quad \mathcal E=\{q(k):k\in\mathbb Z^4\setminus\{0\}\}.
\tag{2}
\]

其中 \(W_\lambda:R\mapsto W_R(\lambda)\) 是线性泛函。
每个层有限。[层留数笔记 §2][shell]已证完整辅助轮廓恰检测
\(\mathcal P_4/\mathcal N_q\)。[解析余项笔记 §5][analytic]支持
\(\operatorname{Res}_{a=-\lambda}\mathscr A_R=W_R(\lambda)\)：
这里是去掉三次对数后的单值亚纯正则部分，不混称原轮廓总是单值亚纯。

当前读取的压力论证认证了 \(s(-\theta)=s(\theta)\)，没有给实际
曲面等距在固定同调基上的矩阵清单，也没有给具体 \(D\) 的精确系数。
整体变号对所有四次齐次多项式本来就作用为恒等，因此这项偶性本身
不把 35 维空间缩小。下文的新几何群输入均明确列为条件。

## 2. 从真实同调作用到字符作用：须取转置

假设 \(f\) 是同一个固定曲面的已认证等距，其在既定整数同调基上的
作用为 \(A_f\in GL_4(\mathbb Z)\)，即
\(\alpha_{f(g)}=A_f\alpha_g\)。令 \(S_f=A_f^{\mathsf T}\)。则

\[
e^{i\theta^{\mathsf T}\alpha_{f(g)}}
=e^{i(S_f\theta)^{\mathsf T}\alpha_g}.
\tag{3}
\]

这里采用字符拉回约定；若改用左作用可写 \(A_f^{-\mathsf T}\)，
对整个几何群所得的矩阵集合及不变空间相同。

等距的微分与单位速度测地流交换，保持周期并置换有向本原轨道。
因此在 Euler 产品的绝对收敛域中，逐轨道重标记给
\(L(v,S_f\theta)=L(v,\theta)\)。这里没有对轨道另取对称商。
沿用[压力笔记 §2][even]的唯一近临界极点输入并缩小共同字符邻域，
亚纯延拓唯一性与极点唯一性推出

\[
s(S_f\theta)=s(\theta),\qquad
S_f^{\mathsf T}\mathsf Q S_f=\mathsf Q,\qquad
P\circ S_f=P.
\tag{4}
\]

所以真实几何字符群的像 \(G=\{A_f^{\mathsf T}\}\) 满足

\[
G\le H:=\mathcal H_q
=\{S\in GL_4(\mathbb Z):S^{\mathsf T}\mathsf QS=\mathsf Q\},
\qquad P\in\mathcal P_4^G.
\tag{5}
\]

群 \(H\) 有限，理由已在[层留数笔记 §3][shell]逐列证明。
定义群平均 \(\Pi_HR=|H|^{-1}\sum_{S\in H}R\circ S\)。已有
\(W_{\Pi_HR}=W_R\) 及 \(\ker\Pi_H\subseteq\mathcal N_q\)。
保持 Hessian 的整数矩阵可能不是曲面等距诱导矩阵，故不能反向由
\(S\in H\) 宣称真实 \(P\circ S=P\)。

## 3. 对称限制下的两个独立核条件

置 \(U=\mathcal P_4^G\)、\(V=\mathcal P_4^H\)，有 \(V\subseteq U\)。

**命题 1。** 有代数直和

\[
U\cap\mathcal N_q
=(U\cap\ker\Pi_H)\oplus(V\cap\mathcal N_q).
\tag{6}
\]

证明：若 \(R\in U\cap\mathcal N_q\)，则
\(R=(R-\Pi_HR)+\Pi_HR\)。平均项在 \(V\cap\mathcal N_q\)，
差项在 \(U\cap\ker\Pi_H\)。反向包含来自平均保持每个层泛函，
且平均的像与核交为零。这里不要求 \(G\) 在 \(H\) 中正规，也没有
断言 \(\Pi_H\) 在单项式系数的 Euclidean 范数下正交。□

因此全部 \(G\)-不变四次方向均可识别，即
\(U\cap\mathcal N_q=0\)，当且仅当以下两项同时成立：

1. \(U=V\)：已知几何对称排除 Hessian 额外等距造成的不可见方向；
2. \(V\cap\mathcal N_q=0\)：不变四次方向之间不再逐层抵消。

第一项的必要性：\(\Pi_H:U\to V\) 满射；若其核为零，有限维数相等，
结合 \(V\subseteq U\) 得 \(U=V\)。其余方向由 (6) 立即得到。

本轮交叉审读澄清：若额外认证的先验将待恢复对象限制在 V，则不必
要求整个 U=V；在这个缩小后的允许类中，第二项即为可识别性条件。
若候选仍允许取遍 U，仅指出单个真实 \(P=\Pi_HP\) 不够：对任何
非零 \(K\in U\cap\ker\Pi_H\)，\(P+K\) 仍属于 U 且与 P 的全部
层观测相同。排除它必须把 \(R=\Pi_HR\) 作为所有允许候选 R 的
已认证约束，而不只是关于真实解的一句陈述。此处澄清的是恢复允许类，
不改变核分解 (6) 或对全部 U 的两条件判准。

在全空间上同样有

\[
\mathcal N_q=\ker\Pi_H\oplus(V\cap\mathcal N_q),\qquad
\mathcal N_q=\ker\Pi_H\iff V\cap\mathcal N_q=0.
\tag{7}
\]

找全 \(H\) 只给平均算子，不能跳过 (7) 右侧的独立检验。
此外 \(U/(U\cap\mathcal N_q)\cong V/(V\cap\mathcal N_q)\)，
同构由 \(\Pi_H\) 诱导；这是可见商类相同，不是原多项式相同。

## 4. 完整有限层的精确秩证书

令 \(d=\dim V\)，固定一组基 \(e_1,\ldots,e_d\)。

**命题 2。** \(V\cap\mathcal N_q=0\) 当且仅当存在 d 个不同层，
使以下方阵可逆：

\[
C_{j\alpha}=\sum_{q(k)=\lambda_j}e_\alpha(k),
\qquad 1\le j,\alpha\le d.
\tag{8}
\]

证明：全部层泛函在 \(V^*\) 中的张成空间，其零化子就是
\(V\cap\mathcal N_q\)。零化子为零恰使张成空间等于 \(V^*\)，
可从这些泛函选出 d 个基向量；反向由方阵可逆直接成立。□

这里必须求和完整层，不能把某层的已枚举部分当作该行。一个更强、
较易解释的充分证书是：选 d 个格点 \(k_j\)，每个完整层恰为
\(Hk_j\)，而评价矩阵 \((e_\alpha(k_j))\) 可逆。此时
\(C_{j\alpha}=|Hk_j|e_\alpha(k_j)\)，故可逆。单轨道条件并非必要；
多个群轨道碰在同层时，仍可能满足 (8)。

也可对 U 直接使用同一完整层满秩判准，判定真实 G-不变方向是否
全可识别。若通过，它已经同时排除了命题 1 的两项障碍。
本篇不重复伪逆、最小奇异值或噪声误差界，也不声称已找到实际层集。

## 5. 非球形反例：已证偶性不够

固定代数测试

\[
q_{\rm test}=x_1^2+2x_2^2+3x_3^2+5x_4^2,
\quad G_{\rm test}=\{\pm I\},\quad R=x_1^3x_2.
\tag{9}
\]

有 \(R\ne0\)、\(R\in\mathcal P_4^{G_{\rm test}}\)。翻转第一坐标
保持该 q 并使 R 变号，每个有限层因此精确配对抵消，全部层总权重为零。
这不是由浮点误差或积分尾项猜测的零。

甚至对固定实 \(\varepsilon\ne0\)，局部函数

\[
s_{\rm test}(\theta)=1-\frac{q_{\rm test}(\theta)}{4\pi^2}
+\frac{\varepsilon\theta_1^3\theta_2}{(2\pi)^4}
\tag{10}
\]

仍偶、实解析、具有相应负定 Hessian，且在足够小邻域有严格二次下降；
其四次项满足 \(s_4(2\pi x)=\varepsilon R(x)\)。所以仅这些局部压力
性质不能推出可识别性。没有证明 (10) 可实现为曲面压力，不能把该测试
当作实际曲面的反例。这里也不借 \(K=0\) 推断整个轮廓恒零。

## 6. 有理独立的条件类及其对称限制

**命题 3（条件类）。** 假设正定 \(\mathsf Q\) 的十个自然独立坐标
\(\mathsf Q_{ii}\ (1\le i\le4)\)、\(\mathsf Q_{ij}\ (i<j)\)
在有理数域上线性无关，则

\[
q(k)=q(l),\quad k,l\in\mathbb Z^4\setminus\{0\}
\quad\Longrightarrow\quad l=\pm k.
\tag{11}
\]

证明：值相等给

\[
\sum_i(k_i^2-l_i^2)\mathsf Q_{ii}
+2\sum_{i<j}(k_ik_j-l_il_j)\mathsf Q_{ij}=0.
\tag{12}
\]

系数是整数，所以独立性迫使 \(kk^{\mathsf T}=ll^{\mathsf T}\)。
取 \(k_j\ne0\)，先由对角项得 \(l_j=\epsilon k_j\)，其中
\(\epsilon=\pm1\)；再由第 j 列得 \(l_i=\epsilon k_i\) 对全部 i 成立。
若改用二次多项式的十个系数 \((\mathsf Q_{ii},2\mathsf Q_{ij})\)，
有理独立条件等价，因为只乘了非零有理因子。□

这个充分条件与 (11) 已在[层留数笔记 §4][shell]出现；本篇复写证明
是为固定坐标含义，不能把它再算新结果。下一节的显式最小点集才是新增。

**新推论。** 在 (11) 下 \(H=\{\pm I\}\)。证明：若 \(S\in H\)，
则 \(Se_i=\epsilon_i e_i\)。再将 (11) 用于 \(e_i+e_j\)，得到
\(\epsilon_i=\epsilon_j\)，故所有符号相同。
所以若实际几何已认证某个字符矩阵 \(S\ne\pm I\)，该 Q 就不可能
满足本节有理独立条件。没有额外矩阵的记录也不反向认证独立性。

## 7. 恰好 35 个显式格点及齐次 Lagrange 公式

取以下固定点集，而不从旧 69 点集合中再搜索行子集：

\[
\mathcal T=\{\alpha\in\mathbb Z_{\ge0}^4:|\alpha|=4\}.
\tag{13}
\]

它由下列向量的全部不同坐标排列组成：
\((4,0,0,0)\) 的 4 个、\((3,1,0,0)\) 的 12 个、
\((2,2,0,0)\) 的 6 个、\((2,1,1,0)\) 的 12 个，
以及 \((1,1,1,1)\) 的 1 个，共 35 个。

令 \(S(x)=x_1+x_2+x_3+x_4\)、\(\alpha!=\prod_i\alpha_i!\)，定义

\[
\Phi_\alpha(x)=\frac1{\alpha!}
\prod_{i=1}^4\prod_{j=0}^{\alpha_i-1}
\left(x_i-\frac j4S(x)\right),\qquad \alpha\in\mathcal T,
\tag{14}
\]

空乘积为 1。每个 \(\Phi_\alpha\) 都是齐次四次多项式。

**命题 4（本轮新增）。** 对任意 \(R\in\mathcal P_4\)，有

\[
\Phi_\alpha(\beta)=\delta_{\alpha\beta}
\quad(\alpha,\beta\in\mathcal T),\qquad
R(x)=\sum_{\alpha\in\mathcal T}R(\alpha)\Phi_\alpha(x).
\tag{15}
\]

证明：在节点 \(\beta\) 上 \(S(\beta)=4\)，故 (14) 的值为
\(\prod_i\binom{\beta_i}{\alpha_i}\)。若 \(\alpha\ne\beta\)，
两者总和相等，必有某个 \(\beta_i<\alpha_i\)；相应下降阶乘含零因子。
若二者相等，则每个因子组除以阶乘都为 1。因而 35 个
\(\Phi_\alpha\) 线性无关；空间维数也是 35，所以它们构成基，
评价直接给出每个展开系数为 \(R(\alpha)\)。□

在 (11) 下，节点各属不同的 \(\pm\alpha\) 层，且四次齐次性给
\(W_R(q(\alpha))=2R(\alpha)\)。于是有明确的 35 层重构

\[
\boxed{R(x)=\frac12\sum_{\alpha\in\mathcal T}
W_R(q(\alpha))\Phi_\alpha(x),\qquad \mathcal N_q=\{0\}.}
\tag{16}
\]

实际上 (16) 只要求这 35 个节点的完整层分别为 \(\{\pm\alpha\}\)，
不要求其他层均非共振。这是一个更弱的有限条件，仍未给实际 Q 认证。
对全部 35 维四次方向，少于 35 个标量线性观测不可能单射，故此点数
在无额外约束的精确线性恢复问题中最小；不包含最优条件数的主张。

若节点层发生碰撞或含其他格点，不能把其留数当作 \(2R(\alpha)\)。
此时应回到第 4 节的完整层矩阵，不能删除同层格点来保住插值公式。

## 8. 实际接口、证据限度与下一单元

一个可证伪的条件路线是：先取得实际 \(A_f\) 及其字符转置群 G；
若其不变实对称二次型空间恰一维，选其中正定 \(Q_0\)，则 (4) 迫使
实际 \(\mathsf Q=cQ_0\)、\(c>0\)。正倍缩放不改变整数等距群或层的
格点划分，只改变层标签。随后仍须分别检验 U=V 和有限完整层满秩，
不能从二次型形状受限直接断言四次压力可识别。

当前最小缺口是实际对称矩阵、其不变空间，以及实际完整层的精确认证。
本篇没有为实际 D/P 加入任何有理独立、非共振或额外压力对称假设；
也没有证明实际 P 非零、层留数非零、K 的符号或原产品的新误差阶。

本次使用已完整读取的当前 ARS 路由、deep-research 工作流及有限
Phase 3 synthesis / devil's-advocate 要求：把继承结论、条件证明、
非实际测试例和未提供的几何证书分开。没有启动全 pipeline 或外部模型。
本文仅引用已读取的本地上游论证；没有进行新颖性检索或原创优先权声称。
新增插值式的证明在第 7 节自含，不冒称为某个外部来源的原结论。

实际只以 apply_patch 新增本笔记，并作限定的文本回读检查；没有执行
格点枚举、符号代数、压力估计、数值积分、实验、科学程序或历史 writer。
未改旧文件、冻结输入、协议、正式回执、失败记录、论文或 Route / Stage；
文本检查不充当数学正确性或实际几何条件已满足的证书。

[shell]: internal_shell_residue_identifiability_and_symmetry_kernel_20260909.md
[even]: internal_quantitative_theta_error_and_pressure_symmetry_20260908.md
[quartic]: internal_first_theta_correction_and_log_free_rate_20260908.md
[analytic]: internal_cubic_log_threshold_and_analytic_remainder_20260909.md
[geometry]: internal_geometric_tower_and_length_cutoff_20260908.md
