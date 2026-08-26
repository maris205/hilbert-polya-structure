# Paper 9 independent manuscript peer review — Round 1

Review date: **2026-08-14 (Asia/Shanghai)**  
Review mode: **ARS independent theorem / integrity / formatting audit**  
Reviewer profile: arithmetic dynamics, quotient topology, topological groupoids,
and computational reproducibility  
Write boundary: this reviewer writes only this report. It does not edit the
manuscript, bibliography, PDF, source/proof locks, Route YAML, historical
Paper-8 artifacts, controls, or result files.

## 1. Review status

**PRE-MANUSCRIPT EVIDENCE GATE: PASS.**  
**INITIAL MANUSCRIPT GATE: REVISION REQUIRED.**  
**FINAL EXACT-BYTE RE-REVIEW GATE: ACCEPT.**

The frozen mathematical, source, Route, and deterministic-control packet is
coherent and is suitable for manuscript composition inside the exact claim
envelope in `composition_blueprint.md`. The initial manuscript required one
critical and eight major corrections. Section 10 records the exact-byte
re-review after those corrections, including theorem-by-theorem, citation,
build, visual, reproduction, and release-package closure.

Pre-manuscript finding count and gates still pending at that historical stage:

```text
Critical: 0
Major:    0
Minor:    0
Pending gates: manuscript, bibliography-context, build, rendered-visual,
               and final reproduction/package audit
```

The first manuscript bytes reviewed were
`paper/manuscript.tex`, SHA-256
`3675229e9ec46689d58559be0f6339fba1f3e618f6d950300bfd825408cbc9ad`.
That version produced the following initial findings:

```text
Critical: 1
Major:    8
Minor:    0
```

They remain part of the Round-1 record even if a later exact-byte addendum
verifies their resolution.

This is an independent review, not a restatement of
`notes/phase3_peer_review.md`. The review was performed against the exact
artifacts and locators recorded below.

## 2. Frozen baseline

| Artifact | SHA-256 | Independent status |
|---|---|---|
| `notes/composition_blueprint.md` | `9258fa741ad8cb60d7b5de4f9220ab64a7aa44a5490ed88c185094c4418a41f5` | read in full; claim/owner/release boundaries coherent |
| `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | read in full; theorem chain independently checked |
| `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | read in full; topology-owner ceiling preserved |
| `notes/route_audit.md` | `f6e3c0ef065fb675d1f6408a411dba14de1581c5dfe4800dbddb532adaf8e730` | read in full; eight typed records coherent |
| `notes/phase3_peer_review.md` | `447a6d575a27c87e3874591dfa3eae5f71ea1714819ada43263ffac44c53a678` | read in full; prior gate used only as corroboration |
| `results/packet_separation_manifest.json` | `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668` | independently reproduced and verified |

The active Phase-1 hashes printed in the blueprint agree with the current
files. The retained-source checksum ledger passes **14/14** when resolved from
the repository root. The five historical Stage-8 YAML hashes printed in
`route_audit.md:59-67` also agree with the current immutable files.

## 3. Independent mathematical review

### 3.1 Restricted quotient topology

`proof_audit.md:103-144` correctly proves that the global orbit quotient is
open and that the fixed-prime prepacket is saturated. For a relatively open
`O=V\cap Z_p`, saturation gives
`rho_p(O)=rho(V)\cap rho(Z_p)`, so the restricted quotient topology is exactly
the subspace topology inherited by `Gamma_p`. This lemma is placed before all
coordinate-based topology conclusions and prevents an illicit product- or
circle-topology substitution.

### 3.2 Simultaneous approximation

`proof_audit.md:151-214` supplies a valid constructive density proof. The
moduli `M_j` are cofinal among prime-to-`p` moduli; the congruence
`m_j \equiv a_jp^{k_j} (mod M_j)` is imposed so that
`q_j=m_jp^{-k_j}`—not merely its numerator—has the required profinite residue;
and the nearest-point choice gives both positivity and the stated real-error
bound. The proof uses the exact additive CRT channel and does not invoke the
false multiplicative-idele slogan excluded by the protocol.

