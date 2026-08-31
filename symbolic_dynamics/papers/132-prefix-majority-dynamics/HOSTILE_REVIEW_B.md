# Hostile Review B — synchronous prefix-majority dynamics

**Review date:** 2026-09-01  
**Review posture:** independent definition-level reconstruction of the current
round-one package  
**Mathematical verdict:** **`GO`**  
**External-release verdict:** **`HOLD_EXTERNAL`**

## Severity ledger

- **Critical:** 0
- **Major:** 0
- **Minor:** 1

The theorem package is mathematically ready for continued internal use.  The
only Round-B finding is a false SHA-256 value in the build/provenance record;
the frozen PDF itself has not changed.  External release remains on hold
because the owner search is deliberately bounded and a non-hit is not novelty
evidence.

## Artifacts reviewed

I read the current manuscript and bibliography, all planning/evidence/control
documents, the full paper-local verifier and frozen raw stdout, Hostile Review
A and its improvement log, both frozen PDFs, the live build log, and the
round-zero/round-one build record.

Current hashes are:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `a26bee914dd2909c825a7c1d3e2a012c09b2def816b14db85ab27c40b60bddaf` |
| `references.bib` | `37af8e3aec5558199966d428bcd4a136dc3612da82318c9d7221c57df280313a` |
| `code/verify.py` | `50ff5f13d47c01b679a9158f79ce5aa20333f43c374d133c31ff46712882604d` |
| `code/verification_output.txt` | `f52d769cd0831772458e700db189722bf745b8e74c4aca2c3539dcfea8a0f442` |
| `main.pdf` | `dcfd7eddb0cb85a197f0ae875af97fd353f50070317ca4ec6f8de0ad5a74527e` |
| `main_round1.pdf` | `dcfd7eddb0cb85a197f0ae875af97fd353f50070317ca4ec6f8de0ad5a74527e` |
| `main_round0_original.pdf` | `f6329905059f20811380dcfe1163d9cd908a592e428a358ec1f9461d55140679` |

Byte comparisons give

```text
cmp(main.pdf, main_round1.pdf)          = 0
cmp(main.pdf, main_round0_original.pdf) = 1
```

This is the expected artifact topology: the live PDF is round one, while the
round-zero PDF remains the pre-repair draft.

## Fresh exact-control replay

I replayed the verifier directly from the current package without creating
bytecode:

```bash
PYTHONDONTWRITEBYTECODE=1 bash -c \
  'cmp -s code/verification_output.txt <(python3 code/verify.py)'
```

The exit status was **0**.  The replay therefore reproduced the raw canonical
stdout byte for byte.  Its frozen totals are:

```text
TOTAL_STATES=131070
TARGET_CELLS=131070
LARGE_SHARP_WITNESSES=10
ASSERTIONS=524452
STATUS=PASS
```

As a separate attack, I used an independently written literal update/orbit and
walk-count implementation, rather than importing the paper verifier.  It
exhausted all words and all targets for `1 <= n <= 14` and reproduced the
fixed sets, periods, maximum depths, complete target-wise fibre formula,
Fibonacci image sizes, and maximizing targets.  It ended in
`INDEPENDENT_LITERAL_P132=PASS`.  Neither finite run is used as an all-length
proof.

## Definition-level reconstruction

### 1. Literal map, closure, and the weak-tie boundary

For `w in {0,1}^n`, replace each letter by the increment `x_i=2w_i-1` and put
`S_i=sum_{j<=i}x_j`.  The map is exactly

```text
P_n(w)_i = 1{S_i >= 0}.
```

It is therefore a self-map of the binary carrier.  The inequality is weak at
zero; this convention is used consistently in the fixed-point proof, the
walk decomposition, the constant fibres, and the verifier.

### 2. Fixed language and recurrent set

At a balance at least one, a source zero would still be reported as one and
cannot occur in a fixed word.  At a balance at most minus two, the dual
argument forces zeros.  From balances zero and minus one, the only way to
avoid entering a constant tail is the alternating return

```text
0 --(source 0)--> -1 --(source 1)--> 0.
```

Thus the fixed words are exactly

```text
(01)^r 0^(n-2r),  0 <= r <= floor(n/2),
(01)^r 1^(n-2r),  0 <= r <= floor((n-1)/2).
```

