# Recurrent divisor testing with a complete arithmetic packet ledger

**Paper ID:** 140-cyclic-divisor-counter.  
**Candidate ID:** ANG-20260915-CDC01.  
**Date:** 2026-09-15.  
**Status:** ADVANCE — EXACT MARKED RETURN SELECTOR, COMPLETE PACKETS, LOCAL ORDINARY ZETA.  
**Route state:** broadened T0--T3 owner audit only; classical A0/A1/A2 NOT
APPLICABLE; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

A reversible cyclic scan tests every proper divisor of every integer in one
uniform countable carrier. It records a witness in a counter whose modulus
prevents cancellation of the complete scan count. The first scan-phase return
has zero counter displacement exactly on prime-labelled components. Every
state is retained: if a(n) is the proper-divisor count, there are
g(n)=gcd(n,a(n)) primitive cycles over n, each of length
T(n)=max(1,n-2)n/g(n). These are genuine closed orbits of the same unit-roof
suspension, with repetition length rT(n). Their complete ordinary product is
holomorphic and nonzero for Re(s)>0. The result is a marked arithmetic return
selector, not one primitive orbit per prime, a logarithmic prime clock,
classical symplectic geometry, or a formal Route result. Divisor suppression,
constant forcing, and modulo-two aliasing controls delimit the construction.

## 1. Frozen identity and lineage

The [version-1 card](candidate-card.md) precedes this audit. No definition,
roof, quotient, or multiplicity was changed to obtain the result.

| Item | Owner and exact specification | Result |
| --- | --- | --- |
| Carrier | Y, the disjoint union of all n>=2 phase-counter fibres | Countable discrete; no selected prime inputs |
| Action | The fixed local divisor-test permutation F below | Bijective; homeomorphism |
| Broadened owner | Transformation groupoid Y crossed with Z | Discrete, locally compact Hausdorff and étale |
| Arithmetic mechanism | Local proper-divisor witness increments at successive scan phases | Executed by F, not a supplied completed prime mask |
| Observable | Conserved n, scan phase j, complete counter c | Marked first-scan return displacement |
| Clock and flow | Unit roof over this same F | Complete suspension; no logarithmic replacement |
| Packets | Every least-period F-cycle modulo cyclic phase | Multiplicity g(n); period T(n) |
| Analytic owner | Ordinary unweighted product of all these packets | Re(s)>0; no asserted operator or Fredholm determinant |
| Classical/later geometry | Positive-dimensional symplectic, Hamiltonian, contact, quantum owner | NOT APPLICABLE / not constructed |

The precise prior-work arrow is

~~~text
prime/composite divisor-exclusion observable
    -> sequential local witness tests
    -> reversible cyclic scan with complete retained counter
    -> groupoid and its own closed packets.
~~~

The divisor exclusion is the source of
[050](../050-causal-binary-sieve-fixed-point-screen/paper.md), read in the
[prior-work lineage](../../docs/prior_work/README.md). Here all proper divisors
are scanned, not only candidates up to the square root, and the chronological
source is replaced by a recurrent all-integer carrier. The equivalence of the
zero-witness tests is proved below; no chronological conjugacy with 050 is
claimed. This supplies the early symbolic/sequential arrow, not an unproved
Logistic/Hénon-to-geometric realization.

## 2. Definitions and permitted inputs

For n>=2 set L_n=max(1,n-2), J_n=Z/L_n Z and C_n=Z/n Z. Use representatives
j=0,...,L_n-1, and put

\[
Y=\coprod_{n\geq2}\{n\}\times J_n\times C_n,
\qquad
h(n,j)=\mathbf1_{\{j+2<n,\ j+2\mid n\}},
\]
\[
F(n,j,c)=(n,j+1\bmod L_n,c+h(n,j)\bmod n).
\]

The n=2 test is zero because its guard fails. This is the displayed uniform
rule, not an added prime exception. At n=3 the unique test concerns 2 and
returns zero.

No prime table, sieve-completed mask, chosen prime fibre, zero data, fitted
weight or per-prime parameter is supplied. The local rule does use ordinary
divisibility; the candidate is an engineered arithmetic algorithm, not a
derivation of arithmetic from an arithmetic-free rule. Its naturalness beyond
the exact source/return relationship remains a separate limitation.

The flow carrier is

\[
S=(Y\times[0,1])/((y,1)\sim(Fy,0)).
\]

Changing the phase of a periodic state identifies the same flow orbit.
Orientation is fixed by the flow; no extra reversal quotient is taken.
Counters, including all nonzero counters, remain in the state space.

## 3. Exact return and primality selector

### Proposition 1 — Inverse and complete scan

The map F is a homeomorphism. Put

\[
a(n)=\#\{d:2\leq d<n,\ d\mid n\}.
\]

For every complete state and every scan phase,

\[
F^{L_n}(n,j,c)=(n,j,c+a(n)\bmod n).
\]

