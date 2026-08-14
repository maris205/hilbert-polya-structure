# Paper 8 Phase-1 source and same-object feasibility audit

Audit date: 2026-08-14  
Scope: retained local primary materials only; no web search, Phase-2 theorem
search, proof credit, or edit to either active lock  
Decision: **REVISE BEFORE PHASE 2 — NO FATAL SOURCE OBSTRUCTION**

## 1. Exact-byte scope

| Locked input | SHA-256 verified |
|---|---|
| `notes/research_protocol.md` | `51c85aae8262d6fb8597d49e6c23a1926ebb24ee3c3429d996228565b4d7a547` |
| `notes/candidate_lock.md` | `d1d11519bd8661be1a62f5cf7bdc34e14a929a79776c52001b2a0d362082cc8a` |

Primary manifestations inspected:

| Source | Local SHA-256 | Read-integrity status |
|---|---|---|
| Deninger, *Dynamical systems for arithmetic schemes*, v4 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `PASS`, 119/119/119 pages |
| Deninger, *Primes, knots and periodic orbits*, v1 | `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | `PASS`, 16/16/16 pages |
| Morishita, *On a relation between Deninger's foliated dynamical systems and Connes--Consani's adelic spaces*, v5 | `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | `PASS`, 26/26/26 pages |

The limited `E_f` correction below was checked against the existing Paper-7
source audit, SHA-256
`a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53`.
It is not imported as source authorship or as Paper-8 proof credit.

## 2. Executive source verdict

Deninger supplies the actual finite-kernel packet, its continuous flow, compact
packet, common exact isotropy, prime label, period, and repetitions.  These data
are enough to define a **topological** transformation groupoid
`Gamma_p rtimes R`.  The retained text does not yet prove the inherited packet
topology Hausdorff, a packet product chart, a transverse measure, or any
groupoid representation or trace.  Consequently the usual locally compact
Hausdorff groupoid/C-star theorem package is not yet available for the packet.

There is nevertheless no fatal obstruction.  Packet second countability has a
short source-based derivation, and a single actual orbit has a viable, narrowly
typed topology bridge through Morishita after the `E_f` domain correction.  The
locks require revision because they currently blur a per-prime packet groupoid
with the all-prime inherited union and state the one-orbit quotient topology as
though it were already source-verified.

## 3. Load-bearing source findings

| Finding | Classification | Exact primary locator |
|---|---|---|
| The suspension flow and `Gamma_x0` are defined; every orbit in a packet has stabilizer `(N x0)^Z` | `SOURCE_THEOREM` | Deninger v4, Section 6, physical p. 38, paragraph before Theorem 6.1 |
| The nontrivial periodic set is the disjoint union of packets; for `Spec Z`, `L_p=log p` and additive isotropy is `L_p Z` | `SOURCE_THEOREM` | Deninger v4, physical p. 39, Theorem 6.1 and following paragraph |
| Each packet is a compact subset with compact periodic-orbit fibres | `SOURCE_THEOREM` | Deninger survey, physical pp. 11--12, Theorem 4.2 |
| The coordinate maps and fibration map depend on auxiliary choices; only (40) is declared canonical | `SOURCE_LIMITATION` | Deninger v4, physical p. 33, paragraph after (39) containing (40) |
| The ambient pointwise, quotient, and colimit topologies are specified; relevant canonical continuous bijections need not be homeomorphisms in general | `SOURCE_LIMITATION` | Deninger v4, Proposition 7.4, physical p. 43; Propositions 7.6--7.7 and Corollaries 7.8--7.9, physical pp. 44--45; Theorem 7.10 and Remarks, physical pp. 46--47 |
| All preceding Section-7 results remain valid for admissible `E`, including `E_f` | `SOURCE_THEOREM` | Deninger v4, physical p. 47, paragraph after Theorem 7.10 |
| No product homeomorphism, Borel product transport, packet disintegration, or transverse measure is supplied for the actual `E_f` packet | `NOT ESTABLISHED` | Negative boundary of the preceding locators; equations (37)--(39) are set/equivariant presentations, physical pp. 32--33 |

### Packet topology consequence

For `Spec Z`, Section 7 supports the following **author-new derivation**:

1. the relevant affine `E_f` spaces are second countable;
2. the countable Frobenius colimit is a countable union of open
   second-countable pieces;
3. product with `R` remains second countable;
4. the suspension quotient is second countable because the quotient map of a
   group action is open; and
5. `Gamma_p`, as a subspace, is second countable.

This should be proved and locked in Phase 2 as `DERIVABLE_NEW_LEMMA`; it is not
an explicit Deninger theorem.  Compactness gives local compactness in the weak
non-Hausdorff sense, but the standard `locally compact Hausdorff` gate remains
open because the retained source does not establish Hausdorffness of the
suspension or of the inherited packet subspace.  Without that gate, standard
Borel/Polish conclusions must not be asserted.

## 4. Derived compact quotient `Q_p`

