# Round-A hostile review: whole-array recomputation of border arrays

**Review date:** 2026-08-31  
**Reviewer posture:** independent internal reviewer; not an author of this manuscript  
**External status:** `HOLD_EXTERNAL`

## Verdict

**`GO_INTERNAL_AFTER_MINOR_REPAIR`**

The theorem package withstands adversarial reconstruction.  Whole-table
recomputation is defined distinctly from scalar failure-link descent; the
exact image argument is valid; the indexed mismatch mechanism proves both the
complete recurrent atlas and the upper clock; the displayed trajectory makes
the clock sharp; and the factorial fibre theorem applies to every target,
including invalid ones.  I found no mathematical counterexample and no
dependence of an all-length claim on finite enumeration.

Two local exposition repairs are required: the mismatch proof attributes
canonical-partner selection to the second coordinate when the full shared
prefix is doing the work, and the maximizing-fibre construction should state
the `n=2` empty-product boundary before referring to `e_2`.  Neither changes a
claim or formula.

**Severity count:** critical 0; major mathematical 0; major scope 0; mandatory
minor 2.

## Frozen evidence and reproducibility check

I audited the manuscript, bibliography, support documents, verifier, frozen
stdout, current PDF, and frozen round-0 PDF.

- `main.tex`: `e5d9c0196aa0627c3b8159332408244f58a4542a82246a6e4d5ca8e1ace35bd8`
- `references.bib`: `1efd506b8a7be8c8ff7591b7fd6af924f700cf05b7354bda1fa3e6d0e1a133fb`
- `code/verify.py`: `3aec6dd12c1e9472e1734061ba4c006d94e2e94a6d255f7dede25464cb7d162d`
- frozen stdout: `cce8c343276f5a299cb2c723e8b1957020749f74ff36a9aeb8462253c4b34d3e`
- current `main.pdf`: `958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829`
- `main_round0_original.pdf`: `958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829`

The current PDF and frozen round-0 PDF are byte-identical (`cmp=0`).  A fresh
verifier replay also reproduced the frozen stdout byte for byte (`cmp=0`).
The run exhausts 409,113 states and the same number of target cells through
length nine, checks 3,279 standardizations and 29 larger witness sizes, makes
1,694,506 exact assertions, and ends in `STATUS=PASS`.

## Mathematical attack

### 1. The literal map and its owner boundary

The carrier
`E_n={(e_0,...,e_{n-1}):0<=e_i<=i}` is closed because a proper border of a
prefix of length `i+1` has length at most `i`.  The paper consistently applies
the border operator to the entire current integer word and makes the resulting
array the next word.  This is not the conventional iteration
`k -> beta_{k-1}(w)` inside one fixed failure table.

The semantic firewall is unusually important here and is presently adequate:
the definition, displayed orbit, and limitations paragraph all repeat the
whole-table/failure-link distinction.  Standard border computation,
validation, realization, generation, and enumeration receive zero credit.
The bounded owner search has not cleared external novelty, so the residual
claim remains internal and `HOLD_EXTERNAL` remains necessary.

### 2. Exact image and canonical recurrent pairs

The exact-image proof is sound.  Standardizing a realizing word by order of
first occurrence preserves every equality and inequality between positions;
border predicates therefore remain unchanged.  The label introduced at
position `i` is at most `i`, so the standardized word lies in the carrier.
This proves both inclusions, not merely image containment.

For every `1<=r<n`, direct border inspection gives
`Pi_n(A_r)=B_{r+1}` and `Pi_n(B_{r+1})=A_r`.  The templates are distinct, so
these are exact two-cycles.  The endpoint `r=n-1` correctly pairs the complete
slope with the all-zero table.

### 3. Indexed mismatch amplifier

For a noncanonical valid table, the first mismatch index is at least three.
The unit-growth inequality and the equality pattern of the shared prefix force
the three local states exactly as claimed:

```text
A1 -> B2 -> extension,
B0 -> A1 -> B2 -> extension.
```

After the first extension, any later mismatch is of `A1` type, so every
further increase of the agreement index costs at most two updates.  Starting
from `L>=3` gives

