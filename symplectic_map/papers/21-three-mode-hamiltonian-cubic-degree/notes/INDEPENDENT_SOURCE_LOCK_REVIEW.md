# Independent source-lock review — Paper 21

Verdict: PASS.

Lock identity and canonical audit:

- `papers/21-three-mode-hamiltonian-cubic-degree/experiments/source_lock.json`
- bytes `19857`, LF `1`, SHA-256 `41f350ca31fc06cf0eae3412419fa6d4615f9670a5d2150b04d7e59f9986b202`
- strict UTF-8 parse succeeded with duplicate-key rejection and nonfinite rejection
- one physical line, terminal LF present, no CR/NUL/BOM
- recursive Unicode-key ordering and compact separators round-tripped byte-exactly
- self-identity fields are null/excluded as required

Per-file author ledger (all verified twice):

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 3238 | 73 | `844268240ac6230d215623a58b77f12fbe2da83a58456c0adc70168a8f444474` |
| `experiments/EXPERIMENT_TRACKER.md` | 2097 | 37 | `8f56ee7483ef087a4539cf842b7fc1dc41ead3fa442949171751b80ccf2fa251` |
| `notes/CITATION_VERIFICATION.md` | 1338 | 17 | `0b7586368ced09d13f6e0d43d9493080bae18a78ec1fe36374434aea46612355` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 3266 | 55 | `44151f219d87c3c9ca662e360b248d60bc1262a87fcc01a91c24add5aff9dc16` |
| `notes/NOVELTY_ASSESSMENT.md` | 3014 | 58 | `a8c3c93e828ad86c940d038cf347630def5b3a58fdecd606357b2813e1c14941` |
| `notes/PROOF_PACKAGE.md` | 16199 | 427 | `599c9da5e5d4ca0e0b78c7b8683cdd2d63da50e555d9d6984bf1cf09f55e21d6` |
| `notes/RESEARCH_QUESTION.md` | 2362 | 49 | `185c276bac0c10b011b2077154103c7cb305550a60469b28b748cc4370e1577d` |
| `refine-logs/FINAL_PROPOSAL.md` | 2794 | 67 | `c39affe93a6a515c84303caa266733dde0a77df293b4410da92b486a11153fc0` |
| `refine-logs/INITIAL_PROPOSAL.md` | 1543 | 44 | `d38dae672970d3baf032a4ed6540134691e1c138e607a1a8dd8dc471eebb988e` |
| `refine-logs/REVIEW_SUMMARY.md` | 1392 | 28 | `f60a63a75ce6933b97a6b3f143f8f647ea861f1a7e83ce62437184f1b8b077e7` |

Aggregate ledger:

- framed record order: byte-sorted relative POSIX names
- framing: `uint64_be(name_len)||name_utf8||uint64_be(content_len)||content`
- content bytes `37243`
- total LF `855`
- framed bytes `37691`
- framed SHA-256 `6ead7872f6af98876b89e62f1b34573cd8fcfc4a61f4202a5a8214c7590acf8f`
- recomputed twice with identical result

Excluded provenance and bindings:

- design review: `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`, bytes `6091`, LF `125`, SHA-256 `1dc32c47d06b06657b9ed810df3ad6b2c4365d3b32aa5a49a5e93da1c410eaac`, final line `SOURCE_DESIGN_PASS`
- candidate records: R1 `d9362d3b07c38e2248494d2c0ec43209e7b0ce8fb089737326d61888b5d1d846`, R1 correction `6f455d8b40c873b8fc18568d95ed3e3b97de7528eddae911e83a00fe5214c132`, R2 `70592ffe85111cefde9e8fa872688958c22ad7cbe6bf4671151d9e5893aad387`
- corrected precedence is binding: the stale R1 T-row wording is superseded by R1 correction and confirmed by R2

Inventory and hygiene:

- exact frozen author inventory: 10 files only
- actual paper-root regular files before this reviewer artifact: 12
- directories present only under `experiments`, `notes`, and `refine-logs`
- zero symlinks
- zero forbidden `code/`, `data/`, `figures/`, `manuscript/`, `paper/`, `results/`, `transport/`, `build/`, PDF, TeX, BibTeX, release, upload, or compilation artifacts

Independent theorem replay:

- gradients, inverse shears, and symplectic Hessian-block check are correct
- matrices match exactly: `A`, `B`, and `C=BA`
- selectors are exactly two-faced: `M_S=(g-2)-2x-2y`, `M_T=(2g-6)x+(g-6)y-6`
- cone invariance split is correct for `8≤g≤11` and `g≥12`
- no-cancellation is characteristic-zero only, via the positive-support semiring induction
- visibility is the third coordinate: `deg(F^n)=e_3^T C^n 1`
- Perron bound and row sums are consistent with `rho(C)<(g-1)^2`
- characteristic polynomial and mod-5 residue table are correct
- `g=7` is a boundary anti-example, not a selector tie

Citation, collision, anti-claim, zero-science, permissions, lifecycle:

- exactly two primary arXiv citations, both terminology/context only
- Papers 12–20 are used only as a bounded internal collision screen; no global priority claim is made
- anti-claims are comprehensive: no genericity, entropy, periodic-point, torus, conjugacy, positive-characteristic, or priority claim
- scientific execution counters remain closed (`scientific_network_calls=0`, `scientific_runs=0`, `numerical_runs=0`, `cas_runs=0`, `datasets=0`, `figures=0`, `experiments_authorized=false`)
- permissions and lifecycle stay closed to manuscript/build/publication/transport/release/upload; only later paper-plan authorship remains to be authorized by the parent lifecycle update

Nonblocking note:

- keep the `e_3` visibility phrasing and the `H_2 = 2H` normalization in downstream writing

SOURCE_LOCK_PASS
