# HCS-C59 research question

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. Primary question

Let $K/\mathbf Q$ be the released $W(E_6)$-normal closure of the
degree-(27) line field of the fixed cubic surface. Can one construct two
concrete primitive degree-(320) fields inside (K) which have equal
Dedekind zeta functions but are nonisomorphic over $\mathbf Q_3$, without
choosing between the two decomposition groups left open by C58?

At the machine code/results tier, the answer is yes. It is proved with exact
subgroup arrays, exact quadratic orbit sums in the 27 labelled line
coordinates, a complete split-prime primitivity witness, exact global
ramification, and both complete local tables.

## 2. Exact locked formulation

Let (H_+) and (H_-) be the exact embedded subgroups specified in
`THEOREM_PACKAGE.md`. Set (alpha_i=Ld_i) and

\[
\eta_+=\sum_{\{i,j\}\in\mathcal S_+}\alpha_i\alpha_j,
\qquad
\eta_-=\sum_{\{i,j\}\in\mathcal S_-}\alpha_i\alpha_j,
\]

where $|\mathcal S_+|=27+27$ and $|\mathcal S_-|=81$. The notation
(eta) is reserved for the scaled integral invariant. The unscaled object,
if needed, is $\widetilde\eta$ and satisfies
$\eta=L^2\widetilde\eta$.

The certified exact gates prove all of:

1. $\mathbf Q(\eta_\pm)=K^{H_\pm}$ and both fields have degree 320;
2. (H_+,H_-) are the unique minimum-index equal-character collision in the
   complete (W(E_6)) subgroup table, with explicit credit to James;
3. the fields are nonisomorphic with common normal closure (K), while their
   Dedekind zeta functions agree;
4. their signature is ((16,152)), their signed discriminant is
   (+3^{624}5^{496}A^{192}B^{160}), and their exact support is the eight
   C58 primes; and
5. the two finite etale $\mathbf Q_3$-algebras differ for each of
   $D_3=\mathrm{ToM} 140$ and $D_3=\mathrm{ToM} 206$.

## 3. Adaptive relation to C58

C58 classifies all inertia filtrations and leaves the decomposition group at
3 in an exhaustive two-element set. C59 does not finish a deferred C58 Euler
factor. Instead, it introduces two new fixed fields and uses C58's complete
filtration to prove an arithmetic-equivalence/local-inequivalence theorem
that is valid in both branches.

The Phase-1 refusal to lock C59 is historical. Its two causes were an
unreleased C58 and a missing primitive-field bridge. C58 is now released, and
the exact quadratic orbit-sum construction clears the primitive-element gate
inside the official producer/checker tuple. Staged pilot bytes remain only
design chronology; project authority comes from the passing G0--G7 evidence.

## 4. Exact in-scope claims

- durable embedded definitions of (H_+) and (H_-);
- exact supports and scaled integral orbit sums;
- exact product-form monic resolvents $R_\pm(T)\in\mathbf Z[T]$;
- 320 distinct conjugates and primitive fixed-field generation;
- full permutation-character equality and the complete collision inventory;
- common normal closure, nonisomorphism, and equal Dedekind zeta functions;
- exact signature, signed discriminant, and ramified support;
- complete ToM-140 and ToM-206 local row tables; and
- branch-independent nonisomorphism of the finite etale $\mathbf Q_3$-algebras.

## 5. Exact out-of-scope claims

The project does not claim:

- that the Gassmann collision, arithmetic equivalence, local inequivalence,
  or relative-resolvent method is new;
- a minimum degree among arithmetically equivalent fields in general;
- expanded characteristic-zero resolvent coefficients or a coefficient hash;
- an integral basis, maximal order, monogenicity, or a polynomial-discriminant
  equality;
- that `(n,e,f,d)` classifies an individual local field;
- a choice of (D_3), integral permutation equivalence, equal class numbers,
  local equivalence, adelic equivalence, or isomorphic idele groups; or
- any forbidden analytic, rational-point, Brauer--Manin, motive, RH, or
  Hilbert--Polya conclusion.

The literal inherited firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## 6. Success criteria and achieved machine tier

One unchanged official tuple has passed all of G0--G7, the independent
checker, official refresh, mandatory nonmutating replay, and hostile
post-refresh machine audit. It contains 13 source files, 8 result files, 21
live code/result entries, and 20 self-excluding scoped entries. Its 15-key
payload has 10,412 scalar leaves; 20,894 certificate rebound mutations and 8
evidence mutations are rejected; and all 48 tests pass. A fresh formal-root
audit, anonymous paper audit, and release-provenance closure remain future
success gates.

Mathematically, all four local row sets must satisfy (n=ef), total degree
320, and total (sum fd=624). In the ToM-140 branch (F_+) must have eight
degree-one factors while (F_-) has none. In the ToM-206 branch (F_+)
must have four unramified quadratic factors while (F_-) has no degree-two
factor.

## 7. KILL criteria

Any of the following kills the selected theorem:

1. predecessor or guard drift;
2. a raw ToM-only or mutable subgroup definition;
3. a support stabilizer larger than the stated subgroup;
4. fewer than 320 specialized values or any modular coefficient mismatch;
5. sampled rather than full character equality;
6. a lower or additional index-320 collision;
7. any failed signature, exponent, sign, or support rebind;
8. an incomplete local row table or a failure in either branch;
9. substitution of the historical graph-feasibility computation for the
   official full G1 reconstruction; or
10. any source, scope, or status overclaim.

No failure licenses an abstract-pair, one-branch, discriminant-only, or
resolvent-only fallback paper.

## 8. Current state

The code/results tier is `PREFREEZE_CODE_RESULTS_PASS`, and the independent
post-refresh machine hostile audit is `POSTREFRESH_PASS`. Principal SHA-256
bindings are payload
`a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b`,
certificate
`3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a`,
check report
`271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3`,
schema file
`07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4`,
group/resolvent evidence
`0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958`
and
`667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6`,
scoped manifest
`c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda`,
payload shape
`788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2`,
and G0 subpayload
`ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d`.

The changed formal roots have passed their hostile audit. Paper construction,
paper audit, compilation, release provenance, promotion, and release remain
pending.
