# Paper29 后备调查：高阶动力次数的可证性与新颖性障碍

日期：2026-09-05。范围：同一 separated polynomial Hamiltonian shear 辛映射族；独立、有界调查。本文不是 Paper29 立项、证明终审、Route 评价或批次通过记录。

## 结论先行

本轮没有得到足以推荐为独立长文的成熟新候选，具体淘汰两个容易计算的方向：

1. **Product-shear 的完整动力次数平台确实可证，但只是短的标准推论。** 对 $r\ge3$、非恒定 $f,g\in\mathbb C[t]$，设 $D=(r\deg f-1)(r\deg g-1)$。则
   $$
   \lambda_0(F)=\lambda_{2r}(F)=1,\qquad
   \lambda_k(F)=D\quad(1\le k\le2r-1).
   $$
   显式有理坐标给出一个环面平移斜积，再结合固定动量底空间，两次应用 Dinh–Nguyên 的相对动力次数乘积公式即可闭合。这个推论不依赖尚在评估的碰撞层完整不变量域定理，也不需要逐个特殊纤维的全局 torsor 定理。
2. **最高次梯度在复射影空间无基点的 kick–drift 属于经典正则多项式自同构。** 若 $\deg\nabla V=a\ge2$、$\deg\nabla W=b\ge2$，且各自最高齐次梯度仅在原点同时为零，则
   $$
   \lambda_k(T_WS_V)=(ab)^{\min\{k,2r-k\}}.
   $$
   所需特殊计算只是 $I_+\cap I_-=\varnothing$；其余是已有理论。加入显式耦合或实严格凸性，不会使这个动力次数公式成为足够的新结果。

更困难而真正不落入这两种机制的是 P20 的偶数非平方 $g$ 子族，例如 $g=6$。本轮能准确缩小到唯一缺失的 $\lambda_2$，并给出两个快捷路线不适用的理由，但没有获得余维二循环的稳定模型。因此它仅是**尚未成熟的族内线索**，不是建议通过的新候选；不得以 $\det C_g$ 或坐标次数矩阵外幂代替答案。

## 输入、方法和证据等级

- 首读 [组合内审计](PAPER29_PORTFOLIO_AUDIT_20260905.md)，随后仅核对 [P20 问题书](../../papers/20-coupled-shear-degree-matrix/notes/RESEARCH_QUESTION.md)、[P25 最终提案](../../papers/25-hamiltonian-support-rank-unbounded-perron-degree/refine-logs/FINAL_PROPOSAL.md) 的映射公式及范围，以及 [product-shear 候选证明包](PAPER29_CANDIDATE_PROOF_V1_20260905.md) 的定义和既有 $\lambda_1$ 计算。没有扫描旧 build。
- 使用 `research-lit` 的对象—机制—结论比较，以及 `novelty-check` 的逐核心声明碰撞检查。数学是本地符号推导；文献核查使用公开一手论文和正式出版方页面。
- 以下完整 profile 是**本调查作者依据已核读外部定理所作的推导**，尚非独立证明验收。所有涉及 $\lambda_2(F_g)$ 的未知项继续标为未知。
- `novelty-check` 指定的 `mcp__codex__codex` 交叉模型工具未出现在可调用工具中；未伪称已完成该项，也没有另寻凭据或外发文稿。当前并发槽位由主任务及其他独立调查占用，没有再委派同一文件。
- 仅写本文件；没有修改旧源码、锁、账本或已接受产物，没有开 Paper29 项目、运行实验、编译、下载论文归档或进行外部写入。

## 1. 统一约定：真正的高阶次数

在光滑射影双有理模型 $\overline X$ 上，以 ample 类 $H$ 定义
$$
\lambda_k(F)=\lim_{n\to\infty}
\left((F^n)^*H^k\cdot H^{\dim X-k}\right)^{1/n}.
$$
这里的 pullback 是双有理图所定义的余维 $k$ 循环作用。它不是已有 Newton 坐标次数递推矩阵的外幂。以下计算采用标准动力次数及相对动力次数的双有理不变性和乘积公式；光滑射影模型可在特征零通过取图和解奇点获得，不要求原仿射商的所有特殊纤维光滑。

