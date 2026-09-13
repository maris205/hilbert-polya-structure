# Proof Package：第三 forcing 上半高系数的完整线性移位段消失

日期：2026-09-08。作者：`/root/negative_subtop_author`。
使用 `proof-writer`。主控提出一般 Ward 恒等式及整段压缩提示，
本作者完成以下有限截断、真实共振误差、阶乘带和端点转移证明。
有界作者侧协作检查参与了移位和整性核算，不计作非作者独立验收。

## Claim

固定任意素数 $p\ge5$、整数 $a\ge2$，保持同一双谐波实际分支与规范。令
$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=3m+1=p+m,
\qquad e_*=M-D.
$$
设 $C_j=[L^j]\mathcal B_3$ 为实际第三 forcing 的系数。则
$$
\boxed{pC_j\in h^{2m}\mathcal O^+
\qquad\text{对全部 }p<j\le D.}                            \tag{1}
$$
这包含最初有界目标的次高临界剩余
$$
\boxed{\overline{h^{-m}pC_{D-1}}=0.}                       \tag{2}
$$
在已接受的首一分解
$$
S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
P_{\rm cl}=L^m+\sum_{i<m}b_iL^i,\quad
U_{\rm cl}=\sum_{r=0}^{p}u_rL^r
$$
中，进一步有
$$
\boxed{u_r\in h^{e_*+2m}\mathcal O^+
=h^{M-m-1}\mathcal O^+
\qquad(m+2\le r\le p).}                                  \tag{3}
$$
特别地 $u_{p-1}$ 在高度 $M-p=e_*+m$ 的剩余为零。
式 (1)、(3) 只是共同下界，不声明高度 $2m$ 或 $M-m-1$ 非零。
下边界 $j=p$ 不在本件证明范围；完整负 Newton 图、准确斜率和因子型均不由本件确定。

## Status

`PROVABLE AS STATED`：以下为一般素数的完整作者证明，待针对冻结新稿的非作者核查。
原次高临界问题由更强的同构造整段结论覆盖。
没有逐素数扫描、参数扫描、根拟合或对实际根型的猜测。

## Assumptions and accepted inputs

令 $\zeta$ 为本原 $p^a$ 次根，取
$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad L=\rho\lambda,
\qquad K^+=\mathbb Q_p(h),\quad \mathcal O^+=\mathbb Z_p[h],
$$
其中 $v_h(h)=1$、$v_h(p)=M\ge5m$。实际有限递推是
$$
d_n(h)V_n(b)=-\frac b2[x^{n-1}]e^{V(b)}
             -L[x^{n-2}]e^{2V(b)},\qquad 1\le n<3p,
\quad d_n(h)=-\frac{2-\zeta^n-\zeta^{-n}}h.                \tag{4}
$$
辅助幅度 $b$ 只用于提取系数，实际取 $b=1$，且
$$
\mathcal B_3=-[x^{3p-1}]e^{V(1)}-2L[x^{3p-2}]e^{2V(1)}.    \tag{5}
$$
$3p<p^a$ 保证这些实际传播子非零；$p\nmid n$ 时它们为单位，
$v_h(d_p)=v_h(d_{2p})=2m$。

只调用以下接受输入中的必要事实，不重开旧证明：

1. [首层内部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
   式 (3)：$h^mV_p(L)$ 逐系数整。齐次性使这条界适用于下面所有第一次内部幅度系数。
2. 同稿 Step 4、式 (15) 的真正形式身份：若 $\mathcal B_1(H,L)$ 为低块给出的第一 forcing，则
   $$
   \mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L),
   \quad \chi=(-1)^{m+1},\quad R,T\in\mathbb Z_p[L][[H]].   \tag{6}
   $$
   参数次数有统一有限界。使用的是这条形式身份，不是在实际商环上对 $h$ 求导。
3. [当前接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_AND_POSTCRITICAL_DISPOSITION_20260908.md)：
   既有共同界 $pC_j\in h^m$（$j>m$）确定临界剩余问题，
   并提供固定次数首一分解、$b_i\in h\mathcal O^+$。
   已接受的最高项较强界和正簇结构不在本件重新证明或降级。

此前 [次高首层作者稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_SUBTOP_PROBE_V1_20260908.md)
采用 $t^4=0$。它尚未单独获全文独审；本件不把其作者状态当作接受依赖，
下面自含地证明推广至 $t^p=0$ 所需的共振误差和阶乘带引理。

