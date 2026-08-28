# P90 — particle-resolved Rule 184 dynamics

Status: **internal mathematical GO; external release HOLD**.

This five-page anonymous `amsart` note takes the classical finite-ring
no-`11`/no-`00` recurrent-core description of Rule 184 as prior background.
Its residual package is:

- the sharp layerwise first-entry depth
  `(min(m,n-m)-1)_+`;
- a min-plus formula for every labeled particle position;
- the complete particle-weighted `F_n^k` fixed polynomial;
- exact temporal orbit counts, their particle refinement, and the finite-map
  Artin–Mazur zeta function;
- the microcanonical recurrent-state exponent.

An internal two-round hostile audit was completed on 2026-08-28. It corrected
the closest-owner bibliography, made the sharpness and particle–hole proofs
explicit, repaired the alternating-state and Möbius endpoint explanations,
and expanded the deterministic control from 144,216 to **298,283 exact
assertions**. This audit is not external peer review.

## Reproduce

From this directory:

```bash
python3 code/verify_rule184.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
sha256sum -c SHA256SUMS
```

The control uses Python 3 and only the standard library. The final PDF is 5
A4 pages, 329,610 bytes, with SHA-256
`7db799503da50d23f747c1a6f7e1483e7a0316b36e52dd4d91cb9615ca55b964`.

## Ownership boundary

The traffic interpretation, conservation law, asymptotic phases, translating
core, Lucas hard-core counts, and Möbius inversion are not claimed. The
closest recent collision found in the bounded search is the 2025/2026 work of
Jha and coauthors on Rule-184 jam relaxation and height functions. Its
observable is close enough that the transient claim carries **medium–high
owner risk**, even though the inspected sources did not expose this exact
layerwise formula or the temporal particle/zeta ledger. The search was not
exhaustive and establishes no priority.

Evidence cutoff: 2026-08-28 UTC. No public posting, submission, or absolute
novelty/priority claim is authorized.
