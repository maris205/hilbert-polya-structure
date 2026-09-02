# Hostile Review B — P165 Low-Weight Support Shortening

**Frozen artifact reviewed:** Round 1 `main_round1.pdf`  
**Pinned PDF SHA-256:** `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a`  
**Independent verdict:** **ACCEPT_INTERNAL**  
**Severity:** **0 Critical / 0 Major / 0 minor**  
**Lifecycle:** **HOLD_EXTERNAL**

## 1. Independence, freeze, and scope

I did not author P165, did not participate in its revision, and did not use
the author or Review-A verifier as an implementation dependency.  I began
from the literal Round-1 map and theorem contract, rederived the claims, and
wrote a separate RREF/finite-field verifier.  I inspected Review A only
afterward to audit its requested-repair status and replay its evidence.

The pinned input record is
`docs/papers162_166_sequence/reviews/p165_b/PINNED_INPUTS.sha256`.
The current, Round-0, and Round-1 PDFs are byte-identical:

```text
main.pdf                    f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
main_round0_original.pdf    f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
main_round1.pdf             f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
main.tex                    bf245d0d0e968edf921af76bae15a77fc8068c3e196b0e880f48ec2a4e3275e4
references.bib              4e91997ae671fcade364a1057c31a7751aef863850f87df52e6277628df4b2a1
```

Review A returned `ACCEPT_INTERNAL — 0C/0M/0m` and requested no repair.
Thus this identity is the required no-change Round-1 freeze, not evidence of
an omitted author correction.

## 2. Principal theorem: independent hostile result

| claim | result | independent reason |
|---|---|---|
| strict descent | **PASS** | A minimum word has weight `d<2d`, hence belongs to the low set and cannot survive zeroing on its support. |
| nonzero distance doubling | **PASS** | A surviving nonzero word below `2d(C)` would simultaneously have support inside `U(C)` and vanish on `U(C)`. |
| unique recurrence and sharp height | **PASS** | Purge supports are pairwise disjoint and have sizes at least `1,2,4,...`; therefore depth `r` costs at least `2^r-1` coordinates.  Direct sums of full-support lines on dyadic blocks attain the bound. |
| every-time image iff for `D!=0` | **PASS** | Repeated doubling forces `d(D)>=2^t`; disjoint purges force `z(D)>=2^t-1`.  Conversely, adjoining dyadic full-support lines on zero coordinates of `D` deletes exactly one line per round. |
| inverse dimension/support lower bounds | **PASS** | The `t` inclusions are all proper, while the disjoint purge sets lie in `Supp(C)\Supp(D)`. |
| simultaneous-equality classification | **PASS** | Equality forces codimension one and `|U_i|=d_i=2^i` at every step.  A minimum word then has support exactly `U_i`, and the restriction kernel splits off its line.  Induction yields exactly the claimed disjoint direct sum. |
| prime-power exact count | **PASS** | Ordered labelled blocks give the factorial quotient.  An `m`-block supports `(q-1)^(m-1)` full-support lines; the total exponent is `(2^t-1)-t`. |

The complete cold derivation is in
`docs/papers162_166_sequence/reviews/p165_b/PROOF_REDERIVATION.md`.
No step assumes a prime field: the splitting and line count use only finite-
field linear algebra.

## 3. Boundary attacks

### Zero target

The main target theorem correctly assumes `D!=0`.  Zero remains in every
time image via the zero source, while its complete fibre is
`{C:tau(C)<=t}`, not the extremal count.  On the exact-depth-`t` slice, the
minimum dimension/support pair is `t, 2^t-1`; its simultaneous minimizers
are the same dyadic-line sources, with ambient `n` replacing `z(D)` in the
count.  Proof and exhaustive checks agree.

### Time and ambient zero

At `t=0`, `T^0` is the identity, both lower bounds vanish, and the empty
product counts the sole source `D`.  At `n=0`, zero is the only state and the
height is `floor(log_2(1))=0`.  Both conventions are explicit and correct.

### Full support and post-cap times

A nonzero full-support target has `z(D)=0`, so it has no positive-time
source.  If `2^t-1>n`, no nonzero target can meet the zero-coordinate
condition, although zero remains in the image.  The manuscript does not
incorrectly erase that zero state.

### Strict cutoff

The `<2d` boundary is essential and consistently used.  For disjoint
full-support lines of sizes one and two, the strict map leaves the second
line after round one, while the weak `<=2d` variant destroys it immediately.
The independent verifier records, for `F2,F3,F4,F5`, the corresponding word
counts `(4,2,1)`, `(9,3,1)`, `(16,4,1)`, and `(25,5,1)` for source, strict
successor, and weak successor.  No proof line silently uses the weak map.

## 4. Findings and repair requests

### Critical

None.

### Major

None.

### minor

None.

### Per-file repair list

- `main.tex`: no repair requested.
- `references.bib`: no repair requested.
- author support/evidence files: no repair requested.
- author verifier/canonical: no repair requested.
- `main.pdf` / `main_round1.pdf`: no repair requested.

