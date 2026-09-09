# R4 E3: review of the exact local quadratic inventory

2026-09-09 UTC. Current-team nonauthor mathematical and bounded
source-applicability review of D2's complete R4
[report](../../d2_slice_quadratic_exclusion/REPORT.md) and
[proof package](../../d2_slice_quadratic_exclusion/PROOF_PACKAGE.md).
This is not a paper-admission assessment or a multi-model review.

## Verdict and binding

**Propositions 1–5: PROVABLE AS STATED at their stated auxiliary
scope. Zero open mathematical or source-applicability must-fixes.**

The complete quadratic inventory, tame finite-compositum index,
and both types of controls pass independent hand checking.
The condition OI is sufficient for ST, but is not proved for any
actual all-period Fricke tower in this package. ST and original
SF2 remain **NOT CURRENTLY JUSTIFIED**. Recommend auxiliary
acceptance only; no paper admission follows.

The verdict binds the following complete author files, whose
SHA-256 hashes were independently checked:

```text
REPORT.md
1923f670aa24f108b2bc789eee85c9c56ced962480b154195a4c73e636a7d019

PROOF_PACKAGE.md
5e8c9890bc9031f056872df8afac19611c1378cd93dbde70fd78d269a3ebbc6b
```

R3's actual sign class, whole-cover specialization and odd-period
symmetry are accepted inputs, not reopened proofs. The native
word remains $T=s_zs_ys_x$, one whole right-to-left word per tick.
All first-pass and R2/R3 files remain untouched. C4's separate
global-fold/remote-sheet argument is not an input to this review.

## 1. Fields, completions and hypotheses

The parameter $C$ stays transcendental. At $D=\varepsilon C$,
the chosen uniformizer is $t=D-\varepsilon C$ and the residue
field is $\kappa=\mathbb Q(C)$, not $\mathbb Q$. The completed
base is $F_\varepsilon=\kappa((t))$.

Each $E_{n,\varepsilon}=F_\varepsilon M_n$ is a completed local
factor of the whole global splitting field. It is finite Galois
over $F_\varepsilon$ even if the global tensor product has more
than one factor. A compatible choice of embeddings defines their
joint field $H_{N,\varepsilon}$. Galois conjugacy makes the
conditions independent of which compatible place is used.
None of this requires good reduction at the sign divisor.

Every finite residue extension here has characteristic zero and
is therefore separable; both $\mathbb Q(C)$ and
$\overline{\mathbb Q}(C)$ are perfect. Completeness gives a
unique extension of the valuation. Thus the proof may use
cyclic tame inertia with order equal to the ramification index,
including for relative extensions inside a finite compositum.
Perfectness is not algebraic closedness: $C$ remains nonsquare
over $\overline{\mathbb Q}(C)$.

## 2. Proposition 1: the exact unit and both branch signs

For $F=\kappa((t))$, any unit divided by its nonzero residue
has residue one and a square root by Hensel lifting. Conversely,
a square has even valuation, and a constant unit square in $F$
reduces to a square in $\kappa$. Therefore, with the displayed
coefficient field and uniformizer,

$$
F^\times/F^{\times2}
\simeq\kappa^\times/\kappa^{\times2}\oplus\mathbb F_2.
$$

Substitution gives

$$
D^2-C^2=t(2\varepsilon C+t)
=(2\varepsilon C)t\left(1+\frac{t}{2\varepsilon C}\right).
$$

The final factor is a square. Hence the target is $[2Ct]$ at
$D=C$ and $[-2Ct]$ at $D=-C$, with exactly these uniformizers.
No branch sign or residual unit may be dropped over $\mathbb Q(C)$.
The valuation at $C=0$ proves $2\varepsilon C$ nonsquare over
both stated residue fields. Extending constants can kill a
numerical factor such as $-1$ or $2$, but cannot kill this
functional squareclass.

## 3. Proposition 2: why the index is an lcm

Fix a finite $N$ and abbreviate $H=H_{N,\varepsilon}$,
$E_n=E_{n,\varepsilon}$ and $F=F_\varepsilon$.
The proof correctly uses the cyclic group $I(H/F)$, not the
whole decomposition group, which need not be cyclic.

Restriction maps inertia into $I(E_n/F)$. Its kernel is
$I(H/E_n)$: it consists of automorphisms fixing $E_n$ and
acting trivially on the residue field of $H$. The relative
extension is Galois. Since inertia orders equal indices and
indices multiply, this kernel has order

$$
|I(H/E_n)|=e(H/E_n)=\frac{e(H/F)}{e(E_n/F)}.
$$

Thus restriction is onto each $I(E_n/F)$. The simultaneous
map to their product is injective because the $E_n$ generate
$H$. If $\tau$ generates the joint cyclic inertia, each
projection has order $e(E_n/F)$, so the tuple has order
$\operatorname{lcm}_n e(E_n/F)$. Injectivity gives exactly

$$
e(H/F)=\operatorname{lcm}_{3\le n\le N}e(E_n/F).
$$

A product of indices would generally be wrong. The argument
does not assume linear disjointness, disjoint residue fields,
or independent inertia factors.

