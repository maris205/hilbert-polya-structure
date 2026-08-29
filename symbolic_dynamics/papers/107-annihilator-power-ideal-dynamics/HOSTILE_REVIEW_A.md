# Independent cross-hostile review A — P107

Audit date: 2026-08-29 UTC. This review was performed on the frozen tree
after cross-hostile review B. The reviewer did not author P107 and did not
reuse computation as a proof. This is an internal correctness gate, not an
external referee report or a novelty certificate.

Verdict: **GO_INTERNAL / HOLD_EXTERNAL**. CRITICAL: 0. MAJOR: 0. MINOR: 0
new findings. The three repairs recorded by review B were independently
checked and retained; review A made no further change to `main.tex`, the
evidence files, the verifier, or the bibliography.

## Independent theorem reconstruction

### 1. Prime-power action and clipping boundary

Every ideal of `Z/p^a Z` is uniquely `(p^e)`, `0<=e<=a`. Its annihilator is
`(p^(a-e))`, and the `r`th ideal power clips the exponent at `a`. Therefore

```text
f_(a,r)(e) = min(a,r(a-e)).
```

For `Delta(e)=(r+1)e-ra`, the unclipped branch gives
`Delta(f(e))=-r Delta(e)`. The clipped branch is selected when
`r(a-e)>=a`; multiplying the manuscript's condition
`Delta(e)<=-a/r` by the positive number `r` shows that the two conditions
are exactly equivalent, including equality. Thus no rounding convention is
hidden at the boundary.

The endpoints satisfy `0<->a`. The only possible interior fixed point solves
`(r+1)e=ra`; since `gcd(r,r+1)=1`, it is integral exactly when `(r+1)|a`.
Every other deviation alternates sign and expands by the factor `r>1` until
a negative phase crosses the clipping boundary and maps to `a`. This excludes
all other cycles without assuming monotonicity of `f`.

### 2. Exact depth and CDF

For a negative initial deviation, negative phases occur at times `2k`, and
the next update clips exactly when `r^(2k+1)|D|>=a`; arrival at the recurrent
endpoint is therefore at time `2k+1`. For a positive initial deviation,
negative phases occur at times `2k+1`, and clipping occurs on the following
update exactly when `r^(2k+2)D>=a`, giving depth `2k+2`. This rederives both
parity branches and confirms the weak inequality at threshold equality.

For the cumulative law, the greatest eligible negative exponent by time
`t` is `2 floor((t-1)/2)`, while the positive branch begins only at `t=2`
and uses `2 floor((t-2)/2)+1`. Taking ceilings after division by the relevant
power of `r` gives `L_-` and `L_+`. Counting
`Delta(e)=(r+1)e-ra` over the interior interval `1<=e<=a-1` gives precisely
the displayed `M_-` and `M_+`; neither tail includes the resonant zero
deviation. Hence the separate contribution `2+epsilon_(a,r)` is neither
missing nor double-counted.

### 3. CRT products, fixed points, cycles, and zeta

Annihilator and ideal powers act coordinatewise under the CRT decomposition.
A product orbit first becomes recurrent when its last coordinate becomes
recurrent, so product depth is the coordinate maximum and its CDF is the
product of the coordinate CDFs. Each recurrent coordinate is either the
resonant fixed point or a point on the endpoint two-cycle. Consequently an
odd iterate fixes exactly `A=prod epsilon_(a_i,r)` product states, whereas an
even iterate fixes all `B=prod(2+epsilon_(a_i,r))` recurrent states. It
follows that there are `A` one-cycles, `(B-A)/2` two-cycles, no higher
periods, and

```text
zeta_T(z) = (1-z)^(-A) (1-z^2)^(-(B-A)/2).
```

The exponent `(B-A)/2` is integral: if every coordinate is resonant, then
`A=1` and `B` is odd; otherwise `A=0` and `B` has an endpoint factor two.

## Endpoint and counterexample attacks

- `a=1`: the coordinate set is only the endpoint two-cycle, so there is no
  transient state and maximum depth is zero. The revised statement handles
  this explicitly.
