# P156 independent hostile review B

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal cold reader; did not author P156
and did not perform Hostile Review A.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`.  No manuscript, proof package, or review
text was sent to an external model, service, specialist, or author.

## Verdict

**REVISE — 0 Critical / 0 Major / 1 Minor.**

The Round-1 mathematical package survives fresh falsification.  I independently
rederived the exact image threshold, the piecewise every-target fibre formula
including both rank boundaries, identity-only recurrence, and the locally
minimum Fibonacci right-inverse ray.  Both Review-A findings are implemented
in the theorem source and executable controls rather than merely marked fixed.
The false pointwise clock remains withdrawn, and neither a global maximum clock
nor global multi-step preimage optimality has reappeared.

A fresh verifier process executed all 3,689,489 assertions and reproduced the
frozen transcript byte for byte.  A source-only four-command build reproduced
`main.pdf` and `main_round1.pdf` byte for byte at SHA-256
`7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979`.
All four rendered pages, settled logs, metadata, text, and font embedding pass.

The sole defect is a local artifact-ledger count.  The Round-1 PDF has 27
`pdffonts` rows, all embedded, subsetted, and Unicode-enabled, whereas
`BUILD.md` and `FINAL_QA.md` say 26.  The number 26 was correct for the Round-0
PDF and was carried into the Round-1 records after the final-page declaration
introduced one additional font object.  This does not affect the PDF itself,
but the two current QA records must be corrected before internal acceptance.

This report is read-only with respect to all author artifacts.  Its creation is
the only paper-local change made by the reviewer.

## 1. Frozen-ceiling and Round-1 comparison

| Frozen interface | Round-1 source | Fresh result |
|---|---|---|
| retain exactly the letters `pi_i>=i`, in order, then standardize | equation (1) | PASS; position one makes every output nonempty |
| `sigma in W(S_n)` iff `n>=m+d(sigma)` | Theorem 1(i), equation (6) | PASS in both directions, including equality `h=d` |
| high-shift/low-tail section and exact minimum source rank | equations (7), (13) | PASS; minimum is target- and one-step-specific |
| every-target fibre at every `n>=1` | Theorem 1(ii), equations (4), (5), and (8) | PASS; now literally piecewise at `n<m` and `n>=m` |
| empty product and same-rank boundary | definition after (5), theorem and proof | PASS; fibre one only for `id_m` at `n=m` |
| identity-only recurrence and strict rank loss | Theorem 1(iii) | PASS |
| canonical inverse update `(m,d)->(m+d,m)` | Theorem 1(iv), equations (9)--(10) | PASS |
| Fibonacci resources and exact tail shift | equations (11)--(12) | PASS for every `t>=1` |
| local one-step rank minimality only | paragraph after Theorem 1 | PASS; no compositional optimum is inferred |
| false pointwise clock withdrawn | Limitations and exact rank-11 witness | PASS; the falsifier is reproduced |
| global maximum clock and global iterated optimum excluded | abstract, theorem aftermath, Limitations, transcript | PASS; neither is claimed or tested |
| static owners and Bell identity aggregate zero-credit | setup and equation (3) | PASS; the residual conjunction is not enlarged |
| external-status boundary | final declaration | PASS; literal `HOLD_EXTERNAL` is visible |

The paper remains within the reframed freeze.  Its contribution surface is the
conjunction of target-resolved images, target- and rank-resolved fibres, and the
dynamics of one chosen minimum-one-step section.  None of the zero-credit
static inputs is repackaged as an independent contribution.

## 2. Independent mathematical rederivation

### 2.1 Carrier, maximum drop, and exceptional identities

For every `pi in S_n`, `pi_1>=1`; hence the retained word is nonempty and its
standardization lies in some `S_m` with `1<=m<=n`.  Therefore the rule is a
self-map of each finite carrier `S_{<=N}` for every `N>=1`, exactly as the
Round-1 source now quantifies it.

For any permutation `sigma`, the coordinate differences
`i-sigma_i` sum to zero, so their maximum is nonnegative.  If
`d(sigma)=0`, then all `sigma_i>=i`; equality of coordinate sums forces every
coordinate to be equal, hence `sigma=id_m`.  Thus every nonidentity target has
strictly positive drop, as required by the inverse-ray construction.

### 2.2 Exact image obstruction and equality case

Assume `W(pi)=sigma`, where the selected positions and selected values are

```text
P={p_1<...<p_m},        A={a_1<...<a_m}.
```

Standardization forces position `p_i` to contain `a_(sigma_i)`.  Since `p_i`
is the `i`th selected position and is selected,

```text
i <= p_i <= a_(sigma_i).
```

Write `h=n-m`.  Among the integers at most `a_j`, exactly `j` belong to the
selected value set at or before its `j`th member, and at most all `h`
complement values can also occur there.  Hence `a_j<=h+j`.  Substitution gives

```text
i <= h+sigma_i,        i-sigma_i <= h,
```

for every `i`, so `d(sigma)<=h`.  This proves necessity without division,
asymptotics, or a generic Ferrers result.

Conversely, if `h>=d(sigma)`, the word

```text
(sigma_1+h,...,sigma_m+h,1,...,h)
```

is a permutation of `[m+h]`.  Each high entry satisfies
`sigma_i+h>=i` and is retained; low value `j` occurs at position `m+j>j` and
is strictly deficient.  The retained word is a shifted copy of `sigma`.
At the equality boundary `h=d`, every coordinate attaining maximum drop lies
exactly on the diagonal and is still retained because the predicate is weak.
Thus the iff and exact minimum source rank `m+d(sigma)` both hold.

### 2.3 Piecewise fibres, empty product, and every inverse direction

If `n<m`, output rank cannot exceed source rank, so the fibre is zero.  This is
now a literal branch of equation (8), not an implicit convention.

For `n>=m`, fix selected sets `A` and `P`.  Their selected assignment is
forced: `p_i` receives `a_(sigma_i)`.  It is retained precisely when
`p_i<=a_(sigma_i)` for all `i`.  Let `B=[n]\\A` and let the complement
positions be `Q={q_1<...<q_h}`.  At step `j`, exactly

```text
#{b in B:b<q_j}-(j-1)
```

unused values are eligible.  Indeed, every previously used complement value
was assigned below an earlier `q_k<q_j`, so it lies in the counted eligible
set.  Multiplication therefore counts every deficient complement bijection
once.  A nonpositive factor gives zero.  The selected sets and complement
assignment are uniquely recoverable from a source, so both directions of the
decomposition are injective and exhaustive.

At `n=m`, both complements are empty and the now-declared empty product is
one.  The sole candidate has `A=P=[m]`; its inequalities are `i<=sigma_i` for
all `i`, which force `sigma=id_m` by the sum argument.  Thus the same-rank
fibre is exactly one for the identity and zero for every nonidentity target.
This closes all boundary cases raised in Review A.

### 2.4 Recurrence

Equal input and output rank means every position was retained, so
`pi_i>=i` for all `i`.  Equal coordinate sums force `pi=id_n`.  Identities are
fixed; every other step strictly lowers positive rank.  Therefore a finite
cutoff has exactly its identities as recurrent states and no hidden cycle.

### 2.5 Canonical inverse update, Fibonacci powers, and tail shift

For a nonidentity target with resources `(m_t,d_t)`, use the sharp section at
`h=d_t`.  Its shifted high entry at position `i` has drop

```text
i-(sigma_i^(t)+d_t) <= d_t-d_t = 0,
```

whereas low-tail value `j` at position `m_t+j` has drop exactly `m_t`.
Consequently

```text
(m_(t+1),d_(t+1))=(m_t+d_t,m_t),
W(sigma^(t+1))=sigma^(t).
```

The image theorem, applied separately at each edge, proves minimum source rank
for that one immediate target.  It supplies no minimum over all `t`-step
preimages, and the source explicitly says so.

Powers of `[[1,1],[1,0]]` yield

```text
m_t=F_(t+1)m+F_t d,
d_t=F_t m+F_(t-1)d
```

for every `t>=1`.  Each lift is nonidentity and maps in one step to the prior
state, so first-hitting times satisfy `tau(sigma^(t))=tau(sigma)+t`.  This is an
exact chosen backward ray, not an upper bound on arbitrary forward orbits.

### 2.6 Withdrawn pointwise clock

For

```text
pi=(11,10,9,4,1,2,3,8,5,6,7),
```

the retained word standardizes to `(5,4,3,1,2)` and `d(pi)=4`.  Direct
iteration gives target tail three, while exhaustive rank-four iteration gives
maximum tail two.  Hence the old pointwise comparison is genuinely false.
The manuscript confines it to the Limitations paragraph, labels it false, and
does not use the Fibonacci inverse ray to infer either an unproved size-only
clock or a global preimage optimum.

## 3. Review-A closure audit

### A-m1: quantified fibre boundaries — closed in source and execution

- The carrier is explicitly quantified by `N>=1` in the setup.
- Theorem 1(ii) now begins “For every source rank `n>=1`” and has a literal
  `0` branch for `1<=n<m`.
- The definition states that the `h=0` product is one.
- The theorem and proof both identify the same-rank identity fibre and exclude
  every nonidentity target.
- `verify_p156.py` has separate `n<m` and `n=m` loops rather than relying on
  the original `n>=m` board lane.
- Fresh execution reported exactly 316,646 lower-rank cells and 46,233
  same-rank cells.
- The regenerated transcript, proof package, claims ledger, control report,
  narrative, README, build record, and QA records all expose the repaired
  boundary interface.

### A-m2: manuscript-level external status — closed visibly

The source now ends its declarations with a literal External Status paragraph
containing `HOLD_EXTERNAL` and explicitly withholding posting, submission,
external circulation, and specialist or author contact.  It is visible and
legible on rendered page four.  PDF title, author, subject, and keyword
metadata remain blank, and `Anonymous` is the only displayed author identity.

No Review-A repair broadened a theorem, revived a clock, or changed the owner
subtraction.

## 4. Owner and portfolio attacks

### 4.1 Direct and nearby ownership

The exact direct collision remains fully subtracted.  Beyene--Backelin--
Mantaci--Fufa Theorem 27 owns the Bell enumeration of permutations whose
weak-excedance-letter subword is increasing, which in this notation is

```text
sum_m |W_n^(-1)(id_m)| = B_n.
```

The manuscript cites it at theorem level, marks it unclaimed, and uses its
finite recovery only as a zero-credit consistency control.  Baril's
transposition-array interface is also subtracted.

The remaining cited sources own excedance-set statistics, maximum-drop and
bounded-drop enumeration, permutation-tableau structure, and weak-excedance
position/value Bruhat classes.  Generic standardization, Ferrers matching,
rank descent, and Fibonacci matrix powers are standard tools and receive no
standalone contribution credit.  All eight bibliography records are cited and
the cold BibTeX build resolves them.

The paper's residual is narrower: the exact target obstruction for this
literal extractor, the target/rank-resolved completion sum, and the dynamics
of one canonical section.  The local source ledger records only a bounded
exact-map non-hit.  I do not treat it as evidence of novelty, priority,
ownership completeness, or clearance; discovery of a direct equivalent-map
owner would reopen the gate.

### 4.2 Portfolio collision

- **P149:** both maps standardize a selected permutation subword, a generic
  carrier overlap receiving no separation credit.  P149 selects
  endpoint-inclusive local maxima and uses alternating peak packing and
  comparison-poset fibres.  P156 uses an absolute diagonal predicate,
  maximum-drop obstruction, and deficient complement boards.  Its inverse
  update is not a consequence of P149's forward peak clock.
- **P155:** both are rank-changing permutation maps with target sections and
  fibres.  P155 reads maxima of cycle supports ordered by minima, has threshold
  `2m-rlmin(sigma)`, and factorial ordered-support weights.  P156 has threshold
  `m+d(sigma)` and selected position/value Ferrers completions.  Only P156
  freezes the canonical Fibonacci inverse ray; P155's power clock is excluded.
- **P152:** a fixed-carrier stochastic triangular-book process, marked
  Chebyshev transform, and mean/parity inverse have no literal update or proof
  engine in common with P156.
- **P153:** finite-field factorial collapse on a fixed plane uses residue
  products and temporal coordinate fibres, not diagonal permutation
  extraction.
- **P154:** iterated subgroup normalizers use two-adic halving forests and an
  arithmetic unlabelled-graph signature, not standardization or Ferrers
  completion.
- **P1--P151 beyond P149:** the historical occupancy ledger reveals no other
  literal diagonal weak-excedance extractor.  Generic rank-changing,
  functional-graph, exact-fibre, or inverse language is not counted as
  separation or contribution.

The system and proof fingerprint therefore passes the portfolio gate under
the stated bounded evidence rule.

## 5. Fresh exact execution

I ran, in a fresh process with bytecode disabled,

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p156.py
```

