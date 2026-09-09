# R9 A1: the general quadratic norm-one obstruction

2026-09-10 UTC. One bounded proof mechanism inside MS6; no new contract.

## Frozen exact question

For every odd prime $p$, let $k=\overline{\mathbb F}_p$. For every
$c\in k$ put $f(x)=x^2+c$. Let $w\in k(x)^\times$ satisfy the exact
norm-one identity

$$w(x)w(-x)=1.$$

Suppose that, except for finitely many ordinary primitive $f$-cycles,
each cycle avoids the zeros and poles of $w$ and has product
$\prod_{x\in O}w(x)=1$. Does this imply $w=1$?
All ordinary periods, including multiples of $p$, are retained.
The clock is one application of $f$; cofiniteness is among all native
primitive cycles, not within a finite field or a merged return divisor.

**Initial status: NOT CURRENTLY JUSTIFIED.** The required success is
a proof for all stated rational $w,c,p$, or an actual cofinite-product
counterexample. A proved auxiliary criterion does not close this
question or general MS6. Products of balanced atoms can cancel on a
cycle; no individual-atom (CP) assertion may be inferred.

## Single selected mechanism and exact inputs

Use the cyclic quadratic quotient
$k[X_0,\ldots,X_{n-1}]/(X_i^2+c-X_{i+1})$ (indices modulo $n$),
clear the numerator and denominator of the entire $w$, and test its
cofinite product identity with a finite-exception annihilator and the
Jacobian. The obligation is a genuine coefficient-separation statement
for the simultaneous balanced divisor, not separate detection of its
atoms. If this cyclic coefficient mechanism does not provide separation,
record its exact remaining implication and stop the bounded attempt.

The actual accepted R7 A2 Sections 3–4 were read: norm-one normalization
reduces the quadratic part of MS6 to this question, and a nonconstant
norm-one function has non-torsion class. Neither is an existence proof.
The accepted R7 single-atom reduction remains read-only. The new R8
critical-atom report is a candidate under whole-proof review, not an
admitted input until its precise coefficient passage has been read and
its review status checked.

Only this report is writable. No mathematical execution, new/nested
agent, external model/API upload, GPU, Git, shared/old-file, manuscript
or PDF action is allocated. At most two targeted source batches may
be used if necessary. The current proof-writer workflow requires a
complete proof or an explicit unchanged gap, not a narrowed substitute.

## 1. Outcome of the bounded attempt

**The original question remains NOT CURRENTLY JUSTIFIED.** No genuine
(CP) counterexample is obtained. The selected coefficient mechanism
does produce a complete auxiliary theorem: for a fixed finite-exception
annihilator, all cyclic coefficient identities admit an explicit finite
matrix-word certificate, with logarithmic dependence on the degree of
the annihilator. The missing separation implication is stated in
Section 8; neither similarity nor a characteristic-zero trace theorem
is substituted for it.

The auxiliary theorem handles the whole rational numerator and
denominator, with every root multiplicity retained. In particular it
does not assume that (CP) for an atom power implies (CP) for the atom.

## 2. Exact simultaneous normalization

Write a norm-one function in reduced form

$$w(X)=\eta\frac{A(X)}{B(X)},\qquad
\eta\in\{1,-1\},\qquad
B(X)=(-1)^m A(-X), \tag{2.1}$$

where $A,B$ are monic, relatively prime polynomials of the same degree
$m\ge0$, and $A(0)B(0)\ne0$. Here is the justification. The norm-one
identity gives opposite divisor orders at $a$ and $-a$, and gives
zero order at the fixed points $0,\infty$ of the sign involution.
Thus numerator and denominator have equal degree, no root at zero,
and their root divisors are negatives of one another under the sign
involution. Monicity determines $B$ as displayed; evaluating at
infinity gives $\eta^2=1$. Odd characteristic makes its two possible
values $1,-1$.