已核读的基础定理是 Dinh–Nguyên, *Comparison of dynamical degrees for semi-conjugate meromorphic maps*, Comment. Math. Helv. 86 (2011), 817–840，Theorem 1.1：若 $\pi F=G\pi$，$\dim X=N$、$\dim Y=M$，则
$$
\lambda_k(F)=\max_{0\le j\le M,\;0\le k-j\le N-M}
\lambda_j(G)\lambda_{k-j}(F\mid\pi).
$$
同文 Proposition 3.5 允许换双有理模型，Example 3.7 还明确讨论了由代数/李群中的变系数自同构给出的斜积。其射影版本已经足够；Dinh–Nguyên–Truong 2012 的 Theorem 1.1 推广到紧 Kähler 情形。参见 [正式全文，Theorem 1.1、§3](https://ems.press/content/serial-article-files/43270)，[Dinh–Nguyên–Truong 原文，Theorem 1.1](https://arxiv.org/html/1108.4792v1)。

## 2. 淘汰方向一：product-shear 平台是标准乘积公式的短推论

### 2.1 固定对象和两个半共轭

令
$$
Q=\prod_{i=1}^r q_i,\quad P=\prod_{i=1}^r p_i,\quad
x=q_rp_r,\quad c_i=q_ip_i-x\ (i<r),\quad c_r=0,
$$
$$
S_f(q,p)_i=\left(q_i,p_i+f'(Q)\prod_{j\ne i}q_j\right),\qquad
T_g(q,p)_i=\left(q_i+g'(P)\prod_{j\ne i}p_j,p_i\right),
\qquad F=T_gS_f.
$$
这不是通过把低维映射作直积而构造的例子：显示坐标中的更新同时依赖全部模。以下不另行声称它在任意双有理坐标下均不可分解；计算只需要实际存在的斜积。

写 $h_c(x)=\prod_i(x+c_i)$，取
$$
B=\{(c,Q,P,x):QP=h_c(x)\},\qquad
\pi:\mathbb A^{2r}\dashrightarrow B,\qquad
\rho:B\longrightarrow\mathbb A^{r-1}_c.
$$
则 $\dim B=r+1$，$F$ 下降为 $\Phi$，而 $\rho\Phi=\rho$。其有理公式为
$$
\widetilde x=x+Qf'(Q),\quad
\widetilde P=h_c(\widetilde x)/Q,\quad
x'=\widetilde x+\widetilde P g'(\widetilde P),\quad
Q'=h_c(x')/\widetilde P,
$$
且 $P'=\widetilde P$、$c'=c$。这些公式表达的是已定义全局多项式剪切在稠密图上的作用；分母不定义新的映射合同。

### 2.2 不是仅凭“有环面纤维”就宣称相对次数为 1

在 $Q\ne0$ 的有理图取 $u_i=q_i$，$1\le i<r$。由
$$
q_r=Q/\prod_{i<r}u_i,\qquad p_i=(x+c_i)/q_i
$$
恢复全部原坐标。因此
$$
\mathbb C(q,p)=\mathbb C(c,x,Q)(u_1,\ldots,u_{r-1}).
$$
一步更新满足
$$
u_i'=a_i(c,x,Q)u_i,\qquad
a_i=\frac{x'+c_i}{\widetilde x+c_i}.
$$
第 $n$ 次迭代在任一一般源纤维上的作用仍是逐坐标乘以非零常数。将纤维紧化为 $(\mathbb P^1)^{r-1}$，它在每一个次数上都是自同构，且在其数值循环群上作用为恒等。系数 $a_i^{(n)}$ 在**底空间**可能很复杂，但限制到一般纤维后没有次数增长。因此
$$
\lambda_j(F\mid\pi)=1\quad(0\le j\le r-1).
$$
这是本例的实际相对循环计算，而不是从坐标次数矩阵作类比。它正处于上述 [Dinh–Nguyên Example 3.7 的变系数斜积框架](https://ems.press/content/serial-article-files/43270)。

### 2.3 无须另开约化曲面的熵计算

令 $d=\deg f$、$e=\deg g$，$D=(rd-1)(re-1)>1$。严格最高项比较已给出
$$
\deg F^n=D^n,
$$
所以 $\lambda_1(F)=D$；这是原候选包明列为吸收内容的计算。第一次乘积公式立即给 $\lambda_1(\Phi)=D$。

另一方面，$\rho$ 的一般纤维是双有理曲面 $QP=h_c(x)$，$\Phi$ 在其上双有理。因此相对次数首尾为 1：
$$
\lambda_0(\Phi\mid\rho)=\lambda_2(\Phi\mid\rho)=1.
$$
底空间映射是恒等，故所有底空间动力次数为 1。再次使用乘积公式的 $k=1$ 情形，得到 $\lambda_1(\Phi\mid\rho)=D$。所以 $B$ 上完整 profile 是
$$
\lambda_0(\Phi)=\lambda_{r+1}(\Phi)=1,
\qquad \lambda_j(\Phi)=D\quad(1\le j\le r).
$$
最后沿 $\pi$ 与 $r-1$ 个全为 1 的相对次数取最大值，得到
$$
\boxed{\lambda_0(F)=\lambda_{2r}(F)=1,\quad
\lambda_k(F)=D\ (1\le k\le2r-1).}
$$
这里中阶范围检查不可省：当 $1\le k\le2r-1$，总能找到 $1\le j\le r$ 且 $0\le k-j\le r-1$；当 $k=0,2r$ 时则只能选到两个首尾的 1。

### 2.4 新颖性判定

**可证性：高；独立长文价值：低；建议：不独立立项。** 这个结果没有为一般环面扩张建立新理论，没有控制新的非平凡相对次数，也没有解决余维二的例外循环问题。它提供一个清楚的 Hamiltonian 应用，但标准定理和显式斜积共同使证明很短。若主候选最终值得成文，至多按其科学范围把本结果作为一个明确标注来源的推论；它不会自动挽救主候选的新颖性。

尤其不能把碰撞层分类的困难重复算到这个环境空间 profile 上：本计算只使用一般纤维，不需给每个碰撞层再做全局 quotient 或完整固定域分类。

## 3. 淘汰方向二：复无穷远无基点的梯度 kick–drift 已正则

### 3.1 可直接检验的充分条件

设
$$
A=\nabla V=A_a+\text{低次项},\quad
B=\nabla W=B_b+\text{低次项},\qquad a,b\ge2,
$$
其中 $A_a,B_b$ 是最高齐次部分，并假定
$$
A_a^{-1}(0)=B_b^{-1}(0)=\{0\}\quad\text{在 }\mathbb C^r\text{ 上}.
$$
对
$$
F(q,p)=\bigl(q+B(p+A(q)),\ p+A(q)\bigr)
$$
有 $\deg F=ab$，最高齐次部分为 $(B_b(A_a(q)),0)$。逆映射为
$$
F^{-1}(q,p)=\bigl(q-B(p),\ p-A(q-B(p))\bigr),
$$
次数同为 $ab$，最高齐次部分为 $(0,-A_a(-B_b(p)))$。在 $\mathbb P^{2r}$ 的齐次坐标 $[q:p:z]$ 中因此
$$
I_+(F)=\{q=0,z=0\}\simeq\mathbb P^{r-1},\qquad
I_-(F)=\{p=0,z=0\}\simeq\mathbb P^{r-1}.
$$
两者不交，故是 Sibony 意义下的 regular polynomial automorphism。经典理论给出正向前 $r$ 阶为 $(ab)^k$，反向对偶给出后 $r$ 阶，故
$$
\boxed{\lambda_k(F)=(ab)^{\min\{k,2r-k\}}.}
$$
已核读 Dinh–Sibony, *Super-potentials of positive closed currents, intersection theory and dynamics*, Acta Math. 203 (2009), 1–82，§5.5 首段、Theorem 5.5.1 及紧随其后的质量公式。该节明确使用不交不定集的定义、维数关系和前半段 pullback 质量 $d_+^k$。本例只是验证其假设；[作者原文 §5.5](https://arxiv.org/html/math/0703702v2#S5.SS5)。

### 3.2 显式耦合也不会绕开碰撞

例如在 $r=2$ 取
$$
V=q_1^4+q_2^4+q_1^2q_2^2+q_1^2+q_2^2,\qquad
W=p_1^4+2p_2^4+p_1^2p_2^2+p_1^2+p_2^2.
$$
两者都在显示坐标中耦合，并且实 Hessian 正定。其四次最高项的梯度在复数域无非零公共零点：在两坐标都非零时，分别归结为系数行列式为 $3$、$7$ 的二元线性系统（未知量为坐标平方）；有零坐标时直接结束。于是 $a=b=3$，完整 profile 是 $(1,9,81,9,1)$，仍只是上述经典情形。

一般固定总次数的齐次势中，无基点条件等价于其最高次射影超曲面光滑；Fermat 势已说明该条件非空。通过选择一般耦合项得到 Zariski 开子族不会提供新的动力次数机制。本节也不把“显示坐标耦合”升级成任意辛/双有理共轭下不可分解的分类定理。

### 3.3 重要纠错：实严格凸不推出复正则性

取 $r\ge2$，
$$
V(q)=\left(\sum_iq_i^2\right)^2+\sum_iq_i^2,
\qquad
W(p)=\left(\sum_ip_i^2\right)^2+\sum_ip_i^2.
$$
实 Hessian 是 $8qq^{\mathsf T}+(4\|q\|^2+2)I$，故严格正定。但最高齐次梯度 $4(\sum_iq_i^2)q$ 在非零复各向同性向量上消失。$F$ 的最高项与 $(\sum_iq_i^2)^4q$ 成正比，逆映射对应 $p$；取非零各向同性 $q$ 和 $p=0$ 就得到 $I_+\cap I_-$ 中的点。这是严格凸但非正则的反例。

**判定：复无基点子族可证但过薄；仅严格凸的泛化缺少假设，不应立项。** 本轮没有继续为径向反例另做正交群约化或扩展新的候选，以免偏离有界调查。

## 4. P20 的准确剩余问题：不是已有两个机制的可用变体

仅保留
$$
V_g=q_1^2q_2^2+q_1^g,\quad W_g=p_1^2p_2^2+p_2^g,
\quad F_g=T_{W_g}S_{V_g},
$$
其中 $g\ge6$ 是偶数且非平方，最小例子 $g=6$。P20 已有
$$
\lambda_1(F_g)=L_g=g+1+2\sqrt g.
$$
### 4.1 前后对称，剩余只有中阶

令 $D_0(q,p)=(q,-p)$。由于两势都是偶函数，
$$
D_0S_{V_g}D_0=S_{V_g}^{-1},\quad
D_0T_{W_g}D_0=T_{W_g}^{-1}.
$$
因此 $R=S_{V_g}^{-1}D_0$ 是多项式对合，满足 $RF_gR=F_g^{-1}$。由双有理不变性与正逆次数对偶，
$$
(\lambda_0,\lambda_1,\lambda_2,\lambda_3,\lambda_4)
=(1,L_g,\boxed{\text{未知}},L_g,1).
$$
对数凹性只给 $L_g\le\lambda_2\le L_g^2$，不确定中间值。这里的对数凹性和正逆对偶采用 [Dinh–Nguyên 原文引言的标准动力次数性质](https://arxiv.org/html/0903.2621v1)。

### 4.2 两个快捷路线均有实质障碍

- **不可能双有理共轭成正则多项式自同构。** 正则多项式自同构的 $\lambda_1$ 等于其整数代数次数，而 $L_g$ 为无理数。
- **不可能由一个双有理曲面映射加全部中性相对次数来产生同一 $\lambda_1$。** $L_g$ 的另一代数共轭为 $(\sqrt g-1)^2>1$，所以它不是 Pisot 或 Salem 数。Diller–Favre 的曲面结果排除这种第一动力次数；乘积公式又会把中性扩张的第一动力次数等同于曲面的第一动力次数。这也排除由两个曲面双有理映射直接作乘积后再双有理共轭得到 $F_g$：其第一动力次数必须是两曲面第一动力次数之一。

第二点核读了 Diller–Favre, *Dynamics of bimeromorphic maps of surfaces*, Amer. J. Math. 123 (2001), 1135–1169，作者全文 Theorems 0.1、0.3（稳定后单位圆外只有一个简单特征值）；对整数 Néron–Severi 作用即可排除本例的第二个大于 1 的共轭。[作者全文](https://www3.nd.edu/~jdiller/research/papers/bimeromorphic.pdf)。这只是 P20 既有数值的结构性推论，不是一篇新的高阶次数论文。

### 4.3 为什么现在不推荐立项

没有得到可迭代控制的余维二代数循环模型、紧化或例外循环追踪。现有 $2\times2$ 坐标次数矩阵
$$
C_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}
$$
仅控制已有的一阶坐标可见性；$\det C_g=(g-1)^2$ 不是已经证明的 $\lambda_2(F_g)$。不能从该行列式作数值拟合后升级为定理，也不能把 P25 的 support-row rank 理论变成高余维循环理论。

若未来重新授权这个具体问题，最小科学关卡应是：**为 $g=6$ 提供真实余维二 pullback 模型，并证明其在任意迭代下足以计算增长；在该机制存在前不写完整 profile 主张。** 单独计算几个有限 $\deg_2(F_g^n)$ 只能帮助排错，不能通过此关卡。本轮到此收束，不为未知值作猜测，也不启动额外实验。

## 5. 文献碰撞与检索边界

| 核心声明 | 最近一手来源 | 本例相对增量 | 新颖性/处置 |
|---|---|---|---|
| 环面变系数平移扩张的相对次数全 1，结合曲面得到平台 | Dinh–Nguyên 2011，Thm.1.1、Prop.3.5、Example 3.7；Dinh–Nguyên–Truong 2012，Thm.1.1 | 显式选择本族有理坐标，并代入两个 fibration | 低；不独立立项 |
| 无基点梯度 kick–drift 的全部次数 | Sibony 的 regular 理论；Dinh–Sibony 2009，§5.5 | 显式计算两个不定集 | 低；不独立立项 |
| P20 的 $\lambda_2$ 与高余维循环机制 | 上述理论仅给障碍及界；Diller–Favre 2001 排除曲面中性扩张快捷路线 | 尚无 $\lambda_2$ 定理 | 未知；仅未成熟线索 |

公开检索使用了三组不同表述，并作了 2024–2026 及最近六个月（2026-03-05 至 2026-09-05）的定向补查：

- product/relative 组：`dynamical degrees semi conjugate meromorphic maps product formula relative`；`Hamiltonian shear product dynamical degrees torus fibration`；`torus relative dynamical degrees translation`；`dynamical degrees skew product torus`；`dynamical degrees Danielewski`。
- regular 组：`regular polynomial automorphism dynamical degrees indeterminacy disjoint`；`symplectic regular polynomial automorphisms`；`gradient regular polynomial automorphism`；`dynamical degrees kick drift`。
- nonregular/中阶组：`Hamiltonian higher dynamical degrees`；`coupled shear dynamical degrees`；`symplectic polynomial automorphism higher dynamical degrees`；`higher dynamical degrees polynomial automorphisms 2024 2025 2026`，并使用 arXiv 域名及上述近六个月日期窗口。

较窄的新近检索未返回可核读的直接同构造命中，宽检索含有大量把物理“degrees of freedom”误配为 dynamical degrees 的无关结果，均未当证据。**未命中不是世界性开放证明。** 淘汰结论不依赖未命中，而依赖已经核读的一手定理确实短推可控两子族。机器学习会议列表与本纯数学问题无关，未作无意义的会议遍历。

正式元数据另核对 [Dinh–Nguyên 出版方页](https://ems.press/journals/cmh/articles/4825) 和 [Nguyên 作者出版目录中的 2012 条目](https://pro.univ-lille.fr/viet-anh-nguyen/publications/)。Truong 的代数化版本 [arXiv:1501.01523](https://arxiv.org/abs/1501.01523) 只核读摘要，未作为任何证明依赖；其 HTML 暂未成功取得，不以摘要代替定理核读。

## 最终建议

本轮成熟新候选数为 **0**。吸收 product-shear profile 作为可用短推论，淘汰复无基点 regular 子族的独立长文包装；P20 偶数非平方子族的 $\lambda_2$ 保留为未成熟族内问题。没有改变当前 Paper29 的科学状态或批次计数。
