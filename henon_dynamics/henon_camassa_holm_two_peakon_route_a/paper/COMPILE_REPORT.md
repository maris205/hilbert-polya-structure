# C278 compile report

- Engine: LuaLaTeX (LuaHBTeX, TeX Live 2022)
- `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`
- Fixed hexadecimal trailer ID: yes
- Passes per build: 2
- Fresh builds per revision: 2
- Fresh-build comparison: byte-identical for rounds 0, 1, and 2
- Final-pass warnings: none (no layout, citation, reference, destination,
  undefined-control, or rerun warnings)
- Fonts: all embedded and subset
- Text extraction: PASS
- Visual audit: every page of all three retained revisions inspected; no crop,
  overlap, broken glyph, malformed equation, or blank content page
- Final PDF pages: 3
- Post-release metadata rebuild: CH1993 now reads `Physical Review Letters
  71(11) (1993), 1661--1664`.  Because the bibliography is shared by every
  revision, rounds 0, 1, and 2 were each rebuilt twice in fresh directories.
- Final executable receipt after the metadata repair: 551 independent
  assertions, 10 SymPy identities, byte-identical replay, and 41/41
  repaired-hash attacks rejected.

| artifact | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `386fe10aff86527b4566678451d87cc4ae92541433408414f8f16870ebc6c62a` |
| `main_round1.pdf` | `18ea8214dc9f821093ac5cb156d3c3e32d8704ac0f8a26c36ec031b1cb1f63b4` |
| `main_round2.pdf` | `3aef1600dc97bb94cb50922ba7d135950ee9db37295a40268467a474b36faa67` |
| `main.pdf` | `3aef1600dc97bb94cb50922ba7d135950ee9db37295a40268467a474b36faa67` |

The archived rounds are selected with `\CRevisionRound=0,1`; the retained
source defaults to round 2.  Round 1 adds the full signed global atlas, and
round 2 adds collision continuation, boundary faces, the fail-closed nested
schema executable receipt, and Route-A/nonclaim closure.
