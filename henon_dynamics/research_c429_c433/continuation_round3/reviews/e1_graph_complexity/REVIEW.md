# R3 E1: independent review of graph-construction degree obstructions

2026-09-09 UTC. Reviewer: current-session nonauthor E1. Scope: the new
[Round 3 A2 report](../../a2_graph_complexity/REPORT.md), including its
rectangular-support extension. The accepted first-pass and Round 2 proofs
are inputs, not targets for repetition. This is an internal mathematical
review, not external peer review or a paper-admission decision.

## Verdict and exact boundary

**Auxiliary claims: PROVABLE AS STATED. Mathematical must-fix count: 0.**
The additive-separated degree bounds, constant/descent equivalences,
incidence-dimension bounds and actual-periodic-set finite-data control
survive independent checking. No extra separability or prime-to-period
assumption is needed beyond those stated in the relevant result.

**Original PC424-L and the requested fixed-increment graph construction:
NOT CURRENTLY JUSTIFIED.** Neither a polynomial transfer for every
$h\in K_c$, a nonzero global defect, nor a compatible sub-cube-root
sequence has been constructed. The results obstruct named methods;
they do not obstruct every possible construction. Recommendation:
accept as a completed auxiliary proof package, with no separate paper
count and no original-question closure.

The reviewed author artifact has SHA-256:

```text
cb490a31509715df1238fea2451af2a1bbf8b1365545873bb7dd2280642d61dd  continuation_round3/a2_graph_complexity/REPORT.md
```

## Claim, assumptions and dependency map

The original objects remain $k=\overline{\mathbb F}_p$ with $p$ odd,
$f(x)=x^2+c$, $\Delta Q=Q\circ f-Q$, $B_c=\Delta k[x]$, and
$K_c$ the polynomials with zero ordinary sums on every primitive
$f$-cycle. The native skew map is $(x,y)\mapsto(f(x),y+h(x))$.
Periods divisible by $p$ are not deleted; each distinct point is counted
once. In the graph target, $N$ counts selected actual periodic points,
not a containing finite-field cardinality.

The finite-data theorem has deliberately different quantifiers: it fixes
distinct abscissae $S$, a permutation $\pi$ on them, and allows every
zero-cycle-sum vector $w$. It does not assume a single global polynomial
$h$ underlying all such vectors.

Dependencies actually used are:

1. Imported polynomial normal form, leading-degree parity and root
   counting give the additive-separated obstruction.
2. Ordinary cumulative sums give the constant-optimization equivalence;
   finite-field roots and Frobenius return compatibility give the two
   distinct descent tests.
3. A linear cycle-difference map, locally closed vertical-factor strata,
   and finite-type dimension bounds give the incidence theorem.
4. The already known monomial squarefreeness construction supplies
   growing actual periodic sets to which the new incidence theorem applies.

R6 algebraic descent and the Round 2 cubic theorem explain the requested
bridge, but are not used to prove either new obstruction. Their existing
proofs were not rerun or reproved in this review.

## 1. Additive-separated residual and coordinate shear

Let the normalized increment $v\in k\oplus xk[x^2]$ have positive
odd degree $d$. If $U(f(a))-U(a)=v(a)$ on a union $S$ of cycles,
and $L(U(a))=A(a)$ for a nonzero additive polynomial
$L(Y)=\sum_{i=0}^r\lambda_iY^{p^i}$, then additivity gives

$$R=\Delta A-L(v),\qquad R|_S=0.$$

Writing $b=p^r$ and $a_A=\max(0,\deg A)$ with the stated zero
polynomial convention, $\deg L(v)=db$. The leading term cannot be
lost: the top additive summand has strictly larger degree than all
others and nonzero leading coefficient. Since $p$ and $d$ are odd,
$db$ is odd. For nonconstant $A$, the leading term of $A\circ f$
has degree $2a_A$, strictly larger than that of $A$ itself. Therefore
$\deg\Delta A=2a_A$, an even number. If $A$ is constant or zero,
$\Delta A=0$ and $db>0$. In every case,

$$R\ne0,\qquad \deg R=\max(2a_A,db).$$

All points of $S$ are distinct, so root counting gives

