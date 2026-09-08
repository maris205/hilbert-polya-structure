# Non-author internal review: arithmetic frontier helpers

Date: 2026-09-08 UTC. Reviewer: coordinator, not the author of the
arithmetic proof package. Verdict: **PASS_AUXILIARY_PROOFS_ONLY**;
**AF5-G AND AF5-C FULL CONTRACTS UNCLOSED; ZERO ADMISSIONS**.

## Actual inputs and scope

The reviewer read the entire [freeze](FROZEN_CONTRACTS.md) and
[proof package](PROOF_PACKAGE.md), including the generic coding proof,
exact period-four field, both cyclotomic lemmas, source-dependent
finiteness and the shallow effective-DML boundary. Reviewed SHA-256:

| Input | SHA-256 |
| --- | --- |
| `FROZEN_CONTRACTS.md` | `c04925022c3c0887927930865513d57a9d4a8feec5fbf2c8e849430da35150ab` |
| `PROOF_PACKAGE.md` | `117e4876096cda83e5aca813deddf731fae61d0605e6178d3da7c46aadda953b` |

These are byte identifiers, not independent computational certification.
All checks below are hand algebra or exact hypothesis checks. No
mathematical program, old factorization or accepted proof was rerun.

## Generic scheme and dihedral action

The monic relations have pairwise coprime leading monomials, so their
standard monomials give rank $2^n$ over the coefficient ring, including
the repeated-neighbor conventions at $n=1,2$. The formal substitution
$t=-h^{-2}$ is an injection of the rational function field. At each
binary sign word the recursive coefficient matrix is diagonal with
nonzero entries $2\varepsilon_i$; this supplies exactly $2^n$ distinct
formal points. Together with the rank bound this proves generic
reducedness, not just a lower bound on points. The shift and reversal
actions preserve these lifts and their exact periods.

This proves the claimed generic dihedral set. It supplies no transitive
arithmetic monodromy or Galois lower bound; that distinction is essential
and is retained in the author's conclusion.

## Period-four obstruction

Subtracting opposite recurrence equations forces $c=\pm a$ and
$d=\pm b$. The period-two sign choice is correctly removed, and the
remaining choices exhaust three disjoint four-cycles. Their coordinates
both generate and lie in the displayed field
$k(s,\alpha,\beta)$. Transcendence excludes their degeneracies.

At the places $s=-2$ and $s=2$, the two radical square classes have
valuation parities $(1,0)$ and $(0,1)$. They are independent over
$\mathbb Q(s)$; adjoining $s$ first has degree two over $k$. The
involution $s\mapsto-s$ swaps the two radicands and has the stated
order-two lift. Thus the field degree and Galois order are both eight,
and the semidirect action is the order-eight dihedral group.

The reflection has two fixed points on E and none on either V-cycle.
Hence an equivariant permutation preserves E, may swap the V-cycles,
and has only the two half-turn choices within each cycle. This gives
the centralizer order sixteen. In the actual Galois action the V-swap
and E-half-turn are tied by their shared element $s$; the missing
centralizer element cannot fix the V-coordinates while negating $s$.
The proposed all-period maximality is therefore decisively refuted.
No all-period replacement subgroup is proved by this calculation.

## Cyclotomic helpers and exact non-effectivity boundary

The finite-place maximum argument uses integrality of $c$ and proves
integrality in every field containing the periodic tuple. Applying the
complex maximum to every conjugate gives the stated house bound.
Neither bound is misused as a bounded-degree Northcott theorem.

For a hypothetical periodic affine curve, its normalized projective
completion has a finite invariant boundary. A power fixes a pole of
one coordinate. The scalar coordinate functions then have periodic
pole orders, whose positive maximum contradicts the recurrence's
doubling of that pole order. Negative iterates are polynomial, so the
argument genuinely covers every integer index. This excludes periodic
curves for the exact quadratic family, not just nonsingular curves.

The homogenized map and inverse have distinct indeterminacy points,
so the invoked Hénon-type hypothesis holds. Non-density of cyclotomic
periodic points plus invariance of their Zariski closure and absence
of periodic curves does imply finiteness. The invariant-closure step
is a deduction from the source theorem, not its quoted conclusion.
It does not give an effective conductor or period bound. Enumeration
of a known-finite set without a stopping test does not solve AF5-C.

For AF5-D the reviewed statement is qualitative DML only. The direct
pole-order proof was not expanded into an unproved theorem about all
polynomial Hénon normal forms; the broader classical input is labelled
as such by the author. No effective algorithm is certified here.

## Independent primary-source access and ownership limits

- [Ji–Xie–Zhang v2](https://arxiv.org/html/2511.13443v2), explicit
  20 January 2026 header, Definition 1.7, Theorem 1.8 and Corollary 1.9:
  the reviewer actually opened and read these statements. Their scope
  is non-density over the maximal cyclotomic extension. This is an
  imported preprint theorem, not an independently verified long proof.
- [Dullin–Meiss–Sterling](https://arxiv.org/pdf/nlin/0408015), actual
  §3.4 equations (16)–(19): swap reversibility and its fixed-set
  organization are classical inputs, not this package's increment.
- [Endler–Gallas publisher page](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.65.036231):
  actual abstract and bibliographic metadata confirm previous complete
  period-four parametrization. The article body was not accessed;
  the reviewer does not attribute the exact shared-field formula to it.
- [Bell–Ghioca–Tucker](https://arxiv.org/pdf/0808.3266v1), actual
  Theorem 1.3 and Corollary 1.4 on printed page 3: the statement is
  qualitative, not an effective last-hit bound.

This review adds direct opens/finds, not new discovery search queries.
The author's separate source audit has its own wider access ledger;
it is not silently relabelled as the reviewer's independent reading.
No exhaustive novelty search, human peer review or original-source
proof verification is claimed.

## Adjudication

No mandatory mathematical correction was found in the stated helper
proofs. Retain the generic coding, exact field obstruction and
source-dependent finiteness, with all declared classical dependencies.
Reject admission of their shorter fragments in place of the original
all-period Galois classification or terminating cyclotomic atlas.
These remain separate unclosed full questions, and AF5-D remains shallow.

The proof-writer rigor checks and research-review scope checks governed
this internal review. It is not a formal Route-A evaluation, target
arithmetic progress or a fourth paper. `NO_BAD_EULER_OR_ROOT_NUMBER`
is unchanged. Only this review file was written; author inputs were
not modified.

## Subsequent citation-target correction

After the review, the author removed an unverified HTML fragment from
the Ji–Xie–Zhang citation URL. The base v2 URL, theorem number and
mathematical statement remain the same in the reviewer's actual
targeted reread of that paragraph and its application. A read-only
hash now gives `PROOF_PACKAGE.md` SHA-256
`cd7d24ecaa0ec6b8b84eacde2184acc683ea47b6bb21fd64a500a3130a0456bb`.
The initial table identifies the earlier full-read snapshot, rather
than pretending its hash covers these later bytes. This source-link
correction requires no mathematical rerun and leaves the verdict
unchanged; no claim of an automated whole-file historical diff is made.
