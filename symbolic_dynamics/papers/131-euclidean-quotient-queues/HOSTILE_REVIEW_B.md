# Hostile Review B — P131 Euclidean quotient queues, round 1

**Role:** second independent nonauthor reviewer.  **Audit date:** 2026-08-31
UTC.  **Internal verdict:** **GO_INTERNAL**.  **External verdict:**
**HOLD_EXTERNAL**.

The round-one repair clears every substantive re-entry condition from Hostile
Review A.  I independently reconstructed the carrier, Euclidean convention,
marker clock, ordered core, raw path map, raw inverse strings, exact-depth
series, complete one-step fibres, image/Garden counts, and recurrent necklace
formula.  I found no false displayed theorem and no counterexample.  A fresh
canonical verifier run passed all **6,101,926** dynamically counted assertions
and matched the frozen transcript byte for byte.  A separate cut-mask control,
which imported none of the paper verifier, passed **164,096** reviewer
assertions through `N=14`.  A fresh isolated four-stage build was byte-identical
to the frozen four-page PDF, and all four pages passed visual, font, and
metadata inspection.

Severity summary: **CRITICAL 0; MAJOR (mathematics/definition) 0; MAJOR
(control/reproducibility) 0; MAJOR (owner/internal scope) 0; MINOR 1**.  The
minor issue is a boundary qualifier in the comparison with P126, not a defect
in any theorem of P131: levelwise nonconjugacy starts at `N=4`, while the
two-state or smaller functional graphs at `N=2,3` are isomorphic.

## 1. Reviewed artifacts and frozen bytes

| artifact | SHA-256 at Review B |
|---|---|
| `main.tex` | `4c1ed41c63b7784d878acac1da478ab48d9af1aa4928d7b4fe83da0e9b6e6812` |
| `references.bib` | `7b9c097dbe6423895699e054f1f590eeda7759e5abbe795ed27bd4e03f2a0c68` |
| `code/verify.py` | `94939887128cf0d487e6b054d5113c3fcd6f0921c880c07de5351a5b5eb9d07a` |
| `code/verification_output.txt` | `caa4df1e70fd2bdb86aa5aeb1308c2baa74b5d5e560d73980f1f6886c91bc8c6` |
| `main.pdf` | `931e9d5078f202a969b47dfee2a7a686808ca293da2945c82370ca6c9c0c702a` |
| `main_round1.pdf` | `931e9d5078f202a969b47dfee2a7a686808ca293da2945c82370ca6c9c0c702a` |
| `README.md` | `21d94d944a7e0b29300f7ce47ac0572ed070a65bd21b7b45fd8bf498354e99f2` |
| `BUILD.md` | `df2b8e52ec292455b971202ddb1283345942ff8c3d78f9617e42341c07d1c2fe` |
| `CLAIMS_EVIDENCE.md` | `4ded5465dd1778d1644d2c5e3a7e8c6a4f0ec5a1115da84da0826c73cb3114cd` |
| `CONTROL_RESULTS.md` | `37b9c309c276278f4c81f9f3d0474ecc4706e6eb9880a614875f54dad06c61af` |
| `NARRATIVE_REPORT.md` | `91c05b4ccb3f06d2e29b00d2151c4b5b52d5564fbdc765ab5d59c95398726ef5` |
| `PAPER_PLAN.md` | `fbae889f35de95acba44192ed4fb399026741199bae35eb4f87e384bb088a3b9` |
| `IMPROVEMENT_LOG.md` | `dc5779b5b426696edf6f8afee2d4cfdae344518d037e973e2b469eb5257a61ee` |
| `HOSTILE_REVIEW_A.md` | `6fe652112d8487fc9de92d9b1ff9f0c346351eca67bd350318e76919f65ff336` |

For the internal owner comparison I also read the literal source manuscripts,
not only P131's descriptions of them.  Their audited `main.tex` hashes were
`61e9d0ee7af6491a93e713dfa57707ec739609438ec8029d8115eb9e7a064053`
for P117,
`e443cc734b226a5c4d9a598369fc0f8fc42dc6b17ec5973815b9163c0896c576`
for P122, and
`c93d504af40fbf6e162db4cf3b996457bb7d892ea1ab3e2c8ef89dd7273fd270`
for P126.

## 2. Carrier, recurrence, depth, Euclid equality, and marked core

The carrier is correct and honest.  Canonical finite expansions

