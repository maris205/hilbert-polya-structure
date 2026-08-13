# SD-C09 Source Lock

## Object

- Candidate: SD-C09, entropy-oriented anticommutator shift.
- Primary family: countable-state Symbolic Dynamics only.
- Phase space: the directed graph on tensor atoms, ordered by increasing topological entropy.
- Grammar: one loop at every atom and two parallel directed successor edges; no reverse edges.
- Loop roof: `log p_n = h_top(F_pn)`.
- Successor roofs: source roof `log p_n` and target roof `log p_(n+1)`.
- Successor potentials: both `-log 2`, fixed by endpoint exchange symmetry.
- Cocycle: none in SD-C09.
- Function space: `ell^2(N)` in the entropy-ordered atom basis.

## Transfer and determinant conventions

```text
D_s e_n = p_n^{-s}e_n,
S e_n = e_(n+1),
L_s = (1/2){D_s,I+S}.
```

- Euler determinant: ordinary Fredholm determinant `det(I-zL_s)` for `Re(s)>1`.
- Chiral pencil: blocks `[[0,L_s],[L_(1-s)^T,0]]`.
- Chiral determinant: `det_3(I-zB_s)` on `1/3<Re(s)<2/3`.
- Critical-axis map: `s=1/2+it`; this is a pencil parameter, not an eigenvalue of a fixed operator.

## Parameter provenance

- Atom order comes from topological entropy.
- The coefficient `1/2` is the equal endpoint average; it is not fit.
- No adjustable phase, scale, offset, or boundary condition is present.

## Data firewall

Allowed: full-shift tensor products and entropy, algorithmic tensor indecomposables, exact algebra, numerical linear algebra, and primary symbolic-dynamics literature.

Forbidden: Riemann-zero lists, target-root losses, post-hoc scales, prime-labelled hand-designed adjacency, fitted counterterms, and another primary system family.

## Claim boundary

SD-C09 proves an exact Euler ledger and a separate moving chiral `det_3`. It does not prove they are one analytic determinant, analytic continuation, a completed-xi divisor, or a Hilbert--Polya operator. Route B is locked.
