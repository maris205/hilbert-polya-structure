# Proper-Residue GCD Descent: Proof Dossier

日期：2026-08-30。范围：proof spike only；未分配论文编号，未写论文。

## Claim

从整数 $n$ 出发，若当前状态 $m>1$，从 ${1,\ldots,m-1}$ 均匀选取 $A$，并把状态更新为 $\gcd(m,A)$；状态 $1$ 吸收。令 $T_n$ 为首次到达 $1$ 的步数，令

$$
G_n(z):=\mathbb E[z^{T_n}].
$$

本 dossier 证明以下结论。

1. 对每个真因子 $d\mid n$，一步转移核为
   $$
   P(n,d)=\frac{\varphi(n/d)}{n-1}.
   $$
2. 一般 $n$ 的完整吸收时间分布等于对所有严格因子历史的显式加权和，并满足有限 divisor-PGF 递归。
3. 若 $n>1$，则 $G_n$ 的非零次数恰为 $1,\ldots,\Omega(n)$。特别地，$\deg G_n=\Omega(n)$；其首项和最高项都有显式公式。
4. 对素数 $p$ 和整数 $k\geq1$，
   $$
   G_{p^k}(z)
   =z\prod_{j=1}^{k-1}\frac{z+c_{p,j}}{1+c_{p,j}},
   \qquad
   c_{p,j}:=p\frac{p^j-1}{p-1}=p+\cdots+p^j.
   $$
   等价地，$T_{p^k}$ 在分布上是常数 $1$ 加一列独立 Bernoulli 变量之和。
5. 由该分解得到精确均值、方差、端点原子、最大时长的 sharp asymptotic，以及 $k\to\infty$ 的极限分布和统一尾界。

## Status

**PROVABLE AS STATED; POST-GATE VALUE REPAIR ADDED BELOW.**

所有上述陈述均在下文证明。没有把有限计算、数值拟合或 bounded literature non-hit 当作证明。

## Assumptions

- $n$、$m$、$k$ 为正整数，$p$ 为素数。
- $\varphi$ 是 Euler totient function。
- $\Omega(n)$ 是带重数的素因子个数；约定 $\Omega(1)=0$。
- 所有随机选择都只在当前状态的 proper residues 中进行；特别地，不能把采样集合换成 $\{1,\ldots,m\}$。

## Notation

- 写 $d\parallelneqq n$ 表示 $d\mid n$ 且 $d<n$。
- 对 $n>1$，严格因子历史是
  $$
  \gamma=(n_0,n_1,\ldots,n_t),
  \qquad n_0=n>n_1>\cdots>n_t=1,
  \qquad n_i\mid n_{i-1}.
  $$
  长度为 $|\gamma|=t$。
- $[z^t]F(z)$ 表示多项式 $F$ 的 $z^t$ 系数。
- $\mathcal P(n)$ 表示 $n$ 的带重数素因子多重集；$\operatorname{Ord}(\mathcal P(n))$ 表示该多重集的不同线性排列。

## Proof Strategy

先按 $\gcd$ 纤维划分 proper residues，得到精确转移核。严格因子下降使状态图成为有限 DAG，因此逐路径相乘即可得到一般历史公式与 PGF 递归。$\Omega$ 每步至少下降 $1$，控制最高次数；最大长度历史恰好逐次除去一个素因子。

在素幂通道上，将相邻两个 divisor recurrences 相减，得到一阶乘法递推。这给出 PGF 的线性因子分解，进而得到 Bernoulli 表示、矩与极限律。

## Dependency Map

1. Lemma 1 的 residue-fiber count 给出转移核和核的归一化。
2. Theorem 2 只依赖 Markov 性、Lemma 1 和严格下降。
3. Proposition 3 依赖 $d\parallelneqq n\Rightarrow\Omega(d)\leq\Omega(n)-1$，以及最大历史中每个商必须为素数。
4. Theorem 4 依赖 Theorem 2 的素幂 specialization 和恒等式 $p\varphi(p^r)=\varphi(p^{r+1})$。
5. Corollaries 5--7 只依赖 Theorem 4 的有限 Bernoulli 分解和可求和界 $q_{p,j}<p^{-j}$。

