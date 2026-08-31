# Hostile Review B — P129 round 1

Review date: 2026-08-31 UTC  
Role: independent nonauthor Reviewer B  
Artifact reviewed: current round-one source, support package, verifier, and
`main_round1.pdf`; the round-zero preservation artifact was checked by hash  
External status: **HOLD_EXTERNAL**

I did not read `HOSTILE_REVIEW_A.md`.  This review reconstructs the process
and the proofs from the current source and primary papers, then reruns the
paper-local controls and build independently.

## Provisional verdict

**GO_INTERNAL.**  I find no critical or major mathematical defect in the
round-one theorem package.  The finite-clock embedding, indirect-merger
label invariant, predictable compensator, stopped-walk evaluation, boundary
cases, and exact-law claims all close as written.  The three closest modern
mechanism owners are now identified and assigned zero contribution credit.
The residual is narrow and conjunction-specific, so this verdict does not
support external novelty or priority; `HOLD_EXTERNAL` must remain in force.

Severity count:

- **CRITICAL:** 0.
- **MAJOR (mathematics):** 0.
- **MAJOR (owner/scope):** 0.
- **MINOR:** 0 blocking items.  One nonblocking accounting note is recorded
  below: the reported 16,383 and 2,047 state counts are cumulative
  `(ambient n, mask)` loop instances, hence include the same finite set at
  several ambient sizes.  The stated coverage is nevertheless complete,
  and the canonical transcript accurately reports what the program runs.

## 1. Literal process and finite law

For a finite `S` containing zero, an update chooses one member of
`S \ {0}` uniformly and replaces `v` by `v-1`, with set union erasing a
collision.  This is not the lazy chain obtained by sampling a fixed
geometric site set.  The distinction is respected throughout the source.

The potential `Phi(S)=sum(S)` strictly decreases.  An empty-predecessor move
decreases it by one; a collision at `v-1` deletes `v` and decreases it by
`v`.  This proves absorption, acyclicity of the PGF recursion, and the
deterministic upper bound on the number of updates.

I also reconstructed the support induction.  If the predecessor of the
maximum `m` is empty, moving `m` first reduces both maximum and potential by
one and yields the whole interval `[m,Phi(S)]`.  If `m-1` is occupied,
moving `m` first yields `[m,Phi(S)-m+1]`; moving the bottom of the occupied
run ending at `m` decreases the potential by one while retaining maximum
`m`, yielding `[m+1,Phi(S)]`.  Since `Phi(S)>=2m-1`, these intervals touch or
overlap.  The `m=1` case is separated.  Thus the support theorem has no
hidden sparsity or endpoint gap.

For full occupancy, a trajectory of length `n-1` must collide at every
step.  Any deletion below a still-present larger neighbor leaves a vacancy
that eventually forces a noncollision, so the unique shortest order is
`n-1,n-2,...,1`; its probability is `1/(n-1)!`.  The empty full start
`n=1` has time zero, consistently with every formula.

## 2. Finite accessible clocks and the embedded scheduler

Let `M=max(S)`.  Motion is only rootward, so `{1,...,M}` is the complete
finite accessible positive-site set.  Put an independent rate-one Poisson
clock at each of those sites and ignore empty-site rings.  Every effective
ring is a stopping time for this finite clock vector.  Strong Markov at that
time gives fresh independent exponential residuals at all sites, including
a site that was empty when its clock rang previously and has only now become
occupied.

If there are `k` nonroot piles, precisely `k` site clocks can cause the next
effective update.  Their rates are all one, so the total effective rate is
`k`, the winning site is uniform among the current piles, and the embedded
jump chain is exactly the discrete chain in the definition.  The argument
does not attach clocks to original labels or accidentally multiply a
merged pile's rate by its mass.

There are at most `Phi(S)` effective updates.  Before absorption the total
effective rate is a positive finite integer, so each of the finitely many
effective waits is almost surely finite.  This justifies the passage from
finite continuous time to the terminal embedded update count.

## 3. Consecutive label intervals and indirect mergers

The pathwise label claim survives an indirect-merger attack.  Initially the
piles carry singleton labels in spatial order.  A move into an empty
predecessor transports one label interval and preserves order.  At a
collision, the destination at `x-1` is necessarily the immediately
preceding occupied pile: there is no lattice site strictly between `x-1`
and `x`.  Hence the two carried intervals are consecutive, and their union
is again an interval.  Induction over effective rings proves that every
current pile carries a consecutive block of initial labels, even after
either block has previously absorbed third-party labels.

