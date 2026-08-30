# Round-two nonauthor signoff — P120

Status: **GO_INTERNAL / EXTERNAL HOLD**.

Scope: current `main.tex`, `main.pdf`, `main_round2.pdf`, the two hostile
reviews, the paper-local verifier and canonical transcript, and the support
documents.  This is an independent signoff after the Reviewer-B repair.  It
is not a novelty certificate, priority claim, or external-release approval.

## Resolution of the round-one owner-indexing issue

The repair is correct and complete.

Claesson--Kitaev--Steingrímsson--Wang grade their abstract Catalan objects by
Catalan size.  For rooted plane trees this is the number of edges: their
empty Catalan element is the one-node tree.  Their Proposition 2.11 gives
that element together with `C_k` fixed objects at source size `2k+1`, and no
fixed objects at positive even source size.  Since P120 grades by vertices,
`n = source size + 1`, so the exact translation is:

- one `h`-fixed tree at vertex order `1`;
- `C_k` `h`-fixed trees at vertex order `2k+2`;
- no `h`-fixed trees at odd vertex order at least `3`.

Thus `h_4=C_1=1` and `h_6=C_2=2`, whereas the verified P120 counts are
`f_4=5` and `f_6=36`.  The manuscript now states precisely this count
separation and no longer makes the false even-vertex-order parity claim.
The same corrected translation appears in `CLAIMS_EVIDENCE.md`,
`NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, and `BUILD.md`.  No stale false
parity statement remains outside the historical hostile reviews.

The objectwise separation also remains valid.  The primary source explicitly
sends the plane tree with three leaf children at the root to the depth-three
path.  P120's three-leaf star has four vertices, so its root trigger is even;
its three leaf subtrees are individually fixed and the root child list is not
reversed.  It is therefore fixed by `M`.  This demonstrates different
literal actions without elevating that difference into owner clearance.

Primary source checked:
[Claesson--Kitaev--Steingrímsson--Wang, arXiv:2607.06247](https://arxiv.org/abs/2607.06247).

## Earlier mathematical and owner gates

All earlier gates remain resolved.

1. **Simultaneous update and induced transport — PASS.**  The recursive
   source-to-image vertex bijection is defined position by position.  It
   sends every source fringe subtree to its image, preserves its order
   pointwise, and makes the invariant trigger set and involution proof valid.
2. **Boundary lanes — PASS.**  The adjoined empty state is a separate fixed
   singleton with `a_0=f_0=1`; it is absent from `A,E,O,F`.  The one-vertex
   tree is included in the nonempty odd lane and is fixed by the vacuous
   odd-root condition.
3. **Root-local fixed criterion and grammar — PASS.**  Tuple comparison gives
   pointwise fixed children at even roots and an exact `M`-twisted palindrome
   at odd roots.  Off-centre pairs contribute `A(x^2)` and an optional centre
   contributes `E`, yielding the two displayed coupled equations.  Unit
   denominators and the identity Jacobian give the stated formal-series
   uniqueness.
4. **Elimination and branch — PASS.**  The three displayed identities in
   `F,G,B` give `Res_B(Res_G(H1,H2),H3)=4*x^2*P`.  The formal domain permits
   cancellation of `4*x^2`, and `P_y(0,0)=-3` selects one zero-constant
   branch.  No irreducibility or minimal-polynomial claim is made.
5. **Temporal census — PASS.**  Because `M^2=id`, every component has length
   one or two.  The fixed coefficients therefore give the exact two-cycle,
   iterate-fixed, and fixed-order Artin--Mazur zeta formulas, including the
   empty lane.
6. **Owner subtraction — PASS AT THE INTERNAL CLAIM CEILING.**  Catalan
   enumeration, mirror and neighboring involutions, algebraic/resultant
   machinery, and involution/zeta bookkeeping receive zero contribution
   credit.  The surviving claim is only the literal odd-fringe update and
   its map-specific conjunction.  The bounded owner-search non-hit is
   explicitly not treated as proof of novelty or priority.

## Exact verifier evidence

I ran from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 papers/120-odd-fringe-mirror-plane-trees/code/verify.py
```

Fresh result:

- `PASS`;
- **1,155,278 exact assertions**;
- **82,501 states**: the separate empty state and all 82,500 nonempty plane
  rooted trees through vertex order 12;
- coupled and degree-six residuals zero through `x^30`;
- parity-elimination residual zero through `z^15`;
- all 31 coefficient-table rows match;
- stdout is byte-identical to the stored **619-byte**
  `code/verification_output.txt`.

The standard-library sparse audit reconstructed all 25 coefficients of
`4*x^2*P`.  As a second implementation, I also formed both resultants with
SymPy from the three manuscript identities.  The expanded difference from
`4*x^2*P` was exactly zero, both sides had 25 nonzero terms, and the
independent derivative check returned `P_y(0,0)=-3`.

## Isolated build and PDF inspection

I copied the package into a fresh temporary directory and ran the exact
four-stage build:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages returned zero.  The isolated PDF, repository `main.pdf`, and
`main_round2.pdf` are byte-identical:

```text
SHA-256 9d20551ed2394fe554520ddcae553d095d966f9cc6efe54a8bfe2e93d5cde8e2
```

Mechanical audit:

- **5 A4 pages**, **380,615 bytes**; Conclusion and References on page 5;
- settled LaTeX and BibTeX diagnostics: zero genuine warnings, errors,
  undefined citations/references, multiply-defined labels, overfull or
  underfull boxes, and rerun requests;
- bibliography closure: **9/9** cited entries;
- **30/30 fonts** embedded, subsetted, and Unicode-mapped;
- empty Author metadata, no creation/modification dates, no forms,
  JavaScript, encryption, or page rotation;
- both `arXiv:2512.18656` and `arXiv:2607.06247` are visible on page 5;
- no `??`, `[?]`, `[VERIFY]`, `TODO`, `FIXME`, or `internal draft` sentinel.

I rendered and inspected all five pages at 144 dpi.  Equations (including the
degree-six polynomial), both tables, theorem statements, links, and the
bibliography are legible; there is no clipping, overlap, missing glyph, or
misplaced float.

The README snapshot statement is now accurate.  `main.pdf` and
`main_round2.pdf` share the hash above; `main_round1.pdf` is the distinct
380,490-byte first-repair snapshot, and `main_round0_original.pdf` is the
distinct 378,895-byte pre-repair snapshot.

## Verdict

All requested round-two issues are resolved, the mathematical package and
exact controls remain intact, and the current PDF is mechanically stable.
Verdict: **GO_INTERNAL**.

External circulation, submission, specialist contact, novelty language, and
priority language remain **HOLD**.
