# P212 stdin / mask options — proposals only

The immediate disposition remains the unchanged mask-gap HOLD. Of the
possible source changes, the owned empty regular-file alternative below
preserves the existing actual `0xFFF` and fourteen-field evidence obligations.
It is narrower in metadata semantics than introducing nullable fields. It
still changes accepted inputs, source constants, a byte-read purpose and
contracts; this document is not that source delta or its acceptance.

## Preferred subject for a separately selected source delta

One proposed literal input pathname is:

`/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_keyed_stdin_input01/empty.stdin`

Call it `STDIN_FILE` below. It is a proposed name, not an observed absence,
existing file, creation request or selected root policy. Nothing was created
or inspected at this name. It is separate from immutable source packets and
future output directories. Root would need separately scoped physical
parent/input creation, then independent actual reception of its complete
lexical/resolved/ancestor key. If occupied, aliased, nonempty or missing
native fields, stop; never truncate an existing object to make it fit.

The proposed descriptor is `role=stdin`, `kind=file`, `comparison=stable`,
physical `resolved=path`, `symlink_target=null`, `members=null`, complete
fourteen-integer `lstat` and `stat`, and complete empty content. Zero bytes
have the mathematical SHA256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
that known digest is not evidence that this actual file exists or is empty.
Require observed exact size zero, whole same-handle bytes and both before/
after native masks, not a manufactured placeholder. A dedicated `stdin`
role is an explicit enum/purpose extension, while the ten descriptor fields
and fourteen actual stat values remain unchanged. Choosing an existing
`configuration` role instead would also require explicit semantic acceptance;
do not silently relabel `device` as a keyed regular-byte input.

| Exact affected source/contract | Proposed delta; unaffected guarantee |
|---|---|
| [Observer](../p212_preprobe_bootstrap_read_order_delta01/observe.py), `HERE`, `FRONTIER`, `SOURCE_RECEIPT`, `main` control loop; [frontier](../p212_preprobe_bootstrap_preparation01/FRONTIER.json) | New sibling source/receipt/frontier locators are needed because accepted control paths are fixed, and the old frontier cannot be edited. Replace the null metadata target with explicit required regular `STDIN_FILE`, `max_bytes=0`, raw capture enabled, zero memberships, documented origin; add all literal ancestors. Remove `/dev` only after no remaining target or alias dependency needs it. New source locations also require exact changed author-source/package-ancestry frontier rows. The existing generic file/zero-byte validators already permit this shape; keep `native` mask/decoding, same-fd pre-read expected-key guard, raw failure retention, two passes and closing controls intact. The old null-specific kind branch need not be a generic mask change; disposition of that unreachable branch must be explicit in the new diff. |
| [Python probe](../p212_trusted_product_source_delta01/python_runtime_probe.py), `SELF`, validation requirement at lines 91–112; [runtime preparation](../p212_trusted_product_source_delta01/RUNTIME_PREPARATION.md) | Change the mandatory null validation sample to this separately bound regular stdin sample, while retaining self and `/`, sorted uniqueness, actual `statx` request/returned `0xFFF`, raw 256 bytes, all fourteen integers and independent unchanged-target Node/native comparison. Update source locator, source receipt, finite bootstrap key and future authorization. This no longer validates the old null-character sample; explicitly preserve that old obligation as unsatisfied instead of calling it passed. |
| [Outer](../p212_trusted_product_source_delta01/outer_contract.py), `SOURCE/SELF/PRELOAD/DRIVER/DRIVER_SHA`, `descriptor`, validation, prepared request, main | Add/select the exact stdin role and constant; replace mandatory null/character constraints with physical regular, exact role, full empty-content pin and size-zero constraints. Keep all `full_stat`, descriptor shape, `resolve`, full pre/post snapshots and whole inner-to-outer descriptor equality. `read_bound` already requires a canonical same-role regular referent and full pin; its callers need the declared stdin purpose. Update prepared request from `BOUND_/dev/null` to a literal bound regular-file description. Open `STDIN_FILE` with no-follow (and the bounded regular-open guard policy), native-fstat the actual fd with `0xFFF`, verify regular/zero/complete stable key before handing that very fd to `Popen`. Retain same-fd/after evidence and source/receipt pins; no pathname-only assurance. |
| [Inner driver](../p212_execution_scope_source_amendment01/driver.js), `SELF`, `POLICY.stdin`, `descriptorShape`, `fileForPurpose`, mandatory inputs, `nativeCapture`, snapshots/attempts | Introduce the same `stdin` role in both descriptor-role and byte-read-purpose allowlists, keeping exact same-purpose regular referent checks. Merely changing `kind=character` to `file` with `role=device` fails: `snapshot` calls `readPinned` for the mandatory nonnull content pin, but `fileForPurpose` excludes device. Replace the exact null path/policy and character assertions with the physical regular/zero-byte constraints. Resolve all new ancestors; separately open, fstat and verify the actual stdin fd before `spawn(...,stdio:[stdinFd,outFd,errFd])`; preserve full fourteen-field shape, independent native-mask prerequisite, stable comparison, before/after key and complete attempt/configuration records. Each child must receive a verified fresh zero-position read fd, never inherited ambient stdin. |
| [Capture companion](../p212_execution_scope_source_amendment01/companions/CAPTURE_CONTRACT.json), `commands.stdin`; driver `OLD_COMPANIONS` / `oldCompanions` | Create a new companion with the exact regular-input contract and update its literal path/full hash in the new driver; old whole-byte companion pins are enforced. Inspect other relocated companion references and preserve unaffected commands/phase gates. A report attached to the old companion is not a changed operative contract. |
| [Preload](../p212_trusted_product_source_delta01/node_preload.js), [collector](../p212_trusted_product_source_delta01/product_capture.js), [root decision](../p212_trusted_product_boundary_root01/DECISION.json), [read coverage](../p212_trusted_product_source_delta01/READ_ENTRY_COVERAGE.md), [source contract](../p212_trusted_product_source_delta01/SOURCE_CONTRACT.md) | New driver/outer/preload source locations and hashes must agree in every fixed argv, loader check, prepared request and receipt. Preload's existing three-integer-fd check has no direct character assertion; origin verification remains an inner/outer duty, or needs its own explicit added guard. Node probe has no direct null check, but its exact source/bootstrap receipts and `.js` ancestry change if relocated. Update capture/source/runtime/coverage prose and input-role enum; preserve help/version-only scope and all existing startup-trust limitations. No new trust model or observer-of-observer layer is needed or authorized. |
| [Actual observer launch template](../p212_preprobe_observation_root01/REQUEST.json) | A future request cannot keep the old `</dev/null` and then claim all null dependence was removed. Explicitly select the new keyed regular stdin redirection, or separately describe the ordinary product stdin boundary. The original root prefixes contain no stdin clause, and the product collector contains no null redirection; do not invent one in those historical records. All new literal requests and key receipts require root reception. |

