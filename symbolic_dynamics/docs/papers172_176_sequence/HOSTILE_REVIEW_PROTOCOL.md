# Dual hostile-review protocol — P172–P176

Every paper must receive two reviews from readers who did not author that
paper.  Each review has two inseparable parts:

1. a proof/claim/source audit recorded as `HOSTILE_REVIEW_A.md` or
   `HOSTILE_REVIEW_B.md`; and
2. an independently written exact verifier with canonical stdout and a
   checksum manifest under `docs/papers172_176_sequence/reviews/`.

Reviewers must attempt to break:

- the literal update and carrier closure;
- every theorem quantifier and exceptional parameter;
- every labelled-target or fibre formula;
- recurrence, period, tail, spectrum, and Jordan claims;
- the division from quotient mass to one labelled target;
- all direct-owner and P1–P171 subtraction statements; and
- anonymity, lifecycle, and computation-versus-proof wording.

Findings are classified `Critical`, `Major`, or `Minor` with stable IDs.
Every nonzero finding count requires a written repair disposition and a new
manuscript round.  A zero-finding review still requires an explicit
no-change rationale and a preserved byte-identical PDF round.  Review A may
not weaken an amber gate; Review B must re-open every live kill switch rather
than merely confirm Review A.

Completion requires:

- two `PROVABLE AS STATED` or explicitly repaired verdicts per paper;
- zero open Critical, Major, or Minor findings;
- author and both review verifiers passing from fresh processes;
- preserved `main_round0_original.pdf`, `main_round1.pdf`, and
  `main_round2.pdf`; and
- `HOLD_EXTERNAL` unchanged.