## Proof

### Lemma 1. Exact kernel

对 $n>1$ 和 $d\parallelneqq n$，

$$
\#\{a\in\{1,\ldots,n-1\}:\gcd(n,a)=d\}=\varphi(n/d).
$$

所以

$$
P(n,d)=\frac{\varphi(n/d)}{n-1}.
$$

#### Proof

令 $q=n/d>1$。条件 $\gcd(n,a)=d$ 强制 $a=db$，并且

$$
1\leq b\leq q-1,
\qquad
\gcd(q,b)=1.
$$

反过来，每个满足这两个条件的 $b$ 都给出唯一的允许 residue $a=db<n$，且 $\gcd(n,a)=d$。这样的 $b$ 恰有 $\varphi(q)=\varphi(n/d)$ 个。

不同 $d\parallelneqq n$ 的纤维互不相交，并覆盖全部 $n-1$ 个 proper residues，故

$$
\sum_{d\parallelneqq n}\varphi(n/d)=n-1.
$$

因此所给 $P(n,d)$ 非负且总和为 $1$。又因 $d<n$，每一步严格下降，所以过程必在有限步内到达 $1$。$\square$

### Theorem 2. General history formula and PGF recursion

设 $\Gamma_t(n)$ 是从 $n$ 到 $1$ 的全部长度 $t$ 严格因子历史。对

$$
\gamma=(n_0,n_1,\ldots,n_t)\in\Gamma_t(n),
$$

定义

$$
w(\gamma)
:=\prod_{i=1}^{t}
\frac{\varphi(n_{i-1}/n_i)}{n_{i-1}-1}.
$$

则

$$
\Pr(T_n=t)=\sum_{\gamma\in\Gamma_t(n)}w(\gamma),
$$

并且

$$
G_1(z)=1,
\qquad
G_n(z)=\frac{z}{n-1}
\sum_{d\parallelneqq n}\varphi(n/d)G_d(z)
\quad(n>1).
$$

此外，固定一条 divisor history $\gamma$ 后，能够产生该 divisor history 的字面 residue-choice histories 数为

$$
F(\gamma)=\prod_{i=1}^{t}\varphi(n_{i-1}/n_i).
$$

#### Proof

由 Lemma 1 和 Markov 性，沿固定历史 $\gamma$ 依次发生全部转移的概率是各边概率之积，即 $w(\gamma)$。不同状态历史对应互斥事件；长度 $t$ 时吸收的事件是这些事件的并，因此对 $\Gamma_t(n)$ 求和得到 $\Pr(T_n=t)$。

固定状态历史时，第 $i$ 步有 $\varphi(n_{i-1}/n_i)$ 个 residue 产生指定的下一状态。各步的选择纤维按笛卡尔积组合，故字面历史纤维大小是这些数的乘积 $F(\gamma)$。

最后，对第一步落点 $d\parallelneqq n$ 作全概率分解。第一步贡献一个 $z$，之后的条件 PGF 是 $G_d(z)$，所以

$$
G_n(z)
=z\sum_{d\parallelneqq n}P(n,d)G_d(z)
=\frac{z}{n-1}\sum_{d\parallelneqq n}\varphi(n/d)G_d(z).
$$

严格下降保证所有求和都是有限的。$\square$

### Proposition 3. Exact support, degree, first and last coefficients

令 $n>1$ 且 $r=\Omega(n)$。则

$$
[z^t]G_n(z)>0
\quad\Longleftrightarrow\quad
1\leq t\leq r.
$$

因此 $\deg G_n=r$。最低非零系数为

$$
[z]G_n(z)=\frac{\varphi(n)}{n-1}.
$$

最高系数满足递归

$$
[z^r]G_n(z)
=\frac1{n-1}\sum_{p\mid n}(p-1)
\,[z^{r-1}]G_{n/p}(z),
$$

其中求和遍历 $n$ 的不同素因子。显式地，若

$$
\pi=(p_1,\ldots,p_r)\in\operatorname{Ord}(\mathcal P(n)),
$$

