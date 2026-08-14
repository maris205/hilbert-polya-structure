# Source lock — Paper 32 / SD-C34

Lock date: 2026-08-15 UTC

## Frozen research authority

| Artifact | SHA-256 | Status |
|---|---|---|
| `/tmp/paper32_research_package.md` | `b34dd0489fae5080c683bedcaed6ddcc56025ddad6854da6e786c50c36fa61fb` | frozen mathematical, analytic, literature, control, and route authority |
| `/tmp/paper32_derivation_package.md` | `a4423a4f742d695be704f715e77c192d53b5b30a26d5e9db3629ad68467cfe32` | frozen derivation authority |
| `/tmp/paper32_proof_package.md` | `d50434c323af93df3fae848d730f27081a02d983d4f6ca36f680f6bd96a9633c` | frozen proof authority |
| `/tmp/paper32_residue_groupoid_prototype/residue_core.py` | `e7ad9ff5f515973d4a0d9a991be912961f2b7492dcac7ecf0006bf490c6179cf` | prime-blind research candidate core; not canonical repository code |
| `/tmp/paper32_residue_groupoid_prototype/run_prototype.py` | `cb6b128b9b3ace9cd39cf11ffe4ff02ac077d2bc923470bb61dd41580877616a` | independent evaluator/control runner; not canonical repository code |
| `/tmp/paper32_residue_groupoid_prototype/results_a/SHA256SUMS.txt` | `f7c2e0f1c1be4bdce325515feb83a80bebfaf36e5785c39b31bcb12d9481d5e6` | seven-file research payload ledger |

These files are immutable writer inputs.  Canonical experiment code, result
ledgers, evaluator certificates, and manifests are integrator-owned.  The
writer may synchronize final numbers after they are supplied, but may not
create, edit, freeze, or manifest the canonical experimental authority.

## Frozen research census

At research cutoff 192:

| Audit surface | Exact result |
|---|---:|
| moduli \(2,\ldots,192\) | 191 |
| independently labelled primes | 43 |
| prime-power composites | 14 |
| mixed composites | 134 |
| all composites | 148 |
| static field-defect equivalence | 191/191 |
| prime blocks with recurrent support | 43/43 |
| composite blocks with recurrent support | 148/148 |
| matched finite-semiring transports | 191/191 exact |
| seeded random \(C_2*C_3\) controls | 48/48 recurrent |
| canonical cusp diamonds | 31 |
| diamonds with composite top modulus | 31/31 |
| deterministic tests | 13/13 pass |
| isolated repeat runs | seven payload files byte-identical |

Finite computation checks the implementation and adversarial controls only.
The infinite state count, modular relations, diamond family, terminal-gate
equivalence, and trace-class claims have direct proofs.

## Canonical integration freeze

The integration layer subsequently rebuilt the candidate and evaluator under
the same frozen research authority.  These artifacts are read-only inputs to
the manuscript writer:

| Canonical artifact | SHA-256 | Certified role |
|---|---|---|
| `results/SHA256SUMS.txt` | `689a73a593f1791e6b2f49836b50cc2a11e5ddb1b91c46053af7aaa495ae4b8f` | canonical code/result ledger |
| `results/evaluation.json` | `0267d31af1f3a476528277b9154219340ac942d52872b305928d1c5d2311d66e` | independent 4,819,026-check evaluation |
| `results/double_run_certificate.json` | `b3dc8cb3c4cd16cdbbc0a04c4f2b3dddaac65c714c8ba9e92c986cb931829afd` | two fresh runs, 16 primary artifacts byte-identical |
| `results/integrity_audit.json` | `48d0d153dae72e2131e36c0fb2cdfe076dd007439e25c3357bd9eae39cc63df0` | final-tree status `PASS` |
| `EXPERIMENT_REPORT.md` | `acafeb77e0c8a8272ae92dab7fdacc26fde11d73050506eda35423095ce06ce6` | canonical experiment narrative after EOF hygiene |
| `evaluations/route_a/SD-C34/2026-08-15.yaml` | `304a0084773c0896d29acbb19c0101fb2273bbe16519c9ae8363e3e6aba51530` | strict Route-A v0.2 evaluation record |

The independent evaluator imports no candidate module and passes
4,819,026/4,819,026 checks with zero failures.  These include 2,377,759 full
addition-table entries, 2,377,759 full multiplication-table entries, and
56,318 projective edges.  All 13 deterministic assertions pass.  The two-run
certificate covers 16 primary artifacts per run and has aggregate SHA-256
`3cc4d3bddb5e771c5b2621110e9499b169359438d88608c36f8dc615ce73c727`.
The canonical freeze changes no theorem, census, tuple, or branch decision.

## Frozen source and information boundary

The source retains the finite-full-shift semiring
\[
 F_n=(A_n^{\mathbb Z},\sigma_n),\qquad
 F_m\boxplus F_n\cong F_{m+n},\qquad
 F_m\boxtimes F_n\cong F_{mn},
\]
with zero, unit, successor, source equality, quotient/remainder, congruence,
and entropy \(h(F_n)=\log n\).  Source congruence reconstructs the residue
ring \(\mathcal R_n=\mathbb Z/n\mathbb Z\); additive inverse, units,
unimodular pairs, and projective classes are defined by source equations.

