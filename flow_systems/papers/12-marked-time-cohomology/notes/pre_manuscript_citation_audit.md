# Paper 12 pre-manuscript citation and source-integrity audit

Audit date and source cutoff: **2026-08-15 (Asia/Shanghai)**  
Audit scope: final v4 manuscript citation inputs, exact manifestations,
technical locators, claim ownership, internal companion identities, and the
later public-sync source-PDF gate  
Audited composition blueprint SHA-256:
`b343dd47d4a4e2fc7b8570c33eb3270542732a4062142b1ef79530393000e107`
(898 lines)

The earlier blueprint digest
`26f78ea680bab507069b2cf992801c9c9891755885ae406b53258247db62b632`
is superseded and must not be used downstream.  The final digest above was
recomputed after the Route-A and Route-B evaluator-skill receipt rows were
added, and the resulting 898-line file was read in full.

## 1. Decision

```text
PRE_MANUSCRIPT_CITATION_AUDIT=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
BLUEPRINT_IDENTITY=PASS_FINAL_B343DD47_ONLY
RETAINED_SOURCE_CHECKSUMS=PASS_10_OF_10
RETAINED_PDF_PREFLIGHTS=PASS_5_OF_5
MINIMUM_BIBLIOGRAPHY_RECORDS=14
MANUSCRIPT_CITATION_INPUT_READY=true
PUBLIC_RELEASE_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

The final blueprint's source plan is accurate at its stated ceilings.  The
pre-manuscript citation gate is open, subject to using the exact 14-record
minimum tuple and the locator/owner restrictions below.  This is not a
bibliography audit of a later `.bib` file, a venue-policy decision, a
declaration pass, a manuscript-quality pass, or a release pass.

Two later release conditions remain deliberately open:

1. Papers 9--11 presently have exact internal identities but no frozen
   immutable public records.  Before standalone public release, every
   load-bearing companion dependency must either resolve to an honest
   immutable public record for the audited bytes or be restated
   self-containedly in Paper 12.
2. This filesystem snapshot has no Git metadata.  The zero-source-PDF Git,
   staged-payload, archive, attachment, and fresh-clone checks in Section 9
   therefore remain mandatory release gates rather than current findings.

No source, proof, Route, blueprint, manuscript, bibliography, lock, control,
or retained PDF was changed by this audit.

## 2. Exact evidence binding

The citation decision binds the following current bytes:

| Artifact | SHA-256 | Audit use |
|---|---|---|
| `notes/composition_blueprint.md` | `b343dd47d4a4e2fc7b8570c33eb3270542732a4062142b1ef79530393000e107` | final manuscript structure, owner matrix, and citation plan |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` | retained manifestations, licences, locators, and preflights |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` | executable five-PDF/five-sidecar ledger |
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` | author-complex and cohomology-comparator domains |
| `notes/phase3_v4_source_novelty_audit.md` | `cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22` | nearest v4 sources and bounded-search ceiling |
| `notes/proof_audit.md` | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | final theorem/owner/claim boundary |
| `notes/route_audit.md` | `2baf2b1ea63e5573f4b2673da6329520163ec67d76b002cb6f84fcf45c0ac102` | eight-owner Route result; no source substitution |

Any later change to the blueprint, source manifest, proof owner matrix, or a
cited manifestation invalidates this pass until a versioned re-audit binds
the replacement bytes.

## 3. Retained manifestation and preflight integrity

Running `sha256sum -c coh-sources.sha256` from `notes/sources` returned `OK`
for all five retained PDFs and all five JSON sidecars.  Each sidecar has
schema `pdf_read_preflight/1`, tool version `pdf_read_preflight/1.0.0`,
verdict `PASS`, equal declared/enumerated/reader page counts, and an empty
warnings list.

