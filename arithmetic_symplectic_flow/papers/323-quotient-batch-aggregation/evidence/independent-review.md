# Independent internal review — quotient-driven batch aggregation

Candidate: `ANG-20260920-QBA01`.
Package: `323-quotient-batch-aggregation`.
Status: `OWNED BATCH CLOCK; COMPOSITE PRIMITIVES — STOP / FORK`.
Calibration: `NOT_CALIBRATED`; internal inherited-model review only.

## 1. Exact inputs, sequence and limits of independence

The mathematical inputs actually read were the original 152-line
[card](../candidate-card.md) and the released complete 335-line
[paper](../paper.md). The version bindings are:

| Version | SHA-256 | Actual evidence / access |
| --- | --- | --- |
| Original card, first 152 lines | `8c43530ded5637d2d975d951c3a167201a04bdcd174c10c61fb881b8f5333cde` | Measured; read completely to original EOF before raw derivation; prefix remeasured before this report |
| Author's first paper, 317 lines | `46c2b9da4d75d57fa7d0397dd27dbd89ed708f657b83751bdd2cdb6bf882de07` | Author-reported tool lock before any raw mathematical receipt; not read by reviewer |
| Released/final paper, 335 lines | `390b645e864a0d1752b3f0d1c774b978e5c6f891a0c719aaa9a56a54a1a8760e` | Measured, then fully read through EOF without truncation at checkpoint 2 |

The actual sequence was original-card reading, personally completed main/control
raw derivations, metadata-only ALL raw ready, first-draft lock notification and
explicit release permission, six mathematical messages ending ALL RAW FINAL,
explicit paper unlock, measured full-manuscript reading, final adverse check and report.
No manuscript was opened before raw release and explicit unlock. Notification
order does not determine exact cross-agent private derivation or write times.

The author reports an intermediate 318-line terminology clarification after raw
messages 1–5, replacing an ambiguous slash between the ONE control's
two time groups with separate statements. That intermediate file was not read
or independently hash-checked. After raw message 6 the author adopted the
reviewer's explicit NO-DELETION singleton basins and shifted-gcd two-core basin proof.
The final paper is therefore raw-influenced, not an untouched/blind first draft.

The author's interval-digit probability construction was reportedly already in the
first draft. Raw instead used normalized, consistent finite products and the
countable product probability construction. The interval construction was first read
and verified at checkpoint 2; it is not retrospectively credited to raw.

The current ARS router was fully reread for this task, with the
previously read applicable workflow, DA and runtime guidance retained. ARS supplied
checkpoint, adverse-reasoning and scope discipline, not mathematical evidence, venue calibration
or an issue quota. No auxiliary was delegated or consulted.

No scout, ledger, appended outcome, historical research file, peer result or
external source was opened. Source/provenance references seen inside the card/paper
were not followed or independently source-audited. No web, scientific numerical run,
parameter change, extra fixed-word search or higher-period census was performed.
Hashes and line counts are metadata checks only. This report is the
sole written research path; the manuscript and other files were not edited.

The reviewer inherits the same model/runtime, long conversation history and shared
context. Raw-before-manuscript access does not establish fully blinded ideation, cross-model
validation, external peer review, machine proof or independent-error evidence.

## 2. Checkpoint 1: measure, carrier and complete main inverse

The raw normalization is exact:

    pi(n)=1/(n+1)−1/(n+2),  sum_(n≥0) pi(n)=1.

Consistent finite products define the countable product Borel probability. Every
finite cylinder has positive product mass, hence full support. Since pi(n)≤1/2,
every single word has mass at most 2^(−m) for every prefix length m,
and so mass zero. The same bound rules out positive atoms: a
putative atom must meet some member of each countable length-m cylinder
partition with its full mass, contradicting the bound for large m.
All null words remain objects; no conull or returning-word restriction is used.

The full product carrier has arbitrary infinite tails and no finite-dimensional
or local-compactness conclusion is warranted. In fact a basic cylinder still
has an unrestricted infinite alphabet coordinate and is noncompact. The source
domain, second letter b>0, is clopen. At every point q=floor(a/b)
is finite, including genuine q=0 with no batch letters read or consumed.

