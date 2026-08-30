# A02 factor-sum descent：快速 theorem/value spike

日期：2026-08-30 UTC。状态：reserve gate only；未分配论文编号，不是论文或
外部优先权结论。

## Claim

状态为正整数 $n$。若 $n$ 有无序非平凡因子对

$$
\mathcal F(n)=\{(a,b):ab=n,\ 2\leq a\leq b\},
$$

则从 $\mathcal F(n)$ 中均匀选择一对，并更新

$$
n\longmapsto a+b-1. \tag{1}
$$

若 $\mathcal F(n)=\varnothing$，则 $n$ 吸收。scout 希望找到任意尺寸的
吸收终点与时间联合律，而不是将下面的一阶 divisor-DP 重述为定理：

$$
L_n(\mathbf u,z)=
\frac{z}{|\mathcal F(n)|}
\sum_{(a,b)\in\mathcal F(n)}L_{a+b-1}(\mathbf u,z). \tag{2}
$$

在终态 $p$，边界值为 $L_p(\mathbf u,z)=u_p$。

## Status

目标联合律的状态是 **NOT CURRENTLY JUSTIFIED**。

本轮证明了一个全尺寸结构定理：奇素数吸收、sharp logarithmic
pathwise clock，以及达到最大时钟的一个无限族和其精确极端原子。但是，
第二轮尝试没有把这些结果升级为联合律闭式、可乘分解、有限状态 transfer
或第二条非机械历史公式。

最终候选处置：**KILL_THEOREM_THIN / OWNER_ADJACENT**。

这不是因为过程错误；而是因为通过预设门槛的唯一全尺寸结果只是一个两行
势函数论证，完整随机律仍等同于 (2) 的 factorization DAG。

## Assumptions and notation

- 因子对是无序且彼此等概率；重复 child 仍按因子对重数保留概率。
- $T_n$ 表示从 $n$ 出发到吸收的步数。
- $P_n$ 表示吸收终点。
- $q(n)=|\mathcal F(n)|$。
- 对 $n\geq3$，定义势函数 $V(n)=n-2$。
- 对 $r\geq1$，定义 $N_r=2+2^r$。

## Proof strategy and dependency map

1. 将一次下降量因子化，证明 $V$ 每步至少减半。
2. 用奇偶性证明合数起点不可能在 $2$ 吸收，从而终点是奇素数。
3. 反向构造 $N_r\to N_{r-1}$，证明 logarithmic bound sharp。
4. 检查等号条件，确定 $N_r$ 的最长历史唯一，并得到极端联合原子。
5. 分别攻击半素数、素幂、固定因子型和历史展开；判断它们是否关闭为
   非 DP 的任意尺寸联合律。

## Proof: the structural theorem that did survive

### Theorem 1 (absorption, clock, and sharp extremal atom)

For the chain (1):

1. every trajectory strictly descends and is absorbed;
2. from every composite initial state, the absorbing state is an odd prime;
3. for every $n\geq3$,

   $$
   T_n\leq\lfloor\log_2(n-2)\rfloor
   \qquad\text{pathwise}; \tag{3}
   $$

4. for every $r\geq1$, the state $N_r=2+2^r$ has maximum possible
   absorption time exactly $r$;
5. its unique length-$r$ history is

   $$
   N_r\to N_{r-1}\to\cdots\to N_1=4\to3, \tag{4}
   $$

   obtained at every step by choosing the factor pair
   $(2,1+2^{j-1})$ at state $N_j$. Consequently

   $$
   \Pr_{N_r}(P_{N_r}=3,T_{N_r}=r)
   =\prod_{j=1}^r\frac1{q(N_j)}. \tag{5}
   $$

#### Proof

Let $(a,b)\in\mathcal F(n)$ and put $n'=a+b-1$. Strict descent follows from

$$
n-n'=ab-a-b+1=(a-1)(b-1)>0. \tag{6}
$$

For the shifted potential,

