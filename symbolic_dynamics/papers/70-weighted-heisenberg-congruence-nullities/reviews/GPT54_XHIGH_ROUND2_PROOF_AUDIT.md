# GPT54 XHIGH Round 2 Proof Audit

## Provenance and scope

- **Reviewer slot:** official second-round hostile mathematical proof audit for **P70 only**.
- **Audit date:** 2026-08-25 UTC.
- **Frozen package inspected:** complete `papers/70-weighted-heisenberg-congruence-nullities` package, with line-by-line review of current source (`main.tex` and all section files), proof/control/claim ledgers, citation and QA records, prior review files, prior resolution files, control code, frozen control receipt, and current compiled PDF posture.
- **Independent checks performed during this audit:**
  - reran `python3 code/verify_weighted_heisenberg.py` and obtained the frozen terminus `ALL WEIGHTED HEISENBERG CONTROLS PASS`;
  - ran an additional independent 60-case full-matrix sweep outside the frozen receipt on sampled nonzero coefficient triples for `(ell,p)=(3,11),(3,13),(5,19)`;
  - in the same sweep, compared right-translation and left/dual full-matrix nullities on all 60 sampled cases;
  - checked that current `main.pdf` is byte-identical to `main_gpt54_round1.pdf`;
  - extracted current PDF text to confirm the Round-1 wording fixes are present in the built artifact, not only in source.
- **Non-edit statement:** no manuscript, code, or existing package file was modified in this audit. This file is the only new artifact.

## Overall verdict

**Mathematical verdict:** **PASS AS STATED.**

The formula

```text
dim Fix_(N_ell) X_(p;alpha,beta,gamma)
 = D_cycl(alpha,beta,gamma)
   + ell(ell-1) 1_[alpha^ell+beta^ell+gamma^ell=0]
```

is correct under the stated hypotheses:

- `ell` an odd prime;
- `p != ell` prime;
- `alpha,beta,gamma in F_p^x`.

I found **no CRITICAL**, **no MAJOR**, and **no MINOR** new defect in the theorem, proof, manuscript control-language, or source-posture declarations.

**Round-1-fix status:** **PASS.**  
**Hidden-hypothesis audit:** **PASS.**  
**Stale-artifact audit:** **PASS, with historical artifacts clearly fenced by provenance.**  
**External-release verdict:** **EXTERNAL RELEASE HOLD.**

## Severity-ranked findings

### CRITICAL

None.

### MAJOR

None.

### MINOR

None.

## Theorem-by-theorem reconstruction

### 1. Quotient reduction and finite-operator convention

Source: `sections/2_setup.tex:3-34`.

The coordinate law

```text
(r,s,t)(u,v,w)=(r+u,s+v,t+w+rv)
```

gives `ab=bac`, hence `[a,b]=c` with `c` central. For the left shift
`(h.x)_g=x_(h^(-1)g)`, `N_ell`-fixed configurations are constant on left cosets
of the normal subgroup `N_ell`. Identifying the left-coset space with
`Q_ell=Heis(F_ell)`, the local rule

```text
alpha x_g + beta x_(ga) + gamma x_(gb) = 0
```

descends exactly to

```text
(Tf)(q)=alpha f(q)+beta f(qa)+gamma f(qb).
```

This fixes the finite quotient convention and the right-translation operator
with no hidden inverse.

### 2. Base change

Source: `sections/3_regular_decomposition.tex:3-16`.

Nullity is preserved by extension `F_p -> k` to an algebraic closure because
field extension is flat. Therefore the theorem may be proved over `k` and then
descended to `F_p` without changing the kernel dimension.

### 3. Cross-characteristic irreducibles and completeness

Source: `sections/3_regular_decomposition.tex:18-66`.

Over `k`, the paper constructs:

- exactly `ell^2` characters `chi_(u,v)` with `u,v in mu_ell(k)`;
- for each nontrivial `zeta in mu_ell(k)`, one degree-`ell` clock-shift module
  `pi_zeta` with
  `pi_zeta(a)e_j=zeta^j e_j`, `pi_zeta(b)e_j=e_(j+1 mod ell)`,
  `pi_zeta(c)=zeta I`.

I rederived:

- `UV=zeta VU`, matching `ab=bac`;
- irreducibility from distinct clock eigenspaces plus cyclic shift;
- inequivalence of nonlinear blocks from the central scalar;
- completeness from Maschke semisimplicity and the squared-degree ledger
  `ell^2 + (ell-1)ell^2 = ell^3 = |Q_ell|`.

This closes the algebraic-closure irreducible classification with no missing
cross-characteristic step.

### 4. Regular-module multiplicities and right/left audit

Source: `sections/3_regular_decomposition.tex:68-113`.

