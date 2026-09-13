# Publication-Stage Scope

Date: 2026-08-17 UTC

Candidate: shiftlike_torus_coset_decay_v1

Canonical project: papers/17-shiftlike-torus-coset-decay

Exact public title:

**Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors
and the Exact Zero-Constant Boundary**

Status after the paired publication lock is written:

**PUBLICATION_STAGE_LOCKED / PENDING_INDEPENDENT_PUBLICATION_REVIEW /
NO_DRAFT / NO_SOURCE_REVIEW / NO_BUILD / NO_RELEASE**

## Purpose, authority, and present limit

This document is the human-readable publication-stage contract for one
anonymous, proof-first pure-mathematics article. It translates the passed
source design and paper plan into exact content, path, role, review, build,
and closure rules. Its paired canonical authority is
experiments/publication_lock.json.

The present author may create exactly two project files, in this order:

1. notes/PUBLICATION_STAGE_SCOPE.md;
2. experiments/publication_lock.json.

The scope must be stable and hashed before the lock is written. The author may
then perform read-only validation and must stop. This stage does not authorize
paper/main.tex, paper/references.bib, a review, a compilation, a scientific
run, code, data, a result, a figure, an asset, a release, an upload, a
submission, external communication, or identity disclosure.

The sole possible immediate successor is a fresh independent publication-stage
review at notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md. That path is absent
at the present stop. It may be written only after the publication author has
stopped and only if every conjunctive check passes. Its last nonempty line
must be exactly:

**PUBLICATION_STAGE_PASS**

A blocker has disposition **WRITE NOTHING**. The reviewer cannot repair,
draft, compile, or self-authorize. Even an exact pass activates only anonymous
drafting of the two public sources. It does not activate source review or a
build.

## The fifteen frozen inputs

The current universe \(U_{G15}\) consists of exactly the following fifteen
regular files. Each identity is normative and must be rebound by the canonical
lock.

| Path | Bytes | LF | SHA-256 | Frozen role |
|---|---:|---:|---|---|
| experiments/EXPERIMENT_PLAN.md | 6,234 | 140 | 6d3c765e8d9991ccaccbde358fa4c8119003c27201645ac08654d173a1d470f8 | Zero-science symbolic audit plan |
| experiments/EXPERIMENT_TRACKER.md | 2,465 | 59 | ef600f790719a402b294bb06229463a62450653f1f662ff635ebcd9ca82d9206 | Zero-run lifecycle record |
| experiments/source_lock.json | 53,476 | 1 | 31b7e8d156bfe46f48bbe0fd38fc6d0f7cbd50da1d78eced8eb0d2b9d7ab0c9f | Final canonical theorem, proof, citation, and authority lock |
| notes/CITATION_VERIFICATION.md | 10,066 | 173 | 28e6bc4d461a876e326c08e2a2481fd9f3b30ea3192ddc6c576185e88f317ddf | Verified primary-source ledger |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 10,963 | 83 | becba75688dc6e77c18a301f37daa34a17328cf54968f3707a6b76ad1774fea9 | Claims, evidence, scope, and counterexample matrix |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 18,822 | 354 | 99365584ff6e2fc25f5997bf992c64095c3428c2386bf4e9cfa2923dc50d591b | Fresh review ending PAPER_PLAN_PASS |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 22,043 | 390 | aa67cb9c507e244095df86390bcfe5799c8919a1b32b99b84e94ee98b8538260 | Fresh source-design review |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 19,068 | 332 | 97dca62e01f1906c0a9a5042215badfc6db38b521aff8ba6e7ef996fb751b6b2 | Replacement fresh review of the final source lock |
| notes/NOVELTY_ASSESSMENT.md | 10,258 | 200 | d67777768a84199c48170a8eada1c61af10652c81e080c7c341b90629b2c5e29 | Bounded novelty and portfolio boundary |
| notes/PROOF_PACKAGE.md | 30,089 | 852 | a5649bdc97d6853ddfe2716dc5531cf3d4a581fd9e55b4296c9cfe6ccadbcc77 | Complete symbolic proof package |
| notes/RESEARCH_QUESTION.md | 13,539 | 368 | 894259da46aa6e886af06741c8798503c5d7e8229295a1c76a8f53e399bdc82f | Exact setup and theorem package |
| paper/PAPER_PLAN.md | 46,371 | 848 | 904ecde6dd376da9d701d53e5229071c8f543b839180b59f73ea3c4300e6f356 | Repaired, passed eight-section paper plan |
| refine-logs/FINAL_PROPOSAL.md | 8,233 | 257 | f91e41b0af9bf2ede85516f4362ae3880015b16080326d788e268d359c718bc4 | Final unified proposal |
| refine-logs/INITIAL_PROPOSAL.md | 6,920 | 185 | 7cbf74c1db067b58184055dba18ff3fd0d467141bb3868005715612d108edf14 | Candidate and rejection history |
| refine-logs/REVIEW_SUMMARY.md | 10,835 | 208 | af07dea511210fa75f48db5d580106fd25d7984c3262d9a1f279b5baeab51aa9 | Adversarial issue and closure ledger |

The aggregate identity is 269,382 bytes and 4,450 LF characters. There are no
mutable theorem inputs at this stage. A mismatch in any path, bytes, LF count,
or hash invalidates the publication review and grants no write.

## One article, one contribution, and exact hierarchy

The article is not two adjacent notes. Its one-sentence contribution is:

> A single character-deficit geometry gives the sharp \(k-m\) dimension decay
> for anchored type-\(\nu\) survivor cosets and qualitative \(T_k\)
> finiteness, while removal of the anchor has exactly one nonlinear planar
> two-step resonance, the \(\{1,d\}\) locus \(a=-\beta^2\), whose coset closes
> in \(V_3^0\).

Part A is dominant. Part B is the exact loss-of-anchor boundary of the same
character-partition mechanism. Part A receives the first main theorem, the
largest proof allocation, and the equality/sharpness section. Part B may not
be introduced as an unrelated second theorem note.

The manuscript is qualitative in its arithmetic conclusions. Laurent's
theorem supplies finite unions of coset intersections, not an effective
cardinality bound. No experiment, computation, scan, or numerical result is
evidence.

## Exact mathematical setup and Part A theorem

Let \(\Omega\) be algebraically closed of characteristic zero. Fix
\(k\geq2\), \(1\leq\nu\leq k-1\), and \(a\in\Omega^*\). Let

