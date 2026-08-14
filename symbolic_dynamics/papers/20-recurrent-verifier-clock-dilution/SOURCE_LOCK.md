# SOURCE LOCK — SD-C22

**Candidate:** SD-C22
**Title:** *Recurrent Verifier Cycles and Clock Dilution*
**Family:** Symbolic Dynamics only
**Lock date:** 2026-08-14

## 1. Arithmetic source

For the finite full shift $F_n=A_n^{\mathbb Z}$, the only arithmetic
instructions are

\[
F_m\boxtimes F_n\cong F_{mn},\qquad
F_m\boxplus F_n\cong F_{m+n},\qquad h(F_n)=\log n.
\]

Here $\boxplus$ means alphabet-sum; it is not asserted to be a categorical
coproduct of subshifts. Successor, multiplication, equality, and order are the
expanded relations frozen in SD-C21. Prime tables, factor-existence guards,
von Mangoldt weights, and zeta-zero data are forbidden.

## 2. Contracted recurrent verifier

For every $n\ge2$, retain the reachable states
$I_n,T_{n,d},Q_{n,d,q},R_{n,k}$ and transitions

\[
I_n\to T_{n,2},
\]

\[
T_{n,d}\to
\begin{cases}
I_n,&d^2>n,\\
Q_{n,d,2},&d^2\le n,
\end{cases}
\qquad
Q_{n,d,q}\to
\begin{cases}
Q_{n,d,q+1},&dq<n,\\
R_{n,1},&dq=n,\\
T_{n,d+1},&dq>n,
\end{cases}
\]

and $R_{n,k}\to R_{n,k+1}$. The terminal successful transition returns
directly from $T_{n,d}$ to $I_n$; there is no separate accept vertex. This
contracted convention is immutable.

For a prime $p$ and $m=\lfloor\sqrt p\rfloor$, the accepted component is one
simple cycle $\Gamma_p$ of exact graph length

\[
\boxed{\ell(p)=2+\sum_{d=2}^{m}\left\lceil\frac pd\right\rceil
=2+\sum_{d=2}^{m}\left(1+\left\lfloor\frac pd\right\rfloor\right).}
\]

Thus $\ell(5)=5$ and $\ell(4093)=15293$. Distinct inputs have disjoint state
copies. Composite paths enter one-way cemetery rays and never close.

## 3. Phase space and roofs

- Phase space: the one-sided edge shift $X_{G^{\circlearrowleft}}^+$.
- Natural operator space: $\mathcal H=\ell^2(V)$ with counting measure.
- Accepted-cycle roof class: finite real $\tau(e)\ge0$ satisfying
  \[
  \sum_{e\in\Gamma_p}\tau(e)=h(F_p)=\log p.
  \]
- Primary representative: the strictly positive uniform allocation
  $\tau(e)=\log p/\ell(p)$ on $\Gamma_p$.
- Composite computation/cemetery roofs: the summable SD-C21 source roofs.

Only the total $h(F_p)$ is source-visible. Its distribution around a cycle is
a frozen `MODELING_CHOICE`. Zero edge clocks are permitted in the operator
theorem; a standard suspension interpretation uses positive clocks that may
approach zero.

## 4. Frozen operator and determinant convention

For $s\in\mathbb C$ with $\sigma=\operatorname{Re}s>0$,

\[
L_s\delta_u=e^{-s\tau(u\to v)}\delta_v.
\]

$L_s$ is called the source-weighted vertex adjacency. It must not be called a
Ruelle transfer operator. The requested same-object determinant is the
ordinary Hilbert-space Fredholm determinant $\det_{\mathcal H}(I-zL_s)$,
which is admitted only when $L_s\in\mathcal S_1$.

The raw periodic-orbit product

\[
D_{\mathrm{orb}}^{\mathrm{raw}}(s,z)
=\prod_p(1-z^{\ell(p)}p^{-s})
\]

is a separate combinatorial object. At $z=1$ it equals $1/\zeta(s)$ for
$\operatorname{Re}s>1$, but it may not be relabeled as the Fredholm
determinant of the noncompact whole adjacency.

## 5. First-return object

On the section $\Sigma=\{I_p:p\text{ prime}\}$, the induced operator is

\[
R_s\delta_{I_p}=p^{-s}\delta_{I_p}.
\]

It is trace class for $\operatorname{Re}s>1$ and is unitarily equivalent to
the Paper 04 prime-loop diagonal. Its ordinary return-step marker produces
$1-zp^{-s}$, whereas the original graph-step marker produces
$1-z^{\ell(p)}p^{-s}$. They agree at $z=1$, or after explicitly transporting
$z^{\ell(p)}$ through induction.

## 6. Evidence lock

The integrated deterministic prototype is evidence for implementation only:

- 12/12 tests passed;
- all 564 primes through 4096 matched the exact length formula;
- $p=4093$ has $\ell(p)=15293$;
- at $\sigma=2$, its optimal largest edge weight is
  $0.9989128997668932$;
- the SD-C21 source-roof clock divided by $\log p$ is approximately
  $28780.78337618892$ at the largest prime;
- raw and induced products agree exactly at $z=1$ and differ at $z=1/3$;
- padded square, power-of-two, Fibonacci, and hash controls reproduce the
  obstruction.

No target-zero data are used.

## 7. Verdict lock

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED

GO_RECURRENT_VERIFIER_ORBIT_LEDGER
GO_CLOCK_DILUTION_THEOREM
STOP_WHOLE_VERTEX_COMPACTNESS
STOP_WHOLE_VERTEX_FREDHOLM_DETERMINANT
FIRST_RETURN_COLLAPSE
SELECTOR_TAUTOLOGICAL
PROVES_TOO_MUCH
```

The result does not exclude overlapping recurrent grammars, signed or
matrix-valued cancellations, anisotropic quotient spaces, semifinite or
regularized determinants, or geometric carriers outside Symbolic Dynamics.
