# Occurrence-rank transpose: exact signal and decisive owner kill

**Handle:** `D01_ORT`  
**Final gate:** `KILL_DIRECT_OWNER`  
**External status:** `HOLD_EXTERNAL`

## Literal map and internally derived graph

Represent a set partition of `[n]` by its restricted-growth word.  Reading
left to right, replace an element by its zero-based occurrence number inside
its old block and canonicalise the resulting word.  Equivalently, list each
old block increasingly as a row and make the first elements, second elements,
and so on into the new blocks.

If the new blocks are drawn as the sorted columns of a Young diagram, they
form a standard Young tableau.  Reapplying the map transposes this tableau.
Consequently:

- `T^3=T`;
- for `n=1` the sole state is fixed;
- for every `n>=2` there are no fixed states and the entire image consists of
  2-cycles;
- the image has `I_n` states, where `I_n=I_(n-1)+(n-1)I_(n-2)` is the
  involution number;
- for `n=2` every state is recurrent, while for `n>=3` every nonimage state
  has depth one.

The exact program verifies the full graph through `n=9` and `T^3=T` on every
source.  It also reconstructs every target fibre by independent matchings
between adjacent tableau columns and verifies a gap-marked matching
polynomial through `n=8`.

## Direct owner identification

Prasad and Ram, *Set partitions, tableaux, and subspace profiles under
regular diagonal matrices*, European Journal of Combinatorics 124 (2025),
104060, DOI
[10.1016/j.ejc.2024.104060](https://doi.org/10.1016/j.ejc.2024.104060),
provide the decisive source; the accessible FPSAC version is
[here](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2022/35.pdf).

- Their Definition 2.1 lists each block increasingly as a row, sorts and
  top-justifies the columns, and calls the result the associated tableau.
  The blocks output by `D01_ORT` are exactly those sorted columns.
- Their Theorem 2.8 counts the complete fibre over every multilinear tableau
  by the product `c(T)`.  After transposing the display convention, this is
  the adjacent restricted-injection product derived here.
- Their Theorem 3.4 gives a `q`-enumerator of the same fibre by the
  interlacing statistic.  Thus even a natural marked inverse axis is already
  present in the owner neighbourhood.
- Their Theorem 4.4 also records the pivot-cell formula used by `D07_SPR`,
  reinforcing that the paper owns both static tableaux and Schubert-cell
  sides of this search.

## Why the temporal wrapper does not survive

Once Definition 2.1 is subtracted, the only temporal observation is that
feeding the associated tableau's columns back as blocks transposes the
tableau.  Tableau transposition is a classical involution, so `T^3=T`, the
involution-number image census, and the 2-cycle list follow immediately.  A
one-step owned projection followed by a classical involution is the same
thin architecture already rejected for the P166 `SCD` control.

The separately checked gap weight can be written as a weighted matching
permanent on the already owned fibre.  It does not restore a nontransferable
second theorem axis.  Therefore `D01_ORT` is retained only as a high-quality
negative control and must not receive a recommendation or paper number.
