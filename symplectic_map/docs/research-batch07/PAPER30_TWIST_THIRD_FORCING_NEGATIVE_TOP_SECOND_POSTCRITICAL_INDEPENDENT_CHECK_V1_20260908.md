# Proof Package：最高参数端点 Ward 整段及二次边界的非作者全文独立审查

日期：2026-09-08。审查者：`/root/negative_top_quadratic_review`。
作者为 `/root/negative_top_alternative`，主控参与推导；本审查者未参与作者稿撰写。
作者侧子核算均视为作者协作，不作为本次独审的独立性来源。
使用 `proof-writer` 技能。仅新增本报告，不修改作者稿、旧失败稿、接受状态或入口。

审查对象：[最高端点第二后临界作者稿 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md)，全文 658 行。
审查前确认的冻结输入 SHA-256：

```text
e754946905524581d55cbf1d893c8141db7fc69a1aa33050d778c1754bf789a2
```

## Claim

对任意素数 $p\ge5$、整数 $a\ge2$，保持作者稿固定的实际双谐波分支，令

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=p+m=3m+1,
\qquad C_D=[L^D]\mathcal B_3.
$$

本次审查的原命题是

$$
pC_D\in h^{2m+1}\mathcal O^+=h^p\mathcal O^+,
\qquad v_h([L^p]U_{\rm cl})\ge M-m,
$$

以及其推论

$$
\overline{h^{-(m+2)}pC_D}=0.
$$

这不是 $h^p$ 层非零、准确赋值、其余商系数或完整负 Newton 图的命题。

## Status

**PROVABLE AS STATED。全文独审 PASS；下列 30 项全部 PASS。**

原命题保持不变，无须削弱或增加科学假设。未发现必须修订的数学错误或未闭合的关键步骤。
一处引用标签可进一步精确定位：作者稿 Assumptions 指向首内部稿“式 (2)”，
而本轮需要的形式身份在该已接受稿的 **式 (15)**，独审第 11—12 项亦明确引用它。
本次实际读取了式 (15)，证据存在且适用；这不是从单点赋值推导形式可微整除。
此报告只给数学独审结论，不自行授予项目接受、出版或 Route 状态。

## Assumptions

- $h=2-\zeta-\zeta^{-1}$，$\zeta$ 为本原 $p^a$ 次根，
  $\mathcal O^+=\mathbb Z_p[h]$，$v_h(h)=1$，$v_h(p)=M\ge5m$，剩余域为 $\mathbb F_p$。
- 实际传播子 $d_n=-(2-\zeta^n-\zeta^{-n})/h$ 和实际双谐波递推不变；
  原下标始终严格小于 $3p<p^a$，未置零实际内部模态。
- 已接受最高端点前稿提供实际权重身份、低带及正规化高带整性、污染支撑和有限参照引理。
  本轮只核查这些输入的当前适用精度，不重开已接受旧层。
- 第一内部 forcing 的形式整块身份取自已接受局部结构稿式 (15)，
  不是只取该稿式 (2) 的真实点值结论。
- 最终高度换算仅用已接受的首一分解
  $h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$，其中 $\deg P_{\rm cl}=m$、$\deg U_{\rm cl}=p$。

本次定向读取的必要输入及其当前 SHA-256 为：

| 文件 | SHA-256 |
| --- | --- |
| [前一后临界作者稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md) | `730fd03b7da722111250813635ac9f9ac052928b516dee805a28204124df4de7` |
| [前一后临界独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_INDEPENDENT_CHECK_V1_20260908.md) | `156fba39b1aa6f32714a5ed480845227c5b26b4090781f3a10e427ac3e466d49` |
| [首内部局部结构作者稿](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md) | `f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616` |
| [首内部局部结构独审](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_INDEPENDENT_CHECK_20260907.md) | `9fa0a3ff664cdbd68497354d71694606b6475c91fbebe3326514943f5b5ed01e` |
| [共同高项及后临界接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_AND_POSTCRITICAL_DISPOSITION_20260908.md) | `5f253107f93f8b11f3d578b220da1cee599e6b1ee1b3f49f81ab253b7e2f0e4e` |

