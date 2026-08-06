# HCS-C02 frozen pilot protocol

## Question

For the certified local survivor of

\[
H_6(q,p)=(1-6q^2-p,q),
\]

does the true derivative action on raw slopes,

\[
\phi_q(m)=\frac{1}{-12q-m},
\]

produce a canonical complex fibre contraction and separated fibre domains?
The pilot must not replace the itinerary-dependent coefficient (q) by a
fitted constant Möbius generator.

## Frozen inputs

- `docs/related_programs/henon_weighted_zeta/R058_COVERING_PROOF.md`
  (`c73188a079df87c93812f1dd5d90e0110a68d8f91780fea22bd779d40f4f59fe`);
- `docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_SYMBOLIC_CONTRACTION_PROOF.md`
  (`b2d2c46c198e20b40b042cf5bc02cbdcfe9835c1a7c193cd88476eebc3e3f315`);
- `docs/related_programs/henon_weighted_zeta/paper/sections/B_contraction_proof.tex`
  (`0ef59712ee231aac3023d15d3ec857cbedfea884b18be7ec1ac30459757e28a8`),
  which contains the sharper same-sign-window prefactor $7/24$;
- the exact four-state adjacency matrix and raw h-set intervals appearing in
  those proofs;
- IEEE-754 double arithmetic only for the separately labelled closed-cycle
  sanity test.

No Riemann-zero, prime-target, or fitted spectral data are inputs.

## Prespecified tests

1. Convert the R058 normalized cone to a raw slope disk and check its exact
   pole clearance, strict self-inclusion, and Euclidean derivative bound.
2. Derive two child disks only from the exact (q)-intervals and the source
   disk. Check strict containment and separation.
3. Use the published contraction proof to tabulate central-cylinder
   uncertainty for memories $1,\ldots,8$, including the induced map and
   log-derivative bounds. The older R059 markdown uses a loose $5/4$
   continuity prefactor; do not substitute it for the published
   same-sign-window estimate $(7/24)(2/\sqrt{17})^m$.
4. Enumerate every primitive closed state word through period 8. Solve its
   R059 recurrence and check

   \[
   B_{n-1}\cdots B_0=J(DH_{n-1}\cdots DH_0)J,
   \quad
   B_i=\begin{pmatrix}0&1\\-1&-12q_i\end{pmatrix}.
   \]

5. Run an independent artifact checker that recomputes the rational disk
   constants and rejects any Schottky, complex-base, or Route-A A2 promotion.

## Gate semantics

- `PASS` is available for a two-disk separated holomorphic projective fibre
  cocycle over the **real** symbolic base.
- A complexified Hénon base, finitely generated Schottky system, nuclear
  operator, Fredholm determinant, or Hilbert--Pólya statement is outside this
  pilot and must remain `NOT_TESTABLE` or `NOT_ESTABLISHED`.
- A finite constant-generator replacement is a change of object, not a
  strictification of the true cocycle.

## Reproduction

From the repository root:

```bash
python next_paper_henon_candidate_search/code/c02_projective_pilot.py
python next_paper_henon_candidate_search/code/c02_projective_check.py
```