The source cylinders alpha=(a,b,cword of length q) form a countable
disjoint clopen partition of the domain. Each maps homeomorphically to the
full cylinder beta=(b,d), d=r+sum c_i, retaining the same residual tail.
For target (b,d,eta), the complete inverse is as frozen: b≥1,
any q≥0, any actual length-q batch with sum S, r=d−S in
[0,b−1], and predecessor (qb+r,b,cword,eta). No extra labels survive
as arrows, and no root selection is made.

For q≥1 the exact number at that q is

    sum_(r=0)^min(b−1,d) binom(d−r+q−1,q−1).

For q=0 there is one predecessor precisely when d<b. Each target
with b≥1 has countably infinitely many predecessors overall, since every
q≥1 allows r=0 and batch (d,0,...,0), with distinct source first
letters qb. The complete image is first-letter-positive. First-letter-zero targets
have no predecessor, but are not deleted and need not be terminal:
(0,b>0,eta) legally reaches terminal (b,0,eta).

A terminal (b>0,0,eta) retains every predecessor (qb,b,0^q,eta),
q≥0. A terminal whose first letter is zero has none. These
facts separate inverse existence from the second-letter-zero terminal rule.

## 3. Checkpoint 1: full Borel IMAGE, version and cocycle

Write F(n)=−log pi(n). For an actual main branch,

    J=pi(a)*product_(i≤q) pi(c_i)/pi(d),
    kappa=F(a)+sum_(i≤q) F(c_i)−F(d).

For every Borel subset of C(beta), its tail section is Borel.
The product law gives its measure as W(beta) times that tail's
measure, and the inverse image as W(alpha) times the same tail's
measure. Therefore mu(theta E)=integral_E J dmu for ALL such E,
not just the whole cylinder. Common further prefix refinement cancels the
same tail factor on both sides. Every finite actual history reads only
finitely many letters and can be refined to a finite-prefix replacement.

This proves finite-history and finite-branch-pair integral IMAGE as well as the
pointwise product law. J is finite, positive and cylinder-constant at every
actual inverse point, including null words. The frozen version applies there
without a returning-word exception; a.e. measure equality alone does not choose
arbitrary null values. A q=0 main step has J=1 and kappa=0.

Let S_k be the actual clock prefix. Range z/source w branch-pair
IMAGE is exp(−S_k(z)+S_l(w)), while c=S_k(z)−S_l(w). Thus the
actual forward arrow has lag −1 and clock −kappa; its inverse
has +kappa. Common legal suffixes cancel equal-lag presentations, and composition
aligns actual middle histories at their longer defined length. Terminal T⁰
uses an empty sum, not an absorbing loop or nonexistent next step.

The countable legal-prefix partition makes the iterates and retained-lag relation
Borel. Overlapping inverse images do not license an unweighted whole-map IMAGE
formula. The owner remains actual equal-tail triples with lag, not arbitrary
prefix swaps or free branch words. No invariant mu×dh or regularity of
the coarse quotient is inferred.

For any discovered least-P core with full-cycle clock K, its entire
basin is the union of all finite actual predecessors of its core.
Source isotropy is PZ, time image H=KZ, extension kernel zero if
K≠0 and PZ if K=0. Thus |K| is the least positive
time when nonzero, not merely one available return. If T^d z=q_j,
the complete phase is h−S_d(z)+S_j(q_0), modulo KZ when nonzero
and real when zero. Different hitting choices differ by full-cycle sums.
For a terminal basin, phase is h−S_terminal and all isotropies vanish.

## 4. Checkpoint 1: precisely the four main test words

Let e0=0∞, e1=1∞, e2=2∞, u=(4,2,2,...) and v=(2,4,2,...).
These are complete infinite words, not truncated tests.

| Test | Exact history | Source isotropy; H; extension kernel on full basin |
| --- | --- | --- |
| e0 | Terminal with no incoming branch | 0; 0; 0; isolated real phase h |
| e1 | Fixed, q=1, batch (1) | Z; (log6)Z; 0 |
| e2 | Fixed, q=1, batch (2) | Z; (log12)Z; 0 |
| u | u→v→u; first batch (2,2), then empty batch | 2Z; (log144)Z; 0 |

The fixed densities are pi(1)=1/6 and pi(2)=1/12. At u,
the density is pi(2)²=1/144; at v it is one. Since u≠v,
its source period is exactly two. These complete isotropy images prove
the positive primitive times log6, log12 and log144, not just finite
return arrows. The fixed phases are h−S modulo their respective times.
For u/v, S_1(u)=log144, so both hitting phases reduce to h−S
modulo log144.

