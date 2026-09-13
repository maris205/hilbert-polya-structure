# Proof Package：全局形式辛 gauge 的首次有界证明预筛

日期：2026-09-06。性质：作者证明预筛；不是独立审查、Route 评价、正式立项或产物验收。
唯一新增文件为本报告；不修改量子、几何、特征正数候选或当前状态记录。

## Claim

固定任意 $c\in\mathbb C$，令 $A=\mathbb C[x,y]$，
$\{f,g\}=f_xg_y-f_yg_x$，$\sigma=H_c^*$，
$H_c(x,y)=(x^2+c-y,x)$。对一个固定的 $h\in A$，令
$$
g=h-\sigma h,\qquad U_h(\varepsilon)=e^{\varepsilon\operatorname{ad}_g}\sigma,
\qquad \operatorname{ad}_f=\{f,\cdot\}.
$$
问题是存在否
$$
C_\varepsilon=\exp\!\left(\operatorname{ad}_{K_\varepsilon}\right),\qquad
K_\varepsilon=\varepsilon h+\varepsilon^2h_2+\varepsilon^3h_3+\cdots,\quad h_j\in A,
\qquad U_h=C_\varepsilon\sigma C_\varepsilon^{-1}.
$$
所有系数都是全局多项式，不是固定点附近坐标的局部形式展开。

本报告证明以下有限合同结论。

1. **全参数三次分类。** 对每个 $c\in\mathbb C$、每个普通次数
   $\deg h\le3$，下列条件等价：共轭方程通过三阶
   （模 $\varepsilon^4$）；存在全阶形式共轭；存在
   $h=b+aX_i$，其中 $a,b\in\mathbb C$、
   $i\in\{-2,-1,0,1\}$。这些解都有精确的
   $C_\varepsilon=e^{\varepsilon\operatorname{ad}_h}$，
   事实上它及其逆均在 $\mathbb C[\varepsilon,x,y]$ 中为多项式辛自同构。
2. **二阶零集的完整三次分解。** 除上述四条坐标直线及常数外，
   二阶零集恰由下述 A、B 两类显式代数曲线族及其 reversor 像组成，
   允许任意非零复缩放及加常数。它们全部恰在三阶失败；
   A 族有恒非零三阶商系数 $30$，B 族有 $14/9$。
   这些系数在非零缩放 $\lambda$ 后乘以 $\lambda^3$。
3. **尖锐性。** 对每个固定 $c\in\mathbb C$，确有普通次数三的固定
   $h$ 通过二阶而首次在三阶失败；次数不超过二时没有此类例子。
   因而三次合同的三阶截断不可降为二阶。
4. **四次合同的诚实边界。** 对全部复 $c$、全部 $\deg h\le4$，
   本报告给出二阶零集的精确、必要充分的 $17$ 条齐次二次方程。
   未完成该四次零集的显式不可约分解，也未筛尽其三阶零集。
   另保留一个有理系数的四次固定 $h$ 的完整三阶失败证书。

这里“二阶零集”不是线性核；它是齐次二次障碍映射的代数零集。
“坐标直线”均指模常数后的直线；在 $A$ 中对应二维线性子空间
$\mathbb C+\mathbb C X_i$，不同此类子空间仅在常数上相交。

## Status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION**

原始目标覆盖全部普通次数不超过四的显式二阶分类及后续分支；
本报告没有声称完成这项完整四次分解。完成且证明闭合的是：
全部复 $c$ 的三次显式分类与精确三阶判据，以及四次二阶零集的隐式代数描述。
以下三次主定理本身是 **PROVABLE AS STATED**；四次分解与更高次数分类是 **OPEN**。

## Assumptions

- 基域始终为 $\mathbb C$，$c$ 任意；不删去特殊参数，不假设系数为实数。
- 分类按复参数点集逐点解释；不声称三阶理想等于全阶障碍理想，
  也不声称任意非约化参数基上的函子等价。
- $h$ 固定且不依赖 $\varepsilon$；不能向 $g$ 外加任意高阶项制造障碍。
- 仅限制起始 $h$ 的普通次数；求解时不限制 $h_2,h_3,\ldots$ 的次数。
- 对 Hamiltonian 商掉常数，因为且仅因为
  $\ker(f\mapsto\operatorname{ad}_f)=\mathbb C$。
- 等式和 BCH 展开全部在 $\varepsilon$-adic 拓扑中解释。
  不要求一般 $\operatorname{ad}_h$ 局部幂零或解析收敛。
- 采用已接受 Paper29 的轨道标准基及 orbit-coefficient 判据；
  不重新审查其 PDF 或构建产物。

## Notation

定义 $X_0=x$、$X_{-1}=y$，并在全部整数指标上规定
$$
X_{i+1}+X_{i-1}=X_i^2+c,\qquad \sigma X_i=X_{i+1}.
$$
于是
$$
X_{-2}=y^2+c-x,\quad X_1=x^2+c-y,\quad
X_{-3}=(y^2+c-x)^2+c-y,\quad X_2=(x^2+c-y)^2+c-x.
$$
普通次数不超过四的单一轨道坐标恰为
$i=-3,-2,-1,0,1,2$，其次数依次为 $4,2,1,1,2,4$。
在三次合同内只剩中间四个。

对有限无重复整数集 $S$，写 $M_S=\prod_{j\in S}X_j$。
空集给出常数 $1$。对任意非空 $S$，令
$\widehat S=\{j-\min S:j\in S\}$。商空间
$$
\overline{\mathcal H}=A/((\sigma-1)A+\mathbb C)
$$
有基 $[M_S]$，其中选择 $\min S=0$ 的非空有限集。
$Q_S(f)$ 表示 $f$ 的标准形中所有平移为 $S$ 的词的系数和；
常数不计入任何 $Q_S$。

写 $\Delta=1-\sigma$。称“通过第 $n$ 阶”，意为存在多项式
$h_2,\ldots,h_n$ 使目标等式模 $\varepsilon^{n+1}$ 成立。

## Proof Strategy

先用 BCH 固定二、三阶的符号与 gauge 唯一性，再把起始三次
$h$ 的二阶条件按最外侧混合词逐项分支。分支只用非零条件下的除法，
不以实系数正定性或通用参数假设排除复解。
在每个非坐标分支中，选取一个与二阶原函数的单坐标项无关的三阶商系数，
用有限的括号/标准形计算直接证明它恒非零。

四次部分只给完整 $17$ 方程和一个精确反例证书，不进入无界消元。

## Dependency Map

1. BCH 与 $\ker\operatorname{ad}=\mathbb C$ 给出二、三阶可解条件。
2. Paper29 的轨道标准基、shift 与 orbit-coefficient 判据给出商类的精确检测，
   同时证明多项式原函数模常数唯一。
3. Leibniz 规则与轨道递推给出本报告全部有限系数计算。
4. reversor 与非零缩放保持各有限阶可解性，保证手分支覆盖全部三次解。
5. 两个恒非零三阶系数排除全部额外分支；单坐标解由交换导子精确构造。
6. 四次必要充分方程使用同一标准基，但未被当作四次显式分解。

