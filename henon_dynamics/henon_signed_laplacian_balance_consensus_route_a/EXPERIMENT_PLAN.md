# Exact validation plan

| Claim | Proof owner | Exact regression | Mutation target |
|---|---|---|---|
| balance/kernel | quadratic form | every component, `n<=4` | corrupt nullity |
| projector/limit | spectral theorem | stored switches | promote directed case |
| exact rate | orthogonal diagonalization | characteristic polynomials | erase boundary |
| all principal minors | Cauchy–Binet | 11,894 root sets | change minor |
| full characteristic polynomial | sum over roots | 760 polynomials | change coefficient |
| factor 4 | negative-unicycle determinant | bridge-triangle witness | tree-only cofactor |

The producer enumerates ternary edge states `absent,+,-` for every labelled
simple graph on one through four vertices.  For each graph it constructs every
principal minor and independently sums admissible rooted pseudoforests.  The
checker imports no producer code: SymPy reconstructs all matrices while a
separate forest enumerator closes the same identities.  A symbolic script
retains arbitrary positive weights on paths and positive/negative triangles.

Replay must be byte exact.  Twelve repaired-hash attacks cover source, scope,
route, schema, minor, polynomial, balance and both counterexamples; one
stale-hash attack also fails.  PDF and manifest closure use the same fixed-epoch
three-round audit as C199.
