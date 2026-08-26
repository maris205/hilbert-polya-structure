# Paper 13 Phase-2 framework and analytic-source manifest

Manifest date and source cutoff: **2026-08-15 (Asia/Shanghai)**  
Scope: continuous real-line projective multipliers, twisted group formulas,
amenability/full--reduced norms, named groupoid-framework hypotheses, and Borel
multiplier background. The separate Phase-2 novelty lane owns the bounded
exact-package search.

## 1. Integrity and retention protocol

Six exact primary-source PDFs were retained in this directory. Every retained
PDF has a same-stem sidecar produced by the unmodified ARS
`pdf_read_preflight.py` script. An initial run returned `UNAVAILABLE` because
the reader dependency was absent; it was not treated as validation and was
replaced after installing `pypdf 6.16.0`. Every final sidecar reports schema
`pdf_read_preflight/1`, tool `pdf_read_preflight/1.0.0`, verdict `PASS`, equal
declared/enumerated/reader page counts, and an empty warning array.

`framework_sources.sha256` covers exactly the six PDFs and six final sidecars.
It intentionally does not self-hash this manifest. The adjacent `.gitignore`
excludes every `*.pdf`; all retained source bytes are local research evidence,
not manuscript attachments or authorized public-supplement content.

Two already-preflighted Paper-11 framework PDFs are reused by exact hash and
locator in Section 5 rather than copied. Sorkin (1978) is recorded as an
official-page/abstract sentinel in Section 4 because no lawful full text was
available; no local Sorkin PDF exists.

## 2. Exact retained manifestations

