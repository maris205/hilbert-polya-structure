# Independent Plan, Citation, and Figure Integrity Review

Review date: 2026-08-14 UTC  
Reviewer role: fresh independent, read-only plan/citation/figure reviewer  
Verdict: **PASS — `PAPER9_PLAN_FIGURE_CITATION_PASS`**

## Scope and independence boundary

I reviewed the frozen Paper-9 plan, citation ledger, BibTeX file, figure-data
contract, all generators, deterministic audit, machine manifest, provenance,
quality-assurance record, LaTeX captions, and all nine publication outputs.
I did not author any of these assets.  I did not modify the plan, citation
files, bibliography, figures, source lock, proof, result, result manifest,
code, or official reports.  The only project write made by this review is
this file.

Regeneration was confined to temporary replicas containing the eight frozen
scientific inputs and the figure-support files but no Paper-9 candidate code.
No candidate or registered-run entry point, project test suite, network
resource, external prime table, numerical value of (s), numerical
logarithm, zero datum, composite shell, or centralizer calculation was used.

## Bound asset package

| Artifact | Independently observed SHA-256 |
|---|---|
| 24-file framed asset tree | `312c4b095b58acb9e8047d7113308d28870e3db7633f37d17bd904ca2c7ebfaa` |
| `PAPER_PLAN.md` | `406e443e96e4822acb3530990cfe45b64921821738d013f0d328d551de5ed088` |
| `notes/CITATION_VERIFICATION.md` | `ae25c56d17703ee00b8168eba33bbec77c688e72c8fb6ac520214e523241b808` |
| `paper/references.bib` | `37ee7c23398806b9e59e86ec9fbf6fd0dfc0483043cff9459d0837b2bd2457ae` |
| `paper/figures/FIGURE_MANIFEST.json` | `8ae2709444e6e06286b061635352d2ba0c419c04d313edf1272cb57ab41b2b83` |
| `paper/figures/DETERMINISM_AUDIT.json` | `e741a74df5117d146b8ccb85cbbf2d8a30e16a62388cb1f68810fafaa54b38ea` |
| `paper/figures/FIGURE_QA.md` | `fb8eb070dc604af049d603687ed9ddaaa3d268b1acf250c27461f6b9a2123a40` |
| `paper/figures/PROVENANCE.md` | `927b875164b31c036142e4f0f143b7d0b42c6b1253e89a67e4b5389905713e90` |
| frozen `results/result_manifest.json` | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` |

The asset-tree digest was not accepted from the author-side report.  I
recomputed it over the exact 24 paths consisting of `PAPER_PLAN.md`, the
citation ledger, and every regular file under `paper/`.  Paths were sorted as
POSIX strings, and each path/content pair was independently length-framed
with unsigned 64-bit big-endian lengths.  The resulting digest is the value
shown above.  Every member was a single-link nonsymlink regular file, and no
bytecode or cache entry was present.

The final result manifest parses without duplicate keys, has status `PASS`,
binds the exact source and execution-tree hashes, records one registered
exact audit and zero numerical runs, and states that no rerun occurred.  Its
hash is reproduced by the plan, citation ledger, data contract, figure
manifest, and provenance record.

## Plan and claim--evidence review

The plan is a coherent specialized mathematical negative note rather than a
method or discovery paper.  Its working title, one-sentence thesis, section
order, figure plan, appendices, and conclusion all retain the terminal
classification

`PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED /
A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

The eleven planned claim rows have the correct evidence roles:

- C1 and C2 are explicitly classical re-derivations.  The split/inert common
  periods and the binary/ramified boundaries are supported by the frozen
  proof; the five finite rows are corroborating controls only.
- C3 and C4 keep the point-potential/raw-return product separate from the
  externally assigned one-time orbit-label product.  In particular, the
  mixed (p=5) factor remains the semantic stress test rather than being
  replaced by a degree-four label factor.
- C5 states only the fixed nonzero scalar pure-denominator degree
  obstruction.  It does not extend to matrices, numerators, alternating
  products, Fredholm determinants, or cohomological cancellation.
- C6 records the exact equal-weight power sum (m_p^{1-r}) and therefore
  claims repair only at the first repetition when (m_p>1).
- C7 identifies the fractional exponent identity as shell-global normalized
  counting.  Its composite-(q) extension is proof-only and symbolic; no
  composite value is selected.
