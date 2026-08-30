# Independent hostile owner/value gate: odd-component graph complementation

**Audit date:** 2026-08-30.

**Object audited:** the proof spike
COMB_ODD_COMPONENT_COMPLEMENT_REPORT.md, its exact verifier and canonical
output, the earlier combinatorial scout, the P1--P121 internal record, and the
primary/official source neighborhood around cographs, modular decomposition,
cotrees, labelled cograph enumeration, and graph complementation.

## Decision

**Gate verdict: GO.**

More precisely:

- **internal status:** GO_INTERNAL at the narrow claim ceiling below;
- **external status:** HOLD_EXTERNAL;
- **mathematical status:** the stated structural theorem, sharp depth, and
  all-depth labelled recursion are correct;
- **owner status:** no direct owner of the literal parity-triggered self-map
  was found in the bounded audit;
- **value status:** the surviving conjunction has two paper-scale outputs:
  exact finite dynamics with a sharp transient clock, and an exact labelled
  census of every transient layer.

This is not a GO for cotrees, component/co-component recursion, graph
complementation, or labelled SET calculus.  Those are classical and receive
zero contribution credit.  The GO is only for the new scheduler-specific
conjunction.

The residual is thin enough that contribution language must remain exact.
Calling the construction a new cograph decomposition, a new cotree, or a new
graph-enumeration method would reverse this verdict.

## 1. Literal map reconstructed independently

For a finite labelled simple graph \(G\), let \(\Phi(G)\) be obtained
synchronously as follows:

1. compute the connected components of the current graph;
2. for each component of odd vertex order, toggle every edge inside that
   component;
3. leave every even-order component unchanged.

No cross-component edge is toggled.  Hence the component partition at time
\(j+1\) refines the partition at time \(j\).  On an odd connected component
\(H\), exactly one of two things occurs:

- if \(\overline H\) is connected, the component alternates
  \(H\leftrightarrow\overline H\);
- if \(\overline H\) is disconnected, it splits into the connected components
  of \(\overline H\), which can never merge again.

Even components freeze at once.  This reconstruction agrees with the report
and both implementations.

The parity trigger matters.  If every connected component were complemented
without the parity test, the construction would simply walk the familiar
component/co-component decomposition.  Freezing the even children while
continuing only the odd children is the only new mechanism.

## 2. Hostile theorem audit

### 2.1 Refinement, recurrence, and period

**PASS.**  Component refinement follows because \(\Phi\) never changes a
cross-component nonedge.  An odd component with connected complement is on a
two-cycle, while an odd component with disconnected complement undergoes a
strict refinement.  Since strict refinements cannot recur, every recurrent
component is either:

- an even connected component, fixed;
- a singleton, fixed; or
- an odd connected and co-connected component, on a two-cycle.

Therefore a graph is recurrent exactly when every nontrivial odd component is
co-connected.  It is fixed exactly when every component is a singleton or has
even order.  A nonfixed recurrent labelled graph is genuinely period two:
on a nontrivial fixed vertex set, no simple graph equals its edge complement
as the same labelled edge set.

There is no hidden lcm issue.  All nontrivial recurrent factors have period
two, so their synchronous product has period at most two.

### 2.2 Exact depth recursion

**PASS.**  Let \(D(H)\) be the preperiod of a connected odd graph.  If
\(\overline H\) is connected, \(D(H)=0\).  Otherwise

\[
D(H)=1+\max\{D(C): C\text{ is an odd connected component of }\overline H\},
\]

where the empty maximum is zero.  Even children make no further move and
therefore correctly disappear from the maximum.  For an arbitrary graph,
the preperiod is the maximum of \(D\) over its odd components.

This is an exact pointwise clock.  It is a parity-pruned
component/co-component decomposition prefix; it must not be advertised as a
new cotree for arbitrary graphs.

### 2.3 Global depth ceiling

**PASS.**  If an odd parent has order \(s\) and an odd child has order \(r\),
then \(s-r\) is positive and even, hence at least two.  Every active branch
therefore has at most

\[
\left\lfloor\frac{n-1}{2}\right\rfloor
\]

strict splits.

The witness family is correct.  With

\[
H_1=K_1,\qquad H_{2r+1}=\overline{H_{2r-1}\sqcup K_2},
\]

