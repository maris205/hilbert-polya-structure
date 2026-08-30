# Hostile Review A: Cross-Colon Monomial-Ideal Basins

**Reviewer role:** independent nonauthor round-zero reviewer.

**Audit date:** 2026-08-30 UTC.

**Materials audited:** the complete P124 package, including `main.tex`,
`references.bib`, all support documents, both verifier sources, both frozen
canonical transcripts, `main.pdf`, and `main_round0_original.pdf`.  I
reconstructed every displayed theorem and proof equation, reran both exact
controls, performed a source-only isolated four-stage build, and visually
inspected every PDF page.  I did not modify any manuscript, code, PDF, or
support file.

## Verdict

**GO_INTERNAL with two actionable MINOR repairs.  External release remains
HOLD.**

I found no counterexample, false equality, missed strip/square boundary,
basin double count, or verifier discrepancy.  The theorem package survives
hostile reconstruction.  After full subtraction of monomial-colon,
disjunctive-network, lattice-path, reflection, and rowmotion/toggle
background, the surviving paper-scale residual is specifically:

1. the literal crossed-colon-to-sourced-diagonal translation on the invariant
   monomial-ideal state space;
2. the upper-set compatibility that collapses the product of diagonal
   recurrent states to the power/checker families;
3. the first-occupied-diagonal theorem assigning every ideal to its exact
   attractor and checker phase; and
4. the contact-parity transfer that counts every resulting basin uniformly
   in the rectangle dimensions.

The recurrent census and sharp depth law are correct but supporting.  Their
OR-path mechanism receives zero novelty credit.  The current owner audit is
only a bounded direct-map non-hit and cannot support novelty, priority, or
external circulation.

## Severity counts

| Severity | Count | Disposition |
|---|---:|---|
| CRITICAL | 0 | No invalid central claim or unsafe release statement found. |
| MAJOR | 0 | No theorem, proof, control, or build failure requiring STOP found. |
| MINOR | 2 | Repair the claims/evidence locations and add an explicit internal-collision firewall. |

## Actionable repairs

### M1. Correct two proof anchors in `CLAIMS_EVIDENCE.md`

The frozen theorem numbering does not match two rows of the evidence map.

- The sharp square/non-square depth formula is part of **Theorem 3.2**, not
  “Theorem 3.3.”
- The layer identity and terminal ballot formula are part of **Theorem 5.1**,
  not a nonexistent “Corollary 5.2.”

All other listed anchors are consistent with the frozen PDF.  This is a
traceability defect only; the corresponding claims and proofs are correct.

**Required action:** correct those two anchors before the next freeze.

### M2. Record the P107/P104 internal firewall explicitly

The external owner subtraction in `main.tex` is disciplined, but the
paper-local support package does not record the closest internal comparisons.
P107 already occupies the narrative territory “ideal operator, fixed and
two-cycle classification, exact transients,” while P104 contains “monomial”
and “toggle” vocabulary in a random matrix-product setting.  Neither is a
literal collision, but omitting them leaves the P1--P123 collision audit
implicit.

**Required action:** add a short support-document collision note stating:

- P107 uses `I -> Ann(I)^r` on ideals of `Z/NZ`, CRT valuation coordinates,
  and clipped reflection; P124 uses monomial ideals in a truncated bivariate
  ring, crossed variable colons, and sourced OR diagonals.  The mechanisms
  and basin results are different, but generic “ideal dynamics with exact
  cycles/depth” language earns no contribution credit.
- P104 is a random contraction cocycle and has no ideal lattice, colon
  operation, diagonal Boolean dynamics, or basin transfer.  The shared words
  “monomial” and “toggle” carry no value.

This is a claim-discipline repair, not a mathematical objection.

## 1. Literal operator and staircase normal form

Let

```text
R_{a,b}=k[x,y]/(x^a,y^b),
T(I)=x(I:y)+y(I:x)
```

