# Independent Build R1 Review of the Paper 24 Deterministic R0 Repair Build

## Verdict and authority

I performed this review as a fresh independent full Build R1 reviewer. I did
not author the manuscript source, the deterministic repair build, the
original build JSON, the retrospective evidence supplement, or the
supplement review. I treated every builder, supplement, prior-review, and
governance assertion as unproved and recomputed the controlling facts from
the allowed current bytes and the two allowed retained successful roots.

All required scientific, source, output, citation, provenance, PDF,
security, anonymity, visual, and permission checks pass. The retrospective
supplement truthfully closes the four earlier provenance omissions without
altering either original JSON record or claiming contemporaneity. There is no
remaining critical, required, major, minor, cosmetic, or contract blocker.

This artifact certifies only the already completed deterministic R0 repair
build. It does not authorize or perform source revision, compilation, retry,
cleanup, an R1 build, release, Paper 25 work, governance mutation, network
action, or any external effect.

## Opening governance, gate, inventory, and role chain

The review opened on these exact current governance roots:

| Root | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `c5843ac6844abbc8e059b1db7f0f9ef960b509ffbb030471da2d43d3d554e699` | 159,266 | 2,315 |
| `BATCH_06_IDEA_REPORT.md` | `321ced6f6fdb76a08b326bf42a24410464bfc5b32e52bc24ebf4cf1276dc90a2` | 267,021 | 5,181 |

The exact live gate was
`PAPER24_R0_REPAIR_BUILD_R1_REVIEW_OPEN`. The exact Paper 24 queue status was
`R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_PASS_PENDING_FRESH_INDEPENDENT_R1_REVIEW`,
with the stage text stating that all four provenance blockers were closed by
an independently reviewed retrospective supplement and that the fresh full
R1 build review was reopened.

At opening, the project contained exactly 36 regular files, four descendant
directories, zero symlinks, and zero other objects. Every regular file was
mode `0644`, owned by `root:root`, and had link count one. For the canonical
sorted row format
`sha256<TAB>bytes<TAB>LF<TAB>relative-path<LF>`, the complete 36-row
manifest was 3,761 bytes / 36 LF and had SHA-256
`ef6f0868799a309450571d110bc0aa6b8dfc10d5cbb65ac289b1cc413ea465eb`.
The independent u64-big-endian path/content framing of the same 36 files was
1,609,922 bytes and had SHA-256
`21270c774d912321ef34df466d71167228f1010097a43d5200c0eeedce89ca9a`.

