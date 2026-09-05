# P204 Review A — reconstructed proof and exact owner adapter

Reviewer: `/root/batch197_lzk_gate`, 2026-09-05 UTC.
Input: the complete, immutable `frozen_round0/` package recorded in
`INPUT_PINS.sha256` (22 scientific/documentary files plus its manifest).
I did not author NS, its proof, verifier, candidate gate or outline review.
I can see the shared collaboration background; this is process-separated
review, not blind review or an external human/specialist assessment.

Verdict: **MATH_VALID / KILL_VALUE_INVERSE_AXIS_MACMAHON_ADAPTER**.
The proof below is a reviewer reconstruction and collision attack. It is not
new manuscript text, a repaired author lemma, or permission to extend scope.

## 1. Representation and dependency separation

My checker constructs every arrow by enumerating all earlier-index
comparisons. It removes indegree-zero vertices with Kahn's queue, identifies
the remaining cycles, and propagates exact tail/period labels backwards.
It does not use the claimed core to decide which vertices are recurrent or
which tail they have. A separately generated core language is compared with
that graph. All source/target checks are on the full $E_n$, not samples.

The source counter fixes a right-hand successor and recursively chooses
letters from right to left. Its state consists of a prefix length and the
already chosen following value; a transition admits precisely the requested
strict ascent or weak nonascent. It uses neither cut segments nor signed
terms. A second, separately written routine evaluates the manuscript's cut
formula. A third representation counts descent masks of actual permutations
and their classical inversion codes. These choices differ from the author's
backward nearest-smaller scan, core-derived tail assignment and direct
Cartesian-product word count. No author/candidate/old-paper code is imported.
The candidate review itself is not reused as manuscript-review evidence.

## 2. Reconstructing Theorem 2.2, including boundaries

All entries are nonnegative, $x_0=0$, $0\le x_i\le i$, and the update is
synchronous. A positive output distance cannot exceed $i$, so the carrier
is closed. A zero has no strictly smaller predecessor; every positive entry
has the earlier zero at position $0$. Thus the zero set is invariant.
Within a positive block after a zero at $r$, every closest predecessor is
at least $r$; preceding blocks have no influence and the local output is
between $1$ and $j$ at position $r+j$.

Write $p_j$ for that closest predecessor and $b_j=r+j-p_j$. At the first
position $b_1=1$. For $j\ge2$, if $b_j>1$, the adjacent source value is
not strictly smaller, so $x_{r+j}\le x_{r+j-1}$. Every index strictly after
$p_{j-1}$ and before $r+j-1$ has value at least $x_{r+j-1}$ by maximality
of $p_{j-1}$. The index $r+j-1$ also cannot precede a smaller value for
the current letter. Therefore $p_j\le p_{j-1}$, including when two source
values are equal, and $b_j\ge b_{j-1}+1$. No unstated distinctness assumption
is used. Conversely $b_j=1$ exactly when the original adjacent pair rises.

Now recompute on $b$. If $b_j=1$, no positive block entry can be smaller,
and the closest zero at $r$ gives distance $j$. If $b_j>1$, the inequality
above makes $b_{j-1}$ strictly smaller, giving distance $1$. This proves
the displayed second-step decoder for every coordinate. In particular the
second image lies in the claimed block core.

For a core letter equal to its local index $j\ge2$, the preceding core
letter is at most $j-1$, and the next output is $1$. For a core letter $1$,
the closest smaller value is its left zero, giving $j$. At $j=1$ both
descriptions coincide; this coordinate is fixed, not a two-choice bit.
Thus the restriction is exactly $J$, with $J^2=\mathrm{id}$. Every core
word is its own two-step preimage. Surjectivity onto the core and
$P^4=P^2$ follow. A periodic point has a two-step predecessor on its cycle,
so it lies in the second image; there are no recurrent points outside it.

At $n=1$ there is one fixed state. At $n=2$ the states $00,01$ are fixed.
At $n=3$ the six stated words are exhaustive; $002\mapsto001$ is the only
transient arrow into the core. At $n\ge4$, the zero-prepended $0122$ lies
in the carrier and its first image has positive block $112$, whose final
coordinate is not in $\{1,3\}$. Its first image is therefore not recurrent,
whereas its second image is. This proves the sharp height $2$ for every
such $n$, not just for the checked lengths. The graph checker independently
recovers these boundaries and also tests the witness through $n=32$.

The census recurrence uses one choice when starting a positive block and
two only when continuing it. With $(a_0,b_0)=(1,0)$ it gives
$(a_{N+1},b_{N+1})=(a_N+b_N,a_N+2b_N)$, hence the claimed Fibonacci total.
A fixed word has only singleton positive blocks: a block of length at least
two has a genuine coordinate $j=2$ exchanged by $J$. Counting binary words
without adjacent ones gives $F_{n+1}$; all other recurrent words pair into
strict two-cycles. These are valid corollaries, not a separate novelty axis.

## 3. Reconstructing Theorem 3.1