## Notation and finite calculation region

置
$$
t=bx,\qquad u=Lx^2/4,\qquad
\mathscr N=t\partial_t+2u\partial_u,\qquad
\mathscr S=t\partial_t+u\partial_u.
$$
$t^ku^r$ 的 $x$ 权重为 $k+2r$。本件始终同时截断
$$
t^p=0,\qquad k+2r<3p.                                     \tag{7}
$$
被删除单项式生成一个理想，所保留区域对取乘积因子下降封闭。
实际递推的齐次性由 (4) 按 $n$ 归纳得到，故可写成 $V(t,u)$；
删除 $b$ 次数至少为 $p$ 的项不影响任何较低 $b$ 次数的递推。

为避免和实际 forcing 系数 $C_j$ 混淆，Chebyshev 多项式记为 $\mathsf C_n$：
$$
\mathsf C_0(H)=2,\quad \mathsf C_1(H)=2-H,\quad
\mathsf C_{n+1}(H)=(2-H)\mathsf C_n(H)-\mathsf C_{n-1}(H),
\qquad d_n(H)=\frac{\mathsf C_n(H)-2}{H}.
$$
算子 $\mathscr D(H)$ 在正权重 $n$ 上乘 $d_n(H)$。
递推 (4) 的紧凑形式为
$$
\mathscr D(h)V=-\frac t2e^V-4u e^{2V}.                     \tag{8}
$$
所有指数都是有限系数运算；没有 $p$-进指数解析收敛的主张。
只有在先证明整性之后，才对正规化高系数取模 $p$ 或模 $h^r$。

## Proof Strategy and Dependency Map

1. 在窗口 (7) 中保留全部第一、第二内部初值，证明其实际值及所有污染项的界。
2. 将这些内部初值设为零，只作为辅助分支；实际／辅助差乘 $p$ 后至少到 $h^{2m}$。
3. 对辅助分支完整清除唯一阶乘 $p$，得到 $u^p$ 高带的有限算子方程。
4. 在形式 $H$ 环证明准确 Ward 恒等式及整个模 $H^{2m}$ 的 $2p$ 移位。
5. 将高端点压缩成第一 forcing 的形式 $H$ 导数；式 (6) 使其再带一个 $H^m$。
6. 返回实际环，并用首一性把系数高度从 forcing 转给相应商系数。

## Proof

### Step 1. 全部内部初值的实际估值

在 (7) 内，非单位传播子只能位于权重 $p$ 或 $2p$。
第一次内部单项式是
$$
t^ku^{(p-k)/2}\quad(k=1,3,\ldots,p-2),
$$
记其实际系数为 $q_{1,k}$。第二次内部单项式是
$$
t^ku^{p-k/2}\quad(k=0,2,\ldots,p-1),
$$
记其实际系数为 $q_{2,k}$。
齐次性和接受输入 $h^mV_p(L)$ 整给
$$
v_h(q_{1,k})\ge-m.                                        \tag{9}
$$

先看纯偶解 $W=V|_{t=0}=\sum_{r\ge1}W_ru^r$。
它满足
$$
d_{2r}(h)W_r=-4[u^{r-1}]e^{2W}.                            \tag{10}
$$
对 $r<p$，递推的除数为单位，指数只用次数小于 $p$ 的阶乘，故 $W_r$ 整。
到 $r=p$ 时右端仍整，因而
$$
v_h(q_{2,0})=v_h(W_p)\ge-2m.                               \tag{11}
$$

证明其余 $q_{2,k}$ 的界时不能把两个第一内部值的乘积遗漏。
不过第二内部方程的两个指数来源，权重分别是 $2p-1$ 和 $2p-2$，
都严格小于 $2p$，所以不可能同时使用两个始于权重 $p$ 的内部值。
下面说明它们的背景系数整。

在 $t^p=0$ 下将指数先分为
$$
e^{\alpha V}=e^{\alpha W}
\sum_{\ell=0}^{p-1}\frac{\alpha^\ell(V-W)^\ell}{\ell!}.
                                                               \tag{12}
