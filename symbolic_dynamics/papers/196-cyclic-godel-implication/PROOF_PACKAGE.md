# Proof package — P196

## Frozen assumptions

- `q >= 2`, alphabet `A_q={0,...,M}` with `M=q-1`.
- `m >= 1`; indices are cyclic.
- Gödel implication is `M` for `a<=b` and `b` for `a>b`.
- Updates are synchronous.

## Dependency graph

1. Direct coordinate inequalities show `T(A_q^m)` lies in `L`.
2. The defining inequality of `L` shows `T|L=S`; shift invariance supplies
   surjectivity onto `L`.
3. Since every periodic state lies in the image, item 2 gives all clocks and
   periods.
4. Closed walks in `A[a,b]=1{b=M or a>b}` count `L`; repetition gives all
   iterate-fixed counts and Möbius inversion gives exact cycles.
5. Cyclic nontop sites fix one source coordinate per gap. Top outputs give a
   weak chain and the next nontop output gives one terminal strict inequality.
   Stars-and-bars minus the violating chains yields each factor.

## Boundary audit

- `m=1`: the image is `{M}` and its fibre has size `q`.
- all-top target: cyclic weak inequalities force a constant source.
- adjacent nontop sites: `d=1`; the factor is one precisely for the strict
  descent already required by the image language.
- outside-image targets: fibre zero by the image theorem.
- `t>=1`: `T^t=S^(t-1)T`, so higher fibres are rotated one-step fibres.

## Independent falsifiers

The verifier constructs the map literally, rather than using any theorem
formula. It compares the enumerated image with the language, direct fibres
with the product, iterate-fixed counts with matrix traces, and trace powers
with the characteristic recurrence. It includes the `q=3` case that killed
the incorrect tribonacci-style characteristic polynomial.

## Limits

No result is claimed for asynchronous schedules, open boundaries, other
residua, random updates, entropy limits, or logical completeness. A bounded
owner search cannot establish novelty or freedom to operate.
