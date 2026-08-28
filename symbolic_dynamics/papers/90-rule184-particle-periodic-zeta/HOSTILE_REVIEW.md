# Internal hostile review — P90

Audit date: 2026-08-28 UTC
Disposition: **internal GO / external HOLD**
Reviewer status: an independent-in-workflow internal audit by an agent that
did not write the initial P90 draft. This document is not and does not claim
to be external peer review.

## Round 1 — attack of the submitted draft

### Findings and implemented repairs

1. **The sharp witness was asserted too informally.** A claim that a leading
   particle simply “detaches” did not by itself control the cyclic boundary.
   The proof now gives the occupied set at every `0<=t<=m-1`, proves it by
   induction, and checks the wrap-around gap under `n>=2m`.
2. **High density relied on an unnamed symmetry.** The manuscript now defines
   `Theta x_i=1-x_{-i}`, verifies `F_n Theta=Theta F_n`, and states that it
   swaps the two core branches and preserves entry time.
3. **The half-filled subtraction needed a temporal explanation.** The two
   alternating configurations are swapped by Rule 184, hence are fixed by
   the `k`th iterate exactly when `k` is even; for even `n` this is equivalent
   to `gcd(n,k)` even. The coefficient `-2` is now derived explicitly.
4. **The Möbius parity correction was compressed past safety.** The proof now
   evaluates
   `sum_{e|ell} mu(ell/e) 1_{2|e}=1_{ell=2}` and explains why division by
   `ell` leaves exactly `-1_{ell=2}` at the orbit level.
5. **The control stopped the min-plus check too early.** It now compares the
   closed and direct lifted trajectories for every `0<=t<=2n`, adds exact
   symmetry tests, and verifies a sharp witness in every layer.
6. **The owner boundary missed the closest recent work and contained a wrong
   given name.** The bibliography now identifies Aryaman Jha correctly and
   includes both the 2025 published jam-cluster paper and the 2026 analytic
   height-function preprint. The text distinguishes first core-entry time
   from a chosen-cluster lifetime or ensemble relaxation statistic.

Round-1 control after these repairs: **298,283 exact assertions**, all passed.
The revised PDF compiled without errors.

## Round 1 independent derivation ledger

- From the lifted exclusion update,
  `p_j(t+1)=min(p_j(t)+1,p_{j+1}(t)-1)`; induction gives the stated min-plus
  minimum over `0<=s<=t`.
- With `a_j=p_j(0)-2j`, periodic lifting gives
  `a_{j+m}=a_j+n-2m>=a_j`. Replacing the dropped element of an `m`-window by
  this larger translate makes successive minima nondecreasing, forcing every
  particle gap to be at least two at time `m-1`.
- An `F_n^k`-fixed point lies in the recurrent core. On either branch it is a
  repeated cyclic hard-core word of base length `d=gcd(n,k)`; complementation
  produces the high-density term and the alternating overlap produces the
  sole correction.
- Divisor inversion of the Lucas fixed count gives exact-period points;
  dividing by period gives temporal orbits. Primitive hard-core words give
  the particle-resolved refinement.
- The finite-map zeta product follows from the exact temporal-orbit ledger;
  no spatial SFT zeta is being asserted.

No contradiction was found in these rederivations.

## Round 2 — reattack of the repaired draft

The second pass targeted small rings, empty/full layers, half filling,
long-time lifted indexing, thermodynamic notation, and owner overreach.

- Direct exhaustive controls include `n=1,2`, `m=0,n`, every even
  half-filled alternating case, and times beyond the claimed first-entry
  bound. All passed.
- The finite-ring setup now explicitly assumes integer `n>=1`.
- The microcanonical limit now states both `n->infinity` and `m/n->rho`, so
  it cannot be misread as a limit over an unspecified index.
- Log, citation, font, text-extraction, and five-page visual inspections found
  no production defect.

No further mathematical change was required in Round 2.

## Bounded owner/scope audit

Queries included combinations of `Rule 184`, `finite ring`, `exact transient
time`, `relaxation time`, `periodic orbit`, `Lucas`, and `zeta`, with arXiv
and general scholarly-web checks through 2026-08-28. The classical papers in
the bibliography own conservation, convergence, traveling phases, and
preimage methods. The closest recent collision is Jha et al. (2025) and Jha,
Wiesenfeld, and Laval (2026), which analyze jam relaxation, total delay,
height functions, and related transient observables.

That thematic collision is material: the exact first-entry formula should
not be released as novel until those sources and their citation graph have
been compared line by line. No inspected result directly matched the full
combination of layerwise depth, weighted iterate-fixed polynomial,
particle-resolved temporal ledger, and finite-map zeta, but absence from this
bounded search is not evidence of priority.

## Residual risks and verdict

- **Mathematics:** low residual risk after proof rederivation and exhaustive
  finite controls on the registered ranges.
- **Scope:** low if `tau_n` remains explicitly a first-core-entry variable.
- **Owner/novelty:** medium–high for the transient component; medium for the
  orbit/zeta package because classical Rule-184 and golden-mean components
  are mature.
- **Verdict:** GO for internal Stage 2 use; HOLD for posting, submission, or
  priority language.
