# Paper 13 Result-Aware Proof-to-Writing Scope

## R120 state and purpose

- Candidate: `henon_primitive_cycle_cover_v1`
- Handoff row: `R120`
- Date: 2026-08-16 UTC
- Prepared authorization target: anonymous, proof-first manuscript drafting
- Current writing authorization: `false`
- Required next verdict: `RESULT_AWARE_HANDOFF_PASS`
- Finalization authorization: `false`, both before and after that verdict
- Figure authorization under this handoff: `false`

This scope prepares, but does not self-authorize, the transition from the
source-approved theorem package and the independently reviewed sealed audit to
an anonymous proof-first draft.  Writing becomes authorized only if a fresh,
role-separated reviewer writes
`notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md`, binds this scope and
`experiments/manuscript_lock.json` by exact SHA-256, verifies every binding and
closed-world rule, and returns the exact verdict
`RESULT_AWARE_HANDOFF_PASS`.  Until then, no manuscript path may be created.
The pass, if issued, authorizes drafting only; it does not authorize figures,
final PDF production, finalization, submission, identity disclosure, or a
terminal integrity claim.

## Authority hierarchy

1. The unique theorem authority is the conjunction of the exact
   `notes/PROOF_PACKAGE.md` bytes at SHA-256
   `9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9`
   and the independent `SOURCE_LOCK_PASS` in
   `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` at SHA-256
   `83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e`,
   which binds source lock SHA-256
   `11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469`.
2. `RESEARCH_QUESTION.md`, `CLAIMS_EVIDENCE_MATRIX.md`,
   `CITATION_VERIFICATION.md`, and `NOVELTY_ASSESSMENT.md` constrain notation,
   evidence attribution, literature positioning, and nonclaims.  They may
   explain the theorem but may not enlarge or replace the proof authority.
3. `results/INDEPENDENT_RESULT_REVIEW.json` at SHA-256
   `a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a`
   has verdict `RESULT_PASS` with scope
   `BOUNDED_IMPLEMENTATION_CONSISTENCY_ONLY`, one registered run, no rerun,
   and zero scientific recomputation by the reviewer.  It is lifecycle and
   bounded-consistency evidence only.
4. The seven sealed R100 runtime objects and their manifest DAG are hash-bound
   in `experiments/manuscript_lock.json` solely to preserve lifecycle
   provenance.  They are not theorem inputs, may not be read by a manuscript
   agent, and may not be promoted through a citation, path, hash, summary, or
   transitive reference.

No machine record may issue or support `PROVED`, `SOURCE_LOCK_PASS`, theorem
validation, scientific truth, or a priority claim.  A machine mismatch could
have falsified the bounded implementation; machine agreement cannot prove
PC1, PC2, or any proof bridge.

## Locked theorem content

### PC1 — normalized primitive-cycle cover

For fixed integers $d,n\geq2$, with

\[
A=\mathbb Q[a,c],\qquad K=\mathbb Q(a,c),\qquad
H_{a,c}(x,y)=(ay+x^d+c,x),
\]

the manuscript may state only the source-approved conjunction:

1. the full cyclic fixed algebra $B_n$ is $A$-free of rank $d^n$;
2. the generic actual-exact-period block $E_n$ is one field of degree
   \(\nu=\sum_{e\mid n}\mu(n/e)d^e\);
3. its relative normalization $S$ is geometrically integral and finite
   locally free of rank \(\nu\);
4. the exact scheme-theoretic scalar fiber is
   $S/aS\simeq D_n=\mathbb Q[c,z]/(\Phi_{d,n})$;
5. $S_0=S^{C_n}$ is finite locally free of rank $r=\nu/n$, with
   $S_0/aS_0\simeq D_n^{C_n}$; and
6. on a common dense finite-etale open, the geometric monodromy on the
   $r$ cycles is $S_r$, with $S_1$ explicitly trivial when $r=1$.

The four objects $B_n,E_n,S,S_0$ must remain distinct.  The scalar quotient
is affine, and the actual-period object is defined first as a generic clopen
idempotent block rather than as an everywhere embedded family.

### PC2 — two separately primitive coordinates

With $F=\operatorname{Frac}(S_0)$,

