# Bounded primary-owner and adjacency search

**Search date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Rule:** a bounded non-hit is not novelty, priority, ownership,
freedom-to-operate, or release evidence.

## Query vocabulary

The finalists were searched using literal and structural variants of:

```text
"prefix distinct count" iteration word map restricted growth sequence
"number of distinct symbols" prefix sequence combinatorics
prefix diversity transform first occurrence word iteration
statistic restricted growth word prefix distinct letters
subset transform "a_i-i" iteration finite dynamical system
combinatorics map subset {a_i-i} distinct values
binary one positions minus rank zero-run support
partition beta set subtract rank support iteration subset
permutation rank pi_i-i displacement standardization iteration
stable rank transform permutation displacement dynamics
```

Searches were bounded to literal combinations and the nearest named
interfaces.  Sources below were inspected at the definition or theorem level
available from the primary/author-hosted text or publisher record.

## PDD: the RGF owner flag

Toufik Mansour and Vincent Vajnovszki,
[*Efficient generation of restricted growth words*](https://doi.org/10.1016/j.ipl.2013.05.008),
*Information Processing Letters* 113 (2013), 613--616, is the strongest
adjacent owner located.  Its statistic-restricted-growth framework explicitly
uses prefix statistics to constrain the next letter.  Restricted-growth
words, first-occurrence encodings, and prefix-statistic generation therefore
receive **zero contribution credit**.

This source is flagged because it is not merely a generic word reference: its
interface is the closest inspected RGF/prefix-statistic construction.  In the
inspected title, abstract, and available author/publisher text, it did not
state the autonomous map

```text
w -> (number of distinct letters in each strict prefix of w)
```

or the all-time shift, clock, and every-target fibre conjunction proved in
`PDD_THEOREM_SPIKE.md`.  That is a bounded non-hit only.  A fuller search that
finds the literal transform, even under RGF terminology, reopens the gate.

## RCS: the direct rank-subtraction owner flag

Richard P. Stanley's author-hosted combinatorics notes
[*Enumerative Combinatorics: Selected Notes*](https://math.mit.edu/~rstan/papers/comb.pdf)
record the classical weak/strict sequence shift `b_i=a_i+i-1` and its
stars-and-bars consequences.  Reversing this bijection is exactly the
rank-subtraction step `a_j-j` **before multiplicities are discarded**.  This
one-step strict-to-weak transform and all stars-and-bars/Fibonacci reductions
receive zero contribution credit.

Matthew Fayers,
[*Minimal Partitions with a Given s-Core and t-Core*](https://doi.org/10.1007/s00026-022-00577-4),
*Annals of Combinatorics* (2022), supplies adjacent beta-set language for
encoding partitions by finite sets.  Beta sets and gap/partition vocabulary
also receive zero credit.

These sources are explicitly flagged as the closest subset-transform owners.
In the inspected texts, neither takes the **support** of the weak list and
feeds that set back into the same rank-subtraction rule, nor states the
ordered all-time gap deletion and coefficient-sum fibre formula.  Again, this
is only a bounded non-hit, not positive evidence.

## DSR reserve adjacency

- The primary article
  [*Ranks, copulas, and permutons*](https://doi.org/10.1007/s00184-023-00908-2)
  treats rank transforms as an established interface.
- The *Electronic Journal of Combinatorics* article
  [*Permutation displacement patterns*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p1/pdf/)
  documents the mature permutation-displacement setting.

No inspected source was needed to kill DSR directly: the internal theorem
gate already fails because the numerical convergence through `S_9` has no
general clock proof or complete inverse.  The sources prevent stable ranking
of `pi_i-i` from being treated as owner-free vocabulary.

## Direct owner inherited for the BDS kill

Amritanshu Prasad and Samrith Ram,
[*Set partitions, tableaux, and subspace profiles under regular diagonal
matrices*](https://doi.org/10.1016/j.ejc.2024.104060), *European Journal of
Combinatorics* 124 (2025), 104060, define the set-partition-to-tableau
occurrence-rank transform and give its fibre formula.  The present BDS rule
uses numerical distance from an old block minimum and is not literally their
map, but this owner makes the nearby tableau/column mechanism high pressure.
Because BDS also lacks a proved general clock/inverse, it is killed rather
than forced.

## Search conclusion

| candidate | direct literal iterative owner located in this bounded pass? | decision |
|---|---:|---|
| `PDD` | no; close RGF/prefix-statistic owner explicitly flagged | internal recommendation only, `HOLD_EXTERNAL` |
| `RCS` | no; direct one-step rank-subtraction bijection and beta-set owners explicitly flagged | internal recommendation only, `HOLD_EXTERNAL` |
| `DSR` | no claim; adjacent rank/displacement owners found | reserve, not promotable |
| `BDS` | adjacent occurrence-rank tableau owner already decisive pressure | kill |

No row in this table is a novelty certificate or an authorization to assign a
paper number.

