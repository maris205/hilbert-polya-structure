# Hostile Review B — P117

## Review identity and provisional verdict

Role: independent nonauthor Reviewer B. I reconstructed the manuscript from
`main.tex`, the compiled PDF, the bibliography, all support documents, and
the verifier. I did not read or use Review A.

**Provisional verdict: `GO_INTERNAL_AFTER_REPAIR`. External status remains
`HOLD`.**

The two sharp clocks survive hostile reconstruction, and I found no direct
temporal owner in the bounded search. There is, however, one false lemma as
stated: the converse realization claim in Lemma 5.2 omits the necessary
even-length condition on the boundary-parity word. The smallest
counterexample is one symbol. This is a mandatory mathematical repair, but
all uses in Theorem 5.4 already involve even-length words, so it does not
invalidate the advertised maximum-preperiod formula.

## Package and independence boundary

Reviewed without consulting any hostile-review file:

- `main.tex`, `main.pdf`, and `main_round0_original.pdf`;
- `references.bib` and `figures/table_exact_counts.tex`;
- `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`,
  `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`, and `BUILD.md`; and
- `code/verify.py` and `code/verification_output.txt`.

No manuscript, bibliography, verifier, support document, PDF, shared ledger,
or Git state was changed in this review.

## Independent reconstruction of the theorem chain

1. For a nonconstant cyclic word, every old run receives one uniform flip
   decision. Hence no boundary can be born. At a boundary separating lengths
   `a,b`, the endpoint bits remain unequal exactly when `a` and `b` have the
   same parity.
2. Boundary inclusion is monotone. A recurrent orbit can therefore lose no
   boundary; equal incident parities propagate around the run cycle. All-even
   runs are fixed and all-odd runs are complemented each step, giving exact
   period two. Conversely these states are recurrent.
3. At odd circumference, neither an all-even cyclic composition nor an even
   number of odd parts can sum to an odd integer. Thus only the two constant
   states recur, as a two-cycle. At circumference `2m`, even boundary gaps
   give `2^(m+1)-2` fixed states, and positive odd cyclic compositions give
   the displayed exact-period-two sum. The zeta product then follows
   routinely.
4. If `n=2t+1`, a nonrecurrent round deletes an even positive number of
   boundaries, hence at least two. There are at most `n-1` boundaries. The
   composition with one part `2` and `2t-1` singleton parts absorbs the two
   adjacent singletons per round and attains depth `t`.
5. For even `n`, write the surviving boundary sites in cyclic order and mark
   their site parities by `q_i`. The parity of the intervening gap is
   `q_i+q_(i+1)`, so the boundary at `i` survives precisely when
   `q_(i-1)=q_(i+1)`. This is the stated subsequence eroder `D`.
6. For a realizable nonempty `q`, an unequal adjacent pair costs at least one
   site and an equal pair at least two, giving
   `C(q)=|q|+e(q)`. For **even** `|q|`, choosing all gaps at these minima
   realizes `q`, and adding two to a gap preserves all boundary parities.
7. Decomposing `q` into constant runs shows that each nonsingleton run loses
   two endpoints. With the empty-word transition convention made explicit,
   the manuscript's estimate gives `C(Dq)<=C(q)-4` for every mixed
   even-length `q`.
8. Every last mixed parity word costs at least six, so a depth-`t` orbit costs
   at least `6+4(t-1)=4t+2`. The family `q=0^(2t+1)1` has cost `4t+2`, loses
   the two zero endpoints each round, and reaches `01` after exactly `t`
   rounds. Minimal realization and one `+2` gap extension cover respectively
   `n=4t+2` and `n=4t+4`.

This reconstruction confirms the main sharp formula after the local repair
to Lemma 5.2.

## Severity-ranked findings

### CRITICAL

None.

### MAJOR (mathematics)

#### M1. Lemma 5.2 has a false unrestricted converse

The lemma begins with an arbitrary nonempty cyclic binary word `q` and says
conversely that `q` is realizable at circumference `C(q)` and every
`C(q)+2j`. A nonconstant cyclic binary word, however, has an even number of
run boundaries. Therefore a boundary-parity word of odd length is never
realizable.

The smallest counterexample is

```text
q=(0),  e(q)=1,  C(q)=2.
```

There is no binary cyclic word with exactly one boundary. The proof's last
sentence tacitly uses the missing hypothesis when it says alternating bit
values can be assigned consistently.

**Required repair.** Restrict the converse, and preferably the entire lemma,
to nonempty cyclic words of even length. State separately that every actual
boundary-parity word has even length. No downstream estimate changes:
Theorem 5.4 starts from actual boundary words, and its sharp family
`0^(2t+1)1` has length `2t+2`.

#### M2. The cost-drop proof needs an empty-word transition convention