Fresh stdout had SHA-256

```text
5c78864527c5781da43f79f8b2b667f9d915fd13fadaea09abe6a7c49f76f53e
```

and was byte-identical to `verification_output.txt`.  The decisive terminal
and boundary fields were

```text
fibre_n_lt_m_boundary_cells=316646
fibre_n_eq_m_boundary_cells=46233
pointwise_drop_clock=FALSE_COUNTEREXAMPLE_REPRODUCED
global_maximum_clock=NOT_CLAIMED
global_iterated_preimage_minimality=NOT_CLAIMED
boxes=40
assertions=3689489
status=PASS
```

The run also covered 409,113 literal states through rank nine, 99,451 image
cells, 1,704 constructive sections, 6,985 board-formula fibre cells, and six
inverse levels for all 46,225 nonidentity targets through rank eight.

As a separate implementation that did not import `verify_p156.py`, I
enumerated 873 sources through rank six and independently reconstructed the
literal map, image sets, fibre products, hitting times, and lifts.  It checked
1,072 image cells, 1,072 full fibre cells, 4,166 `n<m` cells, 873 same-rank
cells, and 4,335 tower edges; all passed, including the rank-11 clock
falsifier.

Neither computation proves the all-rank theorems, completes the owner search,
establishes novelty or priority, proves either excluded global statement, or
authorizes external release.  Their role is bounded exact counterexample
pressure and regression control.

