# Paper 10 manuscript release candidate

**Title:** *Separated Reflections and Observable Collapse of Indiscrete
Arithmetic Prime Packets*

**Author:** Liang Wang, School of Artificial Intelligence and Automation,
Huazhong University of Science and Technology (HUST),
wangliang.f@gmail.com

## Claim boundary

For each rational prime, the manuscript starts from Paper 9's theorem that the
actual finite-kernel packet, each inherited orbit, and the time-orbit quotient
are nontrivial indiscrete spaces. It proves their direct singleton `T0`,
Hausdorff, and completely regular Hausdorff universal images; constant scalar
and fixed-operator continuous maps; trivial Borel algebras; constant measurable
maps to countably separated targets; and classification of positive finite
measures by total mass. It also proves the transported-law/trivial-continuous-
character result on the actual `Q_p` owner, the two standard-circle comparison
directions, and the discrete-label/`ell^1_+` classification for an explicitly
tagged copied coproduct.

The copied coproduct is not the global Deninger suspension. The manuscript
makes no Radon, Haar, state, trace, representation, unbounded-operator,
determinant, analytic-continuation, zero-matching, quantization, Hilbert--Pólya,
or Route-B claim. The seven Route-A records are five exploratory negative
priors and two rejected copied controls; every owner fails A1--A4.

## Release contents

- `paper.pdf` — 19-page A4 XeLaTeX/BibTeX release-candidate PDF.
- `manuscript.tex` — complete English manuscript with independent
  Simplified-Chinese abstract and provisional declarations.
- `references.bib` — nine cited entries, nine in-text keys, zero orphan or
  missing keys, and one load-bearing companion-paper self-citation.
- `figures/owner_collapse_and_proxy.tex` — native TikZ actual-owner and proxy
  interface map.
- `figures/copied_coproduct_ledger.tex` — native TikZ copied-label and mass
  ledger.

No external raster or vector image is imported. `pdfimages -list paper.pdf`
reports zero embedded images; both figures remain native vector graphics.

## Build

From this directory:

```text
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
```

The audited clean build used XeTeX/TeX Live 2022-dev, BibTeX, TeX Gyre
Termes, TeX Gyre Termes Math, TeX Gyre Heros, TeX Gyre Cursor, and Noto Serif
CJK fonts. It has zero undefined citations, undefined references, duplicate
labels, BibTeX warnings, missing glyphs, build errors, or overfull boxes. Four
harmless underfull-box notices remain. All PDF fonts report `emb=yes`,
`sub=yes`, and `uni=yes`.

## Deterministic controls

The release candidate was rechecked from the project directory with:

```text
./experiments/reproduce.sh
```

Result: 24/24 tests passed; ten CSV artifacts contain 676 rows; verify-only
validation passed; two fresh generations were byte-identical; no bytecode was
left behind. The final controls-manifest SHA-256 is
`edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215`.
These finite controls are regression evidence, not proof of the infinite or
source-specific theorems.

## `figure_table_trace`

| Figure ID | Final source and SHA-256 | Forward claim/use coverage | Reverse use-to-evidence coverage | Explicit limitations |
|---|---|---|---|---|
| `FIG-P10-1` | `figures/owner_collapse_and_proxy.tex` — `d5be1f45dbf4c5b3c7668d326e416166941dd9dbb7b7d0c64d076a8f41d03421` | The grouped actual-owner branch covers P10-1 singleton reflections, P10-2 scalar collapse, P10-3 trivial Borel/separated measurable maps, P10-4 total-mass measures, and the fixed norm/SOT/WOT part of P10-5. The lower `ACT-Q-p` branch covers law transport and the trivial continuous circle character; the orbit branch covers both P10-6 `beta` directions. | Every box and arrow is used in manuscript Figure 1 and maps back to proof-audit §§2--4, SHA `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a`; the crossed box maps to the theorem-boundary paragraphs in §§3--5. No decorative mathematical node lacks a textual owner or proof. | Excludes non-`T0` targets, algebraic/alternate-topology characters, representations, measurable fields, unbounded operators, traces, and topology transport through `phi_p`. |
| `FIG-P10-2` | `figures/copied_coproduct_ledger.tex` — `e4bceb3b3bb67d6a837014c44d226ce2131ca7cdd4184cdd4aa8da12f8f90291` | Covers the abstract countable tagged-coproduct theorem and P10-7--P10-8: component-union topology/Borel algebra, discrete-label `K0`, `ell^1_+` component masses, external `log p`, and prime/composite/arbitrary-label neutrality. | Every component, quotient arrow, mass arrow, external-data arrow, arbitrary-label control, and crossed global claim is used in manuscript Figure 2 and maps back to proof-audit §5 plus the copied-component controls in the final manifest. | Explicit modeling choice only; not a topology theorem for the global suspension, not an intrinsic prime discriminator, and not a selector of a nonzero mass, return time, trace weight, or A1 datum. |

