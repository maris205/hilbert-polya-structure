# Narrative report

HCS-C215 gives one complete owner to the partition-valued Kingman coalescent.
Pairwise rate-one mergers induce the pure-death block chain
`lambda_k=binom(k,2)`, but the package keeps the labelled partition process in
view so that exchangeability and projective consistency are not lost.

The all-`n` transition law is hypoexponential.  Independent holding times give
the MRCA product transform, exact mean and variance, and a monotone
projective-coupling limit with finite absorption time.  Scaling each holding
time by its number of branches turns total tree length into a sum with rates
`1/2,1,3/2,...`.  These are precisely the exponential order-statistic spacings,
so the exact CDF is `(1-exp(-ell/2))^(n-1)`, including its `n=1` boundary.

The checker recomputes all finite rows, semigroup identities, Bell numbers,
moments, and CDF values independently.  SymPy verifies partial fractions and
the beta-integral transform.  Replay, hostile mutations, and deterministic
PDF builds close reproducibility.  The source is attributed rather than
claimed novel, and no Markov determinant is called an Artin--Mazur zeta or an
arithmetic object.
