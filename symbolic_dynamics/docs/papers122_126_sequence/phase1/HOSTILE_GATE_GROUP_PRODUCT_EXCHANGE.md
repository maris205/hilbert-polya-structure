# Hostile owner/value gate: group product-exchange

Date: 2026-08-30 UTC. Role: independent nonauthor gate. Scope inspected:

- `proof_spikes/GROUP_PRODUCT_EXCHANGE_REPORT.md`;
- `proof_spikes/verify_group_product_exchange.py` and canonical stdout;
- the C12 algebraic scout entry;
- P111 and P119 claim/evidence and collision records;
- the Boffa--Point Thue--Morse owner line and the closer dynamical treatment
  by Almeida.

No manuscript or verifier source was edited. No paper number was allocated and
no Git operation was performed.

## Gate decision

**KILL_AS_STANDALONE / DIRECT_ENGINE_AND_DYNAMICS_OWNER / THEOREM_THIN.**  
External status remains **HOLD_EXTERNAL**.

The algebra in Theorems 1--2 and the depth/cycle formulas is essentially
correct. The kill is a value and ownership decision, not a falsification of the
main equalities.

After strict subtraction, the residual consists of:

1. an elementary one-step observation that the fibre over `(a,b)` is the set
   of conjugators from `a` to `b`;
2. the fact that, once the owned class-two identity sends every pair to the
   diagonal at time two, odd-order power maps permute that diagonal and hence
   preserve uniform fibres;
3. aggregate depth counts from the classical commuting-pair identity; and
4. the standard cycle/zeta census of the squaring permutation.

This is a sound proposition package, but not a paper-scale theorem package.
Boffa--Point own the recursive Thue--Morse identity engine. More seriously for
the dynamics framing, Almeida (2003) explicitly calls
`(x,y) -> (xy,yx)` the **Thue--Morse operator**, studies it as an implicit
operator on finite groups, and visualizes its functional graphs with distance
to cycle and cycle identity encoded in the plots. Thus neither the map, the
iteration viewpoint, the Thue--Morse interpretation, nor “finite-group
dynamics of product exchange” can be presented as new. The exact fibre census
was not found verbatim in the bounded search, but it is too mechanical and too
short to survive those subtractions as an independent paper.

## Claims matrix

| Item | Correctness | Credit after subtraction | Gate finding |
|---|---:|---:|---|
| `Phi(x,y)=(xy,yx)` generates the two Thue--Morse blocks | Correct | Zero | Boffa--Point identity engine; Almeida names and iterates the exact operator |
| Class-two groups satisfy `I_2`, hence `Phi^2` is diagonal | Correct | Zero | Explicitly designated zero-credit owner input |
| Arbitrary-group one-step fibres are centralizer cosets | Correct | Low residual | Four-line conjugator calculation; ordinary conjugacy facts are background |
| Odd class-two `Phi^t`, `t>=2`, has uniform diagonal fibres of size `|G|` | Correct | Low residual | Owned collapse plus bijectivity of an odd power map |
| Depth-layer counts `(10)` | Correct | Very low residual | Owned collapse plus the commuting-pair identity |
| Recurrent cycles and fixed-count formula | Correct modulo a typesetting defect | Zero/very low | Pure squaring-map orbit bookkeeping |
| Prime-exponent zeta product | Correct | Zero | Standard conversion from identical nonidentity cycle lengths |
| “Full functional graph” | Overstated | Not allowed | Report gives pointwise indegrees and aggregate layers/cycles, not rooted in-tree isomorphism types or attachment classification |

Allowed archival claim ceiling: **an elementary proposition/corollary note**
about conjugacy fibres and the resulting aggregate census on odd class-two
groups. It must not claim a new Thue--Morse map, a new identity, a first
dynamical treatment, or a full functional-graph classification.

## Round 1: equation-by-equation hostile audit

Write

\[
\Phi(x,y)=(xy,yx).
\]

### A. Arbitrary-group conjugacy fibres: passes

For a target `(a,b)`, `xy=a` gives `y=x^{-1}a`. Substitution into `yx=b`
gives

\[
x^{-1}ax=b. \tag{A1}
\]

Thus preimages are in bijection with conjugators from `a` to `b`. If `x_0`
is one such conjugator, all are the left coset `C_G(a)x_0`, so the fibre has
size `|C_G(a)|`; otherwise it is empty. This proves the claimed image

