# Stage 3 Phase-2 Proof Audit and Same-Object Controls

Audit date: **2026-08-13**  
Scope: Route A, gates A3--A4 and certificate gates T0--T7  
Frozen candidates: `DEN-WITT-Z-FIN`, `MOD-GEO`  
Route-B status: **not invoked**

## 1. What is proved here

This note closes the three elementary proof obligations preregistered in
`research_protocol.md`.

1. A local trace germ does not determine a global distribution.  If all
   possible nonzero singular locations are known in advance, then all
   nonzero **singular** germs determine a distribution exactly only modulo a
   term smooth off zero; fixing the zero-time singular germ reduces the
   ambiguity to a globally smooth term.
2. Under the two frozen clocks, repeated modular geodesic lengths and
   rational-prime-power logarithms are disjoint.
3. A certificate assembled coordinatewise from two candidate records fails
   the object-identity gate T0.  A genuine bridge would be additional
   mathematical data, not a relabeling of borrowed fields.

The first and third results are inference/certification theorems.  The second
is a candidate-specific algebraic obstruction.  None is a universal no-go
theorem for future enrichments or time-changed candidates.

The code controls accompanying this note use no Riemann-zero data, perform no
fit, and do not transcribe a cofinite Selberg formula.  The exact cofinite
test-function class and Fourier normalization remain source-acquisition obligations
recorded in `source_matrix.md`.

## 2. Distributional definitions

