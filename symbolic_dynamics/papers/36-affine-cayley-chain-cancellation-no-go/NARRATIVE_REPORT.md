# Paper 36 narrative report — SD-C38

## 1. The question left by Paper 35

Paper 35 separated the positive affine graph, formal symmetrization,
nonbacktracking relation ledger, and Bost--Connes diagonal partition trace. It
left one narrow repair: perhaps the unwanted relation cycles could be removed
at chain level, directly from the same presentation, without projecting to a
boundary sector or changing the graph clock.

Paper 36 tests that repair in its strongest literal form. It fills every
translate of the defining Cayley relation cell and insists that recurrence,
the free edge marker, and determinant ownership all survive on one object.

## 2. Central tension

The relation cell is simultaneously too strong and too inhomogeneous.

- It is too strong because the filled affine Cayley complex is contractible.
  Complete relation cancellation kills all closed-path homotopy, including any
  sector one hoped to retain.
- It is too inhomogeneous because it equates `vu` with `u^r v`, paths of
  lengths two and `r+1`. A marker counting each original edge once cannot pass
  to the quotient.

These are independent obstructions. The first removes recurrence; the second
invalidates same-clock descent even before an operator is chosen.

## 3. The analytic separation

The paper then closes a possible loophole: perhaps the quotient could still be
called the determinant of the prequotient symbolic operator. Source-coordinate
damping makes the full Hashimoto operator trace class without inspecting any
arithmetic target. Its Fredholm trace at length `r+3` receives a strictly
positive contribution from the affine relation polygon. The chain quotient is
empty. One determinant-bearing object cannot have both ledgers.

This is the paper's clearest visual and conceptual firewall:

```text
same prequotient shift + same z + honest Fredholm trace
                         sees the relation polygon
                                      |
                                      | cell quotient
                                      v
contractible filled complex + no surviving loop + z does not descend
```

## 4. Why superdeterminants do not rescue the mechanism

The most obvious graded lift gives one even vertex copy, two odd edge copies,
and one even cell copy. Its supertrace multiplier is `1-2+1=0` at every power.
This cancellation is mathematically valid, but it never reads the affine
relator. It works for every two-generator one-relator presentation and erases
desired and undesired recurrence together. Generic success is the failure
mode.

## 5. Contribution and restraint

The contribution is not a new homology theory or determinant formula. It is a
source-locked incompatibility theorem joining four exact statements that are
often blurred when symbolic, homological, and operator objects share the same
presentation notation.

The paper should lead with the negative theorem, make the marker calculation
visible early, and keep three traces separate throughout:

1. path/homotopy cancellation in the Cayley complex;
2. ordinary Fredholm traces of the damped prequotient Hashimoto operator;
3. finite-factor traces and supertraces used only as controls.

## 6. Exact evidence

The canonical source and prototype each pass `33/33` checks; the independent
authority evaluator passes `35/35`, and the integration suite passes `53/53`.
For `r=2,3,4,5`, the first identity-word excess over the free group occurs
exactly at lengths `5,6,7,8`, the relator lengths. At the composite baseline
`r=4`, the excess is `14` and one damped relation cycle has weight `2^-46`.
Six finite chain controls pass twelve boundary-square checks; complete
finite-presentation filling kills their first homology. All `48` sampled
supertraces vanish exactly. Fresh A/B and cold C reproduce `19` scientific
payloads byte-identically, with authority aggregate
`58a5d3b404d85163edfe74bea45b077da07ac6ff4f0794aff0bf9f1fbcf6ea9e`.

These computations expose the mechanism but do not carry the infinite proof.

## 7. Decision

The exponent is genuinely structural (`A0`), but no nonzero recurrent sector
survives (`A1`), the marker fails (`A2`), determinant ownership fails across
the quotient (`A3`), and graded cancellation is generic (`A4`). Therefore
Route A is rejected and Route B is not invoked.

The next paper, if any, must keep paths distinct and test a source-derived
non-flat finite-rank coefficient system on the unquotiented same-marker
Hashimoto object. Another full relation quotient would repeat the closed
failure.
