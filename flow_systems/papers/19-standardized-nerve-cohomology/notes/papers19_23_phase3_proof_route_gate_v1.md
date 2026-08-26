# Papers 19--23 Phase-3 proof and Route crosswalk gate v1

Date: **2026-08-24**

Status: **PHASE 3 RESEARCH COMPLETE — P22 STANDALONE PASS, P21 FOCUSED-NOTE PASS, THREE MERGE DISPOSITIONS UNCHANGED**

Post-Phase-2 authority: the user explicitly confirmed continuation into the
next proof round.  That authority covered the bounded P21/P22 Phase-3 kill
tests and their independent adversarial audit.  This gate ends the ARS
research stage.  It does not silently authorize submission, release, Git
action, or a Hilbert--Polya/Route claim.

## 1. Outcome first

The five-slot round produces **two paper-shaped results, not five inflated
manuscripts**:

1. **P22 is the priority standalone theorem.**  No additive lift of the
   sheafified Verschiebung `V_N` exists on the absolute fppf site for any
   `N>1`; the same is true on the finite-flat site.  The proof gives an
   explicit failed descent section.  It also supplies a counterexample to
   the sectionwise Dedekind equality printed as Deninger's Corollary 4.6,
   whose proof confuses a sheaf epimorphism with objectwise surjectivity.
2. **P21 passes as a focused quantitative note.**  Every relative Artin
   conductor is computed, yielding exact maximum conductors and an eventual
   unconditional improvement over `|D_E|^310`.  The result has no printed
   numerical cutoff because Thorner--Zaman retains an unprinted absolute
   implied constant, and it does not beat the ERH bound.
3. **P19, P20, and P23 keep their Phase-2 merge/note dispositions.**  Nothing
   in the new proofs justifies reopening them as standalone manuscripts.

## 2. Phase-3 theorem receipts

### 2.1 P21 — exact relative conductors

For odd `r`, with

```text
F=Q(zeta_r),
E=Q(zeta_(r^(m+1)),p^(1/r)),
```

the complete character ledger gives

```text
Q(E/F)=p^(r-1) r^[m(r-1)+1].
```

At the prime `lambda=(1-zeta_r)`, the Kummer conductor exponent is `2` when
`v_r(p^(r-1)-1)=1` and `0` otherwise; a cyclotomic character of exact order
`r^j` has exponent `j(r-1)+1`.  The latter is at least `r`, so there is no
top-conductor cancellation.  At primes over `p`, every nontrivial Kummer
character is tamely ramified with exponent one.

For `r=2`, after retaining the noncyclic cyclotomic character group and the
small-`m` cancellations,

```text
Q(E/Q)=p 2^(m+1).
```

Thorner--Zaman consequently gives, for odd `r`,

```text
ell <<
 p^[521(r-1)] r^[694(r-2)+521(m(r-1)+1)]
 +
 p^[367(r-1)] r^[232(r-2)+367(m(r-1)+1)]
 (r-1)^[290(r-1)],
```

and, for `r=2`,

```text
ell << (p 2^(m+1))^521+(p 2^(m+1))^367.
```

The implied constant is absolute and effectively computable but not printed
numerically in the source theorem.  The comparison therefore proves an
eventual infinite unconditional improvement range, not a named cutoff.  The
conditional Bach--Sorenson logarithmic-square bound remains strictly the
right ERH lane.

Proof artifact: [P21 relative-conductor theorem](../../21-effective-exact-order-witnesses/notes/phase3_relative_conductor_theorem.md).

### 2.2 P22 — all-index nonlift theorem

On a universe-small absolute `NoethAffSch_fppf` in Deninger's sense, let

```text
Z=underline Z(O)^sharp,
W=W_rat(O),
omega:Z->>W.
```

For every `N>1`, write `N=q^a d`, choose a finite field `k/F_q` containing
`mu_d`, and take the finite-free cover

```text
k[x] -> k[s],       x |-> s^N.
```

Injectivity of `omega` at the Dedekind ring `k[s]` forces the unique local
value

```text
c=q^a sum_(zeta in mu_d)(zeta s).
```

On the double overlap, specialize `s_1|->epsilon`, `s_2|->0` to
`k[epsilon]/(epsilon^N)`.  The descent difference becomes

```text
q^a sum_(zeta in mu_d)(zeta epsilon)^sharp != 0,
```

