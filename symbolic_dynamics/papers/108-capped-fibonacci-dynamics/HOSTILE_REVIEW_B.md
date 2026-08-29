# Independent hostile review B — P108

Review date: 2026-08-29 UTC. Scope: the current post-Review-A manuscript,
bibliography, paper-local evidence and build records, canonical exact
verifier and stored stdout, compiled PDF, historical and within-batch
collision boundaries, and paper-local owner subtraction. This is not final
QA and does not authorize external circulation.

## Verdict and severity

**GO_INTERNAL / HOLD_EXTERNAL.**

The full theorem package is **PROVABLE AS STATED**.

- **CRITICAL: 0.**
- **MATHEMATICAL MAJOR: 0.**
- **OWNER/SCOPE MAJOR: 0.**
- **MINOR: 2, both repaired.**

No theorem formula, quantifier, endpoint, verifier code, or stored control
output changed.

## Repaired findings

### MINOR 1 — ambiguous real-interval semiring claim

The proof-lane paragraph originally called

    ([0,a], min(a,u+v), min(a,uv))

a commutative semiring. Read in the usual way as a real interval, this is
false: for a=10, capped multiplication gives

    (10 tensor 10) tensor 0.1 = 1,
    10 tensor (10 tensor 0.1) = 10.

Thus associativity fails on the real interval. The phase space itself is
integer-valued, and the theorem proofs use only

    min(a,min(a,u)+min(a,v)) = min(a,u+v)

for nonnegative integers. I removed the unnecessary semiring claim,
described the forward route by this clipping identity, and replaced
“finite semiring dynamics” in the conclusion by “finite saturated
dynamics.” The exact-iterate proof and every theorem remain unchanged.

### MINOR 2 — incomplete paper-local batch firewall

Review A had made the P83/P89/P101 boundary explicit, but the manuscript did
not locally disclose its separation from the other four systems in the
current P107–P111 batch. I added the update-level distinction to main.tex,
README.md, and CLAIMS_EVIDENCE.md:

- P107 acts on residue-ring ideals by annihilator then power;
- P109 maps finite-field subspaces by one nilpotent operator;
- P110 joins a partition with its cyclic translate;
- P111 is an iid positive Heisenberg matrix product.

None uses P108's finite integer square, capped second-order addition, or
Fibonacci half-plane hitting clock.

## Independent theorem reconstruction

### 1. Exact iterate

Write the uncapped forms at time t as

    U_t=F_(t-1)x+F_t y,
    V_t=F_t x+F_(t+1)y.

The t=1 pair is exactly (y,min(a,x+y)). If the capped state at time t is
(min(a,U_t),min(a,V_t)), one further update is

    (min(a,V_t),
     min(a,min(a,U_t)+min(a,V_t))).

The clipping identity turns the second coordinate into min(a,U_t+V_t).
The two Fibonacci recurrences then give V_t=U_(t+1) and
U_t+V_t=V_(t+1). This proves the displayed iterate for every integer
a>=1, every state in Q_a, and every t>=1, including partially saturated
orbits.

### 2. Recurrent set, fixed counts, and zeta

A fixed state obeys x=y and y=min(a,2y). On the integer interval this forces
y=0 or y=a. If a state is nonzero, at least one coordinate is at least one,
so both nonnegative Fibonacci forms eventually reach a. Hence every
nonzero state reaches (a,a), and no other cycle can exist in the finite
functional graph.

Therefore each iterate has exactly the same two fixed points. Substitution
in the Artin–Mazur definition gives

    exp(sum_(k>=1) 2 z^k/k)=(1-z)^(-2).

The argument includes a=1 and does not infer cycle absence from finite
control.

### 3. Pointwise depth and CDF

For t>=1, F_t>=F_(t-1) and F_(t+1)>=F_t, so V_t>=U_t. A nonfixed state has
entered the recurrent set at time t exactly when U_t>=a. This gives

    depth(x,y)=min{t>=1:F_(t-1)x+F_t y>=a}.

The two fixed states are correctly excluded from that formula and assigned
depth zero.

At positive time, the states of depth at most t consist of (0,0) plus the
integer points satisfying U_t>=a; (a,a) is already in the half-plane, so
the leading one neither omits nor double-counts it. For fixed x, F_t>=1 and
the allowed integers y begin at

    max(0,ceil((a-F_(t-1)x)/F_t)).

This lower endpoint never exceeds a, because its numerator is at most a.
Thus the manuscript's untruncated upper count is valid, and successive CDF
differences give every exact depth shell.

### 4. Sharp depth and Fibonacci-cap jumps

For every nonzero integer state,

    F_(t-1)x+F_t y >= F_(t-1),

and equality for all t is attained by (1,0). Consequently

    D_a=min{t>=1:F_(t-1)>=a}
       =1+min{k>=0:F_k>=a}.

The repeated value F_1=F_2=1 is an important endpoint: D_1=2, while D_2=4.
Literal small-cap reconstruction gives

    D_1,...,D_8 = 2,4,5,6,6,7,7,7.

