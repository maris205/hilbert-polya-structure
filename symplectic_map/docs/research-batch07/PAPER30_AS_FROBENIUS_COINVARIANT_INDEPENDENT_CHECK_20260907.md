# Paper30 Artin–Schreier／Frobenius coinvariant 独立数学核查

日期：2026-09-07。类型：全新有界独立证明审查。

## Claim

唯一作者输入为本目录的
`PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md`，336 行。
SHA256：`05aba58b468f3c4a5a9201f032200adb96e5acc6216ca65920066d2b2b3fe4d6`。

已完整读取该文件。本审查员未参与其作者工作；本次未读取旧 AS 模板、
未重审此前 kicked-chain 工作，亦未运行实验或有限次数枚举。
以下只判定输入实际声明的数学结果，不评价新意、容量或候选资格。

核查的命题是：任意特征的二进制 orbit basis 与 twisted obstruction；
Artin–Schreier 特征空间和常数商 coinvariant 中 Frobenius 固定空间的桥接；
strong-balanced 顶层次数增长及唯一奇反射例外的必要条件；
两个 single-letter 公式；以及特征 $3$ 特例的完整 Frobenius 核分类。

## Status

**已声明的上述定理、引理与公式：`PROVABLE AS STATED / PROVED`。**

未发现需要改公式、补科学假设或弱化这些命题的数学缺口。
本报告显式展开普通次数三角性、移位碰撞的互素条件和半线性边界，
这些均来自输入原有假设，不是另加限制。

**全部 mixed 支撑的 Frobenius 固定空间及 $Q^{\sigma=\lambda}$ 分类：
`NOT CURRENTLY JUSTIFIED / OPEN`，与作者边界一致。**

核分类不改变后一状态。本报告不是候选 `PASS`，不产生新项目或篇数登记。
`route_applicability: NOT_APPLICABLE`。

## Assumptions and Notation

沿用原命题：$K$ 代数闭，$\operatorname{char}K=p>2$，
$A=K[x,y]$，$F(x,y)=(x^2+c-y,x)$，$\sigma=F^*$，
$c\in K$，$\lambda\in\mathbb F_p^*$，$L=\sigma-\lambda$。
记 $\wp(u)=u^p-u$、$Q=A/\wp(A)$、
$\overline C_\lambda=A/(LA+K)$，以及
$\phi\langle h\rangle=\langle h^p\rangle$。

$Q$ 是加法群的商和 $\mathbb F_p$-向量空间，不是一般的 $K$-向量空间。
$\overline C_\lambda$ 是 $K$-向量空间，$\phi$ 为加法的 $p$-半线性映射。
引入轨道坐标 $X_i$ 和二进制 word 的约定、指数编码 $(a,b)$、
轨道次数 $d(O)$ 与 $\delta$ 均与作者输入一致。
非空 word 的轨道次数至少为 $1$。

## Proof Strategy and Dependency Map

1. 终止且合流的平方重写给出任意特征 orbit basis。
2. 各无限移位轨道的有限支撑差分方程给出 coinvariant 基与常数判据。
3. 上一步结合 $\wp(K)=K$ 和 $\lambda^p=\lambda$ 证明桥接双射。
4. 首项二进制编码、离散凸性与缩放后的轨道分离证明顶层必要条件。
5. 直接有限重写检查两个 single-letter 公式。
6. 独立使用不变量常数性、Wronskian 和 $\ker d=A^3$ 完成特征 $3$ 核分类。

## Proof

### 1. 特征 $p$ orbit basis 与 twisted obstruction — `PROVED`

规则 $Z_i^2\mapsto Z_{i-1}+Z_{i+1}-c$ 的每个分支都严格降低总因子次数，
每次替换至多产生三项。因此从有限多项式出发的约化树有限；
无限指标集不引入无限约化链。不同平方因子互素，两个不同位置的
局部选择都可再到达作者给出的同一个乘积表达式。
即使位置相邻，也可先替换仍保留的另一个原平方因子，再处理新产生的平方。
由总因子次数归纳，完全约化唯一。

