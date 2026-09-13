# Paper30 candidate brief: exact nonlinear quantum periodic trace modules

Date: 2026-09-06. Status: SAME_INPUT_PACKAGE_FOR_INDEPENDENT_CANDIDATE_REVIEW.
This is a selection-stage package, not a manuscript, source/publication lock,
accepted candidate, PDF or completed paper. Batch07 remains 3/5.
The geometric-point probe is a separate question and is **not** part of this
candidate. No results from that probe may be added to its capacity estimate.

## 1. Decision requested and unchanged gates

Two fresh independent reviewers receive this exact package. Each must assess
the complete contribution, its actual closest prior work, local noncollision,
proof confidence and natural substantive capacity. Neither reviewer may read
the other review or exchange conclusions before submitting their own report.

The existing conjunctive gates are unchanged: each report must independently
give novelty at least 7.5/10, research value at least 7.5/10, proof confidence
at least 9/10, and credible support for **22–30 substantive body pages**.
Both reports must pass all conditions; their best components cannot be mixed.
An estimate is not a PDF measurement or a theorem that a certain length is
impossible. A mathematical proof PASS does not imply a candidate PASS.

Format assumption: anonymous English single-column `article`, 11pt,
letterpaper, one-inch margins, normal line/theorem/display spacing.
References start on a separate page and do not count toward the body.
Background can be explained when necessary, but not expanded to reach the
minimum. Do not duplicate scalar and multiphase proofs, reproduce Paper29's
long estimates, add unrelated examples or turn every calculation into a
separate section. Paper29's one-time natural-draft capacity exception does
not extend to Paper30. No such exception is assumed here.

## 2. Frozen evidence and reading responsibilities

All paths below are relative to this directory. Root has fully read these
inputs. They remain unchanged during review.

| Input | Lines | SHA256 |
| --- | --- | --- |
| `PAPER30_QUANTUM_PERIOD_TRACE_PROBE_20260906.md` | 419 | `058cd7eaae3b5e1c19a2ca97a0beaafd7623fee9f67ff3a9e33d5117aaf95af2` |
| `PAPER30_QUANTUM_BRIDGE_INDEPENDENT_CHECK_20260906.md` | 487 | `8c44255e401eb4328b48169ca1a1ef9065f2897ad9a3e59a0f389be6db325573` |
| `PAPER30_QUANTUM_BRIDGE_PRIOR_CHECK_20260906.md` | 147 | `c83a09a5429361d3c002cca238b71bafec688fdcc145a61398dbc4a9a70fadf4` |
| `PAPER30_LITERATURE_LANDSCAPE_20260906.md` | 171 | `a57c482c2b036538d9ef70f2d151a860f720d4dc00ab1b656969e1d4619c88d6` |
| `PAPER30_PORTFOLIO_SCREEN_20260906.md` | 374 | `50c6972d975d27a905266c5418b529b634c00b7b6ea5e1855915ee5806b4ca11` |

Read the proof, independent mathematical check, dedicated prior check and
this brief in full. Read the landscape's quantum sources/boundaries and the
portfolio's already-occupied scope and Q entry. Their preliminary descriptions
precede the completed proof; do not treat their old “surjection only” wording
as the current mathematical state. Conversely, the author proof's earlier
prior list is supplemented by the delivered dedicated prior report.
Only inspect directly relevant Paper29 source sections if needed to resolve
a specific inherited dependency; do not reopen accepted artifacts or builds.

## 3. The actual problem and completed claims

For monic, periodically repeated polynomials $p_i$ of degrees $d_i\ge2$
over a characteristic-zero field $K$, put $\delta=\prod_{i=0}^{k-1}d_i$.
Over $R=K[\hbar]$, or $R=K$ at any fixed value of $\hbar$, use
$$
A=R\langle x,y\rangle/(xy-yx-\hbar),\qquad
X_{i+1}+X_{i-1}=p_i(X_i),\quad X_0=x,\ X_{-1}=y,
$$
and $\sigma X_i=X_{i+k}$. Independent polynomial coefficient parameters
are permitted. All Hochschild homology is relative to $R$.
For $N=kn$ and $\tau=\sigma^n$, the periodic object is the **linear module**
$$
T_n=A/\operatorname{span}_R\{ab-b\tau(a):a,b\in A\}.
$$
It is not a quotient algebra at nonzero $\hbar$.

**Q1.** Chronological multiplication explicitly identifies $T_n$ with the
oscillatory quotient of the actual discrete cyclic action:
$$
S_N=\sum_iP_i(z_i)-\sum_i z_i z_{i+1},\qquad
D_i=M_{\partial_iS_N}-\hbar\partial_i,
$$
$$
Q_N=R[z_0,\ldots,z_{N-1}]/\sum_iD_iR[z_0,\ldots,z_{N-1}],
\qquad [\prod_i z_i^{e_i}]\longmapsto[\prod_iX_i^{e_i}].
$$
The bounded exponents $0\le e_i<d_i$ give a free $R$-basis of rank
$\delta^n$. Positive relative twisted HH vanishes. The statement includes
$N=1,2$, all coefficients, $\hbar=0$, and nonreduced classical collisions.

**Q2.** The actual $\sigma$ action is exact cyclic translation by $k$ on
this basis. There are no lower-order $\hbar$ corrections. Consequently
$\operatorname{tr}(\sigma^r\mid T_n)=\delta^{\gcd(n,r)}$.
The character is a short combinatorial consequence, not another new theory.