## Notation

沿用作者稿 $u=Lx^2/4$、$\Theta=u\partial_u$、$\mathcal Q=2\Theta+1$、
$\mathcal E=H\partial_H$、$\chi=(-1)^{m+1}$。
$H$ 是形式变量，真实赋值使用 $H=h$。
低偶带为 $w=W_{<p}$，低奇带为 $a=A_{<m}$；$f_1=e^w$、$f_2=e^{2w}$。
只在指定有限 $u$ 次数内使用这些指数及导数。

$$
\mathscr R_H=\mathbb F_p[H]/(H^p)\cong\mathcal O^+/(h^p),
\qquad \lambda=\chi H^m(4-H)^{m+1}.
$$

对二次边界另记 $f=(1-u)^{-1}$、$g=f^2$、$G=(1+u)f$，
$\ell=\log(1-u)$、$\mathscr D=\sum_{k\ge1}u^k/k^2$、
$\mathscr H=\sum_{r\ge0}u^r/(2r+1)$。
后三个级数先在特征零定义，实际约化分别只取次数 $\le m,\le m,<m$。

## Proof Strategy

按实际有限方程、传播子准确移位、形式 Ward 消失、完整二次响应、端点有限和、
真实误差六步重建证明。一般量词依靠符号身份与单位三角唯一性；
固定 $p=5$ 的独立重算仅核对最小边界，不替代一般证明。

## Dependency Map

1. 实际权重、整性、支撑与有限参照共同产生模 $h^p$ 的两条正规化高带方程及端点。
2. Chebyshev 加法与导数身份将线性移位压缩为精确形式 Ward 响应。
3. 第一内部 forcing 的形式整块身份消去全部线性端点至模 $H^p$。
4. 准确的二次常数项与线性反馈平方给两条二次方程，有限单位三角性确定其解。
5. 显式二次解的有限卷积闭式消去唯一剩余 $H^{2m}$ 边界。
6. 实际误差及首一性将有限结论提升为原命题，且只提升到声明精度。

## Proof

### 1. 实际有限对象及模 $h^p$ 的合法性

作者稿 (9)—(10) 与已接受最高权重身份一致：

$$
d_{2r}W_r=-4[u^{r-1}]e^{2W},\qquad
d_{2r+1}A_r=-\frac12[u^r]e^W-8[u^{r-1}]e^{2W}A,
$$

$$
4^DC_D=-[u^{p+m}]e^W-16[u^{p+m-1}]e^{2W}A.
$$

因此只需 $W_{\le p+m}$、$A_{\le p+m-1}$。偶高带正下标对应
$2p+2j$、$1\le j\le m$，奇高带对应 $2p+2j+1$、$0\le j<m$；
其常数对角元模 $p$ 均非零。没有倒置 $d_{3p}$ 或 $d_0$。

对 $W_r$、$r<p$，形式递推的对角常数 $-4r^2$ 是 $p$ 单位；
对 $A_r$、$r<m$，相应常数 $-(2r+1)^2$ 是 $p$ 单位。
所需低指数阶乘同为单位。因此这些低块的全部 $H$ 系数 $p$ 整，
包含本次隐含在 Ward 身份中的二阶及更高低带系数。
原递推系数是有理的且全部除数在上述范围为 $p$ 单位，故可在
$\mathbb Z_{(p)}[[H]]$ 构造有限低块；已接受稿采用 $\mathbb Z_p[[H]]$ 不造成差异。

正规化高带 $\tau_j=pW_{p+j}$、$\sigma_j=pA_{p+j}$ 在使用范围已整。
真实偶初值满足

$$
v_h(\tau_0)\ge M-2m\ge3m\ge2m+1=p,
$$

