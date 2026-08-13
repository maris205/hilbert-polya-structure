# Paper 4 algebraic action-clock source lock：独立反例审计

**独立性记录（未读文件）.** 本审计没有读取 `notes/PROOF_PACKAGE.md`、`notes/DERIVATION_PACKAGE.md`、`notes/COUNTEREXAMPLE_AUDIT.md`、`notes/NOVELTY_AUDIT.md`、`notes/RESEARCH_QUESTION.md`、`experiments/source_lock.json` 或 `experiments/EXPERIMENT_PLAN.md`。没有访问或生成 prime/zero 数据，也没有运行候选周期轨道或 action 实验；以下只使用任务消息给出的冻结命题及形式代数验算。

**结论：REPAIR（核心定理 PASS；越过下列边界的推广 FAIL）.** 在 $P\in X(\overline{\mathbf Q})$、逐步定义域安全、$G\in\overline{\mathbf Q}(X)$ 单值有理且所有允许常数属于 $\overline{\mathbf Q}$ 时，$A_G(P)\in\overline{\mathbf Q}$ 是直接且无条件正确的；Hermite--Lindemann 后果也正确。Hénon 的符号、生成函数、有限周期点代数性和“仅 $3A$ 必为 $S$-整数”均可证明。必须修复或明说的地方是：

1. gauge 必须限定为单值的 $\overline{\mathbf Q}$-有理 gauge（或逐点明确保证所有 gauge/transition 值代数）；对数 gauge、解析多值 primitive 和未受控 monodromy 不在定理内。
2. 时间/图册 gauge 的一般移位是

   \[
   A'-A=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j,
   \]

   只有端点 gauge 在端点识别下兼容时，首项才消失。
3. “complex logarithm”应精确写为：若 $\beta\in\overline{\mathbf Q}^{\times}$ 且 $e^A=\beta$，则唯一可能是 $A=0,\beta=1$。$\beta=0$ 没有复对数；不能把 $|A|\ne\log p$ 偷换成 $\log|A|\ne\log p$。
4. $S$-整性陈述须令数域包含 $a$ 和轨道坐标；若先在较小数域 $K_0$ 给出 $a$，则应在轨道域 $K/K_0$ 及 $S$ 在 $K$ 上的延拓中陈述。
5. $n=1,2$ 的循环递推中左右邻居重合但必须按两次计数；不能把重复邻居去重。

**精确 stop conditions.** 出现下列任一情形时，不得宣称冻结的 source lock：某一步 $F(P_j)$ 未定义；任一被求值的 $G_j,\chi_j$ 或 transition 在相应点有极点；只知道 $F^*\theta-\theta$ 闭而没有全局单值有理 primitive；使用含 $\log$ 的多值 primitive/gauge 而未证明闭环 monodromy 为零；任一实际进入 action 的常数、端点差或分支跳跃不在 $\overline{\mathbf Q}$；常数按目标或轨道拟合且允许超越值；把结论应用于 $\log|A|$；或在未证明周期点零维/代数时删去代数轨道假设。端点不匹配若其差仍在 $\overline{\mathbf Q}$，只应停止使用“移位恰为 $\sum C_j$”这一公式，source lock 本身仍保留。

## 1. 核心代数值锁：独立证明

令 $P_j=F^j(P)$。有理映射 $F$ 定义在 $P_j\in X(\overline{\mathbf Q})$ 时，其像仍是 $\overline{\mathbf Q}$-点。因此由归纳法，逐步定义域假设给出

\[
P_j\in X(\overline{\mathbf Q}),\qquad 0\le j<n.
\]

若 $G\in\overline{\mathbf Q}(X)$ 在 $P_j$ 正则，则有理函数求值 $G(P_j)\in\overline{\mathbf Q}$。于是

\[
A_G(P)=\sum_{j=0}^{n-1}G(P_j)\in\overline{\mathbf Q}.
\]

这个最短证明甚至没有使用 $F^*\theta-\theta=dG$ 或周期性；后二者赋予该和“闭轨 action/gauge”含义，但在已经假设代数轨道时并非代数值结论所需。

Hermite--Lindemann 的适用形式是：非零代数数 $\alpha$ 的 $e^\alpha$ 是超越数。因此，对 $A\in\overline{\mathbf Q}$，

\[
e^A\in\overline{\mathbf Q}\quad\Longrightarrow\quad A=0,\quad e^A=1.
\]

