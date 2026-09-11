# Additive response to the closed-pointer candidate gate

2026-09-08 UTC. CORRECTIONS_SUBMITTED / SAME_REVIEWER_ACCEPTANCE_PENDING.
This is an author response to PTR-G-S1/C1/D1, not a gate verdict. All three
Minors remain OPEN in the unchanged reviewer record until that reviewer
accepts an exact response. PTR-G-E1 also remains OPEN: no actual pilot
output or execution binding is supplied by this document.

## Scope and preserved inputs

The controlling gate is [REPORT.md](../finite_pointer_residual_gate/REPORT.md),
with its complete [source boundary](../finite_pointer_residual_gate/SOURCES_AND_SUBTRACTION.md),
[mathematical audit](../finite_pointer_residual_gate/MATHEMATICAL_AUDIT.md)
and [finding census](../finite_pointer_residual_gate/FINDINGS.json).
All four were read completely for this response. The original five-payload
author dossier, eight-payload gate, prepared scientific pilot and sealed
runtime preparation remain unchanged. This new directory is the sole write
scope. There is no new proof, scientific execution, larger box, manuscript
number, candidate admission or independent review here.

## PTR-G-S1: corrected attribution and subtraction

The original author source account was incomplete. The following two
attributions supplement it; they do not replace or narrow its existing
Manna–Waldinger, Loginov–Reps–Sagiv and Holroyd et al. credits.

