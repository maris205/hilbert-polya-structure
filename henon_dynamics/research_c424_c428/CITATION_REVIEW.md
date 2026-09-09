# C424–C428 bounded citation-integrity review

2026-09-09 UTC. Initial snapshot at 07:03 UTC; C428 handoff and final
targeted citation recheck completed after 07:07 UTC. Sole writer: current-team agent
`round6_positive_characteristic`. This is the separately assigned
batch citation cross-check, not five new manuscript reviews or a formal
Route-A evaluation. The checker previously drafted C424 and reviewed
C427; no blind-panel, independent-human or personal-authorship
certification is inferred from this task.

## Result and scope

The 28 bibliography entries across the five manuscripts all have matching
active-source citations, converged auxiliary citation keys, bibliography
items and resolved bibliography labels. The inspected versions have
**zero orphan citations, zero uncited entries, zero duplicate bibliography
keys/items/labels and zero unresolved final citation diagnostics**.
The same work appearing in different papers is not a duplicate within a
paper's bibliography.

This narrow key-consistency result is **not a citation-all-compliance
PASS certificate**. Five known arXiv-DOI presentation/completeness items
remain recorded below, every paper exceeds the requested 15% internal-work
alert threshold, one older source has no verified DOI, and retraction,
competing-interest and venue checks were not performed. No manuscript,
bibliography, historical source record, global registry or Git state was
modified by this review.

I read all five current `references.bib` files, all five complete
manuscript citation/source audits, each selected complete `.bbl`, and
the citation/bibliography records in each selected converged `.aux`.
The final `.log` and `.blg` were checked for substantive unresolved
citation/reference, warning and error diagnostics. A read-only traversal
of the literal active `main.tex` input trees extracted actual citation
commands and compared their keys with the three bibliography layers.
It did not execute any mathematical source or build a PDF.

## Version binding, including revisions in progress

All build paths in this table are relative to the corresponding paper
directory under `papers/`.

| Paper | Citation output inspected | Actual status at this snapshot |
| --- | --- | --- |
| C424 `C424_integer_valued_quadratic` | `build/round0_layout1/main.{aux,bbl,blg,log,pdf}` | Entered the audit after no-change round 1; coordinator subsequently reported both manuscript passes accepted and delegated final builds to the original reviewer. Bibliography remains unchanged; this audit does not certify those later builds. |
| C425 `C425_fricke_return` | `build_round1_01/main.{aux,bbl,blg,log,pdf}` | Entered this task under authorized abstract revision. Author subsequently confirmed STOP-WRITE/pending_round2; `ROUND1_HANDOFF.md` and improvement log were read. Active PDF equals this revised build; bibliography is unchanged. |
| C426 `C426_affine_good_models` | `builds/round1_revised/main.{aux,bbl,blg,log,pdf}` | Revised bibliography frozen; active PDF equals this build. This citation record does not award a manuscript-review gate. |
| C427 `C427_vieta_semilinear` | `builds/round1_revised/main.{aux,bbl,blg,log,pdf}` | Actual revised PDF after the adopted absolute-value clarification; active PDF equals this build. The separately written second manuscript review is not replaced by this audit. |
| C428 `C428_integer_period_spectrum` | `builds/round1_revised_03/main.{aux,bbl,blg,log,pdf}` | Entered the audit under authorized pseudocode/P2 revision. Author subsequently completed handoff and STOP-WRITE/pending_round2. The final targeted recheck confirms active PDF and `main_round1.pdf` equal `_03`; the seven bibliography entries remain unchanged from inspected `_02`. |

C428's final selected revision is 16 pages, 389314 bytes, SHA256
`cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`.
At the initial 07:03 snapshot, the old active `main.pdf` still had SHA256
`d5aeb4ae86009dc9f229a54c50083ccb03eba1f3bdc562d13a12400140dd8cde`.
An initial comparison therefore correctly reported different PDFs; this
was an expected in-progress handoff, not a concealed build failure.
The author identified `_02` during work, then `_03` after a non-citation
hyphenation correction. I read the final improvement log/state, reread
the complete `_03` bibliography and its auxiliary citation records, and
verified that its `.bbl` and `.aux` are byte-identical to `_02`.
The final counts here use `_03`; P2 was not merely assumed carried over.

For every paper, the current bibliography was compared with its actual
build-source snapshot/archive and matched byte for byte: C424's frozen
`baseline/round0_layout1/`, C425's `source_snapshot/`, C426/C427's
`source.tar`, and C428 `_03`'s `source.tar`. No current-bibliography
check is silently paired with an unrelated old `.bbl`.

## All-key cross-check and internal-work ratios