For $m=0$, the accepted [R6 A2, Section 4, Corollary 4.3
(using Lemmas 4.1–4.2)](../../continuation_round6/a2_multiplicative_saturation/REPORT.md)
gives (CP) only for $\eta=1$. For $m>0$, the accepted
[R7 A2, Sections 3–4, Theorem 3.1 and Proposition 4.1](../../continuation_round7/a2_multiplicative_existence/REPORT.md)
says that $[w]$ is non-torsion. This is not a proof that (CP) fails. The root
multiplicities in $A$ may be arbitrary positive integers; none is
replaced by its squarefree part, by its residue modulo $p$, or by an
exponent-one atom.

Put

$$\mathcal A_n=k[X_0,\ldots,X_{n-1}]/
(X_i^2+c-X_{i+1}:i\bmod n),\qquad
P_n=\prod_{i=0}^{n-1}X_i.$$

For a nonzero polynomial $S\in k[X]$, define

$$U_n(S,A,B,\eta)=
S(X_0)(2^nP_n-1)
\left(\eta^n\prod_{i=0}^{n-1}A(X_i)
      -\prod_{i=0}^{n-1}B(X_i)\right)\in\mathcal A_n. \tag{2.2}$$

All powers $2^n$ and $\eta^n$ in (2.2) are scalar powers; $f^{\circ n}$
below denotes the ordinary iterate. Define $\ell=\deg S$ and

$$k_S=\begin{cases}
0,&\ell=0,\\
\lfloor\log_2\ell\rfloor+1,&\ell\ge1.
\end{cases} \tag{2.3}$$

## 3. Auxiliary finite-word theorem

**Theorem.** For every frozen $p,c,w$ in (2.1), and every nonzero
$S\in k[X]$, the following are equivalent:

1. $U_n(S,A,B,\eta)=0$ in $\mathcal A_n$ for every integer $n\ge1$;
2. the same identities hold for

   $$1\le n\le k_S+16(m+2)^2. \tag{3.1}$$

Each identity can be tested exactly by the finite matrices in Section 5
and all binary words of its length. No mathematical execution or
enumeration of these tests is performed here. The theorem is a finite
certificate for these annihilation identities, not a finite certificate
for (CP), and it gives no bound on the degree of an exceptional
polynomial $S$ supplied by a hypothetical (CP) assumption.

The dependency map is: the squarefree basis gives a nondegenerate
coefficient pairing; the finite residue expansion gives matrix-word
contractions; one distinguished high-degree site loses its excess
state size after $k_S$ bulk sites; a finite matrix-algebra span bounds
all remaining word lengths. These statements are proved next.

## 4. (CP) supplies the annihilation identities, but not conversely

Let $F_n(x)=f^{\circ n}(x)-x$, a monic polynomial of degree $2^n$.
There is an isomorphism

$$\mathcal A_n\simeq k[x]/(F_n),\qquad
X_i\longmapsto f^{\circ i}(x). \tag{4.1}$$

The defining relations determine all $X_i$ from $X_0$ and then give
$F_n(X_0)=0$, which proves both directions of the isomorphism.
Replacing a square by $X_{i+1}-c$ lowers total degree, so squarefree
monomials span $\mathcal A_n$. Their images in (4.1) are monic of
the distinct degrees $\sum_i\epsilon_i2^i$, $\epsilon_i\in\{0,1\}$,
between zero and $2^n-1$. They are linearly independent and form a
basis, for every $n\ge1$.

Assume (CP). Let $S$ vanish at every point of every exceptional
cycle and at every zero or pole of $w$; a finite product of the
corresponding linear factors is a nonzero such polynomial. At a
periodic point of least period $r\mid n$ outside this finite set,
the $n$-step product of $w$ is its ordinary $r$-cycle product raised
to the integer $n/r$, and hence is one. The entire polynomial

$$S(X_0)\left(\eta^n\prod_i A(X_i)-\prod_i B(X_i)\right)$$

therefore vanishes at every distinct root of $F_n$. At a root of
multiplicity $e$, $F_n'$ has order at least $e-1$, including when
$p\mid e$. Multiplying a polynomial vanishing at the root by
$F_n'$ gives order at least $e$. Consequently $F_n$ divides this
product by $F_n'$. The derivative chain rule gives
$F_n'=2^nP_n-1$ in (4.1), proving

