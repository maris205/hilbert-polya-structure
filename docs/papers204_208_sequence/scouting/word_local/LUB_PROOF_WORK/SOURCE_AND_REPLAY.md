# LUB sources, replay and closure

2026-09-05 UTC. NO_PROMOTION. This package is author proof/scouting work,
not an independent candidate gate or manuscript review. The exact
deductions are in [PROOF_AND_DISPOSITION.md](PROOF_AND_DISPOSITION.md).

## Primary sources and exact adapter boundary

| Source | Actual reading | Use and limitation |
|---|---|---|
| Philippe Salembier, Albert Oliveras and Luis Garrido, Antiextensive Connected Operators for Image and Sequence Processing, IEEE Transactions on Image Processing 7(4), 1998, 555–570; DOI 10.1109/83.663500. [Author-hosted primary PDF](https://imatge.upc.edu/web/sites/default/files/pub/aSalembier98.pdf). | Actual first three printed pages, especially §II-C's recursive local-background/component construction; additionally §IV-A on printed p. 562 defining the descendant-inclusive pixel area. Not all 16 pages. Web PDF rereads timed out and the repository alternate returned 403; the author PDF was then successfully streamed through curl and pdftotext, with no local PDF created. | LUB evaluates the existing max-tree node area at each vertex's own node. The node atom may be disconnected, as the source explicitly allows for a local background. This is not a claim that LUB equals an area opening: an opening thresholds/removes nodes, while LUB feeds their areas back. The complete inverse adapter is proved here, not falsely quoted from the filtering paper. |
| David Wright and Wenhua Zhao, D-log and formal flow for analytic isomorphisms of n-space, Transactions of the AMS 355(8), 2003, 3117–3141. [Primary preprint](https://arxiv.org/pdf/math/0209274), [institutional publication record](https://openscholarship.wustl.edu/math_facpubs/3/). | Preprint opening context plus §4.2's recursive polynomial algorithm and §4.3, Theorem 4.5 and its full proof, printed preprint pp. 27–29. Not all 32 preprint pages or unrelated formal-flow proofs. Journal metadata confirmed by the institutional record and authors' publication pages; the preprint is dated September 2002. | The ancestry root is the unique minimum and strict maps to a finite chain are counted by the strict order polynomial. Theorem 4.5's proof gives the child-product finite-difference recursion. LUB's recovered target tree and alphabet n substitute directly, with no unexplained scale, extra independent variable or unknown tree sum. |

The static component-area primitive and the full strict-tree-height inverse
therefore receive zero separate contribution credit. The source record
does not establish that the literal autonomous feedback has been studied
before. That stronger ownership assertion is unnecessary for this
NO_PROMOTION: the proposed second axis is wholly transferred, while a
complete residual two-axis contract was not proved.

The optional image census in the proof is an elementary rooted-gap
decomposition. Its generating series is the shifted central-Delannoy
series, not a recurrent-state generating series. Neither the count nor
the combinatorial name is presented as a new mechanism.

## Internal collision scope

Local literal searches covered super/sublevel component size, local upper
basin, component trees, subtree spans, Cartesian trees and nearest-smaller
encodings in the current and earlier batches before external retrieval.
Root's actual component_pilot.py and complete COMPONENT_CANONICAL.jsonl
were read; the script imports the older word-local pilot.py for its
functional-graph census, so all three context files are pinned in
INPUTS.sha256. Our verifier imports none of them.

The current P204 rejection proof/source record, in
docs/papers204_208_sequence/reviews/p204_a/SOURCE_AND_PROOF.md, and
CRC3_GATE/SOURCE_AND_ADAPTERS.md were inspected at their old
nearest-smaller/Cartesian and full-adapter boundaries. A one-direction
nearest-smaller distance, a cyclic record depth and a two-sided component
area are not asserted equal. Their lesson here is formula-level
subtraction, not a blanket old-word-system conjugacy.

For LUB, with a nonminimal input letter, the exact static size is the sum
of its clockwise and counterclockwise strict-smaller stopping distances
minus one. A global minimum has size n. This strict treatment of ties is
essential; a weak tie-breaking binary Cartesian tree cannot simply
replace the multiway component tree. The recovered component family and
atom-height bijection in this package resolve that issue explicitly.

No Zotero/Obsidian connector or arxiv_fetch helper was available; direct
primary web/arXiv retrieval was the disclosed fallback. No external
manuscript upload, specialist contact or publication took place.

## Author verifier, scope and actual execution

Runtime inspection reported Python 3.12.3. All verifier runs used -B.

The self-contained verify_lub_adapter.py has two forward representations:
threshold-induced graph BFS and strict-smaller directional stops. For
every source in the unchanged n=1,...,6 boxes it checks equality of the
two updates, exact upper-to-lower component SUPPORTS, image membership,
L-idempotence and adjacent signs. For every image target it constructs
the decoded tree, counts strict height labels by the child recursion,
independently enumerates all height-labelled source words, and compares
the complete reconstructed source SET with direct forward enumeration.
This is stronger than matching only aggregate fibre counts.

It additionally computes complete finite forward graphs by direct orbit
walks, checks the sole fixed point, tests the image formula and preserves
both directional-monotonicity counterexamples. It does not assert an
all-parameter period bound, nor import a root/verifier/source library.

Exploratory execution:

    python -B docs/papers204_208_sequence/scouting/word_local/LUB_PROOF_WORK/verify_lub_adapter.py

Process 16979 completed with exit zero, empty displayed error output and
complete JSON stdout (terminal chunk 6c86c1). No scientific verifier
change followed that successful execution.

Two subsequent separate child executions were launched by this actual
wrapper, from /root/autodl-tmp/symbolic_dynamics:

    import subprocess, sys, hashlib, json
    p = "docs/papers204_208_sequence/scouting/word_local/LUB_PROOF_WORK/verify_lub_adapter.py"
    a = subprocess.run([sys.executable, "-B", p], capture_output=True)
    b = subprocess.run([sys.executable, "-B", p], capture_output=True)
    assert a.returncode == b.returncode == 0, (a.returncode,b.returncode,a.stderr,b.stderr)
    assert a.stderr == b.stderr == b""
    assert a.stdout == b.stdout
    print(json.dumps({
        "runs": 2, "returncodes": [a.returncode,b.returncode],
        "empty_stderr": True, "raw_equal": True, "bytes": len(a.stdout),
        "sha256": hashlib.sha256(a.stdout).hexdigest(),
        "stdout": a.stdout.decode()
    }, sort_keys=True))

Pair process 8316 completed with wrapper exit zero (launch chunk 4baa73,
completion a290a0). The actual receipt, excluding only the separately
archived full stdout field, was:

    {"bytes": 2334, "empty_stderr": true, "raw_equal": true,
     "returncodes": [0, 0], "runs": 2,
     "sha256": "5e65151795357b659938bb56d9022af3ba260c8f5f220a0d43e866885cef2452"}

The complete first child's stdout was decoded and saved using apply_patch
as CANONICAL.json. Its actual hash and 2,334-byte size were checked
after saving. No normalized comparison or third archival replay is
substituted for this raw pair.

Final verifier SHA256:

    6d9fe4ef44b055db811ce2d4f601ff90803c626f0784ecd44b08de271a9b800c

Actual output per child:

    status: STATIC_ADAPTER_VERIFIED_NO_PROMOTION
    assertions: 1258675
    sources: 50069
    image_targets: 2084
    full_parameter_temporal_claim: NOT_PROVED
    enumeration_sha256: 630f64615d00d15c68ef2fd0f29fbea1cd00f0ffae315969291467ef609f1e48

The complete canonical contains all six profiles and both explicit
counterexample orbits. The 2,084 exact target source-set comparisons span
all 50,069 sources, not selected easy fibres.

## Failed directions and preservation

An early inline diagnostic had a Python syntax typo in an assignment
(the token orw instead of or w), exited one before running any checks,
and wrote no file. The corrected diagnostic ran on n=1,...,6 only and
found counterexamples to both proposed coordinate inequalities between
F and F-cubed. Those failed mathematical directions are explicitly
preserved in the proof and final verifier. No later theorem quietly
assumes either inequality.

The primary max-tree web fetch failures and successful streamed
fallback are disclosed above; no full-paper read is claimed from failed
requests. No failed manuscript, review or historical source was changed.

## Final disposition

The complete static inverse adapter is proved, source-checked and
finite-pressure-tested. The all-parameter temporal conjecture is left
unproved. Per root's explicit stop direction, no additional temporal
search or cutoff growth is used to rescue an already-transferred
inverse axis. This closes LUB with NO_PROMOTION, not with a theorem
that longer cycles are impossible or that all future work is valueless.

Only LUB_PROOF_WORK was written for this task. Root's scripts, canonical
and central indexes remain untouched; no Git change is made by this
author. SHA256SUMS is directory-relative and covers every nonself
package file. INPUTS.sha256 is workspace-root-relative and records
read-only context, not imported executable dependencies.