| ID | Exact retained manifestation | PDF SHA-256 | Pages | Sidecar SHA-256 | Result |
|---|---|---|---:|---|---|
| `COH-DEN-v4` | Deninger, arXiv `1807.06400v4`, 7 February 2024 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `119=119=119` | `84e43728af040d539a46fbbb95ff8cd34f46c75c0245130ef79c2978ccc3806d` | `PASS`, warnings 0 |
| `COH-MACK-1978` | Mackenzie, final Cambridge publisher PDF | `b94ed23e24a13047037dbffc5c84513df1cd8931c4391670e05c1f5904f66f83` | `25=25=25` | `8716b0e77a254642f1aae2a9dd75e84e30722711548abb26fa7335a59a0692c2` | `PASS`, warnings 0 |
| `COH-BUW-2023` | Blanco--Uribe--Waldorf, final EMS paginated PDF | `3d46127491c66f3ec0568fccb8df60b9e4465c4f4719b712fc3e23ca48f9e143` | `52=52=52` | `ae2272eed854f175d2d5bec4c624806c826bf9f364d2f4c27e230ede38ea6e42` | `PASS`, warnings 0 |
| `COH-FHKP-2022` | Farsi--Huang--Kumjian--Packer, final Cambridge PDF | `194583c289d3c08463a32221a8e6561292d48d5357021db370237c71de697083` | `32=32=32` | `908dea03b5b4523764249a6749e50ae696c0f342a21fe5522c22c1b962a0cb3b` | `PASS`, warnings 0 |
| `COH-FW-v2` | Fuchssteiner--Wockel, arXiv `1110.2977v2`, 12 April 2012 | `194483f7c90cb752b95f86b2557572bb8deb135032b749503347d7592d752f42` | `13=13=13` | `20303cd7044682edf01aaad44ba2cfd8f90c8694cc8e4eb61241f1640d625acc` | `PASS`, warnings 0 |

No additional publisher PDF was retained for the v4 audit.  Stacks, the two
Encyclopedia of Mathematics entries, and the official publisher or
institutional manifestations for Gepner--Meier, Guillou--May, and
Alp--Wensley were inspected at their exact locators without adding local
PDFs.  Local hashes above are reproducibility locators, not scholarly
identifiers and not evidence of redistribution permission.

Manifestation-level retention remains stricter than licence availability:
the BUW and FHKP final PDFs state CC BY 4.0, while no reuse licence is inferred
for the retained Deninger/Fuchssteiner--Wockel arXiv bytes or the Mackenzie
publisher bytes.  All five are nevertheless excluded from the public payload
under one uniform project rule.

## 4. Exact minimum bibliography tuple

The frozen blueprint requires the following **14 records**.  The suggested
keys are stable internal keys; a selected venue may rename keys but may not
change record identity, manifestation, or status.  DOI values should be
stored as bare DOI strings, not as a second invented identifier.  Page and
proposition locators belong in the citing sentence or note, not only in the
bibliography.

### 4.1 External records: eleven

| Suggested key / type | Exact minimum bibliographic fields | Canonical manifestation rule |
|---|---|---|
| `Deninger2026Dynamical` / `@article` | Christopher Deninger; “Dynamical systems for arithmetic schemes”; *Indagationes Mathematicae* **37**(1) (2026), 25--136; DOI `10.1016/j.indag.2024.05.007`; arXiv `1807.06400`, version 4, primary class `math.DS` | Keep both the published DOI identity and `https://arxiv.org/abs/1807.06400v4`; every technical page locator in Paper 12 is explicitly to arXiv v4, not an assumed publisher-page crosswalk. |
| `Stacks0B1W` / `@misc` | The Stacks Project Authors; “The Stacks Project, Section 5.29 (Tag 0B1W): Topological colimits”; Tag `0B1W`; URL `https://stacks.math.columbia.edu/tag/0B1W`; accessed 2026-08-15 | Do not manufacture a journal, volume, page range, DOI, or publication year. |
| `EoMTopologicalGroup` / `@misc` | *Encyclopedia of Mathematics*; “Topological group”; URL `https://encyclopediaofmath.org/wiki/Topological_group`; accessed 2026-08-15 | Corporate/reference-work identity; do not infer an individual page author or DOI. |
| `EoMHomogeneousSpace` / `@misc` | *Encyclopedia of Mathematics*; “Homogeneous space”; URL `https://encyclopediaofmath.org/wiki/Homogeneous_space`; accessed 2026-08-15 | Corporate/reference-work identity; do not infer an individual page author or DOI. |
| `GepnerMeier2023` / `@article` | David Gepner and Lennart Meier; “On equivariant topological modular forms”; *Compositio Mathematica* **159**(12) (2023), 2638--2693; DOI `10.1112/S0010437X23007509` | Cite the DOI/Cambridge final article; use Proposition 2.15 at printed p. 2647. |
| `GuillouMay2017` / `@article` | Bertrand J. Guillou and J. Peter May; “Equivariant iterated loop space theory and permutative G-categories”; *Algebraic & Geometric Topology* **17**(6) (2017), 3259--3339; DOI `10.2140/agt.2017.17.3259` | Cite the DOI/MSP final article; use Proposition 5.19 at printed p. 3311. |
| `AlpWensley2010` / `@article` | Murat Alp and Christopher D. Wensley; “Automorphisms and homotopies of groupoids and crossed modules”; *Applied Categorical Structures* **18**(5) (2010), 473--504; DOI `10.1007/s10485-008-9183-y` | The DOI/published record controls metadata; use Section 3.1 at published p. 481.  The Bangor institutional record is a manifestation aid, not a second scholarly identity. |
| `Mackenzie1978` / `@article` | K. A. Mackenzie; “Rigid cohomology of topological groupoids”; *Journal of the Australian Mathematical Society* (Series A) **26**(3) (1978), 277--301; DOI `10.1017/S1446788700011794` | Cite the DOI/Cambridge final article; use Theorem 3 at printed pp. 298--299. |
| `BlancoUribeWaldorf2023` / `@article` | Jaider Blanco, Bernardo Uribe, and Konrad Waldorf; “Pontrjagin duality on multiplicative gerbes”; *Journal of Noncommutative Geometry* **17**(4) (2023), 1469--1520; DOI `10.4171/JNCG/528` | Cite the DOI/EMS final article; use Section 2.4 and Lemmas 2.3 and 2.5. |
| `FarsiHuangKumjianPacker2022` / `@article` | Carla Farsi, Leonard Huang, Alex Kumjian, and Judith Packer; “Cocycles on groupoids arising from `N^k`-actions”; *Ergodic Theory and Dynamical Systems* **42**(11) (2022), 3325--3356; DOI `10.1017/etds.2021.69` | Cite the DOI/Cambridge final article; use Definition 3.7 at printed p. 3336. |
| `FuchssteinerWockel2012` / `@article` | Martin Fuchssteiner and Christoph Wockel; “Topological Group Cohomology with Loop Contractible Coefficients”; *Topology and its Applications* **159**(10--11) (2012), 2627--2634; DOI `10.1016/j.topol.2012.04.006`; arXiv `1110.2977`, version 2 | Cite the published identity and `https://arxiv.org/abs/1110.2977v2`; technical locator is Corollary II.8 in arXiv v2, whose final-version crosswalk is recorded, without claiming publisher-byte identity. |

