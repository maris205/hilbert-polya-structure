# Proof-Audit Plan

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Execution class

This project is proof-only. The experiments directory is retained solely for
repository consistency. This document authorizes no scientific or symbolic
execution.

The only possible next activity, under separate authorization, is a
read-only human-style proof and citation audit of the ten source-design
files.

## Explicit prohibitions

Do not perform:

- numerical experiments;
- symbolic algebra or computer algebra;
- SymPy, SageMath, Mathematica, Maple, Magma, Singular, Macaulay2, or
  equivalent calculations;
- parameter scans;
- random sampling;
- periodic-point enumeration;
- finite-field or modular checks;
- coefficient-ledger scripts;
- Gröbner-basis computation;
- automated theorem proving;
- code generation;
- data or result generation;
- figure generation;
- LaTeX compilation;
- manuscript writing;
- source-lock creation.

A machine calculation may not be described as a “sanity check.” No
scientific run is admissible at this lifecycle.

## Fresh-review protocol

The reviewer must be independent of the source authoring pass and must
rederive the following items by hand from the written definitions and
primary sources.

### P1. Scope and trace convention

Verify:

- Part A is algebraically closed characteristic zero;
- Parts B--C are over \(\mathbb C\);
- the source is the single-factor \(\mathcal H^1_4\);
- \(\operatorname{Trace}_n\) uses formal-period cycles and multiplicities;
- the target is a finite product of symmetric products;
- quasi-finite is not replaced by injective.

Acceptance condition: no unproved base-change descent, no composition
scope, and no reduced-only reformulation appears.

### P2. Fixed algebra

Starting from

\[
f_{a,p}(x,y)=(ay+p(x),x),
\]

derive

\[
s=1-a,\qquad q=p-sx,\qquad A_q=k[x]/(q),
\]

