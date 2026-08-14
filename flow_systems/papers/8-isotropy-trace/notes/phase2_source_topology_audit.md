# Paper 8 Phase-2 primary-source topology and same-object audit

Audit date: 2026-08-14 (Asia/Shanghai)  
Evidence cutoff: 2026-08-14  
Method: ARS deep-research/source-verification; authoritative primary records
and locally retained primary full texts only  
Decision: **REVISE — no fatal source obstruction, but the packet-level P8-1
LCH gate remains `NOT_TESTABLE`; the one-orbit fallback passes**

`REVISE` is a research-gate verdict, not a request to edit the Phase-1 locks.
No active lock, manuscript, operator proof, or Route record was changed in
this audit.

## 1. Exact Phase-1 byte lock

The active inputs were re-hashed before source work:

| Artifact | SHA-256 verified |
|---|---|
| `notes/research_protocol.md` | `127d80d98532ef150df4c74706c44047c3509c14c3498322d6dee09ed81f98c2` |
| `notes/candidate_lock.md` | `25c37f5a81ad95640f31e4d7f13b0bb328b4cf5735f31c70ce3e30b0f99a699b` |
| `notes/phase1_amendment.md` | `2a5f721ed2e61495f4ccaad1095e571ce74c069e70e59507f97dd1307ecb51e6` |
| `notes/phase1_source_relock.md` | `9829bc0afa4f9d16a9581fc4eaaf6733437f4bd0a6143af29300985e2a8c6714` |

The retained-source manifest is
`notes/sources/phase2_topology_source_manifest.md`, SHA-256
`ca9c7f7527bd1b523fb8dc98bf541d157601bd97b9458fb9d50b712bd5a4c58b`.
Its independent checksum file is
`notes/sources/phase2_topology_sources.sha256`, SHA-256
`1d17d442972502bda760e84e397f368d6e57b937ec493426c4fd50a4df2f0210`.
All three retained PDFs and their same-stem preflight sidecars pass the
checksum file.

Classification vocabulary in this report is strict:

- `SOURCE_THEOREM`: printed in a retained primary manifestation at the cited
  locator;
- `DERIVABLE_NEW_LEMMA`: proved below from source theorems plus elementary
  topology/algebra, and not attributed to the source author;
- `OPEN`: not established or refuted by the audited sources;
- `NOT_TESTABLE`: a downstream record cannot presently be formulated under
  its frozen hypotheses because an upstream gate is `OPEN`.

## 2. Executive gate matrix

Here `Xcheck_0(C)_{E_f}` denotes Deninger's checked pre-suspension space and
`X_0^{E_f}=Xcheck_0(C)_{E_f} x_{Q_+} R_+` the actual suspension.  They must not
be conflated.

