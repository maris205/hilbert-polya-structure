# P29 内部研究：最小对称素理想集合与随机选择的精确代价

记录日期：2026-09-09 UTC。第四次 P29–P33 五篇整轮内部论证。
承接[不动素理想分类与选择判准][criterion]及[无限本原障碍族][family]。
本篇研究单值 E+D 已失败之后，两种明确改变输出类型的数学替代：
有限素理想集合，以及素理想上的概率分布。

原项目的冻结值域仍是单个非零 Gaussian 素理想。下面的集合／概率值
构造不是原机制的解，不登记候选，不改 owner 域或冻结公理，也不把
增加随机性称为获得轨道算术信息。它们只是辨明对称障碍的最小代价。

## 1. 继承对象与新的输出类型

沿用完整 level-(3) 群的本原无向 loxodromic owner 集 X，Gaussian
共轭对合记为 \(\sigma\)。从已经确认的本原代表得到

\[
T=2+9a,\qquad d(x)=D_9(x)=a(4+9a)=\frac{T^2-4}{9},
\qquad d(\sigma x)=\overline{d(x)}.
\tag{1}
\]

这里 \(a\in\mathbb Z[i]\)，且 \(|d(x)|\ge5\)。设

\[
S(d)=\{\mathfrak p:\mathfrak p\text{ 为非零 Gaussian 素理想},
\ d\in\mathfrak p\},\qquad S(x)=S(d(x)).
\tag{2}
\]

上一轮已自含证明 S 非空有限及
\(S(\bar d)=\overline{S(d)}\)。本轮的有限集合规则要求

\[
\varnothing\ne A(x)\subseteq S(x),\qquad
A(\sigma x)=\overline{A(x)}.
\tag{3}
\]

共轭作用于集合中的每个理想。单值 E+D 恰是 (3) 中
\(|A(x)|=1\) 的特殊情形。集合不是理想的乘积或交，也不是将两个
不同素理想合并后冒称为一个素理想。

称规则为“判别式局部的”，是指存在映射 \(\mathcal A\)，使
\(A(x)=\mathcal A(d(x))\)，且在
\(\mathcal D=d(X)\) 上满足
\(\mathcal A(\bar d)=\overline{\mathcal A(d)}\)。
这是一条额外的输入限制；一般 owner 规则还可能使用 d 之外的信息。

## 2. 最小范数层总共不超过两个素理想

定义理想范数 \(N\mathfrak p=|\mathbb Z[i]/\mathfrak p|\)。
上一轮对 \(\mathbb F_p[t]/(t^2+1)\) 的完备分类，同时给出

\[
\begin{array}{c|c|c}
\text{有理素数情形}&\text{上方素理想}&N\mathfrak p\\
\hline
p=2&(1+i)&2\\
p\equiv3\pmod4&(p)&p^2\\
p\equiv1\pmod4&(p,i-r),(p,i+r),\ r^2\equiv-1\pmod p&p
\end{array}
\tag{4}
\]

最后一行的两个理想不同且互为共轭；其余两行各只有一个，且被共轭
固定。表中商域的大小直接给范数，不需要新的素因子资料表。

不同有理素数的上方素理想不可能因范数而出现第三个并列值：
素数不能等于另一素数的平方，而不同正素数的平方也不同。因此
每个范数层最多有两个 Gaussian 素理想；若有两个，必为一个分裂
共轭对。

令

\[
A_{\min}(x)=
\{\mathfrak p\in S(x):N\mathfrak p
          =\min_{\mathfrak q\in S(x)}N\mathfrak q\}.
\tag{5}
\]

S 非空有限，范数又在共轭下不变，所以 (5) 对全部 X 满足 (3)，且

\[
1\le |A_{\min}(x)|\le2.
\tag{6}
\]

这已给出一个不要求先判断 \(\sigma x=x\) 的全域集合值规则。
但最小范数不一定使集合基数最小：较小范数的分裂对可能同时伴随
一个较大范数的共轭不动素因子。第 5 节给真实本原 owner 的例子。

## 3. 判别式局部规则的逐点最小基数

### 3.1 数据不动点与 owner 不动点不应混淆

对本项目的 d，若 \(d\in\mathbb R\)，则其实 \(d\in\mathbb Z_{>0}\)。
证明如下：写 \(T=t+is\)，由 (1)，
\(t=2+9\operatorname{Re}a\ne0\)。而 \(T^2=4+9d\) 为实数使
\(2ts=0\)，故 s=0。于是 T 为实整数，loxodromic 给
\(|T|>2\)，从而 d 为正整数。

这没有证明 \(\sigma x=x\)。即使某个 owner 对合轨道有两个元素，
它们也可能具有相同的实判别式；本篇没有断言这种情形确实出现，
也不将其实迹条件当作 owner 判等程序。

记

\[
F(d)=\{\mathfrak p\in S(d):\overline{\mathfrak p}=\mathfrak p\}.
\tag{7}
\]

