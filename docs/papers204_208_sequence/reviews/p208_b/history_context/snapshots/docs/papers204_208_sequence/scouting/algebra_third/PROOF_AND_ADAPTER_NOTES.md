# Third algebra intake: deductive subtraction, not an admission

Date: 2026-09-05 UTC. Author: algebra scout. These are author deductions
and source adapters, not an independent candidate or manuscript review.

## Claims, assumptions and status

The sought claim was an all-parameter temporal classification together
with a materially separate inverse or sharp-extremal mechanism. That
conjunction is `NOT CURRENTLY JUSTIFIED` for every one of the six maps.
The explicitly restricted deductions below are `PROVABLE AS STATED`.
No pilot observation is promoted to an all-parameter assertion.

Throughout, $p$ is prime, matrix size $n\geq1$, cyclic length $L\geq3$,
and $G$ is a finite group. Group products act rightmost first. Our
commutator is $[g,h]=ghg^{-1}h^{-1}$, not P119's displayed convention.
All carriers are full carriers, not a selected orbit or a post-hoc subset.

Dependency map: ST uses only a characteristic-two expansion; HN uses an
explicit polynomial inverse; EG uses normality of derived subgroups and
the orbit-stabilizer fibre of conjugation; RC uses coefficient comparison
and invertibility of $1,\ldots,p-1$; binary LV uses its eight-entry truth
table and maximal runs; ND uses telescoping and the fixed-coset lemma.

## ST: square plus transpose

Define $T(A)=A^2+A^{\mathsf T}$ on $M_n(\mathbb F_p)$.

1. In characteristic two, $(A+I)^2=A^2+I$, so $T(A+I)=T(A)$.
   Translation by $I$ is fixed-point-free for $n\geq1$; hence each
   nonempty fibre has even cardinality.
2. Also in characteristic two,
   $\operatorname{tr}(A^2)=\operatorname{tr}(A)^2$: off-diagonal
   products occur in cancelling pairs. For $p=2$, every image has trace
   zero. Neither assertion identifies the complete image.
3. The symmetric subspace is invariant, and there the update is the
   polynomial functional-calculus map $A\mapsto A^2+A$. This restricted
   primitive gets zero credit. No such reduction was proved for the full
   matrix carrier, because transpose and multiplication do not commute
   in general.

The actual $n=3,p=3$ graph has height $25$, core $663$, and periods
$1,2,3,4,6,8,12$. No all-size clock or independent full inverse mechanism
was found. P127's parity-transpose map is not the literal update: it has
an outer-product correction and its all-size height is one. The distinction
does not provide positive value evidence. `NO_PROMOTION`.

## HN: a standard Hénon automorphism

Define $H(x,y)=(y,y^2-x)$ on $\mathbb F_p^2$.
For every commutative ring the formula
$H^{-1}(u,v)=(u^2-v,u)$ is a two-sided inverse, as direct substitution
in both orders gives the identity. Thus all finite states are recurrent
and every all-time fibre has cardinality one. With $R(x,y)=(y,x)$,
$RHR=H^{-1}$.

This is exactly Roberts–Vivaldi's Equation (9) with $\delta=1$ and
$\epsilon=0$, and their Table 1 type $L_1$ with $h(y)=y^2$.
It is an ordinary quadratic generalized Hénon map, including its
finite-field reduction and reversing involution, not a new system.
The nontrivial cycle census varies in the pilots and no all-prime closed
census was derived. Bijectivity and reversibility alone are not two axes.
`NO_PROMOTION`.

## EG: moving-parameter commutators

Define $E(g,h)=(h,[g,h])$ on $G^2$.

1. For a target $(h,k)$ the inverse equation is exactly
   $ghg^{-1}=kh$. If $kh$ is not conjugate to $h$, the fibre is empty.
   Otherwise choose $g_0$ with $g_0hg_0^{-1}=kh$. Equality of
   $ghg^{-1}$ and $g_0hg_0^{-1}$ is equivalent to
   $g_0^{-1}g\in C_G(h)$, so all solutions are precisely
   $g_0C_G(h)$. The count is $|C_G(h)|$. This is the full conjugator
   coset formula; a centralizer jump is not an independent counting axis.
2. Put $G^{(0)}=G$ and $G^{(r+1)}=[G^{(r)},G^{(r)}]$.
   For $a,b\in G^{(r)}$, the element $c=[a,b]$ belongs to
   $G^{(r+1)}$. Since that subgroup is normal in $G^{(r)}$,
   $[b,c]$ also belongs to $G^{(r+1)}$. Consequently
   $E^2((G^{(r)})^2)\subseteq(G^{(r+1)})^2$.
   If the derived length is $d$, then $E^{2d}$ is constant at $(1,1)$.
   This is the generic derived-series contraction, not a new clock.

The heights $2,4,6$ in $S_2,S_3,S_4$ saturate that bound in those three
finite boxes only. No all-$S_n$ conclusion follows: the solvable hypothesis
does not hold for all symmetric groups. The fixed regular unitriangular
map of P119 has a different second-variable rule; its generic coset
proof is nevertheless exactly the counting primitive used here.
No nilpotent restriction is substituted to manufacture a fresh seat.
`NO_PROMOTION`.

## RC: truncated-ring Riccati feedback

