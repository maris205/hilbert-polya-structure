# Route-A theorem-progress batch plan: C164--C168

Status: **completed and release-audited**.

Date: 2026-08-25

Source commit: `4342893ce5e2516924181744bfacc01c12e4959d`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round keeps five dynamical systems separate and requires one new
all-parameter theorem per paper.  A finite ledger is only a regression
sentinel.  A proposed continuation of an earlier model is rejected when it
does not clear a genuinely stronger theorem gate; the replacement dynamics
and the reason for the pivot are then recorded explicitly.

## Frozen sequence and required progress

1. **C164 -- induced Fredholm ownership for the recurrent Thue--Morse
   renewal shift.**  Retain the C159 S-gap system and its first-return series

   ```text
   S={s>=0:t_s=1},                 F(z)=sum_(s in S) z^(s+1).
   ```

   On the return-branch Hilbert space choose a fixed subexponential gauge
   `q_s=exp(-sqrt(s+1))`, put `u=(q_s)`, and define

   ```text
   ell_z(f)=sum_(s in S) q_s^(-1) z^(s+1) f_s,
   K_z f=ell_z(f)u,                L_z=[z] direct_sum K_z.
   ```

   Prove for every `|z|<1` that this is a trace-norm holomorphic rank-one
   first-return family, that `Tr(K_z^m)=F(z)^m`, and that

   ```text
   det_F(I-L_z)=(1-z)(1-F(z))=zeta_X(z)^(-1).
   ```

   Separately freeze the uninduced one-step renewal adjacency
   `A delta_n=delta_(n+1)+t_n delta_0`.  Prove that on every weighted
   `l2(N0,w)` on which `A` is bounded, `A` is noncompact and belongs to no
   Schatten class.  Finally prove that the induced owner cannot extend as a
   trace-class meromorphic family through any unit-circle arc.  The paper
   must distinguish the natural first-return transfer family from the
   uninduced time-one adjacency and from a tautological scalar determinant.

2. **C165 -- reversible Margolus block cellular automaton.**  The broad
   proposal for another composite-clock Rule-90 closed law is not used: three
   preceding rounds already occupy that lineage, and the general trace-zero
   count has no uniform elementary reduction.  Pivot to binary configurations
   on a ring of `2m` sites.  Let `A` swap `(0,1),(2,3),...`, let `B` swap the
   staggered pairs `(1,2),(3,4),...,(2m-1,0)`, and take one full clock tick to
   be `T=B*A`.  Prove the site law

   ```text
   even sites: +2,                 odd sites: -2  (mod 2m),
   ```

   the exact conjugacy to a four-letter cyclic rotation of length `m`, and

   ```text
   #Fix(T^n)=4^gcd(m,n),
   P_m(d)=sum_(e|d) mu(d/e)4^e,   C_m(d)=P_m(d)/d  (d|m),
   zeta_T(z)=product_(d|m)(1-z^d)^(-C_m(d)).
   ```

   Prove `Pr(period<m)<=m*4^(-m/2)`, the reflection reversor, the finite
   Koopman determinant `det(I-zU)=zeta_T(z)^(-1)`, and the corresponding
   antiunitary time reversal.  Do not describe the conjugate necklace system
   as chaotic or interacting.

3. **C166 -- high-dimensional dyadic Pascal skew tower.**  The proposed
   two-dimensional affine shear is rejected because its odd-modulus branch
   is conjugate to a product rotation and its even branch is only the
   two-dimensional case below.  For `q=2^r`, `r>=1`, and `d>=2`, define

   ```text
   T(x_1,...,x_d)=(x_1+x_2,...,x_(d-1)+x_d,x_d+1)  mod q.
   ```

   Put `a=floor(log_2 d)` and `M=2^(r+a)`.  Prove from the Pascal iterate
   coefficients and exact 2-adic valuations that

   ```text
   Fix(T^n)=the whole q^d-state space iff M divides n,
   Fix(T^n)=empty otherwise.
   ```

   Hence every point has exact period `M`, there are `q^d/M` primitive
   cycles, and

   ```text
   zeta_T(z)=(1-z^M)^(-q^d/M),
   det(I-zU_T)=(1-z^M)^(q^d/M).
   ```

   In the truncated-polynomial representation
   `p(t)=1+x_d t+...+x_1 t^d`, prove that `T` is multiplication by `1+t` and
   that substitution `t -> -t/(1+t)` is an involutive reversor.  This yields
   a same-clock finite Koopman unitary and antiunitary reversal without any
   Hilbert--Polya claim.

