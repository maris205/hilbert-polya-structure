# Paper30：奇素数幂首个极点后的模态块与第二内部 forcing

日期：2026-09-07。
状态：TWIST_PRIME_POWER_SECOND_INTERNAL_LAYER_ACCEPTED_FULL_RESONANCE_OPEN。

本轮接续用户“继续”，完成此前指定的实际模态范围 $p+1\le n\le2p$。
非内部模态块和第二内部 forcing 使用同一物理递推、固定参数与 SUM action。
它们是完整参数多项式的结论，不是有限素数算例或一般位置参数的猜测。
完整 $C_{r,p^a}$、其与 $Q$ 的关系及全部实根问题仍未由本轮解决。

## 1. 规范与已接受输入

固定任意奇素数 $p$、$a\ge2$，$\zeta$ 为任意本原 $p^a$ 次单位根。
本节不同于此前两倍素数的 $h=D_2$ 规范，改用

$$h=D_1=2-\zeta-\zeta^{-1},\qquad
\rho=-h,\qquad L=\rho\lambda,\qquad
m=(p-1)/2,\qquad M=p^{a-1}m.$$

在完成实分圆局部域的整数环 $\mathcal O^+$ 中，
$v_h(h)=1$、$v_h(p)=M>2m$，剩余域为 $\mathbb F_p$。
令 $D_n=2-\zeta^n-\zeta^{-n}$，实际缩放分支为

$$V_n(L)=\rho^n v_n(L/\rho),\qquad
d_n=D_n/\rho=-D_n/h,$$
$$d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.$$

特别是 $d_1=-1$、$V_1=1/2$ 精确成立。
$2p<p^a$，所以本轮没有全系统共振，也没有把 $V_p$ 或 $V_{2p}$ 置零。

此前[素数幂首个内部层](PAPER30_TWIST_COMPOSITE_FIRST_LAYER_AND_PROPAGATOR_DISPOSITION_20260907.md)
的结论保持接受，不重审。记同一缩放参数中的内部 forcing

$$\mathcal B_k(L)=-[x^{kp-1}]e^V-2L[x^{kp-2}]e^{2V},\qquad k=1,2.$$

只需要对应次数以下的实际分支；$\mathcal B_1$ 正是此前的 $\mathcal B(h,L)$。
已有
$$\overline{h^{-m}\mathcal B_1}=(-1)^{m+1}(2-L^m),\qquad
\overline{h^mV_p}=\frac{(-1)^m}{2}(2-L^m).$$
这些首层身份和其根、局部因子型不再作为未完成义务。

## 2. 非内部模态块：正确尺度从 $h^m$ 变为 $p$

[新模态块证明](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md)
对所有 $1\le j<p$ 给出

$$\boxed{pV_{p+j}\in\mathcal O^+[L].}$$

令 $q=(1-4L)/16$、$A(x)=1-x/2+qx^2$，完整首层为

