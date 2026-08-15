# Paper 35 source lock — SD-C37

## 1. Question

Can the unprojected positive `ax+b` semigroup source, with its original
generator-step marker and multiplicative energy, own a nonzero primitive
periodic ledger whose ordinary Fredholm trace-log is the Bost--Connes zeta
partition function?

The answer is negative for the objects frozen below. The paper is an affine
benchmark and object-separation theorem, not a new Bost--Connes model.

## 2. Full positive affine semigroup

Let

```text
P = N_0 semidirect N^times,
(b,a)(d,c) = (b+ad, ac),
u = (1,1),
d_n = (0,n), n>=2.
```

The positive right Cayley graph has edges `x->xu` and `x->xd_n` for every
`n>=2`. The identity generator is excluded. The height

```text
h(b,a)=b+a
```

strictly increases along every edge. Thus the positive graph has no nonempty
directed closed path. The source is not prime-labeled: it uses all `n>=2`.

The natural unweighted whole adjacency has infinite outdegree and is not an
operator on a vertex basis vector in `ell^2(P)`. For `beta>1`, the weighted
formal sum

```text
A_beta = V_u + sum_{n>=2} n^{-beta} V_{d_n}
```

is norm-convergent and bounded, but contains an undamped translation isometry
and is noncompact. The Hamiltonian `H delta_(b,a)=log(a) delta_(b,a)` has
infinite additive multiplicity, so `exp(-beta H)` is never trace class on the
full `ell^2(P)`.

## 3. Minimal bounded benchmark

For `r>=2`, freeze

```text
P_r = <u,v | vu=u^r v>^+
    = {(b,k): b,k in N_0},
(b,k)(d,l)=(b+r^k d,k+l).
```

The right generators are

```text
U(b,k)=(b+r^k,k),
V(b,k)=(b,k+1).
```

The canonical experiment uses `r=4`; `r=2,3,5` and mutated exponents are
controls. Each edge has roof one, and `z` counts one generator edge. The
positive vertex adjacency is `A_+=S+T` on `ell^2(P_r)`, where `S,T` are the
right shifts.

## 4. Three recurrence objects

1. **Positive graph.** The height `h_r(b,k)=b+r^k` strictly increases, so it
   has no nonempty directed closed word.
2. **Formal symmetrization.** Add a reverse arc for every retained edge. Each
   edge then gives a primitive two-step backtrack. This is a new graph.
3. **Hashimoto graph.** States are oriented edges; immediate reversals,
   including at the cyclic join, are forbidden. The reduced relation word

   ```text
   v u v^{-1} u^{-r}
   ```

   has length `r+3`, is primitive, and survives. Full affine slices also
   retain multiplicative commutation relation words.

The complete relation ledger is generic in `r`; it is not prime selective.

## 5. Whole-operator ownership

`A_+`, the bounded symmetrized adjacency, and the bounded finite-degree
Hashimoto operator are tested on their natural uninduced `ell^2` spaces.
All are noncompact. No ordinary Fredholm determinant is claimed for them.
Finite-volume determinants are diagnostic only and do not define an infinite
Fredholm limit without an additional theorem.

## 6. Finite quotient boundary

Congruence quotients preserve the labeled affine relation identity, but they
also create positive translation cycles `U_q^q` and may collapse a relation
polygon at small moduli. A quotient primitive ledger is therefore not the
ledger of the infinite positive Cayley graph.

## 7. Bost--Connes firewall

On `ell^2(N^times)`, the Bost--Connes Hamiltonian satisfies

```text
H epsilon_n = log(n) epsilon_n,
D_beta = exp(-beta H),
Tr(D_beta)=zeta(beta), beta>1.
```

Its actual Fredholm determinant obeys

```text
-log det(I-z D_beta)
  = sum_{m>=1} z^m zeta(m beta)/m.
```

Thus `zeta(beta)` is the first trace coefficient, not the determinant. The
bosonic determinant in the original construction uses a prime-indexed
one-particle basis and specializes fugacity at `z=1`; it is not the primitive
determinant of the positive affine graph.

## 8. Source/evaluator firewall

Candidate code may use affine multiplication, generator words, heights,
finite quotients, exact matrices, and formal power series. It may not inspect
primality, factorization support, zeta zeros, fitted coefficients, or an
accepted-support table. The independent evaluator reconstructs normal forms,
relations, cyclic reduction, primitive roots, quotient cycles, determinant
coefficients, and all control labels without importing the source core.

## 9. Mandatory controls

- `r=2,3,4,5`, including the composite baseline `r=4`;
- mutated relations `vu=u^qv` and arbitrary finite monoid presentations;
- positive, symmetrized, and nonbacktracking ledgers;
- finite quotient moduli with extra translation cycles and small-modulus
  degeneration;
- diagonal Gibbs traces versus Fredholm trace-log coefficients;
- bosonic fugacity `z` versus the specialization `z=1`;
- signed, matrix, supertrace, boundary/GNS, and fixed-target controls;
- exact source/evaluator separation and no prime oracle.

## 10. Route lock

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

No xi completion, functional equation, zero divisor, Weil compression,
critical-line fit, or RH implication is claimed.

## 11. Provenance

- Mathematical package SHA-256:
  `e04f11dbb0ced5ad55a878cc4364c8a8d1ca33cb4cbb919b8e6b2149b83ebd25`.
- Literature audit SHA-256:
  `f2a11df03f72a0277205a805f077996d17ef2d51b235ad993c1619ac3a1d2653`.
- Canonical experiment and two-stage Git hashes are intentionally not
  embedded in this source lock. They are recorded downstream in the experiment
  report, results ledger, integrity audit, and Route card. This keeps the
  pre-execution research lock acyclic when it hashes this file.

## 12. Paper 36 boundary

Paper 36 may test one quotient-aware or homological cancellation of the
affine relation ledger only if it remains on a single uninduced symbolic
object, commutes with the original generator marker, kills backtracks and
all affine/commutation relation cycles chainwise, retains a nonzero
source-natural arithmetic sector, and fails matched generic presentations.
A boundary/KMS projector, prime basis, or another scalar character is not an
eligible repair.
