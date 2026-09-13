# Paper30：第三 forcing 上半高系数完整移位段独立核查 V1

日期：2026-09-08。审查者：`/root/negative_upper_high_review`。
本审查者未参与目标稿的推导、作者协作或文字修改；仅写本报告。
已完整读取并使用 `proof-writer`，全文审查以下冻结作者稿的 544 行。

- 目标：[UPPER_HIGH_CRITICAL_PROBE_V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_HIGH_CRITICAL_PROBE_V1_20260908.md)。
- 绑定 SHA256：`a1788d54a7e400c688c47af00e4f6bbab413b56fbfc1f137a446f17c1492ec77`。
- 作者侧子检查未被援引为本次独审证据。

## Claim

固定任意素数 $p\ge5$、整数 $a\ge2$，保持目标稿规定的同一实际双谐波递推、
传播子负号及幅度规范。令

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=3m+1=p+m,
\qquad e_*=M-D,
$$

且 $C_j=[L^j]\mathcal B_3$。审查的原结论为

$$
pC_j\in h^{2m}\mathcal O^+\quad(p<j\le D),
\qquad \overline{h^{-m}pC_{D-1}}=0.
$$

在既有分解

$$
h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
P_{\rm cl}=L^m+\sum_{i<m}b_iL^i,\quad b_i\in h\mathcal O^+,
\qquad U_{\rm cl}=\sum_{r=0}^p u_rL^r
$$

下，还审查

$$
u_r\in h^{e_*+2m}\mathcal O^+
=h^{M-m-1}\mathcal O^+\quad(m+2\le r\le p).
$$

不把 $j=p$、准确赋值、非零剩余、完整负 Newton 图或负因子型并入结论。

## Status

**PASS — PROVABLE AS STATED。**

原结论在原量词和原范围内成立，无须增加假设或削弱结论。
本报告是目标冻结稿的全文独立数学核查，不是论文、PDF、Route 或批次终局验收。

## Assumptions

本次只使用以下既有输入，不重开未变的旧审查：

1. [首层内部结构稿](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
   的式 (3)：$h^mV_p(L)$ 逐系数整。目标稿中的幅度齐次性将它转为全部第一次内部初值的界。
2. 同稿 Step 4、式 (15) 是真正的形式身份
   $$
   \mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L),
   \quad R,T\in\mathbb Z_p[L][[H]],\quad \chi=(-1)^{m+1},
   $$
   且 $L$ 次数有统一有限界。本审查已直接读取原式，而非只依据目标稿的转述。
3. [当前接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_AND_POSTCRITICAL_DISPOSITION_20260908.md)
   中固定次数首一分解及 $b_i\in h\mathcal O^+$。
4. 实际局部规范给出 $v_h(p)=M$、$v_h(d_p)=v_h(d_{2p})=2m$；
   其余正权重小于 $3p$ 的传播子均为单位。$p\ge5,a\ge2$ 保证
   $3p<p^a$ 及 $M\ge5m$。

旧次高作者稿、作者侧协作检查及旧最高项证明均不是本证明闭合所需的新依赖。
既有最高项较强界没有被本次核查降级。

## Notation

$t=bx$、$u=Lx^2/4$，保留窗口为 $t^p=0$、$\deg_x<3p$。
$\mathscr N=t\partial_t+2u\partial_u$、$\mathscr S=t\partial_t+u\partial_u$。
$\widetilde V$ 指全部内部初值指定为零后的辅助分支；$w$ 是权重小于 $p$ 的低块。
$\tau$ 是先乘 $p$ 后的 $u^p$ 高带。
$\mathsf S_n$ 表示 Chebyshev 配套多项式，不与 $\mathscr S$ 混用。
本报告中 $\lambda(H)=\chi H^m(4-H)^{m+1}$ 表示移位标量，
不是实际物理参数 $L/\rho$。

## Proof Strategy

逐段检查从实际分支到形式辅助分支再返回实际环的完整链条：
先核实每个内部初值及其污染的最坏赋值，再核实唯一非单位阶乘的正规化，
随后独立推导 Chebyshev 移位与 Ward 身份，最终检查端点压缩、形式理想保持及商转移。
不使用根拟合、逐素数扫描或计算成功替代一般证明。