The full opening manifest was:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `bfd644a19d15f51a4c7eca6323909852d38e7477afac73aea77b02642ffb6f94` | 7,098 | 186 |
| `experiments/EXPERIMENT_TRACKER.md` | `61e34652fdea217b0da4f7774478f243ca806fb88a97e18f09d767e24fbe8db0` | 3,459 | 59 |
| `experiments/publication_lock.json` | `a2f3a4e0a005972b60f8c5b2241889ec5fffc1841b83ada69d5b8b7582fcdb6a` | 57,325 | 1 |
| `experiments/source_lock.json` | `45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232` | 45,607 | 1 |
| `notes/BUILD_R0_BLOCKER.md` | `4b5f88b9f31fb60366d3f294917be43cb466a44946ea0c9c9a89e70e4f14de5e` | 3,447 | 59 |
| `notes/CITATION_VERIFICATION.md` | `66558b974ebdcc0fd7627c52c4caee0c80b404514d06f622ededd9b9a8900fb9` | 6,694 | 93 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `28f8f3dd6add8617a63c16b5d6956d5a1214dc453a2416721dca824faba00dc5` | 7,040 | 114 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `4d642580cad2dec337249cb0a11acbb662ae640a8d5faf44077f6ec2be354d68` | 20,521 | 483 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_BUILD_REPAIR_REVIEW.md` | `ea520dea141a3334231bf0c3d577bb1d7fb13c833432b1f49892d3336171c8b6` | 19,297 | 472 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `c95698f426f9237eaabc44ff20c6961d09ed4c21bd69d6e077d292de94481e89` | 23,203 | 567 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `e91bcda341469dfbb877d70fe0daeace876570b3696ef6fc0b881851fe7c9075` | 21,751 | 435 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `c11b139759e7951ee5e13617537f60caaad04124638c9c64b95e5071af334972` | 10,735 | 240 |
| `notes/INDEPENDENT_R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_REVIEW.md` | `8a7771c3a19c35a785bc6aa279bf2675fb6b6fe184c6341a29ef07b496fbaa30` | 17,766 | 302 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8` | 16,630 | 490 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `a420a26fbf3a535aedafdfd701969db8084b932e2ae9e6d806570c460090abea` | 24,533 | 754 |
| `notes/NOVELTY_ASSESSMENT.md` | `e873bcdc57c0f39e04b950bf9221c894993370c1accd313cbcb05495fa92fb2c` | 5,532 | 119 |
| `notes/PROOF_PACKAGE.md` | `b6df4be9e9a00a5ae71e48505b007a59fea70bcff3046661af804714378963bf` | 18,290 | 1,048 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `c0354c4621afcdfe79d5bddad035b378f6a4917e4c69a570971419ef5e80f762` | 46,832 | 1,331 |
| `notes/RESEARCH_QUESTION.md` | `5dc091d3500800610360512f464a877adb51c1f83857c8335a28dccebd35ef7d` | 5,052 | 132 |
| `paper/BUILD_EVIDENCE_SUPPLEMENT_R0.json` | `3a54b0667937df9c06720528c88d8bb904fbb2c2b177b132fb58c607b21815b7` | 35,512 | 1 |
| `paper/BUILD_METADATA_R0.json` | `0d91c80183c9532bd4b3f0353277af9c2f5bcc5efdf7a9bd427ee45de3eed2a7` | 12,124 | 1 |
| `paper/BUILD_RECEIPT_R0.json` | `7d34e1e952af185920f78736c71dd03c7c8242dd3f18a4360abfffbfbe7e8a57` | 3,360 | 1 |
| `paper/PAPER_PLAN.md` | `ee5c320f800919543411b147b5d1484d33c577a56519121b9b4883fdff8122ad` | 36,690 | 586 |
| `paper/main.aux` | `d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf` | 13,965 | 138 |
| `paper/main.bbl` | `b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855` | 3,371 | 78 |
| `paper/main.blg` | `04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535` | 900 | 46 |
| `paper/main.log` | `ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08` | 28,421 | 733 |
| `paper/main.out` | `02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d` | 6,374 | 23 |
| `paper/main.pdf` | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 |
| `paper/main.tex` | `0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f` | 77,196 | 2,004 |
| `paper/main_round0.pdf` | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 |
| `paper/math_commands.tex` | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 |
| `paper/references.bib` | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 |
| `refine-logs/FINAL_PROPOSAL.md` | `bf04aa95c67b19bc876c594b8162534c7000f12a92fc696017d36bf9cf7e96bf` | 4,773 | 175 |
| `refine-logs/INITIAL_PROPOSAL.md` | `7e5d64d5c4d3029d8d9d10f82c5dee41e66c5c2fb9cc3271e203657eeb74a8dc` | 3,971 | 148 |
| `refine-logs/REVIEW_SUMMARY.md` | `b2357b00fb2a9e05dbc96db775be9ef6a243e164b5b720525ecef9b3bd220c82` | 4,233 | 102 |

The original deterministic builder, the retrospective supplement author,
and this fresh R1 reviewer are distinct roles. The prior zero-write R1
reviewer did not author the supplement and later independently reviewed that
supplement; this fresh full reviewer is a new role and does not inherit that
reviewer's verdict. The repaired-source author/reviewer chain also precedes
and is separate from the builder. The exact opening manifest proves that the
conditional R1 artifact and `notes/BUILD_R0_REPAIR_BLOCKER.md` were absent;
it also contains no downstream R1 authorization/build, revision, release, or
Paper 25 artifact. Current governance keeps all such future work closed.

## Frozen source, immutable blocker, and scientific audit

The exact frozen source trio is:

| Project path | SHA-256 | Bytes | LF | Project inode |
|---|---|---:|---:|---:|
| `paper/main.tex` | `0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f` | 77,196 | 2,004 | 12,351,090,233 |
| `paper/math_commands.tex` | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 | 12,351,069,267 |
| `paper/references.bib` | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 | 12,351,069,268 |

