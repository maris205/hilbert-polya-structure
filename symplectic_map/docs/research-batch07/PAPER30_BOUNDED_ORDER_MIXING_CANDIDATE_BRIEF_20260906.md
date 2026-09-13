# Candidate brief: coefficient-uniform bounded-order Hénon mixing

Date: 2026-09-06. Status: `SAME_COMPLETE_FROZEN_INPUT_FOR_BLIND_CANDIDATE_REVIEWS`.
This is a candidate-selection brief only. No formal Paper30 project,
manuscript, capacity-measurement exception or physical page count exists.
Route applicability: `NOT_APPLICABLE`.

## 1. The single problem

Can two specified polynomial symplectic permutations generate a walk
that mixes several distinct initial points when every point receives
the **same** random word, uniformly over all coefficients in a fixed
degree? The coefficient quantifier forbids hiding dependence on an
integer lift, coefficient height or generic-parameter exception inside
the spectral-gap constant.

The proposed answer concerns one exact Hénon family over prime fields:
$$
H_{P,j}(x,y)=(P(x)+j-y,x),\quad j=0,1,
\qquad P\in\mathbb F_p[t]\text{ monic},\quad\deg P=d\geq2.
$$
For every fixed $d$, every $p\geq16d^2$, every such $P$ and every
$1\leq m\leq d+1$, the lazy symmetric law on $H_{P,0}^{\pm1}$ and
$H_{P,1}^{\pm1}$ has a positive gap $\delta_d$ on ordered distinct
$m$-point configurations. The constant is the same for all those
coefficients, primes and point orders. The substantive non-affine
range begins at three points.

This is not a general new definition of tuple mixing or a new Feistel
construction. Those notions and the auxiliary randomization argument
have strong direct precedents. The possible increment is the complete
fixed-two-Hénon, all-coefficient spectral theorem and the quantitative
algebraic realization that transfers those precedents to this walk.
It may still be judged too incremental or too short after deductions.

## 2. Exact scientific claims and nonclaims

On $\Omega_{p,m}=\operatorname{Conf}_m(\mathbb F_p^2)$ use normalized
counting measure and
$$
M_{P,m}=\tfrac12I+
\tfrac18\sum_{j=0}^1(\rho_m(H_{P,j})+\rho_m(H_{P,j}^{-1})).
\tag{1}
$$
The same permutation acts on all $m$ coordinates; it is not an
independent product of $m$ single-point walks. Configurations are
ordered and pairwise distinct, including collinear configurations and
ones with repeated coordinate values.

**Main theorem.** There is $\delta_d>0$ with
$$
\langle f,(I-M_{P,m})f\rangle\geq\delta_d\operatorname{Var}(f)
\quad\text{for every }f:\Omega_{p,m}\to\mathbb C
\tag{2}
$$
under all the quantifiers above. In particular the configuration chain
is irreducible and its stationary measure is uniform. Neither of these
facts is assumed in order to prove (2).

**Quantitative realization used by the theorem.** For every $p>d$ and
every polynomial $R$ of degree at most $d$, the shear
$T_R(x,y)=(x+R(y),y)$ has length at most
$$
B_d=12\,2^d-4d-11
\tag{3}
$$
in the auxiliary alphabet $\operatorname{ASL}_2(\mathbb F_p)
\cup\{H_{P,0}^{\pm1}\}$. This is a relative word metric: an arbitrary
special-affine element counts as one letter. It is **not** a claim that
every such element has bounded length in the original four Hénon letters.
The latter issue is handled by a spectral comparison, not by pretending
to have a uniform finite-word sampler for the affine group.

**Mixing consequence.** With $N_{p,m}=(p^2)_m$,
$$
\|\mathcal L(Z_n)-u_{p,m}\|_{\mathrm{TV}}
\leq\tfrac12p^m e^{-\delta_dn}.
\tag{4}
$$
At fixed accuracy the mixing time is $\Theta_{d,\varepsilon}(\log p)$,
uniformly over all the coefficients and allowed $m$. The lower bound
counts the support of at most $5^n$ words. This is an elementary
consequence, not another large stand-alone theorem block.

