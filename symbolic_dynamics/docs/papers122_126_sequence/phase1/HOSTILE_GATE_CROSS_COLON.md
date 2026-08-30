# Independent hostile owner/value gate: cross-colon monomial-ideal dynamics

**Audit date:** 2026-08-30 UTC  
**Object audited:** `proof_spikes/ALG_CROSS_COLON_REPORT.md`, its independent
verifier and canonical output, the relevant P1--P121 internal records, and the
primary owner neighborhood for disjunctive Boolean networks, monomial colons,
and rowmotion/toggles.  
**Posture:** fail-closed. A correct theorem is not by itself a paper-scale
residual after direct-owner and internal-collision subtraction.

## Executive decision

**REWRITE / NO PAPER FREEZE / HOLD_EXTERNAL.**

The literal operator and the all-parameter theorem survive the mathematical
audit. In particular, the diagonal decomposition, recurrent-ideal
classification, count `3 min(a,b)-2`, and rectangular-versus-square maximum
depth formula are correct. The verifier is unusually strong and reproduces
its canonical output exactly.

That mathematical pass does **not** produce a present paper-scale pass. The
no-source OR-path recurrence, period at most two, and transient-height
mechanism belong to established disjunctive-network theory. The one- and
two-source path cases are fixed-source/augmented-graph specializations whose
fill times are elementary distance calculations. I therefore assign **zero
novelty credit to every path periodicity and path-depth result**, including
the numerical ingredients from which the global depth maximum is taken.

After that subtraction, the real residual is:

1. the exact conversion of the crossed-colon operator into sourced OR paths
   on total-degree diagonals;
2. the non-product compatibility argument imposed by the monomial upper-set
   condition, yielding precisely the power and checker-boundary recurrent
   ideals and hence the `3m-2` census; and
3. the observation that the one-source band exists exactly off the square,
   which translates owned path heights into the stated square depth anomaly.

Items 1--2 are genuine and no direct literal owner was located. Item 3 is a
clean algebraic/geometric translation but, after OR-height subtraction, is
mostly downstream bookkeeping. Taken together they are **borderline rather
than sufficient**, especially because P107 already uses the internal story
“ideal operator + fixed/two-cycles + exact transient depth” and has a richer
fibre/CDF/zeta package. The candidate is not killed: one nonmechanical,
all-parameter enumerative increment can repair it.

## Severity ledger

| issue | severity | finding | consequence |
|---|---:|---|---|
| Literal operator and staircase update | pass | exact, including `a=1` or `b=1` | theorem remains alive |
| Diagonal OR decomposition | pass | exact conjugacy on the invariant monomial-ideal state space | defensible residual, but OR dynamics themselves are owned |
| Recurrent-ideal classification | pass | upper-set compatibility forces powers and checker boundaries | strongest current residual |
| Sharp depth theorem | pass mathematically / severe owner subtraction | maximum and witnesses are correct, but component heights are established OR/walk phenomena | square law may be claimed only as a translation for this operator |
| Definition paragraph for `C_r^epsilon` | **minor mathematical wording error** | a claimed full-shadow covering is false in one checker phase | must be corrected before any manuscript freeze |
| Direct colon-dynamics owner | bounded no direct hit | no exact operator or theorem found | not a novelty certificate |
| P107 collision | medium/high value pressure | no literal collision, but same narrative skeleton | an additional exact output is mandatory |
| Present paper-scale value | insufficient | residual is coherent but too thin after zero-credit subtraction | **REWRITE** |

## 1. Literal operator audit

Let

\[
R_{a,b}=k[x,y]/(x^a,y^b),\qquad
T(I)=x(I:y)+y(I:x)
\]

on monomial ideals only. Represent `I` by its upper set in the exponent
rectangle and by thresholds

\[
b\ge h_0\ge h_1\ge\cdots\ge h_{a-1}\ge0,
\qquad x^iy^j\in I\Longleftrightarrow j\ge h_i.
\]

The dossier's literal calculation is correct:

- `(I:y)` has row threshold `max(h_i-1,0)` because the top row in the
  `y` direction is killed by `y`;
- multiplication by `x` shifts those thresholds one column and kills the
  last source column;
- `(I:x)` uses the next column threshold, with the last column included
  because `x^a=0`;
- multiplication by `y` raises the threshold with clipping at `b`; and
- the sum of two monomial ideals takes the coordinatewise minimum of their
  staircase thresholds.