\[
\operatorname{im}\Phi=\{(a,b):a\sim_G b\}. \tag{A2}
\]

Summing over conjugacy classes gives

\[
|\operatorname{im}\Phi|=\sum_K |K|^2. \tag{A3}
\]

No orientation error was found. The proof should say explicitly which coset
side is used if it is ever promoted, but the cardinality is unaffected.

Value finding: (A1) is useful, pointwise, and valid for every finite group;
it is nevertheless a direct change of variables followed by the most basic
centralizer-coset fact. It cannot carry a paper by itself.

### B. Class-two collapse: passes, but is owned

In a group of class at most two, `xy` and `yx` differ by a central
commutator, hence commute. Therefore

\[
\Phi^2(x,y)=((xy)(yx),(yx)(xy))=(r,r),
\qquad r=xy^2x. \tag{B1}
\]

This is exactly the `I_2` equality. It is the crucial engine for every later
claim and receives zero contribution credit under the requested
Boffa--Point subtraction.

### C. Uniform fibres for every iterate: passes

For finite odd-order `G`, the map `q_s:g -> g^{2^s}` is bijective for every
`s>=0`. If `e=exp(G)`, choose an integer `h` with
`2^s h = 1 (mod e)`; `g -> g^h` is a two-sided inverse. This argument is
valid even when `G` is nonabelian because only powers of the same element are
composed.

Fix `r in G`. For each `x in G`, equation `xy^2x=r` is equivalent to

\[
y^2=x^{-1}rx^{-1}, \tag{C1}
\]

which has one solution. Hence every `(r,r)` has exactly `|G|` preimages
under `Phi^2`. More explicitly, for `t>=2`,

\[
\Phi^t(x,y)=
\left(r^{2^{t-2}},r^{2^{t-2}}\right). \tag{C2}
\]

Bijectivity of `q_{t-2}` transports the size-`|G|` fibres of `Phi^2` to
every later iterate. Theorem 2 is therefore correct, including its support
only on the diagonal.

Hostile value finding: after (B1) is assigned zero credit, (C1)--(C2) are a
one-line odd-power permutation consequence. “All-iterate” sounds stronger
than the remaining proof content.

### D. Recurrent set and depth layers: passes

The diagonal is forward invariant and `Phi(g,g)=(g^2,g^2)`. Oddness makes
squaring a permutation, so every diagonal point is recurrent. Equation (B1)
puts every state on the diagonal by time two. Hence the recurrent set is
exactly the diagonal.

A non-diagonal point has depth one exactly when its coordinates commute;
otherwise it has depth two. The number of ordered commuting pairs is
`|G|k(G)`. Consequently the layer counts are exactly

\[
L_0=|G|,\qquad
L_1=|G|k(G)-|G|,\qquad
L_2=|G|^2-|G|k(G). \tag{D1}
\]

The maximum-depth boundary is also correct:

- trivial group: depth zero only;
- nontrivial abelian odd group: maximum depth one;
- nonabelian odd class-two group: a noncommuting pair exists, hence maximum
  depth two.

Again, (D1) is aggregate bookkeeping once (B1) is known. It does not classify
the isomorphism types of the in-trees attached to individual cycles.

### E. Periods, fixed points, and zeta: passes modulo typo and claim scope

On the diagonal, the exact period of `(g,g)` is the least positive `m` with
`g^{2^m}=g`, namely

\[
\operatorname{ord}_{\operatorname{ord}(g)}(2). \tag{E1}
\]

All fixed points of positive iterates are recurrent, so

\[
|\operatorname{Fix}(\Phi^m)|
=|\{g\in G:g^{2^m-1}=1\}|. \tag{E2}
\]

The report's displayed equation (12) currently contains the malformed token
`g^{,2^m-1}`. This is a typesetting defect, not a mathematical counterexample,
but it must be fixed in any reusable version.

If `exp(G)=p` is an odd prime and `o=ord_p(2)`, identity is the sole fixed
cycle and every nonidentity element lies in an `o`-cycle. Thus

\[
\zeta_\Phi(t)=(1-t)^{-1}(1-t^o)^{-(|G|-1)/o}. \tag{E3}
\]

