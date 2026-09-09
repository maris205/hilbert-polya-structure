# Round 9: finite certificates and actual Frobenius incidences

2026-09-09 UTC, coordinator adjudication after all three final internal
reviews. This is a research checkpoint, not manuscript release.
The continuous user authorization and Route-A boundary are unchanged.

## 1. Actual outcome

Three author reports and three nonauthor mathematical reviews are complete.
The coordinator read all author proofs and every final review line,
hand-checked the proof-bearing interfaces, and verified the final hashes.
The reviews have 527, 107 and 425 lines, **1,059 lines total**.
There are zero open mathematical or provenance/source-applicability
must-fixes within the auxiliary claims accepted below.

The full quadratic norm-one implication, all-degree MS6, and the specified
arbitrary integral tame lift remain **NOT CURRENTLY JUSTIFIED**.
The existing PC424-L, UL4, OM4 and RLG5 contracts remain the only four
admitted contracts. There is no fifth admission, manuscript, completed paper,
PDF or formal evaluation. No target-arithmetic grade changes.

All tasks reused existing current-session threads. R9 had **zero mathematical
program executions**: the matrices, bounds and controls are proofs, not
executed finite certificates. No extra agent, external model/API upload,
GPU job, evaluator edit, Route B work or other-stream research occurred.

## 2. A1: a finite certificate for a fixed annihilator

Author: [general quadratic norm-one report](a1_general_quadratic_normone/REPORT.md).
Nonauthor: [E2 complete review](reviews/e2_finite_normone_certificate/REVIEW.md).

For every odd prime, every $c\in\overline{\mathbb F}_p$, and every rational
norm-one function, retain the reduced normalization

$$w=\eta A/B,\qquad B(X)=(-1)^mA(-X),\qquad \eta\in\{1,-1\},$$

where $A,B$ are monic coprime degree-$m$ polynomials, nonzero at zero.
All root multiplicities and simultaneous factors are retained. In the
actual cyclic quadratic algebra, put

$$U_n=S(X_0)(2^nP_n-1)
\left(\eta^n\prod_iA(X_i)-\prod_iB(X_i)\right),
\qquad P_n=\prod_iX_i.$$

For each fixed nonzero $S$, with $\ell=\deg S$ and
$k_S=0$ if $\ell=0$, otherwise $k_S=\lfloor\log_2\ell\rfloor+1$,
the accepted auxiliary theorem is

$$\forall n\ge1:\ U_n=0
\quad\Longleftrightarrow\quad
\forall\,1\le n\le k_S+16(m+2)^2:\ U_n=0.$$

The proof uses the nondegenerate top-coefficient pairing on the nonreduced
cyclic algebra, a general-$c$ finite residue expansion, four block matrices
with the phase and signs retained, logarithmic contraction of the one
exceptional high-degree site, and the elementary finite span of matrix words.
It does not use a characteristic-zero trace-uniqueness theorem. Both root
and E2 checked the empty tail, self-loop $n=1$, $c=0$, $m=0$, $\ell=0$,
wild periods, repeated roots and arbitrary powers.

The ordinary cofinite primitive-cycle product condition (CP) supplies
**one fixed** $S$ annihilating every level, by multiplying the cleared
product identity by $(f^{\circ n}-x)'$. Thus the theorem is a finite
certificate for a fixed annihilation problem, not an algorithm deciding CP.
No degree bound for an unknown exceptional $S$ is proved. No implication
from all the annihilation identities back to CP, or from those identities
to $w=1$, has been established.

The characteristic-three example $f=x^2$,
$f^{\circ2}-x=x(x-1)^3$, shows Jacobian loss on one local factor.
It does not refute the all-level converse. Likewise the trace of $p$ copies
of a representation vanishes on all words, but no trace-identification
claim is used in this proof. Infinitely many bad cycles for one atom do
not exclude a fixed finite product-value group or imply factorwise CP.

