# P214 Review B build01 HOLD and build02 exact recipe delta

2026-09-11 UTC. `BUILD01_HOLD_PRESERVED / BUILD02_SOURCE_ONLY`.

The consumed build01 controller exited 1. All four TeX/BibTeX passes, four
diagnostic commands and seven page renders had supervised exit 0. The sole
controller failure was the final `science.after` check: the recipe remained
in `reviews/p214_b/build01/source_only`, while all seven manifest paths are
workspace-relative. The preserved `science.after.stderr` has exactly seven
not-found messages plus the strict summary warning. The matching
`science.before` check from the workspace root passed.

Build01 remains HOLD. Its partial tree, seven renders, consumed grant and all
failure evidence are unchanged. They provide no accepted artifact or page-view
credit and are not retried, cleaned, resumed or relabelled PASS.

The complete machine-checkable unified diff is preserved separately as
`BUILD_RECIPE.diff`. Its four changed line pairs are:

```diff
--- p214_b_build_preparation01/BUILD_REQUEST.sh
+++ p214_b_build_preparation02/BUILD_REQUEST.sh
@@
-P214_PREP='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p214_b_build_preparation01'
+P214_PREP='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p214_b_build_preparation02'
@@
-P214_OUT='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/reviews/p214_b/build01'
+P214_OUT='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/reviews/p214_b/build02'
@@
-sha256sum -c --strict "$P214_OUT/SCIENCE_AND_HISTORY_INPUTS.sha256" > "$P214_OUT/science.before.stdout" 2> "$P214_OUT/science.before.stderr"
+(cd /root/autodl-tmp/symbolic_dynamics && sha256sum -c --strict "$P214_OUT/SCIENCE_AND_HISTORY_INPUTS.sha256") > "$P214_OUT/science.before.stdout" 2> "$P214_OUT/science.before.stderr"
@@
-sha256sum -c --strict "$P214_OUT/SCIENCE_AND_HISTORY_INPUTS.sha256" > "$P214_OUT/science.after.stdout" 2> "$P214_OUT/science.after.stderr"
+(cd /root/autodl-tmp/symbolic_dynamics && sha256sum -c --strict "$P214_OUT/SCIENCE_AND_HISTORY_INPUTS.sha256") > "$P214_OUT/science.after.stdout" 2> "$P214_OUT/science.after.stderr"
```

There are no other recipe changes. A labeled `diff -u` reproduces
`BUILD_RECIPE.diff` byte for byte. The two science checks are now symmetric
and explicitly execute from the workspace root. This note is not a grant or
an execution record. `OWNER_AMBER / HOLD_EXTERNAL`.
