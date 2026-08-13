# Novelty Audit: Additive Finite Arithmetic Capacity

**Candidate:** `additive_finite_arithmetic_capacity_v2`  
**Search cutoff:** 2026-08-14  
**Status:** independent proof and collision search completed before any Paper-5
candidate execution  
**Authoritative review:** `INDEPENDENT_PROOF_NOVELTY_REVIEW.md`, SHA-256
`4036f346b75e44ff1acc8402cc1b17f497f3510ee0f4aa6456288f9856fbb63b`

## Verdict

`PROCEED AFTER REPAIR`, with an overall novelty assessment of **5.5/10**.
The version-1 selector/union bound is correct but too close to a bookkeeping
corollary.  The independently reconstructed additive theorem is the strongest
defensible contribution:

$$
\log p=v+\log q+\alpha,
\quad
v\in V,
\quad
q>0\text{ algebraic},
\quad
q^2\text{ an }S_{\mathbb Q}\text{-unit},
\quad
\alpha\text{ real algebraic}
$$

implies

$$
\#\mathcal P_{\rm hit}
\le \dim_{\mathbb Q}V+|S_{\mathbb Q}|.
$$

The mathematical delta is the coupling: Hermite--Lindemann removes algebraic
additive contamination, and valuations remove multiplier contamination with
fixed finite support, forcing outside-prime L-parts to be rationally
independent.

## Claim-by-claim assessment

| Claim | Assessment | Safe interpretation |
|---|---:|---|
| Finite-rank locally constant capacity | 2/10 | Elementary linear algebra plus unique factorization. |
| Good-reduction Hénon prime-support certificate | 5/10 | A useful exact formulation built from standard integrality and unit arguments. |
| Algebraic action versus `log p` | 3/10 | Direct safe evaluation plus classical Hermite--Lindemann. |
| Additive mixed capacity theorem | 6/10 | Moderate synthesis novelty; the most defensible theorem-level delta. |
| Machine-auditable assumption/escape ledger | 6/10 | A reproducibility and design artifact, not a foundational theorem. |

## Collision-search conclusion

The independent reviewer searched web-indexed primary literature, publisher
records, arXiv, and open monographs across finite-rank suspension roofs,
arithmetic length spectra, Hénon good reduction and multipliers,
exact-symplectic actions, transcendence, and arithmetic prime-orbit programs.
No source found through the cutoff states the same three-source additive bound.
This negative search is evidence against an obvious collision, not a proof of
priority.

The closest verified contexts are:

- Parry--Pollicott for finite-state suspensions and periodic-orbit zeta
  functions;
- Ingram and Hsia--Kawaguchi for arithmetic Hénon dynamics;
- Cantat--Dujardin and Bianchi--He for current complex Hénon multiplier
  rigidity and thermodynamic geometry;
- Bialy--Tsodikovich for exact-symplectic action-sum formalism;
- Hermite--Lindemann for the transcendence step;
- Berry--Keating for prime logarithms as desired semiclassical periods; and
- Deninger, Connes, and Connes--Consani for positive infinite/adelic arithmetic
  architectures.

Full verified links and the query protocol are recorded in the authoritative
independent report.  The eventual manuscript must cite Deninger and
Connes--Consani prominently so that the scoped certificate cannot be mistaken
for a universal obstruction.

## Safe title and contribution statement

Use:

> **Finite Arithmetic Capacity under Additive Locally Constant,
> Good-Reduction Multiplier, and Algebraic-Action Readouts**

Safe contribution statement:

> We formulate a fixed additive readout class combining a finite-rank locally
> constant term, logarithms of positive algebraic moduli whose squares have
> fixed finite bad-prime support, and a real algebraic action term.  We prove
> that the number of exactly realized rational-prime logarithms is at most the
> rational rank plus the bad-prime count.  The result is a scoped architecture
> certificate, not a no-go theorem for smooth symplectic dynamics.

## Mandatory language constraints

Do not claim:

- a first theorem, historical priority, or novelty of the classical
  ingredients;
- a complete or exhaustive escape trichotomy;
- failure of all finite-dimensional or smooth symplectic dynamics;
- that prime clocks require infinite dimension;
- that an escaped certificate automatically yields arithmetic provenance; or
- any Riemann-zero, determinant, quantization, or Route-B conclusion.

## Repair closure

All ten mandatory items in Section B of the independent report are now
reflected in the version-2 research question, proof package, experiment plan,
tracker, and source lock.  Formal candidate execution remains closed until an
independent code review certifies that the implementation enforces the same
scope.
