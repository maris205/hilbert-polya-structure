# Paper30：临界 Chebyshev 投影与第三 forcing 的统一常数碰撞

日期：2026-09-07。作者：`p30_third_forcing_general_independent`；
主控共同推导有限和的望远镜求值及实际常数的解释边界。
代理的历史独审角色名不构成本轮独立性。本件使用 `proof-writer`，
明确绑定同轮新有理性输入；不从五、七的幂数据拟合或逐素数补表。

## Claim

取任意素数 $p\ge5$，令 $m=(p-1)/2$、$\chi=(-1)^{m+1}$。
主用范围是此前未闭合的一般 $p\ge11$；下面的推导本身统一覆盖 $p\ge5$。
对真实 Chebyshev 传播子 $d_i(H)$ 及移位权重 $\mathsf S_i(H)$，$1\le i<p$，有

$$
\boxed{[H^m]d_i=2\chi i\,\mathbf1_{i>m},\qquad
[H^m]\mathsf S_i=-\chi\,\mathbf1_{i>m}\quad\text{于 }\mathbb F_p.}
\tag{1}
$$

令 $\mathcal F_3(H,L)$ 为已接受完整三次移位响应，不删去其四个端点项。
在所绑定新高阶有理结构成立的显式依赖下，本件证明

$$
\boxed{\mathcal F_3(H,0)=\frac{3\chi}{32}H^m+O(H^{m+1}).}
\tag{2}
$$

特别地，所有严格低于 $m$ 的标量层同时消失。写
$a_p=[H^m]\mathcal F_3(H,0)$，则实际碰撞的形式常数是

$$
\boxed{a_p=\frac{3\chi}{32},\qquad
C_p:=8\chi a_p-\frac32=-\frac34\ne0.}
\tag{3}
$$

再取 $a\ge2$、本原 $p^a$ 次根 $\zeta$，沿用实际规范

$$
h=2-\zeta-\zeta^{-1},\quad K^+=\mathbb Q_p(h),\quad
\mathcal O^+=\mathbb Z_p[h],\quad v_h(h)=1,
$$
$$
M=p^{a-1}m=v_h(p),\quad q_3=3m+1,\quad e_*=M-q_3,\quad
S=h^{-q_3}p^2\mathcal B_3.
$$

则真正实际常数满足

$$
\boxed{p^2\mathcal B_3(0)=-\frac34h^{4m}+O(h^{4m+1}),\qquad
S(0)=-\frac34h^{m-1}+O(h^m).}
\tag{4}
$$

已接受唯一首一正根簇因子的常数项进而为

$$
\boxed{P_{\rm cl}(0)=16\chi h^{m-1}+O(h^m).}
\tag{5}
$$

这里不凭常数端点单独认定整簇的准确 Newton 边、不可约性或分裂域；
这些结论还需要正参数系数的支撑证明，不在本件代证。

## Status

式 (1)—(5)：`PROVABLE AS STATED`，完整作者证明完成，
其中式 (2)—(5) 的新有理性依赖在下表明确绑定。
本件和该新依赖仍待本轮真正非作者核查，作者交叉推导不替代该检查。

## Assumptions and Frozen Inputs

| 输入 | 本件有限调用与状态 | SHA256 |
| --- | --- | --- |
| [高阶响应结构 V1](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md)，393 行 | 同轮新稿，待新独审；$L=0$ 的有理性、$p$ 整性和真实低块桥；$W_0,\ldots,W_{m-1}$ 的准确值 | `af5cd169e101948d9732cf9f913181ba2697e9fa9b4a848eebd1ffda841f21d1` |
| [一般下一层 V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md)，761 行 | 已接受；完整四项 $\mathcal F_3$、精确 $t,q$ 响应和规范 | `3d0fea6035d33c11e912946a442278711f061bebde32724ad003a3b2f9994e6d` |
| [完整四次移位剩余 V1](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md)，320 行 | 已接受；$\mathcal E=r^3\mathcal F_3+r^4E_4+O(H^{4m+1})$、$E_4(0)=-3/32$ | `ec3f6de59e55176fe11a62b36d27da516bb8d620c438fdd0037ee6c099a260da` |
| [根簇分离 V1](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md)，455 行 | 已接受；实际模 $h^M$ 桥、唯一因子及其商的高度 | `da834676ba00aa72e292acee6281b1a4ee4cd4dc8ebfab964a7fd28b503b7f2f` |

