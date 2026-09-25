# Evidence — `ASFS-SCOUT-20260914-28`

## Exact input and reproducible calculation

The definitions are those of [019](../../019-primorial-gap-recursion-control/paper.md)
and [028](../../028-primorial-wheel-fibre-carrier/paper.md):

```text
P_2=6,  W_2={1,5},                       R_2(1)=5;
P_3=30, W_3={1,7,11,13,17,19,23,29},     R_3(1)=7.
```

Under reduction modulo six,
`rho_(3,2)(R_3(1))=7 mod 6=1`, while
`R_2(rho_(3,2)(1))=R_2(1)=5`.

This finite counterexample needs no cutoff, external prime table, fitted
parameter, prime-log clock, or zero data.

## Related controls

- [020](../../020-wheel-event-dichotomy/paper.md): cyclic local wheels do not
  repair advancing stage events.
- [026](../../026-sieve-natural-extension-obstruction/paper.md): a formal
  natural extension changes the one-sided chronology owner.
- [032](../../032-primorial-gap-suspension-flow/paper.md): its packet carrier
  is distinct and its orbit/zeta data cannot transfer here.
