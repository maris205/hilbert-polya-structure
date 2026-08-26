# Paper 12 Phase-3 independent final mathematical peer review

Date: **2026-08-15 (Asia/Shanghai)**  
Review lane: **independent, read-only review of the frozen Phase-3 tuple**  
Scope: **`P12-1` through `P12-9`; standalone-content disposition**

## 1. Final decision

**Verdict: PASS (`C0/M0/m0`).**

The two proof files establish `P12-1`--`P12-8` at the registered signs,
domains, coefficient hypotheses, owners, and topology directions. The
deterministic package establishes the registered `P12-9` witness/falsifier
contract and reproduces exactly. I found no critical, major, or minor
mathematical, methodological, source-integrity, or reproducibility finding.

The exact scoped decisions are:

```text
phase3_peer_verdict: PASS
critical: 0
major: 0
minor: 0
complex_collapse: CONFIRM_COMPLEX_COLLAPSE
marked_period: CONFIRM_MARKED_PERIOD_RECOVERY
category_boundary: CONFIRM_STRICT_VS_SCALED_SPLIT
packet_result: PACKET_COROLLARY
ORBIT_ONLY: false
novelty_ceiling: SUPPORTED_WITHIN_SEARCH
direct_precedent_found: false
standalone_disposition: STANDALONE_PASS
P12-10: outside this review and still separately gated
Route_B_invocation: false
manuscript_or_release_authorized_by_this_report: false
```

`STANDALONE_PASS` is the preregistered content/nonredundancy disposition, not
a release decision. Route serialization, manuscript composition, citation,
declaration, public-sync, and release gates remain separate.

## 2. Frozen-byte receipt

I reviewed only the following stable Phase-3 tuple and independently rehashed
it immediately before freezing this report.

| Artifact | SHA-256 |
|---|---|
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` |
| `results/manifest.json` | `5337f13b07498872a97ed0d13f0ff0f5ffbcea9e3e37bf8e0c558c3e966e5d3a` |
| `code/generate_controls.py` | `fe557d3296e2fd841e313c9e0708a144acfc9da616616f82de30b00f873ec6e7` |
| `code/test_controls.py` | `719e492a1fe07033c8b25edc7dd46aa589f3c6e21d50b14573bef955f638fde6` |
| `experiments/reproduce.sh` | `b3e85a593b1910683ed7545e9ccca9d482f94d8ebf7a7da94d0337fc0e577828` |

The active lock/gate bytes also match their recorded receipts:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` |
| `notes/pipeline_state.md` | `24c226e35d69c6aab68df19d495957469ec761551680696b20cff865604fe62d` |
| `notes/phase1_final_gate.md` | `fc327245bf5653b18f21f782f4783a2ad0b606340c5f5e7da6516d0514cac72c` |
| `notes/phase1_status_relock.md` | `a7a9875c810ea98f5a5563c8f243612b006c20f397aaa8ebae533d8b8c6c61d6` |
| `notes/phase2_category_owner_audit.md` | `8fad79f121439145e0ac3cac7ca67e82f3e2ad6af86da5b0f001e92da30e1d62` |
| `notes/phase2_novelty_search.md` | `c4584862824dbaadec9945fb85defd6d11ee7822849471b075ff4d90d57ca1bd` |
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` |
| `notes/phase2_final_review.md` | `032d558fecdccc492ce59733e20dd9322f573d033355aee3c74563680cea2ea7` |
| `notes/phase2_final_gate.md` | `1b05110e23f23848442742b415811205ef24616413b59989996993d4297be9ab` |
| `notes/phase2_status_relock.md` | `c6fb9d3a04171bc68ed6239e1a91cee8f9987cd75d8516967d3ded5de6b89eea` |

I read the complete Phase-1 and Phase-2 gates, reviews, amendments, relocks,
source manifest/checksum/preflight records, both stable proof files, both
control implementations, the reproduction script, manifest, and every CSV.
I also applied the full academic peer-review, methodology, domain,
devil's-advocate, and integrity-review instructions. No browser search was
performed and no reviewed artifact was edited.

## 3. Target-by-target disposition

| Target | Independent result | Exact boundary retained |
|---|---|---|
| `P12-1` | **PROVED** | all finite nerve degrees, not an extrapolation from `n=1` |
| `P12-2` | **PROVED** | author-defined continuous unnormalized complex; direct `d^2=0` |
| `P12-3` | **PROVED** | every named `T0` topological abelian coefficient group; non-`T0` removal refuted |
| `P12-4` | **PROVED** | algebraic `Z^1=Rc`, `B^1=0`, `H^1=R[c]`; no cochain/cohomology topology |
| `P12-5` | **PROVED** | restriction descends only after coboundary vanishing; lattice conclusion only with `H=LZ` |
| `P12-6` | **PROVED — `PACKET_COROLLARY`** | exact fixed orbit and exact fixed-prime packet only; `ORBIT_ONLY=false` |
| `P12-7` | **PROVED** | strict preservation, positive-scale covariance, weaker-category existential non-descent, and nonconverse |
| `P12-8` | **PROVED** | normalized strict pointed quotient functor; standard-to-actual continuity only; scaled map semilinear only |
| `P12-9` | **PASS** | deterministic finite witnesses/falsifiers, not universal proof or source proof |

## 4. Independent mathematical rederivation

### 4.1 Nerve topology, indices, faces, and `d^2`

For a composable `n`-tuple, the first range `x` and the `n` real time
coordinates determine every later range recursively. This gives the stated
bijection `Psi_n`. After reordering the ambient product as `X^n x R^n`, its
opens are exactly `X^n x U`; intersecting with the composable locus pulls
back to exactly `X x U`. This proves both directions of the homeomorphism for
every finite `n`, including the complete open-set claim.

The range-first face formulas have the correct three effects: the zeroth face
moves the unit to `x dot t_1` and drops `t_1`; an interior face replaces
`t_i,t_(i+1)` by `t_i+t_(i+1)`; the last face drops the last time. I checked
the face identity with restored degrees,

```text
partial_i^(m-1) partial_j^m
 = partial_(j-1)^(m-1) partial_i^m,  i<j,