### 3.3 Fixed-stage `E_f` convergence

`proof_audit.md:218-278` keeps raw characters, Galois-orbit points, and colimit
points distinct. Every rational approximant has finite kernel, convergence is
eventual equality on each finite-order element in one fixed raw fibre, and only
then is it passed through the continuous Galois quotient and colimit map. The
quotient-level stabilizer identity is explicitly not used as a raw-character
identity. This closes the most serious domain and topology risks in the
argument.

### 3.4 Exhaustiveness, equivalence, and universal specialization

The unit-normalization argument at `proof_audit.md:282-298` exhausts the packet
without transporting topology through Deninger's set parametrization. The
normalized equivalence criterion at `:300-324` correctly separates the
transverse `H_p=p^{\widehat{\mathbb Z}}` condition from the time `p^\mathbb Z`
condition. For arbitrary ordered packet points, the single sequence selected
at `:354-376` targets both `u/v` in the real coordinate and `ab^{-1}` in the
profinite coordinate. Its representatives remain in one quotient class while
converging in the prequotient to a representative of the arbitrary target.
Consequently the constant sequence at any `x` converges to every `y`.

### 3.5 Indiscreteness and nontriviality

The closure argument at `proof_audit.md:378-388` proves indiscreteness, not
merely non-Hausdorffness. Nontriviality is established separately for packet
and orbit by a time ratio outside `p^\mathbb Z`. For
`Q_p\simeq U_p/H_p`, `:419-424` uses the fact that a procyclic profinite group
has at most one element of order two, whereas two independent odd-prime sign
coordinates yield at least three nonidentity order-two elements in `U_p`.
Thus the stated failures of `T0`, `T1`, and Hausdorff separation are
non-vacuous for all three object types.

### 3.6 Nonclosed relation and comparison objects

The sequence at `proof_audit.md:443-464` consists of related pairs and converges
to a pair outside the exact restricted relation; its nonmembership follows
from the already proved exhaustive equivalence criterion. The naive adelic
argument at `:489-536` independently uses convergence in the restricted
product and unit normalization, rather than importing the Deninger result by
analogy. The source-owned intrinsic scaling-topos circle, naive inherited
adelic orbit, and explicitly retopologized standard-circle proxy remain
separate throughout `:538-572`.

### 3.7 Scoped groupoid consequence

`proof_audit.md:576-589` refutes only the frozen standard LCH-Hausdorff
transformation-groupoid branch: a Hausdorff groupoid cannot have the proved
non-Hausdorff unit subspace. It does not claim that every non-Hausdorff
groupoid, Haar system, completion, or trace theory is impossible. This is the
correct theorem strength.

## 4. Paper-8 corrigendum scope

The claimed failed premise is present at the stated historical locators:

- `papers/8-isotropy-trace/notes/phase2_source_topology_audit.md:203-239`
  types the Morishita target as a Hausdorff standard circle and uses
  compact-to-Hausdorff inverse continuity at `:237-239`;
- `papers/8-isotropy-trace/notes/phase3_topology_ownership_proofs.md:65-70`
  imports that orbit homeomorphism, and `:82-99` propagates it to the actual
  orbit's LCH/Haar owner;
- `papers/8-isotropy-trace/notes/proof_audit.md:74-80` and `:464-473` record the
  resulting actual-owner theorem package and source/new-proof ledger.

The Stage-9 correction is properly scoped as follows: the actual inherited
Hausdorff-circle premise and the standard-LCH actual-owner branches are
**REFUTED**; the algebraic/Floquet/FNS/corner calculations are **RETYPED** to
the explicit standard-circle proxy; proxy-internal statements are
**PRESERVED**; and the independent positive-time scalar ledger is
**UNCHANGED**. Historical Paper-8 bytes remain immutable. No current evidence
licenses saying that Paper 8's internal proxy algebra was disproved.

