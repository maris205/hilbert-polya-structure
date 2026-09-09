# Independent bounded check of the coordinator's nonlinear-geometry deductions

2026-09-08 UTC. Nonauthor mathematical/source cross-check requested by
the coordinator. The three files in `../nonlinear_geometry/` were read
in full: `FROZEN_QUESTIONS.md`, `PROOF_AND_GAPS.md`, and
`SOURCE_AUDIT.md`. Only this review file was written. No mathematical
program, probe, old census, build or source-file edit was performed.

**Disposition:** the specified NG2-F counterexample, clock relation,
fixed-fibre finiteness deduction and NG2-V difference identities are
`PROVABLE AS STATED`. No substantive defect was found in those claims.
This is not approval of a complete atlas or a paper admission: the
coordinator expressly leaves both full questions unclosed, correctly.

## 1. Fixed native word versus the full Vieta group

At $A=B=C=0$, let $F(x,y,z)=(y,z,yz-x)$ and
$P=(-1,3,-1)$. Directly, without a program,

$$
P\xmapsto{F}(3,-1,-2)
\xmapsto{F}(-1,-2,-1)
\xmapsto{F}(-2,-1,3)
\xmapsto{F}P.
$$

These four triples are distinct, and $K(P)=11-3=8$. Since $T=F^3$,
the same four points form one least-period-four $T$-cycle.

Separately, $s_zs_x(P)=(-2,3,-5)$. On the plane $z=-5$, the word
$s_ys_x$ sends $(-u,v,-5)$ to $(-u',v',-5)$ with

$$
u'=5v-u,\qquad v'=5u'-v.
$$

If $0<u<v$, then $u'>4v$, whence $v<u'/4$ and
$v'>19u'/4>4u'>16v$. Starting at $(u,v)=(2,3)$ preserves
$0<u'<v'$ and strictly unbounded growth. Thus these are infinitely
many distinct integral points in the **same full group orbit** of $P$.
The counterexample is valid on the same invariant level, not a
comparison across different fibres or different coefficient families.
It disproves substituting finite full-group orbit for fixed-word
periodicity. It does not claim that a group-orbit equivalence theorem
is itself false or that no later use of such a theorem can help.

## 2. Clock and elementary equations

Three scalar updates with forcing $A,B,C$ send
$(x_0,x_1,x_2)$ to $(x_3,x_4,x_5)$, exactly the ordered product
$s_zs_ys_x$. At $A=B=C=a$, these are three iterates of the single
cyclic map $F_{3,a}$; hence $T=F_{3,a}^3$. An $F$-cycle of least
period $r$ breaks into $\gcd(r,3)$ cycles under addition by three
on $\mathbb Z/r\mathbb Z$, each of least period
$r/\gcd(r,3)$. The author's clock conversion is exact.

Subtracting adjacent forced recurrences and writing
$d_i=x_{i+2}-x_i$ gives

$$
x_{i+3}-x_{i-1}
=(x_{i+1}+1)(x_{i+2}-x_i)+(a_i-a_{i-1}),
$$

which is precisely (F1), because its left side is
$d_{i+1}+d_{i-1}$. In particular, the extra forcing term cannot be
removed in the unequal-coefficient family.

The fixed-point assertion also holds: the final first coordinate of
$T$ is the value after $s_x$; equality with the initial point forces
$s_x$ to fix it. The final second coordinate then forces $s_y$ to
fix it, and the last forces $s_z$ to fix it. This yields exactly
$2x=A+yz$, $2y=B+xz$, $2z=C+xy$. The axis control at $A=B=0$ is
$T(0,0,t)=(0,0,C-t)$; its level equation is $t^2-Ct=D$.
It illustrates why fixed-fibre finiteness is not global finiteness
over all levels.

## 3. Cantat's source scope supports the stated limited deduction

