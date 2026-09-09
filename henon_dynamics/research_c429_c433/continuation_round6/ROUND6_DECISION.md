# Round 6 — auxiliary proofs closed; full-question gaps retained

Coordinator mathematical checkpoint, 2026-09-09 17:58 UTC. All five
allocated R6 nonauthor mathematical reviews are now fully read and closed
at their stated scopes, with zero open must-fixes. This is a research
decision, not a completed-paper release or an already performed R6 push.
The verified Git baseline is
`dcf475843e87bb5a7c4026ec986a0e73bf065046`; the frozen R5 research
commit is `6d37f9fad2ff75a23b491690c44719dcd60ad620`.

**Four independent contracts remain admitted; zero papers are complete.**
PC424-L, UL4, OM4 and RLG5 keep their existing boundaries. There is no
fifth-contract admission, manuscript numbering, five-contract plan freeze,
formal route evaluation, PDF or target-arithmetic promotion in this record.
Five complete papers is a checkpoint, not the continuous-run stopping rule.

## 1. Final mathematical decisions

| Actual artifact and full question at its stated scope | Coordinator decision | Remaining boundary |
| --- | --- | --- |
| [E2 affine-coordinate reflection classification](e2_nine_reflection_directions/REPORT.md), with [E6 independent review](reviews/e6_nine_reflection_directions/REVIEW.md) | Accept the complete strict-subclass theorem, zero open must-fixes | Not the full integral tame stabilizer or integer period-nine question |
| [C2 Sections 1–4](c2_nine_point_stabilizer/REPORT.md): exact nine points, actual maps and restriction group | Accept the shared explicit data and the group $S_3\times C_3$ | A preserved set of nine points is not a nine-cycle |
| C2 Section 5: arbitrary vertical quadratic shear followed by arbitrary unimodular affine coordinates, with [E4 independent review](reviews/e4_quadratic_shear_reflections/REVIEW.md) | Accept the complete specified quadratic-shear subclass, zero open must-fixes | No arbitrary pre-affine change, higher shear, general nonlinear conjugator or full tame-stabilizer classification |
| C2 Section 6: arbitrary-degree single vertical triangular conjugate of the specified affine map, with [separate E6 review](reviews/e6_triangular_affine_conjugates/REVIEW.md) | Accept the full single-conjugator proposition, zero open must-fixes | Intermediate points may leave the set, but a general returning tame word is not covered |
| [X2 replacement scout](x2_independent_replacement/REPORT.md), M6 | Accept the elementary counterexamples as auxiliary and reject this proposed new-paper candidate | No full multiplicative kernel classification |
| X2 replacement scout, Z6 | Reject admission: the full all-odd-characteristic transcendence claim is unproved here | An old source-owned question with no demonstrated all-level counting bridge, not a refuted statement |
| [B1 wandering-singleton report](b1_wandering_singleton_bridge/REPORT.md) | Accept the bounded gap disposition and the elementary conditional arithmetic step | The common irreducible rational time equation is unproved; unchanged LG4 remains open |
| [A4 specified primitive-branch report](a4_primitive_branch_bridge/REPORT.md), with [E4 independent review](reviews/e4_primitive_branch_bridge/REVIEW.md) | Accept the characteristic-zero crossing, contact identity, conditional fold/isolation interfaces and collision control; zero open must-fixes at those scopes | Actual mod-three survival, full SB and PC424-D remain unproved; RB is unassessed |
| [X2 MS6 source audit](x2_multiplicative_saturation_sources/REPORT.md) | Accept the limited source disposition and the explicit non-counterexample | Neither source retrieval nor an already algebraic transfer supplies existence from cofinite products |
| [A2 MS6 saturation theorem](a2_multiplicative_saturation/REPORT.md), with [E8 complete independent review](reviews/e8_multiplicative_saturation/REVIEW.md) | Accept the all-parameter conditional saturation theorem and its stated equivalences, zero open must-fixes | Cofinite products have not been proved to imply torsion; original MS6 remains open |

The coordinator has read all 407 lines of E2, all 378 current lines of C2,
all 354 lines of the first E6 review, all 201 lines of the second E6 review,
all 203 lines of E4's quadratic-shear review, and all 340 lines of X2.
Root has also read B1's complete 219-line report, A4's complete 171-line
report, E4's complete 94-line primitive-branch review and X2's complete
207-line MS6 source report. The author/reviewer date labels follow their
environment date; this coordinator receipt uses the actual UTC clock.
Root also read all 441 lines of A2's final saturation report and all 340
lines of E8's final review. The five actual mathematical review files
total 1,192 lines. No audit or source scout is counted as another
mathematical review.
These are actual-file reads. Version matching below
establishes integrity only, not a substitute for the proof checks.

## 2. Exact nine-point results and their proof boundaries