$$
第二因子所用阶乘全是单位；在权重小于 $2p$ 的第一因子中，
所需纯偶次数小于 $p$，其阶乘也全是单位。
按权重在 $p<n<2p$ 的非共振位置作单位三角归纳，
每个系数均为 $q_{1,k}$ 的整系数仿射多项式；
两个 $q_{1,k}$ 的乘积最低权重为 $2p$，在此处不能出现。
因此第二内部方程的源项赋值至少为 $-m$。
除以高度 $2m$ 的 $d_{2p}(h)$，得到
$$
\boxed{v_h(q_{2,k})\ge-3m\quad(2\le k\le p-1,\ k\text{ 偶}).} \tag{13}
$$
式 (9)、(11)、(13) 保留每个实际内部值，没有赋予它们零值或普通剩余。

### Step 2. 辅助分支与完整共振误差引理

把 (7) 内全部 $q_{1,k},q_{2,k}$ 指定为零，其余位置仍按 (8) 递推，
得到辅助分支 $\widetilde V$。这只定义一个证明装置，不改变实际分支。
在形式参数 $H$ 下也作同样定义；所有未被指定的位置满足 $p\nmid n$，
故 $d_n(H)$ 在 $\mathbb Z_p[[H]]$ 中为单位，有限三角解唯一。

辅助分支的全部 $u$ 次数小于 $p$ 的系数属于 $\mathbb Z_p[[H]]$。
证明按权重归纳，使用 (12)：正 $t$ 指数只用 $\ell!$、$\ell<p$；
纯偶指数只用 $r!$、$r<p$；指定零值不引入除法，其余传播子都是单位。
所以代入 $H=h$ 后，特别有
$$
[t^ku^r]e^{\alpha\widetilde V(h)}\in\mathcal O^+
\quad(k+2r<2p),\qquad \alpha=1,2.                         \tag{14}
$$

现在在实际 $h$ 处把全部内部初值暂看成独立变量 $q$，
指定它们后用其余单位递推定义 $V(q)$，并令
$\Delta=V(q)-\widetilde V(h)$。
给 $q_{1,k}$ 标记最低权重 $p$，给 $q_{2,k}$ 标记最低权重 $2p$。
源项乘以 $t$ 或 $u$、以及指数乘积均不降低这些权重。
因此 $\Delta$ 始于权重 $p$，且在权重小于 $3p$ 时准确有
$$
e^{\alpha V(q)}-e^{\alpha\widetilde V(h)}
=e^{\alpha\widetilde V(h)}
\left(\alpha\Delta+\frac{\alpha^2}{2}\Delta^2\right).      \tag{15}
$$
三次项始于权重 $3p$，在本件区域之外。

按权重归纳，$\Delta$ 和 (15) 的每个系数都是 $q$ 的整系数多项式。
理由是任何带 $\Delta$ 的项只能与权重小于 $2p$ 的背景指数相乘；
这些系数由 (14) 整。剩余运算只有加乘和单位除法。
允许的 $q$ 单项式只有一次项，或两个第一次内部值的乘积；
任何含第二内部值的二次项最低权重已为 $3p$。
由 (9)、(11)、(13)，所有一次项赋值至少为 $-3m$，
两个第一次内部值的乘积赋值至少为 $-2m$。
将实际初值代入，得到逐系数界
$$
\boxed{V-\widetilde V(h),\quad
e^{\alpha V}-e^{\alpha\widetilde V(h)}
\in h^{-3m}\mathcal O^+\quad(t^p=0,\;\deg_x<3p),
\quad\alpha=1,2.}                                        \tag{16}
$$
因此先乘 $p$ 后的实际／辅助误差满足
$$
\boxed{p\bigl(e^{\alpha V}-e^{\alpha\widetilde V(h)}\bigr)
\in h^{M-3m}\mathcal O^+\subseteq h^{2m}\mathcal O^+.}     \tag{17}
$$
这里使用 $M\ge5m$。等号边界仍足以得到模 $h^{2m}$ 的结论，
但本引理不给出模 $h^{2m+1}$ 的统一误差。

### Step 3. 单阶乘带及带常数缺陷的准确高方程

