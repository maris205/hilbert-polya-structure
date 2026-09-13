# Proof Package：有限参照首个 $h^p$ ghost 的非作者全文独立审查

日期：2026-09-08。审查者：`/root/negative_top_quadratic_review`。
目标稿作者为 `/root/negative_hp_ghost_author`；本审查者未参与本稿推导或撰写。
使用 `proof-writer` 技能，已为本轮重新全文读取该技能。
仅新增本报告，不修改作者稿、入口、接受处置或其他研究状态。

审查对象：[有限参照首个 $h^p$ ghost 作者稿 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md)，全文 458 行。
冻结输入 SHA-256：

```text
9a4b698fe1a4f4e236010e735c0105bb687fd9ebf554e36840e2b9302f8c4894
```

## Claim

对任意素数 $p\ge5$、整数 $a\ge2$，在固定实际双谐波分支上，令

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=p+m,
\qquad \mathscr R=\mathcal O^+/(h^{p+1}).
$$

准确有限参照为

$$
T=\sum_{r=1}^{p-1}W_ru^r,\qquad
Q_{\rm ref}=T-\sum_{r=1}^{p-1}\frac{u^r}{r},\qquad
G=-\log(1-u)+Q_{\rm ref}.
$$

本次审查以下三个相连的原命题：

1. 对 $c=1,2$，次数 $N<2p$ 的参照指数系数乘 $p$ 后整，并有

   $$
   pe^{cG}\equiv-\frac c4h^pu^p(1-u)^{-c}
   \pmod{(h^{p+1},u^{2p})}.
   $$

2. 令 $\delta=h^p/4$、$\eta=1+\delta$，则实际正规化指数高带在所需有限次数内满足

   $$
   E_c=cf_c(\tau-\eta).
   $$

3. 对同一传播子及低带下、仅将缺陷常数 $\eta$ 换成 $1$ 的唯一辅助高带解，
   有

   $$
   (\tau,\sigma)=\eta(\widehat\tau,\widehat\sigma),\qquad
   4^DpC_D=\eta\widehat{\mathfrak C}=\widehat{\mathfrak C}
   \quad\text{于 }\mathscr R.
   $$

最后的等式仅消去有限参照 ghost 对完整最高端点的净 $h^p$ 贡献。
它不判断总剩余 $\overline{h^{-p}pC_D}$，不证明 $pC_D\in h^{p+1}\mathcal O^+$。

## Status

**PROVABLE AS STATED。全文独审 PASS；下列 26 项全部 PASS。**

原命题保持不变，无须削弱或增加科学假设。未发现必须修订的数学错误或缺失的关键步骤。
本次通过严格限于上述参照误差、真实高带缩放和净 ghost 贡献；
不给其他 $H^p$ 响应、总端点剩余或更高消失阶附带授予 PASS。
独审结果不自行改变项目接受或出版状态。

## Assumptions

- $h=2-\zeta-\zeta^{-1}$，$\zeta$ 为本原 $p^a$ 次根，
  $\mathcal O^+=\mathbb Z_p[h]$，$v_h(h)=1$，$v_h(p)=M$，剩余域为 $\mathbb F_p$。
- 实际传播子 $d_n=-(2-\zeta^n-\zeta^{-n})/h$ 及实际偶、奇权重递推保持不变。
  原下标严格小于 $3p<p^a$。
- 所需偶低系数 $W_r$、$r<p$ 整且模 $h$ 为 $1/r$；
  奇低系数 $A_r$、$r<m$ 整且模 $h$ 为 $1/2$。
- 所需正规化高系数 $pW_{p+j}$、$0\le j\le m$ 与
  $pA_{p+j}$、$0\le j<m$ 整；真实 $W_p$ 及中间奇系数的赋值下界为 $-2m$。
- 实际最高权重身份为

  $$
  4^DC_D=-[u^{p+m}]e^W-16[u^{p+m-1}]e^{2W}A.
  $$

定向读取的已接受依赖仅为下列文件的有限参照、实际整性与支撑部分，
未重开旧 Ward 或二次边界证明：

| 必要依赖 | 本次确认的 SHA-256 |
| --- | --- |
| [前一后临界稿 Step 1—2](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md) | `730fd03b7da722111250813635ac9f9ac052928b516dee805a28204124df4de7` |
| [完整二次边界稿 Step 1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md) | `e754946905524581d55cbf1d893c8141db7fc69a1aa33050d778c1754bf789a2` |

