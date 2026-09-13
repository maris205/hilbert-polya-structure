# Paper31：Picard–Fuchs forcing 与好纤维准确切触的独立数学审查 V1

日期：2026-09-12 UTC。审查者：`/root/p31_good_contact_independent_v1`。
身份：`FRESH_NON_AUTHOR / BOUNDED_MATHEMATICAL_REVIEW`。
`route_applicability: NOT_APPLICABLE`；`required_corrections: []`。

## 1. 结论及准确效力

**结论：新作者[G]的两条核心接口及 Hasse 简单零引理 PASS；新作者[C]的 C1–C4 全部 PASS，必要修正为 ∅。**
这是对两份实际冻结新稿的书面证明、关键有理恒等式及量词边界的独立核查。
旧[M]、[PF]和接受处置[D]仅作为已接受输入消费，不在本件重新投旧数学票。
此处 PASS 不是正式候选四门、新意、价值、长文容量、完整分类或 PDF 验收。

| 本轮新数学项 | 结论 | 本人核验核心 |
|---|---|---|
| [G] Gauss–Manin 还原和二阶 exact primitive | PASS | 两个多项式还原、消元符号、算子常数项 |
| [G] 完整 Picard–Fuchs forcing | PASS | 无穷远组合极部归零；两次 Leibniz 的全部移动端点 |
| [G] 全部实际 $p>3$ 的导数桥 | PASS | 独立正特征逐系数 C1–C4；未将积分方程模 $p$ 使用 |
| [G] $q\delta\ne0$ 上 Hasse 简单零 | PASS | $A=C=0$ 与单简单极点函数不可能性的矛盾 |
| [C] C1：Manin 根的准确重数 | PASS | 低阶导数项先排除 $p$ 次幂盲区，准确重数至多三 |
| [C] C2：全部真实 prime-to-characteristic 好切触 | PASS | 普通／超奇异不同阶；先证明 $i_n<p$ 再比较非零首项 |
| [C] C2：原 $t_O$ 首项、特征零及 $q=0$ | PASS | 参数首项不变；周期消去、复嵌入转移和好点排除 |
| [C] C3：素域初始交数 | PASS | 仅在旧素域充要性范围内应用 C2；点阶与倍数传播分开 |
| [C] C4：所有有限好点 Hasse 零阶 | PASS | $q=0$ 时 $A'=0$、$A''=\beta'C\ne0$ |

所有交数保持原基 $z=h-h_*$，原曲线、原截面 $P=(0,T)$ 与固定非零 $T$ 均未替换。
一般代数闭正特征域中的 $N_p$ 根不被本审查认定为真实切触的充分条件。
本件不处理节点、尖点、无穷远、$p$-primary 回返或全部固定理想。

## 2. 审查身份、本人实读及工具边界

本人是这两份新作者稿的非作者；未参与它们的推导、编辑或作者辅助。
未读取本轮节点作者稿、p-primary 作者稿或其他 fresh 报告，未与作者、作者 helpers、旧 reviewer 校准。
未委派辅助审查；本件关键公式、正特征系数和局部首项均由本人检查。
主控通信仅用于任务交付及进度，不据其其他席结论修订本判断。

按要求完整读取 research-review 技能。技能列明的 GPT-5.4 Codex MCP 审查工具未配置／不可调用；
实际使用已授权的可用 Codex 独立代理 xhigh fallback，而非声称调用该模型或建立跨模型复审。
`mcp_threadId: null`。技能使本件保留输入、逐项问题及最终修正清单；没有引入新实验或额外权限。
本任务的限定输出优先于技能默认的根目录报告、记忆更新及多轮作者对话，本件均未执行这些扩张动作。

### 2.1 本人 FULL 阅读的五份数学输入

