# Two literal coupling attempts: proofs and hard subtraction

Author: `/root/round211_rational_scout`, 2026-09-08 UTC.
All proofs below are author deductions. No finite search output is used as
an induction hypothesis, and no scientific program was run.

## Claim, status, assumptions, and dependencies

The prospective claim is a full-carrier all-parameter temporal/recurrent
theorem together with a materially separate evaluated inverse/fibre/extremal
theorem after known mechanisms are deducted.

**Status of that two-axis admission claim: NOT CURRENTLY JUSTIFIED for both
QSC and CAC.** The weaker mathematical propositions explicitly stated below
are **PROVABLE AS STATED**. All fields have odd cardinality $q$, and matrix
size is exactly two. Matrix products are ordered products, not commutative
scalar products. A tail is the first entrance time into the recurrent set.

Dependency map:

1. QSC inverse: split the zero-denominator source from regular sources;
   solve one affine-linear equation; count impossible targets and maxima.
2. QSC subtraction: quadratic-root Cayley coordinates give the classical
   Fibonacci monomial map only on the rational domain; the literal zero
   reset becomes an identity-deletion rule on a cyclic group. No recurrence
   classification of that modified rule is claimed.
3. CAC time: polarized two-by-two Cayley–Hamilton and cyclic trace imply
   orthogonality constraints; these force the third second-coordinate to
   vanish; an explicit integral pair proves sharpness in every odd field.
4. CAC inverse: invertible output mixing reduces exactly to prescribed
   $AB$ and $BA$; fixed-$A$ linear fibres give a generic unique zero
   maximum; classical mutually-annihilating counts evaluate that maximum.

## 1. QSC: all-target inverse, but an unclosed reset recurrence

Use the full literal $S_c$ of INTAKE.md. Write
$N_c(u,v)=|S_c^{-1}(u,v)|$ and let $\mathbf1_E$ denote the indicator of $E$.

### Proposition 1: exact sources and fibre law

For every target $(u,v)\in\mathbb F_q^2$,
$$N_c(u,v)=\mathbf1_{v=0}+
\begin{cases}
\mathbf1_{u^2\ne c},&u\ne v,\\
(q-1)\mathbf1_{u^2=c},&u=v.
\end{cases}$$

The first summand is the unique possible singular source $(-u,u)$.
For $u\ne v$ the regular source, when it exists, is
$$\left(\frac{uv-c}{u-v},u\right).$$
For $u=v$ with $u^2=c$, every $(x,u)$ with $x\ne-u$ is a regular source.

**Proof.** The first output forces $y=u$. If $x=-u$, the defining zero
inverse makes the second output zero, giving exactly the singular term.
For $x\ne-u$, the second equation is equivalent to
$$xu+c=v(x+u),\qquad (u-v)x=uv-c.$$
When $u\ne v$, this has the displayed unique solution, and its denominator
test is
$$x+u=\frac{u^2-c}{u-v}.$$
It is therefore a regular source exactly when $u^2\ne c$. When $u=v$,
the equation reduces to $u^2=c$, independently of $x$. It allows precisely
the $q-1$ values $x\ne-u$ if that condition holds, and none otherwise.
The regular and singular sets are disjoint and exhaust all sources. ∎

### Corollary 2: evaluated image and all maximizing targets

$$|\operatorname{im}S_c|=
\begin{cases}
q^2-2q+2,&c=0,\\
q^2-3q+7,&c\text{ is a nonzero square},\\
q^2-q+1,&c\text{ is a nonsquare}.
\end{cases}$$

If $c=0$, the unique maximum fibre is at $(0,0)$ and has size $q$.
If $c=r^2\ne0$, the maximum is $q-1$ and its only maximizing targets are
$(r,r)$ and $(-r,-r)$. If $c$ is a nonsquare, the maximum is two and its
maximizing targets are precisely $(u,0)$ with $u\ne0$.

**Proof.** For $c=0$, the empty fibres are the $q-1$ nonzero diagonal
targets and the $q-1$ targets $(0,v)$ with $v\ne0$. For $c=r^2\ne0$,
there are $q-3$ nonzero diagonal targets whose coordinate is not a root,
and $2(q-2)$ off-diagonal targets $(u,v)$ with $u\in\{r,-r\}$ and
$v\notin\{0,u\}$. These lists are disjoint and Proposition 1 shows that
there are no other empty fibres. For nonsquare $c$, exactly the $q-1$
nonzero diagonal targets have empty fibres. Subtract from $q^2$.

