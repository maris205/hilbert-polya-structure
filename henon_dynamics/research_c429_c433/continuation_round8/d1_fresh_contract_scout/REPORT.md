# R8 D1 — 不同子型有界筛选：无独立合同推荐

2026-09-10 UTC。本轮仅写本文件；最多两项完整问题，本次实际冻结一项。三批定向搜索、共十二个具体 query 已用完。未运行数学程序、启动 agent、调用外部模型/API、使用 GPU、修改 Git／共享文件／旧轮次或稿件。

## 1. 结论与实际排除范围

**推荐：none。** 找到一个有完整负向证明的 Hénon 全处周期点存在性问题，但扣除经典 intersective 多项式后，剩余只是一个短的实周期最大值／最小值实现。建议保留为辅助控制，不作为第五份独立合同；没有用“搜索未命中”或一个新的 yes/no 表述替代实质判断。

已实际读取 [ADMISSION_DECISIONS.md](../../ADMISSION_DECISIONS.md) 的四份合同及同篇扩展、[R6 X2](../../continuation_round6/x2_independent_replacement/REPORT.md) 全文和 [R7 裁决](../../continuation_round7/ROUND7_DECISION.md) 全文。范围扣除如下。

| 已有对象 | 本轮不重新打开或计数的内容 |
| --- | --- |
| PC424-L | 所有素数、所有 $d\ge2$、所有 $c$ 的 unicritical 普通周期和／多项式 coboundary 等式及有限证书；不把改变量名当成新桥 |
| UL4 | 小周期域满局部惯性、定向商稳定及后续最终商塔；不重述为新全局 Galois 合同 |
| OM4 | 最优周期测度、经典紧致支撑、$\mathbb Z_p$ 极限及 Haar 测度；本轮不再写其推论 |
| RLG5 | 全处多项式 reversor 存在但原数域不存在；不再次组合 Wang 类和同一中心化子扭转 |
| R6/R7 的未闭合支路 | M6 的初等饱和反例、Z6 的旧 Bridy 问题无全计数桥、一般 norm-one／CP 存在箭头、临界二周期 atom、tame 九周期均保持原状态，不另起副本 |

内部预筛还考虑了高维 additive-Livšic 改写和固定次数 integer-valued 有理周期限制。前者迅速落到非约化／纯不可分转移的初等障碍，不符合本轮排除简单 blindness 的要求，未冻结第二项问题；后者定点读到 [C1-UB3 原报告](../../lanes/c1_integer_valued_cubic/REPORT.md) 后，确认是已有未解合同，仍缺系数无关的离散约束，并无新桥。本轮没有把它们扩写成两份新课题。

## 2. 唯一冻结问题 HP8：各处存在周期点能否推出有理周期点？

### 对象、量词、时钟与成败标准

对每个 monic $P\in\mathbb Z[t]$、$\deg P\ge2$，考虑保守 generalized Hénon 自同构

$$
H_P(x,y)=(y,P(y)-x)
\quad\text{on }\mathbb A^2_{\mathbb Q}.
$$

其逆为 $(x,y)\mapsto(P(x)-y,x)$，Jacobian 为 $1$。对域扩张 $L/\mathbb Q$ 定义

$$
\operatorname{Per}_L(H_P)
=\{z\in L^2:\exists n\ge1,\ H_P^{\circ n}(z)=z\}.
$$

原生一 tick 是一次 $H_P$，不选取新 return clock。observable 是整个普通周期点集合是否非空，不是指定点的模素数约化，也不是 reversor、普通 zeta 或目标 Euler 因子。精确完整问题为

$$
\tag{HP8}
\left[\operatorname{Per}_{\mathbb Q_v}(H_P)\ne\varnothing
\text{ for every finite or infinite place }v\right]
\Longrightarrow
\operatorname{Per}_{\mathbb Q}(H_P)\ne\varnothing ?
$$

各处见证和周期允许随 $v$ 改变。正向答案必须覆盖全部显示的 $P$ 和全部原生周期。负向答案须给同一个允许的 $P$，在每个实际完备域中存在周期点，却排除所有有理点的所有正周期；仅有无有理固定点不够。

### 状态、策略与依赖

**完整负向结论：PROVABLE AS STATED，作者手证明；尚无独立非作者审查。** 原肯定命题 (HP8) 为假。下述证据不弱化其局部或全周期量词。

