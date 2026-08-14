# Paper 8 Phase-2 topology/source manifest

Frozen: 2026-08-14 (Asia/Shanghai)  
Scope: Deninger/Morishita primary manifestations used for the packet-topology,
same-object, and corrected one-orbit audit.  Groupoid/imprimitivity sources with
the `grp-` prefix belong to a separate audit.

All retained PDFs were downloaded from the versioned arXiv endpoints below on
2026-08-14.  ARS `pdf_read_preflight/1.0.0` returned `PASS` for every PDF:
declared, enumerated, and reader page counts agree and the warning arrays are
empty.  Hashes are SHA-256 over the exact local bytes.

| ID | Exact local full text | Canonical primary endpoint | Pages | PDF SHA-256 | Preflight sidecar SHA-256 | Retention role |
|---|---|---|---:|---|---|---|
| `TOP-DEN-DYN-v4` | `topo-deninger-dynamical-systems-arithmetic-schemes-v4.pdf` | <https://arxiv.org/pdf/1807.06400v4> | 119 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `0526c6a84b907d109db4e2932cbb378b60b172dce8981c034d866e398a25a9e4` | `E_f`, fixed-fibre parametrization, packet/isotropy, and pre-suspension topology |
| `TOP-DEN-SUR-v1` | `topo-deninger-primes-knots-periodic-orbits-v1.pdf` | <https://arxiv.org/pdf/2301.11643v1> | 16 | `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | `de951a65ca4ebe0bca9743e3509253f895bc1f9ee1f99883caf18c79fc506e34` | packet and individual-orbit compactness theorem |
| `TOP-MOR-v5` | `topo-morishita-deninger-connes-consani-v5.pdf` | <https://arxiv.org/pdf/2508.15971v5> | 26 | `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | `f0061d741b0ecfba33241402c666945285ffbd75d6efdbc1ebcae6a5aed00a97` | continuous adelic map, target prime circle, omitted-refinement warning, and printed-scope audit |

The independent checksum list is `phase2_topology_sources.sha256` in this
directory.  It covers the three PDFs and their three same-stem preflight
sidecars; it intentionally does not self-hash this manifest.

## Load-bearing locator index

### `TOP-DEN-DYN-v4`

- physical p. 32, equation (35): every finite-kernel character in a fixed
  residue-characteristic-`p` fibre is represented by
  `chi_x o ( )^a o ( )^nu`, with `a in Zhat_(p)^x` and `nu in N`;
- physical pp. 38--39, Section 6 and Theorem 6.1: suspension flow, prime
  packets, period `log N x_0`, and exact common isotropy `N x_0^Z`;
- physical p. 43, Proposition 7.4: open stages and Frobenius
  homeomorphisms in the colimit;
- physical p. 44, Proposition 7.6: the affine initial space is metrizable and,
  for separable `C`, second countable and separable;
- physical pp. 44--45, Proposition 7.7 and Corollary 7.8: compact-Galois
  quotient metric and Hausdorffness of the affine quotient stage;
- physical p. 45, Corollary 7.9: the checked pre-suspension spaces are
  Hausdorff when the arithmetic scheme has an ample invertible sheaf;
- physical pp. 46--47, Theorem 7.10 and Remark 2: the displayed coproduct
  maps are continuous bijections and need not be homeomorphisms;
- physical p. 47, paragraph after Theorem 7.10: admissible-`E` spaces have the
  stated subspace/colimit topologies and all preceding Section-7 results remain
  valid after restriction to `E`.

### `TOP-DEN-SUR-v1`

- physical pp. 11--12, Theorem 4.2: each `Gamma_x0` is a compact subset,
  packets are pairwise disjoint, and the fibres over the compact profinite
  base are compact periodic orbits.

### `TOP-MOR-v5`

- physical p. 5, equation (1.1.5): the adelic prime orbit `C_p` is the
  Hausdorff circle `R_+/p^Z`, of logarithmic length `log p`;
- physical p. 13, Remark 2.1.13: Morishita expressly omits Deninger's
  character refinement, so the printed ambient source object is not the
  genuine `E_f` object;
- physical pp. 16--17, equation (2.2.7) and Theorem 2.2.8: full-character
  parametrization/homeomorphism assertions whose applicability to `E_f` must
  be re-proved rather than imported;
- physical p. 23, Lemma 3.4, and physical p. 24, Lemma 3.5: continuity and
  equivariance of the character/adelic map and flow anti-equivariance after
  suspension;
- physical pp. 24--25, Theorem 3.6(2) and proof: the printed orbit-image
  claim and its proof, which checks only the zero `p`-component.

## Manifestation and currentness audit

- The official arXiv record for `1807.06400` was checked on 2026-08-14.  Its
  latest version remains v4, dated 2024-02-07.  Elsevier's official record
  identifies the journal manifestation as *Indagationes Mathematicae* 37(1)
  (January 2026), pp. 25--136, DOI
  `10.1016/j.indag.2024.05.007`, open access under CC BY 4.0.  The publisher
  PDF endpoint returned HTTP 403 in this environment, so every technical page
  locator in this audit is explicitly to arXiv v4; no claim is made that its
  physical pagination equals the journal pagination.
- The official arXiv record for `2301.11643` still has only v1, dated
  2023-01-27.  Deninger's official University of Muenster bibliography records
  the corresponding chapter in *Colloquium De Giorgi 2021--2022*, Scuola
  Normale Superiore (2024).  The retained locator manifestation is v1.
- The official arXiv record for `2508.15971` remains v5, dated 2026-01-21;
  its comments say “to appear in Münster Journal of Mathematics.”  Morishita's
  Kyushu University profile, updated 2026-06-18, records it as a reviewed 2026
  journal paper.  No later accessible full-text manifestation was located.
- Official arXiv author searches, Deninger's Muenster bibliography, and
  Morishita's Kyushu profile were checked through the 2026-08-14 cutoff.  No
  later Deninger/Morishita paper supplies a packet-Hausdorff, packet product
  chart, or transverse-measure theorem.

## Screened but not retained

| Primary record | Current manifestation checked | Exclusion reason |
|---|---|---|
| C. Deninger, *Rational Witt vectors and associated sheaves* | arXiv `2508.05329v1`, 2025-08-07 | sheafification/relative-correspondence paper; no load-bearing packet-topology theorem |
| C. Deninger, *Is there a Birch and Swinnerton-Dyer conjecture for Dedekind zeta functions?* | arXiv `2504.15767v3`, final version 2026-04-01 | cohomological existence question; no packet-topology update |
| C. Deninger and D. Kamlesh, *A remark on the vanishing of Higgs fields in the p-adic Simpson correspondence* | arXiv `2508.13685`, current author listing checked | unrelated p-adic Simpson result |
| J. A. Alvarez Lopez, J. Kim, and M. Morishita, *Regularized determinant formulas for the zeta functions of 3-dimensional Riemannian foliated dynamical systems* | arXiv `2410.20758`, official author-search record | theorem for a separate smooth 3-dimensional FDS class, not the rational-Witt `E_f` packet topology |

## Reuse and redistribution boundary

Versioned arXiv endpoints and exact hashes make the local reading
reproducible.  They do not by themselves settle redistribution of every PDF
in a public repository.  Before publication, verify each displayed licence;
if necessary publish this manifest, checksums, URLs, and locators without the
PDF bytes.
