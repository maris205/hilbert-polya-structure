# Paper 13 Phase-2 independent integrated final review

Status: **PASS TO BOUNDED PHASE 3 AND A SEPARATE CONTROL-DESIGN LOCK**  
Verdict: **C0 / M0 / m0**  
Review date and evidence cutoff: **2026-08-15 (Asia/Shanghai)**  
`route_b_invocation_allowed: false`  
Standalone status at this gate: **not granted**

This is the independent integrated Phase-2 gate required by
`notes/phase1_final_gate.md`. It adjudicates the exact frozen Phase-1 tuple,
the bounded precedent search, the convention/owner audit, and the final
framework/source package. It is not a proof receipt, deterministic-control
implementation authorization, Route decision, composition or manuscript
approval, standalone decision, release approval, Git authorization, or public
synchronization approval.

## 1. Exact authority and reviewed bytes

I independently rehashed every authorizing or load-bearing artifact below at
adjudication time. Every value matched.

| Artifact | SHA-256 | Integrated receipt |
|---|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | active Phase-1 tuple: MATCH |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | active Phase-1 tuple: MATCH |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` | active Phase-1 tuple: MATCH |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | active Phase-1 tuple: MATCH |
| `notes/phase1_final_gate.md` | `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` | authorizing gate: MATCH |
| `notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` | final bounded-search report: MATCH |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` | corrected final report, including Addendum A: MATCH |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | final source/domain report: MATCH |
| `notes/sources/framework_source_manifest.md` | `4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e` | final source/locator manifest: MATCH |
| `notes/sources/framework_sources.sha256` | `7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f` | final 12-entry source ledger: MATCH |
| `notes/sources/.gitignore` | `c36e58e6a0e338579a7be747879a2891b023bfb79a676da58afca5e1b94c86be` | local-PDF exclusion rule: MATCH |

The convention report's pre-addendum hash
`f1035a1344acd4a3b2d9a5e5d4615e5c1c680fc6c202461a59c3affb8259a04b`
is a historical byte state only. Addendum A in the final reviewed bytes
explicitly withdraws every occurrence of the earlier Austad locator and
supersedes it with Proposition 2.4, printed p. 7. This integrated gate binds
only the final hash `498830...` above.

## 2. Independent evidence-integrity receipts

Running `sha256sum -c notes/sources/framework_sources.sha256` from the source
directory returned **12/12 OK**: six retained PDFs and their six final
preflight sidecars. I also reran the ARS PDF read-integrity preflight directly
to standard output, without replacing a sidecar. All six PDFs returned
`PASS`, equal declared/enumerated/reader page counts, and no warnings:

| Source ID | PDF SHA-256 | Page receipt |
|---|---|---|
| `FW-AO20-v1` | `c4b7b1cb7e225e3873b1071deb844b047ba0f1404aac4ca97002862aec2682c7` | `13=13=13`, PASS |
| `SRC-AUSTAD21` | `9edaf338a3d1f2f1b503a3709f20fceaa2bf1a6624a8d6fce0d80f3f15c77bc3` | `22=22=22`, PASS |
| `SRC-HUL66` | `eacf80abfbd7dc7320b4130ff2a2028d98cbd89b48bcf8ee62562d3e79f64f4a` | `10=10=10`, PASS |
| `SRC-HUL64` | `a30bcf1bda9699b56f1a846f15bc46f0ce420fb42f114fdc22d564d0a6f321fa` | `12=12=12`, PASS |
| `SRC-KLEP65` | `75f9f5e62e47e8c9dc885a5eba74ccbdfaefa296c02b1fcc5de8fbcf9dd51264` | `73=73=73`, PASS |
| `SRC-LEPTIN68` | `0bde30eba4eb8cee42bed5285e32272994090d04fc8880f841799ed75c96039c` | `25=25=25`, PASS |

The Paper-11 sources reused in place also rehashed exactly:

- Tu PDF `ff88e322eee65d2d6dd083697c82febb3759268f9b36083264a3e20b6e586897`
  and PASS sidecar
  `e82c95d4c3fd668d43c324db0631216372cc67505234a73e2ddc9ebf875884af`;
- Buss--Holkar--Meyer PDF
  `8be7896ed1aab1138b8ccf067ebfbba0f8b7d8a1dc8713fbf6c2f173ffe647e6`
  and PASS sidecar
  `c288efb2dca89ca8fd47bd9371decb7d042853dd6b60b35897df2f70214bfb59`;
- Paper-11 framework manifest
  `b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f`.

The companion manuscripts and registered labels were independently checked
on these exact bytes:

| Companion | Manuscript SHA-256 | Verified owner locators |
|---|---|---|
| Paper 9 | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | `cor:packet` at line 409; `cor:orbit` at line 421 |
| Paper 11 | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | `thm:qc`, `thm:phi`, `thm:star-algebra`, `thm:regular`, `thm:completions` at lines 360, 466, 524, 598, 681 |
| Paper 12 | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | `thm:factorization`, `def:std`, `thm:std-topology`, `cor:packet-comparison` at lines 437, 671, 688, 1062 |

