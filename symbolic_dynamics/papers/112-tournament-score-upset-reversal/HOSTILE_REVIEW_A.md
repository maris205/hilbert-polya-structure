# Hostile Review A: *Tournament score-upset reversal dynamics*

**Role:** independent non-author review from first principles  
**Review date:** 2026-08-29  
**Provisional verdict:** **MAJOR REVISION / EXTERNAL DISSEMINATION HOLD**  
**Novelty and priority status:** **HOLD; not assessed positively by this review**

## 1. Executive assessment

I independently reconstructed the update, the simultaneous-reversal energy calculation, the score-class factorization, the recursive depth argument, the fixed-set structure, the labelled enumeration, and the finite-map zeta calculation. I also reran the supplied verifier from a fresh process, compared its output byte for byte with the committed transcript, rebuilt the paper in an isolated temporary directory, and inspected every rendered page.

I found **no theorem-level counterexample** to the stated core results. In particular, simultaneous reversals do not invalidate the energy identity, equal-score blocks cannot merge after the first iterate, the depth recursion gives the advertised universal bound, and the regular-block characterization is both necessary and sufficient.

That favorable mathematical conclusion does **not** clear the manuscript. Equation (5), the central iterate factorization, is visibly malformed in the source and PDF: its superscripts are printed as `,t-1`. Moreover, the notation `\Phi_{C_i}` is not formally defined, although only `\Phi_n` has been defined. The recursive tree is used before its well-foundedness is established. Finally, the owner boundary is incomplete around static and iterative Copeland procedures. These are publication-blocking defects even though the intended mathematics can be repaired locally.

The correct disposition is therefore major revision with external dissemination on hold. The manuscript must not claim novelty, priority, a direct-owner clearance, or a sharp maximum depth on the evidence presently assembled.

## 2. Independent contract reconstruction

Let `T` be a labelled tournament and let `s_T(v)` be the outdegree of `v`. For distinct vertices `u,v`, the clean update rule is

\[
 u\to_{\Phi(T)}v
 \quad\Longleftrightarrow\quad
 s_T(u)>s_T(v)
 \ \text{or}\ 
 \bigl(s_T(u)=s_T(v)\text{ and }u\to_Tv\bigr).
\]

Thus every old edge whose tail has lower score than its head is reversed simultaneously; an edge joining equal-score vertices is retained.

| Contract | Independent reconstruction | Review result |
|---|---|---|
| Update orientation | Unequal-score pairs point from the higher old score to the lower old score; ties keep the old orientation. | Sound, but the displayed definition should be simplified and restricted explicitly to distinct vertices. |
| Simultaneous-reversal energy | With `R(T)={x->y : s_T(x)<s_T(y)}`, `delta_v=s_{Phi(T)}(v)-s_T(v)`, and `E(T)=sum_v s_T(v)^2`, expansion gives the exact identity in Section 2.1 below. | Sound. The proof should expose the incidence formula for `delta_v` so simultaneity is beyond doubt. |
| Fixed points | `Phi(T)=T` iff `R(T)` is empty, equivalently every unequal-score pair already points from high score to low score. | Sound. State this local criterion explicitly before the structural theorem. |
| Equal-score intervals | After one update, old score classes become ordered blocks with pairwise disjoint score intervals. | Sound; this proves that blocks never merge later. |
| Iterate factorization | For old score classes `C_1,...,C_k`, later dynamics acts independently inside those same blocks. | Intended theorem is sound; the printed equation and its operator notation are not acceptable as written. |
| Recursive tree | A nonfixed node has at least two nonempty score classes, hence all children have strictly smaller order. | Sound, but well-foundedness is proved too late in the exposition. |
| Depth recursion and bound | For nonfixed `T`, `tau(T)=1+max_i tau(T[C_i])`, hence `tau(T)<=n-1` for `n>=1`. | Sound. The iff step for stabilization of the block sum should be written out. |
| Fixed structure | Fixed tournaments are exactly unique ordered sums of nonempty regular tournaments. | Necessity, sufficiency, and uniqueness are sound. |
| Enumeration | `f_0=1`, `f_n=sum_j binom(n,j)r_j f_{n-j}` and `F(x)=1/(1-R(x))`. | Sound as generic labelled-sequence bookkeeping once the fixed classification is known. This is not an independent novelty claim. |
| Zeta | Strict energy rules out nontrivial cycles, so every iterate has exactly `f_n` fixed points and `zeta_{Phi_n}(z)=(1-z)^{-f_n}`. | Sound as a formal finite-map consequence. |
| Boundary cases and mask 148 | The empty and one-vertex states are fixed. Under the stated bit convention, mask 148 maps to 4, then 0, then remains 0. | Sound in the fresh exhaustive run; wording about “first” and “certification” needs tightening. |