实际依赖的已接受文件仅为
[Paper29 第2节](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/2_orbit_algebras.tex)
的轨道基/shift，以及
[第3节](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/3_filtered_primitives.tex)
的普通次数适配基与完整 orbit 障碍。
本报告不依赖周期点检测、几何 reducedness 或数值实验。

## Proof

### Step 1. BCH 符号、二阶原函数与三阶不变量

设 $B=\{h,\sigma h\}$。由于 $\sigma$ 是 Poisson 自同构，
$$
C_\varepsilon\sigma C_\varepsilon^{-1}\sigma^{-1}
=e^{\operatorname{ad}_{K_\varepsilon}}
 e^{-\operatorname{ad}_{\sigma K_\varepsilon}}.
$$
Hamiltonian 的 BCH 级数到三阶为
$$
\operatorname{BCH}(K,-\sigma K)
=\Delta K-\frac12\{K,\sigma K\}
-\frac1{12}\{K+\sigma K,\{K,\sigma K\}\}
+O(\varepsilon^4).
$$
这里所有 Hamiltonian 等式均允许相差常数；映到导子后这些常数恰好消失。
比较二阶得
$$
\Delta h_2=\frac12B\pmod{\mathbb C}. \tag{1}
$$
因而通过二阶当且仅当 $[B]=0$ 于 $\overline{\mathcal H}$。

若 $\Delta f$ 为常数，则其标准形常数系数为零，因此该常数为零。
非恒定轨道上的有限系数序列不可能在非零平移下不变，
故 $\ker\Delta=\mathbb C$。由此，满足 (1) 的 $h_2$ 模常数唯一。

比较三阶得
$$
\Delta h_3=T(h,h_2)\pmod{\mathbb C},\qquad
T(h,h_2)=\frac12\bigl(\{h,\sigma h_2\}+\{h_2,\sigma h\}\bigr)
+\frac1{12}\{h+\sigma h,B\}. \tag{2}
$$
所以在二阶可解后，三阶可解当且仅当 $[T]=0$。
给 $h_2$ 加常数不改变 (2)，因此本报告的三阶非零系数与 gauge 选择无关。

若
$B=b_\varnothing+\sum_O\sum_j b_{O,j}\sigma^jM_O$
且每个非恒定 orbit 的系数和为零，则可取
$$
h_2=\frac12\sum_O\sum_j
\left(\sum_{k\le j}b_{O,k}\right)\sigma^jM_O. \tag{3}
$$
累积和在两端都为零，因此这是有限和、多项式，
并且 $\Delta h_2=(B-b_\varnothing)/2$。
这是下文使用的确定二阶原函数规则。

### Step 2. 有限括号计算规则及三次系数

基本括号为
$$
\{X_i,X_{i+1}\}=-1,\qquad \{X_i,X_i\}=0,\qquad
\{X_i,X_j\}=2X_{j-1}\{X_i,X_{j-1}\}-\{X_i,X_{j-2}\}\quad(j\ge i+2). \tag{4}
$$
第一式由 $\{x,x^2+c-y\}=-1$ 及 shift 得出，第三式由轨道递推与 Leibniz 得出；
反向指标用反对称性。每次出现平方时用
$$
X_i^2\longmapsto X_{i-1}+X_{i+1}-c. \tag{5}
$$
每次替换严格降低形式词的因子数，故结束；唯一性为已接受的标准基结果。
对两个标准词，逐因子使用 Leibniz 后应用 (4)、(5)，再按平移求和，
就得到 $Q_S$。这给出可手工验证、与参数特殊值无关的有限计算。

三次适配基使每个 $\deg h\le3$ 唯一写为
$$
\begin{aligned}
h={}&b+uX_{-2}+vX_{-1}+wX_0+zX_1\\
&+pX_{-2}X_{-1}+qX_{-2}X_0+sX_{-1}X_0
+kX_{-1}X_1+lX_0X_1. \tag{6}
\end{aligned}
$$
这是常数加九个非恒定标准词，不漏任何普通三次单项式。

记 $E_S=Q_S(\{h,\sigma h\})$。用于分支的六个最高支撑方程为
$$
\begin{aligned}
E_{024}&=-18lp,\\
E_{04}&=-15(kp+lq),\\
E_{013}&=-2(6ul+6kp+5kq),\\
E_{023}&=-2(5kq+6lq+6zp),\\
E_{03}&=-3(6uk+k^2-4ckp+6lp-4clq+3ls+6zq+3ps+q^2),\\
E_{012}&=-2(4uz+3kl+3kp-4ckq+3ks+3lq+3pq+3qs).
\end{aligned} \tag{7}
$$
数字下标缩写集合，例如 $024$ 代表 $\{0,2,4\}$。
剩余方程为 $E_0,E_{01},E_{02}$；
它们是附录四次表令 $a_0=a_5=a_8=a_{12}=a_{13}=0$ 后的对应三式。
以下分支中会给出用到的全部约化式，故无需依赖计算机解方程。

### Step 3. Reversor、缩放和坐标分支

令 $R f(x,y)=f(y,x)$。有
$$
R\sigma R=\sigma^{-1},\quad R X_i=X_{-1-i},\quad
\{Rf,Rg\}=-R\{f,g\}.
$$
它在 (6) 中交换
$$
u\leftrightarrow z,\quad v\leftrightarrow w,\quad
p\leftrightarrow l,\quad q\leftrightarrow k,\qquad s\leftrightarrow s.
$$
不仅二阶零集，而且每个有限阶和全阶可解性都被 $R$ 保持。确实，
$$
R U_h(\varepsilon)^{-1}R=U_{Rh}(-\varepsilon).
$$
若 $K_h(\varepsilon)$ 给出某有限阶共轭，则
$-R K_h(-\varepsilon)$ 给出 $Rh$ 的同阶共轭，首项仍为 $\varepsilon Rh$。
其第 $j$ 阶 Hamiltonian 为 $(-1)^{j+1}Rh_j$，特别 $h_2'=-Rh_2$。
此证明同时处理 anti-symplectic 符号与参数变号，不能只交换变量后忽略符号。

加常数不影响任何导子。非零缩放 $h\mapsto\lambda h$ 对应
$\varepsilon\mapsto\lambda\varepsilon$，保持有限阶可解性；
可以取 $h_2\mapsto\lambda^2h_2$，于是 $[T]\mapsto\lambda^3[T]$。

先完整处理普通次数不超过二的子空间，即 $p=q=k=l=0$。
其非零二阶系数恰为
$$
\begin{aligned}
E_{012}&=-8uz,&E_{02}&=-6s(u+z),\\
E_{01}&=-4(uw+vz)-6s^2,\\
E_0&=-2\bigl(uv+vw+wz-3uz
+3s(u+v+w+z)-2cs(u+z)-cs^2\bigr).
\end{aligned} \tag{8}
$$
若 $s\ne0$，前两式给 $uz=0$、$u+z=0$，故 $u=z=0$，
第三式成为 $-6s^2=0$，矛盾。因此 $s=0$。
剩余条件为
$$
uz=0,\qquad uw+vz=0,\qquad uv+vw+wz=0.
$$
若 $u\ne0$，则 $z=w=v=0$；若 $z\ne0$，则 $u=v=w=0$。
若 $u=z=0$，则 $vw=0$。故二次二阶零集恰为
$b+aX_i$，$i=-2,-1,0,1$。

