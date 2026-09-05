# C399–C403 算术续筛收束：0 个新准入合同

日期：2026-09-05。作者：独立算术 scout；这是有界选题报告，不是编号论文、完成论文包或研究发布。

## 结论与工作边界

本次最多两个新子类型入口均在廉价准入阶段淘汰。**新冻结合同数为 0；本轮未找到其余两篇的事实必须保留。** 不用矩阵参数变换、Hessian 的代数群商模型、CRT 插值或有限局部 jet 填名额。

已执行的是仓库碰撞检索、主文献网页核对及闭合机制检查；本轮没有对下列两个新入口运行周期点枚举、GPU 试验或外部模型/API，也没有为它们撰写证明包、分配正式编号或提交 Git。限定的否定选择结论不等于全世界不存在新定理。

使用 `idea-creator` 与 Route A batch 工作流作准入筛选；按当前授权以 Astra 内部判断替代该 skill 旧外部 GPT 接口，不声称执行了跨模型审稿。全程维持 `NO_BAD_EULER_OR_ROOT_NUMBER`。

## 0. 前轮固定特征非线性 zeta：仍无全局闭合机制

对象保持为 $f(x)=x^2+1$ 在 $\mathbb A^1(\overline{\mathbb F}_7)$ 上的整数迭代，$N_r$ 是 $f^{\circ r}(x)-x$ 的**不同几何根数**，不是次数或带重数根数；真正的周期 zeta 为 $\exp(\sum_{r\ge1}N_rz^r/r)$。

本轮没有补出全周期乘子、全部野分歧塔及其全局汇总／消去控制。前轮的有限周期分解与局部重根检查不能推出全局有理性或非有理性；本轮不把继续算一个局部 jet 当作该全问题的推进。保留 `PARKED / NO GLOBAL CONTRACT`。

此结论不宣称问题已被证明全局开放；有限文献检索未发现现成解答，不是新颖性证明。也不将 C393 的特征零通用逆像树或 C384 的加性映射野分歧定理误充该非线性固定特征问题的解答。

## 1. 非线性矩阵多项式动力学：计数机制已有经典所有权

**准确对象／拟议全问题。** 对 $f\in\mathbb F_q[x]$，研究 $T_f:A\mapsto f(A)$ 在全部 $\operatorname{Mat}_n(\mathbb F_q)$ 上的迭代，原拟对全部维数与周期给出固定点计数、周期数及非半单 Jordan 修正，而不只是向量空间上的线性映射。

**最便宜精确检验与核心机制。** 第 $r$ 次固定点恰为

$$
(f^{\circ r}(x)-x)(A)=0.
$$

写 $E_r=f^{\circ r}(x)-x=\prod_\phi\phi^{e_\phi}$。当 $E_r\ne0$ 时，有理标准形把矩阵归为 $\mathbb F_q[x]$ 模；对应 $\phi$ 的分拆 $\lambda_\phi$ 必须满足最大部件不超过 $e_\phi$。记 $c_\lambda(q^{\deg\phi})$ 为该主模的自同构群阶，普通相似类计数给出

