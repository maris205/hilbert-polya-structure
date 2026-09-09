# E8 Round 2: dynamics-algebra and trace-interface audit

2026-09-09 UTC. Nonauthor current-team internal review by
`/root/c429_e8_coboundary_review`. This is an independent check of the
Round-2 A1 argument, not human peer review, a formal evaluation, or a
reopening of the accepted first-pass auxiliary proofs.

## Verdict and allowed claims

**The mathematical statements and displayed proofs pass. No proof-level
must-fix was found. Original PC424-L and the finite Frobenius-dependence
bridge (F) remain unproved.** One minor concluding-sentence precision
was requested from the author and has been independently read back and
closed. There are no remaining review corrections.

The primary artifacts are the complete
[REPORT](../../a1_frobenius_finiteness/REPORT.md) and
[PROOF_PACKAGE](../../a1_frobenius_finiteness/PROOF_PACKAGE.md), initially
73 and 371 lines; the final proof has 379 lines after the checked changes.
This review checks their new statements rather than
using the author's favorable summary as evidence.

The original domain, parameters and observable remain all odd primes
$p$, $k=\overline{\mathbb F}_p$, $c\in k$, $h\in k[x]$, and ordinary
primitive $f_c=x^2+c$ cycle sums counting distinct points once, including
periods divisible by $p$. One application of
$(x,y)\mapsto(f_c(x),y+h(x))$ is the native tick. The proposed bridge is
one nonzero scalar linear relation among $[h^{p^i}]$ in
$k[x]/\Delta k[x]$, independent of field or period cutoffs. The new
algebraic presentation preserves this question; it does not answer it.

The following auxiliary conclusions are justified:

- For any algebraically closed $k$ and any polynomial $f$ of degree at
  least two, the direct limit $D$ and its automorphism $\alpha$ define
  the stated skew Laurent algebra with the finite presentation (3).
- Its finite-dimensional simple unital modules are exactly primitive
  ordinary $f$-cycles with a nonzero scalar return twist. Critical
  cycles and characteristic-divisible periods are included.
- All finite-dimensional character conditions on $h\in k[x]$ are
  precisely the original ordinary-cycle conditions.
- The grade-zero cocenter is exactly the polynomial coboundary
  quotient. Each nonzero grade is the linear coinvariant quotient of
  the full corresponding periodic-scheme coordinate ring, for both
  signs of the grade.
- In characteristic $p$, a trace-radical class becomes Frobenius-nilpotent
  in every finite-dimensional quotient. The exponent may depend on the
  quotient; no global Frobenius relation has been obtained.
- The Leavitt control refutes a blanket assertion for all finitely
  presented algebras, not the special assertion for $A_f$.

These conclusions are vector-space/representation-theoretic interfaces.
They do not establish residual trace separation, a finite-dimensional
global defect, an algebraic transfer, or an independent-paper admission.

## 1. Ascending algebra and finite presentation

Proof §1, equations (1)–(3), is correct. Substitution by nonconstant $f$
is injective on $R=k[x]$, including when $f$ is inseparable. Therefore
the injective direct limit can be represented as the increasing union
$D=\bigcup_i k[x_i]$, with $x_i=f(x_{i+1})$. The assignments
$\alpha(x_i)=f(x_i)$ and $\alpha^{-1}(x_i)=x_{i+1}$ respect every
relation and are inverse $k$-automorphisms. This makes the skew Laurent
construction legitimate; $\sigma:R\to R$ itself need not be surjective.

For the presentation, $z_i=U^iXT^i$ satisfies
$z_i=f(z_{i+1})$ because $TU=UT=1$ and $TXU=f(X)$. If $i<j$, then
$z_i=f^{\circ(j-i)}(z_j)$, so all $z_i$ commute. Thus the compatible
stage maps really give a map from the commutative direct limit into
the presented algebra. Conjugation by $T$ acts as $\alpha$, yielding
the reverse map from the skew Laurent algebra. The two maps are
inverse on the generators. No unproved injectivity of the map into
the presented algebra is being assumed in this argument.

The algebra is finitely presented, but this does not make it finite
dimensional: it contains the embedded polynomial ring $k[x_0]$.

## 2. Simple modules, scalar return and characteristic-p traces

Proposition 2.1 does not incorrectly diagonalize the shift $T$.
Instead it diagonalizes $X$. The sum $E$ of its ordinary eigenspaces
is nonzero over algebraically closed $k$, and

$$XT^{-1}=T^{-1}f(X)$$

sends an eigenvector of eigenvalue $a$ to one of eigenvalue $f(a)$.
Hence $T^{-1}E\subseteq E$. Injectivity and finite dimension give
equality, so $E$ is stable under $X,T,T^{-1}$ and simplicity forces
$E=V$. No derivative condition enters.

