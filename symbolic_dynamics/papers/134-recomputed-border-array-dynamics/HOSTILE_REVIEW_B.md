# Hostile Review B — whole-array recomputation of border arrays

**Review date:** 2026-09-01  
**Review posture:** independent definition-level reconstruction of the current
round-one package, supplemented by a separate xhigh hostile audit  
**Secondary audit task:** `/root/alg_root_hostile_gate/p134_round_b_math_audit`  
**Mathematical verdict:** **`GO`**  
**External-release verdict:** **`HOLD_EXTERNAL`**

## Severity ledger

- **Critical:** 0
- **Major:** 0
- **Minor:** 2

No theorem gap, false boundary, witness failure, fibre error, or provenance
break was found.  The two findings are documentary: an internal paragraph
pointer became false after the Review-A insertion, and two package-index
documents still describe the now-superseded round-zero/deferred-review state.

## Artifacts reviewed

I read the current manuscript and bibliography, all planning/evidence/control
documents, the full paper-local verifier and frozen raw stdout, Hostile Review
A and its improvement log, both frozen PDFs, and the live build records/logs.
The independent secondary reviewer separately reconstructed the theorem
package and ran a definition-level census without importing the paper's
verifier.

Current hashes are:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `f14a1e2a10f51acf800fb922b073a0a8b227f1b9f5b2196535b5ba380f0ac4a3` |
| `references.bib` | `1efd506b8a7be8c8ff7591b7fd6af924f700cf05b7354bda1fa3e6d0e1a133fb` |
| `code/verify.py` | `3aec6dd12c1e9472e1734061ba4c006d94e2e94a6d255f7dede25464cb7d162d` |
| `code/verification_output.txt` | `cce8c343276f5a299cb2c723e8b1957020749f74ff36a9aeb8462253c4b34d3e` |
| `main.pdf` | `d1c1ed8fe7667bb192c6c00e59259e1a80403c5a18e52735be99e907c7662525` |
| `main_round1.pdf` | `d1c1ed8fe7667bb192c6c00e59259e1a80403c5a18e52735be99e907c7662525` |
| `main_round0_original.pdf` | `958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829` |

Byte comparisons give

```text
cmp(main.pdf, main_round1.pdf)          = 0
cmp(main.pdf, main_round0_original.pdf) = 1
```

This agrees with the round-one build and improvement records.

## Fresh exact-control replay

I replayed the verifier from the current package without creating bytecode:

```bash
PYTHONDONTWRITEBYTECODE=1 bash -c \
  'cmp -s code/verification_output.txt <(python3 code/verify.py)'
```

The exit status was **0**, so the raw stdout is byte-for-byte reproducible.
The frozen run reports:

```text
EXHAUSTIVE_RANGE=n=1..9
STATES=409113
TARGET_CELLS=409113
STANDARDIZATION_CASES=3279
LARGE_WITNESS_SIZES=29
ASSERTIONS=1694506
STATUS=PASS
```

The secondary reviewer independently implemented the border definition and
exhausted the full carrier through `n=9`.  Its state/image/recurrent/depth/
valid-depth/maximum-fibre profiles matched the frozen transcript at every
length and ended in `independent_full_status=PASS`.  This is additional
counterexample pressure, not a substitute for the following all-length proof
audit.

## Definition-level reconstruction

### 1. Literal map and the failure-link firewall

For a word `w`, `beta_i(w)` is the longest proper prefix of
`w_0...w_i` that is also its suffix.  On

```text
E_n = {(e_0,...,e_(n-1)): 0 <= e_i <= i},
```

the paper defines the whole-array self-map `Pi_n(e)=beta(e)`.  Closure is
immediate because a proper border of a prefix of length `i+1` has length at
most `i`.

This is not scalar failure-link descent.  The classical operation fixes one
original word and follows `k -> beta_(k-1)(w)` inside its table.  Here the
complete integer table becomes a new word before the next border computation:

```text
e -> beta(e) -> beta(beta(e)) -> ... .
```

