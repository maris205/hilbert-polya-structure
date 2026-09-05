# Independent internal admission review: finite-real Boole stability

Review date: 2026-09-05. Reviewer: a separate current-team agent, not the
author of the reviewed proof. This is an independent internal mathematical
review, not human peer review, an external-model review, a formal Route-A
evaluation, a publication-novelty certificate, or a completed paper.

## Decision

Mathematical status: **PROVABLE AS STATED** for the five-part source-system
contract in the reviewed proof. I found no false quantified assertion,
missing substantial lemma, or counterexample to that contract. The original
parameter range, physical domain, clock and determinant convention survive.

Admission recommendation: retain this as **one coherent source-system
candidate**, centered on the finite-real weighted divisor and its parabolic
collision/compensation law. Before paper-level freeze, make the ownership
amendment R1 below. Do not count the phase picture, deleted-prepole domain,
unweighted census, full-circle spectrum, or individual exceptional parameters
as independent papers. This review does not itself complete any paper or
establish publication originality.

## Inputs and what was actually inspected

I read all 593 lines of `boole/PROOF_PACKAGE.md`, all 152 lines of
`boole/SOURCE_AUDIT.md`, all 127 lines of `boole/exact_check.py`, the entire
saved JSON receipt and reproducibility note, and all 203 lines of the closest
completed C380 proof. I also read the repository and Hénon guidance, current
state, the relevant batch workflow, and the full `proof-writer` skill. That
skill's feasibility, assumption and quantifier audit determined the review
structure; it did not authorize changing the author's proof.

Input SHA256 values, measured before this review file was written:

| Input | SHA256 |
|---|---|
| `boole/PROOF_PACKAGE.md` | `9ef4c0d8e3beab75e95be19d5a835e4b491392ce1565589997fa213f0296f725` |
| `boole/SOURCE_AUDIT.md` | `7ae457ff174a2a0ff41f3c04c3ed357347d72a375da28a5be02e1b62cef5700e` |
| `boole/exact_check.py` | `9c4a7dd0af9c2afc90fc4294d29ee998e1214d4e40ef64f9545c9594cbf35c2b` |
| `boole/EXACT_CHECK_OUTPUT.json` | `b8e6edc086cb15f5b2afebfdd986d78b2525dd7d8a0954b3f37c661c29ce26d8` |
| `boole/REPRODUCIBILITY.md` | `8c3b83f30faf99727c261962ecb834f9023e8ab2cc759c60588580628151d173` |
| C380 `proof/ANALYTIC_PROOF.md` | `1729cbc5c273ca82322867c52c49f0d87dd1483a4138bf7f50464d079c50d2d5` |

The mathematical assessment below comes from checking the arguments and
independently deriving decisive identities. I did not run the author's
checker and relabel its output an independent proof. I did run the separate
small symbolic audit described below. No proof, source, code, evaluator,
registry, manuscript, release artifact or Git state was modified by me.

## Assumptions and dependency audit

