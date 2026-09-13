# Paper27 reviewed layout-copy build

Status: AUTHOR_STOP_PENDING_SOURCE_AND_CONTROL_REVIEWS

This is bounded compilation correction 2/3, justified by actual first-build overfull and metadata failures. It is not a replay of the failed attempt. The complete acceptance contract and no-external-effect boundary of LOCAL_BUILD_20260905_PLAN.md remain in force; its failed root and script are immutable.

Source identity:

- Main: `paper-layout-20260905/main.tex`, SHA256 `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`.
- Notation: original `paper/math_commands.tex`, SHA256 `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957`.
- Bibliography: original `paper/references.bib`, SHA256 `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5`.
- Preserved original main hash is independently rechecked by every new pre/post binding: `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e`.

Script: `notes/LOCAL_LAYOUT_BUILD_20260905.py`, SHA256 `a38c05bb7d33e3800ea4ea2aff8d5836a135e5c1ebdfd0d7749c3cd140dad9d5`.
It is a mechanical derivative of the dual-reviewed first-attempt script. Only new filenames/root names, the new main-source hash, explicit main-source selection and original-main preservation check change. All executable publication commands, pre/post checks, snapshots, acceptance predicates, failure handling and determinism logic remain unchanged.

Exact new paths, none touched before review consumption:

- `build/layout-20260905-evidence`
- `build/layout-20260905-r0`
- `build/layout-20260905-r1`

There is no alternate suffix, old-root access, cleanup, source mutation during build, retry in either root, or fifth publication pass. A failed execution remains failure; success still requires both roots and independent actual-output review.

Before execution:

1. Independent typesetting/source-equivalence review binds both original and layout-copy hashes and verifies mathematical tokens, numeric rows, references, captions and table structure preserved. It must explicitly identify the metadata-only directive and does not assert runtime fit.
2. Independent code-delta review binds the new script hash and verifies that the change is only the source/path rebind described above, plus original-source preservation. The previous dual review is evidence for unchanged code, not a fictitious review of new bytes.
3. Pure regression suite and read-only preflight must pass. Main records consumption of both review decisions in `LOCAL_LAYOUT_BUILD_20260905_REVIEW.md`; only then may `--build` run once.

After execution, verify actual page count, overfull zero, metadata, full content/reference suffix, remaining warnings, glyphs/fonts/layout, exact two-root determinism and integrity before any release-grade claim. Existing source/publication locks remain unchanged historical artifacts; this new source binding and its independent equivalence review form the explicit layout-only supplement, not a silent rehash of those locks.
