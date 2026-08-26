# Paper 9 Phase-2 topology and source audit

Audit date: 2026-08-14 (Asia/Shanghai)  
Decision: **PASS TO PHASE 3 WITH STRICT OBJECT-SPLIT GATES**  
Novelty result: **no direct primary-source precedent found for the proposed
rational-Witt `E_f` packet non-separation theorem**

## 1. Exact-lock binding and audit boundary

This audit is bound to the exact Phase-1 tuple independently re-locked by both
review artifacts:

| Active input | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `895b2357d4815d295a8a63f1b6a0c412aaf5afdc34e715b2607d5d25945ad49e` |
| `notes/candidate_lock.md` | `0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded` |
| `notes/phase1_design_amendment.md` | `b3a7143b6b213501869467ac78090a6d8ae433f6137185fc6537d99698120cbb` |

The independent re-lock reports are
`phase1_methodology_relock.md`, SHA-256
`936b17eb465697414371dd95b691ee9179d2706496e6303b868e366ab97cb88b`,
and `phase1_amended_relock.md`, SHA-256
`0e18c1de19a56c988ae17a88859493a238291a2264c012dc09d4e77db688e346`.
Both verdicts are PASS with zero Critical, Major, and Minor findings.

Phase 2 verifies source ownership, manifestations, exact locators, and the
absence of an already-published exact theorem. It does **not** prove density,
character convergence, packet indiscreteness, non-closedness of the restricted
relation, or any Phase-3 target `P9-1`--`P9-9`.

The retained-source manifest is
`notes/sources/paper9_source_manifest.md`; its independent file ledger is
`notes/sources/paper9_sources.sha256`.

## 2. Executive source verdict

The exact Deninger source object is reconstructible, but the desired topology
classification is not source-owned:

1. Deninger defines the suspension quotient and exact right action, proves the
   fixed-prime exponent parametrization and stabilizer, and supplies the
   pre-suspension topology needed for a new proof.
2. His fixed-prime coordinate maps in equations (38), (39), and Section 6 are
   only equivariant **bijections**. They are not asserted to be
   homeomorphisms.
3. His Hausdorff results stop at the checked pre-suspension spaces. His global
   suspension decomposition is only a continuous bijection, expressly “not
   [a] homeomorphism[] in general.”
4. His use of “compact” for packets and periodic orbits does not say compact
   Hausdorff and cannot supply an LCH-Hausdorff groupoid hypothesis.
5. Deninger gives strong warnings that leaf slices need not inherit their
   source topology and that the relevant ambient adelic action is not properly
   discontinuous. Neither warning itself classifies the genuine fixed-prime
   `E_f` packet.
6. No primary source found states that this packet, its inherited orbits, or
   its orbit quotient is non-`T0`, indiscrete, Hausdorff, LCH-Hausdorff, or the
   base of a principal `K_p`-bundle.

Therefore the Phase-3 topology theorem is both necessary and, subject to the
pre-registered map/domain gates, genuinely new relative to the verified
literature.

## 3. Deninger: exact source ownership

The primary manifestation is C. Deninger, *Dynamical systems for arithmetic
schemes*, arXiv `1807.06400v4`, retained as `P9-DEN-DYN-v4`.

### 3.1 Set parametrization and isotropy

| Locator | Exact source content | Permitted Phase-3 use | Forbidden promotion |
|---|---|---|---|
| physical p. 32, Eq. (35) | finite-kernel residue-field characters are reached by `(a,nu)` with `a in Zhat_(p)^times`, `nu in N` | finite-kernel/unit-exponent exhaustiveness input, after the frozen quotient-level audit | topology, inverse continuity, or product structure |
| physical p. 32, Eq. (38) | `Q_{>0}`-equivariant bijection from the displayed exponent quotient to `C_{x_0}` | set equivalence and exact action | homeomorphism or transported product topology |
| physical p. 33, Eq. (39) | equivalent bijection using `Q_{>0}/N(x_0)^Z`; following paragraph describes a set fibration over `Zhat_(p)^times/p^Zhat` | set-level orbit/base labels | compact-group bundle, locally trivial bundle, or principal bundle |
| physical pp. 38--39, Section 6 and Theorem 6.1 | suspension quotient, `(P,u)q=(F_qP,q^{-1}u)`, packet, induced `R_{>0}`-bijection, and exact isotropy `N(x_0)^Z` | source action sign, packet membership, clock `log N(x_0)`, and stabilizer | a topological circle or packet homeomorphism |

For `X_0=Spec Z` and `x_0=(p)`, these locators own the set/action facts
required by the lock: packet label `(p)`, common stabilizer `p^Z`, and clock
`log p`. The sentence that all orbits are circles follows an explicitly named
`R_{>0}`-bijection; it does not change that bijection into a homeomorphism.