No claim is made about extension fields, smaller primes, nonmonic
leading coefficients, forward-only walks, $m>d+1$, or full symmetric/
alternating-group Cayley expansion. The range $m\leq d+1$ is an exact
interpolation range for this proof, not a proved sharp barrier to mixing.
Degree-one affine maps preserve triangle area, so they cannot mix all
ordered distinct triples; that boundary is a brief explanation, not
capacity to be expanded into another result.

## 3. Complete input package

Both eventual reviewers must receive the same final brief and these
same full files. They must read the complete inputs, not only summaries,
scores or another agent's description. They may read the linked primary
sources for focused novelty or applicability checks. The old three-point
file contains an alternative quotient proof for provenance; only its
affine comparison is needed for the new main argument.

1. [Original three-point author proof V1](PAPER30_UNIFORM_THREE_POINT_MIXING_PROOF_V1_20260906.md),
   554 lines, SHA256
   `1b2e03a56164f62d02fa8e11ed63b8169105be3a831d0148c3fd72b1896398ba`.
   Steps 1–3 supply the coefficient-uniform affine comparison in arbitrary
   representations. The later quotient proof is not extra body capacity.
2. [Independent affine-chain and three-point audit](PAPER30_THREE_POINT_AFFINE_CHAIN_INDEPENDENT_CHECK_20260906.md),
   343 lines, SHA256
   `1f471faad2485966c22bb8477ea47fc375d0f9ddb550672329e6ca74832d9bb1`.
   Completed and fully read by root, PROVABLE AS STATED. The sole finding
   is a bibliographic `of`/`with` typo in the Wan–Wang title; the new
   interpolation proof does not use that Weil input at all.
3. [Bounded polynomial-shear proof](PAPER30_BOUNDED_POLYNOMIAL_SHEAR_PROBE_20260906.md),
   253 lines, SHA256
   `cd49ecdd80d9ef2694cf3305ea628a43f6a6023c5f4fd88eabd5bd0a2acc3ed5`.
   Complete and fully read by root. It proves (3) with exact alphabet,
   all lower coefficients and all target polynomials specified.
4. [New interpolation/minorisation author proof](PAPER30_INTERPOLATION_MINORISATION_PROOF_20260906.md),
   343 lines, SHA256
   `0f0e3b0a00a51a6165d3795efb1ab028118ca94067bc79df27f7d95bfcee8956`.
   Complete and fully read by root. It supplies the higher-point theorem,
   exact auxiliary kernel and transfer to (1).
5. [New bounded-order independent mathematical audit](PAPER30_BOUNDED_ORDER_MIXING_INDEPENDENT_CHECK_20260906.md),
   356 lines, SHA256
   `932bb59d553b6e555f343a0bba5d1969bae5958de58a08de862ae45be06774e0`.
   Completed and fully read by root. Both new inputs are independently
   PROVABLE AS STATED; no formula, quantifier, field, threshold or
   constant repair is required. The unchanged affine interface was
   explicitly reused without repeating its already passed audit.
6. [Original three-point prior report](PAPER30_HENON_THREE_POINT_MIXING_PRIOR_PROBE_20260906.md),
   178 lines, SHA256
   `a6438cd3fcc234fc1030506eb3b3e550a09f704b5d4c99b6bd2e7a550d16875c`.
7. [All-degree/all-coefficient prior supplement](PAPER30_ALL_DEGREE_THREE_POINT_MIXING_PRIOR_SUPPLEMENT_20260906.md),
   201 lines, SHA256
   `9cfa00837d8f0e1938522e6f447aa6cd0831f8a938c5e5066000bedbd5cbfe20`.
8. [Bounded-order/Feistel prior supplement](PAPER30_BOUNDED_ORDER_MIXING_PRIOR_SUPPLEMENT_20260906.md),
   178 lines, SHA256
   `01d4e12be47a9e4016cc9617030b0bdd0781094c2da8161ff9522db53eceb658`.

All three prior reports were fully read by root. They are incremental
records: the newer report corrects old time-specific statements without
altering the old files. Their search misses have only bounded-search
meaning and do not establish world priority.

This complete brief is now frozen with all eight inputs available and
the new mathematical audit accepted. No candidate score or capacity
decision has yet been made; the earlier authors and mathematical auditors
do not serve as the two fresh candidate reviewers.

## 4. Mathematical architecture, credited once

