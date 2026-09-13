# Paper30：负端最高系数预临界与临界消失的接受处置

日期：2026-09-08。状态：`NEGATIVE_TOP_VANISHING_ACCEPTED; NEGATIVE_FACTOR_OPEN`。
主控已全文读取下列新作者稿与独立报告；科学接受仅限本件明确列出的结论。

## 1. 当前接受的最高系数结论

同一实际双谐波分支、固定参数及规范保持。对全部素数 $p\ge5$、$a\ge2$，令
$$
m=(p-1)/2,\quad M=p^{a-1}m,\quad D=3m+1=p+m,\quad e_*=M-D.
$$
在 $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$ 中，$P_{\rm cl}$ 首一次数 $m$，
$U_{\rm cl}$ 次数 $p$。本轮证明并经独审接受
$$
\boxed{p[L^D]\mathcal B_3\in h^{m+1}\mathcal O^+,\qquad
v_h([L^p]U_{\rm cl})\ge e_*+m+1=M-2m.}
$$
因此最高商系数从原候选高度 $e_*$ 到 $e_*+m$ 的各层全部为零。
原先待算的 $h^{-e_*}[L^p]U_{\rm cl}\bmod h$ 已经确定为零，不再 OPEN。
高度 $M-2m$ 是下一可能层，不是已证明的准确赋值或非零系数。

预临界证明在 $\mathcal O^+/h^m$ 中利用准确倍角变换、正阶有理核的有限整性，
得到两个正规化高带 $\tau=-2\Theta w$、$\sigma=-(1+2\Theta)a$；
端点提取的乘子均为 $2m+1=p$。
临界证明在 $\mathcal O^+/h^{m+1}$ 中保留真实传播子移位，求得
$$
t=-\frac{4\chi u}{1-u},\qquad s=-\frac{2\chi}{(1-u)^2},\qquad
\chi=(-1)^{m+1}.
$$
完整端点修正为 $4\chi m(2m+1)^2$，其剩余仍为零。
这个形式 $p^2$ 因子不提供超过当前 $h^{m+1}$ 误差控制的实际赋值。

## 2. 负根界与原负端点

令
$$
\delta_+=\min\left\{\frac{e_*}{p-1},\frac{M-2m}{p}\right\}
>\frac{e_*}{p}.
$$
已接受的其余系数下界 $v_h(u_j)\ge e_*$（$1\le j<p$）与新最高项下界给出
$$
\boxed{v_h(\beta)\le-\delta_+\quad(U_{\rm cl}(\beta)=0).}
$$
在任意有限扩域中，非零参数 $\ell$ 若 $-\delta_+<t=v_h(\ell)\le0$，则
$$
v_h(U_{\rm cl}(\ell))=0,\qquad v_h(S(\ell))=mt.
$$
合并既有正簇距离式后，其原来的完整点值公式适用范围可由 $t>-e_*/p$
延伸到 $t>-\delta_+$；没有改动正簇根或其临界抵消。
最初排除的端点 $t=-e_*/p$ 现在严格位于已证范围内；新端点 $-\delta_+$ 仍不包含。

相对于最初的弱界这是严格改进；相对于本轮预临界界不保证每个 $a$ 都再次严格改进。
特别是 $a=2$ 时，两次的最小值均由 $e_*/(p-1)$ 控制。
本件不从根界推出等号、唯一负 Newton 边、不可约性或简单性。

## 3. 新证据、独立性与原稿问题

| 证据 | 本轮处置 |
| --- | --- |
| [原模 h 作者稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_COEFFICIENT_PROBE_V1_20260907.md)及[独立核查](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_INDEPENDENT_CHECK_V1_20260908.md) | 数学目标有独立证明；原 V1 字面逐行无修正审查为 FAIL，原文件不改写 |
| [初层替代推导](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_ALTERNATIVE_V1_20260908.md) | 完整处理实际奇共振支撑；独立推导作者稿，不冒充非作者终审 |
| [预临界证明 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md)及[预临界独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_INDEPENDENT_CHECK_V1_20260908.md) | 306 行新作者稿，23 项独立核查全部 PASS，无需修订；接受 |
| [临界证明 V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_CRITICAL_PROBE_V1_20260908.md)及[临界独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_CRITICAL_INDEPENDENT_CHECK_V1_20260908.md) | 539 行新作者稿，22 项独立核查全部 PASS，含上述根界应用；接受 |

原 V1 的实质问题是将奇响应 $A$ 的普通约化写到共振后；实际 $A_m,A_{m+1}$
赋值为 $-m$，不能如此约化。新证明只约化 $A_{<m}$，对中间层证明
$v_h(A_r)\ge-2m$，并利用目标乘积次数至多 $p+m-1$，使其配对的偶指数系数
仍在整低带；先乘 $p$ 后误差至少为 $M-2m$。
若乘积次数达到 $p+m$，该支撑排除不再有效。原稿错误及失败意见完整保留，
不把后继证明的 PASS 追溯为原稿全文 PASS。

输入身份（只绑定本次直接新证据）：

- 预临界作者稿：`033a05a8bc6f9d34125696366bf0ee23f84682049df1d7edd8dd80c702929502`。
- 预临界独审：`0793aa675cd71c7123c7efe7f782bc219de4cdd671d63f0781d46a901439653f`。
- 临界作者稿：`b621699d75512e0d762e7e7ac84218f43d80305a0ea6fdac61d236e72e8ebb0a`。
- 临界独审：`62d0e86f4c22198b19219a18811786fb6a98338fac97c555e2b206e6a09ac799`。

主控的自由符号核对是作者核算，不计独审票。所有一般量词、整性和误差由证明承担；
有限符号残差仅用于防止代数笔误。没有逐素数扫描、根拟合、旧 39 项重跑或旧构建检查。

## 4. 下一项与仍开放的义务

下一对象仍是同一负赋值 $p$ 次因子的完整下凸包。需要计算相关中间高系数的首层，
并判定最高项 $h^{M-2m}$ 层是否非零；不能只用这一项的下界替代整幅 Newton 图。
原 $e_*$ 最高层和本次已消失的预临界／临界层不再作为待算问题反复启动。

若继续提高最高项精度，旧有理核整性只覆盖 $k+j\le m$，不覆盖 $R_{m+1,0}$；
新的核整性、下一移位项及实际误差必须各自有证据，不从当前公式直接外推。
负因子的准确斜率、因子型、简单性、根间距和野分裂域均仍 OPEN。
旧 [负因子边界处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_FACTOR_DISPOSITION_20260907.md)
中的 DVR 逻辑反例及原输入不足结论保留；本件只以实际新系数证据加强结论。

一般第二／第三 forcing 互素、完整素数幂 $C,Q$、其他合数及全实根问题未因此闭合。
正簇已接受结论、旧特殊素数分支、冻结原稿和 Papers27–29 产物不改。
Batch07 仍为本地接受 **3/5**；Paper30 未正式立项，Paper31 未开展。
正文 22–30 页、新意、研究价值、完整证明与独立产物验收要求均不变。
本件不是候选容量票、论文稿件、PDF 或 Route 评价；没有任何投稿、上传或外部效力。
