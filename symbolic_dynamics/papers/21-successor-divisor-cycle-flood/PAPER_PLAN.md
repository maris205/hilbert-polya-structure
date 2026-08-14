# Paper Plan — SD-C23

**Title:** *The Successor–Divisor Shift: A Sharp Trace-Class Determinant with
an All-Length Primitive-Cycle Flood*
**Type:** mathematical theory plus exact finite certificates
**Format:** anonymous A4 article
**Primary family:** Symbolic Dynamics
**Target length:** 15–18 pages including references and appendices
**Review loop:** intentionally omitted

## Claims–evidence matrix

| Claim | Evidence | Status | Manuscript location |
|---|---|---|---|
| The edge rule is intrinsic to the full-shift semiring skeleton | \(F_{n+1}\cong F_d\boxtimes F_q\iff n+1=dq\) | proved | Sections 2–3 |
| The graph is strongly connected and mixing | explicit paths through \(2\); cycles of lengths \(2,3\) | proved | Section 4 |
| A simple primitive cycle occurs at every length \(k\ge2\) | \(C_k=(k,\ldots,2k-1)\) | proved | Section 4 |
| Fixed-order infinite traces are finite-prefix exact | maximal-vertex inequality \(M\le2r-1\) | proved | Section 5 |
| The weighted adjacency is trace class exactly for \(\Re s>1/2\) | row nuclear decomposition plus successor Fourier extraction | proved | Section 6 |
| The Fredholm determinant has an exact trace/primitive ledger | trace-class theory plus finite closed-walk sums | proved | Section 7 |
| The Riemann Euler target fails at degree one | \(\Tr L_s=0\) versus \(\sum_pp^{-s}\) | proved | Section 8 |
| Orbit norms have the wrong arithmetic species | \(e^{T_\gamma}=N(\gamma)^2\), a composite square | proved | Section 8 |
| The obstruction survives severe pruning | \(q\in\{1,2\}\) spine theorem | proved | Section 9 |
| The exact graph/theorem combination was not found in bounded search | documented search plus named nearest work | search-bounded | Section 2 |

## Argument blueprint

### Core claim

Recurrence and analytic determinant control can emerge from the full-shift
semiring, but the most direct successor-factor grammar is nonselective at the
primitive-orbit layer.

### Reasoning chain

1. The source grammar is genuinely arithmetic and recurrent.
2. Its topology is stronger than required: it is mixing and contains simple
   cycles at every length.
3. A maximal-vertex argument turns the infinite trace problem into finite
   exact combinatorics.
4. A row decomposition yields a trace-class determinant on the sharp
   half-plane \(\Re s>1/2\).
5. The determinant's first marked coefficient is nevertheless incompatible
   with the prime Euler product.
6. A two-quotient spine reproduces the obstruction, so the full divisor
   grammar has zero selectivity margin.

### Counterargument handled

The existence of a trace-class determinant close to the critical line might
look like partial Riemann structure.  The paper answers that objection by
separating own-object analyticity from target global structure and by
comparing marked traces before zeros.

## Section plan

### Abstract

State the source grammar, mixing/cycle result, \(2r-1\) confinement, sharp
trace-class half-plane, and degree-one target obstruction.  No citations.

### 1. Introduction

Frame the inherited verifier-versus-recurrence dilemma.  Preview the strongest
positive and negative theorems.  Give four falsifiable contributions and the
strict Route-A boundary.

### 2. Classical and literature boundary

Synthesize finite shift zeta theory, countable Markov shifts, trace-class
Fredholm determinants, infinite weighted graph zeta functions, and arithmetic
graphs.  Bound the novelty statement by the documented search.

### 3. Full-shift source and frozen shift

Define \(F_n,\boxtimes,\boxplus,S\), the edge grammar, phase space, quotient
label, roof, and operator.  State all conventions.

### 4. Recurrent topology and cycle flood

Prove strong connectivity, mixing, canonical cycles, and the
divisor-indexed subflood.  Include Figure 1.

### 5. Exact finite confinement

Prove \(M\le2r-1\), equality uniqueness, exact finite trace cutoff, and the
necklace recurrence.  Include Figure 2 and the finite count table.

### 6. Sharp trace-class theorem

Give the row-nuclear sufficiency proof, local holomorphy, and Fourier
superdiagonal necessity proof.  Explain why entrywise \(\ell^1\) gives only a
nonsharp domain.

### 7. Fredholm and primitive ledger

Define the determinant, derive the first four traces, and state the local
primitive product with its honest \(z\)-domain.

### 8. Exact Euler-target obstruction

Prove the marked first-trace mismatch and composite-square orbit-norm theorem.
State the claim boundary regarding isolated scalar coincidences.

### 9. Pruning and quotient controls

Prove the two-quotient spine theorem, successor-only negative control, and
the general cycles \(C_{d,q}\).

### 10. Route evaluation and next obligation

Freeze the Route tuple, A3/A4 failures, Route-B lock, and Paper22 quotient
filter task.

### 11. Conclusion

Restate the advance: a strong determinant with the wrong primitive species.
Include limitations and reproducibility/scope statements.

### Appendix A

Give expanded proofs for fixed-order enumeration, first low-order ledgers, and
the trace-class holomorphy details.

### Appendix B

Give the complete claim/status/route ledger.

## Figure plan

| ID | Type | Content | Source | Priority |
|---|---|---|---|---|
| Figure 1 | pure TikZ graph | induced prefix, successor spine, quotient returns, \(C_2,C_3,C_5\) | theorem definitions | high |
| Figure 2 | pure TikZ proof diagram | maximal drop and \(r-1\) return bound yielding \(M\le2r-1\) | confinement proof | high |

No data plot is required for a theorem whose threshold is analytic.  A
near-boundary prefix plot could mislead readers because convergence at
\(\sigma=0.51\) is extremely slow.

## Table plan

1. Literature boundary table.
2. Unweighted \(T_r,P_r\) for \(r\le20\).
3. First weighted trace/primitive ledger.
4. Full graph versus spine versus successor-only controls.
5. Strict Route-A and claim-status ledger.

## Citation plan

- Introduction: Bowen–Lanford, Gurevich–Savchenko, Simon.
- Literature boundary: Artin–Mazur, Bowen–Lanford, Gurevich–Savchenko,
  Sarig, Simon, Deitmar, Phunphayap–Pongsriiam–Noppakaew, McNew,
  Perucca–Seuré–Wolff.
- Operator theorem: Simon for standard Fredholm facts only.
- All candidate-specific graph and operator claims cite internal theorem
  numbers, not external literature.

## Page allocation

| Part | Pages |
|---|---:|
| Abstract/status/Introduction | 2.0 |
| Literature and source setup | 2.0 |
| Topology and confinement | 3.0 |
| Trace class and determinant | 3.0 |
| Obstruction, controls, route | 2.5 |
| Conclusion | 0.5 |
| References and appendices | 3–5 |

## Quality locks

- No target-zero data.
- No direct prime predicate in the source.
- No review loop.
- No whole determinant/block ambiguity.
- No primitive/repetition ambiguity.
- No claim of primitive-product convergence at \(z=1\) without proof.
- No A3 credit for own-object half-plane holomorphy alone.
- All citations verified by DOI, publisher page, or primary arXiv record.