The site-arrow construction is consistent under such outside mergers.  An
outside label joining a designated path does not change that path's future
site arrows; a merged pile still reads the single rate-one clock of its
current site.  Therefore adjacent initial labels are in the same current
pile exactly after their two graphical paths first meet.  With `r` initial
interfaces, the number of nonroot piles is pathwise

```text
N_t = sum_{i=1}^r 1{tau_i > t}.
```

No independence of the `tau_i` is used or asserted.

## 4. Predictable compensator and interface additivity

For the effective-ring count `J_t`, the conditional intensity immediately
before time `t` is `N_{t-}`, not `N_t`.  Since the finite-time rate is
bounded, the compensated process

```text
J_t - integral_0^t N_{u-} du
```

is integrable and has mean zero.  Both `J_t` and its compensator increase
with `t`; `J_infinity=T_S<=Phi(S)`.  Monotone convergence therefore passes
the finite-time expectation identity to infinity.  The left- and
right-continuous versions of `N` differ only at finitely many jump times,
which are Lebesgue-null, and Tonelli applies to the nonnegative finite sum
of interface indicators.  This yields

```text
E[T_S] = sum_i E[tau_i].
```

For a pair at `0<a<b`, the paths occupy distinct sites before meeting and
read independent rate-one clocks.  The next pair event has mean `1/2` and
chooses either path with probability `1/2`; strong Markov resets the pair
after the move.  Equality gives zero remaining time, while a lower path
fixed at zero leaves exactly `b` mean-one upper moves.  Thus the three
boundary/recurrence equations defining `h(a,b)` are correct, including
`h(0,b)=b`, and the arbitrary-state interface sum follows.

## 5. Hostile reconstruction of the stopped-walk proof

The `m=1` case is correctly removed before introducing `p=m-1`; it is the
root boundary `h(0,1)=1`.  For `m>=2`, let a lower-path event be `+1`, an
upper-path event be `-1`, let `U_k` count lower events, and put

```text
D_k = 1 + sum_{ell<=k} xi_ell,
K   = inf{k : D_k=0 or U_k=p}.
```

Until `K`, `D_k` is exactly the spatial gap.  Meeting after `j` lower and
`j+1` upper events has probability

```text
A_j / 2^(2j+1),   A_j = binom(2j,j)/(j+1),   0<=j<p.
```

Root exit after `p` lower and `q` upper events has probability

```text
P_{p,q} = B_{p,q}/2^(p+q),
B_{p,q} = binom(p+q-1,q)-binom(p+q-1,q-1),   0<=q<p.
```

The restriction `q<p` is forced because just before the terminal `p`th
lower event there are only `p-1` lower events and the gap must still be
positive.  Hence `K<=2p-1`; optional stopping is bounded and requires no
uniform-integrability argument.

Set `t_r=4^(-r) binom(2r,r)`.  I checked the two displayed telescopes
algebraically:

```text
(2r+1)t_r - (2r-1)t_{r-1} = t_r,
P_{p,q} = F_q-F_{q-1},
F_q = binom(p+q,q)/2^(p+q).
```

The first gives the meeting-time contribution

```text
S_1 = ((2p+1)t_p-1)/2.
```

The second gives root probability `t_p`; consequently the meeting
probability is `1-t_p`, so the two exits exhaust the stopped walk.  Since
`D_k` is a fair-walk martingale and `K` is bounded,
`E[D_K]=D_0=1`.  On root exit, `D_K=p+1-q`, hence

```text
sum_q P_{p,q}(p+1-q) = 1,
E[K 1{root exit}] = (2p+1)t_p-1.
```

The remaining upper path has `D_K` mean-one moves after root exit, so the
root contribution is

```text
S_2 = ((2p+1)t_p+1)/2.
```

Therefore `S_1+S_2=(2p+1)t_p=2(p+1)t_{p+1}`, which is exactly
`2m binom(2m,m)/4^m=(2m-1)!!/(2m-2)!!`.  The final identification with
`E|W_{2m}|` is a valid binomial telescope.  Summing the adjacent interfaces
and using the standard central-binomial estimate gives the claimed
`4 n^(3/2)/(3 sqrt(pi)) + O(n^(1/2))` full-start asymptotic.

As a reviewer-side control independent of `code/verify.py`, I enumerated
all first-exit words for `p=1,...,8` and checked the Catalan and reflected
ballot counts, then checked the exact `Fraction` telescopes, root/meeting
probabilities, optional-stopping moments, `S_1`, `S_2`, and the recurrence
triangle through `p,m=100`.  Result: **PASS, 10,972 assertions**.

