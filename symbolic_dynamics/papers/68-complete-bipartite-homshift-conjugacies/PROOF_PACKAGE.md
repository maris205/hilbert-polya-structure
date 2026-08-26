# Formal proof package

## Theorem P68-A: product conjugacy classification

**Assumptions.** `d>=1`; all graph parts are nonempty.

**Statement.** `X_(m,n)^(d) ~= X_(r,s)^(d)` as `Z^d` systems iff `mn=rs`.

**Sufficiency engine.** Choose a bijection `f:A x B -> A' x B'`. An `A` symbol at `v` anchors `(v,v+e_1)`; a `B` symbol at `v` belongs to the anchor at `v-e_1`. Apply `f` once per dimer. Target-part membership is preserved, the rule commutes with all translations, and applying the same rule with `f^{-1}` returns every dimer.

**Necessity engine.** The single-global-phase formula gives connected-box counts with exponential rate `(mn)^(1/2)` per site; conjugacy preserves entropy. Disconnected pieces never choose their phases independently.

**Failure checks.** The anchor is detected from the symbol rather than absolute lattice parity. Both phases are covered. The inverse uses the same matching. No one-sided conclusion is drawn.

## Theorem P68-B: phase rigidity under finite dependence

**Statement.** Any finitely dependent law carried by `X_(m,n)^(d)` has deterministic phase. An `L`-invariant such law exists iff `L<=E`; none has full support on all `X`.

**Engine.** For an even `u` beyond the dependence range, `I_0=I_u` pointwise and independence gives `p=p^2`. An odd element of `L` exchanges deterministic phases. If `L<=E`, independent full-support colours on the fixed parity alphabets give a 0-dependent law.

## Theorem P68-C: pressure and equilibrium

**Statement.** For a one-site potential, `P=(log Z_A+log Z_B)/2`; the unique full-action equilibrium is the equal mixture of the two parity-wise Gibbs products.

**Engine.** The weighted single-phase restriction count gives the pressure. Full-action invariance fixes phase weights at `1/2`. A joint dimer entropy bound and the finite-alphabet Gibbs inequality give the sharp variational upper bound; equality forces independence both within dimers and across the even-subgroup full shift.

## Proposition P68-D: finite-index periodic data

If `L` contains an odd vector, fixed points are impossible. Otherwise `Z^d/L` has `q=[E:L]` cosets of each parity, giving `2(mn)^q` points.