本轮完整读取新 393 行输入，核对其冻结身份；只调用下列具体新事实。
设 $u=x/4$、$\mathcal N=u\partial_u$、
$R_b(u)=[H^b]P(H,0,4u)$。有

$$
R_0=-2\log(1-u),\qquad
R_b\in\mathbb Z_{(p)}[u,(1-u)^{-1}]
\quad(1\le b\le m-1),
\tag{6}
$$

$R_b$ 仅在 $u=1$ 有极点，阶数至多 $2b$，$R_b(0)=0$、$R_b(\infty)$ 有限。
这些有理函数的模 $u^p$ 约化严格对应真实有限低块。
$b\ge1$ 时所有正阶 $\mathcal N$ 导数在无穷远为零；对零阶项则
$\mathcal NR_0(\infty)=-2$、$\mathcal N^rR_0(\infty)=0$ 对 $r\ge2$。
未假设 $R_b(\infty)=0$。

另令 $\Omega_i=i\mathsf S_i$，则新输入给

$$
W(H):=\sum_{i=1}^{p-1}\Omega_iP_i(H,0)P_{p-i}(H,0),\qquad
[H^k]W=\beta_k:=\frac{(k!)^2}{(2k+1)!},\quad0\le k<m.
\tag{7}
$$

这里 $P_i=[x^i]P$ 是 $x$ 模态，勿与式 (6) 的 $H$ 系数混淆。
因 $P_iP_{p-i}$ 对称，以 $(\Omega_i+\Omega_{p-i})/2$ 替换权重不改变 $W$。
本件不调用新输入尚未断言为零的临界正参数最高主部。

## Notation and Proof Strategy

形式计算在 $\mathbb F_p[[H]]$ 中进行，$x$ 模态始终严格小于 $p$。
$\mathcal H=H\partial_H$，在 $L=0$ 时精确响应算子是
$\mathcal R=\mathcal N-\mathcal H$。
误差 $O(H^r)$ 和实际 $O(h^r)$ 均指相应环中的整除，不表示数值拟合。

依赖链为：整数 Chebyshev 系数 $\Rightarrow$ 临界反射缺陷；
新有理结构 $\Rightarrow$ 临界前标量消失；
有限配对与 Chebyshev 微分方程 $\Rightarrow$ 临界常数只依赖旧 $W$ 层；
准确望远镜求和 $\Rightarrow a_p$；保留四次移位并检查实际精度 $\Rightarrow$ 式 (4)、(5)。

## Proof

### Step 1. 先在整数系数中计算临界投影

定义

$$
C_0=2,\quad C_1=2-H,\quad C_{i+1}=(2-H)C_i-C_{i-1},\quad
d_i=(C_i-2)/H,
$$
$$
\mathsf S_0=0,\quad\mathsf S_1=1,\quad
\mathsf S_{i+1}=(2-H)\mathsf S_i-\mathsf S_{i-1}.
$$

其生成函数直接由递推乘 $z^i$ 求和得到

$$
\sum_{i\ge0}C_i z^i=\frac{2-(2-H)z}{(1-z)^2+Hz},\qquad
\sum_{i\ge0}\mathsf S_i z^i=\frac{z}{(1-z)^2+Hz}.
\tag{8}
$$

先按 $H$ 展开有理分母，再取 $z^i$，给

