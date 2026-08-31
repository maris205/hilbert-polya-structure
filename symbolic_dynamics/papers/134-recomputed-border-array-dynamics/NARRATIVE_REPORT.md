# Narrative report — P134

An ordinary border array is usually used as a static index into the borders of
one word.  This paper asks a different question: treat the whole integer table
as the next word, recompute all of its borders synchronously, and repeat.  The
phrase **whole-array recomputation** is kept throughout because classical
failure-link “iteration” means only following entries inside one fixed table.

The first update collapses the carrier of inversion sequences onto the valid
border arrays.  Every valid table begins in one of two canonical forms: an
initial slope `0,1,...,r` followed by zero, or an initial zero run followed by
one.  Their completed templates form `n-1` explicit two-cycles.  For a table
that departs from its template, the first mismatch can have only three labelled
states.  Ordinary border recursion gives

```text
A1 -> B2 -> extension,
B0 -> A1 -> B2 -> extension.
```

After the first extension, each later coordinate costs at most two updates.
This indexed mismatch amplifier both excludes further recurrent states and
gives the global upper bound `2n-4`.

The bound is exact.  A pair of equality-pattern witnesses advances one
canonical coordinate every two recomputations and reaches the `A_1/B_2`
two-cycle at the predicted time.  The small sizes `n=1,2,3` are separated
explicitly, giving the full maximum-depth law `0,0,1,2n-4`.

The inverse result uses only the subexceedant carrier bounds.  Prescribing a
positive border at position `i` forces the new letter; prescribing zero leaves
at most `i` choices.  This gives `(n-1)!` for every target.  Equality leaves
only the all-zero table and `010^(n-2)`.  Their source families are verified by
where a proper suffix can start, which repairs the tempting but false general
shortcut that a nonzero final letter alone forbids every border.

Border computation, validity testing, realization, generation, and census are
fully credited background.  The owner search for the repeated whole-array map
is bounded and its non-hit supports no novelty or priority inference.  The
manuscript is anonymous and remains `HOLD_EXTERNAL`.

