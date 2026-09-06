# Positive-characteristic scout: one full-family follow-up, no paper admission

2026-09-07. Status: **0 admitted contracts; the full degree-$2p$ coefficient
family has an author proof pending independent review; two decisive failed
shortcuts remain.** This is the bounded positive-characteristic lane for the
authorized C414–C418 batch, not a numbered paper or five-paper plan.

Continuation: the initial strict-gap-only screen below has been superseded
within PC414-R by [FULL_DEGREE_2P_PROOF.md](FULL_DEGREE_2P_PROOF.md): every
odd prime $p$, $q=p^e$ with $e\ge3$, all degree-$2p$ lower polynomials, every
allowed coefficient and every positive period. A two-term perfected-ring
invariant closes the previously missing low-support branch. Independent
proof, source and substance gates remain pending; author closure is not
paper admission. The sextic construction is a special case, not another
contract. The earlier restricted note and failed shortcuts are retained as
the historical screening record.

The repository batch workflow was used first; `research-lit`, `idea-creator`
and ARS source verification supplied bounded collision checking, and
`proof-writer` was used to separate the closed restricted lemma from the
unproved full-family target. The current team and CPU exact arithmetic were
used; no older model/API default, external review, or GPU pilot was invoked.
The skill-driven narrowing does not reduce the user's substantial-paper gate.

## Disposition

| Contract | Exact substantial target | Decisive screening outcome | Disposition |
|---|---|---|---|
| PC414-R: inseparable-lower-degree resonant Hénon returns | A coefficient-sensitive, all-period classification of degree and reduced counts, with a finite Hasse-support invariant replacing C404's coprime-degree assumption | Same degree and leading coefficient give different third-period counts. The initial strict-gap companion has now been strengthened to an author proof for the entire degree-$2p$ family, every odd $p$ and $q\ge p^3$, using a finite perfected-ring invariant. | **AUTHOR_PROOF_READY; independent proof/source/substance review pending; unadmitted** |
| PC414-F: forward arithmetic of the wild cubic | For every finite-field parameter in the specified wild cubic family, classify ordinary periodic counts and local multiplicities at all forward times, retaining the finite-extension axis | At the base specialization x^3+x^2, time 5 already has 238 points versus length 243. The missing all-cycle ramification/multiplier classification is not encoded by the generic inverse-tree group. | **NOT_CURRENTLY_JUSTIFIED; no forward theorem** |
| PC414-S: nonlinear monomial-base Frobenius skew inverse problem | Determine whether the entire finite-field forward-return ledger recovers polynomial forcing modulo natural vertical polynomial conjugacy | Every P and P^p give identical return ledgers via a radicial conjugacy. An explicit infinite family remains pairwise distinct modulo polynomial vertical shears and fibre scaling. | **REFUTED_INVERSE_CLAIM; short classical-type obstruction, not a paper** |

The coordinator's substance guidance is incorporated: neither the two-term
lemma nor the pure-Frobenius-support face is counted separately. No old
formal-disc cocycle, PSL tower or C410 inverse theorem is renumbered.

## PC414-R: native resonant Hénon–Frobenius returns

### Frozen target and increment

Object: $H(x,y)=(y,y^q+g(y)-ax)$ over $\mathbb F_q$, $a\ne0$, with
$2\le m=\deg g<q$ and $p\mid m$. Domain: the whole affine plane over
$\overline{\mathbb F}_q$. Clock: $S=H^{-1}\Phi_q$ iterated at every
positive integer $n$. Observable: ordinary geometric fixed points of $S^n$,
equivalently $H^n(P)=\Phi_q^n(P)$; not scheme length alone, not periodic
points of $H$ on a fixed finite field, and not a fixed variety's Hasse–Weil
zeta. When finite, the source zeta convention is
$\exp(\sum_{n\ge1}N_nt^n/n)$.

The intended new increment is a finite, coefficient-sensitive Hasse-support
description valid through all iterates, including branch changes and ties.
C404 already supplies the commuting-pullback framework and the complete
coprime-degree case. A new parameter table or a new proof of those classical
conversion steps is not the increment. The native source analytic problem is
meaningful, but no target arithmetic bridge has been constructed.

The cheap decisive test was to keep characteristic, degree, leading coefficient
and map determinant fixed while changing lower support at the first wild time.
The actual result is

| p, q, a, n | g | second fixed-equation degree | ordinary geometric points |
|---|---|---:|---:|
| 3, 27, 1, 3 | y^6 | 2484 | 48,892,572 |
| 3, 27, 1, 3 | y^6+y^5 | 3030 | 59,639,490 |

The first equation has top monomial $x^{19683}$, the second its stated pure
$y$ power, and the Jacobian determinant is one. Thus the finite computation
does not substitute scheme length for ordinary points. A separate short
algebraic certificate and the gap-stratum theorem are in
[PROOF_NOTE.md](PROOF_NOTE.md).

