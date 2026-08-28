# P27 Round-8 theorem — a four-quadrant collective renormalization law

Date: **2026-08-28**

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Workflow position: ARS Stage 1 research, new-owner Route-A calibration
- Candidate: `P27-HOMOLOGY-RENORMALIZED-GEODESIC-PANEL`
- Freeze SHA-256:
  `88d10c3dcdee3387b16414d2c56d4934b6daeef6728acc689855049840850a72`
- Core-output SHA-256:
  `a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`
- Target prime/zero data: none

## New-owner declaration

This round does not alter the Round-7 residual inverse-limit object.  It
registers a different cover tower, a different clock, and a different
multiplicity normalization in order to test the smallest lawful collective
renormalization suggested by the previous no-go theorem.

Let `Sigma` be a marked closed hyperbolic surface of genus two,

```text
Gamma = <a1,b1,a2,b2 | [a1,b1][a2,b2]=1>,
```

and for `N>=1` set

```text
H_N = ker(Gamma -> H_1(Sigma;Z/NZ)).
```

The executed nested schedule is `N=n!`, `n=1,...,8`.  Unlike the Round-5
intersection with the residual cores, this pure homology tower is not
residual: its intersection is `[Gamma,Gamma]`.  That distinction is part of
the object definition, not a limitation hidden after the result.

The owner panel consists of the three Round-5 primitive-content-one classes
`a1`, `a1*b1`, and `a1*a2*b2`.

## Theorem 1 — exact order, component count, and lifted period

`[PROVED]` For every panel owner `g` and modulus `N`:

1. the deck group is `(Z/NZ)^4` and the cover degree is `N^4`;
2. the image of `g` has exact order `N`;
3. the full preimage of its base closed geodesic has exactly `N^3`
   primitive components; and
4. every component has physical period `N ell(g)`.

### Proof

The abelianization of the marked surface group is `Z^4`, so reduction modulo
`N` is onto `(Z/NZ)^4`.  A content-one integral vector has additive order
exactly `N` modulo `N`: Bezout gives an integral linear combination of its
coordinates equal to one, so `k v=0 mod N` forces `N|k`.

The lift of the base loop through a deck point follows the orbit of translation
by the image of `g`.  Each orbit has `N` deck points; hence the `N^4` points
split into `N^4/N=N^3` cycles.  Because `g` is primitive and
`H_N intersect <g>=<g^N>`, each cycle is a primitive lifted geodesic of length
`N ell(g)`: indeed, the centralizer of a nontrivial element in a torsion-free
closed hyperbolic surface group is cyclic.  Thus if `g^N=h^q` with `h in H_N`
and `q>=2`, the unique-root property puts `h=g^r`; then `rq=N`, whereas the
displayed intersection forces `N|r`, a contradiction.  QED.

## Theorem 2 — the four renormalization quadrants

Write `x_g=exp(-s ell(g))`.  Compare two clock choices:

```text
physical:   T_N=N ell(g),
rescaled:   T_N^ren=T_N/N=ell(g),
```

and two multiplicity choices:

```text
raw:             keep all N^3 lift factors,
geometric mean:  log Z^ren=(1/N^3) log Z_panel.
```

`[PROVED]` The four owner factors are exactly

| quadrant | clock | multiplicity | factor | fixed-prefix behavior |
|---|---|---|---|---|
| `Q00` | physical | raw | `(1-x_g^N)^(-N^3)` | coefficientwise to `1` |
| `Q10` | rescaled | raw | `(1-x_g)^(-N^3)` | coefficient of `x_g` is `N^3` |
| `Q01` | physical | geometric mean | `(1-x_g^N)^(-1)` | coefficientwise to `1` |
| `Q11` | rescaled | geometric mean | `(1-x_g)^(-1)` | exact base factor at every level |

Thus time rescaling alone fails through divergent lift multiplicity, while
multiplicity normalization alone fails through support escape.  Applying both
interventions is jointly sufficient and recovers the base finite-owner factor
exactly, not merely asymptotically.

### Proof

Theorem 1 supplies `N^3` identical lifted factors.  Under physical time their
monomial is `x_g^N`; under the declared `1/N` clock it is `x_g`.  Keeping the
multiplicity raises the factor to `N^3`; taking the declared formal
geometric mean divides its logarithm by `N^3`.  This gives the four displayed
formulas.

For the two raw-clock rows, the first nonconstant degree is `N`, so every fixed
coefficient prefix is eventually constant one.  For `Q10`, the coefficient of
`x_g` is `N^3` and diverges.  `Q11` is visibly the base factor at every level.
QED.

## Exact coefficient replay

The builder emits:

- 96 owner/level/quadrant rows (`3*8*4`); and
- 1,248 exact coefficient rows through degree 12 (`3*8*4*13`).

For a general row `(1-x^m)^(-k)`, it uses the exact coefficient law

```text
[x^d](1-x^m)^(-k) = 0                         if m does not divide d,
                     binom(k+d/m-1,d/m)       if m divides d.
```

The replay verifies the formal series and serialization.  The theorem follows
from the cover calculation, not from eight finite levels.

## Scientific consequence

Round 7 proved that fixed-owner factors disappear under the unchanged clock.
Round 8 shows precisely what a collective rescue costs: **both** a new clock
and a new multiplicity normalization.  It also proves that neither change
alone is enough.

The positive `Q11` identity is not arithmetic evidence.  It holds for every
marked genus-two hyperbolic metric and for any finite panel of primitive
content-one homology owners.  It therefore serves as a proves-too-much
calibrator for future tower limits.

## Route-A boundary

The newly registered tuple is

```text
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)
overall = ROUTE_A_REJECTED.
```

`A1_PASS_ANALYTIC` is scoped to the exact finite-panel owner/lift ledger.  No
full primitive census, full-flow dynamical zeta, target divisor, analytic
continuation, or natural quantization is defined.  The original Round-7
same-owner candidate remains independently `ROUTE_A_REJECTED`, and Route B
remains closed.

## Disclosure

The content-one owner/primitivity inputs are source-locked to the Round-5
artifact.  The new cover calculation and four-quadrant theorem are proved in
this note.  AI-assisted research and code generation were used; exact machine
claims are bound to the freeze, two-build replay, tests, validation, and
receipt.
