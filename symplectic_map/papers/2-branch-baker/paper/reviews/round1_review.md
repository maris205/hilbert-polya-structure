# Round-1 Technical Review

Manuscript: *Finite-Rank Obstructions for Locally Constant Multiplier Clocks: A Certified PCF Markov--Baker Case Study*

Overall score: **5/10**

Recommendation: **Weak reject / major revision**

Line references below are to `paper/manuscript.tex`.

## Summary

This is a careful, disciplined manuscript with a real theorem, a clean affine carrier construction, and unusually good provenance/reproducibility hygiene. After checking the manuscript, proof package, bibliography audit, frozen result manifests, exact ledgers, parent-audit outputs, and the main implementation modules, I did **not** find a serious error in the central finite-rank theorem, the branchwise symplectic calculation, or the rank-one multiplier corollary as stated.

My main reservation is not sloppiness; it is **research-paper significance**. The core theorem is mathematically correct but very elementary once the locally constant finite-memory setting is fixed. The worked PCF case is audited in impressive detail, yet it mostly certifies a negative control for a clock that is explicitly *not* the nonlinear parent derivative cocycle. In its current 16-page form, the manuscript reads more like a carefully documented note/certificate than a contribution strong enough for a full nonlinear-dynamics research article.

I would therefore not recommend acceptance in the current form. I would encourage either:

- a substantial **repositioning as a short note / certified case-study note**, or
- a stronger revision that materially increases the theorem-level novelty or dynamical significance.

## Correctness blockers vs. other limitations

### Correctness blockers I found

- **No core correctness blocker** in Theorem 1 (lines **288-335**), Proposition 2 (lines **461-505**), or Corollary 3 (lines **610-645**) as stated.

### Exact-claim gap that should be fixed before publication

- The manuscript treats the parent quotient as **exactly one** symbolic boundary replacement, yielding the all-period factor \( (1-z^2)/(1-z)=1+z \) (lines **544-564**, and appendix discussion at **927-937**). I believe this claim is probably true for this PCF example, but in the manuscript it is **asserted more than it is proved**. The independent parent audit only verifies it through period 20; that is not the same as a clean all-period argument. This is not a blocker for the main finite-rank theorem, but it is a real gap in one of the exact auxiliary claims.

## Ranked strengths

1. **The main theorem is correct, self-contained, and honestly scoped.**  
   The finite-rank obstruction in lines **288-335** is straightforward but valid, and the manuscript is careful not to overextend it to variable roofs, countable-state models, matrix spectral radii, or smooth derivative cocycles (lines **366-375**, **780-790**).

2. **The branchwise symplectic construction is done carefully.**  
   The carrier setup and the exactness calculation in lines **418-505** are clear and convention-safe. In particular, the manuscript explicitly distinguishes factor orientation from symplectic orientation and proves branchwise exactness via a Liouville primitive rather than hand-waving with determinant one alone.

3. **The separation of four different determinant/zeta objects is exemplary.**  
   Lines **581-631** do a very good job separating the unsigned SFT zeta, the parent quotient, the factor-orientation object, and the Lefschetz convention. This is one of the manuscript’s best expository contributions.

4. **Reproducibility and artifact discipline are unusually strong.**  
   Section 6 and Appendix D-equivalent material (lines **655-754**, **943-1008**) provide a credible, auditable evidence chain. Even though these checks do not increase theorem novelty, they do increase trust in what was actually implemented.

## Ranked weaknesses

### CRITICAL

1. **No critical flaw found in the core theorem/proposition/corollary package.**

### MAJOR

1. **The exact parent-boundary quotient needs a direct all-period proof, not only a declared replacement plus finite audit support.**  
   The manuscript states that the symbolic period-2 orbit \(1\leftrightarrow 2\) is removed and the parent fixed point \(d\) is added, giving the exact factor \(1+z\) and the parent zeta formula (lines **544-564**; appendix lines **923-937**). What is missing is a short rigorous argument that **no other periodic boundary identifications occur**.  
   Actionable fix: add a concise proof from the endpoint dynamics/monotonicity structure showing that \(d\) is the only periodic boundary point producing a coding duplication; otherwise weaken the claim to “verified through period 20.”

2. **The paper’s novelty is too limited for a full article in its current form.**  
   The central observation is that a finite locally constant scalar clock has periodic lengths in the rational span of finitely many local logs (lines **108-115**, theorem at **288-335**). That is correct, but it is also close to the first thing one writes down after formulating the model. The certification apparatus is much more elaborate than the theorem itself.  
   Actionable fix: either (a) reposition the manuscript as a short note centered on a negative certificate, or (b) materially strengthen the mathematical contribution beyond the present finite-span argument.

