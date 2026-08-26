# Paper 12 candidate lock

Lock date: **2026-08-15 (Asia/Shanghai)**  
Status: **V4 DESIGN/SOURCE RE-LOCK PASS — TARGETED PROOF AND CONTROLS AUTHORIZED**

## 1. Candidate family

```text
Family: DEN-EF-ACTUAL-MARKED-TIME-COHOMOLOGY
Actual owner: Paper-11/Paper-12 transformation groupoids built from the
              Deninger right flow on Paper-9 actual inherited topologies
Marked datum: source logarithmic-time 1-cocycle c(x,t)=t
Primary object: author-defined globally continuous unnormalized nerve cochain
                complex with the constant coefficient bundle
Primary boundary: strict invariance plus scaled covariance; explicit unequal-
                  period counterisomorphisms prove weaker-category non-descent;
                  canonical orbitwise standardization retains strict arrows,
                  and the actual-to-standard H^1 map is the invariant diagonal
```

Every fixed-orbit arithmetic statement quantifies over every rational prime
`p` and every normalized Paper-9 orbit label `a`.  A fixed-prime packet
corollary uses the separately frozen `G_p^pkt=Gamma_p rtimes R` owner and is
conditional on Phase 2 re-verifying the exact additive action, normalized
clock, and common stabilizer on every packet unit. The full Deninger
suspension and every cross-prime/global owner are excluded.

## 2. Inherited exact evidence

The design depends on, but does not mutate:

- Paper 9 proof audit, SHA-256
  `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8`;
- Paper 9 source audit, SHA-256
  `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20`;
- Paper 10 proof audit, SHA-256
  `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a`;
- Paper 11 integrated proof audit, SHA-256
  `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28`;
- Paper 11 composition blueprint, SHA-256
  `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b`.

Paper 9 owns actual orbit and packet indiscreteness. Deninger physical
pp. 38--39, Section 6/Theorem 6.1 own the source flow, packet membership,
common multiplicative stabilizer `p^Z`, and logarithmic clock conversion.
Paper 10 owns separated unit-observable collapse. Paper 11 owns the
range-first transformation-groupoid definition, arrow-time factorization,
and global-QC convolution collapse. Paper 12 owns only the new nerve complex,
cohomology classification, marked categories, isotropy image, normalized
pointed quotient shadow, orbitwise standardization equivalence, and the
standardized-versus-actual degree-one comparison.
“Deninger's groupoid/cohomology” is forbidden
unless a future exact source locator genuinely defines it.

## 3. Frozen owners

```text
GEN-INDISC-R-ACTION-CONT-COCHAIN
  = the full globally continuous nerve cochain complex of an arbitrary
    nonempty indiscrete right R-space, with the constant T0 coefficient
    bundle and the author-defined unnormalized differential;

DEN-EF-ACTUAL-ORBIT-GRPD-p-a
  = G_(p,a)^orb=X_(p,a) rtimes R, the Paper-11/Paper-12 range-first
    transformation groupoid on the exact Paper-9 inherited orbit topology;

DEN-EF-ACTUAL-ORBIT-TIME-CLASS-p-a
  = G_(p,a)^orb together with the Deninger-normalized class [c], c(x,t)=t;

DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-p-a
  = isotropy restriction of the strictly marked pair (G,c), not an invariant
    of G alone or of an unnormalized one-dimensional cohomology space;

DEN-EF-ACTUAL-PACKET-GRPD-p
  = G_p^pkt=Gamma_p rtimes R with the Paper-9 actual packet topology and the
    same restricted Deninger additive flow;

DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-p
  = packet-level uniform-period corollary, source-gated at every packet unit;

DEN-EF-STANDARD-PERIOD-QUOTIENT-p
  = the one-orbit standard R/Per(c) isomorphism-class proxy and pointed
    shadow; it does not serialize the same-set packet standardization and is
    never identified with the actual inherited topology;

DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-p
  = the constructed orbitwise coproduct packet groupoid, the continuous
    comparison J_p:G_p^std->G_p^actual, and the degree-one diagonal/invariant
    theorem; Q_p is used only as a bare orbit set;

UNMARKED-PERIOD-SCALING-CONTROL
  = explicit isomorphisms between different-period unmarked groupoids;

ARBITRARY-PERIOD-MARKED-CONTROL
  = frozen trivial, free, nontransitive, dense-period, prime/composite/
    nonarithmetic/neutral-clock and label controls showing the construction
    is not arithmetically selective;

DEN-FULL-SUSPENSION-GLOBAL
  = EXCLUDED_OWNER: no full-suspension or cross-prime theorem.
```

