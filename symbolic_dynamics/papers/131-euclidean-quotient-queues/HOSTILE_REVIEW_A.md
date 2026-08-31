# Hostile Review A — P131 Euclidean quotient queues

**Role:** independent nonauthor reviewer.  **Audit date:** 2026-08-31.
**External status:** **HOLD_EXTERNAL**.  **Provisional verdict:**
**GO_IF_REPAIRED (internal only)**.

The principal formulas survive reconstruction and fresh exact control.  I find
no counterexample to the marker clock, cyclic absorption, layer series,
pointwise fibre law, image/Garden census, or Burnside count.  The draft is not
yet ready for an internal freeze for two reasons.  First, several objects used
in the main theorem are described but not defined with the precision needed at
the boundary: `depth`, recurrence, the equality subtraction, and the cut in
the contracted cyclic word.  Second, the advertised “independent” (L/R)
route is currently the digit proof transported to run lengths; both the prose
and verifier compress the path back to the quotient tuple before making the
dynamical comparison.  That is a valid encoding check, but it does not yet
clear the paper's own second-engine/P126 value gate.  The main text also hides
P117/P122/P126 behind unnamed descriptions rather than performing the promised
explicit zero-credit subtraction.

Severity summary: **CRITICAL 0; MAJOR (math/definition) 2; MAJOR
(owner/internal scope) 1; MINOR 3**.

## 1. Reviewed artifacts and reproducibility

| artifact | SHA-256 at review |
|---|---|
| `main.tex` | `19f110f77b792bdce48e2d6b0a9735c0a8b3b26c8f017906216c89e432910734` |
| `references.bib` | `7b9c097dbe6423895699e054f1f590eeda7759e5abbe795ed27bd4e03f2a0c68` |
| `code/verify.py` | `f99ab05f4434de016a5c4bec10059e4e9513ade2fde33b1dca7d55b271986d12` |
| `code/verification_output.txt` | `77af5bffbc21dc60ac1d4486fa20d2d800a8447fab40496b7d9763328d61f988` |
| `main.pdf` | `ec8fa88db4ca4bf83db02e758afa626238bb333c300ba7065caf2c8130c87d61` |
| `main_round0_original.pdf` | `ec8fa88db4ca4bf83db02e758afa626238bb333c300ba7065caf2c8130c87d61` |
| `README.md` | `a4ceaf27c2ecacc14ef320911f7d329b269417d2d41cfed3ba1ab48ad200d44b` |
| `PAPER_PLAN.md` | `4ced561fce321296aa107fcd002dc34ac79ea2c8d48f0efbdf1cfa6b280d0048` |
| `NARRATIVE_REPORT.md` | `75926e1a95a94559c07018e60eedcf37be3fd6e4d84b6b0f5dfb55fede16e830` |
| `CLAIMS_EVIDENCE.md` | `55215f4d1dad5894424cfbd817f6326d611357d8d4c044b8b55ba7c4b0bd7621` |
| `CONTROL_RESULTS.md` | `8bbb68a74390359f383b6899e39053da042b435e7546cffdf0106ec685dda626` |
| `BUILD.md` | `7be73a2778ad18d651354547775a1df348d7d6adf2e3bd404ea1bc70d6b7e4dc` |
| `IMPROVEMENT_LOG.md` | `a38b7e4b5c9af4a984e96bd08aa37b1977f8b5ee4b9c21d9c31fcffe5dc54648` |

Fresh verifier command:

```sh
fresh=$(mktemp /tmp/p131-reviewA-verify-XXXXXX.txt)
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py > "$fresh"
cmp "$fresh" code/verification_output.txt
sha256sum "$fresh"
```

The comparison passed byte for byte.  Fresh stdout has SHA-256
`77af5bffbc21dc60ac1d4486fa20d2d800a8447fab40496b7d9763328d61f988`
and reports **2,097,489 assertions**, every state for (2\le N\le18),
and `STATUS=PASS`.

I also wrote no paper artifact but ran a temporary independent control from a
cut-set construction of compositions, separate rational continuants and
subtractive paths, a raw normalized path-string queue, brute orbit tails, and
literal target fibres.  It checked every state for (2\le N\le14) and passed
**32,894 reviewer assertions**.  In particular it verified the stronger raw
identity suggested in repair M2 below; this is evidence that the repair is
available, not a substitute for an all-size proof in the paper.

