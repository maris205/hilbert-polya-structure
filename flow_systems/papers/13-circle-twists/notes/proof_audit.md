# Paper 13 integrated proof, ownership, controls, Route, and technical-note audit

Audit date: **2026-08-15 (Asia/Shanghai)**

Mathematical verdict: **PASS — P13-1 through P13-8C are proved at their exact owners**

Independent proof findings: **C0 / M0 / m0**

Publication disposition: **PASS TO TECHNICAL NOTE; NOTE_OR_MERGE remains binding**

Standalone disposition: **C0 / M1 / m0; STANDALONE_PASS=false; the Major is not closed or downgraded**

Deterministic controls: **effective PASS — 176/176 tests, 12 CSVs, 2,665 body rows, 67/67 explicit negatives, 13 generated artifacts, three byte-identical copies**

Route disposition: **10 Route-A records, 3 exploratory and 7 rejected; every A2--A4 coordinate fails; Route B is false**

Manuscript, bibliography, figure, declaration, release, Git, and public-sync status: **not authorized by this audit**

## 1. Scope and acyclic boundary

This audit integrates the active Paper-13 locks, the bounded Phase-2 source
and precedent record, all three stable proof streams and their independent
reviews, the replacement deterministic-control tuple, the binding
standalone review, the technical-note disposition gate, and the final ten
owner-local Stage-13 Route-A records.

It creates no theorem and changes no proof. It audits what may be composed,
who owns each premise and conclusion, which topology and completion each
formula inhabits, and which claims must remain negative.

The dependency graph is one-directional:

    active locks and source audits
        -> stable core/support/corona proofs and peer reviews
        -> stable replacement controls and independent controls review
        -> standalone NOTE verdict and technical-note disposition
        -> ten Stage-13 Route-A YAMLs
        -> route_audit.md
        -> this integrated proof audit
        -> downstream composition blueprint

The final Route audit does not bind this file. This file does not bind the
downstream composition blueprint. The blueprint may bind this file's
detached SHA-256 after these bytes are frozen. No self-digest is embedded.

The audit preserves two simultaneous conclusions:

1. the mathematics is correct at C0/M0/m0; and
2. the proposed standalone centre reduces, after component isometries, to a
   generic constant-diagonal lemma for a c0 sum, so the binding standalone
   Major remains open and the publication form must be a technical note.

## 2. Exact-byte evidence lock

Every digest in this section was independently recomputed before this audit
was written.

### 2.1 Active protocol, candidate, and Phase-1 lock

| Artifact | SHA-256 | Role |
|---|---|---|
| notes/research_protocol.md | 519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064 | active objects, claims, owner firewalls, Route and release boundary |
| notes/candidate_lock.md | 8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266 | amended candidate and exact cochain/algebra domains |
| notes/pipeline_state.md | d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5 | unchanged active-state receipt |
| notes/phase1_amendment_v1.md | ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27 | typed gauge/support centre and ten-owner registry |
| notes/phase1_final_gate.md | 8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19 | independent Phase-1 closure |

### 2.2 Phase-2 source, convention, and bounded-precedent lock

| Artifact | SHA-256 | Exact strength |
|---|---|---|
| notes/phase2_framework_source_audit.md | b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592 | source hypotheses, exact locators, named-framework applicability |
| notes/phase2_convention_owner_audit.md | 498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52 | normalization, signs, gauge direction, source ownership |
| notes/phase2_novelty_search.md | 444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea | dated bounded search; Arm-A prior art confirmed |
| notes/phase2_final_review.md | ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9 | Phase-2 PASS C0/M0/m0 |
| notes/sources/framework_source_manifest.md | 4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e | retained source and locator ledger |
| notes/sources/framework_sources.sha256 | 7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f | retained-source checksum ledger |

The maximum external-precedent wording is
**SUPPORTED_WITHIN_SEARCH**, with cutoff 2026-08-15. The bounded search found
no direct exact-package match, but it confirmed prior art for the real-line
collapse and standard twisted-algebra ingredients. It does not establish
firstness, priority, novelty, or standalone weight.

### 2.3 Stable proof and independent-review lock

| Artifact | SHA-256 | Integrated role |
|---|---|---|
| notes/phase3_core_twist_proofs.md | 62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd | P13-1--P13-5 |
| notes/phase3_core_peer_review.md | a96a91adb1474062656cbca4d677019f952b5fb84775bda952b6c996a700e665 | independent core PASS C0/M0/m0 |
| notes/phase3_support_retention_proofs.md | f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811 | P13-6--P13-8 |
| notes/phase3_support_peer_review.md | ded657fb7022114527e99a8c0bc12d9f70d9b4ca3f976a6335065190d0640bed | independent support PASS C0/M0/m0 |
| notes/phase3_standalone_amendment_v2.md | 99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82 | base P13-8A--C design |
| notes/phase3_standalone_amendment_v2_ownership_addendum.md | d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f | Paper-2 credit and owner correction |
| notes/phase3_v2_methodology_review.md | 96a5067015847ff88155b91658ae94e9ef5a6355ae176c1945644b3e729f4f74 | final amended-tuple PASS |
| notes/phase3_v2_devils_advocate.md | 1c6bbb0bc7d3fc366de4d8a4eb869d4d4708f19647f10d780be095ac9e81f110 | final amended-tuple PASS |
| notes/phase3_v2_source_feasibility.md | 3ce4e8db7914c0053a31b7e0e08e8f0fe02e0b2db15620f194c1ccae5ffeb320 | final source/ownership PASS |
| notes/phase3_v2_design_gate.md | 0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706 | bounded P13-8A--C proof authorization |
| notes/phase3_v2_corona_proofs.md | 81b0f8aaa1cf6277323452c55107cf33d8ad69783eb80998cc0f4f0d9d636858 | final P13-8A--C proof |
| notes/phase3_v2_corona_peer_review.md | 0ae271fd99f3290d7d18486cfc98ad8ccf95aa1421619ccd4fdf72865deb28c8 | independent corona PASS C0/M0/m0 |

