# Hostile Review B — P172 fresh-map self-image erosion

**Reviewer:** independent Reviewer B; no author/scout/Review-A code was
imported, and Review A was not used as a premise for any finding below.  
**Review date:** 2026-09-03 UTC  
**External state:** `HOLD_EXTERNAL` (unchanged)  
**Disposition:** `MAJOR_REVISION / MATHEMATICS_SURVIVES`  
**Manuscript/PDF edits in this turn:** none

## 1. Bottom line

I found no counterexample to the stated finite-dynamical results.  The
endpoint count, every-time labelled lift, algebraic spectrum, forced top
`J_2`, absorption statements, and multiepoch marked-kernel product all
survive independent re-derivation.  The separate executable control passes
`20,317` exact assertions.

The manuscript is nevertheless not ready to advance externally.  Its owner
subtraction misses a direct specified-bin/extended-occupancy formulation of
the entire one-step size row, and the multiepoch matrix product is presented
without formally separating the generic marked-kernel mechanism from the
literal one-step refinement.  Its internal subtraction is also too vague:
P158, P162, P170, and the sibling P173 must be named, and the shared proof
shell must be assigned zero credit.

There are therefore **no Critical findings, three Major findings, and five
Minor findings**.  All three Major repairs are mandatory before another
external-value gate.

## 2. Normalized theorem and independent re-derivation

Fix `n >= 1`.  Given a current set `A subseteq [n]`, sample a fresh uniform
endomap `f:[n] -> [n]` and set

\[
    \Phi_f(A)=A\cap f(A).
\]

Write `a=|A|`, fix `B subseteq A` with `b=|B|`, and set
`K=|f(A)|`.  Only `f|_A` is visible, and its `n^a` possibilities are uniform.

### 2.1 Endpoint and total-image refinement

If `K=k` and `A cap f(A)=B`, then the image is `B union R`, where
`R subseteq [n] setminus A` and `|R|=k-b`.  Choose `R`, then choose an onto
map from the `a` labelled source points to the chosen `k` image points.  Thus

\[
 H_n(a,b;k)
 =\binom{n-a}{k-b}\,k!\,\left\{\begin{matrix}a\\ k\end{matrix}\right\}.
\]

The binomial convention makes this formula valid at every integer `k`; in
particular, it vanishes unless `b <= k <= a` and `k-b <= n-a`.  For the empty
source it requires the standard conventions
`S(0,0)=1` and `S(a,0)=0` for `a>0`.

Summing over `k` gives the fixed-target count `N_ab`.  A second derivation,
which does not use Stirling numbers, is useful as a hostile control.  Maps
must avoid the `a-b` forbidden labels of `A setminus B` and hit every one of
the `b` required labels in `B`.  Inclusion--exclusion gives

\[
 N_{ab}
 =\sum_{j=0}^{b}(-1)^j\binom bj(n-a+b-j)^a.                 \tag{B.1}
\]

Consequently, for one fixed labelled target,

\[
 P(A,B)=\frac{N_{ab}}{n^a},
 \qquad
 Q_{ab}=\binom ab\frac{N_{ab}}{n^a}.                       \tag{B.2}
\]

This independently confirms Theorem 1(i) and the displayed quotient.  If
full endomaps rather than restrictions are counted, the common multiplicity
is `n^(n-a)`, as the manuscript says.

### 2.2 All-time labelled quotient

Every trajectory is nested, so a final target outside `A` is unreachable.
For `B_1,B_2 subseteq A` of the same size, there is a permutation of `[n]`
that stabilizes `A` setwise and sends `B_1` to `B_2`.  Conjugating every fresh
map in a complete history by that permutation is a probability-preserving
bijection of histories.  Therefore the endpoints in a fixed final size
layer have equal probability.  Since their aggregate mass is `(Q^t)_{ab}`,

\[
 P^t(A,B)=\mathbf 1_{\{B\subseteq A\}}
           \frac{(Q^t)_{ab}}{\binom ab}.                   \tag{B.3}
\]

The same argument covers `t=0`.  This proves the labelled formula without
assuming that the chain is uniform over intermediate paths.

### 2.3 Complete algebraic spectrum

Order all subsets by nondecreasing size.  The full row-stochastic transition
matrix is lower triangular because every transition goes to a subset.  A
self-loop at an `a`-set occurs precisely when `f|_A` is a permutation of
`A`, so its diagonal entry is

