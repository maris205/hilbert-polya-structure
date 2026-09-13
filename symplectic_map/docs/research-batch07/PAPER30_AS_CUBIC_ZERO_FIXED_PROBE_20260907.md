# Paper30：特征三零参数的完整 Frobenius 固定空间

日期：2026-09-07。范围：有界纯数学作者探查及并行作者提出的新引理的窄核对；
不是新鲜独立审稿、正式候选评价、稿件或数值实验。只新增本记录，旧记录不改。

## Claim

设 $K$ 为特征 $3$ 的代数闭域，

$$
A=K[x,y],\qquad F=(x^2-y,x),\qquad \sigma=F^*,
\qquad \lambda\in\{1,-1\},
$$

$$
\overline C_\lambda=A/((\sigma-\lambda)A+K),
\qquad \phi\langle h\rangle=\langle h^3\rangle.
$$

本记录证明全部多项式支撑上的结论

$$
\boxed{\ker(\phi-1:\overline C_\lambda\longrightarrow
\overline C_\lambda)=0\quad(\lambda=1,-1).}
\tag{1}
$$

由已接受的 Artin–Schreier 桥接，还得到

$$
\bigl(A/\{u^3-u:u\in A\}\bigr)^{\sigma=\lambda}=0
\quad(\lambda=1,-1).
\tag{2}
$$

## Status

`PROVABLE AS STATED / PROVED`（作者侧证明状态）。

原始完整固定空间目标未削弱；证明不把 Frobenius 核等同于固定空间。
关键新输入是本轮另一作者探查提出、在下文逐式核对的双加权次数引理。
本记录另明确依赖 [移位公式窄勘误](PAPER30_AS_SHIFT_FORMULA_ERRATUM_20260907.md)
修复后的 strong-balanced 引理，不以旧接受报告作为该修复的证据。
本文件不自行授予独立数学终审通过状态。

## Assumptions

- 使用已接受的 [Frobenius coinvariant 证明](PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md)
  中未受勘误影响的轨道基、轨道次数凸性和桥接同构。
  这些未改部分不在本轮重新审稿。
- Strong-balanced 顶层排除改用 [移位公式窄勘误](PAPER30_AS_SHIFT_FORMULA_ERRATUM_20260907.md)
  第 2–3 节：极小代表至多两个且必相邻，再用正确的一步移位及整除性排除碰撞。
  旧 Step 3 的任意多步移位公式确有二进制低位未反转错误，旧独立报告未发现；
  本文不使用错误公式或其一般多步整除论证。修复不改结论量词，但独立关闭仍待完成。
- [已接受处置](PAPER30_AS_FROBENIUS_SCREEN_DISPOSITION_20260907.md)
  中的完整核结论保留，但不是下文固定空间消失的推理前提。
- 第 2–4 步为清晰呈现新局部引理，暂允许一般奇特征 $p$ 及任意 $c$；
  这三步取 $\lambda\in\mathbb F_p^*$，按同一公式定义 $\overline C_\lambda$，
  并暂用 $\phi\langle h\rangle=\langle h^p\rangle$。
  最终主结论 (1) 只在本分工的 $p=3,c=0$ 下陈述。
- 未作有限次数枚举、数值实验、网页检索或正式评分。

## Notation

沿用轨道坐标

$$
X_0=x,\quad X_{-1}=y,\quad X_{i+1}=X_i^2+c-X_{i-1}.
$$

二进制 word $e=(e_i)_{i\in\mathbb Z}$ 有有限支撑，对应

$$
M_e=\prod_iX_i^{e_i},\qquad
a(e)=\sum_{i\ge0}e_i2^i,\qquad
b(e)=\sum_{i\le-1}e_i2^{-i-1}.
$$

记 $M(a,b)$ 为由二进制编码唯一确定的 word 多项式。
其唯一普通次数最高单项式为 $x^ay^b$，系数为 $1$。
对指数对记 $\mu(a,b)=a+b$。
非空 word 的平移轨道为 $O$，其最小普通次数为 $d(O)$。
对非零 coinvariant 向量 $v$，记其最高支撑轨道次数为 $\delta(v)$。

