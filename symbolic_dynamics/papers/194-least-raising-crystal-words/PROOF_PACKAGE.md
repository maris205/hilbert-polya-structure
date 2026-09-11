# Proof package — P194 least-colour raising crystal words

## Theorem package

For the literal least-colour raising map on `[k]^n`:

1. fixed and recurrent words are exactly the highest, equivalently ballot,
   words, and each crystal component has one such sink;
2. if a word has reverse-RSK shape `lambda`, its exact tail is
   `sum(w)-sum_i i lambda_i`;
3. the sharp global tail is `n(k-1)`, uniquely at `k^n`;
4. one component of shape `lambda` has normalized principal-specialization
   depth polynomial
   `product_(x in lambda) (1-q^(k+ct(x)))/(1-q^(h(x)))`;
5. shape-`lambda` components occur with multiplicity `f^lambda`, giving the
   global layer polynomial after summation;
6. fixed words are counted by `sum f^lambda`, equivalently by involutions
   whose RSK shape has at most `k` rows;
7. every labelled target has exactly the self-source when highest together
   with the lowerings `f_i(y)` at which all colours below `i` remain
   unavailable;
8. every fibre has size at most `k`, and equality occurs for some target if
   and only if `n >= binom(k,2)`.

## Status

`PROVABLE AS STATED / OWNER_AMBER / HOLD_EXTERNAL`

All implications are all-parameter and cover `n,k >= 1`.  Enumeration is not
used as a premise.  Classical crystal and tableau theorems are invoked with
citations and receive zero contribution credit.

## Literal assumptions

- Words are read left to right on the ordered alphabet `[k]`.
- In the `i`-signature, `i` is `+` and `i+1` is `-`.
- Matching deletes `+-` pairs, including pairs separated by ignored letters.
- `e_i` edits the rightmost unmatched minus; `f_i` edits the leftmost
  unmatched plus.
- All availability tests use the state at the start of the epoch.
- Exactly the least available `e_i` is applied; if none is available, the
  state holds.
- The component shape is the row-insertion shape of the reversed word.

## Notation

- `F=F_(n,k)`: the deterministic scheduler.
- `E(w)`: sum of the letters of `w`.
- `lambda=sh(w)`: reverse-word RSK shape, padded with zero parts through `k`.
- `b(lambda)=sum_i i lambda_i`: highest-word energy in the component.
- `tau(w)`: first entrance time into the recurrent set.
- `D_(lambda,k)(q)`: depth polynomial of one shape-`lambda` component.
- `f^lambda`: number of standard Young tableaux of shape `lambda`.

## Dependency map

1. The signature-prefix lemma depends only on the frozen cancellation
   convention.
2. The highest-word characterization combines that lemma with the holding
   clause; uniqueness per component is classical crystal theory.
3. The clock uses component preservation, one-unit energy drop, and the
   highest content.
4. Sharp global depth uses only the clock and equality conditions in two
   elementary bounds.
5. Component layers use the clock plus the classical SSYT weight enumerator;
   the product form uses principal specialization.
6. Shape multiplicity and the fixed/involution census use reverse RSK and the
   standard-tableau index.
7. The inverse atlas uses only partial crystal-string inversion and the
   least-colour scheduler.
8. Fibre sharpness uses the inverse atlas, adjacent strictness of a highest
   weight, and the explicit staircase target.

## Proof

### Step 1. Signature and prefix deficits

Fix `i`.  Scan the `i/i+1` subword from left to right, pushing every `+` and
matching a `-` whenever a pushed `+` is available.  A minus survives exactly
when, at some prefix, the number of `i+1` letters exceeds the number of `i`
letters.  Therefore every `e_i` is absent exactly when every prefix has at
least as many `i` letters as `i+1` letters for every adjacent pair.  These
are precisely the ballot/Yamanouchi words.

The stack description also fixes the edited positions.  Along every
`i`-string, changing the rightmost unmatched minus and changing the leftmost
unmatched plus are inverse operations.  No later proof silently changes the
tensor convention.

### Step 2. Highest sinks and termination

The holding clause says `F(w)=w` exactly when all `e_i` are absent, so fixed
words are the ballot words of Step 1.  Classical finite type-A word-crystal
theory decomposes the carrier into connected highest-weight components, each
with a unique highest word.

Every active update is one crystal edge and stays in its component.  It
changes one `i+1` into `i`, decreasing `E` by one.  Thus there is no
nontrivial directed cycle.  Finiteness forces each orbit to stop, and its only
possible endpoint is the unique highest word in its component.  Recurrent
therefore equals fixed.

### Step 3. Exact pointwise clock

Let the component shape be `lambda`.  Under the chosen reverse-RSK
convention, its highest word has content `lambda`, hence energy
`b(lambda)=sum_i i lambda_i`.  Each nonfixed epoch decreases energy by exactly
one and the endpoint has that baseline.  Consequently

```text
tau(w)=E(w)-b(lambda).
```

This argument shows why the route may depend on the scheduler while its
length does not: every raising path from a word to its component highest
vertex has the same weight-rank difference.

### Step 4. Sharp global tail and unique extremizer

For any length-`n` word, `E(w) <= nk`.  Since `lambda` partitions `n`,
`b(lambda) >= n`.  The clock gives `tau(w) <= n(k-1)`.  Equality in the first
bound requires `w=k^n`.  That word has shape `(n)`, highest endpoint `1^n`,
and baseline `n`, so it realizes equality.  The required equality condition
also proves uniqueness.

For `k=1`, the statement reads maximum tail zero with unique word `1^n`, as
required.

