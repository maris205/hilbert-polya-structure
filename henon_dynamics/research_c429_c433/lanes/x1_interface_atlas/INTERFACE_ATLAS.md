# X1 — exact interfaces and the two surviving open joins

2026-09-09 UTC. Source-proof synthesis, not a new manuscript, admission,
formal evaluation, or whole-history summary. The six old modules below were
read in their actual proofs. Their established results remain imported;
their original open questions are not silently weakened. There were no
mathematical executions, PDF builds, source edits, or external-model uploads.

## 1. Small interface table

All local links in this table point into the sealed C424–C428 source package.
“Good” always means both directions integral, both degrees retained, and
disjoint forward/backward indeterminacy sets at infinity.

| Module / actual proof | Assumptions and domain | Native clock / observable | Exact output available to a consumer |
| --- | --- | --- | --- |
| **GR5 / C426** — [R5 arithmetic, §§1–5](../../../research_c424_c428/continuation_round5/arithmetic/PROOF_PACKAGE.md) | Number field $K$, $F(x,y)=(y,f(y)-ax)$, $a\ne0$, $d=\deg f\ge2$, $b=\operatorname{lc}(f)$; all affine changes, over the original local/global fields. Local proof also applies to finite extensions of $\mathbb Q_p$. | One $F$; observable is regular good-model existence, not a periodic count. The auxiliary $q=f-aY$ identifies the good disk; its iteration is **not** the native dynamics. | At $v$, existence iff $v(a)=0$, $k_v=-v(b)/(d-1)\in\mathbb Z$, and some $q^{s,r}=(q(sY+r)-r)/s$ is integral, $v(s)=k_v$. At most $\lvert\kappa_v\rvert^{v(d)}$ center candidates, at most one modulo $sO_v$. Every good affine-coordinate image is the same $D_v^2=(r+sO_v)^2$. If all places pass, disks glue to $(r,r)+(I\oplus I)$, $(b)I^{d-1}=O_K$; a global affine chart exists iff $[I]^2=1$, not iff $[I]=1$. |
| **WM6** — [R6 arithmetic-spectral, §§1–5](../../../research_c424_c428/continuation_round6/arithmetic_spectral/PROOF_PACKAGE.md) | Any prime $p$, finite $E/\mathbb Q_p$, $d=p^m$, $k=p^r$, $m>r\ge1$, $F=(y,y^d+cy^k-ax)$; actual periodic points over $\overline E$. | Least period $n$ under $F$; eigenvalue norms of $D(F^n)_P$, normalized by $1/n$. | Put $R=\max(1,\lvert c\rvert^{1/(d-k)})$, $B=\lvert p\rvert^rR^{d-1}$, $C_*=\lvert p\rvert^{-r(d-k)/(d-1)}$. All return eigenvalues are units iff $\lvert a\rvert=1$, $\lvert c\rvert\le C_*$. Potential all-affine good reduction iff $\lvert a\rvert=1$, $\lvert c\rvert\le1$. For $\lvert a\rvert=1$, the all-period envelope is $\log\max(1,B)$, attained at a fixed point. It uses GR5 **locally**, not its ideal-class theorem. |
| **LG4 partials** — [R4 arithmetic, §§2–5](../../../research_c424_c428/continuation_round4/arithmetic/PROOF_PACKAGE.md) | $F,F^{-1}$ integral polynomial maps, $P\in\mathbb Z^d$; original question $d=2$. All moduli, including mixed moduli. | Two-sided ordinary time $n\in\mathbb Z$; $r_m$ is the period of $P\bmod m$, not the order of the whole finite permutation. | If $P$ is nonperiodic, $\theta_P(t)_m=F^{t\bmod r_m}P\bmod m$ is a homeomorphism $\widehat{\mathbb Z}\to X_P$ with $F\theta_P(t)=\theta_P(t+1)$. Periodic source/target and uniformly bounded two-sided iterate degree are closed cases. General LG4 still requires $\theta_P^{-1}(\mathbb Z^2)=\mathbb Z$. |
| **PC424-L descent** — [R6 positive characteristic, §§1–7, 9](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md) | Algebraically closed $k$, characteristic $p>0$, $f\in k[x]$, $d\ge2$, $p\nmid d$. An actual finite algebraic transfer $u$ with compatible embedding $\sigma$ fixing $k$ pointwise, $\sigma x=f(x)$, $\sigma u-u=h\in k[x]$. | One $f$ / triangular lift step; ordinary primitive-cycle sums are the **upstream** observable, not an assumption of the descent theorem. | Every such $u$ is polynomial, unique up to a constant. Thus algebraic-transfer existence equals polynomial coboundariness. For $f=x^2+c$, odd $p$, the missing original implication is ordinary-cycle vanishing $K_c\subseteq A_c$; the theorem proves $A_c=B_c$, not $K_c\subseteq A_c$. |
| **C425 Fricke** — [statement](../../../research_c424_c428/papers/C425_fricke_return/sections/01_introduction.tex), [exact graph](../../../research_c424_c428/papers/C425_fricke_return/sections/03_state_graph.tex), [exhaustion](../../../research_c424_c428/papers/C425_fricke_return/sections/05_line_exhaustion.tex), [level restriction](../../../research_c424_c428/papers/C425_fricke_return/sections/07_level_counts.tex) | Fixed ordered $(A,B,C)\in\mathbb Z^3$; every point of $\mathbb Z^3$, every integral invariant level, singular levels included. | $T=s_zs_ys_x$, rightmost first. The phase lift advances three times per $T$ and retains its phase. | Periodic lattice locus is at most 27 whole affine integer lines plus exact finite-box cycles, radius $100(1+\max(\lvert A\rvert,\lvert B\rvert,\lvert C\rvert))$. Each line has polynomial identity $T^rP(t)=P(t)$, $r\le54$, exact generic/exceptional least-period procedure, and monic quadratic $K(P(t))$. The line identities extend algebraically; the **integer exhaustion does not**. |
| **C427 Vieta** — [statement](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/01_statement.tex), [block proof](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/02_blocks.tex), [classical inputs](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/03_classical.tex), [atlas](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/04_atlas.tex) | $n\ge3$, $a\in\mathbb Z$, $F(x_1,\ldots,x_n)=(x_2,\ldots,x_n,x_2\cdots x_n+a-x_1)$ on the entire integer lattice. | One cyclic shift/update $F$; scalar-word shift period equals native state period. No rotation/reversal quotient. | Finite union of free integer semilinear sets, each with exact native least period, plus finite level-independent remainder. For $n\ge4$, every nonzero update window is bounded or contains one large factor and otherwise units. This makes finite tagging exactly linear. Dimension three imports C421. Fixed levels have finite effective counts, not an all-lattice finite-count zeta. |

