# Exact theorem package — HCS-C366

## Frozen convention

Let $\mathcal H_1=\mathbb C^{N+1}$, with ordered site basis
$\{|j\rangle:0\leq j\leq N\}$, where $N\geq0$. For the main theorem let
$\Omega>0$, and define

\[
h_N=\frac{\Omega}{2}\sum_{j=0}^{N-1}\sqrt{(j+1)(N-j)}
 (|j\rangle\langle j+1|+|j+1\rangle\langle j|).
\]

The many-body Hamiltonian is the number-conserving fermionic second
quantization $H_N=d\Gamma(h_N)$. Basis vectors are increasing wedges
$|j_1<\cdots<j_m\rangle$, and $U(t)=e^{-itH_N}$. A uniform-field boundary
means adding $B\widehat m$, where $\widehat m$ is the fermion-number operator.

## Theorem 1 — one-particle representation and full spectrum

Put $J=N/2$ and identify $|j\rangle$ with the $J_z$-weight $m_z=j-J$.
Then $h_N=\Omega J_x$. Consequently its simple spectrum is

\[
E_r=\Omega\left(\frac N2-r\right),\qquad r=0,\ldots,N.
\]

For

\[
K_r(j)=\sum_{\ell}(-1)^\ell
\binom j\ell\binom{N-j}{r-\ell},
\]

the normalized eigenvector has components

\[
v_r(j)=\frac{\sqrt{\binom Nj}\,K_r(j)}
 {\sqrt{2^N\binom Nr}}.
\]

In particular,

\[
\sum_{j=0}^N\binom NjK_r(j)K_s(j)
=2^N\binom Nr\delta_{rs}.
\]

### Proof

The spin-$J$ identity

\[
\langle m_z+1|J_x|m_z\rangle
=\frac12\sqrt{(J-m_z)(J+m_z+1)}
\]

is the displayed hopping coefficient after $m_z=j-J$. Rotation of $J_z$ to
$J_x$ gives the $N+1$ simple weights $J,J-1,\ldots,-J$. Pascal identities in
the tridiagonal equation give $h_Nv_r=E_rv_r$. Moreover, the coefficient of
$z^r$ in $(1-z)^j(1+z)^{N-j}$ is $K_r(j)$, and

\[
\sum_j\binom Nj(1-z)^j(1+z)^{N-j}
                   (1-w)^j(1+w)^{N-j}
=2^N(1+zw)^N.
\]

Extracting $z^rw^s$ proves orthogonality. The $N+1$ nonzero orthogonal
vectors are complete.

## Theorem 2 — exact propagator and perfect mirror

For a particle starting at site zero,

\[
\langle k|e^{-ith_N}|0\rangle
=(-i)^k\sqrt{\binom Nk}
 \sin^k\frac{\Omega t}{2}
 \cos^{N-k}\frac{\Omega t}{2}.
\]

Thus its position is binomial with parameter $\sin^2(\Omega t/2)$. At
$t_*=\pi/\Omega$,

\[
e^{-it_*h_N}=(-i)^N R,
\qquad R|j\rangle=|N-j\rangle.
\]

At $t_*/2$, the endpoint-start distribution is $2^{-N}\binom Nk$.

### Proof

The spin-$J$ representation is the symmetric $N$-fold tensor power of the
spin-$1/2$ representation. Since
$e^{-it\Omega\sigma_x/2}|0\rangle=
\cos(\Omega t/2)|0\rangle-i\sin(\Omega t/2)|1\rangle$, expansion in the
normalized symmetric weight basis gives the amplitude. At angle $\pi$, every
bit flips with phase $-i$, giving $(-i)^NR$.

## Theorem 3 — full many-body mirror phase and spectrum

The $m$-particle propagator is

\[
U_m(t)=\bigwedge^m e^{-ith_N}.
\]

At $t=t_*$,

\[
|j_1<\cdots<j_m\rangle\longmapsto
(-i)^{mN}(-1)^{m(m-1)/2}
|N-j_m<\cdots<N-j_1\rangle.
\]

Every $m$-particle energy is

\[
E_S=\Omega\left(\frac{mN}{2}-\sum_{r\in S}r\right),
\qquad S\subseteq\{0,\ldots,N\},\quad |S|=m.
\]

If the Gaussian polynomial is defined recursively by

\[
{n\brack m}_q={n-1\brack m}_q+q^{n-m}{n-1\brack m-1}_q,
\quad {n\brack0}_q={n\brack n}_q=1,
\]

with out-of-range entries zero, then all multiplicities are encoded by

\[
\prod_{r=0}^N(1+yq^r)
=\sum_{m=0}^{N+1}y^m q^{m(m-1)/2}{N+1\brack m}_q.
\]

### Proof

Second quantization acts on the $m$-particle space by the exterior power.
At $t_*$ each occupied orbital contributes $(-i)^N$. Reflection reverses all
$m$ wedge factors, and restoring increasing order takes $m(m-1)/2$
transpositions. Exterior products of the one-particle eigenvectors give the
energy formula.

Let $A_{N,m}(q)$ be the coefficient of $y^m$ in the product. Splitting subsets
according to whether they contain $N$ gives

\[
A_{N,m}=A_{N-1,m}+q^N A_{N-1,m-1}.
\]

The proposed expression $q^{m(m-1)/2}{N+1\brack m}_q$ satisfies the same
recurrence because the displayed Gaussian recursion contributes the factor
$q^{N+1-m}$ before the exponent shift. The empty product is the common base
case, proving the identity coefficient by coefficient.

## Proposition 4 — exact boundaries

1. For $N=0$, there is one site and reflection is the identity.
2. For $\Omega=0$, $H_N=0$; distinct endpoints do not transfer.
3. For $\Omega<0$, the positive time $\pi/|\Omega|$ gives the conjugate
   one-particle phase $i^N$; probabilities are unchanged.
4. Adding $B\widehat m$ multiplies sector $m$ by $e^{-imBt}$ and changes no
   within-sector transport. More precisely,
   \[
   U_B(2\pi/|\Omega|)=
   e^{-i(2\pi B/|\Omega|)\widehat m}(-1)^{N\widehat m},
   \qquad
   U_B(4\pi/|\Omega|)=e^{-i(4\pi B/|\Omega|)\widehat m}.
   \]
   Hence the first time is a full Fock identity exactly when
   $2B/|\Omega|+N\in2\mathbb Z$, and the second is a full Fock identity
   exactly when $2B/|\Omega|\in\mathbb Z$.
5. In particular, for the unshifted model $B=0$, the $2\pi/|\Omega|$
   propagator is identity for even $N$ and fermion parity for odd $N$;
   $4\pi/|\Omega|$ is always identity.
6. No perfect-transfer claim is made for generic perturbations of the
   engineered couplings.

The identity conditions include the vacuum sector, so “global phase” means
literal identity. A sectorwise phase alone is not a global Fock revival.

## Route-A evaluation

The theorem is **PROVABLE AS STATED**. The exact finite ledger covers every
fermionic subset through $N=14$, but analytic proofs own the all-$N$ claims.

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
scope = NO_BAD_EULER_OR_ROOT_NUMBER
```

Natural source quantization and revivals do not provide a rational-prime
carrier, logarithmic-prime clock, target determinant, target divisor,
functional equation, target-zero match, or Hilbert--Pólya operator.
