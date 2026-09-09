# E8 independent full review: MS6 conditional multiplicative saturation

2026-09-10 UTC. Current-team nonauthor review using proof-writer and
research-review under the selected-model/no-external-upload boundary.
This review concerns the complete conditional result actually proved in
the allocated report. It does not substitute that result for MS6's
unproved existence implication.

## Decision and exact reviewed version

**Conditional Theorem 1 and its stated auxiliary implications:
PROVABLE AS STATED.** Mathematical must-fixes: **0**. Imported-source
applicability must-fixes: **0**. Required minor/textual repairs: **0**.

**Original MS6 equivalence: NOT CURRENTLY JUSTIFIED.** The report does
not prove that cofinite ordinary cycle products make the multiplicative
cohomology class torsion. No MS6 counterexample is established either.

The actual [author report](../../a2_multiplicative_saturation/REPORT.md)
was read completely, all 441 lines. Its frozen SHA256 is
`b02bcc4cfad2433b9ee0d88dc69e74ac62ae30e508ddbc4c3787f1adf8ade1c3`.
The author confirmed that this version has no pending edits; the reviewer
checked the hash independently.

The [X2 source report](../../x2_multiplicative_saturation_sources/REPORT.md)
was also read, all 207 lines. It was used as a record of source and
logical boundaries, not as a substitute for checking the proof or the
actual Hodge source. Its unrelated Mahler and cohomology source receipts
are not independently recertified by this review.

## Exact questions and scope of the positive decision

For every prime $p$, $k=\overline{\mathbf F}_p$, integer $d\ge2$,
$c\in k$, and $g\in K^\times$ with $K=k(x)$, put
$f(x)=x^d+c$, $\sigma a=a\circ f$, and $\delta a=\sigma a/a$.
Let (CP) mean that all but finitely many ordinary primitive native
$f$-cycles avoid the support of $g$ and have product one.

The original MS6 question is whether (CP) is equivalent to
$g^{p^e}=\delta h$ for some $e\ge0$, $h\in K^\times$.
The forward construction from (CP) remains open in the reviewed report.

The theorem that passes is the conditional statement

$$
(\mathrm{CP})\quad\text{and}\quad g^m=\delta a
\quad\Longrightarrow\quad
g^{p^{v_p(m)}}=\delta b
\qquad(m\ge1).
$$

Under (CP), it follows that torsion of $[g]\in K^\times/\delta K^\times$,
existence of a finite forward-stable algebraic transfer, and existence
of a $p$-power rational transfer are equivalent. The additional torsion
or finite-transfer premise is not silently inferred from (CP).

All primes, including two, all allowed degrees and parameters, and all
ordinary primitive periods are retained. Projective completion is a
proof device: infinity is one fixed cycle and is expressly excluded
from the later good-cycle count. This does not change a cofinite
ordinary-cycle condition on the affine line.

## 1. Easy implication, support exceptions, and constants: PASS

If $g^{p^e}=\delta h$, removing cycles meeting the zeros or poles of
$g$ or $h$ removes only finitely many primitive cycles. On every other
cycle, the product of the transfer ratios genuinely telescopes. The
resulting cycle product has $p^e$th power one, hence is one because
$Z^{p^e}-1=(Z-1)^{p^e}$ in characteristic $p$.

This handles $e=0$ and does not evaluate $h(f(a))/h(a)$ at a zero or
pole of $h$, even if that ratio has a cancelled rational expression.
The support convention is therefore strong enough for the claimed
pointwise implication.

The recorded example $f=x^{p+1}$, $g=x$ is correctly subtracted.
Products on nonzero cycles are one, an unsaturated transfer is excluded
by its valuation at zero, but $g^p=\delta x$. It is not an MS6
counterexample. Constant phases are handled by the separate large-prime
period argument below, not assumed away.

## 2. Finite algebraic transfer and purely inseparable converse: PASS

Let $H\ne0$ lie in a finite extension admitting the stated $k$-embedding,
and let $A(Y)$ be its monic minimal polynomial over $K$, of degree
$m=[K(H):K]$. Applying the embedding and using
$\widetilde\sigma H=gH$ gives a root $H$ of

