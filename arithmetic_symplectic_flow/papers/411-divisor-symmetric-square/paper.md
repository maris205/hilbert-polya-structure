# Symmetric-square transport: owned clocks and continuous composite fixed packets

Candidate ID: `ANG-20260923-DSS01`. Paper411; 2026-09-23.
Batch: `NONLINEAR-LIFT-20260923-M`, round2/5.
Outcome: `OWNED SYMMETRIC IMAGE CLOCK; CONTINUOUS COMPOSITE FIXED PACKETS — STOP / FORK`.

The [frozen card](candidate-card.md), original95 lines, is the sole scientific contract.
This paper proves its inverse/IMAGE and whole-ledger obligations and classifies
all fixed states of MAIN and three separately owned controls, without a q cutoff.
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
AI-assisted author derivation and drafting; shared-history NOT_CALIBRATED.

## Abstract

On all real symmetric two-by-two matrices, current floor-divisibility permits
matrix squaring followed by translation by the current integer quotient.
All actual inverse branches, including scalar targets, admit one consistent
analytic IMAGE density. The full retained-lag groupoid therefore owns its
signed clock and height-translation action. MAIN nevertheless has a scalar
fixed packet of primitive time \(\log64\) and continuous fixed families of
primitive time \(\log(4q)\) for every integer \(q\ge1\). Distinct fixed matrices
are distinct source packets, even after every incoming history is included.
The permission-off control has exactly the same fixed set; quotient-off has
one fixed core with time \(\log8\); square-off has a continuum of zero-clock
fixed cores. These are exact fixed-set statements, not a higher-period census.
The owned clock does not meet the ordinary-prime target; the candidate stops.

## 1. Full source, mechanism and scope

Write \(A=\begin{pmatrix}x&y\\y&z\end{pmatrix}\), \(\delta(A)=xz-y^2\),
\(t(A)=x+z\), \(m=\lfloor x\rfloor\), \(n=\lfloor\delta(A)\rfloor\).
The carrier is \(X=\operatorname{Sym}_2(\mathbb R)\cong\mathbb R^3\),
with its usual Borel structure and \(\mu=dx\,dy\,dz\), not a similarity quotient.
Let
\[
D_0=\{\delta t\ne0\},\quad
D=\{A\in D_0:m\ne0,\ m\mid n\},\quad q=n/m\text{ on }D.
\]

| Owner | Legal source | Actual successor |
| --- | --- | --- |
| MAIN | \(D\) | \(A^2-qI\) |
| G, permission-off | \(D_0\) | \(A^2-q_GI\), with \(q_G=\lfloor n/m\rfloor\) if \(m\ne0\), and \(q_G=0\) if \(m=0\) |
| Q, quotient-off | \(D\) | \(A^2\) |
| S, square-off | \(D\) | \(A-qI\) |

Each row owns its own map, inverse atlas, measure and clock. The floor is signed
mathematical floor; divisibility permits \(m=\pm1,n=0,q=0\).
Every complementary point remains an object and a forward terminal, with its
identity and all actual incoming arrows, not an absorbing fixed point.
No cut, zero entry, singular matrix or trace-zero fibre is removed from \(X\).
Floor cells include their lower face and exclude their upper face.
No undefined quotient is evaluated at \(m=0\).

For integers \(N,d\), \(N\ge2,\ 1<d<N\), the interface
\[
A_{N,d}=\begin{pmatrix}d&1\\1&(N+1)/d\end{pmatrix}
\]
has \(\delta=N,\ t>0,\ (m,n)=(d,N)\). MAIN is legal there exactly when \(d\mid N\).
The interface is not the full source or a selected recurrent subset.
It deforms the [prior prime/composite symbolic lineage](../../docs/prior_work/README.md):
proper-divisor admissibility becomes a current matrix readout that determines
an actual quotient translation, followed by a new readout of the transported matrix.
There are no prime lists, per-prime components, roofs or fitted densities.
This exact interface does not establish strong naturalness or a prime return law.

## 2. Complete inverse atlas, including scalar targets

