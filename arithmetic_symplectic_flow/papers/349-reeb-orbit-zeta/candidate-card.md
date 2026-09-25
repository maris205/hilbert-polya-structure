# P0 — same-flow orbit zeta and scalar trace audit

**Audit ID:** `ANG-AUDIT-20260921-RCZ01`  
**Unchanged flow ID:** `ANG-20260921-RCF01`  
**Version/date:** v1, 2026-09-21.  
**Freeze status:** `P0 FROZEN; SAME-FLOW ZETA AND SCALAR TRACE OPEN`.

## 1. Authority and exact owner relationship

The user requested the next step after348. Root stated that this means a
bounded same-object analytic-layer audit, with an optional question allowing
the user to redirect to naturalness. This card supplies that analytic scope;
it does not authorize formal Route A/B, quantization, a spectral target,
external circulation or changes to the flow. Strong naturalness stays OPEN.

This is a NEW analytic-audit identity, NOT a renamed dynamical candidate.
The full underlying source, contact form, flow, quotient and packet convention
are exactly RCF01, pinned to348's card and proof:

- Full219-line card SHA-256:
  `062f1ac4c797f9f0562f4236cd7e738420129120a41d111bcfc3c697ca186f25`.
- Full603-line paper SHA-256:
  `6ebce46d764aa9455349ff7d859eec5a4439aa4df7eb81a4d8d4e64b34045cff`.

Those348 files are read-only. Their source/quotient/packet results may be
used only after verifying the EXACT SAME INPUTS, not as cross-candidate
credits. Root has read the complete card and mathematical continuation
G1–G4/P1/C1–C3/S1–S2/supplement, including all original controls.

## 2. Restated full dynamical tuple

W consists of all finite ordered positive-integer words, including empty,
units, repetitions and arbitrary order. Cover atoms r>1 have no proper
nonunit integer divisor. fct(n) is the increasing complete atom-factor word
with multiplicities and product n; fct(1)=empty. Freeze

```text
C((n))=fct(n); C((a,b,tail))=(gcd(a,b),tail); C(empty) undefined;
Y=coproduct_w {(q,xi,z):q>0,xi,z real}; mu=counting_W x dq dxi dz;
S(w,q,xi,z)=(Cw,q/a,a xi,z), a=first entry, w nonempty;
u=log q, v=q xi;
beta=(1+vz)du+(v dz-z dv)/2;
G={(y,m-n,x):m,n>=0,S^m y=S^n x,all steps valid};
source=x,target=y, inherited topology in Y x discrete Z x Y;
Q=Y/G with the full quotient topology;
Phi^t(w,q,xi,z)=(w,exp(t)q,xi,exp(-t)z), t in R.
```

All inverse branches are the singleton(n) branch over fct(n), restoring
(nQ,X/n,Z), and ALL pairs(a,b,tail) over(gcd(a,b),tail), restoring
(aQ,X/a,Z). Each has the whole target chart as domain. All incoming data,
actual lag kernels and transverse states remain. Equal triples, not arbitrary
rewrite histories, are the arrows. No new roof or per-prime clock is added.

The proved full quotient coordinates in348 are one R^3 terminal component
and one(R/(log r)Z) x R^2 component per atom, with

```text
Phi^t([u],v,z)=([u+t],exp(t)v,exp(-t)z);
nu=beta wedge d beta=du dv dz (descended contact volume).
```

The circular lengths are consequences of S, not newly prescribed inputs.
Nu is NOT the infinite-sheeted pushforward of mu. It is infinite, and
Phi^1 is not measure-theoretically conservative. The full primitive set
P consists of the actual Phi-orbits, not selected labels or source points.
The certified348 ledger supplies one period-log r primitive per atom and
no other closed orbit; repetitions k ell_gamma belong to that same orbit.
The actual transverse first-return map is(v,z)->(rv,z/r). These are the
same-flow input lemmas to this audit, not new conclusions at this freeze.

Lineage: proper-divisor admissibility -> atom words/gcd dynamics -> full
contact geometric lift -> the SAME physical packet ledger's analytic layer.
No new arithmetic carrier, unrelated trace formula or operator is substituted.

