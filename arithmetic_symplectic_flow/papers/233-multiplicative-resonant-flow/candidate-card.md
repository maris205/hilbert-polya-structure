# Frozen broadened candidate — multiplicative resonant mode flow

**Candidate ID:** `ANG-20260918-MRF01`  
**Paper ID:** `233-multiplicative-resonant-flow`  
**Version:** 1, frozen 2026-09-18 before mathematical claims or computation.  
**Initial status:** `FROZEN — GLOBAL FLOW AND COMPOSITE RETURN TEST OPEN`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Complete carrier and exact equation

Let E be the complex Hilbert space

\[
E=\left\{z=(z_n)_{n\ge2}:Q(z):=\sum_{n\ge2}\log n\,|z_n|^2<\infty\right\}.
\]

The candidate flow carrier is the entire charge shell
\(\mathcal M=\{z\in E:Q(z)=1\}\), with its norm topology. All integer
modes and every point of this shell are retained. It is not the finite-support
union, a prime-selected subspace, a projective quotient or a finite-dimensional
symplectic manifold. The ambient weak two-form and formal Hamiltonian are

\[
\Omega=i\sum_{n\ge2}dz_n\wedge d\bar z_n,\qquad
\mathcal B(z)=\sum_{a,b\ge2}\frac{\bar z_{ab}z_az_b}{ab},\qquad
H(z)=Q(z)+\operatorname{Re}\mathcal B(z).
\]

The sum is over all ordered pairs, including a=b. Its convergence and
differentiability are audit obligations. The restriction of Omega to the
shell is not claimed symplectic. Define

\[
(Lz)_n=(\log n)z_n,\qquad (S_tz)_n=n^{-it}z_n,
\]
\[
D(L)=\left\{z:\sum_{n\ge2}(\log n)^3|z_n|^2<\infty\right\},
\]
\[
N_n(z)=\frac1{2n}\sum_{\substack{a,b\ge2\\ab=n}}z_az_b
       +\sum_{b\ge2}\frac{z_{nb}\bar z_b}{nb}.
\]

The proposed action Phi_t is the unique maximal mild solution of

\[
z(t)=S_tz(0)-i\int_0^t S_{t-s}N(z(s))\,ds.
\tag{C1}
\]

For data where the strong equation is justified it must agree with
\(i\dot z=Lz+N(z)\). The whole E mild-state space must be retained;
classical differentiability in time may not be asserted at every point of E.
Local uniqueness, charge conservation, global existence in both directions
and shell invariance must be proved before calling Phi a full action. Its
transformation groupoid, if these obligations close, has objects M and arrows
\((z,t)\) with source z and range Phi_t(z).

## Arithmetic and lineage contract

The [prior-work](../../docs/prior_work/README.md) prime/composite observable
is deformed as follows:

```text
proper-divisor witness d|n, 2<=d<n
  -> all integer factor triples (a,b,ab)
  -> coherent local fusion/fission couplings in one mode equation
  -> an actual continuous-time arithmetic action, if globality is proved.
```

This replaces a symbolic admissibility test by its full factor-interaction
network. No equivalence with a chronological sieve, Logistic orbit or Hénon
system is asserted. No prime list, prime-specific coupling, von Mangoldt
weight, Riemann-zero data or fitted spectral parameter is allowed.

The coefficient 1/(ab), the charge level 1, and the dispersion log n are
fixed all-integer design choices. The resonance relation between multiplication
and logarithms is a proposed conservation mechanism, not an endogenous
prime-length theorem or a proof of naturalness. In particular a frequency
log n is not a period log n. No suspension roof is supplied or borrowed.

## Packet, clock and first discriminator

Packets are every nonconstant primitive point orbit of the full flow on M,
modulo actual time translation only. A primitive period is the least positive
physical return time; r-fold traversal of that same orbit has time rT.
Different mode labels, phases or harmonics must not be substituted for
traversals. No global phase or source-support quotient is imposed.

The intended prime-specific interpretation would assign a packet to one
arithmetic prime p through its source support in {p^k:k>=1}. A full closed
orbit supported in {6^k:k>=1} is therefore a decisive mixed-prime source
counterexample: its active labels have both prime factors 2 and 3 and lie in
no single-prime power sector. This is the precommitted arithmetic observable,
not a label assigned after a return is found.