No coordinate from these owners may be spliced into Paper-8 traces, Paper-11
completions, or an all-prime scalar Euler ledger.

## 4. Frozen conventions

- Right action: `x dot t`.
- Arrow groupoid: `G=X rtimes R` with product topology and range-first
  operations from Paper 11.
- Nerve: `G^(0)=X`; for `n>=1`, `G^(n)` is the subspace of composable
  `n`-tuples in `G^n`.
- Coefficients: the constant bundle `underline(A)_X=X x A -> X` for a named
  `T0` topological abelian group, with every arrow acting by the identity.
- Cochains: the author-defined **unnormalized** continuous nerve complex;
  after the frozen trivialization, all globally continuous maps
  `G^(n)->A`, including degenerate simplices; no support, boundedness,
  integrability, smoothness, Borel-only, or compactness gate.
- Naming: use `C_cnv`, `Z_cnv`, `B_cnv`, and `H_cnv` until an exact source
  proves equivalence with a named standard theory at matching hypotheses.
- Cohomology: `Z=ker d`, `B=im d`, and `H=Z/B` as algebraic abelian groups;
  for real coefficients, algebraic real vector spaces. No cochain-space or
  quotient topology is claimed.
- Degree-zero differential: `(d h)(gamma)=h(s gamma)-h(r gamma)`.
- For `n>=1`, use the frozen inhomogeneous alternating face differential in
  `research_protocol.md`; Phase 3 must check `d^2=0` with the range-first
  convention.
- Real time class: `c(x,t)=t` with Deninger's fixed logarithmic-time scale and
  orientation.
- Isotropy restriction: `res_x(b)=b|_(G_x^x)`; after proving coboundaries
  vanish, `Per_x([b])=image(res_x(b))`.
- Strict marked morphism: `F` with `c' o F=c`.
- Positive scaled morphism: `F` with `c' o F=alpha c`, `alpha>0`.
- Unmarked morphism: no cocycle condition.
- `Per_x([b])` is defined only after `res_x` is proved to kill coboundaries;
  every covariance formula compares `x` with `F_0(x)`.
- Strict category: normalized transitive coordinate-clock objects and
  topological groupoid isomorphisms with `c' o F=c`.
- Scaled category: pairs `(F,alpha)`, `alpha>0`, with
  `c' o F=alpha c`, multiplicative scale composition, and reciprocal inverse.
- Unmarked category: the same topological groupoid isomorphisms after
  forgetting the cocycle.
- `R/Per_x(c)=R/Stab_R(x)` carries its usual quotient topology only for the
  normalized coordinate clock. For arbitrary `[b]`, `R/Per_x([b])` is a
  separate value-space quotient, not an orbit parametrization.
- The strict functor maps `(G,c)` to the pointed standard homogeneous space
  `(R/Stab_R(x),[0])` and strict `F` to `[t]|->[t]`; it must satisfy identity,
  composition, basepoint rotation, and the naturality square. Scaled dilation
  is separate and semilinear.
- Common-stabilizer category:
  `C_common=disjoint-union_(L>0) C_common(LZ)` of nonempty globally
  indiscrete right-`R` spaces,
  not necessarily transitive, with `c(x,t)=t` and one common lattice
  `Stab_R(x)=H=LZ`, `L>0`, at every unit; strict marked isomorphisms only.
- The central v4 functor gives every orbit its quotient `R/H` topology and
  takes their nonempty topological coproduct (`Q=X/R` is nonempty) on the
  same underlying set. It is
  section-free, full and faithful, and inverse to global indiscretization.
  Its target orbit index is discrete by construction and is not the actual
  quotient topology.
