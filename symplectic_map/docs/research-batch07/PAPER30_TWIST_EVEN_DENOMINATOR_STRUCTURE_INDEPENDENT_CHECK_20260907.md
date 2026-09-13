# 偶数半阶消元与两倍奇素数首项：非作者独立核查

日期：2026-09-07。审查者：`p30_twist_leading_structure_probe`，未参与被审
半阶消元、局部主层或外部剩余因子型的作者构造。
本轮完整读取并使用 `proof-writer` 技能；本票不重审已接受的奇素数包。

## Claim

核查全部偶数分母的半阶作用量公式，以及全部 $s=2p$、$p$ 奇素数、
$\gcd(r,2p)=1$ 时的实际 primitive 约化

$$
S_{2p}=\frac{h^{p-1}}pC_{r,2p}\in\mathcal O^+[\lambda],\qquad
\bar S_{2p}=2\kappa^p+\frac14\kappa^m,
$$

其中本件特有的尺度为 $h=D_2$，$m=(p-1)/2$、$\kappa=\lambda-1/16$。
同时核查外部简单根、零剩余根簇、$\deg\gcd(C,C')\le m-1$，
以及外部因子的局部一次／二次类型和两个 Legendre 条件。

## Status

**`PROVABLE AS STATED`；下列 18 项全部 PASS，没有未修复的数学缺口。**

已全文读取并绑定
[作者稿](PAPER30_TWIST_EVEN_DENOMINATOR_STRUCTURE_PROBE_V1_20260907.md)，
SHA256 为 `2fc421fe37d923c5b87bcd76fcafd9ba160dacd6c7951139d1226036e7b9967a`。
本票只针对这些新身份，不把旧奇素数证明或旧有限算例重复计为新增验收。

## Assumptions and Notation

沿用作者的物理正 kick、SUM action、固定参数规范：

$$
v_n=-\frac{E_{n-1}/2+\lambda F_{n-2}}{D_n},\quad E=e^v,\quad F=e^{2v},
\qquad C=-E_{s-1}-2\lambda F_{s-2}.
$$

对 $s=2p$，$\xi=-\zeta$ 是本原 $p$ 次根，$\pi=\xi-1$；
$\mathcal O=\mathbb Z_p[\xi]$，$\mathcal O^+=\mathbb Z_p[h]$，
$h=D_2$。在大环按 $\pi$ 约化，在完成实子环按 $h$ 约化，两个剩余域均为
$\mathbb F_p$，但不能把大环 $\mathcal O/(h)$ 当作域。

作者对代数闭包中根的“零剩余类”按延拓赋值的最大理想解释，准确含义是
$v_h(\lambda-1/16)>0$。若根簇需要分歧扩域，该说法并不声称
$v_h(\lambda-1/16)\ge1$ 或根差属于 $h\mathcal O_{\rm ext}$。
这是剩余映射的明确约定，不改变作者的根簇结论。

## Proof Strategy and Dependency Map

先在特征零核半阶临界值，再审两个传播子估值层及低半部分支。
随后逐个检查高阶指数的阶乘赋值，最后才在剩余域进行有限截断运算。
次数、根簇和局部因子型必须在 primitive 整性与约化保持次数之后推导。

新局部结论所需的标准工具已核对一手来源：完成 DVR 中互素首一因子唯一
Hensel 提升，以及有限非分歧扩域与有限剩余域扩张的对应。其假设在本件
特征零、有限剩余域情形满足。
[Milne，Theorem 7.33](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=123)，
[Proposition 7.50 及 Example 7.54](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=129)。
本轮亲读了相关陈述和证明，未增加本地文献 PDF。

## Itemized verdicts

| 项目 | 判定 | 核查重点 |
| --- | --- | --- |
| 1. 半阶作用量与整体规范 | PASS | $C_{r,2M}=-4MG$，各 $2$ 和 $M$ 因子正确 |
| 2. 高半部消元 | PASS | 高变量只线性出现，其系数为相应低阶驻值方程 |
| 3. 中央平方与低部余项 | PASS | 中央贡献 $-T_M^2/(2D_M)$；不能删除两项指数势 |
| 4. 本原根与传播子奇偶层 | PASS | $\xi=-\zeta$ 本原，偶模式含 $\pi^2$，奇模式单位，$D_p=4$ |
| 5. $D_2$ 实尺度 | PASS | $h/\pi^2=-4\pmod\pi$，$D_1$ 在此反而是单位 |
| 6. 低半部整性 | PASS | $n<p$ 的偶部整、奇部含 $\pi$；递推只用单位阶乘 |
| 7. 局部奇部消去与 $\kappa$ | PASS | 奇部产生 $-1/16$，不是从其他可积构造移入 |
| 8. 有限低支的显式解 | PASS | 截断对数与几何系数只在正确阶数范围使用 |
| 9. 高指数层的整性 | PASS | $e^A$ 因始于二次仍整；$e^{\pi B}$ 必须另查阶乘 |
| 10. 唯一 $p!$ 层与符号 | PASS | 奇数 $k=1,p$ 恰为首赋值，$\pi^{p-1}/p!\equiv1$ |
| 11. 普通奇项与中央项合并 | PASS | 有限卷积精确给出 $-\mathcal F_{p-1}/32$ |
| 12. Frobenius 修正项 | PASS | 仅 $B$ 一次系数留下 $-q^m/16$，不可省略 |
| 13. 有限截断指数身份 | PASS | $\mathcal F_{p-1}=-q^{p-1}$；不以完整有理解替换高系数 |
| 14. primitive 转回实环 | PASS | 整性先成立，再除公共尺度；最终单位剩余值为 $1$ |
| 15. 次数保持与根簇 | PASS | $\deg C=p$，外部 $m+1$ 根简单，零剩余簇次数 $m$ |
| 16. 特征零 gcd 界 | PASS | 仅簇因子可有重根，故次数界 $m-1$；不是平方自由定理 |
| 17. $\mathbb F_{p^2}$ 与局部因子型 | PASS | Frobenius 为 $\alpha\mapsto1/(64\alpha)$，外部局部次数仅 $1,2$ |
| 18. Legendre 条件与边界 | PASS | 两固定点条件正确；$p=3$ 合法，未扩展到实根或 $C,Q$ 互素 |

## Independent proof checks

### 1. 全偶数分母半阶式

对 $s=2M$，取 $P=\sum_{n<M}v_nt^n$。
在有限作用量中，每个 $v_j$、$j>M$ 只能线性出现，因为两个高半部模式的
总次数已经大于 $2M$。它的系数为

$$
D_{2M-j}v_{2M-j}+\frac12E_{2M-j-1}+\lambda F_{2M-j-2}=0.
$$

这些指数系数只使用 $P$，不依赖中央或更高模式，所以消去合法。
中央模式的动能和势能贡献是
$D_Mv_M^2/2+T_Mv_M$，驻值为 $v_M=-T_M/D_M$，
故贡献 $-T_M^2/(2D_M)$。
低部动能次数至多 $2M-2$，在所取系数中为零。
因此

$$
G=\frac12[t^{2M-1}]e^P+\frac\lambda2[t^{2M-2}]e^{2P}
-\frac{T_M^2}{2D_M}.
$$

权重 Euler 身份给出 $2MG=-C/2$，合并就是作者式 (4)。
$D_M=4$ 只在最后使用；没有把 $D_{n+M}=4-D_n$ 误作非线性分支对称性。
此式也不等于较低分母 $C_{r,M}$ 的闭合递推。

### 2. 两个模式层和低阶约化

$\xi^p=1$ 且 $\xi\ne1$，所以其阶为 $p$。
偶模式直接因式分解得
$D_n/\pi^2=-n^2\pmod\pi$；奇模式为 $2+\xi^n+\xi^{-n}=4\pmod\pi$。
中央 $p$ 模式属于奇层，精确为 $4$，并不是内部小除数。

乘以 $\pi^n$ 后，递推是

$$
\widehat v_n=-\frac{\pi\widehat E_{n-1}/2+
\lambda\pi^2\widehat F_{n-2}}{D_n}.
$$

若先前奇系数都含 $\pi$，则奇指数系数也含 $\pi$。
对偶 $n$，两个驱动均至少含 $\pi^2$，正好抵消 $D_n$ 的赋值；
对奇 $n$，两个驱动分别至少含 $\pi,\pi^3$，除单位后仍含 $\pi$。
从第一阶归纳，得到 $\widehat P=A+\pi B$，$A,B$ 整且奇偶性如作者所述。

在所需低阶范围，除以 $\pi$ 后的奇方程给出 $\bar B=-xe^{\bar A}/8$。
再代入偶方程，第一谐波贡献为 $-x^2e^{2\bar A}/16$，因此

$$
(x\partial_x)^2\bar A=(\lambda-1/16)x^2e^{2\bar A}\pmod{x^p}.
$$

设 $w=x^2$、$q=\kappa/4$，四倍的 $w$-Euler 平方核正好给出
$\bar A=\sum_{j=1}^m q^jw^j/j$。
相应 $\bar B=-x\sum_{j=0}^{m-1}q^jw^j/8$。
低阶三角分母 $4j^2$ 非零，故此解由唯一性确定。

### 3. 为什么高指数必须多留一层

在半阶作用量中，$A$ 的最小次数为 $2$。
计算 $e^A$ 至 $x^{2p-2}$，最多用 $A^{p-1}/(p-1)!$，这些系数整。
但奇指数 $e^{\pi B}$ 至 $x^{2p-1}$ 可用到 $k=p$，而

$$
v_\pi(\pi^k/k!)=k-(p-1)\lfloor k/p\rfloor,
\qquad 1\le k<2p.
$$

在奇数 $k$ 中恰好 $1,p$ 给出赋值 $1$，其他至少为 $3$。
在偶数 $k>0$ 中赋值至少为 $2$，所以所需 $e^{2\widehat P}$ 的偶部约化
没有额外首层修正。

利用 $p=\prod_{j=1}^{p-1}(1-\xi^j)$，
$p/\pi^{p-1}\equiv(p-1)!\equiv-1$；因此
$\pi^{p-1}/p!\equiv(-1)(-1)=1$。
得到合法有限系数身份

$$
(e^{\widehat P})_{\rm odd}/\pi
\equiv e^{\bar A}(\bar B+\bar B^p)\pmod\pi.
$$

这一步在特征零先识别整的组合，才作约化。
它不从“低支整”错误推出“任意高指数整”，也没有删去 $p!$ 项。

### 4. 中央平方、Frobenius 与有限截断

令 $\mathcal E=e^{\bar A}$、$\mathcal F=\mathcal E^2$。
低于等于 $m$ 阶有 $\mathcal E_j=q^j$，于是

$$
\mathcal F_{2m}=2\sum_{j=0}^{m-1}q^j\mathcal E_{2m-j}+q^{2m}.
$$

普通奇项是右侧和式乘以 $-1/16$；中央项为 $-q^{2m}/32$。
二者合并恰为 $-\mathcal F_{2m}/32$。
另一方面，$\bar B^p=-x^p/8\pmod{x^{2p}}$：其余奇幂取 $p$ 次方后
至少到 $x^{3p}$。这个项给出 $-q^m/16$。
连同第二谐波势项，精确得到

$$
\overline{\widehat G/\pi^2}=\frac\kappa2\mathcal F_{p-1}-\frac{q^m}{16}.
$$

对 $\mathcal F_{p-1}$，必须使用截断 $\bar A$。
补入 $m+1$ 至 $p-1$ 阶的有限对数后，补项的平方从 $w^{p+1}$ 起，
故在模 $w^p$ 下只留一次补项。完整有理因子的该阶系数为零，而修正为

$$
-2q^{p-1}\sum_{j=m+1}^{p-1}\frac{p-j}{j}
=2m q^{p-1}=-q^{p-1}.
$$

这证明作者式 (13)，并非将有限 $\mathcal E_j$ 错换成任意高阶几何系数。
整个证明在 $\mathbb F_p[q]$ 中进行，未除以 $q$ 或 $\kappa$。

### 5. primitive 及实坐标的返回

以上同时证明 $\widehat G/\pi^2$ 整。
由 $C=-4pG$，在特征零合法得到

$$
S^\pi=\frac{\pi^{2p-2}}pC=-4\widehat G/\pi^2\in\mathcal O[\lambda].
$$

其约化为 $8q^p+q^m/4$。
因为 $4^p=4$、$4^m=1$ 于 $\mathbb F_p$，这就是
$2\kappa^p+\kappa^m/4$。
注意 $\kappa$ 是多项式变量，未将 $\kappa^p$ 替换为 $\kappa$。

真实实尺度满足 $h/\pi^2=-4\pmod\pi$，故
$S=(h/\pi^2)^{p-1}S^\pi$ 的倍因子约化为 $1$。
$S$ 具有实子域系数，大环整性于是降至 $\mathcal O^+$。
这也核对了为何此处必须用 $D_2$：$D_1\equiv4$ 是单位，不具有要求的赋值。
每个互素 $r$ 都给出同样的本原 $\xi$ 计算，因此量词覆盖全部分子。

### 6. 根簇和 gcd 界

先以最高次单位系数将 $S$ 化为首一多项式。
约化保持次数 $p$，其两个互素首一部分为
$\kappa^m$ 和 $\kappa^{m+1}+1/8$。
互素因子 Hensel 引理给出相应的次数 $m,m+1$ 的整因子。

所有根都整，因为多项式已首一。
前一因子的全部根约化为零，故按重数计恰有 $m$ 个根满足
$v_h(\lambda-1/16)>0$；并未进一步确定它们的赋值或互异性。
后一约化因子的导数 $(m+1)\kappa^m$ 在根处非零，
所以每个外部剩余根在适当非分歧局部扩域中唯一提升成简单根。

两个提升因子互素，外部因子平方自由，故所有重数都来自次数 $m$ 的簇因子。
特征零中，一个非零次数 $m$ 多项式与其导数的 gcd 次数至多 $m-1$。
这直接证明作者的界，无需依赖约化导数最高次数是否塌缩。
$p=3$ 时 $m=1$，该界为零，边界合法。

### 7. 外部局部因子型及 Legendre 条件

对任意外部剩余根 $\alpha$，由 $\alpha^{m+1}=-1/8$ 得

$$
\alpha^{p+1}=1/64,\qquad \alpha^p=1/(64\alpha),\qquad
\alpha^{p^2}=\alpha.
$$

因此全部外部根在 $\mathbb F_{p^2}$，Frobenius 轨道只有一次或二次。
简单剩余因子唯一 Hensel 提升，且对应非分歧扩域的 Galois 群与剩余域群
一致，所以外部因子在完成局部域上的不可约次数恰为这些轨道长度。
这不是原全局数域因子次数的声明。

一次轨道满足 $\alpha=1/(64\alpha)$，所以只能取 $\alpha=\pm1/8$。
在 $\mathbb F_p$ 中直接计算

$$
(1/8)^{m+1}=\frac18\chi_p(2),\qquad
(-1/8)^{m+1}=-\frac18\chi_p(-2).
$$

分别与 $-1/8$ 比较，得到作者的准确条件：
$+1/8$ 出现当且仅当 $\chi_p(2)=-1$，
$-1/8$ 出现当且仅当 $\chi_p(-2)=1$。
两个条件未互换，亦没有引入二次互反律或实嵌入结论。

## Verification actually run

本轮独立运行一次纯符号核验：取抽象反射传播子
$(D_1,D_2,D_3,D_4,D_5)=(A,B,H,B,A)$，在
$\mathbb Q(A,B,H,\lambda)$ 中由原递推构造完整首项，
减去对应的半阶作用量表达式；残差严格为零。
输出为 `INDEPENDENT_EXACT_PASS general reflected half-action identity`。
该检查针对新增消元身份，不代入任何实际素数、三角数值或数值根。

一般 prime 主层、Frobenius 层和有限截断身份由上面的通用证明核查承担，
没有重跑旧奇素数包或旧六分母递推，没有新增素数列表或根扫描。

## Corrections or Missing Assumptions

无需修改输入或改变科学结论。唯一需要明确的阅读约定是：
分歧扩域中的“零剩余根簇”仅指正的延拓赋值，不额外承诺被原基域素元 $h$ 整除。
按该标准剩余映射解释，作者原陈述成立。

## Open Risks and Delivery Boundary

- $p\ge5$ 时簇内 $m$ 个根的完全简单性尚未证明；本票不将簇重数当作实际重根。
- 其他偶数分母只有所述精确半阶公式，未获得同一个 primitive 约化。
- 本件不推出偶数分母的 $\gcd(C,Q)=1$ 或全部根实性。
- 外部一次／二次因子型只属于完成局部域，不自动给全局因式分解。
- 仅新写本独审报告；输入作者稿、旧证明、入口、冻结锁和其他验收产物未改。
