# E5 internal nonauthor review: C4 R3 smooth-fold reductions

2026-09-09. Reviewer: `c429_e5_fricke_galois_review`.
This is a current-team mathematical/source review, not external peer review.

## 1. Verdict and exact scope

**Mathematical verdict on the displayed auxiliary propositions:
PROVABLE AS STATED.** The global critical-divisor calculation,
all-smooth-base finite flatness, complete period-two isolation, and
normalized residual criterion survive independent checking.

**SF2: NOT CURRENTLY JUSTIFIED.** Its original all-native-period
quantifier remains intact. None of these reductions proves absence of
ramification at finite genuinely higher-period points over the fold.
FGT remains open. Accepted first-pass FG2 and R2 NI are read-only inputs;
this review does not reopen or replace either accepted theorem.

One determinant-column convention clarification was requested in the
summary report and independently read back as corrected. It changes
no critical locus, proof or conclusion. Final disposition and hashes
are recorded in §9. **Unresolved mathematical/source must-fixes: zero.**

The whole new author package was read, not only its favorable summary:

- [REPORT.md](../../c4_smooth_fold_separation/REPORT.md), all sections.
- [PROOF_PACKAGE.md](../../c4_smooth_fold_separation/PROOF_PACKAGE.md),
  §§0–6, initially 479 lines, plus the final three-line citation delta.
  This is the actual supplement filename; the final file has 482 lines.
- [Accepted FG2](../../../lanes/c4_fricke_galois/REPORT.md), relevant
  §§3.3–3.6, for the exact imported model and complete fold-fibre interface.
- The accepted R2 iterate-ideal and generic reducedness interfaces,
  used without an unnecessary second whole-proof NI review.

### Claim, assumptions and dependency map

Work in characteristic zero on the four-parameter Fricke family
$K=x^2+y^2+z^2-xyz-Ax-By-Cz=D$, with the ordered native return
$T=s_zs_ys_x$, rightmost first. The base is the full
$\mathbb A^4_{\overline{\mathbb Q}}$, and $B^{\rm sm}$ excludes
singular fibres. The fixed scheme $\mathcal X_n$ includes multiplicity;
$P_n$ denotes ordinary generic points of exact least native period $n$.

The rational cycle map $\Phi$ and its accepted fold at
$c_f=(2/3,3/2,3/2,3/2)$ over $b_f=(0,0,0,-9/4)$ are imported.
The divisor $\mathscr F$ is the reduced image closure of its full
finite-chart critical hypersurface. The proof dependencies are:

1. Explicit Jacobian algebra and Gauss's lemma identify one irreducible
   critical hypersurface; the accepted simple fold identifies its
   image dimension and odd cycle-sign inertia.
2. Every-smooth-fibre intersection lengths give quasi-finiteness;
   the local complete intersection gives flatness; constant length
   plus the precise finiteness lemma gives finiteness.
3. The entire accepted period-two fibre, residue-form invariance and
   finite closed resonance images exclude nontrivial root-of-unity
   multipliers over the generic fold.
4. The parameter-family iterate ideals then exclude every
   higher-period specialization into the period-two part.
5. Henselian finite-algebra decomposition isolates the residual point
   algebras. Their normalized ramification is exactly the remaining SF2 test.

## 2. Critical hypersurface and actual global fold

The determinant calculation in package §1 uses columns $(X,Y,Z,q)$.
I checked its block expansion, including the polynomial adjugate step,
so no unmentioned inversion of the upper-left block is required.
For $S=X^2+Y^2+Z^2$, $P=XYZ$ and
$Q=X^2Y^2+Y^2Z^2+Z^2X^2$, it gives
$$
r=(1-6q)P-S+qQ+q^2(S^2+PS-4Q)+q^3P^2.
$$
For example, writing $H$ for the off-diagonal symmetric matrix in the
package, $Hv=2g$ and
$\operatorname{adj}(I-qH)=I+qH+q^2(H^2-SI)$ verify the three
displayed contractions and the final block determinant directly.

On $q\ne0$, the coordinate change $(a,b,c)=(qX,qY,qZ)$ gives
$q^3r=U+qV$. The factorization
$U=(ab+c)(ac+b)(bc+a)$ is correct. Its three factors are irreducible,
pairwise nonassociate over $\overline{\mathbb Q}$. Restricting to
$ab+c=0$ and then $a=c=0$ leaves $V=b^2(b^2-1)$, a nonzero
polynomial. Cyclic versions exclude the other two factors. Thus
$\gcd(U,V)=1$, not merely a coprimality assertion at a single point.

