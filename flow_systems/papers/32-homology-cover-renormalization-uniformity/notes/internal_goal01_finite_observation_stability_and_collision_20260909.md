# P32 内部研究：有限层观测的稳定恢复与参数碰撞

记录日期：2026-09-09 UTC。持续目标的第一个有界内部推导单元。
本次只新增此笔记；不改论文、旧笔记、协议、冻结输入或阶段回执。
承接[层留数与对称核][shell]及[亚纯正则部分][analytic]。

结论分两层：固定 Q 的有限维 theta 族可以由有限完整层观测稳定恢复
整个亚纯轮廓的紧集限制；在固定可见维数、完整层成员稳定及共同避开
移动候选极点的紧参数族上，可取得条件一致的恢复常数。这不是任意
含噪全纯函数的稳定解析延拓，也不认证实际压力 Hessian 满足这些条件。

## 1. 固定对象、范数和继承的解析结构

实际项目仍固定曲面、整数同调基、有向本原 owner、时钟、
\(Q=2\pi^2D\) 及 \(P(x)=s_4(2\pi x)\)，不自由替换 D、P。
以下变动 Q 或测试 P 仅用于条件命题与代数反例，不是新实际压力数据。
令 \(V=\mathcal P_4\) 为四变量齐次四次空间，规定
\[
 P(x)=\sum_{|\alpha|=4}c_\alpha x^\alpha,
 \qquad \|P\|_V^2=\sum_{|\alpha|=4}|c_\alpha|^2,
 \qquad \dim V=35.                                      \tag{1}
\]
这是完整单项式系数范数，不是对称张量的另一加权范数。
以下可在实空间工作；用复系数及复误差时同一上界仍成立。
记 \(q_Q(x)=x^{\mathsf T}Qx\)、\(\mathcal E_Q=\{q_Q(k):k\ne0\}\)，
\[
 W_{Q,P}(\lambda)=\sum_{q_Q(k)=\lambda}P(k),\quad
 p_{0,Q}(P)=\int P(x)e^{-q_Q(x)}dx,\quad
 G_{Q,P}(u)=\sum_kP(k)e^{-uq_Q(k)}-p_{0,Q}(P)u^{-4}.        \tag{2}
\]
继承的核判准是
\[
 \mathcal N_Q=\bigcap_{\lambda\in\mathcal E_Q}\ker W_{Q,\cdot}(\lambda)
 =\ker(P\mapsto\mathscr A_{Q,P}),\qquad E_Q=\mathcal N_Q^\perp. \tag{3}
\]
规范整函数部分已由原 theta 积分固定，不能任意添加整函数。
[既有指数加权式][analytic]给
\[
 \mathscr A_{Q,P}(a)=\int_0^1e^{-au}G_{Q,P}(u)du
 +\sum_{k\ne0}\frac{P(k)e^{-(q_Q(k)+a)}}{q_Q(k)+a}
 -p_{0,Q}(P)V_4(a),                                    \tag{4}
\]
其中 V_4 是该笔记定义的固定整函数。候选极点为 \(-\mathcal E_Q\)，
阶数至多一，留数为 W；零留数使候选极点可消。
\(\mathcal L_{Q,P}=\mathscr A_{Q,P}-p_{0,Q}(P)a^3\operatorname{Log}a/6\)，
所以一般亚纯的是 \(\mathscr A\)，不能把含对数项的 \(\mathcal L\)
不加条件地称为全平面单值亚纯函数。

## 2. 固定 Q：有限完整层与紧集恢复定理

置 \(d=\dim E_Q\)。d=0 时轮廓恒零；以下设 d>0。
所有层泛函在 E_Q 上的共同核为零；若当前选出的共同核非零，再选
一个不在该核上恒零的层，核维数至少下降一。因此可选 d 个层
\(\lambda_1,\ldots,\lambda_d\)，使其限制组成 E_Q 的对偶基。
这比非共振格点的特定重建公式更一般，但不提供所需最大层高的上界。

