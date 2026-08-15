# Paper 36 preregistration — SD-C38

## 1. Frozen question and verdict rule

Test the source-derived Cayley-chain cancellation for

```text
M_r=<u,v | vu=u^r v>+,  r>=2,
```

on one uninduced cyclically nonbacktracking affine edge shift with the original
unit generator-step marker.

A positive decision would require all of the following: every backtrack and
affine relation factor is removed; a nonzero source-natural primitive sector
survives; the unit marker descends coefficientwise as a free `z`-germ; one
same-object operator owns the claimed determinant; and the mechanism fails
matched generic presentations. Failure of any item closes the candidate.

## 2. Frozen family and data split

- Main family: `r=2,3,4,5`; baseline `r=4`.
- Balanced control: `r=1`.
- Infinite word cutoff: all words of lengths `0,...,12` on the same four
  oriented letters.
- Free control: the free group on those letters.
- Finite controls: `(r,q,t)=(1,4,3),(2,3,2),(3,4,2),(4,5,2),(4,7,3),`
  `(5,6,2)`.
- Damping audit: `theta=1/2`, with the theorem proved for every
  `0<theta<1`.

The source layer may construct presentation arithmetic, normal forms,
relation words, finite semidirect actions, and source-coordinate damping. The
evaluator must independently compute ranks, boundary compositions, trace
coefficients, primitive/cyclic reductions, graded controls, and decisions.
Target labels, primes, factorization, zeta zeros, and fitted coefficients are
forbidden from both layers.

## 3. Frozen symbolic and chain objects

1. Build the positive right Cayley graph of `M_r`.
2. Add distinct formal reverse arcs.
3. Use the oriented-edge Hashimoto transition with immediate reversals
   forbidden, including at the cyclic join.
4. Count one original oriented edge by each factor of the free marker `z`.
5. Attach at every vertex the source relation cell comparing `vu` and
   `u^r v`.
6. Compare path homotopy and `H_1=ker(partial_1)/im(partial_2)` with the
   unquotiented damped operator

   ```text
   T_(r,theta)=D_theta H_r D_theta,
   d_theta(e)=theta^(1+b(e)+k(e)).
   ```

No induced system, support projection, or finite quotient may replace the
infinite source.

## 4. Preregistered exact tests

1. Evaluate `v u bar(v) bar(u)^r` exactly in the enveloping affine group.
2. Count identity words through length `12` for `r=2,3,4,5`.
3. Subtract free-group identity-word counts on the same alphabet.
4. Verify that the first excess occurs exactly at length `r+3`.
5. Compare relation-side lengths `2` and `r+1`; verify the balanced `r=1`
   control.
6. Construct exact rational cellular boundary matrices on each finite
   semidirect control.
7. Independently verify `partial_1 partial_2=0` for affine-only and complete
   presentation cells.
8. Compute cycle dimension and `H_1` before cells, after affine cells, and
   after complete presentation cells.
9. Evaluate the scalar chain-supertrace multiplier and sampled powers through
   length `12`.
10. Run the full scientific payload twice in process and require canonical
    byte equality; repeat from a cold process with `PYTHONHASHSEED=0`.

## 5. Frozen expected theorem checks

- Prove contractibility of the infinite Cayley complex independently of the
  finite audit.
- Prove marker non-descent from `(r-1)deg(u)=0` independently of enumeration.
- Prove trace-class ownership of `T_(r,theta)` from source-coordinate damping
  and the trace-ideal property.
- Prove a strictly positive relation contribution
  `Tr(T^(r+3)) >= (r+3)theta^(2S_r)` with
  `S_r=r(r+1)/2+2r+5`.
- Prove the all-orders generic identity
  `Str(A_tilde^n)=(1-2+1)tau(A^n)=0`.

Finite enumeration may support but may not replace any of these proofs.

## 6. Frozen acceptance and stop rules

The candidate is rejected if any of the following occurs:

- complete relation filling yields no nonzero recurrent class;
- the unit generator marker fails to descend;
- a prequotient relation coefficient remains positive while the quotient
  ledger is empty;
- the proposed graded cancellation works for arbitrary two-generator
  one-relator presentations; or
- the argument requires `z=1`, first return, a KMS/GNS slice, a boundary or
  terminal projector, a prime basis, finite-quotient substitution, target-zero
  data, or Route B.

The strict decision schema is frozen as

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

## 7. Frozen prototype and provenance

Prototype directory:

```text
/tmp/paper36_exact_prototype/
```

Canonical command:

```text
PYTHONHASHSEED=0 python3 run_exact.py
```

The completed prototype passes `33/33` assertions. Its canonical scientific
payload is `results/scientific_results.json`, SHA-256
`499b1a5b0647e9a9999dbfdfc881a8edc0877875102d91607c10e041f69f5221`.
Environment-bearing metadata must remain separate from that scientific
payload.

The frozen research package is `/tmp/paper36_research_package.md`, SHA-256
`d29255f9eda598b780aa79165f0dcce6913880dcfa0b9ce5d370c1c43ffbd299`.
No authority experiment ledger, Route card, manifest, or Git hash is
preregistered here; those are downstream integration artifacts.
