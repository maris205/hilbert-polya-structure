# Papers 14--18 batch amendment v2 — Paper-14 merge/replacement and trace-branch split

Status: **ACTIVE DESIGN REDIRECT / EXACT-BYTE REVIEW REQUIRED**  
Version: `P14-18-BATCH-AMENDMENT-v2.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Active manuscript slots: **five, provisionally retained**  
Technical Note allocation: **Paper 17 remains the sole candidate**  
Proof, controls, Route A/B, manuscript, release, Git, and public
synchronization authorized by this amendment: **false**

## 1. Exact authority

This amendment binds the following stable records:

```text
historical Papers 14--18 batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
Papers 14--18 batch amendment v1
  sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802
old Paper-14 global-topology proof
  sha256:3d03722c866a6ec9998673ff404cd05208106d4953e8d4461429c6fd303371fe
old Paper-14 independent mathematical review
  sha256:0750a44ddcaba3d0176ec93f0865ff0982438046db0504296b61ed9df587e02f
old Paper-14 standalone/nonredundancy review
  sha256:d05432f4e8dec4d53c69c79cf363425e88d098309f381de09ae8d0d2d13042f4
Paper-18 base research protocol
  sha256:d3fa7c262727ebb7501d09692315b1dc53dc5c3409f4fd37000cef9f22bd572e
Paper-18 base candidate lock
  sha256:98fb74d3dd27e854af22ee31a94753b8d26d1f22e3260cec5ca977f854d6ed17
```

The old Paper-14 proof and its mathematical review remain valid theorem
receipts.  The standalone report is the binding publication-level verdict:
`MERGE/REPLACE -- C1/M0/m0`.  Mathematical correctness is not silently
promoted to standalone weight.

## 2. Binding disposition of the old Paper 14

The project *Global Periodic-Locus Topology of the Rational-Witt
Suspension* is no longer an active manuscript slot.

Its proved content is retained as a shared foundation:

1. the descended source-base map and full fixed-prime fibres;
2. the zero-versus-unit source-open packet isolator;
3. the actual all-prime coproduct comparison;
4. the finite, all-prime, and cofinite ambient-closure formulas; and
5. the exact incidence reduction and source stop for arbitrary
   infinite-coinfinite prime subsets.

The following parts receive no new standalone credit downstream:

```text
Paper-9 fixed-packet indiscreteness;
Paper-10 generic coproduct and T0 consequences;
Deninger's collective unitary closure;
the unresolved arbitrary-S arithmetic incidence classification.
```

The historical directory
`papers/14-global-periodic-topology/` remains an immutable audit and
foundation record.  It is not a sixth active project and is not renamed into
a second Technical Note.

## 3. Replacement Paper-14 identity

The provisional replacement manuscript slot is:

```text
working directory:
  papers/14-packet-coordinate-descent/
working title:
  Coordinate-Change Groupoids and Haar Descent for Rational-Witt Packets
owner:
  exact source-permitted fixed-prime coordinate presentations,
  their transition arrows, and the separately named abstract compact base
  B_p=U_p/H_p
```

The candidate question is deliberately narrower than the old Paper-18
protocol and stronger than existence of abstract Haar:

> Enumerate the actual auxiliary choices in the source packet formulas,
> compute every induced transition on the compact transverse coordinate and
> time coordinate, and prove either a choice-independent normalized-Haar
> descent theorem or a complete transition-moduli obstruction.

The replacement earns no theorem merely from the set bijection

```text
Gamma_p <-> (U_p/H_p) x (R_{>0}/p^Z)
```

and no theorem merely from uniqueness of normalized Haar on the abstract
compact group `B_p`.  It must first prove the transition maps and their
composition, inverse, and covariance laws.

## 4. Replacement fail-fast and standalone gate

The first bounded source/domain precheck must answer:

1. Which choices are made around the source formulas leading to equations
   (35)--(39) and the finite-kernel packet presentation?
2. Which changes of those choices are actually licensed by the source?
3. Does each change induce a group automorphism, affine map, translation,
   time shift, or a more general set map on the displayed coordinates?
4. Which equalities are pointwise, set-theoretic, Borel, measure-class, or
   normalized-measure statements?
5. Can all transition arrows be composed and inverted without importing a
   topology or sigma-algebra from a different owner?
6. Is there a concrete permitted transition that changes transported Haar,
   or a direct proof that every permitted transition preserves it?

Fail closed:

- If the source does not expose enough transition data to state a complete
  class, record `SOURCE_UNDERDETERMINED` and replace/stop the slot.
- If every result reduces to abstract Haar uniqueness after an immediate
  group-automorphism observation, record `MERGE/REPLACE`.
- Standalone eligibility requires either a nontrivial complete transition
  classification plus choice-independent descent, or a complete sharp
  canonicality obstruction on the exact source presentations.
- A negative bounded search may say only
  `NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`.

No measured enhancement, disintegration, representation, trace, or operator
is authorized at this gate.

## 5. Paper-18 split and narrowed center

The current Paper-18 base protocol is retained as a historical broad design.
A future versioned amendment must remove its claims `P18-1`--`P18-3` from
Paper-18 contribution credit and treat the final reviewed replacement-P14
transition/descent result as an upstream premise.

The narrowed Paper-18 center is:

```text
positive replacement-P14 descent
  -> named measured enhancement of the actual packet owner
  -> disintegration along literal time orbits
  -> one represented algebra and one map into its von Neumann owner
  -> same-map return trace/weight theorem or a fixed-class no-go.