\[
 P(X)=c+\sum_{j=1}^{s}b_jX^{e_j},
 \qquad 0<e_1<\cdots<e_s,
\]

where \(a,c,b_1,\ldots,b_s\) are nonzero and \(s\geq2\) is the actual
nonconstant support after equal exponents are collected and zero coefficients
are deleted. The type-\(\nu\) map and its zero-based scalar recurrence are

\[
 S(z_1,\ldots,z_k)
  =(z_2,\ldots,z_k,P(z_{k-\nu+1})+az_1),
 \qquad
 x_{n+k}=P(x_{n+k-\nu})+ax_n.
\]

For every \(m\geq0\), \(V_m\subset\mathbb G_m^{k+m}\), with coordinates
\(x_0,\ldots,x_{k+m-1}\), is cut out by

\[
 x_{n+k}=P(x_{n+k-\nu})+ax_n
 \quad(0\leq n<m),
\]

and \(V_0=\mathbb G_m^k\). For a characteristic-zero field \(K\), a map
defined over \(K\), and a finite-rank subgroup \(\Gamma\leq K^*\),

\[
 T_m(S,\Gamma)
  =\{z\in\Gamma^k:S^j(z)\in\Gamma^k\text{ for every }0\leq j\leq m\}.
\]

Thus \(m\) means \(m\) transitions and \(m+1\) states. If
\(z=(x_0,\ldots,x_{k-1})\), the time-\(j\) state is
\((x_j,\ldots,x_{j+k-1})\), and projection to the first \(k\) coordinates is
a bijection

\[
 V_m\cap\Gamma^{k+m}\longrightarrow T_m(S,\Gamma).
\]

The first main theorem must state, without weakening or strengthening:

> For every \(0\leq m\leq k\), if \(H\) is a connected embedded subtorus and
> \(\xi H\subseteq V_m\), then
> \(\dim H\leq k-m\). The same dimension bound holds for a translate of a
> possibly disconnected algebraic subgroup by passage to every component of
> its identity component.

Equality must be exhibited at every window. If \(a=1\) and \(P(1)=0\), set

\[
 R_m=\{\,n-\nu\bmod k:0\leq n<m\,\}.
\]

The subtorus \(H_m\) fixes \(x_r=1\) for \(r\in R_m\) and imposes
\(x_{k+n}=x_n\) for \(0\leq n<m\). It is connected, saturated,
isomorphic to \(\mathbb G_m^{k-m}\), and contained in \(V_m\). The
conditions \(a=1\) and \(P(1)=0\) are sufficient; necessity and a
classification of all equality cosets are not claimed.

For every prescribed actual support size \(s\geq2\), take

\[
 a=1,\qquad b_1=\cdots=b_s=1,\qquad c=-s,\qquad
 \Gamma=\langle2\rangle.
\]

At \(m=k-1\), the sole free initial residue is
\(q=k-1-\nu\). Set \(x_q=t\), set every other initial coordinate to \(1\),
and put \(x_{k+n}=x_n\) for \(0\leq n<k-1\). The choices \(t=2^N\)
give infinitely many states in \(T_{k-1}\). This is the sharp rank-one
clock.

At \(m=k\), the dimension bound excludes positive-dimensional torus cosets.
After the full Laurent bridge below, this proves that \(T_k(S,\Gamma)\) is
finite for every finite-rank \(\Gamma\leq K^*\), with arbitrary torsion and
without finite generation. Since \(T_m\subseteq T_k\) for \(m\geq k\), all
later windows are finite as well.

## Mandatory Part A proof chain

Every implication below belongs in the main text. No appendix exists and no
proof may be deferred to a supplement.

1. **Scheme sanity.** View the defining equations as Laurent-polynomial
   equations in the ambient torus. Eliminate each monic future variable in
   succession. The coordinate ring becomes an iterated localization of the
   initial Laurent-polynomial domain, so \(V_m\) is integral.

2. **Group-algebra singleton rule.** On a connected torus translate
   \(\xi H\), restrict every ambient coordinate to a scalar times a character
   of \(H\). Characters form a basis of the group algebra. After equal
   characters are collected, a nonzero singleton cannot cancel. State the
   torsion-freeness of \(X^*(H)\).

3. **Forced middle character.** In equation \(n\), the nonzero constant
   \(c\), at least two distinct positive exponents, and the singleton rule
   force
   \(\chi_{k+n-\nu}=1\). This step must not be replaced by an informal
   character count.

4. **Exact scalar split.** After aggregation, split according to
   \(P(\xi_{k+n-\nu})\). If it is nonzero, both endpoint characters are
   trivial. If it is zero, then
   \(\chi_{k+n}=\chi_n\) and
   \(\xi_{k+n}=a\xi_n\). Coefficient cancellation is exhausted by this
   zero/nonzero split.

5. **Integral independence.** In the ambient character lattice put
   \[
   A_n=\epsilon_{k+n-\nu},\qquad
   B_n=\epsilon_{k+n}-\epsilon_n
   \quad(0\leq n<m).
   \]
   For each equation, \(A_n\) and either both endpoint basis vectors or
   \(B_n\) lie in the restriction kernel. Prove the locked set of \(2m\)
   relations integrally independent: the \(A\)-pivots form one length-\(m\)
   interval, the \(B\)-endpoint pairs are disjoint, and no pair is wholly
   inside the pivot interval. The first proof table records these pivots,
   supports, and consequences; the prose proves every row.

6. **Character generation.** Prove explicitly that the ambient coordinate
   characters, including all future coordinates, generate \(X^*(H)\).
   Reduce future characters through endpoint relations and then reduce middle
   indices to initial residues. This yields
   \(\operatorname{rank}X^*(H)\leq k-m\).

7. **No gcd phase.** The killed initial residues are exactly the translation
   \[
   R_m=\{\,n-\nu\bmod k:0\leq n<m\,\},
   \]
   which contains \(m\) distinct residues. It is not the iterated orbit
   \(\{-j\nu\bmod k\}\). No hypothesis, case split, or conclusion involving
   \(\gcd(k,\nu)\) may appear.

8. **Disconnected groups.** If \(\xi D\subseteq V_m\) for a possibly
   disconnected algebraic subgroup \(D\), every component is a translate of
   \(D^0\) contained in \(V_m\), and
   \(\dim D=\dim D^0\leq k-m\).

9. **Saturated equality family.** Verify every recurrence on \(H_m\).
   Prove that its relation lattice is a direct summand, hence saturated, so
   \(H_m\) is connected. Prove the displayed isomorphism and exact dimension.