## 6. Source-only build, PDF, and manifest audit

A fresh temporary directory was populated with only `main.tex` and
`references.bib`, then executed exactly

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

All four commands exited zero.  The settled log has no unresolved citation or
reference, rerun request, duplicate label, build warning, overfull box, or
underfull box.  The resulting PDF is byte-identical to both current
`main.pdf` and `main_round1.pdf`:

```text
pages=4
bytes=336311
SHA256=7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979
```

The author freeze is preserved separately:

```text
main_round0_original.pdf
SHA256=ee5cedd089d9d837839f9fc715aae9530e19fc4f414dfcbef77ad0adfafa256c
```

The Round-1 PDF is A4, unencrypted, has no form, JavaScript, metadata stream,
or embedded file, and contains no volatile creation/modification date.  Its
title, author, subject, and keyword metadata are blank.  Text extraction found
no workspace path, account, affiliation, email, ORCID, or identifying
acknowledgment.

All four pages were independently rasterized and inspected.  The piecewise
fibre theorem, same-rank proof, inverse formulas, numerical control paragraph,
withdrawn counterexample, seven house declarations including External Status,
and eight references are legible.  There is no clipping, overlap, broken
formula, unresolved marker, corrupt glyph, or identifying author information.

Before this report was written, `SHA256SUMS` contained exactly the 28 other
paper-local files, excluded itself, passed `sha256sum -c`, and agreed exactly
with a filesystem enumeration.  Adding this Review-B report necessarily makes
that pre-review manifest incomplete; final closure must regenerate it after
all Round-2 records are frozen.

