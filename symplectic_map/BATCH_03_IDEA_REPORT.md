# Batch 03 Paper-12 Candidate Audit

## Decision

No Paper-12 project is opened in this audit.

The terminal candidate-gate disposition is

```text
BATCH03_PAUSED_NO_PAPERWORTHY_CANDIDATE
```

This is a quality-control decision, not a claim that the research programme has
no remaining open problems.  Three mathematically valid packages were found,
but none simultaneously cleared the proof-maturity, direct-collision, and
standalone-novelty gates required of the first paper in a new five-paper batch.
The strongest package is suitable for a short inverse-spectral note or a theorem
inside a broader paper; the independent novelty audits did not agree that it is
strong enough to serve as the Batch-03 flagship.

No Paper-12 directory, source lock, implementation, registered run, result,
figure package, or manuscript was created.

## Gate used in this audit

A candidate could open Paper 12 only if all of the following held before any
source-lock work:

1. it had a degree- or modulus-independent theorem, rather than another finite
   shell ledger;
2. its proof survived an independent counterexample audit;
3. a primary-source search left at least a defensible standalone novelty level
   of roughly 4/10;
4. its arithmetic input was intrinsic to the proposed object rather than a
   prime label, normalization, selector, or target-dependent spectrum inserted
   by hand;
5. it did not merely restate a standard Euler product, Hasse--Weil zeta,
   moment problem, or Fredholm factorization in the vocabulary of an earlier
   paper; and
6. a passing theorem would materially advance Route A or constrain Route B,
   rather than only rename an already certified obstruction.

Theoretical candidates were permitted to skip a numerical pilot.  No Riemann
zero data, external prime table, new prime scan, or additional periodic-orbit
enumeration was permitted.

## Candidate ranking

| Rank | Candidate | Proof status | Conservative novelty | Gate decision |
|---:|---|---|---:|---|
| 1 | Integer-sampled self-adjoint Fredholm rigidity plus finite-sample blindness | theorem package proved | disputed 2--6/10; aggregate about 4/10 | `STOP_AS_BATCH03_FLAGSHIP`; retain as short-note theorem package |
| 2 | Frozen PCF quadratic: exclude normalized multiplier products \(B_C=\pm1\) for every period | all-period bridge absent; new exact exclusions only for fixed degrees | potentially high only if the all-period theorem is proved | `DO_NOT_OPEN_ON_FINITE_DEGREE_EXTENSION` |
| 3 | Projective fixed-line scheme of the standard cat map and its quadratic Artin factor | corrected theorem proved; general naive version false | about 3/10 for the full boundary package, about 1/10 for the Artin factor | `STOP_STANDARD_ARTIN_FORMALISM` |
| 4 | Fixed finite-rank graded local systems on prime-torsion shells | virtual-rank obstruction proved, but a universal augmentation complex is an exact escape | about 2--4/10 | `STOP_PROVES_TOO_MUCH_ESCAPE` |
| 5 | Quantitative approximate prime-clock equality | standard prime-gap upper bound; no uniform lower bound in the old theorem class | about 3/10 | `CONTROL_ONLY` |
| 6 | Closed-one-form or multivalued logarithmic clocks | reduces to finite topological rank under finite-CW hypotheses | about 2/10 | `LEMMA_ONLY` |
| 7 | Rational \(S\)-unit multipliers for a non-exceptional algebraic Henon map | potentially deep | proof maturity about 1/10 | `LONG_TERM_OPEN_PROBLEM` |

## Candidate 1: integer-sampled Fredholm rigidity

### Strongest safe theorem

Let \(A_+\) and \(A_-\) be compact self-adjoint strict contractions, possibly
on different Hilbert spaces, with \(A_\pm^2\) trace class.  Suppose that for
every integer \(n\ge 2\),

\[
 \frac{\det(I-A_+^n)}{\det(I-A_-^n)}=\zeta(n)^{-1}.
\]

