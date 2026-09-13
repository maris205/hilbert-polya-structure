# Independent Paper 27 source-lock review (R3)

## Authorization and read boundary

This is the fresh independent source-lock review authorized by
`B07-E0078-P27-SOURCE-LOCK-CORRECTION-REVIEW-AUTHORIZATION-R3`.  I read
`BATCH_07_STATUS.md` first, verified its true-EOF parent, and then read only
the other 24 paths enumerated by E0078.  The complete input whitelist is
therefore exactly 25 paths (the 24 aggregate rows plus the controlled status
ledger):

1. `BATCH_07_STATUS.md`
2. `BATCH_05_FINAL_AUDIT.md`
3. `BATCH_05_IDEA_REPORT.md`
4. `BATCH_05_STATUS.md`
5. `BATCH_06_FINAL_AUDIT.md`
6. `BATCH_06_IDEA_REPORT.md`
7. `BATCH_06_STATUS.md`
8. `BATCH_07_CHARTER_REVIEW.md`
9. `BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R1.md`
10. `BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R2.md`
11. `BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R2_CORRECTION.md`
12. `README.md`
13. `docs/candidate_registry.md`
14. `papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_PLAN.md`
15. `papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_TRACKER.md`
16. `papers/27-positive-newton-translation-reciprocity/notes/CITATION_VERIFICATION.md`
17. `papers/27-positive-newton-translation-reciprocity/notes/CLAIMS_EVIDENCE_MATRIX.md`
18. `papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`
19. `papers/27-positive-newton-translation-reciprocity/notes/NOVELTY_ASSESSMENT.md`
20. `papers/27-positive-newton-translation-reciprocity/notes/PROOF_PACKAGE.md`
21. `papers/27-positive-newton-translation-reciprocity/notes/RESEARCH_QUESTION.md`
22. `papers/27-positive-newton-translation-reciprocity/notes/SOURCE_LOCK.md`
23. `papers/27-positive-newton-translation-reciprocity/refine-logs/FINAL_PROPOSAL.md`
24. `papers/27-positive-newton-translation-reciprocity/refine-logs/INITIAL_PROPOSAL.md`
25. `papers/27-positive-newton-translation-reciprocity/refine-logs/REVIEW_SUMMARY.md`

The only permitted write is this review artifact.  I used no recursive search,
glob, parent-directory traversal, unlisted path, network, build, compiler,
CAS, numerical run, cache-producing action, copy, cleanup, or external effect.
No file was changed before this single artifact write.

## E0078 true-EOF and parent binding

The physical status ledger is a regular file, mode `0644`, link count `1`,
with 272357 bytes and 5338 LF bytes.  It is strict UTF-8, has no BOM, CR, or
NUL, and has exactly one terminal LF.  Its current SHA-256 is
`0c830471d53698858c39cc1f9b6ae64665c1c49bbe2e28dc9583c24da34a587c`.

The first 269075 bytes (the E0078 `parent_ledger_bytes` value) hash to
`44262092be6a8c2e4c7139c35ffaa6065e1fe5f42bb1ab51ed1a7800dd752ab2`, exactly
the E0078 `parent_ledger_sha256`.  That prefix ends with the complete line
`BATCH07_PAPER27_SOURCE_LOCK_CORRECTION_AUTHOR_STOP_R3`; the next bytes begin
the E0078 heading, so the authorization is appended at physical EOF with no
intervening or trailing parent bytes.  The E0078 machine fields are
internally consistent: `seq: 75`, `manifest_rows: 24`,
`manifest_framing_bytes: 3230`, `manifest_lf: 24`, serialization token
`path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>`, and identical pre/post
manifest digest
`1e52c70fd0804f04e78dd4b0dbe6b522bd4f0e40a5bdba3a37a3fdcd3faed158`.
The authorized reviewer role, full whitelist, sole allowed create path,
candidate ID, next gate, and final authorization marker all agree with the
true-EOF event.

## Physical census of the 24 aggregate rows