$$N\le\max(2a_A,db)\le\max(2,d)D,
\qquad D=\max(a_A,b).$$

The proof includes $r=0$, vanishing linear coefficient of $L$,
inseparable $L$, constant or zero $A$, and wild native periods.
It never divides by a period or differentiates $L$. Since no choice
of a cycle constant entered the argument, optimizing all those constants
cannot evade the bound. Even empty $S$, if permitted, only makes the
inequality vacuous.

For the original fixed $h\in K_c$, the imported decomposition
$h=\Delta Q_0+v$ keeps $v$ inside $K_c$. A fixed point exists
over $k$, so a nonzero constant cannot lie in $K_c$. Thus the two
cases are exactly $v=0$ and positive odd degree. The first already
gives a polynomial transfer; the second is hypothetical, not asserted
to exist.

Subtracting $Q_0(a)$ from transfer values changes the increment to $v$.
For an original equation $L(Y)=A_0(X)$ this gives
$L(Z)=A_0-L(Q_0)$. With $q_0=\max(0,\deg Q_0)$ and original
total degree $D_0$, one has $b\le D_0$ and
$a_A\le\max(D_0,bq_0)$. Hence

$$N\le\max(2,2q_0,d)D_0.$$

Cancellation inside $A_0-L(Q_0)$ only lowers $a_A$ and does not
invalidate this upper bound. The constants are fixed once $h,f,Q_0$
are fixed, independently of the selected cycles and additive rank.
The linear-order obstruction is consequently valid in both the declared
normal proof coordinate and the original coordinate. It cannot be
applied to arbitrary non-additive graph equations.

## 2. Constants, finite fields and Frobenius blocks

The geometric equivalence assumes zero native sums on $S$. Its necessity
is the residual calculation. For sufficiency, on a cycle based at $a$
write $s_j=\sum_{i=0}^{j-1}h(f^i(a))$. Algebraic closedness supplies a root
$z$ of $L(z)=A(a)$ because $L$ is nonconstant. Setting
$U(f^j(a))=z+s_j$ is consistent at the closing step precisely because
the full cycle sum is zero. The pointwise residual identity propagates
$L(U)=A$ around the whole cycle. This proves the stated equivalence
without assuming separability of the root equation.

Over a prescribed finite field $F$ containing the stated data, that
root must instead satisfy $z\in F$. The additional condition
$A(a)\in L(F)$ is both necessary and sufficient. Changing the cycle
representative changes $A(a)$ by $L(s_j)$ with $s_j\in F$, so this
condition does not depend on the representative. The geometric
surjectivity of $L$ is not incorrectly transferred to $F$.

For Frobenius equivariance, all the stated coefficients must be over
$\mathbb F_q$, and $S$ must be $q$-Frobenius stable. On a block of
$e$ native cycles, let $a^{q^e}=f^t(a)$. Necessity of the simultaneous
equations follows from equivariance and the native recurrence:

$$L(z)=A(a),\qquad z^{q^e}-z=s_t.$$

For sufficiency define $U=z+s_j$ on the chosen cycle and transport by
$q$-powers to the other $e-1$ cycles. Their distinctness follows from
the minimal definition of $e$, so the only possible conflict is the
return. Since $f,h$ have the declared field of definition,

$$s_j^{q^e}=s_{t+j}-s_t.$$

Here the zero full-cycle sum makes cumulative sums periodic in their
indices; no division by the native length occurs. The second root
equation therefore yields

$$(z+s_j)^{q^e}=z+s_{t+j},$$

which proves compatibility at every point, including a return crossing
the indexing boundary. The first equation and the residual give the
curve equation on the initial cycle; the field of definition of $L,A$
propagates it to the other cycles. Repeated Frobenius transport around
a point's full Frobenius orbit forces its value into the indicated
finite field. No additional return condition is missing.

The control $h=0$, $S=\{0\}$, $L(Y)=Y^p-Y$, $A=1$ has a zero
residual but incompatible requirements $z^p-z=1$ and $z^p-z=0$.
It correctly refutes automatic descent of a prescribed equation only.
The original increment still has the polynomial transfer $0$; there is
no claimed PC424-L counterexample and no conflict with imported
finite-field coefficient descent for an unrestricted transfer.

