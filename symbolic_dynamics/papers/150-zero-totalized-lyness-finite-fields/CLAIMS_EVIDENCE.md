# P150 claims--evidence ledger

Status: `ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL`. The P150 entry of
`FINAL_THEOREM_CONTRACTS.md` is an absolute claim ceiling. Exact enumeration
is counterexample pressure and never the proof of an all-parameter claim.

| ID | Exact claim | Formal support | Executable support | Ownership / limitation | Status |
|---|---|---|---|---|---|
| `P150-C1` | `F_q^2` is the disjoint union of the generic locus, the coordinate axes, and the three displayed exceptional layers, of sizes `(q-2)(q-3)`, `2q-1`, `q-1`, `q-2`, `q-2`. | Stratification theorem: zero-coordinate case followed by the ordered tests `y=-1`, `x=-1`, `x+y+1=0`. | Set construction, pairwise disjointness, pointwise unique membership, coverage, and all sizes. | Only this literal all-affine boundary split is in scope. | Proved; controls pass. |
| `P150-C2` | The recurrent set is the generic locus plus the axes; its size is `q^2-3q+5`. The three exceptional sets have exact tails one, two, and three, giving the frozen temporal polynomial and sharp maximum three. | Generic five-iterate lemma, axis lemma, and exceptional-arrow lemma. | Every state receives the predicted `(tail,period)` pair and full layer histogram. | Classical rational five-periodicity is zero credit. | Proved and sharp; controls pass. |
| `P150-C3` | There are `1+r_q` fixed points, two 2-cycles, `(q-3)/2` 4-cycles, and `((q-2)(q-3)-r_q)/5` 5-cycles. | Fixed equation; inversion orbits on `F_q^*`; five prime and `L^5=id` on the generic locus. The nonfixed generic states are a disjoint union of five-element orbits, proving integrality as well as the count. | Literal cycle extraction, exact period counts, and divisibility; boundary boxes include `q=3`, `q=5`, and extensions of characteristic five. | Cycle division and generic zeta bookkeeping are zero credit. | Proved; Review-A repair independently closed by Review B; controls pass. |
| `P150-C4` | The dynamical zeta function is the product of the four frozen factors. | Substitute the complete cycle census in the standard finite-map Euler product. | Cycle exponents and fixed-iterate shadows checked. | Artin--Mazur formalism is standard and zero credit. | Derived from proved census. |
| `P150-C5` | The fibre is `q` at `(-1,0)`, zero at `(-1,v)` for `v!=0`, and one elsewhere; `|im L|=q^2-q+1`. | Target coordinate reduction and a three-case solution of `(1+u)inv0(x)=v`. | Literal predecessor counter for every target; image and unique maximum fibre. | General rational inverse language is zero credit. | Proved; controls pass. |
| `P150-C6` | The whole exceptional component consists of the distinguished two-cycle, one depth-one leaf, and `q-2` length-three chains. | Layer arrows plus the fibre theorem exclude every additional predecessor. | Exact predecessor sets for cycle, chain, and leaf targets. | No generalization to other totalizations is claimed. | Proved complete; controls pass. |
| `P150-E1` | The paper-local audit uses exact finite-field arithmetic with no sampling, floating point, external CAS, runtime network access, or third-party package. | `verify_p150.py` source contract. | Frozen `verification_output.txt` and byte replay. | Computation establishes neither proof nor ownership. | Pass. |

## Round-2 review closure

- Hostile Review A: **0 Critical / 0 Major / 2 Minor**.  The replayable owner
  ledger plus Lyness/Kanki subtraction, and the five-orbit integrality plus
  `q=3`/characteristic-five boundary exposition, are repaired.
- Hostile Review B: **0 Critical / 0 Major / 1 Minor, REVISE**.  Every theorem,
  source, verifier, build, and visual interface passed; the sole stale
  `FINAL_QA.md` provenance Minor is repaired by the current Markdown closure.
- Post-closure unresolved findings: **0 Critical / 0 Major / 0 Minor**.
- Accepted evidence: 2,144,131 assertions; byte-identical frozen replay; 5/5
  cited references; two isolated builds byte-identical to the 5-page,
  403,358-byte current PDF; 5/5-page visual acceptance; SHA-256
  `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`.
- Root separately froze `main_round2.pdf` during this closure; a read-only
  comparison confirms that it matches the 403,358-byte current PDF byte for
  byte at the accepted SHA-256.

## Zero-credit inputs

- the classical Lyness recurrence and its five-period identity on the
  birational domain;
- Lyness's 1942 cycle observation and Kanki's distinct extended-space or
  almost-good-reduction convention for finite-field singularities;
- QRT, cluster-algebra, associahedron, and integrability interpretations;
- projective compactification and denominator handling;
- generic finite-field rational-map and elliptic-curve methods;
- elementary finite-field inversion and quadratic root counts;
- generic finite functional-graph, fixed-iterate, cycle, and zeta identities.

## Scope sentinels

- `q` is an odd prime power and the carrier is exactly the affine plane
  `F_q^2`.
- `inv0(0)=0` is part of the literal update, not a projective convention.
- Entry time means first entrance into the recurrent set.
- The generic locus is exactly
  `xy(x+1)(y+1)(x+y+1)!=0`.
- The temporal polynomial counts all `q^2` states by tail depth.
- The singular in-tree claim refers to the component of
  `(-1,0)<->(0,-1)` and is certified with the every-target fibre law.
- The root count `r_q` is left intrinsic; no uncontracted quadratic-character
  claim is needed.
- A bounded direct-owner non-hit is not novelty, priority, or clearance.
- External posting, contact, submission, and release remain unauthorized.
