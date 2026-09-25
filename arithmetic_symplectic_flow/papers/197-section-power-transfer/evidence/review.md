# Actual mathematical review: full-section power transfer

**Paper ID:** 197-section-power-transfer  
**Candidate ID:** AQC-20260916-SPT01  
**Reviewed status:** ADVANCE — FULL-SECTION POWER REPRESENTATION AND ORDINARY FREDHOLM IDENTITY ON RE S > 1; NATURALNESS OPEN.  
**Review date:** 2026-09-16.  
**Initial core digest capture:** 2026-09-16 05:56:00 UTC.  
**First two-summary targeted capture:** 2026-09-16 06:03:36 UTC.  
**Final four-summary targeted capture:** 2026-09-16 06:12:16 UTC.  
**Reviewer invocation:** `/root/research_controller/power_transfer_reviewer_round19`.  
**Verdict:** No unresolved required correction after F19-P1; all four identified summary corrections accepted and closed.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Actual reading, provenance and scope

This is the one actual different-invocation mathematical review assigned
to 197, not an assignment notice or a criteria-only receipt. Before
reading the author's completed proof, this invocation read the frozen
[card](../candidate-card.md) and the complete source, topology, section
and full-orbit arguments in the
[193 paper](../../193-indecomposable-radial-quotient/paper.md), together
with its [card](../../193-indecomposable-radial-quotient/candidate-card.md).
It independently derived the proposed representation and sent the
controller preliminary risk feedback. After the controller reported
author stop-write and core readiness, this invocation completely read
the then-current [README](../README.md), [card](../candidate-card.md),
[paper](../paper.md), [ledger](../claim-ledger.md) and
[evidence index](README.md). No author core was edited by this reviewer.
The later F19-P1 finding and bounded re-readings are recorded below;
the initial review missed the erroneous summary sentences and must
not be read as a claim that no correction was ever required.

The local guidance, plan, entry page, roadmap boundary and prior-work
guide were read for scope. ARS was limited to its fully read router,
academic-paper workflow and argument-builder claim/evidence/reasoning
discipline. No external-paper assertion in the prior-work guide was
adopted as a theorem premise. No external lookup or theorem import was
needed for the explicit estimates below.

The reviewer and author inherit the selected model and shared context.
The card-derived audit preceded reading the completed draft, but the
review is not blind: the proposed claims were supplied in the task and
preliminary feedback was communicated to the controller and author.
There was no model substitution, separate external-model call or helper
review tree. This is model checking, not human peer review, venue
validation, novelty validation or a certificate of independent errors.

## Independent rederivation and final-text checks

### 1. Source and unchanged full owner

The span of products of two nonunits is exactly the composite-coordinate
span, so I/I^2 has the derived prime basis. The construction nevertheless
retains every finite positive mixed support. The actual section topology,
map F(u)_a=u_a/[a c(u)] and roof -log c(u), with c(u)=sum_a u_a/a,
are precisely those proved for 193. Neither a completed cone nor a
disjoint-face topology replaces them in 197. The non-Zeno lower bound
log 2 and the full time-preserving suspension owner remain the old
proved geometric dependency; no old analytic operator is inherited.

### 2. Uniform bounded continuity, injection and state separation

For sigma=Re(s)>1, sum_a u_a^(2 sigma)<=1 on the whole section.
Cauchy--Schwarz therefore gives ||J_s b||_infinity<=||b||_2. In
particular, for finite-coordinate truncations b_N,

    sup_(u in S) |J_s(b-b_N)(u)| <= ||b-b_N||_2 -> 0.

This is an actual uniform tail estimate, not an inference from the fact
that each individual state has finite support. The author's stronger
Lipschitz estimate is also valid: the positive-real function x^s has
derivative s x^(s-1), continuous at zero with value zero, so its
Lipschitz constant on [0,1] is at most |s|. This gives the stated
bound in ||u-v||_0 and hence continuity for the original stronger
weighted-norm topology.

Singleton evaluation recovers b_a, proving injection and norm one.
If two arbitrary section states differ in coordinate a, the moduli of
their coordinate powers are u_a^sigma and v_a^sigma, which differ.
Thus the image separates all states, including mixed points. The
transported Hilbert completion changes the observable space only; it
does not complete or restrict the geometric section.

### 3. Kernel convention and observable-space limitations

With the inner product linear in its first argument, the coefficient
vector of K_s(.,v) is (overline(v_a^s))_a. Consequently

    <J_s b, K_s(.,v)> = sum_a b_a v_a^s = J_s b(v).

Both the conjugation placement and the claimed exact evaluation norm
are correct. Bounded evaluations and the transported complete norm
establish the RKHS statement.

The author's constant-exclusion argument using infinitely many atoms
is valid. An independent finite-edge check reaches the same conclusion:
if J_s b is a nonzero constant C, singleton evaluations force b_a=C;
at (q_a+q_d)/2 its value would have modulus
|C| 2^(1-sigma)<|C|. Products u_a^s u_d^s, a different from d, vanish
at every singleton but not at that mixed point, so coefficient recovery
rules out algebra closure.

