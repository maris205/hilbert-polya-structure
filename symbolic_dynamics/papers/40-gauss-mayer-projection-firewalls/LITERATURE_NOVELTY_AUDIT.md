# Paper 40 independent literature and novelty audit — replacement seal

Audit date: 2026-08-17 UTC
Candidate: `SD-C42`
Status: `INDEPENDENT_POST_RUN_SOURCE_ONLY_AUDIT`
Decision: `PROCEED_WITH_CAUTION_AS_SCOPED_CLOSURE_ONLY`
Overall novelty score: `4/10`

## 1. Exact binding and chronology

This audit binds only the following corrected bytes:

| Role | SHA-256 |
|---|---|
| Acyclic 22-entry claim-boundary seal | `168c29620445002fdf0bdf9c49bd7792414fe5ef378c80615b115646db9214cb` |
| Scientific source lock | `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041` |
| Mayer source/domain boundary | `a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5` |
| Six-card selection audit | `0739263b6da1795bfa693ba2600e92a87fd973d9af08398d505a8fa4afa3190c` |
| Literature/claim addendum | `fb2cdae0e4b1aa662a3426d7d569a926d94b5bf7b2b36b5de0e8bc77f6ffb9fb` |
| Derivation | `7f1f80637b8dbadf95461245419529180243faec08637e306b79da76389229ea` |
| Proof | `9ae5b6220ba1fde93b4592e6ec1b1dd78289248f376b7ef395b96dc815e9aa8e` |
| Object ownership | `7cda0257d99547b8dd28f8c7e5fc0c315e34fcb0e2724f10d75a40dfd3553e7f` |
| Primitivity firewall | `5280a3ef22fcfef0078ed4e162246aa6cc516135aece0a53f78ce8fad2ca18a8` |
| Route status / YAML | `4fb51559b79420f5515698b0f3b069d94c46736c9ef8e4f999041f2ed81a3c07` / `057e2040ed93ab8cf532683bf84782997a3579d195b38b060b16b55460a3922b` |
| Control / independent control | `d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f` / `729287849f36046b8aa21d8dba615650f4289dd1d3202c1783cc41af207c4d92` |
| Prototype / independent prototype | `2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995` / `78a1846b19cffde3c21642e6220b893a82690adaee5314ff6be2b19e7265fe38` |

The seal is acyclic: it excludes this audit. A later outer research manifest
may bind both without creating a hash cycle.

The chronology is retrospective and fully conceded. Provisional v1 results
and multiple in-flight corrective smoke outputs were known while M1--M20 were
changing the contract and evaluators. Only the exact fifteen corrected inputs,
seeds, grids, and fixtures enumerated by `CONTROL_LOCK.md` were frozen before
one canonical empty-results replacement rerun. Proof, Route, literature,
report, summary, and manifest bytes are post-run renderings. M21--M25 are
post-run proof/schema corrections. No part of that corrective sequence earns
prospective, priority, or novelty credit.

## 2. Executive verdict

The corrected package is supportable as a narrow theorem-grade closure of a
pre-existing `SD-C04` audit request. It is not supportable as a new
Gauss--Mayer mechanism, a new Selberg or two-variable determinant, the first
observation of trace/length multiplicity, a first or minimal collision
witness, a universal no-selector theorem, or a Paper-39-selected direction.

The defensible contribution is:

> For the exact retrospectively corrected two-digit/even-iterate Gauss--Mayer
> pair-return contract, the three frozen scalar projections---trace,
> trace/order discriminant of `Z[M]`, and geodesic norm---each fail at least
> one conjunct of the full rational-prime reciprocal-Euler-ledger target,
> while the intrinsic pair ledger and its same-object Mayer Fredholm
> determinant retain narrow positive ownership credit.

That statement is valid only with the package's full typing, marker,
multiplicity, branch-order, amplitude, domain, chronology, and operator-scope
qualifications. The research value is the exact falsification architecture and
all-orders closure, not a new analytic mechanism or qualitative discovery.

## 3. Internal priority and independent selection

The strongest priority collision is internal. Paper 1 and its historical
`SD-C04` artifacts already record:

- the Gauss/Mayer candidate and `det(I-L_s^2)`;
- the qualitative failure of trace, discriminant, norm, and parity to create
  a canonical rational-prime ledger;
- 7,018 non-reversal trace-collision groups in the historical finite census;
- the next exact trace/composite-discriminant audit request.

Paper 40 may therefore claim only exact theorem-grade completion of that
request. It may not claim discovery of the mismatch or collisions.

The independent six-card rule is now literal and correct. It retains
`SD-C01`, `SD-C02`, and `SD-C04`; `SD-C02` survives because its one
period-one zero orbit is a nonempty intrinsic ledger. `SD-C04` uniquely wins
the A3 comparison and then A4. The rule uses known historical Route cards and
was corrected after provisional Paper-40 outputs. Its independence is the
absence of imported P39 ranking or cross-candidate coordinates, not blindness
to prior results.

Paper 39 contributes terminal-clean provenance only:

- artifact commit `0f194edbfd05af853153043a568ffafd6c2f8afb`;
- metadata commit `18530b90317f6efc43ec2e4601ed8cef57daaddc`;
- research Route SHA-256
  `7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd`;
- sealed Route-card SHA-256
  `3a5da787a2d20439f345610b7523a565bf1eb55a618b977933ef1046eab0dbb8`;
- 91-entry Paper-39 manifest SHA-256
  `9fe17f0e746fa57a3dbbec7c96d4578b480b6cebcd04c7cb1be03209692516bd`.

None of these selects, ranks, or authorizes `SD-C42`.

## 4. Closest prior art and collision classes