\[
q=[0;a_1,\ldots,a_k],\qquad a_i\geq1,\quad a_k\geq2,
\]

parametrize precisely the rationals in `(0,1)`.  At digit sum `N`, the map

\[
B_N(a_1,\ldots,a_k)=(a_1,\ldots,a_{k-1},a_k-1)
\]

is a literal bijection from the P131 level to the positive compositions of
`N-1`; hence the levels `N=0,1` are empty and
`|R_N|=2^{N-2}` for `N>=2`.  Every branch of `Phi` preserves weight and ends
in a digit at least two, including the singleton branch, so `Phi` really is a
self-map of every stated level.

The definitions that were absent in round 0 are now present before the main
theorem (`main.tex:133-137`): recurrent means lying on a directed cycle, and

\[
\operatorname{depth}(w)=\min\{t\geq0:\Phi^t(w)\text{ is recurrent}\}.
\]

The equality convention in the subtractive Euclidean algorithm is also now
literal (`main.tex:82-88`).  If the equal pair was reached through an `L`
step, the final repeated `L` performs `v <- v-u=0`; if it was reached through
an `R` step, the final repeated `R` performs `u <- u-v=0`.  Because the input
begins with `0<u<v`, a preceding letter always exists.  On a reduced pair,
equality occurs once, at termination.  This gives, for example,
`E(1/2)=LL`, `E(2/3)=LRR`, and in general

\[
E(q)=L^{a_1}R^{a_2}L^{a_3}\cdots,
\qquad |E(q)|=\sum_i a_i=N.
\]

