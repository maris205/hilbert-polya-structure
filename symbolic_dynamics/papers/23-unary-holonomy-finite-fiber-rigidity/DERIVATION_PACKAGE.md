# Derivation Package — SD-C25

**Candidate:** SD-C25  
**Purpose:** compact algebraic derivation ledger for implementation and
manuscript cross-checking  
**Arithmetic mode:** exact integer/rational/symbolic whenever possible  
**Zero-data use:** none

## D1. Graph edge and quotient

\[
 n\to d
 \iff d\mid n+1,\ d\ge2,
\qquad
 q(n,d)=\frac{n+1}{d}.
\]

On the canonical orbit

\[
 C_k:k\to k+1\to\cdots\to2k-1\to k,
\]

\[
 q(n,n+1)=1,\qquad
 q(2k-1,k)=2.
\]

Therefore

\[
        W(C_k)=1^{k-1}2.
\]

This identity is the only new source datum used by the finite-fiber branch.

## D2. Endpoint monomial

With \(\tau(n,d)=\log(nd)\),

\[
\begin{aligned}
\exp R(C_k)
 &=\prod_{(n,d)\in C_k}nd\\
 &=\left(\prod_{n=k}^{2k-1}n\right)
   \left(\prod_{d=k}^{2k-1}d\right)\\
 &=M_k^2,
\end{aligned}
\]

where

\[
        M_k=\frac{(2k-1)!}{(k-1)!}.
\]

Hence

\[
        e^{-sR(C_k)}=M_k^{-2s},
\qquad
        z^{|C_k|}=z^k.
\]

## D3. Finite-semigroup response

For a morphism \(\phi\), put

\[
        a=\phi(1),\qquad b=\phi(2).
\]

Then

\[
        \phi(W(C_k))=a^{k-1}b.
\]

If \(a^i=a^j\) for \(i<j\), then

\[
        a^{i+r}b=a^{j+r}b
\]

for every \(r\ge0\).  Tail and period are

\[
        \mu=i+1,\qquad \lambda=j-i
\]

in the \(k\)-index convention.  Any terminal acceptance or scalar
evaluation inherits this period.

## D4. Composite witness in an accepted residue class

If an ultimately periodic prime-only set contains \(p\) beyond a tail with
period \(\lambda\), then

\[
        c=p(1+\lambda)=p+p\lambda
\]

satisfies

\[
        c\equiv p\pmod\lambda
\]

but is composite.  This witness avoids any density theorem about primes.

## D5. Characteristic recurrence

Let \(\mathbb F\) be a characteristic-zero field and take
\(A,B\in M_d(\mathbb F)\), \(u,v\in\mathbb F^d\).
Let

\[
 \chi_A(t)=t^d+c_{d-1}t^{d-1}+\cdots+c_0.
\]

Cayley–Hamilton gives

\[
        A^{k+d-1}
        +c_{d-1}A^{k+d-2}
        +\cdots+c_0A^{k-1}=0.
\]

For

\[
 \Lambda_{\rm bil}(X)=u^{\mathsf T}XBv,
\qquad
 \Lambda_{\rm tr}(X)=\operatorname{tr}(XB),
\]

we obtain

\[
 r_{k+d}+c_{d-1}r_{k+d-1}+\cdots+c_0r_k=0.
\]

The resolvent identity yields

\[
\sum_{k\ge1}x_kz^{k-1}
=u^{\mathsf T}(I-zA)^{-1}Bv,
\]

\[
\sum_{k\ge1}y_kz^{k-1}
=\operatorname{tr}\bigl((I-zA)^{-1}B\bigr).
\]

Both denominators divide \(\det(I-zA)\).

## D6. SML support conversion

For a characteristic-zero LRS \(r_k\), SML gives

\[
 Z(r)=F\cup\bigcup_{j=1}^J
 \{a_j+m_jt:t\ge0\}
\]

for a finite set \(F\).  With

\[
        m=\operatorname{lcm}(m_1,\ldots,m_J),
\]

membership in \(Z(r)\), and therefore its complement, is periodic modulo
\(m\) beyond a finite threshold.

Thus

\[
 \operatorname{supp}(r)\subseteq\mathbb P
 \Longrightarrow
 |\operatorname{supp}(r)|<\infty.
\]

For the fixed-level set \(r_k=c\), apply the same derivation to \(r_k-c\).

## D7. Bilinear nilpotent memorizer

For cutoff \(N\), let \(J_N\) be the \(N\times N\) shift

\[
        (J_N)_{j+1,j}=1,\qquad J_N^N=0.
\]

With

\[
        v=e_1,\qquad
        u=(\eta_1,\ldots,\eta_N)^{\mathsf T},
\]

\[
        J_N^{k-1}v=e_k
\]

for \(k\le N\), so

\[
        u^{\mathsf T}J_N^{k-1}v=\eta_k.
\]

The coefficient vector contains the target response explicitly.

## D8. Trace nilpotent memorizer

Let

\[
        (B_\eta)_{1k}=\eta_k
\]

and all other entries be zero.  Since

\[
        (J_N^{k-1})_{k1}=1,
\]

\[
 \operatorname{tr}(J_N^{k-1}B_\eta)
 =(J_N^{k-1})_{k1}(B_\eta)_{1k}
 =\eta_k.
\]

The response vanishes for \(k>N\).

## D9. Block adjacency and composition order

For the column-source block adjacency, now specializing the analytic layer
to \(A,B\in M_d(\mathbb C)\) on
\(\ell^2(V)\otimes\mathbb C^d\),

