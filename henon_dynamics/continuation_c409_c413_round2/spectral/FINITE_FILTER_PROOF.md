# Proof package: finite-cutoff filters and logarithmic Gibbs coherence

2026-09-06. Unnumbered candidate. Mathematical proof status below is separate
from source priority and the five-paper substance/admission gate.

## Claim and status

**PROVABLE AS STATED.** For every fixed finite probability filter, the
zero-coherence thermodynamic exponent is classified by the multiplicity
of its generating polynomial at $-1$. The filter changes only finitely
many top-level populations, and its normalized state is $O(N^{-1})$ in
trace norm from the ordinary Gibbs state on exactly the same finite
Hilbert space. A local zero-splitting theorem covers every finite
multiplicity of every encoded zero in the open critical strip.

This is not yet an independent-review or admission verdict. The sharp
cutoff result is owned by the primary source identified below, and the
finite-difference mechanism is classical. Whether their full stability
classification is sufficiently substantial remains an open screening issue.

## Assumptions and notation

Fix an integer $J\ge0$ and real weights $w_0,\ldots,w_J\ge0$ with
$\sum_{j=0}^Jw_j=1$. Define

$$P(z)=\sum_{j=0}^Jw_jz^j,\qquad k=\operatorname{ord}_{z=-1}P(z),
\qquad a=\frac{P^{(k)}(-1)}{k!}\ne0.$$

Here the order is zero when $P(-1)\ne0$. It is finite since $P(1)=1$.
Zero final weights are allowed; they only enlarge the ambient space.
Write $(s)_k=s(s+1)\cdots(s+k-1)$, with $(s)_0=1$.

For each positive integer $N$, let $\mathcal H_N=\mathbb C^{N+J}$ with
orthonormal basis $|n\rangle$, $1\le n\le N+J$, and set

$$H_N|n\rangle=(\ln n)|n\rangle,\qquad
U_N(t)|n\rangle=(-1)^{n+1}n^{-it}|n\rangle.$$

For $0<\beta<1$, define positive operators and partition sums

$$Q_N^P(\beta)=\sum_{j=0}^Jw_j\sum_{n=1}^{N+j}
n^{-\beta}|n\rangle\langle n|,\quad Z_N^P(\beta)=\operatorname{Tr}Q_N^P(\beta),
\quad \rho_N^P=Q_N^P/Z_N^P,$$

$$\rho_N^{\mathrm{full}}=
\frac{\sum_{n=1}^{N+J}n^{-\beta}|n\rangle\langle n|}
{\sum_{n=1}^{N+J}n^{-\beta}}.$$

Thus both states use the same $H_N$, $\mathcal H_N$ and observable $U_N(t)$.
The filtered state is a mixture of cutoff Gibbs states with mixture
probabilities $w_jZ_{N+j}(\beta)/Z_N^P(\beta)$; the weights of normalized
states are not incorrectly identified with $w_j$.

Let $s=\beta+it$ and define

$$\eta(s)=(1-2^{1-s})\zeta(s),\quad
S_N^P(s)=\sum_{j=0}^Jw_j\sum_{n=1}^{N+j}(-1)^{n+1}n^{-s},$$

$$L_N^P(\beta,t)=\operatorname{Tr}(\rho_N^P U_N(t))
=\frac{S_N^P(s)}{Z_N^P(\beta)},\qquad
F_N^P(\beta,t)=-\frac{\ln|L_N^P(\beta,t)|}{\ln N}.$$

The finite-size rate is interpreted as $+\infty$ when the numerator
vanishes. Its limit at each fixed $s$ will be finite and eventually
well-defined. All logarithms here are natural. No simplicity or RH
assumption is imposed on the zeta zeros.

## Theorem

For all the filters above:

1. Uniformly for $s$ in every compact subset $K$ of $\Re s>0$,

   $$\eta(s)-S_N^P(s)=(-1)^N\frac a2(s)_kN^{-s-k}
   +O_K(N^{-\Re s-k-1}).\tag{1}$$

2. For each fixed $0<\beta<1$,

   $$Z_N^P(\beta)\sim\frac{N^{1-\beta}}{1-\beta},\qquad
   \|\rho_N^P-\rho_N^{\mathrm{full}}\|_1
   \le \frac{2J(1-\beta+o(1))}{N}.\tag{2}$$

3. At each fixed $s=\beta+it$, $0<\beta<1$,

   $$\lim_{N\to\infty}F_N^P(\beta,t)=
   \begin{cases}1-\beta,&\eta(s)\ne0,\\1+k,&\eta(s)=0.\end{cases}\tag{3}$$

   In particular, every integer spike value $1,2,3,\ldots$ occurs,
   while the off-zero value and limiting encoded zero set are unchanged.

