# Synchronous sink reversal: source-only owner subtraction

Disposition: **KNOWN_FAMILY_SOURCE_DESK / NO_NEW_LITERAL / ZERO_PILOTS /
NO_ADMISSION / HOLD_EXTERNAL**. This is a source desk for the parent's one
existing last-seat lane, not another candidate slate or a mathematical review.

## Result

The exact acyclic all-sinks update is explicitly an old object, scheduling by
edge reversal (SER). The acquired primary research preprint supports the
following subtraction, with important proof-reading limits:

- Yeh, *A Dynamic View of Circular Colorings*, arXiv:math/0604226v1 (2006),
  p. 11: fixed connected undirected simple graph; acyclic orientation; sinks
  have zero outdegree; each step reverses every edge incident to the current
  sinks. This is the synchronous orientation sequence, not a chosen single
  sink or a topology-changing routing rule.
- Sections 1--3 give the marked-graph framework. A good marking has one token
  per oppositely directed arc-pair and positive token count on every directed
  cycle. At each positive integer pulse every fireable vertex fires together.
  Lemma 5 states the eventual period/multiplicity ratio
  `p/m = max_C |C|_c/|C|_T`; its printed proof is read.
- Theorem 6 minimizes that ratio over good markings. The literal SER
  specialization is Corollary 7 (p. 12): `chi_c(G) = min_omega p_omega/m_omega`.
  The text credits Barbosa--Gafni [5] for equal sink counts per vertex within
  a period, and [5,21] for the specialization.
- This owns the temporal **rate mechanism**, not an asserted closed formula
  for the least period itself, every transient length, or every basin. No
  inverse/fibre theorem was found in the actually consumed sections. All-source
  reversal is **not** asserted to invert the all-sinks map.

Primary source: [Yeh preprint](https://arxiv.org/abs/math/0604226).
Local acquired [PDF](r3_yeh_2006.pdf) and [layout text](r3_yeh_2006.txt).

Do not extend these inspected results to arbitrary cyclic orientations,
disconnected graphs, isolated-vertex boundary conventions, or inverse counts.
No source-derived proof or new adapter was authored here. Internal collisions
and any new theorem contract remain the parent's responsibility.

## Three-route acquisition ledger (closed)

| Route | Primary target and actual endpoint | Native result | Body-read status |
|---|---|---|---|
| R1 | Barbosa--Gafni, *Concurrency in heavily loaded neighborhood-constrained systems*, TOPLAS 11(4):562--584 (1989); `https://dl.acm.org/doi/pdf/10.1145/69558.69560` | curl exit 22, HTTP 403; headers and complete stderr preserved | No acquired body; attribution comes from the inspected Yeh bibliography/text, not a read of the 1989 proof |
| R2 | Yeh--Zhu, *Resource-sharing system scheduling and circular chromatic number*, TCS 332:447--460 (2005); `https://www.sciencedirect.com/science/article/pii/S0304397504007923/pdf` | curl exit 22, HTTP 403; headers and complete stderr preserved | Publisher search abstract only; no acquired body/proof |
| R3 | Yeh, *A Dynamic View of Circular Colorings* (2006); `https://arxiv.org/pdf/math/0604226` | curl exit 0; actual PDF is 236,143 bytes, 23 pages | Selected full Sections 1--3 and beginning of Section 4, plus references, as detailed below |

The preliminary publisher web opens also returned `Internal Error`; neither
those nor search snippets count as acquired proof. R3 is an author-deposited
preprint, not represented as a peer-reviewed journal edition. No fourth route
or retry endpoint was used.

## Exact reading boundary

`r3_read_1_630` records `sed -n 1,630p r3_yeh_2006.txt` in full (35,914 output
bytes). The combined tool display initially elided a small part of Theorem 4;
the separate `r3_read_280_410` captured and displayed the entire affected
Theorem 4 proof (7,303 bytes). Thus Sections 1--3 (printed pp. 1--11), Corollary
7 and Section 4 introduction (p. 12), and only the start of Theorem 8 on p. 13
were inspected; **not** all 23 pages. Theorem 8's proof is not claimed read.
`r3_read_references` reads text lines 1070--1145 (3,427 bytes), covering the
reference section on printed pp. 22--23 and a preceding figure caption.

Within the inspected body:

- Theorem 1's two-direction proof is printed and read.
- Reiter's Theorem 2 is stated and attributed; its original proof is not
  printed here and was not acquired. The theorem's hypotheses include a
  vertex reaching all others and positive token count on each directed cycle.
- Theorem 3 is identified as Mohar's result and deduced from Theorems 1--2;
  Mohar's original circulation proof was not acquired.
- Theorem 4's full printed proof is read, but is not needed for this SER
  owner subtraction.
- Lemma 5's full printed proof is read. It relies on Theorem 2, cites prior
  multiplicity facts, and states a greedy-vs-admissible induction claim without
  supplying that induction. No missing induction or original dependency proof
  was supplied or silently treated as read by this desk.
- Theorem 6 and Corollary 7 are presented as consequences. The equal-count
  assertion is credited to earlier work; this paper does not reproduce its
  proof at that point.

`r3_text_locate` runs an explicitly recorded `rg -n` across the entire acquired
text; later theorem-name/word matches are navigation only, not proof reads.
No theorem beyond the selected body is used to claim a general inverse result.

## Evidence and limitations

[SCOPE.md](SCOPE.md) records instructions, bootstrap/navigation bounds and
initial exact discovery strings. [QUERY_LEDGER.md](QUERY_LEDGER.md) supplies
the remaining exact web requests and records which raw web responses are
persisted. Each `commands/<label>/` contains exact native `argv`, cwd,
before/after explicit input pins, executable/recorder pin, complete stdout and
stderr byte files and true child exit in `receipt.json`. The outer recorder
normally exits 0 even when curl exits 22; **child** status is the evidence.

The first `read_failures` capture omitted its explicit `--input` options; that
original is retained. `read_failures_pinned` is a separate fresh identical
native read with all four consumed error/header files pinned. Control-file pins
were taken after bootstrap reads, and are labelled accordingly; they are not
a claim of historical pre-read pinning. Source-PDF/text reads have their own
before/after explicit pins. Raw command outputs may be displayed by ordinary
read-only shell calls without recursively recording copies of those displays.

The final local checksum seal establishes artifact bytes only. It is not an
independent mathematical review, full dependency audit, pilot, numerical
canonical, candidate gate, manuscript acceptance or root adoption. No protected
science/review/build bodies, central writes or external messages were used.
