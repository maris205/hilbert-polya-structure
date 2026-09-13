# Paper30 geometric detection: degree control and a uniform parameter-family period

Date: 2026-09-06. Status: NEW_AUTHOR_PROOF_ADDENDUM, INDEPENDENT_CHECK_REQUIRED.
This supplements the frozen
[rank-detection proof V1](PAPER30_GEOMETRIC_RANK_DETECTION_PROOF_V1_20260906.md),
320 lines, SHA256
`9544b15fcef634697e21a33e85d55f0a656728ba01f225b47e57148d6009e79d`.
It does not edit or silently expand that input while it is independently
reviewed. Its two new claims are checked separately below at author level.
Neither the quantum nor the wild-cover results are used.

## 1. Claims, assumptions and dependencies

Use the same complex Hénon composition of fixed ordered degrees
$\mathbf d=(d_0,\ldots,d_{k-1})$, each $d_i\ge2$, with every leading
coefficient nonzero. Let $\delta=\prod_i d_i$ and $D\ge0$. Set
$$
C_D=\left\lfloor\frac{(D+2)^2}{4}\right\rfloor,
\qquad \eta_D=C_D^{-1}.                                \tag{1}
$$
Let $L_D$ be the explicit degree-only orbit-word diameter bound from the
accepted mixed-radix basis, uniformly for these ordered degrees and all
coefficients. All periodic tests use complete $\operatorname{Fix}(F^n)$
geometric sets, not only points of least period $n$, unless explicitly stated.

**G4 — PROVABLE AS STATED.** For $\deg g\le D$, $g\notin(\sigma-1)A$,
$kn\ge3$ and $kn>2L_D$, the rank estimate in V1 improves to
$$
\operatorname{rank}(m_{[S_ng]})\ge\frac{\delta^n}{C_D},\qquad
\#\{z\in\operatorname{Fix}(F^n):S_ng(z)=0\}
\le(1-C_D^{-1})\delta^n.                               \tag{2}
$$
Thus $\eta_D$ may replace the possibly weaker $\kappa_D$ everywhere in
V1's finite count criterion, positive-density conclusion and adaptive
single-map algorithm. This is uniform in the coefficients and depends on
the ordinary degree $D$, not on the number of cyclic variables $kn$.

**G5 — PROVABLE AS STATED.** There is a terminating exact symbolic
algorithm depending only on $\mathbf d,D$ which outputs an integer
$M(\mathbf d,D)\ge1$ such that for every complex choice of the polynomial
coefficients of these degrees, and every polynomial $g$ of degree at most
$D$,
$$
S_Mg(z)=0\quad\forall z\in\operatorname{Fix}(F^M)(\mathbb C)
\quad\Longleftrightarrow\quad g\in(F^*-1)\mathbb C[x,y].\tag{3}
$$
Every positive integer multiple of this same $M$ also works for every
such coefficient choice. No a priori elementary formula, useful runtime,
uniform all-sufficiently-large-period statement, or computed numerical
value of $M$ is claimed. The algorithm constructs a finite algebraic
certificate, not an empirically selected period.

The dependencies are V1's proved-at-author-level rank/zero-count lemma and
the existing BLS saddle-count theorem, Paper29's coefficient-independent
ordinary-degree mixed-radix data, elementary digit inequalities, the
trace-form point-count identity, the Hilbert Nullstellensatz/Noetherian
finite generation, and divisibility of periodic sums. No uniform parameter
version or effective convergence rate of the BLS asymptotic is assumed.

## 2. A mixed-radix product inequality

Consider finite digits $0\le e_j<b_j$ in any radices $b_j\ge2$, with
$w_0=1$ and $w_j=b_0\cdots b_{j-1}$. Put $a=\sum_j e_jw_j$.
Then
$$
\prod_j\frac{b_j}{b_j-e_j}\le a+1.                    \tag{4}
$$

