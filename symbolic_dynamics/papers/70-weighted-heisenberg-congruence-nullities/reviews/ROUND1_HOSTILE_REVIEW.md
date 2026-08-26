# Round 1 hostile review

## Provenance and scope

**Provenance:** independent cross-agent review.  The requested GPT-5.4 child
reviewer was unavailable because the agent tree had reached its structural
thread cap.  This report does not claim GPT-5.4 provenance.  The reviewer did
not author P70 and inspected the full manuscript, proof/source ledgers,
bibliography, finite-matrix control, frozen receipt, build files, and round-0
PDF before proposing any edit.

**Release posture:** external release remains **HOLD**.  No priority or
worldwide-novelty conclusion is made.

## Overall verdict

**Verdict:** **MAJOR REVISION, theorem likely correct but the representation-
theoretic convention gate is not yet self-contained.**

**Score:** **7.5/10** at round 0.

The cyclotomic count, determinant identity, recurrence corank bound, and
regular-multiplicity arithmetic check out.  The vulnerable point is earlier:
the manuscript cites a complex/unitary Stone--von Neumann source while it
works over an algebraic closure of `F_p`, and it asserts the exact right-
regular block matrices without exhibiting the intertwiner or the possible
dual.  These are repairable proof-presentation gaps, not evidence against the
main formula.

## Strengths

1. The assumptions `ell` odd, `p != ell`, and all coefficients nonzero are
   explicit and are used at exactly the necessary proof steps.
2. The character elimination has the correct odd-`ell` sign and uses
   separability of `t^ell-1` correctly.
3. The clock--shift determinant proof identifies the only two nonzero
   permutation terms; the cyclic recurrence then upgrades singularity to
   exact nullity one.
4. The full `ell^3` matrices test the actual quotient group law and therefore
   provide a useful convention regression, not merely a repeated symbolic
   block calculation.

## CRITICAL issues

None.

## MAJOR issues

### M1. The cross-characteristic irreducible list is not proved by the cited
complex Stone--von Neumann statement

**Evidence.** `sections/3_regular_decomposition.tex` extends scalars to an
algebraic closure `k` of `F_p` and then says finite Stone--von Neumann theory
gives exactly `ell^2` characters and `ell-1` degree-`ell` irreducibles, citing
Gurevich--Hadani.  That primary source states the unitary/complex finite-field
Stone--von Neumann theorem.  The desired conclusion in algebraically closed
cross-characteristic is true, but the manuscript neither proves the transfer
nor constructs the modules over `k`.

**Required fix.** Add a self-contained lemma over `k` after Maschke:

1. define the `ell^2` characters;
2. for every nontrivial `ell`th root `zeta`, define the clock--shift module
   with `U V = zeta V U`;
3. prove irreducibility because `U` has `ell` distinct eigenspaces and
   `V` cyclically permutes them;
4. distinguish the modules by their central character; and
5. use the sum of squared degrees `ell^2+(ell-1)ell^2=ell^3` to prove
   completeness in the semisimple group algebra.

Keep Gurevich--Hadani as the owner/context citation, but do not ask its complex
statement to silently supply the cross-characteristic step.

### M2. The exact right-regular block convention is asserted rather than
computed

**Evidence.** Proposition `prop:regular-ledger` writes the block as
`alpha I+beta pi(a)+gamma pi(b)`.  Remark `rem:left-right` discusses what
happens after changing conventions, but it does not show which block the
chosen operator `(R_h f)(q)=f(qh)` actually induces on a matrix-coefficient
copy.  In a noncommutative group this omission is precisely where inverses,
transposes, or contragredients enter.

**Required fix.** Define `R_h` explicitly and compute its action on a matrix-
coefficient basis, recording whether the resulting block is `pi(h)`,
`pi(h)^T`, or `pi(h^{-1})^T` under the selected identification.  If a dual
appears, write the ledger using that block and then perform the change of
variables `(u,v)->(u^{-1},v^{-1})` in the character count.  For nonlinear
blocks, state explicitly that duality sends the central character `zeta` to
`zeta^{-1}` and that the determinant/nullity formula is unchanged.  The final
summed formula can remain exactly as stated, but the path to it must be
convention-complete.

