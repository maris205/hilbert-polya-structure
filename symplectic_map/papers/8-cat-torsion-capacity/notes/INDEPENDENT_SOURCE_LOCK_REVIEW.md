# Independent Source-Lock Review

Review date: 2026-08-14 UTC.

Verdict: **PASS**.

This is a read-only mathematical and source-design audit of Paper 8 at
source-lock v1.  It is not a deployment review, registered execution,
result review, or manuscript review.  No candidate code was run, no period
above twelve was computed, and no network, external prime table, generated
prime target array, or Riemann-zero data was accessed.

## Frozen authority and binding checks

The reviewed source-lock is

`87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce`.

All six local design bindings reproduce exactly:

| Artifact | SHA-256 |
|---|---|
| `README.md` | `3386d710b26900350fe963c2c040fdce569e6ebd3a961cef6c54531bafb5e880` |
| `notes/RESEARCH_QUESTION.md` | `8f10e2eb2485351e93a58948bfa15dab8584cd549d2998836fcecff5487ca4d5` |
| `notes/NOVELTY_AUDIT.md` | `dcc30076f31099db5fb960284374819c39fdbf5f9a5c9348c19bf5ed92a22212` |
| `notes/PROOF_PACKAGE.md` | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| `experiments/EXPERIMENT_PLAN.md` | `a45fd3c68667e4d93c80f863b724df5d95714a45bb9b8138c896ce3d52858081` |
| `experiments/EXPERIMENT_TRACKER.md` | `b977106d20039a5de31db31969ead23829d4dab058d9c7f4c03b1b96e54748f9` |

The declared Paper 6 source/proof/final-PDF bindings, Paper 7
source/proof/final-PDF bindings, and Route-A evaluator binding also reproduce
exactly.  The JSON parses strictly, the frozen matrix has trace three and
determinant one, and the determinant sign convention is consistently
`Delta_n=det(A^n-I)=2-tr(A^n)`.

## Theorem and proof audit

1. **General positive-trace case: PASS.**  For trace greater than two, the
   expanding eigenvalue is a nontrivial positive quadratic algebraic unit of
   norm one, and
   `N(alpha^n-1)=det(M^n-I)`.  These are the hypotheses actually needed from
   Flatters; no splitting, semisimplicity, unramified-prime, or kernel-rank-one
   assumption has been inserted.  A rational primitive divisor makes the
   finite-field kernel nonzero, and every nonzero kernel vector has exact
   period, rather than merely period dividing, `n`.  The stated cycle count
   `(p^r-1)/n` follows because all those vectors lie in disjoint exact
   `n`-cycles.

2. **Negative-trace extension: PASS.**  Writing `B=-M` reduces the imported
   theorem only to a positive unit; the conversion back to `M` is correctly
   presented as Paper 8's separate parity lemma.  The three branches exhaust
   every `n>12`:

   - for odd `n`, a primitive divisor at index `2n` makes `B^n-I`
     invertible, so an exact `B`-period-`2n` kernel vector satisfies
     `B^n v=-v`; characteristic two would contradict that exact period, and
     the resulting `M`-period is exactly `n`;
   - for `4|n`, a primitive divisor at index `n` remains exact for `M`; a
     hypothetical smaller odd return would imply `n|2m`, which is impossible
     by the two-adic valuation;
   - for `n=2k` with odd `k>=7`, the primitive index is `k`, not `n`.
     Flatters Theorem 1.4 covers `k>12`, while the complete Theorem 3.1
     classification supplies `k=7,9,11`.  The primitive prime cannot be two:
     modulo two an orbit of a nonzero vector has length in `{1,2,3}`, and an
     odd `k>=7` would force an earlier determinant divisor.  Thus
     `M^k v=-v!=v`, and exact `B`-period `k` converts to exact `M`-period
     `2k`.

   This also checks the explicitly forbidden half-period shortcut in the
   `n=2 mod 4` branch.  Signs, the prime two, ramification, nonzero-vector,
   exact-versus-dividing-period, and repeated-divisor edge cases introduce no
   gap.

3. **Frozen standard-cat classification: PASS.**  The twelve determinant
   values, signs, factorizations, and first primitive factors are mutually
   consistent.  Primitive factors cover `n=2,3,4,5,7,8,9,11`, and the
   general theorem covers every `n>12`.  At `p=5`, the exact identity
   `A=-I+N`, with nonzero rank-one `N` and `N^2=0`, gives four nonzero kernel
   vectors of period two and twenty nonkernel vectors of exact period ten,
   hence two period-ten cycles.  The complete determinant supports at six
   and twelve reduce respectively to `{2,5}` and `{2,3,5}`; the declared
   modulo-two, modulo-three, and modulo-five classifications exclude both
   periods.  Together with `det(A-I)=-1`, this proves the exact exception set
   `{1,6,12}`.  The absent period twelve also makes the strict universal
   cutoff twelve sharp.

4. **Order-clock obstruction: PASS.**  Periodic points equal torus torsion;
   unimodularity preserves exact additive order; `(1/m,0)` realizes every
   positive integer order.  For an order-`m` torsion point and
   `N_k=k*m+1`, the perturbation `x+(1/N_k,0)` has exact order `m*N_k` and
   tends to `x`.  This proves relative-neighborhood unboundedness and
   discontinuity at every torsion point, and consequently rules out any
   continuous, locally bounded, or Holder extension.  The source correctly
   keeps this global group label separate from a local point potential:
   `S_n L=nL`, repeated traversal scales the sum rather than the raw label,
   while `D(T_A^n)=A^n` and its unstable logarithm `n log(alpha)` are
   independent of the carrier prime.

## Cross-document contract and execution boundary

The README, research question, proof package, novelty audit, source JSON,
experiment plan, and tracker agree on theorem scope, the three negative-trace
indices, the exact standard-cat exception set, the period-ten Jordan repair,
the all-integer/nonlocal clock obstruction, and the
`A0_FAIL_PROVES_TOO_MUCH` interpretation.  The novelty record assigns the
primitive-divisor theorem and prime-lattice background to prior work, uses
only scoped synthesis language, and makes no priority claim.

Controls K001--K008 cover determinant sign, primitive transfer,
nonprimitive period ten, complete exclusions, all-integer range, local
unboundedness, monodromy blindness, and negative-trace parity.  The run order
keeps the all-period tail proof-only and computation at `n<=12`.  Stop rules
fail closed on stale authority, theorem or dual-engine disagreement, any
carrier at six or twelve, loss of the period-ten repair, an invalid parity
branch, or forbidden scope expansion.  The allowed/forbidden-data lists and
mandatory nonclaims consistently prohibit external prime/zero targets,
fitting, post-hoc selection, transfer/Fredholm or quantum evidence, and any
Route-A A1--A4 or Route-B opening.

At review time the Paper 8 directory contains only the seven frozen design
documents plus this independent review: there is no candidate code, result
artifact, deployment authority, or registered claim.  Every tracker entry is
`TODO`; the source lock records zero candidate runs, zero registered exact
audits, zero target matches, zero generated prime arrays, and zero
prime/zero-data access.  The formal gate still requires an independent
code-review `DEPLOYMENT_PASS` bound to this source-lock hash and the future
code-tree hash before any registered audit.

## Blockers

None.  Source-lock v1 is mathematically coherent and internally bound for
implementation authoring and later independent deployment review.  This PASS
does not itself authorize registered execution.
