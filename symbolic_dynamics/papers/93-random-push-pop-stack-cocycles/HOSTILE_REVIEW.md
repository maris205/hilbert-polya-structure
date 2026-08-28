# Internal hostile review — P93

Audit date: 2026-08-28 UTC  
Disposition: **internal GO after proof repair / external HOLD**

The stochastic candidate scout wrote the initial theorem package. Round 1
was an independent integrating derivation by the primary agent. Round 2 was a
strictly read-only attack by the algebraic scout, followed by targeted repairs
and a fresh exact-control run. This is internal adversarial review, not
external peer review.

## Round 1 — derivation and boundary audit

The integrating pass independently checked the finite normal form, image and
fibre geometry, quenched rates, synchronization boundary, critical marginal
limits, ballot expansion, and the three annealed regimes. It retained the
theorem package but tightened three boundaries:

1. At `p=1/2`, the manuscript now says that `I_n/sqrt(n)` and `J_n/sqrt(n)`
   are each marginally half-normal; it explicitly makes no joint-limit claim.
2. The owner discussion now credits bicyclic/zero-automatic monoid normal
   forms, ballot and gambler's-ruin identities, reflected walks, and
   exponential tilting. Search absence is not presented as priority evidence.
3. The exact control is described as a regression layer, not as a substitute
   for the strong law, Donsker's theorem, uniform integrability, or Markov-chain
   convergence.

The pass reran 265,609 exact assertions and a clean four-stage build before
Round 2.

## Round 1 derivation ledger

- Cancelling `D C_a=Id` gives the unique finite map form
  `Phi_n=C_(u_n) D^(J_n)`, with `J_n=M_n` and `I_n=|u_n|=M_n-S_n`.
- Therefore the image is exactly `[u_n]`, its diameter is `b^(-I_n)`, and
  each image point has exactly `b^(J_n)` preimages.
- The strong law gives quenched rates `(2p-1)_+ log b` and
  `(1-2p)_+ log b`; record times give the exact synchronization criterion
  `p<1/2`.
- At `p=1/2`, reversal symmetry makes `I_n` and `J_n` equal in law. Donsker,
  reflection, and Doob's `L^2` bound yield the two marginal half-normal
  limits and expectation asymptotics.
- The tail-sum identity for `b^(M_n)` plus the ballot first-hit law yields the
  exact finite formula. Gambler's ruin, a critical first-hit tilt, and a
  supercritical product tilt yield the three annealed regimes.
- Comparing the annealed exponent with the pathwise exponent exposes the two
  distinct thresholds `1/(b+1)` and `1/2` and the strict intermediate gap.

## Round 2 — proof attack and repairs

The algebraic reviewer found no counterexample and independently rederived
all displayed constants. It nevertheless returned **REVISE**, because two
compressed steps did not yet support the manuscript's complete-proof claim.
Both are now repaired:

1. The supercritical density is explicitly factorized as the mean-one
   product martingale
   `b^(S_n)/lambda^n = product_t b^(xi_t)/lambda`. This proves consistency
   of the finite tilted laws and produces iid tilted increments with
   probabilities `alpha` and `beta`. The zero-state transition is now stated
   correctly as `P_*(0,0)=alpha`, `P_*(0,1)=beta`.
2. At the critical tilt, the proof now defines
   `Yhat_n=Mhat_n-Shat_n`, writes its geometric stationary law, and uses a
   monotone coupling to obtain
   `0 <= Ehat Yhat_n <= 1/(b-1)`. Together with
   `Mhat_n=Shat_n+Yhat_n`, this supplies the asserted linear term and `O(1)`
   remainder without an unstated recurrence estimate.

Three endpoint/wording repairs were also adopted. The ballot display is
quantified for `0<p<1`; the direct endpoint laws are stated separately; and
the exclusion `b>=2` is explained, since at `b=1` the phase space is a
singleton and the metric/normal-form formulation degenerates. The program's
diagnostic docstring now correctly counts five floating diagnostics.

Finally, the control was expanded by 252 exact endpoint assertions: for
`b=2,3,5`, `p=0,1`, and `0<=n<=20`, direct propagation is checked against
both the finite ballot sum and `A_n(0)=1` or `A_n(1)=b^n`. The frozen total is
**265,861 exact integer/rational assertions**, with five floating diagnostics
explicitly excluded.

## Bounded literature and scope audit

Mairesse is cited for the zero-automatic/bicyclic monoid setting; Feller and
Asmussen are cited for the classical first-passage, change-of-measure, and
reflected-walk tools. These are umbrella citations in the internal draft.
Before any external release, a specialist should add theorem-, chapter-, or
page-level pointers for the precise ballot, gambler's-ruin, and reflected
birth--death facts used here.

A bounded search did not locate the full conjunction of a many-prefix/shift
random cocycle, exact image/fibre geometry, and the complete alphabet-
dependent annealed trichotomy. That negative result is not a novelty proof.

## Residual risks and verdict

- **Mathematics:** low after two independent derivations, the targeted
  critical/supercritical proof repairs, and exact endpoint controls.
- **Scope:** low for the stated prefix--shift cocycle and observables.
- **Literature/priority:** medium pending finer source localization and a
  specialist search across monoid walks and queueing terminology.
- **Verdict:** GO for internal Stage 2 use; HOLD for posting, submission,
  author contact, or priority language.