Then the virtual nonzero spectral multiplicity is

\[
 m_+(x)-m_-(x)=
 \begin{cases}
 1,&x=p^{-1}\text{ for a rational prime }p,\\
 0,&x\ne p^{-1}\text{ for every rational prime }p.
 \end{cases}
\]

In particular, all negative net spectrum vanishes.  If common nonzero
multiplicities are cancelled abstractly, there is a compact self-adjoint
Hilbert--Schmidt spectator \(B\) such that, up to the invisible kernel spaces,

\[
 A_+\simeq \operatorname{diag}(p^{-1})_p\oplus B,
 \qquad
 A_-\simeq B.
\]

The same proof works from any complete integer tail \(n\ge n_0>1\), provided
\(|A_\pm|^{n_0}\) is trace class.  It also gives the corresponding virtual
Beurling-prime statement under absolute \(n_0\)-summability.

### Proof contract

Write

\[
 a_m=\operatorname{Tr}(A_+^m)-\operatorname{Tr}(A_-^m),
 \qquad
 b_n=-\log\frac{\det(I-A_+^n)}{\det(I-A_-^n)}.
\]

Self-adjoint strict contraction makes every determinant positive, so the real
logarithm has no branch ambiguity.  The Fredholm expansion gives

\[
 b_n=\sum_{r\ge1}\frac{a_{nr}}r.
\]

The Hilbert--Schmidt and strict-contraction assumptions give exponential tail
bounds, hence absolute convergence of the double series used below.  The
Möbius inversion on multiples is therefore legitimate:

\[
 a_n=\sum_{r\ge1}\frac{\mu(r)}r b_{nr}.
\]

The same formula applied to

\[
 \log\zeta(n)=\sum_{r\ge1}\frac1r\sum_p p^{-nr}
\]

gives \(a_n=\sum_p p^{-n}\).  The raw signed counting measure need not be
finite, so the correct compact moment object is

\[
 \sigma=x^2\left(\nu_+-\nu_--\sum_p\delta_{1/p}\right).
\]

It is a finite signed Borel measure on \([-1,1]\), and all its moments vanish.
Polynomial density and Riesz uniqueness imply \(\sigma=0\).  Taking each
nonzero atom separately gives the virtual multiplicity formula.  Zero
eigenspaces, eigenvectors, and a geometric identification of the common
spectator are not recovered.

The proof uses standard ingredients: the Fredholm log--trace identity,
Fröberg's prime-zeta Möbius formula, and compact Hausdorff moment
determinacy.  The careful points are absolute convergence, the signed weighted
measure, and the distinction between a common spectral multiset and a common
invariant subspace.

### Exact finite-sample blindness

The infinite theorem does not justify finite experimental matching.  Let
\(S=\{n_1,\ldots,n_N\}\subset\{2,3,\ldots\}\) be arbitrary and select
\(N+1\) reciprocal-prime eigenvalues.  Their contribution to the sampled log
determinants is

\[
 \Psi_i(x_1,\ldots,x_{N+1})
 =\sum_{j=1}^{N+1}\log(1-x_j^{n_i}).
\]

The Jacobian entries are

\[
 -\frac{n_i x_j^{n_i-1}}{1-x_j^{n_i}}.
\]

The analytic functions
\(g_i(x)=n_i x^{n_i-1}/(1-x^{n_i})\) are linearly independent because their
lowest powers at zero are distinct.  Reciprocal primes accumulate at zero; if
no \(N\) evaluation columns had full rank, a nonzero analytic linear
combination would vanish on an accumulating set, a contradiction.  The
implicit-function theorem therefore produces a nontrivial local one-parameter
family preserving every determinant sample in \(S\).  Small generic points on
the curve remain positive, distinct, strictly below one, avoid all original
reciprocal-prime atoms, and preserve the Schatten assumptions.

