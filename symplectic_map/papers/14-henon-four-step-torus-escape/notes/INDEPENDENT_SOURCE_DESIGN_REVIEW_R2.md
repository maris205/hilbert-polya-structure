# SOURCE_DESIGN_PASS

## R2 identity and narrow mandate

This is the narrow second-round independent source-design review dated
2026-08-16.  Review began only after the author supplied an explicit
stop/freeze signal and the three replacement hashes.  Before that signal, the
three files under repair were not opened and no project file was written.

The controlling citation audit is
notes/INDEPENDENT_CITATION_PRECISION_AUDIT.md with SHA-256

7e625c593267545088320459b65e990fdea5e347ed779416a6ce334d5a131f17.

Its citation-only verdict was CITATION_REPAIR_REQUIRED with the five-item
ledger R1--R5.  This R2 review checks only whether those repairs were
implemented precisely, whether any unrelated source claim moved, and whether
the theorem and window convention remain unchanged.

The canonical R2 verdict is:

> **SOURCE_DESIGN_PASS.**  R1--R5 are implemented accurately; the frozen
> theorem, quantifiers, proof, and window convention are unchanged; and no
> unauthorized source-state artifact is present.

## Freeze and hash gate

The author supplied the following stable post-repair files:

| Authorized changed file | Bytes | Frozen SHA-256 |
|---|---:|---|
| notes/CITATION_VERIFICATION.md | 12,919 | 0c9b08f566eedb1e9f344f6fb07dfcf0c87015daa566435d0c989ac722d4e2af |
| notes/NOVELTY_ASSESSMENT.md | 8,660 | 2fafbef234a7e7cc8fbe10b25e0b920188b3c35472538fcbaf023da8d357bac1 |
| refine-logs/FINAL_PROPOSAL.md | 7,814 | 719214a159f1e36676d059c626dcefab7fe11b012e44146243db8aa500eb38a0 |

All three observed byte counts and hashes agree exactly with the freeze
message.

The citation audit itself also agrees exactly with the controlling hash
above.  The eight other pre-existing source-design files agree byte for byte
with the manifest frozen in that audit and with the preceding source-design
review:

| Immutable file | Verified SHA-256 |
|---|---|
| experiments/EXPERIMENT_PLAN.md | 709b32fa83e7cf1502e57393e4b46daf33c83ccb88832a498e223d084eabbd95 |
| experiments/EXPERIMENT_TRACKER.md | da117759e1e6a95579fcae16f27c3c868bd67b6d0b8b5d98e936b456a9354a97 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | e3dc9864c72d150e0f7a69d08aad9f4e24f0dde1c6115fe3d428b129ade4573c |
| notes/PROOF_PACKAGE.md | c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa |
| notes/RESEARCH_QUESTION.md | 782b48dfec973d877bf87c964a3bdd7227b52a21101b68a9a576929441bedb9c |
| refine-logs/INITIAL_PROPOSAL.md | ecb3a5151c75dba6ac4b8415d000f9a9a3c36ff80af5b651b9de7ecbad7a6e22 |
| refine-logs/REVIEW_SUMMARY.md | ac2a75bb0f393de1255958705bbcd2e75fa1e0800805d420f048cb0f72c5d54f |

In particular, notes/PROOF_PACKAGE.md is byte-for-byte unchanged.  The
observed state before this R2 file was written therefore had exactly the
expected twelve regular files: the eleven earlier source-design files plus
the controlling citation audit.  The only changes to the original eleven
were the three authorized R1--R5 targets.

## R1--R5 implementation audit

### R1: Mello--Yasufuku range correction

PASS.  V12 now names Theorems 1.1--1.2, Corollary 1.3, and Theorem 4.2 and
states the scope accurately:

- the main theorems concern projective endomorphism semigroups over number
  fields and finitely generated subgroups;
- they are conditional on $\mathrm{Hyp}_\epsilon$ and require
  $\epsilon\ge(1+c)/2$;
- Theorem 4.2 assumes additional divisor hypotheses and Vojta's Main
  Conjecture and obtains the relevant non-density only for sufficiently small
  $\epsilon$;
- consequently Theorem 4.2 does not establish the general hypothesis needed
  by the main theorems.

The revised text no longer presents Vojta as a general route that verifies
the main hypotheses.  It also keeps the result outside unconditional Hénon
fixed-window scope.

This wording was checked directly against
Mello--Yasufuku, arXiv:2604.03745v1, especially Theorems 1.1--1.2,
Corollary 1.3, the discussion immediately following Corollary 1.3, and
Theorem 4.2.

