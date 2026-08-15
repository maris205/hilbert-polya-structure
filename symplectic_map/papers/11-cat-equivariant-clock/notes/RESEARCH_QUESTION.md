# Research Question

## Frozen identity

- Candidate ID: `cat_equivariant_retention_tradeoff_v1`.
- Safe title: **An Equivariant-Zeta Audit of Cat-Map Centralizer
  Quotients**.
- Date and literature cutoff: **2026-08-15 UTC**.
- Intended paper type: scoped boundary/negative mathematical audit.
- Feasibility decision: `GO_SCOPED_BOUNDARY_NOTE_LOW_NOVELTY`.
- Required terminal certificate:
  `EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /`
  `A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

Paper 11 opens exactly the equivariant/orbifold/stacky boundary that Paper 10
left outside scope.  It starts only after Papers 9 and 10 reached
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`.  It does not alter or rerun either
upstream project.

The inherited map is

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad
T_A(x)=Ax\pmod{\mathbb Z^2}.
$$

For every integer $q\ge 2$, put $R_q=\mathbb Z/q\mathbb Z$ and retain the
Paper-10 cyclic-vector locus

$$
X_q=\mathrm{CV}_q
=\{v\in R_q^2:\det[v,Av]\in R_q^\times\}.
$$

Paper 10 proved that

$$
G_q=C_q=\operatorname{Cent}_{\mathrm{GL}_2(R_q)}(A)
=R_q[A]^\times
$$

is finite abelian and acts freely and transitively on $X_q$.  Under a chosen
base point, $X_q\simeq G_q$ as the left regular $G_q$-set.  The map
$\phi_q=A|_{X_q}$ is left translation by the distinguished element
$a_q=A\in G_q$.  Define

$$
r_q=\operatorname{ord}_{G_q}(a_q)=\operatorname{ord}_q(A),
\qquad
n_q=|G_q|=|X_q|,
\qquad
m_q=\frac{n_q}{r_q}.
$$

Thus the source system consists of $m_q$ cycles, each of exact length $r_q$,
whereas the coarse quotient $X_q/G_q$ is one fixed point.

## The exact question

Paper 10 showed that the ordinary zeta function of the coarse quotient is
$(1-t)^{-1}$ and that the specialization $t=q^{-s}$ is external.  Paper 11
asks whether a standard refinement can retain enough of the discarded data
to produce both:

1. one local factor rather than $m_q$ source factors; and
2. an intrinsic modulus/prime clock rather than a shell label supplied from
   outside.

The word **standard** is frozen to the following named constructions and no
others:

1. the point-order Burnside-ring equivariant zeta associated with
   $L^{G_q}$;
2. the orbit-order integral Burnside-ring equivariant zeta associated with
   $\widetilde L^{G_q}$;
3. the 2013 $G$-permutation zeta of Gusein-Zade, an element of the
   Grothendieck ring of finite $(\mathbb Z\times G_q)$-sets determined by all
   twisted fixed-point data $L^{G_q}(g\phi_q^m)$;
4. the two 2015 orbifold reductions through the Gusein-Zade--Luengo--
   Melle-Hern\'andez homomorphism $\Phi_q$;
5. the enhanced Burnside class of Ebeling--Gusein-Zade and its enhanced
   orbifold zeta;
6. the action groupoid and quotient stack $[X_q/G_q]$ with the induced
   endomorphism; and
7. Zegowitz's exact shortening/gluing description of the coarse quotient.

Miles's zeta for group actions and Walton's finite-field quotient identities
are literature boundaries, not objects to be implemented.  Miles explicitly
tacitly assumes an infinite finitely generated acting group; Walton assumes
quasiprojective varieties over finite fields.  Neither convention may be
silently transplanted to the finite local groups $G_q$ or composite residue
rings.

## Frozen definitions

Let $B(G_q)=K_0(\mathrm{f.}\,G_q\text{-sets})$ be the Burnside ring and set

$$
\mathbf u_q=[G_q/\{e\}]\in B(G_q).
$$

This is the class of the regular orbit.  Its Burnside marks are

$$
\mu_K(\mathbf u_q)=|(G_q/\{e\})^K|
=\begin{cases}
n_q,&K=\{e\},\\
0,&K\ne\{e\}.
\end{cases}
$$

Two scalar maps are relevant:

$$
\kappa_q:B(G_q)\to\mathbb Z,
\qquad \kappa_q([Y])=|Y|,
$$

and, because $G_q$ is abelian, the additive orbifold homomorphism of
abelian groups

