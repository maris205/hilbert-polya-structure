# Fresh08 shift entrance: bounded source and proof check

Date: 2026-09-09 UTC. Status: **ONE_NEWLY_SPECIFIED_LITERAL / NO_NOMINATION**.
This is a source-contributor report, not an independent candidate gate,
manuscript review, priority certificate, or global absence claim.

Only this directory is owned by the present contributor. No historical file,
central index, paper, verifier, Git state, runtime setting, or external manuscript
was changed. There were no scientific runs, pilots, cutoff expansions, or
additional schedules. The parent owns the separate finite-field Lyness entrance.

## 1. Exact question, assumptions and carrier

Fix integers $n\geq1$ and $0\leq k\leq n$. The complete carrier is
$X_{n,k}=2^{\binom{[n]}k}$, the set of all families of $k$-subsets of $[n]$.
There is no intersection restriction. Every family-size sector is invariant.

For $1\leq i<j\leq n$, the elementary shift $C_{ij}$ replaces
$A\in\mathcal F$ by $A-j+i$ exactly when $j\in A$, $i\notin A$, and
$A-j+i\notin\mathcal F$; otherwise it retains $A$.
All replacements for this single pair are simultaneous.
Let $p_1,\ldots,p_N$ be the pairs in lexicographic order, explicitly
$(1,2),(1,3),\ldots,(1,n),(2,3),\ldots,(n-1,n)$, where $N=\binom n2$.
The autonomous update in this entrance is
$$S=C_{p_N}\circ\cdots\circ C_{p_1}.$$
For $n=1$ the empty product is the identity.

This report has specified this literal sweep. No exact internal original for
that sweep was established in the bounded search below, so it is **one newly
specified literal attempt**, not a zero-literal desk. That accounting does not
claim the map or any theorem to be new to mathematics.

## 2. Proof status and dependency map

The following deductions are **PROVABLE AS STATED**:

1. The local Boolean pair rule, its complete local image and local inverse.
2. Strict potential decrease at every nontrivial local shift.
3. The fixed and recurrent families of $S$ are exactly the shifted families.
4. A generic, nonsharp upper bound for the number of nonfixed sweeps.
5. The explicit example disproving a product of local fibre sizes as a
   formula for the full-sweep fibre.

Items 1–2 depend only on the literal rule. Items 3–4 depend on the potential
and on every pair being included in each sweep. Item 5 is a direct deduction
inside the same carrier, not a separate system or computer experiment.

A sharp all-parameter lex-sweep clock, the assertion $S^2=S$, and an
independently evaluated full-sweep target-fibre theorem are
**NOT CURRENTLY JUSTIFIED by this report**. No assertion that several
sweeps are necessary has been made.

## 3. Local pair proof

Fix $i<j$. For each
$B\in\binom{[n]\setminus\{i,j\}}{k-1}$, use the pair of coordinates
$$x_B=\mathbf1_{\{B\cup\{i\}\in\mathcal F\}},\qquad
  y_B=\mathbf1_{\{B\cup\{j\}\in\mathcal F\}}.$$
Different $B$ give disjoint coordinate pairs. Sets containing both $i,j$,
or neither, are untouched. On each pair,
$$00\mapsto00,\quad10\mapsto10,\quad01\mapsto10,\quad11\mapsto11,$$
equivalently $(x_B,y_B)\mapsto(x_B\vee y_B,x_B\wedge y_B)$.
This preserves the family size and ranks, and proves totality.

Consequently a target $\mathcal G$ lies in the image of $C_{ij}$ exactly
when it has no pair $01$, equivalently $C_{ij}\mathcal G=\mathcal G$.
Let $s_{ij}(\mathcal G)$ count its pairs $10$. Then
$$|C_{ij}^{-1}(\mathcal G)|=
\begin{cases}
2^{s_{ij}(\mathcal G)},&C_{ij}\mathcal G=\mathcal G,\\
0,&\text{otherwise}.
\end{cases}$$
Indeed $00$ and $11$ have unique sources; each $10$ has sources $10,01$;
the untouched coordinates are forced. These choices are independent for
this one pair of labels, and remain in the same family-size sector.
For $k=0$ or $k=n$ there are no such coordinate pairs and the map is identity.

The displayed definition in Frankl–Kupavskii's §3.2 is exactly this local
family shift, with $u=i,v=j$; the OR/AND and inverse statements here are
elementary deductions from that sourced definition, not claimed new source
theorems or a separate valued mechanism.

## 4. Complete recurrent deduction, generic temporal bound