```

including the adjacent-addition and `i=0,j=1` right-action cases.

Expanding `d^(n+1)d^n` gives indices
`0<=i<=n+1`, `0<=j<=n+2`. Each term with `i<j` pairs with `(j-1,i)`:
the composite face map is identical and the exponents `i+j` and
`(j-1)+i` have opposite parity. Conversely every index pair with first
index at least the second is uniquely the partner of `(second,first+1)`.
Thus these pairs partition the full double sum; no endpoint or diagonal term
is left over. The same calculation covers `n=0`, where the separately written
`d^0=h\circ s-h\circ r` is exactly the two-face formula. The signs and
`d^2=0` proof are correct.

### 4.2 Constant coefficients, `T0` factorization, and the chain map

The constant-bundle identity action is a continuous restriction of
`(gamma,(y,a)) |-> (r(gamma),a)` and obeys the unit/composition laws.

For fixed time coordinates, `(x,t)` and `(y,t)` are topologically
indistinguishable. A continuous map to a `T0` target therefore takes the same
value at both. Evaluation at a chosen unit is continuous and becomes
unit-independent only after this lemma, so the proof does not assume its
inverse. Projecting each groupoid face gives the corresponding one-object
group face, including the unit-moving zeroth face, and hence `d_G T=T d_R`
in every degree. Degree zero is checked separately and correctly.

The hypothesis is sharp: with an indiscrete two-point coefficient group, a
nonconstant degree-zero map is continuous and cannot lie in the constant
pullback image. This is an exact non-`T0` counterexample, not merely a failed
finite probe.

### 4.3 Real `H^1`, isotropy descent, and scale blindness

With a one-cochain written as `b(x,t)=f(t)`, the frozen sign convention gives

```text
(d^1b)(x;t,u)=f(u)-f(t+u)+f(t).
```

The cocycle equation is therefore the additive Cauchy equation. The proof
derives rational linearity and then uses continuity to obtain
`f(t)=lambda t`; it does not assume measurability or a stronger regularity
hypothesis. Every continuous `X->R` map is constant, so `B^1=0`. Hence the
claimed algebraic line and its marked coordinate class are correct.

On isotropy, the time chart is the topological group isomorphism
`H_x -> G_x^x`. A one-cocycle restricts to a continuous homomorphism, while
every one-coboundary vanishes pointwise because source and range coincide.
This vanishing is proved before passing to cohomology, making
`Per_x([b])` representative-independent. For `[lambda c]` its image is
exactly `lambda H_x`. Under transitivity, conjugation transports restrictions
and additive commutativity fixes the time label, so both stabilizers and
images agree across units. Finally,

```text
{lambda LZ:lambda!=0}={rZ:r>0}
```

is independent of the original `L`; no such lattice statement is extended
to trivial, free, dense, or nontransitive controls.

### 4.4 Same-owner packet specialization

The primary-source locator supports the exact chain used in the proof:
Deninger's right multiplicative flow is `[P,u] dot v=[P,uv]`, additive time
is `[P,u] dot t=[P,u exp(t)]`, and Theorem 6.1 gives multiplicative isotropy
`N(x_0)^Z` at every point of the fixed packet. For `Spec Z`, `x_0=(p)`, and
the exact Paper-9 packet (`E=E_f`), this is `p^Z` at every packet unit. Taking
the logarithmic time coordinate gives

```text
{t:exp(t) in p^Z}=(log p)Z.
```

Paper 9, not Deninger, owns the inherited indiscrete packet/orbit topology;
Papers 11--12 own the range-first transformation groupoid; Paper 12 owns only
the isotropy image of the marked class. The conclusion therefore is a valid
every-unit `PACKET_COROLLARY`, not an orbitwise promotion and not a new
derivation of the source stabilizer.

### 4.5 Strict, scaled, and unmarked morphisms

The three author-defined categories close under the displayed identities,
compositions, and inverses. For `(F,alpha)` with
`c'\circ F=alpha c`, the isomorphism sends `G_x^x` onto
`G'_(F_0x)^(F_0x)`, so the covariance direction is

