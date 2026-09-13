# Independent Paper20 source R2 page-fix audit

Date: 2026-08-22 UTC  
Review ID: `PAPER_SOURCE_R2_PAGEFIX_ADVERSARY_2026_08_22`

This is a fresh, independent, read-only audit of the source after the
authorized page-contract repair.  I read the live `paper/main.tex`,
`paper/math_commands.tex`, `paper/references.bib`, `paper/PAPER_PLAN.md`,
`paper/BUILD_METADATA_R1.json`, `paper/SOURCE_REVISION_RECEIPT_R1.json`,
`experiments/source_lock.json`, and the page-fix authorization note to EOF.
I also recomputed the locked ten-file aggregate and the source/authority
hashes.  I performed no LaTeX, BibTeX, PDF, CAS, symbolic, numerical,
experiment, network, transport, upload, publication, or author-source edit.
This reviewer-owned note is outside the frozen author aggregate.

## Live identity and authority binding

The current source identities are:

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 61,835 / 1,619 | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7c545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |
| `paper/BUILD_METADATA_R1.json` | 5,549 / 1 | `b891b8bb81d6383fc4b49fb81f41c346ecafbbd9663a25b44e7eb6bb8badf8dd` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 6,206 / 1 | `d8600e8d50efcda1b694e332a5b4282beb8b6c9ad9b5f302199f6f1aba728d3a` |
| `notes/SOURCE_PAGEFIX_AUTHORIZATION_R1.md` | 1,095 / 22 | `2043428f4a18dc1a980d122bb98273fa7d6fd89410f8e7eb68d1eeb5b51d20a8` |

The R1 metadata source rows and the revision-receipt source rows both match
the live byte counts, LF counts, and digests above.  The receipt's
`build_metadata_r1` row matches the live metadata (`5,549` bytes, SHA
`b891b8bb...`).  Its page-fix transition binds exactly the authorized change
from the prior 58,944-byte source to the current 61,835-byte source, with no
other manuscript, notation, bibliography, plan, or lock file changed.  The
metadata and receipt both retain the frozen theorem binding, source-lock
digest, plan digest, anti-claim/citation invariants, and page-fix reason.

The page-fix authorization explicitly permits one proof-first source repair
that adds leading-form propagation and full-coordinate support recurrence,
then requires fresh R1/R2 source audits before a replacement build.  The live
metadata remains `SOURCE_R1_PAGEFIX_PENDING_REVIEW`; its build permission is
false and all build artifact/page fields are null.  This audit does not infer
build permission from any other note.

