# Primary blocker source check — failed body access

Status: `PRIMARY_BODY_UNREAD / REQUESTED_OWNERSHIP_NOT_VERIFIED`.
Date: 2026-09-10 UTC. This is bounded documentary source assistance, not an
independent candidate gate or manuscript review. No admission or paper ID is
assigned and no research index is edited.

## Target and result

Requested source: J. Edmonds and D. R. Fulkerson, *Bottleneck Extrema*,
Journal of Combinatorial Theory 8 (1970), 299–306, at the
[specified original PDF](https://web.vu.lt/mif/s.jukna/EC_Book_2nd/Edmonds-Fulkerson.pdf).

| Requested source ownership | Result of this check |
| --- | --- |
| Definition as inclusion-minimal transversals | Not verified from the original body. |
| Double-blocker identity for clutters | Not verified from the original body. |
| Reduction from arbitrary families to inclusion-minimal members | Not verified from the original body. |
| Empty family / empty edge conventions | Undetermined: no basis to label them explicitly stated, absent, or inferred by the original authors. |

The exact-title search in call 02 returned an indexed excerpt from printed
page 305 of the requested original, on array examples. That excerpt does not
cover any of the requested definition/theorem/convention locations. Incidental
secondary search snippets were not used to establish mathematical ownership.
No relevant original-body page, theorem, proof, or definition was successfully
read. This note does not infer absence from failed access.

A separately adopted convention that blockers comprise **all**
inclusion-minimal hitting subsets of a finite ground set, with the empty
subset permitted, would give b(empty family) = {empty set} and
b({empty set}) = empty family by vacuous intersection requirements. This is
only a conditional definitional observation, **not** a verified assertion
about this source's conventions, wording, or theorem scope.

## Exact access record

1. `BROWSER01_REQUEST.json` / `BROWSER01_RETURN.json`: direct original PDF
   open; HTTP-tool failure `(400) Timeout fetching`.
2. `BROWSER02_REQUEST.json` / `BROWSER02_RETURN.json`: exact direct retry plus
   an exact-title bibliographic search; direct open returned `Internal Error`.
   The same primary URL appeared as search result `turn10725search12` with
   only the page-305 excerpt described above. All returned search material,
   including irrelevant results, is retained without claiming it was an
   independent full-body read.
3. `BROWSER03_REQUEST.json` / `BROWSER03_RETURN.json`: narrowly justified
   extra call after the two-call target proved infeasible: open that indexed
   primary ref at line 0 and request screenshots of PDF pages 0 and 1. Open
   again failed `(400) Timeout fetching`; both screenshots failed to resolve
   because the loaded content type was not `application/pdf`.

Three browser calls occurred; there was no successful screenshot. Requests
are the exact argument objects supplied to `web__run`. Returns are complete
JSON serializations of its actual returned values (not a claim to retain raw
HTTP transport bytes). The files were written only with `apply_patch`.

## Read and action scope

- Completely read `.agents/skills/symbolic-dynamics-research/SKILL.md`, its
  linked `docs/research_state/WORKFLOW.md`, and the applicable installed
  `/root/autodl-tmp/.codex/skills/research-lit/SKILL.md`.
- Recovery context: requested lines 1–260 of `SYMBOLIC_DYNAMICS_STATE.md`;
  its 192-line return was truncated by the command output budget. Used only
  the visible current-status paragraph, not hidden content or recovery text
  as proof. Read `docs/papers211_215_sequence/PIPELINE_STATE.md` lines 1–28.
- Applied research-lit only to the specifically assigned web source; no
  local paper-library scan, arXiv script, private library query, or generic
  expansion was authorized or attempted.
- The output directory's nonexistence was confirmed before creation by
  `test ! -e docs/papers211_215_sequence/scouting/finite_residual_fresh13/primary_blocker_check`,
  actual exit 0 with empty output.
- No fresh13 proof, P211–P213 proof/audit/source, candidate proof, or other
  protected research evidence was read. No scientific execution, code
  import/AST/syntax check, host/runtime/environment/configuration/process
  query, Git, SSH, external contact, or upload occurred.
- Only this newly created directory is owned. Documentary hashing/checking
  and the nonself manifest do not imply source verification or scientific
  validation. Parent receives this failed-access handoff and controls any
  subsequent primary-source recovery.

`SHA256SUMS` covers this note and all six browser JSON files, excluding itself.
