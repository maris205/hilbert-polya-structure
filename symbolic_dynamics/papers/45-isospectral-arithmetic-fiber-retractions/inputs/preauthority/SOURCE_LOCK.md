# Source lock

## Candidate identity and chronology

- Provisional identity: P45-ALLH-RETRACTIONS-PREAUTHORITY
- Family: arithmetic weighted retractions on \(\ell^2(\mathbb N)\)
- Stage: result-free preauthority theory/source candidate
- Source cutoff: 2026-08-18 UTC
- Accepted authority-tree commit used by Phase 2:
  6e5658649d2eab0fce077cbcdcc00070dd54095f
- Portable package identity: paper45_preauthority_candidate
- Authorized authority, mirror, registry, and Git writes: none

The final unique Phase-2 parent/source manifest SHA256SUMS.txt in the
external Phase-2 packet has SHA-256
d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181.
It supersedes every earlier Phase-2 manifest candidate and was verified
entry by entry against the current Phase-2 directory.

## Frozen arithmetic objects

Let \(h\ge2\) and let

\[
\mathcal F_h=\{m\ge1:v_p(m)<h\text{ for every prime }p\}.
\]

Define two idempotent retractions of \(\mathbb N\) onto \(\mathcal F_h\):

\[
\tau_h(n)=\prod_p p^{\min(v_p(n),h-1)},\qquad
\omega_h(n)=\prod_p p^{v_p(n)\bmod h}.
\]

Both satisfy

\[
\tau_h(m)=\omega_h(m)=m\quad(m\in\mathcal F_h).
\]

The standard basis of \(\ell^2(\mathbb N)\) is \((e_n)_{n\ge1}\). For
\(s\in\mathbb C\), \(\sigma=\Re s\), define on \(c_{00}(\mathbb N)\)

\[
S_{h,s}e_n=n^{-s/2}e_{\tau_h(n)},\qquad
M_{h,s}e_n=n^{-s/2}e_{\omega_h(n)}.
\]

No bounded operator is presumed until the fiber square masses have been
checked. The exact extension domains are:

\[
S_{h,s}\in\mathcal B(\ell^2)\iff\sigma>0,
\qquad
M_{h,s}\in\mathcal B(\ell^2)\iff\sigma>1/h.
\]

On those domains the respective operators are compact.

## Frozen fiber and block convention

For \(m\in\mathcal F_h\), set

\[
J_h(m)=\{p:v_p(m)=h-1\}.
\]

The two fibers and squared block singular norms are locked as

\[
\tau_h^{-1}(m)
=\left\{m\prod_{p\in J_h(m)}p^{r_p}:r_p\in\mathbb Z_{\ge0}\right\},
\]

\[
\omega_h^{-1}(m)=\{ma^h:a\in\mathbb N\},
\]

\[
\rho_S(m)^2
=m^{-\sigma}\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1},
\qquad
\rho_M(m)^2=m^{-\sigma}\zeta(h\sigma).
\]

The direct-sum blocks are indexed by the target \(m\), not by a prime,
primitive orbit, or fitted spectral datum.

## Frozen marker and spectral conventions

- \(s\) is the Dirichlet weight parameter; \(\sigma=\Re s\) controls
  singular norms.
- \(m\in\mathcal F_h\) is a block/eigenvalue label.
- \(z\) is reserved for the Fredholm or regularized determinant variable.
- \(\lambda_m=m^{-s/2}\) is a nonzero operator eigenvalue.
- A finite-output \(\lambda_m\) is serialized as the canonical symbolic
  `DIRICHLET_POWER` envelope. The positive base and every exponent
  numerator/denominator are canonical integer strings: no JSON numeric,
  Boolean, plus sign, leading zero, or `-0` is legal, and denominators are
  positive. The reduced exponent is \(-s/2\), with
  `REAL_LOG_POSITIVE_BASE`. The raw object is canonicalized to RFC8785 JCS;
  the exact JCS UTF-8 string and lowercase SHA-256 are stored and
  recomputed. It is never a rational `complexExact` value.
- Duplicate JSON members are detected at every nesting depth in the token
  stream and rejected before object construction; last-win parsing is
  forbidden. Reordered unique members are accepted and canonicalize to the
  same JCS bytes/hash.
- \(\rho_T(m)\) is the unique nonzero singular value of block \(m\).
- \(P_T(m)\) is the norm of the Riesz idempotent for \(\lambda_m\).
- No one of these types may be reidentified with a rational-prime primitive
  atom.

For every positive integer \(k\),

\[
T_m^k=m^{-(k-1)s/2}T_m.
\]

The common trace is owned only on the common bounded and trace-class domain:

\[
\sigma>1/h,\qquad k\sigma>2.
\]

For an integer regularization order \(r\ge1\), a common
\(\det_r(I-zT)\) comparison is owned only when

\[
\sigma>1/h,\qquad r\sigma>2.
\]

## Frozen Tauberian convention

For the saturated singular values define

\[
w_{h,\sigma}(m)
=m\prod_{p\in J_h(m)}(1-p^{-\sigma})^{1/\sigma}.
\]

Its positive generalized Dirichlet series is

\[
F_{h,\sigma}(z)=\sum_{m\in\mathcal F_h}w_{h,\sigma}(m)^{-z}
=\zeta(z)G_{h,\sigma}(z),
\]

where

\[
G_{h,\sigma}(z)=\prod_p(1-p^{-z})L_p(z),
\]

\[
L_p(z)=\sum_{e=0}^{h-2}p^{-ez}
+p^{-(h-1)z}(1-p^{-\sigma})^{-z/\sigma}.
\]

The proof must establish local uniform convergence and holomorphy in

