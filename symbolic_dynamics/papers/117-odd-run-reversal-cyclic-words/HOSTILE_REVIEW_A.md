# Hostile Review A — P117

Status: independent nonauthor review. External dissemination, novelty,
priority, and submission remain **HOLD**. I reviewed the complete paper-local
package, `main.tex`, the six-page `main.pdf`, the bibliography, the canonical
verifier and transcript, and the supporting claim/control documents. I did
not edit the manuscript or consult another review.

## Provisional verdict

**MAJOR REVISION, with the main theorem package likely correct after local
repairs.** I found no critical counterexample to the recurrence
classification, recurrent census, or either sharp depth formula. The even
four-unit cost drop is sound. The principal formal defect is that the
realization lemma is false on the domain printed in the paper. There is also
a small but real endpoint error in the odd extremal construction and a
verifier-coverage overstatement.

Severity count: **C: 0; M: 2; m: 3.**

## Independent reconstruction

For a nonconstant cyclic word, an old boundary with incident run lengths
`ell_left, ell_right` survives precisely when those lengths have the same
parity. No new boundary can occur inside an old run. Boundary sets therefore
decrease, and a recurrent orbit can lose no boundary. Equal incident
parities then propagate around the cyclic run list. Thus the recurrent words
are exactly the all-even-run fixed words and all-odd-run complement pairs;
constants fit this statement separately.

The census also reconstructs. For `n=2m`, a nonconstant fixed word has a
nonempty even-cardinality boundary subset in one of the two site-parity
classes. The two choices of bit and the two parity classes give
`2^(m+1)-4`, and the two constants give `f_(2m)=2^(m+1)-2`. For exact period
two and `r` even runs, writing each odd part as `2x_i+1` gives
`binom(m+r/2-1,r-1)` ordered compositions. Choosing a labelled boundary and
the following bit and dividing by the word's exactly `r` boundaries gives
the displayed `p_(2m)` formula. Rotationally symmetric words do not upset
this argument because the sites, not necklaces, are labelled.

For odd circumference, every nonrecurrent round deletes a positive even
number of boundaries, hence at least two. For even circumference, the
boundary-site parity word obeys the deletion rule retaining `q_i` iff
`q_(i-1)=q_(i+1)`. With `C(q)=|q|+e(q)`, decomposition into cyclic constant
runs gives exactly two deletions for every nonsingleton run. If `a` is the
number of nonsingleton runs and `h` the number of length-two runs, then
`C(q)-C(Dq) >= 4a-2h`; the `a=1` parity case supplies the missing sharp
argument. I also exhaustively checked all 349,488 mixed even words of even
length at most 18: the minimum drop is four, attained for example by
`0001 -> 01`.

## Critical issues

None found.

## Major issues

### M1 (mathematics): Lemma 5.1 is false without an even-length hypothesis

The cost is defined for every nonempty cyclic binary word `q`, and the
converse in Lemma 5.1 says that `q` is realizable at circumference `C(q)` and
at `C(q)+2j`. A boundary set of a nonconstant cyclic binary word always has
even cardinality. Thus an odd-length `q` is not realizable. The one-symbol
word `q=(0)` is an immediate counterexample: `C(q)=2`, but no binary cyclic
word can have exactly one boundary.

The proof itself invokes even boundary cardinality only in its last sentence;
it does not make an odd-length `q` realizable. The core even-depth theorem
uses only even-length parity words, so this is repairable without changing
that theorem.

Required repair: state the lemma for cyclic `q` of even length (or explicitly
for a word already known to be a boundary-parity word), and treat the empty
boundary word separately. Make the same domain explicit wherever the
converse is invoked.

### M2 (control/evidence): the claimed boundary-transition check is absent

The manuscript and `CLAIMS_EVIDENCE.md` say that the verifier compares the
literal update with run/boundary data through `n=16`. It does not. For each
state, `code/verify.py` asserts only that the eventual period is one or two
and that preperiod zero agrees with equal run parity. The remaining three
assertions per order check the census, maximum depth, and one witness. This
accounts exactly for the reported count

`2 * sum_(n=1)^16 2^n + 3 * 16 = 262188`.

There is no assertion that the new literal boundary set equals the subset
predicted by the survival lemma, and no direct check that the induced parity
word is `Dq` or that its cost drops by four. This does not invalidate the
paper proofs, but it makes the evidence description materially inaccurate.

Required repair: either add direct one-step boundary-survival, `q -> Dq`,
and cost-drop assertions and refresh the canonical count/output, or narrow
the manuscript and claim-map descriptions to the controls actually run.

## Minor issues

### m1 (mathematics): the odd extremal proof mishandles its final round

In the construction with one even run and `2t-1` singleton odd runs, the
claim that “these three runs coalesce into one even run” is correct only
while the two incident odd runs are distinct. At `t=1`, the composition is
`(2,1)`: the same odd run lies on both sides of the even run, and the result
is a constant run of length three, which is odd. More generally, after the
first `t-1` rounds the remaining composition is `(2t,1)`; the final round
removes both boundaries and produces the odd constant run of length
`2t+1`.

The witness and depth remain correct. Required repair: separate the first
`t-1` three-run mergers from the final two-run collapse, including `n=3` as
the smallest instance.

### m2 (owner boundary): separate the temporal delta from static counting

The cited shrinking-automata papers own deletion/shrinking models, and the
2026 Balado--Silvestre paper owns extensive static parity-run enumeration.
The manuscript appropriately assigns those tools zero credit, but its final
residual sentence still lists the labelled census without saying that the
enumeration is a routine consequence once the new recurrent classification
is known. Tighten this sentence so that the defensible temporal residual is
the rule-specific survival/classification and sharp clocks, with the census
presented as their labelled enumerative corollary.

A bounded search using the literal rule, boundary deletion, parity-eroder,
and 2025--2026 formulations found no direct temporal owner. That is only a
bounded non-hit. The nearest primary sources remain
[Rosenfeld--Wu--Dubitzki (1983)](https://doi.org/10.1016/0020-0255(83)90045-2),
[Modanese--Worsch (2016)](https://doi.org/10.1007/978-3-319-39300-1_13),
[Kutrib--Malcher--Wendlandt (2017)](https://doi.org/10.1007/s11047-016-9588-8),
and [Balado--Silvestre (2026)](https://arxiv.org/abs/2602.10005).

### m3 (package record): `BUILD.md` is unfinished

The build record still says that settled results and warning counts “are
filled after compilation,” but no such metrics are filled. The existing PDF
is six clean, legible A4 pages and the settled log I inspected contains no
warning, error, undefined-reference, overfull, or underfull diagnostic. Fill
the record or remove the promise before release.

## Controls and boundary cases

- Fresh canonical verifier: **PASS**, 262,188 assertions, exhaustive
  `n=1,...,16`.
- Fresh stdout versus `code/verification_output.txt`: **byte-identical**.
- `n=1`: both constants form the same two-state complement orbit and every
  state has depth zero, as claimed.
- `n=2,4`: every state is recurrent and the even maximum depth is zero.
- The zeta product correctly uses `p_n/2` primitive two-cycles.
- Six-page visual inspection: no clipped equations, unreadable table, or
  evident layout defect.

## Mandatory resolution before circulation

1. Restrict Lemma 5.1 to even-length realizable boundary words.
2. Repair the final-round wording in the odd sharpness construction.
3. Make the verifier claims match the verifier, preferably by adding the
   missing transition-level assertions.
4. Clarify that static run enumeration is prior and that the census is a
   corollary of the temporal classification.
5. Keep external status **HOLD** pending an independent owner decision.