normal form 消去关系理想，并固定二进制单项式，故这些单项式在商中
张成且线性无关。递推向两个方向消去全部其他变量，商环与
$K[Z_0,Z_{-1}]$ 互为显式逆同构。这一步没有除以可能在特征 $p$ 中为零的整数。

$\sigma X_i=X_{i+1}$，非空有限 word 不可能有非零平移周期。
对任一非空轨道，$Ls\in K$ 给出
$u_{r-1}-\lambda u_r=0$；有限支撑迫使全部 $u_r=0$。
所以 $Ls\in K\Rightarrow s\in K$，特别多项式 $\sigma$-不变量只有常数。

obstruction 为 $\sum_r\lambda^r c_r$。直接代入
$$
u_r=-\lambda^{-r-1}\sum_{s\le r}\lambda^s c_s
$$
得到 $u_{r-1}-\lambda u_r=c_r$。obstruction 为零时左右尾部都为零，
故这个原函数确有有限支撑。因而每个非空轨道恰贡献一个 $K$-维方向，
并有 $\langle\sigma^rM\rangle=\lambda^r\langle M\rangle$。
当 $\lambda=1$ 时必须额外商去常数；当 $\lambda\ne1$ 时
$L$ 已在常数上可逆，原稿对此区分正确。

### 2. 桥接的下降、常数、双射与半线性 — `PROVED`

因为 $\lambda^p=\lambda$，
$$
(Lu+k)^p=L(u^p)+k^p,
\qquad L\wp(u)=\wp(Lu).
$$
第一式使 $\phi$ 在 $\overline C_\lambda$ 上定义良好；
它满足 $\phi(av)=a^p\phi(v)$，而不是一般的 $K$-线性。

对 $[g]\in Q^{\sigma=\lambda}$，方程 $Lg=\wp(h)$ 定义
$\Psi[g]=\langle h\rangle$。另选 $h$ 的差属于
$\ker\wp=\mathbb F_p\subset K$；另选 $g+\wp(u)$ 时，可选
$h+Lu$。故该映射不依赖任一代表，且像满足 $\phi v=v$。

若像为零，则 $h=Lu+a$，于是
$L(g-\wp(u))=\wp(a)\in K$。第 1 步给出 $g-\wp(u)\in K$，
再由代数闭性提供的 $K=\wp(K)$，得到 $[g]=0$。
该证明没有要求 $\lambda\ne1$，也没有把非零常数错误当成零多项式。

反之，固定元满足 $\wp(h)=Lg+a$。选 $b\in K$ 使
$\wp(b)=-a$，即有 $\wp(h+b)=Lg$，给出所需原像。
因此作者式 (1) 是自然的 $\mathbb F_p$-线性同构；并未声称一个不存在的
$K$-线性固定空间同构。

### 3. 普通次数与最小代表的离散凸性 — `PROVED`

$X_i$ 在非负射线的首项为 $x^{2^i}$，在负射线的首项为
$y^{2^{-i-1}}$，均为首一单项式。不同二进制 word 编码不同 $(a,b)$，
因此普通最高齐次项不同。有限 word 线性组合的次数恰为其中最大的
$a+b$；最高层不会跨 word 消去。

这也给出后续必要的三角性：次数至多 $D$ 的多项式，其唯一 orbit-basis
normal form 不可能出现普通次数大于 $D$ 的 word，否则最大层的不同
首项无法消去。次数恰为 $D$ 的 source 的 $p$ 次幂，唯一普通次数
$pD$ 的 word 是编码 $(pa,pb)$ 的 word，系数为 source 系数的 $p$ 次幂。
其余项的普通次数严格小于 $pD$。

直接移位得到作者式 (4)。每个被占据指标的次数贡献序列为
$\ldots,4,2,1,1,2,4,\ldots$ 的平移，该序列的一阶差分单调不减。
有限和仍离散凸。因此某位置是全局最小值，当且仅当左右邻点的次数
均不低于它；代入式 (4) 正好是
$2a\ge b-(b\bmod2)$、$2b\ge a-(a\bmod2)$。
这是全局最小判据，不只是局部必要条件。

### 4. strong-balanced 顶层：所有来源与 orbit-shift collision — `PROVED`

