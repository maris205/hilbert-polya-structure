# Non-author review: simple projective wild inverse tower

2026-09-06. The coordinator read the complete 542-line initial proof
[WILD_PSL_RATIONAL_PROOF.md](positive_characteristic/WILD_PSL_RATIONAL_PROOF.md),
not only the author's theorem summary. This is current-team internal
mathematical review, not human peer review or a novelty certificate.

**Mathematical verdict: PASS for the stated all-prime, all-height theorem.**
No gap was found in the global induction or local argument. The later
source/substance review is now complete: **REJECT_SUBSTANCE for a separate
paper**, with the valid proof retained as a companion note. See the final
adjudication below. The first-level cover and abstract wreath/Goursat
mechanisms are classical.

## Exact reviewed contract

For every prime $p\ge5$, every field $k$ of characteristic $p$ and every
$n\ge1$, the generic splitting tower of $f(X)=X^p+X^{-1}$ has group
$W_n$, the full $n$-fold permutation wreath power of
$G=\operatorname{PSL}_2(\mathbb F_p)$ in degree $p+1$. Arithmetic and
geometric groups agree. Over algebraically closed constants, only
infinity branches. With $m=(p-1)/2$ and $b=m+1$,
$$
 e_n=mp^n,\qquad D_n=p^{n+1}-(m+2),\qquad
 I_n=(C_p)^n\rtimes C_m,
$$
and the wild group occupies exactly lower levels $1,\ldots,b$.
The genus is
$$
 1+\frac{|W_n|}{2m}\left(1-\frac{m+2}{p^n}\right).
$$
This is an inverse-image-height theorem. It is not a calculation of
ordinary forward periodic points, finite-field extension-degree counts,
an Artin--Mazur zeta, or a target arithmetic determinant.

## Global steps independently checked

### First cover and upper bound

The degree of $k(v,w)/k(t)$ is exactly $pm(p+1)$ for
$w^p-w=v^{-b}$ and $t=v^{mp}+v^{-m}$: the AS right side has pole
order prime to $p$, and the rational map in $v$ is separable of degree
$m(p+1)$. The listed $p+1$ roots are distinct. Inverting the differences
of two nonselected roots from the selected root recovers $v$, then $w$;
the displayed field is therefore the splitting field, not a larger
auxiliary field.

The $\operatorname{SL}_2(\mathbb F_p)$ transformations preserve the
AS relation, since the fractional-linear difference is divided by
$(a+cw)^{p+1}$, exactly the change in $v^{-b}$. They preserve the
target, and the kernel is $\{\pm I\}$. All formulas are over the prime
field. Compatible copies of this first splitting cover at every tree
vertex give the full-wreath upper bound over arbitrary $k$; there is
no unexplained passage from symmetric or PGL local actions to PSL.

### Leaf stabilizers have no quotient isomorphic to G

In the recursive leaf stabilizer, the distinguished Borel factor is
normal and solvable. Every other bottom factor is a copy of the
nonabelian simple $G$. Its image under a hypothetical surjection to
$G$ is either trivial or all of $G$. The previous-level leaf stabilizer
has no singleton orbit on the remaining parents: its first-divergence
Borel translation moves any such parent while fixing the selected path.

If one bottom factor survived, a different conjugate bottom factor
would survive as well. Their full images would commute, contradicting
noncommutativity of $G$. Killing all bottom factors leaves a surjection
from the previous leaf stabilizer, so induction is valid. The argument
uses no information about the next dynamical Galois group.

### Base change precedes independence

$L_n/k(\alpha)$ is Galois with the already established leaf stabilizer
as group. Its intersection with the first splitting cover at $\alpha$
is Galois over $k(\alpha)$ and, by simplicity, either trivial or the
whole simple cover. The latter would supply the forbidden quotient.
Thus every base-changed child field really has group $G$ before any
claim of a full new kernel is made.

### Distinct ramification supports, then the direct product

The local lemma proves actual nontrivial degree-$p$ ramification at
each pole and complete splitting at nonpoles. At infinity the pole
leaves form an embedded full $p$-ary subtree. The previous full wreath
group moves this subtree through every possible omitted-child choice.
For any distinct pair of leaves, choose an omission at their first
divergence that retains the first and removes the second. The two child
fields then have different ramification at a conjugate place and cannot
be equal.

For nonabelian simple Galois fields, pairwise distinction suffices for
joint independence by the explicitly proved simple-factor lemma: any
surjection from a product of copies of $G$ onto $G$ kills all but one
factor. This reasoning would be false for general abelian covers, but
the proof does not make that generalization. The full kernel and the
wreath upper bound determine the next group.

## Local reasoning independently checked

The coordinator rederived the local estimates and then fully read the
separate non-author [local review](arithmetic/REVIEW_PSL_LOCAL.md).
Its detailed calculations agree with the coordinator's audit.