| Claim component | Closest prior art | Novelty disposition |
|---|---|---|
| Nuclear Gauss transfer operator on a holomorphic space | [Mayer 1990](https://doi.org/10.1007/BF02473355) | Foundational prior art; not a P40 contribution |
| `Z(s)=det(I-L_s)det(I+L_s)=det(I-L_s^2)` for the modular group | [Mayer 1991](https://doi.org/10.1090/S0273-0979-1991-16023-4) and the official [MPIM preprint](https://archive.mpim-bonn.mpg.de/id/eprint/346/) | Exact functional prior art |
| Continued-fraction/modular-geodesic coding | [Series 1985](https://doi.org/10.1112/jlms/s2-31.1.69); [Arnoux--Schmidt 2026](https://arxiv.org/abs/2605.09230) | Foundational coding prior art |
| Two-variable transfer-operator zeta mechanism | [Bonanno--Isola 2014](https://doi.org/10.1088/0951-7715/27/5/897) | Strong collision with marker/mechanism novelty |
| Quadratic forms and modular geodesics | [Sarnak 1982](https://doi.org/10.1016/0022-314X(82)90028-2) | Classical arithmetic context |
| Trace/length multiplicities | [Peter 2002](https://doi.org/10.1007/s002201000574); [Belolipetsky et al. 2026](https://doi.org/10.1007/s00220-026-05581-w) | Strong collision with multiplicity novelty |
| Trace/order/field discriminant distinctions | [Maucourant 2025](https://doi.org/10.5802/jtnb.1343) | Required terminology and scope source |
| Prime-geodesic trace arithmetic | [Chatzakos--Harcos--Kaneko 2024](https://doi.org/10.1093/imrn/rnae198) | Recent functional/conceptual overlap |
| Strict and twisted transfer-operator sectors | [Fedosova--Pohl 2020](https://doi.org/10.1007/s00029-019-0534-3); [Pohl--Wabnitz 2026](https://doi.org/10.1090/memo/1616); [Doll--Pohl 2026](https://arxiv.org/abs/2607.14981) | Blocks universal no-twist/no-sector language |

No source found in the documented searches states the exact corrected package
with all three frozen projections, typed return-map splitting, the exact
branch-order discriminator, full target conjunction, and contract-relative
owner firewall. This is a bounded search result, not proof of global absence
and not witness priority.

## 5. Claim-by-claim source audit

### 5.1 Operator and determinant

Mayer owns the operator, nuclearity framework, and modular
Selberg-zeta/Fredholm identity. P40's contribution is not a new operator. It
re-indexes the known even iterate `K_s=L_s^2` on the ordered-pair return space
and proves an intrinsic pair-ledger Fredholm regrouping.

The exact domain split is mandatory:

- nuclearity and the holomorphic Fredholm identity: `Re(s)>1/2` on the stated
  Mayer holomorphic Banach-space realization;
- initial absolute convergence of the Selberg Euler product: `Re(s)>1`;
- source-supported meromorphic continuation: the complex plane.

For the free marker `u`, the Fredholm determinant family exists in the nuclear
setting, but the logarithmic trace and primitive-pair product are used only
coefficientwise/formally in `u^2`, or analytically for sufficiently small
`|u|`. No single-valued logarithm is continued through determinant zeros.
The `u=1` Selberg identity comes separately from Mayer's theorem and is not an
arbitrary-`u` Selberg identity.

### 5.2 Three primitive types

The package correctly separates:

1. `SigmaPrimitiveDigit` under the digit shift `sigma`;
2. `RhoPrimitivePair` under the one-pair shift `rho`;
3. `GeodesicPrimitiveClass` under hyperbolic/geodesic conjugacy.

The grouping map satisfies `rho iota=iota sigma^2`. A least-period-`n` digit
orbit gives `gcd(n,2)` cycles under the squared shift, yielding

`N_(D^2)(k)=2 N_D(2k)+1_(k odd) N_D(k)`.

Thus even digit periods split into two pair phases and odd periods remain one.
The determinant identity at `u=1` does not, by itself, identify these three
primitive types objectwise. No claim may cross them without a separate bridge
theorem.

### 5.3 Matrix, branch, and clock

With `A(a)=[[a,1],[1,0]]` and the fixed left-to-right stored order, the
matrix/branch bridge `A=JBJ` ties the stored monodromy to the same Gauss branch
used by the operator. Raw summation indices of `L_s^(2k)` compose in the
reverse order, so rewriting them in stored composition order requires global
dummy-index reversal and the corresponding nested weight. The
non-palindromic exact fixture distinguishes the correct branch/weight
`442/623`, `16/388129` from the wrong same-index values `146/697`,
`16/485809`.

For `t=tr M`, the three frozen projections are exactly

- `P_t=t`;
- `P_Delta=Delta_(Z[M])=t^2-4`;
- `P_N=lambda_+^2`.

The discriminant notation is the characteristic/order discriminant of
`Z[M]`, not automatically the fundamental field or multiplier-ring
discriminant. The geodesic norm is a real quadratic unit and is generally
irrational; it is not a rational integer merely because “prime geodesic” uses
prime terminology.

### 5.4 Exact witnesses and all-orders firewalls

The exact trace-4 reversal pair, trace-6 non-reversal pair, and trace-10
cross-pair-length non-reversal pair are valid contract falsifiers. None is
claimed to be first, novel, or minimal. The trace-10 fixture is retained only
for its cross-length property.

The universal conclusions rest on algebra, not finite enumeration:

- `Delta=(t-2)(t+2)` is rational prime only at `t=3`;
- `lambda_+^2` is irrational because its polynomial has nonsquare
  discriminant `t^2(t^2-4)`;
- `q_r=tr(M^r)` obeys the Cayley--Hamilton recurrence rather than `t^r`;
- trace and order discriminant fail exact temporal powers;
- `lambda_+^2` passes the exact clock and temporal powers but fails rational
  integer/prime support;
- every `t>=3` occurs for the one-pair family `((1,t-2))`, so no constant
  rescales `log t` to the exact source clock on all realized traces.

The bounded 39,622-row prototype checks implementation and fixtures only. It
does not prove the infinite Fredholm identity, the all-orders algebra, witness
minimality, or novelty.

### 5.5 Target amplitude and ownership

The positive comparison object is the reciprocal determinant. For a primitive
pair word of pair length `k`, the local/formal source logarithmic coefficient
is

`u^(2kr) d_w^(rs) / (r(1-d_w^r))`,

whereas a hypothetical rational-prime factor contributes

`u^(2kr) p^(-rs) / r`.

Even the formal assignment `p=lambda_+^2=d_w^(-1)` leaves the source stability
denominator and Selberg tower. A full match must preserve support, bijective
target multiplicity, powers, clock, digit marker, amplitude, sign,
orientation, phase, controls, and one operator-owned trace.

The package proves only an absence-of-declaration fact: no rational-prime
scalar selector is declared to own a reducing sector of the frozen untwisted
`K_s` schema. The positive toy owner and prime-indexed direct-sum
countercontrol correctly demonstrate that other operators or twists can own
selected sectors. Universal selector nonexistence is not claimed.

## 6. Novelty grades

| Contribution atom | Score | Reason |
|---|---:|---|
| New transfer-operator or Selberg mechanism | 1/10 | Mayer and later transfer-operator literature own the mechanism |
| Individual algebraic identities | 2/10 | Mostly elementary `SL_2` and quadratic algebra |
| Exact typed three-projection closure | 5/10 | Useful contract-specific theorem synthesis |
| Reproducible marker/operator/ownership audit | 5/10 | Strongest methodological contribution |
| Overall research novelty | 4/10 | Narrow closure value, heavy ingredient and qualitative prior art |

## 7. Required publication language

The following wording constraints are part of the verdict:

- use “two-digit/even-iterate Gauss--Mayer return,” not bare “even continued
  fraction” terminology;
- call `t^2-4` the trace/order or `Z[M]` discriminant;
- call `lambda^2` the geodesic norm/quadratic unit;
- define “prime geodesic” as primitive rather than rational-prime labeled;
- describe `u` as digit-counting bookkeeping, not a new two-variable zeta
  mechanism;
- restrict non-ownership to the frozen untwisted schema;
- preserve pair/digit/geodesic primitivity types;
- concede Paper-1/`SD-C04` priority and the retrospective M1--M25 chronology;
- state that P39 supplies provenance only;
- keep `route_b_invocation_allowed: false`.

Belolipetsky--Cosac--Doria--Teixeira Paula must be cited as *Communications in
Mathematical Physics* **407**, article 76 (2026), published 9 March 2026, DOI
`10.1007/s00220-026-05581-w`; it is not issue `407(4)`. Maucourant must appear
once, not as duplicate records under two discriminant descriptions.

## 8. Strongest counterargument

The proposed contribution can be read as a retrospective repackaging of an
already rejected Gauss--Mayer candidate. Mayer already owns the operator,
nuclear Fredholm determinant, and modular Selberg-zeta identity; Paper 1
already owns the qualitative rational-prime mismatch and thousands of finite
trace collisions. After provisional Paper-40 outputs were known, the contract
was changed to repair the selection rule, collision witnesses, GO logic,
multiplicity conditions, determinant sign, branch order, and primitive object
type. The new pair-return ledger is not the historical digit ledger: even
digit orbits split into two pair phases, odd ones do not, and a pair-primitive
factor may be digit-imprimitive. A finite exact census, however large, cannot
prove the infinite determinant theorem or exclude a future independently
declared twist/projector. Nor can absence of a selector in one frozen schema
become universal nonexistence. The only defensible result is therefore a
narrow, typed closure of exactly three scalar projections under a fully
disclosed retrospective contract. It earns no prospective-selection,
mechanism, minimal-witness, or universal-no-go novelty credit. Publication is
justified only if every manuscript, Route, proof, control, result, and
literature artifact preserves this restricted claim and the precise
Mayer-domain, local-`u`, primitivity, marker, multiplicity, and ownership
boundaries.

## 9. Method limits and final disposition

The search log documents the query families, exact-package check, and
freshness pass. Literature search is intrinsically incomplete. No unpublished
package was sent to an external model, and no cross-model judgment is
fabricated. The independent audit is a source-and-claim review, not proof that
no future paper contains an exact collision.

Final literature disposition:

`PROCEED_WITH_CAUTION_AS_SCOPED_CLOSURE_ONLY`

Automatic downgrade to `DO_NOT_PROMOTE_UNTIL_FIXED` applies if a derivative
artifact drops the internal-priority concession, calls a witness minimal or
novel, calls the marker mechanism new, conflates discriminant or primitivity
types, globalizes the local-`u` product, universalizes selector non-ownership,
attributes selection to P39, or opens Route B.
