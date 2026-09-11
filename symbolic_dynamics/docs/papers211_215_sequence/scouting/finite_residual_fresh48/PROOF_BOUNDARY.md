# Proof feasibility boundary

## Claim and status

The desired claim is a source-subtracted, all-parameter temporal theorem
together with a materially separate evaluated all-target inverse/fibre
theorem for one of the two maps specified in DESK.md.

**NOT CURRENTLY JUSTIFIED.** The elementary controls below are provable as
stated, but they do not establish the desired research claim.

## Assumptions and notation

For the matrix control, $R$ is a finite commutative unital ring, $d\ge1$,
$A\in M_d(R)$, and $I$ is the identity matrix. For the graph controls,
$n\ge2$ and graphs are simple, undirected and labelled on $[n]$.
$G^2$ joins distinct vertices at distance at most two; $\overline G$ is
the loopless complement. The map is $T(G)=\overline{G^2}$ on all such graphs.

## Strategy and dependency map

1. The matrix boundary follows by an explicit affine conjugacy.
2. The disconnected-graph control follows by cross-component edges.
3. The labelled seven-cycle obstruction follows by modular step multiplication.
4. The special bipartite control follows by parity of path lengths.
5. The unresolved inverse axis reduces exactly to unrestricted square roots.

## Proof of controls

Step1. Put $E=I-A$. Then $T(A)=(I-E)(I+E)=I-E^2$, so the bijection
$A\mapsto I-A$ conjugates the matrix rule to $E\mapsto E^2$. All iterate
and inverse assertions transfer to that occupied map. If $E$ is nilpotent
with index $\nu$, then the first zero iterate is exactly the least $t\ge0$
with $2^t\ge\nu$; the convention $\nu(0)=1$ gives time zero correctly.

Step2. If $G$ is disconnected, every cross-component pair belongs to $H=T(G)$.
Two vertices in different components are adjacent in $H$. Two vertices in
one component have a common $H$-neighbor in a different component. Thus
$H^2=K_n$, and $T^2(G)$ is empty. This gives no conclusion for all connected
$G$. Since $n\ge2$, the empty graph and $K_n$ are distinct and form a two-cycle.

Step3. On $\mathbb Z/7\mathbb Z$, let $C_s$ have edges of differences
$\pm s$, with $s\ne0$. The square has differences $\pm s,\pm2s$;
therefore $T(C_s)=C_{3s}$. The distinct signed classes $\pm1,\pm3,\pm2$
cycle under multiplication by three, giving exact labelled period three.
This calculation coincides with the old odd-cycle inverse-shortcut action
at seven vertices and does not supply a new temporal mechanism.

Step4. Fix a nonempty bipartition $U,V$ and restrict to bipartite $G$ such
that both $G$ and its bipartite complement $G^b$ have diameter three.
Pairs in the same part have even positive distance at most three, hence two.
Across parts, nonedges have odd distance greater than one and at most three,
hence three. Thus $T(G)=G^b$. The defining condition is symmetric in
$G,G^b$, so the carrier is closed and $T^2(G)=G$. Each cross pair toggles,
so there are no fixed points. The inverse within this restricted carrier is
unique and equals $G^b$. This proof is the primary diameter-three mechanism,
not a separated inverse theorem.

Step5. On the unrestricted graph carrier, $T(G)=H$ is equivalent to
$G^2=\overline H$. No evaluated parametrization or cardinality of this
solution set has been derived. Rewriting the equation is not an inverse
classification. Together with the missing general temporal theorem, this
blocks the desired claim.

## Corrections and open risks

No all-graph period-two statement is made: Step3 refutes it. No labelled
fixedness is inferred from graph isomorphism. No claim that the primary
source settles every temporal question is made. No new all-size theorem
can be inferred from an enlarged pilot. The exact full research claim
remains unjustified; the two controls warrant no admission or reserve.
