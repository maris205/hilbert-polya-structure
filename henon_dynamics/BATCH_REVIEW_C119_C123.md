# Batch review: HCS-C119--HCS-C123

Date: 2026-08-24

System family: Route-A dynamics variants under the frozen scope firewall
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **continue exploratory Route A; keep Route B unauthorized**.

## Completed paper outputs

1. **C119 -- bosonic-Fock operator for a contraction.**  The frozen matrix has
   eigenvalues \(1/2,1/4\) and squared singular values
   \((7\pm3\sqrt5)/16<1\).  The second-quantized operator \(\Gamma(A)\) is
   trace class and satisfies
   \(\operatorname{Tr}\Gamma(A)^n=((1-2^{-n})(1-4^{-n}))^{-1}\), with
   Fredholm product \(\prod_{i,j\geq0}(1-z2^{-i}4^{-j})\).  Coefficients
   through degree eight and the complete zero multiplicity law are exact.
   This is a genuine source-owned analytic determinant, but the base map has
   only the origin as a periodic point and no target divisor is matched.
2. **C120 -- exact quartic variational three-cycle.**  The cycle
   \((0,-1)\to(1,0)\to(-1,1)\to(0,-1)\) has monodromy
   \(\left(\begin{smallmatrix}-1&0\\-3&-1\end{smallmatrix}\right)\), cyclic
   action \(1/2\), and an action Hessian with determinant four, characteristic
   polynomial \((\lambda+2)(\lambda^2-2\lambda-2)\), and Morse index two.
   Three exact controls reject nearby or structurally altered models.
3. **C121 -- all-order projective degree doubling.**  The forward and inverse
   indeterminacy points are distinct and the exceptional line maps to a
   forward-fixed point, yielding algebraic stability and
   \(\deg H^n=2^n\) for every \(n\geq1\).  Replay through degree 256, two
   algebraic fixed points, and the primitive cycle
   \((0,-2)\leftrightarrow(-2,0)\) are exact.  The dynamical degree two is
   explicitly not called entropy.
4. **C122 -- adaptive-feedback automorphism.**  The three-dimensional map has
   an exact polynomial inverse and constant Jacobian determinant \(1/2\).
   Its two fixed points are
   \((-2\pm\sqrt5,-2\pm\sqrt5,-13\pm6\sqrt5)\), while
   \((1,-1,-3)\leftrightarrow(-1,1,1)\) is a primitive two-cycle.  The
   two-step monodromy has trace \(1/4\), determinant \(1/4\), and
   \(\det(I-zM)=1-z/4+(5/2)z^2-z^3/4\).  Exact controls uniquely isolate the
   feedback gain three and offset \(-1/2\).
5. **C123 -- periodic noise words and exact Markov moments.**  All 126 rooted
   sign words through length six are checked; primitive necklace counts are
   \((2,1,2,3,6,9)\), totaling 23.  A displayed \(2^{-n}\) is the probability
   of the chosen rooted length-\(n\) block, not the total mass of a necklace
   and not an infinite periodic-orbit probability.  The source-owned
   degree-four polynomial Markov operator has dimension 15, trace \(453/256\),
   and determinant \(2^{-80}\).  Its stationary covariance is
   \(\left(\begin{smallmatrix}1088&128\\128&68\end{smallmatrix}\right)/3375\),
   with exact Lyapunov residual zero; the stationary fourth cumulant is also
   reconstructed exactly.

## Uniform release audit

All five packages pass their deterministic producer, checker that imports no
producer code, independent SymPy reconstruction, canonical replay, and
hostile mutation suite.  Mutation rejection totals are 12/12, 21/21, 16/16,
16/16, and 19/19.  Every content-addressed manifest closes at 26/26 files with
matching evidence and PDF hashes.

For every paper, two fresh fixed-date isolated LaTeX builds are byte-identical
to one another and to the checked-in PDF.  All five PDFs have two pages, all
fonts are embedded, and the final logs contain no LaTeX/package warning,
overfull or underfull box, undefined reference, multiply-defined label, or
citation warning.  A rendered ten-page contact audit found no clipping,
truncation, collision, blank content, or visibly broken formula/table layout.

## Integrity and failure-mode audit

- **Implementation bugs as discoveries:** mitigated by independently written
  checkers, direct symbolic reconstruction, canonical evidence replay, and
  hostile mutations that alter mathematical conclusions and scope fields.
- **Hallucinated or irreproducible results:** mitigated by exact rational or
  algebraic arithmetic, deterministic JSON receipts, content hashes, and
  isolated fixed-date builds.  No numerical tolerance or random seed is used.
- **Pipeline frame lock:** mitigated by five materially different systems:
  global Fock second quantization, variational dynamics, birational projective
  geometry, adaptive three-dimensional feedback, and stochastic affine
  moments.
- **Shortcut-to-global-theorem risk:** C119's analytic owner is separated from
  target matching and from nontrivial orbit semantics; every other local,
  low-period, degree, word, or moment prefix carries its explicit cutoff.
- **Bug-as-insight risk:** no failed assertion, compiler warning, or numerical
  accident is repackaged as a mathematical result.  All headline claims pass
  both reconstruction and mutation controls.
- **Methodology or review fabrication:** no external reviewer, acceptance
  score, literature novelty result, or citation is claimed.  Improvement logs
  distinguish internal prose passes from preserved release snapshots.
- **Forbidden arithmetic promotion:** arithmetic data, Euler factors, root
  numbers, automorphy, Hilbert--P\'olya, and Route B occur only in explicit
  nonclaim/firewall statements or deliberately rejected hostile-mutation
  payloads.

## Route-A assessment

Every verdict now uses only labels admitted by
`skills/route-a-evaluator.md`.  The strongest single-candidate tuple in this
round is C120:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
```

C119 is the main conceptual advance of the round: it provides a natural
global function space, a source-defined action, trace-class control, an exact
trace law, and a Fredholm product.  It also exposes the remaining obstruction
cleanly: the underlying contraction has no nontrivial primitive-orbit
structure, its determinant is not primitive-orbit-owned, and it is not
compared with the target; strict A1--A3 therefore fail despite the structural
theorem.  C123 gives a strong finite stochastic operator prefix, but its
degree-four characteristic determinant is not the target-facing dynamical
zeta required by A2.  C120--C122 enlarge exact orbit and geometric coverage
without pretending that tangent data are global transfer owners.  Tuples from
different candidates are not combined coordinatewise.  The correct overall
status is therefore still `ROUTE_A_EXPLORATORY`.

## Next gate

The next five-system round should preserve subtype diversity but prioritize a
candidate combining three features in one source model: nontrivial recurrent
or primitive-orbit dynamics, a natural global function space with a proved
operator trace law, and a frozen target-facing comparison protocol.  Until
that joint bridge is demonstrated, no arithmetic upgrade or Route-B step is
authorized.
