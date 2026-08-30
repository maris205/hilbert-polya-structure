# Hostile Review A: Odd-Component Complementation

**Reviewer role:** first independent, nonauthor round-0 reviewer.

**Audit date:** 2026-08-30 UTC.

**Materials audited:** `main.tex`, `references.bib`, `main.pdf`,
`main_round0_original.pdf`, every paper-local support document, and the
paper-local verifier and canonical output.  I also reconstructed the map and
the claimed clock independently, reran the verifier, extended the coefficient
recursion beyond its exhaustive range, performed an isolated four-stage
LaTeX build, and inspected every rendered page.  I did not modify the
manuscript or its code.

## Verdict

**GO_INTERNAL, subject to the two nonblocking MINOR support-document repairs
listed below.  External release remains HOLD.**

I found no counterexample, false converse, missing boundary case, or
coefficient error in the manuscript's theorem package.  After subtracting
the classical component/co-component, cograph/cotree, labelled-SET, and
connected-graph-enumeration machinery, the surviving conjunction is narrow
but sufficient for a focused internal short paper:

1. the literal parity-scheduled self-map on all labelled simple graphs;
2. its exact pointwise entrance clock and complete period classification;
3. the sharp all-order transient bound with witnesses at every order; and
4. the labelled EGF of every cumulative and exact depth layer, hence the
   recurrent, fixed, two-cycle, and zeta censuses.

The direct-owner search remains bounded, and the closest classical owner
boundary is unusually close.  Therefore this is not a novelty or priority
clearance, and it is not a release clearance.

## Severity summary

| Severity | Count | Result |
|---|---:|---|
| CRITICAL | 0 | No false theorem or invalid proof found. |
| MAJOR | 0 | No issue requiring STOP or manuscript rewrite found. |
| MINOR | 2 | Support-document claim discipline and mechanical-evidence mapping should be corrected before a later freeze. |

## Required MINOR repairs for the next round

### M1. The two proof routes are complementary, not logically independent

`NARRATIVE_REPORT.md` is headed “Why the paper has two independent proof
routes.”  The enumerative route is not logically independent of the temporal
route: the proof of the EGF recurrence explicitly invokes equation (2), the
pointwise depth recursion, to identify odd children of depth at most
`t-1`.  The two routes produce nonidentical outputs and give genuine
complementary value, but “independent” overstates their logical separation.

**Required repair:** replace “independent” by “complementary” and say that the
labelled-class translation uses the already-proved pointwise recursion.
Nothing in `main.tex` needs mathematical repair on this point.

### M2. The claims/evidence ledger overstates and mislocates verifier coverage

The paper-local verifier is sound for what it actually asserts, but the
support ledger should be more exact.

- `CLAIMS_EVIDENCE.md` points C1 to “Lemma 2.1,” C2 to “Theorem 2.3,” and
  C3--C4 to “Corollary 2.4.”  In the frozen paper these are respectively
  Lemma 1.1, Theorem 2.2, and Corollary 2.3.
- The 67,758-assertion verifier does **not** literally compute the
  parity-pruned tree and assert `depth(G)=D(G)` state by state.
- It does **not** literally assert component-partition refinement or the
  fixed/recurrent iff criteria state by state.
- Its `fixed` array is assembled from the claimed allowed connected
  components and checked only to be a subset in count of the recurrent
  array; it is not compared with an exhaustive count of states satisfying
  `Phi(G)=G`.  Thus `CONTROL_RESULTS.md` and C8 should not imply a literal
  exhaustive fixed-state comparison by this verifier.

This is a control-description problem, not a theorem problem.  My independent
pointwise audit supplied the missing checks and passed, as recorded below.

**Required repair:** either strengthen the verifier with those literal
assertions or narrow the mechanical-evidence descriptions, and correct the
theorem locations.

## 1. Literal map reconstructed

For a current graph `G`, the map first takes the connected components of
that current state.  Inside each odd-order component it toggles every
possible edge, and inside each even-order component it does nothing.  It
never changes a cross-component nonedge.

Three consequences are immediate and correctly used throughout the paper:

1. the component partition can only refine;
2. every even component is permanently fixed; and
3. an odd connected component `H` either alternates with its connected
   complement, or its complement is disconnected and the component splits
   permanently after one step.

The word “synchronously” causes no hidden ambiguity: all trigger parities
and components are computed in the pre-update graph, and components are
vertex-disjoint, so the toggles commute.

## 2. Pointwise split tree and exact clock

