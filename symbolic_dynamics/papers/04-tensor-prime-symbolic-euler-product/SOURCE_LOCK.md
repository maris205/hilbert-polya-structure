# SD-C07 Source Lock

Frozen on 2026-08-12 before the Route-A verdict.

## Object

- **Primary family:** Symbolic Dynamics only.
- **Source category:** the symmetric monoidal skeleton
  \(\mathsf{FSh}=\{[F_n]:n\geq1\}\) of finite two-sided full shifts, up to
  topological conjugacy.
- **Tensor product:** actual coordinatewise Cartesian product of shifts.
- **Tensor unit:** \([F_1]\).
- **Atom alphabet:** all nonunit tensor-indecomposable isomorphism classes in
  \(\mathsf{FSh}\); atom membership may not be declared externally.
- **Phase space:** the one-sided countable Markov shift
  \[
    Y_\otimes=\{(a_j)_{j\geq0}:a_{j+1}=a_j,\ a_j\in
    \operatorname{At}(\mathsf{FSh})\}.
  \]
- **Dynamics:** left shift \(S\) on \(Y_\otimes\).
- **Roof:** \(\tau(a)=h_{\rm top}(a)\), with no rescaling or offset.
- **Potential/cocycle:** zero / none.
- **Function space:** \(\ell^2(\operatorname{At}(\mathsf{FSh}))\).
- **Transfer operator:**
  \((\mathcal L_s f)(a)=e^{-s\tau(a)}f(a)\).
- **Determinant convention:**
  \(D_\otimes(s)=\det(I-\mathcal L_s)\) and
  \(Z_\otimes(s)=D_\otimes(s)^{-1}\), initially for \(\Re s>1\).

The tensor-atom relation is categorical.  A tensor atom is not a primitive
temporal necklace inside the full shift that represents it.  It becomes a
temporal primitive orbit only after applying the fixed atom-loop
orbitification above.

The unweighted Artin--Mazur zeta of the derived countable shift is not used:
it has infinitely many fixed points.  The frozen global object is the
entropy-weighted Ruelle/suspension zeta and its trace-class Fredholm
determinant in \(\Re s>1\).

## Data and computation lock

- Exact registry cutoffs: \(N\in\{32,64,128,256\}\).
- Object-side inputs: opaque IDs, the partial tensor table, entropy, period
  1–4 fixed counts, and reciprocal Artin–Mazur determinant coefficients.
- Precision: exact integer/rational arithmetic where applicable; IEEE-754
  binary64 only for logarithms and summary errors.
- Training data: none.
- Allowed verifier: an independent primality predicate used only after atom
  recovery for scoring.
- No zero fitting, seed selection, scale fitting, or post-hoc adjacency
  changes.

## Frozen controls

1. additive alphabet law;
2. 64 matched-cardinality random atom declarations per cutoff;
3. shifted multiplication with the intrinsic entropy clock;
4. the same shifted law with a deliberately post-hoc clock;
5. positive free mixing for all 28 pairs among the first eight recovered
   atoms.

All seeds and all cutoffs are reported.  No best-case control may be selected.

## Forbidden moves

- a prime table or rational-prime symbol list in the definition;
- a Riemann-zero table anywhere in construction or validation;
- manually assigning \(\log p\), \(\Lambda(n)\), phases, signs, or parity;
- adding cross-atom transitions after inspecting coefficients;
- borrowing the Mayer determinant, wheel-sieve clock, Knauf signs, or any
  other candidate's coordinate;
- importing a Gamma factor or functional equation and calling it dynamical;
- treating the known meromorphic continuation of \(\zeta\) as a trace-class
  continuation of \(\mathcal L_s\);
- invoking Route B.

## Claim boundary

The locked claim is an exact same-object symbolic Euler/Fredholm realization
in \(\Re s>1\), plus a positive no-mixing theorem and an obstruction to
holomorphic trace-class continuation through zeta zeros.  It is not an RH
proof, a completed-\(\xi\) determinant, or a Hilbert–Pólya operator.