After T0, test the complete closed subspace

\[
E_6=\{z\in E:z_n=0\text{ unless }n=6^k\text{ for some }k\ge1\}.
\]

This subspace is a counterexample probe inside the full carrier, not a
restriction of the main candidate. The planned discriminator is invariance
of E_6 and a possible positive extremum of Re B on its Q-unit ball. If a
critical point yields an actual periodic relative equilibrium, derive its
least period and retain it in the full ledger. Do not infer its existence
from a finite cutoff or a numerical stationary point.

## Controls, collisions and stopping boundary

- Zero coupling is a distinct linear-frequency control, not the candidate.
- Pure-mode initial states test whether the nonlinear source actually moves;
  finite support must not be assumed invariant.
- A prime-power support, such as {2^k}, and mixed-prime support {6^k} test
  whether the feedback really singles out arithmetic primes.
- Galerkin cutoffs may be used for a convergence proof only with explicit
  uniform estimates; cutoff periodic points are not full-model evidence.
- [186](../186-multiplicative-bar-clock/README.md) is a separate diagonal
  character-clock control; [193](../193-indecomposable-radial-quotient/README.md)
  first takes an indecomposable quotient. Neither supplies this full nonlinear
  mode action or its return ledger. Static-label Hamiltonian constructions
  such as [182](../182-nonlinear-two-pair-hamiltonian/README.md) likewise do not
  establish feedback for (C1).

Stop/fork immediately if the full mild action cannot be established within
the planned estimates, or if an intrinsic mixed-prime periodic packet is
proved. Do not delete composite modes, change the regularization or charge,
replace physical time, or construct a trace to rescue this ID. A T0 theorem
and a return counterexample may be recorded without claiming full orbit
classification. Remaining periodic data stay OPEN / NOT CLASSIFIED.

## Type and later-owner ledger

| Field | Scope at freeze |
| --- | --- |
| Type | Infinite-dimensional coherent-mode flow and its transformation groupoid; broadened ANG track |
| Classical (M,omega,F,tau) suspension | NOT APPLICABLE; no finite-dimensional symplectic base or mapping torus supplied |
| T0 | Mild action, topology, full shell and groupoid ownership OPEN |
| T1 | Factor interaction source and physical clock OPEN; design naturalness OPEN |
| T2 | Full point-orbit convention frozen; composite-power discriminator OPEN |
| T3 | NOT SUPPLIED; no transfer space, trace, zeta or determinant |
| Quantum/Hilbert–Pólya owner | NOT SUPPLIED; E is a classical mode space, not a target spectral realization |
| Route status | Formal coordinates UNASSIGNED; B NOT INVOKED |

The bounded deliverable is the global-owner audit followed by this one exact
return discriminator, with independent technical checking and Markdown-only
records. Root owns registry integration. No publication or broader analytic
programme is authorized by the card itself.

## Appended audit outcome — 2026-09-18

The version-1 mathematical inputs above are unchanged. The
[full paper](paper.md) proves global well-posedness of the mild action on the
entire charge shell, using bounded quadratic tensors, resonance and charge
conservation. It also proves an actual nonconstant periodic packet on the
precommitted mixed-prime probe \(E_6\). If \(m>0\) is the cubic maximum and
\(d\) the maximizing state's active-exponent gcd, its least physical period
is \(2\pi/[(1+3m/2)d\log6]\), with repetitions \(rT\).

**Current status:** `T0 ESTABLISHED; MIXED-PRIME PERIODIC PACKET — STOP / FORK`.
**Portfolio decision:** `stop / fork`, because that packet is supported on
integers divisible by both 2 and 3 and therefore violates the frozen
prime-exclusive source interpretation. Genuine factor feedback is
established, but source/scale naturalness remains `OPEN`. The full periodic
ledger is `OPEN / NOT CLASSIFIED`; no trace, determinant or later owner is
supplied. Formal Route coordinates remain `UNASSIGNED`; Route B remains
`NOT INVOKED`. Classical symplectic-suspension fields remain
`NOT APPLICABLE`. No orbit is deleted and no object or clock is changed.