所以 $\tau_0=0$ 只是在本次商环中的结论，不是对实际 $W_p$ 的置零。
中间奇响应的正规化高度也至少 $M-2m\ge p$。
其下标 $r\ge m$ 在总次数 $N\le p+m-1$ 内只乘到指数下标
$N-r\le p-1$ 的整系数；非整指数与它相遇最早在 $p+m$，超出目标。
两个高带相乘最早在 $2p>p+m$，同样不出现。

有限参照引理的既有证明实际给到 $h^p$，不是只到旧端点的 $h^{m+2}$：
若 $Q=W_{<p}-\sum_{r=1}^{p-1}u^r/r\in h\mathcal O^+[u]$，
则 $G_{\rm ref}=-\log(1-u)+Q$ 与低带准确相同，且
$e^{cG_{\rm ref}}=(1-u)^{-c}e^{cQ}$，$c=1,2$。
次数 $N<2p$ 内至多出现 $q<2p$ 个 $Q$；$q<p$ 时乘 $p$ 后高度至少 $M$，
$p\le q<2p$ 时 $v_p(q!)=1$，正规化高度至少 $q\ge p$。
故正规化参照指数确在 $h^p$ 内，高带参照的 $p$ 倍只有常数 $1$ 留下。
这正给出作者稿 (11)—(12)，误差精度合法但不能自动提高。

记 $K=f_1/2+16uf_2a$。两条高带因而为

$$
(\mathcal L_e+\Delta_e)\tau=8uf_2,\qquad
(\mathcal L_o+\Delta_o)\sigma=-K(\tau-1)
$$

于各自有限次数范围；端点为

$$
4^DpC_D=-[u^m]f_1(\tau-1)
-16[u^{m-1}]\{f_2\sigma+2f_2(\tau-1)a\}.
\tag{A}
$$

### 2. 准确 Chebyshev 移位及二次项

在特征 $p$ 中，$C_p=C_1^p=2-H^p$，故
$C_{2p}=C_p^2-2=2-4H^p+H^{2p}$，且

$$
z^{2p}-z^{-2p}=(z-z^{-1})^p(2-H^p).
$$

Chebyshev 加法公式中的反对称乘积除以 $2H$ 后为

$$
\frac{(z-z^{-1})^{p+1}}{H}
\left(1-\frac{H^p}{2}\right)S_n
=\chi H^m(4-H)^{m+1}
\left(1-\frac{H^p}{2}\right)S_n,
$$

因为 $(z-z^{-1})^2=-H(4-H)$。对称乘积则为
$(-2H^{p-1}+H^{2p-1}/2)(2+Hd_n)$。
这逐项重得作者稿 (14)，所以在 $H^p=0$ 的环中

$$
\Delta(n)=\lambda S_n-4H^{2m}.
\tag{B}
$$

常数项 $-4H^{2m}$ 不能省略；非恒定二次项 $-2H^pd_n$ 恰从排除层开始。
模 $p$ 的整数多项式误差代入 $h$ 后高度至少 $M\ge p$，没有精度损失。

从 $C_n=2+Hd_n$ 及对 $z$ 的链式求导得

$$
C_n'=-nS_n,\qquad d_n+Hd_n'=-nS_n.
\tag{C}
$$

所用 $n=2j$ 或 $2j+1$ 均在 $1\le n<p$；因而频率因子可逆。
偶常数不需要使用 (C) 的逆频率式。

### 3. 形式 Ward 响应与第一 forcing 的真实依赖

低方程为 $\mathcal D_ew=-4uf_2$、$\mathcal L_oa=-f_1/2$。
对前者分别取 $\mathcal E$、$\Theta$，得到

$$
\mathcal L_e(\mathcal Ew)=-(\mathcal E\mathcal D_e)w,
\qquad \mathcal L_e(\Theta w)=-4uf_2=\mathcal D_ew.
$$

