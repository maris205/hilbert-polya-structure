# Proof package: exact height interface and finite-place blindness

## Claim and status

**Original LG4: NOT CURRENTLY JUSTIFIED.** Its full statement and frozen B2
bridge are in [REPORT.md](REPORT.md). No original quantifier is removed.

**Auxiliary statements below: PROVABLE AS STATED.** They locate the required
height compatibility and refute two stronger intermediate implications, not
LG4. They are elementary transfer diagnostics, not proposed separate papers.

## Assumptions and notation

Let $F\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$, let $P,Q\in\mathbb Z^2$,
and set $\mathcal O=\{F^nP:n\in\mathbb Z\}$. Let $r_m$ be the least positive
period of $P$ modulo $m$, and write

$$
C_m=\{n\in\mathbb Z:F^nP\equiv Q\pmod m\},\qquad
H(R)=\max(1,|R_1|,|R_2|).
$$

When $C_m\ne\varnothing$, define
$\mu_m=\min\{H(F^nP):n\in C_m\}$. The minimum exists because the set is a
nonempty subset of the positive integers. Its definition does not assert
that an algorithm has found it. Put $\|R\|_\infty=\max_i|R_i|$.

## Strategy and dependency map

1. Finite quotient permutations identify exact hitting cosets.
2. Finite integer boxes turn a bound for *some* representatives into a true
   orbit hit; this is the missing bridge in height language.
3. Injectivity of a nonperiodic orbit proves the opposite behavior for
   *arbitrary* representatives and for continuous height extensions.
4. Integral forward and inverse coefficients force every finite-place orbit
   to be bounded, so all finite-place escape-rate observables vanish.
5. A specific everywhere-good Hénon map realizes the failed intermediate
   implications inside the original parameter family.

The full profinite parametrization is imported, without reproving it, from
`research_c424_c428/continuation_round4/arithmetic/PROOF_PACKAGE.md`, Sections
2–3. Statements 1–5 below require only the indicated elementary arguments.

## Proof

### 1. Exact hitting cosets and the height compatibility theorem

If $a\in C_m$, then

$$C_m=a+r_m\mathbb Z.\tag{1}$$

Indeed, in a finite cycle two iterates of its starting point agree precisely
when their indices differ by its least period. Negative indices are allowed
because reduction of $F$ is a permutation.

Assume henceforth in this section that $C_m\ne\varnothing$ for every $m\ge2$.
The following conditions are equivalent:

1. $Q\in\mathcal O$.
2. $\sup_{j\ge2}\mu_{j!}<\infty$.
3. There are integers $j_k\to\infty$ and $n_k\in C_{j_k!}$ for which
   $H(F^{n_k}P)$ is bounded independently of $k$.
4. For some $m\ge2$ and $n\in C_m$,
   $\|F^nP-Q\|_\infty<m$.

To prove $1\Rightarrow2$, choose one true hitting time for every modulus;
then $\mu_m\le H(Q)$. For $2\Rightarrow3$, choose a minimum for each
$j!$. To prove $3\Rightarrow1$, a bounded integer box contains only
finitely many points. Some $R\in\mathcal O$ therefore equals $F^{n_k}P$
for infinitely many indices $k$. Every coordinate of $R-Q$ is divisible by
the unbounded integers $j_k!$ along that subsequence, so both coordinates
are zero. Finally, $1\Rightarrow4$ uses zero difference, and
$4\Rightarrow1$ holds because the only integer divisible by $m$ with
absolute value less than $m$ is zero. This proves all four equivalences.

In particular, the full LG4 would follow from a new theorem giving bounded
$\mu_{j!}$ under all-modulus solvability. This is an **equivalent formulation
of the missing assertion**, not a proof obtained by defining a minimum.
The weaker-looking estimate $\mu_{j!}+\|Q\|_\infty<j!$ for some $j$ would
also suffice. Neither estimate has been derived here from the mere
nonemptiness of all $C_m$; doing so would close the original question.

### 2. Why product formula estimates need that compatibility