For every integer $t\ge2$, the temporal theorem gives
$P^t(x)=J^{t-2}P^2(x)$. Zeros force exactly the target's block positions.
For an even time, a target coordinate equal to local $j$ means an original
ascent. For an odd time, it is the target value $1$ that means an original
ascent. The offset used in source bounds is the global $r$, whereas $j$
in the target decoder is local. Confusing these two indices would be an
error; the frozen statement and proof do not confuse them.

Let $A$ be the required set of local positions $j\ge2$ immediately after
an ascent. Initially enforce nonascent outside $A$. Inclusion-exclusion
removes the failures among required ascent positions. For $B\subseteq A$,
the surviving unspecialized count allows rises only before positions in
$B$, with sign $(-1)^{|A|-|B|}$. Cutting there leaves weakly decreasing
segments. On a segment $[a,b]$, all values are bounded by the first value,
at most $r+a$; later flags are larger and impose no additional restriction.
Positive weakly decreasing words of that length are counted by the
multiset coefficient $\binom{r+b}{b-a+1}$. Segment products and the signed
sum are therefore correct. Distinct positive blocks are independent after
zeros are fixed. Noncore targets have zero fibre, and the all-zero target
has the unique all-zero source by the empty product. Cases $m=1$, $A$ empty,
$A$ full, $r=0$ and every $n\ge1$ are included without extra hypotheses.

This establishes mathematical validity of the frozen formula. It does not
establish independent research value of its enumerative mechanism.

## 4. Decisive formula-level adapter to classical descent sets

Put $S=A-1=\{j-1:j\in A\}\subseteq[m-1]$, and let
$\beta_m(S)$ count permutations of $[m]$ with exact descent set $S$.
For all $r\ge0$, $m\ge1$ and all $A$, the exact adapter is

$$D_{r,m}(A)=\binom{r+m}{m}\,\beta_m(A-1). \tag{A.1}$$

Here is an explicit all-parameter double count, using the classical
inversion code stated in the cited Lin–Kim introduction. It is a reviewer
collision deduction, not a claim that Lin–Kim states (A.1) verbatim.

1. Given a positive source block $w_j\in[1,r+j]$, put $e_{r+j}=w_j-1$
   for $1\le j\le m$. These are exactly the final $m$ coordinates of a
   length-$r+m$ inversion code $0\le e_i\le i-1$ in one-based notation.
2. Fill the first $r$ coordinates by any inversion code of length $r$.
   There are exactly $r!$ independent choices, including one when $r=0$.
   The ordinary bijection
   $e_i=|\{h<i:\pi_h>\pi_i\}|$ maps these completed codes to permutations
   of $[r+m]$.
3. This code has $e_i<e_{i+1}$ if and only if $\pi_i>\pi_{i+1}$.
   Thus the internal ascent set of the block is precisely the descent set
   of the relative permutation of the final $m$ letters. The common
   subtraction by one does not change comparisons, and only internal
   edges are constrained; no hidden edge across the first $r$ letters is
   imposed.
4. Count full permutations with a permitted suffix relative order instead.
   Choose the suffix's $m$ labels in $\binom{r+m}{m}$ ways, choose its order
   in $\beta_m(S)$ ways, and arrange the remaining $r$ labels in $r!$ ways.
   Equating this count to $r!D_{r,m}(A)$ and cancelling $r!$ proves (A.1).

The static $β$ itself has MacMahon's classical evaluated formula. If
$\delta(T)$ is the composition of $m$ cut at $T\subseteq S$, then

$$\beta_m(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}
              \frac{m!}{\prod_{d\in\delta(T)}d!}. \tag{A.2}$$

Theorem 2.3 in the directly opened author paper *Descent polynomials*
records this formula and credits MacMahon. Hence (A.1) is not merely a
vocabulary overlap with Eulerian numbers. It replaces **every** flagged
block count by an ordinary exact-descent-set coefficient and a binomial
scale. The full paper fibre becomes a product of these classical factors
after inserting the mask already supplied by Theorem 2.2. No additional
independent inverse mechanism remains in the registered contract.

### Phase counts and the precise limit of the framing objection

The complement involution $\sigma_i\mapsto m+1-\sigma_i$ gives
$\beta_m(S)=\beta_m([m-1]\setminus S)$. Consequently

$$D_{r,m}(A)=D_{r,m}(\{2,\ldots,m\}\setminus A),\qquad
  |(P^{2k})^{-1}(y)|=|(P^{2\ell+1})^{-1}(y)| \tag{A.3}$$

for all $k\ge1$, $\ell\ge1$ and all targets $y$. Counts in fact do not
depend on the time once it is at least two. Source sets and their semantic
target direction can still differ: $011$ is sent to $011$ at time two and
to $012$ at time three. My checker therefore includes 471,132 **pointwise**
phase-mask checks; aggregate fibre counts alone cannot detect a swapped
phase mask. This is a testing distinction, not a counterexample to (8) or (9).

