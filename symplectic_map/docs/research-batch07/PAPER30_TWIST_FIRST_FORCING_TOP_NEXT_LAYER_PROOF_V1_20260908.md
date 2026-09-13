# Proof Package：第一内部 forcing 最高参数项的下一形式层

日期：2026-09-08。作者：主控。
本件用 `formula-derivation` 固定第三 forcing 的线性端点所需输入，
再用 `proof-writer` 证明该输入；不是将第一 forcing 替换为批次最终目标。

## Claim

固定素数 $p\ge5$、整数 $a\ge2$，令

$$m=(p-1)/2,\quad M=p^{a-1}m,\quad \chi=(-1)^{m+1},\qquad
h=2-\zeta-\zeta^{-1},\quad v_h(p)=M,$$

其中 $\zeta$ 为本原 $p^a$ 次根。$H$ 表示独立形式变量。
在此前已接受的低整块规范中，第一内部 forcing 记作 $\mathcal B_1(H,L)$。
其最高参数系数在 $\mathbb F_p[[H]]$ 中满足

$$\boxed{[L^m]\mathcal B_1(H,L)
=-\chi H^m-\frac\chi{16}H^{m+1}+O(H^{m+2}).}\tag{1}$$

因此在实际圆分整环中同样有

$$[L^m]\mathcal B_1(h,L)
=-\chi h^m-\frac\chi{16}h^{m+1}+O(h^{m+2}).\tag{2}$$

若依最高项 Ward 稿记
$B_{\rm low}=-4^m[L^m]\mathcal B_1(H,L)$，则形式模 $p$ 有

$$\boxed{[H^{m+1}]B_{\rm low}=\chi/16.}\tag{3}$$

对 $\lambda_H=\chi H^m(4-H)^{m+1}$、$\mathcal E=H\partial_H$，
第三 forcing 的已识别线性端点在新层的贡献因而为

$$\boxed{[H^p]\{-\lambda_H(\mathcal E-m)B_{\rm low}\}=-1/4.}\tag{4}$$

这里 $\lambda_H$ 是形式移位因子，不是实际双谐波参数 $\lambda$。
式 (4) 仅是完整第三端点的一部分，不能单独推出其新层非零。

## Status

`PROVABLE AS STATED`；以下给出一般素数的有限证明，待非作者独审。
不新增假设、不扫描素数、不对局部域数值作未定义的形式求导。

## Assumptions and accepted inputs

保持双谐波负传播子规范。取整数 Chebyshev 多项式

$$C_n(H)=z^n+z^{-n},\quad H=2-z-z^{-1},\qquad
d_n(H)=\frac{C_n(H)-2}{H}.$$

低整块由

$$d_n(H)V_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},
\quad1\le n<p,$$
$$\mathcal B_1(H,L)=-[x^{p-1}]e^V-2L[x^{p-2}]e^{2V}$$

定义。$V$ 无常数项，所有指数只取低于 $p$ 的次数。
因 $d_n(0)=-n^2$ 为 $p$ 单位，有限递推与相关 action 均在
$\mathbb Z_{(p)}[L][[H]]$ 中。

本件只用下列已接受结论的所需部分：