Use E2's labels $0,\ldots,8$ for

$$
C=\{(0,0),(1,0),(1,1),(3,1),(0,2),(-1,-2),(-1,0),(1,-1),(2,2)\}.
$$

The actual maps are $A(x,y)=(1-y,x-y)$ and
$I(x,y)=(x,q(x)-y)$, where
$q(t)=-t^4+4t^3-2t^2-3t+2$. Their restrictions are $a,i$.
C2 uses labels one larger; the reviews check this conversion explicitly.

For every integral unimodular affine coordinate change $B$ and every
$Q\in\mathbb Z[t]$, a nonidentity restriction to $C$ of
$B^{-1}(u,Q(u)-v)B$ that preserves $C$ is exactly one of
$i,aia^{-1},a^{-1}ia$. The 36 unordered point pairs yield 18 primitive
unoriented directions in six $A$-orbits. Four direction orbits fail a
mod-two polynomial value condition; one fails the mod-five condition.
The remaining orbit has actual integral-polynomial realizations, not only
rational or integer-valued interpolation. The affine coordinate lemma
includes signs, complements and integer translations. The resulting
restriction group is exactly $S_3\times C_3$, with no element of order nine.

The quadratic-shear extension is now also independently accepted: for
every nonzero integer $b$, conjugating a triangular reflection by
$L\circ V_b$, where $V_b=(x,y+bx^2)$ and $L$ is any integral unimodular
affine map, yields only the known vertical restriction $i$ whenever it
preserves $C$. Three fixed labels and three exchanged pairs are forced by
the bijection $C\to\mathbb F_3^2$. The proof covers all 31 nonvertical
pairs, all slope denominators, all unbounded parameter ranges and six
finite exceptions, then eliminates the three remaining cases by integer
polynomial divisibility. E4 supplies the explicit common-fiber tables,
including shared endpoints, and verifies both determinant signs and all
coordinate complements. No finite-search extrapolation is involved.

The independently reviewed single-conjugator proposition states that for
every

$$
E(x,y)=(\alpha x+c,\beta y+f(x)),\quad
\alpha,\beta\in\{1,-1\},\quad c\in\mathbb Z,\quad f\in\mathbb Z[t],
$$

if $E^{-1}AE$ preserves $C$, its restriction belongs to
$\{a,iai,a^{-1},ia^{-1}i\}$. The centroid forces $\alpha=1,c=0$;
the possible intermediate invariant set lies among 18 explicitly listed
lattice points. Complete orbit/multiplicity classification leaves four
sets, and the exact fiber gap leaves only $C$ and $R(C)$, where
$R(x,y)=(x,x-y)$. The four actual restrictions of $E$ are $1,I,R,RI$;
inverse restrictions are taken on the correct intermediate set. This
covers every degree of $f$, without a coefficient window.

These propositions do not exclude arbitrary nonlinear coordinate
conjugates, longer tame words with changing directions and intermediate
sets, or another integral nine-point set. Periods $9,12,18,24$ in the full
integer spectrum remain unresolved; the accepted R5 period-16 exclusion
and genuine dyadic-nine witness remain unchanged.

## 3. Replacement rejection and actual source checks

M6's literal original implication fails for every prime $p$: take
$f=x^{p+1}$ and $g=x$. Every admissible native cycle product has $p$th
power one and thus equals one, while a rational transfer would require
$p\operatorname{ord}_0(h)=1$. The base map is separable. This is a complete
negative answer to that implication, but the elementary divisor obstruction
is insufficient independent paper substance. In characteristic five,
$f=x^2,h=x-1,g=x+1$ separately shows why evaluating a cancelled rational
coboundary at its cancelled fixed point does not telescope. Neither
counterexample is a kernel classification.

For Z6, the ordinary native counts are the distinct-root degrees of
$f_p^{\circ n}-x$ for $f_p=x^2+1$. The recently accepted PC424-L carry
certificates concern a possibly nonreduced cyclic algebra and do not
compute those integer counts. UL4 and OM4 concern nonconstant, nontrivially
valued deformations, not the fixed constant-field maps; their multiplier
condition cannot hold for a nonzero constant difference in
$\overline{\mathbb F}_p$.

