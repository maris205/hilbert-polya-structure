# Autonomous divisor digit renewal: an owned composite primitive

Candidate ID: ANG-20260925-ADR01.
Outcome: OWNED DIVISOR-RENEWAL CLOCK; COMPOSITE PRIMITIVE — STOP / FORK
Paper484; batch PRE-P0-STRUCTURE-20260925-AA, round5/5; 2026-09-25.
Status: exact all-one-consumption classification and decisive MAIN counterexample.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

A current real digit determines an autonomous proper-divisor checking phase.
Consumption changes that real coordinate and thereby changes future arithmetic input.
For four separate full measured owners, the actual inverse atlas gives zero scan clocks and consumption clock \(\log[n(n-1)]\), including all prescribed endpoint values.
All cycles whose least microstep period contains exactly one consumption are classified without a digit cutoff.
MAIN admits precisely prime digits in this window, but its complete \(n=3\) packet has primitive \(\log6\), not an ordinary prime logarithm.
Its \(n=2\) packet with primitive \(\log2\) remains; the failure is purity, not empty positive data.
Full incoming, retained-lag kernels, entire isotropy-clock images, height phases and repetitions are preserved.
No cycle with two or more consumptions is searched.

## 1. Frozen owners, lineage and claim boundary

The [91-line clarified card](candidate-card.md), including the unchanged original81 lines, has SHA256
2dd3d58b9cc323bca77d8795893811f662e7a9967ce6266833bcbb2716155050.
Each owner has its OWN complete \(X=[0,1]\times\mathbb N_{\ge2}\), Borel structure and original \(\mu=\operatorname{Leb}_{[0,1]}\otimes\#\), in \((x,d)\) order.
For \(x>0\), set
\[
 n(x)=1+\lfloor1/x\rfloor,\quad
 I_n=(1/n,1/(n-1)],\quad A_n=n(n-1),\quad L_n(x)=A_nx-(n-1).
\]
The cells \(I_n\), \(n\ge2\), partition \((0,1]\) by the exact floor inequality.
The integer \(n\) is reread from \(x\), not stored as an independent label.

| Owner | Scan \((x,d)\mapsto(x,d+1)\) | Consume \((x,d)\mapsto(L_n(x),2)\) |
| --- | --- | --- |
| M MAIN | \(2\le d<n,\ d\nmid n\) | \(d=n\) |
| P divisibility-OFF | \(2\le d<n\) | \(d=n\) |
| C divisor-hit-consumption | \(2\le d<n,\ d\nmid n\) | \(2\le d<n,\ d\mid n\) |
| E scan-OFF | None | Every \(d\ge2\) |

All unlisted sources and every \((0,d)\) are terminal objects: no outgoing step, but units and all actual incoming remain.
The lineage is actual divisor observation to autonomous checking phase to consumed real digit to new future admissibility.
Neither a prime predicate nor an external schedule selects the action.
No measure normalization, prime table, target weight or log-prime roof is added.
Classical symplectic, mapping-torus, Hamiltonian and quantum fields are NOT APPLICABLE; no operator, trace or zeta is constructed.

The sole location gate is every actual cycle whose LEAST positive microstep period contains exactly one consumption edge, including the closing edge.
Cyclic rotations describe the same core; repetitions are not new packets.
The owner, inverse atlas and history formulas remain global.
Positive nonemptiness, prime-only purity, at-most-one packet per prime and all-prime coverage are distinct target clauses.
Only an actual MAIN falsifier, not an empty or zero-clock window alone, warrants the negative decision here.

## 2. Complete inverse atlas and own every-Borel IMAGE

Every permitted source chart is \(I_n\times\{d\}\), with owner, \(n,d\), and scan/consumption type fixed.
These source pieces are disjoint and cover exactly the legal domain.
A scan chart has image \(I_n\times\{d+1\}\) and inverse
\[
 \theta^{\mathrm{scan}}_{n,d}(y,d+1)=(y,d),\qquad J^{\mathrm{scan}}_{n,d}=1.
\]
On \(I_n\), consumption maps onto \((0,1]\), so its image is \((0,1]\times\{2\}\), and
\[
 b_n(y)=\frac{y+n-1}{A_n},\qquad
 \theta^{\mathrm{con}}_{n,d}(y,2)=(b_n(y),d),\qquad J^{\mathrm{con}}_{n,d}=A_n^{-1}.
\]
Directly, \(b_n(y)\in I_n\) if and only if \(0<y\le1\), and both inverse identities hold.
In particular the reconstructed source digit is \(n\); the target digit need not equal \(n\).

Here is the complete target-by-target enumeration.
For \(y=0\), all four predecessor sets are empty.
For \(y>0,e=2\),
\[
 \begin{aligned}
 F_M^{-1}(y,2)=F_P^{-1}(y,2)&=\{(b_n(y),n):n\ge2\},\\
 F_C^{-1}(y,2)&=\{(b_n(y),d):n\ge2,\ 2\le d<n,\ d\mid n\},\\
 F_E^{-1}(y,2)&=\{(b_n(y),d):n\ge2,\ d\ge2\}.
 \end{aligned}
\]
For \(y>0,e\ge3\), put \(m=n(y)\).
M and C have the sole predecessor \((y,e-1)\) exactly when \(3\le e\le m\) and \((e-1)\nmid m\).
P has that sole predecessor exactly when \(3\le e\le m\); E has none.
Every other predecessor set is empty.
These alternatives exhaust scan and consumption images.
Distinct consumption digits reconstruct disjoint \(I_n\); different source phases are different objects.
Thus overlapping target images do not create duplicate actual predecessors or justify deleting any branch.

All domains and images are Borel and the maps are restrictions of affine ambient diffeomorphisms on their fixed phase fibres.
For every Borel \(B\) in an actual inverse domain, one-dimensional change of variables, with both phase counting factors equal to1, proves
\[
 \mu(\theta^{\mathrm{scan}}B)=\int_B1\,d\mu,\qquad
 \mu(\theta^{\mathrm{con}}_{n,d}B)=\int_B A_n^{-1}\,d\mu.
\]
The displayed positive finite derivatives are the prescribed values at EVERY actual point.
They are supplied by the fixed ambient affine germs, not deduced from a.e. uniqueness.
For E, summing infinitely many predecessor-phase measures can give infinity; each individual branch still has its own finite \(J\), with no division by branch count.

Endpoint ownership is exact: \(x=1\in I_2\), while \(x=1/n\in I_{n+1}\), not \(I_n\).
The inverse at \(y=1\) includes \(b_n(1)=1/(n-1)\).
The formal value \(b_n(0)=1/n\) is outside that branch and must be rejected.
Every actual forward image has positive first coordinate; hence each \((0,d)\) is a singleton terminal source packet, not a loop or a topologically isolated point.
Positive late phases \(d>n(x)\) have no incoming; they are terminal in M/P/C but have actual outgoing consumption in E.
Other terminal targets may have incoming: for example C's \((1,2)\) retains all its consumption predecessors.
No target outgoing legality was imposed in the atlas.

Only after these ownership identities, the actual clocks are
\[
 \kappa=0\text{ on scans},\qquad \kappa=\log A_n>0\text{ on consumption}.
\]
There is no clock at an undefined terminal step, and no unit roof on the scans.

## 3. Full legal histories, cocycle and kernels

Apply this construction separately to each owner.
Let \(D_r\) be the legal \(r\)-step domain, \(D_0=X\), and let
\[
 V_r(z)=\prod_{\substack{0\le j<r\\\text{step }j\text{ consumes}}}A_{n(F^jz)},
 \qquad V_0=1,\qquad S_r(z)=\log V_r(z).
\]
For an actual inverse word \(\Theta\) of length \(r\), restrict its target domain at every intermediate chart.
Its own all-point derivative product is \(J_\Theta(y)=V_r(\Theta y)^{-1}\).
One-step IMAGE extends to nonnegative Borel functions by simple approximation and monotone convergence.
Induction then proves \(\mu(\Theta B)=\int_B J_\Theta\,d\mu\) for EVERY Borel part of every actual word domain.
All domains and source itineraries are Borel; no terminal is extended.

For any target \(p\), define
\[
 B_0(p)=\{p\},\qquad
 B_{r+1}(p)=\bigcup_{w\in B_r(p)}\{\theta_i(w):w\text{ is in that actual inverse domain}\}.
\]
The atlas proves by induction that this is exactly the full depth-\((r+1)\) incoming set.
The index set includes ALL digits and source phases; all compatible infinite inverse sequences remain.
Actual coincident states are identified, rather than counted again for a different word label.
Each finite-depth set is countable, but no depth or label cutoff is made.

The actual retained-lag groupoid and clock are
\[
 G=\{(z,m-r,w):F^mz=F^rw\text{ legally},\ m,r\ge0\},\qquad
 c(z,m-r,w)=S_m(z)-S_r(w).
\]
Source is \(w\), range is \(z\), and only equal triples are identified.
Changing a witness for one triple shifts both depths equally and adds the same common-tail sum.
This proves pointwise descent, including every null boundary.
For composition, extend the shorter middle depth to the longer one using the other witness's legal tail; the middle clock sums cancel.
Thus \(c\) is additive, and the forward arrow \((Fz,-1,z)\) has \(c=-\kappa(z)\).

A history-pair map \(\Theta_\alpha\Theta_\beta^{-1}\) sends \(w=\Theta_\beta y\) to \(z=\Theta_\alpha y\).
Weighted substitution gives its every-Borel IMAGE density
\[
 J_{\alpha\beta}(w)
 =J_\alpha(y)/J_\beta(y)
 =V_{|\beta|}(w)/V_{|\alpha|}(z)
 =e^{-c(z,|\alpha|-|\beta|,w)}.
\]
Every arrow is covered, including terminal units.
The full lag, clock and joint kernels consist of actual meeting triples satisfying, respectively,
\[
 m=r,\qquad V_m(z)=V_r(w),\qquad
 m=r\text{ and }V_m(z)=V_m(w).
\]
They are not automatically units: in E, any fixed \(n,y>0\) and two different source phases give distinct equal-depth consumption predecessors with the same clock, hence a nonunit joint-kernel arrow.

## 4. Entire return groups and all physical phases

Full source packets are exactly actual common-tail classes.
Finite-forward classes are classified by their terminal endpoint: if \(z,w\) reach the same terminal in \(t_z,t_w\) steps, their unique lag is \(t_z-t_w\) and their clock is \(S_{t_z}(z)-S_{t_w}(w)\).
Infinite non-eventually-periodic classes keep the unrestricted legal-meeting test.
These descriptions retain every incoming branch from §3.

A nonzero-lag source loop is equivalent to eventual periodicity.
For any actual least-period-\(q\) core, equal sufficiently late iterates have exactly depth differences in \(q\mathbb Z\).
If its actual cycle sum is \(C\), every incoming source therefore has source isotropy \(q\mathbb Z\), loop character \(jq\mapsto jC\), and ENTIRE
\[
 H_z=C\mathbb Z.
\]
Incoming path sums cancel from loops, and cyclic reindexing leaves \(C\) unchanged.
Every actual cycle in these owners contains a consumption: a sequence of scans alone strictly increases the phase \(d\).
Hence \(C>0\) for every actual cycle.
This is a structural clock statement, not a location census for multi-consumption cycles.
At terminals and infinite non-eventual sources, source isotropy and \(H\) are zero.

On the full \(X\times\mathbb R\), arrows act by \((w,h)\mapsto(z,h+c)\).
Extension isotropy is the kernel of the source loop character, hence zero everywhere here.
In one source packet choose a reference \(p\) and an actual arrow \(g_z:p\to z\), and write \(a_z=c(g_z)\).
ALL extension phases are exactly
\[
 [h-a_z]\in\mathbb R/H_p.
\]
Changing the chosen arrow adds a loop clock; equality modulo \(H_p\) conversely supplies an actual loop adjustment.
Changing the reference translates the coordinate; no global selector or regular quotient is presumed.
Height translation on the orbit SET has stabilizer exactly \(H_p\).
For a periodic core, its primitive is \(C\) and its positive repetitions are \(jC\); if \(H_p=0\), all real phases remain and no positive return exists.
There is no division by \(q\), even when some microsteps have zero clock.

## 5. ALL one-consumption cores, without a digit cutoff

In a least cycle with one consumption, start immediately after that edge, at phase2.
All remaining edges are scans, which preserve \(x\).
Closure therefore forces \(L_n(x)=x\) for one constant actual digit \(n\) throughout the cycle.
Since \(A_n-1>0\), the only possible coordinate is
\[
 x_n=\frac{n-1}{A_n-1}.
\]
It is always actually in its stated cell:
\[
 x_n>\frac1n,\qquad
 x_n\le\frac1{n-1}
 \ \Longleftrightarrow\ (n-1)^2\le n(n-1)-1
 \ \Longleftrightarrow\ n\ge2.
\]
The upper equality occurs only at \(n=2\), where \(x_2=1\).
Thus every candidate coordinate has the correct actual digit; all other coordinates, zero endpoints and incorrectly assigned lower endpoints are excluded.

For M, starting at phase2 reaches consumption at \(d=n\) legally exactly when no integer \(2\le d<n\) divides \(n\).
This is precisely ordinary primality, derived from the current tests, not used to define the action.
For P, all \(n\ge2\) reach \(d=n\).
For C, the first consuming phase from2 is
\[
 \lambda(n)=\min\{d:2\le d<n,\ d\mid n\},
\]
which exists exactly for composite \(n\).
For prime \(n\), C instead reaches the terminal \(d=n\).
Later divisor-hit source phases cannot form another one-consumption cycle, because resetting to2 encounters the first hit before them.
For E, every consumption lands at2, so a one-consumption cycle has just phase2.

These facts give the complete, separate owner ledgers:

| Owner | Allowed digit \(n\) in this window | Whole least core | Least microperiod \(q\) |
| --- | --- | --- | --- |
| M | Ordinary primes | \(\{(x_n,d):2\le d\le n\}\) | \(n-1\) |
| P | Every \(n\ge2\) | \(\{(x_n,d):2\le d\le n\}\) | \(n-1\) |
| C | Composite integers | \(\{(x_n,d):2\le d\le\lambda(n)\}\) | \(\lambda(n)-1\) |
| E | Every \(n\ge2\) | \(\{(x_n,2)\}\) | \(1\) |

The listed phases are distinct; phase2 occurs once before the closing consumption.
Consequently the displayed periods really are least periods, including the period1 cases.
Conversely the corresponding listed steps verify a legal cycle, so the classification is both necessary and sufficient.
Late phases and composite MAIN starts at \(d=n\) remain real objects, but cannot bypass the required return through phase2.
No cycle with another consumption count is classified by this table.

## 6. Whole incoming packets, kernels, phases and multiplicity

Fix one of the listed cores \(\Gamma_n\) in its OWN owner, with \(q\) from the table and
\[
 C_n=\log A_n.
\]
Its complete full-source packet is
\[
 \mathcal B(\Gamma_n)=\bigcup_{r\ge0}\ \bigcup_{p\in\Gamma_n}B_r(p).
\]
Every such state has an actual forward arrival; conversely a common-tail meeting with the periodic core forces a finite arrival in it.
Thus the atlas recursion supplies the entire packet, including every allowed digit/phase predecessor and every compatible infinite incoming history.
It is not a selected symbolic subsystem or a finite inverse tree.

Take the reference \(p_n=(x_n,2)\).
For \(z\in\mathcal B(\Gamma_n)\), let \(t_z\) be its first legal arrival at \(p_n\), and let \(b_z=S_{t_z}(z)\).
Later arrivals occur exactly at depths \(t_z+qj\) and have sums \(b_z+jC_n\), \(j\ge0\).
The COMPLETE restricted groupoid and clock are therefore
\[
 (z,k,w)\in G
 \iff k=t_z-t_w+q\ell\text{ for some }\ell\in\mathbb Z,
 \qquad
 c(z,k,w)=b_z-b_w+\ell C_n.
\]
Necessity follows by extending any meeting to the reference; sufficiency follows by taking nonnegative arrival-loop counts large enough to realize any difference \(\ell\).
The lag kernel imposes \(t_z-t_w+q\ell=0\); the clock kernel imposes \(b_z-b_w+\ell C_n=0\); the joint kernel imposes both.
At EVERY incoming source the source isotropy is \(q\mathbb Z\), the entire \(H=C_n\mathbb Z\), and extension isotropy is zero.
All physical phases are \([h-b_z]\in\mathbb R/C_n\mathbb Z\); the least positive return is \(C_n\), with all repeats \(jC_n\).
Incoming paths cannot create smaller loop times: their sums cancel and their lag differences are exactly multiples of the least core period.

Different listed cores have disjoint full packets, since a common-tail meeting of periodic cores forces the same core.
Also \(A_{n+1}-A_n=2n>0\), so different listed digits in one owner give distinct primitive times.
There is exactly one full packet per listed core; cyclic phases and repeated incoming word descriptions are not additional packets.
This is uniqueness within the one-consumption family, not a claim about unsearched multi-consumption cycles.

## 7. First MAIN falsifier and gate decision

The full symbolic classification precedes witness selection.
For \(n=2\), MAIN has the actual fixed point \((1,2)\) and primitive \(\log2\), which is retained.
For every \(n\ge3\), \(n(n-1)\) is composite because both factors exceed1.
The first allowed MAIN digit after2 is the ordinary prime3.
It gives the exact least two-step core
\[
 (2/5,2)\longmapsto(2/5,3)\longmapsto(2/5,2).
\]
The first step is the actual nondivisor scan; the second is consumption with \(L_3(2/5)=2/5\).
Its step clocks are \(0,\log6\).
By the ENTIRE-group calculation, its primitive is \(\log6\), not \((\log6)/2\) or a chosen repeat.
As \(6\) is not prime and the exponential is injective, this primitive cannot equal \(\log p\) for any ordinary prime.
The complete incoming packet from §6, not just the two displayed states, is the counterexample.

P and E retain their own full one-consumption families, including both prime and composite digits.
C retains its own composite-digit family and all late divisor-hit predecessors.
Their clocks and phase conventions were derived from their own actual charts; no control supplies MAIN credit or alters MAIN multiplicity.
Their results test divisibility permission, consumption at a hit, and phase removal; they do not establish strong naturalness or defeat PROVES_TOO_MUCH concerns.

| Gate | Exact status | Boundary |
| --- | --- | --- |
| T0 | Full inverse atlas, original-measure IMAGE and history owner ESTABLISHED | Broadened measured carrier, not a classical suspension |
| T1 clock COMPONENT | Own scan/consumption clock ESTABLISHED | Arithmetic T1 NOT PASSED |
| T2 short gate | Four complete one-consumption families and their full packets ESTABLISHED | MAIN prime-only purity REFUTED by primitive log6 |
| Positive nonemptiness | Actual MAIN log2 and log6 packets present | Not the same clause as purity, uniqueness or coverage |
| T3 / classical / formal / B | NOT AUDITED / NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No analytic object or formal evaluation |

Decision: STOP / FORK, with same-object ownership intact.
The existing MAIN falsifier is not repaired by any unsearched cycle.
No two-consumption search, endpoint change, new density, clock rescaling or formula retuning follows.

## 8. Reproducibility and AI/access disclosure

Data/proof availability: [frozen card](candidate-card.md), this paper, [claim ledger](claim-ledger.md) and [overview](README.md), following the [paper template](../paper-template.md).
The author personally read card lines1–91 through the clarified EOF and template lines1–107 through EOF; wc and sha256sum bind the card bytes in §1.
Methods are exact affine substitution, unrestricted inverse induction, actual common-tail arguments and symbolic fixed-coordinate/phase classification.
There is no numerical precision or digit/depth cutoff, scientific code, network, old edit, Git mutation, PDF, operator or external publication.
Mechanical checks cover full author self-read, IDs, literal Outcomes, local links, table columns and unchanged frozen-card hash.

AI author /root/batch_clock_scope_review supplied the core classification, full-history derivation, drafting and internal checking; root owns card/integration.
Same-author helper /root/batch_clock_scope_review/ccg_cotangent_probe checked the design tuple in messages only, then after release read ONLY the full91-line frozen card with the same hash as §1.
Its bounded proof task was the four inverse atlases, endpoints, original-measure IMAGE and terminal boundaries, not cycle or target classification; those formulas were checked in §2.
This is author assistance, not a reviewer or independent validation seat.
No current reviewer scope, raw, peer proof or old proof was read during author proof work.
Design-only collision reads were365card1–49/118, prefix SHA
6ea1e5d5c44c5111d6329bfcde400f427adba1881583457a97dcb7c446ae3d0b,
and382card1–48/83, prefix SHA
0c9d4fa8c9b4d1f6acf8ca2684dab7a52e2d0838985618b8326058b8db2c5bf9.
No Outcome body or old proof was read in those two collision files.
Inherited divisor-scan work and informal return-equation feasibility influenced design; it was not blind or sealed preregistration.
After the complete proposal was sent, a list_agents response unexpectedly exposed other blueprints and historical summaries; this was disclosed and did not change the definition.
No global novelty, nonconjugacy, old theorem transfer or cross-candidate credit is claimed.
ARS supplied bounded scope, proof-record and integrity/disclosure discipline, using the personally read router/workflow/runtime and local governance; criteria_binding_unavailable.
Shared-model/history AI assistance is NOT_CALIBRATED; no human, external, cross-model or independent-error mathematical verification is certified.
Human contributions, funding and competing interests are unspecified; no human participants or sensitive personal data are involved.
