# Paper30：奇素数幂第二阶乘带与第三 forcing 的普通首层取消

日期：2026-09-07。
状态：TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_ACCEPTED_THIRD_FORCING_OPEN。

本轮从此前指定的 $n=2p+1$ 接续，完成同一实际分支的整个
$2p+1\le n\le3p-1$ 非内部模态块。
此前的 $p^2$ 尺度候选现有完整证明及非作者核查；
没有把该尺度直接延伸到端点 $3p$。

## 1. 固定规范及输入

固定任意奇素数 $p$、$a\ge2$ 及任意本原 $p^a$ 次根 $\zeta$。
仍使用原双谐波模型、固定物理参数及 SUM action，令

$$h=D_1=2-\zeta-\zeta^{-1},\quad
\rho=-h,\quad L=\rho\lambda,\quad
m=(p-1)/2,\quad M=p^{a-1}m.$$

在完成实分圆局部域的整数环 $\mathcal O^+$ 中，
$v_h(h)=1$、$v_h(p)=M$，剩余域为 $\mathbb F_p$。
使用同一实际缩放分支

$$V_n(L)=\rho^n v_n(L/\rho),\qquad
d_n=-D_n/h=D_n/\rho,$$
$$d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.$$

特别地，$V_1=1/2$ 精确成立；不要把 $d_n$ 改成正的 $D_n/h$，
也不要混用此前分母 $2p$ 结果的 $h=D_2$。

[此前第二内部层处置](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_DISPOSITION_20260907.md)
及其冻结证明保持接受。本轮只调用所需输入：

$$V_i\in\mathcal O^+[L]\ (i<p),\qquad
pV_p\in h^{M-m}\mathcal O^+[L],$$
$$pV_{p+j}\in\mathcal O^+[L]\ (1\le j<p),\qquad
pV_{2p}\in\mathcal O^+[L],\quad\overline{pV_{2p}}=-1/4.$$

其中端点的准确剩余值作为旧结论保留；新块证明本身只需要 $pV_{2p}$ 的整性。

令 $q=(1-4L)/16$、$A=1-x/2+qx^2$，
旧非内部块的剩余生成函数为
$Y=xA'/(2A)=-\mathcal NW/2$，其中 $\mathcal N=x\partial_x$。
$W=-\log A$ 的系数仅在次数小于 $p$ 时约化；
其 $\mathcal N$ 导数则使用分母为 $A$ 的整有理表达式。

## 2. 新块：准确尺度为 $p^2$

[第二阶乘块作者证明](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md)
对全部 $1\le j<p$ 给出

$$\boxed{p^2V_{2p+j}\in\mathcal O^+[L].}$$

其完整剩余生成函数为

$$\boxed{\sum_{j=1}^{p-1}\overline{p^2V_{2p+j}}x^j
=\frac18\mathcal N^2W
=\frac{x(1-8qx+qx^2)}{16A(x)^2}\pmod{x^p}.}$$

用已接受的幂和多项式
$T_0=2,T_1=1/2,T_j=T_{j-1}/2-qT_{j-2}$ 表示，则

$$\overline{p^2V_{2p+j}}=\frac j8T_j
=-\frac j4\,\overline{pV_{p+j}}.$$

每个剩余多项式非零，次数为 $\lfloor j/2\rfloor$，
因此每个新模态的系数最小赋值恰为 $-2M$。
这不是所有参数处每个模态的点值赋值断言；
在 $T_j(\bar L)\ne0$ 时点值才自动达到 $-2M$。
对应两块的剩余零点相同，不意味着实际参数多项式具有相同根。

首入口的剩余是常数：

$$\boxed{\overline{p^2V_{2p+1}}=1/16.}$$

故对任意有限局部扩域中的代数整数参数 $L$，
$v_h(V_{2p+1}(L))=-2M$，包括此前 $\bar L^m=2$ 的根类。

## 3. 为什么不能只沿已有极点传播

严格小于 $3p$ 的低指数使用的阶乘满足 $N<p^2$，
所以其 $p$ 因子数最多为二；这也覆盖 $p=3$ 时 $3p=p^2$ 的边界。
最高阶乘带给出

$$\overline{\frac{p^2}{(2p+r)!}}=\frac1{2r!},
\qquad 0\le r<p.$$

高块必须保留二次项。乘 $p^2$ 后，同阶剩余有四个来源：
低块的 $(2p)!$ 带、旧高模乘低块 $p!$ 带、旧高模平方，以及新高模线性项。
它们合成为

$$\overline{p^2[x^{2p+j}]e^{\alpha V}}
=[x^j]A^{-\alpha}
\left(\alpha Z+\frac{\alpha^2}{2}(Y-1/2)^2\right),
\qquad \alpha=1,2,\quad 0\le j<p,$$

