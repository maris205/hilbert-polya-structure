# Review A: proof and source attacks

2026-09-07. Reviewer `/root/p210_a_reviewer`; no P210 authorship or previous
candidate contribution. This report assesses the physical Round0 whose seal is
`e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26`.
Full frozen proof, all mathematical TeX, bibliography, source audit, claims,
plan, narrative and adoption were read. `INDEPENDENCE_ORDER.md` distinguishes
pre-commitment proof reads from later author code/canonical and candidate-source
familiarity. No candidate checker was read or imported. Candidate clearance and
root acceptance are not independent manuscript proof.

## Deductive assessment of the exact contract

**Literal map and time convention.** The state is an ordered positive integer
composition of N>=1, not a partition/multiset or a vector of reals. An update
keeps precisely the OLD strict-descent cuts. Each component mass is summed once;
new sums cannot trigger additional deletions within that round. With this rule,
the sample (3,2,1,1) takes three nonfixed updates. Defining tau as the first t
with F^(t+1)=F^t counts those updates, including zero for already fixed states.
Deleting cuts strictly lowers block count whenever a state is not a strict
descent; no longer recurrent cycle remains. These generic facts earn no credit.

**Lemma2.1: oriented left mass/right birth.** I attacked the implication that
the right block must specifically have been born in the preceding round.
At a cut removed at t>=2, take the rightmost parent a of the old left block A
and the leftmost parent c of the old right block B. Their inter-block cut
survived at t-1, so a>c. If B were unchanged, c=B and A>=a>B contradicts
the deletion condition A<=B. Thus B has at least two parents; its first
internal cut, whose left block is c, really was deleted at t-1. The induction
hypothesis concerns that cut, not a vaguely chosen genealogical ancestor.
It gives c>=t-1, and positivity/integrality give A>=a>=c+1>=t. The base
t=1 only needs positive mass. This argument does not assume every parent is
new and does not reuse one support mass in two disjoint contributions.

**Lemma2.2 and Theorem2.3.** For a block born at t, its first two OLD parents
are disjoint. Lemma2.1 gives at least t mass in the first and a birth at t-1
for the second. Applying the new-block induction only to the latter gives
t+M_(t-1)=1+t(t+1)/2; extra parents cannot lower the mass. A last nonfixed
round creates a block, so total N bounds that mass. The assertion remains
valid if several independent mergers happen simultaneously. N=1 is separately
fixed. For each integer h>=1 and r>=0 the claimed witness orbit has suffix
r+1+T_j and unchanged descending prefix h,...,j+1. Positivity gives
r+1+T_j>=j+1 for j>=1. Earlier OLD prefix comparisons remain strict
descents even when r is arbitrarily large. Hence only one prefix part joins
per round, and exactly h rounds occur. This establishes arbitrary surplus
deductively, not by the finite test of its28 in-box instances. Selecting
h=H(N), r=N-1-T_h proves the sharp maximum at every positive mass.

**Lemma3.1 and Theorem3.2.** Target cumulative masses specify unique input
cuts, so run refinements cannot be ambiguously segmented or overcounted.
Every internal segment is weakly increasing; every inter-segment boundary
is a strict descent. These conditions are necessary AND sufficient. For a
feasible right suffix its finite nonempty first-endpoint set has an attained
minimum r. An incoming refinement can attach exactly when its last part is
greater than r: attachment to a minimizer proves sufficiency, and every
other feasible first endpoint is >=r. No interval/convexity assumption is
needed. In fact the target(6) has attainable first endpoints {1,2,3,6}.
If incoming mass s<=r it cannot contain a sufficient last part. At s=r+1
only singleton(s) works; at s>=r+2, (1,s-1) attains1 and has a sufficient
last part. This proves all three branches and all failures; a larger right
first endpoint cannot rescue one. The base last part always has an all-one
refinement. The claimed O(m) bound counts integer comparisons, not fixed-cost
bit operations. Order sensitivity is genuine: (2,3,2) passes, (2,2,3) fails.