## 5. Route-A / Route-B audit

Independent PyYAML validation found exactly eight Stage-9 Route-A files and no
Stage-9 Route-B file. All candidate IDs match their directory names, all
top-level fields match the v0.2.0 output schema, all A2 blocks contain the nine
mandatory metrics, all overall verdicts are `ROUTE_A_EXPLORATORY`, and all
`route_b_invocation_allowed` values are Boolean `false`.

| Owner class | Independent tuple assessment |
|---|---|
| actual packet topology | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` — coherent |
| actual inherited orbit topology | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` — coherent |
| bare quotient `Q_p` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` — conservative and coherent |
| actual standard-LCH packet/orbit branches | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` — prerequisite failure correctly typed |
| bare standard-circle proxy | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` — model ownership explicit |
| proxy regular trace | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` — nonzero returns erased |
| proxy trivial-character trace | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` — exact proxy comb only |

No tuple can be strengthened by splicing actual-source A0, proxy A1, and the
independent scalar ledger. Nothing in the evidence packet defines a same-object
determinant, global analytic continuation, functional equation, Weil
compression, quantization, or Route-B-ready operator.

## 6. Independent deterministic reproduction

The reviewer executed `experiments/reproduce.sh` with bytecode disabled. The
receipt was:

```text
20/20 unit tests PASS
8 CSV artifacts / 240 data rows
verify-only hashes, sizes, rows, metrics, locks, and implementation hashes PASS
two fresh generations byte-identical
no __pycache__ artifact
manifest SHA-256:
52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668
```

The independently observed extrema agree with the proof/blueprint ledger:
maximum real error `6.5383536556262208e-06`, maximum finite-character error
`0`, and maximum correct-time error `7.7964676432670538e-05`. These are
deterministic finite regression controls. They do not prove any infinite
topological theorem or Route verdict.

## 7. Initial manuscript and release checks — historical Round-1 findings

### 7.1 Initial manuscript findings

#### Critical C1 — global invalid mathematical delimiters and build blockers

**Evidence anchors:** `paper/manuscript.tex:85-641`, with representative
instances at `:85`, `:103-109`, `:142-170`, `:220-225`, and `:637-641`;
additional deterministic errors at `:231`, `:298`, `:347`, and `:537`; the
undefined `\Tau` also occurs in
`paper/figures/topology_owner_split.tex:26`.

The manuscript uses plain parenthesized text such as `(p)`, `(E_f)`, and
`(D_p=\Z[1/p]_{>0})` as if parentheses opened and closed LaTeX mathematics.
They do not. Commands such as `\mathbb`, subscripts, superscripts, and
`\log` therefore occur outside math mode across the paper. Separately,
`\ell_i^{,j}` has a stray comma, two `quad` tokens lack a backslash, and
`\Tau` is undefined. The exact first draft cannot compile and is not a
reviewable release PDF.

**Required correction:** use real `\(...\)` or display math delimiters
consistently, correct the three local typographic errors, define or replace the
trace symbol, compile from a clean state, and supply a stable log/PDF hash.

#### Major M1 — finite-kernel proof contains false unit language

**Evidence anchors:** `paper/manuscript.tex:269-286`, especially `:269-280`.

The draft says evaluation factors through a finite quotient of `U_p` and calls
multiplication by `bq_j` a prime-to-`p` unit operation on “`p`-primary” data.
But `q_j=m_j/p^{k_j}` may have numerator factors at primes different from
`p`, so it need not be a unit of `A_p`; moreover the torsion orders in
`\overline{\mathbb F}_p^\times` are prime to `p`, not `p`-primary. The desired
finite-kernel conclusion is true, but the printed justification is not.

**Required correction:** restore the exact decomposition from
`proof_audit.md:218-265`: write `m=p^s m'` with `(m',p)=1`; identify the unit,
`p^s`, and `p^{-k}` factors as automorphisms and the `m'` factor as having
finite torsion kernel; then prove eventual equality modulo the order `N` of
each fixed torsion element before applying the Galois quotient and colimit
map.

