# Paper30：两倍奇素数分母的完整简单性与次项非消失

日期：2026-09-07。
状态：TWIST_TWO_PRIME_COMPLETE_SIMPLICITY_AND_NONVANISHING_ACCEPTED_GLOBAL_ROOTS_OPEN。

接续用户“继续”，本轮完成此前 $2p$ 剩余根簇和 $C,Q$ 共同根这两项明确缺口。
本处置以本轮作者稿、非作者核查及主控全文读取为依据；
不重开未变的奇素数证明、素数幂内部首层或传播子分类。
仍是同一双谐波模型、固定参数和 SUM action，没有更换构造或事后调参。

## 1. 完整结论及其准确范围

仍研究
$$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p'.$$

$C_{r,s},Q_{r,s}$ 沿用已接受的首项／次项物理规范。
对每个奇素数 $p$、全部 $\gcd(r,2p)=1$，现已证明

$$\boxed{\deg C_{r,2p}=p,\qquad
\gcd(C_{r,2p},C'_{r,2p})=\gcd(C_{r,2p},Q_{r,2p})=1.}$$

gcd 在相应特征零实分圆数域的多项式环中解释；没有假设根为实数。
特别地，首项的每个代数根均为单根，且次项在每个首项根上非零。
此前 $2p$ 内簇简单性和全部共同根排除不再 OPEN。

该结论与此前[全部奇素数结论](PAPER30_TWIST_PRIME_COMPLETE_NONVANISHING_DISPOSITION_20260907.md)
合起来覆盖分母 $p$ 和 $2p$，不等于一般合数／素数幂或全实根分类。

## 2. 真实根簇的第二尺度

令 $h=D_2$、$m=(p-1)/2$、$\kappa=\lambda-1/16$，
$S(\kappa)=h^{p-1}C_{r,2p}(1/16+\kappa)/p$。
这里 $h$ 是完成实分圆局部整数环 $\mathcal O^+$ 的素元，$v_h(p)=m$。

此前[首层定理](PAPER30_TWIST_COMPOSITE_FIRST_LAYER_AND_PROPAGATOR_DISPOSITION_20260907.md)
已经给出
$$S\in\mathcal O^+[\kappa],\qquad
\bar S=2\kappa^m(\kappa^{m+1}+1/8).$$
外层 $m+1$ 个根简单，局部因子次数为 $1$ 或 $2$；剩余 $m$ 个根处于零剩余类。
本轮没有重审这些已接受输入。

对 $p\ge5$，新的[实际权重证明](PAPER30_TWIST_TWO_PRIME_CLUSTER_WEIGHT_PROBE_V1_20260907.md)
对严格低于半阶的完整奇偶分支作三角归纳，消去临界二次驱动，
并将权重与实际有限半阶 action 对接。
令 $\operatorname{wt}(h)=2,\operatorname{wt}(\kappa)=1$，
$H,K$ 为 $h,\kappa$ 的初始符号，$w$ 为形式变量。其初始面为

$$\operatorname{in}_m S=
\frac14\sum_{j=0}^{\lfloor m/2\rfloor}
(-1)^j\binom m{2j}\binom{2j}j
\left(\frac5{12288}\right)^jH^jK^{m-2j}.$$

更具体地，
$$v_h([\kappa^b]S)\ge
\max\{0,\lceil(m-b)/2\rceil\}.$$
这不是预设平移尺度；它来自实际递推的全低半权重闭合。
奇指数的第 $p$ 项是唯一达到该初始权重的阶乘层，
高阶指数和中央平方均已分别估值，不能把 $p!$ 项删除。

在 $p\ge7$ 时，取 $\tau^2=h$、$\kappa=\tau K$。
缩放后的剩余多项式为非零常数乘以

$$G_m(K;\gamma)=[w^m]((1+Kw)^2+\gamma w^2)^{-1/2},
\qquad \gamma=5/3072.$$

[有限多项式辅助证明](PAPER30_TWIST_DEGENERATE_FLIP_QUARTIC_JET_LEMMA_V1_20260907.md)
给出其次数为 $m$，且全部根简单：
二阶微分身份在普通点排除重根，奇点则直接代入排除。
[Newton／提升证明](PAPER30_TWIST_TWO_PRIME_CLUSTER_NEWTON_PROBE_V2_20260907.md)
将这些根合法提升回实际 $S$，并与已接受的外层根计数拼合。
因此不是仅证明一个辅助多项式可分。

以下先限于 $p\ge7$。若 $m$ 偶，全部 $m$ 个内簇根都有 $v_h(\kappa)=1/2$。
若 $m$ 奇，其中 $m-1$ 个有该赋值，另一个满足 $v_h(\kappa)>1/2$；
这个更深根仍然是单根，不预设其下一层精确赋值。
这些赋值均在适当局部代数扩张中解释，不是实根坐标。

$p=5$ 时 $\gamma$ 的剩余值为零，通用非退化面必须停用。
[五素例外精确证书](PAPER30_TWIST_TWO_PRIME_FIVE_CLUSTER_CERTIFICATE_V1_20260907.md)
对唯一必要边界 $s=10$ 直接在二次数域计算：
取 $5$-单位 $N=1189085184$、$F=NS$，
则 $h^{-2}F(hK)$ 整且约化为 $K^2+2$。
该式在特征五可分，故两个内簇根均简单，且 $v_h(\kappa)=1$。
对 $p=3$，旧首层中 $m=1$ 的根本就全部简单，无需另做算例或重开证明。

## 3. 同一个次项在所有首项根上非零

[完整负指数正规化证明](PAPER30_TWIST_TWO_PRIME_OUTER_NONVANISHING_PROBE_V1_20260907.md)
实际覆盖所有奇素数 $p\ge3$，不只覆盖文件名中的 outer 根。
其结论是

$$\boxed{\frac{h^p}{p}Q_{r,2p}\in\mathcal O^+[\lambda],
\qquad \overline{\frac{h^p}{p}Q_{r,2p}}=\frac1{16}.}$$

等价地，
$$\overline{h^{m+1}Q_{r,2p}}=\frac{(-1)^{m+1}}{16}.$$
所以在每个局部代数整数参数上，$v_h(Q)=-(m+1)$，特别是 $Q\ne0$。
已接受的 $S$ 具有单位最高系数，其全部根均局部整，
因而该常数约化直接排除全部共同根，不依赖内簇简单性。

证明使用原递推的完整 $n<2p$ 分支和 $n=2p+1$ 末端。
两个 $p!$ 极点先用精确末端系数配对相消，再作剩余约化；
普通卷积由 $e^Ae^{-A}=1$ 消去。
保留下来的 Frobenius 项在第 $w^{m+1}$ 阶制造偶模缺陷，
精确给出 $[w^{m+1}]e^{-\bar A}=1/16$。
这里不能用旧低半支替代完整分支，也不能先模掉非整项。

## 4. 独立核查与新增验证

- [通用实际根簇联合独审](PAPER30_TWIST_TWO_PRIME_CLUSTER_INDEPENDENT_CHECK_20260907.md)：
  22 项全部 PASS，覆盖 JET、WEIGHT、NEWTON V2 全链。
- [五素例外独审](PAPER30_TWIST_TWO_PRIME_FIVE_CLUSTER_INDEPENDENT_CHECK_20260907.md)：
  15 项全部 PASS，实际重算六系数、改标剩余及独立低模方程。
- [全部两倍奇素数次项独审](PAPER30_TWIST_TWO_PRIME_NONVANISHING_INDEPENDENT_CHECK_20260907.md)：
  18 项全部 PASS，覆盖所有 $p\ge3$ 的完整正规化与 gcd 推论。

三份审查均为对应证明的非作者核查，无数学修正要求；主控已经全文读取
五份作者／辅助证明和三份审查。
NEWTON V1 完整保留，最终绑定 V2；V2 仅补一个公式反斜杠及文件尾空行，
主控与独审者均核对了精确差异，没有为排版修正重开未变数学。
本轮按 proof-writer 将辅助身份、实际作用量桥、例外边界与最终推论分开陈述，
再由非作者检查完整依赖链；没有用作者自检替代独立核查。

四次 jet 与最低权重桥接中有协作交叉推导，未重复计为贡献或互相充当独审。
作者符号自检的 stdout 标签不构成独立认证。
非作者根链审查覆盖实际权重、辅助可分性和最后提升，不只核一个末端公式。

本轮只运行一般新身份的符号核对和 $p=5$ 退化边界的精确证书。
没有新增素数／根扫描，没有重跑旧63／六例诊断，没有用有限例子外推一般定理。
保留旧作者稿、锁、失败记录和接受证据；没有修改旧数学结论。

## 5. 接下来仍未完成的义务

1. 奇素数幂的后续内部层与完整首项：此前第一个内部 forcing
   $\mathcal B_{p\mid p^a}$ 的根、因子型和极点结论保持接受，
   但它不是完整 $C_{r,p^a}$；必须保留非整内部模态及阶乘贡献。
   下一有界目标先到 $2p$：处理 $p+1\le n<2p$ 的非内部模态，
   再确定第二内部 forcing 的准确首个非零层。
   新的 $p!$ 层从 $n=p+1$ 就出现，不能仅沿 $V_p$ 的已知极点尺度递推；
   新规范的整性和同阶取消均须证明，不预设它复制首层的剩余多项式。
2. 其余合数分母的完整简单性与共同根问题。
   本轮全 $2p$ 结论不能外推到 $2p^a$ 或其他组合。
3. 实际参数根的全实性。此前真实正／逆传播子的有限保根分类继续保持，
   但它作用于 $t$，不是受限非线性 forcing 的参数根分类。
   不重复已排除的普遍逆传播子、路径、Hermitian 或自动实循环芽捷径。
4. 整体研究的新意与自然正文容量仍未做最终认证；不以本轮定理直接授予立项。

这些是准确接续项；不再把 $p$ 或 $2p$ 的简单性、$C,Q$ 互素列为未证明。
新结果效力仅限本地数学包，没有正文估页、正式候选票、试写测页、Paper30 项目、
PDF、Route 评价、投稿、上传或其他外部操作。
Batch07 仍为 **3/5**，Paper30 未立项、Paper31 未开展；
22–30页实质正文、完整证明与独立验收要求不变。

## 6. 新输入身份

| 本轮输入 | SHA256 |
| --- | --- |
| 四次 jet 与有限多项式辅助稿 | 58a65cc7ca2f646f3e40c7d558ca731df887991e0b3ef3bbc596a5b8712dcf97 |
| 实际低半权重与阶乘桥 | 6af2251223c61eb255cbd35d62421374f6f2c339e97d1de6f5484b057b7b7cef |
| 实际 Newton 与提升 V2 | 6dd8cc117889c37aeb15001caf4c63584b3160bf7b9c32978d90ee0a57f1c616 |
| 五素退化边界精确证书 | 806aaae02e7bf8c8adebd905b63667be0c5adf134bac4c815f31d9c00ef67fe6 |
| 完整次项非消失作者稿 | e3dad8a1e2cec0fd95b69aefc123474e37502abc5ee9e32ee82521a5bc1af572 |
| 通用根簇22项独审 | 3cec308a578b4051b23b134ec83d190e98f685925787e32ac7d0584958e6966e |
| 五素例外15项独审 | 10705aaa77b776fa6adbc7633d919b5c1a38e4dbcb0b79be38031e93d90783f5 |
| 次项非消失18项独审 | f7d5d9175ba6da766d7b3cdc7c0f29692866ffcb497ebfb0467f874fb3bc14da |
