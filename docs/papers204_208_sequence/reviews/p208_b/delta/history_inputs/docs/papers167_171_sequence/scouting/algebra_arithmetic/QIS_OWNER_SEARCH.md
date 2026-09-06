# QIS preliminary owner search

Search date: 2026-09-03.  Rule: substantive conclusions below use author
preprints or publisher pages only.  This is a bounded scouting search, not a
novelty certificate.

## Candidate searched

```text
K = F_{p^4}; states are all F_p-subspaces A <= K;
J(A) = span_Fp({a^{-1}: a in A, a != 0}).
```

Search strings included variants of:

- `finite field inversion subspace lattice dynamical system`;
- `span inverses subspace finite field iteration dynamics`;
- `image of a subspace inverse function finite field span`;
- `inverse of line cyclic model PG(n,q) normal rational curve`;
- `A inverse contained in B finite field subspaces same dimension`;
- the exact phrases `quartic inverse-span`, `iterated span of inverses`,
  `inverse-span dynamics`, `functional graph`, `preimage`, and `zeta` paired
  with `finite field subspace`.

The exact-dynamics strings did not return a source stating this self-map's
functional graph, tail dichotomy, zeta function, or fibre atlas.  That no-hit
is only evidence about these bounded queries.

## Primary owners found

### 1. Direct equality-case owner

Nikolay Kolomeec and Denis Bykov, *On the image of an affine subspace under
the inverse function within a finite field*, arXiv:2206.14980 (2022):

<https://arxiv.org/abs/2206.14980>

Their abstract states that, for patched inversion on `F_{p^n}`, an affine
`F_p`-subspace of size greater than two has affine-subspace image exactly when
it is a nonzero scalar multiple of a subfield.  In QIS, equality
`dim J(A)=dim A` means by cardinality that patched inversion maps `A` onto the
linear subspace `J(A)`.  Their theorem therefore directly supplies the
classification of recurrent candidates.

**Owner subtraction:** QIS cannot claim the characterization of lines/scaled
quadratic subfields as a new inversion-preserving-subspace theorem.

### 2. Direct inverse-line geometry owners

Giorgio Faina, György Kiss, Stefano Marcugini, and Fernanda Pambianco,
*The Cyclic Model for PG(n,q) and a Construction of Arcs*, European Journal of
Combinatorics 23(1), 31--35 (2002), DOI 10.1006/eujc.2001.0525:

<https://www.sciencedirect.com/science/article/pii/S0195669801905256>

The publisher abstract says that the inverse of a line is always a normal
rational curve in some projective subspace, with the subspace dimension tied
to a divisor of the extension degree.

Michel Lavrauw and Corrado Zanella, *Geometry of the inversion in a finite
field and partitions of PG(2^k-1,q) in normal rational curves*, arXiv:1311.4309,
later Journal of Geometry 105 (2014), 103--110:

<https://arxiv.org/abs/1311.4309>

The authors explicitly study the projective inversion map and give a more
detailed description of inverse lines, including the small-`q` regime as
independent `(q+1)`-tuples.

**Owner subtraction:** the fact that a non-subfield plane in `F_{p^4}` has an
inverse projective line spanning a twisted cubic/independent tuple is known
geometry.  The elementary rational-function proof in the proof package is an
independent derivation, not a novelty claim.

### 3. Strong adjacent inverse-subspace owners

Sandro Mattarei, *Inverse-closed additive subgroups of fields*, arXiv:
math/0511538; Israel Journal of Mathematics 159 (2007), 343--348:

<https://arxiv.org/abs/math/0511538>

This classifies additive subgroups closed under inversion.  In odd
characteristic it includes subfields and trace-zero groups from quadratic
extensions.  It is a direct owner of the fixed/equality geometry, though the
QIS recurrent map may exchange two scalar copies rather than fix one.

Bence Csajbók, *Linear subspaces of finite fields with large inverse-closed
subsets*, Finite Fields and Their Applications 19(1), 55--66 (2013), DOI
10.1016/j.ffa.2012.10.005:

<https://www.sciencedirect.com/science/article/pii/S1071579712000937>

This studies equal-dimensional subspaces `A,B` with large intersection between
`A^{-1}` and `B`, using linearized polynomials and Singer-group geometry.

Sandro Mattarei, *Inversion and subspaces of a finite field*, arXiv:1311.3644;
Israel Journal of Mathematics 206 (2015), 327--351:

<https://arxiv.org/abs/1311.3644>

This sharpens bounds for `|A^{-1} cap B|` for equal-size subspaces and
classifies extremal small-dimensional examples.

Sandro Mattarei, *A property of the inverse of a subspace of a finite field*,
arXiv:1312.1293; Finite Fields and Their Applications 29 (2014), 268--274:

<https://arxiv.org/abs/1312.1293>

This proves geometric restrictions on inverse sets and their intersections
with two-dimensional subspaces; its publisher text also recalls the known
normal-rational-curve description of inverse lines.

## Claim-by-claim ownership matrix

| Proposed statement | Search assessment | Treatment |
|---|---|---|
| Patched inverse of a subspace is a subspace iff it is a scalar subfield | **Directly owned** by Kolomeec--Bykov (with antecedents in Mattarei) | Cite as an external theorem; no novelty language. |
| Inverse of a projective line is a normal rational curve/independent small tuple | **Directly owned** by Faina et al. and Lavrauw--Zanella | Cite; retain the short rational-function proof only for self-containment. |
| Recurrent QIS states are zero, full field, lines, and scaled quadratic-field planes | Immediate dynamic corollary of a direct owner plus rank monotonicity | At most a synthesis lemma. |
| Sharp QIS tail is 2 at `p=2`, 1 at odd `p` | No exact iterated-span statement found | Candidate residual contribution, but geometrically close to inverse-line owners. |
| Complete component graph and image stabilization | No direct match found | Candidate residual contribution. |
| Fixed/two-cycle counts and Artin--Mazur zeta | No direct match found; follows easily after classification | Secondary synthesis contribution, not sufficient alone. |
| Every-target, every-time fibre atlas; binary hyperplane fibre exactly 2 | No direct match found | Strongest residual structural contribution. |
| Twisted Singer relation `J(lambda A)=lambda^{-1}J(A)` | Elementary and implicit in cyclic-model geometry | Tool, not novelty claim. |

## Decision

`GREEN_OWNER_THIN`, not `GREEN`.

There is a coherent paper-shaped residual package: one exact characteristic
anomaly, the full graph, zeta, and complete fibres.  However, both geometric
inputs are directly owned, and much of the recurrent count is a short
corollary.  A paper should proceed only if a stricter citation-graph/full-text
search finds no prior iteration of `A -> span(A^{-1})` and an external reviewer
judges the fibre/graph synthesis substantial enough.

## Required next novelty actions before allocation

1. Backward/forward citation chase from Kolomeec--Bykov, Faina et al.,
   Lavrauw--Zanella, Csajbók, and both 2013 Mattarei preprints.
2. Search MathSciNet, zbMATH, Crossref/OpenAlex, Google Scholar exact phrases,
   and cryptographic papers on inverse-preserved subspaces/S-box invariant
   spaces.
3. Search non-English and thesis literature for iterated `linear span of the
   inverse image`.
4. Ask an external algebra/finite-geometry reviewer the literal question,
   including formulas, rather than presenting only a title/abstract.
5. Kill immediately if the same self-map plus degree-four graph has an owner;
   do not retreat to `p=2` as a parameter-only paper.