#### Major M2 — unit normalization does not follow the locked source theorem

**Evidence anchors:** `paper/manuscript.tex:295-304`.

The coordinatewise-valuation paragraph is not the exact source argument and
does not transparently establish exhaustion of every `E_f` packet point. It
also obscures that one globally finite positive-integer factor, rather than an
arbitrary coordinatewise factorization, is supplied by Deninger's equation
(35).

**Required correction:** state the locked form `a\nu`, with `a\in U_p` and
`\nu\in\mathbb N`; absorb powers of `p` into `a`; and print the exact diagonal
action identity showing
`[j(P_{a\nu}),u]=[j(P_a),\nu u]`, followed by the set-level exhaustion from
equations (38)--(39).

#### Major M3 — normalized-equivalence proof is under-justified

**Evidence anchors:** `paper/manuscript.tex:306-332`, especially `:317-329`.

The phrase “the two conditions coupled by the same rational orbit relation”
is liable to suggest an equality of the profinite and integral powers, while
the proof replaces the necessary valuation and Galois-quotient argument with
“the common power relation.” The locked proof requires a precise distinction
between rational `q=p^n`, the quotient-level `H_p=p^{\widehat{\mathbb Z}}`
ambiguity, and the exact time stabilizer `p^\mathbb Z`.

**Required correction:** reproduce the necessity argument from the rational
orbit equation, show that a positive rational unit at every away-from-`p`
place is a power of `p`, invoke the exact Galois quotient, and derive
sufficiency from Deninger's balanced-product set theorem. Do not state or
imply a raw-character equality.

#### Major M4 — actual-to-actual Morishita proposition is asserted rather than proved

**Evidence anchors:** `paper/manuscript.tex:480-490`.

The proposition promises finite-kernel nonvanishing, unit normalization, and
an induced bijection, but its proof does not show any of them. In particular,
it omits the exact away-from-`p` components `\nu a_\ell`, diagonal
`\nu^{-1}` normalization, right unit normalization, orbitwise surjectivity,
and the equal-stabilizer injectivity step.

**Required correction:** restore those calculations from
`proof_audit.md:554-567`, then use the already proved indiscreteness of both
actual owners only for the final homeomorphism conclusion.

#### Major M5 — the manuscript invents non-existent `P9-10`--`P9-20` labels

**Evidence anchors:** `paper/manuscript.tex:124-129`.

The pre-registered proof targets are `P9-1`--`P9-9`; the twenty manuscript
claims are `C-01`--`C-20`. Calling table rows `P9-1--P9-20` breaks exact claim
traceability and conflicts with both the protocol and the composition
blueprint.

**Required correction:** use `C-01`--`C-20` in the table, or map each row
explicitly to both the real `P9-1`--`P9-9` proof target and its `C-xx` claim
IDs without inventing new `P9` identifiers.

#### Major M6 — Route-A layers A2 and A3 are misdefined

**Evidence anchor:** `paper/manuscript.tex:574`.

The draft calls A2 the missing exact explicit-formula bridge and A3 the
missing zero/divisor correspondence. Under `route-a-evaluator` v0.2.0, A2 is
the dynamical-zeta/Fredholm-determinant layer, including frozen divisor/zero
testing, while A3 is global analytic structure together with natural
Weil-compression compatibility. The prose does not match the frozen YAML
schema.

**Required correction:** use the canonical Route definitions and retain the
same conservative `A2_FAIL/A3_FAIL/A4_FAIL` verdicts.

#### Major M7 — unverified human-approval assertions

**Evidence anchors:** `paper/manuscript.tex:696-709`, especially `:699-709`;
composition requirement `notes/composition_blueprint.md:308-320,346-347`.

The manuscript makes affirmative authorship-role, competing-interest,
funding, acknowledgement, and “final manuscript reviewed and approved by the
author” declarations even though the composition blueprint requires human
confirmation before submission and no such final-manuscript confirmation is
part of the reviewed evidence packet. The AI sentence is especially
temporally impossible for this first draft.

