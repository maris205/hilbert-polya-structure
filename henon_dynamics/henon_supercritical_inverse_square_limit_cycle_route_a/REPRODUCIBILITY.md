# Reproducibility

Frozen baseline: `0c877206d202f732e21ea0b194f9c7fdf30467ee`; date 2026-09-05; epoch 1788566400; candidate HCS-C391; obstruction HEN-O375. Authority is `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

From this directory run `python -B code/c391_producer.py`, checker, sympy_crosscheck, replay, mutation, and `python -B -m unittest tests/test_c391_smoke.py`. The release command runs all lanes again. `--build-pdfs` builds all drafts twice in separate temporary directories, using two LuaLaTeX passes per directory and SOURCE_DATE_EPOCH=1788566400. It preserves actual settled normalized logs as paper/build_round0.txt through build_round2.txt. Then use release `--write` and release without arguments for closure.

The manifest excludes itself, includes every declared payload file and every actual settled log, and records main.pdf byte identity with round two. No package build requires changing the user's home, installing a new tool, a network service, external model or GPU.
