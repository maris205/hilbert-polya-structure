# P162 Hostile Review B — Round 1

**Review date:** 2026-09-03 UTC  
**Frozen artifact:** `main_round1.pdf`  
**Round-1 SHA-256:** `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62`  
**Independent verdict:** **ACCEPT_INTERNAL / HOLD_EXTERNAL**  
**Severity:** **0 Critical / 0 Major / 0 minor**

## 1. Independence and artifact boundary

I did not author P162 and did not perform Hostile Review A.  I read the
Review-A report only to identify its requested repair.  I did not read,
import, execute, or copy the author verifier or the Review-A checker.  The
Review-B verifier was written independently from the literal subset map and
the frozen theorem statements.

Input hashes were pinned before derivation in
`docs/papers162_166_sequence/reviews/p162_b/PINNED_INPUTS.sha256`.  The saved
Round-0 PDF still has the hash recorded by Review A,
`e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46`.
The current `main.pdf` is byte-identical to `main_round1.pdf`.

Review A's only finding is closed.  The Round-1 abstract says “a sharp
worst-non-full-source emptying clock,” matching the theorem's quantifier
`A_0 != V`.  After normalizing whitespace and line-break hyphenation, the
Round-0 and Round-1 PDF text becomes identical when precisely that phrase is
replaced; no theorem, equation, or proof content changed.  The reviewer
verifier also pins both PDF hashes and asserts the corrected abstract phrase.

## 2. Independent theorem re-derivation

### 2.1 History-span identity

For subspaces `H,K <= V`, distributing the intersections gives

```text
E_K(E_H(A)) = intersection_(k in K,h in H) (A+h+k) = E_(H+K)(A).
```

Because `<v>={0,v}` over `F_2`, a literal update
`A -> A intersection (A+v)` is `E_<v>(A)`.  Induction therefore proves

```text
A_t = E_<v_1,...,v_t>(A_0)
```

for every history, including the empty history.

### 2.2 Rank law and mean

For a fixed `r`-space `H`, a length-`t` history spans `H` exactly when the map
`F_2^t -> H` sending the standard basis to the sampled vectors is onto.  The
number of such maps is

```text
S(t,r) = product_(i=0)^(r-1) (2^t-2^i).
```

Multiplying by the Gaussian number of `r`-subspaces and dividing by `2^(dt)`
gives the displayed rank law.  At rank `r<d`, the next sample increases rank
with probability `1-2^(r-d)`.  Solving the exact rank-chain hitting equations
gives

```text
E sigma = sum_(r=0)^(d-1) 1/(1-2^(r-d)),
```

with the empty value zero at `d=0`.

### 2.3 Two fixed states and the sharp non-full witness

If a state is fixed by every update, then `A subset A+v` for every `v`.
Cardinality forces translation invariance, and transitivity leaves only
`empty` and `V`.  Conversely, both are fixed.

Once the history span is `V`, every non-full source erodes to empty.  The
bound is sharp because

```text
E_H(V\{0}) = V\H.
```

The witness therefore empties exactly at the full-span time.  The full-rank
history count yields the stated CDF, including the `t<d` support hole.

### 2.4 Every-target source-size/history polynomial

For a fixed span `H`, `E_H(A)` is the union of exactly those `H`-cosets wholly
contained in `A`.  A target `B` is possible if and only if
`H <= Stab(B)`.  If `dim H=r`, its `b/2^r` target cosets are forced into the
source, while each outside coset may be any proper subset.  Hence the exact
fixed-span polynomial is

```text
z^b ((1+z)^(2^r)-z^(2^r))^(2^(d-r)-b/2^r).
```

There are `[s choose r]_2` eligible subspaces inside `Stab(B)` and `S(t,r)`
ordered histories spanning each one.  Summation gives equation (8) exactly.
This proves both directions of the stabilizer filter; it does not confuse
target invariance with source invariance.

### 2.5 One-step boundary and recovery

At one step, the zero vector supplies the rank-zero contribution one.  Every
nonzero vector in an `s`-dimensional stabilizer supplies one rank-one history,
and each outside two-point coset has three proper subsets.  Thus

```text
F_1(B;1) = 1                                      if s=0,
F_1(B;1) = 1+(2^s-1)3^(2^(d-1)-b/2)             if s>=1.
```

The separate `s=0` branch is necessary for odd `b`.  At fixed `(d,b)`, the
power of three is constant and positive, so the second expression is strictly
increasing in `s`; its value is greater than one.  The phase size
`2^(2^d)` first recovers `d`, and the one-step mass then recovers `s`.

The full formal derivation is frozen in
`docs/papers162_166_sequence/reviews/p162_b/PROOF_PACKAGE.md` with status
**PROVABLE AS STATED**.

## 3. Boundary attacks

| boundary | independent result |
|---|---|
| `d=0` | The one-point vector space has two subset states, both universally fixed; the unique history symbol is zero; the empty/full target polynomials are `1` and `z` at every time. |
| `t=0` | Only rank zero contributes; every target has the singleton source polynomial `z^|B|`. |
| `s=0` | The one-step mass is exactly one.  No half-integral exponent is evaluated; all odd-cardinality targets tested lie in this branch. |
| `B=empty` | The coefficient of `z^0` is `2^(dt)`, one empty source for every history; all higher source sizes are handled by proper subsets of every span coset. |
| `B=V` | The only source is `V`, and all `2^(dt)` histories reach it, giving `2^(dt)z^(2^d)`. |
| `t=1` | Zero and nonzero stabilizing translations give exactly the two branches above. |
| `t<d` | Full rank, hence witness emptying, has probability zero. |
| `t>=d` | The full-rank count equals the displayed product, including repeated/zero sampled vectors. |

