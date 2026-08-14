# PAPER PLAN — SD-C19

**Title:** *Genuine Fiber Symmetry after Relabeling Failure: Artin Character
Factors of the Tensor-Atom Shift*
**Type:** theory plus exact computational certificates
**Format:** anonymous A4 article
**Primary family:** Symbolic Dynamics
**External review:** intentionally omitted by instruction

## One-sentence contribution

The tensor-subset shift has a lawful recurrent \(C_2\) Artin factorization, but
operator-coherent one-letter cleanliness forces cyclic degree count and thereby
proves no arithmetic selectivity.

## Claims–evidence matrix

| Claim | Evidence | Status | Manuscript location |
|---|---|---|---|
| The parity cover is a genuine commuting finite-fiber extension. | Direct commutation and transitivity proof. | proved | §§3–4 |
| \(D_+\), \(D_-\), and \(D_{\rm reg}\) are exact blocks of one transfer. | Inclusion–exclusion, regular decomposition, two-atom matrix. | proved | §4, Appendix A |
| Natural operator-clean one-letter rules are degree powers with cyclic image. | Coefficient comparison in a faithful representation; 72,079-table certificate. | proved + exact check | §5 |
| Atom-local factors do not remove mixed lifted primitives. | \(q=m/\gcd(m,c)\), lift multiplicity, exact census. | proved + exact check | §6 |
| The mechanism is arithmetic-nonselective. | Formal substitution theorem and 64 matched controls. | proved + exact check | §7 |
| Route A still fails and Route B is locked. | Primitive mismatch, zero control margin, absent completion/operator. | scoped evaluation | §8 |

## Structure

### Abstract

State the lawful repair, exact determinants, cyclic rigidity theorem, primitive
mismatch, and zero control margin.  Explicitly say that no RH conclusion
follows.

### 1. Introduction

Open with the distinction between a formal atom relabeling and a genuine deck
symmetry.  Present the \(C_2\) cocycle and exact result immediately, then list
the construction, rigidity, and obstruction contributions.

### 2. Classical boundary and related work

Separate classical dynamical Artin machinery from the new scoped contribution.
Cover shift determinants, twisted transfer operators, cocycle cohomology,
finite graph/hypergraph covers, and nonclassification warnings.

### 3. Frozen tensor-subset shift and parity extension

Define the tensor source, subset alphabet, scalar sign, arithmetic roof,
skew product, countable convergence boundary, and transitivity/mixing.

### 4. Same-object Artin character factors

Prove the regular decomposition and degree-power product.  Specialize to
\(C_2\) and \(C_m\), display the two-atom matrix, and state the whole/isotypic
boundary.  Place the factorization/scope figure here.

### 5. Functorial one-letter rigidity

State all assumptions before the theorem.  Prove dependence on cardinality,
coefficientwise power law, cyclic image, and the transitivity consequence.
Record determinant-only and transition-dependent exclusions.

### 6. Primitive lifts and the failure of orbitwise arithmetic

Derive \(q=m/\gcd(m,c)\) and \(\gcd(m,c)\) lifted cycles.  Contrast singleton
and mixed edges.  Explain why local-factor cleanliness does not imply a
primitive bijection.

### 7. Exact certificates, controls, and transition boundary

Report the formal, trace, character, naturality, primitive, control, and unit
test counts.  Distinguish pass-rate margin from numerical determinant values.
Use transition controls only to exhibit the theorem boundary.

### 8. Analytic and Route-A boundary

State the honest half-plane, off-shell failure, character-divisor cancellation,
finite/infinite fiber boundary, strict route tuple, and Route-B lock.  Credit A3
only for same-object Artin structure, not imported continuation.

### 9. Conclusion

Retain the positive lawful symmetry and close the one-letter branch.  Name
transition incidence holonomy as the next symbolic test.  Keep geometric ideas
as ROUND2_CLUE.

### Appendices

- Appendix A: full algebraic and primitive proofs.
- Appendix B: exact certificate definitions, transition controls, and
  reproducibility boundary.

## Figure and table plan

| ID | Type | Content | Source |
|---|---|---|---|
| Figure 1 | TikZ structure diagram | Same regular transfer \(\to\) two isotypic blocks \(\to\) whole product, with primitive and control stops below. | exact theorem |
| Table 1 | related-work boundary | Classical mechanism versus SD-C19 contribution. | verified literature |
| Table 2 | exact certificate summary | Counts and exact outcomes. | frozen prototype |
| Table 3 | route coordinates | Evidence and strongest failure at A0–A4. | frozen evaluation |

The figure is relational rather than decorative: it prevents the main
same-object confusion at a glance.

## Citation plan

- Introduction/setup: Bowen–Lanford, Parry–Pollicott, Adachi–Sunada.
- Cohomology boundary: Livšic, Parry–Pollicott (1997), Kalinin.
- Graph/hypergraph analogues: Stark–Terras, Eyler–Jun.
- Determinant nonclassification warning: Boyle–Schmieding.

All bibliography entries are verified by DOI or an authoritative monograph
record.  Only cited entries will remain in references.bib.

## Mechanical targets

- Modular section files with no orphans.
- Four final clean pdflatex passes after BibTeX.
- Zero undefined references/citations and zero overfull/underfull boxes.
- A4 page geometry, all fonts embedded and subset.
- No unresolved drafting markers or build intermediates in the final directory.
