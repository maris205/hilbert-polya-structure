# Test report

- Producer: PASS, 12,018 paths, 27 summaries and 24 moment rows.
- Producer-independent checker: PASS, all paths, moments and three
  environments reconstructed.
- SymPy: PASS, 37 symbolic/exact beta, moment, regrouping and stationary checks.
- Replay: PASS, two isolated directories, 4,813,459 identical bytes.
- Hostile mutation: PASS, 79/79 rejected, including rewrite and deletion of
  the nonempty-outgoing-row assumption.
- Optimized execution: all six scripts explicitly reject -O and -OO; the
  release gate exercises the five subordinate lanes.
- PDF revisions: 2/2/2 pages, fresh double builds byte-identical; final PDF has
  19 embedded and subset font rows.
- Settled warnings, layout boxes, undefined references, missing characters,
  extracted control bytes and drafting sentinels: zero.
- All forbidden flags and Route-B invocation: false.