The ratios count distinct bibliography entries within each paper, not
repeated in-text mentions. “Internal” includes the actual unpublished
project manuscripts, proof packages and review/certificate archives.
It is **not verified personal self-citation**: human author identities
and authorship overlap have not been established. Required predecessors
and substantive proof evidence should not be removed to lower a ratio.

| Paper | Bibliography entries | Source citation commands | Auxiliary citation records | Internal entries | Internal proportion | >15% flag | Orphans / duplicate entries / unresolved keys |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| C424 | 4 | 9 | 9 | 2 | 50.0% | FLAG | 0 / 0 / 0 |
| C425 | 6 | 9 | 9 | 1 | 16.7% | FLAG | 0 / 0 / 0 |
| C426 | 5 | 9 | 9 | 1 | 20.0% | FLAG | 0 / 0 / 0 |
| C427 | 6 | 10 | 10 | 1 | 16.7% | FLAG | 0 / 0 / 0 |
| C428 revised `_03` | 7 | 15 | 18 | 4 | 57.1% | FLAG | 0 / 0 / 0 |

C428 has one source `Pezda2002` citation inside `\text{...}` in a
displayed equation (`sections/01_theorem_sources.tex:42`) and four
corresponding auxiliary records. This is consistent with math-style
expansion; the source occurrence count is one, not four independently
written citations. There is only one Pezda bibliography item and one
resolved label. The difference is not an orphan or duplicate reference.
Similarly, `thebibliography{1}` in the plain-style C426/C428 output is a
label-width argument, not a statement that only one entry exists.

In the following complete key tables, `S/A` gives source-command and
auxiliary-record occurrence counts. **Every listed key is present in
the `.bib`, `.bbl` and resolved `.aux` label set**; none was omitted from
the comparison. The DOI column separates stored metadata from actual
rendered bibliography output.

### C424 — four entries

| Key | S/A | Identity/version and role | DOI status in the inspected output |
| --- | ---: | --- | --- |
| `am1certificate` | 2/2 | Internal AM1 proof/exact-certificate archive, 8 September 2026; substantive finite dependency. | No external DOI asserted or invented. |
| `c412` | 5/5 | Internal anonymous C412 predecessor, 2026; full accompanying PDF and exact theorem/table locators. | No external DOI asserted or invented. |
| `ingram2014canonical` | 1/1 | Patrick Ingram; PLMS 108(3), 780–808; issue year 2014, online 22 July 2013. | `10.1112/plms/pdt026` is stored and rendered. |
| `kim2025many` | 1/1 | Four authors Kim–Krieger–Postolache–Szeto; arXiv:2412.01668v2, 8 July 2025; initial deposit 2 December 2024. | `10.48550/arXiv.2412.01668` is stored but **not rendered**; exact version URL is rendered. |

### C425 — six entries

| Key | S/A | Identity/version and role | DOI status in the inspected output |
| --- | ---: | --- | --- |
| `abboud2025rigidity` | 1/1 | Marc Abboud, arXiv:2406.11510v3, 23 April 2025; no journal publication asserted. | `10.48550/arXiv.2406.11510` is stored and rendered via the note. |
| `c4212026integral` | 2/2 | Internal anonymous C421, 8 September 2026; equal-forcing prior ownership. | Explicitly no DOI/public archival identifier; relative repository URL is not public hosting. |
| `cantat2009bers` | 2/2 | Serge Cantat; Duke Math. J. 149(3), 411–460 (2009); read version arXiv:0711.1727v2, 5 December 2007. | `10.1215/00127094-2009-042` is stored and rendered. |
| `planat2024dynamics` | 1/1 | Michel Planat, David Chester, Klee Irwin; Dynamics 4(1), 1–13 (2024). | `10.3390/dynamics4010001` is stored and rendered. |
| `shin2026character` | 2/2 | Eunju Shin; Proc. AMS 154(10), 4091–4106 (2026); consulted accepted arXiv:2308.16614v3, 1 June 2026. | `10.1090/proc/17770` is stored and rendered; issue metadata is not a claim of reading an unavailable final journal proof. |
| `vishkautsan2016residual` | 1/1 | Solomon Vishkautsan; Rend. Lincei 27, 25–35 (2016); arXiv:1504.07099v2, 8 July 2015. | `10.4171/RLM/720` is stored and rendered; independent publisher retrieval remained unavailable in the source record. |

### C426 — five entries

