# SD-C10 Experiment Report

## Outcome

The recurrent positive-cone symbolic transfer succeeds exactly at the base
trace level and fails exactly at the first chiral-adjoint moment.  Distinct
positive free generators are the frozen universal realization, but the
positive-abelian control proves that freeness is not the mechanism.

```text
base recurrent graph + positive labels:
    every mixed closed word is killed by tau                  PROVED

chiral adjoint:
    gg^-1 and g^-1g backtracks appear at r=2                 PROVED

free-group specificity:
    positive free-abelian Z has the same base cancellation   REFUTED

actual mechanism:
    cocycle into a conical/positive monoid                   PROVED

global FK/Brown determinant:
    finite/rooted proxies only                               OPEN
```

No Riemann-zero data were loaded, compared, or fitted.

## Frozen object

For an entropy-ordered finite atom prefix and a bidirectional nearest-
neighbor symbolic graph,

\[
 (L_s)_{ii}=p_i^{-s}\lambda(e),\qquad
 (L_s)_{ji}=\left(\alpha p_i^{-s}+(1-\alpha)p_j^{-s}\right)
              \lambda(g_{ij}).
\]

Every directed cross edge receives a distinct positive free generator; the
reverse graph edge receives another positive generator, not the inverse.
The frozen candidate uses `alpha=1/2`.  The trace is

\[
 \mathfrak t=\operatorname{Tr}_{N}\otimes\tau,
 \qquad \tau(a)=\text{coefficient of the group identity in }a.
\]

Predeclared exact cutoffs were `r<=10` for the three-atom base ledger and
`r<=6` for the chiral ledger.  Additional atom cutoffs `N=2,3,4` were
enumerated through `r=8`.

## Raw data tables

### Exact base trace, three atoms

| r | closed paths | mixed closed paths | tau survivors | mixed tau survivors | exact trace |
|---:|---:|---:|---:|---:|---|
| 1 | 3 | 0 | 3 | 0 | `x0+x1+x2` |
| 2 | 7 | 4 | 3 | 0 | `x0^2+x1^2+x2^2` |
| 3 | 15 | 12 | 3 | 0 | `x0^3+x1^3+x2^3` |
| 4 | 35 | 32 | 3 | 0 | `x0^4+x1^4+x2^4` |
| 5 | 83 | 80 | 3 | 0 | `x0^5+x1^5+x2^5` |
| 6 | 199 | 196 | 3 | 0 | `x0^6+x1^6+x2^6` |
| 7 | 479 | 476 | 3 | 0 | `x0^7+x1^7+x2^7` |
| 8 | 1,155 | 1,152 | 3 | 0 | `x0^8+x1^8+x2^8` |
| 9 | 2,787 | 2,784 | 3 | 0 | `x0^9+x1^9+x2^9` |
| 10 | 6,727 | 6,724 | 3 | 0 | `x0^10+x1^10+x2^10` |

Across these powers there were 11,460 mixed closed paths and zero mixed
identity survivors.  All `N=2,3,4`, `r<=8` atom-cutoff cases also passed;
that auxiliary audit contained 6,104 mixed paths.

The resulting trace-log identity is

\[
 D_\tau(z)=\exp\left[-\sum_{r\ge1}\frac{z^r}{r}\mathfrak t(L_s^r)\right]
 =\prod_{i=1}^N(1-zp_i^{-s})
\]

formally.  The scalar trace series converges absolutely at `z=1` for
`Re(s)>1`, so the scalar Euler product is direct there.  An analytic
operator-determinant interpretation is asserted only on a chosen
small-norm/invertible logarithm branch, not globally.

### Chiral adjoint ledger

For \(B=\begin{psmallmatrix}0&L\\L^*&0\end{psmallmatrix}\):

| r | closed paths | mixed closed paths | tau survivors | mixed tau survivors | mixed identity extra |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 0 | 0 | 0 | `0` |
| 2 | 14 | 8 | 14 | 8 | `2*(y01^2+y10^2+y12^2+y21^2)` |
| 3 | 0 | 0 | 0 | 0 | `0` |
| 4 | 70 | 64 | 54 | 48 | nonzero positive polynomial |
| 5 | 0 | 0 | 0 | 0 | `0` |
| 6 | 398 | 392 | 242 | 236 | nonzero positive polynomial |

The first eight mixed identities at `r=2` are precisely each directed cross
edge followed by its adjoint, in both chiral parity blocks.  Algebraically,

\[
 \mathfrak t(B_t^2)=2\sum_i|d_i|^2+2\sum_{i\to j}|c_{ij}(t)|^2.
\]

### Label controls

