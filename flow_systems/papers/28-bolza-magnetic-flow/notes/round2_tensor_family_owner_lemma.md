# P28 Round-2 tensor-family owner lemma

Date: **2026-08-27**
Scope: owner bookkeeping only; no magnetic-orbit, spectral, or trace-regime
claim is made.

## Frozen objects

Let `Sigma_B` be the curvature `-1` Bolza surface, let `L` be the frozen
degree-one Hermitian line bundle with its frozen unitary connection, and let
`L_dual` carry the dual connection. For every integer `N>=1`, define

```text
Hilbert_(N,+) = L2(Sigma_B,L^N),
H_(N,+)       = Delta^(L^N),
Hilbert_(N,-) = L2(Sigma_B,(L_dual)^N),
H_(N,-)       = Delta^((L_dual)^N).
```

The operator domain is the Sobolev space of `H2` sections of the named bundle;
equivalently, the operator is the self-adjoint elliptic closure of its action
on smooth sections. The zero-field control uses the trivial bundle and trivial
connection.

## Lemma 1 — degree and holonomy ownership

`[PROVED]` For every `N>=1`,

```text
deg(L^N)=N,                  deg((L_dual)^N)=-N,
Hol_(L^N)(gamma^r)=Hol_L(gamma)^(N*r),
Hol_((L_dual)^N)(gamma^r)=conj(Hol_L(gamma))^(N*r).
```

**Proof.** First Chern class is additive under tensor product and changes sign
under duality. The induced tensor connection is the sum connection, so parallel
transport tensorizes; dual parallel transport is the inverse, which is complex
conjugation for unitary holonomy. Repeating a loop `r` times raises its holonomy
to the `r`th power. Combining tensor power and repetition gives the displayed
exponent `N*r`. No primitive-orbit or trace multiplicity is used.

## Lemma 2 — exact field-reversal owner

`[PROVED]` Fibrewise Hermitian conjugation defines an antiunitary map

```text
C_N: L2(Sigma_B,L^N) -> L2(Sigma_B,(L_dual)^N)
```

which intertwines the Bochner Laplacians built from the connection and its
dual:

```text
C_N H_(N,+) C_N^(-1) = H_(N,-).
```

On the classical unit tangent bundle, velocity reversal `R(x,v)=(x,-v)` obeys

```text
phi_(-b)^t R = R phi_b^(-t).
```

Thus the exact comparison partner of `b=+1/2` is `b=-1/2` at the same `N`,
and the corresponding holonomy phase is conjugated. A spectral statistic that
forgets orientation and phase cannot use field-sign persistence as an
arithmetic discriminator. This is a falsification constraint, not a positive
prime mechanism.

## Lemma 3 — tensor-family and fixed-operator credits do not transfer

`[PROVED]` The sequence `{H_(N,+)}_(N>=1)` is a changing-bundle operator
family. It is not the high-energy sequence of the single operator `H_(1,+)`.

**Proof.** The bundles `L^N` and `L^M` have different first Chern classes when
`N != M`; hence no bundle isomorphism over the identity can canonically
identify their sections or connections. Abstract separable-Hilbert-space
unitaries do not preserve the geometric owner and therefore provide no trace
credit. Although `H_(1,+)=Delta^L` is literally the `N=1` member, the limits

```text
N -> infinity through changing (Hilbert_N,H_N)
```

and

```text
lambda -> infinity in the spectrum of fixed Delta^L
```

have different varying data. An implication between them would require a
separate uniform two-parameter theorem specifying the rescaled operator,
energy window, trace distribution, and remainder. No such theorem has been
established in this project.

Consequently,

```text
SEMICLASSICAL_RESCALED_OPERATOR=UNASSIGNED
SEMICLASSICAL_TRACE_REGIME=OPEN
SEMICLASSICAL_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
FIXED_OPERATOR_CREDIT_TRANSFER_ALLOWED=false
```

The bookkeeping convention `h=1/N` used in the Round-2 owner ledger is a
`[MODELING_CHOICE]`. It does not select whether the operative family is
`h^2 H_N`, a shifted/rescaled operator, or another source-bound normalization.

## What this lemma does and does not establish

The lemma closes the bundle, duality, domain, repetition, and owner-separation
obligations needed before code can safely distinguish regimes. It does not
establish:

- a primitive magnetic-orbit enumeration;
- an energy-window scaling;
- a magnetic trace formula for the frozen family;
- a prime or prime-ideal dictionary;
- an arithmetic-specific phase cancellation;
- an A4 or Route-B credit.

The next smallest test is to source-bind one rescaled operator, one energy
window, and one trace distribution, then construct a genuine magnetic-orbit
ledger with residual and completeness diagnostics. The still-uninstantiated
area-matched non-arithmetic genus-2 metric remains a mandatory control.
