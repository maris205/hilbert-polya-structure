# Exact Tensor-Atom Experiment Report

## Frozen question

Can an algorithm recover tensor atoms and the Euler, reciprocal-determinant,
and logarithmic-derivative coefficient ledgers using only registered
categorical/dynamical data of finite full shifts, without reading a prime
table?

Candidate-side inputs are limited to:

1. opaque object IDs;
2. the registered unit and partial binary operation table;
3. topological entropy;
4. reciprocal Artin--Mazur determinant coefficients;
5. fixed-point counts for periods one through four.

The candidate recovery function contains no primality test.  A trial-division
predicate is used only after recovery as an independent score.  No Riemann
zeros are read anywhere.

## Reproduction

```bash
python code/exact_tensor_atom_experiment.py --output results
PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s code -p 'test_*.py' -v
```

Python standard library only; default cutoffs are \(32,64,128,256\), with 64
deterministic random-atom controls per cutoff.

## Raw data table — main system

| \(N\) | recovered atoms | verifier \(\pi(N)\) | all recovered atoms prime | unique factorization | \(a(n)=1\) through \(N\) | tensor weight/fixed-count compatibility |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 11 | 11 | 1.000 | 1.000 | 1.000 | 1.000 / 1.000 |
| 64 | 18 | 18 | 1.000 | 1.000 | 1.000 | 1.000 / 1.000 |
| 128 | 31 | 31 | 1.000 | 1.000 | 1.000 | 1.000 / 1.000 |
| 256 | 54 | 54 | 1.000 | 1.000 | 1.000 | 1.000 / 1.000 |

At \(N=256\), the maximum floating error in
\(h(X\otimes Y)=h(X)+h(Y)\) is \(8.88\times10^{-16}\).  Determinant-weight
multiplicativity and the period-one-to-four fixed-point tensor identities are
integer-exact for every registered product.

The exact prefix artifacts verify:

\[
 Z_N(s)=\prod_{a\in\mathrm{Atoms}_N}(1-a^{-s})^{-1}
       =\sum_{n\le N}\frac{1}{n^s}+O(N^{-\Re s}),
\]

in the coefficient sense through \(N\); the reciprocal coefficients agree
with \(\mu(n)\), and the negative logarithmic derivative is supported exactly
on prime powers with coefficient \(\log p\).

## Raw data table — adversarial controls at \(N=256\)

| control | atom/UFD result | zeta coefficient accuracy | reciprocal accuracy | relative \(\Lambda\)-ledger \(L^1\) error | decisive failure |
|---|---|---:|---:|---:|---|
| additive alphabet law \(m\boxplus n=m+n\) | one atom, UFD 1.000 | undefined | undefined | undefined | sole atom has weight 1 and zero entropy; Euler factor diverges |
| 64 matched random atom sets | Jaccard \(0.1147\pm0.0253\) | \(0.2607\pm0.0327\) | \(0.3483\pm0.0287\) | \(1.5823\pm0.0806\) | declarations disagree with tensor indecomposability and coefficient ledger |
| shifted law \(m\star n=(m-1)(n-1)+1\) | UFD 1.000; atoms \(p+1\) | 0.1758 | 0.2773 | 1.9248 | intrinsic entropy/AM norm is incompatible with \(\star\) |
| shifted law with post-hoc clock \(\log(n-1)\) | same UFD | 1.000 | 1.000 | 0.0000 | exact fit returns only after abandoning intrinsic topological entropy |
| free-mixing two-atom grammar (28 pairs) | mixed primitive words | 2 at every \(pq\), target 1 | not applicable | positive at every \(pq\), target 0 | word order creates spurious semiprime trace terms |

The random-control accuracy range at \(N=256\) was 0.2109--0.3438 for zeta
coefficients; no seed approached the exact main result.

## Key findings

### 1. Exact atom recovery

**Observation.** At every cutoff, the opaque tensor algorithm recovered
exactly \(\pi(N)\) atoms, all of which the sealed verifier classified as
prime.  Every registered object had one tensor-atom factorization.

**Interpretation.** Prime detection is categorical indecomposability of finite
full shifts under their actual Cartesian product.

**Implication.** The candidate has an exact, table-free A0 arithmetic source;
it is not a prime-label shuffle.

**Next step.** Freeze the infinite tensor-atom groupoid and the diagonal atom
shift as one formal candidate rather than leaving the construction at the
finite registry level.

### 2. Exact Euler and determinant prefixes

**Observation.** The Euler coefficients were all one through the cutoff.  The
reciprocal and log-derivative ledgers reproduced the Möbius and von Mangoldt
patterns, respectively.

**Interpretation.** Unique tensor factorization supplies the Dirichlet
coefficients, while differentiation of the entropy roof supplies \(\log p\).

**Implication.** The diagonal atom shift supports an exact A1 primitive/repeat
ledger and an A2 trace-class determinant for \(\Re s>1\).

**Next step.** Write the trace-class theorem and keep the target orientation
explicit: \(Z=\zeta\), whereas \(\det(I-\mathcal L_s)=1/\zeta\).

### 3. Random atoms do not survive the registered tensor law

**Observation.** Same-cardinality random sets had low Jaccard agreement with
the intrinsic atoms and substantial coefficient/log-derivative error.