4. **C167 -- rectangular Dirichlet Abel branches under controlled
   deformation.**  For `Q_alpha=(0,1)x(0,alpha)`, `alpha>0`, derive the full
   anisotropic Poisson identity

   ```text
   W_alpha(s)=alpha*s/(2*pi) sum_(m,n in Z)
       (s^2+4(m^2+alpha^2*n^2))^(-3/2)
     -1/4-1/(2(exp(pi*s)-1))-1/(2(exp(pi*s/alpha)-1)).
   ```

   For every nonzero shell `E=m^2+alpha^2*n^2`, prove

   ```text
   lim_(eps->0+) eps^(3/2) W_alpha(eps-2i*sqrt(E))
     =alpha*exp(i*pi/4)*R_alpha(E)/(8*pi*E^(1/4)),
   ```

   including coincident axes and boundary simple poles.  With
   `beta=alpha^2`, classify every non-sign collision by the positive rational
   parameter

   ```text
   beta=(m'^2-m^2)/(n^2-n'^2),
   ```

   prove every pairwise crossing is transverse, prove that irrational `beta` has no
   non-sign collision, and identify rational `beta=u/v` shells with the exact
   fibres `v*m^2+u*n^2=N`.  No general divisor formula for those fibres may
   be asserted without a separate theorem.

5. **C168 -- three-phase Haar law for a natural four-symbol open Walsh
   gate.**  Reject a freely chosen diagonal three-phase tensor model as
   post-hoc.  Instead freeze

   ```text
   A=F_4^* diag(1,0,1,1),
   chi_A(x)=x(x-1)(x^2+i*x/2-1/2).
   ```

   Its nonzero roots are `1` and `lambda_+/-=(+/-sqrt(7)-i)/4`; their
   normalized phase ratio satisfies

   ```text
   r=(-3+i*sqrt(7))/4,            r+r^(-1)=-3/2,
   ```

   and is not torsion.  For the full-cycle tensor `C_k=A^(tensor k)`, prove
   the complete multinomial secular factorization and the phase Fourier law

   ```text
   mu_hat_k(m)=((1+u_+^m+u_-^m)/3)^k.
   ```

   Deduce exponential decay for each fixed nonzero Fourier mode and weak
   convergence to circle Haar measure.  Prove the centered log-modulus CLT
   with variance `(log 2)^2/18` and the joint Gaussian--Haar product limit.
   Retain the hole-zero torsion branch as an exact finite-group control.
   Explicitly do not claim a uniform all-mode spectral gap or total-variation
   convergence to continuous Haar measure.

## Uniform artifact and integrity contract

Each paper must release the same closed package class as C159--C163: source
audit, research question, proof package, experiment and paper plans,
narrative report, two-round internal improvement record, deterministic
producer, producer-independent checker, separate symbolic reconstruction,
canonical byte replay, hostile semantic mutation suite, results/test/hostile
reports, a complete Route-A YAML, a bilingual LaTeX paper, three preserved
content-distinct PDF snapshots, compile report, canonical evidence, and a
self-excluding release manifest.

Every all-parameter conclusion must have a proof independent of its finite
sentinel.  ARS Stage 2.5 and Stage 4.5 each apply the seven failure modes.
Final release requires exact evidence replay, manifest disk closure,
fixed-epoch double PDF builds, embedded fonts, warning-free logs,
rendered-page inspection, and absence of build/cache debris.  Review is
described as internal only; no external reviewer, cross-model independence,
acceptance score, unperformed computation, or interval certificate may be
invented.

## Frozen claim boundary

No paper may read a target zero table or prime table, freeze a target divisor
or counting law, introduce arithmetic local data, claim Euler factors, root
numbers, automorphy, a Hilbert--Polya operator, or combine coordinates across
the five source systems.  Source integers, finite rings, gcds, Moebius
inversion, and exact quadratic-form fibres remain internal source
bookkeeping.  Route-A labels may be weakened by evidence but not promoted
from finite tables.  Every evaluation must retain
`route_b_invocation_allowed=false`.
