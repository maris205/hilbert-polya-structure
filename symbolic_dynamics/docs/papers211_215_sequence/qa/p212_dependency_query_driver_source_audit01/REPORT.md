# P212 dependency-query driver — independent source audit

2026-09-09 UTC. **SOURCE_REVISION_REQUIRED / HOLD_OPERATIONAL**.

One **Major/open** source defect blocks reception and use of this driver
revision: the complete returned-body authorization check can run after an
early body-byte read. There is also one disclosed Minor inner-key coverage
observation assigned to the separately required outer binding contract;
it is not a second operative defect. No Critical finding or executed incident
is claimed. Findings are returned only as findings; the author's seven-file
preparation, all historical originals and central indexes are unchanged.

This is a nonauthor infrastructure audit, not P212 mathematical/manuscript
review, an operational test, enabled-binding acceptance or root reception.

## Exact target

[Preparation01](../p212_dependency_query_driver_preparation01/STAGED_CAPTURE_AND_CLOSURE.md):
six payloads / seven files; manifest SHA-256
`bbb6bed92196fcb2876db00dc83f0aad41f630f3d738f292f2047e91222d7917`.
The entire 938-line, 49,231-byte [driver.js](../p212_dependency_query_driver_preparation01/driver.js)
was independently read in five contiguous ranges; its SHA-256 is
`fc61b463fbb8cb6c09887f12a85152e9e345c242ec0c3693621f396c42066381`.
All six other submitted files were read completely, including the disabled
interface, staged closure contract, provenance, native preparation record
and both pin lists. The driver/checker was never loaded or executed.

## DQD-S1 — Major/open: the body-read guard is ordered too late

The submitted promise is explicit: the entire returned-path set is checked
before any body bytes can be read (staged contract 188–194; driver 869–871).
The source instead allows the following symbolic control-flow witness.
No binding, test file, symlink or mutation was materialized or run.

1. In a hypothetical bodies-phase binding, let a receipt's lexical path q
   lie below ROOT and point by a fully bound symlink chain to regular file h.
   q and h are both tagged role=body, content=null, with matching stat fields.
   Give the receipt ref a complete expected pin. q/h are not in the eventual
   returned-body set. This specifies descriptor relationships only, not real
   host paths or an assertion that a genuine receipt has this shape.
2. Input shape and phase/alias validation permit these values (304–329,
   538–547). referenceShape checks q's lexical workspace location and pin
   shape, but not its read purpose, role or referent role (417–421).
3. readPinned explicitly accepts body + bodies phase + an expected pin even
   when content=null (356–361). It then opens and reads h (364–381).
4. main calls receiveRef at 863–864, before validateQueryInputs at 871.
   The latter can reject q/h as unreturned only at 755–756. The same issue
   exists inside validateQueryInputs: its stdout/stderr/result refs are read
   at 695–696, before the complete returned-body authorization at 739–756.

A later refusal cannot undo the earlier read. Even a subsequent hash mismatch
is checked after opening/reading; a pin-shape check is not a purpose guard.
The defect concerns the future executable source's advertised invariant,
not an observed unsafe run or a currently accepted malformed root receipt.
Independent bounded consultation [DCC-F1](context_contract/REPORT.md)
reached the same witness; the main auditor independently traced it.

Required correction, in a **new-only revision**: validate the purpose,
non-body role, ordinary-file/alias kind, resolved referent role and complete
prebound bytes of every bootstrap receipt/source/runtime/query-result read
before any read can occur. Keep those channels disjoint from first body
capture. Body-byte permission must remain false until the entire ordered
returned set and every body descriptor/alias role have passed; a supplied
expected pin must not bypass it. The new source and exact delta require
fresh source reception. This auditor does not implement the correction.

## Other static conclusions and explicit limits

