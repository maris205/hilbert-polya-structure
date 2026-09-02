# P152 independent hostile review B

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** fresh internal reader; did not author P152, implement its
Round-1 repairs, or perform Review A.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`.  No manuscript content was sent to an
external model, reviewer, or service.

## Verdict

**REVISE — 0 Critical / 0 Major / 1 Minor.**

The owner-subtracted theorem package survives a fresh derivation.  The literal
signed-edge process has the asserted strongly lumped quotient; the reflected
Bellman elimination, Chebyshev formula, all small and singular cases, quadratic
mean and equality cases, parity law, inverse algebra, and private-block tail
argument are correct.  Both Review-A artifact findings were substantively
repaired.  The expanded verifier replays exactly, a source-only build is
byte-identical to Round 1, and all five rendered pages and PDF integrity checks
pass.

One local quantifier defect remains in the inverse statement.  The theorem
advertises a feasibility test for candidate pairs, but it takes a real square
root before requiring a positive mean (or otherwise defining rejection of a
negative radicand).  The verifier now explicitly rejects a negative-mean
candidate, so source and exact-control semantics are not quite aligned.  This
does not falsify the formula for any genuine nonabsorbing observation and is
therefore Minor, but the candidate-domain boundary must be made literal before
internal acceptance.

This is a raw review.  I did not edit any author source, verifier, transcript,
ledger, bibliography, PDF, or manifest.  This report is the only file added.

## 1. Frozen ceiling and claim-by-claim comparison

I cold-read `FINAL_THEOREM_CONTRACTS.md`, `BTB_FREEZE_CONTRACT.md`, Review A,
`IMPROVEMENT_LOG.md`, `main.tex`, `references.bib`, the complete paper-local
Markdown package, `verify_p152.py`, the frozen transcript, all three retained
PDF names, build products, and the Round-1 manifest.

| Frozen interface | Round-1 source | Review-B result |
|---|---|---|
| established `p=1/3` local-triad kernel, known triangular-book carrier, and active-epoch clock are zero-credit inputs | opening scope and Table 1 | PASS; no model, carrier, XOR, or generic-convergence claim is retained |
| strong count quotient `k -> k-1` with mass `2/3`, `k -> r-k` with mass `1/3` | Theorem 1(i), Section 2 | PASS, including coincident quotient targets |
| complete joint `(T,J)` transform in Chebyshev-rational form | Theorem 1(ii), Section 3 | PASS as a reduced rational-function identity |
| mandatory `r=1`, `r=2`, `z=0`, self-loop, and removable-factor boundaries | equation (6) and transform proof | PASS |
| quadratic mean and all sharp extrema | Theorem 1(iii), Section 4 | PASS, including `r=1` and both odd maximizers |
| parity law and exact feasibility-aware inverse from `(m,q)` | Theorem 1(iv), Section 4 | MATHEMATICS PASS; one candidate-domain wording defect remains (m1) |
| explicit scalar nonidentifiability witnesses | end of parity proof | PASS; both are asserted in the verifier |
| private-block absorption certificate and exponential tail | Theorem 1(v), Section 2 | PASS, including `n=0` |
| no noisy recovery, full-state recovery, nonuniform, arbitrary-graph, all-triad-clock, or friendship-graph extension | theorem aftermath and Limitations | PASS |

The paper remains inside the owner-thin ceiling.  Its value still rests on the
full marked-transform/clock/inverse conjunction; neither the owned kernel nor a
generic finite-chain recurrence is presented as contribution value.

## 2. Fresh mathematical falsification

### 2.1 Literal full-state quotient and clock

For page `i`, write its imbalance bit as the XOR of the common-spine sign and
its two private-edge signs.  A private flip on the selected active page toggles
only that bit, hence clears it and sends the count from `k` to `k-1`.  The
common-spine flip toggles all `r` bits and sends `k` to `r-k`.  The two private
physical choices have total probability `2/3`, and the spine has probability
`1/3`, independently of the representative in a count fibre.  This proves
strong, not merely weak, lumpability.

If `k-1=r-k`, the distinct physical choices enter the same quotient cell and
their masses add.  At `r=2,k=1`, the spine target is the source itself, so the
self-loop used later is genuine.  The manuscript consistently counts only
active imbalanced-triad update epochs; it does not import the no-op holds of
the all-triad clock.

### 2.2 Marked Bellman system and Chebyshev elimination

Marking every epoch by `z` and only a spine flip by `u` gives

```text
F_k=z[(2/3)F_(k-1)+(u/3)F_(r-k)],   F_0=1.
```

For `1<=k<r`, the equations at `k` and `r-k` give

```text
uF_(r-k)=3F_k/z-2F_(k-1),
F_(r-k-1)=3F_(r-k)/(2z)-(u/2)F_k.
```

Only `2z` is divided out, after entering the rational-function field with
`z!=0`; no division by `u` occurs.  Substitution in the equation at `k+1`
gives

```text
F_(k+1)=2 xi F_k-F_(k-1),
xi=[9+z^2(4-u^2)]/(12z).
```

With `F_0=1`, the Chebyshev solution is
`F_k=U_(k-1)(xi)F_1-U_(k-2)(xi)`.  The terminal equation
`F_r=(2z/3)F_(r-1)+zu/3` yields exactly the printed numerator and denominator
for `F_1`.  Thus the transform formula is not inferred from the finite replay.

The exceptional values also survive independently:

- `r=1`: all three choices absorb in one epoch, giving `F_1=z(2+u)/3`;
- `r=2`: `F_1=z[2/3+(u/3)F_1]=2z/(3-zu)`, and the raw common factor
  `3+zu` must be cancelled;
- `z=0`: `xi` is undefined, while the Bellman boundary is `F_0=1` and
  `F_k=0` for `k>0`;
- `u=0` is regular because the proof never divides by `u`.

### 2.3 Mean, extrema, parity, and inverse

The absorption certificate makes the mean finite.  Its Bellman system reduces
to

```text
m_(k+1)-2m_k+m_(k-1)=-1,
m_0=0,  m_r=1+(2/3)m_(r-1),
```

whose unique solution is `m_k=k(r+2-k)/2`.  On `1<=k<=r`, strict concavity,
the endpoint values `(r+1)/2` and `r`, and the vertex `(r+2)/2` give precisely
the printed unique minimum and even/odd maximizing sets.  The one-point
`r=1` domain is correctly separated.

For `h_k=E_k[(-1)^J]`, a spine flip changes the sign and a private flip does
not, so

```text
h_0=1,  h_k=(2/3)h_(k-1)-(1/3)h_(r-k).
```

The bounded affine solution `(r+2-2k)/(r+2)` can be iterated to `T wedge n`;
almost-sure absorption and bounded convergence identify it with the desired
expectation.  Hence `q=P(J odd)=k/(r+2)`.

For a genuine state, putting `R_0=r+2` gives

```text
m=k(R_0-k)/2,
q(1-q)=k(R_0-k)/R_0^2,
2m/[q(1-q)]=R_0^2.
```

The necessity, converse construction `r=R-2,k=qR`, admissible interval, and
uniqueness are all correct.  The central value `q=1/2` is regular.  The two
printed collisions really separate the complementary statistic.  Finding m1
below concerns only the total definition of the feasibility test on arbitrary
candidate input; it is not a counterexample to these identities.

### 2.4 Absorption and the tail quantifier

At every active epoch, the private/spine type is an independent Bernoulli
choice with private mass `2/3`, irrespective of the count.  A pre-generated
run of `r` private types decreases every still-positive count at each performed
update and therefore absorbs within that block.  Conditional on survival to a
block boundary, this event has mass `(2/3)^r`.  Markov iteration gives

```text
P_k(T>nr) <= [1-(2/3)^r]^n
```

for every integer `n>=0`; at `n=0` both sides are one.  This is correctly
positioned as a carrier-specific certificate, not a general triadic-dynamics
convergence theorem.

## 3. Review-A closure

Review A returned 0 Critical / 0 Major / 2 Minor.

1. **Incomplete manifest: substantively closed at Round 1.**  Before this
   report was added, `SHA256SUMS` excluded itself and covered exactly all 27
   other retained files.  `sha256sum -c` passed 27/27, and an independent
   filename count also gave 27.  The protocol requires regeneration after this
   Review-B report and Round-2 artifacts are frozen; that expected new omission
   is not scored as a prior author defect.
2. **Narrow inverse/certificate verifier lane: closed by actual code.**  The
   Round-1 script compares the exact criterion with 7,335 candidate pairs,
   rejects 7,266, exercises twelve explicit rejection inputs, asserts both
   scalar collisions, sums 8,190 exact private/spine word masses, and checks
   546 finite survival inequalities.  The manuscript and ledgers continue to
   call these checks bounded counterexample pressure rather than proof.

## 4. Owner-zero-credit and portfolio attacks

The source boundary remains conservative.  Antal--Krapivsky--Redner own the
local social-balance update and the equiprobable-edge `p=1/3` kernel; Istrate
owns the same general-graph kernel and its triadic-dual/XOR representation;
Istrate--Bonchis--Marin own the generic hypergraph particle-system, drift, and
WalkSAT program; and Sehrawat--Bhattacharjya own the signed triangular-book
carrier and static switching classes.  Bellman/resolvent rationality,
Chebyshev identities, finite-chain tail iteration, and quadratic concavity are
also zero-credit tools.  The paper claims only the boundary-complete law on the
special carrier, and its bounded source non-hit is not described as novelty,
priority, or ownership completeness.

The internal firewall also survives.  P136/S09 deletes edges on a superficially
similar shared-edge carrier; P145 is a stationary vertex-push group walk; P138
is deterministic prefix-XOR feedback; and P151 uses unequal-spider
continuants and leaf tomography.  P153--P156 use unrelated finite-field,
subgroup, and permutation-extraction systems.  P152 is separated by its
literal absorbing sign-flip update and the spine-marked reflected Chebyshev
law, not by generic XOR or first-passage vocabulary.

## 5. Fresh replay and evidence semantics

From a scrubbed process I ran

```bash
env -i PATH="$PATH" LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 \
  python3 verify_p152.py
