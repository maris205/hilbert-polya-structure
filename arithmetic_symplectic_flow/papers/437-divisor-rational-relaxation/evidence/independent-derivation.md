# DRR01 — card-only independent derivation

## 1. Authority, exact input and review boundary

Candidate `ANG-20260923-DRR01`; root separately released raw mathematics after fully reading CP1.
Sole scientific input: `candidate-card.md`, all 96 lines through actual EOF, SHA256 `7be673a1470edcf1351835bb53fa300874fce70f922393e4560593befaea60da`.
The entire card was reread after release. Frozen `scope-review.md`: 60 lines, SHA256 `f770fc3d08b504f558d1f4556d015af2fad600f077943a8716e3f41c3a323b43`.
No 437 author paper, README, claim ledger, outcome, helper result, peer answer, 429 theorem or sibling proof was read.
Previously read stream/ARS instructions and shared history remain retained. This is inherited-model internal review, `NOT_CALIBRATED`, not blind or human/external peer review.
Only this raw evidence file is written. The arguments are exact algebra, ordinary change of variables and actual-history proofs; no scientific numerical code, external source, Git, auxiliary agent or higher-cycle census is used.

## 2. Full laws, inverse identities and all actual domains

Write `d(u,v)=max(1,gcd(abs(floor u),abs(floor v)))`, with `gcd(0,0)=0`.
Every point of R3 is legal. Signed axes, floor faces, unbounded coordinates and all w values remain; w is a source coordinate, not physical height.
For fixed integer d, the MAIN/D real sweeps can be written
`U=d+(u-d)/(1+v^2)`, `V=d+(v-d)/(1+U^2)`, `W=w+d(u^2-v^2)`.
Their complete inverse on all R3 is
`v=(1+U^2)V-d U^2`, `u=(1+v^2)U-d v^2`, `w=W-d(u^2-v^2)`.
Both directions follow by solving the second sweep for v, then the first for u, then the drift for w. The inverse uses updated target U but the reconstructed ORIGINAL u,v in the drift.
Thus each fixed-d map is a global smooth R3 diffeomorphism, independently of the assembled floor/content readout.
For MAIN enumerate EVERY integer `d>=1`; its exact inverse domain is the Borel set where these reconstructed u,v satisfy `d(u,v)=d`.
The displayed forward equality then holds identically. Conversely an actual source supplies its original d and is recovered by precisely this branch, so the atlas is exhaustive.
D instead has the sole d=1 branch on all R3, without a gcd check or any duplicated arithmetic label.

For fixed d, the N inverse is `v=V-d U^2`, `u=U-d v^2`, `w=W-d(u^2-v^2)`.
Solving its two polynomial sweeps in reverse verifies both inverse identities and a global smooth fixed-d diffeomorphism.
N's actual domain for that branch is its own reconstructed-content equality `d(u,v)=d`; all d are enumerated without cutoff.
Every such domain is Borel, since floor/content is Borel and the reconstructed coordinates are polynomial in the target.
An actual source has a unique original readout, so equal points are not multiplied by labels. Different branch target domains may overlap with genuinely different predecessors.
Failure of an inverse branch means only that it supplies no predecessor; it introduces no terminal into any of the three total source maps.
MAIN/N are not presumed globally injective or smoothly assembled. Their full atlases are countable, with no inverse-index or depth bound.

## 3. Full three-dimensional IMAGE, including w mixing

Fix d and put `a=1/(1+v^2)`, `b=2v(d-u)/(1+v^2)^2`, `c=1/(1+U^2)`, `e=2U(d-v)/(1+U^2)^2`.
The complete MAIN/D derivative in the original three entries is

```text
      a           b         0
     ea         c+eb        0
     2du        -2dv        1
```

The mixed drift entries are retained. Expansion along its last column gives determinant `ac=1/[(1+v^2)(1+U^2)]`.
This derives the full R3 determinant; it is not a two-dimensional reference-measure substitution.
For N the complete fixed-d derivative is

```text
       1             2dv             0
      2dU        1+4d^2 Uv           0
      2du            -2dv            1
```

