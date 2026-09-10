# Independent review of the C429–C433 batch outline

2026-09-10 UTC. Current-team, nonauthor outline review using the
paper-plan claim/evidence framework and the batch/proof-writer scope
and dependency checks. This is an outline audit, not a new admission
round, a fresh full re-proof of the accepted mathematics, or one of the
two manuscript reviews required later.

## Decision

**CHANGES REQUESTED: three small, concrete outline repairs before drafting.**
The five admitted questions, their allocation, and their substantive
proof obligations survive unchanged. I found no outline-level reason
to reopen admission or create, merge, or replace a contract. In
particular, the C430/C431 dependencies are noncircular; C429 retains
every prime and degree; C432 excludes every polynomial reversor; and
C433 retains ordinary products and both kinds of support exceptions.

The mandatory repairs below make the frozen theorem interfaces explicit
in the outline itself. They require no new theorem, computation, source
search, manuscript, or PDF. Root adjudicates the repairs and requests
targeted readback before closing the outline gate.

## Reviewed inputs and evidence boundary

I read all 328 lines of `BATCH_PLAN.md` and all 778 lines of
`ADMISSION_DECISIONS.md`, including the current Section 6. Historical
lower counts are not the current decision: **5/5 contracts are admitted
and 0/5 papers are complete**.

Input SHA256 values actually recomputed for this review:

| Input | SHA256 |
| --- | --- |
| `BATCH_PLAN.md` | `4faeaa9197bf9f429ccc79f20fa1739213881c2bccaf0f15cfc67686bd8747de` |
| `ADMISSION_DECISIONS.md` | `244d40921c1fb0fef5604162c55db5efeabf38bd5e5914d2f02fd7516882a78e` |
| R10 A3 final 713-line proof/report | `34a773edfce1e02e3dbe39f967888d4e49ba50d1384040f07d350c1e79779f1c` |
| R10 E8 429-line review | `6074afa280e6ac735074b1da70532b2d9adc38e0d6a56d16a209b920117c0951` |
| R10 X2 293-line source report | `340c85b45f11c5a5fec8c18b4490a70c7c313f39cad2b8309a55414aa7628a85` |

The last three agree with the final admission pins. Checking those
hashes is not a claim to have independently repeated E8's entire
mathematical review. For this outline audit I read the entire final A3
proof and entire X2 report, and the pertinent E8 statement, boundary,
provenance, and final-assessment sections. The five-line provenance
addition is credited; the accepted mathematical body remains frozen.

For C429 I inspected the actual R4 and R5 theorem/certificate statements,
the characteristic-two statement and parity dependency audit, and the
final finite-certificate arguments. For C430/C431 I inspected the actual
all-level inertia and oriented-quotient interfaces, the arbitrary-field
coefficient realization and contact estimates, D1's compact-limit and
aperiodicity proof, and the eventual tower's uniform character-transfer
argument. For C432 I inspected the actual exhaustive-family statement,
whole-group dependency map, coset/descent and all-place proof sections,
and the failed two-factor control. Relevant source/substantiality records
were read as local evidence, not converted into a claim that every
prospective bibliography entry has now been independently verified.

All line locations below refer to the pinned 328-line outline.

## Mandatory minimum repairs

### M1. C429: define the finite-certificate input and all three tests

**Location:** lines 118–128, following the claim/evidence matrix.

The displayed bounds use an integer $M\ge1$ without stating that it
bounds $\deg h$. The symbols $F_j,H_j$ are not defined in this outline,
and only the Hasse-regime divisibility is actually displayed. The
instruction to compare three regimes is sound, but it does not itself
freeze the other two tests.

**Minimum repair:** add

$$\deg h\le M,\quad M\in\mathbb Z_{\ge1},\qquad
F_j=f^{\circ j}-x,\qquad
H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i},$$

with zero input explicitly included, and give this three-row interface:

| Regime | Test at each of the two specified levels |
| --- | --- |
| $p\nmid d(d-1)$ | $F_j\mid F_j'H_j(h)$ |
| $p\mid d$ | $F_j\mid H_j(h)$, since $F_j'=-1$ |
| $p\mid d-1$ | $F_j\mid D^{[P]}F_j\,H_j(h)^P$, where $P=p^{v_p(d-1)}$ |

Define $D^{[P]}$ as the coefficient of $z^P$ in evaluation at $x+z$.
Retain the existing two-level formulas and bounds, applying the first
formula to the first two rows and the Hasse formula to the third.
These are exact equivalent certificates for the accepted theorem,
including characteristic two and constants, not only necessary tests.
The degree bounds stated here are iterate-degree bounds, not bounds on
every unreduced product in the test or optimized running time.