**Theorem4.1 and Corollary4.2.** An accepted scan uniquely splits into complete
increment/reset cycles and a terminal increment string. A cycle with threshold
k before reset has mass (T_k-1)+(k+2+u)=T_(k+1)+u. The initial rightmost
part b and terminal string jointly contribute (b-1)+T_k. These two identities
give weight preservation without counting objects. The inverse MUST reserve
the final triangular atom before grouping initial ones or reset followers.
The manuscript does so; T_1=1 at the final boundary is consequently unambiguous.
Every remaining triangular atom>=3 starts exactly one reset group; its maximal
following one-string records surplus. Reversal restores target orientation.
Both decompositions recover each other's groups, hence prove bijectivity and
surjectivity, not just a matching sequence. Nonempty output holds even for
N=1; the auxiliary i_0=1 is only a formal empty-list convention. The series
is well-defined coefficientwise by positive weights. Known triangular counting
and generic reset coding are deducted, not additional results.

**Proposition5.1: support only.** For equal endpoints a=b there is exactly
one all-a refinement iff a divides s. For a<b, reserve one smallest and one
largest part and freely choose all multiplicities between; the coefficient
of z^(s-a-b) in the coin product counts each weakly sorted refinement once.
Strict boundary coefficients point from the left LAST endpoint toward the
right FIRST endpoint. The product and suffix sum count every complete source
by the unique-segmentation lemma, including empty fibres. This correct formula
is ordinary partition/transfer bookkeeping and receives zero separate novelty.

The two retained obligations are distinct: a total-mass birth bound over
iterated dynamics does not decide an order-sensitive one-step target, while
the suffix feasibility grammar does not control delayed births. No maximal
fibre, closed pointwise clock, higher-iterate inverse, classification of all
deepest states, asymptotic or unrestricted conjugacy/priority claim is added.

## Actual primary-source and bibliography audit

All seven bibliography records are cited and their author/title/date/venue
metadata agree with the directly inspected primary records below. Fresh
browser returns are physically preserved in `sources/web01.actual.json`
through `web04.actual.json`:10 initial/open or follow-up-open operations plus
one publisher-PDF click, with2 genuine failed opens. These are complete tool
returns, not raw HTTP or downloaded entire PDFs. No new source search queries,
database crawl, external review API, upload or specialist contact occurred.

