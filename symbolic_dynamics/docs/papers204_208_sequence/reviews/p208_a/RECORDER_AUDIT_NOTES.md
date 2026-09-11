# Recorder completeness audit

The producer's code-only mathematical tests are independent of documentation
and use no external proof data. All inputs are frozen and each comparison is
raw `/usr/bin/cmp`. The initial runtime failure and v1 auxiliary-scope issue
are separately preserved, not suppressed.

After cold03/cold04 and build01, A audited the recorders themselves. The
Python/cmp/ldd binaries were in their pre-run inventories, but the math
recorder's after-check only covered consumed Python modules and resolved
shared libraries, not those fixed executable files. `/bin/bash`, the ldd
script interpreter, was also not explicitly pinned. Those numerical runs
are real successful runs, but are not the final dependency-complete pair.
The revised recorder explicitly pins and rechecks those fixed executables,
including Bash. Only cold05/cold06 are the final controlled pair. Build02
likewise adds Bash and all renderer/comparator dynamic-link probes. Build01
and its genuine all-page view are retained; Build02 requires its own actual
page views. These are reviewer evidence corrections, not manuscript defects.

Scope limitation: OS kernel and process service are not captured as a
historical hermetic machine image. Concrete consumed source/configuration,
TeX resources, interpreter/tools, Python modules and resolved libraries are
captured at execution time; no missing dependency is invented from a hash.

## Final superseding audit

The earlier paragraph naming cold05/cold06 and build02 is retained as the
actual intermediate audit, not the final designation. Before sealing A,
another self-audit found that -I still permits site .pth execution, -B
alone prevents writes but not reads from ordinary bytecode caches, and the
math ldd probes had not explicitly resolved Bash's system libtinfo.
Cold05/cold06 remain genuine successful runs under those earlier checks.
The final qualifying pair is cold07/cold08, using -I -S -B and a unique
nonexistent pycache prefix, explicit cmp/Bash link probes, loader/config
before/after pins and the same unchanged scientific code/canonical.

Build03 uses the final helper, adds loader/font/locale configuration
inventories, and was actually viewed on all seven pages after completion.
All three physical builds have identical PDFs, but matching hashes did
not substitute for the final actual view. REPLAY_LOG.md and BUILD_REPORT.md
state the final evidence key. These corrections remain wholly within the
reviewer's evidence package; the manuscript was not changed.