| label system | first mixed identity | result |
|---|---:|---|
| distinct positive free generators | none through 12; all-order proof | pass |
| 32 random positive free-generator assignments | none through 8; 32/32 pass | `PROVES_TOO_MUCH` |
| positive labels in free abelian `Z` | none through 12; all-order proof | `PROVES_TOO_MUCH` |
| inverse-paired free labels | 2 | fails immediately |
| distinct labels in finite nonabelian `S3` | 4 | finite relation failure |
| positive labels in finite abelian `C5` | 10 | finite relation failure |

These first-failure lengths combine the group relation with admissibility in
the vertex graph.  The bidirectional chain is bipartite, so every closed path
uses an even number of cross edges.  With every `C5` label equal to `+1`, the
cross count must be both even and divisible by five; its smallest positive
value is `lcm(2,5)=10`.  For the frozen `S3` assignment, the two-step label
composite on the edge pair `1<->2` is a transposition of order two.  Squaring
that composite gives the first admissible identity after four cross steps;
no two-step paired product is identity.  Thus neither failure should be
reported merely as “at the order of an individual label.”

The six-dimensional regular representation of `S3` reproduced the canonical
group trace exactly at every power `r<=12` (maximum residual zero).  Its
trace changes from the pure-loop value 3 to 5 at `r=4`, then grows to 6,493
at `r=12`, of which 6,490 paths are mixed identity contributions.

### Endpoint-alpha chiral moments

Three atoms, 401 heights on `0<=t<=40`:

| alpha | range of tau Tr B^2 | range of tau Tr B^4 | motion |
|---:|---:|---:|:---:|
| 0 | `1.78e-15` | `6.22e-15` | no |
| 0.125 | `1.129011` | `2.839554` | yes |
| 0.25 | `1.935447` | `4.468142` | yes |
| 0.5 | `2.580596` | `5.531214` | yes |
| 0.75 | `1.935447` | `4.468142` | yes |
| 0.875 | `1.129011` | `2.839554` | yes |
| 1 | `1.78e-15` | `3.56e-15` | no |

The endpoints are exact left/right phase gauges.  The symmetric point has
the largest interference motion, but this motion lives in the quadratic
backtracking sector that broke the chiral Euler ledger.

### Atom-cutoff motion

| N | last atom | free rank | range of tau Tr B^2 | range of tau Tr B^4 |
|---:|---:|---:|---:|---:|
| 2 | 3 | 2 | `1.632993` | `3.402069` |
| 3 | 5 | 4 | `2.580596` | `5.528650` |
| 4 | 7 | 6 | `3.165947` | `6.404864` |
| 8 | 19 | 14 | `3.949582` | `7.090023` |
| 16 | 53 | 30 | `4.217665` | `7.178704` |
| 32 | 131 | 62 | `4.264681` | `7.185070` |

All cutoffs move.  The `B^4` range increments decrease from `2.12658`
(`N=2 -> 3`) to `0.00637` (`N=16 -> 32`), a numerical plateau rather than
an infinite-cutoff theorem.

### Inventory controls

| inventory | tau Tr B^4 range | ratio to tensor-atom range | base ledger |
|---|---:|---:|:---:|
| entropy-ordered tensor atoms | `7.090268` | `1.0000` | exact |
| shuffled same atoms | `6.431733` | `0.9071` | exact |
| composites only | `2.285245` | `0.3223` | exact |
| matched-count random integers | `0.096146` | `0.0136` | exact |

The controls differ quantitatively but all pass “exact ledger plus chiral
motion.”  That pair of properties is therefore not an arithmetic selector.

### Word-ball singular and determinant probes

For the two-atom candidate at `alpha=1/2`, height zero:

| radius | ball dim | min/median/max singular value | empirical tau(L*L) | rooted tau(L*L) |
|---:|---:|---|---:|---:|
| 1 | 5 | `0.2727 / 0.7071 / 1.1719` | `1.1633` | `1.65825` |
| 2 | 17 | `0.1758 / 0.7071 / 1.2386` | `1.2215` | `1.65825` |
| 3 | 53 | `0.1293 / 0.7071 / 1.2609` | `1.2380` | `1.65825` |
| 4 | 161 | `0.1020 / 0.7071 / 1.2709` | `1.2432` | `1.65825` |

The rooted second moment is already exact at radius one; the normalized
empirical moment is boundary-biased because free-group balls are not Følner.
For every word-ball case, ordinary eigenvalues lie exactly at the loop
values and the normalized finite determinant matches the loop product to
about `1e-14`, despite large singular motion.

At the safe small probe `z=0.25`, height zero, the rooted regularized
hermitization/FK-proxy error decreases as

```text
R=1: 2.206e-4
R=2: 6.488e-6
R=3: 1.912e-7
R=4: 5.809e-9
```

At `z=1`, the same errors instead are

```text
0.675, 0.940, 1.082, 1.156,
```

while the ordinary finite determinants remain loop-exact.  This cleanly
separates the local trace-log identity from an unproved global FK/Brown
identity.  No Brown measure is claimed.

