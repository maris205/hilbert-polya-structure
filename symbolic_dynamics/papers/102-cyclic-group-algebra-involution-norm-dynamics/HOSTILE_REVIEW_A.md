# Independent cross-hostile review A — P102

Audit date: 29 August 2026.  This is the second independent mathematical
pass, written after review B froze its repairs.  It is not a novelty
certificate or an authorization to circulate the paper.

## Verdict

**Internal PASS / external HOLD.**  Unresolved CRITICAL: 0.  Unresolved
mathematical MAJOR: 0.  New MINOR requiring source repair: 0.  Review A
independently confirms the two clarifications repaired by review B and finds
the main theorem package correct under the stated split hypothesis
`n | (q-1)`.

## From-scratch block reconstruction

1. **Fourier orientation.**  With
   `hat(a)(j)=sum_r a_r omega^(jr)`, cyclic coefficient reversal gives
   `hat(a*)(j)=hat(a)(-j)`; no inverse-transform normalization enters the
   forward product rule.  Because `n | (q-1)`, the primitive root lies in
   the ground field and `p` does not divide `n`, so the Fourier matrix is
   invertible and the group algebra is `F_q^n` without modular nilpotents.
2. **Block dynamics.**  A self-inverse character satisfies `2j=0 mod n`
   and therefore carries `z -> z^2`.  A nonself inversion orbit carries
   `(u,v) -> (uv,uv)`.  The number of self characters is
   `s=gcd(n,2)` and the number of blocks is `o=(n+s)/2`.  This verifies the
   orientation and exponent `2^(k-1)` in every positive iterate.
3. **Fixed points.**  Fixedness of a paired block under a positive iterate
   first forces `u=v`; both block types then satisfy `z^(2^k)=z`.  Zero is
   one root and the nonzero root count is
   `gcd(2^k-1,q-1)`, giving the claimed `o`th power.  There is no missing
   first-image multiplicity.

## Recurrence, sharp depth, and endpoint attack

For `q-1=2^alpha m`, repeated squaring removes exactly one factor of two
from the multiplicative order.  Hence the scalar recurrent set is
`{0} union mu_m` and its maximum depth is `alpha`.  A periodic paired block
must be diagonal.  The repaired pointwise formula is exact:

```text
self z:                 d_q(z)
pair (u,u):             d_q(u)
pair (u,v), u != v:     1 + d_q(uv)
```

Thus a pair already on the diagonal is not overcharged.  If a nonself pair
exists, `(1,gamma)` with primitive `gamma` attains `alpha+1`; otherwise
`n=s`, so `n` is 1 or 2 and a primitive self coordinate attains `alpha`.
The checks include the easy-to-miss endpoints `q=2,n=1`, even `n=2`, and
characteristic-two fields with `alpha=0` and `n>=3`.

## Period, Möbius, and zeta attack

Squaring is an automorphism of `mu_m` of order `ell=ord_m(2)`; zero is
fixed.  Coordinatewise squaring on the recurrent product therefore has
only periods dividing `ell` (with the declared `m=1, ell=1` convention).
The identities `F_k=sum_(d|k) P_d` and `C_k=P_k/k` reproduce both Möbius
displays.  Multiplying one `(1-z^k)^(-1)` per exact cycle gives the stated
finite zeta product, with the signs and divisor support correct.

## Rigidity attack

The recovery theorem does not silently assume `q` or `n`.  `F_1=2^o` gives
`o`; the maximum fixed-coordinate root count gives the odd part `m`; and
`2o=n+gcd(n,2)` leaves only `2o-1` and `2o-2` (the latter only when
positive).  Depth reconstructs a field candidate after subtracting the
appropriate synchronization indicator.

The exceptional `o=2` branch was checked independently.  If both `n=2` and
`n=3` candidates survived, their fields would obey
`q_2-1=2(q_3-1)` and the common phase size would give `q_2^2=q_3^3`.
Unique factorization yields `q_2=r^3,q_3=r^2`, whence
`(r-1)(r^2-r-1)=0`, impossible for integral `r>=2`.  For `o>=3`, both
candidates have the same field and distinct positive exponents, so phase
size separates them.  The theorem appropriately describes within-family
recovery and does not claim zeta-only classification.

## Repairs from review B confirmed

- The proof now distinguishes diagonal and nondiagonal paired-block depths;
  the theorem value is unchanged and the endpoint attainment is explicit.
- `main.tex`, `README.md`, and `CLAIMS_EVIDENCE.md` now contain the P86
  collision firewall.  P86's adjacent product is a spatial stochastic
  two-block factor; P102's product is one Fourier block of a deterministic
  finite self-map followed by squaring.  The multiplication primitive is
  disclosed and receives no separate contribution credit.

No further source correction was needed in review A.

## Owner and internal-collision boundary

Fourier decomposition, the involution/symmetric-unit setting, scalar power
functional graphs, and Artin--Mazur cycle bookkeeping are all positively
cited and subtracted.  The bounded search found no direct source for the
whole-algebra temporal conjunction, but the map `a -> aa*` is sufficiently
canonical that a specialist direct-owner search remains a **major release
gate**.  Search absence is not novelty evidence.

Beyond P86, P97 also combines squaring language with a sharp absorption
depth, P99 supplies finite cycle/zeta/recovery data in an algebraic state
space, and P87 uses ring multiplication inside a symbolic shift.  Their
phase spaces, maps, invariants, and proofs do not reproduce P102, so these
are low motif collisions rather than theorem collisions.

## Independent control and artifact replay

A fresh run of the coefficient-first verifier reproduced the stored stdout
byte for byte:

```text
cyclic group-algebra involution norm verification: PASS
literal_lanes=9
rigidity_lanes=85
assertions=116278
```

The literal lanes build cyclic convolution and reversal independently of the
Fourier prediction, including explicit `F_4` and `F_16` polynomial bases.
They exhaust the registered functional graphs and compare fixed, recurrent,
depth, and cycle data.  The 85 rigidity lanes are formula-level recovery
falsifiers; they are not represented as an independent proof of the
universal uniqueness argument.

The exact sequence `pdflatex -> bibtex -> pdflatex -> pdflatex` exited zero.
Final log scans found no substantive warning, undefined citation/reference,
multiply-defined label, overfull/underfull box, or error.  The rebuilt PDF
has 6 A4 pages and 328,565 bytes.  `pdffonts` reports 24 entries, all
embedded, subsetted, and Unicode-mapped; `pdftotext -layout` recovered
19,852 bytes.  All six rendered pages were inspected and show no clipping,
collision, malformed formula, or orphaned heading.

## Residual disposition

- Mathematical package: **GO for internal Stage 2 use**.
- Direct-owner risk: **medium-high**, because the involutive norm is a
  canonical classical operation even though the exact temporal package was
  not located.
- External posting, submission, specialist contact, novelty, and priority
  language: **HOLD**.