1. [第一内部局部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
   式 (9)—(11)：有限整性及精确 Euler 缺陷身份。其式 (15) 的已接受首层结论保持。
2. [最高项后临界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md)
   式 (17)—(19)，及其[非作者独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_INDEPENDENT_CHECK_V1_20260908.md)：
   所需有限低偶、低奇块的 $H$ 一次系数。本件不重开这些已通过的方程与唯一性。
3. [最高项二次边界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md)
   及其[独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_INDEPENDENT_CHECK_V1_20260908.md)：
   仅在式 (3)—(4) 使用 $B_{\rm low}$ 和线性端点的准确权重身份。

## Notation and proof map

引入辅助幅度 $b$，实际仍取 $b=1$，令 $u=Lx^2/4$，并写

$$V(b)=W(H,u)+bxA(H,u)+O(b^2).$$

在最高参数提取中只需要这两个幅度阶。记

$$W=W^{(0)}+HW^{(1)}+O(H^2),\qquad
A=A^{(0)}+HA^{(1)}+O(H^2).$$

证明图：精确反射缺陷的下一项 → Euler 身份中最高参数的偶奇配对
→ 有限低带系数 → 一个可交换的有限双和 → 显式模 $p$ 剩余。
所有推导先在形式整块中进行，再代入实际 $H=h$。

## Proof

### Step 1. 反射缺陷的准确下一项

令 $S_i=(z^i-z^{-i})/(z-z^{-1})$。在特征 $p$ 中，
$C_p=2-H^p$、$z^p-z^{-p}=(z-z^{-1})^p$。
Chebyshev 加法给出准确身份

$$d_i-d_{p-i}=\frac{\lambda_H}{2}S_i
+H^{2m}+\frac{H^p}{2}d_i.\tag{5}$$

这里用 $(z-z^{-1})^2=-H(4-H)$，所以
$(z-z^{-1})^{p+1}/H=\lambda_H$。
低次展开为

$$S_i=i-\frac{i(i^2-1)}6H+O(H^2),$$
$$\lambda_H=4\chi H^m
\left(1-\frac{m+1}{4}H+O(H^2)\right).$$

第二式使用 $4^m=2^{p-1}=1$ 于 $\mathbb F_p$。
又 $m+1=1/2$ 于该域，且 $2m\ge m+2$ 对全部 $m\ge2$ 成立。
因此式 (5) 给

$$\boxed{d_i-d_{p-i}
=2\chi iH^m-\frac{\chi i(4i^2-1)}{12}H^{m+1}
+O(H^{m+2}).}\tag{6}$$

$m=2$ 时式 (5) 的 $H^{2m}$ 恰在被排除阶，不能把本截断自动延长一阶。
本件所有固定分母 $2,6,12$ 均为 $p$ 单位。

### Step 2. Euler 身份与最高参数偶奇配对

已接受的精确有限身份是

$$\mathcal B_1=-2p\Phi+
\sum_{i=1}^{p-1}i(d_i-d_{p-i})V_iV_{p-i},\tag{7}$$

其中 $\Phi\in\mathbb Z_{(p)}[L][[H]]$。
所以形式模 $p$ 后 action 项为零，且不存在先除以 $p$ 的操作。
齐次权重使 $[L^m]V_iV_{p-i}$ 恰有一次 $b$：一个偶下标和一个奇下标。
将偶下标写为 $i=2r$、$1\le r\le m$，另一个下标为 $p-2r$，则

$$[L^m]V_{2r}V_{p-2r}=4^{-m}W_rA_{m-r}.\tag{8}$$

在模 $p$ 中，两个配对指标互为负数；式 (6) 在式 (7) 中分别含
$i^2$ 与 $i^2(4i^2-1)$，都是偶函数。
故每对恰贡献两次，而没有省略奇端的权重。于是

$$[L^m]\mathcal B_1
=\chi4^{-m}H^m
\left\{16\sum_{r=1}^m r^2W_rA_{m-r}
-\frac{2H}{3}\sum_{r=1}^m r^2(16r^2-1)W_rA_{m-r}\right\}
+O(H^{m+2}).\tag{9}$$

第二和只需其 $H$ 零阶，第一和需要一次低响应。

### Step 3. 所需低块的有限系数

已接受低响应给出，在各自所需的 $u$ 次数内

$$W^{(0)}=-\log(1-u),\quad A^{(0)}=\frac1{2(1-u)},$$
$$W^{(1)}=\frac{u(1+u)}{4(1-u)^2},$$
$$A^{(1)}=\frac{1+16u+7u^2}{48(1-u)^3}
-\frac{1+u}{48(1-u)}\sum_{q\ge0}\frac{u^q}{2q+1}.\tag{10}$$

因此对于 $1\le r\le m$、$0\le s<m$，

$$W_r^{(0)}=1/r,\quad A_s^{(0)}=1/2,\quad
W_r^{(1)}=(2r-1)/4,$$
$$A_s^{(1)}=
\frac1{48}\left(12s^2+6s+1-\frac1{2s+1}
-2\sum_{q=0}^{s-1}\frac1{2q+1}\right).\tag{11}$$

空和在 $s=0$ 时取零。所有 $2s+1<p$，没有使用非法的 $u^m/p$ 奇系数。
式 (9) 的首层和为
$16\sum r^2/(2r)=4m(m+1)=-1$ 于 $\mathbb F_p$，
再次得到已接受的首层 $-\chi H^m$。

### Step 4. 新层的完整有限和

将新层系数除以单位 $\chi4^{-m}$，记其特征零有限和表达式为 $R_m$。
由式 (9)—(11)，准确有

$$R_m=-\frac43\sum_{r=1}^m r^3-2\sum_{r=1}^m r^2
+\frac13\sum_{r=1}^m r+16\sum_{s=0}^{m-1}(m-s)A_s^{(1)}.\tag{12}$$

最后一和的两个分母项可合并。交换有限双和后，

$$2\sum_{s=0}^{m-1}(m-s)\sum_{q=0}^{s-1}\frac1{2q+1}
=\sum_{q=0}^{m-1}\frac{(m-q-1)(m-q)}{2q+1}.$$

再加直接项 $\sum(m-s)/(2s+1)$，恰得到

$$C_m=\sum_{s=0}^{m-1}\frac{(m-s)^2}{2s+1}
=-\frac{m(3m+2)}4+\frac{(2m+1)^2}{4}H_o,
\quad H_o=\sum_{s=0}^{m-1}\frac1{2s+1}.\tag{13}$$

最后等式来自逐项除法
$(m-s)^2/(2s+1)=-m+s/2-1/4+(2m+1)^2/[4(2s+1)]$。
多项式部分是

$$\sum_{s=0}^{m-1}(m-s)(12s^2+6s+1)
=\frac{m(m+1)(2m^2-1)}2.\tag{14}$$

将式 (13)—(14) 及
$\sum r=m(m+1)/2$、$\sum r^2=m(m+1)(2m+1)/6$、
$\sum r^3=m^2(m+1)^2/4$ 代回式 (12)，得到

$$\boxed{R_m=-\frac{(2m+1)^2H_o+12m^3+13m^2+2m}{12}.}\tag{15}$$

这是明确的有限有理身份；所用各分母在当前范围都是 $p$ 单位。
约化 $2m+1=p=0$、$m=-1/2$ 后，分子多项式部分为 $3/4$，因此

$$R_m=-1/16\quad\text{于 }\mathbb F_p.$$

再用 $4^{-m}=1$，式 (1) 得证。

### Step 5. 实际代入与线性端点

原低块形式整，且 $M\ge5m\ge m+2$，故所有形式模 $p$ 误差在实际代入后
都属于 $h^{m+2}\mathcal O^+$。由式 (1) 得式 (2)。
式 (3) 使用准确系数关系 $B_{\rm low}=-4^m[L^m]\mathcal B_1$。
算子 $\mathcal E-m$ 消去首层 $H^m$；因 $p=2m+1$，式 (4) 只用
$\lambda_H$ 的首项 $4\chi H^m$ 与 $B_{\rm low}$ 的次项 $\chi H^{m+1}/16$。
故其系数为 $-4\chi\cdot\chi/16=-1/4$。证毕。

## Verification and boundaries

主控用自由符号精确运算核对式 (14)、(15) 及对 $2m+1$ 的多项式余式；
这是有限代数交叉检查，不替代上述一般证明，也不计非作者独审。
所有目标系数仅使用偶下标 $r\le m$、奇下标 $s<m$；最小素数 $p=5$ 全部除数合法。
第一 forcing 的已接受根结构没有重开或改变。

## Corrections or Missing Assumptions

无需要削弱或额外增加的科学假设。必须使用形式整 Euler 身份，
不能把第一 forcing 的真实单点赋值直接求导，也不能忽略式 (9) 中两个端点权重。

## Open Risks

本件只给第三 forcing 的线性端点新层 $-1/4$。
有限参照误差、高带相应修正和同阶二次响应尚须各自合并；
没有因此宣布 $\overline{h^{-p}pC_D}$ 非零、完整负 Newton 图或 Paper30 已完成。
