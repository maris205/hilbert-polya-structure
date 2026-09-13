# Derivation / Proof Package：参数伴随后的负端二次端点直接求值

日期：2026-09-08。作者：`/root/negative_adjoint_endpoint_evaluation`。
本件是作者数学推导，不是非作者独立审查。
使用 `formula-derivation` 固定同一有限端点，再使用 `proof-writer` 完成条件求值。
唯一新写文件为本件；旧源、接受记录、实际桥与 ghost 证明不变。

## Target / Claim

固定任意素数 $p\ge5$，令 $m=(p-1)/2$，工作于
$R=\mathbb F_p[H]/(H^2)$。取同一有限低带及 A22 式 (12) 的二次响应
$X,Y$，其源项定义见式 (3)。在下述参数伴随身份 (2) 成立的条件下，直接证明

$$
\boxed{\mathcal C_H(X,Y)=0-\frac12H\pmod{H^2}.}
\tag{1}
$$

这里不使用 A19 的显式 $X_0,Y_0$，也不使用 A22 的六核、双和或其最终
$-1/2$ 答案作为推导输入。计算不先求 $X,Y$，只配对它们的直接驱动。

## Status

**COHERENT AS STATED；PROVABLE AS STATED AS A CONDITIONAL EVALUATION。**

精确条件是式 (2) 的有限参数伴随引理。该引理由同轮主控在
[参数化交叉伴随作者稿](PAPER30_TWIST_NEGATIVE_PARAMETRIC_ADJOINT_PROOF_V1_20260908.md)
式 (1) 中证明；本件已全文读取该稿，核对相同 $R$、偶奇范围、配对权重和直接源。
本件不把它假装成既有接受输入或已完成独审的结论。
在此条件下，式 (1) 的全部求值已在本件完成，包括 $p=5$。
伴随引理及本件的新证明仍须对应的真正非作者变更检查；
旧数学接受状态不因这种新作者化而改变。

## Invariant Object

唯一对象是 A22 同一有限二次响应的完整端点

$$
\mathcal C_H(X,Y)
=-[u^m]f_1X-16[u^{m-1}]f_2(Y+2aX).
$$

参数伴随只是这个端点的另一种有限配对表达，不换动力系统，不改响应源项，
也不以低带的某个子项替代完整端点。

## Assumptions and precise inputs

1. $\Theta=u\partial_u$，$\mathcal Q=2\Theta+1$，
   $\mathcal E=H\partial_H$。有限偶范围为 $1\le j\le m$，
   有限奇范围为 $0\le j\le m-1$。偶常数项单独固定为零。
2. $w=w_0+Hw_1$ 至 $u^m$，$a=a_0+Ha_1$ 至 $u^{m-1}$，
   $f_1=e^w$、$f_2=e^{2w}$，只提取次数至多 $m<p$ 的指数系数。
   所需阶乘都是 $\mathbb F_p$ 的单位。
3. $\mathcal D_eu^j=d_{2j}(H)u^j$，
   $\mathcal D_ou^j=d_{2j+1}(H)u^j$，
   $\mathcal L_e=\mathcal D_e+8uf_2$，
   $\mathcal L_o=\mathcal D_o+8uf_2$，
   $K=f_1/2+16uf_2a$。同一低方程为
   $\mathcal D_ew=-4uf_2$、$\mathcal L_oa=-f_1/2$。
4. **同轮条件输入（不是本件证明的引理）：** 对 $[u^0]X=0$、
   有限奇级数 $Y$，若 $P=\mathcal L_eX$、
   $Q_{\rm src}=\mathcal L_oY+KX$，则

   $$
   \boxed{\mathcal C_H(X,Y)
   =2[u^m](\mathcal Qa)P+4[u^m](\Theta w)Q_{\rm src}.}
   \tag{2}
   $$

   身份在 $R$ 及上述有限配对内使用。本件不把特征零伴随身份约除 $p$，
   不把低精度反射提升成不存在的特征零等式。
5. 完整读取 [A22 作者稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md)
   和 [A19 作者稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md)。
   只将已接受的低带 $w_0,a_0,w_1,a_1$，以及 A22 式 (12) 的同对象驱动
   当作求值输入；不重审未改变的低带证明。
