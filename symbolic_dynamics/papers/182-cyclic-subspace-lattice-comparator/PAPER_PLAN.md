# P182 paper plan

**One-sentence contribution.** The three-register lattice polynomial
`T(a,b,c)=(c,a∧b,a∨b)` satisfies `T^4=T^2` universally and has, on finite
subspace lattices, a complete `(q,d)` graph and every-target fibre atlas.

## Section and page plan

1. **The rule and complete theorem package** (about 1.2 pages): define the
   system, place the closest verified literature, introduce six finite-field
   counting polynomials, and state one complete theorem.
2. **Universal lattice dynamics** (about 0.7 pages): prove the iterate
   identity, image, recurrence, period, and depth predicates without assuming
   modularity or finiteness.
3. **Subspace counts and functional graph** (about 1.0 page): derive interval,
   recurrent, disjoint-pair, and depth populations.
4. **Every-target fibres** (about 0.7 pages): quotient by the target meet,
   count ordered complements, derive the histogram and sharp maximizers.
5. **Exact audit, subtraction, and limitations** (about 0.6 pages): report the
   paper-local falsifier, assign background zero credit, and state
   `OWNER_AMBER / HOLD_EXTERNAL`.
6. **Declarations** (compact): Data Availability, Ethics, CRediT, conflicts,
   funding, and AI-use disclosure.

Target: four to five A4 pages including bibliography.  The manuscript is a
proof-only short paper; no decorative figure is planned.

## Claims–evidence matrix

| Claim | Formal evidence | Computational control | Owner boundary |
|---|---|---|---|
| `T^4=T^2` on every lattice | absorption calculation in Lemma 1 | checked at every enumerated source | lattice axioms assigned zero credit |
| recurrent iff `b<=a,c`; only periods 1,2 | solve `T^2x=x`, then restrict `T` | direct graph decomposition in 15 boxes | generic finite-map bookkeeping assigned zero credit |
| image equals triples `(C,M,J)` with `M<=J` | two inclusions; predecessor `(M,J,C)` | image table checked exactly | interval counting is classical background |
| full `(q,d)` fixed/cycle/depth census | Gaussian interval count and disjoint-pair lemma | formulas checked per box | Gaussian coefficients and complement counts assigned zero credit |
| fibre of `(C,M,J)` is `kappa_dim(J/M)` | bijection with ordered complements of `J/M` | every target, including empty fibres, checked | classical single-subspace complement count assigned zero credit |
| maximum fibre and all maximizers | strict embedding `kappa_k<kappa_{k+1}` | maximum targets checked implicitly by full atlas | retained only as part of the full dynamic conjunction |

## Reader-facing order

The title, abstract, first theorem table, and exact `(2,4)` example all expose
the same point: a tiny universal image tower coexists with a nontrivial clock
and a quotient-controlled fibre law.  Proof details then follow in the same
order.  Related work is folded into the opening because the short paper has
no separate survey claim.

