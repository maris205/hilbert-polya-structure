# HCS-C190: Bulgarian solitaire recurrent-necklace route

This release freezes the ordinary noninvertible Bulgarian-solitaire map on
the integer partitions of every `N>=1`.  With the unique decomposition

\[
N=\binom{k}{2}+r,\qquad 0\le r<k,
\]

Brandt's attributed theorem identifies recurrent partitions with length-`k`,
weight-`r` binary words.  The explicit map adds the word to
`(k-1,k-2,...,0)` and deletes a final zero; one Bulgarian move is right
rotation.  This single source theorem closes every positive-iterate fixed
count, every least period and primitive cycle, the full finite zeta, the full
Koopman algebraic spectrum, recurrent-core reflection reversal, and the
triangular boundary.

## Exact result

For `t>=1`, put `g=gcd(k,t)`.  Then

\[
F_t=\#\operatorname{Fix}(T_N^t)=
\begin{cases}
\binom{g}{rg/k},&(k/g)\mid r,\\
0,&\text{otherwise}.
\end{cases}
\]

For each `d|k`,

\[
P_d=\sum_{e\mid d}\mu(d/e)F_e,\qquad C_d=P_d/d,
\]

and therefore

\[
\zeta_{T_N}(z)=\prod_{d\mid k}(1-z^d)^{-C_d}.
\]

On all functions on the full partition set,

\[
\det(\xi I-U_N)=
\xi^{p(N)-\binom{k}{r}}\prod_{d\mid k}(\xi^d-1)^{C_d}.
\]

Thus zero has algebraic multiplicity `p(N)-binom(k,r)`; the nonzero
root-of-unity multiplicities come from the cycle blocks.  The phase-zero
reflection `Q(w)_i=w_(-i mod k)` reverses rotation on the recurrent core.
The `k` phase-labelled formulas `rho^a Q` need not act distinctly when the
weight layer is nonfaithful.

## Reproduce

Run from the repository root:

```bash
python henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/code/c190_bulgarian_necklace_producer.py
python henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/code/c190_bulgarian_necklace_checker.py
python henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/code/c190_sympy_crosscheck.py
python henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/code/c190_replay.py
python henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/code/c190_mutation.py
python henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/code/c190_release_manifest.py
```

The finite oracle covers `N=1,...,40`: 215,307 direct partitions, 757
recurrent words, 114 cycles, 248 fixed rows, 117 period rows, and 248 spectral
rows.  The independent checker passes 658,664 assertions, the separate SymPy
path passes 2,210 checks, replay is byte exact, and the hostile suite rejects
118 repaired-hash mutations plus one stale-hash mutation.

## Boundary and verdict

Complete transient functional trees, exact hitting-time distributions, and
nilpotent Koopman Jordan sizes are outside the claim.  The map is not globally
invertible, so no global reversor is asserted.  The finite census is a
regression oracle, not an all-`N` proof.

Route tuple:
`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`; Route B is false.  Scope literal:
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The sources retain ownership of the recurrent theorem.  This package is not
an external review, an acceptance score, or a literature-wide novelty
certificate.
