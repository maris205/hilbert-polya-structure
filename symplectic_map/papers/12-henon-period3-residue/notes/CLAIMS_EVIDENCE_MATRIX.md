# Claims--Evidence Matrix

## Frozen status

- Candidate: henon_period3_residue_v1
- Decision: GO_BORDERLINE_STANDALONE_SPECIALIST_NOTE
- Dominant contribution: sharp quartic full-fiber theorem and minimal
  period-three separator
- Supporting contribution: uniform all-\(m\) two-term residue law and exact
  slope certificate
- Evidence state: proof package complete at SHA-256
  `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`;
  source-lock v2 frozen after bounded R1 repair; fresh independent v2 review
  pending
- Forbidden state: no code, registered run, result, figure, or manuscript
- Required later scientific certificate:
  HENON_PERIOD3_RESIDUE_LAW_CERTIFIED /
  QUARTIC_MINIMAL_SEPARATOR_CERTIFIED /
  UNIVERSAL_NONVANISHING_OPEN

## Claim matrix

`PROVED_*` below means proved in the bound author proof package. It does not
mean `SOURCE_LOCK_PASS`, registered certification, or manuscript approval.

| ID | Frozen claim | Proof evidence | Closest collision | Later exact audit | Status / boundary |
|---|---|---|---|---|---|
| C1 | The project works in the normalized monic-centered Jacobian-minus-one Henon category over characteristic zero | explicit definitions and normal-form theorem | Friedland--Milnor | schema/category assertion only | ASSUMPTION_LOCK |
| C2 | On the length-\(2m\) fixed scheme, \(q=p'\) is nilpotent with \(q^2=0\), so the multiplication spectrum of the trace is \(0^{\times2m}\) | quotient by \((x^m-a)^2\) | Cantat--Dujardin quartic instance | exact quotient-ring check on frozen cases | PROVED_SCHEME_THEORETIC |
| C3 | The exact formal period-two trace multiset is \(2^{\times((2m)^2-2m)}\) | product fixed scheme; \(2+q(x)q(y)\) has nilpotent correction; diagonal subtraction | Cantat--Dujardin quartic instance | independent exact quotient and direct matrix engines | PROVED_SCHEME_THEORETIC |
| C4 | Within normalized moduli, \(f_{m,a}\sim f_{m,b}\) iff \(a^{2m-1}=b^{2m-1}\) | normalized conjugacy/root-of-unity action and converse | Friedland--Milnor; Cantat--Dujardin normal forms | symbolic forward/reverse action checks | PROVED_NORMALIZED_ONLY |
| C5 | The three cyclic equations at \(\varepsilon=1\) encode \(\operatorname{Fix}(f^3)\), and their Jacobian determinant is \(q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2)\) | direct recurrence and determinant calculation | low-period generalized-Henon calculations | independent determinant and iterate engines | PROVED |
| C6 | The cyclic quotient is monic free of rank \((2m)^3\) over the parameter ring | leading monomials \(x_i^{2m}\); division basis | complete-intersection algebra | basis-count and monicity gates | PROVED |
| C7 | \(S_m=\operatorname{Tr}(t_\varepsilon^m)=\operatorname{Res}(t_\varepsilon^{m+1})\) | complete-intersection trace/residue theorem with Jacobian \(t_\varepsilon\) | Cattani--Dickenstein--Sturmfels | finite engine agreement only; theorem remains proof-derived | PROVED_PRIOR_METHOD_SPECIALIZATION |
| C8 | Weighted homogeneity initially permits exactly four monomials in \(S_m(a,\varepsilon)\) | weight equation and invariant exponent \(2m-1\) | weighted residue machinery | exact symbolic weight enumerator | PROVED |
| C9 | The coefficient of \(a^{3(2m-1)}\) is zero | separated \(\varepsilon=0\) algebra and \(q_i^2=0\) | elementary local algebra | structural nilpotence gate | PROVED |
| C10 | The coefficient of \(a^{2(2m-1)}\varepsilon^m\) is zero | Step 7 treats all three Puiseux root-pattern branches and proves local trace order strictly greater than \(m\); Step 10 closes the exact diagonal branch | no direct Henon collision located; local degeneration methods mature | no finite interpolation accepted; proof-contract gate only | PROVED_LOCAL_DEGENERATION_IN_BOUND_PROOF / SOURCE_REVIEW_PENDING |
| C11 | \(S_m(a,\varepsilon)=C_m\varepsilon^{3m}+D_ma^{2m-1}\varepsilon^{2m}\) | C7--C10 | no direct source found | exact finite cases are falsification checks only | PROVED_UNIFORM_LAW |
| C12 | \(C_m=0\) for odd \(m\) | cyclic-coordinate reversal and parity | symmetry consequence | sign/reversal regression | PROVED_COROLLARY |
| C13 | The frozen nested-binomial expression equals \(D_m\) for every \(m\ge2\) | Step 9: terminating recurrence, order-independent Laurent/admissible-tuple sum, local binomial identity (9.14), distinguished-coordinate/transfer-flow classification, and separate \(j=0\) flow | residue algorithms are prior; exact Henon formula not found | two structurally independent integer evaluators on a preregistered finite tuple | PROVED_EXACT_CERTIFICATE_IN_BOUND_PROOF / SOURCE_REVIEW_PENDING |
| C14 | The formal fixed contribution to the \(m\)-th period-three trace moment is zero | on the fixed algebra \(q^2=0\); \(\operatorname{tr}Df^3=q^3+3q\); \(m\ge2\) | elementary | direct quotient remainder check | PROVED |
| C15 | Every normalized monic-centered quartic with formal fixed-point trace multiset \(0^4\) has \(p=(x^2-L)^2\) | trace-zero forces all roots multiple; root partition plus centering | Cantat--Dujardin gives the family, not this full-fiber classification | coefficient/root-multiplicity engine with adversarial quartics | PROVED_QUARTIC_FULL_FIBER |
| C16 | On the quartic fiber, \(S_2^{(3)}(L)=-1296000-1572864L^3\) | Step 12 gives a direct tensor-Laurent derivation independent of the all-\(m\) collapse; the \(m=2\) specialization of Step 9 is only a cross-check | no direct identity found | two independent exact engines must match every coefficient | PROVED_BY_INDEPENDENT_SOURCE_DERIVATIONS / SOURCE_REVIEW_PENDING |
| C17 | Exact-period-three pointwise length is 60 and cyclewise moment is \(-432000-524288L^3\) | Step 13: the transverse \((u,v)\)-Jacobian is invertible and the remaining equation has exactly the fixed-root multiplicity \(r\), so fixed support is not thickened; then \(4^3-4\), prime-period orbit size three, and C14 | formal dynatomic background | independently check fixed moment, local fixed multiplicity, exact length, and division | PROVED_WITH_LOCAL_FIXED_BRANCH_MULTIPLICITY / SOURCE_REVIEW_PENDING |
| C18 | Period three is the minimal conjugacy separator on the complete quartic fiber whose formal fixed-point trace multiset is \(0^4\) | C2--C4, C15--C17 and nonzero quartic slope | Cantat--Dujardin establishes only the period-one/two obstruction | positive identity plus negative controls | PROVED_SCOPED_MINIMALITY |
| O1 | \(D_m\ne0\) for every \(m\ge2\) | no degree-independent sign/nonvanishing proof | explicit new combinatorial question | finite checks cannot change status | OPEN_CONJECTURE_NONCLAIM |
| X1 | Period three globally separates all quartic Henon maps | no proof and outside fiber | stronger than any result here | forbidden | EXCLUDED |
| X2 | The project computes a global cutoff \(P(4)=3\) | no proof | Cantat--Dujardin cutoff is finite but ineffective | forbidden | EXCLUDED |
| X3 | Global residue or formal dynatomic machinery is new | false | direct mature prior art | forbidden | EXCLUDED |

