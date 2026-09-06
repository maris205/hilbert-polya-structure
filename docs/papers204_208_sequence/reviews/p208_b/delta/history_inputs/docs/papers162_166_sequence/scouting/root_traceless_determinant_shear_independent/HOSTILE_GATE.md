# Independent hostile gate — traceless determinant shear

**Candidate:** `Phi(A)=A+det(A)I` on traceless `2 x 2` matrices over
`F_{2^m}`  
**Decision:** **KILL**  
**Code:** `KILL_CONJUGATE_TO_CLASSICAL_ARTIN_SCHREIER_LINEAR_MAP`  
**Secondary code:** `KILL_PROOF_ENGINE_COLLISION_P115`  
**Lifecycle:** **HOLD_EXTERNAL**

## 1. Independence and pinned input

This gate did not import or modify the root scout.  The sole root artifact
available at freeze time was
`scouting/root_traceless_determinant_shear/verify_scout.py`, pinned at

```text
2eb951016b494d55d8d2d305566b08f71ed50c7665759ff46415b37d0d54d91b
```

I rederived the formulas from the literal matrix map and wrote a separate
finite-field implementation that discovers its irreducible moduli at
runtime.  Exact enumeration is falsification pressure only.

## 2. Decisive hostile observation

Write a state as `A=(a,b,c)` for `[[a,b],[c,a]]` and put
`e=det A=a^2+bc`.  Then

```text
Phi(a,b,c)=(a+e,b,c),
det Phi(A)=e^2+e=D(e).
```

The advertised determinant semiconjugacy is correct but incomplete.  The
map

```text
H(A)=(b,c,det A)
```

is bijective because `a` is uniquely recovered as the square root of
`e+bc`.  Consequently

```text
H Phi H^{-1}(b,c,e)=(b,c,e^2+e).                  (1)
```

Thus the entire system is exactly `q^2` passive copies of the classical
Artin--Schreier linear map `D(x)=x^2+x`.  There is no matrix-sensitive
pullback, target fibre, or recurrent structure left after (1).

The Route-A gate explicitly assigns generic Frobenius/Artin--Schreier facts
zero credit.  This full conjugacy therefore kills the candidate even though
the proposed formulas are mostly correct.

## 3. Formula adjudication

Let `R_t(z)=1+z+...+z^{t-1}` for `t>=1`, `R_0=0`, and let
`s=2^{v_2(m)}`.

| proposed statement | verdict | independent form |
|---|---|---|
| determinant semiconjugacy | **correct but materially weak** | upgrade to the full bijective conjugacy (1) |
| pointwise iterate | **PASS** | `Phi^t(A)=A+R_t(D)det(A)I`, and `det Phi^t(A)=D^t det(A)` |
| sharp tail | **PASS** | `D` has one zero-primary block of size `s`; maximum tail is `s` |
| recurrent count | **PASS** | `q^2 2^{m-s}` |
| depth CDF | **PASS** | `#{depth<=t}=q^2 2^{m-s+min(t,s)}` |
| exact depth shells | **PASS** | depth zero is `q^2 2^{m-s}`; depth `j` is `q^2 2^{m-s+j-1}` for `1<=j<=s` |
| time-`t` image | **PASS** | size `q^2 2^{m-min(t,s)}` |
| every-target feasibility | **PASS, simplifies** | for target `B`, feasibility is exactly `det B in im D^t` |
| proposed `R_t(D)det(B)` condition | **PASS, equivalent** | `R_t(D)e in im D^t` iff `e in im D^t`; it is not a second inverse invariant |
| nonempty fibre | **PASS** | size `2^{min(t,s)}` |
| time-one trace criterion | **PASS** | `Tr_{F_q/F_2}(det B)=0`, with two sources |
| fixed iterates | **PASS** | `q^2 2^{deg gcd(R_k,(z+1)^m+1)}` |
| exact periods/zeta | **PASS but zero-credit** | ordinary Möbius conversion of the fixed sequence |
| recurrent-target exact `t`-ancestry | **PASS** | every recurrent target has `2^{min(t,s)}` exact `t`-step sources |
| recurrent-target cumulative ancestry | **false if stated for arbitrary recurrent targets** | the union through time `t` also depends on the target's recurrent period; simple law holds only for fixed targets |

## 4. Why the two-primary tail is exactly `s`

In a normal basis, Frobenius is cyclic with polynomial `z^m+1`.  For
`D=F+I`, the characteristic and minimal polynomial are

```text
chi_m(z)=(z+1)^m+1.
```