- Resonance `(r+1)|a`: the unique zero-deviation interior state is fixed and
  is excluded from both CDF tails.
- Nonresonance `(r+1)∤a`: there is no odd-period fixed coordinate; one such
  component makes the global odd fixed count zero.
- Exact clipping equality `r^m|D|=a`: it clips on the stated next update and
  is correctly included by `>=`.
- Squarefree `N`: every exponent is one, so every factor is only the endpoint
  two-cycle; the product can still contain many two-cycles but no hidden
  longer period.
- Repeated prime powers: the coordinate maximum and product CDF agree with
  literal divisor-ideal iteration; the primes themselves do not enter the
  coordinate dynamics.
- `r=1` is not covered. The no-other-cycle proof genuinely uses expansion
  by `r>1`; the paper does not silently extend the theorem to that endpoint.

No counterexample or quantifier defect was found.

## Owner subtraction and internal collision audit

The closest direct owner is Ryan C. Schwiebert, *The radical-annihilator
monoid of a ring*, *Communications in Algebra* 45(4), 1601–1617, DOI
[`10.1080/00927872.2016.1222401`](https://doi.org/10.1080/00927872.2016.1222401).
The publisher issue page and the author's preprint confirm that it treats
radical and annihilator as operators on the ideal poset, their generated
monoid, and finite-product behavior. P107 now assigns that operator viewpoint,
bare annihilator iteration, and product framework to the owner. The residual
scope is only the specified power-after-annihilator map and its proved
clipped-reflection/transient/cycle package.

The internal firewall is also adequate after review B: P100 erases least
valuation digits on residue classes; P102 uses an involution--norm map on a
cyclic group algebra. P107 instead alternates annihilator complementation
with ideal power on a divisor ideal lattice. Shared valuation, CRT, and zeta
bookkeeping receive no contribution credit. No same-action internal duplicate
was found.

The search remains bounded. It does not establish global novelty, priority,
or freedom to publish, so **HOLD_EXTERNAL** is mandatory.

## Fresh control replay

Review A reran

```text
python3 code/verify_annihilator_power.py
```

and compared stdout byte-for-byte with `code/verification_output.txt`. The
comparison exited zero. The frozen output is

```text
annihilator-power ideal dynamics exact control: PASS
assertions=212843
coordinate_states=29880
literal_divisor_ideal_states=49476
coordinate_grid=r=2..10, a=1..80
literal_moduli=N=2..1000, r=2..8
```

The first lane exhausts the coordinate grid and checks deviation updates,
depths, CDFs, recurrent sets, and iterate-fixed counts. The second lane uses
literal divisor generators and the gcd update for every `2<=N<=1000` and
`2<=r<=8`, then independently compares CRT steps, depths, CDFs, recurrence,
fixed counts, and two-cycle integrality. The finite ranges are falsification
evidence only.

## Four-stage build and visual inspection

Review A freshly ran `pdflatex -> bibtex -> pdflatex -> pdflatex`; all stages
exited zero. The resulting artifact is 4 A4 pages and 271,211 bytes. Final
log and extracted-text scans found:

- 0 undefined citations and 0 undefined references;
- 0 LaTeX/package warnings and 0 multiply defined labels;
- 0 overfull and 0 underfull boxes;
- 23 of 23 font entries embedded, subsetted, and Unicode-mapped;
- 13,646 extracted bytes over 211 lines, with no `??`, placeholder, or lost
  TeX-command sentinel.

All four pages were rendered and inspected. The clipped-reflection formulas,
piecewise depth clock, floor/ceiling CDF, CRT fixed-count display, DOI-bearing
bibliography, and HOLD language are legible with no clipping, overlap, or
orphaned reference page.

## Disposition

- Mathematical theorem package: **GO_INTERNAL**.
- Exact verifier and stored evidence: **GO_INTERNAL**.
- Current owner subtraction and P100/P102 firewall: adequate for internal
  circulation.
- Public posting, submission, specialist contact, novelty, and priority:
  **HOLD_EXTERNAL** pending specialist owner clearance and final QA.