This is correct. It is also entirely standard power-map orbit and
Artin--Mazur conversion; it adds no independent theorem weight.

## Round 2: verifier audit

The supplied verifier was rerun byte-for-byte against the canonical output:

```text
GROUP PRODUCT-EXCHANGE EXACT CONTROL: PASS
assertions=320848
```

The full stdout diff was empty. SHA-256 at review time:

- verifier: `a7f91fbb2e249f990bcefba44e0fec1df505828230a358abe052130485cf543e`;
- canonical stdout: `520140bd8aa4fbcb74eb47238750674b644804840e5b3b009d2ff6d2b009e020`.

### What it genuinely checks

- group identities on `S_3`, `C_3`, `C_9`, `H_3`, `H_5`, and
  `H_3 x C_3`;
- every one-step fibre for every target in those groups;
- literal two-step diagonal collapse in the flagged odd class-two groups;
- every diagonal two-step fibre and iterated fibres through `t=7`;
- all depth states and fixed points through `t=8`;
- a negative-scope `S_3` lane for Theorem 1.

The reported assertion total and all canonical tables reproduce.

### Boundaries and wording that must not be overstated

1. `class_two_odd` is a constructor flag. The script checks centrality of
   commutators only on a deterministic sample, not on every triple in the
   larger groups. Likewise associativity is sampled for larger groups.
   Therefore the report's phrase “class two is checked directly” should be
   qualified as “checked on a deterministic sample” unless the loops are
   made exhaustive.
2. There is no even class-two negative control and no odd class-three negative
   control. These are useful falsification boundaries if the result is ever
   generalized.
3. The nonabelian tests have exponent `3` or `5`; `C_9` tests higher odd
   exponent only in the abelian lane. A nonabelian odd class-two group of
   exponent `9` would be a better power-map boundary control.
4. The verifier validates formulas, not ownership or paper value. Its large
   assertion count does not enlarge the theorem.

These limitations do not undermine the symbolic proof, but they matter to
the evidence wording.

## Owner subtraction

### Boffa--Point 1991: identity engine, zero credit

M. Boffa and F. Point, *Identités de Thue--Morse dans les groupes*,
**C. R. Acad. Sci. Paris Sér. I 312** (1991), 667--670, define the recursive
Thue--Morse identities

\[
I_0(x,y):x=y,\qquad I_{n+1}(x,y):I_n(xy,yx),
\]

and characterize the finite groups satisfying such an identity. The exact
recursion is the candidate dynamics. The words, the identity interpretation,
and class-two `I_2` therefore receive zero credit, as required by this gate.

The original four-page paper was not available as machine-readable full text
through the current bounded network pass. Its theorem and bibliographic data
were cross-checked against the published literature, including the explicit
Boffa--Point theorem statement in Allouche--Shallit's survey. This access
limitation is not used to make an absence claim.

### Almeida 2003: direct dynamical framing owner

