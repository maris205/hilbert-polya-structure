# Independent principal-oldform review receipt

Date: 2026-09-07 UTC.

## Scope and actual work

The assigned claim was the all-prime/all-exponent fixed-basis
commutativity of the principal oldform block defined in the parent
AS2 files. The assignment also required verification of width-one
applicability and of the fixed, not spectral-parameter-dependent,
multiplicity normalization.

Read completely: `FROZEN_CONTRACTS.md`, `AS2_CONJECTURE.md`,
`AS2_oldform_probe.py`, and `AS2_CHECK_RECEIPT.md`. The proof-writer
workflow was used to separate the precise proved subclaim from the
unproved or falsified full-level conjecture.

The independent argument was derived by column differences of the
incoming matrix, finite geometric summation, and two reciprocal
polynomial identities. No symbolic or numerical mathematical probe
was launched. In particular the parent's already executed 40-cell
grid was not repeated.

Fresh primary access:
[Booker--Lee--Strömbergsson, arXiv:1803.06016v2](https://arxiv.org/html/1803.06016v2),
version dated 17 April 2020. Directly inspected the displayed cusp
classification and scaling formulas in Section 2.5, the defining
normalizations in Section 2.7, Lemma 2.19 and Remark 2.20. This is
limited section/formula access, not a claim to have read the full
paper. Young's Theorem 7.1 is identified there as equivalent; Young's
paper was not independently reread during the initial principal proof.
The subsequent parity extension did directly inspect Young, as recorded
below.

## Result

`PROOF_PACKAGE.md` gives a fixed basis for every prime $p$ and every
$e\geq0$, all eigenvalues, the genuine cusp reduction, the fixed
multiplicity similarity, and the immediate tensor-product corollary
for the principal channel at arbitrary $N$.

Status: **PROVABLE AS STATED for the assigned principal-sector claim**.
The original full-level AS2 conjecture is not proved or reinstated.
The separate primitive-character review owns the reported level-$50$
counterexample and any repaired criterion.

Scientific-increment assessment: this is a classical-formula
verification lemma, not an independently admitted paper. There is no
target-time mechanism or new arithmetic Euler prescription.

## File and action boundary

The initial principal handoff created only its proof and this receipt
in `arithmetic_spectral/oldform_review/`; the authorized extension added
`TWIST_PARITY_LEMMA.md` in that same directory.
No old-tree, manuscript, formal evaluation, build, global registry,
Git, GPU, external model or paid-API action was taken. No raw outputs
were relabelled as a proof.

## Coordinated parity extension

After both the coordinator and character reviewer identified even-exponent
imaginary-phase cancellation, the assigned local algebra was extended in
`TWIST_PARITY_LEMMA.md`. It proves the complete local parity dichotomy,
its tensor-product noncancellation argument, and the real-character
all-exponent sufficiency. It directly specializes the already inspected
Booker--Lee--Strömbergsson formula for general primitive $\chi$ and
checks the normalization against
[Young, arXiv:1710.03624v2](https://arxiv.org/html/1710.03624v2),
version dated 3 November 2017: definition (3.3), completion before
Proposition 4.1, Proposition 4.2 and (4.6), plus displayed (7.3)
and the adjacent Fourier-basis discussion were directly accessed.
This remains limited section/formula access, not a full-paper read.

The conclusion is conditional on $\chi^2$ being real: its paired
oldform sector commutes if and only if every imaginary unramified
character value occurs at an even exponent of $L=N/q^2$.
The first repair's stronger condition is therefore false, with
$N=100$ a commuting counterexample established without computation.
The nonreal-square necessity for the complete classification remains
the separate character reviewer's task.

All three files are proof/audit artifacts only. No new mathematical
computation was executed; no existing check was repeated. The spelling
of the third source author was corrected to Andreas Strömbergsson
following the coordinator's citation check, without changing any
principal proof formula.