10. **Sharp arithmetic clock.** Verify the free-residue family coordinate by
    coordinate for every \(k,\nu\), with \(q=k-1-\nu\), and verify
    compatibility with \(\langle2\rangle\).

11. **Arithmetic endpoint.** Invoke Laurent only after the geometric
    zero-dimensional result and only through the arbitrary-field,
    division-hull bridge. The conclusion is finite, not quantitatively
    bounded.

## Exact Part B theorem: deleting the constant anchor

Part B fixes \(k=2\), \(\nu=1\), \(c=0\), \(a\neq0\), and

\[
 P(X)=\sum_{e\in E}b_eX^e,
\]

where \(E\) is a nonempty finite set of positive integers, every \(b_e\) is
nonzero, and \(E\) is actual collected support. Write \(V_m^0\) for the
subvariety of \(\mathbb G_m^{m+2}\) defined by

\[
 x_{n+2}=P(x_{n+1})+ax_n\quad(0\leq n<m).
\]

The scalar orientation is fixed:

\[
 x_2=P(x_1)+ax_0,\qquad
 x_3=P(x_2)+ax_1,\qquad
 x_4=P(x_3)+ax_2.
\]

The phase theorem must state all of the following.

- If \(E=\{1\}\), \(P(X)=\beta X\), and
  \(r\in\Omega^*\) satisfies \(r^2=\beta r+a\), then
  \[
  \{(t,rt,\ldots,r^{m+1}t):t\in\mathbb G_m\}\subseteq V_m^0
  \]
  for every \(m\geq0\). Thus linear support can retain a one-dimensional
  coset in every window.

- If \(E=\{d\}\) with \(d\geq2\), if
  \(E=\{p,q\}\) with \(2\leq p<q\), or if \(|E|\geq3\), then
  \(V_2^0\) contains no positive-dimensional connected torus coset.

- If \(E=\{1,d\}\), \(d\geq2\), and
  \(P(X)=\beta X+\delta X^d\), then \(V_2^0\) contains a
  positive-dimensional connected torus coset if and only if
  \[
  a=-\beta^2.
  \]
  On that locus the unique connected positive-dimensional coset is
  \[
  C_d=
  \left\{\left(
   \frac{\delta}{\beta^2}t^d,\ t,\ \beta t,\
   \delta\beta^dt^d
  \right):t\in\mathbb G_m\right\}.
  \]

- For every coefficient choice in every nonlinear support, including the
  resonant \(\{1,d\}\) locus, \(V_3^0\) contains no
  positive-dimensional torus coset.

- Consequently, for every characteristic-zero \(K\) and every finite-rank
  \(\Gamma\leq K^*\) with arbitrary torsion, \(T_2\) is finite for every
  nonlinear support other than the resonant \(\{1,d\}\) locus, while
  \(T_3\) is finite on that locus. The linear support \(E=\{1\}\) is
  explicitly excluded from these finiteness statements and may remain
  infinite for every window.

The existence of \(C_d\) is geometric and does not imply that
\(T_2(S,\Gamma)\) is infinite for every fixed \(\Gamma\). Arithmetic
compatibility must be demonstrated separately.

## Mandatory Part B partition calculus

The main text must give the full local classification, not only its outcome.

1. Restrict one recurrence to a connected coset and write the middle,
   lag, and output characters. If the middle character is trivial, split
   exactly into:

   - \(P(\xi_{n+1})\neq0\), which kills both endpoint characters;
   - \(P(\xi_{n+1})=0\), which gives the root-copy relation
     \(u_{n+2}=u_n\) and scalar \(\xi_{n+2}=a\xi_n\).

   Close the root-copy branch in the next equation.

2. For linear support, verify the all-window chain directly. Include the
   compatible arithmetic data
   \[
   \beta=2,\quad a=-1,\quad r=1,\quad
   \Gamma=\langle2\rangle,\quad t=2^N,
   \]
   which gives \((t,\ldots,t)\) in every window.

3. For nonlinear monomial support \(P(X)=X^e\), \(e\geq2\), show that the
   only nontrivial local relation is
   \(u_{n+2}=u_n=e\,u_{n+1}\), and that two equations give
   \((e^2-1)u_1=0\). Preserve the corrected compatible one-step tuple
   \[
   (x_0,x_1,x_2)=(t^e,t,2t^e)
   \]
   for \(a=1\), \(\Gamma=\langle2\rangle\), \(t=2^N\).
   The transposed tuple is forbidden.

4. For every prescribed actual support size \(s\geq2\), exhibit a compatible
   one-step family. For example take
   \[
   b_1=\cdots=b_{s-1}=1,\qquad b_s=-(s-1),
   \]
   so \(P(1)=0\), then take \(a=1\), \(\Gamma=\langle2\rangle\), and
   \[
   (x_0,x_1,x_2)=(t,1,t).
   \]
   This example is separate from the two-step resonance.

5. If \(|E|\geq3\), place at least three distinct middle power
   characters against only two endpoints. Use the singleton rule and then the
   second recurrence to close every root-copy branch.

6. For \(E=\{p,q\}\), \(1\leq p<q\), let \(u=u_{n+1}\).
   The second proof table must define the exhaustive labels and their scalar
   equations:

   \[
   \begin{array}{ll}
   A:&u_{n+1}=0,\quad u_{n+2}=u_n;\\
   B:&u_n=pu,\quad u_{n+2}=qu,\quad
      a\xi_n=-b_p\xi_{n+1}^{p},\quad
      \xi_{n+2}=b_q\xi_{n+1}^{q};\\
   C:&u_n=qu,\quad u_{n+2}=pu,\quad
      a\xi_n=-b_q\xi_{n+1}^{q},\quad
      \xi_{n+2}=b_p\xi_{n+1}^{p}.
   \end{array}
   \]

   Explain that \(A\) contains the trivial-middle/root-copy branch and that
   \(B,C\) are the two endpoint-to-power partitions. An endpoint-endpoint
   pair would leave the two distinct power characters single, so there is no
   fourth label.

7. The third proof table is the complete adjacent-word transition and closure
   matrix. The prose must derive all nine words:

   - \(AA,AB,AC,BA,CA\) force zero or contradict a nonzero middle;
   - \(BB\) requires \(pq=1\);
   - \(BC\) requires \(q^2=1\);
   - \(CB\) requires \(p^2=1\);
   - \(CC\) requires \(pq=1\).

   Hence only \(CB\) with \(p=1\) can be nonzero.

