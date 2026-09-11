# SPR: sharp height thresholds and full target fibres

Author/proof contributor: `/root/round211_arithmetic_scout`, 2026-09-08 UTC.
This is an author scouting proof, not an independent review or admission.
Status of the statements below: **PROVABLE AS STATED**. Source/value review
and finite verifier pressure are separate obligations, not premises.

## 1. Carrier, map, claims and conventions

Fix integers $n\ge1$ and $M\ge0$. The carrier is
$X_{n,M}=\{0,\ldots,M\}^n$, with labelled coordinates. If $x$ has at most
one positive coordinate, put $T(x)=x$. Otherwise let $p(x)$ be its second
smallest positive entry, counting multiplicities, and put
$$T(x)_i=x_i\bmod p(x).$$
The remainder is the ordinary integer in $\{0,\ldots,p(x)-1\}$. Every
positive coordinate equal to the pivot becomes zero. Zeros remain zero.

Write $h(x)$ for the first time that $x$ reaches a recurrent state, and
$H(n,M)=\max_{x\in X_{n,M}}h(x)$. For a finite nonnegative vector $v$,
$S_j(v)$ means the sum of its $j$ largest entries, padding with zeros when
$j$ exceeds its length. Say $u\preceq_w v$ when $S_j(u)\le S_j(v)$ for
every integer $j\ge1$. This is weak majorization in the largest-sum
convention; vectors of different lengths are compared after zero padding.

For a positive sorted tuple $a=(a_1\le\cdots\le a_s=m)$ with $s\ge2$, set
$$R(a)=(m,m+1,m+1+a_1,\ldots,m+1+a_{s-1}). \tag{1}$$
The displayed tuple is sorted. Define
$$c^{(1)}=(1,1),\qquad c^{(t+1)}=R(c^{(t)}),\qquad
   m_t=\max c^{(t)}. \tag{2}$$
Thus $c^{(t)}$ has exactly $t+1$ positive entries. This deterministic
integer-vector recurrence uses addition and a moving maximum only; it
does not iterate $T$, enumerate a carrier or call an optimization oracle.

**Temporal theorem.** The recurrent states are exactly the states with
at most one positive entry, and all are fixed. For every $t\ge1$, every
state with $h(x)\ge t$ satisfies
$$c^{(t)}\preceq_w x. \tag{3}$$
The tuple $c^{(t)}$, in any labelled order and with any number of zero
coordinates appended, has height exactly $t$. Consequently
$$H(n,M)=\max\bigl(\{0\}\cup
 \{t\ge1:t+1\le n,\ m_t\le M\}\bigr). \tag{4}$$
This is a sharp simultaneous height threshold for every $n,M$, not a
nonsharp support bound. No classification of all maximizing sources is
claimed.

**Inverse theorem.** Fix $y\in X_{n,M}$. Put $r=|\{i:y_i>0\}|$ and
$k=n-r$. For each integer $p$ with $\max_i y_i<p\le M$, let
$$B=\lfloor M/p\rfloor,\quad
 A_i=\lfloor(M-y_i)/p\rfloor\quad(y_i>0),$$
$$P=\prod_{i:y_i>0} A_i,\qquad
 Q=\sum_{i:y_i>0}\prod_{j:y_j>0,\ j\ne i} A_j.$$
Empty products equal one; the empty sum equals zero. Define
$$D_k(B)=(B+1)^k-B^k,$$
$$E_k(B)=(B+1)^k-B^k-kB^{k-1}\quad(k\ge1),\qquad E_0(B)=0.$$
In these sums $B\ge1$, so the case $k=1$ uses $B^0=1$ without a
zero-to-negative-power convention. Then
$$|T^{-1}(y)|=\mathbf1_{\{r\le1\}}+
 \sum_{p=\max y+1}^{M}\bigl(D_k(B)Q+E_k(B)P\bigr). \tag{5}$$
An empty pivot range contributes zero. Every source is recovered by the
disjoint pivot/residue construction in Section 5.

For $n\ge2$ and $M\ge1$, the **unique** target maximizing (5) is $0^n$,
with exact maximum
$$1+\sum_{p=1}^{M}\left[
  (\lfloor M/p\rfloor+1)^n-\lfloor M/p\rfloor^n
  -n\lfloor M/p\rfloor^{n-1}\right]. \tag{6}$$
For $n=1$, $T$ is the identity and every target has one source; for $M=0$
the zero vector is the only state.

## 2. Strategy and dependency separation

The temporal argument has three ingredients: a sharp lower bound for every
predecessor in weak majorization; monotonicity of the additive reverse
construction across different support sizes; and an attaining chain.
Ordinary support descent supplies only termination and is assigned zero
contribution credit. The sharper inequality (3) is the substantive claim.

The inverse argument instead records the selected pivot, the unique
possible subpivot source coordinate, and the number of coordinates equal
to the pivot. Independent quotient choices produce (5). A binomial
comparison over different support sizes proves the strict global maximum.
It neither uses (3) nor the sequence (2). Conversely the height proof
does not use fibre counts, their products, or the maximum comparison.
This is logical separation; an independent value desk must still decide
whether both residual axes clear the project's contribution threshold.

