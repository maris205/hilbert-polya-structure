# HCS-C52 experiment tracker

Status: **B0--B2 release candidate; all exact gates pass**

This tracker separates the locked C52 B0--B2 theorem from successor gates.
The independent lane reports \(16/16\) semantic gates and \(44/44\)
targeted mutation/transaction tests passing.  Frozen hashes are recorded in
the release reports rather than duplicated in theorem-bearing prose.

## B0--B2 theorem gates

| Gate | Mathematical target | Exact control required | Current status |
|---|---|---|---|
| B0 | Complete projective monomial source stabilizer | Exhaust all \(16\) eight-cycle support permutations and normalized \(\mathbf F_3^7\) phases; verify equation scalars and projective equality | producer/checker pass |
| B0-group | Identify the order-\(24\) group | Verify \(r^{12}=s^2=1\), \(srs=r^{-1}\), distinct \(r^k,sr^k\), and the element-order spectrum | producer/checker pass |
| B1-Chow | Construct \(\pi_{2i},\pi_5,e_G\) and prove all Chow compositions | Symbolically replay decomposable-correspondence composition, graph multiplication, transposition, and commutation with \(h\) | proof and symbolic checker pass |
| B1-residue | Build the projective Cayley action | Verify \(F(M_gx)=A_gF(x)\), include \(\det M_g/\det A_g\), and repeat with scalar lift \(\lambda=2\) | scalar-lift and mutation controls pass |
| B2-character | Recover the exact \(R_{2,-3}\) character | Obtain ambient dimension \(164\), relation rank \(81\), quotient rank \(83\), all rotation/reflection traces, and irreducible multiplicities | independent quotient replay pass |
| B2-Hodge | Prove rank \(10/158\) and the two Hodge ledgers | Check invariant multiplicities in \(R_{1,-3}\), \(R_{2,-3}\), conjugate pieces, and total rank \(168\) | proof and exact gate pass |
| B2-no-go | Prove sharp graph-algebra lower bound | Verify the augmentation action on every trivial copy and that \(e_G\) attains rank \(10\) | proof and exact gate pass |

## Required negative controls

The independent test suite must reject at least the following semantic
mutations:

1. replacing the closing coefficient \(\rho\) by \(1\);
2. admitting an odd rotation or an even reflection without solving the
   phase equations;
3. declaring the dihedral group to have order \(12\);
4. dropping projective phase normalization;
5. omitting the residue multiplier \(\det(M_g)/\det(A_g)\);
6. changing the scalar lift without compensating the Cayley action;
7. changing the Jacobian relation rank \(81\);
8. changing any row of the rotation or reflection trace ledger;
9. confusing irreducible multiplicity with representation dimension;
10. claiming rank \(2\) from the trivial character alone;
11. treating \(\pi_5\) as an MCK theorem; and
12. extending the augmentation obstruction beyond the graph algebra.

## Release evidence policy

The theorem-bearing producer must emit canonical exact data for the phase
system, group table or equivalent presentation checks, Cayley quotient,
residue twist, character inner products, Hodge ranks, and augmentation
bound.  The checker must reconstruct the mathematical consequences from
the frozen source and fail closed on missing, mistyped, or extra semantic
fields.  Merely comparing a producer-supplied verdict string is
insufficient.

The Markdown proof remains theorem-bearing for the Chow composition and
scope statements.  The machine checker need not implement a Chow ring,
but it must verify the finite algebra that enters those identities and
must not be described as independently proving facts outside its schema.

## Deferred gates: not C52

| Gate | Reason for deferral | Owner paper |
|---|---|---|
| B3 | Full rank-\(10\) local Frobenius polynomials and factorization/irreducibility controls are a new arithmetic experiment | C53 |
| B4 | Incidence correspondences outside \(\mathbf Q[G]\), coniveau tests, or an actual low-rank motivic refinement require new geometry | C53 or later |

No B3/B4 result may be silently folded into the C52 release certificate.

## Stop/go decision

The mathematical gate is **GO, amber**: B0--B2 give a
theorem-sized positive projector and a theorem-sized negative optimum.
The release gate is **PASS**: the exact producer, independent checker,
mutation suite, paper audit, Route-A archive, and full manifest are frozen.