on monomial ideals.  The monomial basis consists of the rectangle cells
`(i,j)` with `0<=i<a` and `0<=j<b`, and a monomial ideal is an exponent upper
set.  The nonincreasing thresholds `h_i` therefore encode it bijectively.

For a fixed column `i`, membership in `(I:y)` begins at
`max(h_i-1,0)`.  The `-1` represents ordinary movement toward the ideal,
while clipping at zero correctly incorporates annihilation at `y^b=0`.
Multiplication by `x` shifts this threshold from column `i-1` to column `i`.
Similarly, `(I:x)` has thresholds

```text
h_1,h_2,...,h_{a-1},0,
```

because multiplication by `x` annihilates the last column; multiplication by
`y` raises these thresholds by one and clips at `b`.  The sum of monomial
ideals is union of their exponent upper sets, hence coordinatewise minimum of
thresholds.  This gives exactly equation (2.3):

```text
h'_0     = min(b,h_1+1),
h'_i     = min(max(0,h_{i-1}-1),h_{i+1}+1),
h'_{a-1} = min(max(0,h_{a-2}-1),1).
```

The degenerate strips are correct.  If `a=1`, then `x=0`, `(I:x)=R`, and
`T(I)=(y)` for every `I`.  If `b=1<a`, equation (2.3) reduces to the
staircase of `(x)`, as required by the symmetric annihilation calculation.
When `a=b=1`, `(y)=0=m`, so the statement remains valid.  No characteristic
or field-cardinality hypothesis is hidden.

Equation (2.5) also follows literally.  A target cell `(i,j)` receives the
`x(I:y)` term exactly from `(i-1,j+1)`, with a constant true condition when
`j=b-1`; it receives the `y(I:x)` term from `(i+1,j-1)`, with a constant true
condition when `i=a-1`.  Both predecessors have the same total degree as the
target.  Thus total-degree diagonals do not interact.

## 2. Diagonal source geometry

Indexing a degree-`d` diagonal by the `x` exponent produces

```text
(G_d w)_s = w_{s-1} OR w_{s+1}.
```

The missing left neighbor is a true source precisely when the diagonal has
hit the top `y` wall, `d>=b`; the missing right neighbor is a true source
precisely when it has hit the right `x` wall, `d>=a`.  With
`m=min(a,b)` and `M=max(a,b)`, the table (2.6) follows:

| Degrees | Length | Sources |
|---|---:|---:|
| `0<=d<m` | `d+1` | zero |
| `m<=d<M` | `m` | exactly one |
| `M<=d<=a+b-2` | `a+b-1-d` | two |

The middle band is empty if and only if `a=b`.  The diagonal map is an exact
coordinate representation on the constrained upper-set subset, not a claim
that arbitrary products of diagonal words are ideals.

## 3. Sourced-path lemma

### 3.1 No sources

For the source-free path, Boolean iteration records reachability by walks of
exact length.  For length `n>=2`, once `t>=n-2`, inserting or deleting an
immediate backtrack gives `G^(t+2)=G^t`.  The equation `G^2w=w` forces equality
within each vertex-parity class, and every such word satisfies it.  This
gives the four recurrent words: zero, all one, and the two checker phases.
An endpoint singleton has preperiod `n-2`, attaining the bound.  For `n=2`
this correctly says every word is already recurrent and the maximum depth is
zero.

For `n=1`, the adjacency OR is empty, so `1` maps to `0` and only `0` is
recurrent.  The special maximum depth one is necessary.

### 3.2 One and two sources

A boundary source injects a one at every step.  Monotonicity shows that the
orbit from any word dominates the orbit from zero.  With one source, the
farthest vertex is reached on update `n`, and zero attains this entrance
time.  With two sources, the fill time from zero is

```text
1 + max_i min(i,n-1-i) = ceil(n/2).
```

Once filled, `1^n` is fixed; every initial state reaches it.  Hence it is the
unique recurrent word in both sourced cases.  All boundaries `n=1,2` agree
with the displayed formulas.

These facts are mathematically correct but classical disjunctive-network and
walk-distance material.  They carry no independent contribution credit.

