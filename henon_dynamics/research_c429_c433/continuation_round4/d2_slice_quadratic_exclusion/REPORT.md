# R4 D2: local exclusion at the two sign branches

2026-09-09 UTC. All first-pass and rounds 2–3 artifacts are read-only
accepted inputs. This lane has no mathematical-execution allocation.

## Frozen question and success condition

Keep the native word $T=s_zs_ys_x$, with one entire right-to-left word
as one tick. On the Fricke slice $\Sigma=\{A=B=0\}$ put

$$
K=\mathbb Q(C,D),\qquad
S_{C,D}:x^2+y^2+z^2-xyz-Cz=D.
$$

For $n\ge3$, $M_n/K$ is the splitting field of the *complete*
specialization to $\Sigma$ of the generic ordinary exact-$n$ native
coordinate cover, as defined and justified in accepted R3,
Proposition 3. Do not replace this cover by one local periodic germ
or by an arbitrary component of a specialized fixed-point scheme.

The sole target is

$$
\tag{ST}
K(\sqrt{D^2-C^2})\not\subseteq M_3\cdots M_N
\quad\text{for every finite }N\ge3.
$$

Its geometric counterpart uses $\overline{\mathbb Q}(C,D)$ and is
separate. Accepted R3 proves that ST suffices for the original generic
SF2 independence question, not that the two questions are equivalent.
Specialization can create extra relations. Success here means an
actual all-$N$ exclusion, an actual finite generic-slice inclusion,
or a precisely proved barrier identifying an unproved whole-cover
hypothesis. No finite census, genericity assertion, or abstract
permutation model will count as an answer to ST.

## Source-first boundary and bounded plan

