# Paper 12 Phase-2 framework and exact-owner source audit

Audit date: **2026-08-15**  
Search/source cutoff: **2026-08-15**  
Decision: **PASS — C0/M0/m0**  
Standalone source branch: **`PACKET_COROLLARY` feasible; `ORBIT_ONLY` not triggered**

## 1. Exact-byte authority and scope

This report is bound to the following unchanged status tuple:

| Authority | SHA-256 |
|---|---|
| `notes/phase1_final_gate.md` | `fc327245bf5653b18f21f782f4783a2ad0b606340c5f5e7da6516d0514cac72c` |
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` |
| `notes/pipeline_state.md` | `9a3c2dbf85a4f2f9a8ebe82a6b8ad82b79379bb7bd5245bbe03e9a39a2200e05` |

The audit used the ARS source-verification and PDF-preflight rules and only
primary or authoritative manifestations: publisher records/PDFs, arXiv
versioned records/PDFs, and an author publication list for the published
Fuchssteiner--Wockel crosswalk. It addresses framework conventions,
applicability, exact source ownership, the fixed-prime packet gate, and the
release/citation boundary. It does **not** prove any `P12-*` target, perform
the independent bounded exact-package novelty search, inspect another Paper-12
Phase-2 report, or authorize Phase 3, Route, manuscript, or release work.

## 2. Decision and finding register

The frozen protocol is source-feasible without amendment.

| Severity | Count | Open finding |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

The domain mismatches and naming ceilings below are not defects in the locked
design: the protocol already requires author-defined notation, direct proofs,
owner separation, and conditional use of named theories. They are mandatory
citation constraints for later phases.

## 3. Exact packet/common-stabilizer chain

### 3.1 Primary-source steps

The exact same-object chain closes:

1. Deninger, arXiv `1807.06400v4`, physical/printed p. 38, Section 6,
   defines

   ```text
   X_0 = Xcheck_0(C)^E x_(Q_{>0}) R_{>0},
   (P_0,u)q=(F_q(P_0),q^{-1}u),
   [P_0,u] . v=[P_0,uv],
   phi^t([P_0,u])=[P_0,u e^t],
   Gamma_{x_0}=C_{x_0} x_(Q_{>0}) R_{>0}.
   ```

   Thus the additive `+t` action in Paper 12 is the restriction of the same
   source right flow, with the same logarithmic normalization; it is not a
   refitted clock.

2. On physical/printed p. 39, Theorem 6.1 states that **for every point** of
   `Gamma^E_{x_0}` the multiplicative isotropy group is
   `N(x_0)^Z`, and describes `Gamma^E_{x_0}` as the packet corresponding to
   the finite-residue-field point `x_0`. The preceding p. 38 paragraph states
   that `Gamma^E_{x_0}=Gamma_{x_0}` whenever `E_f` is contained in `E`; taking
   the exact Paper-9 owner `E=E_f` therefore gives the full fixed-prime
   `Gamma_p`, not an orbitwise or larger-character surrogate.

3. For `X_0=Spec Z` and `x_0=(p)`, `N(x_0)=p`. The fixed-prime packet is
   therefore `Gamma_p`, and every one of its units has multiplicative
   stabilizer `p^Z`.

4. The source's own additive flow uses the exponential group isomorphism
   from additive `R` to multiplicative `R_{>0}`. Hence the preimage of `p^Z` is exactly
   `(log p)Z`. Every packet unit has additive stabilizer `(log p)Z` in the
   Paper-12 time coordinate.

This is the required every-unit statement, so the source gate selects
`PACKET_COROLLARY`, not `ORBIT_ONLY`. It establishes source feasibility only:
the representative-independent cohomological period statement remains a
Phase-3 proof obligation.

### 3.2 Ownership ceiling

Deninger owns the suspension set, fixed-prime packet, right flow, common
stabilizer, and logarithmic clock. Deninger's p. 38 description uses an
equivariant **bijection** to orbit circles; it does not supply the actual
inherited packet/orbit topology, a transformation groupoid, a nerve complex,
or a cohomology theory. No later citation may say “Deninger's groupoid” or
“Deninger's cohomology” for the Paper-11/Paper-12 constructions.

## 4. Separate Paper-9 and Paper-11 rebind

| Dependency | Frozen local evidence | Exact retained contribution | Forbidden promotion |
|---|---|---|---|
| Paper 9 source audit | `papers/9-packet-separation/notes/source_audit.md`, SHA-256 `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | Deninger locator/strength split; `Gamma_p`, `p^Z`, `log p`; no topology through Eqs. (38)--(39) | no Paper-9 groupoid/cohomology credit |
| Paper 9 proof audit | `papers/9-packet-separation/notes/proof_audit.md`, SHA-256 `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | Lemma 3.2 restricted quotient topology; Lemmas 6.1--6.2 packet exhaustion/equality; Corollaries 7.2--7.3 actual packet and every inherited orbit indiscrete | no ordinary-circle topology and no Deninger topology credit |
| Paper 11 proof audit | `papers/11-indiscrete-convolution/notes/proof_audit.md`, SHA-256 `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | range-first `X rtimes R`, product arrow topology, continuous groupoid maps, every arrow open `X x U`, and `T0`-target time factorization (`P11-1`--`P11-2`) | no all-degree nerve or Paper-12 cohomology credit |
| Paper 11 composition blueprint | `papers/11-indiscrete-convolution/notes/composition_blueprint.md`, SHA-256 `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | citation/owner ceiling and exact range-first convention | no new proof theorem |

The chain is intentionally non-spliced:

```text
Deninger packet/action/common stabilizer/clock
  + Paper 9 actual inherited unit topology
  + Paper 11 generic arrow groupoid and n=1 factorization
  -> Paper 12 may define G_p^pkt and attempt its new all-degree results.