8. For \(p=1,q=d\), preserve the character vector
   \[
   (u_0,u_1,u_2,u_3)=(du,u,u,du).
   \]
   The first \(C\) equations are
   \[
   a\xi_0=-\delta\xi_1^d,\qquad \xi_2=\beta\xi_1,
   \]
   and the second \(B\) equations are
   \[
   a\xi_1=-\beta\xi_2,\qquad \xi_3=\delta\xi_2^d.
   \]
   Derive, in this orientation, the unique resonance
   \(a=-\beta^2\) and
   \[
   \xi_0=\frac{\delta}{\beta^2}\xi_1^d,\qquad
   \xi_2=\beta\xi_1,\qquad
   \xi_3=\delta\beta^d\xi_1^d.
   \]
   Verify both recurrences directly.

9. Prove uniqueness of \(C_d\): ambient coordinate characters generate a
   cyclic lattice, positive dimension is one, and the nonzero \(x_1\)
   character is surjective on a one-dimensional torus over the algebraically
   closed field.

10. Close \(V_3^0\) after \(CB\): a following \(A\) is impossible, \(B\)
    gives \((d-1)u=0\), and \(C\) gives \((d^2-1)u=0\). If the first four
    characters are trivial, the third equation kills the fifth. The
    adjacent-word table must include this closure column.

11. Exhibit the compatible resonance example
    \[
    \beta=\delta=1,\quad a=-1,\quad\Gamma=\langle2\rangle,\quad
    (x_0,x_1,x_2,x_3)=(t^d,t,t,t^d),
    \]
    with \(t=2^N\). State explicitly that it proves infinite \(T_2\) for
    this \(\Gamma\), not for every finite-rank group.

## Laurent theorem and the exact arbitrary-field bridge

Michel Laurent's 1984 qualitative theorem is the sole imported proof theorem.
In the exact form used: for a closed subvariety \(X\) of a complex algebraic
torus and the division group \(\Lambda^{\mathrm{div}}\) of a finitely
generated subgroup \(\Lambda\), the intersection
\(X\cap\Lambda^{\mathrm{div}}\) is a finite union of intersections with
torus cosets contained in \(X\). The only used corollary is that the
intersection is finite when \(X\) contains no positive-dimensional torus
coset.

The manuscript must prove the bridge rather than cite a stronger field
version:

1. For an arbitrary finite-rank \(\Gamma\), choose
   \(\gamma_1,\ldots,\gamma_r\) whose tensor classes form a
   \(\mathbb Q\)-basis and put
   \(\Gamma_0=\langle\gamma_1,\ldots,\gamma_r\rangle\).

2. For each \(\gamma\in\Gamma\), an integral rational relation says that
   \(\gamma^N\) times an element of \(\Gamma_0\) is torsion. Kill the finite
   order of that individual torsion element. Then
   \(\gamma^{NM}\in\Gamma_0\), so
   \(\Gamma\subseteq\Gamma_0^{\mathrm{div}}\) elementwise.

3. There is no bounded-torsion or finite-generation assumption on
   \(\Gamma\). This elementwise argument includes arbitrary infinite torsion,
   including \(\mu_\infty\) when present, because each torsion element has
   finite order and belongs to the division hull of the identity.

4. For any characteristic-zero \(K\), let \(L\) be generated over
   \(\mathbb Q\) by the finitely many map coefficients and generators of
   \(\Gamma_0\). The finitely generated field \(L\) embeds in
   \(\mathbb C\). Every element of \(\Gamma\) is algebraic over \(L\), and
   the embedding extends to an algebraic closure containing the relevant
   points. Do not assert an embedding of all of \(K\).

5. Apply the complex theorem in the needed Cartesian power. Absence of a
   positive-dimensional torus coset is preserved by the chosen embedding, and
   injectivity transfers finiteness back.

No second unit-equation or Diophantine theorem is imported. In particular,
Evertse--Schlickewei--Schmidt is not a citation entry.

## Bibliography and citation lock

The bibliography contains exactly eight entries, all actually cited. The
exact key set is

\[
\begin{split}
\{&
\texttt{Laurent1984},
\texttt{BedfordPambuccian1998},
\texttt{Bera2018},
\texttt{BeraVerma2013},\\
&
\texttt{BellGhioca2024},
\texttt{JiXieZhang2026},
\texttt{MelloYasufuku2026},
\texttt{KarimovKelmendiOuaknineWorrell2024}
\}.
\end{split}
\]

The cited keys in main.tex, the entry keys in references.bib, and the
\(\backslash\)bibitem keys in the generated main.bbl must be exactly equal to
this set. Wildcard nocite, duplicate keys, missing entries, and uncited entries
are forbidden.

| Key | Locked verified identity | Permitted role |
|---|---|---|
| Laurent1984 | Michel Laurent, “Equations diophantiennes exponentielles,” Inventiones mathematicae 78 (1984), 299--327, DOI 10.1007/BF01388597; journal EuDML record 143175 | Sole imported qualitative proof theorem |
| BedfordPambuccian1998 | Eric Bedford and Victoria Pambuccian, “Dynamics of shift-like polynomial diffeomorphisms of C^N,” Conformal Geometry and Dynamics 2 (1998), 45--55, DOI 10.1090/S1088-4173-98-00027-7 | Type-\(\nu\) terminology and map provenance only |
| Bera2018 | Sayani Bera, “Polynomial shift--like maps in C^k,” arXiv:1805.03142v3 | Complex-dynamical context only |
| BeraVerma2013 | Sayani Bera and Kaushal Verma, “Some aspects of shift-like automorphisms of C^k,” arXiv:1309.3392 | Complex-dynamical context only |
| BellGhioca2024 | Bell--Ghioca, “Intersections of orbits of self-maps with subgroups in semiabelian varieties,” arXiv:2210.03152 | Fixed-orbit, finitely generated subgroup comparison only |
| JiXieZhang2026 | Ji--Xie--Zhang, “Cyclotomic integral points for affine dynamics,” arXiv:2511.13443 | Cyclotomic affine/Hénon rigidity context only |
| MelloYasufuku2026 | Mello--Yasufuku, “On higher dimensional integrality and multiplicative dependence in semigroup algebraic dynamics,” arXiv:2604.03745 | Semigroup-orbit dependence/integrality comparison only |
| KarimovKelmendiOuaknineWorrell2024 | Karimov--Kelmendi--Ouaknine--Worrell, “Multiple Reachability in Linear Dynamical Systems,” arXiv:2403.06515 | Linear algorithmic reachability comparison only |