The trace is bidirectional: every figure claim maps to a theorem/control owner,
and every registered visual use in the manuscript is represented by one of the
two rows. Any change to a TikZ source requires a new hash and trace re-lock.

Strict six-key ARS trace entries:

```yaml
- artifact_id: FIG-P10-1
  source_data:
    - "notes/proof_audit.md §§2–4; sha256:efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a"
    - "figures/owner_collapse_and_proxy.tex; sha256:d5be1f45dbf4c5b3c7668d326e416166941dd9dbb7b7d0c64d076a8f41d03421"
  transformation: "Manual native-TikZ owner/arrow projection of the proved P10-1–P10-6 domain map; no external image or data transformation."
  caption_claim: "Every registered actual owner has singleton separated reflections, constant scalar/fixed-operator observables, and trivial-Borel/total-mass interfaces; only ACT-Q-p receives the transported-law/trivial-character branch, and only ACT-ORBIT-p-a receives the two beta directions."
  supported_manuscript_claims:
    - "P10-1 singleton K0/Hausdorff/CRH universal images — manuscript §3, Theorem 3.1, Figure 1."
    - "P10-2 constant C/Cb and P10-5 fixed norm/SOT/WOT maps — manuscript §3, Theorems 3.2–3.3, Figure 1."
    - "P10-3 trivial Borel/separated measurable maps and P10-4 total-mass/Dirac collapse — manuscript §4, Theorems 4.1–4.2, Figure 1."
    - "P10-5 transported ACT-Q-p law and trivial continuous circle character — manuscript §5, Theorem 5.1, Figure 1."
    - "P10-6 beta noncontinuity actual-to-circle and continuity in reverse — manuscript §5, Theorem 5.2, Figure 1."
  limitations: "Does not classify non-T0 targets, algebraic or alternate-topology characters, representations, measurable fields, unbounded operators, traces, or any topology transported through phi_p."

- artifact_id: FIG-P10-2
  source_data:
    - "notes/proof_audit.md §5; sha256:efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a"
    - "results/separated_reflection_controls_manifest.json; sha256:edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215"
    - "figures/copied_coproduct_ledger.tex; sha256:e4bceb3b3bb67d6a837014c44d226ce2131ca7cdd4184cdd4aa8da12f8f90291"
  transformation: "Manual native-TikZ projection of the abstract countable tagged-coproduct proof and its exact copied-label/mass controls; no external image or fitted data."
  caption_claim: "A declared tagged coproduct of copied indiscrete components retains exactly the discrete labels and ell1-positive component masses; prime logarithms are external and arbitrary/composite labels have the same abstract classification."
  supported_manuscript_claims:
    - "Component-union topology/Borel algebra, discrete K0 label quotient, and T0-map factorization — manuscript §6, Theorem 6.1 and Corollary 6.2, Figure 2."
    - "ell1-positive component-mass classification including zeros — manuscript §6, Theorem 6.1 and Corollary 6.3, Figure 2."
    - "External unbounded log p, label neutrality, and no source-global promotion — manuscript §6, Corollary 6.3 and §6.1, Figure 2."
  limitations: "Explicit modeling choice only: not the global Deninger-suspension topology, not an intrinsic primality test, and not a selector of a nonzero mass, return time, trace weight, or A1 datum."
```

## Frozen evidence ledger