取 E_Q 的正交基 \(e_1,\ldots,e_d\)，设
\[
 M_{ij}=W_{Q,e_j}(\lambda_i),\quad
 y=Mc+\eta,\quad \|\eta\|_2\le\varepsilon,\quad
 \widehat c=M^{-1}y.                                    \tag{5}
\]
对任意未知 P，这里 c 表示其正交可见部分；不可见部分不改变轮廓。
\(\|\widehat P-P_{E_Q}\|_V\le\varepsilon/\sigma_{\min}(M)\)。

**命题 1。** 对任意固定
\(K\Subset\mathbb C\setminus(-\mathcal E_Q)\)，有
\[
 \|\mathscr A_{Q,\widehat P}-\mathscr A_{Q,P}\|_{C(K)}
 \le\frac{C_{Q,K}}{\sigma_{\min}(M)}\varepsilon,
 \quad C_{Q,K}=\sup_{a\in K}
 \left(\sum_j|\mathscr A_{Q,e_j}(a)|^2\right)^{1/2}<\infty. \tag{6}
\]
证明：轮廓对 P 线性，应用 Cauchy–Schwarz 和 (5)；各基轮廓在 K
连续有界。所有 K 的重建来自同一个有限维系数，不是逐域选择延拓。□

可给不依赖抽象范数等价措辞的上界。令
\(R=\max_K|a|\)、\(\delta=\operatorname{dist}(K,-\mathcal E_Q)>0\)，则
\[
 C_{Q,K}\le\left(\sum_jB_j^2\right)^{1/2},\quad
 B_j=e^R\left[\int_0^1|G_{Q,e_j}(u)|du+
 \delta^{-1}\sum_{k\ne0}|e_j(k)|e^{-q_Q(k)}\right]
 +|p_{0,Q}(e_j)|\max_K|V_4|.                             \tag{7}
\]
有限性由零端 Poisson 界与 Gaussian 格点和保证。
另一种直接表达是定义层对偶多项式
\[
 R_i=\sum_j(M^{-1})_{ji}e_j,\quad
 W_{Q,R_i}(\lambda_j)=\delta_{ij},\quad
 \mathscr A_{Q,P}=\sum_iW_{Q,P}(\lambda_i)\mathscr A_{Q,R_i}. \tag{8}
\]
这时误差常数可直接取
\(\sup_K(\sum_i|\mathscr A_{Q,R_i}|^2)^{1/2}\)，可能优于 (6) 的乘积界。
固定对数支上的 \(\mathcal L\) 可用相应基轮廓得到同类界；极点上的
普通 sup 范数不能使用。数据模型始终要求未知轮廓属于这个固定族。

## 3. 欧氏测试型的精确奇异值及对偶基

仅取代数测试 \(q_\circ=\sum_i x_i^2\)，记
\(S_4=\sum_i x_i^4\)、\(S_{22}=\sum_{i<j}x_i^2x_j^2\)。
前轮的核分类及带符号置换在 (1) 下的正交性给
\(E_{Q_\circ}=\operatorname{span}\{S_4,S_{22}\}\)，维数恰为二。
对 \(P=AS_4+BS_{22}\)，
\[
 \|P\|_V^2=4|A|^2+6|B|^2,\quad
 e_1=S_4/2,\quad e_2=S_{22}/\sqrt6,\quad
 W(1)=8A,\quad W(2)=48A+24B.                            \tag{9}
\]
因而对于两个未加权层观测的欧氏误差范数，
\[
 M=\begin{pmatrix}4&0\\24&4\sqrt6\end{pmatrix},\quad
 MM^*=\begin{pmatrix}16&96\\96&672\end{pmatrix},\quad
 \boxed{\sigma_\pm=\sqrt{344\pm40\sqrt{73}}}.             \tag{10}
\]
检验：迹为 688，行列式为 1536；这直接给 (10)，无需数值程序。
\(\sigma_+\approx26.187\)、\(\sigma_-\approx1.497\)，条件数约 17.498。
完整 35 维空间上的算子有 33 维核；(10) 只描述两个可见方向。
若换成层平均、相对误差或加权观测范数，必须重新计算常数。

