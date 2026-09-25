# Raw-card derivation — Global divisor exchange and asymmetric product laws

Candidate: `ANG-20260922-GDR01`.
Result: **MAIN IMAGE ADMISSION FAILS: all-point limits and Borel nonsingularity**.
EQUAL-LAW and SWAP-OFF admit zero clocks; REINDEX-OFF also fails admission.

## 1. Input, role and boundary

After root's separate release, personally reread ONLY original card 1–86,
through its original EOF marker. Its 86-line prefix SHA256 was remeasured:
`29b2759103d3c1024e76c4109d5a8bf2b0a70fe20366d4e8410e57558d593cae`.
No author paper, peer/independent report, scout or other new science was read.
Earlier CP1 here and 369 authorship are shared history, not blind discovery;
the finite-write theorem is NOT used. The card's old112/326/scout exposures
are provenance only; those files were not opened. Retained ARS discipline,
internal shared-history **NOT_CALIBRATED**, not external peer review.
All arguments below are exact; no numerical experiment or external search ran.

## 2. Full source, inverse and exact all-state isotropy test

The predicate chi is symmetric under exchange. Thus R^2=id: an exchanging
pair exchanges back, and a nonexchanging pair stays fixed. R is a permutation
of the discrete alphabet A^2, so its coordinatewise action C is a homeomorphism
of the ENTIRE product, with C^-1=C. The rail shift S is a homeomorphism with
(S^-1 x)^L_i=a_(i+1), (S^-1 x)^R_i=b_(i-1). Therefore F=S C has inverse
C S^-1 on all X: both compositions cancel S^-1 S or C^2 exactly.
No terminal, missing predecessor, finite-support restriction or tail deletion occurs.

Write R=(r_L,r_R). The following local recurrences give an explicit full-state
criterion, including configurations with infinitely many active exchanges.
Start u_i^0=a_i, v_i^0=b_i. For n>=0 set

```text
u_i^(n+1)=r_L(u_(i-1)^n,v_(i-1)^n),
v_i^(n+1)=r_R(u_(i+1)^n,v_(i+1)^n);
u_i^(-n-1)=r_L(u_(i+1)^(-n),v_(i-1)^(-n)),
v_i^(-n-1)=r_R(u_(i+1)^(-n),v_(i-1)^(-n)).
```

Induction identifies these with the two rails of F^k x. For each fixed k they
use only the original interval [i-|k|,i+|k|] at site i. The EXACT criterion is
I_x={k in Z: u_i^k=a_i AND v_i^k=b_i for EVERY i}. It retains both full rails,
not one particle or a finite test window. It is {0} if no positive k passes;
otherwise it is pZ, where p is the least positive passing integer. This follows
from the subgroup law and division with remainder, not a cellular-orbit census.

All incoming arrows are (F^-k x,k,x), k in Z; the entire history through x
is its actual inverse/forward iteration. Composition adds lags and inversion
negates them. Equal endpoints do not delete different lag labels. The source
lag kernel is only k=0 identities; C and S create no separately adjoined arrows.

For a full constant pair (u,v), S changes neither rail. If chi(u,v)=1, F
interchanges the two unequal constant rails and the least source period is 2.
Otherwise it fixes that source and its least period is 1. Thus both prescribed
(2,4)/(4,2) sources have I=2Z; every diagonal constant (u,u) has I=Z.

## 3. Probability, support and exact finite-cylinder ratios

The geometric sums give sum_(n>=2)p(n)=sum_(m>=1)2^-m=1 and
sum_(n>=2)q(n)=2 sum_(m>=1)3^-m=1. Every symbol weight is positive. Thus the
specified product is a full-support Borel probability. With L=2N+1,

```text
0<mu(C_N(x))=product_(i=-N)^N p(a_i)q(b_i) <= (1/3)^L.
```

These countable cylinder partitions have maximal mass tending to zero, so
there are no atoms: a positive atom would lie modulo null sets in one cell
of each partition and have mass at most (1/3)^L for every N.
S preserves this asymmetric mu: it separately permutes identically distributed
left coordinates and right coordinates. Check on finite cylinders, then extend
to all Borel sets by uniqueness of probability measures. Its inverse also preserves mu.

C sends C_N(x) exactly to the cylinder with R(a_i,b_i) on the same interval;
outside it R remains a bijection. S only shifts the two constraint intervals.
Consequently the FORWARD image/source ratio for k=1, for EVERY N>=0, is

```text
mu(F C_N(x))/mu(C_N(x)) = product_(i=-N)^N rho(a_i,b_i),
rho(a,b)=1 if chi=0; rho(a,b)=p(b)q(a)/(p(a)q(b))=(3/2)^(b-a) if chi=1.
```

The constant (2,4) gives (9/4)^L -> infinity; (4,2) gives (4/9)^L -> 0.
Hence the prescribed positive finite all-point J_1 fails at retained sources.
For diagonal constants the one-step ratio is 1; this does not repair the
universal admission condition. Already k=1 refutes the requirement for ALL k;
no post-failure all-iterate clock construction is justified.

## 4. Actual Borel singularity, separate from the exceptional-point test

Let lambda(a,b)=p(a)q(b). Under C_*mu, site pairs remain independent and
identically distributed with lambda'(a,b)=lambda(R(a,b)), because R is its
own inverse. In particular lambda(2,4)=1/27, while lambda'(2,4)=1/12.
Define the Borel set

```text
B={x: lim_(M->infinity) (1/M) sum_(i=1)^M 1_{(a_i,b_i)=(2,4)}=1/12}.
```