$$\mathrm{(CP)}\Longrightarrow
\text{there exists }S\ne0\text{ such that }U_n=0
\text{ for every }n\ge1. \tag{4.2}$$

This uses the products of whole primitive cycles, not products
merged between different cycles.

Define $L_n:\mathcal A_n\to k$ to be the coefficient of $P_n$
in the squarefree basis. Under (4.1), this is the coefficient of
$x^{2^n-1}$ in the degree-below-$2^n$ remainder: $P_n$ is monic
of that degree, and every other basis element has lower degree.
The pairing $(u,v)\mapsto L_n(uv)$ is nondegenerate. In fact, if
the nonzero remainder of $u$ has degree $d$ and leading coefficient
$a$, multiplying it by $x^{2^n-1-d}$ gives degree $2^n-1$ with
leading coefficient $a\ne0$, without any reduction. Since the
squarefree monomials span, it follows that

$$U_n=0\quad\Longleftrightarrow\quad
L_n\left(\prod_iX_i^{\epsilon_i}U_n\right)=0
\text{ for every }\epsilon\in\{0,1\}^n. \tag{4.3}$$

This is a Frobenius pairing statement for the actual nonreduced
algebra, not a point-count formula.

## 5. Finite matrices for every coefficient word

For a polynomial $H$ consider the finite coefficient extractor

$$\mathscr R_n(H)=
[X_0^{-1}\cdots X_{n-1}^{-1}]
H\prod_i\left(
\sum_{q_i\ge0}X_i^{-2q_i-2}(X_{i+1}-c)^{q_i}
\right). \tag{5.1}$$

For an input monomial of total degree $D$, a contributing term,
choosing power $r_i\le q_i$ from the $i$th binomial, has

$$D-n=2\sum_iq_i-\sum_ir_i\ge\sum_iq_i.$$

Thus only finitely many $q_i$ contribute. This is an algebraic
coefficient calculation, not an assertion of analytic convergence.
Multiplication by a defining relation cancels its geometric series;
without that series no remaining factor has a negative power of
the corresponding $X_i$. Hence the extractor annihilates the ideal.
It is one on $P_n$ and zero on every lower-degree squarefree monomial,
by the displayed degree bound. It descends to $\mathcal A_n$ and
equals $L_n$.

For $h(X)=\sum_j h_jX^j$, with $h_j=0$ outside its degree range,
define

$$T_h(r,s)=\sum_{q\ge s}
\binom qs(-c)^{q-s}h_{2q+1-r}. \tag{5.2}$$

Every sum is finite. For a factored input $\prod_i h_i(X_i)$,
the exponent condition in (5.1) is
$j_i=2q_i+1-r_{i-1}$. Summing the cyclic indices therefore gives

$$L_n\left(\prod_i h_i(X_i)\right)
=\sum_{r_0,\ldots,r_{n-1}\ge0}
\prod_i T_{h_i}(r_{i-1},r_i),\qquad r_{-1}=r_{n-1}. \tag{5.3}$$

A nonzero transition from $r$ to $s$ satisfies

$$2s\le r+\deg h-1. \tag{5.4}$$

At a maximal cyclic index, (5.4) implies that this index is at
most $\max_i\deg h_i-1$. For the inputs below, it is therefore
enough to use the common range

$$0\le r,s\le R:=m+\ell+1. \tag{5.5}$$

Formula (5.3) is then the trace of the product of these finite
matrices, with no omitted closed carry.

For $h=A$ or $B$, $j\in\{0,1\}$, and $\epsilon\in\{0,1\}$, put

$$C^h_{j,\epsilon}=T_{X^{j+\epsilon}h},\qquad
D^h_{j,\epsilon}=T_{S X^{j+\epsilon}h},$$

using the range (5.5). Define block-diagonal matrices

$$\mathsf M_\epsilon=
\operatorname{diag}\left(
2\eta C^A_{1,\epsilon},\ \eta C^A_{0,\epsilon},\
2C^B_{1,\epsilon},\ C^B_{0,\epsilon}\right), \tag{5.6}$$

