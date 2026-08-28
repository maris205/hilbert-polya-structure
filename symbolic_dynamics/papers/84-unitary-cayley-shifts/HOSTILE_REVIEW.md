# Hostile review — P84

**Verdict: GO** for the theorem-bearing internal paper after the corrections
listed below.  The standing prohibition on public posting or priority claims
in `README.md` is unchanged.

Audit date: 2026-08-28 UTC.

## Formula-by-formula audit

- Fourier diagonalization gives the Ramanujan eigenvalue
  `mu(d)*phi(n)/phi(d)` for `d=n/gcd(n,r)`.  The residues with a fixed `d`
  are exactly `r=(n/d)s` with `s` reduced modulo `d`, hence the multiplicity
  is exactly `phi(d)`, including multiplicity one at `d=1`.
- Summing eigenvalue powers gives the displayed fixed-point formula, and the
  determinant product gives the zeta function.  The endpoints
  `P_1=0` and `P_2=n*phi(n)` agree with direct walk counting.
- The graph is irreducible because `+1` generates the cyclic group.  A
  reversible edge gives a two-cycle; for odd `n`, the `n` successive `+1`
  steps give an odd cycle, whereas for even `n` every unit step changes
  parity.  Thus the periods are exactly one and two, respectively.
- Under the Parry law, `K=A/phi(n)` is self-adjoint in uniform `L^2`.  For
  odd `n`, the largest nonconstant eigenvalue modulus is
  `1/(p_min-1)`: among squarefree divisors `d>1`, `phi(d)` is minimized by
  the least prime divisor.  A real part of the corresponding Fourier
  eigenvector attains equality in the correlation bound for every `k`.
- The pair `(log phi(n), n*phi(n))` recovers `n`.  Equality of zeta functions
  also recovers entropy because
  `limsup_k P_k(n)^(1/k)=phi(n)`, including the even, period-two case where
  odd fixed counts vanish.

## Corrections applied

1. Added the one-line proof of the Ramanujan multiplicity `phi(d)`.
2. Specified real mean-zero vertex observables, the uniform `L^2` norm, and
   normalized real eigenfunctions attaining the sharp bound.
3. Replaced an unqualified periodic-growth sentence by the precise `limsup`
   statement needed for period two.
4. Strengthened the control with direct multiplicity assertions and exact
   rational arithmetic for the sharp rate.
5. Restored one missing backslash before `\qquad` in the endpoint display.

## Reproducibility and release checks

- Deterministic control: **PASS — 19,901 exact assertions**.
- The control directly checks matrices for `2<=n<=30`, traces through power
  10, every divisor multiplicity in that range, grouped characteristic
  polynomials through `n=14`, the period witnesses, exact sharp rates, and
  the rigidity registry.
- Four-stage build (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`): all exits
  zero.
- Final PDF: **4 A4 pages, 306,993 bytes**.
- Log scan: no undefined references/citations, LaTeX errors, overfull or
  underfull boxes, fatal errors, or rerun requests.
- Fonts: **24/24 embedded, subsetted, and Unicode-mapped**.
- Visual inspection: all four pages clean; no clipping, collision, or stray
  `qquad` text.

## Surviving scope boundaries

The family is restricted to `n>=2`.  The sharp rate concerns vertex
observables under the Parry measure and is stated only for odd `n`; ordinary
mixing fails for even `n`.  Rigidity is only inside the unitary-Cayley-shift
family.  The Ramanujan spectrum, finite-type determinant identity, and Parry
construction remain explicitly cited prior results; no priority claim is
made.