**Required correction:** obtain and record human confirmation, or replace
these assertions in the research artifact with explicit pending-confirmation
language. Never represent autonomous pipeline review as the named author's
final approval.

#### Major M8 — incomplete published chapter metadata

**Evidence anchor:** `paper/references.bib:57-72`, DOI
`10.1090/conm/842/16852`.

The BibTeX record for Connes--Consani's published chapter omits its page range.
An independent Crossref lookup on 2026-08-14 returns the matching title,
authors, DOI, June-2026 publication, and pages **105--132**. Under the ARS
integrity gate, an incomplete chapter record is not a clean bibliographic pass.

**Required correction:** add `pages={105--132}` and ensure the rendered
bibliography retains the volume/DOI/version-family distinction between the
published chapter and the arXiv-v1 technical locators.

### 7.2 Rendered-figure advisory pending PDF

`paper/figures/topology_owner_split.tex:29-34` draws a dashed intrinsic-to-naive
set-comparison edge and a red barred reverse edge on the same geometric path,
and labels the proxy-to-intrinsic edge “same underlying circle set.” This may
render as overlapping arrows or visually merge owners that the prose must
keep separate. The semantic owner split is correct in source, so no severity
is assigned until the stable PDF is inspected.

The final review will not infer these checks from the blueprint. It will verify
them directly against exact manuscript/PDF bytes:

1. map every theorem, corollary, abstract claim, figure caption, and conclusion
   sentence to C-01--C-20;
2. check all Deninger raw/Galois/colimit levels, action signs, stabilizers,
   universal quantifiers, and nontriviality arguments line by line;
3. audit every Paper-8 correction statement against the four-status matrix and
   historical locators;
4. verify all bibliography entries and citation contexts against primary
   source manifestations, with no unresolved or anchorless citation;
5. ensure the two figures keep actual, intrinsic, and proxy topology owners
   distinct and do not visually imply a forbidden homeomorphism;
6. compile the LaTeX from a clean state, inspect warnings, references, fonts,
   page geometry, overfull boxes, and the rendered PDF page by page;
7. rerun the deterministic controls and compare manuscript numbers with the
   exact manifest;
8. confirm no local source PDF is included in the public release package and
   no unapproved authorship, funding, conflict, licence, DOI/archive, or data
   availability assertion is made.

## 8. Initial editorial assessment — historical Round-1 gate

The evidence packet has a clear and potentially significant theorem: a
constructive simultaneous real/profinite approximation channel collapses the
actual inherited prime packet topology to the indiscrete topology and exposes
a precise owner-attribution error in the preceding paper. The proof is concise,
uniform in `p`, and unusually careful about raw-character versus quotient-level
identities. Its main publication risks are no longer mathematical gaps in the
frozen proof; they are manuscript-level overstatement, topology-owner
conflation, citation-context drift, and failure to distinguish finite controls
from proof.

**Provisional gate: PASS TO MANUSCRIPT AUDIT.** No final score or publication
verdict is issued before the exact manuscript and rendered PDF are available.

## 9. Review integrity disclosure

This review followed the ARS reviewer, integrity-verification, and formatting
instructions. It used exact-byte local evidence, source preflight/checksum
ledgers, independent theorem reconstruction, mechanical Route-YAML parsing,
historical-locator comparison, and a fresh deterministic reproduction. It did
not modify any audited artifact, did not use Riemann-zero data or fitted target
data, and did not upload unpublished material to an external model.

## 10. Exact-byte re-review addendum and final gate

### 10.1 Locked release tuple

The re-review was performed against the following stable release bytes. No
manuscript, bibliography, PDF, figure, lock, YAML, historical Paper-8, control,
or result byte was changed by this reviewer.