Gauss's lemma now applies to the primitive linear polynomial in $q$.
Localization cannot make it a unit or split it: it is not associated
to $q$. Conversely, a factor lost on returning to the original chart
could only be a power of $q$, excluded by $r|_{q=0}=P-S\ne0$.
This checks geometric irreducibility of the **entire** affine critical
hypersurface, including possible components in the omitted locus.
On its dense open where the displayed rational expression is defined,
$q=-U/V$ proves rationality as claimed.

The image closure is irreducible and has dimension at most three.
The accepted simple-fold germ supplies dimension three, so it is an
actual divisor. Since $b_f$ is a smooth-fibre parameter, this divisor
is not the singular-fibre divisor. All four critical points lie in the
same irreducible source, hence their four analytic branch graphs lie
in the same algebraic image divisor. An irreducible algebraic divisor
may have several local analytic branches at one singular point.

The accepted local cycle-degree exhaustion is $4\cdot2+3=11$.
A meridian avoiding the other local branches transposes just one
pair of cycle sheets. The phase cover is unramified there because
$1-4q_f=-5/3\ne0$. This witnesses odd generic cycle sign along
$\mathscr F$; it is not an inference from the discriminant of an
uncontrolled line section. No assertion that all compactified-chart
branch divisors have been classified is being approved.

## 3. Every-smooth-fibre length and complete-intersection flatness