对任何单坐标 $h=b+aX_i$，
$\{h,\sigma h\}=-a^2$ 为常数，故
$[\operatorname{ad}_h,\operatorname{ad}_{\sigma h}]=0$，
从而
$$
e^{\varepsilon\operatorname{ad}_h}\sigma
e^{-\varepsilon\operatorname{ad}_h}
=e^{\varepsilon\operatorname{ad}_{h-\sigma h}}\sigma. \tag{9}
$$
此外 $\operatorname{ad}_{X_i}=\sigma^i\operatorname{ad}_x\sigma^{-i}$，
而 $\operatorname{ad}_x=\partial_y$ 局部幂零。
所以 (9) 的 gauge 是代数参数 $\varepsilon$ 上的多项式自同构，
逆亦多项式。这是同一精确构造的直接性质，不另算独立机制。

### Step 4. 全部三次额外二阶零点的穷尽分支

由 $E_{024}=0$ 有 $lp=0$。借助 $R$ 可令 $l=0$，
但不删除其像；最终答案明确包含两类的 $R$ 像。

**分支 A：$p\ne0$。**
由 $E_{04}=0$ 得 $k=0$；由 $E_{023}=0$ 得 $z=0$。
此时 (7) 中剩下
$$
q^2+3ps=0,\qquad q(p+s)=0. \tag{10}
$$
若 $q=0$，则 $s=0$，而 $E_{02}=-6wp$ 强制 $w=0$，
随后 $E_{01}=-6p^2$ 不为零，矛盾。故 $q\ne0$，
$s=-p$，$q^2=3p^2$。

除以非零 $\lambda=p$，令 $r=q/p$、$t=u/p$；
则 $r^2=3$。在这个规范化图上，其余系数均指除以 $p$ 后的值，
且
$$
(2r-3)t+(3+2r)w=0,\qquad tw+rv+9=0.
$$
因为 $3+2r\ne0$，逐式求解得
$$
w=(4r-7)t,\qquad v=\frac{7r-12}{3}t^2-3r.
$$
最后剩余的唯一方程为 $E_0=4P_A(c,t,r)=0$，其中
$$
P_A(c,t,r)=c\bigl(8+(4-2r)t\bigr)+(15r-26)t^3+(3r-6)t. \tag{11}
$$
因此定义
$$
\begin{aligned}
h_A(c,t,r)={}&tX_{-2}
+\left(\frac{7r-12}{3}t^2-3r\right)X_{-1}
+(4r-7)tX_0\\
&+X_{-2}X_{-1}+rX_{-2}X_0-X_{-1}X_0,\qquad r^2=3. \tag{12}
\end{aligned}
$$
本分支恰为 $b+\lambda h_A(c,t,r)$，
$\lambda\ne0$、$P_A(c,t,r)=0$。
把 (12) 代回九个二阶系数，除 $E_0=4P_A$ 外八式均为零，
证明这些必要条件也是充分条件。

**分支 B：$p=0$，且已取 $l=0$。**
由 $E_{013}=0$ 得 $kq=0$。再次允许 $R$，可令 $k=0$。
若也有 $q=0$，已经落入 Step 3 的完整二次分类。
剩下 $q\ne0$，除以 $\lambda=q$，置 $q=1$、$u=t$。
由 $E_{03}=0$、$E_{012}=0$ 依次得
$$
z=-\frac16,\qquad s=\frac{2t}{9}.
$$
然后 $E_{02}=0$ 与 $E_{01}=0$ 依次给出
$$
w=-\frac{t^2}{3}-\frac{23t}{18}-\frac c3,\qquad
v=\frac25t^3+\frac{13}{9}t^2+\frac23ct-\frac{17}{5}.
$$
剩余的唯一方程为 $E_0=P_B(c,t)/810=0$，其中
$$
\begin{aligned}
P_B(c,t)={}&216t^5+528t^4+(576c-550)t^3+(80c+534)t^2\\
&+(360c^2+420c+807)t-1080c^2+11034c. \tag{13}
\end{aligned}
$$
因此定义
$$
\begin{aligned}
h_B(c,t)={}&tX_{-2}
+\left(\frac25t^3+\frac{13}{9}t^2+\frac23ct-\frac{17}{5}\right)X_{-1}\\
&+\left(-\frac{t^2}{3}-\frac{23t}{18}-\frac c3\right)X_0-\frac16X_1
+X_{-2}X_0+\frac{2t}{9}X_{-1}X_0. \tag{14}
\end{aligned}
$$
本分支恰为 $b+\lambda h_B(c,t)$，
$\lambda\ne0$、$P_B(c,t)=0$。
直接代入九式，除 $E_0=P_B/810$ 外其余均零，证明充分性。

**覆盖与边界。**
整个二阶零集是四坐标直线，加上 (12)、(14) 的非零缩放、
常数平移以及各自的 $R$ 像。
这不是仅 generic 参数上的分类：所有除法的分母都是明确非零的
$p$、$q$、$3+2r$ 或固定有理数；
$p=0$、$q=0$ 已分别覆盖，$r$ 两个复根均保留。
两族在非零缩放下始终是普通三次多项式：
A 的 $y^3$ 最高项系数为 $1$，B 的 $xy^2$ 最高项系数为 $1$；
参数变化不能使它们降为坐标分支。允许 $\lambda=0$ 只会回到已包含的常数。
同一个零点即便存在重复表示也不影响上述穷尽的集合等式。

### Step 5. 两族的三阶恒非零证书

在 $P_A=0$ 或 $P_B=0$ 上用 (3) 定义 $h_2$。
其非单坐标部分分别为
$$
\begin{aligned}
(h_2^A)_{\mathrm{mixed}}={}&
-6X_{-2}X_{-1}+\xi X_{-2}X_0+6X_{-1}X_0
-3rX_{-2}X_{-1}X_0,\\
\xi={}&(21-14r)t+2r, \tag{15}\\
(h_2^B)_{\mathrm{mixed}}={}&
-\frac52X_{-2}X_{-1}-\frac{23t}{9}X_{-2}X_0
-\frac23X_{-2}X_1+\eta X_{-1}X_0,\\
\eta={}&-\frac{60ct+36t^3+110t^2-891}{270}. \tag{16}
\end{aligned}
$$
A 的剩余部分在 $\operatorname{span}(X_{-2},X_{-1},X_0)$ 中，
B 的剩余部分在 $\operatorname{span}(X_{-2},X_{-1},X_0,X_1)$ 中，
系数由 (3) 唯一指定。将 (15)、(16) 代入 $\Delta h_2-B/2$，
所有多因子标准词项消失；对剩余单坐标项用 (3) 累积。
若在参数曲线之外仍取截至最右项之前的累积和，
残差的非恒定部分分别为 $-2P_A X_1$、$-P_B X_2/1620$。
在对应曲线上二者为零，常数允许留下。

