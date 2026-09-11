# ECA108: two-step projection and generic inverse subtraction

Author: `/root/thirty_third_finite_scout`, 2026-09-07 UTC.
These are author deductions, not independent review or a candidate gate.
Disposition: `KILL_VALUE_KNOWN_ECA_GENERIC_INVERSE / NO_PROMOTION`.

## Claim, status and assumptions

Status of the mathematical deductions below: **PROVABLE AS STATED**.
Status of a materially separate two-axis research contribution:
**NOT CURRENTLY JUSTIFIED**.

For every integer $n\ge1$, let $X_n=\{0,1\}^{\mathbb Z/n\mathbb Z}$,
with labelled sites and simultaneous updates from the old configuration.
All indices below are taken modulo $n$, including when several offsets
coincide. Define exactly one comparison literal

$$F(x)_i=x_i\oplus(x_{i-1}x_{i+1}),$$

where $\oplus$ denotes addition in $\mathbb F_2$. Its outputs at the
ordered inputs $111,110,101,100,011,010,001,000$ are
$0,1,1,0,1,1,0,0$. Thus this is literally the standard ECA rule 108,
not a new rule, a restriction of the carrier or an asynchronous variant.
No program, pilot output or finite verification is a premise.

Put $G=F^2$. Then:

1. $G(x)\le x$ coordinatewise, $G^2=G$, and $F^4=F^2$.
2. $\operatorname{Rec}(F)=\operatorname{Fix}(G)=G(X_n)$, all labelled
   recurrent periods divide two, and the exact maximum entrance time is
   $H(1)=1$ and $H(n)=2$ for $n\ge2$.
3. Every target fibre is decoded, without multiplicity, by a four-state
   closed-path construction, with count
   $\operatorname{tr}(M_{y_0}\cdots M_{y_{n-1}})$ as specified below.

The first two points refine the known rule's short-period classification
by a direct calculation. No claim that the exact clock is globally new
or that the inspected primary explicitly prints this proof is made.
The third point is precisely the generic de Bruijn inverse construction;
no separate extremal theorem is claimed.

## Strategy and dependency map

1. Expand the literal twice in the Boolean ring; this gives a radius-two
   support-deleting map, without asserting that this map is order-preserving.
2. Check persistence of every retained coordinate by the four possible
   values at distance two. This proves idempotence on the entire carrier.
3. Use the idempotent-image identity and explicit all-size witnesses to
   obtain recurrence and the sharp entrance time.
4. Encode overlapping source pairs around the labelled target ring to
   give a bijective inverse decoder. This is a separate representation,
   but it is an already available generic method, not research novelty.

## 1. Exact two-step formula

At a site write $(d,a,b,c,e)=(x_{i-2},x_{i-1},x_i,x_{i+1},x_{i+2})$.
In the Boolean ring every variable satisfies $u^2=u$. The three values
after one step are $a\oplus db$, $b\oplus ac$, and $c\oplus be$.
Consequently

$$G(x)_i=(b\oplus ac)\oplus(a\oplus db)(c\oplus be)
       =b(1\oplus ae\oplus dc\oplus de). \tag{1}$$

This is an identity of Boolean variables, so it stays true when the
finite ring identifies any of the named offsets. In particular $b=0$
forces $G(x)_i=0$. This proves support deletion, not monotonicity in $x$.
For $b=1$, the conditions for retention in (1) are exactly:

| $(d,e)$ | Necessary and sufficient condition for $G(x)_i=1$ |
|---|---|
| $(0,0)$ | none |
| $(0,1)$ | $a=0$ |
| $(1,0)$ | $c=0$ |
| $(1,1)$ | $a\ne c$ |

## 2. Every retained one persists under $G$