| Claim/gate | Classification | Exact support or reason | Consequence |
|---|---|---|---|
| The genuine `E_f` prime packet `Gamma_p` is compact and its orbit fibres are compact | `SOURCE_THEOREM` | Deninger survey v1, Theorem 4.2, physical pp. 11--12 | compactness closes, but compact does not imply Hausdorff in the ambient category |
| Every point of `Gamma_p` has exact stabilizer `p^Z` in multiplicative time, equivalently `(log p)Z` in additive time | `SOURCE_THEOREM` | Deninger v4, Theorem 6.1, physical p. 39 | common clock and exact kernel close |
| `Xcheck_0(C)_{E_f}` is Hausdorff for `Spec Z` | `SOURCE_THEOREM` | Deninger v4, Corollary 7.9, physical p. 45, plus the admissible-`E` extension on physical p. 47 | the space *before* suspension is Hausdorff |
| `Xcheck_0(C)_{E_f}`, the suspension `X_0^{E_f}`, and each packet `Gamma_p` are second countable | `DERIVABLE_NEW_LEMMA` | Proposition 7.4, Proposition 7.6, Corollary 7.8, and the `E` paragraph on physical pp. 43--47; proof in Section 4 below | packet countability closes |
| The suspension `X_0^{E_f}` is Hausdorff | `OPEN` | no retained theorem proves the diagonal `Q_+` orbit relation closed/proper; Hausdorffness of the product before quotient is insufficient | ambient suspension separation remains open |
| Each packet `Gamma_p` is Hausdorff, hence LCH in the frozen groupoid sense | `OPEN`; packet groupoid `NOT_TESTABLE` | compactness is printed, but neither a Hausdorff packet chart nor a closed restricted equivalence relation is printed or derived | `Gamma_p rtimes R` cannot yet receive packet-level LCH groupoid credit |
| `K_p=R/(log p)Z` acts continuously and freely on `Gamma_p` | `DERIVABLE_NEW_LEMMA` | continuity of the source flow plus exact common stabilizer | the intrinsic quotient is legally defined without a `B_p` identification |
| `Q_p=Gamma_p/K_p` is compact and second countable | `DERIVABLE_NEW_LEMMA` | continuous compact image; the compact-group quotient map is open | these two quotient properties close |
| `Q_p` is Hausdorff or `q_p` is a locally trivial principal bundle | `OPEN` | freeness of a compact action on a possibly non-Hausdorff domain does not supply these conclusions | no packet measure-lifting or product-chart promotion follows |
| Every actual inherited `E_f` orbit is homeomorphic, flow-anti-equivariantly, to Morishita's `C_p=R_+/p^Z` | `DERIVABLE_NEW_LEMMA` | corrected proof in Section 6 below | orbit `T1/T2` close; the orbit is compact Hausdorff, second countable, and LCH |
| `Gamma_p` is homeomorphic/Borel-isomorphic to `B_p x R/(log p)Z` | `OPEN` | Deninger's displayed packet maps are set bijections; Morishita omits `E_f` and his printed full-character parametrization has a scope defect | the product proxy remains separate |
| Deninger/Morishita select a transverse probability, packet trace, or cross-prime mass | `OPEN` / absent source field | none of the retained source statements makes such a selection | no analytic `T4--T7` bridge |

The strongest source-topology result is therefore asymmetric: **packet
compactness and second countability are closed, packet Hausdorffness is not;
the single-orbit topology is fully closed.**

## 3. What Deninger's primary text actually supplies

### 3.1 Packet, clock, and compactness

Deninger v4 defines the suspension and the packet
`Gamma_x0=C_x0 x_{Q_+} R_+` on physical p. 38.  The displayed parametrization
there is expressly an `R_+`-**bijection**, not a homeomorphism.  Theorem 6.1
on physical p. 39 states that the nontrivially periodic set is the disjoint
union of the packets and that every packet point has isotropy `N x_0^Z`.
For `X_0=Spec Z` and `x_0=(p)`, this is `p^Z`, so additive least period is
`L_p=log p`.

Compactness comes from a second primary manifestation, not from silently
topologizing the set bijection: Deninger's survey Theorem 4.2 (physical
pp. 11--12) calls the `Gamma_x0` compact subsets, pairwise disjoint, and says
their fibres over the compact group are compact periodic orbits.  This closes
compactness of both a packet and each orbit but does not add Hausdorffness.

### 3.2 The exact ambient-topology split

For affine arithmetic schemes, Deninger v4 Proposition 7.6 (physical p. 44)
gives the initial point space a metric and makes it second countable and
separable for separable `C`.  Proposition 7.7 and Corollary 7.8 (physical
pp. 44--45) give the compact-Galois quotient a metric, hence Hausdorffness and
second countability.  Proposition 7.4 (physical p. 43) says the Frobenius
stages are open and Frobenius maps on the colimit are homeomorphisms.
Corollary 7.9 (physical p. 45) makes the checked pre-suspension spaces
Hausdorff whenever `X_0` has an ample invertible sheaf, as `Spec Z` does.
Finally, the paragraph after Theorem 7.10 on physical p. 47 says the
admissible-`E` spaces carry the corresponding subspace/colimit topologies and
that all preceding Section-7 results remain valid after the `E` restriction.
Thus these statements apply to `E_f`.

None of those results says that the subsequent diagonal quotient

```text
X_0^{E_f} = (Xcheck_0(C)_{E_f} x R_+)/Q_+
```

is Hausdorff.  A quotient of a Hausdorff space by a group action is Hausdorff
only after a separation condition such as closedness of the orbit relation;
the retained Deninger/Morishita texts supply no such packet-level result.
Accordingly, this audit does not upgrade a compact packet to compact
Hausdorff merely by convention.

