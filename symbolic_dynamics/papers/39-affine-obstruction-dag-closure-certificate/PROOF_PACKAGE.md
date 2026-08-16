# Proof Package — Paper 39 / SD-C41

## Claim

### Theorem (relative exhaustion of the frozen affine symbolic branch)

Let $\mathcal A_{14}$ be the exact fourteen-class repair alphabet frozen by
Paper 38, let $\Sigma_{16}$ be the exact sixteen-token frozen instance set,
and let $\mathfrak C_{\mathrm{aff}}(r)$ be the endpoint-typed candidate-state
family carried by nonempty audit-provenance paths, as defined in
`paper39_SOURCE_LOCK.md`. For every integer $r\ge2$ and every
$c\in\mathfrak C_{\mathrm{aff}}(r)$,

$$
\neg\operatorname{Good}(c),
$$

where `Good` is the conjunction of intrinsic source, nonempty
repetition-compatible primitive recurrence, arithmetic selectivity,
same-object determinant ownership, marker compatibility, and survival of the
frozen controls.

Every class in $\mathcal A_{14}$ has a frozen disposition, and every token in
$\Sigma_{16}$ is classified as one theorem-covered frozen family/instance or
one explicit exit. The two mixed classes each contribute one tested token and
one alternative-exit token. There is no catch-all instance token and no claim
about arbitrary compound repairs. Every state in
$\mathfrak C_{\mathrm{aff}}$ has a typed endpoint carrying a proved
obstruction. Hence no successor remains **under this frozen affine
contract**, and the affine branch has terminal status
`CLOSE_ENTIRE_AFFINE_BRANCH`. Exit classifications are not claims that the
corresponding outside construction is impossible.

In the frozen repository snapshot, the historical non-affine registry
predicate is nonempty because `SD-C01`--`SD-C06` were each defined in the
Session-4 preregistration/source lock before their own evaluation. Therefore
the realized post-closure decision is

```text
RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY
```

The decision

```text
STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR
```

is the explicit conditional fallback only when that historical witness set is
empty; it is not realized in the observed snapshot.

Paper 39 has no new candidate mechanism and therefore has strict Route-A tuple

```text
(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL),
```

with `ROUTE_A_REJECTED` and Route B locked.

## Status

`PROVABLE AS STATED`, where “as stated” includes the explicit frozen-contract
and frozen-snapshot qualifiers. The claim does not survive if those qualifiers
are removed.

## Assumptions

1. The hashed final source locks, proof packages, derivation packages,
   Round-2 clues, and Route cards of Papers 35--38 are the predecessor
   authority facts for Paper 39.
2. The retrospective Paper-39 affine encoding consists exactly of the
   fourteen class labels, sixteen stable instance tokens, and endpoint
   families linked by the seventeen internal audit-provenance edges in the
   Paper-39 source lock; it is not an informal universe of all affine
   constructions or compound repairs.
3. A typed object change resets marker, operator, determinant, and ownership
   unless the corresponding frozen edge contains a proof of descent or
   transport. A many-to-one coarse projection cannot weaken an expanded reset
   to a carry/equivalence assertion.
4. The main affine parameter satisfies $r\ge2$. The case $r=1$ is used only
   as the balanced boundary specified by Papers 36 and 38.
5. Canonical modular weights in the Paper-38 row use a finite complex
   parameter $s$, so their two orientation magnitudes are nonzero.
6. “Historically source-locked before evaluation” has its literal meaning:
   the candidate definition and stop rule were frozen before that candidate's
   numerical result was inspected. It does not mean “currently unevaluated.”
7. The observed registry snapshot is the Session-4 source lock and registry
   identified by the hashes in the Paper-39 source lock.
8. The six `Good` coordinates are the typed consolidation of pre-existing
   Route/source fields mapped explicitly in the Paper-39 source lock. The
   governing Route-A criterion file has SHA-256
   `29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a`.
9. This is a retrospective closure encoding assembled after P35--P38 outcomes
   were known and frozen before the Paper-39 checker run. No claim is made
   that its 14-class/16-token encoding was preregistered before all predecessor
   failures.