$$
[H^k]\mathsf S_i=(-1)^k\binom{i+k}{2k+1},
$$
$$
[H^k]d_i=(-1)^{k+1}
\left\{\binom{i+k+1}{2k+2}+\binom{i+k}{2k+2}\right\}
=\frac{(-1)^{k+1}i}{k+1}\binom{i+k}{2k+1}.
\tag{9}
$$

二项式超过上指标时取零；最后等式可由两项分别化为
$\binom{i+k}{2k+1}$ 的倍数核对，也覆盖两边皆零的情形。

现在令 $k=m$。有 $2k+1=p$，$k+1=(p+1)/2$ 为单位，且 $i+m<2p$。
若 $i\le m$，上指标小于 $p$，故相应二项式为零。
若 $i>m$，写 $i+m=p+s$，$0\le s<p$，由
$(1+z)^{p+s}=(1+z^p)(1+z)^s$ 于 $\mathbb F_p[z]$ 得
$\binom{i+m}{p}=1$。
式 (9) 因而准确给出式 (1)。

对 $k<m$，还可写

$$
[H^k]\Omega_i=
\frac{(-1)^ki^2\prod_{s=1}^k(i^2-s^2)}{(2k+1)!}.
\tag{10}
$$

此时分母是 $p$ 单位，所以它是 $i$ 的偶多项式；$d_i$ 的同阶系数也为偶多项式。
但在 $k=m$ 时，式 (10) 的形式分母含 $p$，不能先约化再使用偶性。
令 $i^*=p-i$、$\Omega_i^-=(\Omega_i-\Omega_{i^*})/2$，式 (1) 得

$$
\boxed{\Omega_i^-=-\frac\chi2iH^m+O(H^{m+1}),\qquad
d_i-d_{i^*}=2\chi iH^m+O(H^{m+1}).}
\tag{11}
$$

记
$\Psi_i=i^2\mathsf T_i=i^2(2+Hd_i)/(2(H-4))$。
因为这里的 $d_i$ 差额外乘了 $H$，有
$\Psi_i-\Psi_{i^*}=O(H^{m+1})$。
这就是临界奇权修正与预临界偶配对的准确分界。

### Step 2. 完整端点的偶配对与不可丢弃的反对称项

沿用已接受的精确响应

$$
t=-\frac12\mathcal RP,\qquad
q=\frac18\mathcal R^2P-\frac{\mathcal RP}{4(H-4)},
\tag{12}
$$

式 (12) 的原代入验证是一般下一层输入的式 (9)—(14)：
它只用 Chebyshev 微分身份、参数导数和单位三角唯一性，
所除的数与级数仅为 $2$ 的幂、$H-4$ 及 $-i^2$（$1\le i<p$）。
故该具体身份在 $p=5$ 也成立；本件不调用该输入另需 $p\ge7$ 的二阶矩求值。

以及完整端点

$$
\mathcal F_3=
\frac{3H}{8(H-4)}\sum_i i^2\Omega_iP_iP_{i^*}
-6\sum_i\Psi_iP_it_{i^*}
+6\sum_i\Omega_iP_iq_{i^*}
+3\sum_i\Omega_it_it_{i^*}.
\tag{13}
$$

记偶部 $\bar\Omega_i=(\Omega_i+\Omega_{i^*})/2$、
$\bar\Psi_i=(\Psi_i+\Psi_{i^*})/2$，以及 $f_i=P_iP_{i^*}$。
对 $\mathcal R$ 作用的两个因子，总 $x$ 权重是 $p=0$，故合并算子为 $-\mathcal H$。
把式 (12) 代入式 (13)，分别平均 $i,i^*$，得到偶部

$$
\begin{aligned}
\mathcal F_3^{\rm ev}={}&
\frac38\sum_i\bar\Omega_i\mathcal H^2 f_i
+\frac{3}{4(H-4)}\sum_i\bar\Omega_i\mathcal H f_i
-\frac32\sum_i\bar\Psi_i\mathcal H f_i\\
&+\frac{3H}{8(H-4)}\sum_i i^2\bar\Omega_i f_i.
\end{aligned}
\tag{14}
$$

