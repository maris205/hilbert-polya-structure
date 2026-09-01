# HOSTILE REVIEW A — P149

**Manuscript:** *Iterated Endpoint-Peak Extraction on Permutations: All-Rank Images, Sections, and a Sharp Clock*  
**Reviewer mode:** independent hostile review; the reviewer did not author P149  
**Date:** 2026-09-01 UTC  
**External status:** `HOLD_EXTERNAL`  
**Files changed by this review:** this report only

## Verdict

**REVISE before internal freeze.**  I find no mathematical counterexample to
the packing theorem, the all-iterate image/right-section theorem, the sharp
clock, or the comparison-poset fibre formula.  The verifier, transcript, and
PDF build are mutually consistent.  The release blocker is the ownership
layer: the manuscript conflates its two-sided zero-boundary peak convention
with the ordinary, interior-only pinnacle convention used by all four cited
papers, and it omits a primary source that treats the manuscript's exact
boundary convention.  This is repairable without changing the theorem
ceiling.

| Severity | Count | Summary |
|---|---:|---|
| Critical | 0 | No false lead theorem, invalid inverse, or corrupt artifact found. |
| Major | 1 | Boundary convention and owner subtraction are materially inaccurate/incomplete. |
| Minor | 2 | One false/ambiguous strictness sentence; incomplete version-of-record metadata. |

## Findings, in severity order

### Major 1 — the cited pinnacle owners use a different boundary convention, while an exact-convention owner is missing

P149 defines

```text
pi_0 = pi_{n+1} = 0,
```

so either endpoint may be a peak.  This is essential: it makes the output
nonempty, gives the bound `ceil(n/2)`, and supplies the unique singleton
absorber.  By contrast, the cited Davis--Nelson--Petersen--Tenner,
Rusu--Tenner, Fang, and Alexandersson--Nabawanda papers define ordinary peaks
only at positions `2,...,n-1`.  Their pinnacle or peak-value sets exclude both
endpoints.  Thus the sentence “The set of peak values, or pinnacle set, and its
static admissibility are established subjects” is not correct as written for
the statistic that P149 actually iterates.  The corresponding claims in
`SOURCE_VERIFICATION.md` and `BUILD.md` that the static owners are fully
subtracted are consequently too strong.