Both retained roots contain byte-identical copies of all three files, and
every root copy is a distinct inode from its peer and project comparator.
The original formal source PASS artifact is
`notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md`, SHA-256
`c95698f426f9237eaabc44ff20c6961d09ed4c21bd69d6e077d292de94481e89`,
23,203 bytes / 567 LF, with terminal `PAPER_SOURCE_R1_PASS`; it bound the
pre-layout-repair main source at SHA-256
`1008cfa8c691d06645b79f33de00044df45e97a18b6d5a0f6ded2431f1df8f4e`,
67,011 bytes / 1,707 LF, and the same two companion files. The immutable old
failed-build blocker remains
`notes/BUILD_R0_BLOCKER.md`, SHA-256
`4b5f88b9f31fb60366d3f294917be43cb466a44946ea0c9c9a89e70e4f14de5e`,
3,447 bytes / 59 LF, terminal `R0_BLOCKED`. The fresh repaired-source PASS is
`notes/INDEPENDENT_PAPER_SOURCE_R1_R0_BUILD_REPAIR_REVIEW.md`, SHA-256
`ea520dea141a3334231bf0c3d577bb1d7fb13c833432b1f49892d3336171c8b6`,
19,297 bytes / 472 LF, terminal
`PAPER_SOURCE_R1_R0_BUILD_REPAIR_PASS`, and binds the current trio.

I read and checked the current source rather than relying on those PASS
tokens. The article has one abstract, eight numbered sections, exactly three
tables, zero figures, zero appendices, six explicit hypotheses in the
conditional lemma, 78 unique labels, and 122 resolved references. There are
no primitive `\over` fractions. The corrected symplectic-shear signs are
literal: the lower shear has `H-H^T` and the upper shear has `H^T-H`.

The main theorem is over an arbitrary characteristic-zero field, for
integers `m>=2`, `s>=1`, and arbitrary nonzero `A,B,C,D`. It defines

`V_m=A q_1^m q_2^2+B q_1 q_2^(2m)`,
`W_(m,s)=C p_1^(s(2m+1)+1)+D p_2^(sm+1)`,
`S(q,p)=(q,p+grad V_m(q))`, `T(q,p)=(q+grad W_(m,s)(p),p)`, and
`F_(m,s)=T o S`.

Direct algebraic expansion verifies all five theorem parts: polynomial
automorphism and symplecticity; strict alternating selectors
`A_-,A_+,A_-,A_+,...` from the ordinary seed with no wall iterate; strict
two-phase temporal carry and nonzero top-form survival for every allowed
coefficient choice; visibility of the first position coordinate against the
other three coordinates; and the monodromy/degree laws. With
`B_m=diag(2m+1,m)` and `P_m=(B_m A_+)(B_m A_-)`, the exact vector laws are

`u_(2j)=(s^2 P_m)^j(1,1)^T` and
`u_(2j+1)=s B_m A_- (s^2 P_m)^j(1,1)^T`.

The two eigenvalues are
`H=m^2(2m+1)^2` and `L=2m(m+1)`, with `H>L>0`, so
`lambda_1(F_(m,s))=sm(2m+1)`. The stride-two recurrence is

`d_(n+4)=s^2(H+L)d_(n+2)-s^4HLd_n`,

with
`d_0=1`, `d_1=2m(2m+1)s`,
`d_2=2m(m+1)(2m-1)(2m+1)s^2`, and
`d_3=8m^4(m+1)(2m+1)s^3`.
The signed wall gaps are exactly
`u_(2j,1)-2u_(2j,2)=-(s^2L)^j` and
`u_(2j+1,1)-2u_(2j+1,2)=2ms(s^2L)^j`.

Writing `Delta=4m^3+4m^2-m-2`, the checked parity formulas are

`u_(2j)=s^(2j)/Delta * [2(m+1)(2m^2-1)H^j(2,1)^T + L^j (-(2m+1)(2m^2+m-2),m)^T]`,

`d_(2j)=s^(2j)/Delta * [4(m+1)(2m^2-1)H^j-(2m+1)(2m^2+m-2)L^j]`,

and

`d_(2j+1)=2m(2m+1)s^(2j+1)/Delta * [2(m+1)(2m^2-1)H^j+mL^j]`.

The denominator creates no arithmetic assumption: integrality follows from
the integer matrix law, equivalently from the recurrence and initial data.
Independent multiplication also verifies `tr(P_m)=H+L`,
`det(P_m)=HL`, eigenvectors `(2,1)^T` and
`(-(2m+1)(2m^2+m-2),m)^T`, the seed decomposition, the odd-prefix
coefficients, and the wall left-eigenfunctional.