由 A=W(1)/8、B=W(2)/24-W(1)/4，得
\[
 R_1=S_4/8-S_{22}/4,\quad R_2=S_{22}/24,
 \quad \|R_1\|_V^2=7/16,\quad \|R_2\|_V^2=1/96,
 \quad \langle R_1,R_2\rangle=-1/16.                     \tag{11}
\]
Gaussian 单变量矩给 \(p_0(S_4)=3\pi^2\)、\(p_0(S_{22})=3\pi^2/2\)，
故 \(p_0(R_1)=0\)、\(p_0(R_2)=\pi^2/16\)。这里 R_1 也直接满足
\(\Delta R_1=0\)。该测试型的对数系数因此由 W(2) 单独确定：
\(p_0(P)=\pi^2W(2)/16\)。这不是实际压力系数的测量。

## 4. 两个极点碰撞：精确留数与平滑观测的差别

取 \(Q_t=\operatorname{diag}(1+t,1-t,1,1)\)、
\(P=x_1^4-x_2^4\)，\(\|P\|_V=\sqrt2\)。当 \(0<|t|<1/3\)，
所有 \(|k|^2\ge2\) 的点满足
\(q_t(k)\ge2(1-|t|)>1+|t|\)。因此完整层 \(1+t,1-t\) 分别只有
\(\pm e_1,\pm e_2\)，留数恰为 2、-2；两层间距为 \(2|t|\)。
其两个 Laurent 主部之和为
\[
 \frac2{a+1+t}-\frac2{a+1-t}
 =\frac{-4t}{(a+1)^2-t^2}.                              \tag{12}
\]
在共同远离 a=-1 的紧集上，这一对主部是 O(|t|)，虽然每个留数不小。
(12) 仅描述这两个主部，不把其他层或整函数部分丢弃为零。

更直接的完整 theta 诊断：固定 u>0，逐项微分由 Gaussian 绝对一致
收敛允许；交换坐标 1、2 说明 \(\Theta_{t,P}(u)\) 关于 t 为奇函数。
\[
 \Theta_{t,P}(u)=-t C(u)+O(t^3),\quad
 C(u)=u\sum_k(k_1^2-k_2^2)^2(k_1^2+k_2^2)e^{-u|k|^2}>0. \tag{13}
\]
正性已由 \(k=\pm e_1\) 等项保证，不依赖截断试验。
对任意固定有限组 \(u_1,\ldots,u_m>0\)，单位系数方向 P/√2 的
观测增益至多
\(|t|(\sum_jC(u_j)^2)^{1/2}/\sqrt2+O(|t|^3)\)。
它确实是 \(E_{Q_t}\) 内的方向：任何 \(R\in\mathcal N_{Q_t}\)
由上述两层必须满足 \(c_{4000}(R)=c_{0400}(R)=0\)，故与 P 正交。
因此平滑取样的下增益不能跨 t=0 保持正的一致下界。

t=0 时交换对称使整个 P 轮廓消失。非零小 t 的三个低层
\(1+t,1-t,1\) 分别检测 \(2c_{4000},2c_{0400},2(c_{0040}+c_{0004})\)，
故 \(\dim E_{Q_t}\ge3\)，而 \(\dim E_{Q_0}=2\)：这里确有秩变化。
这不证明精确分层留数的振幅矩阵也必然病态；其另一个难点是分辨
趋零的层间距。精确层标签、含噪平滑观测和未知 Q 误差不可混为一谈。

## 5. 新推导：稳定完整层给出局部固定的可见空间

必须区别两个“无碰撞”条件。仅声明所选 \(\lambda_i(Q)\) 彼此不等，
不能排除未选格点进入一个所选层，也不能排除层内原有成员分裂。
本文使用更明确的**完整层成员稳定**条件：在相对参数邻域 U 上，
存在固定非空有限格点集 \(S_1,\ldots,S_d\) 和连续标签 \(\lambda_i(Q)\)，使
\[
 \{k\ne0:q_Q(k)=\lambda_i(Q)\}=S_i\quad(Q\in U),
 \qquad \lambda_i(Q)\ne\lambda_j(Q)\ (i\ne j).           \tag{14}
\]
于是 \(T_i(P)=\sum_{k\in S_i}P(k)\) 在系数空间 V 上根本不依赖 Q。
U 可为一个受约束参数族的相对邻域；不声称对称层在整个正定锥的
任意开邻域中都保持成员不变。(14) 也不要求全部未选层彼此无碰撞。

