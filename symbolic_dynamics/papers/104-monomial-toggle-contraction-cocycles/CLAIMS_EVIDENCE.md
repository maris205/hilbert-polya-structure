# Claims–Evidence Map

Status: initial author package; external release **HOLD**. Independent
cross-hostile review and final mechanical freeze remain pending.

| Claim | Proof anchor | Independent exact control | Residual risk |
|---|---|---|---|
| Every left product has the orientation/occupation normal form | Theorem 2.1 and the two left-multiplication identities | Literal rational matrix multiplication for 122,865 words versus an independently recorded orientation and occupation count | A reversed composition convention changes the induction; the first-word sentinel and explicit left-product definition fix it |
| The determinant, two singular values, and condition number are exact finite-word functions of `J_n,Z_n` | Corollary 2.2 | Literal determinant and literal Gram matrix are checked independently of the asserted normal matrix | `0<a<1` is essential for ordering the two singular values; `a=0,1` is excluded |
| Quenched exponents are `(0,log a)` at `q=0` and double `(log a)/2` for `0<q<=1` | Theorem 3.1 | Exact endpoint paths, occupation distributions, and finite singular moments | `q=1` is periodic, not covered by the interior ergodic-chain argument; it is proved separately |
| For `0<q<1`, `Z_n/sqrt(n)` has variance `(1-q)/q` and a Gaussian limit | Theorem 3.2; bounded martingale decomposition | Exact conditional martingale mean/variance and exact first/second occupation moments through time 80 | The finite control verifies the algebra, not the CLT; the infinite limit uses the cited martingale CLT |
| Centered log singular values and log condition number have the stated folded-normal limits | Corollary 2.2 plus Theorem 3.2 and the continuous mapping theorem | Exact finite-time Gram spectrum and signed-occupation laws | Folded limits are asserted only in the open interval `0<q<1` |
| Signed occupation transforms equal `e_+^T K_theta^n 1` and satisfy the displayed recurrence | Signed-transform and recurrence displays in Section 4 | 61,425 literal weighted words versus separately coded transfer matrices; 375 Cayley–Hamilton recurrence steps | The verifier uses rational surrogates for `exp(theta)`; the symbolic proof covers every positive real value |
| The annealed order-`s` exponent is the logarithm of the explicit larger root | Theorem 4.1 and the absolute-transform squeeze | Positive/negative signed transforms, absolute DP, trace/determinant recurrence, and endpoint lanes | “Annealed exponent” is defined explicitly without division by `s`; alternative conventions differ by that factor |
| The annealed/quenched gap is strict for `0<q<1` and closes at `q=0,1` | Characteristic polynomial evaluated at one; direct endpoint paths | Exact strict-root sign sentinels and 162 endpoint-time checks | Strictness depends on `s>0` and `0<a<1` |

The program is a finite falsification control and does not replace any
asymptotic proof. Bibliographic search absence is not used as evidence.

## Assumption and convention firewall

- `0<a<1`; singular matrices (`a=0`) and the isometric degeneration
  (`a=1`) are outside the theorem statements.
- Products are `M_n=A_n...A_1`; `A_1` acts first.
- `U_n` counts the orientation before updates, over `0<=t<n`.
- The folded CLT and strict interior gap use `0<q<1`.
- The deterministic endpoints `q=0,1` are computed directly and are not
  obtained by silently extending the interior proof.
- `Gamma_s=lim n^(-1) log E||M_n||^s`; no factor `1/s` is implicit.

## Internal collision firewall

- **P91:** generalized-dihedral reverser shifts, periodic points, zeta data,
  and recovery. P104 is an invertible random linear cocycle with fixed
  determinant magnitude and singular-value pressure. No shift or reverser
  dynamical system is constructed. The shared coordinate involution remains
  a disclosed medium collision risk.
- **P93:** noninvertible push–pop stack cocycles, reflected maxima, fiber
  loss, and two thresholds. P104 has no stack, boundary reflection, or fiber
  loss; every generator is invertible.

## Owner subtraction

The manuscript subtracts general random-product laws
(Furstenberg–Kesten), generalized Lyapunov/transfer methods (Texier), and
the martingale CLT (Brown). The residual exact specialization remains on
HOLD until a specialist direct-owner search is complete.