I made no change to any author source, bibliography, support file, code,
canonical transcript, PDF, Review-A artifact, or Git state.

## 5. Independent exact verification and replays

Review-B evidence is under
`docs/papers162_166_sequence/reviews/p165_b/`.

```text
independent verifier SHA-256:
  987e913be21a91d7f612bf158f14d84c0b597950e215a870c4d0405280685b54
Review-B canonical/replay SHA-256:
  3a593364f3a30a18bf76fe1611dad2a8330a57772cd466afd8d672cda238da04
fresh Review-B replays: 2/2 byte-identical
assertions: 1,220,460
distinct labelled code states: 37,193
target-time interfaces: 215,030
transition digest:
  26f9a5289fff65e701ecfc0c18cb1d91271b652ca8f1067263497db1374ae8b7
```

The reviewer verifier imports neither author nor Review-A code.  It
enumerates subspaces from unique RREF matrices and materializes the literal
support-shortening map.  Complete boxes are:

- every `F2` code for `0<=n<=7`;
- every `F3` code for `0<=n<=5`;
- every code over the genuine nonprime field
  `F4=F2[a]/(a^2+a+1)` for `0<=n<=4`; and
- every `F5` code for `0<=n<=4`.

The `F4` addition/multiplication tables are native, not arithmetic modulo
four, and all field laws plus `a^2=a+1`, `a^3=1` are checked.  The program
tests Gaussian state totals, every literal transition and orbit, exact
heights, all tested target/time image cells, both inverse lower bounds, the
entire actual-versus-constructed equality-source set and count, zero-target
exact-depth minimizers, and every mandatory boundary.

For cross-checking only, the author verifier and the independent Review-A
verifier were also freshly replayed twice.  Both runs of each were
byte-identical to their own frozen canonical:

```text
author:   2/2; 605,733 assertions; output SHA-256
          0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd
Review A: 2/2; 1,574,098 assertions; output SHA-256
          66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7
```

These enumerations are falsification pressure, not all-parameter proofs or
ownership evidence.

## 6. Owner and internal-collision verdict

Jibril et al. directly own the neighboring low-weight hitting-set shortening
principle.  Their generalized protected range contains the one-step route
through weight `2d-1`; Grassl and White own nearby low-weight-support special
puncturing.  P165 cites both and explicitly assigns the entire one-step
shortening/distance-increase mechanism zero contribution credit.  A fresh
search also checked general finite-field shortening literature and found no
direct owner for the autonomous map or residual all-time/inverse conjunction.
This remains an owner-thin bounded non-hit, not a novelty claim.

The closest internal carrier is P109, but its map is the image under one
fixed nilpotent operator and its fibres are Gaussian-incidence fibres.  P137
is the closest clock silhouette, but it uses additive triangular resource
growth on abelian-group partition types.  P143 uses Boolean row inclusion;
P162 uses stochastic translation spans; P163 uses complemented shadows; and
P164 uses a fixed affine cellular tail on individual words.  None transfers
P165's adaptive low-weight support kernel, joint target
distance/zero-capacity criterion, or dyadic full-support-line rigidity.

The full P1--P165 audit and primary-source links are in
`docs/papers162_166_sequence/reviews/p165_b/OWNER_AUDIT.md`.  No literal or
proof-engine collision requiring revision was found.

## 7. Source-only builds and artifact QA

Two fresh directories received only `main.tex` and `references.bib`.  Each
completed `pdflatex -> bibtex -> pdflatex -> pdflatex`.  The settled logs,
`.bbl` files, and PDFs agree byte for byte, and both PDFs are byte-identical
to the Round-1 artifact.

```text
pages:                   4 (A4)
bytes:                   288,837
PDF SHA-256:             f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
font rows:               23
embedded/subset/Unicode: 23/23, 23/23, 23/23
rendered references:     3/3
settled warnings/errors: 0
BibTeX warnings:         0
```

The PDF is unencrypted, A4, has no form, JavaScript, custom metadata,
metadata stream, attachment, or signature.  Title/author/subject/keywords/
creator/producer metadata fields are empty.  Extracted text has an anonymous
byline and no identity leak, affiliation, email, ORCID, acknowledgement,
funding string, local path, or draft token.  The visible `HOLD_EXTERNAL`
statement is present.

All four pages were rendered at 150 dpi and inspected individually.  There
is no clipping, overlap, missing glyph, illegible formula, broken citation,
bad page break, or margin overflow.  Page 4's white area is the natural end
after references 2 and 3.  Full receipts are in
`docs/papers162_166_sequence/reviews/p165_b/BUILD_QA.md`.

## 8. Final recommendation

**ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 minor.**  The Round-1 theorem,
all mandatory exceptional cases, the true prime-power count, owner
subtraction, executable evidence, and built artifact survive fresh Hostile
Review B.  This is internal acceptance only.  Keep the manuscript anonymous
and maintain **HOLD_EXTERNAL**; it does not authorize posting, circulation,
submission, author contact, or a novelty/priority claim.