because the inner sum maps in the big-Witt sheaf to
`1-epsilon^dT^d != 1`, while multiplication by `q^a` remains monic after
abelian sheafification.  Thus no additive lift exists for any `N>1`; `N=1`
is the identity control.  Equivalently, for the actual extension

```text
e:0->K->Z->W->0,
```

there is no `u:K->K` with `u_*e=V_N^*e`.

For `N=2`, the detector is exactly Deninger's surviving
`2(epsilon)^sharp` class. The same finite-free calculation, with the
finite-flat site inputs checked separately, proves that comparator. In that site
it also shows that `1-xT^N in W_rat(k[x])` has no global preimage in
`Z(k[x])^sharp`, correcting Corollary 4.6's printed sectionwise equality.
Proposition 4.5, together with the Dedekind-domain refinement, supplies the
needed injectivity; Corollary 4.6 is not used as a premise.

Proof artifact: [P22 all-index nonlift theorem](../../22-fppf-verschiebung-lifts/notes/phase3_all_index_nonlift_theorem.md).

**Stage-2 receipt (2026-08-24):** the user subsequently authorized local
composition. The standalone seven-section manuscript and 12-page PDF are
complete, and the independent evaluator accepted Round 2. The source-author
note remains UNSENT. Stage 2.5, submission, release, Git action, and Route
advancement remain unauthorized. See the
[Paper-22 pipeline state](../../22-fppf-verschiebung-lifts/notes/pipeline_state.md).

## 3. Five-slot portfolio disposition

| Slot | Strongest proved result after Phase 3 | Paper disposition | Binding next action |
|---|---|---|---|
| P19 | conditional standardized cohomology collapses above degree one | **MERGE INTO P12** | prove the exact author-complex/cup/`J*` comparison only when P12 is reopened |
| P20 | exact fixed finite-coordinate densities and positive-density infinite fibres | **MERGE INTO P15 / TECHNICAL COROLLARY** | obtain the missing 2023 full text before any novelty sentence |
| P21 | exact relative conductors, exact discriminants, specialized unconditional least-witness bound | **FOCUSED SHORT PAPER / SECOND WRITING PRIORITY** | compose with asymptotic/effective wording; do not print a fabricated cutoff or ERH gain |
| P22 | explicit nonlift for every `N>1` on fppf and finite-flat sites; source corollary correction | **STAGE-2 STANDALONE DRAFT COMPLETE / EVALUATOR ACCEPT** | await explicit Stage-2.5 authorization; keep author note unsent |
| P23 | normal tracial weights are central-density weights; full translation invariance selects Haar and erases nonzero returns | **P8 AMENDMENT / TECHNICAL NOTE** | retain the missing converse hypotheses and proxy-only boundary |

## 4. Exact correspondence with the two roadmap files

Roadmap owners:

- [`skills/route-a-evaluator.md`](../../../skills/route-a-evaluator.md),
  version `0.2.0`;
- [`skills/route-b-evaluator.md`](../../../skills/route-b-evaluator.md),
  version `0.2.0`.

These files require one compatible dynamical/operator object and prohibit
coordinatewise promotion.  Papers 19--23 are supporting theorem lanes, not
new Route candidates with the required input tuples.

### 4.1 Route-A layers

| Slot | Potential reusable evidence | A0 | A1 | A2 | A3 | A4 |
|---|---|---|---|---|---|---|
| P19 | cohomological reduction/negative prior | `NOT_TESTABLE` as a dynamical candidate | `NOT_TESTABLE` | `NOT_TESTABLE` | no intrinsic determinant or Weil compression | no lift object |
| P20 | exact arithmetic density prior | arithmetic lemma only; no candidate arithmetic origin tuple | no primitive orbits | no dynamical Zeta | no global analytic owner | no quantization |
| P21 | **proved exact-order arithmetic witness and density** | reusable positive arithmetic structural prior, but not an A0 pass for a missing dynamical candidate | no primitive-orbit owner | no determinant | no Weil/dynamical compression | no lift |
| P22 | **proved obstruction to an algebraic sheaf operation** | off-layer algebraic negative prior | no orbit object | no determinant | no analytic structure | no natural quantization claim |
| P23 | trace-weight proxy and owner-boundary control | no prime-origin tuple | no orbit owner | no determinant | proxy trace is not a Weil compression | no lift |

Therefore no slot receives an `(A0,A1,A2,A3,A4)` success tuple.  P21 may be
reused later inside the arithmetic-relevance evidence of a separately frozen
candidate, but the lemma alone cannot create that candidate.  P23 cannot be
transplanted from the standard-circle proxy to the actual packet.

