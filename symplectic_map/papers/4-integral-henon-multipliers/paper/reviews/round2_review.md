# Independent Manuscript Review — Round 2

**Manuscript:** *Rational Periodic Multiplier Moduli under Good Reduction: A
Hénon Certificate and Exact Audit*  
**Review date:** 2026-08-14  
**Review role:** independent verification of the Round-1 repairs, mathematical
consistency, evidence integrity, build reproducibility, and visual output  
**Revised source reviewed:** `paper/manuscript.tex`, SHA-256
`8b1e92941956872d9d504a390a9091b2e530fede93b88d2629f6daad0d1ce1d9`  
**Revised PDF reviewed:** `paper/paper_round1_revised.pdf`, SHA-256
`f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156`

## Verdict

`PASS`

**Overall assessment:** **8.8/10** as a narrowly scoped arithmetic-dynamics
certificate note.  All three Round-1 minor comments are independently closed.
I found no critical, major, or remaining required minor issue, and no
mathematical, bibliographic, numerical, figure, build, or scope regression.
The manuscript may proceed to finalization and the final integrity pass.

The contribution remains intentionally modest: it packages standard
good-reduction, integrality, and unit arguments around exact rational
multiplier moduli and supplies a source-locked nonlinear certificate plus
sharp controls.  The revised manuscript continues to state this positioning
accurately and does not promote the finite period audit into an all-period
proof.

## Round-1 repair closure

### M1 — Standalone algebraic implications: CLOSED

The revised proof of Lemma 3.4 now explicitly supplies the previously
compressed ring-theoretic chain:

1. the monodromy characteristic polynomial is monic over the integral closure
   `Rbar`;
2. each root is integral over `Rbar`;
3. `Rbar` is integral over `R`, so transitivity makes each root integral over
   `R`; and
4. determinant one makes the second eigenvalue `lambda^{-1}`, putting both
   `lambda` and its inverse in `Rbar` and proving the unit assertion.

The revised proof of Lemma 3.5 also makes the place restriction explicit.  A
place `W` outside the saturated set `T` lies above a rational prime outside
`S_Q`, hence restricts outside `S`; applying the preceding integrality result
to both `lambda` and `lambda^{-1}` forces
`v_W(lambda)=0`.  The subsequent Galois-stable conjugation step is unchanged
and correct:

\[
q^2=\lambda\bar\lambda.
\]

The proof still carefully avoids the false identification
`bar(lambda)=lambda^{-1}`.  Reciprocity is used to obtain the inverse unit;
complex conjugation is used only after passing to the saturated Galois
extension.

### M2 — Bibliographic metadata: CLOSED

The three relevant records now agree:

- `references.bib` gives Silverman, *Mathematische Zeitschrift* **215(2)**,
  237--250 (1994);
- `notes/CITATION_VERIFICATION.md` gives the same issue and page range; and
- `notes/NOVELTY_AUDIT.md` gives Kawaguchi (2013), 1225--1252.

The revised bibliography renders Silverman as 215(2), 237--250.  Citation-key
closure is exact: **12 used keys, 12 bibliography keys, zero missing, zero
unused**.  I found no citation change that alters a mathematical claim.

### M3 — Stray control byte: CLOSED

The historical integrity text now contains literal Markdown math
`$\bar\lambda$`.  An independent UTF-8/C0 scan over the paper's Markdown,
TeX, BibTeX, JSON, Python, shell, and SVG text artifacts found **zero**
disallowed control characters.  The repaired integrity artifact and all
dependent active hashes agree with `INTEGRITY_ROUND1_REVISION.md`.

## Mathematical regression audit

The all-period argument remains correct and has not been weakened or inflated:

- separate-degree homogenization and the absence of projective points at
  infinity give algebraicity of every finite complex periodic orbit;
- the cyclic non-Archimedean maximum gives integrality outside the declared
  places;