The manuscript keeps that distinction explicit in its definition, displayed
orbit, abstract, and limitations section.  No theorem silently switches to the
classical scalar interpretation.

### 2. Exact image

Every output is a valid border array by definition.  Conversely, given a word
realizing a valid table, relabel its letters `0,1,2,...` in order of first
occurrence.  A label first appearing at position `i` is at most `i`, so the
standardized word lies in `E_n`.  Standardization preserves every equality and
inequality of positions, hence every prefix/suffix equality and the entire
border array.  This proves surjectivity onto all valid arrays, not just an
inclusion.

### 3. Canonical exact two-cycles

For `1 <= r < n`, let

```text
A_r = (0,1,...,r,0,...,0),
B_(r+1) = (0,...,0,1,...,1), with r+1 initial zeros.
```

In `A_r`, the initial distinct slope has no nonempty border.  Every later zero
gives border one, and a longer suffix would begin with two zeros rather than
the prefix `01`.  Thus `Pi_n(A_r)=B_(r+1)`.

In `B_(r+1)`, the initial zero prefixes have longest borders
`0,1,...,r`.  Once the one-run begins, a suffix starting in the initial zero
run has fewer leading zeros than the prefix, while a suffix inside the one-run
does not start with zero.  Hence all later borders vanish and
`Pi_n(B_(r+1))=A_r`.  The states are distinct, including the endpoint
`r=n-1`; these are exact period-two cycles.

### 4. Canonical selection and indexed mismatch

For a valid table `p` with `p_1=1`, its maximal initial slope
`0,1,...,r` comes from `r+1` equal realizing letters.  If the slope stops, the
next realizing letter differs and destroys every positive border, so the next
table value is zero.  This selects `A_r`.

For `p_1=0`, let `k` be the maximal initial zero-run length.  If the run stops,
unit growth `p_i<=p_(i-1)+1` forces `p_k=1`, selecting `B_k`.  A noncanonical
valid table therefore shares at least three coordinates with its unique
template.

Let `L` be the first mismatch.  Prefix dependence shows the next table agrees
with the partner template before `L`.  The repaired proof correctly uses the
**whole shared prefix** to fix the partner parameter:

- from `A_r`, the shared next-table prefix includes the `r+1` initial zeros of
  `B_(r+1)` and its first one;
- from `B_k`, it includes the complete slope of `A_(k-1)` and its first
  following zero.

At an `A`-type mismatch, unit growth forces the actual value one.  The preceding
prefix has border one, and appending one extends it to border two, so
`A1 -> B2`.  At a `B`-type mismatch, the actual value is zero or two.  Zero
creates border one (`B0 -> A1`); two fails to match the initial zero and extends
the agreement prefix.  After an extension, any remaining mismatch is again of
`A1` type.  Therefore the exhaustive local automaton is

```text
A1 -> B2 -> extension,
B0 -> A1 -> B2 -> extension.
```

### 5. Recurrent atlas and upper clock

The first extension costs at most three updates.  Every later extension costs
at most two, and each strictly increases `L`.  Starting with `L>=3`, a valid
table reaches a template in at most

```text
3 + 2(n-L-1) <= 2n-5
```

updates.  Strict increase at the extension events excludes every other cycle.
An arbitrary carrier state enters the valid image after one update, giving
the global upper bound `2n-4` for `n>=4`.

### 6. Sharp witness and all small boundaries

The displayed families have the stated lengths and direct border calculation
gives

```text
e_n -> p_n -> Y_0 -> X_1 -> Y_1 -> ... -> X_(n-3) -> A_1,
Y_j -> X_(j+1),
X_j -> Y_j,          1 <= j <= n-4,
X_(n-3) -> A_1.
```

No preceding state is canonical.  Hence `p_n` has depth `2n-5` and `e_n`
has depth `2n-4`, attaining the upper bounds for every `n>=4`.

The small carriers close separately:

| `n` | carrier states | recurrent states | cycles | maximum depth |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | one fixed point | 0 |
| 2 | 2 | 2 | one exact two-cycle | 0 |
| 3 | 6 | 4 | two exact two-cycles | 1 |