There is also a directly relevant primary source missing from the ledger.
Section 2 of Amy M. Fu, [*A Context-free Grammar for Peaks and Double Descents
of Permutations*](https://arxiv.org/abs/1801.04397), *Advances in Applied
Mathematics* 100 (2018), 179--196,
[DOI 10.1016/j.aam.2018.06.004](https://doi.org/10.1016/j.aam.2018.06.004),
sets exactly `pi_0=pi_{n+1}=0`, calls the selected indices peaks (also noting
the names maxima/modified maxima), and treats their static distribution.  It
does not appear to iterate the standardized ordered peak-value word, so it
does not kill the lead theorem, but it directly owns static facts under the
exact boundary convention and must receive zero credit.

The ordinary pinnacle literature remains relevant, but only after stating the
convention bridge.  One clean bridge is

```text
pi_1 ... pi_n  ->  1, pi_1+2, ..., pi_n+2, 2.
```

The ordinary interior pinnacles of this padded permutation are precisely the
endpoint-inclusive peak values of `pi`, shifted by two and in the same
left-to-right order.  This shows why ordinary pinnacle results are nearest
owners, without pretending that their definitions are literal matches.

The bounded audit also needs to distinguish the actual run-sorting result.
Alexandersson--Nabawanda prove a multivariate equidistribution by constructing
an auxiliary bijection `eta` with
`PKV(sigma)=PKV(runsort(eta(sigma)))`; run-sorting itself is not asserted to
preserve every input's peak-value set.  The ledger's phrase “a peak-value
invariant” should be qualified accordingly.

Finally, if the fibre result is retained, “fully subtracted” should not be
claimed without directly logging the closest fixed-set and ordering sources,
including at least:

- Diaz-Lopez--Harris--Huang--Insko--Nilsen,
  [*A Formula for Enumerating Permutations with a Fixed Pinnacle Set*](https://arxiv.org/abs/2001.07325);
- Domagalski--Liang--Minnich--Sagan--Schmidt--Sietsema,
  [*Pinnacle Set Properties*](https://arxiv.org/abs/2105.10388), which also
  discusses counting admissible orders;
- Falque--Novelli--Thibon,
  [*Pinnacle Sets Revisited*](https://arxiv.org/abs/2106.05248).

These are not a direct hit on the all-iterate variable-rank map.  They do,
however, define the subtraction boundary for the secondary fibre axis more
accurately than the current four-item ledger.

**Required repair.**

1. Replace “peak values, or pinnacle set” by terminology that keeps
   “endpoint-inclusive peak-value word” distinct from the conventional
   interior pinnacle set.
2. Add Fu 2018 as a direct owner of the exact zero-boundary static statistic
   and assign all static distribution facts zero credit.
3. Explain the padding bridge before invoking ordinary pinnacle/order
   literature, or otherwise state explicitly that those papers use a
   different convention.
4. Correct the run-sorting description from pointwise invariant language to
   the actual bijection/equidistribution statement.
5. Expand the source ledger with direct-versus-nearest labels, the fixed-set
   sources above, actual search queries, and the limitation that a bounded
   non-hit for the iterated standardized extraction is not novelty evidence.
6. Preserve the current contribution ceiling: only the conjunction
   “ordered endpoint-inclusive peak values, standardization, iteration,
   every-iterate images/right sections, and sharp clock” survives the
   subtraction.

### Minor 1 — “The upper bound is strict” is false under its ordinary mathematical reading

Immediately after

```text
1 <= |P(pi)| <= ceil(n/2),
```

the manuscript says “The upper bound is strict when `n>1`.”  Equality in that
upper bound certainly occurs; for example, `P(213)=12` has size two, equal to
`ceil(3/2)`.  The proof package contains the intended and correct statement:
`ceil(n/2)<n` for `n>1`, so **rank** strictly decreases.

**Required repair.**  Replace the sentence by, for example,
“Since `ceil(n/2)<n` for `n>1`, every nonsingleton step strictly decreases
rank.”  No theorem or verifier change is needed.

### Minor 2 — two final journal records and one DOI are absent from the bibliography

The bibliography cites the Davis et al. and Rusu--Tenner papers as arXiv
`@misc` entries even though their version-of-record metadata are stable:

- Davis et al., *Discrete Mathematics* 341(11) (2018), 3249--3270,
  [DOI 10.1016/j.disc.2018.08.011](https://doi.org/10.1016/j.disc.2018.08.011);
- Rusu and Tenner, *Graphs and Combinatorics* 37(4) (2021), 1205--1214,
  [DOI 10.1007/s00373-021-02306-9](https://doi.org/10.1007/s00373-021-02306-9).

The Alexandersson--Nabawanda entry should also record
[DOI 10.54550/ECA2022V2S1R2](https://doi.org/10.54550/ECA2022V2S1R2).
The existing author-hosted/arXiv links may be retained alongside the final
metadata.

**Required repair.**  Upgrade those BibTeX entries and make the source ledger
match.  Rebuild and refresh PDF hashes after this metadata-only change.

## Independent mathematical re-derivation

### 1. Endpoint packing and strict descent — PASS

The global maximum exceeds both genuine neighbours and any fictitious zero
neighbour, so at least one peak is selected.  Two selected positions cannot
be adjacent.  A nonadjacent subset of a path on `n` vertices has size at most
`ceil(n/2)`, giving

```text
1 <= |P(pi)| <= ceil(n/2).
```

For `n>1`, `ceil(n/2)<n`; this, rather than strictness of the displayed peak
bound, is the rank-descent statement used by the clock proof.

Boundary checks pass: `P(1)=1`; both permutations of rank two map to `1`; and
endpoint peaks can coexist at rank three, as in `213 -> 12` and `312 -> 21`.

### 2. One-step lift — PASS, including parity and singleton boundaries

For `sigma in S_m` and `n>=2m-1`, the lift uses three disjoint value sets:

- highs `n-m+1,...,n`, ordered as `h_i=n-m+sigma_i`;
- separating valleys `1,...,m-1`;
- the decreasing tail `n-m,n-m-1,...,m`.

Their sizes sum to `n`.  Every high is a peak; every inserted valley has a
larger high neighbour; and every tail entry has a larger left neighbour.  The
peak-value word is exactly `h_1...h_m`, whose standardization is `sigma`.

The delicate boundaries are correct:

- at `n=2m-1` the tail is empty and the last high is compared with the right
  zero boundary;
- at `n=2m` the tail is the singleton `m`;
- at `m=1`, `L_{n,1}(1)=n,n-1,...,1`, whose only selected value is `n`.

Thus the one-step image is exactly every rank
`m<=ceil(n/2)`.

### 3. Every iterate and every-target right sections — PASS

Repeated packing gives the forward rank bound
`ceil(n/2^k)`.  For integer `m`,

```text
m <= ceil(n/2^k)
iff n >= 2^k m - (2^k-1)
iff n >= 2^k(m-1)+1.
```

With `a_k=m` and `a_j=2a_{j+1}-1`, one has
`a_j=2^(k-j)(m-1)+1`.  Every inner lift is therefore legal at its minimal odd
source length, while the displayed inequality is exactly the legality
condition `n>=2a_1-1` for the outer lift.  Composition gives a literal
right section of `P^k` over every feasible target, not merely a cardinality
argument.

The `n=1` and large-`k` cases are sound: once an intermediate rank is one,
`L_{1,1}` is the identity, and the outer decreasing lift reaches `1` on its
first extraction and remains there.  As extra targeted pressure beyond the
frozen verifier, I checked identity and reverse targets for all
`1<=n<=64`, `1<=k<=16`; all 1,282 constructed sections returned the target.

### 4. Sharp clock and equality witnesses — PASS

The strict rank descent makes the singleton the only recurrent state.  The
packing recursion reaches rank one in the least `k` with `n<=2^k`, namely
`ceil(log_2 n)`, so this is a pointwise upper bound.  The recursive witness

```text
w_n = L_{n,ceil(n/2)}(w_{ceil(n/2)})
```

attains equality at the first step and then follows the same recurrence.
Hence its rank sequence saturates every intermediate ceiling and
`tau(w_n)=ceil(log_2 n)` for every `n`, not just powers of two.  The base
`w_1=1` gives `tau=0` as required.

### 5. Comparison-poset fibre — PASS

For a fixed comparison word, the manuscript's endpoint formula is correct:
the first position is a peak for initial `D`, an interior position for `UD`,
and the last position for terminal `U`.  The empty word at `n=1` has its
single position as a peak.

The adjacent inequalities form an oriented-path poset.  Every selected peak
position is maximal in that poset, so imposing an arbitrary total order among
the peak positions cannot create a directed cycle.  If the left-to-right
target is `sigma`, the chain

```text
p_{sigma^{-1}(1)} < ... < p_{sigma^{-1}(m)}
```

has the correct direction: it orders peak positions from smallest peak value
to largest.  Assigning ranks `1,...,n` along a linear extension is then
bijective with permutations having that comparison word and standardized
peak word `sigma`.  Comparison words are disjoint, so summing gives the full
fibre.  The infeasible-rank sum is empty, and `n=m=1` contributes one empty
word and one extension.

This proof is complete, but it is appropriately secondary and should remain
explicitly zero-credit with respect to generic zigzag-poset/linear-extension
machinery and the static pinnacle-order literature.

## Owner subtraction after repair

| Relationship | Source class | Review conclusion |
|---|---|---|
| Direct for the exact two-zero-boundary **static peak statistic** | Fu 2018 and the classical work it identifies | Zero credit; missing from the current manuscript. |
| Nearest for **interior peak values/pinnacles and their orders** | Davis et al.; Rusu--Tenner; Diaz-Lopez et al.; Domagalski et al.; Fang; Falque et al. | Zero credit after explicitly stating the convention/padding bridge. |
| Nearest size-preserving peak-value dynamics | Alexandersson--Nabawanda run-sorting/equidistribution | Zero credit; describe the auxiliary-bijection statement accurately. |
| Direct for the exact standardized ordered endpoint-peak map under iteration | Bounded primary-source search non-hit | A non-hit is not novelty, priority, or clearance evidence. |
| Surviving conjunction | exact map + all iterate images + every-target sections + sharp every-rank clock | Mathematically survives this review, subject to repaired ownership language. |

Queries included combinations of “iterated/local maxima/peak extraction,”
“standardization,” “peaks of peaks,” “endpoint peaks,” “modified maxima,”
“pinnacle ordering,” and “run-sorting,” restricted to primary arXiv, DOI, or
author-hosted records.  The search was bounded and cannot certify novelty.

## Verifier and artifact audit

### Exact control — PASS

Cold command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p149.py
```

returned

```text
assertions=1228181
P149_THEOREM_INTERFACES_PASS
```

The cold output is byte-identical to `verification_output.txt`.  The reported
coverage is internally consistent:

- 409,113 source permutations, exactly `sum_{n=1}^9 n!`;
- full image sets for `1<=k<=5` through source rank nine;
- every feasible explicit section and target fibre through source rank eight;
- recursive clock witnesses through rank nine;
- 1,228,181 exact assertions.

The verifier implements the literal endpoint-zero map, checks image **sets**
rather than only sizes, and compares brute source fibres with a separate
subset-DP linear-extension calculation.  Enumeration is correctly presented
as falsification pressure, not proof.

### Cold source-only build — PASS

A fresh temporary directory containing only `main.tex` and `references.bib`
was built with

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

The resulting PDF is byte-identical to the checked-in `main.pdf`:

```text
pages       4
bytes       368101
SHA-256     c72edb2a165b959d1e9b9410e7f4d70dd630d289b41b351a996779811677c1ad
```

The round-zero file also matches its recorded hash
`2cbd557258087f59dc5a378a379137b137d85a0d767a20da6f919bb47d0e8dcd`.
All four bibliography entries are cited and resolved.  The final log has no
undefined citation/reference, bad-box, or multiply-defined-label warning.
`pdfinfo`, `pdffonts`, and text extraction succeed; all fonts are embedded and
subsetted; author/title/date metadata are suppressed as recorded.  All four
pages were rasterized and visually inspected; no clipping, collision, or
unreadable table was found.  `qpdf` was not installed in the review
environment, so no additional `qpdf --check` result is claimed.

No placeholder or TODO token was found.  Counts, page total, byte count, and
hashes agree across manuscript, transcript, control ledger, and build ledger.

## Freeze recommendation

Do **not** freeze the present source unchanged.  Freeze is recommended after
the Major 1 convention/owner repair and the two minor repairs, followed by one
cold verifier replay and a refreshed deterministic build.  The mathematical
theorem surface itself needs no contraction: all-rank images, explicit
every-target right sections (including `n=1` and arbitrarily large `k`), the
sharp logarithmic clock with equality witnesses, and the comparison-poset
fibre all survive independent re-derivation.

