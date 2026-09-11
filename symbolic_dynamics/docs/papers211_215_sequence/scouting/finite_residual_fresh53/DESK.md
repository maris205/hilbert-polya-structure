# Fresh53 — bounded path/board pre-admission screen

Date: 2026-09-11 UTC. Author: current_round_independent_scout.
Disposition: **ZERO_ELIGIBLE_NEW_LITERALS / NO_HANDOFF / NO_PILOT**.
This is an author desk, not an independent review or a seat decision.

The parent requested at most two genuinely unoccupied finite combinatorial
rules, archive/quotient subtraction first, and deductive feasibility before
any pilot. No scientific program was written or executed. Only this file
was created; no old author package, central index, number, Git state or
external manuscript was changed. Fresh52 is not reopened here.

## 1. Directed peg-jump navigation stops at an exact old control

The tempting board rule is simultaneous disjoint replacement
$110\mapsto001$ on a rooted binary circle of length $n\ge3$.
It removes one peg per jump. This is **not a fresh candidate**:
the old ZR rule is simultaneous $001\mapsto110$ on the identical carrier.
Writing $C(w)_i=1-w_i$, the update identity is
$$C\circ ZR\circ C=J.$$
Indeed complementation matches the active triples bijectively, and the
unbordered triple has disjoint occurrences. It also matches the old
identity conventions for $n=1,2$. No reversal is needed for this adapter.

The original old proof, not a recovery summary, was read at
`docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md`,
lines 24–75 (actual native return `632640`). It already supplies the
monotone peg/zero count, fixed-point description, inverse-selection
constraints and sharp largest fibre. Its proposed stronger clock remains
explicitly unproved there; that gap does not free the occupied map.

Opening the circle into an interval would change the boundary, so this
desk does **not** assert an unproved whole-carrier conjugacy between the
interval and circle versions. It also does not promote a boundary-only
change: no independent interval residual was established. The original
resource-rewriting discussion, lines 180–227, was read separately
(`eff0ee`); its PFF rule is different and is not falsely identified with J.

## 2. Finite collision ants: the natural full-state rule is bijective

This is an explicitly defined **ineligible board control**, not a newly
admissible nonbijective literal. It tests whether synchronous collisions
create information loss in a locally reversible walker model.

### Claim and assumptions

Status: **PROVABLE AS STATED**. Let the board be
$B=\mathbb Z/a\mathbb Z\times\mathbb Z/b\mathbb Z$, with $a,b\ge1$.
The full finite state consists of a coloring $c:B\to\{0,1\}$ and $m\ge0$
labelled ants with positions $p_j\in B$ and directions
$d_j\in\{0,1,2,3\}$. Directions remain formal four-valued headings even on
a board of width one or two. Write $e(d)$ for the corresponding unit step
in the quotient board, and $r(0)=1,r(1)=-1$ modulo four.

All ants read the **old** coloring, turn, and move simultaneously:
$$d'_j=d_j+r(c(p_j)),\qquad p'_j=p_j+e(d'_j).$$
Every old cell is flipped once per ant leaving it, with parity:
$$c'(v)=c(v)+\#\{j:p_j=v\}\pmod2.$$
Collisions are permitted, with this precise parity convention. No
annihilation, position-forgetting or hidden update order is inserted.
The full-state map is a bijection; so is its quotient by ant relabelling.
Consequently all its finite orbits are recurrent and every fibre is one.

### Strategy and dependencies

Recover positions from the output headings, then parity counts, then old
colors, then old headings. The quotient conclusion uses equivariance of
this explicit inverse, not a general assertion about arbitrary projections.

### Proof

1. From an arbitrary output state, set
   $p_j=p'_j-e(d'_j)$. Thus every old position is determined uniquely,
   regardless of collisions or coincident step vectors on a narrow board.
2. Compute $N(v)=\#\{j:p_j=v\}$. Recover the unique old coloring by
   $c(v)=c'(v)-N(v)\pmod2$.
3. Set $d_j=d'_j-r(c(p_j))\pmod4$. These are unique old headings.
   Substitution into the three forward equations recovers the supplied
   output exactly. This constructs a two-sided inverse on the entire
   finite carrier, including $m=0$.
4. Relabelling ants commutes with both the forward rule and the constructed
   inverse. They therefore induce mutual inverses on the orbit set of
   labelled states under the symmetric group. Unlabelled multiplicities
   do not create nontrivial fibres.

This proves the claim. It is only an elementary eligibility obstruction,
not a new orbit-period classification or a publication-level result.

Forgetting directions is different: it need not give an autonomous factor.
For example, on a $5\times5$ all-white board, a single ant at the same
position but with two different headings moves to different positions
after turning. Their direction-forgetting images initially agree, but
their next direction-forgetting images do not. Thus a board/position-only
projection is not a valid way to manufacture a deterministic quotient.

## 3. Source and search limits

The project research workflow was reread in full (`4dba68`), as were the
installed proof-writer and research-lit instructions (`b4ff9c`, `222feb`).
The current batch header was read (`7d22b6`). Earlier lifecycle paragraphs
in the long stream-state return were truncated and are not proof inputs.

The primary publisher-indexed body of *Recognizing the Repeatable
Configurations of Time-Reversible Generalized Langton's Ant Is
PSPACE-Hard*, Algorithms 4 (2011),
<https://www.mdpi.com/1999-4893/4/1/1>, defines the single-ant process and
expressly describes full-configuration time reversibility. That is the
background ownership used here; the parity-collision proof above is the
desk author's own deduction, not attributed to that paper. The fresh
direct page opening returned HTTP 429, so no successful full-page/body
opening or independent source-proof audit is claimed. The indexed
publisher result is actual source evidence, with this access limitation.
No complexity theorem is used in the exclusion proof.

Bounded archive searches used `rg` for cyclic automata, board walkers,
promotion, box-ball, peg jumps, Langton/turmite and flipping scatterers.
The initial broad search also matched embedded JSON and was truncated;
it was navigation only. A later Markdown-oriented search found the exact
old ZR original. The Langton/flipping-scatterer Markdown search returned
exit 1/no match (`c756d7`), which is **not** an absence or novelty certificate.
Promotion/rotor/box-ball hits were not instantiated as new candidates.
An overbroad local filename lookup returned many unrelated PDFs and a
missing `literature/` directory (exit 2, `244fd2`); no local PDF was read
or represented as relevant on that basis. No download/API script or
scientific executable was run.

## 4. Handoff boundary

There is no eligible candidate and no request for a larger box. The exact
peg-jump conjugacy blocks the first navigation lead. The finite collision
walker and its legitimate unlabelled quotient both have singleton fibres;
the lossy orientation projection is not autonomous. Changing the local
physics to force information loss would be a new rule, not a conclusion
of this desk, and has not been proposed. Current seat counts are untouched.
