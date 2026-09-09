# B2: adelic time versus ordinary integer time

2026-09-09 UTC. Lane-owned scout; no admission or manuscript number.

## Frozen original question

For every $F\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ (both $F$ and
$F^{-1}$ integral), every $P,Q\in\mathbb Z^2$, and the native two-sided clock
$n\in\mathbb Z$, determine whether

$$
Q\in\{F^nP:n\in\mathbb Z\}
\quad\Longleftrightarrow\quad
(\forall m\ge2)(\exists n_m\in\mathbb Z)\ F^{n_m}P\equiv Q\pmod m.
\tag{LG4}
$$

All mixed moduli and prime powers remain present. The decisive outcome is a
proof of these full quantifiers, or an explicit triple with all-modulus hits
and no integer-time hit. No finite census settles either alternative.

## Frozen B2 bridge and source subtraction

The inherited R4 arithmetic proof, Sections 2–3, gives for nonperiodic $P$ an
injective homeomorphism

$$
\theta_P:\widehat{\mathbb Z}\longrightarrow
\overline{\{F^nP:n\in\mathbb Z\}},\qquad
\theta_P(t)_m=F^{t\bmod r_m}P\bmod m,
$$

where $r_m$ is the native point period modulo $m$. Thus the exact missing
theorem is $\theta_P^{-1}(\mathbb Z^2)=\mathbb Z$. Periodic starting/target
points and bounded-degree iterates are already handled; the latter belongs
to Segal through the inherited saturated-lattice reduction. C394/Poonen own
local interpolation and adding-machine mechanisms, not this global bridge.

B2 will test whether finite-place interpolation plus global height/product
formula estimates supply **height-controlled representatives of the hitting
cosets**. With $H(R)=\max(1,|R_1|,|R_2|)$ and

$$
\mu_m(P,Q)=\min\{H(F^nP):n\in\mathbb Z, F^nP\equiv Q\pmod m\},
$$

defined when that set is nonempty, the candidate compatibility output is a
uniform bound on $\mu_{j!}(P,Q)$, or a sufficient submodulus bound, whenever
all mixed-modulus hits exist. This is an interface to test, not an assumed
lemma. The investigation will also test whether relevant good-model/Green
function modules provide any information beyond finite-place boundedness.

Before further proof or browsing: no mathematical execution is proposed.
The discriminant is a hand proof of the missing bound, an exact obstruction
to the proposed transfer, or a recorded unclosed original LG4. Merely
showing a height-transfer method fails will not be called a counterexample
to LG4. No old programs, builds, shared state, or Git writes are authorized.

## Outcome

**FULL_QUESTION_UNCLOSED; METHOD_TRANSFER_PARTLY_REFUTED; NOT_ADMITTED.**
The complete argument is in [PROOF_PACKAGE.md](PROOF_PACKAGE.md). Its exact
new diagnostic statements are proved, but none is proposed as a substantial
new paper or a replacement for LG4. No explicit all-modulus false positive
has been found, and the equivalent height-compatibility implication remains
unproved.

| Proposed transfer | Exact result and remaining condition |
| --- | --- |
| All mixed-modulus hits → profinite time | Imported R4 Sections 2–3 already prove this, including uniqueness for nonperiodic $P$. It does not prove diagonal integer time. |
| Finite-place interpolation → archimedean height by continuity | **Refuted:** every nonempty profinite orbit neighborhood contains points of unbounded ordinary height. No real orbit interpolation on compact $\widehat{\mathbb Z}$ can agree with all integer iterates. Proof Sections 3 and 5. |
| GR5 good models → informative finite-place Green values on integral points | **Refuted for these observables:** all forward/backward escape rates are zero on the entire integral locus; fixed affine model changes preserve boundedness. Proof Sections 4–5. |
| Product formula + large modulus → equality | Needs an upper bound for the same chosen representative. The actual product-formula consequence of a nonzero difference is a lower bound $\|F^nP-Q\|_\infty\ge m$, consistent with fast orbit growth. Proof Section 2. |
| Existence of small representatives → integer time | **Proved equivalence:** under all-modulus hits, $Q\in\mathcal O_F(P)$ iff $\sup_{j\ge2}\mu_{j!}<\infty$. The missing implication is the production of this bound, not the bounded-box argument afterward. Proof Section 1. |

The concrete good-model control is $F(x,y)=(y,y^2-x)$, with integral inverse
$(x^2-y,x)$. Its Jacobian and leading coefficient are units at every prime,
and its forward/inverse points at infinity remain distinct under reduction.
The point $P=(0,2)$ is nonperiodic by a strictly increasing scalar recurrence.
Arbitrarily large-height iterates converge to $P$ in all finite-place
topologies. In contrast, $Q=(0,3)$ has the same all-zero finite-place Green
vector but differs from the fixed reduction of $P$ modulo $2$. The first
control defeats continuity of height passage; the second defeats separation
by Green values. Neither is an LG4 counterexample.

## Exact compatibility theorem still missing

For every original $F,P,Q$, without excluding degree growth or nonperiodic
targets, one would need to prove

