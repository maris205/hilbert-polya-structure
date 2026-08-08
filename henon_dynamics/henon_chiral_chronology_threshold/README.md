# HCS-C21: chronology--cohomology threshold in chiral Hénon covers

**Date:** 2026-08-08
**Status:** exact period-six cover theorem, exact scoped period-six/seven
threshold, and exact lower-period marker obstruction; Route-A exploratory
**Research stage:** Stage 2 complete; 17-page bilingual manuscript compiled
and accepted by the two-round release review

## Outcome

This round found a sharp negative structure rather than a Hilbert--Pólya
construction.

Starting from the published period-six chiral polynomial of Endler and
Gallas, the normalized twelve-state ordered-edge object is a geometrically
connected genus-one $\mathsf D_6$-cover, where $\mathsf D_6$ has order $12$.
Hénon
time has exact order six on its points but acts trivially on its entire
weight-one cohomology:

\[
g(E_6)=1,
\qquad
\tau^*|_{H^1(E_6)}=1.
\]

The certified period-seven chiral cover from HCS-C20 has

\[
g(E_7)=8,
\qquad
\dim H^1(E_7)_{\tau\ne1}=12.
\]

Consequently, among the **source-identified and repository-certified chiral
ordered covers through period seven**, the smallest period for which at
least one certified component has nontrivial weight-one time characters is
seven.  This is not a classification of every exact-period component and is
not a Riemann-zero threshold.

A second tempting signal also fails.  The period-six reversible marker and
the period-seven chiral marker define the same quadratic field, but both are
affine reparametrizations of the period-one fixed-point marker:

\[
D^{\mathrm{mark}}_6(s_6)=4D_1(s_6/2),
\qquad
C^{\mathrm{mark}}_7(s_7)=D_1(s_7-2).
\]

Thus the apparent cross-period relation is the lower-period alias

\[
D^{\mathrm{mark}}_6\longrightarrow D_1
\longleftarrow C^{\mathrm{mark}}_7,
\]

not a primitive chronology-preserving Hecke bridge.

## Three objects that must not be conflated

1. $C^{\mathrm{mark}}_6(\sigma)=\sigma-2$ is the published coarse
   orbit-sum marker of the period-six chiral doublet.
2. $P_6(A,x)=f_{\eta}(x)f_{-\eta}(x)$, with
   $\eta^2=A-3$, is the published six-coordinate carrier.
3. $E_6$ is the new smooth projective normalization of the twelve valid
   ordered edges of that doublet.

The separate polynomial $D^{\mathrm{mark}}_6$ used in the lower-period
shadow belongs to a reversible/self-conjugate period-six class.  It is not
the chiral cover $E_6$.

## Coordinate and clock conventions

The Paper-5 recurrence

\[
q_{t+1}=1-Aq_t^2-q_{t-1}
\]

becomes, under $x_t=Aq_t$ for $A\ne0$,

\[
x_{t+1}=A-x_t^2-x_{t-1}.
\]

HCS-C19/C20 use the edge $(x_i,x_{i-1})$, for which the forward time map is

\[
H_A(x,y)=(A-x^2-y,x).
\]

The C21 code instead stores $(x_i,x_{i+1})$.  Its forward edge shift is

\[
(x_i,x_{i+1})\mapsto(x_{i+1},x_{i+2})
=H_A^{-1}(x_i,x_{i+1}).
\]

These generators are inverse and conjugate by reversal, so their quotient
genera and isotypic dimensions agree.  They are not claimed to be the same
coordinate formula.

The radical is written $\eta$ in prose.  The three dynamical/arithmetic
clocks remain distinct:

- $n$: primitive Hénon period;
- $s$: Hénon time phase;
- $r_F$: Frobenius extension degree.

No chronological evolution is replaced by an averaged transition matrix.

## Exact period-six theorem

Put

\[
f_{\eta}(x)
=x^3-(1+\eta)x^2-Ax+A(1+\eta)-1,
\qquad \eta^2=A-3,
\]

and

\[
m_{\eta}(x)=x^2+1-A-\eta.
\]

The map $m_{\eta}$ carries the roots of $f_{\eta}$ bijectively to those
of $f_{-\eta}$.  If $\alpha,\beta,\gamma$ are the roots of
$f_{\eta}$, then every valid ordered state is represented by

\[
(\alpha,m_{\eta}(\beta),\gamma,
  m_{\eta}(\alpha),\beta,m_{\eta}(\gamma)),
\qquad \alpha\ne\beta.
\]

The alternating orbit sum recovers the radical intrinsically:

\[
\eta=
\frac{x_0-x_1+x_2-x_3+x_4-x_5}{2}.
\]

Hence one valid ordered edge recovers the full orbit, the radical, and the
three cubic roots.  It is the splitting-field cover, not an artificially
labelled auxiliary cover.

The two radical sheets are generically disjoint because