### 3.3 Set disjoint union is not a topological coproduct

The disjoint-union sign in Theorem 6.1 is a decomposition of the periodic
**set**.  More generally, Theorem 7.10 on physical p. 46 gives canonical maps
from displayed coproducts that are continuous bijections, while Remark 2 on
physical p. 47 warns that they are not homeomorphisms in general.  Therefore:

- the inherited all-prime periodic subspace is not source-verified as the
  topological coproduct of the individual `Gamma_p`;
- each per-prime groupoid and a newly chosen topological coproduct remain
  different typed objects; and
- compact support on a chosen coproduct cannot be inferred from the inherited
  global source topology.

## 4. New second-countability lemma

**Lemma (`DERIVABLE_NEW_LEMMA`).**  For `Spec Z`, the genuine `E_f`
pre-suspension, suspension, each prime packet, and `Q_p` are second countable.

**Proof.**  By Proposition 7.6, Corollary 7.8, and the physical-p. 47
admissible-`E` paragraph, the initial quotient stage for `E_f` is a separable
metric space and hence second countable.  The checked space is the union over
`n in N` of the open Frobenius stages.  Proposition 7.4 makes each stage
homeomorphic to the initial stage.  A countable union of open subspaces with
countable bases has the union of those bases as a countable base, so
`Xcheck_0(C)_{E_f}` is second countable.

Its product with `R_+` is second countable.  The quotient map for the
`Q_+` action is open: the saturation of an open set is the union of its group
translates.  Images of a countable base under an open quotient map form a
countable base, so `X_0^{E_f}` is second countable.  Every `Gamma_p` is a
subspace and hence second countable.  Finally, the `K_p` quotient map is open
for the same reason, so `Q_p` is second countable.  QED.

This proof establishes no Hausdorff statement and uses no packet product
chart.

## 5. The intrinsic compact quotient `Q_p`

Write the source flow additively and put `L_p=log p`.  Theorem 6.1 says the
stabilizer of every `x in Gamma_p` is exactly `L_p Z`.  Hence the action has
that common kernel and factors through

```text
K_p = R/(L_p Z).
```

The quotient homomorphism `R -> K_p` is open.  Descending the continuous
`R` action along this open quotient gives a continuous `K_p` action.  Exactness
of the stabilizer makes the descended action free.  These are
`DERIVABLE_NEW_LEMMA` conclusions, not source-attributed definitions.

The orbit-space quotient

```text
q_p: Gamma_p -> Q_p=Gamma_p/K_p
```

is therefore a legitimate intrinsic new object.  Since `Gamma_p` is compact,
`Q_p` is compact; Section 4 proves it second countable.  But the usual compact
group theorem yielding a Hausdorff quotient starts from a Hausdorff domain.
Because packet Hausdorffness remains `OPEN`, `Q_p` Hausdorffness also remains
`OPEN`.  Freeness alone does not prove local triviality, a `B_p`
identification, or a transverse-measure theorem.

## 6. Corrected genuine-`E_f` one-orbit homeomorphism

### 6.1 Why the printed enlarged-object statement cannot be imported

Morishita v5 Remark 2.1.13 (physical p. 13) explicitly omits Deninger's
character refinement.  Consequently Morishita's printed ambient object
contains every character in `Hom(Fbar_p^x,C^x)`, including characters with
infinite kernel, and is not the frozen `E_f` object.

There is also a concrete printed-scope defect.  Equation (2.2.7) and Theorem
2.2.8 on physical pp. 16--17 treat the map from
`Zhat_(p)^x x N` as surjective onto all such characters.  Every character in
that displayed image has finite kernel, whereas the trivial character is
allowed in the stated full-character codomain and has infinite kernel.
Thus the asserted surjectivity, literally on the enlarged domain, is false.
Likewise, the proof of Theorem 3.6(2) on physical p. 25 checks only that the
associated finite adele has zero `p`-component.  Membership in the target
prime orbit also requires every `q != p` component to be nonzero up to the
adelic quotient; the trivial character gives zero at every finite component.

Therefore neither Morishita's packet homeomorphism nor his full-domain orbit
claim is legal same-object evidence for `E_f`.  The following restricted proof
uses only the parts that survive restriction.

### 6.2 Restricted theorem and proof