对 $v$ 每轨道取一个最小代表，得到次数 $D=\delta(v)$ 的有限多项式 $h$。
若一个最高 source 满足 $2a\ge b,2b\ge a$，则 $(pa,pb)$ 也满足这些不等式，
故其目标轨道的最小次数就是 $pD$。
这首先排除所有普通次数小于 $pD$ 的贡献，包括同一 source 的其他项、
其他最高 source 的低项，以及全部较低 source 的所有项。

剩下唯一风险是不同最高 source 的最高 word 进入同一目标轨道。
假设 $(pa,pb)$ 右移 $r\ge0$ 后等于另一对被 $p$ 整除的指数，其公式为
$$
\left(2^rpa+t,\frac{pb-t}{2^r}\right),
\qquad t=pb\bmod2^r.
$$
第一分量迫使 $t=pu$。由 $0\le t<2^r$ 得 $0\le u<2^r$。
又 $2^r\mid p(b-u)$，这里确实使用原假设 $p>2$，使
$\gcd(p,2^r)=1$，从而 $2^r\mid b-u$。
于是 $u=b\bmod2^r$。将整个式子除以 $p$，所得正是原指数对
$(a,b)$ 的同一 $r$ 格移位。两个 source 原本属于同一轨道，
与每轨道仅取一个代表矛盾。左移情形交换两 source 后使用这一论证。

所以目标轨道只获得一个非零贡献；其 twisted 权重是某个非零
$\lambda$ 幂，也不会使该贡献变零。另一方面，$h^p$ 的所有 word
普通次数至多 $pD$，轨道最小次数也至多 $pD$。
因此 $\phi v\ne0$ 且 $\delta(\phi v)=pD>D$，命题 3 的量词完整成立。

### 5. $D=3n+1$ 的奇反射例外及唯一性 — `PROVED`

最小代表满足上一节的含奇偶修正不等式，却不满足 strong-balanced 时，
整数性只允许 $b=2a+1$ 或 $a=2b+1$。
前者右移一次即为后者；两者属于同一轨道。
若 $a=n,b=2n+1$，最低负位为中心 $1$，其余负位逐一复制正位，
恰形成关于中心的反射 word。普通次数为 $3n+1$。
二进制编码的唯一性保证每个这样的 $D$ 只有一个可能例外轨道。

因此非零固定元的最高支撑只能落在这一例外轨道，且
$D\equiv1\pmod3$。它并不限制更低层轨道，亦不提供 $D$ 的上界。
原稿没有把这个必要条件误当作充分条件或有限维分类。

### 6. $p=3$ 与 $p=5$ single-letter 公式 — `PROVED`

$p=3$ 时，由 $X_0^3=X_0(X_{-1}+X_1-c)$ 及移位权重，直接得到
$$
\phi(u)=(1+\lambda^{-1})E-cu.
$$
当 $\lambda=-1$ 时，$\phi(au)=-ca^3u$；固定元方程为 $-ca^3=a$。
$c=0$ 时仅零解，$c\ne0$ 时零解及两个相反的非零解恰好齐全。
又 $(\sigma+1)(xy)=x^3+cx$，所以在 $ca^3=-a$ 时
$(\sigma+1)(a^3xy)=\wp(ax)$。桥接确实将 $[a^3xy]$ 映到 $au$，
且由桥接单射和 $u\ne0$ 保证这些类非零。

$p=5$ 时将 $X_0(X_{-1}+X_1-c)^2$ 展开，并先用
$X_{-1}^2=X_{-2}+X_0-c$、$X_1^2=X_0+X_2-c$，得到
$$
X_0X_{-2}+X_0X_2+2X_0^2+(c^2-2c)X_0
 +2X_{-1}X_0X_1-2c(X_{-1}X_0+X_0X_1).
$$
再替换 $X_0^2$ 并商去常数，正好是作者式 (10) 的全部系数。
其中 $D_2,E$ 的支撑间距不同，$T$ 的支撑基数又不同，三个轨道互异。
$T$ 系数 $2\lambda^{-1}$ 非零，因此 $Ku$ 中没有非零固定元。
这只排除该直线，不能排除高层 source 与其共同抵消。

