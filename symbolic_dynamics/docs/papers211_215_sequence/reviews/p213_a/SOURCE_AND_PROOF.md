# P213 A first substantive proof and source audit

2026-09-11. Status: PROOF_SOURCE_REVIEWED / VERIFIER_SOURCE_READY;
not complete manuscript PASS. Reviewer /root/p213_manuscript_review_a is
process-separated from both listed author-side contributors. No candidate
implementation was read or reused. No external or cross-model review.

## Inputs and limits

Reviewed the physical frozen_round0 manuscript TeX, complete PROOF_PACKAGE,
all documentary payloads and entire 451-line author verify.py as source.
All 25 physical payload hashes passed sha256sum --strict -c SHA256SUMS
(actual command33eef9, exit0). Freeze manifest hash is
0273621904180a32c1ce93da0befab6c4107b96fb4703ac9cf71d2a139160fe3.
INPUT_PINS.sha256 binds the whole freeze, including its manifest, plus the
specific internal primary proofs and root acceptance receipts used here.

The 1623893-byte,18485-line author canonical was whole-byte hashed and its
header and final records inspected; this is not a claim of independently
reprocessing every scientific record. The author pair's root DATA receipt
is read and used at its stated scope, not replayed. FREEZE_SCOPE supersedes
only historical pending lifecycle wording. The accepted confirmation02
receipt is read: run01's missing texfonts.map prepin remains historical;
run02 closes initial scope prospectively, not terminal scope.

The prior overbroad hash command encountered the sections directory and
exited1 after producing the regular-file hashes; no PASS is attributed to
that command. The earlier complete strict check succeeded. Large combined
text reads truncated; the omitted mathematical/source and documentary
sections were subsequently retrieved separately. Recovery indexes were read
narrowly for current state, not as proof. No scientific source was executed,
imported, compiled or AST-parsed and no build was launched by A.

## C1: temporal attack and independent reasoning

The literal uses simultaneous old-state currents. Translation works because
the same added baseline appears in both adjacent currents and cancels. A
residual zero has zero inflow and outflow, hence the residual minimum really
stays zero; merely nondecreasing minimum would not suffice for C3.

Inside a positive run every site except its head retains positive incoming
mass. Thus deletion cannot occur at two adjacent sites in the same round,
nor can an interior hole split the run. The original endpoint has permanently
zero successor and cannot be deleted even when it becomes the sole site.
Before that event its immediate predecessor is still positive, so its mass
increases by an integer at least one each round. The bound M-b counts exactly
nonfixed transitions, not visits including the terminal state. Independent
zero-separated intervals retain their original masses, proving both the
terminal formula and global maximum-of-run-clocks rule. Recurrent=fixed
follows after finite-time fixation; the argument is not circular.

n=1 has one cancelling current; n=2 has two equal currents, so the identity
and fixed classification agree even at unequal positive masses after minimum
subtraction. n=3 admits at most two consecutive positive residual sites.
For masses A,B the receiver obeys B'=min(2B,A+B), giving the least t with
2^t B>=A+B and the witness (N-1,1,0). Nonzero baselines only reduce residual
mass, so the full-carrier upper bound still uses N. N=1 needs no logarithm
exception beyond log2(1)=0. For n>=4 the witness (N-2,1,1,0,...) gives
(N-2-t,1,1+t) until t=N-2 and then fixes in one further step. This includes
N=3 correctly; N=2's two-site witness and N=0,1 are separately valid.
No closed pointwise clock for general n>=4 is proved or claimed.

## C2: all-parameter atlas attack

Re-derived the four local equations directly: valley a_i; ascent interior
a_(i-1); descent interior 2a_i-a_(i+1); peak a_i+a_(i-1)-a_(i+1).
The tie-to-1 convention is necessary for disjointness; all-one forces uniform
and all-zero contradicts a strict cyclic order. On a mixed word, each valley
is forced by its target, and descending interiors are recursively forced
backward with denominator two. Odd numerators and equality on a strict
descent must reject. Negative descent is a harmless unreachable defensive
test for nonnegative targets, not positive branch-coverage evidence.

When r=1, valley and prepeak coincide and there is no free interval. When
d=1, the next coordinate is already the next valley; no descent interior
exists. When r=2, y_(v+1)=y_v remains essential even though the order chain
is vacuous. For longer ascents the shifts force every coordinate except the
prepeak/peak pair, with sum S=y_p+A_(p+1). The inequalities are precisely
t>=y_(p-1), 2t<=S and t<=y_p-1. The last '-1' is an integer decrement,
not a subscript; replacing it by y_(p-1) would be false. Empty intervals
have zero weight. Prepeak=peak ties are allowed and belong to exactly one
word. Cyclic blocks form disjoint coordinate roles even when wrapping the
label-zero cut; choosing a starting valley is not a rotational quotient.

Sufficiency checks every local equation before invoking telescoping. Therefore
sum(a)=sum(y) is a consequence and not an omitted feasibility constraint.
For every positive word weight any independent selection fills all coordinates
nonnegatively with exactly its declared comparisons. Distinct selections
differ at a prepeak; distinct words differ in the source's unique comparisons.
This establishes both full-set equality and all multiplicities for arbitrary
n,N, not only the finite box. The O(n2^n) count concerns arithmetic operations
on forced values and interval lengths, not printing each predecessor or
bit-complexity uniform in N. Source code enumeration is correctly not used
as the complexity implementation.

