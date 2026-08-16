# Paper 39 quantifier and hidden-gap audit — SD-C41

## 1. Exact Paper-39 quantifiers

Write

$$
\operatorname{Good}=G_I\wedge G_R\wedge G_S\wedge G_D\wedge G_M\wedge G_C
$$

for the six frozen conjuncts. For an admissible audit state $c$, let
$\operatorname{end}(c)$ be the endpoint of its nonempty typed provenance path,
and define the tested obstruction-endpoint set

$$
\begin{aligned}
\mathcal V_{\rm obs}=\{&N35F,N35P,N35S,N35H,N35Q,N35D,N35B,\\
&N36F,N36G,N37O,N37D,N37N,N38T,N38M,N38L,N38O,N38K\}.
\end{aligned}
$$

An outgoing edge can record a later historical successor audit and may reset
the object; it is not continuation of the same candidate. Accordingly, the
argument below is endpoint-obstruction totality, not a graph-termination
claim.

The exact failure-coordinate map is:

| Obstruction endpoint(s) | Nonempty set $F(v)$ of failed `Good` coordinates |
|---|---|
| `N35F,N35P` | $\{R,D\}$ |
| `N35S,N35H` | $\{S,D,C\}$ |
| `N35Q` | $\{S,D,M\}$ |
| `N35D` | $\{R,S,M\}$ |
| `N35B` | $\{I,S,M\}$ |
| `N36F` | $\{R,S,D,M,C\}$ |
| `N36G` | $\{R,S,C\}$ |
| `N37O,N37D` | $\{S,C\}$ |
| `N37N` | $\{R,S,C\}$ |
| `N38T,N38M` | $\{R,D\}$ |
| `N38L` | $\{D,C\}$ |
| `N38O` | $\{S,D,M,C\}$ |
| `N38K` | $\{M\}$ |

The proof isolates endpoint totality from the coordinatewise obstruction.

**Endpoint-obstruction totality.** For every $r\ge2$ and every
$c\in\mathfrak C_{\rm aff}(r)$,

$$
\operatorname{end}(c)\in\mathcal V_{\rm obs},
\qquad F(\operatorname{end}(c))\ne\varnothing.
$$

This follows from the complete seventeen-head enumeration and the nonempty
failure-coordinate table.

**Endpoint obstruction.** For every such $c$,

$$
\bigvee_{j\in F(\operatorname{end}(c))}\neg G_j(c).
$$

The node ledger and the predecessor lemmas prove every entry of this finite
map. Because $F(v)$ is nonempty, endpoint obstruction implies

$$
\forall r\in\mathbb Z_{\ge2}\;
\forall c\in\mathfrak C_{\mathrm{aff}}(r)\;
\neg\operatorname{Good}(c).
$$

Only this last formula is logically equivalent to

$$
\neg\exists r\in\mathbb Z_{\ge2}\;
\exists c\in\mathfrak C_{\mathrm{aff}}(r):
\operatorname{Good}(c).
$$

It is not

$$
\neg\exists c\in\{
\text{all affine or symbolic constructions}\}:\operatorname{Good}(c).
$$

The failed coordinate depends on $\operatorname{end}(c)$; the theorem does not
assert one common analytic obstruction for every row. The balanced value
$r=1$ is outside the main affine theorem quantifier and is included only
through the explicitly frozen boundary controls.

## 2. Contract quantifier

The top-level repair alphabet has exactly fourteen classes
$\mathcal A_{14}$, while the expanded proof graph has seventeen internal
transition tags. The frozen instance-token set has exactly sixteen tokens:
one frozen family token for each of the six obstructed classes, one literal
exit token for each of the six exit-only classes, and two tokens—one tested
frozen instance and one explicit alternative-exit token—for each of the two
mixed classes. There is no `OTHER_INSTANCE` token and no quantifier over
arbitrary conceivable instances.

Let $\mathcal P_{\rm fr}$ be the finite set of nonempty typed **audit
provenance paths** from `N00` through the seventeen internal edges. If
$p\in\mathcal P_{\rm fr}$ ends at $v$, let $X_v(r)$ be the source-frozen
candidate family typed at $v$. Define

