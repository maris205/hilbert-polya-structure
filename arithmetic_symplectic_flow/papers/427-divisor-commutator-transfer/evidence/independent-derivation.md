# DCT01 — card-only independent derivation

## 1. Authority, exact input and access boundary

Candidate `ANG-20260923-DCT01`; root separately released raw mathematics after fully reading CP1.
Sole scientific input: `candidate-card.md`, all 95 lines through actual EOF, SHA256 `04cc5ca8f9e03a1409a83855cfc682132db5704c0d7fc2be19d438dbfaf8657f`.
The entire card was read at CP1 and reread after raw release. Frozen `scope-review.md`: 61 lines, SHA256 `78304b2d9d35e91e3570bf7de2e8bf5f8cd84ea42427ac4c7a592223afb155e9`.
No 427 author paper, README, claim ledger, outcome, peer answer, sibling proof or helper output was read. Earlier shared history and fully read stream/ARS instructions remain retained, not treated as blindness.
This is inherited-model internal review, `NOT_CALIBRATED`, not external or human peer review. Methods below are exact real/complex algebra and change of variables, without scientific code, numerics, external sources, Git or delegation.
Only this evidence file is written. Card and scope are unchanged. After freezing, further scientific access waits for root's full raw read and a separate PAPER UNLOCK.

## 2. Full operators, regularity and the lineage interface

All three owners keep `X=N0 x M2(R) x M2(R)` and counting times flat eight-entry Lebesgue measure.
For legal phase/divisibility data `n=dq`, use the uniform notation
`L_B=alpha Id+beta ad_B`, `ad_B(A)=BA-AB`, with `(alpha,beta)=(d,q)` for MAIN, `(d,0)` for C and `(1,q)` for S.
The matrix part on a fixed-index branch is `Phi(A,B)=(B,L_B(A)+I2)`; every owner still rereads its own actual output.
Put `Delta(B)=(tr B)^2-4 det B`. If `B=[[u,v],[w,t]]`, the four-entry matrix of `ad_B`, ordered by `(A11,A12,A21,A22)`, is

```text
  0     -w       v       0
 -v      u-t     0       v
  w      0       t-u    -w
  0      w      -v       0
```

Expansion gives `det(lambda Id-ad_B)=lambda^2(lambda^2-Delta(B))`, where `Delta=(u-t)^2+4vw`.
This is a polynomial identity in the entries, valid for every real B, not a diagonalizability assumption or an eigenbasis prescription.
Consequently
`det_R4 L_B=alpha^2(alpha^2-beta^2 Delta(B))`.
There is also a basis-free rational inverse. Set `T=ad_B`; Cayley–Hamilton applied to `K=B-(tr B)I2/2` gives `K^2=Delta I2/4`, hence `T^3=Delta T`.
Multiplication then verifies
`L_B^-1 = alpha^-1 Id - beta/(alpha^2-beta^2 Delta) T + beta^2/[alpha(alpha^2-beta^2 Delta)] T^2`.
This formula holds precisely on the stated invertibility locus, since `alpha>0`; for C it reduces to `d^-1 Id`.
Repeated eigenvalues and non-diagonalizable B are included. At `Delta=0`, for example, the determinant is `alpha^4`, with no extra exclusion.
MAIN excludes exactly `Delta(B)=d^2/q^2`; S excludes exactly `Delta(B)=1/q^2`; C has no operator-singularity restriction.
These are the owners' frozen permissions, not newly manufactured terminals. A or B individually may be singular; the separate source condition is `g=det_C(A+iB)!=0`.

For the stipulated interface family `A=diag(cos phi,1)`, `B=diag(sin phi,0)`, one has `g=e^(i phi)`.
Thus `0<=phi<2 pi` realizes every phase, and for register n the complete digit-j sector is exactly `[2 pi(j-1)/n,2 pi j/n)`.
Divisibility permission is exactly `j|n`. On this family `Delta(B)=sin^2 phi`, so MAIN additionally tests `d^2-q^2 sin^2 phi!=0`, while S tests `1-q^2 sin^2 phi!=0`.
For a permitted digit these extra equations exclude only their actual finite sets of angles, not an entire nonempty sector; the endpoints keep their frozen assignments.
This proves the proposed phase/divisor interface while distinguishing operator permission. It is an interface witness only; no commuting or scalar restriction is placed on the full source or fixed calculation.
The commutator, phase, kick, dimensions and measure remain declared designs. This interface proves neither naturalness nor prime generation.

