# HCS-C79 minimum-repair witness multiplicity

C79 refines the finite repair geometry of the frozen named support
`L={S1,...,S16}` in `Q=Z/9 + Z/3 + Z/2`.  For a deletion mask `D`, write
`A=L\\D` and define

```text
rho(D) = min{|R| : R subset D and Phi(A union R)=Q},
W(D)   = #{R subset D : |R|=rho(D) and Phi(A union R)=Q}.
```

All `2^16=65536` masks are enumerated.  The pivot is `S9`, and the four
direction blocks are `[S1]`, `[S16]`, `[S7,S15]`, and
`[S3,S4,S8,S11,S12]`; the remaining six labels are generation dummies.
The exact structural formulas are

```text
rho(D) = 1_{S9 in D} + max(0,t(D)-2)
W(D)   = 1                         (t <= 2)
       = sum_i s_i                 (t = 3)
       = sum_{i<j} s_i*s_j         (t = 4),
```

where `t(D)` counts fully deleted direction blocks and `s=(1,1,2,5)`.
Thus `W` takes exactly `{1,4,7,8,25}`.  The global joint inventory is

```text
(rho,W): (0,1)=30400, (1,1)=30400, (1,4)=1984, (1,7)=192,
          (1,8)=128, (2,4)=1984, (2,7)=192, (2,8)=128,
          (2,25)=64, (3,25)=64.
```

The canonical trivariate receipt is
`results/c79_repair_witness_multiplicity_evidence.json` with SHA-256
`147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879`.
The producer, direct point-set checker, SymPy block expansion, clean replay,
and hostile mutation audit are in `code/`.

This is a finite named-coordinate result only.  It makes no arithmetic,
local, Euler-factor, root-number, automorphy, full Burnside-ring/table-of-
marks, or Hilbert--Polya claim.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