### 4.2 Internal companion records: three

Use `@unpublished` (or the selected style's exact unpublished-manuscript
equivalent) with only author, exact title, year, and an honest note such as
“Companion manuscript.”  Do **not** put the local path or SHA-256 into the
scholarly record, do not invent a DOI or acceptance status, and do not add a
mutable branch URL.

| Suggested key | Exact scholarly fields now | Internal audit binding; not a Bib field |
|---|---|---|
| `Wang2026PacketSeparation` | Liang Wang; “Indiscrete Prime Packets in Deninger's Rational-Witt Flow: Simultaneous Approximation and a Topological Corrigendum”; 2026; companion manuscript; no URL | Audited release PDF SHA-256 `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` |
| `Wang2026SeparatedReflections` | Liang Wang; “Separated Reflections and Observable Collapse of Indiscrete Arithmetic Prime Packets”; 2026; companion manuscript; no URL | Audited release PDF SHA-256 `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |
| `Wang2026ContinuousConvolution` | Liang Wang; “Continuous Convolution Collapse on Indiscrete Arithmetic Orbit Groupoids”; 2026; companion manuscript; no URL | Audited release PDF SHA-256 `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |

### 4.3 Exact 14-record BibTeX seed

This block is the mechanically consumable minimum tuple.  A venue-specific
style conversion may change formatting fields, but the identities, versions,
URLs, DOI strings, unpublished status, and absence of companion URLs are
frozen.

