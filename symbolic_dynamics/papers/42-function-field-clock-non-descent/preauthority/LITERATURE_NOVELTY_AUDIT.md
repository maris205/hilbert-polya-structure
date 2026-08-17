# Literature and novelty audit

Search cutoff: 2026-08-17 UTC.

## Proposed contribution

The proposed Paper-42 contribution is not the necklace formula, the
finite-field irreducible-polynomial count, the full-shift determinant, or the
rational Euler product. It is the exact source-contract statement that the
`SD-C01` finite-field degree clock and source-symbol marker cannot be retyped
factorwise as the rational-prime ledger while preserving totality,
multiplicity, and determinant ownership.

## Core claims and collision grades

| Claim | Literature status | Novelty |
|---|---|---|
| `N_q(n)` counts aperiodic necklaces and monic irreducibles | Explicit classical result, reiterated in current literature | none |
| full-shift zeta is a finite determinant / rational function | Foundational symbolic-dynamics prior art | none |
| rational zeta has one Euler factor per rational prime on `Re(s)>1` | Classical number theory | none |
| exact clock forces a length-`n` image label `q^n`, so `[01]` cannot map to a rational prime | Elementary consequence of the frozen contract; no exact published formulation located | low, bounded |
| marker plus weight force `n=1,p=q`, followed by a `q:1` multiplicity collision | Project-specific typed factor comparison; no exact published formulation located | low-to-moderate, bounded |
| strict Route rejection and selection chronology | Internal audit/governance result | none |

An unsuccessful search for the exact formulation is not proof of novelty.

## Verified source-to-claim matrix

| Source | Status | Claim supported | Boundary |
|---|---|---|---|
| M. Artin and B. Mazur, “On Periodic Points,” *Annals of Mathematics* 81 (1965), [DOI](https://doi.org/10.2307/1970384) | peer-reviewed foundational article | periodic-point zeta framework | does not identify full-shift primitive factors with rational primes |
| R. Bowen and O. E. Lanford III, “Zeta Functions of Restrictions of the Shift Transformation,” in *Global Analysis*, PSPUM 14 (1970), [DOI](https://doi.org/10.1090/pspum/014/9985), [official AMS volume](https://bookstore.ams.org/PSPUM/14) | primary proceedings article; existence and metadata verified by AMS | finite-shift determinant/Euler-product ownership | source determinant theorem, not Paper-42 novelty |
| S. K. Chebolu, J. Mináč, T. T. Nguyen, N. D. Tân, “Analytic Properties of Necklace Polynomials,” [arXiv:2605.11445](https://arxiv.org/abs/2605.11445) (2026) | recent preprint, not treated as peer reviewed | explicitly states that the necklace polynomial counts both aperiodic necklaces and monic irreducibles over finite fields | directly removes novelty from the source count; does not discuss the typed rational-prime clock projection |
| NIST DLMF §25.2(iv), Eq. 25.2.11, [permalink](https://dlmf.nist.gov/25.2.E11) | authoritative reference, version current in 2026 | `zeta(s)=prod_p(1-p^(-s))^(-1)` on `Re(s)>1` | target comparator only; not a source-owned operator |
| Session-4 Paper 1, `SD-C01` frozen derivation and proof | internal frozen source | owns `D_q`, `N_q(n)`, exact function-field ledger, and `O(R)` divisor-growth obstruction | Paper 42 may not reclaim these as new |

## Recent-window search

The 2024--2026 discovery pass used multiple formulations for each technical
claim, including:

```text
full shift finite field irreducible polynomials necklace dynamical zeta
function field zeta primitive necklaces symbolic dynamics
necklace polynomial irreducible polynomials finite fields primitive necklaces
rational primes full shift zeta symbolic dynamics
Riemann zeta primitive necklaces
function field rational prime dynamical zeta shift
prime zeta dynamical determinant symbolic
finite-field degree clock rational-prime factor map
q^n norm primitive orbit rational prime
marked dynamical zeta source-symbol marker prime Euler product
same-clock symbolic projection rational primes
full-shift primitive factor multiplicity rational Euler product
```

The search surfaced the 2026 necklace-polynomial preprint above, the 2026
preprint *Cyclotomic factors of rational necklace functions*
([arXiv:2606.02324](https://arxiv.org/abs/2606.02324)), and recent work on
necklaces in unrelated polynomial dynamics. These sources reinforce that
necklace enumeration is active and prior; none located by this bounded search
states the exact `SD-C01` clock/marker/multiplicity firewall.

No 2024--2026 source found in this pass provides a same-object map from every
full-`q` primitive necklace to a rational prime with exact clock
`n log q`. This is a search result, not a theorem of absence.

## Internal collision audit

| Internal source | Overlap | Firewall |
|---|---|---|
| Paper 1 / `SD-C01` | all positive full-shift formulas and the finite-memory global no-go | Paper 42 claims only the exact rational-prime projection/factor closure |
| Paper 14 / `SD-C16` | mixed primitive necklaces are not tensor atoms or rational primes | different tensor-bar grammar and determinant; methodological collision only |
| Paper 19 / `SD-C21` | a finite-field full-shift identity appears as a generic compiler control | no source-specific clock/marker descent theorem |
| Paper 24 / `SD-C26` | finite-alphabet prime-code/Kraft/Fredholm trilemma | Paper 42 does not quantify over arbitrary codes, code lengths, or compactness |
| Paper 27 / `SD-C29` | source-derived rational-prime atom compiler | different divisibility source and atom projection; cannot be imported into C01 |
| Paper 39 / `SD-C41` | terminal registry handoff | explicitly no ranking or authorization |
| final Paper-40 research seal / proposed `SD-C42` | Gauss/Mayer pair projection firewalls | different object, marker, operator, and primitive type |
| frozen Paper-41 preauthority / proposed `SD-C43` | exact rooted Knauf clock/sign non-descent | its source clock fails cyclicity/powers; C01's source clock succeeds and only rational-prime retyping fails |

## Source quality and verification limits

- The Bowen-Lanford metadata was verified against the official AMS volume.
- The 2026 necklace source is explicitly labeled a preprint; only its stated
  enumeration overlap is used.
- DLMF is used as an authoritative formula reference, not as novelty evidence.
- No source is called human-read beyond the portions actually inspected in
  this audit.
- No Crossref/Semantic Scholar/OpenAlex bulk verification or external
  cross-model review was available to this Phase-1 worker.
- Independent DA must repeat citation chaining from Bowen-Lanford and the
  2026 necklace papers, including conceptual synonyms such as closed points,
  prime polynomials, norm, degree, marked zeta, and orbit codes.

## Novelty assessment

- Source/function novelty: **0/10**.
- General mathematical difficulty: **low**; the proof is elementary.
- Exact typed `SD-C01` closure novelty: **3/10**, conditional on independent
  collision review.
- Broad mechanism novelty: **0/10**; no new Hilbert-Polya mechanism is
  proposed.
- Selector/chronology novelty: **0/10**.

Overall recommendation: `PROCEED_WITH_CAUTION_TO_INDEPENDENT_DA` only as a
program-closure theorem. Position the work as an ownership and factor-typing
certificate, not as a new connection between finite fields and rational
primes. If independent review finds the exact typed theorem already explicit,
return `STOP_DUPLICATE`.
