# Source and historical boundary: twenty-fifth scout

Date: 2026-09-07 UTC. This is bounded discovery and author deduction, not a
global novelty clearance or an independent gate. External release/contact
remain HOLD_EXTERNAL. No external manuscript upload or specialist contact
was made. Main agent alone contributed the MBO definition and proof.

## 1. Physical primary-owner evidence and honest read extent

Pascal Schweitzer, *An introduction to the Weisfeiler–Leman algorithm and
recent developments*, LOGALG, Vienna, 21 November 2025, author presentation:

https://www.ac.tuwien.ac.at/wp/wp-content/uploads/logalg25_schweitzer.pdf

The institutional PDF was physically retrieved by curl with exit 0; its
942,738 bytes have SHA-256
`61a2cabae89d2ac966792030b55e3757c8d6057b6f9f414c9f16b6efab0b62dc`.
pdftotext also returned 0. The main agent read local extracted lines 1–38
(title/date and start of next slide) and 1038–1078 (slide 32 in full, slide
33 in full, neighboring headings). The 1,865-line file was not read in full.
The slide drawings on generalized H-neighborhood rules were not inspected
visually and are not used.

Slide 32 defines iteration on the same vertices by existence of a common
neighbor. It also gives a diameter-based stabilization statement for finite
connected non-bipartite graphs other than odd cycles, credited to 2013.
We use the explicit owner definition as a collision boundary. The slide
does not supply the proof of that theorem, and we do not import it into
MBO. Slide 33 is only context, not a new candidate or a theorem dependency.

Identified research-paper owners, not full-paper reads:

- Martin Sonntag and Hanns-Martin Teichert, *Iterated neighborhood graphs*,
  Discussiones Mathematicae Graph Theory 32 (2012), 403–417,
  DOI 10.7151/dmgt.1610. Search exposed the exact common-neighbor definition
  and journal metadata. The physical attempt at
  https://bibliotekanauki.pl/articles/743216.pdf returned curl 22 / HTTP 403,
  saving a 178-byte error body (not a PDF), SHA-256
  `887c8ada6058f01125a5131f1c495ba5f0171b2c40466ea824494403b87c1a22`.
  The DOI landing attempt failed with curl 60 (certificate verification);
  no landing body was saved. A separate direct-publisher attempt at
  https://www.dmgt.uz.zgora.pl/publish/pdf.php?doi=1610 also failed with curl
  60 and no PDF body. This last URL was a transparently inferred publisher
  PDF pattern from a different indexed DMGT article, not a claimed followed
  link. Certificate checking was not disabled.
- Pascal Schweitzer, *Iterated open neighborhood graphs and generalizations*,
  Discrete Applied Mathematics 161 (2013), 1598–1609,
  DOI 10.1016/j.dam.2012.12.023. The publisher abstract was opened during
  discovery. The author homepage
  https://users.cecs.anu.edu.au/~pascal/ was opened and lists this work at
  lines 48–49; it did not provide an adjacent PDF link. DBLP search exposed
  an unpaywalled-version entry, but the physical record attempt at
  https://dblp.org/rec/journals/dam/Schweitzer13.html timed out with curl 28
  and no body. No unpaywalled target was actually resolved or read.

Browser attempts at Biblioteka Nauki, DOI/DMGT, DBLP, DML-PL, CiteSeerX and
the Lübeck publications page returned forbidden, unsafe-to-open, fetch
failure or timeout responses. These browser responses are not physical
downloads, and we do not pretend their complete payloads are in the lane.
The physical curl attempts have complete exact commands, explicit
environment, headers, stdout, stderr, exits and available bodies in
public_sources/ and public_sources_additional/. Both source recorders have
before/after hashes, as do their curl/pdftotext binaries.

Full research-paper source gate: HOLD / OWNER_PAPER_BODY_NOT_READ.
The author presentation is primary author evidence for the definition, not
a substitute for auditing the 2012 or 2013 proof. This gap does not make the
generic threshold conjugacy new, and does not block a negative disposition.
The proof package's exact identities are proved there from definitions and
do not depend on any unavailable paper theorem.

## 2. Public discovery scope

The main public searches covered cyclic cellular automata, finite-state
pulse-coupled/Greenberg–Hastings directions, weighted common-neighbor or
bottleneck transforms, and exact titles/DOIs of the neighborhood-iteration
owners. Relevant arXiv metadata actually opened during local-word scouting
were Lyu's 1407.1103 and Lyu–Sivakoff's 1706.08117; their bodies were not
read here and no theorem is imported. Those directions were not frozen as
additional candidate definitions. ResearchGate, a mathematical Q&A result,
DBLP and search snippets were discovery leads only, not proof authorities.
Irrelevant results returned by broad queries were not used.