## 4. Recurrent ideals and sharp global depth

### 4.1 Upper-set compatibility

Diagonal recurrence by itself would allow many products of the four
source-free recurrent words.  The ideal upper-set condition eliminates those
products.  Every sourced recurrent diagonal is all one.  In the source-free
region, a recurrent word is zero, all one, or checkerboard.

If a diagonal is all one, its upper shadow is all one.  If it is a nonzero
checkerboard, its shadow contains an adjacent occupied pair.  Among recurrent
source-free words, only the all-one word contains such a pair; if the next
diagonal is sourced, it is independently forced to all one.  Therefore a
recurrent ideal has:

- zero on all diagonals below a first nonzero degree `r`;
- either all one or one checker phase on degree `r`; and
- all one on every higher diagonal.

Degree zero cannot be the first nonzero recurrent diagonal because the
one-vertex source-free map has only zero recurrent.  A checker first trace
requires `r<m`.  Thus equation (3.2) is complete:

```text
{m^r : 1<=r<=m} disjoint-union
{C_r^0,C_r^1 : 1<=r<m}.
```

Each `m^r` is fixed.  Neighbor OR swaps the two parity supports on degree
`r`, so `C_r^0` and `C_r^1` form one two-cycle.  The count is therefore
`m+2(m-1)=3m-2`, with no longer periods.

The sentence following definition (3.1) is now correct: `C_r^epsilon` is
upward closed because **all** higher-degree monomials are explicitly
included.  The proof later uses only the true statement that the immediate
shadow of the checker trace contains an adjacent pair.

### 4.2 Entrance time and square anomaly

The diagonal projections commute with `T`.  A whole ideal is recurrent
exactly when every diagonal projection is recurrent: once all projections
have period dividing two, their synchronized product also has period
dividing two; conversely, a recurrent ideal has recurrent projections.
Therefore the ideal entrance time is the maximum of its diagonal entrance
times.

Off the square, the one-source middle band contains a word of length `m`, so
the global upper bound is `m`; the zero ideal has the zero word there and
attains it.  On the square, the one-source band disappears.  The longest
source-free contribution is `m-2`, while the longest two-source contribution
is at most `ceil((m-1)/2)`, bounded by `max(1,m-2)`.  For `m>=3`,
`(y^(m-1))` has a single endpoint one on the length-`m` source-free diagonal
and attains `m-2`.  The unit ideal at `m=1` and zero ideal at `m=2` both have
depth one.  Equation (3.3), including every exceptional case, is sharp.

## 5. Complete first-trace basin theorem

Let `nu(I)` be the first occupied total degree, with `nu(0)=infinity`, and
let `S_r(I)` be the occupied `x`-exponents on degree `r`.

Every diagonal below `nu(I)` is zero and remains zero.  When
`1<=r=nu(I)<m`, degree `r` is a source-free path of length `r+1`.  Exact walk
reachability implies that for all sufficiently large `t`:

- if `S_r(I)` lies in one parity class `epsilon`, the occupied positions are
  precisely parity `epsilon+t mod 2`; and
- if `S_r(I)` meets both parities, the whole diagonal is occupied.

The recurrent classification then leaves exactly one compatible whole-ideal
attractor: the checker phase in the first case and `m^r` in the second.  This
also proves the phase formula (4.5); no unknown global phase is discarded.

If `nu(I)>=m`, every source-free diagonal remains zero and every sourced
diagonal eventually fills, producing `m^m`.  If `nu(I)=0`, upper-set closure
forces `I=R`, and `T(R)=m`.  When `m=1`, these cases exhaust all ideals and
the only basin is that of `m`.  The four cases in Theorem 4.1 are disjoint
and exhaustive.

The theorem uses the standard deterministic basin of a periodic orbit, so a
checker basin is correctly counted once for the two-cycle rather than twice
for its two phases.

## 6. Staircase paths and contact transfer