\[
\tau=\sum_{i=0}^{n-1}z_i,\qquad
\rho=\operatorname{tr}(M_{n-1}\cdots M_0),\qquad
M_i=\begin{pmatrix}d z_i^{d-1}&a\\1&0\end{pmatrix},
\]

the manuscript may state

\[
K(\tau)=F=K(\rho).
\]

The non-base arguments for $\tau$ and $\rho$ must remain separate until the
common full-$S_r$ maximal-stabilizer step.  For each
$s\in\{\tau,\rho\}$, the
multiplication characteristic polynomial is defined basis-freely on
\(\bigwedge_A^r S_0\), lies in $A[T]$, and is irreducible of degree $r$
over $K$.  Here \(\rho\) is the pointwise derivative-return matrix trace,
never a field trace and never the determinant \((-a)^n\).

## The sixteen required proof bridges

The draft must expose all sixteen bridges in this order.  A bridge may move to
an appendix, but it may not disappear, be replaced by a computation, or be
collapsed into a citation that lacks the stated internal argument.

1. **Monic cyclic Groebner basis.**  With a graded variable order,
   \(\operatorname{LM}(g_i)=z_i^d\); pairwise coprime monic leading monomials
   and coefficient-ring division give the standard-monomial $A$-basis and
   rank $d^n$.
2. **Generic etaleness and actual-period idempotent.**  Establish the generic
   finite-etale algebra, isolate the Galois-stable clopen actual-period block
   only there, and obtain its Mobius degree \(\nu\).
3. **Henselian connected lift.**  Lift the scalar exact factor over the
   henselian $a$-adic pair, identify the lift with the generic actual block,
   and use connectedness to prove that $E_n$ is one field.
4. **Finite normalization.**  Use excellence, the Nagata property, and finite
   normalization to prove that $S$ is finite over $A$.
5. **Cohen--Macaulayness and miracle flatness.**  Use normal-surface
   Cohen--Macaulayness, local dimension equality, and miracle flatness to
   obtain finite local freeness of rank \(\nu\).
6. **The $a$-adic divisor and nilpotent exclusion.**  Prove the unique
   height-one prime above $(a)$, ramification index $e=1$, residue degree
   \(\nu\), multiplicity-one divisor, and reducedness through $R_0+S_1$.
7. **Exact scalar fiber.**  Construct the finite birational map from the
   normal scalar dynatomic algebra and conclude $S/aS\simeq D_n$, without
   asserting automatic normalization/base-change compatibility.
8. **Constants and geometric integrality.**  Inject algebraic constants into
   \(\operatorname{Frac}(D_n)\), prove that \(\mathbb Q\) is algebraically
   closed in $E_n$, and deduce geometric integrality of $S$.
9. **Cyclic invariants and base change.**  Extend the faithful generic shift
   to $S$, apply the Reynolds idempotent, prove rank $r$, and prove
   arbitrary invariant base change, including the exact affine quotient
   fiber.
10. **Special-line to global monodromy.**  Use the scalar
    $C_n\wr S_r$ theorem on a common good line, the correctly directed map
    \(\pi_1(U_0)\to\pi_1(U)\), and the time-shift centralizer upper bound to
    obtain global $S_r$ cycle monodromy.
11. **Cyclic invariance of the observables.**  Put both observables in $S_0$
    and define \(\rho\) by the ordered derivative product, with cyclic trace
    invariance and the $n=2$ sign/order check.
12. **Scalar infinity branches.**  Use $c=-q^{-d}$, $z_i=q^{-1}v_i$, and
    primitive root-of-unity words to obtain the leading word sum for \(\tau\)
    and the independently derived inverse word product for \(\rho\).
13. **Separate non-base proofs.**  Treat $d\geq3$ and the binary $n\geq3$
    cases separately, proving \(\tau\notin K\) and \(\rho\notin K\) for
    $r>1$ without using one observable to certify the other.
14. **Full-symmetric stabilizer step.**  Use maximality of
    $S_{r-1}<S_r$, after the two non-base results, to derive each field
    generation statement separately.
15. **Determinant line and irreducibility.**  Define multiplication
    characteristic polynomials on the top exterior power, identify them with
    the generic minimal polynomials/norms, and record the nonzero wedge,
    Vandermonde, and discriminant without fiberwise promotion.
16. **Explicit degree-one boundary.**  Derive the complete $(2,2)$ formulas
    directly and state that they provide no nontrivial monodromy evidence.