10. Expanded edge `E22` is an auxiliary Paper-37 historical firewall outside
    the exact $\mathcal A_{14}/\Sigma_{16}$ request domain. It is retained in
    the 28-edge audit artifact but supplies no class, token, or failed-`Good`
    coverage.

## Notation

- $M_r=\langle u,v\mid vu=u^rv\rangle^+$ is the positive affine monoid.
- $G_r=BS(1,r)=\langle u,v\mid vuv^{-1}=u^r\rangle$ is its group completion.
- $X_r^H$ is the cyclically nonbacktracking oriented-edge affine Cayley shift.
- $K_r$ is the fully relation-filled Cayley $2$-complex.
- $T_{r,\theta}=D_\theta H_rD_\theta$ is the Paper-36 damped prequotient
  Hashimoto operator.
- $T_{P,\theta}$ is a finite-fiber matrix-weighted damped Hashimoto operator.
- $T_r$ is the Bass--Serre tree canonical for the frozen ascending-HNN
  splitting/presentation; $B$ is its full-edge Hashimoto operator.
- $\mathcal H_{35:38}$ is the typed obstruction history.
- $\Sigma_{16}$ is the exact frozen instance-token set.
- $\mathcal P_{\rm fr}$ is the finite set of nonempty audit-provenance paths.
- $\mathfrak C_{\mathrm{aff}}$ is the endpoint-typed state family over those
  paths; paths do not compose candidate mechanisms.
- $\operatorname{end}(c)$ is the endpoint node of the provenance path of $c$.
- $\mathcal V_{\rm obs}$ is the set of seventeen tested obstruction
  endpoints.
- `E22` is the unique auxiliary non-domain firewall edge. Its Paper-37
  historical boundary path is not a request-classification path.
- `Good` is the six-conjunct success predicate stated in the claim.
- $R_*=\{c:\operatorname{HistoricallyLockedNonAffine}(c)\}$ is the historical
  registry witness set.

## Proof Strategy

Use a finite typed reduction. First prove that object, marker, and determinant
ownership cannot be borrowed across an unproved type-changing edge. Then apply
the four predecessor theorems in sequence: the Paper-35 recurrence/object
fork, the Paper-36 filling/clock fork, the Paper-37 coefficient
leakage-or-erasure fork, and the Paper-38 tree/orbital terminal fork. Finally,
verify the fourteen class dispositions, sixteen frozen instance tokens, and
seventeen endpoint families. Audit paths record provenance only; a reset edge
does not compose candidate mechanisms. The registry decision is then a
separate finite-witness argument.

## Dependency Map

1. The main relative-closure claim depends on Lemmas 1--6 below.
2. Lemma 1 depends only on the typed ownership definition.
3. Lemma 2 depends on Paper 35: strict height, backtrack creation, surviving
   affine relation polygon, quotient extra cycles, and the Bost--Connes
   trace/determinant identity.
4. Lemma 3 depends on Paper 36: contractibility, marker non-descent,
   prequotient trace-class ownership, positive relation coefficient, and
   generic scalar-superlift cancellation.
5. Lemma 4 depends on Paper 37: trace-class finite-fiber ownership, ordinary
   deletion/nilpotence equivalence, the explicit mixed leakage formula, and
   normal-closure saturation.
6. Lemma 5 depends on Paper 38: tree periodic emptiness, noncompactness,
   modular-weight persistence, action-hypothesis split, necklace collapse,
   balanced divergence, and marker collision.
7. Lemma 6 depends on exact enumeration of the fourteen class rows, sixteen
   instance tokens, seventeen internal heads, and the endpoint typing of
   nonempty audit-provenance paths.
8. Lemma 7 depends on the hashed Session-4 preregistration/source lock and
   candidate registry.
9. The Route tuple depends on the fact that the Paper-39 source object is a
   history/meta-object rather than an arithmetic dynamical source.

## Proof

### Step 1. Type safety and ownership firewall

**Lemma 1.** Suppose an edge changes any of the state space, recurrence
notion, marker, operator, or determinant category. Then the source-node
ownership statement is not a target-node ownership statement unless that edge
contains an explicit descent or transport proof.

**Justification.** An ownership statement has the form

