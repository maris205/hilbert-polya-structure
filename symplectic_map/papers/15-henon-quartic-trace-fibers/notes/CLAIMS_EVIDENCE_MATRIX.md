# Claims--Evidence Matrix

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Evidence classes

- **Internal proof:** a complete author-side symbolic derivation appears in
  PROOF_PACKAGE.md.
- **External theorem:** a primary source is imported with its exact scope.
- **Direct precedent:** prior work already contains the family or
  phenomenon.
- **Finite quotient:** follows from a proved statement and a finite group
  action.
- **Search boundary:** a bounded primary-source search report, not a
  theorem or priority claim.
- **Provenance:** an earlier local project supplied material now reproduced
  inside this package.
- **Pending:** not a current theorem and not evidence.

## Matrix

| ID | Claim | Evidence | Exact location | Current status | Fresh-review obligation |
|---|---|---|---|---|---|
| C1 | \(\operatorname{Trace}_n\) is a regular formal-cycle multiset map | External definition plus internal setup | CD §3.1--3.2; PROOF_PACKAGE Step 1 | supported over \(\mathbb C\) | verify formal-cycle degree and symmetric-product target |
| C2 | \(C_f(T)\) is determined by pure fixed trace data | Internal proof | PROOF_PACKAGE Step 2 | supported | confirm fixed equation \(q=p-(1-a)x\) and trace \(p'\) |
| C3 | \(C_f'(s)=0\) for \(s=1-a\) | Internal proof | PROOF_PACKAGE Step 2 | supported in algebraically closed characteristic zero | replay squarefree residue identity and nonreduced local factor |
| C4 | fixed traces leave at most \(d-1\) Jacobians | C2--C3 | PROOF_PACKAGE Step 2 | supported | verify \(C_f'\) is nonzero of degree \(d-1\) |
| C5 | the quartic bound is at most \(3\), not \(7\) | C4 | PROOF_PACKAGE Step 2 | supported | reject every seven-candidate transcription |
| C6 | with fixed \(a\ne1\), period-\(\le2\) formal traces have finite fibers | External theorem | CD author PDF, Theorem 4.2 | supported over \(\mathbb C\) | verify fixed-Jacobian input and \(a\ne1\) |
| C7 | pure trace fibers over all \(a\ne1\) are finite | C4 plus C6 | PROOF_PACKAGE Step 3 | supported over \(\mathbb C\) | confirm finite union over Jacobian candidates |
| C8 | on \(a=1\), formal \(\operatorname{Trace}_2\) is determined by \(\operatorname{Trace}_1\) | Internal proof | PROOF_PACKAGE Step 4 | supported | replay tensor algebra and fixed-cycle subtraction |
| C9 | the \([1111]\) fixed-trace fibers are finite | External theorem plus finite normalization | Sugiyama; PROOF_PACKAGE Step 5 | supported over \(\mathbb C\) | verify \(h=x+p\) has all multipliers \(\ne1\); no use on other strata |
| C10 | the \([31]\) stratum has finite fixed-trace fibers | Internal proof | PROOF_PACKAGE Step 5 | supported | check \(p=(x-r)^3(x+3r)\) and \(-64r^3\) |
| C11 | the \([211]\) stratum has finite fixed-trace fibers | Internal proof | PROOF_PACKAGE Step 5 | supported | check \(A=u^2(u-v)\), \(B=-v^2(u-v)\), and all boundaries |
| C12 | \([22]\cup[4]\) is exactly \(E=\{p=(x^2-L)^2\}\) | Internal proof; direct precedent for family | PROOF_PACKAGE Step 5; CD Example 4.3 | supported | verify converse from \(0^{\times4}\) and uniqueness of \(L\) |
| C13 | the exact common lower fiber on \(E\) is \((0^4,2^{12})\) | Internal proof; direct precedent in substance | PROOF_PACKAGE Steps 4--5; CD Example 4.3 | supported | preserve formal multiplicities |
| C14 | the exact non-quasi-finite locus of \(\mathfrak T_{\le2}\) is \(E\) | C7--C13 plus finite-type criterion | PROOF_PACKAGE Step 6 | author-supported | verify pointwise quasi-finiteness criterion outside \(E\) |
| C15 | the residual action is \(L\mapsto\zeta L\), so \(E/\mu_3=\mathbb A^1_{L^3}\) | Internal proof / finite quotient | PROOF_PACKAGE Steps 1 and 6 | supported | recheck diagonal scaling convention |
| C16 | the period-three cyclic quotient is free of rank \(64\) | Internal proof | PROOF_PACKAGE Step 7 | supported | verify leading monomials and absence of points at infinity |
| C17 | the cyclic Jacobian equals \(\operatorname{tr}(Df^3)\) | Internal proof | PROOF_PACKAGE Step 7 | supported | multiply matrices and check cyclic signs |
| C18 | the trace--residue exponent is \(t^3\) for the second moment | External method plus internal application | CDS; PROOF_PACKAGE Step 7 | supported | distinguish \(\operatorname{Tr}(M_{t^2})\) from the residue numerator |
| C19 | only \(\varepsilon^6\) and \(L^3\varepsilon^4\) survive | Internal proof | PROOF_PACKAGE Step 8 | author-supported | replay weights, separated algebra, every Puiseux cluster, and diagonal branch |
| C20 | the formal fixed contribution to the period-three second moment is zero | Internal proof | PROOF_PACKAGE Step 9 | supported | use \(q^2=0\), not the false identity \(q=0\) |
| C21 | the first finite slope certificate gives \(D_2=-1572864\) | Internal finite ledger / provenance cross-check | PROOF_PACKAGE Step 10 | author-supported | independently verify \(H(2,1)\), \(A_{2,2}\), and powers of \(4\) |
| C22 | the tensor-Laurent ledger independently gives \(D_2=-1572864\) | Internal proof | PROOF_PACKAGE Step 11 | author-supported | replay all \(\rho\), \(\mu\), signs, and cyclic multiplicities |
| C23 | the normal-form ledger gives \(C_2=-1296000\) | Internal proof | PROOF_PACKAGE Step 12 | author-supported | replay every recurrence row and six contribution groups |
| C24 | \(S_2^{(3)}(L)=-1296000-1572864L^3\) | C19--C23 | PROOF_PACKAGE Step 12 | author-supported | compare both slope ledgers and formal subtraction |
| C25 | fixed support has no residual formal-period-three length | Internal proof | PROOF_PACKAGE Step 13 | supported | replay formal elimination for root multiplicities \(2\) and \(4\) |
| C26 | pointwise formal-period-three length is \(60\) | C16 and C25 | PROOF_PACKAGE Step 13 | supported | verify \(64-4\) with schemes, not reduced points |
| C27 | the cyclewise second moment is \(-432000-524288L^3\) | C24--C26 | PROOF_PACKAGE Step 13 | supported | divide by three only after pointwise subtraction |
| C28 | \(\mathfrak T_{\le3}\) has finite geometric fibers | C7--C15 and C24 | PROOF_PACKAGE Step 14 | author-supported | check the exceptional lower fiber is exactly \(E\) |
| C29 | \(\mathfrak T_{\le3}\) is quasi-finite on \(\mathcal H^1_4\) | C28 plus Stacks Tag 02NH | PROOF_PACKAGE Step 14 | author-supported | verify chosen trace target is finite type and quasi-compact |
| C30 | the descended period-\(\le3\) map is quasi-finite on the finite quotient | C15 and C28 | PROOF_PACKAGE Step 14 | author-supported | replay quotient-fiber argument |
| C31 | the pure-trace cutoff is sharply \(3\) | C13--C15 and C29--C30 | PROOF_PACKAGE Step 14 | author-supported | confirm cutoff definition is quasi-finite, not injective |
| C32 | no direct indexed statement of this unified package was located | Search boundary | CITATION_VERIFICATION; NOVELTY_ASSESSMENT | bounded search only | redo current primary-source search |
| C33 | Paper 15 absorbs Paper 12 and cannot be submitted in parallel with it | Publication-scope decision | all source-design documents | frozen policy | verify no dual-publication plan appears later |
| C34 | proof confidence has passed \(9.0\) | none | REVIEW_SUMMARY | false at current stage | fresh reviewer must certify at least \(9.0\) |
| C35 | Parts B--C hold over all algebraically closed characteristic-zero fields | none | anti-claims | explicitly not claimed | would require a separate descent argument |
| C36 | the trace map is globally injective or has a stated exact degree | none | anti-claims | explicitly not claimed | no action |
| C37 | \(P(d)=3\) for every \(d\) | none | anti-claims | explicitly not claimed | no action |

## Primary dependency diagram

\[
\begin{array}{c}
\operatorname{Trace}_1
\longrightarrow
C_f
\longrightarrow
C_f'(s)=0
\longrightarrow
\text{at most three quartic Jacobians}
\\[4pt]
a\ne1
\longrightarrow
\text{Cantat--Dujardin Theorem 4.2}
\longrightarrow
\text{finite lower fibers}
\\[4pt]
a=1
\longrightarrow
[1111]\cup[31]\cup[211]\cup[22]\cup[4]
\longrightarrow
E=\text{only positive-dimensional lower fiber}
\\[4pt]
E
\longrightarrow
S_2^{(3)}=-1296000-1572864L^3
\longrightarrow
L^3
\longrightarrow
\mathfrak T_{\le3}\text{ quasi-finite}.
\end{array}
\]

## Claim-language controls

Permitted:

- “pure trace data leaves at most three quartic Jacobian candidates”;
- “exact non-quasi-finite locus on the single-factor normalized quartic
  space”;
- “quasi-finite, not necessarily injective”;
- “formal period-three second moment separates the exceptional curve”;
- “bounded primary-source search found no direct statement of the unified
  package”;
- “author-side proof pending independent replay.”

Forbidden:

- “the Jacobian is known” in the pure-trace theorem;
- “seven Jacobian candidates”;
- “all quartic Hénon compositions”;
- “all loxodromic automorphisms”;
- “all algebraically closed characteristic-zero fields” for Parts B--C;
- “period three uniquely identifies every map”;
- “the moment alone classifies quartic moduli”;
- “new exceptional family”;
- “new residue or dynatomic method”;
- “first ever” or any absolute priority wording;
- “independently certified” before the fresh review passes;
- any statement that Paper 12 and Paper 15 may be submitted separately with
  overlapping central theorems.
