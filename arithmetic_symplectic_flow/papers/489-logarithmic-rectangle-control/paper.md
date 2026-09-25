# Logarithmic rectangle transport retains continuum return-packet multiplicity

Candidate ID: ABF-CONTROL-20260925-LRC01.
Outcome: OWNED LOG FLOW; CONTINUUM LOG2 PACKETS — CONTROL STOP / FORK
Paper489; batch PRE-P0-STRUCTURE-20260925-AB, round5/5; 2026-09-25.
Changed-geometry CONTROL, not a fifth MAIN or an independent prime-source architecture.
Exact proof; same-model/shared-history NOT_CALIBRATED.
Classical ASFS fields NOT APPLICABLE; formal Route coordinates UNASSIGNED;
Route B NOT INVOKED; T3 NOT AUDITED.

## Abstract

The declared logarithmic charts define a Hausdorff translation surface with
the corners removed, a maximal partial flow and its own preserved area measure.
Physical time is the parameter of \(\dot x=x,\dot y=y\), not a logarithm of
an IMAGE factor. The full saturation of the open label-\((1,1)\) rectangle
is a punctured square torus. Every nonzero transverse class gives a distinct
complete packet with entire return group \(\log2\,\mathbb Z\); the diagonal
is one incomplete, nonreturning packet. Thus a continuum of packets shares
the positive primitive \(\log2\). Identity-update control R has the same
tested multiplicity; independent-pairing control D has primitive \(\log6\)
on its tested regular packets; Euclidean control E has primitive \(1\).
All phases, seams, actual time lags and incomplete histories are retained.
These results decide the frozen control without classifying other label classes.

## 1. Contract and four distinct owners

The sole scientific input is the complete 84-line [frozen card](candidate-card.md),
SHA256 d875b4d93fa3cd5b37e4fd5a6e6a94a5841bd3ddfcf2a7ad8460f2ca68967068.
The target is exactly one positive primitive \(\log p\) for each ordinary
integer prime, with no extra packets or times. There is no rescaling,
transverse quotient, centre selection or added clock/height fibre.
The [claim-intent ledger](claim-ledger.md) was written before author derivation.

For \(a,b\ge1\), write \(a-1=bq+r\), \(0\le r<b\), and put
\[
 h_b(a)=bq+1+((r+1)\bmod b),\qquad
 h_b^{-1}(a)=bq+1+((r-1)\bmod b).                                  \tag{1}
\]
Each permutes every block \(\{bq+1,\ldots,bq+b\}\), \(q\ge0\),
and the two displayed maps are inverse. The wrap occurs precisely when
\(b\mid a\): then \(h_b(a)=a-b+1\), otherwise \(h_b(a)=a+1\).
For \(b=1\), \(h_1(a)=a\), including its inverse.
Let \(\pi\) exchange \(2k-1\) and \(2k\) for every \(k\ge1\).

Each owner uses ALL cells \([1,a+1]\times[1,b+1]\) minus their four corners,
and pairs the full open right/top edges with open left/bottom edges.
The original LRC owner is denoted L below; it is still a CONTROL.

| Owner | Right / top label update | Declared coordinates and side lengths | ODE and original measure |
| --- | --- | --- | --- |
| L | \((h_b(a),b)\) / \((a,h_a(b))\) | \(u=\log x,v=\log y\); \(\ell_a=\log(a+1)\) | \(\dot x=x,\dot y=y\); \(\sum dx\,dy/(xy)\) |
| R | Both identity | Same logarithmic charts | Same ODE; own \(\sum dx\,dy/(xy)\) |
| D | \((\pi(a),b)\) / \((a,\pi(b))\) | Same logarithmic charts | Same ODE; own \(\sum dx\,dy/(xy)\) |
| E | L's actual label updates | \(u=x-1,v=y-1\); \(\ell_a=a\) | \(\dot x=\dot y=1\); own \(\sum dx\,dy\) |

Every owner has its own quotient, flow, original measure and physical time.
The arithmetic lineage is the exact residue/divisibility observable in (1),
chosen at an actual geometric seam, changing the next integer cell width.
This is the card's stated divisor-symbolic-to-seam deformation, with changed
geometry and removed direction variable. No result, roof or credit from 486 is used.