$$
\Phi_q:B(G_q)\to\mathbb Z,
\qquad
\Phi_q([G_q/H])=|H|.
$$

No multiplicativity for the Cartesian Burnside product is asserted.  Indeed,
for a nontrivial $G_q$ the regular class satisfies
$\mathbf u_q^2=n_q\mathbf u_q$, whereas
$\Phi_q(\mathbf u_q)=1$ and
$\Phi_q(\mathbf u_q^2)=n_q\ne1=\Phi_q(\mathbf u_q)^2$.

In particular,

$$
\kappa_q(\mathbf u_q)=n_q,
\qquad
\Phi_q(\mathbf u_q)=1.
$$

For any additive map $\psi:B(G_q)\to R$, the notation
$\psi_*(\zeta)$ below means the **exact-period exponent reduction**

$$
\psi_*\!\left(\prod_{m\ge1}(1-t^m)^{-s_m/m}\right)
:=\prod_{m\ge1}(1-t^m)^{-\psi(s_m)/m}.
$$

It does not assert that $\psi$ preserves Burnside multiplication, the
pre-$\lambda$ structure, or the power structure.  For $\psi=\Phi_q$, this
is precisely the 2015 orbifold
construction: first apply $\Phi_q$ to the equivariant Lefschetz sequence,
then perform divisor inversion and form the scalar zeta.  The same
exponentwise convention defines the cardinality ledger.  Ordinary Burnside
marks are used only on the exact-period classes themselves, never by a
naive coefficientwise application to a Burnside power series.

The point-order and orbit-order equivariant Lefschetz sequences are denoted
$L^{G_q}(\phi_q^k)$ and $\widetilde L^{G_q}(\phi_q^k)$, respectively.  The
first is the fixed-point class underlying the 2008 rational Burnside zeta;
the second underlies the distinct 2015 integral orbit-order zeta.  The 2015
paper discusses both sequences.  The first counts points fixed by the
iterate as a $G_q$-set.  The second counts $G_q$-orbits setwise fixed by the
iterate, decorated by their orbit type.

## General information-loss hierarchy frozen for proof

The regular torsor is the decisive Paper-11 specialization, but the
definition boundary is clearest in the following finite theorem.  Let $C$ be
any finite abelian group, let $a\in C$, let $H=\langle a\rangle$, and let
$X$ be a finite $C$-set.  Write its unique orbit-type decomposition as

$$
X\simeq\coprod_{K\le C} n_K(C/K),
\qquad n_K\in\mathbb Z_{\ge0}.
$$

For every $K$ with $n_K>0$, define

$$
d_K=[H:H\cap K],
\qquad
M_K=[C:HK].
$$

On each copy of $C/K$, translation by $a$ has exact point period $d_K$ and
$M_K$ cycles.  The theorem to prove before implementation is the exact
hierarchy

$$
\zeta_{X,\phi_a}(t)
=\prod_{K\le C}(1-t^{d_K})^{-n_KM_K},
$$

$$
\zeta_{X/C,\bar\phi_a}(t)
=(1-t)^{-\sum_K n_K},
$$

$$
P_m^C=\sum_{d_K=m}n_K[C/K],
\qquad
\zeta_{\mathrm{pt}}^C(t)
=\prod_{m\ge1}(1-t^m)^{-P_m^C/m},
$$

and

$$
\widetilde P_1^C=[X]=\sum_Kn_K[C/K],
\qquad
\widetilde P_m^C=0\ (m>1),
\qquad
\widetilde\zeta_{\mathrm{orbset}}^C(t)=(1-t)^{-[X]}.
$$

The untwisted exact-period classes $P_m^C$ depend on $a$ only through the
cyclic subgroup $H=\langle a\rangle$; they do not distinguish generators of
$H$.

For abelian $C$, orbifold reduction gives

$$
\Phi_{C,*}(\zeta_{\mathrm{pt}}^C)
=\prod_K(1-t^{d_K})^{-n_K|K|/d_K},
\qquad
\Phi_{C,*}(\widetilde\zeta_{\mathrm{orbset}}^C)
=(1-t)^{-\sum_Kn_K|K|}.
$$

The stronger $C$-permutation invariant has, on a copy of $C/K$, the
$(\mathbb Z\times C)$-stabilizer

$$
\widehat K_a
=\langle\{0\}\times K,(1,a^{-1})\rangle,
$$

and therefore records the twist $a^{-1}K$.  Across all nonempty orbit types
it recovers $a$ only modulo the action kernel

$$
N=\bigcap_{n_K>0}K.
$$