Its full determinant is exactly 1, including the same original-coordinate drift mixing.
Therefore, on a target's actual inverse branch with reconstructed old v,
`J_MAIN=(1+v^2)(1+U^2)`, `J_D=(1+v_1^2)(1+U^2)` for its sole d=1 reconstruction, and `J_N=1`.
The v in these formulas is NOT the target V. All J are positive and finite at EVERY actual point, including integer faces and null sets.
The fixed-d smooth germ, not the discontinuous content selector, is differentiated. Its global inverse formula makes local chart agreement immediate.
Ordinary change of variables on that R3 diffeomorphism, restricted to any Borel E in its actual inverse domain, proves `mu(theta_d E)=integral_E J_d dmu`.
This includes infinite measure and null boundaries. The countable domain atlas covers every legal source; no atomic integer factor or changed density enters Lebesgue R3.
For any Borel source set E, let `N_E(y)` count all actual immediate predecessors of y in E. Then
`mu(T(E))=integral 1_{N_E>0} dmu`, while `integral_E exp(kappa) dmu=integral N_E dmu` by countable branch addition.
The target union is not silently assigned one Jacobian, and the all-point derivative prescription is not replaced by an arbitrary a.e. version.

The actual signed clocks are
`kappa_MAIN=kappa_D=-log[(1+v^2)(1+U^2)]`, using their OWN first sweep, and `kappa_N=0`.
For MAIN/D the clock is nonpositive and equals zero EXACTLY on `Z0={(0,0,w):w in R}`: equality requires v=0 and U=0, hence u=0.
All other legal steps have strictly negative signed clock. Positive physical primitive time will be the absolute whole isotropy generator, not this sign or an imposed positive roof.

## 4. Full histories, kernels, source isotropy and phases

For each owner define `R_r(z)=product_{j<r} exp(kappa(T^j z))`, `S_r=log R_r`, `R_0=1` and `S_0=0`.
All forward iterates exist. Use precisely `G={(z,r-s,y):T^r z=T^s y}`, identifying equal actual triples and retaining lag, with source y and range z.
Two presentations of the same lag differ by a common increment; their equal meeting future adds the same clock sum, proving descent of `c=S_r(z)-S_s(y)`.
Aligning the two middle histories proves composition and cocycle additivity; inversion changes the sign. In particular `(Tz,-1,z)` has clock `-kappa(z)`.
The Borel equality loci and countable inverse atlas give countable source/range fibers and source orbits. No formal inverse word is made into an arrow without its actual meeting.
Inverse histories have IMAGE factor `1/R_r`; a history bisection from y to z has IMAGE factor `R_s(y)/R_r(z)=exp(-c)`.
The COMPLETE kernels, always restricted to actual meeting triples, are
`ker c`: `R_r(z)=R_s(y)`;
`ker lag`: `(z,0,y)` with `T^r z=T^r y` for some r;
`ker c intersect ker lag`: those equal-depth meetings with `R_r(z)=R_r(y)`.
For N the clock kernel is all G and its joint kernel is its lag kernel. Clock equality alone never supplies a missing arrow.

Nonzero source isotropy is equivalent to eventual full-state periodicity. If the least eventual period is q and the signed whole cycle sum is lambda, the lag group is `q Z`, `c(jq)=j lambda`, and the ENTIRE image is `H_z=lambda Z`.
This follows from actual repeated-state equalities and cancellation of transient prefixes, not from a chosen loop. At non-eventually-periodic states source isotropy and H are trivial.
In the extension `(y,h)->(z,h+c)`, isotropy is the source-isotropy c-kernel. For `lambda!=0` it is trivial, and physical primitive is `abs(lambda)` with repetitions `m abs(lambda)`, positive integer m.
For `lambda=0` the full source isotropy remains ineffective extension isotropy, while physical height translation has no positive return.
For MAIN/D, a zero-clock cycle must have every point in Z0 because each step clock is nonpositive and is strictly negative off Z0. Z0 consists of fixed points, as directly checked below.
Every off-Z0 cycle therefore has a nonzero negative signed sum and a positive physical generator. This conditional statement neither enumerates nor assumes further higher cycles.

Let `Pred_0(p)={p}` and `Pred_{r+1}(p)` be the union of ALL actual own inverse branches over `Pred_r(p)`.
The full source orbit is `union_{s>=0} union_{r>=0} Pred_r(T^s p)`; for a periodic core it is `union_r Pred_r(p)`.
Every reconstructed readout is checked at every node. This is an exact full-depth description, not a selected backward path or finite inverse table.
If `T^a y=T^b p` on a reference periodic core, its full phase is `h+S_b(p)-S_a(y) mod H_p`; choices of witnesses differ exactly by H_p.
For a fixed core this reduces to `h-S_a(y) mod kappa(p) Z` when `T^a y=p`. Zero H keeps a real phase, not an invented zero-period primitive.
All real heights and source coordinates remain; the orbit space is only the declared set-level quotient.

