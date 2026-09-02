# P159 Hostile Review B — independent cold report

**Review date:** 2026-09-02 UTC  
**Input freeze:** current `main.tex`, `main_round1.pdf`, frozen theorem contract,
author evidence package, and immutable `main_round0_original.pdf`  
**External state:** `HOLD_EXTERNAL`  
**Disposition:** **REVISE — 0 Critical / 0 Major / 1 Minor**

This review was performed fresh from the literal dynamics and the frozen
theorem contract.  I did not assume that the author proof, Hostile Review A,
or either verifier was correct.  I re-derived the strict transfer, its matrix
orientation, the fixed/strict temporal split, all mandatory boundaries, and
the resulting image and census formulas before replaying any executable
evidence.  The mathematics and Round-1 PDF survive.  The sole finding is a
contradictory lifecycle sentence in one author-side evidence ledger; it does
not alter a theorem, proof, verifier, or PDF claim.

## 1. Cold theorem reconstruction

Fix a target graph `H` on a particular label set `S`, with `|S|=s`, and a
nonempty deleted set `D` disjoint from `S`, with `|D|=d`.  The target-internal
edges are forced.  The free binary variables are precisely the

```text
sd + binom(d,2)
```

edges meeting `D`.  Requiring every vertex of `S` to be even in the source
and every vertex of `D` to be odd gives the vertex-edge incidence system of
the graph consisting of all free edges.  That graph is connected for every
`d>0`, including the singleton boundary `s=0,d=1`; its binary incidence rank
is therefore `s+d-1`.

The sum of the right-hand side is the target degree sum plus `d`, hence is
`d mod 2`.  The system is consistent exactly when `d` is even.  For positive
even `d`, its nullity is

```text
sd + binom(d,2) - (s+d-1)
  = s(d-1) + binom(d-1,2).
```

Choosing `D` among the `n-s` unused labels proves

```text
B_n(s,s+d)
  = binom(n-s,d) 2^[s(d-1)+binom(d-1,2)]
```

for positive even `d`, and zero otherwise.  The target enters only through a
degree-parity vector whose total is automatically even, so the claimed
target-edge independence is valid.

The degenerate interfaces are also correct.

- At `d=0`, the strict problem is absent.  A same-rank one-step source must
  delete nothing, must be even, and must equal the target.  Thus the full
  diagonal is one exactly for an even target, while the strict matrix has
  zero diagonal.
- At `s=0,d=2` for a fixed deleted pair, its sole possible edge is forced;
  the unique source is `K_2`.  Ambient label choice gives
  `B_n(0,2)=binom(n,2)`.
- At `n=0`, the empty graph is the sole fixed state.  At `n=1`, the empty and
  singleton graphs are fixed.  Both maximum depths are zero.
- At `t=0`, `B_n^0=I`; both temporal-fibre branches are the identity and the
  image is the complete carrier.

## 2. Transfer direction, time fibres, images, and censuses

Rows are targets and columns are sources.  Consequently

```text
(B_n^2)(s,m) = sum_k B_n(s,k) B_n(k,m).
```

The sentinels `B_4(0,2)=6`, `B_4(2,0)=0`, and
`(B_4^2)(0,4)=24` confirm this orientation and reject its transpose.  A
strict predecessor contains a nonempty set of current odd-degree vertices,
so it is non-even and cannot wait.  Target independence supplies the next
strict inverse count uniformly, while determinism makes the intermediate
graph unique.  Matrix powers therefore count literal strict inverse chains,
not merely rank walks.

If `H` is non-even, every one of the `t` transitions ending at `H` must be
strict; any earlier even state would be fixed forever.  Its rank-refined
fibre is consequently `B_n^t(s,m)`.  If `H` is even, the disjoint cases are
first arrival after `j=0,...,t` strict transitions followed by waiting, giving
`(I+B_n+...+B_n^t)(s,m)`.  The manuscript applies the geometric sum only to
even targets.

A non-even rank-`s` target needs `t` positive even reverse rank increments,
so it is in the time-`t` image only if `n-s>=2t`.  Conversely, `t` increments
of two have positive transfer entries, proving sufficiency.  Even targets are
in every image through their fixed self-source.  This proves the displayed
image iff for `t>=1`, with the correct separate identity statement at `t=0`.

On a fixed `s`-set, the even graphs form the kernel of the complete-graph
incidence map and number `e_0=e_1=1` and
`e_s=2^binom(s-1,2)` for `s>=2`.  Summing the geometric fibres over all
labelled even targets counts exactly the states whose entrance time is at
most `t`; successive CDF differences give the shells.  The phase, fixed,
image, and CDF formulas in Theorem 1 follow without an omitted multiplicity.
The path witness loses its two endpoints per active round and confirms the
sharp `floor(n/2)` clock.

## 3. Review-A and lifecycle audit

