# Independent paper source R1 replacement review — Paper 21

Verdict: PASS.

## Review scope and provenance

I acted as a fresh independent manuscript-source reviewer after the earlier R1
receipt became stale.  I reviewed the final source bytes against the frozen
publication lock and scope, the passed paper plan, the proof package, the
citation lock, and the anti-claim / permission boundary.  I did not author or
edit any manuscript source, compile LaTeX, run BibTeX, run CAS or numerical
code, access a dataset, use scientific network evidence, or create a build,
transport, upload, or publication artifact.

The stale receipt at `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` binds an
earlier `main.tex` and is not evidence for the source reviewed here.  This note
is the replacement R1 review and is my sole project write.

Frozen upstream identities checked:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/publication_lock.json` | 6,704 | 1 | `14966ffc04e0ce68eed83688bfaf871aa02422ba2564532d0f6fff5a7071e114` |
| `notes/PUBLICATION_STAGE_SCOPE.md` | 4,653 | 104 | `94c185559e9ecb0c0680aa4c58b2fb725e80128bea465b6d4b6e26cbe0decccd` |
| `paper/PAPER_PLAN.md` | 15,765 | 245 | `63a7de8600af40648bb4ab94903bd4331bf4dc4265aabe8b88392a595b60a620` |
| `notes/PROOF_PACKAGE.md` | 16,199 | 427 | `599c9da5e5d4ca0e0b78c7b8683cdd2d63da50e555d9d6984bf1cf09f55e21d6` |

Final manuscript source identities reviewed:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 67,605 | 1,554 | `c3d34411f3012a446238c098a10e1f76258236a5d0b6da91f7b01475633c1e86` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |

## Independent theorem audit

- I recomputed the gradients of
  (V=q_1^2q_2^2q_3^2+q_1^g) and
  (W=p_1^2p_2^2p_3^2+p_3^g).  All six displayed gradient coordinates and
  every entry of the two displayed Hessians are correct.  The Hessians are
  symmetric, the subtraction inverses are polynomial, and the block matrices
  (J_S=(I,0;H_V,I)), (J_T=(I,H_W;0,I)) satisfy the stated symplectic
  identities with (H_W) evaluated at the intermediate (P)-coordinate.
- The complete six-row support ledger is exhaustive.  It has exactly two
  competitive rows and no invented third face.  Reading the selected rows gives
  
  \[
  A_g=\begin{pmatrix}g-1&0&0\\2&1&2\\2&2&1\end{pmatrix},\qquad
  B_g=\begin{pmatrix}1&2&2\\2&1&2\\0&0&g-1\end{pmatrix}.
  \]
  Direct multiplication gives
  (C_g=B_gA_g=((g+7,6,6),(2g+4,5,4),
  (2(g-1),2(g-1),g-1))), exactly as stated.
- The first score difference is
  (u_1[(g-2)-2x-2y]=u_1M_S).  For the second face the manuscript now
  correctly changes phase to (v=A_gu); recomputation gives
  ((g-1)v_3-(2v_1+2v_2+v_3)
   =u_1[(2g-6)x+(g-6)y-6]=u_1M_T).
  On the locked cone, (M_S>1) and (M_T\ge 3g-18\ge6).
- For (U'=C_gU), I independently obtained
  (D=g+7+6x+6y),
  (X'-1=(g-3-x-2y)/D), and
  (Y'-1=[g-9+(2g-8)x+(g-7)y]/D).  Expanding the height form gives
  
  \[
  H_2=U_1Q,\qquad
  Q=g^2-4g-25+2(g-12)x+4(g-6)y.
  \]
  For (8\le g\le11), the cone boundary substitution yields
  (Q>2g^2-17g+11\ge3); for (g\ge12), (x,y\ge1) yields
  (Q\ge g^2+2g-73>0).  Thus all three cone inequalities are preserved.
- Both carried-coordinate phases are now explicit.  The base (S)-vector is
  (A_g\mathbf1=(g-1,5,5)^T>\mathbf1).  At later (S)-phases,
  (A_g(u_n-u_{n-1})>0).  Separately, the new lemma proves at every
  (T)-phase, including (n=0),
  
  \[
  B_gv_{n+1}-u_n=(C_g-I)u_n>0.
  \]
  Hence the two internal face gaps and both carry comparisons close the exact
  phase induction without a half-step/full-step mismatch.
- The positive-support argument is valid in the stated characteristic-zero
  setting: composition uses Minkowski addition of finite supports, all
  coefficient paths are positive integers, and a selected coefficient cannot
  cancel or vanish.  No positive-characteristic extension is asserted.
- I recomputed
  
  \[
  C_g-A_g=\begin{pmatrix}8&6&6\\2g+2&4&2\\2g-4&2g-4&g-2\end{pmatrix}>0.
  \]
  The output-row differences are
  (U'_3-U'_2=[-6+(2g-7)x+(g-5)y]U_1>0) and
  (U'_3-U'_1=[g-9+(2g-8)x+(g-7)y]U_1>0).  Thus (q_3) dominates all
  six coordinate degrees and the exact identity
  (deg(F_g^n)=e_3^TC_g^n\mathbf1) follows for every (n\ge0).
- (C_g) is positive.  Its row sums are (g+19), (2g+13), and
  (5(g-1)); their differences from ((g-1)^2) are respectively
  ((g-6)(g+3)), ((g-6)(g+2)), and ((g-1)(g-6)), all positive for
  (g\ge8).  Perron--Frobenius and the positive initial/observable vectors
  therefore give (lambda_1(F_g)=\rho(C_g)<(g-1)^2).
- The trace is (2g+11).  The principal minors recompute to
  (11-7g), ((g-1)(g-5)), and (-3(g-1)), whose sum is
  (g^2-16g+19).  Since
  (det A_g=det B_g=-3(g-1)), (det C_g=9(g-1)^2).  These data give
  exactly
  
  \[
  t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2.
  \]
- I re-evaluated the three reduced cubics at all five elements of
  (mathbb F_5).  The table rows are exactly
  ((1,3,1,1,4)), ((4,3,4,3,1)), and ((4,2,3,3,3)); none contains
  zero.  The degree-three irreducibility and cubic Perron corollary for
  (g\equiv2,3,4\pmod5) follow with the stated bounded meaning.
- At (g=7), the seed has (x+y=2=(g-3)/2) while
  (M_S=5-2-2=1).  The manuscript correctly records a strict-cone boundary,
  not a selector tie or a theorem extension.

## Identity, citation, scope, and static-source audit

- The public identity is exactly `Anonymous Authors`, the source date is
  empty, and the PDF metadata title is the locked A6 title.  No real author,
  affiliation, email, ORCID, acknowledgment, funding, local path, digest,
  reviewer/agent/model identity, lifecycle token, or private provenance occurs
  in the manuscript source trio.
- The bibliography contains exactly the two authorized keys
  `BlancVanSanten2019` and `ShaoSun2025`, and both are cited only in the bounded
  related-work section.  The repaired Shao--Sun sentence now describes only
  dimension-four affine-triangular algebraic-degree context and explicitly
  transfers no symplectic, selector, recurrence, or proof input.
- All forbidden genericity, entropy, periodic, trace, multiplier, torus,
  arithmetic-dynamics, conjugacy/classification, priority/firstness,
  positive-characteristic, numerical, and CAS-proof enlargements remain
  excluded.  The proof order remains L1 through L9 and all theorem-critical
  content stays in the main body.
- Static inspection without compilation found balanced environments and
  braces, 48 unique labels, 60 `ref`/`eqref` uses with no missing target, two
  citation keys with exact BibTeX closure, and no TODO/FIXME/XXX/VERIFY marker.
  All three source files are UTF-8, BOM-free, CR-free, NUL-free, LF-terminated,
  and no `.aux`, `.bbl`, `.blg`, `.log`, `.out`, or PDF artifact exists.
- The locked 24--29 substantive-page band is credible from source alone:
  `main.tex` contains 1,554 lines, approximately 7,090 detex-visible words,
  eight main sections, nine proof-ledger tables, dense displayed derivations,
  no appendix, and only the two excluded references.  No compilation was used
  to make this source-stage judgment.

The repaired final manuscript source is anonymous, scope-clean, internally
self-contained, and mathematically consistent with the frozen Paper 21
theorem and proof contract.

PAPER_SOURCE_R1_REPLACEMENT_PASS