6. A22 的直接驱动准确是

   $$
   \begin{aligned}
   P&=(4+2H\mathcal D_e)\tau^{\rm b}-(16-4H)S_eZ,\\
   Q_{\rm src}&=(4+2H\mathcal D_o)\sigma^{\rm b}-(16-4H)S_oT,\\
   \tau^{\rm b}&=-2\Theta w,&\sigma^{\rm b}&=-\mathcal Qa,\\
   Z&=(\mathcal E-\Theta)w,&T&=(\mathcal E-\Theta-1)a.
   \end{aligned}
   \tag{3}
   $$

   $S_eu^j=S_{2j}(H)u^j$，$S_ou^j=S_{2j+1}(H)u^j$。
   这里保留了非恒定二次传播子 $2H\mathcal D$ 和平方系数的一次变化
   $16-4H$，未退回 A19 的零阶二次系统。

## Notation and truncation conventions

记

$$
f=(1-u)^{-1},\qquad G=(1+u)f,\qquad
\mathscr H=\sum_{r=0}^{m-1}\frac{u^r}{2r+1}.
$$

$f,G$ 是形式有理级数的记号，始终只提取上述有限低次数。
$\mathscr H$ 是明确的有限多项式，绝不调用 $u^m$ 处的 $1/p$。
有

$$
\Theta\mathscr H=\frac{f-\mathscr H}{2}\pmod{u^m}.
\tag{4}
$$

对本件所需次数，已接受低带输入为

$$
\begin{aligned}
w_0&=\sum_{k=1}^{m}\frac{u^k}{k},&a_0&=\frac f2,\\
w_1&=\frac{u(1+u)f^2}{4},&
a_1&=\frac{(1+16u+7u^2)f^3-G\mathscr H}{48}.
\end{aligned}
\tag{5}
$$

$w_0,w_1$ 取至 $u^m$，$a_0,a_1$ 取模 $u^m$。
$\Theta$ 和 $\mathcal Q$ 保持这些截断理想。
式 (2) 的第一乘积中 $P$ 无常数项，因此只需要 $\mathcal Qa$ 至 $u^{m-1}$；
第二乘积中 $\Theta w$ 无常数项，因此只需要 $Q_{\rm src}$ 至 $u^{m-1}$。
未定义的奇第 $m$ 项不会进入配对。

本件以 $A_i=\mathcal Qa_i$、$B_i=\Theta w_i$ 作为简写，
这些 $A_i,B_i$ 不是原实际模态或 forcing 多项式。
$P_i=[H^i]P$、$Q_i=[H^i]Q_{\rm src}$ 都是**直接源项**，
不是 A22 式 (18) 扣去 $\mathcal L_{e1}X_0$、
$\mathcal L_{o1}Y_0+K_1X_0$ 后的同名字号。

## Derivation Strategy / Dependency Map

1. 使用有限参数伴随，把完整端点写成已知低带与直接驱动的配对。
2. 只将该配对展开到 $H^1$；不展开未知响应或求其零阶解。
3. $H^0$ 配对合并为一个有理核，其系数含 $2m+1$ 因子。
4. $H^1$ 配对合并为一个有理核加一个 $\mathscr H$ 核。
5. 两个核的系数是固定分母仅含 $2,3$ 的多项式。
   在实际有限求和区间内用 $m\equiv-1/2$，奇分母逐项约掉，
   只剩一个二次多项式单和。全程是精确身份，没有近似步骤。

## Main Derivation / Proof

### Step 1. 完整直接源的两阶展开

由 A22 的传播子及 Chebyshev 一次系数，

$$
\begin{gathered}
\mathcal D_{e0}=-4\Theta^2,\qquad
\mathcal D_{o0}=-\mathcal Q^2,\\
S_{e0}=2\Theta,\qquad S_{o0}=\mathcal Q,\\
S_{e1}=-(8\Theta^3-2\Theta)/6,\qquad
S_{o1}=-(\mathcal Q^3-\mathcal Q)/6.
\end{gathered}
\tag{6}
$$

直接代入式 (3) 给

$$
\begin{gathered}
Z_0=-B_0,\quad Z_1=(1-\Theta)w_1,\quad
T_0=-f^2/2,\quad T_1=-\Theta a_1,\\
P_0=-8B_0-16S_{e0}Z_0,\qquad
Q_0=-4A_0-16S_{o0}T_0,\\
P_1=-8B_1-4\mathcal D_{e0}B_0
-16S_{e0}Z_1-16S_{e1}Z_0+4S_{e0}Z_0,\\
Q_1=-4A_1-2\mathcal D_{o0}A_0
-16S_{o0}T_1-16S_{o1}T_0+4S_{o0}T_0.
\end{gathered}
\tag{7}
$$

