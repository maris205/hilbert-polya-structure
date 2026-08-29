# Claims–Evidence Map — P115

Status: author proof package; external release/novelty/priority **HOLD**.
Finite computation is falsification evidence, not a substitute for proof.

| Claim | Main proof anchor | Independent exact control | Boundary / residual risk |
|---|---|---|---|
| `C^t(f)` selects `c_(p^t j)` and applies inverse Frobenius `t` times | Theorem 3.1, induction on `t` | Direct orbit iteration versus closed coefficients in every exhaustive lane | `p^(-t)` is automorphism notation; `t=0` and post-truncation constants are explicit |
| Chain coordinates conjugate `C` to inverse Frobenius times finite nilpotent shifts; Frobenius cycles support the stated components and isomorphic attached trees | Theorem 3.2, explicit forward/inverse coordinate change and product-graph proof | Every state is reconstructed and satisfies the product update; component sizes and per-root layers are exhaustively checked | Generic cyclic--nilpotent decomposition and attached-tree machinery receive zero credit; the empty positive-coordinate product at `n=0` is explicit |
| `Im(C^t)=X_(q,floor(n/p^t))`; all nonempty fibres are uniform and every other fibre is empty | Theorem 3.3, explicit free coordinates | Every target fibre is enumerated; outside-image witnesses are required to have count zero | Formula includes `t=0` and `p^t>n` |
| The fibre and CDF formulas have a complementary rank recount | Proposition 3.4, `F_p`-rank factorization after Theorem 3.1 | Kernel size and image set are checked separately | This route depends on the iterate formula and is not described as logically independent; `C` is generally not `F_q`-linear when `a>1` |
| Pointwise depth is one plus the largest occupied positive-index valuation | Theorem 4.1, coefficient-chain extinction | Literal orbit entry time for every state | Constants are a separate case, so no empty maximum or `v_p(0)` occurs |
| The CDF, all shells, sharp maximum, and deepest-shell cardinality are exact | Theorem 4.1, constraint count and CDF differencing | Full histograms and deepest-shell counts in all lanes, including all `n=0` boundaries | Equal degree does not determine depth; verifier includes a counterexample guard |
| The stable and periodic core is the constants under inverse Frobenius | Theorem 5.1, decreasing images and periodic-image argument | Literal constant orbits in six actual fields | For `n=0`, phase and core coincide |
| `#Fix(C^m)=p^gcd(a,m)`, exact cycles follow by Möbius inversion, and zeta is the cycle Euler product | Theorem 5.1, fixed subfields and divisor inversion | Full-map fixed counts through two Frobenius periods; cycle census; two independent zeta expansions | `a=1` reduces to `(1-z)^(-p)`; extension fields have nontrivial cycles |
| Reverse-depth tails stabilize exactly along `n_L=floor(alpha p^L)` | Theorem 6.1, nested-floor identity | 33 rational `(p,a,alpha)` lanes through `L=9` | Statement is for fixed `k` once `L>=k-1`; `1<=alpha<p` |
| Phase size and the full fixed sequence recover `(p,a,n)` | Theorem 7.1, first count / first maximum / phase exponent | Each exhaustive lane reconstructs its input triple | Covers `a=1` and `n=0`; no unspecified finite-prefix claim is made |

## Two-route assertion

Route I reasons pointwise on `p`-adic coefficient chains and establishes the
iterate before the structural coordinate change. Route II then uses that
iterate in an `F_p`-linear factorization and complementarily recounts affine
kernel cosets and the CDF. Fixed subfields and divisor inversion handle the
periodic data. Agreement is an internal consistency check, not a novelty
assertion or a claim of logically independent derivation.

## Owner and collision firewall

- Bridy’s `Lambda_i` formula owns the direct coefficient-selector convention.
- Cartier’s construction owns the historical operator family.
- Jeong’s power-series Cartier families are a close direct operator neighbor.
- Finite-field Frobenius and subfields are standard and explicitly cited.
- After restriction of scalars, this is a classical finite `F_p`-linear
  system. Elspas, Wang, Hernández Toledo, Panario--Reis, and Reis own the
  generic state-diagram, cyclic--nilpotent, component, and attached-tree line.
- Rank/kernel counts, generic product decomposition, and functional-graph
  machinery are assigned zero novelty and priority credit.
- P100, P103, P107, and P109 have different phase spaces and updates; P109’s
  nilpotent-image rank machinery is the closest internal proof-engine risk.
  P115’s residual scope is only the exact bounded Cartier specialization,
  including its closed coefficient/component formulas, together with the
  lattice and recovery conjunction.

A bounded owner check cannot establish absence. Specialist review is still
required before external use.