The terminal equality symbol is in the same run as the preceding symbol;
this is exactly why the last block has length at least two.  The external
Euclidean-cost citation is appropriately zero-credit: the primary source
explicitly records that subtractive step count is the sum of the partial
quotients ([Minelli--Sourmelidis--Technau](https://link.springer.com/article/10.1007/s00208-022-02452-2)).

For the clock, let `delta(w)` be the greatest linear index carrying a one,
or zero if there is none.  If `delta>0`, either a leading nonsingleton rotates
to the end or a leading one is deleted and increments the last digit.  In both
cases every surviving one shifts left by exactly one, and no one is created.
Thus

\[
\delta(\Phi(w))=\delta(w)-1\quad(\delta(w)>0).
\]

When no one remains, `Phi` is rotation, so the state is recurrent.  A state
that still has a one cannot be recurrent because the number of digits
strictly drops when that one eventually reaches the front, and ones are never
recreated.  Therefore `depth(w)=delta(w)` and the recurrent set is exactly the
words with all digits at least two.

The ordered terminal core is also now well-defined.  Each maximal cyclic run
`1^s` is absorbed into its immediately preceding nonsingleton by adding `s`.
The last original one marks the gap before the first original nonsingleton
following it; transporting this gap through all contractions fixes the
otherwise ambiguous rotation of the contracted word.  Repeated update does
exactly these contractions, and after the last deletion that marked survivor
is at the front.  Hence

\[
\Phi^{\delta(w)}(w)=\kappa(w).
\]

On the core, the eventual period is its primitive rotation period.  The final
digit is at least two, so at most `N-2` earlier positions can be ones; the
witness `(1^{N-2},2)` realizes the bound, including the `N=2` interpretation
`(2)`.  The displayed `(2,1,3)` example correctly yields the ordered core
`(3,3)`: the original terminal `3` follows the marked gap and comes first.

## 3. The literal normalized path map and all-size conjugacy

Let `E_N` consist of length-`N` `L/R` strings beginning with `L` and ending
in a constant block of length at least two.  Alternating run lengths give a
bijection `E:R_N -> E_N`.  The repaired manuscript defines `Psi` on these
raw strings before taking run lengths.

For a string with more than one block, write uniquely `W=L^aY`, where `Y`
begins with `R`, and put `T=overline(Y)`.  If `epsilon` is the last letter of
`T`, then

\[
\Psi(W)=
\begin{cases}
W,&Y=\varnothing,\\
T\epsilon,&a=1,\\
T\overline\epsilon^{\,a},&a>1.
\end{cases}
\]

This is a genuine string self-map:

- in the one-block case the terminal block already has length at least two;
- when `a=1`, complementation makes `T` begin with `L`, and repeating its
  final letter extends an already legal terminal block from length at least
  two to at least three;
- when `a>1`, the appended letter is opposite the last letter of `T`, so a
  new terminal block of length `a>=2` is created;
- every branch preserves total string length `N`.

If the blocks of `W` have lengths `(a_1,...,a_k)`, complementation changes no
block boundary.  The `a_1>1` branch therefore has normalized block lengths
`(a_2,...,a_k,a_1)`, while the `a_1=1` branch has normalized block lengths
`(a_2,...,a_{k-1},a_k+1)`.  A normalized `L`-initial string is uniquely
determined by its block lengths.  This proves, for every size and including
`k=1`, the literal identity

\[
E\circ\Phi=\Psi\circ E.
\]

The proof is no longer merely a `run_lengths` comparison: `Psi(W)` itself is
defined and shown to equal the full normalized output string.

## 4. Path-only singleton clock, core, and both raw inverse strings

The direct path dynamics is correct.  Mark the maximal constant blocks of
length one.  A nonsingleton first block moves to the rear after normalization;
a singleton first block disappears and contributes one literal symbol to the
last block.  Consequently the last singleton-block index drops by one per
step and no singleton block is created.  A cyclic run of singleton blocks is
therefore absorbed, one symbol at a time, into the preceding nonsingleton
block.  Transporting the gap after the last original singleton block gives
the first surviving block after the final absorption.  This is a path-string
derivation of the clock and ordered core, not an invocation of the digit
recurrence.

The predecessor split is exhaustive.  Let `V=UZ`, where `Z` is the terminal
block.

1. If `V` has one block, its rotation predecessor is `V`.  Otherwise a
   rotation predecessor exists exactly when the terminal block of `U` has
   length at least two, and it is

   \[
   L^{|Z|}\overline U.
   \]

2. A deletion predecessor exists exactly when `|Z|>=3`.  Deleting the final
   symbol gives `V^-`, and the predecessor is

   \[
   L\overline{V^-}.
   \]

Direct substitution in `Psi` returns `V`.  Conversely, the `a>1` and `a=1`
branches force these strings, respectively, so there is no third source.
The first alternative has the target's block count; the second has one more
block, so they cannot collide.

The singleton boundary is explicitly correct.  For `V=L^b`, the rotation
source is `L^b`; when `b>=3`, the second source is

\[
L\overline{L^{b-1}}=LR^{b-1},
\]

whose quotient word is `eta(b)=(1,b-1)`.  For `b=2` this candidate would end
in a singleton block and is correctly rejected.  At the first nontrivial
boundary, `Psi(LRR)=LLL`, matching `(1,2) -> (3)` on the digit side.

## 5. Exact-depth layers, fibres, image/Garden counts, and Burnside edges

The exact-depth ordinary generating functions are correct as formal series.
At depth zero one has a nonempty sequence of parts at least two.  At exact
depth `t>=1`, the first `t-1` parts are arbitrary positive parts, part `t` is
one, and the nonempty suffix has all parts at least two.  Hence

\[
D_0(x)=\frac{x^2}{1-x-x^2},\qquad
D_t(x)=\frac{x^{t+2}}{(1-x)^{t-1}(1-x-x^2)}.
\]

With `F_0=0,F_1=1`, coefficient extraction gives

\[
[x^N]D_0=F_{N-1},\quad [x^N]D_1=F_{N-2},
\]

and, for `t>=2` and `M=N-t-2>=0`,

\[
[x^N]D_t=\sum_{j=0}^{M}
\binom{j+t-2}{t-2}F_{M-j+1}.
\]

The coefficient is zero for `N<t+2`.  Summing over all `t` simplifies to
`x^2/(1-2x)`, recovering `2^{N-2}`.  The delicate boundaries `N=2,3` and
`t=0,1` have the displayed values with no shifted Fibonacci index.

For a target `y=(b_1,...,b_l)`, inversion of the three update cases gives
exactly:

- `rho(y)=y` for `l=1`;
- `rho(y)=(b_l,b_1,...,b_{l-1})` for `l>1` when `b_{l-1}>=2`;
- `eta(y)=(1,b_1-1)` for `l=1` when `b_1>=3`;
- `eta(y)=(1,b_1,...,b_{l-1},b_l-1)` for `l>1` when `b_l>=3`.

The two source types have different lengths.  Thus fibres have size `0,1,2`.
A target has no source precisely when it has length at least two and suffix
`(1,2)`.  This yields

\[
|\operatorname{im}\Phi|=
\begin{cases}
1,&N=2,3,\\
3\cdot2^{N-4},&N\ge4,
\end{cases}
\]

and Garden counts `0,1,2^{N-4}` for `N=2`, `N=3`, and `N>=4`.  In
particular, the `N=3` fibre over `(3)` is `{(3),(1,2)}`, while `(1,2)` itself
is the sole Garden target.

On the recurrent set, `Phi` is rotation.  For weight `N` and word length
`k`, the Burnside count

\[
\mathcal C_{N,k}=\frac1k\sum_{d\mid\gcd(N,k)}\varphi(d)
\binom{N/d-k/d-1}{k/d-1}
\]

is correct: a word with repetition factor `d` reduces to a length-`k/d`,
weight-`N/d` composition with every part at least two.  The edge
`N=2,k=1` gives `1`, and `N=2k` leaves the well-defined binomial
`binom(k-1,k-1)`.  The formula counts rotation orbits grouped by word length,
not primitive periods, exactly as the manuscript says.  Fixed states are the
constant digit words, so their number is `d(N)-1`.

These are correctly assigned zero contribution credit.  The primary
cyclic-composition sources really do cover compositions modulo cyclic shift
and restricted parts
([Gibson--Just--Wang](https://math.colgate.edu/~integers/s19/s19.pdf),
[Hadjicostas](https://cs.uwaterloo.ca/journals/JIS/VOL19/Hadjicostas/hadji2.html)).

## 6. What the 6,101,926-assertion verifier actually checks

I inspected the source rather than trusting the transcript or support prose.
`ASSERTIONS` begins at zero and is incremented only inside `check`; the final
number is printed from that live counter, not assigned as a constant.

| obligation | exact source check | audit result |
|---|---|---|
| Euclidean run identity | `run_lengths(path) == word` at line 270 | present as an encoding check |
| full raw output | `next_path == expected_next_path` at line 275 | compares complete `L/R` strings |
| raw self-map closure | `normalized_path(next_path)` at line 276 | checks normalized carrier membership |
| quotient summary after raw output | `run_lengths(next_path) == update(word)` at line 277 | additional, not the decisive comparison |
| raw clock | `raw_path_depth(path) == tail` at line 285 | direct singleton-block index |
| raw terminal iterate/core | raw `Psi` iteration at lines 288-293 followed by `path_iterate == subtractive_path(rational_value(core))` | compares the complete core string |
| both raw inverse strings | `path_literal == expected_path_literal` at line 305 | compares the ordered tuple of full strings |
| raw inverse legality | normalized-source and `raw_path_update(source_path) == target_path` at lines 306-309 | direct substitution of every raw source |
| complete digit fibre | literal sources, membership, substitution, and census at lines 299-315 | includes singleton `eta` through the generic line-248 branch |

Thus the decisive forward, core, and inverse assertions are not run-length
summaries.  `run_lengths` appears at lines 270 and 277 as useful additional
cross-checks, but line 275 compares the full output, line 293 compares the
full terminal raw string, and lines 305/309 compare and reapply the two full
inverse strings.

One limitation should be recorded accurately.  The expected core at line 293
is the raw encoding `E(kappa(w))` of the independently computed digit
marked-gap core; the verifier does not implement a fourth, separately named
`raw_path_core` oracle.  This is a strong full-string cross-engine comparison
and exactly supports the manuscript's finite-control claim, but it is not an
additional all-size proof.  The all-size path-only core statement rests on the
argument in Proposition 2.2, as it should.

Fresh control command:

```sh
fresh=$(mktemp /tmp/p131-review-b-verify-XXXXXX.txt)
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py > "$fresh"
cmp -s "$fresh" code/verification_output.txt
sha256sum "$fresh" code/verification_output.txt
wc -c "$fresh" code/verification_output.txt
```

The result was `cmp=0`; both files were **1,868 bytes** and had SHA-256
`caa4df1e70fd2bdb86aa5aeb1308c2baa74b5d5e560d73980f1f6886c91bc8c6`.
The fresh output reports every level `2<=N<=18`,
`ASSERTIONS=6101926`, `STATUS=PASS`, and the correct finite-evidence and
external-hold sentinels.

I also ran an unsaved reviewer control that imported no function from
`code/verify.py`.  It generated compositions by cut masks rather than the
author's recursion, evaluated rationals independently with exact fractions,
implemented the equality subtraction and raw `Psi`, built fibres by complete
source enumeration, and compared those fibres with both inverse-string
formulas.  It independently checked marked cores, orbit tails and periods,
all depth bins, image/Garden boundaries, singleton `eta`, and Burnside counts
for every state through `N=14`.  It passed **164,096** reviewer assertions.
The only initial failure in developing this reviewer check was my own use of
a `defaultdict`: looking up a Garden target inserted an empty key into my
temporary image dictionary.  Counting only nonempty fibres corrected that
reviewer-side bookkeeping error; no paper or canonical-control artifact was
changed.

## 7. Literal internal collision and owner subtraction

The P126 collision is literal, not rhetorical.  Under the carrier bijection
`B_N` above, write a composition of `N-1` as `c=(c_1,...,c_r)`.  The P131 map
transported to this composition carrier is

\[
T(c)=
\begin{cases}
c,&r=1,\\
(c_2,\ldots,c_{r-1},c_r+1,c_1-1),&r>1,\ c_1>1,\\
(c_2,\ldots,c_{r-1},c_r+1),&r>1,\ c_1=1.
\end{cases}
\]

Here the middle range is empty when `r=2`, so the last two branches read
`(c_2+1,c_1-1)` and `(c_2+1)`, respectively.

P126 acts on the same full composition carrier (with index shifted from `N`
to `N-1`) but uses the different synchronous substitution
`m -> (floor(m/2),ceil(m/2))` for every part `m>1`.  P126 already owns an
exact-depth census, pointwise and iterated fibres, and image/Garden
enumeration on this carrier.  P131 correctly receives no value merely for
renaming compositions as continued-fraction digits.

The residual mechanisms are genuinely different.  P126 has a single
attractor, balanced synchronous refinement, logarithmic maximum depth, and an
all-iterate kernel.  P131 has a one-place queue, last-singleton linear clock,
fibres at most two, and recurrent rotation cycles.  This supports the internal
firewall once the now-complete raw `L/R` engine is included.

The other two internal subtractions are also accurate and appropriately
narrow:

- P117 is on labelled cyclic binary words, not this carrier, but already owns
  cyclic run-reduction and recurrent-classification language; those generic
  interfaces receive zero credit here.
- P122 is on permutations, not this carrier, but already owns the
  sharp-linear-clock plus target-fibre/image/Garden presentation silhouette;
  that silhouette receives zero credit here.

P131 now names all three projects and states the collision and the mechanism
difference in `main.tex:119-130`, rather than hiding them in support files.
The external subtraction is also credible at the claimed, deliberately weak
level.  The cited primary sources cover the subtractive Euclidean cost,
Stern--Brocot/continued-fraction interface
([Reutenauer](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.1104/)),
finite words/continuants with prefixes and endings
([Kan](https://www.mathnet.ru/eng/sm10170)), periodic extended continuants
([Jones](https://zenodo.org/records/20597606)), and cyclic/restricted
composition enumeration.  The paper assigns all of these interfaces zero
credit and explicitly says that the owner screen is bounded and proves
neither novelty nor priority.  That is the correct epistemic ceiling.

## 8. Isolated build, four-page visual QA, fonts, and metadata

I copied only `main.tex` and `references.bib` to the isolated temporary
directory `/tmp/p131-review-b-build-Z0fdS0` and ran, in order:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages returned success.  The settled LaTeX log and BibTeX log have
no errors, warnings, undefined citations, undefined references, multiply
defined labels, overfull boxes, underfull boxes, or actionable rerun request.
The two `microtype` messages about character `029` are explicitly
`Package ... Info` notices that protrusion settings for an absent small-caps
character are ignored; they are not missing PDF glyphs or warnings.
BibTeX's `missing$ -- 6` line is its function-execution statistic, while its
actual `warning$` count is zero.

The isolated PDF is byte-identical to both `main.pdf` and `main_round1.pdf`:

- **4 pages**, **314,622 bytes**;
- SHA-256
  `931e9d5078f202a969b47dfee2a7a686808ca293da2945c82370ca6c9c0c702a`;
- A4 (`595.276 x 841.89 pt`), rotation zero, PDF 1.5;
- unencrypted, no form, no JavaScript, no metadata stream, and no suspect
  object reported by `pdfinfo`;
- blank PDF title, subject, keywords, and author fields; the visible author is
  `Anonymous`;
- **21/21** font rows embedded, subsetted, and Unicode-mapped; every row is
  Type 1;
- `pdfimages -list` reports no embedded raster image.

I rasterized all four isolated pages at 160 dpi and inspected each page, not
only thumbnails.  There is no clipping, overlap, malformed display, missing
glyph, accidental blank page, broken hyperlink text, or unreadable
bibliography entry.  Page breaks are clean; the owner-subtraction paragraph
continues naturally from page 1 to page 2, the raw formulas fit page 3, and
the complete references fit page 4.

## 9. Review-A re-entry matrix

| Review-A condition | round-one evidence | status |
|---|---|---|
| M1: define recurrence/depth, equality step, and marked cut | `main.tex:82-88,133-152` | **closed** |
| M2: literal raw `Psi` self-map | `main.tex:194-215` | **closed** |
| M2: all-size `E Phi = Psi E` | Proposition 2.2 and proof, `main.tex:216-236` | **closed** |
| M2: path-only clock/core and both inverse strings | `main.tex:238-263` | **closed** |
| M2: full-string verifier comparison | `verify.py:273-277,288-309` | **closed** |
| O1: name and subtract P117/P122/P126 | `main.tex:119-130` | **closed** |
| singleton target `eta(b)=(1,b-1)` | `main.tex:314-319`; verifier line 248 and raw line 148 | **closed** |
| marked-cut example | `main.tex:184-190` | **closed** |
| synchronize support documents | README/narrative/claims/control/plan/log agree | **closed** |
| rerun exact and isolated build controls | fresh byte matches above | **closed** |

## 10. Severity-ranked finding

### CRITICAL

None.

### MAJOR — mathematics or definitions

None.

### MAJOR — control or reproducibility

None.

### MAJOR — owner or internal scope

None.  The literal composition carrier is admitted, the conflicting internal
claim silhouettes are named, and the residual is restricted to the exact
P131 temporal conjunction plus its raw path engine.

### MINOR

**B1 — Qualify the P126 nonconjugacy sentence at the two smallest levels.**
The sentence at `main.tex:127-129` says the temporal differences “prove
nonconjugacy.”  This is correct for the graded families and levelwise for
every `N>=4`, but not literally levelwise at `N=2,3`:

- P131 on `R_2` and P126 on `Comp_1` are both a singleton fixed graph;
- P131 on `R_3` is `(1,2) -> (3) -> (3)`, while P126 on `Comp_2` is
  `(2) -> (1,1) -> (1,1)`, so the two functional graphs are isomorphic.

At `N=4`, P131 already has two recurrent fixed states whereas P126 has one
attractor, so levelwise nonconjugacy is immediate from there onward; for odd
`N>=5`, P131 also has a nontrivial recurrent rotation cycle.  Replacing “This
proves nonconjugacy” by “This proves nonconjugacy of the graded families (and
levelwise for `N>=4`)” would remove the only scope ambiguity.  This is a
nonblocking precision edit and does not affect any stated P131 theorem,
enumeration, or Review-A re-entry condition.

## 11. Allowed claim ceiling and final verdict

The admissible internal contribution remains only the literal conjunction
for this specific finite map:

1. the canonical rational half-level and explicitly normalized quotient
   queue;
2. the last-one entrance clock, sharp `N-2` witness, and marked-gap terminal
   core;
3. the full normalized raw-path self-map, all-size conjugacy, singleton-block
   absorption, and complete raw predecessor split;
4. every exact-depth OGF layer and coefficient formula;
5. every one-step `0/1/2` fibre, image, and Garden census;
6. recurrent rotation classification and pointwise primitive period.

The Burnside orbit count and divisor fixed count may remain only as
zero-credit classical corollaries.  No contribution claim is permitted for
canonical finite-CF uniqueness, terminal-one normalization, Euclidean
digit-sum cost, Stern--Brocot coding, continuants, general composition
dynamics, regular-language machinery, cyclic-composition enumeration,
Burnside, or divisor counting.  The paper must continue to make no novelty,
priority, ownership, posting, or submission claim.

**Final Review-B verdict: GO_INTERNAL.**  Review A's substantive re-entry
conditions are closed, and B1 is editorial rather than gate-blocking.

**External status: HOLD_EXTERNAL.**  Re-entry to any external-release gate
requires a specialist primary-source owner search focused on literal cyclic
finite-CF quotient transformations and Euclidean path queues, an explicit
claim-to-owner matrix, resolution of authorship/release authority, and a new
independent release decision.  A bounded non-hit can never by itself satisfy
that gate.
