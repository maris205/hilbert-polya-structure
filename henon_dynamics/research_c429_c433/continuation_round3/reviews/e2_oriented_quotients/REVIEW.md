# E2/R3: independent oriented-quotient corollary review

2026-09-09 UTC. Bounded internal nonauthor proof-and-source review of
[ORIENTED_QUOTIENT_STABILIZATION.md](../../a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md).
This is separate from E6's whole full-local-inertia review. No new
mathematical execution or external-model review is involved.

## Claim and verdict

**PROVABLE AS STATED. PASS; zero open mathematical or source-applicability
must-fixes in the submitted corollary.**

Fix an odd prime $p$, $k=\overline{\mathbb F}_p$, $K=k((s))$,
$v(s)=1$, and the original native map $P_s(z)=(1+s)z+z^2$.
Let $L_e/K$ be the canonical cyclic small-cycle field of degree $p^e$,
with all fields inside one fixed separable closure. The designated
generator is one application of $P_s$, not an unspecified generator
of the same cyclic group.

For the displayed trace resolvents normalized by
$\sigma_e y_e-y_e=+1$, put $a_e=y_e^p-y_e$. Then the proof establishes

$$
[a_e]=[a_2]\in K/\wp(K),\qquad
F_e:=K(y_e)=F_2\quad(e\ge2),
$$

and

$$
L_1\cap L_e=K\quad(e\ge2).
$$

At $p=3$ only, the old accepted certificate consequently propagates
the reduced polar class $2s^{-4}+s^{-2}$ to all $e\ge2$.
This is a corollary of a proved torsor identification, not a new
coefficient computation or a finite-prime extrapolation.

## Inputs actually checked and dependency order

I read the complete submitted corollary, complete
[FULL_LOCAL_INERTIA.md](../../a3_interlevel_contacts/FULL_LOCAL_INERTIA.md),
complete frozen
[PROOF_SUPPLEMENT.md](../../a3_interlevel_contacts/PROOF_SUPPLEMENT.md),
and the final E6 reports for
[interlevel contacts](../e6_interlevel_contacts/REVIEW.md) and
[full local inertia](../e6_full_local_inertia/REVIEW.md).
I also checked the fixed-sign interface against the original
[E2 pair review](../../../continuation_round2/reviews/e2_local_as/REVIEW.md)
and the relevant original trace-resolvent proof passages.

The dependency chain is noncircular:

1. Accepted small-cycle and prime-level facts give the uniform contact
   theorem and second-layer degree. That argument does not assume
   the first quotient of $L_2$ equals, or differs from, $L_1$.
2. The full-local proof uses that second layer to match top clusters
   and prove full local inertia. It uses neither the present equality
   of oriented AS classes nor the present noncontainment result.
3. The present corollary uses the resulting cluster matching to compare
   characters. Its separate contradiction argument uses uniform
   contact and displacement formulas at level two.
4. Only the explicit $p=3$ reduced polynomial uses the earlier
   computational certificate. Neither uniform conclusion does.

The E6 reports record zero open must-fixes in the required inputs.
This review checks their exact interfaces rather than replacing their
distinct whole-proof tasks or treating report hashes as proof.

## 1. Native equivariance removes the scalar ambiguity

Write $r=(p-1)/p$. The full-local proof gives exactly $p$ top
clusters at every level $e\ge2$, with equivalence determined by
distance valuation greater than $2r$. They are the native indices
modulo $p$. At every $e\ge3$ it gives a unique perfect matching
between these clusters and the level-two clusters, characterized by

$$
v(x-y)>2r.
\tag{1}
$$

For all relevant points,

$$
P_s(x)-P_s(y)=(x-y)(1+s+x+y),
$$

and the second factor is a unit, because $x,y$ have positive
valuation. Therefore $P_s$ preserves (1). It permutes each native
root set, and uniqueness of the matching gives

$$
\phi_e(P_sC)=P_s\phi_e(C).
\tag{2}
$$

This is additional structure beyond Galois equivariance. In labels
where one native step adds one, any map satisfying (2) has the form
$i\mapsto i+c$. A map $i\mapsto ui+c$ with $u\in\mathbb F_p^*$
satisfies (2) only if $u=1$. Thus the matching fixes the positive
generator of the quotient torsor; a phase shift remains harmless.

Absolute Galois also preserves (1), the two root sets, and the
unique valuation extension. Hence $\phi_e$ is Galois-equivariant
for the same fixed embeddings. Both equivariances are established,
not inferred from equality of abstract degree-$p$ fields.

Let $\rho_e(g)$ be the native rotation index of $g(\alpha_e)$.
Since $P_s$ is defined over $K$, Galois commutes with native
iteration; the rotation indices add under composition. A different
starting root does not change this character. On the cluster labels,
Galois acts by adding $\overline{\rho_e(g)}$ modulo $p$.
Commuting this action with the phase map gives

