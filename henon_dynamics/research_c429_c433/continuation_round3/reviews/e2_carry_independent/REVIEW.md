# Independent proof challenge: cyclic carry stabilization for PC424-L

2026-09-09 UTC. Internal nonauthor proof work by
`/root/c429_e2_wild_witt_review`, under the current-session setting.
This is not external-model review, human peer review, or paper admission.

## Claim

Let $p$ be odd, $k=\overline{\mathbb F}_p$, $c\in k$, and

$$
R_n=k[X_i:i\in\mathbb Z/n\mathbb Z]/(X_i^2+c-X_{i+1}),
\qquad P_n=\prod_{i=0}^{n-1}X_i.
$$

For

$$
v(x)=a_0+\sum_{\substack{1\le d\le D\\d\text{ odd}}}a_dx^d,
\qquad D\ge1\text{ odd},\quad a_D\ne0,
$$

put $m=\lfloor\log_2D\rfloor$, let $E\subseteq\{0,\ldots,m\}$
be the binary support of $D$, and write $X^E=\prod_{j\in E}X_j$.
Coefficients below refer to the squarefree basis of the **full** algebra
$R_n$, not its reduced quotient. Define

$$
H_n(v)=\sum_{i=0}^{n-1}v(X_i),\qquad
C_n=[X^E]\bigl(P_nH_n(v)\bigr).
$$

The proposed assertion is that $C_n$ is independent of $n$ for every
$n\ge3m+4$. The requested further check is whether it combines with
the previously proved coefficient and Jacobian identities to settle
the original ordinary-cycle PC424-L statement.

## Status

**PROVABLE AS STATED. ZERO OPEN MATHEMATICAL MUST-FIXES in the carry
stabilization argument and its stated PC424-L implication.**

The proof below constructs an exact, weight-preserving insertion/deletion
bijection. It includes all lower odd exponents, the constant term,
$m=0$, carry extinction on the final step, and cyclic wraparound.
No genericity, nonzero-weight, reducedness, or prime-to-$p$ period
hypothesis is used.

The original all-odd-prime/all-parameter PC424-L equality follows from
this new lemma and the matched frozen inputs. This is a mathematical
proof conclusion, not an integration decision, literature-novelty
certification, independent paper count, or target-arithmetic upgrade.

## Assumptions and source discipline

The coordinator supplied A1's proposed carry mechanism and the precise
stabilization target. I derived the expansion, source localization, and
bijection independently before reading the frozen interfaces. I did not
inspect A1's current author proof or the pending E8 review.

Accepted earlier material, actually read for hypothesis matching:

1. [Original PC424-L normal-form package](../../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md),
   Step 4: $k[x]=B_c\oplus(k\oplus xk[x^2])$.
2. [Frozen R2 scheme-level package](../../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md),
   Steps 1--2: the full cyclic algebra, squarefree basis, and
   $[X^E]H_n(v)=a_D$ for $n>2m$.
3. The same package, Steps 3 and 5: ordinary-cycle vanishing implies
   radical divisibility and hence $J_nH_n(v)=0$, where
   $J_n=2^nP_n-1$. Its documented failure of the **converse at one
   level** is preserved; that converse is not used.

These old lemmas are subtracted, not presented as new discoveries.
The new bridge is stabilization of the full-product coefficient, which
allows comparison of two adjacent levels. No root-multiplicity estimate,
external dynamical regularity theorem, finite algebraic transfer,
or assumption about a functional detecting the reduced quotient is used.

## Notation

A source is the index $i$ of a summand $P_nX_i^d$.
For its reduction, write sites in the order

$$
i, i+1, \ldots, i+n-1\pmod n.
$$

The integer $t_r$ is the extra exponent arriving at site $i+r$;
$t_0=d$. For an integer $t\ge0$, define

$$
q(t)=\left\lfloor\frac{1+t}{2}\right\rfloor,
\qquad b(t)=(1+t)\bmod2.
$$

A carry transition $t\longrightarrow t'$ is allowed when
$0\le t'\le q(t)$ and has polynomial weight

