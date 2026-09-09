# R4 B4: the exact first quotient break

2026-09-09 UTC. Bounded proof-only conductor attack complementary to
A3's cluster-resolvent work. All accepted R2/R3 files remain unchanged.

## Frozen claim and status

For every odd prime $p$, let $K=\overline{\mathbb F}_p((s))$,
$v(s)=1$, and $P_s(z)=(1+s)z+z^2$. Let $L_2/K$ be the
accepted cyclic degree-$p^2$ small-cycle field and let $F_2$ be
its unique degree-$p$ subfield. Determine the unique lower/upper
ramification break $u$ of $F_2/K$, without assuming that it equals
the certified prime-$3$ value or using unknown AS coefficients.

**PROVABLE AS STATED:**

$$
u=2(p-1)\qquad\text{for every odd prime }p.
$$

By the accepted oriented first-quotient stabilization, the same break
holds for the common degree-$p$ quotient $F_e=F_2$ at every
level $e\ge2$. The separate native period-$p$ field $L_1$
has break $p-1$. In the convention that an Artin conductor is one
more than the upper break of a ramified degree-$p$ character, the
common quotient's nontrivial characters have conductor $2p-1$.

The full proof is [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md).
This is an exact local invariant, not a paper admission or a global
dynatomic-component theorem.

## Accepted inputs and scope

The following were read and treated as accepted, not reproved:

- [Full local inertia](../../continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md):
  the native small fields are cyclic of degree $p^e$.
- [Oriented quotient stabilization](../../continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md):
  $F_e=F_2$ for $e\ge2$ and $L_1\cap L_2=K$.
- The same R3 proofs give, for a root $\alpha$ of $M_2$ and
  a root $\beta$ of $M_1$, with $r=(p-1)/p$,

  $$
  v(\alpha)=v(\beta)=r,\qquad
  v(\alpha-\beta)=\frac{2(p-1)^2}{p^2},\qquad
  v(P_s(\alpha)-\alpha)=v(P_s(\beta)-\beta)=2r.
  $$

The conductor proof does not need the known $p$-step displacement
$2(p-1)$, a total polynomial discriminant, a normalization index,
an explicit AS representative, or an unproved higher-layer pattern.
It does not reinterpret the contradiction-only second-break value in
the stabilization proof as an actual ramification computation.

The proof-writer skill is used to preserve the exact all-odd-prime
claim and isolate the nontrivial cancellation lemma. A3 sent a
parallel conductor proposal during this analysis. B4 checked and
formalized its cancellation argument, and supplied the explicit
character-theoretic justification that the order-$p$ kernel survives
through the required upper-numbering interval.

## Proof mechanism

The disjoint compositum $B=L_2L_1$ has group
$C_{p^2}\times C_p$. In its integer valuation, set

$$
\eta=\alpha-\beta,\qquad
a=v_B(\eta)=2p(p-1)^2,\qquad
A=2p^2(p-1).
$$

Every Galois displacement of $\eta$ has valuation at least $A$;
the automorphism that acts by one native step on $\alpha$ and fixes
$\beta$ attains $A$.

If $b_0$ is the first lower break of $B/K$, its quotient $L_1$
implies $b_0\le p-1$. Consequently $A>a+p b_0$. The
uniformizer expansion of $\eta$ then forces:

1. its first nonzero exponent prime to $p$ is
   $n=a+(p-1)b_0$;
2. the first ramification quotient has order exactly $p$;
3. any automorphism with later lower break $c>b_0$ displaces
   $\eta$ at valuation exactly $n+c$.

If the unknown quotient break $u$ were at most $p-1$, the
elementary quotient $F_2L_1/K$ would have two distinct upper jumps
$b_0<p-1$ and $p-1$. Its second jump would force a displacement
$a+p(p-1)<A$, a contradiction. Thus $u>p-1$.

Now $b_0=p-1$. Applying the exact later-break formula to the
native automorphism gives its lower break $p^2-1$, and Herbrand's
conversion yields $u=2(p-1)$.

## Source subtraction, verification, and limitations

The ramification inputs are classical: upper numbering is compatible
with quotients, and the upper breaks $u<w$ of a totally ramified
cyclic degree-$p^2$ extension in characteristic $p$ satisfy
$w\ge pu$. The exact hypotheses and formula were directly checked
in [Elder–Keating, Section 2, Lemma 2.2 and Theorem 2.3](https://arxiv.org/html/2503.16830v1);
their perfect residue field hypothesis includes
$\overline{\mathbb F}_p$. The cancellation and finite-character
arguments are written out, not attributed to a theorem outside its
scope.

The crucial kernel-persistence step is not inferred merely from
surjecting onto a ramification subgroup of $L_2/K$: such a
surjection alone could admit a diagonal subgroup. The proof uses
all finite abelian characters and their break comparison to rule
out that gap.

The R3 branch-only discriminant limitation remains valid and is not
used as a no-go here. The new proof uses the disjoint native
period-$p$ field, the exact cross contact, and the ramification
filtration of their compositum.

Author audit checks the prime-to-$p$ exponent, coefficient
cancellations, first-grade root count, strict inequalities,
kernel persistence, both conductor regimes, and the native
automorphism's exact lower break. Nonauthor review is a separate
coordinator-owned step.

Mathematical executions: **zero**. Only the two new files in this
assigned R4 directory were written. No older-file mutation,
shared/Git/manuscript/evaluation work, external model upload,
or new diagnostic. No coefficient formula or higher Witt-coordinate
stabilization is claimed.

NO_BAD_EULER_OR_ROOT_NUMBER.