| ID | Exact local file and authoritative manifestation | Bytes | Pages / final preflight | PDF SHA-256 | Sidecar SHA-256 | Regularity tier and load-bearing ceiling |
|---|---|---:|---|---|---|---|
| `SRC-AUSTAD21` | Are Austad, “Spectral Invariance of \(*\)-Representations of Twisted Convolution Algebras with Applications in Gabor Analysis,” *Journal of Fourier Analysis and Applications* **27**, article 56 (2021), DOI `10.1007/s00041-021-09860-z`; official [record](https://link.springer.com/article/10.1007/s00041-021-09860-z) and [PDF](https://link.springer.com/content/pdf/10.1007/s00041-021-09860-z.pdf); `src-austad-twisted-convolution-2021.pdf` | 539,378 | 22 / `22=22=22`, `PASS`, no warnings | `9edaf338a3d1f2f1b503a3709f20fceaa2bf1a6624a8d6fce0d80f3f15c77bc3` | `00d34a9fb17f2bcb5e00192f4ed4c3f9fd35848b6c12783023b0f877eb5b752e` | `MIXED`: cocycle regularity continuous; gauge theorem N/A; full-text access. Exact normalized cocycle, twisted product/star, projective left regular representation, integrated form, and amenable maximal norm; no gauge-triviality theorem and no actual non-Hausdorff groupoid ownership |
| `FW-AO20-v1` | Are Austad and Eduard Ortega, “C*-uniqueness Results for Groupoids,” arXiv `2005.06208v1` (13 May 2020), [exact PDF](https://arxiv.org/pdf/2005.06208v1); published in *International Mathematics Research Notices* **2022**(4), 3057--3073, DOI `10.1093/imrn/rnaa225`, official [record](https://academic.oup.com/imrn/article/2022/4/3057/5901311); `fw-austad-ortega-cstar-uniqueness-v1.pdf` | 233,524 | 13 / `13=13=13`, `PASS`, no warnings | `c4b7b1cb7e225e3873b1071deb844b047ba0f1404aac4ca97002862aec2682c7` | `f48bbf527341557458f970163c12f309c56224ec9fe212a2f0b4ea507d93ebe8` | `MIXED`: cocycle regularity continuous; gauge theorem N/A; author-full-text access. Hypothesis/convention source for second-countable locally compact Hausdorff **étale** twisted groupoids; exclusion source only on the actual owner |
| `SRC-LEPTIN68` | Horst Leptin, “Darstellungen verallgemeinerter \(L^1\)-Algebren,” *Inventiones Mathematicae* **5** (1968), 192--215, DOI `10.1007/BF01425550`; official Springer [record](https://link.springer.com/article/10.1007/BF01425550); exact SUB Göttingen/GDZ [article scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0005/LOG_0026.pdf); `src-leptin-generalized-l1-1968.pdf` | 2,305,072 | 25 / `25=25=25`, `PASS`, no warnings | `0bde30eba4eb8cee42bed5285e32272994090d04fc8880f841799ed75c96039c` | `7e29d6f893f7a6ea3674c7295f221637c339cfc0c86b70e8a7e3c815554bfb39` | `MIXED`: measurable factor-system setting; gauge theorem N/A; official-library full-scan access. Original generalized-\(L^1\) amenability/maximal--reduced result, used only through Austad's continuous specialization and never as a continuous gauge source |
| `SRC-HUL64` | Andrzej Hulanicki, “Groups whose regular representation weakly contains all unitary representations,” *Studia Mathematica* **24** (1964), DOI registry `10.4064/sm-24-1-27-59`; official IMPAN [record](https://www.impan.pl/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/studia-mathematica/all/24/1/95703/groups-whose-regular-representation-weakly-contains-all-unitary-representations) and [scan](https://www.impan.pl/shop/en/publication/transaction/download/product/95703?download.pdf); `src-hulanicki-weak-containment-1964.pdf` | 5,950,418 | 12 spread-images / `12=12=12`, `PASS`, no warnings | `a30bcf1bda9699b56f1a846f15bc46f0ce420fb42f114fdc22d564d0a6f321fa` | `029aa3aff02517d95fea74f72f7b1d26c5cbeb5e7df4922d6aff6384e9d8bff6` | `MIXED`: cocycle and gauge regularity N/A; official full-scan access. Weak-containment/invariant-mean direction for locally compact groups only; no twist convention |
| `SRC-HUL66` | Andrzej Hulanicki, “Means and Følner condition on locally compact groups,” *Studia Mathematica* **27** (1966), 87--104, DOI `10.4064/sm-27-2-87-104`; official IMPAN [record](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/27/2/96164/means-and-folner-condition-on-locally-compact-groups) and [scan](https://www.impan.pl/shop/en/publication/transaction/download/product/96164?download.pdf); `src-hulanicki-folner-1966.pdf` | 3,269,534 | 10 spread-images / `10=10=10`, `PASS`, no warnings | `eacf80abfbd7dc7320b4130ff2a2028d98cbd89b48bcf8ee62562d3e79f64f4a` | `0cb8bad6a64a131656bbb7b392c08554056a8e61fa3443cfd47093951c13aea6` | `MIXED`: cocycle and gauge regularity N/A; official full-scan access. Locally compact invariant-mean/Følner background and Abelian-group inclusion only; no twist convention |
| `SRC-KLEP65` | Adam Kleppner, “Multipliers on Abelian Groups,” *Mathematische Annalen* **158** (1965), 11--34, DOI `10.1007/BF01370393`; official Springer [record](https://link.springer.com/article/10.1007/BF01370393); exact SUB Göttingen/GDZ [issue scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0158/LOG_0005.pdf); `src-kleppner-multipliers-issue-1965.pdf` | 8,946,465 | 73 / `73=73=73`, `PASS`, no warnings | `75f9f5e62e47e8c9dc885a5eba74ccbdfaefa296c02b1fcc5de8fbcf9dd51264` | `2eda422adce992695f0a2c4ea1b68ab821ee9a34790d32fc96c16689c38dc1f0` | `BOREL/BOREL`: exact official-library issue-scan access; classic projective-multiplier background and similarity by a Borel one-cochain only; never sole support for a continuous trivializer |

`SRC-AUSTAD21` is CC BY 4.0 in the exact PDF. The two IMPAN records label
their downloads CC BY. The GDZ manifestations impose noncommercial research
access/redistribution restrictions. The stricter project rule nevertheless
keeps **all six** source PDFs local-only.

## 3. Exact locator and convention index

### 3.1 `SRC-AUSTAD21`: continuous group formulas

- physical p. 5 / journal “Page 5 of 22,” Definitions 2.1--2.2 and
  Eqs. (2.1)--(2.2): a strongly continuous projective unitary representation
  satisfies `pi(x1)pi(x2)=c(x1,x2)pi(x1x2)`; `c` is a continuous normalized
  circle-valued 2-cocycle;
- physical p. 6 / “Page 6 of 22”: the twisted left regular representation is
  `L^c_y f(x)=c(y,y^{-1}x)f(y^{-1}x)`; twisted convolution is
  `integral f1(y)f2(y^{-1}x)c(y,y^{-1}x)dy`; the involution is
  `m(x^{-1}) overline{c(x,x^{-1}) f(x^{-1})}`;
- physical p. 7 / “Page 7 of 22”: the integrated form is defined, and
  **Proposition 2.4** says that for an amenable locally compact group and a
  continuous cocycle, the integrated twisted left regular norm is the
  maximal C*-norm on `L1(G,c)`. It explicitly identifies the statement as a
  special case of Leptin, Satz 6.

For additive `G=R`, `y^{-1}x=t-s` and the modular function is one. The source
therefore translates exactly to the frozen formulas

```text
(lambda_sigma(s)xi)(t)=sigma(s,t-s)xi(t-s),
(f *_sigma g)(t)=integral f(s)g(t-s)sigma(s,t-s) ds,
f^{*sigma}(t)=overline{sigma(t,-t)} overline{f(-t)}.
```

The canonical locator is Proposition **2.4**, not Proposition 2.3, in the
retained published manifestation.

### 3.2 `FW-AO20-v1`: named Hausdorff étale framework

- physical p. 1, abstract and introduction: the domain is a second-countable,
  locally compact, Hausdorff, étale groupoid with continuous 2-cocycle;
- physical p. 3, Section 2.3 opening: all groupoids in the paper carry that
  topology; étale means range, hence source, is a local homeomorphism, so
  source and range fibres are discrete;
- physical pp. 3--4, Eqs. (2.1)--(2.5): normalized continuous groupoid
  cocycle, ordinary continuous compact-support test functions, twisted sum
  product/involution, and the `I`-norm completion;
- physical p. 7, Theorem 3.1: the main `C*`-uniqueness result retains the
  same second-countable locally compact Hausdorff étale hypotheses.

The OUP record confirms the published identity and DOI. The retained arXiv
v1 is the exact author full text used for physical locators.

### 3.3 `SRC-LEPTIN68` and the norm chain

- physical p. 2 / printed p. 192: the introduction states that for amenable
  groups the full and reduced C*-envelopes coincide in the generalized
  `L(G,A;P)` setting;
- physical p. 14 / printed p. 204: amenability (`mittelbar`) is defined by a
  positive normalized left-invariant functional on bounded continuous
  functions; Satz 6 says that if `G` is amenable, the reduced C*-envelope
  attached to every maximal representation of the coefficient algebra is
  canonically isomorphic to the full C*-envelope.

This is the original result cited by Austad Proposition 2.4. Because Leptin's
generalized-algebra setup includes measurable unitary factor systems, Leptin
does not independently own Paper 13's continuous gauge domain or signs.

### 3.4 `SRC-HUL64` and `SRC-HUL66`: amenability/weak containment

- `SRC-HUL64`, physical p. 11 scan / printed pp. 56--57: Theorem 5.4 gives
  the regular-norm equality for nonnegative `L1` functions in class `(R)`;
  Section 6's Main Theorem says that a locally compact group in `(R)` admits
  a left-invariant Banach mean on `L_infinity(G)`;
- `SRC-HUL64`, physical p. 12 scan / printed p. 58: the proof closes, and the
  discrete corollary states the equivalence between `(R)` and a
  left-invariant Banach mean; the paper credits the reverse locally compact
  direction to earlier work rather than claiming both directions as new;
- `SRC-HUL66`, physical p. 1 scan / printed p. 87 and physical p. 2 scan /
  printed p. 88: the introduction compares the regular, Følner, and
  invariant-mean classes and states that the invariant-mean class contains
  Abelian and compact groups.

Bibliographic anomaly: the current IMPAN record and DOI register
`27--59`, but the exact downloadable article scan visibly begins at printed
p. 37 and ends at printed p. 59; its physical p. 1 right-hand page is 37.
Physical/printed evidence locators above follow the retained scan. The DOI
and official registered pagination are recorded without silently converting
one into the other.

### 3.5 `SRC-KLEP65`: Borel-only background

- physical p. 14 / printed p. 11, introduction: multiplier classification
  is the projective-representation problem; the commutator is described as a
  continuous bicharacter and symmetric multipliers as trivial in Kleppner's
  Borel similarity relation;
- physical p. 31 / printed p. 28, Section 7: a multiplier is explicitly a
  **Borel** `omega:GxG->T` satisfying normalization and the cocycle identity;
  similarity explicitly uses a **Borel** `rho:G->T`;
- physical p. 32 / printed p. 29, Lemmas 7.1--7.2: the commutator becomes a
  continuous alternating bicharacter and symmetry is equivalent to Borel
  triviality;
- physical p. 36 / printed p. 33, Theorem 7.1: under its locally compact
  Abelian hypotheses, including the case where `x |-> x^2` is an
  automorphism, every Borel multiplier is similar to a bicharacter.

For `R`, the squaring map in Kleppner's multiplicative notation corresponds
to the additive doubling automorphism. This is useful Borel background, but
the source does not supply a continuous trivializing cochain in Paper 13's
frozen complex.

## 4. Sorkin sentinel: official abstract only, no retained PDF

| ID | Official metadata/access | Evidence ceiling |
|---|---|---|
| `SENT-SORKIN78` | Rafael Sorkin, “The triviality of continuous multipliers for the real line,” *International Journal of Theoretical Physics* **17** (1978), 369--376, DOI `10.1007/BF00674107`; official [Springer record](https://link.springer.com/article/10.1007/BF00674107). The record is subscription-only and no lawful author/repository full text was located in the bounded check. | `CONTINUOUS/CONTINUOUS` at title/official-abstract level only. The abstract says that every continuous group multiplier on `R` can be reduced to the identity by continuous remultiplication. It establishes an exact prior-art sentinel and the novelty ceiling, but owns no normalization, quotient orientation, sign, proof step, or physical-page locator. P13-3 remains author-owned and direct-proof mandatory. |

Access status is `UNAVAILABLE_FULLTEXT / NON_EVIDENCE_FOR_SIGNS`. No surrogate
HTML-to-PDF file was manufactured. The absent full text is not an open
claim blocker because no Paper-13 mathematical step is permitted to depend
on it.

## 5. Exact prior-paper framework reuse

The following Paper-11 bytes were rehashed in place and not copied:

| ID | Existing manifestation and receipts | Closed tier/access detail | Exact locator / Paper-13 ceiling |
|---|---|---|---|
| `REUSE-TU04` | `papers/11-indiscrete-convolution/notes/sources/fw-tu-nonhausdorff-groupoids-2004.pdf`; PDF `ff88e322eee65d2d6dd083697c82febb3759268f9b36083264a3e20b6e586897`; preflight `e82c95d4c3fd668d43c324db0631216372cc67505234a73e2ddc9ebf875884af`, `PASS`, `34=34=34`, no warnings | `MIXED`: cocycle/gauge regularity N/A; exact official full text reused in place | physical p. 3 / printed p. 567, Definition 1.1: Tu's local compactness requires a compact neighborhood and therefore local Hausdorffness; physical p. 17 / printed p. 581, Section 4.1: `C_c` is the Hausdorff-open zero-extension span, not necessarily globally continuous; physical p. 19 / printed p. 583, Definition 4.6: Haar-system domain. Hypothesis exclusion only. |
| `REUSE-BHM18-v2` | `papers/11-indiscrete-convolution/notes/sources/fw-buss-holkar-meyer-universal-property-v2.pdf`; PDF `8be7896ed1aab1138b8ccf067ebfbba0f8b7d8a1dc8713fbf6c2f173ffe647e6`; preflight `c288efb2dca89ca8fd47bd9371decb7d042853dd6b60b35897df2f70214bfb59`, `PASS`, `30=30=30`, no warnings | `MIXED`: cocycle/gauge regularity N/A; exact author full text reused in place | physical pp. 1--2: universal property for a locally compact Hausdorff groupoid with Haar system; the authors explicitly state that the construction as written works only for Hausdorff groupoids. Standard Hausdorff-framework boundary only. |

The reused Paper-11 source manifest is
`framework_source_manifest.md`, SHA-256
`b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f`.

## 6. Companion-byte and locator crosswalk

All registered companion bytes independently match the active protocol:

| Companion | Rehashed bytes | Exact Paper-13 premise locator and ceiling |
|---|---|---|
| Paper 9 | manuscript `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb`; PDF `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` | `cor:packet`, manuscript lines 409--415: fixed-prime packet is indiscrete and has at least two points; `cor:orbit`, lines 421--427: inherited orbits are nontrivial indiscrete and their set stabilizer/primitive logarithmic clock is `p^Z`/`log p`. No twist, standard topology, cohomology, or convolution credit. |
| Paper 11 | manuscript `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002`; PDF `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d`; proof audit `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | `thm:qc`, lines 359--376: actual quasi-compact support projection criterion; `thm:phi`, lines 465--484: exact time-function/support identity; `thm:star-algebra`, `thm:regular`, and `thm:completions`, lines 519--711: untwisted product/star, exact source-fibre regular kernel, and author transported completions. Untwisted baseline only; Paper 13 must reprove every twisted identity and no standard actual-groupoid completion follows. |
| Paper 12 | manuscript `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163`; PDF `3fda5ae01fd3b7a78ddbefb11a62befa4d2ab50906b112b39e3c48e89901a294`; proof audit `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | `thm:factorization`, lines 436--464: all-degree `T0` time factorization; `def:std` and `thm:std-topology`, lines 638--725: same-carrier orbitwise coproduct standardization and continuous identity direction `Std(X)->X_indisc`; `cor:packet-comparison`, lines 1054--1088: fixed-prime standardization on bare `Q_p`. No actual quotient topology, orbit count, measure, or twist is imported. |

Paper-12 downstream receipts also rehash exactly as registered: citation audit
`f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf`,
peer review
`e1f1558e170831457685a4a5c8c4d77f061b405d6c499867b6ce4f91bea6dc2b`,
and release audit
`53403b3ea8c44f30b6941653e2809432ad0e6b99f5cf983f0d929aa9d5c2760d`.

## 7. Release boundary

Public prose and bibliography may cite canonical DOI, publisher, arXiv, or
official-library endpoints. Local filenames, checksums, and sidecars are
internal reproducibility locators, not scholarly identifiers. Before any
future public synchronization, a payload audit must demonstrate that no
`papers/13-circle-twists/notes/sources/*.pdf` is included. Downloadability,
open-access labelling, or a source-side licence is not treated as a project
decision to redistribute the exact retained bytes.