## 3. Termination and the sharp reverse-predecessor inequality

Every nonfixed state has at least two positive entries and loses at least
one of them, since a pivot entry becomes zero. No zero becomes positive.
It follows that every orbit reaches the at-most-one-positive set, which
is fixed by definition. There can be no other recurrent state: strict
support decrease precludes return to a state outside that set. A state
with $s$ positive entries has height at most $s-1$: until termination
support falls by at least one, and support two requires at most one more
step. Thus $h(x)\ge t$ implies $s\ge t+1$.

**Lemma 1.** If $T(x)=y$ and $y$ has at least two positive entries, let
$a=(a_1\le\cdots\le a_s=m)$ list its positive entries. Then
$$R(a)\preceq_w x. \tag{7}$$

**Proof.** The source cannot be in the identity branch because that branch
has at most one positive output. Write $p=p(x)>m$. At most one positive
source entry is less than $p$.

If such an entry exists, it is one of the target entries, say $a_j$.
Every other positive target entry $a_i$ comes from a source at least
$p+a_i$. There is also a source equal to $p$. Therefore $x$ contains a
submultiset bounded below entrywise by
$$V_j=(a_j,p,\{p+a_i:i\ne j\}).$$
Extra source entries only increase largest partial sums. Compare $V_j$
with $V_s$. Their total sums equal $sp+\sum_i a_i$. For every partial
sum up to $s-1$, their largest entries are chosen from the lifted values
$p+a_i$. Removing the largest $a_s$ minimizes each such largest partial
sum, so $S_q(V_s)\le S_q(V_j)$ for $1\le q\le s-1$. For $q=s$ the
sum is the common total minus the subpivot entry, again minimized by
removing $a_s$. For $q\ge s+1$ the sums agree. Hence
$V_s\preceq_w V_j\preceq_w x$. Reducing $p$ to $m+1$ decreases every
entry of $V_s$ except its first, and gives exactly $R(a)$.

If there is no positive source entry below $p$, there are at least two
entries equal to $p$; otherwise $p$ would be the smallest but not the
second smallest positive entry. Every $a_i$ is lifted to at least
$p+a_i$. Consequently $x$ contains a submultiset dominating
$$W=(p,p,p+a_1,\ldots,p+a_s).$$
The largest $q\le s-1$ entries of $V_s$ are a subset of the lifted
entries of $W$, so their sum is no larger. At $q=s$, $V_s$ has sum
$sp+\sum_i a_i-m$, whereas $W$ has largest-$s$ sum
$sp+\sum_i a_i$. At $q=s+1$, the total of $V_s$ is
$sp+\sum_i a_i$, at most the largest-$s+1$ sum of $W$,
$(s+1)p+\sum_i a_i$. For larger $q$ the sum of $V_s$ stays fixed.
Thus $R(a)\preceq_w V_s\preceq_w W\preceq_w x$. Both cases prove (7).
This argument includes repeated target values: deleting any occurrence
of a largest value gives the same sorted multiset. ∎

## 4. Monotone reverse construction and all-parameter height

**Lemma 2.** Let $a,b$ be positive sorted tuples of lengths $s\ge r\ge2$.
If $b\preceq_w a$, then $R(b)\preceq_w R(a)$.

**Proof.** Put $m=\max a$. The largest partial sums of (1) are
$$S_q(R(a))=
\begin{cases}
 q+(q-1)m+S_{q+1}(a),&1\le q\le s-1,\\
 s+(s-1)m+S_s(a),&q=s,\\
 s+sm+S_s(a),&q\ge s+1.
\end{cases} \tag{8}$$
The last expression is the total sum. Let $\ell=\max b\le m$.
For $q\le r-1$, the first expression for both tuples is monotone in
$m$ and $S_{q+1}$, proving the comparison. For $q=r$, if $s=r$ use the
second expression for both. If $s>r$, use the first expression for $a$;
$S_{r+1}(a)\ge S_r(a)\ge S_r(b)$ proves the same comparison.
For $q=r+1$, if $s=r$ compare the two totals. If $s\ge r+1$, formula
(8) gives a largest-$r+1$ sum at least
$r+1+rm+S_r(a)$, which exceeds or equals the total
$r+r\ell+S_r(b)$ of $R(b)$. All larger partial sums of $R(a)$ are
at least this one, while the sum of $R(b)$ stays fixed. ∎

We now prove (3) by induction on $t$. A state of positive height has at
least two positive integers, so its largest entry is at least one and
the sum of its two largest entries is at least two. This is precisely
$c^{(1)}\preceq_w x$, including all larger partial sums.

For $t\ge2$, let $h(x)\ge t$ and put $y=T(x)$. Then $h(y)=h(x)-1\ge
t-1$, so $y$ has at least $t$ positive entries and, by induction,
$c^{(t-1)}\preceq_w y$. Taking the positive sorted tuple of $y$ does
not change its largest partial sums. Lemma 2 and Lemma 1 give
$$c^{(t)}=R(c^{(t-1)})\preceq_w R(y^+)\preceq_w x.$$

