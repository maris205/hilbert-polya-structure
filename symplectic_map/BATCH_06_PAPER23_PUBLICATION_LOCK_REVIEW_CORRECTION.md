# Paper 23 Publication-Lock Review — Immutable Kernel Correction

Correction date: 2026-08-25 UTC

## 1. Role, scope, and verdict

I performed this check as a fresh independent root-governance correction
reviewer. I authored none of Paper 23's candidate records, project files,
locks, plans, scopes, earlier reviews, or Batch 06 roots. I did not inherit the
original reviewer's verdict.

The only object corrected by this record is the literal mathematical meaning
of lines 431--432 of the immutable publication-lock review. Every other line
of that review survives the consequential-drift audit unchanged.

The original review remains byte-for-byte immutable. This file neither edits
nor replaces it.

## 2. Immutable reviewed object

The original review is exactly:

- path:
  `papers/23-hamiltonian-quartic-spectral-escape/notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`;
- SHA-256:
  `0ecfdc71a2de08e37311cb4683e393e397bb8e87854b01eb021a7db7f4d46dec`;
- size: 23,481 bytes;
- LF count: 633;
- mode: 0644;
- type: regular, non-symlink, link count one;
- terminal line: `PUBLICATION_LOCK_PASS`.

The file is valid UTF-8, has exactly one terminal LF, and has no BOM, CR, or
NUL byte.

## 3. Exact two-line defect and sole supersession

The two false literal formulas in the original review are:

1. line 431: `ker(A_g)=span(0,0,1,-1)^T`;
2. line 432: `ker(B_g)=span(1,-1,0,0)^T`.

They are superseded, respectively and only, by:

\[\ker(A_g+I_4)=\operatorname{span}(0,0,1,-1)^{\mathsf T},\]

\[\ker(B_g+I_4)=\operatorname{span}(1,-1,0,0)^{\mathsf T}.\]

No ordinary-kernel claim survives. The exact ordinary kernels are

\[\ker(A_g)=\ker(B_g)=\{0\}.\]

No other sentence, formula, hash, metadata statement, provenance statement,
permission, lifecycle statement, or terminal token in the original review is
superseded by this correction.

## 4. Independent proof of the corrected formulas

The frozen matrices are

\[
A_g=
\begin{pmatrix}
g-1&0&0&0\\
0&g-2&0&0\\
2&2&1&2\\
2&2&2&1
\end{pmatrix},
\qquad
B_g=
\begin{pmatrix}
1&2&2&2\\
2&1&2&2\\
0&0&g-2&0\\
0&0&0&g-1
\end{pmatrix}.
\]

With the first two and last two coordinates grouped, (A_g) is block lower
triangular and (B_g) is block upper triangular. Their diagonal blocks are,
in the appropriate order,

\[\operatorname{diag}(g-1,g-2),\qquad
\begin{pmatrix}1&2\\2&1\end{pmatrix}.\]

Therefore

\[\det(A_g)=\det(B_g)=(g-1)(g-2)(1-4)
=-3(g-1)(g-2).\]

For every allowed integer (g\ge10) over a characteristic-zero field, this
scalar is nonzero. Hence both matrices are invertible and their ordinary
kernels are zero.

Put

\[v=(0,0,1,-1)^{\mathsf T},\qquad
w=(1,-1,0,0)^{\mathsf T}.\]

Direct row multiplication gives

\[A_gv=(0,0,-1,1)^{\mathsf T}=-v,\qquad
B_gw=(-1,1,0,0)^{\mathsf T}=-w.\]

Moreover,

\[
A_g+I_4=
\begin{pmatrix}
g&0&0&0\\
0&g-1&0&0\\
2&2&2&2\\
2&2&2&2
\end{pmatrix}.
\]

Its kernel equations force (x_1=x_2=0) and (x_3+x_4=0), proving the
first shifted-kernel formula. Likewise,

\[
B_g+I_4=
\begin{pmatrix}
2&2&2&2\\
2&2&2&2\\
0&0&g-1&0\\
0&0&0&g
\end{pmatrix}.
\]

Its kernel equations force (x_3=x_4=0) and (x_1+x_2=0), proving the
second shifted-kernel formula. The two displayed one-dimensional subspaces
have zero intersection.

Thus, on the common covector kernel, the general spiked matrices act as
(-I), and their product acts as (I). For the frozen profile the two
(-1)-eigenspaces intersect trivially. The independent identity

\[R_g(1)=3g(g-1)(3g^2-11g+4)\ne0\]

then confirms that (C_g=B_gA_g) has no unrelated unit eigenvalue. This is
exactly the logic stated around the mistranscribed lines in the original
review.

## 5. Consequential-drift audit

I read the original 633-line review through EOF and checked every section
against the frozen proof package, plan, publication scope, stage review, both
canonical locks, both current roots, and the correction-opening addendum.