The research-lit procedure was applied with a capability-aware fallback:
enabled-tool discovery found no Zotero/Obsidian methods, and the suggested
arxiv_fetch.py helper was absent in the searched skill locations (rg file
search returned no match). Ordinary web discovery and direct public-source
capture were used. No nonexistent service call is represented as completed.

## 3. Original historical reads, not recovery-summary substitution

Before task work the main agent read current SYMBOLIC_DYNAMICS_STATE.md,
the entire linked 740-line batch PIPELINE_STATE.md (including a reread of
490–540 after a small aggregate-output truncation), both current and
inherited problem anchors, WORKFLOW.md, HISTORY_AND_CAVEATS.md and the
complete project research skill. The research-lit and proof-writer skills
were read completely in this task's preparation.

Actual scientific historical-body reads used to avoid stale variants:

- papers/202-ternary-ordered-reset/main.tex, lines 1–120: exact ordered-reset
  rule, not a cyclic predator successor increment.
- papers/205-conflict-triggered-cyclic-increments/sections/01_setup.tex,
  complete file: equality-triggered increment, not successor-triggered CCA.
- docs/papers204_208_sequence/scouting/graph_relation_second/SCOUT_REPORT.md,
  complete 94 lines (the earlier requested read range extended past EOF):
  exact ECD, LRC, CCI and other old resource literals, plus their scope.
- docs/papers204_208_sequence/scouting/word_local/CPC_INTAKE.md, complete:
  integer count of predecessor-color neighbors, not ordinary CCA increment.
- docs/papers204_208_sequence/scouting/graph_relation/SCOUT_REPORT.md,
  lines 1–100: existing Boolean relation products and graph exclusions.
- docs/papers197_201_sequence/scouting/second_replacement_20260905/
  CONTRACTS_AND_PROOF.md, lines 1–155: D2G's exact nonadjacent
  distance-two condition and its empty-target proof, with neighboring
  ND1/CCW context. Not the entire file.
- papers/171-boolean-gram-dynamics/main.tex, lines 1–145: exact full
  Boolean-matrix map, loop production and stated temporal theorem. This
  read is sufficient for the literal-loop counterexample; the remainder
  of its temporal proof and full fibre proof were not reread here.

An earlier Boolean-Gram scout note was also read for orientation in the
preparation context; the pinned P171 original, not an unspecified scout
summary, is the operative loop-sensitive boundary. No older scientific
kernel was imported or executed.

## 4. Recorded searches and exact limitations

history_search.py was created before the first broad content search. Its
history_01/ receipt records 3 queries on 3,520 selected text files across
six documented root/mirror roots: local (266 output lines), metric (229)
and coupling (70), each query exit 0. Complete raw stdout/stderr, exact
commands, selected paths, per-file hashes, query exits and before/after
hashes are saved. All selected inputs and recorder/search tool were stable;
the explicit forbidden-filename audit was empty.

This is a selected corpus, not every file ever created. Duplicate mirrors
and incidental hits are retained, not counted as independent candidates
or publications. Terminal inspection of some raw output was truncated;
the saved raw output is complete, but we do not claim to have read every
matched document in full. Subsequent narrow rg searches and filename
discovery included old P171/P202/P205 build/review filenames without opening
their contents. No P208/P209/FTH/OFS scientific body or excluded kernel was
opened in this lane. All strict broad-content exclusions remain explicit
in the recorder. One guessed old SCOUT.md text query produced no matching
lines with exit 1; it was not treated as a full-history nonhit.

finish.py performs a new targeted read-only query capture against the same
selected filename list, archives the explicitly listed operative original
inputs as physical copies, writes root-relative original and copy hash
lists, and actually runs sha256sum -c on both. Its REPORT.json is the
authority for completion, exact counts and command exits. It checks overlap
with the first discovery's original hashes instead of silently refreshing
changed scientific inputs. Navigation-index copies are capture-time
snapshots; later root activity must not rewrite the old pins.

No source-only corpus, historical copy, preserved failure or source receipt
is presented as a science producer. Zero literal kernels, zero pilot boxes,
zero enumerated states, zero scientific producer executions, zero canonical
pairs, and zero scientific byte comparisons occurred. Source and archival
commands have their own honest execution receipts.