$$
g^{-m}(\sigma A)(gY).
$$

This is a monic degree-$m$ polynomial over $K$. Minimality forces
it to equal $A$, even if the minimal polynomial is inseparable and
even though $\sigma K$ is a proper subfield of $K$. Comparing its
nonzero constant term gives $g^m=\delta a_m$.
No separable norm or linear-disjointness assertion is needed.

Conversely, from $g^P=\delta a$, $P=p^e$, adjoining the unique
$P$th root $H$ of $a$ gives a finite purely inseparable extension
$K(H)/K$. The embedding of $K$ extends uniquely to its perfect
closure and satisfies $(\widetilde\sigma H)^P=(gH)^P$ there.
Injectivity of Frobenius gives $\widetilde\sigma H=gH$, so the
finite subfield $K(H)$ is forward stable. This includes $P=1$.

The report's warning about unconditional equivalence is correct.
A nontrivial constant root of unity has an integer-power relation
but cannot have such a finite transfer. The coefficient equations
$\sigma a_j=\zeta^j a_j$ force every nonzero rational coefficient
to have rational-map degree zero, since composition multiplies that
degree by $d>1$. Then $H$ is algebraic over the algebraically closed
constant field and lies in $k$, contradicting its nontrivial phase.
This is a phase obstruction without (CP), not an MS6 counterexample.

## 3. Fixed finite exceptions and large prime periods: PASS

The multiplicity lemma is restricted to a fixed finite union $E$ of
periodic cycles. For a prime integer $n$ larger than all periods in
$E$, only the original fixed points in $E$ can be fixed by $f^n$.
No assertion about all other periodic-root multiplicities is made.

At any such fixed point, multiplier zero gives fixed multiplicity one.
A multiplier $\lambda\ne0,1$ has finite order $t$ because
$\lambda\in\overline{\mathbf F}_p^\times$; for prime $n>t$,
$\lambda^n\ne1$, again giving multiplicity one.
For multiplier one, a nonidentity germ has first nonlinear term
$\alpha z^r$ with $r\ge2$. The iterate has first nonlinear term
$n\alpha z^r$ when $p\nmid n$, so the multiplicity remains exactly
$r$. A germ of $f$ cannot be the formal identity, since a rational
function with zero germ is zero and $\deg f>1$.

Infinity is a fixed point of multiplier zero for this polynomial map.
Thus summing the finitely many relevant fixed multiplicities gives a
constant independent of sufficiently large prime $n\ne p$.
All choices of a period, multiplier order, and local first nonlinear
degree here belong to the fixed finite set, not to a growing family.

The full projective fixed-point length is $d^n+1$: the affine
polynomial has degree $d^n$, and infinity contributes one. The bounded
contribution of the original fixed points cannot account for this
length. For prime $n$, every remaining fixed point has exact period
$n$ and is affine. This proves the large-prime-period lemma without
a global multiplicity bound or a periodic-point census.

A nontrivial constant $\zeta$ of order $t$ satisfying (CP) is then
impossible: choose such a prime period larger than $t$ and the periods
of all exceptional cycles. Its product is $\zeta^n\ne1$.
Therefore the constant phase is rigorously removed, rather than an
implicit choice of Kummer component being made later.

## 4. Actual primary-source applicability: PASS