Each of the three returning basins contains ALL prescribed predecessors,
not just its core. They are countably infinite: every level is countable,
and an immediate inverse level is infinite. Hence each such basin is null.
Ancestors have eventually constant tails, but ordinary eventual-tail equality is
not the owner relation. In particular e2 and u/v share eventual-2
tails yet belong to disjoint actual T-tail classes, since their deterministic
cycles differ. Therefore log144=2log12 is a distinct primitive packet, not
the second repetition of the e2 packet. Repetitions of a fixed packet
do not create new primitives.

Already e1 supplies the nontarget composite primitive log6. This is the
decisive main STOP / FORK. The other predeclared tests finish the bounded
gate; no assertion that these are the only fixed words, cycles or
positive packets is made, and no further fixed-word search was undertaken.

## 5. Checkpoint 1: three controls with their own owners

### BATCH-FEEDBACK-OFF

Its complete image is (b,d,eta) with b≥1 and 0≤d<b.
All q≥0 and all length-q batches are allowed in its inverse,
with a=qb+d. Every target in this image has countably infinitely many
predecessors. Its density is pi(a)*product pi(c_i)/pi(r), not main's
pi(r+S) denominator; kappa=F(a)+sum F(c_i)−F(r).

The header follows Euclidean (a,b)→(b,r). Each positive second letter
strictly decreases, so every full word terminates within its initial b steps.
This exact decreasing-integer argument closes the control globally without a census.
The terminal header is (gcd(a,b),0); the complete residual tail is
what remains after the Euclidean history's actual cumulative batch consumption.
Full terminal classes must be indexed by the ENTIRE terminal word, not gcd alone.

All source/time/extension isotropy is zero. The finite potential minus the
actual terminal clock prefix makes this control's cocycle a coboundary; its
phase is h−S, even when nonloop clocks are nonzero.
The four tests give e0 terminal, e1→(1,0,1∞) with kappa=log18,
e2→(2,0,2∞) with kappa=log72, and u to that SAME latter
terminal with kappa=log2160. None has a legal one/two-step return.
Here e2 and u genuinely share a terminating basin, unlike main.

### ONE-LETTER-BATCH

At target (b,d,eta), b≥1, every inverse has q≥0,
r=0,...,min(b−1,d), c=d−r and source (qb+r,b,c,eta).
There are min(b,d+1) predecessors per q and countably infinitely many overall.
The complete image is first-letter-positive. q=0 still consumes one actual
letter. Its own density is pi(a)pi(c)/pi(d), and kappa=F(a)+F(c)−F(d).

e0 remains isolated terminal. e1 and e2 are fixed with their own
countably infinite null basins, source isotropy Z, zero extension kernel and
primitive times log6 and log12. Their basin inverse rules differ from main's.
Here u maps directly to e2 with kappa=log30. It is NOT
itself periodic at one or two steps, but belongs to the same full
basin as e2. Thus u still has source isotropy Z and H=(log12)Z,
not zero and not a new log30 packet. Its relative phase is
h−log30 modulo log12. This distinguishes actual period from eventual-core isotropy.
All other source/packet classifications remain outside this test.

### NO-DELETION

The complete tail tau is invariant. At (b,d,tau), use ONLY its
actual prefix sums S_q; predecessors are

    b≥1, q≥0, 0≤d−S_q<b,
    (qb+d−S_q,b,tau).

Distinct valid q give distinct sources, since floor(a/b)=q. The exact
number is #{q:d−b<S_q≤d}. It may be zero, any finite positive
number, or countably infinite. Infinitely many occur exactly when tau is
eventually zero and its total sum lies in (d−b,d]. Terminal
(b>0,0,tau) has one predecessor for each initial all-zero prefix,
including q=0; all-zero tau gives infinitely many. First-letter-zero targets
have none. For example (1,1,2∞) has none but is a legal source.

Retained batch factors cancel, giving OWN J=pi(a)/pi(d), kappa=F(a)−F(d).
The finite global potential B=log[pi(a)pi(b)] satisfies kappa=B∘T−B
on every legal step. Hence c=B(source)−B(range), all H=0, and
full phase is the real value h+B. This does not erase source isotropy.

