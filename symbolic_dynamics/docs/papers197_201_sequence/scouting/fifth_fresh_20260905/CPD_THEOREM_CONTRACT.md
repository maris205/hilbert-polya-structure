# Circular parking displacement feedback (CPD)

Status: **KILL_OWNER_THIN / HOLD_EXTERNAL**, following the independent gate
`../../reviews/cpd_cspd_owner_gate_20260905/OWNER_TRANSFER_GATE.md` (relative
to the batch root, `reviews/cpd_cspd_owner_gate_20260905/OWNER_TRANSFER_GATE.md`).
No paper allocation. The original theorem spike and canonical verifier
transcript are retained as correct negative evidence. Its shallow temporal
axis and the directly adjacent parking-outcome scout `D05_CPA` do not clear
the separate-contribution threshold; see `BREADTH_AND_KILL_LEDGER.md`.

## Literal map

For `n>=1` the carrier is `X_n={0,...,n-1}^n`. Given preferences `a`, cars
`i=0,...,n-1` arrive in that order at a directed circular car park. Car `i`
starts at `a_i` and parks at the first unoccupied site clockwise. Let `d_i`
be the number of occupied sites it passes. Define `D(a)=d`. The car park is
emptied before each new epoch. This outputs displacement, **not** the
assignment permutation output by the old `D05_CPA` map.

## Theorem A: complete dynamics

Put `I_n=prod_{i=0}^{n-1}{0,...,i}` and `C(d)_i=i-d_i` on `I_n`.

1. `im D=I_n` and `D|I_n=C`; hence `D^3=D`.
2. `Rec(D)=I_n`. For `n>=2` every recurrent orbit is a strict two-cycle,
   so there are `n!/2` cycles and no fixed points. At `n=1` the sole state
   is fixed.
3. Tail is exactly `0` on `I_n` and `1` off `I_n`. At `n>=2` its maximum
   is one, and the depth counts are `n!` and `n^n-n!`.

Proof. At car `i` at most `i` sites are occupied, so `0<=d_i<=i`.
For preferences in `I_n`, induction shows that car `i` parks at site `i`:
its preference is at most `i`, and sites `0,...,i-1` are precisely the
occupied ones. Therefore its displacement is `i-a_i`. The complement is an
involution and hits every point of `I_n`, proving the image and cubic law.
For `n>=2` coordinate one has no fixed integral complement. All conclusions
follow. This is a proof, not an inference from the verifier.

## Theorem B: target-resolved inverse atlas

For an arbitrary target `d notin I_n`, the fibre is empty. For `d in I_n`,
let `A_d(S)` be defined for subsets of `{0,...,n-2}` by

```
A_d(empty)=1,
A_d(S)=sum_{L subset S\{m}, |L|>=d_m}
            A_d(L) A_d(S\({m} union L)),  m=max S.
```

Then

```
|D^{-1}(d)| = n A_d({0,...,n-2}).
```

In particular this quantity is independent of `d_(n-1)`.

Proof. A parking outcome can be encoded by the cyclic ordering of car
labels around the spots. Fix car `n-1` at spot zero, leaving `n` choices of
global rotation. Just before car `i` arrives, its required displacement
`d_i` is possible exactly when at least `d_i` consecutive sites immediately
counterclockwise from its outcome site have smaller labels. For each
compatible outcome there is a unique input preference, namely outcome site
minus `d_i` modulo `n`. Car `n-1` has all other sites already occupied, so
any of its `n` permitted displacement values works.

Cut at car `n-1` to obtain a linear permutation of the other labels. Its
maximum `m` separates a left subword `L` and a right subword `R`. The number
of smaller labels immediately preceding `m` is exactly `|L|`, and for
other labels a larger boundary (`m` or the cut label) blocks further runs.
Thus the conditions recurse independently on those two subwords. Choosing
their label sets gives exactly the displayed subset recurrence.

At time `t>=1`, use `D^t=C^(t-1)D` to obtain

```
|(D^t)^{-1}(d)| = |D^{-1}(C^(t-1)d)|  (d in I_n),
```

and zero outside `I_n`.

## Theorem C: sharp fibre maximum and all maximizers

For every `n>=1`, `max_d |D^{-1}(d)|=n!`. For `n>=2`, equality holds
precisely at the `n` targets

```
d_0=...=d_(n-2)=0, 0<=d_(n-1)<=n-1.
```

Proof. Each permutation of occupied sites permits at most one preference
vector with prescribed displacements, giving the `n!` bound. When all
earlier displacements vanish, every outcome works, as does every choice
for the last displacement. Conversely, if `d_i>0` for some `i<n-1`, choose
an outcome in which car `i` occurs immediately clockwise after car `n-1`.
The preceding spot is still empty when `i` arrives, so this outcome is
incompatible; the fibre is strictly smaller than `n!`. The `n=1` boundary
is immediate.

## Scope and threshold caveat

The circular parking procedure, displacement statistic, inversion-sequence
bounds, prescribed-outcome reconstruction, and decreasing Cartesian-tree
decomposition are background and receive zero novelty credit. The question
for a hostile gate is whether feeding the displacement vector back, plus
the exact target inverse and all maximizers, has sufficient residual mass.
The whole time theorem is short; it must not be embellished as a long-time
discovery. Generic one-step-to-involution systems and `D05_CPA` make a
`RESERVE` or `KILL_OWNER_THIN` outcome entirely possible.
