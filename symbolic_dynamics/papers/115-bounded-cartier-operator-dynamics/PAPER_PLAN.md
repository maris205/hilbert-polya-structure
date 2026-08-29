# Paper Plan — P115

Status: author draft; external novelty/priority/release **HOLD**.

## One-sentence contribution

For the residue-class-zero Cartier section on degree-bounded polynomials over
`F_(p^a)`, determine its explicit index-chain product, every iterate fibre,
transient shell, Frobenius-core component, lattice depth law, and recoverable
parameter.

## Contract-to-section map

| Required contract | Main-text destination | Proof mechanism |
|---|---|---|
| Coefficient iterate | Theorem 3.1 | Induction along coefficient-index chains |
| Product/component structure | Theorem 3.2 | `d_(u,v)=sigma^(-v)(c_(up^v))`; nilpotent shifts and inverse Frobenius |
| All images and fibres | Theorem 3.3 | Explicit preimage coordinates; complementarily, Proposition 3.4 rank–nullity |
| Core-entry CDF and sharp depth | Theorem 4.1 | `p`-adic chain extinction, CDF differencing, top-chain count |
| Inverse-Frobenius fixed/cycle/zeta | Theorem 5.1 | Stable image, finite-field fixed subfields, Möbius inversion, cycle Euler product |
| Lattice depth limit | Theorem 6.1 | Exact floor identity; fixed tails stabilize rather than merely converge |
| `(p,a,n)` temporal recovery | Theorem 7.1 | First fixed count, first global maximum of fixed sequence, phase cardinality |

## Narrative order

1. Start from the finite dynamical question, not generic Cartier history.
2. Subtract the exact coefficient selector and finite-field background before
   presenting residual claims.
3. Define inverse-Frobenius notation and all small-parameter conventions.
4. Establish the iterate once, expose its index-chain product and components,
   then close images/fibres with an explicit proof and a complementary count.
5. Use the coefficient forest to expose the transient profile.
6. Pass to the stable constant image for periodic data.
7. Convert the finite CDF into the lattice law and then temporal rigidity.
8. End with exact controls, false-shortcut guards, and HOLD scope.

## Proof-route firewall

- **Route I — coefficient forest:** Each positive index `j=p^v*u` survives
  through time `v` and is killed at `v+1`; the constant index follows an
  automorphism. This route is pointwise and proves the sharp clock.
- **Route II — complementary finite-field linear algebra:** After the iterate
  formula is established, over `F_p`, `C^t` factors as coordinate restriction,
  inverse Frobenius, and zero-padding. Rank--nullity recounts uniform fibres
  and the CDF. It is not advertised as an independent derivation of the map.

Neither route is presented as new general Cartier theory or new generic
finite-linear functional-graph theory. Restriction-of-scalars linearization,
cyclic--nilpotent decomposition, component products, and attached-tree
machinery are classical owner territory and receive zero credit. The residual
is limited to the exact bounded Cartier specialization and the
lattice/recovery conjunction.

## Boundary checklist

- `t=0`: identity iterate, full image, singleton fibres, constants are the
  depth-zero CDF.
- `n=0`: phase equals core, maximum depth zero, all `q` states are deepest.
- `a=1`: inverse Frobenius is identity and zeta is `(1-z)^(-p)`.
- `p^t>n`: image is exactly the constants and each nonempty fibre has `q^n`
  points.
- Empty fibres: every target of degree above `floor(n/p^t)` has fibre zero.
- Constant polynomial: no empty maximum and no use of `v_p(0)`.
- `alpha=1`: included; `alpha=p` is represented after shifting `L` and is
  excluded from the chosen half-open lattice window.
- Fixed/cycle formulas use `m>=1` and positive divisors only.