The bounded structural lemma is correctly limited to its crossed-binomial /
diagonal-pure-power ansatz. For wall `R` and common support value
`L_wall`, global open-chamber exchange holds if and only if
`e/f=R(L_wall-1)/(L_wall-R)`; its branch derivative has the required strict
negative sign. The specialization gives `R=2`, `L_wall=2m+2`, and precisely
`(e,f)=s(2m+1,m)`. The conditional period-`k` lemma is explicitly
technical and requires all six separate hypotheses: unique strict faces,
strict temporal carry, nonzero domain survival, linear transport in temporal
order, total-degree visibility for every residue, and Perron-class
spectral-circle visibility/noncancellation. Only after those hypotheses does
it conclude `u_(k ell+j)=D_j M^ell u_0`, the residue recurrences, and
`lambda_1=rho(M)^(1/k)`.

The source makes no assertion on the wall, in positive characteristic, for a
vanishing coefficient, for added supports, or for reversed phase order. It
does not claim inverse-degree equality, any entropy equality, integrability,
nonintegrability, generic dynamics, periodic-point or arithmetic-orbit
results, nonconjugacy, arbitrary selector words, arbitrary shear words,
period greater than two realizations, automaton realization, or novelty of
the conditional lemma. It makes no firstness or priority claim. The citation
roles remain contextual rather than proof transfer. Title, rendered
`Anonymous`, empty date, source comments, bibliography, public/private
firewall, and venue/identity exclusions all pass with no drift or leak.

## Both retained successful roots and deterministic execution

The exact successful roots are `/tmp/paper24-r0-repair-A.F4nzXg` and
`/tmp/paper24-r0-repair-B.k4LK3V`. Root A is mode `0700`, inode
11,825,646,800, link count two; root B is mode `0700`, inode 12,351,200,848,
link count two. Each is a flat inventory of exactly 17 regular files, zero
child directories, zero symlinks, and zero other objects. Every file is mode
`0644`, link count one. The basename/content u64 framing is 677,746 bytes in
each root and has common SHA-256
`ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145`.

The full root inventory, including distinct inode evidence, is:

| Name | Role | SHA-256 | Bytes | LF | A inode | B inode |
|---|---|---|---:|---:|---:|---:|
| `main.aux` | final output | `d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf` | 13,965 | 138 | 11,825,646,809 | 12,351,200,854 |
| `main.bbl` | final output | `b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855` | 3,371 | 78 | 11,825,668,960 | 12,351,200,860 |
| `main.blg` | final output | `04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535` | 900 | 46 | 11,825,668,957 | 12,351,200,859 |
| `main.log` | final output | `ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08` | 28,421 | 733 | 11,825,646,808 | 12,351,200,853 |
| `main.out` | final output | `02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d` | 6,374 | 23 | 11,825,646,810 | 12,351,200,855 |
| `main.pdf` | final output | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 | 11,825,668,792 | 12,351,200,856 |
| `main.tex` | source copy | `0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f` | 77,196 | 2,004 | 11,825,646,801 | 12,351,200,849 |
| `math_commands.tex` | source copy | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 | 11,825,646,802 | 12,351,200,850 |
| `pass1.merge` | command log | `bec6f982a2a245910fc3b4837a8fabf2f9ba8a4e76a1ce44119cb9c7ed502e29` | 19,722 | 662 | 11,825,646,805 | 12,351,200,852 |
| `pass1.status` | raw status | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 | 11,825,668,797 | 12,351,200,857 |
| `pass2.merge` | command log | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 | 11,825,668,952 | 12,351,200,858 |
| `pass2.status` | raw status | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 | 11,825,672,119 | 12,351,200,861 |
| `pass3.merge` | command log | `c83edf7c33f7ed55db7cf21a3af62abd9620cb112ba687815ab131c3676f0e59` | 8,971 | 174 | 11,825,672,120 | 12,351,200,862 |
| `pass3.status` | raw status | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 | 11,825,672,121 | 12,351,200,869 |
| `pass4.merge` | command log | `f14da56a798e2af44e178401bac6b5579f82b3ff65325fcc79e0d225e6114e6b` | 7,837 | 130 | 11,825,678,359 | 12,351,200,871 |
| `pass4.status` | raw status | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` | 1 | 0 | 11,825,678,360 | 12,351,219,448 |
| `references.bib` | source copy | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 | 11,825,646,804 | 12,351,200,851 |

Every corresponding A/B file is byte-equal and inode-distinct. The three
source copies and six final outputs also equal their exact project
comparators, whose inodes are distinct. Project `main.pdf` and
`main_round0.pdf` are byte-equal but inode-distinct (12,351,222,016 and
12,351,222,017).

Each root records exactly this single four-command sequence, with no retry:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

The exact locked environment is `PATH=/usr/bin:/bin`,
`SOURCE_DATE_EPOCH=1787616000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
`LC_ALL=C`, and `LANG=C`. The epoch is 2026-08-25 00:00:00 UTC and agrees
with the final transcript. Read-only local toolchain identity checks agree
with the retained logs: pdfTeX `3.141592653-2.6-1.40.22`, executable SHA-256
`01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`,
and BibTeX `0.99d`, executable SHA-256
`c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`.

