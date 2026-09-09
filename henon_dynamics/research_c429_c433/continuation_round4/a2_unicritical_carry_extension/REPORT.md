# R4 A2: unicritical carry extension — frozen bounded question

2026-09-09 UTC. This is an allocated same-paper algebraic extension
scout, not a second contract or a retrospective enlargement of the
already admitted quadratic PC424-L theorem. New writes are confined to
this directory; the admitted quadratic proof and admission records are
read-only.

## Exact proposed theorem

Let $p$ be odd, $k=\overline{\mathbb F}_p$, let $d\ge2$ be an
integer with $p\nmid d(d-1)$, and let $c\in k$. For
$f(x)=x^d+c$ and $h\in k[x]$, ask whether

$$\sum_{a\in O}h(a)=0\quad\text{for every ordinary primitive }
f\text{-cycle }O
\quad\Longleftrightarrow\quad
h=Q\circ f-Q\text{ for some }Q\in k[x].$$

Every distinct point is counted once, including periods divisible by
$p$. The native clock is one application of $f$, and the observable
is the ordinary additive sum. The proposed proof also targets the
same-paper finite certificate: for $\deg h\le M$, $M\ge1$, put

$$n=3\lfloor\log_d M\rfloor+4,\qquad
F_j=f^{\circ j}-x,\qquad H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i}.$$

Then coboundary membership should be equivalent to
$F_j\mid F_j'H_j(h)$ for both $j=n,n+1$, and to ordinary-root
return-sum vanishing at those two levels. Expected primitive detector
cutoff: $3\lfloor\log_d M\rfloor+5$. These are proposed exact
bounds, not results inferred from finite computations.

## Chosen mechanism and falsifiable recurrence

The coordinator proposed the $d$-ary extension of the admitted binary
carry mechanism. Work in the full cyclic algebra

$$A_n=k[X_0,\ldots,X_{n-1}]/(X_i^d+c-X_{i+1}:i\bmod n),$$

with digit basis $\prod X_i^{e_i}$, $0\le e_i<d$, and full
Jacobian background $P_n=\prod X_i^{d-1}$. For a normal exponent
$k_0>0$ with $d\nmid k_0$, the initial carry is $t_0=k_0$;
at each site use

$$b_s=(d-1+t_s)\bmod d,\quad
r_s=\left\lfloor\frac{d-1+t_s}{d}\right\rfloor,\quad
0\le t_{s+1}\le r_s.$$

The transition has binomial weight
$\binom{r_s}{t_{s+1}}(-c)^{r_s-t_{s+1}}$. The falsifiable
bound is $t_s\le1+(k_0-1)/d^s$, and the source output satisfies
$b_0\le d-2$, so one final carry of size at most one is legal.
For every nonzero short target digit vector supported in
$[0,m]$, $m=\lfloor\log_d M\rfloor$, the proposed recurrence is

$$[X^{\mathbf e}]\left(P_n\sum_i v(X_i)\right)
=[X^{\mathbf e}]\left(P_{n+1}\sum_i v(X_i)\right)
\quad(n\ge3m+4),$$

for every normal $v$ of degree at most $M$. Source localization,
digits greater than one, wraparound at the source and insertion/deletion
of a weight-one zero site must all be proved, not assumed from the
binary case. Combining this with $d^nC_n=a_D$ at adjacent levels
should force $(d-1)a_D=0$, using the stated exclusion.

## Frozen status and source subtraction

At the freeze, the exact recurrence is **NOT CURRENTLY JUSTIFIED**
pending the full written argument. The complete proof or a precise
failed lemma will be recorded in `PROOF_PACKAGE.md`.

Imported inputs: the actual admitted
[quadratic carry proof](../../continuation_round3/a1_periodic_normal_form/PROOF_PACKAGE.md),
the [old binary digit detector](../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md),
and the [bounded primary-source assessment](../../continuation_round3/NOVELTY_CHECK_PC_L.md).
The extension cannot claim ownership of normal forms, monic pure-power
cyclic bases, Jacobian trace/residue methods, binomial transfer matrices,
or the already admitted adjacent-level argument. The proposed increment
is checking the exact $d$-ary carry compatibility and resulting parameter
range inside the same paper.

Hand triage has also identified a concrete method-boundary candidate:
if $d\equiv1\pmod p$, take $c=0$, $h=x$. Then all Jacobian
tests hold, although the fixed point $1$ has nonzero sum. This would
refute a stronger Jacobian-certificate claim in the excluded range,
not the original ordinary-cycle implication there.

No mathematical run is allocated or executed. No old rerun, manuscript,
PDF, evaluation, Git write, external model/API call or nested worker.

## Completed author result and exact current range

The [full proof](PROOF_PACKAGE.md) establishes the frozen carry
recurrence and the proposed equality and finite certificate for
$p\nmid d(d-1)$. After the initial freeze, the coordinator explicitly
authorized the separate branch $p\mid d$. There $F_n'=-1$,
so squarefreeness and the leading-digit detector give the equality
directly. The combined author-proved theorem is therefore

$$K_f=\Delta k[x]\quad\text{for every odd }p,
\ d\ge2\text{ with }d\not\equiv1\pmod p,
\ c\in\overline{\mathbb F}_p.$$

The exact two-return certificate remains at
$n=3\lfloor\log_d M\rfloor+4$ and $n+1$. A noncoboundary
of degree at most $M$ has a detecting primitive period dividing one
of these integers, hence at most $3\lfloor\log_d M\rfloor+5$.
The two iterate degrees are at most $d^5M^3$; no optimized algorithm
or optimal cutoff is claimed.