**Proof.** Given the output (n,j,c), let k=j-1 modulo L_n. The unique
preimage is (n,k,c-h(n,k) modulo n). This gives inverse maps on all states.
Every map between discrete spaces is continuous. During L_n steps the scan
phase visits every residue exactly once; the increments therefore sum to
a(n), independently of the starting phase and counter. For n>=3 the tests
are exactly d=2,...,n-1. For n=2 there are no proper divisors in this range
and the guard supplies one zero test. QED.

The action groupoid has arrows (y,k) with source y and range F^k y. It is
discrete, countable, locally compact Hausdorff and étale; singleton
neighbourhoods suffice for these assertions.

### Proposition 2 — No cancellation of the arithmetic witness

For every n>=2,

\[
0\leq a(n)\leq n-2<n,\qquad
F^{L_n}(n,j,c)=(n,j,c)
   \ \Longleftrightarrow\ a(n)=0
   \ \Longleftrightarrow\ n\ \hbox{is prime}.
\]

**Proof.** There are n-2 possible proper-divisor tests, including zero
possibilities at n=2. Thus the integer count cannot be a nonzero multiple of
the counter modulus n. A prime has no proper divisor between 2 and n-1.
Conversely a composite n=ab with a,b>=2 has 2<=a<n, so a(n)>0.
The claimed dynamical equivalence now follows from Proposition 1. QED.

This also reconciles the source with the square-root sieve: if n=ab is
composite, at least one of a,b is at most sqrt(n), and it has a prime divisor
in that range. Both zero-witness tests therefore recognize exactly the same
prime indicator. They use different dynamics.

The return selector is intrinsic to the frozen marked system: its first
scan-phase return L_n and counter displacement are read from F itself, for
every counter and every phase. It does not require a separate zero seed for
each n. It does retain the n and phase observables; primality is not proved
recoverable from an unmarked length alone.

## 4. Complete primitive-orbit and flow ledger

### Proposition 3 — All states and all multiplicities

Define g(n)=gcd(n,a(n)), with gcd(n,0)=n. The entire n-fibre consists of
exactly g(n) distinct primitive F-cycles. Every one has least period

\[
T(n)=L_n\,\frac{n}{g(n)}.
\]

In particular n is prime exactly when T(n)/L_n=1. For a prime p there are
p primitive cycles, each of length L_p, not one cycle.

**Proof.** Any return of a full state must first return its phase, hence
must have time kL_n for an integer k>=1. By Proposition 1 this is a return
exactly when ka(n)=0 modulo n. The least such k is n/g(n): write
n=g(n)b and a(n)=g(n)d with gcd(b,d)=1, so b divides k exactly when n
divides ka(n). This also covers a(n)=0, where the least k is 1.

Every state in the fibre has this same least period. The fibre contains
L_n n states, so its number of cycles is L_n n/T(n)=g(n). Equivalently,
each cycle meets phase zero in one orbit of translation by a(n) on C_n.
That translation has g(n) counter cosets; none is removed. QED.

For n=2 and n=3 the complete fibres contain respectively two and three fixed
points. Their suspensions are five different primitive circles of length 1.
These are not five representatives of one circle.

### Proposition 4 — Same-object suspension and repetitions

The suspension is complete, and its primitive closed orbits are exactly the
cycles in Proposition 3, with lengths T(n). Their r-fold traversals have
length rT(n), for every positive integer r.

**Proof.** For a representative (y,u) with 0<=u<1 and any real time t, put
k=floor(u+t). The state is F^k y and the new height is u+t-k. This is
defined for all t because F is invertible; there are finitely many unit-roof
crossings on every bounded time interval. Returning to the same suspension
point requires an integer elapsed time and return of the complete base
state. Least positive flow periods are therefore precisely least F-periods.
Concatenating r traversals gives rT(n). QED.

No differential monodromy or stability of a positive-dimensional base is
assigned to this discrete carrier. There are no additional periodic
families hidden by selecting a zero section: all states have been counted.

## 5. The same ordinary product

### Proposition 5 — Local analytic object with the full ledger

The frozen ordinary unweighted product is

\[
Z_{\rm CDC}(s)=
\prod_{n\geq2}
 \left(1-e^{-sL_n n/g(n)}\right)^{-g(n)}.
\]

It converges absolutely, locally uniformly and to a holomorphic nonzero
function on Re(s)>0. In that half-plane its logarithm is the absolutely
convergent repetition sum

\[
\log Z_{\rm CDC}(s)
=\sum_{n\geq2}g(n)\sum_{r\geq1}
        \frac{e^{-srT(n)}}r .
\]

**Proof.** For sigma>0, T(n)>=L_n>=1 and g(n)<=n. Therefore

\[
\sum_{n\geq2}g(n)e^{-\sigma T(n)}
\leq2e^{-\sigma}+
 \sum_{n\geq3}n e^{-\sigma(n-2)}<\infty.
\]

Furthermore

\[
\sum_{r\geq1}\frac{e^{-\sigma rT(n)}}r
\leq\frac{e^{-\sigma T(n)}}{1-e^{-\sigma}},
\]