| 输入 | 行数 | SHA-256 |
|---|---:|---|
| [G] 新 forcing 作者稿 | 267 | `c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b` |
| [C] 新好切触作者稿 | 281 | `7ec721bfac1d43f214dc9c8b3906c8bab131fe53b67fd6c48e06eeaa752f27aa` |
| [M] 原 Manin 接口 | 446 | `48029bd31748637edaa6a9a123cd0d525406ea5b65f7eab53799606a5c97dbe2` |
| [PF] 素域充要性 | 325 | `de9cdb5ee8fef26b50365e6794e148f7206c4c167738143fc28e77159b0debef` |
| [D] 旧接受处置 | 176 | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |

以上共 1495 行，均是本席实际全文读取，不继承上游 FULL 标签。
一次组合工具输出发生外层截断后，[PF]与[D]已分别重新完整输出并读完，未把截断当 FULL。
另 FULL 读取 `AGENTS.md`（28行）、`docs/WORKFLOW.md`（39行）及
`/root/autodl-tmp/.codex/skills/research-review/SKILL.md`（106行）。其实际 SHA-256 依次为
`73ff82bcf298285ef8c3b6a4d3e1dff80eedb7eeda93ea47a55334c862c43412`、
`b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2`、
`62859ebaa64be9915546b0ba8fb3464110bcfe015307fc33b15c97f03dc392a5`。

### 2.2 本人实际核对的一手来源

本次直接打开 [Ulmer–Voloch 官方 HTML v1][UV]，本人读取如下使用范围：

- §2 设置、$M,A,L$ 定义、(2.2)–(2.3)、Proposition 2.3 陈述及完整证明、Remark 2.4，页面归一化行 79–180。
- §4.5 的积分／周期说明，行 440–458；§4.10 至 Proposition 4.11 完整证明末尾，行 541–584。

源 §2 的消去和更细局部下界与[M]、[C]一致；这里只使用好约化局部部分，不调用全局处处半稳定结论。
源 §4.10 明确保留先微分被积函数、后在移动端点评价的项；[G]采用 $dX/(2Y)$，故规范为源 $dx/y$ 的一半。
这些是本席实际所读源段，不声称全文或 Manin／Broumas／Voloch 上游原文读取。
所读页面正文日期为 August 24, 2026；本件绑定实际 v1 URL 和读取范围，不解释历史日期差或另造版本身份。

## 3. [G] 的独立核验

以下沿用两新稿的 $a,b,s,q,H,\delta$，$f=X^3+aX+b$，以及
$\alpha=-\delta'/(12\delta)$、$\beta=-q/\delta$、$\gamma=a\beta/3$、$\kappa=\beta'/\beta$。
其中 $D$ 固定 $X$，不是对 $f(X_P(h),h)$ 的全导数。

### 3.1 多项式还原和消元：PASS

本人先按一般 $a,b,\alpha,\beta$ 展开[G]的两条多项式右侧，得到

$$
\begin{aligned}
2(\alpha+\beta X)f+2f(r_0)_X-f_Xr_0
&=(4a\alpha-6b\beta)X+6b\alpha+\tfrac43a^2\beta,\\
2(\gamma-\alpha X)f+2f(r_1)_X-f_Xr_1
&=(4a\alpha-6b\beta)X^2+(6b\alpha+\tfrac43a^2\beta)X.
\end{aligned}
$$

直接代入原族验证 $a'=-4a\alpha+6b\beta$、$b'=-6b\alpha-4a^2\beta/3$，
因此两式分别是 $-f_h$、$-Xf_h$。这给出真正的相对微分还原，而非预设积分满足方程。
同时 $r_1-Xr_0=2\beta f$，故 $R_1-XR_0=\beta Y$，其中没有少一个二因子。

再由第一条 Gauss–Manin 式微分并消去 $\omega_1$，准确得到

$$
(D^2-\kappa D-V)\omega=d_XQ,\quad
V=\alpha'+\alpha^2+\beta\gamma-\alpha\kappa,
$$

