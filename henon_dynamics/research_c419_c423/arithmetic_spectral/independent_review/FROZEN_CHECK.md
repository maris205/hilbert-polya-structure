# Bounded independent AS2 check

Frozen 2026-09-07 before executing a new arithmetic check in this directory.
The parent [conjecture](../AS2_CONJECTURE.md) is not altered.

## Exact object and decision

Use the full width-one cusp scattering matrix for the single level
$N=50$, with trivial nebentypus and weight zero. The two regular
parameters are $s=2$ and $t=3$. Choose the primitive character modulo
$q=5$ with $\chi(2)=i$, so $\chi^2$ is real; put $L=N/q^2=2$.
There is no parameter search, cusp truncation, or all-level census.

The mathematical check reconstructs Young's Theorem 7.1 coefficient
matrices, with oldform labels $B=1,2$ and fixed cusp-character labels
$f=5,10$. It then forms
$$
M_\chi(s)=10^{2s-1}C_\chi(s)^{-1}C_{\bar\chi}(1-s),
$$
and the conjugate-character partner. The power removes only a common
scalar. The common analytic scattering scalar is dealt with in the
proof, not assigned an arbitrary numerical value. Gauss-sum phases are
removed by one constant similarity. A fixed Walsh change of coordinates
selects the plus channel. No change of coordinates depends on $s$.

Success for this falsification check means proving a nonzero commutator
of this invariant fixed-coordinate block. The anticipated exact entry,
obtained by hand before CPU, is $384i/221$. A successful check refutes
the proposed sufficiency but does **not** classify all levels or admit
a new manuscript. A failure triggers inspection of the derivation;
it does not trigger an expanded search.

## Authorization and stops

Write only this `independent_review/` directory. No oldform principal
probe rerun, full scattering census, paper, evaluation, Git mutation,
paid model, or external upload. Primary source applicability is checked
against Young arXiv:1710.03624v2; the coordinator owns the wider novelty
search. Stop after a minimal proof, exact check and receipt, with the
full classification explicitly open.