All three JSON authority objects are UTF-8, LF-only, exactly one-terminal-LF,
compact recursively Unicode-key-sorted JSON with exact canonical round trips;
there are no BOM, CR, NUL, nonfinite values, or duplicate-key effects, and all
self-identity fields are null/self-excluded as required.  The ten-file
author aggregate independently recomputes to 45,416 bytes, 873 LF, and
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`, exactly
matching `source_lock.json`.  The frozen lock itself is unchanged.

The existing `main.pdf`, auxiliary files, and the older `main_round1.pdf` are
unbound historical/generated files under the metadata's forbidden-output
policy; none is treated as evidence for this source review.  The older
`BUILD_AUTHORIZATION_R1.md` also binds the superseded pre-page-fix source and
is not used as current build authority.  A fresh page-fix build authorization
will be needed after this source gate; this is a downstream handoff condition,
not a source-identity blocker.

## Authorized page-fix delta

A read-only comparison with the prior expanded source shows one contiguous,
non-duplicative addition immediately after the positive-coefficient
no-cancellation proof.  The addition is exactly the authorized
`Leading-form propagation` proposition and its support corollary; it adds no
citation, assumption, parameter range, map term, permission, genericity
claim, or external result.  The frozen headline theorem, phase order, and
anti-claim boundary are unchanged.

## Mathematical audit against the frozen proof contract

* **Canonicality and inverse (L1).**  The triangular inverse formulas have
  the correct order (F^{-1}=S^{-1}\circ T^{-1}).  The pullback and block
  Jacobian calculations use the symmetric Hessians in the stated
  ((q_1,q_2,p_1,p_2)) order; the displayed composite identity
  (DF_g^{\mathsf T}JDF_g=J) and determinant check are consistent.  No
  constant-Jacobian criterion replaces the explicit polynomial inverse.
* **First selector (L2).**  The derivative support is complete.  On
  (1\le u_2/u_1<(g-2)/2), the (q_1^{g-1}) contribution strictly beats
  (q_1q_2^2), while the second row is (q_1^2q_2).  The old carried
  (p)-vector is compared separately; the source correctly distinguishes
  \(\bar v=v_n\) from the new (v^+=A_gu_n), avoiding a false zero-as-gap
  substitution.
* **Second selector (L3).**  With (v=A_gu), the first row is
  (v_1+2v_2).  The intermediate ratio
  (v_2/v_1=(2+u_2/u_1)/(g-1)\ge3/(g-1)>2/(g-2)) for (g\ge5)
  strictly selects (p_2^{g-1}) in the second row.  Both carried (q)
  coordinates have explicit positive gaps.
* **Two-stage cone (L4).**  The fractional-linear return map
  (f_g(r)=(g-1)(2+r)/(g+3+2r)) is increasing; the lower and upper
  endpoint margins are (2(g-4)/(g+5)) and (g(g-4)/(2(2g+1))),
  respectively.  Thus the half-open cone is invariant for every integer
  (g\ge5), and (C_gu>u) componentwise.  The exact phase-return equality
  (v_{n+1}=A_gu_n) is retained; no invalid single strict two-shear cone or
  half-step theorem matrix is introduced.
* **Carried terms and no cancellation (L5).**  The (n=0) gaps and the
  simultaneous induction track every S- and T-phase carry.  Iteration in
  \(\mathbb Z_{\ge0}[q_1,q_2,p_1,p_2]\), positive scalar/multinomial path
  weights, and characteristic zero make selected leading pieces nonzero;
  the proof does not rely on monomial-path uniqueness or a genericity claim.
* **Recurrence and visibility (L6).**  The exact phase equations are
  (v_{n+1}=A_gu_n) and (u_{n+1}=C_gu_n).  The entrywise-positive
  (C_g-A_g) puts final p-degrees below corresponding q-degrees, while the
  cone gives (u_{n,2}>u_{n,1}) for (n\ge1).  Hence (q_2) is indeed the
  total-degree functional.
* **Perron calculation (L7).**  The trace (2g+2), determinant
  ((g-1)^2), and discriminant (16g) give
  ((\sqrt g\pm1)^2).  The explicit positive right/left eigenvectors and
  nonzero initial/output pairings establish both Perron accessibility and
  visibility, so the limit is the claimed ((\sqrt g+1)^2), not merely a
  formal matrix radius.

### Specific audit of the page-fix leading forms and \(\mathbb N^4\) support

For the top homogeneous forms (Q_{i,n}) and intermediate forms
(R_{i,n+1}), the four displayed identities are the literal top-degree
parts of the coordinate formulas:

\[
R_{1,n+1}=gQ_{1,n}^{g-1},\quad
R_{2,n+1}=2Q_{1,n}^{2}Q_{2,n},\quad
Q_{1,n+1}=2R_{1,n+1}R_{2,n+1}^{2},\quad
Q_{2,n+1}=gR_{2,n+1}^{g-1}.
\]

The strict selector/carry gaps isolate these terms before taking homogeneous
parts.  Substitution gives (Q_{1,n+1}=8gQ_{1,n}^{g+3}Q_{2,n}^2) and
(Q_{2,n+1}=g2^{g-1}Q_{1,n}^{2(g-1)}Q_{2,n}^{g-1}), with nonzero positive
coefficients at the base step and every iterate.  In the full coordinate
order ((q_1,q_2,p_1,p_2)), positive-coefficient product supports have exact
Minkowski sums; consequently

\[
E_{1,n+1}=(g+3)E_{1,n}+2E_{2,n},\qquad
E_{2,n+1}=2(g-1)E_{1,n}+(g-1)E_{2,n}.
\]

Coincident exponent sums add rather than cancel in characteristic zero.  These
are a monomial-level refinement of the already locked degree recurrence, not
a new generic Newton-fan assertion.  The notation is consistent with top
forms in the full \(\mathbb N^4\) support, even though the degree vectors only
retain the two q-phase totals.

## Structure, citations, and scope

The current source has 67 unique labels (67 occurrences), 44 unique internal
reference targets, and all targets resolve; its eight explicit tags are
unique.  `begin`/`end` environment counts are 107/107 and brace balance is
zero.  The exact draft-marker scan (`TODO`, `TBD`, `VERIFY`, `FIXME`, `??`,
`[?]`) is empty; ordinary lowercase prose such as “verify” is not a marker.
All seven bibliography keys used in the source resolve to the locked
`references.bib`.  Citation roles remain only the four bounded context roles
authorized by the citation lock; no source is promoted to proof, priority, or
firstness evidence.

The source remains restricted to the fixed positive-coefficient family over an
algebraically closed characteristic-zero field and integer (g\ge5).  It
continues to exclude arbitrary supports/words/coefficients, generic finite
Newton fans, positive characteristic, universal symplectic or conjugacy
claims, entropy equalities, periodic/trace/centralizer/torus/arithmetic
classifications, numerical/CAS certificates, and absolute novelty or priority.
The P12--P19 table remains a bounded collision boundary.  No figure, dataset,
experiment, code, result, transport, or publication claim was introduced by
the page-fix section.

## Verdict

No source-identity, page-fix authorization, theorem/proof, leading-form,
full-coordinate-support, phase-indexing, label/citation, scope, anti-claim,
or permission blocker was found.  This note is a source gate only: it does
not authorize compilation, a PDF handoff, publication, transport, upload,
experiments, CAS, or further source editing.

PAPER_SOURCE_R2_PAGEFIX_PASS