For MAIN/G, at an arbitrary target \(B\) enumerate every integer \(q\).
Put \(Z=B+qI\). A legal source \(A\) satisfies \(A^2=Z\);
invertible symmetric \(A\) forces \(Z\) to be positive definite.
Also \(A\) commutes with \(B=A^2-qI\).
If \(B\) has distinct eigenvalues \(\beta_+>\beta_-\), its real orthogonal
projectors \(P_\pm\) therefore give exactly the four candidate roots
\[
A_{\epsilon_+,\epsilon_-}
=\epsilon_+\sqrt{\beta_++q}\,P_+
+\epsilon_-\sqrt{\beta_-+q}\,P_-,
\quad\epsilon_\pm\in\{1,-1\},\quad\beta_-+q>0.                 \tag{1}
\]
This follows by restriction to the two one-dimensional eigenspaces.
Their traces cannot vanish: opposite signs would require equal positive
square roots, contrary to \(\beta_+\ne\beta_-\).

If \(B=\beta I\) and \(\beta+q>0\), a symmetric root has eigenvalues in
\(\{\sqrt{\beta+q},-\sqrt{\beta+q}\}\).
Mixed signs give trace zero and are illegal, including their entire continuous
conjugacy family. The only legal candidates are
\(\pm\sqrt{\beta+q}I\). A nonpositive \(\beta+q\) gives no invertible real
symmetric root. Thus the scalar-target rule omits no legal source.

Retain a candidate exactly when its own source domain and its own arithmetic
quotient equal the enumerated q; require the displayed forward equation.
For Q use the same recipe with \(Z=B\), once only, and test \(A\in D\).
For S enumerate all \(q\in\mathbb Z\), \(A=B+qI\), and retain precisely
\(A\in D,\ n(A)/m(A)=q\). These are necessary and sufficient in every case.
No target-forward test is substituted for a source test.
The same candidate source is never counted twice.

For definiteness, take the positive and negative definite square-root branches
on the full positive-definite cone, including scalar targets.
The two mixed-sign branches use its distinct-eigenvalue part.
The projectors in (1) are analytic locally there; definite roots are analytic
also at scalar targets, as follows from the invertible derivative below and
local uniqueness of the definite root. These four choices for each q, with
the actual Borel source checks, constitute a countable Borel inverse atlas.
There is no separate scalar-only chart whose derivative could be chosen arbitrarily.
For S the corresponding analytic extension is simply \(B\mapsto B+qI\).
All targets lacking an accepted inverse still retain their own forward status.

Define \(\mathcal P_O(B)\) to be the complete accepted predecessor set just
specified for owner \(O\), and recursively
\[
\mathcal P_O^0(B)=\{B\},\qquad
\mathcal P_O^{j+1}(B)=\bigcup_{C\in\mathcal P_O^j(B)}\mathcal P_O(C). \tag{2}
\]
This is an exact all-integer, all-depth incoming prescription, not a truncated
search. Induction using the one-step necessity and sufficiency proves that it
contains exactly all sources of legal j-step histories into B. It includes
terminal targets and never supplies a continuation beyond a terminal.

## 3. All-point IMAGE and native volume clock

On a fixed arithmetic branch, the derivative of \(A\mapsto A^2-qI\) is
\(H\mapsto AH+HA\). In an orthogonal eigenbasis of \(A\), with eigenvalues
\(\lambda_1,\lambda_2\), this linear map on symmetric matrices has diagonal
multipliers \(2\lambda_1,\lambda_1+\lambda_2,2\lambda_2\).
Changing that basis conjugates the linear endomorphism, so its determinant
in the frozen \((x,y,z)\) coordinates is \(4\delta(A)t(A)\).
It is nonzero precisely on \(D_0\). The inverse function theorem proves the
local analytic assertions in Section2, including both definite scalar roots.
Consequently, at every actual inverse point, for MAIN/G/Q,
\[
J_\theta(B)=\frac1{4|\delta(\theta B)t(\theta B)|},\qquad
b_O(A)=J_{\theta_A}(T_OA)^{-1}=4|\delta(A)t(A)|.              \tag{3}
\]
For S, independently, \(J_\theta=1,\ b_S=1\).
These are positive finite full-point formulas. At any overlap naming the same
source, (3) agrees; each point has only its own actual arithmetic quotient.
At floor faces it is the derivative of the fixed-branch analytic extension,
not a claim that the globally piecewise map is differentiable across the face.