For a nonzero integer $z$ divisible by $m$, prime factorization gives

$$
|z|=\prod_p p^{v_p(z)}\ge\prod_p p^{v_p(m)}=m.\tag{2}
$$

This is the rational product formula in its elementary integer form. If
$F^nP\equiv Q\pmod m$ but $F^nP\ne Q$, at least one coordinate difference
is nonzero, and hence

$$
\|F^nP-Q\|_\infty\ge m,\qquad
H(F^nP)+\|Q\|_\infty\ge m.\tag{3}
$$

Thus the product formula gives a lower bound compatible with rapid orbit
growth. It does not give the upper bound in Section 1. The coordinates
$F^{n_m}P-Q$ vary with $m$; no fixed nonzero integer is being required to
have infinitely many prime divisors or unbounded divisibility.

### 3. No local height boundedness on an infinite profinite orbit

Suppose $P$ is nonperiodic. Then $n\mapsto F^nP$ is injective: equality at
two different times would give a positive period by applying an inverse
iterate. Consequently, for any $a\in\mathbb Z$, $r\ge1$, and $B\ge1$,
only finitely many $k\in\mathbb Z$ satisfy

$$H(F^{a+kr}P)\le B.\tag{4}$$

Otherwise infinitely many different integer points would lie in a finite
integer box. In particular, $H(F^{a+kr}P)\to\infty$ as $|k|\to\infty$.
By (1), every nonempty $C_m$ contains iterates of arbitrarily large height,
even if $Q$ itself lies in the actual orbit.

Let $X_P\subset\widehat{\mathbb Z}^{2}$ be the full congruence closure of
$\mathcal O$. Every nonempty relatively open subset $U\subset X_P$ contains
a point of $\mathcal O$, since $\mathcal O$ is dense. A basic congruence
neighborhood of that point, with some modulus $m$, is contained in $U$.
Its ordinary orbit points have indices in one coset modulo $r_m$, so (4)
proves that $H$ is unbounded on $U\cap\mathcal O$.

It follows that there is no real-valued function on $X_P$, agreeing with
$H$ on $\mathcal O$, that is continuous at even one point of $X_P$.
Continuity at a point would bound the function on some neighborhood of
that point, contrary to the preceding paragraph. Also there is no
continuous map $A:\widehat{\mathbb Z}\to\mathbb R^2$ with
$A(n)=F^nP$ for every integer $n$: its compact image would be bounded,
contradicting injectivity and finiteness of integer boxes.

An explicit sequence makes the forbidden limit passage visible. For each
$j\ge2$, choose a multiple $n_j$ of both $j!$ and $r_{j!}$ with
$H(F^{n_j}P)>j$. Such a multiple exists by (4). Then $n_j\to0$ in
$\widehat{\mathbb Z}$ and $F^{n_j}P\to P$ in every finite-place congruence
topology, while $H(F^{n_j}P)\to\infty$. The finite limit is the ordinary
integral point $P$; this is not an LG4 counterexample.

This argument refutes the proposed step “extend the archimedean orbit or
height continuously along the compact profinite interpolation.” It does
**not** refute the existence of special height-small representatives:
for $Q=P$, the constant time $0$ gives those representatives.

### 4. Finite-place Green functions are blind on the integral locus

Fix a prime $p$. Both $F$ and $F^{-1}$ map $\mathbb Z_p^2$ to itself, so for
every $z\in\mathbb Z_p^2$ and every $n\in\mathbb Z$,

$$\|F^nz\|_p\le1.\tag{5}$$

For any real normalization $D>1$, therefore,

$$
\lim_{n\to\infty}D^{-n}\log^+\|F^nz\|_p
=\lim_{n\to\infty}D^{-n}\log^+\|F^{-n}z\|_p=0.\tag{6}
$$

The terms are zero individually. In particular, whenever the usual regular
automorphism Green functions use the degree normalizations, both are zero
on all of $\mathbb Z_p^2$. This assertion does not require that reduction
preserve polynomial degree: integral forward/inverse coefficients suffice.
It applies to every local component of $\theta_P(t)$ as well as to every
ordinary integral point, whether or not that point is in the orbit closure.