This gives the displayed staircase update in the dossier. The formula also
handles the degenerate strips `a=1` and `b=1`; no hidden assumption that both
side lengths exceed one is used. Since colons, multiplication, and sums of
monomial ideals are monomial, the stated state space is invariant. The result
does not depend on the characteristic or cardinality of `k`.

The scope restriction is binding: nothing here classifies the action on
nonmonomial ideals.

## 2. Total-degree network decomposition

On a fixed total-degree diagonal, a cell `(i,j)` is present after one update
exactly when one of its two diagonal neighbors was present before the update,
with a constant `1` supplied when the relevant predecessor lies just beyond a
nilpotent wall. Thus the diagonal word evolves by

\[
(Gw)_s=w_{s-1}\lor w_{s+1}
\]

with left/right boundary sources. The rectangle divides exactly as claimed:

| degree range | word length | sources |
|---|---:|---:|
| `0 <= d < m` | `d+1` | none |
| `m <= d < M` | `m` | exactly one |
| `M <= d <= a+b-2` | `a+b-1-d` | two |

where `m=min(a,b)` and `M=max(a,b)`. The middle range is empty precisely
when `a=b`. Because an update never mixes total degrees, this is a literal
coordinate decomposition, not an analogy.

The mechanical-translation risk begins immediately after this point. The
path maps are standard disjunctive Boolean networks. Constant sources can be
represented by adjoining fixed-one source vertices, or treated directly as
affine boundary inputs; thereafter an iterate is determined by walk
reachability. Hence source filling times are graph distances, and the
no-source behavior is the bipartite parity structure of a path.

## 3. Path lemma: correct, but zero credit

The dossier's four path claims are correct.

- A no-source one-vertex path has recurrent word `0` and maximum depth one.
- A no-source path of length at least two has exactly the two parity-constant
  fixed words and the two alternating phases; its maximum depth is `n-2`.
- A one-source path has unique recurrent word `1^n` and maximum depth `n`.
- A two-source path has unique recurrent word `1^n` and maximum depth
  `ceil(n/2)`.