The stated east/south path is bijective with a nonincreasing staircase: at
abscissa `i`, descend to `h_i` before taking the east step.  The path has
`a` east and `b` south steps, hence there are `binom(a+b,a)` ideals.

For `1<=r<m`, the condition `nu(I)>=r` is precisely

```text
h_i >= r-i, 0<=i<=r,
```

which is equivalent to staying in the half-plane `i+j>=r`.  A legal path
contacts `(i,r-i)` exactly when `h_i=r-i`; under the barrier condition this
is equivalent to `x^i y^(r-i)` belonging to `I`.  Consequently the parity
mask of barrier contacts is exactly the parity mask of the first trace.

Equations (5.1)--(5.3) are an ordinary last-step recurrence.  Every prefix
arrives uniquely from the west or north.  Above the barrier its mask is
unchanged; on the barrier it is unioned with the parity bit of the current
abscissa.  The four states `empty`, `E`, `O`, and `E,O` are exhaustive and
disjoint.  Because `r<m<=a,b`, neither endpoint lies on the barrier, so no
initial or terminal contact is missed.

At `(a,0)`, the nonempty masks count ideals of exact first degree `r`.
The mixed mask gives the fixed-power basin; the two singleton masks jointly
give the checker-cycle basin.  At `r=1`, the unique mixed trace contains both
degree-one monomials, whose upper closure is exactly `m`, so `A_1^M=1` and
the basin of `m` consists of `m` plus the unit ideal.  Thus its size is two
for every `m>=2`.

## 7. Reflection and partition identities

Set `z=i+j-r`.  East steps raise `z` by one and south steps lower it by one;
the start and end heights are `b-r` and `a-r`.  Reflecting a bad prefix at
its first visit to `-1` swaps east and south steps in that prefix and yields
an unrestricted path with exactly `r-1` south steps.  Hence

```text
B_{>=r} = binom(a+b,a)-binom(a+b,r-1).
```

At `r=m`, this is exactly the terminal basin `nu(I)>=m`.  For `r<m`, paths
of exact first degree `r` are those staying above barrier `r` but not above
barrier `r+1`, so their number is

```text
B_{>=r}-B_{>=r+1}
  = binom(a+b,r)-binom(a+b,r-1).
```

The three nonempty contact masks partition this layer.  Adding the degree
zero unit ideal, all layers `1<=r<m`, and the terminal class telescopes to
`binom(a+b,a)`.  Equations (5.5)--(5.8) and the example table are correct.
For `(a,b)=(5,7)`, the reported basin sizes sum to 792 and the even/odd phase
splits sum to their corresponding checker basins.

For fixed `r`, the transfer stores four integers at each rectangle vertex.
Repeating for `r<m` costs `O(abm)` arithmetic operations with reusable
`O(ab)` storage.  This is polynomial in the rectangle parameters and is not
ideal-by-ideal enumeration.  The manuscript properly does not claim
minimality of the four-state transfer or scalar closed forms for its two
singleton-parity counts.

## 8. Exact mechanical controls

### 8.1 Core dynamics lane

Fresh command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon.py
```

Result: **PASS**, `assertions=1469669`.

The fresh output is byte-identical to
`ALG_CROSS_COLON_CANONICAL.txt`, with SHA-256
`b924e05c5e9ac71a25fb668d5bc2033f6ab58c325c7c73642a4dd0b096d67deb`.
The program checks all 131,064 path words through length 14 for all four
source types, and all 184,736 monomial ideals in the 81 rectangles
`1<=a,b<=9`.  It compares literal basis arithmetic, staircase update, and
diagonal update; then checks closure, recurrent/fixed/two-cycle families,
sharp depths, and witnesses.

### 8.2 Basin lane

Fresh command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon_basins.py
```

Result: **PASS**, `assertions=265987`.

