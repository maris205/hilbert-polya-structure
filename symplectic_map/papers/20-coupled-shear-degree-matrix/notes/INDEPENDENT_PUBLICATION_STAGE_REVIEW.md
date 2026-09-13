# Paper20 independent publication-stage review

Date: 2026-08-22 UTC  
Review role: fresh, independent publication-stage gate  
Review ID: `PUBLICATION_STAGE_REVIEW_FRESH_2026_08_22`

This is a read-only audit of the frozen Paper20 scope, publication lock, source
chain, manuscript, receipt, PDF, citations, theorem contract, identity boundary,
and permission boundary.  I did not compile, run LaTeX/BibTeX, run experiments,
run CAS/symbolic/numerical code, access data, use the network, or perform any
external action.  The sole project write from this review is this note.

## Frozen identity and canonical lock checks

The scope file has the required identity: 14,472 bytes, 299 LF, SHA-256
`875c615b00aa98ffc3a290548582762fc321907d19ed338741de58456b2133e2`.
The publication lock has the required identity: 12,382 bytes, one LF, SHA-256
`4559e4947613b70eda65523f83d5c1f369199c77852af3cc1940afa7ecbf0eff`.
The source lock has SHA-256
`57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`.

The lock was parsed with duplicate-key rejection and a finite-number check.  It
is UTF-8, has no BOM, CR, or NUL, has exactly one terminal LF, and its exact
byte string equals a recursive Unicode-code-point key-sorted JSON serialization
using `,:` separators.  The self-excluded lock identity is represented by the
required null fields; no duplicate keys or nonfinite values were found.

The lock's 57 non-self inventory entries were rehashed independently: every
listed path exists, and each byte count, LF count, and SHA-256 matches.  The
project has exactly the four expected directories (`experiments`, `notes`,
`paper`, `refine-logs`), no symlinks, and 58 regular files before this reviewer
note.  The only unlisted pre-review file is the publication lock itself, as
required by self exclusion.  There are no unexpected files, and no forbidden
`code`, `data`, `figures`, `manuscript`, `results`, `transport`, `build`, or
paper transport/results/figures/build directories.  The newly authorized review
note is the only additional project path and is not treated as a frozen author
input.

The exact frozen source and plan identities are present:

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 61,835 / 1,619 | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |

## Build and PDF gate

The R1 receipt is 11,325 bytes, one LF, SHA-256
`0c0ce98b3ee4349d269aaebacf78d89ad237aec4f36595a02d268c2fdf78cc31`.
Its source bindings for `main.tex`, `math_commands.tex`, `references.bib`,
`PAPER_PLAN.md`, `source_lock.json`, `BUILD_METADATA_R1.json`, and
`SOURCE_REVISION_RECEIPT_R1.json` all match the live files.  Its persisted R1
candidate is `paper/main_round1.pdf`, 429,723 bytes, SHA-256
`07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40`; the
current file independently matches these receipt values.  No source or receipt
binding changed after the recorded build.

Both required source page-fix reviews are present and terminate with
`PAPER_SOURCE_R1_PAGEFIX_PASS` and `PAPER_SOURCE_R2_PAGEFIX_PASS`.  The page-fix
authorization terminates with `SOURCE_PAGEFIX_AUTHOR_STOP`.  Both required
fresh build reviews are present and terminate with `BUILD_R1_PAGEFIX_PASS` and
`BUILD_R2_PAGEFIX_PASS`.  The build authorizations terminate with
`BUILD_AUTHORIZATION_R1_PAGEFIX` and `BUILD_AUTHORIZATION_R1_PAGEFIX_RETRY`.
The receipt records the two isolated roots, byte-identical roots, the complete
four-command historical build, and no source edits during that build.

Independent PDF readback reports the locked artifact metadata: title
`Coupled Hamiltonian Shear Degree Matrices in A4`, author `Anonymous Authors`,
23 pages, Letter size, unencrypted, no JavaScript.  The PDF has 25 font rows and
every row is embedded, subset, and Unicode mapped.  Text extraction places the
conclusion on page 22 and References beginning on page 22; the total is 23
pages and there is no appendix.  Final-build diagnostics recorded in the
receipt and corroborated by the retained log are zero fatal errors, undefined
citations, undefined references, overfull boxes, and draft-marker hits.  The
three underfull-box, one label-change, and four hyperref PDF-string warnings
are the explicitly recorded nonfatal diagnostics.  BibTeX reports zero
warnings.

