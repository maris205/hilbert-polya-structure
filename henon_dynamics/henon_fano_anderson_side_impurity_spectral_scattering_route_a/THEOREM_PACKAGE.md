# Proof package

## Status

`PROVABLE AS STATED` for the frozen main domain `J>0`, `epsilon real`, and
`g nonzero`.  The faces `g=0` and `J=0` are separate exact degenerations.

## Claim

Let

```text
H = H_chain direct_sum epsilon|d><d|
    + g(|0><d|+|d><0|)
```

on `ell2(Z) direct_sum C|d>`, where
`(H_chain u)_n=J(u_{n+1}+u_{n-1})` and `J>0`.
For `g!=0`, the spectrum is the purely absolutely continuous band
`[-2J,2J]`, of multiplicity two almost everywhere, plus exactly two simple
eigenvalues, one on each exterior component.  The impurity density, atom
weights, scattering probabilities, and continuum Fano zero are the formulas
stated below.

## Assumptions and notation

- `S(z)=sqrt(z^2-4J^2)` is analytic on the complement of the band and is
  normalized by `S(z)/z -> 1` at infinity.
- `m(z)=<0,(z-H_chain)^(-1)0>=1/S(z)`.
- `D(z)=z-epsilon-g^2 m(z)` and `G_dd(z)=1/D(z)`.
- On the real exteriors, `S(E)>0` above the band and `S(E)<0` below it.

## Dependency map

1. Fourier transform gives the free spectrum and local Green function.
2. Block inversion gives `G_dd=1/D` and the pole/eigenvector equivalence.
3. Monotonicity of the two real physical branches gives exactly two simple
   bound states.
4. Reflection parity gives a free odd half-line and an even-plus-impurity
   Jacobi matrix.  The latter is cyclic when `g!=0`; its explicit
   anti-Herglotz Cauchy resolvent classifies the whole even spectral measure.
5. Local-uniform boundary values and Stone inversion give the full open-band
   measure, while off-band meromorphy and edge atom tests exhaust the
   remaining support.
6. Stationary matching gives scattering amplitudes and the Fano zero.

## Proof

### 1. Operator and free resolvent

The chain has norm `2J`; the impurity and hybridization are finite rank.
Thus `H` is bounded and self-adjoint on the full Hilbert space.  Fourier
transform sends the chain to multiplication by `2J cos(k)`, so its spectrum
is purely absolutely continuous on `[-2J,2J]`, with multiplicity two in the
open band.  The elementary contour integral gives

```text
m(z) = (2pi)^(-1) integral_0^{2pi} (z-2J cos k)^(-1) dk
     = 1/S(z).
```

The normalization at infinity fixes the sheet, including the negative sign
of `S(E)` below the band.

### 2. Schur complement and two physical poles

Block inversion at the impurity coordinate gives

```text
G_dd(z)=1/(z-epsilon-g^2/S(z)).
```

A real exterior zero of `D` produces an `ell2` eigenvector by applying the
free resolvent to the origin; conversely every exterior eigenvector has a
nonzero impurity component and hence gives such a zero.

For `E>2J`, define

```text
D_+(E)=E-epsilon-g^2/sqrt(E^2-4J^2).
```

It tends to minus infinity at `2J+`, tends to plus infinity at infinity, and

```text
D_+'(E)=1+g^2 E/(E^2-4J^2)^(3/2)>0.
```

Thus it has exactly one simple zero.  For `E<-2J`, define

```text
D_-(E)=E-epsilon+g^2/sqrt(E^2-4J^2).
```

It tends to minus infinity at minus infinity, to plus infinity at `-2J-`,
and

```text
D_-'(E)=1-g^2 E/(E^2-4J^2)^(3/2)>0.
```

It too has exactly one simple zero.  Squaring either equation yields

```text
(E-epsilon)^2(E^2-4J^2)-g^4=0,
```

but the upper root must also satisfy `E>max(2J,epsilon)`, and the lower root
must satisfy `E<min(-2J,epsilon)`.  Roots violating these inequalities are
on the wrong algebraic branch and are not eigenvalues.

### 3. Spectral type and multiplicity

Reflection about the origin reduces the chain into odd and even subspaces.
The odd subspace has `u_0=0` and does not see the impurity; it is a free
Dirichlet half-line Jacobi matrix with simple purely absolutely continuous
spectrum on the band.  Order the even-plus-impurity subspace as
`d,0,e_1,e_2,...`, where `e_n` is the normalized even pair at `plus_or_minus n`.
Its Jacobi off-diagonals are `g,sqrt(2)J,J,J,...` and its diagonal is
`epsilon,0,0,...`.  Because `g!=0`, the impurity vector is cyclic.

Let `mu_d` be the spectral measure of the cyclic vector `|d>`.  With the
resolvent convention used here,

```text
G_dd(z)=integral (z-E)^(-1) d mu_d(E)
```

has negative imaginary part in the upper half-plane: it is the
anti-Herglotz Cauchy transform.  Equivalently,
`M_dd(z)=-G_dd(z)=<d,(H-z)^(-1)d>` is Herglotz.  This sign distinction is
essential below.

