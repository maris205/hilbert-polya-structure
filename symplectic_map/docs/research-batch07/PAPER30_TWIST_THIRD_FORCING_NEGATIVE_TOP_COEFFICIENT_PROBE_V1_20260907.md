# Proof Package：第三 forcing 负端最高参数系数

日期：2026-09-07。作者数学探针；不修改批次入口、旧接受稿或出版锁。目标是计算
\([L^{3m+1}]p^2\mathcal B_3/h^M\bmod h\)，不逐素数扫描、不拟合根。

## Claim

对任意素数 \(p\ge5\)、\(a\ge2\)，令
$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=3m+1=p+m,\qquad
q_3=D,\qquad e_*=M-D .
$$
沿用实际第三 forcing \(\mathcal B_3\)、\(S=h^{-D}p^2\mathcal B_3\) 及已接受首一分解
\(S=P_{\rm cl}U_{\rm cl}\)，\(\deg P_{\rm cl}=m,\deg U_{\rm cl}=p\)。
本文证明最高 \(L\)-系数的 \(h^M\) 主部消失：
$$
\overline{\,p[L^D]\mathcal B_3\,}=0
\quad\text{in }\mathcal O^+/h\mathcal O^+ .
\tag{1}
$$
因此（使用既有 \(p^2[L^D]\mathcal B_3\in h^M\mathcal O^+\)）
$$
v_h([L^D]S)>e_*,
\qquad
v_h([L^p]U_{\rm cl})>e_* .
\tag{2}
$$
本文不声称下一非零层、负端完整 Newton 图或负根的最终斜率。

## Status

**PROVABLE AS STATED**（在下列既有高系数整性桥作为输入的范围内）。
式 (1) 是新的最高参数系数消失证书；式 (2) 是其直接赋值推论。它说明“最高系数恰有
高度 \(e_*\)”这一最简单的单边猜测不能由当前数据成立。

## Assumptions

- \(K^+=\mathbb Q_p(h)\) 为特征零离散赋值域，\(v_h(h)=1\)、\(v_h(p)=M\)。
- 实际递推
  \(d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}\)，其中 \(d_n(0)=-n^2\) 当 \(p\nmid n\)。
- 第三 forcing 定义为
  \(\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}\)，只用 \(n<3p\) 的实际分支。
- 已接受高参数桥：对 \(j>m\)，
  \(p^2[L^j]\mathcal B_3\in h^M\mathcal O^+\)。特别地
  \(p[L^D]\mathcal B_3\in\mathcal O^+\)。
- 已接受首一性给出 \([L^D]S=[L^p]U_{\rm cl}\)；实际次数 \(D\) 的最高系数非零。
- 低于第一个奇共振的真实 Chebyshev 展开可约化为 \(d_n(0)=-n^2\)。奇共振
  及纯二次偶共振的系数只需满足 \(v_h\ge-2m\)（故乘 \(p\) 后消失，
  因 \(M\ge5m>2m\)）；该粗界直接来自共振传播子的 \(h^{2m}\) 首阶和低层
  整性，属于既有阶乘桥的低精度后果，不是参数扫描。

## Notation

引入 Euler 幅度 \(b\)：
$$
d_nV_n(b)=-\frac b2[x^{n-1}]e^{V(b)}
-L[x^{n-2}]e^{2V(b)} .
\tag{3}
$$
令 \(y=Lx^2\)、\(W(y)=V|_{b=0}\)，并令
$$
\left.\partial_bV\right|_{b=0}=xA(y),\qquad u=y/4.
\tag{4}
$$
写 \(\widehat W(u)=W(4u)\)、\(\widehat A(u)=A(4u)\)。
系数下标 \(r\) 指 \(u^r\) 系数。所有带横线的量均取 \(h\)-剩余。

## Proof Strategy

最高 \(L\)-次数的加权齐次性把第一 forcing 项化为纯二次 \(W\)，把第二项化为
\(b\)-线性响应 \(A\)。低层满足两个显式有理生成函数。穿过唯一奇共振 \(p\) 后，
只保留一个 \(p\)-分母层；求出该层的两个有理剩余，再代回最高项。两个贡献分别含
\(p\)，故 \(h^M\) 主部相消。

## Dependency Map