All eight status files contain exactly the one raw ASCII byte `0`, no LF,
and therefore the displayed common SHA-256; independently decoding them
gives exit vectors `[0,0,0,0]` in both roots. The four merged logs have the
exact identities in the inventory and link to the commands/statuses in the
same indices. The exhaustive 17-name inventories contain no `pass5`, no
fifth status/log, no retry record, and no unaccounted output.

## Original JSON records, supplement, and history reconstruction

The immutable originals are:

| Record | SHA-256 | Bytes | LF | Inode |
|---|---|---:|---:|---:|
| `paper/BUILD_METADATA_R0.json` | `0d91c80183c9532bd4b3f0353277af9c2f5bcc5efdf7a9bd427ee45de3eed2a7` | 12,124 | 1 | 12,351,219,449 |
| `paper/BUILD_RECEIPT_R0.json` | `7d34e1e952af185920f78736c71dd03c7c8242dd3f18a4360abfffbfbe7e8a57` | 3,360 | 1 | 12,351,219,450 |

I traversed both complete materialized value trees and compared every live
source, root, command, environment, log, output, persistence, inventory,
blocker, identity, and external-effect field with the current allowed
objects. Metadata has 10 top-level keys, 382 key occurrences, and 328 leaves;
receipt has nine top-level keys, 84 key occurrences, and 75 leaves. Every
value is internally and externally consistent. Metadata truthfully has
top-level `status=BUILD_R0_REPAIR_PASS`. Receipt truthfully has no top-level
`status`; only `this_repair_build.status=BUILD_R0_REPAIR_PASS`. That original
absence is transparent and has not been repaired in place.

I validated metadata, receipt, and supplement with two independent strict
implementations: a duplicate-aware integer-only Python parser/canonical
encoder, and a separately written recursive-descent Node parser with a
Unicode-code-point-sorted encoder. Each parser reproduced each original byte
string exactly: one UTF-8 object, recursively sorted keys, compact separators,
one physical record, exactly one terminal LF, and no BOM, CR, NUL, duplicate
key, nonfinite value, float, exponent number, negative zero, malformed UTF-8,
surrogate, trailing record, or noncanonical whitespace/order. Independent
adversarial suites rejected 22/22 Python cases and 23/23 Node cases,
including literal and escape-equivalent duplicates and every listed numeric,
encoding, ordering, separator, root-type, and record-boundary failure.

The retrospective supplement is
`paper/BUILD_EVIDENCE_SUPPLEMENT_R0.json`, SHA-256
`3a54b0667937df9c06720528c88d8bb904fbb2c2b177b132fb58c607b21815b7`,
35,512 bytes / one LF, inode 12,351,222,021. I read and recomputed the full
21-top-level-key tree: 162 objects, 22 arrays, 475 integers, 93 booleans, two
nulls, 1,118 object-key occurrences, 1,072 leaves, and 1,620 strings when
keys are counted. Its self SHA/byte fields are null. It explicitly and
truthfully states `retrospective=true`,
`contemporaneous_with_build=false`, and `history_rewrite=false`; its own
top-level status is `BUILD_R0_REPAIR_PASS_EVIDENCE_SUPPLEMENTED`, while it
records the original receipt's top-level-status presence as false.

Using the declared frame
`u64be(path_utf8_length)||path_utf8||u64be(content_length)||raw_content`
over UTF-8 byte-sorted paths, I independently obtained:

| Universe | Entries | Framed bytes | SHA-256 |
|---|---:|---:|---|
| Build opening project | 25 | 475,261 | `05bb3276fcf370c4e8791059dd1e6b010b9b1a02b635ad34672452068cfe1b30` |
| Opening 25 plus exact success 9 | 34 | 1,556,510 | `3e6dd57462806de2bb61d958933472e8418e2074e3959fac06487e8c46fc6fba` |
| Retained root A | 17 | 677,746 | `ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145` |
| Retained root B | 17 | 677,746 | `ceb33e75c2faf8baeca3b6f4c361bb29b46f51d0b665c5fc67c43ce1391b1145` |

