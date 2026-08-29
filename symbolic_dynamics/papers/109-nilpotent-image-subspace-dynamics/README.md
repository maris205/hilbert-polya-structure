# P109 — Nilpotent image dynamics on finite subspace lattices

Status: **FINAL MECHANICAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

Let `V = F_q^d`, let `N` be one regular nilpotent Jordan block, and let
`L(V)` be the full lattice of linear subspaces.  This note studies the finite
map

```text
T(U) = N(U).
```

It is not the saturation map `U -> U + N(U)`, and it does not restrict the
phase space to `N`-invariant subspaces.

The internal collision firewall also separates it from P73's symbolic
Jordan-block substitution discrepancy, P99's bijective unipotent shear on
fixed-index integer sublattices, and P103's adjugate map on full matrix
space.  None shares this phase space, update rule, or transient fibre census.

The frozen theorem package is:

1. `T^t(U)=N^t(U)` and every `t`-step fibre is explicit: for an
   `s`-subspace `W <= im(N^t)`,

   ```text
   #{U in Gr(r,V): N^t(U)=W}
      = [t choose r-s]_q q^(s(t-r+s));
   ```

2. multiplying by `[d-t choose s]_q` gives every joint transition count for
   `(dim U, dim N^t U)`, while summing over `r` gives every iterated indegree;
3. with `G_j(q)=sum_a [j choose a]_q`, the absorption CDF and exact layers are

   ```text
   #{depth <= t}=G_min(t,d)(q),
   #{depth = t}=G_t(q)-G_{t-1}(q)  (1 <= t <= d);
   ```

4. zero is the unique periodic point, the maximum depth is exactly `d`, and
   the Artin–Mazur zeta function is `(1-z)^(-1)`; and
5. the depth census recovers `(q,d)` for `d>=2`, whereas every `d=1` field
   gives the same two-state system.  This exception is explicit and necessary.

Two independent proofs of the transition formula are retained in the paper:
quotient-fibre geometry and a hyperplane recurrence.  The exact control uses
literal RREF subspaces and Jordan shifts over prime fields and explicit
polynomial-basis models of `F_4`, `F_8`, `F_9`, and `F_16`.

Run the control from this directory with:

```bash
python3 code/verify.py
```

The expected final line is:

```text
PASS: 515,379 exact assertions
```

The canonical entry point delegates to the documented implementation
`code/verify_nilpotent_image.py`.  The complete deterministic output is stored in
[`code/verification_output.txt`](code/verification_output.txt).  Claim-to-proof
and claim-to-control mappings are in [`CLAIMS_EVIDENCE.md`](CLAIMS_EVIDENCE.md),
and [`CONTROL_RESULTS.md`](CONTROL_RESULTS.md) explains the lanes.  The PDF
recipe is in [`BUILD.md`](BUILD.md); author proof triage is recorded in
[`AUTHOR_SELF_CHECK.md`](AUTHOR_SELF_CHECK.md), and the two independent
team-internal audits are recorded in [`HOSTILE_REVIEW_A.md`](HOSTILE_REVIEW_A.md)
and [`HOSTILE_REVIEW_B.md`](HOSTILE_REVIEW_B.md), with their consolidated
decision in [`HOSTILE_REVIEW.md`](HOSTILE_REVIEW.md).  These are not external
referee reports.  The final mechanical freeze is recorded in
[`FINAL_QA.md`](FINAL_QA.md), and `SHA256SUMS` authenticates the frozen
source/evidence/PDF package.

Gaussian subspace/intersection counts and invariant-subspace lattices are
classical and explicitly subtracted.  The dimension-sequence/profile work of
Bender–Coley–Robbins–Rumsey (DOI
`10.1016/0097-3165(92)90093-A`) and Ram's 2026 general subspace-profile
formula (DOI `10.1017/fms.2026.10193`) are the closest identified owners and
are also subtracted.  The residual pointed-fibre/functional-graph package has
passed only a bounded owner search.  No global novelty, priority, public
release, submission, or author-contact claim is authorized; external status
remains **HOLD**.
