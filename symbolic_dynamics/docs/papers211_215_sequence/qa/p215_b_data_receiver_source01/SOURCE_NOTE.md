# P215 Review B independent initial DATA receiver source

2026-09-11 UTC. `SOURCE ONLY / PROCEDURAL HOLD`.

`RECEIVE_INITIAL.cjs` was written without reading any initial scientific
capture bytes. It is
hard-bound to corrected preparation `p215_b_execution_preparation02` and the
future `p215_b_initial_run01` tree. The strict wire parser uses the verifier's
actual V1 field spelling `maxfibre`; it rejects the obsolete planned spelling
`max_fibre`.

The receiver does not import, invoke or read `reviews/p215_b/verify.cjs` at
runtime. It binds that file through both captured before/after `sha256sum`
records, cross-manifest digest agreement and the runtime binding. All other
preparation, runtime, package and 43 scientific pins are checked against
current regular non-symlink files. It also requires the exact 27-member
capture, zero child/controller exits, empty stderr, raw-identical pre/post
logs, exact check-log contents and the three-member output digest manifest.

Independently for all 30 carriers, it constructs all 5,704 literal states and
transition/predecessor arrays. It obtains the recurrent set and first-entry
depths by indegree peeling and reverse dynamic programming, and compares each
depth with the compressed-sign clock. Every fibre is reconstructed by dynamic
programming over prefixes of admissible nondecreasing record heights, checked
by literal transition, and counted separately with the manuscript recurrence.
Image, height, maximum fibre, unique maximizer and closed forms are checked.
The emitted verifier assertion count is retained only as a positive observed
wire field; it is not credited as a receiver-derived hidden-check count.

The only source-stage execution permitted is syntax checking and
`--self-test`, whose fixtures are malformed framing/spelling strings and carry
no scientific output. A successful later run writes `INITIAL_NATIVE.json`
with exclusive creation. Its result is initial DATA only, not canonical,
strict replay, delta, verdict, build, Round2 or completion. `HOLD_EXTERNAL`.

Exact later command, only after the capture exists and root separately grants
DATA reception:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC \
  /usr/bin/node /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p215_b_data_receiver_source01/RECEIVE_INITIAL.cjs \
  --receive-initial
```

However, this directory is on procedural HOLD because the source author used
a broad historical-receiver discovery command that traversed `qa` to depth
two. It returned no P215 B capture member or scientific output, but the
traversal could query future-directory entry metadata. See
`SOURCE_STAGE_FAILURE01.md`. This source must not receive execution credit
unless root explicitly resolves that contract failure; a clean replacement
source from a process that never made that query is the conservative remedy.
