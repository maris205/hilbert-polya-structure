# Independent Paper20 R1 source audit after page-contract repair

Date: 2026-08-22 UTC  
Review ID: `PAPER_SOURCE_R1_PAGEFIX_AUDITOR_2026_08_22`

This is a fresh, independent, read-only audit of the page-fixed manuscript
source.  I did not compile, run BibTeX, run CAS or symbolic execution, run an
experiment, access a dataset, edit an author source/metadata file, transport,
publish, or upload anything.  This reviewer-owned note is out-of-band and is
not part of the frozen ten-file author aggregate.

## Live identities and authority bindings

The following identities were recomputed from the live files:

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 61,835 / 1,619 | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |
| `paper/BUILD_METADATA_R1.json` | 5,549 / 1 | `b891b8bb81d6383fc4b49fb81f41c346ecafbbd9663a25b44e7eb6bb8badf8dd` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 6,206 / 1 | `d8600e8d50efcda1b694e332a5b4282beb8b6c9ad9b5f302199f6f1aba728d3a` |
| `notes/SOURCE_PAGEFIX_AUTHORIZATION_R1.md` | 1,095 / 22 | `2043428f4a18dc1a980d122bb98273fa7d6fd89410f8e7eb68d1eeb5b51d20a8` |

The R1 metadata `source_files` rows match the live manuscript, notation,
bibliography, and plan byte/LF/hash identities.  Its plan row matches the
live plan, its source-lock row matches the frozen lock, and its page-fix
authorization row matches the live authorization note.  The revision receipt
binds the live metadata digest and the same current manuscript identity.  The
receipt records the earlier compact-to-expanded transition separately and its
page-fix `to` identity is the current 61,835-byte source; this is a coherent
two-stage provenance chain, not an unrecorded source edit.

The lock's ten author-file allowlist was independently rehashed: every row
matches, with 45,416 total bytes and 873 LF and aggregate SHA
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.
The frozen theorem, citation roles, collision boundary, anti-claims, and
permissions therefore remain the source-lock authority.  The source lock,
metadata, and revision receipt are UTF-8, LF-only, exactly one-terminal-LF,
duplicate-key-free, recursively Unicode-key-sorted canonical JSON; their
self-identity fields are null/excluded and all finite-number/round-trip checks
pass.

The planned build remains future-null (`NOT_RUN`, null artifact/page fields,
`build_authorized: false`).  Existing `main_round1.pdf` and auxiliary files
are historical pre-page-fix outputs; the page-fix authorization explicitly
excludes that failed 21-page-body build from the replacement receipt.  No
build or experiment output was created in this review, and no build,
publication, transport, or upload authority is granted here.

## Source structure, labels, citations, and hygiene

`main.tex` is UTF-8/LF-only with no BOM, CR, or NUL.  It has 67 unique labels,
64 reference uses (44 unique targets), no missing or duplicate targets, eight
unique explicit equation tags, balanced 107 `begin`/`end` environments, and
balanced braces.  The seven bibliography keys are unique and every cited key
resolves.  Draft/verification markers (`TODO`, `TBD`, `VERIFY`, `FIXME`,
`??`, and `[?]`) occur zero times.  The only input/bibliography paths are the
declared `math_commands` and `references` files.  No build, results,
transport, figures, code, data, or experiment directory was introduced.

The page-fix source delta is exactly the authorized leading-form propagation
proposition and its full-coordinate Minkowski-support recurrence.  It is
inserted after the coefficientwise no-cancellation proof; the surrounding
source is unchanged from the previously reviewed 58,944-byte identity.

## Mathematical audit

The fixed family remains (K) algebraically closed of characteristic zero,
(g\ge5),

\[
V=q_1^2q_2^2+q_1^g,\qquad W=p_1^2p_2^2+p_2^g,
\qquad F_g=T\circ S,
\]

with

\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\quad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},\quad
C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

The seven locked proof obligations were checked independently:

* **L1 (inverse and canonicality).**  The triangular inverse formulas have
  the correct (T^{-1})-then-(S^{-1}) phase order.  The gradient Hessians
  are symmetric; the pullback calculation, block Jacobians
  (DS=\left[\begin{smallmatrix}I&0\\Q&I\end{smallmatrix}\right]),
  (DT=\left[\begin{smallmatrix}I&P\\0&I\end{smallmatrix}\right]),
  (DF=\left[\begin{smallmatrix}I+PQ&P\\Q&I\end{smallmatrix}\right]),
  the direct (DF^{\mathsf T}JDF=J) multiplication, and the determinant
  check are consistent.
