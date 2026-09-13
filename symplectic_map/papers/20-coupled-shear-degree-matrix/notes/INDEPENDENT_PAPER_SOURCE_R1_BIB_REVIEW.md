# Paper20 — Independent Manuscript-Source R1 Review (BibTeX repair)

**Review ID:** `PAPER_SOURCE_R1_BIB_2026_08_22`

**Scope:** the author-stopped source snapshot after the authorized mechanical
BibTeX repair. This review is read-only: no TeX/BibTeX compilation, CAS or
numerical run, build, transport access, upload, or author-file edit was
performed. The note is reviewer-owned and excluded from the ten-file author
aggregate.

## Exact identities and bindings

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 37,423 | 981 | `2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014` |
| `paper/math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 | 73 | `5cc0a88c3792b945ab6181ed1e83659c6d5251e172fa4885453b90c8dee15a2c` |
| `paper/BUILD_METADATA_R0.json` | 3,588 | 1 | `fd03d826bc9e65d0b578de5fce0a6b029bd38196d561e4b092aac2cfb77bd675` |

The upstream plan is unchanged at 22,064 bytes/LF397, SHA
`4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3`; the
source lock is unchanged at 11,847 bytes/LF1, SHA
`57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`.
All source files are regular mode 0644, UTF-8, LF-only, with no CR, BOM, or
NUL. The updated metadata and unchanged source lock both pass strict JSON
round-trip checks (duplicate keys rejected, finite numbers only, recursive
Unicode-key ordering, compact separators, one terminal LF), and their
self-identity fields remain null/excluded.

Every `source_files` row in `BUILD_METADATA_R0.json` matches the on-disk
length and SHA. Recomputing the frozen ten-author-file framing gives 10
files, 45,416 bytes, 873 LF, and aggregate SHA
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.
The manuscript, bibliography repair, metadata, and this reviewer note are
downstream/out-of-band and do not enter that aggregate. No forbidden project
outputs (`aux`, `bbl`, `blg`, `log`, `out`, `pdf`, build, transport, results,
or figures) or symlinks are present. Metadata still records build, CAS,
experiment, data, figure, publication, transport, and upload permissions as
false; planned build status is `NOT_RUN`.

## BibTeX-only repair

The only changed manuscript-side source identity is `references.bib`; the
master TeX source and notation file retain their previously reviewed hashes.
The two titles containing complex affine-space notation now use protected,
valid BibTeX math fragments:

```bibtex
title = {Dynamics of polynomial automorphisms of {$\mathbb C$}^k}
title = {Dynamical compactifications of {$\mathbb C$}^2}
```

The bibliography has seven unique entries, balanced nested braces (67 opening
and 67 closing braces), LF-only syntax, and no NUL/BOM/CR. A structural entry
parse finds seven complete entries with unique keys and complete field spans.
The `$...$` fragments are properly nested inside protected title braces, and
`main.tex` loads `amssymb`, which supplies `\mathbb`. No theorem, prose,
equation, citation key, or permission field changed in `main.tex`.

## Citation and cross-reference closure

The 14 citation uses in `main.tex` resolve exactly to the seven bibliography
keys: `FriedlandMilnor1989`, `Deserti2018`, `GuedjSibony2002`,
`FavreJonsson2011`, `DangFavre2021`, `Fujioka2023`, and `HenonSurvey2024`.
Their roles remain bounded to planar degree-product background,
higher-dimensional degree-growth context, dynamical-degree spectral
terminology, historical valuation context, and a neighboring four-dimensional
coupled-Hénon hyperbolicity object. No citation is used as proof of the
recurrence, symplecticity, selectors, no-cancellation, Perron root, or
priority.

The repaired TeX source has 40 unique labels and 43 `ref`/`eqref` uses, with
zero missing or duplicate targets. `eq:Sface`, `eq:Tfirstgap`, `eq:Tface`,
and `eq:Tsecondgap` are all inside numbered `equation` environments; the
obsolete unused `eq:ratiomap` label is absent. Environment and brace stacks
balance. This is a source parse only; compilation was intentionally not run.

## Theorem and proof fidelity

The unchanged manuscript still matches the locked theorem over an algebraically
closed characteristic-zero field (K), integer (g\ge5):

\[
V=q_1^2q_2^2+q_1^g,\qquad W=p_1^2p_2^2+p_2^g,\qquad F_g=T\circ S,
\]

with the canonical triangular shears and explicit inverses. The displayed
phase rows and complete-step matrix are

\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\quad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},\quad
C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

The proof retains every locked gate:

1. symmetric-Hessian pullbacks and triangular inverses establish symplectic
   polynomial automorphisms;
2. the (S)-selector uses (1\le u_2/u_1<(g-2)/2) and the strict gap
   (u_1+2u_2<(g-1)u_1);
3. after (v=A_gu), the (T)-selector uses
   (v_2/v_1=(2+u_2/u_1)/(g-1)\ge3/(g-1)>2/(g-2)), with both carried-(q)
   gaps explicit;
4. the complete-step ratio map is increasing, preserves the half-open cone,
   and has upper-boundary margin (g(g-4)>0), while the phase-return equality
   (v_{n+1}=A_gu_n) remains explicit;
5. all carried terms are checked at the base step and inductively, and positive
   integer coefficients in characteristic zero prevent cancellation;
6. (v_{n+1}=A_gu_n, u_{n+1}=C_gu_n), with
   (C_g-A_g=\bigl(\begin{smallmatrix}4&2\\2g-4&g-2\end{smallmatrix}\bigr)>0),
   makes (q_2) the visible maximal coordinate and gives
   \(\deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T}\);
7. trace (2g+2), determinant ((g-1)^2), discriminant (16g), and
   Perron positivity give
   \(\lambda_1(F_g)=\rho(C_g)=(\sqrt g+1)^2\), strictly below
   \((g-1)^2\).

The scalar recurrence, (g=5) check, half-step warning, and narrow support
coupling comparison remain algebraically consistent. No generic Newton-fan,
arbitrary-word, entropy, periodic, torus, universal-conjugacy, priority, or
numerical/CAS claim appears.

## Verdict

The BibTeX repair is syntactically and semantically bounded, all updated source
bindings are exact, and the repaired source passes the theorem, citation,
cross-reference, anti-claim, inventory, and permission gates. This review
authorizes no compilation, publication, transport, upload, or release.

PAPER_SOURCE_R1_PASS
