# Proof Package — an all-place failure of polynomial reversibility

## Claim

The universal implication frozen in [REPORT.md](REPORT.md) is false.
More precisely, put

$$
H_{c,d}(x,y)=(y,c y^d-x),\qquad
K=\mathbf Q(\sqrt7),\qquad
F=H_{4,7}\circ H_{1/16,15}\circ H_{16,15}\circ H_{1/4,7}.       \tag{1}
$$

Then every original completion $K_v$, including every finite and infinite
place, admits a polynomial automorphism $R_v$ satisfying
$R_vFR_v^{-1}=F^{-1}$, but no polynomial automorphism over $K$ does.
The global exclusion has no degree, order, affine, or involution
restriction. One application of the entire displayed word is the
native map throughout.

## Status

**PROVABLE AS STATED — author proof of the negative answer.**
The original universal affirmative implication is disproved, not
weakened. Independent mathematical review and the separate
source-substantiality/admission judgment remain pending.

## Assumptions

The example uses precisely the number field and finite nonempty word
in (1). Every factor has degree at least two and has coefficient of
$-x$ equal to one, so it is an allowed generalized Hénon automorphism.
There is no integrality or good-model hypothesis in the frozen question;
none is introduced. The geometric classification below is carried out
over $\mathbf C$. A fixed embedding of a number field into $\mathbf C$
is only a proof device for excluding global reversors, not a replacement
of its original global field or completions.

The only non-elementary structural input is the classical
Jung–van der Kulk amalgam description of the full polynomial
automorphism group. Its exact use is stated in §1. The needed facts about
its tree and the particular centralizer are proved below. The
all-local eighth-power exception is classical Wang arithmetic, also
verified directly in §4.

## Notation

Group multiplication is composition, with the rightmost map acting first.
Let $G=\operatorname{Aut}_{\mathbf C}(\mathbf A^2)$,
let $\mathcal A$ be its affine subgroup, and let

$$
\mathcal E=\{(x,y)\mapsto(\alpha x+p(y),\beta y+\eta):
              \alpha\beta\ne0\},\qquad
\mathcal B=\mathcal A\cap\mathcal E.
$$

Write $\tau(x,y)=(y,x)$, $H_d=H_{1,d}$,
$e_d(x,y)=(-x+y^d,y)$, so $H_d=\tau e_d$. Set

$$
F_0=H_7H_{15}H_{15}H_7,\qquad
S_\zeta(x,y)=(\zeta x,\zeta^{-1}y).
$$

For a map $g$, $C_G(g)$ is its full centralizer in $G$ and
$\operatorname{Rev}_L(g)$ denotes all polynomial reversors defined over
a specified field $L$. This set is allowed to be empty.

## Proof strategy

Compute the entire geometric centralizer of $F_0$, not just a commuting
subgroup. The aperiodic degree cycle of its tree axis forces every
centralizer translation to be a native power. Computing the pointwise
axis stabilizer then leaves exactly $\mu_8$. A diagonal twist transfers
this exhaustive classification to (1). Consequently any global
polynomial reversor, after removal of a $K$-defined native power, would
give an eighth root of $16$ in $K$. Such a root exists in every $K_v$
and does not exist in $K$.

## Dependency map

1. The counterexample follows from the exhaustive family criterion in
   §3 and the direct all-place arithmetic in §4.
2. The family criterion uses the scalar conjugation identities in §3
   and the **equality** for the full centralizer in §2.
3. The centralizer equality uses the aperiodic axis argument in §1,
   followed by explicit four-factor diagonal-affine comparisons.
4. Section 1 imports only $G=\mathcal A*_{\mathcal B}\mathcal E$
   and the corresponding reduced-word theorem. No source theorem
   requiring roots of unity to be only $\{\pm1\}$ is used.
5. The local reversors are constructed directly. No classification over
   a completion, field embedding $K_v\hookrightarrow\mathbf C$, common
   local exponent, density theorem, or omitted-place argument is needed.

## Proof

### 1. The whole-group axis and its degree labels

The classical Jung–van der Kulk theorem gives

$$
G=\mathcal A*_{\mathcal B}\mathcal E.                         \tag{2}
$$

