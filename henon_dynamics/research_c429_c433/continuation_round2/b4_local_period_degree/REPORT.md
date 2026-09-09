# B4/R2: native small periods versus cyclic local extension degree

2026-09-09. Independent proof-only support for A3's local tower. This is
not a reopening of the completed first-pass B4 jet theorem.

## Frozen question

For every odd prime $p$, let $k=\overline{\mathbb F}_p$,
$K=k((s))$, and $v_K(s)=1$. Put

$$
P_s(z)=(1+s)z+z^2.
$$

For every $e\ge1$, is the following implication true?

$$
\begin{gathered}
L/K\ \text{finite cyclic Galois},\quad
\alpha\in L,\quad v_K(\alpha)>0,\\
\alpha\ \text{has ordinary least period }p^e\text{ under }P_s
\end{gathered}
\quad\Longrightarrow\quad [L:K]\ge p^e.                 \tag{LD}
$$

Here “cyclic extension” means separable Galois with cyclic group, not
purely inseparable degree or a cyclic dynamical orbit. One application
of $P_s$ is one native tick. The coefficient field has algebraically
closed residue field and is not a locally compact finite-residue local
field. The valuation on any extension is the unique extension of
$v_K$; normalized integer valuations will be explicitly distinguished.
The ordinary cycle condition includes $P_s^{p^{e-1}}(\alpha)\ne\alpha$.

Success is a full uniform proof or an actual counterexample satisfying
all these hypotheses. A bound merely divisible by $p$, a formal length,
a multiplier calculation, or a one-cycle Galois-transitivity assumption
does not settle (LD). The original global PC424-D component question
remains separate even if (LD) is proved.

## Accepted local input and exact comparison with A3

The current root/Hénon/batch guidance, CONTINUOUS_RUN, and A3's
[round-2 freeze](../a3_wild_local_tower/REPORT.md) were read first,
followed by the actual A3/A4 first-pass definitions and proofs.
The proof-writer skill is used to preserve the exact claim and report
an honest missing lemma.

The accepted
[A3 local factor](../../lanes/a3_wild_tower/REPORT.md)
is the unique monic Hensel factor
$M_e\in k[[s]][z]$ of

$$
Q_e(z,s)=\frac{P_s^{p^e}(z)-z}{P_s^{p^{e-1}}(z)-z}
$$

with reduction $z^{p^e}$. It has $p^e$ distinct generic roots,
forming one native ordinary cycle, all of valuation $(p-1)/p$.
These statements are source-dependent accepted inputs, not new B4
results or assumptions of transitive Galois action.
Every point in (LD) belongs to this factor: its ordinary least period
makes $Q_e(\alpha)=0$, while $v_K(\alpha)>0$ makes the complementary
Hensel factor a unit at $\alpha$, since that factor is nonzero at
$(s,z)=(0,0)$. Thus passing to $M_e$ does not narrow (LD).

For any such root $\alpha$, its field $K(\alpha)$ already contains
every root, because they are its polynomial iterates. Since $M_e$ is
separable, this is its splitting field and is finite Galois. Galois
commutes with the single native cycle and therefore embeds faithfully
in $C_{p^e}$. Thus

$$
[K(\alpha):K]=p^h,\qquad 1\le h\le e,
$$

and $K(\alpha)/K$ is cyclic. In particular **the cyclicity hypothesis
in (LD) is automatic for the minimal root field**. The full (LD) claim
is equivalent to $h=e$, not a weaker local-period lemma which can be
imported before proving A3's full inertia. The
[accepted A4 torsor criterion](../../lanes/a4_witt_local_data/PROOF_SUPPLEMENT.md)
also identifies this condition with the nonzero full-layer
Artin–Schreier class in A3's current task.

## Completed proof outcome

**NOT CURRENTLY JUSTIFIED** for the uniform (LD) claim. This lane
constructs no counterexample. The original question survives unchanged
and is not promoted to a theorem or an admitted paper.

The [complete proof supplement](PROOF_SUPPLEMENT.md) proves the following
auxiliary statements for every odd $p$ and every $e\ge1$. Write
$r=(p-1)/p$, let $L=K(\alpha)$ have degree $p^h$, let $d_L$ be
its integer-normalized different exponent, and put
$\delta_j=v_K(P_s^{p^j}(\alpha)-\alpha)$ for $0\le j<e$.

1. **Native displacement:** $\delta_0=2r$ and
   $\delta_j\ge(p^j+1)r$.