- Under the ambient ZFC convention, canonically as abstract groups only,
  `1->(R/H)^Q->Aut_R(G_std)->Sym(Q)->1`. A semidirect/wreath splitting is
  noncanonical and requires one chosen origin per orbit; surjectivity and the
  standardized zero-slope potential proof record their choice use.
- `J:G_std->G_actual` is the continuous identity functor. For trivial real
  coefficients, `H_cnv^1(G_std;R)=R^Q` algebraically and `J^*` embeds the
  actual line as the constant diagonal, equal to strict-automorphism
  invariants. Standardized coboundaries are generally nonzero; no claim
  `Z_std^1=R^Q c`, no cohomology topology, and no higher-degree standard
  computation is frozen.

The time cocycle is unbounded and has all-arrow support. It is not an element
of Paper 11's `C_qc^glob` and is not a convolution multiplier until a separate
domain theorem is proved. Strict marking is sufficient, not necessary, for
subgroup equality; the weaker-category statement is existential non-descent,
not universal loss.

### 4.1 Frozen deterministic controls

```text
TRIV-2:          X={0,1}, indiscrete, trivial action, H=R;
FREE-R:          X=R as an indiscrete set, translation, H={0};
PER-L:           L in {log 2, log 4, sqrt(2), 37/29};
DENSE-Q:         X=R/Q indiscrete, translation, H=Q;
NONTRANS-1-2:    (R/Z) disjoint-union (R/2Z) with one indiscrete topology;
NON-T0-A2:       X={x_0,x_1}, trivial action, A=Z/2Z indiscrete,
                  h(x_0)=0 and h(x_1)=1 in degree zero;
SCALE-LM:        every ordered unequal pair from PER-L;
REVERSE-L:       ([r],t)|->([-r],-t);
LABEL-SWAP:      prime/composite/nonarithmetic/neutral labels permuted.
STD-COPROD-H1:   n in {3,5,7}, m in {1,2,3}; exact common-cycle topology,
                  automorphisms, H1 dimensions, diagonal and invariants.
```

Implementation paths are exactly `code/generate_controls.py`,
`code/test_controls.py`, `experiments/reproduce.sh`, `results/*.csv`, and
`results/manifest.json`; Python standard library only, optional reserved seed
`120012`, at least 96 tests, zero tolerance for exact checks and `1e-12` only
for frozen real approximations. The manifest and two-fresh-generation
byte-identity contract in the protocol are mandatory.

The new CSV is exactly
`results/orbitwise_standardization_h1_controls.csv`, with `3252` body rows
under the exact schema/order in `phase3_standalone_amendment_v4.md`. The
complete package has `11` CSV files and `3486` body rows.

## 5. Decision vocabulary

Primary scoped verdicts are:

```text
CONFIRM_COMPLEX_COLLAPSE
CONFIRM_MARKED_PERIOD_RECOVERY
CONFIRM_STRICT_VS_SCALED_SPLIT
ORBIT_ONLY
PACKET_COROLLARY
STANDALONE_PASS
NOTE_OR_MERGE
REFUTE
NOT_TESTABLE
```

`CONFIRM_MARKED_PERIOD_RECOVERY` means only that the **source-normalized marked
pair** recovers the source stabilizer through isotropy restriction.  It does
not mean that the unmarked groupoid, the abstract cohomology line, or a
generic period construction selects `log p`.

`STANDALONE_PASS` requires the all-degree natural chain theorem, fully typed
marked covariance/non-descent theorem, normalized pointed quotient shadow,
full-and-faithful orbitwise standardization equivalence, the canonical
automorphism exact sequence, the standardized `H^1=R^Q` theorem, and the
actual diagonal/invariant characterization, together with the
source-verified `PACKET_COROLLARY`, updated controls, and a nearest-precedent
audit at that exact strength.
`ORBIT_ONLY` forces `NOTE_OR_MERGE`. If the package reduces
to Paper-11 factorization plus a routine formal nerve corollary, standard
coproduct/wreath facts, and Deninger's stabilizer, `NOTE_OR_MERGE` is mandatory
even if every formula is correct. Topology plus a wreath formula without the
cohomological diagonal is insufficient.