## 3. Complete inverse domains and all-point eight-dimensional IMAGE

At target `(m,C0,D0)`, enumerate every positive pair `d+q=m`, set old register `n=dq`, and use that owner's `(alpha,beta)`.
If `L_C0` is invertible, set `B=C0` and `A=L_C0^-1(D0-I2)`; for C this is `(D0-I2)/d` without MAIN's exclusion.
The exact actual domain further requires
`g_source=det_C(A+iC0)!=0` and `Arg(g_source)/(2 pi) in[(d-1)/(dq),1/q)`.
The original digit is then exactly d, divisibility holds, and substitution gives `Phi(A,C0)=(C0,D0)` and target register m.
Conversely every actual predecessor has some positive `d,q` with `d+q=m`, its first output fixes B, and invertibility forces precisely this A.
This proves both inverse identities and completeness, including every target that cannot itself move forward.
There are no inverse pairs at registers zero or one. No condition on the TARGET complex determinant or target next-step operator is imposed.
Each actual source determines its own n, phase digit d and q, so duplicate candidate descriptions never create duplicate actual arrows.
All these domains are Borel: reconstructed matrices are rational on an open operator locus, and the nonzero-determinant phase sector is Borel with its assigned cuts.

For fixed indices, `Phi` is a smooth diffeomorphism from `{(A,B):det L_B!=0}` onto `{(C0,D0):det L_C0!=0}`, with the displayed rational inverse.
It therefore supplies a unique smooth inverse germ even where the readout changes digit or crosses its principal-Arg cut.
In original eight-entry coordinates the forward derivative is
`D Phi = [[0,Id_4],[L_B,K_A]]`, with `K_A(delta B)=beta[delta B,A]`.
Exchanging the two four-dimensional column blocks has sign `(-1)^16=+1`, so `det_R8 D Phi=det_R4 L_B` regardless of the mixed block.
The actual forward absolute factors and source-selected inverse factors are consequently

| Owner | `rho(n,A,B)=abs det_R8 D Phi` | `J(target)` at this actual inverse |
| --- | --- | --- |
| MAIN | `d^2 abs(d^2-q^2 Delta(B))` | `1/[d^2 abs(d^2-q^2 Delta(C0))]` |
| C | `d^4` | `d^-4` |
| S | `abs(1-q^2 Delta(B))` | `1/abs(1-q^2 Delta(C0))` |

These are positive and finite at EVERY legal inverse point by exactly the frozen owner permissions, with counting-register factor one.
The absolute value retains orientation-reversing branches. A phase cut, null subset or repeated eigenvalue causes no derivative ambiguity: the rational fixed-index germ is used, not the jumping selector.
Local coordinate refinements of the same actual germ agree. The index collection is countable and its sector restrictions can be disjointified without changing assigned points.
Ordinary change of variables for the full open diffeomorphism, restricted to any Borel subset E of its actual inverse domain, gives
`mu(theta E)=integral_E J dmu`, including infinite measure and all null boundaries.
Thus the version is canonically prescribed by the germ everywhere, not filled in arbitrarily on a measure-zero fixed set.
The legal step clock is `kappa=log rho`; terminals have no next-step clock, not an invented zero step.
For reference, the exact legal zero loci are MAIN `Delta=(d^2-d^-2)/q^2` or `(d^2+d^-2)/q^2`, C `d=1`, and S `Delta=0` or `2/q^2`.
These are intersected with each owner's actual phase/divisibility domain; zero sums around an unexamined cycle are not classified by one-step zeros.
For any Borel set E in the legal source domain, let `N_E(y)` count all its actual immediate predecessors of y.
The branch atlas proves `F(E)` Borel and `mu(F(E))=integral 1_{N_E>0} dmu`, whereas `integral_E rho dmu=integral N_E dmu`.
This distinguishes union IMAGE from multiplicity-weighted IMAGE, without giving overlapping inverse branches a single target-only density.

## 4. Full histories, kernels, entire H and phases