| Key | S/A | Identity/version and role | DOI status in the inspected output |
| --- | ---: | --- | --- |
| `AllenDeMarkPetsche2018` | 2/2 | Kenneth Allen, David DeMark, Clayton Petsche; arXiv:1610.04271v3, 6 February 2018. | Exact version URL present; no DOI field or rendered DOI. The primary record does supply arXiv DOI `10.48550/arXiv.1610.04271`; see targeted check below. |
| `BruinMolnar2012` | 2/2 | Nils Bruin and Alexander Molnar; LMS J. Comput. Math. 15, 400–417 (2012). | `10.1112/S1461157012001131` is stored and rendered via the note. |
| `GR5WorkingNotes` | 1/1 | Internal AI-assisted frozen GR5 proof package, 8 September 2026; provenance, not an external publication. | No DOI asserted or invented. |
| `Kawaguchi2013` | 2/2 | Shu Kawaguchi; Algebra & Number Theory 7(5), 1225–1252 (2013). | `10.2140/ant.2013.7.1225` is stored and rendered via the note. |
| `PetscheStout2014` | 2/2 | Clayton Petsche and Brian Stout; JTNB 26(3), 813–823 (2014); journal online date 9 March 2015 distinguished from volume year. | `10.5802/jtnb.889` is stored and rendered; author arXiv:1303.5783v1 URL also retained. |

### C427 — six entries

| Key | S/A | Identity/version and role | DOI status in the inspected output |
| --- | ---: | --- | --- |
| `c421` | 2/2 | Internal anonymous C421, 8 September 2026; explicit computer-assisted three-dimensional theorem/table import. | No DOI asserted or invented. |
| `ginsburgSpanier1966` | 2/2 | Seymour Ginsburg and Edwin H. Spanier; Pacific J. Math. 16(2), 285–296 (1966); classical effective-semilinearity ownership. | `10.2140/pjm.1966.16.285` is stored and rendered. |
| `huTanZhang2015` | 2/2 | Hengnan Hu, Ser Peow Tan, Ying Zhang; Geometriae Dedicata 192, 207–243 (2018); read arXiv:1501.06955v2, 6 May 2015. Key's 2015 suffix is not the publication year. | `10.1007/s10711-017-0235-z` is stored and rendered. |
| `maloniPalesiTan2015` | 1/1 | Sara Maloni, Frédéric Palesi, Ser Peow Tan; GGD 9(3), 737–782 (2015); fork locator explicitly in arXiv:1304.5770v1. | `10.4171/GGD/326` is stored and rendered. |
| `shin2023` | 1/1 | Eunju Shin; arXiv:2312.07890v2, 17 December 2023; full-group/unforced comparison, not the native forced theorem. | `10.48550/arXiv.2312.07890` is stored but **not rendered**; version URL present. |
| `whang2023` | 2/2 | Junho Peter Whang; arXiv:2305.13529v3, 8 September 2023; classical period/decidability context. | `10.48550/arXiv.2305.13529` is stored but **not rendered**; version URL present. |

### C428 — seven entries, frozen first revision `_03`

| Key | S/A | Identity/version and role | DOI status in the inspected output |
| --- | ---: | --- | --- |
| `C412Working` | 1/1 | Internal anonymous C412 quadratic predecessor, 2026; actual relative local source locator. | No DOI asserted or invented. |
| `C417Working` | 1/1 | Internal anonymous C417 monic cubic predecessor, 2026; positive-spectrum/method ownership retained. | No DOI asserted or invented. |
| `IH6Working` | 4/4 | Internal IH6 frozen proof and two exact author certificate programs, 9 September 2026. | No DOI asserted or invented. P2's duplicated year is absent in current `.bbl`. |
| `IH6Review` | 5/5 | Internal current-team nonauthor reconstruction/review/receipt, 9 September 2026; explicitly AI-assisted and nonblind, not human review. | No DOI asserted or invented. P2's duplicated year is absent in current `.bbl`. |
| `KimEtAl2025` | 2/2 | Same four-author arXiv:2412.01668v2 as C424; v2 8 July 2025 and initial 2 December 2024 preserved. | Exact version URL present; known arXiv DOI `10.48550/arXiv.2412.01668` omitted from both `.bib` field and `.bbl`. |
| `Pezda2002` | 1/4 | T. Pezda; Acta Math. Inform. Univ. Ostraviensis 10(1), 95–102 (2002); DML handle and precise theorem scope retained. | **No DOI verified**, not proof that no DOI exists. No first-name expansion or DOI was guessed. |
| `deHenon2024` | 1/1 | Published credit Julia Xénelkis de Hénon; Arnold Math. J. 10, 585–620 (2024); Section 11 ownership P. Ingram and Conjecture 3 explicit. | `10.1007/s40598-024-00252-x` is stored and rendered via the note. |

## Source verification reused, targeted new check and unresolved items