For matrix coefficients `phi_(lambda,v)(q)=lambda(pi(q)v)`, the right action
satisfies

```text
R_h phi_(lambda,v)(q)=phi_(lambda,pi(h)v)(q),
```

so the right regular block is exactly

```text
alpha I + beta pi(a) + gamma pi(b).
```

Each irreducible of degree `d` occurs with multiplicity `d`, giving:

- characters once each;
- each nonlinear degree-`ell` type with multiplicity `ell`.

The remark on the dual convention is correct: on characters it sends
`(u,v)` to `(u^(-1),v^(-1))`, and on nonlinear modules it sends `zeta` to
`zeta^(-1)`. Those are permutations of the index sets, so the **summed nullity**
is invariant even though the individual block matrices need not be identical.

### 5. Character blocks and the gcd term

Source: `sections/4_character_blocks.tex:7-31`.

On a character block, singularity is the scalar equation

```text
alpha + beta u + gamma v = 0.
```

Because `gamma != 0`, a chosen `u` determines a unique candidate
`v=-(alpha+beta u)/gamma`. Since `ell` is odd, `v^ell=1` is equivalent to

```text
(alpha + beta u)^ell + gamma^ell = 0.
```

Therefore the singular characters are exactly the common roots of
`t^ell-1` and `(alpha+beta t)^ell + gamma^ell`. Since `p != ell`,
`t^ell-1` is separable, so the number of singular character blocks is exactly

```text
D_cycl(alpha,beta,gamma)
 = deg gcd_(F_p[t])(t^ell-1,(alpha+beta t)^ell+gamma^ell).
```

The sign and field-of-definition issues are correctly handled.

### 6. Nonlinear clock-shift determinant

Source: `sections/5_nonlinear_blocks.tex:12-33`.

For `A=alpha I + beta U + gamma V`, with `U=diag(1,zeta,...,zeta^(ell-1))`
and `Ve_j=e_(j+1 mod ell)`, I rederived that the determinant expansion has only
two nonzero permutation terms:

- the full diagonal term;
- the full `ell`-cycle term.

No mixed term survives because the off-diagonal support is one single cycle.
Since `ell` is odd, the cycle sign is `(-1)^(ell-1)=1`. Hence

```text
det(A)=prod_j(alpha+beta zeta^j)+gamma^ell
      = alpha^ell + beta^ell + gamma^ell.
```

This determinant is independent of the chosen nontrivial central character.

### 7. Exact singular corank one

Source: `sections/5_nonlinear_blocks.tex:35-54`.

With the displayed basis, `(Vx)_j=x_(j-1)`, so `Ax=0` is exactly

```text
(alpha+beta zeta^j)x_j + gamma x_(j-1) = 0
```

for `j mod ell`. Since `gamma != 0`, one coordinate determines all others by
backward cyclic propagation. Therefore `dim ker(A) <= 1`. If the determinant is
nonzero, the kernel is zero; if the determinant is zero, the square matrix is
singular and hence has nonzero kernel, forcing `dim ker(A)=1`.

This establishes the exact singular corank-one statement, not merely a
determinant test.

### 8. Regular multiplicities, Fermat jump, and main theorem

Source: `sections/5_nonlinear_blocks.tex:56-63` and `sections/2_setup.tex:48-58`.

There are `ell-1` nonlinear irreducible types, each singular simultaneously on
the Fermat locus

```text
alpha^ell + beta^ell + gamma^ell = 0,
```

each with block nullity `1` and regular multiplicity `ell`. Their total
contribution is therefore `ell(ell-1)`. Adding the character contribution gives
the full formula over `k`, and the base-change lemma descends it to `F_p`.

### 9. Corollaries: projective phase diagram and characteristic-3 specialization

Source: `sections/6_phase_diagram_controls.tex:7-37`.

The projective corollary follows because both the Fermat equation and the gcd
root set are homogeneous under scaling by a nonzero scalar. For unit
coefficients, the nonlinear determinant is `3`, so the jump occurs exactly in
characteristic `3`. The unit-coefficient gcd expression is correct because
`(-1-t)^ell-1` differs from `(1+t)^ell+1` by the unit `-1` when `ell` is odd.

## Explicit audit of the official Round-1 fixes

### R1-M1 control-language narrowing

**Result:** **PASS.**

The official Round-1 hostile review correctly required a narrower statement of
what the finite controls do and do not certify. That narrowing is now present
and internally consistent:

- manuscript control section:
  `sections/6_phase_diagram_controls.tex:39-47` and `:69-76`;
- proof ledger:
  `PROOF_PACKAGE.md:174-186`;
- claims ledger:
  `CLAIMS_EVIDENCE.md:13-23`;
- compiled PDF text:
  extracted current `main.pdf` contains
  `Nullity comparison alone does not distinguish ... because ... the total nullity is invariant`.