## Dependency Map

1. 实际初值界 $\Rightarrow$ 实际／辅助指数误差属于 $h^{-3m}$。
2. 完整截断及辅助整性 $\Rightarrow$ 单阶乘清除、$pR$ 整和准确高带方程。
3. Chebyshev 加法与形式 Ward 身份 $\Rightarrow$
   $\tau=-\mathscr Nw+\lambda(H)(H\partial_H-\mathscr S)w\pmod{p,H^{2m}}$。
4. 两端点配对与第一 forcing 的形式输入 $\Rightarrow$
   $p\widetilde C_j\in(H^{2m},p)$。
5. $M-3m\ge2m$ $\Rightarrow$ 同一结论返回实际 $C_j$。
6. 首一分解的递降三角比较 $\Rightarrow$ 指定商系数的高度。

## Proof

### 1. 截断与全部内部初值：PASS

删除 $t$ 次数至少为 $p$ 或 $x$ 权重至少为 $3p$ 的单项式确实定义理想。
保留区域对取乘积因子下降封闭，故被删除项不能向保留系数回流。
递推中的 $t$ 与 $u$ 分别升权重一与二，且传播子按权重对角作用；
按权重归纳即得幅度齐次性和截断相容性。

第一次内部节点恰为 $t^ku^{(p-k)/2}$，$k=1,3,\ldots,p-2$；
第二次恰为 $t^ku^{p-k/2}$，$k=0,2,\ldots,p-1$。
第一内部节点的 $k=p$ 已被明确删除；窗口内未遗漏任何其余非单位传播子。
齐次缩放只引入 $4$ 的单位幂，因此既有 $h^mV_p$ 整给出每个
$v_h(q_{1,k})\ge-m$。

纯偶第二内部值 $W_p=q_{2,0}$ 的源项只取 $u^{p-1}$，其背景和阶乘整，
所以 $v_h(q_{2,0})\ge-2m$。
其余第二内部源项权重为 $2p-1$ 或 $2p-2$，不可能含两个第一次内部值。
在 $t^p=0$ 下

$$
e^{\alpha V}=e^{\alpha W}
\sum_{\ell=0}^{p-1}\frac{\alpha^\ell(V-W)^\ell}{\ell!}
$$

把正 $t$ 部分的阶乘限制在 $\ell<p$；权重小于 $2p$ 的纯偶背景又只需
$u$ 次数小于 $p$。单位三角递推遂给第一内部值的整系数仿射依赖。
第二内部源项至少为 $h^{-m}$，除以 $d_{2p}$ 后确得
$v_h(q_{2,k})\ge-3m$。本段没有遗漏两个第一次初值的潜在乘积；
它们只是尚未进入第二内部源项的权重。

### 2. 实际／辅助误差及最小素数精度：PASS

辅助分支中全部 $u$ 次数小于 $p$ 的系数整，理由正是上式的双因子展开与单位递推；
不能仅以总权重小于 $2p$ 直接声称所有原始阶乘是单位，目标稿没有这样使用。

将所有内部初值暂作独立变量是合法的三角参数化。$\Delta=V-\widetilde V$ 始于权重 $p$，
所以在目标窗口中指数差准确为

$$
e^{\alpha\widetilde V}\left(\alpha\Delta+\frac{\alpha^2}{2}\Delta^2\right).
$$

每个含 $\Delta$ 的乘积所需背景权重严格小于 $2p$，已由辅助整性覆盖。
只有内部初值的一次项和两个第一次初值的乘积可能保留；
含第二次初值的二次项及三次项均在窗口之外。
这些项的赋值分别至少为 $-3m$、$-2m$。因此目标式 (16)—(17) 成立。

尤其 $M-3m\ge2m$，且只在 $(p,a)=(5,2)$ 取等号。
误差在此边界仍属于需要消去的 $h^{2m}$ 理想，但不支持统一模 $h^{2m+1}$。
作者稿准确保留了这一精度限制。

### 3. 完整单阶乘带正规化：PASS

对窗口内每个 $t^ku^r$，

$$
k+r\le\frac{(3p-1)+(p-1)}2=2p-1.
$$

