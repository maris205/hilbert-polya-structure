# Route-A dynamics-diversification batch plan: C139--C143

Status: **complete; five papers released as separate Route-A packages**.

Date: 2026-08-25

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round keeps the five candidates separate and deliberately changes the
dynamical mechanism from paper to paper.  Every finite ledger is only an
implementation sentinel.  All all-period, all-word, or analytic statements
require independent proofs.

## Frozen sequence and required progress

1. **C139 -- minimal four-block marker suspension.**  Extend C135's
   directed-edge roof by the local marker
   `sqrt(5) 1_{0011}`.  Prove the exact eight-state determinant, all-period
   primitive product, separation of `001011/001101`, and minimality of memory
   four for this frozen forward-cylinder comparison.  Retain the explicit
   collision `0101111/0110111`.
2. **C140 -- strictly sofic mod-three gap suspension.**  Use the label system
   in which consecutive `1` symbols are separated by a multiple of three
   zeros.  Prove strict soficity, minimal three-state Fischer cover, and the
   unique all-zero covering anomaly:

   ```text
   Z_140(u,v)=(1+v+v^2)/(1-u-v^3).
   ```

   The cover determinant must not be substituted for the label determinant.
3. **C141 -- stability-weighted complex quadratic Ruelle ladder.**  Freeze
   `F(z)=z^2-6`, its two inverse branches on the radius-four disk, and the
   weights `m=0,1,2`.  Prove trace class, complete periodic-point coding, the
   all-period trace formula, the `m=2` primitive Fredholm product, and the
   exact ladder `m=0` bare counting, `m=1` trace cancellation, `m=2`
   nontrivial stability retention.
4. **C142 -- trace-class countable renewal operator.**  Freeze
   `T=S+R` on `l2(N0)` with
   `S e_n=2^{-(n+1)}e_{n+1}` and
   `R e_n=2^{-(n+1)}e_0`.  Prove

   ```text
   det_F(I-zT)=1-sum_{m>=1}2^{-m(m+1)/2}z^m,
   ```

   entire order zero, and the primitive excursion product.  The
   constant-advance control must retain its formal rational renewal series
   while failing compactness and ordinary Fredholm ownership.
5. **C143 -- inhomogeneous coined quantum walk.**  Freeze two rational
   reflection coins on the five-cycle and `U_w=S C_w`.  Prove exact
   unitarity, `Theta_w=C_wK` time reversal, signed primitive path ownership,
   and the nonzero determinant difference between equal-population
   arrangements `00011` and `00101`.  Population averaging must be tested
   and rejected when it destroys unitarity.

## Uniform artifact contract

Each package contains 27 manifested payloads plus one self-excluded manifest:
source audit, research question, theorem package, experiment and paper plans,
narrative report, two-round internal improvement log, deterministic producer,
producer-independent checker, separate symbolic reconstruction, byte replay,
semantic mutation suite, results/test/hostile reports, Route-A YAML, LaTeX
source, three preserved snapshots, final PDF, compile report, exact evidence,
and release ledger.

Final release additionally requires isolated fixed-date double PDF builds,
embedded fonts, zero layout/reference/citation warnings, rendered-page visual
inspection, exact manifest disk closure, and no build caches.

## Strict boundary

The provisional tuples are:

```text
C139 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C140 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C141 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C142 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C143 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

No paper contains a frozen target divisor, target zero census, target
functional equation, target counting law, arithmetic local factor, Euler
factor, root number, automorphy statement, or Hilbert--Polya operator.
`route_b_invocation_allowed=false` for all five.

## Completion ledger

| paper | explicit retained progress | exact validation | release artifact |
|---|---|---|---|
| C139 | Exact eight-state four-block determinant and cutoff-free primitive product; the period-six pair first unresolved by all forward memories through three is separated, while the first residual feature collision occurs at period seven. | 16,467 checker assertions; 35 SymPy checks; 49/49 mutations rejected. | 2-page PDF; 27 manifested payloads + self-excluded manifest. |
| C140 | Strict soficity, intrinsic three-state right-Fischer lower bound, and exact all-period correction of the cover's unique all-zero anomaly. | 2,028 checker assertions; 53 SymPy checks; 54/54 mutations rejected. | 2-page PDF; 27 manifested payloads + self-excluded manifest. |
| C141 | Trace-class quadratic inverse-branch ladder with complete periodic-point exhaustion, exact `m=0/1` controls, and a nontrivial `m=2` product starting at stability index two. | 82 checker assertions; 38 SymPy/resultant checks; 37/37 mutations rejected. | 2-page PDF; 27 manifested payloads + self-excluded manifest. |
| C142 | Infinite-rank trace-class renewal owner with an exact entire order-zero Fredholm determinant and primitive excursion product; matched formal-but-noncompact control. | 110 checker assertions; 56 SymPy checks; 25/25 mutations rejected. | 3-page PDF; 27 manifested payloads + self-excluded manifest. |
| C143 | Exact inhomogeneous coined-walk unitary, antiunitary reversal, signed path product, and determinant sensitivity to equal-population spatial order. | 62 checker assertions; 39 SymPy checks; 30/30 mutations rejected. | 3-page PDF; 27 manifested payloads + self-excluded manifest. |

The final uniform audit totals are 18,749 checker assertions, 221 separate
symbolic checks, and 195/195 mutation rejections.  All five fixed-epoch
isolated double builds reproduce their checked-in PDFs byte for byte; the 12
rendered pages use embedded fonts and pass warning, layout, and visual gates.
