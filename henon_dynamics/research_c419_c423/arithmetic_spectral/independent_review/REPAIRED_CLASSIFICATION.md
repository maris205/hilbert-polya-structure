# Proof Package: the all-level parity-corrected scattering criterion

2026-09-07. This is a separate proof package following two falsified
conjectures. The original [N=50 counterexample](PROOF_PACKAGE.md)
and its exact-check artifacts are not modified. The first repair
requiring reality at every unramified divisor prime is also false;
the present statement includes the necessary parity qualification.

## Claim

For every positive integer $N$, let $\Phi_N(s)$ be the full width-one
cusp scattering matrix of $\Gamma_0(N)$, with trivial nebentypus and
weight zero. The following are equivalent:

1. $[\Phi_N(s),\Phi_N(t)]=0$ for every pair of regular parameters.
2. Every primitive character $\chi$ of conductor $q$ with $q^2\mid N$
   satisfies both
   $$
   \chi^2=\bar\chi^2,
   \qquad
   \chi(p)\in\{1,-1\}
   \quad\text{for each }p\mid N,\ p\nmid q,
   \text{ with }v_p(N)\text{ odd}.
   \tag{C}
   $$

The second clause does **not** constrain an unramified divisor prime
whose exponent in $N$ is even. The conductor-$1$ character is included.
The physical object and all-level quantifier are those of the
[original frozen contract](../FROZEN_CONTRACTS.md).

## Status

**PROVABLE AS STATED**, by the proof below and the explicitly supplied
fixed-basis algebraic dependencies. This is a mathematical proof-package
status, not a claim of novelty or an admission decision.

The first original conjecture is false at $N=50$. Its first repair is
false at $N=100$. Neither is retrospectively relabelled as this theorem.
No computation beyond the already recorded single $N=50$ check is used
here, and no new mathematical computation was executed for this proof.

## Assumptions and notation

- For each divisor $f\mid N$, set $g_f=(f,N/f)$ and label its cusps by
  $1/(uf)$ with $u\in(\mathbb Z/g_f\mathbb Z)^\times$, represented
  coprime to $N$. All scaling matrices conjugate the stabilizer to
  translations of period one.
- Fix a primitive character $\chi$ of conductor $q$ with $q^2\mid N$.
  Put $L=N/q^2$, $d=\tau(L)$, and $e_p=v_p(L)$. Here $\tau(L)$ is
  the number of positive divisors of $L$, whereas $\tau(\chi)$ below
  is the primitive Gauss sum; the argument distinguishes the two.
- Write $E_\chi(z,s)=E_{\chi,\chi}(z,s)$ in Young's notation. Its
  nebentypus is trivial, since Young's nebentypus convention is
  $\chi_1\bar\chi_2$.
- Define the $d$ fixed Fourier rows
  $$
  D_{\chi,f}(z,s)=\sum_{u\in(\mathbb Z/g_f\mathbb Z)^\times}
  \chi(-u)E_{1/(uf)}(z,s),\qquad f=qg,\ g\mid L.
  $$
- Let $\mathcal E_\chi(s)=(E_\chi(Bz,s))_{B\mid L}$,
  $D_\chi(s)=(D_{\chi,qg}(z,s))_{g\mid L}$, and define the incoming
  coefficient matrix by $\mathcal E_\chi(s)=C_\chi(s)D_\chi(s)$.
- Empty tensor products, in particular at $N=1$, mean the one-by-one
  identity matrix. The level-one scattering sector is scalar.
- The completion and its scalar functional-equation factor are
  $$
  A_\chi(s)=\frac{(q/\pi)^s\Gamma(s)L(2s,\chi^2)}{\tau(\chi)},
  \qquad a_\chi(s)=\frac{A_{\bar\chi}(1-s)}{A_\chi(s)}.
  $$
  Every displayed identity is meromorphic. A quotient is first used
  away from its exceptional set and then continued; no zero-times-pole
  substitution is made in separated completion factors.

