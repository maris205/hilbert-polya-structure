# P140 paper plan

## Status

`ANONYMOUS_ROUND1 / REVIEW_A_REPAIRED / GO_INTERNAL / HOLD_EXTERNAL`

This is a short exact-probability note about a shrinking binary-word process.
It is not a majority-vote model on a fixed carrier, and no external release is
authorized.

## One-sentence residual

For uniform majority contraction of a length-three window in a two-run odd
binary word, derive the complete absorption split, terminal history counts,
the cross-boundary history PGF with its one-cross coefficient, and an
independent continuous clock having an exact Beta representation and Gamma
limit.

## Formal claim spine

1. **P140-C1, two-run closure.** Classify every current window as left
   homogeneous, right homogeneous, or boundary crossing, including block-size
   one and two boundaries.
2. **P140-C2, endpoint and history laws.** Prove the harmonic absorption law
   and multiply by the common history denominator `(n-2)!!`.
3. **P140-C3, marked cross PGF.** Give the exact polynomial recurrence,
   symmetry, coefficient support, and the closed exactly-one-cross atom.
4. **P140-C4, whole-history clock independence.** Use equal-rate exponential
   races and strong Markov memorylessness at every deterministic length to
   separate the entire holding-time vector from the entire window history.
5. **P140-C5, Beta/Gamma clock law.** State `tau_1=0` almost surely; for
   `n=2m+1>=3`, evaluate the Laplace product and identify
   `exp(-2 tau_n)` as `Beta(1/2,m)`; then prove the rate-one Gamma limit along
   `m -> infinity`.

## Owner subtraction, before novelty language

- Krapivsky--Redner own majority-rule opinion dynamics. Majority, consensus,
  and local-majority motivation receive zero credit.
- Goles--Montealegre--Salo--Torma exemplify majority automata on a fixed
  carrier. Fixed-carrier majority dynamics and complexity receive zero credit.
- Exponential races, the strong Markov property, beta--gamma algebra, and
  Gamma limits receive zero credit as standard machinery.
- The residual is the exact conjunction for this literal shrinking-word
  process. The bounded owner search is not a priority certificate.

## Hypotheses that must remain visible

- The word length is odd. The substantive two-run theorem assumes
  `a,b>=1` and `a+b=2m+1`; one-run boundary values are stated separately.
- A discrete history records current window positions, not unlabelled ternary
  trees or only the resulting state path.
- `C` counts heterogeneous window contractions along a two-run history.
- In continuous time every current window has rate one. The number of
  discrete contractions is deterministic; elapsed time is random.
- At `n=1`, both embedded vectors are empty and `tau_1=0` almost surely. The
  Beta identity is asserted only for `m>=1`, equivalently `n>=3`.
- `Gamma(alpha,1)` means shape `alpha`, rate one.

## Paper architecture

1. Subtract owners and define the literal process.
2. Prove two-run closure, absorption probabilities, and history counts.
3. Mark boundary crossings and prove the polynomial recurrence and extreme
   coefficient.
4. Construct the continuous-time chain and prove whole-history independence.
5. Derive the exact Beta representation, moments, and Gamma limit.
6. State the finite exact controls and their limitations.

## Evidence contract

The paper-local verifier is deterministic and uses only integers and
`fractions.Fraction`. It checks every binary word of odd length at most 15,
every two-run pair through total length 201, marked cross-history polynomials
through total length 101, literal marked histories through length 13, joint
continuous-time transforms through length 11, and Laplace products through
length 201. These controls falsify finite instances; symbolic proofs carry all
unbounded and limiting statements.

## Round-A closure criteria

- Every claim above has a complete proof in `main.tex`.
- `code/verification_output.txt` is a byte-for-byte replay of `code/verify.py`.
- The stable repository build succeeds and the PDF/log/font/text checks pass.
- No claim confuses deterministic discrete count with random elapsed time.
- The degenerate `n=1` clock is explicit, and no `Beta(1/2,0)` law is stated.
- External status remains `HOLD_EXTERNAL`.
