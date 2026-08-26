# Paper 18 research protocol

Status: **PHASE-1 USER-CONFIRMED / BLOCKED BY PAPER 14**  
Version: `P18-P1-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Working title: **Haar Descent and the Same-Map Trace Dichotomy for Rational-Witt Packets**  
Route B, proof implementation, controls, Route A, manuscript, release, and
Git/public synchronization: false

Batch design lock:

```text
sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
```

## 1. Dependency and research question

Paper 18 starts only after Paper 14 fixes what is and is not known about the
source-global periodic locus.  For one rational prime, Deninger's coordinate
formulas describe the packet through auxiliary choices and an abstract
compact quotient

```text
U_p = product_{ell != p} Z_ell^x,
H_p = p^{Zhat},
B_p = U_p/H_p.
```

Papers 2 and 7 use normalized Haar only on a separately frozen abstract
compact-group/proxy record; Papers 9--10 show that the actual quotient
topology and its Borel algebra cannot provide that transverse information.
Paper 18 asks:

> Do all source-permitted packet coordinate changes preserve one canonical
> measurable/Haar class that descends to the exact packet owner, and if so
> can its disintegration, representation, and return trace be constructed on
> one named map?  If not, what is the complete descent obstruction?

The two branches are equally valid.  The protocol does not assume a positive
answer.

## 2. Owner registry

### 2.1 Actual source owner

```text
Gamma_p_actual subset X_susp,
Q_p_actual=Gamma_p_actual/R,
```

with the Paper-9 inherited indiscrete topologies and literal time action.
The topology-generated Borel algebra is the Paper-10 trivial algebra and is
not silently enlarged.

### 2.2 Abstract compact quotient owner

`B_p=U_p/H_p` has its compact Hausdorff quotient-group topology and normalized
Haar probability.  This owner is source-adjacent but not identified
topologically with `Q_p_actual`.

### 2.3 Coordinate presentations

The source formulas around the finite-kernel packet use choices including a
point above `(p)` and a compatible roots-of-unity identification.  Every
allowed presentation, its domain, codomain, and transition map must be
registered before any descent claim.

### 2.4 Prohibited substitutes

The selected Paper-7 product proxy, Paper-12 orbitwise standardization,
Paper-15 mixed standardization, copied tagged components, and an arbitrary
set bijection `Q_p -> B_p` are different owners.

## 3. Coordinate-transition gate

The first theorem package must:

1. enumerate the exact auxiliary choices in the source packet formulas;
2. prove that changing one choice induces a named transition on `B_p` and
   on the time coordinate;
3. prove composition and inverse laws for the full transition class;
4. decide whether every transition is a Haar-preserving affine/group
   automorphism, or exhibit a permitted non-Haar-preserving transition;
5. distinguish pointwise equality, equality of measure classes, and equality
   of normalized measures; and
6. state whether the result is fixed-prime only or compatible across primes.

No appeal to uniqueness of Haar is sufficient until the transition maps are
proved to lie in a class to which uniqueness applies.

## 4. Positive descent branch

Only if the transition gate is positive may the paper define a measured
packet owner.  The definition must specify:

- the sigma-algebra on the actual carrier or a separately named measured
  enhancement;
- the normalized transverse probability or measure class;
- choice independence and covariance;
- disintegration along time orbits;
- the action-groupoid Haar/source-fibre system used;
- the represented algebra and exact map into its von Neumann owner; and
- the trace/weight domain.

The same-map theorem must show how local orbit test operators restrict,
compress, or disintegrate from the packet representation.  Borrowing the
standard-circle character trace or the regular trace is prohibited without
that theorem.

## 5. Negative descent branch

If transitions do not preserve a unique measure, the paper must classify the
resulting parameter space or obstruction.  A complete negative theorem must
show:

- which choices change the transported measure;
- whether only measure class, total mass, or no nontrivial datum survives;
- how the obstruction relates to the free mass family in Paper 7; and
- why target coefficients cannot select a preferred point of the parameter
  space.

This branch closes the canonical packet-trace route for the declared class;
it is not evidence that every conceivable non-Hausdorff or stack-theoretic
measure theory is impossible.

## 6. Return-trace gate

On a positive branch, the project may ask for a distributional or semifinite
return trace only after the measured owner is complete.  The proof must keep
on one owner:

```text
test class,
convolution/representation,
domain,
disintegration,
normalization,
primitive and repeated coefficients,
clock and phase,
non-orbit terms.
```

Mandatory falsifiers are:

- singleton transverse base;
- arbitrary probability base;
- composite and arbitrary clock families;
- Paper-8 standard-circle regular/character split; and
- Paper-11 time-only convolution shadow.

If the result is unchanged under all these substitutions, it is not a
source-sensitive packet trace.

## 7. Candidate claim ledger

| ID | Candidate claim | Phase-1 status |
|---|---|---|
| P18-1 | Exact registry of source choices and coordinate presentations. | SOURCE AUDIT REQUIRED |
| P18-2 | Complete coordinate transition groupoid/class. | CENTRAL / UNPROVED |
| P18-3 | Haar descent or exact canonicality obstruction. | CENTRAL / UNPROVED |
| P18-4 | Positive measured enhancement and disintegration, if P18-3 passes positively. | CONDITIONAL |
| P18-5 | Same-map representation/trace transport, if P18-4 passes. | CONDITIONAL |
| P18-6 | Source-sensitive return formula or a fixed-class trace no-go. | CONDITIONAL |
| P18-7 | Cross-prime mass classification without target leakage. | BLOCKED BY P14 AND P18-3 |
| P18-8 | Deterministic transition/disintegration controls. | DESIGN UNAUTHORIZED |

## 8. Nonredundancy and standalone gate

The following are already owned and cannot be central claims:

- existence/uniqueness of normalized Haar on abstract compact `B_p`;
- actual topology-generated finite measures seeing only total mass;
- a selected product proxy with arbitrary component masses;
- local standard-circle Poisson or character traces;
- regular normal return blindness;
- the positive-time scalar closed-point ledger; and
- a generic `c0`-sum/corona diagonal.

Standalone eligibility requires either:

1. a source-audited, choice-independent measured packet owner plus a new
   same-map disintegration/trace theorem; or
2. a complete transition classification proving a sharp canonicality no-go
   not already contained in Paper 2's abstract free-mass observation.

If only abstract Haar survives, the project is merged or stopped.  Paper 18
does not consume the batch's Technical Note allowance by default.

## 9. Phase gates

Paper 14's final topology disposition is a prerequisite.  The exact source
formulas and manifestations must then pass independent source,
methodology/nonredundancy, and devil/domain audits.  A positive transition
gate needs a versioned amendment before any measured or trace proof.
Controls, Route, manuscript, and release remain separately blocked.  Route B
and Git/public synchronization remain false.