Then mu(B)=0 and (C_*mu)(B)=1. For completeness the needed Bernoulli frequency
law has an elementary proof: variance of the average through M is at most
1/(4M). Chebyshev at M=j^2 gives summable deviation probabilities for each
rational positive tolerance; the union bound on their tails gives convergence
along squares almost surely. Between consecutive squares, monotonicity of
the counts and (j+1)^2/j^2 -> 1 give full-sequence convergence. Apply this
separately at parameters 1/27 and 1/12. The limit event is Borel, being a
countable limit condition on finite-coordinate indicator sums.

Thus C_*mu is singular to mu. For the ACTUAL MAIN pushforward,
F_*mu=S_*C_*mu is concentrated on S B, whereas mu(S B)=mu(B)=0.
Equivalently S B tests the frequency of (a_(i+1),b_(i-1))=(2,4).
This gives mu(F^-1(S B))=1 with mu(S B)=0, so forward nonsingularity fails.
For the distinct FORWARD IMAGE direction, use S-invariance and C^-1=C:

```text
mu(F B)=mu(S C B)=mu(C B)=(C_*mu)(B)=1, whereas mu(B)=0.
```

No every-Borel density mu(F E)=integral_E J dmu can satisfy this identity.
This is not a finite-modulus or sampling argument and does not infer singularity
solely from the constant-source limits. It establishes both relevant directions
for the same frozen map and measure, without symmetrizing that measure.

MAIN therefore has NO admitted c, clock kernel, clock/lag intersection,
extension, H, physical phases or primitive-time ledger. These are NOT DEFINED,
not zero. The source action, incoming, I_x and lag kernel from section 2 remain.

## 5. EQUAL-LAW: its own admitted zero-clock ledger

The own probability mu_eq=product(p times p) has full support and no atoms;
its paired cylinders have maximal mass at most (1/4)^L. Every pair and its
R-image have the SAME weight p(a)p(b). Hence R preserves the one-site law,
C preserves its product, and the rail permutation S preserves it as well.
These cylinder identities extend to every Borel set; F and every integer
iterate preserve mu_eq. Thus every prescribed cylinder ratio is exactly 1,
for all points, N and integer k. The admitted all-point J_k=1 and c_k=0
satisfy every-Borel IMAGE and the cocycle law; no density was borrowed from MAIN.

The actual action/inverse and full-state isotropy criterion are those in
section 2, since this control changes the measure, not the map or full source.
Source isotropy is I_x={0} or pZ; extension isotropy is the ENTIRE I_x and H_x=0.
The full clock kernel is ALL actual arrows; lag kernel and intersection are
identities. All incoming iterates and repeated return labels remain. Over each
actual source orbit, extension classes have phase h and form one real height-
translation orbit with trivial time stabilizer. Different actual orbits are
not merged by spatial shift, finite differences or equal weights. There is
no positive physical packet. The two test pairs have source period 2 and
diagonal constants period 1, but every such return has time zero.

## 6. SWAP-OFF: full two-rail periods, not a one-tape reduction

This owner has map S and inverse S^-1 on full X with its own asymmetric mu.
The independent-rail permutation proof in section 3 gives every-Borel invariance
for this map and all integer powers. Its own prescribed ratios are 1 at every
point, N and k; J_k=1 and c_k=0 are admitted, including both test pairs and diagonals.

For a whole rail define P(a)={k:a_(i+k)=a_i for every i}, and similarly P(b).
The complete source criterion is I_x=P(a) intersection P(b), because
S^k x=(a_(i-k),b_(i+k))_i. Each P is {0} for an aperiodic rail or dZ for its
least positive rail period d. If either rail is aperiodic, I_x={0}; if both
have periods d,e, then I_x=lcm(d,e)Z. ALL constant pairs are fixed, not period 2.
The incoming k-step source is (a_(i+k),b_(i-k))_i; both entire rails remain.
All actual lag labels are retained, including every multiple of a source period.
Extension isotropy equals I_x, H_x=0; clock kernel is the entire actual action,
lag kernel/intersection are identities. Phase is h on each actual simultaneous
opposite-shift orbit, not a quotient by two independently chosen rail shifts.
Each physical orbit is a free real phase line; no positive packet exists.

## 7. REINDEX-OFF: its own failed admission and complete source ledger

The map is C on full X, inverse C, with the same asymmetric product law.
Its forward cylinder ratio is the product of rho from section 3. Since C^2=id,
ALL integer even iterates have ratios 1; ALL odd iterates have that product.
The two prescribed constant sources therefore have odd-iterate limits infinity
and zero; diagonal constants have ratios 1. Independently, the set B in
section 4 gives mu(B)=0, mu(C B)=1 and C_*mu singular to mu. This owner fails
both prescribed all-point admission and the every-Borel/nonsingularity test.

Its complete source isotropy is Z if chi(a_i,b_i)=0 at EVERY site, and 2Z
otherwise: any active site changes an unequal pair, while C^2 fixes all sites.
Thus the test pairs have source period 2 and all diagonal tapes are fixed.
Every incoming iterate is C^-k x=C^k x, retaining the full simultaneous
all-site operation and every lag, even when endpoints repeat. The lag kernel
is the identity arrows; no effective Z/2 quotient is taken. Despite even-
iterate ratios 1, a full c was NOT admitted. Clock kernel/intersection,
extension, H, phases and physical packets remain NOT DEFINED, not zero.

## 8. Scoped decision

Stop/fork MAIN at IMAGE admission; retain its full source ledger unchanged.
Its asymmetric-law failure is neither a finite-write cancellation result nor
a universal obstruction to other measures or global reindexing owners. The
equal-law control is its separately frozen owner, not a post-failure repair.
Admitted controls have zero H by their OWN proofs; failed controls have no H.
Strong naturalness remains OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED and Route B NOT INVOKED. No paper-unlock or new batch is implied.