以下选定的三阶系数均不受上述单坐标项影响；
逐项用 (4)、(5) 检查，对任何对应范围的单坐标线性组合 $N$，
$$
Q_{012}\bigl(\{h_A,\sigma N\}+\{N,\sigma h_A\}\bigr)=0,\quad
Q_{04}\bigl(\{h_B,\sigma N\}+\{N,\sigma h_B\}\bigr)=0. \tag{17}
$$
因此只需列出混合项的有限计算。
把 (2) 分为交叉项 $T_{\mathrm{cross}}$ 与嵌套项
$T_{\mathrm{nested}}$，含各自的 $1/2$、$1/12$ 系数。

| 规范化分支 | 选定商系数 | $Q(T_{\mathrm{cross}})$ | $Q(T_{\mathrm{nested}})$ | 合计 |
| --- | --- | --- | --- | --- |
| A，$r^2=3$ | $Q_{012}$ | $45$ | $-15$ | $30$ |
| B | $Q_{04}$ | $7/3$ | $-7/9$ | $14/9$ |

为使表格可独立手核，A 族交叉项的全部非零贡献如下。
第一列为 $h_A$ 的标准词，第二列为 $h_2^A$ 的标准词；
数值已经乘上词系数及交叉项的 $1/2$。

| $h_A$ 词 | $h_2^A$ 词 | 对 $Q_{012}$ 的贡献 |
| --- | --- | --- |
| $(-2,-1)$ | $(-2,0)$ | $-3\xi$ |
| $(-2,-1)$ | $(-2,-1,0)$ | $27r/2$ |
| $(-2,0)$ | $(-2,-1)$ | $18r$ |
| $(-2,0)$ | $(-1,0)$ | $-18r$ |
| $(-2,0)$ | $(-2,-1,0)$ | $45$ |
| $(-1,0)$ | $(-2,0)$ | $3\xi$ |
| $(-1,0)$ | $(-2,-1,0)$ | $-27r/2$ |

它们的和为 $45$。嵌套项按 $h_A+\sigma h_A$ 的外侧词分组，
仅四词给出非零贡献。置 $\theta=(28rt+r-42t)/2$，它们依次是
$$
(-2,-1): -\theta,\quad
(-2,0): \frac32(4r-5),\quad
(-1,1): -\frac32(4r+5),\quad
(0,1): \theta.
$$
总和为 $-15$。
B 族交叉项只有词对 $((-2,0),(-2,1))$ 贡献 $7/3$，
嵌套项只有外侧词 $(-2,0)$ 贡献 $-7/9$。
这些有限表格直接由 (4)、(5) 得出；附录代码可复算，
不是把 CAS 的布尔成功作为证明前提。

所以 A、B 两族的 $[T]$ 都不为零。
非零缩放不能消除这些系数；Step 3 的 reversor 等价性排除它们的全部像。
Step 4 已穷尽所有二阶可解三次 $h$，
因此通过三阶的三次 $h$ 恰为 Step 3 的坐标分支，
而这些分支由 (9) 全阶精确可积，证明主分类。

### Step 6. 截断阶和普通次数的尖锐性

固定任意 $c\in\mathbb C$，选择任一个 $r$ 满足 $r^2=3$。
在 (11) 中，$t^3$ 的系数 $15r-26$ 不为零：
否则平方后会得到 $675=676$。
因此 $P_A(c,t,r)$ 是真正的三次复多项式，有复根 $t$。
选定任何这样的根后，(12) 是一个固定的普通三次 $h$，
通过二阶而由 Step 5 在三阶失败。
这里选定的是 $h$ 的固定系数，不是事后改变 $\varepsilon$ 高阶扰动。

Step 3 证明所有二次二阶通过者全阶可积；
故对每一个固定复参数 $c$，这种首次三阶失败的最小普通次数都是三。
在 $c=0$ 时可以直接取 $t=0$，得到
$$
h=X_{-2}X_{-1}+rX_{-2}X_0-X_{-1}X_0-3rX_{-1},\qquad r^2=3.
$$
例如 $r=\sqrt3$ 时，
$$
h=y^3+\sqrt3\,xy^2-2xy-\sqrt3\,x^2-3\sqrt3\,y.
$$
其三阶商不仅 $Q_{012}=30$，还有 $Q_{03}=-48$。
因此二阶短例与真正的三阶首次失败已经严格区分。

更简洁的有理三次特例来自 B 族的 $c=t=0$，因为 $P_B(0,0)=0$：
$$
h_B=X_{-2}X_0-\frac16X_1-\frac{17}{5}X_{-1}
=xy^2-\frac76x^2-\frac{97}{30}y.
$$
其二阶原函数可直接取
$$
h_2=-\frac52X_{-2}X_{-1}-\frac23X_{-2}X_1
+\frac{33}{10}X_{-1}X_0,
\qquad \Delta h_2-\frac12\{h_B,\sigma h_B\}=\frac{9409}{1800}.
$$
三阶 $Q_{04}(T)=14/9$ 已由 Step 5 证明。
若需要整数系数，固定 $30h_B=30xy^2-35x^2-97y$ 即可，
相应三阶系数为 $30^3(14/9)=42000$。

### Step 7. 保留的有理四次证书

已有上述有理三次例；以下四次计算只保留本次预筛最初发现的完整证书，
不把“有理系数”当作四次例的额外突破或正文容量理由。

在 $c=0$ 取
$$
h=X_{-3}-6X_{-2}X_0+\frac{102}{5}X_{-1}
=y^4-8xy^2+7x^2+\frac{97}{5}y. \tag{18}
$$
直接按 (4)、(5) 计算得
$$
B=-\frac{9409}{25}
+48X_{-3}X_0-48X_{-2}X_1
-\frac{1188}{5}X_{-2}X_{-1}
+\frac{2088}{5}X_{-1}X_0-180X_0X_1.
$$
每条非恒定 orbit 的系数和为零。可取
$$
h_2=24X_{-3}X_0-\frac{594}{5}X_{-2}X_{-1}+90X_{-1}X_0,
\qquad \Delta h_2-\frac12B=\frac{9409}{50}. \tag{19}
$$
在原坐标中，
$$
h_2=24x^3-48x^2y^2+24xy^4+\frac{924}{5}xy-\frac{594}{5}y^3.
$$
(2) 的完整标准形为
$$
\begin{aligned}
T={}&\frac{2164}{5}X_{-3}+\frac{57518}{25}X_{-2}
-\frac{16182}{25}X_{-1}+\frac{7766}{5}X_0-\frac{8388}{5}X_1-150X_2\\
&+448X_{-3}X_{-1}+336X_{-3}X_1
+\frac{3498}{5}X_{-2}X_0-930X_{-1}X_1\\
&-16X_{-3}X_{-2}X_{-1}-112X_{-3}X_{-1}X_0
-\frac{8872}{5}X_{-2}X_{-1}X_0-264X_{-2}X_{-1}X_1\\
&+528X_{-2}X_0X_1+1080X_{-1}X_0X_1.
\end{aligned}
$$
所以其完整非零商系数为
$$
\begin{array}{c|rrrrrr}
S&0&02&04&012&013&023\\ \hline
Q_S(T)&45296/25&1088/5&336&-3552/5&-264&416.
\end{array}
$$
尤其 $Q_{04}=336\ne0$，故 (18) 恰在三阶失败。
这份四次证书不等于四次所有分支的分类。