```text
H'_(F_0x)=alpha H_x,
```

not `alpha^(-1)H_x`.

For `alpha=M/L`, the formula

```text
F_alpha([r]_L,t)=([alpha r]_M,alpha t)
```

is well-defined because `alpha L=M`; its displayed inverse, source/range,
product, inverse-arrow, topology, and mark calculations all check. It gives
scaled and unmarked isomorphisms for unequal positive periods, while strict
covariance rules out a strict unequal-period isomorphism. The orientation
reversal `([r],t)|->([-r],-t)` is unmarked, is not a positive-scale morphism,
and preserves `LZ`; it correctly refutes the converse from subgroup equality
to strictness. The arbitrary-subgroup family and dense `Q` example prevent
the weaker existential claims from being misstated as universal loss.

### 4.6 Pointed quotient, basepoints, and topology direction

A basepoint-preserving strictly `R`-equivariant map between standard
quotients is forced to send `[t]_H` to `[t]_(H')`; its existence forces
`H=H'`. Strict covariance therefore makes `S` well-defined. Its identity and
composition laws hold exactly, although it need not be faithful.

The chart `theta_x([t])=x dot t` is a well-defined equivariant set bijection.
The naturality square follows from the unique arrow with range `F_0(x)` and
marked time `t`, and the basepoint-change law is
`theta_(x dot u)=theta_x\circ tau_u`. The map from the usual Hausdorff
quotient to the actual indiscrete orbit is continuous. Its inverse would be
a nonconstant continuous map from a nontrivial indiscrete space to a `T0`
space and therefore is not continuous. No homeomorphic identification is
claimed.

For positive scale, `D_alpha([t])=[alpha t]` is a quotient homeomorphism and
obeys the semilinear law with `alpha u`. If `alpha!=1`, strict equivariance
would require `(alpha-1)R` to lie in the discrete lattice `alpha H`, which is
impossible. Thus it is correctly stopped outside the strict target category.

