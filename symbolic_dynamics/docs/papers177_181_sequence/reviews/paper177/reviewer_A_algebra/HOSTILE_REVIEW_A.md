# Hostile Review A — P177 random projective-hyperplane toggling

**Role:** independent algebra reviewer; no author/scout code imported  
**Frozen author baseline:** `main.tex` SHA-256
`3309beca09a6b0d1502913590906a46804b107385249cb629e2ef744e2c2a763`  
**Original Round-0 decision:** `MAJOR_REPAIR / DO_NOT_KILL / HOLD_EXTERNAL`  
**Round-1 delta disposition:** `ACCEPTED / HOLD_EXTERNAL`  
**Current open findings:** `0 Critical / 0 Major / 0 Minor`

## 1. Scope and independent method

I read the literal update, all five parts of the main theorem, the proof,
author verifier and canonical transcript, claims/evidence ledger, source
verification, plan, self-QA, build ledger, bibliography, PDF metadata, and the
P145/internal collision subtraction.  I did not compile or edit any paper
file.

The review verifier was rewritten from scratch.  It represents vectors and
incidence words as tuples, closes the increment subgroup by breadth-first
addition, partitions the full carrier by tuple-minimal coset representatives,
expands ordered form histories literally, evaluates both TV distances with
`Fraction`, and computes every Walsh eigenvalue directly.  It does not use
the author's bit-mask model, model class, or dynamic-convolution organization.
Two process-separated runs are byte-identical to `CANONICAL.txt`.

## 2. Re-derivation of the theorem spine

For every nonzero form `ell`, the hyperplane word is

```text
h_ell(x) = 1 + ell(x), hence h_ell = 1 + c_ell.
```

The evaluation map `a -> c_a` is injective.  The all-one word is outside the
simplex code when `d>=2`, and differences of two nonzero masks produce every
`c_u`; adjoining any mask then produces `1`.  Thus the increments generate
`W=<1,C>` of dimension `d+1`.  Its cosets are exactly the communicating
classes.  Coordinates `(epsilon,a)` turn addition of `h_ell` into
`(epsilon+1,a+ell)`, which reaches every opposite-side coordinate except the
matched one.  Hence each class is the crown graph of order `2q`, has degree
`N=q-1`, and has period two.

For an ordered word `(ell_1,...,ell_t)`, the endpoint increment is

```text
(t mod 2) 1 + c_L,   L=sum ell_i.
```

Fourier inversion on the additive group gives exactly the two displayed
counts `a_t(0)` and `a_t(L!=0)`.  Subtracting their two probability levels
from uniform on the occupied `q`-point half gives
`1/(q N^(t-1))`.  Comparing instead with uniform on all `2q` component
vertices gives `1/2+1/(2q)` at time one and exactly `1/2` thereafter.  These
are genuinely different TV comparison spaces; the manuscript keeps them
separate correctly.

For a Boolean character indexed by `S`, put
`sigma(S)=sum_(x in S)x`.  Since
`|S cap H_ell| = |S|+ell(sigma(S)) mod 2`, its eigenvalue is
`(-1)^|S|` when `sigma=0` and `(-1)^(|S|+1)/N` otherwise.  The map
`S -> (|S| mod 2,sigma(S))` is onto and every fibre has size
`K=2^(m-d-1)`.  Therefore the full-carrier algebraic multiplicities are
`K,K,NK,NK`.  The complete Walsh basis rules out Jordan blocks.  The
reviewer enumeration confirms all of this through `d=4`, including all
32,768 characters at `d=4`.  At `d=1` the only mask is zero, so the identity
boundary is also correct.

## 3. Findings

### Critical

None.

### P177-A-M01 — The history-existence biconditional is false at two stated times

**Severity:** Major.  **Location:** `main.tex`, Theorem 1(ii), lines 111–124.

The manuscript states for every `t>=0` that a history exists *exactly when*
the unique endpoint parameter `L` exists.  The endpoint condition is
necessary, but it is not sufficient in two boundary cases:

1. At `t=0`, choose `L!=0` and `B=A+c_L`.  The endpoint equation holds with a
   unique `L`, but no zero-step history changes `A`; indeed the displayed
   formula itself gives `a_0(L)=0`.
2. At `t=1`, choose `L=0` and `B=A+1`.  Again the endpoint equation holds,
   but one sampled nonzero form cannot sum to zero; the formula gives
   `a_1(0)=0`.

This is not a failure of the count formula.  It is a false support statement
immediately before a correct formula.  For `d>=2`, the exact replacement is:

```text
endpoint form plus L=0       when t=0;
endpoint form plus L!=0      when t=1;
endpoint form with any L     when t>=2.
```