依赖顺序为：经典五次局部根例 → 每个完备域中真正的固定点 → 实数中的单次符号变号 → 有限周期序列的最大值／最小值 → 排除任意有理周期。原型最初写成不同的正二次因子；协调者指出只需符号而无需导数估计。来源核查后采用原文已有的最简因子，避免把这项改造误算成增量。

### 第一步：明确一个允许的映射

取

$$
G(t)=(t^3-19)(t^2+t+1),\qquad P(t)=2t+G(t).
$$

这是 monic 五次整数多项式。固定点方程恰为 $x=y$、$G(x)=0$。

### 第二步：逐处证明局部固定点，不把模素数根直接当成局部根

- 若素数 $\ell\equiv1\pmod3$，则 $\mathbb F_\ell^\times$ 有一个非平凡三次单位根 $u$。于是 $u^2+u+1=0$，且它是单根，因为 $\ell\ne3$。Hensel 引理给出 $\mathbb Q_\ell$ 中 $t^2+t+1$ 的根。这包含 $\ell=19$；也可直接用 $u=7$，因为 $7^2+7+1=57\equiv0\pmod{19}$、导数 $15\not\equiv0\pmod{19}$。
- 若 $\ell\equiv2\pmod3$，包括 $\ell=2$，则立方映射是 $\mathbb F_\ell^\times$ 的双射。由于 $\ell\ne19$，存在非零 $u$ 满足 $u^3=19$；导数 $3u^2$ 为单位。Hensel 引理给出 $t^3-19$ 在 $\mathbb Q_\ell$ 中的根。
- 对 $\ell=3$，令 $t=1+3z$，则

$$
t^3-19=9\bigl(z+3z^2+3z^3-2\bigr).
$$

括号内多项式在 $z=2$ 模 $3$ 为零，其导数模 $3$ 为 $1$。Hensel 引理给出 $z\in\mathbb Z_3$，从而给出 $t^3=19$ 的真正 $\mathbb Q_3$ 根。

- 在实处取 $\alpha=\sqrt[3]{19}$。

故每处 $v$ 都有 $a_v\in\mathbb Q_v$ 满足 $G(a_v)=0$，$(a_v,a_v)$ 是 $H_P$ 的固定点。局部证据比 (HP8) 要求的任意周期点更强，且覆盖了所有坏素数。

### 第三步：一次性排除全部非定常实周期

对所有实数 $t$，

$$
t^2+t+1=(t+1/2)^2+3/4>0,
$$

所以 $G(t)$ 的符号恰等于 $t-\alpha$ 的符号。无需断言 $G$ 单调。

任一实原生周期可写为有限循环序列 $(x_i)_{i\in\mathbb Z/n\mathbb Z}$，满足

$$
x_{i-1}+x_{i+1}=P(x_i)=2x_i+G(x_i).
$$

在达到最大值 $M$ 的位置有 $G(M)\le0$，故 $M\le\alpha$；在达到最小值 $m$ 的位置有 $G(m)\ge0$，故 $m\ge\alpha$。结合 $m\le M$ 得全部 $x_i=\alpha$。这个论证对每个 $n\ge1$ 都成立，包含重复坐标，不需任何预先周期上界。

因此

$$
\operatorname{Per}_{\mathbb R}(H_P)=\{(\alpha,\alpha)\}.
$$

若 $\alpha\in\mathbb Q$，则对其 $19$-进赋值有 $3v_{19}(\alpha)=1$，与整数值性矛盾。于是 $\operatorname{Per}_{\mathbb Q}(H_P)=\varnothing$，完整反驳 (HP8)。$\square$

### 为什么不推荐独立立项

这一全周期反例与 RLG5 的反演子存在性实质不同，也不是四份已接受定理的直接逻辑推论。但独立性不等于足够体量。经典来源已经明确给出 $G$ 的全部算术成分；新增实现只需把 $G$ 放入 $P-2t$，再用最大值／最小值排除其他实周期。其全局排除虽完整，却没有留下一个新的长程算术机制或完整分类难点。

尤其不建议通过以下方式扩大标签：增加同一正因子族、把同一个证明拆成各处／实处／有理处三项，或把经典五次极小性另算分类结果。Berend–Bilu 的小于五次结论针对“各处有根、无有理根”的多项式；它不自动证明在 (HP8) 的可变局部周期设定中，五次是最小反例次数。本轮不提出这个未证的更强结论，也不任意追加一个新限定分类来保住候选。