### 2.1 Energy identity under simultaneous reversals

For each vertex,

\[
 \delta_v
 =\#\{x\to v\in R(T)\}
  -\#\{v\to y\in R(T)\}.
\]

Consequently,

\[
\begin{aligned}
 E(\Phi T)-E(T)
 &=2\sum_v s_T(v)\delta_v+\sum_v\delta_v^2\\
 &=2\sum_{x\to y\in R(T)}\bigl(s_T(y)-s_T(x)\bigr)
   +\sum_v\delta_v^2.
\end{aligned}
\]

The second equality aggregates the linear contribution of every reversed arc; the final square term contains all interaction between simultaneous reversals. If `R(T)` is nonempty, every summand in the first sum is strictly positive. Thus energy increases strictly exactly when the tournament changes. Because the state space is finite, every orbit reaches a fixed point and no nontrivial periodic orbit exists. This derivation validates the result, but the manuscript's compressed sentence should be replaced by the displayed incidence calculation.

### 2.2 Score classes, non-merging, and factorization

Order the old score classes `C_1,...,C_k` by strictly decreasing old score and put

\[
 L_i=\sum_{j>i}|C_j|.
\]

The first image is the ordinal sum of the induced subtournaments on these classes. If `v in C_i`, its new global score is

\[
 L_i+s_{T[C_i]}(v),
\]

so every score in block `i` lies in

\[
 [L_i,L_i+|C_i|-1].
\]

The maximum possible score in the next lower block is `L_i-1`. Hence consecutive block intervals are strictly separated. Their cross edges therefore remain fixed forever, and no two such blocks can later merge into one score class. Internal score comparisons are unaffected by the common external offset. The intended factorization is therefore

\[
 \Phi_n^t(T)
 =\Phi_{C_1}^{\,t-1}(T[C_1])\oplus\cdots\oplus
  \Phi_{C_k}^{\,t-1}(T[C_k]),\qquad t\ge 1,
\]

provided `Phi_C` is first defined as the same rule on tournaments whose vertex set is the arbitrary finite set `C`. An equally clean alternative is to transport each induced tournament to `[|C_i|]`, apply `Phi_{|C_i|}`, and transport it back. The current manuscript does neither, and its actual superscript contains an erroneous comma; see CRITICAL item C1.

### 2.3 Recursive tree and stabilization depth

An equal-score tournament is fixed because the rule retains every tied edge. Therefore a nonfixed tournament has at least two score classes. Each nonempty child `T[C_i]` then has order strictly smaller than its parent. This is the well-foundedness proof needed **before** recursively defining the refinement tree or its height.

After the first update, the cross-block edges are frozen and the block dynamics are disjoint. The ordinal sum at time `t+1` equals that at time `t` iff every internal factor has stabilized. Thus, with

\[
 \tau(T)=\min\{t\ge0:\Phi^{t+1}(T)=\Phi^t(T)\},
\]

one obtains

\[
 \tau(T)=0\quad\text{for fixed }T,
 \qquad
 \tau(T)=1+\max_i\tau(T[C_i])\quad\text{otherwise}.
\]

