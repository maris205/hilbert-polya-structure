# P156 independent hostile review A

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal reader; did not author P156.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`.  The manuscript was not sent to an
external model, reviewer, or review service.  Primary records were consulted
only for the owner audit.

## Verdict

**REVISE — 0 Critical / 0 Major / 2 Minor.**

The reframed theorem package survives independent hostile checking.  The
maximum-drop image obstruction is necessary and sufficient, the high-shift/
low-tail section is sharp, the deficient-completion product resolves every
target fibre, identities are the only recurrent states, and the canonical
minimum-one-step inverse ray has the stated Fibonacci resource update and
exact tail shift.  The manuscript also keeps the false pointwise clock, the
open global clock, and global multi-step minimality outside the theorem.

No direct owner of the full owner-subtracted map conjunction was found; the
Bell identity aggregate is correctly assigned to its source.  The frozen
verifier and PDF reproduce exactly, and no anonymity defect was found.

Two local repairs remain.  The fibre theorem says “at every source rank” even
though its board notation is defined only for `n>=m`; the `n<m` and empty-
product `n=m` boundaries should be literal rather than implicit.  In
addition, the PDF ends after Funding and omits the explicit
`HOLD_EXTERNAL`/External Status declaration used by the sequence house style
and recorded everywhere else in the package.

This is a raw review.  I did not edit `main.tex`, the verifier, bibliography,
transcript, PDF, or any author ledger.

## 1. Package and theorem-ceiling comparison

I read `WEX_REFRAMED_FREEZE_CONTRACT.md`, `main.tex`, `references.bib`, all
paper-local planning/evidence/source/control/build records, the proof package
and author self-QA, `verify_p156.py`, its frozen transcript, the manifest, and
both Round-0 PDFs.

| Frozen interface | Manuscript interface | Hostile result |
|---|---|---|
| literal map retaining `pi_i>=i` and standardizing | equation (1) | PASS; position 1 prevents an empty output |
| exact image threshold `sigma in W(S_n)` iff `n>=m+d(sigma)` | Theorem 1(1), Section 2 | PASS in both directions and at equality `h=d` |
| explicit section at every admissible rank and exact minimum source rank | equations (7), (13) and proof | PASS |
| every-target deficient-Ferrers fibre formula | Theorem 1(2), equations (4)--(5), Section 2 | mathematically PASS; quantified-domain clarification required |
| identity-only recurrence and strict rank drop | Theorem 1(3), Section 3 | PASS |
| locally minimum canonical inverse ray | Theorem 1(4), Section 3 | PASS; “locally” remains one-step only |
| update `(m,d)->(m+d,m)`, Fibonacci powers, and tail shift | equations (10)--(12) | PASS for every `t>=1` and nonidentity target |
| false pointwise clock explicitly withdrawn | Section 4 and exact counterexample | PASS; reproduced independently by the verifier |
| no global maximum clock or global `t`-step inverse optimum | abstract, theorem aftermath, Section 4 | PASS; no ceiling overrun |
| static weak-excedance/drop/tableau/Bruhat/Bell inputs zero-credit | Section 1 | PASS; residual is correctly conjunction-only |

The paper-value gate remains narrow but intact.  The one-step image theorem or
generic Ferrers matching alone would be too thin.  The accepted object is the
target-resolved image/fibre pair plus the exact dynamics of one canonical
right inverse; the manuscript keeps all three axes.

## 2. Independent theorem rederivation and proof attacks

### 2.1 Well-definedness and carrier quantifiers

For every nonempty permutation, position one satisfies `pi_1>=1`, so the
retained word is nonempty and its standardization is a permutation.  Output
rank never exceeds input rank.  Thus, for each fixed `N>=1`, the rule is a
self-map of the finite disjoint union `S_1 disjoint_union ... disjoint_union
S_N`.  The source says this correctly in substance, although explicitly
quantifying `N>=1` at the first occurrence would close the carrier boundary.

For a nonidentity permutation, `d=max_i(i-pi_i)` is positive.  If it were
nonpositive, every `pi_i>=i`; equality of the two coordinate sums would force
equality in every coordinate and hence the identity.

### 2.2 Image necessity and every inequality

Suppose a source `pi in S_n` maps to `sigma in S_m`, with selected positions

```text
P={p_1<...<p_m}
```

and selected values

```text
A={a_1<...<a_m}.
```

Standardization forces the value at `p_i` to be `a_(sigma_i)`.  Since `p_i`
is the `i`th selected position, `i<=p_i`; since it is selected,
`p_i<=a_(sigma_i)`.  With `h=n-m`, the `j`th selected value has exactly `j`
selected values at or below it and at most all `h` complement values below
it, so

```text
a_j <= h+j.
```

Consequently

```text
i <= p_i <= a_(sigma_i) <= h+sigma_i,
i-sigma_i <= h.
```

Taking the maximum gives `d(sigma)<=h`, or
`n>=m+d(sigma)`.  No hidden assumption about the order of selected values is
used.

### 2.3 Sufficiency, equality `h=d`, and exact minimum rank

For `h>=d(sigma)`, define

```text
R_n(sigma)=(sigma_1+h,...,sigma_m+h,1,...,h).
```

The first `m` entries satisfy `sigma_i+h>=i` and are selected.  Low value `j`
occurs at position `m+j>j` and is strictly deficient.  The selected word is
therefore exactly the shifted copy of `sigma`, whose standardization is
`sigma`.  This remains valid at equality `h=d`; coordinates attaining the
maximum drop become diagonal weak excedances, which are retained because the
predicate is non-strict.

Necessity and this section prove both the iff and the exact minimum source
rank `m+d(sigma)`.  No division or asymptotic argument occurs.

### 2.4 Every-target fibre and nonpositive factors

Fix `A,P`.  The selected assignment is forced: position `p_i` receives
`a_(sigma_i)`.  It is weak-excedant exactly when
`p_i<=a_(sigma_i)` for every `i`.

Let `B=[n]\A` and `Q={q_1<...<q_h}=[n]\P`.  At increasing complement
position `q_j`, an admissible value must lie strictly below `q_j`.  There are
`#{b in B:b<q_j}` such values.  Each of the `j-1` values used earlier is in
this set because it was assigned below an earlier position
`q_k<q_j`.  Therefore the number of choices is exactly