Put `K_p=R/L_p Z` and let it act through the source flow.  Exact common
isotropy gives a well-defined **free** `K_p`-action: if `[t]` fixes a point,
then `t` lies in `L_p Z`.  Continuity of the descended action follows from the
open quotient `R -> K_p`.  Since `Gamma_p` is compact, the orbit quotient

```text
Q_p = Gamma_p / K_p
```

is compact; the open-quotient argument also makes it second countable after the
preceding lemma closes.

This construction avoids any identification `Q_p=B_p`, but it does **not** by
itself prove that `Q_p` is Hausdorff.  A compact group quotient is Hausdorff
once `Gamma_p` is Hausdorff (or once the orbit relation is independently proved
closed); neither premise is closed by the retained packet source.  Freeness also
does not supply a global section, local product charts, a principal-bundle
trivialization, or a canonical probability on `Q_p`.  In particular, even a
compact Hausdorff `Q_p` is not automatically a compact group and has no
source-selected Haar probability.

**Q-p gate:** retain `Q_p` as a useful per-prime derived candidate, conditional
on a Phase-2 Hausdorff/closed-relation proof.  Do not identify it with `B_p` or
use it to claim a packet disintegration before a separate theorem.

## 5. One-orbit restriction and the limited Morishita bridge

From Deninger alone, the orbit map

```text
R/L_p Z  ->  O_x,   [t] |-> phi^t(x)
```

is a continuous bijection, but the retained source does not show that it is a
homeomorphism onto the **inherited** orbit subspace.  Thus the lock's intrinsic
`R/L_p Z` description is immediately safe only as an explicitly introduced
quotient-topology candidate.

There is, however, a legal limited bridge to close this point in Phase 2:

1. Morishita Lemmas 3.4--3.5 (physical pp. 22--24) construct a continuous,
   flow-anti-equivariant map;
2. Paper 7 derives its restriction to Deninger's genuine `E_f` subsystem and
   repairs the packet-image argument using Deninger (35);
3. on each source orbit it is onto the target circle `C_p`; Morishita (1.1.5),
   physical p. 5, identifies `C_p` with `R_+/p^Z`, while Deninger gives the same
   stabilizer `p^Z` on the source orbit;
4. anti-equivariance plus equality of stabilizers makes the orbit restriction
   injective; and
5. the compact source orbit mapping continuously and bijectively to the
   Hausdorff target circle is homeomorphic to it.

This is a **`DERIVABLE_NEW_LEMMA`**, not Morishita's printed theorem on his
larger full-character object and not an inherited Paper-7 credit.  Paper 8 must
restate and prove it from the locked primary manifestations.  It can close
one-orbit `T1` and `T2`.  It cannot close packet Hausdorffness: every transverse
source orbit in `Gamma_p` maps to the same `C_p`, so the map collapses the
packet quotient.  It supplies no measure, Haar system, groupoid algebra,
representation, trace, or arithmetic mass transport.

## 6. Per-prime object versus global packet union

The per-prime object `Gamma_p rtimes R`, the family of those groupoids, and one
groupoid on `union_p Gamma_p` are different records.  The candidate lock calls
the latter a `disjoint_union` while simultaneously requiring its inherited
source topology.  These words do not choose the same topology:

- the inherited subspace union can contain packet-accumulation phenomena and
  is not proved locally compact, open, or closed by the per-prime results;
- the topological coproduct makes each packet open and is a new chosen
  topology, not automatically the source subspace topology; and
- a time-only kernel over every prime need not be compactly supported on the
  global groupoid even when its restriction to every per-prime groupoid is
  admissible.

The lock must therefore split the per-prime groupoid/family from any global
assembly.  All Phase-2 topology and operator results should first be stated per
prime; the global record requires its own topology, algebra, support domain,
component masses, and convergence theorem.

## 7. Haar and probability normalization

Three measures must remain distinct:

| Measure | Role | Total mass |
|---|---|---|
| Lebesgue `dt` on the acting group `R` | proposed transformation-groupoid Haar system on arrow fibres | infinite |
| length Haar `du` on `R/L_p Z` | invariant unit measure in a length coordinate | `L_p` |
| probability Haar `du/L_p` on `R/L_p Z` | normalized invariant unit probability | `1` |

The arrow Haar system does not choose an invariant/transverse unit measure.
Nor may `du` and `du/L_p` be interchanged: they change trace coefficients by a
factor `L_p`.  The displayed factor `1/(2 pi L_p)` in the preregistered
character integral combines dual-Haar/covolume and unit-measure conventions; it
must not be called merely an isotropy-Haar probability average.  Phase 2 must
freeze acting-group Haar, orbit length measure, orbit probability, isotropy
Haar, dual measure, and fibre-trace normalization separately and use one common
convention in the regular/trivial-character comparison.

## 8. T0--T7 source-feasibility matrix