```text
ROUTE_A_OVERALL=NO_NEW_CANDIDATE_EVALUATION
ROUTE_A_ADVANCEMENT=NONE
ROUTE_B_INVOCATION_ALLOWED=FALSE
```

### 4.2 Route-B layers and Gates A--E

None of the five slots supplies a single Hilbert space, operator action,
dense domain, boundary conditions, self-adjointness theorem, target spectral
type, von-Mangoldt trace, or completed-xi determinant.  In particular:

- P21's exact-order prime witnesses are not a von-Mangoldt weighted trace
  and do not pass `B4`;
- P22's Witt-vector sheaf obstruction is not an operator/domain theorem;
- P23's proxy trace classification does not belong to the same owner as a
  prime-power trace or determinant.

| Roadmap gate | Required owner | Papers 19--23 result |
|---|---|---|
| Gate A | canonical intrinsic dynamical spectral determinant | **NONE** |
| Gate B | time-oriented scattering/unitary completion | **NONE** |
| Gate C | self-adjoint generator and intrinsic `T log T` law | **NONE** |
| Gate D | von-Mangoldt prime-power trace plus arithmetic/Weil compatibility | **NONE** |
| Gate E | completed-zeta divisor equality | **NONE** |

```text
B1=B2=B3=B4=B5=NOT_TESTABLE_FOR_THESE_SUPPORT_LANES
HILBERT_POLYA_CLAIM_ALLOWED=FALSE
COORDINATEWISE_MAXIMUM_USED=FALSE
```

This is a faithful roadmap correspondence, not a negative judgment on the
two paper results: P21 and P22 are manuscript-worthy arithmetic/algebraic
outputs, but paper value and Route advancement are different ledgers.

## 5. Independent adversarial audit

Three failure modes were actively tested and retained in the disposition:

1. **P21 hidden constant.**  The monomial improvement is proved, but a
   particular numerical threshold is not.  `<<` remains in the theorem.
2. **P21 hypothesis split.**  The unconditional relative-conductor result is
   not advertised as an ERH improvement; Bach--Sorenson remains separate.
3. **P22 sheaf versus sections.**  A sheaf epimorphism is only locally
   surjective.  The explicit overlap class both proves nonexistence for all
   possible induced `u` and exposes the source corollary's gap.  Publication
   requires author notification rather than silent correction.

The audit also confirmed that neither abelian group in P21 may be replaced
by a cyclic group when applying auxiliary conductor comparisons.  The proof
uses the character-by-character conductor product and applies the main
Thorner--Zaman theorem, which requires an abelian subgroup, directly.

## 6. ARS research-stage checkpoint

Research question: decide the two surviving Phase-3 kill tests and retain
only paper-shaped results.

Method: exact local conductor calculation and primary-theorem substitution
for P21; explicit finite-free descent obstruction and sheaf-extension audit
for P22; independent devil's-advocate review for both.

Strongest findings:

```text
P21_RELATIVE_CONDUCTOR=PROVED
P21_UNCONDITIONAL_IMPROVEMENT=PROVED_EVENTUAL
P22_ALL_NONTRIVIAL_VERSCHIEBUNG_LIFTS=NONEXISTENT
P22_EXPLICIT_KERNEL_OBSTRUCTION=PROVED
P22_SOURCE_COROLLARY_CORRECTION=REQUIRED
```

Limitations:

- no numerical Thorner--Zaman cutoff without extracting its hidden constant;
- no P21 ERH improvement;
- P22's source correction needs author contact and a human-sensitive audit;
- no Route-A/Route-B advancement;
- P19/P20/P23 remain merge/note results.

Recommended Stage-2 composition order:

```text
1. P22 focused standalone manuscript and correction note;
2. P21 focused quantitative manuscript;
3. keep P19/P20/P23 queued as amendments, not standalone drafts.
```

```text
PHASE3_RESEARCH=COMPLETE
LIVE_PAPER_SHAPES=P22,P21
PRIMARY_MANUSCRIPT=P22
SECONDARY_MANUSCRIPT=P21
FIVE_STANDALONE_MANUSCRIPTS=FALSE
MANUSCRIPT_COMPOSITION=AWAITING_MANDATORY_USER_CHECKPOINT
SUBMISSION_RELEASE_GIT=NOT_AUTHORIZED
ROUTE_ADVANCEMENT=NONE
```