```text
#{b in B:b<q_j}-(j-1).
```

If a factor is nonpositive, there is no completion; otherwise sequential
multiplication counts every deficient bijection once.  Every source has one
unique selected-set pair and one unique completion, and the reverse
construction creates a unique source.  The sum is therefore disjoint and
exact.

At `n=m`, the complement sets are empty.  With the standard empty-product
value one, the only pair is `A=P=[m]`; its admissibility inequalities
`i<=sigma_i` hold only for the identity.  Hence the same-rank fibre is one
for `id_m` and zero for every nonidentity target.  At `n<m`, rank alone makes
the fibre empty, but the current `h,Q,K` notation is not defined.  This is
the local quantifier defect scored as m1 rather than a failure of the formula
on its intended domain.

As a check independent of `verify_p156.py`, I enumerated all **873** source
permutations through rank six, all **1,072** target/source-rank cells, and an
independently coded completion product.  Every literal fibre and every image
threshold agreed, and the same-rank/empty-product boundary passed for every
target.

### 2.5 Recurrence and rank equality

If `W(pi)` has the same rank as `pi in S_n`, every position was selected, so
`pi_i>=i` for all `i`.  Since both sides have equal sums, every inequality is
an equality and `pi=id_n`.  Conversely, an identity is fixed.  Every other
step strictly lowers positive integer rank, so no nonidentity cycle exists
and the recurrent states of the finite cutoff are precisely its identities.

This proof also establishes absorption without importing the excluded clock
conjecture.

### 2.6 Canonical inverse update and Fibonacci powers

For nonidentity `sigma`, `d=d(sigma)>0`; applying the sharp section with
`h=d` gives a genuine rank-increasing preimage.  In a lift of a state with
resources `(m_t,d_t)`, each shifted high entry has drop

```text
i-(sigma_i^(t)+d_t) <= d_t-d_t = 0,
```

while every low-tail value `j` occurs at position `m_t+j` and has drop
exactly `m_t`.  Hence

```text
(m_(t+1),d_(t+1))=(m_t+d_t,m_t).
```

The image theorem proves that this particular one-step source has minimum
possible rank.  It does not imply a minimum among all multi-step sources,
and the text explicitly refuses that implication.

Powers of `[[1,1],[1,0]]` give, for `t>=1`,

```text
m_t=F_(t+1)m+F_t d,
d_t=F_t m+F_(t-1)d.
```

Every lifted state is nonidentity and makes one step to its immediate target,
so the deterministic first-hitting time satisfies
`tau(sigma^(t))=tau(sigma)+t`.  This is a chosen backward ray, not a bound on
all forward orbits.