On $R_p=\mathbb F_p[X]/(X^p)$ define $Q(f)=f'+f^2$.
The derivation is well-defined because $(X^p)'=0$, so differentiating
two representatives changes the result by a multiple of $X^p$.

For a target $b=\sum_{j=0}^{p-1}b_jX^j$, choose $a_0\in\mathbb F_p$.
There is exactly one recursively forced sequence

$$a_{j+1}=(j+1)^{-1}\left(b_j-\sum_{k=0}^j a_ka_{j-k}\right),
\qquad 0\leq j\leq p-2.$$

It is a source precisely when
$b_{p-1}=\sum_{k=0}^{p-1}a_ka_{p-1-k}$. Indeed, these equations
are every coefficient equation of $f'+f^2=b$, with no missing top
coefficient. This is an exact decoder with at most $p$ trial initial
coefficients, not a closed all-target fibre classification. It is the
ordinary triangular coefficient recursion and receives no mechanism credit.
At $p=2$, $f=a_0+a_1X$ gives $Q(f)=a_0+a_1$; both constants are fixed
and the height is one. This characteristic-two boundary is too thin.

The full $p=5$ pilot has height $94$ and one strict $22$-cycle in addition
to two fixed points. No full-prime temporal theorem is established.
The literature's $p$-Riccati equation $f^{(p-1)}+f^p=h^p$ is a different
equation and is not asserted to own this literal finite feedback map.
`NO_PROMOTION`.

## LV: cyclic quadratic feedback and exact ECA-72 adapter

Define $V(x)_i=x_i(x_{i+1}-x_{i-1})$ on $\mathbb F_p^L$, with
indices modulo $L$. The sum of the output coordinates is zero because
$\sum_i x_ix_{i+1}=\sum_i x_ix_{i-1}$. This is a quadratic
vector-field feedback map, not a time-one Lotka–Volterra flow or its
Kahan discretization.

For $p=2$, the neighborhood rule $v(a,b,c)=b(a+c)$ is one exactly
on $011$ and $110$. In Wolfram's order $111,110,101,100,011,010,001,000$
its output word is $01001000$, i.e. rule $72$. This is a literal
identification, not just a common qualitative behavior.

Here is the full elementary temporal argument. Zeros stay zero. An
all-one cycle becomes all zero in one step. Otherwise partition the
ones into maximal runs separated by zeros. A run of length one vanishes;
a run of length two stays fixed; a longer run loses its interior after
one step, leaving two isolated endpoints, which vanish at the next step.
The separating zeros prevent interaction between distinct original runs.
Thus $V^2$ retains exactly the original length-two runs, and $V^3=V^2$.
Periodic configurations are precisely disjoint length-two runs and the
zero configuration. The finite-cycle claim is also the direct restriction
of Meunier's rule-72 statement in Proposition 3. Its entire temporal
mechanism receives zero credit.

For $L=3$ over any characteristic-two field, after one step $x+y+z=0$,
and the update on that plane is coordinatewise squaring. This is a second
owned Frobenius boundary, not a rescue by field extension. Over odd primes
the pilot has varying core/height behavior, without an all-parameter
temporal theorem or an independent inverse theorem. `NO_PROMOTION`.

## ND: nonabelian cyclic differences

Define $D(x)_i=x_i^{-1}x_{i+1}$ on $G^L$.

1. For every image $y$, the ordered product $y_0\cdots y_{L-1}$
   telescopes to $1$. Conversely, if that product is $1$, choose
   $a\in G$ and set $x_0=a$ and
   $x_i=a y_0\cdots y_{i-1}$ for $1\leq i<L$.
   Every adjacent equation holds; the final one holds exactly by the
   product condition. These are all sources since a source is forced
   by its first coordinate. Therefore every nonempty fibre has $|G|$
   elements and the image has $|G|^{L-1}$ elements.
2. This is also a complete adapter to the generic twisted-coboundary
   lemma used inside P119. Let $\Gamma=G^L$ and let $\sigma$ be
   cyclic coordinate shift. Then $D(x)=x^{-1}\sigma(x)$, while
   $\operatorname{Fix}(\sigma)=\{(a,\ldots,a):a\in G\}$.
   If $D(x)=D(z)$, then
   $\sigma(zx^{-1})=zx^{-1}$. Conversely every left multiplication
   by a fixed element preserves the output. Thus each fibre is precisely
   a left diagonal-$G$ coset; the preceding coordinate formula merely
   writes that coset out. Neither uniformity nor the product constraint
   is a second research axis here.
3. When $G$ is abelian, additive notation makes $D=\sigma-I$,
   an owned linear difference system. When $L=2$ the first image is
   $(h,h^{-1})$ and the next parameter is $h^{-2}$, an owned power map;
   that length was deliberately excluded from the pilot.

The nonabelian $L\geq3$ pilots do not supply an all-group temporal
classification. The common small-box periods in some solvable groups
are not claimed to be universal. `NO_PROMOTION`.

## Open risks and stopping rule

There is no retained all-parameter two-axis candidate, no reserve, and no
paper theorem contract. The foregoing narrow deductions are not claims
that the full unsolved systems have no worthwhile mathematics. Larger
matrix sizes, primes or permutation groups were not used to compensate
for absent mechanisms. Failed or ambiguous source matches remain scoped
in the separate source report. Historical papers are not being rereviewed
or edited by this subtraction note.
