# HOSTILE REVIEW B — P149

**Manuscript:** *Iterated Endpoint-Peak Extraction on Permutations: All-Rank Images, Sections, and a Sharp Clock*  
**Review role:** independent Review B; the reviewer did not author P149 or Review A  
**Date checked:** 2026-09-01 UTC  
**External status:** `HOLD_EXTERNAL`

## Verdict

**REVISE**

| severity | count | disposition |
|---|---:|---|
| Critical | 0 | No theorem was falsified, the exact verifier is reproducible, and the bounded audit did not locate an owner of the surviving iterative theorem conjunction. |
| Major | 1 | The Review-A repair assigns the exact two-zero endpoint convention to Fu 2018, but Fu's literal definition admits the left endpoint and excludes the right endpoint.  The direct-owner ledger is therefore still materially false. |
| Minor | 1 | `BUILD.md` labels a pre-hostile intermediate hash as “Current” and later records a different actual current hash. |

The mathematical package survives independent rederivation.  The manuscript is
not releasable because the source subtraction on which the repaired positioning
depends is wrong.  This is a Major rather than a Critical finding: the incorrect
attribution concerns a static statistic that the manuscript already assigns zero
contribution credit; it does not provide an owner of the ordered standardized map,
its iteration, all-rank sections, or sharp clock.

## 1. Required Major repair: Fu 2018 is not an exact-convention owner

### 1.1 Literal source check

P149 sets

```text
pi_0 = pi_(n+1) = 0
```

and permits a peak at either endpoint.  In contrast, the official publisher text
of Amy M. Fu, *A Context-Free Grammar for Peaks and Double Descents of
Permutations*, defines an exterior peak only when

```text
i = 1 and pi_1 > pi_2,
or 1 < i < n and pi_(i-1) < pi_i > pi_(i+1).
```