At `n=3`, the two noncanonical states are `(0,0,2)` and `(0,1,1)`, and each
enters a template in one update.

### 7. Every-target factorial extremum

The theorem applies to every target in `E_n`, valid or invalid.  A source has
`e_0=0`, and target coordinate `p_1` uniquely fixes `e_1`.  At position
`i>=2`:

- if `p_i=k>0`, suffix/prefix equality forces `e_i=e_(k-1)`, leaving at most
  one choice;
- if `p_i=0`, then `e_i` cannot equal `e_0=0`, leaving at most the `i` values
  `1,...,i`.

Multiplication gives `|Pi_n^{-1}(p)| <= product_{i=2}^{n-1}i=(n-1)!`.
If any `p_i>0` for `i>=2`, one factor is at most one rather than `i`, so
equality leaves only `0^n` and `A_1=(0,1,0,...,0)`.

For `0^n`, choose `e_1=1` and every later `e_i` freely from `1,...,i`;
position zero is the only zero, so no proper suffix can equal a prefix.  For
`A_1`, choose `e_1=0` and the same later nonzero choices; a suffix starting at
position at least two fails immediately, while one starting at position one
fails at its second letter.  Both families have exactly `(n-1)!` sources.
Review A's boundary repair is correct: at `n=2` the product is empty and the
literal sources `(0,1)` and `(0,0)` give the two size-one maximizing fibres.
At `n=1`, the sole fibre also has size one.

No all-length conclusion here depends on the finite verifier.

## Review-A closure

- **A134-1 closed:** partner parameters are now derived explicitly from the
  complete shared prefix, rather than from coordinate two alone.
- **A134-2 closed:** the `n=2` empty product and its two literal sources are
  separated before the `n>=3` argument invokes `e_2`.

The source diff between round zero and round one contains these two repairs
and the associated pagination shifts; theorem statements, verifier, frozen
stdout, bibliography, and contribution boundary are unchanged.

## Finding B134-1 — stale paragraph pointer after the Review-A insertion

**Severity:** minor, mandatory editorial repair.

Near the end of the mismatch-lemma proof, the current source says:

> The first paragraph of the proof forces its actual value to be one.

After A134-1 inserted a new opening paragraph about full-prefix partner
selection, the statement forcing an `A`-type mismatch value to be one is no
longer in the first paragraph; it is in the subsequent `A_r` case.  The needed
argument is present and correct, so this is not a proof gap.  Replace the
pointer by “the preceding `A_r`-case argument” or an equally exact reference.

## Finding B134-2 — package-index documents still advertise round zero

**Severity:** minor, mandatory handoff/provenance repair.

`README.md` still says Hostile Reviews A/B are not part of the round.
`PAPER_PLAN.md` still labels the package a round-zero manuscript with A/B
deferred, and its checklist leaves both reviews unchecked.  The live package
instead contains a completed Review A, a frozen round-one PDF, and now Review
B.  `BUILD.md` and `IMPROVEMENT_LOG.md` correctly describe round one, so the
artifacts themselves are not ambiguous; the package indexes are stale.

Either mark `PAPER_PLAN.md` explicitly as a frozen round-zero planning
snapshot or update its stage/checklist, and update `README.md` to point to the
round-one/current review state.  Do not rewrite the frozen PDFs or canonical
stdout for this documentation repair.

## Build and artifact audit

Every recorded round-zero and round-one source/PDF hash agrees with the live
files.  The current `main.pdf` is byte-identical to `main_round1.pdf` and
distinct from the preserved round-zero artifact.  It is a five-page A4 file
of 323,084 bytes with blank identifying metadata.  All 24 reported font rows
are embedded, subsetted, and Unicode-capable.  Text extraction succeeds.  The
settled LaTeX/BibTeX logs contain no error, undefined citation/reference,
bad-box warning, or rerun request.

## Owner boundary

The cited primary literature owns the static/one-step territory:

- [Knuth--Morris--Pratt](https://epubs.siam.org/doi/10.1137/0206024) owns
  classical pattern matching and failure-function computation;
- [Franek et al.](https://combinatorialpress.com/jcmcc-articles/volume-042/verifying-a-border-array-in-linear-time/)
  own validation/generation questions for border arrays;
- [Duval--Lecroq--Lefebvre](https://www.numdam.org/item/ITA_2009__43_2_281_0/)
  own validation, construction, generation, and related automaton structure;
  and
- [Gawrychowski--Jeż--Jeż](https://link.springer.com/article/10.1007/s00224-013-9522-8)
  own fast online failure-function validation and realization machinery.

These mechanisms, together with scalar failure-link descent, valid-array
census, the inversion-sequence carrier, and generic factorial language,
properly receive zero contribution credit.  Literal searches for “border
array of a border array,” equivalent whole-table updates, and recomputed
prefix-function dynamics found no direct owner of the repeated map, but that
bounded non-hit cannot establish novelty or priority.  The residual internal
contract is only repeated whole-array feedback and the theorem package audited
above.  `HOLD_EXTERNAL` remains mandatory.

## Final Round-B disposition

**GO** for internal theorem use and the next controlled manuscript round.
Repair B134-1 and B134-2 before declaring the package editorially final.
**HOLD_EXTERNAL** remains in force independently of those minor repairs.

## Closure addendum — 2026-09-01

I independently rechecked both Round-B findings, the fresh exact-control
replay, and the round-two build/provenance chain.  The repairs change no
theorem statement, verifier, canonical stdout, bibliography, or contribution
boundary.

### B134-1 closure evidence

- The current source now reads: “The preceding `$A_r$`-case argument forces
  its actual value to be one.”  It no longer contains the stale “first
  paragraph of the proof” pointer.
- This wording identifies the exact local argument that proves the mismatch
  value, while leaving the proof logic unchanged.
- The current `main.tex` has SHA-256
  `4fac43a74db22838e1595975c73972360cc3aa54e79530feaa3a22e5bc3153b6`.
- Extracted round-two PDF text contains the corrected pointer at the expected
  location.

**B134-1 is CLOSED.**

### B134-2 closure evidence

- `README.md` now declares
  `GO_INTERNAL / ROUND 2 REPAIRED / HOLD_EXTERNAL`, identifies round zero and
  round one separately, and says Hostile Reviews A and B are complete.
- `PAPER_PLAN.md` now labels the stage “Stage-2 Round-B repair complete” and
  its completion checklist marks both independent reviews and their requested
  repairs complete.
- Neither file retains the superseded “round-zero manuscript / reviews A/B
  deferred” package status.

**B134-2 is CLOSED.**

### Fresh control and round-two provenance

- A fresh verifier replay reproduces the frozen raw stdout byte for byte
  (`cmp=0`), retaining 1,694,506 exact assertions and `STATUS=PASS`.
- `main.pdf`, `main_round2.pdf`, and
  `/tmp/p134r2iso.9edN6H/main.pdf` are pairwise byte-identical.  Each has
  SHA-256
  `7d69a1e9338e9421ef31ac3e265a35317e0d11c836f1a652a76a69c36b923962`.
- Both the repository and isolated settled logs have no error, warning,
  undefined citation/reference, bad box, or rerun request.
- The current PDF is a five-page A4 file of 323,103 bytes with blank
  identifying metadata; all 24 font rows are embedded, subsetted, and
  Unicode-capable.
- `main_round1.pdf` remains preserved at
  `d1c1ed8fe7667bb192c6c00e59259e1a80403c5a18e52735be99e907c7662525`.
  `main_round0_original.pdf` remains preserved at
  `958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829`.
  Both differ bytewise from round two, as expected, and their recorded hashes
  are unchanged.

### Final post-closure ledger and verdict

- **Critical:** 0
- **Major:** 0
- **Unresolved minor:** 0
- **Internal verdict:** **`GO_INTERNAL`**
- **External verdict:** **`HOLD_EXTERNAL`**

This addendum supersedes only the earlier instructions to repair B134-1 and
B134-2; all mathematical and owner-boundary conclusions of the main Round-B
review remain unchanged.