The ranges are disjoint and give `n+1` words.  The later stabilization theorem
puts every orbit into this set, so no nontrivial cycle remains.  Consequently
every iterate has the same `n+1` fixed points and the stated finite dynamical
zeta function `(1-z)^(-(n+1))` follows.

### 3. Sharp stabilization clock

Every nonfixed word has a longest fixed prefix.  Such a prefix cannot end at
balance zero, since either following bit would extend it.  It therefore has an
alternating core and a nonempty constant tail.  A zero-tail has length at
least two.

If the tail length is `ell`, one update preserves at least `2ell` tail letters
on the one branch and at least `2ell-1` on the zero branch.  Hence, while an
orbit remains nonfixed,

```text
one branch:  ell_t >= 2^t ell_0,
zero branch: ell_t - 1 >= 2^t(ell_0 - 1).
```

Taking `2^t >= n` forces the fixed prefix to fill the word, giving the global
upper bound `ceil(log_2 n)`.  For sharpness, direct prefix-balance calculation
gives the all-parameter identity

```text
W_a = 1^a 0^(n-a),
P_n(W_a) = W_min(2a,n).
```

Starting from `W_1` first reaches `1^n` after exactly `ceil(log_2 n)` updates.
This includes `n=1`, where `W_1` is fixed and the depth is zero.

The first small boundaries independently reconstruct as follows:

| `n` | fixed states | image size | maximum depth | maximum fibre |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 0 | 1, with both targets tied |
| 2 | 3 | 3 | 1 | 2, uniquely at `1^2` |
| 3 | 4 | 5 | 2 | 3, uniquely at `1^3` |

### 4. Complete fibre formula

The target records whether a simple walk is in the nonnegative or negative
half-line at every positive time.  A change `1 -> 0` forces the edge
`0 -> -1`; a change `0 -> 1` forces `-1 -> 0`.  Cutting at these edges is a
bijection, not merely a counting analogy.

For a target with alternating runs
`b_1^(ell_1)...b_s^(ell_s)`:

- if `s=1`, the all-one fibre is the set of length-`n` nonnegative meanders,
  of size `M_n`, and the all-zero fibre has its first down-step forced, of
  size `M_(n-1)`;
- if `s>=2`, a first positive run is a nonnegative excursion and must have
  even length, contributing `C_(ell_1/2)`;
- a first negative run has a forced first down-step and final up-crossing,
  so it has odd length and contributes `C_((ell_1-1)/2)`;
- every interior run is a crossing step plus an excursion, hence must have
  odd length and contributes `C_((ell_j-1)/2)`; and
- after the crossing into the last run, the remaining `ell_s-1` steps form an
  unrestricted half-line meander, contributing `M_(ell_s-1)`.

Concatenation reverses the cut uniquely.  This proves both the zero-fibre
parity criterion and the displayed product for **every** target, including the
empty product when `s=2`.

### 5. Image and fibre extremum

The admissible run language has generating function

```text
2L + (E+O)L/(1-O) = (2z+z^2)/(1-z-z^2),
L=z/(1-z), O=z/(1-z^2), E=z^2/(1-z^2).
```

Its coefficient is `F_(n+2)`, so the image formula follows from the proven
parity language.

For a source walk `S` in a fixed target fibre, `R_i=|S_i|` is a nonnegative
meander.  The target signs recover `S` from `R`, making this map injective.  A
nonconstant target forces a positive-time visit of `R` to zero and therefore
misses the all-up meander.  The all-zero fibre has
`M_(n-1)<M_n` for `n>=2`.  Thus `1^n` is the unique maximizing target for
`n>=2`, with size `M_n=binom(n,floor(n/2))`; both targets tie only at `n=1`.

No step in this reconstruction appeals to the finite census.

## Review-A closure

The three manuscript repairs are closed:

- **A132-1 closed:** the fixed-language exponents are now literally
  `0^{n-2r}` and `1^{n-2r}`.
- **A132-2 closed:** the constant-fibre display now contains `\qquad`, not the
  printed word `qquad`.
- **A132-3 closed:** the abstract now claims precisely the recurrent set,
  sharp global stabilization, and target-wise one-step fibres; it no longer
  says “complete finite dynamics.”

