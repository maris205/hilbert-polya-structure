# Independent Paper16 Source-Lock Review

Date: 2026-08-17 UTC

Candidate: `henon_support_size_torus_escape_v1`

Lock reviewed: `experiments/source_lock.json`

I am the fresh post-lock reviewer. I authored none of the 22 bound inputs and
did not author the source lock. I began the lock review only after the explicit
`LOCK AUTHOR STOP` and stable-identity notice. Before that notice I did not
stat, list, open, or otherwise inspect the future lock. I made no project write
before all checks below passed. This report is the sole project-file write made
by this review.

No web access, compilation, rasterization, CAS, scientific computation,
parameter scan, code execution for theorem evidence, data creation, result
creation, figure work, manuscript work, submission, upload, or external
communication was performed. Read-only parsing, hashing, byte counting, PDF
text inspection, and bounded filesystem inventory checks were used only for
integrity review.

## Lock identity and canonical JSON

The stable lock independently rehashed to exactly:

- bytes: `31945`;
- LF count: `1`;
- SHA-256:
  `86205b1f4dc12ab71302e9b283021c8085afc16f0cf6b479d9a91738c03041fd`.

Strict UTF-8 parsing with duplicate-object-key rejection and nonfinite-number
rejection succeeded. A recursive lexicographic-key, compact-separator,
`ensure_ascii=false` serialization followed by one LF reproduced the lock
byte-for-byte. There is no CR byte, BOM, insignificant whitespace, second
terminal LF, duplicate key, or nonfinite number. Independent synthetic probes
rejected `{"x":1,"x":2}`, `NaN`, `Infinity`, and `-Infinity`.

The lock contains no binding record giving its own byte count or SHA-256. Its
11 local bindings omit `experiments/source_lock.json`; the self-exclusion is
also stated explicitly by `self_bytes_excluded=true` and
`self_hash_excluded=true`. Every bound path is unique, nonempty, relative,
free of dot and dot-dot segments, and resolves inside its declared base. No
absolute workspace path or remote-web byte object is bound.

## Exact 22-input binding replay

The local binding set is exactly the intended 11 Paper16 source-design files,
and the upstream binding set is exactly the intended seven Paper14 provenance
files plus four workspace governance files. Immediately before this report was
written, every file was independently reread and rehashed as follows.