| Release artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` |
| `paper/references.bib` | `0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35` |
| `paper/figures/constant_class_convergence.tex` | `abece8b050760a3a85afb88f12875f5eed6a39a7ccbc51e92d4e9adade4f9cb7` |
| `paper/figures/topology_owner_split.tex` | `53b4c678011d90d9cc20cba5e6b37720c14b1f9462cf2e9e1a2e2e81f8b7f1dc` |
| `paper/paper.pdf` | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` |
| `paper/paper.log` | `4042b378a758e588e9e9b1bc424438926d4cb183cec12ecda8c3921655eadbc2` |
| `paper/README.md` | `5ac7a34024672d01ce2e8d9cac24036c0e7be9f2516b79da7603a5dfaf04eb34` |

The README hash is later than the stable manuscript/PDF tuple only because its
page-count receipt was corrected from 20 to the actual 21 pages. The current
record agrees with `pdfinfo` at `paper/README.md:26,54,61-63` and does not
change the paper.

### 10.2 Resolution of the initial findings

| Finding | Exact-byte resolution | Status |
|---|---|---|
| C1 — invalid delimiters/build blockers | All mathematics is now in valid math environments; `\Tau` is defined at `manuscript.tex:74`; both TikZ sources compile; the clean four-pass build has no undefined control sequence, error, missing glyph, unresolved reference/citation, or overfull box. | **RESOLVED** |
| M1 — false unit language | `manuscript.tex:273-309` now writes `q_j=m_j/p^{k_j}`, factors `m_j=p^{s_j}m'_j`, proves finite kernel factor by factor, then proves eventual equality modulo `N=ord(zeta)` before quotient/colimit passage. | **RESOLVED** |
| M2 — unsupported normalization | `manuscript.tex:315-333` now uses Deninger equation (35)'s exact `a nu` form and prints `(j(P_a),nu u)nu=(j(P_{a nu}),u)` before invoking equations (38)--(39) for exhaustion. | **RESOLVED** |
| M3 — under-justified equivalence | `manuscript.tex:335-363` derives `q=u/v`, the away-from-`p` valuation condition, `q=p^n`, Galois ambiguity `H_p`, and sufficiency from the balanced-product set theorem without claiming a raw-character identity. | **RESOLVED** |
| M4 — asserted Morishita comparison | `manuscript.tex:515-523` prints the away components `nu a_ell`, diagonal `nu^{-1}` and integral-unit normalization, orbitwise surjectivity, equal-stabilizer injectivity, and only then the indiscrete-space homeomorphism conclusion. | **RESOLVED** |
| M5 — invented target IDs | The ledger at `manuscript.tex:126-131` now uses the authorized `C-01`--`C-20` identifiers. | **RESOLVED** |
| M6 — incorrect Route definitions | The exact enum tuples appear at `manuscript.tex:595-610`; `:612` now gives the correct A2 determinant/divisor-test, A3 global-analytic/Weil-compression, and A4 quantization meanings. | **RESOLVED** |
| M7 — unverified human assertions | `manuscript.tex:734-747` now marks CRediT, competing-interest, funding, acknowledgement, and final verification as provisional or requiring human confirmation. The README repeats the same submission boundary at `:89-93`. | **RESOLVED** |
| M8 — incomplete chapter metadata | `references.bib:58-65` now records volume 842, pages 105--132, publisher, and DOI `10.1090/conm/842/16852`; the rendered entry retains the arXiv-v1 technical-locator note. | **RESOLVED** |
| Figure advisory | The final owner map has one unambiguous solid actual-to-actual arrow, separate dashed set/action arrows, and a standalone red dashed unavailable-branch box; source is `topology_owner_split.tex:14-32`, rendering is PDF p. 14. | **RESOLVED** |
| README page-count residual | The package record now says 21 pages at `README.md:26,54` and extends its recorded raster inspection through page 21 at `:61-63`. | **RESOLVED** |

### 10.3 Theorem-by-theorem closure