Strong induction now gives `tau(T)<=n-1` for `n>=1`: every child has size at most `n-1`, and the child bound is at most its size minus one. This is a universal bound only. Neither the proof nor the exhaustive data establishes the sharp maximum as a function of `n`.

### 2.4 Fixed tournaments and uniqueness of regular blocks

Suppose `T` is fixed. Distinct score classes are ordered by score, and the fixed-point criterion forces every edge between them from the higher class to the lower class. All vertices in one class receive the same external score offset, so equality of their global scores forces equality of their internal outdegrees. Each induced block is therefore regular.

Conversely, take an ordered sum of nonempty regular blocks of sizes `m_1,...,m_k`. Every vertex in block `i` has global score

\[
 a_i=\sum_{j>i}m_j+\frac{m_i-1}{2}.
\]

For consecutive blocks,

\[
 a_i-a_{i+1}=\frac{m_i+m_{i+1}}2>0.
\]

Thus the blocks are exactly the intrinsic global score classes, all cross edges already point from high score to low score, and all internal edges join tied vertices. The tournament is fixed. Because the score classes are intrinsic, the ordered regular-block decomposition is unique. For `n=0`, the unique empty tournament is the empty ordinal sum.

### 2.5 Labelled recurrence, EGF, and zeta

Let `r_j` count labelled regular tournaments on a prescribed `j`-element label set, with `r_0=0` and `r_j=0` for positive even `j`. Let `f_n` count fixed labelled tournaments, with `f_0=1`. Selecting the unique top regular block gives

\[
 f_n=\sum_{j=1}^n\binom{n}{j}r_jf_{n-j}.
\]

For exponential generating functions

\[
 F(x)=\sum_{n\ge0}f_n\frac{x^n}{n!},\qquad
 R(x)=\sum_{j\ge1}r_j\frac{x^j}{j!},
\]

the recurrence is `F=1+RF`, hence `F=1/(1-R)`. The displayed values

\[
 (f_0,\ldots,f_6)=(1,1,2,8,40,264,2048)
\]

agree with the fresh calculation.

Strict energy implies `Fix(Phi_n^m)=Fix(Phi_n)` for every `m>=1`, so the Artin--Mazur zeta function is

\[
 \zeta_{\Phi_n}(z)
 =\exp\!\left(\sum_{m\ge1}\frac{f_nz^m}{m}\right)
 =(1-z)^{-f_n}.
\]

At `n=0` and `n=1`, the state space is a singleton, `f_n=1`, and the same formula gives `(1-z)^{-1}`.

### 2.6 The mask-148 witness

Under the manuscript's convention—pairs scanned lexicographically and bit one meaning that the smaller endpoint wins—`148=2^7+2^4+2^2`. Direct reconstruction gives

| state | score vector |
|---|---|
| mask 148 | `(2,2,2,2,3,4)` |
| mask 4 | `(1,1,2,2,4,5)` |
| mask 0 | `(0,1,2,3,4,5)` |

The orbit is `148 -> 4 -> 0 -> 0`, so this tournament has depth two. The exhaustive program reports no failure of idempotence below order six and reports 148 as the least numerical mask at order six when orders and then masks are scanned increasingly. That precise order-dependent statement should replace an unqualified “first witness.”

## 3. CRITICAL

### C1. The central iterate formula is visibly corrupted and not well-typed

The source of Equation (5) uses

```tex
\Phi_{C_1}^{,t-1}(T_1)\oplus\cdots\oplus
\Phi_{C_k}^{,t-1}(T_k).
```

The comma is not a harmless source-code curiosity: it appears in the rendered PDF as part of each superscript, and fresh PDF text extraction likewise returns `Phi_C1^{,t-1}`. This is the main structural formula of the paper. In addition, `Phi_C` has not been formally defined; the manuscript defines `Phi_n` on `[n]` and then silently changes the subscript from an order to a label set.

