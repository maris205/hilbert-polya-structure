# Proof Package — SD-C25

**Candidate:** SD-C25  
**Proof status:** complete for every manuscript theorem  
**Primary family:** Symbolic Dynamics  
**External theorem:** classical characteristic-zero
Skolem–Mahler–Lech, with source/corrigendum ledger in
[LITERATURE_AUDIT.md](LITERATURE_AUDIT.md)  
**Imported internal theorems:** Paper22 classification of \(Q=2\) cycles;
Paper19 transient wrapper; Paper20 recurrent clock dilution

## 0. Notation

Let

\[
 V=\{2,3,\ldots\},\qquad
 n\to d\iff d\ge2,\ d\mid n+1,
\]

and let

\[
        q(n,d)=\frac{n+1}{d}.
\]

Paper22's holonomy-two family is

\[
        C_k=(k,k+1,\ldots,2k-1),\qquad k\ge2.
\]

The unique least vertex marks the orbit.  Letter \(1\) denotes a quotient-one
successor edge and letter \(2\) denotes its quotient-two return edge.

For a characteristic-zero field \(\mathbb F\), fix

\[
        A,B\in M_d(\mathbb F),\qquad u,v\in\mathbb F^d
\]

and put

\[
 x_k=u^{\mathsf T}A^{k-1}Bv,\qquad
 y_k=\operatorname{tr}(A^{k-1}B).
\]

## 1. Canonical word and roof

### Theorem 1.1 — exact ordered word

For every \(k\ge2\),

\[
        W(C_k)=1^{k-1}2.
\]

**Proof.**  The first \(k-1\) edges have the form \(n\to n+1\), so

\[
        q(n,n+1)=\frac{n+1}{n+1}=1.
\]

The closing edge is \(2k-1\to k\), with

\[
        q(2k-1,k)=\frac{2k}{k}=2.
\]

The orbit contains \(k\) edges, and the unique least vertex fixes the stated
ordering. \(\square\)

### Theorem 1.2 — exact endpoint roof

Let

\[
        \tau(n,d)=\log(nd).
\]

Then

\[
 R(C_k)=2\log M_k,\qquad
 M_k=\prod_{n=k}^{2k-1}n
     =\frac{(2k-1)!}{(k-1)!}.
\]

The scalar cycle monomial is

\[
        z^kM_k^{-2s}.
\]

**Proof.**  Every vertex of a directed cycle occurs once as a source and
once as a target.  Therefore

\[
\begin{aligned}
 R(C_k)
 &=\sum_{(n,d)\in C_k}(\log n+\log d)\\
 &=2\sum_{n=k}^{2k-1}\log n
 =2\log M_k.
\end{aligned}
\]

There are \(k\) graph edges, hence marker \(z^k\). \(\square\)

## 2. Ultimately periodic sets and rational primes

### Definition 2.1

A set \(E\subseteq\mathbb N\) is ultimately periodic if some \(N,m\ge1\)
satisfy

\[
 n\ge N\Longrightarrow
 [n\in E\iff n+m\in E].
\]

### Lemma 2.2 — prime-only periodic sets are finite

If an ultimately periodic set \(E\) is contained in the rational primes,
then \(E\) is finite.

**Proof.**  Suppose \(E\) is infinite.  Choose \(p\in E\) beyond a tail
threshold \(N\), and let \(m\) be a tail period.  Repeated periodicity places
every \(p+tm\), \(t\ge0\), in \(E\).  At \(t=p\),

\[
        p+pm=p(1+m)
\]

is composite, a contradiction. \(\square\)

### Corollary 2.3

The rational primes are not ultimately periodic.  More strongly, no
infinite subset of them is ultimately periodic.

## 3. Fixed finite fibers

### Lemma 3.1 — powers in a finite semigroup

Let \(S\) be finite and \(a\in S\).  There exist \(\mu,\lambda\ge1\) such
that