对实 d，上一轮给出
\(F(d)\ne\varnothing\) 当且仅当 \(2\mid d\)，或 d 有一个
\(3\bmod4\) 的有理素因子。

### 3.2 显式构造

先在所有非零 Gaussian 素理想上固定一个可比较的序：
先比较范数，再比较下方有理素数；对分裂理想
\((p,i-r)\)，以 \(0\le r<p\) 的整数值破同层并列。
由 (4)，这是无歧义的有限比较规则。它本身不要求共轭不变。

在 \(\mathcal D\) 上定义 \(\mathcal A_*(d)\)：

1. 若 \(\operatorname{Im}d>0\)，取 S(d) 中上述序最小理想的单元素集。
2. 若 \(\operatorname{Im}d<0\)，取
   \(\overline{\mathcal A_*(\bar d)}\)；此时 \(\bar d\) 已由第 1 项定义。
3. 若 d 为实且 \(F(d)\ne\varnothing\)，取 F(d) 中范数最小的单个理想。
4. 若 d 为实且 \(F(d)=\varnothing\)，取 S(d) 的最小范数层。

第 3 项没有并列：不动素理想的范数为 2 或不同素数的平方。
第 4 项因 S(d) 本身共轭稳定且无不动点，最小范数层必恰为一个
完整的分裂共轭对。因此

\[
A_*(x)=\mathcal A_*(d(x))
\tag{8}
\]

满足 (3)，并且

\[
|A_*(x)|=
\begin{cases}
2,&d(x)\in\mathbb R,\ F(d(x))=\varnothing,\\
1,&\text{其余情形}.
\end{cases}
\tag{9}
\]

这里选择 \(\operatorname{Im}d\) 的符号用的是原 Gaussian 坐标。
该构造只证明所列共轭等变性，不声称对其他未指定的坐标对称也自然。

**命题 1。** (9) 在全部判别式局部的非空集合值规则中逐点最小。

证明。在非实 d 或实 d 具有不动素因子时，非空集合的基数至少为 1，
而 (9) 达到 1。在实 d 且无不动素因子时，任一数据局部等变规则
必须满足 \(\mathcal A(d)=\overline{\mathcal A(d)}\)。S(d) 分解成
无不动点的二元共轭轨道，故其非空不变子集至少有两个元素；
(9) 恰取一个轨道而达到 2。□

最优性中的“判别式局部”不能删去。一般 owner 规则在一个真正的
二点 owner 轨道上可以使用额外数据选定方向，上一轮已给抽象单值
选择；若它们具有实 d，仅靠 d 则不能分辨。对真正不动的坏 owner，
基数至少 2 的下界才对所有 owner 集合规则都成立。

### 3.3 有限算术可求值，不等于已有 owner 算法

给定确切的非零 Gaussian 整数 \(d=A+Bi\)，全部 S(d) 可由有限整除
检验得到。先对正整数 \(N=d\bar d=A^2+B^2\) 做有限试除，得到
所有有理素因子 p；任何含 d 的素理想收缩到这样的 p，因为
\(d\bar d\) 也在该理想中。然后使用

\[
\begin{aligned}
d\in(1+i)&\iff A+B\equiv0\pmod2,\\
d\in(p),\ p\equiv3\pmod4
   &\iff A\equiv B\equiv0\pmod p,\\
d\in(p,i-r),\ p\equiv1\pmod4
   &\iff A+Br\equiv0\pmod p,\quad r^2\equiv-1\pmod p.
\end{aligned}
\tag{10}
\]

最后一行只需枚举 \(0\le r<p\)。这些等价式分别来自相应商域中的
i 的像；(4) 保证没有遗漏分支。试除和剩余类枚举均有明确有限范围，
所以 (8) 在给定 d 上有一个理论上可终止的整数过程。

本轮没有执行该过程或评价效率，也没有从任意输入矩阵中认证本原
代表、求出 owner 最小代表或完成 owner 判等。若输入是真幂而未先
取本原根，其判别式不能冒充 (1) 的本原 owner 数据。

## 4. 概率等变可以实现，但每次抽取不能消除不动点障碍

允许输出有限 S(x) 上的概率分布 \(\mu_x\)。概率版 E+D 为

\[
\mu_x(\mathfrak p)\ge0,\qquad
\sum_{\mathfrak p\in S(x)}\mu_x(\mathfrak p)=1,\qquad
\mu_{\sigma x}(\overline{\mathfrak p})=\mu_x(\mathfrak p).
\tag{11}
\]

在 A_*(x) 上均匀分布、其余理想赋零，立即给出全 X 上满足 (11)
的规则。这只是数学概率核；没有运行随机抽样或把输出注册为机制。

**命题 2。** 若 x 是共轭不动且 S(x) 无不动素理想，则任何满足
(11) 的分布都有

\[
\max_{\mathfrak p}\mu_x(\mathfrak p)\le\frac12,\qquad
H_2(\mu_x)\ge1.
\tag{12}
\]