No broken, circular, or falsely transferred premise was found. Paper 9 owns
the packet/orbit inputs, Paper 11 owns only the untwisted actual global-QC
baseline, and Paper 12 owns only factorization and same-carrier
standardization. Paper 13 must prove every twisted identity and the cross-owner
support-transfer statement it claims.

## 3. Convention, locator, and source-ownership adjudication

### 3.1 Frozen signs are coherent

Independent substitution and coboundary checks agree with the active
amendment and with the convention audit:

- `sigma overline{tau}=delta a` orients
  `U_a:A_sigma -> A_tau`; hence `sigma=delta alpha` gives
  `U_alpha:A_sigma -> A_1`.
- The actual and time-reduced twisted products and involutions translate
  consistently from the locally compact group formulas with additive
  notation and `Delta_R=1`.
- The frozen projective law
  `lambda_sigma(s)lambda_sigma(u)=sigma(s,u)lambda_sigma(s+u)` and the
  intertwiner
  `Lambda_sigma(f)=M_overline(alpha) lambda(U_alpha f) M_alpha` have the
  correct direction and conjugations.
- If `alpha` and `beta` are trivializers, `beta/alpha` is required to be a
  continuous character; its multiplier is the correct mechanism for proving
  choice independence of both transported norms.
- With the phase convention `exp(iq)`, a lifted defect lies in `2 pi Z`, not
  merely `Z`. Normalization on both axes is mandatory. The remaining real
  continuous 2-cocycle coboundary step is still a genuine Phase-3 proof
  obligation and was not inferred from the lift setup.

These checks establish a coherent proof specification; they do not discharge
P13-3--P13-8.

### 3.2 Canonical analytic locator and ownership chain

Direct inspection of the retained published Austad manifestation confirms the
continuous normalized cocycle, twisted convolution, twisted involution,
projective left regular representation, and integrated form on physical
pp. 5--7. The amenability statement is **Proposition 2.4, printed p. 7
(reader page 7 of 22)**. The immediately preceding sentence identifies it as
a special case of Leptin `[39, Satz 6]`. Proposition 2.3 is not an admissible
downstream locator.

The permitted ownership chain is therefore:

1. Hulanicki supplies the locally compact group amenability/weak-containment
   background, including the Abelian group case;
2. Leptin Satz 6 supplies the original generalized-`L1` result;
3. Austad Proposition 2.4 supplies the exact continuous-cocycle twisted-group
   specialization; and
4. Paper 13 may use that result only on the standard one-object group `R`,
   after independently proving its exact time reduction and norm
   identifications.

No cited source owns an actual non-Hausdorff action-groupoid completion, and
the transported Paper-13 records must not be renamed as such.

The Hulanicki (1964) manifestation has a disclosed pagination anomaly: the
current IMPAN/DOI record gives pp. 27--59, while the retained official scan
visibly begins at printed p. 37 and ends at p. 59. Load-bearing locators use
the scan's physical pages and visible printed numbers. The manifest preserves
both facts and does not silently repair the bibliographic record; this is an
access/manifestation note, not an open finding.

### 3.3 Regularity and framework boundaries

The final manifest uses the closed regularity tags consistently:

- Sorkin is `CONTINUOUS/CONTINUOUS` at official-title/abstract level only. Its
  advertised continuous-real-line collapse is an exact prior-art sentinel,
  but inaccessible full-text detail owns no normalization, sign, proof step,
  quotient orientation, or physical-page locator.
- Kleppner is `BOREL/BOREL` and may provide historical multiplier background
  only. It cannot support a continuous trivializer.
- Austad, Austad--Ortega, Leptin, Hulanicki, Tu, and
  Buss--Holkar--Meyer are `MIXED`, with their relevant hypothesis, access,
  and ownership ceilings stated separately. No `MIXED` or Borel statement is
  promoted into P13-3.

For `|X|>=2`, the registered actual owner lies outside the audited standard
Hausdorff Haar-groupoid, Hausdorff étale, and Tu locally Hausdorff frameworks.
This is a named-framework exclusion only; it is not a claim that every
possible framework is absent. The singleton owner is exactly the ordinary
Hausdorff time group `R`, although the nondiscrete one-object group is still
not étale. The author fibre construction and any standard group result remain
separate until Paper 13 proves the typed time/group bridge.

## 4. Novelty and precedent boundary

The bounded search followed its preregistered decision rule: 24 primary
queries plus the one authorized Arm-B fallback, 119 displayed cards screened,
and 10 candidate identities scope-checked. Its maximum defensible conclusion
is accepted exactly as written:

```text
SUPPORTED_WITHIN_SEARCH
NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH
```

This is neither an absence proof nor a novelty, priority, or standalone
finding.

