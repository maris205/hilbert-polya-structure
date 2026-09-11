# C12 rank-at-most-one residual: elementary complete one-step fibres

Author hand deduction, 2026-09-11. **OLD-KERNEL RESIDUAL / NO_NEW_LITERAL /
NO_PROMOTION.** No pilot, source program, manuscript or central edit.
The first Fresh25 handoff is unchanged. This note is not independently reviewed.

## Claim and status

Let $q$ be any prime power, $V=\mathbb F_q^2$, and
$X=\{(A,B):\operatorname{rank}A,\operatorname{rank}B\le1\}$.
The old C12 map $T(A,B)=(AB,BA)$ preserves $X$. The deductions below are
**PROVABLE AS STATED**, but their combination is below the paper-value gate:
the dynamics is scalar monomial iteration with at most two projective phases;
the inverse is ordinary rank-one outer-product factorization.

## Temporal reduction, including exceptional traces

Write $a=\operatorname{tr}A$, $b=\operatorname{tr}B$,
$c=\operatorname{tr}(AB)$. Rank at most one gives
$A^2=aA$, $B^2=bB$, and $ABA=cA$, $BAB=cB$, including zero matrices.
Consequently
$$T^2(A,B)=(cbA,caB).$$
These identities follow by writing each nonzero rank-one matrix as a column
times a row; the middle products are scalars. No spectral theorem is needed.

If $abc=0$, then $T^3(A,B)=(0,0)$: when $c=0$ this already holds at time two;
when $c\ne0$ but $a=0$ or $b=0$, at least one component at time two is zero.
Time three is sharp even over $\mathbb F_2$: take
$$A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\1&0\end{pmatrix}.$$
Here $a=0,b=c=1$ and $T^2(A,B)=(A,0)\ne(0,0)$.

If $abc\ne0$, put $E=A/a$, $F=B/b$, $k=\operatorname{tr}(EF)=c/(ab)$.
Then $E,F$ have trace one and are idempotent, and
$$T^2(A,B)=(abcE,abcF),\qquad
T^2(\lambda E,\lambda F)=(k\lambda^4 E,k\lambda^4 F).$$
Thus after time two, even iterates lie on a single scalar ray and odd iterates
on its image ray. Since $k\ne0$, this stratum never reaches zero. Its scalar
map is $\lambda\mapsto k\lambda^4$ on $\mathbb F_q^*$; in a cyclic-generator
coordinate it is the standard affine exponent map $j\mapsto4j+d$ modulo
$q-1$, where $k=g^d$. It need not be conjugate by scalar rescaling to pure
fourth powers: that would require a suitable cube root of $k$. Coincident
projective phases can shorten the original $T$ period, so no unsupported
exact period formula is inferred from the two-step description.

## Complete one-step inverse census and extremum

Let $R=(q^2-1)^2/(q-1)$, the number of nonzero rank-one endomorphisms of $V$.
For every target $(P,Q)\in X$:

| Target | Number of predecessors in $X$ |
|---|---:|
| $(0,0)$ | $1+(q+1)R$ |
| Exactly one component nonzero, and that component nilpotent | $q(q^2-1)$ |
| Both components nonzero, with equal nonzero traces | $q-1$ |
| Every other target | $0$ |

Proof strategy: separate zero products, then determine the image/kernel lines
of both factors. This supplies every fibre, rather than a formal counting sum.

1. A rank-one map is $uv$ with nonzero column $u$ and row $v$. Exactly $q-1$
   such pairs represent each map, proving the value of $R$.
2. For zero target, pairs with a zero factor contribute $2R+1$. For each
   nonzero $A$, both products vanish precisely when
   $\operatorname{im}B=\ker A$ and $\ker B=\operatorname{im}A$.
   There are $q-1$ such nonzero $B$, yielding $R(q-1)$ more.
3. For target $(P,0)$ with $P\ne0$, trace equality forces $\operatorname{tr}P=0$;
   a rank-one two-dimensional matrix of trace zero is nilpotent. Choose
   $P=ut$ with $tu=0$. Every preimage uniquely has $A=uv$, $B=st$,
   where $v$ is a nonzero row, $s$ a column, and $vs=1$.
   Indeed $AB=P$ forces $\operatorname{im}A=\operatorname{im}P$ and
   $\ker B=\ker P$, and conversely $BA=s(tu)v=0$.
   Each of the $q^2-1$ nonzero rows has $q$ solutions to $vs=1$.
   Swapping the factors proves the reversed-target case.
4. For nonzero $P=ut$ and $Q=sv$, a preimage must have
   $A=\alpha uv$ and $B=\beta st$ with $\alpha,\beta\ne0$, by their forced
   image and kernel lines. The two product equations are
   $\alpha\beta(vs)=1$ and $\alpha\beta(tu)=1$.
   Their solvability is exactly $\operatorname{tr}P=tu=vs=\operatorname{tr}Q\ne0$,
   and then exactly $q-1$ choices of $\alpha$ determine $\beta$.

These cases exhaust $X$. The zero target uniquely maximizes the fibre:
$$1+(q+1)R>q(q^2-1)>q-1\qquad(q\ge2),$$
because $(q+1)R/[q(q^2-1)]=(q+1)^2/q>1$.

## Subtraction, provenance and stopping reason

The complete old `papers122_126_sequence/phase1/HOSTILE_GATE_GROUP_PRODUCT_EXCHANGE.md`
and the original algebraic scout lines 54–78 were actually read. The old gate
leaves broader matrix rank-stable dynamics open, so it does not itself refute
this restriction. Nevertheless this restriction reduces immediately to scalar
monomials plus standard factorization; its trace-zero exceptions die in three
steps and introduce no deeper recurrent mechanism. The full fibre formula
above is a useful elementary residual, not evidence of a new literal or a
paper-scale independent engine. No assertion that the exact table was already
printed in the old group gate or a primary paper is made.

Three bounded Web calls searched rank-one/Thue–Morse/AB–BA and finite-field
rank-one counting, then attempted the [primary Almeida CIM article](https://www.cim.pt/magazines/bulletin/26/article/197/pdf).
The direct primary open returned Internal Error. The final exact-locator
search returned irrelevant results. Other hits were merely adjacent metadata
(including the primary arXiv record *Weight and rank of matrices over finite
fields*, math/0403314), not a read of this fibre theorem. No primary body was
successfully retrieved and no search non-hit establishes novelty. The old
gate's Almeida ownership statement is attributed to that read gate, not
misreported as a fresh primary inspection. All mathematical claims in this
note have the self-contained author proofs above. Native requests/returns
remain in the conversation; no extra receipt package was generated.

Recommendation: stop this residual without pilot or expansion. Zero new
literals/admissions/reserves; HOLD_EXTERNAL. No impossibility statement about
the unrestricted C12 matrix carrier follows.