It recovers the exact labelled element when and only when the $C$-action is
effective, $N=\{e\}$.  It does not recover an “unlabelled generator” after
forgetting the ambient $C$-identification.

The quotient stack decomposes as

$$
[X/C]\simeq\coprod_{K\le C}n_KBK.
$$

Translation by $a$ induces an endomorphism $2$-isomorphic to identity on
every component.  The inertia of $BK$ has $|K|$ sectors because $K$ is
abelian, but all sectors carry static period-one dynamics.  Thus stabilizer
or twisted-sector data may survive while the clock does not.

### Frozen abstract counterexample

Let $C=C_6$, let $a$ be a generator, and let

$$
X=C_6/C_2\ \sqcup\ C_6/C_3,
$$

where $C_j$ denotes the unique subgroup of order $j$.  The action is
effective because $C_2\cap C_3=\{e\}$, and the stronger $C$-permutation
invariant recovers $a$.  Nevertheless

$$
d_{C_2}=3,
\qquad
d_{C_3}=2,
$$

so

$$
\zeta_{X,\phi_a}(t)
=(1-t^3)^{-1}(1-t^2)^{-1}
$$

has no period-six factor even though $a$ has order six.  Meanwhile

$$
\zeta_{X/C,\bar\phi_a}(t)=(1-t)^{-2},
$$

$$
\Phi_{C,*}(\zeta_{\mathrm{pt}}^C)
=(1-t^3)^{-2/3}(1-t^2)^{-3/2},
\qquad
\Phi_{C,*}(\widetilde\zeta_{\mathrm{orbset}}^C)=(1-t)^{-5},
$$

and

$$
[X/C]\simeq BC_2\sqcup BC_3
$$

has five static inertia sectors.  This is a proof-level structural control,
not a new modulus and not an additional candidate search.

## Questions frozen for proof

### Q1. Which equivariant zeta retains the source period?

Prove that

$$
L^{G_q}(\phi_q^k)=
\begin{cases}
\mathbf u_q,&r_q\mid k,\\
0,&r_q\nmid k,
\end{cases}
$$

so the point-order exact-period sequence has the single nonzero term
$s^{G_q}_{r_q}=\mathbf u_q$.  In the standard rational Burnside convention,

$$
\zeta^{G_q}_{\mathrm{pt},q}(t)
=(1-t^{r_q})^{-\mathbf u_q/r_q}
\in 1+t\,(B(G_q)\otimes\mathbb Q)[[t]].
$$

This refinement retains the source period $r_q$, but its cardinality
reduction is

$$
\kappa_{q,*}\!\left(\zeta^{G_q}_{\mathrm{pt},q}(t)\right)
=(1-t^{r_q})^{-n_q/r_q}
=(1-t^{r_q})^{-m_q},
$$

which is exactly the ordinary source zeta and therefore restores the full
orbit multiplicity.  In this regular-translation specialization the entire
untwisted sequence depends only on $r_q$.  It cannot distinguish two
different elements of $G_q$ having the same order; in particular it does not
retain the distinguished generator $a_q$ itself.  This point-order series
must not be conflated with the stronger $G$-permutation invariant below.

### Q2. Which equivariant zeta keeps integral Burnside coefficients?

Since $X_q/G_q$ is a single orbit and $\phi_q$ sends it to itself for every
iterate, prove

$$
\widetilde L^{G_q}(\phi_q^k)=\mathbf u_q
\quad(k\ge1).
$$

The orbit-order exact-period sequence is
$\widetilde s^{G_q}_1=\mathbf u_q$ and zero otherwise, so

$$
\widetilde\zeta^{G_q}_{\mathrm{orbset},q}(t)
=(1-t)^{-\mathbf u_q}
\in1+t\,B(G_q)[[t]].
$$

This version retains the free-orbit type and its Burnside marks, but the only
dynamical exponent is $1$.  It does not retain $r_q$.

### Q3. What do the scalar and orbifold reductions do?

Prove the exact four-way ledger

$$
\begin{aligned}
\kappa_{q,*}(\zeta^{G_q}_{\mathrm{pt},q})
  &=(1-t^{r_q})^{-m_q},\\
\Phi_{q,*}(\zeta^{G_q}_{\mathrm{pt},q})
  &=(1-t^{r_q})^{-1/r_q},\\
\kappa_{q,*}(\widetilde\zeta^{G_q}_{\mathrm{orbset},q})
  &=(1-t)^{-n_q},\\
