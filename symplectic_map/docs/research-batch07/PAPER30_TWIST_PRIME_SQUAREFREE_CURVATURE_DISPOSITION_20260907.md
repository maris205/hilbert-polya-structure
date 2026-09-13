# Paper30：奇素数平方自由性与次项第一曲率的本轮处置

日期：2026-09-07。
状态：TWIST_PRIME_SQUAREFREE_AND_PARTIAL_NONVANISHING_ACCEPTED_EXCEPTION_BRANCH_OPEN。

接续用户“继续”，本轮在同一双谐波模型内完成奇素数首项平方自由证明，
并证明次项第一曲率及统一的部分非消失结论。首项、次项和辅助机制的
三份独立核查均通过，主控已经全文读取。全分母全部根实、全部简单以及
所有固定消失点处次项非零，仍未作为完整合取命题关闭。
Paper30 未立项，Paper31 未开展，Batch07 保持3/5；不是权限阻塞。

## 1. 对象与规范

保持实际映射

$$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p',$$

以及不除以分母的 SUM action。固定奇素数 $p$、$1\le r<p$，
$\zeta=e^{2\pi ir/p}$、$D_n=2-\zeta^n-\zeta^{-n}$。
这里的 $p$ 作为分母时与上式动量符号按语境区分。
$C_{r,p}(\lambda)$ 是首个共振项，$Q_{r,p}(\lambda)$ 是此前已经严格定义的
首项消去后的下一阶同谐波系数。所有动力学结论仍固定 $\lambda$；
下面的变量缩放只用于同一个多项式的算术分析，不是随 $\epsilon$ 调参。

物理正频支满足

$$v_n=-\frac{[t^{n-1}]e^v/2+\lambda[t^{n-2}]e^{2v}}{D_n}
\quad(p\nmid n),\qquad v_p=0,$$

并使用已接受的 $Q=-p[t^{p+1}]e^{-v}$。共振规范不删除指数系数。
正树规范另用 $a=-4\lambda$，其终端多项式记为 $R_p(D;a)$，
$C_{r,p}=2(-1/2)^pR_p(D;-4\lambda)$，不混合两套参数。

## 2. 已接受：全部奇素数分母的首项无重根

对每个奇素数 $p$ 和全部 $1\le r<p$，

$$\boxed{\deg C_{r,p}=\frac{p-1}{2},\qquad
C_{r,p}\text{ 在特征零中平方自由。}}$$

即全部复根互异；不意味着这些根全部为实数。
这是一个真正无限分母族的重根排除定理，不是有限素数试算。

令 $\pi=\zeta-1$、$m=(p-1)/2$。关键的局部 primitive 身份是

$$\mathcal S_p(A)=
\frac{\pi^{2(p-1)}}pR_p(D;A/\pi^2)
\in\mathbb Z[\zeta]_{(\pi)}[A],
\qquad
\boxed{\overline{\mathcal S_p}(A)=(-A)^m-1.}$$

先在特征零有限系数泛函中证明 $R_p=-pG_p$ 及 $G_p$ 的局部整性，
才合法除去整体 $p$。随后使用 $D_n/\pi^2\equiv-n^2$，
只在低于 $p$ 阶的有限指数／对数中计算。约化保持次数且无重根，
因此 resultant 为局部单位，结论返回实际多项式。
未经 primitive 归一的第一层多项式整体约化为零，不能直接用于重根判断。

见[首项作者证明](PAPER30_TWIST_PRIME_SQUAREFREE_PROBE_V1_20260907.md)
与[12项独立核查](PAPER30_TWIST_PRIME_SQUAREFREE_INDEPENDENT_CHECK_20260907.md)。
独立核查另给有限二项式证明，逐项确认常数项及
$\overline{\operatorname{Res}}=-m^m\ne0$，包括 $p=3$ 和全部 $r$。
主控已全文读取，两份输入无需作者修订。

## 3. 已接受：次项第一曲率与至多一个例外分支

本节证明及14项非作者核查均已完成，按下面的限定范围接受。
定义

