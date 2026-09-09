# MS6: bounded primary-source and transfer-saturation audit

Source check completed 2026-09-10 UTC. This is a feasibility input to A2,
not a theorem admission, a novelty certificate, or a replacement of M6.

## 1. Frozen question and outcome

Let $k=\overline{\mathbf F}_p$, $d\ge2$, $c\in k$,
$f=x^d+c$, and $g\in k(x)^\times$. MS6 asks whether

$$
\prod_{a\in O}g(a)=1\quad\hbox{for all but finitely many primitive
native $f$-cycles }O
\quad\Longleftrightarrow\quad
g^{p^e}=h\circ f/h\quad(e\ge0,
\ h\in k(x)^\times).
$$

Cycles meeting a zero or pole are exceptional; the clock is one application
of $f$. Neither restriction to one finite field nor omission of all
$p$-divisible periods is allowed. The original unsaturated M6 remains refuted.

**Outcome: no complete covering theorem or actual MS6 counterexample was
located in the authorized three search batches. The reverse implication
is NOT JUSTIFIED by this source audit.** Absence from this bounded search
does not establish novelty or nonexistence of an applicable theorem.

What was obtained is useful but narrower: precise limits of a close Mahler
algebraicity theorem, a verified characteristic-free intersection formula,
and an explicit failure of unconditional algebraic-to-$p$-saturated descent.
The last item fails the periodic hypothesis and is not an MS6 counterexample.

## 2. Search and access ledger

Exactly three targeted web-search batches were used. Their axes were:

1. Rational periodic-orbit coboundaries, multiplicative Livšic over finite
   fields, positive-characteristic cohomological equations, Mahler transfer.
2. Periodic products and rational coboundaries, Hilbert 90/Mahler,
   finite-field cohomological equations, Frobenius/norm/Chebotarev.
3. Recent multiplicative-coboundary literature, arXiv periodic rational
   coboundaries, positive-characteristic algebraic Mahler solutions,
   Kummer splitting and function-field Chebotarev.

The recent pass included 2024–2026 terms and an arXiv recency restriction.
There was no fourth search batch. Subsequent actions were direct source
opens, within-document finds, and official table-of-contents navigation.
Irrelevant hits and snippets were not promoted into evidence.

No exposed Zotero/Obsidian access or installed arXiv-fetch command was
located in the initial tool check; direct web primary access was used.
Only this new report was written. No mathematical program, parameter
census, new agent, external model/API, Git operation, manuscript/PDF, or
old/shared-file modification was performed.

## 3. Closest newly verified algebraicity result

