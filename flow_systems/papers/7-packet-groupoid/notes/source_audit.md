# Paper 7 Phase-2 source audit — Deninger packet ownership

Audit status: **FROZEN — SOURCE OWNERSHIP COMPLETE; ANALYTIC TRANSPORT NOT FOUND**  
Cutoff: **2026-08-14, Asia/Shanghai**  
Scope: `DEN-WITT-Z-FIN` and its proposed transport to the Paper-7 proxy records  
Local full texts locked: **4**  
Downstream proof or manuscript synthesis: **not performed**

## 1. Executive verdict

Deninger's source owns the following data for `Spec Z` under the finite-kernel
admissibility condition:

- the prime closed point `(p)` and its unique packet `Gamma_p`;
- the packet's periodic circles, isotropy/repetition group `p^Z`, and least
  additive period `log p`;
- an auxiliary-choice-dependent equivariant set parametrization involving
  the abstract compact group
  `B_p = Zhat_(p)^x / p^Zhat`; and
- the assertion that `Gamma_p` is compact and is fibred over a compact group
  with the periodic circles as fibres.

The source does **not** own a choice-independent product identification
`Gamma_p ~= B_p x R/(log p)Z`, a Borel isomorphism of that form, a transverse
measure or disintegration, a packet groupoid or Haar system, the selected
decomposable von Neumann algebra, a normal semifinite trace, a return trace,
the zero-mode projections, `K_s`, or a determinant.  Deninger's Section 11
does contain a genuine Haar convolution algebra, but it has a different
underlying inverse-limit group and no theorem maps it to the packets or the
Paper-7 analytic records.

There is one limited post-2024 salvage which must not be suppressed.
Morishita's continuous map to the Connes--Consani adelic space can be
restricted to Deninger's finite-kernel admissible subsystem.  This gives a
**newly derivable, continuous time-reversing intertwining map** with the
genuine Deninger system as its domain.  Global surjectivity is not stated or
proved, so it is not called a global factor map here.  The packetwise image
claim requires the `E_f` supplement in Section 7.3; Morishita's printed
full-space proof is insufficient.  After that supplement, every circle in
`Gamma_p` maps onto the same adelic circle `C_p`, so the transverse packet
multiplicity is collapsed packetwise.  The map is not an isomorphism or the
Paper-7 proxy bridge, and no measure, algebra, trace, or determinant is
transported.

Accordingly:

```text
source closed-point/packet/clock ownership       SOURCE_THEOREM
abstract normalized Haar on B_p                  DERIVABLE_NEW_LEMMA
counting measure on prime closed points          DERIVABLE_NEW_DEFINITION
Morishita E_f-restricted intertwining map         DERIVABLE_NEW_LEMMA
product Borel/Haar transport to Gamma_p          NOT_TESTABLE / no theorem found
counting measure -> proxy central m_p = 1         MODELING_CHOICE / no theorem found
packet -> M_p, tau_m, P_0, K_s, determinant      NOT_TESTABLE / no theorem found
```

Thus Phase 2 supplies **no source promotion** for
`DEN-WITT-PACKET-DECOMP-MASS-FAM`,
`DEN-WITT-PACKET-DECOMP-RETURN-DIST-M`, or
`DEN-WITT-PACKET-DECOMP-K0-M1`.  It does not prohibit a new enrichment
theorem; it records that no such theorem occurs in the audited sources.

## 2. Locks, lineage, and evidence vocabulary

The protocol and candidate records read for this audit had the following
hashes at freeze time:

| File | SHA-256 |
|---|---|
| `research_protocol.md` | `0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4` |
| `candidate_lock.md` | `0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa` |

Prior-session inputs were read, not silently inherited:

| Prior audit | SHA-256 | Use here |
|---|---|---|
| Paper 2 `phase2_deninger_source_audit.md` | `a4785e0fd56cb4e24211ea4d8f0e78a83ccdd6c942dc6572c87b2c1230ae521a` | claims and open topology/measure fields rechecked |
| Paper 2 `proof_audit.md` | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | normalized-Haar versus trace-coefficient boundary |
| Paper 2 `phase3_trace_no_go_audit.md` | `b4930e919bdaf6cf4a30667e3a2a0013603b8afe5492ced1cc0b3f3077968f18` | source-only trace no-go boundary |
| Paper 3 T0--T7 protocol | `e7c91c0aba9f34f979f36cb90046fbb04e41ba5cfca406d24dc51c88206e01f4` | same-object transport fields |

Evidence grades in this file mean:

- **E-A:** primary full text, hash-locked, read-integrity `PASS`, with an exact
  theorem/equation/physical-page locator;
- **E-B:** primary author survey, current arXiv preprint, or publisher/author
  metadata used within its proper scope;
- **E-C:** reproducible full-text keyword or official-index exclusion; useful
  for absence screening, never a universal non-existence theorem;
- **D:** a transparent standard consequence or restriction argument proved
  from source-owned data, but not stated by the source; and
- **M:** a Paper-7 modeling choice, not source evidence.

`SOURCE_THEOREM`, `DERIVABLE_NEW_LEMMA`, and `MODELING_CHOICE` are therefore
kept disjoint throughout.

## 3. Source manifestations and read integrity

| ID | Primary manifestation | Local file and SHA-256 | Integrity | Grade and role |
|---|---|---|---|---|
| `DEN-DYN-v4` | C. Deninger, *Dynamical systems for arithmetic schemes*, [arXiv:1807.06400v4](https://arxiv.org/abs/1807.06400v4), 7 Feb 2024 | `sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf`, `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `PASS`, 119/119/119 pages | **E-A**, load-bearing formulas and topology |
| `DEN-DYN-VOR` | [Indagationes Mathematicae 37(1), Jan 2026, 25--136, DOI 10.1016/j.indag.2024.05.007](https://www.sciencedirect.com/science/article/pii/S0019357724000491) | publisher metadata only; no separate local VOR PDF | open-access publisher record | **E-A** for bibliographic manifestation only; physical locators below refer to `DEN-DYN-v4` |
| `DEN-SURVEY-v1` | C. Deninger, *Primes, knots and periodic orbits*, [arXiv:2301.11643v1](https://arxiv.org/abs/2301.11643v1) | `sources/deninger-primes-knots-periodic-orbits.pdf`, `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | `PASS`, 16/16/16 pages | **E-B**, author corroboration and explicit compact-packet statement |
| `DEN-SHEAF-v1` | C. Deninger, *Rational Witt vectors and associated sheaves*, [arXiv:2508.05329v1](https://arxiv.org/abs/2508.05329v1) | `sources/deninger-rational-witt-vectors-associated-sheaves-v1.pdf`, `19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002` | `PASS`, 31/31/31 pages | **E-B**, later-update screen |
| `MOR-v5` | M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes--Consani's adelic spaces*, [arXiv:2508.15971v5](https://arxiv.org/abs/2508.15971v5), 21 Jan 2026 | `sources/morishita_2025_dynamical_systems_arithmetic_topology_v5.pdf`, `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | `PASS`, 26/26/26 pages | **E-B**, related-source same-object audit |

All page counts were checked by the ARS `pdf_read_preflight/1.0.0` script using
`pypdf`; all four sidecars record `PASS` with no warning.  “Physical PDF page”
below means the one-based reader page in these locked files.  Equation,
section, theorem, and printed-page numbers are supplied as independent
anchors.

## 4. Exact Deninger packet formulas and their owner

### 4.1 Coordinate choices and set parametrization

In `DEN-DYN-v4`, Section 5 begins by fixing two auxiliary data:

1. a point `x` of the normalization above the finite-residue-field point
   `x_0`; and
2. an injection `iota: mu(K) -> mu(C)`.

See physical PDF pp. 31--32, especially equation (32) and the paragraph
before (35).  With those choices, equation (37) gives an equivariant
surjection and equation (38) gives the `Q_{>0}`-equivariant bijection

```text
(Zhat_(p)^x / (N x_0)^Zhat) x_{p^Z} Q_{>0}  -->  C_{x_0}.
```

Exact locator: physical PDF p. 32, equations (37)--(38).  Equation (39) is a
second orbit/fibre presentation on physical p. 33.

For `Spec Z`, `x_0=(p)`, `N x_0=p`, and `deg(x_0)=1`.  Therefore, after the
same choices, (38) specializes to the equivariant **set** bijection

```text
B_p x_{p^Z} Q_{>0}  -->  C_p,
B_p = Zhat_(p)^x / p^Zhat.
```

Because `p^Z` dies in the quotient `B_p`, this yields the familiar chosen
set model `B_p x (Q_{>0}/p^Z)` and, after suspension, a chosen set model by
circles.  This specialization is **D**, not a source statement of a product
homeomorphism or measurable conjugacy.

The decisive ownership sentence occurs immediately after (39): Deninger
states that maps (37), (38), **and the fibration map** depend on the choices
of `x` and `iota`.  Only the map

```text
C_{x_0} -> Q_{>0}/p^Z
```

in equation (40) is declared canonical.  Exact locator: physical p. 33,
paragraph containing (40).

No transition formula between two pairs `(x,iota)` is stated there or later.
In particular, the source does not prove that every transition is continuous,
Borel, a compact-group automorphism/translation, or Haar preserving.

### 4.2 Flow, packet, period, and multiplicity

Section 6 defines the suspension and flow by

```text
X_0(E) = check X_0(C)_E x_{Q_{>0}} R_{>0},
phi^t[P_0,u] = [P_0,e^t u].
```

It defines `Gamma_{x_0}=C_{x_0} x_{Q_{>0}} R_{>0}` and uses (39) to give an
`R_{>0}`-equivariant bijection; it then states that every orbit in the packet
is `R_{>0}/(N x_0)^Z`.  Exact locator: `DEN-DYN-v4`, Section 6, physical
p. 38, paragraph before Theorem 6.1.

Theorem 5.2 states that all points with nontrivial `Q_{>0}` isotropy are the
disjoint union of the `C^E_{x_0}`, with isotropy `(N x_0)^Z`; for an
admissible class containing `E_f`, the full `C_{x_0}` is present.  Exact
locator: physical pp. 34--36, especially printed statement on p. 34,
equation (47).

Theorem 6.1 states that all points with nontrivial `R_{>0}` isotropy are the
disjoint union of the packets `Gamma^E_{x_0}`, again with isotropy
`(N x_0)^Z`.  The explanatory paragraph says:

- finite-residue-field points correspond bijectively to packets;
- a packet consists of periodic orbits of length `log N x_0`; and
- every periodic orbit lies in the packet of a unique `x_0`.

Exact locator: physical p. 39, Theorem 6.1 and the paragraph immediately
following it.

For `Spec Z`, the source-owned conclusion is therefore:

```text
one prime closed point (p) <-> one packet Gamma_p,
least additive period = log p,
repetition/isotropy group = p^Z.
```

It is **not** one prime closed point per individual circle.  The individual
circles form the transverse family within `Gamma_p`.

### 4.3 Topology, Borel structure, compactness, and Haar

The topology actually proved in `DEN-DYN-v4` is the pointwise-convergence,
quotient, and inductive-limit topology on the ambient spaces:

- Proposition 7.4: the original `X(C)` is clopen in `check X(C)`, every
  `F_q` is a homeomorphism, and `G` acts by homeomorphisms (physical p. 43);
- Propositions 7.5--7.7 and Corollaries 7.8--7.9: continuity of the `G` action
  and metrizability/separability/Hausdorff results in the stated affine or
  ample setting (physical pp. 44--45); and
- after Theorem 7.10, admissible `E`-subspaces are explicitly assigned the
  subspace, quotient, and inductive-limit topologies (physical p. 47).

Theorem 7.10 itself gives canonical **continuous bijections** for certain
injective-character sectors (physical p. 46), and its second remark warns
that those bijections are not homeomorphisms in general (physical p. 47).
This warning is global and is not by itself a proof that the packet map (38)
is non-homeomorphic.  It does, however, prevent treating a source-level
continuous bijection as a homeomorphism without a packet-specific theorem.

The author survey supplies the strongest compactness statement.  Theorem
4.2 says that the `Gamma_{x_0}` are pairwise disjoint **compact subsets**,
consist of periodic orbits of length `log N x_0`, and are fibred over the
compact group `Aut(Fbar_p^x)/Aut(Fbar_p)` with compact orbits as fibres.
Exact locator: `DEN-SURVEY-v1`, physical pp. 11--12, Theorem 4.2 and its
first explanatory paragraph.

Consequences must be typed separately:

| Claim | Status | Reason |
|---|---|---|
| `B_p` is an abstract compact Hausdorff group | `SOURCE_THEOREM` | v4 after (39); survey Theorem 4.2 |
| normalized Haar probability on abstract `B_p` exists and is unique | `DERIVABLE_NEW_LEMMA` | standard Haar theorem for compact groups |
| `B_p` is compact metrizable and has its standard Borel sigma-algebra | `DERIVABLE_NEW_LEMMA` | explicit profinite quotient by the compact/closed image `p^Zhat` |
| `Gamma_p` is compact | `SOURCE_THEOREM` | survey Theorem 4.2 |
| chosen packet map is a product homeomorphism | `NOT_TESTABLE` | source calls it a bijection and says its fibration depends on choices |
| chosen packet map is a Borel isomorphism | `NOT_TESTABLE` | no Borel theorem or transition maps found |
| Haar on `B_p` gives a choice-independent transverse measure on `Gamma_p` | `NOT_TESTABLE` | no measure transport/disintegration theorem found |
| `Gamma_p/R` has the compact-group topology of `B_p` | `NOT_TESTABLE` | no quotient-topology identification found |

Thus `Y_p=B_p x R/(log p)Z` with its product topology, product Borel
structure, and product/Haar measure is owned by
`DEN-WITT-PACKET-DECOMP-MASS-FAM`, not by `DEN-WITT-Z-FIN`.

## 5. Closed-point counting and the `m_p=1` provenance gate

The five frozen provenance fields resolve as follows.

| Gate | Finding | Evidence class |
|---|---|---|
| 1. closed point `(p)` to packet component | **PASS**: Theorems 5.2 and 6.1; survey Theorem 4.2 | `SOURCE_THEOREM`, E-A/E-B |
| 2. target-free counting measure on closed points | The countable set of prime closed points may be equipped with counting measure before mentioning any Euler product | `DERIVABLE_NEW_DEFINITION`, D |
| 3. transport to central trace weights of the same proxy algebra | no source central projections, algebra, trace, or transport map | `MODELING_CHOICE`, M |
| 4. duplication and coordinate-change compatibility | packet index counting is invariant under relabelling, but no theorem relates it to copied proxy components or choice-dependent packet charts | `OPEN / NOT_TESTABLE` |
| 5. status separation | packet bijection is source; counting is a new definition; central mass assignment is modeling | **CLOSED AS A CLASSIFICATION**, not as a transport theorem |

The source bijection makes “one unit per prime-indexed packet” a natural
arithmetic **ledger convention**.  It does not make `m_p=1` the coefficient
of a normal semifinite trace.  A counting measure on packet labels is not a
disintegration on each packet, and a central projection in the chosen direct
product algebra is not a source packet until a new map identifies the two.

Therefore `DEN-WITT-PACKET-DECOMP-K0-M1` remains `MODELING_CHOICE` at the
source gate.  This conclusion is independent of whether a later analytic
calculation proves an Euler product.

## 6. No Deninger theorem transports packets to the analytic owner

The requested transport fields give this matrix.

| Field | `DEN-WITT-Z-FIN` source status | Transport to Paper-7 proxy |
|---|---|---|
| underlying set / packet decomposition | proved at packet level | only an auxiliary-choice set parametrization; no frozen proxy map |
| topology and Borel structure | ambient topology and packet compactness proved | product topology/Borel transport absent |
| flow and clock | proved; `phi^t`, `p^Z`, `log p` | set-level chosen coordinates only; no full topological/measurable equivalence |
| transverse measure and disintegration | absent | absent |
| algebra and representation | absent for packets | selected by the proxy |
| trace positive cone and `L1` domain | absent for packets | selected by the proxy |
| test class and return distribution | absent | selected/proposed by the return-distribution record |
| zero-mode projection and analytic family | absent | selected by `K0-M1` |
| determinant convention and normalization | absent | selected/proposed by `K0-M1` |

This is not changed by Section 11 of `DEN-DYN-v4`.  Physical pp. 66--68
define a different locally compact, zero-dimensional inverse-limit group
`lim K^x`, normalize Haar by `mu(T mu_K)=1`, and define convolution in
equations (104)--(108).  Equations (111)--(114) and Lemma 11.2 construct a
`G`-equivariant **algebra homomorphism** into continuous functions.  The
source supplies no map from that inverse-limit group/algebra to `Gamma_p`,
`B_p`, `Y_p`, the circle translation representation, `tau_m`, `P_(0,p)`, or
`K_s`.  The map `varphi` is not a packet trace or determinant.

The survey's formula (9), physical p. 8, is likewise an analogy involving a
different smooth foliated system and a transverse index.  No transfer theorem
to the rational-Witt packets is stated.

## 7. Morishita v5: exact same-object boundary

### 7.1 The object is explicitly enlarged

Morishita equation (2.1.5) uses the full character set
`Hom_Gr(kappa(p)^x,C^x)` and equips the resulting `Xdot_Q(C)` with the
pointwise-convergence topology (physical p. 12).  Quotient and inductive-limit
topologies are then imposed in equations (2.1.9)--(2.1.12) (physical p. 13),
and the suspension gets the quotient topology in (2.2.1) (physical p. 14).

Remark 2.1.13 is explicit: Deninger's Section-4 conditions make the spaces
smaller and are intended to lead to the correct geometric model, but
Morishita omits that refinement for his comparison.  The reminder is repeated
after (2.2.2).  Hence define the typed owner

```text
MOR-UNREFINED-DEN-SYS-v5
```

for those full-character spaces.  It is not `DEN-WITT-Z-FIN`.

### 7.2 Theorems 2.2.8/2.2.9 do not transfer topology credit

Theorems 2.2.8 and 2.2.9 claim equivariant **homeomorphisms** from mapping
torus models to packets in `MOR-UNREFINED-DEN-SYS-v5` (physical pp. 16--18).
Their stated basis is (2.2.6), the asserted surjection (2.2.7), and “passing to
the inductive limit,” with a citation to Deninger Sections 5--7.  No separate
continuity, quotient-map, inverse-continuity, or compact-to-Hausdorff proof of
these packet maps is supplied.

The exact claimed objects are:

| Result | Domain case and claimed maps | Target topology |
|---|---|---|
| Theorem 2.2.8(1), physical pp. 16--17 | when the residue field at the chosen point is already `Fbar_p`: `Zhat_(p)^x x_{p^Z} Q_+ -> C_P` and `Zhat_(p)^x x_{p^Z} R_+ -> Gamma_P` | `C_P` is a fibre in Morishita's full-character inductive-limit space; `Gamma_P` is its suspension subset |
| Theorem 2.2.9(1), physical pp. 17--18 | for finite `K`, `N p=p^f`: `(Zhat_(p)^x/(N p)^Zhat) x_{p^Z} Q_+ -> C_p` and the analogous `R_+` mapping torus to `Gamma_p` | the same unrefined pointwise/quotient/inductive-limit/suspension topology fixed on physical pp. 12--14 |
| Theorem 2.2.9(2), physical p. 18 | fibres indexed by `Zhat_(p)^x/p^Zhat` are claimed homeomorphic to `R_+/(N p)^Z` | subspace topology inside that unrefined `Gamma_p` |

For `K=Q`, Theorem 2.2.9, not 2.2.8, is the directly relevant displayed
claim; it has `f=1` and `N p=p`.  The mapping-torus side carries its natural
profinite/usual quotient topology, whereas the target topology is inherited
from Morishita's enlarged construction.  Deninger v4 Sections 5--7 supply
equivariant bijections and ambient topology theorems, but do not state this
packet coordinate map as a homeomorphism.

There is also a mechanical domain mismatch.  Equation (2.2.7) claims that
`Zhat_(p)^x x N` surjects onto the **full** character space.  Its displayed
images have finite kernel, while the full space in (2.1.5) contains the
trivial character with infinite kernel.  Thus (2.2.7) cannot be surjective on
the unrefined object as written.  This is a `DERIVABLE_NEW_LEMMA` audit
witness, not a claim attributed to either author.

Conversely, the exact **fibrewise set image** of (2.2.7) is the finite-kernel
class `E_f`.  More precisely, after fixing the algebraically closed finite
residue field `Fbar_p` and the reference injection `chi_P`, a character of
`Fbar_p^x` has finite kernel exactly when its exponent in
`Zhat_(p)` is a unit times one positive integer; this is precisely the image
of `Zhat_(p)^x x N`.  This audit lemma says nothing about a global chart,
transition between choices, quotient topology, or inverse continuity.  It
repairs the fixed-fibre set domain only; it does not insert the missing
topological proof into Morishita's theorem or erase Deninger's explicit
choice dependence.  The homeomorphism wording therefore receives no
topology/Borel/Haar credit for `DEN-WITT-Z-FIN`.

The same full-character mismatch also leaves the printed proof of Theorem
3.6(2) incomplete.  On physical p. 25 the proof checks only that the exponent
adele `alpha=psi(P,P)` has `alpha_p=0`.  Membership in the standard adelic
circle `C_p`, however, also requires every finite coordinate away from `p` to
be nonzero so that the class can be normalized to coordinates `1`.  The
trivial character is an explicit full-space counterexample: it gives
`alpha_q=0` for every prime `q`, and multiplication by `Q^x` or
`Zhat^x` cannot change its zero-coordinate set.  Thus neither the printed
full-space statement nor its printed proof may be imported unchanged.  The
`E_f` packet claim below is a corrected new derivation.

### 7.3 Limited salvage: an `E_f`-restricted intertwining map

The separate map in Section 3 survives the domain correction.

- Morishita defines `psi(P,P)` by restricting `P` to roots of unity and proves
  it continuous and Frobenius/Galois equivariant in Lemma 3.4 (physical
  pp. 22--23).
- Passing to the inductive limit and suspension gives a continuous map; Lemma
  3.5 makes `Psi` flow-anti-equivariant and Galois-equivariant (physical
  pp. 23--24).
- Deninger's `E_f` is Frobenius- and Galois-stable, and v4 physical p. 47 fixes
  the admissible subspace, quotient, and inductive-limit topologies.

It follows by restriction and descent that `psi/Psi` defines a continuous,
time-reversing intertwining map on the genuine `E_f` subsystem.  This
continuity/intertwining conclusion does not yet identify the packet image.
That identification needs the following additional source-based check:

1. Deninger equation (35), physical p. 32, writes every fixed-fibre `E_f`
   character as `chi_x o ( )^a o ( )^n`, with
   `a in Zhat_(p)^x` and `n in N`.
2. Its exponent adele under `psi` has coordinate `0` at `p` and coordinates
   `n a_q != 0` for every `q != p`; only the finitely many prime divisors of
   `n` contribute nonunit valuations.
3. Multiplication by `n^(-1) in Q^x`, followed by the relevant element of
   `Zhat^x`, normalizes all `q != p` coordinates to `1` while the `p`
   coordinate remains `0`.  The positive real coordinate remains within the
   `R_+` orbit.  Hence the resulting adelic class lies in the standard `C_p`.
4. Flow anti-equivariance then makes the image of that entire source circle
   exactly the `R_+` orbit `C_p`, hence orbitwise onto.

Steps 1--4 prove only the `E_f` restriction and only packetwise onto.  They do
not repair Morishita's unrefined theorem, establish global surjectivity, or
transport the transverse base.  The corrected conclusion is typed as

```text
MOR-PSI-RESTRICT-EF
status: DERIVABLE_NEW_LEMMA
domain: DEN-WITT-Z-FIN (E_f subsystem)
target: Connes--Consani adelic system
transported fields: topology/continuity, flow up to time reversal,
                    prime label and absolute period
surjectivity: packetwise onto C_p only; no global onto claim
```

This is a real intertwining morphism and so the audit does **not** say that no
same-object topological map exists.  It remains far below the Paper-7
transport gate.

Morishita Theorem 3.6(2), physical p. 25, prints the corresponding claim for
an arbitrary full-space circle, but the audit credits it only after the above
`E_f` repair.  On that corrected domain, the image of every circle in the
packet is the same `C_p`; distinct transverse circles therefore have the same
target orbit.  The map has packetwise transverse-collapsing behaviour; it is
not a packet homeomorphism and not a map to `Y_p` or `M_p`.

The full-text audit found no packet groupoid, Haar system, Borel
disintegration, transverse measure, von Neumann representation, normal
semifinite trace, trace ideal, zero-mode family, or determinant transport.
Occurrences of “trace formula” and “determinant” are historical introduction
or bibliography references only.  Therefore `MOR-PSI-RESTRICT-EF` cannot
transport `m_p=1`, `tau_m`, the return distribution, `P_0`, `K_s`, or a
determinant.

## 8. Later-update screen through 2026-08-14

The current [arXiv author search for Christopher Deninger](https://arxiv.org/search/?query=Christopher+Deninger&searchtype=author&abstracts=show&order=-announced_date_first&size=50),
the [official Münster recent-publications record](https://www.uni-muenster.de/FB10srvi/persdb/MM-member.php?id=62),
the author [publication page](https://www.uni-muenster.de/Arithm/deninger/publ.shtml),
arXiv version histories, and the publisher record were checked at the cutoff.

| Update | Current version/date at cutoff | Relevance decision |
|---|---|---|
| `DEN-DYN` | arXiv v4, 7 Feb 2024; publisher issue Jan 2026 | included; no arXiv v5 exists |
| Deninger, *Rational Witt vectors and associated sheaves* | [2508.05329v1](https://arxiv.org/abs/2508.05329v1), 7 Aug 2025 | included for screen: physical pp. 1--2 cite the dynamical construction, mention its shortcomings, and motivate improved Witt/sheaf understanding; the paper proves sheaf/correspondence results, not packet topology, groupoids, measures, traces, or determinants |
| Deninger, *Is there a Birch and Swinnerton-Dyer conjecture for Dedekind zeta functions?* | [2504.15767v3](https://arxiv.org/abs/2504.15767v3), 1 Apr 2026 | excluded by title/abstract/full-text screen: conditional cohomological vector-space question, no packet bridge |
| Deninger--Kamlesh, *A remark on the vanishing of Higgs fields...* | [2508.13685v3](https://arxiv.org/abs/2508.13685v3), 30 Mar 2026 | excluded: p-adic Simpson correspondence, no packet bridge |
| Nikzad--Deninger, *Invariant Functions on p-divisible Groups and the p-adic Corona Problem II* | [2608.11943v1](https://arxiv.org/abs/2608.11943v1), 12 Aug 2026 | excluded: p-divisible-group dimension extension, no packet bridge |
| Morishita comparison | [2508.15971v5](https://arxiv.org/abs/2508.15971v5), 21 Jan 2026 | included and audited in Section 7; limited intertwining-map salvage only |

`DEN-SHEAF-v1` was searched in full.  Its uses of “determinant” are Hankel or
finite-module determinants in rational-Witt algebra; they are not flow traces
or packet determinants.  The other excluded current papers were screened on
their official arXiv abstract/full-text manifestations.  No later source
found in this bounded primary-source search supplies the missing analytic
transport theorem.

## 9. Source theorem / derivation / modeling classification

| Item | Classification | Owner |
|---|---|---|
| packet decomposition over finite-residue-field points | `SOURCE_THEOREM` | `DEN-WITT-Z-FIN` |
| isotropy `(N x_0)^Z`, repetitions, least period `log N x_0` | `SOURCE_THEOREM` | `DEN-WITT-Z-FIN` |
| compact packet and compact abstract base group | `SOURCE_THEOREM` | `DEN-WITT-Z-FIN` |
| chosen `Spec Z` set model `B_p x R/(log p)Z` | `DERIVABLE_NEW_LEMMA`, choice dependent | chosen chart only |
| normalized Haar on abstract `B_p` | `DERIVABLE_NEW_LEMMA` | abstract group `B_p` |
| counting measure on prime closed points | `DERIVABLE_NEW_DEFINITION` | closed-point ledger |
| `E_f`-restricted Morishita intertwining map | `DERIVABLE_NEW_LEMMA` | typed source-to-adelic morphism; packetwise onto only |
| product topology/Borel structure on `Y_p` | `MODELING_CHOICE` | mass-family proxy |
| product/Haar disintegration on `Y_p` | `MODELING_CHOICE` | mass-family proxy |
| `m_p=1` as central trace mass | `MODELING_CHOICE` | `K0-M1` until a new theorem |
| decomposable `M_p`, representation, and `tau_m` | `MODELING_CHOICE` | mass-family proxy |
| return distribution | `MODELING_CHOICE` plus later Paper-7 theorem target | return-distribution record |
| `P_(0,p)`, `K_s`, trace determinant | `MODELING_CHOICE` plus later Paper-7 theorem targets | `K0-M1` |

## 10. T0--T7 source-to-proxy transport matrix

Statuses concern transport from `DEN-WITT-Z-FIN` to the Paper-7 proxy, not
future within-proxy proofs.

| Gate | Deninger evidence | Morishita salvage | Transport verdict |
|---|---|---|---|
| `T0` object identity | original and proxy have distinct IDs | a genuine restricted morphism exists, but its target is the adelic space, not the proxy | **FAIL for proxy transport**; no coordinatewise borrowing |
| `T1` classical ledger | packet, repetitions, prime label, clock intrinsic; no trace amplitude | prime label/period transported but transverse circles collapsed | **PARTIAL** |
| `T2` trace definition | no packet trace or explicit trace test class | none | **NOT_TESTABLE** |
| `T3` analytic ledger | no packet operator/domain/spectrum tied to a trace | none transported | **NOT_TESTABLE** |
| `T4` theorem extent | exact set/topological packet theorems only | continuous time-reversing intertwiner, packetwise onto only, not an analytic identity | **SCOPED ONLY** |
| `T5` coefficient provenance | period is sourced; central mass, density, sign, phase, determinant coefficient are not | no coefficient transport | **FAIL for `m_p` and analytic weights** |
| `T6` clock/normalization | `log p` and `p^Z` sourced | absolute clock survives with time reversal; no Fourier/trace/determinant normalization | **PARTIAL** |
| `T7` arithmetic promotion | rational-prime packet support and repetitions sourced | prime label reaches `C_p`; no prime-power analytic weights | **PARTIAL; no determinant promotion** |

The matrix permits inherited `A1_WEAK` for the original packet structure and
does not supply measured A2, A3, A4, or Route-B evidence.  A future theorem
could populate the missing fields, but neither a selected proxy construction
nor the Morishita intertwining map does so by itself.

## 11. Reproducible search and verification log

### Local verification commands

Run from the repository root:

```bash
sha256sum papers/7-packet-groupoid/notes/sources/*.pdf
pdfinfo papers/7-packet-groupoid/notes/sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf
pdfinfo papers/7-packet-groupoid/notes/sources/deninger-primes-knots-periodic-orbits.pdf
pdfinfo papers/7-packet-groupoid/notes/sources/deninger-rational-witt-vectors-associated-sheaves-v1.pdf
pdfinfo papers/7-packet-groupoid/notes/sources/morishita_2025_dynamical_systems_arithmetic_topology_v5.pdf
/tmp/paper7-pdf-preflight-venv/bin/python \
  /root/.codex/plugins/cache/ars-codex/ars-codex/0.1.24/skills/academic-research-suite/ars/scripts/pdf_read_preflight.py \
  INPUT.pdf --output INPUT.preflight.json
pdftotext -f 31 -l 39 -layout \
  papers/7-packet-groupoid/notes/sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf -
pdftotext -f 42 -l 47 -layout \
  papers/7-packet-groupoid/notes/sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf -
pdftotext -f 66 -l 68 -layout \
  papers/7-packet-groupoid/notes/sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf -
pdftotext -f 11 -l 12 -layout \
  papers/7-packet-groupoid/notes/sources/deninger-primes-knots-periodic-orbits.pdf -
pdftotext -f 12 -l 18 -layout \
  papers/7-packet-groupoid/notes/sources/morishita_2025_dynamical_systems_arithmetic_topology_v5.pdf -
pdftotext -f 22 -l 25 -layout \
  papers/7-packet-groupoid/notes/sources/morishita_2025_dynamical_systems_arithmetic_topology_v5.pdf -
```

Full-text negative screens used case-insensitive searches for:

```text
groupoid, Haar, measure, Borel, disintegration, von Neumann, semifinite,
trace ideal, trace class, zero mode, return distribution, Fredholm,
Ruelle determinant, decomposable
```

Negative keyword results were manually checked for false positives.  For
example, Deninger Section 11 contains “Haar” but on a different inverse-limit
group; Morishita contains historical “trace formula” references but no
transport theorem.

### Primary-source web queries

The following bounded queries were run on 2026-08-14; only arXiv, author,
institutional, or publisher results were admitted:

```text
site:arxiv.org/abs/1807.06400 Deninger dynamical systems arithmetic schemes v4
site:arxiv.org/abs/2508.05329 Deninger rational Witt vectors associated sheaves
site:arxiv.org Deninger rational Witt packet periodic orbit 2025 2026
site:arxiv.org "Deninger's foliated dynamical systems"
site:arxiv.org "Dynamical systems for arithmetic schemes" groupoid trace
site:uni-muenster.de Christopher Deninger publications 2025 2026 rational Witt
site:sciencedirect.com/science/article/pii/S0019357724000491 "25-136"
```

Direct version-history and currentness endpoints:

```text
https://arxiv.org/abs/1807.06400
https://arxiv.org/abs/2508.05329
https://arxiv.org/abs/2508.15971v5
https://arxiv.org/abs/2504.15767
https://arxiv.org/abs/2508.13685
https://arxiv.org/abs/2608.11943
https://arxiv.org/search/?query=Christopher+Deninger&searchtype=author&abstracts=show&order=-announced_date_first&size=50
https://www.uni-muenster.de/FB10srvi/persdb/MM-member.php?id=62
https://www.uni-muenster.de/Arithm/deninger/publ.shtml
https://www.sciencedirect.com/science/article/pii/S0019357724000491
```

Search saturation for this Phase-2 question was reached when the current
author index, exact-title/citation search, later rational-Witt paper, and the
only directly related 2026 comparison all failed to provide any
measure/operator/trace/determinant transport.  The search then stopped in
accordance with the frozen protocol.

## 12. Phase-2 handoff

The source audit closes P7-9's bibliographic ownership fields as follows:

- packet, period, repetition, compactness: sourced;
- product topology/Borel and choice transitions: unresolved;
- normalized abstract Haar and prime-index counting: derivable but not
  transported;
- a limited Deninger-to-adelic continuous intertwiner: derivable,
  packetwise onto, and explicitly transverse-collapsing on each packet, with
  no global-surjectivity claim;
- algebra, representation, trace domain, return trace, zero mode, analytic
  family, and determinant: absent from the source bridge.

No downstream source search, proof synthesis, or manuscript drafting is part
of this deliverable.