$$
\mathfrak C_{\rm aff}(r)
=\coprod_{p\in\mathcal P_{\rm fr}}\{p\}\times X_{\operatorname{end}(p)}(r).
$$

The path records only provenance and inherited obligation. The candidate data
$x$ belong solely to the endpoint type. In particular, `E07` is a historical
reset from the filled-object audit to the separately source-locked
unquotiented coefficient object; it is not a cumulative operation that
unfills a complex and adds a local system.

The fourteen-row disposition relation is total on the fourteen class labels,
and the sixteen-token classifier is total on the explicitly frozen tokens.
An exit token maps to `NX`, which is a domain statement and not evidence for
$\neg\operatorname{Good}$. Root damping and finite-total-weight retrofit may
change compactness, and arbitrary groupoid or valuation-tree constructions
are not quantified over. The Bass--Serre tree canonical **for the frozen
ascending-HNN splitting/presentation** and the frozen tree-lattice/category
import are tested; their two explicitly listed alternative tokens exit.

Expanded edge `E22` is not part of any of these quantifiers. Its exact label
is an auxiliary Paper-37 future-search firewall, not one of the fourteen
literal repair-tag IDs and not one of the sixteen instance tokens. Although
its source prose uses the English nouns “character,” “rank,” and
“representation,” those words do not introduce alternative instances into
$\Sigma_{16}$. Let $\mathcal E_{\rm tok}(\sigma)$ be the union of the
obstruction, boundary-comparison, and exit edge fields of token $\sigma$, and
let $\mathcal E_\Gamma(a)$ be the analogous edge union in the class-coverage
row for $a$. Formally,

$$
E22\notin\mathcal T_{17},\qquad
E22\notin\bigcup_{\sigma\in\Sigma_{16}}\mathcal E_{\rm tok}(\sigma),
\qquad
E22\notin\bigcup_{a\in\mathcal A_{14}}\mathcal E_\Gamma(a).
$$

Its path is retained separately as historical boundary evidence, and its
`NX` target asserts only nonmembership. It contributes neither a failed
`Good` coordinate nor an exhaustiveness witness.

No theorem is asserted for compound repairs or for arbitrary combinations of
node coordinates. Such a construction requires a new source lock and a new
typing/ownership proof.

## 3. Predecessor quantifier ledger

