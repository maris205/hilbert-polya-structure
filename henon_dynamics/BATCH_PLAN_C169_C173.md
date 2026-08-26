# Route-A theorem-progress batch plan: C169--C173

Status: **completed and release-audited**.

Date: 2026-08-26

Source commit: `ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round follows Route-A evaluator version 0.2.0, frozen specifically to
`flow_systems/skills/route-a-evaluator.md` at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
The authority is recorded explicitly because the Hénon-local evaluator file
remains the older 0.1.0 vocabulary; this batch does not silently treat that
local file as v0.2.  Artifact bases in the five YAML records are repository-
root-relative.  In particular, arithmetic relevance is now the explicit
entry gate `A0`, before
the orbit, determinant, analytic, and natural-lift gates `A1--A4`.  A source
may have a complete orbit theorem and still fail `A0`; that outcome is kept as
useful dynamics research, not promoted to a primary Hilbert--Polya candidate.
The five systems below remain separate.

## Candidate pivots before freezing

Three initial proposals were rejected by the local collision scan.

- A one-parameter hyperbolic toral-automorphism family would have varied the
  trace in the already completed C125 Anosov torus theorem.  It was not
  promoted as a new subtype.
- A classical baker-map paper was too close to the C148/C158/C163/C168 Walsh
  baker and open-scattering lineage.  A change from quantum to classical
  coordinates was not, by itself, a sufficiently new theorem gate.
- A complete-graph nonbacktracking zeta was also screened out before
  freezing.  The repository already contains C15 and C29--C30
  Ihara--Hashimoto constructions and obstructions, while the proposed Bass
  factorization is established finite-graph machinery rather than the new
  source-specific advance required in this round.

The replacements are a parabolic skew shift, a deterministic kinetic ring,
a reversible stochastic chain, a primitive finite-field multiplier, and a
nonlinear integrable birational map.

## Frozen sequence and required progress

1. **C169 -- irrational Furstenberg skew shift.**  For every irrational
   `alpha`, freeze

   ```text
   T_alpha(x,y)=(x+alpha,y+x) mod 1.
   ```

   Prove the all-iterate formula

   ```text
   T_alpha^n(x,y)
     =(x+n*alpha, y+n*x+alpha*n*(n-1)/2) mod 1,
   ```

   so every positive iterate has an empty fixed set and the source
   Artin--Mazur zeta is exactly one.  On the Fourier basis of Haar
   `L2(T^2)`, prove

   ```text
   U e_(m,k)=exp(2*pi*i*m*alpha)e_(m+k,k).
   ```

   The `k=0` component is pure point, whereas every `k!=0` component splits
   into `|k|` bilateral shifts; the continuous part therefore has countably
   infinite Lebesgue multiplicity.  Prove noncompactness, exclusion from all
   finite Schatten classes, and absence of an ordinary Fredholm determinant.
   The involution `R(x,y)=(alpha-x,y)` must reverse the same clock and induce
   an antiunitary time reversal.  The empty orbit zeta is an obstruction, not
   a target match.

2. **C170 -- Kac scatterer ring.**  For `N>=1`, marker word
   `epsilon in {+1,-1}^N`, and `eta=product_j epsilon_j`, freeze

   ```text
   T(j,sigma)=(j+1,epsilon_j*sigma)
   on (Z/NZ) x {+1,-1}.
   ```

   Prove uniformly over all marker words that `eta=+1` gives two exact
   `N`-cycles, whereas `eta=-1` gives one exact `2N`-cycle.  With
   `L=N` in the first case and `L=2N` in the second, derive

   ```text
   #Fix(T^n)=2N if L divides n, and 0 otherwise,
   zeta_T(z)=(1-z^L)^(-2N/L),
   det(I-zU_T)=(1-z^L)^(2N/L).
   ```

   A marker gauge followed by an unfolded orbit coordinate must construct an
   involutive reversor, not merely appeal to finite permutation theory.  The
   resulting Koopman unitary and antiunitary are same-clock finite objects.
   Marker parity completely classifies the dynamics, so the model supplies no
   chaotic or arithmetic complexity beyond this theorem.

3. **C171 -- Ehrenfest hypercube and its Krawtchouk lumping.**  For every
   `d>=1`, let `P_d` flip one uniformly selected coordinate of
   `{+1,-1}^d`.  Prove that every Walsh character `chi_S` is an eigenvector
   with eigenvalue `1-2|S|/d` and hence

   ```text
   Tr(P_d^n)=sum_(j=0)^d binom(d,j)(1-2j/d)^n,
   det(I-zP_d)=product_(j=0)^d
       (1-(1-2j/d)z)^binom(d,j).
   ```

   The diagonal return probability is `2^(-d)Tr(P_d^n)` and vanishes at odd
   times.  Prove that Hamming-weight lumping yields the reversible birth--death
   chain

   ```text
   Q(k,k+1)=(d-k)/d,      Q(k,k-1)=k/d,
   ```

   with binomial invariant law, Krawtchouk eigenvectors, and the same distinct
   eigenvalues with multiplicity one.  For every `d>1` this is a weighted
   Markov trace-log determinant, not a deterministic Artin--Mazur zeta.  At
   `d=1` the operator is the isolated deterministic two-cycle, which supplies
   no uniform all-family primitive layer or arithmetic structure.  Although
   the natural operator is finite and self-adjoint, turning it into a unitary
   time evolution changes the discrete stochastic clock; the natural-lift
   label is therefore kept at a formal hint.

4. **C172 -- primitive finite-field multiplier.**  For every prime power
   `Q>=2`, primitive `a in F_Q^*`, and `N=Q-1`, freeze `T_a(x)=a*x`.
   Prove that zero is fixed and the nonzero field elements form one exact
   `N`-cycle, giving

   ```text
   #Fix(T_a^n)=Q if N divides n, and 1 otherwise,
   zeta_T(z)=1/((1-z)(1-z^N)),
   det(I-zU_T)=(1-z)(1-z^N).
   ```

   Inversion on the nonzero field, extended by `0 -> 0`, is an involutive
   reversor.  Classify the complete Koopman spectrum and prove that the
   permutation unitary is self-adjoint exactly for `Q<=3`.  Prime-power phase
   space size is intrinsic, so `A0` may retain only a weak arithmetic
   relation; a composite cyclic surrogate has the same cycle theorem, and no
   prime-to-orbit, logarithmic clock, or von-Mangoldt weight emerges.

5. **C173 -- Lyness five-cycle obstruction.**  On the positive quadrant
   freeze

   ```text
   F(x,y)=(y,(1+y)/x).
   ```

   Compute all five iterates and prove `F^5=id`.  The only fixed point is
   `(phi,phi)`, where `phi=(1+sqrt(5))/2`, and every other point has exact
   period five.  Consequently `Fix(F^n)` is a singleton when `5` does not
   divide `n` and the whole positive quadrant when `5` divides `n`; the
   classical Artin--Mazur zeta is therefore undefined.  Prove invariance of
   `dx dy/(xy)`, the reversor `R(x,y)=(y,x)`, and, on the corresponding
   sigma-finite `L2` space,

   ```text
   U^5=I,
   P_j=(1/5)sum_(r=0)^4 omega^(-j*r)U^r.
   ```

   Each of the five eigenspaces is infinite-dimensional.  Thus the natural
   same-clock Koopman unitary is noncompact, non-Schatten, non-self-adjoint,
   and has no ordinary Fredholm determinant.  The paper treats the infinite
   fixed sets as a decisive determinant obstruction rather than replacing
   them by a finite sentinel.

## Uniform artifact and integrity contract

Each paper releases one source audit, research question, theorem package,
experiment plan, paper plan, narrative report, two-round internal improvement
record, deterministic producer, producer-independent checker, separate SymPy
reconstruction, canonical byte replay, hostile semantic mutation suite,
results/test/hostile reports, a current A0--A4 Route-A YAML, bilingual LaTeX
source, three content-distinct PDF snapshots, final PDF, compile report,
canonical evidence, and a self-excluding release manifest.

Every all-parameter conclusion is proved independently of its finite
regression sentinel.  ARS Stages 2.5 and 4.5 each run the seven-mode failure
audit.  The registered reference and citation populations are zero: these
source-locked theoretical notes use no external bibliography and make no
literature-priority claim.  Final release requires exact evidence replay,
27/27 manifest closure, fixed-epoch double builds, embedded fonts,
warning-free logs, rendered-page inspection, and no build/cache debris.
Internal review is not described as external or independent peer review.

## Frozen claim boundary

No paper may read or fit a target zero table or prime table, freeze a target
divisor or counting law, introduce arithmetic local data, claim Euler factors,
root numbers, automorphy, a Hilbert--Polya operator, or merge A0--A4
coordinates across source systems.  C172's finite field is a finite source
space, not a local factor in a global product.  Every evaluation retains
`route_b_invocation_allowed=false`.

## Completion ledger

All five packages contain 28 physical files: 27 content-addressed payload
files plus one self-excluded manifest.  The final batch totals are 120,174
checker assertions, 2,768 separate SymPy checks, 168/168 hostile mutation
rejections, 135/135 manifest payload entries, and ten PDF pages.  Exact
per-paper hashes and the two mandatory ARS integrity gates are recorded in
`BATCH_REVIEW_C169_C173.md`.
