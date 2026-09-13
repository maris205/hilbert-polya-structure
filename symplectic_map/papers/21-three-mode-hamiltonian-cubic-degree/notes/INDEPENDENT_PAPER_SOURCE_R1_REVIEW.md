# Independent paper source R1 review — Paper 21

Verdict: PASS.

Scope checked: the manuscript source trio against the frozen publication-stage
scope, the canonical publication lock, the passed paper plan, and the locked
proof package / claims-evidence / citation-verification records.

| Artifact | Bytes | LF | SHA-256 | Role |
|---|---:|---:|---:|---|
| `paper/main.tex` | 51647 | 1251 | `74434cdc99fcabd173d9d59e578ec82811ac99b7846761b11601bd58b26d0a99` | reviewed main manuscript |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` | reviewed shared notation |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` | reviewed bibliography |

Checks passed:

- Public identity is consistent with the frozen manuscript contract:
  `Anonymous Authors`, empty source date, and PDF metadata title string
  `Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies`,
  while the typeset title renders `\A^6`.
- The source trio contains no local paths, digests, JSON/Markdown file names,
  reviewer/workflow prose, acknowledgments, affiliations, funding, email,
  ORCID, or internal-project provenance markers.
- The bibliography contains exactly the two authorized keys
  `BlancVanSanten2019` and `ShaoSun2025`; both are present in
  `references.bib`, both are cited from the bounded related-work section only,
  and neither is promoted into theorem proof, priority, or firstness language.
- The manuscript preserves the locked proof order L1 \(\rightarrow\) L9:
  canonicality and inverses; six-row support ledger; exactly two selector gaps
  with corrected `M_T`; cone invariance; phase/carry induction and
  characteristic-zero no-cancellation; `q_3` visibility and exact degree row;
  Perron/row-sum bound; characteristic polynomial plus mod-5 audit; and the
  `g=7` boundary note.
- The first theorem and later setup sections contain the exact displayed
  gradients, subtraction inverses, Hessian blocks, six support rows, and the
  literal matrix multiplication
  \(\displaystyle C_g=B_gA_g=\begin{psmallmatrix}g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1\end{psmallmatrix}\).
- The selector analysis is correctly restricted to two competitive rows only:
  \[
  M_S=(g-2)-2x-2y,\qquad
  M_T=(2g-6)x+(g-6)y-6,
  \]
  and the text explicitly rules out any invented third selector face.
- The cone argument includes the exact normalized updates
  `D`, `X'-1`, `Y'-1`, the height functional `H_2`, and the symbolic split
  `8 <= g <= 11` versus `g >= 12`, with the strict inequalities written in the
  main body rather than delegated elsewhere.
- The phase/carry section proves strict old-term dominance with `C_g-I>0`,
  derives `v_{n+1}=A_g u_n` and `u_{n+1}=C_g u_n`, and states the positive
  semiring / characteristic-zero no-cancellation mechanism explicitly.
- The visibility section contains the exact matrix difference `C_g-A_g`,
  the strict positivity formulas for `U_3-U_2` and `U_3-U_1`, and the exact
  degree identity
  \[
  \deg(F_g^n)=e_3^{\mathsf T}C_g^n\mathbf 1.
  \]
- The Perron and arithmetic sections preserve the locked row sums
  `g+19`, `2g+13`, `5(g-1)`, the characteristic polynomial
  \[
  t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2,
  \]
  and the explicit mod-5 no-root table for residue classes `2,3,4`.
- Static LaTeX consistency checks passed without compilation:
  balanced `\begin{...}` / `\end{...}` counts for all environments, balanced
  braces after comment/escape stripping, no undefined `\ref{}` / `\eqref{}`
  targets, no missing BibTeX entries, no uncited bibliography entries, and no
  `TODO` / `FIXME` / `XXX` / `VERIFY` markers.
- The 24–29 substantive-page contract is credible from source content alone:
  `main.tex` has 1251 lines and roughly 5203 detex-visible words, contains six
  dense main-body sections plus six tables and no appendix, so a body length in
  the locked band remains plausible.

Overall: the current manuscript source is anonymous, scope-clean, proof-first,
and statically consistent with the frozen Paper 21 theorem and publication
governance records.

PAPER_SOURCE_R1_PASS
