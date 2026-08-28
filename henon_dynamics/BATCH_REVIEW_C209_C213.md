# Route-A batch review: C209--C213

Date: 2026-08-28
Source baseline locked by the packages: `e8054522273dbd545f9d406978e5d4648c627918`
Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`
Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## What advanced

This is a five-owner cross-subtype round.  Each paper closes one complete
source theorem and its singular/boundary cases; none is a parameter slice of
another paper.

| ID | Frozen owner | Theorem-scale advance | Route-A tuple | Final PDF SHA-256 |
|---|---|---|---|---|
| C209 | ordinary Kreweras complement on `NC(n)` | all-iterate fixed ledger (source-attributed CSP), exact Möbius periods/cycles, finite zeta, Koopman spectrum, rank duality, reflection reversors, and the `1,2,2n` order boundary | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` | `79318d957ab3fdd8560d232e195dcdb0eb4febe7c312bd75a6f7a8c1011105cb` |
| C210 | scalar retarded delay | Lambert-W roots and multiplicity, exact method-of-steps resolvent, eventual compactness/spectral mapping with collision aggregation, and the complete nonnegative stability/Hopf atlas | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `13c4900f1df2e4b2d7e00075adcc5913d41826e389fa789a12acd64c5c1ebd0e` |
| C211 | positive Hamiltonian Lotka--Volterra | strict-convex global period annulus, Lambert-W turning branches, area/period/action quadratures, center limit, and exact cycle averages | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `50298402105c9fbeb5bb642c0397caa6c18dd9cfeac922543cd5aaa070192461` |
| C212 | affine-impact bouncing ball | exact affine event map and physical roof sums, sharp Zeno/sticking split, forced cycle, elastic/translation boundaries, and regular-vs-closed formal series | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `f6cc08eb6a122eebf0d27a7c2d6b213de3b59cbe5b2c11179958f382026c582b` |
| C213 | circular telegraph Markov process | exact all-mode Fourier exponentials, critical Jordan blocks, telegraph equation, spectral-abscissa gap, stationary faces, and essential-norm/noncompactness boundary | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `dc8d5e0e5474290f12bdd50f8a409f7b350db88ede7a3e14923df6532b50b124` |

The tuples are package-local evaluations, not transferred scores.  Every
package is `ROUTE_A_REJECTED`; every `route_b_invocation_allowed` value is
false.  The negative result is part of the progress: no paper manufactures a
prime clock, target divisor, Euler factor, root number, automorphy statement,
or Hilbert--Polya operator.

## Reproducibility and hostile audit

Each directory contains exactly 28 physical files: 27 content-addressed
payloads plus a self-excluded release manifest.  There are no LaTeX sidecars,
Python caches, symlinks, or untracked generated outputs inside the five
packages.  The final PDF equals `main_round2.pdf`; the three retained revision
PDF hashes are pairwise distinct.  Two fresh fixed-epoch two-pass LuaLaTeX
builds per final source were byte-identical, with embedded/subsetted fonts,
clean stabilized logs, extractable text, and page-level visual inspection.

| ID | checker | SymPy | hostile (repaired + stale) | payload SHA-256 | evidence SHA-256 | manifest SHA-256 |
|---|---:|---:|---:|---|---|---|
| C209 | 8,025 | 1,110 | 33 (32+1) | `962d35dca28d8777333687a79c2ac77bcdf43f7d1536e472bf710d2d28dfda1b` | `a3ae942ddbbae61e10692fe5782e7f9974f20066228e3c41e3e7f365b42b3254` | `dfd0f541e29c177658f59307f9cbda8890802433cd52666c345160a3ccd17228` |
| C210 | 358 | 179 | 25 (24+1) | `8ea5f16b4bf9a88c507f2069ed6b0f32a87275d53940c72cbf0f5d64ac8dae2f` | `97b1030818cc941f8766774d63864f217ee551d838e9164a3f9968c2f791718e` | `ab2d5e785387fa4bd584a87f618e49b50d7ff6e2af7b7691a81618803feb7a64` |
| C211 | 732 | 12 | 12 (11+1) | `fe47c6de6ab657c6ce5cda988a4dbe0802820aa3726004237a02b703fab12c56` | `bf80cd8c8322ac11a5f7f8131024c44418c1f1759a55f7cf457e520ff950fdb0` | `a4f0056f3cb3e7e647706bb042825e132ca92d884d18b34f81046f07e3944046` |
| C212 | 368 | 11 | 14 (13+1) | `a57cf59f1b4f6b404b83e6ef8c4bfae1c76c711bee8cea75b4f36e327bf31334` | `a0738f4307e93ed6e27164a8ad5492ca895d5d49f5f3e5b5dac78e1d5f718277` | `7d6a2ef027c0231f90165f218cb8f6a59026b5d8c0511a5e52223325d89d9df6` |
| C213 | 20,923 | 2,133 | 27 (26+1) | `a172c2740c79abc5a146e23895fec5ebb03c72f98ac7925a5b841a3a08e8f9e7` | `7b1fe9b4f14682e9072a887271af50aa157997fedad01f1b0f9cebd5807a9fc3` | `4a62f31e16cc14f02955c822b38d1833c36f818d3ce73f12714c5ac72fa187e5` |
| **total** | **30,406** | **3,445** | **111** | **135 payloads** |  | **13 PDF pages** |

The producer/checker boundaries are independent: C209 directly enumerates
2,055 partitions through `n=8`; C210 checks 156 method-of-steps cells; C211
reintegrates 24 heterogeneous periods with DOP853; C212 checks 96 exact roof
cells and 36 impact cells; C213 checks 700 blocks (2,800 entries) and 25 gap
rows at 100-digit working precision.  All five replay scripts regenerate the
canonical receipts byte-for-byte.

## Cross-review repairs and source audit

The internal read-only cross-audits found and closed the following issues:

- C209: the order proof now separates odd `n` (rank reversal) from even `n`
  (the nontrivial half-turn), while retaining the actual-order/CSP-order
  distinction at `n=2`.
- C210: the zero-delay branch, Lambert branch-point condition, Hopf crossings,
  exponential spectral-collision aggregation, and hostile counts are explicit.
- C211: convex-level connectedness, canonical Hamilton equations, coarea time
  identity, heterogeneous period integration, and all result counts are
  explicit.
- C212: `r=0,J=0` is one-flight sticking rather than infinite Zeno; the formal
  closed-section affine series is separated from physical-flow cycles.
- C213: the backward generator/adjoint density convention, `c>0` telegraph
  elimination, periodic `H^1` domain, and essential-*norm* title are explicit.
  The final source also suppresses optional PDF metadata so independent build
  directories reproduce the same bytes.

Primary source metadata were checked against DOI records: Kreweras (1972),
Reiner--Stanton--White (2004), and Bessis--Reiner (2011) for C209;
Hale--Verduyn Lunel (1993) for C210; Waldvogel (1983, 1986) and Hsu (1983)
for C211; Leine--Nijmeijer (2004) and Goebel--Sanfelice--Teel (2012) for
C212; and Kac (1974) for C213.  Source-derived statements are labelled as
such; the finite grids are regression evidence, not proofs of infinite
quantifiers or external peer review.

## Completion decision

The five theorem packages, evaluator receipts, manifests, cross-review, scope
firewall, README/index entries, and registries are closed for this batch.
The next user checkpoint is before selecting C214--C218.