故若 $\beta\in\overline{\mathbf Q}^{\times}\setminus\{1\}$，$A$ 不可能是 $\beta$ 的任何复对数；这与对数分支无关，因为所有分支都满足 $e^A=\beta$。对于 $\beta=1$，只有零分支 $A=0$ 可能是代数数，非零的 $2\pi i k$ 分支仍不可能。

复共轭保持 $\overline{\mathbf Q}$，所以

\[
\Re A=\frac{A+\overline A}{2},\qquad
\Im A=\frac{A-\overline A}{2i},\qquad
|A|^2=A\overline A
\]

均为代数数，且 $|A|$ 是代数方程 $T^2-A\overline A=0$ 的非负实根，也属于 $\overline{\mathbf Q}$。对素数 $p>1$，实数 $\log p$ 非零且超越，故

\[
\Re A\ne\log p,\qquad \Im A\ne\log p,\qquad |A|\ne\log p.
\]

这里没有关于 $\log|A|$ 的排除结论。事实上 $A\ne0$ 时

\[
\log|A|=\log p\quad\Longleftrightarrow\quad |A|=p,
\]

后者完全可能发生，例如零维恒等系统取代数常数 $G=p$。同理，
$\Re(\operatorname{Log}A)=\log|A|$ 也不受本 source lock 排除。

## 2. 攻击一：超越、目标依赖和事后选择的常数

导数方程只在常数模掉以后确定 primitive。若把允许的系数域从 $\overline{\mathbf Q}$ 放宽到 $\mathbf C$，结论立即失败。最小反例为

\[
X=\operatorname{Spec}\overline{\mathbf Q},\quad F=\mathrm{id},\quad
\theta=0,\quad G=0,\quad n=1.
\]

