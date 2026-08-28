# Research question

**Can the partition-valued Kingman coalescent be treated as one complete
genealogical owner—rather than a collection of unrelated Markov formulae—by
closing its all-`n` block transitions, MRCA law, branch-length law, and
projective absorption limit with auditable evidence?**

The answer is yes at the classical source-theorem level.  Pairwise rate-one
mergers induce independent exponential holding times and a uniform jump chain;
partial fractions give every block-count transition; and exponential
order-statistic spacings identify the total branch length as a maximum of iid
exponentials.  The answer is deliberately negative for arithmetic promotion.

## Frozen assumptions

* States are labelled set partitions of `[n]`, with restriction maps under
  deletion of labels.  Every pair of current blocks merges at rate one.
* `K_t` denotes the number of blocks, `T_n` the absorption/MRCA time, and
  `L_n=sum_k k E_k` the total tree length.
* The holding variables in one standard construction are independent, and the
  pair selected at each jump is uniform independently of holding durations.
* The infinite-sample statement uses the standard projective coupling, not
  independent marginal copies.
* No determinant is called an Artin--Mazur zeta and no arithmetic data enter.

## Falsifiers

Release stops if a partial-fraction transition disagrees with an independently
computed semigroup, row sums or Chapman--Kolmogorov fail, MRCA or branch
moments disagree, the exact branch CDF fails, Bell-number partition checks or
the `n=1` boundary fail, the projective limit is misstated, or a repaired-hash,
stale-hash, or unknown-key mutation is accepted.
