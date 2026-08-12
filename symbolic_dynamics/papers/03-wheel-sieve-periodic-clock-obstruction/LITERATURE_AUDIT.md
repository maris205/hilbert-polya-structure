# Literature Audit: Periodic Clocks, Cohomology, and Prime-Sieve Symbolics

Search date: 2026-08-12

Primary system family: **Symbolic Dynamics only**
Route B: **locked**

## Audit conclusion

The elementary contradiction used in this project is not presented as a new
general theorem. If \(d\) is a single-valued observable on a system \((Y,S)\),
then

\[
\sum_{j=0}^{m-1}
  \bigl(d(S^{j+1}y)-d(S^jy)\bigr)
=d(S^my)-d(y)=0
\]

on every \(m\)-periodic point. This is the necessary, telescoping direction
of the periodic-orbit obstruction familiar from Livšic cohomology. For
integer-valued continuous observables on zero-dimensional systems, the same
principle sits naturally in ordered cohomology: finite-orbit traces annihilate
coboundaries. Neither that identity nor the abstract statement that a
genuinely drifting clock cannot close around a cycle is claimed as original.

The project contribution is narrower and wheel-sieve specific. Starting from
the already proved endogenous multiplier sequence of the graded wheel source,
it packages:

1. the fiber-consistency criterion for exact clock decoding;
2. the direct-image periodic-point obstruction with no topology;
3. a closure theorem based on separation of lagged clock pairs from the
   diagonal;
4. compactness and clock-topology controls;
5. explicit hypothesis-deletion counterexamples; and
6. the resulting Route-A **THEOREM_STOP** for inherited exact-clock
   stationarizations.

This is a claim of scoped synthesis and application, not a claim that the
general cohomological mechanism was previously unknown.

## Source-to-claim ledger

