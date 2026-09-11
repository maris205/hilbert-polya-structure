# Primary-source and internal-collision audit

Checked 2026-09-08 UTC by the author scout. This is a bounded source audit,
not a systematic review, novelty certificate, independent gate, or claim of
human reading. AI-assisted retrieval and algebraic author deductions were
used. All sources are public; no private manuscript or research package
was uploaded to an external model or submission service.

## Sources, actual access, and claim ceilings

| Source | Existence and actual read scope | Subtraction or relevance |
|---|---|---|
| Eric Bedford and Paul Frigge (2018), *The Secant Method for Root Finding, Viewed as a Dynamical System*, Dolomites Research Notes on Approximation 11(4), 122–129, [publisher record](https://drna.padovauniversitypress.it/2018/4/11), DOI 10.14658/PUPJ-DRNA-2018-4-11 | Publisher metadata read. Actual publisher PDF downloaded with HTTP 200, 249,251 bytes; native text extraction succeeded. Introduction and Section 4 including Example 4.2 read from those bytes. Published original mathematical article; no bibliometric or personal-COI clearance is implied. | The quadratic secant formula and its linear/Fibonacci monomial reductions are explicit prior art. The source uses rational/projective dynamics, not the present all-affine zero-reset convention. No finite-field reset theorem is attributed to it. |
| Jason Fulman and Robert Guralnick (2021 preprint), *Cohen Lenstra Partitions and Mutually Annihilating Matrices over a Finite Field*, [NSF-hosted original](https://par.nsf.gov/servlets/purl/10415826), [author arXiv record](https://arxiv.org/abs/2111.09433) | Actual NSF PDF downloaded with HTTP 200, 92,099 bytes; native extraction succeeded. Introduction, Section 2 context and Section 3.1 including Lemma 3.2 and its proof read. Captured title page says November 14, 2021; the arXiv submission record is November 17, 2021. These are different dates, not an inconsistency. | Lemma 3.2 gives exactly the fixed-$A$ mutually-annihilating count used in CAC; the Section 3.1 proof derives the all-size generating function. The size-two zero count is thus wholly consumed. This source does not assert the CAC dynamical update or its fourth iterate. |
| Yifeng Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, [arXiv version record](https://arxiv.org/abs/2110.15566), [publisher record](https://www.sciencedirect.com/science/article/pii/S0021869322005622) | Author record identifies v1 October 29, 2021 and v3 December 13, 2022. Publisher metadata identifies Journal of Algebra 619 (2023), 26–50, DOI 10.1016/j.jalgebra.2022.11.021. Abstract and exposed introduction/metadata only; no full original proof is claimed read. | Establishes the direct all-size mutually-annihilating counting programme and its relation to the independently fetched Fulman–Guralnick proof. CAC subtraction does not depend on pretending this unread full body was inspected. |
| Nicholas Freeman (2025), *Böttcher-type potential for the secant map*, [author arXiv record](https://arxiv.org/abs/2508.05847) | Actual current author abstract/version page read; v1 August 7, 2025. Full 32-page manuscript not downloaded or read. Preprint, not represented here as peer-reviewed. | Recent secant research concerns holomorphic potentials and attraction basins. This is current context, not a literal finite-field zero-reset owner or a candidate theorem. |

For the two PDF-backed mathematical subtractions, the retained originals
are `sources/bedford_frigge.pdf` and `sources/fulman_guralnick.pdf`.
Their exact HTTP observations, extraction command lines and complete raw
text are recorded under `native02/`. The receipt pins both original PDF
byte strings. Section labels identify the read scope; this audit makes no
validated local-PDF page-anchor claim and no visual-QA claim.

Mathematical-source quality is judged relative to this theorem task:
an actual matching statement and proof in a primary original carry the
subtraction, whereas an abstract supplies topic scope only. The clinical
I–VII hierarchy is inapplicable to deductive algebra. No comprehensive
venue-index, retraction-database, author-affiliation, or conflict-of-interest
investigation was performed; none is labelled clear or certified.

## Search scope, positive collisions, and non-hit ceiling

Initial read-only local searches covered the paper source files and nearby
old/new scouting prose using literal terms:

- `arithmetic.harmonic`, `harmonic.mean`, `Markov.*(map|recurr)`,
  `Euler.top`, `Kahan`, `Cremona`, `Hirota`, `qd.algorithm`,
  `quotient.difference`;
- `secant`, `割线`, `割線`, `anticommutator`, `PXE`,
  `commutator-sum`, `AB.?BA`.

The broad discovery calls were read-only tool searches, not a pinned
whole-corpus audit. Their non-hits are not used to prove absence. The final
native `narrow_history` command records the precise twelve-file set and
pattern after relevant originals were selected. Every such file is pinned
in `INPUT_PINS.sha256`; the before and after lists were actually compared
by native `cmp`. The two current controls have physical historical copies
and actual successful raw comparisons in the capture evidence.

Positive internal hits were the old CS original's characteristic-two
commutator–sum theorem, the MAR literal register entry, and the old PXE
pair-product entry, alongside the six explicit P150/P157/P168/P174/P175/P180
source bodies. The precise literal and mechanism boundaries are in
PROOF_AND_SUBTRACTION.md. No source-only idea is counted as a third attempt.

Public web searches included:

- `finite field arithmetic harmonic mean dynamical system recurrence rational map`;
- `finite fields rational map x y quotient-difference`;
- `finite fields Markov recurrence rational map dynamics three variables`;
- `secant method quadratic polynomial finite field dynamics secant map xy alpha x+y`;
- `secant map finite fields` and `secant method monomial quadratic dynamics`;
- `commutator anticommutator dynamical matrices map`;
- `mutually annihilating matrices finite field pairs`;
- `Bedford Frigge Secant Method`;
- `mutually annihilating matrices 2024 2025 2026`;
- `secant map finite 2024 2025 2026 quadratic`.

The recent-window search returned directly relevant older foundational
owners and the 2025 secant preprint. A result's recent crawl timestamp was
not confused with its publication date. Secondary aggregators, search
snippets about unrelated geometry, and generic numerical-method pages
were discovery leads only, not support for the mathematical claims.
The named primary sources were inspected through their actual records or
captured bodies as specified above.

## Preserved failures and non-certification boundary

1. The first artifact collector assumed `/usr/bin/rg`, which does not
   exist. It terminated before fetching any source or writing its final
   receipt. Its source, successful partial native outputs and snapshots
   remain unchanged; FAILURE_01.md identifies the missing receipt and the
   exact observed exception. The separate `capture_native02.py` resolves
   the actual tool paths and completed ten native commands successfully.
2. Browser opening of the NSF original failed with a `(400) Timeout fetching`
   observation. Later native curl retrieval succeeded with HTTP 200; the
   success does not retroactively turn the failed browser call into a read.
3. A browser text-find on the EMIS PDF returned no match for `Example 4.2`.
   Direct native publisher extraction contains the complete actual example.
   This is a search/extraction-path limit, not missing mathematics.
4. The initial failure traceback was returned by the shell tool but was not
   separately captured as a native stderr file. The failure note is a
   transparent transcription, not fabricated native evidence. The later
   collector's commands do have complete stdout/stderr payloads and exits.

No scientific producer, full loader/runtime capsule, independent review,
manuscript, admission, or new experiment exists here. Input hashes certify
the captured byte relationships only; the proof content remains author
work awaiting root reception. All results remain on external hold.