$$
Q=(D+\alpha-\kappa)R_0+\beta R_1
=\frac{2VX-\beta a'}{2Y}-\frac{r_0f_h}{4Y^3}.
$$

分子中的 $X^2$ 系数由 $\kappa=\beta'/\beta$ 消掉，$X$ 系数为 $2V$，常数为 $-\beta a'$。
算子常数项也可直接化为以下有限多项式身份：令 $K=8h^3-18h^2+9h-12T$，则

$$
12q\delta\delta''-q(\delta')^2-48aq^3-96\delta\delta'=144\delta K.
$$

因而 $-V=K/(q\delta)$，导数系数 $-\kappa=\delta'/\delta-8/q$；两者符号均与[G]一致。

### 3.2 无穷远端与移动端：PASS

取 $t=X^{-1/2}$、$Y=t^{-3}(1+at^4+bt^6)^{1/2}$，固定 $X$ 的微分也固定此 $t$。
$R_0=-\beta/t+\alpha t+O(t^3)$，$R_1=\alpha/t+\gamma t+O(t^3)$。
分别声称两者在 $O$ 为零是错误的；实际组合 $Q$ 的极部系数为

$$
-\beta'-(\alpha-\kappa)\beta+\beta\alpha=-\beta'+\kappa\beta=0.
$$

展开仅有奇次幂且无常数；亦可由 $Q$ 简式直接见 $Q=O(t)$，所以确有 $Q(O)=0$。
这同时确保闭周期上 exact 项积分为零，因此 $\mathcal L$ 杀掉周期。

本人两次对收敛积分应用 Leibniz 法则。第二次有两个来源不同的 $X_P'f_h(P)$ 项，最终边界为

$$
\frac{X_P''-\kappa X_P'}{2Y_P}
-\frac{2X_P'f_h(P)+(X_P')^2f_X(P)}{4Y_P^3}.
$$

本点 $X_P'=h/6$、$f_X(P)=-Th/2$、$f_h(P)=Th^2/12$，虽然 $Y_P'=0$，后一个固定 $X$ 偏导仍非零。
边界准确等于 $-h^3/(36T^2)+(1-\kappa h)/(6T)$，而
$Q(P)=h^3/(36T^2)+(\kappa h-1)/(6T)-H/(q\delta)$。
相加得到 $\mathcal LI=-H/(q\delta)$。源文 corrected endpoint 所警告的漏项在这里已真实处理。

### 3.3 原 $B$ 接口和正特征逐系数桥：PASS

本人直接核对 $B=(X_P'+r_0(P))/(2Y_P\beta)$。
记 $b_0=2h^2-3h-8T$，则所需短 forcing 恒等式可清成

$$
12\delta(b_0'q-8b_0)-qb_0(\delta'+qs)-12q^3T=24\delta H.
$$

这正是 $B'+(\alpha+\beta X_P)B+\beta Y_P=H/q^2$，仅用 $2,3$ 可逆。
因此其正特征使用不依赖任何特征零积分解释。

对每个实际 $p>3$，令 $F=f^{(p-1)/2}=X^pM+AX^{p-1}+L_{<}$，$C=[X^{p-2}]F$。
本人逐项检查[G]的系数步骤，而非由几个素数测试外推：

1. 在特征 $p$，$2fF_X+f_XF=0$。高次部分中 $AX^{p-1}$ 的贡献为 $AX^{p+1}$，
   $CX^{p-2}$ 的贡献为 $-CX^p$；余下低次项不进入商。因此
   $2fM_X+f_XM=C-AX$。
2. 用已核定多项式还原和 $(p-1)/2=-1/2$，有
   $F_h=(\alpha+\beta X)F+(r_0F)_X$。
3. 取 $X^{p-1}$ 系数时，导数项的系数带因子 $p$，故为零，给
   $A'=\alpha A+\beta C$。取 $X^p$ 商时，$AX^{p-1}$ 分别给 $+\beta A$ 与 $-2\beta A$，
   总计 $-\beta A$；$L_{<}$ 不贡献商，故[G]的 $M_h$ 式准确。
4. 对 $U=YM$，以上式子给 $2YU_X=C-AX$，而 $f_h$ 消去后给
   $U_h=r_0U_X-\beta AY$。这是独立的有限系数恒等式，不是对积分作不可分延拓。

沿原 $P$ 取全导数，用 $X_P'+r_0(P)=2Y_P\beta B$，再由
$\mu(P)=U(P)+B^p-AB$、$(B^p)'=0$，准确有

$$
\mu(P)'=-A\bigl[B'+(\alpha+\beta X_P)B+\beta Y_P\bigr]
=-\frac{AH}{q^2},\qquad N_p'=-q^{p-2}AH.
$$

后一式两边都是 $k[h]$ 中多项式；函数域恒等式已保证包括特殊时间在内的全多项式身份。
没有在 $q=0$ 的奇异消元系数上擅自逐点除法。

### 3.4 Hasse 引理及其在 C4 中的使用：PASS

若某光滑闭纤维 $A=C=0$，上一节第一式给 $d(YM)=0$。
代数闭常数域完美，$X$ 为可分变量，故该一变量函数域的微分核是 $p$ 次幂子域。
于是 $YM=v^p$。但 $M$ 首一、次数 $(p-3)/2$，故 $YM$ 唯一极点是 $O$，准确极阶 $p$。
$v$ 将只在 $O$ 有一阶极点，与 genus-one Riemann–Roch 的 $\ell(O)=1$ 矛盾。
所以每个有限好纤维都有 $A=0\Rightarrow C\ne0$。

这里的论证只用 $2fM_X+f_XM=C-AX$，不需 $q\ne0$；它可供[C]的 C4 使用，
虽然[G]主陈述的“简单零”特意限于 $q\delta\ne0$。在该开集上
$A'=\beta C\ne0$，简单零结论随即成立。

### 3.5 本人实际精确符号核算记录

本人另在内存中运行 SymPy 有理通分核验以下 16 个差式，输出全为准确的零：
$a'$、$b'$ 两关系；两条 G0；$R_1-XR_0$；G2 分子；PF 常数项；
$B$ 端点接口；$B$ forcing；$f_X(P)$；固定 $X$ 的 $f_h(P)$；$Q(P)$；完整移动端点；
完整积分 forcing；$\delta(9/8)$；$H(9/8)$。
另外输出并检查 §3.1 所列两条一般系数展开。
这是本人新执行的精确转录核对，不继承作者“八项成功”；书面代数与端点论证仍是证明主体。
未落地辅助脚本、未运行任何素数／扩域采样、未改作者输入。

## 4. [C] C1–C4 的独立核验

### 4.1 C1 的根重数与 $p$ 次幂盲区：PASS

在 $q_*\delta_*\ne0$ 的实际根处，$\mu(P)$ 正则且常数项为零。
写 $e=\operatorname{ord}A\in\{0,1\}$、$\epsilon=\mathbf1_{H_*=0}$；因为 $H'=3\ne0$，
导数式给 $\operatorname{ord}\mu(P)'=e+\epsilon=:j\le2$。
其首项迫使 $c_1=\cdots=c_j=0$ 且 $(j+1)c_{j+1}\ne0$。
由于 $j+1\le3<p$，这些系数可逆，任何正的 $p$ 倍指数都比它更大，不能藏在更低首项。
所以 $\operatorname{ord}N_p=1+e+\epsilon$；这个论证没有无条件套用 $\operatorname{ord}f'=\operatorname{ord}f-1$。

### 4.2 先给不除以 $i$ 的局部下界：PASS

设真实 $Q=nP$ 与 $O$ 切触，$w(Q)=cz^i+\cdots$、$i\ge2$。
短式直接给 $X=w^{-2}+O(w^2)$、$Y=-w^{-3}+O(w)$；负阶首项的系数固定为一，
故基系数微分除以 $2Y$ 后至少有 $w^5$ 阶，得到[C]的 D1。
由完整消去，$\mu(Q)=R_Q+\wp_A(D_Q)-\wp_A(E_Q)$，且

$$
R_Q=Cw+O(w^3),\qquad \operatorname{ord}D_Q\ge i-1,\qquad
\operatorname{ord}E_Q\ge i.
$$

其中 $Cw$ 的符号来自 $-CY/X^2=C/(wX)$；其余 $L_{<}$ 项至少是 $w^3$。
普通点由 $-AD_Q$ 得整体下界 $i-1$；超奇异点 $\operatorname{ord}A=1$，
而 $p(i-1)\ge i$，所以整体下界是 $i$。两下界均不要求 $p\nmid i$。

现在才利用 $p\nmid n$、$\mu(Q)=n\mu(P)$ 和 C1：
普通点给 $i-1\le1+\epsilon$，超奇异点给 $i\le2+\epsilon$。
两者均得 $2\le i\le3<p$。后续涉及 $i$ 的非零系数并非循环假设。

### 4.3 普通／超奇异的不同准确阶及原参数首项：PASS

现在 $i<p$，普通点唯一最低项是 $-AD_Q$，其准确值为

$$
\mu(Q)=-\frac{A_*ic}{\beta_*}z^{i-1}+O(z^i).
$$

超奇异点设 $a_1=A'_*$，则 $C_*=a_1/\beta_*$。
$R_Q$ 在 $z^i$ 的系数是 $a_1c/\beta_*$，$-AD_Q$ 在同次的系数是 $-ia_1c/\beta_*$，
因此确切为

$$
\mu(Q)=\frac{(1-i)a_1c}{\beta_*}z^i+O(z^{i+1}).
$$

$D_Q^p$ 的阶为 $p(i-1)>i$；$\wp_A(E_Q)$ 的阶至少 $i+1$，均不加入上述系数。
因 $i=2$ 或 $3$，两种最低项均非零，比较 C1 得 $i=2+\epsilon$。
这解释了为何实际切触时普通点的根重数是 $i-1$，超奇异点却是 $i$。

本人逐项比较导数 forcing 的四种积分首项与 $\mu(Q)=n\mu(P)$：

| 闭纤维状态 | $\mu(P)$ 首项 | 解出的 $c$ |
|---|---|---|
| $A_*H_*\ne0$ | $-A_*H_*z/q_*^2$ | $n\beta_*H_*/(2q_*^2)$ |
| $A_*\ne0,H_*=0$ | $-3A_*z^2/(2q_*^2)$ | $n\beta_*/(2q_*^2)$ |
| $A_*=0,H_*\ne0$ | $-a_1H_*z^2/(2q_*^2)$ | $n\beta_*H_*/(2q_*^2)$ |
| $A_*=H_*=0$ | $-a_1z^3/q_*^2$ | $n\beta_*/(2q_*^2)$ |

由 $\beta_*=-q_*/\delta_*$，这些就是[C]的 J。
原广义式参数 $t_O=-u/v$ 与短式 $w=-X/Y$ 满足 $w=t_O+O(t_O^2)$；
因此相交截面的首非零系数完全相同，未以分歧参数改变交数或偷偷改变首项规范。
唯一 $q=0$ 的好点由已接受[M]排除 prime-to-$p$ 切触，正特征 C2 没有漏掉它。

### 4.4 特征零、周期和嵌入转移：PASS

在复数好纤维附近，原 $\omega$ 的局部积分满足 $J_Q=w(Q)+O(w(Q)^5)$，
故若交数 $i\ge2$，$J_Q=cz^i+\cdots$。
局部 Abel 积分的群法则给 $J_Q-nI$ 是固定整系数的周期组合；[G]已由相对 exact 身份消去周期。
因此 $\mathcal LJ_Q=-nH/(q\delta)$，这一步没有将真实 $nP$ 换成其他 Betti leaf。

当 $q_*\ne0$，左侧首项是 $i(i-1)cz^{i-2}$。
右侧在 $H_*\ne0$ 时为非零常数，在 $H_*=0$ 时首项为 $-3nz/(q_*\delta_*)$，
故分别得 $i=2,c=-nH_*/(2q_*\delta_*)$ 和 $i=3,c=-n/(2q_*\delta_*)$。

当 $q_*=0$，先乘 $q$；所得等式在该好点正则。若 $i\ge2$，左侧常数为零，
右侧却是 $-nH_*/\delta_*\ne0$，因为
$H_*=(256T+27)/8$、$\delta_*=(256T+27)^2/4096\ne0$。
故这个好点在特征零也无切触。

一般代数闭特征零域不需整体嵌入 $\mathbb C$。
固定实际 $n,T,h_*$ 后，定义其有理坐标和待比较局部首项的有限数据位于某有限生成特征零子域；
该子域可嵌入 $\mathbb C$。注入保持有理函数在原 $z$ 的非零首系数、零阶及 $q\delta$ 非零条件。
上述复数结论因而逐个给出原量词的结论；这不是依赖全部常数域可嵌入的错误转移。

### 4.5 素域初始交数 C3 与全好点 Hasse 零阶 C4：PASS

C3仅使用旧[PF]已经接受的素域充分方向。
若 $p\nmid d$，$dP(h_*)=O$，所以 $N_p\ne0$ 强制 $i_d=1$；
$N_p=0$ 时 C2 给准确二阶或三阶，条件分别是 $H_*\ne0$ 或 $H_*=0$。
$d\nmid n$ 时不相交；$n=md$、$p\nmid n$ 时 $[m](w)=mw+O(w^2)$ 保持局部阶。
$p\mid d$ 时没有 prime-to-$p$ 的相交倍数。作者没有声称已求闭纤维点阶 $d$ 的统一闭式。

C4中，任意有限好纤维 $A_*=0$ 均由 §3.4 得 $C_*\ne0$。
$\alpha,\beta$ 只以 $\delta$ 作分母，故 $A'=\alpha A+\beta C$ 可在 $q=0$ 好点直接评价。
那里 $\beta_*=0$、$\beta'_*=-8/\delta_*\ne0$，于是

$$
A'_*=0,\qquad A''_*=(\alpha'A+\alpha A'+\beta'C+\beta C')_*=
\beta'_*C_*\ne0.
$$

因 $2$ 可逆，Hasse 零阶准确二；$q_*\ne0$ 时准确一。
这是“若该好点是 Hasse 零点”的分类，不断言每个 $q=0$ 好点必然超奇异。

## 5. 必要修正、开放边界和终态

必要修正：**∅**。本席未发现影响新[G]或[C]已列量词的逻辑缺口、符号错误或漏端点。
没有把书面正确的 C4 引理使用误记为缺证：其所需更广 $A=C=0$ 排除已由同一无分母的相对恒等式直接供应。

以下仍开放，但不是本轮定理内部的 GAP：

- 一般代数闭域中所有 $N_p$ 根的真实回返／切触充分性；全部切触位置及闭纤维点阶。
- 三阶真实切触的具体存在实例；$H=0$ 仅是发生三阶时的准确条件，未由候选线推出存在。
- $p\mid d$ 的初始交数、$p\mid n$ 的传播、坏纤维、无穷远及未审完整固定理想的其他消费者。
- 非标准新意、论文价值、22–30 页自然容量和完整项目准入；本任务明确不评价这些事项。

源 Manin 消去、相对 de Rham 还原、经典形式群和 Riemann–Roch 是所用标准机制；
本件只核查两份新稿在原族上的准确公式与消费者，不将标准机制重新授予新意。
旧接受、失败和产物状态均保持，不把本有界 PASS 计作 Paper31 已完成。

唯一新增为本报告，全部使用 `apply_patch`。
没有改作者稿、旧报告、候选登记、锁、索引或批次入口；没有新项目、论文、PDF、GPU、采样扩展或外部写入。
终态将本人全文回读，再回报实际行数及 SHA-256；不在文件中递归自载其哈希。

[G]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[C]: PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[D]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1
