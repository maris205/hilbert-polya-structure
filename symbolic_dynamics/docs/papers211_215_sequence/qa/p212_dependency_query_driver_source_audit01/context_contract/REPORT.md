# P212 driver: independent context and binding-source audit

2026-09-09 UTC. **SOURCE_ONLY / ONE_MAJOR_GUARD_GAP / HOLD_OPERATIONAL**.

This bounded independent infrastructure audit concerns exact query contexts,
immutable companion contracts, future binding roles and no-generation gates.
It is not a manuscript review, root reception, enabled-binding acceptance,
runtime test, host-body receipt or operational authority. The parent auditor
owns overall driver reception. No author packet or central file was edited.

## Findings

### DCC-F1 — Major: body-role byte reads can precede whole returned-set validation

The current source does not enforce its unconditional promise that the entire
returned-path set is checked before any body bytes can be read
(STAGED_CAPTURE_AND_CLOSURE.md:188–194; driver.js:869–871).

Static branch witness, not a created or executed test:

1. In a hypothetical bodies-phase binding, let a receipt's lexical path q be
   below the workspace and let it be a symlink to a regular referent h. Supply
   the finite observed alias/ancestor chain, equal alias/referent stat fields,
   q and h both tagged role=body, and content=null. Let the receipt reference's
   own required pin describe the complete bytes at h. The intended approved
   returned-body list does not contain q or h.
2. These role/kind/content values are permitted by descriptorShape
   (driver.js:304–329), the phase-only body-role gate (538–539), and the
   symlink checks (540–546). referenceShape (417–420) constrains q's lexical
   workspace path and pin shape but neither its input role nor its referent's
   role. A fully bound workspace symlink may resolve outside the workspace.
3. receiveRef delegates directly to readPinned (421). In bodies phase,
   readPinned explicitly permits a body-role input with a supplied expected
   pin even when content=null (356–361), and opens/reads its complete regular
   referent at 364–381.
4. main calls receiveRef for receipts and outer source/request refs at 863–864,
   before validateQueryInputs at 871. Thus h may already be read before
   q/h are eventually rejected as unreturned body paths at 755–756.
   The same bootstrap issue exists inside validateQueryInputs itself:
   stdout/stderr/result refs are read at 694–696 before the whole returned
   body-path set is constructed and checked at 739–756.

The witness does not allege a real accepted receipt, enabled binding or host
read. Root's separate semantic receipt/binding reception could reject such
misclassification. That external obligation does not establish the inner
driver's advertised unconditional guard. A later rejection cannot undo a
prior body read. Severity is Major for the prospective operative source guard,
not for an executed incident.

Recommendation before operative acceptance: assign and validate byte-read
purposes before any read. Receipt, source and archived-query reads need
explicit non-body roles, correct file/alias/referent kinds and complete
prebound bytes; prohibit their lexical/resolved alias roles from entering the
unknown-body channel. Validate all returned-body descriptors before enabling
that channel. Keep any source correction in a new immutable revision and
receive its exact delta; this audit makes no author edits.

### DCC-O1 — Minor: the selected binding file is not an inner mandatory byte key

main initially reads and decodes filename at driver.js:854. The mandatory
input list at 529–530 includes SELF, Node aliases, /dev/null and query paths,
but not filename; the source never subsequently calls readPinned(filename)
or independently checks its current bytes. snapshot (385–409) and final
comparison (914–915) cover supplied input descriptors only. The exact fixed
binding path (497) and canonical syntax (258–265) do not pin its file bytes.
BINDING_RECEIVED at 878 records the parsed initial content, not a later fresh
source-file comparison.

The separately received outer input key is explicitly required by
STAGED_CAPTURE_AND_CLOSURE.md:170–179, and post-start inner checks are
explicitly disclaimed as a startup gate at 94–99. Therefore this is an inner
coverage limit/future binding obligation, not evidence of a currently
accepted missing key or an automatic Major failure.

Recommendation: make the actual selected binding bytes, lexical/resolved
identity and before/after agreement explicit mandatory roles of the separate
outer pre-startup/capture contract. Do not advertise the inner snapshot as
covering that file merely because its pathname is fixed. Avoid attempting
a circular in-file full self-hash; use the outer receipt/key.

## Independently checked context and contract facts

