# Paper 9 Phase-2 source manifest

Frozen: 2026-08-14 (Asia/Shanghai)  
Scope: topology and comparison sources for the fixed-prime rational-Witt
`E_f` packet, plus the conditional quotient-measure bridge.  
Checksum ledger: `paper9_sources.sha256`

## 1. Exact retained manifestations

The first three PDFs are reused byte-for-byte from Paper 8 rather than
duplicated. The remaining four are Paper-9 local research copies. Every PDF
has an adjacent ARS `pdf_read_preflight/1.0.0` sidecar with verdict `PASS`,
equal declared/enumerated/reader page counts, and an empty warning array.

| ID | Exact local full text | Canonical primary endpoint | Manifestation | Pages | PDF SHA-256 | Preflight sidecar SHA-256 | Retention role |
|---|---|---|---|---:|---|---|---|
| `P9-DEN-DYN-v4` | `../../../8-isotropy-trace/notes/sources/topo-deninger-dynamical-systems-arithmetic-schemes-v4.pdf` | <https://arxiv.org/pdf/1807.06400v4> | arXiv v4, 2024-02-07; technical locators are to this version | 119 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `0526c6a84b907d109db4e2932cbb378b60b172dce8981c034d866e398a25a9e4` | exact `E_f` character packet, set parametrization, suspension, isotropy, and topology warnings |
| `P9-DEN-SUR-v1` | `../../../8-isotropy-trace/notes/sources/topo-deninger-primes-knots-periodic-orbits-v1.pdf` | <https://arxiv.org/pdf/2301.11643v1> | arXiv v1, 2023-01-27 | 16 | `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | `de951a65ca4ebe0bca9743e3509253f895bc1f9ee1f99883caf18c79fc506e34` | compactness wording and continuous-bijection warning |
| `P9-MOR-v5` | `../../../8-isotropy-trace/notes/sources/topo-morishita-deninger-connes-consani-v5.pdf` | <https://arxiv.org/pdf/2508.15971v5> | arXiv v5, 2026-01-21 | 26 | `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | `f0061d741b0ecfba33241402c666945285ffbd75d6efdbc1ebcae6a5aed00a97` | adelic target wording, omitted-refinement notice, and continuous comparison map |
| `P9-CC-SCALING-2016` | `cc-scaling-site-2016.pdf` | <https://www.numdam.org/item/10.1016/j.crma.2015.09.027.pdf> | publisher PDF, *C. R. Acad. Sci. Paris* 354 (2016), 1--6, DOI `10.1016/j.crma.2015.09.027` | 6 | `fc10fee06a68c516688c2e1c3a8e7010f3e82f4b7af6215023fbadc408175887` | `e68f18ba682e37fa18b44e4d25cbd21380e5cb75e57a0c14b74f0fbd05527896` | intrinsic scaling-topos point subspace `C_p` and its explicit topological circle theorem |
| `P9-CC-XQ-v1` | `cc-knots-primes-class-field-theory-v1.pdf` | <https://arxiv.org/pdf/2501.06560v1> | arXiv v1, 2025-01-11; published in *Regulators V*, Contemporary Mathematics 842 (2026), p. 105 ff., DOI `10.1090/conm/842/16852` | 30 | `f200c41d6d772389528bb1de58ad7fe98fd8db807d72360d4311ecb3c44d2fe5` | `88396c16d6884aac4d62e8008c3c63ed47fee9d08a97d4b0933d57313e1c4c38` | latest primary wording for the natural quotient `X_Q`, its inherited `C_p`, and the mapping-torus cover |
| `P9-LB-2016` | `lebruyn-sieve-topology-2016-author-version.pdf` | <https://repository.uantwerpen.be/docman/irua/e9b2f1/10764.pdf> | institutional archived preprint of the peer-reviewed article, *J. Algebra Appl.* 15 (2016), 1650020, DOI `10.1142/S0219498816500201` | 10 (repository cover plus 9 article pages) | `50895be562a1939d9032dde63d84f43f8b51d7a9d115ba3ee56ce307780d0f5e` | `88723b2ae76d0f5462daf3722ac971da2078551a1065853091330e7bebb9e0cc` | formal correction of the earlier claim that the standard finite-adele-class topology is trivial |
| `P9-JUS-v2` | `justel-zak-transform-strongly-proper-v2.pdf` | <https://arxiv.org/pdf/1605.05168v2> | arXiv v2; published *J. Lond. Math. Soc.* 97(1) (2018), 47--76, DOI `10.1112/jlms.12097` | 30 | `6e8f63351b20868b3aaf40a27b9d0d9f1dfa1179fee5ff5628e3c4fcce343672` | `929e2893e68c64f139881f5fdcc9c0d3c727995080e73aa7015c76a7230c309a` | conditional Weil disintegration theorem for strongly proper lcH actions |