The review directly accessed
[Cantat, arXiv:0711.1727v2](https://arxiv.org/pdf/0711.1727v2),
specifically the full-parameter family definition, §2.3 boundary and
matrix formulas, Proposition 2.2, Theorem 3.1 with its displayed
proof, and Proposition 3.2/Corollary 3.3 with their displayed proofs.
No new broad literature search or final-journal-version verification
was undertaken. These are remote theorem/section references, not new
local PDF page anchors.

The substitution $z\mapsto-z$ changes the coefficients to
$(A,B,-C,D)$ in the source's plus-$xyz$ equation. Its family ranges
over every complex quadruple; the argument is not restricted to
integral boundary traces from a surface representation. Its §2.3
expressly states smoothness near the whole triangle at infinity for
every parameter choice, allowing singularities inside the affine
surface. The matrix multiplication is

$$
r_zr_yr_x=\begin{pmatrix}1&2\\-2&-5\end{pmatrix},
\quad \det=-1,\quad\operatorname{tr}=-4,
\quad\rho=2+\sqrt5>1.
$$

The cyclic word uses each involution once and has no cyclic
cancellation, so Proposition 2.2 gives algebraic stability for this
actual word. No passage to a different clock or a conjugated word is
needed.

For clarity, the compactness deduction can be made explicit. On each
fixed projective fibre, Corollary 3.3's proof chooses a neighborhood
$B$ of $v_-$ in the inverse-attracting basin and a neighborhood $V$
of the rest of the boundary in the forward-attracting basin. Their
union covers the triangle at infinity. A periodic affine point lies
in neither: forward or inverse convergence to a boundary vertex is
incompatible with a finite affine orbit. Therefore all periodic
points lie in

$$
\overline S\setminus(B\cup V),
$$

a compact **subset of the affine surface**. Its intersection with
$\mathbb Z^3$ is finite. The neighborhood construction occurs near
the smooth boundary, so affine singular fibres do not invalidate it.
This is the limited source consequence stated in the author's package.

The conclusion fixes **all of $A,B,C,D$**. It supplies neither a
bound uniform in $D$ nor a known effective enumeration radius, and
cannot alone be called a terminating full-parameter atlas. The author's
separation of these obligations is correct. No periodic-point count,
source-owned entropy theorem or compactness lemma is approved here as
an independent paper increment.

## 4. NG2-V identities preserve the full zero/sign domain

For the unforced difference of the two original recurrences, the
overlap product is $p_i=\prod_{j=2}^{n-1}x_{i+j}$. Thus

$$
u_{i+n}+u_i
=p_i(x_{i+n}-x_{i+1})
=p_i\sum_{j=1}^{n-1}u_{i+j},
$$

which verifies (V1) with every index unchanged. No division is used.
The maximum bound (V2) is valid but only bounds this product times
the full sum, not its individual summands.

For $d_i=x_{i+n-1}-x_i$, set
$q_i=\prod_{j=1}^{n-2}x_{i+j}$. Subtraction at $i$ and $i-1$
gives

$$
x_{i+n}-x_{i-1}=(1+q_i)d_i.
$$

Writing the left side as
$d_{i+1}+x_{i+1}-x_{i-1}$ verifies (V3). Only when $n=3$ is
$x_{i+1}-x_{i-1}=d_{i-1}$, with $q_i=x_{i+1}$.
The warning against carrying the three-variable tridiagonal argument
over unchanged is therefore justified.
The displayed $n=4$ two-zero word has $x_{i+4}=-x_i$ and every
$p_i=0$, so it satisfies the claimed boundary check for arbitrary
integer amplitudes. It does not provide the missing global support
exhaustion.

## Final scope

No mathematical correction is required for the specified helper claims.
The phrase "compact and affine" is most precisely read as "a compact
subset of the affine surface," not an assertion that a topological
complement is an affine algebraic variety. This clarification does not
change the argument. The source check above does not independently
re-audit all of Shin's paper or certify the coordinator's entire search
ledger. Both original questions correctly remain unclosed and not
admitted; AM1 and AR2 admission are outside this review.
`NO_BAD_EULER_OR_ROOT_NUMBER`.