For each owner separately define `R_a(z)=product_{j=0}^{a-1} rho(F^j z)`, `S_a=log R_a`, and `R_0=1`, using only legal histories.
The actual groupoid is precisely `G={(z,a-b,w):F^a z=F^b w}` with equal triples identified, source w and range z.
Two witnesses of the same lag differ by a common increment. Their common meeting-point future adds the same clock sum to both sides, proving descent of `c=S_a(z)-S_b(w)`.
To compose, extend the shorter middle history to the longer available one; the existing legal middle tail suffices, even when a meeting endpoint is terminal. Its sums cancel, proving cocycle additivity.
The inverse arrow reverses c. The forward arrow `(Fz,-1,z)` has clock `-kappa(z)`, not `+kappa(z)`.
Inverse histories have IMAGE density `1/R_a`; a branch-pair arrow from w to z has density `R_b(w)/R_a(z)=exp(-c)`.
The equality loci are Borel, and the finite inverse list at each fixed target gives countable source fibers and source orbits over all depths.
The complete kernels, always on actual meeting triples, are
`ker c`: `R_a(z)=R_b(w)`;
`ker lag`: `(z,0,w)` with `F^a z=F^a w` for some legal a;
`ker c intersect ker lag`: those equal-depth meetings with `R_a(z)=R_a(w)`.
Neither equal products alone nor an integer label alone creates an arrow.

Nontrivial source isotropy is equivalent to eventual full-state periodicity. If the least eventual source period is k and one whole cycle has signed sum `lambda=sum_cycle kappa`, then
`G_z^z` has lag group `k Z`, its clock sends `jk` to `j lambda`, and its ENTIRE image is `H_z=lambda Z`.
This follows from repeated-state equalities and cancellation of every transient prefix. At other points source isotropy and H are trivial.
This is a complete conditional characterization on the whole source, not an assertion that any additional higher cycle exists.
The extension uses all `X x R` and `(w,h)->(z,h+c)`. Its isotropy is the c-kernel of source isotropy.
If `lambda!=0`, extension isotropy is trivial and the physical least positive return is `abs(lambda)`, with repetitions `r abs(lambda)`, `r>=1`.
If `lambda=0`, all `k Z` source isotropy remains ineffective extension isotropy, and physical height translation has no positive return. There is no division by k.

Let `Pred_0(x)={x}` and define `Pred_{a+1}(x)` to be the union of all actual own inverses of every point of `Pred_a(x)`.
Then `[x]_G=union_{b: F^b x defined} union_{a>=0} Pred_a(F^b x)` is the exact full incoming/source orbit, without depth truncation.
All terminal trees are retained. Their source isotropy and H are trivial, even when their incoming is nonempty or infinite; register-zero terminals have no incoming.
For an actual arrow g from w to a reference core f, its full phase is `h+c(g) mod H_f`.
In particular, if `F^a w=f` is fixed, it is `h-S_a(w) mod kappa(f) Z`; if `F^a w=F^j f0` on a cycle, it is `h+S_j(f0)-S_a(w) mod H_f0`.
These formulas keep every real height and every ineffective stabilizer. They assume no nice coarse quotient, positive roof or classical smooth flow.

## 5. Complete full-source fixed classification

A fixed state is a legal point fixed by the partial map, not a terminal's identity arrow.
For EACH owner, fixed register requires `dq=d+q`, hence `(d-1)(q-1)=1`; since d and q are positive integers, exactly `d=q=2,n=4` is possible.
The first matrix equality then forces `A=B`. This is deduced from the full equations, not imposed as a commuting section; therefore `[B,A]=0` at every possible fixed state.
For MAIN and C the second matrix equality is `A=2A+I2`, giving the unique possible pair `A=B=-I2`.
At this pair `g=det_C(-(1+i)I2)=2i`, so its phase is `1/4`, and at n=4 its actual digit is `1+floor(1)=2`.
This lower sector endpoint is included. MAIN has `L=2 Id_4`, which is invertible; C has its own always-invertible scalar operator. Thus both candidates really are legal fixed states.
Consequently `Fix(MAIN)=Fix(C)={f}`, with `f=(4,-I2,-I2)` understood as a separate core of each owner.
For S the second fixed equality would instead be `A=A+I2`, impossible. Therefore `Fix(S)=empty` on the entire source.
The argument covers every register and every pair of real matrices, including singular, non-diagonalizable and noncommuting input possibilities before they are excluded by the fixed equations.

## 6. Exact full fixed basin, H, kernels and packet convention

