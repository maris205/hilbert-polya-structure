# Consolidated hostile review — P103

Audit date: 2026-08-29 UTC
Disposition: **GO for internal Stage 2 after evidence repair / external HOLD**

Two reviewers independent of the P103 author audited the paper in sequence.
The complete records remain in `HOSTILE_REVIEW_B.md` and
`HOSTILE_REVIEW_A.md`.  Review B attacked the initial repaired package;
review A then strengthened the verifier and froze the current canonical tree.

## Severity ledger

- unresolved mathematical CRITICAL: **0**;
- unresolved mathematical MAJOR: **0**;
- repaired evidence-chain MAJOR: **1**;
- repaired MINOR/source findings: **3**;
- unresolved release-only owner gate: **1**.

Review B attached Dolgachev's direct Cremona reference to the in-text
projective-adjugate claim and confirmed the earlier repair of the visible
`,qquad` token.  It independently recovered singular collapse, the `E_k`
iterate, determinant-fibre fixed counts, projective image indices, and the
valuation depth formula.

Review A found that the author-stage controls never exercised a stabilization
time greater than one, despite the manuscript advertising a general image
staircase.  It added literal scalar-line lanes with `t_*=0,1,2,4,1`, requires
strict image loss before `t_*` and equality afterwards, and added full matrix
and determinant iterate checks to the signal lanes.  This is a genuine
evidence strengthening: **850 new assertions**, raising P103 from 140,340 to
**141,190**.  The theorem now also defines `I_0=GL_d(q)` explicitly at the
coprime endpoint and records its nearest P99/P97 internal firewalls.

## Final evidence gate

The canonical verifier still computes two adjugates from signed minors on all
of `M_3(F_2)`, `M_3(F_3)`, and `M_4(F_2)`, and now carries the additional
multi-step scalar-line routes.  Fresh stdout is byte-identical to the stored
output.  The four-stage build passes and yields a clean **4-page A4 PDF of
296,320 bytes**; 23/23 font records are embedded, subsetted, and
Unicode-mapped, and the modified pages passed visual inspection.

Jacobi/hyperadjugate identities, projective adjugation as a Cremona map,
finite-field matrix counts, and scalar power maps are established owners and
receive no novelty credit.  The bounded search did not locate the displayed
full-matrix temporal conjunction, but specialist owner review remains
mandatory.  External posting, submission, contact, venue choice, and
priority language remain **HOLD**.
