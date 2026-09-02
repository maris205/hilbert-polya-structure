# Independent hostile gate: divisor-imbalance dynamics (DDI)

Verdict: **KILL (1 Critical / 0 Major / 1 minor)**  
Mathematical audit: **PASS**  
Portfolio/owner audit: **FAIL -- exact internally killed duplicate**  
External state: **HOLD_EXTERNAL**

## Outcome first

The formulas in the DDI scout are correct.  The candidate nevertheless fails
the paper threshold decisively: it is the exact previously killed `D01/X01`
complementary-divisor tent map, and the historical X01 archive proves a
strictly stronger theorem package.  This is a kill, not an amber repair lane.

## Cold derivation

Write `N=product_i p_i^(e_i)` and `d=product_i p_i^(a_i)`.  Primewise,

`v_p(lcm(d,N/d)/gcd(d,N/d))=|a-(e-a)|=|2a-e|`.

For one coordinate let `x=e-a`.  If
`fold_(2e)(r)=min(r mod 2e,2e-(r mod 2e))`, then

`e-|2a-e|=fold_(2e)(2x)`,

and induction yields

`Phi_e^t(a)=e-fold_(2e)(2^t(e-a))`.

Thus the state is a sign class in `Z/(2e)`, acted on by doubling.  Put
`L=v_2(2e)` and `e=2^(L-1)m`, `m` odd.  A class becomes recurrent exactly
when its representative is divisible by `2^L`, so

`delta_e(a)=max(0,L-v_2(e-a))`, with `v_2(0)=infinity`.

Counting sign classes gives

`H_e(0)=H_e(1)=(m+1)/2`,
`H_e(r)=2^(r-2)m` for `2<=r<=L`.

The product depth is the maximum of coordinate depths, hence its exact layer
is the product-CDF difference.  The sharp height is
`max_i(1+v_2(e_i))`.

On the recurrent odd modulus, a class is fixed at time `k` iff
`2^k x=+x` or `2^k x=-x`.  The two solution groups intersect only at zero,
and sign Burnside gives

`F_e(k)=(gcd(2^k-1,m)+gcd(2^k+1,m))/2`.

Products give `Fix(Phi_N^k)`, and ordinary Möbius inversion gives the number
of cycles of each exact length.

At time `t>=1`, let `g=2^min(t,L)` and put `y=e-b` for target exponent `b`.
Solving `2^t[x]=[y]` gives

```text
0       if g does not divide y,
g/2+1   if y=0,
g/2     if y=e and g divides e,
g       otherwise.
```

The zero endpoint contains both reflection-fixed source classes; the opposite
endpoint contains neither.  This proves the image size and endpoint-sensitive
fibre factors.  All global statements multiply over prime coordinates.

## Boundary attacks

- `t=0` is the identity and was kept separate from the positive-time fibre
  formula.
- `e=1` is a genuine one-step constant map and satisfies the histogram and
  endpoint formula.
- Odd and even `e`, pure powers of two, odd `e`, and mixed prime-exponent
  products were all checked.
- Both reflection-fixed endpoints `y=0,e` were enumerated independently.
- Post-tail images and nontrivial odd recurrent cycles were checked through
  exact direct functional graphs.
- The cycle formula was tested by direct extraction of minimal cycles, not
  only by comparing fixed-point counts.

No mathematical counterexample was found.

## Independent executable evidence

`verify_hostile.py` imports no author code.  It uses direct integer gcd/lcm,
direct finite-map orbit detection, independent residue-quotient lifting, and
direct minimal-cycle extraction.

Coverage:

- all local exponents `e=1..256`, all states, times `0..19`;
- 18 product boxes, all states/targets, times `0..11`;
- exact cycle lengths `1..20` checked against direct cycle inventories;
- 21 literal integers, including mixed and high-divisor boxes;
- **2,832,764 assertions**.

Two fresh replays were byte-identical to `CANONICAL.txt`:

- replay 1 SHA-256: `e8fd4c8916f8f66c626dacc17e7e6c2fea0ee3e21c715da720b0673a31b712fc`
- replay 2 SHA-256: `e8fd4c8916f8f66c626dacc17e7e6c2fea0ee3e21c715da720b0673a31b712fc`
- verifier SHA-256: `e3687e2e07f95d93f9a1c6c5443a6590f4867e039ccb2d969fc45c0157ae4789`

Reproduce with:

```bash
python3 docs/papers162_166_sequence/phase1/ddi_hostile_gate/verify_hostile.py
```

## Findings and executable repairs

### Critical C1 -- exact resurrection of a permanently killed system

DDI equals historical `D01/X01` in carrier and literal update.  The old X01
archive already proves all current axes and additionally classifies every
point's least eventual period.  A prior independent gate explicitly forbids
resurrection as a reserve or fallback.

**Repair:** none within DDI.  Mark the candidate killed and select a genuinely
different literal system.  Changing notation, adding larger verification
boxes, or repackaging endpoint fibres is not a repair.

### minor m1 -- current owner log misses the decisive records

The author log notes OEIS and generic tent maps but omits both direct
arithmetic Z-game owners and, more importantly, the exact internal D01/X01
kill record.

**Repair for archival accuracy only:** add Cobeli--Zaharescu,
Cobeli--Prunescu--Zaharescu, the X01 proof spike, and the P132--P136 hostile
kill.  This repairs provenance but cannot change the KILL verdict.

## Final decision

**KILL / ARCHIVE ONLY / HOLD_EXTERNAL.**  The theorem package is correct, but
it has zero new internal theorem mass because a strictly stronger proof of
the identical map is already present in the killed archive.  No paper should
be drafted and DDI must not remain a fallback candidate.