\[
        a^{n+\lambda}=a^n\qquad(n\ge\mu).
\]

**Proof.**  Two elements among
\(a,a^2,\ldots,a^{|S|+1}\) agree, say \(a^i=a^j\) with \(i<j\).
Right multiplication by \(a^r\) gives
\(a^{i+r}=a^{j+r}\) for every \(r\ge0\).  Take
\(\mu=i\) and \(\lambda=j-i\). \(\square\)

### Theorem 3.2 — finite-semigroup no-go

Let \(\phi:\{1,2\}^{+}\to S\) be a morphism into a fixed finite semigroup.
For every subset \(H\subseteq S\),

\[
 E_{\phi,H}
 =\{k\ge2:\phi(1^{k-1}2)\in H\}
\]

is ultimately periodic.  If \(E_{\phi,H}\) is prime-only, it is finite.

Every scalar response \(f(\phi(1^{k-1}2))\) is eventually periodic.

**Proof.**  Set \(a=\phi(1)\) and \(b=\phi(2)\).  Then

\[
        \phi(1^{k-1}2)=a^{k-1}b.
\]

The convention is \(\phi(xy)=\phi(x)\phi(y)\), so multiplication follows
word-reading order.

Lemma 3.1 makes \(a^{k-1}\), hence \(a^{k-1}b\), eventually periodic.
Membership and scalar evaluation preserve equality.  Apply Lemma 2.2.
\(\square\)

### Corollary 3.3 — finite groups

For a fixed finite group, \(a^{k-1}b\) is periodic from the start with
period dividing \(\operatorname{ord}(a)\).  Membership, characters, class
functions, and fixed representation coefficients cannot have infinite
prime-only support.

### Theorem 3.4 — DFA and NFA no-go

A fixed DFA or NFA cannot accept exactly

\[
        \{1^{p-1}2:p\ \text{prime}\}
\]

or an infinite prime-only sublanguage of this form.

**Proof.**  A DFA supplies two transformations \(T_1,T_2\) of a finite
state set, acting on column states.  Function composition is right-to-left,
so its terminal state is

\[
        (T_2\circ T_1^{k-1})(q_0),
\]

which is eventually periodic by Theorem 3.2 applied to the finite
transformation semigroup.  For an NFA, determinize or use the finite
Boolean-relation semigroup.  Lemma 2.2 completes the proof. \(\square\)

## 4. Fixed-dimensional responses

### Theorem 4.1 — characteristic recurrence

Let

\[
 \chi_A(t)=t^d+c_{d-1}t^{d-1}+\cdots+c_0.
\]

Both \(x_k\) and \(y_k\) satisfy

\[
 r_{k+d}
 +c_{d-1}r_{k+d-1}
 +\cdots+c_0r_k=0
 \qquad(k\ge1).
\]

Their generating functions are

\[
 \sum_{k\ge1}x_kz^{k-1}
 =u^{\mathsf T}(I-zA)^{-1}Bv,
\]

\[
 \sum_{k\ge1}y_kz^{k-1}
 =\operatorname{tr}\bigl((I-zA)^{-1}B\bigr).
\]

**Proof.**  Cayley–Hamilton gives

\[
        A^d+c_{d-1}A^{d-1}+\cdots+c_0I=0.
\]

Multiply by \(A^{k-1}\) and apply the linear functional
\(X\mapsto u^{\mathsf T}XBv\) or
\(X\mapsto\operatorname{tr}(XB)\).  The generating functions follow from
the formal geometric series for \((I-zA)^{-1}\), whose adjugate formula is
rational. \(\square\)

### Theorem 4.2 — SML support obstruction

The zero set of \(x_k\) or \(y_k\) is a finite union of arithmetic
progressions and a finite set.  Its nonzero support is ultimately periodic.
If that support is contained in the rational primes, it is finite.