旧参照的 $O(h^p)$ 结论不作为当前更高精度的充分证据；其首误差在下文重新核算。

## Notation

沿用 $u=Lx^2/4$、$w=T$、$a=A_{<m}$、$f_c=e^{cw}$，
其中低指数只取次数 $<p$；$\tau_j=pW_{p+j}$、$\sigma_j=pA_{p+j}$。
$\Theta=u\partial_u$、$\mathcal Q=2\Theta+1$。
$\mathcal L_e,\mathcal L_o,\Delta_e,\Delta_o$ 均使用作者稿定义的同一实际传播子。
记 $\mathcal K=f_1/2+16uf_2a$。

本报告中 $\bar R^p$ 表示剩余域多项式的 $p$ 次幂，
即作者稿 Frobenius 公式中的 $\overline R^{,p}$。
同余 $pe^{cG}$ 始终按有限的 $u^N$、$N<2p$ 逐系数解释。

## Proof Strategy

先审计有限指数展开中每一种阶乘分母，独立确定唯一存活项及其常数。
再按实际下标分类恢复两条高带和完整端点；
用三角唯一性证明共同缩放，而不是只在端点上插入误差。
最终只需零阶有限解即可判定这一 ghost 的净贡献。

## Dependency Map

1. 实际低带整性、准确 $W_1$ 和有限次数上界决定首参照误差。
2. 准确低带匹配与正规化高带整性将该误差转换为缺陷常数 $\eta$。
3. 实际污染高度与次数支撑保证当前模 $h^{p+1}$ 的方程及端点完整。
4. 同一算子的单位三角性使真实解为辅助解的共同 $\eta$ 倍。
5. 零阶端点的 $p$ 因子令这个共同缩放在模 $h^{p+1}$ 不改变端点。

## Proof

### 1. 新工作环及唯一存活的有限指数项

由 $M\ge5m$ 与 $m\ge2$，有

$$
M\ge p+1,\qquad M-2m\ge3m\ge p+1.
\tag{A}
$$

因此当前商环的特征为 $p$，但在乘 $p$ 之前不能约化非整指数系数。
$Q_{\rm ref}\in h\mathcal O^+[u]$，无常数项且次数 $<p$，并且

$$
e^{cG}=(1-u)^{-c}\sum_{q\ge0}\frac{c^qQ_{\rm ref}^q}{q!}.
\tag{B}
$$

因 $c=1,2$，前因子具有整数系数。固定 $N<2p$ 后只有 $q\le N$ 参与：

| 指数项数 | 乘 $p$ 后的高度下界 | 模 $h^{p+1}$ 的作用 |
| --- | --- | --- |
| $0\le q<p$ | $M+q\ge p+1$ | 消失，包含 $q=0$ |
| $q=p$ | $p$，因为 $p/p!=1/(p-1)!$ 为单位 | 唯一可能存活 |
| $p<q<2p$ | $q\ge p+1$，因为 $v_p(q!)=1$ | 消失 |

这同时证明了所有所需正规化系数整，且无需任何全局有理核假设。
设 $Q_{\rm ref}=hR$，则唯一可能存活项为

$$
h^p(1-u)^{-c}\frac{c^p}{(p-1)!}\bar R^p.
\tag{C}
$$

在 $\mathbb F_p^\times$ 中将元素与逆元配对，只有 $1,-1$ 自逆，
故 $(p-1)!\equiv-1$；而 $c^p=c$。
Frobenius 给 $\bar R^p=\sum_{r=1}^{p-1}\bar R_r^pu^{rp}$。
由于 $R$ 无常数项且截断为 $u^{2p}=0$，此式只保留 $r=1$。

实际偶入口由 $d_2=h-4$ 和 $d_2W_1=-4$ 精确给出

$$
W_1=\frac4{4-h},\qquad R_1=\frac{W_1-1}{h}=\frac1{4-h}.
$$

因此 $\bar R^p=u^p/4\pmod{u^{2p}}$，代入 (C) 得

$$
pe^{cG}\equiv-\frac c4h^pu^p(1-u)^{-c}
\pmod{(h^{p+1},u^{2p})}.
\tag{D}
$$