e0 is isolated terminal. e1 and e2 each have only themselves as
immediate predecessors, hence singleton full basins, source/extension isotropy Z and H=0.
u/v remains an exact two-cycle, with both step clocks zero and
source/extension isotropy 2Z. Its full basin is exactly

    {(a,b,2∞): a,b≥2 and gcd(a−2,b−2)=2}.

Necessity follows from tail invariance and the inverse a=d+(b−2)q,
which preserves the domain a,b≥2 and the shifted gcd. For sufficiency
put U=a−2,V=b−2. The actual update is (V,U−qV),
q=floor((U+2)/(V+2)). If U<V it swaps once. If U≥V>0,
then 1≤q≤U/V and the nonnegative integer sum U+V strictly decreases.
Eventually a coordinate is zero; unchanged gcd2 forces (2,0) or (0,2),
exactly the tested core. This is a complete basin proof for that
one predeclared core, not a search/classification of other constant-tail cores.
The basin is countably infinite and null, with real phase h+log[pi(a)pi(b)].
Other source periods remain unclassified despite the complete global H=0 theorem.

## 6. Checkpoint 2: complete manuscript verification

The measured 335-line paper was read entirely. All inverse domains/counts,
clock signs, finite refinements, four-word equalities, basins and own-control limits
agree with the released raw results. No correction is requested.

The manuscript's interval-digit construction was independently checked at this stage.
Its intervals I_n=[1−1/(n+1),1−1/(n+2)) form a disjoint partition
of [0,1), each with length pi(n). Successive residual affine coordinates
give a Borel digit map. Every specified finite prefix has an interval
preimage of its product length, whose residual coordinate ranges over all
[0,1). For any Borel tail set E, its preimage under that
residual digit map therefore has exactly W(alpha)*mu(E) measure.
This establishes the full tail law, not just cylinder notation. Cylinder
generation gives the stated product probability. No assertion that every individual
word has a chosen real representative is needed or used.

The manuscript's common-prefix refinement argument correctly extends the branch IMAGE
to arbitrary finite histories and branch pairs. It does not sum overlapping
images as if disjoint. Its clock descends on all null words because
the same frozen pointwise version is used throughout.

The reported ND additions match the raw singleton and shifted-gcd proofs;
their complete-basin scope is correct. The ONE control's two time groups
are separately stated, and its u example retains eventual isotropy without
calling u periodic. The manuscript neither replaces full basins by ordinary
shift-tail classes nor calls the numerical relation log144=2log12 a repetition.
The unaccessed 317/318-line versions were not retrospectively audited.

## 7. Checkpoint 3: strongest adverse checks and disposition

The main counterargument is that the tested cycles and all their finite
ancestor basins are null for mu. That does not remove them from
the frozen full-point owner: every word was retained, and the cylinder-constant
version was fixed before return tests. The report does not claim that
a.e. density alone canonically selects all null values or that pi is
the unique natural arithmetic measure. Changing weights or the pointwise convention
would change the candidate, not repair the current result.

A second concern is confusing equal time with packet identity. The full
isotropy images and disjoint deterministic core basins rule out that confusion:
main's log144 packet is primitive in its own class, whereas a second
turn of e2 is a repetition only inside e2's different class.
The ONE control supplies the opposite situation: u genuinely enters e2's
class, so its incoming log30 step creates no new primitive.

A third concern is changing the source through an inverse description.
Main/FEEDBACK-OFF/ONE may insert freely chosen actual batch words under their
own rules; NO-DELETION must use target-visible batch letters. Its finite/zero
predecessor counts, cancellation of batch weights, singleton fixed basins and global
zero-time potential all depend on that distinction. None is transferred to main.

The owner is arithmetically linked by actual division and quotient-dependent reading,
but this does not prove natural A0 or prime-selective time. The failure
is explicit composite primitive recurrence, not absence of source dynamics. It
does not prove a no-go for all symbolic measures or batch architectures.
Untested main/ONE/ND source periods and global prime coverage remain open.

Final finding: no blocking or nonblocking manuscript correction is needed.
The exact final status and STOP / FORK are supported; the same-object
ledger remains intact. T3 is NOT SUPPLIED / NOT PURSUED, classical
A0/A1/A2 are NOT APPLICABLE, formal Route is UNASSIGNED and B is
NOT INVOKED. No smooth/Hausdorff-circle, invariant-volume, trace/operator, RH or
Hilbert–Polya result follows. This freezes the bounded review and ends further work.