**Proof.**  Theorem 4.1 makes the response a linear recurrence sequence over
a characteristic-zero field.  The Skolem–Mahler–Lech theorem gives the
zero-set description.  Beyond the largest finite exception, membership in
the zero set is periodic modulo the least common multiple of the finitely
many progression moduli.  The complement is therefore ultimately periodic.
Lemma 2.2 excludes an infinite prime-only complement. \(\square\)

### Corollary 4.3 — fixed-level tests

For fixed \(c\in\mathbb F\), the set

\[
        \{k:r_k=c\}
\]

is ultimately periodic.

**Proof.**  The constant sequence is a linear recurrence sequence, so
\(r_k-c\) is one as well.  Apply Theorem 4.2 to its zero set. \(\square\)

### Corollary 4.4 — finite packages

Finite direct sums, fixed tensor products, fixed matrix coefficients, and
fixed trace contractions reduce to a fixed finite-dimensional linear
representation.  Any finite Boolean combination of exact zero and
fixed-level tests is ultimately periodic.

### Boundary 4.5

The theorem does not classify sign, positivity, threshold, cutpoint, phase
sector, or variable-tolerance recognition by recurrence sequences.  It does
not address nonlinear updates, positive characteristic, growing dimension,
or general infinite-dimensional representations.

## 5. Finite-cutoff memorization

### Theorem 5.1 — bilinear nilpotent memorizer

Fix \(N\ge1\) and arbitrary
\(\eta_1,\ldots,\eta_N\in\mathbb F\).  Let

\[
 J_Ne_j=e_{j+1}\ (j<N),\qquad J_Ne_N=0,
\]

and set

\[
 v=e_1,\qquad B=I,\qquad
 u=\sum_{j=1}^N\eta_je_j.
\]

Then

\[
 u^{\mathsf T}J_N^{k-1}Bv
 =
 \begin{cases}
 \eta_k,&1\le k\le N,\\
 0,&k>N.
 \end{cases}
\]

**Proof.**  For \(k\le N\), \(J_N^{k-1}e_1=e_k\).  For \(k>N\),
\(J_N^{k-1}=0\). \(\square\)

### Theorem 5.2 — trace nilpotent memorizer

Let \(B_\eta\) have first-row entries

\[
        (B_\eta)_{1k}=\eta_k,\qquad 1\le k\le N,
\]

and all other entries zero.  Then

\[
 \operatorname{tr}(J_N^{k-1}B_\eta)
 =
 \begin{cases}
 \eta_k,&1\le k\le N,\\
 0,&k>N.
 \end{cases}
\]

**Proof.**  The only nonzero contribution to the trace is

\[
 (J_N^{k-1})_{k1}(B_\eta)_{1k}=\eta_k.
\]

Nilpotence handles \(k>N\). \(\square\)

### Corollary 5.3 — PROVES_TOO_MUCH

Prime indicators, square indicators, powers of two, Fibonacci membership,
seeded bit strings, hashes, and arbitrary rational values all have exact
finite-prefix realizations of the same dimension.  The data are stored in
\(u\) or \(B_\eta\).  The construction is not prime-selective.

The quantifiers are

\[
\forall N\ \forall(\eta_1,\ldots,\eta_N)\
\exists\text{ an }N\text{-dimensional realization},
\]

not the existence of one fixed finite-dimensional realization for all
\(k\).

## 6. Same-object trace-class operator

### Definition 6.1

On

\[
        \mathcal H=\ell^2(V)\otimes\mathbb C^d,
\]

fix \(A,B\in M_d(\mathbb C)\) and define

\[
\begin{aligned}
 L_{s,A,B}(e_n\otimes\xi)
 &=(n(n+1))^{-s}e_{n+1}\otimes A\xi\\
 &\quad+
 \mathbf1_{\{n\ {\rm odd}\}}
 \bigl(n(n+1)/2\bigr)^{-s}
 e_{(n+1)/2}\otimes B\xi.
\end{aligned}
\]

Write \(\sigma=\Re s\).

### Theorem 6.2 — sharp nuclear domain