综上，所有声称的三次分类、二阶零集穷尽和尖锐性成立。$\square$

## Four-degree exact zero locus

对 $\deg h\le4$，用下面的固定系数顺序：
$$
h=b+\sum_{j=0}^{13}a_jM_j.
$$

| $j$ | 标准词指标 | $j$ | 标准词指标 |
| --- | --- | --- | --- |
| $0$ | $(-3)$ | $7$ | $(-2,0)$ |
| $1$ | $(-2)$ | $8$ | $(-2,1)$ |
| $2$ | $(-1)$ | $9$ | $(-1,0)$ |
| $3$ | $(0)$ | $10$ | $(-1,1)$ |
| $4$ | $(1)$ | $11$ | $(0,1)$ |
| $5$ | $(2)$ | $12$ | $(-2,-1,0)$ |
| $6$ | $(-2,-1)$ | $13$ | $(-1,0,1)$ |

普通次数适配基保证这 $14$ 个非恒定词加常数恰为整个 $V_4$ 的基。
非零二阶商系数只能出现在下列 $17$ 个集合：
$$
\begin{gathered}
0,\ 01,\ 02,\ 03,\ 04,\ 05,\ 012,\ 013,\ 014,\ 023,\ 024,\ 034,\\
0123,\ 0124,\ 0134,\ 0234,\ 01234.
\end{gathered}
$$
下方机器可读的精确式是 $E_S=Q_S(\{h,\sigma h\})$；
所有 $E_S=0$ 是四次合同二阶可解的**必要充分**条件。
这些式对每个复 $c$ 逐点成立；没有除以 $c$ 或先取 generic 参数。
它们给出一个完整隐式代数零集，但不是它的显式不可约分解。
代码记号中的整数元组代表集合，双星号表示幂；a0 至 a13 即上表系数。

