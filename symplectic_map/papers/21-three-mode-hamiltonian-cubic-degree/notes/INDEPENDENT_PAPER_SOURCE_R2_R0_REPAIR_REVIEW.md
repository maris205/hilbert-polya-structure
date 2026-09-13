# Independent Repair-Source R2 Review — Paper 21

Verdict: PASS.

## Independence, authority, and frozen bytes

I acted as a fresh repair-source R2 reviewer, independently of the author and
the repair-source R1 reviewer.  I read the publication-stage scope, source and
publication locks, paper plan, proof package, `BUILD_R0_BLOCKER.md`,
`R0_PROOF_FIRST_SOURCE_REPAIR.md`, the complete frozen source trio, and the
fresh R1 repair-source review.  I treated every older source review and both
PAGEFIX reviews binding `910086eb...` as stale and without authority over the
current source.  I did not compile or invoke BibTeX, run CAS or numerical code,
use a network or dataset, edit source or dashboard files, or rely on generated
output.  This note is my sole project write.

The identities checked before and after the audit are:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 84,917 | 1,990 | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |
| fresh repair-source R1 review | 6,040 | 110 | `07114e0da0eb41ed827f86064186639ffed49c2be2db97bf3e016d7390fface0` |

The R1 review ends in `PAPER_SOURCE_R1_R0_REPAIR_PASS`.  Its presence was
checked as a prerequisite, not used as a substitute for the recomputations
below.

## Independent theorem-critical recomputation

### Maps, derivatives, and canonical blocks

Direct differentiation gives

\[
\nabla V=(2q_1q_2^2q_3^2+gq_1^{g-1},
2q_1^2q_2q_3^2,2q_1^2q_2^2q_3)
\]

and

\[
\nabla W=(2p_1p_2^2p_3^2,
2p_1^2p_2p_3^2,2p_1^2p_2^2p_3+gp_3^{g-1}).
\]

The displayed Hessians have the correct diagonal and mixed derivatives and are
symmetric.  Subtraction gives the stated polynomial inverses.  With the
W-Hessian evaluated at the intermediate vector
`P=p+\nabla V(q)`, the Jacobian blocks are

\[
J_S=\begin{pmatrix}I&0\\H_V&I\end{pmatrix},\qquad
J_T=\begin{pmatrix}I&H_W\\0&I\end{pmatrix}.
\]

Multiplication against
\(\Omega=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)\)
gives exactly the two displayed matrices with skew blocks
\(H_V-H_V^{\mathsf T}\) and \(H_W^{\mathsf T}-H_W\), hence both pullbacks are
\(\Omega\).  The full derivative is correctly ordered as \(J_TJ_S\).

### Support, phase matrices, and selectors

The six derivative rows are exhaustive.  Reading their selected exponents gives

\[
A_g=\begin{pmatrix}g-1&0&0\\2&1&2\\2&2&1\end{pmatrix},\qquad
B_g=\begin{pmatrix}1&2&2\\2&1&2\\0&0&g-1\end{pmatrix},
\]

and hand multiplication gives

\[
C_g=B_gA_g=
\begin{pmatrix}
g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1
\end{pmatrix}.
\]

Only the first V-row and third W-row contain two monomials.  For
\(x=u_2/u_1\), \(y=u_3/u_1\), the first score subtraction is

\[
(g-1)u_1-(u_1+2u_2+2u_3)=u_1(g-2-2x-2y).
\]

For the second subtraction it is essential to use the new phase vector
\(v=A_gu\).  Its entries are
\((g-1,2+x+2y,2+2x+y)u_1\); therefore the pure and mixed W-scores differ by

\[
(g-1)v_3-(2v_1+2v_2+v_3)
=u_1\bigl((2g-6)x+(g-6)y-6\bigr).
\]

Thus the corrected \(M_T\), the phase at which it is evaluated, and the claim
of exactly two selector faces are all correct.  On the stated cone,
\(M_S>1\) and \(M_T\geq3g-18\geq6\).

### Complete cone algebra