Fixed affine coordinate changes do not repair the blindness. If
$T\in\operatorname{Aff}_2(\mathbb Q_p)$ and $G=T^{-1}FT$, then
$G^n(T^{-1}z)=T^{-1}(F^nz)$ lies in the compact, hence bounded set
$T^{-1}(\mathbb Z_p^2)$ for every positive or negative $n$. Dividing its
bounded logarithmic norm by $D^n$ again gives zero. There is no need for
$T^{-1}z$ itself to be integral in the new coordinates.

Thus GR5's choice of local good-model lattices cannot by itself make these
escape rates detect the global diagonal integer-time condition. This is a
statement about this observable, not a claim that good models or all other
finite-place data are useless.

### 5. Concrete failure inside the everywhere-good Hénon family

Set

$$F(x,y)=(y,y^2-x),\qquad F^{-1}(x,y)=(x^2-y,x),\qquad P=(0,2).\tag{7}$$

The map is an integral plane automorphism. Its leading coefficient and
Jacobian are units at every prime; its projective forward and inverse
indeterminacy points are $[1:0:0]$ and $[0:1:0]$, including after reduction.
Thus this example also has regular good reduction at every finite prime.
In GR5 notation $a=b=1$, $d=2$, $q(Y)=Y^2-Y$, and the identity coordinates
already give the standard lattice at every prime; no class-group patching
obstruction is present.

Write $F^nP=(b_n,b_{n+1})$ for $n\ge0$, where $b_0=0$, $b_1=2$, and
$b_{n+2}=b_{n+1}^2-b_n$. First $b_2=4>b_1$. If
$b_{n+1}>b_n\ge2$, then

$$b_{n+2}>b_{n+1}^2-b_{n+1}\ge b_{n+1}.$$

Induction gives strict growth, so $P$ is nonperiodic. Section 3 consequently
provides congruence returns to $P$ of arbitrarily large real height despite
regular good reduction at every finite place.

For an even sharper observable check, take $Q=(0,3)$. Every finite-place
forward/backward escape rate of both $P$ and $Q$ is zero by (6), but modulo
$2$, $P$ is the fixed point $(0,0)$ while $Q$ reduces to $(0,1)$. Hence
$Q$ is not even in the congruence orbit modulo $2$, and in particular is
not in the actual orbit. Equality of the entire finite-place Green vector
does not imply all-modulus solvability, much less actual orbit membership.
This explicitly refutes the Green-observable transfer, not LG4.

## Corrections or missing assumptions

To close original LG4 by this route, prove the still-missing implication

$$
(\forall m\ge2)\ C_m\ne\varnothing
\quad\Longrightarrow\quad
\sup_{j\ge2}\mu_{j!}<\infty.\tag{HC}
$$

An independently derived submodulus representative bound from Section 1
would be sufficient as well. Local interpolation determines the cosets;
finite-place Green functions vanish; a product formula supplies (3). No
derivation of (HC) from their combination is established here. The attempted continuous extension
of heights is false by Section 3. Failure of that stronger intermediate
step does not settle (HC), whose truth is equivalent to LG4 under the
all-modulus premise.

## Open risks and ownership

- No complete LG4 proof or all-modulus false positive is supplied.
- These are elementary compatibility diagnostics and imported-theorem
  applications, not a literature novelty claim or substantial paper claim.
- Finite-place escape rate zero is not being confused with global canonical
  height zero; the archimedean place remains essential.
- All finite hitting periods are native $r_m$; no prime-wise return clock
  replaces the original mixed-modulus time.
- No mathematical program, old rerun, PDF build, or formal evaluation was
  executed. The auxiliary proofs have author checking only unless the
  coordinator assigns a separate checker.
- `NO_BAD_EULER_OR_ROOT_NUMBER`; no target-arithmetic conclusion follows.