The full proof keeps target digits, not only their nonzero positions.
At the source the final digit is $b_0+t_n\le d-1$; at other
sites it is $b_s$. Source localization proves the same short interval
$[-m,m+1]$ as in the quadratic ancestor. In the long zero-target
gap, the only eligible transition is $1\to1$ with weight one,
so insertion and deletion preserve every digit and path weight.
That is the actual compatibility needed for the degree extension.

The excluded congruence class has the promised concrete method control:
for $d\equiv1\pmod p$, $c=0$ and $h=x$, every Jacobian
test holds because $F_n=xR_n$, $F_n'=R_n$ and $x\mid H_n(x)$.
Yet the fixed point $1$ has sum $1$. This is an all-level failure
of the Jacobian certificate, not an ordinary-cycle counterexample.
The ordinary-sum equality in that congruence class is not settled here.

Current status: **PROVABLE AS STATED — full author proof, nonauthor
R4 check pending**. The proof was fully reread without changes;
its stable SHA256 supplied to E8/root is
`766f8d95f3297fdfe2b803965bc217ed28ccc7934090c07c68f42c9624f0cd01`.
This extension belongs to the already admitted PC paper if the
coordinator accepts it; it neither creates a second contract nor
changes the frozen quadratic artifact.

## Primary-source comparison actually performed

| Source | Inspected primary passage | Ownership and relation |
| --- | --- | --- |
| Cattani, Dickenstein and Sturmfels, *Computing Multidimensional Residues* (1994 preprint) | [Section 4, pp. 19–21](https://arxiv.org/pdf/alg-geom/9404011): monic pure-power basis, Lemma 4.2 and proof, Theorem 4.3 and proof, Jacobian trace formula and Algorithm 4.8. The complex-subfield setup in Section 1 was also checked. | General normal-form/residue/trace machinery is classical. The proof here supplies elementary positive-characteristic arguments and does not specialize an unseen analytic theorem. |
| Cvitanović, Hansen, Rolf and Vattay, *Beyond the periodic orbit theory*, Nonlinearity 11 (1998), 1209–1232 | [Section 3 equations (17)–(19), Section 4 equations (24)–(28) and derivation, conclusion p. 1229](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf). | General multiplier sum rules, finite binomial matrices and successive-trace comparison are prior work. The inspected degree-general rules do not assert the positive-characteristic ordinary additive coboundary conclusion. Their finite quadratic matrices explicitly credit Levin–Sodin–Yuditskii. |
| Li and Zhang, *Ground states and periodic orbits for expanding Thurston maps*, Math. Ann. 391 (2025), 3913–3985 | [arXiv v2, Theorem 1.1, pp. 8–9, and its proof/Remark 6.6, p. 38](https://arxiv.org/pdf/2303.00514); [publisher bibliographic record](https://doi.org/10.1007/s00208-024-03018-0). | A genuine degree-general Livšic antecedent: the stated maps are expanding Thurston maps or postcritically finite rational maps without periodic critical points on the Riemann sphere; potentials and transfers are real Hölder functions. These hypotheses and regularity do not give the present algebraic finite-characteristic statement. |

For the last source the publisher body was subscription-restricted;
the actual theorem and proof were read in the primary arXiv version.
No full audit of its proof dependencies is claimed or needed for the
scope comparison. The initial attempt at a nonexistent HTML version
failed; the bibliographic record and accessible PDF then resolved the
correct v2 source. For Levin–Sodin–Yuditskii, this round inspected the
explicit attribution in the 1998 source, not the unavailable original
full text. The inherited access limitation remains.

The new targeted query families were: unicritical/Livšic; $x^d+c$
and coboundary; polynomial periodic-orbit sums over finite fields;
unicritical positive-characteristic cohomological equations; polynomial
coboundary and characteristic; polynomial Livšic and finite field;
$x^d$ cohomological equations; unicritical orbit sums; Livšic and
positive characteristic; Livšic and degree; rational-function
cohomological equations over finite fields; periodic unicritical
coboundaries; Livšic for rational maps; polynomial-map periodic
cohomological equations; and periodic points/polynomial coboundaries.
An additional arXiv title query located the Li–Zhang primary text.
These searches used the available web index, not exhaustive native
database access. Search-only hits on dynatomic portraits or unrelated
cohomology were not mathematical inputs.

No exact previously published degree-general algebraic theorem was
identified in the inspected material. This is a bounded search outcome,
not a global-priority or novelty certification. In particular, the
quadratic carry mechanism, ordinary polynomial normal forms, finite
certificates as a general idea, and all trace machinery are subtracted.
The report proposes only a checked same-paper extension of the specific
admitted mechanism.

## Final author execution and handoff

Proof-writer required the precise congruence range, explicit source-digit
check and separation of a method obstruction from an original-claim
counterexample. Research-lit supplied local-first source subtraction and
the primary passage comparison above. The batch workflow kept the new
extension in its assigned directory and prevented counting it as another
paper. E8 has the stable full proof for a targeted internal nonauthor
check; source acceptance and integration belong to the coordinator.

R4 new writes: only this report and `PROOF_PACKAGE.md`. Mathematical
runs, old reruns, manuscripts/PDFs, evaluations, Git writes, external
model/API calls and nested workers: **0**. No R4 theorem produces
target Euler factors, root numbers, automorphy or a Hilbert–Pólya
correspondence. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