```python
E[(0,)] = -2*a0*a1 + 8*a0*a10*c + 16*a0*a10 + 4*a0*a11*c - 18*a0*a11 - 8*a0*a12*c**2 + 32*a0*a12*c - 8*a0*a12 - 16*a0*a13*c**2 + 48*a0*a13*c + 6*a0*a3 - 10*a0*a5 + 4*a0*a6*c - 6*a0*a6 + 16*a0*a7*c + 12*a0*a8*c + 6*a0*a8 + 8*a0*a9*c - 6*a0*a9 + 16*a1*a10*c + 8*a1*a11*c - 6*a1*a11 + 18*a1*a12*c - 8*a1*a13*c**2 + 32*a1*a13*c - 8*a1*a13 - 2*a1*a2 + 6*a1*a4 - 6*a1*a6 + 4*a1*a7*c - 8*a1*a7 + 8*a1*a8*c - 14*a1*a8 + 4*a1*a9*c - 6*a1*a9 + 16*a10**2*c + 6*a10*a11*c - 12*a10*a11 - 16*a10*a12*c**2 + 81*a10*a12*c - 8*a10*a13*c**2 + 36*a10*a13*c - 40*a10*a13 + 4*a10*a2*c - 8*a10*a2 + 4*a10*a4*c - 8*a10*a4 + 16*a10*a5*c - 8*a10*a6*c**2 + 34*a10*a6*c - 6*a10*a6 + 12*a10*a7*c - 24*a10*a7 - 8*a10*a8*c**2 + 34*a10*a8*c - 22*a10*a8 + 6*a10*a9*c - 12*a10*a9 + 2*a11**2*c - 56*a11*a12*c**2 + 25*a11*a12*c - 18*a11*a12 - 4*a11*a13*c**2 + 20*a11*a13*c - 24*a11*a13 + 4*a11*a2*c - 6*a11*a2 - 6*a11*a3 - 6*a11*a4 + 4*a11*a5*c - 6*a11*a5 - 8*a11*a6*c**2 + 58*a11*a6*c - 8*a11*a7*c**2 + 34*a11*a7*c - 6*a11*a7 + 12*a11*a8*c + 20*a11*a9*c - 8*a12**2*c**2 + 56*a12**2*c + 8*a12*a13*c**3 - 92*a12*a13*c**2 + 114*a12*a13*c - 80*a12*a13 + 4*a12*a2*c - 8*a12*a2 + 18*a12*a3*c - 8*a12*a4*c**2 + 32*a12*a4*c - 8*a12*a4 - 16*a12*a5*c**2 + 48*a12*a5*c - 4*a12*a6*c**2 + 20*a12*a6*c - 24*a12*a6 - 8*a12*a7*c**2 + 36*a12*a7*c - 40*a12*a7 - 20*a12*a8*c**2 + 49*a12*a8*c - 38*a12*a8 - 4*a12*a9*c**2 + 20*a12*a9*c - 24*a12*a9 - 8*a13**2*c**2 + 56*a13**2*c + 18*a13*a2*c + 4*a13*a3*c - 8*a13*a3 + 18*a13*a4*c - 8*a13*a5*c**2 + 32*a13*a5*c - 8*a13*a5 - 56*a13*a6*c**2 + 25*a13*a6*c - 18*a13*a6 - 16*a13*a7*c**2 + 81*a13*a7*c - 20*a13*a8*c**2 + 49*a13*a8*c - 38*a13*a8 - 4*a13*a9*c**2 + 20*a13*a9*c - 24*a13*a9 - 2*a2*a3 + 6*a2*a5 - 6*a2*a6 + 2*a2*a8 - 6*a2*a9 - 2*a3*a4 + 4*a3*a6*c - 6*a3*a6 + 4*a3*a7*c - 8*a3*a7 + 2*a3*a8 - 6*a3*a9 - 2*a4*a5 + 8*a4*a6*c - 6*a4*a6 + 16*a4*a7*c + 8*a4*a8*c - 14*a4*a8 + 4*a4*a9*c - 6*a4*a9 + 4*a5*a6*c - 18*a5*a6 + 8*a5*a7*c + 16*a5*a7 + 12*a5*a8*c + 6*a5*a8 + 8*a5*a9*c - 6*a5*a9 + 2*a6**2*c + 6*a6*a7*c - 12*a6*a7 + 12*a6*a8*c + 20*a6*a9*c + 16*a7**2*c - 8*a7*a8*c**2 + 34*a7*a8*c - 22*a7*a8 + 6*a7*a9*c - 12*a7*a9 - 8*a8**2*c**2 + 52*a8**2*c + 20*a8*a9*c + 2*a9**2*c
E[(0, 1)] = 16*a0*a10*c + 16*a0*a11*c + 8*a0*a12*c - 16*a0*a13*c**2 - 4*a0*a2 + 12*a0*a4 - 10*a0*a7 + 16*a0*a8*c + 8*a0*a9*c - 10*a1*a10 + 8*a1*a11*c - 14*a1*a12 + 8*a1*a13*c - 4*a1*a3 + 12*a1*a5 + 8*a1*a8*c - 13*a10**2 + 4*a10*a11*c - 8*a10*a12*c**2 - 43*a10*a12 + 20*a10*a13*c - 4*a10*a3 - 10*a10*a5 + 8*a10*a6*c + 16*a10*a7*c + 12*a10*a8*c + 4*a10*a9*c - 6*a11**2 + 52*a11*a12*c + 12*a11*a13*c - 30*a11*a6 + 8*a11*a7*c - 9*a11*a8 - 15*a11*a9 - 4*a12**2*c**2 - 37*a12**2 - 16*a12*a13*c**2 + 80*a12*a13*c - 14*a12*a3 + 8*a12*a4*c - 16*a12*a5*c**2 + 12*a12*a6*c + 20*a12*a7*c + 44*a12*a8*c + 12*a12*a9*c - 4*a13**2*c**2 - 37*a13**2 - 14*a13*a2 - 14*a13*a4 + 8*a13*a5*c + 52*a13*a6*c - 8*a13*a7*c**2 - 43*a13*a7 + 44*a13*a8*c + 12*a13*a9*c - 4*a2*a4 - 4*a2*a7 - 4*a3*a5 + 8*a4*a6*c - 10*a4*a7 + 8*a4*a8*c + 16*a5*a6*c + 16*a5*a7*c + 16*a5*a8*c + 8*a5*a9*c - 6*a6**2 + 4*a6*a7*c - 9*a6*a8 - 15*a6*a9 - 13*a7**2 + 12*a7*a8*c + 4*a7*a9*c - 30*a8**2 - 18*a8*a9 - 6*a9**2
E[(0, 2)] = -8*a0*a10 + 8*a0*a12*c - 14*a0*a12 + 28*a0*a13*c - 6*a0*a6 + 8*a0*a7*c - 12*a0*a8 - 6*a0*a9 + 8*a1*a10*c - 6*a1*a11 + 8*a1*a13*c - 14*a1*a13 - 4*a1*a7 - 4*a1*a8 - 6*a1*a9 - 6*a10*a11 + 36*a10*a12*c + 8*a10*a13*c - 20*a10*a13 - 4*a10*a2 - 4*a10*a4 + 8*a10*a5*c + 8*a10*a6*c - 18*a10*a6 - 12*a10*a7 + 8*a10*a8*c - 18*a10*a8 - 6*a10*a9 + 24*a11*a12*c - 9*a11*a12 + 6*a11*a13*c - 12*a11*a13 - 6*a11*a2 - 6*a11*a5 + 24*a11*a6*c + 8*a11*a7*c - 18*a11*a7 + 8*a11*a8*c + 22*a12**2*c - 24*a12*a13*c**2 + 28*a12*a13*c - 58*a12*a13 - 6*a12*a2 + 8*a12*a4*c - 14*a12*a4 + 28*a12*a5*c + 6*a12*a6*c - 12*a12*a6 + 8*a12*a7*c - 20*a12*a7 - 8*a12*a8*c**2 + 4*a12*a8*c - 37*a12*a8 + 6*a12*a9*c - 12*a12*a9 + 22*a13**2*c - 6*a13*a3 + 8*a13*a5*c - 14*a13*a5 + 24*a13*a6*c - 9*a13*a6 + 36*a13*a7*c - 8*a13*a8*c**2 + 4*a13*a8*c - 37*a13*a8 + 6*a13*a9*c - 12*a13*a9 - 2*a2*a8 - 6*a3*a6 - 4*a3*a7 - 2*a3*a8 - 6*a4*a6 + 8*a4*a7*c - 4*a4*a8 - 6*a4*a9 - 8*a5*a7 - 12*a5*a8 - 6*a5*a9 - 6*a6*a7 + 8*a6*a8*c + 8*a7*a8*c - 18*a7*a8 - 6*a7*a9 + 16*a8**2*c + 8*a8*a9*c
E[(0, 3)] = 16*a0*a10*c + 12*a0*a12*c - 40*a0*a13 + 4*a0*a4 - 18*a0*a7 + 16*a0*a8*c - 18*a1*a10 - 6*a1*a12 + 12*a1*a13*c + 4*a1*a5 - 3*a10**2 - 31*a10*a12 - 18*a10*a5 + 12*a10*a6*c + 8*a10*a8*c + 24*a11*a12*c - 18*a11*a6 + 12*a11*a7*c - 15*a11*a8 - 9*a11*a9 - 31*a12**2 + 42*a12*a13*c - 6*a12*a3 + 12*a12*a4*c - 40*a12*a5 + 32*a12*a8*c - 31*a13**2 - 6*a13*a2 - 6*a13*a4 + 12*a13*a5*c + 24*a13*a6*c - 31*a13*a7 + 32*a13*a8*c - 18*a4*a7 + 16*a5*a7*c + 16*a5*a8*c - 15*a6*a8 - 9*a6*a9 - 3*a7**2 + 8*a7*a8*c - 12*a8**2 - 18*a8*a9
E[(0, 4)] = -16*a0*a10 + 6*a0*a11 - 12*a0*a12 + 24*a0*a13*c - 18*a0*a8 - 12*a1*a13 - 15*a10*a6 - 7*a10*a8 + 18*a11*a12*c - 15*a11*a7 - 18*a12*a13 - 12*a12*a4 + 24*a12*a5*c - 18*a12*a8 - 12*a13*a5 + 18*a13*a6*c - 18*a13*a8 + 6*a5*a6 - 16*a5*a7 - 18*a5*a8 - 7*a7*a8
E[(0, 5)] = -24*a0*a13 - 24*a12*a5
E[(0, 1, 2)] = -12*a0*a10 + 16*a0*a11*c - 6*a0*a12 + 16*a0*a13*c - 8*a0*a3 + 24*a0*a5 - 8*a0*a8 - 6*a1*a13 - 8*a1*a4 - 6*a10*a11 + 8*a10*a12*c - 10*a10*a13 - 6*a10*a6 + 8*a10*a7*c - 6*a10*a8 - 6*a10*a9 - 24*a11*a12 - 9*a11*a13 - 6*a11*a7 + 8*a11*a8*c + 12*a12**2*c + 28*a12*a13*c - 12*a12*a13 - 6*a12*a4 + 16*a12*a5*c - 9*a12*a6 - 10*a12*a7 + 8*a12*a8*c - 12*a12*a8 - 9*a12*a9 + 12*a13**2*c - 6*a13*a5 - 24*a13*a6 + 8*a13*a7*c + 8*a13*a8*c - 12*a13*a8 - 9*a13*a9 - 8*a2*a5 - 4*a2*a8 - 4*a3*a8 + 16*a5*a6*c - 12*a5*a7 - 8*a5*a8 - 6*a6*a7 + 8*a6*a8*c - 6*a7*a8 - 6*a7*a9
E[(0, 1, 3)] = 16*a0*a10*c - 12*a0*a11 + 16*a0*a13*c - 12*a0*a8 - 12*a0*a9 - 12*a1*a11 - 5*a10*a13 - 12*a10*a6 - 10*a10*a7 - 2*a10*a8 - 9*a11*a12 + 12*a12*a13*c - 23*a12*a13 - 14*a12*a4 - 9*a12*a6 - 5*a12*a7 + 12*a12*a8*c - 10*a12*a8 - 14*a13*a5 - 9*a13*a6 + 12*a13*a7*c - 20*a13*a8 - 9*a13*a9 - 8*a4*a8 - 12*a5*a7 + 16*a5*a8*c - 10*a7*a8
E[(0, 1, 4)] = -20*a0*a10 + 24*a0*a13*c + 8*a0*a5 - 21*a11*a12 - 11*a12*a8 - 18*a13*a6 - 16*a5*a8
E[(0, 2, 3)] = -12*a0*a10 - 14*a0*a12 + 16*a0*a8*c - 14*a1*a13 - 8*a1*a8 + 12*a10*a12*c - 5*a10*a13 - 10*a10*a7 - 10*a10*a8 - 9*a11*a12 - 9*a11*a13 - 12*a11*a7 + 12*a12*a13*c - 23*a12*a13 + 16*a12*a5*c - 5*a12*a7 - 20*a12*a8 - 9*a12*a9 - 9*a13*a6 + 12*a13*a8*c - 10*a13*a8 - 12*a4*a6 - 12*a5*a6 + 16*a5*a7*c - 12*a5*a8 - 12*a5*a9 - 2*a7*a8
E[(0, 2, 4)] = -18*a0*a13 - 15*a10*a12 - 18*a11*a6 + 18*a12*a13*c - 18*a12*a5 - 15*a13*a7 - 6*a8**2
E[(0, 3, 4)] = 8*a0*a5 - 16*a0*a8 - 18*a11*a12 + 24*a12*a5*c - 21*a13*a6 - 11*a13*a8 - 20*a5*a7
E[(0, 1, 2, 3)] = -12*a0*a13 - 16*a0*a4 - 16*a1*a5 - 14*a10*a12 - 12*a11*a8 - 8*a12**2 - 12*a12*a5 - 8*a13**2 - 14*a13*a7 - 12*a6*a8
E[(0, 1, 2, 4)] = -24*a0*a11 - 21*a12*a13
E[(0, 1, 3, 4)] = -28*a0*a13 - 28*a12*a5
E[(0, 2, 3, 4)] = -21*a12*a13 - 24*a5*a6
E[(0, 1, 2, 3, 4)] = -32*a0*a5
```