| Source | What it supports here | What it does not support |
|---|---|---|
| G. A. Hedlund, “Endomorphisms and automorphisms of the shift dynamical system,” *Mathematical Systems Theory* 3 (1969), 320–375, [DOI](https://doi.org/10.1007/BF01691062) | The standard finite-alphabet category in which continuous shift-commuting maps are described by local coding rules. It supplies context for calling a continuous equivariant observation a symbolic recoding. | It does not prove the wheel-clock theorem, treat the noncompact graded source used here, or make exact arithmetic decoding automatic. |
| A. N. Livšic (English record: A. N. Livshits), “Cohomology of dynamical systems,” *Mathematics of the USSR-Izvestiya* 6(6) (1972), 1278–1301, [DOI](https://doi.org/10.1070/IM1972v006n06ABEH001919) | The classical cohomological framework and periodic-orbit criterion for coboundaries in hyperbolic/Markov settings. We use only the elementary necessary direction: a coboundary telescopes to zero on a periodic orbit. | We do not invoke the Livšic converse, a regularity theorem, hyperbolicity, or a claim that the wheel source satisfies those hypotheses. |
| W. Parry and M. Pollicott, *Zeta Functions and the Periodic Orbit Structure of Hyperbolic Dynamics*, Astérisque 187–188 (1990), [Numdam](https://www.numdam.org/item/AST_1990__187-188__1_0/) | Standard periodic-orbit and suspension-flow language: a roof is an increment accumulated along a periodic base orbit, and a closed-orbit weight is an orbit sum. | It does not identify rational primes with wheel periodic data or justify a zeta function or determinant for this theorem-stopped mechanism. |
| M. Boyle and D. Handelman, “Orbit equivalence, flow equivalence and ordered cohomology,” *Israel Journal of Mathematics* 95 (1996), 169–210, [DOI](https://doi.org/10.1007/BF02761039) | Ordered first cohomology for zero-dimensional dynamics, including quotienting integer-valued observables by coboundaries and evaluating classes on finite orbits. This is the closest categorical language for the integer-clock telescoping audit. | It is not a direct proof of our closure theorem, and its compact-homeomorphism setting is not silently imposed on the one-sided graded wheel source. |
| B. Heeren, “On The Nature Of Primes: A deterministic, endogenous, non-stationary S-adic Automaton for the sieve of Eratosthenes,” SSRN working paper 6015434 (2026), [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6015434) | Direct topical prior art for a deterministic, endogenous, non-stationary symbolic realization of the sieve of Eratosthenes over a finite alphabet. It blocks any claim that this project is the first symbolic or non-stationary automaton treatment of prime sieving. | Its public abstract does not supply this exact-decoder factor theorem, the lag-pair closure criterion, or a stationarization obstruction for the frozen wheel tail-path source. It is identified explicitly as a non-peer-reviewed working paper; manuscript-level overlap should be rechecked before submission. |

## Positioning of the mechanism

### Direct images are controlled by fiber consistency

For a map \(\pi:X\to Y\), a decoder \(d:\pi(X)\to C\) with
\(d\circ\pi=\kappa\) exists exactly when \(\kappa\) is constant on each
\(\pi\)-fiber. If \(y=\pi(x)\) is \(m\)-periodic and
\(\pi\circ\sigma=S\circ\pi\), then

\[
\pi(\sigma^m x)=S^m\pi(x)=\pi(x).
\]

The two source points lie in one fiber, but the wheel grading gives
\(\kappa(\sigma^m x)\ne\kappa(x)\). No continuity, locality, finite alphabet,
compactness, or surjectivity is used. Surjectivity is needed only to conclude
that the whole target is aperiodic.

When subtraction is available, the same contradiction can be written with
\(a=d\circ S-d\). Its target-cycle sum is zero, while exact source lifting
would give

\[
\sum_{j=0}^{m-1}a(S^j\pi(x))
=\kappa(\sigma^m x)-\kappa(x)\ne0.
\]

This explains the Livšic/ordered-cohomology ancestry without claiming their
deeper converse theorems.

### Closures need a separate inheritance theorem

The image proof says nothing about a periodic point newly appearing in
\(Y_0=\overline{\pi(X)}\setminus\pi(X)\). For fixed \(m\), set

\[
E_m=\{(\kappa(x),\kappa(\sigma^m x)):x\in X\}\subset C\times C.
\]

If \(S:Y_0\to Y_0\) and a total decoder \(d:Y_0\to C\) are continuous and
\(\overline{E_m}\cap\Delta_C=\varnothing\), then continuity of
\(F_m=(d,d\circ S^m)\) transfers the separation from the dense image to its
closure. An \(m\)-periodic boundary point would map to the diagonal, a
contradiction.

This short topological lemma is proved in full and is not attributed to any
of the contextual references. For \(C=\mathbb N\) with the discrete topology,
\(E_m\) is closed and disjoint from the diagonal. For the usual real clocks
\(q_{k+1}\) and \(\log q_{k+1}\), it is locally finite and escapes to
infinity. In the one-point compactification
\(\mathbb N\cup\{\infty\}\), however, the lag pairs converge to
\((\infty,\infty)\); continuity alone then permits a boundary fixed point.

### Compact target and compactified clock are different

- If the recoded phase space \(Y_0\) is compact and
  \(d:Y_0\to\mathbb N_{\mathrm{disc}}\) is continuous, then \(d(Y_0)\) is
  compact in a discrete space and hence finite. It cannot contain the
  unbounded exact wheel clock.
- If instead the clock codomain is compactified by adding \(\infty\), the
  exact decoder on a dense image can extend continuously to a boundary fixed
  point. The closure theorem is not contradicted: its lag-pair separation
  hypothesis fails at \((\infty,\infty)\).

### Roofs are increments, not absolute clock labels

Parry–Pollicott's suspension framework makes the relevant distinction clear.
A positive roof \(r(y)\) is summed repeatedly around a periodic base orbit;
the accumulated time after one lap need not be zero. There is no general
obstruction to a periodic base carrying a roof.

The frozen wheel observable \(\tau=\log\kappa\) is instead an absolute
source-level label. Exact decoding on a periodic target would require one
revisited state to equal both \(\log q_{k+1}\) and
\(\log q_{k+m+1}\). A new rule independently assigning a positive
\(\log p\) roof to target cycles is a different arithmetic mechanism and must
pass A0 independently.

## Direct-prior collision audit

The Heeren working paper changes the novelty language in three concrete ways.

1. The manuscript must not claim the first finite-alphabet, endogenous, or
   non-stationary symbolic sieve.
2. The natural non-stationarity of a prime sieve is background, not a new
   discovery of this project.
3. The contribution to defend is the obstruction to passing the already
   frozen wheel prime clock through exact shift-compatible images and
   continuous orbit closures, together with the explicit failure modes.

The two systems are not declared equivalent. The present source is the graded
wheel tail-path system with the multiplier recurrence proved in Paper 01;
Heeren's public description uses an S-adic automaton with shift, expansion,
and filtering on a growing tape. No equivalence or inequivalence theorem is
asserted.

## Literature-limited novelty statement

The strongest admissible positioning sentence is:

> The universal periodic-coboundary contradiction is classical. Our
> contribution is a source-specific obstruction package showing how the
> endogenous wheel-sieve prime clock fails to survive periodic
> stationarization under direct exact decoding or continuous closure
> inheritance, and which deleted hypotheses permit cycles to return.

This audit does not prove that no earlier paper has an equivalent
source-specific formulation. It provides a defensible claim boundary and a
finite set of primary/direct sources to check again before venue submission.

## Scope and route discipline

- All developed mathematics remains in Symbolic Dynamics.
- No determinant, zeta equality, operator, or Hilbert–Pólya claim is inferred
  from cohomological language.
- Route B remains locked.
- Cross-family analogies are recorded only as **ROUND2_CLUE** and receive no
  argument or evidentiary credit.