```bibtex
@article{Deninger2026Dynamical,
  author        = {Christopher Deninger},
  title         = {Dynamical systems for arithmetic schemes},
  journal       = {Indagationes Mathematicae},
  year          = {2026},
  volume        = {37},
  number        = {1},
  pages         = {25--136},
  doi           = {10.1016/j.indag.2024.05.007},
  eprint        = {1807.06400},
  archivePrefix = {arXiv},
  primaryClass  = {math.DS},
  url           = {https://arxiv.org/abs/1807.06400v4},
  note          = {Technical locators refer to arXiv version 4, 7 February 2024}
}

@misc{Stacks0B1W,
  author = {{The Stacks Project Authors}},
  title  = {The Stacks Project, Section 5.29 (Tag 0B1W): Topological colimits},
  url    = {https://stacks.math.columbia.edu/tag/0B1W},
  note   = {Tag 0B1W; accessed 15 August 2026}
}

@misc{EoMTopologicalGroup,
  author = {{Encyclopedia of Mathematics}},
  title  = {Topological group},
  url    = {https://encyclopediaofmath.org/wiki/Topological_group},
  note   = {Accessed 15 August 2026}
}

@misc{EoMHomogeneousSpace,
  author = {{Encyclopedia of Mathematics}},
  title  = {Homogeneous space},
  url    = {https://encyclopediaofmath.org/wiki/Homogeneous_space},
  note   = {Accessed 15 August 2026}
}

@article{GepnerMeier2023,
  author  = {David Gepner and Lennart Meier},
  title   = {On equivariant topological modular forms},
  journal = {Compositio Mathematica},
  year    = {2023},
  volume  = {159},
  number  = {12},
  pages   = {2638--2693},
  doi     = {10.1112/S0010437X23007509}
}

@article{GuillouMay2017,
  author  = {Bertrand J. Guillou and J. Peter May},
  title   = {Equivariant iterated loop space theory and permutative {G}-categories},
  journal = {Algebraic \& Geometric Topology},
  year    = {2017},
  volume  = {17},
  number  = {6},
  pages   = {3259--3339},
  doi     = {10.2140/agt.2017.17.3259}
}

@article{AlpWensley2010,
  author  = {Murat Alp and Christopher D. Wensley},
  title   = {Automorphisms and homotopies of groupoids and crossed modules},
  journal = {Applied Categorical Structures},
  year    = {2010},
  volume  = {18},
  number  = {5},
  pages   = {473--504},
  doi     = {10.1007/s10485-008-9183-y}
}

@article{Mackenzie1978,
  author  = {K. A. Mackenzie},
  title   = {Rigid cohomology of topological groupoids},
  journal = {Journal of the Australian Mathematical Society. Series A},
  year    = {1978},
  volume  = {26},
  number  = {3},
  pages   = {277--301},
  doi     = {10.1017/S1446788700011794}
}

@article{BlancoUribeWaldorf2023,
  author  = {Jaider Blanco and Bernardo Uribe and Konrad Waldorf},
  title   = {Pontrjagin duality on multiplicative gerbes},
  journal = {Journal of Noncommutative Geometry},
  year    = {2023},
  volume  = {17},
  number  = {4},
  pages   = {1469--1520},
  doi     = {10.4171/JNCG/528}
}

@article{FarsiHuangKumjianPacker2022,
  author  = {Carla Farsi and Leonard Huang and Alex Kumjian and Judith Packer},
  title   = {Cocycles on groupoids arising from {$\mathbb{N}^k$}-actions},
  journal = {Ergodic Theory and Dynamical Systems},
  year    = {2022},
  volume  = {42},
  number  = {11},
  pages   = {3325--3356},
  doi     = {10.1017/etds.2021.69}
}

@article{FuchssteinerWockel2012,
  author        = {Martin Fuchssteiner and Christoph Wockel},
  title         = {Topological Group Cohomology with Loop Contractible Coefficients},
  journal       = {Topology and its Applications},
  year          = {2012},
  volume        = {159},
  number        = {10--11},
  pages         = {2627--2634},
  doi           = {10.1016/j.topol.2012.04.006},
  eprint        = {1110.2977},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/1110.2977v2},
  note          = {Technical locator refers to arXiv version 2, 12 April 2012}
}

@unpublished{Wang2026PacketSeparation,
  author = {Liang Wang},
  title  = {Indiscrete Prime Packets in Deninger's Rational-Witt Flow: Simultaneous Approximation and a Topological Corrigendum},
  year   = {2026},
  note   = {Companion manuscript, 14 August 2026}
}

@unpublished{Wang2026SeparatedReflections,
  author = {Liang Wang},
  title  = {Separated Reflections and Observable Collapse of Indiscrete Arithmetic Prime Packets},
  year   = {2026},
  note   = {Companion manuscript, 14 August 2026}
}

@unpublished{Wang2026ContinuousConvolution,
  author = {Liang Wang},
  title  = {Continuous Convolution Collapse on Indiscrete Arithmetic Orbit Groupoids},
  year   = {2026},
  note   = {Companion manuscript, 15 August 2026}
}
```

No separate bibliography record is required for the continuous Cauchy step,
compactness of `R/LZ`, the direct v4 topology/automorphism/cohomology proofs,
or the finite deterministic controls.  Adding a generic textbook merely to
decorate these direct arguments would not strengthen claim verification.

The 14-record tuple is minimum for the frozen blueprint, not permission for
orphan references: every record must be cited at the placement below, and a
later bibliography audit must still require zero unresolved citations and
zero uncited entries.

## 5. Technical manifestations, exact locators, and claim ceilings

### 5.1 Source-owned packet facts

**Deninger.**  The controlling technical manifestation is arXiv
`1807.06400v4`, not an unverified publisher-page crosswalk.

- Physical/author p. 38, Section 6 defines the suspension packet setting,
  the right multiplicative action, and the additive normalization
  `phi^t([P,u])=[P,u e^t]`.
