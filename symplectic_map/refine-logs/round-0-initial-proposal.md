# Round 0: Initial Proposal State

## Provenance

- Source: `propose-symplectic-map.md`
- Review stage: before focused implementation and confirmatory experiment
- Date recorded: 2026-08-12
- Status: superseded as an actionable Stage-1 plan; retained as the original research
  brief.

This log summarizes the initial proposal rather than rewriting it. The source file is
the authoritative full text.

## Original research objective

The proposal asked whether conservative/symplectic maps could be a more natural
geometric carrier of the arithmetic structures attributed to low-dimensional chaotic
prototypes. Its conceptual chain was:

```text
Logistic-type arithmetic seed
    -> Hénon-type geometric bridge
    -> symplectic maps / Hamiltonian chaos
    -> periodic-orbit geometry
    -> dynamical zeta / trace structure
    -> possible quantum/operator lift
```

The main contrast was conservative versus dissipative dynamics, with Route-A gates:

- A0: arithmetic relevance;
- A1: primitive periodic orbits;
- A2: dynamical zeta/Fredholm determinant;
- A3: analytic/Weil-compression compatibility;
- A4: natural quantization.

The proposed session could explore area-preserving Hénon maps, standard maps, kicked
maps, cat maps, twist maps, higher-dimensional couplings, and symplectic cocycles, so
long as it remained in the discrete symplectic-map family.

## Initial Stage-1 scope

Stage 1 was named "Conservative vs Dissipative Structural Baseline" and assigned to
`papers/1-symp-vs-diss/`. It targeted A0--A1 through:

- matched conservative/dissipative maps;
- a low-period UPO census;
- monodromy and recurrence comparisons;
- a first arithmetic-naturalness audit;
- a possible negative theorem or numerical obstruction.

The proposal correctly required that:

- prime or Riemann-zero tables not define the candidate;
- no period be assigned \(\log p\) by hand;
- no von Mangoldt weights be inserted;
- numerical evidence not be called proof;
- generic chaos or GUE statistics not count as arithmetic evidence;
- matched random, composite, shuffled, neighboring-parameter, and simpler-parent
  controls be used;
- a negative result be acceptable.

## Initial hypothesis package

The broad working hypothesis was:

```text
Logistic supplies an arithmetic seed
    -> Hénon supplies a geometric bridge
    -> symplectic maps supply a conservative mother structure
```

The proposal treated this as a hypothesis, not an assumption, but did not yet resolve
four critical operational questions:

1. What arithmetic property of the Logistic parent was independently reproducible?
2. What precise smooth relation would constitute a "lift" across the critical point?
3. What single statistic would test survival without inspecting prime labels?
4. How would orbit completeness and branch identity be certified in a mixed,
   nonuniform regime?

## Candidate family selected during Round 0

The audit selected the matched Hénon family

\[
H_{a,\rho}(x,y)=(1-a x^2-\rho y,x)
\]

because it has the exact determinant \(\rho\), contains a singular quadratic endpoint
at \(\rho=0\), conformally symplectic controls for \(0<\rho<1\), and the
area-preserving endpoint at \(\rho=1\).

The primary parameter was frozen at

\[
u_c=1.5436890126920763,
\]

inherited from the earlier Logistic work and not selected from Hénon multipliers,
prime labels, or Riemann zeros.

The initial candidate package contained:

- an exact conformal-symplectic calculation;
- a type-1 generating function at \(\rho=1\);
- a chain-rule obstruction to a regular smooth critical-map factor;
- a proposed low-period periodic-orbit ledger;
- a speculative unstable-multiplier Euler product;
- eventual zeta and quantum-map questions.

## Audit findings that forced refinement

### Upstream arithmetic weakness

The earlier Logistic evidence did not establish a prime-sieve isomorphism. The
reproducible conceptual support was, at most, a mod-2/parity shadow. Mod-3/mod-6
structure and admissible finite sieve words were not established. Legacy comparisons
also contained target-dependent scale choices or missing computational support.

Therefore the phrase "arithmetic seed" had to be downgraded to "attributed seed" or
"weak mod-2 shadow" until independently reproduced.

### Known direct priors

Fogedby and Jensen (2005) already constructed a canonical weak-noise extension of the
Logistic map, and Demaeyer and Gaspard (2009) analyzed singularities where \(f'=0\).
Generic Hénon orbit ledgers, symbolic dynamics, and spectral determinants are also
mature. The broad lift/ledger/zeta package therefore had low novelty.

### Exact but elementary obstruction

Differentiating a putative submersion factor
\(\pi\circ F=f\circ\pi\) gives an immediate rank contradiction over a critical point
when \(F\) is a local diffeomorphism. This is exact and useful for scoping, but it is an
elementary known boundary rather than a standalone novel theorem.

### Singular continuation

The \(\rho=0\) endpoint has zero determinant. It cannot be described as an ordinary
smooth continuation point of the regular \(\rho>0\) family. Orbit identity through
this endpoint needs an explicit branch rule and can be lost at collision, period
collapse, or bifurcation.

### Arithmetic Euler-product gap

For primitive hyperbolic multipliers one can formally define

\[
Z_u(s)=\prod_\gamma(1-|\Lambda_{u,\gamma}|^{-s})^{-1},
\]

but no intrinsic map from frozen Hénon orbits to rational primes had been specified.
Generic prime-orbit counting is not rational-prime coding, and the ordinary
semiclassical stability denominator is not the proposed multiplier monomial.

## Round-0 disposition

The broad multi-stage hypothesis remained scientifically interesting but was not ready
for implementation as written. It was sent to independent technical review with these
candidate priorities:

1. elementary obstruction plus a frozen-parameter symbolic survival/failure test;
2. high-\(a\) anti-integrable orbit-finder calibration;
3. multiplier-prime Euler product, explicitly marked speculative and deferrable.

No numerical conclusion was made in Round 0.

