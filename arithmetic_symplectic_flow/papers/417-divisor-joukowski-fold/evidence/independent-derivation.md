# 417 independent card-only derivation — full fold owners and the bounded word

Candidate `ANG-20260923-DJF01`; mathematics after root's separate RAW RELEASE.
Sole scientific input: `candidate-card.md`, all 86 lines through EOF, SHA256 `b3daee69e3850c1bd09a95312ecb9157d678996901f863dde8cbc404255e652f`.
Frozen CP1: `scope-review.md`, 58 lines, SHA256 `e6fe9005c24d56b6e47e12b00f2feee9ff951a9062e3ebe2bbab632e3bf6a77b`.
Actual access: the original card was reread completely after release and hashed; CP1 was hash-checked. No author paper, README, ledger, outcome appendix, helper, peer/sibling proof, or other new scientific package was read.
Retained ARS/stream instructions and earlier task history govern method and exposure only. Shared-history, inherited-model internal review is **NOT_CALIBRATED**, not blind, cross-model, human, or external peer review.
No scientific code, numerical grid, external source, auxiliary delegation, parameter fitting, replacement measure, or higher-period census is used.

## 1. Complete source and actual inverse roots

Write `X=N_0×C`, `μ=#×area`, and `a(z)=Arg(z)/(2π)∈[0,1)` for z≠0. All n=0 and z=0 objects remain, as do every owner's forbidden-permission and critical objects.
For d,q≥1 put n=dq and define the sector

`Q_dq={z≠0:(d−1)/(dq)≤a(z)<d/(dq)}`.                       (1)

The legal L cells are `{dq}×Q_dq`; the legal MAIN T, V, H cells also require z²≠q. These cells partition each own legal domain because n and its assigned angle digit determine d uniquely, and permission then determines q.
The half-open sector convention retains every lower ray, including the positive-axis Arg seam when assigned. Illegal objects have identity histories but no absorbing forward loop or step clock.
For fixed d,q let the own complex branch expressions be

`f_T(z)=f_H(z)=(z+q/z)/d`, `f_V(z)=z+q/z`, `f_L(z)=z/d`.

The target memory is m=d+q for T,L,V and m=dq for H. At each target, enumerate every positive factor pair satisfying that own equation; H has none at m=0, while T/L/V have none at m=0 or 1.
For T/H set `Δ=(dw)²−4q` and `ζ_σ(w)=(dw+σ sqrt(Δ))/2`, σ=±1; for V use `Δ=w²−4q`, `ζ_σ=(w+σ sqrt(Δ))/2`. The square-root selector has Arg Δ in [0,2π).
For each such branch the COMPLETE inverse domain is

`E_dqσ^O={(m,w):Δ≠0, ζ_σ(w)∈Q_dq}`, `O=T,V,H`,
`I_dqσ^O(m,w)=(dq,ζ_σ(w))`.                               (2)

Indeed the roots solve `z²−dw z+q=0` for T/H, or `z²−wz+q=0` for V. Their product is q>0, so neither root is zero. A root satisfies z²=q exactly when it is a double root, equivalently Δ=0; thus Δ≠0 already enforces the required branch-critical exclusion.
The sector test in (2) is exactly the original floor digit at n=dq. Divisibility is then automatic, and the quadratic equation proves forward equality. Conversely every actual predecessor solves that quadratic, is noncritical, and is exactly one of the two distinct retained roots. This proves both inverse identities and exhaustion.
When Δ=0 the sole root is excluded as a critical source of that candidate branch, so it contributes no inverse there. This does not delete the target or any inverse belonging to a different d,q.
For L the COMPLETE inverse is instead

`E_dq^L={(d+q,w):dw∈Q_dq}`, `I_dq^L(d+q,w)=(dq,dw)`.        (3)

