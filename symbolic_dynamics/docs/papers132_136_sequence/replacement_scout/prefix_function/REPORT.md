# Repeated border-array dynamics on inversion sequences

**Stage:** post-hostile-gate repair; eligible for the internal Stage-2 short-paper lane.  
**Disposition:** theorem-complete reserve; it may not coexist with another
inversion-sequence paper in the final five.  The owner search remains bounded
and supplies no novelty or priority certificate.  
**External status:** `HOLD_EXTERNAL`.

## 1. Literal self-map

Let

```text
E_n = {(e_0,...,e_(n-1)) : 0 <= e_i <= i}.
```

Regard `e` as an integer word.  Define `Pi_n(e)=p`, where `p_i` is the length
of the longest proper prefix of `e_0...e_i` that is also a suffix.  This is
the ordinary Morris--Pratt border array, often called the KMP prefix-function
array.  Since `0<=p_i<=i`, it is a literal self-map of `E_n`.

The map depends only on equality of letters, but the carrier is not an
arbitrary alphabet: the subexceedant bounds make every one-step fibre finite
and give the factorial extremum in Section 4.

## 2. Complete recurrent atlas

For `1<=r<n`, put

```text
A_r = (0,1,...,r,0,...,0),
B_(r+1) = (0,...,0,1,...,1),
```

where `B_(r+1)` has `r+1` initial zeros.  Direct border inspection gives

```text
Pi_n(A_r)=B_(r+1),       Pi_n(B_(r+1))=A_r.             (2.1)
```

Indeed, a prefix of `A_r` ending in its initial distinct slope has no
nonempty border; after the slope its longest border is the single zero.  A
prefix of `B_(r+1)` inside the initial zero run has border one shorter than
itself, while any prefix ending in the one run has no nonempty border.

These are all recurrent states.  Thus `n=1` has one fixed state, and for
every `n>=2` the graph has exactly

```text
2(n-1) recurrent states = n-1 cycles of exact period two.              (2.2)
```

The exhaustion of the recurrent set follows from the convergence proof
below rather than from finite enumeration.

## 3. Canonical-prefix amplifier and sharp clock

Call an integer array *valid* if it is the border array of some word.  The
one-step image of `Pi_n` is exactly the valid arrays of length `n`: one
inclusion is definitional, and for the converse one may standardize any
realizing word by the order of first occurrence of its letters.  The
standardized word lies in `E_n` and has the same equality pattern.

Every valid array `p` has `p_0=0` and `p_1` equal to zero or one.

- If `p_1=1`, take the maximal initial slope `0,1,...,r`.  If it is not the
  whole array, the next value is zero: a realizing word begins with `r+1`
  equal letters, so its next border is either `r+1` or zero.  Hence `p`
  agrees initially with `A_r`, including the first zero after the slope.
- If `p_1=0`, take its maximal initial zero run of length `k`.  If it is not
  the whole array, the next value is one because every border array obeys
  `p_i<=p_(i-1)+1`.  Hence `p` initially agrees with `B_k`, including the
  first one after the zero run.

Index coordinates from zero.  Let `Q(p)` be the selected canonical template
and define

```text
L(p)=min{i : p_i != Q(p)_i},
```

with `L(p)=n` when no mismatch exists.  Thus `L(p)` is both the first
mismatch index and the number of agreeing coordinates.  A nonrecurrent valid
array has `L(p)>=3`.

**Indexed mismatch lemma.**  Let `q=Pi_n(p)` and suppose `L=L(p)<n`.

- If `Q(p)=A_r`, then `p_L=1`, `Q(q)=B_(r+1)`, `L(q)=L`, and `q_L=2`.
- If `Q(p)=B_k`, then `p_L` is zero or two and `Q(q)=A_(k-1)`.  If
  `p_L=0`, then `L(q)=L` and `q_L=1`; if `p_L=2`, then `L(q)>L`.
- After an extension, if a later mismatch exists, it is an `A` mismatch
  with actual value one.