Independent verifier uses current complementarity instead of implementing
these same blocks. For each candidate current c, a=y+c-shift(c); min-current
is equivalent to two nonnegative slacks with zero product. This alternative
finite inverse has a unique current for every source. Its finite bounded
enumeration attacks full inverse sets; the deductive paragraph above is
the actual all-parameter atlas audit. No numerical result is yet claimed.

## C3: fixed-target exclusion and sharp degree

Invariant minimum is needed to pass to residual sources. Uniform target
forces every source coordinate at least m with sum nm, hence source=target.
A residual source run loses at most one head in a single update, so an
isolated-spike output requires source runs of length at most two, all ending
at output spikes. There cannot be an unobserved positive source run: its
endpoint persists. A target-positive coordinate must already be source-positive.
Consequently the previous target spike really does block disappearance of
an optional head in a gap of one zero. For a gap of at least two zeros,
0<=h<=floor(p/2) gives all possibilities; nonzero heads cannot overlap or
erase the necessary separator. The product includes the sole-spike gap n-1,
empty product and zero-target boundary without hidden factors.

Each interval needs a one-run with at least two edges and its following
nonempty zero-run, so the associated disjoint edge blocks cost at least three.
There are at most floor(n/3) intervals. Using the already-proved source
bijection, any permitted free coordinate is <=N; hence no interval exceeds
N+1 values. This is a legitimate dependency, not a circular upper bound.
For n>=3 let k=floor(n/3)>=1. Choose k spikes three labels apart; the cyclic
last gap is also >=2 zeros because n>=3k. N>=2k ensures q=floor(N/(2k))>=1.
The mass remainder does not destroy positivity or separation, and each
factor is >=q+1>=N/(2k). Thus the exponent is sharp with stated constants.
No exact finite-N maximum or full maximizer classification follows. The
n=6 example at q=0 is uniform and independently gives one source, as stated.

## Primary bibliography audit (actual 2026-09-11 access)

All three BibTeX records match primary metadata. These are narrow citation
checks, not global novelty searches or whole-source mathematical reviews.

- Boccara/Fuks: [publisher record](https://journals.sagepub.com/doi/10.3233/FUN-2002-521-302)
  was returned by primary-domain search with title, authors, Fundamenta
  Informaticae52(1-3),1-13,September2002 and DOI. Initial abstract URL open
  succeeded, but later range/find requests returned Internal Error; those
  failures are not publisher full-body access. [Author arXiv record](https://arxiv.org/abs/adap-org/9905004)
  dates versions1999/2000. [Author PDF](https://arxiv.org/pdf/adap-org/9905004)
  pp1-4, especially Theorem2.1 and proof, establishes the finite-alphabet
  number-conservation characterization used only as background. Its template
  header2024 is not publication metadata. No priority for conservation.
- Nishinari/Takahashi: [author-institution metadata](https://waseda.elsevierpure.com/en/publications/analytical-properties-of-ultradiscrete-burgers-equation-and-rule-/)
  supplies title/authors, J.Phys.A31(24),5439-5450,1998 and DOI with BibTeX.
  [Author PDF](https://hakotama.jp/laboratory/works/public/98nt.pdf), first six
  pages including equations16/21, gives current min(M,sender,L-receiver) and
  its unbounded-current specialization. The displayed2001 front date is not
  a1998 metadata contradiction. This audit does not transfer Cole-Hopf results.
- Fukuda/Segawa/Watanabe: [author-institution metadata](https://shibaura.elsevierpure.com/en/publications/generalized-discrete-and-ultradiscrete-burgers-equations-derived-/)
  confirms the published title, JDEA29(1),84-101,2023 and DOI. The [v2 preprint](https://arxiv.org/html/2104.14009v2)
  has a different title. Equations15-17 explicitly contain receiver vacancy
  and a second evolving variable; only this examined formulation is compared.
  No published full-body access, published equation numbering or equality of
  every version is asserted. Citation scope in the manuscript is accurate.

## Internal subtraction

Read the complete original UUC PROOF_PACKAGE and MNA_PROOF at the pinned
workspace paths. UUC has binary uphill current, energy convergence and an
implicit current-word inverse. Its conservation, permanent zeros and generic
flux reconstruction earn no new credit here. P213 instead transfers the
minimum mass, including along descending positive edges; its endpoint and
sharp-clock conclusions are not UUC's generic quadratic potential bound.
MNA sums increasing positive composition runs and deletes parts; its triangle
mass clock and refinement threshold act on changing-length ordered blocks.
It is not this fixed-length labelled cyclic map. Generic run decomposition,
chamber elimination, products and packing are fully deducted. These literal
distinctions do not prove absence of all factors, conjugacies or encodings.
The retained value is the narrow conjunction, not global novelty or venue fit.

## Finding census and remaining gates

Current examined proof/source findings: Critical0, Major0, Minor0. This is
not zero-open terminal acceptance: independent execution/canonical/strict
pair, complete final review artifacts, exact delta and later rounds/builds
remain unperformed obligations. A has made no live edit and accepts no delta
yet. Historical run01 provenance limitation stays explicitly retained.
OWNER_AMBER / HOLD_EXTERNAL.
