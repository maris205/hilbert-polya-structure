# Hostile Review B — P177 random projective-hyperplane toggling

**Reviewer process:** root; preliminary Round-0 review, then explicit Round-1
re-entry after Reviewer A's support finding.  
**Reviewed bytes:** Round-1 `main.tex`
`fb4cf3eb309e97724a53e037aaf6888881a3f57de6f1e035dc350c7dd40dc06a`
and PDF
`ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c`.  
**Verdict:** `PROVABLE AS STATED / 0 CRITICAL / 0 MAJOR / 0 MINOR /
HOLD_EXTERNAL`.

## Independent reconstruction

I discarded the author's bit-mask coordinate implementation and rebuilt the
literal chain with tuple vectors and `frozenset` subsets.  Direct products of
form histories, graph search, set-valued hyperplane masks, rational TV, and
fresh Boolean-character sums make **224,874 assertions**.  Two fresh processes
produce `CANONICAL.txt` byte for byte.

The reconstruction confirms:

- the masks generate `W=<1,C>` and the cosets have the stated number/size;
- each support is exactly the claimed bipartite crown and has period two;
- every ordered-history count, including `t=0`, agrees with the two-level
  formula and has a unique endpoint coordinate;
- phase TV and ordinary component-stationary TV are distinct, with the latter
  equal to `1/2+1/(2q)` at `t=1` and `1/2` thereafter;
- the complete full-carrier character multiplicities are `K,K,NK,NK`;
- the `d=1` excluded case is the identity because its only mask is empty.

## Proof audit

The code-coordinate lemma proves injectivity, `1 notin C`, and generation of
both `C` and `1`; no connectivity step is assumed.  Crown coordinates give
both sides and the missing matching explicitly.  Fourier inversion includes
the trivial/nontrivial character sums and covers the zero-time boundary.  The
ordinary-TV proof checks positivity relative to `1/(2q)` only where it is
needed (`d>=2`, `t>=2`).  The spectrum proof exhibits a full character basis,
so algebraic multiplicities and absence of Jordan blocks follow.  The
reconstruction claim is properly restricted to the promised family.

## Round-1 re-entry and findings

The preliminary Round-0 prose review missed the false bare history-existence
biconditional later identified by Reviewer A.  I reopened the actual Round-1
bytes rather than carrying that preliminary verdict forward.  The theorem now
requires `a_t(L)>0`, explicitly gives the `t=0`, `t=1`, and `t>=2` support
cases, and the proof and author verifier contain the corresponding positivity
and zero-count sentinels.  This closes Reviewer A's substantive defect on the
bytes reviewed here.

### `P177-B-M1` — Minor — verifier provenance wording

`BUILD.md` calls the author-created control an “Independent exact verifier,”
and `CLAIMS_EVIDENCE.md` uses “independent dynamic convolution.”  The program
is well separated in representation from the scout, but it is still an
author-side control and is not process-independent review evidence.  Rename
the heading and phrases to `paper-local author-side regression control`, and
reserve `independent` for the present hostile-review implementation.

This wording issue did not weaken any theorem.  It is now closed: `BUILD.md`,
`CLAIMS_EVIDENCE.md`, and the other author surfaces consistently call the
program an author-side regression control.  The live author verifier replays
byte-identically, the paper manifest passes 16/16 entries, and the immutable
Round-0 and Round-1 PDFs are correctly distinguished.

## Source, collision, and release gates

All four bibliography entries resolve to the records stated in the source
ledger.  Code/design, crown, Cayley/Fourier, and generic finite-walk facts are
explicitly zero credit.  The P145 Fourier shell is acknowledged and the
residual is a conjunction, not an ingredient-level originality claim.  No
bounded non-hit is called novelty.  Owner status correctly remains amber;
this review does not authorize release.

## Kill switches reopened

The paper would fail on any direct owner of the literal conjunction, failure
of mask generation, confusion of phase TV with ordinary mixing, a missing
full-carrier multiplicity factor, or extension to `d=1`/nonbinary spaces.
None fires on Round 1.  Two fresh Reviewer-B processes reproduce the
224,874-assertion canonical transcript byte for byte.  There are no open
Reviewer-B findings; the lifecycle remains `HOLD_EXTERNAL`.