## 2. Exact quotient, inverse seams and Borel area

In its declared coordinates every cell is
\([0,\ell_a]\times[0,\ell_b]\) minus corners. A right edge is paired with
the left edge of exactly one cell of the same height; a top edge is paired
with the bottom edge of exactly one cell of the same width.
The permutations in the table make both pairings bijective. Left crossings
use \(h_b^{-1}\), identity or \(\pi^{-1}=\pi\), respectively; bottom crossings
use the corresponding inverse in the second label. Thus all inverse seam
domains are the ENTIRE relevant open edges, with no missing branches.

Every interior point has a rectangle chart. For a right seam at height
\(v_0\), choose collars shorter than both adjacent widths and away from the
two missing endpoints. The chart is \((u-\ell_a,v)\) on the old collar and
\((u',v')\) on the new collar. It joins two half-rectangles into an open
rectangle. Top seams use \((u,v-\ell_b)\) and the next cell's \((u',v')\).
All chart transitions are translations, including self-paired edges.
No corner has a chart or is supplied as a quotient point.

For completeness, these charts give the exact quotient topology, not only a
formal atlas. Each seam class has exactly two edge representatives; an interior
class has one. A collar chart has a saturated preimage open in its two
corner-deleted cells. Conversely the quotient-open condition restricts to
the usual open condition on both halves of each collar and on each interior.
Two distinct classes have finitely many representatives; choose such collars
or interior disks sufficiently small that their preimages are disjoint in
each common cell. This separates the two classes. The quotient is Hausdorff.
Countably many cells, rational interior rectangles and rational collar
subrectangles provide a countable base. The resulting Borel structure is
exactly the Borel structure of this Hausdorff, second-countable surface.

Let \(q_{ab}\) denote the quotient maps. The original measure is, precisely,
\[
 \mu_O(E)=\sum_{a,b\ge1}\int_{q_{ab}^{-1}(E)}du\,dv.                 \tag{2}
\]
Seams have area zero, so their two representatives introduce no extra mass.
Equation (2) is the chart area measure \(du\,dv\); it is sigma-finite since
each cell has finite area. In L/R/D it is exactly the stipulated \(dx\,dy/(xy)\);
in E it is exactly \(dx\,dy\), not a borrowed logarithmic measure.
All seam points and all zero-area trajectories nevertheless remain objects.

## 3. Maximal partial flow, actual time and own IMAGE

The vector field is \((\dot u,\dot v)=(1,1)\) in every chart and matches
across translation transitions. In a single L/R/D cell, before any crossing,
\[
 \Phi^t(x,y)=(xe^t,ye^t),\qquad
 \Phi^{-t}(x,y)=(xe^{-t},ye^{-t});                                 \tag{3}
\]
in E these are \((x+t,y+t)\) and \((x-t,y-t)\).
At each seam the complete inverse permutations above give the unique reverse
continuation. A simultaneous corner hit has no continuation or chosen crossing order.
Raw Euclidean normal derivatives need not match across L's seams:
the specified smooth structure is logarithmic, where the vector field does match.

Explicitly, an interior source next reaches a forward boundary after
\(\min(\ell_a-u,\ell_b-v)\). Unequal margins determine the single crossed
edge, its actual label update and the reset of that normal coordinate to zero.
Equal margins reach a missing corner and stop. In reverse, the next margin
is \(\min(u,v)\); an unequal margin uses the relevant inverse permutation
and resets that coordinate to the full width/height of the predecessor cell.
Equal reverse margins stop at a missing corner. A seam source first uses its
collar chart. This procedure determines every legal forward and inverse domain.

All cell widths and heights are at least \(\log2\) in L/R/D and at least
\(1\) in E. Between consecutive right crossings, the new \(u\) travels from
\(0\) through an entire width; intervening top crossings do not change that
width or \(u\). The same holds vertically and in reverse. Hence a bounded
time interval has only finitely many seam crossings in any owner.
In particular there is no finite-time infinite-chart limit here.
A finite endpoint of a maximal trajectory can only approach a removed corner;
an interior or open-seam endpoint would have a continuation in a chart.
This does not assert that every trajectory is complete.

