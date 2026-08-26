# Full Stage-2 checkpoint -- Papers 67--71

Checkpoint date: 2026-08-25 UTC  
State: **AWAITING USER CONFIRMATION BEFORE STAGE 2.5**  
Checkpoint type: **FULL**  
External release: **HOLD**

## Outcome first

Stage 2 has landed five actual internal papers on five primary symbolic
dynamical systems.  Every row has a compiled PDF, theorem/proof package,
deterministic controls, a reproducible build, supplemental two-round
cross-agent improvement, and a separate two-round GPT-5.4/xhigh workflow
review.  All five final theorem packages pass the internal mathematical gate.

One Stage-1 row was deliberately replaced rather than padded.  The
Rudin--Shapiro skew-product calculation was mathematically valid, but owner
subtraction left too little independent paper mass.  P69 is now an
orientation-sensitive surface-group flat-connection SFT paper with a stronger
inverse theorem.

This is not a release-ready claim.  The source work performed in Stage 2 was a
bounded writing-level owner/subtraction gate.  Statement-level integrity,
alternate-terminology collision searching, priority clearance, specialist
review, and human release authorization belong to Stage 2.5 and have not run.

## Five landed papers

| Slot | Paper and primary system | Concrete mathematical progress | Final artifact |
|---:|---|---|---|
| P67 | *Arithmetic Prefixes and Cycle-Matroid Dependence in a Multiplicative Plaquette Shift*; multiplicative-semigroup shift on `N` | global free-axis coordinates; arbitrary finite projection dimension; complete alternating-cycle compatibility; direct-sum graphic matroid; Haar total correlation and forest independence; prefix/rectangle corollaries | [PDF](../../papers/67-multiplicative-plaquette-matroid-complexity/main.pdf), 11 pages, `48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e` |
| P68 | *Product Classification and Phase Rigidity for Complete-Bipartite Hom-Shifts*; `Z^d` hom-shift for nonempty bipartite parts and `d>=1` | explicit translation-equivariant radius-one dimer code; conjugacy iff `mn=rs`; subgroup finite-dependence dichotomy; correct arbitrary-shape language formula; pressure/equilibrium and finite-index periodic counts | [PDF](../../papers/68-complete-bipartite-homshift-conjugacies/main.pdf), 7 pages, `b96ac6118ad81839eb796ad5640357ce710ff9e1372411bfa7931883dd3ac7c6` |
| P69 | *Orientation-Sensitive Periodic Spectra of Surface-Group Flat-Connection Shifts*; nonorientable-surface-group SFT | rooted-gauge identity `|Fix_H X_K|=|K|^([Lambda:H]-1)|Hom(H,K)|`; orientable/nonorientable divisibility-directed cover-family spectra; joint recovery of `|K|` and `(d_chi,nu_chi)` multiplicities; exact `D_8/Q_8` separation | [PDF](../../papers/69-orientation-sensitive-surface-flat-sft/main.pdf), 10 pages, `09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08` |
| P70 | *Weighted Three-Term Shifts on Finite Heisenberg Quotients*; weighted linear shift over the discrete Heisenberg group | exact fixed-nullity formula with cyclotomic character term and `ell(ell-1)` nonlinear jump on `alpha^ell+beta^ell+gamma^ell=0`; cross-characteristic irreducible-block and convention audit | [PDF](../../papers/70-weighted-heisenberg-congruence-nullities/main.pdf), 7 pages, `e20e1151597684736d72deeac8875d4be0e5e95d95ef2c187468d07f734f3ac5` |
| P71 | *Degree Pressure, Multifractal Fibres, and Profile Rigidity for Full Zip Shifts*; noninvertible full zip shift | `P_tau(t)=log sum_z k_z^(t+1)` and unique equilibrium family; pressure derivatives; full Bowen entropy spectrum; profile recovery and conjugacy; degree-weighted periodic counts and zeta | [PDF](../../papers/71-zip-shift-degree-pressure/main.pdf), 9 pages, `ff85975c69b7848ff8675edde2e753ed9deb6cd377f37aeeb60669d403026bcf` |

