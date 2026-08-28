# P92 Claims–Evidence Ledger

Status: internal theorem freeze **GO**; external release **HOLD**.

| Claim | Quantifiers | Proof anchor in `main.tex` | Exact control | Residual risk |
|---|---|---|---|---|
| State/skew-product normal form | Every prime power `q>=2`, every `r>=2`, every primitive companion `C` | Proposition 2.2; invertibility gives both past and future, and the overlap coordinates prove conjugacy | Full state matrices are built in every lane; row and column sums are checked | None inside the stated primitive-companion family |
| Fourier action | Same quantifiers | Lemma 3.1 computes `A chi_xi = w(xi_r) chi_(C^T xi)` with `w(0)=q-1`, `w(a)=-1` otherwise and records nondegeneracy of the character pairing | The transpose orbit, coordinate weights, and resulting full characteristic polynomial are checked | Requires a nontrivial additive character, which exists for every finite field |
| Two-factor characteristic polynomial | Same quantifiers | Theorem 3.2; zero frequency is one scalar block, while all nonzero frequencies form one Singer orbit with `H=q^(r-1)-1` hyperplane hits | Faddeev–LeVerrier computes the full integer characteristic polynomial of each actual adjacency matrix | The theorem does not extend unchanged to nonprimitive `C` or arbitrary error sets |
| All fixed counts | Same quantifiers, every `n>=1` | Theorem 4.1 takes power sums of the two Fourier factors | Direct matrix traces are checked for every `1<=n<=L+1` in each lane | None within scope |
| Zeta function and least-period orbits | Same quantifiers | Theorem 4.1 sums the trace logarithm and applies Möbius inversion | The determinant polynomial and all tested traces independently force the recorded rational zeta factors | Bowen–Lanford rationality itself is prior art and is not claimed |
| First-anomaly recovery of `(q,r)` | Same quantifiers | Corollary 4.2 proves `F_1=q-1` and first positive `F_n-F_1^n` at `n=q^r-1` | Every lane checks the first anomaly and reconstructs the parameters | Recovers `(q,r)`, not the particular primitive polynomial `C` |
| Mixing, entropy, and unique uniform MME | `q>=3`, `r>=2`, primitive `C` | Theorem 5.1 uses double regularity, a simple Perron root, spectral separation, and period one; then applies the Parry construction | Forward/reverse reachability and graph period one are checked in four positive lanes | The `q>=3` restriction is essential |
| Binary boundary | `q=2`, `r>=2`, primitive `C` | Proposition 5.2 translates the affine state permutation to `C`, yielding a fixed orbit and one orbit of length `2^r-1` | `(q,r)=(2,2)` is a negative mixing control and verifies all algebraic formulas | Only one binary rank is enumerated, while the proof covers every `r>=2` |

## Ownership subtraction

- Ghorpade–Hasan–Kumari provide the cited primitive-polynomial/Singer-cycle background.
- Chang–Ezerman–Ling–Wang provide the cited deterministic LFSR cycle structure, including
  arbitrary characteristic polynomials.
- Bowen–Lanford provide the cited finite-type zeta determinant framework.
- Parry provides the cited intrinsic maximal-entropy Markov measure construction.
- P92 does **not** claim any of those objects or frameworks.  Its residual
  contribution is the nonzero-discrepancy SFT and the exact weighted Singer
  Fourier block it produces.

The source search is bounded, so literature and priority clearance remains **HOLD** rather than
an absolute novelty certification.