The frozen `sections/03_fibres.tex:64`–`:67` only establishes that the
offset scale cannot be omitted. Its example is numerically correct, and
(A.1) retains that scale; it refutes no literal equation there. The word
“unflagged” also must not be confused with an ordinary univariate Eulerian
polynomial, which forgets the exact set. What fails is the attempted value
separation from **scaled exact-set** enumeration, not the elementary claim
that dropping $r$ altogether changes the answer. Similarly the abstract's
phase wording is defensible for source identities, but supplies no separate
phase-dependent counting phenomenon. These are framing consequences of the
single critical value finding, not fabricated mathematical errors.

## 5. Exact internal collisions checked

P134's literal update recomputes longest proper-border lengths on the same
factorial carrier. For $n\ge2$, its second coordinate sends $0\leftrightarrow1$;
it therefore has no fixed point. P204 has fixed points. This rules out
full-carrier conjugacy and same-size surjective factors (which would be
bijective). P134's indexed mismatch propagation and forced-last-letter
factorial fibre bound do not supply the nearest-smaller predecessor
inequality. Their actual manuscript definitions and proofs were read.

P185 recomputes the number of distinct letters in each strict prefix on
$[n]_0^n$. Its first-image binary-rise path is shifted one place at each
later time; all states reach one fixed identity word. It cannot surjectively
factor onto P204's strict two-cycle systems ($n\ge3$). Conversely a factor
of a system satisfying $P^4=P^2$ inherits that identity. P185 does not at
$n=4$, as its displayed $0013\to0112\to0122\to0123$ trajectory shows;
its general height is $n-1$. This is a concrete boundary, not a blanket
claim that prefix feedback is new. These internal noncollisions leave the
temporal result alive, but do not rescue the inverse axis from (A.1).

## 6. Actual primary-source contexts and limits

- Berkman–Schieber–Vishkin (1993), DOI 10.1006/jagm.1993.1018:
  [Technion primary record](https://cris.technion.ac.il/en/publications/optimal-doubly-logarithmic-parallel-algorithms-based-on-finding-a/)
  was reopened. Its abstract explicitly specifies smaller values on either
  side and its metadata agrees with the manuscript. This supports §1's
  static-search attribution only; the full 27-page article was not read.
- Park–Amir–Landau–Park (CPM 2019):
  [publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2019.16)
  and [publisher PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol128-cpm2019/LIPIcs.CPM.2019.16/LIPIcs.CPM.2019.16.pdf)
  were opened. Definition 2 on printed 16:3 uses earlier $\le$, and Algorithm
  1 on 16:5 retains that tie convention. This supports the Cartesian-code
  sentence and the explicit strict/weak distinction, not P204's feedback.
  The PDF is pinned locally; only the relevant introductory/definition/
  algorithm sections are asserted read, not an audit of all indexing results.
- Lin–Kim, DOI 10.1016/j.jcta.2017.11.009:
  [author PDF](https://mathsci.kaist.ac.kr/~dskim/papers/LinKim161209v2.pdf)
  was reopened and downloaded. It is the 18-page version dated 22 December
  2016, with the natural code on printed page 1, ASC/DES identity and (1.1)
  on page 2, and Remark 5.4/Theorem 6.1 on page 17. The introduction and
  those contexts support both §1 and §4 citations. No restricted avoidance
  theorem is applied to the full carrier. DOI BibTeX was fetched successfully
  and confirms author order, journal, volume 155, 267–286, year 2018. The
  final publisher body failed to open; no final-body read is claimed.
- Diaz-Lopez–Harris–Insko–Omar–Sagan, *Descent polynomials*, author version
  dated 12 November 2017:
  [author PDF](https://users.math.msu.edu/users/bsagan/Papers/Old/dp.pdf)
  was opened and downloaded. Definition of exact descent counts, Proposition
  2.1 and Theorem 2.3 with proof on printed pages 2–5 were read. This is
  a directly read primary paper reproducing and crediting MacMahon's
  formula; the original 1915 book was not opened and is not claimed read.

The first three entries exhaust the frozen bibliography and its four
citation occurrences. The fourth is the newly used owner-formula source.
An attempted Zhuang thesis PDF failed; no result depends on that attempt.
Bounded literal searches combined previous/nearest smaller, iteration,
inversion sequences, exact ascent/zero sets and permutation descent
enumeration. Several returns were irrelevant or secondary and were not
used as proof authorities. No search nonhit, recent crawl timestamp,
retraction check, global-priority or specialist certificate is claimed.

## 7. Final subtraction and boundary

The nearest-smaller search, Cartesian encoding, inversion code,
Fibonacci arithmetic, multiset count, inclusion-exclusion and exact
permutation descent-set enumeration all receive zero primitive credit.
Theorem 2.2 remains a valid literal feedback result; this review has not
shown it to be a classical iterate or an internal conjugate. However,
Theorem 3.1 now reduces fully to (A.1)–(A.2), with its target mask already
provided by the temporal theorem. Under this batch's two-axis admission
bar, the independent inverse axis is lost. The appropriate conclusion is
KILL_VALUE, not a wording-only repair or enlargement of the test cutoff.
No author lemma is supplied to manufacture a replacement contribution.
The frozen manuscript and all historical acceptance records stay unchanged.
