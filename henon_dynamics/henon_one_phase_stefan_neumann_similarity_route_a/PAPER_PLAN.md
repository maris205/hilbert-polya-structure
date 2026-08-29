# Paper plan

- State the normalized one-phase moving-boundary heat problem and its scaling.
- Insert the Neumann similarity profile and derive the Stefan root equation.
- Prove root existence/uniqueness and record the exact derivative.
- Invert the root at small Stefan number and bound it at large Stefan number
  with Lambert W, retaining the error mechanism from erfc.
- Derive wall/interface fluxes, their exact ratio, and the integrated energy
  identity (sensible plus latent terms).
- Separate zero superheat, zero diffusivity, and zero latent heat as singular
  rescalings; distinguish this source-native theorem from C207 Barenblatt and
  C202 KPP families.
- Report independent numerical, symbolic, replay, mutation, fixed-epoch PDF,
  and manifest audits. Explicitly state that the source heat clock is not
  target continuation/divisor/counting law and therefore A3_FAIL.