Put $m=|\mathcal F|$ and
$$\Phi(\mathcal F)=\sum_{A\in\mathcal F}\sum_{a\in A}a.$$
If $r$ pairs $01$ are changed in a local $C_{ij}$, then
$$\Phi(C_{ij}\mathcal F)=\Phi(\mathcal F)-(j-i)r.$$
There are no other changes. Thus every nonidentity local shift strictly
decreases this integer potential.

If $S\mathcal F=\mathcal F$, the potential is equal before and after
the full sweep. Every intermediate decrease is nonnegative, so every one
must be zero. Hence every intermediate state equals $\mathcal F$ and
$C_{ij}\mathcal F=\mathcal F$ for all $i<j$. Conversely these local fixed
conditions imply $S\mathcal F=\mathcal F$. This is exactly shiftedness:
membership is closed under replacing a present larger label by an absent
smaller one.

If $S^r\mathcal F=\mathcal F$ for any $r\geq1$, summing the same decreases
over all $r$ sweeps gives zero, so the first sweep already fixes the state.
There are therefore no strict cycles. Every orbit eventually reaches a
shifted family because the carrier is finite and the potential decreases
on each nonfixed sweep.

For fixed family size $m$,
$$m\,\frac{k(k+1)}2\leq\Phi(\mathcal F)
 \leq m\,\frac{k(2n-k+1)}2.$$
Each nonfixed sweep lowers $\Phi$ by at least one. Writing $\tau(\mathcal F)$
for its first entry into the fixed set, this proves
$$\tau(\mathcal F)\leq
 \Phi(\mathcal F)-m\,\frac{k(k+1)}2
 \leq mk(n-k).$$
The empty family and $k=0,n$ satisfy the bound with entrance time zero.

This proof is the generic compression-potential mechanism. The modern
primary source explicitly owns shifting to shifted families and
preservation of set/family size, but its read passages do not state this
exact fixed-order temporal bound or the exact lex-sweep clock. The loose
bound does not certify a new temporal contribution. In particular, this
report neither proves nor refutes single-sweep stabilization.

## 5. The local inverse is not a full-sweep inverse

Different $C_{ij}$ pair different occupancy coordinates. Their inverse
choices must pass all intermediate image constraints in reverse order.
It is not valid to multiply their local fibre sizes at the final target.

Here is an exact illustration within $X_{3,1}$ and the specified
$C_{12},C_{13},C_{23}$ order. For the target
$\mathcal G=\{\{1\}\}$, family size preservation permits only
$\{\{1\}\},\{\{2\}\},\{\{3\}\}$ as sources. Each maps to $\mathcal G$:
the second source moves at $C_{12}$, the third at $C_{13}$, and the first
does not move. Thus
$$|S^{-1}(\mathcal G)|=3.$$
At that same final target the three elementary fibre sizes are $2,2,1$,
whose product is $4$. This is a hand-derived boundary counterexample to
the multiplication shortcut, not a pilot.

One can always write a sum over admissible intermediate families, or
reverse the local rule recursively. No such generic path sum is treated
here as an evaluated full-sweep fibre law, an extremal classification,
or an independent second axis.

## 6. Primary sources actually read