so the double series is absolutely convergent. The same bounds hold
uniformly on every compact subset of Re(s)>0 by taking a positive lower
bound for Re(s). Exponentiating this holomorphic logarithm gives the stated
nonzero product, with exactly the multiplicities and unit-roof repetition
law of Propositions 3 and 4. QED.

This is an ordinary dynamical product, not a Fredholm determinant or an
operator trace. Analytic continuation, a target divisor, a completed
functional equation, a natural function space and a trace-class owner are
OPEN. No assertion about them follows from local convergence.

## 6. Controls, source ownership, and limitations

The following are explicitly distinct control objects, not modifications of
the frozen candidate.

| Control | Exact comparison | Consequence |
| --- | --- | --- |
| Suppress all local tests, h=0 | Every n has n cycles of length L_n | Every integer passes the first-scan return test; the candidate's composite period extension is nontrivial |
| Replace h by constant one | Scan displacement is L_n modulo n, nonzero for every n>=2 | No integer passes the first-scan test; prime recognition is not forced by phase/counter geometry alone |
| Change counter to Z/2Z | Scan displacement is a(n) modulo 2; n=6 has two proper divisors | A composite passes; modulus n prevents a real aliasing obstruction |
| Retain every counter | A prime p contributes p separate cycles, not a chosen c=0 orbit | Full multiplicity is compulsory; no one-packet-per-prime claim |
| Forget marked n and scan phase | T(n) is an unmarked length, not the normalized marked return | The theorem is not an unmarked prime-length decoding theorem |
| Replace divisibility by another bounded witness predicate | Similar finite-counter scans can encode other bounded counts | PROVES_TOO_MUCH risk remains at the level of broad algorithmic naturalness |

For a concrete control difference, n=4 has L=2 and a=1: the candidate has
one cycle of length 8, while the suppressed-test control has four cycles
of length 2. At prime n=5 the candidate has five cycles of length 3,
whereas constant forcing has one cycle of length 15.

The conserved n does not itself make this an external prime-indexed
assembly: all integers and all complete states belong to one frozen,
uniform action, and the proper-divisor tests are performed along its actual
recurrent orbits. In [031](../031-primality-automaton-attractor-screen/paper.md)
there was no corresponding complete global carrier and distinct prime
inputs collapsed to one fixed point. In
[052](../052-hyperbolic-wheel-packet-lift/paper.md) the completed wheel
packets were supplied in advance and the action did not execute their
source update. Those particular failure proofs do not automatically apply
here. Conversely, these distinctions do not establish a canonical or unique
choice of counter algorithm.

There are still major adverse findings. Composites also supply genuine
closed packets and remain in Z. Prime p owns p packets with clock L_p:
for p>=3 this is p-2, not log p. Repetition rT(p) is a traversal law,
not an identification with prime power p^r. No packet may be discarded,
weighted by hand, or retimed to repair these shortcomings under this ID.

## 7. Gate assessment and decision

| Gate | Evidence for ANG-20260915-CDC01 | Status | Limitation |
| --- | --- | --- | --- |
| T0 | Full uniform countable carrier, inverse, groupoid and unit suspension | ESTABLISHED | No classical symplectic realization |
| T1 | Exact prime/composite selector in first-scan return, three explicit mechanism controls | ESTABLISHED FOR MARKED ARITHMETIC RETURN; CLOCK LIMITATION | Algorithmic naturalness qualified; prime clock p-2, not log p |
| T2 | Complete cycles, every counter multiplicity, all repetitions | ESTABLISHED | p cycles over p; composite packets present |
| T3 | Same complete ordinary product and repetition sum on Re(s)>0 | ESTABLISHED FOR LOCAL ORDINARY PRODUCT ONLY | Operator/trace/global continuation OPEN |
| Classical A0/A1/A2 | Broadened discrete groupoid track | NOT APPLICABLE | No rebranding as classical coordinates |
| Formal Route A | Target/divisor evaluation not performed | UNASSIGNED | No Route-A pass |
| Route B | No same-candidate formal readiness/authorization | NOT INVOKED | No B coordinate |

**Portfolio decision: advance.** The early marked arithmetic return and
complete packets warrant the same-object ordinary-product calculation, and
that bounded advance is now complete. Retain this as a positive broadened
source/return/analytic construction. Further geometric or clock changes need
a new frozen candidate; an unrelated operator cannot upgrade this one.
This is not a declaration that the programme's classical A0+A1 goal has
been achieved, nor a reason to stop the authorized breadth search.

## Reproducibility and evidence

The theorems are elementary proofs for all n, independent of finite testing.
The exact all-state check for 2<=n<=20 visits 2,453 states and tests inverse,
scan displacement and the complete period/multiplicity ledger. Its full
command, output and limits are in [evidence](evidence/README.md).

- [Frozen card and audit addendum](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Package summary](README.md)
- [Evidence and exact check](evidence/README.md)

This is a model-assisted internal research note, not externally peer
reviewed or venue-calibrated work. No human/animal data, private dataset,
external upload or publication is involved. Human authorship, funding and
conflict declarations have not been collected; none is inferred.