### Font evidence and the one finding

`pdffonts` reports:

```text
Round 0: 26 rows
Round 1/current/source-only replay: 27 rows
Round 1 non-embedded, non-subsetted, or non-Unicode rows: 0
```

Thus font integrity passes, but the current author ledgers' numerical count
does not.

## 7. Finding and required repair

### m1 — Minor: Round-1 font-row count retained the Round-0 value

**Evidence.**  `BUILD.md` says “all 26 reported font rows” and `FINAL_QA.md`
says “All 26 font rows are embedded.”  Independent `pdffonts` runs on
`main.pdf`, `main_round1.pdf`, and the byte-identical source-only replay each
report 27 rows.  All 27 have `emb=yes`, `sub=yes`, and `uni=yes`.  The preserved
Round-0 PDF has 26 rows, which explains the stale value.

**Severity.**  Minor artifact-provenance defect only.  There is no missing
font, visual defect, metadata leak, mathematical problem, or reproducibility
failure.

**Required repair.**  Correct the Round-1/current count from 26 to 27 in
`BUILD.md` and `FINAL_QA.md`; leave the historical Review-A statement about its
Round-0 PDF unchanged.  Record this Review-B disposition in
`IMPROVEMENT_LOG.md`, freeze `main_round2.pdf` byte-identical to `main.pdf` if
the manuscript source remains unchanged, and regenerate the complete final
manifest after all records exist.

## 8. Internal disposition

P156 is **not yet `ACCEPT_INTERNAL`** solely because the protocol requires
zero unresolved Minor items.  After the one ledger correction is documented
and the Round-2/manifest invariant is frozen, no further mathematical,
ownership, computational, build, visual, anonymity, or external-status issue
identified by this review remains.

This review makes no novelty, priority, authorship, posting, circulation,
specialist-contact, submission, or release claim.  External status remains
`HOLD_EXTERNAL`.