其中 $Z=\sum_{j=1}^{p-1}\overline{p^2V_{2p+j}}x^j$。
实际 $V_p$ 和 $V_{2p}$ 都完整保留；
$\overline{pV_p}=0$、$\overline{p^2V_{2p}}=0$ 来自已知正赋值，
不是将内部模式设为零。

逐阶整性先由每个 $d_{2p+j}\equiv-j^2$ 的单位除法证明，
然后才取剩余并解二阶变分方程。
上述合式给出 $Z=\mathcal N^2W/8$；
仅写出这个有理式或核对入口系数，不能替代实际递推的整性证明。

## 4. 第三 forcing：只接受普通首层取消

由已知的全部 $n<3p$ 实际模态定义

$$\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}.$$

它不需要定义或除出 $V_{3p}$。
同一有限指数身份直接给出

$$\boxed{p^2\mathcal B_3\in h\mathcal O^+[L].}$$

证明将有理二阶变分身份取 $x^p$ 系数：
驱动只依赖 $Z$ 的低于 $p$ 次系数，
而 $[x^p]\mathcal N^2 Z_{\rm rat}=p^2[x^p]Z_{\rm rat}$ 的约化为零。
这里 $Z_{\rm rat}$ 的全部系数在奇特征处整，
没有对含 $1/p$ 的对数系数直接取模。

这项结论只消去普通常数层。
$\mathcal B_3$ 的准确首个非零层、非消失、其根及 $V_{3p}$ 的尺度均未据此解决；
也没有把它与之前 $\mathcal B_2$ 的常数单位结论混为一谈。

## 5. 独立核查与交付

[新非作者核查](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_INDEPENDENT_CHECK_20260907.md)
给出 **PROVABLE AS STATED：14 项限定核查全部 PASS**，
没有阻断性缺口或作者修改要求。
主控已全文读取475行冻结作者稿与334行独审报告；
两份新输入的交付哈希与绑定记录一致。

核查者未参与本轮作者推导，独立检查了实际入口和初值、两条阶乘带、
四项三角整性、有限剩余桥、二阶变分身份、系数与点值边界，
以及仅限普通首层的第三 forcing 推论。
其独立自由符号运算残差为零，入口系数为 $1/16$；
这些运算不代替一般整性、实际赋值和量词范围的论证。

本轮按 proof-writer 先证明实际整性，再取得剩余方程与准确赋值，
将普通首层取消和高精度端点问题分开。
主控与作者共推的身份不算独立审查或多个独立贡献。
只运行新自由符号身份核对，没有新增素数、分子、分母或根扫描；
未重跑旧诊断，也未重开输入未变的已接受证明。
旧稿、失败记录及已接受产物保持原样。

## 6. 下一准确缺口与批次状态

下一有界对象是 $\mathcal B_3$ 的首个非零层，而不是继续假定 $p^2V_{3p}$ 整。
必须先补第二阶乘带的形式 $H$／实际 $h$ 精细误差桥，
并保留低模乘第二块、第一块乘第一块的耦合响应及传播子配对缺陷。
不能由普通剩余为零便猜测下一层是 $m$ 或 $2m$。

端点必须分开处理：$p\ge5$；$p=3,a\ge3$；
以及 $p=3,a=2$ 时 $3p=p^a=9$ 的真正共振。
三的幂情况下，$3p$ 本身已有两个素因子 $3$，不能沿用前两个内部传播子的尺度。
真共振处更不能把 $d_{3p}=0$ 当作可除的内部传播子。

完整 $C_{r,p^a}$ 的结构、简单性与 $C,Q$ 互素，
其他合数分母及实际参数根的全实性仍未完成。
此前[全部奇素数](PAPER30_TWIST_PRIME_COMPLETE_NONVANISHING_DISPOSITION_20260907.md)
和[全部两倍奇素数](PAPER30_TWIST_TWO_PRIME_COMPLETE_DISPOSITION_20260907.md)
的完整结论保持接受；前两个内部 forcing 的已证明范围亦不重开。

整体新意和自然正文容量尚未最终认证。
不估页、不投正式候选票、不试写测页；没有 Paper30 项目、PDF、Route 评价或对外操作。
Batch07 仍为 **3/5**，Paper30 未立项，Paper31 未开展；
22–30页实质正文、完整证明及独立验收要求不变。

## 7. 新输入身份

| 新输入 | SHA256 |
| --- | --- |
| SECOND_FACTORIAL_BLOCK V1 | `3ff45f425669adbd012245f5cf605083a72e3cccb131cc6469f787cc58920e04` |
| SECOND_FACTORIAL_BLOCK INDEPENDENT_CHECK | `76a436c38f75f2fc23ce128cdf57897a2162587d0d6f8013443510909319edc6` |

本处置只同步当前范围与下一缺口，不修改上述冻结稿及旧接受记录。