对单项式的两种正加权次数定义为

$$
w_{21}(x^ry^s)=2r+s,\qquad
w_{12}(x^ry^s)=r+2s.
$$

对非零多项式，两种加权次数均定义为其非零单项式的相应权重最大值。

## Proof Strategy

经窄勘误修复的 strong-balanced 引理把非零固定元的最高支撑压到唯一奇反射轨道
$(a,b)=(n,2n+1)$。其 $p$ 次幂的普通最高 word 所在轨道，在原最高次数以下
仅有一个额外的平移伙伴。新双加权界排除该伙伴的系数，因此留下不能消去的
高次轨道 obstruction。这覆盖全部 $n\ge1$，而非检查有限多个例子。
剩余单字母轨道用特征三的精确公式处理。

## Dependency Map

1. 主结论依赖窄勘误第 2–3 节修复后的 strong-balanced 排除、第 4 步的奇反射严格增长及
   第 5 步的单字母公式。
2. 奇反射严格增长依赖第 2 步双加权界和第 3 步完整轨道局部几何。
3. 双加权界仅依赖 $X_i$ 的递推和普通次数三角 normal form。
4. AS 推论 (2) 仅额外使用已接受的全 mixed 桥接同构。
5. 第 1 步记录的权重零/Cartier 观察不进入主结论的依赖链。

## Proof

### Step 1. 原先 Cartier 方向的准确边界

仅在本步取 $p=3,c=0$。给 $x,y$ 分配 $\mathbb Z/3\mathbb Z$ 权重 $1,-1$。
递推使 $X_i$ 的权重为 $(-1)^i$，且 $\sigma$ 交换权重 $1$ 与 $-1$。
Frobenius 的像全部处于权重零部分；故固定元只能使用权重零轨道方向。

令

$$
u=x^3,\qquad v=y^3,\qquad t=xy,\qquad R=K[u,v].
$$

权重零子环为

$$
B=R\oplus tR\oplus t^2R,
\qquad t^3=uv.
$$

以 $S=\sigma|_R$ 记限制，则

$$
S(u)=u^2-v,\qquad S(v)=u,\qquad
\sigma(t)=u-t,\qquad \sigma(t^2)=u^2+ut+t^2.
$$

对 $L=\sigma+1$，直接展开得到

$$
L(a+tb+t^2d)
=La+uS(b)+u^2S(d)
+t\bigl(b-S(b)+uS(d)\bigr)+t^2\bigl(d+S(d)\bigr).
\tag{3}
$$

若此像属于 $R$，则 $S(d)=-d$，由已接受的多项式特征函数引理得 $d=0$；
继而 $S(b)=b$，所以 $b\in K$。故

$$
R\cap L(B)=L(R)+Ku.
\tag{4}
$$

这是真正的精确恒等式，但本身只呈现单字母核障碍，并不提供严格下降的
次数函数。由 (4) 直接声称固定空间消失是不成立的推理；下文另行补足
全局最高层论证。因为主控转向新双权重路线，本步没有继续扩张为一般
Cartier 分类工程。

### Step 2. 双加权界及 normal form 的保持性

本步允许任意奇特征 $p$ 及 $c\in K$。

**引理 1。** $M(a,b)$ 的每个普通单项式 $x^ry^s$ 都满足

$$
2r+s\le2a+b,\qquad r+2s\le a+2b.
\tag{5}
$$

而 $x^ay^b$ 的轨道基 normal form 中，每个出现的 $M(r,s)$ 也满足 (5)。

**证明。** 对 $i\ge0$，由 $X_0=x$、$X_1=x^2+c-y$ 及递推归纳，有

$$
w_{21}(X_i)\le2^{i+1},\qquad w_{12}(X_i)\le2^i.
$$

归纳步中，平方项的权重界加倍，$X_{i-1}$ 和常数的权重不超过这个新界。
向负指标从 $X_{-1}=y$、$X_{-2}=y^2+c-x$ 归纳，得到