For \(U'=C_gU\) and \(D=g+7+6x+6y\), row subtraction gives

\[
X'-1=\frac{g-3-x-2y}{D},\qquad
Y'-1=\frac{g-9+(2g-8)x+(g-7)y}{D}.
\]

With \(h=g-3-2x-2y\), the repair's identities
\(M_S=1+h\) and \(X'-1=(x+h)/D\) are exact.  The Y numerator has the lower
bound \(4g-24\).  Expanding every row of the height functional gives

\[
H_2=(g-3)U'_1-2U'_2-2U'_3=U_1Q,
\]

\[
Q=g^2-4g-25+2(g-12)x+4(g-6)y.
\]

For \(8\leq g\leq11\), multiplying
\(x<(g-3)/2-y\) by the negative coefficient \(2(g-12)\) reverses the
inequality and yields

\[
Q>2g^2-19g+11+2gy\geq2g^2-17g+11
=3+(g-8)(2g-1)\geq3.
\]

For \(g\geq12\), substitution of \(x,y\geq1\) gives

\[
Q\geq g^2+2g-73=95+(g-12)(g+14)>0.
\]

The X, Y, and upper-height faces are therefore all strict, with no missing cone
face or endpoint error.

### Phase indexing, carries, and coefficient survival

The six-coordinate update is correctly ordered:

\[
\widetilde P^{(n+1)}=P^{(n)}+\nabla V(Q^{(n)}),\qquad
Q^{(n+1)}=Q^{(n)}+\nabla W(\widetilde P^{(n+1)}),
\]

with \(P^{(n+1)}=\widetilde P^{(n+1)}\).  Starting from
\(u_0=\mathbf1\), this supports precisely

\[
v_{n+1}=A_gu_n,\qquad u_{n+1}=C_gu_n.
\]

At the seed, \(A_g\mathbf1=(g-1,5,5)^T>\mathbf1\).  At later S-phases,
\(v_n=A_gu_{n-1}\) and
\(A_g(u_n-u_{n-1})>0\) row by row.  At every T-phase, including \(n=0\),

\[
B_gv_{n+1}-u_n=(C_g-I)u_n>0,
\]

because every entry of \(C_g-I\) is positive.  Hence neither carried P nor
carried Q can replace the fresh selected row.  The temporary symbol \(p_n\) in
the old-term proposition is fixed there by the equation
\(p_n=A_gu_{n-1}\) and is the carried p-degree vector denoted \(v_n\) in the
six-coordinate ledger; it creates no competing recurrence or index shift.

The first two audit vectors also recompute exactly:

\[
u_1=(g+19,2g+13,5(g-1))^T,
\]

\[
v_2=((g-1)(g+19),14g+41,11g+59)^T,
\]

\[
u_2=(g^2+68g+181,2g^2+72g+121,11g^2+48g-59)^T.
\]

The coefficient witnesses have the right semantics.  They exhibit one positive
contribution for each selected gradient row; they do not claim uniqueness of a
coefficient path.  Any additional path adds a nonnegative integer because all
forward coordinate polynomials remain in the positive semiring.  The six
witnesses
\(ga_1^{g-1}\), \(2a_1^2a_2a_3^2\),
\(2a_1^2a_2^2a_3\), \(2b_1b_2^2b_3^2\),
\(2b_1^2b_2b_3^2\), and \(gb_3^{g-1}\) are therefore nonzero in
characteristic zero.  This proves existence and survival of a top-degree
monomial without the false assertion that every expansion path is unique.

### Six-coordinate visibility and Perron squeeze

The difference

\[
C_g-A_g=
\begin{pmatrix}8&6&6\\2g+2&4&2\\2g-4&2g-4&g-2\end{pmatrix}
\]

is entrywise positive.  Thus \(u_n>v_n\) coordinatewise.  Row subtraction in
the q-vector gives

\[
U_3-U_2=[-6+(2g-7)x+(g-5)y]U_1,
\]

\[
U_3-U_1=[g-9+(2g-8)x+(g-7)y]U_1,
\]

with lower bounds \(3g-18\) and \(4g-24\).  Combining corresponding q/p
dominance with these two q-row inequalities proves that q3, and not merely some
unspecified maximum, is the unique visible coordinate for every \(n\geq1\).
The \(n=0\) tie is separately and correctly handled.  Consequently

\[
\deg(F_g^n)=e_3^TC_g^n\mathbf1\qquad(n\geq0).
\]

The Perron argument is a genuine one-row squeeze.  For a positive right Perron
vector \(r\), constants \(a,b>0\) with
\(ar\leq\mathbf1\leq br\) give

\[
a\rho(C_g)^nr_3\leq e_3^TC_g^n\mathbf1
\leq b\rho(C_g)^nr_3.
\]

Taking roots proves that this exact visible row has exponential rate
\(\rho(C_g)\); no unproved max-over-rows substitution occurs.  The row sums are
\(g+19\), \(2g+13\), and \(5(g-1)\), and their gaps below \((g-1)^2\) are
respectively
\((g-6)(g+3)\), \((g-6)(g+2)\), and \((g-1)(g-6)\).

### Cubic audit and boundary

The trace is \(2g+11\).  The three principal minors are
\(11-7g\), \((g-1)(g-5)\), and \(-3(g-1)\), whose sum is
\(g^2-16g+19\).  Also
\(\det A_g=\det B_g=-3(g-1)\), hence
\(\det C_g=9(g-1)^2\).  These invariants give exactly

\[
\chi_{C_g}(t)=t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2.
\]

For \(g\bmod5=2,3,4\), the reductions are respectively
\(t^3+t+1\), \(t^3-2t^2-1\), and \(t^3+t^2+t-1\).  Their value rows at
\(t=0,1,2,3,4\) recompute as
\((1,3,1,1,4)\), \((4,3,4,3,1)\), and \((4,2,3,3,3)\), so each cubic has no
root modulo five.  The irreducibility and degree-three Perron conclusions are
therefore valid for precisely the claimed infinite subfamilies.

At \(g=7\), the seed has \(x=y=1\) and
\(x+y=(g-3)/2=2\), while \(M_S=1\).  The manuscript correctly records this as
failure of strict cone entry, not as a selector tie or a theorem at \(g=7\).

## Scope, citations, anonymity, and static source

- The exact locked metadata title is present, the typeset title uses the
  expressly permitted \(\mathbb A^6\) rendering, the author is exactly
  `Anonymous Authors`, and the source date is empty.  No private identity,
  affiliation, email, ORCID, acknowledgment, funding, local path, digest,
  reviewer/model identity, venue, or submission provenance appears in public
  manuscript text or metadata.
- Exactly two citation commands occur, one each for `BlancVanSanten2019` and
  `ShaoSun2025`, and the bibliography contains exactly those two matching
  entries.  Their uses remain affine-triangular terminology and dimension-four
  algebraic-degree context only; neither supplies theorem proof, priority, or
  classification authority.
- The theorem and section order remain L1 through L9.  There are eight main
  sections, no appendix or figure, and no theorem-critical external dependency.
  The anti-claims exclude genericity, arbitrary dimensions or characteristic,
  entropy, periodic/trace/multiplier/torus enlargement, universal conjugacy or
  classification, priority, and computer-assisted proof.
- Static closure gives 720 opening and 720 closing braces, 119 properly nested
  begin/end pairs, 56 unique labels, and 65 ref/eqref uses with no missing
  target.  Citation keys close exactly.  The trio is valid UTF-8, BOM-free,
  CR-free, NUL-free, and LF-terminated.  No unresolved TODO, FIXME, VERIFY,
  placeholder, or undefined-reference marker occurs.
- Without compiling, the 1,990-line and approximately 8,856-word source, with
  thirteen proof-ledger tables, about one hundred displayed-math environments,
  and twenty-seven theorem-like environments, credibly supports the locked
  24--29 substantive-page band.  Relative to the historical 21-page blocked
  source, the repair adds 17,312 bytes and 436 lines before the unchanged
  references, an expansion of roughly one quarter concentrated in substantive
  proof material.  This is a source-feasibility judgment; only a separately
  authorized build can certify the actual page count.

No theorem, proof, phase, coefficient, visibility, spectral, arithmetic,
citation, anonymity, static-source, scope, or page-feasibility blocker was found
in the frozen R0-repair source.

PAPER_SOURCE_R2_R0_REPAIR_PASS