所以 $Z=(\mathcal E-\Theta)w$ 满足作者稿 (18)。
对奇方程求导时，$8uf_2$ 的 $\Theta$ 导数必须同时包含显式 $u$ 的导数。
完整计算给

$$
\mathcal L_o(\mathcal Ea)=-K\mathcal Ew-(\mathcal E\mathcal D_o)a,
\qquad
\mathcal L_o(\Theta a)=-K\Theta w-8uf_2a.
$$

再减去 $\mathcal L_oa=-f_1/2$，得到

$$
\mathcal L_oT=-KZ-(\mathcal D_o+\mathcal E\mathcal D_o)a,
\qquad T=(\mathcal E-\Theta-1)a.
$$

这独立核对了 (19) 的常数 $-1$ 与全部耦合项。
基解 $\tau^{\rm b}=-2\Theta w$、$\sigma^{\rm b}=-\mathcal Qa$ 满足零移位高带方程。
由 (C)，$\lambda S_e\tau^{\rm b}=\lambda(\mathcal D_e+\mathcal E\mathcal D_e)w$，
奇式同理；于是 $\tau^{\rm b}+\lambda Z$、$\sigma^{\rm b}+\lambda T$
将所有线性移位残差准确消去。剩余先在 $H^{2m}$ 出现，单位三角性保证这不是另一个构造的解。

基解的两个端点核分别为
$-(2\Theta+1)f_1$、$-(2\Theta+3)(f_2a)$。
提取次数 $m,m-1$ 后因子均为 $2m+1=p$，故基端点在当前环中为零。
线性核则有准确乘积身份

$$
f_1Z=(\mathcal E-\Theta)f_1,\qquad
f_2(T+2aZ)=(\mathcal E-\Theta-1)(f_2a).
$$

因此线性端点恰为 $-\lambda(\mathcal E-m)B_{\rm low}$，其中
$B_{\rm low}=[u^m]f_1+16[u^{m-1}]f_2a$。

第一内部 forcing 的定义是 $\mathcal B_1=-[x^{p-1}]e^V-2L[x^{p-2}]e^{2V}$。
最高 $L^m$ 的第一项只用零个一次谐波，给 $4^{-m}[u^m]f_1$；
第二项含一次一次谐波，$e^{2V}$ 的相应奇项为 $2xe^{2W}A$，
连同外部 $2L$ 给系数 $16\cdot4^{-m}[u^{m-1}]f_2a$。
这证明

$$
B_{\rm low}=-4^m[L^m]\mathcal B_1(H,L).
\tag{D}
$$

此处需要的原下标至多 $p-1$，确属已接受首内部整块，不涉及新的共振高带。
已接受首内部作者稿式 (15) 原文给出

$$
\mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L),
$$

其中 $R,T$ 形式整且 $L$ 次数有统一有限界，其独审第 11—12 项明确核对了这一输入。
由 (D)，模 $p$ 的 $B_{\rm low}$ 属于 $H^m\mathbb F_p[[H]]$；
$\mathcal E-m$ 将 $H^m$ 项准确杀去，所以

$$
(\mathcal E-m)B_{\rm low}\in H^{m+1}\mathbb F_p[[H]],
\qquad
\lambda(\mathcal E-m)B_{\rm low}\in H^{2m+1}.
\tag{E}
$$

这一操作对形式整系数进行，不对实际单点 $p$-进数求导。
因此全部线性端点在模 $H^p$ 消失；尚需检查的是二次边界。

### 4. 二次响应完整性与解的核对

模 $H^p$ 中，余响应可唯一写成

$$
\tau=\tau^{\rm b}+\lambda Z+H^{2m}X,
\qquad \sigma=\sigma^{\rm b}+\lambda T+H^{2m}Y,
$$

