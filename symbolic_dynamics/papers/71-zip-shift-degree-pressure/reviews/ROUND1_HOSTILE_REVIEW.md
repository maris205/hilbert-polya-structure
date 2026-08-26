# Round 1 hostile review

## Provenance and scope

**Provenance:** independent cross-agent review.  The requested GPT-5.4 child
reviewer was unavailable because the agent tree had reached its structural
thread cap.  This report does not claim GPT-5.4 provenance.  The reviewer did
not author P71 and read the manuscript, formal proof package, source and claim
ledgers, bibliography, deterministic control and receipt, prior internal
review, QA report, and round-0 PDF before proposing any edit.

**Release posture:** external release remains **HOLD**.  No priority or
worldwide-novelty conclusion is made.

## Overall verdict

**Verdict:** **MAJOR REVISION; the thermodynamic and rigidity formulae are
strong, but the advertised Bowen-entropy theorem is not proved at the
Carathéodory level of precision.**

**Score:** **7.0/10** at round 0.

No counterexample was found to the pressure, equilibrium, periodic, profile,
or spectrum formulae.  The major issue is proof type: method-of-types counts
of fixed-length words immediately control separated/capacity entropy, whereas
Bowen entropy for a noncompact set is defined by variable-length covers.  The
manuscript needs the missing cylinder comparison and Carathéodory argument,
not merely the assertion that past symbols contribute `O(1)`.

## Strengths

1. The local-degree index `x_{-1}` is consistent with the zip map, and the
   single boundary term in the orbit sum is correct.
2. The pressure proof starts from an arbitrary invariant measure and uses the
   sharp entropy-rate/Gibbs equality conditions, giving a genuine unique
   Bernoulli equilibrium rather than a Bernoulli-only calculation.
3. Fixed-point local-degree histograms recover fibre multiplicities, and the
   explicit coordinatewise code proves sufficiency of equal profiles.
4. The pressure recovery retains coefficients `m_k`; it does not confuse the
   set of fibre sizes with the multiset.
5. Martins--Mattos--Varão’s metric and folding formulae are explicitly
   owner-subtracted at the point of use.

## CRITICAL issues

None.

## MAJOR issues

### M1. The multifractal proof does not yet establish Bowen entropy rather
than upper-capacity entropy

**Evidence.** Lemma `lem:boundary` says an `n`-step Bowen name fixes
`n+O(1)` future symbols and only `O(1)` past symbols.  Theorem
`thm:spectrum` then counts words of a given type and invokes typical-word
separated sets.  Fixed-length covering/separation estimates alone compute
capacity entropy.  For an exact Birkhoff level set, Bowen’s noncompact-set
entropy requires a Carathéodory cover by Bowen balls of variable lengths and
a lower entropy-distribution argument.

**Required fix.** Strengthen Section 5 as follows.

1. Fix an explicit compatible two-sided product metric, for example
   `rho(x,y)=2^{-N(x,y)}` with a precise central-window convention.
2. Prove a cylinder sandwich: for every small scale `epsilon=2^{-M}`, an
   `(n,epsilon)` Bowen ball is determined, up to constants depending only on
   `M`, by the initial past block `[-M,-1]` and future block
   `[0,n+M-1]`.  Thus the number of past refinements is bounded independently
   of `n`.
3. For the upper bound, write the exact level set as a countable union over
   `N` of points whose averages stay in an `eta`-window for all `n>=N`.
   Cover at arbitrary lengths `n>=N` by type cylinders and show the
   Carathéodory sum converges for every exponent above the constrained
   Shannon maximum.  Then let `eta` decrease to zero.
4. For the lower bound, take a Bernoulli law with feasible marginal `p`, note
   it gives full measure to the level set, and prove the required local
   entropy bound on Bowen balls (or cite and apply the entropy distribution
   principle precisely).  This yields `h_B >= H(p)`.

After this repair, the conditional-entropy and Legendre calculations can
remain essentially unchanged.

## MINOR issues

### m1. The natural-extension measure/entropy bridge is only called
“standard” although pressure depends on it

Proposition `prop:natural` explicitly proves the topological inverse-limit
conjugacy but ends the measure correspondence and entropy equality in one
sentence.  Add either a precise standard reference or a short finite-alphabet
proof: invariant base measures have a unique inverse-limit lift, and the
coordinate generator shows that the lift and base have equal entropy.  This
will prevent the main pressure theorem from resting on an uncited black box.

