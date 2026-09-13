# Paper 27 strict-canonical source lock

## Lock identity

This record freezes the proof-first source package for candidate
`positive_newton_translation_reciprocity_v5` (Paper 27).  It is an internal
control record, not part of a future anonymous article.  The lock is valid
only for the exact bytes listed below and for the theorem scope in the
canonical source-design documents.  It creates no publication, upload,
submission, hosting, identity, or other external effect.

The source-design review is the fresh independent all-zero review in
`notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`.  Its review digest is
`4fdf61878bc78315f42d07b4a4d565d9fe154910c3fa50e49a4c234867b0dbed` (11,229
bytes, 231 LF).  The source-design package plus that review has the
self-excluding aggregate
`b86617e99feee6b6c287260fc903d800c29a9673c22e5b6f414147644cf19670` over 23
rows and 3,079 framing bytes.

For this aggregate, rows are sorted by bytewise relative path and serialized
as
`path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>`.
The `644` token is unpadded octal serialization of physical mode `0644`; it
does not change the filesystem mode.  The frozen Batch-07 opening passport
used padded `0644`, so the two historical event-local conventions must not be
silently mixed.  The corrected 64-hex digest for the retained historical R2
correction row is
`da719d459bb9fbcc925ef3c38adf5021af9a8961db82516cc416843ecd885106`.

## Frozen project universe

Exactly three child directories exist under this project at the lock:
`experiments`, `notes`, and `refine-logs`.  Exactly these eleven regular,
non-symlink files are in the project universe:

| Relative path | Bytes | LF | Mode | Links | SHA-256 |
|---|---:|---:|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 4928 | 108 | 0644 | 1 | `1b9628e18703fd2332c90799c71abaaa42467b7080cb35a59ab3617b1c4c9a9d` |
| `experiments/EXPERIMENT_TRACKER.md` | 3116 | 52 | 0644 | 1 | `bbd8ec0ebdd866fb09174b65dd87075623fae78eba48e96aaccc4625deb45e8e` |
| `notes/CITATION_VERIFICATION.md` | 9366 | 61 | 0644 | 1 | `1a54b62d83cd6861679f851ec509854d6ed83eb046d5b6db7343b6e96aa9c26b` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 6022 | 43 | 0644 | 1 | `b0415cf8118b6e33352d513e170f5c2ad854e54a3ba854d683faca3eb6425b14` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 11229 | 231 | 0644 | 1 | `4fdf61878bc78315f42d07b4a4d565d9fe154910c3fa50e49a4c234867b0dbed` |
| `notes/NOVELTY_ASSESSMENT.md` | 6040 | 81 | 0644 | 1 | `16b97ac1e7df048e1eb2d05f69980064f8201cf56a878bbd496831d20eec647c` |
| `notes/PROOF_PACKAGE.md` | 19921 | 527 | 0644 | 1 | `c583d2cedcd97bef8410172bed967dfe99bcaf9caa69595c305bbf36ccd51fd1` |
| `notes/RESEARCH_QUESTION.md` | 4908 | 126 | 0644 | 1 | `73b094e1905f4a5af49c82f3b3bfa7a242125e56ff724dcf00c1c8bb1a0ea4cc` |
| `refine-logs/FINAL_PROPOSAL.md` | 5446 | 131 | 0644 | 1 | `d2bd1a47959907efa35364e408ede645353059a47cb3641226f5d022605a71ae` |
| `refine-logs/INITIAL_PROPOSAL.md` | 3525 | 75 | 0644 | 1 | `af290d3d3587d6824cbe1c892d3b11c8551113d63c5fe03c1f641967af75e3e6` |
| `refine-logs/REVIEW_SUMMARY.md` | 4064 | 76 | 0644 | 1 | `3805351516268043f6a3a91c35dc6568428849ad8fbdde33fc9872eef06e7836` |

Every file is strict UTF-8, LF-only, has no BOM, CR, or NUL, and ends in
exactly one LF.  The controlled `BATCH_07_STATUS.md` ledger is outside the
self-excluding project aggregate.  No `paper` directory, standalone
`PAPER_PLAN.md`, bibliography, manuscript, code, data, figure, build root,
cache, PDF, or release copy is part of this lock.

## Theorem contract frozen for downstream writing

The only headline permitted downstream is the separated Hamiltonian-shear
statement over a characteristic-zero field (K), with (r\ge 3), nonempty
finite collected supports (E_V,E_W\subset\mathbb Z_{\ge2}^{,r}), unique
exposed selectors on a strict edge, and positive carries.  With

\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),\qquad F=T_W\circ S_V,
\]

the exposed degree action is
\(A_\alpha=\mathbf1\alpha^{\mathsf T}-I\),
\(B_\beta=\mathbf1\beta^{\mathsf T}-I\), and the phase order is
\((u,w)\mapsto(B_\beta A_\alpha u,A_\alpha u)).  The proof package freezes
the grouped-Hessian/Jacobian and injective-substitution noncancellation
argument, the all-ones translation