The resulting finite spectrum is permuted surjectively, hence bijectively,
by $f$. Each of its cycles gives a submodule, so only one cycle occurs.
The argument then chooses an eigenvector of $T^{-\ell}$ on one
$X$-eigenspace and obtains one vector per distinct point of the cycle.
The scalar return is nonzero because $T$ is invertible. These vectors
span an invariant subspace, so simplicity forces dimension exactly
$\ell$. In the converse direction, polynomial spectral projections
are valid since the $X$-eigenvalues are distinct; they prove simplicity
of the displayed cyclic representation. Choosing a different initial
point merely relabels and rescales this same representation. The
unpointed orbit and return scalar determine its isomorphism class.

This covers a critical cycle: there is no use of $f'(a)\ne0$. It
also covers $p\mid\ell$: $T$ may then have nontrivial Jordan behavior,
but the proof only uses an eigenvector of its invertible return on
one eigenspace. It does not divide by $\ell$ or assume a diagonalizable
cyclic permutation operator.

In Corollary 2.2, a shift not divisible by $\ell$ has zero diagonal,
and a divisible shift is the scalar $\lambda^{-n/\ell}I$. This proves
both trace formulas for positive, negative and zero $n$. Composition
series exist by finite dimension, and trace is additive along an
invariant filtration in every characteristic. Thus arbitrary
finite-dimensional modules impose no additional **vanishing** tests.
One must not strengthen this to recovery of composition multiplicities
from characters in characteristic $p$; no such claim is made.

The orientation is consistent: $T^{-1}$ advances an $X$-eigenvalue
by the native map $f$. Frobenius on the cocenter below is an auxiliary
characteristic-$p$ operation, not a redefinition of that native clock.

## 3. Grade-zero commutator contraction

The bracket $[A_f,A_f]$ is correctly the linear span of commutators,
not their two-sided ideal. Expanding arbitrary commutators into
homogeneous components makes that subspace graded. Since $D$ is
commutative, a degree-zero coefficient is

$$
a\alpha^i(b)-b\alpha^{-i}(a)
=(\alpha^i-1)(b\alpha^{-i}(a)).
$$

For every integer $i$, positive or negative, the right side belongs
to $(\alpha-1)D$ by a finite geometric sum. The reverse inclusion is
given by $[T,dT^{-1}]=(\alpha-1)d$. This proves equation (10), with
no hidden commutators from other total grades.

The contraction to $R$ is also exact, not a conditional use of R6.
Every $u\in\alpha^{-N}R$ is congruent to $\alpha^Nu\in R$ modulo
$(\alpha-1)D$. If $h\in R$ equals $(\alpha-1)u$, set
$r=\alpha^Nu\in R$. Then

$$
h=(\sigma-1)\left(r-\sum_{j=0}^{N-1}\sigma^jh\right).
$$

Both transfers lie in $R$, and the sum is empty for $N=0$. Therefore
$(\alpha-1)D\cap R=(\sigma-1)R$, proving the claimed canonical
isomorphism $HH_0(A_f)_0\simeq R/(\sigma-1)R$.

No quotient ring structure is inferred for $R/(\sigma-1)R$. The
first-pass polynomial normal form identifies its underlying vector
space with $k\oplus xk[x^2]$ in the frozen quadratic case.

## 4. Both nonzero grades and nonreduced periodic schemes

For nonzero $n$, write
$J_n=(\alpha^n(d)-d:d\in D)$ as an actual ideal. The coefficient of
$[a,bT^n]$ is $-b(\alpha^n(a)-a)$, so these commutators span the
whole ideal. The coefficient of $[T,bT^{n-1}]$ is $(\alpha-1)b$.
Modulo $J_n$, $\alpha^n=1$ and every remaining homogeneous
commutator coefficient becomes an $\alpha^i-1$ difference. This
proves

$$HH_0(A_f)_n\simeq D/(J_n+(\alpha-1)D).$$

The ideals are invariant under $\alpha$ and its inverse, and
$J_{-n}=J_n$. Set $m=|n|$. In $D/J_m$ one has $\alpha^m=1$;
therefore every $x_i$ is a nonnegative iterate of $x_0$, with exponent
congruent to $-i$ modulo $m$. The inverse map to the claimed
surjection is exactly

$$x_i\longmapsto f^{\circ r_i}(\bar x),\qquad r_i\equiv-i\pmod m.$$