把 primitive 改成 $G'=G+C$，其中 $C=\log p$，仍有 $dG'=0=F^*\theta-\theta$，但 $A_{G'}=\log p$。若先观察某条轨道的 $A$ 后拟合，则取

\[
C=\frac{\log p-A}{n}
\]

会强制 $A'=\log p$。所以“冻结”本身不够：一个在看轨道前就冻结的 $C=\log p$ 仍会破坏最小反例；真正的数学锁是 $C\in\overline{\mathbf Q}$。反过来，即便在看轨道或目标后才选择，只要实际选择仍属于 $\overline{\mathbf Q}$，代数值结论不会失败。因而“轨道前冻结”是防止数据拟合和保证定义统一的协议条件，$\overline{\mathbf Q}$-值才是逻辑条件。

全局 gauge

\[
\theta'=\theta+d\chi,\qquad
G'=G+\chi\circ F-\chi+C
\]

满足

\[
F^*\theta'-\theta'=dG'.
\]

在所有求值都有限时，闭轨上

\[
\sum_{j=0}^{n-1}G'(P_j)
=A_G+\chi(P_n)-\chi(P_0)+nC=A_G+nC.
\]

若 $\chi\in\overline{\mathbf Q}(X)$、$C\in\overline{\mathbf Q}$，新 action 仍为代数数。若 $C$ 超越，则没有 source lock。

## 3. 攻击二：局部 $C_j$ 与端点 mismatch

令 $P_{j+1}=F_j(P_j)$，并令

\[
G'_j=G_j+\chi_{j+1}\circ F_j-\chi_j+C_j.
\]

逐项求值后只有如下完整公式：

\[
\begin{aligned}
A'-A
&=\sum_{j=0}^{n-1}
  \bigl(\chi_{j+1}(P_{j+1})-\chi_j(P_j)+C_j\bigr)\\
&=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j.
\end{aligned}
\]

即使 $P_n=P_0$，也不能只凭“几何端点相同”删去前两项；还需端点 identification 下的 gauge compatibility，至少要求

\[
\chi_n(P_n)=\chi_0(P_0),
\]

更自然的图册陈述是端点邻域上的两个 gauge germ 相同。若不兼容，正确移位含

\[
\Delta_{\mathrm{end}}=\chi_n(P_n)-\chi_0(P_0).
\]

若所有 $\chi_j,C_j$ 均为 $\overline{\mathbf Q}$-有理且安全求值，则 $\Delta_{\mathrm{end}}$ 仍是代数数，所以 algebraic source lock 继续成立，只是“移位等于 $\sum C_j$”这句失败。若 mismatch 是超越常数或分支跳跃，source lock 也失败。零维恒等系统中取 $G_j=C_j=0$、$\chi_0=0$、$\chi_n=\lambda$，便有 $A'-A=\lambda$；令 $\lambda=\log p$ 就得到目标反例。

每一个局部或逐步常数都必须进入账本。中间端点之所以消去，是因为相邻两步使用了同一个 $\chi_j$ 的同一个值；若图册实现实际上选了不同 branch/germ，则其差是额外 transition constant，不能假装已经 telescoping。

## 4. 攻击三：closed 不等于 rationally exact

若只把假设降为 $F^*\theta-\theta$ 闭，则全局单值有理 $G$ 可能不存在。一个完全代数的例子是

\[
X=\mathbf G_m,\qquad F(x)=x^3,\qquad
\theta=\frac12\frac{dx}{x}.
\]

于是

\[
F^*\theta-\theta=\frac{dx}{x}.
\]

该微分闭，但不是任何有理函数的微分，因为 $dx/x$ 在 $x=0$ 的留数为 $1$，而有理函数的全微分在每一点留数为零。其局部解析 primitive 是 $\operatorname{Log}x$。代数点 $P=-1$ 是 $F$ 的不动点，但任一局部对数值为

\[
(2k+1)\pi i,
\]

不是代数数。故“closed + local primitive”版本直接 FAIL。冻结定理必须保留“存在 $G\in\overline{\mathbf Q}(X)$ 且 $dG=F^*\theta-\theta$”这一全局 rational exactness；仅有解析局部 exactness 不够。

## 5. 攻击四：多值/对数 gauge 与 monodromy

即使 $d\chi=dh/h$ 是代数有理 $1$-form，
$\chi=\operatorname{Log}h$ 也不是 $\overline{\mathbf Q}$-有理函数。沿闭环解析延拓可以产生

\[
\chi_{\mathrm{end}}-\chi_{\mathrm{start}}=2\pi i\,m,\qquad m\in\mathbf Z.
\]

这正是上一节的端点 mismatch；当 $m\ne0$ 时它是超越数。最小演示是在 $X=\mathbf G_m,F=\mathrm{id},\theta=G=0$ 上使用 $\chi=\operatorname{Log}x$：如果端点 branch 相对起点多绕一周，形式 telescope 留下 $2\pi i$，而不是零。离散轨道本身并不自带一条决定 winding number 的连续路径，因此若允许这种 gauge，action 甚至在给定离散轨道后仍未被唯一确定。

可接受的两种修复只有：

1. 定理中完全禁止多值 gauge，只允许单值 $\overline{\mathbf Q}$-有理 $\chi_j$；或
2. 另立带路径/局部系统的定理，显式记录所有 period，并逐一证明闭环总 period 为零或为代数数。

若总 period 非零且含 $2\pi i$ 或代数数的对数，原 source lock 不可宣称。

## 6. 攻击五：极点与不定点

“$F^n(P)=P$”必须表示逐步轨道存在，不能只表示经过有理式消去后的复合映射在 $P$ 有值。例如在 $X=\mathbf A^1$ 上取有理映射 $F(x)=1/x$。作为有理映射有 $F^2=\mathrm{id}$，但在 $P=0$ 处第一步不存在；因此不能把 $F^2(P)=P$ 当成一条长度二的轨道。

极点也不能用形式消去掩盖。例取

\[
F(x)=2x,\qquad \theta=2\frac{dx}{x^2},\qquad G=\frac1x.
\]

在函数域上确有

\[
F^*\theta-\theta=-\frac{dx}{x^2}=dG,
\]

而 $P=0$ 是 $F$ 的不动点；但 $G(P)$ 和 $\theta(P)$ 均无定义，故 action 不是一个复数，更不是一个可应用 Hermite--Lindemann 的代数数。类似地，若 $\chi(P_j)$ 有极点，不允许把闭轨 telescope 写成形式上的“$\infty-\infty=0$”。若某个组合后的 $G'_j$ 经有理函数恒等式延拓为正则函数，可以直接用延拓后的 $G'_j$ 定义 action；但此时不能再使用由各个未定义项逐点求值得到的 telescope 证明。

对单纯的 $A_G\in\overline{\mathbf Q}$ 而言，$\theta$ 在轨道上正则并非必要，因为 action 不求值 $\theta$；但若要解释 pullback、变分或 gauge，冻结命题采用更强的“所有被求值数据安全”是合理且稳健的。

## 7. 攻击六：复对数分支、实部、虚部、模与对数模

分支无关的正确对象是指数方程 $e^A=\beta$，而不是某个未说明 branch 的符号 `log`。冻结结论对 $\beta\in\overline{\mathbf Q}^{\times}\setminus\{1\}$ 的每个 branch 都成立；对 $\beta=1$ 必须保留 $A=0$ 的平凡例外；对 $\beta=0$ 则根本不存在复对数。

对实素数 $p>1$，$\Re A,\Im A,|A|$ 都是代数实数，所以均不等于 $\log p$。以下推论则不成立，必须明确列为越界：

* $\log|A|\ne\log p$；
* $\Re(\operatorname{Log}A)\ne\log p$；
* “$A$ 的辐角必为代数数”。

第一、第二条在 $|A|=p$ 时就是假命题；第三条也不由 $A$ 的代数性推出。

## 8. 攻击七：Hénon 专化的符号和周期点代数性

令

\[
H_a(q,p)=(Q,P)=(q^2-a-p,q),\qquad \theta=p\,dq.
\]

直接计算

\[
H_a^*\theta=P\,dQ=q(2q\,dq-dp),
\]

从而

\[
H_a^*\theta-\theta=(2q^2-p)\,dq-q\,dp
=d\left(\frac23q^3-pq\right).
\]

所以给定的

\[
G=\frac23q^3-pq
\]

符号正确。对

\[
L(q,Q)=\frac13q^3-aq-qQ
\]

有

\[
\partial_qL=q^2-a-Q=p,\qquad -\partial_QL=q=P.
\]

并且在 $Q=q^2-a-p$ 的图上

\[
L=\frac13q^3-aq-q(q^2-a-p)
=-\frac23q^3+pq=-G.
\]

这也符合 $dL=p\,dq-P\,dQ=\theta-H_a^*\theta=-dG$。没有符号错误。

沿轨道 $p_j=q_{j-1}$，故

\[
q_{j+1}+q_{j-1}=q_j^2-a.
\]

循环下标在低周期必须保留重数：

\[
n=1:\quad 2q_0=q_0^2-a;
\]

\[
n=2:\quad
2q_1=q_0^2-a,\qquad 2q_0=q_1^2-a.
\]

若从 $\sum_jL(q_j,q_{j+1})$ 取变分，同一个变量在 $n=1,2$ 时通过不同 argument slot 出现两次；把“相同邻居”去重会得到错误方程。

### 有限周期点为何确实全都代数

仅说“周期方程的系数代数”不够；若解集有正维分支，它会含有坐标超越的复点。这里可用循环递推严格证明零维。长度 $n$ 的周期点等价于仿射 $n$-元方程

\[
q_j^2-q_{j+1}-q_{j-1}-a=0,\qquad j\in\mathbf Z/n\mathbf Z,
\]

其中 $n=1,2$ 按上面的重复邻居计数。引入同一齐次坐标 $Z$，在 $\mathbf P^n$ 中齐次化为

\[
Q_j^2-ZQ_{j+1}-ZQ_{j-1}-aZ^2=0.
\]

若 $Z=0$，所有方程给出 $Q_j^2=0$，故全部 $Q_j=0$，这不是射影点。因此该射影闭集没有无穷远点，完全包含在仿射 chart $Z\ne0$ 中。一个同时为射影且仿射的有限型代数簇只能是零维；故周期解集有限。其方程定义在 $\overline{\mathbf Q}$ 上，零维复点的每个坐标都代数于 $\overline{\mathbf Q}$，因 $\overline{\mathbf Q}$ 已代数闭，实际均属于 $\overline{\mathbf Q}$。最后置

\[
(q,p)=(q_0,q_{n-1})
\]

即可恢复 Hénon 周期点。这个论证也解释了为什么“无无穷远点”必须在正确的齐次循环系统中验证，不能只凭多项式动力学的口头印象断言零维。

## 9. 攻击八：$S$-整 valuation 论证与分母 $3$

精确陈述应为：取包含 $a$ 及全部轨道坐标的数域 $K$，取有限 places 集 $S$（通常含所有无穷 places），并假设 $a\in\mathcal O_{K,S}$。对任一有限 place $v\notin S$，若某个 $q_j$ 有负 valuation，令

\[
m=\min_j v(q_j)<0
\]

并取达到最小值的 $j$。递推给出

\[
q_j^2=q_{j+1}+q_{j-1}+a.
\]

左侧 valuation 为 $2m$，而非 Archimedean 三角不等式给出

\[
v(q_{j+1}+q_{j-1}+a)
\ge\min\{v(q_{j+1}),v(q_{j-1}),v(a)\}
\ge m.
\]

由于 $m<0$，有 $2m<m$，矛盾。因此每个 $q_j\in\mathcal O_{K,S}$，而 $p_j=q_{j-1}$ 也为 $S$-整数。$n=1,2$ 的重复邻居只会出现整数系数 $2$，不破坏该 valuation 论证。

逐项有

\[
3G(q_j,p_j)=2q_j^3-3p_jq_j\in\mathcal O_{K,S},
\]

所以

\[
3A_G(P)\in\mathcal O_{K,S}.
\]

一般不能消去 $3$。形式上的一周期例子是

\[
q=p=1,\qquad a=-1,\qquad A_G=\frac23-1=-\frac13.
\]

它满足固定点方程 $2q=q^2-a$。在 $K=\mathbf Q$ 且 $3$ 未被放入 $S$ 时，$3A_G=-1$ 是 $S$-整数而 $A_G$ 不是。只有当所有 $3$ 上方的素位都在 $S$ 中（使 $3$ 成为 $S$-单位），或另有逐轨道可证明的三整除性时，才能加强到 $A_G\in\mathcal O_{K,S}$。

若最初只给 $a\in\mathcal O_{K_0,S_0}$，而周期点定义在扩张 $K/K_0$，则正确版本是坐标属于 $\mathcal O_{K,S}$，其中 $S$ 至少包含 $S_0$ 上方的 places；不能把不属于 $K_0$ 的坐标直接称作 $K_0$ 中的 $S_0$-整数。

## 10. 攻击九：代数轨道假设是否必要、是否充分

**充分，而且在当前表述中有冗余。** $P\in X(\overline{\mathbf Q})$、$F$ 定义在每一步且定义在 $\overline{\mathbf Q}$ 上，已经自动推出整条有限轨道代数；再由 $G\in\overline{\mathbf Q}(X)$ 的安全求值得到 $A$ 代数。无需另加“轨道代数”作为独立假设。反过来，直接假设所有被求值的 $G(P_j)$ 代数也已足够，哪怕某些 $P_j$ 本身不是代数点。

**对单个系统而言并非必要。** 最简单地，$F=\mathrm{id}$、$G$ 为代数常数时，任意坐标超越的复点都是周期点且 action 仍为代数数。

更强的是，在保留 exactness 和周期性时，通常连这个平凡例子也不需要：在所有迭代都定义的公共开集上令

\[
A_n(x)=\sum_{j=0}^{n-1}G(F^j x).
\]

则

\[
dA_n=\sum_{j=0}^{n-1}(F^j)^*dG
=(F^n)^*\theta-\theta.
\]

把它限制到固定点 locus $Z=\{F^n x=x\}$ 的任一约化不可约分支，右侧限制为零。因此在特征零下，$A_n|_Z$ 是常数；所有数据定义在 $\overline{\mathbf Q}$ 上且基域已经代数闭，该常数属于 $\overline{\mathbf Q}$。所以即便一个正维固定分支含坐标超越的复点，只要所有求值安全，action 仍可因 exactness 而锁为代数常数。

这一加强不是冻结命题成立所必需，建议正文使用简单、透明的“代数点逐项求值”证明；若删除 $P\in X(\overline{\mathbf Q})$，则必须另行写出上述固定 locus/零微分论证，不能无证明地删假设。

## 11. 最终 claims matrix

| 情形 | $A\in\overline{\mathbf Q}$ | 闭轨移位公式 | 可排除 $\log p$ |
|---|---:|---|---:|
| 全局 $G,\chi$ 单值 $\overline{\mathbf Q}$-有理，安全求值，$C\in\overline{\mathbf Q}$ | 是 | $A'=A+nC$ | 是 |
| 逐步 gauge，端点兼容，所有 $C_j,\chi_j$ 代数有理 | 是 | $A'=A+\sum C_j$ | 是 |
| 逐步 gauge，端点不兼容但端点差代数 | 是 | 必须加 $\Delta_{\rm end}$ | 是 |
| 任一实际 shift 为超越数或目标拟合值 | 否 | 数值上仍可记账，但无 source lock | 否 |
| 只有 closed、没有全局 rational $G$ | 无法推出 | 局部 primitive 有 period | 否 |
| 对数/多值 gauge 且 monodromy 未清零 | 无法推出 | 必须加 $2\pi i m$ 等 period | 否 |
| 任一步不定或任一求值有极点 | action 未定义 | 不可 telescope | 不适用 |
| $A\in\overline{\mathbf Q}$，考察 $\Re A,\Im A,|A|$ | 是 | 不涉及 | 均不等于实 $\log p$ |
| $A\in\overline{\mathbf Q}^{\times}$，考察 $\log|A|$ | 通常超越 | 不涉及 | 不能排除等于 $\log p$ |

综上，冻结候选的核心 arithmetic source lock 可以保留；发表级版本应把 gauge 的函数类别、端点差、定义域、对数的精确域以及 $S$-整数所在数域写进定理，而不是只留在口头约定中。