### 2.4 Replacement control lock

The initial control implementation had a review-level Major because its
oracle paths were not sufficiently independent. Its first-run manifest is
historical and is not downstream evidence. The exact replacement tuple is:

| Artifact | SHA-256 | Status |
|---|---|---|
| notes/phase3_control_design_lock.md | 900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c | immutable v1 base |
| notes/phase3_control_design_amendment_v1.md | 5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e | amended-v1 row closure |
| notes/phase3_control_design_review.md | bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184 | final v1 design PASS |
| notes/phase3_control_design_amendment_v2.md | 0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9 | v2 design head |
| notes/phase3_control_design_v2_review.md | 4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6 | v2 design PASS |
| notes/phase3_v2_control_implementation_gate.md | e3226570f6d9630d5a912cb6b189d194bd33df395e276ce56d48ad75f9601312 | initial implementation authorization |
| notes/phase3_v2_control_remediation_gate.md | 1ffba02ae468f7f847146a82a51c2e221aa25a64e65330cddd27504c2a971a42 | exact oracle-remediation authorization |
| notes/phase3_v2_controls_review.md | c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789 | effective replacement PASS C0/M0/m0 |
| results/manifest.json | 26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2 | stable replacement manifest |

The six stable implementation hashes are:

| Path | SHA-256 |
|---|---|
| code/generate_controls.py | 8eabcc08426d16a2b12784fb060c7aa55214e544957098488b6deee138577829 |
| code/test_controls.py | 64d031244d112ff93c518c2e6d1df84d198b8051ab5ba462dfcdf057c1f61aaf |
| code/README.md | fa18564c8aa001cc8e287a8d0520f8696499f2658083bef3c7ee029361df954b |
| experiments/reproduce.sh | a1013af1ad852d30ce0f67aba8c9421118181c5612cc95de228199fa3d3fbdcd |
| experiments/README.md | 3e014b0c997d62c7cf9eea30a436033cd8a49982a7bb342e23b08ddb58042ade |
| results/README.md | 99d4a3bd2a71374157b63458fbe21df3f32745da1935b82ef55aceaf86f6074c |

The manifest binds no concurrent proof digest and never hashes itself. Stable
proof and stable controls meet here as separate inputs. The controls remain
finite diagnostics and policy ledgers, not proof of continuum cardinality,
arbitrary-index multiplier identities, completion norm chains, or corona
faithfulness.

### 2.5 Binding publication disposition

| Artifact | SHA-256 | Binding result |
|---|---|---|
| notes/phase3_standalone_review.md | 0397e1555a1ff07d30f06c3182b6cf570228ccd3e8db9e3c96666d118079c224 | original NOTE_OR_MERGE |
| notes/phase3_v2_standalone_review.md | ee31c644f9569abecae91ce0ca1054ad480485670caf41cf289a8e3f5ccb0c0e | C0/M1/m0; generic constant-diagonal reduction |
| notes/phase3_v2_note_disposition_gate.md | b60c88a33bb3bb5c4f87448aaaf8f2d4020fa945bc9f204fd81d07ea85d7d03e | PASS_TO_TECHNICAL_NOTE |

The technical-note gate selects the NOTE branch; it does not close the
standalone Major. A later document may not report STANDALONE_PASS.

### 2.6 Mandatory internal-owner subtraction

| Companion | SHA-256 | Exact inherited role |
|---|---|---|
| Paper 2 manuscript | 72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc | Proposition prop:uncountable, sign/procyclic continuum lower bound |
| Paper 2 proof audit | aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae | accepted lower-bound proof and topology ceiling |
| Paper 8 manuscript | c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa | one-orbit proxy, trace/return results, scalar ledger |
| Paper 8 proof audit | 1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990 | local-versus-packet and scalar-owner firewall |
| Paper 9 manuscript | 24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb | actual packet, actual topology, stabilizer, bare U_p/H_p |
| Paper 9 proof audit | c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8 | exact packet/bare-owner receipt |
| Paper 11 manuscript | eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002 | actual time collapse, untwisted author algebra and transports |
| Paper 11 proof audit | 03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28 | owner-safe untwisted boundary |
| Paper 12 manuscript | c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163 | all-degree factorization, standardization, components, J |
| Paper 12 proof audit | c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab | actual/standard/bare/discrete owner firewall |

### 2.7 Final Route lock

The final Route audit is notes/route_audit.md, SHA-256
2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9.
It binds exactly the ten YAMLs in Section 10. All eleven Route hashes
recomputed exactly. The audit reports schema, path, artifact-hash, count, and
acyclic-DAG validation PASS. It did not rerun controls.