$$
\overline{\rho_e(g)}=\overline{\rho_2(g)}
\quad\text{for every }g\in G_K.
\tag{3}
$$

The endpoint $e=2$ is tautological; only $e\ge3$ needs the matching.

## 2. Trace normalization gives equality of classes, not raw values

For $N=p^e$, Lagrange interpolation gives

$$
\operatorname{Tr}_{L_e/K}
\left(\frac{\alpha_e^{N-1}}{M_e'(\alpha_e)}\right)=1.
$$

This divides by the nonzero derivative of the separable polynomial,
not by the scalar $N$, which is zero in characteristic $p$.
For any trace-one $w_e$, define

$$
y_e=-\sum_{i=0}^{N-1}\bar i\,\sigma_e^i(w_e).
$$

Reindexing the sum gives
$(\sigma_e-1)y_e=\sum_{i=0}^{N-1}\sigma_e^i(w_e)=1$.
The wraparound term has the same coefficient because $N=0$ in
$\mathbb F_p$. This independently checks the positive sign.
It follows that

$$
g(y_e)-y_e=\overline{\rho_e(g)}.
\tag{4}
$$

By (3)--(4), $y_e-y_2$ is fixed by all of $G_K$. Both elements
belong to $K^{\mathrm{sep}}$, whose fixed field is $K$. Therefore
$b_e:=y_e-y_2\in K$, and

$$
a_e-a_2=b_e^p-b_e.
\tag{5}
$$

Thus the AS classes are exactly equal, not merely proportional by
a nonzero scalar. Their raw Laurent series need not coincide.

The coordinate-choice statements are also correct:

- Replacing a starting root by its $j$th native iterate replaces
  the displayed derivative trace element by $\sigma_e^j(w_e)$,
  hence replaces $y_e$ by $\sigma_e^j(y_e)=y_e+\bar j$.
  It does not change $a_e$ even before passage to the AS class.
- Replacing the trace-one element by a different trace-one element
  leaves the equation $(\sigma_e-1)y_e=1$ unchanged. The two
  resulting coordinates differ by an element of $K$, so their
  AS scalars differ by a coboundary, as in (5).

The stabilizer of $y_e$ in $C_{p^e}$ is exactly
$\langle\sigma_e^p\rangle$, by its translation formula. Hence
$K(y_e)$ is the unique degree-$p$ subfield. Equation (5) was proved
through the stronger equality $y_e=y_2+b_e$, which gives
$F_e=F_2$ **inside the chosen separable closure**.

## 3. The noncontainment contradiction is correctly normalized

Assume temporarily that $L_1\subset L_2$. Choose roots
$\alpha$ of $M_2$ and $\beta$ of $M_1$, and put
$\eta=\alpha-\beta\in L_2$. The accepted uniform contact and
displacement formulas give, with the base-extended valuation $v$,

$$
v(\eta)=\frac{2(p-1)^2}{p^2},\qquad
v(P_s^{\circ p}(\alpha)-\alpha)=2(p-1).
\tag{6}
$$

The actual full second-layer theorem gives total ramification degree
$p^2$, so the integer-normalized field valuation is
$v_{L_2}=p^2v$. Consequently

$$
A:=v_{L_2}(\eta)=2(p-1)^2>0,\qquad p\nmid A.
\tag{7}
$$

Oddness is essential in the last assertion. Let
$\sigma\alpha=P_s(\alpha)$ and $\tau=\sigma^p$.
Under the containment assumption, the unique subgroup of order $p$
fixes $L_1$, so $\tau\beta=\beta$. Hence

$$
v_{L_2}(\tau\eta-\eta)=2p^2(p-1).
\tag{8}
$$

The frozen prime-valuation lemma applies: for a positive element of
valuation prime to $p$, its displacement order minus its own order
equals $v_{L_2}(\tau(t)-t)-1$. Its proof fixes the coefficient
field $k$ and separates the leading uniformizer monomial from the
higher-order tail; no assumption about $\eta$ itself being a
uniformizer is required.

Here $\tau$ generates the unique order-$p$ subgroup of $C_{p^2}$,
so its lower ramification value is the second lower break. Under
the contrary assumption, that break would satisfy

$$
b_2=2p^2(p-1)-2(p-1)^2
   =2(p-1)(p^2-p+1).
\tag{9}
$$

The degree-$p$ quotient would be $L_1/K$, whose accepted break
is $p-1$. Upper-numbering quotient compatibility and the equality
of first upper and lower breaks therefore give $b_1=p-1$.

### Source-applicability check

I accessed [Elder--Keating, Section 2 and Lemma 2.2](https://arxiv.org/html/2503.16830v1)
on 2026-09-09. The section explicitly works over characteristic-$p$
complete discrete valuation fields with arbitrary perfect residue
field; it does not impose residue finiteness. Our residue field
$\overline{\mathbb F}_p$ is perfect. Its Hasse--Arf statement gives
integer upper breaks for a totally ramified cyclic extension, and
Lemma 2.2 gives

$$
b_1=u_1,\qquad b_2-b_1=p(u_2-u_1),
\tag{10}
$$

with the integer-normalized extension valuation used above. The same
lemma identifies the first break with that of the degree-$p$
quotient. All these hypotheses are satisfied by $L_2/K$.

But (9) and the hypothetical $b_1=p-1$ yield

$$
b_2-b_1=(p-1)(2p^2-2p+1)\equiv-1\pmod p,
$$

contradicting (10). Thus $L_1\not\subset L_2$. Its prime degree
then implies $L_1\cap L_2=K$.

The expression (9) is **hypothetical**, not an established formula
for the actual second break at every prime. The identification of
$L_1$ with the degree-$p$ quotient, and hence the assignment
$b_1=p-1$, must not be retained after discarding the containment
assumption. The normalization $v_{L_2}=p^2v$ itself remains valid.

For $e\ge2$, if $L_1\cap L_e\ne K$, prime degree forces
$L_1\subset L_e$. Cyclicity would make it the unique degree-$p$
subfield $F_e=F_2\subset L_2$, a contradiction. This proves the
claimed intersection statement for every allowed prime and level.

## 4. The prime-three specialization and boundaries

The previously accepted pair used the same fixed $s$, same map,
same native direction, and same positive translation convention.
Its class is $[2s^{-4}+s^{-2}]$. No sign or scalar conversion is
needed before applying (5).

Over the algebraically closed constant field, every regular Laurent
series is an AS coboundary. The reduced negative representative is
unique: a nonzero difference of reduced polar polynomials has a
highest pole prime to $p$, whereas an AS coboundary with a pole has
highest pole divisible by $p$. It follows that at $p=3$,

$$
\operatorname{red}_{\mathrm{AS}}(a_e)=2s^{-4}+s^{-2}
\qquad(e\ge2).
$$

Its break is $4$ by the prime-degree AS break criterion in
[Elder--Keating, Lemma 2.1](https://arxiv.org/html/2503.16830v1),
while the separate prime-level field has break $2$.
The displayed coefficients and break $4$ are not generalized to
other primes. At a general odd prime, field noncontainment is proved
without calculating the common quotient's actual break.

Neither $F_e=F_2$ nor $L_1\cap L_e=K$ asserts $L_2\subset L_e$,
a tower of full fields, stabilization of complete Witt vectors,
or equality of raw resolvent values. Global native-cycle quotient
transitivity and global PC424-D remain outside this result.

## Findings, provenance and execution record

No correction or extra hypothesis is required for the submitted
corollary. The fixed native orientation, hypothetical-break qualifier,
fixed base, and prime-three-only coefficient scope are necessary
parts of its valid statement and are already present.

Classical Hasse--Arf/Herbrand and AS facts, the accepted small-cycle
inputs, the reviewed full-local theorem, and the old pair computation
remain source-owned dependencies. This review does not certify
literature priority, a new paper admission, or a formal Route-A grade.

The proof-writer and research-review skills were used for exact claims,
boundary cases, dependency checking, and internal nonauthor review.
Their older external-model examples were not executed under this
current-session, no-upload assignment.

Mathematical executions: **zero**. No pair rerun, new coefficient
calculation, new agent, model/API upload, author/shared-state edit,
Git operation, manuscript/PDF, or formal evaluation occurred.
Only this assigned review file was written.

| Reviewed author artifact | SHA256 |
| --- | --- |
| `ORIENTED_QUOTIENT_STABILIZATION.md` | `18366e789a1cb693000a2a50d42452e7e7658091cd67ece1c715d38e2a4ae479` |
| `FULL_LOCAL_INERTIA.md` | `0a4f4ff66b633de268d741142502c1b4244868b9eccd3eb040ae472e0b296250` |
| Frozen `PROOF_SUPPLEMENT.md` | `7e9494aa53bb96f5927b8a6ab8e27c5d318d35a9c0f1751663acb9b91f0c1bdb` |

These hashes identify the read versions, not mathematical evidence.

**ZERO_OPEN_MUST_FIXES; ORIENTED_FIRST_AS_CLASSES_STABILIZE_FROM_LEVEL_TWO;
PRIME_LEVEL_INTERSECTION_TRIVIAL; GLOBAL_PC424_D_UNCLOSED.**

**NO_BAD_EULER_OR_ROOT_NUMBER.**