$$
\sum_{n\ge0}\frac{\#\{A\in\operatorname{Mat}_n(\mathbb F_q):E_r(A)=0\}}{|\operatorname{GL}_n(\mathbb F_q)|}u^n
=\prod_{\phi\mid E_r}\sum_{\lambda:\lambda_1\le e_\phi}
\frac{u^{(\deg\phi)|\lambda|}}{c_\lambda(q^{\deg\phi})}.
$$

这说明所谓完整固定点计数很容易闭合，却恰是将迭代多项式代入经典矩阵方程计数。$E_r=0$ 的退化情形是全部矩阵固定，亦不产生新机制。这里是解析准入检查；**未运行矩阵枚举试验**。

**经典／近期主文献。** Hua 的 *Polynomial equations for matrices over finite fields* 已给出矩阵多项式方程解数的一般公式，并明确联系 $\mathbb F_q[x]/(E)$ 的表示计数。它是上述直接代入合同的经典所有者，而非本轮发现。[Hua, 1999, DOI:10.1017/S0004972700032603](https://doi.org/10.1017/S0004972700032603)

Panja 的 *Periodic Points of Power Maps in Finite Matrix Groups and Algebras* 又直接研究有限矩阵幂映射的周期点及若干群的极限比例。该预印本的具体参数限制不能被夸大为覆盖任意多项式的完整功能图；但它进一步排除了把简单矩阵幂周期普查当成未被研究的新入口。[arXiv:2603.12295](https://arxiv.org/abs/2603.12295)

**仓库碰撞。**

- `symbolic_dynamics/docs/papers107_111_sequence/scouting/ALGEBRAIC_SCOUT.md:41,328–339` 已将 nilpotent-matrix squaring 判为占用的 Jordan-halving／squaring／absorber 机制，且已引用 Panja 上述预印本。
- `symbolic_dynamics/docs/papers107_111_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md:27` 有同一淘汰条目。
- `symbolic_dynamics/docs/papers147_151_sequence/phase1/HISTORICAL_OCCUPANCY.md:25` 已标明 generic group/semigroup/matrix power maps 的占用。

**为何原本值得看。** 非半单局部代数把有限域算术与非线性周期拼接在同一对象中，可避免外加素数钟。但“对象内生有限域”本身不使经典计数成为新的 A1/A2 桥梁。

**最强反对／杀题条件。** 如果主定理只有将 $E_r$ 代入 Hua 公式、Jordan 块更新或已有幂映射计数，则停止。该条件已经满足。没有提出并证明超出这些所有权的结构定理，故 `KILL_CLASSICAL / INTERNAL_COLLISION`，不冻结合同。

## 2. 椭圆模空间 Hessian 动力学：直接文献及本地筛选重叠

**准确对象／拟议全问题。** 对特征不为 $2,3$ 的有限域，在 $j$ 直线上研究由平面三次曲线 Hessian 产生的映射

$$
H(j)=\frac{(6912-j)^3}{27j^2},
$$

将它作为 $\mathbb P^1$ 上的有理自映射，包括极点和无穷远点。拟议全问题原是全部有限域的功能图、周期长度及曲线同构类与 $j$ 轨道之间的提升歧义分类。

**廉价检验／可能证明机制。** 先核对 Hessian 映射的 CM／Lattès 椭圆曲线商模型及现有全图分类；只有确认不被其覆盖后，才值得枚举小有限域。这里恰在第一关即发现直接所有权，因此**没有运行新功能图普查**。把已知椭圆曲线自同态经有限商推到 $j$ 直线，不是符合本轮要求的新机制。

**主文献所有权。** Mula、Pintore、Taufer 的最新条目标题为 *The Hessian of elliptic curves as a Lattès map*，直接研究该对象及有限域功能图。不能只引用早期版本某一同余类描述较少，便宣称最新版本仍有相同缺口。[arXiv:2407.17042](https://arxiv.org/abs/2407.17042)

Pintore 的 2025 官方会议摘要明确宣称按 $q\bmod3$ 描述有限域功能图。该摘要足以否定“此全图问题尚无直接研究”的初筛前提，但不是我们已逐项复核完整论文证明的证据。[官方会议摘要](https://ntmeeting.polito.it/content/download/1127/5421/file/9th_Pintore_Abstract.pdf)

Kettinger 的 *The dynamics of the Hesse derivative on the j-invariant* 又研究 $j$ 迭代、轨道尺寸及曲线层面的周期问题。其复几何结果不应被冒称为任意有限域全图定理；它仅作为相邻直接所有权的补充证据。[DOI:10.1016/j.jaca.2026.100043](https://doi.org/10.1016/j.jaca.2026.100043)

**仓库碰撞。** `symbolic_dynamics/docs/papers152_156_sequence/scouting/algebraic_replacement2/OWNER_SEARCH_LOG.md:236–251` 已检索并引用 Hessian 动力学与 arXiv:2407.17042；同目录 `SCOUT.md:321–322` 已明确记录有限域 Hessian 图。其 binary-covariant 候选不是字面相同的 $j$ 映射论文，故这里不夸大为同一定理的仓库成稿；但本入口并非新发现、也未绕开原有所有权。

**重要性与最强反对。** 几何构造内生地产生有限域算术动力学，原本是良好的对象筛选理由；直接文献和代数群商机制已占据所拟全问题，则是当前决定性反对。

**杀题条件／结论。** 主定理若只是重推已有 Lattès 半共轭、代入有限群周期公式或重枚举已描述的功能图，则淘汰。该条件已触发，故 `KILL_DIRECT_OWNER / INTERNAL_SCOUT_COLLISION`，没有新合同。

## 3. 不将廉价 CRT 事实晋升为论文

有限域有限测试集合上的多项式一致性，可通过标准根数界和 CRT／插值精确表达。但“有限观测不能唯一确定任意高次数映射”本身是经典插值事实；本轮未证明由此导致两个系统的全局周期 zeta 类型、目标算术或障碍等级发生指定分离。它不是第三个候选，也不是 A2 成果。

## 最终交接

算术续筛结束，不再扩展本报告的选题清单。当前没有 A1/A2 晋级证据，没有为补足五篇而退回来源侧经典公式。独立审查 root 的全双曲普通迹证明另存为同目录 `HYPERBOLIC_TRACE_ADMISSION_REVIEW.md`；那个审查通过与否不会改变本报告的 **0 个新算术准入合同**。