**Lemma (`DERIVABLE_NEW_LEMMA`; exact scope).**  Let `gamma` be any actual
periodic orbit in Deninger's `Spec Z`, finite-kernel subsystem `E_f`, lying in
`Gamma_p`.  Restrict Morishita's construction to that subsystem.  The
restricted map sends `gamma` continuously and flow-anti-equivariantly onto
the adelic prime circle `C_p`; it is a homeomorphism.  It preserves the
unoriented clock `log p` and reverses flow orientation.  It says nothing about
the topology transverse to `gamma`.

**Proof.**

1. Morishita Lemma 3.4 (physical p. 23) proves continuity/equivariance of the
   character restriction map, and Lemma 3.5 (physical p. 24) proves that its
   suspension is continuous and `R_+`-anti-equivariant.  Restriction to
   Deninger's `E_f` subspace preserves continuity; equivalently, the
   restricted pre-suspension map descends directly through the restricted
   quotient.
2. Fix a point above `p`.  Deninger v4 equation (35), physical p. 32, writes
   its finite-kernel residue-field character as
   `chi_P o ( )^a o ( )^n`, with `a in Zhat_(p)^x` and `n in N`.  Under
   Morishita's map to `A_f`, the exponent adele `b` satisfies `b_p=0`; for
   every `q != p`, `b_q=n a_q` is nonzero in `Q_q`.
3. Multiply diagonally by `n^{-1} in Q^x` and on the right by the profinite
   unit whose `q`-component is `a_q^{-1}` for `q != p` (take its
   `p`-component to be `1`).  The resulting representative has finite
   components `0` at `p` and `1` at every `q != p`.  It is therefore in the
   orbit `C_p` defined by Morishita equation (1.1.5), physical p. 5.
4. Flow anti-equivariance now maps the whole source orbit onto the whole
   target orbit.  Deninger Theorem 6.1 gives source stabilizer `p^Z`;
   Morishita equation (1.1.5) identifies the target with `R_+/p^Z`, with the
   same stabilizer.  An equivariant or anti-equivariant map between these
   homogeneous orbits with equal stabilizer is injective.  It is therefore a
   continuous bijection.
5. Deninger survey Theorem 4.2 says the source orbit is compact.  The target
   `R_+/p^Z` is a Hausdorff circle.  A continuous bijection from a compact
   space to a Hausdorff space is a homeomorphism.  QED.

This proof closes only the inherited topology and clock on one actual orbit.
It does **not** prove a packet map injective, a packet chart, a transverse
Borel isomorphism, measure transport, groupoid equivalence, Haar transport,
representation transport, or trace transport.  Many distinct source orbits
map to the same `C_p`, so the map deliberately forgets the transverse packet
coordinate.

## 7. T0--T7 same-object audit

| Field | Corrected one-orbit bridge | Packet / `Q_p` status |
|---|---|---|
| `T0` object identity | **PASS, `DERIVABLE_NEW_LEMMA`**: domain is explicitly the actual `E_f` restriction, not Morishita's enlarged object | actual `Gamma_p` is source-owned; `Q_p` and the action groupoid remain typed new definitions |
| `T1` topology/Borel | **PASS on one orbit only**: compact-to-Hausdorff proof gives the inherited-orbit homeomorphism | packet compact + second countable; packet and `Q_p` Hausdorffness `OPEN`; no `B_p` chart |
| `T2` flow/clock | **PASS on one orbit**: anti-intertwining and common stabilizer `p^Z`, hence length `log p` | source flow and common clock pass; no global product-coordinate transport |
| `T3` groupoid/Haar | **NO CREDIT in this audit**: the orbit homeomorphism alone does not choose completion or prove a packet Haar theorem | packet groupoid LCH gate `NOT_TESTABLE` until Hausdorffness closes |
| `T4` measure | **NO CREDIT**: no transverse measure exists on a single-orbit statement | no source-selected probability on `Q_p`; no packet or cross-prime mass |
| `T5` representation/trace | **NO CREDIT** | absent from Deninger/Morishita packet sources |
| `T6` test algebra/formula | **NO CREDIT** | absent from this topology bridge |
| `T7` arithmetic promotion | **NO CREDIT** | closed-point identity and clock do not select analytic component masses |

