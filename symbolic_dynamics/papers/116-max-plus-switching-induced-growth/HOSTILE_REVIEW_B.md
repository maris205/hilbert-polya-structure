# Hostile Review B — switching-induced max-plus growth

Review date: 2026-08-29  
Reviewer role: independent non-author, second hostile pass  
Release status: **HOLD**  
Provisional verdict: **GO_INTERNAL_AFTER_REPAIR**

I did not consult any Review A artifact. I rebuilt the argument from the raw
max-plus products, the author sources, the exact verifier, and a bounded
primary-source/DOI search. This is not final QA, novelty clearance, or release
approval.

## Bottom line

The displayed generator powers, chronological orientation, five-gap reward
table, three-state kernel, characteristic cubic, stationary law, drift,
Poisson martingale, variance, Perron derivatives, Gärtner--Ellis package,
word bounds and rare masses, zero-temperature limits, and deterministic
endpoints all reconstruct correctly. A fresh verifier run passed 1,182,943
exact assertions and matched the stored stdout byte-for-byte. A fresh
eight-page build is clean, fully embedded, and visually sound.

However, the manuscript contains a concrete false firewall assertion. Section
6.3 says that there is “no reset word” and “no regeneration time.” In fact,
four chronological words of minimal length three have tropical rank-one
products and reset every finite projective input to a fixed gap. This does not
invalidate the pair-specific formulas, but it directly breaks the stated
mechanism separation and materially changes the owner ledger: rank-one
memory loss and projective coupling are classical max-plus mechanisms. It is
a release-blocking critical repair.

## Independent reconstruction from raw products

### 1. Orientation, generator powers, spectral radii, and rank

The convention is

```text
M_n = X_n tensor ... tensor X_1,
```

so the first letter acts first. Literal multiplication gives, for example,
the chronological word `A,A,B` as

```text
B tensor A tensor A = [[1,1],[-1,-2]],
```

which differs from its reversed matrix product. The row maxima of `M_n` are
exactly `M_n tensor (0,0)^T`, so their coordinate maximum equals the global
matrix height.

For each generator, the loop cycle means and two-cycle mean are

```text
A: -2, -1, 0;       B: -1, -2, 0.
```

Thus both tropical spectral radii are zero. In both matrices the diagonal
cross-sum is `-3` and the off-diagonal cross-sum is `0`, so each finite
`2x2` generator has tropical rank two. Direct powers give

```text
A^(2m)   = [[0,-2],[0,0]],
A^(2m+1) = [[-1,-1],[1,-1]]       (m>=1),
B^(2m)   = [[0,0],[-2,0]],
B^(2m+1) = [[-1,1],[-1,-1]]       (m>=1),
```

with the original matrices at exponent one. Hence generator-only heights are
`n mod 2`, and the endpoint growth and fixed-tilt pressure are zero.

### 2. Literal gap and reward table

Normalize a projective vector to `(d,0)^T`. Raw multiplication gives

```text
A(d,0)^T = (max(d-2,-1), max(d+1,-1))^T,
B(d,0)^T = (max(d-1, 1), max(d-1,-2))^T.
```

Starting at `d=0`, closure produces exactly
`{-3,-2,0,2,3}`. Subtracting the old coordinate maximum yields the author
table:

```text
d=-3,-2: A -> (0,-1),  B -> (3,+1)
d=0:     A -> (-2,+1), B -> (2,+1)
d=2,3:   A -> (-3,+1), B -> (0,-1).
```

Both representatives of each nonzero sign class have the same target sign
and reward, so the joint state/reward lumping into `N,Z,P` is literal, not
merely distributional. Summing rewards from height zero recovers `H_n` word
by word.

### 3. Tilted kernel and characteristic cubic

With rows and columns ordered `N,Z,P`, attaching probability times `y^reward`
to each transition gives

```text
Q_p(y) = [[0,p/y,qy],
          [py,0,qy],
          [py,q/y,0]].
```

Starting from `Z`, the exact transform is therefore

```text
E[y^H_n] = e_Z^T Q_p(y)^n 1,
```

including `n=0`. Direct determinant expansion gives

```text
det(rI-Q_p(y))
  = r^3 -(p^2+q^2+pq y^2)r - pq y
  = r^3 +(2a-1-a y^2)r-a y,     a=pq.
```

