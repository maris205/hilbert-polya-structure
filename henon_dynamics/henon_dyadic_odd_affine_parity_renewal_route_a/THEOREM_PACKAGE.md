# Exact theorem package / 精确定理包

Let \(a,b\in\mathbb Z\) be odd and let \(T=T_{a,b}\) be the frozen map on \(\mathbb Z_2\). Write \(\epsilon_j(x)=T^j(x)\bmod2\), \(s_j=\sum_{i<j}\epsilon_i\), and

\[
A_\epsilon=\sum_{j=0}^{n-1}\epsilon_j2^j a^{s_n-s_{j+1}}.
\]

以下所有结论同时适用于任意奇整数 \(a,b\)。有限计算只做回归验证，证明是全参数符号证明。

## Theorem 1 — fixed words and classical zeta / 固定词与经典 zeta

For every admissible length-\(n\) parity word,

\[
2^nT^n(x)=a^{s_n}x+bA_\epsilon.
\]

Because \(2^n-a^{s_n}\) is odd, the word has the unique fixed point

\[
x_\epsilon=\frac{bA_\epsilon}{2^n-a^{s_n}}\in\mathbb Z_2.
\]

The classical parity conjugacy makes every binary word admissible and distinct. Hence

\[
\#\operatorname{Fix}(T^n)=2^n,
\quad
P(n)=\sum_{d\mid n}\mu(n/d)2^d,
\quad
\zeta_{AM}(z)=\frac1{1-2z}.
\]

**Proof.** Induct on the branches to obtain the iterate identity. The denominator is an even integer minus an odd integer, hence a unit of \(\mathbb Z_2\). The parity homeomorphism gives existence and uniqueness for every word. Möbius inversion separates exact periods, and the exponential definition of \(\zeta_{AM}\) gives the rational expression. ∎

逐分支归纳得到迭代公式；分母为“偶数减奇数”，故在 \(\mathbb Z_2\) 中可逆。经典 parity 同胚保证每个二元词恰对应一个点。Möbius 反演与指数定义给出其余公式。

## Theorem 2 — stability-weighted parameter blindness / 稳定性加权参数盲性

At the point with word \(\epsilon\),

\[
(T^n)'(x_\epsilon)=\frac{a^{s_n}}{2^n},
\qquad
\left|1-\frac{a^{s_n}}{2^n}\right|_2=2^n.
\]

Therefore

\[
W_n=\sum_{x\in\operatorname{Fix}(T^n)}|1-(T^n)'(x)|_2^{-1}=1,
\qquad
\zeta_{\rm stab}(z)=\exp\!\left(\sum_{n\ge1}\frac{W_nz^n}{n}\right)=\frac1{1-z}.
\]

**Proof.** The branch derivatives are \(1/2\) and \(a/2\). Moreover \(2^n-a^{s_n}\) is odd, so the displayed 2-adic norm is \(2^n\). There are \(2^n\) fixed points, each of weight \(2^{-n}\). ∎

两个 zeta 都完全抹去奇参数 \(a,b\)：无权计数只剩二元词数，稳定性权重又把每个时期的总和压成 1。

## Theorem 3 — first-return renewal / 首返 renewal

Let \(O=1+2\mathbb Z_2\). For \(x\in O\), define

\[
\tau(x)=v_2(ax+b),\qquad R(x)=\frac{ax+b}{2^{\tau(x)}}.
\]

The single point \(x_*=-b/a\) has \(\tau=\infty\), maps to zero, and never returns. More generally, parity strings with only finitely many ones form a countable Haar-null exceptional set. On the full-conditional-measure recurrent set \(O_\infty\), successive blocks are
\(10^{k-1}\), so \(R\) is conjugate to the one-sided full shift on \(k\in\{1,2,\ldots\}\), with

\[
\mu_O(\tau=k)=2^{-k}.
\]

The return times are iid under conditional Haar measure. Each constant symbol gives