If every whole-layer index is odd at one fixed sign branch,
this formula gives odd joint index for every finite $N$.
A global target inclusion would imply a local inclusion of
$F(\sqrt{2\varepsilon Ct})$, an Eisenstein quadratic extension
of index two. Multiplicativity contradicts the odd joint
index. This proves OI$\Rightarrow$ST, separately for the
arithmetic and geometric completed bases.

The quantifier is important: OI requires odd inertia index for
**every $n\ge3$, including even native periods**, at one fixed
choice of $\varepsilon$. The symmetry controls below concern
odd $n$ only and do not supply that missing assertion.

The full-point interpretation also passes. A splitting-field
action on all coordinate points is faithful. The inertia
generator's order is the lcm of its permutation-cycle lengths,
so it is odd exactly when every such length is odd. Positive
point sign says only that the number of even-length cycles
is even; it does not prove odd inertia order.

## 4. Proposition 3: all quadratic subfields, not selected signs

For any finite Galois $E/F$, the kernel
$V(E/F)\subset F^\times/F^{\times2}$ parametrizes all its
quadratic subfields, together with the identity class. If
$b\in\kappa^\times$, then $b$ is square in $E$ exactly when
its residue is square in $\kappa_E$. One direction is reduction
of a unit square root; the other is Hensel lifting in the
complete valuation ring of $E$, where the derivative is a
nonzero residue because the characteristic is zero.

Thus the even-valuation part of $V$ is exactly the specified
kernel $U$. The parity image of the subgroup $V$ is either
zero or all of $\mathbb F_2$. In the latter case, selecting
one odd class $[at]$ gives

$$
V=U\sqcup[at]U.
$$

This is a complete inventory statement. The representative $a$
may change by an element of $U$, but the coset does not. A
nontrivial unit class gives an unramified quadratic extension,
whereas an odd class gives a ramified quadratic extension.
Accordingly, the ramified coset exists exactly when some
character of the **actual whole group** $\operatorname{Gal}(E/F)$
is nontrivial on inertia.

In that case $[2\varepsilon Ct]\in V$ is equivalent to
$[2\varepsilon C/a]\in U$, or to $2\varepsilon C/a$ being
square in $\kappa_E$. The test therefore retains both the
ramification parity and its residual-unit ambiguity.

No proof identifies the joint inventory with the span of
individual inventories or with the native phase/cycle signs.
No extension of a character from inertia to the whole group
is presumed. Even inertia is necessary for a ramified quadratic
subfield but, as Proposition 5 shows, is not sufficient.

## 5. Proposition 4: model rank, labels and signs

For any nonzero $u\in\kappa$, the Eisenstein ring
$R_u=R[w]/(w^2-ut)$ is $\kappa[[w]]$ with $t=w^2/u$.
It is a complete normal DVR and finite free of rank two over
$R$. Consequently

$$
\mathcal A_u=R_u^{2n}\times R^{2n(s-2)}
$$

is finite flat and normal, of rank
$4n+2n(s-2)=2ns$. When $s=2$, the split factor is omitted.
Normality does not mean its special fibre is reduced or that
the cover is étale at $t=0$; neither stronger property is claimed.

The factor index $j$ ranges over $\mathbb Z/(2n)$; the sign
$\delta$ labels the two embeddings of each quadratic factor.
They are different roles. The permutation $h(j,\delta)=(j+1,\delta)$
comes from a cyclic permutation of the factors. On the coordinate
ring one uses the inverse permutation, as usual for the induced
point action; this convention changes none of the equations.
The remaining split factors supply $s-2$ further $2n$-orbits.

Since $n$ is odd, $\gcd(2n,n+1)=2$. Therefore
$T=h^{n+1}$ has exact period $n$ on every generic point,
$g=h^n$ is fixed-point-free of order two, and
$gT=h^{2n+1}=h$. There are $s$ free $h$-orbits and $2s$
native cycles. All these actions extend to the finite flat model.

The entire point algebra splits over $E_u=F(\sqrt{ut})$ and
requires that field. Its nontrivial Galois element changes
$\delta$ while fixing $j$, and is the full inertia generator.
Its point action has $2n$ transpositions, hence positive sign.
Its native-cycle action exchanges the two even-$j$ cycles and
the two odd-$j$ cycles, hence has two transpositions and positive
sign. Its $h$-orbit action is one transposition, hence has
negative paired-orbit sign. The unaffected split factors add
only fixed labels. All counts and signs hold also for $s=2$.

For $u=1$ the splitting field is $F(\sqrt t)$; for
$u=2\varepsilon C$ it is exactly the target. These quadratic
fields are distinct because their ratio class $2\varepsilon C$
is nonsquare. Both have index two, residue $\kappa$, and the
same abstract permutations. The distinction persists over
$\overline{\mathbb Q}(C)((t))$.

These are normal finite flat full-point controls, not actual
Fricke periodic schemes. Choosing $s=s_n$ matches only the
accepted cardinality and listed free-action structure. The
authors do not claim their model satisfies the surface equation,
Vieta return or actual inertia signs. The controls refute an
inference from the listed data alone, not ST or SF2.