The theorem is about real $a,b>0$, with original iteration time and physical
state space $X=\mathbb R\setminus\bigcup_{j\ge0}T^{-j}\{0\}$. Fixed-point
weights are $((T^n)'(x)-1)^{-1}$, not inverse multipliers and not signed
complex fixed-point indices. The defining exponential is first a normalized
germ at zero. These restrictions are used correctly throughout.

The proof dependency chain is sound: domain and half-plane localization
give the complete simple physical fixed-point set; the projective degree
and infinity jet give its census and index; the index gives all-iterate
weights; absolute convergence gives the primitive product and explicit
continuation; divisor arithmetic and uniform coefficient bounds give the
exceptional parameters and critical limits. No operator trace identity is
used to infer the finite-real sums.

### 1. Domain, phases and every fixed-point count

The deletion is genuinely forward invariant. If an image hit a prepole,
the original point would already be a prepole. A finite periodic orbit
cannot hit zero, since the next state would be the fixed point at infinity.
Conversely, deleting prepoles removes no finite periodic point. In the
subcritical circle chart only one periodic orbit is deleted: the point
corresponding to infinity. Its nonperiodic inverse images do not create
extra primitive factors.

The inverse-Jacobian identity is valid on both monotone branches and for
measurable sets, including infinite measure. The Cauchy density follows
from the disk-fixed-zero circle map and pulls back with the stated scale.
For $a>1$, the two separated inverse intervals lie inside $[-r,r]$, their
uniform contractions give a genuine one-sided full shift, and exterior
monotone escape excludes additional periodic points. The survival identity
is exact for the stated initial Lebesgue ensemble. None of these arguments
proves or requires a new mixing or ergodicity theorem.

For $a<1$, strict disk contraction and reflection leave exactly the two
nonreal fixed points, while angular expansion certifies simplicity of all
circle cycles. For $a\ge1$, increasing absolute imaginary part rules out
every nonreal finite cycle and every real derivative exceeds one. This
avoids the invalid inference that degree counting alone counts distinct
real roots. Infinity has multiplicity one off criticality and three at
criticality, giving $N_n=2^n-2$ for $a\le1$ and $N_n=2^n$ for $a>1$.
The $n=1$ zero count on the lower side, $q=0$ at $a=1/2$, and all positive
$b$ are handled. Möbius inversion and the unweighted zeta then follow.

### 2. All-period critical residue

I independently recomputed the infinity coordinate correction:
$$
\frac{dz}{z-F(z)}=
\left(\frac1{w-g(w)}-\frac1w\right)dw,
\qquad g(w)=\frac1{F(1/w)}.
$$
Thus the sphere residue sum uses $I_\infty-1$, not $I_\infty$ as the
residue at infinity. For the critical odd jet, composing
$w+bw^3+b^2w^5+O(w^7)$ adds $b$ to the cubic coefficient and
$3bA_n+b^2$ to the quintic coefficient. Summing gives
$$
A_n=nb,\qquad B_n=\frac{n(3n-1)}2b^2,
\qquad I_\infty=\frac{B_n}{A_n^2}=\frac{3n-1}{2n}.
$$
This verifies the result for every positive integer $n$, rather than by
extrapolating six symbolic jets. Multiplicity three, multiplier one and
this index are distinct quantities. Subtracting the two nonreal weights
only when $a<1$ gives exactly equation (16), with the correct signs.

### 3. Primitive product, divisor and entire exceptions

Positive physical multipliers and the bounded all-iterate weights make
the absolute logarithmic sum finite on $|u|<1$. This justifies the two
regroupings by primitive orbit and multiplier power. The separate geometric
products are entire by local uniform absolute convergence; their tails are
nonzero away from the listed factors. Hence the quotient cannot hide
unlisted zeros or cancellations.

At the first possible denominator point $u=a^{-1}$, cancellation requires
$a=q^j$. Positive $q$ has $q<a$, making that impossible. Negative $q$
forces $j=2m$ and therefore $a=(1-2a)^{2m}$. At precisely those parameters,
every denominator factor is the numerator factor indexed by $2mk$; its
remaining multiplicity is one. This proves necessity and sufficiency,
not only a sufficient family. Strict monotonicity proves a unique root
for each $m$, and distinct powers show different roots cannot coincide.
The stated rational-log index pairs and all residual multiplicities are
correct, including negative zeros and the $q=0$ case.

The abstract diagonal operators at resonant and supercritical parameters
are indeed self-adjoint and trace class. Their construction after the
product calculation supplies no natural physical transfer realization.
The explicit nonclaim is essential and must survive the manuscript.

### 4. Critical boundary and two-sided compensation

The logarithmic derivative has limiting residue $1/2$ at the positive
unit boundary. A meromorphic germ would have an integer residue there;
this proves the asserted obstruction at $u=1$. It does not give a natural
boundary along the whole circle. The proof explicitly avoids that stronger
false inference.

On the lower side, convexity gives nonnegative coefficients, and
$q\le a^2$ gives the bound $\tau_n\le(1+a^n)^{-1}\le1$ uniformly near
criticality. On the upper side, division by the complete factors of the
two fixed primitives subtracts $2/(q^n-1)$ at every iterate, not only
at $n=1$. The same inequality gives
$0\le\tau_n^{\rm red}\le(1+a^n)^{-1}\le1/2$.
Together with the fixed-$n$ expansions these bounds justify the compact-disk
uniform limit of the logarithms and their exponentials. I found no
interchanged-limit gap. The unreduced upper determinant instead tends to
zero at every real $0<u<1$ while remaining one at zero, so it cannot have
the claimed locally uniform critical limit without compensation.

These checks concern the stated open disk only. No limit uniform at
$u=1$, spectral convergence of an unspecified operator, or whole-plane
limit has been established or is needed.

## Executable evidence inspected and independent finite check

The saved receipt's script hash matches the actual script. Its four counts
sum to 139; the script's quotient-ring/partial-fraction identity is correct
when the checked fixed polynomial is squarefree. This supports the stated
finite cases, not the all-parameter theorem. Receipt hashing is only
integrity evidence. I did not independently witness its earlier execution.

My separate read-only SymPy 1.14.0 command completed with exit status zero.
It verified the receipt hash/count arithmetic and, independently of the
author's iterate-polynomial method, used the explicit two-cycle
$x_\pm=\pm\sqrt{b/(a+1)}$. Its multiplier is $(2a+1)^2$, so its entire
two-point contribution is
$$
\frac{2}{(2a+1)^2-1}=\frac1{2a(a+1)}.
$$
The symbolic audit checked that this equals the subcritical $n=2$ formula
for all $a$, and that adding the two supercritical fixed-point repetition
weights gives $1/(a^2-1)$. It also checked the critical value $1/4$ and
the logarithmic-derivative residue $1/2$. Its actual stdout was:

```json
{"author_checker_rerun": false, "receipt_check_count": 139, "receipt_integrity_matches": true, "reviewer_origin_exact_checks": "PASS", "sympy": "1.14.0"}
```

This is a small independent consistency lane, not a proof of all periods,
the divisor classification, or uniformity. Those were checked analytically
above. No additional numerical census is needed to address an identified
mathematical failure in the present inputs.

## Primary ownership checks and required amendment

I opened and inspected the relevant primary passages, not just search
snippets. Umeno–Okubo's introduction and equations (2)–(3) already give
this family and the invariant Cauchy law; its abstract states the three
statistical phases. These receive no novelty credit here.
[Primary author version](https://arxiv.org/html/1510.08569v3).

Bandtlow–Just–Slipantschuk Theorem 5.4 and Remarks 5.5–5.7 own the
full-circle spectral/determinant mechanism and disclose earlier ancestry.
C380 specializes the negative-$q$ case; changing to positive $q$ does not
escape the wider prior theorem.
[Primary journal PDF](https://www.numdam.org/item/AIHPC_2017__34_1_31_0.pdf).

**R1 — strengthen ownership before paper freeze.** Mendoza–Ruiz already
defines $R_f=\mathbb R\setminus\bigcup_{n\ge0}f^{-n}(0)$ in §3. Lemma 3.1
and Theorem 4.5 own exterior escape and the supercritical binary Cantor
system. More importantly than the current audit records, Theorems 4.2
and 4.4 give the critical and $1/2<a<1$ conjugacies to the binary shift
with eventually constant sequences removed. Its periodic sequences are
all binary periodic sequences except the two constants, so $2^n-2$ is
an immediate prior corollary in those regimes. Cite these additional
locators; do not present the physical-domain definition or those counts
as the independent increment. This is an attribution repair, not a change
to the proof or a finding that the weighted theorem is already there.
[Primary publisher PDF](https://revistas.utm.edu.ec/index.php/Basedelaciencia/article/download/4408/7355/27220).

My directed searches used `"Boole" "determinant" periodic`,
`"Boole" "dilogarithm" dynamics`, `"ax-b/x" zeta`,
`"Boole transformation" "zeta"`, `"Boole map" "Fredholm"`,
`"Boole map" "periodic" "determinant"`, and
`"x-1/x" "dynamical" "zeta"`. They did not yield a direct matching
weighted-resonance/compensated-limit theorem. Much returned material was
irrelevant Boolean algebra or numerical integration. This is a bounded
no-match observation only; I did not audit every older rational-map
normal form, book, thesis or citation graph. I did not independently
recheck every bibliographic entry in the author's source audit.

## Minor presentation action and retained limits

**R2 — optional precision.** Replace the introductory phrase “All iterates
... are determined” with “All-iterate fixed-point counts ... are
determined.” The proof determines the census and weighted sums for every
iterate; it does not purport to list every point in closed radical form.
This wording improvement does not require weakening any displayed theorem.

After R1, the remaining substantive candidate increment is the integrated
weighted finite-real continuation, exceptional entire classification and
two-sided parabolic compensation law, with correct ownership of infinity.
That is a defensible single source-system contract beyond the old C380
full-circle calculation. Its literature significance remains search-bounded;
the main author/coordinator should reassess admission if a prior matching
theorem is found.

There is no natural finite-real trace-class transfer theorem, intrinsic
prime labeling, target zero/divisor correspondence, Euler factor, root
number, automorphy or Hilbert–Pólya result. The exploratory ceiling stays
$A0\_FAIL$, $A1\_WEAK$, $A2\_FAIL$, $A3\_FAIL$, $A4\_FORMAL\_HINT$;
all target and Route-B flags remain false. This report neither runs nor
modifies the evaluator and grants no additional authority. Review findings
apply to the hashes above; later mathematical changes require checking
their affected reasoning, not automatically repeating every lane.
