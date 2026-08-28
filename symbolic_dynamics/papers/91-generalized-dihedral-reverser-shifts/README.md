# P91 — generalized-dihedral reverser shifts

Status: **internal mathematical GO; external release HOLD**.

This four-page anonymous `amsart` note studies, for `G=Dih(A)`, the directed
one-step relation
`g -> h` iff `hgh^{-1}=g^{-1}`. It proves mixing, complete spectral and zeta
compression to `(N,t)=(|A|,|A[2]|)`, and family conjugacy rigidity from the
first two periodic counts. The full-shift endpoint `N=t` is treated
separately.

An internal two-round hostile audit was completed on 2026-08-28. It
rederived the group-law orientation, completed the invariant-space proof,
added the endpoint zeta and explicit first-period traces, tightened the
two-count rigidity argument, and expanded the deterministic control from
10,682 to **12,175 exact assertions** on 20 finite-abelian presentations.
This audit is not external peer review.

## Reproduce

From this directory:

```bash
python3 code/verify_reverser_shift.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
sha256sum -c SHA256SUMS
```

The control requires Python 3 and SymPy.  All comparisons are exact integer,
rational, or symbolic-polynomial identities.

The final PDF is 4 A4 pages, 296,997 bytes, with SHA-256
`196160eff81a974c496e0259ca15f73e9b8fcf6a7838cf5afef193ef0c5c6df6`.

## Ownership boundary

Reversing elements, generalized-dihedral groups, commuting graphs, equitable
decompositions, Parry theory, and SFT determinant identities are prior tools.
A bounded relation/parameter search found no direct owner of this exact
directed reverser shift, but this is not an exhaustive novelty search. The
construction is elementary enough, and its components classical enough, that
owner risk remains **medium**. The classification is only inside the named
family and does not classify groups or arbitrary relation shifts.

Evidence cutoff: 2026-08-28 UTC. No public posting, submission, or absolute
novelty/priority claim is authorized.