### 2.1 Definition and well-foundedness

For connected odd `H`, the manuscript stops when the complement of `H` is
connected.  Otherwise, it takes the connected components of the complement,
freezes even children, and recurses only on odd children.  An odd child is a
strict vertex subset whenever a split occurs, so the recursion is
well-founded.

The empty-maximum convention is harmless and is needed for an arbitrary
graph having no odd components.  In the recursive connected-odd case the
maximum is in fact nonempty: components of a graph of odd total order cannot
all have even order.  Thus the convention neither hides nor creates a
boundary case.

### 2.2 Exact entrance time

For a connected odd `H`, write `d(H)` for its preperiod.  Directly from the
map,

```text
d(H) = 0                                      if complement(H) is connected,
d(H) = 1 + max d(C) over odd complement-components C otherwise.
```

Even children have preperiod zero, and the disjoint union of independently
evolving children enters the recurrent set at the maximum, not the sum, of
their entrance times.  Thus this recurrence is exactly the manuscript's
`D(H)`.  Taking the maximum over initial odd components gives the arbitrary
graph case.  The induction on vertex order in Theorem 2.2 is valid.

No phase mismatch occurs after a split: entrance into the recurrent set is a
property of the simultaneous product state, and all surviving factors have
period one or two.

### 2.3 Independent pointwise stress test

I independently implemented the recursive `D` evaluator around the frozen
map functions and checked every labelled graph through order six.  The audit
made **101,604 exact assertions**:

- `orbit_preperiod(G) = D(G)` for every state;
- `preperiod(G)=0` iff every nontrivial odd component is co-connected; and
- `Phi(G)=G` iff every component is a singleton or has even order.

Result: **PASS**.  The recursive connected-odd evaluator encountered 733
distinct memoized states.  This test was review-side only and did not alter
the paper-local verifier.

## 3. Recurrent, fixed, and period classification

The recurrent classification is exact.  A nontrivial odd component is
recurrent precisely when its complement is connected; it then alternates
with that complement.  A singleton is fixed.  Every even component is fixed.
If an odd component splits, the component partition changes strictly and can
never coarsen, so the original state cannot be recurrent.

The fixed classification is also exact.  A nontrivial labelled graph cannot
equal its literal edge complement on the same vertex set, because every
unordered vertex pair is toggled.  Hence a recurrent state is fixed exactly
when all of its components are singletons or even.  There is no component
permutation loophole because the vertex blocks are labelled and preserved.

Every nonfixed recurrent factor has period two, and the synchronous product
of period-one and period-two factors still has period at most two.  Thus the
period ceiling and “genuine two-cycle” statement are correct.

## 4. Sharp global depth

### 4.1 Upper bound

Along an active branch, an odd parent `H` and odd child `C` have odd orders.
Because the complement of `H` has at least two components, `H\C` is nonempty;
its order is the positive even number `|H|-|C|`, hence at least two.  Each
split therefore reduces active order by at least two.  A branch beginning at
order at most `n` has at most `floor((n-1)/2)` split nodes.  Taking a maximum
over initial odd components preserves this bound.

### 4.2 Sharp witnesses and boundaries

The family

```text
H_1 = K_1,
H_{2r+1} = complement(H_{2r-1} disjoint-union K_2)
```

is valid.  The complemented disconnected union is connected, while the
complement of the resulting graph is exactly the displayed odd child plus
the frozen even child.  Hence its depth rises by one at each recursion.
Adding a singleton gives every even-order witness.  The cases `n=1` and
`n=2` both give depth zero, and `n=0` is separately and correctly stated as
zero.  There is no missing `r=0` boundary.

## 5. All-depth labelled EGF

### 5.1 Co-connected base class

For `n>=2`, a graph and its complement cannot both be disconnected.  Since
complementation is a label-preserving involution, the number of connected
and co-connected labelled graphs is

```text
q_n = 2 c_n - 2^(n choose 2).
```

The exceptional convention `q_1=1` is required and correct.  Restricting `Q`
to odd orders matches the dynamical base atoms.

### 5.2 Recurrence for connected odd states

A positive-depth connected odd graph `H` corresponds bijectively, by
complementation, to a disconnected labelled SET of:

- arbitrary connected even components; and
- connected odd components of depth at most `t-1`.

The exponential counts this SET.  Subtracting `1+C_e+O_{t-1}` removes the
empty SET and every one-component SET, while odd-part extraction imposes odd
total order.  There is no missing automorphism factor because labelled SET
calculus already supplies the correct EGF normalization, and complementation
is a pointwise bijection.  Adding `Q` is disjoint from the positive-depth
alternative.  Equations (7)--(9) are therefore correct as identities of
formal power series.