Gwladys Fernandes, *Regular extensions and algebraic relations between
values of Mahler functions in positive characteristic*, arXiv:1808.00719v1
(2018): [author manuscript](https://arxiv.org/pdf/1808.00719v1).

Actual reading: introduction and hypotheses, Theorem 1.4/Corollary 1.3,
and the complete selected Proposition 4.1/Corollary 4.1 proof chain in §4,
including the proof of Theorem 1.4. This is not a claim to have read every
proof in the 31-page paper.

Proposition 4.1 assumes a **finite extension already exists**, monomial
substitution $z\mapsto z^d$, and $p\nmid d$. It classifies such a stable
extension over the paper's complete algebraically closed coefficient field
as purely inseparable over a radical monomial field. Corollary 4.1 adds
$L\subset C((z))$; Theorem 1.4 obtains rationality for an already algebraic
ordinary Mahler power series. These statements do not construct a transfer
from periodic products; do not cover $p\mid d$; and do not directly treat
$x^d+c$ with arbitrary $c$. The analytic-value theorems also require the
paper's valued function-field/regular-point hypotheses.

Thus this source does not repair the previously identified Roques bridge
gap. A locally constructed formal transfer is not thereby algebraic;
algebraicity is not thereby the periodic-to-transfer implication.

## 4. The $p$-primary distinction is real, but is not a proof

[Stacks Project, §59.28, Kummer theory](https://stacks.math.columbia.edu/tag/03PK)
was actually read at Lemmas 59.28.1 and 59.28.3, including their proofs.
For invertible $n$, the Kummer sequence is exact on the étale site;
for arbitrary $n$ it is exact on the fppf/syntomic sites. This is a
legitimate reason to distinguish prime-to-$p$ covers from purely
inseparable phenomena, not an existence theorem for dynamical transfers.

Directly, $\mu_{p^e}(k)=\{1\}$ because
$X^{p^e}-1=(X-1)^{p^e}$. Geometric periodic values therefore cannot detect
a $p$-primary root-of-unity discrepancy. That observation explains why
the proposed saturation is plausible; it does not prove completeness.

## 5. Three exact hand checks, with domains retained

### 5.1 The forward implication is valid with finite cycle exceptions

Suppose $g^{p^e}=h\circ f/h$. Exclude cycles meeting the finite support
of $\operatorname{div}(h)$ or $\operatorname{div}(g)$. There are only
finitely many such primitive cycles. On every remaining cycle,
telescoping gives $P_O^{p^e}=1$, hence $P_O=1$ in $k$.
No separability assumption on $f$ is used.

This proof must exclude transfer zeros/poles even if they cancel in the
rational expression for $h\circ f/h$. For example, in characteristic
$5$, $f=x^2$, $h=x-1$, $g=x+1$ gives $h\circ f/h=g$, but the fixed point
$1$ has $g(1)=2$. MS6 can exclude this one cycle; naive pointwise
telescoping at $h(1)=0$ cannot. This was already an input from the M6 audit.

### 5.2 The old M6 obstruction is absorbed, not disproved retroactively

For $f=x^{p+1}$ and $g=x$, one has $g^p=f(x)/x$ with $h=x$.
Thus the old counterexample to an unsaturated rational transfer is
compatible with MS6 using $e=1$. It is not a new positive theorem.

### 5.3 Algebraic ordinary series need not descend by a $p$-power

Here is an elementary diagnostic **without** the MS6 periodic hypothesis.
Take $p>2$, $f=x^p$, $g=1+x$, and let $H\in\mathbf F_p[[x]]$ be the
unique branch satisfying

$$H(0)=1,\qquad H^{p-1}=1+x.$$

Existence and uniqueness follow by recursively solving coefficients,
since $p-1$ is invertible. Frobenius on these coefficients gives
$H(x^p)=H(x)^p$, whence $H\circ f/H=1+x=g$. So an ordinary power-series
transfer is algebraic and separable, with a nontrivial tame radical.

Nevertheless, no $h\in k(x)^\times$ and $e\ge0$ satisfy
$g^{p^e}=h\circ f/h$. At the totally ramified fixed point $a=-1$,
orders of rational functions would give

$$p^e=(p-1)\operatorname{ord}_{-1}(h),$$

which is impossible for $p>2$. This rules out every $e$, not only $e=0$.

Why this is **not** an MS6 counterexample: for $a\in\mathbf F_{p^n}$,

$$\prod_{i=0}^{n-1}(1+a^{p^i})
=N_{\mathbf F_{p^n}/\mathbf F_p}(1+a).$$

Choose $\lambda\in\mathbf F_p^\times\setminus\{1\}$.
There are $(p^n-1)/(p-1)$ choices of $a$ with this norm, an unbounded
number as $n$ grows. Each belongs to a primitive cycle whose product
is not $1$: otherwise the length-$n$ product would be $1$.
A finite union of bad primitive cycles contains only finitely many
points. Hence infinitely many bad cycles exist. This example only
invalidates an unconditional descent shortcut for inseparable bases.

More generally, at a fixed point of local degree $r$, a putative
saturated transfer imposes
$p^e\operatorname{ord}_a(g)=(r-1)\operatorname{ord}_a(h)$.
Finite exceptional cycles cannot make this rational-function identity
optional; they only alter the pointwise periodic side.

## 6. A verified standard input for A2's conditional Kummer route

J. S. Milne, *Lectures on Étale Cohomology*, v2.21 (2013), §25,
Theorem 25.1: [official readable PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf).
The theorem, Lemmas 25.3–25.4, and the displayed proof on printed
pp.147–148 were actually read. For a complete nonsingular variety over
an algebraically closed field and any regular selfmap $T$,

$$\Gamma_T\cdot\Delta=\sum_i(-1)^i\operatorname{Tr}
 (T^*\mid H^i(X,\mathbf Q_\ell)).$$

There is no separability hypothesis. Where the intersection is finite,
it counts fixed points with intersection multiplicities, not just
distinct geometric points. This confirms the relevant interpretation
for inseparable curve maps. It is not by itself the square-root error
bound for an arbitrary curve selfmap.

A2 independently proposed deriving that bound from Hodge index on
$Y\times Y$, including graph self-intersection, instead of assuming a
Frobenius point-counting theorem applies to arbitrary $T$.
The intersection algebra supplied by A2 was checked; an actual
Hodge-index theorem text was not obtained in this bounded source pass.
Stacks Ch43/45 contents were inspected but are not claimed to contain
that missing theorem. The ordinary Milne PDF repeatedly timed out;
the official cropped version supplied the text above.

Even a completed Kummer argument here is conditional: it starts with
some identity $g^m=h\circ f/h$. Extracting a prime $q\mid m$ requires
using $u=g^{m/q}$ in $u^q=h\circ f/h$. The normalization of $z^q=h$
must be checked for connectedness; if it splits, component permutations
and constant $\mu_q$ twists cannot be ignored. These cautions were sent
to A2. Removing prime-to-$p$ torsion **after its existence** does not
construct finite torsion from the original periodic hypothesis.

## 7. Handoff decision

The auditable remaining obligation is

$$\text{cofinite primitive products }1
\ \Longrightarrow\ \text{an actual finite transfer relation}
\ \Longrightarrow\ \text{$p$-primary rational transfer}.$$

The first arrow is not supplied by any source verified here.
The second needs the periodic hypothesis for inseparable bases, as
§5.3 demonstrates. Consequently this audit supports a precise bounded
obstruction report and further proof work, not MS6 closure or admission.
No third candidate, all-rational-map generalization, or claim to a
fifth source-paper contract is made. Research-lit/novelty-check discipline
kept actual primary reading separate from search coverage and mathematical
inference; the proof discipline kept the non-counterexample explicitly
separate from the frozen question.