\[
\begin{aligned}
L_{s,A,B}(e_n\otimes\xi)
&=[n(n+1)]^{-s}e_{n+1}\otimes A\xi\\
&\quad+
\mathbf1_{\{n\ {\rm odd}\}}
[n(n+1)/2]^{-s}e_{(n+1)/2}\otimes B\xi.
\end{aligned}
\]

Starting at \(k\), the first \(k-1\) maps are \(A\) and the closing map is
\(B\).  Column composition is

\[
        BA^{k-1}.
\]

Trace cyclicity gives

\[
        \operatorname{tr}(BA^{k-1})
        =\operatorname{tr}(A^{k-1}B).
\]

No analogous cyclic simplification is asserted for a marked bilinear
coefficient; its word convention is frozen separately.

## D10. Nuclear upper bound

For \(\sigma=\Re s\),

\[
\begin{aligned}
\|L_{s,A,B}\|_1
&\le
\|A\|_1\sum_{n\ge2}[n(n+1)]^{-\sigma}\\
&\quad+
\|B\|_1\sum_{d\ge2}[(2d-1)d]^{-\sigma}.
\end{aligned}
\]

Both scalar sums have tail \(d^{-2\sigma}\), hence converge exactly above
\(\sigma=1/2\).

For necessity:

- if \(A\ne0\), compress to even sources and odd successor targets;
- if \(A=0\), \(B\ne0\), use the injective return map
  \(2d-1\mapsto d\).

The resulting singular-value sums diverge at and below the boundary.

## D11. Transient decider majorant

For computation length \(T(n)\),

\[
\sum_{n\ge2}\sum_{t=0}^{T(n)}
[n(t+2)]^{-\sigma}
\le
\left(\sum_{n\ge2}n^{-\sigma}\right)
\left(\sum_{j\ge2}j^{-\sigma}\right).
\]

The cemetery family has the same product majorant.  For \(\sigma>1\), the
whole operator is trace class independently of the growth of \(T(n)\).
Only accepted loops contribute to power traces.

## D12. Recurrent clock lower bound

If nonnegative roofs on an \(\ell(n)\)-cycle sum to \(\log n\), then

\[
 \min_j\tau_{n,j}\le\frac{\log n}{\ell(n)}.
\]

Therefore

\[
 \max_j e^{-\sigma\tau_{n,j}}
\ge n^{-\sigma/\ell(n)}.
\]

If \(\ell(n)/\log n\to\infty\), the right side tends to one.  Disjoint
cycles turn the selected edges into an orthogonal noncompactness witness.

For \(C_k\),

\[
        \ell(k)=k,\qquad
        \frac{k}{\log k}\to\infty.
\]

## D13. Factorial scale

Stirling gives

\[
\begin{aligned}
\log M_k
&=\log(2k-1)!-\log(k-1)!\\
&=k\log k+(2\log2-1)k+O(\log k).
\end{aligned}
\]

Thus the natural endpoint roof

\[
        2\log M_k
\]

has order \(2k\log k\), not \(\log k\).

## D14. Final ledger

Put

\[
        w_k=z^kM_k^{-2s},
\qquad
        P_k=BA^{k-1}.
\]

For a fixed complex block fiber, the complete local factor is

\[
        \Delta_k=\det_{\mathbb C^d}(I-w_kP_k),
\]

and

\[
 -\log\Delta_k
 =\sum_{r\ge1}\frac{w_k^r}{r}\operatorname{tr}(P_k^r).
\]

The first trace-log term is
\[
        w_k\operatorname{tr}(P_k),
\]
not the whole factor.  In particular,
\(\operatorname{tr}(P_k)=0\) does not imply \(\Delta_k=1\);
\(P_k=\operatorname{diag}(1,-1)\) gives \(\Delta_k=1-w_k^2\).
The marked bilinear response is separate from both expressions.

The full block coefficients are

\[
 \Delta_k
 =\sum_{j=0}^d(-w_k)^j\alpha_{j,k},
\qquad
 \alpha_{j,k}
 =\operatorname{tr}\!\left((\wedge^jB)(\wedge^jA)^{k-1}\right).
\]

Each \(\alpha_{j,k}\) is an LRS.  Therefore the set where the complete
block factor is nontrivial is a finite union of ultimately periodic
supports.  This is the valid full-factor no-go; it does not identify the
first trace term with the determinant.

For a distinct one-dimensional oracle deletion control, set
\[
        c_k=\mathbf1_{\mathbb P}(k),
\qquad
        \Delta_k^{\rm oracle}=1-w_kc_k.
\]
Only under this extra scalar assumption does the surviving product become

\[
        \prod_{p\in\mathbb P}(1-z^pM_p^{-2s}).
\]

The desired diagonal prime-loop determinant would be

\[
        \prod_{p\in\mathbb P}(1-zp^{-s}).
\]

Both the \(z\)-degree and the \(s\)-roof disagree before any comparison with
zeros.

## D15. Implementation invariants

An exact prototype must assert:

1. quotient words without prime calls;
2. exact eventual-period certificates;
3. zero Cayley–Hamilton residuals;
4. arbitrary matched finite-prefix realizations;
5. trace composition order and cyclicity;
6. separate successor/return nuclear sums;
7. absence of transient closed walks;
8. recurrent maximum-edge lower bounds;
9. exact factorial monomials;
10. deterministic byte identity and SHA-256 integrity.

No floating-point equality is accepted for D1–D9 or D14.
