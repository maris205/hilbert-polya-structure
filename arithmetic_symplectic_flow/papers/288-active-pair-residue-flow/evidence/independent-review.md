# 288 独立内部复核：完整部分 owner、全周期与返回盆

**Candidate ID:** ANG-20260920-APR01  
**Status:** OWNED ACTIVE-SOURCE PRIME PACKETS; NATURALNESS OPEN — SCOPED ADVANCE / FORK  
**Verdict:** 三检查点完成，无待修正的数学阻断项。完整部分群胚、联合 Haar 时钟、全周期及 packet 分类成立；支持限定的 T0–T2 advance，不关闭自然性或后续拓扑／解析义务。

## 1. 输入绑定、实际顺序与权限

| 实际审阅输入 | SHA-256 |
|---|---|
| 原始 version-1 冻结卡 | 1459ec2252afe8d84736c986ac4f572104bc4c6b0d3031672ac780a1f03fc3d4 |
| 完整比较的主文 | b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8 |

检查点 1 仅读完整原卡，自行推导部分 owner、全部周期、前像递归、isotropy 与三项控制，先将 raw 结论发给主控。没有读取未来主稿或另一控制作者的答案。

主控宣布稿件完成并提示新增 Proposition 7 的命中界之后，主审在尚未读稿时另行推导该界并发送结果；这项定点核对不是没有提示的盲发现。随后才完整读取主稿，完成检查点 2/3。

卡后续若追加行政 outcome，仍以上表原始字节为 raw 输入。历史提案一致性按卡说明记录，本审查未另读旧 scout 文件核对其字节，也未从旧包转入证明。主审只写本报告；其他路径与 241/242 未修改。

## 2. 检查点 1：全部域、实际像与联合 Haar

在根 \((a,b)\) 上，允许 digit 恰为

\[
0\le j<b,\qquad j\ge\max(0,a-2b-w(b)+2).
\]

因此 D 及其补集均为 clopen 分支之并。\(D_0=Y\)，\(D_{m+1}=D\cap T^{-1}(D_m)\) 逐层 clopen；第 \(m\) 步落在 terminal point 仍属于 \(D_m\)，不能额外要求下一步存在。

每个许可分支把整个 \((j+bK)\times K\) 映到目标根的全部 \(K^2\)。实际逆为

\[
\theta(u,v)=(a,b,j+b(v-u),u).
\]

代回 T 及 residue 条件双向成立。整数乘法在完整 \(K\) 上单射，保证唯一除法；未把 \(K\) 当成整环。

联合测度计算分两步：\((u,v)\mapsto(v-u,u)\) 是保持联合 Haar 的群自同构，再将首坐标乘 b 并平移 j。故对任意 Borel terminal set E，
\(\mu(\theta E)=(h\otimes h)(E)/b\)，不是边缘密度猜测或双坐标因子抵消。

目标根 \((r,s)\) 的所有前驱分支由 \(0\le j<r\)、\(a=2r+w(r)+j-s\ge2\) 参数化。因此其整个 \(K^2\) 有 incoming 当且仅当 \(2\le s\le3r+w(r)-3\)。

三个预列域控制均成立：\((4,2)\) 全 terminal；\((3,2)\) 仅 j=1 有定义并到 \((2,2)\)，j=0 terminal；目标 \((2,4)\) 无 incoming。terminal 与 missing-incoming 是不同性质，terminal units 也可能拥有前像。

## 3. 完整部分群胚与时钟

对可复合表示 \((x,m-n,y)\)、\((y,p-q,z)\)，只把中间 y 的前缀对齐到 \(\max(n,p)\)。较长的已定义前缀认证另一侧所需 continuation，因此外侧也有实际公共终点；没有越过 terminal endpoint 凭空延长。

同一箭头的两个表示具有相同 lag，较长表示本身认证两前缀可同步延长。在其实际有限分支域内取 clopen 邻域，给出合法的公共 refinement、逆与复合。空前缀保留所有 terminal identities。

有限前缀的联合 IMAGE factor 为 \(1/D_\alpha\)。因而完整 beta-to-alpha branch pair 上