The exact upstream bindings are:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/publication_lock.json` | `6f1830f14413c49cad0945facc7b10c081be1a36d4884e5768205273fce200c4` | 51,578 | 1 |
| `experiments/source_lock.json` | `5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248` | 32,889 | 1 |
| `notes/PROOF_PACKAGE.md` | `0d0ffb5a7d540c987d37a93ec38c7a7736ac8445f6a82c5096e471ebcc34c040` | 24,560 | 1,184 |
| `paper/PAPER_PLAN.md` | `fa7e5a7ea6693b0d8ef10651da317d253f5a1ba199e3b026a3b92c8104b6c974` | 44,881 | 799 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `fa0aef81669da75eacbe604614d86ae4a18610ef2ce70ba58391a47657f29b31` | 44,575 | 1,269 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `8711ba1e5e6daaef5c008f773cd5a5a0751eb1794b8595befc4c8bd5e4df88fb` | 15,589 | 483 |

Both JSON locks remain byte-exact strict-canonical UTF-8 records with one
physical line, one terminal LF, recursively sorted keys, integer-only numeric
tokens, and null self digest/byte fields. The publication lock's seventeen
pre-lock bindings all rehash exactly. Its text ledger remains 1,811 bytes with
SHA-256
`5ddd7b9ab5455fbaa1e299b674c6204bc830366c60fe291350e278e92d817f89`,
and its uint64-be framed stream remains 278,655 bytes with SHA-256
`790628fa98532abaf965b309c202293cb6cac5ccae8001ae95b4c3724512ae91`.

The source lock, proof package, plan, and publication scope state the shifted
kernels exactly. The publication lock's mnemonic fields `A_g_kernel` and
`B_g_kernel` occur inside an object that also binds the action
`Ax=Bx=-x`, zero intersection, full combined covector span, and
`R_g(1)!=0`; they are labels for the same frozen (-1)-eigenspaces, not a
second literal assertion that either invertible matrix has a nonzero ordinary
kernel. No other project artifact contains an uncorrected literal formula
`ker(A_g)=...` or `ker(B_g)=...`.

All other review assertions pass their governing records: positive signs and
phase order, symplecticity, support rows, matrices, seed vectors, four
selectors, six cone walls, both carries, characteristic-zero coefficient
survival, seven-competitor visibility, the (n=0) tie, exact degree, quartic,
recurrence, Perron conclusion, modulo-five certificate, restricted (g=9)
boundary, public identity, 26.00-page/nine-section/no-appendix/zero-figure/
three-table contract, exact nine-source metadata boundary, anti-claims,
provenance, lifecycle, and permissions. I found no second consequential
mathematical, metadata, provenance, inventory, or lifecycle defect.

## 6. Root history and live correction gate

The original review correctly bound its then-live review-opening roots as:

- status: SHA-256
  `0a8ca695d8343676e9de99399bfa66117f2f01de4ab8a2391933607e6708dc81`,
  63,530 bytes and 950 LF;
- idea: SHA-256
  `8cc6aff396853ad3e393d024733d7311ae25ab822b7fedee34804cf4b08a0dfe`,
  98,943 bytes and 1,935 LF.

The later append-only defect-opening transition is now bound by these live
roots:

- `BATCH_06_STATUS.md`: SHA-256
  `239de9938bcded9c3adf4d913a88bc88a61f1c78183d704afdf088a30a230540`,
  64,805 bytes and 967 LF;
- `BATCH_06_IDEA_REPORT.md`: SHA-256
  `9dfd95b4c4f9ca30e08363d229eac1d6855db53faac4a820c7602c6294655273`,
  101,024 bytes and 1,973 LF.

The live gate is exactly
`PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION_OPEN`. The current queue keeps
Paper 24 blocked and authorizes only this root-level correction write.

## 7. Inventory, immutability, and corrected composite effect

Immediately before this correction, the Paper 23 project was exactly:

- 19 regular files;
- 4 child directories;
- 0 symlinks;
- 0 other objects.

The three candidate source paths remain absent:

- `paper/main.tex`;
- `paper/math_commands.tex`;
- `paper/references.bib`.

This correction is outside the Paper 23 project. It changes no project file,
project inventory, lock, review, source path, build state, PDF state, Paper 24
state, or external state. The original review retains its exact identity.

The original terminal token `PUBLICATION_LOCK_PASS` is valid only when the
original review is read together with this immutable correction. The
corrected composite supersedes only the two false literal kernel formulas
identified above.

This corrected composite still does not authorize source authoring. A
separate parent/root lifecycle transition must consume it and explicitly open
one source-only invocation before any member of the exact source trio may be
created. Build, PDF, release, Paper 24, submission, upload, hosting,
repository push, transport, messaging, identity disclosure, and every other
external effect remain closed.

PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS
