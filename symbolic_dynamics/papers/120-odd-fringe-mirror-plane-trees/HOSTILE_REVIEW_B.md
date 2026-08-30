# Hostile Review B — P120, round 1

Status: independent nonauthor review of the current round-one author
package. External dissemination, novelty, priority, and submission remain
**HOLD**. I used the current source, `main_round1.pdf`, canonical verifier,
coefficient artifact, supporting documents, and primary literature; I did
not use Reviewer A as mathematical evidence or adopt its conclusions. I did
not edit the manuscript or any existing file.

## Provisional verdict

**MAJOR REVISION for one direct-owner indexing error; the core theorem
package otherwise passes.** I found no counterexample to the induced vertex
transport, empty/nonempty conventions, involution, twisted-palindrome
grammar, coupled-series uniqueness, degree-six annihilator, or cycle/zeta
census. The fresh verifier has the requested 1,155,278 assertions and is
byte-stable. The material defect is in the comparison with the closest 2026
Catalan involution: that source grades plane trees by edges, whereas P120
grades them by vertices. The resulting fixed-point parity claim in Section 6
is false as written. The literal star-to-path separation remains valid, and
the count comparison can be repaired without changing a theorem about
`M`.

Severity count: **C: 0; M: 1 (owner scope/factual indexing); m: 1.**

## Independent reconstruction

### The map, induced transport, and `M^2`

For a nonempty plane tree `T=[T_1,...,T_k]`, the recursive definition is

`M(T)=[M(T_1),...,M(T_k)]` for even `|T|`, and
`M(T)=[M(T_k),...,M(T_1)]` for odd `|T|`.

At an odd source vertex, source child `i` therefore lands at target position
`k+1-i`, and that target subtree is exactly `M(T_i)`; at an even vertex it
lands at position `i`. Recursing inside that matched subtree gives a genuine
vertex bijection. Induction shows `|M(T_i)|=|T_i|`, so every transported
vertex has the same fringe order and the parent--child relation is
unchanged. This proves the pointwise statement, not merely preservation of
the multiset of fringe orders.

The same induction proves the involution. Root parity survives the first
round. At an even root the second round applies `M^2` to each child in place;
at an odd root it applies `M^2` and reverses the root list a second time.
Both return the source tuple. Thus there is no asynchronous-clock ambiguity
in the recursive notation.

The empty state `epsilon` is distinct from the leaf `[]`. It is fixed by a
separate convention and never enters the child grammar. The leaf is a
nonempty odd-order tree with zero children, so the odd fixed condition is
vacuously true. All quantifiers in Theorem 2.2 and all `n=0,1` uses are
consistent.

### Twisted-palindrome grammar

At an even-order root there is no outer reversal, so equality with the image
is equivalent to every child being fixed. The children's total order must be
odd. With `F=E+O` and `F(-x)=E-O`, the odd part of `SEQ(F)` is

`(1/2)(1/(1-F(x))-1/(1-F(-x)))`
`=O/((1-E)^2-O^2)`.

After adding the root marker this gives the displayed equation for `E`.

At an odd-order root, every off-centre choice `T` forces the opposite child
to be `M(T)`. Such a pair has series `A(x^2)`, and an ordered sequence of
pairs has series `1/(1-A(x^2))`. If a centre is present, it must be fixed;
because all pairs have even total order and the root's child total must be
even, the centre must have even order and contributes `E`, not `F`. The
optional centre therefore gives `1+E`, proving

`O=x(1+E)/(1-A(x^2))`.

There is neither a missing empty child nor a quotient by the two-cycle
action: the chosen left half of the ordered child list uniquely determines
the right half.

### Coupled uniqueness in `Q[[x]]`

Clearing the unit denominators gives

`H_1=E((1-E)^2-O^2)-xO=0`,

`H_2=O(1-A(x^2))-x(1+E)=0`.

For the specified Catalan branch `A(0)=0`, the Jacobian of `(H_1,H_2)` with
respect to `(E,O)` at `(x,E,O)=(0,0,0)` is the identity. The formal implicit
function theorem therefore supplies exactly one pair in
`(x Q[[x]])^2`. This proves the uniqueness claimed in Theorem 3.1;
the separately adjoined empty state does not create a constant term.

### Degree-six elimination and branch selection

With `F=E+O`, `G=E-O`, `B=A(x^2)`, and `c=1-B`, the coupled system becomes

`(F+G)(1-F)(1-G)=x(F-G)`,

`(c+x)G=(c-x)F-2x`,

`B^2-B+x^2=0`.

The signs and multiplication order are correct. The canonical exact lane
constructs these polynomials independently of the series coefficients,
takes the quadratic--linear resultant in `G`, reduces modulo the monic
quadratic in `B`, and computes the norm
`x^2 U^2+UV+V^2`. It compares all 25 nonzero monomials with `4x^2P` using
sparse integer arithmetic. I also recomputed both resultants independently;
they factor exactly as `4x^2P`.

Substitution of the formal solution makes this resultant zero. Cancellation
of `4x^2` is valid because `Q[[x]]` is an integral domain. Finally
`P(0,0)=0` and `P_y(0,0)=-3`, a unit in `Q`; hence the formal implicit
function theorem gives exactly one zero-constant branch. The manuscript
correctly calls `P` an annihilating equation and does not claim
irreducibility or minimality.

### Cycles and zeta

