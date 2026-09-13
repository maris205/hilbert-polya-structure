# Paper20 independent manuscript-source review (R2)

**Review ID:** `PAPER_SOURCE_R2_2026_08_22`

**Scope:** read-only audit of the author-stopped manuscript source.  No
compilation, CAS run, experiment, transport access, upload, or author-file
edit was performed.  This note is a reviewer-owned artifact and is outside
the author source aggregate.

## Reviewed identity

The four files named by the source lock were rehashed byte-for-byte:

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 37,343 | 981 | `032659df2fefefdc6f9ad0f5df81b1e00367e9132feff2f4b69b3e70efa4b26c` |
| `paper/math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,331 | 73 | `5bd232714f5875a97c368342bbb978ee4cadda5893ce23c9af092c8895840774` |
| `paper/BUILD_METADATA_R0.json` | 3,588 | 1 | `2d00e67a28e2514ecf9d2a1b0e8f3b9d03e4471defe4fdc1286ff1200064bd2a` |

The bound source lock is
`experiments/source_lock.json`, SHA-256
`57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`,
11,847 bytes, one LF.  All four file rows and the upstream `PAPER_PLAN.md`
row in `BUILD_METADATA_R0.json` match their on-disk bytes.  The metadata JSON
passes strict UTF-8/duplicate-key/nonfinite-number/terminal-LF canonicality,
has null self-identity fields, and reports build, CAS, experiment, figure,
publication, transport, and upload permissions as false.  No forbidden build
or transport output was present.

## Mathematical replay

The source faithfully instantiates the locked family over algebraically closed
characteristic-zero (K), integer (g\geq5):

\[
 V=q_1^2q_2^2+q_1^g,\qquad W=p_1^2p_2^2+p_2^g,
 \qquad F_g=T\circ S.
\]

The following checks passed from the displayed definitions, without relying
on a citation or numerical calculation.

1. The triangular inverses are explicit, and the symmetric-Hessian pullback
   calculation proves preservation of
   (dq_1\wedge dp_1+dq_2\wedge dp_2).
2. The phase rows are the actual differentiated support rows
   \[
   A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
   B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},
   \]
   and multiplication gives
   \[
   C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
   \]
3. The two-stage cone (1\le r=u_2/u_1<(g-2)/2) is used rather than an
   invalid single strict cone across the phase equality.  The source proves
   \(f_g(r)=(g-1)(2+r)/(g+3+2r)\), monotonicity, both endpoint inequalities,
   and componentwise growth for every (g\ge5).
4. The (S)- and (T)-phase carried-coordinate gaps are written explicitly;
   the (T)-selector uses
   \(v_2/v_1=(2+r)/(g-1)>2/(g-2)\).  The initial carried degree-one
   coordinates and all later carried terms are covered by the induction.
5. Nonnegative coefficients and characteristic zero give the stated
   no-cancellation step.  The resulting recurrence is
   \(v_{n+1}=A_gu_n\), \(u_{n+1}=C_gu_n\), with
   \(u_n=C_g^n(1,1)^\mathsf T\).
6. (C_g-A_g) is entrywise positive and the cone gives (u_{n,2}>u_{n,1}),
   so (q_2) sees the total coordinate degree.  The trace, determinant, and
   discriminant give eigenvalues
   \((\sqrt g\pm1)^2\), and positivity supplies Perron reachability and
   visibility.  The scalar recurrence and the strict comparison with
   \((g-1)^2) are algebraically consistent.

The proof therefore satisfies the source-lock L1--L7 dependency order and
does not promote a half-step matrix, a generic Newton-fan assertion, or an
external citation into evidence.

## Citation, collision, and permission checks

All seven citation keys used by `main.tex` resolve uniquely in
`references.bib`.  Their uses match the locked roles: planar degree-product
background, higher-dimensional degree-growth context, dynamical-degree
spectral terminology, and a four-dimensional coupled-Hénon neighbor.  The
paper does not attribute the displayed recurrence, symplecticity, selector
inequalities, no-cancellation argument, or Perron root to the literature.
The P12--P19 table and the limitations section retain the bounded-collision
and no-priority/firstness boundaries.  The manuscript makes no forbidden
claim about arbitrary sparse shears, positive characteristic, topological or
arithmetic entropy, periods, traces, torus translates, universal conjugacy,
or numerical/CAS proof.  The source metadata leaves manuscript/build and
publication permissions closed.

Static inventory checks also pass: braces and square delimiters balance,
`begin`/`end` environments have matching multisets, labels are unique, and
all `\\ref`/`\\eqref` targets are defined.  These checks alone do not certify
that every label is attached to a numbered environment, which is the issue
below.

## Blocking source defect

Five equation labels are placed inside unnumbered display math delimiters
`\\[ ... \\]` in `paper/main.tex`:

| label | display line (approx.) | later use |
|---|---:|---|
| `eq:Sface` | 520--521 | `\\eqref` at line 687 |
| `eq:Tfirstgap` | 556--559 | `\\eqref` at lines 687 and 694 |
| `eq:Tface` | 576--577 | `\\eqref` at lines 687 and 695 |
| `eq:Tsecondgap` | 581--583 | `\\eqref` at lines 688 and 694 |
| `eq:ratiomap` | 624--626 | currently not referenced, but still unnumbered |

`\\[ ... \\]` is an unnumbered display environment.  A `\\label` there does
not create a stable equation number; depending on the preceding counter state
it can resolve to the previous theorem/equation label or otherwise produce an
incorrect cross-reference.  Thus the proof text's `\\eqref{eq:Sface}` etc. do
not reliably identify the inequalities they are intended to cite, despite the
labels being syntactically present.  This is a source-level reproducibility
and proof-navigation defect, not a mathematical change to the inequalities.

Minimal admissible repair: put each referenced display in a numbered
`equation` environment with its existing label (and either number or remove
the currently unused `eq:ratiomap` label), or remove all corresponding
`\\eqref` references and use unlabelled prose.  After repair, the complete
source hash, metadata binding, and this R2 review must be regenerated; no
reviewer is authorized to edit the manuscript.

## Verdict

`PAPER_SOURCE_R2_BLOCK`

The theorem/proof content, citation scope, metadata canonicality, and
permissions pass, but the five unnumbered referenced displays prevent a
clean, stable manuscript-source handoff.  A new author-stopped snapshot with
the label environments corrected is required for R2 re-review.  This verdict
does not authorize compilation, publication, transport, or any downstream
artifact.
