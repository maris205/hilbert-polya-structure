# Paper20 — Independent Source-Design Review

Date: 2026-08-22 UTC

Project: `papers/20-coupled-shear-degree-matrix`

Role: fresh post-author independent source-design reviewer

## Verdict and authority boundary

**SOURCE_DESIGN PASS — bounded internal theorem/source scope; publication HOLD.**

I read the repaired, frozen ten-file author package to EOF after the explicit
author stop, independently reproduced its framed aggregate identity twice,
expanded the four map coordinates, replayed the two selector phases and the
invariant cone, checked the carried-coordinate and total-degree comparisons,
recomputed the Perron root, checked the Paper12--19 collision boundary, and
refreshed the bounded primary-source comparison.

The headline theorem and every substantive mathematical gate pass. The only
pre-review source defect was the two naked `qquad` tokens on line 21 of the
superseded design log; the authorized repair changes exactly those tokens to
`\qquad`. The new per-file and aggregate identities below were independently
recomputed in two byte-identical passes. No theorem redesign or unreviewed
author-file change is present.

This review authorizes no manuscript, experiment, code, CAS run, source lock,
transport, build, PDF, publication, release, submission, upload, or external
action. This reviewer-owned file was added only after the ten author files were
frozen and hashed; it is not part of the author aggregate below, and no author
file was modified.

## Exact author input and independent binding

The author allowlist contains exactly ten regular UTF-8 Markdown files, zero
symlinks, and no other source file type; the reviewer-owned report is explicitly
out of band. Every author file has mode `0644`, LF endings, one terminal LF, and
no CR, NUL, or BOM. The independently measured ledger is:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `a0ea0eb5b5ffae47cccac4ddc15f060b2fbeb695cd60930ce516718fc010ecba` | 2,146 | 47 |
| `experiments/EXPERIMENT_TRACKER.md` | `562db5acb674e269cad5e3d17dfb8ff8673601f8411347817276c60e585f5a3f` | 1,232 | 32 |
| `notes/CITATION_VERIFICATION.md` | `bb075a0d7918603062795be88a1adcae932e4d550d0b544e46030f51207fe832` | 5,723 | 48 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `7275171195b4aa2d95df1b4d701b6ae43a5e17778b7f3ce6b94027172e7d4f92` | 5,607 | 48 |
| `notes/NOVELTY_ASSESSMENT.md` | `762bd9352641feffe6db5b9426d4a7b657509d7fb6bb9b065b32e7be391d9a2b` | 5,840 | 102 |
| `notes/PROOF_PACKAGE.md` | `c111c75a11714c7b401583fdc459549ab4c0f783a1064112b495794e2e7e4baa` | 9,407 | 269 |
| `notes/RESEARCH_QUESTION.md` | `eee1350eeefb818f240328493a16d3036df7bdb028a86016594bb8e26d956b86` | 5,150 | 88 |
| `refine-logs/FINAL_PROPOSAL.md` | `186036967ecda1f8ba82f61c6b5d3ea086b010693a54476391512dba482a8ee5` | 4,156 | 100 |
| `refine-logs/INITIAL_PROPOSAL.md` | `48bec53019c21662033e9e3dbef6f180d60e6868d1f5169dbf2643604bc0fb2e` | 3,447 | 88 |
| `refine-logs/REVIEW_SUMMARY.md` | `838bf872a4902fbd193d3045972a518fda55d059c0892f1080e6e352ccb1f1fa` | 2,708 | 51 |

Total author input: **45,416 bytes and 873 LF**.

For the aggregate, I sorted the ten relative POSIX names bytewise and fed, for
each record,

`uint64_be(name_bytes) || name || uint64_be(content_bytes) || content`

with no separators or terminal record. The independently reproduced author
aggregate is

`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.

Two post-stop passes produced the same individual and aggregate identities. The
review file itself is excluded from this ten-file framing and from all author
source scans.

## Independent theorem replay

### Map and symplecticity — PASS

With

`V=q1^2 q2^2+q1^g` and `W=p1^2 p2^2+p2^g`,

the intermediate coordinates are

`p1hat=p1+2 q1 q2^2+g q1^(g-1)` and
`p2hat=p2+2 q1^2 q2`.

The final coordinates are

`q1'=q1+2 p1hat p2hat^2`,
`q2'=q2+2 p1hat^2 p2hat+g p2hat^(g-1)`, and
`p'=phat`.

The inverse of each triangular shear is obtained by negating its potential.
The pullback of the standard symplectic form has an additional Hessian term,
which vanishes because the Hessian is symmetric and wedge products are
antisymmetric.

### First phase and carried terms — PASS

For `r=u2/u1` in `1 <= r < (g-2)/2`, the two candidate degrees in the first
gradient coordinate are `u1+2u2` and `(g-1)u1`; the latter is strictly larger.
The other selected degree is `2u1+u2`. Thus

`v_(n+1)=A u_n`, with `A=[[g-1,0],[2,1]]`.