\[
       \lambda_a=\frac{a!}{n^a}.
\]

There are `binom(n,a)` such states.  Hence the characteristic polynomial is

\[
 \chi_P(x)=\prod_{a=0}^{n}
            \left(x-\frac{a!}{n^a}\right)^{\binom na}.      \tag{B.4}
\]

This is the complete **algebraic** eigenvalue multiset.  The manuscript
properly refrains from claiming the full Jordan form of `P`.

### 2.4 Forced top `J_2`

For `0 <= a < n`,

\[
 \frac{\lambda_{a+1}}{\lambda_a}=\frac{a+1}{n}.
\]

Thus all quotient diagonal values are distinct except

\[
 \lambda_{n-1}=\lambda_n
 =\frac{(n-1)!}{n^{n-1}}
 \quad (n\ge 2).
\]

Moreover, when the source is the full set, the only possible image size for
a target of size `n-1` is `n-1`, so

\[
 Q_{n,n-1}
 =\binom n{n-1}\frac{(n-1)!
   \left\{\begin{matrix}n\\ n-1\end{matrix}\right\}}{n^n}>0. \tag{B.5}
\]

Let `lambda=lambda_n` and solve `(Q-lambda I)x=0` in increasing row order.
Rows `0,...,n-2`, whose diagonal values differ from `lambda`, successively
force `x_0=...=x_{n-2}=0`.  Row `n-1` initially leaves `x_{n-1}` free, but
row `n`, together with (B.5), forces `x_{n-1}=0`; only `x_n` remains free.
The algebraic multiplicity is two and the eigenspace dimension is one.
Therefore the quotient has exactly one `J_2(lambda)`.

If `L` lifts a function on cardinalities to a function on labelled subsets,
then direct summation gives `P L = L Q`.  Cardinality functions are therefore
a `P`-invariant subspace carrying `Q`.  A diagonalizable operator has a
diagonalizable restriction to every invariant subspace, so this `J_2`
proves that `P` is not diagonalizable.  It does not determine the other
Jordan blocks of `P`, and the manuscript does not claim otherwise.

### 2.5 Absorption and boundaries

For `n>=2`, every nonempty proper `A` has positive one-step probability of
reaching the empty set: map all its points into `[n] setminus A`.  From the
full set there is positive probability of strict loss, for instance under a
constant map, and the resulting singleton has positive probability of
reaching zero.  Hence every state reaches the absorbing empty set, so the
empty set is the unique recurrent state and absorption is almost sure.

For `tau=min{t:A_t=emptyset}` this gives

\[
 \Pr_a(\tau\le t)=(Q^t)_{a0},
 \qquad
 m_0=0,\quad
 m_a=\frac{1+\sum_{b<a}Q_{ab}m_b}{1-Q_{aa}}.              \tag{B.6}
\]

The denominators are nonzero because `a!/n^a<1` for every `a>0` when
`n>=2`.  The independent calculation also confirms

\[
 Q_{n=2}=\begin{pmatrix}1&0&0\\1/2&1/2&0\\0&1/2&1/2\end{pmatrix},
 \qquad m_2=4.
\]

Boundary audit:

- `n=1`: both subsets are fixed, so the absorption assertion is correctly
  excluded;
- `A=emptyset`: the sole restriction and mark have `a=b=k=0` and mass one;
- `n=2`: this is the first nonsemisimple case and the stated sentinel is
  correct;
- `n=0`: it is outside the manuscript's contract.  If admitted later, it
  must be isolated rather than hidden behind a `0^0` convention.

### 2.6 Multiepoch marks

Put `W_r=|f_r(A_{r-1})|` and define the fixed-target subprobability
polynomial

\[
 M_t^{A,B}(z_1,\ldots,z_t)
 =\mathbb E_A\!\left[
   \mathbf 1_{\{A_t=B\}}\prod_{r=1}^t z_r^{W_r}\right].    \tag{B.7}
\]

The one-step marked size kernel is

\[
 Q_{ab}(z)=\binom ab n^{-a}\sum_k H_n(a,b;k)z^k.           \tag{B.8}
\]

Conditioning on each intermediate size and multiplying monomials yields

