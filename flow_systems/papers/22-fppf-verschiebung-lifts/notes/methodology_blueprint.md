# Paper 22 methodology blueprint

Date: **2026-08-24**
Design: **sheaf/descent obstruction theorem; no computational experiment required initially**

## Phase-2 typing precondition

Before proof, bind from the primary source:

- a universe-small version, in Deninger's sense, of the absolute site
  `NoethAffSch_fppf`;
- the definitions of `underline Z(O)^sharp` and `W_rat(O)^sharp`;
- the epimorphism `omega` and the source/target conventions for `V_N`;
- the category in which additivity, naturality, and equality are asserted.

If any of these remains ambiguous, the project stays `NOT_TESTABLE`.

## Method

1. Compute the kernel sheaf `K=ker(omega)` and the extension class
   `e in Ext^1(W_rat(O)^sharp,K)` in the abelian category of fppf sheaves.
2. Prove the extension-theoretic precheck: for a fixed induced
   `u:K->K`, an additive lift exists exactly when `u_*e=V_N^*e`; if it
   exists, its choices form a `Hom(W_rat(O)^sharp,K)`-torsor.
3. Only after choosing an actual cover or resolution, determine whether this
   `Ext` condition admits a valid Cech/descent representative; do not assume
   Cech cohomology computes sheaf `Ext` in advance.
4. Evaluate the actual kernel and obstruction first for `N=2`, with `N=1`
   retained only as the identity control.
5. In an existence branch, prove additivity, naturality, choice-independence,
   and the frozen `F/V` laws diagram by diagram.
6. In a nonexistence branch, produce an explicit object/cover on which the
   obstruction is nonzero.

## Controls

- a finer site where `omega` is known to be an isomorphism as a positive
  comparator, without transferring that conclusion to fppf;
- identity or trivial index operations;
- refinement independence of Cech representatives;
- two different local choices yielding the same global lift exactly when the
  obstruction vanishes;
- fp versus fppf kept in separate records;
- generic quotient-sheaf examples demonstrating that kernel knowledge alone
  does not decide the arithmetic lift.

## Failure modes

- the source uses a different site or sheafification than the draft;
- local lifts exist but do not descend;
- a noncanonical section is treated as natural;
- additivity is checked while `F/V` compatibility is assumed;
- a generic extension class is never computed for the actual `V_N`;
- a pure algebra result is promoted into a packet or Route bridge.

## Validation

- exact commutative-diagram ledger;
- independent kernel and obstruction derivations;
- local-to-global proof with cover-refinement audit;
- source theorem/page map and nearest-precedent subtraction;
- devil's-advocate tests for hidden choice and category mismatch.

## Expected output and effort

Source and notation binding are complete.  After a separate user checkpoint,
the next bounded effort is the `N=2` kernel/extension kill test.  Promotion
requires an actual computation of `K,e,V_2^*e` and a decided lift or explicit
obstruction; the abstract Ext criterion alone does not pass.