**Evidence:** R4 A2 `PROOF_PACKAGE.md`, Claim and final certificate;
R5 A2 `PROOF_PACKAGE.md`, Claim and finite-certificate conclusion;
R5 A2 `CHARACTERISTIC_TWO.md`, Claim, dependency audit, and final
certificate. This restores definitions already proved in those inputs;
it does not alter PC424-L.

### M2. C430: state the odd-prime range and sharpen the AS label

**Location:** lines 137–145, with the same scope carried into the
formal theorem and any eventual-tower consequence.

The one-sentence contribution currently introduces $p$ without its
odd-prime restriction. The admitted UL4 theorem and its oriented
quotient theorem both explicitly require odd $p$. C431's restriction
cannot silently supply a missing hypothesis in C430.

**Minimum repair:** begin the C430 contribution with “For every odd
prime $p$, over $K=\overline{\mathbb F}_p((s))$, …”. Also replace
the matrix label “Exact first-AS class and first-level intersection”
with “Native-oriented AS-class stabilization and first-level
intersection,” as independently suggested by the proposed C430 author.

The latter wording matches what the cited argument establishes:
$[a_e]=[a_2]$ with the prescribed $+1$ native generator and equality
of the embedded degree-$p$ fields. It does not promise an explicit
full-coefficient Laurent representative for general $p$. The outline's
later distinction between classes, raw resolvents, and field nesting
is correct and should stay. The accepted ramification invariants in
lines 158–161 are separate claims and are not withdrawn by this repair.

**Evidence:** R3 A3 `FULL_LOCAL_INERTIA.md`, Claim; and
`ORIENTED_QUOTIENT_STABILIZATION.md`, Claim and Sections 1–2. The
latter states the general-prime class equality and labels its explicit
reduced representative as a $p=3$ specialization.

### M3. C433: make the ordinary CP criterion self-contained

**Location:** lines 269–294, preserving the support warning at
lines 296–303.

“Height $m$” and “the original $F_n,H_n,S_*$ definitions” refer to
the right source, but leave the displayed central finite criterion
undefined in the outline. This is particularly important because
$H_n$ must be a difference of two whole orbit products, not a product
of pointwise differences or a multiplier-weighted trace.

**Minimum repair:** explicitly set $A,B\ne0$, $\gcd(A,B)=1$,
$m=\max(\deg A,\deg B)$, and define

$$F_n=f^{\circ n}-x,\qquad
H_n=\prod_{i=0}^{n-1}A(f^{\circ i}(x))-
    \prod_{i=0}^{n-1}B(f^{\circ i}(x)),\qquad
S_* =\prod_{r=1}^{D}F_r.$$

Define (CP) as: all but finitely many ordinary primitive affine cycles
avoid the zeros and poles of $g$ and satisfy
$\prod_{x\in O}g(x)=1$. Each distinct point is counted once under
one original application of $f$. Keep the present values of $b,D,N$
and the range $1\le n\le N$ unchanged.

Also make the proposed author's two terminology/domain clarifications
explicit. A product-visible return point satisfies
$F_n(x)=0$ and $H_n(x)\ne0$ for some $n$; a cycle is visible if it
contains such a point. If the comparison table uses Jacobian-visible
data, distinguish the condition $e_n(x)H_n(x)\ne0$, where
$e_n(x)=\operatorname{ord}_x F_n$ is interpreted in $k$. The latter
comes from the derivative-filtered annihilator and is not, in general,
the condition $F_n'(x)H_n(x)\ne0$ evaluated pointwise. Here $F_n'=-1$
makes every $e_n(x)=1$, so this distinction cannot discard an ordinary
product-visible return. The one-step skew map is defined on
$(\mathbb A^1\setminus V(AB))\times\mathbb G_m$ with values in
$\mathbb A^1\times\mathbb G_m$; this domain need not be forward
invariant. Iteration along an admissible cycle is well-defined.

Carry the existing support distinction into this theorem interface:
under (CP), every cycle visible in some cleared $H_n$ has period at
most $D$; this does not bound the number of exceptional points, nor
the period of a cycle meeting both numerator and denominator zeros.
The latter cycles are finite support exceptions invisible in these
cleared products. No rational/algebraic transfer conclusion is added.