$$
(\mathcal X,m,\mathcal H,T,\mathfrak d),
$$

where $\mathcal X$ is a state space, $m$ a marker, $\mathcal H$ an operator
space, $T$ an operator, and $\mathfrak d$ a determinant category. Equality of
ownership at the next node requires an identification of all five typed
fields, or maps accompanied by a theorem that preserves the invariant. The
contract defines an object-changing edge to reset any field for which no such
proof is present. Therefore no coordinate can be inherited solely because it
is favorable. Applying a quotient/projection to the audit graph does not
manufacture the missing identification: the projected edge must preserve the
expanded non-inheritance constraint it represents. In particular, `E36_37`
represents expanded `E07`, so its object, redeclared marker, operator owner,
and determinant owner are all resets under the P37 source lock; only
obligations and historical provenance carry. This is a typing consequence,
not an analytic no-go. $\square$

### Step 2. Paper-35 object fork is terminal within its rows

**Lemma 2.** None of the positive, symmetrized, Hashimoto, finite-quotient, or
Bost--Connes/Fock rows satisfies `Good`.

**Justification.** On the positive affine source, the height strictly
increases along every positive generator edge, so the primitive ledger is
empty and recurrence fails. Formal reverse edges change the object and create
the primitive backtrack $e\bar e$ for every retained edge, which fails
selectivity and generic controls. Hashimoto reduction deletes those immediate
reversals but retains

$$
C_{r,x}=vu\bar v\bar u^r,
$$

a primitive length-$(r+3)$ relation polygon reproduced by exponent mutations
and generic presentations. Its natural whole operator is noncompact and has
no ordinary Fredholm determinant at this node.

Finite congruence quotients add $U_q^q$ cycles and possible small-modulus
degeneracies; by Lemma 1, their finite determinant is not the infinite-source
determinant. On the diagonal Gibbs object,

$$
\operatorname{Tr}D_\beta=\zeta(\beta),\qquad
-\log\det(I-zD_\beta)
=\sum_{m\ge1}\frac{z^m}{m}\zeta(m\beta).
$$

Thus the partition trace is one coefficient of a determinant owned on a
different space and marker. At least one conjunct of `Good` fails in every
row. $\square$

### Step 3. Complete relation filling cannot retain all obligations

**Lemma 3.** Complete source-relation filling and its scalar graded repair do
not satisfy `Good`.

**Justification.** The frozen contractibility theorem gives

$$
\pi_1(K_r)=0,\qquad H_j(K_r;\mathbb Z)=0\quad(j\ge1).
$$

Hence complete filling removes every recurrent class rather than only an
unwanted affine class. For an additive grading into a torsion-free abelian
group, relation invariance gives

$$
(r-1)\deg u=0.
$$

For $r\ge2$, $\deg u=0$, contradicting the unit edge marker. Meanwhile, the
separately owned prequotient operator is trace class and has

$$
\operatorname{Tr}(T_{r,\theta}^{r+3})
\ge(r+3)\theta^{2S_r}>0.
$$

Thus its determinant cannot be the empty filled ledger. In the balanced
control $r=1$, the marker descends, but the filled square-grid complex remains
contractible; marker descent is not sufficient.

The diagonal scalar chain lift has

$$
\operatorname{Str}(\widetilde A^n)
=(1-2+1)\tau(A^n)=0
$$

for every $n\ge1$ and every two-generator one-relator presentation. It
retains no selective sector and is `PROVES_TOO_MUCH`. $\square$

### Step 4. Finite coefficients have a complete leakage-or-erasure fork

**Lemma 4.** Under the finite-rank inverse-edge coefficient row and its frozen
all-orders mixed-relation obligation, no ordinary or graded branch satisfies
`Good`.

**Justification.** For a finite matrix $W$,

$$
\det(I-tW)=1
\iff \operatorname{Tr}(W^m)=0\ \text{for all }m\ge1
\iff W\text{ is nilpotent}.
$$

The first equivalence follows from the formal logarithm and Newton identities;
the second follows from Cayley--Hamilton. A product of invertible edge
transports is invertible and cannot be nilpotent. Hence the ordinary branch
cannot delete a complete primitive factor.