## Corrections or Missing Assumptions

- “二阶零集只有单坐标直线”的初始猜测在三次已经被反驳，
  不是只在四次或某个未保留的参数边界被反驳。
- 正确的全参数三次结论是“通过三阶当且仅当单坐标”，
  不能把二阶和三阶互换。
- 已显式保留 $r^2=3$ 的两根、任意复系数、全部 $c$、
  零缩放退化、reversor 的反辛符号以及 Hamiltonian 常数商。
- 起始次数限制从来没有施加到后续未知 $h_j$；
  因而非可解结论不是人工原函数次数上界造成的。
- 四次 $17$ 方程尚未显式分解，不能写成四次全阶分类完成。

## Actual Verification

实际完成的是有限精确符号诊断及上述作者证明，不是数值实验或独立审查。

1. 读取 AGENTS、WORKFLOW、当前批次入口、proof-writer 完整技能，
   指定 portfolio 的 §5(F)、§12，以及上述 Paper29 的实际使用部分。
2. 用 (4)、(5) 构造全部 $14\times14=196$ 个标准基对
   $\{M_i,\sigma M_j\}$；逐个与原坐标
   $f_xg_y-f_yg_x$ 的直接展开核对，全部在符号参数 $c$ 上相等。
3. 得到并保留全部 $17$ 个四次二阶系数；
   三次分支通过精确代入及手工零因子分情况穷尽。
   一次规范化四次端点分支的 Gröbner 试算出现表达式膨胀，
   未用它支持任何显式四次分类或证明，随后停止该消元方向。
4. 对 A、B 两个三次族，在符号参数 $c,t$ 上计算 $B,h_2,T$；
   A 始终保留关系 $r^2=3$。两个族的 $B$ 和完整 $T$
   均与直接 $x,y$ 求导表达式精确一致。
5. 三阶所选系数另拆成交叉项、嵌套项和逐标准词贡献，
   得到表中 $45-15=30$ 及 $7/3-7/9=14/9$，
   并检查允许的二阶单坐标部分不影响这些系数。
6. 四次有理例的 $B,h_2,T$ 也与直接坐标计算相符，
   残差确为允许的常数 $9409/50$，三阶 $Q_{04}=336$。
7. 未重审旧 PDF、未编译、未改旧报告或状态；未查新评分、
   未作正式 Route 评价、未创建 Paper30 项目、未外发或使用付费资源。

## Open Risks

- 本文件是作者证明包，尚待 fresh 独立数学检查；精确脚本核对不代替该检查。
- 普通次数四的显式二阶分解、三阶零集和全阶解集仍为 **OPEN**。
- 任意次数的全阶分类仍需控制更长混合标准词的抵消；
  三次中两类分支的恒非零系数不能未经证明推广到所有支撑。
- 本次没有证明任意预定首次失败阶的构造，也没有证明任何一般次数
  的明确统一截断阶、可终止算法或复杂度界。
- 一阶条件、BCH 通用递推、坐标直线的交换导子构造，以及本合同的短闭合，
  不自动构成独立长文容量。这里不评新意/容量分数，不据此授予立项。
  也不将本 F 问题补入已停止的几何或量子候选为其增加篇幅。

## Reproduction appendix

下方代码仅进行小型、精确的符号代数。
它实现证明中已经列明的有限规则，可复算全部四次方程；
没有参数抽样或浮点计算。单坐标项和常数分别保留到指定的商步骤，
不会把原坐标常数项误当标准形常数项。
复制运行时使用本地 Python 与 SymPy；本报告不要求安装或更改任何环境。

