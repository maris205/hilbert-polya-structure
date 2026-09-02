# P153 independent hostile review A

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal reader; did not author P153.  
**Protocol:** docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md.  
**External state:** HOLD_EXTERNAL. No manuscript content was sent to an
external model or service.

## Verdict

**REVISE — 0 Critical / 0 Major / 2 Minor.**

The all-parameter theorem package is mathematically coherent and stays within
the FTC freeze contract. I found no false central formula, no direct owner of
the owner-subtracted residual conjunction, no verifier mismatch, and no
anonymity failure. The two required repairs are local: make the t=0
observation-partition boundary literal and bring the promised declarations
into agreement with the manuscript.

This is a raw review. I did not edit main.tex, the verifier, transcript, PDF,
or any author ledger.

## 1. Package and theorem-ceiling comparison

I read the final theorem allocation, FTC_FREEZE_CONTRACT.md,
FTC_FOCUSED_AUDIT.md, the FTC owner log, main.tex, all paper-local Markdown
ledgers, references.bib, verify.py, both transcript copies, and the current
five-page PDF.

| Frozen interface | Manuscript interface | Hostile result |
|---|---|---|
| rising-factorial iterate and time-p collapse | Theorem 1(i), Lemma 2 | PASS; explicitly zero-credit input |
| one p-cycle, p-1 labelled depth-p arms, leaf (1,-a) | Theorem 1(ii), Section 2 | PASS |
| temporal polynomial including collapse transition | Theorem 1(iii) | PASS |
| every-time, every-target 1/p/0 fibres | Theorem 1(iv), equations (1), (6) | PASS |
| image size and target/source conservation | equations (2), (3), (7) | PASS |
| pointwise initial-coordinate identifiability | Theorem 1(iv), equation (8) | PASS |
| fixed iterates, unique least-p cycle, zeta | Theorem 1(v), Section 4 | PASS |
| odd-prime, formal-versus-pointwise, leaf-sign, and t>=p boundaries | Sections 2--4 | PASS |

The nested-observation-partition corollary is a direct reformulation of the
frozen fibre atlas, not a material enlargement of the theorem ceiling.
Generic functional-graph and zeta language is not used as independent
contribution value.

## 2. Independent theorem rederivation and proof attacks

### 2.1 Iterate, collapse, and quantifiers

Induction gives

~~~text
T^t(x,y)=(x+t, y product_{j=0}^{t-1}(x+j)).
~~~

The monic degree-p product has all elements of F_p as its simple roots, hence
P_p(X)=X^p-X as a polynomial. Evaluating on F_p makes it zero pointwise.
The manuscript correctly separates the formal identity from this evaluation.
After time p the ordinate stays zero and the first coordinate keeps
translating, so the t>=p saturation clause is valid for every integer t.

The restriction to odd primes is respected. The Z/4 counterexample correctly
shows why replacing the field by a composite ring breaks both first-zero
timing and the fibre trichotomy.

### 2.2 Arm coordinates, equality cases, and leaf sign

For a state at positive depth s, the forced first coordinate is 1-s. Before
the collapse transition, the ordinate is multiplied by

~~~text
(-1)^(s-1) (s-1)!.
~~~

Labelling its depth-one ordinate by a gives exactly the displayed v_(a,s).
Direct substitution proves every arrow. There are p(p-1) such distinct
vertices, which equals the entire off-axis population, so the exhaustion
argument has no hidden component. At s=p, oddness plus Wilson gives
(p-1)!=-1 and hence the leaf (1,-a), not (1,a). The equality case s=1 also
works: v_(a,1)=(0,a) maps directly to (1,0).

Every nonzero ordinate in a fixed source column has the same first-zero time.
There are p-1 states at every depth 1 through p and p recurrent axis states,
which proves the temporal polynomial with the collapse transition included.

### 2.3 Every-target fibres, divisions, and saturation