**Q3.** Expand $g$ in the infinite ordered orbit basis, and let $L(g)$ be
the maximum diameter of an individual nonconstant word. If $N\ge3$ and
$N>2L(g)$, then
$$
\left[\sum_{j=0}^{n-1}\sigma^jg\right]_{T_n}=0
\quad\Longleftrightarrow\quad g\in(\sigma-1)A.
$$
This uses every coordinate of the finite twisted-trace module, equivalently
all its linear twisted traces, not one selected scalar functional.
The result is exact at every $\hbar$, not only an $\hbar$-adic lifting.

## 4. What is actually proved, and what is inherited

The new proof's central calculation eliminates the interior $D_i$ using
increasing weights, leaving a genuine PBW isomorphism to $A$. The two ends
become $E_y$ and $-E_x$, where $E_a=L_a-R_{\tau(a)}$. The relative Weyl
resolution and a bounded Koszul bicomplex identify the full homology with
no degree shift. A separate one-variable elimination handles $N=1$.

Twisted cyclicity moves a whole ordered terminal block to the front. That
proves both exact macro equivariance and exact short-word wrapping without
illegal multiplication of module-class equalities. The short-word no-alias
lemma and orbit-coefficient criterion then give Q3.

The independent mathematical report found no theorem-level gap and no
additional hypotheses. It supplies explicit resolution signs, degree-zero
strictness, the single-row spectral-sequence argument and the inequality
$t-N<s$ which makes the wrapped product already chronologically ordered.
These clarifications are available for a later manuscript; the frozen author
input has not been silently edited.

Deduct rather than rebrand the following:

- Weyl PBW, its elementary nonlinear shears, the relative length-two Koszul
  resolution, and monic regular-sequence filtered arguments are standard.
- Paper29 supplies the infinite orbit basis, its ordinary-degree leading
  terms, orbit-coefficient obstructions, no-alias combinatorics and all
  degree-to-diameter estimates. Their PBW transport is short.
- The inherited logarithmic period bound, $\delta^4D^4$ rank estimate for
  $D\ge1$, unchanged Hilbert series and bounded-degree primitives are not
  additional new headline contributions.
- A rank-two nonideal example at $p=x^2+2x$, $n=1$ has $[x^2]=0$ and
  $[x^3]=\hbar[1]$. It clarifies the object, but is only a short example.

## 5. Strongest actual prior and remaining uncertainty

The dedicated report records actual-read sections, versions and links.
In particular, **do not say existing theory only handles linear maps**.

- Gunningham–Safronov, *Deformation quantization and perverse sheaves*,
  Duke Math. J. 175(6) (2026), Theorems 5.9/7.1, already give the nonlinear
  Lagrangian-DQ-to-twisted-de-Rham comparison, including non-Morse settings.
  It is a substantive method prior, not just a loose analogy.
- Petit gives the general DQ kernel/diagonal Hochschild trace framework;
  Charles supplies FIO composition and transverse fixed-point asymptotics.
- Krause–McCandless–Nikolaus, Theorem 6.26, gives general cyclic trace
  structure on bimodule tensor powers. Existence of a $C_n$ action is prior.
- Douai–Sabbah supplies tame Brieskorn-lattice freeness and Jacobian fibers.
  AFLS, Sharapov–Skvortsov and Etingof–Stryker cover the stated linear Weyl
  and general twisted-trace background.
- Quantized Hénon and exact nonlinear quantum shears are already prior.
  The 2000/2004 Hénon papers' full texts remain unread after bounded public
  access attempts. Weickert 2003 explicitly restates relevant early results;
  that is not a substitute for claiming the two target full texts were read.

The remaining possible increment is the specified **global polynomial
$K[\hbar]$ lattice**, all specializations, chronological basis, and its
exact compatibility with finite wrapping and detection. The read general
theorems do not by themselves identify this complete package; analytic or
$\mathbb C((\hbar))$ comparison cannot be inverted to recover a chosen
polynomial lattice and its $\hbar=0$ fiber. This is a precise distinction,
not proof of world priority or an assurance of sufficient research value.
Reviewers should explicitly decide whether the direct elementary realization
is nevertheless a short standard specialization after these deductions.

## 6. Non-padding organization to assess

A possible unified organization is: problem and prior delta; the Weyl orbit
and linear periodic object; oscillatory filtration and internal elimination;
endpoints, relative HH and small periods; exact cyclic basis action; infinite
PBW words, exact wrapping and finite detection; classical specialization,
one nonideal example and limitations. This is a dependency order, not a page
allocation or evidence that the package reaches 22 pages.

Give your own section-by-section **natural** low/central/high estimates,
identify unavoidable overlaps, and explicitly return each gate and the
conjunctive outcome. Do not invent unproved quantum spectral, positivity,
analytic integral, convergence, period-tower, deformation-classification or
arithmetic results to make the estimate pass. Further development proposals
must be labeled unproved and must not count as current substance.

## 7. Scope and reviewer provenance

The unavailable specified GPT-5.4/Codex-MCP endpoint is not being claimed.
Use actual fresh independent secondary agents with xhigh reasoning under the
available research-review workflow. This is not an external human review.
Route A/B applicability is NOT_APPLICABLE: these are structural algebraic
claims, not Riemann determinants or Hilbert–Pólya operators.
All effects are local; there are no numerical experiments, paid resources,
uploads, submissions, external messages or mutations of accepted Papers27–29.