## The $(d,n)=(2,2)$ boundary

The boundary record must appear exactly as

\[
\nu=2,\qquad r=1,\qquad \tau=a-1,
\]

\[
z_0z_1=(a-1)^2+c,
\qquad
\rho=4a^2-6a+4+4c.
\]

Both multiplication polynomials are linear.  The manuscript must not assert
\(\tau\notin K\), \(\rho\notin K\), or nontrivial monodromy in this case.
The sealed Q/R equality for these formulas is bounded implementation
consistency only and is not part of this derivation.

## The twelve anti-claims

All twelve restrictions must survive theorem statements, abstract,
introduction, related work, captions, appendices, and any supplementary prose.

1. Formal dynatomic period is not asserted equal to actual exact period on
   every special fiber.
2. The primitive cover is not asserted to be an everywhere embedded
   subscheme of \(\operatorname{Spec}B_n\).
3. Normalization is not asserted to commute with $a=0$ without the
   same-rank, divisor, and nilpotent-exclusion proof.
4. No every-fiber smoothness, reducedness, etaleness, or free cyclic-torsor
   claim is made for $S$ or $S_0$.
5. \(X_0^{\mathrm{aff}}(n)\) is not a projective compactification.
6. The false lower-bound direction
   $G_{\mathrm{global}}\subseteq G_{\mathrm{special}}$ is never used.
7. Non-base behavior alone is not asserted to imply primitivity without full
   $S_r$ and the maximal-stabilizer argument.
8. \(\rho\) is not a field trace and is not \((-a)^n\).
9. Neither \(\tau\notin K\) nor \(\rho\notin K\) is asserted in the
   $r=1$ case.
10. PC1 and PC2 are not extended to arbitrary generalized Henon maps or
    arbitrary polynomial automorphisms.
11. No finite $(d,n)$ table, numerical root ledger, parameter scan, prime or
    modulus check, or machine certificate is treated as proof.
12. Scalar \(\rho\)-primitivity, scalar quadratic \(\tau\)-primitivity, and
    formal trace-spectrum rigidity are not claimed as Paper 13 novelties.

## Related-work and novelty boundary

- Gao--Ou supply scalar affine dynatomic smoothness and geometric
  irreducibility; these are imported inputs, not Paper 13 contributions.
- Morton (1998), Theorem D/Theorem 10, supplies the all-degree scalar wreath
  theorem.  Fakhruddin (2014), Theorem 3.2, supplies its arbitrary
  characteristic-zero-field form and hence the geometric scalar input.