## 3. Incidence dimension after all cycle constants are optimized

For $\delta U=U\circ\pi-U$, the kernel is the space of functions
constant on each native cycle, of dimension $m$. Its image is exactly
$H_S$: telescoping proves one containment, cumulative sums the other.
Thus $\dim H_S=N-m$ in every characteristic, even if $p$ divides
some cycle length. The cycle-sum equations remain independent because
their supports are disjoint and each has nonzero coordinate coefficients.

The coefficient space for degree at most $D$ is
$\mathbb P^{M_D-1}$, $M_D=\binom{D+2}{2}$, and the displayed
incidence equations are homogeneous in the coefficients of $P$.
Thus they define a closed finite-type incidence scheme $I_D$.

The exact-$J$ coefficient strata used by the author are locally closed:
for each selected abscissa, identically zero specialization is a finite
set of linear coefficient conditions, and nonzero specialization is the
complement of that closed condition. There are only finitely many $J$.
If $t=|J|$, the pairwise coprime factors $X-x$ give
$P=V_JR$. Since total degrees of nonzero products add,
$\deg R\le D-t$ and the stratum is empty for $t>D$. For $t\le D$,
multiplication by the fixed $V_J$ identifies its ambient linear
coefficient space with one of projective dimension $M_{D-t}-1$.

For a fixed coefficient point, the $t$ coordinates over $J$ are free.
Every other ordinate satisfies a nonzero polynomial in one variable;
it has a finite root scheme or no roots. Thus each nonempty fibre has
dimension $t$. Multiple roots and inseparability only change nilpotents
or multiplicities, not this dimension. The same observation applies over
residue fields of nonclosed coefficient points. The finite-type
dimension inequality now gives

$$\dim(I_D|_J)\le M_{D-t}-1+t\le M_D-1.$$

Taking the finite union of locally closed strata is legitimate for
dimension. In particular, the proof does not make the false assertion
that the unstratified projection has finite fibres. When $D=0$ and
$N\ge1$, the incidence set is empty, which is consistent with the bound.

The map $I_D\to H_S$, $([P],U)\mapsto\delta U$, has precisely the
desired image: all transfers and all cycle constants are already present
in the source. For each irreducible source component, dominance onto its
image closure gives an inclusion of function fields, bounding the latter
dimension by the former. Therefore

$$\dim\overline{E_D}\le M_D-1.$$

This is not a count that assumes independent nonlinear interpolation
conditions or subtracts cycle constants without proving a quotient.
If $M_D-1<N-m$, its complement is a nonempty Zariski-open subset
of $H_S$. Since only one finite-dimensional open set is asserted at
each fixed $S,D$, the countability of $\overline{\mathbb F}_p$ causes
no issue; no countable intersection of dense open sets is being used.
The bound is an upper dimension estimate, not a claim of optimal equality.

The rectangular extension is valid as well. Vertical division changes
the support from $(A,B)$ to $(A-t,B)$, so the coefficient dimension plus
free ordinates is

$$(A-t+1)(B+1)-1+t
=(A+1)(B+1)-1-tB\le(A+1)(B+1)-1.$$

Strata with $t>A$ are empty. The argument includes $A=0$ or $B=0$;
some such strata have empty incidence, which only strengthens the bound.
The same image argument proves the reported rectangular estimate.

## 4. Actual periodic cardinalities and the fixed-global-increment boundary

For $c=0$, put $t_p=\operatorname{ord}_{\mathbb F_p^*}(2)>1$.
An arbitrarily large prime $n$ is not divisible by $t_p$, after excluding
$n=t_p$ if $t_p$ is prime. Hence $p\nmid2^n-1$ and
$X(X^{2^n-1}-1)$ has exactly $2^n$ distinct roots. These are actual
points of period dividing $n$. For prime $n$, only period $1$ and
period $n$ occur. The fixed points are exactly $0,1$, giving

$$N_n=2^n-2,\qquad m_n=N_n/n.$$

Thus the report never counts nilpotent multiplicity or replaces $N_n$
by a field size. With $D_n=\lfloor(\sqrt2-\epsilon)\sqrt{N_n}\rfloor$,
where $0<\epsilon<\sqrt2$,

