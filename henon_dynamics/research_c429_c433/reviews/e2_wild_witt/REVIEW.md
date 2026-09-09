# E2 independent review: A3 wild cluster and A4 Witt resolvent

2026-09-09 UTC. Internal current-team **nonauthor** review by
/root/c429_e2_wild_witt_review. This is a mathematical/source review,
not human peer review, formal Route-A evaluation, or manuscript admission.
Write ownership is restricted to this review directory.

## 1. Outcome and original contract

**The A3/A4 join is mathematically valid as a scoped auxiliary interface.**
I found no invalid trace-resolvent identity, no subgroup-direction error,
and no hidden assumption that the degree-\(p^e\) torsor is already a field.
The characteristic-\(3\) example and truncated-Witt counterfamily check
by hand. The newly added B4 ambient-jet application also checks.

**It does not close PC424-D or currently justify an independent
paper-level contract.** The exact original question remains classification
of all geometric irreducible components of

\[
\overline{\Phi}_{p^e}(x,c)
=\overline{\frac{f_c^{\circ p^e}(x)-x}
 {f_c^{\circ p^{e-1}}(x)-x}},
\qquad f_c(x)=x^2+c,
\]

over \(\overline{\mathbb F}_p\), for every odd \(p\) and every \(e\ge1\),
on the full affine parameter plane. One application of \(f_c\) is one
tick; \((p,e)=(3,1)\) is not removed.

There are still two unproved obligations in the proposed route:
evaluate the parabolic cluster's explicit first AS class uniformly at
higher levels, and prove transitivity of the global native-cycle quotient
or classify it completely. The first would not prove the second.
A different argument could bypass this route; its current gap is not
an impossibility theorem.

Final review disposition:

- Mathematical must-fixes to the stated auxiliary results: **0**.
- Source-scope must-fixes: **1 raised, independently read back and closed**.
- Open must-fixes: **0**.
- Original-contract closure: **UNCLOSED**, as the authors already state.
- Admission: not recommended from this join alone; classical inputs and
  short adaptations must be subtracted.

## 2. Numbered findings and revision closure

### MF1 — singularity citation must retain \(n>3\): CLOSED

