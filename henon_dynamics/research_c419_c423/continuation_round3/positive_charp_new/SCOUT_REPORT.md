# Round 3 positive-characteristic scout

Date: 2026-09-07. Outcome: **0 new admissions**. The accepted M1/AS2/IR1 set is unchanged; this lane does not fill either remaining seat and creates no manuscript.

## Frozen candidates and decisions

| Candidate | Original full-family observable | Result | Decision |
|---|---|---|---|
| PC3-A | $f_p(z)=z^p+1/z$ on $\mathbb P^1(\overline{\mathbb F}_p)$, every odd $p$, distinct fixed points of every native iterate and ordinary zeta rationality | Not dynamically affine, but all-cycle return multiplicities remain uncontrolled | **HOLD — PROOF NOT CLOSED** |
| PC3-B | Every ordinary $E$, odd $p$, $g\ge2$, and nonsingular integer $A$ without root-of-unity eigenvalues acting on $E^g/\{\pm1\}$ | Exact native counts and rationality iff $A\bmod p$ is nilpotent follow from a short classical reduction | **REJECT — SHORT CLASSICAL COMPANION** |

Contracts were frozen before any candidate computation. At most these two contracts were deep-screened. The optional integral-polynomial-ring idea was not deep-screened or used as a third replacement.

## PC3-A: a different map, but not a completed theorem

The map has degree $p+1$, is separable, and has exactly one critical point: infinity, fixed with local degree $p$. Therefore it has no totally ramified point and cannot be conjugate to a polynomial or a signed power map. A separable Lattès realization is also impossible: the local degree at that fixed critical point would force unbounded ramification indices in a finite elliptic quotient fiber. See the explicit argument in the [proof package](PROOF_PACKAGE.md).

Faber owns the unicritical continued-fraction structure, while Bridy's dynamical-affine classification excludes the direct existing zeta theorem route; neither fact is a novelty certificate for the desired ordinary zeta classification. The closest general separable-map statement in the inspected Bridy source is a conjecture.

The first native fixed-point equation is

$$z^{p+1}-z^2+1=0.$$

It is squarefree for odd $p\ne3$, whereas at $p=3$ it equals $(z^2+1)^2$. Including infinity,

$$N_{f_p}(1)=3\quad(p=3),\qquad N_{f_p}(1)=p+2\quad(p\ge5).$$

This is a proved symbolic check, not sampled evidence. It defeats the naive multiplicity-free count, not the frozen conjecture. For a native cycle of length $r$, the multiplier is $(-1)^r/(\prod z_i)^2$. Its cycle-dependent order and later wild return multiplicities are not controlled uniformly here. No formula valid for every native $n$ and every odd $p$ was derived. Accordingly this genuinely different structural direction remains on hold, without an admission or an asserted novelty level.

## PC3-B: full closure, then classical subtraction

Put $D_\pm(n)=\det(A^n\pm I)$. The exact distinct-point formula, including quotient branch points, is

$$N_A(n)=\frac{D_-(n)^2p^{-v_p(D_-(n))}+D_+(n)^2p^{-v_p(D_+(n))}}2.$$

The classical quotient count and ordinary elliptic kernel formula own this expression. The full classification is

$$Z_A(t)\in\mathbb Q(t)\iff A\bmod p\text{ is nilpotent}.$$

The short reduction is important: it does **not** pretend that the scalar Kummer theorem's valuation-ring hypothesis automatically holds for arbitrary matrices. If the reduction is nilpotent, both inseparable corrections vanish and even exterior powers give a rational product. Otherwise choose a fixed integer $r$ killing the nonzero eigenvalues of $A\bmod p$. Along $n=rm$, the plus kernel is an unweighted determinant recurrence. Rationality of the original quotient zeta would then force the minus kernel to be recurrent, contradicting the existing abelian/FAD recurrence criterion. The original clock is preserved; the subsequence is only a proof device.

This supplies a full certificate for rejection, not a new research admission. Matrix parameters do not create an independent mechanism beyond Burnside/orbit-stabilizer counting and the existing algebraic-group distortion theorem. No claim of natural boundary, transcendence, or nonholonomicity of the quotient zeta is added.

## Evidence and execution limits

- [SOURCE_AUDIT.md](SOURCE_AUDIT.md) records ten exact additional source queries, including two with a 183-day filter, and the actual closest primary passages read. Preliminary orientation queries were also made; the gate does not depend on counting them.
- [PROOF_PACKAGE.md](PROOF_PACKAGE.md) contains the proved structural checks for PC3-A, its exact missing obligation, and the full classical reduction for PC3-B.
- A targeted local search checked the previous new-characteristic, positive-characteristic, and elliptic scout directories for the exact rational form, matrix/Kummer terminology, and owner identifiers. It found no hits for those strings. This narrow negative result is not an exhaustive local or global novelty claim.
- No candidate CPU experiment, finite-field table, high-degree iterate expansion, GPU job, or independent rerun of IR1/any legacy experiment was performed. Symbolic stop-loss and classical collision checks were sufficient for the decisions.
- The batch, idea-creator, research-lit, bounded ARS verification, and proof-writer instructions informed contract freezing, primary-source scope checks, and explicit separation of proved statements from gaps. No paid/human/external-model process was invoked. This is a current-team scout, not an external review.
- Only the new owned lane contains output files. The initial missing `henon_dynamics/` prefix for the frozen contract was corrected by moving that one self-created file; no mathematical contract changed and no candidate computation preceded the correction. The mistakenly created parent directories remain empty.

## Handoff

Keep PC3-A as unclosed, not admitted. Exclude PC3-B as a short classical companion. Preserve M1/AS2/IR1 and the current no-manuscript status. This bounded lane is finished; no third deep-screen candidate is being opened to manufacture a seat.
