# HCS-C60 exact experiment plan

Status: **PREFREEZE_CODE_RESULTS_PASS / POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. Objective and decision rule

Build one project-local exact certificate for the biquadratic envelope of the
released C59 Gassmann pair. The target passes only if G0--G7 all pass in one
independently checked tuple. The official refresh and mandatory live replay
met that machine-layer decision rule. Any KILL condition would have terminated
the target; a partial normalizer, invariant, or one-branch local computation
was not accepted as a success state.

The external adaptive scan and Pilot A/B values remain design chronology, not
authority. The passing implementation reconstructed them from released inputs
and newly emitted durable carriers.

## 2. Frozen inputs

### Released predecessor tuple

G0 must bind at least:

```text
I59 implementation commit
  6c806120f17dab2e7b0bca37fcc156dfc459a4b7
P59 / repository main / origin main at selection
  961c45f4b0c66ec94d2f069fd9ecc9d4b529d03a
C59 live and archived Route SHA-256
  fab227cc8e83155e39793d665ea721e46522d5beee77a113a19379b64b2130c5
C59 FULL_PROJECT_HASHES.sha256 SHA-256
  4d756452d5b6d981e5fe4de3991cf6b7838f74fb8c411027a91dc2cf89a8d1a4
C59 full-manifest entries
  63, all verified at target selection
C59 group evidence SHA-256
  0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958
C59 resolvent evidence SHA-256
  667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6
```

G0 must also bind the exact C58 filtrations retained by C59, the current
Batch target, and the protected guard without modifying the guard.

### Locked constants and conventions

- $G=W(E_6)$, $|G|=51840$, on the released labelled $27$-line carrier.
- $H_+,H_-$ are the released C59 subgroups.
- One-based label-map arrays use left transport
  $H_3=xH_-x^{-1}$; GAP `Hminus^x` is the equivalent right-labelled syntax.
- Expected orders are $(|N|,|H_0|,|J|)=(324,162,81)$.
- Expected degrees are $(160,320,640)$ for $(M,F_0,L)$.
- The split witness is $p=692717$.
- Both $D_3=\mathrm{ToM}\ 140$ and $D_3=\mathrm{ToM}\ 206$ remain live.
- `NO_BAD_EULER_OR_ROOT_NUMBER` is literal.

## 3. G0 — released-authority rebind

The importer must:

1. resolve fixed canonical predecessor paths, not paths chosen by a
   certificate;
2. verify complete C59 scoped/full manifests and all self-exclusion policies;
3. verify live/archive Route byte identity and release status;
4. bind I59/P59, provenance policy, labelled $G$, $H_\pm$, line roots and
   supports, C58 local groups, Batch, and guard;
5. reject missing, extra, stale, or type-confused leaves; and
6. expose canonical hashes for independent rebound.

KILL on any byte or status drift.

## 4. G1 — common-normalizer lattice

The group producer reconstructs the exact arrays from `THEOREM_PACKAGE.md` and
computes:

- transport of $N_G(H_-)$ to $N_G(H_+)$ and $H_3=xH_-x^{-1}$;
- order, index, core, normalizer, derived subgroup, abelianization,
  SmallGroup ID, and frozen ToM locator for every target group;
- all three index-two subgroup classes in $N$;
- all pairwise intersections and generated groups;
- $J=[N,N]$, $N/J\cong V_4$, and $N_G(J)=N$; and
- all $350$ subgroup classes, $339$ character profiles, and eleven C59
  collision buckets.

The exact uniqueness predicate is

```text
normalizers conjugate in G AND normalizer indices over both subgroups = [2,2]
```

and must select only `[301,303]`. The broader existence of another generated
$V_4$ configuration is not excluded.

The frozen bounded group-component inventory is:

```text
code/c60_group.py
code/c60_checker_group.g
code/test_c60_group.py
code/run_group.sh
code/README.md
results/c60_group_evidence.json
results/c60_gap_projection.json
results/c60_group_schema.json
results/C60_GROUP_REPLAY.md
results/TEST_REPORT.md
```

