# Actual bounded mathematical review — 176

**Candidate ID:** ASFS-20260915-XWH01  
**Reviewed status:** ADVANCE — COMPLETE CROSS-COUPLED PRIME PACKETS AND CHANGED FLOQUET LAW; NATURALNESS OPEN.  
**Review date:** 2026-09-15 12:24:14 UTC.  
**Disposition:** one identity blocker found and resolved; no unresolved mathematical blocker found in the stated contract. Formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Invocation, material and method

Actual reviewer: `/root/research_controller/cross_coupled_hamiltonian/coupled_owner_reviewer`.
This is a different invocation from the author and force-check helper, using
the inherited model family and visible proposal/context. It is nonblind,
uncalibrated model assistance, not human peer review, cross-model confirmation
or a certificate of independent errors. No other reviewer was simulated.

I read the complete [paper](../paper.md), [card](../candidate-card.md),
[ledger](../claim-ledger.md), [README](../README.md) and [evidence index](README.md),
plus the full [171 mathematical antecedent](../../171-separatrix-witness-hamiltonian-clock/paper.md)
for its generator, return strip, axis periods and monodromy. I independently
recomputed the coupled equations, derivative inequalities, complete branch
classification and integral estimates rather than accepting the verdict labels.
ARS router, academic-paper workflow and argument-builder instructions were
read and applied only as bounded claim/evidence/counterargument discipline.
No publication pipeline, venue assessment, numerical experiment, external
model/API, script artifact, Git mutation or change to the submitted proof was used.

## Finding and correction: identifier collision

The initial 176 identifier `ASFS-20260915-CWH01` already belonged to
[145](../../145-convex-witness-henon-sieve/candidate-card.md). I reported this
as an identity blocker before recording final hashes. The author corrected
only 176's five core files to `ASFS-20260915-XWH01` and appended the dated
card erratum and evidence account. I reread those changes and directly
confirmed 145's existing identifier. A targeted read-only `rg` now finds
XWH01 only in this package within `papers/` and the root README search scope.
The displayed Hamiltonian, energy, section, physical clock and design inputs
did not change. The blocker is **RESOLVED**, not a clean first-pass freeze;
no result or ownership is inherited from 145.

## Independently checked mathematical chain

1. **Full completeness and regularity (Proposition 1).** The cross force is
   `-((1-a)c+I/2)W'-8a`, with conserved `I=QP`. The bound `abs(W')<=4`
   bounds scalar acceleration on each trajectory, and `1<=b<=3/2` bounds
   both transverse exponentials on finite time intervals. Critical points
   require `Q=P=p=0`; the composite derivative is at least `3a+5`, and
   prime critical energies are `0,c>1`. Thus energy 1 is regular throughout.

2. **Every composite energy branch (Proposition 2).** Direct differentiation
   gives `b^2 J_a'=((a-1)c-1/2)W'+4a(qW'-W-2)`.
   With `t=q^2`, `qW'-W=4t(1-3t)/(1+t)^3<=1/3`; hence the claimed
   bound `b^2 J_a'<=-5a/3` is valid for every real q and every composite a.
   Its limits are opposite infinities. The equation
   `p^2/2=b(J_a-I)` therefore has one simple turn for every real I,
   allowed region `q<=q_I`, no equilibrium and no bounded oval.
   For `I<1`, the second zero-position crossing has negative momentum,
   so no composite bi-return state is omitted. The old force premise really
   fails: the displayed n=4 state has `H=129+4-132=1` and `pdot=344/5`.

3. **Prime return and true suspension (Propositions 2–3).** Solving
   `0<1-I<c+I/2` gives exactly `-2/(3n^2)<I<1`; only inner ovals return.
   Outer branches, saddles, separatrices, `B<=0`, `I=1` and `I>1` are
   correctly retained or shown empty. On an inner oval, the clockwise
   angular speed is positive and at most 14, so `tau>=pi/7` is valid.
   The true return exponent is `Lambda=integral b dt`, not elapsed `tau`.
   Their two area cross terms cancel using `dI=P dQ+Q dP`. The inverse,
   full invariant strip and transverse flow-box argument establish precisely
   the complete return-saturation owner, not the entire energy surface.

4. **Full periodic multiplicity (Proposition 4).** For any positive closed
   time, `K(t)>=t` forces both `Q=P=0` on the entire energy, including
   the nonreturning complement. Its scalar axis has exactly one prime inner
   oval and no composite closed orbit. One positive section crossing gives
   least map period one and one oriented flow packet; `dI=0` at its origin
   yields the stated repeated multipliers `exp(±r L_p)`. No centre is selected
   in advance and no time/energy neutral direction is counted as transverse.

5. **Physical clock versus Floquet law (Proposition 5).** The substitution
   `y=(1-q^2)/(1+q^2)` gives exactly the stated f and period integral.
   The low-end error is bounded by `C_0/2`; the upper denominator is at
   least `sqrt(1/20)`. This gives `T_n=2 sqrt2 log n+O(1)` uniformly.
   In `L_n=3T_n/2-R_n/2`, the low part of R is bounded using `y^2<=y/2`
   and the upper part by integrability of f, proving a uniform `R_n=O(1)`.
   Thus `L_p=3 sqrt2 log p+O(1)` and `T_p<L_p<3T_p/2` are correct.
   The corresponding-packet time-preserving C1 conjugacy obstruction follows
   from different Poincare eigenvalues; no unrestricted nonconjugacy follows.

6. **Ordinary product (Corollary 6).** Actual physical T_p, the uniform
   logarithmic error and positive period bound imply absolute normal
   convergence exactly when `Re s>1/(2 sqrt2)`. The first repetitions
   force divergence at the positive boundary via the elementary prime
   harmonic argument; a single prime suffices when `Re s<=0`. Finite
   physical windows contain finitely many packets and repetitions. This
   proves neither continuation nor an operator/Fredholm identity.

## Scope and binding

The stated scoped advance is supported: a complete changed generator and
Floquet law, with the old axis clock rederived, not a new primitive clock.
Static arithmetic, designed rational barrier/coupling/energy and the arbitrary
zero-set control leave naturalness OPEN. No other candidate's operator is
attached, and no formal Route or target-divisor claim is reviewed as passed.
The same-object ledger is intact after the identifier correction.

Reviewed four-core SHA-256 values, obtained by read-only `sha256sum`:

| File | SHA-256 |
| --- | --- |
| [README.md](../README.md) | `6585b663faf513f5661267079950019a284e4b9de02a7eca4536c27888824ece` |
| [paper.md](../paper.md) | `18ba3a36ecba3a8e3df076369c46b0c53b8f4f7cd4a33141cabe3e30a0c0b575` |
| [candidate-card.md](../candidate-card.md) | `d4ddef15ef05c3262c14d561cf2cb10d140cb9aea55b6e3e3bf05b7f0c8effdc` |
| [claim-ledger.md](../claim-ledger.md) | `d979df1e6954975eb251ee722deaaee39d36c38a7701bf2d6bf3371d002a439b` |

The evidence index may receive the author's actual completion receipt and is
not hash-frozen here. Root retains the final integrated structural checks.
Any changed mathematical input or stronger owner claim requires targeted
re-review; unchanged derivations need not be rerun to repeat this disposition.