## Exact formulas locked for C13

The implementation, if later authorized, must use these definitions without
post-result revision:

\[
H(r,k)=
\sum_{\substack{u+v=k\\2u\le r,\;2v\le r}}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v},
\]

\[
A_{m,r}=
\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
(-1)^{r+k}
\binom{m-1}{2(m-k)-1}H(r,k),
\]

\[
D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.
\]

No later code may replace this expression with an interpolating polynomial,
lookup table, or stored expected output.

## Proof versus audit boundary

| Claim class | What proves it | What computation may do | What computation may not do |
|---|---|---|---|
| All-\(m\) structural law C2--C14 | source-locked proof | check implementation on a frozen finite tuple; attack signs and multiplicities | promote finite agreement to universal proof |
| Quartic theorem C15--C18 | algebraic proof plus exact identity | independently reproduce coefficients, lengths, and fiber controls | replace the full-fiber or conjugacy proof |
| Universal nonvanishing O1 | future degree-independent proof only | report frozen diagnostic values if authorized | change OPEN to PROVED |
| Novelty | primary-source bounded search and independent review | preserve citations and roles | infer priority from no-hit search |

## Primary-source roles

| Source family | Allowed role | Forbidden inference |
|---|---|---|
| Cantat--Dujardin 2026 | direct quartic obstruction, period-one/two blindness, finite cutoff context | that Paper 12 discovers the family or low-period failure |
| Friedland--Milnor | normalized Henon form and conjugacy background | that normal forms are new |
| Cattani--Dickenstein--Sturmfels | global residue and quotient trace machinery | that Paper 12 invents multidimensional residues |
| Cvitanovic et al. | periodic-orbit contour sum rules and Henon precedent | that their weighted sum is the same raw trace moment |
| Dullin--Meiss | explicit generalized-Henon low-period calculations | that all period-three calculations are new |
| Huguin and Hutz | small-cycle multiplier and dynatomic/invariant background | direct plane-automorphism support beyond stated scope |
| Guillot--Ramirez and Ueda | fixed-point index/multiplier background | direct proof of C11--C18 |