### R2: Kim--Krieger--Postolache--Szeto range correction

PASS.  V10 now states:

- Theorem A is for every odd $d>2$;
- it constructs a rational polynomial $s_d$ of degree at most $d$ such that
  $h_d(x,y)=(y,-x+s_d(y))$ has at least $(d-4)^2$ rational periodic points;
- Theorem B is for $d\equiv1\pmod6$ and gives an integer cycle of length
  $(8d+10)/3$;
- after swapping coordinates this is a general-polynomial Hénon family, not
  the monomial-plus-constant family of Paper 14.

The text no longer attributes the theorem to the impossible phrase “odd
$d\ge2$,” and it distinguishes the rational Theorem A statement from the
integer-cycle Theorem B statement.  This wording was checked directly
against arXiv:2412.01668v2, Theorems A and B.

### R3: Bell--Ghioca V7A

PASS.  The new entry is labeled V7A, so V8--V13 were not renumbered.  It
accurately records Bell--Ghioca Theorem 1.1:

- part (i) treats the return times of one fixed orbit of a rational self-map
  of a semiabelian variety to a finitely generated subgroup, giving finitely
  many arithmetic progressions plus a Banach-density-zero residual set;
- part (ii), under regularity, replaces only the residual set by a finite
  set, and does not imply that the arithmetic-progression portion or the
  whole return-time set is finite;
- $H|_{\mathbb G_m^2}$ is generally only a rational torus self-map, because
  $b x^d+a y+c$ can vanish;
- neither clause counts all initial states, imposes a prescribed finite
  window, or yields a rank-only cardinality bound.

These statements were checked directly against Bell--Ghioca,
arXiv:2210.03152, Theorem 1.1(i)--(ii).

### R4: theorem-number precision

PASS.  The repaired citation file contains the required theorem numbers with
their correct comparison roles:

| Entry | Locked result numbers | Role verified in R2 |
|---|---|---|
| V2 | Theorems 1.7--1.8 | distinct one-variable image and orbit $S$-unit results |
| V5 | Corollary 4.9; Theorem 4.11 | consecutive-iterate dependence and distinct-iterate finiteness under stated hypotheses |
| V6 | Theorems 1.2--1.4; Theorem 1.7 | exceptional-map scope and polynomial-iterate finiteness modulo a finitely generated group |
| V7 | Theorems 1.1--1.2 | fixed-orbit membership-time structure and torus-factor conclusion |
| V7A | Theorem 1.1(i)--(ii) | fixed-orbit whole-state subgroup return times |
| V8 | Theorem 1.2; Corollary 1.5 | projective fixed-orbit non-density and its integral-point consequence |
| V9 | Theorem 1.2 | common-iterate locus for compositionally independent Hénon-type maps |
| V10 | Theorems A and B | general-polynomial Hénon lower bounds and a long integer cycle |
| V11 | Theorem 1.8; Corollary 1.9 | cyclotomic Hénon-type and plane positive-entropy non-density |
| V12 | Theorems 1.1--1.2; Corollary 1.3; Theorem 4.2 | conditional projective semigroup dependence and the distinct Vojta range |

None of V2--V13 is imported into the Paper 14 proof.  The theorem numbers
lock the prior-art boundary only.

### R5: novelty and final-proposal propagation

PASS.  Both notes/NOVELTY_ASSESSMENT.md and
refine-logs/FINAL_PROPOSAL.md now:

- distinguish Bell--Chen--Hossain's one-observable fixed-orbit result from
  Bell--Ghioca's whole-state fixed-orbit subgroup result;
- state that neither is an all-initial-state, fixed-window, rank-only
  cardinality theorem;
- give the corrected Theorem A/B role for Kim et al.;
- state the conditional $\mathrm{Hyp}_\epsilon$ status of
  Mello--Yasufuku and distinguish the main theorems' large-$\epsilon$
  requirement from Theorem 4.2's small-$\epsilon$ conclusion;
- identify the residual novelty axes as all initial states, a fixed
  four-transition window, a degree-and-rank-only bound, finite-rank rather
  than finitely generated groups, and the exact $T_4/T_3$ threshold.

The bounded-search novelty wording remains conservative.  The novelty score
is still $7.0/10$, and the two standalone-size and proof-confidence records
are unchanged and remain advisory rather than theorem evidence.

## Theorem and quantifier preservation

The current theorem-bearing files still have the exact same claim:

- $K$ is an arbitrary field of characteristic zero;
- $d$ is an integer with $d\ge2$;
- $a,b,c\in K^\ast$;
- $\Gamma\le K^\ast$ is any finite-rank subgroup of rank $r$;
- no coefficient-membership or finite-generation assumption is introduced;
- $H(x,y)=(b x^d+a y+c,x)$; and
- the uniform upper bound is

$$
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
$$

The existential rank-one $T_3$ sharpness theorem and the weighted bound for
exact periodic orbits wholly contained in $\Gamma^2$ are also unchanged.
No citation repair has entered the theorem, proof, constant, coefficient
hypotheses, orbit-containment semantics, or nonclaim boundary.

The fixed-coefficient ESS use also remains unchanged.  The variables

$$
(x_{i+1},x_i^d,x_{i-1})
$$

lie in $\Gamma^3$, of rank at most $3r$, while
$c^{-1},-b/c,-a/c$ are fixed nonzero coefficients.  ESS is the only
external proof theorem.

## Window-convention audit

The controlling convention is still

$$
T_m(H,\Gamma)=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2
\text{ for every }0\le j\le m\}.
$$

It has not been shifted to $0\le j\le m-1$.

Consequently:

- $T_4$ contains the five states
  $P,H(P),H^2(P),H^3(P),H^4(P)$;
- these five states supply four local recurrence equations at
  $i=0,1,2,3$;
- “four-step” and “four-transition” are equivalent descriptions in this
  package, but “four states” would be incorrect;
- $T_3$ contains four states and three transitions; and
- the explicit rank-one construction proves that this immediately shorter
  $T_3$ window can be infinite.

notes/PROOF_PACKAGE.md, notes/RESEARCH_QUESTION.md, and
refine-logs/FINAL_PROPOSAL.md all state the correct $0\le j\le m$
convention.  The novelty and citation files consistently use
“four forward iterates” or “four-transition window.”  The sole appearance of
$0\le j\le m-1$ is in the controlling citation audit's explicit withdrawal
of that earlier external suggestion; it is not a live project definition.

## Citation-role and collision conclusion

The proof/citation separation remains sound:

1. Evertse--Schlickewei--Schmidt, published Theorem 1.1, is the only imported
   theorem.  It supplies the fixed-coefficient finite-rank bound for
   nondegenerate solutions.
2. Bell--Ghioca is the closest newly recorded whole-state subgroup
   near-neighbor, but it concerns one fixed orbit and a finitely generated
   subgroup and supplies return-time structure rather than all-initial-state
   cardinality.
3. Kim et al. provide degree-dependent lower-bound context for a
   general-polynomial Hénon family.
4. Mello--Yasufuku provide a conditional projective-semigroup
   multiplicative-dependence boundary, with no unconditional Paper 14
   fixed-window conclusion.
5. The remaining sources retain their one-dimensional, fixed-orbit,
   non-density, common-zero, height, or parameter roles.

The repaired collision sentence is therefore safe:

> A targeted primary-source search through 2026-08-16 located no theorem
> combining the three-coefficient monomial Hénon family, arbitrary
> finite-rank multiplicative groups, a coefficient-uniform
> four-transition cardinality bound, and a rank-one sharp
> three-transition failure.

This remains explicitly a bounded-search conclusion, not absolute priority.

## Inventory and lifecycle audit

Before this authorized R2 file was added:

- there were twelve regular project files and no symbolic links;
- the only top-level project subdirectories were experiments, notes, and
  refine-logs;
- there was no lock or source-lock file or directory;
- there was no code, results, paper, or manuscript tree;
- the experiment records still report no scientific execution or result;
  and
- the lifecycle remained
  SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW /
  NO_CODE / NO_RESULTS / NO_MANUSCRIPT.

This R2 review is the authorized thirteenth regular file.  It creates no
source lock and authorizes no code, result, or manuscript.

## Final R2 disposition

All narrow gates pass:

1. the author freeze and three replacement hashes match;
2. the controlling citation-audit hash matches;
3. only the three authorized source-design files changed from the original
   eleven-file package;
4. every other source file, including the proof package, is byte-for-byte
   unchanged;
5. R1--R5 are complete and primary-source accurate;
6. the theorem, quantifiers, fixed-coefficient ESS role, and nonclaims did
   not move;
7. the $0\le j\le m$ convention and its five-state/four-transition
   interpretation remain correct; and
8. the inventory contains no forbidden artifact.

The canonical verdict is **SOURCE_DESIGN_PASS**.  No repair item remains
within the R2 mandate.