负号、系数 $c/4$、$u^p$ 起点及全部使用范围均与作者稿 (2) 一致。
只有在乘 $p$ 并给出整性后才做 Wilson 与 Frobenius 约化。

### 2. 正规化实际指数与缺陷常数的符号

由参照定义，$G_{<p}=W_{<p}$ 准确成立，且 $G_r=1/r$ 对 $r\ge p$。
于是 $W-G$ 始于 $u^p$，在特征零中有有限精确身份

$$
e^{cW}=e^{cG}\{1+c(W-G)\}\pmod{u^{2p}}.
\tag{E}
$$

对 $0\le j\le m$，$pG_{p+j}$ 在当前环中为 $\mathbf1_{j=0}$：
当 $j>0$，分母 $p+j$ 为单位，其高度为 $M\ge p+1$。
(E) 的高带旁只出现次数 $<p$ 的低指数，这些系数整并与 $f_c$ 准确相同；
$p(W-G)$ 的相应高系数也已整。由 (D)—(E) 得

$$
E_c=cf_c(\tau-1)-\frac c4h^p(1-u)^{-c}.
\tag{F}
$$

低带剩余保证 $f_c\equiv(1-u)^{-c}\pmod h$，故在乘 $h^p$ 的项中可以替换，
得到 $E_c=cf_c(\tau-\eta)$、$\eta=1+h^p/4$。
因此负的直接参照误差使缺陷常数增加，而不是减少；没有漏掉相反符号。

### 3. 新精度下的真实污染和两条高带

由 (A)，真实 $pW_p$ 在当前商环为零，所以偶高带常数固定为 $\tau_0=0$。
这没有将真实内部模态置零，也没有倒置 $d_0$。

对目标 $N\le p+m-1$ 中的 $p[u^N]e^{2W}A$，按奇响应下标 $r$ 分类：

- $r<m$ 时响应整，低指数部分乘 $p$ 后高度至少 $M$；指数高带部分保留为 $E_2a$。
- $m\le r<p$ 时指数下标 $N-r\le p-1$，其系数整；
  乘积正规化高度至少 $M-2m\ge p+1$，故不参与当前环。
- $r\ge p$ 时只有 $r=p+j$、$0\le j<m$ 可能参与，旁边指数下标 $<m<p$，
  正规化贡献为 $f_2\sigma$。

非整指数与中间响应相遇最早在 $p+m$，两高带相乘最早在 $2p$；两者均超出所需目标。
因此作者稿 (17) 对所有所需次数成立。
当 $N<p$，只有前两类且没有指数高带，故整个正规化乘积为零；
特别包含奇入口所需的 $N=p-1$，不是只核查 $N\ge p$。

将 (F) 和上述分类代回原实际递推，逐项得到

$$
(\mathcal L_e+\Delta_e)\tau=8\eta uf_2,\qquad \tau_0=0,
$$

$$
(\mathcal L_o+\Delta_o)\sigma=-\mathcal K(\tau-\eta).
\tag{G}
$$

偶式的符号来自 $-4E_2=-8f_2(\tau-\eta)$；
奇式中 $-8E_2a$ 与 $-E_1/2$ 合为 $-\mathcal K(\tau-\eta)$，
$-8uf_2\sigma$ 移到左侧。因此两个源项必须使用同一个 $\eta$。
完整端点同步为

$$
4^DpC_D=-[u^m]f_1(\tau-\eta)
-16[u^{m-1}]f_2\{\sigma+2a(\tau-\eta)\}.
\tag{H}
$$

### 4. 同一传播子下的精确共同缩放

保持 (G) 的传播子、低核和所有移位完全不变，仅令缺陷常数为 $1$，
得到作者定义的有限辅助解 $(\widehat\tau,\widehat\sigma)$。
偶正下标为 $d_{2p+2j}$、$1\le j\le m$；奇下标为
$d_{2p+2j+1}$、$0\le j<m$，均为非共振单位。
非对角乘子 $8uf_2$ 严格提高 $u$ 次数。
因此偶系数可依次唯一求出，再唯一求出奇系数，且偶常数单独固定为零。

标量 $\eta$ 与上述全部算子及低核交换，故
$\eta\widehat\tau$ 满足第一方程及常数条件，
$\eta\widehat\sigma$ 满足第二方程，因为
$\eta(\widehat\tau-1)=\eta\widehat\tau-\eta$。
唯一性给出