The detailed primary-reading boundaries remain in the five actual source
records, all read in full for this task:

- [C424 citation audit](papers/C424_integer_valued_quadratic/CITATION_AUDIT.md): actual internal sources, successful DOI/Crossref metadata and arXiv v2 checks, online/issue-year distinction, and failed browser opens.
- [C425 source audit](papers/C425_fricke_return/SOURCE_AUDIT.md): bounded Shin/Cantat/Vishkautsan/Abboud/Planat primary reading, three successful DOI-to-BibTeX responses and unavailable independent Vishkautsan publisher retrieval.
- [C426 source audit](papers/C426_affine_good_models/SOURCE_AUDIT.md): actual publisher/arXiv sources and earlier proof-stage scope; unsuccessful MSP XHTML retrieval followed by successful publisher PDF access.
- [C427 source audit](papers/C427_vieta_semilinear/SOURCE_AUDIT.md): exact primary versions, prior versus new access, unsuccessful fresh Springer/Pezda opens and actual reused classical sources.
- [C428 source audit](papers/C428_integer_period_spectrum/SOURCE_AUDIT.md): DML-CZ Pezda record, Kim v2, official open-problems sources, internal predecessor/evidence roles and source-location failures.

These are preserved observations, not freshly invented whole-source reads
or a new assertion that every cited theorem was independently reproved.
No new global search query or programmatic bibliographic resolver was
used. No private manuscript or source corpus was uploaded.