## 5. Source, framework, and ownership audit

The source checksum ledger was independently rerun: all five PDFs and all
five preflight sidecars returned `OK`. Every preflight record has matching
declared, enumerated, and reader page counts, `verdict=PASS`, and no warning.
Direct inspection of Deninger physical/printed pp. 38--39 confirms the packet,
flow, and every-unit stabilizer statements used above.

Blanco--Uribe--Waldorf supplies the nearest primary convention comparator for
continuous simplicial cochains and the full inhomogeneous differential on its
stated domain. It does not prove this arbitrary-indiscrete-owner `T0`
factorization theorem. Mackenzie and Fuchssteiner--Wockel remain framework
comparators at different domains; Farsi--Huang--Kumjian--Packer supplies
degree-one terminology, with its opposite coboundary sign producing the same
image after negation. None is promoted to an exact same-package owner.

| Claim | Exact owner retained | Credit stop |
|---|---|---|
| generic nerve and `C_cnv/H_cnv` collapse | Paper 12 direct proof; Paper 11 only supplies the arrow-level premise | no arithmetic or standard-theory identity claim |
| fixed packet/action/common `p^Z` | Deninger | no topology, groupoid, or cohomology credit to Deninger |
| inherited actual indiscrete orbit/packet topology | Paper 9 | no usual-circle topology |
| representative-independent marked isotropy image | Paper 12 | no claim that abstract `H^1` or the unmarked groupoid selects `c` |
| standard period quotient | Paper 12 construction using the Paper-10 topology direction | proxy only; no actual-topology or arbitrary-class orbit credit |
| full suspension, cross-prime union, traces, completions, determinants | excluded | no conclusion or Route credit |

## 6. Deterministic controls and reproduction

I read the complete generator and test suite, verified the manifest against
the checked artifacts, and independently executed:

```text
cd papers/12-marked-time-cohomology
./experiments/reproduce.sh
```

The command exited `0` and reported:

```text
Ran 88 tests in 80.539s
OK
PASS schema=paper12-marked-time-cohomology-controls/1 csv=10 rows=234 negative=12
PASS: tests, strict verification, three-way byte identity, and no-cache scan
```

The script strictly verified the checked-in directory, generated two fresh
temporary result sets, strictly verified both, and compared checked-in plus
both fresh generations byte-for-byte. The manifest SHA printed by the run was
`5337f13b07498872a97ed0d13f0ff0f5ffbcea9e3e37bf8e0c558c3e966e5d3a`.
An independent post-run scan found no `__pycache__`, `.pyc`, `.pyo`, pytest,
mypy, or ruff cache under the paper directory.

The ten checked CSVs contain 234 data rows (244 physical lines including ten
headers), and their independently checked hashes are:

| Artifact | Rows | SHA-256 |
|---|---:|---|
| `control_summary.csv` | 9 | `61fc4f8cb46f15710886a8f4f4bd6e65559ebd78367fc50cd3653b98f5ea6370` |
| `degree1_cohomology_controls.csv` | 125 | `ebd3bb8062e1c4acec70f5b28d3dca90fc9aabdb92fd90592c0f2bb0dafb6b51` |
| `factorization_controls.csv` | 6 | `888b2a95f23a80ef9eb06ef008ee9f81344612a01bce19e0ff1f88993213fce0` |
| `label_boundary_controls.csv` | 24 | `b3f82c3af8382b1d890cd25e1d496cc2b93be90104c036c15d6159ae2af91e90` |
| `morphism_controls.csv` | 20 | `00dbe2ff0e918682cfc75db6e5893631537d77111fcf60c9eff6d21c915a6d2d` |
| `negative_controls.csv` | 12 | `0a3a5c2333a0d5d2620b0f54c22e1dfeba9a8eacc336a61d6de45d9ca2736493` |
| `nerve_face_controls.csv` | 12 | `c50500cc4775abf20c96de55caf6c62330abfa79177bc7dec6eee76b20c52672` |
| `packet_period_controls.csv` | 12 | `3f13dbbbe464522d92e3e33c5b55528be6fd55e92d26b295d74c87ab83c9932e` |
| `period_controls.csv` | 10 | `b7f2450441514b87bd15f9da3598d5c05f4f11cb948679536c0af05433de5d33` |
| `quotient_topology_controls.csv` | 4 | `0bc8338ca42a3a617638c25d3a89309c0388c376fd7208cb592d020bcd9ff5df` |