The future regular-file open should use the existing bounded regular-file
guard pattern (`O_NOFOLLOW`, with `O_NONBLOCK` where needed to avoid waiting
on a substituted nonregular object), inspect the same opened fd before any
read or handoff, and retain its whole key/empty content. If an empty-content
check advances an fd, explicitly establish its handoff offset; a fresh
read-only open of a verified empty file avoids sharing offset state between
the outer's Node stdin and each inner native-child stdin. Do not substitute
a pathname hash for fd identity, or `stdio='ignore'`/inherited input for an
explicitly verified fd. Finite endpoint checks still are not an atomic or
continuous-race guarantee. All ancestors must actually support the retained
mask; this source proposal does not predict that they will.

## What is and is not a behavioral equivalence

In the inspected wrappers, character kind is asserted as part of the chosen
stdin binding; no ioctl, device-specific read or device protocol is applied
to that fd. The Python/Node author-probe application sources contain no stdin
read, and the wrappers
hand the fd to Node or the exact native help/version children. This establishes
where the source dependency is imposed, not that every downstream program
ignores file type. A verified zero-length read-only regular file supplies
EOF for ordinary reads, but a regular file and a character device differ in
stat/type, seekability and device-specific operations. The actual installed
Node/native-child implementations were not inspected here. Their relevant
stdin handling for the exact first help/version vectors remains a required
separate source/behavioral justification. No scientific requirement for a
character device was established by this analysis, and no theorem or child
equivalence is inferred. Later lookup/body/build actions retain their own
gates; they do not inherit blanket equivalence.

## Alternatives and decision boundary

- **Keep the exact source and HOLD:** the only currently available outcome.
  Preserve all actual failure evidence; do not rerun expecting a different
  mask without a new bounded reason/authority. This does not close the old
  key or authorize author probes.
- **Delete only `/dev/null` from the frontier:** rejected under current
  sources. The Python sample, outer/inner input mandates, actual fd opens,
  capture companion and current observer shell redirect still depend on it.
- **Role-scoped mask/nullable-field delta:** a distinct, broader evidence-
  semantics change, not preferred here. It would need explicit requested/
  returned-mask validity, missing-value representation, descriptor/read/key/
  projection/Node comparison changes and native failure retention across all
  consumers. An ancestor-only exception leaves null-leaf support unknown.
  Globally dropping birthtime, supplying zero or adopting Node's field as
  native mask evidence is not acceptable. No such design is implemented.
- **Closed-input pipe:** avoids a pathname but introduces an instance/fd and
  writer-ownership/closure contract. All writers, including inherited ones,
  must be closed before the intended EOF; pipe fd kind/lifecycle cannot be
  represented as this unchanged keyed regular-file descriptor. It may also
  introduce different runtime/native operations. Using it while retaining
  the old path/full-field contract is not a solution; its wider source and
  ownership changes need separate selection and review.

If root selects a new regular-input source delta, the order remains exact
new source/contracts and noncontributor review → root source reception →
separately authorized creation and finite independent observation/key reception
through the received mechanism → separately received author-probe/runtime/
child-semantic evidence → later explicit
operation gate. The allocation of creation versus observation authority must
be stated then; none is supplied here. Source acceptance alone is not a run
grant, and the old strict `/dev` requirement is never retroactively satisfied.