For each actual inverse chart and every Borel subset E of its actual domain,
\[
\mu(\theta E)=\int_EJ_\theta\,d\mu.                          \tag{4}
\]
Indeed cover the analytic root branch by countably many local diffeomorphism
charts, partition E into disjoint Borel pieces subordinate to that cover,
and apply ordinary change of variables on each piece. The inverse branch is
injective, so the image pieces remain disjoint. The actual source restrictions
are Borel restrictions of these charts; they need not be open. The translation
case is the same argument with derivative identity. Thus (4) includes all
null subsets and cut faces. The analytic prescription, not the measure alone,
specifies values on null sets. No null-point repair has been introduced.

The legal-step clock is \(\kappa_O=\log b_O\). It may have either sign or be zero.
It is neither an added positive roof nor an ordinary physical ODE time.
The arithmetic quotient changes the actual successor and hence later clock
factors, although it does not occur explicitly in the branch determinant.

## 4. Entire retained-lag ledger

The following assertions apply separately to each owner, with its own legal
iterates and \(b_O\). Set
\[
P_j(A)=\prod_{i=0}^{j-1}b_O(T_O^iA),\quad P_0=1,\quad S_j=\log P_j.
\]
The Borel groupoid consists of all actual triples
\[
g=(A,r-s,B),\qquad T_O^rA=T_O^sB,\quad r,s\ge0
\text{ with both histories legal};\qquad c(g)=\log\frac{P_r(A)}{P_s(B)}. \tag{5}
\]
Its range is A and source B; equal triples, not histories with arbitrary
extra labels, are identified. Each forward iterate is deterministic and each
predecessor set is countable, so the source fibres are countable.
The groupoid is the countable union of Borel equal-iterate relations.

Two presentations of one triple differ by adding the same nonnegative number
of steps to both sides of one of them. Their common forward tail contributes
the same product to numerator and denominator in (5), proving descent.
To compose arrows, align their two legal histories at the middle object:
extend the shorter one only along steps already present in the longer history.
This proves closure even near terminals; the matching products cancel.
Thus c is additive, and inverse arrows have the negative clock.
A forward step \((T_OA,-1,A)\) has clock \(-\kappa_O(A)\).

Finite inverse words have the product of their step IMAGE densities.
On an injective local graph of an arrow (5), the map from B to A has density
\(P_s(B)/P_r(A)=e^{-c(g)}\), by (4) and composition. Such graphs cover all
arrows countably. This also proves measure-class compatibility of the
actual groupoid, without replacing it by an independently weighted owner.

The complete kernels, with all equal-iterate restrictions understood, are
\[
\begin{aligned}
\ker\ell&=\{(A,0,B):T_O^rA=T_O^rB\text{ for some legal }r\},\\
\ker c&=\{(A,r-s,B):P_r(A)=P_s(B)\},\\
\ker\ell\cap\ker c&=\{(A,0,B):T_O^rA=T_O^rB,\ P_r(A)=P_r(B)
                         \text{ for some legal }r\}.        \tag{6}
\end{aligned}
\]
In particular the lag kernel is not declared trivial: different predecessors
may merge. For S, \(c=0\) everywhere, so \(\ker c=G_S\) and the intersection
is its full lag kernel. Formulas (2), (5), (6) cover all source points; they do
not assert a classification of higher cycles for MAIN/G/Q.

An object has nontrivial source isotropy exactly when its forward history
eventually reaches a legal periodic core. To see this, a nonzero-lag equality
equates two different iterates and hence repeats the intervening finite segment.
Conversely every eventual period supplies such an equality.
If the least core period is r and its one-cycle sum is C, then
\[
G_A^A=r\mathbb Z,\qquad H_A=c(G_A^A)=C\mathbb Z,\qquad
\operatorname{Iso}_{G^c}(A,h)=\{kr:kC=0\}.                  \tag{7}
\]
Prefix clocks cancel, so every incoming object has the same H.
For a non-eventually-periodic history, including one ending at a terminal,
source and extension isotropy are trivial and H is zero.

In the full extension \((B,h)\mapsto(A,h+c(g))\), all heights are retained.
Height translation acts on the orbit SET. Its stabilizer over a source packet
is exactly H: comparison at the same source object is precisely an isotropy
arrow. The phase fibre is \(\mathbb R/H\).
Explicitly, if \(T_O^a z=F\) is a fixed core with \(C=\kappa_O(F)\),
the arrow \((F,-a,z)\) assigns phase \(h-S_a(z)\pmod{C\mathbb Z}\);
a different legal hitting time changes this by an element of \(C\mathbb Z\).
For any source orbit, choose a base object b and an actual arrow \(g_z:z\to b\).
Its phase coordinate is \(h+c(g_z)\pmod{H_b}\). Two such arrows differ by
a loop at b, so their coordinates differ by an element of \(H_b\).
If C is nonzero, the primitive is \(|C|\), repetitions are \(k|C|\), and
extension isotropy is trivial. If C is zero, source and extension retain
\(r\mathbb Z\), the phase line is free, and there is no positive primitive.
There is no smooth/Hausdorff quotient or positive-suspension claim.