其中 $X,Y$ 只需取 $H$ 零阶。由于 $\lambda/H^m$ 的常数为 $4\chi$，
其平方为 $16$，而 (B) 的二次常数为 $-4$，代回实际高带给

$$
\mathcal L_{e0}X=4\tau^{\rm b}_0-16(2\Theta)Z_0,
$$

$$
\mathcal L_{o0}Y=-\left(\frac f2+8uf^3\right)X
+4\sigma^{\rm b}_0-16\mathcal QT_0.
\tag{F}
$$

其中 $Z_0=-uf$、$T_0=-f^2/2$、$\tau^{\rm b}_0=-2uf$、
$\sigma^{\rm b}_0=-(1+u)f^2/2$。
两个来源均已保留：移位的二次常数，以及线性移位再次作用于线性响应。
高带相乘受 $u$ 支撑排除，不存在另一个漏掉的指数二次高带贡献。
更高反馈至少 $H^{3m}$，且 $3m\ge2m+1$ 对全部 $m\ge2$ 成立。

用 $\Theta\ell=-uf$、$\Theta\mathscr D=-\ell$、
$\Theta\mathscr H=(f-\mathscr H)/2$ 逐项求导，可独立核得

$$
X=4\ell-2G\mathscr D,
\qquad
Y=-(1+u)f^2\mathscr D-2f\ell-2f-4G\mathscr H.
\tag{G}
$$

偶方程右端化为 $8u(3+u)f^2$，奇方程中不含 $X$ 的源项化为
$2(u^2+12u+3)f^3$。将 (G) 代入对应算子后分别得到这两个表达式。
本次独立自由符号微分计算的两条残差均严格为零；该核算不依靠特定素数。

$X(0)=0$，而 $Y(0)=-6$；后者由奇常数方程 $-Y(0)=6$ 直接要求，不能省去。
偶正下标 $1\le j\le m$ 的对角元 $-4j^2$ 与奇下标 $0\le j<m$ 的
$-(2j+1)^2$ 均为单位，故满足方程与常数条件的有限解唯一。
应用导子不增大 $u$ 次数，不会把 $\mathscr H$ 的非法边界 $u^m/p$ 拉回低范围。
所有被约化的分母均小于 $p$，也没有使用指数的非法阶乘系数。

### 5. 二次端点及一般有限和

令 $J_2=fX$、$K_2=g(Y+fX)$。由 (G) 准确得到

$$
J_2=4f\ell-2(1+u)f^2\mathscr D,
$$

$$
K_2=-3(1+u)f^4\mathscr D+2f^3\ell-2f^3-4(1+u)f^3\mathscr H.
\tag{H}
$$

定义 $H_1=\sum_{k=1}^m1/k$、$H_2=\sum_{k=1}^m1/k^2$、
$H_o=\sum_{r=0}^{m-1}1/(2r+1)$。第一核由
$[u^n](1+u)f^2=2n+1$ 直接给出

$$
[u^m]J_2=-2(2m+1)H_2.
\tag{I}
$$

第二核的卷积使用
$[u^n](1+u)f^4=(n+1)(n+2)(2n+3)/6$、
$[u^n]f^3=(n+1)(n+2)/2$、
$[u^n](1+u)f^3=(n+1)^2$。
它产生作者稿 (35) 的三个和 $\mathfrak A_m,\mathfrak B_m,\mathfrak C_m$。
为独立核对闭式，可逐项使用

$$
\frac{(m-k)(m+1-k)(2m+1-2k)}{k^2}
=\frac{m(m+1)(2m+1)}{k^2}
-\frac{6m^2+6m+1}{k}+3(2m+1)-2k,
$$

$$
\frac{(m-k)(m+1-k)}k=\frac{m(m+1)}k-(2m+1)+k,
$$

$$
\frac{(m-r)^2}{2r+1}
=-m+\frac r2-\frac14+\frac{(2m+1)^2}{4(2r+1)}.
$$

求和即得作者稿 (36)，代入后为