这里 \(H_2(\mu)=-\sum\mu\log_2\mu\)，约定 \(0\log_2 0=0\)。

证明。将 S(x) 写成互不相交的共轭对
\(\{\mathfrak p_j,\overline{\mathfrak p_j}\}\)。等变性在不动 x 上要求
每对两边质量相同。令该对总质量为 \(w_j\)，则每边为 \(w_j/2\)，
且 \(\sum_jw_j=1\)。因此每个原子质量至多 1/2，并且

\[
H_2(\mu_x)
=-\sum_j2\,\frac{w_j}{2}\log_2\frac{w_j}{2}
=1-\sum_jw_j\log_2w_j
=1+H_2(w)\ge1.
\tag{13}
\]

等号成立当且仅当全部质量集中于一个共轭对，两边各为 1/2。
均匀分布于 A_*(x) 达到此下界。□

同一个事实还给出与任何确定性输出的定量距离。将分布延拓为全部
Gaussian 素理想上的零质量，令 \(\delta_{\mathfrak p}\) 为单点分布，
则有限支持概率的总变差距离为

\[
\|\mu_x-\delta_{\mathfrak p}\|_{\rm TV}
=1-\mu_x(\mathfrak p)\ge\frac12.
\tag{14}
\]

公式由该点的质量差与其余点的总质量各为 \(1-\mu_x(\mathfrak p)\)
直接得到。故这里不存在“任意接近确定性”的等变概率规则。

概率分布可以共轭等变，并不意味着固定一次随机结果后仍得到单值
E。对不动坏 owner，任何实现值都是一个非不动素理想，仍违反
\(M(x)=\overline{M(x)}\)。若同时改变随机种子并让其携带共轭作用，
那已经扩大了输入对象，不是原来的 X 上的单值规则。

## 5. 真实本原族中的手算边界

使用[已证完整群本原性][family]的
\(A_n=\left(\begin{smallmatrix}1&3\\3n&1+9n\end{smallmatrix}\right)\)，
记 owner 为 x_n。本轮仅引用该证明，不重新执行根检查。

当 n=1 时，\(d=13=(3+2i)(3-2i)\)，两个不同因子的理想范数均为
13，故

\[
A_*(x_1)=\{(3+2i),(3-2i)\}.
\tag{15}
\]

当 n=5 时，\(d=5(4+45)=245=5\cdot7^2\)。
5 给范数 5 的两个分裂理想 \((2+i),(2-i)\)，而 (7) 是范数 49
的不动素理想。因此 A_min 取前一对，但
\(A_*(x_5)=\{(7)\}\)。这验证了“最小范数层”和“最小基数”并非同一事。

对前轮坏族 \(x_{25^k}\)，\(k\ge1\)，d 是奇数、含有因子 5，
且没有 \(3\bmod4\) 素因子。由 (4)，小于 5 的素理想范数只有 2，
而 d 为奇数排除了这一项；5 的两个理想确实都含 d。因此

\[
A_*(x_{25^k})=\{(2+i),(2-i)\}\qquad(k\ge1).
\tag{16}
\]

所以同一个达到最小基数／最小熵的规则在无限多个不同 owner 上
给出完全相同的集合和概率分布。这里的一比特熵描述抽样本身的
不确定性，不是一比特 owner 信息：无论事先在这个子族上采用什么
概率权重，条件输出分布恒定，输出与 owner 独立。

这也直接限制结论强度：对称性可行、算术可求值、标签区分能力及
动力学信息是四个不同问题，前两者不能替代后两者。

## 6. 与原单值机制的关系及实际动作

本篇证明了三个不同范围的结论：

- 全 X 上存在至多两个素理想的等变集合规则，且给出了数据局部
  规则的逐点最小基数；
- 在不动坏 owner 上，两元素和一比特条件熵都是不可降低的下界；
- 放宽输出类型不会自动提高标签信息量，也不能反推出原单值 E+D。

全 X 上原单值 E+D 的不可能性仍由坏 owner 保持。没有把 (3) 或
(11) 替换为冻结值域，没有登记随机机制、筛掉坏 owner、修改
canonical bytes，或声称 Gate M／Q、Route 与正式完整性已通过。

ARS 的有界 argument-builder 流程用于区分继承对象、输出类型改变、
owner 与判别式数据的对合、可计算性与信息量。新增整数程序的终止性、
集合下界、熵恒等式及总变差公式均有纸面证明；不依赖未读外部来源，
也没有作新颖性检索或宣称这些一般对称性原理是新定理。

实际只新增本笔记，由主线程统一追加总记录。没有运行素数、矩阵、
owner 或随机程序，没有实验、fixture、历史 writer 或论文构建。
旧笔记、现稿、书目、冻结协议、输入锁、正式回执、失败记录及
FAIL / BLOCK 保持；D06 Recovery 3、Route 与 Stage 5／6 边界不变。

[criterion]: internal_fixed_prime_classification_and_selector_criterion_20260908.md
[family]: internal_infinite_primitive_split_obstruction_family_20260908.md
