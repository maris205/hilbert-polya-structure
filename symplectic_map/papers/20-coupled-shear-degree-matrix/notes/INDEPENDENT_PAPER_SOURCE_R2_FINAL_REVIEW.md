# Paper20 independent manuscript-source review (R2 final citation repair)

**Review ID:** PAPER_SOURCE_R2_FINAL_2026_08_22

This receipt applies only to the final author-stopped identities below. It
supersedes the provisional BibTeX pass and its subsequent correction for the
preceding bibliography hashes. The review was read-only: no compilation,
BibTeX run, CAS, experiment, transport access, upload, or author-file edit was
performed.

## Hash-bound identity

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| paper/main.tex | 37,423 | 981 | 2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014 |
| paper/math_commands.tex | 702 | 20 | 37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582 |
| paper/references.bib | 2,335 | 73 | 529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf |
| paper/BUILD_METADATA_R0.json | 3,588 | 1 | 75e94cc9da7dd738fd287db32994fb98863d65c00350201ac6c77e48d017cc9c |

The source lock is unchanged:
57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581,
11,847 bytes/LF1. The plan row remains
4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3,
22,064 bytes/LF397.

## Citation-file repair

The two affected titles now keep their superscripts inside math mode:

    title = {Dynamics of polynomial automorphisms of {$\mathbb C^k$}},
    title = {Dynamical compactifications of {$\mathbb C^2$}},

The seven BibTeX keys are unique and every key cited by the unchanged
main.tex resolves exactly once. Braces and quotes balance; the file is
UTF-8/LF-only with no CR, NUL, or BOM and one terminal LF. The corrected
expressions are TeX-safe; unlike the preceding {$\mathbb C$}^k form, no
superscript is left outside math mode.

BUILD_METADATA_R0.json is canonical JSON with recursive Unicode-key ordering,
strict duplicate/nonfinite rejection, null self identity, and byte-exact
roundtrip. Its source rows match all four current files and the upstream plan.
Build/CAS/experiment/data/figure/publication/transport/upload permissions are
false; planned build is NOT_RUN with null artifact identities.

## Manuscript theorem and source gates

main.tex is unchanged from the passed label-repaired identity. The four
selector-gap displays are numbered equations, eq:ratiomap is not retained,
all 40 labels are unique/resolved, no label is inside an unnumbered display,
and all TeX environment/delimiter balances pass.

The locked L1--L7 proof remains faithful: triangular symplectic inverses;
literal A_g and B_g support rows; the two-phase cone
1 <= u_2/u_1 < (g-2)/2 and its ratio-map invariance; carried-coordinate
gaps and positive-coefficient no-cancellation; u_(n+1)=C_g u_n with q_2
degree visibility; and Perron roots (sqrt(g)+/-1)^2 with the strict
comparison to (g-1)^2. The P12--P19 collision boundary, bounded citation
roles, anti-claims, and no-priority wording remain unchanged. No forbidden
build, result, figure, PDF, or transport output exists.

## Verdict

PAPER_SOURCE_R2_PASS

The final manuscript source is hash-consistent, citation- and TeX-safe at
source level, theorem-faithful, label-safe, and permission-safe. This is a
source review only and authorizes no compilation, publication, transport,
experiment, or downstream artifact.
