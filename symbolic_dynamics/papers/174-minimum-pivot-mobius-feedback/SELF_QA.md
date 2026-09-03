# P174 final Round-2 QA

**Verdict:** `PASS / PROVISIONAL_AMBER / HOLD_EXTERNAL`  
**Scope:** mathematics, claim boundary, source verification, exact replay,
build, anonymity, and rendered PDF  
**Independent hostile reviews:** both complete; all findings closed

## Mathematical QA

- The carrier is exactly the `k`-subsets of `P^1(F_p)` with prime `p` and
  `2<=k<=p`; the lower bound guarantees a finite pivot and the upper bound
  guarantees a depth-two state.
- The integer representative order is declared part of the literal map, so
  no projective-naturalness claim is implicit.
- The projective branches `a->infinity` and `infinity->0` are explicit.
  They prove the two nested images in both directions, not merely as upper
  bounds.
- States in `Y`, `Z\Y`, and `X\Z` are shown pointwise to have tails zero,
  one, and two.  Their binomial counts partition the whole carrier.
- Once a state reaches `Y`, its pivot is zero and the map is projective
  inversion.  This proves all recurrent periods are one or two and proves
  `M^4=M^2` on transient as well as recurrent states.
- The odd-prime fixed coefficient treats `1` and `-1` as singleton inversion
  orbits and the remaining nonzero points as pairs.  The manuscript handles
  `(p,k)=(2,2)` separately rather than forcing the odd formula.
- Fixed-iterate and weak-component counts follow only after recurrence and
  cycle structure are established.
- For a proposed pivot `a`, the inverse projectivity forces a unique parent.
  The modular inequality distinguishes wrap from no wrap and yields exactly
  `0<=a<h(T)`.
- The pivot polynomial records each valid pivot with coefficient one; source
  uniqueness is justified by the least finite point.
- The fibre distribution separates targets that contain zero from those
  that do not and uses Pascal's identity.  Its `j=0` boundary is checked
  separately.  The maximum-fibre and mass identities follow.
- The one-step inverse specifies every branch of every depth-two component,
  so “complete graph” is not based on aggregate level counts alone.

The proof status is `PROVABLE AS STATED`.  That mathematical judgment does
not upgrade the owner/value status beyond provisional amber.

## Source and internal-boundary QA

- `references.bib` contains exactly five cited records.
- Four published records were checked through DOI/Crossref and primary
  publisher, repository, or author surfaces; Grinberg--Mao was checked on the
  live primary arXiv v4 record.
- The old Aluffi--Faber DOI deposit lacks author/title metadata, so the author
  PDF and journal record were used to confirm those fields.
- El Abdalaoui--Shparlinski receives credit only for fixed Möbius dynamics;
  Tricot and Aluffi--Faber receive credit only for projective subset and
  configuration actions.
- Grinberg--Mao is cited only as quotient/group-action pressure relevant to
  the killed AQN control, not as an input to the P174 theorem.
- Jefferson et al. is cited only for ordered minimal/canonical images and
  canonizing elements; P174's orbit-nonconstant feedback, containment tower,
  and target-dependent pivot interval are explicitly distinguished.
- P96 fixed-map hyperspace machinery, P168 inverse-span machinery, and AQN's
  adaptive-normalization architecture are visibly assigned zero credit in
  the main text.
- The manuscript says explicitly that its bounded literal-owner non-hit is
  not novelty, priority, ownership, or freedom-to-operate evidence.
- No uncited BibTeX entry, unresolved citation placeholder, or invented
  source remains.

## Verifier QA

Two fresh processes produced the same 24,534-byte, 1,149-line transcript;
both match `verification_output.txt` byte for byte.  Each run reports
131,018,555 explicit checks in 69 complete parameter boxes.  The transcript
SHA-256 is
`1faac49f7cb9cdfb7be13caf1a533f36a07851cdff1a9a955b85a3ec593e0646`.

The script parses under Python 3.12.3, uses only the standard library, imports
no scouting implementation, and freezes one complete-edge digest per box.
Its output records `AUTHOR_ROUND0_PASS` and
`PROVISIONAL_AMBER / HOLD_EXTERNAL`.

## Build and PDF QA

- canonical settling sequence: `pdflatex`, `bibtex`, `pdflatex`,
  `pdflatex`;
- two additional source-only cold builds: both passed and matched the
  canonical PDF byte for byte;
- canonical and cold settled logs: zero warnings, bad boxes, unresolved
  references/citations, rerun requests, or fatal errors;
- PDF: four A4 pages, 321,776 bytes, SHA-256
  `b428c24be406d8c2cef9c1d6fc5a2630495f2eed54473ed1dec7b1120444ff7f`;
- `main_round2.pdf` is byte-identical to `main.pdf`; Round 0 and Round 1 are
  preserved separately;
- all 25 font rows are embedded, subsetted, and Unicode mapped;
- metadata title, author, subject, keywords, creator, and producer fields are
  blank; the file is unencrypted and has no form or JavaScript;
- extracted text contains no unresolved marker, email address, filesystem
  path, affiliation, acknowledgement, or nonanonymous author identifier.

## Visual and lifecycle QA

All four pages were rendered at 144 dpi and inspected.  No clipping,
collision, overflow, orphaned heading, malformed formula, missing glyph, or
unreadable table cell was found.  The long theorem, modular-wrap display,
exact-control table, boundary chain, references, and proof endings were
checked specifically.

The byline and running heads are anonymous.  The exact lifecycle string
`PROVISIONAL_AMBER / HOLD_EXTERNAL` is visible in the manuscript.  Review A
passed 161,536 independent assertions with no finding; Review B passed
4,755,152 and its one minor source repair is delta-accepted.  This is an
internal final package, not authorization for external circulation.