For s different from t, membership of u_a^s in H_t would force its
coefficient vector to be the a-th unit vector. A mixed two-coordinate
edge would then give x^s=x^t for every x in (0,1), which is impossible.
This proves genuinely different sets of physical functions, without an
unrequested classification of their intersections. The final paper
explicitly limits completeness to the transported norm and does not
claim sup-norm closedness in C_b(S), resolving the preliminary scope
risk flagged during the card audit.

### 4. Full-state forward composition before spectral assignment

All factors in u_a/[a c(u)] are positive real when u_a is nonzero.
Using the declared real logarithm gives, on every section state,

    c(u)^s (u_a/[a c(u)])^s = a^(-s) u_a^s.

Zero coordinates also agree under the fixed 0^s convention. This
establishes L_s J_s=J_s T_s and invariance of H_s before its traces
are assigned. The result is the actual forward weighted-return
composition, not an inverse-branch sum or an axes-only operator.
The explicit mixed state (q_2+q_3)/2 gives c=5/12, return weights
(3/5,2/5), and the checked value 4^(-s) on u_2^s. Telescoping the
successive normalizations yields all three identities in equation (9),
including the actual mixed-state accumulated return time.

### 5. Ordinary traces, determinant and convergence domain

Under the proved unitary identification J_s, the singular values are
a^(-sigma). Their sum is bounded by the convergent all-integer power
sum for sigma>1. This gives ordinary Hilbert trace class, with no
regularization or Banach-nuclearity substitution. The Parseval and
absolute-sum argument in equation (11) correctly proves that the trace
does not depend on a specially selected orthonormal basis. It applies
to every positive power and gives sum_a a^(-rs).

The all-integer tail bound N^(1-sigma)/(sigma-1) is valid for the
stated integer cutoff. The k-th exterior-power absolute trace bound
(sum_a a^(-sigma))^k/k! establishes the ordinary Fredholm series and
its finite-rank product limit. The bound in equation (15) permits the
logarithmic power series and both summation orders. Thus the product,
exponential formula, normalization and nonvanishing are justified.
A common sigma_0>1 on every compact subset gives locally uniform
convergence and holomorphy on exactly the claimed sufficient half-plane.
No sharp-boundary or continuation assertion is needed for this result.

### 6. Complete physical ledger, not a selected periodic subcarrier

For every full state, exp(t)v=D^j v requires exp(t)=a^j in every
nonzero coordinate for one common integer j. Distinct positive atoms
exclude a nonzero return on every mixed support. On a singleton,
the time stabilizer is exactly (log a)Z, and positive amplitudes lie
on one actual radial orbit. This rederives the complete primitive
ledger, not merely the behavior of chosen representatives.

Its unit-weight positive repetitions are therefore exactly a^(-rs)/r.
Their absolutely convergent sum equals the proved power-trace series,
so the reciprocal packet zeta equals the ordinary determinant in the
specified domain. No stability weight or unproved geometric fixed-point
trace formula is used to bridge a missing ownership step. The continued
presence and point separation of aperiodic mixed states are compatible
with this identity on the deliberately restricted observable space.

### 7. Controls and remaining nonclaims

The changed-unit-roof control destroys the exact cancellation; the
generic distinct-multiplier alphabet reproduces the mechanism only
under its separately stated summability assumption. Equal multipliers
would produce additional mixed recurrent states. These are appropriate
ownership and PROVES_TOO_MUCH controls, not extra main candidates.

The five read cores consistently retain the designed, nonunital,
nonalgebraic and s-dependent representation, OPEN source-clock and
representation naturalness, and the absence of a fixed physical
Hilbert-flow generator. No determinant is transferred to 194 or 196.
The analytic construction establishes no classical symplectic A0--A2,
formal Route passage, completed determinant, target-zero statement or
Route-B coordinate.

## F19-P1: correction history and four-summary closure

**Final disposition:** MINOR summary correction, accepted and CLOSED
for the four identified summary surfaces after the final targeted
re-reading on 2026-09-16 at 06:12:16 UTC.

### First two-summary correction, 06:03:36 UTC

The first targeted receipt reported closure of the README and Abstract
corrections at 06:03:36 UTC. That historical two-surface check remains
valid for those corrected sentences, but its unqualified closure wording
was premature: it did not cover the two additional summary surfaces
subsequently identified below.

After this invocation's initial review, the controller found that the
README compressed power traces, the repetition series and the
Fredholm determinant into an incorrect common equality with a
repetition product. The original author was authorized to correct that
sentence only. During the requested targeted re-reading, this reviewer
then identified the same error remaining in the paper's Abstract. The
controller authorized the original author to correct that second
sentence only. This reviewer had missed both summary errors during
the initial complete reading; they were not errors first introduced
after review.