If \(A,B\) are fixed and not both zero, then

\[
        L_{s,A,B}\in\mathcal S_1
        \iff \sigma>\frac12.
\]

On this half-plane the family is \(\mathcal S_1\)-valued holomorphic.

**Proof, sufficiency.**  Split \(L=S_A+R_B\) into successor and return
parts.  Their edge-rank-one expansions give

\[
 \|S_A\|_1
 \le \|A\|_1
 \sum_{n\ge2}[n(n+1)]^{-\sigma},
\]

\[
 \|R_B\|_1
 \le \|B\|_1
 \sum_{d\ge2}[(2d-1)d]^{-\sigma}.
\]

Both sums are comparable to
\(\sum n^{-2\sigma}\), hence converge for \(\sigma>1/2\).

**Proof, necessity when \(A\ne0\).**  Compress the domain to even source
vertices and the range to odd target vertices.  Even sources have no
quotient-two return edge, so the compression is the block weighted shift

\[
 e_{2m}\otimes\xi
 \longmapsto
 [(2m)(2m+1)]^{-s}e_{2m+1}\otimes A\xi.
\]

Its singular values are the products of the scalar weights with the
singular values of \(A\).  Its trace norm is

\[
 \|A\|_1\sum_{m\ge1}[(2m)(2m+1)]^{-\sigma},
\]

which diverges for \(\sigma\le1/2\).  A compression of an
\(\mathcal S_1\) operator would remain in \(\mathcal S_1\).

**Proof, necessity when \(A=0\), \(B\ne0\).**  The map
\(2d-1\mapsto d\) is injective in source and target.  Thus

\[
 \|L_{s,0,B}\|_1
 =\|B\|_1\sum_{d\ge2}[(2d-1)d]^{-\sigma},
\]

which again diverges for \(\sigma\le1/2\).

Local uniform convergence of the rank-one series on compact subsets of
\(\sigma>1/2\) gives \(\mathcal S_1\)-valued holomorphy. \(\square\)

### Corollary 6.3 — Fredholm determinant

For \(\Re s>1/2\),

\[
        D_{A,B}(s,z)=\det(I-zL_{s,A,B})
\]

is a genuine Fredholm determinant, entire in \(z\).

### Proposition 6.4 — canonical block ledger

With column-source composition, a circuit around \(C_k\) yields
\(BA^{k-1}\).  Hence

\[
 \operatorname{tr}(BA^{k-1})
 =\operatorname{tr}(A^{k-1}B).
\]

Put

\[
        w_k=z^kM_k^{-2s}.
\]

The first canonical trace-log term is

\[
        w_k\operatorname{tr}(BA^{k-1}).
\]

The complete local block factor and its normalized logarithm are

\[
 \Delta_k(s,z)
 =\det_{\mathbb C^d}(I-w_kBA^{k-1}),
\]

\[
 -\log\Delta_k(s,z)
 =\sum_{r\ge1}\frac{w_k^r}{r}
  \operatorname{tr}\!\left((BA^{k-1})^r\right).
\]

Thus a zero first trace does not delete the block factor.  For
\(BA^{k-1}=\operatorname{diag}(1,-1)\), the first trace vanishes while
\(\Delta_k=1-w_k^2\).  The bilinear word response is a separately marked
observable, realized by the frozen word convention or by transposing the
block representation and swapping endpoint vector/covector.  It is not a
Fredholm coefficient.

### Proposition 6.5 — complete block-factor support

Expand

\[
 \Delta_k(s,z)=\sum_{j=0}^d(-w_k)^j\alpha_{j,k},
\qquad
 \alpha_{j,k}
 =\operatorname{tr}\!\left((\wedge^jB)(\wedge^jA)^{k-1}\right).
\]

For each fixed \(j\), the coefficient \(\alpha_{j,k}\) is an LRS.  Hence
the set on which \(\Delta_k\) is nontrivial as a polynomial in \(w_k\) is
ultimately periodic; if it is prime-only, it is finite.