Here w≠0 is required through Q_dq. There is no critical exclusion z²≠q: the linear control does not retain the fold's removed critical states.
All selectors and sectors are Borel. Each inverse in (2) or (3) is injective on its own domain, because applying the own forward map recovers its target.
For any actual predecessor, its memory and digit first determine d,q; its actual complex value then determines the unique σ at that target when two roots are present. Different descriptions therefore do not create redundant copies of one source point.
The images of all these inverse maps are a disjoint Borel partition of the legal source. For the folded owners this further divides a source sector by its selector-root index; the original sector itself need not be a globally injective branch.
At any fixed target there are finitely many inverse candidates, all tested. Target forward legality is never added to (2) or (3).

## 2. Countable germ atlas, version consistency, and every-Borel IMAGE

For T/H/V fix d,q and consider its rational expression on `C\{0, sqrt(q), −sqrt(q)}`. Its complex derivative is nonzero throughout that set. Thus every point has an open neighborhood on which the expression is injective and has a holomorphic local inverse.
Take a countable cover by rational-center/rational-radius open disks subordinate to such neighborhoods. This exists by the countable basis of C; denote the injectivity disks U_j and their holomorphic inverses by g_j on f(U_j).
Fix one selector-root inverse I_α from (2), with source image S_α. Define the disjoint source partition

`S_αj=(S_α∩U_j)\⋃_{i<j}U_i`, `E_αj=f(S_αj)`.              (4)

S_α is Borel: it consists of the points x in the corresponding legal source sector satisfying `F(x)∈E_α` and `I_α(F(x))=x`. Each S_αj is Borel. Since f is a homeomorphism on U_j, E_αj is Borel; these sets partition E_α, and I_α agrees with g_j there.
At a target whose chosen root is z, any two local inverse germs taking w to z coincide on a sufficiently small common neighborhood by uniqueness of the local inverse. Their derivatives agree. A selector-cut label can jump without changing this germ prescription at any specified actual root value.
The same construction permits source sector endpoints because the local rational expression extends across the sector ray; its permitted Borel subset is simply restricted afterward. No derivative of the jumping selector or Arg representative is taken.
For L the inverse z=dw is already globally holomorphic, and restriction to its own sector domain gives the same chart conclusion without a fold-critical removal.

On an actual folded inverse root z, direct differentiation of the local inverse yields

`J_T=J_H=d²/|1−q/z²|²`, `J_V=1/|1−q/z²|²`,
`J_L=d²`.                                                (5)

These are absolute two-dimensional real determinants: a complex derivative multiplies real area by its modulus squared. They are positive finite at EVERY actual inverse point, since z≠0 and the own folded sources exclude z²=q. No limiting value at an excluded critical source is used.
On each E_αj the ordinary holomorphic chart change of variables proves the IMAGE identity for every Borel subset. Summing the disjoint partition (4) proves for every Borel E⊂E_α

`μ(I_α E)=∫_E J_α dμ`.                                   (6)

This includes selector cuts, lower sector rays, and infinite measures. The memory register is a singleton-to-singleton counting correspondence of factor one, not an additional continuous or lattice determinant.
Hence (5) is the prescribed consistent all-point version, not merely an almost-everywhere representative. The chart construction is countable over all d,q,σ,j and exhausts the full legal source.
For any Borel legal source set A, define `N_A(y)=Σ_α 1_{E_α}(y)1_A(I_αy)`, each summand zero outside its actual domain. Then

`F(A)={N_A>0}`, `μ(F(A))=∫1_{N_A>0}dμ`,
`∫N_A dμ=Σ_α μ(F(A∩S_α))=∫_A exp(κ_F)dμ`.                 (7)

Each restricted image is Borel via the inverse description. The first identity counts the actual union once; the second counts genuine multiple predecessors. No redundant root labels or overlapping target images are added as a union measure.

## 3. Signed clocks and the full actual history owner

At a legal source ξ=(n,z) with its own d,q, equations (5)–(6) give

`κ_T=κ_H=2log|1−q/z²|−2log d`,
`κ_V=2log|1−q/z²|`, `κ_L=−2log d`.                         (8)

