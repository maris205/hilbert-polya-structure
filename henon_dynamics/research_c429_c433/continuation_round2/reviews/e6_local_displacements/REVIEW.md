# E6/R2 — Independent local-displacement and ramification review

2026-09-09 UTC. Nonauthor, proof-only review of B4/R2's
[REPORT.md](../../b4_local_period_degree/REPORT.md) and
[PROOF_SUPPLEMENT.md](../../b4_local_period_degree/PROOF_SUPPLEMENT.md).
The final reviewed version includes the coordinator-origin weighted-Gauss
sharpening, not only the earlier linear-growth estimate. First-pass files
and reviews were preserved. This is current-team mathematical review, not
human peer review, independent-model-family evidence, formal evaluation,
or manuscript admission.

## 1. Outcome and exact accepted claims

**Zero open mathematical or source-applicability must-fixes were found in
the revised auxiliary statements. The full degree bound remains unproved.**

Fix an odd prime $p$, $k=\overline{\mathbb F}_p$, $K=k((s))$,
$v(s)=1$, $P_s(z)=(1+s)z+z^2$, and a root $\alpha$ of the accepted
small factor $M_e$, of ordinary least period $p^e$. Put

$$
r=(p-1)/p,\quad L=K(\alpha),\quad [L:K]=q=p^h,
\quad 1\le h\le e,\quad v_L=qv.
$$

The following conclusions are verified:

1. With $\delta_j=v(P_s^{p^j}(\alpha)-\alpha)$,

   $$
   \delta_0=2r,\qquad \delta_j\ge(p^j+1)r\quad(0\le j<e).
   $$

   The earlier relative estimate $\delta_{j+1}\ge\delta_j+r$ for
   $0\le j<e-1$ also remains valid by its separate telescoping proof.
2. The field different exponent satisfies

   $$
   d_L\ge p^h-1+p^{e-1}(p-1).
   $$

   This implies the originally assigned weaker inequality
   $d_L\ge q-1+(e-h+1)p^{h-1}(p-1)$.
3. If $h=1$, the unique lower break satisfies

   $$
   b_L=p\delta_{e-1}-(p-1)\ge p^{e-1}(p-1).
   $$

   In particular the older bound $b_L\ge e(p-1)$ holds as well.
4. The same first-level root field, of degree $p$ and break $p-1$,
   contains no small native $p^e$-cycle for any $e\ge2$.
5. No fixed finite extension $B/K$, even if not separable or Galois,
   contains small native cycles for unbounded values of $e$.

These statements do **not** prove $[K(\alpha):K]=p^e$, do not construct
a counterexample to it, and do not establish a nested root-field tower.
They are a complete auxiliary package. After subtracting the existing
small-cycle theorem, elementary filtered-operator algebra, and classical
ramification theory, this review recommends no new independent paper
admission from these bounds alone.

## 2. Root field, inertia and valuation normalization

The accepted A3 inputs are: $M_e$ has $p^e$ distinct geometric roots,
they form one ordinary native cycle, and all have valuation $r$.
They do not include irreducibility of $M_e$ or transitive Galois action.

Nevertheless every root is an iterate of $\alpha$, so every root lies
in $K(\alpha)$. This field is therefore the splitting field of the
separable polynomial $M_e$, even if that polynomial factors. It is
finite Galois. Galois commutes with the polynomial's action on the root
set, and the centralizer of one $p^e$-cycle is its cyclic rotation group.
The Galois subgroup thus has order $p^h$ and acts faithfully. Its order
is divisible by $p$ because its value group contains $(p-1)/p$.

The unique subgroup of order $p^h$ in this rotation group is generated
by $P_s^{p^{e-h}}$. Consequently

$$
\tau(\alpha)=P_s^{p^{e-h}}(\alpha)
$$

defines an actual Galois generator. The statement is about permutations
of the root set followed by their unique field automorphisms. The
single native map $P_s$ is not assumed to be a field automorphism when
$h<e$. There is no illicit replacement of dynamical time by Galois time.