\[
 \sum_{\substack{B\subseteq A\\ |B|=b}}
 M_t^{A,B}(z_1,\ldots,z_t)
 =\bigl[Q(z_1)\cdots Q(z_t)\bigr]_{ab}.                   \tag{B.9}
\]

The stabilizer argument from Section 2.2 applies coefficient by coefficient
to complete map histories and preserves every `W_r`.  Therefore

\[
 M_t^{A,B}(z_1,\ldots,z_t)
 =\mathbf 1_{\{B\subseteq A\}}
   \frac{[Q(z_1)\cdots Q(z_t)]_{ab}}{\binom ab}.           \tag{B.10}
\]

This validates the manuscript's intended marked claim.  Equations
(B.7)--(B.10), however, should replace its present informal phrase “the
joint generating polynomial”; see Major-B2.

## 3. Executable hostile control

The independent verifier is at
`docs/papers172_176_sequence/reviews/p172_review_b/verify_review_b.py`.  It
imports no paper/scout/review implementation.  Its formulation differs from
the author verifier in the following material ways:

1. it enumerates complete function tuples `[n] -> [n]`, not only visible
   restrictions;
2. it constructs Stirling numbers from explicit restricted-growth words,
   not a recurrence or onto inclusion--exclusion;
3. it independently computes (B.1) by a required-box sieve;
4. it computes exact full-matrix characteristic polynomials with SymPy;
5. it checks `P L = L Q` and labelled powers directly;
6. it encodes entire mark histories by Kronecker substitution and compares
   every coefficient; and
7. it uses exact-domain rank and fundamental-matrix calculations for the
   Jordan and absorption controls.

Settled coverage:

| control | range |
|---|---|
| complete endomaps, every source/target/mark | `1 <= n <= 5` |
| labelled powers | epochs `0,...,5`, `1 <= n <= 5` |
| full characteristic polynomial | `1 <= n <= 5` |
| coefficientwise mark histories | epochs `1,...,3`, `1 <= n <= 4` |
| quotient `J_2`, spectrum, absorption mean | `2 <= n <= 18` |
| explicit boundaries | `n=1,2` |

Canonical result:

```text
DIGEST e89739f361c2a3b59796e194cf09359b024b5eeb4b2881364c955c1897947ab5
ASSERTIONS 20317
VERDICT EXECUTABLE_CLAIMS_PASS_OWNER_REPAIR_REQUIRED
```

The canonical transcript and provenance manifest are in the same directory.
These checks are falsification evidence, not proofs or owner clearance.

## 4. External owner audit reopened from primary sources

The existing paper cites broad random-mapping and repeated-image controls,
but omits sources closer to its actual one-step kernel.

### 4.1 Direct specified-bin occupancy owner