For the frozen graded shear pair, the direct relator factors and all their
powers agree, but the primitive mixed word

$$
M_r=\bar u^rv\bar u^{r-1}vu\bar v^2
$$

has supertrace

$$
-4r^4(r-1)\ne0
$$

for every $r\ge2$. Thus direct cancellation leaks. If the obligation is
strengthened to every finite mixed product in the relator's normal closure,
every closed Cayley label is included, so every primitive graded term
vanishes and $Z_{\rm gr}=1$. Thus complete saturation erases the whole ledger.
The three finite-coefficient rows respectively fail cancellation, complete
mixed cancellation, or retained recurrence/selectivity. $\square$

**Absolute-grouping check.** Fix a basis in the finite fiber and let $C_P$ be
the maximum entrywise absolute row/column sum of the finitely many generator
and inverse transport matrices. Finite fiber dimension, finite edge degree,
and $D_\theta\in\mathcal S_1$ then give a scalar nonnegative dominating kernel

$$
K=C_P(D_\theta H_{\rm abs}D_\theta)\in\mathcal S_1.
$$

For sufficiently small $|z|$,

$$
\sum_{n\ge1}\frac{|z|^n}{n}
\lVert K\rVert_1\lVert K\rVert^{n-1}<\infty.
$$

This supplies the absolute cycle domination needed to regroup the trace-log
by primitive roots; no conditional rearrangement is used.

### Step 5. The frozen-splitting tree row and every frozen substitute fail

**Lemma 5.** The full-tree, canonical modular, tree-lattice, orbital, and
marker rows of Paper 38 do not satisfy `Good`.

**Justification.** A positive-period point of the full oriented-edge tree
shift would be a positive reduced closed path in a tree, which does not exist.
Thus recurrence fails. For an infinite orthonormal family of suitably chosen
edges,

$$
\langle B\delta_{e_i},B\delta_{e_j}\rangle=0\quad(i\ne j),
\qquad \|B\delta_{e_i}\|^2=r.
$$

Therefore $B$ is noncompact and not trace class, so it owns no ordinary
Fredholm determinant. For finite complex $s$, the canonical modular step
weights have nonzero magnitudes $r^{-\operatorname{Re}s}$ and
$r^{\operatorname{Re}s}$; a fixed-orientation subfamily gives the same
noncompactness proof.

For $r\ge2$, the $G_r$ action is faithful and its image has infinite vertex
stabilizer, hence is nondiscrete in the compact-open topology. At $r=1$, the
image is the discrete translation group, but the original $\mathbb Z^2$
action has infinite kernel and stabilizers, is nonproper, and fails the
finite-stabilizer hypotheses. Quotienting to the image changes the acting
group and ledger. Hence the tree-lattice determinant row does not provide the
required same-object ordinary Fredholm determinant.

The positive-height conjugacy substitute is a changed object. For $r\ge2$,
its primitive counts give

$$
Z_{+,r}(z)=\frac{1-z}{1-rz},
$$

the generic $r$-ary necklace law reproduced by matched ascending-HNN controls.
At $r=1$, the coefficient at every positive height is infinite. Finally,
$\ell_T(a,k)=|k|$, so $u^m$ has tree length zero and $u^mv$ has tree length
one regardless of their old generator lengths. The old marker cannot be
transported. Each row fails at least one conjunct of `Good`. $\square$

### Step 6. Edge coverage is exhaustive relative to the retrospective Paper-39 encoding

**Lemma 6 (endpoint-obstruction totality).** Every state in
$\mathfrak C_{\mathrm{aff}}$ has one of the obstruction nodes in Lemmas 2--5
as the endpoint of its nonempty audit-provenance path. More precisely:

1. every one of the fourteen class labels has a nonempty frozen disposition;
2. every one of the sixteen stable instance tokens has an explicit
   `OBSTRUCTED` or `EXIT` classification;
3. for every $r\ge2$ and $c\in\mathfrak C_{\mathrm{aff}}(r)$,
   $\operatorname{end}(c)\in\mathcal V_{\rm obs}$ and
   $F(\operatorname{end}(c))\ne\varnothing$;
4. at least one `Good` conjunct fails at $\operatorname{end}(c)$.

