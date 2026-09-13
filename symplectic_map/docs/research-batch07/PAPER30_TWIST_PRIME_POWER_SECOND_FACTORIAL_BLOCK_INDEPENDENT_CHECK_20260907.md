# Paper30：第二阶乘带与下一非内部模态块独立核查

日期：2026-09-07。核查者：late_nonnenmacher_source。
本轮完整读取并使用 proof-writer；只核查本轮新增作者稿。

## Claim

固定任意奇素数 $p$、$a\ge2$、$s=p^a$ 及任意本原 $s$ 次单位根。
保持原物理正 kick、固定参数与 SUM action，使用
$h=D_1$、$\rho=-h$、$L=\rho\lambda$、
$d_n=-D_n/h$、$m=(p-1)/2$、$M=p^{a-1}m$。

本票核查以下实际结论：

- 对 $1\le j<p$，$p^2V_{2p+j}\in\mathcal O^+[L]$，且
  $\overline{p^2V_{2p+j}}=jT_j/8$，入口剩余为 $1/16$。
- 其有限生成函数为
  $Z_*=x/(16A)+Lx^2/(8A^2)=N_x^2(-\log A)/8$，
  其中 $A=1-x/2+(1-4L)x^2/16$。
- 每个剩余多项式的次数和作者最高系数公式正确；
  实际系数最小赋值为 $-2M$，点值准确性保留必要的非零剩余条件。
- 作者 Step 7 的 $\mathcal B_3$ 仅有普通首层取消
  $p^2\mathcal B_3\in h\mathcal O^+[L]$；
  不据此求解 $V_{3p}$ 或判断准确下一层。

## Status

**PROVABLE AS STATED。以下 14 项限定核查全部 PASS。**

未发现阻断性数学缺口，不要求修改冻结作者稿。
没有缩小全部奇素数、全部 $a\ge2$ 或参数多项式的范围。
本票不重新认证旧阶段，不增加完整端点或完整共振结论。

## Exact input and independence

已全文读取 475 行
[SECOND_FACTORIAL_BLOCK V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md)，
并实际核对其 SHA256：

    3ff45f425669adbd012245f5cf605083a72e3cccb131cc6469f787cc58920e04

本轮还全文读取 169 行已接受
[SECOND_INTERNAL_DISPOSITION](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_DISPOSITION_20260907.md)，
SHA256：

    77069ed7697b42887d794871ecd0a2d51647d54527ce8c90bc4432cceee7debe

其绑定的旧 POST_POLE_BLOCK 和 SECOND_INTERNAL_FORCING 已在此前全文核查，
本轮对应哈希仍分别为 0a70394315cfe78b860c6ac46eec53bb58ccb8b3e432c1108438f7e721ee4c34、
278ce73d9844c8a30b93b8952b8a3a178aa577f1c808fce48c333be721c97f15。
本票只调用其已接受结论，不重授上轮 25 项独审。

核查者未参与本轮作者稿的推导，未向作者提供修补证明。
本轮独立预核、自由符号核算和冻结文本核查不以主控／作者的协作同式为证据。

## Assumptions and notation

$\mathcal O^+$ 为既定完成实分圆整数环，$v_h(p)=M>2m$，
剩余域为 $\mathbb F_p$。使用的旧结论为：
低块 $V_n$ 在 $n<p$ 时整，$V_1=1/2$ 精确，
$pV_p\in h^{M-m}\mathcal O^+[L]$，
$pV_n$ 在 $p<n\le2p$ 时整，以及 $\overline{pV_{2p}}=-1/4$。

写
$V=P+R_1+R_2$，三段的次数分别为
$1,\ldots,p-1$、$p,\ldots,2p-1$、$2p,\ldots,3p-1$；
递推只取已求前缀。
记旧块剩余为
$Y=\sum_{j=0}^{p-1}\overline{pV_{p+j}}x^j=xA'/(2A)$，
新块剩余为
$Z=\sum_{j=0}^{p-1}\overline{p^2V_{2p+j}}x^j$。
两者常数项均为零，但真实内部模态没有置零。
所有指数使用都严格限定到次数小于 $3p$。