Write $x'=G(x)$ and use primes on the local variables. If $b'=0$,
support deletion already gives $G(x')_i=0$. Suppose $b'=1$, so $b=1$.

If $d=e=0$, then $d'=e'=0$ and the first row of the table retains $b'$.
If $d=0,e=1$, retention implies $a=0$. Then $d'=a'=0$; either the
first row or the second row applies, and again $b'$ is retained.
If $d=1,e=0$, retention implies $c=0$. Then $e'=c'=0$ and either
the first or third row retains $b'$.

It remains to treat $d=e=1$ and $a\ne c$. First take $a=0,c=1$.
Let $g=x_{i+3}$ and $h=x_{i+4}$. Equation (1), applied at $i+1$
and $i+2$, gives

$$c'=1\oplus bg\oplus ae\oplus ag=1\oplus g,$$
$$e'=1\oplus ch\oplus bg\oplus bh=1\oplus g.$$

Thus $a'=0$ and $c'=e'$. If $d'=0$, the first or second table row
retains $b'$. If $d'=1,e'=0$, then $c'=0$ and the third row retains
$b'$. If $d'=e'=1$, then $a'=0,c'=1$ and the fourth row retains it.
For $a=1,c=0$, reflection of the labelled coordinates about site $i$
interchanges $a,c$ and $d,e$. Both the literal and (1) commute with
this reflection, since the neighbour product is symmetric. Applying
the proved case to the reflected configuration supplies the last case.

All cases prove $G^2(x)_i=G(x)_i$ for every site. Hence $G^2=G$ and
$F^4=F^2$. Coincident offsets in small rings only restrict which of
the cases can occur; the identities and the exhaustive cases remain valid.

## 3. Recurrent set and exact clock

Idempotence gives $G(X_n)=\operatorname{Fix}(G)$. On this set $F^2$
is the identity. It is invariant under $F$, because $F$ commutes with
its square. Thus every point in this set is recurrent with period one
or two, and every orbit reaches it by time two.

Conversely, if $x$ is recurrent, choose a positive multiple $t$ of its
period with $t\ge2$. Then $x=F^t(x)$ lies in $G(X_n)$, proving

$$\operatorname{Rec}(F)=G(X_n)=\{x:G(x)=x\}. \tag{2}$$

The radius-two table above is an explicit local criterion for (2).
Fixed points are exactly those $x$ for which no pair of sites at offsets
$i-1,i+1$ is simultaneously one, since $F(x)_i=x_i$ is equivalent
to $x_{i-1}x_{i+1}=0$. Every other point satisfying (2) has period two.
No separate count of either language is asserted.

For sharpness, at $n=1$ the literal is $F(b)=b\oplus b=0$, so the
source $1$ has entrance time one and $H(1)=1$.
For even $n\ge2$, take the cyclic alternating word $(10)^{n/2}$.
For odd $n\ge3$, take $11(01)^{(n-3)/2}0$. In both cases every zero
has two one-neighbours, and every one has at least one zero-neighbour.
Thus $F(x)=1^n$, while $F(1^n)=0^n$ and $0^n$ is fixed. Neither
$x$ nor $1^n$ equals $0^n$, so neither is recurrent: its orbit reaches
the fixed state without ever returning to the initial nonzero state.
The entrance time of $x$ is exactly two. This proves $H(n)=2$.

## 4. Full target inverse — generic closed paths

Order the pair states as $00,01,10,11$. For $s\in\{0,1\}$ put

$$M_0=\begin{pmatrix}
1&1&0&0\\0&0&0&0\\1&0&0&0\\0&0&0&1
\end{pmatrix},\qquad
M_1=\begin{pmatrix}
0&0&0&0\\0&0&1&1\\0&1&0&0\\0&0&1&0
\end{pmatrix}. \tag{3}$$

The entry from pair $(a,b)$ to pair $(b,c)$ is one in $M_s$ exactly
when $b\oplus ac=s$; all nonoverlapping pair transitions are zero.
This definition verifies every entry of (3) from the eight rule values.

Given a source $x$, put $v_i=(x_{i-1},x_i)$. Then $F(x)=y$ if and
only if $(v_0,v_1,\ldots,v_n=v_0)$ is a closed path whose $i$-th
edge is allowed by $M_{y_i}$. Conversely, a closed allowed path
recovers $x_i$ as the second component of $v_i$. Pair overlap and
closure ensure that its first component is $x_{i-1}$ at every site,
including the cyclic edge. This is a two-sided inverse between sources
and labelled closed paths, not paths modulo rotation. It also covers
$n=1$: a closed one-edge path forces its pair components to agree.

Expanding matrix multiplication and summing equal initial/final states
counts exactly those paths. Therefore, for all $n\ge1$ and $y\in X_n$,

$$|F^{-1}(y)|=\operatorname{tr}(M_{y_0}\cdots M_{y_{n-1}}). \tag{4}$$

The trace is zero exactly when the fibre is empty. No kernel was run,
no maximum over targets was evaluated, and no claim that such a maximum
is attained by a homogeneous target is made.

## Source subtraction, limitations and decision

Schüle–Stoop explicitly print the rule-108 polynomial and list this rule
in Proposition 8. Their displayed proof example is for rule 72, not
108. The proof above closes its own rule-specific steps and does not
pretend to recover an omitted source proof. The 2025 Donoso-Leiva et al.
paper identifies rule-108 walls and a constant parallel-cycle regime;
its sequential large-cycle theorem is not a theorem about this literal.

Powley–Stepney's Eq. (24) already supplies the arbitrary-target trace
construction, with the general proof attributed to an earlier source.
Section 4 above independently supplies the short closed-path proof and
deducts that entire inverse mechanism. Fukś's appendix gives conjectured
finite-block preimage sequences, not a proved full finite-ring inverse.
Those formulas are not used here.

The new local derivation is retained as a checked author argument, but
the literal is fully source-owned and its only completed inverse axis is
the standard transfer graph. No material second residual survives this
bounded check. A correct short clock for a known rule plus (4) does not
meet the batch's two-axis admission standard. This is a local negative,
not a theorem that all synchronous finite-alphabet rules are exhausted.
No admission, independent review, pilot, manuscript or follow-on lane is
authorized by this package.