## Key findings

### 1. Recurrence and an exact Euler ledger coexist after group labelling

- **Observation:** 11,460 mixed closed paths through `r=10` are all killed by
  the identity-coefficient trace.
- **Interpretation:** recurrence remains in the base graph, while its mixed
  cycles leave the identity sector of the skew product.
- **Implication:** the Paper07 DAG obstruction can be bypassed at the
  group-valued symbolic level without signed numerical cancellation.
- **Next step:** establish determinant-class estimates for an infinite atom
  prefix, still using only the canonical group trace.

### 2. Chiral self-adjointization destroys the clean ledger at the first moment available

- **Observation:** the first nonzero chiral moment, `r=2`, contains eight
  mixed identity backtracks and the exact extra `2 sum_e y_e^2`.
- **Interpretation:** taking the adjoint necessarily supplies the inverse of
  every cross label; canonical trace cancellation cannot kill a norm square.
- **Implication:** the base Euler determinant and the chiral singular motion
  cannot be called one clean trace ledger in this construction.
- **Next step:** prove a no-go theorem for positive/faithful graded or relative
  traces, or exhibit an intrinsic non-faithful homological quotient and audit
  whether it also removes the divisor.

### 3. The mechanism is positive-cone, not free-group, specific

- **Observation:** free abelian `Z` and all 32 repeated/random positive label
  assignments retain the base result.
- **Interpretation:** no inverse can appear in a positive word; commutator
  geometry is unused by the holomorphic ledger.
- **Implication:** free-group labelling alone earns no arithmetic specificity
  credit and triggers a strong `PROVES_TOO_MUCH` warning.
- **Conclusion:** the exact base theorem is properly a **conical/positive
  monoid cocycle theorem**: any cocycle whose nonempty positive products
  exclude the identity gives the same cancellation, including the abelian
  monoid inside `Z`.
- **Next step:** seek a label rule forced by tensor-atom operations rather
  than chosen from any ordered group.

### 4. Finite relations are fatal at predictable word lengths

- **Observation:** inverse pairs fail at 2, the frozen `S3` labelling at 4,
  and `C5` at 10.
- **Interpretation:** the first group relation compatible with a closed
  vertex path becomes a spurious primitive identity word.
- **Implication:** finite quotients can validate finite regular trace code but
  cannot supply an all-order faithful replacement unless their girth grows
  with the trace cutoff.
- **Next step:** use residual-finiteness deliberately: select finite quotients
  injective on the preregistered word ball and quantify the required group
  size without interpreting that sequence as a canonical infinite model.

### 5. Ordinary finite spectra hide the singular geometry

- **Observation:** word-ball eigenvalues and determinants are exactly
  loop-diagonal while singular values and rooted moments move.
- **Interpretation:** positive skew paths form a finite acyclic radical;
  ordinary spectral data see only semisimplification.
- **Implication:** finite ordinary eigenvalue or determinant agreement is a
  maximally nonselective `PROVES_TOO_MUCH` control.
- **Next step:** analyze rooted hermitization moments, not normalized
  word-ball eigenvalues, and prove convergence before invoking FK/Brown
  terminology globally.

## Claim boundary

```text
all-order finite-N base tau trace:             PROVED
local/formal tau determinant product:          PROVED
first chiral gg^-1 contribution at r=2:        PROVED
endpoint gauge / interior moment motion:       PROVED algebraically;
                                                numerically audited
finite regular trace implementation:           EXACT for S3
word-ball singular/FK diagnostics:             NUMERICAL OBSERVATION
global Fuglede-Kadison determinant:             OPEN
Brown measure:                                  NOT ESTABLISHED
Riemann divisor / zero claim:                   NOT MADE
```

## Recommended next same-family experiment

The smallest useful continuation is a theorem-level audit of a *relative or
graded identity-sector trace* on the same labelled symbolic graph:

1. require it to preserve every base loop repetition;
2. require it to cancel the quadratic adjoint backtracks;
3. test faithfulness/positivity and determinant multiplicativity;
4. stop immediately if all-order cancellation makes the relative determinant
   one or if arbitrary ordered abelian labels still pass.

Separately, prove convergence of rooted hermitization moments for fixed
polynomial degree before attempting any infinite FK/Brown claim.

## Reproduction

```bash
cd papers/08-positive-cone-recurrent-trace
python code/sdc10_positive_cone_experiment.py
pytest -q code/test_sdc10_positive_cone_experiment.py
```

Outputs:

- `results/summary.json`
- `results/exact_base_trace.csv`
- `results/exact_chiral_trace.csv`
- `results/exact_atom_cutoffs.csv`
- `results/alpha_motion.csv`
- `results/atom_cutoffs.csv`
- `results/inventories.csv`
- `results/finite_regular_s3.csv`
- `results/word_ball.csv`

Frozen integration test result: `8 passed`.
