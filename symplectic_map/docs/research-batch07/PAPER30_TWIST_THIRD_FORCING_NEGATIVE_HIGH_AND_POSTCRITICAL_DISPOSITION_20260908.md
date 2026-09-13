# Paper30：全部高系数预临界段与最高项后临界层的接受处置

日期：2026-09-08。
状态：`NEGATIVE_HIGH_PRECRITICAL_AND_TOP_POSTCRITICAL_ACCEPTED; NEGATIVE_FACTOR_OPEN`。
主控已全文读取下列三份新证明及其各自独立报告；本件科学接受严格限于列明结论。

## 1. 本轮接受的共同高度与最高项

对全部素数 $p\ge5$、整数 $a\ge2$，保持同一双谐波实际分支、固定参数、
传播子负号及 SUM action。令

$$m=(p-1)/2,\quad M=p^{a-1}m,\quad D=3m+1=m+p,\quad e_*=M-D,$$
$$S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
U_{\rm cl}=\sum_{r=0}^{p}u_rL^r,\qquad a_m=[L^m]S.$$

已接受分解的 $P_{\rm cl}$ 首一次数 $m$，$U_{\rm cl}$ 次数 $p$，$a_m$ 为单位。
本轮共同结论为

$$\boxed{p[L^j]\mathcal B_3\in h^m\mathcal O^+
\quad(m<j\le D),\qquad
U_{\rm cl}\equiv a_m\pmod{h^{M-p}\mathcal O^+[L]}.}$$

因此全部非恒定商系数从旧高度 $e_*$ 到 $e_*+m-1$ 的各层均为零；
共同下一可能高度为 $e_*+m=M-p$。这是实际多项式的逐系数结论，
不是只在若干参数或素数上观察到消失。

最高项另有本轮接受的更强结论

$$\boxed{p[L^D]\mathcal B_3\in h^{m+2}\mathcal O^+,
\qquad v_h(u_p)\ge e_*+m+2=M-p+2.}$$

上一轮最高项的下一可能高度 $M-p+1=M-2m$ 也已证明为零，不再 OPEN。
本轮不声称新的两个可能高度 $M-p$、$M-p+2$ 非零，不将下界写成等号。
商常数 $u_0$ 只与 $a_m$ 同余，并未被证明精确相等。

## 2. 严格加强的负根界与点值范围

令

$$\delta_{\rm neg}=\min\left\{\frac{M-p}{p-1},\frac{M-p+2}{p}\right\}.$$

共同高度控制 $1\le r<p$ 的商项，最高项使用其更强高度；单位常数的
唯一最低赋值论证给出

$$\boxed{v_h(\beta)\le-\delta_{\rm neg}
\quad\text{对每个 }U_{\rm cl}(\beta)=0.}$$

对上一轮
$\delta_+=\min\{e_*/(p-1),(M-p+1)/p\}$，两个候选比值分别提高
$m/(p-1)$ 与 $1/p$，故对所有允许参数均有
$\delta_{\rm neg}>\delta_+>e_*/p$。
这一合并应用已在共同预临界独审中条件核查；最高项另审接受后，条件现已满足。

最小值仅在 $(p,a)=(5,2)$ 由第一项控制，此时 $\delta_{\rm neg}=5/4$；
其余允许参数均由第二项控制。可始终使用上述最小值公式，无需另设构造。

任意有限扩域中的非零参数若 $-\delta_{\rm neg}<t=v_h(\ell)\le0$，则

$$v_h(U_{\rm cl}(\ell))=0,\qquad v_h(S(\ell))=mt.$$

合并既有正簇距离式，记 $t_*=(m-1)/m$ 及正簇根 $\alpha_1,\ldots,\alpha_m$，
完整点值式的范围现在是 $t>-\delta_{\rm neg}$：

$$v_h(S(\ell))=
\begin{cases}
mt,&t<t_*,\\
(m-1)t_*+\max_jv_h(\ell-\alpha_j),&t=t_*,\\
m-1,&t>t_*.
\end{cases}$$

$\ell=0$ 时为 $m-1$；根处允许无穷值。
最初端点 $-e_*/p$ 和上一轮端点 $-\delta_+$ 现在都包含；新端点
$-\delta_{\rm neg}$ 仍不包含。实际 forcing 与模态的换算保持
$v_h(\mathcal B_3)=D-2M+v_h(S)$、$v_h(V_{3p})=m+1-2M+v_h(S)$。
未改变正簇的根、临界抵消或分裂域。

## 3. 新证明机制与独立证据

共同高系数证明保留实际初值 $q=Y^{\rm act}_0\in h^{M-m}\mathcal O^+[L]$，
而不把它改为零或常数。实际响应满足

$$\Delta Y=q(1+\mathcal NP)+O(h^M),\qquad
\Delta Z=-q\mathcal N^2P/2+O(h^M).$$