- Physical/author p. 39, Theorem 6.1 states that every point of the packet
  attached to `x_0` has multiplicative isotropy `N(x_0)^Z` and records orbit
  length `log N(x_0)`.  For the exact fixed-prime rational-Witt packet with
  `N(x_0)=p`, logarithmic time therefore gives the common additive stabilizer
  `(log p)Z` at every unit.
- Equations (38)--(39) and the surrounding set parametrizations are only set
  statements.  They do not transport a topology.

Claim ceiling: Deninger owns the packet, right action, every-unit stabilizer,
and logarithmic clock.  Deninger does not own Paper 9's actual inherited
topology, the Paper-11/12 action groupoid, `C_cnv/H_cnv`, orbitwise
standardization, standardized cohomology, or the invariant diagonal.

### 5.2 Standard quotient and coproduct background

**Stacks Project, Tag `0B1W`.**  Section 5.29 and Lemma 5.29.1 verify the
arbitrary set-indexed coproduct topology and the componentwise universal
continuity property.  This supports assembling the open orbit components.
It proves no action continuity, same-carrier uniqueness, common-lattice
theorem, cohomology, automorphism extension, or packet application.

**Encyclopedia of Mathematics.**  “Topological group” and “Homogeneous
space” verify the canonical quotient topology on `G/H`, the transitive
orbit/stabilizer description, Hausdorffness when `H` is closed, and the
`R/Z` circle model.  For `H=LZ`, `L>0`, Paper 12 should prove compactness
directly as the continuous image of `[0,L]`; that direct compact-to-Hausdorff
argument is what powers the uniqueness theorem.  Neither EoM entry compares
the constructed standard topology with the actual indiscrete topology.

Claim ceiling for all three web records: routine component background only.
They are not evidence that `Std_coprod`, `Indisc`, their strict equivalence,
or the same-carrier comparison is source-owned.

### 5.3 Strict action-groupoid lift/descent comparator

**Gepner--Meier.**  In the final Cambridge article, printed p. 2643 defines
`Top` to mean compactly generated weak-Hausdorff spaces.  Proposition 2.15 at
printed p. 2647 states the full faithfulness of the action-groupoid functor
from `G`-spaces to topological groupoids over `B G`: the object map is forced
to be equivariant and the arrow map retains the `G` coordinate.

Claim ceiling: this is the nearest formal over-`B R` mechanism for strict
time-preserving maps.  A nontrivial globally indiscrete actual unit space is
not weak Hausdorff, so Proposition 2.15 cannot be imported to the actual
owner.  It does not construct the orbitwise topology, global
indiscretization, the common-`H` equivalence, automorphisms, cohomology, or
`J`.  Paper 12 must retain its direct exact-category proof.

### 5.4 Finite wreath precedents

**Guillou--May.**  Proposition 5.19 at printed p. 3311 treats finite groups
and finite `G`-sets.  It decomposes a finite `G`-set by orbit type and gives
the wreath-product automorphism group for `k` copies of `G/H`; the following
skeletal passage uses chosen isomorphisms.

Claim ceiling: finite `G`, finite `G`-set, and finite `k` only.  It does not
cover the topological group `R`, arbitrary `Q`, the full product
`(R/H)^Q`, a canonical split, the actual indiscrete topology, or cohomology.

**Alp--Wensley.**  Section 3.1 at published p. 481 states the wreath-product
automorphism mechanism for a disjoint union of `m` isomorphic connected
groupoids; the article's setting and displayed result use finite groupoids
and finite `m`.

Claim ceiling: finite-copy algebraic groupoids only.  It proves no arbitrary
set-indexed topological coproduct theorem, no continuity, no maps over
`B R`, no choice accounting for arbitrary `Q`, and no cohomological
invariant statement.

Together these records require the manuscript wording:

```text
1 -> (R/H)^Q -> Aut_R(G_std) -> Sym(Q) -> 1
```

is canonical, while surjectivity uses ZFC choice and any split/wreath
coordinates are noncanonical.  The kernel is the full Cartesian product,
not a direct sum, and the arbitrary-`Q` result remains Paper 12's direct
proof.

### 5.5 Transitive and continuous-cohomology comparators

**Mackenzie.**  The retained final PDF independently verifies the strict
domain at printed pp. 277--280 and Theorem 3 at physical pp. 22--23 / printed
pp. 298--299.  Under Mackenzie's locally trivial, locally compact,
Hausdorff/transitive setting with the specified manifold base and continuous
locally convex vector-bundle module, Theorem 3 identifies his derived rigid
cohomology with continuous cohomology of a vertex group.

Claim ceiling: a different rigid cohomology theory and a transitive
vertex-group comparator only.  It is not `H_cnv`, does not cover the actual
non-Hausdorff owner or a nontransitive coproduct as one groupoid, and proves
neither `H_std^1=R^Q` nor the map or invariant image of `J^*`.