The reviewer directly accessed Brosnan's official
[Section 3.3](https://math.umd.edu/~pbrosnan/notes/Surfaces/shit.html),
reading Lemma 3.11, Corollaries 3.12 and 3.14, Theorem 3.15, and
their displayed proofs. The imported result makes the intersection
form nonpositive on the orthogonal complement of a positive ample
class, with equality only for a numerically trivial class. Corollary
3.14's very-ample wording poses no mismatch: a positive multiple of
the ample divisor is very ample, or Theorem 3.15 applies directly.

The algebraically closed field hypothesis was checked in
[Section 3.1](https://math.umd.edu/~pbrosnan/notes/Surfaces/sect0016.html),
including its adjunction statement. The arbitrary-characteristic
orientation was checked in
[Section 1.1](https://math.umd.edu/~pbrosnan/notes/Surfaces/sect0002.html).
The supporting Riemann–Roch statement and displayed proof in
[Section 3.2](https://math.umd.edu/~pbrosnan/notes/Surfaces/sect0017.html)
were also read. The invoked Hodge argument is algebraic and does not
introduce a complex-field, separable-map, or Kodaira-vanishing premise.

The surface used below is the smooth projective product $Y\times Y$
over the stated algebraically closed field, so these hypotheses apply.
The source supplies Hodge index, not the later Kummer construction or
an existence theorem for MS6. Those steps were independently checked.

## 5. Graph self-intersection and the square-root bound: PASS

The relevant count is the intersection length of the graph and diagonal,
not the number of distinct points. For a degree-$q>1$ morphism
$\phi:Y\to Y$ on a smooth connected projective curve of genus
$\gamma$, the graph is a smooth closed copy of $Y$ even if
$\phi$ is inseparable.

Its tangent map is $v\mapsto(v,d\phi(v))$. The quotient map
$(v,w)\mapsto w-d\phi(v)$ identifies its normal bundle with
$\phi^*T_Y$. The first component is the identity, so this calculation
remains valid if $d\phi=0$. Degree of a pulled-back line bundle is
multiplied by the full degree $q$, including inseparable degree.
Consequently $\Gamma^2=q(2-2\gamma)$.

The fiber intersections also use full lengths: $\Gamma F_1=1$,
$\Gamma F_2=q$, and the corresponding diagonal intersections are
one. With

$$
A=\Gamma-qF_1-F_2,\qquad B=\Delta-F_1-F_2,
$$

both classes are orthogonal to $F_1+F_2$. Independent expansion gives

$$
A^2=-2\gamma q,\qquad B^2=-2\gamma,\qquad
AB=N(\phi)-q-1.
$$

The product polarization is ample. Applying Cauchy–Schwarz to the
negative Hodge pairing gives
$|N(\phi)-(q+1)|\le2\gamma\sqrt q$.
If $\gamma=0$, the zero-square orthogonal classes are numerically
trivial, so the same conclusion holds with zero error.

All intersection numbers and the quadratic inequality are numerical
integers or real numbers, not field scalars reduced modulo $p$.
In particular, characteristic two does not erase the factors two in
the intersection calculation. Since $q>1$, graph and diagonal are
distinct irreducible curves and the fixed-point intersection is finite.
Taking $q=d^n$ proves exactly the upper bound used in the report.

## 6. Kummer connectedness, the actual lift, and its degree: PASS

Fix a prime $\ell\ne p$ and a relation $W^\ell=\delta h$,
with $W$ satisfying (CP). If $h=a^\ell$, then
$W/\delta a=\zeta\in\mu_\ell(k)$. Away from the finite union
of support cycles, the products of $\delta a$ telescope, so
$\zeta$ satisfies (CP). Section 3's constant-phase conclusion gives
$\zeta=1$. This settles the split case, including its possible twist.

If $h$ is not an $\ell$th power, $K(y)$ for $y^\ell=h$
contains all roots of the polynomial because $\mu_\ell\subset k$.
The polynomial is separable, and its splitting-field Galois group
injects into $\mu_\ell$. The degree is therefore one or $\ell$;
degree one would contradict the assumed nonpower condition. This proves
irreducibility and connectedness of the cover, not merely its formal
degree before normalization.

The smooth projective curve $Y$ with this function field exists over
the perfect field $k$, and $\pi:Y\to\mathbf P^1$ has degree
$\ell$. The rule $x\mapsto f(x)$, $y\mapsto W(x)y$ respects
the defining relation. It induces a nonzero homomorphism from the
field $L$ into itself and hence an embedding. It fixes $k$ and
corresponds to a genuine morphism $T:Y\to Y$ with $\pi T=f\pi$.

The degree computation does not assume linear disjointness:
$[L:k(f)]=\ell d$, while the embedding identifies
$[\widetilde\sigma L:k(f)]$ with $[L:k(x)]=\ell$.
Thus $[L:\widetilde\sigma L]=d$, including for inseparable $f$.
The lift is the one specified by the given $W$, not an unexamined
root-of-unity twist of it.

## 7. Good fibers and preservation of local multiplicities: PASS

The exceptional set $E$ is a finite union of whole primitive cycles:
the (CP) exceptions, cycles meeting the supports of $W,h$, cycles
meeting the finite branch locus, and infinity. Nonperiodic support
points do not belong to any fixed-point count and need not be added.
This set is fixed before $n$ varies.

On every other cycle of length $r$, the cover is étale and each fiber
has exactly $\ell$ distinct points with finite nonzero $y$-coordinate.
The formula for this actual lift gives multiplication by
$\prod_O W=1$ after exactly $r$ steps. It therefore fixes all
$\ell$ points individually. Setwise preservation alone would not
be sufficient, and is not what is used.

For $r\mid n$, each such point is fixed by $T^n$. At a point
$P$ above $a$, étaleness and the algebraically closed residue field
identify both completed local rings using a base uniformizer.
The identity $\pi T^n=f^n\pi$ then identifies the entire return
germs, not just their multipliers. The lengths of their differences
from the identity are equal. This proves equality of fixed-point
intersection multiplicities without a separability assumption on $T$.

For sufficiently large prime $n\ne p$, the fixed set $E$ contributes
at most a constant $C$ downstairs. Lifting all other fixed points
with their multiplicities gives

$$
N(T^n)\ge\ell(d^n+1-C).
$$

The Hodge calculation gives
$N(T^n)\le d^n+1+2\gamma d^{n/2}$.
Here $\ell$, $\gamma$, $E$, and $C$ are all fixed before choosing
the arbitrarily large primes. Since $\ell>1$ and $d>1$, the
two inequalities are incompatible for large $n$.
Thus the connected nonpower Kummer case is impossible under (CP).

No uniform upper bound for all periodic-root multiplicities was used.
No comparison of distinct-point counts was substituted for the required
length comparison, and no Frobenius-only point-counting theorem was
applied to an arbitrary self-map.

## 8. Removal of every prime-to-$p$ factor: PASS

Writing $m=p^t s$ with $p\nmid s$ and $G=g^{p^t}$, the order
$r$ of $[G]$ in the multiplicative quotient divides $s$.
If $r>1$, take a prime $\ell\mid r$ and put $W=G^{r/\ell}$.
Then $\ell\ne p$, powers preserve (CP), and $W^\ell$ is a
rational multiplicative coboundary. The preceding lemma makes $W$
a coboundary, contradicting minimality of $r$.

Thus $r=1$, giving precisely $g^{p^{v_p(m)}}=\delta b$.
This covers repeated prime factors, $m=1$, and $s=1$; it does not
merely remove one prime from one specially chosen relation.

The equivalence of the report's three existence properties under (CP)
now follows: the minimal-polynomial constant term gives finite transfer
to torsion, the saturation theorem gives torsion to a $p$-power rational
transfer, and the purely inseparable construction gives the converse
finite transfer. Their respective hypotheses are correctly retained.

## Remaining MS6 obligation and work receipt

The only unproved implication in this proposed route is

$$
(\mathrm{CP})\ \Longrightarrow\
[g]\in K^\times/\delta K^\times\text{ is torsion}.
$$

Equivalently under the reviewed conditional result, one must actually
construct a finite forward-stable algebraic transfer. Neither pointwise
fixed vertical fibers, an unspecified iterate with trivial multiplier,
nor an already-algebraic Mahler-series theorem constructs it. The report
keeps these distinctions explicit. The additive PC424-L theorem and the
refuted unsaturated M6 example do not fill the gap.

This review therefore accepts the conditional saturation reduction and
the proved forward implication, while retaining the original MS6 status
as NOT CURRENTLY JUSTIFIED. It does not infer admission or an additional
paper from a correct auxiliary reduction.

Verification used the complete actual report, direct reading of the
specified primary Hodge sources and their relevant proofs, independent
hand intersection/field/local-ring calculations, and read-only hashes.
There were no mathematical executions, external model/API calls, new
agents, Git operations, author-file or shared-state edits, or PDF work.
The only new workspace write by E8 is this allocated review file.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
