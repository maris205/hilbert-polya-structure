# DDI independent owner and collision audit

Audit date: 2026-09-03  
Status: **KILL / EXACT INTERNAL DUPLICATE / HOLD_EXTERNAL**  
Novelty boundary: bounded search only; no novelty or priority claim

## Frozen author snapshot

| file | SHA-256 |
|---|---|
| `CANONICAL.txt` | `0e722c2bdfdcc8604160be42f6d4082cae65b8fd9d5da346a54c15b2dda29cce` |
| `OWNER_SEARCH_LOG.md` | `5da6b79fa7122a9b3412c3c9484683f36a30661b8752ce4bbbec8ea72e474052` |
| `SCOUT.md` | `e4c71ebdb753f4a51fbd35b5caa2ded9b5ceb18a9e54a6a42c9074f47905fe01` |
| `verify_scout.py` | `73f45adc1f3da591f31909f8af00e1b858d9393de6e8d986b019c8220eb40dff` |

Hashes were pinned before the author files were read.  No author file was
modified.

## Fatal internal collision

The proposed map

`Phi_N(d)=lcm(d,N/d)/gcd(d,N/d)`

is exactly, symbol for symbol, the previously screened candidate `D01` and
the archived `X01 complementary-divisor tent`:

- `docs/papers132_136_sequence/replacement_scout/algebraic/SCOUT.md`, Section
  4, gives the same map and the same exponent rule `a -> |2a-e|`;
- `docs/papers132_136_sequence/phase1/HOSTILE_GATE_REPLACEMENT_ALGEBRAIC.md`
  labels `D01` **KILL -- EXACT INTERNAL DUPLICATE** and expressly says not to
  resurrect it as a reserve or fallback;
- `docs/papers122_126_sequence/proof_spikes/X01_DIVISOR_TENT_REPORT.md` is the
  older proved archive, marked **KILLED AFTER HOSTILE OWNER/VALUE GATE /
  CORRECT ARCHIVE ONLY**.

The old X01 dossier already contains:

1. the same literal gcd/lcm divisor self-map;
2. the same sign-quotient doubling formula;
3. every point's preperiod **and least eventual period**;
4. every depth layer and sharp height;
5. every iterated target fibre, including both endpoint corrections;
6. every fixed-iterate count, Möbius cycle count, and zeta function;
7. the same Cartesian product over prime exponents.

Thus the old archive is strictly stronger than the current DDI contract: DDI
does not add the archived pointwise least-period formula.  Renaming X01/D01 as
DDI cannot reopen a candidate already killed by an independent portfolio
gate.

P142 is a second, non-exact but severe portfolio collision.  P142 already
occupies a literal divisor/valuation map reduced to a finite tent-type scalar
map and proves recurrence, fixed iterates, pointwise/sharp clocks, a temporal
polynomial, image, and every-target fibres.  Taking products over the prime
exponents of `N` is standard unique-factorization bookkeeping and does not
create a new proof engine.

## External owner subtraction

The internal collision alone decides the gate, but the external boundary is
also owner-heavy.

- Cobeli and Zaharescu, [*A game with divisors and absolute differences of
  exponents*](https://arxiv.org/abs/1411.1334) (JDEA 2014, DOI
  `10.1080/10236198.2014.940337`), directly studies a divisor game whose
  action occurs through absolute differences of prime exponents.
- Cobeli, Prunescu and Zaharescu, [*A growth model based on the arithmetic
  Z-game*](https://arxiv.org/abs/1511.04315) (Chaos, Solitons & Fractals 2016,
  DOI `10.1016/j.chaos.2016.05.016`), explicitly defines
  `Z(a,b)=ab/gcd(a,b)^2`.  DDI is exactly the fixed-complement specialization
  `Z(d,N/d)`.  The operation, its absolute-difference exponent rule, and its
  name therefore receive zero credit.
- OEIS [A332618](https://oeis.org/A332618) records the exact static summand
  `lcm(d,n/d)/gcd(d,n/d)` and the identity `n/gcd(d,n/d)^2`; static arithmetic
  receives zero credit.
- Scheicher--Sirvent--Surer,
  [*Dynamical properties of the tent map*](https://doi.org/10.1112/jlms/jdv071),
  is a primary control for tent-map periodicity transfer.  The continuous
  full tent map and circle-doubling/sign quotient are classical.
- Tan and Li, [*Graph Structure of the Generalized Tent Map over Ring
  Z_(2^e)*](https://arxiv.org/abs/2501.12645), explicitly studies functional
  graphs of finite fixed-precision tent maps.  Its literal quantization is not
  DDI, but it confirms that “finite tent functional graph” is an active direct
  owner lane rather than residual novelty.

The bounded exact-string search did not locate an external source that
iterates precisely `d -> Z(d,N/d)` on `Div(N)` and states the whole atlas.
That non-hit has no positive weight and cannot override the exact internal
duplicate.

## Contribution subtraction

Every advertised theorem is transported from the same elementary quotient:

`Div(N) ~= product_i {0,...,e_i}` and
`a -> |2a-e| ~= ([x] -> [2x]) on Z/(2e) modulo x~-x`.

The point tail is two-adic valuation loss; depth histograms count valuation
classes; fixed/cycle formulae count solutions of `2^k x=+/-x`; images and
fibres count solutions of `2^t x=+/-y`; products are Cartesian products.
Endpoint sensitivity is a correct Burnside correction, not an independent
axis.  The archived X01 proof already performs all these steps.

## Verdict

**KILL.**  There is no repair that makes this same literal system eligible in
the current portfolio.  Preserve it only as a correct historical negative
control.  A replacement must change the carrier/update and introduce a proof
object not transported from sign-quotient doubling or from P142's
divisor-valuation atlas.

