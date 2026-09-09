# LG4 R6 — wandering singleton source check and one algebraization bridge

2026-09-09 UTC. B1. Only this new report is written.

## Outcome and unchanged claim

**NOT CURRENTLY JUSTIFIED / FULL_QUESTION_UNCLOSED.** Three new targeted
search batches did not yield an applicable theorem. The precise additional
bridge below remains unproved. No all-modulus false positive, new complete
question, paper admission, or mathematical execution is reported.

The original question remains, for every
$F\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ with integral inverse and
every $P,Q\in\mathbb Z^2$,
$$
Q\in\{F^n(P):n\in\mathbb Z\}
\quad\Longleftrightarrow\quad
(\forall m\ge2)(\exists n_m\in\mathbb Z)\quad F^{n_m}(P)\equiv Q\pmod m.
\tag{LG4}
$$
All mixed moduli and the native two-sided clock are retained. The already
accepted periodic-target, bounded-degree, virtual-centralizer, and
return-ideal controls are inputs, not re-proved results. This pass concerns
the remaining wandering-singleton case with exponential Hénon degree growth.

Actual local entry reads: the prior B1 report's final source gap and
conclusion; the inherited
[SOURCE_AUDIT](../../../research_c424_c428/continuation_round4/arithmetic/SOURCE_AUDIT.md);
the complete round-2 B1 report; and the exact native-time interface in
[R4 proof §3](../../../research_c424_c428/continuation_round4/arithmetic/PROOF_PACKAGE.md).
Research-lit, proof-writer, and the batch workflow were followed, with the
selected-team/primary-source fallback and no external model upload.

## Primary-source evidence, not keyword transfers