Charalambides, Section 4.2 of *On Weighted Stirling and Other Related Numbers
and Some Combinatorial Applications*, treats distinct balls allocated among
specified and additional cells and records the distribution of the number
of occupied specified cells.  See *The Fibonacci Quarterly* 22(4), 296--309
(1984), especially pp. 306--307, DOI
[`10.1080/00150517.1984.12429864`](https://doi.org/10.1080/00150517.1984.12429864)
and the [primary PDF](https://www.fq.math.ca/Scanned/22-4/charalambides.pdf).

P172's size row is the exact specialization

```text
distinct balls       = a,
specified cells      = a (the labels in A),
additional cells     = n-a (the labels outside A),
occupied specified   = b = |A cap f(A)|.
```

Thus the unmarked endpoint-size law `Q_ab` is not merely “classical in
spirit”; it is a direct modified-occupancy distribution.  Equation (B.1) is
the fixed-target version of the same specified-box problem.

### 4.2 Modern extended-occupancy formulation

O'Neill, *Three Distributions in the Extended Occupancy Problem*,
*Methodology and Computing in Applied Probability* 25, article 84 (2023),
DOI
[`10.1007/s11009-023-10053-y`](https://doi.org/10.1007/s11009-023-10053-y),
develops the extended occupancy distribution, its noncentral-Stirling form,
and a transition-matrix/spectral treatment.  At a P172 state of size `a`,
take O'Neill's number of bins and balls both equal to `a`, and take the
effective-ball probability to be `theta=a/n`; a choice outside `A` is a
fall-through event.  His mass function becomes

\[
 \operatorname{Occ}(b\mid a,a,a/n)
 =n^{-a}(a)_b S(a,b,n-a)
 =Q_{ab},                                                   \tag{B.11}
\]

where the last `S` is the noncentral Stirling number used in that source.
This source does **not** own P172's state-dependent iteration, labelled
fixed-target recovery, or forced terminal Jordan collision.  It does own a
direct standard formulation of every one-step size row and must be cited and
subtracted.

### 4.3 Generic marked-kernel product

Multiplying transition kernels decorated by generating variables is standard
finite-state Feynman--Kac/Markov-additive machinery.  A representative
primary background source is Fitzsimmons and Pitman, *Kac's moment formula
and the Feynman--Kac formula for additive functionals of a Markov process*,
*Stochastic Processes and their Applications* 79 (1999), 117--134, DOI
[`10.1016/S0304-4149(98)00081-7`](https://doi.org/10.1016/S0304-4149(98)00081-7),
which includes discrete-time analogues and product-moment machinery.
Palmowski, Ramsden, and Papaioannou, *Exit Times for a Discrete Markov
Additive Process*, *Journal of Theoretical Probability* 37 (2024),
1052--1078, DOI
[`10.1007/s10959-024-01322-8`](https://doi.org/10.1007/s10959-024-01322-8),
is a modern discrete Markov-additive control.

Neither is a direct owner of P172's polynomial (B.8).  The generic product
step in (B.9), however, earns no residual credit.  The only potentially
literal-specific marked contribution is the explicit endpoint/total-image
kernel (B.8) together with the coefficientwise labelled lift (B.10).

### 4.4 Bounded literal search

Exact and paraphrased searches for `A cap f(A)`, intersection with a random
map's self-image, and the corresponding Markov chain did not locate a source
stating the full P172 conjunction.  This remains

```text
BOUNDED_LITERAL_OWNER_NON_HIT / NOT NOVELTY EVIDENCE.
```

It is not priority, novelty, publication, or freedom-to-operate evidence.

## 5. Internal collision audit

The current phrase “earlier random-intersection notes” is not an auditable
subtraction.  The following comparison is required.

| internal paper | shared shell assigned zero credit | nontransferable P172 residue |
|---|---|---|
| P158 | nested random intersection, labelled endpoints, absorption | P158 uses graph-cut masks and cut-history fibres, not specified-bin image occupancy |
| P162 | `A cap random-transform(A)` language, stabilizer recovery | its transforms are group translations and its inverse engine is coset/stabilizer geometry, not noninvertible endomap occupancy |
| P170 | subset erosion, marked histories, size quotient | it intersects with permutation fixed sets and uses symmetric-group cycle marks, not total image size |
| P173 | fresh ambient maps, nested erosion, small quotient, every-target lift, triangular spectrum, Jordan obstruction, absorption | P173 uses a quotient-kernel/injective-map fibre and a complementary-dimension Jordan ladder; P172 uses specified-box/Stirling fibres, a total-image mark, and one terminal `J_2` |

P172 is not killed by these comparisons: no P1--P171 item supplies its
specified-bin endpoint/total-image refinement plus terminal resonance, and
P173's inverse engine is not a coefficient substitution into (B.1).  But
the generic proof skeleton is heavily shared and must not be advertised as
separation value.

## 6. Findings

### Critical findings

**Critical-B0 — none.**  No false theorem, missing essential hypothesis, or
boundary counterexample was found.

### Major findings

#### Major-B1 — direct occupancy owner is missing

**Evidence.**  The whole one-step size row is the modified specified-cell
occupancy law of Charalambides and also the extended occupancy specialization
(B.11).  Neither direct control appears in `main.tex`, `references.bib`, or
`SOURCE_VERIFICATION.md`.

**Impact.**  Calling occupancy merely “classical” does not show what portion
of the displayed theorem is already a named distribution with an existing
noncentral-Stirling and spectral formulation.  The current residual boundary
is therefore overstated and not reproducible.

**Mandatory repair.**  Add and verify both Charalambides (1984) and O'Neill
(2023); display the parameter identification above; explicitly assign
`Q_ab`, the fixed-target required-box count, and ordinary Stirling/occupancy
algebra zero contribution credit.  Rewrite the residual as the
state-dependent self-image erosion plus the labelled endpoint/total-image
refinement and forced top coupling, not the occupancy row itself.

**Acceptance test.**  A reader must be able to recover (B.11) from the cited
definition and see, in one paragraph, which P172 assertions are not supplied
by that source.

#### Major-B2 — the marked theorem is correct but underspecified and under-subtracted

**Evidence.**  The manuscript never defines the fixed-target polynomial as
an expectation/subprobability.  Its proof says final relabelling works “as
in” the unmarked case, but does not state that the stabilizer bijection
preserves the full mark vector coefficientwise.  It also does not subtract
the generic marked-kernel/Feynman--Kac product mechanism.

**Impact.**  The intended assertion is mathematically recoverable, but the
present wording leaves ambiguity between an aggregate final-size generating
function, a conditional generating function, and the fixed-target
subprobability polynomial.  It also risks claiming a standard matrix-product
device as a result.

**Mandatory repair.**  Insert definitions (B.7)--(B.10), including the
indicator of the fixed endpoint, the aggregate identity, and the
coefficientwise stabilizer proof.  Cite a standard marked-kernel,
Feynman--Kac, or Markov-additive source and assign matrix multiplication zero
credit.  Retain only the explicit one-step refinement and labelled lift as
literal-specific content.

**Acceptance test.**  For every monomial `prod z_r^(k_r)`, the revised proof
must identify both sides as the same set of complete histories, up to the
stabilizer's free relabelling of the final target.

#### Major-B3 — internal subtraction is too vague, especially against P173

**Evidence.**  `main.tex` says only that earlier notes use translations,
cuts, or permutation fixed sets.  It does not name P158/P162/P170, and it
does not discuss P173, despite P173 sharing the fresh-map erosion, quotient,
labelled-recovery, triangular-spectrum, Jordan, and absorption shell.

**Impact.**  The reader cannot audit whether this is a second paper built
from a transferable proof engine or a genuinely different inverse axis.
The phase firewall contains the necessary distinction, but the manuscript
does not.

**Mandatory repair.**  Name and subtract P158, P162, P170, and P173.  State
that nesting, symmetry-to-labelled recovery, triangular eigenvalue reading,
Jordan-recursion tactics, and absorption recursions earn zero separation
credit.  State positively that P172's surviving axis is specified-bin
occupancy refined by total image size with one terminal resonance, whereas
P173 uses quotient-kernel injectivity and a complementary Jordan ladder.

**Acceptance test.**  The paper-local source/evidence ledger and revised
claim-boundary paragraph must contain an explicit row for every paper named
above.

### Minor findings

#### Minor-B1 — “Boolean multiplicities” is ambiguous

Replace it in the abstract with “binomial layer multiplicities
`binom(n,a)`.”  “Boolean” could be read as a field or semiring claim.

#### Minor-B2 — state the empty-source conventions

Near the definition of `H_n`, state `S(0,0)=1`, `S(a,0)=0` for `a>0`, and
the out-of-range binomial convention.  This makes the `a=0` marked formula,
not just its denominator, self-contained.

#### Minor-B3 — make the absorption path explicit

Replace “a finite monotone chain then reaches zero” by the two explicit paths
used in Section 2.5 and record `lambda_a<1` for all nonempty layers.  The
present proof is valid but too compressed for a boundary-sensitive short
note.

#### Minor-B4 — avoid overloading `E_a`

Use `m_a=E_a[tau]` (or equivalent).  The current line uses `E_a` both as a
scalar name and as expectation notation.

#### Minor-B5 — update the evidence ledger to the strongest actual control

The author verifier cited in the manuscript checks one-step marked counts.
The revised evidence ledger should also point to Review B's coefficientwise
three-epoch control and state its finite range.  This does not turn the
calculation into a proof.

## 7. No-change rationale

The following items should **not** be weakened merely because owner repairs
are required:

| item | Reviewer-B status | rationale |
|---|---|---|
| `H_n(a,b;k)` | `PROVABLE_AS_STATED` | image-set choice followed by an onto-map count |
| every fixed target, every time | `PROVABLE_AS_STATED` | stabilizer of the initial set is transitive on final targets and preserves full histories |
| complete algebraic spectrum | `PROVABLE_AS_STATED` | full labelled operator is triangular with the stated diagonal census |
| one quotient `J_2` at the top collision | `PROVABLE_AS_STATED` | algebraic multiplicity two, positive resonant subdiagonal, eigenspace dimension one |
| non-diagonalizability of full `P` | `PROVABLE_AS_STATED` | the cardinality-function subspace is invariant and carries nonsemisimple `Q` |
| absorption and `n=1,2` boundaries | `PROVABLE_AS_STATED` | explicit access to zero plus exact boundary matrices |
| multiepoch polynomial identity | `PROVABLE_AFTER_FORMALIZATION` | marked Chapman--Kolmogorov multiplication plus coefficientwise stabilizer symmetry |
| full Jordan form of `P` | `NO_CLAIM / NO_REPAIR` | the manuscript expressly does not assert one |
| external novelty | `NO_CLAIM / HOLD_EXTERNAL` | bounded source non-hit supplies no positive evidence |

## 8. Mandatory repair checklist

- [ ] **Major-B1:** add Charalambides and O'Neill, give the exact parameter
  specialization, and narrow the residual claim.
- [ ] **Major-B2:** define the fixed-target multiepoch polynomial, prove the
  coefficientwise lift, and subtract generic marked-kernel machinery.
- [ ] **Major-B3:** explicitly subtract P158, P162, P170, and P173, including
  the shared proof shell.
- [ ] Address Minor-B1--B5 in the manuscript/evidence package.
- [ ] Recompile and rerun both author and Reviewer-B verifiers only after the
  manuscript repair turn.
- [ ] Preserve `HOLD_EXTERNAL`; do not describe a bounded non-hit as novelty.

Subject to those repairs, I recommend retaining the theorem package rather
than killing it.  The correct disposition is owner/evidence major revision,
not mathematical rejection.

## 9. Round-2 delta acceptance

**Acceptance date:** 2026-09-03 UTC  
**Reviewed state:** Round-2 candidate after the final boundary and package
synchronization patches  
**Delta method:** read-only inspection of the manuscript, bibliography,
source/evidence ledgers, QA/build records, compiled PDF, and fresh executions
of both exact controls.  No manuscript or PDF was edited by Reviewer B.  
**Open Review-B findings after this audit:** `0`

### 9.1 Frozen delta inspected

| artifact | accepted state |
|---|---|
| `main.tex` | SHA-256 `c1d72b29b57f967f84ed49daccb4ff7053d1d4d96a7d89172a91ee0bfee75f58` |
| `references.bib` | SHA-256 `e28bd029aa7a9b1b99626da0e7e718f297b7a129adb41bdc948d0fae53933be3` |
| `main.pdf` | 4 pages, 274,791 bytes, SHA-256 `91e8cc76f007eafba48a343aae116eeda03daa8bf3e1bcdbe50d2fc2e2013c83` |
| `main_round2.pdf` | byte-identical to `main.pdf` |
| final LaTeX pass | no undefined citation/reference, bad-box, or package warning |
| author control | 48,575 assertions, `RESULT PASS` |
| Reviewer-B control | 20,317 assertions; canonical SHA-256 `0f3d49edd5225222c9811299bd131d6f09840f476103b6784013d89d0abc7c9d` |

The Reviewer-B verifier was freshly rerun.  Its stdout remained byte-identical
to `CANONICAL.txt`, and every entry in its manifest verified.

### 9.2 O'Neill parameter check

O'Neill's notation gives, for a positive number `r` of balls, `m` bins, and
`0 < theta <= 1`,

\[
 \operatorname{Occ}(k\mid r,m,\theta)
 =\frac{\theta^r}{m^r}(m)_k
   S_{\rm nc}\!\left(r,k;m\frac{1-\theta}{\theta}\right).
\]

For a nonempty P172 source, substitute

\[
       r=a,\qquad m=a,\qquad \theta=\frac an.
\]

Then

\[
 \frac{(a/n)^a}{a^a}=n^{-a},
 \qquad
 a\frac{1-a/n}{a/n}=n-a,
\]

and hence

\[
 \operatorname{Occ}(b\mid a,a,a/n)
 =n^{-a}(a)_bS_{\rm nc}(a,b;n-a)=Q_{ab}.
\]

As a separate algebraic check, Reviewer B evaluated this identity against
the required-box inclusion--exclusion formula for all
`1 <= a <= n <= 30` and every `0 <= b <= a` (5,425 exact rational cases),
with no mismatch.  The revised text now states `a>=1` before invoking the
source and treats `Q_00=1` separately.  It therefore no longer extends
O'Neill's positive-bin, positive-`theta` distribution notation to the
degenerate `a=0` row.

### 9.3 Fixed-target coefficientwise check

Let `B,C subseteq A` with `|B|=|C|=b`.  Choose a permutation `sigma` of
`[n]` such that `sigma(A)=A` and `sigma(B)=C`.  For a complete history
`(f_1,...,f_t)`, set

\[
        g_r=\sigma\circ f_r\circ\sigma^{-1}
        \quad (1\le r\le t).
\]

If `A'_0=A` and the primed trajectory uses the maps `g_r`, induction on `r`
gives

\[
       A'_r=\sigma(A_r),
 \qquad
       |g_r(A'_{r-1})|=|f_r(A_{r-1})|.
\]

Conjugation is a bijection on the complete uniform endomap histories, takes
the endpoint event `A_t=B` to `A'_t=C`, and preserves the full exponent vector
`(W_1,...,W_t)`.  Thus, for every monomial
`z_1^{k_1}...z_t^{k_t}`, the coefficients of the two fixed-target
subprobability polynomials agree.  The aggregate marked
Chapman--Kolmogorov identity sums those equal polynomials over the
`binom(a,b)` possible internal targets; nesting gives zero for targets outside
`A`.  This proves the displayed fixed-target division coefficientwise.

The repaired theorem now defines the subprobability polynomial, states the
aggregate and fixed equations separately, and includes exactly this
coefficientwise bijection.  The generic marked-kernel multiplication is
explicitly cited and assigned zero contribution credit.  The claim is now
`PROVABLE_AS_STATED`, rather than merely recoverable from informal wording.

### 9.4 Finding-by-finding closure ledger

| finding | status | delta acceptance evidence |
|---|---|---|
| Critical-B0 | **CLOSED / NO CRITICAL FINDING** | the repairs introduced no counterexample or unsupported theorem; both exact controls pass |
| Major-B1 | **CLOSED** | Charalambides and O'Neill are cited and verified; the required-box and exact extended-occupancy specialization are displayed and assigned zero credit; the retained residue is narrowed; the `a=0` source-domain boundary is separated |
| Major-B2 | **CLOSED** | `M_t^{A,B}` is an explicit fixed-target subprobability polynomial; aggregate and fixed equations are distinct; the proof is coefficientwise; generic Feynman--Kac/marked-kernel multiplication is cited and subtracted |
| Major-B3 | **CLOSED** | the manuscript and source ledger separately name P158, P162, P170, and P173, subtract the shared proof shell, and identify the nontransferable fibre/Jordan differences |
| Minor-B1 | **CLOSED** | “Boolean multiplicities” is replaced by “binomial layer multiplicities” in both the abstract and exact-claims ledger |
| Minor-B2 | **CLOSED** | the out-of-range binomial rule and `S(0,0)`, `S(a,0)` conventions are explicit; the empty quotient row is also separated from O'Neill's domain |
| Minor-B3 | **CLOSED** | the proof gives a direct zero path from every proper nonempty set, a two-step path from the full set, and `a!/n^a<1` on every nonempty layer |
| Minor-B4 | **CLOSED** | mean scalars use `m_a`, including the corrected sentinel `m_2=4`; `E_a` is reserved for expectation notation |
| Minor-B5 | **CLOSED** | `CLAIMS_EVIDENCE.md` records the fixed-target claim and Reviewer B's coefficientwise complete-history control through `t=3`, `n<=4`; source, QA, improvement, and build records are synchronized to Round 2 |

### 9.5 Final Reviewer-B disposition

```text
REVIEW_B_CLOSED
ROUND2_DELTA_ACCEPTED
MATHEMATICS_SURVIVES
NO_REMAINING_REVIEW_B_REPAIR
HOLD_EXTERNAL
```

P172 may proceed to the batch-level cold-freeze gate.  This acceptance closes
the findings in this review; it is not an external novelty, priority,
publication, or freedom-to-operate clearance.  A later direct owner of the
retained literal conjunction remains a kill switch.