**引理 2。** 若 U 上 \(\dim E_Q=d\) 恒定，且这些 d 个 T_i 在某个
\(Q_0\in U\) 的 \(E_{Q_0}\) 上完整，则
\[
 \mathcal N_Q=\ker T,\qquad E_Q=\operatorname{ran}T^*
 \quad(Q\in U),\qquad T=(T_1,\ldots,T_d).                \tag{15}
\]
证明：\(\mathcal N_Q\subseteq\ker T\) 因 T_i 始终是完整层泛函。
在 Q_0 完整使 T 的秩为 d；\(\ker T\) 和 \(\mathcal N_Q\) 都有
维数 35-d，故包含成为相等。取正交补即得 (15)。□

因此无需臆定一个随 Q 任意挑选的“连续基”：在 U 上可直接固定
\(\operatorname{ran}T^*\) 的正交基，M 也是固定矩阵，最小奇异值正且不变。
仅有整数值 d 恒定并不是本文对无限个、可能改变成员的层核所给的
连续性证明；(14) 与完整性才提供所需识别。若改用连续加权观测，
则须另证 E_Q 的正交投影连续、选局部正交标架及 M_Q 满列秩。
奇异值不依赖局部标架的正交变换，但不能假定全局标架总已给定。

## 6. 紧参数集合上的条件一致恢复

**命题 3。** 设 \(\mathcal T\) 为正定矩阵的非空紧集，满足：

1. \(\dim E_Q=d>0\) 在 \(\mathcal T\) 上恒定。
2. 每个 Q 都有相对邻域及满足 (14) 的 d 个完整层，且在该邻域的
   一个基点上完整。这里“完整”是对 E_Q 的单射性，不只是层互异。
3. 固定非空紧复集 K 对所有 Q 共同避开全部候选极点：
   \(a+q_Q(k)\ne0\) 对 \(a\in K,Q\in\mathcal T,k\ne0\) 成立。

则存在有限个局部观测设计和常数 \(\sigma_*>0,C_*<\infty\)，使已知
Q 使用其所在设计并满足观测误差 \(\|\eta\|_2\le\varepsilon\) 时，
\[
 \|\widehat P-P_{E_Q}\|_V\le\varepsilon/\sigma_*,\qquad
 \|\mathscr A_{Q,\widehat P}-\mathscr A_{Q,P}\|_{C(K)}
 \le C_*\varepsilon/\sigma_*                           \tag{16}
\]
对 \(Q\in\mathcal T\) 一致成立。每个设计用 d≤35 个层；有限覆盖的
全部标签数可超过 35，不把局部存在性误写成一个预先给定的全局列表。

证明代数部分：由紧性取有限子覆盖 \(U_1,\ldots,U_r\)。引理 2 在每片
给固定 E 和固定满秩矩阵 \(M_\ell\)，故可取
\(\sigma_* =\min_{1\le\ell\le r}\sigma_{\min}(M_\ell)>0\)。
片间重叠处 E 相同，改变正交基不改变对应奇异值；连通片上的 E
因局部固定而固定。若同一套完整层在整个参数集稳定，则可只用一个 M。

证明共同避让：紧性给 \(0<cI\le Q\le CI\)，令 \(R=\max_K|a|\)。
若 \(|k|^2>(R+1)/c\)，则 \(|a+q_Q(k)|>1\)。剩余 k 只有有限个，
每个分母在 \(K\times\mathcal T\) 连续且不为零，因而
\[
 \delta_*:=\inf_{Q\in\mathcal T,a\in K,k\ne0}|a+q_Q(k)|>0. \tag{17}
\]
所以只检查所选极点避开 K 并不足够；但不必排除远离 K 的未选极点
彼此碰撞。假设 3 是充分的候选极点条件，可能强于实际不可消极点所需。

