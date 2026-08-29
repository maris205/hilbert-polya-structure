# Independent cross-hostile review B — P107

Audit date: 2026-08-29 UTC. This is a team-internal independent audit, not
an external referee report. The reviewer did not author P107. No novelty,
priority, submission, or release endorsement is implied.

Verdict: **GO_INTERNAL / HOLD_EXTERNAL**. CRITICAL: 0. Mathematical MAJOR:
0. Repaired owner/scope MAJOR: 1. Repaired MINOR: 2.

## Independent theorem reconstruction

### Prime-power action and composition convention

Every ideal of `Z/p^a Z` is uniquely `(p^e)`, `0<=e<=a`. Its annihilator is
`(p^(a-e))`; taking the `r`th ideal power clips the exponent at `a`. Hence

```text
f_(a,r)(e) = min(a,r(a-e)).
```

For `Delta(e)=(r+1)e-ra`, the unclipped branch gives
`Delta(f(e))=-r Delta(e)`. The clipped branch is selected exactly when
`r(a-e)>=a`, equivalently `Delta(e)<=-a/r`. This checks both the inequality
direction and the equality case.

The endpoints satisfy `0<->a`. The fixed equation is
`(r+1)e=ra`; because `gcd(r,r+1)=1`, its integral solution exists exactly
when `(r+1)|a`. Every other nonzero deviation alternates sign and expands by
`r>1` until a negative phase clips to `a`. Thus no unlisted cycle survives.

### Depth clock and transient CDF

If the initial deviation is negative, negative phases occur at times `2k`
and the following update clips exactly when `r^(2k+1)|D|>=a`, so the depth is
`2k+1`. If it is positive, negative phases occur at times `2k+1` and clipping
requires `r^(2k+2)D>=a`, so the depth is `2k+2`. The review separately
checked equality at the threshold, the resonant `D=0` state, and `a=1`,
where there are no transient states and maximum depth is zero.

For time `t`, the greatest eligible negative exponent is
`2 floor((t-1)/2)` and the greatest eligible positive exponent is
`2 floor((t-2)/2)+1`. Converting the corresponding threshold to an integer
deviation cutoff gives the displayed ceilings. Counting
`D=(r+1)e-ra` over `1<=e<=a-1` gives `M_-` and `M_+`; neither includes the
resonant zero deviation, so adding `2+epsilon_(a,r)` does not double count.

### CRT product, periodic counts, and zeta

Under CRT, annihilator and ideal product power act coordinatewise. A product
state first becomes recurrent when its last coordinate does, so global depth
is the coordinate maximum and its CDF is the product of coordinate CDFs.
Every recurrent coordinate is either fixed or on the endpoint two-cycle.
Therefore an odd iterate fixes only a resonant coordinate in every component,
giving `A`, while an even iterate fixes all `B` recurrent points. There are
`A` fixed points and `(B-A)/2` two-cycles, and the finite-map zeta is exactly
`(1-z)^(-A)(1-z^2)^(-(B-A)/2)`. A transient point cannot be fixed by an
iterate, so no hidden periodic contribution is omitted.

## Findings and implemented repairs

### MAJOR (owner/scope) — closest operator-dynamics owner was omitted

The original draft cited annihilating-ideal graphs but not the substantially
closer work that treats radical and annihilator maps as operators on the
ideal poset, their generated monoid, and finite-product behavior. This made
the owner subtraction incomplete even though the exact map in P107 also
takes an ideal power.

The manuscript, README, claims ledger, and bibliography now explicitly
subtract Ryan C. Schwiebert, *The radical-annihilator monoid of a ring*,
*Communications in Algebra* 45(4), 1601–1617, DOI
[`10.1080/00927872.2016.1222401`](https://doi.org/10.1080/00927872.2016.1222401).
Crossref records print publication in 2017 and online publication in 2016.
The residual scope is now only the power-after-annihilator clipped-reflection
law and its exact temporal conjunction. External release remains HOLD.

### MINOR — internal valuation collisions were not disclosed in the paper

The phase-one firewall named P100 and P102, but the manuscript did not. It
now states that P100 acts by least-valuation digit erasure on residue classes,
whereas P107 acts on ideals by an alternating annihilator/power reflection;
P102 is a cyclic-group-algebra involution–norm system governed by polynomial
factorization. Shared CRT, valuation, and zeta bookkeeping receive no credit.

### MINOR — maximum-depth wording did not explicitly cover an empty transient set

The former sentence referred to the smallest positive and negative
deviations even when one sign side—or at `a=1`, both—has no transient state.
It now gives the sidewise statement and declares the global maximum to be
zero when the transient set is empty. No formula or control count changed.

## Endpoint and counterexample attacks

- `a=1`: only `0<->1`, no fixed resonance, depth maximum zero.
- `(r+1)|a`: the unique interior zero-deviation state is fixed and is
  excluded from both transient CDF tails.
- `(r+1)∤a`: there is no coordinate fixed point; consequently a CRT product
  with even one nonresonant component has no odd-iterate fixed point.
- Threshold equality `r^(m)|D|=a` clips on the next update and is included by
  the weak inequality in the theorem and verifier.
- `N` with repeated and squarefree prime factors: only the exponent tuple
  matters; primes themselves do not enter the coordinate map.
- `r=1` is outside scope. The expansion/no-other-cycle proof uses `r>1` and
  was not silently extended to that endpoint.

No mathematical counterexample was found.

## Fresh exact control and stored-output audit

The final repaired tree was rerun with
`python3 code/verify_annihilator_power.py`. Its stdout is byte-identical to
`code/verification_output.txt`:

```text
annihilator-power ideal dynamics exact control: PASS
assertions=212843
coordinate_states=29880
literal_divisor_ideal_states=49476
coordinate_grid=r=2..10, a=1..80
literal_moduli=N=2..1000, r=2..8
```

The coordinate lane tests every state on 720 parameter pairs, including
depths, CDFs, deviation steps, recurrent sets, and iterate-fixed counts. The
second lane uses literal divisor generators and the gcd update for every
`2<=N<=1000`, `2<=r<=8`; it independently checks the CRT step, depth, CDF,
fixed counts, recurrence, and two-cycle integrality. These are finite
falsification controls, not proofs of the quantified claims.

## Four-stage build and PDF inspection

The sequence `pdflatex -> bibtex -> pdflatex -> pdflatex` passed after the
repairs. The final author artifact has 4 A4 pages and 271,211 bytes;
`pdftotext -layout` recovered 13,646 bytes and 211 lines. The final log scan
contains no LaTeX/package warning, undefined citation/reference,
multiply-defined label, overfull/underfull box, or error. All 23 fonts are
embedded, subsetted, and Unicode mapped. All four pages were rendered and
visually inspected; equations, citations, DOI, and the repaired firewall are
visible without clipping or malformed text.

## Disposition

- Exact dynamical theorems and endpoint handling: **GO_INTERNAL**.
- Code and stored finite evidence: **GO_INTERNAL**.
- Owner language after the Schwiebert repair: adequate for internal use.
- External circulation, public posting, specialist contact, novelty, and
  priority language: **HOLD_EXTERNAL** pending a specialist direct-owner
  search and the later final QA/freeze.