**Blanco--Uribe--Waldorf.**  Printed p. 1472 fixes `Topab` as compactly
generated, locally contractible, Hausdorff topological abelian groups.
Printed pp. 1473--1475, Section 2.4 and Lemmas 2.3 and 2.5, give the full
continuous one-object nerve convention, a conditional comparison under the
stated simplicial-paracompact/coefficient hypotheses, and
`H^1` as continuous homomorphisms in the matched one-object case.

Claim ceiling: exact `(R,R)` one-object and conditional simplicial-space
comparator only.  It does not rename or establish the full generic
Paper-12 groupoid complex for arbitrary `T0` coefficients.

**Farsi--Huang--Kumjian--Packer.**  Definition 3.7 at physical p. 12 /
printed p. 3336 defines continuous `H`-valued groupoid 1-cocycles,
coboundaries, and degree-one continuous groupoid cohomology for a locally
compact abelian coefficient group.  Real coefficients match that degree-one
terminology.  Their coboundary representative is
`f(r gamma)-f(s gamma)`, opposite to Paper 12's frozen representative sign;
the image subgroup is unchanged under `f -> -f`.

Claim ceiling: degree one and terminology only.  No all-degree complex,
arbitrary-`T0` coefficient theorem, marked isotropy image, or period theorem
is imported.

**Fuchssteiner--Wockel.**  ArXiv `1110.2977v2`, author pp. 2--3, defines the
one-object continuous homogeneous/standard group cochain setting;
Corollary II.8 at author p. 7 compares continuous and locally continuous
cohomology for loop-contractible coefficients.

Claim ceiling: one-object topological-group comparator for real
loop-contractible coefficients only.  It is not the Paper-12 non-Hausdorff
action-groupoid complex and supplies no standardized component product or
comparison theorem.

**Continuous Cauchy step.**  No additional source is necessary.  The
manuscript must give the elementary direct proof that a continuous additive
`f:R->R` satisfies `f(q)=q f(1)` on the rationals and hence
`f(t)=t f(1)` by rational approximation and continuity.  Do not make a
separate source appear to own `Z_actual^1=Rc`, `B_actual^1=0`, or the marked
class.

## 6. Exact v4 claim-owner deployment

| Frozen claim | Citations that must accompany it | Exact owner and citation ceiling |
|---|---|---|
| `P12-1` finite nerve charts and `P12-3` all-degree time factorization | Paper 11 at first predecessor comparison | Paper 12 owns every finite degree and the `T0` theorem.  Paper 11 supplies only the range-first arrow-degree/time-factorization context. |
| `P12-2` author differential and `P12-4` actual real `H^1` | BUW, Farsi et al., and FW; Mackenzie only if the convention/comparator paragraph is retained | These are convention or strict-domain comparators.  The manuscript must say “author-defined globally continuous unnormalized nerve cohomology,” keep the direct Cauchy proof, and claim no standard named theory. |
| `P12-5` representative-independent `Per_x` | Farsi et al. for degree-one cocycle/isotropy terminology | Paper 12 owns coboundary descent and the marked image.  Arbitrary images need not be lattices. |
| `P12-6` every-unit fixed-prime `(log p)Z` | Deninger arXiv v4 pp. 38--39/Thm. 6.1 and Paper 9 | Deninger owns action/clock/common stabilizer; Paper 9 owns actual packet topology; Paper 12 owns the groupoid/cohomological recovery.  State `PACKET_COROLLARY` and `ORBIT_ONLY=false`. |
| `P12-7` strict/scaled/unmarked boundary | no external theorem; cite Paper 10 only for separated-reflection context where used | Paper 12 owns the categories and proofs.  State strict preservation, positive scaled covariance, and existential non-descent, not universal loss. |
| `P12-8a` pointed standard quotient and one-sided continuity | EoM quotient entries and Paper 10 context | A deliberately lossy standard proxy.  It is not the actual orbit topology or a reflection; only standard-to-actual continuity is available. |
| `P12-8b` section-free common-`H=LZ` standardization and strict equivalence | Stacks Tag `0B1W`, both EoM entries, Gepner--Meier Prop. 2.15 | Paper 12 owns the same-set construction, uniqueness, full faithfulness, and global `Indisc`.  Citations provide component background or a CGWH analogy only. |
| `P12-8c` automorphism exact sequence | Guillou--May Prop. 5.19 and Alp--Wensley Section 3.1 | Paper 12 owns arbitrary nonempty `Q`, full product kernel, choice accounting, and the canonical extension.  Never call the split canonical. |
| `P12-8d` `H_std^1=R^Q`, nonzero `B_std^1`, and invariant diagonal | Mackenzie Thm. 3 as a different-theory comparator; BUW/Farsi/FW for the convention boundaries already stated | Paper 12 owns the full algebraic product, `J^*`, and strict-automorphism invariants.  Degree one only; no topology on `R^Q` or cohomology. |
| `P12-8e` fixed-prime four-way application | Deninger and Paper 9; Papers 10--11 only at their separate contextual ceilings | Keep `Gamma_p^actual`, `Gamma_p^std`, `Q_p^actual`, and `Q_p^disc` distinct.  `Q_p` is a bare nonempty set; no count, enumeration, measure, local triviality, or topology transfer. |
| `P12-9` controls and `P12-10` Route result | internal manifest/Route records, not scholarly source substitution | Finite controls are witnesses/falsifiers only.  Six Route-A exploratory records and two rejected controls, all A2--A4 failures, and no Route B give no determinant, operator, or spectral evidence. |

