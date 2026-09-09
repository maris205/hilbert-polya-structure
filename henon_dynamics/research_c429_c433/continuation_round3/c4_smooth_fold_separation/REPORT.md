# R3 C4: smooth-fold separation from higher native layers

2026-09-09. New exclusive continuation directory. Accepted FG2, NI and
the generic ordinary-sheet count are read-only inputs. No mathematical
execution is allocated. The original full Fricke Galois-tower question
FGT remains unchanged and unclosed.

## 1. Exact frozen SF2 test

Keep $k=\mathbb Q(A,B,C,D)$, the surface
$x^2+y^2+z^2-xyz-Ax-By-Cz=D$, and the ordered native return
$T=s_zs_ys_x$ (rightmost first). For $n\ge1$, $P_n$ is the ordinary
geometric exact least-native-period-$n$ set on the generic fibre and
$L_n/k$ is its splitting field. Let $B=\mathbb A^4$ and let $B^{\rm sm}$
be the complement of the singular-fibre divisor.

The accepted degree-eleven two-cycle cover has rational model
$$
\Phi(q,X,Y,Z)=
\bigl(X-qYZ,\ Y-qXZ,\ Z-qXY,\
q(XYZ-X^2-Y^2-Z^2)\bigr).
$$
Set $c_f=(2/3,3/2,3/2,3/2)$ and
$b_f=\Phi(c_f)=(0,0,0,-9/4)$. Let $R_f$ be the unique irreducible
component of the critical hypersurface $\det D\Phi=0$ through $c_f$,
and let $\mathscr F$ be the reduced Zariski closure of its image in
$B$. The accepted simple-fold local model makes these specifications
unambiguous; verifying this global-divisor description is part of the
present proof package. The other three sign branches at $b_f$ are not
assumed to define different global divisors.

**SF2.** For every $n\ge3$, the whole normalization of
$B_{\overline{\mathbb Q}}$ in the geometric splitting field of $P_n$
is unramified over the generic point of $\mathscr F$. Accepted FG2
supplies odd cycle-sign inertia along $\mathscr F$. Hence SF2 would
give, in every finite joint tower, an inertia element whose restriction
to $L_2$ has odd cycle sign and whose action on every higher layer is
trivial.

This is a sufficient branch-separation criterion for the remaining
period-two character intersection, not a claim that it is logically
necessary for FGT. The quantifier is every native $n\ge3$; no finite
$n=3,4$ census or arbitrary truncation can settle it. No all-period
neighborhood or rational-specialization statement is included.

**Status at freeze: NOT CURRENTLY JUSTIFIED.** Success requires control
of every higher-period sheet at generic $\mathscr F$, including remote
periodic points and possible escape to infinity. A no-resonance or
iterate-ideal calculation only at the two colliding two-cycles is
insufficient. A shared higher-period branch component would refute
SF2; failure to exclude it leaves SF2 open, not refuted.

## 2. Discriminating argument at freeze

First identify the actual global fold divisor and its generic local
inertia from the accepted model. Then test whether the all-smooth-fibre
intersection calculation plus the boundary dynamics makes every fixed
incidence finite over the smooth base. If justified, this removes
escape-to-infinity as a loophole and leaves a precise residual
multiplier/ramification condition at every other periodic point over
the generic fold. Local parabolic iterate stability will be recorded
only as a component of that global test.

Source subtraction precedes any increment claim. The proof-writer
status gate and research-lit local-first source search are in use;
no relevant locally named PDF or configured Zotero/Obsidian tool was
found, so primary web sources are being checked. The available arXiv
fetch-script paths were absent; arXiv web search is the fallback.

D2 owns the complementary cycle-character and parameter-symmetry
approach in its separate R3 directory. First-pass and R2 files, shared
indexes, Git, manuscripts and PDFs remain read-only.

## 3. Author-complete result and exact status

The complete argument is in [PROOF_PACKAGE.md](PROOF_PACKAGE.md).
**SF2 remains NOT CURRENTLY JUSTIFIED.** No actual counterexample or
shared higher-period branch component is produced. Nonauthor review
of the partial claims is pending; neither this report nor its package
marks FGT closed.

