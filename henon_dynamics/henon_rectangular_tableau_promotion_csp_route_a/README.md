# HCS-C187: rectangular tableau promotion CSP

This release freezes Schützenberger promotion on every rectangular standard
Young-tableau set `SYT(b^a)`, with `N=ab`.  Rhoades's unshifted q-hook cyclic
sieving theorem is the attributed all-rectangle input.  The package derives a
complete every-iterate fixed ledger, exact-period and cycle counts, finite
Artin--Mazur zeta, finite Koopman determinant and spectrum, and the evacuation
reversor.  It never claims that promotion has exact order `N` uniformly.

## Exact result

For

\[
F_{a,b}(q)=\frac{[N]_q!}{\prod_{c\in b^a}[h(c)]_q},
\qquad \zeta_N=e^{2\pi i/N},
\]

Rhoades's CSP gives

\[
\#\operatorname{Fix}(j^d)=F_{a,b}(\zeta_N^d).
\]

Möbius inversion yields every exact-period population and cycle count.  If
`C_l` is the number of cycles of length `l`, then

\[
\zeta_j(z)=\prod_{l\mid N}(1-z^l)^{-C_l},\qquad
\det(I-zU_{a,b})=\prod_{l\mid N}(1-z^l)^{C_l}.
\]

Evacuation satisfies `e^2=id` and `e j e=j^{-1}`.  The one-row and one-column
families are singleton identity systems; the `2 x 2` family has two tableaux
and promotion order two, not four.

## Reproduce

Run from the repository root:

```bash
python henon_dynamics/henon_rectangular_tableau_promotion_csp_route_a/code/c187_tableau_csp_producer.py
python henon_dynamics/henon_rectangular_tableau_promotion_csp_route_a/code/c187_tableau_csp_checker.py
python henon_dynamics/henon_rectangular_tableau_promotion_csp_route_a/code/c187_sympy_crosscheck.py
python henon_dynamics/henon_rectangular_tableau_promotion_csp_route_a/code/c187_replay.py
python henon_dynamics/henon_rectangular_tableau_promotion_csp_route_a/code/c187_mutation.py
python henon_dynamics/henon_rectangular_tableau_promotion_csp_route_a/code/c187_release_manifest.py
```

The exact evidence has 36 rectangle rows, 441 every-iterate rows, 162 period
rows, and 441 spectral rows.  Independent enumeration covers 26 rectangles
and 37,401 tableaux.  The checker passes 230,034 assertions, the separate
SymPy path passes 3,065 checks, and the hostile suite rejects 107 repaired-hash
mutations plus one stale-hash mutation.

## Route-A verdict

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall
`ROUTE_A_REJECTED`; Route B is false.  Scope literal:
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The finite Koopman permutation is a natural source operator, but rectangle,
hook and cyclotomic data contain no intrinsic rational-prime semantics and no
target divisor match.  Classical theorem ownership remains with the cited
sources; this release is not an external review or literature-wide novelty
certificate.