### 2.7 Withdrawn clock claims and exact falsifier

For

```text
pi=(11,10,9,4,1,2,3,8,5,6,7),
```

the weak-excedance letters are `11,10,9,4,8`, which standardize to
`(5,4,3,1,2)`.  The source maximum drop is four.  Direct iteration gives
target tail three, whereas exhaustive rank-four enumeration gives maximum
tail two.  Thus the old inequality comparing `tau(W(pi))` with the rank-`d`
maximum is false.  The manuscript labels it false, does not infer the global
maximum-clock formula, and does not claim global iterated-preimage
minimality.

## 3. Owner attack

### Direct ownership and exact collision

The most important collision is fully subtracted.  Beyene--Backelin--
Mantaci--Fufa's [official Journal of Integer Sequences article](https://cs.uwaterloo.ca/journals/JIS/VOL26/Beyene/beyene13.html),
Theorem 27, counts permutations whose weak-excedance-letter subword is
increasing by the Bell number.  In P156 notation this is exactly

```text
sum_(m=1)^n |W_n^(-1)(id_m)| = B_n.
```

That aggregate and the Baril transposition-array proof chain are assigned
zero credit.  P156 does not relabel the Bell theorem as a consequence of its
target-resolved formula and claim ownership.

### Nearby ownership