\[
\operatorname{Res}_x(f_\eta,f_{-\eta})=8\eta^3.
\]

Over the $\eta$-line the cubic splitting cover has group $S_3$ and
discriminant

\[
\Delta(\eta)=16\eta^4+88\eta^2+125.
\]

Its four finite zeros are simple and infinity is unramified.  Therefore

\[
2g(E_6)-2=6(-2)+4\cdot3=0,
\qquad
\boxed{g(E_6)=1}.
\]

After adjoining the central sheet involution $\eta\mapsto-\eta$, the group
over the $A$-line is

\[
S_3\times C_2\simeq \mathsf D_6,
\]

of order $12$.

Let

\[
w=(\alpha-\beta)(\alpha-\gamma)(\beta-\gamma).
\]

The central involution sends both $\eta$ and $w$ to their negatives.
Thus $v=\eta w$ is invariant under the order-six time subgroup, and a
degree comparison proves the exact fixed field

\[
\mathbb Q(E_6)^{\langle\tau\rangle}
=\mathbb Q(A,v),
\qquad
v^2=(A-3)(16A^2-8A+5).
\]

The cubic on the right has discriminant $-4{,}000{,}000$, so the quotient
also has genus one.  Riemann--Hurwitz makes
$E_6\to E_6/\langle\tau\rangle$ an unramified cyclic cover of degree six.
After base change to $\overline{\mathbb Q}$ and a choice of origin, $\tau$
is a six-torsion translation and

\[
H^1(E_6,\mathbb Q)
\cong \varepsilon_{\mathrm{refl}}^{\oplus2},
\qquad
\tau\mapsto1,
\quad
\rho\mapsto-1.
\]

## Cross-period obstruction

The coarse marker fiber product factors as

\[
(s_6-2s_7+4)(s_6+2s_7)=0.
\]

Its normalization is the disjoint union of the two graphs

\[
s_6=2s_7-4,
\qquad
s_6=-2s_7.
\]

Before normalization the graphs meet at

\[
A=-1,
\qquad
s_6=-2,
\qquad
s_7=1.
\]

As a general clock obstruction, let $(X_m,X_n)$ be integral exact-period
covers with time automorphisms of exact orders $(m,n)$.  If a dominant
nonconstant rational map satisfies

\[
\phi\circ H_m=H_n^k\circ\phi,
\]

then $n\mid km$.  If $\gcd(k,n)=1$, then $n\mid m$.  Hence there is no
clock-faithful dominant map between distinct periods in $\{5,6,7\}$.
This does not exclude clock-forgetting maps, non-dominant boundary maps, or
multivalued correspondences.

## Route-A result

The formal tuple is

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` with status
`ROUTE_A_EXPLORATORY`.

- A1 is weak: native phase and reversal survive exactly, and the first
  certified nontrivial weight-one time sector through $n=7$ is located;
  there is still no all-period primitive tower or repetition law.
- A2 fails: no cross-period trace-class operator or Fredholm determinant is
  defined.
- A3 fails: no Riemann divisor, gamma factor, functional equation, or
  Riemann--von Mangoldt bridge exists.
- A4 is only a formal hint: period seven retains a finite-dimensional
  self-adjoint real chronology correspondence, while period six proves a
  complete $H^1$-level chronology collapse.

Route B is not authorized.

## Reproduce

From this directory:

```bash
python -m pip install -r requirements.txt
python code/c21_producer.py --output results/c21_certificate.json
python code/c21_independent_check.py \
  --certificate results/c21_certificate.json \
  --output results/c21_independent_check.json
python -m unittest discover -s code -p 'test_c21.py' -v
sha256sum -c results/ARTIFACT_HASHES.sha256
```

Frozen result:

- certificate SHA-256:
  `5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc`;
- independent status: `PASS`, 133 named checks;
- regression/fail-closed suite: 14 tests passed.

## Project map

- [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md): question, hypotheses, gates, and
  falsifiers.
- [DERIVATION_PACKAGE.md](DERIVATION_PACKAGE.md): exact proof chain.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md): primary-source and novelty boundary.
- [RESEARCH_SYNTHESIS.md](RESEARCH_SYNTHESIS.md): Stage-1 evidence synthesis.
- [DEVILS_ADVOCATE_CHECKPOINT2.md](DEVILS_ADVOCATE_CHECKPOINT2.md): pressure
  test and resolution ledger.
- [AUTO_REVIEW.md](AUTO_REVIEW.md): two-round manuscript review and closure
  ledger.
- [COMPILE_REPORT.md](COMPILE_REPORT.md): PDF toolchain, hash, font, link, and
  visual-validation record.
- [code/](code/): producer, non-importing checker, and tests.
- [results/](results/): exact certificate and checked report.
- [evaluations/route_a/hcs_c21/](evaluations/route_a/hcs_c21/): formal
  Route-A record.
- [paper/](paper/): LaTeX sources and compiled 17-page bilingual manuscript.