## Registered audit requirements

If implementation is later authorized, the audit must:

1. contain two genuinely independent exact engines for C16;
2. contain two structurally independent finite evaluators for the C13 sum on
   the sole preregistered diagnostic tuple \(T_{\mathrm{reg}}=(8,9)\): Track Q
   evaluates the pre-collapse recurrence/Laurent admissible-tuple certificate,
   whereas Track R evaluates the collapsed \(H/A/D\) formula; they share no
   summation, generalized-binomial, or intermediate-record code;
3. recompute all expected quartic coefficients rather than loading them;
4. distinguish raw \(\operatorname{Fix}(f^3)\) from formal exact period three;
5. preserve nilpotent scheme structure instead of reducing to distinct roots;
6. verify the normalized conjugacy action and reject wrong exponent variants;
7. include adversarial sign, epsilon-power, fixed-subtraction, and cycle-division
   mutations;
8. carry an exact boolean that universal_nonvanishing_claimed is false;
9. use only \(T_{\mathrm{reg}}=(8,9)\), with no neighboring-index expansion;
   label it implementation falsification rather than a degree scan, and keep
   the disclosed source-stage \(m=2,\ldots,7\) recheck outside both engines;
10. give both scientific engines access only to a definitions-only schema,
    never the proof, plan, tracker, review, or acceptance ledger, and report
    exact zero counters for source-document, acceptance-ledger, historical
    value, and stored-\(D_8,D_9\) access;
11. bind a fresh independent proof-review authority; machine checks may audit
    local definitions and identities but may not self-certify the Puiseux or
    all-\(m\) proof;
12. run at most once after independent deployment authorization.

## Terminal wording lock

If and only if source, deployment, registered result, and independent integrity
gates all pass, the scientific result may say:

> The normalized exceptional family is blind to periods one and two. Its
> formal period-three \(m\)-th trace moment is affine in the exact quotient
> coordinate \(a^{2m-1}\), with an explicit finite slope certificate. In the
> complete quartic fiber whose formal fixed-point trace multiset is \(0^4\),
> that slope is nonzero and period
> three is the minimal conjugacy separator. Universal nonvanishing of the
> all-degree slope remains open.

No stronger terminal wording is authorized by this matrix.