**Justification.** The class table in Section 5.1 of the derivation package
contains exactly six `OBSTRUCTED` classes, six `EXIT_ONLY` classes, and two
mixed classes. The token table contains exactly six theorem-covered frozen
family tokens, six explicit exit tokens, and two tested/exit pairs for the
mixed classes, for a total of sixteen. There is no `OTHER_INSTANCE` token.
Root damping and a finite-total-weight retrofit are exit tokens; the proof
does not apply undamped noncompactness to those changed operators. The full
Bass--Serre tree canonical for the frozen ascending-HNN
splitting/presentation and the frozen tree-lattice/groupoid import are the two
tested mixed-class tokens; only their explicitly listed alternatives exit.

The remaining expanded edge `E22` does not add a seventeenth token or convert
the finite-rank, character, or grading classes to mixed status. Its exact tag
is the Paper-37 **future-search prohibition** against trying an unenumerated
post-result coefficient construction. That tag is neither an exact element of
$\mathcal A_{14}$ nor a member of $\Sigma_{16}$. The bridge therefore records
`E22` under `non_domain_firewall_edges`, with empty request-token and
class-coverage fibers, and excludes it from $\Gamma$, $\chi$, and the endpoint
obstruction theorem. Its target `NX` records nonmembership only; it is not
evidence for $\neg\operatorname{Good}$.

The expanded DAG uses exactly the seventeen internal transition tags on
`E00a`, `E00b`, `E01`--`E03`, `E04a`, `E04b`, and `E05`--`E14`. Each has one
recorded head under $\kappa_{\rm int}$, and
$\mathcal V_{\rm obs}=\operatorname{im}(\kappa_{\rm int})$. If
$c=(p,x)\in\mathfrak C_{\mathrm{aff}}(r)$, then $p$ is nonempty, so its
endpoint is the head of an internal edge and belongs to
$\mathcal V_{\rm obs}$. The finite failure map assigns a nonempty coordinate
set to every such endpoint. This proves endpoint-obstruction totality; it
does not assert a dynamic process or a graph-termination theorem.

The endpoint datum $x$ is typed only by $\operatorname{end}(p)$. The failure
map in the quantifier audit assigns a nonempty subset of
$\{I,R,S,D,M,C\}$ to each of the seventeen endpoints. Lemma 2 verifies its
seven Paper-35 rows, Lemma 3 its two Paper-36 rows, Lemma 4 its three Paper-37
rows, and Lemma 5 its five Paper-38 rows. Hence

$$
\bigvee_{j\in F(\operatorname{end}(c))}\neg G_j(c),
$$

which implies $\neg\operatorname{Good}(c)$ because `Good` is the conjunction
of all six $G_j$.

Audit paths are not compound repairs. A reset edge discards the predecessor's
object, marker, and ownership fields and records historical succession. In
particular, `E07` points from the Paper-36 audit to the independently
source-locked unquotiented Paper-37 object; it is not an
unfill-plus-local-system operation. Its coarse projection `E36_37` preserves
all four candidate-identity resets; the reused marker notation is a
redeclaration, not `CARRY_WITH_EQUIVALENCE`. With

$$
\begin{aligned}
&\rho(N00)=0,\quad\rho(N35F)=\rho(N35P)=1,\quad
\rho(N35S)=2,\quad\rho(N35H)=3,\\
&\rho(N35Q)=\rho(N35D)=\rho(N35B)=\rho(N36F)=4,\\
&\rho(N36G)=\rho(N37O)=5,\quad\rho(N37D)=6,\quad
\rho(N37N)=7,\quad\rho(N38T)=8,\\
&\rho(N38M)=\rho(N38L)=\rho(N38O)=\rho(N38K)=9,\\
&\rho(NX)=\rho(NC)=10,\quad\rho(NR)=\rho(NS)=11,
\end{aligned}
$$

every edge strictly increases rank. Hence no hidden cycle or indefinite audit
loop exists. Exact
enumeration proves finite class/token coverage and endpoint obstruction of
$\mathfrak C_{\mathrm{aff}}$. It proves nothing about unlisted instances or
arbitrary compound mechanisms. $\square$