The separate Laurent Bordeaux seminar record, EuDML 182179, is not the
Inventiones article and cannot be used as theorem-level journal provenance.
Kaur and every ESS entry are excluded. The other seven locked sources are
context only and may not be made proof dependencies. No generated-from-memory
metadata or unverified source may enter references.bib.

## Exact article architecture and page contract

The article uses one monolithic pdfTeX-compatible source and one lean
bibliography:

- paper/main.tex;
- paper/references.bib.

The class line is exactly \(\backslash\)documentclass[11pt]\{article\}.
There are exactly eight numbered main sections, in this order:

1. Introduction and anchor-loss question;
2. Shift-like recurrences, survivor varieties, and the Laurent bridge;
3. Characters on recurrence cosets;
4. Sharp anchored torus-coset decay;
5. Equality subtori and sharp arithmetic clock;
6. Zero-anchor local partition calculus;
7. Exact zero-constant phase and third-step closure;
8. Assumption boundaries, contextual separation, and conclusion.

There is no appendix. References follow Section 8 after an explicit forced
clear page, occupy exactly one final page, and are the last public content.

The abstract is result-first, citation-free, history-free, anonymous, and
contains 180--220 words under the following robust convention. Strip TeX
comments; isolate the abstract environment; replace each maximal inline,
display, delimiter, or named mathematics span by one token; preserve ordinary
text in command arguments while deleting formatting commands and braces;
normalize ties and whitespace; then count maximal word tokens, allowing
internal apostrophes and hyphens, plus each mathematics token as one word. The
source review and receipts record the resulting integer and the exact
counter-snippet hash.

The source author aims at about 22 substantive pages under the passed plan,
within its hard 19.5--22.5 substantive-page credibility range. The suggested
source envelope is 70--95 KB and roughly 8,000--10,500 raw prose words. These
are anti-underdevelopment guides, not quotas. They cannot be met through
spacing, repetition, background inflation, oversized displays, or padding.
The compiled PDF gate is decisive:

- 20--23 nonempty substantive-content pages from page 1 through the end of
  Section 8;
- exactly one nonempty final References page;
- 21--24 total pages;
- no blank page anywhere.

Part A remains dominant in theorem order, proof space, and argumentative
weight.

Exactly three table environments occur:

1. the relation/pivot independence table in Section 4;
2. the \(A/B/C\) label definitions and scalar equations table in Section 6;
3. the adjacent-word transition and \(V_3^0\)-closure matrix in Section 7.

They are proof tables, not empirical tables, and every row is derived in
surrounding prose. There is no other table. There are zero figures, figure
environments, included graphics, image files, raster or vector assets, scans,
external inputs, datasets, experiments, empirical results, or hero figures.
A figure would duplicate the exact lattice and word calculations rather than
clarify them; the three proof tables are the complete visual structure.

## Public-safe predecessor boundary

The following paragraph appears verbatim exactly once, in Section 8 only:

> An earlier companion treatment established stronger explicit bounds for the
> planar nonzero-constant problem and subsumed its own support-one precursor.
> The present article neither reproduces nor improves those planar estimates;
> its contribution is the all-dimensional torus-coset decay profile and the
> exact zero-constant boundary.

It is forbidden in the abstract, Sections 1--7, theorem statements, proofs,
tables, and References. The predecessor is not a bibliography entry or a
black-box proof input. The present article does not absorb it, resubmit it, or
claim improved explicit planar cardinality bounds.

## Fifteen public mathematical anti-claims

All fifteen boundaries must be visible in mathematically natural locations.
Internal paper numbers and governance language are replaced by public-safe
phrasing.

1. Dimension belongs to a torus coset contained in \(V_m\), not to the set
   \(T_m\) itself.
2. Resonance does not make \(T_2(S,\Gamma)\) infinite for every
   \(\Gamma\).
3. The conditions \(a=1\) and \(P(1)=0\) are sufficient for the equality
   family, not asserted necessary.
4. There is no \(\gcd(k,\nu)\) hypothesis or phase.
5. The killed set is the translation
   \(\{n-\nu\bmod k:0\leq n<m\}\), not an iterated orbit.
6. Nonlinear monomials are not in the no-finite-window class when \(c=0\).
7. No effective cardinality, exceptional-locus algorithm, height bound, or
   enumeration follows from Laurent.
8. The standard character-partition and group-algebra singleton observations
   alone are not presented as the contribution.
9. There is no extension to positive characteristic, \(a=0\), rational or
   Laurent maps, or arbitrary polynomial automorphisms.
10. Actual collected support is not asserted invariant under affine
    conjugacy.
11. Finite rank is not replaced by finite generation or bounded torsion;
    arbitrary torsion, including \(\mu_\infty\), is allowed.
12. The present results do not improve the earlier companion's explicit
    planar nonzero-constant cardinality bounds.
13. The bounded primary-source comparison is not a global, exhaustive,
    first-result, or unpublished-work claim.
14. Part A does not classify all equality cosets or all maximal cosets.
15. No periodic-point classification or effective enumeration is claimed.

## Anonymous and public-text contract

The manuscript is an anonymous standard article, not a venue template. It
contains no author name, affiliation, email address, self-identifying link,
acknowledgment, grant, repository identity, submission identifier, date,
identity-bearing timestamp, local path, hash, internal candidate identifier,
paper number, governance term, gate or review verdict, agent name,
operational instruction, or unsupported priority statement.

Neutral bibliographic names, years, journal details, DOI data, and locked
arXiv identifiers are required in citations and References and are not author
identity. They do not authorize a manuscript author line or metadata dates.
The PDF has no author identity, subject or keyword identity, creation or
modification date, trailer ID, or local-path metadata. A generic,
identity-free creator/producer string is permissible only if unavoidable and
recorded.

The public source must contain deterministic pdfTeX controls that suppress the
date, identity-bearing metadata, and trailer identifier. Those controls are
implementation details and may not expose governance text in the article.

## Exact monotone stage universes

Every universe below is an exact set of safe project-relative regular-file
paths. At every stage the only directories are experiments, notes, paper, and
refine-logs; there are zero symlinks and no other entry types.

\(U_{G15}\), count 15, is exactly the frozen-input table above.

\(U_{L17}=U_{G15}\cup\{\)

- notes/PUBLICATION_STAGE_SCOPE.md,
- experiments/publication_lock.json

\(\}\), count 17.