For $c=0$, every nonexceptional nonempty fibre has size at most two, less
than $q$. For nonzero square $c$ and $q\ge5$, the two root diagonals have
size $q-1>2$, while all other fibres have size at most two. For $q=3$,
the two nonzero field elements are exactly the two roots, so no target
$(u,0)$ with nonzero nonroot $u$ exists; hence the same two root diagonals
are the only size-two fibres. For nonsquare $c$, Proposition 1 gives size
two exactly at the stated targets. ∎

### 1.3 Exact classical adapter and its precise boundary

Let $c=r^2\ne0$ in a splitting field, and set
$$\phi_r(x)=\frac{x-r}{x+r}.$$
On the rational domain where the expressions are defined,
$$\phi_r\!\left(\frac{xy+r^2}{x+y}\right)
=\frac{(x-r)(y-r)}{(x+r)(y+r)}=\phi_r(x)\phi_r(y).$$
Thus $S_c$ is the quadratic secant map and the ordinary rational part is
the Fibonacci monomial update $(a,b)\mapsto(b,ab)$. This is explicitly
present in Bedford–Frigge, Example 4.2; their reciprocal choice of Cayley
coordinate gives the same product identity. The double-root case $c=0$
is, away from zeros, reciprocal-conjugate to the Fibonacci linear map
$(a,b)\mapsto(b,a+b)$. Neither classical rational identity is a new result.

The zero-totalized finite carrier must not be silently identified with that
projective rational system. For $c=r^2\ne0$ in $\mathbb F_q$, the set
$$U=(\mathbb F_q\setminus\{r,-r\})^2$$
is invariant under $S_c$. Indeed a regular second output equals $r$ only
if $(x-r)(y-r)=0$, and equals $-r$ only if $(x+r)(y+r)=0$; the singular
second output is $0$, which is not a root. The map $\phi_r$ identifies
each coordinate of $U$ bijectively with
$\mathbb F_q^*\setminus\{1\}$. Under this bijection the full restricted
literal is
$$H(a,b)=\begin{cases}(b,ab),&ab\ne1,\\(b,-1),&ab=1.\end{cases}$$
To verify the second branch, $ab=1$ is equivalent to $x+y=0$, since
$2r\ne0$; the literal output zero has Cayley coordinate $-1$.

For nonsquare $c$, choose $r\in\mathbb F_{q^2}$ with $r^2=c$.
Then $r^q=-r$, so $\phi_r(x)^q=\phi_r(x)^{-1}$ for every $x\in\mathbb F_q$.
The formula $x=r(1+a)/(1-a)$ shows conversely that every norm-one element
$a\ne1$ gives a unique $x\in\mathbb F_q$: applying Frobenius to the
formula and using $a^q=a^{-1}$ returns $x$. Thus the **whole** carrier in
this nonsplit case is conjugate to the same $H$ on
$(\mu_{q+1}\setminus\{1\})^2$, not to ordinary group multiplication.

Both groups here are cyclic of even order $m=q-1$ or $q+1$. In exponents,
the modified rule is $(i,j)\mapsto(j,i+j)$ modulo $m$ except that the
excluded value $i+j=0$ is replaced by $m/2$. This is an exact reduction,
not an evaluated all-$m$ cycle or tail theorem. The replacement can lie on
recurrent orbits. For example, by direct substitution in $\mathbb F_5$,
$$S_1:(2,0)\longmapsto(0,3)\longmapsto(3,2)\longmapsto(2,0).$$
The third arrow has zero denominator. The three distinct states therefore
form a genuine period-three cycle for the literal totalization. This is a
three-substitution symbolic example, **not an executed finite pilot**.

**Missing obligation.** No all-parameter recurrent set, sharp tail law, or
evaluated cycle census of the identity-deletion reset rule has been proved.
An arbitrary first-return decoder or finite-map cycle search would not
close that obligation. P150's special Lyness boundary has an actual short
stratum chain; that theorem does not transfer to this recurrent reset.
QSC closes `NO_PROMOTION / HOLD_FULL_TEMPORAL_PROOF`. The elementary
complete fibre law does not repair its missing first axis.

## 2. CAC: sharp four-step collapse, but an entirely consumed inverse axis

For $F(A,B)=(C,D)$ set
$$C=[A,B],\qquad D=AB+BA,\qquad t=\operatorname{tr}D,\qquad E=[C,D].$$

### Lemma 3: the required polarized identity

For any two-by-two matrices $X,Y$ over an odd field,
$$XY+YX=(\operatorname{tr}X)Y+(\operatorname{tr}Y)X+
\bigl(\operatorname{tr}(XY)-\operatorname{tr}X\operatorname{tr}Y\bigr)I.$$

