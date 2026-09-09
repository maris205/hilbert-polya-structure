# D1: finite algebraic holonomy labels for native Hénon trajectories

2026-09-09 UTC. Author scout; no admission or target-arithmetic grade.
**Current outcome: full finite-cover question closed negatively; exact
infinite-stage sharpness mechanism retained; independent check's one
mathematical correction implemented and read-back closed.**
Author recommendation: `CLOSED_AUXILIARY_INTERFACE_ONLY`, not a new paper.

## Frozen full question (before substantial proof)

Let $K$ be any number field and let $H$ be any finite nonempty composition
of generalized Hénon maps $(x,y)\mapsto(y,P(y)-ax)$, with $a\in K^*$ and
$\deg P\ge2$, or a polynomial conjugate of such a composition. A tick is
one application of this specified $H$, not one factor and not a logarithmic
roof. The domain is the entire affine plane $X=\mathbb A_K^2$.

The proposed intrinsic arithmetic label mechanism is a finite dominant
normal cover $\pi:Y\to X$ equipped with a $K$-automorphism $G$ satisfying
$\pi G=H\pi$. Ramified covers are allowed initially; disconnected normal
covers with every component dominating $X$ are allowed. On the étale locus,
a primitive native orbit $c$ of length $n$ has the conjugacy class of the
fiber permutation $G^n|_{\pi^{-1}(x)}$, for $x\in c$. Its class functions,
permutation-character traces, and twists of ordinary primitive-orbit sums
are the observables. No arithmetic-prime weight is inserted.

**Full question D1-FC:** classify all such label systems for every $K,H$,
and determine whether any distinguishes two primitive trajectories of the
same native length. The classification must also resolve the possible
loopholes of a lift available only for $H^m$ ($m\ge1$), finite algebraic
field-extension lifts, and compatible towers of finite covers. In the
$H^m$ variant, one lifted return always means exactly $m$ original ticks;
it is not substituted for the original clock.

**Decisive criterion.** A positive mechanism requires a genuinely
geometrically nonconstant cover, with an orbit-dependent holonomy invariant.
A negative answer must prove complete geometric constancy in this scoped
family and give the exact remaining arithmetic/time representation; merely
observing no target Euler identification is not a counterexample.

**First proof test (frozen pre-proof text).** The branch support is invariant under a lift; the
no-periodic-curve theorem for Hénon-type automorphisms, purity of branch,
and characteristic-zero étale simple connectivity of affine space may
force constancy. Exact hypotheses and closest-source ownership are being
checked. This is not yet an independently reviewed theorem.

## Source subtraction fixed at selection

- AS424-I's finite torsion memory is the classical geometric $U$ family;
  its exact-support cancellation and source determinant are fully deducted.
- AS424-D's ordinary rational-Witt packet trace and AS424-B's standard
  Bost–Connes Liouvillian obstructions are deducted, not extended here.
- R4 Salem greedy-return and R5 cyclic-resultant inverse spectra,
  Hénon–Frobenius equalizers, and periodic-parameter Galois towers retain
  their existing ownership and open boundaries.
- D1-FC concerns covers of the entire phase plane equivariant under its
  native automorphism. It is not a cover of parameter space or an isolated
  periodic locus, and it does not claim to constrain those different covers.
- The no-invariant-curve input is already source-owned (Dujardin–Favre,
  published Proposition 1.9, explicitly crediting Bedford–Smillie
  Proposition 4.2). Purity and affine-space étale simple connectivity are
  classical inputs. Their combination may yield a useful interface but
  is not automatically a substantial independent paper.

## Completed answer and reusable interfaces

The full argument, exact hypotheses, dependency map and source scopes are
in [FINITE_COVER_PROOF.md](FINITE_COVER_PROOF.md).

1. **Finite-cover classification, proved in §§3–4.** For every frozen
   $K,H$ and every $m\ge1$, every finite normal cover admitting a lift of
   $H^m$ is
   $Y\simeq\mathbb A_K^2\times\operatorname{Spec}A$, with $A$ a finite
   étale $K$-algebra and lift $H^m\times\tau$. The branch divisor is
   excluded by the classical no-periodic-curve theorem; purity removes
   potential isolated branching; characteristic-zero affine-space étale
   simple connectivity and descent supply the classification. Finite
   extensions of $K(x,y)$ admitting a lift and compatible finite equivariant towers
   give no escape. This is a geometric conclusion, not a statement that a
   target bridge happens to be missing.
2. **Exact primitive/spectral output, proved in §5.** Every length-$n$
   primitive native orbit has the same finite holonomy $\tau^n$.
   A sheet cycle of length $r$ yields exactly $\gcd(n,r)$ lifted primitive
   trajectories of length $\operatorname{lcm}(n,r)$. The Koopman action is
   the constant-sheet tensor product; any arithmetic Frobenius on this
   additional sheet factor is independent of the phase point. These
   explicit interfaces prevent an equal-length arithmetic distinction
   from being hidden in a cover or in an iterate-only lift.
3. **Characteristic boundary, exact in §6.** In characteristic $p$,
   $H(u,v)=(v,v^p-u)$ commutes with the connected degree-$p^2$ étale cover
   $\pi(u,v)=(u^p-u,v^p-v)$. The characteristic-zero conclusion really
   fails. This is a classical additive/Artin–Schreier control, not a
   solution of the current one-variable wild transfer question.