$$\mathsf B_\epsilon=
\operatorname{diag}\left(
2\eta D^A_{1,\epsilon},\ -\eta D^A_{0,\epsilon},\
-2D^B_{1,\epsilon},\ D^B_{0,\epsilon}\right). \tag{5.7}$$

For every binary word $\epsilon_0\cdots\epsilon_{n-1}$,
expansion of (2.2) and (5.3) gives the exact identity

$$L_n\left(\prod_iX_i^{\epsilon_i}U_n\right)
=\operatorname{tr}\left(
\mathsf B_{\epsilon_0}
\mathsf M_{\epsilon_1}\cdots
\mathsf M_{\epsilon_{n-1}}\right). \tag{5.8}$$

For $n=1$ the product following $\mathsf B$ is the identity.
The signs in (5.7) occur only at the distinguished site, so (5.8)
retains $\eta^n$, not an incorrect phase independent of the period.

## 6. Logarithmic contraction of the exceptional site

Away from the distinguished $S$-site, the degree is at most $m+2$.
Thus every bulk transition satisfies

$$s\le\frac{r+m+1}{2}. \tag{6.1}$$

The indices $0,\ldots,m+1$ form a closed range under bulk
transitions. Starting at any index at most $R=m+\ell+1$, after
$j$ bulk transitions every possible index is at most

$$m+1+\frac{\ell}{2^j}. \tag{6.2}$$

If $\ell=0$ it is already in the closed range. Otherwise
$2^{k_S}>\ell$, so after $k_S$ transitions its integer index is
at most $m+1$. This bounds all paths, including paths whose weights
cancel or vanish in characteristic $p$.

Let $\mathsf M^0_0,\mathsf M^0_1$ be the restrictions of (5.6)
to these closed ranges in its four blocks. Their common dimension is

$$v_0=4(m+2). \tag{6.3}$$

For $n\ge k_S+1$, every cyclic contribution to (5.8) has its input
at the $S$-site in the closed range, since the preceding $n-1$
sites include at least $k_S$ bulk transitions. Its output after the
first $k_S$ bulk sites is also in that range. Let
$\mathsf E_{\epsilon_0\ldots\epsilon_{k_S}}$ be the restriction
to closed-range rows and columns of

$$\mathsf B_{\epsilon_0}\mathsf M_{\epsilon_1}
\cdots\mathsf M_{\epsilon_{k_S}}.$$

Intermediate large states in this prefix are still included. The
remaining bulk path stays in the closed range. Consequently (5.8)
becomes

$$\operatorname{tr}\left(
\mathsf E_{\epsilon_0\ldots\epsilon_{k_S}}
\mathsf M^0_{\epsilon_{k_S+1}}\cdots
\mathsf M^0_{\epsilon_{n-1}}\right). \tag{6.4}$$

This compression is only of the long bulk; it does not discard the
large-degree exceptional polynomial or replace it by its leading term.

## 7. Proof of the finite-word bound

For any two $v_0$-by-$v_0$ matrices $M_0,M_1$ over a field, let
$W_j$ be the span of their word products of length at most $j$,
including the empty product. Then

$$W_{j+1}=W_j+W_jM_0+W_jM_1.$$

If $W_{j+1}=W_j$, the space is stable under right multiplication
by both letters and already contains every word product. Otherwise
its dimension strictly increases. Since $\dim W_0=1$ and the
ambient matrix space has dimension $v_0^2$, all word products are
spanned by words of length at most $v_0^2-1$.

Apply this fact to the two matrices in (6.3). For every fixed prefix
in (6.4), its trace functional vanishes on every tail word if and
only if it vanishes on tail words of length at most $v_0^2-1$.
Those contractions occur at lengths

$$k_S+1\le n\le k_S+v_0^2.
$$

Together with the finitely many lengths $1\le n\le k_S$, they
are exactly covered by (3.1). By the nondegenerate pairing (4.3),
vanishing of all these contractions gives $U_n=0$ for every $n$.
The reverse implication is immediate by restricting the lengths.
This proves the auxiliary theorem. $\square$

The argument uses only linear spans of matrix words and trace as a
specified linear functional. It makes no claim that traces determine
representations, semisimplifications, or rational transfers.