## 3. Frozen objects, topologies, and analytic records

| Record | Exact owner/domain | Permitted conclusion | Forbidden promotion |
|---|---|---|---|
| TIME-R-CONT-TWIST | usual locally compact Hausdorff one-object group R | continuous normalized circle multipliers, time product/star, projective regular representation | packet, action, period, or arithmetic credit |
| G_actual(X) | X_indisc semidirect R, X nonempty, product arrow topology | globally continuous normalized cochains and Paper-11 author fibre records | standard Hausdorff groupoid C-star naming |
| actual non-Hausdorff branch | preceding owner with cardinality of X at least two | named audited Hausdorff/local-Hausdorff frameworks do not apply | claim that no framework exists |
| singleton control | X is a singleton | exactly the usual time group | calling it non-Hausdorff or etale |
| T | usual Hausdorff circle, trivial action | continuous normalized one- and two-cochains | Borel-only, smooth-only, bounded, or measurable substitution |
| H_tw^2 | abstract gauge quotient | algebraic zero-class statement | quotient topology |
| A_sigma | C_c(R) time algebra and its author actual pullback | exact twisted product, star, support, gauge | global actual twisted groupoid algebra |
| TW-FULL-TRANSPORT | author full record transported through time and gauge | restriction agrees with the standard time-group maximal norm | C-star algebra of the actual groupoid |
| TW-RED-TRANSPORT | author reduced record transported through the projective regular representation | separately typed reduced norm | inference from or identification with the full owner before proof |
| Q^bare | nonempty orbit-index set only | finite/infinite predicate and arbitrary-index c0 sum | topology, measure, enumeration, or count |
| Std(X) | Paper-12 coproduct of compact open R/H torsors, H=LZ | standard compact support and component records | actual topology or reflection status |
| J | continuous identity functor G_std to G_actual | pullback of actual functions to standard owner | reverse continuous identity |
| B_(q,sigma)^epsilon | one standard compact-orbit component, epsilon=max or r | component test map and completed isometry | canonical common origin or equality of whole max/r component algebras |
| A_(std,sigma)^epsilon | author c0 sum of the component records | arbitrary-index multiplier product and selected diagonal | unaudited global twisted groupoid C-star naming |
| M(A)/A | corona of the author c0 sum | exact location and norm of the selected diagonal | classification of the full corona or owner-specific obstruction |
| Q_p^actual | Paper-9 actual quotient | indiscrete, second countable, non-Hausdorff context | discrete topology or standard topology failures |
| Q_p^bare | underlying fixed-prime orbit set | continuum cardinality | topology |
| Q_p^disc | discrete quotient of the standard coproduct | non-second-countability and non-sigma-compactness | topology of Q_p^actual |

The gauge orientation is frozen:

    sigma overline(tau) = delta alpha,
    (delta alpha)(s,t) = alpha(s) alpha(t) overline(alpha(s+t)),
    U_alpha : A_sigma -> A_tau.

All support statements use that a circle-valued gauge is nowhere zero.
Maximal and reduced statements are serialized and proved separately. The
amenability endpoint belongs only to the usual group R. No equality of the
entire maximal and reduced component algebras is claimed.

## 4. Integrated target matrix

| Target | Exact audited result | Owner | Proof locator | Nonpromotion ceiling |
|---|---|---|---|---|
| P13-1 | degree-one and degree-two actual cochains into T factor through time | inherited actual/time bridge | core proof §3 | Paper 12 owns all-degree T0 factorization; no P13 novelty |
| P13-2 | normalized cocycle, coboundary, and gauge quotients commute exactly with time reduction | actual and time cochain quotients | core proof §4 | author convention only; no quotient topology |
| P13-3 | H_tw^2(R;T)=0, hence the actual quotient is zero; trivializers differ by continuous characters | usual R, then typed actual pullback | core proof §5 | Sorkin owns advertised prior theorem; P13 owns only the sign-exact direct verification |
| P13-4 | twisted product, support, associativity, involution, and oriented gauge-star isomorphism | time C_c(R) and Paper-11 author actual domain | core proof §6 | standard formulas are prior; no global actual groupoid completion |
| P13-5 | projective regular representation, full/reduced norm restrictions, choice independence, amenable time equality | standard time group and separately named author transports | core proof §7 | max/r separate; no equality of whole components or actual groupoid C-star naming |
| P13-6 | exactly TIME-GAUGE, ACTUAL-TW-TEST, ACTUAL-TW-FULL, and ACTUAL-TW-RED are constant after tags are forgotten | four registered records only | support proof §§3--4 | not every invariant; literal stabilizer/topology/period remains |
| P13-7 | on the registered fixed-prime owner the scalar twist adds no restricted continuous cohomology-class invariant | exact packet and literal H=(log p)Z | support proof §5 | no prime recovery, period erasure, trace, or amplitude |
| P13-8 | J-pullback support is Std(X) times supp(f); compact support iff f=0 or Q^bare is finite; infinite image intersection is zero | common-lattice actual/standard pair | support proof §§6--10 | test-function statement; finite-Q map gives no completion theorem |
| P13-8A | P13 upper bound closes continuum equality; standard/discrete topology consequences follow | Q_p^bare, Q_p^disc, standard unit/arrow owners | corona proof §2 | Paper 2 owns lower bound; Papers 9/12 own carrier/standardization; zero standalone credit |
| P13-8B | component maps are isometric for max/r; arbitrary-index multiplier product, diagonal membership, exact corona norm, actual-author map, and gauge squares hold | separately typed component/c0/multiplier/corona author records | corona proof §§3--9 | corona step is generic after isometries; no full target classification |
| P13-8C | for each prime and both epsilon values every nonzero time element lies outside the c0 algebra and survives isometrically in the corona | fixed-prime standard author records | corona proof §10 | inherited infinitude; no prime-sensitive invariant |
| P13-9 | replacement deterministic package reproduces exact finite diagnostics and policy negatives | control package | manifest and controls review | controls are not proof |
| P13-10 | framework/source and exact-package precedent audits are closed at bounded strength | source record | Phase-2 and v2 source reviews | SUPPORTED_WITHIN_SEARCH only |
| P13-11 | ten owner-local Route-A records are complete | ten exact owners | route_audit.md | 3 exploratory, 7 rejected, Route B false |