$$\boxed{\sum_{j=1}^{p-1}\overline{pV_{p+j}}x^j
=\frac{xA'(x)}{2A(x)}
=\frac{-x/4+qx^2}{1-x/2+qx^2}\pmod{x^p}.}$$

定义幂和多项式 $T_0=2,T_1=1/2,T_j=T_{j-1}/2-qT_{j-2}$，
则每个剩余系数为 $-T_j/2$。
它的 $L$ 次数为 $\lfloor j/2\rfloor$，最高系数不消失，
故每个实际 $V_{p+j}$ 的系数最小赋值恰为 $-M$。
这是逐系数的准确性，不能写成“任意参数处每个模态都有同一极点”；
只有剩余值不为零的参数才自动达到该极点阶。
特别地，$pV_{p+1}$ 的剩余为常数 $-1/4$，对所有局部代数整数参数均为单位。

证明保留实际 $pV_p\in h^{M-m}\mathcal O^+[L]$。
高模式在次数严格小于 $2p$ 的指数中只线性出现，
但低块指数必须保留第 $p$ 至第 $2p-1$ 项的阶乘带。
在独立形式变量 $H$ 中，作者证明了准确的有限系数桥

$$p[x^{p+j}]e^{\alpha P(H,x)}
=-\frac{\alpha}{2}[x^j]e^{\alpha P(H,x)}+pR_{\alpha,j}(H,L),
\quad \alpha=1,2,\quad 0\le j<p,$$

其中 $P$ 是原低块，$R_{\alpha,j}\in\mathbb Z_{(p)}[L][[H]]$。
误差是 $p$ 倍整数级数，不是未经控制的 $H$ 误差；
这一步才使后续更精细的实际赋值计算有合法输入。

## 3. 第二内部 forcing：两次取消后的常数单位层

[第二内部 forcing 证明](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md)
确定其首个非零层恰为 $2m$：

$$\boxed{h^{-2m}p\mathcal B_2\in\mathcal O^+[L],
\qquad \overline{h^{-2m}p\mathcal B_2}=2.}$$

不是常数层，也不是最初反射缺陷所在的 $h^m$ 层；两层都发生实际取消。
由于 $d_{2p}/h^{2m}\equiv-4$，原递推还给出

$$\boxed{pV_{2p}\in\mathcal O^+[L],
\qquad \overline{pV_{2p}}=-\frac14.}$$

因此对每个有限局部扩域中的代数整数参数 $L$，都有

$$v_h(\mathcal B_2(L))=2m-M,\qquad v_h(V_{2p}(L))=-M.$$

这包含第一内部层的代数剩余根类 $L^m=2$，
不需要删除这些参数或除以第一 forcing。
已接受的 $h^{-m}\mathcal B_1$ 为整多项式且最高系数为单位，
故 $\mathcal B_1$ 的全部根在 $L$ 坐标中局部整，
所以常数单位还直接给出

$$\boxed{\gcd(\mathcal B_1,\mathcal B_2)=1.}$$

这是两个实际内部 forcing 的互素性，不是完整首项 $C_{r,p^a}$ 与某个多项式的互素性。

证明使用实际 $2p$ 阶有限 action 的反射缺陷。
单个缺陷有 $h^m$ 首层，但配对后的缺陷和从 $h^{2m}$ 才开始；
同时必须保留非内部模态对该缺陷的一阶响应。
两部分在第 $2m$ 层分别贡献 $2-L^m$ 和 $L^m$，最终合为常数 $2$。
不能只保留配对传播子而忽略模态响应。

所有误差均在实际赋值下控制。
尤其 $p=3,a=2$ 时 $M-m=2m$，不能直接把 $pV_p$ 初值当成更高阶丢掉；
它进入最终配对式后还乘一个至少 $h^m$ 的缺陷，贡献因而至少为 $h^M$，
严格高于 $h^{2m}$。该最小边界也完整覆盖，不另添排除条件。

## 4. 独立核查与交付范围

[联合非作者核查](PAPER30_TWIST_PRIME_POWER_POST_POLE_AND_SECOND_INTERNAL_INDEPENDENT_CHECK_20260907.md)
给出 **PROVABLE AS STATED：25 项限定核查全部 PASS**，没有阻断缺口或作者修改要求。
主控已全文读取两份作者稿（391／640行）及联合核查（549行）；
三份新文件的交付哈希均与所绑定输入一致。
核查者没有参与本轮两份新证明的推导；其旧首层作者身份明确披露，
旧输入只按既有接受结论调用，没有被重新授予非作者独审。
核查覆盖完整阶乘桥、三角整性、真实／形式误差、非驻值 Euler 身份、
配对缺陷与 Jacobi 修正、最小边界、全部局部代数整数参数及互素推论。
独审还实际完成了两组新的自由符号身份核对，所列残差均为零；
这些运算不代替一般整性和误差高度的证明。

本轮按 proof-writer 区分候选尺度、逐系数整性、实际误差桥和最后的单位推论。
主控与两位作者协作得到的同一公式不重复计为贡献，也不作为独立审查。
新增验证只针对自由符号身份；没有新增素数、分子、分母或参数根扫描，
没有重跑旧诊断或未变的接受证明。
旧作者稿、失败路径与已接受产物均保留。

此前[全部奇素数](PAPER30_TWIST_PRIME_COMPLETE_NONVANISHING_DISPOSITION_20260907.md)
及[全部两倍奇素数](PAPER30_TWIST_TWO_PRIME_COMPLETE_DISPOSITION_20260907.md)
的完整简单性、$C,Q$ 互素结论保持接受，不因本轮改用素数幂规范而重开。
真实传播子的有限保根分类按原范围保留，也未被当成参数根的全实性证明。

## 5. 下一项准确缺口

下一有界入口是 $n=2p+1$。
低指数首次达到 $(2p)!$，高块展开还必须保留 $V_p^2/2$：
之前“严格低于 $2p$ 时高模只线性出现”的身份不能直接使用。
先证明合适的新正规化及全部同阶项的界，再向后续模态延伸。

只读接续计算提示 $p^2$ 可能是该模态的准确尺度；
这一点没有作为本轮定理接受，后续必须绑定本轮端点输入完成正式证明及独审。
若再扩展到 $3p$，应单列 $p=3,a=2$ 时 $3p=p^a$ 已是真正共振的边界，
不能将其当作第三个非共振内部模态。

更高内部模态、完整 $C_{r,p^a}$ 的首层结构、简单性和 $C,Q$ 互素仍需证明；
其他合数分母及实际参数根的全实性也仍未完成。
本轮的 $\mathcal B_2$ 常数单位不能自动推广到所有内部 forcing，
也不能把已知非内部模态的 $p$ 尺度沿用到新增阶乘带之后。

整体新意与自然正文容量尚未最终认证。
不估页、不投正式候选票、不试写测页，没有 Paper30 项目、PDF、Route 评价或对外操作。
Batch07 仍为 **3/5**，Paper30 未立项，Paper31 未开展；
22–30页实质正文、完整证明与独立验收要求不变。

## 6. 新输入身份

| 新输入 | SHA256 |
| --- | --- |
| POST_POLE_BLOCK V1 | `0a70394315cfe78b860c6ac46eec53bb58ccb8b3e432c1108438f7e721ee4c34` |
| SECOND_INTERNAL_FORCING V1 | `278ce73d9844c8a30b93b8952b8a3a178aa577f1c808fce48c333be721c97f15` |
| POST_POLE_AND_SECOND_INTERNAL INDEPENDENT_CHECK | `74fe04bd24b46012672bc3d964e0d16d334352be22f7d345decc0daecf358ea8` |

本处置只同步当前范围与下一缺口，不改动上述冻结证明及旧接受文件。