**Proof.**  The determinant coefficient identity is
\(\alpha_{j,k}=\operatorname{tr}(\wedge^j(BA^{k-1}))\).  Exterior powers
preserve multiplication, and Cayley--Hamilton applies to \(\wedge^jA\).
SML makes each nonzero support ultimately periodic.  The nontrivial-factor
set is the finite union of those supports for \(1\le j\le d\). \(\square\)

## 7. Factorial-roof obstruction

### Theorem 7.1 — neither block factors nor scalar deletion change the roof

Every term in the block trace-log expansion of Proposition 6.4 has the
base monomial power

\[
        w_k^r=z^{kr}M_k^{-2sr}.
\]

Separately, suppose a one-dimensional oracle deletion control is imposed
after the source is frozen:

\[
        c_k=\mathbf1_{\mathbb P}(k),
\qquad
        \Delta_k^{\rm oracle}=1-w_kc_k.
\]

This is not inferred from a block trace.  Its product over surviving
canonical cycles is

\[
 \prod_{p\in\mathbb P}
 \left(1-z^pM_p^{-2s}\right),
\]

not

\[
        \prod_{p\in\mathbb P}(1-zp^{-s}).
\]

**Proof.**  Proposition 6.4 gives the block formula.  The separately
assumed scalar control can delete a factor, but neither construction changes
the base graph length or endpoint roof established in Theorems 1.1–1.2.
\(\square\)

### Proposition 7.2 — factorial asymptotic

\[
 \log M_k
 =k\log k+(2\log2-1)k+O(\log k).
\]

**Proof.**  Apply Stirling's formula to
\(\log(2k-1)!-\log(k-1)!\).  Replacing \(2k-1,k-1\) by \(2k,k\)
affects only the \(O(\log k)\) remainder:

\[
\begin{aligned}
\log M_k
 &=2k\log(2k)-2k-k\log k+k+O(\log k)\\
 &=k\log k+(2\log2-1)k+O(\log k).
\end{aligned}
\]
\(\square\)

## 8. Licensed countable total-decider wrappers

The next statements concern only the Paper19 transient and Paper20
recurrent architectures.  They are not a classification of all countable
symbolic extensions.

### Theorem 8.1 — transient pruning

Let \(S\subseteq\{2,3,\ldots\}\) be decided by a total deterministic
machine with finite runtime \(T(n)\).  For each \(n\), put its computation
on a finite one-way chain; send acceptance to a self-loop of weight
\(n^{-s}\) and rejection to a one-way acyclic cemetery ray.  Give the
\(t\)-th computation edge weight

\[
        [n(t+2)]^{-s}
\]

and the \(j\)-th cemetery edge weight

\[
        [n(j+1)]^{-s}.
\]

For \(\sigma=\Re s>1\), the weighted adjacency is trace class and

\[
 \operatorname{Tr}L_{S,s}^r
 =\sum_{n\in S}n^{-rs},
\]

\[
 \det(I-zL_{S,s})
 =\prod_{n\in S}(1-zn^{-s}).
\]

**Proof.**  The edge-rank-one nuclear majorant is

\[
\begin{aligned}
\|L_{S,s}\|_1
 &\le
 \sum_{n\ge2}\sum_{t=0}^{T(n)}[n(t+2)]^{-\sigma}\\
 &\quad+
 \sum_{n\notin S}\sum_{j\ge1}[n(j+1)]^{-\sigma}
 +\sum_{n\in S}n^{-\sigma}\\
 &\le
 2\left(\sum_{n\ge2}n^{-\sigma}\right)
  \left(\sum_{j\ge2}j^{-\sigma}\right)
 +\sum_{n\ge2}n^{-\sigma}<\infty.
\end{aligned}
\]

Every computation and cemetery edge is acyclic.  Closed walks occur only on
accepted loops, giving the trace and determinant formulas. \(\square\)

