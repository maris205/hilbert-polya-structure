# Proof package — transitive-triple support reversal

Author/proof contributor: /root/round211_rational_scout.
No independent acceptance is claimed.

## Claim and status

**PROVABLE AS STATED.** The literal rule is exactly TTRS in INTAKE.md.
For every $n\ge4$, put
$$q_n=2^{\binom n2},\qquad
a_n=n(n-1)2^{\binom{n-2}2}.$$
There are $q_n-a_n$ recurrent states, all of exact period two, and $a_n$
nonrecurrent states, all of exact depth one. One-step fibres have the
following complete histogram:
$$\#\{Y:|F^{-1}(Y)|=0\}=a_n,\quad
\#\{Y:|F^{-1}(Y)|=1\}=q_n-2a_n,\quad
\#\{Y:|F^{-1}(Y)|=2\}=a_n.$$
The two-source targets are precisely tournaments having both a global
source and a global sink. Their two predecessors are specified below.
Every assertion for $n=0,1,2,3$ is given separately in Step 7.

## Assumptions and notation

The entire labelled tournament carrier is used, not an isomorphism
quotient or a score-sequence slice. All support predicates use the old
state and an arc is reversed once if it qualifies.

Write $D(T)$ for reversal of every arc, $d_T^+(v)$ for outdegree, and
$T^{uv}$ for reversal of the single arc on $\{u,v\}$. Define $E(T)$ to
be the set of arcs belonging to no transitive induced triple; call them
protected arcs. Define
$$A_n=\{T:E(T)\ne\varnothing\},\qquad
C_n=\mathcal T_n\setminus A_n,$$
and let $B_n$ consist of tournaments with a global source and a global
sink. A global source points to every other vertex; a global sink receives
an arc from every other vertex. For $n\ge2$ either, if it exists, is unique:
two sources or two sinks would require opposite directions on their pair.

Depth $\tau(T)$ is the least nonnegative time at which the orbit is
periodic. A functional-graph arrow is the literal transition $T\mapsto F(T)$.

## Proof strategy and dependencies

Directly classify the protected-arc predicate, then factor the literal map
through a one-arc repair and whole reversal. This is a proof device, not a
changed update rule. No external theorem or finite enumeration is a premise.

1. The protected-arc criterion implies uniqueness when $n\ge4$.
2. Uniqueness gives a one-arc repair and the image normal form.
3. The repair/reversal identities give the exact temporal graph.
4. Reconstruction from the normal form gives every inverse set.
5. Label choices and free residual arcs give all counts.
6. Small carriers are handled directly, outside the uniqueness argument.

## Proof

### Step 1. Exact criterion for a protected arc

Fix an arc $u\to v$ and a third vertex $w$. A tournament on three
vertices is either transitive or a directed cycle. The triple containing
$u\to v$ is a directed cycle exactly when $v\to w$ and $w\to u$.
Consequently, for $n\ge3$,
$$u\to v\in E(T)
\quad\Longleftrightarrow\quad
v\to w\to u\quad\hbox{for every }w\notin\{u,v\}. \tag{1}$$
Such an arc has $d_T^+(u)=1$ and $d_T^+(v)=n-2$.

For $n\ge4$, at most one protected arc can exist. Suppose $u\to v$ is
protected. No other protected arc can have tail $u$, whose only outgoing
arc is $u\to v$. Its tail cannot be $v$, since $d_T^+(v)=n-2\ge2$,
whereas every protected tail has outdegree one. If its tail is
$x\notin\{u,v\}$, (1) gives $x\to u$; outdegree one then forces its
head to be $u$. But a protected head has outdegree $n-2$, whereas
$d_T^+(u)=1$. This is a contradiction.

Conversely, choose an ordered pair of distinct labels $u,v$, orient
$u\to v$ and $v\to w\to u$ for every remaining $w$, and orient the
remaining induced tournament arbitrarily. Equation (1) gives the protected
arc $u\to v$, and the uniqueness just proved shows there is no other.
Each state of $A_n$ therefore has exactly one such presentation.

### Step 2. One-arc normalization

For $n\ge4$ define
$$N(T)=
\begin{cases}
T,&E(T)=\varnothing,\\
T^{uv},&E(T)=\{u\to v\}.
\end{cases} \tag{2}$$
In the second case, (1) shows that $v$ is a global source of $N(T)$
and $u$ is a global sink. In particular $N(A_n)\subseteq B_n$.

A tournament on at least three vertices with global source $s$ has no
protected arc. For an arc not incident with $s$, adjoining $s$ gives a
transitive triple. For an arc $s\to x$, choose any third vertex $w$:
$s$ points to both $x,w$, again giving a transitive triple. Thus
$B_n\subseteq C_n$, and (2) implies $N(\mathcal T_n)\subseteq C_n$.
As $N$ is the identity on $C_n$, it follows that
$$N^2=N,\qquad \operatorname{im}N=C_n. \tag{3}$$

Whole reversal preserves whether a triple is transitive and reverses the
orientation of a protected arc without changing its unordered endpoints.
It follows from (2), separately on $A_n$ and $C_n$, that
$$ND=DN,\qquad D^2=I. \tag{4}$$

### Step 3. Exact dynamics