The revised language is mathematically correct. The proof, not the computation,
settles the convention choice; the controls remain legitimate regression
evidence for sampled group-law/operator/nullity behavior and for detecting many
transcription or implementation mistakes, including omitted regular
multiplicity.

### R1-M2 priority-neutral introduction

**Result:** **PASS.**

The priority-colored wording has been neutralized correctly:

- `sections/1_introduction.tex:7-10` now says
  `a basic nonabelian nilpotent setting`;
- `sections/1_introduction.tex:22-29` and `:55-59` explicitly disclaim novelty
  for the group, framework, and exact integer element `1+a+b`;
- `sections/7_scope_declarations.tex:3-10`,
  `CITATION_AUDIT.md:23-28`,
  `PAPER_CONFIGURATION.md:35-44`,
  and `FINAL_QA.md:34-40` all maintain the bounded-search/no-priority posture;
- extracted current PDF text contains both
  `basic nonabelian nilpotent setting` and
  `No priority language is intended`.

I found no new priority claim in the manuscript or current ledgers.

### R1 freeze integrity

**Result:** **PASS.**

Current `main.pdf` and `main_gpt54_round1.pdf` have the same SHA-256:

```text
e20e1151597684736d72deeac8875d4be0e5e95d95ef2c187468d07f734f3ac5
```

So the artifact audited here is the same compiled post-Round-1 freeze referenced
by the package ledgers.

## Hidden-hypothesis audit

I found no hidden theorem hypothesis beyond those already declared.

The proof genuinely uses:

- `ell` odd prime:
  oddness for the sign manipulations and prime-order finite Heisenberg count;
- `p != ell`:
  Maschke semisimplicity and separability of `t^ell-1`;
- `gamma != 0`:
  both the character elimination and the cyclic recurrence;
- `alpha,beta != 0`:
  not needed for every algebraic line, but part of the explicitly chosen
  nondegenerate family.

I also checked two common hidden-assumption failure modes:

- the theorem does **not** require `F_p` itself to contain `mu_ell`;
  the proof correctly works over an algebraic closure and descends;
- only the **direct block controls** require sample fields with `ell | (p-1)`;
  that numerical restriction is correctly confined to the control script.

## Stale-artifact audit

I searched for residual stale or contradictory statements after the official
Round-1 fix.

Findings:

- no surviving source or ledger text reintroduces the old control overclaim;
- no surviving manuscript or ledger text makes a priority or worldwide-novelty
  claim;
- historical cross-agent review artifacts remain in the package, but they are
  explicitly provenance-labeled and paired with their own resolutions, so they
  do not contaminate the current official posture;
- the package metadata still says Stage 2.5 is pending official Round 2, which
  is correct for the frozen pre-audit state inspected here.

No unlabeled stale artifact was found.

## Independent control recheck

- Frozen receipt rerun: **PASS**.
- Additional independent full-matrix sweep:
  60 sampled nonzero coefficient triples across `(ell,p)=(3,11),(3,13),(5,19)`,
  with **0 formula mismatches**.
- Right-vs-left total-nullity sweep on the same 60 sampled cases:
  **0 mismatches**, exactly as predicted by the analytic dual-convention audit.

These checks support the proof posture; they are not proof premises.

## Pass/fail summary

- Main theorem: **PASS AS STATED**.
- Finite Heisenberg quotient convention: **PASS**.
- Right regular matrix-coefficient block audit: **PASS**.
- Algebraic-closure irreducibles and completeness: **PASS**.
- Clock-shift determinant: **PASS**.
- Exact singular corank one: **PASS**.
- Dual/index orientation audit: **PASS**.
- Character gcd count: **PASS**.
- Regular multiplicities: **PASS**.
- Fermat jump: **PASS**.
- Characteristic-3 specialization: **PASS**.
- Official Round-1 fixes: **PASS**.
- Hidden assumptions / stale artifacts / new issues: **NO NEW DEFECT FOUND**.

## Remaining Stage 2.5 gates

1. **Specialist exact-statement source audit remains open.**
   The package still documents only a bounded source search. That is a
   responsible posture, but it is not a priority certificate.
2. **Administrative freeze update remains open.**
   The package ledgers and state file can move from
   `awaiting_official_gpt54_round2` only after this Round-2 audit is accepted
   and logged.
3. **No theorem revision is requested by this audit.**
   I found no mathematical or control-language change that should be made before
   recording the official Round-2 result.

## EXTERNAL RELEASE HOLD

The theorem is audit-clean at the mathematical level, and the official
Round-1 wording fixes remain correctly implemented. Nevertheless:

- bounded search is not a worldwide exact-formula audit;
- no priority claim is authorized;
- external release should remain **HOLD** until the specialist exact-source gate
  is closed in the package governance process.