## Proof strategy and dependency map

先核新阶乘带和真实入口，再核四项展开的逐阶整性；
这些完成后才取剩余并形成有限 Jacobi 方程。
随后核有理解、参数系数和点值边界。
最后单列 $\mathcal B_3$ 的有限普通首层取消，
不把不可逆的 $j=p$ 作为三角递推的一步。

## Independent proof audit

### 1. 实际规范及严格次数边界：PASS

对每个奇 $p$ 有 $3p-1<p^2\le s$，
所以本轮模态均不是真共振。
当 $p=3,a=2$ 时最高模态为 $8<9=s$，
所用指数亦始终小于 $3p=p^2$。
因此 $v_p(k!)=\lfloor k/p\rfloor\le2$ 对所有实际使用的 $k$ 成立。
作者没有把这个界延长到 $(3p)!$。

### 2. 低块的第二阶乘带及符号：PASS

$P$ 逐系数整；小于 $p$、$2p$、$3p$ 的指数系数
分别以 $1,p,p^2$ 清分母后整。
对 $k=2p+r$、$0\le r<p$，
两个 $p$ 倍数贡献 $2p^2$，两段非零剩余类各贡献 $(p-1)!$，
尾段贡献 $r!$，所以

$$
\overline{\frac{p^2}{(2p+r)!}}=\frac1{2r!}.
$$

这与第一带的 $-1/r!$ 不同，作者正负号正确。
$k<2p$ 的项乘 $p^2$ 后至少含一个 $p$，不贡献普通剩余。
所有取模都在清分母以后进行。

### 3. 入口的实际内部项与高度：PASS

独立按 $x^{2p}$ 次数核得
$[x^{2p}]e^V=E_{2p}+\sum_{r=p}^{2p}V_rE_{2p-r}+V_p^2/2$。
低指数中唯一可贡献 $p^2$ 归一化普通剩余的项是 $P^{2p}/(2p)!$，
给出 $1/8$。

其余实际项的高度分别至少为：
$V_pE_p$ 的 $M-m$，
$p<r\le2p$ 线性项的 $M$，
$V_p^2/2$ 的 $2(M-m)$。
第二谐波只需次数 $2p-1$ 的指数，归一后至少为 $M$。
这些高度全部严格为正，尤其没有删除实际 $V_{2p}$ 或 $V_p^2$。
再除以 $\bar d_{2p+1}=-1$，入口剩余准确为 $1/16$。

### 4. 高块展开的全部可达项：PASS

在特征零的有限次数商环中，准确式为

$$
e^{\alpha V}=e^{\alpha P}
\left(1+\alpha R_1+\alpha R_2+\frac{\alpha^2}{2}R_1^2\right)
\pmod{x^{3p}}.
$$

$R_1R_2$、$R_1^3$ 从 $3p$ 起，$R_2^2$ 从 $4p$ 起，
因而不影响本轮系数，即便这些项带有非单位阶乘。
$R_1^2$ 则不能忽略。
这里的次数理由不依赖高模式的 $h$ 赋值，未把极点系数误当作小量。

### 5. 四项三角整性及真实初值：PASS

乘 $p^2$ 后，四类项分别写成：

| 来源 | 合法整数因子分组及剩余指数范围 |
| --- | --- |
| 低块 | $p^2e^{\alpha P}$，次数小于 $3p$ |
| 旧高块线性项 | $(pR_1)(pe^{\alpha P})$，余下次数小于 $2p$ |
| 新高块线性项 | $(p^2R_2)e^{\alpha P}$，余下次数小于 $p$ |
| 旧高块二次项 | $(pR_1)^2e^{\alpha P}/2$，余下次数小于 $p$ |

归纳初值是实际
$p^2V_{2p}=p(pV_{2p})\in p\mathcal O^+[L]$，
不是将 $V_{2p}$ 设为零。
每个新 $n=2p+j$ 只用此前系数，且
$\bar d_n=-j^2$ 在 $1\le j<p$ 为单位。
所以作者在约化前已证明整个实际块的逐系数整性。

### 6. 第二带的有限 Frobenius 使用：PASS