For a fixed core F its complete source packet is exactly
\(\mathcal B_O(F)=\bigcup_{j\ge0}\mathcal P_O^j(F)\).
Different fixed matrices have disjoint packets: their deterministic forward
tails are the different constant matrices and can never meet.
Equation (2) gives every incoming point of these packets, (5) its height
offset, and (7) its entire isotropy/period group. This remains valid when
the collection of distinct fixed cores is continuous.

## 5. Complete fixed sets: MAIN and G

For \(q\ge1\) define the full matrix family
\[
\mathcal F_q=\left\{\begin{pmatrix}x&y\\y&1-x\end{pmatrix}:
 -1\le x<0,\quad y^2=q+x-x^2\right\}.                       \tag{8}
\]
The displayed equation requires a real y; both signs are included, with their
coincidence at zero counted once. For q=1 the x interval is
\([(1-\sqrt5)/2,0)\); for \(q\ge2\) it is \([-1,0)\).
These include every allowed endpoint and a continuum of matrices for each q.

**Theorem.** The complete fixed sets are
\[
\operatorname{Fix}(T)=\operatorname{Fix}(T_G)
=\{2I\}\ \cup\ \bigcup_{q=1}^{\infty}\mathcal F_q.           \tag{9}
\]
At any MAIN/G fixed point, \(A^2-A-qI=0\) for its own integer q.
Real eigenvalues require \(1+4q\ge0\), hence \(q\ge0\).
For q=0, invertibility forces \(A=I\), but both actual quotient rules give
q=1 there; it is not fixed under MAIN/G.

For a nonscalar fixed A, Cayley--Hamilton gives
\((t-1)A=(\delta+q)I\), forcing \(t=1,\delta=-q\).
Thus \(q\ge1,n=-q,z=1-x,y^2=q+x-x^2\).
MAIN self-consistency \(q=n/m\) forces \(m=-1\).
For G, \(m=0\) gives quotient0, \(m>0\) gives a negative quotient,
and \(m=-k<0\) requires \(q=\lfloor q/k\rfloor\), equivalent to k=1.
Both owners therefore give exactly (8). Conversely its actual m,n equal
\(-1,-q\), and Cayley--Hamilton verifies the fixed equation and legality.

For a scalar fixed point \(A=\lambda I\), \(q=\lambda^2-\lambda\ge1\).
Put \(m=\lfloor\lambda\rfloor\). Then \(n=\lfloor\lambda^2\rfloor=q+m\).
MAIN requires \(q(m-1)=m\), or \((q-1)(m-1)=1\).
The integer possibilities are \((q,m)=(2,2)\) and \((0,0)\);
the latter is already excluded. The root with floor2 is \(\lambda=2\).
For G a negative root has \(m<0,n\ge0,q_G\le0\), impossible.
A positive root is greater than1. If m=1, \(q_G=q+1\), impossible.
If \(m\ge2\), \(q=1+\lfloor q/m\rfloor\) implies
\(q\le m/(m-1)\le2\), while \(\lambda\ge m\) implies
\(q\ge m^2-m\ge2\). Therefore \(m=q=\lambda=2\).
This proves (9) for all integers q without a cutoff.

At \(2I\), (3) gives \(b=64\). At every \(F\in\mathcal F_q\),
\(\delta=-q,t=1\), so \(b=4q\). Hence every full packet in (9) has
\[
\begin{array}{c|c|c|c}
\text{fixed core}&H&\text{extension isotropy}&\text{phase}\\ \hline
2I&(\log64)\mathbb Z&\{0\}&\mathbb R/(\log64)\mathbb Z\\
F\in\mathcal F_q&(\log(4q))\mathbb Z&\{0\}&\mathbb R/(\log(4q))\mathbb Z
\end{array}                                               \tag{10}
\]
Source isotropy is \(\mathbb Z\) at every core and all its incoming objects.
The periods in (10) are primitives, not multiples substituted for a smaller
unseen time: (7) computes the entire H at the core, including all actual arrows.
Distinct conjugate matrices in (8) remain distinct packets.

