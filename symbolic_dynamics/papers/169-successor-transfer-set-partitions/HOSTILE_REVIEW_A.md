# Hostile Review A — Successor Transfer on Set Partitions

**Role:** independent theorem, source, boundary, executable, and PDF attack on
the immutable author Round-0 package.  
**Decision:** `MINOR_SOURCE_REPAIR`.  
**Findings:** `0 Critical / 0 Major / 1 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Pinned Round-0 input

```text
676675f260f1ad756b8a658ea07ab6390698a8be05d10e63fc9150f1cfb2c512  main.tex
0a20bea8b28b93815c08b689b8fe2ab13957bc316bbd5ba7588c61ea951cf195  references.bib
df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2  main.pdf
df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2  main_round0_original.pdf
e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b  verify_p169.py
e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f  verification_output.txt
```

The review treats the pre-paper candidate gate as scouting evidence, not as
a manuscript review.  Every proof axis below was reread from the literal
block map before consulting the author transcript.

## Independent mathematical attack

### Carrier and restricted-growth rule

Every source block retains its minimum: a nonsingleton removes only its
maximum, and a singleton does not donate.  Every element newly entering
block `i+1` is either already in that block or is the maximum of block `i`,
and in both cases it is strictly larger than the retained minimum of block
`i`.  Hence the canonical minimum order is preserved.  The wrap donation
enters block zero and creates no false last-to-first ordering condition.

In a restricted-growth word, exactly the last occurrence of a repeated
letter is its block maximum; it changes to the cyclic successor.  A donor's
first occurrence remains.  Any newly earlier occurrence of `i+1` still lies
after the first `i`, while the wrap to zero is harmless.  Thus the displayed
simultaneous word rule is equivalent to the block rule and preserves the
same number of blocks.

### Load smoothing and the labelled clock

With `z_i=|B_i|-1`, direct accounting gives

```text
z_i' = z_i - 1[z_i>0] + 1[z_(i-1)>0].
```

For the periodic height lift, one step is
`H_i'=max(H_i-1,H_(i-1))`.  Expanding this recurrence gives the printed
finite maximum.  The two adjacent maxima share all interior candidates, so
if their difference produces `z_i(t)=0`, only the new right endpoint can
win; if it produces `z_i(t)>=2`, only the old left endpoint can win.  The
two cone inequalities and the `m-1`/`k-1` smoothing bounds follow with the
stated inequality directions.

The reverse final-`k` window in the dense regime obeys the same mass-`k`
queue because precisely the last occurrence of every colour present in the
window moves.  In the sparse regime a prefix occupancy two moves its excess
one step through prefix occupancies one until it fills a zero.  Equal numbers
of excesses and holes and cyclic-order pairing give the claimed `k-1`
bound.  The resulting dense suffix and sparse prefix are invariant, not just
eventually visited.

Periodic points must already be in both forward-invariant terminal regimes.
Deleting the dense final permutation leaves a surjective restricted-growth
prefix; the sparse final word is an injection after the canonical prefix.
Conversely, those forms are preserved and their nonempty moving word is
incremented modulo `k`, giving exact period `k`.  The Stirling and falling-
factorial counts therefore have both necessity and converse proofs.

The upper clock is the sum of the two exact phase ceilings.  For the word
`0^(m+1)12...(k-1)`, the printed load trajectory prevents the first phase
from ending early.  Its prefix particle/hole trajectory in the sparse case,
and its explicit terminal suffix in the dense case, prevent the second phase
from ending early.  This yields `min(n-2,2k-2)` on each nontrivial stratum
and `n-2` globally.  The boundaries `n=1`, `n=2`, `k=1`, `k=n`, and
`n=2k` agree with the formulas.

### Every-target fibre trace

For fixed target blocks `C_i`, a predecessor determines a cyclic token
`x_i`: either the donated maximum in `C_(i+1)` or absence for an inactive
singleton.  Reconstruction is forced by

```text
B_i = (C_i minus x_(i-1)) union x_i.
```

The five token types are sufficient because deletion size and extrema are
constant within each type.  A present `x_i` must exceed the retained maximum;
an absent `x_i` requires retained size one.  These are exactly the two matrix
entry cases.  The retained minima impose linear canonical order only at
indices below `k-1`; the product joins adjacent token types and the trace
closes the donation wrap without inventing a cyclic minimum comparison.

Every contributing cyclic state-and-label choice therefore constructs one
valid predecessor, and a predecessor recovers that choice uniquely.  The
trace is consequently an exact fibre, including zero fibres.  Singleton
deletion leaves an inadmissible empty remainder, the all-singleton target has
the sole all-absent path, and the printed interlacing matrices and literal
predecessor lists give fibres two and one.  No missing converse or local
multiplicity factor was found.

## Exact-control replay

A fresh standard-library process reran the unchanged author verifier.  Its
1,785-byte output matched the frozen transcript byte for byte:

```text
assertions: 1,217,025
verifier SHA-256:  e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b
transcript SHA-256: e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f
decision: AUTHOR_ROUND0_PASS
```

It exhausts every partition through `n=10`, every target fibre through
`n=9`, 532,467 queue-cone cases, and all sharp-witness strata through
`n=50`.  Enumeration is used only as falsification evidence; the uniform
verdict above follows from the printed proofs.  Review B is required to use
a separately implemented carrier and verifier.

## Source, ownership, build, and PDF audit

The Wachs, Joseph--Propp--Roby, Brandt, Schützenberger,
Striker--Williams, Takahashi--Satsuma, and Choi--Gan--Li--Zhu records match
their DOI/publisher or arXiv surfaces.  All eight entries are cited.  The
manuscript explicitly assigns the RGF carrier, sequential whirling, the
entire directed-cycle chip-firing factor, solitaire, promotion/rowmotion,
box--ball dynamics, stack sorting, Stirling counts, and generic matrix
algebra zero contribution credit.  The bounded literal-owner non-hit is not
used as novelty, priority, or release permission.

The two retained source-only Round-0 builds match the canonical PDF under
SHA-256.  Settled logs contain no warning, bad box, unresolved citation or
reference, rerun request, or fatal error.  The PDF has five A4 pages, all 28
font rows are embedded/subsetted/Unicode mapped, identifying metadata fields
are blank, and there is no encryption, form, or JavaScript.  The five-page
render is legible and anonymous, with no clipping, collision, overflow, or
malformed glyph.

## Findings

### Critical

None.

### Major

None.

### Minor

**M1 — The chip-firing owner record stops at the arXiv version although a
formal publication is available.**  The cited title and authors are
correct, and arXiv `2407.15889` is a valid primary record.  However,
Ji--Li--Wang is now published as “Periods and Atomic Firing Sequences of
Parallel Chip-Firing Games on Directed Graphs,” *Annals of Combinatorics*
29(4), 1155--1175 (2025), DOI `10.1007/s00026-025-00760-3`.  Since this
paper treats that work as a strong mechanism owner, the final bibliography
and source ledger should point to the formal record and may retain the arXiv
identifier as an auxiliary link.  The stable citation key may be renamed or
explained.  This is source currency only and changes no mathematical or
ownership conclusion.

## Recommendation

Accept every theorem without weakening.  Apply M1, make the live lifecycle
label round-independent, rebuild twice from source-only directories, and
then send the repaired source to independent Review B.  Preserve the exact
Round-0 PDF.  External status remains `HOLD_EXTERNAL`; this review grants no
posting or submission permission.