- determinant-one integral monodromy makes both return eigenvalues algebraic
  units;
- saturation above the rational bad-prime set makes the unit support stable
  under complex conjugation; and
- exact rational `q=|lambda|` can therefore have valuation only at the
  declared rational bad primes.

For the frozen monic integral map, the support is empty, so exact rational
modulus is one at every period and exact rational-prime modulus is absent.
This statement does not require the multiplier itself to be rational.  The
denominator-2 fixed-point control still realizes exact moduli `2` and `1/2`,
while the nonunit-determinant and cat-map controls continue to delimit the
theorem rather than contradict it.

The revised page flow moves some floats and paragraph breaks but introduces no
logical reordering: the finite table remains explicitly a period-1--3
implementation audit, whereas Theorem 3.1 and Corollary 4.1 remain deductive
all-period statements.

## Numerical, manifest, and figure verification

The manuscript's finite claims remain aligned with the frozen exact records:

- exact point counts: `2, 2, 6` for periods `1, 2, 3`;
- exact cycle counts: `2, 1, 2`, hence ten points on five cycles;
- one selected-embedding cycle has rational unit modulus and four have
  irrational algebraic-unit moduli;
- the finite exact rational-modulus set is `{1}`;
- all 15 registered audit runs pass; and
- the route decision remains geometry pass, A0 failure by theorem, later
  Route-A gates stopped, Route B unopened.

I independently recomputed every path recorded by
`results/final_result_manifest.json`: **41/41** byte sizes and SHA-256 hashes
match.  The manifest itself retains SHA-256
`e47c93ccc49cf37ffa5bab63bed758be9c1288500f459d539de806d7e4229863`,
and the prospective source lock retains
`3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269`.

The figure package also revalidated completely: all frozen inputs, source
adapter, shared style, three generators, and nine PDF/SVG/PNG outputs match
their declared hashes (**23/23 checked records**).  The scientific values and
captions in Figures 1--3 agree with the result JSON and manuscript narrative.
There is no changed figure input or hand-transcribed result regression.

## Independent build and test verification

To avoid modifying the reviewed project, I copied the paper directory to a
temporary location and executed its deterministic build there.  The rebuilt
PDF had SHA-256

`f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156`,

which is byte-identical to `paper_round1_revised.pdf`.  The final log contained
no LaTeX/package warnings, undefined citations or references, multiply defined
labels, or overfull/underfull boxes.  The output is an unencrypted, letter-size
PDF with 11 pages; every listed font is embedded and subset.

The safe test suite was run with project cache writing disabled:

- `pytest -q -p no:cacheprovider code/tests`: **39 passed**, zero failures.

The revised source, working `manuscript.pdf`, revised snapshot, bibliography,
Round-1 review/response, claim manifest, experiment passport, figure package,
and author revision-integrity hashes all independently agree with the active
hash table.

## Visual inspection

All 11 rendered pages were inspected.  Equations (including the repaired unit
and valuation proof), theorem/corollary statements, tables, references, three
figures, captions, colors, arrows, page boundaries, and hyperlinks are legible.
No text or figure is clipped, no caption is detached from its object, and no
new visual ambiguity was introduced by the repaired proof's additional lines.

## Remaining issues

- Critical: none.
- Major: none.
- Required minor: none.
- Optional editorial suggestions: none needed for finalization.

## Scope and data discipline

This review used the frozen local manuscript and its declared exact artifacts.
It did not modify any implementation, manuscript, result, figure, source lock,
or PDF.  The only project file created is this Round-2 report.  No external
prime table, Riemann-zero data, target matching, or forbidden arithmetic data
was accessed.

## Final recommendation

`PASS — MAY FINALIZE.`

The author should now freeze the revised PDF as the final PDF, add the final
integrity record and pipeline-state transition, and preserve the Round-1 and
Round-2 snapshots.  No further scientific revision, experiment, higher-period
search, theorem weakening, or route reopening is required.
