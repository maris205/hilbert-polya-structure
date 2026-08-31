# Deterministic compile report

- Engine: LuaLaTeX.
- Frozen environment: `SOURCE_DATE_EPOCH=1788048000`.
- Each of rounds 0, 1, and 2 was built twice in separate fresh temporary directories, with two LuaLaTeX passes per build.
- Both fresh outputs for every round were byte-identical.
- Settled second-pass logs contain no LaTeX/package warning, undefined-reference request, overfull box, or underfull box.
- Final PDF: 2 pages; all listed fonts are embedded and subset.
- Visual inspection: both final pages are legible, uncropped, and free of collisions; the reference remains inside the text area.
- `paper/main.pdf` is byte-identical to `paper/main_round2.pdf`.

Archived SHA-256 values:

```text
round 0  9a0a03dff8c93f0e1e6a17cf40795f6132f2ebc5601d96dca74bd80e00b0dc4f
round 1  21252916e5cc1074b2f4eb2ac55c4c171dd2f54f251febeb19a1a758a616756b
round 2  d3d604ea273a27c1286463b23e07ab7bda78895fd5d998a281800343a2aefc3a
final    d3d604ea273a27c1286463b23e07ab7bda78895fd5d998a281800343a2aefc3a
```

Canonical final command, repeated twice in each fresh directory:

```text
SOURCE_DATE_EPOCH=1788048000 lualatex -interaction=nonstopmode -halt-on-error -jobname=main "\def\CRevisionRound{2}\input{/absolute/package/path/paper/main.tex}"
```
