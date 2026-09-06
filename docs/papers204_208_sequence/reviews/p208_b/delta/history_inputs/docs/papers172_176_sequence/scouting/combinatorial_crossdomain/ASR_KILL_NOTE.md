# Adjacent-sum reranking: an explicit recurrent orbit, then atlas failure

**Handle:** `Q01_ASR`  
**Status:** `KILL_NO_ATLAS / HOLD_EXTERNAL`.

## Literal map

For `pi in S_n`, with cyclic indices, form

```text
s_i = pi_i + pi_(i+1).
```

Replace `s` by its stable rank word: smaller sums receive smaller ranks and
equal sums are ordered by the old position index.  Call the resulting
permutation `A_n(pi)`.

## One all-rank recurrent family

Let `p_n` be obtained by writing 1, then the even letters increasingly, then
the still-unused odd letters decreasingly.  Thus

```text
p_8 = 1 2 4 6 8 7 5 3,
p_9 = 1 2 4 6 8 9 7 5 3.
```

Let `q_n` be 1, then the odd letters at least 3 increasingly, then the
still-unused even letters decreasingly:

```text
q_8 = 1 3 5 7 8 6 4 2,
q_9 = 1 3 5 7 9 8 6 4 2.
```

### Lemma

For every `n>=3`,

```text
A_n(p_n)=q_n,       A_n(q_n)=rot(p_n),                 (2.1)
```

where `rot` is left rotation.  Hence `p_n` lies on a cycle of exact period
`2n`.

### Proof

The cyclic adjacent sums of `p_n` are all distinct.  Starting from the first
edge they alternate through the low odd sum 3, increasing even-spaced sums,
the one or two largest turn sums, decreasing even-spaced sums, and the final
cyclic sum 4.  Ranking this list gives exactly `q_n`.  Performing the same
calculation on `q_n` gives `rot(p_n)`.  This is also immediate by separating
the even and odd cases; for example, at `n=8` the two score lists are

```text
p_8: 3,6,10,14,15,12,8,4  -> 1,3,5,7,8,6,4,2,
q_8: 4,8,12,15,14,10,6,3  -> 2,4,6,8,7,5,3,1.
```

Stable tie-breaking is irrelevant on these states.  With distinct cyclic
scores, `A_n` commutes with rotation, so (2.1) alternates between rotations
of `p_n` and `q_n`.  Distinct entries give rotational period `n`; moreover
`q_n` is not a rotation of `p_n` because each contains 1 once, at its first
position, and `p_n!=q_n`.  The full period is therefore `2n`.  `square`

## Exact obstruction to a complete theorem

The attractive first conjecture was that this principal orbit supplied the
whole recurrent set.  Complete functional graphs refute it:

| rank | recurrent cycle multiset | maximum tail | image | maximum one-step fibre |
|---:|---|---:|---:|---:|
| 5 | one 10-cycle | 5 | 58 | 8 |
| 6 | one 12-cycle, one 6-cycle | 11 | 242 | 14 |
| 7 | one 14-cycle | 24 | 1,551 | 23 |
| 8 | one 16-cycle, one 8-cycle | 33 | 10,083 | 54 |
| 9 | three 18-cycles, one 9-cycle | 41 | 74,970 | 99 |

Thus even/odd parity does not classify the recurrent atlas: odd rank 9 is the
first odd rank with extra cycles.  The transient depths and fibres also grow
without a detected target-local statistic.  `verify_asr_kill.py` exhausts
every permutation through `S_9`, checks the principal identity again through
rank 100, and records **409,243 assertions**.

## Owner boundary and decision

Bounded searches covered “rank adjacent cyclic sums,” “permutation adjacent
sum ordering map,” and cyclic distinct-adjacent-sum constructions.  They
located literature on arranging cyclic residues with distinct adjacent sums,
but not this stable-rank iteration.  That literature owns a neighbouring
static construction, not (2.1), and the search non-hit is not novelty
evidence.

The map is a useful genuinely different literal probe, but one explicit
cycle family is not a recurrent classification, and no every-target fibre or
independent structural count survived.  It is therefore a **current kill**,
not a reserve and not a paper allocation.
