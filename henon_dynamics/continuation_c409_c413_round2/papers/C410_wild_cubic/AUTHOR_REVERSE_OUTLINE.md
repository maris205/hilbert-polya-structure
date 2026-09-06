# C410 author reverse outline and contract check

Date: 2026-09-06. Status: **AUTHOR CHECK COMPLETE; INDEPENDENT REVIEW PENDING**.
The reviewed author PDF has 13 pages. The whole source and every rendered page
were read. This receipt does not count as a non-author review.

## Reverse outline

| Section | Function in the paper | Exact logical output |
|---|---|---|
| Abstract | State the family, clock, results and ownership boundary | Three theorem contracts summarized without specialization or forward-period claims |
| 1. Introduction | Motivate the mismatch between many global generators and one local class; locate classical `E_n` | Prior group ownership and characteristic hypotheses separated from the new wild calculation |
| 2. Tower and statements | Fix original and geometric constants, compatible tree labels, and normalized valuations | Theorems 2.1, 2.2 and 2.3, with a simultaneous-induction roadmap |
| 3. Cubic normal form and local tools | Prove the explicit splitting-field identity and the base case; state/prove radical-degree and completion facts | Actual field equality, separability, irreducibility, `G_1=S_3`, infinity index 6; classical tools made explicit |
| 4. Compatible signature bound | Choose Vandermonde signs once on the infinite tree | Arithmetic upper bound `G_n <= E_n`; attributed order recurrence and independent bottom 3-cycles |
| 5. Zero-place valuations and square-class rank | Use tame zero-place geometry and only the already established height-`n` group | Exact sibling relation space and quadratic rank `2*3^(n-1)` |
| 6. Local/global Artin--Schreier induction | Carry the height-`n` group and infinity index together; separate global character projections from local principal parts | Global rank `3^n`, local rank one, next group and next infinity index; degree-sandwich descent to arbitrary `k` |
| 7. Different and genus | Compute the root-cover different, use the relative tame quadratic extension, then Riemann--Hurwitz | Branch set, both different exponents and genus; two-row table derived from the proof |
| 8. Conclusion and scope | Recombine the answer and delimit its interpretation | Explicitly no forward periodic-point theorem, specialization surjectivity, target Euler factors or Hilbert--Polya operator |

## Contract-to-proof ledger

### Theorem 2.1: generic arithmetic and geometric tower

The cubic normal form preserves the coefficient `a` over the original field.
Lemma 3.2 proves the first height. Proposition 4.1 imposes the local product-sign
relations in one compatible labeling, rather than only imposing total leaf
parity. Section 6.4 compares the exact degree increment with the attributed
order ratio and proves every geometric finite-height group. Section 6.5 uses
the arithmetic upper bound and the geometric lower bound to obtain equality;
the tensor-product degree argument proves regularity, including for imperfect
`k`. Compatibility gives the inverse-limit action without changing labels.

### Theorem 2.2: exact global and local ranks

Lemma 5.1 is independent of the next group. Proposition 5.2 spans the full
even-parity subspace on each bottom triple using independent bottom 3-cycles
at height `n`, then uses its orthogonal complement to exclude extra square
relations. The sibling product identity supplies all remaining relations,
including the parent `t` at height one.

Lemma 6.1 obtains pole order one only from the already known infinity index,
and proves complete quadratic splitting there. Proposition 6.2 applies finite
character projections over `F_3` to distinct nonzero global classes. It does
not assume the full quotient vector space is finite-dimensional.
Proposition 6.3 does not project at a fixed place: it compares leading terms
directly and proves local proportionality modulo Artin--Schreier images.
This separately yields the next infinity index.

### Theorem 2.3: geometric ramification and genus

Lemma 5.1 gives branch support and exact tame index at zero. Section 6.4 has
already established the infinity index, before the different is computed.
Proposition 7.1 computes the formal derivative of `h(u)=u^3/(1+a*u)`, applies
the chain rule at every height, and uses a relative tame degree-two extension
of the root completion. The normalized different is `3^(n+1)-2`.
Riemann--Hurwitz is applied only over the algebraically closed constants, so
the number of places is correctly `|E_n|/e`. The result gives `g_1=0` and
`g_2=46`, exactly as the table states.

## Scope and consistency checks

- Only the three frozen substantive contracts are promoted to main theorems.
- There is no new classification of the complete wild inertia group or
  higher ramification filtration; such a classification was not proved.
- The inverse-image height is defined separately from a forward period or
  finite-field extension degree.
- Arithmetic versus geometric assertions are explicit both before and after
  the theorem statements; residue degree one is not asserted over arbitrary
  original constants.
- The family is exactly `X^3+a*X^2`, characteristic three, `a != 0`, generic
  transcendental `t`. No specialization theorem is smuggled into descent.
- Classical group and function-field tools are attributed in the text and
  in `CITATION_AUDIT.md`.
- The low-height table is a consequence of the all-height proof and is not
  offered as computational evidence for it.
- No TODO, TBD, FIXME, VERIFY, citation placeholder, or legacy candidate
  number occurs in the actual TeX/BibTeX manuscript.
- All nine section inputs in `main.tex` exist; there are no orphan section
  files. No proof scripts or legacy enumerations were rerun.

## Author-side corrections found during verification

1. First compilation exposed a missing backslash before `left` in the final
   Riemann--Hurwitz alignment. The exact failure log is retained separately.
2. Source review found a stray comma in the exponent denoting the threefold
   direct product of `E_(n-1)`. It was replaced by TeX thin spacing, leaving
   the intended mathematical definition unchanged.

Neither correction changed a theorem contract. The final successful PDF and
all its page images correspond to both corrections.