For `|E|<2J`, put `s(E)=sqrt(4J^2-E^2)`.  The upper boundary value is

```text
G_dd(E+i0)=1/(E-epsilon+i g^2/s(E)),
```

and Stone--Stieltjes inversion gives

```text
rho_d(E)=-pi^(-1) Im G_dd(E+i0)=g^2 s(E)
 / [pi((E-epsilon)^2 s(E)^2+g^4)].
```

This is positive throughout the open band.  To identify the *whole* measure,
not merely its absolutely continuous part, fix a compact interval
`K subset (-2J,2J)`.  The chosen branch of `S` has a continuous upper boundary
value on `K`, and the imaginary part `g^2/s(E)` of the denominator is strictly
positive.  Consequently `G_dd(E+i eta)` converges uniformly on `K` to the
displayed non-polar boundary value.  For every continuous test function
`phi` supported in the interior of `K`, Stone's formula and Fubini give

```text
integral phi(E) d mu_d(E)
 = limit_(eta downarrow 0) integral phi(E)[-pi^(-1) Im G_dd(E+i eta)] dE
 = integral phi(E) rho_d(E) dE.
```

Thus `mu_d` restricted to every such `K` equals `rho_d(E)dE`; compact
exhaustion identifies the entire open-band restriction and leaves no embedded
singular measure there.

On either real band exterior, `G_dd` continues real-analytically except at
the unique simple zero of `D` already proved.  Applying the same inversion
principle on pole-free exterior intervals shows that there is no measure
there, while each simple pole contributes exactly its residue as an atom.
It remains only to inspect `E_0=plus_or_minus 2J`.  Rewriting

```text
G_dd(z)=S(z)/[(z-epsilon)S(z)-g^2]
```

shows `G_dd(E_0+i eta)->0`.  The atom formula in the present Cauchy convention
is

```text
mu_d({E_0})=limit_(eta downarrow 0) i eta G_dd(E_0+i eta)=0.
```

Any measure supported on the two remaining edge points would be atomic, so
these zero limits exclude the last possible singular remainder.  Hence the
cyclic even component has precisely the density and two exterior atoms, with
no singular continuous component.  Combining it with the odd half-line proves
multiplicity two almost everywhere in the band and completes the full
spectral classification.

At a pole `E_*`, the impurity atom is the residue

```text
w_* = 1/[1-g^2 m'(E_*)].
```

Here `m'(E_*)<0`, so `0<w_*<1`.  Finally
`G_dd(z)=z^(-1)+O(z^(-2))`; its Cauchy-transform representation therefore has
total mass one.  Thus the integral of `rho_d` plus the two residues equals one.

### 4. Scattering

For `E=2J cos(k)`, `0<k<pi`, eliminate the impurity away from `E=epsilon`.
The origin acquires the on-shell potential `V(E)=g^2/(E-epsilon)`.  Matching
an incoming plane wave and its reflected/transmitted waves gives

```text
t = 2 i J sin(k)/(2 i J sin(k)+V),
r = -V/(2 i J sin(k)+V).
```

Consequently

```text
T = 4J^2 sin(k)^2 (E-epsilon)^2
    / [g^4+4J^2 sin(k)^2(E-epsilon)^2],
R = g^4/[g^4+4J^2 sin(k)^2(E-epsilon)^2],
T+R=1.
```

At `E=epsilon`, the uneliminated impurity equation forces `u_0=0` when
`g!=0`, so `T=0` directly.  This energy is an open scattering channel exactly
when `|epsilon|<2J`.  Hence a continuum Fano zero occurs if and only if the
impurity energy lies in the open band.

### 5. Degenerate boundaries

- If `g=0`, the system is the direct sum of the free chain and the isolated
  impurity eigenvalue `epsilon`; that eigenvalue is embedded, at threshold,
  or isolated according as `|epsilon|` is less than, equal to, or greater
  than `2J`.
- Replacing `g` by `-g` is conjugation by the unitary that changes the impurity
  sign, so every spectral and scattering probability is unchanged.
- If `J=0`, the origin/impurity block is `[[0,g],[g,epsilon]]`, with eigenvalues
  `(epsilon plus_or_minus sqrt(epsilon^2+4g^2))/2`; all other lattice sites
  form an infinite-multiplicity zero eigenspace.
- If `epsilon=plus_or_minus 2J`, the impurity energy is not an open channel.
  For `g!=0`, the edge atom test above gives zero mass; equivalently, the free
  threshold recurrence has no nonzero square-summable solution.
- The `g to 0` pole limits are nonuniform at the square-root thresholds; the
  exact `g=0` direct-sum statement is not inferred by continuity.

Therefore the claim follows.  QED.

## Open risks and controlled nonclaims

No theorem depends on finite-box convergence.  The code checks the branch
filter rather than accepting all quartic roots.  The cited literature supplies
provenance only.  No arithmetic, target determinant, target zero, functional
equation, automorphy, Hilbert--Polya, or Route-B conclusion is claimed.