则

$$
[z^r]G_n(z)
=\sum_{\pi\in\operatorname{Ord}(\mathcal P(n))}
\prod_{i=1}^{r}
\frac{p_i-1}
{\displaystyle n/(p_1\cdots p_{i-1})-1},
$$

其中空前缀积取 $1$。

#### Proof

如果 $d\parallelneqq m$，则 $m/d\geq2$，所以

$$
\Omega(d)=\Omega(m)-\Omega(m/d)\leq\Omega(m)-1.
$$

故从 $n$ 出发的每一步都使 $\Omega$ 至少下降 $1$；从 $r$ 降到 $0$ 最多需要 $r$ 步。这证明 $[z^t]G_n=0$ 对所有 $t>r$ 成立。

反过来，固定 $1\leq t\leq r$。从 $\mathcal P(n)$ 中取任意 $t-1$ 个素因子（计重数），令其乘积为 $d$；当 $t=1$ 时令 $d=1$。先从 $n$ 跳到 $d$，再逐次从 $d$ 除去一个素因子。所得历史长度恰为 $t$。Lemma 1 表明历史中每条边的概率均严格为正，因此 $[z^t]G_n>0$。

长度 $1$ 的吸收只能是 $n\to1$。Lemma 1 给出其概率 $\varphi(n)/(n-1)$。

长度达到最大值 $r$ 时，每步 $\Omega$ 必须恰降 $1$，故每个商 $n_{i-1}/n_i$ 必须是素数。这样的历史与 $\mathcal P(n)$ 的不同排列一一对应。若第 $i$ 个被除去的素数是 $p_i$，该边的概率为

$$
\frac{\varphi(p_i)}{n/(p_1\cdots p_{i-1})-1}
=\frac{p_i-1}{n/(p_1\cdots p_{i-1})-1}.
$$

对每条历史取积并对不同排列求和得到显式最高系数。按第一步被除去的不同素因子 $p$ 分组，则得到所述最高系数递归。$\square$

### Theorem 4. Prime-power product and Bernoulli law

令 $p$ 为素数，$k\geq1$，并令

$$
c_{p,j}:=p\frac{p^j-1}{p-1}.
$$

则

$$
G_{p^k}(z)
=z\prod_{j=1}^{k-1}\frac{z+c_{p,j}}{1+c_{p,j}}.
$$

若 $B_{p,1},B_{p,2},\ldots$ 相互独立且

$$
\Pr(B_{p,j}=1)=q_{p,j}:=\frac1{1+c_{p,j}}
=\frac{p-1}{p^{j+1}-1},
$$

则

$$
T_{p^k}\overset d=
1+\sum_{j=1}^{k-1}B_{p,j}.
$$

#### Proof

写 $F_k(z)=G_{p^k}(z)$，并令 $F_0(z)=G_1(z)=1$。Theorem 2 给出

$$
\frac{p^k-1}{z}F_k(z)
=\sum_{i=0}^{k-1}\varphi(p^{k-i})F_i(z).
\tag{1}
$$

对 $k-1$ 的对应恒等式乘以 $p$：

$$
p\frac{p^{k-1}-1}{z}F_{k-1}(z)
=\sum_{i=0}^{k-2}p\varphi(p^{k-1-i})F_i(z).
\tag{2}
$$

对每个 $i\leq k-2$，指数 $k-1-i\geq1$，而

$$
p\varphi(p^{k-1-i})=\varphi(p^{k-i}).
$$

因此从 (1) 减去 (2) 后，右侧只剩 $i=k-1$ 的项 $\varphi(p)F_{k-1}=(p-1)F_{k-1}$。乘以 $z$ 并整理得到

$$
(p^k-1)F_k(z)
=\left[p(p^{k-1}-1)+(p-1)z\right]F_{k-1}(z).
$$

因为

$$
p(p^{k-1}-1)=(p-1)c_{p,k-1},
\qquad
p^k-1=(p-1)(1+c_{p,k-1}),
$$

所以