| Gate | Actual per-prime packet | One actual orbit | Morishita / Paper 7 / product proxy |
|---|---|---|---|
| `T0` object identity | **PASS** as a newly defined restriction of the actual `E_f` source flow; not source-authored as an analytic groupoid | **PASS** for a chosen actual orbit | Morishita's printed full-character object and Paper-7 proxy are not identical; no packet substitution |
| `T1` topology/Borel | **PARTIAL:** compact and second-countability derivable; inherited Hausdorff, standard Borel, and product chart open | **DERIVABLE:** limited `E_f` Morishita orbit-homeomorphism lemma above; otherwise only a quotient-topology candidate | Product topology is a modeling choice; no packet transport |
| `T2` flow/clock | **PASS:** source flow, `L_p=log p`, exact isotropy | **PASS**; Morishita reverses time but preserves absolute period | Only this orbit-level field can bridge |
| `T3` groupoid/Haar | **CONDITIONAL:** topological action groupoid exists; LCH-Hausdorff/completion theorem assumptions not closed | **FEASIBLE AFTER T1:** `dt` is the proposed Haar system, still requiring exact theorem/convention verification | No packet Haar/completion transport from Morishita or Paper 7 |
| `T4` measure | **OPEN:** no source invariant/transverse packet measure, disintegration, or cross-prime mass | normalized orbit Haar is available after the circle topology closes, but orbit selection is extra | Paper-7 probabilities are proxy choices; Morishita transports none |
| `T5` representation/trace | **NOT TESTABLE FROM RETAINED PACKET SOURCES** | technically plausible but no induced-representation/FNS/`C*`-trace theorem yet credited | No legal analytic bridge |
| `T6` test algebra/formula | **UNPROVED TARGET:** membership, domains, signs, convergence, and Poisson/Floquet formula remain obligations | same | Paper-7 formulas do not transport across objects |
| `T7` arithmetic promotion | **PARTIAL:** prime label, packet, clock, and repetitions are sourced; packet and cross-prime masses are not | no canonical orbit selection or component mass | no target-independent mass/trace promotion |

No analytic Route credit follows at Phase 1.  The source packet retains only its
already established clock/periodic-ledger status.  The product proxy and Paper-7
trace/determinant cannot be used coordinatewise to populate missing gates.

## 9. Mandatory revisions before Phase 2

1. Split the per-prime packet groupoid/family from any inherited all-prime
   union and from a topological coproduct; give each a separate ID.
2. Mark packet Hausdorffness and standard Borel structure unresolved.  Record
   second countability as a proposed new lemma, not a source theorem.
3. Either type the orbit as a quotient-topology candidate or preregister the
   limited Morishita `E_f` orbit-homeomorphism lemma as its exact T1 bridge.
4. Add `Q_p` only as a conditional derived record: compact and second-countable
   are feasible; Hausdorffness/closed orbit relation and any measure theorem
   remain gates; no `Q_p=B_p` claim.
5. Name `dt`, `du`, and `du/L_p` separately and split all dual/covolume factors.
6. Preserve the statement that Morishita and Paper 7 give no **packet-level or
   analytic** bridge.

These revisions change typing and proof obligations, not the research
hypothesis.  The one-orbit P8-2--P8-6 chain remains a viable mandatory core;
packet and global promotion remain conditional tiers.

## 10. Precise Phase-2 primary-source obligations

Phase 2 must not credit any item below until an exact primary manifestation,
theorem/section locator, assumption match, and hash are recorded:

1. prove inherited `Gamma_p` Hausdorffness or prove the orbit relation closed;
   separately write the second-countability lemma;
2. re-prove and lock the limited Morishita `E_f` orbit homeomorphism from the
   primary Deninger/Morishita manifestations;
3. decide the topology of the all-prime union and prove its local compactness,
   countability, support, and component-assembly properties if it is retained;
4. verify the exact transformation-groupoid Haar-system, amenability, and
   full-versus-reduced theorems for the frozen arrow convention and object;
5. locate a primary transitive-groupoid/imprimitivity theorem and state whether
   it yields an isomorphism, stable isomorphism, Morita equivalence, or only a
   measurable decomposition;
6. locate primary results for induced isotropy-character representations,
   regular FNS traces/weights, lower-semicontinuous semifinite `C*`-traces, their
   positive domains, and the proposed non-normality/no-extension statement;
7. prove trace-class or trace-ideal membership for `a_f`, the exact
   Poisson/Floquet formula, convergence, sign, and every Haar/covolume factor;
8. classify invariant packet measures through `Q_p` only after the quotient
   topology closes, and keep orbit probability, transverse probability,
   packet mass, and cross-prime mass separate; and
9. issue an explicit exclusion certificate showing that Morishita's collapsing
   map and Paper 7's proxy do not transport T3--T7.

Until those obligations close, the correct source statement is: **the actual
one-orbit groupoid is feasible and has a narrow derived topology bridge; the
actual packet groupoid is topologically defined but not yet verified in the
LCH-Hausdorff analytic category; no source-owned packet trace has been found.**