## 8. Exact missing separation and two forbidden inferences

The mechanism has established the following necessary interface:

$$\mathrm{(CP)}\Longrightarrow
\exists S\ne0\text{ satisfying the finite identities (3.1)}. \tag{8.1}$$

To finish the original question by this mechanism, one would need a
new separation theorem ruling out such an annihilator for every
nonconstant norm-one $w$, or a different justified consequence of
(CP) within this same coefficient system that rules it out. No such
theorem is proved here. The existence and degree of $S$ encode an
unknown finite exceptional set; the finite-word theorem does not
bound that set from the divisor of $w$.

There are two specific reasons not to promote (8.1) to a solution.

1. **Jacobian loss at wild roots.** Multiplication by $F_n'$ is a
   valid forward annihilator, not an invertible passage to ordinary
   points. If a root has multiplicity divisible by $p$, its derivative
   may vanish on the whole local factor. For an actual quadratic
   illustration, in characteristic three, $f=x^2$ has

   $$F_2=x^4-x=x(x-1)^3,\qquad F_2'=x^3-1=(x-1)^3.$$

   Thus $F_2'$ is zero in the local factor $k[x]/((x-1)^3)$, even
   though a tested function need not vanish at the ordinary point
   $1$. This example concerns the annihilator at one return level;
   it is not asserted to refute the all-level condition in (8.1).
   No reverse implication from all the $U_n$ identities to (CP)
   has been proved.

2. **Trace ambiguity in characteristic $p$.** The direct sum of
   $p$ copies of any matrix representation has trace zero on every
   word. Equality of ordinary trace characters therefore cannot
   be used to identify semisimple representations with their integer
   multiplicities, much less to construct a rational native transfer.
   A characteristic-zero matrix-product or trace-uniqueness theorem
   would not repair this step without additional work. Even an
   independently proved matrix equivalence would still require a
   theorem connecting its gauge to $h\circ f/h$.

The R8 exponent-one critical-atom proof cannot fill either gap.
In particular infinitely many products different from one do not
exclude all of them lying in a fixed finite group of roots of unity;
raising an atom to a prime-to-$p$ power could conceal those values.
The present matrices retain all exponents and all simultaneous
numerator/denominator terms, but retaining them is not yet a
separation proof.

## 9. Source subtraction, review status, and freeze

The accepted R7 A2 finite-divisor criterion and norm-one normalization
were actually read in Sections 3–4. They supply the exact question
and the non-torsion obstruction, not (CP)-to-existence. The complete
526-line corrected R8 A2 author report was read, including its finite
residue extractor, cubic/quartic coefficients and prime-period lemma.
Its frozen hash was
`e3fcd6eef80df88ed1d0b5b4633e6d6e1003582bf0b4022c86303df166f278c3`.
The root subsequently reported E5's whole-proof PASS in a 429-line review
report on the final 526-line R8 author proof; E2 supplied a separate
448-line coefficient-only review report. The root has accepted the R8
critical-atom theorem as an auxiliary result, not as paper admission.
No R8 critical-atom
coefficient or prime-selection conclusion is needed in the auxiliary
theorem here: the general-$c$ extractor and all state bounds are
proved again at their required scope.

The top-coefficient/long-carry idea also uses the accepted PC424-L
cyclic basis as an interface, not its additive kernel theorem as a
multiplicative existence assertion. The coordinator independently
suggested the all-word Frobenius pairing and warned about both wild
roots and characteristic-$p$ trace multiplicities; these have been
checked and retained explicitly above.

No external theorem was required and no source-query batch was used.
No mathematical program, parameter census, new/nested agent, external
model/API upload, GPU, Git, old/shared-file, manuscript or PDF action
was performed. All matrices and bounds above are hand derivations,
not executed certificates. Only this allocated report was written.

**Frozen boundary:** the finite-word annihilation theorem is proved
as an auxiliary result. The full quadratic norm-one (CP) implication,
the treatment of arbitrary simultaneous atom multiplicities, and
general MS6 remain **NOT CURRENTLY JUSTIFIED**. No fifth contract or
new paper is claimed, and no wider parameter census or second
mechanism is opened by this report.