$$
F_k(z)=F_{k-1}(z)
\frac{z+c_{p,k-1}}{1+c_{p,k-1}}.
$$

初值 $F_1(z)=z$，对 $k$ 迭代即得乘积公式。

每个线性因子可写为

$$
\frac{z+c_{p,j}}{1+c_{p,j}}
=(1-q_{p,j})+q_{p,j}z,
$$

这是 Bernoulli$(q_{p,j})$ 的 PGF。独立随机变量之和的 PGF 是各 PGF 的乘积，故得到分布恒等式。$\square$

### Corollary 5. Exact mean and variance

对每个素数 $p$ 和 $k\geq1$，

$$
\mathbb E[T_{p^k}]
=1+\sum_{j=1}^{k-1}\frac1{1+c_{p,j}}
=1+\sum_{j=1}^{k-1}\frac{p-1}{p^{j+1}-1},
$$

以及

$$
\operatorname{Var}(T_{p^k})
=\sum_{j=1}^{k-1}\frac{c_{p,j}}{(1+c_{p,j})^2}
=\sum_{j=1}^{k-1}q_{p,j}(1-q_{p,j}).
$$

#### Proof

Theorem 4 把 $T_{p^k}$ 表为独立 Bernoulli 和。期望可加；独立变量的方差可加；Bernoulli$(q)$ 的方差为 $q(1-q)$。代入 $q_{p,j}=1/(1+c_{p,j})$ 即得。$\square$

### Corollary 6. Sharp endpoint atoms and their limits

对 $k\geq1$，最短时间和最长时间的原子分别为

$$
\Pr(T_{p^k}=1)
=\frac{p^{k-1}(p-1)}{p^k-1},
\tag{3}
$$

和

$$
\Pr(T_{p^k}=k)
=\prod_{r=2}^{k}\frac{p-1}{p^r-1}.
\tag{4}
$$

特别地，(3) 有精确误差式

$$
\Pr(T_{p^k}=1)-\frac{p-1}{p}
=\frac{p-1}{p(p^k-1)},
$$

所以

$$
\Pr(T_{p^k}=1)\downarrow\frac{p-1}{p}.
$$

再令

$$
C_p:=\prod_{r=2}^{\infty}(1-p^{-r})^{-1}<\infty.
$$

则最长时间原子具有 sharp asymptotic

$$
\Pr(T_{p^k}=k)
\sim C_p (p-1)^{k-1}
p^{1-k(k+1)/2}.
$$

#### Proof

公式 (3) 也就是 Proposition 3 的首项公式，因为

$$
\varphi(p^k)=p^{k-1}(p-1).
$$

也可由 Bernoulli 表示要求全部 $B_{p,j}=0$ 得到；乘积

$$
\prod_{j=1}^{k-1}(1-q_{p,j})
=\prod_{j=1}^{k-1}\frac{p(p^j-1)}{p^{j+1}-1}
$$

逐项 telescopes 为 (3)。从 (3) 直接通分得到精确误差式，误差严格为正并随 $k$ 下降至 $0$。

最长时间要求全部 $B_{p,j}=1$，因此

$$
\Pr(T_{p^k}=k)
=\prod_{j=1}^{k-1}\frac{p-1}{p^{j+1}-1},
$$

这就是 (4)。把每个分母写成 $p^r(1-p^{-r})$，得到精确恒等式

$$
\Pr(T_{p^k}=k)
=(p-1)^{k-1}p^{1-k(k+1)/2}
\prod_{r=2}^{k}(1-p^{-r})^{-1}.
$$

因为 $p^{-r}\leq1/4$，且对 $0\leq x\leq1/4$ 有

$$
0\leq-\log(1-x)\leq\frac{x}{1-x}\leq\frac43x,
$$

而 $\sum_{r\geq2}p^{-r}<\infty$，所以定义 $C_p$ 的对数级数绝对收敛，无限乘积收敛到有限正数。有限乘积趋于 $C_p$，从而得到所述渐近式。$\square$

### Corollary 7. Infinite-exponent limit law and a uniform tail ceiling

固定素数 $p$。存在几乎处处有限的整数值随机变量