$$
w_{21}(X_i)\le2^{-i-1},\qquad
w_{12}(X_i)\le2^{-i}\quad(i\le-1).
$$

逐因子相加便得到 (5)。这些界允许同权重的下层单项式，未假定它们严格变小。

再按普通次数对单项式 $x^ay^b$ 归纳。用

$$
x^ay^b=M(a,b)-\bigl(M(a,b)-x^ay^b\bigr)
$$

作三角消元；括号内每一项的普通次数严格小于 $a+b$，且两权重不超过
$(2a+b,a+2b)$。对每一项使用归纳假设，其 normal form 仍不超过该项的
两个权重。因此全过程保留 (5)，普通次数严格下降保证终止。证毕。

特别地，$M(a,b)^p$ 的 normal form 中每个 $M(r,s)$ 满足

$$
2r+s\le p(2a+b),\qquad r+2s\le p(a+2b),
\tag{6}
$$

且其普通次数最高 word $M(pa,pb)$ 的系数恰为 $1$。

### Step 3. 奇反射顶层目标轨道的完整局部几何

令 $p=2m+1$ 为奇素数，$n\ge1$，并置

$$
D=3n+1,\qquad A=pn,\qquad
W_0=(A,2A+p).
$$

这里 $W_0$ 是源 $M(n,2n+1)^p$ 的普通最高 word 指数对，普通次数为 $pD$。
向右平移一次得到

$$
W_1=(2A+1,A+m),\qquad \mu(W_1)=pD-m.
\tag{7}
$$

取 $\epsilon=A\bmod2$，$\eta=(A+m)\bmod2$，则左邻及第二个右邻满足

$$
W_{-1}=\left(\frac{A-\epsilon}{2},4A+2p+\epsilon\right),
$$

$$
W_2=\left(4A+2+\eta,\frac{A+m-\eta}{2}\right).
$$

精确次数差为

$$
\mu(W_{-1})-pD=\frac{3A+2p+\epsilon}{2}>0,
\tag{8}
$$

$$
\mu(W_2)-pD=\frac{3A-3m+2+\eta}{2}>0.
\tag{9}
$$

最后的不等式使用 $A=pn\ge p=2m+1$。已接受的轨道次数离散凸性，结合
$\mu(W_1)<\mu(W_0)$ 及 (8)–(9)，说明该完整无限轨道中，普通次数不超过
$pD$ 的 word 恰为 $W_0,W_1$。其唯一最小代表为 $W_1$，故

$$
d(O(W_0))=pD-m.
\tag{10}
$$

这一步同时控制两个无限尾部，没有把局部检查当作无限族结论。

### Step 4. 平移伙伴不能消去，且较低来源不能补回

**引理 2。** 若非零 $v\in\overline C_\lambda$ 的所有最高支撑只含奇反射
例外轨道，且 $D=\delta(v)=3n+1$、$n\ge1$，则

$$
\delta(\phi v)\ge pD-\frac{p-1}{2}>D.
\tag{11}
$$

**证明。** 由每个给定 $D$ 只有一条该例外轨道，可以选最小次数代表

$$
h=\alpha M(n,2n+1)+q,\qquad
\alpha\ne0,\qquad \deg q\le D-1.
$$

这里把两个最小位置统一选为 $(n,2n+1)$ 只改变非零轨道系数，不改变 $v$。
特征 $p$ 给出

$$
h^p=\alpha^pM(n,2n+1)^p+q^p.
$$

引理 1 使第一项 normal form 的每个 word 满足
$w_{21}\le4A+p$。但第 3 步唯一可能与 $W_0$ 同轨道的下层伙伴满足

$$
w_{21}(W_1)-w_{21}(W_0)
=(5A+m+2)-(4A+p)=A+1-m>0.
\tag{12}
$$

因此 $W_1$ 的系数为零；$W_0$ 的系数恰为 $\alpha^p\ne0$。
该源的全部其他 word，不是在目标轨道外，就是普通次数超过 $pD$ 而根本
不可能出现。取 $W_0$ 作为目标轨道基准，其 twisted obstruction 遂恰为
$\alpha^p$，不会被平移加权消去。