The initial A3 source paragraph cited Doyle et al., Proposition 7.1,
then referred to the wild-collision singularity without restating its
\(n>3\) hypothesis. The proposition cannot establish singularity for
\((p,e)=(3,1)\); its proof uses \(n>3\) to make the parameter derivative
vanish. The point/orbit lifting in Proposition 6.14 and Corollary 8.4
likewise explicitly excludes \(p\mid n\).
[Doyle et al., §§6–8](https://arxiv.org/html/1703.04172v2#S7)

The author revised only A3 REPORT.md, as requested through the root.
I independently reread the revised source paragraph and disposition:
the \(p^e>3\) restriction and \((3,1)\) exception are explicit; the
original smooth germ is distinguished from its ramified pullback;
and A3's proof is explicitly independent of singularity. **MF1 is closed.**

The exception is substantive. In A4's characteristic-\(3\) example,

\[
M(w,t)=w^3-tw^2-t^2w+t+t^3,\qquad c=1-t-t^2,
\]

we have \(M_t(0,0)=1\) and \(dc/dt(0)=-1\). Hence the original
dynatomic germ at this cluster is smooth. The substitution
\(t+t^2=s^2\) is a ramified base change, and its pulled-back germ can
be singular without contradicting that fact. No correction to the
Hensel/valuation proof was necessary.

### N1 — exact small-cycle source subtraction: incorporated

The source overlap is stronger than just the iterate-order formula.
Lindahl–Rivera-Letelier Theorem C already supplies the unique small
native cycle and its optimal radius for this exact quadratic family:
\(\lambda=1+s\), residue order \(q=1\), and \(\lambda\) not a root of
unity. Thus the canonical Hensel factor is useful algebraic packaging
of a source-owned cycle/valuation result.
[Lindahl–Rivera-Letelier, Theorem C](https://arxiv.org/html/1311.4478v3#S1.SS5)

The author added this exact subtraction, explicitly for all odd \(p\)
and all \(e\), after formula (1), and repeated it in the disposition.
I read both revisions. The report now makes no literature-novelty claim
for the AS extraction either. This attribution recommendation is satisfied.

### N2 — explicit test versus evaluated test: continuing boundary

The formula defines a calculable Laurent-series class, but neither
report proves a uniform surviving coefficient after AS reduction.
“Explicit local AS test” is accurate; “all-level full inertia”,
“computed tower”, and “Witt recovery from ordinary traces” are not.
Section 6 below makes the calculability and missing proof separate.
This is not a demand to solve an expressly unproved conjecture before
retaining the auxiliary result.

## 3. A3 mathematical check

Use \(R=k[[s]]\), \(K=k((s))\), \(n=p^e\), \(m=p^{e-1}\),
\(\lambda=1+s\), \(x=z+\lambda/2\), and \(c=(1-s^2)/4\).
The coordinate identity gives \(P_s(z)=\lambda z+z^2\) exactly.

The source's odd-characteristic criterion applies even for \(p=3\):
\(a_1=1\ne0\) and \(a_2=0\ne a_1^2\). Its odd-prime proof uses
\(p\ge3\), not \(p\ge5\). Definition 3.4 gives the claimed all-iterate
order, with higher propagation importing the established theorem
in Lemma 3.5. This review does not claim to reprove that external input.
[Lindahl–Rivera-Letelier, §§3.2 and 4.2](https://arxiv.org/html/1311.4478v3#S4.SS2)

The remaining steps check:

1. The order difference is \(p^e\), so
   \(Q_e(z,0)=z^nV(z)\) with \(V(0)\ne0\). Coprime Hensel
   factorization gives the unique monic pair with those specified
   reductions. “Unique factor” here means the canonical cluster
   factor, not an irreducible factor.
2. R5's actual \(c=0\) proof establishes generic separability and
   coprimality with the preceding iterate. These survive the displayed
   field extension. Thus every cluster root has exact native period
   \(n\); \(P_s\) permutes the \(n\) roots, so they form one native cycle.
3. Positive valuation is preserved because \(\lambda+\alpha\) is
   a unit. The identity \(Q_e(0,s)=s^{n-m}\), with
   \(N_e(0,s)\in R^\times\), gives the common valuation
   \((n-m)/n=(p-1)/p\).
4. Galois commutes with the native cycle. Its faithful image is
   \(H_e\le C_n\), not automatically \(C_n\). A root stabilizer in
   this image is trivial: all other roots are its iterates and
   already lie in its root field. Thus every irreducible factor has
   degree \(|H_e|\), and there are \(n/|H_e|\) factors.
5. The denominator of the valuation forces \(p\mid |H_e|\).
   It proves full inertia for \(e=1\), but does not distinguish
   \(p,p^2,\ldots,p^e\) for \(e>1\). Algebraically closed residue
   field rules out a nontrivial residue extension.

The prime-level lower break \(p-1\) also checks. With
\(v_L(s)=p\), \(v_L(\alpha)=p-1\), the summands in
\(\sigma\alpha-\alpha=s\alpha+\alpha^2\) have different valuations,
and the second has order \(2(p-1)\). The leading-uniformizer argument,
using \(p\nmid v_L(\alpha)\), gives break \(p-1\).
For larger inertia degree this primeness condition fails. A3 correctly
does not repeat the inference without additional data.

Accordingly, the proof keeps four different assertions separate:
one Hensel cluster; one native orbit; one local Galois orbit; one
global component. Only the first two are proved here for all \(e\);
the third is proved at \(e=1\); the fourth is not established.

## 4. A4 extraction, AS logic, and characteristic-\(3\) example

### 4.1 The identities work on disconnected torsors

For the stated finite étale rank-\(n\) torsor \(A/B\), the invariant
algebra is \(B\). Over a separable closure the values of \(x\) are
distinct. Lagrange interpolation of \(T^{n-1}\) gives

\[
\sum_{i=0}^{n-1}
\frac{(\sigma^i x)^{n-1}}{M'(\sigma^i x)}=1.
\]

Hence \(z=x^{n-1}/M'(x)\) is well-defined and has native trace one.
For \(y=-\sum_{i=0}^{n-1}\bar i\,\sigma^i z\), the coefficient of
each \(\sigma^jz\) in \(\sigma y-y\) is \(1\), including the wrapped
coefficient \(-\overline{n-1}=1\). The sign is correct.

Thus \(y^p-y\in B\). On a geometric fibre \(y\) has exactly the
\(p\) values \(y_0+\mathbb F_p\), each \(n/p\) times, proving
\(A^{\langle\sigma^p\rangle}=B[y]\) of rank \(p\).
No averaging by \(1/n\) or assumption that \(A\) is a field occurs.

Changing the trace-one element changes \(y\) by an element of \(B\),
so changes \(a_0\) by an AS coboundary. This legitimizes the simpler
trace-one element in the example. The weighted construction is
additive Hilbert 90, not a new general resolvent theorem.
[Elkies, Theorems 4.30–4.33](https://people.math.harvard.edu/~elkies/M250.01/index.html)

### 4.2 Nonzero first quotient forces full inertia

The potentially counterintuitive subgroup direction is correct.
Every proper subgroup of \(C_{p^e}\) lies in \(pC_{p^e}\), so it
has zero image in \(C_{p^e}/pC_{p^e}\cong C_p\). A4's AS quotient
realizes exactly that reduction. Nontriviality therefore forces
the full subgroup, not merely a subgroup of order at least \(p\).

Over algebraically closed \(k\), the regular part of \(k((t))\) is
AS-surjective. Removing \(ct^{-pj}\) by subtracting
\(\wp(c^{1/p}t^{-j})\) terminates on the finite polar part. A nonzero
remaining prime-to-\(p\) pole cannot be an AS coboundary. A raw pole
can cancel, and a regular class could represent residue data over a
different residue field; the report retains both necessary qualifications.

### 4.3 The explicit quadratic test

Substitution \(r=t-w\) gives \(M=t-tr^2-r^3\), and \(y=1/r\) yields
\(y^3-y=1/t\). Direct substitution gives

\[
\sigma w=w+w^2-t^2-t=f_c(2+w)-2.
\]

The nontrivial degree-\(3\) AS extension and this order-\(3\)
automorphism therefore realize the original quadratic native cycle.
The trace is \(w+\sigma w+\sigma^2w=t\); for \(z=w/t\),

\[
-\sigma z-2\sigma^2z=w^2/t-t=1/(t-w).
\]

The last identity follows by multiplying by \(t-w\) and using \(M=0\).
Thus the AS pole was extracted by the native formula, not introduced
as an unrelated extension.

The valuation \(v_t(w)=1/3\) makes \(w\) a uniformizer upstairs.
The smallest term of \(\sigma w-w\) has upstairs order \(2\), giving
break \(1\) and normalized fixed length \(2\). After \(t+t^2=s^2\),

\[
1/t=(1+t)/s^2=s^{-2}+\text{a regular series}.
\]

The reduced pole has order \(2\), giving break \(2\) and fixed
length \(3\) over the new base, in agreement with A3.
The original parameter-fibre length \(3\), original native fixed
length \(2\), and pulled-back normalized fixed length \(3\) are
different observables.

## 5. Witt lengths, normalization, and the counterfamily

A4 correctly requires a full compatible reduced Witt vector, with
the marked native generator acting by addition of
\((1,0,\ldots,0)\). The first resolvent does not provide its higher
coordinates.

The upper-break maximum rule applies to this residue field:
Elder–Keating Theorem 2.3 explicitly allows arbitrary perfect residue
fields. Its direct proof was read, including the valuation comparison
excluding cancellation of the two largest candidate jumps.
[Elder–Keating, Theorem 2.3](https://arxiv.org/html/2503.16830v1#S2)
Generator-compatible equations and classical jump constraints are
explicit in Obus–Pries Lemmas 3.3–3.5; their numbering conventions
agree with A4.
[Obus–Pries, §§2.4–3.3](https://www.math.colostate.edu/~pries/Preprints/10pries_obus409_JPPA.pdf)

The inverse Herbrand slopes \(1,p,\ldots,p^{e-1}\) give

\[
b_i=b_{i-1}+p^{i-1}(u_i-u_{i-1}),\qquad
\ell(\operatorname{Fix}\sigma^j)=b_{v_p(j)+1}+1
\]

when \(p^e\nmid j\), exactly as stated. The identity iterate fixes
the whole formal disc, not a finite-length scheme.

The normalization/fibre identity also checks. In
\(0\to R\to S\to C\to0\), multiplication by \(h\) is injective on
\(R,S\), while \(C[h]\) and \(C/hC\) have equal finite dimensions.
Hence \(\ell(R/hR)=\sum_qv_q(h)\). This does not identify singular
fixed-point lengths with normalized ones. The quotient parameter's
order in \(h\) and the branch list remain extra data.

For
\(\mathbf a_M=(t^{-(p-1)},0,\ldots,0,t^{-M})\),
\(p\nmid M\), \(M>p^{e-1}(p-1)\), the first \(e-1\) coordinates
are fixed but the last upper break is \(M\). The top native fixed
length is the claimed affine function of \(M\), with slope
\(p^{e-1}\), and is unbounded. The characteristic-\(p\) ghosts
depend only on the first coordinate. Every lower break is
\(p-1\pmod p\), so every finite fixed length is divisible by \(p\).
The stated multiplication/twisted traces are all zero. The fixed
ideals are stable under the native action, so these operators are
indeed defined on those quotients.

The actual B4 Lemma 4 proof was also read. Here pullback on
\((u)/(u^{N+1})\) is triangular with every diagonal entry \(1\),
giving \((T-1)^N\) for every prescribed \(N\).
That ambient dimension is chosen externally, not the dynamically
defined fixed-ideal colength. A4's new application is sound.

This is a complete obstruction in the general local cyclic-cover
category, using the inherited R4 trace-blind mechanism. The family
has not been constructed inside the quadratic dynatomic tower.
It proves neither a quadratic counterexample nor a universal no-go
for richer geometric or nonlinear jet data.

## 6. Calculable remaining lemma, not an evaluated tower

**Calculable for each fixed pair: yes. Evaluated uniformly: no.**
A3 supplies the exact \(R\)-polynomial \(M_e\), native action and
invariant field \(K\). A4's formula therefore specifies a class in
\(K/\wp(K)\) without assuming irreducibility. Its nonvanishing is
equivalent to local irreducibility. The remaining assertion is

\[
\operatorname{red}_{\rm AS}(a_{0,e})\ne0
\quad\text{for every odd }p\text{ and every }e>1,
\]

or an exact description of its failures.

An elementary precision bound makes “calculable” concrete. Put
\(D=v_s\operatorname{Disc}_z(Q_e)\) and
\(\delta=v_s\operatorname{Disc}_z(M_e)\). Generic separability makes
\(D\) finite. The Hensel factors are integral with unit resultant,
so the discriminant product identity gives \(0\le\delta\le D\).
On the free order \(\mathcal E=R[z]/M_e\), multiplication by
\(M_e'(z)\) has determinant equal, up to sign, to
\(\operatorname{Disc}(M_e)\). Its adjugate has integral entries.
Consequently

\[
\frac{z^{n-1}}{M_e'(z)}\in s^{-\delta}\mathcal E.
\]

The native action preserves \(\mathcal E\), by substitution
\(z\mapsto P_s(z)\) and its inverse iterate. Hence
\(y\in s^{-\delta}\mathcal E\) and
\(a_{0,e}\in s^{-p\delta}\mathcal E\). Since \(a_{0,e}\in K\) and
the monic basis starts with \(1\),

\[
a_{0,e}\in s^{-pD}R.
\]

Only finitely many negative coefficients can affect its AS class.
Coprime Hensel lifting and rational operations with tracked
determinant valuation determine them at adequate precision for
a fixed pair. This is an in-principle, potentially expensive finite
procedure, not a computation performed in this review.

The reports supply no uniform leading coefficient, recurrence,
cancellation estimate or vanishing classification for \(e>1\).
Nor is the first AS quotient at level \(e\) automatically the already
nontrivial quotient at level \(1\): their generic native cycles
are different. Any useful relation between them requires proof.

Even universal local nonvanishing would give a full rotation only
in the stabilizer of the global cycle-orbit meeting this cluster.
R5's formula
\(\#\operatorname{Irr}(\overline\Phi_{p^e})=\sum_jp^{e-h_j}\)
still requires the global cycle-orbits and the other stabilizers.
No evidence here removes that independent obligation.

## 7. Allowed claims and ownership ledger

| Statement | Review status and ownership |
| --- | --- |
| Generic separability, exact period, reducedness, conditional component formula | Imported R5; actual used proofs checked. |
| Minimal ramification, unique small cycles, optimal root valuation | Source-owned inputs/consequences, not a new all-level theorem. |
| Canonical Hensel factor and finite étale native torsor | Correct useful packaging; not necessarily a field for \(e>1\). |
| \(p\mid|H_e|\), \(H_1=C_p\), prime-level break \(p-1\) | Correct short local consequences. |
| Explicit trace-one resolvent, also for disconnected torsors | Correct classical algebra adapted to the native coordinate. |
| Nonzero reduced AS pole implies full \(C_{p^e}\) inertia | Correct exact conditional test. |
| Full Witt poles determine normalized native fixed lengths | Correct established ramification theory using extra geometric data. |
| Truncated Witt/ghost/trace/ambient-spectrum data miss top length | Correct general local-cover counterfamily; no quadratic realization. |
| Higher-level quadratic AS nonvanishing | **Unproved**. |
| All-\((p,e)\) geometric component classification | **Unclosed**; no admission from this join alone. |

The useful increment is a composable local test and an exact data-loss
boundary. It is neither restoration of multiplicities from ordinary
traces nor a target arithmetic spectral bridge.

## 8. Actual scope and execution record

Read root/Hénon/batch AGENTS, SCOUT_PLAN, current-state entry, and
batch workflow. Used research-review in its local nonauthor mode;
no external reviewer/model upload was invoked.

Actual mathematical files read:

- A3 REPORT.md, including its complete proof/handoff and targeted
  read-back of the final source-scope/subtraction revisions.
- A4 REPORT.md and full PROOF_SUPPLEMENT.md, including the B4
  addition made during this review.
- Original PC424-D and R5 FROZEN_CONTRACTS.md.
- R5 PROOF_AND_GAPS.md and SOURCE_AUDIT.md.
- R4 PROOF_PACKAGE.md, especially actual trace-blindness proofs.
- B4 PROOF_SUPPLEMENT.md, with §4 Lemma 4 checked for the
  characteristic-\(p\) application. No verdict on B4's separate
  good-model contract is intended.

Primary sources opened and inspected:

- Lindahl–Rivera-Letelier, arXiv:1311.4478v3: Theorem C,
  Definition 3.4, Lemma 3.5 statement, Lemma 3.6 proof,
  Proposition 4.4 and entire odd-prime proof; nearby §5 statements.
- Elder–Keating, arXiv:2503.16830v1: ramification conventions,
  reduced-vector definitions, Theorem 2.3 and complete proof.
- Obus–Pries, institution-hosted PDF: §§2.4–3.3, especially
  generator-compatible Lemma 3.3 proof and Lemmas 3.4–3.5.
  Browser text inspection only, not a local PDF/page-image audit.
- Elkies, author-hosted notes: Theorems 4.30–4.33 and the
  displayed additive cocycle construction.
- Doyle et al., arXiv:1703.04172v2: Proposition 7.1 and full proof,
  Proposition 6.14 and proof, Corollary 8.4 and proof.

Three bounded public-source queries tested nearby terminology:
“optimal cycles” “irreducible” polynomial characteristic;
“dynatomic” “Artin-Schreier” quadratic; and
“minimally ramified” “Galois” quadratic periodic points.
They supplied no additional applicable theorem. This is not a
literature-completeness or worldwide-priority certificate.

Mathematical program executions: **0**. New hand checks only.
No old rerun, build, census, manuscript, evaluator, Git, shared-index,
frozen-package, configuration, or external-upload write occurred.
Only this review file was written.

**NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.**