The embedded opening 25 and success 9 are disjoint, every path/hash/byte/LF/
mode/inode/link field matches live evidence, and their union is the exact
pre-supplement 34-file universe. The eight raw status records bind their
one-byte files, decoded zero, commands, indices, and exact merged logs. No
field substitutes an assertion for the raw evidence.

I reconstructed the complete governance history from current bytes by
unique exact line replacements and unique suffix/addendum removal, then
reattached every removed segment and reversed every replacement to reproduce
the source bytes. The independently reproduced stops are:

| Stop | Status SHA-256 / bytes / LF | Idea-report SHA-256 / bytes / LF |
|---|---|---|
| Current fresh-R1 opening | `c5843ac6844abbc8e059b1db7f0f9ef960b509ffbb030471da2d43d3d554e699` / 159,266 / 2,315 | `321ced6f6fdb76a08b326bf42a24410464bfc5b32e52bc24ebf4cf1276dc90a2` / 267,021 / 5,181 |
| Supplement-review opening | `18199d5d32038c580e4ccec49cdee89fb2c13cbd32de9fe5806239d2312a3932` / 157,094 / 2,284 | `59e97d2df82bd4af0e5c98ea9e59616ff2e933d3b98e77aaac4031b9819ee707` / 264,645 / 5,137 |
| Supplement-author opening | `6d5ee61df1e1c0746e7cf45ec787b94bf319ce5f621f4c6d26febb371b61184c` / 154,809 / 2,252 | `59cffa564d09c2be63083984bfea837e4ba9ad5d1172dcd172dfcfa99782dd9e` / 261,766 / 5,085 |
| Original R1-review opening | `90d26e127a441a62892e69c8a0bef50fde5b0a795f24d1e2280e38bb8e674ab8` / 151,769 / 2,211 | `2605da86f5188cb3d42bcff820f4f1b91743cbdd5dc81ac92f675e74016c05d1` / 258,117 / 5,019 |
| Build-time stop | `bb3aae0ec08cfaafae0036615be4a845c3b50aef739fc29adb0f49791b201d9f` / 148,830 / 2,169 | `170e7b99755a26b37ed67b63e79e24183e86248a71d2382e42405a5fe9bc6c4d` / 254,437 / 4,953 |

For the current-to-supplement-review transition, the removed STATUS activity
segment is SHA-256
`db60bfee74b62e58d674c57ad0c72e81c55ebfd10bcad5e2514f20c43a9782c1`,
2,176 bytes / 31 LF, and the removed IDEA addendum is SHA-256
`fa7cca6e2802526cf97de92ebcecc0de558a3745454a125f067fb44781961aae`,
2,376 bytes / 44 LF. The former gate and queue literals used for that STATUS
reversal were supplied from the parent's contemporaneous historical
readback; I did not trust their provenance alone, but independently verified
them by the full resulting `18199d5d...` identity and exact forward
reattachment.

For the supplement-review-opening to supplement-author-opening transition,
the removed STATUS segment is
`3322b11969391f79f343e3f20124ab99693c44474979ec62f10f808d81d8f071`,
2,295 bytes / 32 LF, and the IDEA addendum is
`ec78ee7d5ddff2fa2b91a9171ec230c0b233dc0d7a2412d9d7ed252bc186b089`,
2,879 bytes / 52 LF. From author opening to original R1 opening, the removed
STATUS and IDEA segments are respectively
`052621366bf40cf31ef8bb14d9c9c32ac6759867f59905a204f6fae1248a4043`,
3,018 bytes / 41 LF, and
`2391cb87784579fe3ee9d6aa6911fdd27b8001f5a2d93b2c7a394f596ca5deb4`,
3,649 bytes / 66 LF. From original R1 opening to build time, they are
`030a8d33a778a839ce5167785bbbd75f111e2a2bc64eb9715dc96cf181f874f7`,
2,943 bytes / 42 LF, and
`90351b22fa71f034e1b7436a4ed178c3b37346c1d183e74f465b832e2952ea45`,
3,680 bytes / 66 LF. Every marker and replaced line occurred exactly once.

Thus the build-time and original R1 identities are historical
reconstructions, not current-file claims. The supplement-author identities
were current at author opening, not at build time. The supplement does not
rewrite history or pretend that it existed contemporaneously.