## 5. Proof dependency and ownership-conservation ledger

The mathematical dependencies are:

    Paper-12 T0 factorization
        -> P13 normalized time/actual bridge
        -> sign-exact P13 direct real-line proof
        -> twisted author product/star and transported records
        -> four named nonretention conclusions

    Paper-11 actual support + Paper-12 standardization/J
        -> P13 zero/finite/infinite support and intersection theorem

    Paper-2 continuum lower bound + P13 elementary upper bound
        + Paper-9 bare carrier + Paper-12 standardization
        -> P13-8A equality/retyping/topology context

    standard untwisted component sources + P13 component gauge proof
        -> separately typed max/r component isometries
        -> generic constant-diagonal c0/multiplier/corona lemma
        -> P13 actual-author and fixed-prime instantiations

No arrow reverses. Controls do not prove a theorem. Route does not change a
theorem. The technical-note label does not promote a Route coordinate.

## 6. Direct mathematical audit

### 6.1 Normalized reduction and real-line collapse

The inherited factorization gives actual one- and two-cochains as pullbacks
through pi_1(x,t)=t and pi_2(x;t,u)=(t,u). P13 verifies directly that delta
is normalized, is a cocycle, and commutes with those pullbacks. Thus the
actual and time gauge quotients are isomorphic at the frozen signs.

For the time multiplier, the proof lifts the phase to a real function,
shows its integer-valued cocycle defect is zero, kills the commutator in one
dimension, smooths without changing the class, and obtains

    q = delta(h-A),
    alpha = exp(i(h-A)),
    sigma = delta alpha.

If alpha and beta trivialize sigma, beta/alpha is a continuous character.
The proof uses no inaccessible sign or normalization from Sorkin. Sorkin's
official title/abstract remains mandatory prior credit for the theorem's
advertised strength.

### 6.2 Twisted test algebra and transports

On C_c(R),

    (f *_sigma g)(t)
      = integral f(u) g(t-u) sigma(u,t-u) du,

    f^{*sigma}(t)
      = overline(sigma(t,-t)) overline(f(-t)).

The proof checks support, continuity, absolute Fubini, associativity, both
star laws, the inverse-face identity, and the oriented gauge map. The actual
author formula is obtained only through Paper 11's time-only Phi map and is
not renamed as a standard groupoid convolution.

The projective regular representation and its integrated form are exact.
The author full and reduced transports are separately identified with
restrictions of the standard twisted time-group norms. Trivializer changes
act by a continuous character and preserve both norms. Amenability of R
identifies the two time endpoints, not every element of two whole component
algebras.

### 6.3 Named nonretention and literal-stabilizer firewall

P13 proves constancy only for the four registered outputs:

- TIME-GAUGE;
- ACTUAL-TW-TEST;
- ACTUAL-TW-FULL; and
- ACTUAL-TW-RED.

For a literal stabilizer H_x, the restricted class of a globally trivial
cocycle is zero because the global trivializer restricts. This does not
erase H_x, its embedding, topology, period, marked clock, or representations.
A dense subgroup such as Q is only a continuous-cochain control; no Haar,
regular, or C-star statement is made on it.

### 6.4 Actual-to-standard support

For Phi(f)(x,t)=f(t), pullback along J has support

    Std(X) x supp(f).

It belongs to C_c(G_std) exactly when f=0 or Q^bare is finite. For infinite
Q, the time-only image intersects the standard compact-support algebra only
at zero. Gauges preserve support. For finite Q, the test-level map is a star
homomorphism into the time-only subalgebra; no norm or completion claim is
deduced from that finite test statement.

### 6.5 Fixed-prime cardinality and four-owner topology

Paper 2 owns the hard lower bound and sign/procyclic argument. P13 proves
only the elementary upper bound

    |U_p| <= (2^aleph_0)^aleph_0 = 2^aleph_0

and combines it with the inherited lower bound to obtain

    |Q_p^bare| = |U_p/H_p| = 2^aleph_0.

The actual quotient stays indiscrete and second countable. The bare set has
no topology. Only Q_p^disc, Std(Gamma_p), and its standard arrow space are
non-second-countable and non-sigma-compact. No topology crosses those owner
boundaries.

