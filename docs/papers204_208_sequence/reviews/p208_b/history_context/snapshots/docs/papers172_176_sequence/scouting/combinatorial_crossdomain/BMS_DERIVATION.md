# Bracket-matching support: exact static axis and a nonsharp clock

**Handle:** `W01_BMS`  
**Status:** `KILL_CURRENT / OWNER_AMBER_CONTROL / HOLD_EXTERNAL`.

This is the strongest word-system residual in the lane.  It has a complete
image and every-target fibre theorem plus a genuine convergence argument.
It is still not a paper candidate because the static engine is classical
Dyck reduction already occupied internally and the surviving temporal bound
is not sharp.

## 1. Literal map

For `w in {0,1}^n`, read `1` as an opening parenthesis and `0` as a closing
parenthesis.  Match parentheses by the ordinary LIFO stack rule.  Define

```text
M(w)_i = 1  iff position i belongs to a matched pair.
```

Equivalently, repeatedly cancel adjacent `10` in the current residual word;
`M(w)` marks exactly the letters removed in this reduction.  This is a
length-preserving autonomous map; it does not output the reduced word.

## 2. Image and every-target fibre

For a binary target `y`, let its maximal 1-run lengths be
`r_1,...,r_k`, and let `z` be its number of zeros.

### Theorem 2.1

The following are equivalent:

1. `y` lies in the image of `M`;
2. every `r_i` is even.

If one run is odd, `|M^(-1)(y)|=0`.  Otherwise, writing `r_i=2m_i`,

```text
|M^(-1)(y)| = (z+1) product_i Cat_(m_i),               (2.1)
```

where `Cat_m=binom(2m,m)/(m+1)`.  In particular,

```text
|image(M on {0,1}^n)| = F_(n+1)                        (2.2)
```

for `F_1=F_2=1`.

### Proof

After all `10` cancellations, the residual word has the unique form
`0^a 1^b`: if a residual 1 occurred before a residual 0, that pair would
still be cancellable.  Between consecutive residual letters, before the
first one, and after the last one, the removed letters form completely
matched Dyck words.  Consequently every maximal consecutive block of matched
positions has even length.

Conversely, suppose the 1-runs of `y` have lengths `2m_i`.  On each such run
choose any Dyck word of semilength `m_i`.  At the `z` zero positions of `y`,
choose a boundary `a in {0,...,z}`; fill the first `a` zero positions by
unmatched closes and the remaining positions by unmatched opens.  All chosen
Dyck blocks match internally, and no residual position matches, so the support
is exactly `y`.

The residual symbols of any source must be all closes followed by all opens,
so its boundary is unique.  Each marked run independently carries one of
`Cat_(m_i)` Dyck words.  This proves (2.1), including the empty target and
empty products.  Finally, binary strings whose 1-runs are all even are
counted by the elementary three-state outside/odd/even-run automaton, yielding
the Fibonacci recurrence and (2.2).  `square`

## 3. A strict convergence potential

For nonzero `y` in the image, let `L(y)` be the first 1-position and `R(y)`
the last position of its first 1-run, using zero-based coordinates.

### Theorem 3.1

Every orbit reaches `0^n`.  More precisely, if `y` is a nonzero image state
and `M(y)` is nonzero, then

```text
(L(M(y)),R(M(y))) >_lex (L(y),R(y)).                    (3.1)
```

Thus `0^n` is the unique recurrent state and every orbit has length at most

```text
1 + n(n+1)/2.                                          (3.2)
```

### Proof

Every position before `L(y)` is a closing parenthesis with no opener to its
left, hence stays unmatched.  Therefore the first matched position cannot
move left: `L(M(y))>=L(y)`.

Suppose equality holds.  Then the opener at `L(y)` is matched to a closing
position `j`.  Since the first 1-run of `y` ends at `R(y)`, necessarily
`j>R(y)`.  The opener at `L(y)` remains at the bottom of the stack until it
is popped at `j`.  Every position strictly between it and `j` must therefore
also be matched: a close sees a nonempty stack, while every later opener must
be popped before the bottom opener.  Hence every position from `L(y)` through
`j` is marked in `M(y)`, and `R(M(y))>=j>R(y)`.  This proves (3.1).

There are `n(n+1)/2` possible pairs `0<=L<=R<n`.  After an arbitrary first
step the state is in the image, and (3.1) strictly advances at every later
nonzero step.  This proves convergence and the crude bound (3.2).  `square`

## 4. Exact checks and the unresolved sharp clock

`verify_bms.py` implements matching independently by exhaustive adjacent
`10` cancellation, not by the breadth script's stack.  Through length 16 it
checks every source, every target, (2.1), the three-state image DP, (3.1), and
complete convergence.  It records **848,808 assertions**.  The exact maximum
tails for lengths 1 through 16 are

```text
1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 9, 9.
```

These values are not promoted to a conjectural formula.  The lexicographic
potential proves only a quadratic ceiling and does not yet classify deepest
sources or all depth layers.  Therefore this candidate fails the required
sharp-clock axis even before ownership subtraction.

## 5. Owner and internal subtraction

- Ordinary stack matching, the residual normal form `0^a1^b`, Dyck blocks,
  and Catalan enumeration are classical.  P74 already uses precisely the
  exposed-stack/polycyclic normal-form engine for Dyck and Motzkin systems.
  Those parts of Theorem 2.1 receive zero paper-value credit.
- P93 occupies push--pop stack cocycles.  The present map is deterministic
  and not that cocycle, but generic stack-language claims are unavailable.
- Pairing each 1 with a later 0 is also the particle--vacancy matching behind
  box--ball carrier descriptions; P90 occupies sharp one-dimensional traffic
  clocks.  `M` marks both endpoints rather than moving a conserved particle,
  so no literal conjugacy is asserted, but the interface is owner-sensitive.
- P144 occupies Dyck reassociation and its Catalan target fibres.  Again the
  literal map differs, while the static combinatorial engine does not create
  separation.

A bounded exact-phrase search did not locate iteration of this precise
matched-position support mask.  That non-hit is not novelty evidence.  After
the owned static material is removed, only the nonsharp first-run potential
remains.  The correct gate is therefore **current kill**, reopenable only if a
sharp all-length clock/depth atlas and a genuinely independent residual axis
are proved and then pass a primary-owner search.