Key manifest metrics independently agree with the CSVs: 161,659 face-identity
checks with zero failures; 102,171 `d^2` basis coefficients with no nonzero
row; zero `T0` continuous nonfactor maps versus 254 non-`T0` witnesses; 125
degree-one profiles with five accepted linear profiles and 120 nonlinear or
affine rejections; twelve ordered unequal positive-scale pairs, four strict
identities, and four reversals; four one-sided-topology rows; twelve schematic
packet rows over four primes with zero unit-period mismatch; and all 24 label
permutations sharing one theorem signature and recording `PROVES_TOO_MUCH`.

The tests include deliberate wrong-sign, wrong-scale-direction, reciprocal-
scale, content/hash/schema/row, missing/extra file, lock/gate, and
implementation-drift failures. Verification is fail-closed. The reserved seed
`120012` is unused; the package has no network, external data, randomness,
timestamps, fitting, zeta-zero, trace, determinant, Paper-8 coefficient, or
Paper-11 completion dependency. Packet CSVs explicitly remain schematic and
do not replace the source proof.

## 7. Preregistered falsifier audit

| Falsifier / stop condition | Independent outcome |
|---|---|
| some finite `Psi_n` is not a homeomorphism | closed by the arbitrary-finite-`n` inverse and exact open-set proof |
| a `T0`-valued cochain retains unit dependence | excluded by topological indistinguishability; the non-`T0` boundary has an explicit counterexample |
| `T` fails to commute with `d` | excluded face-by-face, including degrees zero and one |
| wrong face sign or an uncancelled `d^2` term | excluded analytically by the exact involutive pairing and computationally by 102,171 zero coefficients; the wrong-sign negative is detected |
| a nonlinear continuous real additive cocycle | excluded by the continuous Cauchy proof; nonlinear probes are rejected |
| a nonzero continuous real coboundary | excluded because all real-valued degree-zero cochains are constant |
| period depends on representative | excluded because coboundaries vanish pointwise on isotropy before descent |
| rational-Witt isotropy has an extra time or misses an integer multiple | excluded by the same-object exponential/logarithmic source chain |
| a packet unit has a different stabilizer | excluded by Deninger's every-point theorem; no orbit-to-packet inference is used |
| a strict marked isomorphism joins unequal lattices | excluded by strict covariance and least-positive generators |
| the explicit positive-scaled isomorphism fails | all algebraic/topological laws and all twelve ordered unequal controls pass |
| subgroup equality characterizes strictness | refuted by orientation reversal |
| every weaker morphism changes the subgroup | expressly not claimed; orientation reversal and dense `Q` are countercontrols |
| standard quotient and actual orbit are homeomorphic | refuted in the inverse direction; only standard-to-actual continuity holds |
| scaled dilation belongs to the strict target category | refuted unless `alpha=1` |
| `c` has Paper-11 global-QC support | refuted: `c` is unbounded and has all-arrow support |
| generic collapse supplies arithmetic specificity | refuted by arbitrary `H`, four frozen periods, and label permutations |
| a packet/global/all-prime promotion occurs | absent; `G^global` and cross-prime conclusions are explicitly excluded |

No preregistered theorem falsifier fired. The expected scope falsifiers did
fire where required, especially non-`T0`, label-swap, wrong-sign,
wrong-direction, topology inverse, and global-QC controls.

## 8. Nonredundancy and standalone decision