### 3.2 Topology locators and their ceiling

- Physical p. 43, Proposition 7.4 makes the initial colimit stage open and
  closed and each `F_q` a homeomorphism **before suspension**.
- Physical pp. 44--45, Propositions 7.6--7.7 and Corollaries 7.8--7.9 prove
  metrizability/Hausdorffness of the initial and checked pre-suspension spaces
  under the stated scheme hypotheses. `Spec Z` satisfies those hypotheses.
  This does not prove the quotient suspension Hausdorff.
- Physical pp. 46--47, Theorem 7.10 gives continuous bijections from the
  characteristic-stratum mapping-torus models to the suspension. Remark 2 on
  physical p. 47 says they are not homeomorphisms in general and gives a
  connectedness counterexample.
- The paragraph following Theorem 7.10 on physical p. 47 gives admissible-`E`
  objects their subspace/inductive-limit topologies and says the preceding
  Section-7 results persist. Thus these are valid topology inputs for `E_f`,
  but they still stop before an inverse-continuity theorem for the suspension
  coordinate bijection.
- Physical p. 49, equation (68), says that the `Q_{>0}` action on the adelic
  **target** `Hcheck_Etors x R_{>0}` is not properly discontinuous. It is useful
  context but is not a theorem about the restricted relation `R_p` in the
  Deninger source.
- Physical p. 63, opening of Section 10, says that a leaf slice maps
  continuously and bijectively to its image but in general not
  homeomorphically with the inherited subspace topology; without proper
  discontinuity the partition need not be locally trivial. This directly
  supports the protocol's no-topology-promotion rule, not a particular
  `CONFIRM_*` verdict.

### 3.3 Analogies that may not be promoted

Two nearby Deninger results point in different directions and therefore force
an exact fixed-prime proof.

- Physical p. 62 derives the coarse topology on a related quotient `Y`
  (abstractly `Zhat^times`) from strong approximation.
- Physical pp. 64--65, Proposition 10.3 and its first remark, give a related
  generic adelic suspension quotient which is irreducible but `T1`, because
  its orbits are closed.

Neither is the fixed-prime `E_f` packet. In particular, “dense diagonal” alone
cannot be promoted mechanically to “indiscrete quotient”; Phase 3 must prove
the exact closure statement on the frozen restricted relation.

### 3.4 Compactness does not close the topology gate

Deninger's survey, arXiv `2301.11643v1`, physical pp. 11--12, Theorem 4.2,
calls each `Gamma_{x_0}` a compact subset and its orbit fibres compact. It does
not add “Hausdorff,” “locally compact Hausdorff,” “product,” “locally
trivial,” or “principal.” Physical pp. 12--13, Theorem 4.4, again supplies a
continuous bijection which the following sentence says is not a
homeomorphism. Paper 9 must not read compactness as compact Hausdorffness.

## 4. Morishita: useful continuity, unusable topology promotion

The current manifestation is M. Morishita, arXiv `2508.15971v5`, retained as
`P9-MOR-v5`.

### 4.1 Exact findings

- Physical p. 5, equation (1.1.5), says that projection to the infinite
  component makes the adelic prime orbit `C_p` “isomorphic to the circle”
  `R_+/Np^Z`. It does not say “homeomorphic” or identify an inverse-continuity
  theorem.
- Physical p. 13, Remark 2.1.13, expressly says that the paper omits
  Deninger's character refinement. Hence its printed source is not the exact
  rational-Witt `E_f` object.
- Physical pp. 14--17 define the full-character suspension with quotient
  topology and state homeomorphisms in Theorems 2.2.8--2.2.9. But equation
  (2.2.7) parametrizes only characters obtained from a unit exponent and a
  positive integer, hence finite-kernel characters. It does not cover the
  declared full `Hom` space (including the trivial and infinite-kernel
  characters). Those homeomorphism claims therefore cannot carry the
  topology of the exact `E_f` source without a new same-object proof.
- Physical pp. 23--24, Lemmas 3.4--3.5, do give a continuous character/adelic
  map and continuous suspension map with the stated equivariance. These are
  admissible only as continuity inputs after the source-domain audit.
- Physical pp. 24--25, Theorem 3.6(2), asserts that a source orbit maps onto
  the target `C_p`; its printed proof checks only that the `p`-component is
  zero and does not establish that every away-`p` component is nonzero.

### 4.2 Paper-8 source-manifest correction

Paper 8's `phase2_topology_source_manifest.md` described Morishita equation
(1.1.5) as a “Hausdorff circle.” The exact source says only “isomorphic to the
circle.” Paper 9 supersedes that topology promotion:

```text
MOR-CC-Cp-INHERITED            exact quotient-subspace topology under audit
MOR-CC-Cp-STD-CIRCLE-PROXY     ordinary Hausdorff circle by modeling choice
```

The two objects are not source-certified as homeomorphic. Morishita retains
source credit for the target label, set map, clock, and qualified continuity;
he does not certify the actual Deninger orbit or packet as Hausdorff/LCH.

## 5. Connes--Consani: mandatory topology split

Three topological objects must remain separate.

| Typed object | Exact source result | Phase-2 status |
|---|---|---|
| `CC-SCALING-Cp` | Connes--Consani, *The scaling site* (2016), physical/printed p. 5, Lemma 6.3(i): the intrinsic point subspace is **topologically isomorphic** to `R_+^*/p^Z` | `VERIFIED`, but intrinsic scaling-topos ownership only |
| `CC-NAIVE-XQ-Cp-INHERITED` | Connes--Consani, arXiv `2501.06560v1`, physical p. 9: `X_Q` is the natural quotient, `C_p` is a subspace, and `R_+^*/p^Z -> C_p` is called an “isomorphism”; pp. 11--12, Proposition 3.4, gives the topological mapping-torus/fibration description of its inverse image | strong evidence of the authors' intended circle model, but no separately stated theorem identifies the global scaling-topos point topology with the naive quotient topology |
| `DEN-EF-ORBIT-INHERITED-TOPOLOGY-P` | Deninger Section 6 supplies an equivariant bijection only | no topology transport from either CC object |

The latest Connes--Consani paper says that the scaling-topos point set is
**canonically bijective** with the natural adelic quotient; it does not state a
global homeomorphism of point-space topologies. Under the active lock, that
bijection cannot merge `CC-SCALING-Cp` with
`CC-NAIVE-XQ-Cp-INHERITED`, and neither object can merge with Deninger's
rational-Witt orbit.

Consequently the exact homeomorphism

```text
MOR-CC-Cp-INHERITED  ->  MOR-CC-Cp-STD-CIRCLE-PROXY
```

remains **NOT ESTABLISHED BY THE VERIFIED WORDING**. This is a source-level
object/comparison gap, not evidence that the inherited adelic `C_p` is
non-Hausdorff.

## 6. Le Bruyn: formal correction and exact exclusion

The peer-reviewed source is L. Le Bruyn, *The sieve topology on the arithmetic
site*, *Journal of Algebra and Its Applications* 15 (2016), 1650020, DOI
`10.1142/S0219498816500201`. The retained institutional author version has a
repository cover, so printed p. 2 is physical p. 3.

- Printed p. 2 / physical p. 3, Theorem 1, gives a countable basis for the
  **standard topology** on the finite-adele-class quotient. It is coarse but
  not indiscrete.
- Printed p. 9 / physical p. 10 thanks the referee for correcting an erroneous
  statement about that topology in an earlier version.

Therefore the old arXiv `1407.5538v2` conclusion that the standard topology is
trivial is **EXCLUDED** from evidence. It may be cited only as correction
history. The formal 2016 result is **INCLUDED**.

The object is `Q_+^*\A_f/Zhat^*`, not the full adelic quotient `X_Q` and not
Deninger's rational-Witt packet. Its non-indiscrete topology is a valuable
negative control but does not settle `Gamma_p`.

## 7. Properness, bundle structure, and measure bridges

### 7.1 No source-owned packet principal bundle

No verified source proves that the actual `K_p=R_{>0}/p^Z` action on
`Gamma_p` is proper, that its orbit relation is closed, or that
`Gamma_p -> Q_p` is a locally trivial/principal compact-group bundle.

General compact-action and slice theorems require separation/regularity
hypotheses on the total space. They cannot be applied before Phase 3 classifies
the inherited packet topology. Connes--Consani Proposition 3.4 concerns the
different map `pi^{-1}(C_p) -> C_p` in the adelic cover and does not furnish a
principal-bundle theorem for Deninger's packet.

### 7.2 Exact conditional disintegration theorem

D. Jüstel, *The Zak transform on strongly proper G-spaces and its
applications*, arXiv `1605.05168v2`, provides the closest exact bridge:

- physical pp. 3--4, Definition 2.1, freezes the properness hierarchy and
  quotient topology;
- physical p. 5, Lemma 2.3, gives the orbital mean
  `C_c(X) -> C_c(G\X)` for a proper lcH action;
- physical p. 6, Theorem 2.4, gives a unique quotient Radon measure and Weil
  disintegration for a strongly proper lcH action **after** a quasi-invariant
  Radon measure on `X` is supplied.