$$
\omega(t,t')=\binom{q(t)}{t'}(-c)^{q(t)-t'}.
$$

Weights are interpreted in $k$. A zero weight is still part of the
formal expansion; the argument does not discard it or divide by it.

## Proof strategy and dependency map

1. Produce a complete squarefree expansion of each $P_nX_i^d$ in one
   cyclic pass, and prove that wraparound creates no unresolved square.
2. Bound the carry after $m+1$ transitions and classify every source
   capable of producing a fixed nonempty target inside $[0,m]$.
3. Find one zero-output site with forced transition $1\to1$ for every
   contributing path.
4. Insert or delete that site to match all contributing weighted paths
   at adjacent periods.
5. Apply the two frozen full-algebra identities. Their adjacent-level
   comparison contradicts a nonzero highest odd coefficient.

The proof temporarily allows **any nonempty** $E\subseteq[0,m]$ as
an internal strengthening of the stabilization lemma. Only the final
PC424-L step requires $E$ to be the binary support of $D$.

## Proof

### 1. Exact local expansion and termination after one pass

At a site whose exponent is $1+t$, its defining relation gives

$$
X_{i+r}^{1+t}
=X_{i+r}^{b(t)}(X_{i+r+1}-c)^{q(t)}
=\sum_{t'=0}^{q(t)}
  \omega(t,t')X_{i+r}^{b(t)}X_{i+r+1}^{t'}.
\tag{1}
$$

Before the final transition, the next site still has its factor of
exponent one from $P_n$. Thus (1), applied successively in the specified
order, gives precisely the transition rule above. All unprocessed sites
retain that baseline exponent one. The final transition returns to the
already processed source and is treated separately below.

Since $d$ is odd, the first source exponent $1+d$ is even, and its
first-pass output is $b(d)=0$. A complete path is therefore a sequence

$$
t_0=d,t_1,\ldots,t_n,
\qquad 0\le t_{r+1}\le q(t_r)\quad(0\le r<n).
\tag{2}
$$

For every such path,

$$
t_r\le\left\lceil\frac{d}{2^r}\right\rceil,
\qquad t_{m+1}\le1,
\tag{3}
$$

because $q(t)=\lceil t/2\rceil$, iterated ceiling division by two
equals ceiling division by the corresponding power of two, and
$d\le D<2^{m+1}$. Once a carry is at most one, it remains at most one.

Our period bound implies $n\ge m+1$, so the final carry satisfies
$t_n\le1$. It returns to the source, whose exponent was cleared at
the first step. Consequently the final source exponent is just $t_n$,
and no second cyclic pass is needed. Every other site has already
been reduced and is not revisited.

The output bits and path weight are exactly

$$
e_i=t_n,\qquad
e_{i+r}=b(t_r)\ (1\le r<n),\qquad
W(t_\bullet)=\prod_{r=0}^{n-1}\omega(t_r,t_{r+1}).
\tag{4}
$$

Repeated use of polynomial identity (1) proves that summing (4) over
all paths is the full expansion of $P_nX_i^d$. All outputs are
squarefree; uniqueness of the squarefree basis makes their collected
coefficients the coefficients in $R_n$. This does not assume the
algebra is reduced.

### 2. All contributing sources lie in one short cyclic interval

Fix a nonempty target $E\subseteq[0,m]$, and consider any path whose
output support is exactly $E$. Since $n-1\ge m+1$, (3) gives
$t_{n-1}\le1$. There are three exhaustive cases.

**Case A: $t_n=1$.** By (4), the source is in the target:
$i\in E\subseteq[0,m]$.

**Case B: $t_n=0$ and $t_{n-1}=0$.** At the predecessor of the source,
$e_{i-1}=b(0)=1$. Hence $i-1\in E$ and
$i\in E+1\subseteq[1,m+1]$ modulo $n$.

**Case C: $t_n=0$ and $t_{n-1}=1$.** On the whole tail
$m+1\le r\le n-1$, carries belong to $\{0,1\}$ and cannot
increase. Thus all of them must equal one. Every tail output is zero,
and the final source output is zero. The nonempty target is therefore
contained in

$$
\{i+1,\ldots,i+m\}\pmod n.
$$

If $m=0$, this set is empty, so Case C cannot contribute. If $m\ge1$,
choose a target element $e$ and a corresponding $r\in[1,m]$ with
$e\equiv i+r$. Then $i\equiv e-r\in[-m,m-1]$.

Together, all contributing source residues have unique representatives
in

$$
I_m=[-m,m+1]\cap\mathbb Z.
\tag{5}
$$

Uniqueness follows since the interval contains $2m+2<n$ integers.
The final-step extinction in Case C is necessary: omitting it would
incorrectly assert that every source or predecessor belongs to $E$.

### 3. A common insertion site has forced weight one

Set

$$
j=2m+2.
$$

Let $s\in I_m$ be the signed representative of a contributing source.
The forward distance from that source to site $j$ is the integer

$$
r=j-s,\qquad
m+1\le r\le3m+2\le n-2.
\tag{6}
$$

For a negative representative $s$, this distance passes through the
cyclic wrap once; (6) is still the actual distance, since it is
positive and smaller than $n$. Both $j$ and $j+1$ therefore occur
after the initial transient and before the final return to the source.
They are distinct from the source.

Both sites lie outside $E$, so (4) gives $b(t_r)=b(t_{r+1})=0$.
By (3), these two carries belong to $\{0,1\}$; the sole value in
that set with zero output is one. Thus the transition at site $j$ is

$$
t_r=t_{r+1}=1,\qquad \omega(1,1)=1.
\tag{7}
$$

This works uniformly for all contributing sources and every lower odd
$d\le D$. It also works at the smallest allowed values $m=0,n=4$.

### 4. Exact insertion and deletion at adjacent periods

Compare periods $n$ and $n+1$, with $n\ge3m+4$. Insert a new site
with label $j$ immediately before the old site $j$. Identify the old
labels with the new ones by

$$
\phi(a)=
\begin{cases}
a,&0\le a<j,\\
a+1,&j\le a<n.
\end{cases}
\tag{8}
$$

This preserves the cyclic order and fixes every target label in $E$.
It maps each possible signed source $s\in I_m$ to the source with
the same signed representative at the new period: nonnegative sources
are below $j$, and negative ones have old labels at least
$n-m\ge2m+4>j$.

Take any path contributing to $[X^E](P_nX_i^d)$. By (7), the carry
entering old site $j$ is one. Insert an extra transition $1\to1$
at the new site. It outputs zero and has weight one. Keep every old
transition and the source degree $d$ unchanged. The resulting path
at period $n+1$ is allowed, has the same target support $E$, and has
exactly the same weight. The source's initial clearing and final
return carry are unchanged.

Conversely, take any contributing path at period $n+1$. Localization
and (7), now applied at period $n+1$, show that site $j$ is not its
source and has transition $1\to1$ of weight one. Delete that site
and relabel the others by the inverse of (8). The adjacent carries
are both one, so concatenation is an allowed path at period $n$.
The output remains $E$ and the weight is unchanged.

Insertion and deletion are inverse operations. They match **all**
contributing paths, including zero-weight paths, and do not use a
cancellation argument. Sources outside (5) contribute no paths at
either period. Therefore, for every allowed odd $d$,

$$
\sum_{i\bmod n}[X^E](P_nX_i^d)
=\sum_{i\bmod(n+1)}[X^E](P_{n+1}X_i^d).
\tag{9}
$$

The constant part of $P_nH_n(v)$ is $na_0P_n$. Since
$E\subseteq[0,m]$ and $n>m+1$, its coefficient at $X^E$ is zero.
This remains true at period $n+1$, irrespective of the value of $n$
as a scalar in $k$.

Multiply (9) by each $a_d$ and sum. The result is $C_n=C_{n+1}$.
Induction proves stabilization for every $n\ge3m+4$.

### 5. Explicit smallest-degree boundary check, by hand only

For $D=1$, $m=0$, and $E=\{0\}$, the only possible sources are
$0$ and $1$. For source $0$, the final source bit must be one,
forcing every carry to be one; its weight is $1$.

For source $1$, the source bit is zero. The carry must stay one
through all zero-output sites, die at site $n-1$ with transition
$1\to0$ of weight $-c$, and then give the sole output one at
site $0$. Its weight is $-c$. Thus the proof yields

$$
C_n=a_1(1-c)\qquad(n\ge4),
$$

with no constant-term contribution. This is a direct symbolic boundary
check, not a mathematical-program execution or a finite-sample proof.

### 6. The exact PC424-L consequence

Let $f_c(x)=x^2+c$. Write $K_c$ for polynomials with zero sums on
every ordinary primitive periodic orbit, counting each point once,
and $B_c=\{Q\circ f_c-Q:Q\in k[x]\}$. Suppose $h\in K_c$. Use the
accepted normal form $h=Q\circ f_c-Q+v$ with
$v\in k\oplus xk[x^2]$. Telescoping shows that $v$ has the same
ordinary-cycle vanishing.

If $v$ is constant, a fixed point exists because $k$ is algebraically
closed and $x^2-x+c$ has a root. Its primitive orbit sum is $v$,
so $v=0$.

Suppose instead that $v$ has positive odd leading degree $D$ and
$a_D\ne0$. Every root $a$ of $F_n=f_c^{\circ n}-x$ has a primitive
period $r\mid n$, so

$$
H_n(v)(a)=(n/r)\,S_v(O_a)=0.
$$

This uses multiplication by the integer $n/r$, not division in $k$.
At a root of multiplicity $e$, the derivative $F_n'$ has order at
least $e-1$ even when $p\mid e$. Therefore

$$
F_n\mid F_n'H_n(v).
\tag{10}
$$

Under the accepted isomorphism $R_n\simeq k[x]/(F_n)$, the chain
rule identifies $F_n'$ with $2^nP_n-1$. Consequently (10) gives

$$
(2^nP_n-1)H_n(v)=0\quad\text{in }R_n
\tag{11}
$$

for every $n$. The frozen binary-support lemma gives
$[X^E]H_n(v)=a_D$ for $n>2m$. Taking this coefficient in (11), for
every $n\ge3m+4$, yields

$$
2^nC_n=a_D.
\tag{12}
$$

Our proved stabilization gives $C_{n+1}=C_n$. The same equation at
the next level thus reads

$$
a_D=2^{n+1}C_{n+1}=2\,(2^nC_n)=2a_D.
$$

Subtracting gives $a_D=0$, a contradiction. No division by $n$,
a root multiplicity, or an orbit length occurs. Adjacent periods are
both covered by the original all-period hypothesis.

Therefore $v=0$, and $h=Q\circ f_c-Q$. The converse follows by
telescoping on each primitive orbit. This proves the original equality

$$
K_c=B_c
\quad\text{for every odd prime }p
\text{ and every }c\in\overline{\mathbb F}_p.
$$

The previous single-level counterexample to the converse of (10) is
unaffected. The proof needs only its necessary direction and excludes
simultaneous annihilation for one nonzero normal representative at two
sufficiently large adjacent levels. $\square$

## Corrections or missing assumptions

None is required for the stated stabilization bound. The phrase
“source output initially zero” must refer to the first processing of
the source: its **final** bit is $t_n$, not always zero. The proof above
makes this distinction explicit and retains the final-step extinction
case. These are precision requirements in a complete presentation,
not counterexamples to the proposed mechanism.

## Open risks, ownership, and execution record

- No unresolved mathematical gap was found in this specific proof or
  in its use of the three frozen interfaces actually read here.
- The carry idea was supplied as A1's proposal through the coordinator;
  this report supplies an independent derivation/challenge, not a claim
  of independent authorship of that idea.
- No current A1 author manuscript, pending E8 review, or other new
  reviewer conclusion was read. This report is not a substitute for
  the separate whole-author/source review or coordinator adjudication.
- No new literature search or external theorem is invoked. This is not
  a novelty certificate or a claim that the complete source audit is
  finished.
- The proof-writer exact-claim and boundary-case requirements governed
  the structure. The repository workflow's current-team internal review
  mode supersedes older external-model examples in research-review.
- Mathematical executions: **zero**. No old diagnostic was rerun;
  no new mathematical program, external model/API, Git operation,
  shared-state edit, manuscript/PDF, formal evaluation, or child agent.
- The only write is this assigned review file. Original PC424-D and
  other lanes are outside this claim; no target Euler factor, root
  number, automorphy, zero correspondence, or Hilbert--Pólya conclusion.

**CARRY_STABILIZATION_PROVED; PC424_L_MATHEMATICAL_IMPLICATION_VERIFIED;
ZERO_OPEN_MUST_FIXES; NO_BAD_EULER_OR_ROOT_NUMBER.**