I applied the `STANDALONE_PASS`/`NOTE_OR_MERGE` rule independently rather than
treating successful algebra as sufficient. The inherited material is
substantial: Paper 11 already supplies arrow-level topology and `T0`
time-factorization; Blanco--Uribe--Waldorf supplies a close continuous-nerve
cochain convention; Deninger already owns the packet and stabilizer; Paper 9
owns the actual topology. The bare existence of a nerve complex or the formula
`H_x=(log p)Z` therefore carries no standalone weight here.

The proved delta nevertheless does not reduce to those ingredients:

1. it proves a natural, all-degree cochain-complex isomorphism at exact faces
   and signs for the arbitrary indiscrete action owner and every named `T0`
   coefficient group, with a sharp coefficient counterexample;
2. it turns the source mark into a representative-independent isotropy-image
   construction on both the exact orbit and every unit of the exact packet;
3. it gives a fully typed three-category variance theorem, an explicit
   unequal-period positive-scaled isomorphism, and a same-period unmarked
   nonconverse, fixing both the direction and the limits of invariance; and
4. it constructs the normalized strict pointed quotient functor together
   with naturality, basepoint rotation, the one-sided actual-topology map, and
   the precise semilinear obstruction to extension across scaled morphisms.

The category and quotient results are elementary individually, but their
joint role is not cosmetic: they state exactly which marked information
survives which morphisms, supply explicit counterisomorphisms at both weaker
levels, and identify the maximal registered functorial target without
transporting the actual topology. Combined with the all-degree collapse and
the every-unit packet application, this is a substantive theorem package
beyond Paper 11 plus the BUW convention. The deterministic controls further
show that the generic mechanism is deliberately arithmetic-blind rather than
quietly fitted to prime labels.

The bounded Phase-2 audit found no direct source satisfying the same owner,
full locked unnormalized nerve, marked isotropy image, and
strict/scaled/unmarked-plus-quotient conjunction. Its admissible wording
remains exactly `SUPPORTED_WITHIN_SEARCH`; no priority or global-absence claim
is licensed.

Accordingly neither mandatory `NOTE_OR_MERGE` trigger fires:
`ORBIT_ONLY=false`, the packet claim is proved at every unit, and the
category/quotient delta survives the Paper-11/BUW comparison. My exact
standalone-content disposition is therefore **`STANDALONE_PASS`**.

This judgment does not raise the Route ceiling. The generic collapse remains
an action-blind control; the actual marked period may inherit only its
registered source relation; the standard quotient is a proxy; no trace,
primitive-orbit amplitude, determinant, completion, all-prime, or full-
suspension credit follows.