- C8 assigns the three safe global convergence bounds to the proof, not to
  the finite audit.  The gap (2<\operatorname{Re}s\le3), exact abscissa,
  analytic continuation, and conditional convergence remain unclaimed.
- C9 reports the construction cost of a one-orbit selector without claiming
  that a canonical selector is impossible.
- X1 and X2 correctly reserve centralizer quotients and richer cancellation
  mechanisms as outside-scope escapes.

The exact audit is described as one development-seen run at only
(p=2,3,5,7,11), with 203 nonzero points, 37 primitive cycles, and twelve
passing exact controls.  No finite observation is promoted to an all-prime
or global analytic theorem.

The novelty calibration is consistently **2.5--3/10**.  The plan attributes
prime-lattice classification, finite-lattice products, and weighted zeta
formalism to prior work and restricts the Paper-9 delta to a transparent
semantic/mechanism audit.  It prohibits priority, new-classification,
prime-generating, transfer, determinant, quantization, prime/zero, and
Hilbert--Pólya claims.  This framing is conservative and supported.

## Citation and bibliography gate

Mechanical extraction found exactly eleven distinct citation-ledger headings
and eleven distinct BibTeX entries.  The sets are identical:

`Gaspari1994`, `PercivalVivaldi1987`, `DysonFalk1992`,
`BaakeRobertsWeiss2008`, `BaakeNeumaerkerRoberts2013`, `ArtinMazur1965`,
`Ruelle1976`, `ParryPollicott1990`, `BaakeLauPaskunas2010`, `TanLi2025`, and
`Chandra2026`.

There is one entry per key, balanced entry structure, no placeholder
identifier, no unresolved verification flag on a source, and no unverified
auxiliary citation.  Authors, titles, years, venues, volumes/issues, page
ranges, DOI fields, arXiv identifiers, and entry types agree with the frozen
source-by-source ledger.

The package handles the metadata boundaries correctly:

- the current Taylor & Francis DOI is used for Dyson--Falk, while the stable
  JSTOR record is retained as its URL rather than treated as a second paper;
- the Baake--Neumärker--Roberts arXiv record is included without replacing
  the published DOI;
- the Parry--Pollicott Astérisque monograph omits a disputed physical-page
  total and keeps the stable series/number/DOI metadata;
- Baake--Lau--Paskunas uses the 2010 volume year rather than its earlier
  online-first date;
- Tan--Li and Chandra remain `@misc` arXiv preprints, and their
  `10.48550/arXiv...` identifiers are not represented as journal DOIs.

The claim-role firewall is also sound.  Gaspari and
Baake--Neumärker--Roberts are direct novelty collisions; arithmetic cat-map
sources are context only; Artin--Mazur, Ruelle, Parry--Pollicott, and the
toral-zeta sources delimit existing product machinery; Tan--Li and Chandra
are contemporary context, not proof of the Paper-9 theorem.  The manuscript
plan requires direct collisions at the relevant claim sites and does not use
any source to support an excluded priority, transfer, centralizer, or
prime/zero claim.

## Generator and input-contract audit

Static inspection covered all seven Python support/generator files.  No
network-capable or candidate module is imported.  The loader verifies eight
immutable scientific source hashes before exposing data, requires the raw
result and strict manifest to pass, checks the exact source-lock and
classification, enforces the locked five-prime tuple, and rejects nonzero
numeric/search/centralizer counters or forbidden data-access flags.

All plotted values are read from the frozen raw JSON or obtained by exact
rational transformations of its rows.  The loader verifies shell partitions,
cycle partitions, multiplicities, repetitions, fractional sums, selector
costs, and scalar degrees.  Hard-coded explanatory text is protected by the
same exact raw-result hash, proof markers, twelve-control gate, and proof-only
contract.  The generators neither import experiment code nor infer a new
scientific result.

## Independent isolated regeneration

I constructed two independent temporary Paper-9 asset replicas.  Each
contained only the plan/bibliography, the eight frozen scientific inputs, and
the eight generator/support files needed for rendering; neither contained
the `code/` tree.  In each replica, `generate_all.py` performed its two
complete render passes under bytecode-disabled mode, `PYTHONHASHSEED=0`,
fixed SVG hash salt, and `SOURCE_DATE_EPOCH=1471132800`.

