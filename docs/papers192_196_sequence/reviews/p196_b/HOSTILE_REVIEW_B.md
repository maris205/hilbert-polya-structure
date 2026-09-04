# P196 hostile Review B

**Reviewer relation:** process-separated internal Reviewer B; did not author
P196 and did not perform its Review A.  No author or Review-A code is imported.
**Frozen input:** `main_round1.pdf`, the current source/control package, the
batch protocol, and the accepted Review-A package are pinned in
`PINNED_INPUTS.sha256`.
**Decision:** `ACCEPTED_NO_CHANGE` (`0 Critical / 0 Major / 0 Minor`).
**Mathematical decision:** `PROVABLE_AS_STATED`.
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Outcome

The Round-1 theorem package survives a third, materially different
reconstruction.  Review B encodes a state as one radix-`q` integer.  For a
target symbol `c`, it forms the binary relation matrix

```text
R_c(a,b) = 1{a => b = c}.
```

The exact fibre of a cyclic target is the trace of the corresponding product
of relation matrices.  This cyclic constraint-satisfaction representation
proves the image criterion by positivity.  The top-symbol matrix is the
weak-order matrix, while every nontop matrix has rank one; splitting their
cyclic product recovers the claimed binomial-difference factors without
enumerating the manuscript's weak chains.

The characteristic polynomial was rederived from the eigenvector coordinate
recurrence and its possible roots.  Root multiplicities were attacked
explicitly: `lambda^q-(lambda+1)^(q-1)` is square-free.  The executable check
uses Faddeev--LeVerrier through `q=12`, neither the author's row operations nor
Review A's determinant lemma and Leibniz expansion.

The independent verifier exhausts 32 boxes, including the orthogonal range
`2 <= q <= 7`, `1 <= m <= 5` and the longer boxes `(q,m)=(2,9),(3,8)`.
It checks 41,704 literal transitions, every labelled one-step fibre, 208,300
labelled higher-time fibres, all tested iterate-fixed counts, direct least
rotation periods, 3,420 relation-matrix gap coefficients, and eleven complete
characteristic polynomials.  Two consecutive executions are byte-equal to
the frozen reviewer transcript.

## Separation from the earlier routes

| surface | author | Review A | Review B |
|---|---|---|---|
| state representation | tuple/product words | tuple words and incoming-edge tables | packed radix integers |
| image proof | coordinate implication followed by an explicit section | direct coordinate reconstruction | positivity of a cyclic relation-matrix product |
| fibre engine | weak chains cut at nontop sites | direct weak-chain enumeration | trace of symbol-labelled CSP relations and rank-one product factorization |
| characteristic polynomial | row subtraction / last-row induction | rank-one determinant lemma plus executable Leibniz expansion | eigenvector recurrence plus square-free root argument; executable Faddeev--LeVerrier |
| orbit check | literal iterates and transfer traces | tuple functional graph and direct periods | packed functional graph, rotation-period classification, and relation counts |

The unavoidable literal truth table, core predicate, and stated closed
formulas are shared objects under review, not reused implementations.

## Hostile attacks and dispositions

- **Synchronous orientation:** every output digit is computed from the old
  packed digits at `i` and `i+1`.  The checked core action is left shift
  `(Sy)_i=y_(i+1)`, not the inverse shift.
- **Image iff:** relation-product positivity gives a preimage exactly when
  every adjacent pair ending in a nontop letter is a strict descent.  This is
  the manuscript's language, including the cyclic wrap.
- **Tail convention:** the image is a shift-permuted core.  Every outside
  state enters it after one update and no outside state is periodic; depths
  are therefore exactly zero or one as stated.
- **Fixed and periodic boundaries:** a shift-fixed legal word is constant,
  and only the all-top constant is legal.  Fixed iterates through `2m` and
  direct least-period populations agree with the trace and Möbius formulas.
- **Characteristic multiplicity:** zero is not an eigenvalue.  Consecutive
  eigen-equation differences force
  `lambda v_a=(lambda+1)v_(a-1)`, hence the claimed polynomial.  Its only
  possible common root with its derivative would be `-q`, which is not a
  root, so no multiplicity information is lost.
- **Cyclic fibre orientation:** the reviewer uses
  `tr(R_(y_0)...R_(y_(m-1)))`, whose row/column states are consecutive source
  letters.  The rank-one factors occur in the same cyclic order as the
  target's nontop sites.
- **All-top target:** the relation product is `U^m`; `U` is upper triangular
  with unit diagonal, so the trace is `q`.
- **Outside-core target:** a violating adjacent nontop pair contributes a
  zero distance-one factor.  Both the relation trace and literal indegree are
  zero.
- **Adjacent sites and singleton site:** `d=1` reduces to `1{a>b}`.  A target
  with one nontop site uses the unique gap `d=m`; no source coordinate is
  duplicated or omitted.
- **Parameter edges:** every allowed `q` is at least two.  The minimum
  `q=2`, every `m=1` box, top/nontop boundaries, and wraparound gaps are
  explicitly exercised.  The excluded one-symbol alphabet is not silently
  used.
- **Higher-time fibres:** packed iteration agrees for every target at the
  distinct times among `1,2,m,m+1,2m` with the rotated one-step relation
  count.  Off-core higher-time fibres vanish automatically.
- **Mass:** every literal source contributes once; both the one-step and each
  checked higher-time indegree table have total mass `q^m`.

## Source, owner, and production disposition

The five citation records match primary publisher, journal, or arXiv
metadata and are used only for background.  A fresh bounded exact, semantic,
and translated query set located no direct owner of the literal conjunction.
This non-hit is not novelty, priority, completeness, clearance, or freedom to
operate.

Internally, P187 and especially P190 already consume cyclic transfer-matrix
and gap-product fibre machinery.  Those generic engines receive zero
contribution credit here.  The only residual kept for P196 is the conjunction
of the literal finite-chain Goedel implication, its exact first-image
inequality core and rotation, and its specific binomial-difference target
atlas.  The gate therefore remains `OWNER_AMBER / HOLD_EXTERNAL`.

Two source-only cold builds are byte-identical to each other and to
`main_round1.pdf`.  All three A4 pages passed text, font, metadata, active
content, and raster inspection.  No paper source was changed by Review B.

Final disposition: `ACCEPTED_NO_CHANGE`, with no open finding.