**Proof.** Subtract the Cayley–Hamilton equations for $X$ and $Y$ from
that for $X+Y$. Use
$\det(X+Y)-\det X-\det Y=
\operatorname{tr}X\operatorname{tr}Y-\operatorname{tr}(XY)$,
which follows by expanding the four entries of the two determinants.
The remaining degree-two terms are $XY+YX$, giving the identity. ∎

### Proposition 4: exact iterates, recurrent set, and sharp height

For every odd prime power $q$,
$$F^2(A,B)=(E,tC),\qquad
F^3(A,B)=(t[E,C],0),\qquad F^4(A,B)=(0,0).$$
The zero pair is the only recurrent state and the maximum tail is exactly
four for every such $q$. For $h(A,B)$ denoting its tail, the complete
algebraic tests for the nested depth sets are
$$\begin{aligned}
h=0&\iff A=B=0,\\
h\le1&\iff AB=BA=0,\\
h\le2&\iff E=0\ \text{and}\ tC=0,\\
h\le3&\iff t[E,C]=0.
\end{aligned}$$

**Proof.** Cyclic trace gives $\operatorname{tr}C=0$. It also gives
$$\operatorname{tr}(CD)=
\operatorname{tr}(ABAB+ABBA-BAAB-BABA)=0,$$
because the first and last terms have equal trace and the middle two
terms have equal trace. Lemma 3 applied to $C,D$ therefore says
$CD+DC=tC$, proving the second iterate.

The commutator $E$ has trace zero, and
$$\operatorname{tr}(EC)=\operatorname{tr}(CDC-DC^2)=0.$$
Apply Lemma 3 to $E,C$, whose traces and mutual trace vanish, to obtain
$EC+CE=0$. Consequently $F(E,tC)=(t[E,C],0)$. Every pair $(Z,0)$ maps
to $(0,0)$, proving the third and fourth iterates. Since zero is fixed
and every orbit reaches it, it is the entire recurrent set. The displayed
nested tests follow by asking when these exact iterates are zero; at the
first step odd characteristic makes $C=D=0$ equivalent to $AB=BA=0$.

For sharpness choose the following two integral matrices and reduce their
entries into any odd field:
$$A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
B=\begin{pmatrix}1&1\\1&0\end{pmatrix}.$$
They give
$$C=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
D=\begin{pmatrix}2&1\\1&0\end{pmatrix},\quad t=2,\quad
E=\begin{pmatrix}2&-2\\-2&-2\end{pmatrix},$$
and
$$t[E,C]=8\begin{pmatrix}1&1\\1&-1\end{pmatrix}\ne0.$$
The scalar $8$ is nonzero in every odd characteristic. Hence the third
iterate is nonzero and the fourth is zero, so this pair has tail four. ∎

### Proposition 5: all-target linear decoder and evaluated unique maximum

For a target $(U,V)$ set
$$P=(V+U)/2,\qquad Q=(V-U)/2.$$
Its exact source equations are $AB=P$, $BA=Q$. For each fixed $A$,
either there are no solutions $B$, or the solutions form one affine coset
of a vector space of dimension $(2-\operatorname{rank}A)^2$. Therefore
$$|F^{-1}(U,V)|=
\sum_{A\in\operatorname{Mat}_2(\mathbb F_q)}
\mathbf1_{(P,Q)\in\operatorname{im}L_A}\,
q^{(2-\operatorname{rank}A)^2},\qquad L_A(B)=(AB,BA).$$
This is an exact finite linear-solvability decoder, **not** an evaluated
all-target fibre atlas. Its maximum is evaluated completely:
$$\max_{U,V}|F^{-1}(U,V)|=|F^{-1}(0,0)|=3q^4-2q^2,$$
and the zero pair is the unique maximizing target.

**Proof.** The invertible output transformation
$(P,Q)\mapsto(P-Q,P+Q)$ proves the source equations without losing a
solution. The kernel of $L_A$ is exactly the set of $B$ which kill
$\operatorname{im}A$ and have image inside $\ker A$. Equivalently,
$$\ker L_A\cong
\operatorname{Hom}(\mathbb F_q^2/\operatorname{im}A,\ker A).$$
Both spaces have dimension $2-\operatorname{rank}A$, proving the dimension
and the displayed decoder. Each consistent linear fibre is an affine
coset of this kernel; an inconsistent target contributes zero.

The zero target is consistent for every $A$, so each summand for a
general target is at most its zero-target summand. If $(U,V)\ne(0,0)$,
then $(P,Q)\ne(0,0)$, and the summand at $A=0$ is zero, strictly less
than its zero-target value $q^4$. Thus the maximum is uniquely zero.