There was exactly **one new targeted primary open**: the
[Allen–DeMark–Petsche arXiv v3 record](https://arxiv.org/abs/1610.04271v3).
It directly confirms the three authors, title, v3 date 6 February 2018
and arXiv-issued DOI `10.48550/arXiv.1610.04271`. This resolves the
specific distinction between “no journal DOI asserted” and “no DOI
available.” No journal publication or fresh full-paper proof reading
is inferred. Kim's arXiv DOI was already actually verified and recorded
in C424's source audit; it was not guessed from the identifier here.

### Open DOI presentation/completeness observations

| Item | Affected entries | Observed fact and bounded disposition |
| --- | --- | --- |
| D1: stored DOI suppressed by style | C424 `kim2025many`; C427 `shin2023`, `whang2023` | The DOI exists in the current `.bib` but not the actual `.bbl`/rendered reference. All retain exact version URLs. Do not claim all available DOIs are displayed. |
| D2: known arXiv DOI not supplied | C426 `AllenDeMarkPetsche2018`; C428 `KimEtAl2025` | The current entry supplies a version URL but no DOI field or displayed DOI. “No journal DOI asserted” is accurate but does not negate the separate arXiv DOI. |
| D3: DOI genuinely unverified in this record | C428 `Pezda2002` | Keep `no DOI verified` visible. Do not invent one or convert unavailable metadata into verified absence. |

D1/D2 do not prevent a reader from identifying the exact preprint via
its URL, and they are not orphan citations or mathematical counterexamples.
They nevertheless prevent an unqualified DOI-completeness claim. If the
coordinator elects to complete DOI presentation, use a DOI-aware style or
an explicit rendered note and then inspect the resulting `.bbl`/PDF;
merely adding a field to a style that ignores it is insufficient.
This review authorizes and performs **no such manuscript changes**.
The coordinator explicitly elected to retain the exact version URLs and
record these limitations without creating another manuscript revision
solely for DOI display. D1/D2 are therefore retained observations under
that disposition, not a demand for an extra build or a claim that the
DOIs are already displayed.

For comparison, C425's `abboud2025rigidity` already has the DOI in a
rendered note specifically because `plainnat` omits the miscellaneous
entry's DOI field. C426's three journal DOI notes and C428's open-problems
DOI note likewise survive the `plain` bibliography style.

### Revision-specific P2 check

The latest frozen C428 revision's `IH6Working` and `IH6Review` entries each
render a single year after “9 September”; neither retains the adjacent
duplicated `2026` that P2 addressed. Current `references.bib` matches
the final `_03` source archive, and the `.bbl` was read directly. This is the
bounded P2 bibliography check, not approval of the separately revised
pseudocode or of the second manuscript-review gate. The actual author/PDF
handoff is separately recorded and its file identity was checked here.
C425's C421 year
correction is also present in its stable `.bbl`; its current authorized
revision changes only the abstract, not references.

## Explicit unperformed and unavailable checks

- **Retraction / Expression of Concern:** no systematic database search;
  UNPERFORMED, not “none found” and not PASS.
- **Conflicts of interest, verified personal self-citation, named human
  authorship/ORCID and funding:** UNPERFORMED or not supplied. Anonymous
  internal-source labels are not converted into human identity findings.
- **Venue standing, indexing, journal policy/style certification,
  acceptance or publication readiness:** UNPERFORMED. The manuscripts
  use their established numbered mathematical `plain`/`plainnat` output;
  this audit does not impose APA or claim IEEE conformity just because
  citations are numbered.
- **Plagiarism-service or comprehensive claim-to-reference support
  screening:** UNPERFORMED. Recorded precise prior-work ownership is
  retained, but a zero-orphan result does not establish semantic support
  for every sentence.
- **Local PDF structural page-anchor certification:** earlier ARS
  preflights reported UNAVAILABLE where `pypdf` was absent. No missing
  dependency was installed, no structural PASS is inferred, and this
  task makes no new PDF page-anchor or all-page-visual claim. It examines
  the selected `.bbl` and source identities directly.
- **New mathematical execution / PDF build / formal Route-A grade /
  Git operation:** none. The read-only citation parser, hashes and byte
  comparisons do not constitute mathematical experiments.

Older references are retained for their actual classical or adjacent
roles, not treated as recent-news evidence. The per-paper recorded
2021-or-later entry counts are C424 3/4, C425 4/6, C426 1/5, C427 3/6
and C428 6/7, including the dated internal items. These simple year
counts do not measure novelty or justify replacing necessary sources.

## Artifact identities

The following pins permit a later final-version delta check. They do not
freeze other agents' authorized work or create a global release manifest.

| Paper | Current `references.bib` SHA256 | Read source-audit SHA256 |
| --- | --- | --- |
| C424 | `c0bd7e8905353c83fce70abee223d1088988cb43644a2ab79dbe7c2cacab6076` | `c191246df4a6eba7b7347d7b7a4770688d0638d2b1ccc67111be1918e6de20c0` |
| C425 | `9b35b94a205812d6b9e7ab43e2b6d162206fa94c34e07b7a84bce5b0bc69b7c0` | `b51a788f2399684ee9596f68ec8603cdc66b1e661f1aa624335e323e96ef5ee7` |
| C426 | `74c81ffb2eba1bcbb5a9e9b5167e16f227526062f62d69ed348f80a6ce499e19` | `fc00081f1c4cdf43120a5e3c4a2a29c45ff4080bff029a0bd36fc3d580154e38` |
| C427 | `133829fcecde21b8be888891fa8a64a1efd6b91b92566d5377ec83952caa87d2` | `1abd7f6a6503ef9af184e152acc95734d4482a84fd1c594a98657673474f784f` |
| C428 revised `_03` | `6953064f84aa02969faeb35e0a4f41e6cbfc9873dcacc8128e9ffec53c033e7a` | `77b80b7e4601db141a41712d8a3fae8c276db7f71c5e4d4a166d18e9943bb4b1` |

| Paper / selected build | `.aux` SHA256 | `.bbl` SHA256 |
| --- | --- | --- |
| C424 `build/round0_layout1` | `07de9302cd8a3c6f074419b192fe52432c45a3b29cc1d0b17ac1f6429e571108` | `a40f170365abe93edbcff014c7ac849dbd65da8995cdc523d1be74c2647d8824` |
| C425 `build_round1_01` | `72c527d6aa8701f078247376d1a539093e284ea58cd0acc496763b551ceba081` | `1bb000cb51520dd09fdd801795623f735786c4425e07cde6f1e3486bcaf5e783` |
| C426 `builds/round1_revised` | `6f452ec5ce115241eb04167a141c89a090a35222477c65ba4b850a6ebde32f13` | `1097939f1e22347e91f4ba3aaabd09745df0db07e4173501c19b1e61509134df` |
| C427 `builds/round1_revised` | `ebbed3ceaf885530c53ce8ab4a4f3b68a9b75c8f1962b011976c2ccd40a25942` | `38fd6169e75a4aa180ea099f66a1c79c67d7341f18a7d19d5d4fa0c419668788` |
| C428 `builds/round1_revised_03` | `b5838efb184bb26e7df3e9405b0eab5d27376ae040ee3709f570a5d6a7299240` | `51052d95bb908bb53dd30572cc7e6349cd86b51a335810021113c5a4c182df55` |

The selected PDF hashes are C424
`3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b`,
C425 `e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb`,
C426 `d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db`,
C427 `cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1`,
and C428 revised
`cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`.

The ARS citation-check role supplied the exhaustive key comparison,
source/version distinction, internal-reference alert and explicit
degradation labels. The coordinator's bounded read-only assignment
overrides its generic automatic-correction, full-pipeline and global
screening defaults. Formal evaluation review remains unstarted pending
separate authorization.
