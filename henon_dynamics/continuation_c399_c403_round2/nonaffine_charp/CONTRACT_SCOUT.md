# Bounded non-affine characteristic-p scout

Date: 2026-09-05. Stage: candidate feasibility; not a numbered paper, manuscript,
batch freeze, formal Route-A evaluation, or novelty certification.

## Scope and admission condition

This lane may inspect at most three explicit separable nonlinear self-maps.
The intended invariant is always the geometric Artin–Mazur germ

$$Z_f(z)=\exp\!\left(\sum_{n\ge1}\#\operatorname{Fix}(f^{\circ n})\frac{z^n}{n}\right),$$

with the original integer iteration clock, and distinct geometric fixed points
over the algebraic closure of the stated finite field. A fixed-scheme length
or a count on one finite extension is not this invariant.

Admission requires an all-period proof mechanism and a substantial increment
after primary-source and repository collisions are deducted. A local
ramification tower, a small census, or an affine/algebraic-group conjugacy is
not enough. At most one candidate can be retained. No all-period analytic
type is presumed in advance.

## Explicit candidate budget

1. $f_1(x)=x+x^6$ on $\mathbb A^1(\overline{\mathbb F}_3)$.
   It has derivative one and is not an additive polynomial: its degree is six,
   not a power of three. Test whether the displacement's forced cube factor
   closes geometric multiplicities beyond the fixed origin.
2. $f_2(x)=x+x^{-2}$ on $\mathbb P^1(\overline{\mathbb F}_2)$,
   with $f_2(0)=f_2(\infty)=\infty$. Test the special wild critical portrait,
   all-period multiplicity recursion, and any hidden dynamically affine owner.
3. $f_3(x)=x^3+x^2$ on $\mathbb A^1(\overline{\mathbb F}_2)$.
   Test whether its single finite critical point, the fixed point zero,
   suffices for global geometric counting; check Chebyshev/subadditive
   conjugacy before treating it as new.

The cheap kill condition is an unaccounted new-period multiple-root factor,
or a proved reduction to an excluded classical dynamically affine class.
The desired theorem for a survivor would give an all-$n$ geometric count
formula and a rigorously deduced rationality/nonrationality statement for
$Z_f$, not merely a formal definition of its coefficients by polynomial gcd.

## Workflow and prior boundary

The Route-A batch, idea-creator, proof-writer, and ARS provenance instructions
are used for scope, feasibility, and honest claim status. The present task is
pure theory: no GPU pilot is applicable. The unavailable legacy external
GPT-5.4 brainstorming/review call is not represented as executed; current-team
internal scrutiny is the permitted fallback. The instruction-driven action is
to test exact obstructions before manuscript drafting.

The frozen `research_c399_c403` snapshot and its two unnumbered drafts are
untouched. `SCOUT_C399_C403.md` section D and the arithmetic-scout closeout
already exclude replacing all-period control with one $\mathbb F_7$ local
jet. C384 owns the prior additive-map synthesis. No target Euler factor,
root number, zero correspondence, A2/A3, or Route-B assertion is made:
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Results: zero retained substantial contracts

The three-candidate budget is now exhausted. No fourth map, numbered paper,
TeX draft, old-manifest edit, index edit, or Git action was performed.

| Candidate | Decisive evidence | Admission result |
|---|---|---|
| $f_1=x+x^6$ over $\mathbb F_3$ | True period-four and period-five square-free factors have multiplicity six, beyond the forced cube and fixed-origin correction | `PARKED / NO ALL-PERIOD CONTRACT` |
| $f_2=x+x^{-2}$ over $\mathbb F_2$ | Explicit degree-three elliptic endomorphism lift on $y^2+y=x^3$; the map is Lattès | `KILL / EXCLUDED CLASSICAL OWNER` |
| $f_3=x^3+x^2$ over $\mathbb F_2$ | True period-five and period-seven multiple-root factors lie outside fixed-point repetition towers | `PARKED / NO ALL-PERIOD CONTRACT` |

The proof-writer outcome for a new all-period $f_1$ or $f_3$ theorem is
`NOT CURRENTLY JUSTIFIED`. The simple counting ansätze are refuted, but
neither zeta's rationality or nonrationality is determined. This lane does
not claim a theorem excluding every possible future route.

The sharpest new elimination is the $f_2$ lift:

$$\psi(x,y)=\left(x+x^{-2},\ y+x^{-3}+\alpha\right),
\qquad\alpha^2+\alpha=1.$$

Direct substitution maps $E:y^2+y=x^3$ to itself, $\psi(O)=O$, and degree
multiplicativity gives $\deg\psi=3$. Hence its apparently promising
characteristic-two pattern belongs to existing group-quotient theory.

Deliverables:

- [Proof and exact gap boundaries](PROOF_PACKAGE.md).
- [Bounded count tables and primitive-period witnesses](EXACT_EVIDENCE.md).
- [Executable exact producer](exact_probe.py) and
  [complete final stdout](EXACT_STDOUT.json).
- [Primary ownership and repository audit](SOURCE_AUDIT.md).

The final exact producer exited zero. Its in-process reconstruction checks
are not an independent review. There has been no formal Route-A evaluation,
no new paper admission, no global novelty clearance, and no target A2/A3
promotion. The two pre-existing complete unnumbered drafts remain untouched.