\[
\Re z>\theta_{h,\sigma}
=\max\left(\frac1h,\frac{1-\sigma}{h-1}\right)<1,
\]

the simple pole at one, its positive residue, and the monotonicity needed
for Wiener--Ikehara. A finite fit is not admissible evidence.

## Frozen source packet

The mathematical source of truth is the following verified Phase-2 packet:

| Artifact | SHA-256 | Role |
|---|---|---|
| REPLACEMENT_B_THEOREM_AUDIT.md | 12187d0bdb8671e5daf4893aac995b6e33ff87355df4d84778680306b17fbc5a | corrected all-\(h\) theorem |
| P45_INDEPENDENT_AUDIT_ATTESTATION.md | 796e57c14551710264a4dc0c57e922a6856519c5124ad695b91a44f8f99264a5 | independent hostile-audit binding |
| p45_retraction_hostile_audit.md | 926aad2a27ef88fdb82e8cdca487d34c75d44141c9827d9863bf5a3eae8e1326 | independent derivation report |
| SOURCE_VERIFICATION_REPORT.md | 7c37724a63c01d3ba011242142db5553de60c34ef7c15512a6f59d8028927f88 | primary-source verification |
| SEARCH_STRATEGY_AND_ANNOTATED_BIBLIOGRAPHY.md | 28811ffe2ed17125bb9cd742249d73aa9157e4c52eafaff94f8ed670c4c397af | query and bibliography record |
| CLAIM_COLLISION_MATRIX.md | 17aedd8e4419ed2b60d74b66ef122771aafe7d0c993be6a45a13443720eba17b | admissible/forbidden claims |
| FINAL_SEQUENCE_GATE.md | a1fab88bf3dfdb8e8aa7abb521208c66a7c7e2a2bf64dd6137266f8f565035ad | numbering and no-authority gate |

The P43 preauthority package manifest, used only as a structural template,
has SHA-256
f35b469d6a438d9a9e1f03e0682d85590b1010dd2acfe82b4f2ceef677d68d8f.
It supplies no P45 theorem evidence.

## External ownership lock

The following components are already externally owned and receive zero
novelty credit:

- Luan and Khoi, Weighted composition operators on weighted sequence
  spaces, Contemporary Mathematics 645 (2015), 199--215,
  DOI 10.1090/conm/645/12907: generic weighted-composition boundedness and
  compactness framework;
- A. V. Abanin and R. S. Mannanikov, Weighted Composition Operators on
  Quasi-Banach Weighted Sequence Spaces, Vladikavkaz Mathematical Journal
  25 (2023), no. 4, 5--19, DOI 10.46698/x5057-2500-3053-t: generic quasi-Banach
  weighted-composition boundedness and compactness context;
- Carlson, The spectra and commutants of some weighted composition
  operators, Transactions of the AMS 317 (1990), 631--654,
  DOI 10.1090/S0002-9947-1990-0979958-6: generic discrete
  weighted-composition spectrum and commutant context;
- de Weger and van de Woestijne, On the power-free parts of consecutive
  integers, Acta Arithmetica 90 (1999), 387--395,
  DOI 10.4064/aa-90-4-387-395: power-free-part terminology and arithmetic
  context;
- classical Euler products, \(h\)-free counting, prime number theorem,
  Mertens product theorem, Wiener--Ikehara, compact-operator theory,
  Schatten ideals, and regularized determinants.

The current operator is the adjoint-side realization of a discrete weighted
composition operator. Reversing this convention does not create novelty.

## Internal ownership lock

- Paper 27 owns cyclic-invariant blindness to oblique geometry, generic
  oblique projections, and its separate similarity wall.
- Paper 28 owns the project-level adjoint/Gram/Schatten route.
- Paper 29 owns the counterterm and regularized-determinant mechanism.
- Paper 30 owns the free-monoid/free-UFD indistinguishability firewall.
- Paper 43 owns its separate \(h\)-free inventory and typed integration
  pattern, not the present operator theorem.

The P45 package may cite these predecessors but may not call itself a
completion of an open P27 or P28 obligation.

## Allowed evidence

- exact prime-exponent factorization and positive Euler products;
- standard compact-operator, Riesz-projection, and Schatten theory;
- PNT/Mertens and a correctly hypothesized positive Tauberian theorem;
- two independently implemented evaluators that share only the frozen raw
  contract and final canonical projection;
- exact symbolic and rational checks on finite blocks;
- a free formal-UFD clone only as a negative control;
- the verified primary and internal source packet above.

## Forbidden evidence and moves

- any finite truncation presented as proof of an infinite endpoint;
- analytic continuation inferred from numerical coefficient agreement;
- a trace or determinant outside its ideal domain;
- suppressing the \(\sigma>1/h\) existence wall for a power of \(M_{h,s}\);
- claiming \(C_{h,\sigma}\ne D_{h,\sigma}\) for every \(\sigma\);
- using the \(h\ge3\) exponent-one commutator witness at \(h=2\);
- evaluator code, fixtures, expected tables, or serialized intermediates
  shared across the two independent implementations;
- a free-UFD reproduction counted as rational-prime selectivity;
- a generic source or predecessor method counted toward paper size;
- Riemann-zero fitting, target-driven parameter choice, or post hoc
  endpoint changes;
- authority, mirror, registry, root-manifest, or Git mutation.

## Exact claim boundary

The strongest authorized preauthority statement is:

> The all-\(h\) saturated/modulo pair has a common legal cyclic ledger but
> the exact distinct bounded domains, similarity domains, maximal Riesz
> order, singular Weyl laws with equality at \(\sigma=1\), and
> self-commutator ideal laws proved in PROOF_PACKAGE.md.

No broader weighted-composition theorem, rational-prime emergence claim, or
authority decision is included.
