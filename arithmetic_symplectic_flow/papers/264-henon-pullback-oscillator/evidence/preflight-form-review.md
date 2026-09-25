# CS14 冻结后形式审查

## Material Passport

- Scope ID：`ASFS-DISCOVERY-20260919-CS14`。
- 对象：单步 Hénon 酉拉回振子及其 \((h,\kappa)\) 同谱代表。
- 日期：2026-09-19。
- Origin Skill：ARS academic-research-suite / experiment-agent；用于有界合同、证明与执行证据分离。
- 结论：`NO FORMAL BLOCKER IDENTIFIED`，可推进独立实现审查。
- 执行证据：`UNVERIFIED / NOT RUN BY THIS REVIEW`。
- 限制：只读原卡和预执行澄清，独立局部推导；未读取 peer 审查答案、runner 或科学输出，未运行分解、优化、数值积分或其它科学计算。

本代理此前参与过架构预筛，本报告不是外部同行评议或跨模型认证。本次只写此报告，不修改冻结卡。主控补充要求核对经典体积系数和固定指标 Ritz 收敛，两项均由下文独立推导。

## 1. 冻结输入

| 文件 | SHA-256 |
| --- | --- |
| [candidate-card.md](../candidate-card.md)，全文 | `1c5c8568db18f8f445990bcafa268f9a54cc22d7dfbe21a583a2820d6085e9bc` |
| [pre-execution-clarifications.md](../pre-execution-clarifications.md)，全文 | `6e89655cd21195c48302b864d539e04c6bacad7dba04df6c0e1b979e594ee461` |

澄清文件明确了 \(\kappa=0\) 的闭型域、有限幂读出、无有效种子的停止分支及完整 SOURCEOFF 控制；没有改变卡的数学对象或预算。下文所说“精确”指相应解析定义或精确算术，不指机器浮点认证。

## 2. 源映射、拉回方向与混合型

固定

\[
F_a(q,p)=(1-aq^2-p,q),\quad
F_a^{-1}(Q,P)=(P,1-aP^2-Q).
\]

\(\det DF_a=1\)，逆映射全局明定，故 \(U_af=f\circ F_a^{-1}\) 在 \(L^2(\mathbb R^2,dq\,dp)\) 酉，\(U_a^*f=f\circ F_a\)。这是原二阶递推的延迟状态映射，不是另换标准映射；但 Hilbert 空间是两维相空间上的函数空间，不是已经建立的原 Hénon 量子化。

设

\[
\mathfrak a_h[f]=h^2\|\nabla f\|_2^2+
\|(q-.5)f\|_2^2+\|(p-.5)f\|_2^2,
\]

\[
\mathcal V_A=\{f\in H^1(\mathbb R^2):(q-.5)f,(p-.5)f\in L^2\}.
\]

混合型为

\[
\mathfrak h[f]=(1-\eta)\mathfrak a_h[f]+\eta\mathfrak a_h[U_af],
\quad D(\mathfrak h)=\{f\in\mathcal V_A:U_af\in\mathcal V_A\}.
\]

正权重型和在该交集上闭合，且 \(C_c^\infty\) 为稠密子集。不能只假定 \(U_a\) 在整个普通 \(H^1\) 上有统一有界作用；导数系数随 \(q\) 增长。

在变量 \(z=F_a(q,p)\) 下，

\[
DF_a^{-T}\nabla f=(-\partial_pf,\ \partial_qf-2aq\partial_pf),
\]

故 \(\mathfrak a_h[U_af]\) 的动能为
\(h^2(\|\partial_pf\|^2+\|\partial_qf-2aq\partial_pf\|^2)\)，势为
\((q-.5)^2+(p-.5+aq^2)^2\)。这核实了 \(U_a^*A_hU_a\) 的方向和符号；若改为 \(U_aA_hU_a^*\)，不可直接沿用这些坐标公式。