### Corollary 8.2 — selector tautology

Theorem 8.1 works for every total decidable support, not only primes.
Computation is determinant-invisible and pruning leaves diagonal selected
loops.  The construction is PROVES_TOO_MUCH.

### Theorem 8.3 — recurrent clock dilution

Let accepted computations be closed into pairwise disjoint deterministic
cycles of lengths \(\ell(n)\).  Give them nonnegative edge roofs
\(\tau_{n,j}\) with

\[
        \sum_{j=1}^{\ell(n)}\tau_{n,j}=\log n.
\]

If along an infinite accepted subsequence

\[
        \frac{\ell(n)}{\log n}\to\infty,
\]

then the whole weighted vertex adjacency is noncompact for every fixed
\(\sigma>0\).

**Proof.**  Some edge has

\[
 \tau_{n,j}\le\frac{\log n}{\ell(n)},
\]

so its weight obeys

\[
 e^{-\sigma\tau_{n,j}}
 \ge n^{-\sigma/\ell(n)}
 \longrightarrow1.
\]

Select one such edge on each disjoint cycle.  Its source basis vectors are
orthonormal, and their images have mutually orthogonal target components
with norms bounded away from zero.  The images have no norm-convergent
subsequence, contradicting compactness. \(\square\)

### Corollary 8.4 — cofactor-spine clock dilution

For \(C_k\), \(\ell(k)=k\).  Forcing total roof \(\log k\) gives

\[
        \frac{k}{\log k}\to\infty,
\]

so Theorem 8.3 applies.

### Proposition 8.5 — first return changes the marker

Inducing on one marked vertex per accepted cycle replaces the product of
edge weights by \(n^{-s}\), but maps

\[
        z^{\ell(n)}\longmapsto z.
\]

For \(C_k\), it erases \(1^{k-1}2\) and maps \(z^k\) to \(z\).
The return operator is not the unchanged vertex adjacency.

## 9. Route implication

### Theorem 9.1 — ordered-spine closure

Within the frozen model class, no fixed finite semigroup/automaton or fixed
characteristic-zero linear fiber selects prime-only canonical cycles.
Growing finite fibers memorize arbitrary data.  Within the two licensed
Paper19/Paper20 architectures, exact countable wrappers either compile a
selector into transient computation, lose compactness after recurrent
closure under a short roof, or change the object under induction.
Independently, the full block ledger and the separate scalar deletion
control retain the factorial endpoint roof and length marker.

Therefore the route tuple is

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}),
\]

with

\[
        \mathrm{ROUTE\_A\_REJECTED}.
\]

**Proof.**  A0 follows from the source-derived quotient word.  A1 is weak
because the canonical family is exact but not prime-selective.  A2 follows
from Theorem 6.2 and Corollary 6.3.  A3 fails by Theorems 3.2, 4.2, 5.1–5.2,
Proposition 6.5, Theorem 7.1, and the licensed wrapper Theorems 8.1–8.3.
We construct no critical-line or Hilbert--Pólya mechanism, so the candidate
receives the evaluation label A4_FAIL.  This is not a theorem that such a
mechanism cannot exist. \(\square\)

## 10. Dependency and claim firewall

| Statement | Status | Dependency |
|---|---|---|
| \(Q=2\) cycle classification | imported | Paper22 |
| ordered word and roof | proved here | graph arithmetic |
| finite-semigroup/DFA periodicity | proved here | pigeonhole |
| weighted response recurrence | proved here | Cayley–Hamilton |
| exact support periodicity | external theorem | SML |
| growing nilpotent realization | proved here | explicit matrices |
| finite-block \(\mathcal S_1\) threshold | proved here/inherited | Paper21 spine plus block compression |
| transient selector pruning | imported and restated | Paper19 |
| recurrent clock dilution | imported and restated | Paper20 |
| factorial mismatch and route verdict | proved here | same-object ledger |

No proof uses Riemann-zero data.