4. **Infinite-stage boundary and native arithmetic interaction, exact in
   §7.** With declared marked coordinate $f=x$, the distinct divisors of
   $f\circ H^j$, $j\in\mathbb Z$, give independent square classes.
   Adjoining all their square roots yields an infinite multiquadratic
   extension with a native index-shift lift, but no nontrivial finite
   geometric subextension stable under any iterate. For an actual
   primitive orbit $c$ of length $n$ in $\mathbb F_q^2$, where the odd
   finite field $\mathbb F_q$ contains the coefficients of the reduced
   $H,f$, and with the orbit avoiding $f=0$,
   the lifted $n$-tick fixed fibre has a Frobenius character eigenline
   with eigenvalue
   $\chi_q(\prod_{j=0}^{n-1}f(H^jP))$ for $q$-power Frobenius.
   For $H(x,y)=(y,y^2+3-3x)$ modulo $7$, the native fixed points
   $(1,1)$ and $(3,3)$ give opposite eigenvalues. This is a hand proof,
   not a finite census. It demonstrates an actual arithmetic/native-orbit
   interaction without identifying the two clocks.

Potential consumers are D2 (constant-factor versus actual fixed-fibre
Frobenius interaction), A2 (the distinction between finite algebraic
equivariance and an infinite ramification orbit), and X2 (obstructions
preserved under polynomial conjugacy and iterate lifts). The missing
compatibility conditions are explicit: characteristic zero and finite
normal equivariant covers for FC; a marked divisor, infinitely many
non-invariant stages, odd good reduction, and orbit avoidance for the
Kummer character. These interfaces were sent to the coordinator as they
were obtained; receiving lanes must check their own hypotheses.

## Actual closest-source deduction and disposition

The new decisive source is **Cantat–Dujardin (2024), Section 3(a),
Theorem B**: a proper holomorphic semiconjugacy between loxodromic
polynomial automorphisms of $\mathbb C^2$ is an automorphism. Its proof
already uses invariance of the ramification curve and the Hénon no-curve
theorem. The complete displayed theorem and proof were accessed at the
[publisher](https://doi.org/10.1112/blms.13164).

FC allows arbitrary normal source surfaces and arithmetic descent, rather
than assuming another plane as source. But the added passage is classical
purity, affine-space finite étale constancy, and elementary permutation
theory. The infinite Kummer example uses standard square-class independence
and a multiplicative quadratic cocycle, not a new global spectral theorem.
No source literally stating every formulation here was found in the
bounded search; that absence is not evidence of substantial novelty.

**Recommendation:** preserve the complete obstruction and sharpness
interfaces as auxiliary material. No independent-paper increment has been
established after source subtraction. The original finite-cover question
is not left open and is not weakened to a small-degree case. Conversely,
the explicit infinite example prevents converting it into a universal
no-go for every arithmetic label mechanism.

The remaining prospective arithmetic-spectral task would need a specified
global operator/space/trace compatible with the infinite fixed-fibre
construction and its ramification. None has been constructed here.
The marked divisor is extra source data, not a canonical feature of an
unmarked conjugacy class. The example does not establish a unique
arithmetic-prime owner, logarithmic prime clock, target Euler factors,
root numbers, automorphy or a Hilbert–Pólya realization.

## Source-access and execution receipt

The required first-pass AS424-I/D/B materials, including the analytic
package, and R4/R5 arithmetic-spectral reports/proof boundaries were read.
Targeted registry searches located finite-clock, finite-fibre and
monodromy ownership records; noisy/truncated broad hits were discovery
pointers, not an exhaustive local audit. No prior code or PDF was rerun.

Primary browsing submitted eighteen search formulations in six groups:
finite covers and invariant ramification; Hénon no-curve/étale covers;
semiconjugacy and finite field extensions; Bedford–Smillie and purity;
affine-space étale constancy; Kummer/character/difference-field neighbors.
Successful source bodies and unsuccessful accesses are itemized in the
proof supplement §8. The original Bedford–Smillie author PDF link and
later Dujardin–Favre PDF range/find calls failed; they are not claimed as
successful original-body proof reads. The no-curve proof is reconstructed
explicitly, while the primary Cantat–Dujardin collision was read directly.
No mathematical inference uses a secondary search lead or an empty result.

The repository Route-A, `research-lit`, `idea-creator`, and `proof-writer`
instructions drove the local-first subtraction, exact freeze and explicit
proof status. Current-team review replaces old external-model examples;
no such external review or full multi-stage literature pipeline was run.
An independent internal checker, assigned by the coordinator, has received
the complete proof. The checker found one actual scope correction in the
Kummer character: general number-field reduction requires a finite field
$\mathbb F_q$ containing the reduced coefficients and $q$-power Frobenius,
not unqualified $p$-power Frobenius on $\mathbb F_p$ points. This has been
implemented in both files and independently read-back closed. The checker
reported no remaining mathematical must-fix in the examined §§3–7 and
independently confirmed the Cantat–Dujardin source collision. The formal
review file is still being prepared; its final scope is not presumed here.

Mathematical executions: **0**. All examples are written exact arguments.
Created only this report and one genuine proof supplement, using
`apply_patch`, within the assigned lane. No separate ceremonial artifact
quota, source PDF download, new branch or manuscript was initiated.

## Execution and boundaries

No mathematical code, old program, build, PDF, external-model upload,
formal evaluation, shared-index edit or Git write. Only this assigned lane
is writable. `NO_BAD_EULER_OR_ROOT_NUMBER`: no target Euler factors, root
numbers, automorphy, target divisor or Hilbert–Pólya realization follows.