\Phi_{q,*}(\widetilde\zeta^{G_q}_{\mathrm{orbset},q})
  &=(1-t)^{-1}.
\end{aligned}
$$

Among these standard reductions, none simultaneously has source exponent
$r_q$ and unit Euler-factor multiplicity.  Obtaining
$(1-t^{r_q})^{-1}$ would require an extra $q$-dependent operation such as
raising the point-orbifold factor to the power $r_q$.  Obtaining
$(1-q^{-s})^{-1}$ from the period-one factor requires the external
specialization $t=q^{-s}$.

### Q4. What does the 2013 $G$-permutation zeta retain?

Let $K_0(\mathrm{f.}\,G_q\text{-perm})$ be the Grothendieck ring of finite
$G_q$-permutations, equivalently finite $(\mathbb Z\times G_q)$-sets.  For
$g\in G_q$ and $m\ge1$,

$$
L^{G_q}(g\phi_q^m)
=\begin{cases}
\mathbf u_q,&g=a_q^{-m},\\
0,&g\ne a_q^{-m}.
\end{cases}
$$

Therefore the Gusein-Zade $G$-permutation zeta is represented by the actual
finite $G_q$-permutation $(X_q,\phi_q)$.  The stabilizer of the base point
$e\in X_q\simeq G_q$ under the $(\mathbb Z\times G_q)$-action

$$
(m,g)\cdot x=g\,a_q^m x
$$

is

$$
\widehat H_q
=\{(m,a_q^{-m}):m\in\mathbb Z\}
=\langle(1,a_q^{-1})\rangle.
$$

In the standard irreducible triple notation this is

$$
(H,m,\alpha)=(\{e\},1,a_q^{-1}).
$$

Thus this stronger invariant retains the twist $a_q^{-1}$, and recovers the
exact $a_q$ because the regular action is effective and the ambient group
$G_q$ is held fixed and labelled.  In a non-effective action it would retain
only the corresponding coset modulo the action kernel; no stronger claim is
allowed.  Across moduli it still lies in the varying rings
$K_0(\mathrm{f.}\,G_q\text{-perm})$, so retaining $a_q$ does not by itself
construct a common modulus clock or prime selector.

### Q5. Does the enhanced Burnside class retain more?

Regard $(X_q,\phi_q)$ as a finite enhanced $G_q$-set with the only possible
character on its trivial isotropy.  Prove that its irreducible enhanced class
is

$$
\widehat X_{\{e\},1,a_q,1}.
$$

Because $G_q$ is abelian, this class retains the exact distinguished element
$a_q$, and hence its order $r_q$.  This is the positive boundary: a richer
equivariant object can retain what the coarse quotient forgot.

Then prove that its enhanced orbifold zeta is nevertheless

$$
\zeta^{\mathrm{enh,orb}}_q(t)=(1-t)^{-1}.
$$

Indeed, the regular action is free, so only the identity twisted sector is
nonempty, and its centralizer quotient is the one-point set $X_q/G_q$ with
identity induced dynamics.

### Q6. What does the stack quotient retain?

Let $\mathcal G_q=G_q\ltimes X_q$ be the action groupoid.  Prove:

1. the free transitive action makes $\mathcal G_q$ equivalent to the terminal
   one-object groupoid;
2. its inertia groupoid has no nonidentity twisted sector; and
3. the functor induced by $\phi_q(x)=a_qx$ is naturally isomorphic to the
   identity functor.

Consequently, every invariant that depends only on the quotient stack
$[X_q/G_q]$, the induced endomorphism up to $2$-isomorphism, and Morita
equivalence must take the same value as it does on one fixed point.  This is
a conditional functorial statement, not an impossibility theorem for every
object called a stacky zeta function.

### Q7. How exactly are the source cycles lost in the coarse quotient?

Apply Zegowitz's shortening/gluing terminology.  Every source orbit has
length $r_q$, every $G_q$-orbit is all of $X_q$, and

$$
|\mathcal O_{\phi_q}(x)\cap\mathcal O_{G_q}(x)|=r_q.
$$

Therefore every source orbit shortens by the factor $1/r_q$, while precisely

$$
\frac{|\mathcal O_{G_q}(x)|}
{|\mathcal O_{\phi_q}(x)\cap\mathcal O_{G_q}(x)|}
=\frac{n_q}{r_q}=m_q
$$

source orbits glue to the unique quotient fixed point.

### Q8. Does any retained datum create a modulus or prime clock?

The retained source period is the integer $r_q$, not $q$ and not $\log q$.
The frozen controls already contain exact collisions

