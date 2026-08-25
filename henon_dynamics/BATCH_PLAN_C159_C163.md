# Route-A theorem-progress batch plan: C159--C163

Status: **complete; five source-locked paper packages released**.

Date: 2026-08-25

Source commit: `63f75cf476711de93e6096ef74ac16969e1127d0`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round applies a theorem-first gate.  Every paper must add an
all-parameter identity, asymptotic law, classification, or obstruction that
is strictly stronger than its C154--C158 predecessor.  A finite ledger is a
sentinel and cannot by itself satisfy the gate.  When the source model does
not support the proposed theorem, the paper changes dynamical system and
records the pivot instead of presenting the failed claim as progress.

## Frozen sequence and required progress

1. **C159 -- a recurrent Thue--Morse gap-renewal shift.**  The initially
   considered clock-decorated Sturmian vacuum was rejected because its lack
   of periodic points was too close to C144.  Instead let
   `S={s>=0:t_s=1}` for the Thue--Morse sequence and use the uniquely
   decipherable renewal code `C={10^s:s in S}`.  Prove that the resulting
   S-gap shift is topologically mixing, has dense nontrivial periodic points,
   and supports recurrent dense orbits.  With

   ```text
   F(z)=sum_(s in S) z^(s+1)=zT(z),
   P(z)=product_(j>=0)(1-z^(2^j))=1/(1-z)-2T(z),
   ```

   prove the exact Artin--Mazur identity

   ```text
   zeta_X(z)=1/((1-z)(1-F(z)))
            =2/(2-3z+z(1-z)P(z)).
   ```

   Establish the corresponding meromorphic natural-boundary obstruction at
   the unit circle.  This replaces C154's isolated one-pass interface by a
   genuinely recurrent, mixing symbolic interaction with a nontrivial
   periodic ledger.
2. **C160 -- exact maximal-subgroup Rule-90 period loss.**  Retain the
   Mersenne periodic image `V=im(x+x^(-1))` from C155.  For every
   `L=2^r-1`, identify the non-full-period set exactly as the union of the
   maximal proper-clock fixed subspaces indexed by the distinct prime
   divisors of `L`.  Apply inclusion--exclusion and the polynomial-gcd fixed
   dimensions to obtain an exact all-`L` short-period formula, rather than
   the C155 union bound.  On every Mersenne-prime circumference `L>3`, prove

   ```text
   period support={1,L},
   # exact-period-L states=2^(L-1)-1,
   Pr(period<L)=2^(-(L-1)),
   # primitive L-cycles=(2^(L-1)-1)/L.
   ```

   This is a theorem for every parameter satisfying the stated primality
   hypothesis; it makes no claim that infinitely many such parameters exist.
3. **C161 -- pivot to quadratic cyclic-rotation amplitudes.**  The proposed
   all-iterate evaluation of the C156 Heisenberg quadratic sums was stopped:
   unresolved degenerate and 2-adic local types prevent a complete formula.
   The replacement system is the natural family of finite cyclic rotations
   with a quadratic observable.  Reduce every `n`-step Birkhoff exponential
   sum to one explicitly parameterized quadratic Gauss sum, then prove the
   complete gcd/Jacobi evaluation including vanishing cases and the exact
   prime-modulus discriminant law for zero Birkhoff level sets.  The failed
   Heisenberg extension remains an open obligation, not a claimed result.
4. **C162 -- shell-resolved Abel boundary normalization.**  Retain the
   genuine square-billiard Dirichlet Abel half-wave trace from C157.  For
   every represented integer `N>=1`, approach the clean-family boundary at
   `s=-2i sqrt(N)` from the right and prove

   ```text
   lim_(eps->0+) eps^(3/2) W_D(eps-2i sqrt(N))
     =exp(i*pi/4) r_2(N)/(8*pi*N^(1/4)).
   ```

   Prove that analytic shells vanish under this normalization and that a
   coincident simple boundary-subtraction pole, when `N` is a square, also
   vanishes.  Thus the normalized coefficient counts the entire coincident
   clean shell rather than an isolated orbit or a numerical branch sample.
5. **C163 -- phase equidistribution for the open Walsh full cycle.**  For
   the two normalized nonzero one-site phases `u_+` and `u_-`, put
   `r=u_+/u_-`.  Derive

   ```text
   2*cos(arg r)=(sqrt(3)-sqrt(111))/6,
   3x^4-19x^2+27=0.
   ```

   Prove that this value is not an algebraic integer, so `r` is not a root of
   unity.  For the algebraic-multiplicity-weighted full-cycle phase measure,
   prove the exact Fourier identity

   ```text
   mu_hat_k(m)=u_-^(mk)*((1+r^m)/2)^k
   ```

   and hence weak convergence to Haar measure on the unit circle, with
   exponential decay for every fixed nonzero Fourier mode.  This is the
   phase theorem explicitly absent from C158; it is not a self-adjoint or
   target spectral limit.

## Uniform artifact and integrity contract

Each paper must release the same closed package class used in C154--C158:
source audit, research question, proof package, experiment and paper plans,
narrative report, two-round internal improvement record, deterministic
producer, producer-independent checker, separate symbolic reconstruction,
canonical replay, hostile semantic mutation suite, results/test/hostile
reports, complete Route-A YAML, bilingual LaTeX paper, three preserved PDF
snapshots, compile report, exact evidence, and a self-excluding release
manifest.

ARS Stage 2.5 and Stage 4.5 each apply all seven failure modes.  The final
release requires exact evidence replay, manifest disk closure, fixed-epoch
double PDF builds, embedded fonts, warning-free LaTeX logs, rendered-page
inspection, and absence of build/cache debris.  Internal review is described
as internal review only; no external reviewer, independent error process,
acceptance score, unperformed computation, or interval certificate may be
invented.

## Frozen claim boundary

No paper may read a target zero table or prime table, freeze a target divisor
or counting law, introduce arithmetic local data, claim Euler factors, root
numbers, automorphy, a Hilbert--Polya operator, or combine coordinates across
the five source systems.  Route-A labels may be weakened by evidence but not
promoted from finite tables.  Every evaluation must retain
`route_b_invocation_allowed=false`.

## Release outcome

All five hard gates passed after the recorded C159 and C161 model pivots.
Each package contains a two-page bilingual paper, three content-distinct PDF
stages, exact evidence, independent checker, SymPy reconstruction, byte
replay, hostile mutation suite, Route-A evaluation, and a closed 27-file
payload manifest.  The batch-level audit records 486,872 checker assertions,
16,231 symbolic checks, 242/242 hostile rejections, fixed-epoch byte-identical
double builds, embedded fonts, ten visually inspected A4 pages, and 140 total
physical release files.  Exact evidence/PDF/manifest hashes and repair details
are frozen in `BATCH_REVIEW_C159_C163.md`.