## 6. Owner subtraction and residual ceiling

Primary-source audit, accessed 2026-08-31:

- Assiotis, *Random surface growth and Karlin--McGregor polynomials*, EJP
  23 (2018), Article 106, DOI
  [10.1214/18-EJP236](https://doi.org/10.1214/18-EJP236),
  [arXiv:1709.10444v2](https://arxiv.org/abs/1709.10444).  Section 2.2
  explicitly constructs graphical coalescing flows of birth--death chains.
  P129 correctly gives the coalescing-flow/site-arrow mechanism zero credit;
  Assiotis does not state this literal uniform-active embedded-update mean.
- Hitczenko--Wesołowski, *Expected Number of Jumps and the Number of Active
  Particles in TASEP*, J. Stat. Phys. 192 (2025), Article 99, DOI
  [10.1007/s10955-025-03483-0](https://doi.org/10.1007/s10955-025-03483-0),
  [arXiv:2503.03636](https://arxiv.org/abs/2503.03636).  Their Theorem 3
  gives `d E[P_t]/dt=E[a_t]` for step-initial TASEP.  P129 correctly assigns
  the active-count/jump-current bridge zero credit; exclusion dynamics and
  the finite absorption statistic are different.
- Śniady--Urbán, *Exact determinant formulas for coalescing particle
  systems*, [arXiv:2602.10782v3](https://arxiv.org/abs/2602.10782), revised
  8 July 2026.  It treats prescribed coalescence patterns for
  nearest-neighbor systems, has an explicit interval-label setup, and
  covers birth--death chains.  P129 correctly assigns ordered interval
  labels, finite coalescing construction, and pattern machinery zero credit;
  its residual is not a determinant or pattern-probability claim.

Bounded direct-owner searches used the formulations `coalescing pure-death
number of jumps`, `uniform active particle move toward root coalescence`,
`expected embedded updates coalescing path`, and `interface additive jump
count`, including arXiv and publisher/DOI pages through 2026.  I found the
three mechanisms above but no primary source stating the literal
arbitrary-state formula together with this scheduler and the support/full-
start package.  This is only a bounded non-hit, not evidence of novelty.

After subtraction, the admissible ceiling is exactly the paper's current
one: the finite deterministic-rootward set-valued chain, its arbitrary-state
embedded-update expectation, the complete support, and the stated
full-start consequences.  Generic graphical construction, interval-block
coalescence, active-count compensators, ballot identities, and
central-binomial asymptotics earn zero contribution credit.  Owner risk
remains medium because much of the proof technology is classical; the
honest ceiling and `HOLD_EXTERNAL` make that acceptable for internal use.

## 7. Internal collision firewall

The source-level comparison with the current internal papers is literal and
accurate.

- P117 acts on labelled cyclic binary words and flips every odd maximal run
  in parallel.  Its boundary-parity eroder is deterministic, has no pile
  path, root, or random active scheduler, and does not count embedded pile
  moves.  Shared eroder/coalescence language receives no credit.
- P121 repeatedly chooses a current adjacent separator, merges two entries
  by the product-plus-one rule, and induces a BST/Yule deletion history.
  Every P121 step is a separator merger.  A P129 step chooses a pile, may
  merely translate it without merging, and contributes to a different
  update-count observable.  Generic adjacency, random scheduling, and
  coalescence receive no internal credit.

The P114 and P126 exclusions are also consistent: synchronous rooted-forest
peeling and synchronous length-increasing composition refinement do not own
this carrier/kernel/statistic conjunction.

## 8. Fresh verifier and support audit

Fresh command:

```bash
cd papers/129-rootward-active-pile-coalescence
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | tee /tmp/p129-reviewb-verifier.dQt3iL/fresh.txt
cmp -s /tmp/p129-reviewb-verifier.dQt3iL/fresh.txt code/verification_output.txt
```

Result: **PASS; `cmp` exit 0; 506,663 assertions**.  Fresh and canonical
stdout were both 477 bytes with SHA-256
`3e40359274ae4bb033db5efe16d463b28af3fcd7464f9589bc5b136626acd080`.
The code uses integers and `fractions.Fraction`, with no randomness or
floating point.

Executed ranges agree across manuscript, README, plan, claims ledger,
control record, and canonical output:

- mean/Bellman/interface checks for ambient `n=1,...,14`: 16,383 cumulative
  `(n,mask)` instances and 98,305 transitions;
- full distributions and support for ambient `n=1,...,11`: 2,047 cumulative
  instances;
- pair triangle `0<=a<=b<=80`: 3,321 instances;
- stopped-ballot identity through `m=80`;
- full-start laws through `n=11`.

The maximum-time endpoint formula occurs only in the verifier.  Canonical
stdout marks it `PILOT_ONLY` and `MANUSCRIPT_CLAIM=NO`; support documents
mark it excluded.  The manuscript says only that an additional pattern is
retained in the program, gives no formula, assigns no theorem/promotion
credit, and keeps it out of the abstract and contribution ceiling.  I find
no claim leakage.

## 9. Isolated build, PDF, fonts, and visual audit

I copied only `main.tex`, `math_commands.tex`, `references.bib`, and
`sections/*.tex` to `/tmp/p129-reviewb-build.iFyQKF` and ran:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages passed.  Initial/post-BibTeX passes emitted only the
expected transient undefined-reference/citation notices; the settled
fourth-pass `main.log` and `main.blg` contain no LaTeX/package warning,
undefined item, overfull box, or underfull box.  All 8 citation keys close
against all 8 bibliography entries.

The isolated PDF is byte-identical to both `main.pdf` and
`main_round1.pdf`: 6 pages, 342,879 bytes, SHA-256
`5c64a88c1d003fd2729dd032eb229f9073975753040082919d0fc056d1c439f2`.
It is A4, unrotated, unencrypted, has no form or JavaScript, and has blank
title/author/subject/keyword metadata.  All 25 `pdffonts` rows are embedded,
subsetted, and Unicode-mapped.

I rasterized and inspected all six pages, not a sample:

1. title, abstract, model, and owner subtraction;
2. finite law, support induction, and minimum mass;
3. finite clocks, label intervals, and compensator;
4. pair recurrence and the first half of the stopped-walk argument;
5. equations (16)--(19), full-start theorem, and control boundary;
6. scope, conclusion, and all eight references.

There is no clipping, overlap, missing glyph, bad page break, orphaned
heading, or unreadable equation.  The round-one stopped-walk repair and the
PILOT exclusion are visibly legible.

## 10. Reviewed hashes

```text
6f187199a00764f23faf40cf8efec56dfb989cdf4771ee5a3316f7b631d111dd  main.tex
e39d4fba872c07b352c754dbcba8f32e6f66482774aeac28b6f074c56e98f42f  references.bib
20c0e6e0a0329b5e0ffed4d70fb5aee771ebd26f481116fe2f5c26a2f040bbf9  sections/3_interfaces.tex
015b5be981210ba803c7bb6c49476d0e148160beedf5774db0f036c7e8527745  sections/4_ballot.tex
fe79e8e3dfa1d15b16d04138d39ef653ac45bbd6addea50d3b53adf34f5aa272  code/verify.py
3e40359274ae4bb033db5efe16d463b28af3fcd7464f9589bc5b136626acd080  code/verification_output.txt
404b21a8beb9f9691326262544fc797cd1b62bf69b36ad2b5b65f693495dc05d  main_round0_original.pdf
5c64a88c1d003fd2729dd032eb229f9073975753040082919d0fc056d1c439f2  main_round1.pdf
d9b400ed28ac227f5b82f77b1c846dd9f0f6e8810ce5337dc788d84ed9926bf1  README.md
0608a079cb360655464268c8522e699dead57877ac7873e79f6b499ddbcacf38  PAPER_PLAN.md
c6e11aa37848d142a37a884f1b5349de381932eb6c7579ac2dc4441a2d46a9f4  NARRATIVE_REPORT.md
c60e5d6a47507f49f86491870c8bc436d88d7dc5c3215c3b0cfac664e21c6845  CLAIMS_EVIDENCE.md
1c3bd218a80100681ee5d11b7d8046e6a933c09c11a3ddc4779c703c56e82557  CONTROL_RESULTS.md
2caba17b64fb6d56dc7c8f7c9a7ad944dbad6ee944ad63af13aa5abfe18e9e98  BUILD.md
82f4895bce773ec4926e76958cdeefee5e6598a4e728a732d633daf57023e556  IMPROVEMENT_LOG.md
```

## Final decision

**GO_INTERNAL / HOLD_EXTERNAL.**  No manuscript repair is required for the
round-one mathematical contract.  Any later support-only closure may, if
desired, call 16,383 and 2,047 “cumulative ambient-size instances” to avoid
confusing those counters with numbers of distinct underlying finite sets;
this is an accounting clarification, not a coverage or theorem defect.