\[
 v=h_V(u)\mathbf1-u,\qquad
 u'=h_W(v)\mathbf1-v=u+\delta\mathbf1,
 \qquad \delta=h_W(v)-h_V(u)>0,
\]

the global selector-change bound (d_V+d_W-2), and the stationary affine
tail

\[
 t_{n+1}=\lambda t_n+\mu,\qquad
 \lambda=(|\alpha|-1)(|\beta|-1),\qquad
 \mu=((|\beta|-1)\alpha-\beta)\cdot u_0.
\]

Reflection reciprocity is locked only edgewise on the observable spans
\(U_e,V_e\), with the reflected selector, carry, and target certificates;
full-matrix claims require full spans.  The lower-ideal result is locked only
to one strict pair cell, one step, and four normalized projections.  The
exact three-dimensional fixture and the half-step cancellation fixture are
witnesses and boundaries, never substitutes for a universal proof.

## Citation and collision boundary

The twenty primary records and bounded public search cut-off are exactly
those frozen in `notes/CITATION_VERIFICATION.md` and
`notes/NOVELTY_ASSESSMENT.md`.  Downstream writing may cite only verified
records from that package or records independently reverified under a later
authorized gate.  No absolute priority claim, unverifiable computation,
empirical result, broad scan, or new literature narrative may be added under
this lock.  The direct collision and anti-claim boundaries against Papers
12--26 and queued Papers 28--31 remain binding.

## Mutation and anonymity firewall

The eleven files above are immutable source-design inputs.  A later author
may create only paths explicitly authorized by a subsequent ledger event and
must record a new aggregate before any mutation.  Any correction to a locked
source file requires a named append-only disposition, a fresh source-design
review, and a new lock; silent replacement, in-place polishing, or stale-hash
repair is forbidden.  The future article must contain no internal event ID,
filesystem path, hash, reviewer name, author identity, affiliation, or
provenance language.  No external operation is authorized.

## Gate handoff

This lock is complete only after a fresh independent source-lock reviewer
recomputes the physical census, the 23-row aggregate, the theorem contract,
the citation boundary, and the mutation/anonymity firewall with zero findings.
The next author gate is a proof-only article-plan stop.  Until that PASS is
consumed, no `PAPER_PLAN.md`, manuscript source, bibliography, build root, or
publication-stage artifact may be created.

BATCH07_PAPER27_SOURCE_LOCK_FROZEN

## 14. Lock-scope and notation correction addendum

This append-only addendum supersedes only the ambiguous lock prose above; no
earlier byte is deleted.  The table in this record is the **eleven-file
source-design input subset** (the ten author-stop files plus the independent
source-design review).  `SOURCE_LOCK.md` itself is a twelfth project file and
the 24th row of the aggregate; the twelve inherited top-level rows are the
frozen Batch-07 inputs named in the controlling ledger.  Thus the complete
post-lock aggregate is exactly 12 inherited rows + 11 source-design rows + 1
lock row = 24 rows, while the source-design aggregate before this lock was 23
rows.  The lock record is included in the post-lock aggregate and the status
ledger is excluded.

The canonical support notation is
\(E_V,E_W\subset\mathbb Z_{\ge2}^{,r}\), with (r\ge3).  The headline
quantifier is “every certified strict branch (or finite seed-indexed edge
word) satisfying the printed selector, carry, target, and reflected
certificates”; it is not a claim about arbitrary weighted-degree orbits.
Reflected labels are required only through the appropriate reflected support
or action certificate on the observed edge; global reflection closure is not
assumed.  The lower-ideal phrase means a one-edge, one-step four-projection
margin lemma and never an invariant ideal, target-core inclusion, multi-edge
stability, or all-iterate perturbation theorem.

Every later manifest event must state its own serialization token.  Unless a
later event explicitly supersedes this lock, aggregate rows use unpadded
octal `644` for physical mode `0644`, sorted bytewise with LF terminators.
These clarifications are internal controls and must not appear as metadata or
provenance in the anonymous manuscript.

BATCH07_PAPER27_SOURCE_LOCK_CORRECTION_ADDENDUM

## 15. Plain-text notation and whitelist-count correction

This final administrative addendum supersedes the two malformed support
notation strings in the earlier lock prose and removes any dependence on
backslash escaping.  Read the support hypothesis as:

    E_V and E_W are finite nonempty subsets of Z_{>=2}^r, with r >= 3.

The complete review whitelist has 25 paths: the 24 self-excluding aggregate
rows plus BATCH_07_STATUS.md for the ledger parent check.  The aggregate
itself still has exactly 24 rows, because the status ledger is excluded.
The project contains 12 files at this lock: the eleven frozen source-design
inputs in the table above and this SOURCE_LOCK.md record.  These are counting
clarifications only; the theorem and all other lock boundaries are unchanged.

BATCH07_PAPER27_SOURCE_LOCK_PLAIN_TEXT_CORRECTION