All page locators below use physical PDF pages, except that the Le Bruyn
locator also supplies printed article pagination because of the repository
cover.

## 2. Load-bearing locator index

### `P9-DEN-DYN-v4`

- physical p. 32, equation (35): the finite-kernel characters in the fixed
  residue-characteristic-`p` fibre are reached from
  `Zhat_(p)^times x N`; this is a surjection of sets;
- physical p. 32, equation (38): the fixed-prime packet fibre has a
  `Q_{>0}`-equivariant **bijection** from the displayed exponent quotient;
- physical p. 33, equation (39): the same packet fibre is rewritten using
  `Q_{>0}/N(x_0)^Z`, again as an equivariant **bijection**, followed by a
  set-level fibration statement;
- physical pp. 38--39, Section 6 and Theorem 6.1: suspension quotient, right
  diagonal action, packet definition, induced `R_{>0}`-bijection, and exact
  isotropy `N(x_0)^Z`;
- physical p. 43, Proposition 7.4: open colimit stage and Frobenius
  homeomorphisms before suspension;
- physical pp. 44--45, Propositions 7.6--7.7 and Corollaries 7.8--7.9:
  metric/Hausdorff results for the initial and checked **pre-suspension**
  spaces;
- physical pp. 46--47, Theorem 7.10 and Remark 2: source-model maps into the
  suspension are continuous bijections and are not homeomorphisms in general;
- physical p. 47, paragraph after Theorem 7.10: admissible-`E` spaces carry
  the stated subspace/colimit topologies, so the topology setup applies to
  `E_f`;
- physical p. 49, equation (68) and following sentence: the
  `Q_{>0}`-action on the **adelic target model**
  `Hcheck_Etors x R_{>0}` is not properly discontinuous;
- physical p. 62, proof of Theorem 9.6: a related quotient `Y`, abstractly
  `Zhat^times`, has the coarse topology by strong approximation;
- physical p. 63, opening of Section 10: a leaf slice maps continuously and
  bijectively to its image but generally not homeomorphically; without a
  properly discontinuous action the partition need not be locally trivial;
- physical pp. 64--65, Proposition 10.3 and its first remark: a related
  generic adelic suspension quotient is irreducible but `T1` because its
  orbits are closed. This is a mandatory negative control against promoting
  analogy to the fixed-prime packet.

### `P9-DEN-SUR-v1`

- physical pp. 11--12, Theorem 4.2: each packet is a compact subset, the
  packets are disjoint, and the individual periodic orbits are compact;
- physical pp. 12--13, Theorem 4.4 and following sentence: the displayed
  decomposition map is a continuous bijection and is not a homeomorphism.

### `P9-MOR-v5`

- physical p. 5, equation (1.1.5): the adelic prime orbit is said to be
  “isomorphic” via the infinite projection to `R_+/Np^Z`; the statement does
  not say “homeomorphism”;
- physical p. 13, Remark 2.1.13: the paper explicitly omits Deninger's
  character refinement;
