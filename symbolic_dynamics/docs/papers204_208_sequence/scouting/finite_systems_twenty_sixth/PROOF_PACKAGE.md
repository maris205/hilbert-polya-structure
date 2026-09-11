# Proof package and subtraction boundary

Author: `/root/twenty_sixth_finite_scout`. No independent review claimed.
All literal assumptions and carriers are in INTAKE.md.

## Claim and status

**PROVABLE AS STATED:** ASC's exact full-carrier linearization and consequent
generic temporal/inverse formulas; EMD's closure, fixed states, two-pile
doubling factor and full one-step inverse decoder; UTR's literal identity
with the old rule. **NOT CURRENTLY JUSTIFIED:** a fresh two-axis admission
contract for any of the three. ASC's temporal mechanism is consumed, EMD's
full recurrent/temporal classification is missing, and UTR is an exact
historical duplicate with no new theorem.

Dependency map: transpose decomposition -> fixed linear strata -> stable
image and affine-kernel fibres; extremal mass transfer -> two-entry multiset
cancellation -> fixed criterion and inverse decoder. No finite census is a
premise of any argument.

## 1. ASC: the entire dynamics is fixed-stratum linear

Write $A=S+K$, where $S=(A+A^{\mathsf T})/2$ is symmetric and
$K=(A-A^{\mathsf T})/2$ is skew-symmetric. This is a bijection from the
entire matrix carrier to $\operatorname{Sym}_n\times\operatorname{Skew}_n$,
with inverse $(S,K)\mapsto S+K$. Odd characteristic is essential here.
Expansion gives

$$[A,A^{\mathsf T}]=[S+K,S-K]=2[K,S].$$

Since $[K,S]^{\mathsf T}=[K,S]$, the skew part is unchanged. Define the
linear endomorphism $L_K(S)=S+2[K,S]$ of $\operatorname{Sym}_n$.
Thus the displayed bijection is a genuine one-step dynamical conjugacy to

$$(S,K)\longmapsto(L_KS,K),\qquad T^t(S+K)=L_K^tS+K.$$

This is not a claimed conjugacy to one universal matrix independent of
$K$, nor merely a first-image factor. Every initial state is covered.

Put $d=n(n+1)/2$. For any linear map $L$ on a $d$-dimensional space,
the descending image chain stabilizes by step $d$. Hence $L$ maps
$W=\operatorname{im}L^d$ bijectively to itself. Every point of $W$ is
periodic because the field is finite. Conversely, a periodic point belongs
to every image and therefore to $W$. Applied to $L_K$, this proves

$$\operatorname{Rec}(T)=\{S+K:S\in\operatorname{im}L_K^d\},\qquad
\tau(S+K)=\min\{t\ge0:L_K^tS\in\operatorname{im}L_K^d\}\le d.$$

No sharpness of $d$ is claimed. Periods on each stable image are the usual
periods of its invertible linear restriction; fixed points of its $r$th
power are $\ker(L_K^r-I)$. Summing their cardinalities over $K$ is a
standard linear-system expression, not an evaluated new all-$q,n$ census.

For arbitrary target $Y=H+K$, $H$ symmetric, and $t\ge0$, all sources
must have that exact skew part $K$. The source set is precisely

$$\{S+K:L_K^tS=H\}.$$

It is empty unless $H\in\operatorname{im}L_K^t$, and otherwise an affine
coset of $\ker L_K^t$, of size $q^{\dim\ker L_K^t}$. Indeed subtracting
two solutions gives the kernel, and adding any kernel element preserves a
solution. At $t=0$ the formula gives the unique target itself. At $n=1$
the skew space is zero and $L=I$, so every state is fixed with unit fibres.

These are complete structural formulas but the whole temporal mechanism
and affine-kernel decoder are generic finite linear dynamics. No new sharp
global inverse extremum is evaluated. Even such an extremum would not undo
the consumed temporal axis. ASC is **KILL_FIXED_STRATUM_LINEARIZATION**.

## 2. EMD: real coupling, partial temporal result, full local inverse

### 2.1 Closure, fixed points and energy obstruction