\[
J(g)=D_\beta/D_\alpha,\qquad
c_G(g)=\log D_\alpha-\log D_\beta.
\]

公共 tail 因子抵消，证明表示无关与 cocycle 法则。实际 branch pairs 给可数 compact-open 基；端点和整数 lag 分离箭头，得到局部紧、Hausdorff、第二可数 étale owner。

局部常值公式和 source measure 全支撑唯一确定连续全点密度，包括 null returns。forward deletion 的 clock 为 \(-\log b\)，inverse insertion 为 \(+\log b\)。实扩张的全部实参数平移联合连续、双向完整；T 部分定义不使这项实时间作用部分定义。

## 4. 全周期：整数根闭合不等于完整状态闭合

主审 raw 取周期 pair 为 \((q_i,q_{i+1})\)，得到

\[
q_{i+2}-2q_{i+1}+q_i=w(q_{i+1})+j_i\ge0.
\]

周期求和左边为零，故每项 \(w\) 与 j 都为零。零二阶差分的周期序列只能常数，因此根为 \((p,p)\)，且 \(w(p)=0\) 精确等价于 p 为素数。这一步包含所有 defined 周期路径和 p=2。

必须另行排除各长度的非零种子周期。主审 raw 使用整矩阵
\(A_p=\left(\begin{smallmatrix}0&p\\1&p\end{smallmatrix}\right)\)：
零 digit 下 \(p u_{i+1}=A_pu_i\)，周期给 \((A_p^L-p^LI)u_0=0\)。
其特征值 \((p\pm\sqrt{p^2+4p})/2\) 分别大于 p、位于 \((-1,0)\)，所以任意 \(L\ge1\) 的该 determinant 非零。

主文采用等价且更直接的整数逆矩阵

\[
B_p=\begin{pmatrix}-p&p\\1&0\end{pmatrix},
\qquad (B_p^L-I)u=0.
\]

其特征根一个在 \((0,1)\)、另一个小于 \(-p\)，所以任何正次幂都不为 1，\(\det(B_p^L-I)\) 是非零普通整数。该判断先于任何 kernel 结论。

乘整数 adjugate 后，每个 seed coordinate 被这个非零整数消去；整数乘法在 \(K\) 上单射，所以 \(u=0\)。未声称非单位 determinant 在 \(K\) 上可逆，也没有用场论约消。

因此完整 periodic set 精确为 \(z_p=(p,p,0,0)\)，每个都是 fixed point。无其他 fixed、高周期、合数根或非整数 periodic states；不是仅查不动核心或有限长度。

## 5. 全前像、完整稳定子与命中界

对任意 target \((r,s,u,v)\)，全部 immediate predecessors 恰为

\[
(2r+w(r)+j-s,\ r,\ j+r(v-u),\ u),
\quad 0\le j<r,\quad 2r+w(r)+j-s\ge2.
\]

反复使用此有限前像算子，得到且仅得到 \(B_p=\bigcup_{m\ge0}T^{-m}\{z_p\}\)。特别地，\(z_p\) 的直接前像为 \((p+j,p,j,0)\)，\(0\le j<p\)；不能只保留 j=0 核心。

每层逆树有限，所有有限逆前缀在 seed 上 integer-affine，所以全部 returning seeds 是普通整数对。每个 \(B_p\) 以及全 returning locus 可数、joint-Haar-null。整数 seed 本身不是返回充分条件，例如 terminal 根 \((4,2)\)。

非零 lag isotropy 等价于一段真实已定义轨迹闭合，因而产生可无限重复的实际周期；终止轨迹不可能满足这一条件。由全周期分类，恰在某个 \(B_p\) 上有非平凡 source isotropy，完整 lags 为 \(\mathbb Z\)，clock 为 \(k\log p\)。

前缀共轭的 clock 抵消，故 \(H_z=(\log p)\mathbb Z\)，最小正时间为 \(\log p\)，重复为 \(r\log p\)。其他状态的 source isotropy 与 H 均平凡；所有 fixed-object extension isotropy 也平凡。

每个 \(B_p\) 是一个完整 G 轨道；不同 fixed cores 无共同 tail。因此全部实相位给出每素数恰一个 abstract primitive packet，且没有其他 positive packets，不把等时当作同包。