Hence the manuscript's refined wording is correct: Fibonacci caps are the
plateau endpoints, and the depth changes when the integer cap passes such
an endpoint. It does not claim a unit jump or claim that every new cap is a
Fibonacci number. Binet bounds give D_a=log_phi(a)+O(1).

### 5. Image, fibres, and Garden-of-Eden states

Solving T_a(x,y)=(u,v) first forces y=u. If v<a, no clipping occurred and
x=v-u is the unique preimage exactly when u<=v. If v=a, the condition is
x>=a-u, giving u+1 integer choices. Therefore

    #T_a^(-1)(u,v) =
      0       if v<u,
      1       if u<=v<a,
      u+1     if v=a.

The image is precisely u<=v. Its cardinality is
(a+1)(a+2)/2, the complementary lower triangle contains a(a+1)/2
Garden-of-Eden states, and summing all fibres returns (a+1)^2. The inverse
route is independent of the Fibonacci induction.

## Owner and scope audit

The four DOI records and their declared roles were checked against
publisher or authoritative records:

- Artin–Mazur, DOI 10.2307/1970384, owns the periodic-point zeta framework;
- Hmamed et al., DOI 10.1007/s11045-010-0107-2, supplies broad
  saturated-system context, not a direct owner of this map;
- Koshy, DOI 10.1002/9781118033067, owns standard Fibonacci identities and
  Binet estimates;
- Miles, DOI 10.1080/00029890.1960.11989593, owns classical generalized
  Fibonacci matrix machinery.

The Miles metadata is confirmed by the
[publisher record](https://www.tandfonline.com/doi/abs/10.1080/00029890.1960.11989593),
and the Artin–Mazur metadata by the
[JSTOR issue record](https://www.jstor.org/stable/i307331). The remaining
metadata agrees with the Springer/Wiley records already documented in
Review A and the batch source report.

Paper-local searches attacked the exact update, the scalar recurrence

    z_(n+2)=min(a,z_(n+1)+z_n),

and the phrases capped, clipped, truncated, bounded, and saturated
Fibonacci recurrence. They found classical Fibonacci material, unrelated
truncated Fibonacci words/series, and broad saturated-control literature,
but no direct theorem-package owner for this finite self-map. This negative
result is not a novelty certificate. Contribution density is elementary
once the clipping identity is observed, so specialist direct-owner review
remains the decisive external gate.

The historical firewall also survives:

- P83 is a countable Catalan renewal shift;
- P89 is a random reset/golden-mean matrix environment;
- P101 randomly composes cap and floor maps on a real interval.

Shared Fibonacci, capping, finite-depth, or census vocabulary does not make
any of these systems conjugate to P108. The paper claims no absolute
novelty or priority.

## Canonical exact-control replay

Fresh command:

    python3 code/verify_capped_fibonacci.py

The run exited zero, and a byte comparison with
code/verification_output.txt was empty.

    capped Fibonacci dynamics exact control: PASS
    assertions=67475970
    states_checked=3622410
    trajectory_formula_checks=60226906
    fibre_formula_checks=3622410
    caps=a=1..220

The verifier exhausts every state for all 220 caps. It compares literal
updates with the iterate formula at every registered time, compares every
observed first arrival and CDF with the analytic formulas, and constructs a
reverse fibre table from raw inputs. It uses no randomness or floating
point. These are finite convention-sensitive falsification lanes, not a
proof for all caps or an owner certificate.

## Four-stage build and PDF audit

The sequence

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

exited zero. The first pass, immediately after the source edit, requested a
normal label rerun; that notice was resolved by the prescribed later
passes. The final main.log/main.blg scan has no warning, undefined
citation/reference, overfull or underfull box, multiply defined label, or
error.

    pages=3
    page_size=A4
    pdf_version=1.5
    bytes=269786
    sha256=610f893fc1bfb6d393777e90f048eefcfa7780789ee9d5b6ddd7d0cd38446c23
    pdftotext_layout=10420 bytes, 152 lines
    fonts=21, all embedded/subsetted/Unicode-mapped

An additional deterministic pdflatex pass reproduced the hash. All three
pages were freshly rendered at 180 dpi and inspected. The long title,
displayed formulas, page breaks, collision paragraph, conclusion, and four
bibliography entries are legible; there is no clipping, collision, broken
citation, malformed equation, or orphan material.

## Residual risks and release gate

1. The principal risk is an undiscovered direct owner in saturated
   recurrence, finite-state control, or semiring literature.
2. The exact iterate and depth threshold are elementary after the clipping
   identity; external contribution density must be judged on the complete
   owner-subtracted portrait rather than any single formula.
3. The verifier is exhaustive only for a<=220 and cannot establish
   infinite-family claims, asymptotics, or literature completeness.
4. No claim is made for cap zero, negative coordinates, signed saturation,
   a varying cap, or a real rather than integer phase square.

Final decision: **GO_INTERNAL / HOLD_EXTERNAL**. Public posting,
submission, specialist contact, and novelty or priority language remain
blocked pending final QA and specialist owner review.