## 6. Proposition 5: the cyclic quartic and constant extension

Here the letter $s$ is a root of $s^2=2$, not the integer
orbit count used in Proposition 4. Over $F=\mathbb Q(C)((t))$,
$F(s)/F$ is unramified quadratic, since $2$ is nonsquare in
$\mathbb Q(C)$. Over $F(s)$, the equation
$w^2=(2-s)Ct$ is Eisenstein. Thus the total degree is four,
the ramification index is two and the residue field is
$\mathbb Q(C)(s)$.

The proposed automorphism checks exactly:

$$
(1+s)^2(2-s)=2+s,\qquad (1-s)(1+s)=-1.
$$

Hence $\sigma(s)=-s$, $\sigma(w)=(1+s)w$ preserves the
relations and satisfies $\sigma^2(w)=-w$. It has order four,
so $E/F$ is Galois with group $C_4$. Its inertia is
$\langle\sigma^2\rangle$, and its only quadratic subfield is
the unramified $F(s)$. Every quadratic character kills inertia.
In the notation of Proposition 3 this gives
$V(E/F)=U(E/F)=\{1,[2]\}$, with no ramified coset.

After base change to $\overline F=\overline{\mathbb Q}(C)((t))$,
$s^2-2$ splits into two linear factors. For either value
$s=\pm\sqrt2$, the constants $2-s$ and $2$ are squares.
Both local field factors are therefore

$$
\overline F(\sqrt{Ct})=\overline F(\sqrt{2Ct}).
$$

They remain quadratic by odd $t$-valuation. Thus the arithmetic
absence of any ramified quadratic subfield does not imply its
absence after extending constants. This is not a computation of
actual Fricke constants and does not contradict OI, which fails
in the example because its index is even.

## 7. Primary-source applicability and scope receipt

The cited statements and relevant proofs were independently
inspected in the Stacks Project:

| Primary source | Verified use and limit |
| --- | --- |
| [Section 15.113, tag 0EXQ](https://stacks.math.columbia.edu/tag/0EXQ) | Multiplicativity of ramification indices, finite-extension degree formulas, and the single-place henselian case. These match the complete DVRs used here. |
| [Lemma 15.114.5, tag 09EE](https://stacks.math.columbia.edu/tag/09EE) | Residue characteristic zero gives trivial wild kernel and cyclic inertia of order the ramification index. Residue separability is automatic here; no assertion for imperfect positive-characteristic residues is imported. |
| [Lemma 15.116.7, tag 0EXW](https://stacks.math.columbia.edu/tag/0EXW) | Tame ramification can be removed by an appropriate root of a uniformizer followed by an unramified extension. Used as context, not as Fricke-specific data. |
| [Lemma 15.116.8, tag 0EXX](https://stacks.math.columbia.edu/tag/0EXX) | Tameness is preserved through suitable Galois closures and composita. The exact lcm is established by D2's additional cyclic-inertia argument, not read off as a stated Fricke theorem. |

The source's delicate residue-separability qualifications cause
no gap: every residue field in these propositions has characteristic
zero. Conversely, none of these sources supplies actual values
of $e(E_{n,\varepsilon}/F_\varepsilon)$ or proves OI.
Squareclass decomposition, quadratic Galois correspondence and
the explicit controls are proved directly and are elementary
local algebra, not claimed as a new general classification.

Coverage receipt for the absence of repair findings:

| Checked component | Basis for no repair |
| --- | --- |
| Local target and sign | Hensel decomposition retains $2\varepsilon C$; both valuations checked. |
| Finite composita | Joint inertia is cyclic, restrictions are onto, and the product map is injective. |
| Complete quadratic inventory | Parity-kernel argument accounts for every unit and ramified class. |
| Finite flat controls | Rank, normality, factor indices, exact periods and all three signs checked. |
| Quartic control | Degree, automorphism, inertia, sole quadratic subfield and both base-change factors checked. |
| Source and claim limits | All cited DVR hypotheses apply; controls and conditional results are not promoted to actual Fricke data. |

## Final disposition

Accept Propositions 1–5 only as the stated auxiliary bridge and
controls. An actual all-layer odd-inertia theorem at one branch,
or an actual joint quadratic-inventory exclusion for every finite
compositum, remains necessary to finish this particular local
route. No such theorem is proved in the reviewed package.

Only local exclusion is exported to ST, and only the accepted
one-way specialization is exported from ST to SF2. Local presence
has no reverse implication: the supplied $1+t$ example is
nonsquare in $\kappa(t)$ but square in $\kappa((t))$. Neither
completion nor slice specialization is assumed injective on
squareclasses. Arithmetic and geometric statements stay separate.

The research-review and local batch workflow kept the task on
actual proof checking and source ownership. ARS domain-review
guidance was used only inline for that bounded audit; no full
panel, venue judgement, calibrated score or paper admission is
claimed. Mathematical executions: **0**. Primary-source browsing
was performed. Only this assigned new review file was written;
there were no author/shared/frozen-file edits, Git operations,
external-model calls, mathematical scripts, manuscript/PDF writes
or additional agents.