An isolated temporary build used

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled log and `.blg` contain no warnings, undefined citations,
undefined references, or over/underfull boxes.  The isolated PDF is
byte-identical to `main.pdf`: **4 pages, 307,148 bytes**, A4, rotation zero,
unencrypted, no forms or JavaScript, blank PDF author field, and all displayed
fonts embedded Type 1.  All four rasterized pages are visually clean.  The six
bibliography entries are closed in the build.

## 2. Carrier and subtractive Euclid convention

The repaired carrier is mathematically honest.  Every (q\in(0,1)\cap
\mathbb Q) has exactly one finite canonical expansion

\[
q=[0;a_1,\ldots,a_k],\qquad a_i\ge1,\quad a_k\ge2.
\]

At digit sum (N), replacing (a_k) by (a_k-1) gives a bijection to
positive compositions of (N-1).  Thus the carrier is empty at (N=0,1),
has (2^{N-2}) states at (N\ge2), and the single (N=2) state is
([0;2]=1/2).  Equation (3) preserves both weight and the final-digit
condition, including the one-part branch.

The intended subtractive convention is also correct, but “repeat the
preceding letter and send that coordinate to zero” is not a literal update.
At equality (u=v), the manuscript should say: if the preceding letter was
(L), perform (v\leftarrow v-u=0); if it was (R), perform
(u\leftarrow u-v=0), recording that same letter.  The preceding letter
always exists because (0<u<v) at the start.  With this convention
(E(1/2)=LL), (E(2/3)=LRR), and in general
(E(q)=L^{a_1}R^{a_2}\cdots) has length (sum_i a_i=N).  This is precisely
the convention whose cost belongs to the established Euclidean literature,
not a new result.

## 3. Clock and cyclic terminal core

Let (j=\max\{i:a_i=1\}), with (j=0) when there is no one.  If the first
digit exceeds one, rotation decreases every one-position by one.  If the
first digit is one, deletion removes it, decreases every remaining
one-position by one, and creates no one because the final digit was at least
two.  Therefore (j) falls by exactly one until zero.  Once zero, the word
is under a finite rotation and hence is recurrent.  This proves the intended

\[
\operatorname{depth}(w)=\max\{i:a_i=1\}.
\]

The proof also correctly contracts each maximal cyclic run (1^s) into the
non-one digit immediately preceding it by adding (s).  After deleting the
last original one, the first digit is the first original non-one following
that marked position; this supplies the intended ordered cut.  The witness
((1^{N-2},2)) has depth (N-2), and the final-digit constraint gives the
matching upper bound.  The (N=2) maximum is zero.

There is nonetheless a definition gap.  `\depth` is introduced only as a
typesetting macro and is never defined as the least entrance time to the
recurrent set; “recurrent” is likewise not defined as lying on a directed
cycle of this finite map.  Moreover, after the ones are deleted, “cut ...
after the last original one” does not literally name a surviving vertex.
The theorem proof reveals the intended marked gap, but the definition must
say so before the theorem.  This is repair M1, not a failed formula.

## 4. Exact-depth series

The layer calculation is correct as a formal OGF.  At depth zero one has a
nonempty sequence of parts at least two, giving

\[
D_0(x)=\frac{x^2}{1-x-x^2}.
\]

At exact depth (t\ge1), the first (t-1) parts are arbitrary positive
parts, part (t) is one, and the nonempty suffix has all parts at least two.
Hence

\[
D_t(x)=\frac{x^{t+2}}{(1-x)^{t-1}(1-x-x^2)}.
\]

Using ((1-x-x^2)^{-1}=\sum_{m\ge0}F_{m+1}x^m) gives exactly the displayed
coefficient convolution.  The separate (t=0,1) formulas and the zero range
(N<t+2) are correct.  Direct summation gives

\[
D_0+\sum_{t\ge1}D_t=\frac{x^2}{1-2x},
\]

so the coefficient sum is (2^{N-2}).  I found no offset error at
(N=2,3) or (t=0,1).

## 5. Full target fibres, image, and Garden states

For a target (y=(b_1,\ldots,b_\ell)), the exhaustive predecessor split is
correct:

- the rotation predecessor is (y) when (ell=1), and is
  ((b_\ell,b_1,\ldots,b_{\ell-1})) when (ell>1) and
  (b_{\ell-1}\ge2);
- the deletion predecessor is
  ((1,b_1,\ldots,b_{\ell-1},b_\ell-1)) when (b_\ell\ge3).

The two applicable words have different lengths, so there is no collision.
There is no third update branch.  A target has no predecessor exactly when
it has length at least two and suffix ((1,2)).  This gives Garden counts

\[
0,\ 1,\ 2^{N-4}
\quad\text{for }N=2,\ N=3,\ N\ge4,
\]