无常数指数因子的个数不超过 $k+r$。因此辅助低 $u$ 部分 $T$ 整时，
$pe^{\alpha T}$ 的每个保留系数整，至多清除一个 $p$。
$R=\widetilde V-T$ 始于 $u^p$，$R^2$ 的权重至少 $4p$，
故目标式 (19) 是本窗口中的准确等式。

Wilson 清除式 $p/(p+s)!\equiv-1/s!\pmod p$ 的范围 $0\le s<p$ 正确。
模 $p$ 后，正 $t$ 项的 $p$ 次幂消失；纯偶 $u$ 线性项为
$4/(4-H)$，其 $p$ 次幂模 $H^{2m}$ 为一；其他纯偶项的 $p$ 次幂始于 $u^{2p}$。
于是 $T^p=u^p$ 在所需截断中成立。
将唯一阶乘带写成 $T^p$ 乘低指数后，余下权重小于 $p$，准确得到式 (22) 的
$-\alpha e^{\alpha w}$，没有额外混合 Frobenius 端点。

$pR$ 的整性是在定义 $\tau$ 之前由高节点三角递推证明的：
高节点从指定为零的 $\widetilde W_p$ 开始；其余权重 $2p+n$，$1\le n<p$，传播子为单位；
与 $R$ 相乘的背景仅需权重小于 $p$。此论证没有循环使用尚未合法的模 $p$ 高带。
所以式 (24) 以及

$$
(\mathscr D^{[2]}+J)\tau=J,\qquad [1]\tau=0
$$

均成立；$-1$ 是有限阶乘缺陷，而不是把实际内部初值换成形式对数极点。

### 4. Chebyshev 整段移位：PASS

直接展开 Laurent 加法式给出

$$
\mathsf C_{2p+n}-\mathsf C_n
=\frac{\mathsf C_{2p}-2}{2}\mathsf C_n
 +\frac{\mathsf C_p}{2}(z^p-z^{-p})(z^n-z^{-n}).
$$

除以 $H$ 并使用 $z^n-z^{-n}=(z-z^{-1})\mathsf S_n$，
正好得到目标式 (28) 的系数及正号。
其中 $(z^p-z^{-p})(z-z^{-1})/H=(H-4)\mathsf S_p(H)$ 本来即为整多项式，
不存在未说明的 $H^{-1}$ 极点。
Frobenius 进一步给出

$$
\lambda(H)=H^m(H-4)^{m+1}=\chi H^m(4-H)^{m+1}.
$$

加法式第一项从 $H^{p-1}=H^{2m}$ 开始，第二项中
$\mathsf C_p/2-1$ 的贡献从 $H^{p+m}$ 开始。
因此 $\mathscr D^{[2]}-\mathscr D=\lambda\mathsf S\pmod{H^{2m}}$ 保留了
$H^m$ 至 $H^{2m-1}$ 的全部线性移位，不只是最低一层。

### 5. 形式 Ward 身份及高带唯一性：PASS

所有 $H$ 导数先在 $\mathbb Z_p[[H]]$ 的低块计算，合法且保持整性。
由 $\mathscr NF=J(1+\mathscr Nw)$、$\mathscr SF=F+J\mathscr Sw$ 及
$\mathsf C_n'=-n\mathsf S_n$，独立得到

$$
(\mathscr D+J)\mathscr Nw=-J,
\qquad
(\mathscr D+J)(H\partial_H-\mathscr S)w
=\mathscr N\mathsf S w.
$$

把候选 $-\mathscr Nw+\lambda(H)(H\partial_H-\mathscr S)w$
代入高方程，两个一次移位项因对角算子交换相消，二次项属于
$\lambda^2\mathscr R=0$。候选的常数为零。
$J$ 无常数且各正节点的 $d_{2p+n}$ 为单位，故唯一性确立式 (35)。
有限低指数的链式法则遂给式 (36)；$H$ 导数没有误作用到外部 $\lambda$。

### 6. 两端点缩放、压缩及返回实际环：PASS