```python
import sympy as s
from functools import lru_cache
from collections import defaultdict
c=s.Symbol('c'); aa=s.symbols('a0:14')
B=[(-3,),(-2,),(-1,),(0,),(1,),(2,),(-2,-1),(-2,0),(-2,1),(-1,0),(-1,1),(0,1),(-2,-1,0),(-1,0,1)]
@lru_cache(None)
def norm(t):
 t=tuple(sorted(t))
 for i in range(len(t)-1):
  if t[i]==t[i+1]:
   k=t[i]; rest=t[:i]+t[i+2:]; out=defaultdict(lambda:0)
   for new,f in [(rest+(k-1,),1),(rest+(k+1,),1),(rest,-c)]:
    for u,v in norm(tuple(sorted(new))).items(): out[u]+=f*v
   return {u:s.expand(v) for u,v in out.items() if v!=0}
 return {t:s.Integer(1)}
@lru_cache(None)
def br(i,j):
 if i==j:return {}
 if i>j:return {u:-v for u,v in br(j,i).items()}
 if j==i+1:return {():s.Integer(-1)}
 out=defaultdict(lambda:0)
 for u,v in br(i,j-1).items():
  for t,w in norm(tuple(sorted(u+(j-1,)))).items():out[t]+=2*v*w
 for t,w in br(i,j-2).items():out[t]-=w
 return {u:s.expand(v) for u,v in out.items() if v!=0}
def wordbr(t,u):
 out=defaultdict(lambda:0)
 for ii,i in enumerate(t):
  for jj,j in enumerate(u):
   rest=t[:ii]+t[ii+1:]+u[:jj]+u[jj+1:]
   for z,v in br(i,j).items():
    for r,w in norm(tuple(sorted(rest+z))).items():out[r]+=v*w
 return out
out=defaultdict(lambda:0)
for i,t in enumerate(B):
 for j,u in enumerate(B):
  for r,v in wordbr(t,tuple(k+1 for k in u)).items():
   if r: out[tuple(k-r[0] for k in r)] += aa[i]*aa[j]*v
out={r:s.factor(v) for r,v in out.items() if s.expand(v)!=0}

expected = {
 (0,), (0,1), (0,2), (0,3), (0,4), (0,5),
 (0,1,2), (0,1,3), (0,1,4), (0,2,3), (0,2,4), (0,3,4),
 (0,1,2,3), (0,1,2,4), (0,1,3,4), (0,2,3,4), (0,1,2,3,4)
}
assert set(out) == expected
for shape in sorted(out, key=lambda u:(len(u),u)):
 print(shape, s.factor(out[shape]))
```

### 三次族与三阶证书的精确复算

下面代码接在上一代码块后运行。它在全部符号参数上检查两族的
唯一二阶曲线条件、二阶原函数残差、选定三阶系数及单坐标项独立性；
还把完整括号与原坐标求导交叉核对。
关系 $r^2=3$ 通过精确多项式余式保留，不选择浮点平方根。

```python

r,t=s.symbols('r t')
def red(e):return s.factor(s.rem(s.expand(e),r*r-3,r))
subA={a:s.Integer(0) for a in aa}
subA.update({aa[1]:t,aa[2]:(7*r-12)*t*t/3-3*r,aa[3]:(4*r-7)*t,aa[6]:1,aa[7]:r,aa[9]:-1})
subB={a:s.Integer(0) for a in aa}
subB.update({aa[1]:t,aa[2]:s.Rational(2,5)*t**3+s.Rational(13,9)*t*t+s.Rational(2,3)*c*t-s.Rational(17,5),aa[3]:-t*t/3-s.Rational(23,18)*t-c/3,aa[4]:-s.Rational(1,6),aa[7]:1,aa[9]:s.Rational(2,9)*t})

def Padd(*terms):
 out=defaultdict(lambda:0)
 for fac,pol in terms:
  for t,v in pol.items():out[t]+=fac*v
 return {t:red(v) for t,v in out.items() if red(v)!=0}
def Pbr(P,Q):
 out=defaultdict(lambda:0)
 for u,a in P.items():
  for v,b in Q.items():
   for w,z in wordbr(u,v).items():out[w]+=a*b*z
 return {w:red(v) for w,v in out.items() if red(v)!=0}
def shift(P):return {tuple(k+1 for k in u):v for u,v in P.items()}
def quotient(P):
 out=defaultdict(lambda:0)
 for u,v in P.items():
  if u:out[tuple(k-u[0] for k in u)]+=v
 return {u:red(v) for u,v in out.items() if red(v)!=0}
def primitive(P):
 orbs=defaultdict(dict)
 for u,v in P.items():
  if u:orbs[tuple(k-u[0] for k in u)][u[0]]=v/2
 hp={}
 for u,cf in orbs.items():
  accum=0
  for j in range(min(cf),max(cf)):
   accum=red(accum+cf.get(j,0))
   if accum!=0:hp[tuple(k+j for k in u)]=accum
 return hp

PA = c*(8+(4-2*r)*t)+(15*r-26)*t**3+(3*r-6)*t
PB = (216*t**5+528*t**4+(576*c-550)*t**3+(80*c+534)*t**2
      +(360*c**2+420*c+807)*t-1080*c**2+11034*c)
x,y = s.symbols('x y')
@lru_cache(None)
def X(i):
 if i == 0: return x
 if i == -1: return y
 if i > 0: return s.expand(X(i-1)**2+c-X(i-2))
 return s.expand(X(i+1)**2+c-X(i+2))
def ev(P):
 return s.expand(sum(v*s.prod(X(i) for i in u) for u,v in P.items()))
def sig(f):
 return s.expand(f.subs({x:x*x+c-y,y:x}, simultaneous=True))
def pb(f,g):
 return s.expand(s.diff(f,x)*s.diff(g,y)-s.diff(f,y)*s.diff(g,x))
for name,sub in [('A',subA),('B',subB)]:
 h = {B[i]:v for i,a in enumerate(aa) if (v:=sub[a]) != 0}
 sh = shift(h)
 BB = Pbr(h,sh)
 qq = quotient(BB)
 expected_q2 = 4*PA if name == 'A' else PB/810
 assert set(qq) == {(0,)}
 assert red(qq[(0,)]-expected_q2) == 0
 hh = primitive(BB)
 residual = Padd((1,hh),(-1,shift(hh)),(-s.Rational(1,2),BB))
 last = (1,) if name == 'A' else (2,)
 assert {u for u in residual if u} == {last}
 assert red(residual[last]+expected_q2/2) == 0
 cross = Padd((s.Rational(1,2),Pbr(h,shift(hh))),
              (s.Rational(1,2),Pbr(hh,sh)))
 nested = Padd((s.Rational(1,12),Pbr(Padd((1,h),(1,sh)),BB)))
 TT = Padd((1,cross),(1,nested))
 target = (0,1,2) if name == 'A' else (0,4)
 expected_parts = (45,-15) if name == 'A' else (s.Rational(7,3),-s.Rational(7,9))
 assert red(quotient(cross)[target]-expected_parts[0]) == 0
 assert red(quotient(nested)[target]-expected_parts[1]) == 0
 for j in ([-2,-1,0] if name == 'A' else [-2,-1,0,1]):
  N = {(j,):s.Integer(1)}
  change = Padd((1,Pbr(h,shift(N))),(1,Pbr(N,sh)))
  assert quotient(change).get(target,0) == 0
 hp = ev(h)
 hhpol = ev(hh)
 bdir = pb(hp,sig(hp))
 assert red(bdir-ev(BB)) == 0
 tdir = s.expand((pb(hp,sig(hhpol))+pb(hhpol,sig(hp)))/2
                 +pb(hp+sig(hp),bdir)/12)
 assert red(tdir-ev(TT)) == 0
 print(name, "symbolic checks passed; third coefficient",
       quotient(TT)[target])
```