1. (3)--(4) 给出最高 \(L\)-次数的纯二次／线性分解。
2. 低层递推给出 \(\widehat W_0=-\log(1-u)\)、\(\widehat A_0=1/[2(1-u)]\)。
3. \(p\)-带递推给出 \(\tau(u)=\overline{p\widehat W_{p+\bullet}}\) 和
   \(\sigma(u)=\overline{p\widehat A_{p+\bullet}}\)。
4. 代入 \([L^D]\mathcal B_3\) 得 (1)，再用既有高系数整性桥得 (2)。

## Proof

### Step 1. 最高 \(L\)-次数的两个递推

令 \(b=0\) 后所有奇次 \(V_n\) 消失，\(W\) 为偶次部分。对 \(r\ge1\)，直接从 (3) 得
$$
d_{2r}\,[u^r]\widehat W
 =-4[u^{r-1}]e^{2\widehat W}.
\tag{5}
$$
对 \(b\) 在零处求导，奇次部分写成 \(xA(y)\)，得到
$$
d_{2r+1}\,[u^r]\widehat A
 =-\frac12[u^r]e^{\widehat W}
-8[u^{r-1}]e^{2\widehat W}\widehat A .
\tag{6}
$$
这里的因子 \(4\) 和 \(8\) 仅来自 \(y=4u\)。式 (5)--(6) 是有限递推的逐项恒等式，
不涉及 \(V_{3p}\)。

### Step 2. 共振前的有理低层

对 \(r<p\) 且 \(2r+1\ne p\)，有
\(d_{2r}\equiv-4r^2\)、\(d_{2r+1}\equiv-(2r+1)^2\pmod h\)。
逐项唯一性给出
$$
\widehat W_0(u)=-\log(1-u),\qquad
\widehat A_0(u)=\frac1{2(1-u)}
\tag{7}
$$
在后续所需的低次数内。这里的对数只表示其系数级数；涉及的系数下标均小于 \(p\)，
分母为 \(p\)-单位。奇共振下标 \(r=m\) 不被 (7) 用来求解；其实际系数的既有界
\(v_h\ge-m\) 意味着乘 \(p\) 后在剩余域中消失，因为 \(M>m\)。

### Step 3. 偶次 \(p\)-带

定义
$$
\tau_j=\overline{p[u^{p+j}]\widehat W},\qquad
\tau(u)=\sum_{j=0}^{m}\tau_ju^j .
$$
由 \(v_h([u^p]\widehat W)\ge-2m\)，有 \(\tau_0=0\)。
在次数 \(p+j<2p\) 内，唯一的阶 \(p\) 分母来自低层对数的
\(u^p/p\)；故对 \(0\le j\le m\)，
$$
\overline{p[u^{p+j}]e^{2\widehat W}}
=[u^j]\frac{2}{(1-u)^2}\bigl(\tau(u)-1\bigr).
\tag{8}
$$
解释 (8)：完整级数 \(e^{2\widehat W_0}=(1-u)^{-2}\) 的 \(p\)-倍系数为零；
截断低级数相对于它少掉 \(2u^p/p\)，给出 \(-2(1-u)^{-2}\)，而实际
\(p\)-带系数贡献为 \(2(1-u)^{-2}\tau\)。更高的两个 \(p\)-分母在
\(p+j<2p\) 不可能同时出现。

把 (8) 代入 (5)，并使用 \(d_{2p+2j}\equiv-4j^2\)（\(j\ge1\)），得到
$$
j^2\tau_j=[u^{j-1}]\frac{2}{(1-u)^2}(\tau-1),\qquad 1\le j\le m .
\tag{9}
$$
有理级数
$$
\boxed{\tau(u)=-\frac{2u}{1-u}}
\tag{10}
$$
满足 \(\tau_0=0\) 和 (9)：右端系数为 \(-2j^2\)。逐项唯一性证明 (10) 是所需
\(p\)-带的唯一剩余，而不是经验拟合。

### Step 4. 奇次 \(p\)-带

定义
$$
\sigma_j=\overline{p[u^{p+j}]\widehat A},\qquad
\sigma(u)=\sum_{j=0}^{m-1}\sigma_ju^j .
$$
中间奇共振系数 \(A_m,\ldots,A_{p-1}\) 的高度至多为 \(-2m\)，故
 \(p\)-倍后为零；
在 \(p+j< p+m\) 的右端，它们也不能与新的 \(p\)-带相乘产生所需次数。
因此只有低层 \(A_0\)、偶次 \(p\)-带和奇次 \(p\)-带本身参与。

记
$$
E_1(u)=\frac{\tau(u)-1}{1-u}
       =-\frac{1+u}{(1-u)^2},\qquad
