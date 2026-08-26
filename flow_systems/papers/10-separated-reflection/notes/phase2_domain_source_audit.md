# Paper 10 Phase-2 independent domain/source audit

Audit date: **2026-08-14 (Asia/Shanghai)**  
Decision: **PASS TO PHASE 3 — NO MANDATORY DOMAIN AMENDMENT**  
Findings: **Critical 0 / Major 0 / Minor 0**  
Novelty status: **bounded negative search only; not a novelty proof**

## 1. Exact binding and boundary

This audit read, but did not edit, the final active Phase-1 locks recorded by
`phase1_final_gate.md` (SHA-256
`bdc5e3698110695a84f392c47bb907b7cf8ddc8807ea9af04654791090e4ab68`):

| Active artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `4fe51d7dc9514dea101178995dec73e120ab7032b11c06ecd4bc0efadf9cbc58` |
| `notes/candidate_lock.md` | `4cc6cae36630e13623d638a5eac7daaab084eef9549f4ca3bd44b026a32d26cf` |
| `notes/phase1_design_amendment.md` | `e0e3fb42c2285b8c5da521f05588581e7981de8957e33aa3cf237f653d1c432f` |
| `notes/pipeline_state.md` | `75cec92ff33ef52a456304361d6df5c26c055164adecbffb7f603b63e195e5ce` |

The earlier independently re-locked content tuple remains historical; the
final gate certifies that the differences are only status/ledger updates.
This report checks source definitions, exact domains, map directions, and
ownership boundaries. It gives no proof of `P10-1`--`P10-10`, no manuscript
claim, no Route credit, and no verdict inherited from Paper 9 beyond its
hash-locked arithmetic inputs.

The retained independent source set and locators are frozen in
`notes/sources/dom-source-manifest.md`; byte verification is in
`notes/sources/dom-sources.sha256`.

## 2. Domain/source gate

| Interface under stress | Authoritative finding | Lock consequence | Gate |
|---|---|---|---|
| `T0` and Hausdorff reflection | Cagliari--Mantovani, physical pp. 3--4, gives the `T0` quotient unit and UMP. Hofmann, physical pp. 10--11, gives `T0` iff Hausdorff for topological groups and the closure-of-identity Hausdorff group factor. | The direct UMP formulation in `P10-1` is correctly typed. General reflection terminology is corroboration, not a substitute for the registered direct determination. | PASS |
| Indiscrete group and quotient group law | Hofmann, physical pp. 5--6, separates two facts: every group with the indiscrete topology is a topological group; a normal group quotient with the quotient topology is a topological group. | Transporting a group law through `phi_p` is domain-valid, but it earns no source-canonical topology or group-law credit. Continuity must be checked on `ACT-Q-p`'s actual indiscrete topology. | PASS |
| Continuous characters | Hofmann's Corollary 1.19 factors continuous homomorphisms into Hausdorff groups through the Hausdorff group quotient. The circle target is Hausdorff. | `Hom_cont((ACT-Q-p,*_p),T)` is a valid exact domain after the transported operations are checked. No conclusion may be transferred to algebraic characters or to `U_p/H_p` with a natural quotient topology. | PASS |
| Fixed operator targets | Hoermann, physical p. 43 / printed p. 39, defines SOT and WOT on the same `B(H)` and explicitly calls both Hausdorff; it also records norm `>` SOT `>` WOT in fineness. | The lock's common carrier `B(ell^2(N))` with three separately named topologies is correct. A collapse result for continuous maps would not be a representation, measurable-field, or unbounded-operator result. | PASS |
| Borel and standard Borel domains | Andre, physical pp. 17--18, identifies the Borel algebra of a nontrivial indiscrete space as trivial. Encyclopedia of Mathematics places standard Borel spaces in the countably separated class. | `P10-3` correctly requires target separation and separately tests the source. A nontrivial source with trivial sigma-algebra must not be called standard Borel. | PASS |
| Positive finite measures and Dirac | Fremlin, physical pp. 5--6, defines a positive countably additive measure on its stated sigma-algebra and defines Dirac by set membership. Tao gives the same Dirac definition for any measurable space. | `delta_x` is defined even when `{x}` is not measurable, because its arguments are measurable sets. On the actual source, avoid the phrases "singleton mass" and "measurable singleton"; different labels may define the same measure. | PASS |
| Radon/Haar wording | Li's notes introduce Haar/Radon only after the locally compact Hausdorff group hypothesis. | The protocol's `Radon` prohibition is necessary and sufficient. Positive finite Borel measures here require no regularity language. | PASS |
| Tagged coproduct topology and Borel algebra | Andre, physical pp. 18--19, and Stacks Tag `0B1W` define the tagged coproduct topology componentwise; each component is clopen. | With indiscrete components, opens are exactly unions of whole components, hence the topology is already a sigma-algebra. This is the Borel owner for the copied control only, not for the global Deninger suspension. | PASS |
| Component measures | Fremlin's countable-additivity domain, combined with the countable prime label set, is the exact setting for component weights. | Finite positive measures are typed by nonnegative component masses with finite sum, including zero components. Countability and finite total mass are mandatory; the topology selects no distinguished weight. | PASS |
| Retopology map direction | Andre's finer/coarser definition and continuity convention make direction sensitive: the identity from a finer topology to a coarser one is continuous; the reverse requires the target opens to pull back to source opens. | For the frozen nonconstant bijection, `beta_{p,a}` has actual-indiscrete domain and standard-circle codomain, while its inverse points toward the indiscrete codomain. The two directions may never be swapped or called one untyped identity. | PASS |