A time-t target (u,v) forces x=u-t. Its ordinate equation is

~~~text
v = y C_t(u),    C_t(u)=product_{r=1}^t (u-r).
~~~

Division occurs only in the explicitly nonzero case. If the coefficient is
zero, v=0 has all p ordinates and v nonzero has none. For 0<=t<=p, C_t has
exactly t distinct target-column roots. For t>=p the product contains a full
residue system and vanishes in every column. Thus

~~~text
N_1=p(p-r_t), N_p=r_t, N_0=r_t(p-1),
|im T^t|=p(p-r_t)+r_t, r_t=min(t,p).
~~~

Both the codomain partition and source-mass identities check. The abscissa is
recoverable for every feasible observation because it is forced; the ordinate
is recoverable if and only if C_t(u) is nonzero. Impossible targets are not
mistaken for nonidentifiability.

### 2.4 Periodic data

If p does not divide n, first-coordinate translation prevents every fixed
point. If p divides n, then n>=p and T^n(x,y)=(x,0), so exactly the p axis
states are fixed. All have least period p and all off-axis states are
transient. The fixed-count series therefore gives one factor
1/(1-z^p), as stated.

### 2.5 Local boundary defect

Corollary 3 says, for 0<=t<=p, that the t non-singleton columns have abscissae

~~~text
{0,-1,...,1-t}.
~~~

The prose supplies the intended cardinality, but at t=0 this interval-style
set notation is not literally defined as empty. This does not affect the
theorem or verifier, but a quantified boundary should not rely on convention.
This is Finding m1 below.

## 3. Owner attack

### Direct ownership

Ostafe--Shparlinski is correctly treated as a direct family owner. After the
coordinate exchange (Y,X)=(y,x), the map becomes (YX,X+1), the stated
g_0(X)=X, h_0=0, a=b=1 specialization. Therefore the literal construction,
triangular-family membership, degree-growth framework, and elementary
factorial iterate receive zero contribution credit.

### Nearby ownership

Ostafe's maximal-period triangular systems and Maubach's characteristic-p
triangular automorphism/conjugacy work own nearby vocabulary and methods but
not this noninvertible whole-plane graph. Konyagin et al. own generic
finite-field functional-graph background for univariate polynomials. These
are appropriately treated as nearby or standard background.

### Residual and bounded non-hit

The residual is narrowly stated as the complete nonpermutation arm graph plus
the all-time target-resolved fibre/inverse atlas and its periodic
consequences. The manuscript does not convert the bounded conjunction non-hit
into novelty, priority, or ownership-completeness language. I found no
internal evidence that a checked source directly states the residual
conjunction. A future direct source would reopen the slot.

The shorter paper-local source ledger omits some same-family descendants
listed in FTC_FOCUSED_AUDIT.md, but it retains the decisive direct owner and
does not thereby misstate the credit boundary. I do not score that omission.

## 4. Portfolio-collision attack

- **P99/P104:** only product/cocycle notation overlaps. P153 has a
  noninvertible scalar factorial collapse on F_p^2, not HNF layers or random
  invertible matrix words.
- **P150:** this is the closest interface collision. Functional graphs,
  fibres, images, and zeta receive zero standalone credit. P153 is separated
  by polynomial factorial collapse, one translating p-cycle, depth growing
  to p, and the every-time progressive column atlas; it has no Lyness
  totalization.
- **P152:** P152 is an absorbing stochastic reflected-count chain with a
  bivariate Chebyshev transform and mean/parity inverse. No literal carrier or
  proof engine collides.
- **P154:** both are finite noninvertible maps with equal-depth branches, but
  P154 uses arithmetic parity-halving subgroup-normalizer forests, whereas
  P153 has one field-translation cycle and factorial arms.
- **P155/P156:** both later notes have target-resolved rank-changing
  permutation inverses, but their obstructions are right-to-left minima or
  Ferrers matchings. P153's forced abscissa and progressive zero coefficient
  are not those selectors or sections.

