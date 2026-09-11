# MNC gate actual execution and input receipt

2026-09-06 UTC. Candidate evidence, not a manuscript or batch terminal gate.

## Independent producer and canonical

From this directory the actual initial command was

```sh
python3 -B verify.py > CANONICAL.json 2> canonical.stderr
```

The process was observed to finish with exit 0. It emitted the full
24,635-byte canonical, **293,461 assertions**, internal record digest
`5a531261ccbbc98336dfd99c6e740cd70db781763599878993eb7ea0724414b0`.
`canonical.stderr` is empty. No failed mathematical producer or patched
test failure occurred in this gate. Author verifier and canonical content
were not read or imported to produce these independent records.

Scientific hashes:

- `verify.py`: `1b37b3f17846bfda0b714d1379257efd24077989fc02007a20eb03f4629d21b6`
- `CANONICAL.json`: `2443974a2021d24d02b0fd5c16aca292706f5ec6fed838281403fd3d52e86602`
- `INPUT_PINS.sha256`: `455aafef11feaf81ad98ee8a5e1db49e54dc3fc7bbe52a61a355e64d553678e0`

## Two additional actual processes and raw comparisons

The new command `python3 -B replay.py reviewer_pair_01` completed with
exit 0. It ran from 06:26:02.650010 to 06:26:09.072340 UTC using
`/root/miniconda3/bin/python3`, Python 3.12.3, and recorded settings
`PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, `LC_ALL=C`, `TZ=UTC`.
The producer has no runtime input files or nonstandard imports. The
harness reads files only to pin inputs and collect complete child outputs;
it does not import or alter the producer.

| Run | Child command | Child exit | Actual raw comparator | Comparator exit |
|---|---|---|---|---|
| 1 | `/root/miniconda3/bin/python3 -B verify.py` | 0 | `cmp CANONICAL.json reviewer_pair_01/run1.stdout.json` | 0 |
| 2 | `/root/miniconda3/bin/python3 -B verify.py` | 0 | `cmp CANONICAL.json reviewer_pair_01/run2.stdout.json` | 0 |

Both outputs contain all 293,461 assertions and have the canonical hash
above. Both are 24,635 bytes. Child stderr and both comparator streams
for each run are empty. This was byte comparison, not normalized text or
a comparison of hashes alone. The original streams and machine-readable
observations are in [reviewer_pair_01/receipt.json](reviewer_pair_01/receipt.json).
The three producer/canonical/pin-list hashes and all 17 reviewed context
pins were unchanged before/after that pair.

## Coverage and proof status

The full cyclic range is unchanged at $3\le n\le9$, totaling 29,511
source states and as many labeled targets. The checker independently
peels the full directed functional graph, rather than assuming a height
bound; reconstructs every source set by local constraint propagation for
$n\le7$; counts every target by remembered-overlap DP and separately by
the distance-word formula; checks every singleton mask; and tests the
entire colored tail class in those boxes. All nine-symbol ternary and
seven-symbol binary local identity windows are also checked.

At lengths 10–64, only two constant-target scalar counts, scalar
inequalities, and one explicit witness per length are tested. These are
not a larger full-state pilot. Finite testing is counterexample pressure;
all-$n$ conclusions are supported by the fully read deductive proof and
the audit's explicit adapters.

## Source/manifest verification

`sha256sum -c MANIFEST.sha256` in the closed author directory passed all
25 entries before and after review. Its manifest hash stayed
`f0274a66983e8b811deea94a5ab0cf4186cb3451477f5ef7e9f1cdd7086eec38`.
The author package's nine workspace-root-relative input pins also passed.
The gate's main 17 pins and supplementary three pins passed from the
workspace root; supplementary entries cover the read-only intake and
the exact structural-preflight script/helper, not extra runtime producer
dependencies. The supplementary tool paths are absolute by design.

Three actual structural-preflight commands used the installed
`pdf_read_preflight.py` on the pinned `Fuks2003.pdf`, `Jen1989.pdf`, and
`JerasDobnikar.pdf`, with package-local output sidecars. Each command
exited zero but returned verdict `UNAVAILABLE`, with the explicit warning
`pypdf-not-installed: preflight cannot parse the document`. Those original
sidecars remain preserved; there was no dependency installation or fake
PASS. `pdftotext -layout` produced the three archived full extracts with
exit zero. The missing equation (2.1) was rendered by `pdftoppm` and
actually viewed. This does not certify PDF structure or all-page reading.

The final gate manifest is directory-relative and nonself, covers all
reports, pins, checker/harness, canonical, raw pair streams and source
retrieval records, and is checked with exact path-set closure. No build
or manuscript review is claimed because this is an unnumbered rejected
candidate. No author or historical evidence was modified.