| Artifact | SHA-256 |
|---|---|
| `notes/composition_blueprint.md` | `b2b2aa203abe4bed3067279049ad12296fe51917043f8ecb0b88714150dbd50e` |
| `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` |
| `notes/phase3_peer_review.md` | `cd075d267865812c2368679346a2dfde9a5a976d4306b4dc61664adf5f8a3a7e` |
| `notes/phase3_final_gate.md` | `ec672859dd28e433f82a392685b7816c421b55c096f334bc3ca803dc87a68541` |
| `notes/route_audit.md` | `fded0943eb3c628e90b407c14aece688b1a79f8be4510c02e98010592b9ca4ee` |
| `notes/pre_manuscript_citation_audit.md` | `9b9ee072cdc44129084ee28945574bd59750dbbec39008301fea7eef3c1d6850` |
| `results/separated_reflection_controls_manifest.json` | `edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215` |
| `notes/sources/.gitignore` | `6cbf9577be5add7a925718f4047f672fe46d991772fd451f428390aa323b6d3f` |

The seven immutable Stage-10 Route-A records are:

| Owner ID | YAML SHA-256 |
|---|---|
| `DEN-EF-ACTUAL-SEPARATED-REFLECTION-P` | `57bdf64ffcdf66797ba10985082e9bcb42cd64b45bf479a5af8de4d125e123af` |
| `DEN-EF-ACTUAL-CONT-OBS-P` | `a94cc0a8fb48488de0e46bb6f30e845ee3641b5a8517da707e6b1570e212af82` |
| `DEN-EF-ACTUAL-BOREL-MFIN-P` | `be95f98692bab5eb54ef93edab64b0f0bb8bbf7c0131f7021f559c614de94b0d` |
| `DEN-EF-QP-ACTUAL-CONT-CHAR-P` | `9d846ba5577c5424da786a9b28edb471b96a2246ec91cc9d4de5c6767929c146` |
| `DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P` | `f8b9a454c6ebb14163c78ed1e6bd6c188b8a96522fff1c2ba26f3ab45e022ed1` |
| `DEN-EF-COPROD-PRIME-K0-CONTROL` | `5b78ea0199d67457b6963664d42934dde04ee93aa78cf7bd642403f81bc9b6d3` |
| `DEN-EF-COPROD-PRIME-MFIN-CONTROL` | `d38e066923abceae8ebbb382c876b08c562dcff554be465ec5a10d887ccf1aad` |

All seven validate against the frozen schema and enum set with exactly nine A2
validation fields each; every artifact path resolves, Route B is false, and no
Stage-10 Route-B YAML exists.

## Release-candidate hashes

| File | SHA-256 |
|---|---|
| `manuscript.tex` | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` |
| `references.bib` | `201e997ad953ebc1f27bd4c068400be656a1b9b6fbc4a231443ad8c2770e98b1` |
| `figures/owner_collapse_and_proxy.tex` | `d5be1f45dbf4c5b3c7668d326e416166941dd9dbb7b7d0c64d076a8f41d03421` |
| `figures/copied_coproduct_ledger.tex` | `e4bceb3b3bb67d6a837014c44d226ce2131ca7cdd4184cdd4aa8da12f8f90291` |
| `paper.pdf` | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |

## Human-confirmation and public-release boundary

The CRediT, funding, competing-interest, acknowledgment, affiliation, venue,
license, repository/archive, and final journal-facing AI-disclosure wording
remain explicitly provisional and require confirmation by the human author.
The companion Paper-9 citation is transparently an unpublished internal-batch
artifact bound to PDF SHA-256
`c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`;
no false or mutable public artifact URL is asserted. An immutable public
identity must be added only after the final batch sync and re-lock.

All twelve `../notes/sources/*.pdf` files are local verification copies and
must remain outside any public payload. The exact local exclusion rule is
`../notes/sources/.gitignore`, hash
`6cbf9577be5add7a925718f4047f672fe46d991772fd451f428390aa323b6d3f`.
Manifests, checksum ledgers, preflight sidecars, canonical URLs, locators, and
hashes may be synchronized. A fresh-clone staged-file audit requiring zero
third-party PDFs remains mandatory immediately before public synchronization.