* **L2 (S selector).**  The derivative support is complete.  On
  (1\le u_2/u_1<(g-2)/2), the first-row candidates satisfy
  (u_1+2u_2<(g-1)u_1), while the second row is (2u_1+u_2).  The old
  carried (p)-coordinates are compared separately, including the
  (u_0=v_0=(1,1)^{\mathsf T}) base case.
* **L3 (T selector).**  With (v=A_gu), the first row has degree
  (v_1+2v_2).  The second-row ratio is
  (v_2/v_1=(2+u_2/u_1)/(g-1)\ge3/(g-1)>2/(g-2)), so the pure
  (p_2^{g-1}) term strictly beats (2v_1+v_2) and the carried (q_2)
  coordinate.  The carried (q_1) gap is also explicit and positive.
* **L4 (two-stage cone).**  The fractional-linear map
  (f_g(r)=(g-1)(2+r)/(g+3+2r)) is increasing, has the stated strict
  lower and upper endpoint margins, preserves the half-open cone, and gives
  (C_gu>u) componentwise.  The proof retains the exact phase-return
  equality (v_{n+1}=A_gu_n), rather than imposing a false strict
  cross-phase cone.
* **L5 (old terms and no cancellation).**  The simultaneous induction has
  the correct old vector (v_n=A_gu_{n-1}), checks all S- and T-phase carried
  terms at (n=0) and at every later step, and uses the positive-integer
  coefficient semiring plus characteristic zero to preserve selected leading
  pieces.  No unsupported monomial-uniqueness or genericity assertion is
  needed.
* **L6 (recurrence and visibility).**  The induction closes with
  (v_{n+1}=A_gu_n) and (u_{n+1}=C_gu_n).  Since
  (C_g-A_g=\left[\begin{smallmatrix}4&2\\2g-4&g-2\end{smallmatrix}\right])
  is entrywise positive and the cone gives (u_{n,2}>u_{n,1}) for
  (n\ge1), the final (q_2) coordinate is the maximum of all four
  coordinate degrees.
* **L7 (Perron limit).**  The trace (2g+2), determinant ((g-1)^2),
  discriminant (16g), explicit positive right/left Perron vectors, and
  nonzero initial/observed pairings give
  (ho(C_g)=(\sqrt g+1)^2) and the claimed degree limit.  The scalar
  recurrence and (g=5) hand audit agree with these values.

### Page-fix proposition and full-coordinate support check

The new `prop:leadingforms` is a consequence of the already checked strict
selector gaps, not an additional assumption or genericity claim.  With
(Q_{i,n}=(q_{i,n})^{[u_{i,n}]}) and
(R_{i,n+1}=(\widehat p_{i,n+1})^{[v_{i,n+1}]}), the displayed identities

\[
R_{1,n+1}=gQ_{1,n}^{g-1},\quad
R_{2,n+1}=2Q_{1,n}^2Q_{2,n},\quad
Q_{1,n+1}=2R_{1,n+1}R_{2,n+1}^2,\quad
Q_{2,n+1}=gR_{2,n+1}^{g-1}
\]

follow by taking top homogeneous parts: old carries and the unselected face
terms are strictly lower degree.  Substitution gives the stated scalar
factors (8g) and (g2^{g-1}), with exponents (g+3,2) and
(2(g-1),g-1), respectively.  The base forms
(q_1,q_2,gq_1^{g-1},2q_1^2q_2) are nonzero, and the domain/characteristic
zero hypotheses preserve nonzero positive products at every step.

For exponent supports in the declared full coordinate space
(\mathbb N^4), positive coefficients make product supports exact Minkowski
sums (coincident exponent sums add rather than cancel), so

\[
E_{1,n+1}=(g+3)E_{1,n}+2E_{2,n},\qquad
E_{2,n+1}=2(g-1)E_{1,n}+(g-1)E_{2,n}
\]

is a valid monomial-level refinement of the same (C_g) degree rows.  This
addition stays within the fixed-family, proof-first scope and does not assert
anything about arbitrary supports, words, characteristics, or Newton fans.

## Scope and verdict

The manuscript continues to exclude arbitrary potentials/coefficients/words,
positive characteristic, generic finite Newton-fan theorems, all symplectic
automorphisms, entropy equalities, periodic/trace/multiplier/centralizer or
torus/arithmetic classifications, universal non-conjugacy, priority, and
numerical/CAS proof certificates.  Citations remain bounded context only and
are not promoted to proof or priority evidence.  The coordinate-scoped
support-connectivity and strict comparison with ((g-1)^2) are unchanged.

No source-identity, page-fix authorization, theorem/proof, leading-form,
support, phase-indexing, label/citation, scope, anti-claim, permission, or
provenance blocker was found.  The current page-fixed source is eligible for
the next separately authorized deterministic build and fresh build audits;
this review itself does not authorize that build or any publication action.

PAPER_SOURCE_R1_PAGEFIX_PASS