### m2. Periodic-word alignment should be explicit

In Proposition `prop:periodic`, “repeat its `tau`-image on negative
coordinates” leaves a possible cyclic phase ambiguity.  Give the coordinate
formula, e.g. `x_i=s_(i mod n)` for `i>=0` and
`x_{-j}=tau(s_((-j) mod n))` with a fixed residue convention, and then list
the local degrees in their actual cyclic order.  The product identity is
unchanged.

### m3. Clarify the endpoint multiplicity sentence

After Theorem `thm:spectrum`, replace “when `k` is the unique extremal size
value” by a statement explicitly for `k=k_min` or `k=k_max`, with all
`m_k` fibres of that extremal size included.  A size value is automatically
unique as a numerical endpoint; its fibre label need not be unique.

### m4. Add the arXiv identifier to the published direct-owner bibliography
entry

The Martins--Mattos--Varão DOI and title are correct.  Add
`eprint={2407.01828}` and `archivePrefix={arXiv}` so the exact theorem version
audited in the source ledger can be recovered from the bibliography itself.

## Proof-dependency audit

```text
zip map
  -> exact local degree
  -> explicit full-shift natural extension
  -> invariant-measure / entropy correspondence
  -> pressure, equilibrium, derivatives

local degree + periodic coordinates
  -> weighted periodic identity and zeta

local degree + fixed points
  -> profile necessity under conjugacy
equal profile
  -> coordinatewise conjugacy
pressure exponential sum
  -> recursive profile recovery

orbit-sum boundary identity
  -> Bowen-ball/cylinder sandwich
  -> Caratheodory upper bound + entropy-distribution lower bound
  -> constrained Shannon spectrum
  -> fibre conditional maximum and Legendre formula
```

All nodes except the Bowen-ball/Carathéodory node are closed at round 0.  M1
must be repaired because the spectrum is a headline theorem, not an optional
remark.

## Source and ownership audit

- Lamei--Mehdipour’s primary record defines the zip space/map, describes the
  finite-to-one local-homeomorphism setting, and treats periodic orbit
  structure: <https://arxiv.org/html/2502.11272v1>.
- Martins--Mattos--Varão Theorem A gives the Shannon metric entropy and
  Theorem B gives the within-fibre conditional/folding entropy for the exact
  extended-shift map used here: <https://arxiv.org/html/2407.01828v2>.
- Mehdipour--Jangjooye Shaldehi explicitly claim intrinsic ergodicity for
  uniform `n`-to-one full zip shifts and square-entropy classification in
  their abstract: <https://arxiv.org/abs/2505.24647>.
- Bowen’s original noncompact-set entropy record is correctly identified by
  DOI: <https://doi.org/10.1090/S0002-9947-1973-0338317-X>.

The direct-owner attribution in Corollary `cor:folding` matches Theorems A--B.
The bounded exact-formula search found no primary source stating the entire
pressure/spectrum/profile package.  This is not a priority certificate, and
the active neighboring thermodynamic project keeps external release on HOLD.

## Control and reproducibility audit

- The baseline deterministic script passes periodic identities for two
  profiles through period five and four integer exponents.
- Mean/variance, profile recovery, ordinary-entropy collision, and binary
  Legendre checks pass.
- The spectrum control is numerical and cannot validate the distinction
  between Bowen and capacity entropy; M1 must be resolved by proof.
- Round-0 PDF preservation is present and hash-identical to the baseline
  `main.pdf`.
- `SHA256SUMS` and `FINAL_QA.md` must be regenerated after Round 2 because
  the review archive and revised proof change the package.

## Actionable Round 1 checklist

1. Supply the explicit Bowen metric, cylinder sandwich, Carathéodory upper
   bound, and entropy-distribution lower bound.
2. Close or cite the natural-extension entropy bridge.
3. Fix periodic alignment and endpoint wording.
4. Add the audited arXiv version to the direct-owner bibliography entry.
5. Re-run controls and a complete LaTeX/BibTeX build before preserving
   `main_round1.pdf`.

## Release recommendation

**HOLD.** Advance to Round 2 only after the Bowen proof is upgraded from a
capacity-level sketch to a genuine noncompact-set entropy proof.