| Result / claim block | Stable manuscript anchor | Independent disposition |
|---|---|---|
| restricted open quotient and saturated restriction (C-01) | `manuscript.tex:194-218` | **PASS** — the inherited packet topology is obtained before any coordinate topology is used |
| positive real/profinite approximation (C-02) | `:222-265` | **PASS** — positivity, real sign, cofinal moduli, and the twisted numerator congruence are all explicit |
| fixed-stage finite-kernel convergence (C-03) | `:267-309` | **PASS** — approximants and limit stay on the licensed finite-kernel domain, with raw/Galois/colimit levels separated |
| unit normalization and exact equivalence (C-04--C-05) | `:311-363` | **PASS** — exhaustive set/action normalization and exact `H_p`/`p^Z` relation; no topology transport |
| universal constant-class convergence (C-06) | `:365-407` | **PASS** — one sequence simultaneously targets `u/v` and `ab^{-1}`, is constant after quotient, and converges to the arbitrary target |
| packet, orbit, and time-quotient indiscreteness/nontriviality (C-07--C-09) | `:409-441` | **PASS** — topology and nontriviality are proved separately for every named owner |
| nonclosed restricted relation (C-10) | `:443-465` | **PASS** — a convergent sequence of related pairs has an explicitly unequal limit pair |
| set models and naive adelic orbit (C-11--C-12) | `:482-509` | **PASS** — the double-quotient theorem is proved directly and is not imported from another topology owner |
| repaired Morishita map and intrinsic scaling circle (C-13--C-14) | `:511-543` | **PASS** — exact `E_f` nonvanishing/normalization and source-owned topology split are visible |
| scoped LCH-Hausdorff consequence (C-15--C-16) | `:545-551` | **PASS** — only the named Hausdorff unit-space prerequisite fails; no general non-Hausdorff no-go is claimed |
| Paper-8 corrigendum/retyping/scalar boundary (C-17--C-18) | `:553-587` | **PASS** — all ten historical branches match the versioned matrix and the exact historical locators |
| controls and Route ceiling (C-19--C-20) | `:589-671` | **PASS** — eight frozen exploratory tuples, exact A2/A3/A4 failures, no Route B, and finite-control limits are explicit |
| abstract, owner figure, conclusion | `:87-99`, `:527-543`, `:673-679` | **PASS** — each restates the theorem and limitations without broadening the claim ledger |

The Paper-8 historical bytes were rechecked and remain exactly:

```text
phase2_source_topology_audit.md  f76dc87df56bacc54ea420447b28cb37020fc2625fa97d2eca2f173278ee83a3
phase3_topology_ownership_proofs.md 209989444b48a625777c0c4626b92429ed08b58f3dc4c31b03f7d23b067dca14
proof_audit.md                    1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990
stage8_summary_zh.md              4aede4aaac2161350786a1c29991565c569d0d3bd41ad6769ba6ec5a2c618771
```

The failed compact-to-Hausdorff step remains at the manuscript's stated
historical locator, `phase2_source_topology_audit.md:237-239`, and its exact
propagation remains at `phase3_topology_ownership_proofs.md:65-70,82-99` and
the two `proof_audit.md` ranges. Paper 9 corrects ownership without altering
those historical bytes.

### 10.4 Citation, source, Route, build, visual, and reproduction audits

- **Citation/source:** 20 citation commands close onto exactly seven unique
  BibTeX keys and seven entries. Every load-bearing technical locator and
  manifestation was checked; the retained PDF/preflight checksum ledger passes
  14/14. There is no unresolved or anchorless citation and no source-owned
  set bijection is promoted to a topology theorem.
- **Route:** exactly eight Stage-9 Route-A YAMLs retain the eight SHA-256 values
  printed in Appendix A; there is no Stage-9 Route-B YAML. The manuscript's
  exact enum strings and all-false A2/A3/A4 tail agree row for row with the
  machine-readable records.