This is conditional infrastructure only. It supplies neither the missing
Hausdorff/properness theorem nor a canonical transverse measure for the actual
`E_f` packet. If Phase 3 proves a non-Hausdorff packet, its lcH-Hausdorff
hypotheses fail; if Phase 3 proves separation, the measure input remains an
independent obligation.

### 7.3 Groupoid/trace ceiling

Paper 8's verified Muhly--Renault--Williams, Green, and Combes--Zettl results
remain conditional general bridges. They do not reconstruct the topology,
select a transverse probability, or identify a represented normal trace on
the actual packet. No 2026 update located through the cutoff removes those
inputs. In particular, current étale-groupoid trace results do not apply to
the continuous `R`-action merely by analogy.

Thus `T3`--`T6`, packet completion, Haar system, trace, and determinant claims
remain withheld exactly as the active lock requires.

## 8. Approximation-source boundary

Standard additive strong approximation supports the arithmetic plausibility
of `P9-1`; for example, J. Voight, *Quaternion Algebras*, Chapter 28,
Section 28.1, especially Theorem 28.1.8 and formulation 28.1.9, treats strong
approximation with one omitted place and uses `Z[1/ell]` plus CRT in the
proof. The same chapter explicitly warns that `Q^times` does not satisfy
multiplicative strong approximation in the finite ideles.

This reference is contextual, not load-bearing. The active protocol correctly
requires a constructive positive-numerator/denominator CRT proof for the exact
diagonal subset and forbids the slogan “multiplicative strong approximation.”
No general theorem may skip the `E_f` unit-target/domain checks.

## 9. Novelty and negative-search ledger

The search cutoff was 2026-08-14. The audit checked:

- current official arXiv records and later-version histories for Deninger,
  Morishita, and Connes--Consani;
- Deninger's Münster bibliography and Morishita's Kyushu profile;
- exact and combined searches for `rational Witt`, `E_f`, `prime packet`,
  `non-T0`, `indiscrete`, `Hausdorff`, `closed orbit relation`, `properly
  discontinuous`, and `principal bundle`;
- current primary literature on quotient measures and groupoid traces.

No primary source was found which directly proves or refutes any of the
following for Deninger's genuine fixed-prime rational-Witt `E_f` packet:

- indiscreteness or failure of `T0`/`T1`;
- Hausdorffness or LCH-Hausdorffness;
- closedness/non-closedness of the restricted diagonal orbit relation;
- properness of the `K_p` action;
- a compact/principal-bundle structure over `Q_p`; or
- an exact transverse-measure/disintegration/operator-trace bridge.

This is a bounded negative search result, not a proof that no such source can
exist. It is sufficient for the present novelty gate: the Phase-3 theorem must
be proved from the verified definitions and topology arrows, not cited as an
existing result.

## 10. Phase-3 source-use matrix

| Proposed use | Source status |
|---|---|
| exact Deninger source object, right action, packet, `p^Z`, and `log p` | `PASS` |
| unit/finite-kernel set parametrization and packet exhaustiveness input | `PASS` at set level; topology forbidden |
| initial/Galois/colimit topology arrows | `PASS`, with the three frozen object levels kept distinct |
| Deninger set model is a homeomorphic product or circle | `FAIL / not source-owned` |
| pre-suspension Hausdorffness | `PASS` |
| suspension packet/orbit Hausdorffness or LCH-Hausdorffness | `NOT ESTABLISHED` |
| intrinsic scaling-topos `C_p` is an ordinary topological circle | `PASS`, exact object only |
| naive adelic inherited `C_p` equals the scaling-topos `C_p` topologically | `NOT ESTABLISHED BY AN EXACT COMPARISON THEOREM` |
| Morishita inherited `C_p` equals the ordinary circle proxy homeomorphically | `NOT ESTABLISHED` |
| Le Bruyn old-arXiv “trivial standard topology” conclusion | `EXCLUDED / formally corrected` |
| Jüstel quotient measure/Weil formula | `CONDITIONAL`; missing packet hypotheses and measure |
| direct published precedent for `CONFIRM_STRONG`, `CONFIRM_ORBIT`, or `REFUTE_OBSTRUCTION` | `NONE FOUND`; Phase 3 decides |

## 11. Public synchronization boundary

All locally retained source PDFs passed read-integrity preflight, but no
blanket redistribution licence is inferred from access, a URL, or an arXiv
record. Public GitHub synchronization must exclude
`papers/9-packet-separation/notes/sources/*.pdf` and the reused Paper-8 source
PDFs unless an exact-manifestation licence is documented. The public audit
package should include this audit, the source manifest, the checksum ledger,
preflight sidecars, URLs, and exact locators.

**Phase-2 verdict:** the source object and all required source arrows are
sufficiently verified to begin the bounded Phase-3 proof. No source licenses a
topology promotion or settles the topology theorem in advance.
