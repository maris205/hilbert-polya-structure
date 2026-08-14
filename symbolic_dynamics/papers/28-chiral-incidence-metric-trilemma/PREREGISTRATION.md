# Preregistration — SD-C30

Freeze time: 2026-08-14 UTC, before manuscript integration.

## Question

Can the source-derived oblique Möbius-incidence family from Paper 27 be completed by a holomorphic reflected/adjoint double so that the critical line carries an honest self-adjoint Schatten-class determinant without sacrificing arithmetic selectivity?

## Frozen construction

On \(\mathcal H_\eta\), \(\eta>1\), use the bounded incidence similarity

\[
q_n=ZE_nZ^{-1},\qquad
T_s=ZD_s^AZ^{-1},\qquad
D_s^A=\sum_{p\in A}p^{-s}E_p.
\]

With the source-real weighted transpose \(\sharp\), study

\[
\mathcal B_s=
\begin{pmatrix}
0&T_s\\T_{1-s}^{\sharp}&0
\end{pmatrix}.
\]

The positive-metric adversary class consists of all bounded positive boundedly invertible \(G\) satisfying \(Gq_p=q_p^*G\) for every active atom.

## Primary endpoints

1. Exact common Schatten strip of \(\mathcal B_s\).
2. Whether the critical-line family is self-adjoint.
3. Exact two/three-atom mixed-Gram phase formula.
4. Which trace powers are removed or retained by the first honest \(\det_q\).
5. Whether a retained spectral moment varies with \(t\).
6. Whether that variation survives mutated, composite-only, and generic-poset controls.
7. Whether a positive metric can remove the Gram defect without atom collapse.

## Success and rejection rules

- An analytic determinant may be called honest only on a proved Schatten domain.
- Critical-line self-adjointness passes the local operator check but does not pass the fixed-operator route gate if the operator itself depends on \(t\).
- Arithmetic selectivity requires the effect to fail, or change by a proved arithmetic invariant, on aggregate non-arithmetic controls.
- A positive-metric completion fails if it is unitarily equivalent on the active sector to independent one-dimensional atom coordinates.
- Any target-zero-dependent construction, tuning, or evaluation is prohibited and would invalidate the candidate.

## Frozen route prior

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

Expected overall decision: REJECTED; Route B locked false.

## Two-stage note

Stage 1 freezes the object, endpoints, adversaries, and rejection rules in this file. Stage 2 integrates the already generated exact artifact and proofs into the manuscript. The manuscript may sharpen proofs or exposition but may not change the object or promote a failed route gate after inspecting the controls.