令 \(\kappa=\eta(1-\eta)a^2\)。逐项完成平方得

\[
\begin{aligned}
\mathfrak h[f]={}&h^2\|\partial_qf-2\eta aq\partial_pf\|^2
+h^2\|\partial_pf\|^2+4\kappa h^2\|q\partial_pf\|^2\\
&+\|(q-.5)f\|^2+\|(p-.5+\eta aq^2)f\|^2
+\kappa\|q^2f\|^2.
\end{aligned}
\]

没有遗漏一次导数修正或势常数；该等式首先在紧支光滑函数上成立，再延拓至相应闭型。

## 3. 剪切与 \(h\) 缩放 Fourier 变换

置 \(r=p-.5+\eta aq^2\)，以 \(f(q,p)=g(q,r)\) 实现保测剪切。此时

\[
(\partial_q-2\eta aq\partial_p)f=\partial_qg,
\qquad \partial_pf=\partial_rg.
\]

故同谱 Friedrichs 代表的形式为

\[
\mathfrak j[g]=h^2\|\partial_qg\|^2+h^2\|\partial_rg\|^2
+\|(q-.5)g\|^2+\|rg\|^2
+\kappa\|q^2g\|^2+4\kappa h^2\|q\partial_rg\|^2,
\]

其微分表达式确为

\[
J=-h^2\partial_q^2-h^2(1+4\kappa q^2)\partial_r^2
+(q-.5)^2+r^2+\kappa q^4.
\]

\(\kappa>0\) 的形式域由上述六项及 \(L^2\) 范数有限给出。这个域是闭算子图范数的交集，不能简化为未经核对的普通 \(H^2\) 算子域。

用

\[
(\mathcal F_hg)(q,y)=(2\pi h)^{-1/2}
\int_{\mathbb R}e^{-iry/h}g(q,r)\,dr
\]

变换 \(r\)：\(-h^2\partial_r^2\mapsto y^2\)、\(r^2\mapsto-h^2\partial_y^2\)。因此

\[
S=-h^2(\partial_q^2+\partial_y^2)
+(q-.5)^2+y^2+\kappa q^4+4\kappa q^2y^2.
\]

系数 \(4\kappa\) 无额外 \(h\) 因子。\(S\) 的型域为

\[
\{g\in H^1:(q-.5)g,yg,q^2g,qyg\in L^2\}.
\]

\(\kappa=0\) 时必须删除后两个加权条件，采用原二维振子的闭型域；若继续强加它们，该较小域并不是振子型范数下的闭域。预执行澄清已经正确消除这个歧义。

所有 \((a,\eta)\) 的谱依赖经上述酉变换只剩 \(\kappa\)。卡固定 \(\eta=1/2,a=2\sqrt\kappa\) 是有效的唯一代表选择，活动参数确为 \((h,\kappa)\)，不是 \((h,a,\eta)\) 三个参数。该算子同谱坍缩不证明不同源映射的轨道动力学等价。

## 4. 正下界、紧预解及分数幂

对紧支光滑 \(g\)，一维配方给

\[
h^2\|\partial_qg\|^2+\|(q-.5)g\|^2\geq h\|g\|^2,
\quad
h^2\|\partial_yg\|^2+\|yg\|^2\geq h\|g\|^2.
\]

故 \(S\geq2hI\)，从而 \(J,H\geq2hI\)。形式闭合可由各导数与多项式乘法闭算子的图范数交集直接得到；紧支光滑函数的截断、局部光滑化给出型核心。

型范数控制 \(H^1\) 及 \((q-.5)^2+y^2\) 的二阶位置矩。局部 Rellich 紧性加位置矩控制的统一尾部小量，给出型域到 \(L^2\) 的紧嵌入，因此这些算子有紧预解和完整离散本征列。这里未声称该本征列与任何外部目标相同。

\(K=J^{3/2}\) 由正算子的谱演算唯一定义。若 \(Je_j=\lambda_je_j\)，则

