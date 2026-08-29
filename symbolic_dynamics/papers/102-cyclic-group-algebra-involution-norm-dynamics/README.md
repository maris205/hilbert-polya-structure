# P102 — Involutive norm dynamics in split cyclic group algebras

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

For a prime power `q` and `n | (q-1)`, this note studies the nonlinear finite
map

```text
T(a) = a a*
```

on the whole split cyclic group algebra `A = F_q[C_n]`, where `*` is induced
by inversion in `C_n`.  The phase space includes zero divisors; it is not a
unit-group-only calculation and not a modular (`char(F_q) | n`) group-algebra
claim.

The frozen theorem package is:

1. Fourier inversion orbits give scalar blocks `z -> z^2` and paired blocks
   `(u,v) -> (uv,uv)`, while the coordinate-free identity is
   `T^k(a)=(aa*)^(2^(k-1))` for `k>=1`;
2. with `s=gcd(n,2)` and `o=(n+s)/2`, every fixed count is
   `(1+gcd(2^k-1,q-1))^o`;
3. if `q-1=2^alpha m` with `m` odd, the recurrent core has size `(m+1)^o`
   and the exact maximum transient depth is
   `alpha + 1_{n>s}`;
4. Möbius inversion gives all least-period points and cycles, hence a finite
   Artin–Mazur zeta product supported on divisors of `ord_m(2)`; and
5. phase size, the complete fixed sequence, and maximum depth recover the
   ordered pair `(q,n)`, with the `o=2` branch proved separately.

Run the exact control with:

```bash
python3 code/verify_involution_norm.py
```

The deterministic output is frozen in
[`code/verification_output.txt`](code/verification_output.txt) and interpreted
in [`CONTROL_RESULTS.md`](CONTROL_RESULTS.md).  The proof/control mapping is in
[`CLAIMS_EVIDENCE.md`](CLAIMS_EVIDENCE.md), and the four-stage PDF recipe is in
[`BUILD.md`](BUILD.md).

Classical Fourier decomposition, group-algebra involutions and unit theory,
scalar power-map functional graphs, and Artin–Mazur zeta bookkeeping are
explicitly subtracted.  The residual full-algebra temporal package passed only
a bounded owner search.  Public release, submission, author contact, absolute
novelty language, and priority claims remain **HOLD**.  Independent hostile
reviews A and B, their consolidated ledger, final mechanical QA, and the
verified SHA-256 seal are retained in this package.

Internal collision note: P86 uses the same elementary multiplication
primitive inside a spatial adjacent-product factor of an iid process.  P102
instead uses it as one finite Fourier block followed by deterministic
squaring; its claims concern temporal census and transient depth, not support
entropy or prediction memory.