the graph \(H_{2r+1}\) is connected and its first image is
\(H_{2r-1}\sqcup K_2\).  Thus \(D(H_{2r+1})=r\).  Adding \(K_1\) gives the
even-order sharp witnesses.  This includes the boundary cases \(n=1,2\);
the theorem correctly states the bound only for \(n\geq1\).

### 2.4 Connected and co-connected atom count

**PASS, zero-credit derivation.**  For \(n\geq2\), a graph and its complement
cannot both be disconnected.  Complementation bijects disconnected graphs
with connected graphs whose complements are disconnected.  If \(c_n\) is the
connected labelled-graph count, the connected and co-connected count is

\[
q_n=2c_n-2^{\binom n2}.
\]

The exceptional convention \(q_1=1\) is stated explicitly and is consistent
with the dynamics.

### 2.5 All-depth EGF recursion

**PASS.**  Let \(O_t\) count connected odd graphs of depth at most \(t\), and
let \(Q\) count connected co-connected odd atoms.  For a nonrecurrent
connected odd graph \(H\), its complement is a disconnected labelled SET of:

- unrestricted connected even components; and
- connected odd components of depth at most \(t-1\).

Deleting the empty and one-component SETs makes this alternative disjoint
from \(Q\).  Odd coefficient extraction then gives exactly

\[
O_t=Q+\operatorname{Odd}\!\left(
\exp(C_{\rm even}+O_{t-1})-1-C_{\rm even}-O_{t-1}
\right).
\]

Assembling arbitrary current components yields

\[
F_t=\exp(C_{\rm even}+O_t).
\]

Thus \(F_0\) counts recurrent graphs, \(F_t-F_{t-1}\) counts exact depth \(t\)
for \(t\geq1\), and

\[
F_{\rm fix}=\exp(x+C_{\rm even})
\]

counts fixed graphs.  There is no complement multiplicity: complementation
is a label-preserving bijection between each disconnected assembly and its
connected odd parent.

The formal power-series reading is essential.  No analytic convergence claim
is needed.

### 2.6 Independent coefficient stress test

**PASS.**  Recomputing connected labelled-graph counts from
\(2^{\binom n2}\), and then applying the report's SET recursion independently,
gives:

| \(n\) | \(F_0[n]\) | first \(t\) with \(F_t[n]=2^{\binom n2}\) |
|---:|---:|---:|
| 5 | 648 | 2 |
| 6 | 30,512 | 2 |
| 7 | 1,845,984 | 3 |
| 8 | 266,301,568 | 3 |
| 9 | 66,266,955,904 | 4 |
| 10 | 35,158,965,365,120 | 4 |

The stabilization depth is exactly
\(\lfloor(n-1)/2\rfloor\) through \(n=10\), consistent with the sharp family.
The \(n\leq6\) entries reproduce the exhaustive census.

## 3. Mechanical evidence and scope

The exact verifier
comb_odd_component_layers_verify.py was rerun in a fresh temporary directory.
Its output is byte-for-byte identical to the canonical file:

- SHA-256:
  03bafdf88fd5c2ffd83d67b94e7a764dd8482f89fee530a3af5c7583ee03be32;
- assertions: 67,758;
- exhaustive state space: every labelled graph for \(0\leq n\leq6\);
- verified: period ceiling, depth ceiling, connected/co-connected count, and
  all cumulative depth-layer assembly counts.

The earlier scout is a separate, broader control with 214,396 assertions.  It
also checks component refinement, the fixed criterion, the recurrent
criterion, fixed/recurrent assembly counts, and records maximum indegrees.

This distinction should be preserved in any later support document.  The
67,758-assertion verifier does not itself assert the fixed/recurrent criteria
or indegrees line by line; those checks are in the 214,396-assertion scout.
The proof report's phrase “independent exhaustive scout” is accurate only
when it refers to that earlier scout, not solely to the newer verifier.

No control character or malformed carriage-return sequence remains in the
current proof report.

## 4. Direct-owner history and subtraction

### 4.1 Modular decomposition