**Pham.** For a fixed finite strongly connected directed multigraph G,
with fixed local cyclic orders, let T_G(v) count oriented spanning trees
toward v, d_G^+(v) be its outdegree, and M=gcd{T_G(v):v in V(G)}.
Theorem 1 states that every recurrent rotor-router orbit has size
(1/M) sum_v d_G^+(v)T_G(v), and the number of recurrent orbits is M.
Orbit size is independent of the chosen local cyclic orders, although
the orbits themselves may change. Loops and parallel edges are allowed.
These are Pham's established full fixed-digraph orbit facts, not merely
the Eulerian special case, and receive no pointer contribution credit.
[Trung Van Pham, arXiv:1403.5875v8, 30 June 2015](https://arxiv.org/pdf/1403.5875v8),
Theorem 1 on PDF page 2; conventions on page 3; its full proof on pages 6–7
(extracted lines 263–321).

The citation is to recurrent rotor states on a fixed digraph with fixed
cyclic orders. It is not a proof that every arbitrary pointer state is
that rotor state, nor a claim that all possible encodings or factors have
been excluded. The gate's same-core comparison has its expressly bounded
scope. The pointer dossier receives no novelty credit merely because
Holroyd et al.'s older discussion did not state the broader Pham theorem.

**Berdine–Cook–Distefano–O'Hearn.** Example 8 explicitly analyzes reversal
of a panhandle list: the handle is reversed, the cycle is reversed, and
the handle is reversed again. The discussion names 2i+j+k as decreasing
with each loop iteration, where i measures the handle and j,k describe
the two cycle segments. Thus doubled handle traversal/restoration and
its linear clock are established prior reasoning, even though their
Mutant analysis did not detect that ranking quantity.
[Berdine et al., CAV 2006 author-hosted prepublication](https://jberdine.github.io/pub/2006_cav.pdf),
PDF page 13, entire Example 8 paragraph, extracted lines 665–679.

That initialized terminating-list argument is not presented as an
arbitrary-pair, no-nil exact periodic-orbit theorem. Conversely, removing
nil does not make its doubled-handle mechanism new. No audit of the
paper's general termination-analysis algorithm is claimed in this response.

For this correction, the Pham theorem/model/convention statements and
complete Theorem 1 proof were reread directly, as was Berdine et al.'s
entire Example 8 paragraph. The gate's source table remains the source
audit for its other cited works; this response does not relabel their
whole papers as newly read. These additions correct ownership wording
only and make no global novelty or universal nonconjugacy claim.

Proposed disposition: attribution correction supplied for the same
reviewer's inspection; PTR-G-S1 remains OPEN pending acceptance.

## PTR-G-C1: exact finite-coverage wording

The only prepared pilot scope is n=1,2,3,4, totaling 4,356 full states.
Preparation is not an observed finite result. No family has been
claimed actually exercised on the strength of this response.

If that exact pilot is later executed and its evidence accepted, the
following subclasses will still have no representatives in it:

| Subclass absent from n<=4 | Length conditions and core size s | First possible s |
|---|---|---|
| Figure-eight with two long cycles | a,b>=3; s=a+b-1 | 5 |
| Barbell with two long cycles | a,b>=3, bridge c>=1; s=a+b+c-1 | 6 |
| Theta with three nondirect paths | a,b,c>=2; s=a+b+c-1 | 5 |

Here a,b,c count edges in the same core conventions used by the unchanged
dossier and gate. In particular, a nondirect path has an internal vertex.
The third row is essential: the degree-four coefficient checks cannot
exercise the three-nondirect-path theta orbit-order quotient.

The gate's all-parameter orientation/order arguments deductively cover
these cases. A future accepted small-box result would remain a finite
check of represented cases, not a proof of the all-parameter theorem or
a demonstration that every orientation, degeneration or multiplicity
subcase was executed. The gate's hand-derived polynomials are expectations,
not independent literal-run output. No cutoff expansion, n=5 or n=6 run,
or new predicate is requested or authorized by this wording correction.

Proposed disposition: coverage correction supplied for the same reviewer's
inspection; PTR-G-C1 remains OPEN pending acceptance.

## PTR-G-D1: historical full-read claim withdrawn

My original source table incorrectly described P167 as
“Lines 1–180 (complete file returned).” The complete-file clause is false
and is withdrawn. The original table and native record remain sealed.

The independently checked historical facts are:

| Recorded read | Exact command and archived native result | True extent |
|---|---|---|
| Author's earlier read | sed -n '1,180p' papers/167-minimum-inverse-position-feedback/main.tex; chunk c59488; exit 0 | Exactly the first 180 lines, ending at the table's midrule, before the proofs |
| Gate's later read | cat papers/167-minimum-inverse-position-feedback/main.tex; chunk 9a718e; exit 0 | All 385 lines of the same pinned file |

The unchanged original has SHA256
500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73.
The new documentary check compares the earlier archived output with the
exact first-180-line byte prefix, and the later gate output with the
complete source bytes. Both equalities hold. This is mechanical archival
binding, not a new scientific execution or a fresh P167 theorem audit.

Corrected historical wording for any future account:

> The author originally read only P167 lines 1–180, not the full 385-line
> source. Current subtraction additionally relies on the gate reviewer's
> separate later complete read. That later action does not retroactively
> enlarge the author's earlier read or transfer credit for the full audit.

The gate's completed P167 source reading supplies the current independent
subtraction extent. It cannot make the old completeness claim true.
No original source table, author native record, P167 file or gate artifact
is edited by this correction.

Proposed disposition: exact additive history correction supplied for the
same reviewer's inspection; PTR-G-D1 remains OPEN pending acceptance.

## PTR-G-E1 and handoff

PTR-G-E1 is NOT addressed by these documentary corrections and remains
Major / OPEN. Runtime preparation, source acceptance, checked manifests,
hand-derived coefficients and this response are not actual finite data.

Root must receive the separately authorized exact source/runtime binding,
actual complete pilot output, its asserted comparison evidence and real
native records. Root will then return this exact response together with
that finite evidence to the same gate reviewer. No reviewer acceptance,
candidate admission, paper number or further execution is inferred here.

The project research skill enforces the additive-only correction and
same-reviewer gate. Root and this author remain proof contributors, not
independent manuscript reviewers. OWNER_AMBER / HOLD_EXTERNAL.