\(U_{P18}=U_{L17}\cup\{\)

- notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md

\(\}\), count 18.

\(U_{D20}=U_{P18}\cup\{\)

- paper/main.tex,
- paper/references.bib

\(\}\), count 20.

\(U_{S21}=U_{D20}\cup\{\)

- notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md

\(\}\), count 21.

\(U_{R0}=U_{S21}\cup\{\)

- paper/main_round0.pdf,
- paper/BUILD_RECEIPT_R0.json

\(\}\), count 23.

\(U_{V1}=U_{R0}\cup\{\)

- notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md

\(\}\), count 24.

\(U_{S1}=U_{V1}\cup\{\)

- paper/SOURCE_REVISION_RECEIPT_R1.json

\(\}\), count 25.

\(U_{R1}=U_{S1}\cup\{\)

- paper/main_round1.pdf,
- paper/BUILD_RECEIPT_R1.json

\(\}\), count 27.

\(U_{V2}=U_{R1}\cup\{\)

- notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md

\(\}\), count 28.

No stage may skip a predecessor, pre-create a later path, or retain a build
intermediate. The sole additions are exactly those displayed.

## Disjoint temporal roles and read/write universes

Roles are temporally disjoint. No role may author an object that it reviews,
read a later-stage artifact, expand its own allowlist, or turn a conditional
permission into current permission.

| Role | Activation | Exact project read universe | Exact project write universe |
|---|---|---|---|
| Publication-stage author | This task only | \(U_{G15}\) | scope, then lock |
| Independent publication reviewer | Stable PUBLICATION AUTHOR STOP | \(U_{L17}\) | notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md only, and only on all-pass |
| Anonymous manuscript author | Exact PUBLICATION_STAGE_PASS | \(U_{P18}\) | paper/main.tex and paper/references.bib only |
| Formal manuscript-source reviewer | Stable source AUTHOR STOP with exact two-source identities | \(U_{D20}\) | notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md only, and only on all-pass |
| Round-0 builder | Exact MANUSCRIPT_SOURCE_PASS plus separate explicit build GO | \(U_{S21}\) | paper/main_round0.pdf and paper/BUILD_RECEIPT_R0.json only |
| Round-1 manuscript reviewer | Stable Round-0 builder stop | \(U_{R0}\) | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md only |
| Sole bounded revision author | Stable R1 review | \(U_{V1}\) | may edit the two public sources and must add paper/SOURCE_REVISION_RECEIPT_R1.json |
| Round-1 builder | Stable revision stop | \(U_{S1}\) | paper/main_round1.pdf and paper/BUILD_RECEIPT_R1.json only |
| Fresh Round-2 manuscript reviewer | Stable Round-1 builder stop | \(U_{R1}\) | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md only |

A bounded pre-source repair author exists only after a separately authorized
repair instruction responding to a zero-write blocker. It reads
\(U_{D20}\), may edit only the two existing public sources, may not enlarge
the theorem or bibliography, and must stop with new source identities. The
same unique source-review path remains absent until a fresh reviewer passes
the repaired sources.

Reviewer independence is substantive and temporal. The publication reviewer
authored none of the fifteen inputs or governance pair. The source reviewer
authored neither public source. The R1 reviewer is distinct from authors and
builder. The R2 reviewer is fresh and distinct from every author, builder, and
prior reviewer.

## Anonymous drafting contract

Only exact PUBLICATION_STAGE_PASS activates drafting, and only under a
separate manuscript-author invocation. The anonymous author reads exactly
\(U_{P18}\) and writes exactly, in one stable source episode:

- paper/main.tex;
- paper/references.bib.

All eight sections, all definitions, theorem statements, proofs, examples,
limitations, three proof tables, the unique predecessor paragraph, and static
controls are in main.tex. No sections directory, macro file, style file,
class file, appendix, supplement, figure, asset, code, data, result, or build
artifact is authorized.

The author does not compile, use the network, install software, invoke CAS or
a symbolic engine, run a scientific calculation, scan parameters, generate
data or assets, or read a future review or build artifact. Static source
checks are permitted. The author reports stable SHA-256, bytes, LF counts, the
abstract count, exact key equality, and exact \(U_{D20}\), then stops. That
stop does not authorize source review automatically.

## Formal source-review gate

There is exactly one formal source-review path:

notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md

It is temporally after a stable manuscript AUTHOR STOP that reports exact
hashes and byte counts for both public sources. A fresh reviewer reads exactly
\(U_{D20}\) and independently checks:

- the exact title, 11pt article class, anonymous front matter, abstract count,
  eight sections, no appendix, and final References;
- every Part A and Part B theorem assumption and conclusion;
- scheme sanity, singleton lemma, scalar split, \(2m\) integral independence,
  future-character generation, disconnected components, no-gcd bookkeeping,
  saturated equality family, and sharp clock;
- every trivial-middle/root-copy, linear, monomial, multisupport, binomial
  \(A/B/C\), adjacent-word, resonance, uniqueness, and \(V_3^0\) closure
  step;
- the arbitrary-characteristic-zero, finite-rank, division-hull, and
  infinite-torsion Laurent bridge;
- every sharp scalar orientation and geometric/arithmetic separation;
- exactly three proof tables and zero figures or assets;
- all fifteen public anti-claims and exactly one predecessor paragraph in
  Section 8;
- exact equality of the eight citation-key sets and Laurent as the sole proof
  input;
- static pdfTeX compatibility, deterministic source controls, anonymity, and
  absence of drafting markers.

If any item fails, the reviewer writes nothing. A repair requires a separate
explicit instruction and a fresh full review at the same path. Only an
all-pass reviewer may create the file, binding both exact source hashes and
bytes, and its last nonempty line is exactly:

**MANUSCRIPT_SOURCE_PASS**

That pass alone does not authorize compilation. Round 0 additionally requires
a separate explicit build GO.

## Frozen deterministic toolchain and environment

No build is performed at this stage. A future authorized builder must use the
following invocation paths and resolved executable identities. A path,
resolved target, or SHA-256 mismatch is a blocker and authorizes no build.