**Evidence:** admission Section 6 and the final R10 A3 report,
Sections 1, 4, 7, and 8. The report already proves the full ordinary
statement; this repair avoids an accidental change of observable in
the transition to manuscript writing. The contrasting filtered
visibility definition was checked directly in R10 A1's report,
Section 3, rather than inferred from the word “Jacobian.”

## Claim/evidence and complete-proof placement audit

| Paper | Interface preserved by the outline | Proof placement assessment |
| --- | --- | --- |
| C429 / PC424-L | All $p$, all $d\ge2$, all $c$, polynomial $h$; ordinary sums including wild periods; additive polynomial coboundary equality | Sections 2–7 assign normal form, full cyclic algebra, leading-coefficient stabilization, adjacent-level detection, Hasse/adaptive cut, and characteristic-two checks. M1 completes the finite interface. Typeset the substantive carry and stabilization arguments, not only their matrices. |
| C430 / UL4 | Fixed Laurent-series base and separable closure; every canonical $p^e$ cycle; native cyclic Galois action; oriented first quotient and level-one separation | Sections 2–6 cover Hensel factors, contacts, full inertia, class matching, and actual field ramification. M2 restores odd $p$. The optional eventual tower has a separate, correctly declared dependency and a full section/appendix location. |
| C431 / OM4 | Every allowed complete algebraically closed odd-characteristic field and $0<|\lambda-1|<1$; full sequence of real probability measures; compact type-I limit | Sections 2–6 include the actual arbitrary-field realization, all-higher-level contact identity, unbounded anchor estimate, aligned couplings, compactness, aperiodicity, and native adding-machine conjugacy. No subsequence or formal-field substitution is proposed. |
| C432 / RLG5 | One whole four-factor native word over $\mathbb Q(\sqrt7)$; local witnesses at every original completion; exclusion of all global polynomial reversors | Sections 2–5 retain the full amalgam/axis centralizer equality, primitive translation labels, pointwise stabilizer, scalar twist, original-field descent, and all-place arithmetic. Section 6 retains a genuine nonlinear-reversor control. No affine/involution ansatz replaces the whole-group proof. |
| C433 / FCP10 | All derivative-zero polynomials, all nonzero reduced rational weights, ordinary CP, unrestricted coefficient fields and support multiplicities | Sections 2–7 place normalization, the CP ideal, general-polynomial Laurent extraction, two-block contraction, both full-rank evaluations, long-return persistence, the visible-period bound, and the final cutoff inside the article. M3 completes the formal criterion. |

The shared instruction at lines 33–38 correctly requires all central
new proofs in each article or its included appendix. Local proof-file
links are author inputs, not admissible substitutes in the finished
paper. A precisely stated companion theorem may be cited with an
accessible reference and truthful unpublished status; the outline does
not require duplicating an entire companion article merely to avoid
circularity.

## C430/C431 dependency check

The actual dependency order is:

1. Credited small-cycle geometry, coefficient realization, Hensel
   factorization, and displacement/contact algebra provide shared inputs.
2. UL4 proves its full local inertia and native-oriented first quotient.
   Independently, OM4's A1 contact theorem and D1 compact-limit/aperiodicity
   argument prove the complete-field measure/adding-machine theorem.
3. Only the optional later tower combines the native Galois action with
   that compact limit to obtain eventual higher quotient characters.

There is no arrow from UL4 full inertia to the standalone OM4 proof:
A1 explicitly realizes the canonical factors without irreducibility or
local inertia. Conversely, UL4's core does not invoke the eventual tower.
The latter's finite clopen quotient proof gives a threshold uniform on
the whole Galois group, in the order
$\forall j\ \exists E_j\ \forall e\ge E_j\ \forall g$.
The outline correctly excludes $E_j=j$, $K_j=L_j$, and nesting of the
original $L_e$. Its character-kernel fields are in the separable closure;
the type-I compact limit in the completion is not asserted algebraic.

## Source subtraction and remaining drafting checks

The plan correctly separates classical ingredients from each integrated
increment: residue/normal-form and Hasse methods for C429; small-cycle
geometry, ramification, and character extraction for C430; classical
compact isometric inverse limits and Haar measure for C431; Wang and
whole-group reversing/centralizer mechanisms for C432; and arbitrary-field
word cutoffs, rank factorization, residue algebra, and the shared R9/A1/root
development for C433. Bounded searches do not certify worldwide priority.
No unverified bibliographic placeholder becomes verified by this review.

During drafting, retain these already-supported distinctions:

- In C431, the closure containing old finite cycles need not be uniquely
  ergodic; the limiting compact set has the proved aperiodic Haar system.