| Record and actual context | Deduction and read limit |
|---|---|
| [Wiseman A353847](https://oeis.org/A353847), fresh full142-line entry, example/code and May30,2022 author field | Equality-run sum and ordinary run-sum vocabulary are owned. This is not weak-order summation; the example on(1,2) distinguishes literals only, not novelty. |
| [Wiseman A375123](https://oeis.org/A375123), fresh full126-line entry, definition/code and Aug2,2024 author field | Weakly increasing run detection is owned; the map retains FIRST parts and need not conserve total. No claim to invent run detection survives. |
| [Wilson A023361](https://oeis.org/A023361), fresh full234-line entry, June14,1998 author, formulas and Arndt March25,2014 comment | Triangular-part compositions, recurrence, reciprocal series and reset/increment representations are known. Only their exact connection to this F-image is retained. |
| [Robbins2014](https://ac.inf.elte.hu/Vol_043_2014/239_43.pdf), fresh timeout; independently read full frozen199-line primary extraction in frozen `sources/archive/robbins_archived_primary.json` | Theorem1/proof printedp.240 and Theorem4(a) p.241 establish the allowed-part recurrence already. Author/title/journal43(2014),239–243 match. The extraction's table gives93 atN12, unlike recurrence94. This is not a fresh successful fetch, a typography check, or an audit of unrelated asymptotics. |
| [Gessel2019](https://ajc.maths.uq.edu.au/pdf/74/ajc_v74_p364.pdf), fresh restricted-URL failure; frozen successful primary body in `sources/archive/root_web02.actual.json` | Header74(2)(2019),364–370 and ribbon/run theorem on pp.365–366 directly read; the full358-line extraction was displayed and read, but no independent proof audit of later cyclotomic results is claimed. It tracks run LENGTHS, not a vector of individual run masses. Total letter-weight substitution loses the latter. |
| [Zhuang2016](https://arxiv.org/abs/1505.02308), fresh metadata and [PDF](https://arxiv.org/pdf/1505.02308) selected body | Published metadata JCTA142,147–176(2016) checked; PDF front date2021 is not substituted for publication year. Positive-word/ribbon definitions, Theorem1, network definition and Theorem2/matrix proof through printedp.7 read. No all26-page audit. A supplied run network and general transfer do not themselves establish the attained-minimum reduction. |
| [Gessel–Zhuang2019 publisher](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2019/6.html) and [PDF](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2019/6.pdf), fresh successful metadata/body | SLC82B Article6,12pages(2019) checked; introduction/ribbons/run theorem and homomorphism applications pp.1–7 read. General lifts/transfer are prior infrastructure. Later shuffle-compatibility results were not independently audited. |

The strongest external adaptation attempt is to specialize ribbon letters to
mass weights, keep separators/endpoints, and obtain every fibre by a transfer.
That succeeds as generic inverse bookkeeping and is fully deducted. It does
not supply the extra sufficiency argument collapsing endpoint sets to a single
attained minimum or the delayed right-birth/left-mass induction. A network
encoding the already-proved threshold grammar is not another contribution.
None of these limited observations excludes an unknown full adapter.

## Internal proof-mechanism subtraction

Frozen original comparisons, not only author/source summaries, were read:
P147 entire main.tex; P121 literal/genealogy passage original lines65–145;
CRG complete section171–198; FPT C08 row and surrounding ledger; PDCF section
270–287. Their exact origins are frozen `FROZEN_LINK_MAP.json`; archived
relative links must not be resolved from their deeper physical copy paths.

| Internal object | Actual subtraction and residual limit |
|---|---|
| P147 equality-run consolidation | Deduct same carrier/coarsening, previous-new-parent genealogy, and boundary-transfer inverse. Equality forces doubling; it does not force MNA's oriented integral left contribution. Its sharp same-mass bound is2 atN7 versus MNA3. This refutes only a same-total clock-preserving conjugacy, not arbitrary adapters. |
| CRG gcd-linked component sum | Deduct the complete positive-composition sum-coarsening carrier, adaptive old-neighbor tests and coupled refinement segmentation. MNA remains within this occupied family. CRG's archived length bound is not the sharp triangular clock. |
| P121 random xy+1 pair coalescence | Deduct coalescence/genealogy language. Its one-pair random rule, changing mass and Yule/BST law do not specialize to this autonomous conserved-sum update. No unrelated moment result is audited anew. |
| FPT leftmost unit transfer | Deduct sequential local transfers, potential bookkeeping and local inverses. Its fixed-length priority rule is not simultaneous cut removal. |
| PDCF prefix-divisibility cut filter | Deduct monotone-cut clocks and target-local path DP. The literal uses absolute prefix divisibility, not the adjacent weak-order comparison needed in the two retained arguments. |

After my own proof/code commitment I also read the frozen candidate
SOURCE_AND_PROOF report. This is disclosed post-commitment familiarity,
not a second manuscript review and not the basis for claiming an independent
checker. No source/claim was copied from its scientific implementation.

## Verdict boundary

The narrow all-size deductions survive these attacks, and no complete adapter
was established in the named inspected contexts. The residual value is modest
and specific: an oriented triangular clock plus a full position-sensitive
image-class identification. This meets the frozen internal two-axis ceiling,
not a journal recommendation or global priority certificate. Source failures,
extracted-table discrepancy and bounded read limits remain visible.
OWNER_AMBER / HOLD_EXTERNAL remain unchanged.