配对差中两类线性项准确合为
$-q\sum_{i+j=p}ijP_iP_j(jC_i+p\delta_i^{\rm mid})$，
真实组合缺陷 $C_i\in h^{2m}$ 使完整误差达到 $h^{M+m}$。
先投影去掉参数次数至多 $m$ 的模型，再除以 $p$，并单独控制 action
与全部 Euler 余项，得到共同 $h^m$。冻结前作者协作纠正的一个多余 $i$
已记在新稿中；绑定冻结稿独审无需进一步修订。

最高项新稿构造与实际低偶段准确匹配的有限多项式参照，
其正规化指数误差达到 $h^p$。这足够覆盖当前 $h^{m+2}$，
不需要假设全局 $R_{m+1,0}$ 整性。完整保留下一移位、低奇有限和和两条高带修正后，
端点闭式中的每项仍含 $p$；所有实际约化分母均为单位，覆盖 $p=5$。
全局新核极部没有被求出，只是不再是这次有限计算的必要依赖。

| 新证据 | 独立核查与处置 |
| --- | --- |
| [全部高系数首层稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_LAYER_PROOF_V1_20260908.md)及[独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_LAYER_INDEPENDENT_CHECK_V1_20260908.md) | 343 行作者稿；29 项全部 PASS，接受 $pC_j\in h$，后由下项加强 |
| [全部高系数预临界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_PRECRITICAL_PROOF_V1_20260908.md)及[独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_PRECRITICAL_INDEPENDENT_CHECK_V1_20260908.md) | 304 行作者稿；8 个完整检查项全部 PASS，并核查合并根界；接受共同 $pC_j\in h^m$ |
| [最高项后临界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md)及[独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_INDEPENDENT_CHECK_V1_20260908.md) | 619 行作者稿；28 项全部 PASS；接受 $pC_D\in h^{m+2}$ |
| [次高项另一作者推导](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_SUBTOP_PROBE_V1_20260908.md) | 379 行，主控全文读取；保留为作者稿，未单独授予全文独审 PASS；其结论已被上述完整共同证明覆盖，不作为接受依赖 |

主控、各作者及作者侧子检查的代数核算不计非作者独审。
三份独立报告只核本次新证明及必要输入，没有重跑旧正簇、已接受最高项层或旧构建。
独立符号残差用于核对代数，不替代一般证明、整性与实际误差控制。

本次直接证据的 SHA256：

| 文件 | SHA256 |
| --- | --- |
| HIGH_LAYER 作者稿 | `0d3aa48f80052d8ee8da5a9808e873a6b63c0054a3b8a262c7596bf03558222a` |
| HIGH_LAYER 独审 | `3601a76aa118d60a16f59f63cf17d431f99695d7210c447a738c856af12bf31e` |
| HIGH_PRECRITICAL 作者稿 | `7d869eff22fda9975b0da74233c2d93bc962d7ccb91e209e6fbdee32c8c91516` |
| HIGH_PRECRITICAL 独审 | `77c9df4286d55b4b715f705396659882eea65e57bb39ae0a32c9833c004d9f75` |
| TOP_POSTCRITICAL 作者稿 | `730fd03b7da722111250813635ac9f9ac052928b516dee805a28204124df4de7` |
| TOP_POSTCRITICAL 独审 | `156fba39b1aa6f32714a5ed480845227c5b26b4090781f3a10e427ac3e466d49` |

## 4. 保留记录、下一项和交付边界

[上一轮最高项处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_DISPOSITION_20260908.md)
及其原模 $h$ 稿的非整约化错误、原稿字面 FAIL 和后继修复均完整保留。
本轮 PASS 不追溯改写原失败稿。
[更早负因子边界处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_FACTOR_DISPOSITION_20260907.md)
中的 DVR 反例仍有效：只给系数下界不能决定完整 Newton 图。

下一对象仍是同一负赋值 $p$ 次因子的完整下凸包。需要判定有关中间商系数
在当前首个可能高度 $M-p$ 是否非零，以及最高项在 $M-p+2$ 层的实际剩余。
已消失的旧层不再反复列为待算；要以相关非零锚点决定准确斜率和因子型。
继续算最高项时，有限参照只保证到 $h^p$，而二次临界项从 $h^{2m}$ 起；
$p=5$ 时这些项正好进入下一层，不能自动复用本次一次修正截断。

完整负因子的准确根赋值、不可约性、简单性、根间距及野分裂域仍 OPEN。
一般第二／第三 forcing 互素、完整素数幂 $C,Q$、其他合数和全实根问题未因此闭合。
Papers27–29 的接受产物、正文 22–30 页及正式新意和容量要求均不改。
Batch07 本地验收仍为 **3/5**；Paper30 未立项，Paper31 未开展。
本件不构成候选票、论文稿件、PDF 或 Route 评价；效力仅限本地，无对外操作。