例如二次响应与 $t_it_{i^*}$ 的二次算子项合成
$\tfrac12(\mathcal R_i+\mathcal R_{i^*})^2f_i$，
一次算子项合成 $-\mathcal Hf_i/2$；这固定了式 (14) 的系数和符号。

剩余反对称部分在 $H^m$ 层只须代入 $H=0$ 的响应。
令 $U_i=2/(i4^i)$，则

$$
t_i(0)=-iU_i/2,\qquad
q_{i^*}(0)=(i^2/8-i/16)U_{i^*}.
$$

式 (13) 最后两项的反对称部分合并为
$-(3/8)\sum_i i\Omega_i^-U_iU_{i^*}$；
第一项因 $i^2f_i$ 对称而没有反对称贡献，第二项的缺陷高于目标。
而
$\sum_i i^2U_iU_{i^*}=1$：每个乘积等于 $-4/4^p$，共有 $p-1$ 项。
于是

$$
\boxed{\mathcal F_3=\mathcal F_3^{\rm ev}
+\frac{3\chi}{16}H^m+O(H^{m+1}).}
\tag{15}
$$

这个 $3\chi/16$ 来自真实临界反射缺陷，不能用预临界偶矩公式略去。

### Step 3. 所有临界前标量层同时消失

先记录所需有限提取事实。若 $K(u)$ 是 $p$-整有理函数，仅在 $1$ 有极点，
阶数 $D\le p-1$，在无穷远有限，则部分分式和
$\binom{p+d-1}{d-1}=1\pmod p$ 给

$$
[x^p]K(x/4)=\frac14\{K(0)-K(\infty)\}\quad\text{于 }\mathbb F_p.
\tag{16}
$$

这里 $4^{-p}=1/4$。每个 $d\le D$ 的同余可逐项将
$\prod_{s=1}^{d-1}(p+s)/s$ 约化，故未涉及 $p$ 分母。

固定 $0\le n<m$。在式 (14) 的前三类项中，展开权重的 $H^a$ 系数
及两个低块的 $H^b,H^c$ 系数。权重是无常数的偶多项式，次数至多 $2a+2$：
对 $\Omega$ 由式 (10)，对 $\Psi$ 由其定义中 $Hd_i$ 的额外 $H$ 得到。
一个 $\mathcal N^{2r}$ 权项可作准确有限分部

$$
\sum_{i=1}^{p-1}i^{2r}A_iB_{p-i}
=(-1)^r[x^p](\mathcal N^rA)(\mathcal N^rB).
\tag{17}
$$

用式 (6) 的完整有理函数代替有限块后，两个因子仍均零常数，
所以第 $p$ 项不使用任何单独的第 $p$ 个低模态。
所得核是 $p$-整有理函数，其极点阶数至多

$$
2b+r+2c+r\le2(a+b+c)+2\le2n+2\le p-1.
\tag{18}
$$

$1/(H-4)$ 的额外展开只减少可用的 $a+b+c$，不破坏此界。
核在 $0$ 为零。在无穷远，若 $b>0$ 或 $c>0$，至少一个正阶导数为零；
若 $b=c=0$，$\mathcal H f_i$ 或 $\mathcal H^2f_i$ 的系数因子分别为
$b+c$ 或 $(b+c)^2$，同样为零。
故式 (16) 使前三类项的 $H^n$ 系数全部为零。

式 (14) 最后一项的权重 $i^2\Omega$ 最低为四次幂、最高为 $2a+4$ 次幂，
但已有一个外部 $H$，所以其有理核阶数仍不超过
$2(n-1-a)+2a+4=2n+2$。
均分导数后 $r\ge2$，连两个零阶 $R_0$ 因子的无穷远贡献也为零。
对 $n=0$ 该项根本没有贡献。因此

$$
\boxed{[H^n]\mathcal F_3(H,0)=0,\qquad0\le n<m.}
\tag{19}
$$