Ehrenborg--Steingrimsson own excedance-set enumeration; Chung--Claesson--
Dukes--Graham and Chen--Chen own maximum-drop/bounded-drop enumerators;
Steingrimsson--Williams own the permutation-tableau weak-excedance
interfaces.  Bergeron--Gagnon explicitly define the weak-excedance position
and value sets and their equivalence classes in the
[primary manuscript](https://arxiv.org/abs/2302.10814).  Those static
statistics, classes, tableau/Bruhat structure, and distributions receive no
contribution credit.

Generic Ferrers/rook matching, standardization, rank monotonicity, and
Fibonacci matrix powers are standard tools and likewise carry no standalone
credit.

### Residual and bounded non-hit

I repeated exact and alias searches for `weak excedance subword`, `retain
weak excedance letters`, `standardized weak excedance`, `deletion and
standardization`, `iterated weak excedances`, `maximum drop image`, and
target-resolved fibres.  The primary results recovered the static owners and
the exact Bell identity collision, but no checked source states the full
nonidentity target threshold/fibre plus canonical inverse-ray conjunction.

This is a bounded non-hit only.  It does not establish novelty, priority,
ownership completeness, or clearance.  A direct source for the exact map or
for an equivalent diagonal-extraction iteration would reopen P156.

## 4. Portfolio-collision attack

- **P149:** both systems select a permutation subsequence and standardize,
  which is zero-credit carrier overlap.  P149 uses endpoint-inclusive local
  peaks, alternating packing, and zigzag/pinnacle fibres.  P156 uses the
  absolute diagonal predicate, maximum-drop cost, high-shift/low-tail
  section, and deficient complement matching.  No P149 proof yields the
  P156 threshold or inverse update.
- **P155:** both maps change rank and have target sections/fibres.  P155 reads
  cycle-support maxima, has threshold `2m-rlmin`, and factorially weighted
  ordered-support fibres.  P156 has threshold `m+d`, selected position/value
  boards, and the only frozen Fibonacci inverse tower.
- **P152:** P152 is a stochastic fixed-carrier reflected-count chain with a
  marked Chebyshev transform and a mean/parity inverse.  There is no literal
  update or proof-engine collision.
- **P153:** a fixed finite-field plane collapses through rising-factorial
  coefficients.  Forced coordinates and all-time plane fibres are unrelated
  to deficient permutation matchings.
- **P154:** subgroup normalizers, two-adic halving forests, and an unlabelled
  arithmetic graph signature share only generic inverse/iteration language.

The portfolio gate passes.  It depends on the literal diagonal selector,
`m+d` obstruction, Ferrers completion, and canonical backward dynamics; the
paper does not seek separation value from the generic phrase “standardize a
subsequence.”

## 5. Independent exact replay and assertion semantics

I cold-ran, in a fresh process,

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p156.py
```

Fresh stdout matched `verification_output.txt` byte for byte.  Its SHA-256 is

```text
a40c259e9270151b9efbc1e1276e9089783bafa9f04ada107638f9cea914a458
```

and the run ended with

```text
boxes=32
assertions=3326610
status=PASS
```

The verifier enumerates all 409,113 permutations through rank nine, checks
99,451 target/rank image cells, compares 6,985 every-target fibre cells
through source rank seven, recovers the zero-credit Bell aggregate, lifts all
46,225 nonidentity targets through rank eight for six levels, and reproduces
the rank-11 clock counterexample.  The literal predecessor dictionaries and
the subset/completion formula are separately implemented.

My independent scratch audit, not importing the paper verifier, added the
873-state/1,072-cell checks and explicit same-rank boundary described above.

These computations do **not** prove an all-rank theorem, complete the owner
search, establish novelty or priority, prove the excluded global clock,
establish global multi-step inverse optimality, or authorize release.  They
are bounded exact counterexample pressure.

## 6. Source-only build, PDF, and anonymity

A fresh temporary directory containing only `main.tex` and `references.bib`
completed

```text
pdflatex -> bibtex -> pdflatex -> pdflatex
```

and reproduced the current PDF byte for byte:

```text
pages=4, bytes=328932
SHA256=ee5cedd089d9d837839f9fc715aae9530e19fc4f414dfcbef77ad0adfafa256c
```

The current PDF and `main_round0_original.pdf` are byte-identical.  The
settled source-only log has no unresolved citation/reference, rerun request,
build warning, overfull box, underfull box, or duplicate label.  All 26 font
rows are embedded and subsetted.  The PDF is A4 and unencrypted; title,
author, subject, and keyword metadata are blank, with no volatile date, form,
or JavaScript.

I rasterized and inspected all four pages.  The map, owner subtraction,
theorem, image/fibre proofs, inverse tower, counterexample, declarations, and
eight references are legible and within bounds.  No clipping, overlap,
corrupt glyph, unresolved marker, or identifying author information is
visible.  `Anonymous` is the only displayed author identity.

The complete Round-0 stable-file manifest passes at review time.  It must, as
the protocol requires, be regenerated after the review, improvement log, and
historical Round-1/Round-2 artifacts are added.

## 7. Findings and required repairs

### m1 — Minor: the fibre quantifier omits the `n<m` and empty-product
boundaries

**Evidence.**  The board notation is introduced with “For `n>=m`, write
`h=n-m`,” but Theorem 1(2) then says “At every source rank `n`” without
repeating the restriction.  For `n<m`, the fibre is trivially empty, while
`h`, `Q={q_1<...<q_h}`, and the product in equation (5) are not defined.  At
`n=m`, the formula is correct only with the conventional but unstated value
`K(emptyset,emptyset)=1`.  The verifier starts target ranks at `m` and does
not make either boundary a named assertion.

**Required repair.**  State the fibre result for every `n>=1` in a literal
piecewise form: zero for `n<m`, and equation (8) for `n>=m`.  Define the empty
product as one, and mention that the same-rank fibre is one for `id_m` and
zero otherwise.  Add deterministic `n<m` and `n=m` boundary assertions to
the verifier/transcript and synchronize the proof package and evidence
ledger.  Also quantify `N>=1` when the finite carrier is first introduced.

### m2 — Minor: the frozen PDF omits its explicit External Status declaration

**Evidence.**  `README.md`, `BUILD.md`, `FINAL_QA.md`, the source ledger, and
the contract all say `HOLD_EXTERNAL`.  The manuscript itself ends after the
Funding paragraph and bibliography.  Unlike P152 and the other sequence
house artifacts, it has no `External Status` paragraph stating that posting,
submission, circulation, and author contact remain unauthorized.  The PDF is
otherwise anonymous and clean; this is a local artifact-integrity omission,
not an anonymity leak.

**Required repair.**  Add the house External Status declaration immediately
after Funding, using the literal `HOLD_EXTERNAL` token and the same posting/
submission/circulation/contact boundary as the sequence.  Recompile, inspect
the final page, and keep title/author metadata blank.  Do not interpret this
internal status line as a novelty or submission claim.

## 8. Required Round-1 disposition

Record both items in `IMPROVEMENT_LOG.md`, implement the boundary/declaration
repairs without reviving any withdrawn clock claim or broadening ownership,
replay the verifier in a fresh process, rebuild from a source-only copy,
preserve `main_round0_original.pdf`, and freeze `main_round1.pdf`.  P156
remains `HOLD_EXTERNAL`; this review does not claim novelty, priority,
submission readiness, or release clearance.