The residue field of every finite extension remains $k$. Finite
extensions of this complete discretely valued, perfect-residue field
are defectless, so $e(L/K)=q$ and $f(L/K)=1$. The full Galois group
is inertia. Thus $v_L=qv$, $v_L(s)=q$, and
$v_L(\alpha)=p^{h-1}(p-1)$. The existing constant field $k\subset K$
provides coefficients in the expansion $O_L=k[[t]]$, and all relevant
automorphisms fix those coefficients pointwise.

An arbitrary positive-valuation point of least period $p^e$ is in this
small factor: the preceding-period denominator in $Q_e$ is nonzero,
and the complementary Hensel factor has unit constant reduction and
no positive-valuation roots. Therefore the original (LD) question is
equivalent to $h=e$ for these minimal root fields. Cyclicity is not a
new hypothesis capable of proving that equality by itself.

The report's final attribution to the accepted A4 torsor criterion is
also correct. On the rank-$p^e$ cyclic étale torsor, the extracted
degree-$p$ quotient class is nonzero exactly when the Galois translation
subgroup maps nontrivially to $C_{p^e}/pC_{p^e}$. Every proper subgroup
maps trivially, so this is equivalent to $h=e$. This equivalence does
not evaluate the class and does not add evidence that it is nonzero.

Evidence: B4 report's accepted-input discussion and supplement setup;
the actual [A3 first-pass proof](../../../lanes/a3_wild_tower/REPORT.md),
Steps 1–4, its accepted E2 interface review, and
[A4's torsor criterion](../../../lanes/a4_witt_local_data/PROOF_SUPPLEMENT.md),
§§1–2 and 7, were checked as inputs.

## 3. Native displacement bounds

### 3.1 The weighted-Gauss sharpening is valid on polynomials

For $Q=\sum a_i z^i\in K[z]$, let
$w_r(Q)=\min_i(v(a_i)+ir)$, with $w_r(0)=+\infty$.
For the $K$-linear operator $UQ=Q\circ P_s$, set $\Delta=U-I$.
Every nonconstant monomial satisfies

$$
\Delta(z^i)=z^i((1+s+z)^i-1).
$$

Every surviving term in the bracket contains at least one $s$ or $z$,
and hence has weight at least $r$, since $v(s)=1>r>0$.
The constants cancel, including all further binomial cancellations in
characteristic $p$. Such cancellations can increase valuation only.
Constants are killed by $\Delta$. K-linearity and the minimum
inequality therefore give $w_r(\Delta Q)\ge w_r(Q)+r$ for every
polynomial, including polynomials with arbitrary Laurent coefficients.

Induction yields $w_r(\Delta^N z)\ge(N+1)r$ for every integer $N\ge0$.
In the associative algebra of $K$-linear operators, $U$ commutes with
$I$, so the ordinary binomial identity in characteristic $p$ gives

$$
(U-I)^{p^j}=U^{p^j}-I,
\qquad \Delta^{p^j}z=P_s^{p^j}(z)-z.
$$

There is no nonlinear-operator binomial error: substitution on
polynomials is linear as an operator. All sums and all iterated
polynomials here are finite; no formal-series convergence or completion
of an operator space is needed. Evaluating a polynomial at $v(\alpha)=r$
can only increase its weighted lower bound. This proves the new estimate.

At $j=0$, the two terms $s\alpha$ and $\alpha^2$ have distinct
valuations $1+r>2r$, so equality $\delta_0=2r$ is justified.
The restriction $j<e$ is necessary for finiteness: at $j=e$ the
displacement vanishes. No sharpness claim at higher $j$ is established.

The coordinator proposed this argument during review; B4 adopted it
after checking it, and this reviewer independently checked it before
reading back its complete implementation. Its proof ownership is not
being assigned to this review.

### 3.2 The older relative-growth argument also checks out

For two points of the small cycle,

$$
P_s(x)-P_s(y)=(x-y)(1+s+x+y),\qquad v(s+x+y)\ge r.
$$

Thus every native step preserves their distance and changes their
difference by a multiplicative factor in $1+\{u:v(u)\ge r\}$.
Finite products stay in that set. Summing $p$ successive $p^j$-step
displacements cancels the common leading displacement because $p=0$
in $K$; each remaining error has valuation at least $\delta_j+r$.
This proves the relative estimate on its stated index range. It is
not inferred from the new absolute lower bound, which alone would
not control the gap between two actual displacement valuations.

Evidence: revised supplement §1 and preserved §1.1, equations (3)–(5).

## 4. Trace-dual estimate and the field different

The report defines $d_L$ using the trace dual of the maximal order
$O_L$. This is the correct field different, not a polynomial-order
or dynamical discriminant.

For every integer $m$, the claimed identity is

$$
\operatorname{Tr}_{L/K}(\mathfrak p_L^m)
 =\mathfrak p_K^{\lfloor(m+d_L)/q\rfloor}.
$$

The floor, sign, and factor $q$ are correct. Indeed, containment of
the left side in $\mathfrak p_K^a$ is equivalent to
$s^{-a}\mathfrak p_L^m\subseteq\mathfrak p_L^{-d_L}$, because this
fractional ideal is stable under multiplication by $O_L$. Its integer
valuation inequality is $m-aq\ge-d_L$. The largest admissible $a$
is exactly the displayed floor. The trace image is a nonzero fractional
ideal; separability supplies nondegeneracy even though $q=0$ as an
element of the characteristic-$p$ field. The argument does not divide
by $q$ inside that field.

Setting $m=q-1-d_L$ produces a trace-one element $w$ with
$v(w)\ge-(d_L-q+1)/q$. For $x$ of nonintegral base valuation $r$,
put $b=\operatorname{Tr}(wx)\in K$. Then

$$
x-b=\sum_\gamma\gamma(w)(x-\gamma x).
$$

If every nonidentity conjugate displacement has valuation at least
$D$, the right side has valuation at least $v(w)+D$.
On the other hand $v(b)$ is integral or infinite, so it cannot equal
$r$ and $v(x-b)=\min(r,v(b))\le r$. Hence
$D\le r+(d_L-q+1)/q$. This verifies the general lemma without a
finite-residue-field assumption.

For $x=\alpha$, let $j=e-h$, which lies in $[0,e-1]$.
The actual Galois generator is $\tau=P_s^{p^j}$. Every nontrivial
power's displacement is a sum of equally valued $p^j$-step
displacements, so has valuation at least $\delta_j$. Using the new
bound gives

$$
d_L\ge q-1+q(\delta_{e-h}-r)
 \ge q-1+qp^{e-h}r
 =p^h-1+p^{e-1}(p-1).
$$

The old bound follows from $p^{e-h}\ge e-h+1$. The equivalent
statement $p^{e-1}\le(d_L-p^h+1)/(p-1)$ in revised (11) is correct.
For an actual root its right side is positive, and an optional integer
upper bound is $e\le1+\lfloor\log_p((d_L-p^h+1)/(p-1))\rfloor$.

### Derivative/discriminant guardrail

No derivative or computed discriminant is used to identify $d_L$ in
this proof. That is important: even for the minimal polynomial $m_\alpha$,
the power order $O_K[\alpha]$ need not be $O_L$. Its discriminant
contains the square of its integral index in $O_L$. In this totally
ramified setting one has $d_L\le v_L(m_\alpha'(\alpha))$, with equality
only when the power basis is an integral basis. If $M_e$ is reducible,
its derivative also includes differences from roots outside the
minimal polynomial's conjugacy orbit. It cannot be silently substituted
for the field different. The revised report expressly retains this
warning. A3's separate $(p,e)=(3,2)$ calculation, including any reported
polynomial discriminant, is not evidence used in this review.

Evidence: supplement §2, equations (6)–(11), and report's remaining-lemma
discussion. The trace-dual normalization agrees with the
[Stacks Project, Dedekind different](https://stacks.math.columbia.edu/tag/0BW0);
the discriminant's squared change-of-basis factor follows from its trace
Gram determinant, as defined in [Trace and norm](https://stacks.math.columbia.edu/tag/0BIE).

## 5. Degree-p lower break and fixed-field exclusions

When $h=1$, $v_L(\alpha)=p-1$ is prime to $p$. A nontrivial
order-$p$ automorphism fixes the constant field and has multiplier one
on a uniformizer: that multiplier's order divides $p$ in $k^\times$.
Thus $\tau(t)=t+ct^{b_L+1}+\cdots$ with $b_L\ge1$ and $c\ne0$.
This matches the standard lower-break convention, where
$v_L(\tau(t)-t)=b_L+1$.

For $a>0$ prime to $p$, the first term of $\tau(t^a)-t^a$ is
$ac\,t^{a+b_L}$. If $p\mid a$, that coefficient vanishes and all
remaining terms have strictly greater valuation, since $b_L>0$.
In the convergent uniformizer expansion of $\alpha$, the first term
has exponent $p-1$ and all later differences have strictly larger
valuation. There is no cancellation of that first difference. Hence

$$
p\delta_{e-1}=v_L(\tau\alpha-\alpha)=(p-1)+b_L,
$$

which proves both the equality and the revised lower bound in (12).
The same equality cannot be transferred to $h>1$: then
$v_L(\alpha)=p^{h-1}(p-1)$ is divisible by $p$.

For $e=h=1$ the exact initial displacement gives $b_{L_1}=p-1$.
If a higher small cycle lay in this same field $L_1$, its root field
would have degree divisible by $p$ and at most $p$, hence would equal
$L_1$. Its necessary break would exceed $p-1$, a contradiction.
This excludes the **same first-level field**, not every degree-$p$
field and not a degree-$p$ quotient of an unrelated higher root field.
There is no claim that $L_1$ embeds in every $L_e$.

For a fixed finite $B/K$, all the relevant root fields are separable
subextensions. They lie in the maximal separable subextension of $B/K$,
whose finite normal closure has a finite Galois group. There are thus
only finitely many possible root subfields, even if $B/K$ itself has
an inseparable part. Each has fixed degree and different, so (11)
bounds its possible levels. The maximum over the finitely many fields
proves the assertion; if none exist the assertion is vacuous.

As an optional boundary observation, in equal characteristic with
perfect residue field a degree-$p$ cyclic break is prime to $p$.
Therefore equality in $b_L\ge p^{e-1}(p-1)$ is impossible for $e\ge2$.
The submitted inequality makes no sharpness claim, so this is not a
must-fix. The older bound $e(p-1)$ is also a valid consequence because
$p^{e-1}\ge e$.

Evidence: revised supplement §§3–4, equations (12)–(13).

## 6. Primary-source applicability and subtraction

Primary-source checks were made on 2026-09-09; no manuscript text was
uploaded and no mathematical executable was run.

- [Lindahl–Rivera-Letelier, *Optimal cycles in ultrametric dynamics and
  minimally ramified power series*, Theorem C and Lemma 2.3](https://arxiv.org/html/1311.4478v3).
  The open-unit-disk convention, odd-prime quadratic statement, and
  optimal-radius formula were checked. Here the residue multiplier has
  order one, $1+s$ is not a root of unity, and the accepted reduction
  is minimally ramified. This source owns the small native cycle and
  radius; it does not establish full Galois degree. This review retains
  A3's accepted generic separability and Hensel packaging as inputs.
- [Elder–Keating, *Artin–Schreier–Witt extensions and ramification breaks*,
  §2, Lemma 2.1 and Theorem 2.3](https://arxiv.org/html/2503.16830v1).
  The source explicitly allows arbitrary perfect residue fields, so
  algebraically closed $k$ is within scope. Its normalization gives
  $[L:K]=ef$ and the uniformizer definition of lower groups used above.
  For every positive $b$ prime to $p$, $X^p-X-s^{-b}$ defines a cyclic
  degree-$p$ extension with lower break $b$. These fields show that
  fixed degree alone gives no conductor ceiling. They are not points
  of $P_s$ and are not counterexamples to (LD).
- [Keating, *Extensions of local fields and truncated power series*,
  Theorem 6.1 and opening proof estimates](https://arxiv.org/html/math/0312391v2).
  The theorem assumes $p>3$, a finite extension of $\mathbb Q_p$ with
  restricted absolute ramification, and a specified finite reduction
  index. Its characteristic-zero multiplier increment cannot be used
  over $k((s))$, where $(1+s)^{p^j}-1=s^{p^j}$. B4's explicit
  nonapplication is correct, including the prime-three boundary.
- The Stacks definitions linked in §4 were checked for trace-dual and
  discriminant conventions. The trace-ideal floor formula is proved
  completely in the submitted supplement; no unverified external
  theorem is needed to fill that step.

The new weighted operator estimate is an elementary filtered-algebra
argument; the trace-one argument is classical different theory. Their
combination supplies a useful exponential ramification-cost constraint.
It does not supply an upper bound for the different of the actual
proper-subgroup root fields, and no novelty or priority certification
is inferred from not finding a source that settles (LD).

## 7. Must-fixes and allowed research boundary

**Open must-fixes: zero.** Coverage underlying that conclusion:

| Check | Result |
| --- | --- |
| Valuations and inertia | Base valuation and integer valuation are distinguished; total ramification and cyclic subgroup indices are correct. |
| Displacement induction and cancellations | Both old telescoping and new weighted-polynomial arguments are valid; every index and nonvanishing condition is retained. |
| Trace ideal and different | The floor formula, trace-one choice and inequality direction are correct for the maximal-order different. |
| Degree-p break | Prime-to-p valuation and fixed coefficients justify the unique leading term; the h=1 restriction is essential and present. |
| Fixed-field conclusions | The same-first-level-field exclusion and finite-subfield argument prove exactly the stated claims, without degree uniformity. |
| Source subtraction | Small-cycle theory and classical ramification are credited; inapplicable mixed-characteristic theorems are not imported. |

The coordinator-origin sharpening was independently checked and its
propagation through all final bounds was read back. A concrete optional
observation about unattainable equality in the degree-$p$ bound was
sent to B4; it does not invalidate the retained nonsharp inequality.

Allowed handoff: “The all-odd-prime small-cycle displacement and
ramification-cost bounds are proved, including the sharper exponential
estimate. They exclude reuse of the first-level field and any fixed
finite field for unbounded levels. Full local degree $p^e$ and the
global PC424-D component question remain unproved.”

Do not shorten this to “period forces degree,” “full inertia,” or
“all small cycles form a proved field tower.” Do not treat a varying
high-conductor Artin–Schreier family as a dynamical counterexample.
All conclusions remain auxiliary, with `NO_BAD_EULER_OR_ROOT_NUMBER`.

## 8. Provenance and execution boundary

The research-review skill was used for evidence-backed nonauthor
checking and explicit claim/gap separation. Its external-model workflow
was not run, in accordance with the current-session/no-upload contract.
No extra agent was spawned. The original and revised B4 files were read
in full, with the weighted revision independently checked; only the
relevant accepted A3/E2 proof interface and A4 torsor criterion were
imported. A3 computation
files and outputs were not read as mathematical evidence or rerun.

No first-pass file, author file, shared index, evaluator, Git object,
or PDF was written. No mathematical program was run. The only new file
is this review in its assigned directory. The synchronized final
inspected B4 files have these SHA-256 hashes:

| File | SHA-256 |
| --- | --- |
| `REPORT.md` | `95f398d36ad9e43c5917dcc39cc40294231e9b23fd2875f25c4535868c8ec32d` |
| `PROOF_SUPPLEMENT.md` | `144b88ae2e9310920b1de22783aa551804d82f0ade16dbcca35c81663b617fc9` |