在所需次数中，
$\bar P^p=x^p/2+O(x^{2p})$，
故 $\bar P^{2p}=x^{2p}/4+O(x^{3p})$。
与第 2 项合并，得到

$$
\overline{p^2e^{\alpha P}}
=\frac{\alpha^2}{8}x^{2p}A^{-\alpha}\pmod{x^{3p}}.
$$

乘去 $x^{2p}$ 后只需低于 $p$ 阶的整指数，
所以此处使用低块平方传播子输入合法。
$\alpha^{2p}=\alpha^2$ 只用于整数 $\alpha=1,2$；
作者没有误用 $L^p=L$，也没有把第一带公式延用到不满足其界的次数。

### 7. 完整四项剩余桥：PASS

令 $pR_1=x^p\mathcal Y$、$p^2R_2=x^{2p}\mathcal Z$。
旧高块线性项应与第一阶乘带结合，而非与普通低指数首层结合。
逐项核得公共因子 $x^{2p}A^{-\alpha}$ 前的系数分别为

$$
\frac{\alpha^2}{8},\qquad
-\frac{\alpha^2Y}{2},\qquad
\alpha Z,\qquad
\frac{\alpha^2Y^2}{2}.
$$

它们合成
$\alpha Z+\alpha^2(Y-1/2)^2/2$，即作者 (18)。
$Y(0)=0$ 和 $Z(0)=0$ 均来自真实整数初值的剩余。
入口 $V_p^2$ 的普通剩余虽为零，整个 $R_1^2$ 仍有后续贡献；
$p=3$ 时其首次贡献进入本文 $\mathcal B_3$ 所需系数，
$p\ge5$ 时已进入块内后续 forcing，作者范围说明正确。

### 8. 有限 Jacobi 方程的符号和唯一性：PASS

将第 7 项分别取 $\alpha=1,2$ 代回原负传播子递推，
得到

$$
N_x^2Z=\mathcal JZ+\mathcal K(Y-1/2)^2\pmod{x^p},
$$
$$
\mathcal J=\frac{x}{2A}+\frac{2Lx^2}{A^2},\qquad
\mathcal K=\frac{x}{4A}+\frac{2Lx^2}{A^2}.
$$

两组二次谐波系数不同，作者均保留正确。
$\mathcal J,\mathcal K$ 无常数项，且 $j^2$ 对 $1\le j<p$ 可逆，
所以零常数项的有限解唯一。
这一步不涉及 $j=p$ 的不可逆方程。

### 9. 二阶变化身份的系数：PASS

核查者独立核对作者的
$U_\varepsilon=\varepsilon+U(e^\varepsilon x)$。
其代入平方传播子方程仍成立，因为每项 $x^ke^{kU}$
都变成同一个新变量 $e^\varepsilon x$ 下的项。
这是特征零的辅助族，不是修改实际零常数分支。

第一次与第二次变化为
$G=1+N_xU$ 和 $H_*=N_x^2U$。
第二次求导后的 $H_*$ 系数为 $\mathcal J$，
$G^2$ 系数为 $x/(2A)+4Lx^2/A^2=2\mathcal K$。
故

$$
(N_x^2-\mathcal J)H_*=2\mathcal K G^2.
$$

除以 $8$，再用 $Y-1/2=-G/2$，
恰得到第 8 项的源，而不是差一个因子二或四。

### 10. 有理解及新自由符号检查：PASS

因此候选解准确为

$$
Z_*=\frac18N_x^2U
=\frac{x}{16A}+\frac{Lx^2}{8A^2}.
$$

核查者本轮以自由 $x,L$ 独立计算
$N_x^2Z_*-\mathcal JZ_*-\mathcal K(Y-1/2)^2$，
通分残差为零，入口系数为 $1/16$。
$G,H_*,Z_*$ 均为分母常数项为单位的有理级数，
只含 $2$ 的常数分母；故在所有奇素数下系数整。
这允许从特征零身份约化，而无需在特征 $p$ 中定义无限对数或指数。
由第 8 项的有限唯一性，得到作者整个块的剩余式。

### 11. 参数次数、最高系数和准确系数尺度：PASS