and verify that the formal fixed traces are the eigenvalues of
multiplication by \(p'\).

Acceptance condition: the characteristic polynomial \(C_f\) is determined
by pure trace data alone.

### P3. The identity \(C_f'(s)=0\)

Independently prove both cases:

1. squarefree \(q\), using
   \[
   \sum_{q(\alpha)=0}\frac1{q'(\alpha)}=0;
   \]
2. non-squarefree \(q\), using a local factor
   \((T-s)^m\) with \(m\ge2\).

Acceptance condition:

\[
C_f'(s)=0
\]

with no division by \(C_f(s)\) in the nonreduced case.

### P4. Jacobian candidate count

Verify that \(C_f'\) is nonzero of degree \(d-1\) in characteristic zero.
Check

\[
J=s-1.
\]

Acceptance condition: at most \(d-1\) candidates, and at most \(3\) for
quartics. Any count of \(7\) is an automatic failure.

### P5. Cantat--Dujardin scope

Open the May 10, 2026 author PDF and inspect:

- formal trace definitions in §3.1--3.2;
- Theorem 3.7;
- Theorem 4.2;
- Example 4.3.

Acceptance condition: Theorem 4.2 is used only over \(\mathbb C\), with
fixed Jacobian, for \(a\ne1\), after P4.

### P6. Formal period two on \(a=1\)

Re-derive

\[
A_2=\mathbb C[x,y]/(p(x),p(y))
\]

and

\[
\operatorname{tr}(Df^2)=2+p'(x)p'(y).
\]

Verify the full length-\(16\) multiset and the length-\(4\) fixed-cycle
subtraction.

Acceptance condition: the formal period-two length is \(12\), including
nonreduced multiplicity, and is determined by fixed trace data.

### P7. The \([1111]\) stratum

For \(h=x+p\), verify that simple roots of \(p\) give fixed multipliers

\[
1+p'(\alpha)\ne1.
\]

Open Sugiyama's primary theorem and verify its \(V_4\) finite-fiber scope.

Acceptance condition: Sugiyama appears nowhere in the proof of
\([31]\), \([211]\), \([22]\), or \([4]\).

### P8. The singular root partitions

By hand, verify:

\[
[31]:
\quad
p=(x-r)^3(x+3r),
\quad
p'(-3r)=-64r^3;
\]

\[
[211]:
\quad
4r+u+v=0,
\quad
A=u^2(u-v),
\quad
B=-v^2(u-v),
\quad
\frac BA=-\left(\frac vu\right)^2.
\]

Then verify finite recovery of \(v/u\), \(u^3\), \(v\), and \(r\).

Acceptance condition: all ordering choices remain finite.

### P9. Boundaries and exceptional curve

Verify:

- \(u=0\) and \(v=0\) lead to \([31]\);
- \(u=v\ne0\) leads to \([22]\);
- \(u=v=0\) leads to \([4]\);
- \([22]\cup[4]\) is exactly
  \[
  E=\{p=(x^2-L)^2\};
  \]
- fixed trace \(0^{\times4}\) has no other quartic polynomial.

Acceptance condition: the exact lower fiber on \(E\) is

\[
(0^{\times4},2^{\times12}).
\]

### P10. Exact non-quasi-finite locus

Combine P4--P9 and the finite-type pointwise criterion.

Acceptance condition: every point outside \(E\) is a quasi-finite point of
\(\mathfrak T_{\le2}\), and every point of \(E\) lies on its
positive-dimensional fiber.

### P11. Period-three complete intersection

Recheck:

\[
F_i=(x_i^2-L)^2+\varepsilon(x_{i-1}-x_{i+1}),
\]

\[
t_\varepsilon
=
q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2).
\]

Verify by hand:

- rank \(64\);
- the cyclic signs;
- equality of the Jacobian determinant and derivative trace;
- the trace--residue exponent
  \[
  \operatorname{Tr}(M_{t^2})=\operatorname{Res}(t^3).
  \]

Acceptance condition: no hidden computation or reduced-point assumption.

### P12. Two-term support

Replay the weight equation and verify that only

\[
\varepsilon^6,\quad
L^3\varepsilon^4,\quad
L^6\varepsilon^2,\quad
L^9
\]

are initially possible. Check:

- separated-algebra removal of \(L^9\);
- all Puiseux root-cluster valuations for \(L\ne0\);
- diagonal fixed-branch zero;
- polynomial continuation to \(L=0\).

Acceptance condition:

\[
S_2(L,\varepsilon)
=
C_2\varepsilon^6+D_2L^3\varepsilon^4.
\]

### P13. Exact coefficient ledgers

Without CAS, replay:

1. the finite \(H/A\) slope certificate;
2. every Laurent coefficient \(\rho_{3,h}(e)\);
3. \(\mathcal C_{2,0}=-6\) and all zero terms;
4. the normal-form recurrences for \(R(e_0,e_1,e_2)\);
5. every row of the exponent-pattern table;
6. every contribution to \(C_2\).

Acceptance conditions:

\[
D_2=-1572864,
\qquad
C_2=-1296000,
\]

and the two slope routes agree exactly.

### P14. Formal period-three subtraction and local length

Verify on the fixed algebra:

\[
q^2=0,\qquad
t_\varepsilon^2=0.
\]

At root multiplicities \(r=2,4\), replay formal elimination in
\((\delta,u,v)\) and check the remaining equation has order exactly \(r\).

Acceptance conditions:

- no residual fixed support;
- pointwise formal period-three length \(64-4=60\);
- cyclewise division by \(3\) occurs only after subtraction.

### P15. Quotient and global quasi-finiteness

Verify the residual action

\[
L\mapsto\zeta L,
\qquad
\zeta^3=1,
\]

and invariant coordinate \(L^3\). Check that equality of full period-three
multisets implies equality of the second moments, hence finite \(L\)-fibers.

Acceptance conditions:

- \(\mathfrak T_{\le3}\) has finite geometric fibers;
- finite type implies quasi-finite;
- the descended quotient map is quasi-finite;
- period two remains non-quasi-finite on \(E/\mu_3\).

### P16. Citation and collision audit

Open every primary link in CITATION_VERIFICATION.md. Confirm:

- the author PDF controls over arXiv v1;
- Sugiyama's domain is \(V_d\);
- no theorem source is extended beyond \(\mathbb C\);
- residue methods are credited;
- the bounded collision search is current.

Acceptance condition: any direct collision or scope mismatch triggers
source repair, not rhetorical downgrading.

### P17. Publication and anti-claim audit

Confirm:

- Paper 15 absorbs Paper 12;
- parallel overlapping submission is prohibited;
- no global injectivity, exact degree, all-degree cutoff, positive
  characteristic, or composition claim appears;
- the one period-three moment is confined to separating \(E\);
- no computation is described as evidence.

## Exit gate

All P1--P17 must pass. The fresh reviewer must explicitly assign:

- novelty at least \(6.5\);
- standalone size at least \(6.0\);
- proof confidence at least \(9.0\).

The review must issue a separate artifact only under new authorization. This
plan does not authorize creation of that artifact.

If proof confidence remains below \(9.0\), the package stays at source
design. If a proof step fails, the theorem must be downgraded to
**NOT CURRENTLY JUSTIFIED** rather than repaired by computation.

## Expected outputs at the present stage

None:

- no code;
- no data;
- no results;
- no computation;
- no figures;
- no manuscript;
- no build;
- no source lock;
- no review artifact.