$$
(\tau,\sigma)=\eta(\widehat\tau,\widehat\sigma).
\tag{I}
$$

(H) 中所有项因而共同乘 $\eta$，所以
$4^DpC_D=\eta\widehat{\mathfrak C}$。
辅助系统不是另一个实际 forcing，也未把真实传播子替换成理想传播子。
这一步包含了 ghost 对高带的源响应，而非只改端点公式。

### 5. 零阶完整端点足以消去这一 ghost

模 $h$ 时，$d_n=-n^2$，平移 $n\mapsto n+2p$ 不改变剩余。
低函数为 $w_0=-\log(1-u)$、$a_0=f/2$、$f=(1-u)^{-1}$、$g=f^2$。
在有限合法次数内，零阶辅助解为

$$
t=-2\Theta w_0=-2uf,
\qquad s=-\mathcal Qa_0=-\frac{1+u}{2}f^2.
\tag{J}
$$

独立代入零阶算子 $\mathcal L_{e0}=-4\Theta^2+8ug$、
$\mathcal L_{o0}=-(2\Theta+1)^2+8ug$，得

$$
\mathcal L_{e0}t=8ug,\qquad
\mathcal L_{o0}s=-\left(\frac f2+8uf^3\right)(t-1).
$$

结合相同的单位三角性，(J) 确是当前辅助系统的零阶解。
两个端点核有准确有理身份

$$
f(t-1)=-(1+2\Theta)f,
\qquad
g\{s+2a_0(t-1)\}=-(3+2\Theta)(ga_0).
\tag{K}
$$

提取次数 $m$、$m-1$，得到

$$
\overline{\widehat{\mathfrak C}}
=(2m+1)\left([u^m]f+16[u^{m-1}]ga_0\right)=0.
\tag{L}
$$

所有系数整且只涉及小于 $p$ 的低下标；无 $1/p$ 可抵消前面的 $p=2m+1$。
所以 $\widehat{\mathfrak C}\in h\mathscr R$，从而

$$
(\eta-1)\widehat{\mathfrak C}
=\frac{h^p}{4}\widehat{\mathfrak C}=0\quad\text{于 }\mathscr R.
$$

与 (I) 合并即得原命题 (4)。整个论证只用零阶端点，不使用此前更强的消失层，
更没有假定新的总 $h^p$ 剩余已经为零。原命题得证。$\square$

### 6. 直接项、源响应及最小参数的独立复核

固定辅助高带，只改变端点的缺陷常数时，直接增量为

$$
\delta\left([u^m]f+32[u^{m-1}]ga_0\right)
=\delta\{1+8m(m+1)\}=-\delta.
\tag{M}
$$

高带源响应由 (I) 是 $\delta t,\delta s$；其中
$g(s+2a_0t)=-(1+5u)f^4/2$，所以其端点增量为

$$
\delta\{2m+4m(m+1)(2m-1)\}=+\delta.
\tag{N}
$$

最后两步只使用 $m=-1/2$ 于 $\mathbb F_p$。
在自由符号 $m$ 下，两个括号之和准确为 $(2m+1)^3$；
故作者稿 (28)—(29) 的符号与有限系数计算通过。
本次独立符号核算已验证两条零阶方程、(K) 的两个核、响应核、
上述多项式身份及模 $2m+1$ 的余式，全部残差为零。

另作不承担一般量词的固定 $p=5$ 检查：
对任意较高低带斜率 $r_2,r_3,r_4\in\mathbb F_5$，

$$
(4u+r_2u^2+r_3u^3+r_4u^4)^5\equiv4u^5\pmod{u^{10}},
$$

实际展开约化与 Frobenius 一致。
正规化参照 $h^5$ 层从 $u^5$ 至 $u^9$ 的系数分别为
$(1,1,1,1,1)$（$c=1$）和 $(2,4,1,3,0)$（$c=2$），吻合 (D)。

本次还在 $\mathbb F_5[H]/(H^6)$ 独立从整数 Chebyshev 递推构造传播子，
解出相同实际低带，分别以 $\eta=1$ 和 $\eta=1+H^5/4$ 求解两条有限高带。
计算只比较 ghost 引入的差，不据此审定其他 $H^5$ 响应。结果为