These are real and finite on every actual step, including all assigned rays. There is no step clock at a terminal. For the folded owners, neither nonnegativity nor nonpositivity is assumed.
The complete legal zero-step loci are `|1−q/z²|=d` for T/H, `|1−q/z²|=1` for V, and d=1 for L, always with the full own source predicates. Zero-step loci are not a cycle or isotropy classification.
Define the nonzero branch-derivative factors

`b_T=b_H=(1−q/z²)/d`, `b_V=1−q/z²`, `b_L=1/d`,
`B_a(ξ)=∏_{j<a}b_F(F^jξ)`, `B_0=1`, `S_a=2log|B_a|`.       (9)

Products are taken only along legal finite histories; an endpoint may be terminal. These are products of the frozen local branch germs, not an assertion that the full discontinuous digit map is differentiable across sectors.
The actual groupoid and its clock are

`G_F={(ξ,a−b,η):F^aξ=F^bη, a,b≥0 legal}`,
`c_F(ξ,a−b,η)=2log(|B_a(ξ)|/|B_b(η)|)`.                    (10)

Equal triples are one arrow, with integer lag retained. Two witnesses of one triple have lengths differing by a common increment; their added common legal future cancels from S_a−S_b. Thus c descends.
For composition, align the two middle histories at their longer legal length. Their meeting equality supplies the corresponding legal extension on the other side, so the middle sums cancel. This proves additivity without continuing a terminal after its lifetime.
The legal finite-iterate equality loci are Borel. Finitely many incoming roots per target and finitely many predecessors at each fixed depth give countable source fibers for G_F.
Finite-history inverse charts have IMAGE `exp(−S_a)=|B_a|^(−2)` by (6) and the chain rule. A branch-pair chart from η to ξ has range/source IMAGE `exp(−c_F)`, using precisely those same point versions.

The COMPLETE kernels, with all displayed meetings required to be actual and legal, are

`ker c_F=⋃_{a,b}{(ξ,a−b,η):F^aξ=F^bη, |B_a(ξ)|=|B_b(η)|}`,
`ker lag_F=⋃_a{(ξ,0,η):F^aξ=F^aη}`,
`ker c_F∩ker lag_F=⋃_a{(ξ,0,η):F^aξ=F^aη,|B_a(ξ)|=|B_a(η)|}`. (11)

These include non-isotropy arrows; equality of two products without an actual meeting creates no arrow. In particular memory-hold does NOT imply injectivity for this rational fold.
For example, in T and V the two legal sources (1,i),(1,−i) both map to the terminal (2,0); in H they both map to (1,0). Their own b values are both 2, so they give a nonunit arrow in BOTH kernels in each of these three owners. Nevertheless neither terminal-ending source has nonzero isotropy.
As another retained incoming boundary, MAIN maps `(1,exp(iπ/4))` and `(1,exp(−iπ/4))` to `(2,sqrt(2))`, which is critical under its own target digit d=1,q=2 and therefore terminal. Target criticality does not remove these incoming arrows.

## 4. Entire isotropy, physical returns, and the residual source

Nonzero source isotropy is equivalent to eventual periodicity of the full forward state: a nonzero isotropy witness repeats a forward state, and such a repetition supplies a legal repeatable cycle.
If the eventual least source period is k and the actual cycle product is `M_C=∏_{j<k}b_F(f_j)≠0`, then

`G_{F,ξ}^ξ=kZ`, `c_F(jk)=jΛ`, `Λ=2log|M_C|`,
`H_ξ=ΛZ`, `extension isotropy={jk:jΛ=0}`.                  (12)

All transient prefix factors cancel. Every multiple of k occurs and no smaller nonzero lag can occur. If no eventual cycle exists, source and extension isotropy are units and H={0}; this includes finite terminal-ending histories.
For Λ≠0 the entire physical least positive return is |Λ|, and all repetitions are r|Λ|, r≥1. For Λ=0 the physical height action is free, but source/extension isotropy kZ remains. In folded owners neutral cycle products may involve cancellation of nonzero step clocks; they are not restricted to cycles of individually zero steps.
Retain every object `(ξ,h)∈X×R`, with arrows `(η,h)→(ξ,h+c_F)`. The stabilizer of height translation on its orbit SET is exactly H_ξ, not a selected subgroup or a substituted positive roof.
For a source-orbit reference o and an actual arrow g:ξ→o, all extension phases are `h+c_F(g) mod H_o`. Choices differ by reference isotropy, and composing isotropy realizes every subgroup adjustment. Thus the full height orbit is R/H_o, with every phase retained.
For an arrival `F^aξ=f_j`, where `f_j=F^j f_0` lies on a k-cycle, this becomes