乘 $H$ 的传播子项只需要 $\mathcal D_{e0},\mathcal D_{o0}$；
无需 $\mathcal D_{e1},\mathcal D_{o1}$ 作用于未知响应。
由式 (2)，若 $c_i=[H^i]\mathcal C_H(X,Y)$，则准确有

$$
\begin{aligned}
c_0&=[u^m](2A_0P_0+4B_0Q_0),\\
c_1&=[u^m]\{2(A_1P_0+A_0P_1)+4(B_1Q_0+B_0Q_1)\}.
\end{aligned}
\tag{8}
$$

式 (8) 已包含伴随权重随 $H$ 的变化；它不是只对零阶伴随权重计算新源。

### Step 2. 零阶端点无需二次零阶解

式 (5)—(7) 给

$$
A_0=\frac{(1+u)f^2}{2},\quad B_0=uf,\quad
P_0=8u(u+3)f^2,\quad Q_0=2(u^2+12u+3)f^3.
$$

因此

$$
2A_0P_0+4B_0Q_0=16u(u^2+8u+3)f^4.
\tag{9}
$$

用 $[u^n]f^4=\binom{n+3}{3}$，得到固定分母至多为 $6$ 的身份

$$
\begin{aligned}
c_0
&=16\left\{\binom m3+8\binom{m+1}3+3\binom{m+2}3\right\}\\
&=16m^2(2m+1)=0\qquad\text{于 }\mathbb F_p.
\end{aligned}
\tag{10}
$$

这里的求值从直接源得出，没有引用 A19 的二次端点零结论。

### Step 3. 一次阶配对只剩两个核

为使化简可逐项复算，式 (4)—(7) 给出以下完整表达式：

$$
\begin{aligned}
B_1&=\frac{u(3u+1)f^3}{4},\\
A_1&=\frac{u f^4}{24}
 \{3u^2+42u+27-2(1-u)^2\mathscr H\},\\
P_1&=2u(7u^2-18u-5)f^4,\\
Q_1&=\frac{9u^4+47u^3-247u^2-187u-6}{6}f^5
 -\frac{u(7u+1)}3f^3\mathscr H.
\end{aligned}
\tag{11}
$$

例如 $A_1$ 由 $\mathcal Q$ 作用于式 (5) 的 $a_1$，
每次遇到 $\Theta\mathscr H$ 都只在模 $u^m$ 内使用式 (4)。
同一规则作用于式 (7) 的 $Q_1$，收集有理部分和 $\mathscr H$ 部分，
分别得到式 (11) 的最后一行。

把式 (11) 与 Step 2 的四个零阶量代入式 (8)，收集两类项，准确得到

$$
c_1=[u^m]\{R(u)+J(u)\mathscr H(u)\},
\tag{12}
$$

$$
\boxed{\begin{aligned}
R(u)&=-\frac{8u(3u^3+35u^2+31u+3)}{3(1-u)^5},\\
J(u)&=-\frac{16u^2(2u+1)}{3(1-u)^4}.
\end{aligned}}
\tag{13}
$$

这是式 (8) 的代数化简，不借助端点预期值。
尤其 $J$ 从 $u^2$ 开始，实际上只需要 $\mathscr H$ 至 $u^{m-2}$。
也没有 $\log(1-u)$、二重对数或它们与 $\mathscr H$ 的乘积。

### Step 4. 两个核的有限矩及唯一单和

对全部整数 $n\ge0$，式 (13) 的系数满足

$$
\begin{aligned}
r(n):=[u^n]R&=-\frac{8n(9n^3-n^2+1)}9,\\
j(n):=[u^n]J&=-\frac{8n(n-1)^2}{3}.
\end{aligned}
\tag{14}
$$

证明只需展开

$$
\begin{aligned}
r(n)&=-\frac83\left\{3\binom n4+35\binom{n+1}4
 +31\binom{n+2}4+3\binom{n+3}4\right\},\\
j(n)&=-\frac{16}3\left\{2\binom n3+\binom{n+1}3\right\}.
\end{aligned}
$$

二项式分母只有 $24$ 和 $6$，在所有 $p\ge5$ 中可逆。
这些是有限阶有理系数身份，不是对伴随关系作特征零提升。
低端 $n=0,1$ 也包含在公式内，且 $j(0)=j(1)=0$。

于是式 (12) 完整等于

