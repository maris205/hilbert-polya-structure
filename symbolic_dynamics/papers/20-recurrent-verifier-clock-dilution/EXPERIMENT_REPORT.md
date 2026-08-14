# Experiment Report — SD-C22 Recurrent Verifier Clock Dilution

## Outcome

The exact suite verifies a recurrent prime-verification ledger and proves that
it cannot support the frozen whole-operator Fredholm determinant. With the
contracted terminal rule
\(T_{p,\lfloor\sqrt p\rfloor+1}\to I_p\), the fully expanded quotient-search
path has exactly

\[
\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}
\left\lceil\frac p d\right\rceil
=\frac12p\log p+(\gamma-1)p+O(\sqrt p).
\]

For any nonnegative roof allocation of exact total \(\log p\), at least one
cycle edge has roof at most \(\log p/\ell(p)\to0\). The natural whole
adjacency therefore has essential norm one, is noncompact, and lies in no
finite Schatten class. Its ordinary Fredholm determinant does not exist.

Frozen verdict:

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_PASS_ANALYTIC,
     A2_FAIL,
     A3_FAIL,
     A4_FAIL)

    ROUTE_A_REJECTED
    CLOCK_DILUTION_OBSTRUCTION
    ESSENTIAL_UNIT_CIRCLE
    POINCARE_COLLAPSE
    SELECTOR_TAUTOLOGICAL / PROVES_TOO_MUCH
    ROUTE_B_LOCKED

No target-zero data, root fitting, Route-B object, or cross-family experiment
was used.

## Endpoint and no-oracle certificates

The scientific source materializes input, divisor, quotient-search, and
cemetery states. The transition routine uses multiplication, successor, and
order comparisons; an independent prime sieve appears only in sealed
validation. The source audit finds no hidden factor-existence macro, real
quotient states occur through the frozen cutoff, and composite paths enter a
one-way cemetery rather than a recurrent reject loop.

The endpoint convention is fixed and executable: the old accept vertex is
contracted, so the final trial state returns directly to the input. A
different convention retaining a separate accept vertex would add one edge;
it is not mixed into these artifacts.

Primary artifact: results/source_oracle_certificate.json.

## Exact cycle census

Formula and independent local-state traversal agree for all 564 primes through
4096. Selected rows are:

| \(p\) | \(\ell(p)\) | \(\ell(p)/\log p\) | optimal max edge weight, \(\sigma=2\) |
|---:|---:|---:|---:|
| 5 | 5 | 3.10667 | 0.525306 |
| 101 | 202 | 43.7692 | 0.955334 |
| 1009 | 3075 | 444.575 | 0.995511 |
| 4093 | 15293 | 1838.76 | 0.998913 |

The displayed weight is
\(\exp(-2\log p/\ell(p))\), the smallest possible maximum edge weight among
all nonnegative exact-clock allocations. Its approach to one is a finite
witness for the theorem, not the proof itself.

## Whole-operator obstruction

Every accepted block satisfies

\[
B_{p,s}^{\ell(p)}=p^{-s}I,
\qquad
|\lambda|=p^{-\operatorname{Re}s/\ell(p)}.
\]

Thus block eigenvalue radii approach one. Their phases become dense on the
unit circle, giving singular Weyl sequences on disjoint blocks. For every
\(\operatorname{Re}s>0\), the unit circle belongs to the essential
approximate spectrum and \(I-zL_s\) is non-Fredholm for \(|z|=1\).

The proof is allocation-independent. Uniform allocation is the most
compactness-friendly case; a terminal-lumped allocation makes all other edge
weights exactly one.

## Orbit-product / first-return firewall

The raw graph-step block factor is

\[
1-z^{\ell(p)}p^{-s}.
\]

For primes through 31 at \(s=2\), exact rational arithmetic confirms:

- at \(z=1\), the raw product equals the induced prime-loop product;
- at \(z=1/3\), the raw and ordinary return-step products are different;
- the first four nonzero power traces of every small block have the exact
  value \(\ell(p)p^{-2k}\).

The \(z=1\) identity
\(\prod_p(1-p^{-s})=\zeta(s)^{-1}\) is a normally convergent combinatorial
orbit product on \(\operatorname{Re}s>1\). It is not the Fredholm determinant
of the noncompact whole operator. First return gives
\(R_se_p=p^{-s}e_p\), which is exactly the Paper 04 diagonal core and records
a contraction of the verification clock.

## Source-clock distortion

Redirecting the Paper 19 terminal edge while retaining its summable
edge-by-edge roofs preserves the trace-class majorant on
\(\operatorname{Re}s>1\), but every verifier edge then has roof at least
\(\log p\). The cycle total is at least \(\ell(p)\log p\), not \(\log p\).
At \(p=4093\), the measured source total divided by \(\log p\) is about
28780.8.

Hence:

    exact total roof log p  => noncompact whole adjacency;
    source-summable edge roofs => trace class but wrong orbit clock.

## Universal-decider controls

Square, power-of-two, Fibonacci, and seeded-hash predicates were padded by the
same uniformly prescribed \(n^2+2\) runtime. Their cycle products remain
exact by construction and their most favorable maximum edge weights all
exceed 0.999997 at cutoff 4096. The failure is therefore presentation/runtime
driven rather than prime-selective.

## Verification status

- twelve exact tests: passed;
- contracted formula versus explicit path traversal: exact through 4096;
- explicit Q-state/no-oracle audit: passed;
- 564-prime cycle census: exact;
- exact rational marker firewall: passed;
- exact rational power traces: passed;
- four padded total-decider controls: passed;
- target-zero fields: not applicable and unused;
- Route B invocation: false.

The deterministic orchestrator regenerates code-derived artifacts, analysis,
tests, schema/integrity audit, and the SHA-256 ledger twice and requires
byte-identical ledger bytes.

## Next smallest in-family obligation

Do not build another vertex-disjoint verifier compiler. The next candidate
must begin with an overlapping genuinely recurrent semiring-local grammar and
prove a positive primitive-cycle separation theorem before choosing a roof,
character, determinant, or target-zero comparison. Geometric, scattering,
semifinite, or anisotropic repairs remain ROUND2_CLUE only.