## 6. Complete fixed sets of Q and S

For Q, an invertible symmetric idempotent must have both eigenvalues1,
so \(\operatorname{Fix}(T_Q)=\{I\}\). This point is legal: \(m=n=1\).
Its own density is \(1/8\), so H is \((\log8)\mathbb Z\), source isotropy
is \(\mathbb Z\), extension isotropy is trivial and phase is
\(\mathbb R/(\log8)\mathbb Z\). The complete incoming packet is \(\{I,-I\}\):
the only legal symmetric roots of I are \(\pm I\), both legal for Q,
whereas \(-I\) has no real symmetric square root. Thus no predecessor is lost.

For S, equality \(A-qI=A\) forces q=0, equivalently n=0 on its legal domain.
Since \(\delta\ne0\), this is \(0<\delta<1\). Positive determinant of a real
symmetric invertible two-by-two matrix already implies nonzero trace.
Consequently
\[
\operatorname{Fix}(T_S)=\{A:0<\det A<1,\ \lfloor x\rfloor\ne0\}. \tag{11}
\]
Every point in (11) is retained, not one point per conjugacy class.
Each full incoming packet is given by (2); its source and extension isotropy
are \(\mathbb Z\), H is zero, and its phase is the entire free line.
More generally S has zero clock on every actual arrow, including any
higher-period core: this is a clock statement, not a census of those cores.

## 7. Decision, ownership and limitations

MAIN already violates the necessary ordinary-prime condition at its own
fixed core \(2I\): \(\log64\) cannot equal \(\log p\) for an ordinary prime.
Equation (8) additionally supplies continuous multiplicity of the composite
times \(\log(4q)\), with no similarity quotient or selected centre.
No sign restriction, half-time normalization, return section or altered
measure is introduced. The same-object ledger remains intact.

G has exactly the same fixed set and fixed clocks as MAIN, showing that the
permission test does not distinguish these fixed packets from that control.
Q has its own composite fixed time; S has its own zero-clock ledger.
Neither control's failure is used as a substitute for MAIN's direct failure.
T0 and the precise analytic clock ownership are established here; the T2
target fails in the complete fixed window. Strong naturalness and
PROVES_TOO_MUCH/arbitrary encoding remain OPEN. Higher cycles of MAIN/G/Q are
not classified; their exact conditional ledger is (5)--(7).
All-prime coverage is not established, and cannot rescue the exhibited wrong
primitive. No operator, trace, zeta or formal Route evaluation was performed.
Decision: STOP / FORK, with no authorized local repair or longer census.

## Reproducibility, access and AI assistance

Proof method: exact real spectral algebra, signed-floor identities, local
change of variables and deterministic-history algebra. No scientific code,
numerical cutoff, external source campaign, Git mutation or PDF was used.
The full [claim ledger](claim-ledger.md) and [overview](README.md) bind these claims.
The card was personally read through original95-line EOF before author proof.
Earlier definition comparisons were [336 card](../336-divisibility-lu-reassembly/candidate-card.md)
1--57 and [397 card](../397-geometric-content-square/candidate-card.md)1--52,
neither EOF. Heading searches exposed outcome titles but not bodies.
Entry reads: readme1--42; plan125--239,289--321 and headings;
prior-work44--108,221--257 and headings. The readme exposed preceding results.
Previous336/397/401/406 participation and shared historical context remain
disclosed; no blind discovery, global novelty or nonconjugacy claim is made.
One author-side helper derived only G's complete fixed classification from
the frozen definition; the lead author checked and integrated that argument.
This helper was not an independent reviewer. No reviewer/raw/peer science
was read by the author or used in this derivation.

Data availability: the frozen card and the displayed proofs are the exact inputs
and evidence; there is no hidden dataset. AI agents supplied mathematical
derivation, drafting and author-side checking; the separate internal-review
workflow also uses AI agents. No human or external mathematical verification
is certified. Ethics: no human subjects or personal data. Human CRediT
attestations, funding and conflict-of-interest declarations were not supplied;
none is fabricated. Venue criteria are not supplied; no submission-readiness
claim is made. All AI-assisted internal work is NOT_CALIBRATED.