The exact comparison direction must remain

```text
J:G_std -> G_actual,
J^*:H_cnv^1(G_actual;R) -> H_cnv^1(G_std;R).
```

Under the slope identification, `J^*` has the constant diagonal as its image,
and only strict time-preserving equivariant automorphisms define the invariant
subspace.  Raw pullback uses `lambda o sigma`; only the declared left action
uses `lambda o sigma^{-1}`.

## 7. Papers 9--11 internal identity and public-status conditions

The current internal identities were independently rehashed.  Dates below
are the manuscript dates, not publication or acceptance dates.

| Companion | Exact local identity tuple | Licensed dependency in Paper 12 | Forbidden promotion |
|---|---|---|---|
| Paper 9 | Liang Wang; exact title in Section 4.2; dated 14 August 2026; TeX SHA `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb`; PDF SHA `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`; Bib SHA `0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35`; proof-audit SHA `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8`; source-audit SHA `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | actual fixed-orbit and entire fixed-prime packet topology; actual quotient context | no standard-circle, standardization, Paper-12 cohomology, orbit count, or arithmetic selection credit |
| Paper 10 | Liang Wang; exact title in Section 4.2; dated 14 August 2026; TeX SHA `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315`; PDF SHA `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4`; Bib SHA `201e997ad953ebc1f27bd4c068400be656a1b9b6fbc4a231443ad8c2770e98b1`; proof-audit SHA `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | separated-reflection context and actual/standard topology-direction warning only | no credit for `Std_coprod`, its uniqueness/equivalence, `H_std^1`, or the diagonal |
| Paper 11 | Liang Wang; exact title in Section 4.2; dated 15 August 2026; TeX SHA `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002`; PDF SHA `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d`; Bib SHA `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877`; proof-audit SHA `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28`; composition SHA `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | range-first action groupoid, arrow-level time factorization, and convolution-collapse context only | no Paper-11 completion, all-degree, standardized-`H^1`, standardization, or invariant-diagonal credit |

As of the audit cutoff, no immutable public URL, DOI, repository release,
archive identifier, journal status, or acceptance status is frozen for any of
these three records.  The draft bibliography must therefore remain
`@unpublished`/companion-manuscript metadata with no URL.

After a real public sync, a companion entry may acquire a URL only when all
of the following hold:

1. the endpoint is immutable (for example, an actual archive DOI, repository
   release/tag with immutable object identity, or content-addressed record),
   not a mutable default-branch or working-tree URL;
2. the deposited artifact is the exact cited version, with its digest
   checked against the internal identity above or an explicitly versioned
   successor reviewed in a new audit;
3. the title, author, year, version/status wording, and any licence statement
   agree with the public record; and
4. the bibliography uses the public scholarly identity while the local hash
   remains only in the audit/release ledger.

If those conditions are not met by standalone release, Paper 12 must restate
all load-bearing dependencies self-containedly.  A companion citation may
still be retained as context, but it cannot be the sole public support for an
unavailable theorem premise.

## 8. Claim-language and novelty firewall

The only permitted negative-search status is dated and bounded:

```text
SUPPORTED_WITHIN_SEARCH through 2026-08-15
```

If a novelty sentence is retained, it may say that the bounded search did
not identify a direct same-domain precedent for the exact conjunction.  It
may not say “first,” “novel,” “unprecedented,” “no precedent exists,” or
convert unavailable/non-exportable endpoints into zero results.

The manuscript must also preserve these source-sensitive ceilings:

- call `C_cnv/H_cnv` the Paper-12 author-defined globally continuous
  unnormalized nerve complex/algebraic cohomology, not unqualified
  topological-groupoid cohomology;
- credit `(log p)Z` to Deninger's `p^Z` plus logarithmic clock, while crediting
  Paper 12 only with marked cohomological recovery and Paper 9 with actual
  topology;
- call `R/H` a standard proxy or a component of the constructed topology,
  never the inherited actual orbit topology;
- call standardization an action-and-mark-dependent same-set
  retopologization, not a Hausdorff/Kolmogorov/completely regular reflection;
- call `R^Q` a full algebraic Cartesian product with no imposed topology,
  not `C(Q,R)`, a direct sum, bounded functions, or a topological product;
- state that standardized coboundaries are generally nonzero and that only
  cohomology classes, not all cocycles literally, admit time-only
  representatives;
- use only strict time-preserving equivariant automorphisms in the invariant
  theorem; and
- infer no higher standardized cohomology, trace, determinant, analytic
  continuation, quantization, completion, or operator lift.

## 9. Later Git and public-sync zero-source-PDF gate

The local source directory contains five intentionally retained internal
PDFs and the existing exclusion file is exactly:

```gitignore
*.pdf
!*.preflight.json
```

That rule is appropriate but is not, by itself, proof that no PDF is tracked,
staged, attached, archived, or embedded.  Git metadata is absent from the
current filesystem snapshot, so the following checks must be run at the real
repository root immediately before release.  Every command marked “zero”
must produce no matching path.

### 9.1 Index, staged delta, HEAD, and LFS

```bash
git ls-files | rg '^papers/.*/notes/sources/.*\.pdf$'                 # zero
git diff --cached --name-only --diff-filter=ACMR \
  | rg '^papers/.*/notes/sources/.*\.pdf$'                           # zero