For `0<p<1` and `y>0`, the directed graph has cycles of lengths two and
three, so `Q_p(y)` is primitive.

### 4. Stationary law, Poisson martingale, and variance

At `y=1`, balance into `N` and `P` gives

```text
pi_N=p/(1+p),
pi_P=q/(1+q),
pi_Z=(1-a)/(2+a).
```

The only negative transitions are `N--A->Z` and `P--B->Z`; hence

```text
mu = 1-2(p pi_N+q pi_P) = 3a/(2+a).
```

The displayed solution

```text
h_N=-2p/(1+p), h_Z=0, h_P=-2q/(1+q)
```

satisfies `(I-P)h=f-mu*1` symbolically. Consequently
`D_k=g-mu+h(S_k)-h(S_{k-1})` is a bounded martingale difference. I
independently simplified all six state/letter entries and their stationary
second moment; the result is exactly

```text
sigma^2 = 4a(1-a)(5-2a)/(2+a)^3.
```

At `p=1/2` the six state/letter cases collapse to only three distinct numeric
values, but the table's phrase “six possible values” is harmless if read as
six cases rather than six distinct numbers.

The finite-chain ergodic theorem supplies the almost-sure drift and the
quadratic-variation limit from the nonstationary initial state `Z`; bounded
increments give conditional Lindeberg. Thus the martingale CLT argument is
complete.

### 5. Perron derivatives, pressure, and LDP hypotheses

For

```text
F(r,t)=r^3+(2a-1-a exp(2t))r-a exp(t),
```

the derivatives at `(1,0)` are

```text
F_r=2+a, F_t=-3a, F_rr=6, F_rt=-2a, F_tt=-5a.
```

Two implicit differentiations reproduce `mu` and `sigma^2`. Because the
tilted matrix is primitive at every finite real `t`, its Perron root is
simple and positive, and the pressure is real analytic on all of `R`.

The Gärtner--Ellis hypotheses used here are met: the limiting cumulant
generating function exists and is finite/differentiable on the full line;
the effective-domain boundary is empty, so essential-smoothness steepness is
vacuous; and `0<=H_n<=n` gives exponential tightness. The full LDP with the
Legendre transform and infinite rate outside `[0,1]` follows. The manuscript
has the ingredients, although one sentence making this hypothesis check
explicit would improve it.

### 6. Exact words and rare masses

Rewards are `+1` or `-1`; every negative reward lands at `Z`, and every exit
from `Z` has reward `+1`. Negative rewards are therefore isolated. Among `n`
steps there are at most `floor(n/2)` negatives, giving

```text
n mod 2 <= H_n <= n.
```

Avoiding every negative transition forces letter alternation, with exactly
two choices for `n>=1`. Their masses are

```text
P(H_n=n) = 2a^(n/2)       (n even),
P(H_n=n) = a^((n-1)/2)    (n odd).
```

For `n=2m`, attaining zero forces each reward pair to be `(+1,-1)`, and the
only corresponding return blocks are `AA` and `BB`. Thus

```text
P(H_2m=0)=(p^2+q^2)^m=(1-2a)^m.
```

The author verifier additionally finds every parity-compatible height through
its finite horizon, but the theorem only claims bounds and extremizers; it
does not improperly promote this finite observation to a support theorem.

### 7. The two zero-temperature normalizations

At the positive edge,

```text
Q_p(y)/y -> L_+,
char(L_+)=r(r^2-pq),
```

so the Perron root divided by `y` tends to `sqrt(pq)`. At the negative edge,
with `D_y=diag(y^-1,1,y^-1)`, direct entrywise calculation gives

```text
D_y^-1 Q_p(y) D_y
  = [[0,p,qy],[p,0,q],[py,q,0]]
  -> L_-,
char(L_-)=r(r^2-p^2-q^2).
```

These yield the two displayed pressure limits. The diagonal matrix is
invertible for every `y>0`; its singular limit at zero is not used as a
similarity at `y=0`. The endpoint cases `p=0,1` are correctly separated and
have pressure zero for each fixed tilt.

## Critical counterexample to the firewall

For a finite `2x2` max-plus matrix, tropical rank one is equivalent to equality
of the two permutation cross-sums, and such a matrix maps every finite input
vector to a fixed projective difference. Exhaustion of words of lengths one,
two, and three shows no reset at lengths one or two, but four resets at length
three:

| chronological word | literal product `M_3` | reset gap |
|---|---|---:|
| `ABA` | `[[0,-2],[3,1]]` | `-3` |
| `ABB` | `[[1,-1],[1,-1]]` | `0` |
| `BAA` | `[[-1,1],[-1,1]]` | `0` |
| `BAB` | `[[1,3],[-2,0]]` | `3` |

For example, the cross-sums of the `ABA` product are both `1`, its rows differ
by the scalar `-3`, and direct evaluation on gaps
`-100,-3,-1,0,1,3,100` always returns `-3`. The analogous constant-gap check
holds for the other three matrices. Every one of these words has positive
probability for `0<p<1`; occurrences in disjoint three-letter blocks already
give an almost-sure finite coupling opportunity.

This is a genuine max-plus memory-loss/reset word. The main paper happens not
to use a regenerative proof, but “there is no reset word, regeneration time”
is false.

## Findings by severity

### CRITICAL

1. **False internal-firewall claim.** Section 6.3 says that rank-two
   generators imply there is no reset word or regeneration time. Products can
   lose rank even when each generator has rank two, and the four minimal words
   above do exactly that. This is both a mathematical falsehood and a mechanism
   collision/owner-scope error.

   **Executable repair:** replace the P89 row with a truthful distinction:
   “The pair does possess length-three tropical rank-one memory-loss words
   (`ABA`, `ABB`, `BAA`, `BAB`). The present proof does not use a symbolic
   language or a regeneration decomposition; its pair-specific observable is
   instead computed through the explicit finite projective reward chain.” Add
   exact verifier assertions for the four products, their rank-one cross-sums,
   constant image gaps, and the absence of shorter reset words. Treat the
   memory-loss/coupling mechanism as zero-credit background.

### MAJOR (math)

No additional theorem-level mathematical failure was found after the reset
firewall counterexample. The reset words do not change the finite law, drift,
variance, pressure, LDP, word extrema, or endpoint formulas.

### MAJOR (owner-scope)

1. **The induced finite projective Markov-chain method needs explicit owner
   subtraction.** The paper credits general max-plus algebra, memory loss, and
   limit theorems, but leaves “literal five-to-three state reduction” in the
   residual conjunction without saying that finite induced Markov chains in
   max-plus projective space are themselves classical. Baccelli et al. are
   already cited, but the relevant section/method is not identified.

   **Executable repair:** explicitly assign zero credit to the general induced
   projective-chain/Markov reward method. Pinpoint Baccelli et al. Section 8.4
   and/or cite Blondel--Gaubert--Tsitsiklis, which expressly describes this
   method. Credit Mairesse for projective coupling/stationary regimes and
   Merlet for memory loss. Reserve only the concrete five values, this exact
   lumping table, and the resulting rational/cubic formulas as pair-specific
   residual calculations, still without novelty language.

2. **Pair-specific owner search is not equivalence-complete.** Exact-matrix,
   exact-formula, and phrase searches found no direct owner of this pair, but
   tropically equivalent pairs can be hidden by row/column scalings,
   permutations, transposition, or additive normalization.

   **Executable repair:** keep external HOLD and say explicitly that the
   bounded search did not exhaust tropical equivalence classes. Do not use
   “no direct hit” as a novelty statement.

### MINOR

1. Rename Lemma 4.1 “stationary law of the lumped projective chain.” The
   displayed vector is not the five-state literal-gap distribution, although
   the body text currently makes the intended three states clear.
2. In the Gärtner--Ellis proof, add the one-line check that full effective
   domain makes the steepness condition vacuous. This prevents readers from
   wondering whether only exposed-point lower bounds were proved.
3. Replace conclusion-level “exact word interval” by “exact parity bounds,”
   or add a short construction proving the stronger exact support
   `{n mod 2, n mod 2+2, ..., n}`. The current proposition proves the bounds,
   not that stronger support statement.
4. If “six possible values” is intended to mean distinct numbers, qualify it:
   at `p=1/2` the six state/letter entries collapse to three distinct values.

## Owner audit and zero-credit ledger

The bounded primary/DOI search covered exact matrix strings, the rational
drift formula, “neutral max-plus switching,” stochastic max-plus Lyapunov
exponents, finite projective Markov chains, memory loss, stationary regimes,
CLT/LDP, and pair-specific phrases.