$$
c_1=r(m)+\sum_{r=0}^{m-1}\frac{j(m-r)}{2r+1}.
\tag{15}
$$

求和上限是原来的整数 $m-1$；末项因 $j(1)=0$ 为零。
没有添加 $r=m$ 的非法 $1/(2m+1)$ 项。
在这个固定区间内，每个 $2r+1$ 都属于 $\{1,3,\ldots,p-2\}$，是单位。

仅在被加数的多项式系数中代入 $m=-1/2$，式 (14) 给

$$
r(m)=-\frac16,\qquad
\frac{j(m-r)}{2r+1}
=\frac{-8\{-(2r+1)/2\}\{-(2r+3)/2\}^2}{3(2r+1)}
=\frac{(2r+3)^2}{3}.
\tag{16}
$$

合法约去 $2r+1$ 后，只剩二次多项式单和。用一次、二次有限幂和，

$$
\sum_{r=0}^{m-1}\frac{(2r+3)^2}{3}
=\frac{m(4m^2+12m+11)}9
=-\frac13\quad\text{于 }\mathbb F_p.
\tag{17}
$$

最后一等号才在已经求完的多项式中使用 $m=-1/2$。
从式 (15)—(17) 得 $c_1=-1/6-1/3=-1/2$；
连同式 (10)，式 (1) 得证。$\square$

## Minimal-prime and algebra checks

- 全部固定分母只含 $2,3$。变动分母只来自 $1\le k\le m$ 和
  $1\le2r+1\le p-2$，不会碰到 $p$。没有四次幂和所带来的 $1/5$。
- 当 $p=5,m=2$，式 (15) 只含 $r=0,1$，后者为零。
  $r(2)=-368/3\equiv4$、$j(2)=-16/3\equiv3$，
  故 $c_1=4+3=2=-1/2$；式 (10) 同样给 $c_0=0$。
  这只是最小边界的展开检查，一般证明由式 (14)—(17) 承担。
- 作者侧实际执行了自由符号核验：以
  $\Theta F=u\partial_uF+(f-\mathscr H)\partial_{\mathscr H}F/2$
  复算式 (7)、(11)、(13)；展开二项式复算式 (14)；
  自由符号求和复算式 (17)。各身份残差为零。
  这些核验不是非作者审查，也不使用素数扫描、零点或拟合。

## Remarks and Interpretation

新参数伴随把端点中的未知响应及乘积随 $H$ 的变化一次吸收进配对权重。
因此二次零层不必解出 $X_0,Y_0$，二次一次层也不必先将未知量的零层
插入 A22 的式 (18) 再用零阶伴随。
求值链由“显式二次零层解—六核—三角双和”变为
“直接驱动—两个低带核—一个二次多项式单和”。
这是作者新推导的逻辑依赖变化，不是版面容量认证或已接受替代处置。

## Boundaries and Non-Claims

- 结论仅是同一有限二次响应端点的模 $H^2$ 求值。
  不独自重建实际高带整性、三参数窗口或参考前污染支撑。
- A22 从实际移位得到式 (3) 的桥、基带和完整线性 Ward 部分仍需保留。
  原真实端点的 ghost 共同缩放及净零证明也仍需保留；
  本件不把各 ghost 项分别设为零。
- 本件条件证明可用于替换二次端点求值部分，不能删除仍被别处实际调用的
  A19/A22 输入，不能擅自删除原接受文件或改写其历史身份。
- 不从旧最终 $-1/2$、实际 $-3/16$ 或最高系数赋值反推任何新身份。
  不授予 Route、科学评分、容量票、Paper30 立项、写稿测页或外部效力。

## Open Risks and Handoff

1. 式 (2) 已有上述同轮主控作者证明：其式 (1) 与本件式 (2) 相同，
   其式 (15) 与本件式 (3) 相同；本件的 $Q_{\rm src}$ 是该稿的 $Q$。
   本件全文读后的接口核对不是该引理的非作者独审。
   $p=5$ 的反射精度及伴随权重边界仍由该稿及其独审负责。
2. 本件新增的式 (7)—(17) 及其与参数伴随的接口需要非作者变更检查。
   已接受且未改变的低带 $w_0,a_0,w_1,a_1$ 不因这种接口检查重开。
3. 在式 (2) 及本件通过相应变更检查前，只能称为作者条件闭合；
   是否形成正式替代，由主控保持原实际桥和 ghost 后另行处置。