The fresh output is byte-identical to
`ALG_CROSS_COLON_BASINS_CANONICAL.txt`, with SHA-256
`bdfd3e041b9f641101436c40918adbba59fd14b1f1381d77fa943ce00c0c76ff`.
This implementation does not import the core lane.  It rebuilds literal
colon arithmetic, follows all 48,602 ideals in the 64 rectangles
`1<=a,b<=8`, compares actual attractors and long-time checker phases with
Theorem 4.1, and compares exhaustive basin counts with the contact transfer.
It then checks ballot, partition, and transpose identities through
`a,b<=30`, covering 8,555 nontrivial transfer triples.

Combined exact assertions: **1,735,656**.  Both programs are deterministic,
standard-library-only integer controls.  Their bounded success corroborates
translations and boundary cases; it is not an all-parameter proof or an
owner certificate.

## 9. Owner subtraction

### 9.1 Disjunctive Boolean networks

The OR-path periodicity, Boolean-matrix/walk semantics, and generic transient
mechanism are established.  The manuscript cites the direct and later
owners, including [Goles and Hernández, *Dynamical Behavior of Kauffman
Networks with AND--OR Gates*](https://doi.org/10.1142/S0218339000000109),
[Jarrah, Laubenbacher, and Veliz-Cuba, *The Dynamics of Conjunctive and
Disjunctive Boolean Network Models*](https://doi.org/10.1007/s11538-010-9501-z),
and [Gadouleau, *Dynamical Properties of Disjunctive Boolean
Networks*](https://doi.org/10.4230/OASIcs.AUTOMATA.2021.1).

Accordingly, the following receive zero contribution credit:

- endpoint walk reachability and parity classes;
- period-one/period-two structure of an undirected OR path;
- one- and two-source fill times as graph distances; and
- generic Boolean-network basin terminology and algorithms.

The residual begins only when these path components must arise from one
monomial upper set and are translated back to the literal colon operator.

### 9.2 Monomial ideals and colon arithmetic

Monomial ideals as exponent upper sets, staircases, colon ideals, and
coordinatewise operations are classical.  Miller--Sturmfels is an adequate
general source, and the cited Ambhore--Sengupta paper is a static colon
neighbor rather than a dynamics owner.  None of this algebraic interface
earns contribution credit.

Current targeted searches for the exact expressions `x(I:y)+y(I:x)`,
`x(I:y)`, `y(I:x)`, crossed-colon iteration, and combinations with
“monomial ideal,” “attractor,” and “basin” did not locate a primary paper
defining the literal self-map or proving its first-trace/contact-transfer
package.  This is **BOUNDED_NO_DIRECT_HIT**, not a novelty certificate.

### 9.3 Rowmotion and toggles

The state space is visually the upper-set lattice of a rectangle, so
rowmotion and toggles are mandatory neighbors.  The manuscript provides the
correct firewall.  Rowmotion and every composition of ordinary toggles are
bijective on the finite state set; P124 has transient states in every
rectangle.  Therefore there can be no whole-state conjugacy.  The
simultaneous neighbor-OR rule is also not a sequential toggle product.

All generic order-ideal, path, file, rowmotion, and toggle vocabulary is
zero-credit background.  The paper does not attempt to reclaim it.

### 9.4 Generic basin algebra

Austin--Dinwoodie gives a general algebraic treatment of basin cylinders for
network dynamics.  That work does not define this ideal-lattice self-map or
own the first-degree contact classification.  It removes any value from
generic claims that basins can be encoded algebraically, but not from the
literal contact-parity formulas.

## 10. Internal P1--P123 collision audit

No earlier numbered paper uses the exact cross-colon map, sourced
total-degree diagonals, first-trace basin criterion, or four-state contact
transfer.

| Internal item | Shared surface | Noncollision and subtraction |
|---|---|---|
| P107, annihilator-power ideal dynamics | Finite ideal operator, fixed/two-cycle structure, sharp transients, basin-like exact temporal data. | P107 acts on all ideals of `Z/NZ` via `Ann(I)^r`, uses CRT valuation coordinates and clipped reflection, and derives arithmetic clocks/fibres/CDF/zeta.  P124 acts on monomial ideals of `k[x,y]/(x^a,y^b)` via crossed variable colons, uses sourced OR diagonals, and derives upper-set contact basins.  No literal or proof-mechanism collision; generic ideal-dynamics rhetoric is consumed. |
| P104, monomial toggle contraction cocycles | Words “monomial” and “toggle.” | P104 is a random two-by-two matrix contraction product with Lyapunov and fluctuation results.  It has no ideal lattice, colon, OR diagonal, or attractor basin.  Vocabulary overlap has zero value. |
| Classical/scouted rowmotion lanes | Rectangle order ideals and path/file coordinates. | Bijective toggle products cannot be conjugate to the transient cross-colon map.  State-space adjacency alone carries no contribution. |
| P118/P123 all-depth and basin-adjacent finite dynamics | Complete temporal classifications on other finite systems. | Different carriers and mechanisms.  Generic “complete basin/depth classification” language is not itself new; P124's residual is the literal first-trace/contact package. |

The basin theorem and polynomial transfer are important for value: without
them, the residual recurrent/depth package would be too close in narrative
shape to P107 after OR-network subtraction.  With them, P124 has a distinct
operator-specific output sufficient for an internal short paper.

## 11. Isolated build, freeze, visual, and metadata audit

I copied only the LaTeX source, bibliography, verifier files, canonical
outputs, and frozen PDF to a fresh temporary directory and ran:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages completed successfully.  The final log contains no LaTeX or
package warning, undefined citation/reference, overfull/underfull box, rerun
request, or error.

- PDF: 5 A4 pages, 293,617 bytes.
- PDF SHA-256:
  `3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81`.
- Fresh PDF, packaged `main.pdf`, and `main_round0_original.pdf` are
  byte-identical.
- Source SHA-256:
  `a34a431f1e048e3d43871b630dbfee63ac31097a7eff45c134455e80f415ac56`.
- All listed fonts are embedded and subsetted, with Unicode maps.
- Author, title, subject, and keywords metadata fields are empty; no
  creation/modification dates are reported.
- The PDF is unencrypted and has no form, JavaScript, or embedded file.
- Extracted text has no `??`, `[?]`, `[VERIFY]`, TODO, or FIXME marker.

I rasterized every page at 170 dpi and inspected all five pages.  Equations
(1.1)--(5.8), theorem blocks, source-band table, basin table, citations, and
bibliography are legible.  I found no clipping, collision, malformed symbol,
orphaned heading, blank page, or unreadable table entry.  Table 1 floats to
the top of page five after its short discussion at the foot of page four;
the reference is resolved and the placement is acceptable.

## 12. Binding claim ceiling

Allowed internal contribution claims:

- the literal synchronous cross-colon map on monomial ideals of the stated
  truncated bivariate rings;
- its exact sourced-diagonal translation and upper-set recurrent
  compatibility;
- the resulting powers/checker recurrent families and operator-specific
  sharp depth law, as supporting conclusions;
- the complete first-trace attractor and checker-phase theorem; and
- the operator-specific contact-parity recurrence and basin formulas.

Zero-credit or forbidden claims:

- a new theorem about disjunctive OR networks, path parity, or source fill
  times;
- a new monomial-colon, staircase, ballot/reflection, or finite-transfer
  method;
- a new rowmotion/toggle action or conjugacy;
- a first/novel/priority claim based on exact-string search;
- extension to nonmonomial ideals, asynchronous dynamics, or higher
  truncations;
- minimality of the four-state transfer or scalar closed forms for the two
  singleton-parity contact counts; and
- external posting, submission, or release.

## Final recommendation

**GO_INTERNAL / HOLD_EXTERNAL.**

The central mathematics, exact controls, frozen PDF, and owner subtraction
all pass.  The two MINOR repairs are documentary: fix the two incorrect proof
anchors and make the internal P107/P104 collision firewall explicit.  They do
not justify STOP.  External release must remain on HOLD pending a broader
specialist search for the literal colon operator and its basin theorem.