Let \(Y\subset\mathbb R\) be open.  Write \(\mathcal D'(Y)\) for distributions
and \(\mathcal E(Y)=C^\infty(Y)\) for smooth functions, embedded in
\(\mathcal D'(Y)\) in the usual way.

- Two distributions have the **same full germ** at \(x\) if their
  restrictions agree on some neighborhood of \(x\).
- They have the **same singular germ** at \(x\) if their difference is smooth
  on some neighborhood of \(x\).  This is equality in the stalk of the
  quotient sheaf \(\mathcal D'/\mathcal E\).

These notions must not be interchanged.  Adding a smooth function always
preserves singular germs, but it preserves a full germ only where that
function vanishes on a neighborhood.

## 3. Theorem A: local-germ ambiguity

### Proposition A1 (one audited neighborhood)

Let \(T\in\mathbb R\), let \(U\) be an open neighborhood of \(T\), and assume
that \(\operatorname{int}(\mathbb R\setminus U)\neq\varnothing\).  For every
\(\Theta\in\mathcal D'(\mathbb R)\) there is a different global distribution
\(\widetilde\Theta\) with exactly the same full germ on \(U\).

#### Proof

Choose a nonzero real-valued
\(\psi\in C_c^\infty(\operatorname{int}(\mathbb R\setminus U))\) and set

\[
\widetilde\Theta=\Theta+\psi.
\]

Because \(\psi|_U=0\), the restrictions of the two distributions to \(U\)
are equal.  They are nevertheless different globally: testing their
difference against \(\psi\) gives

\[
\langle\widetilde\Theta-\Theta,\psi\rangle
=\int_{\mathbb R}\psi(t)^2\,dt>0.
\]

Thus even the complete distributional germ near one period does not identify
the global trace.  \(\square\)

The construction permits an arbitrary distribution supported outside \(U\),
not merely a smooth bump.  The smooth choice is sufficient and preserves all
singular-support information.

### Theorem A2 (all nonzero singular germs; exact boundary)

Let

\[
X=\mathbb R\setminus\{0\},\qquad P\subset X,
\]

and let \(\Theta_1,\Theta_2\in\mathcal D'(\mathbb R)\).  Assume

\[
\operatorname{sing\,supp}(\Theta_j|_X)\subset P,
\qquad j=1,2,
\]

so that \(P\) contains every possible nonzero singular location.  If
\(\Theta_1\) and \(\Theta_2\) have the same singular germ at every
\(p\in P\), then

\[
(\Theta_1-\Theta_2)|_X\in C^\infty(X).
\]

Equivalently, the exact global ambiguity left by all nonzero singular germs is

\[
\mathcal A_0=
\{S\in\mathcal D'(\mathbb R):S|_{\mathbb R\setminus\{0\}}
\in C^\infty(\mathbb R\setminus\{0\})\}.
\]

If the singular germ at zero is also fixed, or if both distributions are
known to be smooth near zero, the ambiguity reduces to
\(C^\infty(\mathbb R)\).

#### Proof

Put \(S=\Theta_1-\Theta_2\).  At every \(p\in P\), equality of singular
germs says that \(S\) is smooth on some neighborhood of \(p\).  At every
\(x\in X\setminus P\), the singular-support hypotheses say that both
\(\Theta_1\) and \(\Theta_2\), hence \(S\), are smooth near \(x\).
Local smoothness therefore holds at every point of \(X\), and the sheaf
property gives \(S|_X\in C^\infty(X)\).

Conversely, adding any \(S\in\mathcal A_0\) changes no singular germ at a
nonzero point.  Hence \(\mathcal A_0\) is not only an upper bound but the exact
ambiguity class for those data.  If the zero-time singular germs also agree,
then \(S\) is smooth near zero as well as on \(X\), and is therefore globally
smooth.  Conversely every globally smooth addition preserves every singular
germ.  \(\square\)

### Boundary cases that prevent overclaiming

1. **No singular-support prior.**  If one merely knows the germs at the listed
   periods but has not proved that all other nonzero points are regular, one
   may add \(\delta_q\) at an unlisted \(q\neq0\).  The conclusion “unique
   modulo a smooth term” is then false.  Only the audited local statements
   survive.
2. **Zero time not audited.**  All nonzero singular germs leave the entire
   class \(\mathcal A_0\), not just distributions supported at zero.  For
   example, a distribution may be smooth on the punctured line yet fail to
   extend smoothly through zero.
3. **Full germs rather than singular germs.**  A smooth addition preserves a
   full germ only if it vanishes on a neighborhood of the audited point(s).
   Proposition A1 supplies such additions whenever the complement of the
   audited neighborhoods has nonempty interior.
4. **An operator-defined trace already exists.**  The theorem does not make
   that trace ambiguous.  It says that local periodic-orbit information alone
   cannot reconstruct its smooth, zero-time, continuous, or other non-orbit
   terms.

This is the precise local-to-global boundary needed at T4.  It is compatible
with a Duistermaat--Guillemin local wave-trace expansion and with an exact
global Selberg identity; it does not identify the two theorem types.

## 4. Theorem B: modular and rational-prime clocks do not intersect

### Theorem B1 (quadratic norm obstruction)

Let \(\gamma\in\mathrm{PSL}_2(\mathbb Z)\) be hyperbolic, let \(A\) be either
lift to \(\mathrm{SL}_2(\mathbb Z)\), and put

\[
m=|\operatorname{tr}A|>2,\qquad
\lambda=\frac{m+\sqrt{m^2-4}}2>1.
\]

For the unit-speed hyperbolic clock,

\[
\ell_\gamma=2\log\lambda,\qquad
N_\gamma=e^{\ell_\gamma}=\lambda^2.
\]

Then \(N_\gamma^r\notin\mathbb Q\) for every integer \(r\ge1\).  Consequently,
for every rational prime \(p\) and integers \(r,k\ge1\),

\[
r\ell_\gamma\ne k\log p.
\]

#### Proof

Set \(D=m^2-4\).  The integer \(D\) is not a square: if
\(D=a^2\), then \((m-a)(m+a)=4\); the only positive factorization with the
two factors of the same parity is \(2\cdot2\), which gives \(m=2\), excluded.
Thus \(K=\mathbb Q(\sqrt D)\) is quadratic.  Its nontrivial automorphism
\(\sigma\) sends

\[
\lambda\longmapsto
\frac{m-\sqrt D}{2}=\lambda^{-1},
\qquad
N_\gamma\longmapsto N_\gamma^{-1}.
\]

If \(N_\gamma^r=q\in\mathbb Q\), applying \(\sigma\) gives
\(N_\gamma^{-r}=q=N_\gamma^r\).  This is impossible because
\(N_\gamma>1\).  Hence every positive power is irrational.

If \(r\ell_\gamma=k\log p\), exponentiation gives
\(N_\gamma^r=p^k\in\mathbb Q\), contradicting the preceding paragraph.
\(\square\)

### Corollary B2 (disjoint repeated atomic supports)

Under the frozen clocks,

\[
\{r\ell_\gamma:\gamma\text{ primitive modular hyperbolic},\ r\ge1\}
\cap
\{k\log p:p\text{ rational prime},\ k\ge1\}
=\varnothing.
\]

Therefore no atom-by-atom, clock-preserving identification can transfer
modular Selberg orbit coefficients to Deninger's rational-prime packets.

The conclusion is deliberately narrow.  It does not rule out non-atomic
transforms, a new time change, a new arithmetic flow, or a future
quantization.  A time change alters the frozen candidate and must restart the
Route-A gates, including coefficient and normalization checks.

## 5. Lemma C: coordinatewise splicing fails T0

### Typed certificate model

Let \(F\) be the required field set in `research_protocol.md`, from
`classical_phase_object` through `arithmetic_map`.  A field datum is not an
untyped value; it has provenance

\[
(\texttt{candidate\_id},\texttt{source\_lock}).
\]

A trace-certificate record declares one such identity.  Gate T0 holds only if
every populated field has exactly that declared provenance.  Passing T0 says
nothing by itself about completeness or T1--T7.

### Lemma C1 (no coordinatewise maximum)

Let \(C_D\) and \(C_M\) be records with distinct provenances \(D\neq M\).
Form a record \(C_*\) by selecting at least one field datum from \(C_D\) and
at least one from \(C_M\), without a theorem that transports and rederives
those data in a new object.  Then \(C_*\) fails T0 for every declared identity.

#### Proof

The set of field provenances of \(C_*\) contains both \(D\) and \(M\).
If T0 held for a declared identity \(I\), every populated field provenance
would equal \(I\), forcing \(D=I=M\), contrary to \(D\neq M\).  Relabeling the
record changes no field provenance.  \(\square\)

A source-defined bridge morphism could, in principle, be additional
mathematics: it would need specified source and target objects and proofs that
it preserves the clock, primitive/repetition convention, trace functional,
coefficient, non-orbit terms, and normalization.  It is not supplied by
coordinate selection.  For the frozen DEN/MOD pair, Corollary B2 independently
rules out the most direct atomwise clock-preserving version.

## 6. Deterministic controls

`code/trace_certificate_controls.py` provides three controls.

1. **Exact quadratic-field enumeration.**  For finitely many integer
   hyperbolic traces and repetitions it represents

   \[
   N_\gamma=\frac{m^2-2}{2}+\frac m2\sqrt{m^2-4}
   \]

   with rational coefficients.  It checks exactly that the field norm is one,
   the Galois conjugate is the inverse, and the irrational coefficient of
   every tested positive power is nonzero.  Decimal norm and Galois residuals
   are diagnostics only; Theorem B1 is the proof for all traces and powers.
2. **Sampled bump illustration.**  A compactly supported smooth bump is placed
   away from an audited neighborhood.  The baseline and shifted arrays agree
   exactly on every audited sample but differ globally.  The baseline is a
   regularized plotting proxy, not a numerical model of a distributional
   trace.
3. **Typed T0 audit.**  Same-source records pass the identity check even when
   analytically incomplete; a DEN/MOD coordinatewise splice retains both
   provenances and fails T0.  This tests type discipline, not theorem truth.

The experiment metadata records:

```text
Riemann-zero inputs: 0
fitted parameters: 0
network inputs: 0
random seeds: none
```

No finite decimal separation is used as evidence for Theorem B1, and no
sampled function is promoted to a distributional theorem.

## 7. Separate same-object A3/A4 recommendations

These recommendations preserve the existing candidate evaluations; they do
not create a hybrid evaluation.

| Candidate | Same-object finding | A3 recommendation | A4 recommendation | Route B |
|---|---|---|---|---|
| `DEN-WITT-Z-FIN` | T0 passes and the packet period ledger is intrinsic, but T2--T5 are absent; T6 lacks a trace normalization; T7 has prime-log support but no derived trace weights | retain `A3_FAIL` with evidence `NOT_TESTABLE`; no determinant/trace exists whose analytic structure can be audited | retain `A4_FAIL` with evidence `NOT_TESTABLE`; no frozen Hilbert space, domain, symplectic/contact host, or natural quantization is supplied | not allowed |
| `MOD-GEO` | the geodesic flow and automorphic Laplacian form a genuine same-geometry trace benchmark; the exact local cofinite convention still must be transcribed from an acquired full source; T7 is `REFUTED` for rational-prime support | retain `A3_PARTIAL_ANALYTIC_STRUCTURE` as a non-Riemann calibration result; do not promote it to a rational-prime A3 bridge | retain `A4_NATURAL_QUANTIZATION`; the natural Laplacian cannot repair the failed arithmetic gate | not allowed |

For `DEN-WITT-Z-FIN`, the next smallest theorem is a source-intrinsic analytic
object plus a trace/regularization on an explicit test class, with
choice-independent packet disintegration, cross-packet normalization, and
derived repetition coefficients.  Only after that construction exists can
A3 be tested.

For `MOD-GEO`, the next task is documentary rather than a rescue fit: freeze
one complete cofinite Selberg convention, including every continuous and
non-hyperbolic term.  Its role remains an exact same-object control because
Theorem B1 blocks rational-prime atomic promotion under the standard clock.

## 8. Audit conclusion

The three obligations are `PROVED` at their stated scope.  Their combined
message is not that trace formulae are unavailable: `MOD-GEO` demonstrates an
exact same-object trace architecture.  It is that a local orbit germ is not a
global trace, and a trace architecture from one object cannot be pasted onto
the arithmetic clock of another.  Neither candidate reaches
`A4_ROUTE_B_READY`; `route_b_invocation_allowed` remains `false`.