There is one rank-zero matrix. Rank-one matrices number
$(q^2-1)^2/(q-1)$: write $A=uv^{\mathsf T}$ for two nonzero column
vectors, and quotient the $q-1$ choices of reciprocal rescaling.
Invertible matrices number $(q^2-1)(q^2-q)$, by choosing the first
nonzero column and then a second column outside its span. Hence
$$|F^{-1}(0,0)|=
q^4+q\frac{(q^2-1)^2}{q-1}+(q^2-1)(q^2-q)
=3q^4-2q^2.$$
This proof counts all ranks, including nilpotent and nonnilpotent rank-one
matrices; no commuting or invertible subcarrier is substituted. ∎

### 2.3 Why Proposition 5 supplies no second valued mechanism

The entire inverse problem is the ordinary pair-product problem, under an
invertible linear change of **target** coordinates. This is not asserted
to be a conjugacy of full dynamics: product exchange fixes $(I,I)$,
whereas CAC sends it first to $(0,2I)$ and then to zero. The old PXE
group carrier and TP transformation-semigroup carrier are not silently
identified with all matrices either. Only the exact product equations and
their associated inverse mechanism are transferred.

The zero count is a direct size-two specialization of the published
mutually-annihilating-matrix programme. Fulman–Guralnick Lemma 3.2 proves
the fixed-$A$ count $q^{m^2}$, where $m=\dim\ker A$, and its Section 3.1
derives the full all-size generating function. The source proof was
actually read; this is not subtraction inferred from an abstract. Huang's
underlying counting paper supplies the same owner region. The maximum
argument is generic: any family of linear maps on a finite vector space
has nonempty fibres of kernel size, and the identically zero member makes
the zero target strictly maximal in their sum.

Thus the exact source equation, the fixed-$A$ multiplicity, the complete
zero evaluation, and the zero-maximum argument all receive zero independent
contribution credit. A finite-system wrapper cannot turn that whole
transferred inverse axis into a fresh one. Proposition 4 is a valid sharp
temporal deduction, but there is no remaining second axis. CAC closes
`NO_PROMOTION / KILL_VALUE_INVERSE_AXIS_CONSUMED`.

## 3. Internal boundary: actual originals, not matching titles

- P150's $\mathsf L(x,y)=(y,(1+y)\iota(x))$ and its five explicit strata
  were read. QSC changes the pole divisor and introduces a reset that can
  be recurrent. P150's exact three-layer argument is not imported.
- P157's literal $3x^2-2x^3$ modulo $2^n$, selected-error valuation clock,
  and normalized-unit fibre statement were read. Neither candidate has
  that residue-ring/valuation carrier or proof. Quadratic secant is not
  silently equated with this particular Newton–Hensel cubic.
- P168's inverse-span rule on subspaces of $\mathbb F_{p^4}$ and its rank
  transition theorem were read. QSC takes neither inverse spans nor a
  subfield normal form; it receives no inverse-span credit.
- P174's state-selected projectivity on ordered subsets and its forced
  $\{0,\infty\}$ core were read. QSC instead acts on ordered scalar
  pairs and replaces a pole by zero; an eventual projective involution
  cannot be transferred from P174.
- P175's literal diagonal-feedback commutator, entry equations, support
  colouring inverse and square-zero theorem were read. CAC uses two full
  matrices, and its sharp height four prevents reuse of that square-zero
  argument; nevertheless commutator terminology alone has no value.
- P180's common bilinear radial scalar and its cubic scalar iterate were
  read. CAC is not scaled along the original pair. Its second-step scalar
  $tC$ is only one coordinate of a changing commutator pair, not a radial
  power-map contract.
- The old CS original gives $([A,B],A+B)$ in characteristic two and proves
  its image/time laws with polarized Cayley–Hamilton. This exact proof
  primitive is deducted in CAC; the literal, characteristic and terminal
  dynamics are not identified. The old MAR entry is $(B,AB+BA)$ and
  includes nontrivial odd-characteristic recurrence, not CAC.
- The current nonlinear and algebra proof originals rule out reusing
  HUR/PXE/TP, ghost derivatives, inverse aggregation, and shallow common-line
  annihilation as fresh replacements. No FRI/ZGR rule was instantiated.

## Final boundary

Two explicit literal attempts close negatively, with no reserve and no
number assigned. There is no theorem-of-impossibility claim about all
rational or noncommutative finite maps, and no global novelty certificate.
No independent admission gate, manuscript review, verifier replay, build,
page view, or scientific execution occurred in this lane.
