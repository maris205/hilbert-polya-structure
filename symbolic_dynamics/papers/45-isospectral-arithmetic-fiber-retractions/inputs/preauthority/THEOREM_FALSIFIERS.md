# Theorem falsifiers and stop rules

## Decisive mathematical falsifiers

| Claimed component | Decisive falsifier | Required action |
|---|---|---|
| saturated fiber | find \(n\) with \(\tau_h(n)=m\) whose extra exponent occurs outside \(J_h(m)\), or omit a lawful extra exponent inside it | reject all \(S\) block formulas |
| modulo fiber | find \(\omega_h(n)=m\) with \(n/m\) not an exact \(h\)th power | reject all \(M\) block formulas |
| \(S\) existence wall | a bounded block at \(\sigma\le0\), or unbounded block at some \(\sigma>0\) | reject the phase diagram |
| \(M\) existence wall | convergence of \(\sum_a a^{-h\sigma}\) at \(h\sigma\le1\), or divergence above it | reject the phase diagram |
| Schatten powers | convergence at \(k\sigma q=2\), or divergence at a strict point above two | reject the ideal theorem |
| common spectrum | a nonzero block eigenvalue other than \(m^{-s/2}\), or different algebraic multiplicity between the pair | reject the cyclic ledger |
| common trace | a legal trace coefficient not equal to \(\zeta(ks/2)/\zeta(hks/2)\) | reject traces and determinants |
| saturated similarity iff | uniformly bounded saturated Riesz idempotents at \(\sigma\le1\), or unbounded ones at \(\sigma>1\) | reject similarity and maximal order |
| modulo similarity | an unbounded modulo Riesz norm at some \(\sigma>1/h\) | reject modulo similarity |
| exact primorial maximum | an \(m\le x\) with projection norm exceeding the largest admissible saturated primorial | reject maximal order |
| Tauberian strip | a noncancelled local term preventing convergence for \(\Re z>\max(1/h,(1-\sigma)/(h-1))\) | place Weyl theorem on HOLD |
| Tauberian residue | \(G_{h,\sigma}(1)\) differs from the displayed \(C_{h,\sigma}\) | reject saturated Weyl constant |
| positive Tauberian step | generalized weights fail local finiteness or the counting measure is not nondecreasing | reject Wiener--Ikehara use |
| modulo Weyl constant | \(h\)-free counting produces a constant other than \(D_{h,\sigma}\) | reject modulo Weyl law |
| crossover | any \(h\ge2\) with \(C_{h,1}\ne1\) or \(D_{h,1}\ne1\) | reject the corrected package |
| commutator block | rank-one direct calculation does not yield two singular values \(\rho^2\sqrt{1-a^2/\rho^2}\) | reject commutator theorem |
| \(h=2\) necessity | the fixed-prime/second-saturated-prime family fails to force divergence at \(\sigma q\le1\) | reject the \(h=2\) endpoint |
| \(h=2\) Euler control | either Euler product is not separately convergent for \(\sigma>1/2\), or its difference is not the Hilbert--Schmidt sum | reject the explicit control |

## Strict endpoint mutations

Every one of the following is a deliberate falsifying mutation and must be
rejected:

1. replace \(\sigma>0\) for \(S\) by \(\sigma\ge0\);
2. replace \(\sigma>1/h\) for \(M\) by \(\sigma\ge1/h\);
3. replace \(k\sigma q>2\) by \(k\sigma q\ge2\);
4. omit \(\sigma>1/h\) from the statement for \(M^k\);
5. allow an ordinary trace at \(k\sigma=2\);
6. allow an order-\(r\) determinant when \(r\sigma=2\);
7. replace saturated similarity \(\sigma>1\) by \(\sigma\ge1\);
8. replace \(\sigma q>1\) for a commutator by \(\sigma q\ge1\);
9. use an \(h\ge3\) exponent-one necessity witness at \(h=2\);
10. assert \(C_{h,\sigma}\ne D_{h,\sigma}\) at every parameter;
11. change the mandatory row \(C_{h,1}=D_{h,1}=1\);
12. weaken the Tauberian strip or delete positivity, local uniform
    convergence, the simple-pole statement, or the residue calculation.