```

Fresh stdout was byte-identical to `verification_output.txt`, with SHA-256

```text
da908cb14d7825573b0c43870c96155c55b1b40d4d394eef3f1e972071fa1083
```

and terminal profile

```text
assertions=199581
arithmetic=integer_and_Fraction_only
enumeration_is_not_proof=1
external_status=HOLD_EXTERNAL
PASS
```

The assertion total and all table/ledger lane counts agree.  The computation
does not prove the all-`r` rational identity, the inverse iff on arbitrary
exact input, the all-parameter Markov tail, owner completeness, novelty,
priority, or external clearance.

## 6. Source-only build, PDF, and visual inspection

A fresh temporary directory containing only `main.tex` and `references.bib`
completed the declared sequence

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

Its PDF was byte-identical to both `main.pdf` and `main_round1.pdf`:

```text
pages=5
bytes=339258
SHA256=2ac0da7bc87f8ce1fcc8d730eb95a9dd0c79c7bc870f5f7e40a30593bc2f59d9
```

The historical artifact remains unchanged:

```text
main_round0_original.pdf
bytes=338268
SHA256=f2c2476df00d223fdacaf8fb28954d5f620b10611087c3ff35b16ea158f17e57
```

The settled source-only log has no LaTeX/package/pdfTeX warning, unresolved
citation/reference, rerun request, overfull box, underfull box, or build error.
`pdfinfo` reports five A4 pages, no encryption, no form, no JavaScript, no
CreationDate or ModDate, and blank title/author/subject/keyword metadata.  All
25 `pdffonts` rows are embedded, subsetted, and Unicode mapped.  `pdftotext`
contains no path, email address, affiliation, ORCID, acknowledgement,
corresponding-author marker, or nonanonymous identity.

I freshly rasterized and inspected all five Round-1 pages.  The ownership
table, complete theorem, small-boundary display, transform proof, inverse
collisions, expanded audit table, declarations, and bibliography are legible
and inside page bounds.  No clipping, overlap, blank page, corrupt glyph,
unresolved marker, displaced float, or visible identity leak was found.

## 7. Finding and required repair

### m1 — Minor: the candidate inverse test takes an undefined real square root
before closing the mean boundary

**Evidence.**  `main.tex` lines 174--180 say that, given exact candidate
observations `(m,q)`, one first requires only `0<q<1`, then sets

```text
R=sqrt(2m/[q(1-q)])
```

and declares feasibility iff `R` satisfies the integer conditions.  For a
negative candidate mean the real square root is undefined, so this does not
literally define a total iff test on the advertised candidate domain.  The
issue is made concrete by `verify_p152.py` lines 123--140 and 291--307: the
code explicitly rejects a negative-mean candidate before taking an integer
square root, and the Round-1 ledgers advertise that negative-scale rejection
gate.  Thus the mathematical intent and implementation are sound, but the
source omits the corresponding domain clause.

**Required repair.**  Make the theorem's candidate domain explicit before
defining `R`.  The shortest exact repair is to require `m>0` together with
`0<q<1`; equivalently, define candidates with a negative radicand to be
infeasible before taking the principal nonnegative square root.  Carry the same
wording into the proof package and relevant evidence/QA ledgers.  Do not
broaden the theorem to noisy or approximate data.

## 8. Decision

The theorem, owner, collision, replay, build, PDF, and Review-A repair gates
otherwise pass.  Internal acceptance is withheld only for m1 and the mandatory
post-review Round-2/manifest freeze.

**Final Review-B verdict: REVISE — 0 Critical / 0 Major / 1 Minor /
HOLD_EXTERNAL.**