\[
D(K)=\left\{f:\sum_j\lambda_j^3|\langle e_j,f\rangle|^2<\infty\right\},
\quad Ke_j=\lambda_j^{3/2}e_j.
\]

不能将此域无证明地写成普通 \(H^3\)。幂算子仍自伴、有正下界和紧预解。主读出从真实基态编号，\((\lambda_j/\lambda_1)^{3/2}\) 不需要相位分支，也不能减去基态。

## 5. 精确 Hermite 压缩及 padding

固定 \(h,\kappa,\rho>0\)，令 \(b=\rho h\)，\(x=q-.5\)。在一维 Hermite 基底中

\[
X=\sqrt{b/2}(L+R),\qquad
D=(L-R)/\sqrt{2b},\qquad Q=X+.5I.
\]

输入指标 \(0,\ldots,n-1\) 经一次坐标或导数后最多到 \(n\)，因此 \((n+1)\times n\) 矩形矩阵完整包含其像。于是

\[
X_{\rm rect}^*X_{\rm rect}=P_nX^2P_n,
\quad D_{\rm rect}^*D_{\rm rect}=P_n(-D^2)P_n,
\quad Q_{\rm rect}^*Q_{\rm rect}=P_nQ^2P_n.
\]

两次坐标后最多到 \(n+1\)，故 \((n+2)\times n\) 的 \((Q^2)_{\rm rect}\) 给出

\[
(Q^2)_{\rm rect}^*(Q^2)_{\rm rect}=P_nQ^4P_n.
\]

先形成截断 \(n\times n\) 方阵再四次幂会漏掉越过截断边界后返回的链，不是同一压缩。卡中的逐步 padding 正确；独立 padding+4 多项式最后压缩也是足够的控制表示。

不同轴上的乘法可分离，所以完整二维压缩恰为

\[
S_n=H_0\otimes I+I\otimes H_0
+\kappa(Q_4\otimes I+4Q_2\otimes Y_2).
\]

这是 \(S\) 的二次型精确压缩，因而精确算术下 \(S_n\geq2hI\)。\(\rho=1\) 时升降算子的二次非对角项抵消，\(H_0=\operatorname{diag}(h(2i+1))\)。一般基宽则有

\[
(H_0)_{ii}=\tfrac12(b+h^2/b)(2i+1),\quad
(H_0)_{i,i+2}=\tfrac12(b-h^2/b)\sqrt{(i+1)(i+2)},
\]

作为组装解释而非新增数值控制。有限 \(\rho=1.25\) 与有限 \(\rho=1\) 不必同谱；它们逼近相同连续 owner，但子空间不同。

SOURCEOFF 的完整有限谱应为 \(\{2h(i+j+1):0\leq i,j<n\}\) 的带重数排序。这个矩形集合不应笼统称为连续振子的“前 \(n^2\) 个本征值”；在高矩形层它会缺少某些矩形外状态。卡的有限矩形解析控制本身正确。

有限主读出严格是 \((S_n)^{3/2}\)，不是 \(P_nS^{3/2}P_n\)。预执行澄清已正确固定这一点。

## 6. 矩形 Hermite 空间是形式核；Ritz 的确切范围

本节给出固定参数、固定基宽下的收敛结论，不宣称有限 \(n=52\) 的误差已知。

先以光滑大球截断逼近任意 \(S\) 型域函数：多项式加权项靠尾部可积性收敛，梯度中额外的截断导数由 \(L^2\) 尾部控制。再在固定紧集上光滑化，所有权重有界，故 \(C_c^\infty\) 是型核心。

令 \(T_b\) 为二维 Hermite 总数算子加一，其基底本征值是 \(i+j+1\)。升降算子公式直接给出，对于有限 Hermite 线性组合 \(v\)，所有一次导数及次数不超过二的坐标乘法均满足