`h+S_j(f_0)−S_a(ξ) mod H_{f_0}`.                            (13)

In particular the forward-arrival arrow `(f,−a,ξ)` has clock −S_a(ξ), agreeing with the card's forward-clock sign; at a fixed core the phase is h−S_a(ξ).
All incoming is specified by `Pred_0(y)={y}` and taking EVERY own inverse in (2)–(3) at each point of Pred_a(y), with its exact intermediate tests, to form Pred_{a+1}(y). The full source orbit is

`Orb_F(y)=⋃_{b≥0:F^b y defined} ⋃_{a≥0} Pred_a(F^b y)`.      (14)

Both inclusions follow from actual meeting triples. No selected inverse tree, critical continuation, or terminal deletion is introduced. This is an exhaustive all-state conditional ledger; higher-cycle locations for the folded owners remain unclassified.

For L a direct scaling identity sharpens its own residual ledger without a census. Every legal history has `z_a=z_0/D_a`, `D_a=∏d_j≥1`, and S_a=−2log D_a.
A cycle at nonzero z would force D_a=1, hence every d_j=1. Its memory would then increase from n to n+1 at every step, so no L cycle exists. Consequently L source/extension isotropy is trivial and H={0} everywhere.
For any L arrow between nonzero complex coordinates z (range) and w (source), the meeting equality gives `c=2log(|w|/|z|)`. Thus its clock kernel is the actual arrows with |z|=|w|, equivalently z=w because the meeting scales are positive real. Its lag kernel and intersection remain exactly (11), not automatically units.
L has no nonidentity incoming to a z=0 or memory-zero object; such objects keep only their identities. This control's direct global conclusion is not transferred to MAIN/V/H.

## 5. Complete fixed sets of all four owners

A fixed state means a legal one-step return, not a terminal identity. For T,L,V its memory obeys `dq=d+q`, or `(d−1)(q−1)=1`; hence d=q=2 and n=4, with angle sector `[π/2,π)`.
For T its fixed complex equation gives z²=2. The formal roots ±sqrt(2) do not belong to that required sector; they would also be critical for the hypothesized d=q=2 branch. Therefore `Fix(T)=empty`.
This does not declare both formal points critical under their ACTUAL digits: (4,+sqrt(2)) actually has digit 1,q=4, while (4,−sqrt(2)) has forbidden digit 3. Both full-source objects are retained with their actual statuses.
For L the own fixed equation z=z/2 forces z=0, excluded from its legal steps. Thus `Fix(L)=empty`, without importing the removed critical exclusion.
For V the own equation z=z+2/z is impossible at a finite nonzero z. Thus `Fix(V)=empty`; no point at infinity is added to manufacture a fixed state.

For H memory is held, so n=dq is arbitrary and the fixed complex equation is

`(d−1)z²=q`.                                             (15)

There is no d=1 solution. For d=2 every formal root satisfies z²=q, violating the required critical test whenever its source digit would be 2.
For d≥3 the roots are real and nonzero. A positive root has actual angle digit 1, not d. A negative root has angle π, requiring

`d=1+floor(dq/2)`, equivalently `2−2/d≤q<2`.                (16)

For d≥3, any q satisfying (16) would obey 1<q<2, impossible for an integer. Therefore no negative root is admissible either, and `Fix(H)=empty`.
The four complete fixed-sector positive packet ledgers are consequently empty. No conclusion about MAIN/V/H higher periods or their entire global positive ledger follows from this fixed calculation.

## 6. The complete MAIN 5→6→5 word, with every source check