**Required repair:** remove the commas, define the update functorially on every finite label set (or explicitly relabel each block), use one consistent notation for `T_i=T[C_i]`, rerun the verifier, rebuild the PDF, and visually reinspect the corrected display. Until this is fixed, the principal theorem is literally misstated in print.

This is a production and mathematical-notation critical defect, not evidence that the intended factorization is false.

## 4. MAJOR (mathematics and exposition)

### M-MATH-1. Establish well-foundedness before defining the recursive tree

The manuscript recursively attaches score-class children and uses the resulting height before proving that a nonfixed node has at least two classes and therefore strictly smaller children. Move that two-line argument to the definition. State explicitly that fixed nodes have no children. This removes a genuine circularity in presentation even though the recursion is mathematically valid.

### M-MATH-2. Prove both directions of the depth recursion

The factorization readily gives an upper bound on stabilization time, but the equality

\[
 \tau(T)=1+\max_i\tau(T[C_i])
\]

also uses the converse: an ordinal sum with frozen cross edges has stabilized only if every internal factor has stabilized. Write this iff statement explicitly, then split fixed and nonfixed cases. Do not take a maximum over an empty family.

### M-MATH-3. Make the simultaneous-incidence calculation explicit

The current energy proof is correct, but its phrase that every reversed arc “contributes” is too compressed for a synchronous update where many reversals share vertices. Insert the formula for `delta_v` and expand `sum_v s_T(v)delta_v`. This turns a potentially suspicious step into a transparent exact identity.

### M-MATH-4. State the local fixed-point criterion before the block theorem

The useful equivalence

\[
 \Phi(T)=T\quad\Longleftrightarrow\quad R(T)=\varnothing
\]

is currently only implicit in the Lyapunov discussion. Promote it to a proposition or an explicit part of the energy theorem. The later necessity proof for regular blocks should invoke this criterion rather than make the reader reconstruct it.

### M-MATH-5. Define `[0]` without a degenerate interval convention

The notation `[n]={0,1,...,n-1}` is ambiguous at `n=0`, although the empty tournament is later used essentially in the recurrence and zeta statement. Define

\[
 [n]=\{i\in\mathbb Z:0\le i<n\},
\]

so `[0]=emptyset` is literal. Keep the `n=0` and `n=1` fixed-state checks separate from the `tau<=n-1` statement, which is correctly restricted to `n>=1`.

## 5. MAJOR (owner and scope control)

### 5.1 Bounded primary-source/DOI audit

I ran bounded title, phrase, and DOI searches for tournament score correction, reversal of score upsets, Copeland score ranking, repeated/iterative Copeland rules, regular tournament decompositions, and tournament score sequences. I checked the accessible publisher or DOI records for the sources below. This is a bounded audit, not a systematic review and not a novelty certificate.

