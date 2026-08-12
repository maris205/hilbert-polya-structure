# Periodic-Clock Theorem Source Lock

Date: 2026-08-12

Status: **FROZEN — THEOREM AUDIT COMPLETE**

Candidate ID: **not assigned**

Primary family: **Symbolic Dynamics only**

Route B: **locked**

## 1. Source system

Let

$$
X=\bigsqcup_{k\ge 0}X_k
$$

be the wheel-sieve one-sided tail-path space from `SD-C05`.  The shift
$\sigma:X\to X$ deletes the first edge and satisfies

$$
\sigma(X_k)\subseteq X_{k+1}.
$$

Write $\ell(x)=k$ for $x\in X_k$.  The wheel recursion generates

$$
Q_0=1,\qquad Q_1=q_1=2,
\qquad
q_{k+1}=\min\{n>q_k:\gcd(n,Q_k)=1\},
\qquad
Q_{k+1}=Q_kq_{k+1}.
$$

Paper 01 proves that $q_k$ is the $k$-th rational prime.  Define the exact
integer clock and derived logarithmic clock value by

$$
\kappa(x)=q_{\ell(x)+1},
\qquad
\tau(x)=\log \kappa(x).
$$

Thus $\kappa(\sigma^m x)\ne\kappa(x)$ for every $m\ge 1$.

## 2. Exact-clock semiconjugate image

The first theorem class consists of a set $Y$, a self-map $S:Y\to Y$, and a
map $\pi:X\to Y$ satisfying

$$
\pi\circ\sigma=S\circ\pi.
$$

A single-valued image decoder for a frozen clock sequence
$a_k\in C$ is a function $d:\pi(X)\to C$ satisfying

$$
d(\pi(x))=a_{\ell(x)}.
$$

The two wheel specializations are $C=\mathbb N$, $a_k=q_{k+1}$ and
$C=\mathbb R$, $a_k=\log q_{k+1}$.
No topology and no extension of $d$ beyond $\pi(X)$ are needed for the image
theorem.  A factor or quotient is the surjective case $Y=\pi(X)$.

## 3. Orbit-closure recoding

The closure theorem adds the following hypotheses:

- $Y$ is a topological space;
- $S:Y\to Y$ is continuous;
- the clock codomain $C$ is a topological space and, for each $m\ge1$, the
  closure in $C\times C$ of
  $\{(\kappa(x),\kappa(\sigma^m x)):x\in X\}$ misses the diagonal;
- $d:Y\to C$ is continuous and total;
- the target is $Y_0=\overline{\pi(X)}$ with the restricted shift.

The map $\pi$ need not be continuous for the stated closure argument, although
a standard topological recoding normally requires it.

## 4. Path-window decoders

A target point already represents an entire symbolic path.  Consequently a
state, edge, finite-window, variable-window, or continuous infinite-memory
clock rule is covered whenever it defines a total function $d:Y\to C$
and commutes with time through evaluation on $S^ny$.

For $C=\mathbb N$ with the discrete topology, or for the usual real-valued
clocks $q_{k+1}$ and $\log q_{k+1}$, this separation condition holds.  It
fails if one compactifies the clock by adding an infinity point to which all
prime values converge.  The closure theorem does not cover a discontinuous
decoder.  The image theorem does not require decoder continuity.

## 5. Forbidden escape mechanisms

- stored prime or Riemann-zero tables;
- hard-coded $(q_k)$ or $(Q_k)$ sequences;
- prime-indexed components;
- reset or wrap edges;
- hand-assigned $\log p$ roofs;
- cutoff-dependent rules;
- concatenation of transitions with incompatible source representatives;
- borrowing the determinant of `SD-C04` or the zeta quotient of `SD-C06`;
- calling a clock on a boundary periodic point “inherited” when it is not the
  continuous extension of the source clock;
- Route B.

## 6. Analytic layer

```text
determinant_convention: not_defined
A2: A2_NOT_TESTABLE
route_b_invocation_allowed: false
```

No determinant may be introduced unless a separately frozen same-object
candidate establishes both arithmetic fidelity and a primitive-orbit ledger.

## 7. Outcome rule

If the image and closure theorems survive proof and adversarial review, record
`THEOREM_STOP` for exact-clock shift-compatible factors and for continuous
orbit-closure recodings whose lagged clock-pair closures miss the diagonal.
This is a scoped obstruction, not a theorem about every symbolic system.

A proposed escape is eligible for a new source lock only if it supplies one
fixed, level-blind arithmetic rule on its periodic points without using any
forbidden mechanism.  It does not inherit `SD-C05`'s A0 verdict.  No `SD-C07`
identifier is assigned at this stage.
