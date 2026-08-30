# C241 source, provenance, and scope audit

## Frozen inputs

* Source/code baseline: `489506cf92bfed721f94f22dd0444a60427f90a5`.
* Route-A evaluator: `flow_systems/skills/route-a-evaluator.md`, version
  `0.2.0`, authority SHA256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
* Evaluation date: `2026-08-30`; build epoch:
  `SOURCE_DATE_EPOCH=1788048000`.
* Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Mathematical object

The object is the classical Lüroth map on \([0,1]\), with isolated endpoint
\(T_L(0)=0\) and half-open branches
\(I_m=(1/m,1/(m-1)]\), \(m\ge2\).  Each branch image is \((0,1]\), not
\([0,1]\): the excluded left endpoint tends to 0.  The inverse branch is
\(\phi_m(y)=(y+m-1)/[m(m-1)]\).  Finite compositions are strict affine
contractions, giving exact rational periodic points and integer multipliers.

## Evidence boundaries

The evidence receipt contains 11 branch rows, all 780 words over labels 2–6 of
lengths 1–4, 30 finite-cutoff necklace rows, 88 finite weighted rows, 3 limit
rows, and 2 formal primitive-product rows.  It is produced deterministically,
then checked by an independently written Fraction implementation and by exact
SymPy identities.  A clean byte replay compares a fresh producer output.  The
mutation suite includes repaired-digest cases, so semantic checks are exercised
after the outer hash is recomputed.

## Domain precision

\(A(s)=\sum_{m\ge2}[m(m-1)]^{-s}\) is absolutely convergent for
\(\Re(s)>1/2\).  The primitive product/log is absolutely convergent only in
the intersection \(\Re(s)>1/2\) and \(|z|A(\Re(s))<1\).  The formula
\(1/(1-zA(s))\) supplies a meromorphic continuation away from denominator
zeros throughout the half-plane, not an assertion of product convergence there.
At \(s=1\), \(A(1)=1\) by telescoping; the exact cutoff tail after \(m=M\) is
\(1/M\).  Rows at \(s=1/2\) explicitly mark full \(A(s)\) as divergent.

## Citation and negative-claim audit

The package cites Barrionuevo–Burton–Dajani–Kraaikamp (Acta Arithmetica 74(4),
311–327, 1996, DOI `10.4064/aa-74-4-311-327`) and Galambos (Czechoslovak
Mathematical Journal 22(2), 266–271, 1972, DOI `10.21136/CMJ.1972.101097`).
These sources motivate the Lüroth expansion conventions; the exact finite-word
ledger is our reproducible derivation, not a priority claim.  No target primes,
zeros, arithmetic local data, Euler factors, root numbers, automorphy, target
divisor/functional equation, Hilbert–Pólya operator, or Route-B input appears.
Accordingly the locked route tuple is
`[A0_FAIL, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FORMAL_HINT]`.