## MINOR issues

### m1. Add block-level determinant/nullity controls

The full-matrix checks are valuable, but they do not separately localize a
failure of Lemmas `clock-shift-det` and `nonlinear-nullity`.  For cases where
`F_p` already contains a primitive `ell`th root (for example `(ell,p)=(3,7)`
and `(5,11)`), construct `U,V` directly, compare the determinant with
`alpha^ell+beta^ell+gamma^ell`, and check nullity zero/one on both strata.
This is a sensible regression enhancement, not a proof premise.

### m2. Avoid implying that prior work found the mod-`p` characteristic-three
jump

`BILINGUAL_ABSTRACT.md` says the unit case is the characteristic-three
phenomenon “found in the original `1+a+b` specialization.”  Lind--Schmidt
own the integer element and its mixing example; the audited source does not
state this mod-`p` congruence jump.  Rephrase as “obtained here by specializing
the weighted formula at `1+a+b`.”

### m3. Bring the page-posture metadata into agreement with the artifact

`PAPER_CONFIGURATION.md` targets 8--12 pages while the round-0 PDF has six.
Either revise the target to a six-to-eight-page short note or explain that
the proof additions will move the paper into the stated range.  This is not a
mathematical defect.

## Proof-dependency audit

```text
normal congruence kernel + frozen left shift
  -> right-translation operator on F_p[Q_ell]
  -> scalar extension preserves nullity

Maschke + explicit cross-characteristic irreducibles
  -> right-regular multiplicity ledger
  -> exact convention/dual block formula

character blocks
  -> cyclotomic gcd degree D_(p,ell)

nonlinear clock--shift blocks
  -> determinant Delta_ell
  -> recurrence gives nullity <= 1
  -> Delta_ell=0 iff nullity=1

regular multiplicities + base change
  -> main fixed-dimension theorem
```

The determinant and recurrence nodes are closed.  M1 and M2 concern the two
nodes immediately before them; both must be repaired so the final sum cannot
be accused of a convention-dependent coincidence.

## Source and ownership audit

- Lind--Schmidt’s Example 4.4(a) states that the principal action for
  `f=1+x+y` is mixing; it does not state the weighted mod-`p` quotient
  nullity formula: <https://arxiv.org/html/1502.06243v1>.
- Gurevich--Hadani state uniqueness of the irreducible Heisenberg
  representation with prescribed nontrivial central character in their
  complex/unitary setting: <https://arxiv.org/html/0708.0669v3>.
- Zaidenberg’s primary record explicitly treats positive-characteristic
  convolution and torsion-point counts on abelian lattices:
  <https://arxiv.org/abs/math-ph/0606070>.
- Ford--Jha identify Wendt’s determinant with the resultant of
  `X^n-1` and `(-1-X)^n-1`, matching the unit-coefficient gcd up to a unit
  for odd `ell`: <https://www.tandfonline.com/doi/abs/10.1080/10586458.1993.10504271>.

The bounded exact-formula search did not locate the displayed weighted
finite-Heisenberg nullity theorem.  This remains a bounded audit only.

## Control and reproducibility audit

- All ten baseline full-matrix cases pass and include both Fermat strata,
  both `ell=3,5`, and five coefficient characteristics.
- The script is deterministic and standard-library only.
- The current receipt does not include block-local determinant/nullity checks;
  add them under m1 and regenerate the receipt.
- Round-0 PDF preservation is present and hash-identical to the baseline
  `main.pdf`.
- `FINAL_QA.md`, `PAPER_IMPROVEMENT_LOG.md`, and `SHA256SUMS` are missing in
  the round-0 package and must be produced by the end of Round 2.

## Actionable Round 1 checklist

1. Prove the cross-characteristic irreducible list explicitly.
2. Compute the selected right-regular matrix-coefficient convention and its
   dual alternative.
3. Add direct clock--shift determinant/nullity controls and regenerate output.
4. Correct the unit-case ownership wording and metadata posture.
5. Rebuild before preserving `main_round1.pdf`.

## Release recommendation

**HOLD.** The theorem may proceed to Round 2 only after M1--M2 are made
self-contained and the strengthened controls pass.
