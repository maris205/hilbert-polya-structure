# Primary-body comparison after the bounded pilots

2026-09-06 UTC. This supplements, and does not overwrite, the initial
abstract-only source record copied into both pilot capsules.

## Actual retrieval and reading

1. Onus, Richa and Scheideler, *Linearization: Locally Self-Stabilizing
   Sorting in Graphs*, ALENEX 2007. The author's
   [publication page](https://www.cs.bilkent.edu.tr/~onus/arastirma.html)
   contains an image hyperlink missed by the web text extraction. Its HTML
   lines 832–890 were read with `curl`/`sed`; the link is the
   [author-hosted PDF](https://www.cs.bilkent.edu.tr/~onus/yayinlar/linearization-ALENEX07.pdf).
   Web opening of that PDF failed, but actual `curl -L --max-time 30 --fail
   --show-error --output ... URL` returned 0 and downloaded 720015 bytes.
   The preserved PDF and `pdftotext -layout` output are in `public_sources/`.
   Actual text reads: lines 1–460 and the last 95 lines. This covers the
   complete §2 algorithm, lower/upper convergence proofs and other PL
   properties; §3 and the start of §4; conclusions and references. No claim
   to have read the complete experimental section is made.
2. Cramer and Fuhrmann, *Self-Stabilizing Ring Networks on Connected
   Graphs*, Technical Report 2005-5, January 31, 2005. Discovered as PL's
   reference [5]. [Institutional record](https://publikationen.bibliothek.kit.edu/1000003169)
   and [institutional full text](https://publikationen.bibliothek.kit.edu/1000003169/2846).
   Actual `curl` download returned 0; preserved PDF and layout text are
   `public_sources/isprp_correctness_2005.{pdf,txt}`. Read lines 1–390,
   covering the problem, complete protocol description, state/correctness
   definitions and the entire §5.1 Theorem 1 proof, plus §5.2 opening.
   The full flooding and self-stabilization proofs in §§5.2–5.3 were not
   read and are not used as the comparison premise.

The byte size above is verified in the sealed file inventory; download
chronology is reported from actual successful terminal calls, not a claim
that pre-download source hashes existed. Both original failed browser
retrievals remain recorded in `SOURCE_AND_HISTORY.md` and tool history.

## Exact PL subtraction

PL acts on connected undirected graphs. Each synchronous round separately
linearizes smaller neighbours and then larger neighbours, with additions
winning conflicts against deletions. Algorithm 1 and Theorems 2.1–2.2
establish sorted-list stabilization in the sharp worst-case `n−2` rounds
(for the meaningful nonsmall cases). Its descending-label degree induction
is not FTH's recurrent-height proof.

FTH acts on directed functions, including loops; it threads all incoming
sources together regardless of their side relative to the target. It
retains every permutation, including nonsorted cycles, and admits labelled
nontrivial periods. Thus neither literal identification nor transfer of
PL's all-state stabilization theorem is possible. The local star-to-chain
primitive and path-substitution connectivity argument remain classical
owner credit, not new contributions. Memory/shortcut variants retain extra
state and are not the stated FTH carrier.

## Exact ISPRP subtraction

ISPRP uses a circular address order, locally stored route/neighbour data,
messages, and protocol interactions. In its §5.1 proof, every pointer
change from `a→c` to `a→b` has `b` strictly inside the clockwise interval
from `a` to `c`; the sum of interval cardinalities strictly decreases.
Its local endpoint has exactly one predecessor per node.

On labels `0<1<2`, FTH has the loop-free two-cycle

`(1,2,1) → (2,2,1) → (1,2,1)`.

In the first step, vertex 0 changes its target from 1 to 2. The clockwise
interval starting immediately after 0 grows from `{1}` to `{1,2}`.
This transition is forbidden by the cited ISPRP interaction rule; it is
not an asynchronous ordering or simultaneous batching of allowed ISPRP
updates. Rooted at 0, that source already has its correct closest successor.
Both FTH states also have a branch and are not ISPRP's local endpoint.

These comparisons rule out the specified owners' literal dynamics and
direct clock adapters, not every conceivable encoding, unpublished result
or modified protocol. No global novelty claim, independent source gate,
candidate ID, public release or external manuscript communication follows.

## Contribution and remaining gate

The final historical replay searched 4,244 selected manuscript/desk files
across the workspace and both documented mirror layouts; complete raw
queries/results and before/after content pins are in `evidence_capture_02/`.
The initial attempt completed both comparators but failed before launching
`rg` at an incorrect absolute path; it is preserved in `evidence_capture/`.
Results are bounded discovery, with duplicate copies and irrelevant binary
filename matches retained, not a full-file-read or novelty certificate.

Two additional actual originals were read after those discovery hits:

- `papers/167-minimum-inverse-position-feedback/main.tex`, lines 45–235:
  full literal and main theorem, complete first-image/component proof, and
  only the opening of the sharp-clock proof. MIP chooses the minimum
  preimage of each target, defaulting to itself. Its recurrent periods
  divide two and its fixed states are involutions. FTH fixes all
  permutations and has a tail feeding a three-cycle on four labels, of
  exact whole-function period three. The maps are not conjugate at that
  same size; the path/cycle primitive is still old background.
- `docs/papers162_166_sequence/scouting/degree_feedback_jump/SCOUT.md`,
  lines 1–110: literal, universal monotone data, embedded power family and
  fixed-locus proof, with only the opening of the fibre section. DFJ and
  other forward-power/pointer-jump maps send each coordinate along its old
  forward orbit. For `f=(2,2,2)`, FTH sends coordinate 0 to 1, outside
  its old forward orbit `{0,2}`. This rules out the literal forward-jump
  mechanism, not arbitrary factors or a blanket originality assertion.

These two root-relative originals have their own
`HISTORICAL_SUPPLEMENT.sha256`; the earlier fifteen originals are in
`HISTORICAL_INPUTS.sha256`. Neither file is a directory-relative manuscript
manifest. No historical scientific implementation was imported or rerun.

The claimed residual is exactly Theorems 1–3 of `FTH_PROOF_PACKAGE.md`:
the all-target recurrent carrier and labelled period, a nonredundant
increasing-path-cover inverse, and the unique sharp fibre maximizer.
There is no all-size `n−1` entrance-clock theorem in this package.
Root and scout are contributors and cannot independently review it.