For at least two parts, $m\ge1$, $M\ge m$, and
$2m+(M-m)=M+m$, proving mass preservation and carrier closure.
If $M=m$, exactly one positive part disappears, so such a state is not
fixed. If $M>m$, cancellation of all untouched multiplicities in a proposed
fixed state gives $\{m,M\}=\{2m,M-m\}$. Since $2m\ne m$, this holds
exactly when $M=2m$. Thus, in addition to the empty and one-part states,
the fixed states are exactly those whose largest part is twice the smallest.

The sum of squares changes by $2m(2m-M)$, which can have either sign.
This is not old unit majorization with its stopping condition. For example,

$$\{1,4\}\mapsto\{2,3\}\mapsto\{1,4\},\qquad
\{1,2,4\}\mapsto\{2,2,3\}\mapsto\{1,2,4\}.$$

All four arrows follow by substituting the displayed extrema. They are
deductive witnesses, not an enumerated small box. In particular a proof
that every state becomes fixed would be false, including beyond two piles.

### 2.2 Exact two-pile subtraction

Let $X_N$ be partitions of $N$ into at most two parts, with a zero allowed
only as notation for the singleton. The map from $\mathbb Z/N\mathbb Z$
to $X_N$ taking the representative $0\le a<N$ to the unordered pair
$\{a,N-a\}$, omitting any zero, identifies residues exactly up to sign.
For the representative $0\le a\le N/2$, the next pair is
$\{2a,N-2a\}$. Thus on this entire invariant subcarrier EMD is exactly
residue doubling modulo the sign quotient. $N=0$ is separately the empty
fixed state. This is a deduced elementary doubling/tent mechanism, not a
classification of partitions with three or more parts.

### 2.3 Full one-step inverse decoder

Fix a target multiset $\mu$ of positive parts. For each distinct even value
$v$ occurring in $\mu$, put $a=v/2$. Choose a numerical value $u\ge0$:
either $u=0$, or $u$ occurs in $\mu$. For $u>0$, require that the multiset
contains the two occurrences $u,v$ (two copies if $u=v$). Remove those
occurrences; for $u=0$ remove only $v$. Call the residual multiset $R$.
The pair $(u,v)$ is admissible exactly when every part of $R$ lies in
$[a,u+a]$. It produces the source

$$R\uplus\{a,u+a\}.$$

Also include $\mu$ itself when it has zero or one part. These and only
these are the predecessors. Necessity: an updated source has $v=2m$,
$u=M-m$, and every untouched part lies between $m$ and $M$.
Sufficiency: in the reconstructed source the extrema are exactly $a$ and
$u+a$, so the literal rule recovers $\mu$. If $u=0$, the condition forces
all remaining parts to equal $a$, handling all-equal sources and lost zeros.
If two admissible numerical pairs produced the same source, its minimum
and maximum would recover $v=2m$ and $u=M-m$, so the pairs would coincide.
Indistinguishable equal occurrences are not counted several times.
The additional zero/one-part fixed source has smaller length than every
updated source producing it, so there is no overlap.

This gives a finite target-local cardinality by counting admissible
numerical pairs. It is elementary inversion of the two updated entries and
the extremal scheduler, not a solved sharp all-target maximum. The fixed
classification and two-pile factor do not close the missing all-$N$
recurrent structure. Status: **HOLD_PROOF_SOURCE / NO_PROMOTION**.

## 3. UTR exact duplicate

The original T01_UTR row in the P172–P176 combinatorial cross-domain ledger
uses exactly the same labelled tournaments, old-snapshot unique-directed-
triangle predicate and simultaneous reversal. The identity on every
labelled carrier intertwines the maps. No parameter extension, new cycle
claim or source-body interpretation is needed to establish this collision.
Its old pilot observations are not rerun or promoted into all-size facts.
Status: **KILL_LITERAL_INTERNAL**.

## Open risks and final disposition

No full EMD temporal/recurrent theorem or direct-owner clearance has been
obtained. ASC is not rescued by an unevaluated rank formula, and UTR is not
new. Consequently none is proposed for a candidate gate. These are author
deductions with disclosed classical subtraction, not proof of global
novelty, independent acceptance or the impossibility of future research.
