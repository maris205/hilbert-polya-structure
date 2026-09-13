# Final proposal: Diagonal-Translation Rigidity and Phase Reciprocity

## Frozen identity

**Working title:** Diagonal-Translation Rigidity and Phase Reciprocity in
Positive Newton-Fan Hamiltonian Shears.

**Article type:** anonymous, proof-first mathematical theory article.  There
is no empirical section and no computational certificate.

**One-sentence contribution:** For separated Hamiltonian shears
\(F=T_W\circ S_V\) with nonempty finite collected supports
\(E_V,E_W\subset\mathbb Z_{\ge2}^{\,r}\), \(r\ge3\), every strict
weighted-degree orbit has an exact all-ones translation, a global
\(d_V+d_W-2\) selector-change bound, and a stationary affine
\((\lambda,\mu)\) tail; reflected inverse phase reciprocity is characterized
edgewise on observable seed spans, with only a local one-edge four-section
lower-ideal lemma.

## Theorem narrative

Let \(K\) have characteristic zero and write
\[
 V(q)=\sum_{\alpha\in E_V}c_\alpha q^\alpha,\qquad
 W(p)=\sum_{\beta\in E_W}d_\beta p^\beta,\qquad
 E_V,E_W\subset\mathbb Z_{\ge2}^{\,r}.
\]
For
\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),\qquad F=T_W\circ S_V,
\]
the inverse is \(F^{-1}=S_V^{-1}\circ T_W^{-1}\), with subtraction.
On a strict edge, unique exposed \(\alpha,\beta\) and positive carries give
\[
 A_\alpha=\mathbf1\alpha^{\mathsf T}-I,\qquad
 B_\beta=\mathbf1\beta^{\mathsf T}-I,\qquad
 (u,w)\mapsto(B_\beta A_\alpha u,A_\alpha u).
\]
The grouped positive-face Hessian determinant, Jacobian criterion, and
injective substitution prove coefficient-uniform leading-form survival.
Writing \(h_V,h_W\) for support functions yields
\[
 v=h_V(u)\mathbf1-u,\qquad
 u'=h_W(v)\mathbf1-v=u+\delta\mathbf1,\qquad
 \delta=h_W(v)-h_V(u)>0.
\]
Along \(u_n=u_0+t_n\mathbf1\), define
\[
 d_V=|\{|\alpha|:\alpha\in E_V\}|,\qquad
 d_W=|\{|\beta|:\beta\in E_W\}|.
\]
The monotone envelope \(g(t)=h_V(u_0+t\mathbf1)-t\) makes every unequal-
total wall cross at most once, so an infinite strict branch has at most
\(d_V+d_W-2\) selector changes and eventually a stationary pair.  Its global-
origin tail is
\[
 t_{n+1}=\lambda t_n+\mu,\quad
 \lambda=(|\alpha|-1)(|\beta|-1)>1,\quad
 \mu=((|\beta|-1)\alpha-\beta)\cdot u_0.
\]

For coordinate reversal \(R\), compare the forward state with
\(R_{\rm state}(u,w)=(Rw,Ru)\).  The reflected inverse uses W then V and
\[
 B_{R\alpha}R=RA_\alpha,\qquad A_{R\beta}R=RB_\beta.
\]
Necessity and sufficiency are asserted only edgewise on
\[
 U_e=\operatorname{span}_{\mathbb R}\{u:(u,w)\in C_e^{\mathbb Z}\},\qquad
 V_e=\operatorname{span}_{\mathbb R}\{A_\alpha u:(u,w)\in C_e^{\mathbb Z}\},
\]
with reflected selector/carry/target certificates.  Full matrices are claimed
only if the relevant spans are full.

## Section and page plan

The target is 25.7 content pages, within a 24–28-page proof-only range;
references, appendices, governance, and discovery history are excluded.

| Section | Content | Pages |
|---|---|---:|
| 0 | Abstract and exact scope | 0.4 |
| 1 | Motivation, contribution, and boundary map | 1.8 |
| 2 | Related work and claim-level collision positioning | 1.5 |
| 3 | Supports, shears, weighted seeds, cells, and theorem | 2.8 |
| 4 | Grouped Hessian, Jacobian, substitution, and transport | 4.2 |
| 5 | Translation rigidity, wall monotonicity, and tail | 3.8 |
| 6 | Reflected phase reciprocity and observable-span converse | 3.5 |
| 7 | Local one-edge lower-ideal lemma | 1.4 |
| 8 | Exact \(r=3\) fixture and failure boundaries | 3.8 |
| 9 | Limitations, collision, and reproducibility safeguards | 1.8 |
| 10 | Conclusion | 0.7 |
| **Total** |  | **25.7** |

Every theorem-critical derivation remains in the main body.  A later appendix
may carry routine matrix multiplication, but not a missing logical step.

## Proof dependencies and acceptance tests

The dependency order is typed supports/seeds → gradient degree maps →
strict carries → translation → monotone walls/tail.  The Hessian/Jacobian
lemma feeds all exact-degree induction.  Reflection identities plus spans feed
the reciprocity converse.  Four normalized projections plus a typed pair core
feed only the one-edge perturbation lemma.  The fixture is a witness, never a
universal proof.

The source-design reviewer must rederive the determinant coefficient, phase
order, carry signs, \(g(t)\) monotonicity, \(d_V+d_W-2\) count, \(\lambda/\mu\),
reflected restrictions, lower-ideal quantifiers, and every listed fixture
gap.  Any finding is a FAIL requiring an append-only disposition and fresh
review.

## Explicit anti-claims

The final article will not claim arbitrary supports, zero-coordinate
extensions, an unconditional algorithm, a global map-level reversor,
conjugacy/classification, entropy, higher dynamical degrees, a minimal scalar
recurrence, a Perron algebraic degree, same-seed reciprocity away from an
\(R_{\rm state}\)-fixed pair, or priority.  E0051's local lemma is not
multi-edge, target-core, C1→C2 perturbation, or all-iterate stability.

## Anonymous and no-external-effect constraints

The future manuscript must contain no author identity, affiliation, internal
event identifier, filesystem path, hash, reviewer name, or provenance
language.  At source-design time no paper directory, manuscript, bibliography,
code, data, figure, build, cache, or PDF is authorized.  No upload, submission,
hosting, repository push, external message, or identity disclosure is allowed.

BATCH07_PAPER27_FINAL_PROPOSAL_FROZEN
