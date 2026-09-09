# A4 proof supplement — the native resolvent and its exact data boundary

2026-09-09 UTC. Current-team hand proof. No mathematical program was run.

## Claim and status

**PROVABLE AS STATED:** the extraction theorem, local full-inertia test,
Witt-to-local-length formula, normalization/fibre identity, and ghost-data
counterfamily stated below. Their classical ingredients are subtracted.

**NOT CURRENTLY JUSTIFIED:** nonvanishing of the extracted local class at
every level of the quadratic parabolic tower; global PC424-D; PC424-L.
The local test is not an admission or a claimed new general ramification
theorem. No fixed-point-index, Dold, or Lefschetz formula is proposed as
the research increment.

## Assumptions and notation

Let $p$ be an odd prime, $e\ge1$, and $n=p^e$. Initially $B$ is any field
of characteristic $p$ and $A$ is a finite étale $B$-algebra of rank $n$.
Let $\sigma$ be a $B$-automorphism of $A$ for which
$\operatorname{Spec}A$ is a $C_n$-torsor: on geometric points $\sigma$
is a single cycle of length $n$. This permits disconnected $A$.
Assume $A=B[x]$ and that the elements $\sigma^i x$ have pairwise distinct
values on a geometric fibre. One application of $\sigma$ is one tick.

The quadratic generic algebra supplies this setting componentwise:
over $k(c)$, with $k=\overline{\mathbb F}_p$, the reduced dynatomic
polynomial is separable and all generic roots have exact period $n$.
These are the imported R5 regular-fibre facts. Its native action is
$\sigma x=x^2+c$. Passing to one field factor of the invariant algebra
selects an orbit-quotient component, not a marked-point component.

For local statements $B=k((t))$ with $k$ algebraically closed of
characteristic $p$, and $v_B(t)=1$. The Artin–Schreier operator is
$\wp(b)=b^p-b$. A reduced polar representative is a finite sum
$\sum_{j>0,\,p\nmid j}c_jt^{-j}$. Witt coordinates are indexed from
$0$; upper and lower breaks are indexed from $1$.

## Strategy and dependencies

1. Lagrange interpolation gives an explicit trace-one element on the
   generic separable torsor; a weighted native orbit sum gives an
   additive resolvent.
2. Elementary cyclic-group theory and Artin–Schreier reduction make
   its local nonvanishing exactly equivalent to full native inertia.
3. Classical Artin–Schreier–Witt ramification converts the **full**
   reduced pole vector to lengths on a normalized branch.
4. A separate normalization calculation identifies the different
   observable that occurs in a fixed-parameter dynatomic fibre.
5. An explicit characteristic-$3$ quadratic test and an all-$e$
   ghost-blind family distinguish these implications from slogans.

## 1. Explicit native degree-$p$ resolvent

Define in $A[T]$

