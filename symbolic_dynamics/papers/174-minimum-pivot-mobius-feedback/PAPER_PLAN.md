# P174 paper plan

**Working title:** *Minimum-Pivot Möbius Feedback on Projective-Line
Subsets*  
**Venue form:** anonymous AMS short note  
**Round:** final Round 2; dual hostile reviews closed  
**Lifecycle:** `PROVISIONAL_AMBER / HOLD_EXTERNAL`  
**Target length:** 4--6 A4 pages including references

## One-sentence contribution

Minimum-pivot translation followed by inversion on fixed-size subsets of
`P^1(F_p)` produces a sharp depth-two graph whose recurrent core is inversion
and whose complete target inverse is a nonuniform initial interval of pivots.

## Claims--evidence matrix

| Claim | Analytic evidence | Independent evidence | Placement |
|---|---|---|---|
| `im M=Z`, `im M^2=Y`, recurrent set `Y` | pivot and infinity images; inversion on `Y` | complete edge graphs in 69 boxes | Theorem 1(i), Section 2 |
| `M^4=M^2` and exact depth layers | image tower plus involution core | pointwise iterate/tail checks | Theorem 1(ii), Section 2 |
| fixed coefficient and exact 2-cycle count | inversion-orbit decomposition of `F_p^*` | exact cycles in every box | Theorem 1(iii), Section 2 |
| every-target fibre and pivot polynomial | forced inverse plus modular no-wrap criterion | every target and every pivot | Theorem 1(iv), Section 3 |
| fibre distribution and maximum | classify the largest inverse label | complete histograms and mass identity | Corollary 3, Section 3 |
| `(p,k)=(2,2)` boundary | direct three-state calculation | explicit boundary assertions | Section 4 |

## Structure

### Abstract

- Define the literal state-dependent map without citations.
- State the depth-two tower, `M^4=M^2`, fixed/2-cycle atlas, and marked fibre.
- Give the exact verification scale.
- End with the amber/external-hold boundary.

### 1. The map and its claim ceiling

- Define `P^1(F_p)`, the coordinate order, carrier, pivot, and projectivity.
- State the main theorem in one consolidated package.
- Separate the result from fixed Möbius dynamics and `PGL` subset-orbit
  background.
- State P96, P168, and AQN internal subtractions explicitly.
- Say that a bounded direct-owner non-hit has no novelty force.

### 2. The two-stage image tower

- Prove `im M=Z` and `im M^2=Y` in both directions.
- Derive recurrence, inversion core, `M^4=M^2`, and all depth counts.
- Count inversion-invariant recurrent subsets and two-cycles.
- Record fixed-iterate counts as a consequence, without claiming the
  classical involution calculation independently.

### 3. Every-target inverse

- Invert the projectivity for a proposed pivot.
- Prove the modular wraparound lemma.
- Derive the full pivot polynomial including zero fibres.
- Count targets of each positive fibre size and obtain the maximum.
- Explain why this axis is target-local and not supplied by the aggregate
  functional graph.

### 4. Exact controls and limitations

- Display representative exact rows and the complete `p=2,k=2` graph.
- Describe the independent verifier and distinguish checks from proof.
- Reiterate the artificial order, shallow clock, and owner uncertainty.
- Make `PROVISIONAL_AMBER / HOLD_EXTERNAL` visible.

## Figure and table plan

No figure is needed: the two nested image sets are one line of notation, and
a decorative diagram would add no information.  One compact table will show
representative state, image, recurrent, fixed, depth, and maximum-fibre
counts.  Its caption will state that the rows are checks, not theorem
evidence.

## Citation plan

- El Abdalaoui--Shparlinski: trajectories of a fixed Möbius transformation
  over `F_p`; zero-credit fixed-map background.
- Tricot: published `PGL(2,q)` action on `k`-subsets of the projective line;
  zero-credit subset-orbit background.
- Aluffi--Faber: projective-configuration orbit setting; zero-credit orbit
  language.
- Grinberg--Mao: simultaneous group multiplication and cyclic rotation on
  words; cited only to make the AQN quotient warning concrete.
- Jefferson--Jonauskyte--Pfeiffer--Waldecker: ordered minimal/canonical
  images and canonizing elements; zero-credit group-action machinery that
  does not transfer to the orbit-nonconstant feedback or pivot interval.

All five records are checked on primary DOI/arXiv/repository surfaces.  No citation is
inferred from memory, and only cited records enter `references.bib`.

## Round boundary

Review A returned `0/0/0`.  Review B returned `0 Critical / 0 Major / 1
Minor`; its canonical-image source subtraction is implemented and delta-
accepted.  No external release follows from the clean dual-review freeze.