4. Let $s_0=\beta_0+it_0$ be a zero of $\eta$ of multiplicity $m$ in
   $0<\Re s<1$, and let $c=\eta^{(m)}(s_0)/m!\ne0$. Choose any
   $m$-th root $\tau_N$ of $(-1)^NN^{-s_0-k}$. Then, locally uniformly
   in $u\in\mathbb C$,

   $$\tau_N^{-m}S_N^P(s_0+\tau_Nu)
   \longrightarrow cu^m-\frac a2(s_0)_k.\tag{4}$$

   There are exactly $m$ zeros near $s_0$, all simple for sufficiently
   large $N$. They can be labeled

   $$s_{N,j}=s_0+\tau_N(u_j+o(1)),\qquad
   cu_j^m=\frac a2(s_0)_k,\quad 1\le j\le m.\tag{5}$$

   Their displacement scale is $N^{-(\beta_0+k)/m}$. This is a
   statement in the complex $s$ plane, not a claim that finite-cutoff
   zeros lie on the critical line or exactly at $s_0$.

## Strategy and dependency map

The exact alternating-tail integral below reduces the finite filter to
$P(-e^{-x})$. Its first nonzero Taylor coefficient at $x=0$ is precisely
the order $k$ specified above. A direct Laplace remainder estimate proves
(1); integral comparison and a positive-operator estimate prove (2).
Taking logarithms gives (3), and Taylor expansion plus Rouché's theorem
gives (4)–(5). No spectral identification or unproved zero theorem occurs.

Classical inputs are the gamma integral, the alternating-series
representation of $\eta$ on $\Re s>0$, holomorphic Taylor expansion,
and Rouché's theorem. The sharp-tail integral and sharp-cutoff rate are
also explicitly present in the cited 2026 source. No part of that baseline
is claimed as a new theorem here.

## Proof

### Step 1: exact tail representation, including convergence

For $M\ge1$ and $\Re s>0$,

$$R_M(s)=\eta(s)-\sum_{n=1}^M(-1)^{n+1}n^{-s}
=\frac{(-1)^M}{\Gamma(s)}\int_0^\infty
\frac{x^{s-1}e^{-(M+1)x}}{1+e^{-x}}\,dx.\tag{6}$$

To justify the interchange without assuming absolute convergence of
$\sum n^{-s}$, start with a finite alternating tail and apply the gamma
integral term by term. Its geometric sum in the integral is bounded in
modulus by $2e^{-(M+1)x}$ for every $x>0$, independently of the tail
length. The resulting integrable majorant is
$2x^{\Re s-1}e^{-(M+1)x}$. Dominated convergence gives (6). The
alternating Dirichlet series converges locally uniformly on $\Re s>0$
by summation by parts, so the limit is the stated $\eta$ tail.

The finite weighted sum of (6) gives the exact identity

$$\eta(s)-S_N^P(s)=\frac{(-1)^N}{\Gamma(s)}
\int_0^\infty x^{s-1}e^{-(N+1)x}
\frac{P(-e^{-x})}{1+e^{-x}}\,dx.\tag{7}$$

### Step 2: the filter order is the tail order

Since $P(z)=a(z+1)^k+O((z+1)^{k+1})$ and
$1-e^{-x}=x+O(x^2)$,

$$G_P(x):=\frac{P(-e^{-x})}{1+e^{-x}}
=\frac a2x^k+O(x^{k+1})\quad(x\downarrow0).\tag{8}$$

Choose a fixed $\delta>0$ so that the remainder in (8) is bounded by
$C_Px^{k+1}$ on $0<x<\delta$. Since the coefficients are a probability
vector, $|G_P(x)|\le1$ for $x\ge0$.

Insert the leading term from (8) in (7) and integrate it on the whole
half-line. It contributes

$$(-1)^N\frac a2\frac{\Gamma(s+k)}{\Gamma(s)}
(N+1)^{-s-k}=(-1)^N\frac a2(s)_k(N+1)^{-s-k}.\tag{9}$$

For $s$ in a compact $K\subset\{\Re s>0\}$, $1/\Gamma(s)$ is bounded.
The remainder over $(0,\delta)$ is bounded by a constant times

$$\int_0^\infty x^{\Re s+k}e^{-(N+1)x}\,dx
=\Gamma(\Re s+k+1)(N+1)^{-\Re s-k-1}.\tag{10}$$

The integral over $[\delta,\infty)$, including the subtracted polynomial,
is exponentially small uniformly on $K$, hence satisfies the same
polynomial bound for large $N$. Finally,
$(N+1)^{-s-k}=N^{-s-k}(1+O_K(N^{-1}))$. These bounds prove (1).

### Step 3: normalization and trace-norm proximity

For $M\to\infty$, integral comparison gives

$$\sum_{n=1}^M n^{-\beta}=\frac{M^{1-\beta}}{1-\beta}+O_\beta(1).
\tag{11}$$

Each $M=N+j$ has fixed $0\le j\le J$, so averaging proves the
partition asymptotic in (2).

Write $R_N=\sum_{n=1}^{N+J}n^{-\beta}|n\rangle\langle n|$ and
$Z_N^{\mathrm{full}}=\operatorname{Tr}R_N$. We have
$0\le Q_N^P\le R_N$, and the difference is supported on the last
$J$ basis states. Consequently