## 3. Central analytic object: ordinary physical orbit zeta

For s complex, initially TEST absolute/local uniform convergence in Re s>1:

```text
Z_orb(s)=exp(sum_(gamma in P) sum_(k>=1) exp(-s k ell_gamma)/k);
D_orb(s)=1/Z_orb(s);
Theta_orb=sum_(gamma in P) sum_(k>=1) ell_gamma delta_(k ell_gamma).
```

All primitive weights are1; k^-1 is the ordinary repetition convention.
The central object is Z_orb, normalized by Z_orb(s)->1 as Re s->+infinity.
D_orb is just its reciprocal, NOT a declared Fredholm determinant.
Theta_orb is a length-counting distribution, NOT a declared operator trace.
Prove convergence, legitimate rearrangement/differentiation, and the domain
of any Laplace/logarithmic-derivative identity before using them.

A comparison with the classical Dirichlet series sum_(n>=1)n^-s and its
verified standard analytic continuation is allowed as a consequence of
the derived orbit ledger. No prime-power coefficient, von Mangoldt weight,
Riemann-zero datum or gamma completion is inserted into the flow or zeta.
There is no zero matching or new zero-location claim. A named-function
identity alone is not formal Route A success.

## 4. Separately fixed classical scalar pullback and trace prescription

Freeze the unweighted scalar operator, not a quantum construction:

```text
U_t f=f composed with Phi^(-t), f in C_c^infinity(Q), t in R;
H=L^2(Q,nu); if bounded, its full-H extension is the same U_t;
K_t(x,y)=delta_(Phi^(-t)(x))(y), with respect to nu.
```

No function-space change, amplitude twist or state selection is allowed.
The L2 check concerns this classical transfer operator's ordinary trace
class, not a Route-B Hilbert-space/quantization or generator-spectrum audit.
No self-adjoint generator, zero spectrum or Fredholm identity is presupposed.

For h in C_c^infinity((0,infinity)), the PROPOSED positive-time scalar flat
trace is the joint time/space diagonal-kernel distribution

```text
Theta_0(h)=integral_(t>0) integral_Q h(t) K_t(x,x) dnu(x) dt.
```

This notation is an obligation: prove the diagonal restriction is defined
and the pushforward is locally finite, using the actual full flow kernel.
Do not substitute an orbit formula as its definition. Exclude t=0; no
unfrozen zero-time regularization is supplied. Noncompact geometry and the
countable component union must be checked, not assumed harmless.

Only after Theta_0 is established, define the scalar flat-determinant
FUNCTION where its integral converges absolutely:

```text
D_0(s)=exp(- integral_(0,infinity) exp(-s t) Theta_0(dt)/t).
```

Determine its initial domain, normalization, and any justified continuation.
The name flat-determinant function grants no ordinary/nuclear Fredholm
representation. Test Theta_0 against Theta_orb and D_0 against D_orb using
their actual coefficients; retain any mismatch. Never cancel transverse
Jacobians by hand, insert degree signs or add differential-form bundles
to obtain a preferred answer under this frozen scalar card.

## 5. Own controls and completeness tests

Use all three COMPLETE controls frozen and proved in348, with the same
analytic prescriptions applied to each one's OWN full quotient/volume/flow:

1. FACTOR-OFF: C_F((n))=(n) for EVERY n>=1; gcd coalescence and empty
   terminal as before; same scaled S and Phi. Its singleton inverse is
   only over(n), and no branch targets empty. All gcd-pair branches remain.
2. DRIFT-ONLY: same C,S,G,beta, replace physical flow by
   Psi^t(q,xi,z)=(exp(t)q,exp(-t)xi,z). Do not assume isolated closed orbits.
3. UNIT-HOLONOMY: same C,beta,Phi, replace S by(Cw,q,xi,z), with all main
   word inverses and identity geometry. Retain its source lag kernels.