## 9. Finding register and freeze record

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
stable_tuple_reviewed: true
proof_hashes_match: true
implementation_hashes_match: true
manifest_hash_matches: true
source_checksum_ledger: PASS_10_OF_10
source_preflights: PASS_NO_WARNINGS
reproduce_exit_code: 0
tests: 88_PASS
strict_verification: PASS
three_way_byte_identity: PASS
no_cache_scan: PASS
findings: C0/M0/m0
phase3_peer_verdict: PASS
standalone_disposition: STANDALONE_PASS
freeze_basis: current_stable_bytes_only
await_future_v3: false
```

**Final review verdict: PASS (`C0/M0/m0`), with
`PACKET_COROLLARY`, `ORBIT_ONLY=false`, and `STANDALONE_PASS`.**

## V4 closure addendum — final integrated Phase-3 peer review

**Version:** `P12-P3-PEER-V4-CLOSURE-1`  
**Date:** 2026-08-15  
**Mode:** append-only review of frozen bytes; no reproduction run

The preceding 23,121 bytes (433 lines), SHA-256
`12abc205f2e599035ac8fa64346d25672bcadcbea55bca98b88151e5a13022b9`,
are the unchanged historical v2 review. This addendum is the binding review
of the final v4 package.

### Frozen receipt

```text
research_protocol=a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f
candidate_lock=654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41
pipeline_state=f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf
v2_core_proofs=9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd
v2_marked_packet_proofs=3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49
v4_final_proof=77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8
v4_math_review=97dbd63fae6d35ae627520203db98d7c497a927a505599c0855231ac3f3b4e07
control_manifest=7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95
controls_review=886a2648473035bb4d3600a03474680d3f692b1bdca08034096c6e7eebd664e6
source_novelty_audit=cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22
standalone_review=639dc289c024588777a05d46ff9e5cd47b6e50ceeb807ef7571776d0301e6895
route_provenance_amendment=db1fe49108ab3697596847571bcdadbed1e6df251cc941b7d51b6c15780372a7
route_provenance_relock=20c67ace45b81523400053b388923e4a01c725b0bfdd528f2c391803ded0cb4d
proof_audit=c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab
```

The v4 design, amendment, methodology, adversarial, final-gate, and status
reviews were also read on their frozen bytes. Their conclusions agree with
the receipt above; no vote is used to replace proof.

### Integrated checks and disposition

The proofs establish the actual all-degree complex and factorization,
`H_cnv^1(G_actual)=R[c]` with `B_cnv^1(G_actual)=0`, and the frozen
source-period packet result. For a nonempty common-stabilizer orbit set `Q`,
the constructed open-coproduct topology, `Std_coprod`/`Indisc`
full-faithfulness, the canonical automorphism extension (with only a
choice-dependent split), and
`H_cnv^1(G_std)=R^Q` with generally nonzero standardized coboundaries are
proved at their stated domains. The comparison direction is
`J:G_std->G_actual`; `J^*` is the constant diagonal, exactly the strict
time-preserving automorphism invariants. The fixed-prime conclusion is a
packet corollary and preserves the four distinct actual/standard groupoid
and actual/discrete quotient records.

Owner and source boundaries are conserved: Deninger supplies the fixed-prime
flow/clock/stabilizer, Paper 9 the actual packet and quotient topology,
Paper 11 only its retained arrow/time-factorization inputs, and Paper 12 the
author complex, constructed standardization, and comparison. No actual
quotient count/topology, arithmetic selectivity, named-theory identity,
higher cohomology, or priority claim is inferred. The novelty ceiling remains
`SUPPORTED_WITHIN_SEARCH`; all ten local source-ledger entries verify.

The frozen manifest and controls review bind 122 passing tests and 11 CSV
artifacts with 3,486 rows; schema, row-count, hash, and strict three-way byte
checks pass. No local generator, test suite, or reproduction script was run
for this addendum. The reported shared-workspace duplicate-run incident is
retained as a nonblocking orchestration advisory: it violated serialized
top-level ownership, but contributed no accepted evidence, byte drift,
cache, temporary residue, or control failure. Future execution must have one
top-level run owner.

The former routine-reduction major is closed by the same-carrier topology
change, full/faithful comparison, arbitrary-orbit automorphism theorem, and
the proved enlargement from `R` to `R^Q`. The independent final disposition
therefore remains `STANDALONE_PASS`.

### Authorization boundary

The final provenance amendment has been independently relocked on the
canonical field `route_b_invocation_allowed: false`, and the detached
pre-Route `proof_audit` exists and passes at the hash above. Accordingly this
review authorizes **only** final pre-Route receipt integration and one formal
Route-A evaluation of the eight frozen candidate owners. It does not evaluate
or prejudge `P12-10`; no Route output is bound here, and Route B remains
forbidden.

Composition, manuscript drafting, citation/declaration clearance, release,
and public synchronization remain blocked behind their separate downstream
gates.

```text
review_version=P12-P3-PEER-V4-CLOSURE-1
integrated_peer_verdict=PASS
critical_open=0
major_open=0
minor_open=0
standalone_disposition=STANDALONE_PASS
prior_routine_reduction_M1=CLOSED
proof_audit=PASS
pre_route_integration_authorized=true
route_a_evaluation_authorized=true
route_b_invocation_allowed=false
composition_authorized=false
manuscript_authorized=false
release_authorized=false
```

**Final v4 integrated peer verdict: PASS (`C0/M0/m0`) with
`STANDALONE_PASS`; only pre-Route integration and Route-A evaluation are
opened.**