$$
\left[(\forall m\ge2)\ C_m\ne\varnothing\right]
\quad\Longrightarrow\quad
\sup_{j\ge2}\min_{n\in C_{j!}}H(F^nP)<\infty,
\qquad C_m=\{n:F^nP\equiv Q\pmod m\}.
\tag{HC}
$$

The proof package establishes why this is equivalent to the missing LG4
assertion, not why it is true. A theorem producing an appropriate
submodulus representative bound would also suffice. Bounds for *all*
representatives are false. Bounds for *some* representatives remain possible,
but are not delivered by the current local modules. The distinction between
these two quantifiers is essential.

## Primary-source check and subtraction

The cited external facts are narrowly scoped. Poonen's
[Theorem 1 and Remarks 2–3](https://math.mit.edu/~poonen/papers/p-iteration.pdf)
give coefficientwise near-identity interpolation under
$c>1/(p-1)$, with the dyadic threshold retained. They do not give an
archimedean extension or an arithmetic classification of individual
$p$-adic zero times.

Kawaguchi's [Proposition 4.3, Theorem 6.3, and Proposition
7.5](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf) give good-reduction
Green estimates, global canonical-height decompositions and comparison,
and the equivalence between preperiodicity and orbit boundedness at every
place. The word “every” includes the archimedean places. These results do
not state a height bound for congruence-hitting representatives. The zero
finite-place rates and discontinuity assertions in the proof package are
proved directly, rather than inferred from an unverified general source.

Actual access, all on 2026-09-09 UTC:

- Fully read inherited R4 arithmetic `FROZEN_CONTRACTS.md`,
  `PROOF_PACKAGE.md`, `SOURCE_AUDIT.md`, and `DISPOSITION.md`.
- Fully read C394 `THEOREM_PACKAGE.md`, `SOURCE_AUDIT.md`, and
  `proof/ANALYTIC_PROOF.md`. Its exact displacement identity remains local
  at a specified prime, and no common finite-place/real time extension is
  supplied there.
- Read GR5 R5 arithmetic proof's theorem/interface, assumptions, dependency
  map, initial local Jacobian/highest-homogeneous-term proof, and source
  ownership passages; read its full source audit. No claim of rereading its
  full class-group proof is made. For the present example the identity
  good model is checked directly.
- Opened Poonen's author PDF and read the main theorem, proof, and Remarks
  2–3. Opened Kawaguchi's publisher PDF and read Proposition 4.3 with proof,
  the complete Theorem 6.3 statement, and Proposition 7.5 with proof. The
  theorem's global height proof and the rest of the article were not fully
  reread; no such full-read claim is made.
- No dedicated Zotero/Obsidian interfaces were available in the tool list.
  A bounded relevant local library/script search found no matching resource;
  the arXiv fallback used primary-site web discovery, with no PDF download.

Seven bounded discovery queries were actually issued, with no recency or
domain filter: `"polynomial automorphism" "canonical height" "profinite"`;
`"Hénon" "adelic" "orbit closure"`;
`site:arxiv.org "dynamical" "orbit" "local-global" "height"`;
`"Hénon maps" "local-global"`;
`"polynomial automorphisms" "Brauer-Manin"`;
`"profinite" "canonical height" dynamics`;
`"orbit" "p-adic" "height" "Hénon"`.
They did not yield a primary theorem closing (HC); unrelated search results
were not used as mathematical evidence. This is neither a comprehensive
survey nor a literature certification that LG4 is open or novel.

## Reusable interface and consumers

1. **B1:** keep using the full native all-modulus cosets. The equivalent
   minimum-height test precisely identifies what a new arithmetic bound
   would have to deliver. This does not duplicate direct separation work.
2. **B3 / X1:** GR5 may choose an intrinsic local lattice, but every fixed
   affine change preserves boundedness of the transformed integral orbit.
   Any proposed native-orbit restriction needs an observable stronger than
   the all-zero local escape-rate vector. C394's displacement information is
   stronger than Green values, yet still lacks (HC).
3. **X2:** the no-continuous-height extension is universal for nonperiodic
   integral orbits, not limited to one Hénon coefficient. It survives use of
   a return congruence coset; the proof uses all native integer times.

These interfaces were sent to the coordinator while work was ongoing, with
their hypothesis/output boundaries and suggested consumers. Receiving lanes
must verify compatibility, not count them as completed global rigidity.

## Execution and research status

The batch workflow, proof-writer, and local-first research-lit discipline
kept the original claim fixed and caused the height-transfer failures to be
recorded explicitly. No legacy external-model review or GPU pilot ran.
Author checking only; no independent review is claimed in this lane report.

Mathematical program executions: **0**. Old program reruns: **0**.
PDF/TeX builds: **0**. Formal evaluations, shared-index writes, Git writes,
external model/API uploads: **0**. Only this assigned lane's report and
genuine proof supplement were created. No original full contract was closed.

`NO_BAD_EULER_OR_ROOT_NUMBER`; no target Euler factor, root number, automorphy,
or Hilbert–Pólya conclusion is made.