$$
M(T)=\prod_{i=0}^{n-1}(T-\sigma^i x),\qquad
z=\frac{x^{n-1}}{M'(x)},\qquad
y=-\sum_{i=0}^{n-1}\overline i\,\sigma^i z,
\tag{1}
$$

where $\overline i$ is the image of the integer $i$ in $\mathbb F_p$.
Then $M\in B[T]$, $M'(x)$ is invertible in $A$, and

$$
\sum_{i=0}^{n-1}\sigma^i z=1,\qquad
\sigma y-y=1,\qquad
a_0:=y^p-y\in B.
\tag{2}
$$

Moreover

$$
A^{\langle\sigma^p\rangle}
 =B[y]\cong B[Y]/(Y^p-Y-a_0).
\tag{3}
$$

**Proof.** The coefficients of $M$ are $\sigma$-invariant, hence in $B$.
After a separable closure of $B$, the $n$ values of $x$ are distinct;
therefore $M'(x)$ is nonzero on every factor, so it is invertible.
For the distinct geometric values $x_0,\ldots,x_{n-1}$, Lagrange
interpolation of $T^{n-1}$ gives

$$
T^{n-1}=
\sum_{i=0}^{n-1}x_i^{n-1}
\frac{M(T)}{(T-x_i)M'(x_i)}.
$$

Equating leading coefficients gives the first equation in (2).
Reindexing (1), including the wrapped term with coefficient
$-(n-1)=1$ in characteristic $p$, yields
$\sigma y-y=\sum_i\sigma^i z=1$. Thus $\sigma^j y=y+\overline j$;
in particular $\sigma^p y=y$ and $a_0$ is invariant.
On a geometric fibre $y$ has exactly $p$ distinct values, each repeated
$n/p$ times. Therefore it generates the rank-$p$ invariant algebra in
(3). These arguments are identities in the separable closure and
descend to $B$. $\square$

One may replace the displayed $z$ by **any** element of native trace
$1$. The resulting $y'$ also has $\sigma y'-y'=1$, so
$y'-y\in B$ and $a'_0-a_0\in\wp(B)$. Thus the extracted class
$[a_0]\in B/\wp(B)$ is independent of that choice. No division by $n$
or averaging in characteristic $p$ occurs.

The construction is the standard additive Hilbert-90 mechanism with
a Lagrange-interpolation trace-one element, now specified on the
native quadratic cyclic cover. Its algebraic ingredients are not
claimed as new: compare Elkies's [Higher Algebra notes, Theorems
4.30–4.33](https://people.math.harvard.edu/~elkies/M250.01/index.html).

## 2. Exact local full-inertia test

Let $B=k((t))$ as above. Let $H\le C_n$ be the image of the local
absolute Galois group in the permutations of the torsor. Then

$$
H=C_n
\quad\Longleftrightarrow\quad
[a_0]\ne0\text{ in }B/\wp(B)
\quad\Longleftrightarrow\quad
a_0\text{ has a nonzero reduced polar part}.
\tag{4}
$$

In this case $A$ is a field, totally ramified of degree $n$ over $B$.
If it is obtained by completing a generic native cover at a normalized
orbit-quotient place, that place supplies a full native rotation in the
global stabilizer image of R5.

**Proof.** Choose a geometric point of the torsor and identify its
$\sigma$-iterates with $C_n$. Galois commutes with $\sigma$, hence acts
by translations through a homomorphism into $C_n$. The action on (3)
is its reduction modulo $p$. A subgroup of the cyclic group of order
$p^e$ maps nontrivially modulo $p$ exactly when it is the whole group:
each proper subgroup is contained in $pC_n$.

The Artin–Schreier algebra in (3) is connected exactly when its
polynomial has no root in $B$, which is $[a_0]\ne0$. Indeed the
conjugates of one root are obtained by adding elements of $\mathbb F_p$,
and a subgroup of its group of order $p$ is either trivial or full.

For completeness, every Laurent series has the asserted reduced
representative. Its regular part lies in $\wp(k[[t]])$: the constant
term is solvable since $k$ is algebraically closed, and the remaining
coefficients are solved successively because the derivative of
$Y^p-Y$ is $-1$. For a negative term $c t^{-pj}$, subtract
$\wp(c^{1/p}t^{-j})$. Starting from the largest pole order and
repeating decreases that order whenever it is divisible by $p$.
This terminates on the finite negative part. A nonzero reduced polar
polynomial cannot be $b^p-b$: if $v_B(b)<0$, its highest pole order is
divisible by $p$, while if $v_B(b)\ge0$ it has no pole. This also proves
uniqueness of the reduced polar part.

Full translation image makes the torsor connected and its degree is
$n$. A finite extension of $k((t))$ has no nontrivial residue extension
when $k$ is algebraically closed; the resulting cyclic extension is
therefore totally ramified. The local image is a subgroup of the
global image, proving the last assertion. $\square$

The word **reduced** is essential. A raw pole divisible by $p$ can
disappear after Artin–Schreier subtraction and does not certify (4).
Regular $a_0$ at one place does not imply global disconnectedness.

If the global orbit-quotient algebra has only one field factor and
one normalized place satisfies (4), then the full marked dynatomic
curve is irreducible. Without the first condition, this proves only
irreducibility above that one quotient component. This is precisely
the two-obligation distinction in R5, not a substitute for it.

## 3. Which local lengths full Witt pole data recovers

Assume the local test succeeds. Choose a Witt equation compatible
with the native generator:

$$
F(\mathbf Y)-\mathbf Y=\mathbf a=(a_0,\ldots,a_{e-1}),\qquad
\sigma\mathbf Y=\mathbf Y+(1,0,\ldots,0),
\tag{5}
$$

where subtraction and addition are Witt operations. Replace
$\mathbf a$ by a reduced representative, and put
$m_j=-v_B(a_j)$, with $m_j=-\infty$ if $a_j=0$; its first coordinate
has $m_0>0$ and $p\nmid m_0$. A compatible equation exists by
Artin–Schreier–Witt theory; **its higher reduced coordinates are added
data**, not determined here from the degree-$p$ resolvent alone.

The classical pole formula gives upper breaks

$$
u_i=\max_{0\le j<i}p^{i-1-j}m_j\quad(1\le i\le e).
\tag{6}
$$

For a direct proof over arbitrary perfect residue fields, including
the algebraically closed case used here, see Elder–Keating,
[Theorem 2.3](https://arxiv.org/html/2503.16830v1). Generator-compatible
standard equations and the classical break rule already appear in
Obus–Pries, [§3.2–3.3, Lemmas 3.3–3.5](https://www.math.colostate.edu/~pries/Preprints/10pries_obus409_JPPA.pdf).
No new ownership of (5)–(6) is claimed.

Let $R=k[[u]]$ be the completed normalized branch. Define

$$
b_1=u_1,\qquad
b_i=b_{i-1}+p^{i-1}(u_i-u_{i-1})\quad(2\le i\le e).
\tag{7}
$$

For $j\not\equiv0\pmod n$, let $r=v_p(j)\in\{0,\ldots,e-1\}$.
Then the local fixed-scheme length for the native iterate $\sigma^j$ is

$$
\operatorname{length}_k R/(\sigma^j(u)-u)=b_{r+1}+1.
\tag{8}
$$

**Proof of the conversion.** The lower ramification group at a real
number $b\ge0$ consists of those $g$ with
$v_R(g(u)-u)\ge b+1$. The inverse Herbrand function has slopes
$1,p,\ldots,p^{e-1}$ between consecutive upper breaks of a fully
ramified cyclic $p^e$ extension; integration gives (7). An element
whose exponent has valuation $r$ generates the unique subgroup
$\langle\sigma^{p^r}\rangle$. It leaves the lower filtration exactly
at $b_{r+1}$, so its difference has order $b_{r+1}+1$. For a nonzero
power series of order $d$, the quotient of $k[[u]]$ by that series has
length $d$, giving (8). The identity iterate $n\mid j$ has a
one-dimensional fixed formal disc, not a finite local length.
$\square$

The ordinary closed point of this branch contributes **one**, not
$b_{r+1}+1$, to an ordinary fixed-point count. Formula (8) is an
enriched local observable on the same clock, never a replacement
definition of ordinary counting.

## 4. Normalization and fixed-parameter fibres are a separate interface

Let $X$ be a reduced algebraic curve over $k$, let $P\in X(k)$, and
let $h=c-c_0$ be nonzero on every local irreducible component through
$P$. Write $R=\mathcal O_{X,P}$, and let $S$ be its finite semilocal
normalization. Its branches above $P$ have normalized valuations
$v_q$. Then

$$
\operatorname{length}_k R/hR=\sum_{q\mapsto P}v_q(h).
\tag{9}
$$

**Proof.** The quotient $C=S/R$ has finite $k$-dimension. Multiplication
by $h$ is injective on $R$ and $S$. Applying it to
$0\to R\to S\to C\to0$ gives the exact sequence

$$
0\to C[h]\to R/hR\to S/hS\to C/hC\to0.
$$

For an endomorphism of a finite-dimensional vector space, kernel and
cokernel have equal dimensions. Thus the first and last terms cancel
in the length equality, and $\dim_kR/hR=\dim_kS/hS$. On each
normalized discrete valuation branch the latter length is $v_q(h)$;
residue degrees are $1$ because $k$ is algebraically closed.
$\square$

If a branch maps to a normalized quotient branch with parameter $t$
and $h=t^d\cdot\text{unit}$ there, then its contribution to (9) is
$d\,e_q$, where $e_q$ is the ramification index of that branch over
the quotient branch. Full local native inertia gives $e_q=p^e$.
The exponent $d$ and the list of branches are additional compatibility
data. Lower breaks in (8) must not be substituted for these numbers.

In particular, an aggregate fibre length $p^e$ does not by itself
distinguish one fully ramified branch from several less ramified
branches. Nor does normalization automatically preserve individual
fixed-point intersection lengths at a singular point. Equation (9)
addresses the fibre observable, not an unsupported fixed-locus
normalization identity.

## 5. Exact quadratic hand test: characteristic $3$, period $3$

This example tests the extraction on the actual quadratic native
clock. It is not a finite census or an all-level theorem.

Work over $B=k((t))$ in characteristic $3$. Put

$$
c=-t^2-t+1,\qquad x=2+w,\qquad
M(w)=w^3-tw^2-t^2w+t+t^3.
\tag{10}
$$

The change $r=t-w$ gives
$M(w)=t-tr^2-r^3$. Hence with $y=1/r$ the equation is exactly

$$
y^3-y=t^{-1},\qquad w=t-y^{-1}.
\tag{11}
$$

The right side has a reduced simple pole, so (11) is a cyclic
degree-$3$, totally ramified extension. Its generator $y\mapsto y+1$
sends $w$ to

$$
w'=w+w^2-t^2-t.
\tag{12}
$$

To check this, substitute $w=t-y^{-1}$; multiplying the difference
between $t-(y+1)^{-1}$ and the right side of (12) by
$y^2(y+1)$ gives $t(y^3-y)-1=0$. On the other hand,
$f_c(x)-2=(2+w)^2+c-2$ is exactly the right side of (12).
Thus (11)'s generator is the original quadratic one-step return,
and its points have native period $3$, not a separately assigned
arithmetic clock. Consequently $M$ is a factor of the period-$3$
dynatomic polynomial after the indicated parameter base change.

The trace of $w$ is $t$, by the $w^2$ coefficient in (10), so $z=w/t$
is another trace-one choice for §1. Its weighted resolvent is

$$
-\sigma z-2\sigma^2z
=\frac{w^2}{t}-t
=\frac1{t-w}=y.
$$

The middle equality follows from the orbit trace and (12), and the
last follows from (10). Thus the simple pole is obtained by the
claimed native extraction, not inserted as an unrelated equation.

Here $v_B(w)=1/3$, so $w$ is a uniformizer upstairs. Equation (12)
gives $v_R(\sigma w-w)=2$, hence lower break $1$ and local length
$2$. Under A3's base change $c=1/4-s^2/4$, which in characteristic
$3$ gives $c=1-s^2$, the equation $t^2+t=s^2$ has a unique root
$t\in s^2k[[s]]$ with leading term $s^2$. The reduced polar part of
$1/t$ is $s^{-2}$, so the break becomes $2=p-1$ and the normalized
native fixed length becomes $3$. This agrees with A3's prime-level
calculation while illustrating why base/branch conventions matter.

## 6. Exact obstruction to ghost-only or truncated-Witt recovery

Fix $p$ odd and $e\ge2$. For any positive $M$ with

$$
p\nmid M,\qquad M>p^{e-1}(p-1),
$$

take the local native cyclic extension defined by the reduced vector

$$
\mathbf a_M=(t^{-(p-1)},0,\ldots,0,t^{-M})\in W_e(k((t))),
\tag{13}
$$

and choose the generator specified by addition of $(1,0,\ldots,0)$.
For $e=2$ this vector has exactly the two displayed nonzero entries.
All these extensions have degree $p^e$ and one closed normalized
point, whose reduced native action is fixed and whose tangent action
is the identity. Their first $e-1$ Witt coordinates agree.
Every characteristic-$p$ ghost coordinate also agrees, because

$$
\operatorname{gh}_j(a_0,\ldots,a_j)
=a_0^{p^j}+p a_1^{p^{j-1}}+\cdots+p^j a_j
=a_0^{p^j}\quad\text{in }k((t)).
\tag{14}
$$

Their upper breaks are $u_i=p^{i-1}(p-1)$ for $i<e$ and $u_e=M$.
Thus $b_{e-1}$ is independent of $M$, while

$$
\operatorname{length}_k
k[[u]]/(\sigma^{p^{e-1}}u-u)
=1+b_{e-1}+p^{e-1}\bigl(M-p^{e-2}(p-1)\bigr),
\tag{15}
$$

which is unbounded as $M$ ranges over the permitted integers.
This proves that even knowing the first $e-1$ Witt coordinates,
all characteristic-$p$ ghosts, the ordinary closed-point count and
the tangent multiplier does not determine the top native length.

There is an exact match to the R4 trace blind spot. Equations (7)
give $b_i\equiv p-1\pmod p$, so every length in (8) is divisible by
$p$. On any such finite local fixed algebra, multiplication by $U$
has diagonal entries $U(0)$ in the basis $1,u,\ldots,u^{d-1}$.
The native action and all its powers are triangular with diagonal
entries $1$, since a $p$-power-order automorphism has tangent
multiplier $1$ in characteristic $p$. Hence

$$
\operatorname{tr}(m_U\sigma^j)=d\,U(0)=0
\quad\text{for every }U\text{ and }j.
\tag{16}
$$

The fixed ideal is $\sigma$-stable because $\sigma$ commutes with
the iterate defining it, so these operators are well-defined.
The whole trace packet is therefore zero throughout the family,
even though (15) varies. Witt-vector ghost data or postprocessing
this zero trace packet cannot restore the missing length.

An imported B4 result closes a nearby attempted repair. The proof of
[B4 Lemma 4](../b4_wild_jet_detection/PROOF_SUPPLEMENT.md), §4, was
read and its characteristic-independent filtration argument checked.
Applied here, it gives, for **every** prescribed ambient jet depth
$N\ge1$,

$$
\det\bigl(T-\sigma^*\mid (u)/(u^{N+1})\bigr)=(T-1)^N.
$$

Thus even the collection of these ambient jet characteristic
polynomials for all $N$ is identical across (13). This uses only the
common tangent multiplier $1$. The ambient quotient has dimension
chosen externally as $N$; it must not be confused with the dynamical
fixed ideal in (15), whose varying colength is precisely the missing
information. This imported deduction is not a new independent result.

This is a complete obstruction in the stated **local cyclic-cover
category**. The family (13) is not claimed to occur as the quadratic
dynatomic tower. It therefore disproves the general ghost-only
refinement, not PC424-D, PC424-L, or every possible quadratic-specific
bridge. Full Witt pole vectors do distinguish it, as (6)–(8) show.

## 7. Cross-lane application and the exact unfinished implication

A3 supplies the unique degree-$n$ Hensel factor $M_e$ for the cluster
at $c=1/4$, after the tame parameter change
$c=1/4-s^2/4$, with local coordinate
$z=x-(1+s)/2$. Over $K=k((s))$ its $n$ distinct roots form one native
$n$-cycle and all have valuation $(p-1)/p$. This is the exact interface
in [A3 REPORT](../a3_wild_tower/REPORT.md), sections “Proved auxiliary
interface” and “Exact A4 handoff”.

The source-owned inputs used there are consistent with
Lindahl–Rivera-Letelier, [Proposition 4.4 and Theorem C](https://arxiv.org/html/1311.4478v3): the parabolic reduction is minimally ramified and
the relevant small cycle is unique. Their assertions about one
native cycle are not assertions about one Galois orbit.

Apply (1) to this $M_e$ and $z$. The invariant algebra is $K$, so the
resulting $a_{0,e}$ lies in $K$. The remaining local bridge is now
the concrete assertion

$$
\operatorname{red}_{\rm AS}(a_{0,e})\ne0
\qquad\text{for every odd }p\text{ and every }e>1.
\tag{17}
$$

If proved, (17) would force the cluster factor to be irreducible over
$k((s))$ and supply the full rotation image for its quotient
component. The valuation $(p-1)/p$ by itself only forces a factor
degree divisible by $p$, not $p^e$. No general evaluation of (17),
nor an all-component quotient transitivity theorem, is proved here.

## Corrections, open risks, and disposition

- All ramification classification and Hilbert-90 ingredients remain
  classical; the useful output is a precise native-coordinate test.
- The rational denominators in (1) become singular on a collided
  special fibre. Their Laurent/normalization data are new inputs,
  not consequences of ordinary special-fibre trace values.
- A compatible full Witt equation is richer than its first quotient;
  (13)–(16) prove this cannot be omitted in general.
- Local length on a normalized cyclic cover, length of a dynatomic
  parameter fibre, and multiplicity of a periodic point of a
  fixed-parameter germ are not identified without another theorem.
- No full quadratic all-level result, finite-census theorem, target
  Euler factor, root number, automorphy, divisor correspondence,
  Hilbert–Pólya construction, or Route-B entry is claimed.
- Current-team author derivation is not independent internal review
  or human peer review. Admission remains the coordinator's decision.

`NO_BAD_EULER_OR_ROOT_NUMBER`.
