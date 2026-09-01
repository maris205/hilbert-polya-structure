# Hostile review A — round 1

**Verdict: REVISE.**  The mathematical core survived adversarial checking, but
the bibliography contains one objectively wrong DOI and the ownership and
reproducibility gates are not yet strong enough for an accepted package.

## Audit performed

I read every paper-local source artifact, including the manuscript, verifier,
bibliography, planning/evidence/source/build records, and generated BibTeX and
LaTeX records.  I inspected all three rendered PDF pages.  The local verifier
replayed exactly with **265,050 assertions** and the printed census
`(1,4,29,355)` of preorders.  A fresh isolated four-stage build from only
`main.tex` and `references.bib` exited zero and reproduced the current
`main.pdf` byte for byte; its settled logs are clean and all 25 fonts are
embedded.

I also implemented an independent fibre census in `/tmp`, not using
`verify_p143.py`: for all 219 labelled posets `Q` of order four, I classified
all `32^4 = 1,048,576` ordered maps `Q -> B_5` by their reflected inclusion
relation and compared the direct induced-embedding count with the stated
inclusion--exclusion sum.  Every comparison passed.  This exercises a
five-column host beyond the paper's exhaustive `n<=4` box.

## Severity-ranked findings

### Major — `KatonaNagy2015` has the DOI of a different paper

`references.bib` assigns `10.1007/s11083-014-9343-7` to Katona and Nagy's
*Incomparable Copies of a Poset in the Boolean Lattice*.  That DOI resolves to
Andrew P. Dove and Jerrold R. Griggs, *Packing Posets in the Boolean Lattice*,
*Order* 32 (2015), 429--438.  The correct Katona--Nagy DOI is
`10.1007/s11083-014-9342-8`, for *Order* 32 (2015), 419--427.  See the official
[wrong-target record](https://link.springer.com/article/10.1007/s11083-014-9343-7)
and [correct record](https://link.springer.com/article/10.1007/s11083-014-9342-8).
The bad DOI is printed in the current PDF, so this is not inert metadata.

**Required fix:** replace the DOI by `10.1007/s11083-014-9342-8`, add the
official Springer record to `SOURCE_VERIFICATION.md`, regenerate the
bibliography/PDF, and re-audit every printed identifier.  “BibTeX resolved
4/4” is not a metadata-validity test.

### Moderate — the owner subtraction lacks exact locators and a closest-owner gate

The paper correctly gives zero credit to self-residuation, containment
preorders, strong Boolean-lattice embeddings, and inclusion--exclusion.
However, the ownership evidence is too coarse for those subtractions.
`Schmidt2011` is cited as a whole monograph without a page, definition, or
equation identifying the exact row-oriented residual convention.  The
Katona--Nagy article supports weak/strong embedding terminology, but its topic
is extremal packing of incomparable copies, not the number of labelled strong
embeddings or the separating-upset inclusion--exclusion formula used here.
Thus it is not a close owner for the residual inverse count.

**Required fix:** cite the exact Schmidt location and orientation convention;
add and verify a closest source for order embeddings into powersets (including
the classical separating-family/Boolean-lattice representation viewpoint),
then state precisely what remains after that source is subtracted.  Keep
`HOLD_EXTERNAL`; a bounded non-hit still cannot support a novelty statement.

### Moderate — the verifier does not independently exercise the induced-embedding bijection

The local program compares direct fibres of `step` with `fibre_formula`, but it
never enumerates induced embeddings and never checks the map
`A -> (q -> row_support(q))` or its inverse.  The proposition's proof is
correct, and my independent `B_5` census found no counterexample, but the
claims ledger currently gives the embedding interface more executable support
than the checked code actually supplies.

**Required fix:** add a genuinely separate lane that enumerates labelled maps
`f:Q -> B_n`, tests preservation and reflection directly, reconstructs the
source matrix class by class, and compares this set bijectively with the direct
fibre.  Do not reuse `fibre_formula` in that lane.  At minimum retain the
order-four/`B_5` control above or an equivalent deterministic test.

### Moderate — “frozen stdout” and current-build provenance are not machine-checkable

`CONTROL_RESULTS.md` calls its embedded code block “Frozen stdout”, but there
is no canonical transcript file and the README supplies no byte-comparison
command.  The replay happens to match the block, but that is a manual check.
Also, `BUILD.md` records only the round-0 PDF (`331,522` bytes, SHA-256
`2cc73c...`), while the current reproducible PDF is `331,520` bytes with
SHA-256 `c0de4e...`; the two-file distinction is legitimate, but no settled
current-build record explains it.

**Required fix:** freeze verifier stdout as a standalone file and document a
`cmp -s` replay; after the citation/evidence repairs, record the current
four-stage and isolated builds, warning scan, current hashes, and the preserved
round-0 hash separately.

### Minor — distinguish labelled embedding maps from unlabelled copies

The proposition correctly writes a set of functions, but the abstract and
main theorem say that preimages “are” induced embeddings.  Here quotient
classes remain distinguished by the fixed target preorder, so two embeddings
with the same image but differing by an automorphism of `Q` correspond to
different source matrices.  No automorphism quotient is taken, whereas
“copies” in the cited extremal literature can mean images.

**Required fix:** say “canonically bijective to the set of labelled induced
order-embedding maps `Q -> B_n`” at the first two occurrences and explicitly
state that automorphisms are not divided out.

## Mathematical interface disposition

- **Image = preorders:** pass.  Row inclusion is reflexive/transitive, and
  `T(P^T)=P` proves surjectivity with the stated row convention.
- **`T(P)=P^T`:** pass.  The principal-upper-set argument has both directions
  and remains valid for non-antisymmetric preorders.
- **Tails, cycles, fixed iterates, zeta:** pass.  Once in the image, transpose
  is an involution; symmetric preorders are exactly equivalence relations.
- **Fibre/quotient interpretation:** pass mathematically.  Mutual
  comparability forces exactly equal rows, and the antisymmetric quotient
  makes order reflection equivalent to an induced embedding.
- **Inclusion--exclusion:** pass.  Intersections of bad events are precisely
  isotone maps for the reflexive--transitive closure `Q_S`; this remains true
  when the closure identifies elements, and coordinate upper sets give
  `J(Q_S)^n`.

No theorem-level counterexample was found.  The verdict remains **REVISE**
because the printed wrong DOI is a major source-integrity failure and the
ownership/evidence repairs above are required before acceptance.