The five PDFs total 44 pages.  Page count is not used as a quality metric; the
relevant gate is whether each manuscript carries a closed, nontrivial theorem
package after owner subtraction and hostile proof reconstruction.

## Concrete corrections made during Stage 2

### P67: finite-shape theorem and artifact integrity

The paper was enlarged from prefix/rectangle examples to the arbitrary finite
incidence-graph theorem.  Review caught and repaired a leaked LaTeX token, an
undefined graph-vertex symbol, and a malformed claims-ledger row.  Official
Round 2 then found that the live corrected PDF and old QA/hash receipts told
different freeze stories.  The mathematics passed; the package was not marked
complete until the final PDF, text/pdfinfo receipts, state, logs, and 73-entry
manifest were synchronized and replayed.

### P68: global phase, not componentwise phase

An early draft incorrectly multiplied phase contributions over disconnected
components.  A globally extendible pattern has one phase across the entire
lattice.  For nonempty finite `F`, the correct count is

```text
m^|F_even| n^|F_odd| + n^|F_even| m^|F_odd|,
```

with the empty shape handled separately.  The manuscript, weighted partition
identity, pressure proof, claims ledger, and controls all use this corrected
formula.  Both official reviews independently retested disconnected,
same-parity, `d=1`, and one-part-size-one cases and found no remaining theorem
defect.

### P69: replacement, moment recovery, and terminology

The rejected Rudin--Shapiro row is documented in
[the owner-subtracted rejection memo](../../papers/69-orientation-sensitive-surface-flat-sft/RUDIN_SHAPIRO_OWNER_MEMO.md).
The replacement paper closes a different theorem: joint orientation-sensitive
spectra recover finite-group character degrees and Frobenius--Schur indicators.
Official review required the odd-moment inversion to state explicitly that it
first recovers `(c_d^+-c_d^-)/d` and then multiplies by known `d`; it also
required an actual `nu=0` control branch.  A `C_3` control now reconstructs
`(c_1^+,c_1^-,c_1^0)=(1,0,2)`.  The final package also consistently calls the
all-modulus subgroups divisibility-directed families rather than falsely
nested chains.

### P70: full representation proof and honest control boundary

The final proof supplies the algebraic-closure clock--shift construction,
irreducibility and completeness, exact right-regular block convention,
character-gcd term, determinant calculation, and corank-one nonlinear lemma.
Official Round 1 accepted the theorem but rejected one evidence overclaim:
nullity-only full-matrix controls cannot distinguish the selected right action
from its dual-left convention when the theorem proves their total nullities
agree.  The controls are now described only as testing the implemented group
law/operator/final formula and omitted multiplicities; the convention is
settled analytically.  A priority-flavored “first nilpotent setting” phrase was
also neutralized.

### P71: genuine Bowen entropy rather than capacity counting

The first proof sketch used method-of-types counting without closing the
noncompact Bowen-entropy argument.  The final paper specifies the product
metric, proves the Bowen-ball/cylinder sandwich, gives a Caratheodory upper
bound through tail sets and countable stability, and gives an
entropy-distribution lower bound.  Natural-extension entropy, periodic
alignment, Legendre endpoints, and profile multiplicities were separately
audited.  Both official rounds found the repaired theorem package sound.

## Review and verification ledger

Each package contains two deliberately separated tracks:

1. a supplemental two-round cross-agent hostile-review/improvement track; and
2. a two-round GPT-5.4/xhigh workflow-review track run locally through Codex
   CLI, with a review file, resolution, and frozen PDF artifact for each round.

The second track satisfies the internal paper-improvement workflow used for
Stage 2.  It is not external peer review, does not confer specialist status,
and is unscored.  Scores preserved in some supplemental cross-agent histories
must not be transferred to the official workflow reviews.