从 $Z_*=-N_xY/4$ 得
$\overline{p^2V_{2p+j}}=jT_j/8$，
即旧剩余的 $-j/4$ 倍。
最高系数分别为

$$
\frac{2k}{4^{k+1}}\quad(j=2k),\qquad
\frac{(2k+1)^2}{4^{k+2}}\quad(j=2k+1).
$$

在明确的 $1\le j<p$ 范围，分子非零、分母为单位，
因此剩余次数确为 $\lfloor j/2\rfloor$。
结合实际整性，原模态的系数最小赋值恰为 $-2M$。
作者没有将剩余次数误写为实际多项式的完整次数上界。

### 12. 逐参数边界及退化参数：PASS

所有首层身份位于 $\mathbb F_p[L]$；
没有除以 $L$、$q$ 或旧 forcing 的根多项式。
所以 $L=0$、$q=0$ 和旧内部根类都包含在多项式结论中。

实际点值取得 $-2M$ 仍要求 $T_j(\bar L)\ne0$；
旧根类被包含不等于该类中每个模态都为单位。
作者正确保留这个区别。
仅 $j=1$ 因剩余是常数 $1/16$，对全部局部代数整数参数自动准确。

### 13. 第三 forcing 的普通首层取消：PASS

作者 (18) 的实际整性和剩余桥覆盖 $N=3p-1,3p-2$，
所以 $p^2\mathcal B_3$ 先已整。
代入 forcing 给出
$-2[x^p](\mathcal JZ+\mathcal K(Y-1/2)^2)$，系数正确。

因 $\mathcal J,\mathcal K$ 无常数项，
此系数只依赖 $Y,Z$ 低于 $p$ 的已知项；
替换成完整有理式不引入未知实际 $V_{3p}$。
有理身份把它变成 $-2[x^p]N_x^2Z_*=-2p^2[x^p]Z_*$。
这里 $[x^p]Z_*\in\mathbb Z_{(p)}[L]$，
故剩余为零，得到且只得到
$p^2\mathcal B_3\in h\mathcal O^+[L]$。
这一论证使用有理 $Z_*$ 的整系数，不是越过 $p$ 阶直接约化无限对数。

### 14. 真共振边界与结论范围：PASS

上述 $\mathcal B_3$ 由严格低于 $3p$ 的前缀定义，
不需要除以 $d_{3p}$。
特别对 $p=3,a=2$，$3p=s=9$ 已是真共振，
作者只定义 forcing，没有按内部非共振递推定义 $V_9$。
其余参数也没有被授予第三模态整性、准确 $q_3$ 或更高层结论。
所有本轮身份适用于任意允许的本原根；
完整 $C_{p^a}$、其与 $Q$ 的关系、根实性及完整内部塔仍不在结论内。

## Verification actually run

本轮在冻结稿到齐前独立建立新有理方程，并运行自由符号检查；
全文读取后，与实际稿的四项桥、二阶身份及范围逐项比对。
实际输出为：

    REVIEWER_SECOND_FACTORIAL_RATIONAL_RESIDUAL 0
    entry_coefficient 1/16
    no prime, parameter-point, or root samples

没有重跑旧阶段、没有输入素数／本原根／参数根清单。
符号残差只核对新有理身份；
一般阶乘带、真实初值、四项三角整性和端点使用界由上述独立论证承担。

## Corrections or missing assumptions

没有提出数学修正或作者新版本要求。
必须保留的条件包括：严格次数小于 $3p$、
实际 $p^2V_{2p}$ 初值、四项指数桥、
仅在 $j<p$ 使用单位三角唯一性，
以及第三 forcing 结论只到普通剩余取消。

## Open risks and delivery boundary

- $p^2\mathcal B_3$ 的准确首个非零层和实际 $V_{3p}$ 不在本票。
- 不以本块剩余方程代替更高精度的实际传播子与模态响应。
- 不推断完整 $C_{p^a},Q_{p^a}$、全部根实性或完整塔。
- 只新增本独审报告；冻结作者稿、旧稿、入口、脚本和接受状态均未修改。
- 未作额外文献检索、样本扫描、正文估页、论文立项、PDF、Route 或对外操作。