此证明使用真实有理桥和实际消去的核，不从更弱的未经配对极点界外推。

### Step 4. 临界偶部不依赖未知的临界低块

对任意形式级数 $A,B$，有限系数卷积给
$[H^m]A\mathcal H^rB=[H^m](m-\mathcal H)^rA\cdot B$。
在 $\mathbb F_p$ 中 $m=-1/2$，令 $\mathscr A=-1/2-\mathcal H$。
用式 (14) 把 $\mathcal H$ 全部转移到权重，临界偶部为

$$
[H^m]\mathcal F_3^{\rm ev}
=\frac38[H^m]\sum_i\mathscr W_i f_i,
$$
$$
\mathscr W_i=
\mathscr A^2\bar\Omega_i+2\mathscr A\!\left(\frac{\bar\Omega_i}{H-4}\right)
-4\mathscr A\bar\Psi_i+\frac{Hi^2}{H-4}\bar\Omega_i.
\tag{20}
$$

下面的准确微分身份完成消元。设 $I=i^2$、$d=(d_i+d_{i^*})/2$，则
$\bar\Omega=-d-Hd'$、$\bar\Psi=I(2+Hd)/(2(H-4))$。
Chebyshev 微分方程在模 $p$ 下对 $i,i^*$ 的 $I$ 相同，故其平均满足

$$
\mathscr J:=H^2(4-H)d''+H(10-3H)d'
+\{2+(I-1)H\}d+2I=0.
\tag{21}
$$

将 $\bar\Omega,\bar\Psi$ 代入式 (20)，展开并按 $d,d',d'',d'''$ 收集，给完整身份

$$
\boxed{\mathscr W=
\frac{H(H+20)}{4(H-4)^2}\bar\Omega
+\frac{H}{H-4}\mathscr J'
-\frac{H+4}{(H-4)^2}\mathscr J.}
\tag{22}
$$

这是一条只含单位分母 $2,H-4$ 的有理微分身份；
可直接逐个比较四个导数系数，未除以 $H$ 或任何临界模态。
式 (21) 消去最后两项，结合式 (7)、(15)，得到

$$
\boxed{a_p=\frac{3\chi}{16}
+\frac3{32}[H^m]\left\{\frac{H(H+20)}{(H-4)^2}W(H)\right\}.}
\tag{23}
$$

因为括号的前因子被 $H$ 整除，这里只用 $W_0,\ldots,W_{m-1}$，
没有对未知 $W_m$ 或临界 $P$ 层作整性假定。

### Step 5. 准确有限和求值；末端先约去 $p$

令 $B_m$ 为式 (23) 中的系数提取。单位几何级数给

$$
\frac{H(H+20)}{(H-4)^2}
=\sum_{r\ge1}\frac{6r-1}{4^r}H^r.
$$

由式 (7)、$4^m=1$、$2m=-1$ 于 $\mathbb F_p$，有

$$
B_m=\sum_{k=0}^{m-1}\frac{6(m-k)-1}{4^{m-k}}\beta_k
=-2\sum_{k=0}^{m-1}(3k+2)t_k,\qquad
t_k=\frac{4^k(k!)^2}{(2k+1)!}.
\tag{24}
$$

为正确处理最后一项，以下望远镜身份先在 $\mathbb Q$ 中使用。
设 $g_k=k(2k+1)$。直接约去阶乘给

$$
\frac{t_{k+1}}{t_k}=\frac{2(k+1)}{2k+3},\qquad
(3k+2)t_k=g_{k+1}t_{k+1}-g_kt_k.
\tag{25}
$$

求和后，所有中间项抵消。终项虽含单独不整的 $t_m$，乘积却是准确的 $p$-整数：

$$
g_mt_m=mp\frac{4^m(m!)^2}{p!}
=\frac{m4^m(m!)^2}{(p-1)!}.
\tag{26}
$$

式 (26) 必须先约去 $p$，不能先将 $p$ 设为零而得到错误的零终项。
Wilson 定理与分半配对给