$$h=D_1=-\pi^2/\zeta,\quad \rho=-h,\quad d_n=D_n/\rho,\quad L=\rho\lambda,\quad
V(x;L)=v(\rho x;L/\rho),$$
$$\widetilde C(L)=\rho^{p-1}C(L/\rho),\qquad
J(L)=[x^{p+1}]e^{-V}=-\frac{\rho^{p+1}}pQ(L/\rho).$$

系数在完成实分圆子域 $\mathbb Q_p(h)$ 的整数环 $\mathcal O^+$ 中研究。
$h$ 是其均匀化元，$\mathcal O^+/(h)=\mathbb F_p$；
完整分圆环的 $\pi$ 赋值满足 $v_\pi(h)=2$。
不能把完整分圆环按 $h$ 的商环误写成 $\mathbb F_p$。

对全部 $p\ge5$、全部 $1\le r<p$，有

$$\boxed{\overline{\widetilde C/p}=1-L^m,\qquad
J/h\in\mathcal O^+[L],\qquad
\overline{J/h}=\frac{(1-4L)L^m}{32}.}$$

其逻辑顺序为：

1. 先在特征零中精确取消跨越 $p!$ 的两项非整贡献，
   将 $J$ 改写为仅用 $V_1,\ldots,V_{p-1}$ 的局部整表达式。
2. 平方传播子的未投影正支 $W$ 给出常数项 $J_0=-p(p+2)W_{p+1}$，所以所有奇素数的
   $J\bmod h$ 恒为零；这层失败记录保留。
3. 真实传播子的一阶曲率为
   $d_n=-n^2+h\,n^2(n^2-1)/12+O(h^2)$。
   一阶响应 $U=\partial_hW|_{h=0}$ 的 $U_{p+1}$ 含一个 $1/p$ 极点，带 $p$ 的项不能删除；
   完整计算给出上式的 $(1-4L)L^m/32$。
4. 正则化表达式属于 $\mathbb Z_{(p)}[L][[h]]$，
   因而余项确实是整的 $h^2$ 倍数，不存在隐藏的 $h^2/p$ 降阶。
   对 $p\ge5$，$p$ 的 $h$ 赋值 $m\ge2$，常数项除 $h$ 后也不污染该约化。

首项的 $m$ 个剩余根均简单，Hensel 唯一提升把它们与特征零局部根一一对应。
在首项根上，次项约化只可能在 $L\equiv1/4\pmod h$ 为零。因此得到

$$\boxed{\deg\gcd(C_{r,p},Q_{r,p})\le1\qquad(p\ge5).}$$

除唯一例外剩余类对应的根外，其余 $m-1=(p-3)/2$ 个首项根处均有
$Q\ne0$，并有 $v_\pi(J)=2$、$v_\pi(Q)=-p-1$。
$L=1/4$ 只是剩余类，不是声称实际根等于这个数；
$1/4$ 对所有奇素数都是平方，不能按 $p\bmod4$ 排除该分支。
唯一例外根是否真的使 $Q=0$ 仍 OPEN。
$p=3$ 不使用上述曲率式，其旧固定消失点恢复证明不重开。

见[次项作者证明V2](PAPER30_TWIST_PRIME_POST_CANCELLATION_PROBE_V2_20260907.md)
及[14项独立核查](PAPER30_TWIST_PRIME_POST_CANCELLATION_INDEPENDENT_CHECK_20260907.md)。
[V1第一层失败及五分母检验](PAPER30_TWIST_PRIME_POST_CANCELLATION_PROBE_V1_20260907.md)
保留；唯一实际素数算例是 $p=5$ 的精确估值诊断，不从它外推一般公式。
主控与次项作者各自求得同一响应闭式，这属于协作交叉计算，不作为主控的
自我独立认证。非作者另行逐式核验一般响应残差、局部整性和根提升，
只精确复核作者已有的五分母式，没有增加素数或根扫描。
主控已全文读取作者定稿与独立报告，未发现待修复缺口。

## 4. 已接受的辅助身份与明确的方法边界

