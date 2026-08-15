# Paper Plan

## Frozen identity and release state

**Working title:** *A Centralizer-Quotient Audit for Cat-Map Torsion
Shells*.

**Article type:** short theory-and-exact-audit negative note.

**One-sentence contribution:** for the fixed Arnold cat matrix, the
cyclic-vector locus is a torsor under the full local centralizer at every
modulus, but its one-class coarse quotient has identity induced dynamics;
the symplectic quotient retains norm classes, and the same full-centralizer
compression holds at composite controls, so an Euler factor still requires
an external modulus clock.

**Required terminal classification:**
`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /
A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

**Novelty calibration:** **2.5--3/10**.  Cyclic commutants, rational-lattice
centralizers, norm-one Hecke groups, invariant quadratic forms, quotient
periods, and equivariant zeta refinements all have direct prior collisions.
The defensible delta is a transparent all-$q$ assembly for one fixed matrix
and a strict Route-A semantic audit.  The note must not claim a new
centralizer classification, a new zeta function, a new Hecke construction,
or historical priority.

> **Release gate:** source, deployment, registered result, independent result
> review, and strict manifest are all closed.  This authorizes only paper
> planning, citation assets, and deterministic figures under the frozen
> scope.  It does not authorize a candidate rerun, a new modulus scan, a
> matrix/parameter search, or any numerical evaluation of $s$, $\log q$, or
> $q^{-s}$.

### Frozen inputs

| Role | Path | SHA-256 / state |
|---|---|---|
| source lock | `experiments/source_lock.json` | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` |
| proof source | `notes/PROOF_PACKAGE.md` | `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c` |
| novelty assessment | `notes/NOVELTY_ASSESSMENT.md` | `6ee0fe2aff13c2d4329496e32f2d6aa190a92a3c3b4904168a21828b646de0a5` |
| claims--evidence matrix | `notes/CLAIMS_EVIDENCE_MATRIX.md` | `03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d` |
| independent source review | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` (`SOURCE_PASS`) |
| deployment review history | `results/CODE_REVIEW.md` | `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0` (Round-2 `DEPLOYMENT_PASS`) |
| exact registered result | `results/EXPERIMENT_RESULTS.json` | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` |
| independent result review | `results/INDEPENDENT_RESULT_INTEGRITY.md` | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` (`RESULT_PASS`) |
| strict result manifest | `results/result_manifest.json` | `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658` (`PASS`) |
| official result report | `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e` |
| official validation report | `experiments/OFFICIAL_VALIDATION_REPORT.md` | `f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a` |

A changed bound input invalidates the plan/figure package and requires a new
asset review.  The figures read these files only; they never import or invoke
the candidate.

## Scope and positioning

### In scope

1. Fix $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$,
   $R_q=\mathbb Z/q\mathbb Z$, the exact additive-order shell $E_q$, the
   cyclic determinant $\Delta_q(v)=\det[v,Av]$, and the cyclic locus
   $\mathrm{CV}_q=\{v:\Delta_q(v)\in R_q^\times\}$.
2. Prove from the universal cyclic basis $[e_1,Ae_1]$ that
   $\operatorname{Cent}_{M_2(R_q)}(A)=R_q[A]$ for every $q\ge2$, and that
   $U\mapsto Ue_1$ identifies $C_q=R_q[A]^\times$ with $\mathrm{CV}_q$.
3. Identify cyclic $A$-orbits with $C_q/\langle A\rangle$ and explain why
   the residual $C_q$ quotient is one class.
4. Separate this set-theoretic compression from quotient dynamics: because
   $A\in C_q$, the induced map on $\mathrm{CV}_q/C_q$ is the identity with
   native primitive period one.
5. Compare the full local $\mathrm{GL}_2$ centralizer with the symplectic
   centralizer $C_q^1=C_q\cap\mathrm{SL}_2(R_q)$.  Use determinant/norm
   covariance to identify $\mathrm{CV}_q/C_q^1$ with the norm image.
6. State the exact norm-image cardinality, $\varphi(q)$ when $5\nmid q$ and
   $\varphi(q)/2$ when $5\mid q$, with the binary and ramified boundaries
   explicit.
7. Keep the full exact-order shell distinct from the cyclic locus.  Record
   the inert/binary, split, and ramified full-shell strata and the limited
   effect of the fixed reversor.
8. Report the one-shot nine-modulus exact ledger at
   $(2,3,5,7,11,4,6,9,10)$ as a finite implementation/falsification control,
   not as proof of the all-$q$ theorem.
9. Use the composite rows as a proves-too-much control: full-centralizer
   multiplicity one is not an intrinsic prime selector.
10. Mark Burnside-ring, orbifold, stacky, groupoid, twisted-sector,
    group-action-zeta, and Hecke/quantum refinements as outside scope rather
    than impossible.

### Explicit nonclaims

- No new cyclic-matrix, centralizer, rational-lattice, finite-field type, or
  prime-power cycle theorem.
- No claim that every local centralizer element lifts to a global integral
  torus symmetry; the construction uses $q$-dependent local
  pseudo-symmetries.
- No identification of $\mathrm{CV}_q$ with the entire shell at split,
  ramified, or corresponding composite moduli.
- No new Artin--Mazur, equivariant, orbifold, stacky, or group-action zeta.
- No impossibility result for enriched quotients that retain stabilizers,
  twists, or source-period decorations.
- No numerical $s$, $\log q$, or $q^{-s}$; no prime/zero data; no prime
  scan; no replacement modulus; no rerun.
- No transfer/Fredholm, quantum, Hecke-eigenfunction, prime/zero
  correspondence, Hilbert--P\'olya, RH, or Route-B claim.

Use **prove**, **identify**, **separate**, **audit**, **record**, and
**obstruct within the coarse quotient**.  Avoid **discover**, **first**,
**canonical zeta**, **construct the Riemann dynamics**, and any claim that the
finer equivariant route has been closed.

## Reader, structure, and length

The intended reader works in arithmetic dynamics, finite-ring dynamics, or
mathematical physics and knows periodic-orbit products but may not know the
finite centralizer literature.  Use a hybrid theoretical/diagnostic structure
with theorem authority first and finite controls second.  Target **9--11 main
text pages**, excluding references and appendices, plus **3--5 appendix
pages**.  The all-$q$ torsor proof, quotient-clock distinction, symplectic
norm boundary, and composite control remain in the main text.

## Claims--evidence matrix

| ID | Manuscript claim | Theorem authority | Exact-audit support | Literature boundary | Status |
|---|---|---|---|---|---|
| C1 | $e_1$ is cyclic and the full matrix commutant is $R_q[A]$ for all $q\ge2$. | `PROOF_PACKAGE`, Steps 1--2. | Exact direct/algebra commutants at nine locked moduli. | BNR 2013, Marais 2014, and Stasinski 2016 make the general setting prior art. | `CLASSICAL_FIXED_MATRIX_PROOF` |
| C2 | $U\mapsto Ue_1$ is a $C_q$-equivariant bijection $C_q\to\mathrm{CV}_q$, so the cyclic locus is a torsor and lies in $E_q$. | Step 3. | Exact closure, freeness, transitivity, and base-map bijectivity. | Elementary cyclic-module consequence; no first-torsor claim. | `PROVED_TORSOR` |
| C3 | Cyclic $A$-orbits form $C_q/\langle A\rangle$ and all have length $\operatorname{ord}_q(A)$. | Step 4. | Exact $A$-orbit partitions and periods. | Gaspari 1994 and BRW 2008 delimit finite-lattice orbit novelty. | `PROVED` |
| C4 | The full residual quotient has one class, but the induced $A$ map is identity with native period one. | Step 4 and quotient definition. | `CV/C=1` and identity transition at all nine moduli. | Gusein-Zade et al. 2015 and Zegowitz 2017 directly delimit the quotient-period semantics. | `PROVED_CLOCK_KILL` |
| C5 | Replacing $z$ by $q^{-s}$ in $(1-z)^{-1}$ supplies an external modulus label, not a quotient return-time law. | Step 9. | Exact external-label flag; zero numeric evaluations. | Miles 2017 and equivariant/orbifold literature show richer definitions require extra data. | `A0_FAIL_COMPONENT` |
| C6 | $C_q^1$-orbits are norm/Delta fibers, with quotient size $|\operatorname{im}N_q|$. | Steps 5--6. | Exact determinant/norm tables, fibers, and orbit partitions. | KR 2000 and KRR 2007 are direct norm-one/quadratic-form collisions. | `PROVED_SYMPLECTIC_BOUNDARY` |
| C7 | $|\operatorname{im}N_q|=\varphi(q)$ if $5\nmid q$ and $\varphi(q)/2$ otherwise. | Step 6, including $p=2,5$. | Exact counts at all nine moduli. | Local norm analysis is established; claim only the frozen fixed-order assembly. | `PROVED_LOW_NOVELTY` |
| C8 | The full shell has one/three/two full-centralizer strata in the inert-binary/split/ramified prime cases; the reversor merges only allowed strata. | Step 7. | Prime rows $2,3,5,7,11$, with no cyclic/noncyclic mixing. | BNR 2013 is the dominant classification/reversing collision. | `CLASSICAL_COROLLARY` |
| C9 | $|\mathrm{CV}_q|$ obeys the CRT local formula, and all four composite controls have one full cyclic quotient class. | Steps 8--9. | Exact rows $4,6,9,10$. | BNR 2013 and Tan--Li 2025 delimit prime-power/composite novelty. | `PROVES_TOO_MUCH_CONTROL` |
| C10 | The finite ledger reproduces the theorem's fixed controls but does not prove any all-$q$ statement. | Proof plus evidence policy. | One registered audit; independent object-level reconstruction; strict manifest. | Methodological scope statement. | `FINITE_FALSIFICATION_ONLY` |
| X1 | Burnside/orbifold/stacky/groupoid/twisted refinements may retain information erased by the coarse quotient. | Not investigated. | None; construction counter is zero. | Gusein-Zade et al., Miles, and Walton provide the adjacent boundary. | `OUTSIDE_SCOPE_PAPER11` |
| X2 | Norm-one Hecke quantization may use $C_q^1$ nontrivially. | Not investigated. | None. | KR 2000 and KRR 2007. | `OUTSIDE_SCOPE_ROUTE_B_CLOSED` |

## Theorem and notation order

Introduce

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad
R_q=\mathbb Z/q\mathbb Z,\quad
\Delta_q(v)=\det[v,Av]=x^2-xy-y^2,
\]
\[
E_q=\{v:\operatorname{ord}_{+}(v)=q\},\quad
\mathrm{CV}_q=\{v:\Delta_q(v)\in R_q^\times\},\quad
C_q=R_q[A]^\times,\quad C_q^1=C_q\cap\mathrm{SL}_2(R_q).
\]

Recommended logical order:

1. universal cyclic basis and commutant;
2. cyclic-locus torsor and exact additive order;
3. cyclic $A$-orbit quotient;
4. full coarse quotient and clock erasure;
5. determinant/norm covariance and the symplectic quotient;
6. norm-image formula;
7. full-shell prime strata and reversor boundary;
8. CRT/composite formula and exact ledger;
9. Route-A decision and enriched-quotient handoff.

## Section-by-section outline

### Abstract (150--180 words)

State the fixed matrix, torsor theorem, full-versus-symplectic quotient
contrast, identity quotient dynamics, and composite proves-too-much control.
Say explicitly that the note is a low-novelty negative audit.  End with the
terminal classification in prose, not machine syntax.  No priority or
equivariant-zeta novelty claim.

### 1. Introduction: multiplicity versus a dynamical quotient (1.2 pages)

Frame the question left by the prime-shell multiplicity audit: can a
centralizer quotient turn many cyclic orbits into one intrinsic Euler-factor
orbit?  Front-load the answer: one set class is obtained only after
quotienting by a group that contains $A$, so the induced clock is erased.
Position BNR 2013, KR 2000, KRR 2007, Gusein-Zade et al. 2015, Zegowitz 2017,
and Miles 2017 at the exact collision sites.  State the three contributions
as (i) fixed-matrix torsor assembly, (ii) full/symplectic/clock separation,
and (iii) exact all-prime-plus-composite audit.  Figure 1 is the hero figure.

### 2. Cyclic vectors and the full local centralizer (1.6 pages)

Prove $\det[e_1,Ae_1]=1$.  A commuting matrix is determined by its value on
the cyclic basis, yielding $\operatorname{Cent}(A)=R_q[A]$.  Show
$[Ue_1,AUe_1]=U[e_1,Ae_1]$ and derive the $C_q$-torsor
$C_q\simeq\mathrm{CV}_q\subset E_q$.  Explain why this is safe for the
specific matrix over zero-divisor rings without asserting the polynomial
commutant formula for arbitrary matrices.  Cite BNR and the finite-ring
centralizer caveat.

### 3. Three quotient layers and their information loss (2.0 pages)

Identify the cyclic orbit set with $C_q/\langle A\rangle$.  Then compare:

- full local centralizer: one cyclic quotient class, generally
  nonsymplectic, identity induced map;
- symplectic centralizer: norm-image classes, still identity induced map;
- reversing extension: possible pairing $d\leftrightarrow-d$, but no general
  collapse of cyclic and noncyclic strata.

Keep $E_q$ and $\mathrm{CV}_q$ visually and verbally distinct.  Explain the
$q$-dependent local pseudo-symmetry cost.  Figure 1 supports this section.

### 4. Norm classes and prime full-shell strata (1.8 pages)

Use $S_q=R_q[T]/(T^2-3T+1)$ and
$N(a+bT)=a^2+3ab+b^2=\det(aI+bA)$.  Prove
$\Delta_q(Dv)=\det(D)\Delta_q(v)$ and
$\mathrm{CV}_q/C_q^1\simeq\operatorname{im}N_q$.  State the norm-image
formula with separate split, inert/binary, and ramified-five explanations.
Then give the prime full-shell counts: cyclic equals full shell for
$p=2,3,7$ controls; split $p=11$ discards two eigenlines; ramified $p=5$
discards the nonzero Jordan eigenline.  Cite KR/KRR and BNR at the relevant
claims.

### 5. Exact nine-modulus audit (1.3 pages)

Present the ordered tuple $(2,3,5,7,11,4,6,9,10)$ and the exact ledger for
$|E_q|$, $|\mathrm{CV}_q|=|C_q|$, $|C_q^1|$,
$\operatorname{ord}_q(A)$, cyclic $A$-orbit counts, and the quotient class
counts.  Report one registered audit, dual exact engines, independent
object-level reconstruction, and the repaired deployment validator history.
Emphasize that all-$q$ authority remains the proof.  Figure 2 supports this
section; the full ledger may also appear as a compact manuscript table.

### 6. Clock semantics and Route-A decision (1.4 pages)

For any finite quotient $Y$ on which the induced map is identity, the native
formal factor is built in the abstract variable $z$ and every primitive
period is one.  The substitution $z=q^{-s}$, or a length $\log q$, is an
external modulus label.  Contrast this with the source $A$-period and with
finer equivariant/decorated constructions.  Show that $q=4,6,9,10$ obtain the
same one-class full cyclic quotient, so the mechanism supplies no intrinsic
prime selector.  Figure 3 supports this section.

### 7. Limitations, enriched-quotient boundary, and conclusion (0.9 pages)

State the low novelty, local pseudo-symmetry cost, cyclic-locus discard, and
finite-control limitations.  Do not infer that Burnside, orbifold, stacky,
groupoid, twisted-sector, or Hecke refinements fail.  Conclude that the
coarse centralizer escape is closed at A0 while Route B remains unopened.

### Appendices (3--5 pages)

- **Appendix A:** complete commutant/torsor and orbit-stabilizer proofs.
- **Appendix B:** CRT norm-image proof, including $p=2$ and ramified $5$.
- **Appendix C:** prime strata, reversor case split, and full-shell/cyclic
  distinction.
- **Appendix D:** exact ledger, result schema, hashes, and one-shot lifecycle.

## Planned publication figures

Exactly three deterministic publication figures are authorized.  Every
figure is generated by an independent script from a hash-checking, read-only
data contract.  Each is emitted as vector PDF, selectable-text/vector SVG,
and 300 dpi PNG.

### Figure 1: Quotient layers and information loss

**Filename/label:** `fig1_quotient_layers.pdf`,
`fig:quotient-layers`.

**Message:** multiplicity-one occurs only at the full local centralizer
layer; the symplectic layer retains norm classes, and both coarse quotient
maps have identity dynamics.

**Layout:** (A) $E_q\supset\mathrm{CV}_q\simeq C_q$ with the split/ramified
discard boundary; (B) the cyclic $A$-orbit layer
$C_q/\langle A\rangle$ followed by the full and symplectic quotients; (C)
information ledger showing what is retained or erased by full $C_q$,
$C_q^1$, and the reversor.  Encode status by text, border/hatch, and color.

**Caption boundary:** the torsor and quotient statements are all-$q$ theorem
claims; displayed prime examples are fixed controls.  The figure must say
that enriched equivariant/stacky objects are outside scope, not ruled out.

### Figure 2: Exact nine-modulus centralizer ledger

**Filename/label:** `fig2_nine_modulus_ledger.pdf`,
`fig:nine-modulus-ledger`.

**Message:** $|\mathrm{CV}_q|=|C_q|$ and $\mathrm{CV}_q/C_q$ has one class
at all nine controls, whereas $C_q^1$ leaves exactly the norm-image class
count and the full shell may contain noncyclic strata.

**Layout:** (A) paired shell/cyclic-locus bars with $|C_q|$ overlaid as an
exact equality marker; (B) grouped exact counts $|C_q|$, $|C_q^1|$, and
cyclic $A$-orbits; (C) annotated heatmap for
$\mathrm{CV}/C$, $\mathrm{CV}/C^1$, $E/C$, $E/C^1$, and prime reversing
$E$-orbits (composite reversing entries marked not audited).  Use the frozen
order, not numeric sorting.

**Caption boundary:** all nine rows are development-seen exact controls;
the general formulas come from the proof.  No trend fitting or inference is
allowed.

### Figure 3: Source clock, coarse identity, and external label

**Filename/label:** `fig3_clock_semantics.pdf`,
`fig:clock-semantics`.

**Message:** source periods $\operatorname{ord}_q(A)$ do not survive either
coarse centralizer quotient; converting the abstract identity factor into a
$q$-indexed Euler factor adds external data, and composites pass the same
construction.

**Layout:** (A) exact source $A$-periods versus native quotient period one
for all nine moduli; (B) semantic pipeline
`source A dynamics -> coarse quotient identity -> (1-z)^(-k)` followed by a
clearly external, dashed specialization $z\mapsto q^{-s}$; (C) prime versus
composite class cards and an explicit boundary pointing to Burnside/orbifold/
stacky/groupoid refinements as untested.

**Caption boundary:** $q^{-s}$ and $\log q$ appear only symbolically; no
numeric value is evaluated.  The figure concerns the coarse quotient only.

## Citation plan

The bibliography key set is frozen in `notes/CITATION_VERIFICATION.md` and
`paper/references.bib`.  Direct collisions must be cited at the claim site:

- `BaakeNeumaerkerRoberts2013` for finite/rational-lattice centralizers,
  cyclic matrices, prime types, reversing symmetries, and local/global scope;
- `KurlbergRudnick2000` and `KurlbergRosenzweigRudnick2007` for norm-one
  centralizers and the invariant quadratic-form obstruction;
- `GuseinZadeLuengoMelle2015`, `Zegowitz2017`, and `Miles2017` for coarse
  quotient periods and enriched/group-action zeta boundaries;
- `Gaspari1994` and `BaakeRobertsWeiss2008` for prime-/finite-lattice orbit
  structure and products;
- `Marais2014`, `Stasinski2016`, and `NoferiniWilliams2024` as ring/cyclic
  commutant terminology and caveats, never as proof of the fixed theorem;
- `TanLi2025` and `Chandra2026` as current finite-ring/cycle-product
  collisions, not as evidence for the centralizer quotient theorem;
- `Walton2018` only for the adjacent arithmetic quotient/twist boundary.

## Reproducibility and review gates

1. The figure loader verifies all eleven frozen hashes listed above before
   reading the strict result JSON.
2. All quantitative figure values come directly from
   `results/EXPERIMENT_RESULTS.json`; theorem/semantic labels are checked
   against the source lock and proof markers.  Candidate code is neither
   imported nor executed.
3. Each of the nine outputs is regenerated twice with fixed metadata,
   `PYTHONHASHSEED=0`, bytecode disabled, fixed SVG hash salt, and fixed
   `SOURCE_DATE_EPOCH`; the hashes must be byte-identical.
4. PDF fonts must be embedded, subset, Unicode-capable, and non-Type-3; PDFs
   and SVGs must contain no raster image objects; SVG text remains selectable;
   PNG fallbacks must report 300 dpi.
5. Original-resolution visual QA must check clipping, overlap, labels,
   grayscale redundancy, semantic arrows, and evidence-boundary wording.
6. Each figure receives a figure/table trace linking source data,
   transformation script/hash, caption claim, supported manuscript claims,
   and limitations.
7. A fresh independent reviewer must audit the plan, BibTeX key set,
   generators, hash bindings, double-run determinism, rendered outputs,
   captions, provenance, and scientific scope.
8. Manuscript drafting/freeze may proceed only after that fresh asset review
   returns `PASS`.