$$
(p-1)!=-1,\qquad
(-1)^m(m!)^2=-1,\qquad (m!)^2=\chi
\quad\text{于 }\mathbb F_p.
$$

又 $4^m=2^{p-1}=1$，所以式 (26) 的约化为
$-m\chi=\chi/2$。由式 (24)、(25) 得

$$
\boxed{B_m=-\chi,\qquad
a_p=\frac{3\chi}{16}-\frac{3\chi}{32}=\frac{3\chi}{32}.}
\tag{27}
$$

结合式 (19)，式 (2) 完成。已知五、七的幂结果至多作一致性观察，
并未参与这个全素数求和证明。

### Step 6. 保留真实四次移位并返回实际规范

已接受的合法有限移位为
$r=2\chi H^m+O(H^{m+1})$，完整端点满足

$$
\mathcal E(H,0)=r^3\mathcal F_3(H,0)+r^4E_4(0)+O(H^{4m+1}),
\qquad E_4(0)=-3/32.
\tag{28}
$$

式 (19) 的全部低层消失保证 $r^3$ 的更高修正不能再与低层响应凑成目标项。
于是式 (2) 给

$$
[H^{4m}]\mathcal E=8\chi\frac{3\chi}{32}
+16\left(-\frac3{32}\right)=-\frac34.
\tag{29}
$$

余项至少 $H^{4m+1}$。$p\ge5$ 使 $-3/4$ 为非零单位，
这里证明的是总层，不是仅引用 $E_4(0)$ 非零。

旧实际桥为 $p^2\mathcal B_3\equiv\mathcal E(h,L)\pmod{h^M}$。
该桥已经把实际内部常数的原始 $h^{M-m}$ 比较乘以端点的 $h^m$ 缺陷，
提高到 $h^M$；本件不把那些常数重新置零。
而

$$
M\ge pm\ge4m+1\qquad(p\ge5,\ m\ge2),
\tag{30}
$$

因为 $(p-4)m\ge2$。所有模 $p$ 系数提升误差也在 $h^M$ 内。
式 (29) 因此给式 (4) 的第一式，除以 $h^{3m+1}$ 后的余项准确为 $O(h^m)$。

最后调用已接受 $S=P_{\rm cl}U_{\rm cl}$，
$U_{\rm cl}(0)\equiv a_m=[L^m]S\pmod{h^{e_*}}$，
$a_m=-3\chi/64+O(h)$，$e_*>0$。
于是

$$
P_{\rm cl}(0)=\frac{S(0)}{U_{\rm cl}(0)}
=\frac{-3/4}{-3\chi/64}h^{m-1}+O(h^m)
=16\chi h^{m-1}+O(h^m),
$$

完成式 (5) 及全部主张。$\square$

## Corrections or Missing Assumptions

- 临界反射缺陷恰在 $H^m$ 出现；不能把含 $p$ 分母的偶多项式表示直接用于该层。
- 所调用新高阶有理性只需 $L=0$、$H$ 阶严格小于 $m$，且有限整性桥明确成立。
- 单极点提取之前始终均分正阶导数；不使用有 $p$ 分母的单独 $[x^p]R_0$。
- 望远镜的最后乘积先在有理数中约去 $p$ 再约化；没有零乘不整元素的非法运算。
- 常数层不是四次移位常数本身；临界前三次响应消失和同阶合并都已明确证明。

## Open Risks and Scope

1. 本件与所绑定新有理结构仍需本轮真正非作者核查；作者辅助符号核算不计独审。
2. 常数端点非零不单独决定正根簇；一般正参数支撑、全部 Newton 边及根域须由另件证明。
3. 负赋值 $p$ 次因子、完整 forcing 的分裂域、完整周期多项式及全实性不由本件解决。
4. 无素数、参数或根扫描，无拟合、旧冻结稿和入口修改，无估页、Route、PDF 或外部操作。