- Morton (1996), Corollary 1 and pp. 335--336, directly gives scalar
  fixed-field generation by
  \(\rho|_{a=0}=\prod_i f'(f^i(z))\) for every $d,n$.  Corollary 3 and
  p. 336 give scalar fixed-field generation by \(\tau|_{a=0}\) when $d=2$.
  The 2011 corrigendum must accompany the citation with its accurately bounded
  finite-characteristic scope.  Paper 13's residual PC2 delta is only the
  two-parameter lift, the uniform \(d\geq3\) \(\tau\) treatment, and the
  integral basis-free characteristic-polynomial package.
- Cantat--Dujardin (2026), Section 3.2 and Theorems A/3.7, use whole
  formal-period trace multisets over finitely many periods to recover Henon
  map parameters up to uniformly finite ambiguity.  That is adjacent to, but
  distinct from, one fixed actual-period cycle field and one-cycle-value
  primitivity.  Neither theorem implies the other.
- Endler--Gallas (2002, 2004) are direct low-period precedents for quadratic
  Henon orbit-sum carriers and stability equations.  Zhang (2014) is a direct
  bounded-period precedent for cyclic-polynomial Henon elimination.  The
  manuscript must not claim invention of an orbit-sum carrier, stability
  carrier, or cyclic-polynomial method.
- Hutz supplies the formal/actual-period warning; Doyle--Poonen supply scalar
  modular-curve context; Friedland--Milnor supply the ambient Henon category.
  None supplies or enlarges PC1/PC2.

Safe positioning is the exact normalized two-parameter conjunction, with PC1
carrying most of the residual contribution and PC2 described as narrower after
the Morton comparison.  Do not use “first,” “previously unknown,” “method
novelty,” “no prior work,” or any statement that the preserved novelty dissent
has been resolved.  Internal novelty scores and venue predictions are not
manuscript claims.  Venue criteria remain unavailable.

## Result-aware disclosure and same-family limitation

At most one short provenance/reproducibility paragraph may mention R100.  It
must convey all of the following, in substance:

> A preregistered, seedless exact audit used two independently implemented
> bounded routes once and sealed the resulting records.  An independent
> integrity review returned `RESULT_PASS` only for bounded implementation
> consistency.  The computation is neither a proof nor theorem validation;
> PC1 and PC2 rest solely on the source proof and its independent source-lock
> review.  All available reviews used one model family, so correlated-error
> risk remains and no cross-model validation is claimed.

That disclosure may appear in a reproducibility or limitations paragraph.  It
must not appear as a theorem premise, proof step, equation justification,
figure, table, quantitative result, abstract headline, contribution bullet,
or novelty argument.  It may identify the independent result-review record
and its hash, but it may not quote, decode, summarize, or cite raw Q/R
certificates or any other runtime object as scientific evidence.

## Closed manuscript read authority

After, and only after, `RESULT_AWARE_HANDOFF_PASS`, a manuscript agent may
read exactly these project-relative paths:

1. `experiments/manuscript_lock.json`
2. `notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md`
3. `notes/RESEARCH_QUESTION.md`
4. `notes/PROOF_PACKAGE.md`
5. `notes/CLAIMS_EVIDENCE_MATRIX.md`
6. `notes/CITATION_VERIFICATION.md`
7. `notes/NOVELTY_ASSESSMENT.md`
8. `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md`
9. `results/INDEPENDENT_RESULT_REVIEW.json`
10. `notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md`

The allowlist is closed and non-transitive.  A pathname, hash, citation,
manifest entry, embedded record, or reference found inside an allowed file
does not grant authority to read the referenced target.  In particular:

- every path under `code/`, `preexecution/`, and `runtime/` is denied;
- under `results/`, only `INDEPENDENT_RESULT_REVIEW.json` is readable;
- the source lock, experiment plan, and tracker are governance bindings for
  the handoff reviewer, not manuscript inputs;
- `refine-logs/`, upstream Paper 12 artifacts, batch dashboards, temporary
  files, caches, and unlisted notes are denied; and
- no tool, subagent, script, citation fetch, or generated summary may expand
  the allowlist indirectly.

## Conditional draft output authority

If the required handoff review passes with no bound-byte drift, the first
drafting stage may create or edit only:

1. `paper/PAPER_PLAN.md`
2. `paper/main.tex`
3. `paper/references.bib`

The draft must remain anonymous: no author name, affiliation, email,
acknowledgment, funding identifier, identifying repository URL, or hidden PDF
metadata.  It must be proof-first: lock notation and theorem statements,
write the complete sixteen-step proof chain and the $(2,2)$ boundary, then
write related work, introduction, and conclusion around that core.  The three
paths above are an exact write allowlist, not directory authority.  They do
not authorize figures, generated build products, reviews, supplementary
files, a final PDF, or any other path.  Later expansion requires a separate
explicit lock and review; it cannot be inferred from this handoff.

## Independent handoff-review contract

The fresh reviewer must not have authored this scope or
`experiments/manuscript_lock.json`.  Its sole write is
`notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md`.  Before returning the only
passing verdict, `RESULT_AWARE_HANDOFF_PASS`, it must:

1. bind the exact SHA-256 of this scope and the canonical manuscript lock;
2. rehash every source, governance, deployment, result-review, and seven-file
   runtime binding in the lock without scientific recomputation;
3. verify that `RESULT_PASS` still means only bounded implementation
   consistency, with registered count one, no rerun, and reviewer scientific
   recomputation count zero;
4. verify PC1, PC2, all sixteen proof bridges, the explicit boundary, all
   twelve anti-claims, and every listed direct/adjacent prior-art boundary;
5. verify the closed, non-transitive manuscript read and write allowlists;
6. verify current writing authorization is false pending its verdict and that
   finalization remains false even after a pass; and
7. report the one-model-family correlated-error limitation.

Any mismatch, missing requirement, scope promotion, path expansion, or hash
drift is a blocker and authorizes no manuscript write.  This handoff is
fail-closed and has no self-signing path.