No parameter edge, exponent-integrality failure, or support mismatch was
found.

## 4. Independent verifier

Review-B evidence is under
`docs/papers162_166_sequence/reviews/p162_b/`:

- verifier: `verify_review_b.py`;
- verifier SHA-256:
  `8ac14dbe2fbbf702fbe1d17c1b2e5f4eb38ba6ba91c4998161db4071ad9788d9`;
- canonical SHA-256:
  `5336e04c02400191176ff9764aafc866cc280703902f44474f2b8ac09b44ccfd`;
- replay 1 SHA-256:
  `5336e04c02400191176ff9764aafc866cc280703902f44474f2b8ac09b44ccfd`;
- replay 2 SHA-256:
  `5336e04c02400191176ff9764aafc866cc280703902f44474f2b8ac09b44ccfd`.

The two fresh outputs are byte-identical to one another and to the canonical
transcript.  The run executes **2,275,862 exact assertions**, including:

- literal history versus span erosion for every source-history pair through
  `d=3,t=4` (1,048,576 pairs in the largest box);
- every target and every source-size coefficient in all literal boxes;
- independent fixed-span polynomials for all subspaces and targets through
  `d=3`;
- exact rank histograms through `d=4`, and symbolic normalization/full-rank
  support through `d=8,t=12`;
- all 2,825 subspaces of `F_2^6` for the sharp witness;
- the exact two-state universal fixed classification through `d=4`;
- every one-step target through `d=4`, including 62,464 trivial-stabilizer
  targets at `d=4`, with recovery and monotonicity checks;
- named tests for `d=0`, `t=0`, `s=0`, `B=empty`, `B=V`, and `t=1`;
- the pinned Round-0/Round-1 hashes and Review-A abstract repair.

Reproduction command:

```bash
python3 docs/papers162_166_sequence/reviews/p162_b/verify_review_b.py
```

## 5. Owner and P1--P165 collision audit

The manuscript's subtraction boundary is accurate:

- Heijmans--Ronse and Heijmans--Serra own the translation-erosion algebra and
  morphology iteration;
- Sivakumar--Goutsias supplies the stochastic-morphology background;
- Balakin supplies the finite-field random-rank owner lane.

These ingredients receive zero contribution credit.  The residual is the
specific conjunction of the sharp witness, the target-stabilizer filter, the
proper-subset coset polynomial resolving every target and source size, and
the one-step recovery law.  A fresh bounded search found no primary source
stating that conjunction; this non-hit is not a novelty, priority, or
freedom-to-publish conclusion.

Internally, P109 and P115 occupy deterministic finite-linear/subspace
dynamics, P128 occupies deterministic translation/GCD erosion, and P158
occupies random cut intersections.  P158 is the nearest stochastic silhouette,
but its complement-history bicluster fibres do not transfer the affine-coset
proper-subset proof.  P163--P165 use distinct carriers and proof engines.  No
P1--P165 literal or proof-engine duplicate of the residual package was found.

All four citations resolve and agree with the inspected primary records;
BibTeX reports zero warnings.  Details are frozen in
`docs/papers162_166_sequence/reviews/p162_b/OWNER_AUDIT.md`.

## 6. Round-1 cold builds and PDF QA

Two fresh source-only directories each received only `main.tex` and
`references.bib`.  Both completed
`pdflatex -> bibtex -> pdflatex -> pdflatex`.  Their final PDFs and logs are
byte-identical; each PDF is also byte-identical to `main_round1.pdf`.

```text
pages / format:     4 / A4
bytes:              399,828
PDF SHA-256:        730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62
final log SHA-256:  6d1f0c19174359b3eb5a42600fc4fd7e077938069479eb760f31e5db8ad62b89
fonts:              30/30 embedded, subsetted, Unicode mapped
final warnings:     0
BibTeX warnings:    0
```

Every page was rendered at 150 dpi and inspected at original resolution.
There is no clipping, overlap, malformed equation, missing glyph, broken URL,
or running-head/footer collision.  Page 4's remaining white area is the
natural end after the four references.  PDF title, author, subject, and
keyword metadata are blank.  The visible byline is `Anonymous`, no identity
leak was found, and `HOLD_EXTERNAL` is visible in both the abstract and final
lifecycle section.  Full receipts are in
`docs/papers162_166_sequence/reviews/p162_b/BUILD_QA.md`.

## 7. Findings

### Critical

None.

### Major

None.

### minor

None.

## 8. Final recommendation

**ACCEPT_INTERNAL — 0C / 0M / 0m.**  The Round-1 artifact closes Review A's
only finding; all theorem components and all hostile boundaries survive an
independent derivation, independent exact verifier, fresh owner/collision
audit, two source-only cold builds, and full PDF QA.  No source repair is
requested.  Maintain **HOLD_EXTERNAL**: this report does not authorize
posting, circulation, submission, or author contact.