$$D_N:=\operatorname{Tr}(R_N-Q_N^P)\le JN^{-\beta}.$$

The triangle inequality applied to

$$\frac{Q_N^P}{Z_N^P}-\frac{R_N}{Z_N^{\mathrm{full}}}
=\frac{Q_N^P-R_N}{Z_N^{\mathrm{full}}}
+Q_N^P\left(\frac1{Z_N^P}-\frac1{Z_N^{\mathrm{full}}}\right)$$

gives a trace-norm bound of $2D_N/Z_N^{\mathrm{full}}$. Equation (11)
then yields (2). When $J=0$, the difference is identically zero.

### Step 4: fixed-point thermodynamic rates

If $\eta(s)\ne0$, equation (1) gives $S_N^P(s)\to\eta(s)\ne0$.
Together with (2), this proves

$$L_N^P(\beta,t)=(1-\beta)\eta(s)N^{\beta-1}(1+o(1)).\tag{12}$$

If $\eta(s)=0$, the factor $(s)_k$ is nonzero: all its possible zeros
have real part at most zero. Thus (1) and (2) give

$$L_N^P(\beta,t)=(-1)^{N+1}\frac{(1-\beta)a(s)_k}{2}
N^{-1-k-it}(1+o(1)).\tag{13}$$

The constants in (12) or (13) are nonzero. The logarithm of their
modulus, and the logarithm of the relative $1+o(1)$ error, divided by
$\ln N$ tend to zero. This proves (3), including eventual nonvanishing
at each fixed $s$. For every $k\ge0$, the probability polynomial
$P(z)=2^{-k}(1+z)^k$ realizes exactly that order, with $J=k$ and
$a=2^{-k}$. This proves the attainability assertion.

### Step 5: all multiplicities and local complex-zero scale

Choose a disk about $s_0$ contained in $\Re s>0$, containing no other
zero of $\eta$. Taylor's formula gives

$$\eta(s_0+v)=cv^m+O(v^{m+1}).$$

The uniform form of (1) is valid on this disk. We have
$|\tau_N|=N^{-(\beta_0+k)/m}$ and therefore
$|\tau_N|\ln N\to0$. Hence uniformly on compact sets of $u$,

$$N^{-\tau_Nu}=\exp(-\tau_Nu\ln N)\to1,\qquad
\frac a2(s_0+\tau_Nu)_k\to\frac a2(s_0)_k.$$

Divide (1), after substituting $s=s_0+\tau_Nu$, by $\tau_N^m$.
The leading Taylor term of $\eta$ becomes $cu^m$; the tail term
becomes $a(s_0)_k/2$. The Taylor error is $O(|\tau_N|)$ on bounded
$u$ sets, and the tail error is $O(N^{-1+o(1)})$. This proves (4).

The limiting polynomial has $m$ distinct nonzero roots $u_j$, because
$c$ and $a(s_0)_k$ are nonzero. Rouché's theorem on disjoint small
circles about these roots gives exactly one zero, counted with
multiplicity, of the scaled function in each circle for large $N$.
Uniform convergence $S_N^P\to\eta$ and Rouché on the original disk
show that there are exactly $m$ zeros there in total. All the zeros
just found are therefore simple and exhaust the local cluster.
Shrinking the small circles proves (5). This finishes the proof.

## Source ownership and scope corrections

The comparison baseline is Wei et al., *The Riemann Hypothesis manifested
in dynamical quantum phase transitions*,
[Nature Communications (2026)](https://www.nature.com/articles/s41467-026-74935-8).
Their Supplementary Notes 1–3 explicitly prove the $k=0$ sharp-cutoff
rate and handle the divergent normalization. They use spin count
$\log_2N$, so their rate is this document's rate multiplied by $\ln2$.
The proposed increment is the **all-finite-filter stability classification
on the same finite system**, not a correction of that sharp result.

The zero correspondence here is the identity
$\eta(s)=(1-2^{1-s})\zeta(s)$ in $0<\Re s<1$, with the logarithmic
spectrum and alternating phase inserted as input. There is no source-derived
Euler factor or root number, no target spectral divisor and no
Hilbert–Pólya conclusion. No finite-cutoff exact-zero identification is
made. No assertion is made about the second Riemann–Siegel protocol.

## Remaining risks and verification boundary

- Complete proof above, but not yet independently checked. No numerical
  receipt is claimed at this point.
- Priority search for finite-difference/summability ownership and the
  standalone substance decision are still open. The elementary proof
  length is not itself evidence either for or against sufficient substance.
- $P$ and $J$ are fixed before $N\to\infty$. This proof does not allow
  filter degree to grow with $N$, and does not claim high-$t$ uniformity.
- Trace-norm proximity does not mean equal Gibbs states: the altered
  highest populations are an explicit state-preparation perturbation.
- The theorem gives instability of the **pointwise logarithmic rate**
  under this precise vanishing perturbation, not a universal physical
  prohibition on all possible dynamical phase transitions.

AI-assisted mathematical derivation and source checking; internal work,
not human peer review or a publication-readiness certificate.