$$
T_{p,\infty}:=1+\sum_{j=1}^{\infty}B_{p,j}
$$

使得在 Theorem 4 的共同 Bernoulli 耦合下

$$
T_{p^k}\longrightarrow T_{p,\infty}
\quad\text{almost surely and in distribution}.
$$

其 PGF、均值和方差为

$$
G_{p,\infty}(z)
=z\prod_{j=1}^{\infty}\bigl(1-q_{p,j}+q_{p,j}z\bigr),
\qquad |z|\leq1,
$$

$$
\mu_p:=\mathbb E[T_{p,\infty}]
=1+\sum_{j=1}^{\infty}\frac{p-1}{p^{j+1}-1}
<\frac{p}{p-1},
$$

$$
\operatorname{Var}(T_{p,\infty})
=\sum_{j=1}^{\infty}q_{p,j}(1-q_{p,j})<\infty.
$$

而且有定量截断界

$$
d_{\mathrm{TV}}\bigl(\mathcal L(T_{p^k}),
\mathcal L(T_{p,\infty})\bigr)
\leq\frac{p^{1-k}}{p-1},
$$

$$
0<\mu_p-\mathbb E[T_{p^k}]
<\frac{p^{1-k}}{p-1},
$$

以及对每个整数 $r\geq1$ 的统一尾界

$$
\Pr(T_{p,\infty}\geq r+1)
<\frac{1}{r!(p-1)^r}.
$$

#### Proof

先验证

$$
q_{p,j}=\frac{p-1}{p^{j+1}-1}<p^{-j},
$$

因为该不等式等价于 $p^j(p-1)<p^{j+1}-1$，而后二者之差为 $p^j-1>0$。因此

$$
\sum_{j=1}^{\infty}q_{p,j}
<\sum_{j=1}^{\infty}p^{-j}
=\frac1{p-1}<\infty.
$$

由第一 Borel--Cantelli lemma，只有有限多个事件 $\{B_{p,j}=1\}$ 发生，故 $T_{p,\infty}$ 几乎处处有限。其部分和单调趋于 $T_{p,\infty}$，并且第 $k$ 个部分和与 $T_{p^k}$ 同分布，所以得到几乎处处与分布收敛。

当 $|z|\leq1$ 时，

$$
\sum_j|q_{p,j}(z-1)|\leq2\sum_jq_{p,j}<\infty,
$$

故 PGF 无限乘积收敛。期望和方差级数的收敛由 $q_{p,j}<p^{-j}$ 支配；相应公式由独立 Bernoulli 和及单调/支配收敛得到。特别地，

$$
\mu_p<1+\sum_{j=1}^{\infty}p^{-j}
=\frac{p}{p-1}.
$$

在共同耦合下，有限和与无限和不同只可能是某个 $j\geq k$ 的 Bernoulli 成功。因此 union bound 给出

$$
\Pr(T_{p^k}\neq T_{p,\infty})
\leq\sum_{j=k}^{\infty}q_{p,j}
<\sum_{j=k}^{\infty}p^{-j}
=\frac{p^{1-k}}{p-1}.
$$

任一耦合的不相等概率控制 total variation distance，得到第一条截断界。期望差正好是 $\sum_{j\geq k}q_{p,j}$，所以得到第二条。

最后令 $S=\sum_{j\geq1}B_{p,j}=T_{p,\infty}-1$。在事件 $S\geq r$ 上，$\binom Sr\geq1$，故

$$
\Pr(S\geq r)
\leq\mathbb E\binom Sr
=\sum_{1\leq j_1<\cdots<j_r}
q_{p,j_1}\cdots q_{p,j_r}.
$$

展开 $(\sum_jq_{p,j})^r$ 时，每个互异指标的无序乘积出现 $r!$ 次，且其余项非负，因此

$$
\sum_{j_1<\cdots<j_r}q_{p,j_1}\cdots q_{p,j_r}
\leq\frac1{r!}\left(\sum_jq_{p,j}\right)^r
<\frac1{r!(p-1)^r}.
$$

这完成证明。$\square$

## Independent Mechanical Verification