对 $j=p+s$、$1\le s\le m$，第一端点为
$(k,u\text{ 次数})=(p-1-2s,p+s)$，第二端点为 $(p-2s,p+s-1)$。
两者的 $t$ 次数均小于 $p$，都在本件截断中。
转换 $u=Lx^2/4$ 后，第二项外部的 $2L$ 给出相对系数八，
因此目标式 (37)、(40) 的全部符号及 $4$ 的幂次一致。

两个低端点分别满足 $\alpha+\deg_x=p$，故式 (36) 的未移位项在特征 $p$ 中均消失。
它们的 $\mathscr S$ 次数同时等于 $c=p-1-s$，于是配对准确压缩为

$$
p\widetilde C_{p+s}(H)
\equiv4^{-p}\lambda(H)(H\partial_H-c)[L^s]\mathcal B_1(H,L)
\pmod{p,H^{2m}}.
$$

这里 $[L^s]\mathcal B_1(H,L)$ 与既有首层稿式 (15) 的规范相同：
两个指数只使用低于 $p$ 的权重，不含新的内部初值。
已接受形式身份给它属于 $(H^m,p)$；$H\partial_H-c$ 保持该理想；
$\lambda(H)\in H^m\mathbb Z_p[H]$，故右端属于 $(H^{2m},p)$。
不是由实际 $h$ 整除式擅自导出形式导数结论。

所有约化量已先证整，代入 $H=h$ 后形式 $p$ 误差属于 $h^M$；
再加上第二节的实际／辅助误差 $h^{M-3m}\subseteq h^{2m}$，
便得到原结论 $pC_j\in h^{2m}\mathcal O^+$。

### 7. 首层核对、边界与商转移：PASS

$U=-\log((1-t/4)^2-u)$ 只在权重小于 $p$ 使用，所需对数及指数分母均为单位。
目标中的 $Q$ 多项式身份准确给出平方传播子低解；
$\lambda(H)=4\chi H^m\pmod{H^{m+1}}$ 给出式 (43)。
式 (44) 的两个二项式上标分别是 $p$、$p+1$；在 $1\le s<m$ 的指定下标范围内
分母均不含 $p$，分子各含一个 $p$，所以逐端点临界消失正确。
$s=m$ 由完整配对压缩处理，不被错误地纳入逐端点消失。

$p=5$ 时 $m=2,s=m-1=1$；第二低端点的 $u$ 次数为零，合法。
阶乘上界为九，仍小于 $2p=10$。全部边界均由一般有限公式覆盖。

令 $a_j=[L^j](h^{-D}p^2\mathcal B_3)$，已证结论给
$a_j\in h^{e_*+2m}$，$j>p$。首一性首先给 $u_p=a_D$，再按

$$
a_{m+r}=u_r+\sum_{i<m}b_i u_{m+r-i}
$$

从 $r=p-1$ 递降到 $r=m+2$。右端所有有效商下标严格大于 $r$，
且 $m+r>p$；归纳因此闭合。交叉项实际多一个 $h$，与次高商剩余的附加核对相容。
没有把单位 $p/h^M$ 直接置为一；相应被乘剩余为零才保证结论。

### 8. 辅助精确代数核算

另用符号有理多项式运算检查了低 $Q$ 身份的残差以及上述 Laurent 加法式的残差，
两者准确为零。检查变量均为形式独立变量，不取具体素数、参数或根。
这些运算仅核对符号和常数；本报告的一般证明判断由前七节给出，不依赖数值扫描。

## Corrections or Missing Assumptions

无阻断性错误、遗漏假设或必要修订。原目标范围无变化。

## Open Risks and Scope

- $j=p$ 的第二端点需要 $t^p$ 响应，本件截断不保留它；本次 PASS 不覆盖该边界。
- $\lambda^2$ 和移位中的 $H^{2m}$ 项不能用于下一精度时继续删除。
- 最小参数的实际／辅助误差可恰落在 $h^{2m}$，本稿不确定该层真实非零值。
- 共同系数下界不等同于准确赋值、完整 Newton 图或负因子不可约性。
- 本报告不修改作者稿、旧失败记录、接受处置、批次入口或任何论文产物；无外部操作。

综上，冻结目标稿的全部新证明环节及所声明的商转移均通过，原结论保持不变。