The independent supplement review is exact at
`notes/INDEPENDENT_R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_REVIEW.md`, SHA-256
`8a7771c3a19c35a785bc6aa279bf2675fb6b6fe184c6341a29ef07b496fbaa30`,
17,766 bytes / 302 LF, with unique terminal
`R0_REPAIR_BUILD_EVIDENCE_SUPPLEMENT_PASS`. Its opening 35-file sorted
manifest is 3,622 bytes / 35 LF at SHA-256
`108803b392fac0cd985c00924ac5f346e5c1ce069a087ec7c3d773d8b149a476`,
and the review is the sole 35-to-36 delta. Reading all 302 lines and
recomputing its claims confirms 4/4 prior blocker closures: all eight raw
statuses, full historical ledgers, the exact opening-25 manifest, and
truthful supplement-layer status closure while preserving the original
receipt's missing top-level status.

## Final logs, citation closure, and outputs

The six final outputs have these common A/B/project identities:

| Output | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| AUX | `d77042650271b25bfa792e5b27dc96fed32d516234821378b9621cf104175daf` | 13,965 | 138 |
| BBL | `b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855` | 3,371 | 78 |
| BLG | `04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535` | 900 | 46 |
| LOG | `ea9b19673c855fe1f927fe84ca7000affbb488ec2cd26a0bcfba8b6dec74dc08` | 28,421 | 733 |
| OUT | `02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d` | 6,374 | 23 |
| PDF | `27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22` | 506,215 | 2,820 |

Final LOG, AUX, BBL, BLG, and OUT inspection finds zero TeX errors, undefined
references, undefined citations, rerun requirements, missing glyphs,
overfull boxes, or BibTeX warnings. The final log contains exactly five
underfull hbox diagnostics, all at the Table 2 construction around source
line 730. The affected labels are `Carried momentum degrees`, two
`Negative chamber` labels, `Positive chamber`, and `Negative visibility
equality`. High-resolution page-9 inspection shows only harmless widened
label spacing/hyphenation: every label, inequality, rule, and symbol is
readable, with no collision, clipping, or margin defect.

The exact nine citation keys in source order are
`BellonVialletAlgebraicEntropy`, `HasselblattProppMonomialDegreeGrowth`,
`DangFavreSpectralInterpretations`,
`JaneczkoJelonekPolynomialSymplectomorphisms`,
`FordyHoneSymplecticCluster`, `FordyHoneClusterPoisson`,
`IshibashiKanoSignStableEntropy`, `BlancVanSantenAffineTriangular`, and
`ShaoSunDimensionFour`. Source citations, the nine BibTeX entries, nine AUX
`citation` keys, nine AUX `bibcite` keys, and nine BBL `bibitem` keys have
identical sets. AUX points to `references` and `plainnat`. No tenth entry,
missing key, duplicate item, or unresolved marker exists.

## PDF structure, security, anonymity, and visible content

The exact PDF is SHA-256
`27b0ec704e3bc7a2bafe30a27267a1e961b03d59756387098f4b866026089d22`,
506,215 bytes, 27 pages, PDF 1.5, letter size 612 by 792 points, and zero
rotation. Independent parser/render checks establish structural validity and
successful processing of every page. All 27 listed font resources are
embedded and subset. The PDF is not encrypted and contains no JavaScript,
open action, additional action, form/XFA, attachment, embedded file,
FileSpec, raster image, creation date, or modification date.

The PDF Title is exactly `Forced Period-Two Selector Exchange in Two-Mode
Hamiltonian Product Shears`. Author, Creator, and Producer are each empty;
Subject and Keywords are empty; creation and modification dates are absent.
The normalized visible title is exactly the same full title across its
harmless two-line wrap, followed by the visible author `Anonymous`, with no
visible date. Text and object scans find no private or governance path,
username, machine marker, Batch 06 identifier, hash, queue token, review
token, `VERIFY`, `??`, or `[?]` leak.

Text/layout extraction and visual inspection agree on exactly three tables,
zero figures, and nine numbered bibliography items. Pages 1--26 are the
content pages. Page 26 contains the complete conclusion. `References` is the
first content heading at the top of page 27, and all nine entries fit on that
page.

## Every-page visual inspection

I created exactly one fresh validation root,
`/tmp/paper24-fresh-r1-review.rxueFn`, retained it without cleanup, rendered
all 27 pages at 1,700 by 2,200 pixels, and inspected every page individually.
I additionally rendered and inspected pages 1, 9, 12, 26, and 27 at 2,550 by
3,301 pixels. The single-page rerenders rule out contact-sheet or thumbnail
cropping artifacts; the apparent page-12 suspicion in the overview was a
false alarm. Every page is nonblank and uncorrupted, with intact margins,
baselines, formula extents, rules, footers, and page numbers.