\[
x_k=\frac b{2^k-a},
\]

so \(\operatorname{Fix}(R)\) is countably infinite and the ordinary Artin–Mazur zeta of \(R\) is undefined.

**Proof.** The affine map \(x\mapsto ax+b\) is a Haar-preserving bijection from \(O\) to \(2\mathbb Z_2\). The valuation layers in \(2\mathbb Z_2\) have conditional masses \(2^{-k}\). Concatenating return blocks is exactly the classical parity coding. Eventually-zero binary strings are countable and null. Solving \(ax+b=2^kx\) gives \(x_k\), whose valuation is exactly \(k\). ∎

## Theorem 4 — original-clock roof recovery / 原始时钟屋顶恢复

Give symbol \(k\) roof length \(r(k)=k\). The one-loop first-return series and roof zeta are

\[
F(z)=\sum_{k\ge1}z^k=\frac z{1-z},
\qquad
\zeta_{\rm roof}(z)=\frac1{1-F(z)}=\frac{1-z}{1-2z}.
\]

Equivalently,

\[
\log\zeta_{\rm roof}(z)=\sum_{n\ge1}\frac{(2^n-1)z^n}{n}.
\]

These are precisely the original-clock periodic points whose parity words are not all zero. Restoring the omitted zero fixed orbit contributes \((1-z)^{-1}\), hence

\[
\zeta_{\rm roof}(z)(1-z)^{-1}=\frac1{1-2z}=\zeta_{AM}(z).
\]

**Proof.** A closed roof orbit is a cyclic concatenation of return blocks, so the standard one-vertex renewal determinant is \(1-F(z)\). Algebra gives the coefficient identity. Every nonzero periodic binary word contains a one and therefore meets \(O\); the only missing periodic orbit is zero. ∎

该恒等式明确区分“加速后的 return 时钟”和“原始分支时钟”；若遗漏零轨道因子，就不能恢复原系统 zeta。

## Theorem 5 — Koopman boundary / Koopman 边界

On \(H=L^2(\mathbb Z_2,\mu)\), \(Uf=f\circ T\) is a proper isometry. Under parity coding it is the composition isometry of the one-sided Bernoulli shift. Its Wold decomposition is

\[
U\simeq I_{\mathbb C}\oplus S^{(\aleph_0)}.
\]

Thus \(\sigma(U)=\overline{\mathbb D}\), \(\sigma_p(U)=\{1\}\), and \(U\) is noncompact, outside every finite Schatten class, and has no ordinary trace-class Fredholm determinant. The two-sided natural extension gives a same-clock unitary only after changing phase space.

**Proof.** The range consists of functions independent of the first parity digit. The tail intersection is the constants by the Bernoulli zero–one law, while the defect space is an infinite-dimensional copy of the tail \(L^2\) space. Wold's theorem yields the model and its standard spectral consequences. ∎

## Parameter and 3x+1 boundaries / 参数与 3x+1 边界

- Multiplication by odd \(b\) conjugates \(T_{a,1}\) to \(T_{a,b}\).
- If exactly one of \(a,b\) is even, the odd branch numerator is odd and division by two leaves \(\mathbb Z_2\); the frozen theorem does not extend.
- For \((a,b)=(3,1)\), the word \(100\) gives
  \(1/5\mapsto4/5\mapsto2/5\mapsto1/5\). This is a legal \(\mathbb Z_2\) cycle but not a positive-integer orbit. Nothing here proves or advances the positive-integer 3x+1 conjecture.

## Route-A theorem verdict / Route-A 定理结论

The exact tuple is

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

A0 failure forces `ROUTE_A_REJECTED`. The package claims no arithmetic Euler/local data, root number, automorphy, target divisor match, or Hilbert–Pólya operator.

A0 失败强制整体拒绝。精确定理仍有动力学价值，但不构成算术目标或 Hilbert–Pólya 构造。