Its historical preassembly component status was
`PROJECT_LOCAL_EVIDENCE_FROZEN_MACHINE_ASSEMBLY_PENDING`. The bounded tuple
has 10 files and 248,016 bytes, with aggregate
`dfd7d16a0128eae7a64906a4449a3022772dbc277abaae8187b6208340302464`.
Its producer, independent checker, evidence, GAP projection, and schema hashes
are respectively
`fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b`,
`4338ad0e2af9a0fe096cbb6514de6c8d5227386a2ffadeac487a858fb160dde3`,
`dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2`,
`77061a473c504925d24cfb2cedc26f7d4bc7057d4ee84615474cfa154323aba0`,
and `8f57605397dff0bccda2a817775cbb143b6250172f0e938021b1f9cf7e1b2cba`.
The official integrated producer/checker subsequently bound and cross-checked
every retained name. The component is now part of the machine tuple whose
G1 and cross-gate uses are `PREFREEZE_CODE_RESULTS_PASS`.

## 5. G2 — primitive integral carriers

The primitive lane must independently reconstruct:

1. $\mu$, an $81$-term quadratic carrier with stabilizer $N$;
2. $\xi_0$, the displayed $27$-term cubic with stabilizer $H_0$; and
3. $\lambda$, a $135$-term colored quadratic carrier with stabilizer $J$.

For each carrier it must emit the canonical formal support/weight vector,
prove integrality, compute the full formal orbit, evaluate all conjugates at
the complete split witness, prove distinctness, and hash the complete modular
minimal polynomial. Expected coefficient hashes are:

```text
M   b8818888c1ceb83e05d2f2df045e9d6e418f1ea18a5f019d1398e4cd0a59ef6b
F0  ffe9439cd390729bbb0dd7ffa4c6a1045c7fbc9c645e0f37e75c71d1e786e10d
L   c82feda40496156b7d006de4e47a1b808b3cf3ffffe4a386652d3e3fa77861f1
```

It must explicitly prove
$\operatorname{Stab}(x\operatorname{supp}\eta_-)=H_3\subset N$, not merely
the order $162$.

The design carrier hashes recorded elsewhere use canonical compact JSON with
zero-based monomial labels, while formal documents display one-based labels.
The implementation must declare and test this conversion; it may not compare
hashes across undeclared indexing conventions.

The frozen primitive-resolvent component entered assembly with the same
historical component status,
`PROJECT_LOCAL_EVIDENCE_FROZEN_MACHINE_ASSEMBLY_PENDING`. Its 12-file,
140,873-byte tuple has aggregate
`9ceda190badd260008fcb37788afd5f2a3e3457ca9e1e452f3999df24c12fe97`.
The producer, independent checker, evidence, payload, schema, checker-report,
mutation-report, and hostile-I/O-report hashes are respectively
`61b157e8c3e5a68bf304f9499bc176f60fe16bf7c5e5f6d021fbec17d7d9465e`,
`5f4070831d4734ba3be93ae578d7a2be893f46676ab40cdaa4a2de6b8d3fb672`,
`f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da`,
`eb17676ff10190c0b9f78e8f3fcb90121808fcd2c6a3b5d4dd06bfdc6177bb46`,
`fa120e247fa8ff69081059bccd2b94820b399662d2b781cb66c2f3f5f2275e8f`,
`1905cfa0ca45f37586a128a793d91d20c64b887e49e934a027640e5c5f4e44f1`,
`27c461373d5d354b8107f1f8daf4603e1d06ba72d2f1e27197000698383f2433`,
and `9edd5212059fd273069b6ca9e02e82e225a1ee83e906265593f8bdc69305671d`.
Its object status is `PASS / EVIDENCE_REPLAY_PASS /
release_authorized=false`. The official machine tuple completed its required
group cross-check and integrated it into passing G2/G3 evidence. This does not
authorize release.

## 6. G3 — formal invariant-degree obstruction

Enumerate complete point and unordered-pair orbit partitions for $H_0$ and
$N$. Serialize the actual orbit sets, not only sizes. The checker must prove
partition equality and then verify the exact cubic orbit and stabilizer.

The written bridge covers the monomial basis
$1,X_i,X_i^2,X_iX_j$ for $i<j$. Mutation cases must alter both orbit members
and coefficients so a size-only comparison cannot pass.

## 7. G4 — field, automorphism, character, and zeta bridge

Machine leaves must include:

- all subgroup inclusions and indices;
- core and normalizer quotients used for normal closures and automorphisms;
- all $25$ element-class values of the relevant permutation characters;
- equality for $H_+,H_3$ and inequality for $H_0$;
- the full rational Brauer character relation; and
- explicit false leaves for any $G$-set-isomorphism or bad-Euler inference.

The fixed-field and zeta conclusions belong to written mathematics, not a
self-reported Boolean.