In $R/(f^{\circ m}-x)$, substitution $\sigma$ is well-defined and
satisfies $\sigma^m=1$, so is an automorphism even if the ring is
nonreduced. This verifies both compatibility with $\alpha$ and
annihilation of every generator of $J_m$. Thus the asserted
isomorphism of periodic coordinate rings before taking coinvariants
is valid, and quotienting by the linear image of $\sigma-1$ gives
equation (8) for both signs.

No division by $m$ is used. Replacing the finite coordinate ring by
its reduction, or replacing coinvariants by invariants using averaging,
would be invalid without additional hypotheses, especially if $p\mid m$.
The proof performs neither replacement. Its output is the coinvariant
space, not the entire coordinate ring as a vector space or algebra.

One further compatibility is important for reuse. For $n\ne0$,
Frobenius on the cocenter is the **twisted norm**, since directly in
the skew Laurent algebra

$$
F([aT^n])=
\left[\left(\prod_{j=0}^{p-1}\alpha^{jn}(a)\right)T^{pn}\right].
$$

Only on grade zero does this specialize to $[a]\mapsto[a^p]$.
Equation (8) must not be combined with a naive fixed-level coefficient
Frobenius in the other grades. The author has not made that
identification and has now added the checked formula as (15a), with
the explicit warning. This states the exact handoff constraint.

## 5. Frobenius on the cocenter and finite-dimensional quotients

Proof §4's semilinear map is well-defined. In the expansion of
$(a+b)^p$, each nonconstant binary word has a length-$p$ rotation
orbit of size $p$; rotations have the same cocenter class. Such
contributions sum to zero. Applying this additivity to $ab-ba$
gives $[(ab-ba)^p]=[(ab)^p]-[(ba)^p]=0$, since those two words
are cyclic rotations. Additivity extends to finite sums of
commutators, giving the claimed map on classes, naturally under
algebra homomorphisms. Scalar multiplication is $p$-semilinear.

For a finite-dimensional quotient $Q$, algebraic closedness implies
that $Q/\operatorname{rad}Q$ is a product of matrix algebras over $k$.
No separability or division-algebra exception survives over this field.
In a matrix algebra of any size, the commutator span is the trace-zero
subspace: off-diagonal matrix units and diagonal differences give it.
This remains true when the size is divisible by $p$; the scalar identity
then has trace zero and itself lies in that span. Normalized trace
or division by the matrix size is neither needed nor allowed here.

Thus the hypothesis on all simple traces writes
$a=\sum_i[b_i,c_i]+r$, with $r\in\operatorname{rad}Q$. If the radical
has nilpotence index $L$, any $s$ with $p^s\ge L$ gives
$[a^{p^s}]=[r^{p^s}]=0$. One can choose such an $s$ uniformly for all
eligible $a$ in this **fixed** $Q$, a slightly stronger form of the
author's stated fact. It still depends on $Q$.

Conversely, traces of commutators vanish and
$\operatorname{tr}(M^{p^s})=\operatorname{tr}(M)^{p^s}$. Frobenius
injectivity in the field gives zero simple traces. Its inverse, and
hence perfection as a separate condition, is not needed for this
step. The stated algebraically closed field hypothesis already supplies
both perfectness and the required splitting of the semisimple quotient.

Every simple module of a finite-dimensional quotient is a
finite-dimensional $A_f$-module by inflation, so the application to
the trace radical is legitimate. But the conclusion has quantifiers
$\forall Q\,\exists s_Q$, not a single relation in $HH_0(A_f)_0$.
No unboundedness of the actual exponents for this particular dynamics
algebra is proved either: “may depend” is the justified wording.
Even a uniform exponent in all finite quotients would still require
separation of the original cocenter by those quotients to conclude
vanishing in the original cocenter. Neither missing premise follows
from finite presentation.

## 6. Primary sources and the Leavitt negative control

The cited primary texts were opened and their relevant hypotheses
read directly during this review:

- [Etingof, Sections 1.7 and 1.9, Theorem 1.10](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/mit18_706_s23_notes_by_pavel_etingof.pdf):
  the setting is algebraically closed $k$. Independence of irreducible
  finite-dimensional characters does not require $A$ to be finite;
  their spanning of the whole dual cocenter in part (ii) does require
  finite-dimensional semisimple $A$. Its proof uses unnormalized matrix
  trace and is compatible with positive characteristic. The author
  correctly declines to apply part (ii) to $A_f$.