3. **The PCF case study has limited arithmetic-dynamical force because it explicitly excludes the nonlinear parent derivative cocycle.**  
   The manuscript repeatedly and correctly states that the candidate clock is the source-locked constant-slope baker cocycle, not the nonlinear parent derivative (lines **114-115**, **647-653**, **780-790**). That honesty is good, but it also limits the case study’s significance for readers interested in actual smooth/arithmetic dynamics of the parent map.  
   Actionable fix: retitle/reframe the paper more explicitly around “locally constant clocks on symbolic carriers,” or add a clearly separated discussion of what, if anything, the construction suggests about the parent derivative problem.

4. **Section 6 is too long relative to the mathematical payload.**  
   Lines **660-754** spend substantial space on frozen splits, per-step roundtrip checks, and matched controls. These are useful integrity checks, but they do not materially deepen the theorem or the dynamical insight. The paper risks giving the impression that computational volume is compensating for modest theorem novelty.  
   Actionable fix: compress Section 6 aggressively, move more detail to supplement/appendix, and keep the main text focused on the theorem, the carrier, and the exact quotient/convention issues.

5. **The manuscript still lacks a convincing theorem-focused literature positioning for the finite-rank statement itself.**  
   The prior-art boundary is handled responsibly for the PCF/kneading/baker aspects (lines **185-264**), but there is less evidence that the authors have exhaustively positioned the theorem among standard locally constant roof/cocycle facts. The manuscript avoids an explicit “first” claim, which is good, but the reader still needs a stronger sense of whether this is a folklore observation, a known lemma in another language, or a publishable standalone theorem.  
   Actionable fix: add a brief theorem-focused literature paragraph, or explicitly market the result as a concise certificate/obstruction rather than a major standalone theorem.

### MINOR

1. **The abstract should use the same precision as the main text about symplecticity.**  
   The abstract says the carrier is “exact symplectic on every affine branch” (lines **65-67**), whereas the main text carefully restricts claims to branch interiors and almost-everywhere invertibility (lines **461-505**, **507-513**).  
   Actionable fix: say “exact symplectic on every branch interior” in the abstract.

2. **A standard symbolic-dynamics citation on higher-block recoding / orbit inversion would help.**  
   The proof is self-contained, so this is not a correctness issue, but lines **306-310** and **520-527** would benefit from one standard symbolic-dynamics reference.  
   Actionable fix: add a standard source (for example, Lind--Marcus or Kitchens) for higher-block presentations and primitive-orbit counting conventions.

3. **Some readers will find the implementation/certification language too prominent for a theorem paper.**  
   Labels such as `PRE_A0_STRUCTURAL_PASS`, `A0_FAIL / STRUCTURAL_ONLY`, and `A1_WEAK` appear in scientifically central places (lines **155-157**, **766-775**). They are internally consistent, but they read like project-evaluation tags rather than standard mathematical prose.  
   Actionable fix: keep the labels if needed for provenance, but subordinate them to ordinary mathematical conclusions in the abstract/introduction/conclusion.

## Missing references / literature gaps

1. **Add a standard symbolic dynamics reference** for higher-block recoding and primitive-orbit/Möbius bookkeeping near lines **306-310** and **520-527**.

2. **If the authors want to claim theorem-level novelty rather than “useful certificate,” they need a broader theorem-focused literature search** on locally constant roofs/cocycles and periodic length groups. The current targeted novelty audit is careful, but it is not yet enough to persuade me that the finite-rank observation is new in substance.

## Submission readiness

As a full research paper: **not ready / not recommended for acceptance in current form**.

As a revised specialist note: **potentially yes**, if the authors:

1. add a direct proof of the sole boundary quotient;
2. sharply compress the certification material in the main text;
3. reposition the contribution around a narrow obstruction/certificate;
4. strengthen theorem-specific literature positioning.

## Bottom line

This is a serious and honest manuscript, and I trust the authors’ care. But the current paper combines:

- a **correct but elementary** theorem,
- a **carefully audited but narrow** PCF example,
- and a **large verification apparatus** whose scientific payoff is smaller than its size.

That combination is enough for a respectable note, but not yet enough for me to recommend acceptance as a full nonlinear-dynamics / arithmetic-dynamics research article.
