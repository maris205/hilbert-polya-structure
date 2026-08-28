# Claims–Evidence Map

| Claim | Proof location | Independent control |
|---|---|---|
| The chronological cocycle is `Phi_n=omega_n o ... o omega_1` on the one-sided full shift | Section 2, equations labelled `environment-law`, `cocycle`, and `walk` | Direct symbolic-tail composition for every labelled word over `{D,C_0,C_1}` through time 9 |
| Every finite cocycle has a unique form `C_u D^J` | Theorem 2.1, induction using `D C_a=Id` | Definition-level labelled-map comparison; the control does not evaluate the theorem formula on a precomputed map table |
| `J_n=M_n` and `I_n=M_n-S_n` exactly | Theorem 2.1 | Every one of the 65,535 direction words through time 15, with three integer identities per word |
| The image is `[u_n]`, its diameter is `b^(-I_n)`, and every image point has `b^(J_n)` preimages | Theorem 2.1 | Exhaustive finite-input image and multiplicity census through `(b,n)=(2,10)` and `(3,7)` |
| Quenched fibre and contraction rates are `(2p-1)_+ log b` and `(1-2p)_+ log b` | Theorem 3.1 | Strong law plus the pathwise normal form; finite enumeration is not presented as proof of an almost-sure limit |
| Uniform synchronization holds iff `p<1/2` | Theorem 3.1 | Linear growth of `I_n` below the boundary; infinitely many `I_n=0` record times at and above it |
| At `p=1/2`, `J_n/sqrt(n)` and `I_n/sqrt(n)` converge to `|N(0,1)|`, with means asymptotic to `sqrt(2n/pi)` | Proposition 3.2 | Exact equality of the finite-time `I_n` and `J_n` histograms through time 40; Donsker, reflection, and uniform integrability prove the limit |
| The finite annealed moment has the displayed ballot first-passage sum | Section 4, equations labelled `first-passage-decomposition` and `ballot` | Direct rational propagation equals the ballot sum for `b=2,3,5`, five interior rational `p` values through `n=18`, and both endpoints through `n=20` |
| Below `p=1/(b+1)`, `A_n -> (1-r)/(1-br)` | Theorem 4.1(i) | Exact threshold and geometric-series algebra; gambler's-ruin hitting probabilities supply the proof |
| At `p=1/(b+1)`, `A_n=1+((b-1)/b) E_hat[M_n]` and has the stated linear coefficient | Theorem 4.1(ii) | Exact rational change-of-measure identity through time 40 for `b=2,3,5`; coefficient algebra checked separately |
| Above `p=1/(b+1)`, `A_n/lambda^n -> (1-rho)/(1-b rho)` | Theorem 4.1(iii) | Exact tilted-moment identity through time 35 for six rational `(b,p)` pairs; stationary prefactor algebra checked in `Fraction` |
| The endpoint laws are `A_n(0)=1` and `A_n(1)=b^n` | Theorem 4.1, direct endpoint argument | 252 exact comparisons across `b=2,3,5`, `p=0,1`, and `0<=n<=20`, including both the ballot expansion and the closed endpoint law |
| `g_a(p)=log max{1,bp+(1-p)/b}` | Theorem 4.1 | Consequence of the three proved asymptotic regimes; finite controls check identities, not the limiting implication |
| `g_a>g_q` for `1/(b+1)<p<1` | Corollary 4.2 | Positivity in the intermediate regime and strict Jensen above `1/2`; no decimal inequality is used as proof |
| At `p=1/2`, the annealed prefactor is `(b+1)/b` | Corollary 4.3 | Exact substitution `rho=b^(-2)` plus rescaled diagnostics for `b=2` |
| P93 is not a random SFT, reset renewal, or hidden-output process | Section 5 and `README.md` | Object/proof-engine firewall against P79, P86, and P89; this is a scope distinction, not a novelty theorem |
| Owner and release scope | Introduction and Section 5 | DOI-verified bibliography for the main owner families; external release remains HOLD |

The program is a regression control.  It does not replace the strong law,
Donsker theorem, gambler's-ruin limit, ergodic convergence of the reflected
chain, uniform-integrability step, or strict Jensen argument.
