# Paper30：统一正簇算子的有限末项替代

日期：2026-09-08。作者后继证明，不改冻结原稿。
来源：统一算子 V1 的非作者检查提出了下述简化；主控将其单独作者化。
提出者对原 V1 的审查不构成对本新证明的独立验收。
本件使用 `proof-writer` 与 `formula-derivation`，状态为
`PROVABLE AS STATED`（作者完整证明，待未参与推导者的变更检查）。

## 固定输入与唯一变更

取素数 $p\ge5$、$m=(p-1)/2$、$\chi=(-1)^{m+1}$，
$\mathscr E=H\partial_H+L\partial_L$，所有系数在 $\mathbb F_p$ 中。
输入为[统一算子 V1](PAPER30_TWIST_POSITIVE_UNIFIED_CRITICAL_OPERATOR_PROBE_V1_20260908.md)
的定义及 Steps 1–6：真实有限低块的自身整性、平均权精确算子、
真实临界反射修正，以及

$$
\mathcal F_3=\frac38\mathscr D W+\frac{3\chi}{16}H^m
\pmod{(H,L)^{m+1}},\qquad
\mathscr D=\mathscr E^2+
\frac{2(H-1)}{H-4}\mathscr E+\frac H{H-4}.
\tag{1}
$$

其严格预临界输入由[有限矩证明](PAPER30_TWIST_POSITIVE_FINITE_MOMENT_DIAGNOSIS_V1_20260908.md)
提供，而不再调用旧 A11 的有理性证明：

$$
W=V+W_m+O((H,L)^{m+1}),\qquad
V(H)=\sum_{k=0}^{m-1}\beta_kH^k,\qquad
\beta_k=\frac{(k!)^2}{(2k+1)!}.
\tag{2}
$$

$W_m$ 是合法的总阶 $m$ 齐次有限矩，并不假设为零。
统一算子 V1 Step 6 已证明
$\mathscr D W_m=0\pmod{(H,L)^{m+1}}$，因为
$m(m+1/2)=0$，而算子的剩余系数含一个额外的 $H$。

本件只以以下直接末项计算替代该 V1 的 **Step 7**。
其 Steps 1–6 的 Chebyshev 临界缺陷和平均权消元没有删减。

## 有限末项证明

在只含 $H$ 的多项式 $V$ 上，令 $\delta=H\partial_H$。准确有

$$
(H-4)\mathscr D V
=\{(H-4)\delta^2+2(H-1)\delta+H\}V.
\tag{3}
$$

对 $1\le n<m$，右端的 $H^n$ 系数为

$$
n^2\beta_{n-1}-2n(2n+1)\beta_n=0,
\qquad \frac{\beta_n}{\beta_{n-1}}=
\frac{n}{2(2n+1)}.
\tag{4}
$$

常数系数为零。由于 $\deg V=m-1$，右端的次数至多 $m$；
唯一剩余的最高系数就是 $m^2\beta_{m-1}$。故 (3) 甚至给出精确多项式身份

$$
(H-4)\mathscr D V=m^2\beta_{m-1}H^m.
\tag{5}
$$

这里只用 $\beta_0,\ldots,\beta_{m-1}$；每个分母中的阶乘至多为
$(2m-1)!=(p-2)!$，全部可逆。没有定义 $\beta_m$ 或任何含 $1/p$ 的末项。

为计算 (5) 的标量，在 $\mathbb F_p^\times$ 中按逆元配对，
仅 $1,-1$ 自逆，所以 $(p-1)!=-1$。因 $p-1=-1$，又有 $(p-2)!=1$。
再按 $r$ 与 $p-r$ 配对，

$$
(-1)^m(m!)^2=(p-1)!=-1,
\qquad (m!)^2=\chi.
$$

于是

$$
m^2\beta_{m-1}
=\frac{(m!)^2}{(p-2)!}=\chi,
\qquad
\mathscr D V=\frac{\chi H^m}{H-4}
\equiv-\frac\chi4 H^m\pmod{H^{m+1}}.
\tag{6}
$$

将 (2)、(6) 代入 (1)，得到

$$
\boxed{\mathcal F_3=
\left(-\frac{3\chi}{32}+\frac{3\chi}{16}\right)H^m
=\frac{3\chi}{32}H^m\pmod{(H,L)^{m+1}}.}
\tag{7}
$$

这同时保留全部正 $L$ 次数和预临界标量的消失。
$p=5,m=2$ 也属于上述分母与次数范围，没有特殊素数例外。证毕。

## 删除与保留的准确边界

采用本后继时，不再需要统一算子 V1 Step 7 的临界系数伴随卷积、
$B_m$ 有限和、$g_kt_k$ 望远镜或终项先消去 $p$。
它们在原 V1 中仍是合法而被保留的历史证明，不是被本件判错。
新的标量证明仅用同一递推的最后一个系数及有限域阶乘配对。

真实反射缺陷 $3\chi H^m/16$、完整四项端点、精确响应、
四次移位 $E_4(0)=-3/32$ 及实际误差桥全部保留。
特别是最终实际常数仍需完整合并

$$
(2\chi)^3\frac{3\chi}{32}+
(2\chi)^4\left(-\frac3{32}\right)=-\frac34.
$$

本件不单独证明完整 $C1$–$C3$，不改变 $p\ge5,a\ge2$、原科学范围、
22–30 页验收、原正式容量 FAIL 或论文立项状态；没有稿件、测页或对外操作。