Hostile Review A states zero Critical, zero Major, and zero Minor findings.
Its independent syndrome-counting verifier was replayed twice with bytecode
disabled.  Both runs are byte-identical to its frozen canonical transcript,
execute **3,605,601** assertions, and have transcript SHA-256

```text
d4a1592bd29c3f652bef0cb955b2f0b74181c98b6800eeee7df59e5e3a556095
```

The immutable Round-0 PDF has five A4 pages, 363,455 bytes, and SHA-256

```text
bba68d57e9f46cda2996db072b703ff0b18e5d19c7edab2a53ef24d3032c8602.
```

Layout-preserving text extraction shows exactly one Round-0/Round-1 textual
difference: the declarations sentence changed from “This Round-0 artifact
remains `HOLD_EXTERNAL`” to “This artifact remains `HOLD_EXTERNAL`.”  No
theorem, formula, proof, audit count, citation, or release prohibition changed.
Thus the Round-1 manuscript modification was genuinely lifecycle-only, as
the improvement log states.

## 4. Exact-control audit

The author verifier was cold-replayed twice with bytecode disabled.  Both
runs match `verification_output.txt` byte for byte, execute **3,167,525**
assertions, and preserve transcript SHA-256

```text
363d77a151dfa0b1d6b4ded84700d01dd249ed242573bff98fa38d490a1d4879.
```

It covers all 41,658 labelled states through ambient order six, 511
independently row-reduced parity systems through total order nine, every
target/source-rank fibre through stabilization and two extra epochs, exact
images, CDFs and shells, the path clock, the matrix orientation, and
nilpotence.

The fresh Review-B control is
`docs/papers157_161_sequence/reviews/p159_b/verify_p159_review_b.py`.  It
imports neither author nor Review-A code, represents graphs by symmetric
adjacency-row bitsets, independently builds the transfer, and uses a separate
column-basis calculation for the incidence systems.  It checks all 16,383
attainable target-parity cases through total order fourteen, all literal graph
states through `n=5`, every strict/full and temporal fibre in that range, all
mandatory boundaries, images and CDFs, and rank-layer positivity/nilpotence
through `n=24`.

Three cold runs are byte-identical to `CANONICAL.txt`, execute **88,623**
assertions, and end in `STATUS=PASS`.  Their hashes are

```text
reviewer verifier  a9ee66ff1eb59a0991d3d6972e3f9fdf7a0bc48872fc2a59647931e5aeae83fe
canonical output   ee58af611c1020c78748d675c571fa98c18c68200f72dda9b79515fd8639af5d
```

All computation remains bounded falsification pressure, not a substitute for
the all-parameter proof, novelty evidence, owner clearance, or release
authorization.

## 5. Build, metadata, fonts, and visual inspection

Two isolated directories containing only `main.tex` and `references.bib`
were built with `pdflatex -> bibtex -> pdflatex -> pdflatex`.  The two PDFs
are byte-identical to one another, `main.pdf`, and `main_round1.pdf`.  The
current/Round-1 artifact has five A4 pages, 363,444 bytes, and SHA-256

```text
72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d.
```

The settled final logs have no unresolved citation or reference, rerun
request, package warning, bad box, or build error.  PDF title, author,
subject, keywords, and custom metadata are blank; there is no encryption,
form, JavaScript, or identifying metadata.  All 27 reported font rows are
embedded, subsetted, and Unicode mapped.

All five pages were rasterized and inspected.  The title and abstract,
Theorem 1 and all boundary clauses, the incidence equations, matrix
sentinels, proofs, exact-audit table, declarations, external hold, and six
references are legible and within the page bounds.  No clipping, collision,
malformed glyph, or visual ambiguity was found.  The whitespace on page five
is harmless in a five-page short note.

## 6. Findings

### Critical

None.

### Major

None.

### Minor

**M1 — stale lifecycle statement in the claims ledger.**  The header of
`CLAIMS_EVIDENCE.md` correctly says `ROUND-1 / REVIEW A PASS / HOLD_EXTERNAL`,
but its final sentence says, “No formal Review A or Review B has yet been
performed on this manuscript.”  Review A has in fact been completed and is
documented in the same package.  Replace that sentence with a statement that
Review A returned zero findings and Review B is the pending/current gate.
This is an audit-provenance inconsistency only; it does not affect the
manuscript PDF or any mathematical conclusion.

## 7. Final disposition

**REVISE / HOLD_EXTERNAL.**  The required repair is one lifecycle sentence in
`CLAIMS_EVIDENCE.md`; no theorem, proof, verifier, bibliography, or PDF change
is requested.  After that sentence is corrected and the lifecycle status is
advanced consistently, P159 is mathematically acceptable for the internal
Round-2 freeze.  The bounded direct-owner search remains unresolved and this
report does not authorize posting, submission, circulation, author contact,
novelty claims, or priority claims.
