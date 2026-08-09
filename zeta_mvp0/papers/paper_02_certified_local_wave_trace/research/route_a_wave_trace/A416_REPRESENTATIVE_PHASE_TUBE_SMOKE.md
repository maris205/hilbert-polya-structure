# A4.16 representative phase-anchor and branch-tube smoke

Date: 2026-08-09 (UTC)  
Protocol: `R401-VAL-L3-S0-COMPOSITE-DRAFT`  
Authority: **representative implementation evidence / non-licensing**

## Result

The exact representative matrix

\[
 \{\mathrm{S000},\mathrm{S025},\mathrm{S050}\}
 \times\{128,256\}\ \text{bits}
\]

passed two independently checked components and a separate composite
binding. The composite checker reports

```text
implementation_status = PASS_IMPLEMENTATION_SMOKE
component_scope = COMPOSITE_S0
composite_s0_passed = true
scientific_licensing_enabled = false
milestone_status = null
theorem_status = null
final_status = null
```

This is an implementation smoke, not an accepted A4.16 theorem.

## Static phase-anchor component

The static Arb/exact-dyadic component covers the constrained energy-one slow
tube in each of the six representative cells. It proves the outer-domain
gates, the positive fast-angle inequalities, and the positive-section landing
gate.

Its independently replayed archive contains:

- 6 proof objects;
- 84,172 nodes: 42,074 internal and 42,098 terminal;
- 0 unresolved nodes;
- 122,300 independent interval checks;
- maximum proof-tree depth 14.

The weakest representative enclosures satisfy

\[
 D_+>1.1262515601,
 \qquad
 N_+>1.1017163453,
\]

\[
 \omega_+N_+>10.4275826501,
 \qquad
 \dot\vartheta_+<17.9230948836<18.
\]

The component status is `PASS_STATIC_COMPONENT_SMOKE`, its scope is
`STATIC_ONLY`, and `composite_s0_passed` is false.

## Continuous branch-tube component

The CAPD component starts from the accepted L1 primary branch box in each
representative cell and encloses the complete normalized period with a
multiprecision `SolutionCurve` evaluated on 64 closed dyadic phase cells.
The independent checker reconstructs \(\omega_-\) with Arb and recomputes

\[
 r_-^2=(\omega_-Q_-)^2+P_-^2
\]

as an exact rational enclosure from every printed CAPD state box.

All 6 records pass. Across the complete representative matrix,

\[
 \max r_-^2
 =0.0001124580903773778485\ldots<0.04^2=0.0016,
\]

and the smallest squared margin is

\[
 0.0014875419096226221515\ldots>0.
\]

The component status is `PASS_NON_LICENSING_BRANCH_TUBE_SMOKE`; its
milestone, theorem, and final programme values are null.

## Composite replay

The composite packager and a no-import independent checker separately:

1. reconstruct the exact three-slab by two-precision matrix;
2. require the static and branch components to retain their distinct
   component-only statuses;
3. bind all six static proof hashes and all twelve branch raw/stderr hashes;
4. replay the exact 26-file branch provenance set, including the CAPD binary,
   C++ source, runner, checker, dependency record, L1 release chain, compile
   transcripts, report, and raw evaluator transcripts;
5. bind the derivation, protocol, experiment plan, packager, and checker;
6. reject duplicate keys, nonfinite numbers, symlinks, path escapes,
   overwrites, and Boolean/integer/float type aliases.

The canonical composite checker passes all 6 cells, verifies 18 manifest and
component-control bindings, and records an empty failure list.

## Analytic interpretation

For a representative parameter cell, the static inequalities support the
following conditional reduction. If a periodic candidate of period
\(T\in[0.64,0.69]\) remains in \(r_-<0.06\) for its complete period, then
the fast angle is strictly increasing and gains less than \(4\pi\). Its
integer winding is therefore one, so it has exactly one positive oriented
\(P_+=0\) crossing. The landing certificate places that crossing in the
A4.15 reduced root box. A4.15 then identifies the anchored root with the
accepted branch, hence the candidate geometric orbit with that branch modulo
time translation.

The separate CAPD calculation verifies that the distinguished branch itself
belongs to the stricter full-period tube (r_-<0.04) on the representative
matrix.

These statements remain representative because the other 48 slabs were not
run under this S0 protocol.

## Stable provenance

| Object | SHA-256 |
|---|---|
| Static summary | `e55c5280dcda615dcc672e58694a5639177fd0777595ff03eca163014c1bc225` |
| Static manifest | `f37b11967aab879e369080d3440d932c706bfe662734065077a51cfb1f5bb2ce` |
| Static independent checker | `4be68b9369714cba1979b03bcb08bc9dd40a4de8a02732b90fb87b39b422a262` |
| Branch summary | `a8853e4eb308cd44ad8413cbbd45da29240c113df15ea4ff3472bc740d3b089a` |
| Branch manifest | `edfa8a2a8e82e14e95828173da3b30c6a8820ef9950d5f31125bddc9c76231bc` |
| Branch independent checker | `162ebcc992054945deb48c84fa9b47bff970e9865cb629633049b986e3986753` |
| Composite summary | `ab0d7921623a5d4ba61d148ce833d22e14da75c77385897c328b20e41d64257f` |
| Composite manifest | `75c1533196c6c4df96bf21c09ecae3230423924323709652c259cbcd1d67cb05` |
| Composite independent checker | `197a087ecc75c95f186764f5365d3fc6769cb4cfe99793bfc1abc61afc037470` |
| Composite packager source | `0e37af44bda45db3903e46bf46815e29909b8e64db520e5000c913cf217c50a3` |
| Composite checker source | `3ffa8201a89ee07bba4a9e9d1e8042f856f404e07f310c1d35b8edcb15dcfbdb` |

## Non-promotion boundary

This smoke does not establish A4.16 on the other 48 slabs. It does not prove
that every energy-shell candidate remains in the local tube, so it is not a
global orbit-uniqueness theorem. It does not close the global return cover,
event-projected determinant, Taylor residual, \(\delta_{\rm tr}\), or
\(P_0\). It supplies no trace formula, prime-orbit theorem, Hilbert--Polya
operator, zeta-zero reconstruction, RH, or implication toward RH.

The next licensed engineering step is an independent pre-freeze review of a
prospective 51-slab by two-precision A4.16 production protocol. Global tube
routing remains a separate later bridge.
