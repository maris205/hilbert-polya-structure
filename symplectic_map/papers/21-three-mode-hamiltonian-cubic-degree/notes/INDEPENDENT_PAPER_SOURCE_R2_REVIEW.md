# Independent Paper Source R2 Review — Paper 21

Verdict: PASS.

## Independence and scope

I am a fresh R2 source reviewer.  I read the frozen publication scope and
lock, paper plan, proof package, current source trio, the stale original R1
review for provenance only, and the replacement R1 review.  I did not author
or alter a manuscript source, alter an existing project file, compile LaTeX,
run BibTeX, run CAS or numerical code, use a dataset, access the network, or
create a build, transport, upload, or publication artifact.  This note is my
sole project write.

The current source identities rehashed exactly as follows:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 67,605 | 1,554 | `c3d34411f3012a446238c098a10e1f76258236a5d0b6da91f7b01475633c1e86` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |

The stale `INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` therefore remains
provenance only.  The current source identity is the one already reviewed by
the replacement R1 receipt, and independently rechecked here.

## Mathematical audit

- Recomputing both gradients gives
  \(\nabla V=(2q_1q_2^2q_3^2+gq_1^{g-1},2q_1^2q_2q_3^2,2q_1^2q_2^2q_3)\)
  and
  \(\nabla W=(2p_1p_2^2p_3^2,2p_1^2p_2p_3^2,2p_1^2p_2^2p_3+gp_3^{g-1})\).
  The displayed Hessians are symmetric; subtraction inverses are polynomial;
  and the triangular block matrices
  \(J_S=(I,0;H_V,I)\), \(J_T=(I,H_W;0,I)\), with \(H_W\) evaluated at the
  intermediate p-coordinate, satisfy the stated symplectic identities.
- The six-row support ledger is exhaustive.  It gives exactly
  \(A_g=((g-1,0,0),(2,1,2),(2,2,1))\),
  \(B_g=((1,2,2),(2,1,2),(0,0,g-1))\), and
  \(C_g=B_gA_g=((g+7,6,6),(2g+4,5,4),(2(g-1),2(g-1),g-1))\).
  Only the first S row and third T row are competitive, so no third selector
  face is introduced.
- With \(v=A_gu\), direct subtraction gives the two and only two selector
  margins \(M_S=g-2-2x-2y\) and
  \(M_T=(2g-6)x+(g-6)y-6\).  On the locked cone
  \(x,y\geq1\), \(x+y<(g-3)/2\), \(M_S>1\) and
  \(M_T\geq3g-18\geq6\).  This uses the phase-correct \(v=A_gu\), not a
  half-step/full-step substitution error.
- For \(U'=C_gU\), the rederived tests are
  \(X'-1=(g-3-x-2y)/D\),
  \(Y'-1=[g-9+(2g-8)x+(g-7)y]/D\), and
  \(H_2=U_1Q\), with
  \(Q=g^2-4g-25+2(g-12)x+4(g-6)y\).  The source's split is correct:
  for \(8\leq g\leq11\), the cone-boundary substitution gives
  \(Q>2g^2-17g+11\geq3\); for \(g\geq12\), \(x,y\geq1\) gives
  \(Q\geq g^2+2g-73>0\).  Thus all X/Y/height inequalities preserve the
  cone.
- Both carry mechanisms are present, including the base step.  In the
  S-phase \(A_g\mathbf1=(g-1,5,5)^T>\mathbf1\), and later
  \(A_g(u_n-u_{n-1})>0\) supplies all three carried-p margins.  In the
  T-phase, including \(n=0\),
  \(B_gv_{n+1}-u_n=(C_g-I)u_n>0\) supplies all carried-q margins.
  The characteristic-zero positive-semiring argument then correctly prevents
  cancellation of the uniquely selected support coefficient.
- The visibility calculation is correct:
  \(C_g-A_g=((8,6,6),(2g+2,4,2),(2g-4,2g-4,g-2))>0\), while the two
  displayed q-row differences make \(q_3\) strictly largest.  Hence
  \(\deg(F_g^n)=e_3^TC_g^n\mathbf1\) for \(n\geq0\), with no spectral-only
  shortcut.
- The Perron and arithmetic checks recompute: C is positive; the row sums are
  \(g+19,2g+13,5(g-1)\), each strictly below \((g-1)^2\) for \(g\geq8\).
  The trace, principal-minor sum, and determinant give
  \(t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2\).  The three mod-5 value rows
  \((1,3,1,1,4)\), \((4,3,4,3,1)\), and \((4,2,3,3,3)\) have no zero,
  proving the stated irreducible cubic subfamilies for residues 2, 3, and 4.
  At \(g=7\), the seed is on the strict-cone boundary and \(M_S=1\), which
  is correctly described as no selector tie and not as a theorem extension.

## Public, citation, and static-source audit

- The title, anonymous author `Anonymous Authors`, empty date, and locked PDF
  metadata are present.  No real identity, affiliation, email, ORCID,
  acknowledgement, funding, local path, digest, reviewer/agent/model name,
  lifecycle token, or private provenance was found in the source trio.
- `references.bib` has exactly the authorized keys `BlancVanSanten2019` and
  `ShaoSun2025`; both are cited only in the bounded related-work discussion
  and are expressly context-only.  No citation is promoted to a proof input.
- No prohibited genericity, arbitrary-dimension/characteristic enlargement,
  entropy, periodic, trace, multiplier, torus, arithmetic-dynamics,
  universal-conjugacy/classification, priority/firstness, numerical, or CAS
  certificate claim was found.
- Static checks found 48 unique labels, 60 ref/eqref uses with no missing
  target, matching 102 begin/end environments, and exact two-key citation
  closure.  Each source file is UTF-8, BOM-free, CR-free, NUL-free, and
  LF-terminated.  There is no build output in `paper/`.
- Without compiling, the locked 24–29 substantive-page band is credible from
  the 1,554-line, approximately 7,090-visible-word source: eight main
  sections, nine proof-ledger tables, dense main-body derivations, no appendix,
  and only the excluded references.  This is a static feasibility judgment,
  not a build claim.

The current source trio is mathematically consistent, anonymous, scope-clean,
and ready for the separately authorized next stage only.

PAPER_SOURCE_R2_PASS
