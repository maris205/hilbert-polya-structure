# Proof package

For a continuous symbolic potential `f`, marked packet pressure has slope
`int f d eta_J`. If `f'=f+u-u∘sigma`, then

```text
P_J(f')-P_J(f) = -A_J(u),
A_J(u)=int(u-u∘sigma)d eta_J.
```

The law `eta_J` is supported on sequences reflected about zero. Its shifted
law is supported on sequences reflected about the adjacent center. Their
intersection consists of period-two sequences and has measure zero under
either iid half-word construction. Thus the measures are mutually singular,
and the signed measure `eta_J-sigma_*eta_J` has total-variation norm `2`.

For `r>=1`, let

```text
u_r=1{s[-k]=s[k] for 1<=k<=r}.
```

Under `eta_J`, `u_r=1`. After one shift, the constraints are
`xi_(k-1)=xi_(k+1)`, leaving two free parity classes among `r+2` fair bits;
their probability is `2^-r`. For `v_r=2u_r-1`,

```text
A_J(v_r)=2(1-2^-r) -> 2.
```

This realizes the norm asymptotically with locally constant witnesses.

For any periodic word of period `n`,

```text
sum_(j=0)^(n-1) (u-u∘sigma)(sigma^j omega)=0
```

exactly. Hence every orbit-averaged packet pressure is cohomology invariant
at finite `n`, not merely in the limit.

The result shows marked pressure needs a frozen gauge. It does not invalidate
P64's frozen coordinate-Mahler law, but it prevents treating that law as a
canonical Livšic invariant. It proves no prime trace or operator statement.
