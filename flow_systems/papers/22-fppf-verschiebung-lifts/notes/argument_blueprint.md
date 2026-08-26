# Paper 22 Stage-2 argument blueprint

## Central thesis

For every nontrivial index `N>1`, the locally forced root-factorization
preimage of `V_N([x])` fails descent on a finite-free root cover.  Therefore
big-Witt Verschiebung has no additive lift through Deninger's sheaf
epimorphism on either the fppf or finite-flat site.

## Claim--evidence--reasoning chains

### A1. The source question is an objectwise descent problem, not merely a quotient problem

- **Claim:** Proposition 4.3 supplies local preimages but does not supply a
  global section over every object.
- **Evidence:** Deninger, Proposition 4.3; Stacks Tag `03CN`.
- **Reasoning:** epimorphy in an abelian sheaf category is local surjectivity.
  A global additive lift must nevertheless send each global section to a
  compatible global section.
- **Counterargument:** a sheaf epimorphism should allow a lift after choosing
  local roots.
- **Response:** local roots must agree on double overlaps; the proof computes
  a nonzero failure of that agreement.

### A2. The local preimage on the root cover is forced

- **Claim:** over `B=k[s]`, the only possible restriction is
  `c(s)=q^a sum_(zeta in mu_d)(zeta s)`.
- **Evidence:** the characteristic-`q` product identity, Deninger's
  Proposition 4.5, and the domain-refinement lemma.
- **Reasoning:** `omega(c(s))=1-s^N T^N`; injectivity of `omega` on the
  Dedekind domain `k[s]` rules out every alternative local preimage.
- **Counterargument:** a different local choice might descend.
- **Response:** injectivity proves uniqueness, so there is no alternative
  choice to repair descent.

### A3. The forced local section does not descend for any `N>1`

- **Claim:** the two pullbacks of `c(s)` to the double overlap differ by a
  nonzero kernel section.
- **Evidence:** specialize `s_1` to `epsilon` and `s_2` to `0` in
  `k[epsilon]/(epsilon^N)`; the inner section maps to
  `1-epsilon^dT^d != 1` in the big-Witt sheaf, and multiplication by `q^a`
  is monic on `Z`.
- **Reasoning:** a global image of `(x)^sharp` would have equal pullbacks.
  The surviving specialization contradicts this necessary condition.
- **Counterargument:** the obstruction has zero rational-Witt image and may
  vanish after sheafification.
- **Response:** its big-Witt image detects the inner section before the
  torsion-free sheaf lemma preserves the nonzero `q^a` multiple.

### A4. The explicit failure has extension and finite-flat consequences, but no Route consequence

- **Claim:** for every `u`, `u_*e != V_N^*e`; the same cover disproves the
  finite-flat sectionwise Dedekind assertion as stated in v1.
- **Evidence:** functoriality of extensions, Stacks Tags `010I` and `06XP`,
  and the finite-free nature of `k[x] -> k[s]`.
- **Reasoning:** equality of the pushout and pullback extension classes is
  equivalent to a middle-object morphism inducing `(u,V_N)`.  The explicit
  nonlift excludes such a morphism.  In the finite-flat site, the section
  `1-xT^N` is locally but not globally in the image.
- **Counterargument:** the overlap calculation assumes Cech cohomology
  computes `Ext^1`, or the fppf result automatically implies the finite-flat
  result.
- **Response:** the overlap is used only as a necessary descent test.  The
  finite-flat site-dependent injectivity/refinement step is stated and
  proved separately.

## Logical flow

```text
source question and exact owner
  -> sheaf epimorphism versus global section distinction
  -> torsion-free / detector / Dedekind injectivity lemmas
  -> finite-free root cover and unique local preimage
  -> nonzero double-overlap specialization
  -> all-index fppf nonlift
  -> extension-class consequence
  -> separately checked finite-flat nonlift and source correction
  -> controls and no-Route boundary
```

## Strength assessment

| Subargument | Evidence strength | Logical status | Principal risk |
|---|---|---|---|
| A1 | strong primary/formal | valid | confusing epi with objectwise surjectivity |
| A2 | strong | valid after Dedekind refinement lemma | hidden alternative preimage |
| A3 | strong explicit witness | valid | sheafification/nonzero detector mismatch |
| A4 | strong formal plus explicit | valid with typed categories | overclaiming Cech computation or site transfer |

## Draft-writer instructions

Use a neutral theorem-proof register.  Put the source-sensitive correction in
Section 6, not in the title or opening abstract sentence.  Use "as stated in
v1", "appears to use", and "requires correction".  Do not use Corollary 4.6
as a premise.  Do not introduce any packet, dynamical, operator, or determinant
language except in the explicit nonclaim paragraph.