Every listed aggregate row is a regular, non-symlink file with mode `0644`
and link count `1`; all passed strict UTF-8, LF-only, no-BOM, no-CR, no-NUL,
and exactly-one-terminal-LF checks.  The independently measured identities
are:

| Relative path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `BATCH_05_FINAL_AUDIT.md` | 17937 | 325 | `3e583ac5a989a689b93da3a6a6a74ac42e37f2caaa2b6601c7ca14e37d46de3e` |
| `BATCH_05_IDEA_REPORT.md` | 54677 | 1067 | `e697b0b5e252a42b08363548316ffdea620dec57f7970d106b06e7f6b54cfa46` |
| `BATCH_05_STATUS.md` | 63905 | 925 | `296cbbbde7df633de5f995285b3878477487f5ac8ac1032077cac1aa35bf4e1e` |
| `BATCH_06_FINAL_AUDIT.md` | 25301 | 436 | `8f28253a94918a6ab0c6934ce167c3d6129deadc50e7f41d46136dce8b19c1f3` |
| `BATCH_06_IDEA_REPORT.md` | 675259 | 12068 | `2e097d928bbe695866653c47aace6215358e0187326044e8eb548fddd3cd1ef3` |
| `BATCH_06_STATUS.md` | 616461 | 9095 | `5c95ac0f195ae7de935b0c2cc902ebcf6df15f0cb7292835d1c51ea208d45609` |
| `BATCH_07_CHARTER_REVIEW.md` | 20209 | 364 | `4ced8ab1e1b48d89ec088be40206bf3bbff3e23c77471c45672442883b322f73` |
| `BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R1.md` | 18431 | 377 | `0ec08ac6a8cfc25548f213a132855aec58618c3c488a459083e5059a59da32ff` |
| `BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R2.md` | 13329 | 304 | `59cbcbd71b634534f4a84ede34a46a447bab31041ad4e71e87c7c847b9295f2f` |
| `BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R2_CORRECTION.md` | 16395 | 374 | `da719d459bb9fbcc925ef3c38adf5021af9a8961db82516cc416843ecd885106` |
| `README.md` | 9594 | 41 | `415bc57e4d2e87bcf078b969c7edf0c769f436d1ff41cfca1619f37540222cda` |
| `docs/candidate_registry.md` | 17936 | 41 | `27f43be37659125f6a9ed2183772325da83acea1239aed22fe71d9494a54b77b` |
| `papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_PLAN.md` | 4928 | 108 | `1b9628e18703fd2332c90799c71abaaa42467b7080cb35a59ab3617b1c4c9a9d` |
| `papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_TRACKER.md` | 3116 | 52 | `bbd8ec0ebdd866fb09174b65dd87075623fae78eba48e96aaccc4625deb45e8e` |
| `papers/27-positive-newton-translation-reciprocity/notes/CITATION_VERIFICATION.md` | 9366 | 61 | `1a54b62d83cd6861679f851ec509854d6ed83eb046d5b6db7343b6e96aa9c26b` |
| `papers/27-positive-newton-translation-reciprocity/notes/CLAIMS_EVIDENCE_MATRIX.md` | 6022 | 43 | `b0415cf8118b6e33352d513e170f5c2ad854e54a3ba854d683faca3eb6425b14` |
| `papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 11229 | 231 | `4fdf61878bc78315f42d07b4a4d565d9fe154910c3fa50e49a4c234867b0dbed` |
| `papers/27-positive-newton-translation-reciprocity/notes/NOVELTY_ASSESSMENT.md` | 6040 | 81 | `16b97ac1e7df048e1eb2d05f69980064f8201cf56a878bbd496831d20eec647c` |
| `papers/27-positive-newton-translation-reciprocity/notes/PROOF_PACKAGE.md` | 19921 | 527 | `c583d2cedcd97bef8410172bed967dfe99bcaf9caa69595c305bbf36ccd51fd1` |
| `papers/27-positive-newton-translation-reciprocity/notes/RESEARCH_QUESTION.md` | 4908 | 126 | `73b094e1905f4a5af49c82f3b3bfa7a242125e56ff724dcf00c1c8bb1a0ea4cc` |
| `papers/27-positive-newton-translation-reciprocity/notes/SOURCE_LOCK.md` | 9328 | 177 | `ab63ffebbc62149daa0db70f4378cd59604c4c24c201b70036e96f831b9560c6` |
| `papers/27-positive-newton-translation-reciprocity/refine-logs/FINAL_PROPOSAL.md` | 5446 | 131 | `d2bd1a47959907efa35364e408ede645353059a47cb3641226f5d022605a71ae` |
| `papers/27-positive-newton-translation-reciprocity/refine-logs/INITIAL_PROPOSAL.md` | 3525 | 75 | `af290d3d3587d6824cbe1c892d3b11c8551113d63c5fe03c1f641967af75e3e6` |
| `papers/27-positive-newton-translation-reciprocity/refine-logs/REVIEW_SUMMARY.md` | 4064 | 76 | `3805351516268043f6a3a91c35dc6568428849ad8fbdde33fc9872eef06e7836` |

The physical table agrees with the table in `SOURCE_LOCK.md` for its eleven
project source-design inputs and with the frozen inherited identities.  The
status ledger is deliberately not an aggregate row.

## Independent aggregate reconstruction

I serialized each row as one UTF-8 line, sorted by bytewise relative path,
using exactly the event-local unpadded-octal token `644` for physical mode
`0644`:

    path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>

Excluding `SOURCE_LOCK.md` gives the retained 23-row source-design aggregate:
3079 framing bytes, 23 LF, SHA-256
`b86617e99feee6b6c287260fc903d800c29a9673c22e5b6f414147644cf19670`.
Adding the measured lock row gives exactly 24 rows, 3230 framing bytes, 24
LF, SHA-256
`1e52c70fd0804f04e78dd4b0dbe6b522bd4f0e40a5bdba3a37a3fdcd3faed158`.
This equals both E0078 pre/post manifests.  The historical R2-correction
row is bound by the independently measured digest
`da719d459bb9fbcc925ef3c38adf5021af9a8961db82516cc416843ecd885106`.
No padded `0644` token was mixed into this event-local aggregate.

## Lock identity and corrected addenda

`SOURCE_LOCK.md` itself is regular mode `0644`, link-one, strict UTF-8 and
LF-only, with no BOM, CR, or NUL, exactly one terminal LF, 9328 bytes, 177 LF,
and SHA-256
`ab63ffebbc62149daa0db70f4378cd59604c4c24c201b70036e96f831b9560c6`.
Its Section 14 typed-definition correction makes the u-only cone and the
pair cell distinct: all inequalities involving `w`, `Rw`, or transformed
pairs belong to the typed pair-gap predicate, not the u-only cone.  Its
reflected cell is checked after the state swap.  The proof package carries
the same typed correction, so source and lock semantics agree.

The final Section 15 administrative correction is present and unambiguous:

    E_V and E_W are finite nonempty subsets of Z_{>=2}^r, with r >= 3.

It explicitly says that the review whitelist has 25 paths (24 aggregate rows
plus `BATCH_07_STATUS.md`), that the aggregate still has 24 rows because the
status ledger is excluded, and that the project has twelve files (eleven
source-design inputs plus `SOURCE_LOCK.md`).  Section 14 and Section 15 are
append-only clarifications; no earlier byte is silently rewritten.  The two
malformed support-rendering tokens in the preceding lock prose are therefore
superseded without changing the scientific theorem or any aggregate row.

The source-design review digest and pre-lock aggregate in the lock agree with
the independently measured review row and 23-row reconstruction.  The source
lock's post-lock row accounting is exactly 12 inherited rows + 11 project
source-design rows + 1 lock row = 24.  The controlled ledger remains outside
that aggregate.

## Independent theorem-contract and source-design audit

### Family, transport, and survival

The locked family is over a characteristic-zero field K with finite,
nonempty, collected supports E_V and E_W contained in Z_{>=2}^r, r >= 3,
and nonzero coefficients.  Real positive degree vectors are separate from K.
For

    S_V(q,p) = (q, p + grad V(q))
    T_W(q,p) = (q + grad W(p), p)
    F = T_W o S_V

the inverse order is `F^{-1} = S_V^{-1} o T_W^{-1}`, with subtraction in
both inverse shears.  For unique exposed selectors alpha and beta,

    A_alpha = 1 alpha^T - I
    B_beta  = 1 beta^T - I
    v = A_alpha u
    u' = B_beta v

and the strict fresh/carry inequalities separate new gradient blocks from old
blocks.  The grouped Hessian witness is

    det[ alpha_i (alpha_j - delta_ij) ]
      = (-1)^r (1 - |alpha|) product_i alpha_i,

which is nonzero under the locked positive-support and characteristic-zero
hypotheses.  A generic secondary minimizer makes the all-minimizer tuple the
unique lowest determinant group; the Jacobian criterion and injective
substitution then give coefficient-uniform leading-form survival.  The same
argument, with nonzero inverse signs, applies to the reflected inverse phase.

### Translation, wall count, and affine tail

For an exposed alpha and beta,

    v = h_V(u) 1 - u,
    u' = h_W(v) 1 - v = u + delta 1,
    delta = h_W(v) - h_V(u) > 0.

For an integer seed, all matrices and carries are integral, so a strict delta
is at least one and `u_n = u_0 + t_n 1` with `t_0 = 0` and increasing t_n.
Putting `g(t) = h_V(u_0 + t 1) - t` gives a strictly increasing envelope,
because every support total minus one is positive.  W score differences are

    (beta - eta) . v(t)
      = (|beta| - |eta|) g(t) - (beta - eta) . u_0.

Unequal-total walls cross at most once and equal-total differences are
invariant, yielding at most `d_V + d_W - 2` selector changes on an infinite
strict branch.  After the final change, with
`c = (|beta|-1) alpha - beta`,

    t_{n+1} = lambda t_n + mu,
    lambda = (|alpha|-1)(|beta|-1) > 1,
    mu = c . u_0.

The origin is global across the transient; no phase-local intercept is
silently substituted.

### Reflection and observable spans

For coordinate reversal R and state swap `R_state(u,w) = (Rw,Ru)`, the
phase-resolved identities are

    B_{R alpha} R = R A_alpha,
    A_{R beta} R = R B_beta.

The first identity is the reflected W phase and the second is the reflected V
phase.  Equality on all integer seeds forces these restrictions on
`U_e = span_R{u}` and `V_e = span_R{A_alpha u}`; conversely, restrictions on
each certified edge, together with reflected score/carry/target certificates,
induct to all certified steps.  Literal full-matrix statements occur only
when the relevant span is all of R^r.  A proper span, scalar degree equality,
or an unfixed same numerical seed is not promoted to a global identity.

### Local lower-ideal scope

The lower-ideal assertion is restricted to one strict typed pair core, one
forward step, and one reflected inverse step.  Its four normalized projections
are the V-plus input, W-plus output, reflected W-minus input, and reflected
V-minus output.  Selected-minus-new row margins are positive on the compact
normalized projections, while pair-dependent source/target/carry predicates
are checked on the compact pair core.  Homogeneity gives the stated
unnormalized one-step margins.  No target-core inclusion, C1-to-C2 stability,
multi-edge statement, or all-iterate perturbation claim is present.

### Fixture and boundaries

The exact asymmetric fixture is internally consistent:

    a1=(8,2,2), a2=(2,5,6), gamma=(2,8,2)
    b1=(2,2,8), b2=(6,5,2)

The matrices are `1 alpha^T - I` and `1 beta^T - I`, and direct multiplication
gives

    C21 = B2 A1 = I + 1(90,19,22)
    C22 = B2 A2 = I + 1(18,55,70).

The C1-to-C2 selector/carry vectors are
`(84,22,26)`, `(90,16,26)`, `(1078,230,276)`,
`(1078,236,270)`, and the carry vector `1(1074,231,268)`; the C2 self-loop
vectors are `(12,58,74)`, `(18,52,74)`, `(214,662,852)`,
`(214,668,846)`, with carries `1(216,660,840)` and
`1(18,55,70)`.  The displayed cones make every listed form positive.

For the C1 seed `(u,w)=((2,1,1),(1,1,1))`, the V scores are 20, 15, 14,
`A1 u=(18,19,19)`, `C21 u=(223,222,222)`, and the source W gap is 15.
The C2 seed `(1,1,1)` has `A2 u=(12,12,12)` and
`C22 u=(144,144,144)`.  The three C1 span seeds have determinant 1, the
three C2 span seeds have determinant -1, and `det A1=11`, `det A2=12`, so
the stated observable spans are full.  The reflected identities hold on the
two certified components.  At `(1,10,1)`, gamma scores 84 versus 30 and 58
for a1 and a2, while R gamma is absent from E_W; this is local reflection
closure, not a map-level reversor.

The cancellation example `V=(q1+q2+q3)^3`, `W=(p1-p2)^3` has zero/unit
support coordinates and loses the predicted W leading difference at the
first W half-step.  It is an explicit boundary outside the headline class.
Ties, empty cells, failed/nonpositive carries, missing reflected
certificates, positive characteristic, and proper-span complements remain
excluded exactly as stated.

## Citation, collision, and governance audit

`CITATION_VERIFICATION.md` contains exactly twenty first-party records
(`S01`--`S20`), a bounded query log through the stated decision date, and
source-role restrictions.  `NOVELTY_ASSESSMENT.md` supplies the P12--P26
claim-level collision matrix and the disjoint reserved P28--P31 axes.  Both
records use bounded-search/no-priority language and do not use citations as
proof.  The source-design and candidate reviews preserve the same theorem,
anti-claims, page range, and predecessor absorption.

The experiment plan and tracker are proof-only: no empirical run, code, CAS,
dataset, figure, numerical certificate, or build is part of this lock.  The
anonymous firewall excludes identity, affiliation, paths, hashes, event IDs,
reviewer names, and provenance from any future manuscript; the lock itself is
an internal control record.  The immutable source-design inputs may not be
silently edited, and any correction requires a named append-only disposition
and fresh review.  No downstream plan, manuscript, bibliography, build,
cache, PDF, release, upload, submission, hosting, repository push, message,
or identity operation is authorized by this gate.

The historical E0068 boundary-failed review and E0070 trailing-space event
are explicitly marked invalid/non-authoritative in the controlled ledger;
E0071, E0076, and E0077 provide the clean reconciliation and final plain-text
correction.  Those historical bytes do not create an active source-lock
finding or alter the measured aggregate.

## Finding census

| Finding class | Count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |
| Threshold miss | 0 |
| Manifest/path mismatch | 0 |
| Physical type/mode/link/encoding/line-ending defect | 0 |
| Aggregate row/framing/digest mismatch | 0 |
| Theorem, phase, carry, or Hessian mismatch | 0 |
| Reflection/span or lower-ideal scope mismatch | 0 |
| Fixture or boundary mismatch | 0 |
| Citation/collision/portfolio defect | 0 |
| Mutation, anonymity, or downstream-authority leak | 0 |
| Forbidden read/write/network/build/cache effect | 0 |

All required source-lock checks are zero.  The corrected lock, its plain-text
support notation, 25-path versus 24-row accounting, physical identities,
event-local unpadded `644` framing, theorem/source semantics, citation and
collision boundaries, fixture/boundary statements, and mutation/anonymity
firewall are mutually consistent.  This review creates no downstream
authority; it is solely the authorized all-zero source-lock PASS artifact.

BATCH07_PAPER27_SOURCE_LOCK_PASS