Let \(I_z\) be the maximal connected open time interval about \(0\) obtained
by this continuation. Uniqueness in charts gives
\[
 I_{\Phi^t z}=I_z-t,\qquad
 \Phi^s(\Phi^t z)=\Phi^{s+t}z\quad(t\in I_z,\ s\in I_z-t).           \tag{4}
\]
A compact legal segment is covered by finitely many charts; small perturbations
preserve their local continuation. Thus the flow domain is open in
\(\mathbb R\times X_O\), and for fixed \(t\), \(\Phi^t:D_t\to D_{-t}\)
is a diffeomorphism with inverse \(\Phi^{-t}\), where \(D_t=\{z:t\in I_z\}\).
There are no artificial terminal self-loops or added endpoint objects.

In a single logarithmic chart, the Euclidean determinant of (3) is \(e^{2t}\),
while the density changes by \(e^{-2t}\); equivalently it is a translation
in \(u,v\). E's own Euclidean translation has determinant \(1\).
Seam transitions also have determinant \(1\) in the owner's declared charts.
Cover a fixed-time legal domain by countably many finite-execution
neighborhoods and disjointify them into Borel pieces. On each piece the
chart area is preserved; countable additivity proves
\[
 \mu_O(\Phi^t A)=\mu_O(A)\quad(A\subset D_t\text{ Borel}),\qquad
 J_{\Phi^{-t}}(z)=1\quad\text{at every }z\in D_{-t}.                \tag{5}
\]
The second formula is the global chart-germ version, including seams and
null trajectories. It is a valid everywhere-defined IMAGE version, not an
assertion that a.e. measure identities uniquely fix null-point values.
The logarithmic RN cocycle is zero. Physical time is nevertheless the
actual \(t\) in (3)–(4), neither zero nor divided by \(\sqrt2\).

The full retained-time groupoid is
\[
 G_O=\{(\Phi^t z,t,z):t\in I_z\},                                  \tag{6}
\]
with inverse changing \(t\) to \(-t\), multiplication adding actual times,
and only equal triples identified. Equation (4) proves these operations.
All finite incoming histories are precisely the unique reverse segments
allowed by \(I_z\); compatible infinite histories are restrictions of the
same maximal trajectory, not new endpoint objects.
The physical-time cocycle is \(t\); its kernel is the unit groupoid, while
the logarithmic RN kernel is all of \(G_O\). No height extension is introduced.
A nonzero return can be repeated in both directions, making that trajectory
complete. A local flow chart excludes sufficiently small nonzero returns,
so its entire return subgroup is \(L\mathbb Z\) with \(L>0\), or \(\{0\}\)
if there is no return. The following sections compute it on the full tested families.

## 4. L, R and E: complete tested saturation

In L and E, \(h_1\) and its inverse fix every integer. Hence both seam
directions and both reverse directions at label \((1,1)\) preserve that label.
No other label is glued to one of its edges. R has this property directly
from its identity pairings. In each owner the unit cell therefore supplies
an entire open-and-closed quotient component. In its OWN coordinates it is
\[
 Y_\ell=(\mathbb R/\ell\mathbb Z)^2\setminus\{(0,0)\},
 \qquad
 \ell=\log2\text{ for L/R},\quad \ell=1\text{ for E}.               \tag{7}
\]
Opposite edges give exactly the two torus translations; the four omitted
corners give the single missing torus point, which has not been restored.
The flow is \((u,v)\mapsto(u+t,v+t)\) modulo \(\ell\), only while the whole
time interval avoids that point. Every open seam point flows locally into
the open cell, so (7) is exactly its full saturation, not only an invariant superset.