| Source | What it owns or approaches | Required manuscript treatment |
|---|---|---|
| Landau, “On dominance relations and the structure of animal societies: III. The condition for a score structure,” *Bull. Math. Biophys.* 15 (1953), DOI [10.1007/BF02476378](https://doi.org/10.1007/BF02476378) | Classical tournament score sequences. | Zero credit; retain only as background. |
| Moon, *Topics on Tournaments* (1968) | Classical tournament terminology, regular tournaments, and decomposition background. | Zero credit; background only. |
| Rubinstein, “Ranking the Participants in a Tournament,” *SIAM J. Appl. Math.* 38 (1980), DOI [10.1137/0138009](https://doi.org/10.1137/0138009) | Primary treatment of ranking by tournament points/scores. | Missing near-neighbor. Cite and distinguish a static ranking from synchronous edge reorientation. |
| Henriet, “The Copeland Choice Function: An Axiomatic Characterization,” *Social Choice and Welfare* 2 (1985), DOI [10.1007/BF00433767](https://doi.org/10.1007/BF00433767) | Primary static Copeland-choice owner. | Missing near-neighbor. Cite and delimit the score-rule vocabulary. |
| Monsuur, “Characterizations of the 3-cycle count and backward length of a tournament,” *Eur. J. Oper. Res.* 164 (2005), DOI [10.1016/j.ejor.2003.09.032](https://doi.org/10.1016/j.ejor.2003.09.032) | Uses score order to define tournament upsets/inconsistency; close to the manuscript's “score-upset” language. | Already relevant background, but the terminology cannot be presented as newly owned. Its static statistic is not the present iteration. |
| Bouyssou, “Monotonicity of ‘ranking by choosing’: A progress report,” *Social Choice and Welfare* 23 (2004), DOI [10.1007/s00355-003-0250-x](https://doi.org/10.1007/s00355-003-0250-x) | Studies ranking by successive choice, including repeated Copeland choice on shrinking sets. | Mandatory iterative near-neighbor. It removes selected alternatives rather than synchronously reorienting every edge, but that distinction must be stated rather than assumed. |
| Linares Lejarraga and Bodanza, “Choosing how we choose: reconciling competing rationales in collective decision-making,” *Constitutional Political Economy* (2025), DOI [10.1007/s10602-025-09500-4](https://doi.org/10.1007/s10602-025-09500-4) | Accessible primary record uses the name “Iterative Copeland from below” for a collective-choice procedure. | Current terminology-colliding near-neighbor. Cite or explicitly delimit after reading the complete source; do not equate it with the present map. |
| Artin and Mazur, “On Periodic Points,” *Ann. of Math.* 81 (1965), DOI [10.2307/1970384](https://doi.org/10.2307/1970384) | Classical dynamical zeta definition. | Zero credit; the displayed zeta is a routine consequence once all cycles are fixed. |

The bounded search did **not** locate a source that plainly defines the identical synchronous rule “reverse every edge from lower old outdegree to higher old outdegree, retain ties, and iterate.” That negative search result is not evidence of novelty or priority. Terminology varies across tournament rankings, feedback/upset measures, score correction, and social-choice iteration, so an owner clearance requires a broader and documented search.

### O-SCOPE-1. Add the missing Copeland neighbors and a precise subtraction paragraph

The bibliography and related-work discussion must cover Rubinstein, Henriet, Bouyssou, and the current “Iterative Copeland” usage above. The comparison needs a mechanics table: whether the procedure ranks or selects vertices, deletes vertices, changes edges, uses old or recomputed scores, applies updates sequentially or synchronously, and retains ties. Mere citation accumulation is insufficient.

### O-SCOPE-2. Subtract all classical and generic components

The paper receives no independent credit for score sequences, regular tournaments, ordinal sums, the generic labelled-sequence recurrence/EGF, or the Artin--Mazur definition. After subtraction, the plausible residual contribution is the analysis of this particular synchronous map: its exact energy identity, permanent score-class factorization, recursive depth formula and upper bound, plus the map-specific identification of its fixed set. Even that residual remains owner-HOLD pending the expanded audit.

### O-SCOPE-3. Do not convert search absence into novelty or priority prose

The manuscript and all collateral should continue to avoid “new,” “first,” “novel,” “previously unknown,” or equivalent priority language. A bounded miss is not a clearance. The correct public status is `external dissemination HOLD` until an independent owner review is complete.

## 6. MINOR

1. Simplify the update display. The condition `s_T(u)>s_T(v)` already implies `s_T(u) != s_T(v)`; the repeated inequality is noise. State that `u` and `v` are distinct.
2. Replace “first witness” by “least numerical mask under increasing-order, then increasing-mask enumeration.” Without a scan order, “first” has no mathematical content.
3. Replace language that the program “certifies” unrestricted mathematical facts by “exhaustively checks the stated finite range.” The proof, not the script, establishes the general theorem.
4. In the conclusion say “exponential generating function,” not merely “sequence generating function.”
5. Keep `r_0=0` visibly identified as the nonempty-block atom convention, distinct from `f_0=1` for the unique empty fixed tournament.
6. Preserve the manuscript's current sharpness restraint. The bound `n-1` is **not** shown sharp or tight. The finite maxima through order six do not justify a formula for the global maximum depth. No revision should add “sharp depth,” “optimal,” “attained for all n,” or an extrapolated extremal claim.
7. Once Equation (5) is corrected, inspect the actual superscripts in the PDF rather than relying only on a successful TeX exit code.

## 7. Fresh computational audit

I launched the verifier in a fresh Python process with bytecode writing disabled and redirected its output to a new temporary file outside the repository. A direct byte-for-byte comparison with `code/verification_output.txt` returned equality.

| Check | Fresh result |
|---|---:|
| Final status | `PASS` |
| Exact assertion count | `1,677,508` |
| Enumerated tournament states | `33,868` |
| Fresh/stored transcript size | `763 / 763 bytes` |
| Direct byte comparison | equal |

The run covers the stored exact lanes through order six, including the update implementation, energy identity, one-step block form, non-merging/factorization consequences, fixed classification and counts, depth recursion/bound, zeta consequence, and mask-148 orbit. This is strong regression evidence for the finite range; it is not a substitute for the general proofs.

## 8. Fresh isolated build and visual audit

I copied only `main.tex` and `references.bib` to a fresh temporary directory and ran the complete sequence `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`. No workspace source was touched.

| Build/inspection item | Result |
|---|---:|
| PDF pages | 6 |
| PDF size | 308,689 bytes |
| LaTeX warnings in final pass | 0 |
| BibTeX warnings | 0 |
| Overfull boxes | 0 |
| Underfull boxes | 0 |
| Undefined references/citations | 0 |
| Placeholder sentinels (`??`, `[?]`, `VERIFY`, `TODO`, `FIXME`) | 0 |
| Font rows reported by `pdffonts` | 22 |
| Embedded / subset / Unicode fonts | all yes |

All six pages were rendered and visually inspected. I found no clipping, collision, missing glyph, table overflow, or unreadable page. Page 6 has generous white space but no layout failure. The inspection did, however, expose the central Equation (5) superscript comma described in C1. A warning-free build therefore does not imply a correct mathematical rendering.

## 9. Required repair checklist

Before this manuscript may leave HOLD, the author must:

- correct Equation (5), define `Phi_C` or an explicit relabelling transport, and visually verify the repaired superscripts;
- move the strict-size/well-foundedness argument before the recursive-tree definition;
- state and prove the two directions behind the exact `tau` recursion;
- insert the vertex-incidence formula in the simultaneous energy proof;
- state `Phi(T)=T iff R(T)=emptyset` explicitly;
- define `[0]=emptyset` without relying on an ellipsis convention and retain the `n=0,1` checks;
- qualify mask 148 by the exact enumeration order and finite verification range;
- add and distinguish the missing primary Copeland/ranking neighbors;
- rewrite the contribution paragraph under strict owner subtraction;
- preserve the ban on sharp-depth and novelty/priority claims;
- rerun the verifier with the exact assertion total visible and byte-compare the transcript;
- rebuild in a clean directory and repeat the warning, font, text, and all-page visual checks.

## 10. Provisional verdict

**MAJOR REVISION / EXTERNAL DISSEMINATION HOLD.**

The mathematical core survives hostile reconstruction, and I found no counterexample to the advertised contracts. Nevertheless, the main iterate theorem is presently corrupted in print, one of its operators is undefined, the recursive exposition is not ordered rigorously, and the owner comparison omits material Copeland neighbors. Novelty and priority remain unassessed. Classical score-sequence, regular-tournament, ordinal-sum, labelled-EGF, and zeta material must receive zero credit. Clearance requires the repairs above and a separate owner decision; search absence is not novelty.