在形式 $H$ 环中写
$$
\widetilde V=T+R,\qquad
T=\sum_{0\le k,r<p}[t^ku^r]\widetilde V\;t^ku^r,
\qquad R\in u^p\mathbb Q_p[[H]][t,u].
$$
以上求和和所属环始终按 (7) 截断。Step 2 已证明 $T$ 全整。
因为 $k\le p-1$、$k+2r\le3p-1$，有
$$
k+r\le2p-1.                                               \tag{18}
$$
一个指数乘积贡献到 $t^ku^r$ 时，因每个因子无常数，其因子数不超过 $k+r$。
所以所有所需阶乘至多含一个 $p$，$pe^{\alpha T}$ 逐系数形式整。
又因 $R^2$ 始于 $u^{2p}$，其权重至少为 $4p$，有
$$
e^{\alpha\widetilde V}=e^{\alpha T}(1+\alpha R)
\quad\text{在本件窗口内}.                                \tag{19}
$$

Wilson 身份在先清除唯一的 $p$ 后给出
$$
\frac p{(p+s)!}\equiv-\frac1{s!}\pmod p
\qquad(0\le s<p).                                         \tag{20}
$$
以下形式约化在
$$
\mathscr R=\mathbb F_p[H]/(H^{2m})
$$
内进行。因 $t^p=0$，Frobenius 只留下 $T$ 的纯偶部分。
其 $u$ 线性系数准确为
$$
W_1(H)=-4/d_2(H)=4/(4-H),\qquad
W_1(H)^p=(1-H^p/4)^{-1}=1\quad\text{在 }\mathscr R\text{ 中},
$$
因为 $p=2m+1>2m$。纯偶更高项的 $p$ 次幂从 $u^{2p}$ 起。
于是
$$
\boxed{T^p=u^p\pmod{u^{2p},t^p}\quad\text{在 }\mathscr R\text{ 中}.} \tag{21}
$$
没有把 $(t,u)$ 的混合项误当成额外的 Frobenius 端点。

记 $w(H,t,u)$ 为辅助分支的权重小于 $p$ 部分；
它等于实际低块的形式解，属于 $\mathbb Z_p[[H]][t,u]$ 的相应有限区域。
由 (20)、(21)，对 $k+2r<p$ 有
$$
\overline{p[t^ku^{p+r}]e^{\alpha T}}
=-\alpha[t^ku^r]e^{\alpha w}\quad\text{于 }\mathscr R.     \tag{22}
$$
右端只用低于 $p$ 权重的指数，阶乘均为单位。

从 $\widetilde W_p=0$ 开始，按高节点权重递推，
(8)、(19) 及已证的 $pe^{\alpha T}$ 形式整性，
先证明 $pR$ 属于 $\mathbb Z_p[[H]][t,u]$：
与 $R$ 相乘的背景指数权重小于 $p$，因而整，且每个方程只用更早的高节点；
除常数节点已指定为零外，$2p+n$ 的 $1\le n<p$ 传播子均为单位。
因此可以合法定义
$$
\tau(H,t,u)=\sum_{k+2r<p}
\overline{p[t^ku^{p+r}]\widetilde V}\;t^ku^r\in\mathscr R[t,u],
\qquad [1]\tau=0.                                         \tag{23}
$$
式 (19)、(22) 给出完整高指数身份
$$
\boxed{\overline{p[t^ku^{p+r}]e^{\alpha\widetilde V}}
=[t^ku^r]\alpha e^{\alpha w}(\tau-1),
\quad k+2r<p,\quad\alpha=1,2.}                            \tag{24}
$$
常数缺陷 $-1$ 是阶乘贡献，不是以形式对数的 $1/p$ 替换实际内部值。

定义低区域的两个算子及乘法系数
$$
\mathscr D(t^ku^r)=d_{k+2r}(H)t^ku^r,\qquad
\mathscr D^{[2]}(t^ku^r)=d_{2p+k+2r}(H)t^ku^r,
$$
$$
F=\frac t2e^w+4u e^{2w},\qquad
J=\frac t2e^w+8u e^{2w}.                                   \tag{25}
$$
算子方程只对正权重使用，零常数另行指定。由 (8)、(24) 得
$$
\boxed{\mathscr Dw=-F,\qquad
(\mathscr D^{[2]}+J)\tau=J.}                              \tag{26}
$$
$w$ 的第一式先在特征零形式环准确成立；第二式在 $\mathscr R$ 中成立。
没有对 $d_0$ 或内部常数方程作除法。

### Step 4. 完整模 $H^{2m}$ 的真实 $2p$ 移位

