# Evidence record — unary divisor coherence

**Candidate ID:** `ANG-20260918-UDC01`  
**Status:** `GLOBAL OWNER AND SECTOR LEAKAGE; MIXED-SUPPORT RETURN — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Exact inputs and reproducibility

The [version-1 card](../candidate-card.md) preceded its owner and return
audit. The full integer index set, single edge weights, log diagonal,
ordinary norm shell and physical mild equation are its complete inputs.
No empirical data, parameter fit or external theorem about an unrelated
operator is used.

The [paper](../paper.md) gives these exact proof steps:

1. Parametrize each undirected proper-divisor edge by (a,ab), count the two
   matrix orientations, and sum squared coefficients. Elementary integral
   bounds yield norm(K)<1/2<log2.
2. Construct the interaction-picture bounded linear ODE, preserve its norm
   and use uniqueness of the original autonomous mild equation for the group law.
3. Read the e_6 derivatives directly from the same full equation.
4. Use bounded Rayleigh energy and the explicit log-tail estimate for a
   strong H0 subsequential limit; pass the bounded K pairing to that limit.
5. Take absolute values, derive the coordinate multiplier equation, repair
   the strong domain, and propagate positivity along the connected graph.
6. Verify the scalar-phase curve in the full physical equation and identify
   its complete return-time subgroup.

There is no numerical eigenvector, floating precision, finite spectral
matrix, orbit integration, cutoff-derived theorem or GPU result. The
finite-coordinate tail is a compactness proof, not a computational proxy.
Naturalness, other packets, stability and trace structures remain open.

## Comparison and review scope

The bounded collision check compared 186, 192/SC18-F, 193 and 233--235.
It identified this as a changed interaction and norm shell, not as a
renamed previous owner. This is not a literature-wide novelty claim.

A separate read-only checker received the frozen card and independently
derived the owner and first return discriminator. Its actual readback of
all five written files on 2026-09-18 found no conclusion-changing constant,
domain, return-time or scope error. In particular it checked the exact
5/32 bound, adjoint-domain identity, full mild action, log-tail compactness,
post-variation domain repair, connected-graph positivity and return group.
The readback paper.md SHA-256 was
`e33235d2a5b4dc54aec4eade918258f730708c22ed2f6220b84b59fac5d634dd`.

Its sole optional suggestion was to state explicitly the form norm on Y.
Root added norm(z)_Y squared=q_L(z) after (3), without changing the main
carrier or proof. The checker verified this exact delta and reported the
final paper.md SHA-256
`f01bcd1b094e59de064cb19fd5e3a177c4082bc732e061a49bb001c7ce89296a`.

This is same-runtime model checking, not external peer review or a
correctness certificate. No unpublished material was uploaded to an
external service. ARS informed explicit lineage, controls and
claim/evidence separation. Mechanical integration is recorded separately
below and does not certify mathematical correctness.

## Root integration receipt — 2026-09-18

Root explicitly read all five Markdown files in each of 236 and 237 and
the two stream indexes in a read-only Node check. It verified exact IDs,
current statuses, UNASSIGNED, NOT INVOKED, final LF/absence of CR, and local
link-path existence after removing code and stripping fragments. Remote
URLs and fragment anchors were not validated. The method and inputs are
also recorded in 236's evidence index. Observed totals were 10 package
files, 60 package-local links, two index files and 451 index-local links,
with zero errors. The new untracked packages were checked directly, not
assumed included in a Git diff.

`git diff --check -- readme.md papers/README.md` exited 0 without diagnostics.
`sha256sum papers/236-cross-sector-frontier/paper.md papers/237-unary-divisor-coherence/paper.md`
matched the final review hashes, including UDC01's explicit form norm.
No proof was inferred from these mechanical checks, and no unrelated work,
earlier negative record or frozen input was rewritten.