For pole parameters of normalized valuation $-m$, small inverse roots
have valuation $m$. Their difference has valuation
$v(A-B)+2m$, so the appropriately aligned $m$th-root ratio differs
from one at order at least $m+1=b$. The two AS right sides consequently
differ by an integral element. Over the stipulated algebraically closed
residue field that difference is an AS coboundary, while either original
class is nonzero because its pole order $b$ is prime to $p$.

All pole parents therefore give the same degree-$p$ local field. This
determines the new ramification index before the old valuation is
multiplied by $p$. Only in that new normalization does the child
difference identity force all distinct new poles to differ at order
at least one. There is no circular normalization or confusion between
global independence and local equality.

The different of the root-path extension follows independently from
$h(u)=u^p/(1+u^{p+1})$ and
$h'(u)=-u^{2p}/(1+u^{p+1})^2$. The remaining degree $m$ to the Galois
completion is tame. Transitivity gives the claimed different.
Closeness of distinct poles supplies a termwise Hilbert-different lower
bound which exactly attains this value. Hence every nontrivial wild
element has ramification number $b+1$, rather than merely satisfying
a bound. The positive graded quotient injects additively into the
residue field, yielding elementary-abelian wild inertia of rank $n$.
The tame action is scalar and faithful because $\gcd(b,m)=1$ and
$\mu_m\subset\mathbb F_p^*$. The genus calculation is then exact.

Arithmetic equality follows by squeezing the geometric $W_n$ between
the arithmetic group and the already justified arithmetic upper bound.
The degree remains unchanged upon algebraic constant extension, so the
regularity statement does not conceal a constant-field enlargement.

## First owner independently verified

The coordinator independently read the entire Serre appendix in the
[author-deposited 1992 original](https://arxiv.org/pdf/math/9207210), PDF
pages 64--66, together with the bibliographic page and the relevant
historical discussion in Section 11. This was not a full read of the
66-page article. The appendix, a letter dated 15 November 1990, treats
the exact equation $Y^{q+1}-XY+1=0$ and its PSL monodromy. It uses
Dickson invariants and a tame cyclic base change. Setting $q=p$ gives
precisely the present first cover. Its group, branch support and
first-level genus are therefore fully deducted from the increment.

The author's [first-level audit](positive_characteristic/PSL_FIRST_LEVEL_SOURCE_AUDIT.md)
and [bounded exact-check receipt](positive_characteristic/PSL_EXACT_CHECK_REPORT.md)
were also read in full. The finite computations check formulas and
abstract group examples; they do not compute the actual all-height
function-field Galois groups or establish priority. The coordinator did
not rerun them just to duplicate the author's diagnostic receipt.

## Pending gate and exposition requests

The separate source audit must determine whether an existing general
composition theorem owns the all-height increment. No fifth contract
is admitted merely because the three-page classical appendix lacks it.
In particular, characteristic-free field-theoretic appendices must be
checked on their actual hypotheses rather than excluded from a paper's
characteristic-zero title or applications.

The missing backslash in the initial (T1) display was corrected by the
author. Two nonblocking clarifications were requested for the written
proof: explicitly connect the degree-$p^n$ root completion to pole-root
inertia transitivity, and name Schur--Zassenhaus for the tame splitting.
These do not alter the theorem or call for finite mathematical retests.

At this review stage: mathematics PASS, first-level owner classical,
all-tower ownership/substance decision PENDING, formal C admission NONE.

## Final source/substance adjudication

The pending label immediately above records the initial mathematical
review stage, not the final selection status. The coordinator subsequently
read the entire 339-line non-author
[ownership audit](nonlinear_geometry/PSL2_TOWER_SOURCE_AUDIT.md), compared
its deductions with the valid proof, and obtained the author's independent
agreement with its residual analysis. Final decision: **REJECT_SUBSTANCE**
for an additional batch paper; retain all mathematics and diagnostics.

The coordinator independently read KNR's Appendix A and the §2 standing
characteristic-zero convention in the
[primary public v2](https://arxiv.org/pdf/2401.17872). Its Corollary 4.6.B
is not quoted as a literally characteristic-free published theorem.
The finite-group and separable-Galois adaptation supplies the generic
upgrade after the map-specific height-two test and strict local growth;
the independent reviewer examined the underlying group arguments.
This is a deduction/application, not an exact publication collision.

What remains is the quantitative AS-field continuity estimate,
propagated pole closeness and the height-two support test. It is useful,
but substantially shares the cubic package's local-compositum collapse.
Unlike that package, it leaves no separate all-height mixed Kummer/AS
relation problem after the simple-group machinery has been deducted.
Different, jump, genus and regularity are consequences of those inputs.
This concrete subtraction, not proof length or lemma count, is why it
does not supply the missing independent fifth paper.

Both requested exposition clarifications have been incorporated, together
with explicit lower/upper numbering and classical-composition attribution.
These changes do not alter any mathematical formula or diagnostic input;
no unchanged finite lane was rerun. The two inaccessible older Abhyankar
full texts remain explicitly unresolved, and no global priority claim is made.