**Proof.** Induct on the number of digits. The empty sequence has product
one and $a=0$. Write $a=e_0+b_0a'$ and apply the induction hypothesis
to the tail. It remains to check
$$
\frac{b_0(a'+1)}{b_0-e_0}\le e_0+b_0a'+1.
$$
After multiplying by the positive denominator, the right side minus the
left side is exactly
$$
(b_0-e_0-1)(e_0+b_0a')\ge0.
$$
This proves (4) for every finite digit string, including interior zeros.

For an infinite orbit word $M_e$ of finite support, the accepted leading
coordinate monomial is a nonzero scalar multiple of $x^ay^b$, where the
nonnegative and negative tails give the two mixed-radix expansions. In
particular $\deg M_e=a+b$. Apply (4) separately to the two tails:
$$
\prod_i\frac{d_i}{d_i-e_i}\le(a+1)(b+1)
\le\left\lfloor\frac{(a+b+2)^2}{4}\right\rfloor.        \tag{5}
$$
If $a+b\le D$, this is at most $C_D$.

This product bound is sharp as a general inequality for degree-bounded
standard words across the allowed degree families. For $D\ge2$, take
$a=\lfloor D/2\rfloor$, $b=\lceil D/2\rceil$, choose adjacent phase
degrees $d_0=a+1$, $d_{-1}=b+1$, and take $M=x^ay^b$. Then its product
in (5) equals $(a+1)(b+1)=C_D$. For $D=1$ use one exponent one with
degree two; for $D=0$ use the constant word. Within the fixed binary family,
the words with $a=b=2^r-1$ also attain equality along
$D=2^{r+1}-2$. This does **not** prove that actual orbit sums attain the
rank or geometric zero-count bound in (2); no optimal detection threshold
is inferred from sharpness of this intermediate inequality.

## 3. The improved periodic rank and zero-count estimate

Every word occurring in the normal form of a polynomial of degree at most
$D$ has ordinary coordinate degree at most $D$, by the accepted triangular
basis. For each nonzero orbit coefficient in the periodic normal form,
choose a representative that actually occurs in $g$. Its product in (5)
is at most $C_D$.

Macro translation preserves that product because the degrees are periodic
with period $k$. Wrapping a word of diameter less than $kn$ also preserves
it, since the occupied indices remain distinct modulo $kn$ and keep their
phases. The leading nonconstant monomial of the periodic normal form is
one of these wrapped translates. Consequently the sharper, first bound
in V1 equation (7) is at least $\delta^n/C_D$. The nonzero-constant case
has full multiplication rank and satisfies the same inequality because
$C_D\ge1$. V1's independent-local-kernel estimate then gives (2).

This deduction uses the degree of a representative occurring in $g$, not
the potentially much larger coordinate degree of a far translated word.
The product is the translation invariant that makes that distinction valid.
The ordinary-coordinate degree and the formal cyclic-variable degree have
not been interchanged.

## 4. Universal cyclic rings and algebraic open certificates

Introduce variables $a_{i,j}$ for every coefficient of $p_i$, including
the leading coefficient $a_{i,d_i}$, and variables $u_i$ for their inverses.
Over $\mathbb Q$ form the finitely generated parameter ring
$$
R=\mathbb Q[\{a_{i,j}\},u_0,\ldots,u_{k-1}]
/(u_i a_{i,d_i}-1:0\le i<k).                           \tag{6}
$$
Complex points of $\operatorname{Spec}R$ are exactly the allowed coefficient
choices with all leading coefficients nonzero. For every admissible period
$n$ with $kn\ge3$, define the universal cyclic ring $B_n$ over $R$ by the
same cyclic recurrence relations. Multiply the $i$th relation by $u_i$.
It is monic with leading monomial $z_i^{d_i}$ and all other terms of lower
formal degree. Pairwise coprime leading monomials give the same standard
basis over $R$, of size $\delta^n$; monic polynomial reduction works over
this coefficient ring without passing to its fraction field.

In this basis form the symmetric trace matrix
$$
G_n=(\operatorname{Tr}_{B_n/R}(m_{b_vb_w}))_{v,w}.       \tag{7}
$$
Every entry lies in $R$. After any complex specialization it becomes the
actual trace matrix of the corresponding full periodic ring, whose rank
equals its number of distinct geometric points, by V1 §6.

Restrict now to periods with $kn>2L_D$ and put
$$
t_n=\left\lfloor(1-C_D^{-1})\delta^n\right\rfloor+1.
$$
Let $J_n\subset R$ be the ideal generated by all $t_n\times t_n$ minors
of $G_n$. At a complex parameter $s$,
$$
s\notin V(J_n)
\quad\Longleftrightarrow\quad
\operatorname{rank}G_n(s)>(1-C_D^{-1})\delta^n.          \tag{8}
$$
The right side is a sufficient geometric detection certificate at that
period for **every** degree-at-most-$D$ polynomial for that map, by G4.
It is an algebraic open condition, even though the saddle-count theorem
which will establish existence of some such $n$ is analytic.

## 5. A finite algebraic certificate exists without uniform asymptotics

For each fixed complex parameter $s$, the BLS saddle-count theorem implies
that (8) holds for all sufficiently large $n$, where the threshold may
depend on $s$. In particular at least one of the admissible $J_n$ has a
minor nonzero at $s$.

Let $J=\sum_n J_n\subset R$. After base change to $\mathbb C$, its zero
set has no complex points. The Hilbert Nullstellensatz in the finitely
generated complex algebra $R\otimes_{\mathbb Q}\mathbb C$ implies
$$
J(R\otimes\mathbb C)=R\otimes\mathbb C.
$$
The extension $R\to R\otimes_{\mathbb Q}\mathbb C$ is faithfully flat,
so $J=R$. Equivalently, an ideal generated over $\mathbb Q$ which becomes
the unit ideal after this field extension was already the unit ideal.
Membership of $1$ in the sum uses only finitely many terms. Thus there
are admissible periods $n_1,\ldots,n_s$ and finitely many of their minors
$\Delta_\nu$, together with $h_\nu\in R$, such that
$$
1=\sum_\nu h_\nu\Delta_\nu.                            \tag{9}
$$
At every complex parameter at least one of those minors is nonzero.
That parameter's map is therefore detected in degree $D$ by at least one
period in this finite list. This proves the finite-cover assertion directly;
it does not exchange the quantifiers in the BLS limit to obtain a uniform
eventual threshold.

The proof of existence is effective as a terminating exact search. Enumerate
admissible integers $n$ in increasing order, compute the finite matrices and
minor generators, and test whether the cumulative ideal is the unit ideal.
Represent this as polynomial ideal membership over $\mathbb Q$ together
with the relations $u_i a_{i,d_i}-1$, and use exact Gröbner-basis elimination.
Each iteration is a finite algorithm; (9) guarantees that some iteration
returns the unit ideal. Extended ideal-membership computation can retain
a concrete identity (9) as its output certificate. No a priori estimate
for the stopping iteration or determinant-enumeration cost is asserted.

## 6. One period for the entire coefficient family

Take $M=\operatorname{lcm}(n_1,\ldots,n_s)$ from a finite certificate (9).
The list is nonempty because the parameter ring is nonzero.
At a specified parameter choose one certified period $n_i$. If all complete
geometric period-$M$ values of $S_Mg$ vanish, then for any
$z\in\operatorname{Fix}(F^{n_i})(\mathbb C)$,
$$
S_Mg(z)=\frac{M}{n_i}S_{n_i}g(z)=0.
$$
Characteristic zero permits division by $M/n_i$. The certified lower-period
test forces $g$ to be a polynomial coboundary. Conversely a coboundary
telescopes to zero on every periodic point. Replacing $M$ by any positive
multiple gives the same argument. This proves G5.

The output is determined by the symbolic degree-family and $D$, not by a
particular coefficient choice or observed numerical result. This works for
arbitrary complex coefficients, including transcendental ones, because the
symbolic identity (9) specializes to every complex point of (6).

## 7. Scope of the strengthening and remaining review obligations

The uniform-period conclusion strengthens V1's single-map adaptive search;
it is a new argument, not a correction of a false claim in V1. V1 explicitly
did not yet assert such uniformity. This addendum uses a finite algebraic
open cover and the already checked least-common-multiple lemma to obtain
it, without changing the external count theorem.

There is no conflict with the earlier degree-two family whose maximum
Loewy length grows with the resonance order. Uniform local Loewy control
was only one sufficient approach; this proof does not supply that control
and does not need it. Similarly the old small-period point-value false
positive is not contradicted by the existence of another detecting period.

The general footprint inequality, digit arithmetic, trace forms,
Nullstellensatz, ideal-membership algorithms and finite-cover argument are
standard tools. The candidate novelty, if any, lies in their exact use with
the map's orbit-word structure and periodic count to obtain these geometric
detection statements. No part is a new general Nullstellensatz or a new
quantitative saddle-count theorem. A new independent check must verify G4
and G5, especially the symbolic specialization, faithful-flat descent,
termination and single-period versus all-large-period quantifiers.

No manuscript or experiment has been started and no numerical $M$ is
reported. No page-count exception is introduced. Batch07 remains 3/5;
all accepted artifacts and earlier failed candidates remain untouched.