There is no `i=n` clause.  See the definition in the
[Elsevier primary record and full text](https://www.sciencedirect.com/science/article/pii/S0196885818300745)
and the [author-submitted arXiv record](https://arxiv.org/abs/1801.04397).
Fu appends a zero on the right for the grammatical labeling, but that appended
symbol does not turn the last permutation entry into an exterior peak.

The two rules disagree already on `pi=12`:

```text
P149: Peak(12) = (2), because 1 < 2 > 0;
Fu:   no exterior peak, because the last position is excluded.
```

Consequently, all of the following current statements are false as source claims:

- `main.tex`, lines 89--92 and 323--325: Fu uses the exact convention;
- `SOURCE_VERIFICATION.md`, lines 11--20: Fu is the direct two-zero owner;
- `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`,
  `SELF_QA.md`, and `BUILD.md`: the corresponding exact-owner and zero-credit
  assertions;
- Review A, especially its Major-1 repair instruction and owner table.

The Fu bibliographic metadata themselves are correct: *Advances in Applied
Mathematics* **100** (2018), 179--196,
[DOI 10.1016/j.aam.2018.06.004](https://doi.org/10.1016/j.aam.2018.06.004).
The failure is convention/claim attribution, not metadata.

### 1.2 A verified exact-convention replacement exists

Kathy Q. Ji, *The (alpha,beta)-Eulerian Polynomials and Descent-Stirling
Statistics on Permutations*, explicitly assumes
`sigma_0=sigma_(n+1)=0` and defines an exterior peak for every
`1 <= i <= n` satisfying the local-maximum inequalities.  Thus both endpoints
are admitted.  The paper studies the corresponding static distributions and
states that Carlitz and Scoville called these exterior peaks “maxima.”  See
Definition 2.1 and the historical discussion in the
[official Science China Mathematics paper](https://www.sciengine.com/parse/pdf/1674-7283/1A17691E97574ECEAD1E01FA4F0DBCAF.pdf?attname=1A17691E97574ECEAD1E01FA4F0DBCAF.pdf),
*Science China Mathematics* **68** (2025), 2259--2284,
[DOI 10.1007/s11425-024-2362-3](https://doi.org/10.1007/s11425-024-2362-3),
and the [author-submitted arXiv record](https://arxiv.org/abs/2310.01053).

The official EuDML record for the historical paper is L. Carlitz and Richard
Scoville, *Generalized Eulerian Numbers: Combinatorial Applications*,
*Journal fuer die reine und angewandte Mathematik* **265** (1974), 110--137,
[DOI 10.1515/crll.1974.265.110](https://doi.org/10.1515/crll.1974.265.110),
[EuDML record](https://eudml.org/doc/151403).  Before making an earliest-owner
claim, the authors must inspect and quote the literal convention in this original
paper rather than relying only on a later attribution.  Ji 2025 is already a
directly inspected same-object static owner and is sufficient to show that the
current ledger is incomplete.

### 1.3 Required repair

1. Delete every statement that Fu 2018 uses or owns P149's exact two-zero
   convention.
2. Reclassify Fu 2018 as a one-sided exterior/left-peak convention neighbour,
   still at zero contribution credit.
3. Add a directly verified exact-convention static owner, at minimum Ji 2025;
   inspect Carlitz--Scoville 1974 directly before assigning historical priority.
4. Rebuild the direct/same-object/nearest-neighbour ledger in the manuscript and
   every package document listed above.  Preserve zero credit for all static
   distributions.
5. Preserve the surviving claim at its actual conjunction: ordered two-zero
   peak **values**, standardization, iteration, every-iterate images, explicit
   every-target sections, and the sharp every-rank clock.  A bounded non-hit is
   not novelty, priority, clearance, or release evidence.

## 2. Review-A repair checklist

| requested interface | Review-B result | independent check |
|---|---|---|
| Fu exact two-zero convention | **FAIL — Major 1** | Fu excludes the last position; `12` separates the rules. |
| Padding bridge to ordinary pinnacles | **PASS** | For `1,(pi_1+2),...,(pi_n+2),2`, neither padding entry is a peak; each original interior comparison is unchanged; the left and right original entries are ordinary interior peaks exactly under the two zero-boundary tests.  Peak values and their left-to-right order are shifted by two.  The argument also works for `n=1`: `1,3,2` has central peak `3`. |
| Run-sorting statement | **PASS** | The manuscript now says an auxiliary bijection sends the input peak-value set to the peak-value set after run-sorting; it does not claim pointwise invariance of run-sorting.  This matches the [primary arXiv paper](https://arxiv.org/abs/2104.04220). |
| Expanded fixed-set/order ledger | **PASS, subject to Major 1** | Davis--Nelson--Petersen--Tenner, Rusu--Tenner, Diaz-Lopez et al., Domagalski et al., Fang, and Falque--Novelli--Thibon are all cited and assigned zero credit.  They use ordinary interior pinnacles and are connected by the explicit padding bridge, not mislabeled as literal two-zero owners. |
| Journal/DOI metadata | **PASS** | The eight bibliography records match their official journal/DOI or arXiv records.  Fu's role is wrong, but its citation metadata are right. |
| Strict rank-descent wording | **PASS** | The text now distinguishes possible equality in `|P(pi)| <= ceil(n/2)` from the strict inequality `ceil(n/2)<n` for `n>1`. |

The fixed-set/order metadata checked were:

| record | official metadata result |
|---|---|
| Davis et al., *Discrete Mathematics* 341(11), 3249--3270 (2018), [DOI](https://doi.org/10.1016/j.disc.2018.08.011) | PASS |
| Rusu--Tenner, *Graphs and Combinatorics* 37(4), 1205--1214 (2021), [DOI](https://doi.org/10.1007/s00373-021-02306-9) | PASS |
| Diaz-Lopez et al., *Discrete Mathematics* 344(6), 112375 (2021), [DOI](https://doi.org/10.1016/j.disc.2021.112375) | PASS |
| Domagalski et al., *Discrete Mathematics* 345(7), 112882 (2022), [DOI](https://doi.org/10.1016/j.disc.2022.112882) | PASS |
| Fang, *Discrete Mathematics & Theoretical Computer Science* 24(1) (2022), [DOI](https://doi.org/10.46298/dmtcs.8321) | PASS |
| Falque--Novelli--Thibon, *Discrete Mathematics* 347(4), 113834 (2024), [DOI](https://doi.org/10.1016/j.disc.2023.113834) | PASS |
| Alexandersson--Nabawanda, *Enumerative Combinatorics and Applications* 2(1), S2R2 (2022), [DOI](https://doi.org/10.54550/ECA2022V2S1R2) | PASS |

## 3. Independent theorem rederivation

### 3.1 Literal map and one-step packing — PASS

The carrier is the finite disjoint union
`S_<=N = disjoint_union_(1<=n<=N) S_n`.  Standardization makes the selected
distinct-value word a permutation, and the global maximum is selected under the
two-zero boundary convention, so the map is total and nonempty.

Peak positions cannot be adjacent.  Hence a rank-`n` word has at most
`ceil(n/2)` peaks and at least one peak.  For `n>1`,
`ceil(n/2)<n`, so rank strictly descends although the packing bound itself can
be attained.  At `n=1`, the unique state is fixed.

### 3.2 Explicit one-step section — PASS

For `sigma in S_m` and `n>=2m-1`, set

```text
h_i = n-m+sigma_i,
L_(n,m)(sigma) = h_1,1,h_2,2,...,h_(m-1),m-1,h_m,
                  n-m,n-m-1,...,m.
```

The high values are exactly `n-m+1,...,n`; the separators are
`1,...,m-1`; the decreasing tail is the remaining interval.  Each high is a
peak, each separator has a higher neighbour, and each tail entry has a higher
left neighbour.  Therefore the extracted word is `h_1...h_m` and standardizes
to `sigma`.

Boundary checks passed:

- at the minimal length `n=2m-1`, the tail is empty and the final high is a
  peak against the right zero;
- at `m=1`, the lift is the decreasing permutation `n,n-1,...,1`, whose only
  peak is `n`;
- `L_(1,1)` is the identity.

### 3.3 Every-iterate image and sections — PASS

Iterated packing gives

```text
|P^k(pi)| <= ceil(n/2^k),
```

using the standard nested-ceiling identity.  The target condition
`m<=ceil(n/2^k)` is equivalent to

```text
n >= 2^k m - (2^k-1).
```

Backward ranks `a_k=m` and `a_j=2a_(j+1)-1` make every inner lift a minimal
odd lift, while the displayed inequality makes the outer lift legal.  Composing
the one-step sections gives every target of every feasible rank.  Disjointness
of the carrier ranks then gives

```text
P^k(S_n) = disjoint_union_(1<=m<=ceil(n/2^k)) S_m,
|P^k(S_n)| = sum_(m<=ceil(n/2^k)) m!.
```

If a backward rank reaches one, subsequent `L_(1,1)` factors cover arbitrary
larger `k`; there is no hidden assumption that `k<=ceil(log_2 n)`.

### 3.4 Recurrent class and sharp clock — PASS

Strict rank descent off rank one excludes every nontrivial cycle, so the
singleton is the unique recurrent state.  Iterated packing gives the upper
bound `tau(pi)<=ceil(log_2 n)`.  The recursive witness

```text
w_1=1,
w_n=L_(n,ceil(n/2))(w_(ceil(n/2)))
```

is legal for both parities and satisfies
`P(w_n)=w_(ceil(n/2))`.  Induction between consecutive powers of two gives
`tau(w_n)=ceil(log_2 n)`.  The `n=1` value is zero as required.

### 3.5 Complete one-step fibre — PASS

For `n>1`, the comparison word determines endpoint-inclusive peak positions by

```text
{1:w_1=D} union {i: w_(i-1)=U,w_i=D} union {n:w_(n-1)=U}.
```

The adjacent-comparison orientation is acyclic.  All of its peak positions are
maximal, so imposing the target order as a chain among those maxima cannot
create a directed cycle.  Reading a linear extension from low value to high
value bijectively assigns ranks `1,...,n`: the adjacent relations force the
comparison word and the added peak chain forces exactly the standardization
`sigma`.  Comparison-word classes are disjoint, proving the stated sum of
linear-extension counts.  The empty-word case `n=m=1` has one extension; the
infeasible range `m>ceil(n/2)` is empty on both sides.

No theorem-interface error was found.

## 4. Exact verifier and frozen transcript

Cold command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_p149.py
```

Result: **PASS**, byte-identical to `verification_output.txt`.

```text
assertions=1228181
P149_THEOREM_INTERFACES_PASS
```

The replay enumerates all `409,113` permutations through rank nine, compares
full image sets through five iterates, checks every feasible explicit section
through source rank eight, checks the recursive clock witnesses, and compares
every target fibre through source rank eight with independent subset-DP
linear-extension counts.  The printed source-rank image and tail profiles match
the manuscript table.  This is strong counterexample pressure, not proof or
ownership evidence.

## 5. Isolated deterministic build and four-page inspection

A clean temporary directory containing only `main.tex` and `references.bib`
was built with

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The isolated PDF is byte-identical to the checked-in current `main.pdf`:

```text
pages       4 A4
bytes       373097
SHA-256     3a0e734d3edd708d6188406fbb94362658b5f5d690c34cc6897cab6e349a4a9d
PDF version 1.5
```

There are no unresolved citations or references, rerun requests, overfull or
underfull boxes.  All fonts are embedded and subsetted; title and author PDF
metadata are blank.  `main_round1.pdf` is byte-identical to the current PDF,
and the frozen `main_round0_original.pdf` remains distinct at its recorded
round-zero hash.

All four pages were rasterized and inspected at 120 dpi:

1. title, abstract, definition, owner paragraph, and padding display are clear;
2. lift, all-rank theorem, and beginning of the clock theorem are clear;
3. clock proof, fibre theorem, audit table, and conclusion are clear;
4. declarations and all eight bibliography entries are legible.

No clipping, collision, blank page, broken glyph, or bad line break was found.
The visual check cannot cure the false Fu sentence visible near the foot of
page one.

## 6. Minor 1: contradictory “Current” build hash

`BUILD.md` lines 3--9 correctly label a historical section “Pre-hostile build”
but then call the 368,101-byte intermediate hash
`c72edb2a...` the “Current SHA-256.”  Lines 34--36 refer back to “the current
PDF at the SHA-256 above.”  The later hostile-A section correctly records the
actual current artifact as 373,097 bytes with SHA-256 `3a0e734d...`.

Required repair: relabel the old hash unambiguously as a historical
pre-hostile intermediate, remove the backward “current PDF ... above” pointer,
and place the actual current hash in one canonical current-build block.  Keep
the round-zero ledger separate.

## 7. Owner subtraction after this review

| relation to P149 | owner/result | credit boundary |
|---|---|---|
| Direct, exact two-zero **static** peak statistic | Ji 2025; historical trail to Carlitz--Scoville 1974 requires literal original-source confirmation before priority wording | zero contribution credit |
| One-sided exterior/left-peak convention | Fu 2018 | zero contribution credit; not an exact-convention owner |
| Same values/order after explicit padding, but ordinary interior peaks | Davis et al.; Rusu--Tenner; Diaz-Lopez et al.; Domagalski et al.; Fang; Falque--Novelli--Thibon | zero contribution credit |
| Size-preserving run-sorting neighbour | Alexandersson--Nabawanda auxiliary-bijection equidistribution | zero contribution credit; no pointwise-invariance claim |
| Generic comparison-word posets and linear extensions | standard method background | zero contribution credit; fibre axis remains secondary |
| Surviving conjunction | ordered two-zero peak-value word + standardization + iteration + every-iterate exact images + explicit every-target sections + sharp every-rank clock | mathematically survives; bounded owner-search non-hit only |

## 8. Release decision

P149 remains **`HOLD_EXTERNAL`**.  After Major 1 and Minor 1 are repaired, the
source ledger, manuscript wording, package summaries, verifier transcript, and
fresh deterministic PDF must be checked together.  Review B does not authorize
submission, posting, specialist contact, priority language, or external release.