$$
r_2=r_4=3,
\qquad
r_6=r_9=12,
$$

so the period alone does not determine the modulus.  The richer coefficients
live in the varying rings $B(G_q)$, and the enhanced elements live in the
varying rings $\widehat B(G_q)$.  Treating the ambient group/ring name as the
modulus is a family label, not a return-time law.  No canonical comparison or
global coefficient ring is supplied by the construction.

Moreover, the same torsor, all four equivariant formulas, the enhanced class,
and the stack collapse exist for every composite $q\ge2$.  No standard
refinement audited here selects primes.

## Exact audit frozen in advance

Any later implementation may examine exactly the Paper-10 ordered tuple

$$
\mathcal Q_{\rm frozen}=(2,3,5,7,11,4,6,9,10)
$$

and no other modulus.  The five prime controls and four composite controls
are inherited verbatim; none is selected for Paper 11 after inspecting an
equivariant invariant.

The proof-derived ledger is:

| $q$ | $n_q=|G_q|$ | $r_q$ | $m_q=n_q/r_q$ | point support | orbit support | point-orbifold exponent | enhanced twist order | enhanced-orbifold period |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 3 | 1 | 3 | 1 | $1/3$ | 3 | 1 |
| 3 | 8 | 4 | 2 | 4 | 1 | $1/4$ | 4 | 1 |
| 5 | 20 | 10 | 2 | 10 | 1 | $1/10$ | 10 | 1 |
| 7 | 48 | 8 | 6 | 8 | 1 | $1/8$ | 8 | 1 |
| 11 | 100 | 5 | 20 | 5 | 1 | $1/5$ | 5 | 1 |
| 4 | 12 | 3 | 4 | 3 | 1 | $1/3$ | 3 | 1 |
| 6 | 24 | 12 | 2 | 12 | 1 | $1/12$ | 12 | 1 |
| 9 | 72 | 12 | 6 | 12 | 1 | $1/12$ | 12 | 1 |
| 10 | 60 | 30 | 2 | 30 | 1 | $1/30$ | 30 | 1 |

For every row, the later audit must also verify:

- $G_q$ is the exact Paper-10 local centralizer and $X_q$ its exact torsor;
- $\phi_q$ has $m_q$ cycles of uniform length $r_q$;
- the regular orbit has trivial point stabilizer;
- the regular Burnside marks are $n_q$ at the trivial subgroup and zero at
  every nontrivial subgroup;
- the point-order and orbit-order Lefschetz sequences match the theorem;
- the four scalar reductions match exactly as formal exponent/support data;
- the full twisted table has the unique solution $g=a_q^{-m}$ and the
  irreducible $G$-permutation triple is $(\{e\},1,a_q^{-1})$;
- the enhanced tuple is $(\{e\},1,a_q,1)$ and $a_q$ has order $r_q$;
- every nonidentity inertia sector is empty;
- the quotient endomorphism is identity and the action-groupoid endomorphism
  is naturally isomorphic to identity;
- Zegowitz shortening and gluing factors are $r_q$ and $m_q$; and
- no numerical $s$, $\log q$, or $q^{-s}$ is evaluated.

## Required decision and nonclaims

If the theorem and exact audit pass, record exactly

`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

The certificate means:

1. the rational point-order Burnside zeta retains the source order but also
   retains/restores multiplicity under its ordinary scalar reduction;
2. the integral orbit-order Burnside zeta retains the free orbit type but
   has quotient period one;
3. the 2013 $G$-permutation invariant retains the exact translating element
   only after the effective, labelled ambient $G_q$-action is fixed;
4. the enhanced Burnside class likewise retains the distinguished
   translating element, while its orbifold image and the free quotient stack
   collapse to one fixed point;
5. the retained integer period is not a modulus clock;
6. all coefficient/permutation/enhanced rings are shell-wise $q$-dependent;
   and
7. composites satisfy the same construction, so no prime selector appears.

The project does **not** claim a new equivariant zeta, a new Burnside ring,
a new enhanced Burnside class, a new orbifold formula, a new quotient-stack
theorem, a universal impossibility theorem, a canonical comparison among the
rings $B(G_q)$, a Miles zeta for finite groups, an extension of Walton's
finite-field theorem to residue rings, a transfer/Fredholm determinant, a
Hecke quantization, a prime/zero correspondence, or historical priority.
In particular, a trivial action gives the quotient stack $BC$ with $|C|$
inertia sectors when $C$ is abelian, but those sectors have identity dynamics;
sector count must never be called a return-time clock.