### 6.6 Component norm chain

For each compact standard orbit O_q, the origin-free test map is

    d_(q,sigma)(f)(x,t)=f(t).

The unit-regular restriction is the intrinsic twisted time representation.
The maximal upper bound and the reduced restriction close the exact chain

    ||f||_(time,max)
      >= ||d_q(f)||_(component,max)
      >= ||d_q(f)||_(component,r)
       = ||f||_(time,r)
       = ||f||_(time,max).

Therefore both component maps extend isometrically. This is a result about
the selected image. It does not assert equality of the whole maximal and
reduced component algebras.

### 6.7 Generic constant-diagonal lemma and instantiation

For an arbitrary nonempty set I, C-star algebras C and B_i, and isometric
star homomorphisms phi_i:C->B_i, put A=direct-sum_i^c0 B_i. Then the constant
diagonal Delta(c)=(phi_i(c)) belongs to M(A), is isometric, and lies in A
exactly when c=0 or I is finite. If I is infinite, its corona image is
faithful and

    dist(Delta(c),A)=||c||.

This lemma uses no packet, prime, twist, orbit topology, or common origin.
P13's component proof supplies the phi_i; the subsequent membership and
corona theorems instantiate this generic lemma. Gauge covariance and the
actual-author map are exact naturality and typing data. Fixed-prime
unconditionality follows because the inherited continuum result makes the
index infinite. The conclusion does not distinguish primes.

This direct reduction is the reason the mathematics passes while standalone
status does not.

## 7. Claim/source/owner/domain/control/Route matrix

| Claim surface | Prior/source owner | P13-owned proved delta | Domain | Control witness | Route owner |
|---|---|---|---|---|---|
| factorization | Paper 12 | normalization and gauge commutation | actual/time cochains | nerve and cocycle ledgers | GEN-INDISC-R-ACTION-CONT-TWIST |
| real-line collapse | Sorkin advertised theorem | sign-exact direct proof and character ambiguity | usual R | lift and gauge ledgers | TIME-R-CONT-TWIST |
| twisted formulas | Austad; Paper 11 untwisted baseline | actual fibre identities and exact gauge direction | time test algebra and actual author domain | convolution/involution/gauge ledgers | GEN-INDISC-R-ACTION-TWISTED-GLOB-QC |
| full transport | Austad/Leptin/Hulanicki; Paper 11 | exact norm restriction and choice independence | named author full record | completion-gauge ledger | GEN-INDISC-R-ACTION-TW-FULL |
| reduced transport | Austad/Leptin/Hulanicki; Paper 11 | exact regular intertwiner and choice independence | named author reduced record | completion-gauge ledger | GEN-INDISC-R-ACTION-TW-RED |
| fixed-prime twist negative | Deninger/Paper 9/Paper 12 inputs | zero restricted class and no added registered invariant | exact actual packet | action/period and negative ledgers | DEN-EF-ACTUAL-PACKET-CONT-TWIST-P |
| fixed-prime author test algebra | Papers 9/11 inputs | typed twisted identities on the exact domain | actual packet author record | convolution and action ledgers | DEN-EF-ACTUAL-PACKET-TWISTED-GLOB-QC-P |
| support transfer | Papers 11/12 | exact zero/finite/infinite iff and gauge invariance | actual/standard common-H pair | support-transfer ledger | GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER |
| component/corona | standard component and generic c0 facts | component isometries, exact typed instantiation and gauge squares | component/c0/multiplier/corona author records | v2 corona ledger, analytic only | GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER |
| fixed-prime equality/corona | Paper 2 lower bound; Papers 9/12 owners | upper equality closure, owner typing, unconditional instantiation | Q_p^bare and fixed-prime standard author records | owner/evidence rows, not proof | DEN-EF-ACTUAL-STD-QC-SUPPORT-TRANSFER-P |
| nonselectivity | no positive source owner | exact finite policy and domain diagnostics | CONTROL_ONLY | negative-domain and v2 corona ledgers | TWIST-DOMAIN-NONSELECTIVITY-CONTROL |

## 8. Source and framework applicability matrix

| Source/framework | Exact locator or audited strength | Applies to | Does not license |
|---|---|---|---|
| Sorkin, 1978 | official title/abstract and DOI 10.1007/BF00674107 only | advertised continuous real-line remultiplication result | P13 signs, normalization, proof steps, actual-owner transfer, or completions |
| Austad, 2021 | physical pp. 5--7; Proposition 2.4, printed p. 7 | continuous twisted-group formulas and amenable time norm | actual non-Hausdorff groupoid theorem |
| Leptin | Satz 6, physical p. 14 / printed p. 204 | generalized L1 full/reduced endpoint | author transport before identification |
| Hulanicki, 1964/1966 | printed pp. 56--58 and 87--88 | group amenability/weak-containment context | exact actual-groupoid completion |
| Kleppner, 1965 | Borel/Borel multiplier background | historical terminology | continuous trivializer |
| Packer--Raeburn, 1989 | DOI 10.1017/S0305004100078129; publisher-level scope | generic twisted crossed-product prior | P13 actual-owner theorem or novelty |
| Buss--Holkar--Meyer | Corollary 6.2 p. 21; Theorem 7.1 p. 23 | untwisted Hausdorff component bridge; second countability is not required | actual non-Hausdorff owner or an audited global twisted record |
| Williams draft 3.1 | Lemma 2.27, Remarks 2.29--2.30, Proposition 2.34, equation 4.63, Theorems 4.30 and 7.13 | ordinary component crossed products and amenable group action norms | faithfulness of the time C-star map from group-valued injectivity alone |
| Austad--Ortega | second-countable LCH Hausdorff etale groupoid | hypothesis comparator | nondiscrete R or actual owner |
| Tu | locally Hausdorff convention | hypothesis comparator | nowhere locally Hausdorff actual owner with at least two units |
| Stacks Tag 0B1W | set-indexed coproduct | standard coproduct background | action, cardinality, completion, or actual topology |