The portfolio pass depends on leading with the all-time factorial collapse
atlas rather than generic graph/fibre/zeta language. The manuscript does so.

## 5. Independent exact replay

I cold-ran, in a fresh process:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify.py
~~~

The output matched CANONICAL.txt byte for byte and also matched
verification_output.txt byte for byte. The two frozen transcript files are
themselves identical. The run ended with:

~~~text
PROFILE_SHA256 b44a7815c886a98409b5f56a0c26ce24f8644fa4f6b57a238d5a50d8a2d83810
TOTAL boxes=25 states=75993 assertions=18942551
VERDICT PASS_EXACT_REPLAY
~~~

The verifier audits 25 odd primes through 101, 75,993 states, literal
trajectories, first-repetition graph shape, indegrees, every labelled arm,
every target through t=p+3, and fixed sets through 3p. It uses only integers
and exact modular arithmetic.

This computation does not prove the all-prime quantifier, complete the owner
search, establish novelty or priority, validate extensions to prime powers or
rings, or authorize release. The symbolic proof bears the theorem.

## 6. Source-only build, PDF, and anonymity

A fresh temporary directory containing only main.tex and references.bib
completed

~~~text
pdflatex -> bibtex -> pdflatex -> pdflatex.
~~~

The isolated PDF was byte-identical to the current package PDF at review
time:

~~~text
pages=5, bytes=393462
SHA256=8940cc2979406cd788e9a1c2ed23cb76422c50ff92fe99723608d0cfcb8dfd77
~~~

The settled source-only log had no unresolved citation/reference, rerun,
overfull/underfull, or build warning. All displayed font rows are embedded,
subsetted, and Unicode mapped. PDF metadata has blank title, subject,
keywords, and author; it is A4, unencrypted, and contains no form or
JavaScript.

I rasterized and inspected all five pages. The theorem, dependency display,
inverse table, observation-partition corollary, ownership firewall,
transcript excerpt, and four references are legible and within bounds. No
clipping, overlap, corrupt glyph, unresolved marker, or identifying author
metadata was visible.

The current main.pdf and main_round0_original.pdf are byte-identical, and the
paper-local SHA256SUMS passes for its Round-0 entries. FINAL_QA.md records the
author freeze. No provenance finding remains.

## 7. Findings and required repairs

### m1 — Minor: the t=0 column-set boundary is notation-dependent

**Evidence.** Corollary 3 quantifies 0<=t<=p but writes the root set as
{0,-1,...,1-t}; at t=0 this is not literally an empty set under ordinary
interval notation, although the preceding phrase says there are t columns.

**Required repair.** State separately that there are no non-singleton classes
at t=0, and write {0,-1,...,1-t} only for 1<=t<=p, or use an indexed set such
as {-j:0<=j<t}. Retain the t>=p saturation clause.

### m2 — Minor: paper plan and manuscript declarations disagree

**Evidence.** PAPER_PLAN.md promises declarations in Section 5, but main.tex
ends with a compressed reproducibility/release paragraph. It has no explicit
Limitations, Data Availability, Ethics Statement, Author Contributions,
Conflict of Interest, or Funding declarations. The current fifth page has
ample room.

**Required repair.** Add the standard anonymous house-style declarations,
including the odd-prime/no-prime-power and bounded-owner-search limitations,
or revise the plan only if root explicitly waives the common package
requirement. Keep HOLD_EXTERNAL visible.

## 8. Decision

The mathematical and ownership gates pass. No Critical or Major repair is
required. Internal acceptance is withheld until both Minor items are
closed in source/artifacts, recorded in IMPROVEMENT_LOG.md, and followed by a
settled main_round1.pdf as required by the protocol.

**Verdict: REVISE — 0 Critical / 0 Major / 2 Minor / HOLD_EXTERNAL.**