E2's review independently reconstructs all auxiliary mathematics after
reading the author file; it is not labeled blind review. The author's
exposure to coordinator pairing/state-organization suggestions is disclosed.
Two provenance-only repairs clarified that R8 E5's 429-line report reviews
the final 526-line author proof, while R8 E2's 448-line report only reviews
the coefficient. Both were actually read back; no mathematical formula
changed. The final author file has 437 lines.

## 3. A2: exact incidence solutions and the missing uniform bound

Author: [Frobenius-twisted bridge](a2_frobenius_twisted_bridge/REPORT.md).
Nonauthor: [E5 complete review](reviews/e5_frobenius_twisted_bridge/REVIEW.md).

This distinct mechanism retains every prime, every $d\ge2$, every $c$ and
every rational $g$ for $f=x^d+c$. On the actual set
$S_q=\{a:f(a)=a^q\}$, where $q=Q^r>d$ and the coefficient field is fixed,
native iteration really equals $q$-Frobenius. Native period therefore
equals the corresponding finite-field degree, and CP gives norm one on
the retained cycles. This is not asserted for arbitrary periodic points.

Writing $d=\eta s$ with $\eta=p^{v_p(d)}$ and $p\nmid s$, the ordinary
incidence count is $q/\eta$ for $c\ne0$ and $q/\eta-s+1$ for $c=0$.
The proof handles inseparable multiplicities instead of using raw degree
as a point count. A fixed finite forward-stable deleted set leaves an
unbounded number of distinct points.

Elementary finite-field Hilbert--90 and interpolation give nonzero
$H_q\in\mathbb F_q[x]$ of degree less than the retained point count,
satisfying the transfer equation there. These solutions live in finite
quotient algebras; they are not finite extensions of $k(x)$.

The accepted uniform-bound equivalence requires **fixed** exponent $e$,
degree bound $B_0$, field and finite deleted set before arbitrarily large
$q$ are chosen. Then rational interpolants for $g^{p^e}$ of degree at
most $B_0$ yield a single global identity $g^{p^e}=h\circ f/h$.
Indeed a nonzero cross-multiplied polynomial has degree at most
$p^eH(g)+(d+1)B_0$, eventually less than the distinct-root count.
Conversely a global identity supplies fixed interpolants and such data.
**The implication CP to this uniform bound is not proved.**

The old R6 control $f=x^{p+1},g=x$ is explicitly subtracted. The new
denominator-inclusive argument proves that every unsaturated rational
interpolant after at most $C$ fixed deletions has

$$\deg h_q\ge\frac{q-p-2-C}{p+2}.$$

This refutes the unsaturated uniform-degree shortcut, not MS6. The fixed
saturated transfer is $h=x$ for $g^p$, and the fixed purely inseparable
curve $Y^p=X$ has the actual stable lift $Y\mapsto Y^{p+1}=xY$.
The sample graph points of the displayed growing-degree interpolants
lie on that curve. Growing rational degree does not rule out a fixed
algebraic transfer.

The $p=3,f=x^2$ example using primitive $13^t$th roots proves infinitely
many native cycles are omitted by all first-step incidences: powers of
$3$ modulo $13$ never equal $2$. It supplies no observable passing all
incidence tests but failing CP, and does not defeat the degree identity
test. The generic transcendental extension with $\sigma Y=gY$ is also
not the needed finite algebraic extension.