Allowed inputs are those source operations and relations, the fixed matrices
\(S,R\), constants 2 and 3 generated from the unit, the cusp \([1:0]\), roofs
frozen before evaluation, exact arithmetic, deterministic cutoffs and seeds,
matched relabels, and evaluator-only arithmetic classification after the
candidate census.

Forbidden inputs are supplied prime, prime-power, factor, accepted-support,
orbit-projector, von Mangoldt, or target-zero tables; candidate-side
primality/factorization calls; a terminal accept/reject edge; using the static
field defect to determine which recurrent blocks exist; Riemann-zero
ordinates; coefficient fitting; root matching; post-control changes to graph,
roofs, signs, markers, or states; induction/first return that changes object or
clock; and Route B.

## Frozen candidate

For \(n\ge2\), set
\[
 X_n=P^1(\mathcal R_n)
 =\{(a,b):\mathcal R_na+\mathcal R_nb=\mathcal R_n\}/\mathcal R_n^\times.
\]
The two mandatory outgoing transitions at every state are
\[
 S_n[a:b]=[-b:a],\qquad R_n[a:b]=[-b:a+b].
\]
No transition or recurrent-component closure consults a field flag,
factorization, or terminal Boolean.  With \(c_n=[1:0]_n\), add both directed
edges \(c_n\rightleftarrows c_{2n}\) and
\(c_n\rightleftarrows c_{3n}\).

Within-modulus edges have roof \(\log n\).  Either direction of a cross edge
between \(n\) and \(kn\), \(k\in\{2,3\}\), has roof \(\log(kn)\).  The free
marker \(z\) counts one edge of this exact uninduced graph.

On \(\mathcal H=\bigoplus_{n\ge2}\ell^2(X_n)\), define
\[
 B_s=\bigoplus_{n\ge2}n^{-s}(P_{S,n}+P_{R,n})
 +\sum_{n\ge2}\sum_{k\in\{2,3\}}(kn)^{-s}
 (J^+_{k,n}+J^-_{k,n}),
\]
where \(J^+_{k,n}=|c_{kn}\rangle\langle c_n|\) and
\(J^-_{k,n}=(J^+_{k,n})^*\).

## Frozen theorem and analytic boundary

The projective-line count is
\[
 |X_n|=\psi(n)=n\prod_{p\mid n}(1+p^{-1}),
\]
and \(\psi(n)=n+1\) exactly when \(n\) is prime.  This is a static field
criterion.  The projector
\(\bigoplus_n\mathbf1_{\{|X_n|=n+1\}}I_{\ell^2(X_n)}\) is therefore precisely
a completed primality gate and is forbidden.

Direct multiplication gives \(S^2=-I\) and \(R^3=-I\).  Scalar \(-I\) is
projectively trivial, so \(S_n^2=R_n^3=I\) on every \(X_n\).  Every state of
every prime, prime power, and mixed composite block lies in both
marker-distinct recurrent families.  Bidirectional cusp edges add, for every
\(n\ge2\), the simple primitive nonbacktracking cycle
\[
 c_n\to c_{2n}\to c_{6n}\to c_{3n}\to c_n,
\]
whose roof weight is \((216n^4)^{-s}\).  Downward-only residue maps strictly
decrease the modulus and therefore contribute no periodic orbit.

For \(\sigma=\operatorname{Re}s>2\),
\[
 \left\|\bigoplus_{n\ge2}n^{-s}(P_{S,n}+P_{R,n})\right\|_1
 \le2\sum_{n\ge2}\psi(n)n^{-\sigma}
 \le2\zeta(\sigma)\zeta(\sigma-1),
\]
while the cross terms satisfy
\[
 \|C_s\|_1\le
 2(2^{-\sigma}+3^{-\sigma})\sum_{n\ge2}n^{-\sigma}.
\]
Both series converge locally uniformly in trace norm.  Thus the same
uninduced object owns the ordinary Fredholm determinant
\(D_{\mathrm{PR}}(s,z)=\det(I-zB_s)\), entire in \(z\) and holomorphic in
\(s\) on \(\operatorname{Re}s>2\).  This honest A2 ownership does not repair
the failed primitive ledger.

## Frozen route and branch decision

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

- Overall: `ROUTE_A_REJECTED`.
- Route B: `LOCKED`.
- Positive prime-selective candidate: `STOP`.
- Negative obstruction paper: `GO`.
- Branch action: `CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH`.

Paper 33 may continue only through a cycle-level, source-natural quotient or
twist of this same recurrent object.  It must annihilate the universal
\(S^2\), \(R^3\), and cusp-diamond cycles before arithmetic labels or roofs,
then prove the complete surviving primitive ledger and same-object
determinant ownership.  A static field projector, surviving universal cycles,
or equal cancellation on random actions closes the entire semiring-residue
family.

## Writer authority

The writer may create or edit only the narrative, proof, derivation,
literature, planning, round-two, figure, LaTeX, bibliography, PDF,
compilation-audit, README, source-lock, and preregistration files listed in
`README.md`.  The writer may not modify code, experiment plans, results,
evaluations, manifests, repository-level documentation, mirrors, or Git state.