- In C432, state $a\in L^\times$ before using its inverse, keep the
  rightmost-first convention, and mark that $\mathbb Q(\sqrt7)$ has
  two real places and no complex places. Do not invent a complex local
  case for that actual field. The failed two-factor control must exhibit
  its nonlinear involutions, not merely say the affine ansatz fails.
- In C433, use the arbitrary-field reachability/rank arguments, not the
  rational-only Gram argument in the cited source. Characteristic two,
  nonmonic scaling, $m=0$, and all positive returns remain included.
  No finite-support word-series premise or optimized-runtime claim is added.

These are manuscript readback checks, not additional outline blockers.
The shared article format and useful exact comparison tables fit this
proof-only batch. No ML venue, artificial page quota, numerical experiment,
decorative figure, forced score, or invented author information is needed.

## Gate status and work performed

After M1–M3 are adjudicated, only their affected outline passages need
targeted independent readback to close this gate. The two actual full
manuscript review/revision passes remain separate downstream obligations;
this audit counts as neither. Actual compilation, visual inspection,
formal evaluation, and release verification are likewise still future
gates, not achievements inferred from a favorable outline.

Only this allocated review file was created. No accepted proof/source
artifact, author directory, shared state, evaluator, Git object, or PDF
was changed. No nested agent, external-model/API call, mathematical
program, source query, or new primary-source opening was used in this
outline task. `NO_BAD_EULER_OR_ROOT_NUMBER` and the Route B exclusion
remain unconditional.

## Targeted repair verification — outline gate recommendation

2026-09-10 UTC. Root accepted M1–M3 and amended only the relevant
outline interfaces plus the two C432 notation/place clarifications.
The original review above remains the historical **CHANGES REQUESTED**
decision on the 328-line input; it has not been replaced or relabeled.
Its frozen 268-line SHA256 before this append was
`eada466e04917d831c0b7b7503ace05762fcb7562e2e8cf81bc109e39defbfd6`.

I independently read the affected passages and their adjacent theorem
interfaces in the revised 374-line `BATCH_PLAN.md`, with actually
recomputed SHA256
`7cbf39601ccc3ae0677b45ce1a8ac8cc3321ddc3277f09769b5c6382b6e2946e`.

| Required repair | Revised location | Readback result |
| --- | --- | --- |
| M1: C429 finite-certificate interface | Lines 118–144 | **CLOSED.** The degree constraint, zero branch, return/sum definitions, all three disjoint derivative regimes, Hasse derivative, two-level equivalence, and unchanged iterate-degree bounds are explicit. All primes, all degrees, ordinary roots, and constants remain included. |
| M2: C430 scope and oriented class | Lines 156–191 | **CLOSED.** Odd $p$ is explicit and the matrix now says native-oriented AS-class stabilization. Native sign, embedded fields, level-one separation, actual ramification invariants, and the optional tower's noncircular dependence remain correct. |
| M3: C433 ordinary CP interface | Lines 307–349 | **CLOSED.** Nonzero coprime inputs, height, whole-product difference, $S_*$, cofinite admissible ordinary cycles, every return through $N$, support distinctions, and the non-forward-invariant one-step domain are explicit. The constants and admitted theorem are unchanged. |

The C433 terminology is now sharper than an undifferentiated use of
“visible”: product visibility is $H_n(x)\ne0$ at a return root;
derivative-filtered contribution is $e_n(x)H_n(x)\ne0$; and native
Jacobian visibility alone is the condition $p\nmid e_r(x)$ at native
period $r$, without an observable attached. The revised outline does
not identify any of these with pointwise $F_n'(x)H_n(x)\ne0$ at a
possibly multiple return root. In its derivative-zero theorem all
return multiplicities are one, exactly as the accepted proof requires.

The additional C432 edits at lines 264–285 correctly state
$a\in L^\times$, two real places, and no complex places for the
actual field. The full polynomial reversing coset and all-place
counterexample are unchanged. C431's full-sequence, arbitrary-field
statement, contact bounds, and absence of a full-inertia premise remain
unchanged; no new C430/C431 dependency was introduced.

**Targeted verification result: all three mandatory repairs are closed;
zero outline must-fixes remain. Recommend that root close the outline
gate and activate the five already allocated drafting tasks.** This
recommendation applies to the pinned revised outline, not to nonexistent
manuscripts or PDFs. The five admission decisions stand, and both
separate actual manuscript review passes and all later verification
gates remain required. Root retains ownership of the status transition
and activation; this reviewer has not edited shared state or author files.