The package establishes the following all-period reductions.

- **One actual global fold.** For the accepted map, rescaling
  $a=qX,b=qY,c=qZ$ gives, with Jacobian columns ordered $(X,Y,Z,q)$,
  $$
  q^3\det D\Phi=(ab+c)(ac+b)(bc+a)
  +q\bigl((a^2+b^2+c^2)^2
  -4(a^2b^2+b^2c^2+c^2a^2)-a^2-b^2-c^2-6abc\bigr).
  $$
  The two coefficients in this linear polynomial in $q$ are coprime.
  Hence the entire finite-chart critical hypersurface is geometrically
  irreducible; its image $\mathscr F$ is an irreducible divisor. The
  four accepted local branches at $b_f$ belong to that same divisor.
  Accepted FG2 then supplies its odd cycle-sign inertia (§1).
- **All remote sheets at infinity are controlled.** On $B^{\rm sm}$,
  $\mathcal X_n=\operatorname{Fix}(T^n)$ is finite flat of rank
  $a_n=(2+\sqrt5)^n+(2-\sqrt5)^n+4(-1)^n$ for every $n$. The classical
  input is the intersection length on each smooth fibre. The package
  proves local complete-intersection flatness and includes the
  constant-degree quasi-finite-to-finite upgrade (§2).
- **Every period-two germ is isolated from higher native layers.** At
  $b_f$ the eight fold points have unipotent $T^2$ return and the six
  axis points have determinant one and trace $113/16$. Thus no point
  of this complete fibre has a nontrivial root-of-unity return
  eigenvalue. Finite $\mathcal X_2$ makes each such resonance image
  closed, so none contains the generic point of irreducible
  $\mathscr F$. The iterate-ideal identity gives
  $\operatorname{Fix}(T^{2m})_p=\operatorname{Fix}(T^2)_p$ at every
  period-two point there, for every $m$ (§§3–4).

These statements leave a genuine finite-point gap. Over the strict
henselian DVR at $\eta_{\mathscr F}$, remove the open-and-closed
$\mathcal X_2$ part from even $\mathcal X_n$; for odd $n$ remove
nothing. The residual $\mathcal Z_n$ is finite flat, and all its
special points have least native period at least three. SF2 is exactly
the assertion that the normalization of each of these residual generic
point algebras is finite étale, for every $n\ge3$ (§5).

Neither finite flatness nor isolation of lower periods proves that
normalized different is a unit. Any failure must now occur at a
finite genuinely higher-period resonant point on the generic fold.
The package distinguishes a nonreduced raw fibre from ramified
normalization, and does not turn failure of a derivative test into a
counterexample. The next required input is an all-period normalized
ramification exclusion on these $\mathcal Z_n$, or an actual shared
ramification divisor refuting SF2.

## 4. Sources, interfaces and workflow boundary

The structured source-subtraction table and bounded-search record are
in the package §6. The principal external input is
[Iwasaki–Uehara, §§5 and 8](https://arxiv.org/pdf/math/0512583v3), used
for lengths only; the finite flat conclusion uses the classical
[miracle-flatness](https://stacks.math.columbia.edu/tag/00R4) and
[Zariski-main](https://stacks.math.columbia.edu/tag/05K0) tools, with
the relevant finiteness argument written out. The real hyperbolicity
results in [Cantat](https://arxiv.org/pdf/0711.1727v2) do not supply
the missing complex-family ramification exclusion on this fold.

The proof-writer skill enforced the unproved-SF2 status gate and the
explicit dependency/gap record. The research-lit skill supplied the
local-first primary-source check and source subtraction; its unavailable
arXiv script was replaced by primary web retrieval. No literature
search is claimed as a novelty certificate.

The global critical-divisor identity and complete period-two isolation
have been sent to D2 for its complementary character analysis. The
asserted isolation is not a proof that the cycle-sign quadratic avoids
the compositum of higher layers, and no such intersection claim is
exported as established.

Only this new lane's REPORT.md and PROOF_PACKAGE.md were created or
edited. Mathematical executions: **zero**. First-pass and R2 bytes,
shared indexes, manuscripts, PDFs and Git were not modified. No new
child agent was launched in R3.
