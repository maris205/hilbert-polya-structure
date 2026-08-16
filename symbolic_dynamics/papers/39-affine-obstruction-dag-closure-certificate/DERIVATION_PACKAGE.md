# Paper 39 derivation package — SD-C41

Throughout, **expanded proof DAG** means the 22-node/28-edge ledger below.
The prototype's 6-node/5-edge quotient is called only the **structural
spine**. The total many-to-one projection with explicit auditable fibers is
`paper39_DAG_BRIDGE.json`; that bridge retains every expanded record, but the
projection is not invertible.

## 1. Target and invariant

The target is a closure theorem relative to the retrospective Paper-39 affine
encoding assembled from hashed P35--P38 artifacts and frozen before the
Paper-39 checker. The invariant is the typed history $\mathcal H_{35:38}$, not a new
operator. Every displayed step below is labelled as one of:

- **Definition:** part of the Paper-39 contract;
- **Inherited theorem:** proved in a frozen predecessor package;
- **Logical consequence:** follows from the definitions and inherited
  theorems;
- **Boundary control:** prevents an overbroad reading but does not enlarge the
  theorem domain.

For a state $c$, use the conjunctive success predicate

$$
\operatorname{Good}(c)
=I(c)\wedge R(c)\wedge S(c)\wedge D(c)\wedge M(c)\wedge C(c),
$$

where the letters denote intrinsic source, nonempty repetition-compatible
recurrence, arithmetic selectivity, same-object determinant ownership,
marker compatibility, and control survival. This is a **Definition**.

## 2. Obligation vocabulary

The following labels keep the node and edge ledgers compact.

| Label | Exact obligation |
|---|---|
| `O-I` | Source-derived construction with no forbidden arithmetic or target oracle. |
| `O-R` | Nonempty primitive recurrence with compatible powers/repetitions. |
| `O-S` | At least one retained source-proved arithmetic primitive factor and failure on matched generic controls. |
| `O-M` | One free marker per frozen dynamical step, with no specialization or clock substitution. |
| `O-D` | One operator on the declared whole state space owns the declared determinant category. |
| `O-X` | Object, marker, operator, and determinant ownership are not transferred across an edge without proof. |
| `O-A` | All-orders/factorwise cancellation, not only first trace or aggregate cancellation. |
| `O-G` | Balanced, composite, mutation, random, and `PROVES_TOO_MUCH` controls are survived. |

## 3. Typed node ledger

Every row supplies all mandatory fields: inherited obligation, source object,
marker, operator and determinant ownership, exact obstruction, adversarial
control, forbidden escape, and terminal code.

| Node / kind | Inherited obligation | Source object | Marker | Operator / determinant owner | Exact obstruction and decisive control | Forbidden escape | Terminal code |
|---|---|---|---|---|---|---|---|
| `N00` contract root | `O-I,O-R,O-S,O-M,O-D,O-X,O-G` | Frozen Paper-35--38 source corpus and repair alphabet | Typed marker field; no marker is yet selected | No operator and no determinant; this is a data object | No obstruction is asserted at the root; coverage must be proved downstream | Any unnamed repair silently appended after freeze | `CONTINUE_TYPED_AUDIT` |
| `N35F` full positive affine source | `O-I,O-R,O-M,O-D,O-X` | $P=\mathbb N_0\rtimes\mathbb N^\times$ with all dilation generators $d_n$, $n\ge2$ | One original positive generator edge | Unweighted adjacency has infinite outdegree and is not defined on a basis vector; the $\beta>1$ weighted comparison is bounded but noncompact; no ordinary graph Fredholm owner | $h(b,a)=b+a$ strictly increases on every edge, so the positive ledger is empty. Control: all $n\ge2$, not a prime-labelled subset | Reset edge, quotient loop, terminal projector, prime-labelled generator | `STOP_FULL_POSITIVE_AFFINE_RECURRENCE` |
| `N35P` bounded affine slice | `O-I,O-R,O-M,O-D,O-X` | $M_r=\langle u,v\mid vu=u^rv\rangle^+$, with composite baseline $r=4$ and theorem range $r\ge2$ | One original positive $U/V$ generator edge | Finite-degree positive adjacency on $\ell^2(M_r)$ is bounded but noncompact; no ordinary Fredholm owner | $b+k$ (and the Paper-35 height $b+r^k$) strictly increases on every positive edge. Controls: $r=2,3,4,5$ | Reset edge, quotient loop, terminal projector, prime-labelled generator | `STOP_BOUNDED_POSITIVE_AFFINE_RECURRENCE` |
| `N35S` symmetrized edge graph | `O-R,O-M,O-D,O-X,O-G` | Formal reverse-edge enlargement of `N35P` | One oriented edge; explicitly a changed object | Bounded symmetrized adjacency on its own $\ell^2$ space; noncompact; no ordinary Fredholm determinant | Every retained edge creates a primitive two-step backtrack. Control: the same phenomenon occurs for every presentation edge | Calling inverse edges part of the original positive source | `STOP_UNIVERSAL_BACKTRACK_POLLUTION` |
| `N35H` Hashimoto relation ledger | `O-R,O-S,O-M,O-D,O-X,O-G` | Cyclically nonbacktracking oriented-edge shift | One original oriented edge | Natural whole Hashimoto operator is bounded but noncompact; no ordinary Fredholm owner at Paper 35 | $C_{r,x}=vu\bar v\bar u^r$ is primitive of length $r+3$ and survives; matched exponent and arbitrary one-relator controls retain generic relation cycles | Claiming that backtrack deletion deletes presentation relations | `STOP_RELATION_CYCLE_POLLUTION` |
| `N35Q` finite quotient boundary | `O-R,O-S,O-M,O-D,O-X` | Congruence quotient of the affine graph | Quotient edge clock, not automatically the infinite-source clock | Finite matrix owns only its finite quotient determinant | Relation descends but $U_q^q$ and small-modulus degeneracies are added. Control: all frozen $q=1,\ldots,12$ rows | Promoting a finite determinant or quotient ledger to the infinite source | `STOP_QUOTIENT_LEDGER_NON_DESCENT` |
| `N35D` diagonal Gibbs boundary | `O-S,O-M,O-D,O-X` | $\ell^2(\mathbb N^\times)$ with $H\epsilon_n=\log n\,\epsilon_n$ | Free spectral variable $z$, not a Cayley generator-step marker | $D_\beta=e^{-\beta H}$ owns $\det(I-zD_\beta)$ for $\beta>1$ on this diagonal space | $\operatorname{Tr}D_\beta=\zeta(\beta)$ is the first trace, while $-\log\det(I-zD_\beta)=\sum_{m\ge1}z^m\zeta(m\beta)/m$ | Identifying the Gibbs trace/determinant with an affine graph primitive determinant | `STOP_PARTITION_TRACE_IDENTIFICATION` |
| `N35B` prime-Fock/bosonic boundary | `O-I,O-S,O-M,O-D,O-X` | Prime-indexed one-particle/Fock comparison object, not the Cayley graph or diagonal Gibbs space | Occupation fugacity with a $z=1$ specialization, not generator-step length | Any bosonic product is owned only by the prime-Fock construction | Prime labels are preloaded support and occupation number is a different marker. The control exposes input rather than source-derived selectivity | Calling a prime basis emergent or transporting its product to the Cayley operator | `STOP_PRIME_FOCK_MARKER_SUPPORT_SUBSTITUTION` |
| `N36F` complete Cayley-cell fill | `O-R,O-A,O-S,O-M,O-D,O-X,O-G` | Cayley $2$-complex $K_r$ with every translate of $vu=u^rv$ filled; prequotient edge shift kept separately | Unit edge marker would identify $z^2$ with $z^{r+1}$ | Prequotient $T_{r,\theta}=D_\theta H_rD_\theta$ is trace class and owns its Fredholm determinant; the filled homology owns no such determinant | $K_r$ is contractible; all recurrent classes vanish; $(r-1)\deg u=0$ forces $\deg u=0$ in torsion-free grading; yet $\operatorname{Tr}T^{r+3}>0$. Balanced $r=1$ removes length mismatch but still has contractible fill | Setting $z=1$, $\deg u=0$, first return, or calling prequotient determinant the quotient determinant | `STOP_COMPLETE_FILL_ERASES_RECURRENCE` |
| `N36G` scalar graded chain lift | `O-A,O-S,O-D,O-G` | Group-completed $(1,2,1)$ cellular chain orbit data | Same formal $z$ in the explicitly graded control only | Scalar lift owns only its declared finite-trace superdeterminant | $\operatorname{Str}\widetilde A^n=(1-2+1)\tau(A^n)=0$ for all $n$, so the superdeterminant is $1$ for every two-generator one-relator presentation. Control is presentation mutation itself | Crediting total generic erasure as arithmetic selection or as an ordinary positive determinant | `STOP_PROVES_TOO_MUCH_GENERIC_SCALAR_ERASURE` |
| `N37O` ordinary invertible local coefficient | `O-R,O-A,O-S,O-M,O-D,O-X,O-G` | Same unquotiented affine Hashimoto shift with finite-rank inverse-edge transport | Same one-edge free marker | $T_{P,\theta}$ is trace class and owns a matrix Fredholm determinant on the full edge-fiber space | A complete factor is deleted iff $W$ is nilpotent; invertible holonomy is never nilpotent. Control: $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$ has first trace zero but $\det(I-tJ)=1+t^2$ | First-trace-only credit or noninvertible automaton called parallel transport | `STOP_ORDINARY_INVERTIBLE_FACTOR_DELETION` |
| `N37D` direct graded matching | `O-A,O-S,O-M,O-D,O-G` | Rank-two even/odd shear pair on the same edge shift | Same original edge marker | Two parity Fredholm determinants are separately owned; only their explicit ratio is graded | Direct relator, conjugates, and repetitions match, but $M_r=\bar u^rv\bar u^{r-1}vu\bar v^2$ has supertrace $-4r^4(r-1)\ne0$. Random matched controls also direct-match then leak | Aggregate orbit cancellation or omission of mixed normal-closure products | `STOP_MIXED_NORMAL_CLOSURE_LEAKAGE` |
| `N37N` normal-closure saturation | `O-A,O-S,O-M,O-D,O-G` | Same graded edge object, with cancellation required for every finite mixed product in $\langle\!\langle R_r\rangle\!\rangle$ | Same original edge marker | Explicit graded determinant ratio $Z_{\rm gr}$ | Every closed Cayley word lies in the relator normal closure; full saturation gives $\log Z_{\rm gr}=0$ and $Z_{\rm gr}=1$. Control: flat balanced parity cancels every sampled word | Another representation, rank, character, nilpotent automaton, or arbitrary completion on the same ledger | `STOP_LOCAL_COEFFICIENT_SATURATION` |
| `N38T` full Bass--Serre tree of the frozen splitting | `O-R,O-S,O-M,O-D,O-X,O-G` | Full oriented-edge geodesic shift on the Bass--Serre tree canonical for the frozen ascending-HNN splitting/presentation of $BS(1,r)$ | One **new** Bass--Serre tree-edge step; no inherited Cayley-marker credit | Undamped full-tree Hashimoto $B$ on $\ell^2(E^{\rm or}T_r)$; no ordinary Fredholm determinant | A tree has no positive reduced closed path; $B$ maps an infinite orthonormal family to orthogonal vectors of norm $\sqrt r$, hence is noncompact. Controls: finite trees, all frozen $BS(p,q)$ rows | Quotient loop, end, orbital class, or graph-of-groups edge called a full-tree periodic orbit | `STOP_FULL_TREE_EMPTY_NONFREDHOLM` |
| `N38M` canonical modular weight | `O-R,O-S,O-M,O-D,O-X` | `N38T` with only $\Delta(g)=r^{h(g)}$ | Same new tree-edge marker | Modularly weighted full-tree edge operator; no ordinary Fredholm owner | Per-step magnitudes are the two nonzero constants $r^{-\Re s},r^{\Re s}$, so an orthogonal constant-norm subfamily remains; $r=1$ has unit weights | Root/radial damping, finite-total-mass retrofit, or arbitrary cocycle | `STOP_CANONICAL_MODULAR_NONCOMPACTNESS` |
| `N38L` tree-lattice determinant boundary | `O-D,O-X,O-G` | Original $G_r$ action on $T_r$ | Tree/orbital marker in a different determinant framework | Bass/tree-lattice or groupoid category, never the ordinary full-tree Fredholm determinant | For $r\ge2$ the faithful image is nondiscrete; for $r=1$ the image is discrete but the original action has infinite kernel/stabilizers and is nonproper. The $1/\lvert\mathbb Z\rvert:=0$ rule erases every GBS control | Quotienting to the faithful image, reciprocal-infinite-as-zero, determinant-category relabelling | `STOP_TREE_LATTICE_HYPOTHESES` |
| `N38O` positive-height orbital boundary | `O-R,O-S,O-M,O-D,O-X,O-G` | Conjugacy classes in $G_r$, not tree periodic points | HNN height $k$, not old Cayley length and not a literal full-tree closed-path length | Euler product is an orbital formal/product object, not the full-tree Fredholm determinant | For $r\ge2$, $P_r(k)$ is the generic $r$-ary necklace count and $Z_{+,r}(z)=(1-z)/(1-rz)$; for $r=1$, infinitely many classes occur at every height. Prime/composite and matched ascending-HNN controls obey the same law | Presenting the orbital product as the full-tree determinant or discarding the balanced divergence | `STOP_ORBITAL_GENERIC_OR_DIVERGENT` |
| `N38K` marker firewall | `O-M,O-X,O-G` | Comparison of Bass--Serre translation length with Cayley word length | New $\ell_T$ versus old generator count | No determinant transfer is at issue; this is a marker-ownership node | $\ell_T(u^m)=0$, $\ell_T(u^mv)=1$, and the relator has $\ell_T=0$ despite old lengths $m,m+1,r+3$. All marker controls are incompatible | Silent marker inheritance, acceleration, or specialization | `STOP_MARKER_NONTRANSPORT` |
| `NX` nonmembership sink | Applicable obligations are discharged only by leaving the quantified request domain | An explicit $\Sigma_{16}$ exit object, or the separate `E22` historical-firewall boundary | Changed or undefined | Ownership must be reproved in a new source lock; none is inherited | This row asserts no mathematical impossibility; it records nonmembership and carries an empty failed-`Good` set | Treating a token exit or the auxiliary firewall as theorem evidence | `STOP_OUTSIDE_FROZEN_AFFINE_CONTRACT` |
| `NC` affine closure | All obligations | Typed history itself | No dynamical marker | No operator/determinant; closure certificate only | Every tested token is assigned to one of `N35*`, `N36*`, `N37*`, or `N38*`, and every explicit exit token is assigned to `NX` | A new affine object appended after terminal freeze | `CLOSE_ENTIRE_AFFINE_BRANCH` |
| `NR` registry handoff | Registry-existence predicate only | Global Session-4 source lock and registry | Candidate-specific historical markers remain separate | No new owner; historical candidate ownership records remain local to each candidate | `SD-C01`--`SD-C06` are non-affine and were frozen before their own evaluation. This witnesses historical registry nonemptiness but supplies no ranking or live successor | Combining their best coordinates, rerunning one without a new lock, or treating handoff as `GO` | `RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY` |
| `NS` empty-registry fallback | Counterfactual registry predicate | Empty historically locked non-affine registry | None | None | Guard condition $\{c:\operatorname{HistoricallyLockedNonAffine}(c)\}=\varnothing$ | Inventing a candidate inside the closure paper | `STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR` (conditional, not realized) |

## 4. Typed edge ledger

An ownership entry of “reset” means no property is inherited; it does not
mean the target object fails automatically. Edges record historical
successor/audit lineage. They are not presumed to be maps of dynamical
objects, and a reset edge must never be read as a cumulative compound repair.
For each row, the tail ID is an exact foreign key to the tail node's `Source
object` field above; the transfer column then names the target object and the
marker carry/reset mode. This is the edge record's explicit source-object
field, not an informal inference.

| Edge | Repair tag | Inherited obligation | Target object / marker carry or reset | Operator / determinant ownership rule | Exact obstruction and coverage witness | Forbidden escape | Edge terminal |
|---|---|---|---|---|---|---|---|
| `E00a: N00 -> N35F` | instantiate full positive affine source | `O-I,O-R,O-M,O-D` | Select $P$ and its all-$n\ge2$ generator marker | No prior operator owner exists | Full-source strict height and infinite-outdegree theorem cover this tag | Prime subalphabet or reset edge | `N35F` code |
| `E00b: N00 -> N35P` | instantiate bounded affine slice | `O-I,O-R,O-M,O-D` | Select $M_r$ and its $U/V$ generator marker | No prior operator owner exists | Slice strict height covers this primary tag | Adding recurrence by reset edge | `N35P` code |
| `E01: N35P -> N35S` | add formal inverse edges | `O-R,O-M,O-D,O-X` | Object resets; marker becomes oriented-edge count | Positive adjacency ownership does not transfer | Every edge supplies a two-step primitive backtrack | Calling this the original positive graph | `N35S` code |
| `E02: N35S -> N35H` | Hashimoto reduction | `O-R,O-S,O-M,O-D,O-X,O-G` | Same oriented-edge object; immediate reversals removed; marker carried | Symmetric adjacency is replaced by Hashimoto operator | $vu\bar v\bar u^r$ survives and matched presentations reproduce it | Claiming nonbacktracking means relation-free | `N35H` code |
| `E03: N35H -> N35Q` | finite congruence quotient | `O-R,O-S,O-M,O-D,O-X` | Object and generally ledger reset; quotient marker separately typed | Only finite quotient matrix owns its determinant | $U_q^q$ is added for every frozen quotient row | Infinite Fredholm limit without theorem | `N35Q` code |
| `E04a: N35H -> N35D` | diagonal Gibbs substitution | `O-S,O-M,O-D,O-X` | Hilbert space and marker reset to the diagonal spectral object | $D_\beta$ ownership stays local to $\ell^2(\mathbb N^\times)$ | Trace-log identity separates $\zeta(\beta)$ from the graph determinant | Gibbs trace called graph recurrence | `N35D` code |
| `E04b: N35H -> N35B` | prime-Fock/bosonic substitution | `O-I,O-S,O-M,O-D,O-X` | Basis, Hilbert space, and occupation marker reset | Fock-product ownership stays local to the preloaded prime basis | Prime support and occupation fugacity expose the object/marker change | Prime Fock support treated as emergent | `N35B` code |
| `E05: N35H -> N36F` | complete relation-cell filling | `O-R,O-A,O-S,O-M,O-D,O-X,O-G` | Cayley paths are quotiented by cells; attempted unit marker carried and tested | Prequotient $T$ retains owner; no quotient determinant is inherited | Contractibility, degree equation, and positive prequotient relation coefficient jointly cover complete fill | $z=1$, first return, or determinant conflation | `N36F` code |
| `E06: N36F -> N36G` | diagonal scalar chain superlift | `O-A,O-S,O-D,O-G` | Group-completed chain object resets; graded convention explicit | Ordinary and superdeterminant categories are distinct | Euler multiplier $1-2+1$ covers every power and every matched one-relator presentation | Arithmetic credit for universal zero | `N36G` code |
| `E07: N36F -> N37O` | historical successor: source-derived finite-rank inverse-edge coefficient | `O-R,O-A,O-S,O-M,O-D,O-X,O-G` | Reset to the separately source-locked unquotiented Hashimoto object; the original edge marker is redeclared, not transported from the fill | New matrix $T_{P,\theta}$ proves its own trace-class ownership; no `N36F` owner transfers | Nilpotence criterion covers ordinary invertible factors | Reading the edge as cumulative unfill-plus-coefficient composition, or using a noninvertible automaton as transport | `N37O` code |
| `E08: N37O -> N37D` | explicit even/odd grading | `O-A,O-S,O-M,O-D,O-G` | Same path object and marker; determinant category becomes explicit ratio | Each parity owns an ordinary determinant; only the ratio is graded | Frozen shear fixture gives direct all-orders match and exact mixed leak | First trace or aggregate cancellation | `N37D` code |
| `E09: N37D -> N37N` | saturate complete relator normal closure | `O-A,O-S,O-M,O-D,O-G` | Same object and marker | Same determinant ratio | Every closed label lies in the normal closure, so total saturation erases every factor | Omitting mixed products while claiming full cancellation | `N37N` code |
| `E10: N37N -> N38T` | switch to the Bass--Serre tree canonical for the frozen ascending-HNN splitting/presentation | `O-I,O-R,O-S,O-D,O-X,O-G`; `O-M` resets | New full-tree object and new tree-edge marker; historical successor reset, not cumulative composition | No Cayley/local-coefficient ownership transfers | Paper 37 explicitly names this as the unique remaining in-contract new object | Another representation or alternative tree | `N38T` code |
| `E11: N38T -> N38M` | apply canonical modular cocycle | `O-R,O-S,O-M,O-D,O-X` | Full tree and new marker carried | Weighted operator must prove ownership anew | Constant-orientation weight leaves an orthogonal noncompact family | Root damping or arbitrary phase | `N38M` code |
| `E12: N38T -> N38L` | import tree-lattice determinant | `O-D,O-X,O-G` | Action/orbital framework differs; marker separately typed | Ordinary Fredholm ownership never transfers categories | Faithful-nondiscrete $r\ge2$ and discrete-image/nonproper $r=1$ split covers all theorem values | Quotient image or $1/\infty=0$ | `N38L` code |
| `E13: N38T -> N38O` | replace tree recurrence by group conjugacy | `O-R,O-S,O-M,O-D,O-X,O-G` | Object and recurrence notion reset; height marker replaces tree closed-path marker | No full-tree determinant ownership transfers | Burnside/Moebius theorem gives generic necklace product or balanced divergence | Calling orbital closure literal tree periodicity | `N38O` code |
| `E14: N38T -> N38K` | transport old marker to tree | `O-M,O-X,O-G` | Object reset already occurred; proposed marker carry is tested and fails | No operator transfer | Explicit $u^m,u^mv,R_r$ collision witnesses cover noninjectivity | Silent same-marker credit | `N38K` code |
| `E15: N38T -> NC` | close literal full-tree row | all unresolved obligations | No further object | No owner | Empty/non-Fredholm pair violates `O-R` and `O-D` | New full-tree repair after stop | `CLOSE_ENTIRE_AFFINE_BRANCH` |
| `E16: N38M -> NC` | close canonical-weight row | all unresolved obligations | No further object | No owner | Modular weight cannot repair `O-D` or `O-R` | Noncanonical damping | `CLOSE_ENTIRE_AFFINE_BRANCH` |
| `E17: N38L -> NC` | close tree-lattice row | all unresolved obligations | No further object | No owner | Hypotheses/category fail | Determinant relabelling | `CLOSE_ENTIRE_AFFINE_BRANCH` |
| `E18: N38O -> NC` | close orbital row | all unresolved obligations | No further object | No owner | Generic/divergent substitute violates `O-S`, `O-X`, and `O-G` | Drop balanced/generic controls | `CLOSE_ENTIRE_AFFINE_BRANCH` |
| `E19: N38K -> NC` | close marker row | all unresolved obligations | No further object | No owner | Explicit collision violates `O-M` | Altered clock | `CLOSE_ENTIRE_AFFINE_BRANCH` |
| `E20: N35H -> NX` | boundary/support/KMS/prime projector repair | `O-I,O-X` | Object, support, or marker resets | Ownership reset | Paper-35 firewall and Paper-38 forbidden list classify the tag as outside contract; no universal no-go is inferred | Present exit as same object | `STOP_OUTSIDE_FROZEN_AFFINE_CONTRACT` |
| `E21: N36F -> NX` | first return/induction/changed degree repair | `O-M,O-X` | Marker and object reset | Ownership reset | Paper-36 successor boundary excludes the tag | Claim unit-clock preservation | `STOP_OUTSIDE_FROZEN_AFFINE_CONTRACT` |
| `E22: N37N -> NX` | auxiliary Paper-37 future-search firewall; **not** an $\mathcal A_{14}$ repair tag | `O-A,O-S,O-X` | Any unenumerated coefficient category would reset | Ownership reset; no candidate owner is asserted | The hashed Paper-37 source lock and clues forbid a post-result retry with “another” matrix, character, fiber rank, nilpotent automaton, auxiliary representation, or arbitrary completion; this is historical boundary evidence only | Treating the English nouns as new $\Sigma_{16}$ alternatives, a $\Gamma$ class witness, or a theorem against arbitrary constructions | `STOP_OUTSIDE_FROZEN_AFFINE_CONTRACT` |
| `E23: N38T -> NX` | alternative tree, basepoint damping, finite-total-weight retrofit, groupoid/von Neumann category, new affine object | `O-X` | Object, marker, operator, or determinant category resets | Ownership reset | Paper-38 entire-branch closure lists these as forbidden exits | Universalizing P38 instead of declaring exit | `STOP_OUTSIDE_FROZEN_AFFINE_CONTRACT` |
| `E24: NC -> NR` | return governance to global registry | registry existence only | No affine object or marker carried | No affine owner transfers | Session-4 source lock plus registry provide six historical non-affine witnesses | Ranking or coordinatewise assembly | `RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY` |
| `E25: NC -> NS` | empty-registry fallback | counterfactual registry predicate only | No affine object or marker carried | No affine owner transfers | Coverage witness is the guard $R_*=\varnothing$; observed $R_*$ has six elements, so this edge is inactive | Inventing a witness or traversing both registry guards | `STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR` |

The edge partition is exact: `E00a,E00b,E01`--`E03`, `E04a,E04b`, and
`E05`--`E14` are the seventeen
internal transitions; `E15`--`E19` are closure edges; `E20,E21,E23` are the
three token-associated contract exits; `E22` is the sole auxiliary non-domain
firewall; and `E24,E25` are governance guards. In particular, `E22` is not in
$\mathcal T_{17}$, is not the image of any $\Sigma_{16}$ request, and is not
referenced by $\Gamma$. Its explicit historical boundary path is stored under
`non_domain_firewall_edges` in the bridge rather than among request
classification paths. That path has ID `H_NX_E22` and canonical-string
SHA-256
`1231fe11f42c13ec3a7925d68d89f066b1deb2460f57924ecb76dd3d3490850a`.

Projection does not reverse field transfer. Although `E07` projects to the
coarse spine edge `E36_37`, only obligation/provenance carries. The coarse
edge must record `RESET` for object, marker, operator owner, and determinant
owner under `P37_SOURCE_LOCK_SD_C39`. The P37 one-edge marker is a redeclared
target field, not an equivalence transporting the P36 marker. Calling the
unquotiented target “analogous” to a P36 prequotient comparison does not prove
identity with the filled/control source and cannot authorize an
unfill-plus-coefficient construction.

## 5. Coverage map for the retrospective Paper-39 encoding

### 5.1 Exact fourteen-class alphabet

The top-level alphabet is the exact Paper-38 list

$$
\mathcal A_{14}=\{\texttt{affine\_cayley\_representation},
\texttt{finite\_rank\_local\_system},\texttt{character},
\texttt{grading},\texttt{quotient},\texttt{induced\_shift},
\texttt{first\_return\_map},\texttt{bass\_serre\_splitting},
\texttt{valuation\_tree},\texttt{boundary\_model},
\texttt{modular\_phase},\texttt{basepoint\_damping},
\texttt{finite\_total\_weight\_retrofit},\texttt{groupoid\_trace}\}.
$$

Its exact coverage relation $\Gamma:\mathcal A_{14}\to
\mathcal P(\mathcal V\cup\{NX\})$ is set-valued because one repair class can
have several frozen representatives, and because the canonical representative
of a class may be tested while alternative instances are exits.

| Frozen repair class | Contract disposition | Typed witness node(s) | Exact coverage statement |
|---|---|---|---|
| `affine_cayley_representation` | `TESTED_OBSTRUCTION` | `N35F,N35P,N35S,N35H,N36F` | Positive recurrence is empty; inverse edges add backtracks; Hashimoto retains the generic relation polygon; complete filling erases recurrence. |
| `finite_rank_local_system` | `TESTED_OBSTRUCTION` | `N37O,N37D,N37N` | Invertible ordinary deletion requires impossible nilpotence; direct grading leaks; full saturation erases all closed factors. |
| `character` | `TESTED_OBSTRUCTION` | `N37O,N36G` | Rank-one invertible transport falls under ordinary factor deletion; the frozen scalar chain character erases every matched presentation. |
| `grading` | `TESTED_OBSTRUCTION` | `N36G,N37D,N37N` | Scalar grading proves too much; the non-flat graded fork leaks unless saturation makes the entire product one. |
| `quotient` | `TESTED_OBSTRUCTION` | `N35Q,N36F` | Finite quotients add cycles and do not descend to the infinite owner; complete cell quotient destroys the recurrent ledger and marker. |
| `induced_shift` | `CONTRACT_EXIT_ONLY` | `NX` (boundary witnesses `N36F,N38K`) | Induction resets the source object or clock; no theorem says all induced shifts fail. |
| `first_return_map` | `CONTRACT_EXIT_ONLY` | `NX` (boundary witnesses `N36F,N38K`) | First return changes the frozen step marker; it is excluded, not refuted universally. |
| `bass_serre_splitting` | `CANONICAL_TESTED_ALTERNATIVES_EXIT` | `N38T` and `NX` | The full tree canonical for the frozen ascending-HNN splitting/presentation is empty/non-Fredholm; the explicitly listed alternative-splitting token changes the frozen object. |
| `valuation_tree` | `CONTRACT_EXIT_ONLY` | `NX` (boundary witness `N38K`) | A valuation tree is a new tree and marker requiring a new source lock; no valuation-tree no-go is claimed. |
| `boundary_model` | `CONTRACT_EXIT_ONLY` | `NX` (comparison firewalls `N35D,N35B`) | Frozen Gibbs/Fock comparisons expose space/support/marker mismatch, but no boundary-model mechanism is admitted; arbitrary boundary models are outside the retrospective Paper-39 encoding. |
| `modular_phase` | `CANONICAL_TESTED_OBSTRUCTION` | `N38M,N38O` | The permitted canonical modular weights preserve noncompactness; the separately typed orbital substitute is generic or divergent. |
| `basepoint_damping` | `CONTRACT_EXIT_ONLY` | `NX` | Root-dependent damping changes the canonical cocycle and operator. It can change compactness, so undamped noncompactness is not asserted against it. |
| `finite_total_weight_retrofit` | `CONTRACT_EXIT_ONLY` | `NX` | Summable retrofit changes the weighting/operator category and may restore trace class; it is excluded rather than disproved. |
| `groupoid_trace` | `CANONICAL_CATEGORY_TESTED_ALTERNATIVES_EXIT` | `N38L` and `NX` | The frozen tree-lattice import fails its hypotheses/ownership; another groupoid determinant is a different category, not a universally obstructed object. |

Thus every element of $\mathcal A_{14}$ has a nonempty, explicitly typed
classification. A status containing `EXIT` is a nonmembership statement, not
a mathematical impossibility statement.

The instance universe is exactly the following sixteen frozen tokens; it has
no catch-all token and no closure under arbitrary composition.

| Class group | Exact frozen instance token(s) | Token disposition |
|---|---|---|
| `affine_cayley_representation` | `AFFINE_CAYLEY_FROZEN_FAMILY` | `OBSTRUCTED` |
| `finite_rank_local_system` | `FINITE_RANK_LOCAL_SYSTEM_FROZEN_FAMILY` | `OBSTRUCTED` |
| `character` | `CHARACTER_FROZEN_FAMILY` | `OBSTRUCTED` |
| `grading` | `GRADING_FROZEN_FAMILY` | `OBSTRUCTED` |
| `quotient` | `QUOTIENT_FROZEN_FAMILY` | `OBSTRUCTED` |
| `modular_phase` | `MODULAR_PHASE_FROZEN_FAMILY` | `OBSTRUCTED` |
| `induced_shift` | `INDUCED_SHIFT_EXIT` | `EXIT` |
| `first_return_map` | `FIRST_RETURN_MAP_EXIT` | `EXIT` |
| `valuation_tree` | `VALUATION_TREE_EXIT` | `EXIT` |
| `boundary_model` | `BOUNDARY_MODEL_EXIT` | `EXIT` |
| `basepoint_damping` | `BASEPOINT_DAMPING_EXIT` | `EXIT` |
| `finite_total_weight_retrofit` | `FINITE_TOTAL_WEIGHT_RETROFIT_EXIT` | `EXIT` |
| `bass_serre_splitting` | `FROZEN_ASCENDING_HNN_BASS_SERRE_SPLITTING`; `ALTERNATIVE_BASS_SERRE_SPLITTING_EXIT` | `OBSTRUCTED`; `EXIT` |
| `groupoid_trace` | `FROZEN_TREE_LATTICE_GROUPOID_IMPORT`; `ALTERNATIVE_GROUPOID_CATEGORY_EXIT` | `OBSTRUCTED`; `EXIT` |

Let $\Sigma_{16}$ be this literal token set. The token classifier
$\chi:\Sigma_{16}\to\{\texttt{OBSTRUCTED},\texttt{EXIT}\}$ is total by this
table. Family tokens mean exactly the parameterized families quantified by
the cited predecessor theorem; they do not mean every possible instance that
could share the English class label.

### 5.2 Seventeen internal transition tags

The expanded proof DAG refines the top-level classes into the seventeen
internal transition tags on `E00a`, `E00b`, `E01`--`E03`, `E04a`, `E04b`, and
`E05`--`E14`. Call this internal alphabet $\mathcal T_{17}$. Unlike
$\Gamma$, the map

$$
\kappa_{\rm int}:\mathcal T_{17}\longrightarrow
\{N35F,N35P,N35S,N35H,N35Q,N35D,N35B,N36F,N36G,N37O,N37D,N37N,
N38T,N38M,N38L,N38O,N38K\}
$$

is the single-valued head-node map. Exact edge enumeration proves its
totality; this is not an empirical inference. The seventeen tags are proof
refinements and must not be mistaken for seventeen top-level repair classes.

### 5.3 Provenance paths and the theorem domain

Let $\mathcal P_{\rm fr}$ be the finite set of **nonempty audit provenance
paths** from `N00` through edges in $\mathcal T_{17}$. If $p$ ends at node
$v$, let $X_v(r)$ be the source-frozen typed candidate family audited at that
node. Define

$$
\mathfrak C_{\rm aff}(r)
=\coprod_{p\in\mathcal P_{\rm fr}}\{p\}\times X_{\operatorname{end}(p)}(r).
$$

For $c=(p,x)$, every `Good` coordinate is evaluated on the endpoint datum
$x$, with the endpoint node's marker and ownership fields. Earlier-node data
are provenance only. In particular, an edge labelled `reset` starts a
separately typed historical successor audit. It is not a map that transports
or combines candidate coordinates. Thus `E07` does not “unfill” `N36F` and
then add coefficients; it points to the independently source-locked
unquotiented coefficient object `N37O`.

No set of arbitrary compound repairs is defined or quantified over. A
coordinatewise assembly, an unlisted token, or a new English instance of a
class label is outside the theorem and requires a new source lock.

The coverage criterion is:

1. all fourteen top-level classes occur exactly once in the class table;
2. all sixteen and only the sixteen frozen instance tokens occur in the token
   table;
3. every one of the seventeen internal transitions has exactly one typed
   edge head;
4. every in-contract head node names a predecessor theorem falsifying at
   least one conjunct of `Good`;
5. every exit classification is explicitly nonmembership, never a newly
   proved impossibility;
6. object-changing edges reset marker and ownership unless the edge record
   explicitly carries them, and no reset is read as cumulative composition;
7. the auxiliary `E22` firewall has empty request-token and class-coverage
   fibers and is excluded from all class/token/endpoint exhaustiveness claims;
8. all internal and terminal edges are acyclic under the rank function

$$
\begin{aligned}
&\rho(N00)=0,\quad \rho(N35F)=\rho(N35P)=1,\quad
\rho(N35S)=2,\quad\rho(N35H)=3,\\
&\rho(N35Q)=\rho(N35D)=\rho(N35B)=\rho(N36F)=4,\\
&\rho(N36G)=\rho(N37O)=5,\quad\rho(N37D)=6,\quad
\rho(N37N)=7,\quad\rho(N38T)=8,\\
&\rho(N38M)=\rho(N38L)=\rho(N38O)=\rho(N38K)=9,\\
&\rho(NX)=\rho(NC)=10,\quad\rho(NR)=\rho(NS)=11.
\end{aligned}
$$

Let $\mathcal V_{\rm obs}=\operatorname{im}(\kappa_{\rm int})$. Since every
$p\in\mathcal P_{\rm fr}$ is nonempty,
$\operatorname{end}(p)\in\mathcal V_{\rm obs}$. The explicit map
$F:\mathcal V_{\rm obs}\to
\mathcal P(\{I,R,S,D,M,C\})\setminus\{\varnothing\}$ in the quantifier audit
records which `Good` coordinates each endpoint theorem falsifies. This is
endpoint-obstruction totality, not graph-termination rhetoric: an outgoing
edge can be a later reset successor to a new endpoint object.

Consequently,

$$
\forall r\ge2\;\forall c\in\mathfrak C_{\rm aff}(r),\qquad
\neg\operatorname{Good}(c),
$$

and the finite classification statements are

$$
\forall a\in\mathcal A_{14},\quad\Gamma(a)\ne\varnothing,
\qquad
\forall\sigma\in\Sigma_{16},\quad
\chi(\sigma)\in\{\texttt{OBSTRUCTED},\texttt{EXIT}\}.
$$

The first is the relative closure theorem; the latter two are exact finite
contract coverage. None is a universal affine classification or a theorem
about arbitrary compound repairs.

## 6. Core inherited derivation chain

### 6.1 Positive, inverse-edge, and Hashimoto fork

For $M_r=\mathbb N_0\rtimes_r\mathbb N_0$,

$$
U(b,k)=(b+r^k,k),\qquad V(b,k)=(b,k+1).
$$

The height $b+k$ increases on every positive edge, so no positive directed
cycle exists. After formal reversal, $e\bar e$ is a two-edge primitive
backtrack. Hashimoto reduction removes that backtrack but not

$$
C_{r,x}=vu\bar v\bar u^r,\qquad |C_{r,x}|=r+3.
$$

These are **inherited theorems**. They prove that the three recurrence rows
are different typed objects and that none supplies a selective same-object
primitive ledger.

### 6.2 Complete filling and marker failure

The relation cell equates paths of lengths $2$ and $r+1$. An additive degree
into a torsion-free abelian group obeys

$$
\deg v+\deg u=r\deg u+\deg v,
\qquad (r-1)\deg u=0.
$$

For $r\ge2$, $\deg u=0$, so the unit edge degree does not descend. Complete
cell filling makes $K_r$ contractible, while the separately owned prequotient
operator has

$$
\operatorname{Tr}(T_{r,\theta}^{r+3})
\ge (r+3)\theta^{2S_r}>0,
\qquad S_r=\frac{r(r+1)}2+2r+5.
$$

These are **inherited theorems** and show simultaneous recurrence erasure,
marker non-descent, and determinant non-descent.

### 6.3 Finite coefficients

For a complete ordinary primitive factor,

$$
\det(I-tW)=1
\iff \operatorname{Tr}(W^m)=0\ \forall m\ge1
\iff W\text{ is nilpotent}.
$$

Invertible holonomy cannot satisfy this. The graded shear pair cancels the
direct relator factor but leaks on

$$
M_r=\bar u^rv\bar u^{r-1}vu\bar v^2,
\qquad
\operatorname{Tr}W_r(M_r)-\operatorname{Tr}W_{-r}(M_r)
=-4r^4(r-1).
$$

If cancellation is required on the entire normal closure, every closed
Cayley word is covered and $Z_{\rm gr}=1$. These are **inherited theorems**.

### 6.4 Tree of the frozen ascending-HNN splitting

The full tree has no positive reduced closed path. Nevertheless, for an
infinite orthonormal edge family,

$$
\langle B\delta_{e_i},B\delta_{e_j}\rangle=0\quad(i\ne j),
\qquad \|B\delta_{e_i}\|^2=r,
$$

so $B$ is noncompact and not trace class. Canonical modular step weights are
nonzero orientation constants and preserve this obstruction.

The separately typed positive-height conjugacy ledger obeys, for $r\ge2$,

$$
P_r(1)=r-1,\qquad
P_r(k)=\frac1k\sum_{d\mid k}\mu(d)r^{k/d}\quad(k>1),
$$

and

$$
Z_{+,r}(z)=\prod_{k\ge1}(1-z^k)^{-P_r(k)}
=\frac{1-z}{1-rz}.
$$

It is generic across ascending-HNN controls; at $r=1$ it is not locally
finite. Translation length $\ell_T(a,k)=|k|$ collides with the old generator
clock. These are **inherited theorems**.

## 7. Sharp countermodels and adversarial validity checks

These checks prevent illicit quantifier enlargement.

1. **Finite-cycle countermodel.** The adjacency $A$ of the directed cycle
   $C_m$ is finite rank,

   $$\det(I-zA)=1-z^m,$$

   and its primitive ledger is nonempty. Hence the closure cannot mean “all
   symbolic systems are empty or non-Fredholm.”

2. **Nilpotent boundary.** For
   $N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$,
   $\det(I-tN)=1$. This defeats an unrestricted factor-deletion no-go but is
   outside invertible parallel transport.

3. **Root-damping boundary.** A diagonal edge weight with summable absolute
   mass can make $DHD$ trace class on a locally finite tree. It introduces a
   root/absolute-height choice and is excluded from the canonical modular
   contract; Paper 38 does not disprove it.

4. **Proper-tree boundary.** A discrete group acting properly with finite
   stabilizers on a locally finite tree can satisfy tree-lattice determinant
   hypotheses. The frozen $G_r$ action does not. Therefore determinant
   inapplicability is action-relative.

5. **Balanced controls.** At $r=1$, the relation is length-homogeneous and
   the automorphism-group image is discrete. Yet the filled square grid is
   contractible, the original $\mathbb Z^2$ tree action is nonproper with
   infinite kernel, and the orbital ledger diverges. Each corrected boundary
   is necessary.

6. **First-trace counterexample.** The invertible traceless $J$ above has
   nontrivial determinant factor, so first-trace cancellation never proves
   all-orders deletion.

7. **Generic-erasure counterexample.** The scalar $(1,2,1)$ superlift and the
   convention $1/|\mathbb Z|:=0$ both erase matched generic controls; this is
   `PROVES_TOO_MUCH`, not selectivity.

## 8. Registry handoff derivation

The Session-4 file is explicitly a “Preregistration and Source Lock” and says
that candidate definitions were frozen before numerical results were
inspected. It freezes `SD-C01`--`SD-C04`; its source-discovery addendum freezes
`SD-C05` and `SD-C06` before their experiments. All six objects are outside
the affine repair contract.

Let

$$
R_*=\{c:\operatorname{HistoricallyLockedNonAffine}(c)\}.
$$

Then

$$
\{\mathrm{SD\!\!-C01},\ldots,\mathrm{SD\!\!-C06}\}\subseteq R_*,
$$

so $R_*\ne\varnothing$. Therefore the realized guard selects `E24`, not
`E25`.

This is not a claim that $R_*$ contains an unevaluated candidate. In fact,
all six have Route-A records. “Unspent successor” is undefined in the frozen
P38 handoff text. Any future predicate of that kind requires a new prospective
source lock.

## 9. Route consequence

Because `SD-C41` is a meta-object and has no candidate mechanism,

```text
(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
affine_branch = CLOSE_ENTIRE_AFFINE_BRANCH
realized_terminal = RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY
conditional_empty_terminal = STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR
```