## Proof strategy

Use the fixed finite Fourier basis on cusp residue classes, not the
parameter-dependent oldform basis. Derive its coefficient matrices
prime by prime from Young's actual inversion formula. A determinant
argument and an outside-$N$ Dirichlet coefficient detect a nonreal
square. Once all squares are real, the fixed principal oldform basis
and a constant half-chain sign operator give the exact odd/even
dichotomy. A tensor-product lemma prevents cancellation between primes.

## Dependency map

1. Classical definitions, width-one scalings, incoming coefficients,
   and the functional equation are from
   [Young, arXiv:1710.03624v2](https://arxiv.org/html/1710.03624v2):
   §3.1, §3.2, §5.2, Theorems 6.1 and 7.1, equations (7.2)–(7.3),
   the completion preceding Proposition 4.1, and Proposition 4.2.
   They were directly inspected in the
   [independent source audit](SOURCE_AUDIT.md).
2. The principal all-exponent fixed basis, including its two odd
   central eigenvalues, is proved in
   [the independent oldform proof](../oldform_review/PROOF_PACKAGE.md),
   Steps 2–6. Its proof applies algebraically to any nonzero complex
   argument $X$, paired with $p/X$.
3. The constant phase transforms and the local parity dichotomy are
   proved in [TWIST_PARITY_LEMMA.md](../oldform_review/TWIST_PARITY_LEMMA.md),
   Steps 1–3. That proof and its source-normalization Step 5 were
   independently read and checked against the formula derived below.
4. The imprimitive-square scalar identity used in the determinant
   argument is fully derived in the auxiliary lemma of
   [PROOF_PACKAGE.md](PROOF_PACKAGE.md), using the primitive Dirichlet
   functional equation and missing Euler factors. Its primary scalar
   inputs are [DLMF §25.15](https://dlmf.nist.gov/25.15), equations
   (25.15.2), (25.15.4), and (25.15.5).
5. The general tensor commutation lemma, the determinant obstruction,
   and the assembly over all fixed character rows are proved here.
   They do not rely on numerical tests or a prime-density theorem.

## Proof

### Step 1. The full cusp Fourier decomposition is fixed

At a denominator $f$, every character of the finite group
$(\mathbb Z/g_f\mathbb Z)^\times$ is induced from exactly one
primitive character of conductor $q\mid g_f$. The condition
$q\mid g_f$ is equivalent to $f=qg$ with $g\mid N/q^2$.
The ordinary finite Fourier transform therefore assembles the rows
$D_{\chi,f}$ for all $q,\chi,f$ into one invertible matrix $T$ on
the entire cusp space. Every entry of $T$ is a character value;
none depends on $s$.

This establishes a full coordinate change, including all repeated
denominator classes and all primitive conductors. No character sector
is discarded. Normalizing its rows by their finite norms is optional
and would be another fixed diagonal similarity.

### Step 2. Exact local coefficient factors from Young's inversion

In Young (7.3), put $\chi_1=\chi_2=\chi$, write $L=AB$, and use
summation variables $d_0\mid A$, $e_0\mid B$, $(d_0,e_0)=1$.
The summand's cusp denominator and scalar are
$$
f=qBd_0/e_0,\qquad
\frac{\chi(d_0)\chi(e_0)}{(d_0e_0)^s}
\left(\frac{N}{(qBd_0/e_0,qAe_0/d_0)}\right)^s.
\tag{1}
$$
All valuations, gcd factors and character values in (1) factor
multiplicatively, so $C_\chi(s)$ is a tensor product over primes
dividing $N$. We now identify each factor without changing coordinates.

Fix such a prime $p$, put $a=v_p(q)$, $e=v_p(L)$, and index local
rows and columns by $b=v_p(B)$ and $k=v_p(f/q)$, both from $0$ to $e$.
The coprimality condition on $d_0,e_0$ forces their two valuations
to be $\max(k-b,0)$ and $\max(b-k,0)$, respectively.

If $a>0$, the primitive character vanishes on $p$. Thus a term
survives only when $b=k$, and the local coefficient matrix is
$$
C_{\chi,p}(s)=
\operatorname{diag}_{0\le b\le e}
 p^{s(a+\max(b,e-b))}.
\tag{2}
$$
It is independent of the character's nonzero values, and agrees for
$\chi$ and $\bar\chi$.

If $a=0$, set $c=\chi(p)$, a nonzero root of unity. The local factor is
$$
C_{\chi,p}(s)_{b,k}
=c^{|b-k|}p^{s(\max(k,e-k)-|b-k|)}
=\bigl(T_e(cp^{-s})\operatorname{diag}_k
 p^{s\max(k,e-k)}\bigr)_{b,k},
\tag{3}
$$
where $T_e(z)_{b,k}=z^{|b-k|}$. In particular,
$$
C_\chi(s)=\bigotimes_{p\mid N}C_{\chi,p}(s).
\tag{4}
$$
Descending row elimination in $T_e(z)$ gives
$\det T_e(z)=(1-z^2)^e$. Hence (2)–(4) are generically invertible.
They also provide a direct applicability check of the independent
oldform review: its real-sign and imaginary-phase matrices are exactly
the actual unramified local factors, with no omitted cusp-width powers.

### Step 3. Functional equations give fixed paired scattering blocks

Young Proposition 4.2 applies to each oldform label $B$ separately:
$$
A_\chi(s)\mathcal E_\chi(s)
=A_{\bar\chi}(1-s)\mathcal E_{\bar\chi}(1-s).
$$
Set
$$
U_\chi(s)=C_\chi(s)^{-1}C_{\bar\chi}(1-s).
$$
In the fixed Fourier coordinates this becomes
$$
D_\chi(s)=a_\chi(s)U_\chi(s)D_{\bar\chi}(1-s).
\tag{5}
$$
Comparing $y^{1-s}$ coefficients at every width-one cusp proves that
(5) is the actual corresponding row block of $T\Phi_N(s)T^{-1}$.
For $\chi\ne\bar\chi$, the two conjugate characters therefore give
the fixed paired block
$$
\mathcal B_\chi(s)=
\begin{pmatrix}
0&a_\chi(s)U_\chi(s)\\
a_{\bar\chi}(s)U_{\bar\chi}(s)&0
\end{pmatrix}.
\tag{6}
$$
For $\chi=\bar\chi$, there is the single block
$a_\chi(s)C_\chi(s)^{-1}C_\chi(1-s)$, not two artificial copies.
Step 1 shows that these blocks exhaust the cusp space.

### Step 4. A nonreal square cannot be hidden by oldform factors

Suppose the whole family commutes and fix $\chi$ with
$\eta=\chi^2$ nonreal. Then $\chi\ne\bar\chi$. The upper-left
block of the commutator of (6) implies
$$
(a_\chi(s)U_\chi(s))(a_{\bar\chi}(t)U_{\bar\chi}(t))
=(a_\chi(t)U_\chi(t))(a_{\bar\chi}(s)U_{\bar\chi}(s)).
$$
Taking determinants and fixing a generic regular $t$ makes
$$
\Delta_\chi(s)=
\left(\frac{a_\chi(s)}{a_{\bar\chi}(s)}\right)^d
\frac{\det C_{\bar\chi}(s)\det C_{\bar\chi}(1-s)}
 {\det C_\chi(s)\det C_\chi(1-s)}
\tag{7}
$$
a constant meromorphic function. Generic invertibility and nonzero
scalar factors justify all divisions; the determinant identity then
continues meromorphically.

Let $\xi$ of conductor $r$ be the primitive character inducing $\eta$,
and put $P=\{p:p\mid q,\ p\nmid r\}$. The scalar calculation in the
minimal-level auxiliary lemma gives a nonzero constant $K_\chi$ with
$$
\frac{a_\chi(s)}{a_{\bar\chi}(s)}
=K_\chi\frac{H_\xi(s)}{H_{\bar\xi}(s)},
\qquad
H_\xi(s)=
\prod_{p\nmid q}\frac{1-\xi(p)p^{-2s}}{1-\xi(p)p^{1-2s}}
\prod_{p\in P}\frac{1-\xi(p)p^{2-2s}}{1-\xi(p)p^{1-2s}}.
\tag{8}
$$
The extra factor $q^{1-2s}$ in the minimal-level coefficient cancels
from the ratio, so (8) applies exactly to the factors in (7).
Importantly, (8) retains the Euler factors missing from the possibly
imprimitive square; primitivity of $\chi$ does not imply primitivity
of $\chi^2$.

The determinant of a tensor factor occurs in (4) to the power
$d/(e_p+1)$. Ramified diagonal factors cancel between the numerator
and denominator of (7). For an unramified $p$, put
$c_p=\chi(p)$ and $n_p=e_pd/(e_p+1)$, an integer. Formula (3)
shows that its determinant-ratio contribution is
$$
\left[
\frac{(1-\bar c_p^2p^{-2s})(1-\bar c_p^2p^{2s-2})}
 {(1-c_p^2p^{-2s})(1-c_p^2p^{2s-2})}
\right]^{n_p}.
$$
Since $|c_p|=1$, removing a nonzero constant from this expression
leaves, with $z=p^{-2s}$,
$$
\left[
\frac{(1-\bar c_p^2z)(1-c_p^2p^2z)}
 {(1-c_p^2z)(1-\bar c_p^2p^2z)}
\right]^{n_p}.
\tag{9}
$$
The finite product $F_\chi(s)$ of (9) is an Euler rational function
supported only at primes dividing $N$, with constant term $1$.
Consequently (7) is a nonzero constant times
$$
\left(\frac{H_\xi(s)}{H_{\bar\xi}(s)}\right)^dF_\chi(s).
\tag{10}
$$

All factors in (10) have absolutely convergent Dirichlet expansions
in $n^{-2s}$ for $\operatorname{Re}s>1$, and the expression tends to
$1$ as real $s\to+\infty$. Since it is constant, it must be $1$.
For a prime $\ell\nmid N$, its coefficient at $\ell^{-2s}$ is
$$
d(\ell-1)\bigl(\xi(\ell)-\bar\xi(\ell)\bigr).
\tag{11}
$$
Finite-prime factors (9) contribute nothing to this coefficient.
Uniqueness of absolutely convergent Dirichlet series forces (11) to
vanish for every $\ell\nmid N$.

To see why this is impossible without any prime-density input, choose
a unit residue $a$ modulo $q$ with $\eta(a)$ nonreal. By the Chinese
remainder theorem choose a positive integer $n$ satisfying
$$
n\equiv a\pmod q,\qquad
n\equiv1\pmod{\prod_{p\mid N,\ p\nmid q}p}.
$$
Then $(n,N)=1$ and $\eta(n)$ is nonreal. At least one prime factor
$\ell$ of $n$ must have $\eta(\ell)=\xi(\ell)$ nonreal, since
a product of real character values is real. This contradicts (11).
Thus pairwise commutativity forces the first clause of (C) for every
primitive conductor, at every level.

### Step 5. A tensor commutation lemma

We record a general elementary fact to exclude cancellation among
the remaining local matrix factors. Suppose $A_1(s),\ldots,A_h(s)$
are meromorphic matrix families, all generically invertible, and
$A(s)=\bigotimes_jA_j(s)$. Then $A(s)$ is pairwise commuting if
and only if each $A_j(s)$ is pairwise commuting.

Only necessity needs proof. Work near a parameter $s_0$ where all
matrices are holomorphic and invertible. If the tensor family commutes,
then for nearby $s,t$,
$$
\bigotimes_jR_j(s,t)=I,
\qquad
R_j(s,t)=A_j(s)A_j(t)\bigl(A_j(t)A_j(s)\bigr)^{-1}.
$$
Taking traces makes every $\operatorname{tr}R_j$ nonzero, since their
product is the nonzero dimension of the tensor space. Partial traces
then show that each $R_j$ is scalar. Its determinant is $1$, so its
scalar is a root of unity of order dividing $\dim A_j$. On a connected
small neighborhood of $(s_0,s_0)$ this scalar is continuous with values
in a finite set, and hence constant. At $(s_0,s_0)$ it is $1$.
Thus every local commutator vanishes on an open set, and therefore
identically by meromorphic continuation. The converse follows directly
from multiplication of tensor products. ∎

### Step 6. Real-square sectors reduce by constant similarities

Assume now that $\chi^2$ is real. If $\chi$ is real, every unramified
value $\chi(p)$ is $\pm1$. Formula (3) is then a fixed sign-conjugate
of the principal incoming matrix, while (2) is diagonal. The principal
fixed-basis theorem gives a commuting tensor family in its single
character sector, for arbitrary $L$.

Otherwise $\chi$ has order four. Because the two square $L$-functions
are identical, $a_\chi(s)$ and $a_{\bar\chi}(s)$ have a common
nonzero meromorphic scalar and the reciprocal constant factors
$\tau(\chi)/\tau(\bar\chi)$ and $\tau(\bar\chi)/\tau(\chi)$.
One constant block-diagonal similarity removes these factors from (6).

For unramified $p$, set
$$
J_p=\operatorname{diag}_{0\le b\le e_p}
 \bigl(\chi(p)^2\bigr)^b;
$$
for ramified $p$ put $J_p=I$. Since the square values on units are
$\pm1$, equations (2)–(3) give
$C_{\bar\chi,p}(s)=J_pC_{\chi,p}(s)J_p$. Hence, writing
$J=\bigotimes_pJ_p$,
$$
U_{\bar\chi}(s)=JU_\chi(s)J.
$$
A constant similarity by $\operatorname{diag}(I,J)$ and then a
constant two-block Walsh transform reduce (6), up to its common scalar,
to two copies with opposite signs of
$$
\mathcal A_\chi(s)=U_\chi(s)J
=C_\chi(s)^{-1}JC_\chi(1-s)
=\bigotimes_{p\mid N}\mathcal A_{\chi,p}(s),
\tag{12}
$$
where $\mathcal A_{\chi,p}(s)=
C_{\chi,p}(s)^{-1}J_pC_{\chi,p}(1-s)$.
Every transformation is independent of $s$. Every local factor is
generically invertible by Step 2.

### Step 7. The exact local obstruction is odd exponent plus imaginary value

Ramified factors in (12) are diagonal. For an unramified factor, write
$c=\chi(p)$, $e=e_p$, $x=p^s$, and
$r_k=\max(k,e-k)$. Let $C(X)_{b,k}=X^{r_k-|b-k|}$ be the principal
matrix. Define the constant diagonal matrices
$$
H=\operatorname{diag}(c^{r_k}),\qquad
F=\operatorname{diag}((c^2)^{r_k+k}),\qquad X=x/c.
$$
The explicit phase calculation in the independent parity lemma gives
$$
\mathcal A_{\chi,p}(s)
=H^{-1}P_{p,e}(X)F H,
\qquad P_{p,e}(X)=C(X)^{-1}C(p/X).
\tag{13}
$$
Its derivation uses only the entrywise identities
$C_c(x)=C(x/c)H$ and
$J_pC(y/c)=C(c^2y/c)F$, with $y=p/x$; their paired arguments
satisfy $(x/c)(c^2y/c)=p$.

If $c=\pm1$, then $F=I$. If $c=\pm i$ and $e$ is even, then
$r_k+k$ is even for every $k$, so again $F=I$. In both cases the
fixed principal basis proves commutativity of (13).

If $c=\pm i$ and $e=2m+1$, $F$ is $-I$ on the left half and
$+I$ on the right half. In the principal fixed basis, it preserves
each left/right difference eigenline and exchanges the two central
vectors with a minus sign. On their fixed span, $P_{p,e}(X)F$ is
$$
\begin{pmatrix}0&-\lambda_+(X)\\-\lambda_-(X)&0\end{pmatrix},
\qquad
\lambda_\pm(X)=\left(\frac{p}{X^2}\right)^m
\frac{p/X\pm1}{X\pm1}.
$$
The off-diagonal ratio is
$$
\rho_p(X)=\frac{(p+X)(X-1)}{(p-X)(X+1)}.
\tag{14}
$$
It is nonconstant for every prime $p$: a constant value would be
$-1$ by the quadratic coefficients, and the linear coefficients
would then force $p=1$. Thus this fixed two-dimensional family is
noncommuting. Its meromorphic entries are not identically zero, so
the usual two-by-two ratio test applies.

Combining (12), Step 5 and (13)–(14), a quartic paired sector commutes
exactly when it has no unramified prime with imaginary $\chi(p)$
and odd $e_p$. For $p\nmid q$, $e_p=v_p(N)$, which is precisely
the second clause of (C). This also shows why two different bad primes
cannot cancel each other's noncommutativity.

### Step 8. Assemble the complete equivalence and include regular exceptional values

If the whole scattering family commutes, Step 4 forces real squares
for all primitive conductors. Steps 6–7 then force the second clause
of (C) in every quartic sector; real sectors satisfy it automatically.

Conversely, assume (C). Each real sector commutes by Step 6. In each
quartic sector all local factors in (12) commute by Step 7, and hence
their tensor product and the fixed paired block commute. The fixed
Fourier decomposition in Steps 1 and 3 exhausts the cusp space, so
the full scattering family commutes.

These statements first hold on open sets where the displayed inverses
and scalar quotients are defined. Each resulting commutator identity
is a meromorphic matrix identity in $(s,t)$. At any pair of regular
values of the actual full scattering matrix it therefore holds by
continuation, including parameters where an intermediate formula has
a removable singularity. Transposing a scattering convention also
preserves whether a commutator vanishes. This proves the claim. ∎

## Corrections: both earlier conjectures and the level-100 boundary

The condition without any extra-prime qualification is false at
$N=50$, as the immutable counterexample package proves exactly.

The first repair demanded a real value at every unramified divisor
prime, including even exponents. At $N=100$ the only actual primitive
conductors with $q^2\mid100$ are $1$ and $5$: characters modulo $2$
are induced from modulus $1$, and the reduction of unit groups from
modulus $10$ to $5$ is an isomorphism, so modulus $10$ adds none.
All conductor-$5$ characters have order dividing four. The only
unramified prime in those sectors is $2$, with exponent $2$. Thus
(C) holds and the full $\Phi_{100}(s)$ family commutes, even though
the quartic character has $\chi(2)=i$ and violates the first repair.
This conclusion also follows directly from the even case of (13)
and the principal/real-sector proof, without relying on a finite test.

## Open risks and scientific disposition

The theorem here is the parity-corrected character criterion at all
levels; no elementary congruence list is silently substituted for it.
The coordinator separately owns the elementary reformulation and the
closest-source investigation. Both independent oldform proof files
are explicit mathematical dependencies, not labels for unproved steps.

No mathematical gap is identified in this proof after checking those
dependencies and the normalization against Young. Independent review
of this assembled proof remains appropriate before promoting its status
elsewhere. All ingredients after the classical scattering formulas are
finite-dimensional algebra and Dirichlet-series uniqueness; this is
not by itself evidence of literature novelty or paper-level substance.

The object remains spectral scattering with no autonomous source clock.
No target Euler-factor dictionary, root number, zero/divisor realization,
or Hilbert–Pólya bridge is supplied. No manuscript, admission, evaluation,
Git mutation, paid model, GPU job, or external upload is authorized or
performed by this proof package.
