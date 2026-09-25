# Evidence and reproducibility boundary

## Primary source

- K. Miyamoto and H. Umeo, *Real-Time Generation of Prime Sequence by
  One-Dimensional Cellular Automaton with 8 States*, AROB 2012, pp. 666--668:
  [open PDF](https://alife-robotics.co.jp/members2012/icarob/data/papers/GS3/GS3-5.pdf).
  The source defines the half-line CA and sequence-generation condition, states
  the quiescent/boundary initialization, describes the sieve mechanism, and
  states the eight-state/301-rule theorem.
- H. Umeo and N. Kamikawa, *Real-Time Generation of Primes by a
  1-Bit-Communication Cellular Automaton*, *Fundamenta Informaticae* 58
  (2003), 421--435, DOI
  [10.3233/FUN-2003-583-412](https://doi.org/10.3233/FUN-2003-583-412).
  This earlier source independently identifies the same class of fixed-rule,
  real-time sieve CA constructions.

## Method

No numerical experiment was run. The new result uses only the source's
sequence-generator specification plus the elementary periodicity argument in
`paper.md` §3. It does not treat a diagram snapshot or finite simulation as
evidence for an infinite orbit claim.