又由 (10)，

$$
d(O(W_0))=pD-m>p(D-1)\ge\deg(q^p).
\tag{13}
$$

所以 $q^p$ 的任何 normal-form word 都不可能位于该目标轨道。
目标 obstruction 在整个 $h^p$ 中仍非零，得到第一个不等式 (11)。
而

$$
pD-m-D=(p-1)\left(D-\frac12\right)>0,
$$

证明严格增长。此结论没有使用 $c=0$ 或 $p=3$。证毕。

### Step 5. 特征三零参数的完整固定空间

现在回到 $p=3,c=0$，并假设 $v\ne0$ 且 $\phi v=v$。
令 $D=\delta(v)$。若最高层存在 strong-balanced 轨道，使用窄勘误第 3 节修复后的顶层定理，
给出 $\delta(\phi v)=3D>D$，矛盾。因此最高层只能是奇反射轨道，
$D=3n+1$。若 $n\ge1$，引理 2 给出

$$
\delta(\phi v)\ge3D-1>D,
$$

仍矛盾。故 $n=0$，$D=1$，而唯一次数一轨道是单字母轨道。
存在 $a\in K^*$ 使 $v=a u_0$，其中 $u_0=\langle X_0\rangle$。

记 $E=\langle X_0X_1\rangle$。二者来自不同非空 word 轨道，因此线性无关。
使用 $X_0^2=X_{-1}+X_1$，得到精确公式

$$
\phi(u_0)=\langle X_0X_{-1}+X_0X_1\rangle
=(1+\lambda^{-1})E.
\tag{14}
$$

若 $\lambda=-1$，则 $\phi(a u_0)=0\ne a u_0$；
若 $\lambda=1$，则 $\phi(a u_0)=2a^3E\ne a u_0$，
因为 $a\ne0$、$2\ne0$ 且 $E,u_0$ 线性无关。
两种情况都矛盾，故 (1) 成立。已接受桥接随即给出 (2)。证毕。

## Corrections or Missing Assumptions

- 本文的 strong-balanced 依赖已切换到新的窄勘误。旧多步移位错误和旧漏检记录
  保留，不将旧 PASS 重新解释为新修复的证明或独立通过；主结论的假设与量词不变。
- 本轮新增的实质缺口填补是 (12)：原先只知道目标轨道有一个较低普通次数
  平移伙伴，尚未证明其系数为零。两个 Newton 加权界提供了这一结论。
- $n\ge1$ 在引理 2 中不可删除。$n=0$ 的单字母块必须另行处理，
  特别是原有 $p=3,c\ne0,\lambda=-1$ 非零例不会被本证明错误排除。
- 一次 $\bmod 9$ 必要条件和式 (4) 均不是主证明；没有以它们冒充全局消失。
- 本文件只完成指定的 $p=3,c=0$ 结论；其他特征的单字母分析及一般参数
  汇总属于并行作者分工，不在本文件预支结论。

## Open Risks

- 作者侧主结论已闭合；新双加权最高层论证仍须由主控安排的新鲜独立数学
  审查实际核验；该审查还须覆盖新增的相邻极小代表／一步移位修复。
  不能将旧 PASS 或本轮并行作者核对当作这些新依赖的正式独立通过。
- 没有进行论文立项、正文容量判断、稿件编写、编译或对外操作。

## 最终核验记录

- 完整读取指定的两份 AS 输入、工作区入口与 `proof-writer` 技能。
- 对新增部分核对了两种加权界的递推和三角消元保持性。
- 显式计算了 $W_{-1},W_1,W_2$，核对奇偶余数、两个无限尾部及严格不等式。
- 将同源平移消去与较低来源消去分别排除，没有省略其中任一义务。
- 单独处理 $n=0$、$\lambda=1,-1$、非零系数与 Frobenius 半线性。
- 已完整读取新增移位勘误并修订本文件的依赖边界；未改旧冻结作者稿、旧独立报告或处置。
- 未重审未受勘误影响的旧引理；本次只修订本文件，不开展新研究。
