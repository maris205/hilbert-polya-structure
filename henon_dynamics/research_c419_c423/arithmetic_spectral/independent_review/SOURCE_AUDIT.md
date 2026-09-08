# Primary-source applicability audit for the bounded AS2 counterexample

Checked 2026-09-07. This is the independent character-block audit;
the coordinator owns the broader closest-source and all-level search.

## Young: exact version and read locations

Matthew P. Young, *Explicit calculations with Eisenstein series*,
[arXiv:1710.03624v2](https://arxiv.org/abs/1710.03624v2),
[full HTML](https://arxiv.org/html/1710.03624v2),
[versioned PDF](https://arxiv.org/pdf/1710.03624v2).
The arXiv metadata identifies the second version dated 3 November 2017.
The journal record is *Journal of Number Theory* 199 (2019), 1–48,
DOI [10.1016/j.jnt.2018.11.007](https://doi.org/10.1016/j.jnt.2018.11.007).
Locators below refer to the arXiv second version, not journal pagination.

The actual mathematical locations inspected were §3.1, §3.2,
the completion preceding Proposition 4.1, Proposition 4.2, §5.2,
Theorem 6.1, Theorem 7.1, and equations (7.2)–(7.3), together with
the explanatory paragraphs immediately around them.

| Location | Applicable content | Required distinction |
|---|---|---|
| §3.1, (3.1) | Cusp Eisenstein series with stabilizer conjugated to unit translations | Exactly the width-one convention in AS2 |
| §3.2, (3.3) and following paragraph | Character Eisenstein series has nebentypus $\chi_1\bar\chi_2$ | Trivial nebentypus requires $(\chi,\chi)$ |
| Completion before Prop. 4.1 | The factor involves $L(2s,\chi_1\chi_2)$ and $\tau(\chi_2)$ | Here the $L$-function is $L(2s,\chi^2)$ |
| Prop. 4.2, (4.6) | Completed functional equation interchanges and conjugates both characters | The partner is $(\bar\chi,\bar\chi)$ |
| §5.2, (5.4) | Scaling matrix includes square root of the cusp width | The denominator-$5$ and denominator-$10$ prefactors both become $10^s$ |
| Thm. 6.1, (6.1) | Cusp series decompose into primitive character oldforms | Supplies the full spanning/decomposition context |
| Thm. 7.1, (7.1) | Explicit oldform-to-cusp coefficients | Gives the exact two-by-two $C_\chi(s)$ at $N=50$ |
| (7.2)–(7.3) | The $D$ functions are character-weighted cusp sums | $D$ is a fixed Fourier basis, while $C(s)$ is not fixed |

Young's paragraph following (6.1) explicitly attributes an independent
derivation of both basis changes to Booker, Lee and Strömbergsson and
states that these formulas with the functional equation yield the
scattering matrix. Young also identifies Huxley's earlier treatment of
trivial nebentypus in §3.3 and after Theorem 6.1. Consequently neither
the basis changes nor the character functional equation is a new result.

The PDF text extraction omitted some overbars. Attempts to use selected
PDF screenshots either gave reference-only responses or timed out.
All conjugation-sensitive formulas used in the proof were instead
checked against the full HTML, which visibly preserves the overbars.
There is no claim of a successful visual inspection of those PDF pages.

## Dirichlet functional equation and missing Euler factors

[NIST DLMF §25.15](https://dlmf.nist.gov/25.15), version 1.2.7,
release 15 June 2026, was read directly, specifically:

- [25.15.2](https://dlmf.nist.gov/25.15.E2): Euler product and
  nonvanishing in the half-plane $\operatorname{Re}s>1$;
- [25.15.4](https://dlmf.nist.gov/25.15.E4): imprimitive $L$-functions
  as primitive ones with missing Euler factors;
- [25.15.5](https://dlmf.nist.gov/25.15.E5): primitive functional
  equation with conjugation and Gauss sum;
- [25.15.6](https://dlmf.nist.gov/25.15.E6): Gauss-sum convention.

The completed-even-character form in the proof is the algebraic
rewriting of the displayed functional equation with gamma identities.
At $N=50$, the square character is primitive and even. The auxiliary
minimal-level lemma separately retains the missing Euler factors when
a square character is imprimitive.

## What is independently deduced, and what remains unclaimed

The $N=50$ coefficient specialization, invariant fixed Fourier/Walsh
restriction, exact commutator, and the limited minimal-level ratio lemma
are deductions made in this audit. They are not presented as statements
verbatim located in Young. The proof writes all transformations down,
and the code independently enumerates the small divisor sum in (7.1).

The wider Huxley and Booker–Lee–Strömbergsson source comparison is
coordinator-owned and is not represented as an independent fresh read
in this file. No all-level scattering classification, exhaustive
literature novelty claim, or novel spectral realization follows from
this bounded source verification. The result is thin after the
classical-source deduction and is not recommended for admission alone.
