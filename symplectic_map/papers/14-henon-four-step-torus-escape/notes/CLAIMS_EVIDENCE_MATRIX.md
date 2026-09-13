# Claims--Evidence Matrix

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Evidence classes

- **External theorem:** a precise published theorem is imported.
- **Internal proof:** a complete symbolic derivation appears in
  PROOF_PACKAGE.md.
- **Construction:** an explicit family is checked by substitution.
- **Corollary:** follows formally from a proved stronger statement.
- **Search boundary:** supported only as a bounded literature-search report.
- **Pending:** deliberately not a current claim.

## Matrix

| ID | Claim | Evidence | Location | Current status | Independent-review obligation |
|---|---|---|---|---|---|
| C1 | ESS gives at most \(\exp(18^9(3r+1))\) nondegenerate local variable triples | External theorem | CITATION_VERIFICATION V1; PROOF_PACKAGE Steps 1--2 | supported | verify published theorem numbering, fixed coefficients, and finite-rank scope |
| C2 | No coefficient-membership hypothesis is needed | External theorem plus internal proof | PROOF_PACKAGE Step 1 | supported | reject any rewrite that puts coefficient-normalized variables in \(\Gamma^3\) |
| C3 | A specified nondegenerate index contributes at most \(dE(3,3r)\) initial states | Internal proof | PROOF_PACKAGE Steps 1--2 | supported | verify root count and injectivity of \(H^i\) |
| C4 | The nondegenerate part of \(T_4\) has size at most \(4dE(3,3r)\) | Internal proof | PROOF_PACKAGE Step 2 | supported | verify exactly four local indices \(0,1,2,3\) |
| C5 | \(A,B,C\) exhaust local degeneracy | Internal proof | PROOF_PACKAGE Step 3 | supported | verify all summands are nonzero and only pair subsums matter |
| C6 | The displayed nine-transition table is complete | Internal proof | PROOF_PACKAGE Step 4 | supported | independently rederive every table entry with the fixed label convention |
| C7 | Only \(BA\) and \(CB\) can be free adjacent words | Internal proof | PROOF_PACKAGE Step 4 | supported | inspect simultaneous-label cases and coefficient compatibilities |
| C8 | Every \(BA\) prefix closes by the third letter | Internal proof | PROOF_PACKAGE Step 5 | supported | verify the powers \(b^{d+1}a^{d^2}\) and degree \(d^2-1\) |
| C9 | The only free \(CB\) extension is \(CBA\), and it closes at the fourth letter | Internal proof | PROOF_PACKAGE Steps 6--7 | supported | verify \(a=-1\), \(bc^{d-1}=-1\), and all fourth-letter equations |
| C10 | Simultaneous degeneracy causes overcount only, never omission | Internal proof | PROOF_PACKAGE Step 8 | supported | check pair intersections and impossibility of triple intersection in characteristic zero |
| C11 | The fully degenerate part has size at most \(81d^2\) | Internal proof | PROOF_PACKAGE Steps 4--8 | supported | confirm each of \(3^4\) words has at most \(d^2\) initial states |
| C12 | \(\#T_4\le4d\exp(18^9(3r+1))+81d^2\) | C1--C11 | PROOF_PACKAGE Step 9 | supported | full proof replay required |
| C13 | Periods \(1,2,3,4\) require no extra term | Internal proof | PROOF_PACKAGE Step 10 | supported | verify proof never assumes state distinctness |
| C14 | For every \(d\ge2\), rank-one \(T_3\) can be infinite | Construction | PROOF_PACKAGE Step 11 | supported | independently substitute all three iterates and verify rank |
| C15 | \(\sum nC_n^\Gamma(H)\) satisfies the same upper bound | Corollary | PROOF_PACKAGE Step 12 | supported | verify exact-period orbit disjointness and full-orbit containment |
| C16 | No direct prior theorem with the combined scope was located through 2026-08-16 | Search boundary | NOVELTY_ASSESSMENT; CITATION_VERIFICATION | bounded search claim | redo targeted primary-source search |
| C17 | Novelty is approximately \(7/10\), standalone size approximately \(6/10\) | Two independent assessments | NOVELTY_ASSESSMENT | advisory only | do not turn scores into theorem evidence |
| C18 | A full \(T_2/T_3\) coefficient stratification holds | none | RESEARCH_QUESTION secondary questions | pending, not claimed | requires separate proof and review |
| C19 | The constants are optimal | none | nonclaims | explicitly not claimed | no action |
| C20 | General rational or integral periodic points are bounded | none; contrary adjacent context exists | nonclaims; CITATION_VERIFICATION V10 | explicitly not claimed | ensure manuscript never implies it |
| C21 | The quartic Paper 15 reserve supports Paper 14 | none | reserve statements | explicitly false as a dependency | keep projects separate |

## Primary-claim dependency diagram

\[
\begin{array}{c}
\text{ESS fixed-coefficient theorem}
\longrightarrow
4dE(3,3r)
\\[3pt]
\text{nine transitions}
\longrightarrow
\{BA,CB\}\text{ free}
\longrightarrow
\text{three/four-letter closure}
\longrightarrow
81d^2
\\[3pt]
\bigl(4dE(3,3r)\bigr)+\bigl(81d^2\bigr)
\longrightarrow
\#T_4
\\[3pt]
\text{explicit }CBA\text{ family}
\longrightarrow
\#T_3=\infty\text{ in rank one}
\\[3pt]
\mathcal O\subseteq\Gamma^2
\longrightarrow
\sum nC_n^\Gamma(H)\le\#T_4.
\end{array}
\]

## Claim-language controls

The following wording is permitted:

- “uniform in \(K,a,b,c\)”;
- “finite-rank, not necessarily finitely generated”;
- “four-step survival is universally finite”;
- “the immediately shorter three-step window can be infinite in rank one”;
- “targeted primary-source search found no direct collision”;
- “weighted periodic-orbit corollary for orbits wholly contained in
  \(\Gamma^2\).”

The following wording is forbidden:

- “all torus-valued periodic points” without defining full-orbit
  containment;
- “optimal bound”;
- “all \(T_3\) exceptions are classified”;
- “all integral or rational periodic points are bounded”;
- “the normalized variables lie in \(\Gamma\)” when coefficients are outside
  \(\Gamma\);
- “verified computationally”;
- “independently certified” before the next review gate;
- any Paper 15 quartic theorem.