| Source and actual reading | Relevant output and decisive limitation |
| --- | --- |
| Amerik–Kurlberg–Nguyen–Towsley–Viray–Voloch, *Evidence for the Dynamical Brauer–Manin Criterion*, Experimental Mathematics 25 (2016), 54–65: [updated author copy](https://sites.math.washington.edu/~bviray/papers/AKNTVV_EvidenceDynBM.pdf), §4.1–4.2 definitions and full Theorems 4.2–4.4, complete local proof, uniformization alternative, model lemma/global proof, and Proposition 4.9 with its proof; [arXiv v2](https://arxiv.org/pdf/1305.4398v2), corresponding statements and full Proposition 4.16 proof also checked. | The avoidance theorem requires an iterate-invariant/preperiodic target. Its local proof uses preservation of the target ideal; the analytic proof propagates a zero along translated times. Neither applies to a wandering singleton. The singleton proposition uses nonperiodic reductions, unavailable for integral automorphisms. Its negative example is a forward-orbit predecessor, already in the two-sided orbit. The newer local theorem relaxes the ambient smoothness requirement, not target invariance. |
| Keping Huang, *A Gap Principle for Subvarieties with Finitely Many Periodic Points*, Canadian Mathematical Bulletin 63 (2020), 382–392: [publisher article](https://doi.org/10.4153/S0008439519000481); streamed publisher PDF, printed pp. 382–390, including full Theorems 1.1/1.4, §2 setup, §3 avoidance proof, and Proposition 4.2 proof. | Theorem 1.1 bounds the number of actual forward hits. Theorem 1.4 targets the periodic points inside the subvariety, using a positive-density prime set and backward preimages. For $V=\{Q\}$ with wandering $Q$, that target list is empty. Its printed uniformity also has the elementary problem recorded below; no positive inference here relies on this theorem. |
| Farrukh Mukhamedov, *Effective Strassmann Certificates for Local p-adic Dynamical Mordell–Lang Interpolants*, [arXiv:2607.14339v1](https://arxiv.org/html/2607.14339v1), preprint: §3 setup, Lemma 3.1 and Corollary 3.3 with proofs, full Proposition 7.1/proof, and §§13–14 limitations. | Local analytic interpolation and an arc-gcd bound common zeros. The required coefficient congruence is $f=x+p^q\Phi$, $q(p-1)>1$, after legitimate return-map/chart reductions. The result does not identify a $p$-adic common zero with an integer time, nor descend its polynomial across primes. The preprint itself states its local scope. No algorithm or full-paper correctness certification is imported. |

The older-v2 Proposition 4.16 is the updated author copy's Proposition 4.9;
their numbering is not interchanged. This pass did not re-read every proof
in either entire article. The publisher PDF for Huang failed through the
web reader but was actually read through text extraction from a stream;
no PDF was saved or built. Search results on split maps, abelian varieties,
periodic-point counts, and unrelated adelic varieties were not treated as
Hénon orbit-separation theorems.

### Necessary topology and time checks

These are elementary checks on the frozen LG4 object, not new hypotheses.

1. Both $F$ and $F^{-1}$ extend over $\mathbb Z$, so every reduction is a
   permutation. Every reduced $Q$ is periodic, including at every prime.
   Removing a finite bad set cannot make the singleton proposition's
   nonperiodic-reduction hypothesis hold.
2. At each modulus, the forward and two-sided finite orbits coincide.
   Their closures in $\widehat{\mathbb Z}^{\,2}$ therefore coincide, but
   their integer-point orbits need not. A predecessor is not an LG4
   counterexample. For a genuine off-two-sided-orbit pair, an applicable
   forward avoidance theorem would suffice; none was obtained here.
3. All mixed-modulus incidence is simultaneous finite-place approximation
   of the same fixed $Q$, not merely membership in each separate local
   closure. The product of local closures can discard native phase
   compatibility. The closure of our integral orbit lies in
   $\prod_p\mathbb Z_p^2$; a theorem imposing an archimedean approximation
   would ask for extra data absent from LG4.
4. A theorem giving even one avoiding prime power would settle separation
   for that pair; positive density would be more than enough. The issue
   with the new avoidance source is its target, not that density is weak.
   Conversely, a density/sparsity statement about actual integer hitting
   times does not bound congruence-only times.

### An additional caution on the printed Huang avoidance statement

Theorem 1.4 quantifies uniformly over all nonpreperiodic integral initial
points after selecting its positive-density primes. That quantifier is
not safe as printed. Take
$$
f(x,y)=(x,y+x^2),\qquad V=\{(0,0)\}.
$$
For any selected rational prime $p$, the integral point $a=(p,p)$ is
wandering, since
$$
f^n(a)=(p,p+n p^2),
$$
but its reduction equals the fixed target at every iterate. The proof's
last passage on printed p. 388 excludes sufficiently late **first** hits,
then states exclusion of all late hits; early entry into the periodic
cycle is not excluded. This control tests only that source statement.
It is not an LG4 false positive, does not challenge the accepted
periodic-target result, and is not offered as another research question.
The independent wandering-target mismatch already prevents its use here.

## One attempted bridge: a common irreducible time equation

### Assumptions, notation, and dependency map

Assume the right side of LG4 and a wandering $P$. The accepted R4 theorem
gives a unique native profinite time
$$
\tau\in\widehat{\mathbb Z},\qquad \theta_P(\tau)=Q.
$$
Write $\tau_p\in\mathbb Z_p$ for its $p$-component. This notation uses the
full mixed-modulus time, not independently chosen local times.

The attempted route is:

1. Pull the two equations of the **same integral singleton** back along
   each legitimate local analytic time branch.
2. Descend their selected common zero to one irreducible polynomial over
   $\mathbb Q$, independent of $p$ — the missing step.
3. Use transitivity and Chebotarev to show that polynomial is linear,
   then use every $\tau_p\in\mathbb Z_p$ to obtain an integer time.

The candidate missing implication is precisely
$$
\theta_P(\tau)=Q\in\mathbb Z^2
\quad\Longrightarrow\quad
\exists A(T)\in\mathbb Q[T]\text{ irreducible},\ \deg A\ge1,
\quad A(\tau_p)=0\text{ for every prime }p.
\tag{ITA — unproved}
$$
This is a proof interface for LG4, not a narrowed replacement question or
an established arithmetic improvement. In fact, the argument below shows
that obtaining this implication would already settle the remaining case.

### What the singleton actually gives locally

Using the accepted interpolation interface, choose a return modulus
$M_p>0$ and the branch $a_p\equiv\tau\pmod {M_p}$, so that a local analytic
map $\Gamma_p$ interpolates $F^{a_p+M_p n}(P)$. The branch keeps the finite
residue clock. Its selected local time is
$$
z_p=(\tau_p-a_p)/M_p\in\mathbb Z_p,\qquad \Gamma_p(z_p)=Q.
$$
The two restricted series
$$
h_{p,1}(z)=\Gamma_{p,1}(z)-Q_1,\qquad
h_{p,2}(z)=\Gamma_{p,2}(z)-Q_2
$$
cannot both vanish identically: that would make the infinite return
subsequence constant, contradicting wandering. Their nonzero ideal in
$\mathbb Q_p\langle z\rangle$ has a generator, and Weierstrass preparation
gives a nonzero polynomial factor $W_p(z)\in\mathbb Q_p[z]$ with
$W_p(z_p)=0$. This is just the local arc-ideal/Weierstrass mechanism.

**The exact unproved step:** no argument gives one $A\in\mathbb Q[T]$
irreducible over $\mathbb Q$ that vanishes at all the native times
$a_p+M_pz_p$. The $p$-dependent Weierstrass coefficients, degrees, factors,
and branch choices do not descend by integrality of $Q_1,Q_2$. Integer
values on ordinary iterates do not prove that such a time series is an
algebraic function over $\mathbb Q$. No invariant singleton ideal is
available to propagate the selected zero, and exponential degree growth
does not supply a finite-dimensional elimination argument.

### The conditional arithmetic step is complete

Suppose the output of (ITA) were available. Let $d=\deg A$ and let $L$ be
its splitting field. Characteristic zero and irreducibility give a
transitive Galois action on $d$ distinct roots. If $d>1$, this action has
a derangement: the average number of fixed roots is the number of orbits,
namely one, while the identity fixes $d>1$ roots; hence some element fixes
none. Chebotarev supplies an unramified prime outside the finite set of
denominator/discriminant primes whose Frobenius has that conjugacy class.
The corresponding reduction of $A$ has no linear factor. At such a prime
a root in $\mathbb Q_p$ would give a Frobenius-fixed root (equivalently a
linear factor), contradicting $A(\tau_p)=0$.

Thus $d=1$, so $A$ has one rational root $r$ and $\tau_p=r$ for every
prime $p$. Since every component is in $\mathbb Z_p$,
$$
r\in\mathbb Q\cap\bigcap_p\mathbb Z_p=\mathbb Z.
$$
Consequently $\tau=r$ diagonally and $Q=F^r(P)$, with negative as well as
positive $r$ allowed. This uses only the accepted native-time interface
and the classical Frobenius/Chebotarev mechanism; the latter is also
explicitly present in the primary Huang proof, not a new result here.

Irreducibility and a single equation across primes cannot be deleted.
For example, a profinite number with $\tau_2=1$ and $\tau_p=0$ at every
odd prime satisfies $\tau_p(\tau_p-1)=0$ everywhere but is not a diagonal
integer. This is a control on a proposed algebraization inference, not
an example arising from any asserted Hénon orbit. Likewise, an equation
only away from a finite set does not control the omitted time components.

## Exact bounded retrieval and final disposition

Exactly three new search batches, four literal queries each, were used;
there were no recency/domain filters beyond the literal `site:` query.
Subsequent opens/finds and publisher-stream reads followed these hits.

1. `"dynamical Hasse principle" "étale" points wandering`;
   `"dynamical Brauer-Manin" "automorphism" singleton`;
   `"Hénon" "orbit" "local-global" 2025 2026`;
   `site:arxiv.org "dynamical" "orbit" "avoidance" point étale`.
2. `"étale" "orbit" "avoidance" arithmetic points`;
   `"dynamical Hasse principle" "zero-dimensional"`;
   `"dynamical Brauer-Manin" "Hénon" "point"`;
   `"polynomial automorphism" "singleton" orbit`.
3. `dynamical Hasse principle zero dimensional etale endomorphism wandering point Nguyen avoidance`;
   `etale maps avoidance theorem wandering target points local global Bell Ghioca Huang`;
   `polynomial automorphisms affine plane congruence orbit closure Hasse Brauer Manin`;
   `Hénon maps adelic orbit closure integral points local global principle`.

No Zotero/Obsidian tool or relevant locally named PDF was found; the
skill's arXiv helper was unavailable, so the stated web fallback was used.
One combined early output was truncated; unseen portions are not counted
as reading evidence. The relevant primary passages were separately read.

Final verdict: the actual missing arithmetic input is still unproved;
the original full question is unchanged. Bounded retrieval failure does
not establish worldwide open status, novelty, or a universal no-go.
No further search batch, nested agent, external model/API, mathematical
run, Git operation, shared-state change, manuscript, PDF, or Route-B action
occurred. This report contributes zero admitted contracts.

`NO_BAD_EULER_OR_ROOT_NUMBER`.