For `q=0011`, every symbol is deleted and `Dq` is empty. The proof of Lemma
5.3 nevertheless introduces `s'` as the transition count of `Dq` without
defining the transition count of the empty cyclic word. The desired
inequality is true (`C(q)=6`, `C(Dq)=0`), but the written calculation has an
undefined intermediate quantity.

**Required repair.** Define `s(empty)=0` before the calculation, or split off
the case `Dq=empty`. This repair should be made together with M1 so the
realizable, empty, constant, alternating, and mixed domains are disjoint and
explicit.

### MAJOR (owner/scope)

None found in the bounded audit. This is not a novelty certificate.

The cited shrinking-cell papers concern models in which cells are literally
deleted and surviving cells become adjacent; they do not supply this
specified bit-flip map, its site-parity factor, or the two sharp clocks:

- [Rosenfeld--Wu--Dubitzki, 1983](https://doi.org/10.1016/0020-0255(83)90045-2);
- [Modanese--Worsch, 2016](https://doi.org/10.1007/978-3-319-39300-1_13);
- [Kutrib--Malcher--Wendlandt, 2017](https://doi.org/10.1007/s11047-016-9588-8).

The 2026 run-enumeration neighbor is static and composition-based, not a
temporal owner: [Balado--Silvestre, arXiv:2602.10005](https://arxiv.org/abs/2602.10005).
Searches through 2025--2026 using “odd-run reversal,” “flip every odd run,”
“odd-length blocks,” “run parity cellular automaton,” and the literal eroder
condition did not expose a direct source. That statement records only a
bounded no-hit and must not be upgraded to novelty or priority.

### MINOR

#### m1. The canonical verifier does not test the claimed local controls

The manuscript says the verifier “compares literal updates with run data,”
and `CLAIMS_EVIDENCE.md` lists a direct boundary-survival control. In fact,
`code/verify.py` checks period type, the recurrent/equal-parity equivalence,
the census, global maximum depths, and one extremal witness. It never asserts
the one-step boundary-survival identity, the `q -> Dq` factor, minimal
realization, or the four-unit cost drop.

This does not weaken the proofs, but it overstates the control suite.

**Repair.** Either add exact local assertions for those identities or narrow
the prose in `main.tex` and `CLAIMS_EVIDENCE.md`. An independent review-only
enumeration checked the eroder and realization/cost claims for every even
`|q|<=18`, and literal boundary updates for every even circumference
`n<=14`, executing 2,118,938 assertions after imposing even length.

#### m2. Table 1 floats between Theorem 3.1 and its proof

In the six-page PDF, Theorem 3.1 begins at the bottom of page 2; Table 1 is at
the top of page 3; only then does the theorem's proof begin. This is readable
but needlessly interrupts the theorem/proof unit.

**Repair.** Pin the table after Corollary 3.2 or otherwise prevent it from
floating between a theorem statement and its proof.

#### m3. `BUILD.md` is not a settled build record

It says the settled result and warning counts “are filled after compilation,”
but they are not filled even though a settled PDF is committed. Update the
record during repair; do not infer a mathematical issue from this omission.

## Fresh verification and build audit

### Canonical verifier

Commands run from the paper directory:

```bash
cmp -s <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py) \
  code/verification_output.txt
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
wc -c code/verification_output.txt
```

Results:

- fresh run: `PASS`;
- exact assertions reported: `262188`;
- exhaustive orders: `1..16`;
- byte comparison exit status: `0`;
- canonical stdout size: `343` bytes.

The asserted maximum depths and recurrent counts agree with the theorem
formulas through order sixteen. The verifier's local-identity coverage is
limited as noted in m1.

### Isolated build and PDF inspection

I copied only `main.tex`, `references.bib`, and the table source to a fresh
directory under `/tmp`, then ran:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Results:

- six A4 pages, `320849` bytes, PDF 1.5;
- isolated PDF byte-for-byte equal to the stored `main.pdf`;
- no settled LaTeX/BibTeX warning, undefined reference/citation, box warning,
  or rerun request;
- 23 font rows, all embedded, subset, and Unicode mapped;
- empty Author metadata, no form, no JavaScript, and no encryption; and
- all six rendered pages visually inspected: no clipping, collision, missing
  glyph, or unreadable formula. The sole layout objection is m2.

## Sharp-witness and boundary audit details

- Odd witness: after `j` rounds the unique even run has absorbed exactly
  `2j` singleton runs. Two boundaries disappear each time, including the
  final two-boundary step. The edge case `n=1` has depth zero.
- Even witness: `q=0^(2t+1)1` has even length, `e(q)=2t`, and cost `4t+2`.
  Each eroder round replaces the zero exponent by two less; the first
  recurrent factor is `01` at time `t`. Adding two to one realizing gap does
  not alter `q` or its future eroder sequence.
- Small even cases: at `n=2,4`, every realizable boundary factor is already
  empty, constant, or alternating; maximum depth zero is correct.
- Empty deletion: patterns such as `0011` show why `Dq=empty` must be handled
  explicitly, but they satisfy the cost inequality with room to spare.

## Required repair checklist

1. Add the even-length hypothesis to Lemma 5.2's converse and explain why it
   is automatic for actual boundary words.
2. Define transition count and cost conventions when `Dq` is empty, or split
   that case out of Lemma 5.3.
3. Either add direct eroder/cost assertions to the verifier or narrow the
   stated computational coverage.
4. Keep Table 1 out of the middle of Theorem 3.1 and its proof.
5. Settle `BUILD.md` after the repair build.
6. Preserve the present owner language: all searches bounded, all classical
   mechanisms zero-credit, and external dissemination `HOLD`.

After items 1--2 are implemented and the build/control prose is synchronized,
the manuscript is suitable for the next internal gate. It is not cleared for
external release.

## Round-one follow-up

I independently re-read the round-one source, support documents, verifier,
and stored round-one PDF.  This is a repair audit of the A/B objections, not
new author work and not a renewed priority claim.

### Resolution of the requested items

1. **RESOLVED---even-length converse.**  Lemma 5.2 now states the converse
   only for nonempty cyclic binary words of even length, explains that actual
   boundary words have even length, and treats the empty word separately.
   Thus the former false converse no longer admits odd-length parity words.
2. **RESOLVED---the transition when `Dq` is empty.**  Lemma 5.3 now
   explicitly assigns transition count zero to the empty word.  The strict
   cost-drop statement and its proof therefore have a defined terminal case.
3. **RESOLVED---the odd witness's final collapse.**  The sharpness proof now
   distinguishes the first `t-1` three-run mergers from the final
   two-boundary collapse of the remaining composition `(2t,1)`, with the
   case `t=1` stated separately.  It no longer describes the final step as
   another three-run merger.
4. **RESOLVED---computational-control overstatement.**  The verifier now
   checks the boundary-survival identity on every labelled word through
   order 16, checks the parity-eroder identity on every nonconstant
   even-order word in that range, and separately checks realization and
   cost drop on all 349,524 even parity words of lengths 2, 4, ..., 18
   (including 349,488 mixed words for the strict cost test).  Section 6,
   `CONTROL_RESULTS.md`, and `CLAIMS_EVIDENCE.md` describe that coverage
   rather than attributing unimplemented local checks to the old census-only
   loop.
5. **RESOLVED---table placement.**  The exact-count table is now fixed after
   the proof of Theorem 3.1 and Corollary 3.2 and before Section 4; it no
   longer floats between the theorem statement and proof.  This was also
   confirmed on rendered page 3.
6. **RESOLVED---residual wording.**  The conclusion and narrative/evidence
   documents explicitly call the labelled census a routine enumerative
   corollary once the temporal classification is known.  The claimed
   residual is limited to the boundary-survival law, complete recurrence
   classification, and the two sharp stabilization clocks.  Classical
   mechanisms remain zero-credit, owner searches remain bounded, and no
   priority or novelty claim has been introduced.
7. **RESOLVED---build record.**  `BUILD.md` now records the round-one
   four-stage isolated build, verifier result, bibliography closure,
   diagnostics, fonts, metadata, and the A/B repairs.  Its reported PDF and
   control data agree with my fresh checks.

There are **no unresolved A/B repair items** in the requested scope.

### Fresh control and artifact checks

I reran `PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py` and compared its
stdout byte-for-byte with `code/verification_output.txt`.  The run passed,
the comparison returned zero, and the exact total is **1,529,158
assertions**.  Its auditable decomposition is

\[
3(131070)+87364+3(16)+2(349524)+349488=1529158.
\]

I also rebuilt from only the round-one source, bibliography, and table in a
fresh temporary directory using LaTeX--BibTeX--LaTeX--LaTeX.  The resulting
PDF is byte-for-byte equal to both `main_round1.pdf` and `main.pdf`: six A4
pages, 321,439 bytes, with no settled LaTeX/BibTeX warning, undefined
reference or citation, box warning, or rerun request.  All 23 font rows are
embedded, subset, and Unicode mapped.  The PDF has empty Author metadata and
no form, JavaScript, or encryption.  Text extraction found no draft marker,
placeholder, or unresolved token.  Visual inspection of all six pages found
no clipping, collision, missing glyph, or table-placement regression.

### Final verdict

**`GO_INTERNAL`.**  Round one resolves every actionable mathematical,
control, layout, wording, and build objection raised in Reviews A and B.
This verdict clears only the repaired manuscript for the next internal
gate.  External dissemination remains **`HOLD`**, and the bounded owner
subtraction must not be restated as a priority result.
