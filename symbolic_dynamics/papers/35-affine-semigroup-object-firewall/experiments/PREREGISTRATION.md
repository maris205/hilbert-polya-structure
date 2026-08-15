# Authority exact-audit preregistration — SD-C37

**Freeze status:** written after the root `SOURCE_LOCK.md` and
`PREREGISTRATION.md`, and before any authority result artifact.

## 1. Authority and bridge order

The authority source of truth is the Paper 35 scaffold. The read-only bridge
input is `/tmp/paper35_exact_prototype/`; its algorithms and retained
counterexamples may be adapted, but its serialized outputs do not override the
authority source lock.

Two bridge differences are frozen before execution:

1. The prototype used the auxiliary strict height `b+k`. The authority ledger
   uses the source-locked height
   `h_r(b,k)=b+r^k`, so a U edge has increment `r^k` and a V edge has increment
   `(r-1)r^k`.
2. The prototype used rational diagnostic edge weights. The authority primary
   two-generator operator is the source-locked unweighted `A_+=S+T`; all
   primary operator and relation certificates therefore use U/V weight one.

These changes preserve the finite populations but require fresh source and
independent-evaluator reconstruction. They are not post-result repairs.

## 2. Frozen scientific protocol

- baseline `r=4`; controls `r=2,3,5`;
- height origins `0<=b<=12`, `0<=k<=4`;
- formal symmetrization of every retained positive edge;
- exhaustive words in `{U+,V+,U-,V-}` through length eight at bases `(0,0)`
  and `(2,1)`;
- affine relation word `V+ U+ V- (U-)^r`, expected length `r+3`;
- generic dilation commutation pairs `(2,3),(3,5),(4,6),(4,9)`;
- twelve exact orthogonal witness rows for each finite-degree operator class;
- quotients `q=1,...,12`, retaining both the affine relation and `U_q^q`;
- exact diagonal fixtures for `beta=2,3`, cutoff twelve, log degrees one
  through four;
- evaluator-only prime-Fock control through prime cutoff nineteen and particle
  degree six;
- composite and mutated arbitrary one-relator controls;
- signed scalar, nilpotent matrix, traceless invertible matrix, and open
  groupoid boundaries;
- the full `N_0 semidirect N^times` unweighted adjacency is theorem-only and
  receives no finite census.

All decisive computations use integers or `fractions.Fraction`. No target
zero, fitted coefficient, stochastic sample, network call, GPU, Route B, or
floating tolerance is allowed.

## 3. Physical source/evaluator separation

`code/source_core.py` and `code/generate_artifacts.py` may use only neutral
affine multiplication, source-natural generators, exact words, finite
quotients, exact matrices, and diagonal integer-energy fixtures. They may not
contain primality/factorization classifiers, accepted support, target zeros,
or imports from the evaluator.

`code/independent_evaluator.py` must not import either source file. It must
recompute every decisive height, word, quotient, operator, and determinant
identity from serialized artifacts. Prime labels enter only in this evaluator,
after `source_manifest.json` freezes the neutral source artifacts.

## 4. Predeclared success and correction gates

1. All 520 frozen positive edges satisfy the authority height increments and
   each induced window is a DAG.
2. All 520 formal reverse-edge pairs give primitive two-step backtracks and
   are Hashimoto-forbidden.
3. All eight `r`/base affine witnesses are admissible, primitive,
   cyclically nonbacktracking, and length `r+3`; exhaustive census and
   independent reconstruction agree exactly.
4. Generic commutation and mutated one-relator controls retain reduced
   relation cycles without arithmetic acceptance labels.
5. Finite witness families verify exact degree bounds and uniformly nonzero
   image norms, but noncompactness remains theorem-owned.
6. Every frozen quotient preserves the labelled relation and adds `U_q^q`;
   the `(r,q)=(2,2)` degeneration is retained.
7. For each diagonal fixture,
   `[z^m](-log det(I-zD_beta))=Tr(D_beta^m)/m`; the trace, determinant germ,
   reciprocal determinant, and `z=1` specialization stay distinct.
8. Prime-Fock `z` counts bosonic occupation and is evaluator-only; it is not
   the original generator-step marker.
9. Signed/matrix controls never become claims of literal primitive-word
   deletion; the groupoid same-object question remains open.
10. The Cuntz zero loop, identity loop, quotient cycles, small-modulus
    collapse, trace/determinant mismatch, and first-trace/all-orders mismatch
    remain explicit corrections.

Any unexpected mismatch fails the authority suite.

## 5. Strict Route-A v0.2 lock

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall_verdict: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

Every target-zero and root-count field, including A2 stability fields, must be
a string beginning `not_applicable;`. The three provenance fields
`source_commit`, `code_commit`, and `source_lock.code_commit` must be exactly
`PENDING_FIRST_ARTIFACT_COMMIT`. Mixed or partial provenance is forbidden.

## 6. Reproducibility and seal

The scientific pipeline runs in three distinct initially empty directories:
fresh A, fresh B, and cache-free cold start C. Their complete scientific
artifact maps must be byte-identical before A is published. Metadata is added
afterward without altering a scientific byte.

The final suite must certify exact result inventory, strict Route schema,
source separation, research-document hashes, UTF-8, LF-only text, exactly one
terminal LF, no trailing whitespace, no control bytes, no symlink, no cache,
sorted SHA-256, freeze/audit idempotence, and metadata-seal stability.

No Git or mirror operation is authorized in this stage. The paired pending
provenance is intentionally left for a future root-owned metadata-only seal.