## 6. Route ceiling

No Route coordinate is pre-certified.

```text
generic cochain-complex owner:
  A0_FAIL, A1_FAIL ceiling, action-blind control;

actual source-marked period owner:
  may retain source A0 only after same-object source audit;
  A1 ceiling A1_WEAK because a period/repetition subgroup is not yet a
  primitive-orbit amplitude or global prime enumeration;

standard period quotient:
  one-orbit isomorphism-class proxy and pointed shadow only,
  no actual-topology or separated-reflection credit;

standardized packet H1 comparison:
  derived orbitwise coproduct and actual-to-standard comparison owner,
  no Q_p topology/count, actual-topology transport, or arithmetic selectivity;

all owners:
  A2/A3/A4_FAIL or NOT_TESTABLE absent new same-owner results;
  Route B false and no Route-B YAML.
```

The eight exact Route owners and their formerly omitted mandatory keys are:

| `candidate_id` | `family` | `phase_space` | `dynamics` | `parameters` | `parameter_provenance` | exact YAML path |
|---|---|---|---|---|---|---|
| `GEN-INDISC-R-ACTION-CNV` | `GENERIC-INDISCRETE-ACTION-CONTROL` | `G(X,alpha)^(bullet)` | arbitrary right `R` action | `X,alpha,A,n` | author universal variables | `evaluations/route_a/GEN-INDISC-R-ACTION-CNV/2026-08-15-stage12.yaml` |
| `DEN-EF-ACTUAL-ORBIT-CNV-P-A` | `DEN-EF-ACTUAL-ORBIT-TIME-COHOMOLOGY` | nerve of `G_(p,a)^orb` | Deninger right `+t` flow | `p,a,n` | Deninger + P9 + P11 + P12 split | `evaluations/route_a/DEN-EF-ACTUAL-ORBIT-CNV-P-A/2026-08-15-stage12.yaml` |
| `DEN-EF-ACTUAL-PACKET-CNV-P` | `DEN-EF-ACTUAL-PACKET-TIME-COHOMOLOGY` | nerve of `G_p^pkt` | fixed-prime right `+t` flow | `p,n` | every-unit packet source gate | `evaluations/route_a/DEN-EF-ACTUAL-PACKET-CNV-P/2026-08-15-stage12.yaml` |
| `DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A` | `DEN-EF-ACTUAL-MARKED-PERIOD` | `(G_(p,a)^orb,c)` | Deninger right `+t` flow | `p,a` | source clock/stabilizer, no fitted scale | `evaluations/route_a/DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A/2026-08-15-stage12.yaml` |
| `DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P` | `DEN-EF-ACTUAL-PACKET-MARKED-PERIOD` | `(G_p^pkt,c)` | fixed-prime right `+t` flow | `p` | common packet stabilizer gate | `evaluations/route_a/DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P/2026-08-15-stage12.yaml` |
| `DEN-EF-STANDARD-PERIOD-QUOTIENT-P` | `STANDARD-MARKED-PERIOD-PROXY` | usual `R/(log p)Z` | standard right translation | `p` | copied marked-period relation only | `evaluations/route_a/DEN-EF-STANDARD-PERIOD-QUOTIENT-P/2026-08-15-stage12.yaml` |
| `DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P` | `DEN-EF-STANDARDIZED-PACKET-H1-COMPARISON` | comparison `J_p:G_p^std->G_p^actual` | componentwise standard versus actual right `+t` action | `p,Q_p(set),H=(log p)Z` | common source stabilizer + actual packet/orbit set + constructed coproduct; no Q topology/count | `evaluations/route_a/DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P/2026-08-15-stage12.yaml` |
| `UNMARKED-PERIOD-SCALING-CONTROL` | `GENERIC-ARBITRARY-PERIOD-CONTROL` | frozen `G_L` family | standard translation/dilation controls | `L,M,alpha` | preregistered nonarithmetic controls | `evaluations/route_a/UNMARKED-PERIOD-SCALING-CONTROL/2026-08-15-stage12.yaml` |