```text
3 + 2(n-L-1) <= 2n-5
```

updates for a valid table; an arbitrary carrier state needs at most one extra
update to enter the exact image.  Strict increase of `L` at every extension
rules out all noncanonical recurrence.  Thus the proof, rather than the
enumeration, yields the complete recurrent set and the upper clock.

The explicit arrays `e_n,p_n,X_j,Y_j` have consistent lengths and endpoints.
Their equality-block calculations give a trajectory of `2n-4` transient
steps from `e_n`, matching the upper bound for `n>=4`.  The separately listed
boundaries are also correct:

- `n=1`: the sole state is fixed, maximum depth zero;
- `n=2`: the two carrier states are the single canonical two-cycle, maximum
  depth zero;
- `n=3`: four states are canonical and the other two enter them in one step.

### 4. Every-target factorial fibre

The fibre theorem does not assume that the target is valid.  Exposing a source
from left to right, `p_1` uniquely determines `e_1`.  At every later position,
a prescribed positive border `p_i=k` forces `e_i=e_{k-1}`, hence at most one
choice.  A prescribed zero border forces `e_i` to be nonzero, hence at most
`i` choices.  Multiplication gives `(n-1)!`; an invalid target simply realizes
zero choices.

Equality in the product forces all entries from index two onward to be zero,
leaving only `0^n` and `A_1`.  Both constructions really have `(n-1)!`
sources.  For `0^n`, every proper suffix begins with a nonzero letter whereas
the prefix begins with zero.  For `A_1`, a suffix beginning at position at
least two fails immediately, and the suffix beginning at position one fails
at its second letter for every prefix of length at least three.  This avoids
the invalid shortcut that a nonzero final letter by itself forbids all longer
borders.

## Mandatory repairs

### A134-1 — canonical partner is fixed by the shared prefix, not coordinate two alone (`MINOR`, mandatory)

In the proof of the indexed mismatch lemma, the sentence

> its second coordinate selects that partner as `Q(q)`

is too compressed and is not literally sufficient: coordinate one selects
only the `A`-type versus `B`-type family.  The template parameter is fixed by
the entire agreement prefix.  Replace the sentence with an explicit argument:

- in the `A_r` case the mismatch occurs after the first template-tail zero,
  so `q` shares enough of `B_{r+1}` to include its initial zero run and first
  following one;
- in the `B_k` case it occurs after the first one following the zero run, so
  `q` shares enough of `A_{k-1}` to include the full initial slope and first
  following zero.

Those facts force `Q(q)=B_{r+1}` and `Q(q)=A_{k-1}`, respectively.  The rest
of the local-value proof is already correct.

### A134-2 — state the `n=2` empty-product boundary in the maximizer proof (`MINOR`, mandatory)

The theorem correctly includes `n=2`, and both targets then have fibre size
`(n-1)!=1`.  The construction for `A_1` later refers to `e_2` when excluding
longer borders; this is logically under the condition that such a longer
prefix exists, but the boundary should not be left implicit.  State first that
for `n=2` the product is empty and the two sources are immediate.  Then begin
the `e_2` suffix argument with `n>=3`.  No formula or verifier change is
needed.

## Mechanical and claim-control findings

The source/PDF pair has no malformed control sequence analogous to a literal
`qquad`, the stored build is mechanically clean, all cited keys close, and the
current PDF is the frozen round-0 artifact.  The abstract accurately states
the literal carrier, whole-array convention, recurrent classification,
piecewise sharp clock, and factorial maximum.  Unlike an unqualified claim of
"complete dynamics," it specifies the delivered contracts.

The owner subtraction must not be upgraded from "bounded non-hit" to a
novelty or priority assertion.  Standard prefix-function/failure-link theory
owns the one-step table and scalar descent mechanisms; this manuscript's only
residual object is repeated whole-table feedback and the theorem package
proved for that literal map.

## Round-A exit condition

Round A passes once A134-1 and A134-2 are implemented, a fresh four-stage
build is visually checked at those paragraphs, the verifier again reproduces
the frozen stdout, and the reviewed-round hashes are recorded without
overwriting `main_round0_original.pdf`.  No additional enumeration is needed.