| Source | Theorem-level quantifier actually used | Finite-control quantifier that must not replace it | Boundary |
|---|---|---|---|
| P35 positive source | Every edge of $\mathbb N_0\rtimes\mathbb N^\times$ has strict height increase; every $r\ge2$ slice has the analogous acyclicity; for every $\beta>1$ the weighted full comparison is bounded and noncompact | Frozen word, origin, quotient, diagonal, and Fock cutoffs only corroborate formulas | Symmetrization and Hashimoto are changed objects |
| P35 relation word | For every $r\ge2$ and base vertex $x$, $vu\bar v\bar u^r$ is a primitive cyclically nonbacktracking closed word | Explicit witnesses for finitely many $r,x$ | Genericity is shown by matched presentation controls, not by prime/composite statistics |
| P36 filling | For every $r\ge2$, the frozen $K_r$ is contractible; for every torsion-free abelian grading target, cell invariance forces $\deg u=0$ | Six finite semidirect quotients do not prove infinite contractibility | At $r=1$, the marker descends but the fill remains contractible |
| P36 operator | For every $r\ge2$ and $0<\theta<1$, $T_{r,\theta}$ is trace class; the trace-log identity is local in $z$, e.g. $\lvert z\rvert<\lVert T\rVert^{-1}$ | The exact $\theta=1/2$ rows are controls | Fredholm ownership is prequotient only |
| P36 scalar lift | For every positive integer $n$ and every two-generator one-relator presentation in the stated scalar-lift class, the supertrace multiplier is $1-2+1=0$ | Powers through twelve are regression checks | This is an explicit graded finite-trace control, not an ordinary graph determinant |
| P37 ordinary coefficients | Every finite rank and every invertible inverse-edge connection in the stated class: complete ordinary factor deletion implies nilpotence and is impossible | Rank-two fixtures do not establish the arbitrary-rank statement | A noninvertible nilpotent matrix is outside parallel transport and is a sharp counterexample to an unrestricted claim |
| P37 shear leak | For every integer $r\ge2$, the one explicit mixed word has supertrace $-4r^4(r-1)\ne0$ | Rows $r=1,\ldots,8$ verify implementation | The $r=1$ formula is not used as a theorem-row obstruction |
| P37 saturation | Every closed Cayley path label lies in the relator normal closure; if cancellation is imposed on every finite mixed product, every primitive factor is cancelled | Bounded conjugator searches only find examples of leakage | “Complete saturation” is an obligation covering all closed labels; it is not a theorem that direct local matching automatically propagates |
| P38 full tree | For every $r\ge1$, no positive reduced closed tree path exists and the full-edge Hashimoto operator is noncompact | Finite-tree and orthogonal-column truncations are controls | Formal zero diagonal entries do not define a trace on a non-trace-class operator |
| P38 modular weight | For every finite $s\in\mathbb C$, the two permitted orientation magnitudes are nonzero, so a constant-norm orthogonal subfamily persists | Sampled $s$ values are unnecessary | A zero weight or root-dependent summable weight is outside the canonical cocycle contract |
| P38 action | For every $r\ge2$, the action image is faithful and nondiscrete; at $r=1$, the image is discrete but the original action is nonproper with infinite kernel/stabilizers | Finite GBS rows are controls | The $r=1$ split is mandatory; “nondiscrete for all $r$” is false |
| P38 orbital ledger | For every $r\ge2$ and every positive height $k$, Burnside/Moebius formulas hold and the product is $(1-z)/(1-rz)$; at $r=1$, each height has infinitely many classes | Counts through height twelve are checks | Orbital classes are not literal tree periodic points |
| P38 marker | For every $(a,k)\in\mathbb Z[1/r]\rtimes\mathbb Z$, $\ell_T(a,k)=\lvert k\rvert$ | Five marker rows are witnesses | New tree length is not the old Cayley generator length |

## 4. Determinant quantifiers

Each determinant statement must include its owner and analytic domain.

1. For trace-class $T$,

   $$
   -\log\det(I-zT)=\sum_{n\ge1}\frac{z^n}{n}\operatorname{Tr}(T^n)
   $$

   is used near $z=0$, not as an automatic global continuation.
2. P35 diagonal $D_\beta$ owns its determinant for $\beta>1$ on
   $\ell^2(\mathbb N^\times)$; the affine graph does not inherit it.
3. P36 $T_{r,\theta}$ owns a prequotient ordinary Fredholm determinant; the
   filled complex does not inherit it.
4. P37 each parity operator owns an ordinary determinant. The virtual ratio
   is explicitly graded and is not relabelled as a positive determinant.
5. P38 full-tree $B$ and its permitted modular weighting are not trace class,
   so formal vanishing diagonal coefficients do not create an ordinary
   Fredholm determinant.
6. Tree-lattice, groupoid, von Neumann, orbital, and regularized determinant
   categories are typed separately.

## 5. Registry decision quantifiers

The frozen decision is the guarded statement

$$
R_*\ne\varnothing
\Longrightarrow
\texttt{RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY},
$$

$$
R_*=\varnothing
\Longrightarrow
\texttt{STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR},
$$

where

$$
R_*=\{c:\operatorname{HistoricallyLockedNonAffine}(c)\}.
$$

In the hashed snapshot,

$$
\{\mathrm{SD\!\!-C01},\ldots,\mathrm{SD\!\!-C06}\}\subseteq R_*,
$$

so the realized branch is the first implication. This is an existence proof,
not a ranking. It neither asserts

$$
\exists c\in R_*:\operatorname{Good}(c)
$$

nor

$$
\exists c\in R_*:\text{$c$ is currently unevaluated}.
$$

All six candidates already have Route-A records.

### Exact historical witness ledger

| ID | Separately frozen non-affine object | Route-card SHA-256 | Recorded status | Handoff use |
|---|---|---|---|---|
| `SD-C01` | Finite-state function-field arithmetic skeleton | `ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2` | `ROUTE_A_REJECTED` | Existence witness only |
| `SD-C02` | Squarefree admissible shift | `5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f` | `ROUTE_A_REJECTED` | Existence witness only |
| `SD-C03` | Weighted renewal shift | `2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328` | `ROUTE_A_REJECTED` | Existence witness only |
| `SD-C04` | Gauss/Mayer countable transfer candidate | `0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92` | `ROUTE_A_EXPLORATORY` | Existence witness only |
| `SD-C05` | Recursive wheel-sieve level shift | `4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1` | `ROUTE_A_EXPLORATORY` | Existence witness only |
| `SD-C06` | Knauf number-theoretical spin-chain recursion | `d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b` | `ROUTE_A_EXPLORATORY` | Existence witness only |

The six definitions occupy separate candidate sections with separate stop
rules in the preregistration/source lock. The addendum explicitly says that
`SD-C05` and `SD-C06` were added before an experiment on either was run and
that they are evaluated separately. This is sufficient for the frozen
historical-existence guard. None is promoted by Paper 39.

## 6. Hidden-gap audit

### H1. Universalization gap — closed by weakening

Papers 35--38 do not classify all affine mechanisms. Paper 38 literally
freezes a prohibition list and forbids reopening that branch. The Paper-39
theorem is therefore relative to the retrospective encoding built from those
hashed artifacts and frozen before its checker. Finite cycles, nilpotent
coefficients,
root-damped tree operators, and proper tree-lattice actions are explicit
out-of-contract countermodels to overbroad statements.

**Disposition:** no gap in the weakened theorem; fatal gap in a universal
version.

### H2. Compound-repair gap — closed by removing the claim

Coverage of isolated repair labels would not cover arbitrary combinations.
Paper 39 therefore makes no universal statement about compound repairs.
Typed paths encode audit provenance only; they are not compositions of the
endpoint mechanisms. Coordinatewise assemblies are outside the theorem and
are not refuted constructions.

**Disposition:** closed by narrowing the claim, not by a mathematical no-go.

### H2a. Fourteen classes versus seventeen transitions — closed by two maps

Treating the seventeen internal edge tags as the Paper-38 alphabet would
change the frozen data, while forcing one target per top-level class would
erase mixed cases. The derivation therefore uses a set-valued class relation
$\Gamma:\mathcal A_{14}\to\mathcal P(\mathcal V\cup\{NX\})$ and a separate
single-valued internal head map
$\kappa_{\rm int}:\mathcal T_{17}\to\mathcal V$.

**Disposition:** closed by exact fourteen-row enumeration and explicit
sixteen-token enumeration: six obstructed-family tokens, six exit-only
tokens, and two tested/exit pairs. No catch-all `OTHER_INSTANCE` exists.

### H2b. Endpoint-location/no-success conflation — corrected

A graph-location conjunct is not logically equivalent to nonexistence of a
`Good` state without an independent totality theorem. Paper 39 now makes no
substantive termination claim. It defines $\operatorname{end}(c)$, enumerates
all seventeen obstruction endpoints, proves
$F(\operatorname{end}(c))\ne\varnothing$, and derives the failed conjunction
directly.

**Disposition:** closed by endpoint-obstruction totality and the explicit
failure-coordinate map.

### H2c. Unscoped `E22` firewall — closed by domain separation

The Paper-37 successor boundary forbids a post-result search over another
matrix, character, rank, representation, automaton, or completion. Treating
that prose as an admitted alternative instance would contradict the frozen
six/six/two class census and sixteen-token universe. `E22` is therefore typed
as auxiliary non-domain firewall evidence: it remains in the 28-edge audit
artifact, has an explicit historical path and authority hashes, but has empty
request-token and class-coverage fibers.

**Disposition:** excluded from $\mathcal A_{14}$, $\Sigma_{16}$, $\Gamma$,
$\chi$, and endpoint-obstruction totality; retained only for historical
boundary auditability.

### H3. Ownership-transfer gap — closed by typed reset

Earlier papers contain attractive coordinates on different spaces: positive
source arithmetic, prequotient determinants, graded ratios, and orbital
products. Without a descent theorem they cannot be assembled. Every
object-changing edge now states whether marker and ownership carry or reset.
In particular, the `E07` reset is historical succession, not a cumulative
operation on the filled complex.

The same statement is required after projection: `E36_37` may carry the
obligation/provenance record, but object, marker, operator owner, and
determinant owner all reset under the Paper-37 source-lock authority. An
analogous unquotiented comparison at Paper 36 does not establish a transport
theorem from the filled/control node, and the P37 marker is redeclared rather
than inherited.

**Disposition:** closed for the relative theorem.

### H4. Registry word “successor” — genuinely ambiguous

Paper 38 says both “return control to the already existing global registry”
and “already independently source-locked before evaluation.” Those words
support the historical-existence predicate. They do not define an
“unspent/currently unevaluated successor” predicate. Under the latter new
meaning, the observed live witness set could be empty because `SD-C01`--`SD-C06`
are already evaluated.

**Disposition:** use the literal historical predicate for Paper 39; record the
unspent predicate as undefined. Root alone may source-lock Paper 40
prospectively.

### H5. Contractibility dependency — inherited, not independently re-proved

The Paper-36 closure edge uses its cited incompressible one-relator-monoid
contractibility theorem and the claim that its hypotheses hold. Paper 39
checks the logical downstream use but does not independently audit the
external theorem.

**Disposition:** explicit predecessor dependency; a future defect would weaken
`E05` and the corresponding coverage proof.

### H6. Primitive-factor regrouping — closed by domination

A trace-class operator alone does not justify every basiswise absolute cycle
rearrangement. Here finite edge degree, finite fiber, a finite entrywise
transport bound $C_P$, and $D_\theta\in\mathcal S_1$ give the nonnegative
scalar trace-class dominating kernel
$K=C_P(D_\theta H_{\rm abs}D_\theta)$. For small $|z|$,

$$
\sum_{n\ge1}\frac{|z|^n}{n}
\|K\|_1\|K\|^{n-1}<\infty.
$$

**Disposition:** closed in the local trace-log domain; no global continuation
is inferred.

### H7. Finite evidence versus infinite theorem — closed by ownership labels

The finite exact audits verify implementations and controls. Strict height,
contractibility, nilpotence, normal-closure saturation, tree emptiness,
noncompactness, and all-height necklace formulas are proof-owned.

**Disposition:** closed; no finite cutoff is promoted.

### H8. Balanced $r=1$ boundary — corrected

The image action is discrete at $r=1$, so a uniform “image nondiscrete” claim
would be false. The relevant obstruction is instead nonproperness and infinite
stabilizers of the original action, plus orbital divergence and retained
contractibility.

**Disposition:** closed by the required case split.

### H9. Route-coordinate inheritance — closed

The predecessor affine candidates earned structural A0, but `SD-C41` is a
meta-object with no arithmetic dynamical source. Inheriting their A0 would
violate the same-object rule.

**Disposition:** strict tuple is all FAIL.

### H10. Temporal registry gap — snapshot-relative

The nonempty registry proof concerns the hashed snapshot. Future additions,
removals, or changed status semantics require a new audit.

**Disposition:** explicit temporal limitation.

### H11. Moving-goalposts / retrospective-freeze risk — disclosed and scoped

The Route-A criterion predates the Paper-39 checker
(`route-a-evaluator.md`, SHA-256
`29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a`),
and P38 froze the branch-closure instruction in its source lock and Round-2
clues. However, the consolidated fourteen classes, sixteen tokens, and `Good`
notation were encoded after the P35--P38 outcomes were known.

**Disposition:** Paper 39 is explicitly retrospective and frozen before its
own checker run. It cannot be represented as prospective preregistration made
before all predecessor failures.

## 7. Final audit verdict

No hidden gap remains in the theorem

$$
\forall r\in\mathbb Z_{\ge2}\;\forall c\in\mathfrak C_{\mathrm{aff}}(r),
\ \neg\operatorname{Good}(c)
$$

provided the predecessor theorems are accepted as sealed inputs and the
class/token/endpoint definitions remain frozen. The result cannot honestly be
upgraded to universal affine impossibility. The sole unresolved semantic
ambiguity is the undefined notion of an “unspent successor”; it does not alter
the literal historical-registry handoff but prevents Paper 39 from authorizing
Paper 40.