git ls-tree -r --name-only HEAD \
  | rg '^papers/.*/notes/sources/.*\.pdf$'                           # zero
git lfs ls-files 2>/dev/null \
  | rg 'papers/.*/notes/sources/.*\.pdf$'                            # zero
```

The scope is every `papers/*/notes/sources/*.pdf`, not only the five Paper-12
filenames.  A cleared generated `paper/paper.pdf` is a project output and is
not matched by this source-PDF rule.

### 9.2 Exact proposed archive/payload

Build the actual release archive or enumerate the exact upload/staging list,
then inspect that artifact rather than inferring from `.gitignore`:

```bash
tar -tf RELEASE_ARCHIVE.tar \
  | rg '^papers/.*/notes/sources/.*\.pdf$'                           # zero
```

For a non-tar uploader, save its exact file manifest and apply the same
anchored pattern.  Fail closed if the platform adds unenumerated attachments.

### 9.3 Manuscript attachment and source-path scan

```bash
rg -n 'notes/sources|coh-[A-Za-z0-9_-]+\.pdf' \
  papers/12-marked-time-cohomology/paper \
  papers/12-marked-time-cohomology/supplement 2>/dev/null             # zero
pdfdetach -list papers/12-marked-time-cohomology/paper/paper.pdf      # no source attachment
```

The final PDF audit must also reject a visible or hidden local filesystem
path.  A citation to a canonical DOI/arXiv/authoritative URL is permitted;
an embedded retained source PDF is not.

### 9.4 Fresh-clone proof

Clone the exact release ref into a newly created temporary directory, with
no shared working-tree files, and require:

```bash
find FRESH_CLONE/papers -path '*/notes/sources/*.pdf' -type f -print     # zero
```

Then build from that clone and repeat the attachment/path checks.  Record the
release ref, commit, archive digest, command output, and fresh-clone result in
the later release audit.  Any matching source PDF makes the public-sync gate
fail, regardless of the underlying source's open-access status.

## 10. Handoff conditions

The manuscript lane may now consume this report and the final blueprint for
citation planning.  It must use the 14-record minimum tuple, place exact
locators at the supporting claims, preserve every domain and ownership
ceiling, and keep the companion records unpublished and URL-free until a
real immutable record exists.

Before publication, a later citation-integrity audit must inspect the actual
manuscript and `.bib` and require:

```text
UNRESOLVED_CITATIONS=0
ORPHAN_BIBLIOGRAPHY_ENTRIES=0
FABRICATED_IDENTIFIERS=0
LOCAL_PATHS_AS_SCHOLARLY_IDENTITIES=0
CLAIMS_ABOVE_SOURCE_CEILING=0
COMPANION_PUBLIC_STATUS_OVERSTATEMENTS=0
SOURCE_PDFS_IN_PUBLIC_PAYLOAD=0
```

Author/venue intake, declarations, current venue policy, bibliography style,
manuscript review, clean build, final PDF review, and release authorization
remain separate conjunctive gates.