### 7. 特征 $3$、$c=0$ 的一形式 Wronskian — `PROVED`

将 $\sigma$ 扩展为微分形式上的拉回。写 $\alpha=a\,dx+b\,dy$，
利用 $d(x^2-y)=-x\,dx-dy$，条件 $\sigma^*\alpha=-\alpha$ 等价于
$b=\sigma a$、$\sigma^2a=x\sigma a-a$，符号与特征 $3$ 运算正确。

对 $W=ax-y\sigma a$，直接拉回得到 $\sigma W=W$，因此第 1 步保证
$W$ 是常数。令 $y=0$ 得 $xa(x,0)=W$，再令 $x=0$ 得 $W=0$。
故 $a(x,0)=0$，即 $y\mid a$。写 $a=yq$ 后，
$W=xy(q-\sigma q)=0$。整环性质和不变量常数性给出 $q\in K$。
于是全部且仅有 $\alpha=q\,d(xy)$；反向可由
$\sigma(xy)=x^3-xy$ 直接微分核对。

### 8. 完整 Frobenius 核恰为 $K\langle x\rangle$ — `PROVED`

若 $\phi\langle h\rangle=0$，则 $h^3=(\sigma+1)g+k$。
微分后得到 $\sigma^*(dg)=-dg$，上一节给出 $dg=q\,d(xy)$。
特征 $3$ 中两偏导同时为零，等价于每个出现的单项式的两个指数
均被 $3$ 整除。$K$ 完美保证所有系数有三次根，因此
$g=qxy+v^3$。

由于 $(\sigma+1)(xy)=x^3$，
$$
h^3=qx^3+(\sigma v+v)^3+k.
$$
Frobenius 在整环中单射，而 $q,k$ 的三次根存在且唯一，故
$$
h=q^{1/3}x+(\sigma+1)v+k^{1/3}.
$$
取商得 $\langle h\rangle\in K\langle x\rangle$。
反向包含来自 $x^3=(\sigma+1)(xy)$；$\langle x\rangle\ne0$
由第 1 步的单字轨道 obstruction 保证。所以核恰好是一条 $K$-线，
不是 $K[x]$，亦不只是某个低次数截断下的核。

半线性映射的核确为 $K$-线性子空间；固定元则一般仅构成
$\mathbb F_p$-线性空间。该核上 $\phi=0$，所以与
$\ker(\phi-1)$ 的交恰为零，但这不排除核外的固定元。

## Corrections or Missing Assumptions

无需要更正的实际公式或定理级缺口。
移位碰撞中除去 $p$ 所用的互素性、normal-form 普通次数三角性及
完美域的多项式三次根，在原假设与原论证下均可完整展开。
没有借用特征零结论来替代特征 $p$ 证明。

## Open Risks and Boundaries

- 命题 3 不控制奇反射例外的完整 Frobenius orbit obstruction，
  也不控制这些例外与较低 source 之间的消去。
- 例外次数 $D=3n+1$ 无限多；必要条件不意味着有限维异常空间。
- $p\ge5$ 和 $p=3,c=0$ 的全 mixed 固定空间仍未分类。
- $p=3,c\ne0,\lambda=-1$ 的已知非零特征类是否穷尽仍未证明。
- 已分类 $\ker\phi$ 不等于已分类 $\ker(\phi-1)$，
  亦未证明商去核后的严格次数增长。

这些开放项是作者明确保留的边界，不是已经证明命题的反例，
但足以阻止把本文件宣称为最初 full mixed 目标的完成证明。

## 最终数学裁决与执行记录

按已完整读取的 `proof-writer` 要求，将实际定理与未解决目标分开。
桥接、orbit basis、strong-balanced 必要条件、single-letter 公式及
特征 $3$ 完整核分类均为 **`PROVED / PROVABLE AS STATED`**；
**full mixed 固定空间分类仍为 `OPEN / NOT CURRENTLY JUSTIFIED`**。

仅新增本独立报告；作者输入未修改。未作实验、网页查新、评分、篇幅判断或候选裁决。
