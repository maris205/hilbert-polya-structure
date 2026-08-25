# Route-A dynamics-refinement batch plan: C149--C153

Status: **complete; five source-locked paper packages released and audited**.

Date: 2026-08-25

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round advances five distinct dynamical subtypes inherited from the
C144--C148 boundary audit.  No orbit, clock, determinant, regularization, or
Route-A coordinate is transferred between candidates.  Finite exact ledgers
are implementation sentinels only; every all-parameter statement requires an
independent proof.

## Frozen sequence and required progress

1. **C149 -- Thue--Morse with a finite periodic skeleton.**  Form the compact
   disjoint union of the aperiodic minimal Thue--Morse subshift and four tagged
   shift cycles of lengths `1,2,3,5`.  Prove at every period that

   ```text
   #Fix(sigma^n)=sum_(ell in {1,2,3,5}, ell|n) ell,
   zeta_AM(z)=product_(ell in {1,2,3,5}) (1-z^ell)^(-1).
   ```

   Recover the exact primitive skeleton and prove that adding any nonempty
   finite skeleton necessarily destroys minimality.  The result is a
   controlled nonempty periodic layer, not a target-facing upgrade.
2. **C150 -- Mersenne scaling family for Rule 90.**  On cyclic rings of length
   `L_r=2^r-1`, prove that the Rule-90 multiplier `a=x+x^(-1)` satisfies
   `a^(L_r+1)=a`, has image dimension `L_r-1`, and restricts to a permutation
   of order dividing `L_r` on that image.  Thus every state enters the image
   after one tick, exactly half of all states are periodic, and every cycle
   length divides `L_r`.  Recover all fixed/exact-period/cycle counts by
   polynomial gcd and Mobius inversion.  The matched power-of-two family must
   be proved nilpotent with only the zero periodic state.
3. **C151 -- character-resolved Heisenberg fibre rotations.**  For the frozen
   Heisenberg automorphism from C146, parameterize horizontal fixed classes by
   `Z^2/(A^n-I)Z^2`.  If `m=(A^n-I)v`, prove that the central fibre rotation is

   ```text
   rho_n(v)=sum_(j=0)^(n-1) q(A^j v)-m_1 v_2  (mod 1),
   ```

   and that a horizontal class lifts to a clean fixed circle exactly when
   `rho_n(v)=0`.  Give an all-iterate finite root-of-unity projector for the
   component count and an independently reconstructed exact rotation
   histogram through a declared cutoff.  No unproved Lucas-pattern
   extrapolation is allowed.
4. **C152 -- primitive billiard-family heat transform.**  For positive
   coprime square-billiard directions and length
   `L_(m,n)=2 sqrt(m^2+n^2)`, define the convergent source-derived transform

   ```text
   H_prim(t)=sum_(m,n>=1, gcd(m,n)=1) exp(-t L_(m,n)^2),  t>0.
   ```

   Prove its exact Mobius/theta factorization, retain length collisions with
   multiplicity, and derive the small-time law
   `H_prim(t)=3/(8*pi*t)+O(t^(-1/2) log(1/t))`.  This is explicitly a
   primitive-direction heat regularization, not a clean wave trace, an
   isolated stability determinant, or a target spectral identity.
5. **C153 -- growing-k escape for the open Walsh gate.**  For the frozen gate
   `B_k`, prove for every `n,k>=1`

   ```text
   rank(B_k^n)=2^min(n,k) 3^(k-min(n,k)).
   ```

   Deduce the exact macroscopic escape exponent at
   `n=floor(alpha*k)`.  At every fixed period, classify the full set of trace
   subsequential values by the divisors `d|n` through
   `Tr(A^(n/d))^d`, prove that each divisor class occurs infinitely often,
   and prove dimension-normalized fixed-period traces vanish.  This is a
   controlled large-system limit with an explicit gcd obstruction, not a
   self-adjoint or target-matched limit.

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
C149 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
C150 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C151 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
C152 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C153 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

No paper may contain a frozen target divisor, target zero census, target
functional equation, target counting law, arithmetic local factor, Euler
factor, root number, automorphy statement, or Hilbert--Polya operator.
`route_b_invocation_allowed=false` for all five.

## Completion record

All five frozen questions were completed without changing their source
systems or frozen strict tuples.  The release contains five exact
evidence payloads, five independently checked theorem packages, and five
deterministic PDF papers.  Across the batch, the producer-independent
checkers pass 194,934 assertions, the separate SymPy paths pass 1,341 checks,
and all 216 hostile receipts are rejected.  Every package closes an exact
27-payload manifest plus its self-excluded manifest; the six PDF pages are
reproducible from fresh fixed-epoch builds with embedded fonts.

The completed theorem, repair, hash, and failure-mode ledger is recorded in
[`BATCH_REVIEW_C149_C153.md`](BATCH_REVIEW_C149_C153.md).  Route B remains
unauthorized.