**Affine control.** Center $P$ by $C_s(x,y)=(x+s,y+s)$,
$s=-a_{d-1}/d$, without treating that relabeling as a bounded word.
The two Hénon generators yield unit translations. Their repeated
finite-difference words yield coefficient-independent shears with
slopes $d!$, after removing the fixed constant $d!(d-1)/2$.
The fixed integer linear pair is non-elementary and generates every
$\operatorname{SL}_2(\mathbb F_p)$ for $p>d$. Bourgain–Gamburd and
Lindenstrauss–Varjú give an affine gap $\gamma_d>0$.
Regular-representation transfer and word comparison give
$$
\|f-Ef\|_2^2\leq (C_d/\gamma_d)\mathcal D_{\mu_P}(f),
\quad C_d=\frac{8+L_d^2+(L_d+2)^2}{2},
\quad L_d=10\,2^{d-2}-4+d!(d-1).
\tag{5}
$$
No affine transitivity on higher tuples is assumed.

**Polynomial shear realization.** The model
$Q_r=\Delta^{d-r}P$ has degree $r$ and leading coefficient $d!/r!$.
Determinant-one diagonal conjugacy multiplies that coefficient by
$t^{r+1}$. The set of $(r+1)$st powers, including zero, covers the
prime field after $g=\gcd(r+1,p-1)$ sumset additions by Cauchy–Davenport.
Delete zero summands, compose the corresponding nonzero dilations, and
remove all lower terms inductively. This is the exact uniform construction
behind (3); the standard ingredients themselves are not new.

**Naor–Reingold-type auxiliary kernel.** Independent uniform affine
maps $A_0,A_1$ and uniform degree-at-most-$d$ polynomials $R,S$ give
$K$ from $A_1V_ST_RA_0$. For prescribed source and target, the good
initial $y$-frame and final inverse $x$-frame each have probability
at least $1-\binom m2/(p+1)$. At distinct nodes, evaluation of a uniform
polynomial is uniform on $\mathbb F_p^m$ since $m\leq d+1$.
The prescribed transition therefore has conditional probability
$p^{-2m}$, giving $K(z,w)\geq1/(2N_{p,m})$ at the stated threshold.
This supplies a real Dirichlet-energy bound even though $K$ need not
be reversible. This architecture and good-event argument are strong
prior material, as detailed next.

**Original-generator transfer.** Each affine letter has energy at most
$2\|f-Ef\|_2^2$. The auxiliary word has length at most
$\ell_d=2B_d+4$. Combining its energy comparison with (5) gives
$$
\delta_d=\bigl[\ell_d^2(4C_d/\gamma_d+8)\bigr]^{-1}.
\tag{6}
$$
The same constants control all the allowed orders. Formula (6) is
positive but not presented as optimal or as a computed numerical gap.

These four blocks form one proof chain, not four independent discoveries.
A natural article must state and explain the strong inputs accurately,
without re-proving deep standard expansion theorems to create length.

## 5. Mandatory prior deductions

The full source-level reports in Section 3 control the attribution and
access limitations. Particularly important deductions are:

- **Naor–Reingold (1999), J. Cryptology 12, 29–66.** Definition 3.5,
  Proposition 3.4 and Lemma 3.5 already use the initial/final projection
  collision event and obtain exact joint mass on its complement.
  Corollary 8.1 allows bounded-wise independent round functions. Root
  directly read these statements and the central proof in the
  [published PDF](https://link.springer.com/content/pdf/10.1007/PL00003817.pdf).
  The prime-field/additive, special-affine and polynomial-interpolation
  version here is an adaptation, not a newly discovered two-round
  mechanism. Its pointwise minorisation is not distinguished by claiming
  the old paper had only a TV theorem: the pointwise calculation is
  already present in the old proof.
- **Kaplan–Naor–Reingold (2009).** Companion graphs connect simultaneous
  tuple action, spectral gap and almost-independent permutations. This
  abstract bridge is not new either. The report distinguishes the
  author-version numbering from the journal metadata.
- **Finite-difference and triangular-automorphism literature.**
  Edo–Lewis and Bardakov–Neshchadim–Sosnovsky explicitly use translation
  commutators and descending degree. Deduct that principle. Monomial
  dilation, Cauchy–Davenport, Lagrange interpolation and elementary
  energy comparisons are standard tools, not separate new theories.
- **Bourgain–Gamburd (2008) and Lindenstrauss–Varjú (2016).** These are
  the strong linear and affine expansion inputs. They do not by themselves
  remove higher-point affine invariants. They must be cited, not relabeled
  as a new affine-gap theorem.
- **Caprace–Kassabov (2023).** Explicit low-degree polynomial permutations
  giving full alternating-group Cayley expanders already exist in other
  dimensions and with other generators. Neither nonlinearity nor explicit
  polynomial syntax is sufficient novelty. A uniformly bounded bridge
  to this exact planar pair would need proof; none was found in the
  bounded search.
- **Cassidy (2024/2025), and reversible-circuit literature.** Large-tuple
  Schreier expansion is known for random permutations or other local
  generators. Their generator quantifiers differ from the specified
  planar Hénon pair; this does not make the abstract tuple problem new.
- **He (2022).** Coefficient-uniform bounded-degree finite-field nonlinear
  mixing is already a substantive topic, although his state space and
  near-linear mixing scale differ. **Becker–Breuillard (August 2026)**
  is an actual new linear-group expansion preprint, not just the old
  announced sequel; its bounded-rank setting and exceptional-prime
  allowance do not directly settle this contract.

The remaining possible novelty is the complete fixed-pair theorem with
all coefficient/prime/order quantifiers and its specific uniformly
bounded realization/comparison. Reviewers should explicitly consider
whether that is a substantial mathematical synthesis or an insufficient
short application of the listed prior results. A search miss is not an
answer to that question.

## 6. Local noncollision and exclusions

Root directly read the current README and the relevant existing
Papers1–29 portfolio baseline. Papers20–28 concern characteristic-zero
Hamiltonian degree growth/Newton selectors, not configuration Markov
operators. Paper29 concerns polynomial cohomology, periodic-scheme
detection and invariant fields, not same-word finite-field mixing.
Papers8–11 concern deterministic torus torsion orbit/clock quotients;
their use of finite sets is not this stochastic spectral theorem.
The proposed result does not repeat those scientific claims.

This is only a local noncollision statement, not external novelty.
No stopped action reconstruction, formal gauge, quantum trace, resonance
discriminant, torus Fourier or matrix-cocycle result is included.
The older three-point area/Jacobi/Weil proof remains a valid independent
route but is not a second main-proof block or an automatic appendix/body
capacity source. The candidate is the one bounded-order theorem above.

## 7. Unchanged selection contract for two fresh blind reviews

Each reviewer must separately decide all four gates on this exact same
whole package:

1. Novelty at least 7.5/10 after all mandatory deductions.
2. Stand-alone scientific value at least 7.5/10.
3. Complete-proof confidence at least 9/10 for the exact scope.
4. Credible natural capacity of 22–30 substantive English body pages.

Capacity geometry is anonymous English single-column `article`, 11pt,
letter paper, one-inch margins and standard spacing. References begin
separately and do not count as body. Do not inflate displays, fonts or
spacing, force artificial breaks, add blank pages, or count logs, source
listings or appended prior proofs as substantive body.

Each reviewer must provide a justified low/central/high natural-body
table by necessary mathematical block, crediting every argument once
and deducting shared foundations. No author page allocation or target
is supplied. The older quotient route, a full exposition of BG/LV,
cryptographic context and open higher-order/nonmonic questions must not
be used to fill a deficit. If the theorem naturally fits a shorter
article, fail this locked capacity gate without misrepresenting its
mathematical correctness or scientific value.

The decision is the conjunction of all four gates in **both** reports.
Scores cannot be averaged or best components selected across reviewers.
The reviewers must not read each other's report, communicate with each
other, or import previous candidates' scores. They receive complete,
identical input and disjoint output ownership. No inherited Paper29
one-time natural-draft exception exists. Any failed gate stops selection
of this unchanged package; no automatic drafting or post-count expansion
is authorized.

The configured reviewer MCP is unavailable. Actual independent secondary
reviews must identify their real execution and may not claim a GPT-5.4
MCP call, human review or cross-model validation that did not occur.
This pure-proof task has no numerical experiment, zero fitting, paid
resources, external write or Route-score stage. A complete candidate
PASS would only open the ordinary local manuscript workflow; it would
not count as a completed paper or physical PDF acceptance.