| Page | Content inspected | Visual result |
|---:|---|---|
| 1 | Exact title, Anonymous, abstract, Section 1 opening | Clean; title wrap, metadata-visible identity, equations, citations, margins pass at high resolution |
| 2 | Introduction and theorem setup | Clean; no clipping, overlap, crowding, or broken formula |
| 3 | Main theorem recurrence, wall gaps, parity laws | Clean; long displays and qualifiers fully visible |
| 4 | Section 2, literal phases, inverses, symplectic calculation | Clean; matrices and shear signs legible |
| 5 | Support-row derivation | Clean; aligned displays and prose remain inside margins |
| 6 | Table 1 and Section 3 opening | Clean; table rules, rows, caption, and branch formulas fit |
| 7 | Chamber branch algebra | Clean; fractions and implications are intact |
| 8 | Strict selector exchange | Clean; formulas, proof text, and page break pass |
| 9 | Table 2 and Section 4 opening | Clean at high resolution; all five underfull sites are harmless and readable |
| 10 | Temporal-carry proposition and proof | Clean; inequalities and aligned comparisons fit |
| 11 | Top homogeneous survival | Clean; no glyph loss, collision, or spill |
| 12 | Explicit top-form recursions and Section 5 opening | Clean at high resolution; overview suspicion was not a page defect |
| 13 | Visibility proposition | Clean; four-coordinate inequalities and proof are legible |
| 14 | Monodromy multiplication and eigenvectors | Clean; matrices and numbered displays fit |
| 15 | Spectrum and degree consequences | Clean; no clipped delimiter or equation number |
| 16 | Table 3 and Section 6 opening | Clean; full table fits with intact rules and readable ledger rows |
| 17 | Left eigenfunctional, wall gaps, parity derivation | Clean; displays and section headings fit |
| 18 | Parity formulas and integrality | Clean; long closed forms remain within the text block |
| 19 | Section 7 and bounded structural setup | Clean; no layout defect |
| 20 | Crossed-binomial ansatz and branch formulas | Clean; equations, labels, and prose fit |
| 21 | Structural criterion proof and specialization | Clean; ratios and implications remain legible |
| 22 | Conditional period-k lemma | Clean; six-hypothesis layout and formulas fit |
| 23 | Section 8 boundaries and wall/seed discussion | Clean; heading and text block intact |
| 24 | Arithmetic hypotheses and arbitrary nonzero coefficients | Clean; no overflow or missing symbol |
| 25 | Formal-versus-true laws, structural scope, anti-claims | Clean; headings, citations, and paragraphs fit |
| 26 | Priority boundary and Section 8.7 conclusion | Clean at high resolution; conclusion complete, deliberate lower whitespace harmless |
| 27 | References heading and bibliography items 1--9 | Clean at high resolution; heading begins at top, all nine items fit, URLs and diacritics legible |

Across all 27 pages there is no blank/corrupt page, clipped content,
overlap, bad margin, broken formula, malformed table, title defect, leaked
private text, or bibliography spill.

## Findings, permission boundary, and sole-write proof

Finding counts are:

- required/critical findings: 0;
- major findings: 0;
- minor findings: 0;
- cosmetic findings: 0;
- authority expansions: 0;
- prior provenance blocker subfindings closed: 4 of 4.

The audit used only exact allowed current governance roots, the Paper 24
project, the two exact retained successful roots, local read-only validation
tools/toolchain metadata, and the single fresh validation root named above.
It did not compile, invoke TeX or BibTeX, retry, edit source/build/evidence/
root/governance bytes, clean retained evidence, use the network, install a
package, open revision or R1 build work, release anything, touch Paper 25, or
cause an external effect. Excluded prior paths and roots were not accessed.

Immediately before this sole conditional write, the current governance roots
still had the opening identities, both retained roots still had their exact
17-file inventories and common `ceb33e75...` aggregate, the complete project
still matched the 36-row `ef6f0868...` manifest, this target was absent, and
the repair-blocker path was absent. This file is the only authorized and only
performed project write. Because the complete opening universe is bound
above and no preexisting path is changed, creation of this one regular file
makes the exact postwrite universe 37 regular files / four descendant
directories / zero symlinks / zero other objects, with the other 36 files
byte-identical to the opening manifest. The artifact's own SHA-256, byte
count, and LF count are necessarily postwrite external identity facts; they
do not require or authorize a self-referential second edit.

This PASS opens no downstream action by itself. Only a separate parent
governance transition may consume it.

BUILD_R1_R0_REPAIR_PASS
