# CRC3 source and exact-adapter audit

2026-09-05 UTC. Read-only source inspection; no external uploads or contact.
Search non-hits receive zero originality weight. The audit is bounded and
does not claim an exhaustive literature clearance.

## 1. External primary sources actually inspected

### Myers and Wilf: static record counts and templates

Amy N. Myers and Herbert S. Wilf, *Left-to-right maxima in words and multiset
permutations*, [arXiv:math/0701078](https://arxiv.org/abs/math/0701078),
primary [PDF](https://arxiv.org/pdf/math/0701078). The arXiv record dates
the preprint to 3 January 2007; the fetched PDF displays a different
internal title-page date, so no journal/year inference is made from it.
Actually read: definition, results in Sections 1–2, Theorem 3 and its
first-occurrence proof in Section 6, and word-template operators in
Section 7.2. Not a claim to have read all 17 pages.

Theorem 3 gives the single-scan count
`f(n,k,r)=sum_m binom(k,m) [m r] {n m}`. Section 6 reduces records to
the order of first appearances. Theorem 6 counts words with prescribed
record/nonrecord status at positions of ONE linear scan using generating
function operators. These statistics and counting tools are fully prior.
Neither inspected theorem states the joint vector of record counts at
every cyclic starting position, its iteration, or the present Psi formula.

**Adapter test performed here.** The words `123123` and `123213` have
the same multiset, same first-occurrence order, and same strict-record
position template for their displayed linear scans. Their cyclic outputs
are respectively `321321` and `321221`. Thus those old conditioning data
do not determine CRC3's joint target. Theorem 3 is a marginal sum of fibres,
not an every-target formula. This example rules out the direct substitution
of only those statistics; it does not prove that a more elaborate reduction
or another result in the literature is impossible.

### Berkman, Schieber and Vishkin: nearest-value primitive

Omer Berkman, Baruch Schieber and Uzi Vishkin, *Optimal doubly logarithmic
parallel algorithms based on finding all nearest smaller values*, Journal
of Algorithms 14(3) (1993), 344–370,
[DOI 10.1006/jagm.1993.1018](https://doi.org/10.1006/jagm.1993.1018).
Actually read: the [institutional primary record and abstract](https://cris.technion.ac.il/en/publications/optimal-doubly-logarithmic-parallel-algorithms-based-on-finding-a/),
which explicitly defines strict left/right nearest-smaller values and
gives its algorithmic scope. The full 27-page proof was not retrieved.
Order reversal gives the ordinary nearest-greater primitive; this receives
zero credit. The abstract is not evidence for a cyclic record-feedback
iteration theorem or a ternary fibre formula.

**Exact static encoding, reviewer deduction.** Starting at a position,
repeatedly jump to the first strictly greater letter to its right, at or
before the next global maximum. These visited values are exactly the scan's strict
records. Consequently the record count is one plus the depth in this
nearest-greater forest, with roots at global maxima. This exposes the old
pointer/depth primitive; it does not identify a full autonomous conjugacy
when the numerical depths are fed back as the next word. Repeated letters
must retain the strict comparison: weak Cartesian conventions cannot be
silently substituted.

## 2. Formula-level deductions

For any root-terminated run of length m with no target three, the accepted
source words are `2^a 1^(m-a)`, `0<=a<=m`; hence the factor is exactly
the classical count `binom(m+1,1)=m+1` of a binary weak chain. If a target
three occurs, the forced prefix leaves a terminal segment of length t
with `2^a 1^(t-a)`, `1<=a<=t`, giving t. Thus the arithmetic of every
factor and their product is elementary chain enumeration, fully deducted.

After the decoder removes target threes from the maximum problem, it is
literally the old integer-break optimization `max product s_j`,
`sum s_j=n`, not a new extremal engine. All its values and optimal part
lists are deducted. The only residual inverse work is proving that the
complete simultaneous CRC target imposes exactly these forced prefixes,
terminal choices, maximum-symbol branches, and labelled equality targets.
No new general counting method is claimed. No mere mention of chains or
Cartesian trees is promoted into an established full formula adapter.

## 3. Occupied internal mechanisms

Actual manuscripts were inspected rather than relying on batch summaries.
The relevant source pins are:

| Manuscript | SHA256 of main.tex |
|---|---|
| P117 odd-run reversal | `61e9d0ee7af6491a93e713dfa57707ec739609438ec8029d8115eb9e7a064053` |
| P176 first-frequency rotation | `ff1f7d45c7ac7146a06f737a7187a9cedd451591ab9cbffeccf2d35eadc5874a` |
| P202 ternary ordered reset | `bcb24151784b52a27d846dd564ab6a0b438381e617575e6064c698f69683fa1a` |
| P139 Lyndon-factor-start feedback | `97299a0a7b211a8434e3bf96612969d4cad8013796820181b2c723d3130e0af3` |

P117 flips bits in odd cyclic runs, leading to monotone boundary deletion
and parity-sensitive erosion clocks. Its cyclic compositions and run
bookkeeping are old for this batch. It does not supply CRC3's inverse
formula: the inspected manuscript has no every-target fibre theorem, and
its source parity/coalescence analysis does not force the CRC3 binary
maximum-rooted runs. Similar two-period syntax is insufficient for a
mechanism identification. Different carriers alone are not the deduction.

P176 preserves the source necklace and weight. Its exact inverse theorem
tests at most two whole-word rotations, `R^(-k)y` and `R^k y`, subject to
their first-bit conditions. All fibres have size at most two. CRC3 has
three sources even over its constant target and unbounded maximum fibres;
its source choices are not two frozen global permutations. This rules out
literal reuse of that inverse atlas and any full-carrier conjugacy, but is
not an assertion about every conceivable factor/embedding. Generic branch
splitting, rotations, and run lengths receive zero credit.

P202's exact decoder is `2^(number of cyclic 01 edges)` on its edge-21
avoidance language. Each choice affects one disjoint local site. CRC3's
D-language has a similar one-forbidden-edge syntax after relabelling,
plus a required minimum. That shared finite-type syntax is deducted.
Its fibres, however, include seven at n=5, so they are not that power-of-two
atlas under target relabelling. A single maximum-rooted CRC3 run can have
m+1 choices for arbitrary m, or t choices after its last target three;
these choices are coupled by order and not independent binary sites.
P202 also has no fixed state and has a constant three-cycle, whereas CRC3
has exactly one fixed state and no recurrent three-cycle. Hence the two
full-carrier ternary maps are not conjugate. No general absence of factors
is inferred from this obstruction.

P139 encodes Lyndon factor starts through suffix comparisons, not counts
of strict records in cyclic scans of raw letters. Its unique-attractor
erosion and ordered-Lyndon-chain inverse are not the present reflection
core or maximum-rooted binary source language. The common idea of
recomputing a static word encoding is fully prior and cannot count as an
axis. The manuscript's literal rule and relevant proofs were inspected;
no exact adapter transporting its theorem to CRC3 was established.

## 4. Search scope and unresolved owner risk

Local collision checks preceded web work. Online query families covered
cyclic record counts/profiles, records of cyclic shifts, iterated
left-to-right maxima, all-suffix record counts, record-profile inversion,
nearest-greater depths, Cartesian encodings, and visibility/skyscraper
terminology. The arXiv-specific search was also performed. Most literal
phrase queries returned irrelevant results; the useful primary record
literature is recorded above. Secondary snippets, code-interview pages,
and unrelated suffix-array results are not used as theorem evidence.

The unresolved risk is an exact circular record-profile or depth-feedback
owner, or a ready-made joint-profile formula that subsumes the decoder.
The present bounded inspection found no such result in the sections read;
it does not assign probability zero or clear priority. Accordingly the
candidate can be retained internally only with OWNER_AMBER and external
release held. The ordinary independent manuscript reviews remain open.