Use exactly the prescribed ordered branches `(d,q)=(1,5)` then `(2,3)`. Their formal return equations at nonzero z_0,z_1 are

`z_1=z_0+5/z_0`, `2z_0=z_1+3/z_1`.

Writing A=z_0² and eliminating z_1 gives

`A²−3A−25=0`, `A_±=(3±sqrt(109))/2`.                       (17)

To see equivalence without lost denominators, multiply `2z_0z_1=z_1²+3` by z_0² after substituting z_1=(A+5)/z_0. The resulting equation is (17). Its roots are nonzero and are not −5; conversely each root and either square root z_0 gives a nonzero z_1 satisfying both displayed equations.
Set `R=sqrt(A_+)>0`, `B=−A_-=(sqrt(109)−3)/2`, `S=(A_++5)/R>0`, and `C=(5−B)/sqrt(B)>0`. The exact inequalities 3<sqrt(109)<13 give 0<B<5.
The COMPLETE four formal pairs, together with their ACTUAL angle digits at memories 5 and 6, are

| z_0 | z_1 | actual digit at (5,z_0) | actual digit at (6,z_1) | required word verdict |
| --- | --- | --- | --- | --- |
| R | S | 1 | 1 | second prescribed digit 2 fails |
| −R | −S | 3 | 4 | first permission fails; second also fails |
| i sqrt(B) | −i C | 2 | 5 | first permission fails; second also fails |
| −i sqrt(B) | i C | 4 | 2 | first permission fails |

Every entry uses the original Arg convention: the four relevant angles are 0,π,π/2,3π/2, with no deleted ray. At memory 5 only the positive-real pair meets digit 1; its next positive-real point has actual digit 1 at memory 6, not the required digit 2.
For the formal prescribed branches there is no zero or critical-denominator artefact: z_0²=A_± is not 5, and substitution into the second equation gives `z_1²=2A_±+7=10±sqrt(109)`, which is nonzero and not 3. These checks do not assign a q to an actually forbidden source; they only rule out extraneous formal singular roots before the actual digit tests above reject all pairs.
Thus there are NO legal MAIN solutions to the frozen 56 word. Rotating to its 65 cyclic phase cannot repair the failed source test, so there is no legal phase at either starting memory. If such a word were legal its distinct memories would force least source period two, but no actual period-two core is realized here.
No physical H or primitive is assigned to a nonexistent word core, and no two phases are counted as separate packets. Every retained formal source point still has its actual own incoming and status governed by (2), (10), and (14), not by these rejected algebraic arrows.

## 7. Bounded decision and limitations

All four owners have complete actual inverse atlases and consistent positive finite all-point inverse-germ IMAGE. Their actual clocks, groupoids, full kernels, conditional entire H, incoming, and phases are owned by the same frozen sources.
The full fixed sets of all four owners and the only additional MAIN word are empty. Thus the declared window finds no core whose basin or positive packet multiplicity remains to classify; its packet multiplicity is zero within that window only.
There is no MAIN wrong primitive, duplicate prime packet, or IMAGE failure established here. The result is therefore **BOUNDED OPEN / FORK**, not a global no-cycle theorem, H=0 claim for MAIN, failure of global nonemptiness, or prime-target success.
L's own direct no-cycle result is a separate control conclusion. Higher-period MAIN/V/H cycles, their entire global positive ledgers, prime-only support, uniqueness, and all-prime coverage remain unclassified beyond the generic exact criteria above.
The lineage is the whole divisor-sector permission followed by the actual q-dependent reciprocal fold, d-dependent transport, and state rereading. Strong naturalness, critical terminalization choices, and PROVES_TOO_MUCH remain unestablished.
The same-object ledger is intact. Classical symplectic/suspension fields are NOT APPLICABLE, T3 NOT AUDITED, formal Route UNASSIGNED, Route B NOT INVOKED. No operator, new parameter, selected-root model, new candidate, or round 420 is started.

EOF — DJF01 card-only derivation complete; preserve this raw and HOLD for root's full read and separate PAPER UNLOCK.