- [Klep–Špenko, Section 3, Theorem 3.1](https://igorklep.github.io/files/spurnullstellensatz7nov13v3.pdf):
  the field is algebraically closed of characteristic zero, and the
  theorem concerns a finite list of free-polynomial trace equations
  evaluated on tuples of all matrix sizes. It does not directly treat
  the characteristic-$p$ matrix tuples constrained by presentation (3).
  The author's subtraction is correct.
- [Ara–Cortiñas, Section 3 and Theorem 4.4 with its proof](https://arxiv.org/pdf/1108.0352):
  the base is an arbitrary field. Section 3's crossed-product theorem
  uses an automorphism, which applies to $(D,\alpha)$; the separate
  corner-isomorphism statement must not be applied directly to the
  nonsurjective $\sigma:R\to R$. Theorem 4.4 assumes a finite quiver
  without sources. The one-vertex, two-loop quiver meets this exactly,
  and its positive cocenter grades are rotation coinvariants of words.

In the Leavitt control, the two displayed maps really are inverse
$V\oplus V\leftrightarrow V$ by the defining relations. Integer
dimension therefore excludes any nonzero finite-dimensional unital
module, even in characteristic $p$. This argument does not substitute
a trace calculation in $k$ for an integer dimension calculation.

Under the source's word description, $u_1^m$ corresponds to the
one-element rotation orbit of that word. Its coefficient functional
is zero on every rotation difference and equals one on the word,
so its class survives also when $p\mid m$. This does not average
over an orbit or divide by its length. Therefore the full Frobenius
iterates of $[u_1]$ lie nontrivially in distinct grades $p^i$ and
are linearly independent. The representation trace condition is
vacuous for this algebra. This refutes precisely the unrestricted
blanket theorem stated by the author, not (F) for $A_f$, which does
have the explicitly classified finite-dimensional representations.

## 7. Source subtraction, corrections and remaining obligation

The crossed-product cocenter formalism, finite-dimensional radical
argument, character theorem and Leavitt calculation are classical.
The accepted first-pass freeness and coefficient descent, old R6
algebraic-transfer theorem, and A2's conditional graph extraction
are imported, not re-proved or admitted anew. The current contribution
is a direct specialization matching all original cycle and coboundary
quantifiers within one algebra. This is useful auxiliary progress,
not a demonstrated substantial independent-question closure.

**Proof-level must-fixes: zero.** The only requested author change was
to replace the concluding phrase “the nonzero graded pieces retain
the exact full periodic coordinate rings” by “the nonzero graded
pieces retain the coinvariants of the full periodic coordinate rings.”
Equation (8) and the theorem statement were already correct. Readback
status of this minor wording correction: **CLOSED**. The author made
the change at final lines 373–376. The optional twisted-norm clarification
above was also added as (15a), at final lines 282–291. Both affected
passages were independently read back; the identity follows directly
from skew Laurent multiplication for either sign of $n$. No further
change to the mathematical conclusions was required.

The remaining mathematical obligation is exactly the dynamics-specific
statement

$$
z\in\mathcal T_f\cap HH_0(A_f)_0
\quad\Longrightarrow\quad
\exists s\ge0,\ a_s\ne0:\ \sum_{i=0}^s a_iF^i(z)=0
\text{ in }HH_0(A_f)_0.
$$

Here $\mathcal T_f$ is the intersection of all finite-dimensional
character kernels. The accepted first-pass freeness would force
$z=0$ if this statement were proved. Neither finite quotient
nilpotence, the finite dimension of each nonzero grade, nor the
classical sources provide it. One needs an actual uniform/global
separation mechanism or a different complete proof. No counterexample
to original PC424-L is supplied by this review or by the Leavitt control.

## 8. Review provenance and execution receipt

The review followed current Hénon AGENTS, CONTINUOUS_RUN and the
repository batch workflow, using research-review for the critical
internal audit and proof-writer for exact hypotheses and gap labels.
No external reviewer-model example was executed. No full ARS panel,
human review, novelty clearance or target-arithmetic evaluation is
claimed. The primary-source check used the three linked documents;
no broader systematic literature search was performed.

Reviewed source-byte identities:

```text
REPORT.md
7d4d1038fc28f4a2afc87690e7a1925f18efb3e3334f18cb1b4d74479e4bf4f9
PROOF_PACKAGE.md (initial)
9f1f6f7977919993e2877df91bfb6515385ca66e0dc7c51716dcad5df79ed55e
PROOF_PACKAGE.md (final, correction and (15a) read back)
cd2e845d479aac752e8397264f02b03df704f9e172f8d16fbcbdf81f4ea86dd3
```

Only this new assigned review file was written by the reviewer. First-pass
files were preserved; the author made the bounded changes recorded above
in the author's own Round-2 file. Mathematical programs, old reruns,
builds/PDFs, Git operations, evaluations, shared-state writes,
external-model uploads and extra agents: **0**. Read/search operations
and byte hashes are not mathematical experiments.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