Jorge Almeida, “Profinite structures and dynamics,” **CIM Bulletin 14**
(2003), 8--18, is a closer owner than the author report records. The official
[author publication record](https://cmup.fc.up.pt/cmup/jalmeida/) identifies
the publication, and the official
[CIM index](https://www.cim.pt/magazines/search?mag_term1=Article&magazine_id=1&options_1=category)
records the issue, date, and author.

Almeida explicitly studies iteration of implicit operators on finite groups,
names `(x,y) -> (xy,yx)` the “Thue--Morse operator,” and displays functional-
graph visualizations for this exact operator on `Z/70Z`, a wreath product,
and `A_6`; the coloring records distance to cycle and cycle identity. This
source does not, in the inspected text, state the candidate's centralizer
fibre formula or odd class-two census. It nevertheless directly owns the map,
the finite-group dynamical interpretation, and functional-graph viewpoint.

This source materially changes the hostile gate: the candidate is not merely
using a known word identity as input; it is refining an already explicitly
studied finite-group dynamical operator.

### Zero-credit standard ingredients

Even without a direct paper stating the residual conjunction, the following
cannot count toward novelty:

- conjugacy classes and centralizer cosets;
- `|G|k(G)` commuting-pair enumeration;
- bijectivity of power maps coprime to `exp(G)`;
- multiplicative orders and cycle counts for `g -> g^2`;
- Artin--Mazur fixed-point/zeta conversion.

A bounded exact-string search found no primary source stating formulas
(2), (8), and (10) together. That no-hit is not a novelty certificate and
does not overcome the direct identity/dynamics owners.

## Internal collision audit

### C12: same literal mechanism, not merely a neighbor

C12 was defined on matrix pairs by the identical rule

\[
(A,B)\mapsto(AB,BA).
\]

The present group system is a restriction of that product-exchange mechanism
to a group carrier; for matrix groups such as finite Heisenberg groups it is
literally a closed sublane of C12. The class-two theorem is legitimate
progress on the reserve, but it must not be counted as a fifth unrelated
mechanism or as a fresh system discovery.

### P119: severe narrative/package collision

P119 studies a deterministic finite-group map with an owned structural image
theorem and retains exact finite fibres, all iterated fibres, depth layers,
predecessor census, recurrence, and zeta as the residual package. The present
candidate repeats almost exactly that narrative architecture:

```text
owned group identity/collapse
    -> uniform exact fibres
    -> exact layers
    -> recurrent census and zeta.
```

The literal maps differ—P119 is a fixed regular Engel/commutator map on
unitriangular groups, while this is the Thue--Morse product operator—but the
internal portfolio collision is strong. P119 also has a richer filtration-
typed predecessor census and a nonregular boundary guard. The current
candidate is weaker after owner subtraction.

### P111: no literal collision, but carrier/topic crowding

P111 is probabilistic: positive Heisenberg word products encode chronological
area and support exact biased laws, limit theorems, norm exponents, and rare-
event pressure. It is not this deterministic pair map. There is no theorem
collision.

However, using `H_p` as the headline example would create another
Heisenberg/product paper in the same sequence. Since the general theorem does
not need Heisenberg coordinates, this carrier overlap supplies no value and
increases portfolio crowding.

## Paper-scale judgment

Once all zero-credit inputs are removed, the actual proof burden is roughly:

1. substitute `y=x^{-1}a` to obtain a conjugator fibre;
2. invoke owned `I_2` collapse;
3. observe that powers of two are invertible modulo the odd exponent;
4. count commuting pairs and cycles of a power permutation.

There is no new invariant, no parameterized transient beyond the owned fixed
depth two, no nontrivial recurrent stratum beyond a standard power map, and no
new proof technology. The phrase “exact all-iterate fibres” is formally true
but hides that all later iterates differ only by postcomposition with a
permutation. The conjunction does not create paper-scale depth.

Score after subtraction:

- correctness: **8/10** (one typo and evidence-wording limits, no core flaw);
- direct-owner safety: **2/10**;
- residual technical depth: **2/10**;
- internal distinctiveness: **2/10**;
- standalone short-paper value: **2/10**.

## Mandatory corrections if archived or reused

These do not change the kill verdict:

1. Fix equation (12) from `g^{,2^m-1}` to `g^{2^m-1}`.
2. Add Almeida 2003 as a direct map/dynamics owner and prohibit “new
   product-exchange dynamics” wording.
3. Replace “full functional graph” by “pointwise one-step indegrees plus
   aggregate depth/cycle census,” unless rooted in-tree attachments are
   actually classified.
4. State explicitly
   `Phi^t(x,y)=(r^{2^{t-2}},r^{2^{t-2}})` for `t>=2`; this makes the
   all-iterate proof transparent and prevents novelty inflation.
5. Qualify the verifier's associativity/class-two checks as sampled on the
   larger formula-defined groups, or make them exhaustive.
6. Keep `HOLD_EXTERNAL`; a search no-hit for the exact residual conjunction
   is not a priority conclusion.

## Re-entry threshold

Do not reopen the current odd class-two path merely to add more examples,
tables, zeta expansions, or higher verifier counts. Re-entry requires a
qualitatively stronger theorem, such as:

- exact fibre/depth structure for a nontrivial all-class family beyond class
  two, where the collapse time and fibre sizes are not predetermined by one
  owned identity;
- a classification of the rooted in-tree isomorphism types and their
  attachments, not only layer totals;
- an extension to a genuinely broader semigroup/matrix family that resolves
  C12's rank-stable dynamics rather than restricting to a group lane; or
- a new invariant that controls the pre-`I_n` dynamics for arbitrary
  nilpotency class.

Without one of these, the candidate remains **KILL_AS_STANDALONE**.