## 5. Entire fixed sets and complete fixed-core incoming

For MAIN/D, fixedness `U=u,V=v` gives `v^2(d-u)=0` and `u^2(d-v)=0`, before any scalar or diagonal restriction.
If either coordinate vanishes these equations force both to vanish; otherwise they force `u=v=d`. In both resulting cases the drift `d(u^2-v^2)` vanishes, so every w remains fixed.
For MAIN, actual readout at `(0,0)` is 1; at `(p,p)` for ANY integer `p>=1` it is exactly p, including the integer lower faces.
Thus the COMPLETE sets are
`Fix(MAIN)=Z0 union { (p,p,w):p in Z>=1,w in R }`;
`Fix(D)=Z0 union { (1,1,w):w in R }`.
For N, `U=u` forces `d v^2=0`, hence v=0; `V=v` then forces `d U^2=0`, hence u=0. Consequently `Fix(N)=Z0`.
All signed, noninteger and unbounded alternatives were included in these full equations and excluded by the equations, not by a source cut.

At any target `(0,0,W)`, every MAIN/N formal d inverse has u=v=0 and w=W; the reconstructed readout is 1, so only d=1 is actual. D's sole inverse also gives the same point.
Each Z0 fixed core therefore has exactly itself as immediate predecessor and as full incoming class, for EACH owner.
For a MAIN target `(p,p,W)`, `p>=1`, let e be ANY proposed positive integer inverse content and put `j=p-e`.
The reconstructed values are the integers `v=p+p^2 j` and `u=p+j v^2`.
Their signed-floor content is `gcd(abs(u),abs(v))=gcd(p,abs(v))=p`, because v is a multiple of p; this also covers v=0 and negative reconstructions.
Therefore only `e=p` passes the actual guard, and it reconstructs u=v=p and w=W. This proves exhaustion over ALL inverse indices without a cutoff.
Every MAIN nonzero fixed core has a singleton full incoming class. D is its own global d=1 diffeomorphism, so each of its fixed cores also has only itself as predecessor.
In particular no state outside Z0 can enter Z0 under any owner; no hidden transient basin can enlarge any of the listed fixed-core clock groups.

At `f_p(w)=(p,p,w)` the MAIN signed step clock is `lambda_p=-2 log(1+p^2)`.
Its source isotropy is Z, ENTIRE H is `2 log(1+p^2) Z`, extension isotropy is trivial, and the positive primitive is `L_p=2 log(1+p^2)`.
Every real phase `h mod L_p` remains, with repetitions `m L_p`. D has the same own result at p=1, namely signed clock `-log4` and physical primitive `log4`.
At every Z0 core, all three owners retain source AND extension isotropy Z, entire H={0} and every free real height phase h.
Different listed fixed cores are different full source packets, since they have singleton incoming and distinct constant futures. Equal period or phase never identifies different w values.
The MAIN fixed sector has exactly continuum many packets at each distinct `L_p`, and no other fixed-sector positive times. D's fixed sector has continuum many at `log4`; N's has none.
These are fixed-sector counts, not a census of unexamined MAIN/D higher cycles.

For N, its independent global identity `U-u=d v^2>=0`, `V-v=d U^2>=0` shows that any periodic trajectory must have both increments zero at every step, hence must lie in Z0.
Together with the unique predecessor of each Z0 point, this excludes any other eventual source periodicity for N without enumerating periods.
Thus N's source/extension isotropy is Z on Z0 and trivial elsewhere; its entire H is globally zero already from its own IMAGE clock.
For D, global invertibility makes its lag kernel exactly units. Any nonzero-lag segment off Z0 has a strictly signed clock, so its clock kernel is units together with the full Z isotropy on Z0; its joint kernel is units.
MAIN retains the full actual-history/product kernel description above, without importing D's injectivity.

## 6. Global actual source-translation and packet theorem