Paper 7 cannot supply a missing field in this table: its proxy/product
calculation is a separate typed object.  Morishita supplies the limited
one-orbit `T1/T2` lemma after correction, but no packet analytic bridge.

## 8. Haar-normalization boundary

The sources use multiplicative time `r in R_+`; the frozen protocol uses
additive time `t=log r`.  These roles must remain separate:

- `dt` is Lebesgue Haar on the acting group `R` and is the candidate arrow
  Haar coordinate for an action groupoid;
- its quotient on `R/(L_p Z)` is **length Haar** `du`, with total mass `L_p`;
- `du/L_p` is probability Haar on that orbit; and
- neither choice is a transverse probability on `Q_p`.

Dividing by `L_p` changes the normalization and must be applied to every
compared orbit-side expression together.  Packet compactness and compactness
of `Q_p` do not select a probability on `Q_p`, and the source supplies no
cross-prime mass sequence.

## 9. Currentness and later-source screen

The search was bounded to official arXiv author/version records, Deninger's
University of Muenster publication pages, Morishita's Kyushu University
profile, the Münster Journal page, and the official Elsevier article record.
It was completed on the evidence cutoff.

- Deninger's dynamical-systems preprint remains arXiv v4 (2024-02-07); the
  journal record is *Indagationes Mathematicae* 37(1), January 2026,
  pp. 25--136, DOI `10.1016/j.indag.2024.05.007`.
- Deninger's survey remains arXiv v1 and is recorded as a 2024 Scuola Normale
  Superiore chapter.
- Morishita remains arXiv v5 (2026-01-21); his institutional profile, updated
  2026-06-18, records the reviewed 2026 journal paper.
- The later Deninger Rational-Witt-sheaf, Dedekind-BSD, and p-adic-Simpson
  papers do not state a packet-topology update.  Morishita's separate smooth
  3-dimensional-FDS determinant paper concerns another object.  They were not
  retained because the task requires only load-bearing full texts.

No later primary source located through 2026-08-14 closes packet
Hausdorffness, a `B_p` packet chart, or a source-selected transverse measure.
This is a bounded search conclusion, not a universal nonexistence theorem.

## 10. Remaining Phase-2 obligations and final gate

### Packet track

To reopen packet-level P8-1, a later audit must produce one of the following
without coordinate splicing:

1. a primary theorem or a new proof that the restricted diagonal orbit
   relation defining `Gamma_p` is closed, or an actual continuous packet
   parametrization whose target is compact Hausdorff and whose inverse is
   proved continuous;
2. only after that, the exact theorem proving `Q_p` Hausdorff and any claimed
   principal-bundle/local-triviality property;
3. an explicit, source-owned rule for any transverse probability, kept
   distinct from orbit Haar; and
4. separate groupoid/Haar/completion theorems.  None is supplied by the
   topology sources audited here.

Until item 1 closes, the per-prime packet action groupoid is
**`NOT_TESTABLE` under the frozen LCH hypothesis**.  The result is not a proof
that packet Hausdorffness fails.

### Orbit track

The corrected `E_f` lemma proves that every actual source orbit is the
compact Hausdorff second-countable circle `R/(L_p Z)` with the inherited
topology and correct clock.  The **one-orbit source-topology gate is `PASS`**,
so a separately source-verified orbit groupoid/imprimitivity analysis may
proceed.  It must retain `dt`, `du`, and `du/L_p` as distinct normalizations
and may not promote orbit results to a canonical packet trace.

### Final status

```text
packet compactness                 SOURCE_THEOREM / PASS
packet second countability         DERIVABLE_NEW_LEMMA / PASS
packet Hausdorff-LCH                OPEN -> packet P8-1 NOT_TESTABLE
K_p free continuous action         DERIVABLE_NEW_LEMMA / PASS
Q_p compact + second countable      DERIVABLE_NEW_LEMMA / PASS
Q_p Hausdorff/local triviality      OPEN
genuine E_f one-orbit bridge        DERIVABLE_NEW_LEMMA / PASS (T1/T2 only)
packet analytic / measure bridge    NOT_TESTABLE / NO CREDIT
```

No P8-2--P8-9 operator theorem, determinant, Route-A credit, or Route-B
promotion is asserted by this source/topology audit.
