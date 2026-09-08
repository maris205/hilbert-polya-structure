# New bounded exact-screen results

Date: 2026-09-07 UTC. Script: [exact_screen.py](exact_screen.py).
All arithmetic is exact Python integer/finite-field polynomial arithmetic;
no external CAS, predecessor test, GPU or downloaded dataset is used.
The script writes stdout only and is not an all-parameter proof.

## Actual executions

1. Initial script (numeric quartic jets and twisted Hénon checks):
   python -B henon_dynamics/research_c419_c423/positive_characteristic/exact_screen.py.
   Completed with exit 0. The output contained the twelve valuations and
   two Hénon coefficient cases below.
2. Added symbolic-$b$ calculation and an explicit single-axis truncation
   option. Called that new function alone through Python import:
   completed with exit 0 in the tool-reported 0.386 seconds.
3. An attempted /usr/bin/time wrapper failed before Python execution,
   exit 127, because that executable is absent. It produced no mathematical
   result and changed no file.
4. Final complete script, including the changed truncation implementation:

       timeout 90s python -B -c 'import runpy,time; start=time.monotonic(); runpy.run_path("henon_dynamics/research_c419_c423/positive_characteristic/exact_screen.py",run_name="__main__"); print("elapsed_seconds="+format(time.monotonic()-start,".3f"))'

   Completed with **exit 0**, reporting **34.940 seconds** elapsed.
   The 90-second cap did not fire. The full output reproduced the numerical
   rows and Hénon identities and included both new symbolic coefficients.
   This rerun followed an implementation change, not a repeat of an
   unchanged accepted predecessor merely to obtain PASS.

## PC-F: exact first $p$-iterate valuations

The script composes the same map both on the left and on the right and
requires the resulting truncated polynomials to agree. The first nonzero
coefficient is below the cutoff in every row, so each displayed $i_1$ is
an exact valuation.

| $p$ | $b$ | Modulus | $i_1$ | Coefficient of $z^{i_1+1}$ |
|---|---:|---|---:|---:|
| 5 | 0 | $z^{64}$ | 11 | 3 |
| 5 | 1 | $z^{64}$ | 11 | 1 |
| 5 | 2 | $z^{64}$ | 11 | 1 |
| 5 | 3 | $z^{64}$ | 11 | 2 |
| 5 | 4 | $z^{64}$ | 11 | 3 |
| 7 | 0 | $z^{128}$ | 15 | 4 |
| 7 | 1 | $z^{128}$ | 15 | 1 |
| 7 | 2 | $z^{128}$ | 15 | 1 |
| 7 | 3 | $z^{128}$ | 15 | 3 |
| 7 | 4 | $z^{128}$ | 15 | 2 |
| 7 | 5 | $z^{128}$ | 15 | 3 |
| 7 | 6 | $z^{128}$ | 22 | 4 |

The symbolic run keeps $b$ indeterminate, truncating in $z$ alone:

| Characteristic | Computation modulus | First possible nonzero term |
|---|---|---|
| 5 | $z^{18}$ | $(3+4b^2+4b^3)z^{12}$ |
| 7 | $z^{24}$ | $(4+2b+6b^2+2b^3+b^4)z^{16}$ |

At roots of those coefficient polynomials the displayed term vanishes.
The script labels this as an exceptional locus, not as an exact next jump
or an identity iterate. In characteristic 5 the root-free cubic over the
prime field acquires roots over $\mathbb F_{125}$, which is part of the
frozen parameter family. This is why the five prime-field rows alone are
insufficient. No larger-prime or complete extension-field census was run.

## PC-H: new semilinear and native-clock checks

The exact field is $\mathbb F_9=\mathbb F_3[\eta]/(\eta^2+1)$.
Encoding $r+3s$ means $r+s\eta$, not an integer residue modulo 9.
Cases $(a,c)=(3,4)$ and $(1,3)$ therefore mean
$(\eta,1+\eta)$ and $(1,\eta)$; each is genuinely outside the all-base-field
coefficient stratum.

For each case, the script checks:

- $TU=UT$ on a mixed-coefficient polynomial and $\delta(\eta)=0$.
- The untwisted coefficient-linear substitute fails the intended leading
  cancellation on $\eta y$, exposing why the coefficient action matters.
- Exact fixed-polynomial leading monomials and the characteristic-three
  identity $(T^3-U^3)y=\delta^3y$.
- The equivalence between the actual $S^2$ fixed equation and the correct
  twisted-product equation on all 81 $\mathbb F_9$-points.

The polynomial results, identical for both coefficient pairs, are:

| Native $n$ | First leading monomial | Second leading monomial | Quotient length from coprime leading monomials |
|---:|---|---|---:|
| 1 | $x^3$ | $y^2$ | 6 |
| 2 | $x^9$ | $y^6$ | 54 |
| 3 | $x^{27}$ | $y^{14}$ | 378 |

The 81-point checks are an independent native-clock sanity check, **not**
counts over the algebraic closure. Interpreting the polynomial quotient
length as ordinary geometric count requires the Jacobian argument in
[SEMILINEAR_REDUCTION.md](SEMILINEAR_REDUCTION.md). The finite checks do not
prove the all-$n$ reduction or its all-coefficient hypotheses.

## Deliberate non-results

No PC-D calculation was run: its rejection is the exact invariant-factor
kernel collision. PC-F's full higher ramification remains unresolved.
PC-H's arithmetic carrier provides no new target bridge, and its recovered
count law is the owned C404 law. These checks support screening decisions,
not a manuscript, formal evaluation, sealed release or new paper number.
