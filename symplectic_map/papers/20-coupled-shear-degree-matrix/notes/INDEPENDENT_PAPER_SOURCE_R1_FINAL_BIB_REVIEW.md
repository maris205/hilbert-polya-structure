# Paper20 — Independent Manuscript-Source R1 Review (final BibTeX repair)

**Review ID:** `PAPER_SOURCE_R1_FINAL_BIB_2026_08_22`

**Scope:** final author-stopped source snapshot after correction of the
BibTeX math-mode delimiters.  This is a read-only audit.  I did not compile
TeX/BibTeX, run CAS or numerical experiments, build artifacts, access
transport, upload anything, or modify an author file.  This note is
reviewer-owned and excluded from the ten-file author aggregate.

## Bound identities

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 37,423 | 981 | `2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014` |
| `paper/math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 | 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/BUILD_METADATA_R0.json` | 3,588 | 1 | `75e94cc9da7dd738fd287db32994fb98863d65c00350201ac6c77e48d017cc9c` |

`paper/PAPER_PLAN.md` remains 22,064 bytes/LF397 with SHA
`4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3`.
`experiments/source_lock.json` remains 11,847 bytes/LF1 with SHA
`57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`.
All reviewed files are regular mode 0644, UTF-8, LF-only, and contain no CR,
BOM, or NUL.  The updated metadata and source lock both pass strict canonical
JSON round-trip checks, including duplicate-key rejection, finite-number
checking, recursively sorted Unicode keys, compact separators, and exactly
one terminal LF.  Self-identity fields are null and excluded.  Every updated
`source_files` row matches the on-disk bytes, lengths, and SHA.

Recomputing the locked ten-author-file framing gives 10 files, total 45,416
bytes, 873 LF, and SHA
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.
No forbidden project `.aux`, `.bbl`, `.blg`, `.log`, `.out`, `.pdf`, build,
transport, results, or figures output is present; no symlink is present.
Metadata keeps build, CAS, experiment, data, figures, publication, transport,
and upload permissions false, with planned build `NOT_RUN`.

## Final BibTeX syntax and citation identity

The repaired complex-space titles are now entirely inside math mode and are
protected by the title braces:

```bibtex
title = {Dynamics of polynomial automorphisms of {$\mathbb C^k$}}
title = {Dynamical compactifications of {$\mathbb C^2$}}
```

This is the required correction: the superscripts are inside `$...$`, unlike
the superseded form that closed math mode before `^k`/`^2`.  The bibliography
contains seven unique complete entries with balanced nested braces (67 each),
LF-only syntax, and no NUL/BOM/CR.  `main.tex` loads `amssymb`, so `\mathbb`
is an available command.  The master TeX source hash is unchanged from the
previously reviewed theorem source.

All 14 citation uses in `main.tex` resolve to the seven unique keys
`FriedlandMilnor1989`, `Deserti2018`, `GuedjSibony2002`, `FavreJonsson2011`,
`DangFavre2021`, `Fujioka2023`, and `HenonSurvey2024`.  Their roles remain
bounded contextual background only: planar degree products,
higher-dimensional degree growth, dynamical-degree spectral terminology,
historical valuation context, and a nearby four-dimensional coupled-Hénon
hyperbolicity object.  None is promoted to proof or priority authority.

## Labels and theorem-source replay

The repaired TeX source has 40 unique labels and 43 `ref`/`eqref` uses, with
zero missing or duplicate targets.  The four proof-referenced selector-gap
labels `eq:Sface`, `eq:Tfirstgap`, `eq:Tface`, and `eq:Tsecondgap` are in
numbered `equation` environments.  The obsolete unused `eq:ratiomap` label is
absent.  Environment and brace stacks balance.  This is a source-level parse;
compilation was intentionally not run.

The unchanged theorem source matches the locked algebraic statement over an
algebraically closed characteristic-zero field (K), for every integer
(g\ge5):

\[
V=q_1^2q_2^2+q_1^g,qquad W=p_1^2p_2^2+p_2^g,qquad F_g=T\circ S.
\]

The displayed triangular shears, inverse maps, and symmetric-Hessian pullbacks
establish symplectic polynomial automorphisms.  The actual differentiated
supports give

\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},quad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},quad
C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

The proof explicitly checks the half-open cone
(1\le u_2/u_1<(g-2)/2), the strict (S)-gap
(u_1+2u_2<(g-1)u_1), the (T)-phase ratio
(v_2/v_1=(2+u_2/u_1)/(g-1)\ge3/(g-1)>2/(g-2)), both carried-coordinate
gaps, the endpoint margin (g(g-4)>0), and componentwise growth under
(C_g).  It preserves the exact phase equality
(v_{n+1}=A_gu_n) rather than imposing a false single strict two-shear cone.

Positive integer coefficients in characteristic zero and strict degree gaps
give coefficientwise no-cancellation.  The exact recurrence is
(v_{n+1}=A_gu_n, u_{n+1}=C_gu_n).  Since
(C_g-A_g=\bigl(\begin{smallmatrix}4&2\\2g-4&g-2\end{smallmatrix}\bigr)>0)
and the cone makes (q_2) maximal for (n\ge1), the source obtains
\(\deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T}\).  Trace, determinant, and
discriminant give ((\sqrt g\pm1)^2); Perron positivity plus the visible
coordinate gives
\(\lambda_1(F_g)=\rho(C_g)=(\sqrt g+1)^2<(g-1)^2\).  The scalar recurrence
and (g=5) check agree.

The manuscript retains the bounded P12–P19 collision table and all anti-claims:
no arbitrary supports, words, coefficients, or positive characteristic; no
generic Newton-fan/all-symplectic-map theorem; no topological/arithmetic or
measure-theoretic entropy equality; no periodic/trace/torus/centralizer or
universal-conjugacy result; no numerical/CAS proof certificate; and no
firstness or exhaustive-priority claim.

## Verdict

The final math-mode repair is syntactically correct, all bibliography and
metadata bindings are exact, and theorem, labels, citations, permissions,
anti-claims, and forbidden-output gates pass.  This review authorizes no
compilation, publication, transport, upload, or release.

PAPER_SOURCE_R1_PASS