The extracted PDF and final log contain no `TODO`, `FIXME`, `TBD`, `VERIFY`,
`??`, or `[?]` marker.  The sole `hyper@anchor@undefined` text is TeX control
code in auxiliary internals, not an unresolved reference; no undefined-ref or
undefined-citation diagnostic is present.

## Theorem and proof contract

The manuscript matches the frozen theorem exactly: (K) is algebraically
closed of characteristic zero, (g) is an integer with (g\ge5),

\[
V=q_1^2q_2^2+q_1^g,\quad W=p_1^2p_2^2+p_2^g,
\qquad S(q,p)=(q,p+\nabla V),\quad T(q,p)=(q+\nabla W,p),\quad F_g=T\circ S.
\]

It gives triangular inverses, symmetric-Hessian symplecticity, and a block
Jacobian check (L1).  It selects

\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\quad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},\quad
C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

The first and second phase selectors, including all carried-coordinate and
mixed-versus-pure strict gaps, are proved separately (L2--L3).  The half-open
cone is exactly
\(\mathcal C_g=\{u>0:1\le u_2/u_1<(g-2)/2\}\); its ratio map is shown
invariant with strict componentwise growth for every (g\ge5) (L4).  The
simultaneous carried-term induction and the positive-coefficient,
characteristic-zero coefficient-path argument establish no cancellation (L5).
The complete recurrence is
\(v_{n+1}=A_gu_n\), \(u_{n+1}=C_gu_n\), with (u_0=(1,1)^\mathsf T), and
the second q-coordinate is proved to be the maximal total-degree functional
(L6).  The characteristic polynomial gives roots
\((\sqrt g\pm1)^2\); explicit positive left/right pairings establish Perron
accessibility and visibility, yielding
\(\deg(F_g^n)=e_2^\mathsf TC_g^n(1,1)^\mathsf T\) and
\(\lambda_1(F_g)=\rho(C_g)=(\sqrt g+1)^2\) (L7).
The manuscript also proves \(\deg(S)=\deg(T)=g-1\) and the strict comparison
\((\sqrt g+1)^2<(g-1)^2\).  The mixed support/coupling statement is explicitly
coordinate-split and does not assert universal non-conjugacy.

## Citation, anti-claim, and identity checks

The references chain is exact: `references.bib`, all seven citation uses, and
the generated bibliography contain precisely
`FriedlandMilnor1989`, `Deserti2018`, `GuedjSibony2002`, `FavreJonsson2011`,
`DangFavre2021`, `Fujioka2023`, and `HenonSurvey2024`.  Their manuscript roles
are bounded context/collision-boundary evidence only; no citation is used as a
proof of the recurrence, symplecticity, selectors, no-cancellation, or Perron
root, and no priority or firstness claim is made.

The manuscript and PDF preserve the locked anti-claims: no arbitrary-support,
generic Newton-fan, all-automorphism classification, entropy-equality,
periodic-point/trace/multiplier/invariant-curve/centralizer/torus-translate,
arithmetic-specialization, effective-orbit, numerical/CAS, universal-product,
non-conjugacy, absolute-novelty, firstness, or priority claim appears.

Public identity is clean.  The source and PDF show only `Anonymous Authors`, an
empty source date, and the frozen title/metadata.  No real identity,
affiliation, email, ORCID, funding, acknowledgment, reviewer identity, local
path, digest, dashboard, agent/model name, lifecycle token, venue, or private
provenance appears in manuscript text or PDF metadata.  `/Root` found by a raw
PDF string scan is a PDF structural name, not public identity or a local path.

The zero-execution ledger is consistent: scientific experiments, CAS/symbolic
runs, numerical runs, datasets, generated assets, code/data artifacts, result
files, external inputs/uploads, and network reads are all zero.  The lock and
receipts authorize no permissions expansion, compilation, source edit,
experiment, CAS, network, transport, release, submission, or upload.

## Verdict

All frozen hashes, canonical JSON, inventory, build receipt, source/build
reviews, page contract, PDF metadata/text, theorem obligations, citation roles,
anti-claims, identity boundary, zero-execution ledger, and permission checks
passed.  No publication-stage blocker was found.  This note authorizes no later
source edit, rebuild, release, submission, transport, or upload.

PUBLICATION_STAGE_PASS