Both replicas completed successfully and produced no bytecode/cache entry.
Within each replica the two passes were byte-identical.  Across replicas,
all nine outputs, `DETERMINISM_AUDIT.json`, and `FIGURE_MANIFEST.json` were
byte-identical.  They were also byte-identical to the frozen live package.
This independently reproduces the author-side determinism claim instead of
trusting its `PASS` field.

| Figure | PDF SHA-256 | SVG SHA-256 | PNG SHA-256 |
|---|---|---|---|
| 1 | `5df608f06eb36fd73d61888ffa975591c770323d0578361f3cef81341ee92505` | `07179194972d57e8235423252080ce67aade35e9bb4d8b95a6749ccc4931f74a` | `154846b77bdc4a90898eb9b9d88fef1fdfb55a8dd2eac7b90f02ab06562b3600` |
| 2 | `a3eda49062d854529c84ae2b89669064dee025fe6c3fb6ef66ea9d9b860f4da2` | `03291e1efe244821ba910589c548e55fa64eab9480c945e988e2c9dec324c607` | `746e7ff47aed5c6b6870d318e5ba0212137ada37a7243136b8975ec76df086ff` |
| 3 | `826c2fda24125a4b87d7dad8e42e2e0ffc633e9384eec47f1a9822cc3217fbbb` | `3c977277da3872b30cb89bde26d86060c36143cf353061b03f93216e00bcbffa` | `40895d6ff5d50d930edfb1afaadb2fbcc5a62feeba70e932b368537541ce2b31` |

The regenerated manifest is exactly
`8ae2709444e6e06286b061635352d2ba0c419c04d313edf1272cb57ab41b2b83`,
and its bound determinism audit is exactly
`e741a74df5117d146b8ccb85cbbf2d8a30e16a62388cb1f68810fafaa54b38ea`.

## Format and original-resolution visual QA

Independent format probes reproduced every machine claim:

- each PDF is a one-page vector document with zero raster-image objects,
  zero Type-3 fonts, and all fonts embedded, subsetted, and Unicode mapped;
- each SVG parses as XML, contains no `<image>` node, and preserves text as
  selectable text, with 59, 49, and 81 text nodes for Figures 1--3;
- each PNG is RGBA at 299.9994 dpi, within the 300-dpi tolerance, with pixel
  dimensions `2160x1335`, `2160x1425`, and `2160x1500`.

All three PNGs were inspected at original resolution.

1. Figure 1 cleanly displays all five point-period partitions,
   (m_p=(1,2,4,6,24)), the (p=2) and (p=5) boundaries, and the
   (p=11) split strata.  The dashed single-factor annotation is separated
   from the multiplicity labels; cards, legends, values, and the proof-source
   footer are unclipped and legible.
2. Figure 2 makes the two construction pipelines visibly distinct, keeps the
   right-side `retains`/`imports` labels inside their boxes, shows both exact
   (p=5) products without collision, and displays the complete exact
   (m_p/r) grid.  Its footer states the no-numerical-evaluation boundary.
3. Figure 3 separates all five mechanism cards.  In particular, the
   centralizer card has distinct title, `UNTESTED` status, and Paper-10 label
   with no overlap.  Equal-weight sums, fractional weights, selector costs,
   the symbolic composite box, and the terminal footer are readable and
   semantically correct.

No label, mathematical glyph, axis, legend, hatch, card, table cell, footer,
or page-edge element is clipped.  No text/data overlap or exposed raw math
markup is present.  Statuses use text and shape/hatch in addition to color.
There is no decorative figure-level title competing with the LaTeX caption.

The three LaTeX captions use the vector PDF masters, have unique labels, and
are self-contained.  They explicitly distinguish finite controls from
proof-only claims, raw returns from one-time labels, and the proved scalar
obstruction from the untested centralizer and richer-determinant escapes.

## Immutability and disposition

After regeneration and all independent probes, every pre-existing member of
the 24-file asset tree still reproduces its frozen hash.  The source lock,
raw result, independent result review, official reports, and strict result
manifest are unchanged.  No live figure was regenerated or edited.

The plan, citation package, figure-data contract, generators, deterministic
outputs, manifest/provenance chain, captions, and visual semantics are
mutually consistent with the certified Paper-9 result and its deliberately
narrow novelty claim.  Exact blockers: none.  **PASS.**