Any accepted endpoint mutation is a scientific failure, not a cosmetic
issue.

## Type and object mutations

The following must fail schema validation before evaluation:

- \(h=1\), nonintegral \(h\), \(k=0\), \(q\le0\), or basis index zero;
- a claimed block label \(m\notin\mathcal F_h\);
- defining \(J_h(m)\) as all prime divisors rather than exponent-\(h-1\)
  divisors;
- swapping \(\tau_h\) and \(\omega_h\) while retaining the old formulas;
- using \(\sigma=s\) for nonreal \(s\);
- changing \(n^{-s/2}\) to \(m^{-s/2}\) before summing a fiber;
- treating a singular value as an eigenvalue or a Riesz norm as a
  probability;
- serializing \(m^{-s/2}\) as a rational `complexExact` object, using a
  nonpositive base, a nonreduced exponent, or any branch other than
  `REAL_LOG_POSITIVE_BASE`;
- accepting a JSON number (`6.0`, `6e0`, or a rational component `1.0`), a
  Boolean, a plus sign, leading zero, `-0`, or zero denominator where a
  canonical integer string is required;
- constructing an object before duplicate-member detection, applying
  last-win to duplicate `base`, rejecting reordered unique keys instead of
  RFC8785-canonicalizing them, or accepting mismatched stored JCS/hash;
- treating a finite truncated block as the infinite block;
- treating zero eigenvalues from block kernels as additional nonzero cyclic
  atoms;
- using a noninteger regularization order in the frozen determinant
  convention.

## Source and ownership falsifiers

STOP_DUPLICATE applies if a verified primary source proves the materially
same all-\(h\) paired classification, including the similarity and
Weyl/maximal-order core, or a stronger theorem that makes it immediate.

HOLD_SOURCE applies if any of the following occurs:

- a frozen Phase-2 hash does not verify;
- a DOI resolves to a different work, author list, or bibliographic object;
- generic Luan--Khoi or Carlson results are presented as P45 novelty;
- Abanin--Mannanikov's quasi-Banach weighted-composition extension is
  omitted or presented as P45 novelty;
- power-free-part terminology or the \(h\)-free map is presented as new;
- Papers 27--30 or P43 are omitted from the subtraction ledger;
- the result is described as completing an unfilled P27 adjoint obligation;
- the bounded exact-prior-art search is described as proof of priority.

The \(h=2\) saturated radical operator alone is permanently
STOP_GENERIC_SPECIALIZATION unless a genuinely new theorem beyond this
package is supplied.

## Evaluator-independence falsifiers

The two evaluators cease to be independent if they share any production
source file, helper module, generated case expansion, seed, fixture,
serialized intermediate, expected-value table, copied formula
implementation, or postprocessed result payload. They may share only the
immutable EXPERIMENT_CONTRACT.json and MUTATION_REGISTRY.json, their two
strict schemas, and the neutral case IDs/raw values therein. Each
implementation must independently parse and expand the registered cases.

Additional failures are:

- either evaluator reads the other's directory or output before sealing its
  own output;
- a comparator silently coerces Boolean, integer, rational, string, and
  floating-point types;
- a numeric tolerance is selected after outputs are observed;
- one evaluator's result is used as the other's oracle;
- exact fields disagree, numerical certified intervals do not overlap, or
  either method identity/coverage ledger is missing;
- finite experiments are promoted to proofs of an endpoint or Tauberian
  continuation.

Any independence failure puts the package on HOLD even when numbers agree.

## Free-UFD firewall falsifier

Let \(\mathfrak M\) be the free commutative monoid on formal atoms
\(a_1,a_2,\ldots\), assign \(N(a_j)=p_j\), and repeat the exponent
definitions with \(a_j\) in place of \(p_j\). The clone must reproduce the
structural fibers, thresholds, Euler products, similarity wall, Weyl
constants, maximal order, and commutator wall after relabeling.

