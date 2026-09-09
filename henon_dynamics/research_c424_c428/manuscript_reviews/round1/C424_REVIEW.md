# C424 manuscript review — round 1

2026-09-09 UTC. Current-team nonauthor review of the frozen initial manuscript
`papers/C424_integer_valued_quadratic/`. The reviewer is neither the AM1 proof
author nor the C424 manuscript author. This is an actual manuscript and
evidence-migration review, not a restatement of the author's report, the
previous proof review, or an external/human peer-review decision.

## Verdict

**PASS for this first manuscript-review round. No blocking mathematical,
certificate-migration, citation-scope, or observed layout defect was found.
There are no required author corrections from this round.**

Theorem 1.1 genuinely states and proves a classification of the entire
degree-exactly-two integer-valued coefficient class on all of `Q^2`, including
negative leading coefficients. It does not silently restrict original points
to an integral lattice. The missing half-integral normal form is exhausted by
the analytic reduction and the declared exact finite dependency. Its four
parametric families, eleven exceptional cycles, native period set, sharp
17-point bound, and equality condition have survived migration into the actual
TeX and PDF without an identified loss or strengthening.

This verdict retains the paper's two explicit dependencies: the imported
monic-integral theorem C412, and the computer-assisted exhaustion of the proved
finite residual range. It is not a formal proof-assistant certification,
worldwide-priority determination, journal-acceptance forecast, or final release
approval. The coordinator's second manuscript-review round and final
identical-input double build remain outstanding.

## Frozen object and material actually read

| Object | Verified SHA-256 |
| --- | --- |
| Initial `main.pdf`, 21 pages, 463423 bytes | `3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b` |
| `AUTHOR_REPORT.md` | `87c1661675c9c7fbe95974291c74e8a8b5f6914d3faabbc3deb4be98fb7015fa` |
| Complete 29-entry `INPUT_MANIFEST.sha256` | `ea282bedc12d736c9a0e421e5448744504ef742b593d6ebaf07368b27b090f63` |
| Accompanying complete C412 PDF, 14 pages | `66788e384cc8016240b17695decac08962f9289fef40a6782eeb108bd3ab699a` |

The manifest check returned 29/29 matching inputs. I read every manuscript
section, both appendices, both scripts, the macro/preamble files, bibliography,
and all 147 source table rows. I also read the complete 1107-line extracted
manuscript text and inspected all 21 existing individual page images. A fresh
read-only `pdftotext -layout main.pdf -` stream compared byte-for-byte equal to
the preserved text used for this reading; no PDF was rebuilt.

All twelve accompanying evidence files were inspected: the entire C412 PDF
text, the classification and analytic proof package, scout report, both frozen
execution contracts, both full Python programs, both full JSON outputs, the
previous proof review, and its documentation closure. For each JSON output,
the complete metadata and every one of its 147 records were read through
lossless compact rendering, including all alphabets/pruning sizes/words in
the producer output and all original-coordinate states in the independent
output. This was not a sample of nonempty or exceptional records.

Read-only byte comparisons additionally confirmed that all twelve evidence
copies equal the exact original files identified in `CITATION_AUDIT.md`.
The imported theorem and both C412 classification tables were compared with
the supplied complete predecessor, including its analytic proof, finite
complement and sharp-bound argument. The older review was treated as historical
evidence, not as a substitute for examining those arguments.

The author report, citation audit, paper plan, build history, actual converged
LaTeX/BibTeX diagnostics and both preserved baseline identities were also
inspected. Below, theorem/section identifiers and actual source files are the
locators; the structural-PDF advisory at the end is not upgraded into certified
page-anchor integrity.

## Mathematical audit