Direct generic owners found:

- Baccelli--Cohen--Olsder--Quadrat, *Synchronization and Linearity* (1992),
  already cited, is the classical max-plus/discrete-event source.
- Blondel--Gaubert--Tsitsiklis,
  [“Approximating the spectral radius of sets of matrices in the max-algebra
  is NP-hard”](https://doi.org/10.1109/9.880644), explicitly records the
  induced Markov-chain construction in max-algebraic projective space as the
  standard computation when that chain is finite. The complexity theorem is
  not the present claim; its historical statement is the relevant owner
  evidence.
- Mairesse,
  [“Products of Irreducible Random Matrices in the (Max,+) Algebra”](https://doi.org/10.2307/1428012),
  directly owns general projective coupling and unique stationary-regime
  theory for random max-plus products.
- Merlet's
  [memory-loss paper](https://doi.org/10.1287/moor.1090.0434) and
  [topical-operator CLT](https://doi.org/10.1214/105051607000000168) are
  correctly relevant generic owners; Merlet's earlier limit-theorem preprint
  also covers generic CLT and large-deviation machinery.
- Dembo--Zeitouni's
  [large-deviation text](https://doi.org/10.1007/978-3-642-03311-7) is the
  correct generic Gärtner--Ellis owner.

No primary-source hit in the bounded search displayed this exact pair, its
five-gap table, `3pq/(2+pq)`, the stated variance, or the same characteristic
cubic. That is a negative search result only, not an originality result.

The following must receive zero credit: max-plus algebra and cycle means;
projectivization; rank-one memory loss/reset/coupling; induced finite Markov
chains; reward tilting; stationary finite-chain laws; Poisson/martingale CLT;
Perron perturbation; Gärtner--Ellis; and zero-temperature spectral scaling as
a general method. The residual pair-specific computation is the exact raw
table, its particular strong reward lumping, and the formulas obtained from
this concrete kernel. External ownership remains unresolved.

## Fresh verifier audit

All fresh stdout went to `/tmp`; the stored transcript was read only.

```bash
tmp_out=$(mktemp /tmp/p116_verify.XXXXXX.txt)
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  papers/116-max-plus-switching-induced-growth/code/verify.py > "$tmp_out"
cmp -s "$tmp_out" \
  papers/116-max-plus-switching-induced-growth/code/verify.out
```

Result:

- run exit status: `0`;
- byte comparison: `0` (identical);
- stdout: 30 lines, 799 bytes;
- **1,182,943 exact assertions**;
- 131,071 literal words through length 16;
- exact biased laws/PGFs through time 32 at seven probabilities;
- fresh wall-clock reading: approximately 21 seconds.

The verifier thoroughly checks the author claims but currently does **not**
test the false “no reset word” firewall. That omission should be repaired with
the minimal-word assertions specified above.

## Fresh build, fonts, and visual audit

The manuscript was copied into an isolated temporary directory; no existing
source, PDF, log, or support file was modified.

```bash
build_dir=$(mktemp -d /tmp/p116_build.XXXXXX)
cp main.tex math_commands.tex references.bib "$build_dir"/
cp -R sections "$build_dir"/
cd "$build_dir"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdfinfo main.pdf
pdffonts main.pdf
pdftoppm -png -r 120 main.pdf render/page
```

Settled result:

- **8 pages**, A4, PDF 1.5;
- all four compilation stages returned zero;
- settled LaTeX/BibTeX logs: no substantive warnings, undefined references or
  citations, multiply defined labels, overfull boxes, or underfull boxes;
- every listed font is embedded and subsetted;
- all eight rendered pages were inspected at 120 dpi: no clipping, collision,
  missing glyph, broken table rule, or unreadable equation was observed.

## Repair gate

Before internal GO:

1. correct the false no-reset/no-regeneration firewall and freeze the four
   minimal rank-one words in the verifier;
2. explicitly zero-credit the classical induced-projective-chain and
   coupling/memory-loss methods, with owner citations;
3. clarify the lumped stationary-law title and the Gärtner--Ellis hypothesis
   sentence;
4. narrow “exact word interval” or prove exact parity support;
5. retain external **HOLD**, because the bounded pair-specific search is not
   an equivalence-class novelty audit.

The main theorem package can remain intact after these repairs. External
circulation remains **HOLD**.