定义整数多项式
$$
\mathsf S_0(H)=0,\quad\mathsf S_1(H)=1,\quad
\mathsf S_{n+1}(H)=(2-H)\mathsf S_n(H)-\mathsf S_{n-1}(H).
$$
若在辅助 Laurent 环置 $H=2-z-z^{-1}$，则
$$
\mathsf C_n=z^n+z^{-n},\qquad
\mathsf S_n=\frac{z^n-z^{-n}}{z-z^{-1}},\qquad
\mathsf C_n'(H)=-n\mathsf S_n(H).                         \tag{27}
$$
最后一式可对前式在特征零求导，使用
$dH/dz=-(z-z^{-1})/z$；两侧本来都是整数多项式，所以得到多项式身份。

先模 $p$。Chebyshev 加法公式准确给
$$
d_{2p+n}-d_n
=\frac{\mathsf C_{2p}-2}{2H}\mathsf C_n
 +\frac{\mathsf C_p}{2}\lambda\mathsf S_n,\qquad
\lambda=\frac{(z^p-z^{-p})(z-z^{-1})}{H}.                  \tag{28}
$$
在特征 $p$ 中，
$$
\mathsf C_p=2-H^p,\qquad
\mathsf C_{2p}=2-4H^p+H^{2p},\qquad
\lambda=H^m(H-4)^{m+1}=\chi H^m(4-H)^{m+1}.               \tag{29}
$$
其中最后一式来自
$z^p-z^{-p}=(z-z^{-1})^p$ 和 $(z-z^{-1})^2=H(H-4)$。
式 (28) 的第一项从 $H^{p-1}=H^{2m}$ 起；
第二项中将 $\mathsf C_p/2$ 替为 $1$ 的误差从 $H^{p+m}$ 起。
因此在正权重 $n<p$ 的区域，记 $\mathsf S$ 为乘 $\mathsf S_n(H)$ 的对角算子，有
$$
\boxed{\mathscr D^{[2]}-\mathscr D
=\lambda\mathsf S\pmod{H^{2m}},\qquad \lambda\in H^m\mathscr R.} \tag{30}
$$
这保留了从 $H^m$ 到 $H^{2m-1}$ 的整个移位段，不是只取一个首项。
所有被取模的对象原本形式整，实际代入后的额外 $p$ 误差高度为 $M>2m$。

### Step 5. 形式 Ward 恒等式与高带的整个线性修正