| Purpose | Invocation path | Resolved target | Executable SHA-256 | Frozen version lead |
|---|---|---|---|---|
| pdfLaTeX | /usr/bin/pdflatex | /usr/bin/pdftex | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 | pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian) |
| BibTeX | /usr/bin/bibtex | /usr/bin/bibtex.original | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f | BibTeX 0.99d (TeX Live 2022/dev/Debian) |
| PDF metadata/pages | /usr/bin/pdfinfo | /usr/bin/pdfinfo | 8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e | pdfinfo version 22.02.0 |
| PDF text | /usr/bin/pdftotext | /usr/bin/pdftotext | 7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d | pdftotext version 22.02.0 |
| PDF fonts | /usr/bin/pdffonts | /usr/bin/pdffonts | 257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e | pdffonts version 22.02.0 |
| PDF images | /usr/bin/pdfimages | /usr/bin/pdfimages | cdac55daf2eaacbaf9f80cf8371e935c8686cb4fd7e84c42bba9706c1f10c87d | pdfimages version 22.02.0 |
| PDF attachments | /usr/bin/pdfdetach | /usr/bin/pdfdetach | e0c04f35fc5b0c4096199ff11d70e49db2b1952b4110f96f5f9ef0a3a4135b2d | pdfdetach version 22.02.0 |
| PDF signatures | /usr/bin/pdfsig | /usr/bin/pdfsig | 0c50615f466e45cc0309a68bdb8c4ad53778529ec77ab14e521e9c8d765eff09 | pdfsig version 22.02.0 |
| Strict static validation | /root/miniconda3/bin/python3.12 | /root/miniconda3/bin/python3.12 | 9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101 | Python 3.12.3 |
| MIME identity | /usr/bin/file | /usr/bin/file | ffa64f607f77d57cb3e2b650825868367a06eb91cdc5959c4e2f62ceb885b18a | file-5.41 |
| PDF token scan | /usr/bin/x86_64-linux-gnu-strings | /usr/bin/x86_64-linux-gnu-strings | 6ff5cfaddaf8dbc67614f535530465c890e83498509a6c8ffacc3798b6f1126f | GNU strings 2.38 |
| Hashing | /usr/bin/sha256sum | /usr/bin/sha256sum | 7645c8e76d75515ccb75c9086bdcf0d4071f2985f380f249253ead7d7c6810b3 | GNU coreutils 8.32 |
| Byte comparison | /usr/bin/cmp | /usr/bin/cmp | b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791 | GNU diffutils 3.8 |

Every complete version transcript, not only the displayed lead, is recorded in
the build receipt with its command, SHA-256, and byte count. Every
non-raster validation executable whose output enters the receipt is one of the
frozen tools above and is recorded likewise. The frozen Python interpreter may
run only nonpersistent governance-validation snippets; each snippet's literal
source, SHA-256, bytes, command, and output transcript identity must be in the
receipt. It may not run scientific calculations.

Every build command uses exactly:

    TZ=UTC
    LC_ALL=C
    LANG=C
    SOURCE_DATE_EPOCH=1786924800
    FORCE_SOURCE_DATE=1

No extra environment variable may alter TeX, bibliography, locale, clock,
metadata, path lookup, or source discovery. Absolute frozen invocation paths
are used; PATH does not select an executable.

## Round-0 isolated deterministic build

Round 0 begins only after stable exact \(U_{S21}\), an exact
MANUSCRIPT_SOURCE_PASS, absence of every later path, and a separate explicit
build GO.

Create exactly two distinct, new, empty, builder-owned, non-symlink temporary
directories from the literal template

/tmp/p17-paper17-r0-XXXXXXXX

Each resolved path must match

^/tmp/p17-paper17-r0-[A-Za-z0-9]{8}$

and have resolved parent /tmp. The two suffixes differ. Reuse, a preexisting
entry, any symlink, or any other path is a blocker. Copy into each root only
the exact bytes of paper/main.tex and paper/references.bib.

In each root run exactly, in order:

    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/bibtex main
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex

All eight exit codes must be zero. For each command capture exact combined
stdout/stderr bytes without adding a root label, timestamp, or wrapper prefix.
Within the round, run A and run B must have byte-identical:

- main.pdf;
- main.bbl;
- the final main.log;
- each corresponding command transcript and the combined four-command
  transcript.

Identity means equal SHA-256, bytes, and byte-for-byte comparison. A mismatch
fails the round; selecting one output is forbidden.

The only allowed temporary-root entries are regular non-symlink files named:

- main.tex;
- references.bib;
- main.aux;
- main.bbl;
- main.blg;
- main.log;
- optional main.out;
- optional main.toc;
- main.pdf.

There is no shell escape, network access, package installation, rasterization,
source edit, CAS, scientific execution, undeclared project read, or project
intermediate.

## Non-raster source and PDF validation

Both clean runs pass the same checks before persistence.

1. All TeX and BibTeX exit codes are zero. Final logs contain zero TeX,
   LaTeX, package, or BibTeX errors; zero warnings of any kind; zero undefined
   references or citations; zero multiply defined labels; zero missing
   characters or glyphs; zero missing fonts; and zero overfull or underfull
   boxes. The warning gate is literal zero, not a discretionary waiver.

2. Sources and extracted text contain zero TODO, FIXME, XXX, VERIFY,
   placeholder, draft, repair, governance, review-verdict, local-path, hash,
   paper-number, agent, identity, grant, acknowledgment, submission,
   repository, or operational markers.

3. The title is exact. The abstract has 180--220 words under the locked robust
   counter. There are exactly Sections 1--8 in the locked order, no appendix,
   a forced clear page, and final References.

4. There are 20--23 substantive pages through the end of Section 8, exactly
   one final References page, and 21--24 total pages. Every page has
   non-whitespace extracted public mathematical or bibliographic text.

5. There are exactly three table environments in the locked locations, no
   other table, no figure environment, no includegraphics command, and no
   external asset.

6. The citation keys used by main.tex, entry keys in references.bib, and
   bibitem keys in main.bbl have exact eight-key set equality with the locked
   set. There is no wildcard nocite, duplicate, missing, or uncited key.

7. The font count is discovered from each actual PDF and recorded as an
   integer; it is not guessed or frozen in advance. Every discovered font is
   embedded, subset, and has a Unicode map. The two runs have identical font
   tables.

8. The PDF contains zero image XObjects, attachments, embedded files,
   AcroForm, XFA, JavaScript or JS action, Launch action, RichMedia,
   FileAttachment annotation, signature, or external-file action. It has no
   trailer ID. The PDF structure and all inflated Flate streams are included
   in the frozen-tool token audit; raw-byte searching alone is insufficient.

9. PDF metadata is anonymous and contains no author identity, subject,
   keywords, creation or modification date, submission identifier, local
   path, or identity-bearing timestamp. The only permitted creator/producer
   value is generic and identity-free, and its exact value is recorded.