The Stacks Project's definitions and proofs in
[Section 15.113](https://stacks.math.columbia.edu/tag/0EXQ),
[Lemma 15.114.5](https://stacks.math.columbia.edu/tag/09EE),
[Lemma 15.116.7](https://stacks.math.columbia.edu/tag/0EXW), and
[Lemma 15.116.8](https://stacks.math.columbia.edu/tag/0EXX) were read.
They provide characteristic-zero tame DVR and compositum tools, not
Fricke-specific ramification data. R3's sign-character formulas,
specialization bridge, and odd-period commuting involution are
inherited results, not new claims of this round.

The bounded plan is to retain the residual unit in the exact local
target at $D=C$ and $D=-C$, prove the finite-compositum obstruction
with all whole-cover hypotheses explicit, and test whether the
accepted symmetry/sign data actually force that obstruction.
C4 independently owns the full-base smooth-fold/higher-parabolic
noncontainment question; this lane does not duplicate or assume it.

## Completed local bridge and exact status

The complete five-proposition argument is in
[PROOF_PACKAGE.md](PROOF_PACKAGE.md). **ST and original SF2 remain
NOT CURRENTLY JUSTIFIED.** The deliverable is a precise local-algebra
bridge plus a proved barrier to deriving it from the inherited
symmetry/sign information. No actual Fricke inclusion or all-layer
exclusion has been proved. Nonauthor review is pending.

For $\varepsilon\in\{1,-1\}$ set

$$
t=D-\varepsilon C,\quad \kappa=\mathbb Q(C),\quad
F_\varepsilon=\kappa((t)),\quad
E_{n,\varepsilon}=F_\varepsilon M_n,\quad
H_{N,\varepsilon}=E_{3,\varepsilon}\cdots E_{N,\varepsilon}.
$$

These are local fields of the complete splitting covers, not fields
of one colliding point or one selected component.

Proposition 1 retains the exact target class:

$$
[D^2-C^2]=[2\varepsilon C t]
\quad\text{in }F_\varepsilon^\times/F_\varepsilon^{\times2}.
$$

The residual unit $2\varepsilon C$ is nonsquare even in
$\overline{\mathbb Q}(C)$. Passing to algebraically closed
*constants* is not the same as making the residue field
algebraically closed.

Proposition 2 proves, using characteristic-zero cyclic inertia,

$$
e(H_{N,\varepsilon}/F_\varepsilon)
=\operatorname{lcm}_{3\le n\le N}
e(E_{n,\varepsilon}/F_\varepsilon).
$$

Thus odd inertia order on every whole higher layer, at either one
fixed sign branch, is sufficient for ST. This is weaker than
whole-cover unramifiedness, but the actual oddness assertion is
still unproved. A positive point-permutation sign only counts
even-length inertia orbits modulo two; it does not say every
inertia orbit has odd length.

Proposition 3 states the alternative when parity does not suffice.
For any complete joint field $E/F_\varepsilon$ with residue
$\kappa_E$, put

$$
U=\ker(\kappa^\times/\kappa^{\times2}
\longrightarrow\kappa_E^\times/\kappa_E^{\times2}).
$$

Its full quadratic inventory is either $U$, or
$U\sqcup[at]U$ for some $a\in\kappa^\times$.
The second case occurs exactly when an actual joint Galois
character is nontrivial on inertia. In that case the target is
present exactly when $2\varepsilon C/a$ becomes a square in
$\kappa_E$. No proof identifies this joint inventory with the
span of native phase/cycle signs or of the individual inventories.

## Proven barrier, not a Fricke counterexample

Proposition 4 gives two explicit finite flat normal full-point
models. For any odd $n\ge3$ and $s\ge2$, they have $2ns$ points,
free $h$-orbits of length $2n$, and precisely the inherited
relations $g=h^n$, $T=h^{n+1}$, $gT=Tg=h$.
Their generic splitting fields are respectively
$F_\varepsilon(\sqrt t)$ and
$F_\varepsilon(\sqrt{2\varepsilon Ct})$.

Both inertia groups have order two, both residue fields are
$\kappa$, and the abstract inertia permutations are identical:
point sign and native-cycle sign are positive, while the
$h$-orbit sign is negative. Only the second field contains the
exact target. This distinction survives extending constants to
$\overline{\mathbb Q}$. Taking $s=s_n$ matches the accepted point
count, but no model is asserted to solve the Fricke periodic
equations. Also, no positive inertia-sign value is asserted for
the actual Fricke fields. The controls prove only the insufficiency
of the listed information, even if such positive signs were known.

Proposition 5 supplies a separate arithmetic/geometric control:

$$
E=\mathbb Q(C)((t))(s,w),\qquad
s^2=2,\quad w^2=(2-s)Ct.
$$

This is cyclic quartic with inertia order two. Its sole quadratic
subfield is unramified, so no ramified target is present. After
extending constants to $\overline{\mathbb Q}$ its local factors
are exactly the target $\sqrt{2Ct}$ field. Thus even inertia
need not provide a ramified quadratic character, and an arithmetic
inventory exclusion cannot be silently promoted to a geometric one.
This is not a calculation of actual Fricke compositum constants.

## What would finish this local route

At least one actual all-$N$ whole-cover exclusion is still needed:
odd inertia at one branch for every higher layer; absence of a
ramified quadratic character in every joint local field; or an
identified ramified coset whose residual-unit test always excludes
the target. None is established here. C4's separate global-fold
work is not imported as an unproved assumption.

Local exclusion would imply the slice exclusion, then accepted R3
would imply generic SF2. Local presence has no reverse implication:
completion can create squareclass relations, just as the slice
specialization can. All the criteria concern finite composita
before the universal quantifier; no infinite common étale
neighborhood or finite-census extrapolation is used.

## Sources and workflow boundary

| Source actually inspected | Owned input and limit |
|---|---|
| Stacks Project, Section 15.113 | Henselian degree and ramification-index formulas; no dynamical input. |
| Stacks Project, Lemma 15.114.5 | Inertia is cyclic of order the ramification index in residue characteristic zero; used in the finite-compositum proof. |
| Stacks Project, Lemmas 15.116.7–8 | Tame extension/compositum context; no Fricke branch separation supplied. |
| Accepted R3 D2 Propositions 1, 3, 4 | Actual target class, legitimate one-way specialization, and free odd-period symmetry. These are inherited, not R4 increments. |

The local-first source inventory and arXiv-script fallback were
checked in the preceding source pass. A bounded Fricke/Markoff
parabolic-source search supplied no applicable all-layer inertia
theorem; this is not a literature nonexistence or novelty claim.
The package proves its elementary squareclass and control-model
calculations directly rather than attributing them to an unseen
paper.

The proof-writer skill kept the original ST unchanged and the
actual missing hypothesis explicit; research-lit supplied the
primary-source boundary. Only this R4 directory's report and proof
were written. Mathematical programs, old reruns, PDF builds, Git,
shared indexes, manuscripts, and external-model uploads: zero.