以下先对 $w(H,t,u)\in\mathbb Z_p[[H]][t,u]$ 求形式导数，定义
$$
\mathscr A=H\partial_H-\mathscr S.
$$
这里 $H$ 是独立形式变量；没有在实际 $\mathcal O^+/h^r$ 上定义微分。
低区域的 $\mathscr D$ 与 $\mathscr N,\mathscr S$ 交换。
由 $\mathscr Dw=-F$，分别施加 $\mathscr N$、$\mathscr S$、$H\partial_H$，得到
$$
(\mathscr D+J)\mathscr Nw=-J,                             \tag{31}
$$
$$
(\mathscr D+J)\mathscr Sw=-F=\mathscr Dw,
\qquad
(\mathscr D+J)H\partial_Hw=-H\mathscr D'w.                \tag{32}
$$
第一式使用 $\mathscr NF=J(1+\mathscr Nw)$；
第二式使用 $\mathscr SF=F+J\mathscr Sw$，因为 $\mathscr S$ 给显含的 $t,u$ 各权重一。
将 (32) 两式相减，再用
$d_n+Hd_n'=\mathsf C_n'=-n\mathsf S_n$，得到准确身份
$$
\boxed{(\mathscr D+J)\mathscr Aw
=-(\mathscr D+H\mathscr D')w
=\mathscr N\mathsf Sw.}                                  \tag{33}
$$

在 $\mathscr R$ 中考虑候选高带
$-\mathscr Nw+\lambda\mathscr Aw$。
由 (30)、(31)、(33)，将 $\mathscr D^{[2]}+J$ 作用于它，得到
$$
J-\lambda\mathsf S\mathscr Nw
 +\lambda\mathscr N\mathsf Sw
 +\lambda^2\mathsf S\mathscr Aw=J.                       \tag{34}
$$
中间两项因两个对角算子交换而相消，末项因 $\lambda^2\in H^{2m}$ 而为零。
候选的常数为零，与 (23) 相同。
每个正节点 $n<p$ 的 $d_{2p+n}(H)$ 都是单位，且 $J$ 无常数项，
单位三角唯一性遂给
$$
\boxed{\tau=-\mathscr Nw+\lambda\mathscr Aw
\quad\text{在 }\mathscr R\text{ 中}.}                    \tag{35}
$$
结合 (24)，并在低区域合法使用指数的形式导数，得
$$
\boxed{\overline{p[t^ku^{p+r}]e^{\alpha\widetilde V}}
=[t^ku^r]\left(- (\alpha+\mathscr N)e^{\alpha w}
                      +\lambda\mathscr A e^{\alpha w}\right).} \tag{36}
$$
$\lambda$ 在 $\mathscr A$ 外面；本式不把 $H$ 导数错误地作用到 $\lambda$ 上。

### Step 6. 上半段两个端点压缩成第一 forcing

写 $j=p+s$，其中 $1\le s\le m$。令
$$
k=p-1-2s,\qquad k'=p-2s,\qquad c=p-1-s.
$$
第一端点需要 $[t^ku^{p+s}]e^V$，第二端点需要
$[t^{k'}u^{p+s-1}]e^{2V}$。在此范围
$$
0\le k\le p-3,\qquad 1\le k'\le p-2,
$$
所以两个响应都保留在 $t^p=0$ 的窗口内。变量缩放给出准确系数式
$$
\boxed{C_{p+s}=-4^{-(p+s)}
\left([t^ku^{p+s}]e^V
 +8[t^{k'}u^{p+s-1}]e^{2V}\right).}                       \tag{37}
$$
第二项的 $8$ 来自外部的 $2L$ 和提出一个 $u=Lx^2/4$ 的因子 $4$。
此式包含两个指数的全部幅度响应。

在 (36) 中，第一端点的 $(\alpha,k,r)$ 为 $(1,k,s)$，
第二端点为 $(2,k',s-1)$。它们满足
$$
1+k+2s=p,\qquad 2+k'+2(s-1)=p,                           \tag{38}
$$
而两个 $\mathscr S$ 次数均为
$$
k+s=k'+s-1=c.                                              \tag{39}
$$
故 (36) 中的未移位项都被乘子 $p$ 消去，剩下同一算子
$\lambda(H\partial_H-c)$。

记低第一 forcing 的形式系数为
$$
\mathfrak c_s(H)=[L^s]\mathcal B_1(H,L).
$$
它的两个指数端点正是上述低端点；因此在特征零有
$$
\boxed{\mathfrak c_s(H)=-4^{-s}
\left([t^ku^s]e^w+8[t^{k'}u^{s-1}]e^{2w}\right).}         \tag{40}
$$
这里只使用低于 $p$ 权重的系数，与式 (6) 的实际低块形式规范完全一致。
若 $\widetilde C_{p+s}(H)$ 表示 (37) 的辅助分支版本，
由 (36)—(40) 得到核心压缩身份
$$
\boxed{p\widetilde C_{p+s}(H)
\equiv4^{-p}\lambda(H)(H\partial_H-c)\mathfrak c_s(H)
\pmod{p,H^{2m}}.}                                        \tag{41}
$$
左右量均已形式整；这里的 $(p,H^{2m})$ 是该整环中的理想。

接受输入 (6) 给 $\mathfrak c_s(H)\in H^m\mathbb Z_p[[H]]+p\mathbb Z_p[[H]]$。
形式算子 $H\partial_H-c$ 保持这两个理想，所以
$$
\lambda(H)(H\partial_H-c)\mathfrak c_s(H)
\in H^{2m}\mathbb Z_p[[H]]+p\mathbb Z_p[[H]].              \tag{42}
$$
没有从实际 $h^{-m}\mathcal B_1(h,L)$ 整性擅自推断一个实际微分身份。
将 (41)—(42) 代入 $H=h$，形式 $p$ 误差高度至少为 $M>2m$，得到
$$
p\widetilde C_{p+s}(h)\in h^{2m}\mathcal O^+.
$$
再用实际／辅助误差 (17) 及 $4$ 是单位，证明 (1)。

### Step 7. 次高临界核对、最小素数与商转移

为直接核对最初的临界层目标，将 (35) 只保留到 $H^{m+1}$。
低解在 $H=0$ 为
$$
U(t,u)=-\log Q(t,u),\qquad Q=(1-t/4)^2-u,
$$
只在权重小于 $p$ 的系数上使用，阶乘分母合法。
该式可由多项式身份
$ (\mathscr NQ)^2-Q\mathscr N^2Q=tQ/2+4u$
验证低方程，再用单位三角唯一性确定。
因 $4^{m+1}=4$ 于 $\mathbb F_p$，有
$$
\tau=-\mathscr Nw-4\chi H^m\mathscr SU
\pmod{H^{m+1}}.                                           \tag{43}
$$
对 $1\le s<m$，两个低端点系数分别是
$$
[t^ku^s]Q^{-1}=4^{-k}\binom p k,\qquad
[t^{k'}u^{s-1}]Q^{-2}=s4^{-k'}\binom{p+1}{k'}.             \tag{44}
$$
这里 $2\le k\le p-3$、$3\le k'\le p-2$，两个二项式都含 $p$，
其分母的阶乘均小于 $p$。故临界层的两个端点各自为零。
$s=m$ 的最高项不采用这一逐端点解释，而已被 (41)—(42) 的完整配对覆盖。
次高项对应 $s=m-1$，所以 (2) 成立。

当 $p=5$ 时 $m=2$，次高项的 $s=1$、$k=2$、$k'=3$ 均严格小于 $p$；
第二低端点的 $u$ 次数为零，不需负下标或共振除法。
一般窗口的阶乘界仍为 $k+r\le9<10=2p$，
而 $M-3m\ge4=2m$，正好覆盖全部需要的精度。
所有边界依据有限公式处理，不用素数扫描。

现在写 $S=\sum a_jL^j$。由 (1)，
$$
a_j\in h^{M-D+2m}\mathcal O^+=h^{e_*+2m}\mathcal O^+
\qquad(j>p).                                               \tag{45}
$$
首一性先给 $u_p=a_D$。从 $r=p-1$ 递降到 $r=m+2$，比较 $L^{m+r}$ 系数：
$$
a_{m+r}=u_r+\sum_{i<m}b_i u_{m+r-i}.                       \tag{46}
$$
此时 $m+r>p$；和式中的有效商下标均大于 $r$，
已在递降归纳中属于 $h^{e_*+2m}$，而 $b_i$ 整。
所以 $u_r$ 也属于同一理想，证明 (3)。
所有这些交叉项实际还至少多一个 $h$，因为 $b_i\in h\mathcal O^+$。

对最初关心的次高商项，唯一交叉项是
$$
a_{D-1}=u_{p-1}+b_{m-1}u_p.
$$
其交叉项在 $h^{e_*+2m+1}$ 中，特别高于目标高度 $M-p=e_*+m$。
规范化时 $p/h^M$ 只是一个单位，不能一般地置为 $1$；
但它所乘的 $\overline{h^{-m}pC_{D-1}}$ 已为零。
因此
$$
\overline{h^{-(M-p)}u_{p-1}}=0.
$$
证毕。$\square$

## Corrections, Boundaries, and Open Risks

- $j=p$ 的第二端点需要 $t^p$ 响应，正被本件截断删除，故明确不在本定理范围。
  本件不以形式低次数理由偷偷将这条边界包括进来。
- 将 $t^4=0$ 推广为 $t^p=0$ 后，全部第一次和第二次内部值均有明确估值，
  单阶乘上界也重新证明；没有直接沿用只涉及一次奇响应的旧支撑论证。
- 移位的 $H^{2m}$ 项与 $\lambda^2$ 同时进入下一精度。
  本件在模 $H^{2m}$ 中舍去它们，不声称它们自身为零。
- 先乘 $p$ 后的实际／辅助误差属于
  $h^{M-3m}\mathcal O^+\subseteq h^{2m}\mathcal O^+$；
  不从边界等号擅自提高到 $h^{2m+1}$。
- 式 (1) 不是准确赋值，也不单独决定负因子的整幅 Newton 图、不可约性或简单性。
- 本稿为作者证据；作者共同推导与作者侧子检查不计非作者终审。
  没有修改旧稿、状态入口、Paper30 项目或任何已接受产物，也无外部操作。
