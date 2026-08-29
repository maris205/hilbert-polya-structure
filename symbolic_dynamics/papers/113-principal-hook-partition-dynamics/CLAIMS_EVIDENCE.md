# Claims–evidence ledger

Status: internal evidence ledger. External dissemination, novelty, and
priority remain **HOLD**.

| ID | Claim | Symbolic evidence | Exact control | Ownership / risk |
|---|---|---|---|---|
| C0 | `H(lambda)` is the standard principal-hook partition of the same weight, with adjacent gaps at least two. | `main.tex`, Section 2: principal hooks partition the Ferrers diagram; strict Frobenius arms and legs. | Independent Ferrers and Frobenius implementations agree for every partition through `n=40`; weight, Durfee length, and gap checks. | **Zero credit.** Gutschwager owns the map object; Andrews/Chern--Yee cover standard diagonal-hook setup. |
| C1 | The one-step image is exactly the gap-at-least-two partitions. | Proposition 2.1, Frobenius reconstruction. | Observed image set equals the formula set in every lane `1<=n<=40`. | **Direct owner result; zero credit.** Goupil (2009). |
| C2 | The fibre over `h` has weight `h_r product(gap-1)`. | Proposition 2.1: independent bottom split and increment splits. | Direct fibre census and a separate Frobenius dynamic-programming count both equal the product for every target through `n=40`. | **Direct owner result; zero credit.** Goupil (2009). |
| C3 | `(H lambda)_1=lambda_1+ell(lambda)-1`; hence `(n)` is globally absorbing and is the unique fixed/periodic point. | Corollary 3.1: owned first-row/column identity plus strict finite-state growth. “Globally absorbing” is explicitly defined as finite-time capture of every state. | First-part identity, direct orbit termination, cycle guard, and depth agreement for all enumerated states. | Identity directly owned by Gutschwager, **zero credit**; dynamical deduction explicitly **low credit**; external status HOLD. |
| C4 | For Durfee size at least two, the exact gap increment is `ell-lambda'_2+2=2+m_1`. | Main Theorem 3.2(i): subtract explicit `h_1,h_2`. | Both equalities and increment lower bound checked state-by-state through `n=40`. | **Main-contract component.** Bounded owner search not cleared for external claim. |
| C5 | For Durfee size one off the absorbing state, `(a,1^b)` maps to `(n)` with increment `b+1`. | Main Theorem 3.2(ii): the sole diagonal hook is the whole diagram. | Shape, image, exact increment, and lower bound checked exhaustively. | **Main-contract component.** External status HOLD. |
| C6 | `tau(lambda)<=floor((n-g(lambda))/2)<=floor(n/2)`. | Main Theorem 3.2: telescope gains of at least two to terminal gap `n`. | Pointwise and global inequalities checked on all `215,307` states across `n<=40`. | **Main-contract consequence.** External status HOLD. |
| C7 | The maximum depth is `floor(n/2)`, attained by the balanced two-row path. | Main Theorem 3.2: for `n>=2`, `b-1` two-row updates followed by `(n-1,1)->(n)`, for `b` total steps; `(1)` is terminal at `n=1`. | Exact path, witness depth, and maximum of every lane checked through `n=40`. | **Main-contract sharpness.** External status HOLD. |
| C8 | `A_0=1`, `A_1=n-1`, and later layers obey a weighted transport identity. | Corollary 4.1: disjoint first-image fibres and C2; explicitly not closed in `A_t(n)` alone. | Full depth histograms and every nonempty/empty transport lane checked through `n=40`. | **Low credit.** State-weighted use of Goupil's zero-credit weights. |
| C9 | `H(lambda)=H(lambda')`; positive-time orbits agree; depths differ only for `(n),(1^n)`. | Corollary 4.2: conjugation swaps Frobenius arms and legs; terminal exception isolated. | Image equality, positive-time iterates, conjugation involution, and exact exception checked exhaustively. | One-step symmetry **zero credit**; timing exception **low credit**. Chern--Yee is direct diagonal-hook context, not inflated into a temporal owner. |
| C10 | For each fixed `n`, `#Fix(H_n^m)=1` and `zeta_{H_n}=(1-z)^(-1)`. | Corollary 4.3: C3 excludes nontrivial periodic points; formal exponential identity; all-weights zeta explicitly excluded. | Fixed counts through iterate 8 and zeta coefficients through degree 8 checked in every lane. | **Low-credit automatic consequence** of C3; no independent novelty claim. |
| C11 | `n=1,n=2`, empty products, and empty layer sums behave as stated. | Remark 3.3 and conventions in Proposition 2.1 and Corollary 4.1. | Dedicated exact assertions for both small state spaces. | Boundary control. |

## Proof-route separation

- **Route A, Frobenius/fibre:** C0–C2 and one-step conjugation in C9; all are
  zero-credit inputs.
- **Route B, Ferrers/gap:** C4–C7 form the sole main theorem. C3 and C10 are
  low-credit consequences of an owned identity.
- **Bridge:** C8 uses Route A's owned fibre weights over Route B's temporal
  layers and remains a nonclosed, low-credit transport identity.

## Owner-search boundary

The primary-source audit identifies Gutschwager, Goupil, and Chern--Yee by
claim, but does not clear the temporal claims. No exact iterated owner was
located in the bounded search. That absence is not novelty, priority, or
freedom-to-disseminate evidence; external status remains **HOLD**.

## P110 firewall

| Axis | P113 | P110 | Collision decision |
|---|---|---|---|
| States | Unlabelled integer partitions of weight `n` | Labelled set partitions of a cyclic ground set | Distinct |
| Update | Regroup Ferrers cells by principal diagonal hooks | Join a set partition with its cyclic shift | Distinct |
| Progress mechanism | First part and first adjacent gap | Cyclic/lattice closure data | Distinct |
| Counting input | Frobenius hook fibres | Bell/Möbius lattice basins | Distinct |

Shared words such as “partition”, “depth”, and “zeta” carry no theorem credit.