## 8. G5 — absolute and relative arithmetic

For each of $N,H_+,H_0,H_3,J$, compute the complete orbit-count vector on the
C58 filtration groups and complex conjugation. Derive and independently check:

- degrees and signatures;
- signed discriminant exponent vectors;
- exact eight-prime absolute support;
- the four relative exponent differences; and
- $3^{8+16+8}=3^{32}$.

No expanded degree-$160/320/640$ characteristic-zero coefficient vector,
maximal order, or class number is required.

## 9. G6 — both relative local towers

For each retained $D_3$ branch:

1. enumerate $D\backslash G/N$ to obtain every prime of $M$ above $3$;
2. refine each base double coset for $H_+,H_0,H_3,J$;
3. compute every absolute and relative $(g,e,f,d)$ row;
4. group equal rows with exact multiplicities;
5. verify local degree, factor, and different totals;
6. reconcile global relative norms $3^8,3^{16},3^8,3^{32}$; and
7. prove every relative ramified row has $e=2,d=1$.

The output contains both tables and `d3_branch_selected: false`.

## 10. G7 — independence and release envelope

Require:

- disjoint producer/checker theorem call graphs;
- exact-key schemas with canonical serialization;
- scalar, structural, path, type-confusion, and evidence-rebound mutations;
- deterministic two-run or equivalent replay;
- pre/post source rebound around subprocesses;
- rollback-atomic promotion followed by mandatory nonmutating replay;
- self-excluding scoped and later full-project manifests;
- source/novelty and independent hostile audits; and
- explicit false leaves for every scope nonclaim.

## 11. Mutation minimums

At minimum, tests must reject:

1. inverse transport or a changed $x$ entry;
2. raw ToM substitution for a durable array;
3. swapped $H_0/H_3$ or changed subgroup generator;
4. a collision row omitted or duplicated;
5. a carrier term, weight, triple, stabilizer, orbit size, value, or polynomial
   coefficient change;
6. point/pair orbit sets with unchanged size multisets but changed members;
7. a changed character value or Brauer-relation term;
8. a signature/discriminant/support/relative-norm change;
9. any local row, multiplicity, or branch-selection change;
10. any scope false leaf changed to true; and
11. self-consistent evidence replacement plus top-level hash rebound.

## 12. Execution order

```text
G0
 -> G1 group lattice and uniqueness
 -> G2 primitive carriers
 -> G3 invariant obstruction
 -> G4 field/character/zeta bridges
 -> G5 global and relative discriminants
 -> G6 both local towers
 -> G7 independent envelope and atomic promotion
 -> machine hostile audit
 -> post-machine formal rebound/audit
 -> paper only after all earlier gates pass
```

Group and primitive lanes may run in parallel after G0, but their transport,
carrier, and subgroup hashes must be reconciled before G3--G6.

## 13. Current state

The official source-stable tuple passed all C60-EXACT-0--7 gates, the complete
hostile checker, rollback-atomic six-target prefreeze promotion, and the
mandatory nonmutating live replay. The two 53-test cycles reproduced the same
payload and certificate. Exact machine counts are code/results/live/scoped
`13/8/21/20`, payload leaves `9310`, value/type/structural mutations
`9339/9339/14`, deep group/resolver/evidence/artifact cases `6/4/10/2` with
actual total `12`, and snapshot checks `39`.

The official tuple binds:

```text
payload              dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead
certificate          d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518
schema               c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5
independent check    25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44
scoped manifest      f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7
group evidence       dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2
resolver evidence    f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da
source contract      4c484b3532c4604b028f45fc157c261149a7a49ca9631bbcf83f8d1efd1cdb90
G0                   0512db556004edde7c19176bbb35375beaeba89301da53902d5c5d98001cb8a8
official refresh log 5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239
```

The historical machine-bound formal input aggregate remains
`fd76237963d385b79b10b7ea13477173b2cf17261fc47d5b43697379d9b012ca`.
The changed 13-root package and Route semantics have now passed the independent
formal-doc hostile audit, and the live Route binds the post-machine aggregate
externally to avoid a self-hash cycle. Status is exactly
`PREFREEZE_CODE_RESULTS_PASS / POSTREFRESH_PASS /
FORMAL_DOCS_PASS / PAPER_PENDING / NOT_RELEASED`.
`promotion_authorized` remains false. Implementation/provenance commits, the
full-project manifest, Route archive, paper sources, and paper PDF remain null
or pending.