$$
[u^{m-1}]K_2=-\frac{2m+1}{2}
\{- (2m+1)H_1+m(m+1)H_2+2(2m+1)H_o-m\}.
\tag{J}
$$

以上逐项除法、三个闭式以及代回残差均经本次自由符号核算验证为零。
合并 (I)—(J) 后，完整二次端点为

$$
\mathfrak c_2=-[u^m]J_2-16[u^{m-1}]K_2
=2p\{p^2H_2-4pH_1+8pH_o-4m\}.
\tag{K}
$$

这是 $p=2m+1$ 的特征零有限和身份，再利用每个分母为 $p$ 单位进行约化。
两端点各自已含 $p$；因此 $\overline{\mathfrak c_2}=0$ 对每个允许素数成立。
没有借用素数扫描、调和和经验同余、未证明的无限级数整性或边界 $1/p$。

### 6. 实际结论、最小参数及精度封口

由 (A)、(E)、(K)，当前环中

$$
4^DpC_D=-\lambda(\mathcal E-m)B_{\rm low}
+H^{2m}\overline{\mathfrak c_2}=0.
$$

左端此前已证明整，$4$ 为单位，故 $pC_D\in h^p\mathcal O^+$。
首一分解使最高商系数满足

$$
[L^p]U_{\rm cl}=h^{-D}p^2C_D,
\qquad
v_h([L^p]U_{\rm cl})\ge M-D+p=M-m.
$$

再由 $p=2m+1\ge m+3$，旧指定层的正规化剩余为零。原命题全部得到证明。

本次另在 $\mathbb F_5[H]/(H^5)$ 独立从整数 Chebyshev 递推重建 $C_n$ 至 $H^5$，
再计算 $d_n=(C_n-2)/H$；未把作者的传播子表作为输入。
以低方程和两条实际高带三角式直接计算，按 $1,H,H^2,H^3,H^4$ 排列得到

| 量 | 本次独立重算向量 |
| --- | --- |
| $W_1$ | $(1,4,1,4,1)$ |
| $W_2$ | $(3,2,4,4,3)$ |
| $A_0$ | $(3,0,0,0,0)$ |
| $A_1$ | $(3,0,0,3,4)$ |
| $\tau_1$ | $(3,2,2,4,0)$ |
| $\tau_2$ | $(3,2,3,4,0)$ |
| $\sigma_0$ | $(2,0,2,1,0)$ |
| $\sigma_1$ | $(1,0,4,3,3)$ |

两端点核分别为 $3H^2+3H^3+H^4$ 与 $2H^2+2H^3+4H^4$，
其负的第一项减去 $16$ 倍第二项在全部五个系数处为零。
这独立复现了作者边界表，包括逆元平方贡献和 $H^4$ 项；不是只重算其线性截断。
对最小真实参数 $p=5,a=2$，$M=10$，污染正规化高度至少 $M-4=6>5$；
$3m=6\ge5$，故该边界与一般误差论证相容。更高 $a$ 只提高这些下界。

| 实际误差来源 | 本次可用的严格界 | 结论 |
| --- | --- | --- |
| 有限参照正规化指数误差 | 至少 $h^p$ | 模 $h^p$ 可舍；下一层不可直接舍 |
| 真实 $pW_p$、中间响应乘整低指数 | $M-2m\ge3m\ge p$ | 可舍，没有改实际初值 |
| 中间响应乘非整指数 | 最短次数 $p+m>D-1$ | 不参与端点 |
| 两高带乘积 | 最短次数 $2p>D$ | 不参与端点或所需方程 |
| 模 $p$ Chebyshev 身份真实取值误差 | 至少 $M\ge p$ | 可舍 |
| (14) 的非恒定二次项等 | 至少 $H^p$ | 本次可舍；下一层须重计 |
| 线性移位作用于二次响应等反馈 | 至少 $H^{3m}\subseteq(H^p)$ | 覆盖 $m=2$ |

