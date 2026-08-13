# Phase 2 — Deninger packet primary-source audit

Status: **COMPLETE — Investigation only**  
Date: 2026-08-13  
Frozen candidate: `DEN-WITT-Z-FIN`  
Protocol inputs: `research_protocol.md`, `stage1_handoff.md`  
Downstream construction performed: **none**

## Executive finding

**Source-only gate: NO-GO for a packet transverse trace or dynamical determinant.**

- **[PROVED]** Deninger's v4 source defines the ambient rational-Witt colimit, its
  `Q_{>0}` action, the suspension flow, the packets `Gamma_p`, their common least
  period `log p`, and a choice-dependent set/equivariant parametrization of their
  orbit fibres. Theorems 5.2 and 6.1 exhaust all periodic points by pairwise
  disjoint packets.
- **[PROVED]** For `Spec Z`, the set of `R`-orbits in one packet is noncanonically
  identified with the compact group

  ```text
  B_p = Aut(Fbar_p^x) / Aut(Fbar_p)
      = Zhat_(p)^x / p^Zhat.
  ```

  This set is uncountable. Thus a prime labels an uncountable equal-period family,
  not one isolated primitive orbit.
- **[PROVED]** The parametrizations (37)--(39) and the fibration map depend on a
  lift `x` and an embedding `iota`; only projection (40) to
  `Q_{>0}/p^Z` is declared canonical.
- **[OPEN]** The source does not identify the quotient topology on
  `Gamma_p/R` with the compact-group topology on `B_p`, does not prove local
  triviality or properness of the packet fibration, and does not prove that a
  measure transported through different choice-dependent parametrizations is
  independent of those choices.
- **[PROVED]** Abstractly, `B_p` has a unique normalized Haar probability, by the
  standard Haar theorem for compact groups. This is a fact about the abstract
  base group; it is not a source-defined packet trace.
- **[NOT_TESTABLE]** On the frozen source object there is no selected
  packet/orbit groupoid, packet Haar system, observable algebra with a periodic
  trace, transverse lift/disintegration, or rule for the relative masses of the
  components indexed by `p`. Hence neither a packet contribution nor its
  repetition coefficients can be tested without adding structure.
- **[PROVED]** Section 11 does define a Haar-normalized convolution algebra, but
  on a different inverse-limit object. It supplies no proved bridge to packet
  orbit spaces or periodic-return traces; it therefore does not cure the gate
  failure.

The smallest missing datum is not another period calculation. It is a
choice-independent measured trace domain tied to the packet orbit relation,
together with its trace and global component normalization.

## Evidence labels

Only the following labels are used for substantive findings:

- **PROVED** — stated in the audited primary source, or an elementary/standard
  consequence whose derivation is displayed here;
- **OPEN** — mathematically meaningful, but not settled by the audited source;
- **NOT_TESTABLE** — cannot be evaluated on the frozen source object because a
  required definition or domain is absent.

No target Euler factor, Riemann zero, or desired repetition coefficient was used
to infer any structure.

## 1. Corpus, retrieval, and version lock

### 1.1 Included sources