In particular, a nonempty alternating product of elements of
$\mathcal A\setminus\mathcal B$ and
$\mathcal E\setminus\mathcal B$ cannot lie in $\mathcal B$.
The precise background is recorded in Gómez–Meiss, §2.1, Theorem 3,
and, with general-field notation, Baake–Roberts, §2, Facts 1–2 and
Proposition 1. We use (2) over $\mathbf C$ only.
Sources: [Gómez–Meiss](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf)
and [Baake–Roberts](https://arxiv.org/pdf/math/0501151).

Construct a graph with vertices $G/\mathcal A$ and $G/\mathcal E$ and
one edge $g\mathcal B$ joining $g\mathcal A$ to $g\mathcal E$.
It is connected because the two factors generate $G$. A non-backtracking
closed edge path would give a nonempty alternating product of
non-$\mathcal B$ elements of the two factors lying in $\mathcal B$,
contradicting the reduced-word assertion. Hence the graph is a tree,
denoted $\mathcal T$. Left multiplication by every member of $G$
acts on it by an isometry preserving the two vertex types.
In particular this action has no edge inversions.

The word

$$
F_0=\tau e_7\,\tau e_{15}\,\tau e_{15}\,\tau e_7              \tag{3}
$$

has eight alternating non-$\mathcal B$ factors, its first and last
factors lying in different groups. Starting from the base edge
$\mathcal B$, take successive edges obtained by left prefixes of (3):

$$
\mathcal B,\ \tau\mathcal B,\ H_7\mathcal B,\
H_7\tau\mathcal B,\ \ldots,\ F_0\mathcal B.                  \tag{4}
$$

Consecutive edges meet and do not backtrack. Repeating this path by
$F_0^j$, $j\in\mathbf Z$, also introduces no backtracking at the joins,
because the word is cyclically reduced. Thus (4) extends to a
bi-infinite geodesic $\mathcal L$, and $F_0$ translates it by eight
edges.

This is the unique axis of $F_0$. One can see this directly: if a point
$z$ of the tree has projection $q$ to $\mathcal L$, the geodesic from
$z$ to $F_0z$ goes through $q$ and $F_0q$. Its length is

$$
d(z,F_0z)=8+2d(z,\mathcal L).                                \tag{5}
$$

For $z\notin\mathcal L$, the two off-axis branches are attached at
distinct points $q,F_0q$, so this path has no cancellation. Formula (5)
also holds on the axis. Consequently $\mathcal L$ is precisely the
minimal-displacement set. Every $h\in C_G(F_0)$ preserves it. On this
line $h$ cannot reverse orientation: a reflection conjugates a nonzero
translation to its inverse, whereas $h$ commutes with $F_0$.
Its restriction is therefore a translation, possibly by zero edges.
The length is even because the two vertex types are preserved.

There is a useful invariant at every $\mathcal E$-vertex of this line.
If the vertex is $g\mathcal E$ and its two incident axis edges are
$g e_1\mathcal B$ and $g e_2\mathcal B$, with $e_i\in\mathcal E$,
assign the integer

$$
\operatorname{turn}(g\mathcal E)=\deg(e_1^{-1}e_2)\ge2.       \tag{6}
$$

The inequality follows because distinct edges mean
$e_1^{-1}e_2\notin\mathcal B$. To verify that (6) is intrinsic:
changing $g$ to $ge$ changes both $e_i$ to $e^{-1}e_i$ and leaves
their relative product unchanged; changing either edge representative
on the right by an element of $\mathcal B$ multiplies the relative
element on the left and right by triangular affine maps. Such
multiplications preserve the degree of an elementary map of degree
at least two: substitution of a nonconstant affine expression in $y$
preserves its leading degree, and the other added terms have degree
at most one. Reversing the two edges replaces the elementary map by
its inverse, which has the same degree. Finally, left multiplication
by an arbitrary element of $G$ preserves the relative pair exactly.
Thus every $G$-action preserves these turn labels.

Along $\mathcal L$ the labels, in one of its two orientations, are
the periodic sequence

$$
\ldots,7,15,15,7,\ 7,15,15,7,\ldots.                         \tag{7}
$$

Its least positive shift period is four. Shifts one and two fail at
the first entry of $(7,15,15,7)$; shift three fails at its second entry.
Therefore a centralizer element can translate by only a multiple
of four $\mathcal E$-vertices, equivalently eight edges.

**Axis conclusion.** For every $h\in C_G(F_0)$ there is an integer
$j$ such that $h_0=hF_0^{-j}$ fixes $\mathcal L$ pointwise and still
centralizes $F_0$. This conclusion applies to every polynomial
automorphism in $G$, without any degree bound or normal-form ansatz
for $h$.

### 2. Exact computation of the pointwise stabilizer

We compute those $h_0$ from the axis conclusion. Since $\mathcal B$
and $\tau\mathcal B$ occur in (4), their stabilizers imply

$$
h_0\in\mathcal B\cap\tau\mathcal B\tau^{-1}
=\{(x,y)\mapsto(\alpha x+c,\beta y+e):\alpha\beta\ne0\}.      \tag{8}
$$

Indeed, $\mathcal B$ consists of upper triangular affine maps,
and conjugation by $\tau$ makes them lower triangular; their
intersection has diagonal linear part and arbitrary translation.

Put $(d_1,d_2,d_3,d_4)=(7,15,15,7)$ and
$P_0=\mathrm{id}$, $P_i=H_{d_1}\cdots H_{d_i}$.
The axis contains $P_i\mathcal B$ and $P_i\tau\mathcal B$
for $0\le i\le4$, the last pair being in the next translated segment.
It follows that

$$
h_i=P_i^{-1}h_0P_i
$$

is diagonal affine for every such $i$. Moreover
$h_i=H_{d_i}^{-1}h_{i-1}H_{d_i}$ for $1\le i\le4$
and $h_4=F_0^{-1}h_0F_0=h_0$.

For a general diagonal affine map
$D(x,y)=(\alpha x+c,\beta y+e)$, direct substitution gives

$$
H_d^{-1}D H_d(x,y)
 =\big((\alpha y+c)^d-\beta y^d+\beta x-e,\ \alpha y+c\big).
                                                                  \tag{9}
$$

If (9) is diagonal affine, the coefficient of $y^d$ in its first
coordinate gives $\beta=\alpha^d$. Its coefficient of $y^{d-1}$
then gives $d\alpha^{d-1}c=0$, hence $c=0$, since $d\ge2$
and the field has characteristic zero. When $d=2$, the forbidden
$y^{d-1}$ term is the off-diagonal linear term, so the same reasoning
still applies. After these two conclusions (9) becomes
$(\beta x-e,\alpha y)$. Applying the next factor forces its first
translation $-e$ to vanish. Thus the first two factors already
give $c=e=0$ in (8).

All four conjugations now swap the two diagonal scalars. Their
necessary and sufficient equations are

$$
\beta=\alpha^7,\qquad
\alpha=\beta^{15},\qquad
\beta=\alpha^{15},\qquad
\alpha=\beta^7.                                            \tag{10}
$$

The first and third equations imply $\alpha^8=1$, and then
$\beta=\alpha^{-1}$. Conversely these two conditions satisfy all
of (10). Hence every pointwise-axis centralizer is $S_\zeta$
with $\zeta^8=1$. These maps really centralize $F_0$: for
$d\in\{7,15\}$, (9) gives
$H_d^{-1}S_\zeta H_d=S_\zeta^{-1}$, and the four successive
inversions cancel.

Combining this calculation with §1 proves the **full equality**

$$
C_G(F_0)=
\{S_\zeta F_0^j:\zeta^8=1,\ j\in\mathbf Z\}
\cong\mu_8\times\mathbf Z.                                 \tag{11}
$$

There is no hidden root of $F_0$ in this assertion: the axis-period
argument proves that its own native translation generates the entire
translation image. Also $F_0$ has infinite order by its nonzero
axis translation, while $S_\zeta$ has finite order, making the
displayed direct product faithful.

The coordinate swap satisfies $\tau H_d\tau=H_d^{-1}$.
Because the four-factor sequence in $F_0$ is a palindrome,
$\tau F_0\tau=F_0^{-1}$. If $R$ is any polynomial reversor
of $F_0$, $R\tau$ centralizes $F_0$. Conversely every
centralizer multiplied by $\tau$ is a reversor. Thus (11) yields

$$
\operatorname{Rev}_{\mathbf C}(F_0)
=\{S_\zeta F_0^j\tau:\zeta^8=1,\ j\in\mathbf Z\}.            \tag{12}
$$

This derivation, rather than an imposed order assumption, exhausts
all possible polynomial reversors.

### 3. A field-preserving scalar-twist criterion

For a number field $L$ and $a\in L^*$, define

$$
F_a=H_{a,7}\,H_{a^{-2},15}\,H_{a^2,15}\,H_{a^{-1},7}.        \tag{13}
$$

Choose $u\in\mathbf C$ with $u^8=a$ after fixing an embedding
$L\hookrightarrow\mathbf C$, and put $A_u=\operatorname{diag}(u,u^{-1})$.
Two direct identities are

$$
A_u^{-1}H_dA_u^{-1}=H_{u^{d+1},d},\qquad
A_uH_dA_u=H_{u^{-(d+1)},d}.                                \tag{14}
$$

Inserting alternating $A_u,A_u^{-1}$ between the factors therefore gives

$$
A_u^{-1}F_0A_u
=(A_u^{-1}H_7A_u^{-1})(A_uH_{15}A_u)
 (A_u^{-1}H_{15}A_u^{-1})(A_uH_7A_u)
=F_a.                                                     \tag{15}
$$

The conjugated swap is

$$
R_{t_0}=A_u^{-1}\tau A_u,\qquad
R_t(x,y)=(t^{-1}y,tx),\qquad
t_0=u^2,\quad t_0^8=a^2.                                  \tag{16}
$$

Because $A_u$ commutes with every $S_\zeta$, (11)–(12)
conjugate to

$$
\operatorname{Rev}_{\mathbf C}(F_a)
=\{F_a^j R_t:j\in\mathbf Z,\ t^8=a^2\}.                    \tag{17}
$$

In fact $S_\zeta R_{t_0}=R_{\zeta^{-1}t_0}$, and
$\zeta^{-1}t_0$ runs through exactly the eight roots of $a^2$.
This explains all roots, including those with fourth power $-a$;
one must not incorrectly demand $t^4=a$.

If a polynomial reversor $R$ is defined over $L$, (17) writes
$R=F_a^jR_t$ for one integer $j$ and one root $t$. Both
$F_a^{-j}$ and $R$ are polynomial automorphisms over $L$,
even when $j$ is negative. Hence

$$
F_a^{-j}R=R_t\in\operatorname{Aut}_L(\mathbf A^2).
$$

Reading the coefficient of $x$ in the second coordinate gives
$t\in L^*$. This proves necessity without restricting the original
degree or order of $R$. Conversely, if $t\in L$ and $t^8=a^2$,
the affine involution $R_t$ in (16) reverses $F_a$ by (17).
We have proved

$$
\operatorname{Rev}_L(F_a)
=\{F_a^jR_t:j\in\mathbf Z,\ t\in L^*,\ t^8=a^2\},\qquad
F_a\text{ reversible over }L
\ \Longleftrightarrow\ a^2\in L^{\times8}.                  \tag{18}
$$

Only the number-field version of the exhaustive equality (18) is
needed here. Its sufficiency works over **any** characteristic-zero
field containing $a$: choose $u^8=a$ in an algebraic closure, use the
identities (14)–(16), and put $\zeta=t_0/t$. Then $\zeta^8=1$
and $S_\zeta R_{t_0}=R_t$. This proves the reversal identity in
the algebraic closure; since $R_t$ and $F_a$ have coefficients in
the original field, it holds there. In particular this constructs
reversors over each original completion without embedding that
completion into $\mathbf C$.

### 4. The exact all-place Wang class

We verify

$$
16\in K_v^{\times8}\quad\hbox{for every place }v\hbox{ of }K,
\qquad
16\notin K^{\times8},\qquad K=\mathbf Q(\sqrt7).             \tag{19}
$$

This is old arithmetic, recorded for this precise field and exponent
in Song Wang, §2.1, Proposition 2.1 and the following remark on p. 7.
The direct argument below avoids any dependence on the exceptional-set
notation in the PDF text extraction.
[Primary source](https://arxiv.org/pdf/1401.0389v1).

**Odd rational primes.** Let $p$ be odd, and let $\chi$ be the
quadratic character of $\mathbf F_p^*$. At least one of
$2,-2,-1$ is a square modulo $p$. Indeed if both
$\chi(2)$ and $\chi(-1)$ equal $-1$, their product is
$\chi(-2)=1$; otherwise $\chi(2)=1$ or $\chi(-1)=1$.
All three are nonzero modulo $p$, so a square root lifts by Hensel's
lemma to $\mathbf Q_p$. If $r^2=2$ or $r^2=-2$, then $r^8=16$.
If $i^2=-1$, then $(1+i)^2=2i$, $(1+i)^4=-4$, and
$(1+i)^8=16$. Thus $\mathbf Q_p$ contains an eighth root of $16$.
Every completion $K_v$ above $p$ contains $\mathbf Q_p$,
so this proves all of their required local statements.

**The dyadic place.** An odd square in $\mathbf Q_2$ is congruent
to $1$ modulo $8$, so $7$ is not a square and
$K\otimes_{\mathbf Q}\mathbf Q_2=\mathbf Q_2(\sqrt7)$ is a field.
There is therefore one place of $K$ above $2$. The element $-7$
is a square in $\mathbf Q_2$. For example the strong Hensel
criterion applied to $f(X)=X^2+7$ at $X=1$ gives
$v_2(f(1))=3>2v_2(f'(1))=2$. If $b^2=-7$ in $\mathbf Q_2$,
then $i=\sqrt7/b$ belongs to this original completion and has
$i^2=-1$. Consequently $1+i$ is the required eighth root there.
Equivalently this completion is $\mathbf Q_2(i)$.

**Infinite places.** The field $K$ is real quadratic; both infinite
completions are $\mathbf R$. Each contains $t=\sqrt2$ with $t^8=16$.
There are no complex places to add.

**The global field.** Since $K\subset\mathbf R$, a solution
$t^8=16$ in $K$ would be $t=\sqrt2$ or $t=-\sqrt2$.
Neither lies in $\mathbf Q(\sqrt7)$. For completeness,
$(b+c\sqrt7)^2=2$ with $b,c\in\mathbf Q$ forces $bc=0$;
the alternatives require a rational square to equal $2$ or
$2/7$, both impossible by the parity of their $2$-adic valuations.
This proves (19).

### 5. Completion of the original counterexample

Take $a=4$ in (13), so $F_a$ is precisely (1) and $a^2=16$.
For every place $v$, choose the root $t_v\in K_v^*$ just constructed
and set

$$
R_v(x,y)=(t_v^{-1}y,t_vx).
$$

It is an automorphism over the original $K_v$, it satisfies
$R_v^2=\mathrm{id}$, and the sufficiency argument following
(18) gives $R_vFR_v^{-1}=F^{-1}$. Thus every clause of the
local premise holds, including the dyadic and infinite places.

If there were **any** polynomial reversor over $K$, necessity in
(18) would give $t\in K$ with $t^8=16$, contradicting (19).
Therefore the global conclusion fails. This settles the frozen
universal implication negatively without changing its quantifiers. $\square$

## Corrections, source subtraction, and scope

No assumption was added to the original question. The universal
affirmative answer is false; the stated counterexample is the answer
to that question. The uniform criterion (18) is a proof interface
within this one mechanism, not a replacement question or extra
admission.

The arithmetic in §4, the normal-form/tree framework, and the general
centralizer-coset method are classical. In particular the final
example of Cantat–Dujardin (2024), §2.2, already controls the entire
polynomial conjugacy field of two scalar-twisted Hénon maps using
their full centralizer. Consequently scalar twisting plus exhaustive
centralizer descent is **not a new method here**. Combining that
example with Wang also gives an immediate analogous all-place
failure for conjugacy of two independently chosen maps. The present
remaining distinction is realization for the constrained pair
$(F,F^{-1})$ using the single native four-factor word, with all
alternative polynomial reversors excluded in §§1–3.
[Closest mechanism source](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.13164).

We do not import the subgroup inclusion of Gómez–Meiss as a full
centralizer equality, nor a roots-of-unity restriction from a
different-field centralizer theorem. There is no invocation of
universal Kummer injectivity: (19) is itself an explicit failure.
The integer component issue is resolved for this example because
the **entire** translation image is generated by the original
$K$-defined $F$, and removing any of its powers preserves $K$.

## Open risks and verification boundary

The author finds no remaining mathematical gap in this proof.
Independent review must still inspect (6), the eight-edge
translation conclusion, the exhaustive affine calculation (9)–(11),
and descent of **all** components in (17)–(18). These are review
obligations, not assumed lemmas.

No mathematical program was run. The proof uses exact hand identities
and classical structural/arithmetic inputs. No claim is made about
all Hénon words being classified, integral reversors, good models,
other local/global problems, SF2, target Euler factors or root numbers.
Whether the proved inverse-pair realization is substantial enough
for an independent paper requires a separate source-subtraction
and admission decision; mathematical correctness alone does not
establish that decision.
