# Experiment Report — SD-C30

## Outcome

The exact suite supports

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

with ROUTE_A_REJECTED, Route B locked, and no target-zero data. The strongest
gain is an honest S3/det3 strip containing the critical line and a uniquely
positive fourth-moment phase frequency. The decisive failure is that the same
motion occurs on mutated, composite-only, and generic-poset controls, while
every positive metric completion that removes the obliqueness also removes
the motion.

## Raw exact data table

| Artifact | Rows | Result |
|---|---:|---|
| source compilers | 4 | all inverse and primitive relations exact |
| finite native Gram | 43 | symmetric, nonnegative, exact; diagonals positive |
| infinite Gram formulas | 9 | all exact displayed formulas positive |
| Schatten strips | 8 | S3 is the first common strip |
| finite B2 diagnostics | 4 | all direct/Gram identities and phase flips pass |
| infinite S2 firewall | 4 | B is not S2 and B squared is not trace class |
| B4 frequencies | 7 | three unique positive theorem frequencies plus four controls |
| det3 deletion | 8 | powers 1 and 2 deleted; power 4 first visible |
| metric rigidity | 8 | full and active-only certificates pass |
| orthogonalized det3 | 4 | all characteristic and det3 factors phase-free |
| adversarial controls | 4 | native motion persists without arithmetic selectivity |
| marker ownership | 24 | all exponents equal r ell and theorem u is 1 |
| common-t samples | 12 | nongating displays only |
| route gates | 5 | frozen tuple reproduced |
| analysis comparison | 10 | zero claim-bearing failures |
| regression tests | 61 | 61/61 PASS |

These are exhaustive finite identities or exact symbolic theorem
certificates. Means, standard deviations, confidence intervals, and machine
learning performance deltas do not apply.

## Native Gram geometry and finite diagnostic

The weighted adjoint gives a symmetric Gram kernel. At eta=2, the infinite
formulas are

    G_pp = C_eta (1 + p^(-2 eta)),

    G_pq = C_eta (pq)^(-2 eta)
            / ((1+p^(-2 eta))(1+q^(-2 eta)))  for p != q.

All nine displayed prime-pair values are strictly positive. In every finite
fixture, direct matrix multiplication agrees exactly with the Gram expansion
for Tr(B squared), and a phase flip changes the value. This establishes real
motion without relying on floating point.

That finite observation is not promoted to an infinite trace claim. On the
critical line the block belongs to S_q for every q>2 but not to S_2, because
the diagonal lower bound contains the divergent prime harmonic series.
Consequently B squared is not trace class. The four-row firewall records this
scope boundary explicitly.

## Honest det3 and fourth-order motion

The reflected block has common Schatten strip

    1/q < Re(s) < 1 - 1/q.

The first integer q with a nonempty strip is q=3, so det3 is honest on
1/3 < Re(s) < 2/3. Its logarithm deletes powers one and two; odd block traces
vanish; power four is the first visible term. For each unordered atom pair,
unique factorization isolates frequency 2 log(q/p) with coefficient

    4 G_pq squared / (pq) > 0.

For (p,q)=(2,3), the exact coefficient is

    3675 / (971618 pi^8).

This is the strongest positive theorem in SD-C30: the honest regularized
determinant sees genuine phase motion. It does not by itself identify an
arithmetic spectral law.

## Positive-metric rigidity and orthogonal collapse

Writing K = Z transpose H Z, simultaneous self-adjointness of the full
primitive family forces K to be coordinate diagonal. Requiring only the
active atoms allows an arbitrary positive dormant block, but still forbids
every atom-to-dormant coupling. All eight exact metric rows verify those two
cases across the four sources.

After orthogonalization, each active atom contributes a two-by-two chiral
block whose square is p inverse times the identity. The characteristic factor
is 1-z squared/p, and the det3 factor is

    (1-z squared/p) exp(z squared/p).

All phases disappear. Thus the native geometry moves but proves too much;
the positive completion is canonical enough but spectrally static.

## Adversarial controls and marker ownership

The relation mutation promotes label 6 to a source atom. A composite-only
divisibility subposet derives atoms 4, 6, and 9. A deterministic seeded DAG
derives synthetic atoms 10, 14, and 21. Each has nonzero mixed Gram entries
and phase-dependent fourth moment, while no arithmetic selectivity is
observed. These exact controls show that pairwise obliqueness is generic.

Every one of the 24 marker rows preserves the exponent r ell(label). The main
theorem is evaluated at u=1. Taking absolute u below one changes the Schatten
domain and receives no analytic-continuation credit.

## Key findings

1. Observation: all source compilers and finite Gram rows pass independently
   recomputed identities. Interpretation: the mixed geometry is real and
   source-derived. Implication: A0 survives, but the pure Euler orbit ledger
   does not.
2. Observation: all finite B2 traces move with phase. Interpretation:
   obliqueness induces spectral motion. Implication: the infinite non-S2
   firewall prevents using this as an ordinary trace.
3. Observation: S3 is minimal and a unique positive B4 frequency survives
   det3. Interpretation: the critical line is reached honestly.
   Implication: this is a valid analytic family result, not a fixed-operator
   spectral theorem.
4. Observation: every full/active metric row passes and all orthogonal det3
   factors are phase-free. Interpretation: positive completion forces active
   coordinate collapse. Implication: changing the positive square root cannot
   rescue the route.
5. Observation: mutated, composite-only, and seeded-DAG controls retain the
   same motion. Interpretation: the surviving invariant is generic.
   Implication: A4 fails and Route A is rejected.

## Suggested next experiment

Classify source-natural counterterms for the critical finite-cutoff B2 form.
Freeze naturality under finite-poset isomorphisms and compatible cutoff
embeddings before calculating. Determine whether a functorial subtraction can
remove only the diagonal prime-harmonic divergence while retaining a mixed
invariant that vanishes on mutated, composite-only, and seeded-DAG controls.
If every admissible counterterm reduces to atom inventory or generic Gram
data, record a stronger renormalization no-go and stop. Do not introduce
target-zero data or Route B.

## Reproducibility and claim boundary

The canonical runner clears only this paper-local results directory, runs the
generator, 61 exact tests, and analyzer twice under PYTHONHASHSEED=0, compares
all generated hashes, rejects CRLF CSVs and control bytes, removes caches,
audits the strict two-stage pending provenance, and freezes a SHA-256 ledger.
It performs no Git operation.

SD-C30 claims an honest det3 family, exact native motion, and a positive-metric
trilemma/no-go. It does not claim an ordinary B2 trace, a fixed self-adjoint RH
operator, target-zero agreement, a functional equation, analytic continuation
of the Paper27 Euler determinant, or any implication for RH.