## 3. Main conflict tested: `U_p/H_p` is not the topology owner

The only serious source-backed overclaim risk is a topology transfer across
`phi_p`.

General topological-group sources say that a quotient `G/N` with the quotient
topology is a topological group and is Hausdorff when `N` is closed. That
theorem concerns the topology inherited from a topological group quotient.
Paper 10 instead freezes only the set bijection

```text
phi_p: ACT-Q-p -> U_p/H_p
```

and transports the algebraic law back to the already fixed actual indiscrete
topology. Therefore a natural/profinite quotient topology one might place on
`U_p/H_p` is a different owner. It cannot refute Paper 9's `ACT-Q-p`
indiscreteness, make `phi_p` a homeomorphism, or supply nontrivial continuous
characters on `ACT-Q-p`. The active protocol already states this split, so no
amendment is required.

The same ownership rule applies to `beta_{p,a}`: a standard Hausdorff circle
on the same underlying orbit set is a finer retopology proxy, not a separated
reflection or continuous actual-source factor merely because a set bijection
exists.

## 4. Borel, Dirac, and copied-component wording gates

The sources support the current distinctions, with the following exact
language required downstream:

1. A Dirac measure is defined on the measurable domain by
   `delta_x(A)=1_{x in A}`. It does not assert that `{x}` is measurable.
2. On a nontrivial actual indiscrete object, point labels need not yield
   distinct Dirac measures. "Supported at the measurable singleton" is
   forbidden; topological support in a non-Hausdorff convention is not part of
   `P10-4`.
3. On the tagged copied coproduct, component unions are both open and Borel.
   The finite measure ledger is `ell^1_+(P)` only because the prime labels are
   countable and the measures are positive with finite total mass.
4. The same classification must remain a label-set control: replacing primes
   by any countable labels changes no abstract measure result.
5. `p -> log p` is an external function on the copied discrete label set. Its
   unboundedness excludes it from `C_b`; under the ordinary discrete
   `C_0` convention it also fails to vanish at infinity. Neither fact turns it
   into a selected mass, return time, trace, or actual-source observable.

No source conflict requires a protocol amendment.

## 5. Exact rational-Witt conjunction search

Search date: **2026-08-14**. The bounded contrast search used exact/near-exact
conjunctions including:

```text
"Deninger" "rational Witt" "Kolmogorov quotient"
"Deninger" "rational Witt" "continuous characters" Borel measure
site:arxiv.org Deninger "rational Witt" indiscrete topology reflection
"Gamma_p" Deninger Hausdorff reflection measure
```

The search returned Deninger's *Dynamical systems for arithmetic schemes*
(arXiv `1807.06400`) and unrelated false positives, but no primary source
combining the exact finite-kernel rational-Witt packet with the registered
`T0`/Hausdorff UMP, continuous scalar/operator maps, trivial-Borel Dirac and
finite-measure classification, direction-sensitive circle proxy, and copied
prime-component mass ledger.

The Deninger source is reused byte-for-byte through Paper 9's
`P9-DEN-DYN-v4` hash, not duplicated. Its exact set/action/stabilizer locators
remain the Paper-9 manifest locators. This bounded non-hit supports doing the
registered audit package; it does **not** establish global publication-level
novelty, priority, or nonredundancy. Paper 10 must frame its contribution as
the exact typed rational-Witt application/owner-boundary assembly, not as new
general topology or measure theory.

## 6. Required Phase-3 carry-forward conditions

Phase 3 may proceed without amending the locks if it preserves all of the
following:

- prove the actual `phi_p`-transported operations continuous before using
  topological-group character language;
- keep actual, natural quotient, proxy-circle, and copied-coproduct topologies
  as four non-interchangeable owners;
- state every operator-map result separately for norm, SOT, and WOT on the
  fixed `B(ell^2(N))` carrier;
- define every measure on its exact sigma-algebra and retain positivity,
  countable additivity, and finite total mass;
- use neither Radon/Haar nor singleton-support language on the actual
  non-Hausdorff objects;
- state both directions of `beta_{p,a}` with their exact domains/codomains;
- give the copied coproduct no source-global topology or arithmetic-weight
  credit; and
- keep the novelty statement bounded to the exact conjunction search.

Subject to those already locked conditions, the independent domain verdict is
**PASS TO PHASE 3, C0/M0/m0**.
