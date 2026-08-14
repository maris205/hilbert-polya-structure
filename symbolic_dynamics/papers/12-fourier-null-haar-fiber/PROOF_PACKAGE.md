# SD-C14 Proof Package

## Claim

Every finite positive Borel measure `mu` on the unit circle satisfying
`integral z^r dmu=1` for all `r>=1` has the unique form

```text
mu = delta_1 + c m_Haar,  c>=0.
```

The Haar component gives the unique positive diffuse escape from finite
moment rigidity.  In SD-C14 it is realized by
`A=C direct-sum L(Z)`, `W=1 direct-sum u`, and
`Phi_c(a direct-sum x)=a+c tau(x)`.  It preserves every nonzero power trace
but cancels from the analytic trace-log determinant.  Normalization removes
the escape, Fuglede--Kadison visibility is radial and nonholomorphic, natural
self-adjointization erases the phase, and recurrent inverse coupling creates
new balanced mixed words.

## Status

PROVABLE AS STATED.

The positive result is an obstruction theorem, not an RH divisor or spectral
realization.  Route B is not invoked.

## Assumptions

- `mu` is a finite positive Borel measure on `T`.
- Haar measure `m_Haar` is normalized to mass one.
- `u` is the canonical Haar unitary in `L(Z)`.
- `c>=0`; for `c>0`, `Phi_c` is a faithful finite positive trace but is not a
  state.
- The analytic determinant is the scalar trace-log germ at `q=0`.
- Coupled path words are audited before scalar specialization.

## Notation

- `m_r(mu)=integral_T z^r dmu(z)`.
- `A=C direct-sum L(Z)` and `W=1 direct-sum u`.
- `Phi_c(a direct-sum x)=a+c tau(x)`.
- `D_c(q)=exp(Phi_c(log(1-qW)))` for `|q|<1`.
- `Delta_c` denotes the Fuglede--Kadison determinant for `Phi_c`.

## Proof Strategy

Positivity recovers all negative Fourier coefficients from the positive ones.
Subtract a point mass and the only possible zeroth-mode residue; Fourier
uniqueness then forces the residue to be Haar measure.  Functional calculus
computes the analytic and Fuglede--Kadison determinants.  Direct block
multiplication treats self-adjointization and recurrent inverse coupling.

## Dependency Map

1. The classification theorem uses positivity and Fourier uniqueness.
2. The trace construction uses the canonical group trace on `L(Z)`.
3. Analytic invisibility uses the all-order positive moments.
4. Fuglede--Kadison visibility uses Jensen's circle integral.
5. Chiral erasure and mixed-word contamination use exact block products.

## Proof

### Step 1: positive-measure classification

Let `M=mu(T)`. Positivity gives `m_{-r}=conj(m_r)=1`, and
`1=|m_1|<=M`; put `c=M-1>=0`. The signed measure

```text
nu = mu - delta_1 - c m_Haar
```

has every Fourier coefficient equal to zero, including degree zero.
Trigonometric polynomials are uniformly dense in `C(T)`, so integration
against `nu` vanishes on every continuous function. Thus `nu=0`.

### Step 2: normalization and finite support

If `mu(T)=1`, then `c=0`. If `mu` has finite support and `c>0`, the identity
`mu=delta_1+c m_Haar` would contain a nonzero nonatomic part, a contradiction.
Hence finite support also forces `c=0`.

### Step 3: the Haar fiber

The canonical trace satisfies `tau(u^r)=0` for every nonzero integer `r`.
Consequently

```text
Phi_c(W^r)=1,  r!=0,
Phi_c(1)=1+c.
```

For `c>0`, faithfulness holds on both direct summands. Normalizing the trace
divides the visible moment by `1+c`, so the exact ledger is lost.

### Step 4: analytic invisibility

For `|q|<1`, norm-convergent functional calculus gives

```text
log D_c(q)
 = -sum_(r>=1) q^r Phi_c(W^r)/r
 = -sum_(r>=1) q^r/r
 = log(1-q).
```

Thus `D_c(q)=1-q`, independently of `c`. Comparing Taylor coefficients also
proves the converse: equality of scalar trace-log germs is equivalent to
equality of all aggregated positive trace moments.

### Step 5: magnitude, self-adjointization, and coupling

Jensen's formula yields

```text
log Delta_c(1-qW)
 = log|1-q| + c integral_T log|1-qz| dm_Haar(z)
 = log|1-q| + c log^+|q|.
```

Therefore `Delta_c=|1-q|max(1,|q|)^c`. It is ghost-blind for `|q|<1` and
nonholomorphic when it becomes `c`-sensitive.

For `H=[[0,W],[W*,0]]`, direct multiplication gives `H^2=I`. The weighted
self-adjoint block has square `|q|^2 I`; phase is erased. Finally, recurrent
edges labeled by `u` and `u^{-1}` create the identity word `uu^{-1}`. A
two-edge transfer has a quadratic trace proportional to
`2(1+c)xy`, an extra mixed closed path rather than a pure atom repetition.

Therefore the claim follows. ∎

## Corrections or Missing Assumptions

- Positive moments alone do not classify an arbitrary complex measure;
  positivity is what supplies the negative moments.
- `Phi_c` is not a state for `c>0`.
- The trace-log germ is not identified with every Banach-algebra determinant
  convention; its branch and domain are frozen explicitly.
- A nonbacktracking rule may delete immediate reversal only by changing the
  coupled grammar; it does not preserve the proposed self-adjoint block.

## Open Risks

- The construction has no arithmetic selectivity: arbitrary positive atom
  weights admit the same Haar ghost.
- Character-resolved information is averaged out before forming the scalar
  determinant.
- No functional equation, divisor counting law, or spectral operator is
  obtained.

## Route evaluation

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
GO_INFINITE_HAAR_ESCAPE
STOP_DETERMINANT_INVISIBILITY
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

The A1 and A2 passes certify the unchanged base repetition ledger and its
ghost-blind analytic determinant.  They do not certify a new phase mechanism.