I checked the actual smoothness setup and proof passages in
[Iwasaki–Uehara, §§5, 7–8](https://arxiv.org/pdf/math/0512583v3):
Lemma 5.1, Proposition 7.7, and Lemmas 8.1–8.3. The smooth projective
cubic setup applies to every smooth affine fibre. The source excludes
periodic curves, computes graph/diagonal intersection, and subtracts
two boundary terms of length one. This justifies the affine length
$a_n=(2+\sqrt5)^n+(2-\sqrt5)^n+4(-1)^n$ for every such fibre.
It does **not** justify reading the source's cardinality notation as
ordinary reducedness at all parameters. The author's sign conversion
and native Coxeter clock are correct; the Painlevé return is its square.
Reversing the word exchanges the graph factors and preserves the
intersection calculation. Extension of algebraically closed fields
preserves the zero-dimensional scheme lengths used here.

The flatness argument does not assume finiteness. The relative diagonal
of the smooth relative surface is locally defined by two equations.
Pulling back by the graph gives two local defining equations for
$\mathcal X_n$ in a regular total space of dimension six. At a closed
point their common zero scheme has dimension at least four by height,
and at most four by quasi-finiteness over the four-dimensional base.
Thus the two equations have height two and form a regular sequence.

The local ring of $\mathcal X_n$ is therefore Cohen–Macaulay of
dimension four. Its base local ring is regular of dimension four,
with zero-dimensional fibre. These are exactly the three hypotheses
of [miracle flatness, Stacks 00R4](https://stacks.math.columbia.edu/tag/00R4).
The resulting flatness at closed points extends everywhere because
the finite-presentation flat locus is open and a nonempty closed
subset in this finite-type setting has a closed point. Empty
$\mathcal X_1$ is handled separately by its zero length.

## 4. The quasi-finite-to-finite upgrade is valid

This was a specific review target: constant point count or
quasi-finiteness alone would be insufficient. The proof uses
constant geometric **scheme length**, separatedness, flatness and
finite presentation, and it supplies the missing finiteness step.

The author's strict-henselian argument is valid. After
[Zariski's main theorem, Stacks 05K0](https://stacks.math.columbia.edu/tag/05K0),
one takes the schematic closure of the generic fibre in a finite hull.
Flatness over the normal local domain ensures schematic generic
density inside the original open subscheme. The resulting finite
algebra is torsion-free, with generic rank $d$.

Its henselian product decomposition has local finite factors. Each
factor whose closed point is retained is retained in full and is
flat. The ranks of these retained factors already sum to the
closed-fibre length $d$. Every nonzero omitted factor would have
positive generic rank by torsion-freeness, contradicting total rank
$d$. Thus no omitted factor remains. Finiteness descends and finite
flatness gives the asserted locally free rank. In particular, this
argument does not replace the hull's possibly larger special length
by its generic rank without justification.

There is also an exact independently accessed theorem:
[Stacks 07RY](https://stacks.math.columbia.edu/tag/07RY) and
[Stacks 07RZ](https://stacks.math.columbia.edu/tag/07RZ).
For a separated, flat, locally finitely presented quasi-finite map,
they stratify the base by fibre degree so that each corresponding
base change is finite locally free. With constant fibre length all
points belong to one stratum. I read both complete proofs, including
the finite clopen part and maximal-degree argument. The needed
statement therefore is not an unsupported invocation of a vaguely
named theorem. The author added this precise citation in the final
revision; the author's full proof already sufficed independently.

[Conrad's Math 248B Homework 8](https://virtualmath1.stanford.edu/~conrad/248BPage/homework/hmwk8.pdf),
Exercise 2(iv), really states the cited flat constant-fibral-degree
finiteness lemma and attributes it to Deligne–Rapoport. It is not a
published proof supplied by the homework itself; the author correctly
writes the argument actually used.

Consequently every $\mathcal X_n\to B^{\rm sm}$ is finite flat
of rank $a_n$. All generic sheets specialize finitely over valuations
centered on this base. This excludes escape, but neither nonreduced
special fibres nor normalized ramification at finite points.

## 5. Complete period-two multiplier test

The residue two-form is nowhere zero on each smooth fibre. The three
involutions negate it, so $T^2$ preserves it and its vertical
two-dimensional return determinant is one.

At each of the eight doubled ordinary points over $b_f$, the accepted
dual-number local algebra has tangent dimension one. Thus the
vertical $DT^2-I$ has a kernel; determinant one forces both return
eigenvalues to be one. This conclusion does not require diagonalizability.

For an axis point $(x,0,0)$, differentiating the three ordered steps
gives the two matrices printed in the package. Their product is
$$
\begin{pmatrix}1+x^2&x^3\\x^3&x^4-x^2+1\end{pmatrix},
\qquad \det=1,\qquad \operatorname{tr}=x^4+2.
$$
Since $x^2=D=-9/4$, the trace is $113/16>2$. Although $x$ itself
is not real, the characteristic polynomial has two positive real
reciprocal roots different from one; neither can be a root of unity.

For the other axes, the claimed symmetry is an actual symmetry of
the unforced ordered map: $r_0s_xr_0^{-1}=s_z$,
$r_0s_yr_0^{-1}=s_x$, and $r_0s_zr_0^{-1}=s_y$ give
$r_0Tr_0^{-1}=s_zTs_z$. Thus $s_zr_0$ commutes with $T$ and
cycles axis pairs. This avoids importing a false arbitrary-forcing
coordinate-permutation symmetry. The full special-fibre test covers
eight doubled points plus six simple axis points, length
$8\cdot2+6=22$; no omitted axis sheet is ignored.

For each fixed root of unity $\zeta\ne1$, the determinant defining
its vertical eigenvalue locus is a regular function in local bundle
trivializations and hence gives a closed locus on $\mathcal X_2$.
Its image is closed by finiteness, and the complete special-fibre
calculation shows that it misses $b_f$. Since $\mathscr F$ is
irreducible and contains $b_f$, this image cannot contain its generic
point. This works separately for every $\zeta$; no unjustified
intersection of infinitely many open neighborhoods is taken.

## 6. Family iterate ideals and exclusion of lower-period limits

The telescoping identity uses state-coordinate divided differences
with parameters left fixed. At a fixed state its matrix has value
$\sum_{j=0}^{m-1}(Df)^j$. For $f=T^2$, the preceding multiplier
test makes it invertible: the scalar at eigenvalue one is $m\ne0$,
and at a non-root of unity it is $(\lambda^m-1)/(\lambda-1)\ne0$.
Jordan blocks do not change this determinant criterion.

The ambient three-coordinate version is legitimate. Preservation
of $K$ and $dK\ne0$ give one normal quotient eigenvalue equal to
one in addition to the two vertical eigenvalues. Hence the ambient
telescoping matrix is invertible too, and the ideal equality survives
restriction to $K=D$. It is equality of **parameter-family local
ideals**, not only equality of central-fibre point sets.

It follows that at every period-two point over the geometric generic
fold, $\operatorname{Fix}(T^{2m})$ and $\operatorname{Fix}(T^2)$
have the same germ for all $m$. An exact higher-period generic branch
cannot specialize there. Odd iterates cannot fix a least-period-two
point; smooth fibres have no period-one points. Proposition 4.1
therefore covers every point of least period at most two, including
the noncolliding two-cycles.

## 7. Residual normalization criterion, not a proof of SF2

Over the strict henselization of the DVR at $\eta_{\mathscr F}$,
the finite schemes decompose by special-fibre points. Local ideal
equality makes $\mathcal X_2$ an open-and-closed part of even
$\mathcal X_n$. Its complement $\mathcal Z_n$ is finite flat
of rank $a_n-22$; for odd $n$ it has rank $a_n$. Every special
point in the complement has native least period at least three.

Accepted generic reducedness identifies its generic algebra with
the point algebras for $P_d$, $d\mid n$, $d\ge3$. Normalization
is finite by excellence. Unramified finite extensions of a henselian
DVR field are closed under conjugation, subextensions and finite
composita. Consequently all these normalized residual algebras are
étale for every $n\ge3$ if and only if the corresponding splitting
fields are unramified. This validates both directions of (15).

The stronger derivative condition (16) is sufficient, not necessary.
The examples $z^2-t^2$ and $z^2-t$ correctly distinguish an
unramified normalization of a nonreduced raw special fibre from a
ramified normalization. No Fricke realization of either example is
claimed. Constant length alone decides neither behavior.

Any remaining ramification must therefore occur at a finite
least-period-$d$ point with $d\ge3$. A higher exact-period
specialization $n>d$ requires a nontrivial root-of-unity multiplier
for the $d$-return; eigenvalue one alone would leave the iterate
ideals unchanged. Same-period collision can instead have eigenvalue
one. These are necessary conditions, not an exhibited shared branch
divisor and not a refutation of SF2.

## 8. Source ownership and substantive increment

The author's source subtraction is adequate for these auxiliary
claims. The rational model, local fold, degree and fibre inventory
belong to accepted FG2. The ordinary generic reducedness and local
iterate identity belong to accepted R2. Classical intersection
theory and commutative algebra are credited rather than presented
as new stand-alone results. The new assembly strengthens the
available all-period interface without closing a full paper contract.

I also accessed
[Cantat, *Bers and Hénon, Painlevé and Schrödinger*](https://arxiv.org/pdf/0711.1727v2),
Theorem 1.2 and relevant §§5.3.1–5.3.3. The real connected-fibre
hyperbolic regime and its deformation discussion do not provide the
missing complex generic-fold ramification result. In the unforced
line the stated real regime is $D\ge4$, whereas here $D=-9/4$;
the orientation-preserving reduction and singular-period warning
also cannot be dropped when transporting native periods. No broader
claim that the literature contains no such theorem is certified.

The local relevant-name search found no matching primary PDF and
no configured Zotero/Obsidian tool. Primary web documents were read
directly; no missing library or script was treated as evidence of novelty.
No mathematics program, numerical census, old checker, PDF build,
external model/API review, or additional child agent was used.

## 9. Issue disposition and final binding

**Closed notation clarification:** the package defines
its Jacobian using columns $(X,Y,Z,q)$, while the initial report
printed $q^3\det D\Phi$ without that convention next to domain
coordinates $(q,X,Y,Z)$. The conventions differ by sign. The author
has now labeled the report's ordering explicitly, and the reviewer
read back the corrected formula in context. This has no effect on
irreducibility, branch divisors or any proposition above. The author
also added Stacks 07RY–07RZ after Lemma 2.1 and in the source table;
both additions were read back against the independently accessed
theorems. No mathematical weakening or unrequested change was needed.

Final reviewed author files, confirmed stable by the author and
independently measured after the notation/citation readback:

| Artifact | Lines | SHA256 |
| --- | ---: | --- |
| REPORT.md | 156 | `602cc667009f3ddec859819c31bd6980e0807dcc7de80357128d653ab8009283` |
| PROOF_PACKAGE.md | 482 | `2659276b7ccdd73847ebfe131ab1c34fbf300a1e002922d5c88e7b65654d73d7` |

These hashes were independently read from the files; they bind
reviewed bytes and are not mathematical evidence. The initial
479-line package and 156-line report were read in full, then every
reported changed passage was independently read back. Final status:
**zero unresolved mathematical, source-applicability or notation
must-fixes in the auxiliary claims; SF2 and FGT remain open.**

Only this exclusive review file was written. Author files, shared
indexes, accepted earlier-round files, manuscripts, PDFs, evaluator
artifacts and Git were left untouched by the reviewer. The proof-writer
skill enforced separate statuses for proved auxiliary claims and
unproved SF2; research-review was used as a current-team internal
check under the repository workflow, without its historical external
model examples. Research-lit supplied the primary-source scope check.

**Coordinator handoff:** retain the proved auxiliary statements,
preserve the exact finite higher-period normalized-ramification gap,
and do not infer SF2, FGT, higher-layer maximal groups, cycle-character
independence, constant-field independence, target arithmetic or an
additional admitted paper from this package.
