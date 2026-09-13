# Paper 27 publication lock (internal control record)

## Lock identity and purpose

This record freezes the publication-stage contract for candidate
`positive_newton_translation_reciprocity_v5`.  It is an internal control
record and is not part of the anonymous article.  It grants no upload,
submission, hosting, repository, identity, messaging, or other external
effect.  It records the exact scope that a later source author must implement
and the checks that a later source reviewer must complete.

The accepted article title is *Diagonal-Translation Rigidity and Phase
Reciprocity in Positive Newton-Fan Hamiltonian Shears*.  It is a proof-only
mathematical theory article with a 24--28 proof-content-page target (planned
budget 25.7 pages through the conclusion; references and a routine appendix
are outside the count).  The scope was independently passed by the fresh R2
publication-scope review ending in
`BATCH07_PAPER27_PUBLICATION_SCOPE_PASS`; the review file is the exact
13,024-byte, 224-LF, regular-0644/link-one artifact recorded in the ledger.

## Frozen theorem contract

The manuscript may state only the following certified-branch theorem family.

* Work over a characteristic-zero coefficient field.  The dimension is
  (r\ge 3), and the collected supports (E_V,E_W\subset
  \mathbb Z_{\ge 2}^{\,r}) are finite and nonempty, with nonzero
  coefficients.  A conclusion is attached to a certified strict edge: the
  exposed selectors are unique, the required carries are positive, and the
  printed target/score certificates hold.  The grouped positive-face Hessian,
  Jacobian, and injective-substitution argument must be coefficient-uniform
  over this class.
* For
  (S_V(q,p)=(q,p+\nabla V(q))),
  (T_W(q,p)=(q+\nabla W(p),p)), and (F=T_W\circ S_V), define
  (A_\alpha=\mathbf 1\alpha^{\mathsf T}-I) and
  (B_\beta=\mathbf 1\beta^{\mathsf T}-I).  On a certified forward edge
  the leading phase is
  ((u,w)\mapsto(B_\beta A_\alpha u,A_\alpha u)), while the inverse
  phase is W first and V second with the corresponding subtraction signs.
* With support functions (h_V,h_W), every certified edge obeys
  (v=h_V(u)\mathbf 1-u) and
  (u'=h_W(v)\mathbf 1-v=u+\delta\mathbf 1),
  where (delta=h_W(v)-h_V(u)>0).  For integer seeds, strictness gives
  (delta\in\mathbb Z_{\ge1}).  On every infinite certified strict branch,
  selector changes are at most (d_V+d_W-2); after a stationary selector
  pair is reached, and without resetting the global origin (u_0),
  (t_{n+1}=\lambda t_n+\mu) with
  \(\lambda=(|\alpha|-1)(|\beta|-1)\) and
  \(\mu=((|\beta|-1)\alpha-\beta)\cdot u_0\).
* Under coordinate reversal (R) and
  (R_{\rm state}(u,w)=(Rw,Ru)), reflected inverse reciprocity is
  necessary and sufficient edgewise on the observable spans (U_e,V_e),
  provided reflected selector, carry, and target certificates are present.
  Full-matrix identities are allowed only when the relevant spans are full.
* The lower-ideal statement is a one-edge, one-step lemma on one typed pair
  core using four normalized projections and selected-minus-new margins.  It
  does not assert target-core inclusion, a transition-core perturbation
  theorem, multi-edge stability, or all-iterate stability.

The exact asymmetric three-dimensional fixture and the cancellation and
missing-reflection fixtures are witnesses and boundaries only.  They may not
be used as substitutes for the universal proofs.  The article must preserve
all finite-branch stopping cases (ties, failed carries, empty cells, and
missing certificates) and must state the anti-claims in the locked proof
package.

## Required anonymous source trio

After this lock is independently passed, a later source-author event may
create exactly these three regular files and no other manuscript source path:

1. `papers/27-positive-newton-translation-reciprocity/paper/main.tex` is the
   complete anonymous article, with the abstract and all eight body sections
   embedded in this file.  It may use relative `\input{math_commands.tex}`
   and `\bibliography{references}` only.
2. `papers/27-positive-newton-translation-reciprocity/paper/math_commands.tex`
   contains notation macros only; it may not contain theorem text, claims,
   provenance, or process metadata.
3. `papers/27-positive-newton-translation-reciprocity/paper/references.bib`
   contains only verified records that are actually cited by `main.tex`.

No section `.tex` files, figure assets, data, code, experiment output,
custom package, supplementary archive, cache, or generated file belongs in
the trio.  Symbolic diagrams must be native LaTeX constructs with no external
asset dependency.  The source author must use the corrected typed notation:
the u-only cone is separate from the pair cell that contains w-dependent,
reflected, carry, and target predicates.

## Required article organization and evidence

The abstract is unnumbered and contains no citation, priority wording, or
computational claim.  The body has exactly these eight sections:

1. Introduction and contribution boundary.
2. Related work and claim-level collision positioning.
3. Typed setup, strict cells, and omnibus theorem.
4. Positive-face survival and degree transport proofs.
5. Translation, wall monotonicity, and affine tail proofs.
6. Reflected inverse reciprocity and its span criterion.
7. Local lower-ideal lemma and exact fixture.
8. Boundaries, limitations, reproducibility, and conclusion.

Every theorem-critical derivation must appear in the main body or be
explicitly referenced to a routine appendix.  Section 2 must synthesize only
the verified S01--S20 records by methodological family and must call the
literature check a bounded public screen through 2026-08-29 UTC, never a
first, unique, exhaustive, or priority claim.  The exact fixture table must
print its selectors, matrices, products, gaps, carries, seeds, determinant
checks, and reflected path; the cancellation and missing-reflection examples
must be labeled as limitations.

## Citation, anonymity, and reproducibility firewall

Only records in the verified citation package (or records independently
reverified at the later source gate) may be cited.  Each bibliography entry
must have verified author, title, year, and venue or record identifier, and
every entry must be cited.  No citation is evidence for the theorem itself;
no BibTeX field may contain internal event IDs, filesystem paths, hashes,
reviewer names, candidate IDs, or process notes.

The three anonymous source files must contain no author names, affiliations,
acknowledgements, internal event IDs, paths, hashes, reviewer names,
repository or governance language, private URLs, or provenance breadcrumbs.
They must contain no empirical results, numerical fits, CAS certificates,
broad scans, GPU claims, or hidden computational assertions.  Neutral
anonymous authorship and self-reference are required.  The source must not
mention this control record or its workflow.

Before source PASS, a fresh source reviewer must freeze raw bytes and verify
strict UTF-8/LF, one terminal LF, regular mode 0644, link count one, no BOM,
CR, or NUL, balanced delimiters, no stale section files, no external asset,
and no uncited bibliography entry.  A source PASS freezes the trio.  Any
repair requires a separately named revision, a new manifest, and a fresh
source reviewer; silent in-place polishing is forbidden.

## Downstream handoff and prohibited effects

Only after an independent publication-lock PASS may the ledger authorize
creation of the `paper/` directory and the exact trio.  Source review,
build-profile review, deterministic roots, compilation, PDF inspection,
finalization, and local release each require their own later authorizations
and independent roles.  This lock does not authorize any of them.  No build
root, auxiliary file, PDF, release copy, upload, submission, hosting,
repository push, external message, or identity disclosure may be created or
performed at this stage.

BATCH07_PAPER27_PUBLICATION_LOCK_FROZEN