Correct framework wording: for an actual owner with at least two units, the
named audited Hausdorff Haar, Hausdorff etale, and locally Hausdorff
frameworks do not apply. This is not a claim that no framework exists.

## 9. Deterministic-control matrix

| CSV | Rows | Columns | Negatives | SHA-256 | Exact role and ceiling |
|---|---:|---:|---:|---|---|
| nerve_factorization_controls.csv | 280 | 17 | 0 | a00d2d6439aee3022703940b36892136ef7083d49541d2d8ad3bfd994a7582ba | finite factorization diagnostics |
| circle_multiplier_cocycle_controls.csv | 500 | 20 | 0 | 21a5246dba9dbe573a56fa9a0c18399061ff3e09d0238f68213123f3fa77e0a7 | normalized cocycle terms |
| lift_integer_defect_controls.csv | 500 | 20 | 0 | 598d414e46a7d34d1ab6a70b0047967047d984f24a3443aa19224a14a12da5b8 | finite lift/defect checks |
| gauge_coboundary_controls.csv | 196 | 19 | 0 | c8717d8748691e92e8a7ea7ec1a196a5f42d5e151ee6e51244e2875f59677f26 | frozen gauge orientation |
| twisted_convolution_controls.csv | 78 | 23 | 0 | 2874817f2af1d3da31a29f497eba770eeac9c7275e6cc8693a7fa468fb482add | finite product diagnostics |
| twisted_involution_controls.csv | 54 | 26 | 0 | 114228b425905d5e235576b34f57eb15a0fd987065d4d206726045cceee569b5 | finite star diagnostics |
| completion_gauge_controls.csv | 756 | 28 | 0 | e7b8253a7d501b0c7b1d81939b59bfdc2f441b20592c678f749e643c0b800b2a | finite max/r gauge and norm models |
| action_period_nonretention_controls.csv | 56 | 20 | 0 | 9361f555cec4f74cab12faf30595e74830a00b44d7890e43579eae81ddcc9ee1 | named-output nonretention models |
| negative_domain_controls.csv | 20 | 12 | 20 | 82b9e5988b30a8212235558af98a787df823213a7b0ad82be7d080da7c84c123 | exact domain/firewall negatives |
| actual_standard_support_transfer_controls.csv | 96 | 21 | 27 | 7bfb8ca2ed176d1a7aca2e5aa3680fd2d3992ef1d8e86a79b22c971912051176 | finite support and owner witnesses |
| target_summary.csv | 12 | 11 | 0 | 97c2052c6286dd2013f735a79e7331d7a29f2bba7b2575fdc226865a34528f60 | immutable v1 snapshot |
| completion_corona_controls_v2.csv | 117 | 41 | 20 | 672a29d4ac1b220336527517e50ba855f6a0c93568effd9b97e792015e4b2c41 | finite c0/tail/gauge models plus analytic owner/evidence ledgers |

Package totals are exactly 12 CSVs, 2,665 body rows, 67 negatives, 176
discoverable tests, and 13 generated artifacts including the manifest. The
v2 CSV contains 84 diagnostics, 20 negatives, and 13 summary rows. The
effective independent run passed with two fresh generations and three
byte-identical copies. No rerun is authorized or needed for composition.

## 10. Final Route-A ledger