- All 19 complete ordered label/name/program/engine/role/basis/required tuples
  in driver.js:37–209 agree with QUERY_FRONTIER.json:116–288, not merely with
  a count. The second texmf.cnf seed is explicitly bibtex (138–144 versus
  frontier:217–223). Plain style is bibtex; the other 17 are pdflatex; every
  engine is pdftex. There are 11 required and 8 optional exploratory seeds.
- All 53 ordered proposals agree with the entire frontier: two help/version
  [0] proposals, default then --all for 19 contexts with [0,1], 12 ordered
  variables, and one literal -expand-path=$TEXMF with [0,1]. Every result is
  null. driver.js:210–213 and 422–438 independently construct this sequence;
  449–451 compare complete seed tuples, argv records, ENV8 and query cwd.
  BIBINPUTS/BSTINPUTS alone use bibtex among variable queries.
- OLD_COMPANIONS at driver.js:18–35 fixes four independent SHA-256 values.
  readPinned plus whole-byte SHA equality and canonical decoding at 440–454
  preserves every current companion field and byte. The actual four native
  hashes match those constants. Canonical re-encoding at 258–265 rejects
  duplicate members/alternate bytes. This closes the old DSA-O1/O2 patterns
  for this exact immutable revision; it is not a generic revised-contract
  semantic validator and does not erase the old audit's stated limits.
- BINDING_KEYS, RECEIPT_KEYS and controller/options/input/ref/body/query/result
  nested checks explicitly constrain required keys (224–229, 242–245,
  304–329, 417–420, 456–548, 688–756). The disabled actual companion has false
  execution fields, null receipts/closure, empty arrays and no phase.
  A disabled entry throws at 493 before any child or host-key snapshot.
- Contract/lookup/bodies paths are distinct and literal (driver.js:495–502;
  handoff:75–86). Contract cannot assert option acceptance or later receipts
  (505–508). Lookup/bodies require a separate options ref plus accepted
  flags, default/all, expansion, format and generator semantics; unknown
  generators must be false (510–514). The four literal no-mktex flags are
  appended to every one of the 51 lookup proposals, not the two contract
  queries (422–438). spawn is argv-based with shell:false (606–608).
- Help/version results do not automatically accept semantics or enable the
  next phase (899–912, 920–923). Current installed support and sufficiency
  remain unobserved. Required missing resolutions stop (675–684), stderr
  stops before interpretation, and variable output remains data rather than
  absence (903–910). These are static source deductions, not executed tests.
- Nine semantic/lock closure roles remain null and all prohibited roles stay
  false/HOLD_EXTERNAL (214–220, 478–479, 921–923). The fixed manuscript pins
  are read at 867–868; a future execution-prose change requires newly received
  source/profile pins as handoff:33–37 explicitly states.

## Evidence and limits

INPUTS.sha256 contains 17 actual native workspace hashes. The target manifest
was observed as bbb6bed92196fcb2876db00dc83f0aad41f630f3d738f292f2047e91222d7917;
its six payload entries all passed native sha256sum -c. The operative driver
hash is fc61b463fbb8cb6c09887f12a85152e9e345c242ec0c3693621f396c42066381.

NATIVE_READS.json preserves 19 actual command/result records: 17 source-text
reads, one six-payload hash check and one 17-input hash listing. The complete
938-line driver and complete 1325-line frontier are covered by contiguous
bounded reads; the fourth driver piece intentionally overlaps lines 675–680.
Those 19 native returns exited 0 without live sessions or tool truncation.
Initial orientation/combined displays are not claimed as a complete archived
native transcript; some were display-truncated and are excluded from this
archive. Full bounded rereads supply the substantive evidence above.

The project research skill/workflow required source-first verification and
preservation; this audit therefore writes only its allocated new directory.
Old audit reports were read as original evidence, not substituted for the new
inspection; old checker/emitter sources and historical native trees were not
rerun or reaudited. Ordinary read/hash observations are not nanosecond
read-handle attestation, continuous race closure or host runtime provenance.

Zero driver/helper/emitter execution, syntax/AST/import/mutation test, Python,
kpsewhich/help/version/host-body scan, engine/BibTeX, runtime/ldd query, setup,
build, science, canonical/PDF inspection, render/view, Git or external action.
No prospective binding/query/output/cwd/cache path was probed. There is no
operational authority. HOLD_EXTERNAL remains.