$$
(n-2)-2(n'-2)
=ab-2-2a-2b+6
=(a-2)(b-2). \tag{7}
$$

Thus

$$
V(n')\leq\frac{V(n)}2, \tag{8}
$$

and equality holds exactly when $a=2$ because $2\leq a\leq b$.
Strict descent on the positive integers proves finite absorption.

If the current state is odd, both factors are odd and $a+b-1$ is odd. If
the current state is even, the child is odd exactly when the chosen factors
have the same parity, which in this case means that both are even. Therefore,
once a path becomes odd, it remains odd. A child of a composite state is at
least $2+2-1=3$, so the terminal value $2$ cannot be reached from a
composite state. Every absorbing integer at least two is prime. Hence a
composite start is absorbed at an odd prime.

Suppose a trajectory from $n\geq3$ has length $t$. Its terminal prime $p$
satisfies $V(p)=p-2\geq1$. Iterating (8) gives

$$
1\leq V(p)\leq\frac{n-2}{2^t}.
$$

Therefore $2^t\leq n-2$, which proves (3).

For $N_j=2+2^j$, the pair

$$
(2,1+2^{j-1})\in\mathcal F(N_j)
$$

and its child is

$$
2+(1+2^{j-1})-1=2+2^{j-1}=N_{j-1}. \tag{9}
$$

This constructs the length-$r$ history (4). Bound (3) gives
$T_{N_r}\leq r$, so its maximum is exactly $r$.

Finally, a length-$r$ path from $N_r$ has
$V(N_r)=2^r$ and terminal potential at least one. Every inequality in the
$r$ applications of (8) must therefore be an equality, and the terminal
potential must be one. Equation (7) forces $a=2$ at every step; the terminal
is $3$. Thus (4) is the unique length-$r$ history. Each required pair is one
of the $q(N_j)$ equiprobable pairs, so multiplication of the conditional
step probabilities yields (5). $\square$

### What this theorem gives—and does not give

The theorem supplies a genuine all-size result and an exact joint-law atom.
It does not determine any of the following:

- the other atoms of the law from $N_r$;
- the terminal support for a general initial integer;
- the probability generating function of $T_n$ on a closed infinite class;
- even the complete law on powers of one fixed prime.

The extremal probability (5) also retains the arithmetic data
$q(2+2^j)$; it is not a product of an explicit parameter-only sequence.

## Two-round value test

### Round 1: natural infinite families

#### Distinct semiprimes

For $n=pq$ with distinct primes $p<q$, there is one factor pair and the first
step is deterministic:

$$
pq\longmapsto p+q-1. \tag{10}
$$

The child need not be prime, semiprime, a prime power, or a divisor of $pq$.
Its continuation requires the unrestricted factorization of $p+q-1$.
Thus (10) is a one-step formula, not a closed family law.

This lane also has a direct adjacent owner. Kawagoe and Huber define an
iteration using sums of prime and composite factors. Their preimage analysis
states that if distinct odd primes $k,j$ satisfy $k+j=n+1$, then $kj$ maps
to $n$; equivalently, their map agrees with (10) on distinct odd semiprimes
([arXiv:1608.06593](https://arxiv.org/abs/1608.06593)). Consequently the
deterministic semiprime transition and its additive preimage tree cannot be
presented as an A02 residual contribution.

#### Prime powers

For $n=p^k$, the factor pairs are
$(p^i,p^{k-i})$, $1\leq i\leq\lfloor k/2\rfloor$, and the children are

$$
p^i+p^{k-i}-1. \tag{11}
$$

These children leave the prime-power class immediately. Their subsequent
factorizations are not controlled by $k$ or by the divisor lattice of
$p^k$. Even at $p=2$, the exact joint-support size and maximum time for
$2\leq k\leq15$ are

```text
k:            2  3  4  5  6  7  8  9 10 11 12 13 14 15
joint support:1  1  2  2  3  3  5  4  9  5  7  5 12 12
max time:     1  1  2  1  2  2  3  1  3  3  5  4  6  5
```

The nonmonotone values are not themselves a proof that no formula exists.
They do falsify the candidate closures suggested in the scout: the law is
not indexed only by the exponent, does not remain on a multiplicative
subposet, and shows no Bernoulli/product pattern analogous to A01.

#### Fixed factor type and parity classes

The parity statement in Theorem 1 is closed, but it only identifies the
terminal parity. A state with $2$-adic valuation one stays even for that
step; a state divisible by four can choose a mixed-parity pair and stay even
or a pair of even factors and become odd. Hence valuation does not form a
closed Markov quotient. The smallest-prime-factor and divisor-count
statistics also fail to determine the multiset of children (11).

Round-1 result: a sharp clock theorem exists, but none of the three natural
parameter families produces the requested joint law.

### Round 2: history sum / transform route

Expanding (2) expresses every atom as

$$
\sum_{n=n_0>n_1>\cdots>n_t=p}
\prod_{s=0}^{t-1}\frac{m(n_s,n_{s+1})}{q(n_s)}, \tag{12}
$$

where $m(u,v)$ counts factor pairs $(a,b)\in\mathcal F(u)$ satisfying
$a+b-1=v$. Formula (12) is exact, but it is merely the path expansion of the
same acyclic DP. The additive child $a+b-1$ destroys divisibility and
multiplicativity, so neither Dirichlet convolution nor a primewise tensor
factorization appears. Unlike A01, there is no adjacent-state difference
that factors the PGF and no valuation chain that yields independent
increments.

The reverse equation for one edge is

$$
a+b=s+1,\qquad n=ab. \tag{13}
$$

Thus reverse histories require additive representations of $s+1$ together
with factorization restrictions on their products. On prime-pair lanes this
already meets Goldbach/Cunningham-type arithmetic, while on unrestricted
pairs it reconstructs the same divisor DAG. Replacing (2) by (12) or (13)
does not provide an independent proof engine or a nonmechanical closed form.

Round-2 result: the history route is a restatement of the recursion and
fails the precommitted value gate.

## Exact pilot

The independent verifier is
[`verify_stoch_factor_sum_reserve.py`](verify_stoch_factor_sum_reserve.py),
with canonical output
[`verify_stoch_factor_sum_reserve.out`](verify_stoch_factor_sum_reserve.out).
It does not import the scouting pilot and uses `fractions.Fraction` only.

Coverage:

- all $80,659$ literal factor-pair edges for $4\leq n\leq20,000$;
- exact joint laws for all starts $1\leq n\leq5,000$;
- independent forward-mass comparison for $n\leq800$;
- the time bound and odd-prime terminal theorem on every tested state;
- the sharp family and exact extreme atom for $1\leq r\leq15$;
- the power-of-two obstruction table above;
- the stored $n=36$ five-atom law.

Fresh output:

```text
factor-sum descent reserve structural control: PASS
assertions=342915
literal_factor_edges=80659; n=4..20000
exact_start_states=5000; joint_atoms=62455; forward_crosscheck=n<=800
theorem=odd-prime absorption; T<=floor(log2(n-2)); sharp N_r=2+2^r
sharp_atoms_r1_to_r15=[(1, 4, '1'), (2, 6, '1'), (3, 10, '1'), (4, 18, '1/2'), (5, 34, '1/2'), (6, 66, '1/6'), (7, 130, '1/18'), (8, 258, '1/54'), (9, 514, '1/54'), (10, 1026, '1/378'), (11, 2050, '1/1890'), (12, 4098, '1/5670'), (13, 8194, '1/17010'), (14, 16386, '1/51030'), (15, 32770, '1/357210')]
power_two_joint_support_(exponent,size,max_time)=[(2, 1, 1), (3, 1, 1), (4, 2, 2), (5, 2, 1), (6, 3, 2), (7, 3, 2), (8, 5, 3), (9, 4, 1), (10, 9, 3), (11, 5, 3), (12, 7, 5), (13, 5, 4), (14, 12, 6), (15, 12, 5)]
joint_law_n36=(((3, 4), Fraction(1, 8)), ((5, 3), Fraction(1, 4)), ((7, 2), Fraction(1, 8)), ((11, 1), Fraction(1, 4)), ((19, 1), Fraction(1, 4)))
decision_signal=no_all_size_joint_closed_form_beyond_divisor_DAG
```

The $342,915$ assertions are falsification controls, not a proof of the
quantified statements.

## Owner risk

Exact searches on 2026-08-30 used `"factor-sum descent"`,
`choose factorization "a+b-1"`, `"a+b-1" "ab=n" dynamics`,
`random factor pair Markov chain`, and variants with divisor-pair iteration.
No direct source for the full random chain (1) was located. This is
**BOUNDED_NO_DIRECT_HIT**, not a novelty certificate.

Two adjacent primary sources materially reduce the residual:

1. Kawagoe--Huber, *An iteration based on prime and composite factors*,
   [arXiv:1608.06593](https://arxiv.org/abs/1608.06593), owns an integer
   iteration mixing additive and multiplicative factor data and, as noted
   above, exactly owns transition (10) and its prime-pair reverse tree.
2. Kak, *Random Sequences Based on the Divisor Pairs Function*,
   [arXiv:1210.4614](https://arxiv.org/abs/1210.4614), studies randomness
   derived from divisor-pair functions. Its inspected abstract does not state
   (1), but it prevents broad claims that divisor-pair randomness itself is a
   new mechanism.

Generic absorbing-chain recursion, divisor enumeration, strict descent,
and path sums receive zero credit. The bounded direct miss cannot compensate
for the absence of a full-law theorem.

## Decision

**KILL_THEOREM_THIN / OWNER_ADJACENT.** Do not assign a paper number and do
not spend another proof round on A02 in its current form.

Theorem 1 may remain in the reserve ledger as a correct structural lemma, but
it is not sufficient for the requested paper-level value:

- the proof is elementary once $V(n)=n-2$ is chosen;
- only one extremal atom is explicit;
- the proposed main object, the joint absorption law, remains exactly (2);
- prime-power and semiprime restrictions do not close;
- the cleanest semiprime transition is already owned by an adjacent factor
  iteration.

A future re-entry should require genuinely new information, for example a
parameterized class closed under (1) with a complete PGF, or a transform that
turns (12) into a product/determinant independent of the state-by-state DAG.
Additional tables, larger $n$, fitted recurrences, or reformatting the path
sum do not qualify.

## Corrections or missing assumptions

- The scout's phrase “strict下降来自 $a+b-1<ab$” is correct; the exact gap is
  $(a-1)(b-1)$, not merely “strict by one” except at $a=b=2$.
- For composite starts, the absorbing endpoints are odd primes, not arbitrary
  integers with no nontrivial factor pair. Starts $1$, $2$, or an odd prime
  are already absorbed at time zero.
- Equation (5) is the mass of the unique maximum-length atom only for the
  sharp family $N_r=2+2^r$; it is not the whole absorption law.

## Open risks

- A direct owner may exist under recreational-number-theory terminology not
  reached by the bounded search.
- The negative value judgment is a pipeline decision, not a theorem that no
  closed form can exist.
- Rare arithmetic subfamilies defined by extra primality hypotheses can be
  deterministic, but unconditional infinitude of such families may itself
  be open and would not satisfy the current all-size requirement.