Arm A is prior art in substance. Sorkin advertises the exact continuous
real-line multiplier collapse; twisted convolution, gauge isomorphism, and
completion consequences are standard components distributed across the
audited literature. Paper 13 must credit that family and may not count Arm A
as its standalone contribution.

No direct external match for the full Arm-B conjunction was found within the
bounded search: same carrier with actual-indiscrete and orbitwise-standard
topologies, the typed identity comparison, time-only kernel, exact
`f=0 or Q finite` compact-support criterion, circle-gauge support invariance,
and the strictly conditional rational-Witt substitution. This non-hit leaves
P13-8 eligible for proof and later adjudication; it does not establish
originality.

The source/precedent boundary for P13-8 is exact:

- Paper 11 owns actual global-QC quasi-compactness and the time-only support
  identity.
- Paper 12 owns the same-carrier standard topology and the direction
  `J:G_std(X) -> G_actual(X)`.
- Standard topology owns compactness of finite coproducts and failure of
  compactness for an infinite coproduct of nonempty compact open summands.
- Nowhere-zero circle multiplication owns support preservation as an
  elementary fact.
- Paper 13's only candidate center is the correctly typed conjunction across
  those owners and its conditional fixed-prime specialization. A later
  independent post-proof reviewer must decide whether this creates a
  nonformal dependency break of substantive weight.

If P13-8 fails, a direct package precedent is later found, or the proved result
is judged a routine/direct restatement of the inherited facts, the active
disposition remains **`NOTE_OR_MERGE`**. This Phase-2 PASS cannot override
that rule.

## 5. Independent P13-8 feasibility check

The registered statement is type-correct and has a viable proof route:

1. Continuity of `J:G_std(X) -> G_actual(X)` gives the pullback direction from
   actual continuous functions to standard continuous functions.
2. For `f=0`, the support is empty and therefore compact for every `Q`.
3. For nonzero `f`, `supp(f)` is nonempty compact. If `Q` is finite, the
   support is a finite coproduct of compact sets
   `(R/H)_q x supp(f)` and is compact.
4. If `Q` is infinite, those nonempty component pieces give an open-component
   cover with no finite subcover, so the standard support is not compact.
5. A circle-valued gauge is nowhere zero and leaves the support unchanged.
6. Substitution of `H=(log p)Z` and the bare set `Q_p` is consequently
   conditional only; it licenses no assertion about the finiteness,
   cardinality, topology, enumeration, or measure of `Q_p`.

This check supports proof feasibility only. Phase 3 must supply the formal
proof on the frozen owners, and the later substantive-weight review remains
independent.

## 6. Findings and fail-closed obligations

**Critical findings: 0. Major findings: 0. Minor findings: 0.**

The former Austad “Proposition 2.3” locator is not open: it is expressly
withdrawn in the final convention-report addendum, corrected throughout the
final source manifest/report, and independently verified here. All downstream
work must use Proposition 2.4, printed p. 7.

The following are open theorem tasks, not Phase-2 review defects:

- P13-1: exact-lock normalization recheck only;
- P13-2: prove the typed normalized-complex commutation statements;
- P13-3: prove continuous real-line multiplier triviality in the frozen sign
  convention, including uniqueness modulo continuous characters;
- P13-4: prove all actual/time product, star, support, closure, associativity,
  and gauge-star identities;
- P13-5: prove the regular intertwiner, exact norm restrictions, choice
  independence, and only then the amenable full/reduced equality;
- P13-6 and P13-7: prove the finite registered retention conclusions and the
  conditional fixed-prime negative without arithmetic promotion; and
- P13-8: prove the exact support-transfer iff and gauge invariance, then submit
  it to a separate post-proof nonredundancy/standalone review.

The active fail-closed branches remain binding. In particular, an open P13-3
cannot be filled by Borel, measurable, smooth, abstract, or mismatched-sign
substitution; a nontrivial continuous class returns the project to Phase 1;
and a failed or routine P13-8 forces `NOTE_OR_MERGE`.

## 7. Final authorization boundary

The integrated Phase-2 gate is **PASS, C0/M0/m0**. It authorizes only:

1. bounded Phase-3 proof work on the frozen P13-1--P13-8 obligations above;
   and
2. a **separate, versioned deterministic-control design lock only** for the
   registered eleven-CSV inventory.

The design lock must freeze its schema, columns, exact row formulas, canonical
order and serialization, oracle, and pass/fail rules and must itself receive
independent review before any control implementation. Finite diagnostics may
not be presented as proof of an infinite or dense-stabilizer statement.

This PASS does **not** authorize deterministic-control implementation,
Stage-13 YAML, Route evaluation or Route audit, Route B invocation,
composition, manuscript drafting, citation-package promotion, standalone
status, release, Git actions, or public synchronization. The retained source
PDFs remain local-only and excluded by `notes/sources/.gitignore`. Route,
manuscript, and release gates remain blocked until their own later
authorizations.