### Closed salvage, with its substance limit

Let $g=by^m+cy^\ell+R$, with $a,b,c\ne0$, $\deg R<\ell$,
$2\le\ell<m<q$, $p\mid m$, $p\nmid\ell$. Put $h=m-\ell$ and
$\rho=p^{v_p(m)}$. If

$$
q-m>h,\qquad q(\rho-h-1)-m(\rho-1)>h,
$$

the note proves, for every period and every allowed coefficient,

$$
N_n=q^{2n-w}\frac{(\ell-1)q^w+q(h+1)-m}{q-1},
\qquad w=p^{v_p(n)}.
$$

The proof is a closed two-term-block induction, not a numerical extrapolation.
It shows concretely how a highest non-p-divisible lower exponent can control
the all-height count. Its strict inequalities suppress branch competition;
they do not resolve it. The coordinator judged a short additional two-term
induction likely companion-level, and the author agrees not to self-admit it.

### Initially missing theorem and its symbolic closure

The initial precise full-family replacement **within this same contract** was the
degree-six family in characteristic three: every $q=3^e$, $e\ge3$,
every nonzero determinant and leading coefficient, and all five lower
nonconstant coefficients and the constant coefficient of $g$. The nonzero
$y^5$ stratum was already proved. The missing stratum had $y^5$ coefficient
zero and possibly nonzero $y^4$ coefficient; it required controlling support
ties at every height.

The decisive step was not one more point census. It was a finite
Hasse-support invariant, with coefficient data, staying closed under
$\delta=H^*-\Phi_q^*$ and proving the leading terms at every height.
The elementary single-monomial rule is

$$
\deg\delta(y^D)=q(D-r_D)+mr_D,
\qquad r_D=p^{v_p(D)},
$$

but a lower monomial can overtake this candidate, and several contributions
can tie. General mixed monomials also introduce an uncancelled Frobenius term.

The follow-up author proof closes these issues for the larger degree-$2p$
family, all odd $p$. If the highest lower exponent $\ell$ lies in
$[p+2,2p-1]$, the strict gaps are automatic for $q\ge p^3$. Otherwise write
$g=by^{2p}+cy^{p+1}+R_0$, $\deg R_0\le p$. In the perfection set
$\mathcal D=\operatorname{Frob}_p^{-1}\delta$, $Q=q/p$ and
$\varepsilon=(p-1)/p$. The closed invariant is

$$\mathcal D^j y=\alpha_j y^{E_j}
+\beta_j y^{E_j-\varepsilon}+P_j,\qquad
\deg P_j\le E_j-1,\quad E_{j+1}=Q(E_j-1)+2,\quad E_1=2.$$

The retained fractional term has next degree strictly below
$E_{j+1}-1$; arbitrary perfected mixed remainders satisfy the uniform bound
$\deg\mathcal D P\le Q\deg P$. Semilinearity accounts for non-prime-field
coefficients and $\delta^j=\operatorname{Frob}_p^j\mathcal D^j$ gives
ordinary-polynomial descent. Thus in this low class

$$D_j=\frac{p q^j+(q-2p)p^j}{q-p},\qquad
N_n=q^{2n-w}D_w,\quad w=p^{v_p(n)}.$$

The full proof and high-class formula are in the new proof-gate artifact.
The remaining checkpoint is independent verification and the separate
substantiality/ownership decision, not a larger finite census. General
degrees divisible by $p$ beyond this full degree-$2p$ family remain outside
the theorem.

## PC414-F: wild cubic forward and finite-extension returns

Object and quantified family: $f_a(x)=x^3+ax^2$, every finite field
$\mathbb F_{3^s}$ and $a\in\mathbb F_{3^s}^*$. Domain: the affine line
over its algebraic closure. The forward clock is $n\ge1$, while extension
degree $r\ge1$ remains independent. Observables are

$$
N_a(n)=\#\{x:f_a^n(x)=x\},\qquad
M_a(n,r)=\#\{x\in\mathbb F_{3^{sr}}:f_a^n(x)=x\},
$$

together with each local multiplicity of $f_a^n-x$. The intended increment
was a uniform multiplier/ramification classification sufficient for all these
counts, not a generic inverse-image Galois group and not diagonal clock
identification. C410's mixed Kummer/AS inverse tower is a classical-input
boundary for this new question, not the answer to it.

At $a=1$ over $\mathbb F_3$, the exact ordinary counts for $1\le n\le6$
are $3,9,27,81,238,729$. The first failure of the degree shortcut in this
bounded test is time five:

$$
f^5-x=U(x)(x^5-x^4-x^3-x+1)^2,
$$

where $U$ is squarefree of degree 233 and coprime to the displayed squarefree
degree-five factor. Those five repeated points have exact period five.
The source note and [script](bounded_probe.py) state the computational scope.