| ID | Role and evidence level | Verified metadata | Stable access | Local copy |
|---|---|---|---|---|
| `DEN-V4` | Original construction and theorem source; highest discipline-relative mathematical evidence | Christopher Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, last revised 2024-02-07; journal DOI `10.1016/j.indag.2024.05.007`; *Indagationes Mathematicae* 37(1), January 2026, 25--136 | [arXiv record](https://arxiv.org/abs/1807.06400), [v4 PDF](https://arxiv.org/pdf/1807.06400v4), [publisher/DOI](https://doi.org/10.1016/j.indag.2024.05.007) | `sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf` |
| `DEN-SURVEY` | Author's primary overview/restatement; corroborative, not independent replication | Christopher Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643v1, submitted 2023-01-27; written for *Colloquium De Giorgi 2021 and 2022*, edited by Andrea Malchiodi, Edizioni della Normale, 2024, ISBN `978-88-7642-773-2` | [arXiv record](https://arxiv.org/abs/2301.11643), [v1 PDF](https://arxiv.org/pdf/2301.11643v1), [publisher volume](https://edizioni.sns.it/prodotto/colloquium-de-giorgi-2021-2022/) | `sources/deninger-primes-knots-periodic-orbits.pdf` |

Bibliographic verification:

- **[PROVED]** arXiv records four versions of `DEN-V4`: v1 (2018), v2 (2019),
  v3 (2022), and v4 (2024-02-07). The local source lock is v4, because the
  intrinsic rational-Witt construction and later topology differ materially
  from the early extrinsic versions.
- **[PROVED]** The publisher identifies the journal article as open access,
  volume 37, issue 1, January 2026, pages 25--136, DOI
  `10.1016/j.indag.2024.05.007`. The local file is the author/arXiv v4, not a
  claim that the publisher PDF is byte-identical.
- **[PROVED]** The survey's publisher page records the 2024 volume, editor,
  total extent `xvii--230`, and ISBN above. No non-arXiv chapter DOI was found
  in the audited arXiv or publisher records; this is not a claim that none can
  ever be assigned.
- **[PROVED]** Both substantive sources are by the constructor of the system.
  The survey therefore has an intellectual non-independence limitation and is
  used only to corroborate or clarify the original theorem source. No relevant
  financial conflict or venue-integrity warning was found.

### 1.2 Local integrity record

| File | SHA-256 | `pdfinfo` | ARS PDF preflight | Locator policy |
|---|---|---|---|---|
| `deninger-dynamical-systems-arithmetic-schemes-v4.pdf` | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | 119 pages; unencrypted; text extraction succeeds | `UNAVAILABLE` because `pypdf` is absent; see adjacent sidecar | theorem/formula numbers are primary; physical PDF pages were manually cross-checked by page-bounded extraction and arXiv HTML |
| `deninger-primes-knots-periodic-orbits.pdf` | `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | 16 pages; unencrypted; text extraction succeeds | `UNAVAILABLE` for the same dependency reason | theorem numbers are primary; physical PDF pages are advisory manual locators |

- **[PROVED]** The preflight verdict is an environment/tooling limitation, not
  evidence of PDF corruption. Page counts, encryption state, page-bounded text,
  and theorem/formula text were separately checked.
- **[OPEN]** Pixel-level identity between the local arXiv v4 and the final
  publisher typesetting was not tested. Stable theorem and formula numbers, not
  journal pagination, should be used downstream.

### 1.3 Search and screening log

Search date and cutoff: 2026-08-13.

Searched:

1. exact title, author, arXiv ID, and DOI on arXiv and the publisher site;
2. `Deninger rational Witt periodic packet Gamma`, `Theorem 5.2`,
   `Theorem 6.1`, `Haar`, `convolution`, `trace`, `groupoid`, and `Fredholm`
   in the full v4 text;
3. the author's institutional publication record;
4. the survey volume on the Scuola Normale publisher site.

Screening outcome:

- two theorem-bearing works included (`DEN-V4`, `DEN-SURVEY`);
- journal/arXiv manifestations deduplicated at work level;
- Deninger's 2025 *Rational Witt vectors and associated sheaves*
  (`arXiv:2508.05329`) was screened but excluded because its stated subject is
  rational-Witt sheafification/correspondences, not a replacement packet
  theorem or packet trace construction;
- announcements, talks, and analogy papers were excluded from theorem-level
  packet evidence.

## 2. Notation and theorem-number disambiguation

The sources use visually similar symbols for the arithmetic scheme and its
suspension. This audit uses:

| Audit symbol | Source object |
|---|---|
| `mathfrak X_0` | integral normal arithmetic scheme |
| `check X_0(C)_E` | Frobenius colimit carrying a `Q_{>0}` action |
| `X_0(E)` | suspension `check X_0(C)_E x_{Q_{>0}} R_{>0}` |
| `C_{x_0}` | pre-suspension `Q_{>0}` packet over a finite-residue-field point |
| `Gamma_{x_0}` | suspended packet `C_{x_0} x_{Q_{>0}} R_{>0}` |
| `E_f` | Deninger's finite-kernel admissible class; the protocol's local `E_fin` is read as this condition, not as source notation |

Numbering warning:

- **[PROVED]** `DEN-SURVEY`, Theorem 4.2 (PDF pp. 11--12), is the compact
  packet restatement and explicitly points back to `DEN-V4`, Theorems 5.2 and
  6.1.
- **[PROVED]** `DEN-V4`, Proposition 4.2 (PDF p. 27), instead concerns
  invariance of admissible subsystems. These are different results and must not
  be conflated.

## 3. Source reconstruction

### 3.1 Admissibility and functoriality

| Status | Source locator | Audited statement |
|---|---|---|
| **PROVED** | `DEN-V4`, Definition 4.1, PDF p. 27 | An admissible class `E` of characters `chi:kappa^x -> C^x` is invariant under field automorphisms and under the permitted power maps, and satisfies `(Tors)`: the torsion kernel is finite with allowed order. |
| **PROVED** | `DEN-V4`, Proposition 4.2, PDF p. 27 | `X(C)_E`, its Frobenius colimit, and their Galois quotients are invariant under the stated `G`, `N_0`, and `Q_{>0}` actions. |
| **PROVED** | `DEN-V4`, example list, PDF pp. 28--29 | The source defines `E_tors`, `E_max`, `E_f` (finite kernel), `E_fg`, `E_fd`, and `E_fd0`, with `E_f subset E_fg subset E_fd subset E_fd0 subset E_max subset E_tors`. |
| **PROVED** | `DEN-V4`, remark after the examples, PDF p. 29 | The author says the best character condition is unclear and that the topology of the resulting `R`-systems depends strongly on `E`. |
| **PROVED** | `DEN-V4`, Proposition 4.5, PDF pp. 29--30 | For functorial admissible `E`, dominant morphisms induce the stated maps of subsystems. This is restricted functoriality, not a category of packet morphisms. |
| **OPEN** | same section | The source does not designate `E_f` as uniquely canonical among the admissible alternatives. The protocol freezes it; the source merely permits it. |

Consequently, every packet assertion below is conditional on the frozen
finite-kernel choice being the source class `E_f`. This class satisfies the
hypotheses used for the full packets in Theorems 5.2 and 6.1.

### 3.2 The pre-suspension packet `C_{x_0}`

Let `x_0` have finite residue field, let
`p = char kappa(x_0)`, and let `N x_0 = |kappa(x_0)|`.

| Status | Source locator | Audited statement |
|---|---|---|
| **PROVED** | `DEN-V4`, Section 5, equations (37)--(39), PDF pp. 31--33 | After choosing a point `x` above `x_0` and an injection `iota` of roots of unity, the source constructs `N_0`- and then `Q_{>0}`-equivariant surjections/bijections describing `C_{x_0}`. |
| **PROVED** | equation (38), PDF p. 32 | There is a choice-dependent `Q_{>0}`-equivariant bijection `(Zhat_(p)^x/(N x_0)^Zhat) x_{p^Z} Q_{>0} -> C_{x_0}`. |
| **PROVED** | equation (39), PDF p. 33 | Equivalently, the description separates the residual finite `p`-action and the quotient `Q_{>0}/(N x_0)^Z`. |
| **PROVED** | immediately after (39), PDF p. 33 | As a set with orbits, `C_{x_0}` fibres over `B_p = Zhat_(p)^x/p^Zhat = Aut(Fbar_p^x)/Aut(Fbar_p)` and the fibres are its `Q_{>0}`-orbits. |
| **PROVED** | same paragraph, PDF p. 33 | Maps (37), (38), and the fibration map depend on the choices of `x` and `iota`. |
| **PROVED** | equation (40), PDF p. 33 | The map `C_{x_0} -> Q_{>0}/p^Z`, recording the kernel-size ratio modulo `p^Z`, is canonical. This is not the projection to `B_p`. |
| **PROVED** | Theorem 5.2, PDF pp. 34--37 | For admissible `E subset E_max`, all points with nontrivial `Q_{>0}` isotropy are the disjoint union of the `C^E_{x_0}`; their isotropy is `(N x_0)^Z`. If `E` contains `E_f`, the full `C_{x_0}` occurs. |

The choice statement is a hard modeling boundary: the source does not license
silently treating (37)--(39) as canonical coordinates.

### 3.3 Suspension, flow, packet, and period

`DEN-V4`, Section 6 (PDF pp. 38--39), defines

```text
X_0(E) = check X_0(C)_E x_{Q_{>0}} R_{>0},
(P_0,u)q = (F_q(P_0), q^{-1}u),
phi^t[P_0,u] = [P_0,u e^t],
Gamma_{x_0} = C_{x_0} x_{Q_{>0}} R_{>0}.
```

| Status | Source locator | Audited statement |
|---|---|---|
| **PROVED** | `DEN-V4`, PDF p. 38 | Formula (39) induces an `R_{>0}`-equivariant bijection for `Gamma_{x_0}`. Every orbit in it is a circle `R_{>0}/(N x_0)^Z`; the source calls the orbit fibres a fibration over `B_p`. |
| **PROVED** | `DEN-V4`, Theorem 6.1, PDF p. 39 | The nontrivial-`R_{>0}`-isotropy set is the disjoint union of `Gamma^E_{x_0}`, and every point in that packet has isotropy `(N x_0)^Z`. |
| **PROVED** | sentence after Theorem 6.1, PDF p. 39 | Every periodic orbit belongs to exactly one packet, and each finite-residue-field point determines exactly one packet. |
| **PROVED** | `DEN-SURVEY`, Theorem 4.2, PDF pp. 11--12 | The author restates the `Gamma_{x_0}` as pairwise disjoint compact subsets, consisting of compact orbits of length `log N x_0`, fibred over the compact group `B_p`. |
| **PROVED** | specialization to `Spec Z` | For `x_0=(p)`, `N x_0=p`, so the isotropy in additive flow time is `(log p)Z`. Every fibre orbit has least period `log p`; its `r`-fold return time is `r log p`. |

### 3.4 Exact `Spec Z` packet model

For `x_0=(p)` the residue-field degree is one. The residual finite action in
the general formula is trivial, and the source's chosen-coordinate formula
specializes to an `R`-equivariant **set bijection**

```text
Gamma_p  <-->  B_p x (R_{>0}/p^Z)
                  ~= B_p x (R/(log p)Z).
```

This line must be read with all three qualifications below.

1. **[PROVED]** It is an equivariant set-level description inherited from
   (37)--(39), not a source-canonical homeomorphism.
2. **[PROVED]** Its circle fibres are precisely the `R`-orbits.
3. **[OPEN]** The source does not prove that the quotient-topological orbit
   space `Gamma_p/R` is homeomorphic to `B_p`, nor that the displayed packet
   is a locally trivial topological product.

Thus the precise safe statement is

```text
|Gamma_p/R|  <-->  B_p
```

noncanonically as sets. Writing `Gamma_p/R = B_p` as a canonical topological
identity would exceed the source.

## 4. Topology, continuity, and cardinality

### 4.1 What topology the source does define

| Status | Source locator | Audited statement |
|---|---|---|
| **PROVED** | `DEN-V4`, Section 7, especially Proposition 7.4, PDF p. 43 | The source equips the rational-Witt point space with pointwise-convergence topology, the Frobenius colimit with its inductive-limit topology, and the Galois quotient with its quotient topology. Each `F_q` is a homeomorphism. |
| **PROVED** | Propositions 7.5--7.7 and Corollaries 7.8--7.9, PDF pp. 44--45 | In the affine case, including `Spec Z`, the relevant initial and quotient spaces are metrizable/separable and Hausdorff; the colimit spaces are Hausdorff under the stated ample-sheaf hypothesis. |
| **PROVED** | suspension definition, Section 6 | The ambient suspension carries the stated continuous-time action induced by multiplication on `R_{>0}`. |
| **PROVED** | Theorem 7.10 and following remark, PDF pp. 46--47 | Certain canonical global `R_{>0}`-equivariant decomposition maps are continuous bijections, but are not homeomorphisms in general. |
| **OPEN** | Sections 5--7 | No theorem in the audited source identifies the topology of the packet coordinate bijection with a product/bundle topology on `B_p x S^1`; no local sections, properness, or local triviality theorem is supplied. |

Theorem 7.10 does not itself prove that the particular `Gamma_p` coordinate
map fails to be a homeomorphism. It does prove that continuous equivariant
bijections in this construction cannot generally be upgraded to
homeomorphisms without a separate theorem.

### 4.2 Is the orbit family uncountable?

**[PROVED — derived from the source formula plus standard compact-group facts].**

The source identifies the orbit set, after choices, with
`B_p = Zhat_(p)^x/p^Zhat`. This quotient is infinite:

1. `Zhat_(p)^x = product_{ell != p} Z_ell^x` has a quotient containing a
   product of `C_2` over infinitely many odd primes `ell != p`, obtained from
   the square-class quotient in each coordinate. Hence it is not topologically
   finitely generated.
2. `p^Zhat` is procyclic. If it had finite index, the ambient compact abelian
   group would be topologically finitely generated, a contradiction.
3. An infinite compact metrizable group is uncountable (a countable compact
   group would, by Baire category and translations, be discrete and hence
   finite).

Therefore `B_p`, `|Gamma_p/R|`, and the set of primitive period-`log p` orbits
inside `Gamma_p` are uncountable.

Consequences stated at the investigation boundary:

- **[PROVED]** individual primitive periodic orbits are not locally finite by
  length: already at length `log p` there are uncountably many;
- **[PROVED]** a conventional isolated-orbit product that includes every
  primitive orbit cannot satisfy the usual finite-orbit-below-a-cutoff
  condition;
- **[OPEN]** calling this a *topologically continuous family* in the strong
  bundle sense requires the missing topology theorem above. The safe claim is
  “an uncountable family indexed set-theoretically by a compact group.”

## 5. Actions, equivalence relation, and missing automorphism data

### 5.1 Source-defined actions and relation

| Status | Object | Source content |
|---|---|---|
| **PROVED** | Galois action | On pairs `(x,P)`, `G` acts by transport/precomposition; the quotient defines the subscript-zero spaces. See Theorem 4.1 in the survey and Sections 3--4 in v4. |
| **PROVED** | Frobenius monoid | `N_0` acts by power precomposition `F_nu`; under admissibility these maps are injective and can be inverted in the colimit. |
| **PROVED** | rational action | `Q_{>0}` acts by homeomorphisms on the Frobenius colimit. |
| **PROVED** | flow action | `R` acts on the suspension by `phi^t[P,u]=[P,e^t u]`. |
| **PROVED** | monoid equivalence relation | Immediately after Theorem 6.1 (PDF p. 39), for a right `N_0`-set `Y`, the source defines `y ~ y'` iff `y nu = y' nu'` for some `nu,nu'`, and uses it to give an equivariant quotient model of the suspension. |
| **PROVED** | compact base group | `B_p` is defined as a quotient of field-automorphism groups and as `Zhat_(p)^x/p^Zhat`. |

### 5.2 What is not source-defined

| Status | Missing datum | Audit result |
|---|---|---|
| **NOT_TESTABLE** | intrinsic packet-automorphism group/action | The chosen-coordinate model permits translations and automorphisms of the abstract first factor, but the source does not define a choice-independent action of `B_p` (or a packet automorphism category) on `Gamma_p`. “Packet-automorphism invariance” therefore lacks a frozen source domain. |
| **NOT_TESTABLE** | selected periodic groupoid | The `Q_{>0}` action, the `R` flow, the monoid relation, and their orbit relations yield several standard external groupoid candidates. The source does not select one as the periodic trace groupoid or specify its arrows as the trace domain. |
| **NOT_TESTABLE** | transverse relation with topology | The set of flow orbits is clear, but no source theorem gives the required quotient topology/Hausdorffness/local charts on `Gamma_p/R` for a transverse groupoid construction. |
| **OPEN** | choice-change maps | The source says the fibration depends on `x,iota` but does not classify the transition maps between two choices. In particular it does not prove that every transition preserves any transported transverse measure. |

It would be mechanically possible to form the standard transformation groupoids
of the source-defined `Q_{>0}` and `R` actions. Doing so is not performed here:
choosing which one is the periodic trace domain, which completion/observable
algebra to use, and which transverse weight to impose would be a versioned
enrichment rather than a Phase-2 source finding.

## 6. Haar measures: exactly what exists

### 6.1 Abstract Haar probability on `B_p`

- **[PROVED]** Since `B_p` is a compact Hausdorff group, it has a unique
  normalized Haar probability `m_p`.
- **[PROVED]** This uniqueness is an application of the standard Haar theorem;
  Deninger does not state or construct `m_p` in the packet theorem.
- **[OPEN]** The choice-dependent packet-to-base projection prevents a
  source-only assertion that pulling `m_p` back to the orbit space is
  choice-independent. Such independence may be true if all transition maps are
  Haar-preserving, but that statement is not proved or even formulated in the
  audited source.
- **[NOT_TESTABLE]** A probability on the abstract orbit base is not a Haar
  system on a groupoid: it does not specify measures on arrow fibres, a
  disintegration/lift to `Gamma_p`, or a trace on an observable algebra.
- **[NOT_TESTABLE]** Even a canonical probability for each fixed `p` would not
  determine the relative masses of the disjoint components as `p` varies.
  Nothing in the packet theorem implies `tau(Gamma_p)=1` for every prime.

### 6.2 Acting-group Haar measures do not solve the transverse problem

- **[PROVED]** Standard transformation groupoids of the discrete
  `Q_{>0}` action or the `R` flow would carry the usual counting or Lebesgue
  Haar systems along acting-group directions.
- **[NOT_TESTABLE]** Those longitudinal systems do not select a transverse
  probability on the uncountable orbit base or a global packet trace. The
  source supplies no theorem converting them into the required periodic
  distribution.

This distinction prevents “the flow group has Haar measure” from being used as
a normalization argument for “one packet counts once.”

## 7. Section 11 audit: a real algebra, but no packet-trace bridge

It would be incorrect to say that `DEN-V4` contains no algebra or no Haar
normalization. Section 11, PDF pp. 66--68, defines both. It is essential to keep
its object separate from `Gamma_p`.

### 7.1 Source-defined Section 11 structure

| Status | Locator | Exact content |
|---|---|---|
| **PROVED** | equation (104), PDF p. 66 | The locally compact zero-dimensional group `leftarrow K^x = lim_N K^x` fits into `1 -> T mu_K -> leftarrow K^x -> K^x -> 1`, where the compact subgroup `T mu_K` is open. |
| **PROVED** | equations (105), PDF p. 66 | Haar measure `mu` on `leftarrow K^x` is normalized by `mu(T mu_K)=1`, and `C_c(leftarrow K^x)` is given its convolution product. |
| **PROVED** | equations (106)--(108), Lemma 11.1, PDF pp. 66--67 | The open-and-closed inverse-limit submonoid `leftarrow Gamma^x = lim_N(Gamma(mathfrak X,O)\{0})` yields a nonunital subalgebra `C_c(leftarrow Gamma^x)` with the stated truncated convolution formula. |
| **PROVED** | equations (111)--(113), Lemma 11.2, PDF pp. 67--68 | `varphi(f)=integral f(r)r dmu(r)` is a `G`-equivariant algebra homomorphism into `C^0(check X(C),C)`. It integrates the functions represented by global regular elements pointwise. |
| **PROVED** | equation (114), PDF p. 68 | Passing to `G`-fixed points gives `varphi_0:C_c(leftarrow Gamma^x)^G -> C^0(check X_0(C),C)`. |

There is a notation collision: packet `Gamma_{x_0}` and inverse-limit monoid
`leftarrow Gamma^x` are different objects.

### 7.2 Bridge test

| Required bridge | Evidence in Section 11 | Verdict |
|---|---|---|
| map to `Gamma_p/R` or `B_p` | none defined | **NOT_TESTABLE** |
| representation of the suspension `R`-flow on the convolution algebra | none defined | **NOT_TESTABLE** |
| periodic-return kernel/operator | none defined | **NOT_TESTABLE** |
| groupoid of packet orbits and its Haar system | none defined | **NOT_TESTABLE** |
| trace or semifinite weight on `C_c(leftarrow Gamma^x)` | none defined | **NOT_TESTABLE** |
| relation between `mu(T mu_K)=1` and a packet transverse probability | none proved | **NOT_TESTABLE** |
| Fredholm/nuclearity/determinant theorem | none defined | **NOT_TESTABLE** |

Full-text checks of v4 found no occurrence defining a `groupoid`, `trace`, or
`Fredholm` object. “Determinant” occurs in the introduction as motivation for
expected foliation cohomology, not as a theorem for the constructed packet
system.

Therefore:

- **[PROVED]** Section 11 is a genuine source-defined algebraic/Haar structure.
- **[PROVED]** `varphi` is an algebra homomorphism, not a trace functional.
- **[PROVED]** its Haar normalization concerns the compact open subgroup of
  `leftarrow K^x`, not the packet base `B_p` and not an orbit-groupoid Haar
  system.
- **[NOT_TESTABLE]** using Section 11 as the packet transverse trace would
  require new maps, a flow representation, and a trace theorem. No such bridge
  is present in the source.
- **[OPEN]** constructing such a bridge may be a future, explicitly versioned
  noncommutative enrichment, but it is not evidence for the frozen candidate.

## 8. The survey's trace formula is an analogy, not a transfer theorem

`DEN-SURVEY`, formula (9), PDF p. 8, discusses a distributional transverse
index formula for a different class of smooth compact three-dimensional
foliated systems under conformality, leafwise ellipticity, transversality, and
related analytic assumptions. It notes that fixed-time operators need not be
trace class and uses a mollified trace.

- **[PROVED]** The survey presents this formula before the rational-Witt packet
  construction, as part of the motivating analogy.
- **[NOT_TESTABLE]** The audited sources do not verify those smoothness,
  dimension, ellipticity, conformality, compact-leaf, or operator-domain
  hypotheses for `DEN-WITT-Z-FIN`.
- **[NOT_TESTABLE]** Formula (9) therefore cannot be imported as the trace
  theorem for `Gamma_p`.
- **[PROVED]** The same survey later says the rational-Witt spaces are
  infinite-dimensional, that even the `Spec Z` space is not satisfactorily
  understood, and that the construction has some but not all expected
  properties (PDF pp. 9--13).

## 9. Minimal go/no-go matrix

| Obligation | Frozen-source result | Evidence status |
|---|---|---|
| exact packet set | defined by suspension of `C_{x_0}` | **PROVED** |
| packet compactness | theorem-level author assertion/restatement | **PROVED** |
| flow and period | `phi^t`, isotropy `(log p)Z`, least period `log p` | **PROVED** |
| periodic exhaustion | Theorems 5.2 and 6.1 | **PROVED** |
| orbit base as a set | noncanonical bijection with `B_p` | **PROVED** |
| uncountable orbit family | derived from the compact group formula | **PROVED** |
| orbit-space topology `Gamma_p/R ~= B_p` | not established | **OPEN** |
| locally trivial/principal packet fibration | not established | **OPEN** |
| intrinsic base action / packet automorphism category | absent | **NOT_TESTABLE** |
| relevant relation | several actions and one monoid relation are defined | **PROVED**, but no trace-relevant selection |
| relevant packet groupoid | not selected/defined | **NOT_TESTABLE** |
| packet groupoid Haar system | not defined | **NOT_TESTABLE** |
| abstract Haar probability on `B_p` | unique by standard compact-group theory | **PROVED** |
| choice-independent measure on `Gamma_p/R` | not proved | **OPEN** |
| lift/disintegration to packet | absent | **NOT_TESTABLE** |
| global component masses across primes | absent | **NOT_TESTABLE** |
| packet observable/convolution algebra | absent; Section 11 algebra is a different object | **NOT_TESTABLE** |
| periodic trace / clean-family fixed-point theorem | absent | **NOT_TESTABLE** |
| repetition coefficient from the same trace | absent | **NOT_TESTABLE** |
| Fredholm or dynamical determinant domain | absent | **NOT_TESTABLE** |

### Gate decision

**NO-GO, in the strict source-only sense.** The source reconstructs the
periodic object far enough to prove that ordinary isolated-orbit counting is
inapplicable, but not far enough to state a unique packet transverse trace.

The smallest missing definitions/theorems are:

1. a source-canonical topological/measured orbit relation or a selected
   packet groupoid;
2. a compatible Haar system or transverse measure, including proof of
   independence from `x,iota`;
3. an observable/kernel algebra and trace domain for the suspension flow;
4. a lift/disintegration from orbit-base measure to the relevant trace;
5. one global rule for masses of the disjoint packets and one return/repetition
   theorem.

None may be filled by requiring the output to equal an Euler product. A future
standard transformation-groupoid or Section-11 enrichment must be recorded as
a new model version and tested independently.

## 10. Phase-2 limitations and handoff facts

- **[PROVED]** Packet existence, common least period, pairwise disjointness,
  exhaustion, compactness, and uncountable set-level orbit multiplicity are
  secure source findings.
- **[OPEN]** The strongest unresolved geometric question is whether the
  choice-dependent orbit parametrizations induce a canonical compact
  homogeneous transverse measure/topology after all transition maps are
  classified.
- **[NOT_TESTABLE]** The strongest unresolved analytic question is a packet
  trace: no trace domain or periodic fixed-point theorem exists on the frozen
  source object.
- **[PROVED]** The Section 11 convolution algebra must be acknowledged in any
  later paper, but its lack of a packet/flow bridge must be stated at the same
  time.
- **[PROVED]** No paper drafting, determinant definition, Euler product, zero
  comparison, or route-status mutation was performed in this phase.

## References

Deninger, C. (2026). Dynamical systems for arithmetic schemes.
*Indagationes Mathematicae, 37*(1), 25--136.
https://doi.org/10.1016/j.indag.2024.05.007. Audited text: arXiv:1807.06400v4.

Deninger, C. (2024). Primes, knots and periodic orbits. In A. Malchiodi (Ed.),
*Colloquium De Giorgi 2021 and 2022*. Edizioni della Normale. Audited text:
arXiv:2301.11643v1.