E_2(u)=\frac{2(\tau(u)-1)}{(1-u)^2}
       =-\frac{2(1+u)}{(1-u)^3}.
\tag{11}
$$
其中 \(E_1\) 是 \(\overline{p[u^{p+\bullet}]e^{\widehat W}}\)，
\(E_2\) 是 \(\overline{p[u^{p+\bullet}]e^{2\widehat W}}\)。
将 (6) 乘 \(p\)，并用 \(d_{2p+2j+1}\equiv-(2j+1)^2\)，得到
$$
(2j+1)^2\sigma_j
=\frac12[u^j]E_1
+8[u^{j-1}]
\left(\frac{\sigma(u)}{(1-u)^2}
+E_2(u)\frac1{2(1-u)}\right)
\quad(0\le j<m),
\tag{12}
$$
其中 \(j=0\) 时第二项为空。直接代入并逐项比较可得唯一解
$$
\boxed{\sigma(u)=-\frac{1+u}{2(1-u)^2}} .
\tag{13}
$$
例如 \(\sigma_0=-1/2\)；一般 \(j\) 的左端为
\(-(2j+1)^3/2\)，右端同值。因 \(2j+1<p\)，递推除数均为单位，
故 (13) 在全部所需 \(0\le j<m\) 上成立。

### Step 5. 最高系数的相消

第一项 \([x^{3p-1}]e^V\) 的最高 \(L^D\) 次只来自 \(e^W\)；
第二项的最高 \(L^D\) 次必须取 \(b\)-线性部分
\(\partial_be^V|_{b=0}=xe^WA\)。由 \(y=4u\)，
$$
[L^D]\mathcal B_3
=-4^{-D}\left(
[u^{p+m}]e^{\widehat W}
+16[u^{p+m-1}]e^{2\widehat W}\widehat A
\right).
\tag{14}
$$
将 (11)--(13) 代入 p-带提取，得到
$$
4^D\overline{p[L^D]\mathcal B_3}
=-[u^m]E_1
-16[u^{m-1}]
\left(\frac{\sigma(u)}{(1-u)^2}
+E_2(u)\frac1{2(1-u)}\right).
\tag{15}
$$
第一项为 \(-[u^m]E_1=2m+1=p\)，在剩余域中为零。括号内化简为
$$
-\frac32\frac{1+u}{(1-u)^4}.
$$
故其 \(u^{m-1}\) 系数为
$$
-\frac32\left\{\binom{m+2}{3}+\binom{m+1}{3}\right\}
=-\frac{m(m+1)(2m+1)}4
=-\frac{m(m+1)p}{4},
\tag{16}
$$
也在特征 \(p\) 中为零。由 (15)--(16) 得 (1)。

### Step 6. 转回首一商的赋值

既有高参数桥给 \(p^2[L^D]\mathcal B_3\in h^M\mathcal O^+\)，故
\(p[L^D]\mathcal B_3\in\mathcal O^+\)。结合 (1)，
\(v_h(p[L^D]\mathcal B_3)\ge1\)，从而
$$
v_h\!\left(h^{-D}p^2[L^D]\mathcal B_3\right)
\ge M+1-D=e_*+1 .
$$
首一性给 \([L^D]S=[L^p]U_{\rm cl}\)，即得 (2)。证毕。 \(\square\)

## Corrections or Missing Assumptions

- 本文没有把 \([L^p]U_{\rm cl}\) 的下一层 \(e_*+1\) 宣称为精确值；只证明严格大于 \(e_*\)。
- (8) 的“单个 \(p\)-分母”范围是 \(p+j<2p\)，本稿只用 \(0\le j\le m<p\)；
  因此没有隐藏二次 \(p\)-分母。
- 本文不从最高系数消失推断另一中间系数必为 \(e_*\)，也不推断新的 Newton 边。

## Open Risks

- 要确定负因子的准确 Newton 图，仍需计算 \(h^{e_*}\) 层中 \(U_{\rm cl}\) 的最低次数
  非恒定系数；最高系数的 \(h^M\) 主部已被本稿排除。
- 野分歧下一层、负根简单性和分裂域仍未解决；本稿没有声称这些结论。
- 所有结论适用于全部 \(p\ge5,a\ge2\)，但不涉及 \(p=3\) 真共振、完整 forcing
  分裂域或 \(\mathcal B_2,\mathcal B_3\) 互素性。
