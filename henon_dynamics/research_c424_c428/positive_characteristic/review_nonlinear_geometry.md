# Bounded nonauthor review of the nonlinear-geometry scout

2026-09-08 UTC. This is a screening-evidence review, **not** admission,
formal Route-A evaluation, human peer review or a new mathematical
classification. The reviewer did not author the two documents reviewed.
No author file was edited.

## Actual read scope and initial snapshot

Read in full:

- [FROZEN_SCOUTS.md](../nonlinear_geometry/FROZEN_SCOUTS.md), 95 lines,
  SHA-256 f06ba57b97a767f677ea2c358e1d48d6754a57f9344548ad405d7ec1db25b72c.
- [SCOUT_REPORT.md](../nonlinear_geometry/SCOUT_REPORT.md), 218 lines,
  SHA-256 cb8aea9363b168c84cfd008fbd971c39afcc939e050c7e02c8fcebdc57ed3d9d.

The checks below are hand verification of the displayed formulas and
logical scope. No parameter census, symbolic program, old mathematics,
PDF build or formal evaluation was run. The hash operation identifies
the reviewed documents and is not a mathematical experiment.

Only one external source was reopened: Hu–Tan–Zhang,
[arXiv:1501.06955v2 HTML](https://arxiv.org/html/1501.06955v2),
internal version date 6 May 2015, selected Sections 2.5 and 2.6.
Other source-access records in the report were read as the author's
records, not independently reenacted or upgraded to reviewer full-text
reads. The earlier library and C421 proof package were not reread.

The research-review skill supplied the logical-gap and claim-scope
checklist. The assigned current-team bounded review overrides its legacy
external-model/multiround/ML-score examples; no external model transport,
venue score, experimental recommendation or extra reviewer is claimed.

## Overall finding

The displayed maps, inverses and elementary channel checks are correct
on the stated domains. In particular, the two-zero signed-rotation
argument and the claimed nonzero $n=4$ least period $8$ survive review.
The present dispositions are proportionate: NL424-1 is rejected as a
current paper proposal, while NL424-2 and NL424-3 remain unclosed.
None is a theorem of universal impossibility.

The initial snapshot has **one required contract clarification before
reopening NL424-3**: its requested invariant fibres are not specified by a
full invariant map. This does not require reversing its nonadmission.
The coordinator subsequently supplied a formula whose algebra is checked
below. The final addendum verifies its actual incorporation into both
author documents: **M1 is resolved, with zero remaining required changes
for this bounded screening review.** The research questions remain unclosed.

## Required clarification

### M1 — define the fibre object in NL424-3 before further fibre work

Location in initial snapshot: frozen document lines 70–76 and 82–85;
report lines 77–81.

The contract asks for rational invariant fibres, including singular
fibres, while the only invariant explicitly defined is
$S=x_1+x_2+x_3$. The fibres of $S:\mathbb A^3\to\mathbb A^1$ are affine
planes; restricting to the regular domain does not turn this into the
intended elliptic fibration. Thus the later smooth/singular elliptic-fibre
and torsion language depends on an additional invariant or invariant
pencil which the frozen document does not identify.

Before reopening this question, specify the full rational invariant map
$\mathcal I_\beta$, or its polynomial pencil/level equations, and what
“fibre” means when parameters coincide, invariants become dependent,
levels are reducible/nonreduced, or rational formulas have poles.
Preserve the declared native factorwise regular domain; do not
silently replace it by a compactification or root-transfer domain.

This is a precision requirement, not a request to complete the unsolved
classification during screening. The ordinary periodic-point and
native-clock parts are already well-defined. The conclusion that the
full classification is unproved remains valid.

### Coordinator-supplied repair: algebra and actual landing verified

The supplied invariant is
$$
H_\beta=(x_1+x_2)(x_2+x_3)(x_3+x_1)
+\beta_1(x_2+x_3)+\beta_2(x_1+x_3)+\beta_3(x_1+x_2),
\qquad \mathcal I_\beta=(S,H_\beta).
$$
This formula is correct for the stated fixed-site parameters.
For one two-site operation, write its coordinates as $(u,v)$, the third
as $w$, its parameters as $(b,c)$ and the third parameter as $e$.
Set $s=u+v$ and $d=b-c$. Then
$$
H=s(uv+ws+w^2)+bv+cu+(b+c)w+es.
$$
For $s\ne0$, the displayed Adler formula gives
$$
u'v'-uv=\frac{d(v-u)}s-\frac{d^2}{s^2},\qquad
b(v'-v)+c(u'-u)=d(u-v)+\frac{d^2}s.
$$
Multiplication of the first identity by $s$ and addition of the second
gives zero. Since $s,w$ are unchanged, $H$ is preserved. For $b=c$,
the operation is an everywhere-regular swap and the same invariance is
polynomial symmetry, including $s=0$. Relabeling the two affected sites
proves the statement for each factor of the transfer.

Consequently the proposed common affine levels of $(S,H_\beta)$ are a
well-defined invariant object. This does not assert that all levels are
elliptic, smooth, irreducible, nonempty in rational points, or classified.
No rational-periodic-point conclusion follows from this repair alone.

## Formula, domain and quantifier checks

### NL424-1

The inverse $(x,y)\mapsto(y,f_{a,b}(y)-x)$ composes with the stated map in
both orders to the identity. At $x=0$ the two linear formulas coincide,
so the declared axis convention is consistent. Integer parameters
preserve the full lattice; no deleted-origin or ray quotient is introduced.

Positive homogeneity is the correct property: negative rescaling can
switch branches, so oddness is not valid for general $a,b$.
For $a=2$ and every positive integer $t$, substitution gives
$T_{a,b}(t,t)=(t,t)$ independently of $b$. This verifies the report's
distinction between neutral periodic rays/points and global finite order.

The source/global-order discussion is not asserted to classify every
individual periodic lattice point. Rejecting the present proposal because
no substantial residual theorem was produced is consistent with its
frozen full-atlas quantifiers.

### NL424-2

Let $P=\prod_{j=2}^n x_j$ and $x_1'=P+a-x_1$. Before the cyclic
permutation, the difference of the two invariant values factors as
$$
K(x_1',x_2,\ldots,x_n)-K(x_1,x_2,\ldots,x_n)
=(x_1'-x_1)(x_1'+x_1-P-a)=0.
$$
Permutation invariance of $K$ finishes the check. This polynomial
identity includes every invariant level and singular point; no
smoothness or division is used. The displayed inverse recovers
$x_1=P+a-y_n$ and then all remaining coordinates, so it is valid on
all of $\mathbb Z^n$.

At $a=0$, at least two zeros ensure that every product excluding the
first coordinate vanishes. A zero first coordinate leaves another zero;
a nonzero first coordinate leaves both. Replacing the first coordinate
by its negative and rotating preserves the number of zeros, so the
argument is invariant under iteration. Thus the restriction is $J$,
and $J^n=-I$, $J^{2n}=I$ give the claimed divisibility of least periods.

For $n=4$ and $(0,u,0,v)\ne0$, $J^4x=-x\ne x$ over the integer lattice.
Since every proper divisor of $8$ divides $4$, no proper divisor can be
the least period. Together with $J^8x=x$, this verifies least period
$8$ and the displayed scalar word, including $u=0$ or $v=0$ separately.
The zero vector has period $1$, as the report's hypothesis correctly
excludes it from the period-$8$ assertion.

The short $n=3$ difference identity follows from the displayed
three-term recurrence: subtract the relations solving for
$x_{i+3}$ and $x_{i-1}$ to get
$x_{i+3}-x_{i-1}=(x_{i+1}+1)(x_{i+2}-x_i)$.
This checks that identity, not the full previously proved C421
classification or a new all-dimensional extension.

The zero channel refutes a single height box covering all periodic
points at the fixed pair $(n,a)=(4,0)$. It does **not** refute a bound
depending on the invariant level, nor a finite residual core after
all unbounded channels have been separately classified. The report
does not make either stronger claim.

### NL424-3

Writing $d=b-c$ and $s=u+v$, the two-site map preserves $s$.
Solving the output equations gives the inverse displayed in the report.
In fact this inverse is the same two-site formula:
$R_{b,c}^2=I$ on its declared regular domain.

Consequently the inverse of the ordered native transfer is
$$
T_\beta^{-1}
=R_{\beta_1,\beta_2}^{12}\circ R_{\beta_1,\beta_3}^{13},
$$
with the site parameters fixed and the intermediate regularity checks
performed in reverse order. This is consistent with the frozen forward
order $R^{13}\circ R^{12}$ and its one-whole-transfer clock.

The equal-parameter convention cancels $d=0$ before imposing a pole
restriction, so an equal pair is a swap even when $u+v=0$. If all three
parameters coincide, the whole transfer is $(x_3,x_1,x_2)$ on all of
$\mathbb Q^3$. Its period classification in the report is correct.

The explicitly **factorwise** two-sided regular domain is a coherent
choice. It should not be conflated with a possibly larger regular locus
of a simplified rational expression for the entire transfer. No such
enlargement is made in the reviewed text. Replacing the transfer by a
root/extended transfer changes the clock and is correctly disallowed.

## Source-role check

Hu–Tan–Zhang Section 2.5 uses the unforced Vieta relation, and Section
2.6 defines a dihedral Hurwitz map by two distinct zero coordinates at
a vertex. This supports the report's narrow attribution of the
unforced two-zero locus. It does not provide the forced $a\ne0$ cyclic
exhaustion theorem, and the report correctly refrains from that inference.
[Verified primary section](https://arxiv.org/html/1501.06955v2).

For the other sources, this bounded review confirms that the author
distinguishes generic integrability, ray/global order, group-orbit
counting and partial-text access from the requested native periodic-point
classifications. It does not independently certify every source theorem
or worldwide novelty. No source mismatch found here supplies a reason
to upgrade any question to admission.

## Suggestions, not screening blockers

1. Frozen NL424-2 line 54 says the two-zero channel is “below”, but the
   explicit channel appears in the separate report. Replace that word
   with a link to report Section 2 when author metadata is next edited.
2. For NL424-2, the invariant-difference identity above avoids a possible
   literal reading of “the roots of $K$” as restricted to level zero.
   Alternatively say “the roots of $K-\kappa$”.
3. The one-line argument $J^4x=-x\ne x$ makes the least-period-$8$
   check shorter and displays the characteristic-zero lattice assumption.
4. For NL424-3, explicitly writing the reverse composition in the
   report would make the two-sided domain check easier to reproduce.

## Actual-revision addendum

After the coordinator's edit, both author files were reread **in full**:

- Revised frozen document: 106 lines, SHA-256
  a44743719d556af4683075113306fc703fb2d8c93010f51b09aac9415512b588.
- Revised report: 238 lines, SHA-256
  95a452c7c1e6105fa94732643a882f5d79cc8a4cb999fed8295063b83e8cadf9.

The frozen document now explicitly defines $\mathcal I_\beta=(S,H_\beta)$
and all full affine levels at rational level values, includes singular
levels and ordinary points meeting the unchanged native domain, keeps
coincident parameters, and disclaims normalization or universal
ellipticity. The report includes the two-site cancellation proof and the
equal-parameter $s=0$ branch. These are the same identities checked above.
Thus M1 is **RESOLVED IN ACTUAL DOCUMENTS**, not merely promised.

No new mathematical program, external source or library reread was used
for this verification. Optional suggestions remain optional. The existing
three dispositions and zero-admission count are unchanged.

## Handoff boundary

No finding overturns zero admissions or justifies a manuscript.
There are no remaining required changes from this bounded evidence review.
The other observations are optional clarity changes, and the missing
classification theorems remain missing. This review is limited to its
identified initial and revised snapshots; later edits are not covered.
