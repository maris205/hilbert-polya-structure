# Paper20 independent manuscript-source review (R2, repaired snapshot)

**Review ID:** `PAPER_SOURCE_R2_REPAIRED_2026_08_22`

**Scope:** fresh read-only review of the author-stopped source after the
equation-label repair.  This artifact supersedes the `PAPER_SOURCE_R2_BLOCK`
finding for the preceding main-file identity only; it does not alter that
historical receipt.  No compilation, CAS/symbolic execution, experiment,
transport access, upload, or author-file edit was performed.

## Identity and inventory

The authorized source identities rehash exactly as follows:

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 37,423 | 981 | `2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014` |
| `paper/math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,331 | 73 | `5bd232714f5875a97c368342bbb978ee4cadda5893ce23c9af092c8895840774` |
| `paper/BUILD_METADATA_R0.json` | 3,588 | 1 | `1ac4fa5c1f3e575f5e09c4a3e311f4a59854a674585c92d80df4434a47605446` |

The bound source lock remains
`experiments/source_lock.json`, SHA-256
`57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`,
11,847 bytes/LF1.  `PAPER_PLAN.md` remains the locked upstream row
(`4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3`,
22,064 bytes/LF397).

The updated `BUILD_METADATA_R0.json` is strict-canonical JSON: duplicate keys,
nonfinite numbers, CR, NUL, BOM, and non-UTF-8 input are rejected; recursive
Unicode-key ordering and compact serialization reproduce the exact byte
stream.  Its self identity is null/self-excluded.  All four manuscript rows
and the plan row resolve to the actual bytes and hashes.  Build/CAS,
experiment/data/figure, publication, transport, and upload permissions remain
false; planned build status is `NOT_RUN`, with null artifact identities and no
forbidden output files present.

## Label repair and static source integrity

The prior blocker is closed in this identity.  `eq:Sface`, `eq:Tfirstgap`,
`eq:Tface`, and `eq:Tsecondgap` are now each inside numbered `equation`
environments and are the targets of all corresponding `\\eqref` calls.  The
unused `eq:ratiomap` label was removed from its unnumbered display.  No label
remains inside `\\[...\\]`, `equation*`, or `align*`; labels are unique and all
`\\ref`/`\\eqref` targets are defined.  Braces and square delimiters balance,
and the begin/end environment multisets match.

The four source files are UTF-8/LF-only, have no BOM, CR, or NUL, and each ends
with exactly one terminal LF.  The paper tree contains only the declared
source/metadata files (plus the upstream plan); no `.aux`, `.bbl`, `.blg`,
`.log`, `.pdf`, build, result, figure, or transport output was generated.

## Independent proof replay

The repaired source still matches the frozen theorem exactly: (K) is
algebraically closed of characteristic zero, (g\in\mathbb Z), (g\ge5),
\[
V=q_1^2q_2^2+q_1^g,qquad W=p_1^2p_2^2+p_2^g,qquad F_g=T\circ S.
\]

The following checks pass directly from the displayed formulas.

* The triangular inverses are polynomial, and symmetric Hessians prove that
  both shears preserve (dq_1\wedge dp_1+dq_2\wedge dp_2).
* Differentiating the literal supports gives
  \[
  A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\quad
  B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},\quad
  C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
  \]
* The proof uses the correct two-phase cone
  (1\le u_2/u_1<(g-2)/2), not a false strict cone across the equality
  (v_{n+1}=A_gu_n).  The ratio map, its positive derivative, both endpoint
  inequalities, and componentwise growth are valid for every (g\ge5).
* The (S)-phase and (T)-phase selector inequalities include all carried
  coordinates.  In particular, the second (T)-row uses
  (v_2/v_1=(2+r)/(g-1)>2/(g-2)), and the initial degree-one carried terms
  are handled separately.
* Positive integer coefficients in characteristic zero and strict degree gaps
  give the no-cancellation induction.  Therefore
  (v_{n+1}=A_gu_n), (u_{n+1}=C_gu_n), and
  (u_n=C_g^n(1,1)^\mathsf T).
* (C_g-A_g) is entrywise positive, while cone invariance gives
  (u_{n,2}>u_{n,1}).  Thus (q_2) sees the maximum of all four coordinate
  degrees.  The trace/determinant calculation gives
  (lambda_\pm=(\sqrt g\pm1)^2), and positivity gives Perron reachability
  and visibility.  The scalar recurrence and
  ((g-1)^2-(\sqrt g+1)^2=\sqrt g(\sqrt g-2)(\sqrt g+1)^2>0) are consistent.

This is the locked L1--L7 proof dependency, with no generic Newton-fan,
half-step, numerical, or external-citation substitution.

## Citation, collision, and permission boundaries

Every citation key in `main.tex` resolves uniquely in `references.bib`.  The
seven entries are used only for the locked roles: planar degree-product
background, higher-dimensional degree-growth context, dynamical-degree
spectral terminology, historical valuation context, and the bounded
four-dimensional coupled-Hénon neighbor.  The exact Paper20 recurrence,
symplecticity, selectors, no-cancellation argument, and Perron root are proved
internally.  The P12--P19 table and limitations section retain the bounded
collision scope and explicitly reject priority/firstness and universal claims.

The source contains no claim about arbitrary sparse potentials or words,
positive characteristic, topological/arithmetic/measure entropy equality,
periods/traces/torus translates, universal conjugacy, or CAS/numerical proof.
No downstream authority is asserted: manuscript edits, build, publication,
transport, and upload remain locked false in metadata and source lock.

## Verdict

`PAPER_SOURCE_R2_PASS`

The repaired manuscript source is hash-bound, label-safe, theorem-faithful,
citation-scoped, and permission-safe for the authorized source-only review.
This is a source review only; it does not authorize compilation, a PDF,
publication, transport, experiments, or any downstream artifact.