$$\frac{M_{D_n}-1}{N_n}
\longrightarrow\frac{(\sqrt2-\epsilon)^2}{2}<1,
\qquad \frac{N_n-m_n}{N_n}=1-\frac1n\longrightarrow1.$$

The strict inequality needed by the dimension theorem consequently
holds for sufficiently large selected primes. The converse generic
scale control uses only that $M_D>N$ leaves a nontrivial solution of a
homogeneous system with $N$ equations. It does not require its rows to
be independent. These establish the claimed square-root exponent, not
an exact finite-$N$ minimum degree.

Lagrange interpolation represents each data vector by a polynomial
$h_n$ of degree below $N_n$. Its finitely many coefficients lie in some
finite extension, but both the polynomial and that extension may vary.
Nothing establishes bounded degree, compatibility between levels,
zero sums outside $S_n$, or membership of a single fixed $h$ in $K_c$.
The author states all these limitations explicitly. Indeed the imported
monomial control already has $K_0=B_0$; this is entirely compatible
with hard generic finite data because the quantifiers differ.

## 5. Source applicability and subtraction

The relevant initial normal-form proof, first-pass A1 normal/Frobenius
passages and finite-field Section C, and first-pass A2 Section 2 were
read in their actual bodies. The following are old inputs: the odd
normal form, cyclewise solvability, interpolation, noncancellation of
Frobenius degrees, and the global Artin--Schreier certificate. Theorem 1
is a finite-set degree consequence of these, not a newly proved global
regularity theorem.

The monomial squarefree-prime construction also appears explicitly in
[first-pass A1, subsection A](../../../lanes/a1_periodic_coboundary/REPORT.md).
Only its application to the new incidence bound is credited here as
Round 3 work. This attribution clarification was sent to the author and
coordinator; it is not a mathematical defect in the construction.

The primary-source statements and displayed proofs actually checked are:

- [Stacks, Section 29.29, Lemmas 29.29.1--2](https://stacks.math.columbia.edu/tag/02FW):
  their local finite-type dimension inequality applies to each locally
  closed coefficient stratum and its incidence preimage over $k$.
  All fibres have the stated dimension bound, and no characteristic-zero,
  separability, smoothness or flatness hypothesis is needed for the
  inequality direction used here.
- [Stacks, Theorem 29.23.3](https://stacks.math.columbia.edu/tag/054K):
  the morphism from the finite-type incidence space to the affine space
  $H_S$ is quasi-compact and locally of finite presentation, since these
  are finite-type schemes over a field. Thus its image is constructible.
  Constructibility is supplementary; the dimension-of-image argument
  already proves the needed proper-closure conclusion.
- [Stacks, Lemma 10.116.3](https://stacks.math.columbia.edu/tag/00P1):
  its finite-type-over-a-field dimension formula matches the residue-field
  and transcendence-degree reasoning used for the strata and image
  components. It is classical dimension bookkeeping, not a theorem
  about polynomial coboundaries or periodic transfer regularity.

These are targeted source checks, not an exhaustive literature review or
global novelty certification. No search-only theorem is needed to close
one of the displayed proof steps.

## Remaining risks and execution receipt

There is no unresolved mathematical proof obligation inside the stated
auxiliary results. The material remaining gap is exactly the original one:
obtain sufficiently low-degree compatible actual periodic graphs using
one fixed $h\in K_c$ and all its cycle conditions, or prove the equivalent
global transfer by another mechanism. The additive-separated lower bound
and generic-data lower bound cannot be promoted to a universal no-go.

The research-review guidance supplied the nonauthor claim audit and
source-boundary check; proof-writer guidance required preservation of the
original claim, explicit quantifiers and a separate auxiliary verdict.
The batch's current-session-only instruction supersedes old external-model
examples in those skills. No external model or manuscript upload occurred.

New write ownership is only this review. Mathematical executions, old
mathematical reruns, extra agents, Git operations, evaluations and
manuscript/PDF work: **0**. File reads, primary-source browsing and
SHA-256 binding are provenance checks, not mathematical experiments.
