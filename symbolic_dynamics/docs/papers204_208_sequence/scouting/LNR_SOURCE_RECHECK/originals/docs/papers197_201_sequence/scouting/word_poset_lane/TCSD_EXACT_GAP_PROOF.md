# TCSD exact gap product: proof completion before manuscript freeze

## Claim and status

Status: **PROVABLE AS STATED**. This supplements the earlier fibre certificate
by replacing its implicit gap merging with an exact formula. It does not
change the frozen literal map or promote a paper number.

For a target $y$, delete its zero symbols and let $w$ be the resulting cyclic
strict-sign word of length $r$. Write $F_0=0,F_1=1$ and $L_0=2,L_1=1$ for the
Fibonacci and Lucas sequences. If $w$ contains both signs and every cyclic
sign run has length at most two, let $q$ be the number of length-two runs.
When $q>0$, let $g_j$ count the singleton runs between the $j$th doubled run
and the next doubled run, cyclically. Then the fibre has the exact value

$$|D^{-1}(y)|=\prod_{j=1}^{q}F_{g_j+1},\qquad
r=2q+\sum_{j=1}^{q}g_j. \tag{G1}$$

When $q=0$, $r$ is even and the fibre is $L_r$. An all-zero target has fibre
three. A nonempty single-sign skeleton, or a skeleton with a cyclic run of
length at least three, has fibre zero.

## Assumptions and notation

The carrier, cyclic label convention and map are those of
`TCSD_THEOREM_CONTRACT.md`: $n\ge1$ and
$D(x)_i=\operatorname{sgn}(x_{i+1}-x_i)$ on $\{-1,0,1\}^{\mathbb Z/n\mathbb Z}$.
Rows and columns are numbered $1,2,3$ in increasing letter order. Let

$$U=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix},
\quad L=U^\mathsf T,\quad E_{ab}=e_a e_b^\mathsf T.$$

The symbol $L$ for the lower matrix is distinguished from indexed Lucas
numbers $L_r$. All skeletons remain cyclic, including the last-to-first run.

## Strategy and dependencies

1. The comparison-walk trace gives the fibre and removes zero letters.
2. A doubled run is a rank-one matrix, so cyclic trace splits into scalar gaps.
3. Each gap scalar is a Fibonacci number.
4. A Fibonacci addition identity bounds every nonalternating fibre, including
   all equality cases, without a claim of strictness at each individual merge.

## Proof

**Step 1: comparison trace.** The fibre is the trace of the product of $U,L,I$
chosen by the target signs. Factors $I$ may be removed. A nonempty skeleton
of one sign gives the trace of a strictly triangular power, hence zero.
Since $U^3=L^3=0$, a cyclic run of length at least three also gives zero.
If both signs occur, the number of cyclic runs is even. Therefore

$$q\equiv r\pmod 2. \tag{G2}$$

**Step 2: rank-one splitting.** A doubled positive run is $U^2=E_{13}$ and a
doubled negative run is $L^2=E_{31}$. For matrices $B_j$ between consecutive
rank-one blocks, direct multiplication gives

$$\operatorname{tr}(u_1v_1^\mathsf TB_1\cdots
u_qv_q^\mathsf TB_q)=\prod_{j=1}^{q}v_j^\mathsf TB_ju_{j+1},
\quad u_{q+1}=u_1.$$

**Step 3: compute a gap.** Suppose the starting block is $U^2$; exchanging
levels $1$ and $3$ covers the other starting sign. If $g=2a$, the intervening
product is $(LU)^a$ and the next block is $L^2$. The scalar is
$e_3^\mathsf T(LU)^ae_3=F_{2a+1}$. If $g=2a+1$, the intervening product is
$(LU)^aL$ and the next block is $U^2$. The scalar is
$e_3^\mathsf T(LU)^aLe_1=F_{2a+2}$.

To verify both formulas, for $a\ge1$ the lower-right two-by-two block of
$(LU)^a$ equals

$$\begin{pmatrix}F_{2a-1}&F_{2a}\\F_{2a}&F_{2a+1}\end{pmatrix}.$$

This follows by induction from $LU$ and the Fibonacci recurrence. The $a=0$
scalars are directly $1=F_1$ and $1=F_2$. Substituting these gap scalars proves
(G1). If there is no doubled run, $w$ is alternating of even length $r=2a$;
the upper-left block of $(UL)^a$ gives trace $F_{2a+1}+F_{2a-1}=L_{2a}$.

**Step 4: sharp comparison.** For integers $a,b\ge1$, Fibonacci addition gives

$$F_{a+b-1}=F_aF_b+F_{a-1}F_{b-1}\ge F_aF_b.$$

Repeatedly applying it to (G1) yields

$$|D^{-1}(y)|\le F_{1+\sum g_j}=F_{r-2q+1}. \tag{G3}$$

If $r$ is even and $q>0$, (G2) forces $q\ge2$ and $r\ge4$, so
$F_{r-2q+1}\le F_{r-3}<L_r$. Thus the only maximizers at even strict length
are the two alternating words.

If $r\ge3$ is odd, (G2) forces $q\ge1$. At $q=1$, (G1) gives exactly
$F_{r-1}$. At $q\ge3$, $r\ge7$ and
$F_{r-2q+1}\le F_{r-5}<F_{r-1}$. Thus exactly one doubled run is necessary
and sufficient for a maximum at odd strict length. The formal $r=1$ maximum
is zero and all such skeletons are outside the image.

Finally optimize over $0\le r\le n$, remembering the all-zero fibre three.
At even $n\ge4$, $r=n$ strictly dominates every smaller strict length. At
odd $n\ge5$, $r=n-1$ strictly dominates the odd endpoint $F_{n-1}$ and every
smaller strict length. The maximum is therefore $L_{2\lfloor n/2\rfloor}$,
with two fully alternating targets for even $n$ and $2n$ targets with one
zero and otherwise alternating signs for odd $n$. At $n=2,3$ the all-zero
target also ties at three. At $n=1$ it is the sole image target and its
fibre is three. This proves the extremum and all equality cases. $\square$

## Remaining boundary

This closes a proof exposition gap and adds the explicit formula (G1).
It is not an external originality assessment. Paper-stage independent
reviewers must still attack both this formula and the forward temporal proof.