- If it reproduces them, rational-prime selectivity is refuted, as intended.
- If it does not, the evaluator must locate the hidden use of prime
  arithmetic before any positive claim proceeds.
- Calling successful replication evidence for rational-prime emergence is a
  firewall failure.

## Route falsifiers

- A nontrivial same-object rational-prime primitive ledger would require a
  new A1 evaluation.
- A completed same-ledger determinant with a natural functional equation
  would require a new A3 evaluation.
- A fixed self-adjoint operator owning a specified completed target divisor
  would require a new A4 evaluation.
- Equality of the present regularized determinants changes none of those
  verdicts.

ROUTE_EXPECTATION.yaml is an expectation only. Treating it as an evaluated
Route record is an integrity failure.

GO_EVALUATED, HOLD_REPAIR, STOP_FALSE, STOP_DUPLICATE, and
STOP_GENERIC_SPECIALIZATION are external scientific/publication
dispositions. They are not Route terminal codes. Only strict Route
validators may emit the A0--A4 tuple, overall expectation, and Route-B
fields.

## Exact mutation outcome contract

MUTATION_REGISTRY.json is exhaustive for this freeze. Each atomic row fixes
one stable ID, exact target artifact and executable pointer/typed operation,
semantic domain, complete designated-consumer set, exact rejection code,
and exit 2. Pointer operations must resolve under RFC6901 and match
`value_from` in both JSON type and value before mutation. Precondition
failure is HARNESS_ERROR:MUTATION_PRECONDITION_FAILED. The only legal
outcomes are ACCEPT, REJECT, and HARNESS_ERROR. A kill requires every and
only the designated consumers to return REJECT with the exact row code and
exit 2. Any missing, extra, or duplicate consumer; ACCEPT or zero exit;
wrong code; HARNESS_ERROR; parse/schema exception; timeout; malformed
payload; or unclassified nonzero exit is a survivor and forces HOLD.

In particular M050 must reject treating a singular value as an eigenvalue,
M051 must reject treating a Riesz-projection norm as a probability, and
M052 must reject a shared expected-value table. These are separate from the
source-sharing and oracle-use mutations.

M053--M054 reject the rational-complex eigenvalue retype and wrong logarithm
branch. M055--M067 close the infinite-coverage gate: B/P missing, extra,
reordered, undeclared, or wrong-owner cases; a nonempty A infinite ledger;
a changed canonical set hash; or broken per-case hash/verdict closure are
all exact-code rejections. Schema or semantic acceptance of
`INF-UNDECLARED` is a decisive harness failure.

M068--M075 reject floating/Boolean AST scalars, duplicate-member last-win,
false rejection of harmless raw-key reordering, noncanonical stored JCS,
and failure to recompute the AST JCS hash. The reordered positive fixture
must produce exactly the frozen ordered JCS bytes/hash for that same AST;
it is not a rejection case.

## Integrity stop rules

The package is on HOLD if:

- any file outside the declared temporary package root is written by this
  stage;
- any authority, mirror, root manifest, candidate registry, or Git state is
  mutated;
- SHA256SUMS.txt is unsorted, includes itself, omits a requested file, or
  fails verification;
- an experiment output or claimed result is added to this result-free
  package;
- an absolute path is used as a future portable artifact dependency rather
  than as a clearly labeled current provenance pointer;
- trailing whitespace, unresolved placeholders in theorem statements, or
  contradictory endpoint tables remain.

## Exact disposition

GO_WITH_FIREWALL requires every mathematical statement above to survive,
both independent evaluators to pass the later authorized plan, all
applicable mutations to reject, and the source audit to remain collision
free. HOLD means a repairable proof, source, evaluator, or integrity gap.
STOP means the all-\(h\) residual theorem is false, exactly absorbed by prior
art, or reduced to the already rejected \(h=2\) specialization.