| # | Owner and YAML SHA-256 | Exact A0--A4 tuple | Verdict and boundary |
|---:|---|---|---|
| 1 | TIME-R-CONT-TWIST — e10c099de4a3468aee163efaff28d817ae55e2af505b3f88fccc8b160587c4f1 | (A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL) | REJECTED; generic time group |
| 2 | GEN-INDISC-R-ACTION-CONT-TWIST — e8b3c85a8d08554130cae1c44183262de908bff27315a2f7cdb6098527e2ef3c | (A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL) | REJECTED; universal action-blind cochain owner |
| 3 | GEN-INDISC-R-ACTION-TWISTED-GLOB-QC — 24596827430fb6c77fb349379b13ed17ad3a0b95cbd85f21e183f6c4bf1767bb | (A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL) | REJECTED; generic test algebra |
| 4 | GEN-INDISC-R-ACTION-TW-FULL — 27307b7b331deafdcc1cecbd37b0466e1fcdd853be9c3ce0451a136eded0abd2 | (A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL) | REJECTED; generic full transport |
| 5 | GEN-INDISC-R-ACTION-TW-RED — 2154fdc83553b6a35496379f2cc38572de4c042fae3f73e5197856fd23dead17 | (A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL) | REJECTED; generic reduced transport |
| 6 | DEN-EF-ACTUAL-PACKET-CONT-TWIST-P — 9cd6ead9e63266e64aee8942c2482b028b9aba947f3479d6f6e08eac249a4a49 | (A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL) | EXPLORATORY; source packet and weak period only |
| 7 | DEN-EF-ACTUAL-PACKET-TWISTED-GLOB-QC-P — bd0f38f9613c4593f76c336f119818c11fb2875ba2987a938bc4e148e9a91eb1 | (A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL) | EXPLORATORY; fixed domain relation, time-only algebra |
| 8 | GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER — b65d21a61e615b771c0e0a83095df806b7e4317cb03568a52aa409713a33c6ea | (A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL) | REJECTED; generic support/corona relation |
| 9 | DEN-EF-ACTUAL-STD-QC-SUPPORT-TRANSFER-P — 6b2d998303351f922b3e53f9f6c512741cfd5576b761e47df1252e8c2cc78a8d | (A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL) | EXPLORATORY; fixed-prime relation, no selectivity |
| 10 | TWIST-DOMAIN-NONSELECTIVITY-CONTROL — 835b530233e9b416bcf34a2a55ff4ab472ecf2e7121f4c8453d1211648b3b94d | (A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL) | REJECTED; CONTROL_ONLY |

Owners 8 and 9 legitimately combine epsilon=max and epsilon=r because proof
evidence and final Route outcomes are identical. Every owner records
NONE_BY_DESIGN_NO_DETERMINANT_OBJECT. No A2, A3, or A4 coordinate is
positive; Route B has zero files and remains closed.

## 11. Mandatory prior subtraction

| Surface that must be subtracted | Exact owner | What Paper 13 may retain |
|---|---|---|
| continuous real-line multiplier triviality | Sorkin at official-title/abstract strength | independent sign-exact proof and owner-safe integration; no originality claim |
| twisted convolution, gauge, group C-star, amenability | standard sources including Austad, Leptin, Hulanicki, Packer--Raeburn | exact actual-author formulas, restrictions, and choice firewalls |
| c0 sums, multiplier products, constant diagonals, corona tail norms | standard operator-algebra facts | exact component isometries and typed instantiation; generic lemma must be labelled generic |
| sign/procyclic continuum lower bound | Paper 2 | elementary upper-bound equality closure and typed use only; zero novelty/Route credit |
| one-orbit standard-circle proxy, trace/return formulas, local/packet firewall, positive-time scalar ledger | Paper 8 | none; Paper 13 defines no trace or return amplitude |
| actual packet, actual indiscrete topology, stabilizer/period, U_p/H_p | Paper 9 and source chain | twist/support conclusions on the exact inherited owner |
| actual time-only collapse, untwisted author convolution, untwisted full/reduced transports | Paper 11 | twisted identities and exact gauge transport |
| all-degree factorization, same-carrier standardization, compact open components, J, invariant-diagonal comparator | Paper 12 | support and completed selected-diagonal placement |

The manuscript must perform these subtractions in its abstract and
introduction before stating the residual P13 contribution.

## 12. Correction and terminology-conservation matrix

| Do not write | Required replacement |
|---|---|
| Paper 13 discovers or first classifies continuous real-line multipliers. | Sorkin advertises the collapse; Paper 13 gives a sign-exact direct proof at its frozen convention. |
| Every invariant loses the action or period. | Exactly the four named outputs are constant after tags are forgotten; literal stabilizers and periods remain. |
| The twist erases H_x. | The restricted cohomology class is zero; H_x and all literal data are retained. |
| The actual twisted groupoid C-star algebra | the named Paper-13 author test/full/reduced record after time reduction |
| Full and reduced component algebras are equal. | The selected time image has equal max/r norms; whole component equality is not claimed. |
| Q or Q_p is discrete. | Q^bare has no topology; only Q_p^disc is discrete by standard construction. |
| The actual quotient is non-second-countable. | Q_p^actual remains indiscrete and second countable; standard/discrete owners have the topology failures. |
| J goes actual to standard continuously. | J:G_std->G_actual is continuous; functions pull back actual-to-standard. |
| The corona theorem is a packet obstruction or prime invariant. | It is the generic constant-diagonal lemma after component isometries, instantiated on the packet. |
| Non-second-countability forbids every groupoid C-star framework. | It is not a BHM obstruction; only exact named framework hypotheses may be discussed. |
| Controls prove continuum or corona faithfulness. | Direct proof establishes the theorem; finite controls are diagnostics and policy ledgers. |
| Route exploratory means weak determinant evidence. | Exploratory preserves a limited source relation; all A2--A4 coordinates fail. |
| The technical note is a standalone pass. | NOTE_OR_MERGE remains binding and STANDALONE_PASS is false. |

## 13. Manuscript-safe claim boundary

The permitted centre is a **technical-note synthesis and exact verification**:

> After crediting the continuous real-line collapse and standard twisted and
> operator-algebra ingredients, Paper 13 supplies the frozen sign and owner
> translations, proves the actual-author twisted identities and selected
> max/reduced component isometries, computes the exact actual-to-standard
> support and selected-diagonal placement, and records the resulting gauge
> covariance and sharp nonselectivity. The corona conclusion is explicitly
> the generic constant-diagonal c0/multiplier/corona lemma once the component
> maps are isometric.

