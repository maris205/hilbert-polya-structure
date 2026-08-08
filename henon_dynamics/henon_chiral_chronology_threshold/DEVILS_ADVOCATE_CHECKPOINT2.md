# HCS-C21 Devil's Advocate report -- Checkpoint 2

**Initial verdict:** REVISE
**Final re-review verdict:** PASS
**Re-review date:** 2026-08-08

## Verdict

The revised proof chain is complete and noncircular:

\[
\text{ordered-edge recovery}
\Longrightarrow
\text{geometric }D_6\text{ cover}
\Longrightarrow
g(E_6)=1
\]

\[
\Longrightarrow
\mathbb Q(E_6)^{\langle\tau\rangle}
=\mathbb Q(A,\eta w)
\Longrightarrow
g(E_6/\langle\tau\rangle)=1
\Longrightarrow
\tau^*|_{H^1}=1.
\]

No unresolved Critical or Major issue remains.

## Independent re-review

The adversarial re-review was read-only.  It rebuilt outputs in a temporary
location and did not modify project files.

- certificate SHA-256 reviewed by the adversarial pass:
  `1eaa5abec31259fd6140f73618c5d57f69a9d96d6d4916000b75cdef66473dd0`;
- that rebuilt certificate matched the then-frozen bytes;
- independent checker: PASS;
- named checks: 133;
- fail-closed regression tests: 14/14 PASS;
- checker imports no producer or predecessor implementation.

After that PASS, two reviewer-requested Minor changes sharpened the
machine-readable threshold scope and made the checker compute the subgroup
index directly.  The current certificate SHA-256 is
`5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc`.
The mathematical outputs are unchanged; producer, checker, and all 14 tests
were rerun successfully after the Minor edits.

## Resolution ledger

| Initial Major finding | Resolution | Evidence |
|---|---|---|
| A rational specialization did not prove geometric connectedness. | Closed. | The producer and checker now contain the full $q(\eta)=c\eta+d$ absolute-irreducibility case split, plus the nonsquare geometric discriminant. |
| The ordered edge might be an auxiliary object with an attached radical label. | Closed. | Exact even/odd orbit sums recover $\eta$; the recurrence then recovers all six coordinates and all three cubic roots. |
| The quotient equation was not yet an exact fixed-field calculation. | Closed. | The derivation proves $\tau=\iota c$, $\tau^2$ generates $A_3$, $\tau^3=\iota$, and closes the inclusion by the index-two degree.  The checker and a tamper test freeze the conclusion. |
| C21 forward-edge time was being conflated with C20's coordinate convention. | Closed. | The certificate and documentation state that C21 uses $H_A^{-1}$, C20 uses $H_A$, and reversal conjugates them. |
| The $n=7$ threshold could be read as a full saturated-period classification. | Closed. | The certificate and prose now use an existential, source-identified and repository-certified component scope. |
| The period-six reversible marker was being mixed with the chiral ordered cover. | Closed. | $D_6^{\mathrm{mark}}$ and $E_6$ are separated everywhere; the fiber-product intersection before normalization is recorded. |
| The clock-divisibility theorem lacked dominance/free-locus assumptions. | Closed. | The current theorem assumes a dominant nonconstant rational map and explicitly leaves boundary maps, $k=0$, and multivalued correspondences open. |

## Strongest counter-argument

The strongest remaining criticism limits significance rather than
correctness:

> C21 compares two low-period certified components.  The period-six
> cohomological collapse is ultimately explained by torsion translation on a
> genus-one curve, while the coarse marker coincidence descends to period
> one.  It does not create an all-period Hénon tower, intrinsic repetition
> law, Fredholm determinant, or Hilbert--Pólya operator.

The project accepts this criticism.  Its valid contribution is a
chronology--cohomology collapse theorem, a scoped first-occurrence result, and
a lower-period marker-alias obstruction.  Route-A A2 and A3 remain failures.

## Stress tests

| Test | Result |
|---|---|
| Remove the $\eta=1$ specialization: does connectedness remain proved? | PASS; the absolute-irreducibility ledger is independent. |
| Does an ordered edge intrinsically recover the radical? | PASS; exact alternating-sum recovery. |
| Can infinity add hidden ramification and change the genus? | PASS; all three local branches use integral powers. |
| Can the quotient be incorrectly replaced by $w^2=16A^2-8A+5$? | No; the rotation invariant is $v=\eta w$. |
| Can $\tau$ act nontrivially on $H^1$ after the genus-one quotient? | No; the degree-six quotient is unramified and $\tau$ is a translation. |
| Are C21 and C20 time directions compatible? | PASS with the explicit inverse/reversal convention. |
| Does the marker shadow define a chiral-cover bridge? | No; it is a period-one coarse-marker alias. |
| Does the divisibility theorem exclude constant or boundary maps? | No; these are explicitly outside scope. |
| Does the threshold classify all period-seven components? | No; it is existential for the HCS-C20 certified component. |
| Is this a positive Hilbert--Pólya construction? | No; it is correctly evaluated as A2/A3 FAIL. |

\[
\boxed{\text{Checkpoint 2: PASS}}
\]