Root directly read Papanikolas's complete twisting definition, the
$\sigma$-admissibility and existing-fundamental-matrix setup, and
Theorem 4.3.1/Proposition 4.3.3 with their full proofs in the
[original primary text](https://arxiv.org/html/math/0506078v2).
E5 independently checked these passages. The abstract framework is
broader than coefficient twisting, but still assumes an automorphism
and an existing solution. The special relative-algebraic-closure result
does not establish algebraicity of that solution field. No native UB
theorem is imported from it. A2's two targeted search batches gave no
applicable existence bridge; this is not a literature-wide absence claim.

## 4. C2: actual coordinates cannot be replaced by their finite values

Author: [integral tame flexibility](c2_integral_tame_flexibility/REPORT.md).
Nonauthor: [E4 complete review](reviews/e4_integral_tame_flexibility/REVIEW.md).

The exact question remains an arbitrary integral tame conjugate
$K=M^{-1}\rho_QM$ realizing the same
$\kappa=(5\ 9)(3\ 8)(6\ 7)$ on the accepted nine-point set $C$.
There is no word-length, degree or coefficient restriction in this question.
The two-shear obstruction is not promoted to an all-word obstruction.

The accepted iff interface requires an **actual** $M=(U,V)\in
\operatorname{TA}_2(\mathbb Z)$: $U$ is constant on each kappa orbit;
equal $U$-levels have consistent $V(P)+V(\kappa P)$; and the unique
rational interpolating polynomial of degree below the number of distinct
levels has integer coefficients. Monic integer division proves necessity
for all possible degrees of $Q$; the existing integral tame inverse
proves sufficiency. Fixed points require the genuine values $2V(P)$.
Existence of that coordinate pair is not proved.

On the same $C$, the polynomials $x$ and
$x+\prod_{r=-1}^3(x-r)$ have the same evaluations, but the latter
cannot be a rational polynomial coordinate: its Jacobian with any
companion contains the nonconstant factor $1+(\prod_{r=-1}^3(x-r))'$.
This concerns chosen representatives, not nonexistence of every possible
coordinate with desired finite values. An actual lift would give the
native nine-cycle of $KIA$; no lift has been constructed.

Root and E4 read Theorem 3 and its complete proof in
[Berson--Dubouloz--Furter--Maubach](https://arxiv.org/html/1011.0976v1).
For $\mathbb Z$ its common-map local-tameness criterion applies, inside
$\operatorname{GA}_2(\mathbb Q)$ and using localizations $\mathbb Z_{(p)}$,
not completions. It does not exchange $\exists M\forall p$ and
$\forall p\exists M_p$. The finite-field 2026 preprint was checked only
at primary-record/abstract scope; unavailable publisher leads supply no
theorem. The two-batch source screen supplies neither an integral lift
nor an all-word impossibility theorem.

## 5. Final input bindings and integration boundary

All six final input SHA256 values were independently read from disk:

| Relative path | Lines | SHA256 |
| --- | ---: | --- |
| `a1_general_quadratic_normone/REPORT.md` | 437 | `6c7a21d2ceaecf585f7c37f8c57dcce79ce1243d2ec9926059f826adc9e15d40` |
| `a2_frobenius_twisted_bridge/REPORT.md` | 421 | `feb532fd56b8180b52bf45991bff1c8edebbabdef743317619ac53fe0b475052` |
| `c2_integral_tame_flexibility/REPORT.md` | 212 | `d73e3cd3149bc695f5e8b331c3d05bad519630eb7fd8ce7889c97a9ba85f30ea` |
| `reviews/e2_finite_normone_certificate/REVIEW.md` | 527 | `3f54ed01c5b600e4bf23fbda632e2bad72548f55ee0154ba6b00d2af9c5a7533` |
| `reviews/e4_integral_tame_flexibility/REVIEW.md` | 107 | `00b50e977bd94d380120611d1055b114fde1a395baac8462c14769745c1fe8c6` |
| `reviews/e5_frobenius_twisted_bridge/REVIEW.md` | 425 | `956b82c46db9cf4fe3468f2bc39e513e657b3167ef70d757fa8d33616566ec38` |

Author/reviewer date headers retain their environment-provided 2026-09-10;
the coordinator's actual clock reads 2026-09-09 UTC. Neither date is
used as mathematical or execution evidence. Frozen inputs are not rewritten.

All six mathematical inputs are now frozen. The next integration gate is
a separate exact-path, hash, scope and local-link audit, followed by normal
repository synchronization of this checkpoint. Neither staging nor push is
claimed by this decision. Previous round inputs and eight inherited
untracked directories remain untouched. Next-round tasks, if assigned, are
separate files and do not alter this verdict.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force. Ordinary products,
Frobenius norms and finite transfer certificates do not establish target
Euler factors, root numbers, automorphy or a Hilbert--Polya realization.
