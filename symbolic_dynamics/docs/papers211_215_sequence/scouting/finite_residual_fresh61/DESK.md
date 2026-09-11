# Fresh61 — complement/transversal update is old rowmotion

2026-09-11 UTC. Author: current_round_independent_scout.
**ZERO_NEW_LITERALS / ZERO_NOMINATIONS / NO_PILOT**.
This bounded desk closes one retrieval lead at its exact adapter. It does
not reopen an old map or claim that every set-system direction is exhausted.

## Exact rule being screened

Let $U=[n]$, with $n\ge0$, and let a clutter be an inclusion-antichain of
subsets of $U$. Include the empty family and the family $\{\emptyset\}$.
Define edge complementation $C(\mathcal H)=\{U\setminus H:H\in\mathcal H\}$
and let $b(\mathcal H)$ be its inclusion-minimal hitting sets. In particular,
$b(\emptyset)=\{\emptyset\}$ and $b(\{\emptyset\})=\emptyset$.
The screened operation is $T=b\circ C$. These conventions make it a
total autonomous finite map; no shrinking of the ground set is performed.

## Adapter proof

Status: **PROVABLE AS STATED**. The exact claim is that $T$ is ordinary
antichain rowmotion on the Boolean inclusion poset $P=2^U$.
The proof only uses the hitting-set definition and generated order ideal.

For each $X\subseteq U$,
$$
\begin{aligned}
X\text{ hits every member of }C(\mathcal H)
&\iff \forall H\in\mathcal H,\quad X\cap(U\setminus H)\ne\emptyset\\
&\iff \forall H\in\mathcal H,\quad X\nsubseteq H\\
&\iff X\notin\downarrow\mathcal H.
\end{aligned}
$$
Taking inclusion-minimal members yields
$$T(\mathcal H)=\min(P\setminus\downarrow\mathcal H),$$
which is exactly the defining rowmotion formula. Vacuous quantifiers
handle the empty family, and a full-ground edge makes the complement
empty, so both degenerate cases are covered without exceptions.

This is a literal identity, not just similar terminology, a shared
potential or an orbit-level analogy. Its singleton fibres are not the
reason for rejection: it is a directly known action, with no new proved
period/enumeration residual supplied here.

## Specific old collision and historical caveat

The complete original
`docs/papers162_166_sequence/scouting/open_fresh_p166_round2/IDEA_LEDGER.md`
was read (native `82deca`). Its C03/HBL-C is blocker followed by ground
complement, namely $S=C\circ b$ under the fixed-ground interpretation.
Because $C^2=\mathrm{id}$,
$$C\circ S\circ C=b\circ C=T.$$
Thus even reversing the two operations does not create a new map family.

The old row also says “period at most two on support.” That statement is
**not used as a proof premise**. Under the explicit total conventions
above it is false as a universal period claim: on $U=\{1\}$, the old-order
map $S$ has the directly computed cycle
$$\emptyset\ \longmapsto\ \{\{1\}\}\ \longmapsto\
\{\emptyset\}\ \longmapsto\ \emptyset.$$
All three families are distinct. Omitting the degenerate families would
instead require a separate totality convention, since the displayed
operation reaches them. No conclusion about an unspecified altered
support-normalized rule is asserted. The frozen old file is preserved
unchanged; this local caveat does not reopen its historical gate. The
explicit rowmotion identity independently closes the current lead.

## Actual primary source

Michael Joseph, *Antichain toggling and rowmotion*, Electronic Journal of
Combinatorics 26(1) (2019), P1.29,
[primary publisher PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i1p29/pdf/),
was directly opened. Section 2.2, especially Definition 2.4 (PDF page 5,
text lines 142–176), defines antichain rowmotion exactly as the minimal
elements outside the generated order ideal and describes the associated
bijections. This passage, not an inference from a paper title, supports
the adapter. No full 43-page proof audit, visual-page audit, global
Boolean-lattice orbit classification or new theorem is claimed.

## Scope and disposition

The bounded archive lookup (`3d28dc`) found several old blocker controls;
only the specific original above is needed. Source searches located the
Joseph definition, which was then actually read. Secondary results are
retrieval leads, not mathematical evidence. No search non-hit is treated
as novelty clearance.

No second rule, arbitrary-family wrapper, selected-poset restriction or
label decoration was introduced to save this action. No scientific code
was written, imported, parsed or executed, and no pilot, enlarged box,
manuscript, new number, central-index edit, Git operation or external write
occurred. Only this new desk was written. The parent retains reception
authority; there is no independent-review or reserve claim.