**A132-4 is mathematically closed but has one documentary residue.**  The
round-zero file was preserved, round one was frozen separately, and the live
PDF is byte-identical to round one.  However, the build record contains the
wrong hash described below.

## Finding B132-1 — incorrect round-zero hash in `BUILD.md`

**Severity:** minor, mandatory provenance repair.

`BUILD.md` records the immutable round-zero SHA-256 as

```text
f6329905059f6e632162fc71d95996d88f08f18e342ee098659639160a6a2013
```

but a fresh hash of the actual `main_round0_original.pdf` is

```text
f6329905059f20811380dcfe1163d9cd908a592e428a358ec1f9461d55140679
```

The correct value is also the one preserved in Hostile Review A.  The file is
326,793 bytes and has not been silently replaced; this is a record typo, not
an artifact-integrity failure.  Correct the build record and recheck the hash.
Do not overwrite the round-zero PDF.

## Build and artifact audit

The round-one `main.tex` hash, current/round-one PDF hash, byte size, and
three-page A4 description in `BUILD.md` all agree with the live files.  The
current PDF is 326,101 bytes, has blank identifying metadata, and reports 25
font rows, all embedded, subsetted, and Unicode-capable.  Text extraction
succeeds.  The settled LaTeX/BibTeX logs contain no error, undefined
citation/reference, bad-box warning, or rerun request.

A text comparison of round zero and round one shows the expected Review-A
changes: corrected abstract scope, corrected fixed-word exponents, corrected
`\qquad`, and the earlier bibliography-author repair, with pagination shifts
caused by the revised abstract.  No unrecorded theorem change was found.

## Owner boundary

The official SIAM record for Husfeldt--Rauhe assigns prior ownership to the
dynamic partial-sum/prefix-majority query family and explicitly includes
maintaining prefix-majority information:
[SIAM Journal on Computing](https://epubs.siam.org/doi/10.1137/S0097539701391592).
That justifies subtracting the coordinate predicate and its one-step batched
evaluation.  Catalan/ballot/reflection enumeration, meanders, sign persistence,
Fibonacci regular languages, and generic majority-network terminology are
also correctly treated as background.

The residual internal contract is narrower: feed the entire weak-prefix-sign
vector back into the same map, then classify its recurrence, sharp clock, and
target-wise inverse geometry.  Literal/equivalent-map searches did not locate
this exact feedback system, but a search non-hit cannot establish novelty,
priority, or clearance.  `HOLD_EXTERNAL` is therefore the correct release
verdict.

## Final Round-B disposition

**GO** for internal theorem use and the next controlled manuscript round.
Correct B132-1 in the provenance document before calling the package
mechanically final.  **HOLD_EXTERNAL** remains in force independently of that
minor repair.

## Closure addendum — 2026-09-01

I independently rechecked the sole Round-B finding after its reported repair.
No manuscript, verifier, canonical stdout, bibliography, or PDF change was
needed for this documentary correction.

### B132-1 closure evidence

- A fresh `sha256sum main_round0_original.pdf` returns
  `f6329905059f20811380dcfe1163d9cd908a592e428a358ec1f9461d55140679`.
- `BUILD.md` now records that exact 64-hex digest; the erroneous
  `f632990...6e632...` transcription is absent.
- The preserved round-zero file therefore agrees with Hostile Review A, this
  review's original evidence table, and the corrected build ledger.
- `main.pdf` and `main_round2.pdf` both have SHA-256
  `dcfd7eddb0cb85a197f0ae875af97fd353f50070317ca4ec6f8de0ad5a74527e`,
  and a fresh byte comparison gives `cmp=0`.
- `main_round1.pdf` has the same digest, as expected because B132-1 changed no
  compiled source or PDF byte.  The round-zero digest remains distinct.
- A fresh paper-local verifier replay still reproduces
  `code/verification_output.txt` byte for byte (`cmp=0`).

**B132-1 is CLOSED.**  The correction is a provenance-only repair and does not
alter any theorem or evidence contract.

### Final post-closure ledger and verdict

- **Critical:** 0
- **Major:** 0
- **Unresolved minor:** 0
- **Internal verdict:** **`GO_INTERNAL`**
- **External verdict:** **`HOLD_EXTERNAL`**

This addendum supersedes only the earlier instruction to repair B132-1; all
mathematical and owner-boundary conclusions of the main Round-B review remain
unchanged.