For EVERY real t set `alpha_t(u,v,w)=(u,v,w+t)`. It is a free, Lebesgue-measure-preserving R-action on the complete source.
The original content, every floor face and every actual inverse-domain check depend only on u,v. Each frozen formula adds a u,v-dependent drift to w and has a base independent of w.
Hence, separately for MAIN/D/N, `T alpha_t=alpha_t T`, `theta_d alpha_t=alpha_t theta_d` on each actual inverse domain, and `kappa(alpha_t z)=kappa(z)` at EVERY point.
The last equality uses the full R3 determinant already derived, not an assumed base-clock transfer. All branch domains, original measure and prescribed germ versions are preserved.
Every actual arrow `(z,ell,y)` is therefore carried to `(alpha_t z,ell,alpha_t y)`, and conversely by alpha_-t. This is a groupoid automorphism preserving lag, c and all kernels.
The lift `(z,h)->(alpha_t z,h)` is consequently a well-defined action on the actual clock extension and its orbit set, commuting with physical height translation.
It is SOURCE translation, not physical time; h is not changed, and no w section or quotient is imposed.

Now let p lie on any ACTUAL finite full-state cycle C of least period q. Translation preserves that least period and the signed whole clock sum lambda, hence preserves the ENTIRE `H=lambda Z`.
Suppose alpha_t p and alpha_s p were in the SAME full source packet. An actual meeting would give `alpha_(t-s) T^a p=T^b p` for some nonnegative a,b.
Commutation and the fact that successive iterates of either cycle point exhaust C imply `alpha_(t-s) C=C`.
But C is finite: summing its q w-coordinates before and after this permutation gives `q(t-s)=0`. Thus t=s.
This proves pairwise distinction of FULL source packets, not just of points. Incoming trees cannot identify the packets, because their intersection would also give source equivalence of their cores.
Indeed full inverse recursion commutes with alpha_t, so each whole translated incoming class, its clocks and phases is the exact translated copy of the original class.
For `lambda!=0`, equivalently a positive physical generator `abs(lambda)`, EVERY real translate supplies a distinct full physical packet with the SAME entire H, primitive and repetition law.
This gives continuum multiplicity at that length, without a sample, representative choice or claim that arbitrary nonperiodic translates must always be inequivalent.
For lambda=0 it instead gives distinct zero-clock source packets and does NOT assert any positive physical primitive.
The proof uses only the actual deterministic histories, finite full-state cycle and free source translation. No global C1 diffeomorphism theorem, 429 result or global injectivity of MAIN/N was used.

## 7. Arithmetic gate, controls and stop boundary

On a source integer cell with `1<m<n`, the proper-divisor statement `m|n` is exactly `gcd(n,m)=m`, hence exactly the frozen content equality d=m.
That same original content is used in both updated sweeps and the original-coordinate drift, and the resulting geometry is reread next step; this is the specified lineage interface, not a prime oracle.
The conditional translation theorem is distinct from core existence. Existence is separately established above by every MAIN `f_p(w)` and every D `f_1(w)`.
Already MAIN p=1 has positive primitive `log4`, not the logarithm of an ordinary prime. More generally every `L_p=log((1+p^2)^2)` is a composite-square time.
Its source period is one and its ENTIRE H is `L_p Z`; dividing by 2, rescaling the clock, deleting the null fixed set or choosing w=0 would change the frozen ledger.
Thus MAIN decisively fails by its OWN actual fixed core: `OWNED RATIONAL IMAGE CLOCK; COMPOSITE FIXED PRIMITIVES AND TRANSLATED PACKET MULTIPLICITY — STOP / FORK`.
The global theorem adds a separate obstruction: any actual prime-time positive core would have continuum translated packets at that same prime time, violating uniqueness. No such higher prime core is claimed to exist.
D independently has the `log4` fixed-core failure. N independently has an empty global positive ledger because its entire clock is zero; neither control is used to manufacture MAIN's verdict.
All source states, signed clocks, full three-dimensional measure, actual inverses, entire H, incoming, phases and repetitions remain on their own frozen owner.
Strong naturalness, novelty and unrequested MAIN/D higher-cycle classifications remain unestablished. Arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE; formal Route UNASSIGNED; B NOT INVOKED.
No extra return census, clock/density repair, new candidate or 440 work is undertaken. ARS supplies scope/provenance discipline, not external mathematical certification.
Freeze after full self-read and measured receipt, then HOLD for root's full raw read and a separate PAPER UNLOCK; no author or peer surface has informed this derivation.

EOF — card-only raw; decisive MAIN fixed-core failure and a direct actual-history translation-packet theorem.