```

## 5. Framework and convention audit

### 5.1 Source/domain matrix

| Source and exact locator | Source-owned content | Match available to Paper 12 | Ceiling on use |
|---|---|---|---|
| Mackenzie (1978), printed p. 277 / physical p. 1; Defs. 1.3--1.4, printed p. 279 / physical p. 3 | rigid cohomology for Hausdorff, transitive, locally trivial, locally compact topological groupoids | historical topological-groupoid/module comparator | the nontrivial indiscrete Paper-12 unit and arrow spaces fail the Hausdorff/local-trivial framework |
| Mackenzie Def. 2.1, printed p. 280 / physical p. 4; Def. 3.1, p. 282 / physical p. 6; p. 285 / physical p. 9 | locally convex continuous vector bundles/modules; the product bundle `B x R` with trivial action | exact precedent for a trivial real vector-bundle module inside Mackenzie's domain | not a constant bundle for arbitrary `T0` topological abelian `A` on the Paper-12 owner |
| Mackenzie Def. 5.6 and Eq. (5.7), pp. 290--291 / physical pp. 14--15; p. 301 / physical p. 25 | continuous nonhomogeneous cochains on all composable tuples; normalized cochains explicitly postponed | strong full-cochain/unnormalized convention comparator | not an applicability theorem for the actual non-Hausdorff groupoid |
| Blanco--Uribe--Waldorf (2023), §§2.3--2.4, printed pp. 1473--1475 / physical pp. 5--7 | for a simplicial paracompact space, the full complex `Map(X_*,A)` is called cohomology of continuous cochains; for contractible `A` it computes Segal--Mitchison cohomology; explicit full inhomogeneous group-nerve differential | exact one-object comparator for `G=(R,+)`, `A=R`; conditional simplicial-space comparator for an actual groupoid nerve once every level's paracompactness is proved | `Topab` means compactly generated, locally contractible, Hausdorff coefficients (p. 1472 / physical p. 4); arbitrary `T0` `A` is outside; this source does not call the result a general topological-groupoid cohomology |
| Farsi--Huang--Kumjian--Packer (2022), Def. 3.7, printed p. 3336 / physical p. 12 | for any topological groupoid and locally compact abelian `H`, a continuous 1-cocycle is a continuous groupoid homomorphism; first continuous cocycle groupoid cohomology is cocycles modulo unit-function coboundaries | exact degree-one terminology for `H=R` on the Paper-12 groupoid | degree one only; no all-degree nerve complex, arbitrary-`T0` coefficient result, marked period image, or quotient functor |
| Fuchssteiner--Wockel, arXiv `1110.2977v2`, physical/author pp. 2--3 and Cor. II.8 on p. 7 | continuous homogeneous group cochains for a topological group and comparison with locally continuous cohomology for loop-contractible coefficients | standard one-object topological-group comparator; `R` is a loop-contractible trivial `R`-module | homogeneous one-object theory, not the actual groupoid complex; conversion to the Paper-12 inhomogeneous convention must be stated, not assumed |

### 5.2 Naming decision

The exact naming classification is:

- **Generic all-degree owner, arbitrary named `T0` coefficient `A`:** retain
  `C_cnv^*(G;underline(A))` and `H_cnv^*(G;underline(A))` as the
  **Paper-12 author-defined continuous unnormalized nerve complex and its
  algebraic cohomology**. None of the audited named theories matches both
  the actual owner/domain and this coefficient generality.
- **One-object group `(R,+)` with trivial `A=R`:** the Paper-12 full
  inhomogeneous complex is the `Map(R^*,R)` continuous-cochain complex in
  Blanco--Uribe--Waldorf §2.4. Since `R^n` is paracompact and `R` is a
  contractible object of `Topab`, their Lemma 2.3 gives the stated
  Segal--Mitchison comparison. Fuchssteiner--Wockel supplies the compatible
  continuous homogeneous group-cochain comparator. This exact group
  specialization does not rename the actual groupoid theory.
- **Degree one on the actual groupoid with `A=R`:** `Z_cnv^1` is exactly the
  continuous real-valued groupoid-cocycle group of Farsi et al. Definition
  3.7. Their coboundary is written `f(r gamma)-f(s gamma)`, whereas Paper 12
  freezes `h(s gamma)-h(r gamma)`; because `f` ranges over all continuous
  unit functions, negating `f` makes the two **subgroups** equal. Thus the
  degree-one quotient agrees, while the manuscript must disclose the sign
  convention and must not extrapolate to all degrees.
- **Actual all-degree groupoid with `A=R`:** Blanco--Uribe--Waldorf can be
  invoked as a simplicial-space comparison only after Phase 3 independently
  proves that every nerve level meets its paracompactness hypothesis. This
  audit does not discharge `P12-1` or license the unqualified name
  “continuous topological-groupoid cohomology.”

The P12 convention is genuinely full/unnormalized: values on all degenerate
simplices are retained. Mackenzie's p. 301 statement that normalized cochains
are postponed, Blanco--Uribe--Waldorf's full `Map(G^p,A)` complex, and
Fuchssteiner--Wockel's full homogeneous map spaces are compatible convention
comparators. None removes the protocol's obligation to prove `d^2=0` and the
all-degree chain maps directly.

### 5.3 Constant bundle, Cauchy step, and isotropy restriction

- The constant bundle `X x A -> X` with identity arrow action remains an
  elementary Paper-12 definition at generic hypotheses. Mackenzie's
  `B x R` trivial module is exact only for real locally convex coefficients
  in his stricter domain; it is citation support, not ownership transfer.
- Farsi et al.'s “continuous groupoid homomorphism” definition makes the
  restriction of a 1-cocycle to an isotropy group a continuous homomorphism,
  and its displayed coboundary vanishes when `r gamma=s gamma`. The class
  assignment `Per_x([b])=image(res_x b)`, its representative independence,
  transitive-unit comparison, and marked-period interpretation are still
  Paper-12 definitions/proofs; the source does not name that package.
- Blanco--Uribe--Waldorf Lemma 2.5 identifies first group cohomology with
  continuous homomorphisms. For `(R,+)` this source-checks the target of the
  degree-one classification. The further statement that a continuous
  additive `f:R->R` is `f(t)=lambda t` is the elementary continuous Cauchy
  argument preregistered for direct proof; no stronger citation credit is
  needed or claimed.
- The audited framework set supplies no marked strict/scaled/unmarked
  morphism package and no standard period-quotient functor. That statement
  is limited to these exact comparators; the independent bounded novelty
  audit alone may issue the protocol's `SUPPORTED_WITHIN_SEARCH` conclusion.

## 6. Internal nonredundancy and source-credit split

The framework audit supports the locked Paper-9--Paper-12 delta without
making a literature-wide novelty claim:

| Result component | Already owned | Still new/direct in Paper 12 |
|---|---|---|
| actual `Gamma_p` and orbit topology | Paper 9 | no topology re-proof may be sold as new |
| generic range-first arrow groupoid and `T0` arrow-factorization | Paper 11 | all finite nerve degrees, face maps, and chain isomorphism |
| packet/action/common `p^Z` and `log p` clock | Deninger | cohomological isotropy image and marked recovery |
| continuous 1-cocycle terminology | Farsi et al. | exact `H^1` calculation on the indiscrete action groupoid |
| continuous group cochain comparator | Blanco et al.; Fuchssteiner--Wockel | transfer to the exact groupoid owner and frozen convention |
| period quotient and marked morphism categories | no owner in this five-source comparison set | direct typed construction/proofs, subject to the independent novelty audit |

This division prevents arithmetic source credit from being inferred merely
from a copied period label, and prevents a standard quotient topology from
being identified with Paper 9's actual inherited indiscrete topology.

## 7. Manifestation integrity and release boundary

Five exact PDFs and five machine-readable sidecars are retained under
`notes/sources/coh-*`. All five final sidecars report `PASS`, three agreeing
page counts, and no warnings under `pdf_read_preflight/1.0.0`. Exact hashes,
official URLs, bibliographic manifestations, physical/printed page maps, and
licence notes are frozen in `notes/sources/coh-source-manifest.md`; the ten
retained evidence objects are covered by `notes/sources/coh-sources.sha256`.

For Fuchssteiner--Wockel, the retained manifestation is the exact current
arXiv-served `v2` PDF. The arXiv version stamp says `12 Apr 2012`; arXiv
metadata calls it the final version and maps it to *Topology and its
Applications* 159 (2012), 2627--2634, DOI
`10.1016/j.topol.2012.04.006`. The DOI/publisher and author publication
records were verified, but the publisher PDF endpoint denied automated
retrieval. No publisher-PDF byte hash or printed-to-physical content
crosswalk is invented.

The existing `notes/sources/.gitignore` contains:

```gitignore
*.pdf
!*.preflight.json
```

This workspace has no `.git` metadata, so an index/staging check cannot be
run here. That is not treated as a release pass: the protocol's later
public-sync dry run must mechanically show zero source PDFs in the staged
payload. Every retained PDF is an internal evidence cache only, never a
public supplement or manuscript attachment. Scholarly citations must use
the canonical arXiv/DOI/journal/author endpoint, never a local path, sidecar,
or hash.

## 8. Mandatory downstream source conditions

Phase 3 and manuscript work must preserve all of the following:

1. State `PACKET_COROLLARY` only on the exact fixed-prime
   `G_p^pkt=Gamma_p rtimes R`, with “every unit” and the source-normalized
   right `+t` action explicit. Do not promote it to the full suspension or a
   cross-prime owner.
2. Credit Deninger only for packet/action/stabilizer/clock, Paper 9 only for
   actual inherited topology, and Paper 11 only for the generic arrow theorem
   and degree-one factorization.
3. Retain author-defined `C_cnv/H_cnv` at generic hypotheses. Use the named
   group and degree-one comparisons only with the coefficient, domain, degree,
   and sign qualifications in Section 5.
4. Prove the all-degree nerve topology, `d^2=0`, chain isomorphism, continuous
   Cauchy step, coboundary-on-isotropy fact, representative independence,
   covariance/non-descent, and quotient functor directly. This audit is not a
   proof substitute.
5. Keep the standard Hausdorff quotient `R/(log p)Z` distinct from the actual
   inherited indiscrete orbit topology.
6. Preserve source-PDF exclusion and complete the no-PDF staged/index dry run
   before any public release.

Subject to those frozen conditions, the framework/source gate is **PASS —
C0/M0/m0**, and the exact packet source branch is **`PACKET_COROLLARY`**.