On every fixed order, `M^2=id`, so every component is a one-cycle or a
two-cycle. After removing the `f_n` fixed states, the other `a_n-f_n`
states pair without residue. An odd iterate fixes precisely the one-cycles,
and an even iterate fixes the full carrier. The product

`(1-z)^(-f_n) (1-z^2)^(-(a_n-f_n)/2)`

is therefore the exact fixed-order Artin--Mazur zeta function. With
`a_0=f_0=1`, the empty lane reduces to `(1-z)^(-1)`. The claim ceiling is
properly fixed-order and involutive; no asymptotic or global-in-`n` zeta
claim is smuggled in.

## Critical issues

None found.

## Major issue

### M1 (owner scope/factual indexing): the Claesson fixed-point parity is shifted by one

The manuscript says that the 2026 involution `h` “has no positive even-order
fixed points,” contrasting this with `f_2,f_4,f_6>0`. That comparison uses
incompatible size conventions.

In
[Claesson--Kitaev--Steingrímsson--Wang, *Involution h on Catalan
structures*](https://arxiv.org/abs/2607.06247), the single-node plane tree is
the Catalan object of size zero. Thus their size is the number of edges.
Their Proposition 2.11 gives the single-node tree plus `C_k` fixed objects at
edge size `2k+1`, with none at positive even **edge** size. P120 instead
defines order as the number of vertices. In P120's convention this becomes

- one `h`-fixed tree at vertex order `1`;
- `C_k` `h`-fixed trees at vertex order `2k+2`;
- no `h`-fixed trees at odd vertex order at least `3`.

Consequently `h` does have fixed trees at P120 orders `2,4,6`: their counts
are respectively `1,1,2`, while P120's `M` counts are `1,5,36`. The count
separation is real from order four onward, but the printed parity argument is
false. This matters because the paragraph labels `h` the strongest current
owner objection; its subtraction must use its actual grading.

Required repair:

1. State explicitly that Claesson et al. grade plane trees by edges and
   translate their Proposition 2.11 to the present vertex-order convention.
2. Replace the false parity sentence by the correct count comparison, for
   example `h_4=1` versus `f_4=5` and `h_6=2` versus `f_6=36`.
3. Retain the three-leaf-star to depth-three-path example: the primary paper
   states this literal action, and it correctly proves that `h` is not `M`.
4. Keep the conclusion narrow. Different literal action and different fixed
   counts do not by themselves constitute an owner-clearance certificate.

A bounded search using odd fringe order, parity-triggered child reversal,
and twisted-palindrome formulations found no direct source for the literal
`M` grammar or its degree-six fixed series. This remains only a bounded
non-hit.

## Minor issue

### m1 (support artifact): `README.md` names the wrong byte-identical PDF snapshot

The README says that `main.pdf` is byte-identical to
`main_round0_original.pdf`. The files are not identical:

- `main.pdf`: 380,490 bytes;
- `main_round1.pdf`: 380,490 bytes and byte-identical to `main.pdf`;
- `main_round0_original.pdf`: 378,895 bytes and different from both.

`BUILD.md` records the distinction correctly. Required repair: make the
README say that the current PDF and `main_round1.pdf` are identical, while
`main_round0_original.pdf` is the distinct pre-repair snapshot.

## Requested boundary and visibility audit

- Induced transport: source child positions map to the exact target blocks,
  and pointwise fringe order is proved and directly tested.
- `n=0`: one separately adjoined fixed state; it is not a plane-tree child
  and is not counted in `A,E,O,F`.
- `n=1`: the leaf is the `x` term of `O` and is fixed by the vacuous odd-root
  criterion.
- Nonempty quantifiers: all tuple/root grammar statements exclude only the
  adjoined empty state and correctly include the leaf.
- Coupled uniqueness: unit denominators and identity Jacobian are explicit.
- Degree six: exact annihilator and unique zero-constant branch pass; no
  minimal-polynomial claim is made.
- arXiv visibility: page 5 of `main_round1.pdf` visibly prints
  `arXiv:2512.18656` and `arXiv:2607.06247`; both identifiers resolve to the
  cited primary works.
- Cycle/zeta ceiling: fixed-order one-/two-cycle census only; generic
  involution and Artin--Mazur conversion receive zero credit.

## Exact controls and PDF inspection

- Fresh canonical verifier: **PASS**, **1,155,278 assertions**.
- Fresh stdout versus the 619-byte `code/verification_output.txt`:
  **byte-identical**.
- Exhaustive phase: the empty state and all 82,500 nonempty plane trees
  through vertex order twelve, for **82,501 states** total.
- Series controls: coupled and degree-six residuals through `x^30`, parity
  elimination through `z^15`, and all 31 CSV rows.
- Exact resultant: standard-library sparse audit matches all 25 monomials of
  `4x^2P`; independent resultant recomputation agrees.
- `main.pdf` and `main_round1.pdf`: **byte-identical**, 380,490 bytes.
- Five-page visual inspection: no clipping, overlap, missing glyph, or
  unreadable table; both arXiv identifiers are visible in the references.
- The settled log inspected for this review has no warning, undefined,
  multiply-defined, overfull, underfull, error, or rerun diagnostic.

These controls strongly support the map-specific formulas. They do not
repair the source-indexing error or certify novelty.

## Mandatory resolution before circulation

1. Correct the edge-count/vertex-count translation for the Claesson
   involution and replace the false parity comparison.
2. Correct the README's round-zero/round-one byte-identity statement.
3. Retain external status **HOLD** pending owner review of the accurately
   stated residual.
