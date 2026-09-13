# Independent Source-Design Review

## Review identity and scope

This is a fresh independent review of the ten-file author-stopped source-design
package for **Support Size and Finite-Rank Torus Escape for Generalized Hénon
Maps**.  The review was performed after the temporal fence was released on
2026-08-17.  It is a proof, citation, novelty, standalone, lifecycle, and
nonclaim audit; it is not a manuscript review, a computational experiment, or
a submission authorization.

The review used the `research-review` and `proof-writer` standards.  No CAS,
scientific computation, code, numerical scan, or parameter search was used.
The proof was re-derived symbolically rather than accepted from the author's
summary.

## Frozen input verification

Before and after the substantive read, the ten authorized inputs had the
following SHA-256 values:

| File | SHA-256 |
|---|---|
| `experiments/EXPERIMENT_PLAN.md` | `f50a42f9dde61f00801c4696447c6b161a496cdfb7047b468041917225ba65f6` |
| `experiments/EXPERIMENT_TRACKER.md` | `4578dd2cfbedb25cd2a327ba6d865535bf3d007951f9b749032f9bd6d633b83d` |
| `notes/CITATION_VERIFICATION.md` | `6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `bc5541dcebce9b2cb8cb7e180a91097d55f0d6b0fdc74fb5b4be7f432e462311` |
| `notes/NOVELTY_ASSESSMENT.md` | `83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b` |
| `notes/PROOF_PACKAGE.md` | `b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8` |
| `notes/RESEARCH_QUESTION.md` | `43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928` |
| `refine-logs/FINAL_PROPOSAL.md` | `220bb54312f80f17b6b99a37afffa902fd04a6b696c0c3e1f60f4ed8d374b540` |
| `refine-logs/INITIAL_PROPOSAL.md` | `329c7a6687612ff806508640f7add09201ac9ddedd41c10fabd9582a4beab8b2` |
| `refine-logs/REVIEW_SUMMARY.md` | `20256b3f6915781c07dadb6beec26fa69529c5c7d0660b0171c14d460656c55a` |

All ten files were read in full.  Their hashes, byte counts, and line counts
matched the AUTHOR STOP manifest.  The absorbed Paper14 terminal review and
PDF were also independently rehashed as
`9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d`
and
`4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`,
respectively.

## Gate verdict

The conservative independent scores on a ten-point scale are:

| Gate | Required | Score | Verdict |
|---|---:|---:|---|
| Novelty | at least 7.5 | **7.8** | PASS |
| Standalone value | at least 7.5 | **8.0** | PASS |
| Proof correctness and closure | at least 9.0 | **9.3** | PASS |

The author's novelty file deliberately did not invent or preassign numerical
scores.  That omission is not a source-design blocker: these scores are the
output of the separately required independent gate, and they are now recorded
explicitly rather than silently waived.

## Exact statement audit

The package consistently fixes:

- a characteristic-zero field (K);
- collected positive support (1\le e_1<\cdots<e_s=d), with (s\ge2) in
  PC1--PC2;
- nonzero (a,c,b_1,\ldots,b_s\in K^*);
- (P(X)=c+\sum_jb_jX^{e_j}) and
  (H(x,y)=(P(x)+ay,x));
- a finite-rank, not necessarily finitely generated, subgroup
  (\Gamma\le K^*), of rank (r); and
- (T_m=\{Q\in\Gamma^2:H^i(Q)\in\Gamma^2\text{ for }0\le i\le m\}), so
  (T_m) contains (m+1) states and records (m) transitions.

The bound is stated with exactly

\[
\mathcal A(q,R)=(8q)^{4q^4(q+R+1)},
\qquad
\mathcal S_q=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr),
\]

\[
\mathcal S_*=\max_{2\le q\le s+1}\mathcal S_q,
\]

and

\[
\mathcal M(\mathbf e)=2(2^s-1)
+\sum_{|J|\ge2}(e_{\max J}-e_{\min J})
+\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}.
\]

Thus PC1 is exactly

\[
\#T_2\le d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*.
\]

No syntactic repeated-exponent presentation is confused with collected
support.

## Independent proof audit of PC1

### Sparse-image lemma

For a (q\)-term polynomial

\[
F(X)=\sum_{\ell=1}^q f_\ell X^{m_\ell},
\qquad 0\le m_1<\cdots<m_q\le d,
\]

the equation (\lambda u=F(t)) is normalized to

\[
\sum_{\ell=1}^q(f_\ell/\lambda)t^{m_\ell}u^{-1}=1.
\]

The variable tuple is a homomorphic image of (\Gamma^2), so its rank is at
most (2r); coefficients are fixed scalars and are not adjoined to this
group.  Amoroso--Viada bounds the nondegenerate tuples by
(\mathcal A(q,2r)).  A ratio of two coordinates fixes a nonzero power of
(t) of exponent at most (d), giving at most (d) possible (t)'s, after
which (u) is unique.

In the degenerate part, a singleton subsum cannot vanish.  The proper subsets
of sizes (2,\ldots,q-1) number (2^q-q-2).  Each produces a nonzero
polynomial of degree at most (d), hence at most (d) possible nonzero
roots.  This proves

\[
\#\{(t,u)\in\Gamma^2:\lambda u=F(t)\}
\le d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr).
\]

This proof does not use finite generation.  Infinite torsion causes no extra
fiber: the external theorem is rank-based and all remaining fibers are bounded
by ordinary polynomial degree.

### Main nondegenerate local equation

Write

\[
Q=(v,u),\qquad H(Q)=(z,v),\qquad H^2(Q)=(w,z).
\]

Then (T_2) means (u,v,z,w\in\Gamma), and the first recurrence becomes

\[
Z+U+\sum_{j=1}^sM_j=1,
\qquad
Z=z/c,quad U=-au/c,quad M_j=-b_jv^{e_j}/c.
\]

The variable tuple ((z,u,v^{e_1},\ldots,v^{e_s})) is a homomorphic image
of (\Gamma^3), hence has rank at most (3r), independently of whether any
coefficient lies in (\Gamma).  The nondegenerate solutions contribute at
most (\mathcal A(s+2,3r)) tuples.  A fixed tuple has at most (d) possible
preimages (v), so this part contributes at most
(d\mathcal A(s+2,3r)).

### Exhaustive four-type degeneracy check

Choose any nonempty proper vanishing subsum.  Membership of (Z) and (U)
gives exactly the following cases:

| Type | Equations | Labels and bound |
|---|---|---|
| GZ: (Z) in, (U) out | (z=B_J(v)), (-au=c+B_{J^c}(v)) | (J\ne\varnothing); at most (\mathcal S_*) for each of (2^s-1) labels |
| GU: (Z) out, (U) in | (au=-B_J(v)), (z=c+B_{J^c}(v)) | (J\ne\varnothing); at most (\mathcal S_*) for each of (2^s-1) labels |
| R0: neither in | (B_J(v)=0) | (|J|\ge2); at most (e_{\max J}-e_{\min J}) roots |
| R1: both in | (c+B_J(v)=0), where (J) is the complementary monomial set | (J\ne\varnothing); at most (e_{\max J}) roots |

The endpoint checks are sound.  In GZ and GU, (J=[s]) leaves (B_J) with
(s\ge2) terms, while (|J|=1) leaves (c+B_{J^c}) with exactly (s\ge2)
terms.  Thus singleton monomial sides do not require the associated
coefficient to belong to (\Gamma): the complementary multi-term graph is
used instead.  In R0, (J=[s]) is allowed.  In R1, the selected subsum cannot
be the whole left side, so the complementary (J) is nonempty; (J=[s])
corresponds to the allowed selected subsum containing only (Z) and (U).

For either root type, fixing (v=\rho) leaves the second recurrence

\[
w=(c+a\rho)+\sum_{j=1}^sb_jz^{e_j}.
\]

It has (s+1) terms if (c+a\rho\ne0).  If the constant cancels, it still
has exactly (s\ge2) nonzero terms.  The sparse-image lemma therefore bounds
each vertical fiber by (\mathcal S_*), and the first recurrence uniquely
recovers (u) from (v,z).

If several proper subsums vanish, choosing any one label and unioning over all
labels overcounts rather than omits the point.  No partition or uniqueness of
the label is assumed.

The two graph families give (2(2^s-1)\mathcal S_*); the R0 and R1 root
families give the two stated subset sums.  This recovers PC1 exactly.

The checksum

\[
\mathcal M(\mathbf e)=2^{s+1}-2+
\sum_{k=1}^s(2^k-2^{s-k})e_k
\]

follows by counting subsets by maximum and minimum index.  The crude
inequality

\[
\mathcal M(\mathbf e)\le2(2^s-1)+d(2^{s+1}-s-2)
\]

also has the correct numbers of nonempty and at-least-two-element subsets.
Neither checksum replaces the defining subset sums.

## Sharpness and essential assumptions

PC2 is correct for every prescribed collected support.  With

\[
a=b_1=\cdots=b_s=1,\qquad c=-s,\qquad\Gamma=\langle2\rangle,
\]

one has (P(1)=0) and

\[
(1,2^n)\longmapsto(2^n,1),
\]

so (T_1) is infinite in rank one.  This proves sharpness of the
two-transition threshold, not optimality of the numerical constant.

The nonzero-constant hypothesis is genuinely necessary.  For
(P(X)=X^d+X), (a=-1), and any infinite (\Gamma),

\[
(t,t^d)\longmapsto(t,t)\longmapsto(t^d,t),
\]

so (T_2) is infinite when (c=0).  The stated (a=0) example likewise
correctly shows that a free initial second coordinate survives a triangular
degeneration.

## Independent audit of absorbed PC3

For (P(X)=c+bX^d), the local normalized equation has three nonzero variable
terms and rank at most (3r).  If any of the four local equations in a
(T_4) window is nondegenerate, unioning over its index gives at most
(4d\mathcal A(3,3r)) initial states.

For a degenerate local equation, the only pair-subsums give the labels

\[
\begin{array}{lll}
A_i:&x_{i-1}=-c/a,&x_{i+1}=bx_i^d,\\
B_i:&bx_i^d=-c,&x_{i+1}=ax_{i-1},\\
C_i:&bx_i^d=-ax_{i-1},&x_{i+1}=c.
\end{array}
\]

Direct substitution in all nine adjacent words confirms that only (BA) and
(CB) may remain free after two labels.  Every third label closes (BA).
For (CB), only (CBA) can remain free, and only under
(a=-1) and (bc^{d-1}=-1).  Its scalar chain is

\[
bt^d,\ t,\ c,\ -t,\ b(-t)^d.
\]

Each possible fourth label then imposes a nonzero equation of degree at most
(d^2).  Every word of length four therefore has at most (d^2) initial
states, and the (3^4=81) word union gives (81d^2).  Simultaneous labels
are safely overcounted.

The PC3 sharpness family has the correct coordinate order.  With
(b=1), (a=-1), (c^{d-1}=-1), (t=2^n), and
(Q_t=(x_0,x_{-1})=(t,t^d)), the recurrence produces

\[
x_{-1},x_0,x_1,x_2,x_3=t^d,t,c,-t,(-t)^d.
\]

Because (c) and (-1) are torsion, (\langle2,c,-1\rangle) has rank one,
and the distinct (t)'s give infinite (T_3).  Hence PC3's four-transition
threshold is both proved and sharp.

## Citation audit

The exact quantitative proof input is accurately isolated:

- Amoroso--Viada, Theorem 6.2, supplies
  (\mathcal A(q,R)=(8q)^{4q^4(q+R+1)}) for nondegenerate unit-equation
  solutions in a rank-(R) subgroup over an algebraically closed
  characteristic-zero field.  The package explicitly base-extends an
  arbitrary characteristic-zero (K), injects its solutions, and keeps
  coefficients outside the variable group.  It does not quote the theorem in
  positive characteristic or as a count of degenerate solutions.
- Evertse--Schlickewei--Schmidt is correctly historical only and is not used as
  the source of the displayed Amoroso--Viada constant.
- The Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve numbering is corrected
  and safe: Theorem 1.7 is the monic (S)-integral image result; published
  Theorem 1.8 is the local non-Archimedean one-bad-coefficient valuation
  statement; Corollary 1.9 is the associated number-field orbit consequence.
  The package does not miscite the latter as Theorem 1.8.
- Bell--Ghioca Theorem 1.1 is kept to one fixed orbit and a finitely generated
  subgroup.  Arithmetic progressions are allowed to be infinite; in the
  regular-map clause it is the residual set that becomes finite.  The package
  also notes that the Hénon restriction to the torus is generally rational,
  not automatically regular.
- Ji--Xie--Zhang Theorem 1.8 and Corollary 1.9 are described as cyclotomic
  periodic-point non-density results, not finiteness or finite-rank counts.
- Mello--Yasufuku's large-(\epsilon) front hypotheses are not falsely merged
  with the sufficiently-small-(\epsilon), extra-divisor Vojta route.
- Kim--Krieger--Postolache--Szeto Theorems A and B retain their odd-degree,
  degree-at-most, and congruence restrictions and are not turned into a
  classification of all rational or integral periodic points.

These neighboring results do not supply a hidden proof step.

## Novelty, standalone value, and lifecycle

The bounded primary-source search through 2026-08-17 found no direct collision
combining all-initial-state (T_2) survival, arbitrary characteristic-zero
fields, arbitrary finite-rank subgroups, actual support (s\ge2), the explicit
four-type degeneracy budget, and the exact contrast with support one.  This
supports the 7.8 novelty score, but only as a bounded-search assessment.  It is
not a global priority certificate and must be refreshed before a later source
lock or submission decision.

The package is logically standalone.  PC1 and PC2 form the dominant new
theorem-and-sharpness pair; PC3's complete A/B/C proof and example are
reproduced rather than merely cited.  The Paper14 predecessor is
hash-identified as provenance, expressly absorbed, and barred from parallel
external submission.  A later manuscript must preserve that provenance and
no-parallel rule.

The files consistently exclude positive characteristic, (a=0), (c=0),
zero displayed coefficients, affine-conjugacy invariance, numerical-constant
optimality, effective enumeration, height bounds, periodic classification,
and priority over unpublished or unindexed work.  The exact window sharpness
claims are proved; they are not conflated with optimality of the displayed
cardinality constants.

Some source-stage Markdown uses parenthesized symbols where a later manuscript
would use inline mathematical delimiters.  This is a cosmetic rendering issue,
not a semantic ambiguity or a source-design blocker.  The ten files otherwise
agree on notation, scalar order, assumptions, claims, and lifecycle.

## Final disposition

All frozen gates pass.  The source design is mathematically closed at the
claimed scope, citation-safe at theorem-number level, independently valuable,
and standalone after absorption of Paper14.  This decision authorizes only the
source-design PASS requested for this review; it does not authorize a
manuscript, computation, external submission, or parallel use of the absorbed
predecessor.

SOURCE_DESIGN_PASS