| 比较对象 | $H^5$ 系数差 |
| --- | --- |
| 偶高带 $u^0,u^1,u^2$ | $(0,2,2)$ |
| 奇高带 $u^0,u^1$ | $(3,4)$ |
| 完整端点，$1,H,\ldots,H^5$ 全系数差 | $(0,0,0,0,0,0)$ |

各高带逐系数满足实际 $\eta$ 缩放，完整端点差为零。
对最小真实参数 $(p,a)=(5,2)$，$M=10$、$M-2m=6=p+1$；
因此最坏污染恰在当前模数 $h^6$ 消失，而不是凭严格更高的未证下界舍去。
更高 $a$ 只提高这些污染下界。

### 7. 逐项检查表

| 编号 | 实际审查项 | 结果 |
| --- | --- | --- |
| 1 | 冻结稿全文、458 行及指定哈希 | PASS |
| 2 | 一般参数与新环特征、真实高度不等式 | PASS |
| 3 | 同一实际递推、最高权重及有限整性依赖 | PASS |
| 4 | 参照低带准确匹配与 $Q_{\rm ref}\in h\mathcal O^+[u]$ | PASS |
| 5 | 所有有限指数项的阶乘分母与正规化整性 | PASS |
| 6 | 唯一存活的 $q=p$ 项及其精度 | PASS |
| 7 | Wilson 配对与 $c^p=c$ 的合法约化 | PASS |
| 8 | Frobenius 与 $N<2p$ 只保留 $r=1$ | PASS |
| 9 | 实际 $W_1=4/(4-h)$ 与斜率 $1/4$ | PASS |
| 10 | 首参照误差的负号、常数及两种 $c$ | PASS |
| 11 | 参照 $pG_{p+j}$ 的新精度正规化 | PASS |
| 12 | 从参照转回实际高指数的有限乘积整性 | PASS |
| 13 | 低核替换与正确的 $\eta=1+h^p/4$ | PASS |
| 14 | 真实偶初值在新环为零而非实际置零 | PASS |
| 15 | 中间奇污染、两高带支撑及奇入口 $N=p-1$ | PASS |
| 16 | 两条实际高带与完整端点同步使用同一缺陷 | PASS |
| 17 | 偶常数处理、非共振对角元与三角唯一性 | PASS |
| 18 | 同一传播子下精确共同 $\eta$ 缩放 | PASS |
| 19 | 完整端点整体缩放 | PASS |
| 20 | 零阶辅助解的两条方程与有限下标 | PASS |
| 21 | 零阶完整端点含 $p$ 因子且无非整抵消 | PASS |
| 22 | 净 ghost 贡献为零且不借用更强旧消失 | PASS |
| 23 | 直接 $-\delta$ 与源响应 $+\delta$ 的符号及闭式 | PASS |
| 24 | 独立固定五重算与最小真实污染边界 | PASS |
| 25 | $u^{2p}$、$h^{p+1}$ 两个截断边界未被外推 | PASS |
| 26 | 不接受其他 $H^p$ 响应或完整总剩余 | PASS |

## Corrections or Missing Assumptions

- 无必需数学修正，无新增科学假设。
- 本报告把作者稿 $\overline R^{,p}$ 按其明确的 Frobenius 上下文解释为 $\bar R^p$；
  可作记号排版简化，但不影响命题或证明。
- 作者核算不作为本次独审依据；本报告列出的符号恒等式与固定五有限环比较由审查者重新执行。

## Open Risks

- 总剩余 $\overline{h^{-p}pC_D}$ 仍未判定。只有有限参照 ghost 这一来源的净贡献被排除。
- 传播子非恒定二次移位、低带变化以及其余新 $H^p$ 响应不在本次独审范围，
  不因本报告通过而得到接受。
- 当前污染在最小参数时恰从 $h^{p+1}$ 进入；若提高到模 $h^{p+2}$，须重新计算这些实际项。
- 到 $u^{2p}$ 时参照 Frobenius 的 $r=2$ 项和高带乘积可能出现，
  当前有限身份不适用于该次数及更高次数。
- 未推断其他商系数、完整负 Newton 图、准确根赋值、不可约性或分裂域；
  未进行 Route 评价、论文验收、构建或任何外部操作。