**Decisive primary research source.** Peter Frankl and Andrey Kupavskii,
*Simple Juntas for Shifted Families*, Discrete Analysis 2020:14, 18 pp.,
published 2020-09-03; DOI 10.19086/da.14507.
[Author manuscript / publisher-form PDF](https://arxiv.org/pdf/1901.03816v3)
and [primary HTML](https://arxiv.org/html/1901.03816v3).

Read scope: the PDF title/byline/publication/DOI at extracted lines 0–60;
the complete introductory paragraph defining shifted families and preserving
ranks/cardinality at PDF lines 163–177 (also HTML lines 67–70);
and **all of §3.2**, HTML lines 285–296, including the set shift, family
shift, Proposition 16 and its proof. The latter proposition is about juntas,
not about this fixed lex schedule; its theorem is not imported.
No claim that the entire 18-page paper was read or audited is made.
The HTML headline displays only Kupavskii, whereas the embedded journal
metadata and PDF byline explicitly contain both authors; the PDF controls
the attribution. The DOI fetch returned an error, preserved below, so DOI
resolution success is not claimed.

**Foundational lead, not decisive body evidence.** Peter Frankl,
*The Shifting Technique in Extremal Set Theory*, 1987.
[Author-hosted PDF](https://www.renyi.hu/~pfrankl/1987-4.pdf).
Search returned the first-page introduction; PDF opening returned 27 pages
but zero extracted lines. Screenshot requests returned only text references
through this tool interface, no image content was received/viewed.
Thus this report does **not** claim to have read its compression definition,
termination proof, or an exact-schedule theorem. The source remains a
documented lead, not a substitute for the actual modern body read.

Other failed primary openings (EJC shifted-family paper, Katona-hosted text,
and AMS EKR link) and noisy searches remain in RECORDS.json. They do not
support mathematical ownership claims. Nonprimary search hits, including
lecture notes mentioning that an order can avoid repeating pairs, were
navigation only and supply no exact-lex theorem here.
The bounded result is one inspected primary research source for the
actual local rule plus direct proofs; it is not two independent-source
confirmation of the exact sweep.

## 7. Actual internal search and deductions

The archived narrow text search used
Kruskal–Katona / combinatorial shift / ij compression / shifted family /
shifting technique in Markdown and TeX under papers and docs, with explicit
snapshot, originals, evidence, QA, review, source-capsule, cold-build,
frozen and round exclusions. It returned the P107–P111 candidate ledger.
A separate main.tex search for comparator / odd-even / bubble-sort /
sorting-network / left-compression / left-shift located P182 and P189.
These are lexical searches with an explicit limited surface, not a
complete repository scan or no-collision certificate.

The relevant actual originals were then read:

- P182 main.tex lines 55–150: the old map is
  $(a,b,c)\mapsto(c,a\wedge b,a\vee b)$ on lattice triples, with its stated
  four-iterate theorem. This is not the present carrier/sweep. Only the
  already-classical meet/join comparator primitive is subtracted; no
  unproved conjugacy or imported global P182 theorem is claimed.
- P186 main.tex lines 38–245: support iteration
  $\{a_j\}\mapsto\operatorname{supp}\{a_j-j\}$, the full displayed gap law
  proof and inverse-slot proof. Its carrier and update are different;
  rank compression/gap erosion does not establish an exact collision here.
- P189 main.tex lines 40–148: binary row compression followed by transpose,
  its height-calculus proof and four-iterate normal form. This is not
  simultaneous set-family label compression; no exact equality is claimed.
- P107–P111 candidate ledger, matching row and twelve-line context:
  lower-shadow descent and odd-even comparator entries are old disposition
  metadata only. No underlying proof was substituted by these rows.
- The complete earlier finite-compression/recoding HANDOFF was read as
  navigation and to check its zero-nominated scope. Its claim not to
  exhaust all compressions is preserved. P186/P189 were separately opened.

The exact lex sweep was not located in that bounded surface. This is not
clearance to promote it: the actual sourced local operation and standard
potential already consume the available elementary package, while the
exact-time and full-sweep inverse residuals remain missing.

## 8. Decision, authorship and evidence limits

**NO_NOMINATION / NO_PROMOTION.** The valid negative result is not that
every possible theorem on this map is already known. It is that this
bounded desk obtained only a standard compression recurrence mechanism
and a local Boolean inverse, with no sufficiently separate, evaluated
full-sweep inverse/temporal conjunction. Neither an unread source nor
a lexical non-hit repairs that gap.

The present same-model agent independently contributed the comparisons
and proofs in §§3–5 and is therefore a proof contributor, not eligible
to independently review a manuscript that adopts those deductions.
The parent supplied the entrance and fixed schedule, and later explicitly
warned against assuming multiple passes or a global 0-Hecke action.
No 0-Hecke claim, replacement adjacent schedule, or commutation theorem
is asserted or used here.

The project symbolic-dynamics skill governed scope; research-lit,
proof-writer and the ARS source-verification route governed citation,
proof-status and read-scope discipline. Zotero/Obsidian tools were absent;
ordinary browsing was used, with optional bibliographic clients and
external-model calls off. No external-review certificate is claimed.

RECORDS.json contains actual provider request/return strings and native
local read/search/hash results from the decisive bounded work. It does
not purport to include all instruction reads or the initial noisy discovery
call; no conclusion needs an omitted return. Saved screenshot returns are
text references, not retained image bytes. INPUT_PINS.json records five
whole-file hashes, but manuscript reading was only in the stated ranges.
The no-hit search surfaces are not whole-file pinned corpora.

POSTWRITE_CHECK.json preserves the initial wrong-working-directory check
failure and corrected actual metadata read; the first pin-note line count
was corrected from 173 to the observed 166 before freezing.
SHA256SUMS is the complete directory-relative nonself manifest over the
four payload files. There is no scientific verifier, independent gate,
build, or manuscript in this subtree. Source inspection and documentation
do not change batch counts or authorize any external action.