At the first step `A(1,1)=(g-1,3)` strictly dominates the degree-one carried
`p` coordinates. At later steps, `u_n>u_(n-1)` componentwise and the two rows
of `A` give `A u_n>A u_(n-1)`, so the carried final `p` vector cannot change
the selected degrees.

### Second phase and cone — PASS

For `v=A u`, the cross term is the only nonlinear term in the first `W`
gradient coordinate. In the second coordinate the pure term dominates exactly
when

`v2/v1 > 2/(g-2)`.

Since `v2/v1=(2+r)/(g-1) >= 3/(g-1) > 2/(g-2)` for `g>4`, the selected matrix
is `B=[[1,2],[0,g-1]]`. Both selected degrees strictly dominate the carried
`q` degrees.

The complete-step matrix is therefore

`C=BA=[[g+3,2],[2(g-1),g-1]]`,

not the off-diagonal half-step matrix. Its ratio map is

`f_g(r)=(g-1)(2+r)/(g+3+2r)`.

It is increasing. At the lower endpoint `f_g(1)=3(g-1)/(g+5)>1`; at
`R=(g-2)/2`, the inequality `f_g(R)<R` reduces to `g(g-4)>0`. Hence the
half-open cone is forward invariant for every integer `g>=5`.

### No cancellation, visibility, and Perron root — PASS

Every displayed operation uses addition, multiplication, and the images of
positive integers. Starting from coefficient-one coordinate monomials, all
iterate coefficients lie in the image of the nonnegative integers; in
characteristic zero the selected coefficients remain nonzero. Together with
the strict degree gaps, this rules out leading cancellation.

The differences `C u-A u` are

`(4u1+2u2, (2g-4)u1+(g-2)u2)`,

so the final `q` degrees dominate the final `p` degrees. Cone invariance gives
`u_(n,2)>u_(n,1)` for `n>=1`; consequently the second `q` coordinate is the
total-degree observable and

`deg(F^n)=e2^T C^n (1,1)^T`.

The trace and determinant of `C` are `2g+2` and `(g-1)^2`; the discriminant is
`16g`. Hence the Perron root is

`g+1+2sqrt(g)=(sqrt(g)+1)^2`.

The positive initial vector and the positive observable see the Perron class,
so this is the first dynamical degree. Finally,

`(g-1)^2-(sqrt(g)+1)^2=sqrt(g)(sqrt(g)-2)(sqrt(g)+1)^2>0`

for `g>=5`. No topological-entropy conclusion is needed or stated.

## Collision, citation, and novelty audit

The Paper12--19 source questions concern low-period residues and traces,
primitive-cycle covers, torus escape, marked boundary ramification, and
shift-like torus-coset/translate geometry. None uses dynamical-degree growth,
Newton-face degree matrices, or Perron degree observables as a primary object.
The collision table is therefore accurate at the stated bounded level.

The corrected citation IDs are internally consistent:

- `S01`/`S07` cover the planar Hénon/classification background;
- `S02` is Déserti's higher-dimensional degree-growth paper;
- `S05` supplies general spectral language for dynamical degrees; and
- `S06` is the four-dimensional coupled-Hénon hyperbolicity neighbor.

The primary Friedland--Milnor source explicitly states the reduced-word degree
product. Déserti's abstract confirms higher-dimensional degree-growth regimes;
Dang--Favre gives the spectral interpretation context; and the coupled-Hénon
paper studies a four-dimensional symplectic map for horseshoes and
hyperbolicity, not this degree formula. A bounded exact-formula/support search
found no direct collision. This is not an exhaustive priority search and does
not justify “first,” “unique,” or equivalent language.

Conservative independent scores remain: novelty **8.1/10**, standalone scope
**8.0/10**, and proof confidence **9.2/10**. These are bounded design scores,
not a priority certificate.

## Anti-claim and permission audit

The package consistently excludes arbitrary supports and words, arbitrary or
sign-changing coefficients, positive characteristic, generic finite-fan
closure, all symplectic automorphisms, product non-conjugacy, topological or
arithmetic entropy, periodic points, traces, torus geometry, and priority.

Before this review there were no manuscript, plan, build, experiment, data,
figure, source-lock, or transport artifacts under the project. The experiment
tracker records zero runs, and nothing in the theorem proof depends on a
numerical or CAS certificate. The parent-authorized independent review is the
only action taken after author stop.

## Repair verification and final gate

At `refine-logs/INITIAL_PROPOSAL.md:21`, both formerly naked tokens now carry
the required backslash (`\qquad`). The file is 3,447 bytes with SHA-256
`48bec53019c21662033e9e3dbef6f180d60e6868d1f5169dbf2643604bc0fb2e`; all nine
other author-file identities are unchanged, and the framed ten-file aggregate
is `3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90` over
45,416 bytes. No naked `qquad`, CR, NUL, BOM, or downstream manuscript/build/
transport artifact occurs in the author scope.

The final source-design gate is therefore **PASS** for the stated bounded
internal theorem package. Publication, manuscript drafting, experiments, code,
CAS runs, source locks, transport, build, upload, release, and priority claims
remain explicitly **HOLD**.