and image sizes (1,1,3\cdot2^{N-4}), respectively.

The only present defect is syntactic but real: the displayed formula for
(\eta) uses (b_1,\ldots,b_{\ell-1}) without a separate (ell=1) case.
For a one-part target ((b)), it must explicitly read (eta(b)=(1,b-1))
when (b\ge3).  Thus ((2)) has one predecessor, while every singleton
((b)) with (b\ge3) has the two predecessors ((b)) and ((1,b-1)).

## 6. Recurrent cycles and Burnside

The recurrent states are precisely the words with all parts at least two,
and (Phi) acts there by left rotation.  For fixed weight (N) and length
(k), a rotation with repetition factor (d) fixes a word only when
(d\mid\gcd(N,k)); the base word then has length (k/d), weight (N/d),
and parts at least two.  Its count is

\[
\binom{N/d-k/d-1}{k/d-1}.
\]

There are (arphi(d)) rotations of repetition factor (d), so equation
(9) is the correct Burnside orbit count.  It counts rotation orbits grouped
by digit length, not primitive cycles grouped by their actual period, and
the manuscript correctly refuses a zeta upgrade.  Fixed states are constant
words; choosing their common digit is equivalent to choosing a divisor of
(N) other than one, yielding (d(N)-1).  These are classical necklace and
divisor consequences and deserve exactly the zero credit assigned to them.

## 7. The alleged second (L/R)-block proof

The path discussion is correct as a coordinate translation.  If a normalized
alternating path has block lengths ((a_1,\ldots,a_k)), move the first block
length to the end, relabel the alternating blocks to start at (L), and, when
the moved block has length one, merge that terminal singleton into its
predecessor.  The resulting block lengths are equation (3).  Singleton
blocks are therefore the quotient ones, so the same marker invariant gives
the same clock and contraction.

What is not yet justified is the word **independent**.  The manuscript first
defines (Phi) only on the quotient tuple, then describes the path operation
in terms of those same blocks.  The verifier's `path_queue` immediately calls
`run_lengths(path)` and returns a tuple, and the decisive comparison is
`path_queue(path) == update(word)`.  It never defines a raw path self-map or
proves a path-string identity before compressing back to the digit carrier.
The “last singleton block” proof is literally the “last digit one” proof
under a bijection.  This is a useful independent *implementation of the
encoding*, but not yet a substantively different theorem route or a firewall
against P126's composition carrier.

There are two honest choices:

1. demote the subsection, abstract, README, narrative, and control language
   from “independent/second derivation” to “equivalent (L/R)-block
   encoding”; under the phase-one value gate this also demotes P131 to
   **RESERVE/KILL** because P126 remains the only proof carrier; or
2. define a literal normalized path-string map (Psi), prove for every
   rational that
   
   \[
   E(\Phi(q))=\Psi(E(q)),
   \]
   
   prove the singleton absorption and at least the complete predecessor split
   directly in the path language, and add an exact assertion comparing the
   full output strings rather than only their run-length tuples.  The path
   proof should state the forward operation, the terminal merge, the converse
   inverse alternatives, and why normalization beginning at (L) is unique.

My temporary raw-string control confirms option 2 for all states through
(N=14), so this is a proof-writing obligation rather than evidence of a
false theorem.

## 8. Owner subtraction and the P126 firewall

The bibliography is relevant and the following attribution ceiling is
correct:

- Minelli--Sourmelidis--Technau's
  [Euclidean-cost paper](https://doi.org/10.1007/s00208-022-02452-2) owns the
  subtractive step-count/digit-sum interface; it receives zero credit.
- Reutenauer's
  [Stern--Brocot expansion paper](https://doi.org/10.5802/jtnb.1104) owns the
  continued-fraction/run-word and cyclic-word infrastructure; it receives
  zero credit.
- Kan's 2026
  [continuant paper](https://www.mathnet.ru/eng/sm10170) explicitly treats
  canonical finite words, prefixes/endings, matrix products, and continuant
  uniqueness; Jones's 2026
  [extended-continuant paper](https://zenodo.org/records/20597606) covers
  periodic words and cyclic/reversal interfaces.  None of that machinery is
  residual.
- Gibson--Just--Wang's restricted cyclic compositions and Hadjicostas's
  [cyclic-composition paper](https://cs.uwaterloo.ca/journals/JIS/VOL19/Hadjicostas/hadji2.html)
  own the cyclic/restricted composition and necklace enumeration used in the
  recurrent corollary.

The current main text cites these sources and states the broad zero-credit
categories.  A bounded search dated 2026-08-31, including exact variants of
“finite continued fraction cyclic shift partial quotients,” “Euclidean
quotient sequence cyclic rotation,” “trailing-one normalization,” and
“Stern--Brocot block queue,” did not locate a primary source stating this
literal finite map together with its terminal clock and target fibres.  This
is only a bounded non-hit and supports neither novelty nor priority.

The internal subtraction is not yet acceptable.  The main manuscript says
only that “earlier systems” occupy three unnamed mechanisms; only support
files identify P117/P122/P126.  The paper itself must say explicitly:

- P117 already owns cyclic run reduction/recurrent classification vocabulary;
- P122 already owns the sharp linear clock plus target-fibre/image/Garden
  presentation silhouette;
- P126 is the hard collision: after replacing the final quotient (a_k) by
  (a_k-1), the present carrier is literally the full composition set of
  (N-1), while P126 already owns a composition map with exact depth layers,
  pointwise fibres, and image enumeration.

The maps are nonconjugate—P126 has synchronous balanced refinement,
logarithmic absorption, an all-iterate kernel and one attractor; P131 has a
one-place queue, linear marker depth, fibres at most two, and many rotation
cycles.  That difference permits an internal residual only if the raw
Euclidean-path engine in section 7 is completed.  Renaming the composition
coordinates “rational quotients” is not itself portfolio value.

## 9. Severity-ranked findings and executable repairs

### CRITICAL

None.  I found no false displayed theorem and no counterexample in either
fresh exact engine.

### MAJOR (mathematics/definition)

**M1 — Close the foundational definitions before Theorem 2.1.**  Define a
recurrent state as one lying on a directed cycle and define
(\depth(w)=\min\{t\ge0:\Phi^t(w)\text{ is recurrent}\}).  Replace the
ambiguous equality instruction by its two literal coordinate cases.  Define
(\kappa)'s cut as the marked gap immediately before the first surviving
original non-one following the last original one.  State that a non-one
always exists because (a_k\ge2).

**M2 — Supply the claimed second engine or demote the paper.**  Add the raw
normalized path map (Psi), the all-size proof
(E\circ\Phi=\Psi\circ E), a path-only absorption/cut proof, and path-only
derivation of the two inverse alternatives.  Add a full path-string verifier
comparison.  If the authors instead retain only run-length relabelling, all
claims of an independent/second derivation must be removed and the project
returns to **RESERVE/KILL** under the P126 collision gate.

### MAJOR (owner/internal scope)

**O1 — Put the explicit internal subtraction in `main.tex`.**  Name and
zero-credit P117, P122, and especially P126, state the literal composition
bijection, and describe the exact nonconjugate mechanism rather than relying
on unnamed prose or support documents.  Keep the external owners above
itemized and all bounded non-hits non-novelty.

### MINOR

1. Give (eta(b)=(1,b-1)) as a separate (ell=1) branch; the present
   ellipsis is syntactically undefined at that boundary.
2. Add one displayed example containing a cyclic one-run and its marked cut,
   for example ((2,1,3)\mapsto(1,3,2)\mapsto(3,3)), to make the ordering in
   (kappa) auditable.
3. After repairing M2, synchronize `README.md`, `NARRATIVE_REPORT.md`,
   `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`, and `IMPROVEMENT_LOG.md`; at
   present they state that the independent path route and explicit P117/P122/
   P126 firewall are already complete, which overstates the source.

## 10. Allowed claim ceiling and verdict

After repairs, the admissible residual is only the conjunction for this
literal self-map:

1. the canonical ((0,1)) rational level and explicit quotient queue;
2. the last-one entrance clock, sharp (N-2) witness, and ordered cyclic
   absorption core;
3. formal exact-depth OGFs and their coefficient formulas;
4. complete one-step (0/1/2) target fibres, image, and Garden census;
5. recurrent rotation classification and pointwise primitive period.

The Burnside and fixed formulas may remain as zero-credit classical
corollaries.  No claim is allowed for canonical CF uniqueness, Euclidean
cost, Stern--Brocot coding, continuants, composition enumeration, necklace
enumeration, general continued-fraction dynamics, all positive rationals,
novelty, or priority.

**Final Review-A verdict:** **GO_IF_REPAIRED** for internal continuation,
provided M1, M2, O1 and the singleton-fibre boundary are visibly closed and
fresh exact/build controls are rerun.  If M2 is not closed as a genuine raw
(L/R)-path engine, the fallback verdict is **RESERVE/KILL**, not paper
freeze.  External release remains **HOLD_EXTERNAL** in every case.