Combining Lemmas 2--6, every admissible $c$ falsifies at least one conjunct of
`Good`. This proves

$$
\forall r\ge2\;\forall c\in\mathfrak C_{\mathrm{aff}}(r),
\quad\neg\operatorname{Good}(c).
$$

Notice the quantifier over $c$ is restricted to the explicitly defined
contract. No statement about $c\notin\mathfrak C_{\mathrm{aff}}$ follows.

### Step 7. Registry handoff

**Lemma 7.** In the frozen snapshot, $R_*\ne\varnothing$.

**Justification.** The hashed Session-4 document is explicitly titled
“Preregistration and Source Lock” and states that candidate definitions were
frozen before numerical results were inspected. It defines the objects and
stop rules for `SD-C01`--`SD-C04`. Its addendum states that `SD-C05` and
`SD-C06` were added before an experiment on either object was run. The hashed
registry contains all six IDs. Each is a finite/countable symbolic object
outside the Paper-35--38 affine semigroup/HNN repair contract. Hence

$$
\{\mathrm{SD\!\!-C01},\ldots,\mathrm{SD\!\!-C06}\}\subseteq R_*,
$$

and $R_*$ is nonempty. $\square$

The realized guard therefore returns control to the pre-existing registry.
It does not choose a candidate. If $R_*$ had been empty, the frozen decision
tree would instead return `STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR`.

### Step 8. Strict Route tuple

Route coordinates are evaluated on `SD-C41` itself, not inherited from its
inputs. Its source object is an obstruction history, not an arithmetic
dynamical source, so A0 fails. It has no primitive orbit ledger, so A1 fails;
no candidate operator or determinant, so A2 fails; no completion or global
analytic structure, so A3 fails; and no lift or zero correspondence, so A4
fails. Therefore

```text
(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL),
overall = ROUTE_A_REJECTED,
route_b_invocation_allowed = false.
```

This completes the theorem and decision proof. $\square$

## Corrections or Missing Assumptions

- The original informal phrase “close the affine branch” is corrected to
  “close the explicitly frozen affine repair contract.” Removing the domain
  qualifier would be unjustified.
- “Already independently source-locked before evaluation” is interpreted as
  historical existence because the Paper-38 handoff explicitly returns to an
  already existing registry. It is not strengthened to “currently
  unevaluated.”
- Existing `SD-C01`--`SD-C06` records witness registry nonemptiness only. They
  do not constitute Paper-40 authorization, a ranking, or a claim that one
  remains scientifically live.

## Open Risks

1. **Undefined unspent-successor predicate.** The frozen handoff does not
   define whether a “successor” must be unevaluated. Under such a stronger,
   newly imposed predicate, the six historical candidates would not be live
   witnesses and the fallback STOP could apply. Paper 39 must not silently
   change predicates; future governance must source-lock the stronger one.
2. **Predecessor-theorem dependence.** Paper 39 treats the sealed predecessor
   proofs as authority inputs. In particular, Paper 36's use of the
   incompressible one-relator-monoid contractibility theorem is not
   re-litigated here. A defect in that predecessor theorem would weaken the
   corresponding closure edge.
3. **Literal-token boundary.** Exhaustiveness is exact only for the sixteen
   listed tokens. A genuinely new construction that is not one of those
   tokens is outside the theorem; it is neither normalized into a catch-all
   exit nor refuted. `E22` is retained solely as the explicitly typed
   Paper-37 historical firewall for such post-result searching and is not a
   hidden alternative-instance token.
4. **Snapshot dependence.** Registry nonemptiness is established for the
   hashed snapshot. A future registry mutation requires a new audit.
5. **No universal conclusion.** Finite directed cycles, noninvertible
   nilpotent coefficients, root-damped tree operators, and proper
   finite-stabilizer tree actions provide sharp out-of-contract boundaries.
6. **Retrospective-contract limitation.** The Route/source fields and P38
   closure obligation pre-exist the Paper-39 checker, but the consolidated
   14-class/16-token encoding was assembled with predecessor outcomes known.
   It is auditable closure of a frozen historical branch, not prospective
   preregistration of all repairs before those outcomes.