Assembling unrestricted even connected components and odd connected
components counted by `O_t` gives `F_t`.  The cumulative classes are nested,
so `F_t-F_{t-1}` gives exact depth `t` for `t>=1`; `F_0` is exactly the
recurrent class.  The fixed EGF follows from the already-proved component
classification.

### 5.3 Independent coefficient extension

I recomputed connected labelled-graph counts from the standard connected
component recurrence and then ran the manuscript's labelled assembly through
order 12, outside the exhaustive orbit range.  The recurrence stabilized at
exactly `floor((n-1)/2)` at every order tested.  Selected recurrent counts
were:

| `n` | recurrent states | first stabilized depth |
|---:|---:|---:|
| 7 | 1,845,984 | 3 |
| 8 | 266,301,568 | 3 |
| 9 | 66,266,955,904 | 4 |
| 10 | 35,158,965,365,120 | 4 |
| 11 | 35,641,205,953,446,784 | 5 |
| 12 | 73,782,267,413,628,108,288 | 5 |

Result: **PASS**.  This is corroboration, not an all-order proof.

## 6. Two-cycles and dynamical zeta

The recurrent set consists of `f_n` fixed states and `r_n-f_n` states in
two-cycles, so the number of genuine two-cycles is `(r_n-f_n)/2`.  A
transient point cannot be fixed by a positive iterate.  Therefore odd
iterates fix exactly the one-cycles, even iterates fix the entire recurrent
set, and

```text
zeta_n(z) = (1-z)^(-f_n) (1-z^2)^(-(r_n-f_n)/2).
```

The Artin--Mazur manipulation is correct.  This zeta bookkeeping is a
consequence, not an independent source of contribution value, and the paper
appropriately presents it that way.

## 7. Exact verifier audit

Fresh command:

```text
python3 code/verify_odd_component_complementation.py
```

Result: **PASS**, `assertions=67758`.

The fresh standard output was byte-for-byte identical to the canonical
output.  Both had SHA-256
`03bafdf88fd5c2ffd83d67b94e7a764dd8482f89fee530a3af5c7583ee03be32`.
The source hash was
`72cb9baf1be42e0ebb40a2b35ee572ada0538a6cb0b3e4f053020ad6577fa4f5`.

The implementation correctly:

- exhausts all `2^(n choose 2)` labelled graphs for `0<=n<=6`;
- computes the literal synchronous map and exact functional orbits;
- checks every eventual period is one or two;
- checks the claimed global depth ceiling;
- compares exhaustive cumulative depth histograms with the EGF assembly;
- verifies the odd co-connected count identity; and
- reproduces the printed census.

Its limits are exactly those stated in M2.  In particular, bounded exhaustive
agreement does not prove the all-order recurrence, and the manuscript itself
does not rely on it as proof.

## 8. Owner subtraction

### 8.1 Classical owners