The title must contain “Technical Note” or an equally unambiguous label. The
abstract, introduction, conclusion, metadata, cover letter, and publicity
must contain no firstness, new-classification, novel-obstruction, priority,
or standalone-breakthrough language.

Explicitly forbidden conclusions include:

- a globally named twisted groupoid C-star algebra on the actual owner;
- topology transfer between actual, bare, standard, and discrete records;
- prime selection or arithmetic recovery from a gauge class or corona class;
- a trace, determinant, zeta function, analytic continuation, A3 object,
  Hilbert--Polya operator, quantization, or Route-B entry;
- proof by finite controls; and
- any claim that the binding standalone Major has been closed.

## 14. Integrated traceability matrix

| Manuscript-safe claim | Proof | Independent review | Source/owner audit | Controls | Route | Required placement |
|---|---|---|---|---|---|---|
| normalized actual/time gauge bridge | core §§3--4 | core review §5.1 | Phase-2 framework §§3--5 | nerve/cocycle/gauge | owners 1--2 rejected | setup/conventions |
| sign-exact trivialization | core §5 | core review §5.2 | Sorkin ceiling; Phase-2 §3.2 | lift/gauge | owner 1 rejected | concise theorem with prior credit |
| actual-author twisted algebra | core §6 | core review §5.3 | Austad/Paper-11 split | convolution/involution | owners 3 and 7 | direct P13 verification |
| author full/reduced transports | core §7 | core review §5.4 | Austad Prop. 2.4 chain | completion gauge | owners 4--5 rejected | max/r kept separate |
| four named nonretention outputs | support §§3--5 | support review §§4--5 | literal-owner firewall | action/period/negative | owners 2, 6, 7 | limitations and fixed-prime negative |
| support iff zero or finite Q | support §§6--10 | support review §6 | Papers 11/12 premises | support transfer | owners 8--9 | actual/standard comparison |
| fixed-prime equality/topology | corona §2 | corona review §4 | Paper 2/9/12 subtraction | owner ledger only | owner 9 exploratory | supporting context, not contribution centre |
| component isometries | corona §§3--4 | corona review §5 | BHM/Williams/Austad | evidence ledger only | owners 8--9 | exact direct verification |
| diagonal/corona result | corona §§5--10 | corona review §§6--9 | generic lemma subtraction | v2 analytic ledger | owners 8--9 | state generic lemma first |
| no determinant or spectral promotion | proof ceilings | all reviews | Route schema | negative controls | all A2--A4 fail | dedicated limitations section |

## 15. Finding register and final integrated verdict

| Dimension | Result |
|---|---|
| mathematical correctness | PASS C0/M0/m0 |
| source and convention integrity | PASS at exact audited strengths |
| owner/domain integrity | PASS with actual/time/standard and bare/discrete splits |
| max/reduced integrity | PASS, separately typed |
| gauge and support integrity | PASS at frozen orientation and domains |
| deterministic controls | effective PASS C0/M0/m0 on replacement tuple |
| Route integrity | PASS schema/hash/DAG validation; 3 exploratory, 7 rejected |
| standalone centrality | FAIL at C0/M1/m0; Major retained |
| publication destination | TECHNICAL NOTE only |
| manuscript/release | not authorized |

Final machine-readable receipt:

    P13_INTEGRATED_PROOF_AUDIT=PASS
    MATHEMATICAL_FINDINGS=C0/M0/m0
    P13_1_THROUGH_P13_8C_PROVED=true
    REPLACEMENT_CONTROLS_PASS=true
    CONTROL_TOTALS=12_CSV_13_GENERATED_2665_ROWS_67_NEGATIVES_176_TESTS
    ROUTE_A_OWNER_COUNT=10
    ROUTE_A_EXPLORATORY_COUNT=3
    ROUTE_A_REJECTED_COUNT=7
    A2_A3_A4_POSITIVE_COUNT=0
    ROUTE_B_INVOCATION_ALLOWED=false
    STANDALONE_FINDINGS=C0/M1/m0
    STANDALONE_M1_CLOSED=false
    STANDALONE_M1_DOWNGRADED=false
    STANDALONE_PASS=false
    NOTE_OR_MERGE=true
    NOTE_BRANCH_SELECTED=true
    TECHNICAL_NOTE_LABEL_REQUIRED=true
    CORONA_THEOREM_GENERIC_AFTER_COMPONENT_ISOMETRIES=true
    NOVELTY_CEILING=SUPPORTED_WITHIN_SEARCH
    MANUSCRIPT_AUTHORIZED=false
    BIBLIOGRAPHY_AUTHORIZED=false
    FIGURE_CREATION_AUTHORIZED=false
    RELEASE_AUTHORIZED=false
    GIT_AUTHORIZED=false
    PUBLIC_SYNC_AUTHORIZED=false
    HASH_GRAPH_ACYCLIC=true

**Final integrated verdict:** the exact proof, source, controls, and Route
tuple supports composition only as an explicitly labelled technical note.
The mathematical package is stable, but its constant-diagonal corona centre
is generic after component isometries, so the standalone Major remains
binding. This file authorizes no manuscript or release action.