10. Extracted text contains every theorem assumption, the complete proof
    bridges, all examples and scalar orientations, all fifteen anti-claims,
    exactly one predecessor paragraph in Section 8, and no predecessor
    paragraph elsewhere. It contains zero empirical claim.

The validation receipt records exact commands, snippet sources, exit codes,
stdout/stderr transcript identities, counts, set comparisons, and booleans.
No visual or raster inspection is part of the build gate.

## Persistence, canonical receipt, and safe cleanup

Only after both clean runs and every validation pass may Round 0 persist:

- paper/main_round0.pdf;
- paper/BUILD_RECEIPT_R0.json.

The PDF is the exact byte copy common to both runs. No paper/main.pdf,
auxiliary, log, transcript, cache, temporary path, or other project artifact
may persist.

The receipt is strict compact canonical JSON: UTF-8; object keys recursively
sorted by Unicode code point; compact comma/colon separators; no duplicate
key, nonfinite number, BOM, carriage return, or insignificant whitespace; and
exactly one terminal LF. Its own SHA-256 and byte count are excluded. It
binds:

- the publication scope and lock, publication review, both public sources,
  and formal source review;
- exact prebuild and postbuild source identities;
- both roots, regex, ownership, distinctness, initial emptiness, and
  non-symlink checks;
- every frozen executable path, resolved target, hash, complete version
  transcript, and validation snippet;
- exact environment, commands, eight exits, and every command transcript;
- per-run PDF, BBL, final-log, and combined-transcript identities;
- all within-round byte-identity results;
- every log, source, text, page, nonempty-page, abstract, section, table,
  citation, proof-content, anti-claim, font, image, attachment, action,
  metadata, trailer, identity, and external-access check;
- the discovered font count and complete font table;
- persisted PDF identity;
- exact prewrite and postwrite universes; and
- explicit cleanup operations and verified root absences.

After all facts have been captured, validate each resolved root again and its
exact regular-file allowlist. Unlink every allowed file individually by an
explicit resolved path, then remove the now-empty root with rmdir. Recursive
deletion, globs, unresolved variables, symlink traversal, broad directory
targets, and deletion outside the two validated roots are forbidden. Both
roots must be verified absent before the builder stop. A validation failure
authorizes no persistence. A cleanup failure after persistence is reported as
a blocker without creating another project file.

## Round-1 review, sole bounded revision, rebuild, and Round-2 review

After a stable exact \(U_{R0}\) builder stop, a fresh reviewer may write only
notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md. A precondition mismatch has
disposition WRITE NOTHING. The reviewer rehashes the complete chain and
independently audits the receipt, PDF, sources, every theorem and proof
transition, examples, citation roles, page boundaries, nonempty pages, three
tables, fifteen anti-claims, unique predecessor paragraph, fonts, metadata,
security, warnings, anonymity, and layout without rasterization.

The final disposition is exactly one of:

- MANUSCRIPT_R1_PASS;
- MANUSCRIPT_R1_REPAIR_REQUIRED.

Each finding has a stable identifier, severity, exact source/PDF location,
required bounded repair, and theorem-scope impact. Neither disposition
authorizes finalization or release.

Exactly one bounded revision window follows. It includes a no-op. The revision
author may edit only paper/main.tex and paper/references.bib and must create
paper/SOURCE_REVISION_RECEIPT_R1.json. Every change maps to an R1 finding and
preserves theorem scope, proof dependencies, citation keys, page contract,
anonymity, and the unique predecessor paragraph. If R1 requires no repair,
both public sources remain byte-identical and the receipt records zero
changes. There is no second revision window.

The revision receipt is strict canonical JSON under the same rules, excludes
its own hash and bytes, and binds the R1 review, pre/post source identities,
an exact source-diff digest and bounded change ledger, or explicit no-op
identities, plus exact prewrite and postwrite universes.

Round 1 begins only after stable exact \(U_{S1}\). It repeats the entire
two-clean-build and validation protocol in two distinct roots from

/tmp/p17-paper17-r1-XXXXXXXX

matching

^/tmp/p17-paper17-r1-[A-Za-z0-9]{8}$.

It persists only paper/main_round1.pdf and
paper/BUILD_RECEIPT_R1.json. The R1 receipt additionally binds the R0 PDF and
receipt, R1 review, revision receipt, and authorized source diff. If the
revision was a no-op, the R1 PDF must be byte-identical to the R0 PDF. If it
was not a no-op, every difference must arise from the exact authorized source
diff. R0 artifacts remain unchanged.

After stable exact \(U_{R1}\), a fresh reviewer may write only
notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md. A precondition mismatch writes
nothing. The reviewer replays every R1 finding and repair and repeats the
complete theorem, proof, citation, page, PDF, anonymity, warning, public-text,
inventory, and cleanup audit. Its sole positive last nonempty line is:

**MANUSCRIPT_R2_PASS**

A failure creates no second revision authority.

Even an exact R2 pass leaves paper/main.pdf, finalization, camera-ready work,
identity disclosure, public release, repository publication, submission,
upload, venue communication, and every external message unauthorized. Each
would require a separate future lock and fresh independent review.

## Current inventory, future absences, and author stop

Immediately before these governance writes, the project contains exactly
\(U_{G15}\): 15 regular files, four directories excluding the root
(experiments, notes, paper, refine-logs), zero symlinks, and no other entry
type.

After the scope and canonical lock are written, the required universe is
exactly \(U_{L17}\): 17 regular files, the same four directories, zero
symlinks, and no other entry type.

At the publication-author stop, every future path in
\(U_{V2}\setminus U_{L17}\) is absent, as are:

- paper/main.pdf;
- paper/sections and paper/math_commands.tex;
- every appendix, supplement, style, class, figure, asset, code, data,
  result, build intermediate, cache, release, submission, upload, identity,
  and external-message artifact;
- every forbidden directory named build, code, data, figures, manuscript,
  output, release, results, source, or submission.

The canonical lock binds this scope by safe relative path, SHA-256, byte
count, and LF count. The lock binds itself only by safe path and authority
role; its own SHA-256 and byte count are excluded.

After writing and validating exactly these two governance artifacts, the
author rehashes every frozen input, verifies strict canonical round-trip,
duplicate-key and nonfinite rejection, verifies exact \(U_{L17}\), verifies
all future absences, reports both governance identities, and stops. No
reviewer is triggered and no further project write is permitted in this
authoring turn.