为使解析常数也可追查，以下给粗略但明确的统一上界。对 \(\|P\|_V\le1\)，
\(|P(x)|\le\sqrt{35}|x|^4\)，故可取
\[
 S_*:=\sqrt{35}\sum_{k\ne0}|k|^4e^{-c|k|^2},\qquad
 p_*:=6\sqrt{35}\pi^2c^{-4}.                            \tag{18}
\]
它们分别控制 \(\sum|P(k)|e^{-q_Q(k)}\) 和 \(|p_{0,Q}(P)|\)。
最后一个积分常数由两次微分 \(\int e^{-c|x|^2}dx=\pi^2c^{-2}\) 得到。

零端须用统一 Poisson 界，不能分别估计两个发散项。写
\(B_Q(\xi)=\pi^2\xi^{\mathsf T}Q^{-1}\xi\)、
\(\beta=\pi^2/C\)、\(h=2\pi^2/c\)。Gaussian Fourier 变换的四阶导数
由一个四个一阶项之积、六个“二阶乘两个一阶”项及三个二阶配对项组成。
用 \(\|Q^{-1}\|\le1/c\)、\((\det Q)^{-1/2}\le c^{-2}\)，可取
\[
 H_*:=\frac{\sqrt{35}\pi^2}{c^2(2\pi)^4}(h^4+6h^3+3h^2),\quad
 D_*:=H_*\sum_{n\ne0}(1+|n|^4)e^{-\beta|n|^2/2},
 \quad I_*:=D_*\int_0^1u^{-6}e^{-\beta/(2u)}du<\infty.   \tag{19}
\]
确切地，\(0<u\le1\) 时每个非零 Fourier 项由
\(H_*u^{-6}(1+|n|^4)e^{-\beta|n|^2/u}\) 支配。利用
\(e^{-\beta|n|^2/u}\le e^{-\beta/(2u)}e^{-\beta|n|^2/2}\)，
求和给 \(|G_{Q,P}(u)|\le D_*u^{-6}e^{-\beta/(2u)}\)，故零端积分≤I_*。
这是[继承的多项式 Gaussian 推导][harmonic]在紧正定族上的显式版本。

将 (17)–(19) 代入 (4)，对所有单位 P 同时得到
\[
 \boxed{C_*:=e^R(I_*+S_*/\delta_*)+p_*\max_K|V_4|},
 \qquad \|\mathscr A_{Q,P}\|_{C(K)}\le C_*\|P\|_V.       \tag{20}
\]
结合代数误差界即证 (16)。同一支配还保证积分与级数在这些参数和
紧复域上连续；无需先从近似局部函数进行不受控的解析延拓。□

## 7. 证据边界与实际核查

固定 Q 的恢复是有限维线性模型内的定理；(16) 假设 Q 已知，没有
把 Q 的估计误差、层位置误差或模型外误差算入 ε。紧性只在完整性、
固定秩、成员稳定和共同避让已证之后给一致性，不替代这些证据。
常数 (7)、(19)、(20) 是绝对收敛的纸面表达式，本次未数值求值。
Qt 例在 t=0 发生秩变化与所选层合并，所以不满足命题 3 的假设。

ARS 的有界 argument-builder 用于分开继承事实、直接证明、条件统一
及反例；未启动论文流水线、Route 评审或 Stage 变更。数学依据为以上
有限维证明、完整层计数及已读的本地 Gaussian／亚纯表达式；未进行
新颖性查核，亦不声称原创优先权、独立复现或真实压力的数值证书。
没有提高原产品误差阶、赋予精确临界 Euler 产品有限值、恢复 owner
数据、构造自伴算子或证明全局行列式等式。

实际动作限于读取适用工作流和前述笔记、apply_patch 新建本文件，
并作行数、链接及文本核查；没有运行格点、积分、压力、符号或科学
程序，也没有使用历史 writer。当前目录不能提供 Git 状态，未据此
声称工作树洁净；本次唯一写入目标是本文件。旧失败记录与阶段边界保留。

[shell]: internal_shell_residue_identifiability_and_symmetry_kernel_20260909.md
[analytic]: internal_cubic_log_threshold_and_analytic_remainder_20260909.md
[harmonic]: internal_harmonic_quartic_finite_part_and_dual_lattice_series_20260908.md