[平方传播子引理](PAPER30_TWIST_SQUARE_PROPAGATOR_LEMMA_V1_20260907.md)
给出 $d\ne0$ 时 $dn^2$ 辅助递推的二次分母解及终端系数，
并在实 $d>0$ 时给出辅助负实单根公式。
它解释实际圆分约化所需的有限系数身份；
特征零辅助传播子不等于实际正弦传播子，其根公式不能直接移植。

[实循环芽探针](PAPER30_TWIST_REAL_CYCLIC_GERM_PROBE_V1_20260907.md)
证明实型、两反射曲线及未扣低阶项的局部模长单调性对每个实参数自动成立，
不依赖 $R_p=0$。因此它们不筛选共振根，也不给 $R_p'$ 非零性。
对复参数预先强加该实型，二阶系数已经迫使参数实，不能把它当作排除非实根的证明。

两件通过[9项合并独立核查](PAPER30_TWIST_AUXILIARY_REAL_GERM_INDEPENDENT_CHECK_20260907.md)，
主控已全文读取。核查者不是两件的作者，也未复查其自己撰写的素数证明。
这些辅助身份及共享响应不另计为重复主贡献，不拼接成另一系统族的根定理。

## 5. 仍开放的义务与接续

下一项优先目标是 $p\ge5$ 的唯一剩余类 $L\equiv1/4$：
需要在满足首项方程的实际 Hensel 根上取得更高阶信息，而不是冻结为数值 $1/4$，
也不能由该剩余值为零反推特征零共同根存在。
本轮没有执行这一更高阶证明，未将它计为已完成。

此外仍分别需要解决：

- 奇素数分母及一般分母的全部根实性。
- 合数分母的重根排除或准确例外；奇素数简单性不再 OPEN。
- 一般分母固定首项零点处的次项非零性或准确共同因子。

此前[单插入、变分与循环芽规约](PAPER30_TWIST_SINGLE_INSERTION_VARIATIONAL_GERM_DISPOSITION_20260907.md)、
[低分母恢复及真实Jacobi桥接](PAPER30_TWIST_POST_CANCELLATION_AND_BRIDGE_DISPOSITION_20260907.md)
和[首项部分根结构](PAPER30_TWIST_ROOT_STRUCTURE_DISPOSITION_20260907.md)
按原范围保留，不重新打开未变证明、旧63例或旧六例高精度诊断。
本轮的有限符号检查只针对新增身份，没有扩大根扫描。

标准分圆局部输入和简单根提升已在
[Milne作者讲义的命题6.2](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=98)
与[命题7.31](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=122)核对。
它们是标准工具，不作为新贡献；本轮没有完成全局新意排除。
通用Lindstedt、Hill及Suris背景仍按
[既有定点查新](PAPER30_TWIST_ROOT_STRUCTURE_PRIOR_20260907.md)扣除。

没有正文估页、正式候选票、试写测页、论文立项、PDF、Route评价或对外操作。
正文22–30页、完整证明、独立验收与本地效力边界保持不变；
其他已闭合支线不重开、不补模块或拼篇，五篇目标未标为完成。

## 6. 本轮输入身份

| 文件 | SHA256 |
| --- | --- |
| 奇素数首项作者证明 | 37dac7ae617e0d834f974a4ee17bbca9c2e45e1cef442bb027ba59ffd459297b |
| 奇素数首项独立核查 | 26f49b085039a55ede99be593816c5f6654d9ca509b6fde8d947a63619d5ba60 |
| 次项作者V1，保留第一层失败 | 76818374efdace1df40433f55f4c1afac7687db0dc90bb8ba707ae7bb097df8b |
| 次项作者V2 | 6a4a3fa115f277658caed29de4a6f5d35f88d533b3901dd0831e720547c559a1 |
| 次项14项独立核查 | bc4b79b7f6f5298f52c9ff454b091df7532e0434ddca36c51c98d81450c60408 |
| 平方传播子引理 | 9222ff350766960b1d6a606a2cf156409893b693fa1e698b9a3c438bb23fb478 |
| 实循环芽探针 | 9599318f931c43379cd6726297302cbebf2b6bd00b3349e4d23456bdf91d9c6c |
| 两件辅助机制独立核查 | f5cfcffd18b51e2ddf27457b190c6302bc53395bfe91a418f7e0450145643b43 |