For each control, apply Z_orb/Theta_orb to ALL actual primitive flow orbits,
and apply K/Theta_0 to its OWN scalar physical pullback and volume. If a
sum or diagonal restriction is undefined, record that outcome rather than
selecting representatives or borrowing MAIN's transverse return map.
Coincident lengths add distinct orbit/repetition contributions; they do not
identify orbits. Finite primitive products may be used only as analytic
approximants with proved tail bounds, never as numerical completeness evidence.

## 6. Ordered gates, stop rules and nonclaims

J1: verify same-flow input identity; establish ordinary physical orbit zeta
and its honest analytic domain/continuation, if available.
J2: derive scalar kernel diagonal/weights and own trace-class status;
establish D_0 only where justified and compare it with D_orb.
J3: audit all three controls, strongest false inference and naturalness limits.

Stop any asserted scalar trace/Fredholm identification as soon as its
coefficient, domain or operator-class test fails. Preserve J1 positives
and the actual J2 object; do not repair the scalar operator or import
another space, bundle, determinant, clock or analytic normalization.
Failure of this scalar choice does not prove every possible transfer or
graded trace impossible. Those choices require a new explicit owner card.

At freeze all NEW analytic conclusions are OPEN. This is a bounded T3
owner-level audit, not a formal Route coordinate: classical A0/A1/A2 NOT
APPLICABLE, formal UNASSIGNED, B NOT INVOKED. Naturalness remains OPEN.
No PDF, external release, Git operation, optimization or new reserve work.

## 7. Pre-freeze exposure

Root knows348's complete period/monodromy results and anticipates an
Euler-product relationship and a possible scalar transverse-weight mismatch.
These design expectations are NOT blind predictions or proved349 results.
No new scientific run has occurred. Only after this card freezes may the
new analytic claims be derived and reviewed; append results without changing
this original contract. Skill/workflow instructions grant no extra scope.

EOF — original analytic P0; results and clarifications must be append-only.

## 8. Post-derivation disposition — original192 lines preserved

**Audit ID:** `ANG-AUDIT-20260921-RCZ01`.  
**Unchanged flow ID:** `ANG-20260921-RCF01`.  
**Current mathematical status:**
`ORBIT ZETA ESTABLISHED; SCALAR IDENTIFICATION STOP; NATURALNESS OPEN`.

The original192-line prefix remains frozen at SHA-256
`7549da0db82ad6b260ce91dbebde484ce8d6045f92b7672f467900a5fdc9366e`.
The mathematical derivations are in [paper.md](paper.md); their review
standing and mechanical verification are recorded separately, not inferred
from this disposition. No source, clock, state, operator or space changed.

- J1: the full ordinary physical orbit zeta is zeta(s), absolutely for
  Re s>1; classical continuation applies after this derived identity.
  Theta_orb has coefficients log p at k log p. D_orb=1/zeta is not
  declared an operator determinant.
- J2: the joint positive-time scalar kernel restricts and pushes forward
  legitimately on this full noncompact quotient. Its coefficient at k log p
  is(log p)/(p^k+p^(-k)-2). This differs from Theta_orb, already at log2.
  Full-H U_t is unitary and not trace class. STOP scalar identification.
- The ACTUAL D_0 is retained without changing its owner:
  D_0(s)=product_(m>=1)zeta(s+m)^(-m), with defining absolute domain
  Re s>0 and a justified meromorphic continuation to C. This is a flat-
  determinant function, not an ordinary Fredholm representation.
- J3: FACTOR-OFF adds genuine composite primitives and their scalar weights;
  DRIFT-ONLY has non-summable primitive families and an undefined frozen
  diagonal trace; UNIT-HOLONOMY has empty positive-time data and functions1.
  Every control uses its own full owner, not a selected representative.

Portfolio **advance** ordinary zeta and actual scalar analytic layer;
**stop** scalar=ordinary trace/determinant. Strong naturalness OPEN.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
No universal operator no-go, zero-location result or Route credit follows.
Any new analytic construction needs a new owner contract and continuation
decision, not a silent repair here. Original348 and the reserve stay fixed.

EOF — appended mathematical disposition; original P0 intact.