The literal map reverses all arcs except the protected ones. If there is
no protected arc, it is $D$. If there is a unique protected arc, applying
$N$ and then $D$ reverses that arc twice and every other arc once.
Therefore
$$F=DN,\qquad F^2=N,\qquad F^3=F. \tag{5}$$
In particular $\operatorname{im}F=C_n$, and $F$ restricts there to $D$.
For $n\ge4$, every tournament has an arc, and reversing it changes the
labelled tournament; hence $D$ has no fixed state. All states of $C_n$
have exact period two. Every state of $A_n$ maps into $C_n$ in one step
and is itself outside the image, so has exact depth one.

Both classes occur: a transitive tournament lies in $C_n$, and the
construction in Step 1 gives a state of $A_n$ for every $n\ge4$.
Thus the uniform entrance bound one is sharp. Formula (5) also yields,
for every $r\ge1$, $F^{2r}=N$ and $F^{2r+1}=F$.

### Step 4. All targets and all one-step predecessors

Let $n\ge4$ and fix any target $Y$.

If $Y\in A_n$, there is no predecessor since the image is $C_n$.
Suppose $Y\in C_n$. A predecessor in $C_n$ must be $D(Y)$, and this
is indeed a predecessor because $C_n$ is stable under $D$.

An exceptional predecessor $X\in A_n$ with protected arc $u\to v$
maps to a tournament with global source $u$ and global sink $v$:
the old relations $v\to w\to u$ are reversed, while $u\to v$ is kept.
Therefore such a predecessor requires $Y\in B_n$, and its protected
endpoints are uniquely determined by the target's source and sink.

Conversely, if $Y$ has source $s$ and sink $t$, form
$$X=D(Y)^{st}. \tag{6}$$
For every remaining vertex $w$, this state has
$t\to w\to s$ and $s\to t$. Thus $s\to t$ is protected by (1);
Step 1 makes it the only protected arc, and the literal update returns
$Y$. It differs from the ordinary predecessor $D(Y)$ on exactly the
pair $\{s,t\}$. There can be no other predecessor by the two cases above.
We have proved the explicit disjoint source-set formula
$$F^{-1}(Y)=
\begin{cases}
\varnothing,&Y\in A_n,\\
\{D(Y)\},&Y\in C_n\setminus B_n,\\
\{D(Y),D(Y)^{st}\},&Y\in B_n,\ s\text{ source},\ t\text{ sink}.
\end{cases} \tag{7}$$
This is an explicit reconstruction, not an implicit constraint on an
unknown source. In particular the maximum fibre is two and all maximizers
are exactly $B_n$.

### Step 5. Counts, image and depth distribution

There are $q_n$ tournaments because the $\binom n2$ pair orientations
are independent. The unique presentation in Step 1 gives
$$|A_n|=n(n-1)2^{\binom{n-2}2}=a_n. \tag{8}$$
For $B_n$, choose its unique ordered source/sink pair and orient the
remaining induced tournament freely. Every arc touching either chosen
endpoint is forced. This gives $|B_n|=a_n$. Since $A_n$ and $B_n$ are
disjoint, the three classes in (7) have sizes $a_n,q_n-2a_n,a_n$.
The fibre histogram in the claim follows, together with
$$|\operatorname{im}F|=|\operatorname{Rec}F|=q_n-a_n,\qquad
\sum_{T\in\mathcal T_n}z^{\tau(T)}=(q_n-a_n)+a_nz. \tag{9}$$
The fibre sum is $(q_n-2a_n)+2a_n=q_n$, consistent with the whole
carrier, but this arithmetic check is not used to replace the inverse proof.

### Step 6. Every connected functional-graph component

Whole reversal interchanges the source and sink of a state in $B_n$, so
$B_n$ is $D$-invariant. Each of its $a_n/2$ two-cycles has exactly one
nonrecurrent incoming leaf at each cycle vertex, by (7). Each remaining
two-cycle has no such leaf. Thus the full graph consists of
$$a_n/2\ \text{two-cycles with one leaf at each cycle vertex},$$
and
$$(q_n-2a_n)/2\ \text{bare two-cycles}.$$
There are no deeper trees by Step 3. These are labelled states and cycles,
not counts modulo relabelling.

### Step 7. All small-size boundaries

For $n=0$ and $n=1$ the sole tournament is fixed, and its fibre has size
one. For $n=2$ the two tournaments are both fixed, with singleton fibres,
because there is no triple.

For $n=3$, exactly two tournaments are directed cycles; their unique
triple is not transitive, so neither changes. The other six are transitive;
their three arcs all reverse, pairing them into three two-cycles.
Thus every state is recurrent, every fibre has size one, and maximum
depth is zero. In this case each directed cycle has three protected arcs,
so the uniqueness argument and the definition (2) are not extended to it.
The expressions $a_n$ and (7)--(9) were asserted only for $n\ge4$.
This completes every case of the stated claim. ∎

## Corrections or missing assumptions

No hidden fixed-score or unlabeled restriction is used. The original TTRS
rule is unchanged by the proof device $N$. The $n=3$ exception is essential:
one cannot repair “the unique protected arc” on a directed triangle.

## Open risks and value boundary

This is an author deduction without an independent proof review or pilot.
The source search is bounded and does not establish novelty or priority.
Even accepting every theorem above, the temporal and inverse classifications
both come from repairing the same one exceptional arc and then applying a
standard involution. The result therefore closes NO_PROMOTION on value,
rather than claiming the literal is identical to cyclic-triangle reversal.

