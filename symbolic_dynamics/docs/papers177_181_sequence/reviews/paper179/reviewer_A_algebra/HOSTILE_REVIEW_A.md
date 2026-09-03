# Hostile Review A — P179 random singleton isolation

**Role:** independent algebra/combinatorics reviewer; author files read-only  
**Frozen author baseline:** `main.tex` SHA-256
`a5d19d7049f896079d03fe377bcaaff43f7d247545b57946d8c4ca80cf89ac31`  
**Original Round-0 decision:** `MINOR_REPAIR / THEOREM_ACCEPT / HOLD_EXTERNAL`  
**Original Round-0 open findings:** `0 Critical / 0 Major / 2 Minor`  
**Round-1 delta disposition:** `ACCEPTED / HOLD_EXTERNAL`  
**Round-2 science re-entry disposition:** `ACCEPTED / HOLD_EXTERNAL`  
**Current open findings:** `0 Critical / 0 Major / 0 Minor`

## 1. Scope and independent method

I re-read the literal chain, all theorem statements and proofs, the claims
ledger, source verification, bibliography, narrative/plan/self-QA/build
surfaces, the author program and canonical, and the relevant internal
partition-dynamics firewall.  No manuscript, author code, bibliography, or
PDF was changed or compiled.

The independent verifier represents a set partition as a tuple of integer
bit-blocks, rather than as a restricted-growth word.  It tests the spectrum
by an exact characteristic polynomial of `nP=sum_i E_i`, not by the author's
rational eigenspace ranks.  Temporal measures are propagated as integer
counts and compared with a separately generated missing-set expansion whose
surjection counts are computed by inclusion--exclusion.  Every source-target
reachability test uses a blockwise admissibility generator.  This imports no
author or scout code.  Two fresh processes reproduce `CANONICAL.txt` byte for
byte.

## 2. Independent re-derivation

Removing labels `i` and `j` from their old blocks in either order leaves the
same residual blocks, so the maps are commuting idempotents.  Each
linearized `E_i` has square-free minimal polynomial dividing `x(x-1)`.
Commuting diagonalizable operators are simultaneously diagonalizable.
Ordering partitions by refinement makes `nP` triangular, with diagonal
entry equal to the number `s(pi)` of singleton blocks.  The number of
partitions with exactly `s` singletons is

```text
binom(n,s) D_(n-s),
```

where `D_r` counts singleton-free partitions.  The `n-1` layer vanishes
because the remaining label is also singleton, and the discrete partition
alone supplies eigenvalue one.  Exact characteristic polynomials through
`n=5` agree coefficientwise with this factorization; idempotence,
commutation, and layer counts were checked through the larger boxes recorded
in the canonical.

For a history support `A`, each old block `B` becomes the singleton labels
in `A cap B`, plus the residual `B\A` whenever that residual is nonempty.
In particular, an unselected one-label residual remains as a singleton; as
an endpoint partition it is indistinguishable from selecting that final
label too.  With `M=[n]\A`, absorption is therefore equivalent to
`|M cap B_j|<=1` for every old block.  Missing sets of size `m` have weighted
count `e_m(b_1,...,b_k)`, while histories with exact observed support of size
`n-m` number `(n-m)! S(t,n-m)`.  This proves the displayed absorption CDF,
including `t=0`.

For a fixed labelled target, an old block either leaves one prescribed
nonsingleton residual `C`, forcing `M cap B=C`, or is fully dissolved, in
which case `M cap B` may be empty or a singleton.  These missing-set events
are disjoint and give the exact kernel.  The positivity condition is exactly
`r=0=t` or `1<=r<=t`, where `r=n-|M|`.  The independent target-by-target
check confirms the formula and both eventual and exact-time reachability at
`t=0,...,5`.

Finally, an output singleton `i` came either from the unchanged target or by
merging `{i}` into one of the other target blocks.  Forgetting `i` identifies
the two actions associated with merging a pair of output singletons.  This
gives

```text
distinct sources = 1+s(b-s)+binom(s,2),
labelled (source,i) pairs = s b,
```

with both quantities zero when `s=0` except that the first formula is not
invoked.  The `n=1` state has one source and one labelled action, as stated.

## 3. Findings

### Critical

None.

### Major

None.  I found no false formula, omitted target type, failure of simultaneous
diagonalization, or boundary counterexample.

### P179-A-m01 — The domain `n>=1` is used but never stated at the definition

**Severity:** Minor.  **Location:** `main.tex`, lines 52–58.

The displayed transition operator divides by `n`.  The final paragraph
handles `n=1`, so the intended domain is clear, but no sentence actually
fixes `n>=1`; under the usual convention `[0]=empty`, the displayed chain is
undefined.  This is a literal-map boundary, not a mathematical failure for
the intended family.

**Mandatory repair:** change the opening to “Fix an integer `n>=1`” (or an
equivalent explicit domain statement).  Keep the existing `n=1` paragraph.

### P179-A-m02 — The closest internal partition dynamics are absent from the paper-local subtraction ledger

**Severity:** Minor.  **Locations:** `main.tex`, lines 61–73;
`SOURCE_VERIFICATION.md`, lines 1–18.