Put \(c=v-u\pmod\ell\). For every \(c\ne0\), the complete packet is
\[
 C_c=\{(\theta,\theta+c):\theta\in\mathbb R/\ell\mathbb Z\}.          \tag{8}
\]
It avoids the puncture and exists for every real time. An actual return
requires and is guaranteed by \(t\in\ell\mathbb Z\). Thus the ENTIRE
\(H_z=\ell\mathbb Z\), primitive \(L_z=\ell\), and positive repetitions
are \(m\ell\), \(m\ge1\). Between phases \(\theta,\theta'\), all arrow times
are \(\theta'-\theta+\ell\mathbb Z\), retaining every distinct time triple.
All phases, including both seam phases during a circuit, are present.
Different \(c\)'s cannot meet under any forward or reverse history.
Consequently the tested regular family has exactly continuum many distinct packets.

For \(c=0\) the full surviving packet is the open diagonal
\[
 C_0=\{(\theta,\theta):0<\theta<\ell\},\qquad
 I_{(\theta,\theta)}=(-\theta,\ell-\theta),\qquad H_z=\{0\}.         \tag{9}
\]
Between two of its points the only time is \(\theta'-\theta\); adding
a nonzero multiple of \(\ell\) would cross the absent corner.
There is no primitive or repetition, and its phases remain the open interval,
not a completed circle. These are ALL incomplete trajectories in (7).
Regular reverse histories exist for all negative times; diagonal reverse
segments end strictly before their missing endpoint. Label isolation proves
that there are no unexamined incoming histories from another component.
This proves the complete packet classification separately for L/R/E using
their separately constructed flow and measure, not an inherited clock.

## 5. D: a four-cell component, but a smaller tested saturation

Both \(\pi\) and its inverse preserve the pair \(\{1,2\}\). Thus the entire
component accessible by seams from \((1,1)\) has the four labels
\(\{1,2\}^2\), with no incoming seam from another label pair.
Write
\[
 \alpha=\log2,\quad \beta=\log3,\quad L=\alpha+\beta=\log6,\qquad
 \sigma_1=0,\quad \sigma_2=\alpha,\quad
 U=\sigma_a+\log x,\quad V=\sigma_b+\log y.
\]
The four rectangles assemble into the \(L\)-square torus, split at
\(U=\alpha,V=\alpha\). Internal seams are ordinary continuations, and outer
seams are translations modulo \(L\). The four distinct grid vertices remain absent:
\[
 Y_D=(\mathbb R/L\mathbb Z)^2\setminus\bigl(\{0,\alpha\}\times\{0,\alpha\}\bigr).
                                                                        \tag{10}
\]
This is an explicit bijection compatible with the collar charts, hence a
homeomorphism and translation-chart identification. D's original area and
flow become \(dU\,dV\) and \((\dot U,\dot V)=(1,1)\) on this punctured torus.

The transverse invariant is \(c=V-U\pmod L\). The punctures have transverse
classes \(0,\alpha,-\alpha\); class \(0\) contains two punctures.
The open \((1,1)\) rectangle has \(0<U,V<\alpha\), so its transverse classes
are precisely the arc
\[
 J=(-\alpha,\alpha)\pmod L.                                       \tag{11}
\]
Here \(\beta>\alpha\), hence \(L>2\alpha\): the two endpoint classes
\(\pm\alpha\) are not in \(J\). Every \(c\in J\setminus\{0\}\) is represented
in the open rectangle and its WHOLE circle
\(C_c^D=\{(\theta,\theta+c):\theta\in\mathbb R/L\mathbb Z\}\)
avoids all four punctures. It has every real phase, entire \(H_z=L\mathbb Z\),
primitive \(\log6\), repetitions \(m\log6\), and arrow times
\(\theta'-\theta+L\mathbb Z\). Distinct transverse values give distinct packets.

Class \(0\) meets the initial open rectangle only in the small diagonal
\[
 \{(\theta,\theta):0<\theta<\alpha\},\qquad
 I_\theta=(-\theta,\alpha-\theta),\qquad H_\theta=\{0\}.             \tag{12}
\]
Its two missing endpoints cannot be crossed. The other diagonal segment
\(\alpha<\theta<L\), the singular classes \(c=\pm\alpha\), and all classes
outside \(J\) do NOT belong to the requested saturation.
Thus that saturation is exactly the union of the full regular circles with
\(c\in J\setminus\{0\}\) and (12), not all of (10).
These descriptions exhaust all incoming/reverse histories: regular circles
are complete; the small diagonal has only the legal interval (12);
invariant \(c\), missing vertices and the closed label component exclude
every other incoming source. There is no finite-time accumulation of seams.

## 6. Scoped control result and limits

| Owner | Complete regular packets in its tested saturation | Entire return group / primitive | Incomplete packets there |
| --- | --- | --- | --- |
| L | \(c\in(\mathbb R/\log2\,\mathbb Z)\setminus\{0\}\) | \(\log2\,\mathbb Z\) / \(\log2\) | One open diagonal, \(H=\{0\}\) |
| R | Same range, in R's own unit component | \(\log2\,\mathbb Z\) / \(\log2\) | One open diagonal, \(H=\{0\}\) |
| D | \(0<\lvert c\rvert<\log2\), in its \(\log6\)-torus | \(\log6\,\mathbb Z\) / \(\log6\) | Only the small diagonal (12), \(H=\{0\}\) |
| E | \(c\in(\mathbb R/\mathbb Z)\setminus\{0\}\) | \(\mathbb Z\) / \(1\) | One open diagonal, \(H=\{0\}\) |

The absolute-value notation in the D row means the unique real representative
in (11); no phase or sign has been selected within any packet.
L's positive family is nonempty and all its tested regular times equal
\(\log2\), but uniqueness fails with continuum multiplicity. This is enough
to disprove the frozen exact target. No conclusion about coverage by other
label classes is required or asserted.
R proves the same phenomenon without arithmetic label updates: the unit-cell
time cannot certify arithmetic naturalness. D supplies composite exponent
\(6\) as well as continuum multiplicity. E independently has time \(1\):
\(2<e<3\), since \(e=\sum_{n\ge0}1/n!\), its first two terms give \(2\),
and its remaining positive sum is strictly less than
\(\sum_{n\ge2}2^{-(n-1)}=1\). Thus \(1\ne\log p\) for an integer prime.
E also retains the transverse multiplicity.

The unit sector is part of the full frozen owner and cannot be removed after
the test. The same-object ledger remains intact: log geometry/ODE/measure
for L/R/D, Euclidean geometry/ODE/measure for E, actual time for each.
IMAGE preservation alone gives no prime clock, and matching \(\log2\) gives
no packet uniqueness. The OFF controls record arithmetic, geometric,
ownership, robustness and PROVES_TOO_MUCH limits; they are not new MAINs.
T0 ownership is established; strong naturalness remains OPEN; the exact
time/packet target fails at T2. T1 is not a prime-origin PASS, T3 is NOT AUDITED,
and formal Routes remain UNASSIGNED / NOT INVOKED as stated in the header.
Other label classes have only the general construction of Sections 2–3;
their periodic classification remains OPEN. No further census or geometry tuning follows.

## Provenance, reproducibility and integrity

Records: [frozen card](candidate-card.md), [claim ledger](claim-ledger.md),
[README](README.md). Exact coordinate, seam and quotient arguments
are the full method; no numerical simulation, scientific code, truncation,
network, Git, PDF or outside theorem lookup was used.
No reviewer scope/raw/evidence, 486 author result or other new author result
was read. Shared previous author history remains exposure, not blind independence.
The card discloses pre-freeze anticipation of transverse multiplicity and
171/176 definition comparisons; this author did not reopen those cards.
No outcome-sealed preregistration, external novelty or Route credit is claimed.

AI agents supplied mathematical derivation, drafting and internal author checks.
The same-author helper /root/bilateral_transport_review/direct_controls read
only this complete 84-line card as scientific input and derived E's separate
Euclidean saturation/IMAGE/packet calculation; the author checked and integrated
that bounded contribution. It was not an independent reviewer seat.
ARS guidance informed claim-intent-first drafting, scope and disclosure.
Same-model/shared-history work is NOT_CALIBRATED; no human or external
mathematical verification or future review completion is certified.

Data availability: all mathematical inputs and proofs are in this package;
there are no experimental data. Ethics: no human subjects or private data.
Contributions: author formal analysis/writing/self-check, disclosed E helper,
root contract/integration. Funding and human conflicts were not supplied;
none is inferred. Decision: CONTROL STOP / FORK, not a fifth architecture advance.
This author handoff ends the work; no 490 or new owner is begun.