**首次命中界的独立核验。** 设第 h 步首次命中 \(z_p\)，定义 \(\delta_i=b_i-a_i\)。递推给 \(\delta_{i+1}=\delta_i+w(b_i)+j_i\ge\delta_i\)，最终 \(\delta_h=0\)。

若某 \(i<h\) 已有 \(\delta_i=0\)，其后增量全为零，根恒为 p 且 digits 全零；整数逆矩阵把末端零 seed 反传为零，于是第 i 步已是 \(z_p\)，矛盾。所以 h>0 时所有此前 \(\delta_i<0\)。

对 \(1\le i<h\)，\(b_i-b_{i-1}=\delta_i\le-1\)，最后一步 \(\delta_h=0\) 不再降低 b。因此 \(p\le b-(h-1)\)，得 \(h\le b-p+1\le b-1\)；h=0 单独满足 p=b。

沿这些路径 indices 不超过初始 b，长度与每步 digit 数均有有限上界。每个路径对指定零终点有唯一逆像，故每个根上的 \(B_p\) fibre 有限。此结论不推普遍收敛，也不在本报告推 coarse topology。

## 6. 三个独立控制与全文比较

三项控制的结果在主稿前由主审独立推导，未采用另一控制作者的答案。每项单独替换 v、重算其 D 和实际箭头；联合 Haar 证明仍作用于它自身的许可分支。

因 v 非负，循环和给出 constant root n、v(n)=0、所有 digits 零。上述矩阵论证对全部 \(n\ge2\) 成立，稳定子与前像论证遂给各自完整 ledger：

- WITNESS-OFF：每个整数 \(n\ge2\) 恰一个 least-\(\log n\) packet。
- WITNESS-ON：没有周期状态、非零 source isotropy 或 positive packet。
- SHIFTED TEST：恰在 \(n+1\) 为素数、\(n\ge2\) 时有一个 least-\(\log n\) packet。

例如 shifted 的 n=4 核心是独立 primitive，不能视作 n=2 包的第二次重复。这些控制证明选定 witness 的作用，也暴露非负约束零集可被工程选择的风险，不证明自然性。

检查点 2 完整主稿与上述 raw 证明一致；Proposition 7 的 h=0、last-step、零差分早命中与 rootwise finite-word 逻辑均通过。未发现需作者修改的数学命题。

## 7. 检查点 3：反方边界、provenance 与冻结结论

- 部分 owner 的公共尾必须由实际较长迭代认证，不能把 total-map 论证无条件套入；主文已作这项校准。
- 种子矩阵检查覆盖全部正周期，非零 determinant 只用于单射 kernel，不把 profinite 环误作域。
- 全 returning basins 及 terminal units 保留；countable/null 不授权删除它们或选择“中心”代表。
- 三控制是不同 owner，不构成事后修复；w 的直接计算涉及 b−2 个候选除数测试，measure clock \(\log b\) 不等于该计算的 elapsed runtime 或最优复杂度证明。
- 正 prime ledger 不关闭 witness/completion/measure 的自然性，不建立 contact、Hamiltonian、symplectic lift 或 formal Route。
- abstract packets 不自动是完整 coarse quotient 中的闭嵌入圆；该拓扑义务可被命名，但本轮未实施。无 T3、trace、zeta 或 operator。

采用 ARS academic-research-suite 三检查点。辅助 haar_seed_branch_check 仅 raw-card 审 partial domains、joint Haar、合法群胚复合／clock 与三个域端点，未读主稿／他人答案，未检查周期、basins 或三个 witness comparators。主审独立承担全周期、controls、命中界及全文比较。

主控、主审与辅助共享模型／研究上下文；raw-before-paper 是实际执行顺序，不是外部同行评审、独立误差保证或形式验证。未运行科学数值、修改旧包或扩展未授权研究。

最终维持 **SCOPED ADVANCE / FORK**：完整同对象 T0–T2 记录成立，自然性 OPEN；下一项 topology／analytic owner 必须有自己的明确合同。经典 A0/A1/A2 不适用，formal UNASSIGNED、Route B NOT INVOKED；241/242 未触碰。