\[
\|\partial_qv\|+\|\partial_yv\|+\|(q-.5)v\|+\|yv\|
+\|q^2v\|+\|qyv\|+\|v\|
\leq C_b\|T_bv\|.
\]

理由是一次操作的系数为 \(O(\sqrt{i+j+1})\)，二次操作为 \(O(i+j+1)\)，每个操作只连有限个邻近指标。故型范数被 \(T_b\) 图范数控制。

任意 \(f\in C_c^\infty\) 都属于 \(D(T_b)\)。矩形投影 \(P_n^{(2)}\) 与 \(T_b\) 对角相容，且

\[
\|T_b(I-P_n^{(2)})f\|^2
=\sum_{i\geq n\ \mathrm{or}\ j\geq n}(i+j+1)^2|f_{ij}|^2\to0.
\]

由上界和型闭性，矩形 Hermite 展开在型范数下逼近 \(f\)。结合 \(C_c^\infty\) 型核心，\(\bigcup_n\operatorname{Ran}P_n^{(2)}\) 是所需形式核。

因此对固定 \(h,\kappa,\rho\) 和每个固定指标 \(j\)，足够大 \(n\) 时

\[
\lambda_j(S)\leq\lambda_j(S_{n+1})\leq\lambda_j(S_n),
\qquad \lambda_j(S_n)\downarrow\lambda_j(S).
\]

标量正幂也给 \(\lambda_j(S_n)^{3/2}\downarrow\lambda_j(S)^{3/2}\)，但这不是对 \(P_nK P_n\) 的 Ritz 声明。比值 \(\lambda_j(S_n)/\lambda_1(S_n)\) 不必单调，有限相邻网格差不是对极限误差的上界。不同 \(\rho\) 或不同搜索参数的子空间/算子也不能套用同一嵌套单调性。

## 7. 经典相体积的精确领先系数与余项

定义四维经典符号

\[
\mathfrak s(q,y,\xi,\zeta)=\xi^2+\zeta^2+W(q)+(1+4\kappa q^2)y^2,
\qquad W(q)=(q-.5)^2+\kappa q^4.
\]

这是二维算子的四维余切变量积分，不是原 Hénon 二维闭轨体积。设不归一化体积为 \(\mathcal V_J(E)=\operatorname{vol}_4\{\mathfrak s\leq E\}\)，并定义带相格归一化的形式体积
\(\Phi_J(E)=(2\pi h)^{-2}\mathcal V_J(E)\)。这些符号都不是谱计数函数。

先积两动量圆盘，再积 \(y\)，精确得到

\[
\mathcal V_J(E)=\frac{4\pi}{3}
\int_{\mathbb R}\frac{[E-W(q)]_+^{3/2}}{\sqrt{1+4\kappa q^2}}\,dq,
\quad
\Phi_J(E)=\frac1{3\pi h^2}I(E).
\]

固定 \(\kappa>0\)，取 \(R=(E/\kappa)^{1/4}\)、\(g(q)=\sqrt{1+4\kappa q^2}\)。因 \(W\geq\kappa q^4\)，支持包含于 \([-R,R]\)。令

\[
I_0(E)=E^{3/2}\int_{-R}^R\frac{dq}{g(q)}
=\frac{E^{3/2}}{\sqrt\kappa}\operatorname{arsinh}(2\sqrt\kappa R).
\]

对 \(x\geq0\)，\(0\leq1-(1-x)_+^{3/2}\leq3x/2\)，故

\[
0\leq I_0(E)-I(E)
\leq\frac32E^{1/2}\int_{-R}^R\frac{W(q)}{g(q)}dq.
\]

奇函数项 \(-q/g(q)\) 积分为零；其余项利用 \(g(q)\geq2\sqrt\kappa|q|\) 给

\[
\int_{-R}^R\frac{W(q)}{g(q)}dq
\leq\frac{E}{4\sqrt\kappa}
+\frac{E^{1/2}}{2\kappa}
+\frac{\operatorname{arsinh}(2\sqrt\kappa R)}{4\sqrt\kappa}
=O_\kappa(E).
\]