Tibor Gallai, *Transitiv orientierbare Graphen*, Acta Mathematica Academiae
Scientiarum Hungaricae 18 (1967), 25--66,
[DOI 10.1007/BF02020961](https://doi.org/10.1007/BF02020961), is the
foundational primary source for canonical modular decomposition.  Its
series/parallel/prime structure owns the general component/co-component
decomposition background.

Consequently, the following are **zero credit**:

- splitting a disconnected graph into connected components;
- splitting a graph with disconnected complement into co-components;
- stopping at connected and co-connected atoms;
- interpreting these steps as the series/parallel prefix of modular
  decomposition; and
- elementary height induction on such a tree.

### 4.2 Cographs and cotrees

D. G. Corneil, H. Lerchs, and L. Stewart Burlingham,
*Complement reducible graphs*, Discrete Applied Mathematics 3 (1981),
163--174,
[DOI 10.1016/0166-218X(81)90013-5](https://doi.org/10.1016/0166-218X(81)90013-5),
explicitly study graphs reducible by recursively complementing connected
subgraphs and prove a unique tree representation.

D. G. Corneil, Y. Perl, and L. K. Stewart,
*A linear recognition algorithm for cographs*, SIAM Journal on Computing 14
(1985), 926--934,
[DOI 10.1137/0214065](https://doi.org/10.1137/0214065), states the union and
complement closure and the unique cotree representation.

These papers directly own:

- recursive complementation language;
- union/join decomposition of cographs;
- cotrees and alternating union/complement levels; and
- structural conclusions obtained solely by traversing an ordinary cotree.

The current dynamics is defined on **all** labelled graphs, not merely
cographs.  A connected and co-connected odd graph is a recurrent atom rather
than an object decomposed further.  Therefore the literal scheduler is not
identical to cograph recognition or cotree construction.

### 4.3 Labelled cotree and species enumeration

Modern primary work such as Benedikt Stufler,
*Graphon convergence of random cographs*, Random Structures & Algorithms 59
(2021), 464--491,
[DOI 10.1002/rsa.21002](https://doi.org/10.1002/rsa.21002), and Frédérique
Bassino et al., *Random cographs: Brownian graphon limit and asymptotic degree
distribution*, Random Structures & Algorithms 60 (2022), 166--200,
[DOI 10.1002/rsa.21033](https://doi.org/10.1002/rsa.21033), explicitly use
labelled cotree encodings and symbolic/EGF methods.

Thus labelled SET assembly, parity extraction, recursive tree specifications,
and conversion of a specification into an EGF are **zero credit as methods**.
The residual is only the particular scheduler-defined sequence
\((F_t)_{t\geq0}\) and the fact that it enumerates temporal depth exactly.

### 4.4 Literal parity scheduler search

Targeted searches covered the phrases and variants:

- odd-order component complementation;
- complement every odd connected component;
- parity-scheduled graph complementation;
- iterative component/co-component splitting;
- component-wise graph complement dynamics;
- cotree height dynamics and height-restricted cograph enumeration; and
- subgraph complementation dynamics through the current 2026 index window.

No primary paper or official record was found defining the literal map
\(\Phi\), the recurrence criterion under this parity scheduler, its sharp
\(\lfloor(n-1)/2\rfloor\) preperiod, or its depth-layer EGFs.

This is a bounded direct-owner non-hit, not a novelty certificate.  Ordinary
subgraph complementation and local complementation are adjacent operations
but do not choose current connected components by their vertex-order parity
and do not induce this refinement-only dynamics.

## 5. Owned versus residual claim ledger

| Claim or device | Owner/value result | Credit |
|---|---|---|
| graph complementation is an involution | classical | zero |
| disconnected graph / disconnected complement exclusion | classical | zero |
| component and co-component decomposition | Gallai modular decomposition | zero |
| recursive complementation and cotrees for cographs | Corneil--Lerchs--Stewart Burlingham | zero |
| labelled SET and EGF translation | classical species machinery; used throughout cograph enumeration | zero |
| \(q_n=2c_n-2^{\binom n2}\) | elementary complement bijection | zero |
| literal odd-component scheduler on all labelled graphs | no direct owner found | residual |
| refinement-only orbit structure | scheduler-specific | residual |
| recurrent/fixed criteria and period ceiling two | scheduler-specific conjunction | residual |
| exact parity-pruned pointwise depth recursion | scheduler-specific | residual |
| sharp depth \(\lfloor(n-1)/2\rfloor\) and witness family | scheduler-specific, though elementary once decomposed | residual |
| \(O_t,F_t\) for every temporal depth | scheduler-specific census built by zero-credit SET machinery | principal residual |
| bounded \(n\leq6\) census | verification, not contribution | control only |

## 6. Internal P1--P121 collision audit

No literal prior-paper collision was found.

The nearest internal items are:

1. **P75**, which uses complement components of a defining graph to decompose
   recurrent components of a clique-automaton presentation.  It has no graph
   self-map, no parity scheduler, and no refinement clock.
2. **P117**, which flips odd binary runs synchronously.  It shares the broad
   pattern “parity-triggered independent components,” but its state space,
   component definition, survival mechanism, extremal proof, and census are
   different.
3. **P118**, which gives every depth layer for a multipartite mex network.
   This is a methodological resemblance only; neither its quotient map nor
   its fibres are graph complementation.
4. The P102--P106 scouting record contains a **cograph twin quotient** reserve,
   but it was not frozen as a P1--P121 paper and it is not the present map.

P75 prevents generic “complement components create recurrent decomposition”
language from being sold as new.  P117 prevents generic
“parity acts independently on components” language from carrying value.
Neither consumes the exact \(\Phi\)-theorem or its labelled depth recursion.

## 7. Value gate

### Why this clears GO

After full subtraction, two mutually supporting but nonidentical outputs
remain:

1. **Temporal structure:** a complete orbit classification, a pointwise clock,
   and a sharp all-\(n\) maximum preperiod with explicit witnesses.
2. **Temporal enumeration:** an exact recursive EGF for every cumulative and
   exact depth layer, not merely fixed points or bounded tables.

The second output is not a restatement of the first: it counts all labelled
fibres of each temporal layer from the connected-graph sequence.  Conversely,
the sharp witness theorem is not obtained by coefficient extraction from the
EGF.  This is enough for a focused short paper at the internal standard.

### Risk

Owner risk remains **medium-high** because the proofs sit directly on the
cograph/modular-decomposition boundary.  Value risk is **medium** because the
recursions become short after the correct decomposition is seen.  The
conjunction, rather than any single displayed formula, is the contribution.

## 8. Binding claim ceiling for the next stage

Allowed contribution claims:

- the literal parity-triggered component-complement self-map on all labelled
  simple graphs;
- its exact fixed/recurrent/period classification;
- the scheduler-specific parity-pruned depth recursion;
- the sharp maximum depth and explicit witness family; and
- the exact scheduler-specific labelled EGFs for all depth layers.

Required zero-credit statements:

- complementation, connected/co-connected splitting, modular decomposition,
  cographs, and cotrees;
- the connected-labelled-graph recurrence and \(q_n\) identity;
- labelled SET assembly, odd-part extraction, and generic tree-height
  enumeration;
- fixed-point EGF bookkeeping by itself; and
- all bounded census numbers.

Forbidden claims:

- “a new cotree” or “a new modular decomposition”;
- a new enumeration of cographs;
- a new graph-complement operation in general;
- novelty inferred from the exact rule string;
- contribution credit for \(q_n=2c_n-2^{\binom n2}\); or
- any assertion that the exhaustive \(n\leq6\) census proves the all-size
  theorem.

## 9. Required controls despite GO

These are claim-discipline requirements, not a REWRITE verdict:

1. Cite Gallai and Corneil--Lerchs--Stewart Burlingham at the first use of the
   decomposition language, and explicitly subtract them.
2. Call the recursive object a parity-pruned component/co-component tree or
   prefix, not a cotree of an arbitrary graph.
3. State that labelled SET calculus is the derivation tool, while the
   scheduler-defined temporal classes are the residual.
4. Keep the 67,758-assertion verifier and 214,396-assertion scout roles
   distinct.
5. Retain HOLD_EXTERNAL until a later manuscript has a direct-owner note and
   an independent hostile review of its actual contribution wording.

## Final verdict

**GO_INTERNAL / HOLD_EXTERNAL.**

The classical cograph/cotree and modular-decomposition substrate is extensive
and receives zero credit.  It does not, however, fully encode the
parity-triggered dynamics: even components freeze, odd components alone
continue, connected/co-connected odd graphs become two-cycle atoms, and this
produces a sharp scheduler-specific clock and an exact temporal labelled
census.  The resulting residual is narrow but real and is sufficient for a
short-paper proof stage under the binding claim ceiling above.
