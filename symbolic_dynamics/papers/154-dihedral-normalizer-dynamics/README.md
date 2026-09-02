# P154 — Dihedral subgroup-normalizer dynamics

Status: **ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL**.

This directory contains an anonymous amsart short paper on iteration of

    H -> N_{D_{2n}}(H)

over the complete subgroup set of D_{2n}, for n at least 3.

The subgroup coordinates and complete one-step normalizer formula are
classical, explicitly cited, and assigned zero contribution credit. The paper
starts from their iterated consequences: binary forests, all-time target
fibres, an exact unlabelled-graph signature, and arithmetic collisions.

## Main outcome

For n=2^a m with m odd, the dihedral states form sigma(m) full binary inverse
trees of height a. Every rotation subgroup is an extra depth-one source into
the distinguished root. The graph is classified exactly by
(a,sigma(m),tau(n)); in particular 33 and 35 have conjugate graphs.

Run python3 verify.py and compare stdout with CANONICAL.txt.
Build the PDF using the settled five-command sequence in BUILD.md.

`main_round0_original.pdf` preserves the author freeze, and
`main_round1.pdf` preserves the Review-A repair freeze. Hostile Review B
returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. A subsequent
independent final cold-QA found one latent pdfTeX font-expansion warning, so
Round 2 changes only the typesetting preamble to disable microtype expansion
while retaining protrusion; no theorem, proof, bibliography, verifier, or
transcript changed. `main_round1.pdf` remains the five-page, 375,182-byte
Review-A artifact at SHA-256
`aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b`.
The current `main.pdf` and `main_round2.pdf` are byte-identical five-page A4
artifacts (373,090 bytes) at SHA-256
`72b99fe5f4813434cccb3aef9f8a023d0e7ca471029ce9831b4228dfe8db90cd`.

External state: HOLD_EXTERNAL.