另一方面
\(\operatorname{arsinh}(2\kappa^{1/4}E^{1/4})=\frac14\log E+O_\kappa(1)\)。因此

\[
\boxed{\mathcal V_J(E)=\frac{\pi}{3\sqrt\kappa}E^{3/2}\log E
+O_\kappa(E^{3/2})},
\]

\[
\boxed{\Phi_J(E)=\frac{1}{12\pi h^2\sqrt\kappa}E^{3/2}\log E
+O_{h,\kappa}(E^{3/2})}.
\]

对形式经典能量 \(\mathfrak s^{3/2}\)，仅作阈值替换 \(E=t^{2/3}\)，得到

\[
\boxed{\Phi_K(t)=\frac{1}{18\pi h^2\sqrt\kappa}t\log t+O_{h,\kappa}(t)}.
\]

这不声称量子 \(J^{3/2}\) 的完整 Weyl 符号逐点等于 \(\mathfrak s^{3/2}\)，更没有证明任何固定 \(h\) 的 Weyl 谱计数定理、Tauberian 结论或零点认同。实际首点定标还改变能量尺度，不能直接把该领先常数当作拟合目标的已匹配常数。

该渐近不对 \(\kappa\downarrow0\) 一致。\(\kappa=0\) 时四维振子体积直接给
\(\Phi_J(E)=E^2/(8h^2)\)、\(\Phi_K(t)=t^{4/3}/(8h^2)\)，属于不同增长阶。不得把正 \(\kappa\) 的公式代入 SOURCEOFF 的零分母。

## 8. 控制、预算与最终边界

训练 \(n=24,28\) 的维数为576、784；细格36、44、52的维数为1296、1936、2704，均能保留前320态且不选奇偶块。小控制 \(n=8\) 总维64，不套用320态读出门。完整矩阵和同次本征态来自一次全分解，不能补做第二次求态。

12种子加最多18优化调用为30对、60训练分解；加3小控制、3细格、1宽度、1 SOURCEOFF，最多68次全实对称分解。无有效种子则不优化、不造赢家、不后检。零源控制应覆盖全部有限 \(n^2\) 个值。边缘占据的两轴条件取并集，角部不得重复计数。

默认基宽的同参数网格确实嵌套；宽度检查是另一组有限试探空间，不是要求其与默认有限谱精确相同。低残差、正交性、谱矩和边缘占据只是诊断。严格正性的形式证明不自动保证浮点分解或有限尾部精度；卡的失败保留、禁止裁剪和禁止重试规则适当。

稠密全矩阵/全态存储随 \(n^4\) 增长，全分解一般成本随 \(n^6\) 增长；68次上限和600秒硬限不是运行一定完成的保证。本审查没有作预算预演。

最终判断：源映射方向、剪切、Fourier 缩放、\(\kappa\) 坍缩、闭型正性和紧性、矩形 Gram、固定指标 Ritz 结论及经典体积系数均一致。未发现需要改变冻结对象的数学阻断。保留两项已澄清的 owner 区别：\(\kappa=0\) 取振子闭域；有限幂作用于 \(S_n\)，不是先对无限算子取幂再压缩。

本对象仍含新选的振子中心/度量、混合方式和密度导向 \(3/2\) 幂。保留完整单步映射来源不等于保留其全部谱可识别动力信息，更不自动恢复素数符号、时钟或闭轨账本。本报告只支持下一步实现审查，不转授旧结果、不评价 Route、不宣布数值或无限目标成立。

独立推导写入后，按主控要求只读回主稿第2–4节：拉回度规、剪切/Fourier、型域与紧性、体积系数及余项、Hermite 压缩和固定指标 Ritz 范围均与本报告一致。该定点回读未发现新增阻断，不覆盖主稿其它章节或任何尚未审查的执行结果。