For MAIN and C define
`z1=(1,-3I2,-2I2)`, `z2=(2,-2I2,-2I2)`, `z3=(3,-2I2,-I2)`, `z4=f=(4,-I2,-I2)`.
Both OWN laws give `z1 -> z2 -> z3 -> z4 -> z4`.
To prove this is the COMPLETE incoming class, at target z4 the only index pairs are `(1,3),(2,2),(3,1)`.
Every inverse has old `B=-I2`, so its commutator operator vanishes and BOTH owners force `A=-2I2/d`; nonscalar predecessors are impossible.
The source complex determinant is `(-2/d-i)^2`, with normalized phase `arctan(d/2)/pi` in `(0,1/2)`.
The pair `(1,3)` passes: `arctan(1/2)<pi/4`, so the source n=3 digit is 1; it yields z3.
The pair `(2,2)` gives phase `1/4` and the core itself. The pair `(3,1)` requires phase at least `2/3`, whereas its phase is below `1/2`, so it fails.
At target z3, old `B=-2I2` and `A=-2I2/d`, with only `(d,q)=(1,2),(2,1)`.
For `(1,2)`, the source is z2 and g is `8i`, whose phase `1/4` gives actual digit 1 at n=2.
For `(2,1)`, g is `(-1-2i)^2=-3+4i`, with phase strictly below `1/2`, hence again digit 1 rather than required 2. That candidate is rejected.
At target z2, the sole pair `(1,1)` gives z1, whose source g is `(-3-2i)^2=5+12i!=0`; register one has digit 1.
There is no inverse at target register one. This proves complete exhaustion at every depth and includes all operator and source checks.
The four points are distinct, and all transient B are scalar with d=1. Thus their own forward factors are exactly 1 for both MAIN and C.
At the core, `rho=abs det_R4(2 Id_4)=2^4=16`; put `L=log 16`.
This is the FULL eight-entry germ clock, not the derivative of a selected two-scalar section. The core and its finite basin are Lebesgue-null but retained by the frozen all-point prescription.
Every point of this basin has least eventual source period 1, source isotropy `Z`, ENTIRE `H=L Z`, trivial extension isotropy and all height phases `h mod L`.
Prefixes have zero sum and cannot enlarge H or create a smaller positive physical return.

There is also an explicit complete groupoid on this basin. For `j,k in{1,2,3,4}`, every triple `(zj,ell,zk)`, `ell in Z`, is actual by meeting far enough along the fixed future.
Since the tail length of zj is `4-j`, cancellation gives exactly `c(zj,ell,zk)=(ell+j-k)L`.
Its full clock kernel has `ell=k-j`; its full lag kernel has `ell=0`; their intersection consists only of the four unit arrows.
The source isotropy at zj has `j=k`, so its entire clock image is exactly `L Z`, independently verifying the physical period without selecting a loop or predecessor.
Over each owner's four-point source class there is one full physical height-translation packet, with primitive L and repetitions `rL` for positive integers r.
Phases in `R/L Z` are not extra packets; MAIN and C remain different owners despite having the same listed coordinates.
S has no fixed core or fixed-core incoming class. No H value or packet is invented for its empty fixed sector, and its full-source conditional history formulas still apply.

## 7. Decisive bounded result and freeze boundary

All three owners have complete inverse atlases and positive finite, all-point, every-Borel inverse-germ IMAGE in the stipulated counting-times-Lebesgue8 measure.
The MAIN fixed gate itself contains a positive primitive `log 16=4 log 2`, where 16 is not an ordinary integer prime.
Its whole H is `log 16 Z`, so `log 2` is not a return: neither a source-period division, clock rescaling nor a null-core deletion is permitted.
Therefore MAIN fails the necessary ordinary-prime-time target by its OWN full-source packet: `OWNED COMMUTATOR IMAGE CLOCK; COMPOSITE FIXED PRIMITIVE — STOP / FORK`.
C independently has the same own fixed-core violation; it is not the source of MAIN's negative verdict. S's empty fixed set alone remains only a bounded fixed-window result.
No period-two or higher census, broader global no-period assertion, parameter repair or new owner is needed or undertaken.
The same-object ledger remains intact: full source, exact phase/operator permissions, actual germ measure clock, retained-lag groupoid, whole H, incoming, phases and repetition convention all belong to their own frozen owner.
Owner/clock construction is established here, but arithmetic T1 is NOT PASSED; the fixed-window target has a decisive MAIN obstruction. T3 is NOT AUDITED, classical fields NOT APPLICABLE, formal coordinates UNASSIGNED and Route B NOT INVOKED.
Naturalness, novelty and unrelated higher-period classifications are not certified. ARS supplies scope/provenance discipline, not external mathematical validation.
Freeze this raw after full self-read and measured receipt, then HOLD for root's full read and separate PAPER UNLOCK; no author or peer surface has informed it.

EOF — card-only raw derivation; MAIN STOP / FORK from its complete fixed gate.