Equivalently, state that the endpoint equation determines the only possible
`L`, that the number of histories is `a_t(L)`, and that existence means
`a_t(L)>0`.  The proof should explicitly extract the three support cases from
the formula.  The TV statements start at `t=1` and already account for the
zero-mass point, so no TV formula changes.

**Mandatory repair:** revise the theorem biconditional and the adjacent proof
and synchronize the claims/evidence and self-QA wording.  Add both boundary
sentinels to the author regression output.  Failure to repair is a theorem-
statement kill switch.

### P177-A-m01 — Plan cross-references do not match the live theorem numbering

**Severity:** Minor.  **Location:** `PAPER_PLAN.md`, claims matrix lines 21–27.

The live manuscript states the main theorem before the code lemma, so it is
Theorem 1 and the later code result is Lemma 2.  The plan still points to
“Lemma 1; Theorem 2,” and calls the final boundary “Remark 3” although it is
plain section prose.  This does not affect the mathematics, but it weakens
claim-to-evidence traceability.

**Mandatory repair:** replace speculative numbers with stable labels/section
names or synchronize them with the live manuscript.

## 4. Source and ownership audit

The cited primary records support only the zero-credit ingredients assigned
to them: projective/simplex-code terminology, code/design hyperplane
incidence, broad Abelian-walk context, and Brown's left-regular-band and
hyperplane-*chamber* walks.  A fresh literal search did not locate a direct
owner of the projective-hyperplane toggle conjunction.  That non-hit carries
no novelty credit.  The paper correctly separates Brown's chamber state
space from this XOR subset carrier and explicitly subtracts the internal
P145 finite-Abelian/Fourier proof shell.

The owner status must remain `OWNER_AMBER / HOLD_EXTERNAL`.  The residual is
thin: once the augmented-simplex coordinate change is known, the component
walk is the elementary crown walk.  No stronger priority wording is
defensible without a specialist owner search.

## 5. Artifact, anonymity, and status audit

- The settled PDF is four A4 pages; its visible author is Anonymous and its
  title/author/creator/producer metadata fields are blank.
- `main.pdf` and `main_round0_original.pdf` are byte-identical with SHA-256
  `28f719fc52d8a06d61b0425df82f718b4592e736028b3137dc7a0212fe053fec`.
- The paper manifest verifies; the settled log has no unresolved citation or
  reference warning.  No compilation was performed in this review.
- `OWNER_AMBER` and `HOLD_EXTERNAL` are visible in the manuscript and support
  files.  No external-release action is authorized.

## 6. Kill switches and disposition

Immediate kill or withdrawal is required if (a) M01 remains false in the
active theorem, (b) a literal/conjugate owner of the full chain is found, or
(c) the alleged residual is reduced to a routine relabeling of the occupied
P145 system.  None of (b) or (c) was established here.  With the localized
support correction and traceability cleanup, the rest of the theorem may
proceed to delta review unchanged.

**Reviewer assertions:** 36,510.  **Canonical replay:** byte-identical twice.

## 7. Round-1 delta acceptance

I re-read the live repaired package at `main.tex` SHA-256
`fb4cf3eb309e97724a53e037aaf6888881a3f57de6f1e035dc350c7dd40dc06a`
and `main.pdf` SHA-256
`ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c`.
The preserved Round-0 PDF remains distinct, while `main_round1.pdf` is
byte-identical to the live PDF.

- **P177-A-M01 — CLOSED.**  Theorem 1(ii), lines 111--127, now separates
  membership in the parity-compatible endpoint phase from actual history
  existence, requires `a_t(L)>0`, and states the exact support: only `L=0`
  at `t=0`, only `L!=0` at `t=1`, and every `L` for `t>=2`.  Lines 238--251
  derive those cases from the displayed formula.  `CLAIMS_EVIDENCE.md`,
  `SELF_QA.md`, and the author canonical agree, and the author verifier adds
  both zero-count sentinels.
- **P177-A-m01 — CLOSED.**  `PAPER_PLAN.md`, lines 19--27, now uses stable
  main-theorem parts and section labels rather than the stale speculative
  numbering.

The independent reviewer program was rerun in two fresh processes.  Both
runs reproduce `CANONICAL.txt` byte for byte with 36,510 assertions.  The
paper's 16-entry non-self-referential manifest passes 16/16; README, BUILD,
SELF_QA, and IMPROVEMENT_LOG accurately distinguish the immutable Round-0
receipt from the live Round-1 repair and label the author verifier as
author-side evidence.  Visible/PDF anonymity and `OWNER_AMBER /
HOLD_EXTERNAL` remain intact.

**Final Review-A delta verdict:** `0 Critical / 0 Major / 0 Minor open`.
The Round-1 repair is accepted.  This acceptance is not owner clearance and
does not authorize external circulation.
