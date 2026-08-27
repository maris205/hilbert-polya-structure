# Paper build

`main.tex` uses `\CRevisionRound` to preserve three substantive states:

- `0`: finite-time M\"obius, transition, moments and degeneracies;
- `1`: adds all three long-time regimes and their boundary clauses;
- `2`: adds validation, hostile controls, source lock and Route-A firewall.

Build a round in a clean temporary directory with LuaLaTeX twice, for example:

```bash
SOURCE_DATE_EPOCH=1787788800 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error \
  '\def\CRevisionRound{2}\input{main.tex}'
SOURCE_DATE_EPOCH=1787788800 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error \
  '\def\CRevisionRound{2}\input{main.tex}'
```

The final release is `main.pdf`, byte-identical to `main_round2.pdf`. No
figure was introduced because exact equations and the boundary table carry
the theorem more clearly than a diagram.