The sequence-level firewall correctly distinguishes P179, but neither
paper-local surface records the comparison.  At minimum, the audit should
subtract P169 (same labelled set-partition carrier, but deterministic
successor transfer preserving block number and supporting nontrivial
cycles) and P110 (deterministic cyclic shift-and-join/coarsening rather than
random singleton refinement).  Their literal maps do not collide, and
neither transfers the all-but-one coupon kernel or the two predecessor
notions.  The issue is traceability: a reader of the paper package alone
cannot see that the same-carrier internal systems were checked.

**Mandatory repair:** add a compact paper-local internal-collision paragraph
or table to `SOURCE_VERIFICATION.md` and synchronize the contribution
boundary in the manuscript/support ledger.  Assign all generic monotone
partition/refinement and spectral shell credit to background.  Do not turn
the noncollision into novelty language.

## 4. Primary-source and owner audit

The primary EJC article by Knopfmacher, Mansour, and Wagner explicitly uses
the marked-element operation “remove the marked element from its block and
make it form a singleton block” in its bijection, so the manuscript's zero-
credit assignment is accurate.  Brown's paper owns generic diagonalization
and multiplicity technology for semigroup walks, not this exact temporal
kernel.  Stark's partition-generating chains are different in direction and
state construction.  A fresh search also surfaced generic partition-
refinement implementations and nearby partition MCMC moves, but no inspected
primary record stated the literal repeated isolation chain with this theorem
conjunction.

That is only a bounded non-hit.  `OWNER_AMBER / HOLD_EXTERNAL` remains the
correct ceiling.  In particular, the complete spectrum is a short
consequence of commuting idempotents and triangularity and cannot carry
independent ownership weight after Brown is subtracted.

## 5. Claims/evidence, LaTeX, anonymity, and artifacts

- Every listed theorem has a deductive proof and the author ledger correctly
  labels finite enumeration as pressure rather than proof.
- The settled log is clean; first-pass undefined-reference messages are
  normal and are absent from the settled pass.  This review did not compile.
- The visible author is Anonymous and PDF title/author/creator/producer
  metadata are blank.
- At the original Round-0 baseline, `main.pdf` and
  `main_round0_original.pdf` were byte-identical, three pages, SHA-256
  `c0a97f79c22799e90b3c2bd95d0060b4b75b38b28536332e5d60fe38f2a5f923`.
- At that baseline the paper directory had no paper-local `SHA256SUMS`.
  This was an artifact-hardening recommendation rather than a theorem
  finding; later lifecycle rounds added a non-self-referential manifest.

## 6. Kill switches and disposition

Withdraw or kill if a direct owner of the literal chain/conjunction appears,
if the missing-set events cease to be disjoint under a changed update, or if
the action-pair count is presented as a distinct-state count.  None occurs in
the frozen Round-0 manuscript.  After the two minor traceability repairs,
the theorem package is acceptable for the next internal round, still under
`HOLD_EXTERNAL`.

**Reviewer assertions:** 120,977.  **Canonical replay:** byte-identical twice.

## Round-1 delta disposition — accepted

The repaired source at SHA-256
`cb7886a6846a4a8019c6636f77bbe9faa5cd8fbc342bbde6c822d57286938b7b`
and PDF at
`9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d`
close P179-A-m01 and P179-A-m02. The explicit `n>=1` boundary, retained
`n=1` evaluation, P169/P110 subtraction, zero-credit language, owner ceiling,
Round-1 receipts, anonymity, and `17/17` paper manifest all pass. Two new
fresh-process Reviewer-A replays again matched the canonical at 120,977
assertions each; the author control matched at 125,118 assertions.

**Delta decision:** `ROUND1_DELTA_ACCEPT / THEOREM_ACCEPT / HOLD_EXTERNAL`.  
**Post-delta open findings:** `0 Critical / 0 Major / 0 Minor`.

The original verdict above is retained as the historical Round-0 review;
the formal evidence ledger is `DELTA_ACCEPTANCE_TEMPLATE.md`.

## Round-2 science re-entry disposition — accepted

A late science audit correctly observed that the Round-1 support lemma, and
the corresponding sentence in this review's original re-derivation, omitted
an unselected residual of size one.  The intended and now literal rule is:
inside every old block, selected labels become singleton blocks and the
unselected residual remains one block whenever it is nonempty, including
when it is itself a singleton.

The final corrected source is SHA-256
`94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6`;
the Round-2/live PDF is
`6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`.
Lines 89--105 now state and prove the nonempty-residual rule without the
former prose defect.  The correction is consistent with every downstream
formula: absorption permits at most one missing label in each old block,
while the every-target kernel puts empty and singleton residuals in its
discrete-output alternative and reserves its other alternative for a
nonsingleton residual.  The spectrum and inverse census are unchanged.

The author added an exhaustive literal-versus-block-formula oracle through
`n=7`, contributing 127,202 assertions and raising its replay total to
252,320.  Two new fresh-process runs of the independent bit-block Reviewer-A
control each again matched `CANONICAL.txt` byte-for-byte at 120,977
assertions.  The final PDF contains the corrected statement, is byte-identical
to `main_round2.pdf`, and retains blank identifying metadata.  The refreshed
paper-local manifest verifies all 18/18 non-self-listed artifacts.

**Round-2 decision:**
`ROUND2_SCIENCE_REENTRY_ACCEPT / THEOREM_ACCEPT / HOLD_EXTERNAL`.  
**Current open findings:** `0 Critical / 0 Major / 0 Minor`.
