# Route-A dynamics-diversification batch plan: C144--C148

Status: **complete; five source-locked paper packages released and audited**.

Date: 2026-08-25

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round deliberately moves between five different dynamical categories.
No orbit, clock, determinant, or Route-A coordinate is transferred between
the candidates.  Finite ledgers are implementation sentinels only; every
all-period statement requires its own proof.

## Frozen sequence and required progress

1. **C144 -- Thue--Morse periodic-orbit vacuum.**  Freeze the primitive
   constant-length substitution `0 -> 01`, `1 -> 10` and its two-sided
   substitution subshift.  Prove that the subshift is nonempty and recurrent
   but has no shift-periodic point.  Its Artin--Mazur fixed-point counts are
   therefore identically zero and its periodic-orbit zeta is one.  Cyclic
   finite substitution words are retained only as an approximant control and
   must not be promoted to genuine subshift orbits.
2. **C145 -- Rule-90 two-clock periodic geometry.**  On the cyclic ring of
   length `L`, identify Rule 90 with multiplication by `x+x^(-1)` over
   `F_2[x,x^(-1)]/(x^L-1)`.  Prove for every `L,n>=1` that

   ```text
   #Fix(F_L^n)=2^deg(gcd(x^L-1,(x+x^(-1))^n-1)),
   ```

   with the Laurent expression cleared canonically.  Recover exact temporal
   primitive counts at fixed `L`, and exhibit bounded-search witnesses showing
   that area-only or single-fixed-count aggregation destroys the intrinsic
   space--time information.
3. **C146 -- Heisenberg nilmanifold clean fixed sets.**  Freeze the standard
   integer Heisenberg nilmanifold and the automorphism induced horizontally by
   `[[2,1],[1,1]]`.  Prove that the central direction is fixed, so every
   iterate has at least one clean fixed circle rather than an entirely
   isolated fixed set.  The ordinary isolated-orbit stability denominator
   and Lefschetz number vanish at every period.  The horizontal toral
   automorphism has exactly `abs(det(A^n-I))` isolated fixed points and is the
   matched control.  An explicit period-two class must refute the tempting
   but false lift of every horizontal fixed class to a central circle.
4. **C147 -- rectangular-billiard primitive families.**  Unfold the unit
   square billiard and classify primitive positive directions `(m,n)` by
   `gcd(m,n)=1` with length `2 sqrt(m^2+n^2)`.  Prove that each direction
   carries a continuous translation family and a family-tangent unit return
   multiplier, so an isolated Gutzwiller denominator is singular.  Retain the
   exact direction/family ledger and a minimal distinct-direction length
   collision, while keeping the natural Laplacian quantization separate from
   any target-spectrum claim.
5. **C148 -- open Walsh quantum baker.**  On
   `(C^3)^(tensor k)`, freeze the cyclic tensor shift with one-qutrit
   contraction `A=F_3^* diag(1,0,1)`.  Prove contraction, the one-step rank
   `2*3^(k-1)`, the trapped `k`-step rank `2^k`,
   `B_k^k=A^(tensor k)`, the all-time tensor-cycle trace formula, and the
   resulting exact secular determinant and signed primitive expansion.  The
   closed projector control must restore unitarity; the open map remains only
   a finite source-derived scattering subgate.

## Uniform artifact contract

Each package must contain 27 manifested payloads plus one self-excluded
manifest: source audit, research question, theorem package, experiment and
paper plans, narrative report, two-round internal improvement log,
deterministic producer, producer-independent checker, separate symbolic
reconstruction, byte replay, semantic mutation suite, results/test/hostile
reports, Route-A YAML, LaTeX source, three preserved snapshots, final PDF,
compile report, exact evidence, and release ledger.

Final release additionally requires isolated fixed-date double PDF builds,
embedded fonts, no layout/reference/citation warnings, rendered-page visual
inspection, exact manifest disk closure, and no build caches.  Internal
review is reported as internal review; unavailable external model transport
must never be simulated.

## Strict boundary

The final strict tuples are:

```text
C144 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
C145 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C146 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
C147 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C148 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

No paper contains a frozen target divisor, target zero census, target
functional equation, target counting law, arithmetic local factor, Euler
factor, root number, automorphy statement, or Hilbert--Polya operator.
`route_b_invocation_allowed=false` for all five.

## Completion record

All five packages satisfy the 27-payload contract and contain a self-excluded
manifest, for 28 physical release files per package.  The final papers are
two pages each.  Independent reconstruction totals are 181,474 checker
assertions and 1,576 symbolic checks; all 188 hostile cases are rejected.
Fixed-epoch double builds are byte-identical to the released PDFs, all fonts
are embedded, and the ten rendered pages pass visual inspection.

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C144 | `418d3f6f384adb06b8dda10e24a8d0a8254d3a89d6a840a183374e8231e0578d` | `7d226462a14e84e0f5ff36a84b96da659960b477e8fdaba1f7982d6c7e77754f` | `9508aa73d703350622484a9802e6ed0e9fb40df98d5b4e4544d73f22300c0109` |
| C145 | `635a952a8cb5d3b4fcae3eab69e5553bb1165e43c95dd8a345d3fbc93591d246` | `fdc23c119b84e093c0e8c26bf63d70da0cfd23f12a44f64a6d9945146cf9024f` | `0fdbe0b553590ce0e9a46e2a68bfba9c186d032d3a7f8404b797a51fe4881089` |
| C146 | `e6789ac7a8525d81d2cc0802896f83c57602c45e00ad8a89fef81a536228de72` | `8ee75e2e8e293cf3c65856d8c03056dcb52762d92629439170cdaa79e10c80c3` | `99353b6b71d919907049eade88433e869eef76026f7f3c3ddfabb8da6128364f` |
| C147 | `2df27380610e7e7f3c2460563d41213042e95b97b44ee8bacb1dac3c95f771ea` | `d3468d9cb6c2b35fa4034042c388ea1e8e2f6c36e76d9cc5e0b744c073895a1b` | `6e8195d2350647f96bf43556c481af46a88c735f78dabdcbd8bd81f99e1bd570` |
| C148 | `75e93a1253a7d2d51211ea50676b48f4382cd70b050da4db4df0d9837be92787` | `7d74eb952880972d2d73a87e32eb69bbcdd65f430c19aa1ab168bc1e3548dd89` | `fe73e089e5f2c6f796d74ca999de37a155095d0d3af3b4888c508f3452f7c4a4` |

The exact theorem, cross-review, failure-mode, and remaining-boundary audit is
recorded in `BATCH_REVIEW_C144_C148.md`.