```

Paper 18 may not duplicate the transition classification or abstract Haar
theorem.  It must keep on one owner the sigma-algebra, measure class,
normalization, groupoid/source-fibre system, test algebra, representation,
trace or weight domain, primitive/repeated coefficients, clock, phase, and
non-orbit terms.

If replacement Paper 14 ends in the negative obstruction branch, the
positive measured/trace branch of Paper 18 is blocked.  The batch must then
replace or stop Paper 18; it may not manufacture a trace from an arbitrary
chart or declare the obstruction itself a second paper.

## 6. Provisional five-paper register

| Slot | Active center after this amendment | Current ceiling |
|---|---|---|
| 14 | source-coordinate transition groupoid and Haar descent/obstruction | Phase-1 source precheck only; standalone `HOLD` |
| 15 | Wieferich--Ulm classification of the bare compact packet bases | Phase-1 repair/review; standalone `HOLD` |
| 16 | mixed standardized owner plus Arveson component/clock reconstruction | Phase-1 review; standalone `HOLD` |
| 17 | joint open-groupoid topos/quantale interface theorem | sole `TECHNICAL_NOTE_CANDIDATE`; proof review required |
| 18 | measured enhancement, disintegration, and same-map return trace | blocked on positive slot-14 descent; standalone `HOLD` |

The old Paper-14 topology record and old Paper-15 mixed-clock record are
merged foundations, not manuscript slots.  Filesystem history may therefore
contain more than five directories while the active manuscript register has
exactly five entries.

## 7. Dependency DAG and owner firewall

```text
old P14 proved topology (merged foundation)
                   \
                    -> replacement P14 transitions/Haar
                                      -> narrowed P18 disintegration/trace

old P15 mixed-clock foundation -> P16 Arveson reconstruction

replacement P15 Wieferich--Ulm classification     (independent)

P17 open-groupoid interfaces                      (independent Note branch)
```

Owner rules:

1. Actual packet topology, topology-generated Borel algebra, abstract compact
   `B_p`, a chosen chart, a measured enhancement, and a standardized proxy
   remain distinct records.
2. A set bijection does not transport topology, Borel structure, Haar,
   disintegration, completion, representation, or trace.
3. Paper 9's actual packet is indiscrete and Paper 10's actual Borel algebra
   is trivial; neither fact identifies it with the compact Borel owner.
4. Papers 2 and 7 may supply historical choice ledgers and proxy warnings,
   but their arbitrary mass models do not prove canonical descent.
5. Papers 8, 11, 12, and 13 may supply only their exact standard/proxy/time
   comparison ceilings; no standard-circle trace or generic diagonal is
   donated to Paper 18.
6. Target Euler coefficients, zero data, or desired prime weights cannot
   select a chart, measure, normalization, operator, or regularization.

## 8. Authorized next actions

This amendment authorizes only:

1. creation of the replacement-P14 directory and a bounded Phase-1
   source/domain/precedent precheck;
2. after a `C0/M0/m0` precheck, creation of a versioned replacement-P14
   research protocol and candidate lock;
3. read-only independent methodology, devil/domain, source, and
   nonredundancy reviews of those exact bytes; and
4. creation and review of a Paper-18 versioned design amendment only after
   the replacement-P14 owner split has been frozen.

It does not authorize a replacement-P14 or Paper-18 symbolic proof.  It does
not change the separate exact gates already controlling Papers 15--17.

```text
BATCH_AMENDMENT_V2_ACTIVE=true
OLD_P14_STANDALONE=NO_GO
OLD_P14_CONTENT=MERGED_FOUNDATION
REPLACEMENT_P14_CENTER=SOURCE_COORDINATE_TRANSITIONS_AND_HAAR_DESCENT
REPLACEMENT_P14_SOURCE_PRECHECK_AUTHORIZED=true
REPLACEMENT_P14_PROTOCOL_CONDITIONAL_ON_PREFLIGHT_PASS=true
P18_CENTER=NAMED_MEASURED_ENHANCEMENT_DISINTEGRATION_AND_SAME_MAP_TRACE
P18_POSITIVE_BRANCH_REQUIRES_REPLACEMENT_P14_POSITIVE_DESCENT=true
ACTIVE_MANUSCRIPT_SLOTS=5
SOLE_TECHNICAL_NOTE_CANDIDATE=P17
SYMBOLIC_PROOF_AUTHORIZED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