The component/co-component and modular-decomposition substrate is classical.
Gallai's foundational paper is appropriately cited at the first use:
[T. Gallai, *Transitiv orientierbare Graphen*](https://doi.org/10.1007/BF02020961).
Recursive complement/union structure and cotrees for cographs are directly
owned by [Corneil, Lerchs, and Stewart Burlingham, *Complement reducible
graphs*](https://doi.org/10.1016/0166-218X(81)90013-5), with recognition and
the standard cotree representation reinforced by [Corneil, Perl, and
Stewart](https://doi.org/10.1137/0214065).

Accordingly, the following receive zero contribution credit:

- graph complementation as an involution;
- splitting into components or co-components;
- ordinary modular decomposition and cotrees;
- cograph union/join recursion and cotree height arguments;
- labelled SET and odd-part operators;
- connected labelled-graph enumeration and the formula for `q_n`; and
- generic fixed/two-cycle/zeta bookkeeping.

The manuscript makes these deductions explicitly and does not call its
pruned object a new cotree or a new modular decomposition.

### 8.2 Residual and direct-map risk

The residual is not the split operation itself.  It is the scheduler-specific
fact that even components freeze while only odd components continue, applied
on all labelled graphs and stopped at connected/co-connected odd atoms.  The
pointwise temporal clock and the depth-indexed labelled classes are specific
to that literal scheduler.

Targeted current searches for odd-order component complementation,
parity-scheduled component complementation, iterative component/co-component
dynamics, and cotree-height dynamics did not locate a primary paper defining
the exact map or owning its full temporal census.  The search did locate the
expected adjacent literatures on cographs, local/subgraph complementation,
and parity components, but none matched the scheduler.

This is only a bounded non-hit.  Owner risk remains **medium-high** because
the proof becomes short once the classical decomposition interface is
recognized.  The paper is correct to make no novelty or priority claim.

## 9. Internal P1--P122 collision audit

| Internal item | Actual overlap | Why it does not consume the P123 residual |
|---|---|---|
| P75, RACG geodesic join components | Complement components decompose recurrent automaton pieces; zeta is present. | No graph self-map, parity scheduler, refinement clock, or labelled depth census.  Generic complement-component decomposition and zeta language earn no credit here. |
| P117, odd-run reversal on cyclic words | Synchronous parity-triggered component-like blocks; periods at most two; sharp transients. | Different carrier, components, update, boundary-survival mechanism, extremal proof, and enumeration.  It consumes generic “parity acts independently on blocks” rhetoric, not the exact graph theorem. |
| P118, synchronous multipartite mex | Complete depth layers and zeta bookkeeping for a finite quotient. | Different map, quotient/fibre mechanism, and recurrent structure.  It consumes generic “all-depth census” rhetoric only. |
| P122, even record-block reversal | Parity-selected blocks and sharp transient depth. | Permutation record blocks are reparsed and descend lexicographically; there is no graph complementation or component-refinement tree. |
| P102--P106 reserve record | A cograph twin-quotient candidate appeared during scouting. | It was not frozen as a P1--P122 paper and is not this self-map.  Classical cograph material remains zero-credit regardless. |

No literal internal map collision was found.  The manuscript's value must
continue to be stated as the exact scheduler-specific conjunction, not as a
generic discovery of parity scheduling, component decomposition, sharp
finite depth, or zeta enumeration.

## 10. Build, freeze, visual, and metadata audit

I copied only `main.tex`, `references.bib`, the verifier files, and the frozen
round-0 PDF into a fresh temporary directory and ran:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Stage statuses: **0 / 0 / 0 / 0**.

- Final PDF: 4 A4 pages, 281,461 bytes.
- Final SHA-256:
  `e7a5138e142ef89402668e4eca4e86ea804672b080bfdcce3fe33f7fa074f68d`.
- Fresh PDF, packaged `main.pdf`, and `main_round0_original.pdf` are
  byte-identical.
- Final log: no LaTeX warnings, undefined citations/references, overfull or
  underfull boxes, or rerun requests.  The sole grep hit for “Rerun” is the
  package name `rerunfilecheck`, not a diagnostic.
- All listed fonts are embedded, subsetted, and have Unicode maps.
- Author, title, subject, and keywords metadata fields are blank; no
  creation/modification dates are reported.
- PDF is unencrypted, has no forms, no JavaScript, and no embedded files.
- Text extraction contains no `??`, `[?]`, `[VERIFY]`, TODO, or FIXME marker.

I rasterized and visually inspected all four pages at 170 dpi.  Equations
(1)--(12), theorem blocks, the census table, bibliography, headers, and
footers are legible.  I found no clipping, overlap, malformed symbol,
misplaced float, orphaned heading, or blank page.  The four-page layout is
clean.

## 11. Allowed claim ceiling

The following may remain as internal contribution claims:

- the literal odd-component complementation self-map;
- the exact scheduler-specific recurrent/fixed/period classification;
- the parity-pruned pointwise entrance clock;
- the sharp maximum preperiod and its witness family; and
- the scheduler-specific all-depth labelled EGF and its census consequences.

The following must remain zero-credit or forbidden:

- a “new cotree,” “new modular decomposition,” or new general complement
  operation;
- a new enumeration method for cographs or connected labelled graphs;
- novelty inferred from an exact rule-string non-hit;
- logical independence of the EGF proof from the pointwise recursion;
- proof by the order-six exhaustive census; or
- any external novelty, priority, or release assertion.

## Final recommendation

**GO_INTERNAL / HOLD_EXTERNAL.**

The main mathematical package survives hostile reconstruction.  The two
required MINOR repairs concern only support-document precision: remove the
claim of logically independent proof routes, and align the claims/evidence
ledger with the frozen theorem numbering and the verifier's actual literal
coverage.  They do not justify STOP.  External circulation must remain on
HOLD until a broader direct-owner audit is completed and the next round has
rechecked the repaired support controls.