**Interpretation.** The exact ledger is not explained merely by selecting the
right number of generator symbols.

**Implication.** Matched-density controls separate categorical atom recovery
from arbitrary Euler-product fitting.

**Next step.** In a formal candidate evaluation, forbid external atom
declarations; only the tensor table may decide atom status.

### 4. Abstract UFD proves too much unless the entropy norm is locked

**Observation.** Shifted multiplication has perfect unique factorization and
the same number of atoms, but its intrinsic full-shift entropy yields poor
Euler coefficients.  Replacing the roof by \(\log(n-1)\) restores a perfect
fit.

**Interpretation.** Any relabeled UFD can be made zeta-like by a tailored
clock.  The discriminator is the simultaneous compatibility of operation,
topological entropy, AM determinant, and fixed-point counts.

**Implication.** A theorem based only on “free commutative monoid + atom
clock” is `PROVES_TOO_MUCH`.  The strengthened full-shift tensor hypothesis
does not fail this control because its clock is intrinsic and additive.

**Next step.** Make the compatibility square an explicit A0 gate:

\[
 e^{h(X\otimes Y)}
 =e^{h(X)}e^{h(Y)}
 =- [z]D_X^{\rm AM}\,(-[z]D_Y^{\rm AM})
 =-[z]D_{X\otimes Y}^{\rm AM}.
\]

### 5. No-mixing is forced by the prime-power trace

**Observation.** For all 28 distinct pairs among the first eight recovered
atoms, the diagonal atom-loop grammar had zeta coefficient one and
log-derivative coefficient zero at \(pq\).  The free-mixing grammar had zeta
coefficient two and log-derivative coefficient exactly \(\log(pq)>0\).

**Interpretation.** Free symbolic concatenation treats \(pq\) and \(qp\) as
ordered mixed cycles.  Euler multiplication is commutative and permits mixed
products in \(Z\), but the logarithm must contain only powers of one primitive
atom.

**Implication.** The diagonal adjacency is not merely the easiest grammar.  It
is the minimal exact presentation of the Euler primitive/repetition ledger.
Any positive off-diagonal transition immediately violates the von Mangoldt
support condition.

**Next step.** Freeze adjacency as the identity on tensor atoms.  Any future
mixing must carry an intrinsic cancellation mechanism that annihilates every
mixed primitive cycle; positive renewal weights cannot do so.

## Route-A implication

Recommended provisional tuple, conditional on source-locking the diagonal
atom shift as the actual candidate:

```text
A0 = A0_ANALYTIC_ARITHMETIC_ORIGIN      [exact tensor-atom theorem]
A1 = A1_PASS_ANALYTIC                   [one atom loop; repetitions exact]
A2 = A2_ANALYTIC_DETERMINANT            [trace class for Re(s)>1]
A3 = A3_PARTIAL_ANALYTIC_STRUCTURE      [zeta identity, but no intrinsic completion]
A4 = A4_FAIL                            [no natural lift]
overall = ROUTE_A_ANALYTIC_CANDIDATE, ROUTE_B_NOT_READY
```

The A0 label retains a conceptual caveat: full finite-set cardinalities under
Cartesian product are a very direct realization of integer multiplication.
The experiment proves emergence from registered categorical data, but cannot
decide whether a reviewer regards that emergence as too tautological.

## Blocking points

1. The ordinary Fredholm determinant is \(1/\zeta\); the Riemann zeros become
   poles after continuation, not determinant zeros.
2. The transfer operator is trace class only in the Euler half-plane.  The
   known continuation of \(\zeta\) is not yet reproduced by internal symbolic
   estimates.
3. There is no intrinsic gamma factor or \(s\leftrightarrow1-s\) symmetry.
4. There is no target-intrinsic Weil Hermitian compression.
5. The diagonal atom shift has deliberately trivial base dynamics; all
   arithmetic content sits in the tensor spectrum and entropy norm.
6. Route B is blocked: no canonical quantization, self-adjoint generator,
   spectral counting theorem, or completed-xi determinant.

## Suggested next exact experiment

Remain in Symbolic Dynamics and test one bold extension: construct a canonical
**graded/signed symbolic cocycle** from tensor-factorization data itself and
ask whether its super/Fredholm determinant reverses the determinant orientation
without inserting parity by hand.  Controls must include arbitrary parity,
random signs, and the shifted monoid.  If no intrinsic grading exists, record
“Euler product is symbolic; determinant orientation requires extra structure”
as the theorem-level boundary.

## Artifacts

- `code/exact_tensor_atom_experiment.py`: complete generator, recovery algorithm,
  coefficient engine, verifier, and controls.
- `results/main_raw.csv`: main exact results.
- `results/random_atom_raw.csv`: all 256 random-control runs.
- `results/additive_raw.csv`: additive controls.
- `results/shifted_raw.csv`: shifted-multiplication controls.
- `results/no_mixing_raw.csv`: all two-atom free-mixing/no-mixing comparisons.
- `results/coefficient_ledger_N256.json`: exact Euler, reciprocal, and
  log-derivative coefficients through 256.
- Opaque public registries are generated in memory.  Pass `--save-registries`
  only when inspecting them manually; they are intentionally omitted from the
  shareable results because the additive control alone is about 3 MB and is
  exactly reproducible from the source.
- `results/summary.json`: machine-readable aggregate.