The tuple $c^{(1)}=(1,1)$ maps to zero and has height one. If a positive
tuple $a$ is inserted in (1), its second smallest entry is exactly
$m+1$ and its remainder tuple consists of the entries of $a$, with one
additional zero: $m$ survives unchanged, each $m+1+a_i$ gives $a_i$,
and the pivot becomes zero. Sorting and zero padding commute with $T$,
since the rule depends only on positive order statistics. Induction
therefore proves $h(c^{(t)})=t$.

Necessity in (4) follows from support size and the $q=1$ case of (3):
$n\ge t+1$ and $M\ge m_t$. Sufficiency is the attaining tuple, padded
to length $n$. The maximum is finite because $t\le n-1$; the formula
also gives zero for $n=1$ or $M=0$. ∎

## 5. Disjoint every-target inverse and counting formula

Sources in the identity branch contribute exactly one if $r\le1$,
namely the source $x=y$, and none otherwise. Every other source has a
uniquely determined pivot $p$ in the sum range of (5).

Fix such a pivot. At a positive target coordinate $i$ the possible source
values are $y_i+pq_i$, with $q_i\ge0$. There is one subpivot choice
$q_i=0$, and there are exactly $A_i$ lifted choices $q_i\ge1$. At a
zero target coordinate, $q_i=0$ gives source zero; $q_i=1$ gives source
$p$; and $q_i=2,\ldots,B$ give source values above $p$. There are
exactly $B$ choices not equal to $p$ (zero plus the $B-1$ larger
multiples) and one choice equal to $p$.

The pivot is the second smallest positive source value in exactly two
disjoint cases:

1. Exactly one positive target coordinate takes its subpivot choice, and
   at least one zero target coordinate takes the value $p$.
2. No positive target coordinate takes a subpivot choice, and at least
   two zero target coordinates take the value $p$.

The first case has $Q$ choices on positive target coordinates and
$(B+1)^k-B^k=D_k(B)$ choices on zero coordinates. The second has $P$
positive-coordinate choices and $E_k(B)$ zero-coordinate choices;
subtracting $kB^{k-1}$ removes exactly-one-pivot choices. When $k=0$
both cases are impossible, accounted for by $D_0=E_0=0$.

Every combination satisfying either case has at least two positive
source entries, has second smallest positive value $p$, and reduces to
$y$ modulo $p$. Conversely, every nonidentity source has exactly one
of these descriptions. Its pivot and all quotients are recovered from
the source, so no duplication occurs across cases or different pivots.
This proves the decoder and (5). ∎

## 6. Unique maximum target

The zero target has $r=0$, $k=n$, $P=1$, $Q=0$, giving (6). We compare
each other target's contribution at each eligible pivot with $E_n(B)$.
Suppose $r\ge1$. Since $0\le A_i\le B$ and $B\ge1$,
$$P\le B^r,\qquad Q\le rB^{r-1}.$$
For $k\ge1$, expanding the resulting upper bound gives
$$D_k(B)Q+E_k(B)P
 \le B^{r-1}(B+r)(B+1)^k-(B+n)B^{n-1}. \tag{9}$$
The binomial theorem with nonnegative terms gives
$$B^{r-1}(B+r)=B^r+rB^{r-1}\le(B+1)^r.$$
Thus (9) is at most
$(B+1)^n-(B+n)B^{n-1}=E_n(B)$. When $k=0$, the target's pivot
contribution is zero and the same inequality holds because $E_n(B)$
counts choices with at least two pivots and is nonnegative.

A nonzero target has $\max y\ge1$, so its pivot sum omits $p=1$,
where the zero target has a strictly positive contribution $E_n(M)$
for $n\ge2$, $M\ge1$. For example, choosing two specified entries
equal to one and every other entry zero is one counted choice. The
identity-branch contribution of every target is at most the zero
target's one. Summing the termwise inequalities and the omitted strict
term proves strict superiority of $0^n$. ∎

## 7. Limits, source subtraction and proof-pressure targets

No claim of literature novelty, accepted review, manuscript completion or
global source clearance follows from these deductions. The primitive
division algorithm, weak-majorization notation, elementary binomial
counting and support termination receive zero standalone credit.

SPR is not assumed to preserve gcd: for example
$(2,3,5)\mapsto(2,0,2)\mapsto(0,0,0)$, although the original gcd is
one. This hand-derived example distinguishes the old gcd-preserving
cyclic least-positive remainder rule, not every possible old algorithm.

The planned bounded exact pilot must test the literal in two independent
representations, fixed/support structure, all inequalities (3) applicable
inside its box, the sharp maximum (4), the entire target fibre formula
(5) including empty fibres, and uniqueness and size (6). No finite
experiment establishes the quantified lemmas above. No larger box is
authorized if any result fails; failures stay visible and the contract
must be downgraded or closed, not silently repaired after the fact.