Indeed, an `A` mismatch lies after the first zero following the slope.  The
preceding table value is zero, so the unit-growth inequality forces the
nonzero mismatch value `p_L=1`.  The border of the integer word
`p_0...p_(L-1)` has length one; its next comparison is with `p_1=1`, hence
`q_L=2`.  For a `B` mismatch, the preceding table value is one, so unit
growth and mismatch from the template value one leave exactly zero or two.
The current border of the word `p` has length zero.  A new zero matches
`p_0=0` and creates `q_L=1`, whereas a new two does not and creates `q_L=0`,
the required `A`-template value.  The same preceding-zero argument forces
the next unresolved mismatch, if any, to have value one.

Writing the actual value at the first mismatch after an `A` or `B` prefix,
the lemma is the exhaustive automaton

```text
A1 -> B2 -> extension,
B0 -> A1 -> B2 -> extension.                           (3.1)
```

Here “extension” means that the new array agrees with the partner template
through strictly more than `L(p)` coordinates.  The first mismatch of a valid
array is therefore resolved in at most three iterations.  After the first
extension, every remaining mismatch is resolved in at most two.  Starting
from `L>=3`, the explicit count is

```text
3 + 2(n-L-1) <= 3 + 2(n-4) = 2n-5.
```

Consequently

```text
max_(valid p) depth(p) <= 2n-5       (n>=4).             (3.2)
```

An arbitrary `e in E_n` becomes valid after one iteration, giving

```text
max_(e in E_n) depth(e) <= 2n-4       (n>=4).            (3.3)
```

Both bounds are sharp.  Let

```text
p_n=(0,0,1,0^(n-3)),
e_n=(0,1,0,2,1^(n-4)).                                  (3.4)
```

Then `Pi_n(e_n)=p_n`.  For `1<=j<=n-3`, direct application of the border
recursion gives

```text
Pi_n^(2j)(p_n)=(0,0,1^j,2,0^(n-j-3)),                  (3.5)
```

with the intervening arrays

```text
Pi_n^(2j+1)(p_n)=(0,1,0^(j+1),1,2^(n-j-4))
                                                    (0<=j<=n-4).       (3.6)
```

The last state in (3.5) maps to `A_1`.  Hence `p_n` has depth `2n-5` and
`e_n` has depth `2n-4`.  Together with the small boundaries,

```text
max depth = 0,0,1,2n-4  for n=1,2,3,n>=4 respectively.                 (3.7)
```

Equations (2.1) and (3.1) also show that no other recurrent state exists.

## 4. Sharp one-step fibre extremum

Fix a target border array and expose a source word from left to right.  At
position `i>=2`, a prescribed positive border value forces the next letter
to equal one already specified numerical value.  A prescribed zero border
must avoid at least the initial letter zero, leaving at most `i` choices
among `0,...,i`.  At position one either target value zero or one determines
the source letter uniquely.  Therefore

```text
|Pi_n^(-1)(p)| <= product_(i=2)^(n-1) i = (n-1)!.       (4.1)
```

For equality, every target coordinate from position two onward must be zero;
otherwise the one-choice positive-border step is strict.  There are exactly
two possible targets when `n>=2`:

```text
0^n,                    A_1=(0,1,0^(n-2)).              (4.2)
```

For `0^n`, the source has `e_1=1` and may choose any nonzero value at every
later position.  Position zero is then the only zero, so every proper suffix
starts with a nonzero letter and cannot equal a prefix, which starts with
zero.  For `A_1`, the source has `e_1=0` and the same nonzero freedom from
position two onward.  A proper suffix starting at position at least two again
fails in its first letter.  The only remaining possible proper suffix starts
at position one, but it fails in its second letter because `e_2!=0=e_1`.
Thus no prefix after position one has a nonempty border.  Both fibres have
exactly `(n-1)!` elements, and for `n>=2` they are the only maximizers.  When
`n=1`, the sole target `(0)` has the sole source `(0)` and maximum fibre one.

## 5. Exact audit