上述每个实际误差均先控制整性或支撑，再做约化；没有因隐藏的非整因子降低高度。

### 7. 逐项检查表

| 编号 | 实际审查项 | 结果 |
| --- | --- | --- |
| 1 | 全文冻结对象、658 行与指定哈希 | PASS |
| 2 | 参数量词、$3p<p^a$ 与商环同构 | PASS |
| 3 | 实际最高权重正规化、符号与因子 $4^D,16$ | PASS |
| 4 | 全部需要的低带形式 $p$ 整性 | PASS |
| 5 | 正规化高带整性与真实 $\tau_0$ 高度 | PASS |
| 6 | 中间奇污染与两高带支撑 | PASS |
| 7 | 已接受有限参照恰覆盖当前模 $h^p$ | PASS |
| 8 | 两条实际高带方程及其有限次数范围 | PASS |
| 9 | 准确 Chebyshev 加法式 (14) | PASS |
| 10 | 二次常数 $-4H^{2m}$ 与舍去项界 | PASS |
| 11 | Chebyshev 导数身份与合法频率范围 | PASS |
| 12 | 完整偶 Ward 方程 (18) | PASS |
| 13 | 完整奇 Ward 方程 (19) 及显式 $u$ 导数 | PASS |
| 14 | 基导数解及两个基端点的 $p$ 因子 | PASS |
| 15 | 线性移位解的构造与三角唯一性 | PASS |
| 16 | 两条端点 Ward 乘积身份 | PASS |
| 17 | $B_{\rm low}$ 与同一第一 forcing 的准确权重等式 | PASS |
| 18 | 首内部旧稿式 (15) 的实际形式证据及 Euler 操作 | PASS |
| 19 | 二次 $X,Y$ 方程两类来源完整 | PASS |
| 20 | 后续反馈下界，包括 $p=5$ | PASS |
| 21 | 二次偶显式响应及 $X(0)=0$ | PASS |
| 22 | 二次奇显式响应及必须保留的 $Y(0)=-6$ | PASS |
| 23 | $\ell,\mathscr D,\mathscr H$ 的有限合法下标及分母 | PASS |
| 24 | 二次端点核 (32) 的完整化简 | PASS |
| 25 | 三个调和和闭式与逐项符号除法 | PASS |
| 26 | 两端点及合并式 (38) 的一般素数消失 | PASS |
| 27 | 独立重建固定 $p=5$ 的传播子、两高带及完整端点 | PASS |
| 28 | 实际误差全表与最小 $(p,a)=(5,2)$ | PASS |
| 29 | 原命题、旧指定层推论及最高商高度换算 | PASS |
| 30 | 不越过有限参照精度、不声称非零或完整因子型 | PASS |

## Corrections or Missing Assumptions

- 无必需数学修正，无新增科学假设。
- 引用定位可在后续新版本中将“首内部局部结构作者稿式 (2)”注明为
  “式 (15) 的形式身份；式 (2) 是其真实点值推论”。本次证据已实际核实，
  不要求为这一定位问题改写冻结稿。
- 本报告不把作者协作符号核算充当独审；上述两条二次方程、有限和及固定五边界均由审查者重算。

## Open Risks

- $\overline{h^{-p}pC_D}$ 仍未确定；本次只证明到 $h^p$ 的下界。
- 有限参照误差从 $h^p$ 进入，即使 (K) 在特征零额外含 $p$，
  也不能据此抬高实际结论。下一层必须计算这一误差和新的移位项。
- 全部低带高阶系数被形式 Ward 身份包含，并非逐项设零；这一机制只在本次已整的有限范围内使用。
- 其余商系数、完整负 Newton 图、准确负斜率、不可约性、简单性与野分裂域均不在本次证明范围。
- 本报告未进行 Route A/B 评价、论文验收、构建或外部操作；既有接受状态与冻结稿保持不变。