In addition to reading X2's access record, root actually opened the primary
[Bridy arXiv v2](https://arxiv.org/pdf/1306.5267), including Theorems
1.2–1.3, Conjecture 1.6 and its following $x^2+1$ example. Root also read
the relevant introduction/definition and Theorem A passages of
[Byszewski–Cornelissen–Houben](https://arxiv.org/pdf/1904.04942): the
dynamic-affine hypothesis is explicit and $x^2+1$ is excluded for
$p\ne2,3$. These are bounded source checks, not a claim to have audited
both papers in full or established the worldwide current status of Z6.

### Closed bounded attempts, with the missing arrows retained

B1 found no applicable wandering-singleton theorem in its three new search
batches. Root actually checked the relevant AKNTVV Theorems 4.2–4.4 and
Proposition 4.9, Huang's complete printed Theorem 1.4 and the final step
of its proof, and the local Strassmann Proposition 7.1. Invariant or
periodic targets, local common zeros, and actual-hit sparsity do not give
native integer-time descent for a wandering singleton. The explicit
Huang uniform-in-initial-point control is valid for that printed
quantifier; it is not an LG4 counterexample or a challenge to the accepted
fixed-pair periodic-target result. No external contact was made.

If a single irreducible polynomial $A\in\mathbb Q[T]$ vanished at every
component of the same native profinite time, the transitive Galois action,
a derangement and Chebotarev would force $\deg A=1$. Membership of its
common rational root in every $\mathbb Z_p$ would then give an integer.
The existence of that one irreducible equation is precisely the unproved
ITA bridge. Separate local Weierstrass polynomials do not prove it.

A4 specifies, for every $e\ge2$, the majority-one necklace in R4's
two-element characteristic-zero pair at $n=3^e$, its maximal cyclic
representative, and the corresponding parameter-ray landing $\alpha_e$.
The source-owned primitive successor transposition changes its weight
from $(n+1)/2$ to $(n+3)/2$, so it leaves the pair. The common labeling,
non-real landing and exact native period are proved. This is a classical
monodromy application, not arithmetic survival. Root read the cited
Buff–Tan Lei proofs and Doyle specialization statements; the remaining
model check was completed by actual reads of Corollary 5.4, Remark 6.1
and Propositions 6.2–6.3, including the quotient at $3\mid n$.

Two sufficient arithmetic conditions are explicit but unverified for the
actual landing: the unit $\Delta_{n,n}'(\alpha_e)$, or residual native
period together with units $G_c,G_{xx}$ at its parabolic point. The latter
gives the integral completed form $u=w^2$ by implicit solution and Hensel
lifting; the free constant cyclic quotient does not require division by
$n$. The derivative sums and normal finite-flat two-sheet collision
control have independent zero-must-fix review. Even one surviving edge
would not prove the remaining graph connectivity or all-prime PC424-D.

X2's MS6 audit does not locate a complete theorem or actual counterexample
in its bounded search. In particular $f=x^p,g=1+x$ for $p>2$ has an
algebraic ordinary-series transfer but no $p$-power rational transfer;
norm fibers give infinitely many bad primitive cycles, so this is not
an MS6 counterexample. Its selected Fernandes theorem assumes a finite
extension already exists, a monomial base and $p\nmid d$. The Milne
intersection formula permits inseparable maps and counts multiplicities;
it alone is not a square-root error bound for arbitrary curve selfmaps.
A2's full conditional saturation theorem is now independently accepted.
With $K=\overline{\mathbb F}_p(x)$ and $\delta h=h\circ f/h$, it states

$$
\text{cofinite primitive products }1,\quad g^m=\delta a
\quad\Longrightarrow\quad
g^{p^{v_p(m)}}=\delta b,
\qquad m\ge1.
$$

It retains every prime, every $d\ge2,c$, every rational nonzero $g$
and every ordinary native period. A finite stable algebraic transfer
gives some integer-power relation by the minimal polynomial's constant
term, including inseparable extensions. A $p$-power rational relation
conversely gives a finite purely inseparable stable transfer.

For a prime $\ell\ne p$, a connected Kummer cover from
$W^\ell=\delta h$ has an actual degree-$d$ selfmap. Every good base
cycle lifts to $\ell$ individually fixed points at its exact return,
with equal completed-local fixed-point lengths. A fixed finite bad
set contributes a bounded length along sufficiently large prime return
times, including multiplier-one and inseparable cases. The resulting
lower bound $\ell(d^n+1-C)$ contradicts the upper bound
$d^n+1+2g(Y)d^{n/2}$. Root read the actual Brosnan Hodge statement and
proof in Sections 3.3, 3.1 and 1.1; the author and E8 independently check
the graph normal bundle, full inseparable degree and numerical pairing.
This is not a Frobenius-only count misapplied to a general selfmap.
The split-cover constant phase is separately eliminated by large prime
periods, and the quotient-group argument removes all prime-to-$p$
factors. These are complete supporting steps, not the missing existence
theorem. Under cofinite products, finite torsion, finite stable algebraic
transfer and $p$-power rational transfer are equivalent; obtaining any
one of them from the periodic hypothesis remains unproved.

## 4. Completed allocations and next-round boundary

- E4's independent check of C2 Section 5 is complete: all 203 review lines
  and the actual final hash have been read; zero open must-fixes remain.
- B1 completed `b1_wandering_singleton_bridge/REPORT.md`: a bounded primary-source
  and exact-lemma test for the wandering-singleton gap in unchanged LG4.
  The periodic-target and bounded-degree results are not reopened.
- A4 completed `a4_primitive_branch_bridge/REPORT.md`: one primitive branch
  connection crossing the old characteristic-three quotient cut, with
  characteristic-zero labels separated from the needed mod-three survival.
  Original PC424-D is not narrowed to this proposed bridge.
- A2 completed `a2_multiplicative_saturation/REPORT.md`: one newly frozen
  feasibility question MS6, distinct from the already refuted M6. For all
  primes and all unicritical $f=x^d+c$, are cofinite ordinary-cycle products
  of $g\in\overline{\mathbb F}_p(x)^\times$ equal to one if and only if
  $g^{p^e}=h\circ f/h$ for some $e\ge0$ and rational $h$? “Cofinite” allows
  finitely many primitive-cycle exceptions, not a finite-field test or a
  prime-to-$p$ period restriction. The reverse implication is elementary;
  the forward implication is not assumed. This is not a fifth contract.
- X2 completed `x2_multiplicative_saturation_sources/REPORT.md`: a separate,
  at-most-three-search-batch source check for that exact MS6 implication,
  including rational/perfection/Laurent hypotheses and cancelled-point scope.

C2's 378-line report is frozen; both new subclass reviews are now closed.
The suggested finite restriction lemma is not accepted here. A separate
R7 hand-proof assignment now covers its exact 27-candidate restriction
interface and one genuine integral lifting obstruction, in a new directory.
X2 also has a separate two-batch R7 check of the exact base-period
pointwise-fixed-fiber existence bridge. A2 continues the exact MS6 torsion
existence question through one finite divisor criterion; C4 separately
tests the one explicit nine-point reflection lift in a frozen two-shear
conjugator subclass. E6 checks the new C2 finite lemmas independently.
These allocations do not enlarge R6 or authorize a longer-word census;
none is a promised theorem or a fifth contract. R7 is not part of the
R6 save set.

## 5. Version bindings and execution boundary

| Artifact scope actually checked | SHA-256 |
| --- | --- |
| E2 complete report, 407 lines | 8b3c3da72824eb1c53aee2728f05bcbfcac673085bc18a339ffcc0214051fa73 |
| E6 complete direction review, 354 lines | 0a2d7b486f3046f46879d3aa92c276424de2fd3265ecf7529fff19168fec4cc8 |
| C2 complete report, 378 lines | cbab243d0092fced85a85c02a1a02339b9e7d184566e92595364ad829625f87e |
| C2 original 155-line dependency prefix | d28b4671f8380ff2927fdd20ec7ceef04ce3a4f988650a448deeeaf1b22474dc |
| C2 290-line prefix for the separate quadratic review | 062341bd7dfd496b6884876118600a3bbfffed66e719dac613570bf4ad5d350f |
| E6 complete single-conjugator review, 201 lines | db4e65a2fa4008ac9e3b9b6725160b973d784db455613b93c6599c452553c9e9 |
| E4 complete quadratic-shear review, 203 lines | 79038f967ef14a7f398950e6c438a60ca7b2e42caa32f024dd7abe82a2a16c70 |
| X2 complete first replacement scout, 340 lines | e0d4338df842aafbd1029d1f9feaa1c3853a691947a2ccfdfa97399d89ea2bfb |
| B1 complete wandering-singleton report, 219 lines | 67397d44b625b880bea78d7b7ff5229a105a03c09d56119fa75c3f977d03b475 |
| A4 complete primitive-branch report, 171 lines | 5f248eabe14108c7e7ee0a3a6f3ef7b5d882ed2f9b163f2cc1c562754ac56846 |
| E4 complete primitive-branch review, 94 lines | 59921dd07d0e579a946c594d4754118bcf89912da4d1787fe92e3decb7aa9fa3 |
| X2 complete MS6 source audit, 207 lines | e98895f778d762de715076bc5872a01f5676754c6b1eee808062c012bf32c0fa |
| A2 complete MS6 saturation report, 441 lines | b02bcc4cfad2433b9ee0d88dc69e74ac62ae30e508ddbc4c3787f1adf8ade1c3 |
| E8 complete MS6 saturation review, 340 lines | cf427164edbd5fe3c576af14d91ca783afa704457751a2f2babba2e2abf2b679 |

The full-file hashes above were read from the actual files; root also
recomputed both unchanged C2 prefix hashes in read-only streams, matching
the final independent reviews. R6 has zero
allocated or executed mathematical programs. Read-only source access and
file-integrity checks are not mathematical executions. There are no new
agents, external-model uploads, GPU jobs, evaluator changes, manuscript/PDF
builds or R6 Git synchronization claimed by this checkpoint. Completed R5
and earlier files, the other streams and inherited untracked work remain
read-only. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
