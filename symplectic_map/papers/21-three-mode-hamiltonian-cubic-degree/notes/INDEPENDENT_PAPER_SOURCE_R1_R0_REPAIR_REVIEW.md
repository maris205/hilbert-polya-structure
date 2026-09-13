# Independent Repair-Source R1 Review — Paper 21

Verdict: PASS.

## Scope, independence, and frozen identity

I acted as a fresh repair-source R1 reviewer.  I read the paper plan, the
publication and source locks, `BUILD_R0_BLOCKER.md`,
`R0_PROOF_FIRST_SOURCE_REPAIR.md`, and the final frozen source trio.  I treated
all previous manuscript reviews as stale provenance only, including every
PAGEFIX receipt binding `910086eb...`; none supplies authority for this repaired
source.  I did not compile, invoke BibTeX, run CAS or numerical code, access a
dataset or network, or edit a manuscript, dashboard, build artifact, or
existing note.  This review is my sole project write.

The rehashed source identity is exactly:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 84,917 | 1,990 | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |

The repaired `main.tex` is consequently a new frozen source identity, not an
extension of the blocked-R0 or intermediate PAGEFIX review authority.

## Independent mathematical recomputation

- The gradients are correct:
  \(\nabla V=(2q_1q_2^2q_3^2+gq_1^{g-1},2q_1^2q_2q_3^2,2q_1^2q_2^2q_3)\)
  and
  \(\nabla W=(2p_1p_2^2p_3^2,2p_1^2p_2p_3^2,2p_1^2p_2^2p_3+gp_3^{g-1})\).
  Both Hessians are symmetric; subtraction gives polynomial inverses; and the
  displayed lower/upper triangular Jacobian blocks satisfy
  \(J^T\Omega J=\Omega\), with the W Hessian evaluated at the intermediate
  p-coordinate.
- The six support rows give exactly
  \(A=((g-1,0,0),(2,1,2),(2,2,1))\),
  \(B=((1,2,2),(2,1,2),(0,0,g-1))\), and
  \(C=BA=((g+7,6,6),(2g+4,5,4),(2(g-1),2(g-1),g-1))\).
  Only the first S row and third T row have competing faces.
- With the required phase change \(v=Au\), direct score subtraction gives
  \(M_S=g-2-2x-2y\) and
  \(M_T=(2g-6)x+(g-6)y-6\).  On \(x,y\geq1\),
  \(x+y<(g-3)/2\), these are strict.  The new slack ledger is algebraically
  correct: \(h=g-3-2x-2y>0\), \(M_S=1+h\), and
  \(X'-1=(x+h)/D\); the second selector and Y margin have the stated positive
  lower bounds.  No third face is used.
- Re-expanding the full cone calculation gives
  \(H_2=U_1Q\), with
  \(Q=g^2-4g-25+2(g-12)x+4(g-6)y\).  The small-range boundary substitution
  yields \(Q>2g^2-17g+11=3+(g-8)(2g-1)\geq3\), while the large-range estimate
  is \(Q\geq g^2+2g-73=95+(g-12)(g+14)>0\).  The X/Y/height cone proof is
  therefore valid for every integer \(g\geq8\).
- The phase and carry proof is correctly indexed.  The base S vector is
  \(v_1=A\mathbf1=(g-1,5,5)^T>\mathbf1\); later S carries are controlled
  row by row by \(A(u_n-u_{n-1})>0\); and every T carry, including \(n=0\),
  is controlled by \(Bv_{n+1}-u_n=(C-I)u_n>0\).  The explicit six-coordinate
  state properly distinguishes old P, intermediate P, and old Q vectors.
- The new exact audit tables recompute correctly:
  \(u_1=(g+19,2g+13,5(g-1))^T\),
  \(v_2=((g-1)(g+19),14g+41,11g+59)^T\), and
  \(u_2=(g^2+68g+181,2g^2+72g+121,11g^2+48g-59)^T\).
  The two second-step visibility differences factor as
  \(3(g-6)(3g+10)\) and \(10(g-6)(g+4)\), respectively.
- The characteristic-zero coefficient argument is adequate: the six displayed
  selected coefficient witnesses are positive integer products, additional
  support paths only add nonnegative integers, and both 2 and \(g\) remain
  nonzero in characteristic zero.  It claims positivity, not spurious
  uniqueness of all coefficient paths.
- The six-coordinate visibility proof is correct.  \(C-A\) is entrywise
  positive; the two q-row differences have lower bounds \(3g-18\) and
  \(4g-24\); thus q3 is uniquely maximal among all six coordinate degrees and
  \(\deg(F_g^n)=e_3^TC^n\mathbf1\) holds for \(n\geq0\).
- The positive-eigenvector squeeze correctly proves the visible-row rate is
  \(\rho(C)\).  The row sums \(g+19,2g+13,5(g-1)\) are strictly below
  \((g-1)^2\) by the displayed positive factorizations.  The trace, minors,
  determinant, cubic characteristic polynomial, and all three mod-5 value rows
  recompute as written; the irreducible cubic subfamilies for residues 2, 3,
  and 4 follow.  At \(g=7\), the seed is a strict-cone boundary and
  \(M_S=1\), not a selector tie.

## Scope and static-source audit

- The source preserves the locked anonymous title, `Anonymous Authors`, empty
  date, and metadata.  No private identity, path, digest, reviewer/workflow,
  lock, hash, acknowledgement, or provenance text appears in the public
  source.
- Exactly two citations and two bibliography keys occur:
  `BlancVanSanten2019` and `ShaoSun2025`.  Their usage is bounded contextual
  terminology only; neither is promoted to symplecticity, selector,
  recurrence, cancellation, or priority proof.
- The retained anti-claims exclude genericity, arbitrary dimensions or
  characteristics, entropy, periodic/trace/multiplier/torus claims, universal
  conjugacy/classification, numerical or CAS certificates, and priority.
- Static closure passes: 720 opening and 720 closing braces; 119 begin and 119
  end environments; 56 unique labels; 65 ref/eqref uses with no missing label;
  and exact two-key citation closure.  All three source files are UTF-8,
  BOM-free, CR-free, NUL-free, and LF-terminated.  The word “verify” appears
  only as ordinary prose, not as an unresolved `VERIFY` marker.
- No compilation was performed.  The 1,990-line, approximately 8,856
  de-TeXed-word manuscript has eight main sections, no appendix, expanded
  proof-ledger tables and derivations, and only excluded references.  The
  locked 24–29 substantive-page range is credible from static source evidence;
  this is a feasibility judgment, not a PDF/build assertion.

No mathematical, source-hygiene, citation, anonymity, or scope blocker was
found in the frozen repair source.

PAPER_SOURCE_R1_R0_REPAIR_PASS