The correct relationships, already proved in the unchanged substantive
argument, are distinct:

    tr(L_s^r) = sum_a a^(-rs),
    log Z_X(s) = sum_(r>=1) tr(L_s^r)/r,
    det(I-L_s) = Z_X(s)^(-1).

The first two corrected summaries say that the power traces generate
the repetition series and that the determinant is the inverse of the
corresponding primitive-orbit product. This invocation actually re-read
both corrected summary surfaces, compared them with the already
reviewed equations (12), (14) and (16), and made a targeted text scan
of these same trace/product summary phrases. At those two surfaces,
no trace is identified with the whole product and the determinant has
the correct inverse relation. This did not establish correction of all
result-summary surfaces in the package.

This was two bounded author summary deltas and one targeted review
closure, not a new mathematical contract, proof expansion or repeat of
the complete mathematical audit. That digest command confirmed that
the candidate-card and claim-ledger hashes were then unchanged.
Only the README and paper bindings were replaced at that stage. No author
core or evidence index was edited by this reviewer, and no whole-batch
mechanical validation was rerun.

### Remaining two-summary correction and final closure, 06:12:16 UTC

The subsequent 198 scope reviewer identified the third surface: the
appended audit outcome in candidate-card.md still combined the
trace/operator and determinant result with the primitive product
without the required distinction. Root's subsequent targeted scan
identified the fourth surface: the paper's Section 7 Decision still
described the determinant as equal to the complete primitive ledger
without stating its inverse-product normalization. The original author
received bounded authority to correct these outcome sentences and
stopped writing after doing so.

This discovery sequence is retained rather than retroactively called a
clean first review. The initial reviewer, author and early controller
and root readings did not catch all four result-summary surfaces.
The earlier two-surface closure was not evidence of complete summary
coverage. The mathematical formulas themselves were already correct;
this correction did not change the frozen object or the proved
operator, trace or determinant contract.

This invocation then actually read only the new candidate-card appended
outcome and Section 7 Decision deltas. The card now explicitly says
that power traces generate the repetition series and the determinant
equals the inverse primitive-orbit product. The Decision now explicitly
states det(I-L_s)=Z_X(s)^(-1) and calls it the inverse unit-weight
primitive-orbit product. Both agree with the already reviewed equations
(12), (14) and (16). The card's Section 3 stopping-test question about
equality with the unchanged full packet ledger is a prospective test,
not an erroneous outcome assertion; no frozen definition was altered
to resolve this summary finding.

Final F19-P1 closure is therefore specifically the four corrected
surfaces: README summary, paper Abstract, candidate-card appended
outcome and paper Section 7 Decision. It is not a claim of a new
full-text audit or mathematical verification rerun. The final digest
capture confirms that README and claim-ledger retain their preceding
hashes, while candidate-card and paper have the new bindings below.
No core was edited by this reviewer, no new reviewer was dispatched,
and no full-tree or whole-batch check was performed.

## Exact four-core byte binding

After the original complete reading this invocation captured all four
hashes at 05:56:00 UTC. The original README hash was
`8b5bb24800de5c15ef5f684936f12c183cd79c0b1f113b470edaaebbc925298f`
and the original paper hash was
`f9540486fda7e99f110190819299460b4641037963ee3ae2dbcd04f2b06496df`.
The historical two-summary capture at 06:03:36 UTC changed the paper
hash to
`a596e268bc258153bd71ac349462bf53797d1fd023907cce1bd79cd5cdc18a22`,
while the candidate-card still had its original hash
`2ecc6bb03e00a5ba119a8cdc26fa52f5a4e111f723593ff74382bf0cfd26eba5`.
Those two hashes are now superseded historical bindings only.
Following the third and fourth summary corrections, the last targeted
re-reading and the author's renewed stop-write, this invocation ran
`sha256sum` on the four cores again. The table records the final
bindings captured at 06:12:16 UTC. The evidence
index and this review remain unbound so actual integration receipts can
be appended without changing the reviewed mathematical claims.

| Core | SHA-256 |
| --- | --- |
| [README.md](../README.md) | `d8ed30b4d843cf5b75a431025a7227c8c558c28cfb5317155875912cb3f5b9b9` |
| [candidate-card.md](../candidate-card.md) | `4d715a8629897362c233965eeefdf31ab2d1cac971938cad1d9a94db0a1b3fc3` |
| [paper.md](../paper.md) | `f8a896a41ddbf053235823f25751e2d3c4df0a19360ad1c23eee7e9518c36f5e` |
| [claim-ledger.md](../claim-ledger.md) | `9f86663ba4a47f757923a64b45260a488ced7ac66b25c65b55a38b4883f5fe36` |

No whole-batch mechanical validation is claimed by this receipt. Root
owns the sole integrated link, identity/status and byte-binding check.
This review supports the bounded ADVANCE decision and stopping at the
proved contract, not expansion into a new theorem or carrier. After
writing this receipt, the reviewer stops writing and returns integration
ownership to the controller and root.