### Step 5. One-component layers

Reverse-word RSK writes a word as a pair `(P,Q)` of common shape `lambda`,
where `P` is semistandard over `[k]` and `Q` is standard.  Crystal operators
act on `P` and preserve `Q`; fixing `Q` fixes one component.  The letter sum
is the sum of entries of `P`, and the highest tableau fills row `r` by `r`.
Thus

```text
D_(lambda,k)(q)
 = q^(-b(lambda)) s_lambda(q,q^2,...,q^k)
 = q^(-n(lambda)) s_lambda(1,q,...,q^(k-1)),
```

where `n(lambda)=sum_r (r-1)lambda_r`.  The classical principal-specialization
formula is

```text
s_lambda(1,q,...,q^(k-1))
 = q^(n(lambda)) product_(x in lambda)
     (1-q^(k+ct(x)))/(1-q^(h(x))).
```

The two powers cancel and yield the claimed depth product.  Although written
as a quotient, it is a polynomial with nonnegative integer coefficients
because it is the SSYT depth enumerator.

### Step 6. Global layers and the fixed/involution census

There are `f^lambda` choices of the standard recording tableau `Q`, hence
`f^lambda` components of shape `lambda`.  Summing their identical component
polynomials gives

```text
D_(n,k)(q)=sum_(lambda |- n, rows(lambda)<=k)
             f^lambda D_(lambda,k)(q).
```

At depth zero, each component contributes one highest word.  The fixed census
is therefore the same sum of `f^lambda`.  Under ordinary RSK, an involution is
a pair `(Q,Q)`, so the sum also counts involutions with at most `k` rows.
Schensted's theorem translates the height bound to longest decreasing
subsequence length.  When `k>=n`, all shapes occur and the usual telephone
recurrence yields exponential generating function `exp(z+z^2/2)`.

### Step 7. Complete every-target inverse atlas

Fix a labelled target `y`.  If `x` is a nonfixed predecessor and the
scheduler uses colour `i` at `x`, then `y=e_i(x)`.  Partial inversion along
the `i`-string forces `x=f_i(y)`.  The scheduler chooses `i` exactly when
`e_j(x)` is absent for each `j<i`; no condition on higher colours is needed.
This proves necessity.

Conversely, suppose `x=f_i(y)` exists and every lower-colour `e_j(x)` is
absent.  Then `e_i(x)=y`, and `i` is the least available colour at `x`, so
`F(x)=y`.  The only self-predecessors are held states, exactly the highest
words.  Thus

```text
F^(-1)(y)
 = ({y} if y is highest, else empty)
   union {f_i(y): f_i(y) exists and e_j(f_i(y)) absent for every j<i}.
```

Different colours change the content by different simple roots, so their
candidates are distinct.  With at most `k-1` colours and at most one
self-source, every fibre has size at most `k`.  Empty fibres are included by
the set identity, and summing all fibre sizes gives `k^n` because `F` is a
self-map of a finite carrier.

### Step 8. Exact stable sharpness

Assume `k>=2`.  If a target fibre has size `k`, it must contain the self
candidate and all `k-1` lowering candidates.  Hence the target is highest.
For a highest word of padded weight `lambda`, `f_i` exists exactly when
`lambda_i>lambda_(i+1)`.  All colours existing forces

```text
lambda_1>lambda_2>...>lambda_k>=0,
```

so `n >= (k-1)+(k-2)+...+1=binom(k,2)`.

Conversely, write `s=n-binom(k,2)` and take

```text
h=1^(k-1+s) 2^(k-2) ... (k-1)^1.
```

This word is highest and its padded content drops strictly at every adjacent
pair, so all `f_i(h)` exist.  Applying `f_i` affects no signature of colour
`j<i-1`.  In the `(i-1)`-signature it removes one minus and cannot create an
unpaired minus.  Thus all lower `e_j` remain absent, every candidate is
admissible, and the self-source supplies the `k`th predecessor.  For `k=1`,
the sole target and fibre both have size one.

## Boundary audit

- `n=1`: each letter `a` follows a chain to `1`; depths are `a-1`, so the
  unique deepest state is `k` and the fixed count is one.
- `k=1`: the carrier has one word, every signature family is empty, and all
  displayed sums/products reduce correctly.
- A nonhighest target has no self-source even if some lowering candidate
  equals neither it nor another candidate.
- Candidate distinctness is content-based and does not assume injectivity of
  the scheduler.
- The principal-specialization product is interpreted by polynomial
  cancellation at formal `q`; at `q=1` its limit is the hook-content value.
- The stable threshold asserts existence of a size-`k` fibre, not that every
  highest target in that range has size `k`.
- Reverse RSK appears only because of the frozen tensor convention; no word
  reversal is performed by the dynamic.

## Contribution and ownership boundary

The clock's weight-rank mechanism, all component structure, all Schur and
hook identities, the involution correspondence, and the abstract existence
of partial crystal inverses are classical or routine consequences and earn
zero contribution credit.  The paper retains only their conjunction with
the least-colour autonomous scheduler and the exact labelled admissibility
atlas.  A bounded source non-hit does not clear ownership.  The correct gate
is `OWNER_AMBER/HOLD_EXTERNAL`.

## Open risks

- A specialist source may already study this precise priority rule on word
  crystals under another tensor convention.
- Conjugating by word reversal or Dynkin-diagram colour reversal could hide a
  direct owner; both update and scheduler order must be compared.
- The one-step fibre atlas is complete, but no closed all-time target fibre
  formula is supplied.
- Round 0 includes no hostile or process-separated review.