This does not disprove a possible all-cycle theorem. It identifies the exact
missing issue: every relevant first-return multiplier and its characteristic-
three ramification tower, including new parabolic cycles, must be controlled.
The generic inverse group alone provides no proof of this diagonal data.
Bridy's checked paper explicitly separates proved dynamically affine cases
from a broader separable-map conjecture; our bounded search is not a statement
about its complete current global status. The candidate is not admitted, and
there is no evidence-backed bounded route to its full claim at this checkpoint.

## PC414-S: forcing is not identifiable from complete return counts

### Exact inverse question

For every odd prime $p$ and $P\in\mathbb F_p[x]$, set

$$
F_P(x,y)=(x^2,y^p+P(x)).
$$

The source is nonlinear, with native forward clock $n$. The domain for the
observable is $\mathbb F_{p^r}^2$ for every extension degree $r\ge1$;
the complete ledger is $L_P(n,r)=\#\operatorname{Fix}(F_P^n)$ on that finite
set. At each $r$ its finite zeta/determinant convention is the usual
finite-map one, already classical. The proposed new inverse increment was:
does this entire two-axis ledger determine the forcing modulo conjugacies
$(x,y)\mapsto(x,\lambda y+Q(x))$, with $\lambda\in\mathbb F_p^*$ and
$Q\in\mathbb F_p[x]$?

### Complete elementary refutation

The map $J(x,y)=(x,y^p)$ is bijective on every finite extension and satisfies

$$
JF_P=F_{P^p}J.
$$

It follows for **all** $n,r$ that $L_P(n,r)=L_{P^p}(n,r)$. This is a
radicial conjugacy on perfect-field points, not a polynomial automorphism.
It also commutes with the extension-field Frobenius. No finite test is used
to infer the all-extension conclusion.

The forcings $P_k=x^{p^k}$, $k\ge0$, remain pairwise inequivalent under the
stated polynomial vertical conjugacies. Here is a complete separation
argument. Every positive exponent has a unique expression
$u2^a p^b$, with $u$ odd and $p\nmid u$. For fixed $u,s$, let
$\Lambda_{u,s}$ sum the coefficients of a polynomial at exponents
$u2^a p^b$ with $a+b=s$. The shear difference

$$
Q(x^2)-Q(x)^p
$$

is annihilated by every $\Lambda_{u,s}$: a monomial of $Q$ contributes its
coefficient with opposite signs at the two endpoints $2j,pj$ of the same
$(u,s)$ chain. But $\Lambda_{1,k}(P_k)=1$ and
$\Lambda_{1,k}(P_j)=0$ when $j\ne k$. Multiplication by a nonzero fibre
scalar cannot change zero into nonzero. Thus no such shear/scaling equates
the pair, although their complete return ledgers coincide.

This refutes the stated inverse claim. It does not exclude arbitrary
nonvertical polynomial conjugacy, classify all radicial equivalences, or
identify a target spectral divisor. The Stacks Project's classical
topological invariance under universal homeomorphisms is stronger background
for the invisibility mechanism; the small coefficient-chain observation is
not enough to turn this into a substantial separate paper.

## Exact checks and reproducibility

Run from the repository root:

```text
python -B henon_dynamics/research_c414_c418/positive_characteristic/bounded_probe.py
```

The final script ran with Python 3.12.3 and SymPy 1.14.0, exit 0. It
constructs 18 resonance cases, each with two literal fixed equations
(q=9,27; g=y^6,y^6+y^5,y^6+y^2; n=1,2,3), checks unique coprime
leading terms, computes six exact cubic
squarefree decompositions, and runs 18 prime-field skew sanity cases.
Those latter cases do not test extension fields and are explicitly only
sanity checks; the all-extension result has the displayed algebraic proof.

An intermediate unoptimized q=27 polynomial-power implementation was
terminated explicitly (exit 143) after it exceeded the intended cheap check.
Replacing qth powers by the exact characteristic-three Frobenius monomial
operation gave the successful bounded run in under a second. No time limit
was silently treated as a mathematical zero or a passed check. The script
prints its own results and does not read old output or write outside this lane.

Primary-source records, read scopes, search formulations and the exact
classical ownership limitations are in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## Handoff and exclusions

The lane's useful outcome is a concrete full-support proof bottleneck, an
unadmitted all-period stratum theorem and two rigorous rejected shortcuts.
There is no independent-paper admission for the coordinator to count yet.
The next proof question is the degree-six missing stratum above; otherwise a
new subtype would require a fresh bounded contract, not a placeholder PDF.

No formal evaluation was run and no evaluator was edited. All target Euler,
root-number, automorphy, zero/divisor, Hilbert–Pólya and Route B assertions
remain absent. The source note is AI-assisted work with author checking;
independent internal review, paper-level substance adjudication and human
peer review are distinct, unclaimed gates.
