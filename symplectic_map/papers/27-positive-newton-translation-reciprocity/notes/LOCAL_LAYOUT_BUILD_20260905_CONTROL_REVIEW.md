# Layout-copy build: independent control-delta review

Reviewed SHA256: a38c05bb7d33e3800ea4ea2aff8d5836a135e5c1ebdfd0d7749c3cd140dad9d5
Decision: PASS

Date: 2026-09-05 (UTC)
Scope: bounded independent code/path/source-binding delta review against the
previously reviewed `LOCAL_BUILD_20260905.py`, SHA256
`49fba6fa53a6ecf7f4ebd23b2dca72db2a1079d83437088cf89b0c94e6936a9a`,
plus review of `LOCAL_LAYOUT_BUILD_20260905_PLAN.md`. This is the control review
for a separately identified layout-copy correction, not a retry of an existing
root, a source-equivalence decision, a mathematical review, or a statement that
the new layout actually fits. Prior runtime failures were supplied as context;
their build/evidence paths were not inspected by this reviewer.

## Delta verified

The complete textual diff contains only the changes described by the plan:

- Lines 21–22 select the exact new evidence path
  `build/layout-20260905-evidence` and equal-length root paths
  `build/layout-20260905-r0` and `build/layout-20260905-r1`.
- Line 24 replaces only the main-source hash with
  `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`.
  The notation and bibliography hashes are unchanged.
- Lines 210–211 select `paper-layout-20260905/main.tex` for the fixed main name
  and the original `paper` directory for the two other fixed source names.
  Both installation (line 545) and live pre/post binding (line 222) use this
  same selector, and root-copy equality remains required at lines 226–227.
- Lines 215–216 additionally check that original `paper/main.tex` retains
  mode 0644 and SHA256
  `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e`
  whenever `bindings` runs. This includes initial, per-command pre/post, and
  terminal checks through the unchanged call sites.
- Line 654 consumes the new hash-bound review filename, and line 662 freezes
  the new script under its new basename. It does not consume the old gate as
  if it reviewed these different bytes.

No executable publication argv, environment, timeout/cleanup behavior,
dependency/tool/PDF-parser binding, root universe, snapshot schedule, warning
policy, zero-overfull predicate, page/sentinel bounds, metadata/font/security/
text/citation acceptance, or exact cross-root comparison algorithm changed.
The prior known-header exception, single-dot recorder allowlist accommodation,
and reference-suffix safeguards remain intact. There is no added fifth pass,
root reuse, cleanup, source write, runtime filename fallback, or automatic
retry. The old script hash independently remains unchanged.

The plan correctly requires a separate independent source-equivalence PASS
before the main orchestrator records consumption of both decisions in
`LOCAL_LAYOUT_BUILD_20260905_REVIEW.md`. This control PASS alone does not
establish equivalence or replace that requirement. It also retains independent
actual-output review after runtime checks and preserves historical source/
publication locks rather than silently editing their identities.

## Independently executed safe checks

All Python invocations used `-I -B`; no publication command or `--build` was
run. No current, new, or previously failed build/evidence path was opened,
listed, or statted. No network operation or PDF write was performed. The sole
file written by this reviewer is this new report.

- Complete regression-file diff: only the selected script basename changes.
  Test-file SHA256:
  `abad2eb67ac2e5a15731452ee32ce1c52751956679c6437b91d5e133413897a4`.
- `LOCAL_LAYOUT_BUILD_20260905_TEST.py`: all 18 methods and their table-driven
  cases passed using in-memory/mocked fixtures.
- `LOCAL_LAYOUT_BUILD_20260905.py --self-test`: PASS, 2 positive and 11 negative
  cases.
- `LOCAL_LAYOUT_BUILD_20260905.py --preflight`: exit zero, binding the new main,
  original auxiliary sources, preserved original main, fixed tools, 87 logical/
  86 final dependencies, and PDF parser runtime hash
  `66cb425ff3a012c077f5ee1f8b8e7019f8f4d8c471635a2cfc98acdbb3ee6a2b`.
  Dependency-frame SHA256 remains
  `27f807a21bce6c72d09f189b200c1212d3629ef4550d9ad203740eef4a8fb726`.

No blocking defect was found in this bounded control delta. This PASS is bound
only to the exact new script hash above and does not reclassify any old failure,
assert successful pagination/metadata, or grant publication approval.