Thus every finite exact determinant sample family is non-identifying even in
the one-sided positive diagonal model.  The analogous trace-sample statement
uses a generalized Vandermonde matrix.

As a proof-development check only, not as research evidence, the frozen
Papers-9--11 primes \(2,3,5,7,11\) were used with samples
\(n=2,3,4,5\).  The resulting rational \(4\times5\) determinant Jacobian has
rank four; all five maximal minors are nonzero.  No new prime was selected or
scanned.

### Direct collisions and novelty decision

The following primary sources sharply limit the claim:

- Fröberg's [prime-zeta paper](https://doi.org/10.1007/BF01933420) contains
  the Möbius inversion recovering the prime zeta function from
  \(\log\zeta\).
- Beurling's [generalized-prime
  theory](https://doi.org/10.1007/BF02546666) and
  [Hilberdink--Lapidus](https://arxiv.org/abs/math/0410270) already place
  generalized-prime Euler products in a spectral/partition-function setting.
- [Hartmann--Lesch](https://arxiv.org/abs/2106.02444) treats the precise
  boundary between zeta determinants and regularized Fredholm determinants;
  these notions cannot be interchanged without correction terms.
- The compact moment step is a direct signed-measure inference from
  Hausdorff's classical moment determinacy, not a new moment theorem.
- Truncated moment nonuniqueness has extensive prior art; the determinant
  Jacobian formulation is useful, but it does not make the other ingredients
  new.

Two independent specialized assessments disagreed.  One assigned
`STOP / 2/10`, because the infinite chain is a short composition of classical
facts and the prime diagonal model inserts the desired spectrum.  The other
assigned `CONDITIONAL_GO / 6/10` only if the paper centred the virtual signed
classification, the integer-tail sampling theorem, both finite-sample IFT
results, and the Beurling corollary.  The combined conservative assessment is
about 4/10.

That is enough to preserve the package as a short theorem note.  It is not
enough to open the first paper of Batch 03 after the prior cat-map obstruction
ladder has already produced several deliberately low-novelty scoped notes.

### Mandatory nonclaims

The theorem does not:

- construct a prime-independent natural operator;
- recover the two operators separately, their kernels, eigenvectors, or a
  relative embedding;
- cover nonnormal or genuinely complex spectra, where holomorphic moments need
  not determine a planar measure;
- cover an arbitrary \(s\)-dependent operator family;
- cover determinant prefactors \(e^{g(s)}\), conditional signed Euler
  products, fractional virtual multiplicities, or an unspecified regularized
  determinant;
- provide noisy or quantitative stability from finite data; or
- open Route B or establish any statement about Riemann zeros.

Its safe route label is

```text
INTEGER_SAMPLED_VIRTUAL_SPECTRUM_RIGIDITY_PROVED
FINITE_FREDHOLM_SAMPLES_NONIDENTIFYING
A0_REQUIRES_RECIPROCAL_PRIME_SPECTRUM
ROUTE_B_NOT_OPENED
```

## Candidate 2: the frozen PCF quadratic all-period tail

For

\[
 g(z)=z^2-u,
 \qquad u^3-2u^2+2u-2=0,
\]

and an exact \(n\)-cycle \(C\), Paper 7 wrote

\[
 \Lambda_C=2^nB_C,
 \qquad B_C=\prod_{z\in C}z.
\]

The desired all-period theorem is \(B_C\ne\pm1\).  The independent proof
attack did not find a degree-independent closure or an exact counterexample.
The strongest nearby nonarchimedean theorem applies only below a strict
multiplier threshold; the equality case needed here is not rigid, and every
period \(n\ge2\) is already at that norm threshold.  Rivera-Letelier's
[2026 paper](https://arxiv.org/abs/2601.12163) therefore does not close the
boundary.

One useful pure-algebra side result was derived.  If
\(P_C(X)=\prod_{z\in C}(X-z)\) and \(s=(-1)^n\), then

\[
 P_C(g(X))=sP_C(X)P_C(-X).
\]

Under \(B_C=\varepsilon\in\{\pm1\}\),

\[
 P_C(\pm u)=P_C(u^2-u)=s,
 \qquad P_C(0)=s\varepsilon.
\]

Coefficient comparison rules out both signs at exact periods four and five,
extending the proof-derived finite range from \(2,3\) to \(2,3,4,5\).
This derivation is retained as a candidate-stage side theorem only: it has not
been source-locked, independently hash-reviewed, or inserted into the frozen
Paper-7 record.  A finite-degree extension cannot substitute for the requested
all-period result.

The high-order local reformulation

\[
 B_C=\pm1
 \quad\Longleftrightarrow\quad
 \operatorname{Tr}\log(z_\alpha/\widehat\alpha)=0
\]

does not help without a new nonvanishing theorem; wild ramification prevents a
uniform finite truncation.  Paper 7 remains unchanged and its all-period tail
remains open.

## Candidate 3: cat eigenlines and a quadratic Artin factor

For the standard cat matrix

\[
 B=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\]

the projective fixed-line equation has discriminant five, and

\[
 \#\operatorname{Fix}
 \bigl(B;\mathbb P^1(\mathbb F_p)\bigr)-1
 =\left(\frac5p\right)
\]

for every prime, including \(2\) and \(5\).  The corresponding reduced
Hasse--Weil factor is \(L(s,\chi_5)\), while the full zero-dimensional
arithmetic zeta is

\[
 \zeta_{\mathbb Q(\sqrt5)}(s)=\zeta(s)L(s,\chi_5).
\]

The tempting generalization to all integral hyperbolic matrices is false.  If

\[
 A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
 \qquad
 g_A=\gcd(b,c,a-d),
\]

then at primes dividing \(g_A\), the reduction of \(A\) is scalar and all
\(p+1\) projective points are fixed.  For

\[
 A=B^2=\begin{pmatrix}5&3\\3&2\end{pmatrix},
\]

one has discriminant \(45\), \(g_A=3\), and at \(p=3\),

\[
 A\equiv-I,\qquad
 \#\operatorname{Fix}-1=3\ne\left(\frac{45}{3}\right)=0.
\]

Dividing the fixed binary quadratic form by its content gives the horizontal
saturation and removes the vertical whole-fibre artifact.  Normalization then
recovers the maximal quadratic order and its primitive Artin factor.  Moreover,
\(F_{A^n}=u_nF_A\), so the horizontally saturated fixed-line scheme is
insensitive to replacing \(A\) by a power; the apparent power sensitivity of
the raw scheme is only vertical bad reduction.

This package cleanly separates two clocks:

- the exponent in the local Hasse--Weil series is finite-field extension or
  Frobenius time;
- it is not the iteration time of \(A^r\) on projective points or toral
  periodic orbits.

The arithmetic base supplies primes intrinsically, but the nontrivial factor is
a standard quadratic Artin factor and the Riemann \(\zeta\) factor is the
universal constant \(H^0\) mode.  The central identity is therefore standard
zero-dimensional Hasse--Weil/Artin formalism, not a new cat-map dynamical
realization.  Direct background includes
[Mantilla-Soler](https://arxiv.org/abs/1310.2990) on Dedekind zeta as a
permutation Artin factor.  The candidate is retained as a positive baseline,
not opened as Paper 12.

Its safe classification is

```text
A0_ANALYTIC_ARITHMETIC_ORIGIN
A1_DYNAMICS_NEUTRAL_OR_STOP_SCOPED
STANDARD_ARTIN_FACTOR
```

## Candidate 4: fixed finite-rank graded local systems

For a fixed finite-dimensional graded local coefficient system, the directed
degree of each orbit factor is its virtual rank.  On a shell with \(m\) orbits,
the total directed degree is multiplied by \(m\), and cancellation cannot
change that degree.  This proves a clean fixed-rank obstruction to compressing
an \(m>1\) shell to one linear Euler factor.

It does not close the richer mechanism.  For every finite permutation set
\(V\), the canonical augmentation sequence

\[
 0\longrightarrow I_V\longrightarrow K^V
 \xrightarrow{\,\varepsilon\,}K\longrightarrow0
\]

gives the exact determinant ratio

\[
 \frac{\det(I-XP\mid I_V)}{\det(I-XP\mid K^V)}
 =(1-X)^{-1}.
\]

This is natural, finite-dimensional, selector-free, and valid for every finite
permutation and composite shell.  It is therefore an exact cohomological escape
but fails A0 by proving too much.  Genuine infinite-dimensional, nonpositive,
or dynamical Fredholm mechanisms remain outside the finite-rank theorem.

## Other retained boundaries

### Approximate prime clocks

The Baker--Harman--Pintz short-interval theorem implies, for sufficiently
large \(L\), that some prime logarithm lies within approximately
\(e^{-0.475L}\) of \(L\).  Thus post-hoc nearest-prime matching at any weaker
tolerance is a generic proves-too-much baseline, not arithmetic emergence.
Effective transcendence lower bounds require algebraic degree, height, and
coefficient controls absent from Paper 6's arbitrary finite-dimensional real
space.  This is a mandatory null control for future approximate-clock work,
not a standalone Paper-12 theorem.

### Closed one-forms and multivalued logarithms

On a finite CW-type carrier, periods of a fixed closed one-form lie in a group
of rank at most \(b_1\).  This is the topological version of Paper 6's finite
rank obstruction.  Algebraic logarithmic gauges add standard transcendence
obstructions but do not create a sufficiency mechanism.  Infinite topology or
adelic arithmetic spaces are real escapes, already represented by mature
positive architectures.

### Rational \(S\)-unit Henon multipliers

A potentially deep long-term problem is whether a fixed non-exceptional
algebraic area-preserving Henon map has only finitely many primitive cycles
whose unstable modulus is a positive rational \(S\)-unit.  Existing multiplier
rigidity results do not provide the required uniform height or unlikely-
intersection theorem.  The conjecture may be paper-worthy if that bridge is
found, but it is not currently justified.

## Re-entry conditions for Batch 03

Batch 03 may be resumed without discarding this audit if at least one of the
following occurs:

1. a degree-independent proof or counterexample closes the PCF all-period
   \(B_C=\pm1\) boundary;
2. a natural, prime-independent self-adjoint or transfer operator is defined
   first and then proved to have reciprocal-prime virtual spectrum, rather than
   being constructed from that spectrum;
3. a genuinely new stability theorem identifies the minimal finite noisy
   Fredholm data needed under explicit rank, decay, separation, or arithmetic
   priors, and survives the truncated-moment and cyclic-resultant literature;
4. a uniform arithmetic-height theorem controls rational \(S\)-unit
   multipliers for non-exceptional Henon maps; or
5. a fixed global generator-sensitive mechanism supplies primitive/repetition
   structure and arithmetic provenance in the same object without a
   modulus-dependent carrier or external label.

Until then, opening Paper 12 would lower the evidentiary standard below the one
used to finish Papers 7--11.

## Audit provenance and safety

- The candidate search was theorem-first.  No numerical pilot was needed or
  run.
- No Paper-12 project directory or source-lock files exist.
- No finalized Paper 1--11 source, code, result, figure, manuscript, review,
  or integrity artifact was changed.
- No Riemann-zero data or external prime table was accessed.
- No new prime, modulus, periodic orbit, or shell was enumerated.
- The only arithmetic values used in a proof-development Jacobian check were
  the already frozen primes \(2,3,5,7,11\).
- Internet retrieval was limited to primary papers, publisher records, and
  official preprints for novelty and theorem-boundary verification.
- Divergent independent novelty assessments are retained rather than averaged
  into a false consensus.