- **Clean build:** a fresh temporary directory containing only the stable TeX,
  BibTeX, and two TikZ sources was built with XeLaTeX, BibTeX, XeLaTeX twice.
  The result is 21 A4 pages, PDF 1.5. The log contains zero error, undefined
  control sequence, unresolved citation/reference, BibTeX warning, missing
  glyph, or overfull box; six harmless underfull boxes remain. All eight font
  entries report `emb=yes`, `sub=yes`, and `uni=yes`.
- **Release/rebuild equivalence:** PDF byte hashes differ only because volatile
  PDF metadata is regenerated. Released and rebuilt PDFs have identical
  layout-preserving extracted-text hash
  `fb94d76d0b9be5649a836cd8d3f46dbdb8a5c6a7d0e69143d4eda9aee391755d`
  and identical ordinary extracted-text hash
  `b56e34c882685be9261fbee1066000347a0600203d73095fe1cdee6f05251b43`.
- **Visual:** all pages 1--21 were independently rasterized and inspected.
  There is no clipping, collision, missing glyph, unreadable table, ambiguous
  edge, broken continuation header, or owner merge. Both figures remain legible
  at page scale. Table 1's float briefly interrupts a sentence across pp. 3--5
  and p. 21 is intentionally sparse; these are optional production reflow
  opportunities, not correctness or release findings.
- **Reproduction:** the final verify-only rerun reports 20/20 unit tests, 240
  CSV rows, the same three extrema, and manifest SHA-256
  `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668`.
  The earlier full reproduction in this review also produced two byte-identical
  fresh generations and no bytecode/cache artifact.
- **Size/count receipt:** `manuscript.tex` contains 6,914 whitespace-delimited
  source tokens; conservative `detex` prose extraction gives 5,869 words, while
  complete PDF text extraction gives 8,391 tokens including mathematics,
  tables, declarations, appendix, and references. The PDF is 21 pages. The
  paper has 20 citation commands and seven bibliography entries. The numerical
  difference is tooling-defined and is disclosed rather than hidden; the
  theorem proofs are complete and the blueprint's target length is not treated
  as a claim-strength substitute.

### 10.5 Five-dimension score

| Dimension | Weight | Score | Weighted contribution | Key evidence |
|---|---:|---:|---:|---|
| Originality | 20% | 8.8/10 | 1.76 | A bounded, explicitly qualified source search found no prior theorem for the exact inherited `E_f` packet; the topology theorem and scoped corrigendum form a clear new conjunction. |
| Methodological rigor | 25% | 9.5/10 | 2.38 | The proof is constructive, uniform in `p`, owner-typed, and theorem-by-theorem complete; finite controls are never promoted to proof. |
| Evidence sufficiency | 25% | 9.4/10 | 2.35 | Exact source manifestations/locators, 14/14 checksums, historical bytes, eight Route YAMLs, and independent reproduction support every load-bearing boundary. |
| Argument coherence | 15% | 9.2/10 | 1.38 | The dependency order runs from quotient ownership through approximation and character convergence to specialization, consequences, comparison, and corrigendum without circularity. |
| Writing quality | 15% | 8.8/10 | 1.32 | Notation levels, claims, limitations, tables, bilingual abstract, citations, and native figures are clear; only optional float/page reflow remains. |
| **Overall** | **100%** |  | **9.19/10** | **Accept band.** |

### 10.6 Final editorial disposition

```text
Critical: 0 unresolved
Major:    0 unresolved
Minor:    0 unresolved
Verdict:  ACCEPT
```

All initial C1/M1--M8 findings and the rendered-figure advisory are closed on
the locked bytes above. The paper stays inside C-01--C-20, the Paper-8
corrigendum is exact and versioned, Route A remains exploratory for all eight
objects, and Route B remains uninvoked.

Two external pre-submission actions are intentionally not converted into paper
findings: the human author must confirm the provisional declarations before
journal submission, and a future public GitHub synchronization must exclude
local `notes/sources/*.pdf` unless exact-manifestation redistribution rights
are documented. No Git repository is present in this workspace snapshot, so
the latter boundary can be enforced only at the actual synchronization step.