[`verify_prefix_function_dynamics.py`](verify_prefix_function_dynamics.py)
exhausts all `409,113=sum_(n=1)^9 n!` states through length nine and performs
868,745 exact assertions.  It compares the linear prefix-function routine
with a literal border search through length eight; checks carrier closure,
all recurrent states and periods, (3.1) on every valid table, both sharp
clocks, (3.4)--(3.6), and the exact maximum fibres.  The one-step image sizes
are

```text
1, 2, 4, 9, 20, 47, 110, 263, 630.                    (5.1)
```

These are recorded only as the classical valid-border-array census, not as a
contribution.  Reproduce the frozen transcript with

```bash
cmp -s <(PYTHONDONTWRITEBYTECODE=1 python3 verify_prefix_function_dynamics.py) \
  CANONICAL.txt
```

Enumeration is falsification evidence, not a proof.

## 6. Owner and collision boundary

Knuth, Morris, and Pratt own the prefix/failure-function mechanism and its
linear computation ([DOI 10.1137/0206024](https://doi.org/10.1137/0206024)).
Franek--Gao--Lu--Ryan--Smyth--Sun--Yang give a linear border-array validation
algorithm ([primary PDF](https://www.cas.mcmaster.ca/~franek/proceedings/border.pdf)).
Duval--Lecroq--Lefebvre treat online validation, construction, generation, and
counts of distinct border arrays
([DOI 10.1051/ita:2008030](https://doi.org/10.1051/ita:2008030)).
Gawrychowski, Jeż, and Jeż own validation and minimal-alphabet realization of
failure/border arrays
([DOI 10.1007/s00224-013-9522-8](https://doi.org/10.1007/s00224-013-9522-8)).
The valid-array image census (5.1), validation, generation, realization, and
standard border recursion all receive zero contribution credit.

The word *iteration* has two incompatible meanings in this literature.  The
classical notation

```text
beta^j[i] = beta(beta^(j-1)[i])
```

follows failure links inside the fixed border table of one fixed word.  The
present system instead treats the entire table as a new integer word and
recomputes every border:

```text
e -> beta(e) -> beta(beta(e)) -> ... .
```

Only this second operation is meant by *whole-array recomputation* below.
The manuscript may not use the unqualified phrase “iterating the prefix
function.”

Bounded searches for repeated/iterated border arrays, taking the prefix
function of a prefix-function array, and the displayed recurrent templates
did not locate this literal finite dynamical system or the sharp clock.  A
search non-hit is not novelty or priority evidence.

The internal collision firewall is explicit.

- P112 scout C6 follows the failure-link chain of one word; it is the first,
  classically owned notion of iteration above and was killed directly.  The
  present map recomputes the whole table synchronously.
- P105 already occupies permutation cycle-type pruning and a factorial/depth
  silhouette.  Here the carrier is an inversion-sequence encoding, recurrence
  consists of `n-1` two-cycles, and the factorial is a maximum fibre rather
  than a deepest layer.
- P122 already owns a permutation sharp-depth/image/fibre package, but its
  mechanism is record-block reversal and admissible cuts rather than equality
  patterns, valid border tables, and KMP fallback.
- The same-batch `PR1` inversion-rank candidate has an exact owner
  (Allagan--Gao--Testart, arXiv:2608.24476) and is killed.  This border-array
  system is the sole eligible inversion-sequence candidate; retaining both
  would be cosmetic carrier duplication.

The residual is only whole-array recomputation on the explicitly bounded
carrier, its `n-1` two-cycle atlas, the indexed canonical-prefix mismatch
amplifier, the piecewise sharp clock with value `2n-4` for `n>=4`, and the two
factorial extremal fibres.  It is otherwise distinct from the word-reversal,
majority, local-CA, sorting, pruning, and Euclidean systems in P1--P131.

**Post-repair disposition:** eligible for the internal Stage-2 short-paper
lane, subject to the one-inversion-carrier portfolio rule.  External status
remains `HOLD_EXTERNAL`; the bounded owner non-hit is not novelty or priority
evidence.
