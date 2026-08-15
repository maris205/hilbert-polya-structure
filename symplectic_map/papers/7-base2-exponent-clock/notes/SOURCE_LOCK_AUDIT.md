# Independent Source-Lock Audit

**Audit date:** 2026-08-14  
**Scope:** Paper 7 seven-file source-lock package only  
**Execution authority:** read-only mathematical and protocol review; no
candidate execution authorized or performed

## Verdict history

### Version 1: `REPAIR`

The version-1 package had a mathematically sound core: the local unit-circle
theorem, frozen exact 2-adic valuation corollary, Frobenius--Hensel norm
model, mod-2 obstruction, period-two/three exclusion, degree-four
insufficiency witness, cycle-polynomial identity, repeat-return boundary, and
the all-period `OPEN` residue were all independently checked and accepted.

Deployment nevertheless remained blocked because the set-theoretic
least-period component was not specified unambiguously and several proof,
control, disclosure, and citation details required source-lock hardening.
The audited version-1 source-lock SHA-256 was

```text
bb2019349e3616ba3f03b4d33a57e4b70c8284eeaa4424cbf25f26f596336e4b
```

### Version 2: `PASS`

A narrow independent re-review found all eight required repairs closed, the
JSON valid, and no new mathematical or evidentiary drift. The frozen
version-2 source-lock SHA-256 is

```text
205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1
```

## Eight-item closure ledger

| ID | Required repair | Version-2 disposition |
|---|---|---|
| A1 | Freeze an unambiguous set-theoretic exact-period component, while keeping formal dynatomic and scheme-multiplicity records separate. | `CLOSED`: the monic radical/set-difference formula for \(\Psi_n^{\rm set}\) is explicit in the source lock and experiment plan. |
| A2 | Align the local theorem with characteristic zero and replace the malformed coefficient-field notation by \(\mathbb Q(u)=\mathbb Q[U]/(Q(U))\). | `CLOSED` |
| A3 | State that the \(2^n\) distinct Hensel lifts exhaust \(g^n-X\), and prove exact dynamical period from Hensel uniqueness. | `CLOSED` |
| A4 | List the degree-two/three irreducibles and make the irreducible degree-four reciprocal witness and coefficient correspondence explicit. | `CLOSED` |
| A5 | Distinguish a \(g^{nr}\) repeated return from an exact period-\(nr\) orbit; reconcile four dynamical controls plus upstream regression and freeze the Chebyshev period-two outcome. | `CLOSED`: \(\Psi_2=X^2+X-1\), \(B_2=-1\), and \(\Lambda=-4\). |
| A6 | Make the exact rational field norm the independent resultant certificate and prohibit post-hoc finite-field-prime selection. | `CLOSED`: reduction modulo the predeclared \(q=3\) is optional and diagnostic only. |
| A7 | Complete the pre-lock development disclosure. | `CLOSED`: periods 1--8 are development-seen; the second periods 4--7 benchmark records degree-zero sign gcds, nonzero resultants, and runtime below two seconds per period. |
| A8 | Add the Morton--Silverman dynatomic source and correct the scope assigned to Benedetto--Goksel. | `CLOSED` |

## Final boundary and access statement

The version-2 package preserves the exact conclusion

\[
w(\Lambda_C)=n\,w(2),
\qquad
\Lambda_C\in\mathbb Q\Longrightarrow
\Lambda_C=2^n m\quad(m\text{ odd}),
\]

for exact periods \(n\ge2\), while the all-period exclusion
\(B_C\ne\pm1\) remains explicitly `OPEN_FOR_N_GE_4`. Finite periods 2--7
may be used only for development-seen reproduction and implementation
falsification, never as blind or all-period evidence.

Neither audit executed a registered or official candidate run. Neither audit
accessed an external prime table, generated a prime target array, accessed
Riemann-zero data, performed prime/zero matching, or opened a prime/zero
stage.