| Source area | Deduction from the complete text; not an executed test |
| --- | --- |
| Fixed frontier, 18–35 / 37–213 / 422–454 | All 19 complete ordered seed tuples and all 53 argv records match the complete inherited 1,325-line frontier. There are 11 required / 8 exploratory contexts; plain.bst and the second texmf.cnf use BibTeX; only BIBINPUTS/BSTINPUTS use it among variables. Four immutable whole companion hashes plus canonical-byte decoding cover all fields and close the earlier DSA-O1/O2 patterns for this exact revision. |
| Disabled and future schema, 224–229 / 456–549 | Required top-level/nested keys, false/null closure roles, replacement ENV8 and distinct phase locations are explicit. The actual disabled companion reaches the refusal before host-key snapshot or child creation. This says nothing about having safely executed Node startup. |
| No-generation stages, 422–438 / 505–518 / 899–923 | Two help/version operations are distinct from 51 later proposals. All later argv carry the four literal no-mktex flags. Lookup requires separate affirmative option/format/default/all/expansion/generator acceptance; unknown generators stop. Nonempty help is not semantic acceptance and no phase enables the next one. |
| Path/config key, 304–415 / 523–548 | Finite component spellings and aliases are required, absent roles require ENOENT plus a bound present parent, /dev/null has an actual character-handle check. Full integer metadata is retained while declared comparisons exclude atime; identity-only comparison is confined to namespace-ancestor directories. Root still must justify which configuration/search directories and memberships belong in the finite key. DQD-S1 limits the body-role gate. |
| Native capture, 568–664 | ATTEMPT, input/config maps and separate raw files precede spawn. Literal argv, fixed ENV8/cwd, detached-group request, actual events, exit and close are distinct. Deadline/no PID/error/unclosed/nonempty-or-unknown group takes UNKNOWN_UNCLOSED, records no final raw pins, sets ownedUnsettled and prevents the inner success seal. Disallowed exits, required-missing results, diagnostics, oversize or changed-key outcomes stop before phase success; an allowed exit 1 for an empty optional lookup is not falsely called failure. No automatic retry, signal intervention or cleanup appears. |
| Raw interpretation, 665–758 | LF alone is separated; spelling order, duplicates, shadows and empty bytes remain. Relative/control/non-UTF-8 or ambiguous paths refuse interpretation. Required missing inputs stop despite an allowed query exit 1; stderr stops; variable output is explicitly data, not absence. Historical query-result fields/events are checked but receipt authenticity still belongs to root. Bootstrap read-purpose ordering needs DQD-S1's correction. |
| Body copy and cmp, 759–823 / 887–898 | After proper authorization, the intended copy uses a bound regular referent and observed read handle, ordered full bytes, exclusive output and full-size/hash checks. Oversize retains partial failure. Separate literal native cmp, alias/path/copy checks and final complete source hashes are present. cmp's internal handles and continuous races are explicitly not observed. No source semantics or lock is emitted. |
| Inner seal/failure, 825–846 / 914–938 | Complete generated file/directory membership is checked; LOCAL_TREE labels its pre-self census; SHA256SUMS is nonself. Unsettled children cannot reach sealLocal. Failure records retain partial outputs and do not create a valid success seal. This is only an inner seal, not outer native/product acceptance. |

No defect is assigned merely because the complete outer entry is missing:
that absence is truthfully disclosed and operations are already held.
Staged contract 170–179 leaves actual product request/yield/poll/final
envelopes, broader owned-session settlement/member census, outer key and
manifest to a separately received pre-startup source. An ESRCH group sample
does not close those roles. Exact Node/bootstrap/tool/configuration closure
must be established before startup, not inferred from this inner source's
post-start observations. These are intended pending gates, unlike DQD-S1's
actual contradiction of the promised body guard.

The inherited article/plain/array/T1 profile remains exact, including eight
fixed source pins, six inputs and no lmodern/A4 assumption. The current
section 05 still uses historical preparation-stage prose; its later update
requires a new fixed profile receipt. Class/kernel/NFSS/metric/VF/map/font,
format provenance, databases/native/rendering and actual build-cwd closure
remain source-derived future obligations. No old840 transplant or host lock
is treated as complete here.

## DQD-O1 — Minor/nonblocking outer-binding coverage observation

The selected binding file is read once at 854; its filename is not mandatory
in the inner input list at 529–530, and the final snapshot covers only supplied
descriptors. BINDING_RECEIVED at 878 records initial parsed content, not a
fresh comparison of the underlying file. The explicitly required outer key
must bind original selected binding bytes/identity and required before/after
agreement. Do not advertise that as an inner-key check. A full self-hash
inside that same binding would be circular; use the external nonself key.
This retains [DCC-O1](context_contract/REPORT.md) as a coverage observation,
not a second currently defective accepted binding.

## Evidence and authority

[FINDINGS.json](FINDINGS.json) gives the exact source-line census and required
delta. [READ_SCOPE.md](READ_SCOPE.md) distinguishes full text inspection,
hash-only source preservation and intentionally unexecuted obligations.
All 40 original pins, all six submitted payloads and the independent context
subpacket were checked using native file hashes; this is integrity evidence,
not an operational replay. Full selected actual read returns are retained.

The project symbolic-dynamics-research skill required source-first,
dependency-sensitive checking and preservation. Main and consultant are
noncontributors to this driver implementation. Their work is infrastructure
source review only and supplies neither P212 manuscript review.

No driver, old checker/emitter, syntax/AST/import/mutation test, help/version,
kpsewhich, host-body scan, runtime/ldd probe, TeX/BibTeX/Python, science, build,
PDF/render/view, Git or external action was performed. No future binding,
query/output/cwd/cache path was probed. Source PASS would never supply
operational authority; this exact revision does not receive source PASS.
Root reception, new-only repair and further source gates remain pending.