独立 verifier 为 `verify_stoch_gcd_descent.py`；它不导入 scouting pilot，全部使用 `fractions.Fraction`，没有采样、浮点数或级数截断。其 canonical stdout 为 `verify_stoch_gcd_descent.out`。

验证范围：

- kernel、归一化、degree 与首项：$1\leq n\leq300$；
- literal-residue PGF 与 divisor PGF 独立一致，以及最高项 multiset-order 公式：$1\leq n\leq180$；
- 显式严格历史求和与 PGF 一致：$1\leq n\leq140$；
- 素幂乘积、均值、方差、两个端点原子及有限尾界：$p\leq31$、$1\leq k\leq10$。

规范运行共产生 **5,637 条 exact assertions**，结果为 PASS。

复现命令：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_stoch_gcd_descent.py
cmp verify_stoch_gcd_descent.out <(PYTHONDONTWRITEBYTECODE=1 python3 verify_stoch_gcd_descent.py)
```

## Zero-Credit Owner Boundary

### 2026 divisibility-chain framework

Boris Alexeev, Kevin Barreto, Yanyang Li, Jared Duker Lichtman, Liam Price, Jibran Iqbal Shah, Quanyu Tang, Terence Tao, *Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond*, arXiv:2605.00301 (2026), [official arXiv](https://arxiv.org/abs/2605.00301)。其 Definition 2.1 已定义一般 downward divisibility Markov chain，Examples 2.2--2.4 已给随机除素数、Mertens chain 和 von Mangoldt chain。

因此下列内容必须按 **zero credit** 处理：

- “在 divisibility poset 上构造 downward Markov chain”这一总体想法与术语；
- 严格下降链、absorbing state 以及链/流的一般框架；
- 仅仅把一个新 kernel 填入一般 Markov-chain 递归。

本 dossier 的可保留 residual 仅是：proper-residue gcd 的具体逐步 kernel、其吸收时间完整历史律，以及素幂吸收 PGF 的 Bernoulli 乘积、端点和极限推论。该 residual 仍须通过更广的正式 owner 检索。

### Minami one-step gcd distribution

Norihiko Minami, *On the random variable $\{1,\ldots,n\}^r\ni(k_1,\ldots,k_r)\mapsto\gcd(n,k_1\cdots k_r)$*, Journal of Number Theory 133 (2013), 2635--2647, DOI [10.1016/j.jnt.2013.01.012](https://doi.org/10.1016/j.jnt.2013.01.012)（[publisher page](https://www.sciencedirect.com/science/article/pii/S0022314X13000620)）。该文研究固定 $n$ 下均匀 $k_i\in\{1,\ldots,n\}$ 的一次性 gcd 随机变量、矩与卷积。

因此下列内容也按 **zero credit** 处理：

- gcd 纤维由 totient/divisor 数据控制；
- 一次 gcd 随机变量的矩或卷积视角；
- 单独陈述 $\varphi$ 计数或从它机械得到的一步分布。

本过程与 Minami 模型不可混同：这里每一步的采样空间随当前状态改变，并排除当前模数的零 residue；研究对象是首次吸收时间，而不是固定 $n$ 上若干独立样本乘积的一次 gcd。

截至 2026-08-30，对具体 proper-residue iterative kernel 和素幂 PGF 乘积的定向检索是 bounded non-hit；这不是 novelty certificate。

## Corrections or Missing Assumptions

- 本 proof package 不需要增加假设，也没有削弱上述 claim。
- 没有声称一般合数 $n$ 的 PGF 可乘法分解。proper-residue 的分母 $m-1$ 会耦合不同素因子，CRT 本身不足以推出独立性。
- Theorem 4 的 Bernoulli 表示是分布表示；共同 Bernoulli 空间提供跨 $k$ 的便利耦合，但没有声称它就是原始 residue choices 之间的自然逐样本耦合。

## Open Risks

- 数学证明已经闭合，主要剩余风险是直接 owner：旧文献可能已研究同一迭代 gcd kernel 或同一素幂乘积。
- 一般 $n$ 的历史公式是精确但机械的；若后续找不到第二个非素幂无限族，不应把 divisor-DP 本身包装成主要贡献。
- 若进入后续阶段，优先检查平方自由 $n$、固定两个素因子以及 leading-history coefficient 是否有真正的新闭式；若没有，应保持窄结论，而不是扩大叙事。

## Post-gate value repair: an all-integer zeta-mixture law

The hostile gate correctly observed that the prime-power factorization alone
is one chain computation inside an owned downward-divisibility framework.
The following second theorem is genuinely aggregate: it mixes **all** integer
starting states and turns the complete family \(\{G_n\}\) into one explicit
zeta-ratio product.

For real \(s>1\) and \(|z|\le1\), define

\[
                 \mathcal G(s,z)=\sum_{n\ge1}\frac{G_n(z)}{n^s}.
\tag{A01.2}
\]

Since \(|G_n(z)|\le1\) on the closed unit disk, this converges absolutely.
The divisor recurrence is equivalent, coefficient by coefficient, to

\[
nG_n(z)=z\sum_{d\mid n}\varphi(n/d)G_d(z)+(1-z)G_n(z),
\tag{A01.3}
\]

including \(n=1\).  The Dirichlet series of \(\varphi\) is
\(\zeta(s-1)/\zeta(s)\), so (A01.3) gives the shifted functional equation

\[
\mathcal G(s,z)=
\left(1-z+z\frac{\zeta(s)}{\zeta(s+1)}\right)
\mathcal G(s+1,z).
\tag{A01.4}
\]

Iterating (A01.4), and using
\(\mathcal G(s+J,z)\to G_1(z)=1\), yields

\[
\boxed{
\mathcal G(s,z)=
\prod_{j=0}^{\infty}
\left(1-z+z\frac{\zeta(s+j)}{\zeta(s+j+1)}\right).}
\tag{A01.5}
\]

The product converges normally on compact subsets of
\(\{\Re s>1,\ |z|\le1\}\): the ratio minus one is
\(O(2^{-j})\), uniformly after fixing a compact \(s\)-set.  At \(z=1\),
the product telescopes to \(\zeta(s)\), as it must.

Now choose an integer \(N_s\) from the zeta distribution

\[
                     \Pr(N_s=n)=\frac{n^{-s}}{\zeta(s)}.
\tag{A01.6}
\]

Dividing (A01.5) by its value at \(z=1\) gives

\[
\mathbb E[z^{T_{N_s}}]
=\prod_{j=0}^{\infty}
\left(
\frac{\zeta(s+j+1)}{\zeta(s+j)}
+\left[1-\frac{\zeta(s+j+1)}{\zeta(s+j)}\right]z
\right).
\tag{A01.7}
\]

Hence

\[
\boxed{
T_{N_s}\overset d=\sum_{j=0}^{\infty}B_{s,j},\qquad
\Pr(B_{s,j}=1)=1-\frac{\zeta(s+j+1)}{\zeta(s+j)},}
\tag{A01.8}
\]

with independent Bernoulli variables.  Their success probabilities are
positive and summable, so the sum is almost surely finite.  In particular,

\[
\mathbb E[T_{N_s}]
=\sum_{j\ge0}\left(1-\frac{\zeta(s+j+1)}{\zeta(s+j)}\right),
\quad
\operatorname{Var}(T_{N_s})
=\sum_{j\ge0}a_{s,j}(1-a_{s,j}),
\tag{A01.9}
\]

where \(a_{s,j}\) denotes the success probability in (A01.8).

This theorem is not a multiplicative factorization of a fixed composite
\(G_n\), and no such claim is made.  It is an exact all-integer mixture law,
different in scope and proof output from the prime-power product.  The
general downward-chain language, the one-step Minami conditioning, the
Dirichlet series of \(\varphi\), and generic Bernoulli-product consequences
remain zero-credit background; the residual is their exact conjunction for
this adaptive gcd absorption family.

**Re-entry status after the requested second output:**
`PROVED / SEND TO INDEPENDENT RE-REVIEW / HOLD_EXTERNAL`.