| Bound path | Bytes | SHA-256 |
|---|---:|---|
| `papers/16-henon-support-size-torus-escape/experiments/EXPERIMENT_PLAN.md` | 5824 | `f50a42f9dde61f00801c4696447c6b161a496cdfb7047b468041917225ba65f6` |
| `papers/16-henon-support-size-torus-escape/experiments/EXPERIMENT_TRACKER.md` | 1971 | `4578dd2cfbedb25cd2a327ba6d865535bf3d007951f9b749032f9bd6d633b83d` |
| `papers/16-henon-support-size-torus-escape/notes/CITATION_VERIFICATION.md` | 10733 | `6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24` |
| `papers/16-henon-support-size-torus-escape/notes/CLAIMS_EVIDENCE_MATRIX.md` | 7659 | `bc5541dcebce9b2cb8cb7e180a91097d55f0d6b0fdc74fb5b4be7f432e462311` |
| `papers/16-henon-support-size-torus-escape/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 13903 | `046e2ec16b46e8de903eac950c1df922725c5b16e359f5ed6c45bd28e737dd61` |
| `papers/16-henon-support-size-torus-escape/notes/NOVELTY_ASSESSMENT.md` | 7309 | `83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b` |
| `papers/16-henon-support-size-torus-escape/notes/PROOF_PACKAGE.md` | 16808 | `b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8` |
| `papers/16-henon-support-size-torus-escape/notes/RESEARCH_QUESTION.md` | 8319 | `43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928` |
| `papers/16-henon-support-size-torus-escape/refine-logs/FINAL_PROPOSAL.md` | 5387 | `220bb54312f80f17b6b99a37afffa902fd04a6b696c0c3e1f60f4ed8d374b540` |
| `papers/16-henon-support-size-torus-escape/refine-logs/INITIAL_PROPOSAL.md` | 4253 | `329c7a6687612ff806508640f7add09201ac9ddedd41c10fabd9582a4beab8b2` |
| `papers/16-henon-support-size-torus-escape/refine-logs/REVIEW_SUMMARY.md` | 5479 | `20256b3f6915781c07dadb6beec26fa69529c5c7d0660b0171c14d460656c55a` |
| `papers/14-henon-four-step-torus-escape/notes/PROOF_PACKAGE.md` | 13728 | `c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa` |
| `papers/14-henon-four-step-torus-escape/notes/CITATION_VERIFICATION.md` | 12919 | `0c9b08f566eedb1e9f344f6fb07dfcf0c87015daa566435d0c989ac722d4e2af` |
| `papers/14-henon-four-step-torus-escape/notes/CLAIMS_EVIDENCE_MATRIX.md` | 5902 | `d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e` |
| `papers/14-henon-four-step-torus-escape/paper/main.tex` | 47961 | `415f1395f07153ccb158e69cb70051e95e719802d0a1c3315df88be7ccfab538` |
| `papers/14-henon-four-step-torus-escape/paper/FINAL_RELEASE_MANIFEST.json` | 32293 | `e832be91a990d1d1caf7e2b4aba40fa8d9a1196524c815e03b30309df6226e68` |
| `papers/14-henon-four-step-torus-escape/paper/main.pdf` | 384084 | `4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414` |
| `papers/14-henon-four-step-torus-escape/paper/reviews/final_integrity_review.md` | 7429 | `9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d` |
| `BATCH_04_STATUS.md` | 20124 | `6c9b409e9e22b870b966dc7478cc4a19076b88410108c981ee3bc649d1720e2d` |
| `BATCH_04_IDEA_REPORT.md` | 25921 | `2d1c19fc2891a4ee80dbc46ee6b44f059f194815c4c21a6239531377680f517f` |
| `README.md` | 4805 | `64f3ccda2db5af63a63e295e9b9cc98283622c39b15cc4851467024a1fb2bdd8` |
| `docs/candidate_registry.md` | 8665 | `c9e510329baa09a52050b8f27b9f4af99a84a4f3be3894b244577ebfeed2c0cc` |

All 21 textual inputs also match their locked LF counts and decode strictly as
UTF-8. The Paper14 PDF is correctly marked nontextual. The Paper14 final
manifest independently passes the same strict canonical compact-JSON
round-trip and has the exact identity bound above.

The dated top-level pre-project labels are explicitly bound as historical
provenance, not current lifecycle authority. Likewise, the older Paper14
citation wording is historical; the corrected, theorem-number-specific
Paper16 citation record is normative. These role declarations prevent stale
provenance text from contradicting the current lock.

## Inventory replay

Before this report was created, the Paper16 project root contained exactly 12
regular files in exactly three real subdirectories:
`experiments`, `notes`, and `refine-logs`. There were zero symlinks and zero
other filesystem entry types. The 12-file set was exactly the 11 local bound
inputs plus `experiments/source_lock.json`; there was no unbound regular file.

The future path `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` was absent. Each of
`code`, `data`, `figures`, `manuscript`, `output`, `paper`, `results`,
`review`, `reviews`, and `source` was absent. Thus the prewrite inventory is
exactly `12 files / 3 directories / 0 symlinks`, and the lock's sole-pass-write
transition to 13 files is well-defined.

## Independent mathematical replay

I replayed all obligations P01--P16 and all 24 anti-claims, rather than relying
on the earlier source-design verdict.

### Definitions, external theorem, and sparse-image lemma

The package consistently fixes a characteristic-zero field (K), collected
actual support

\[
1\le e_1<\cdots<e_s=d,
\qquad
P(X)=c+\sum_{j=1}^s b_jX^{e_j},
\]

with (a,c,b_j\in K^*\), the automorphism
(H(x,y)=(P(x)+ay,x)), and a finite-rank, not necessarily finitely generated,
group \(\Gamma\le K^*\). The convention that (T_m) contains (m+1) states
and (m) transitions is uniform in every bound source.

The sole external proof theorem is correctly locked as Amoroso--Viada,
Theorem 6.2, with

\[
\mathcal A(q,R)=(8q)^{4q^4(q+R+1)}.
\]

Its algebraically closed characteristic-zero domain is not silently widened.
For arbitrary (K), the proof passes to an algebraic closure, injects the
(K)-solutions, preserves the abstract rank of \(\Gamma\), and applies the
theorem to homomorphic images of \(\Gamma^2\) or \(\Gamma^3\). No descent or
equality of solution sets is asserted. Fixed coefficients remain coefficients
of the linear equation and are never adjoined to the variable group.

For a (q)-term sparse polynomial (F), the tuple
((t^{m_1}u^{-1},\ldots,t^{m_q}u^{-1})) has rank at most (2r).
A coordinate ratio recovers (t) through a nonzero power of exponent at most
(d), giving at most (d) lifts, after which (u) is fixed. In the degenerate
case a singleton cannot vanish, and the (2^q-q-2) possible proper subsets of
sizes (2,\ldots,q-1) each give a nonzero polynomial of degree at most (d).
This proves

\[
\#\{(t,u)\in\Gamma^2:\lambda u=F(t)\}
\le d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr)=\mathcal S_q.
\]

The proof remains valid with arbitrary torsion because the imported theorem
uses rank and every lift is controlled by a polynomial root bound.

### PC1: all four first-degeneracy cases

For a (T_2) point, the first recurrence is normalized exactly as

\[
Z+U+\sum M_j=1,
\qquad
Z=z/c,quad U=-au/c,quad M_j=-b_jv^{e_j}/c.
\]

The variable tuple is a homomorphic image of \(\Gamma^3\), hence has rank at
most (3r). A nondegenerate tuple contributes at most
(d\mathcal A(s+2,3r)), with the (d)-factor supplied by power recovery for
(v).

The degeneracy classification is exhaustive and has no missing free coset:

- GZ gives (z=B_J(v)) and (-au=c+B_{J^c}(v)). If (J=[s]), the first graph
  uses \(\lambda=1\) and has (s\ge2) terms. If \(|J|=1\), the second graph
  uses \(\lambda=-a\) and has (s\ge2) terms. Intermediate cases have a
  multi-term side as well.
- GU gives (au=-B_J(v)) and (z=c+B_{J^c}(v)). If (J=[s]), the first graph
  uses \(\lambda=a\) and (s\ge2) terms. If \(|J|=1\), the second graph uses
  \(\lambda=1\) and (s\ge2) terms. Thus the empty complement at the endpoint
  causes no gap.
- R0 has \(|J|\ge2\) and (B_J(v)=0). Factoring the nonzero power of (v)
  leaves at most (e_{\max J}-e_{\min J}) possible nonzero roots.
- R1 reindexes by the nonempty complement and gives (c+B_J(v)=0), hence at
  most (e_{\max J}) roots.

For either root case, the second recurrence is

\[
w=(c+a\rho)+\sum_{j=1}^s b_jz^{e_j}.
\]

It has (s+1) nonzero terms unless the constant cancels, and exactly
(s\ge2) nonzero terms if it does. The sparse-image lemma therefore closes
every vertical root fiber by \(\mathcal S_*\). Once (v,z) are fixed, the
first recurrence uniquely recovers (u). Multiple vanishing proper subsums
are covered by a full union and only overcount.

The component budget is consequently exactly

\[
\mathcal M(\mathbf e)=2(2^s-1)
+\sum_{|J|\ge2}(e_{\max J}-e_{\min J})
+\sum_{J\ne\varnothing}e_{\max J},
\]

with the closed and crude formulas used only as checksums. This gives the
locked theorem

\[
\#T_2(H,\Gamma)
\le d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*.
\]

### PC2, PC3, and essential assumptions

For every prescribed support with (s\ge2), the rational choice
(a=b_1=\cdots=b_s=1), (c=-s), and \(\Gamma=\langle2\rangle\) has
(P(1)=0) and
((1,2^n)\mapsto(2^n,1)). Hence (T_1) is infinite and the two-transition
threshold is sharp. The optional roots-of-unity rank-zero observation is
properly subordinate to this rational rank-one statement.

PC3 reproduces the support-one argument rather than citing Paper14 as a black
box. At each of four local indices the nondegenerate tuple has rank at most
(3r), giving (4d\mathcal A(3,3r)). I independently rederived all nine
adjacent A/B/C words. Only BA and CB can remain free after two labels; every
BA branch closes at the third label, and only CBA can remain free after three,
under (a=-1) and (bc^{d-1}=-1). Its A/B/C fourth extensions have bounds
(1,d^2,d^2-1). The full (3^4)-word union, including simultaneous labels,
therefore contributes at most (81d^2). This proves

\[
\#T_4(H,\Gamma)\le4d\mathcal A(3,3r)+81d^2.
\]

The rank-one family with (c^{d-1}=-1), (a=-1), (b=1),
(\Gamma=\langle2,c,-1\rangle), and (t=2^n) has the exact scalar chain
(t^d,t,c,-t,(-t)^d), so (T_3) is infinite. The rank audit is correct:
(c) and (-1) are torsion and (2) has infinite order.

The locked counterexamples also check directly. If (c=0),
(P=X^d+X,a=-1) gives
((t,t^d)\mapsto(t,t)\mapsto(t^d,t)). If (a=0),
(P=-1+X+X^2) gives
((1,t)\mapsto(1,1)\mapsto(1,1)). Thus neither nonvanishing hypothesis is a
dispensable presentation choice.

## Citations, novelty, scores, and absorption

The theorem-number and scope boundaries are internally exact:

- Amoroso--Viada Theorem 6.2 is the unique proof input;
- ESS Theorem 1.1 is historical only;
- Krieger et al. Theorem 1.7, Theorem 1.8, and Corollary 1.9 are distinguished
  rather than collapsed;
- Bell--Ghioca Theorem 1.1 concerns one fixed orbit and does not turn the full
  hitting-time set into a finite set;
- Ji--Xie--Zhang Theorem 1.8 and Corollary 1.9 give non-density, not finiteness;
- the Mello--Yasufuku epsilon-range mismatch remains disclosed;
- the exact degree and congruence ranges of Kim et al. Theorems A and B are
  retained.

The no-collision conclusion is correctly limited to a bounded primary-source
search through 2026-08-17 and is not stated as priority or exhaustive absence.
All 24 anti-claims A01--A24 are present exactly once and agree with the claim
matrix and proof package.

The independent source-design review has exact identity
`046e2ec16b46e8de903eac950c1df922725c5b16e359f5ed6c45bd28e737dd61`,
ends with `SOURCE_DESIGN_PASS`, and records novelty `7.8`, standalone value
`8.0`, and proof correctness/closure `9.3`, all above their frozen thresholds.
These scores remain lifecycle records rather than theorem evidence.

Paper14 is completely absorbed: its proof package, claims matrix, source,
canonical release manifest, full 17-page terminal PDF, and terminal review
were all inspected and match their bindings. The predecessor terminal review
ends with `FINAL_INTEGRITY_PASS` and `RELEASE_CONFIRMED`. PC3 reproduces the
support-one proof and updates only the displayed unit-equation constant to the
Amoroso--Viada form. Paper14 remains local provenance, and parallel external
submission of overlapping Paper14 and Paper16 manuscripts is explicitly
forbidden.

## Lifecycle and verdict

The lock records `source_design_frozen=true` and `source_lock_frozen=true` and
accurately reports `NO SCIENTIFIC RUN`: no code, data, result, or figure exists.
The experiment documents are a future symbolic-audit plan only and authorize
no execution.

This pass has one narrow effect. After a separate stage invocation, it makes
only proof-only `paper/PAPER_PLAN.md` authoring and a fresh independent plan
review eligible. Bibliography, TeX, manuscript, code, scientific execution,
data, results, figures, compilation, finalization, release, submission,
upload, external messaging, and identity disclosure remain false or require
later independent governance gates.

No blocking mathematical, citation, provenance, canonicalization, binding,
inventory, independence, or lifecycle finding remains.

SOURCE_LOCK_PASS