For each row, `candidate_definition`, `arithmetic_origin`, `clock`, and
`normalization` are the exact corresponding records in protocol Section 10.
Every row additionally freezes:

```text
determinant_convention: NONE_BY_DESIGN_NO_DETERMINANT_OBJECT;
orbit_cutoff: NOT_APPLICABLE_EXACT_THEOREM;
precision: SYMBOLIC_EXACT_AND_FROZEN_1E-12_CONTROLS;
training_data: NONE;
forbidden_data: zeta zeros, fitting, traces, Paper-8 coefficients,
                Paper-11 completions;
code_commit: unavailable-no-git-content-sha256-lock-required;
artifact_paths: exact proof/manifest/peer/route paths in protocol Section 10
                plus the row-specific YAML path above.
```

`P12-10` is blocked until all exact paths exist and their final SHA-256 values
are serialized. The no-Git value is final provenance, not a pending
placeholder; implementation/content hashes substitute mechanically.

The evaluator owns the final A1 result. A period subgroup by itself does not
satisfy primitive/repeated-orbit enumeration, orientation, multiplicity,
stability, completeness, arithmetic derivation, or adversarial-control gates.
`NONE_BY_DESIGN_NO_DETERMINANT_OBJECT` is a present negative convention and
cannot be upgraded without a new owner/protocol.

## 7. Frozen exclusions

- claiming that `G` or the abstract line `H^1` intrinsically normalizes `c`;
- saying exact subgroup equality characterizes strictness, or that every
  scaled/unmarked isomorphism changes the subgroup;
- calling `log p Z` invariant under the scaled or unmarked category;
- identifying the standard period quotient with the actual orbit topology;
- using `R/Per([b])` as an orbit parametrization for arbitrary scaled `[b]`;
- putting `c` in `C_qc^glob` or Paper-11 completions;
- packet/global promotion without the exact source/topology/stabilizer gate;
- calling the constructed coproduct topology inherited, a separated
  reflection, or the actual topology of `Q_p`;
- using `R^Q` for a direct sum or for continuous functions on actual
  indiscrete `Q_p`, or putting any topology on cohomology;
- saying standardized `B^1` vanishes or every standardized cocycle is
  literally orbitwise time-only;
- reversing `J:G_std->G_actual`, using scaled/unmarked automorphisms in the
  invariant theorem, or calling the wreath splitting canonical;
- all-prime products, traces, determinants, analytic continuation, zero data,
  Weil compression, quantization, or Hilbert--Polya language;
- target-zero data, fitting, random search, or post-hoc period normalization.

## 8. Release and source-byte boundary

- The generated manuscript PDF is releasable only after manuscript, citation,
  declaration, peer, and release gates pass.
- No `notes/sources/*.pdf` is a public supplement or embedded attachment.
- Bibliography entries use canonical DOI/journal/publisher/arXiv/author
  endpoints, never local paths or audit hashes.
- Internal hashes remain reproducibility locators, not scholarly identities.
- If Papers 9 or 11 lack an immutable public manifestation, Paper 12 must use
  an honest companion-preprint record or restate the dependency
  self-containedly.
- A public-sync dry run must enumerate the payload and show zero retained
  source PDFs staged or tracked.

## 9. Lock integrity

`phase1_final_gate.md` binds the historical v2 design tuple and its three
independent `C0/M0/m0` reports; it does not bind these v4 bytes.  The current
v4 content tuple is bound by `phase3_v4_final_gate.md`, SHA-256
`974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0`,
after methodology, devil/domain, and source/novelty re-locks all returned
`C0/M0/m0`.  That gate authorizes only the targeted v4 proof and deterministic
controls.  It does not prove a v4 target, grant `STANDALONE_PASS`, certify
priority, or authorize Route YAML, manuscript, release, or public sync work.
