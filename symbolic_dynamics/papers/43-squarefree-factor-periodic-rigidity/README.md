# Paper 43 pre-output integration candidate

This directory is a portable, result-empty implementation candidate for
`SD-C45`, squarefree-factor periodic rigidity. It contains immutable frozen
research/DA bytes, a 40-source exact byte-container snapshot, a portable
17-file result-free writer baseline, a deterministic authority-root research
lock, a raw packet producer, two independent exact evaluators, strict Route-A v0.2
renderer and validators, mutation harness, and transactional parent.

Every adversarial instance carries an explicit domain, variant, and exact
designated-consumer set.  The harness requires the observed outcome keys to
equal that set and every designated mutation consumer to reject nonzero.
Relocation, isolation, snapshot, and hygiene checks are recorded separately as
typed positive controls rather than being presented as rejection evidence.
Every canonical JSON result is checked by recursive exact Python type and
value, then by exact canonical bytes. In particular, Boolean, integer, and
floating-point values are never accepted through Python's numeric equality.

No canonical result, Route card, report, paper manifest, authority byte, Git
state, mirror byte, or publication registration is present in the declared
static seal. Smoke outputs are generated only in unrelated disposable copies.

The integration static manifest and result ledger deliberately exclude the
authority writer/root-lock overlay. The read-only auditor nevertheless owns
that whole-tree boundary: it accepts either no overlay, the exact 17-file
result-free baseline plus its exact manifest and root lock, or one publication
state in which exactly three declared writer content paths change and both the
PDF and compilation report are present. Missing, extra, partial, or
unauthorized writer/root-lock states reject. The PDF is classified as binary;
all other overlay files are exact UTF-8 text with portable-path hygiene.

Historical source records and the frozen blueprint are stored as canonical
base64url containers.  Their package-relative container hashes, decoded-byte
hashes, and typed source IDs are checked independently; decoded bytes are
never serialized into canonical outputs.

The run remains a retrospective replay of known mathematics, and the V5
disposable canonical-copy outputs were known before this V6 overlay repair.
The frozen
novelty ceiling and external `STOP_DUPLICATE` boundary remain in force.