The witnesses and endpoint cases check out. Nevertheless, none of these is
available as a novelty-bearing theorem. Goles and Hernández give a direct
classification of synchronous OR networks on finite connected undirected
graphs, including fixed/periodic states, basins, and transient behavior in
[Dynamical Behavior of Kauffman Networks with AND-OR Gates](https://doi.org/10.1142/S0218339000000109).
Jarrah, Laubenbacher, and Veliz-Cuba formulate conjunctive/disjunctive
networks through dependency graphs and Boolean matrices and relate height and
period to graph invariants in
[The Dynamics of Conjunctive and Disjunctive Boolean Networks](https://doi.org/10.1007/s11538-010-9501-z).
Gadouleau's primary survey/research article confirms that periodic points,
images, fixed points, and transients are established parts of the
disjunctive-network literature in
[Dynamical properties of disjunctive Boolean networks](https://doi.org/10.4230/OASIcs.AUTOMATA.2021.1).

The exact sourced-path numbers need no stronger ownership assertion to lose
credit: once a fixed source is added, they are immediate distance-to-source
calculations in the same walk semantics. A future draft must cite the direct
Goles--Hernández owner, not only later general treatments.

## 4. Recurrent monomial ideals

This is the strongest surviving theorem component. Diagonal recurrence alone
would allow a Cartesian product of many parity phases. The upper-set
condition couples adjacent diagonals and removes almost all of them.

The compatibility argument is sound:

1. all diagonals in the one- or two-source region are eventually and
   recurrently all one;
2. in the no-source region, a recurrent word is zero, all one, or one of two
   checker phases;
3. the upward shadow of an all-one word is all one;
4. the shadow of a checker word contains adjacent occupied positions, while
   no non-all-one recurrent no-source word contains such a pair; therefore
   the next recurrent diagonal must be all one; and
5. once a first nonzero diagonal occurs, every higher diagonal is all one.

Consequently the recurrent ideals are exactly

\[
\mathfrak m^r\quad(1\le r\le m),
\qquad
C_r^0,C_r^1\quad(1\le r<m).
\]

The `m` power ideals are fixed. For each `1<=r<m`, the two checker ideals
form one two-cycle. Therefore the exact counts are

\[
\#\operatorname{Fix}(T)=m,
\qquad
\#\{\text{two-cycles}\}=m-1,
\qquad
\#\operatorname{Rec}(T)=3m-2,
\]

with no longer periods. I found no missing recurrent boundary family at
`m=1`, and the classifications remain consistent when one side of the ring
has length one.

### Required local correction

The paragraph immediately following the definition of `C_r^epsilon` says
that the upward successors of the alternating selected degree-`r` positions
cover the whole degree-`r+1` diagonal. That statement is false for one phase
at an endpoint. For example, at `r=1`, selecting only position `i=0` shadows
positions `0,1` on degree two but not position `2`.

This does **not** invalidate the ideal definition or later classification:
all monomials of degree greater than `r` are explicitly included in
`C_r^epsilon`, so the displayed set is upward closed by definition; and the
later proof needs only that the checker shadow contains two adjacent occupied
positions. The explanatory sentence must nevertheless be removed or replaced
before a paper freeze. Severity: **minor, mandatory repair**.

## 5. Global depth and the square anomaly

Because diagonal projections commute with `T`, entrance into the recurrent
set occurs at the maximum of the diagonal entrance times. Combining the
correct path maxima gives

\[
D(a,b)=
\begin{cases}
m,&a\ne b,\\
\max(1,m-2),&a=b=m.
\end{cases}
\]

The sharp witnesses in the dossier are valid:

- off the square, the zero word on a longest one-source diagonal takes `m`
  steps to fill;
- on a square with `m>=3`, the no-source diagonal of length `m` supplies a
  depth-`m-2` witness compatible with an upper set; and
- the `m=1,2` exceptions have depth one.

The “square anomaly” is therefore real, not a numerical artifact: the
length-`m` one-source band exists exactly when `a != b` and disappears on the
square.

Its **claim value is limited**, however. The component height formulas are
owned/background, and the global maximum is the maximum over the displayed
diagonal table. What remains is the identification of which band the
cross-colon geometry supplies. It is a clean corollary of the algebraic
conjugacy, not an independent second proof engine.

## 6. Mechanical verification

I reran the verifier independently. Its fresh stdout is byte-identical to
`ALG_CROSS_COLON_CANONICAL.txt` and has SHA-256

`b924e05c5e9ac71a25fb668d5bc2033f6ab58c325c7c73642a4dd0b096d67deb`.

The run reports:

- `1,469,669` assertions;
- every path word of lengths `1..14` for all four source types, totaling
  `131,064` path cases;
- all `184,736` monomial ideals in the `81` rectangles `1<=a,b<=9`;
- literal basis arithmetic against both staircase and diagonal updates;
- exact fixed/two-cycle/recurrent-family classification; and
- sharp maximum depths and witnesses.

This is strong bounded falsification evidence. It does not establish novelty
or replace the all-parameter proof.

## 7. Owner subtraction outside OR networks

### 7.1 Monomial colons

Monomial ideals, exponent staircases, order filters, and the fact that
monomial colons remain monomial are classical and receive zero credit.
Ambhore and Sengupta study static colon representations associated with
monomial ideals in
[Colon Structure of Associated Primes of Monomial Ideals](https://doi.org/10.1142/S1005386724000336).
That work is not a dynamics owner.

Targeted searches for the exact expressions `x(I:y)+y(I:x)` and their
obvious reversed-variable variants did not locate the literal self-map, its
diagonal conjugacy, its recurrent census, or its square law. The only honest
status is **BOUNDED_NO_DIRECT_HIT**. It must not be converted into “first,”
“new,” or priority language without specialist clearance.

### 7.2 Rowmotion and toggles

The state space is the set of upper sets of a product of two chains, so
rowmotion, promotion, files, and toggles are unavoidable neighbors. Striker
and Williams establish the promotion/rowmotion framework and toggle
conjugacies in
[Promotion and rowmotion](https://doi.org/10.1016/j.ejc.2012.05.003).
Einstein and Propp treat the two-chain/product setting and its homomesies in
[Combinatorial, piecewise-linear, and birational homomesy for products of two chains](https://doi.org/10.5802/alco.139).

There is no literal or conjugate collision. Rowmotion and any composition of
toggles are bijections on a finite state set; the cross-colon map has
transients for every rectangle. Classical rectangular rowmotion has order
tied to the side lengths, whereas every recurrent cross-colon orbit has
period at most two. The simultaneous neighbor-OR update is not a sequential
toggle product. All generic order-ideal, file, and toggle language remains
zero credit, and a future manuscript should include this bijection-versus-
transient firewall.

## 8. Internal P1--P121 collision audit

No prior numbered paper uses the literal crossed-colon operator or its
total-degree OR decomposition. The material is therefore not an exact
internal duplicate.

P107 is the decisive value collision. It studies
`I -> Ann(I)^r` on all ideals of `Z/NZ`, reduces the dynamics to primewise
clipped reflections, and derives fixed/two-cycle structure, exact transient
data, fibres/CDFs, and zeta information. Cross-colon dynamics differ
mechanistically:

| P107 | cross-colon candidate |
|---|---|
| ideals of a residue ring | monomial ideals of a truncated bivariate ring |
| annihilator followed by a power | sum of two crossed variable-colon terms |
| CRT/valuation coordinates | total-degree Boolean coordinates |
| clipped expanding reflection | sourced neighbor-OR propagation |
| arithmetic/logarithmic clocks | geometric linear distances and a missing square band |

This defeats literal collision but not narrative collision. The candidate
cannot claim “first ideal-operator dynamics,” and its present census plus
maximum depth is thinner than P107's finished package. The internally scouted
rowmotion variants and the monomial-matrix “toggle contraction” item are only
adjacent by state-space vocabulary; neither is the same map.

## 9. Owned/residual ledger

| component | credit assignment |
|---|---|
| monomial ideals as rectangle upper sets; colon staircases | **zero credit / standard** |
| disjunctive Boolean network representation by graphs or Boolean matrices | **zero credit / owned** |
| OR-path recurrent words, period at most two, transient heights | **zero credit / owned** |
| fixed boundary sources and their fill times | **zero credit / immediate walk-distance specialization** |
| exact crossed-colon-to-diagonal formula | **residual, subject to specialist clearance** |
| compatibility of recurrent diagonal phases with upper sets | **residual and substantive** |
| power/checker recurrent families and `3m-2` census | **residual consequence of compatibility** |
| square-versus-rectangle maximum-depth law | **low residual credit: operator-specific geometric translation of owned heights** |
| rowmotion/toggle comparison | **firewall only, no novelty credit** |
| exact-string search miss | **no positive credit** |

## 10. Minimum repair required for a paper-scale GO

Correcting the checker-shadow sentence is necessary but not enough. Before
paper assignment, the dossier must add **at least one genuinely new,
all-parameter theorem not obtained merely by substituting known path heights
into the diagonal table**. The minimum acceptable increment is one of:

1. an exact depth enumerator
   `H_{a,b}(q)=sum_{I in M_{a,b}} q^{depth(I)}` with a proved uniform closed
   form, rational generating function, or finite transfer recurrence that
   yields explicit coefficients—not merely brute-force dynamic programming;
   or
2. exact basin or iterated-fibre cardinalities for every fixed ideal and
   every checker two-cycle, uniformly in `a,b`, with the upper-set coupling
   handled explicitly.

A bounded table, a restatement of path-distance maxima, another witness for
the same maximum, or a generic algorithm with state space growing as all
ideals does **not** satisfy this increment. The new theorem must have an
all-parameter proof and an independent literal verifier. A direct colon-
dynamics specialist search must then be repeated around the specific new
quantity.

If neither increment closes, the item should be killed rather than promoted
on the square anomaly alone. If one closes and survives owner subtraction,
the candidate may return to a fresh hostile gate.

## Binding claim ceiling

The strongest presently allowed internal statement is:

> For the specific synchronous map `I -> x(I:y)+y(I:x)` on monomial ideals
> of `k[x,y]/(x^a,y^b)`, total-degree coordinates realize sourced
> disjunctive path networks. Compatibility with the monomial upper-set
> condition yields exactly the power and checker-boundary recurrent ideals,
> hence `m` fixed ideals, `m-1` two-cycles, and `3m-2` recurrent states. The
> rectangle geometry translates the established path heights into the stated
> sharp square/non-square maximum-depth law.

Forbidden without further evidence:

- “first colon-ideal dynamics” or any priority claim;
- “new OR-path dynamics,” a new period-two mechanism, or novelty credit for
  the path depth formulas;
- “new rowmotion/toggle action”;
- extension from monomial ideals to all ideals;
- presenting the exact-string search miss as a novelty certificate; or
- suppressing the P107 narrative collision.

## Final gate

**Mathematical theorem:** PASS, subject to one minor wording correction.  
**Mechanical evidence:** PASS, `1,469,669` assertions and byte-identical
canonical output.  
**Direct-owner status:** OR mechanism owned; literal colon conjugacy and
upper-set census only `BOUNDED_NO_DIRECT_HIT`.  
**Short-paper value:** FAIL at the current output level.  
**Decision:** **REWRITE / NO PAPER FREEZE / HOLD_EXTERNAL**.  

The item is repairable, not dead. Its route to GO is an exact all-depth or
basin/fibre theorem that genuinely uses the coupled upper-set geometry; the
already correct square anomaly is not by itself enough after full OR-network
subtraction.

---

## Re-entry audit after the minimum value repair

**Re-entry date:** 2026-08-30 UTC.  This section supersedes the pre-repair
value verdict above; the owner subtraction and external hold remain binding.

### Repairs inspected

1. **Checker-shadow wording: resolved.**  The false claim that every checker
   phase shadows the whole next diagonal has been replaced.  The dossier now
   says exactly what is true: the displayed checker family is upward closed
   because every higher-degree monomial is explicitly present, and its shadow
   contains the adjacent occupied pair needed later.  No theorem statement
   changed.

2. **New basin theorem: proved.**  For a nonzero ideal, let $\nu(I)$ be its
   first occupied total degree and let $S_{\nu(I)}(I)$ be its trace there.
   The amended dossier proves the following complete attractor partition:

   - $\nu(I)=r<m$ and a mixed-parity first trace lead to the fixed power
     $\mathfrak m^r$;
   - a one-parity first trace leads to the checker orbit
     $\{C_r^0,C_r^1\}$, with the eventual phase explicitly determined by
     time parity;
   - $\nu(I)\geq m$, including the zero ideal, leads to $\mathfrak m^m$;
   - the unit ideal maps to $\mathfrak m$; and
   - when $m=1$, every ideal lies in the unique fixed basin.

   This is stronger than a list of recurrent states: it characterizes the
   basin of every fixed point and every two-cycle.

3. **Uniform basin counts: proved by a four-state transfer.**  The staircase
   of an ideal is encoded by an east/south boundary path.  For each
   $1\leq r<m$, the transfer records whether contacts with $i+j=r$ occur at
   no parity, even only, odd only, or both.  The recurrence has
   $4(a+1)(b+1)$ entries for a fixed $r$ and counts all basins in
   $O(abm)$ arithmetic operations over the whole rectangle family; it does
   not iterate through the $\binom{a+b}{a}$ ideals.

   If $A_r^E,A_r^O,A_r^M$ are the even-only, odd-only, and mixed contact
   counts, the exact basin sizes are

   $$
   \begin{aligned}
   |\mathcal B(\{\mathfrak m\})|&=1+A_1^M=2,\\
   |\mathcal B(\{\mathfrak m^r\})|&=A_r^M
      &&(2\leq r<m),\\
   |\mathcal B(\{C_r^0,C_r^1\})|&=A_r^E+A_r^O
      &&(1\leq r<m),\\
   |\mathcal B(\{\mathfrak m^m\})|
      &=\binom{a+b}{a}-\binom{a+b}{m-1}.
   \end{aligned}
   $$

   The reflection check

   $$
   A_r^E+A_r^O+A_r^M
   =\binom{a+b}{r}-\binom{a+b}{r-1}
   $$

   and the total-basin partition give independent global controls.  The last
   fixed basin therefore has a ballot-number closed form, while every other
   basin has a uniform finite contact recurrence.

### Correctness re-audit

The new argument has two independent layers.

- Dynamically, the first nonzero no-source diagonal eventually becomes a
  checker phase if its support occupies one bipartite class and becomes all
  one if it occupies both.  The already proved upper-set compatibility then
  determines the unique whole-ideal attractor.  This handles the zero ideal,
  unit ideal, $m=1$, and $r=1$ boundary cases separately.
- Enumeratively, the staircase/path bijection converts
  $\nu(I)\geq r$ to the barrier constraint $i+j\geq r$.  Contacts are exactly
  occupied degree-$r$ positions, so their abscissa parity is exactly the
  first-trace parity.  The four-state recurrence is an ordinary last-step
  recurrence.  Reflection of the associated height walk proves the ballot
  formulas and the total partition.

I found no quantifier gap or double-counting.  In particular, a checker basin
is counted as the basin of the two-cycle, which is the standard deterministic
basin notion; the two separate contact counts additionally retain the
eventual phase information.

### New independent mechanical control

The new verifier
proof_spikes/verify_alg_cross_colon_basins.py does not import the old
verifier.  It constructs the operator by literal monomial colon and
multiplication, follows every orbit in all $64$ boxes $1\leq a,b\leq8$, and
compares all $48,602$ ideal attractors with the first-trace theorem.  It then
compares the four-state transfer with every exhaustive basin count and checks
ballot, partition, and transpose-symmetry identities through
$1\leq a,b\leq30$.

Its fresh stdout is byte-identical to
proof_spikes/ALG_CROSS_COLON_BASINS_CANONICAL.txt:

    cross-colon basin transfer independent control: PASS
    assertions=265987
    literal_rectangles=64; parameter_grid=a,b=1..8; ideals=48602
    literal_attractors_vs_first_trace=PASS
    contact_transfer_vs_exhaustive_basins=PASS
    ballot_partition_and_swap_identities=PASS
    large_transfer_grid=a,b=1..30; nontrivial_triples=8555
    example_a5_b7_orbit_basins=[(('C', 1), 10), (('C', 2), 45), (('C', 3), 116), (('C', 4), 185), (('P', 1), 2), (('P', 2), 9), (('P', 3), 38), (('P', 4), 90), (('P', 5), 297)]
    example_a5_b7_trace_phases=[(1, (4, 6, 1)), (2, (30, 15, 9)), (3, (44, 72, 38)), (4, (139, 46, 90))]

The canonical SHA-256 is
bdfd3e041b9f641101436c40918adbba59fd14b1f1381d77fa943ce00c0c76ff.
The original $1,469,669$-assertion verifier also remains byte-identical to
its canonical output, so there is no theorem regression.

### Re-entry owner/value subtraction

The new theorem does not reclaim any OR-path credit.  Goles--Hernández,
Jarrah--Laubenbacher--Veliz-Cuba, and Gadouleau still own the surrounding
disjunctive-network mechanism.  Lattice-path encoding, four-state transfer,
and reflection are also classical tools and receive zero method credit.
Generic algebraic algorithms for Boolean-network basins, including
[Monomials and Basin Cylinders for Network Dynamics](https://doi.org/10.1137/140975929),
do not study this state space, literal colon operator, first-trace partition,
or contact-parity basin counts.

A fresh targeted search for the literal operator combined with “basin,”
“attractor,” “monomial ideal,” and “truncated polynomial ring” again found no
direct statement of the operator, basin partition, or transfer.  The result
remains **BOUNDED_NO_DIRECT_HIT**, not a priority certificate.  P107 remains
a narrative neighbor, but the repair answers the earlier asymmetry: C6 now
has an exact basin package, and its first-diagonal/contact-parity mechanism is
not the CRT valuation mechanism of P107.

The increment passes the previous minimum for a specific reason.  Basin
membership is not a componentwise OR-path statistic: diagonal states must be
traces of one upper set.  The first-trace theorem and contact automaton solve
that coupling globally and uniformly.  This is a second paper-scale output
beyond the recurrent census and maximum depth, not another witness for the
same owned path height.

### Revised binding claim ceiling

The earlier ceiling is expanded only by the following residual:

> For the literal cross-colon map, the first occupied diagonal and the parity
> support of its trace determine the complete attractor basin.  Rectangle
> staircase paths with a four-state contact-parity transfer give every fixed
> and checker-cycle basin size uniformly in $a,b$, including a ballot closed
> form for the terminal fixed basin.

All earlier prohibitions remain in force: no “first” claim, no novelty credit
for OR periodicity/heights or lattice-path reflection, no rowmotion/toggle
claim, and no extension to nonmonomial ideals.

### Re-entry verdict

**GO_INTERNAL / HOLD_EXTERNAL.**

The mandatory local correction is complete; the new all-parameter basin
theorem, proof, finite transfer, closed ballot component, and independent
literal verification meet the minimum value repair without lowering the
standard.  C6 may re-enter internal paper selection on the restricted claim
ceiling above.  External circulation remains on hold pending specialist
clearance of the literal colon operator and its basin theorem.
