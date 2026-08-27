# C193 exact-regression plan

The executable artifacts test conventions and finite consequences; they do
not replace the all-solution descent proof.

## Producer path

1. Generate the normalized Vieta graph through depth ten from `(1,1,1)`.
2. Orient every non-root edge by replacing the unique maximum and verify
   strict height decrease.
3. Store local-child-rank words, parents, children, level populations and
   selected complete traces to the root.  Each digit is the local
   lexicographic rank among normalized children, not a fixed labelled
   Vieta-generator symbol.
4. Independently scan all `x<=y<=z<=2000` by solving the quadratic in `z` and
   compare the result with a height-bounded tree generation.
5. Record exact polynomial-invariance sentinels and every hard Route-A scope
   flag.

## Independent checker path

The checker rebuilds levels rather than importing producer traversal code.  Its
bounded census solves the quadratic in `y` at fixed `(x,z)`, reversing the
producer's loop and root variable.  It verifies every row, parent, child,
branch word, Lyapunov step, bounded solution and descent trace.

## Symbolic path

SymPy proves Vieta polynomial invariance and involutivity, reconstructs root
sums/products and the between-roots identity, and then checks every stored
integer edge independently.

## Integrity gates

- byte-identical isolated producer replay;
- repaired-hash attacks on identity, sources, theorems, Route labels, tree
  rows, bounded solutions, paths and traces;
- stale-hash rejection;
- two content-changing paper improvements;
- fresh fixed-epoch double PDF build, embedded fonts, clean logs and rendered
  page inspection.

Any use of mod-prime data, any claim to solve Frobenius uniqueness, or any
promotion of finite enumeration to a global proof is a hard failure.
Depth-ten rows retain every one-step child, including frontier children at
depth eleven that are not themselves stored rows; the census is not a closed
finite tree.
