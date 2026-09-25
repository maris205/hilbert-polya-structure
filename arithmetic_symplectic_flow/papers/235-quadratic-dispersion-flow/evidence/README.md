# Evidence record — quadratic log-dispersion flow

**Candidate ID:** `ANG-20260918-QDF01`  
**Status:** `GLOBAL OWNER ESTABLISHED; MIXED-PRIME RETURN — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Inputs, exact methods and limits

The [version-1 card](../candidate-card.md) was frozen before this candidate's
audit. Its squared-log generator, charge shell and all ordered interactions
are the complete inputs; there is no external dataset or fitted parameter.

The [paper](../paper.md) supplies exact, cutoff-free arguments:

1. Normalize by sqrt(log n) and bound both quadratic coefficient tensors.
2. Prove weighted charge cancellation independently of linear resonance.
3. Apply a time-dependent interaction-picture ODE with uniform ball estimates
   and norm conservation, then derive the actual action law by mild uniqueness.
4. Prove invariance of the complete powers-of-6 probe inside the full carrier.
5. Minimize K+C on Q=1 using the explicit compact embedding tail bound (14).
6. Use the exact two-coordinate trial (15) for strict energy improvement.
7. Derive the multiplier, its positive sign and strong generator-domain tail
   estimate before identifying the actual solution and its least period.

Finite-coordinate tails in the compactness proof are not numerical
truncations used to infer an infinite-model orbit. No simulation, floating
precision, GPU computation, numerical stationary point, PDF or publication
artifact was used. Full periodic classification, stability and naturalness
remain open.

## Review and mechanical verification

A separate read-only technical checker first derived the owner and return
arguments from the raw card without the author's proof, then read the final
paper and all five package files. It reported no mathematical, constant or
same-object error in the bounded audit. The written readback covered the
time-dependent interaction picture, whole-E charge cancellation, compact
energy tails, trial state, multiplier sign, strong domain repair and exact
physical return group. A separately delegated charge check also agreed.
No optional broader regularity theorem or sharper constant from those
checks was adopted into the paper.

The reviewed paper hash, also independently read by root, is:

```text
14b7cf486913a4801227629663ea2ded9baa8489649dc712501ebc60f9d74db3
```

Root's read-only `node` check processed the five Markdown files in this
package and the corresponding five in 234. It required each exact ID,
current result marker, `UNASSIGNED` and `NOT INVOKED`, checked LF text and
final newlines, and resolved local Markdown file targets after stripping
fenced/indented and inline code. It also checked both IDs and targeted
234/235 links in root `readme.md` and `papers/README.md`. Observed stdout:

```json
{
  "package_files": 10,
  "package_relative_links_checked": 42,
  "registry_files": 2,
  "targeted_registry_links_checked": 6,
  "errors": []
}
```

`git diff --check -- readme.md papers/README.md` exited 0 with no output;
that command covers only tracked registry changes, not the untracked
packages. The node readback covers their literal markers and basic text/
link integrity, not Markdown anchors or mathematics. Administrative evidence
receipts add no link targets and change no proof inputs.

Checking is within the same model runtime, not external peer review or a
correctness certificate. ARS informed proof dependencies, adverse controls
and evidence separation. No unpublished material was uploaded externally.