| Slot | Official review closure | Final package status |
|---:|---|---|
| P67 | 2/2; theorem PASS; Round-2 stale-freeze defect resolved | `PASS / EXTERNAL HOLD` |
| P68 | 2/2; no official manuscript change required | `PASS / EXTERNAL HOLD` |
| P69 | 2/2; theorem PASS; terminology/QA package sync resolved | `PASS / EXTERNAL HOLD` |
| P70 | 2/2; theorem PASS; control-language minor revision resolved | `PASS / EXTERNAL HOLD` |
| P71 | 2/2; no official manuscript change required | `PASS / EXTERNAL HOLD` |

The five paper-specific deterministic controls all pass and reproduce their
stored outputs:

```text
P67  python3 code/verify_plaquette_matroid.py
P68  python3 code/verify_complete_bipartite.py
P69  python3 code/verify_surface_flat_sft.py
P70  python3 code/verify_weighted_heisenberg.py
P71  python3 code/verify_degree_pressure.py
```

All five final packages use deterministic LaTeX/BibTeX builds, have no open
critical or major mathematical issue in the official workflow reviews, and
retain package-level SHA-256 manifests.  The controls are regression evidence,
not premises for the universal statements.

## Diversity statement without overclaim

The batch has five distinct primary systems and five distinct main proof
cores:

1. arithmetic root decomposition and graphic matroids;
2. checkerboard phase rigidity and intrinsic dimer coding;
3. surface topology and complex Frobenius--Schur moment inversion;
4. modular finite-Heisenberg representation blocks and Fermat nullities;
5. noninvertible degree thermodynamics and Bowen multifractals.

There is some broad methodological overlap: P69 and P70 both use periodic data
and finite-group representation ideas; P68 and P71 both contain pressure and
conjugacy statements; P67 and P70 both study linear constraints.  The systems,
fields, invariants, and decisive proof engines nevertheless remain distinct.

## Source disposition and Stage-2.5 boundary

Stage 2 verified bibliographic metadata and owner clusters deeply enough to
write conservative internal drafts, returned classical/published inputs to
their owners, avoided worldwide priority language, and preserved exact claim
firewalls.  The status is

```text
STAGE2_BOUNDED_SOURCE_GATE /
BOUNDED_NO_EXACT_COLLISION_LOCATED /
NOT_A_PRIORITY_CERTIFICATE /
EXTERNAL_RELEASE_HOLD
```

Stage 2.5 has not started.  It must independently address at least:

1. line-by-line verification of every cited statement against primary text;
2. exact-neighbor searches under alternate algebraic, coding, entropy,
   topology, group-SFT, and thermodynamic terminology;
3. priority-sensitive collision and folklore review by relevant specialists;
4. failure-mode and claim-language integrity checks across manuscripts,
   abstracts, ledgers, controls, and PDFs;
5. human authorship, contribution, funding, competing-interest, citation, and
   AI-disclosure decisions; and
6. separate human authorization for any external circulation or submission.

## Evidence package

- [Packet overview](README.md)
- [Pipeline state](PIPELINE_STATE.yaml)
- [Material passport](MATERIAL_PASSPORT.md)
- [Theorem closure and replacement ledger](phase2/THEOREM_CLOSURE_AND_REPLACEMENT.md)
- [Writing-level source report](phase2/SOURCE_VERIFICATION_REPORT.md)
- [Historical Stage-1 checkpoint](STAGE1_REPORT.md)

## Confirmation boundary

The valid next state is
`AWAITING_USER_CONFIRMATION_BEFORE_STAGE_2_5_INTEGRITY`, not release-ready.
No external action is authorized by this checkpoint.

**Ready-to-proceed question:** does the user explicitly confirm entry into
Stage 2.5 integrity and priority clearance for these five frozen internal
papers?