- physical pp. 14--17, equation (2.2.7), Theorems 2.2.8--2.2.9: quotient
  topology and printed homeomorphism claims for the full-character source;
  equation (2.2.7) only parametrizes finite-kernel characters and therefore
  does not justify the declared full `Hom` scope;
- physical p. 23, Lemma 3.4, and physical p. 24, Lemma 3.5: the
  character-to-adele map and its suspension are continuous with the stated
  equivariance/anti-equivariance;
- physical pp. 24--25, Theorem 3.6(2): the orbit-image proof checks the zero
  `p`-component but does not check non-vanishing of every away-`p` component.

### `P9-CC-SCALING-2016`

- physical/printed p. 5, Lemma 6.3(i): for the **intrinsic subspace of points
  of the scaling topos**, `R_+^*/p^Z -> C_p` is explicitly a **topological
  isomorphism**.

### `P9-CC-XQ-v1`

- physical p. 3: the naive adele-class quotient is described as highly
  singular;
- physical p. 9, Section 2: `X_Q` is the natural quotient, the scaling-topos
  point set is canonically bijective with it, and a collection of its points
  determines a **subspace** `C_p subset X_Q`; the map
  `R_+^*/p^Z -> C_p` is called an “isomorphism” showing a circle;
- physical pp. 11--12, Proposition 3.4: `pi^{-1}(C_p)` is canonically
  isomorphic to the mapping torus of a homeomorphism, and its projection onto
  `C_p` is a fibration with nontrivial monodromy and no continuous section;
- physical p. 28, Section 6: the homotopy/classifying-space replacement is
  Hausdorff and locally compact because the replacement action is proper.
  This is not a separation theorem for the naive quotient itself.

### `P9-LB-2016`

- printed p. 2 / physical p. 3, Theorem 1: the standard topology on the
  finite-adele-class quotient has a countable basis indexed by finite sets of
  primes; it is coarse but not indiscrete;
- printed p. 9 / physical p. 10, acknowledgement: the referee corrected an
  erroneous statement about the standard topology in an earlier version.

### `P9-JUS-v2`

- physical pp. 3--4, Definition 2.1: Cartan, proper, Palais-proper, and
  strongly proper actions and the quotient topology;
- physical p. 5, Lemma 2.3: for a proper lcH action, orbital averaging maps
  `C_c(X)` into `C_c(G\X)`;
- physical p. 6, Theorem 2.4: a strongly proper action on an lcH space,
  together with a quasi-invariant Radon measure, yields a unique Radon measure
  on the orbit space and the exact Weil formula.

## 3. Manifestation/currentness check

- Deninger `1807.06400` remains at v4. The journal manifestation is
  *Indagationes Mathematicae* 37(1) (January 2026), 25--136, DOI
  `10.1016/j.indag.2024.05.007`; locators here remain explicitly arXiv-v4
  locators.
- Deninger `2301.11643` remains at v1.
- Morishita `2508.15971` remains at v5, dated 2026-01-21. No later accessible
  full text was found.
- Connes--Consani `2501.06560` remains at v1. Its 2026 Contemporary
  Mathematics manifestation was verified bibliographically, but the
  publisher full text was not accessible; technical locators therefore use
  arXiv v1.
- Official arXiv records, author bibliographies, and targeted exact-term
  searches were checked through 2026-08-14. No later primary source supplies
  a Hausdorff/LCH theorem, a closed restricted orbit relation, or a
  non-`T0`/indiscrete theorem for Deninger's genuine rational-Witt `E_f`
  prime packet.

## 4. Retention and public-sync boundary

The PDFs are retained locally for reproducible page-level verification.
Hashes and URLs do not establish redistribution permission. Public GitHub
synchronization must exclude every `notes/sources/*.pdf` in this directory
and the reused Paper-8 source PDFs unless the exact manifestation has a
documented redistribution licence. Synchronize the manifest, checksum ledger,
preflight sidecars, URLs, and exact locators instead.
