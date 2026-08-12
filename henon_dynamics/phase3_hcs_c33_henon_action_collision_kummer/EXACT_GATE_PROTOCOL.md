# HCS-C33 Phase-3 exact gate protocol

## Certificate contract

Schema: `HCS-C33-PHASE3-KUMMER-1`.

Every rational is stored in reduced numerator/positive-denominator form.
Every polynomial records an ordered variable list and a unique descending
monomial ledger.  Every element of
\(K_9=\mathbb Q[A]/(P_9)\) uses the canonical basis
\(1,A,\ldots,A^8\) and one common positive denominator.

The top-level payload has exactly these branches:

- `material_passport`;
- `source_lock`;
- `conventions`;
- `derived_polynomials`;
- `node_gate`;
- `exact_period_and_nonparabolic_gate`;
- `collision_parameter_galois_gate`;
- `hill_kummer_gate`;
- `finite_prime_controls`;
- `route_a_evaluation`;
- `decisions`;
- `scope`.

Unknown or missing keys fail closed.  JSON equality is type-strict, so
booleans cannot masquerade as integers.

## Producer obligations

The producer must derive from the chronological map:

1. orbit coordinates, the exact-period marker, and fixed-factor resultant;
2. the cyclic action remainder and primitive action curve;
3. the degree-preserving \(A=6\), modulo-\(37\) irreducibility
   specializations and the birational inverse subresultant;
4. both discriminants and the coprime factor \(P_9\);
5. the collision value, quadratic branch pair, tangent cone, and branch
   slopes over \(K_9\);
6. the chronological return derivative, action Hessian, \(+1\) gate, and
   separate \(-1\) gate;
7. the symmetric Hill norm, nonmonic field-norm correction, factorization,
   and nonsquare verdict;
8. exact modular factorizations and all four finite control rows;
9. the conservative Route-A and scope decisions.

## Independent-checker obligations

The checker imports no producer module.  It independently rebuilds the
recurrence and action, decodes no unvalidated mathematical verdict, and
checks the canonical payload digest before any semantic gate.

The twelve gates are:

1. schema, conventions, type-strict passport, and payload-hash integrity;
2. source-lock integrity;
3. chronological marker and action-image reconstruction;
4. marker/action discriminants and the new Maxwell factor;
5. birational inverse and generic irreducibility;
6. the exact \(S_9\) modular proof;
7. collision-field quadratic fiber and ordinary node;
8. exact period, Hill identity, and both multiplier gates;
9. normalization-slope transversality;
10. Hill--Kummer norm, gauge contract, and nonsquare class;
11. finite-prime controls, selection rule, and post-hoc disclosure;
12. Route-A decision together with scope and claim firewalls.

A mathematical mismatch raises `GateFailure` and reports `FAIL`.  An
unexpected exception reports `ERROR`; the test suite is forbidden from
counting a checker crash as a successful mutation rejection.

## Mutation requirements

The suite attacks, at minimum:

- stale payload hashes and JSON type confusion;
- source drift;
- marker/action coefficients and the \(P_9^2\) exponent;
- modular Galois cycle types;
- the double action value and quadratic branch fiber;
- the tangent discriminant and branch slope;
- omission of the multiplier \(-1\) gate;
- the field norm and the adversarial nonsquare prime;
- post-hoc disclosure at \(p=61\);
- Route-A promotion, zeta promotion, and unknown nested fields.

## Release rule

The default runner must never rewrite the certificate, checker report, or
hash manifest.  It first verifies the manifest, regenerates both JSON
artifacts in a temporary directory, compares them byte for byte, runs the
mutation suite, and verifies the manifest again.  Refreshing is an explicit
release action only.