### Classical subtraction

GR5 uses classical good reduction, ideal patching and determinant/Steinitz
algebra; its special interface is the all-affine disk-square rigidity.
The good-reduction convention was checked against Kawaguchi,
[Definition 4.1 and Proposition 4.3](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf).
LG4's bounded-degree branch is a finite saturated-lattice application of
[Segal, Theorem 7.2.3(i)](https://www.math.auckland.ac.nz/~obrien/segal-survey.pdf),
whose virtually-polycyclic hypotheses were checked; it is not a theorem about
arbitrary nonlinear degree-growing orbits. Local interpolation is already
[Poonen's Theorem 1](https://math.mit.edu/~poonen/papers/p-iteration.pdf),
requiring coefficientwise proximity with $c>1/(p-1)$.

C427's general integral-period bound and semilinear machinery are classical,
not its new increment. In particular, its proof gives for **every**
$G\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^n)$
$\operatorname{per}(P)\mid L_n=2|\operatorname{AGL}_n(\mathbb F_2)|\operatorname{lcm}(1,\ldots,2^n)$.
For the plane this is $576$. Thus fixed-length integral Hénon compositions
already have a coefficient/degree-independent bound in their own composition
clock. This is also within the broader scope of
[Whang, Theorem 1.1](https://arxiv.org/html/2305.13529v3).
C425's own source subtraction credits Shin for independent coefficients and
group-height methods, Cantat for fixed-fibre dynamical compactness, and C421
for equal forcing; X1 read those ownership passages but did not re-audit all
three external proofs. None is a full-word geometric Galois theorem.

## 2. Two open bridge chains, each with exactly one missing lemma

These are research interfaces, not assertions that a missing lemma is true.
Both target original unclosed arithmetic questions rather than repackaging a
source classification. No further candidate is manufactured.

### Chain A — ordinary cycle sums → finite Frobenius dependence → PC descent

**Consumers:** A1/A2. Keep $f=x^2+c$, every odd $p$, $k=\overline{\mathbb F}_p$,
and $K_c,B_c$ as above. The imported normal form is
$k[x]=B_c\oplus V$, $V=k\oplus xk[x^2]$. Frobenius preserves both summands.

**Single missing lemma:** for every $h\in K_c$, the classes
$[h^{p^i}]\in k[x]/B_c$, $i\ge0$, span a finite-dimensional $k$-space.
Equivalently, some nonzero additive polynomial
$A(T)=\sum_{i=0}^s a_iT^{p^i}$ satisfies $A(h)=\Delta b$ for a polynomial $b$.
A rational $b$ would suffice, because the imported pole lemma makes it
polynomial. This is an alternative certificate for the original algebraicity
bridge; it is **not** obtained from finite-field interpolation.

**Conditional implication, proved here from the imported interfaces.** Write
$h=\Delta Q+v$. Additivity gives $A(v)\in B_c\cap V=0$. If $v$ were
nonconstant of degree $D$, the leading degree of $A(v)$ would be $p^sD$,
so $A(v)\ne0$. Thus $v$ is constant. At any fixed point $\alpha$ of $f$,
the ordinary length-one cycle hypothesis gives $h(\alpha)=0$, whereas
$\Delta Q(\alpha)=0$; hence $v=0$. Therefore $h=\Delta Q$.
Conversely, $h\in B_c$ has zero Frobenius span. This confirms exact
equivalence with the original claim, including its constant defect, rather
than quietly proving a weaker statement.

**Where not to spend effort:** rational-to-polynomial descent, separable versus
inseparable algebraic transfer, and wild extension degrees are already handled
by PC §§1–7. Bounded degree only in a relation's transfer variable is not a
certificate: every interpolant already has the relation $Y-Q_r(X)=0$.
Ordinary primitive sums are not traces on a possibly nonreduced periodic algebra.

### Chain B — good coordinates / congruence closure → controlled representatives → LG4

**Consumers:** B1/B2/B3. For original LG4, $F\in\operatorname{Aut}_{\mathbb Z}
(\mathbb A^2)$ and $P,Q\in\mathbb Z^2$. Define
$C_m=\{n\in\mathbb Z:F^nP\equiv Q\pmod m\}$ and
$H(R)=\max(1,|R_1|,|R_2|)$. The old closure theorem already makes all
$C_m\ne\varnothing$ equivalent to a unique profinite time when $P$ is
nonperiodic. GR5 can supply an integral conjugate only on its exact good-model
branch; an affine chart must carry the selected point-lattice and its congruence
quotients too. For maps already integral over $\mathbb Z$, this chart step adds
no arithmetic separation theorem.

**Single missing lemma:** all $C_m\ne\varnothing$ imply
$$
\sup_{j\ge2}\ \min_{n\in C_{j!}} H(F^nP)<\infty. \tag{HC}
$$
This is the same exact compatibility target now frozen in B2's live report,
not an X1 claim that B2 has proved it.

**Conditional implication, independently elementary.** Choose bounded-height
representatives for $j!$. Only finitely many integer points have that height,
so one actual orbit point $R$ recurs for unbounded $j$. Then $R-Q$ is divisible
coordinatewise by unbounded factorials, hence $R=Q$. Conversely an actual hit
supplies the same bounded-height representative for every modulus. Thus (HC)
is exactly the missing original bridge. A same-representative upper bound
$\|F^{n_j}P-Q\|_\infty< m_j$ for unbounded hitting moduli would also suffice.

**Failed attempted join:** neither GR5 nor WM6 supplies (HC). Every integral
two-sided orbit is bounded at each finite prime, even if its ordinary height
is unbounded. Local interpolation, uniqueness of profinite time, and a global
height formula do not bound a representative chosen from a hitting coset.
For a nonzero congruent integer difference the modulus instead gives a lower
bound on its size. The finite-place/archimedean interface is the issue, not
the construction of the profinite clock.

## 3. Closed, immediately reusable joins — not additional open contracts

### Fixed-point positions recover the scale that multiplier norms lose

Combine GR5 §§1–2 with Vieta's root/coefficient formulas, not with the C427
map. For a single-factor local $F$ put $\rho=|b|^{-1/(d-1)}$ and assume
$|a|=1$. Then potential all-affine good reduction is equivalent to the roots
of $H(Y)=f(Y)-(a+1)Y$ lying in one closed disk of radius $\rho$ over
$\overline E$, equivalently to their pairwise diameter being at most $\rho$.
These roots are exactly native fixed points $(\alpha,\alpha)$.

Indeed, a GR5 good disk contains all fixed points of $q=f-aY$. Conversely,
choose its center $r$ to be one root and pass to a finite extension containing
the roots and a scale $s$ with $|s|=\rho$. The polynomial $H(r+sY)/s$ has
unit leading coefficient and integral roots, so all coefficients are integral.
Adding $Y$ yields exactly $q^{s,r}$; GR5 applies. Repeated roots cause no problem.
This is a proved elementary interface deduction, **not** an inverse-spectral
novelty claim. WM6's roots $0,\xi$ with $|\xi|>1$ show why multiplier-unit
data alone do not supply this common disk. Common relative positions are
information absent from separately scaled local germs.

### A real arithmetic/native-clock equality on Fricke reflection lines

On a retained reflection graph cycle of lifted length $\ell$, select a
phase-zero line $P(t)$. The exact C425 identities give
$$
T^jP(t)=P(-t+\beta),\quad j=\ell/3,\qquad K(P(t))=t^2-bt+c_0.
$$
Invariance of $K$ forces $\beta=b$ by comparing linear coefficients. For a
rational level $D$ with nonzero discriminant
$\delta=b^2-4(c_0-D)$, the two line points are defined over
$\mathbb Q(\sqrt\delta)$. If $\delta$ is nonsquare, its nontrivial Galois
element acts on them by the **actual** native iterate $T^j$. At a good odd
prime with distinct reduced roots, $p$-power Frobenius is the identity or
this swap according as $\delta$ is square or nonsquare modulo $p$.
For a point of native least period $h$, a nontrivial swap inside its cycle
is $T^{h/2}$; this follows from $h\mid2j$ and $h\nmid j$.

This supplies C4/D2 a positive control without defining Frobenius to be time.
It is an elementary consequence on a special-coefficient line stratum, not
the generic periodic Galois tower. Identity-return lines do not automatically
have root-swap in a native cycle. More importantly, C4's inspected live freeze
has algebraically independent $A,B,C,D$: retained-line coefficient relations
cannot be silently transported to that generic base.

## 4. Failed joins and admissible follow-up consumers

| Tempting composition | Exact failure / remaining boundary |
| --- | --- |
| More native periods, or finite base extension, cures WM6's multiplier blindness | Refuted by the full all-period theorem on $1<\lvert c\rvert\le C_*$; not merely by one example. Exact multiplier values are a different observable from their norms. |
| Per-cycle integral jets give GR5's global good lattice | Unjustified: independent scales discard the common disk/leading-term normalization. B4's live report claims a full scale-free jet collapse and cycle-chart theorem; X1 inspected that report but **did not read/review its proof supplement**, so this atlas does not treat those new claims as independently verified evidence. |
| Local good models plus local period lifting detect the class $[I]^2$ | No implication supplied. The intrinsic coset $(r,r)+(I\oplus I)$ exists even when it has no free global chart. Residue reductions alone must not be assumed to see failure of freeness. |
| C425 integer line/core classification gives geometric fixed-point schemes or generic Galois groups | False inference. Exact line identities extend; the height exhaustion and integer-root lists do not. The finite integer core is not a geometric component decomposition. |
| C427 integer atlas extends by clearing rational denominators | Missing integral hypotheses: nonzero factors need not have absolute value at least one; a product of modulus below two need not be a sign. If $Y_i=Mx_i$, the recurrence has product coefficient $M^{-(n-2)}$, outside the same integral family. A denominator theorem alone does not restore the unit-block lemma. |
| An integer period bound implies a semilinear periodic atlas | False even for period one: $(x,y,z)\mapsto(x,y,z+y-x^2)$ has fixed locus $y=x^2$, whose integer projection is not semilinear. C427's mixed-zero linearization is indispensable. |
| An ordinary finite cycle product is a target Euler product | No arithmetic prime labels, root numbers, automorphy, or target spectral divisor are supplied. Keep all Route-B/target claims absent. |

## 5. Provenance, live-lane dependence, and handoff

X1 read all four named old proof packages in full (GR5, WM6, LG4, PC descent)
and the actual C425/C427 statements and proof sections used above, including
their clock, exhaustion, period-label and level-count arguments. External
access was bounded: Segal's exact statement and adjacent explanation;
Kawaguchi's good-reduction definition/local estimates; Poonen's three-page
paper; Whang's theorem statements. No worldwide novelty assertion follows.

Live reports inspected only after they appeared: A1/A2 original freezes,
B2's HC/outcome report, B4's scale-free-jet report, and C4's generic FGT
freeze. They are author-side current-team material, not external reviews.
No claimed live-lane theorem is needed for either conditional proof in §2 or
the elementary deductions in §3. In particular, B2's HC supplies aligned
notation/consumer scope, not the missing bound. C4's freeze supplies the
reason its generic contract does not admit the special-line shortcut.

Immediate source/hypothesis/output/consumer messages were sent to the
coordinator for A1/A2, B1/B2, B3/B4, C2/C3, C4/D2. An additional unreviewed
bounded-order Hasse-jet estimate was sent only as a suggestion for B4 to check;
it is not imported here as a completed result. No extra reviewer or execution
was requested. The skills used enforce local-proof-first source subtraction,
explicit conditional proof status and lane-only writes; no full ARS report or
external-model verification workflow was performed.

**Bottom line:** the most economical original arithmetic target remains
ordinary-cycle data forcing finite Frobenius dependence (Chain A). LG4's real
gap is controlled ordinary representatives (Chain B). The other modules give
strong, exact controls and useful falsifiers, but their combination does not
erase either gap or create target Euler/root-number information.