| Claim / actual manuscript location | Review result and decisive reason |
| --- | --- |
| Full coefficient class; Theorem 1.1 and `sections/2_normalization.tex` | Evaluation at 0, 1, 2 gives the unique integer Newton coefficients `m,n,r`, with `m != 0`. For even `m=2κ`, scaling by nonzero `κ` gives precisely the stated monic integral map. For odd `m`, `q=n-(m+1)/2` is integral, `q(3-q)` is even, and the translated constant is exactly `A=mr+(3q-q^2)/2`. These are rational affine bijections for either sign of `m`, with the stated inverse coordinate recovery and unchanged least native periods. |
| Half-form integrality; Lemma 3.1 | The maximum local norm argument has a unique dominant quadratic term at every prime. At 2 its norm is `2M^2`, greater than `2M` and the integral constant when `M>1`; thus the dyadic denominator causes no omitted cancellation case. The result is for the normal form, not for original `G_P` coordinates. |
| Boundary and height; Lemmas 3.2–3.3 | The summed-square identity is correct. It excludes `a>=2`; at `a=1` the integral equality forces coordinates 1 or 2 and then a constant word. The original-coordinate bound follows from `M^2-5M-2|a|<=0`. The displayed five-cycle at `a=0` has five different states and proves only the explicitly limited nonconjugacy witness. |
| Uniform negative range; Lemmas 4.1–4.2 | The centered recurrence has the necessary factor 2. `a<=-146` gives `N>=290`, `k>=17`, and `ρ>=35/2`. The annulus upper rounding and lower contradiction `5ρ-17/2>4ρ+8` both hold strictly at the stated threshold. The remainder bound `12+|s|<=ρ+23/2<2ρ` forces exact coefficient separation, even offsets and `s=4t`; this is not an asymptotic argument. |
| Inherited word exhaustion; Lemma 5.1 and Proposition 5.2 | The six local cases are fully reproduced, including the cyclic boundary and periods one and two. The surviving `t=-1,0,1,3` patterns give exactly the four table families. Algebraic existence does not reuse a large-parameter inequality at small indices. Distinctness checks retain both three-cycles at `k=0` and rule out a shortened four-cycle. In the large range the unique center and fixed `s` allow at most one surviving row, hence at most six points. |
| Proved finite residual; Section 6.1 and Lemma 6.1 | The odd-coordinate transition and inverse preserve the odd lattice because the numerator is divisible by 8. `B_a=4+isqrt(9-8a)` and the second alphabet inequality contain every periodic coordinate. The descending finite sets preserve every periodic orbit; their stable injective restriction is a permutation. Thus finite exhaustion has no independent period cutoff and proves both inclusions, not just a count. |
| Independent reconstruction; Section 6.3 and complete checker source | The same original square `[-19,19]^2` is complete for every residual parameter: at integer `M=20`, `M^2-5M-290=10>0`, and the polynomial increases thereafter. The path-index algorithm correctly handles escape, completed paths and the repeated-vertex suffix. Source order really computes all 147 graphs before loading author results. It does not import the producer or reuse doubled-coordinate filtering/pruning. |
| Four families, eleven exceptions, counts; Theorems 1.2, Propositions 7.1–7.2 and Tables 1, 2, 5 | All family/exception words, parameter labels and least periods agree with the full stored outputs. The two exceptional four-cycles at `-11` and `-1` differ from the respective parametric four-cycles. Other exceptional periods are outside the parametric list, so the indicator formulas need no overlap subtraction. The complete residual records have maximum 17 only at `a=-1`, with disjoint lengths 4, 4 and 9. The analytic outer ranges then give the global bound. |
| Even branch and full equality locus; Appendix A and proof of Theorem 1.1 | `D=α-h^2+(2-e)h`, translation by `h`, and recovery `(w-h)/κ` agree with C412. Both full imported tables preserve all index restrictions: in particular the odd branch's second three-cycle begins at `k=1`, and the even branch's stated within-row coincidences remain. C412's maximum 8 excludes even `m` from equality at 17. Hence the whole-class equality condition is exactly odd `m` and `A=-1`. |
| Ordinary returns; Corollary 7.3 and Section 8 | A length-`d` cycle contributes `d` points iff `d` divides the native iterate. The formal exponential identity gives the stated finite product. No finite-quotient period, algebraic multiplicity, arithmetic-prime Euler factor, root number, automorphy or spectral realization is substituted for these ordinary rational-point counts. |

## Certificate migration and execution boundary

Both complete programs implement their described algorithms. The producer
checks recurrence, distinct adjacent states, disjoint cycles, full stable-set
coverage and inclusion of every applicable proved family. Canonicalization is
by rotation alone. Its wrapper really uses `range(-145, 2)`; the appendix
accurately identifies the printed core and the omitted-but-accompanying wrapper.
The independent program compares whole oriented words and expanded state sets,
not merely the maximum or aggregate histogram.

A read-only comparison of already stored fields confirmed 147/147 matching
parameter labels, full word lists, histograms, point counts and cycle counts
between the two JSON files. The format-only renderer's stdout also compared
byte-for-byte equal to `tables/residual_rows.tex`. Neither operation evaluated
a map, constructed a graph, searched for a cycle, or recomputed a recurrence.

The complete outputs support the manuscript's receipts: 306 periodic points
and 113 oriented cycles **across different maps**, 223587 independently
processed vertices, the nine listed least periods, eleven unmatched cycles,
and sole maximizing parameter `-1`. The stored author execution is
2026-09-08T14:25:24.330685+00:00; the independent execution is
2026-09-08T14:32:39.006969+00:00. Their recorded source/input hashes match the
supplied actual files and the hashes printed in Appendix B.

No mathematical program, old or new, was executed for this review. No
mathematical uncertainty arose that required a new execution contract.
In particular, this review does not claim to have independently regenerated
the producer's pruning trajectories or the checker's escape-edge counts.
Those are inspected historical receipts; algorithm correctness, complete
range coverage, full retained results, and exact artifact migration were the
present checks. The prior independent run remains a declared proof dependency.

## Citations, ownership and contribution

All four bibliography entries are actually cited and resolve in the converged
PDF. The external uses were checked against primary sources on 2026-09-09:

- [Ingram's arXiv record](https://arxiv.org/abs/1111.3609) supports the
  canonical-height/specialization context and the displayed `+x` quadratic
  conjecture, whose determinant is `-1`. Its scope is not confused with C424.
  [Crossref's DOI metadata](https://api.crossref.org/works/10.1112/plms/pdt026),
  retrieved directly, confirms author/title, volume 108, issue 3, pages 780–808,
  online date 22 July 2013 and print issue March 2014. The bibliography's 2014
  issue year is justified; no unread journal proof is claimed as inspected.
- [Kim–Krieger–Postolache–Szeto v2 record](https://arxiv.org/abs/2412.01668v2)
  and the [primary v2 introduction/Theorems A–B](https://arxiv.org/html/2412.01668v2)
  support the growing odd-degree conservative construction from integer-valued
  polynomials. They do not assert this fixed quadratic classification. The
  bibliography correctly identifies all four authors, v2 on 8 July 2025, and
  the initial 2 December 2024 submission. The generated HTML display date is
  not treated as a different deposited version.

C412 is explicitly an anonymous unpublished internal predecessor, supplied
in full, and AM1 is explicitly an internal proof/certificate archive. No
invented journal status, human author identity or external review is attached
to either. The annulus, maximum-coordinate, six-symbol and finite-permutation
mechanisms are attributed at their actual use; the local-word proof is
reproduced with attribution. The elementary Newton normalization is not sold
as a new method.

The result-level narrative is therefore coherent as **one integrated
coefficient-class classification**, not several independent contributions
manufactured from its bound, exceptional periods and zeta formula. The
methodological dependence on C412 remains strong. This scoped review supports
the full-class presentation, not a new-method claim or a claim of worldwide
priority. The manuscript explicitly respects that distinction.

## PDF, build evidence and remaining release gates

All 21 actual page images were inspected: opening theorems, all cycle tables,
the displayed derivations, both multi-page code listings, all continued receipt
rows and the bibliography. No clipped content, equation collision, missing
row, illegible symbol, unresolved citation marker or broken table continuation
was observed. The source and extracted text agree on the printed claims.
The converged current `main.log` has no Warning/Error/Overfull/Underfull
diagnostic; the bibliography log reports four entries and no warning. The
22 font entries are embedded Type 1 fonts with Unicode mappings. Visible
authorship is anonymous and Author metadata is blank.

The preserved first baseline and the current baseline are real different-input
builds: their PDFs have hashes `95857f7d412d72830ca309733c99519cdb21bb48a53702a3c58ced490989f52d`
and `3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b`.
Comparing all 29 current input paths with `baseline/round0/` found exactly one
changed file, `sections/B_certificate.tex`; its actual diff only displays the
long predicate instead of leaving it inline. All 29 current inputs match
`baseline/round0_layout1/` byte-for-byte. The original nonfatal 10.79245 pt
overflow remains in the first build log; it was not erased or called a failed
mathematical run. These two builds do not constitute the still-required final
identical-input build pair.

The ARS local-PDF structural preflight was attempted on both actual PDFs.
Both returned `UNAVAILABLE` because `pypdf` is absent. No dependency was
installed, and no `PASS` or certified structural page-anchor claim is inferred.
For the permitted single-report write scope, the complete stdout advisories
are retained here under their local reference slugs:

`ref_slug: C424_initial_main`

```json
{
  "schema": "pdf_read_preflight/1",
  "verdict": "UNAVAILABLE",
  "file": "main.pdf",
  "sha256": "3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b",
  "declared_page_count": null,
  "enumerated_page_count": null,
  "reader_page_count": null,
  "warnings": ["pypdf-not-installed: preflight cannot parse the document"],
  "generated_at": "2026-09-09T06:39:16.122890+00:00",
  "tool": "pdf_read_preflight/1.0.0"
}
```

`ref_slug: C412_accompanying_main`

```json
{
  "schema": "pdf_read_preflight/1",
  "verdict": "UNAVAILABLE",
  "file": "evidence/C412_main.pdf",
  "sha256": "66788e384cc8016240b17695decac08962f9289fef40a6782eeb108bd3ab699a",
  "declared_page_count": null,
  "enumerated_page_count": null,
  "reader_page_count": null,
  "warnings": ["pypdf-not-installed: preflight cannot parse the document"],
  "generated_at": "2026-09-09T06:39:16.186989+00:00",
  "tool": "pdf_read_preflight/1.0.0"
}
```

The initial help lookup used the wrong script subdirectory; the actual
`ars/scripts/pdf_read_preflight.py` was then located and used. This diagnostic
lookup error was not a PDF build or mathematical execution.

Required manuscript corrections from this round: **none**. A no-change author
disposition is justified; cosmetic edits are not needed to manufacture a
revision. The coordinator still needs the separately authorized second
manuscript review and final release/build checks. The evidence directory,
complete predecessor copy and manifest must continue to accompany the
manuscript because the finite proof dependency is substantive.

The `research-review` skill supplied the claim/evidence/gap/ownership review
structure, adapted to the explicit current-team mathematical assignment;
the bounded ARS citation/read-integrity phase supplied primary-source and
PDF-advisory checks. No external-model call or external manuscript upload
was made. Only this review report was written; no paper, certificate,
baseline, shared registry or Git state was edited.