Writing `m=su`, with `u` odd and `s` a power of two,

```text
chi_m(z)=((z+1)^u+1)^s.
```

The inner polynomial has a simple zero at zero, so `chi_m` has exact
zero-primary factor `z^s`.  Cyclicity gives one nilpotent block of length
`s` and an invertible complement of dimension `m-s`.  All clock, image,
fibre, and depth formulas follow immediately from this decomposition.

## 5. Cumulative-ancestry counterexample

Let a recurrent target determinant `e` have period `r` under the invertible
part of `D`.  The exact `j`-step source set has size `2^{min(j,s)}`, but its
recurrent coordinate is `D^{-j}e`.  Sets at different times are disjoint
unless the times agree modulo `r`; within one residue class their nilpotent
kernels are nested.

For `m=3`, one has `s=1` and each nonzero recurrent determinant has period
three.  Choosing such a target gives

```text
|Phi^{-1}(B)|=2,
|Phi^{-0}(B) union Phi^{-1}(B)|=3,
```

not two.  More generally, if
`j_rho=rho+r floor((T-rho)/r)`, then

```text
| union_{0<=j<=T} Phi^{-j}(B) |
 = sum_{rho=0}^{min(T,r-1)} 2^{min(j_rho,s)}.
```

Therefore any promoted contract must use “exact `t`-step fibre” or restrict
the simple cumulative claim to fixed targets.  This defect is independently
fatal to the broad ancestry wording, although the conjugacy kill already
settles the candidate.

## 6. Independent exact verification

The reviewer program `verify_gate.py` imports no author code.  It constructs
true fields `GF(2^m)` from irreducible binary polynomials found at runtime,
checks field/Frobenius/square-root/trace identities, exhausts every matrix,
and compares both the literal map and the conjugacy.

```text
fields: GF(2^m), 1<=m<=6
literal states: 299,592
assertions: 7,770,987
symbolic zero-primary/gcd boundaries: 1<=m<=256
verifier SHA-256:
  48d1a9da61fefc219eed4b937cbe9fd1ed65155d79f35ee94fe84b8c063ba760
canonical SHA-256:
  f1e80f0a7b10921d2fbdd1f35171482d81dfcead3b6759a8fa97a7c4fec11ac6
fresh replay 1:
  f1e80f0a7b10921d2fbdd1f35171482d81dfcead3b6759a8fa97a7c4fec11ac6
fresh replay 2:
  f1e80f0a7b10921d2fbdd1f35171482d81dfcead3b6759a8fa97a7c4fec11ac6
result: 2/2 byte-identical; PASS
```

The state total is
`8+64+512+4096+32768+262144=299,592`.  Tests cover the bijection and its
inverse, literal iterates, full image and target-fibre tables through and
beyond the nilpotent cap, depth histograms, trace feasibility, fixed counts,
exact-period Möbius counts, recurrent exact-time fibres, and the `m=3`
cumulative counterexample.

## 7. Owner and internal-collision gate

The bounded exact-phrase search found no public record using the proposed
matrix name.  That does not help: Panario--Reis and the broader linearized-
polynomial literature own the finite linear functional-graph machinery, and
the task mandates zero credit for Frobenius/Artin--Schreier facts.

Internally, P115 is decisive.  It already uses an explicit conjugacy to a
Frobenius permutation times nilpotent shifts and derives uniform fibres,
image sizes, depth CDF, fixed counts, cycles, and zeta data, while explicitly
subtracting the generic linear engine.  TDS has no P115-like bounded
specialization left: the `b,c` coordinates are passive copies.

P125 and P127 are not literal conjugates, but they occupy genuine nonlinear
quadratic-shear and state-dependent matrix interfaces; TDS cannot use its
matrix presentation as separation after (1).  P162 is stochastic and has a
genuinely target-sensitive stabilizer/history axis, absent here.

Complete receipts are in `OWNER_AUDIT.md` and `COLLISION_FIREWALL.md`.

## 8. Final gate

| mandatory GREEN condition | result |
|---|---|
| natural literal self-map | yes |
| formulas and boundaries correct | mostly yes; cumulative ancestry needs restriction |
| two independent theorem axes | **no**; all axes are one linear module |
| owner-distinct after AS subtraction | **no** |
| proof-engine-distinct from P1--P165 | **no**, decisive P115 collision |

**Final decision: KILL.**  Do not allocate P166, draft a paper, or promote a
theorem contract from this candidate.  Preserve the dossier only as a
permanent exclusion.  External posting, circulation, submission, or owner
contact remains **HOLD_EXTERNAL**.