## 3. 已核原始来源与真正归属

| 来源及实际访问段落 | 提供什么；不提供什么 |
| --- | --- |
| Berend–Bilu, *Polynomials with roots modulo every integer*, Proc. AMS 124 (1996), 1663–1671；[作者上传全文](https://www.researchgate.net/publication/254468616_Polynomials_with_roots_modulo_every_integer)，实际读 Introduction、Theorem 1、Example 2、Remark 2、Example 3 | Theorem 1 给局部／Galois 判据；Example 2 明确给出 $(t^3-19)(t^2+t+1)$、$S_3$ 分裂域和坏素数处理；Remark 2 记录五次极小性。这些全部扣除。本次核读的这些段落不包含本报告的 Hénon 全周期结论；未把无此句误当成新颖性证明。 |
| Bergelson–Leibman–Lesigne, *Intersective polynomials and the polynomial Szemerédi theorem*，2008-07-01 [作者稿](https://people.math.osu.edu/leibman.1/preprints/isp.pdf)，实际读首页、§6.1 及对应参考文献 | 再次明确记载同一五次例及低次排除，并归于 Berend–Bilu；促成追溯原始所有权，不作为另一份新算术输入。 |
| Towsley, *A Hasse Principle for Periodic Points*，2013 年预印本版本 [arXiv:1209.2399v4](https://arxiv.org/pdf/1209.2399v4)，实际读摘要、Theorem 1、Corollary 1、邻近解释 | 它固定同一个全局有理点 $\alpha$，比较其全局周期性与各处／模素数周期性。HP8 各处点 $a_v$ 可以不同；不交换这两个量词。该结果不是 HP8 的正向定理，也不是本反例所推翻的命题。 |

AMS 原始 PDF 地址未能打开；CiteSeer 的原稿镜像发生重定向失败。随后成功访问作者上传的完整原文转写，并在实际 theorem/example 正文核查，不仅看摘要。没有下载文件。Hénon 开放问题综述的网页也已打开用于有界定位，但该页面的本轮 find 未返回相关段落；不据此断言它没有相应问题。泛查询中的 Pezda 报告介绍、无关同姓网页和百科均未用作证明来源。

本轮限定检索中未找到已核读的精确 Hénon 版先行表述。这个检索结果既不证明它新，也不改变上述“经典材料的短实现，辅助保留”的决定。

## 4. 三批实际搜索与执行记录

每批为一次包含四个具体 query 的定向搜索；后续只打开、定位这些来源，未追加第四批搜索。

1. `Hénon map local global principle periodic point every completion no rational periodic points`；`Henon map dynamical Hasse principle intersective polynomial periodic points`；`intersective polynomial x3 19 x2 x 1 S3 local roots`；`polynomial automorphism finite field periodic orbit sums Livsic polynomial coboundary`。
2. `"Hénon" "Hasse"`；`"periodic points" "every completion" polynomial`；`intersective polynomial "19" "degree 5"`；`intersective polynomial S3 least degree five x cubed 19`。
3. `Berend Bilu "Polynomials with roots modulo every integer" pdf`；`Henon "periodic" "intersective"`；`"polynomial automorphism" "local-global" "periodic points"`；`"rational periodic points" "locally" "Hénon"`。

本轮使用 idea-creator 的完整问题／淘汰框架、research-lit 的本地先读与原始来源核查、proof-writer 的真实量词与负向证明状态分离，以及项目 Hénon 批次规则。技能中的旧外部模型、广泛 pilot、API 抓取和独立默认输出文件均不执行：当前分配限定本团队、有界检索、纯理论、唯一 REPORT 路径。没有产生 novelty 分数，没有调用 agent 或数学探针。

## 5. 一个推荐的精确下一步

由协调者按需安排一次有界非作者核查，只核 §2 的全部坏素数 Hensel 提升、实周期全排除及 §3 的原文 Example 2 归属；若通过，把 HP8 存为辅助局部—整体控制并关闭这一候选，**不启动稿件、不增加合同数、不扩展参数表**。当前没有可推荐进入证明阶段的新独立合同，故不额外分配第二个猜想或数学程序。

本报告不改变 PC424-L／UL4／OM4／RLG5 或任何 R6/R7 缺口，也不提供目标 Euler 因子、根数、automorphy 或 Hilbert–Pólya 结论。`NO_BAD_EULER_OR_ROOT_NUMBER` 保持。
