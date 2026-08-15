# HCS-C57 paper plan

Status: **PAPER_COMPILED; PAPER_HOSTILE_PASS; implemented manuscript plan;
machine PREFREEZE_CODE_RESULTS_PASS; NOT_RELEASED.**

## 1. Working title

**The Minimal Degree of a 2-Primary Brauer Jump on the Fourth Hénon Yukawa
Surface**

## 2. One-sentence result

For the frozen HCS-C55 cubic surface with HCS-C56 line Galois group
\(W(E_6)\), nonzero 2-primary algebraic Brauer quotient after finite base
change forces

\[
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q],
\]

the degree-36 double-six field attains the bound, and its unique nonzero class
is represented by the canonical quaternion
\((\delta_D,Q_D/u_0^4)\).

## 3. Planned abstract contract

The abstract should state:

1. the frozen C55/C56 input;
2. the divisibility theorem, with minimum 36 as a corollary;
3. equality classification by double-six fixed fields;
4. exact degree-36 orientation data;
5. the determinant-defined quartic and quaternion generator;
6. that the result is instance-specific and search-bounded.

It must not mention rational points, Brauer--Manin obstruction, local
evaluation, stable irrationality, local Artin data, or a “first” resolver.

## 4. Theorem suite

### Theorem 1: divisibility and equality

\[
\left(
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\right)[2]\ne0
\Longrightarrow
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\]

Equality fields are the conjugate \(K^{gU_1g^{-1}}\).

### Theorem 2: exact double-six fields

The exact degree-36 resolvers bind all and only double-sixes, have normal
closure \(K\), and satisfy

\[
\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D).
\]

### Theorem 3: Brauer jump

\[
\operatorname{Br}(Y)/\operatorname{im}\operatorname{Br}(\mathbf Q)=0,
\qquad
\operatorname{Br}(Y_{F_D})/\operatorname{im}\operatorname{Br}(F_D)
\cong\mathbf Z/2.
\]

### Theorem 4: explicit generator

The determinant-defined quartic satisfies

\[
\operatorname{div}(Q_D)=\mathcal E+\mathcal G,
\]

and

\[
(\delta_D,Q_D/u_0^4)
\]

generates the quotient.

## 5. Planned section structure

1. **Introduction and adaptive handoff.**
   State what C55 and C56 actually proved and isolate the C57 advance.
2. **Sources and claim boundary.**
   State the complete \(U_1/U_3\) classification and general resolver
   precedent.
3. **Exact Schläfli incidence.**
   Present the characteristic-zero gcd, counts, and configuration action.
4. **Minimal-degree theorem.**
   Prove the two classification branches, divisibility, and equality case.
5. **Double-six and orientation fields.**
   Define \(\theta,\beta,\delta\), resolvers, stabilizers, and fixed fields.
6. **Picard cohomology and Brauer descent.**
   Separate machine SNF from inflation/Hochschild--Serre.
7. **The determinant-defined quartic.**
   Prove the gauge, rank sandwich, uniqueness, and all restrictions.
8. **Divisor and quaternion.**
   Prove degree exhaustion, norm divisor, unramifiedness, and nontriviality.
9. **Exact replay and limitations.**
   Give the certificate ledger and hostile negative tests.
10. **Conclusion.**
    Restate only the proven theorem; later work remains unselected.

## 6. Planned appendices

- **Appendix A: primary-source locators.**
  Exact SD93 and EJ10 theorem/page ledger.
- **Appendix B: exact incidence and resolver summaries.**
  Compact coefficients or stable machine references, not multi-megabyte raw
  arrays.
- **Appendix C: group cohomology.**
  Generator conventions, relation/principal matrices, ranks, and Smith
  invariants.
- **Appendix D: canonical quartic specification.**
  Gauge block, monomial order, matrix order, pivot rows, determinant
  definition, and replay hashes.
- **Appendix E: certificate contract.**
  Semantic gates and fail-closed mutation inventory.

## 7. Source obligations

The bibliography must include and accurately locate:

- Swinnerton-Dyer 1993, especially Lemmas 1--2;
- Elsenhans--Jahnel 2010 Brauer--Manin paper, especially §1.3, §4.3--4.4,
  Proposition 5.8, Theorem 5.11, and Fact 6.2;
- Elsenhans--Jahnel 2010 invariant-double-six construction;
- Elsenhans--Jahnel 2012 Remark 4.34(iii) as prior art for the general
  degree-36 resolver;
- Farb--Wolfson 2019 for the moduli/resolvent context;
- a supporting Hochschild--Serre locator.

Bibliographic metadata must be checked again against primary DOI, publisher,
and arXiv records when references.bib is created.

## 8. Display strategy

The paper should display:

- the divisibility chain;
- the \(U_1/U_3\) branch table;
- the field tower;
- the gauge determinant;
- the locked monomial/pivot conventions;
- the rank sandwich;
- the divisor/norm identity;
- the final quaternion.

It should not print:

- the full degree-36 coefficient vectors in the main text;
- a 31-by-36 expanded quartic table;
- an uncertified \(\delta=P(\theta)\);
- temporary filenames or hashes.

## 9. Evidence tables

Planned compact tables:

1. theorem/source/machine/written-bridge dependency matrix;
2. incidence and configuration counts;
3. subgroup orders, indices, and cohomology;
4. resolver construction and irreducibility witnesses;
5. G6 gauge/pivot/rank and determinant-quartic gate;
6. G7 divisor/norm/quaternion/nonzero-class gate;
7. separate unnumbered scope-firewall truth table;
8. official release tuple after handoff.

## 10. Paper gates

The prerequisite gates all pass:

- exact producer and independent checker pass (**complete**);
- tests and exhaustive rebound pass (**33/33 and 535/535 complete**);
- scoped manifest passes (**28-entry self-excluding manifest complete**);
- formal docs are rebound to the official tuple (**complete**);
- a hostile theorem/source audit reports no blocker (**complete**);
- the independent hostile paper audit reports no blocker (**complete**);
- the official controlled build and artifact audit pass (**complete**).

The official build applied the prerequisite, static
label/citation/environment, controlled-build, log, font, extracted-text,
Ghostscript, and visual checks. It reports zero LaTeX/BibTeX/reference/citation
or box warnings, 31 embedded fonts, no Type 3 fonts, and no retained generated
auxiliaries.

## 11. Official paper artifacts

| artifact | authoritative value |
|---|---|
| source aggregate | `3c2b0a3a3908368ea5efa35f22fb124796e43f5666328c94d3bee0682fd9c10e` |
| PDF | `60bdbcbb1a9ddc03ac6a142d22142821860545026fb9dfa21a8001960c7d0200` |
| official stabilized log | `ddbbf698c8b0c3b1167f708ec32fe0e92b4ba47d4d6af8c3b5f379425886884b` |
| extracted text | `0d91dd71471e5131a554320bf8dfef94b9a0b378b56b8f3a261d99061b3f1877` |
| compilation report | `4684570886e26e4dc1510ce681baa6f5d28c38f2331bafe50281605a186c64fe` |
| source definition | SHA-256 of lexicographically ordered `sha256sum` lines for 17 TeX files and `paper/references.bib`, evaluated from the C57 project root |
| inventory and size | 18 source files; 20 paper files including PDF and report; auxiliaries 0; PDF 24 pages and 537984 bytes |
| extracted-text metrics | 1321 lines; 9314 whitespace-delimited tokens; 75541 bytes |
| independent audit | `PAPER_HOSTILE_PASS`; 0 blocker |

## 12. Current boundary

The paper directory, six-entry bibliography, official PDF, external stabilized
log digest, extracted-text digest, and compilation report are complete and
bound. The post-compile formal-package identity, commits, self-excluding
full-project manifest, release archive, and project promotion remain pending;
`promotion_authorized=false` and the project is `NOT_RELEASED`.

Later batch items are contingent and unselected; this plan assigns none of
them a topic.