2. **Necessary ramification cost:**

   $$
   d_L\ge p^h-1+p^{e-1}(p-1).
   $$

3. **Degree-$p$ alternative:** if $h=1$, its unique lower break is

   $$
   b_L=p\,\delta_{e-1}-(p-1)\ge p^{e-1}(p-1).
   $$

   The accepted first-level field has break exactly $p-1$, so it
   contains no small native $p^e$-cycle with $e\ge2$.
4. **Fixed-field finiteness:** no single finite extension $B/K$
   contains small native cycles of arbitrarily high $p$-power period.

The weighted substitution proof of statement 1 was proposed by the
coordinator and independently verified by B4. It strengthens B4's
earlier linear estimate $\delta_j\ge(j+2)r$, whose proof is
preserved in Section 1.1 of the supplement. All prospective conclusions
use the stronger estimate. The trace-dual argument and the
prime-degree uniformizer argument use the actual Galois generator
$P_s^{p^{e-h}}$, never an assumed field action of the single native
step.

## Exact remaining lemma and reusable interface

For an individual pair $(p,e)$, (LD) is equivalent to

$$
\operatorname{Gal}(K(\alpha)/K)
 =\langle P_s\rangle
 \quad\text{as permutations of the small root set}.
$$

Thus the missing step is still exclusion of all proper rotation
subgroups; cyclicity by itself supplies no additional leverage.
The new inequality shows that any putative smaller field must pay
an exponentially increasing conductor cost. It gives no upper bound
on that conductor. An estimate

$$
d_L<p^h-1+p^{e-1}(p-1)\quad\text{whenever }h<e
$$

would be one sufficient extra lemma, but it has not been proved and is
not asserted to be necessary or equivalent to (LD).

For A3 the interface is: accepted one-cycle/separability/slope input
implies the four statements above; the first-level root field cannot
be reused to realize higher native periods. Neither a field tower
$L_1\subset L_2\subset\cdots$ nor equality of first degree-$p$
quotients across levels is assumed or established. Varying
high-conductor fields of the same degree remain possible under these
necessary conditions. The different in the inequality is the
different of the **field**, not the discriminant of a possibly
nonmaximal polynomial order; substituting a polynomial discriminant
requires the separate integral-index relation.

## Primary-source access and subtraction

- Lindahl–Rivera-Letelier,
  [Theorem C and Lemmas 2.1–2.3](https://arxiv.org/html/1311.4478v3):
  the relevant statements and local-cycle discussion were directly
  read. Existence, uniqueness, separability and slope are accepted
  source-owned inputs. They do not assert full Galois degree.
- Elder–Keating,
  [Section 2](https://arxiv.org/html/2503.16830v1):
  the introduction, Lemmas 2.1–2.2, and Theorem 2.3 with the relevant
  proof passages were directly read. Their perfect-residue-field
  hypotheses include $k$. In particular $Y^p-Y=s^{-b}$ has
  cyclic degree $p$ and lower break $b$ for arbitrary positive
  $b$ prime to $p$. This explains why cyclicity alone cannot cap
  the conductor; these extensions are not periodic-point
  counterexamples to (LD).
- Keating,
  [Theorem 6.1 and opening proof estimates](https://arxiv.org/html/math/0312391v2):
  the introduction, exact hypotheses, and relevant estimates were
  directly read. The theorem requires a finite extension of
  $\mathbb Q_p$, $p>3$, restricted absolute ramification, and a
  specified reduction index. It cannot be imported into this
  equal-characteristic setting or used to cover $p=3$.

These are passage-level verifications, not claims of reviewing all
three papers. The weighted-operator and trace-dual arguments are
elementary techniques with explicit proofs, not claims of novel
general ramification theory. Targeted searches did not locate an
applicable source that proves (LD); that search outcome is not evidence
that the statement is new or false.

## Verification and execution boundary

Author audit checked the operator identity, evaluation inequality,
trace-ideal exponent and inequality direction, actual Galois
generator, prime-to-$p$ uniformizer valuation, and fixed-field
quantifiers. A nonauthor internal reviewer is checking this final
stronger version separately; that check is not external peer review.

Mathematical executions in this lane: **zero**. No old-file edits,
shared-index/Git changes, PDF/evaluation work, external upload, or
additional subagents were used. Only this report and its new
supplement were written in the assigned directory. A3's separately
allocated diagnostic is not a B4 execution or a uniform proof here.

NO_BAD_EULER_OR_ROOT_NUMBER.
