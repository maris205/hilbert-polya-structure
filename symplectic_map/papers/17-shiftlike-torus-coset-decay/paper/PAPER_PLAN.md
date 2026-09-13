# Paper Plan

## Article identity

**Title:** Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors and the Exact Zero-Constant Boundary

**Form:** a proof-first pure-mathematics article with eight numbered main sections, followed by an unnumbered reference list. There are no appendices.

**Primary audience:** researchers in arithmetic dynamics, algebraic dynamics, Diophantine geometry, and polynomial automorphisms who are comfortable with algebraic tori and character lattices but should not need prior knowledge of this recurrence.

**One-sentence contribution:** For sparse type-\(\nu\) shift-like recurrences, a nonzero constant anchor gives the sharp torus-coset dimension law \(\dim H\leq k-m\) and qualitative finiteness of \(T_k\), while deleting that anchor leaves exactly one nonlinear planar two-step resonance, supported on \(\{1,d\}\) with \(a=-\beta^2\), whose explicit coset \(C_d\) necessarily closes in \(V_3\).

The article is unified by one mechanism: the constant term is a fixed trivial character in each restricted recurrence. Part A shows that this anchor forces one independent loss of torus dimension per transition. Part B removes exactly that character and classifies all pairings that can replace it. Part A is the structural main theorem and remains dominant in theorem order, setup, notation, proof architecture, and conclusions; Part B is the exact boundary test, not an adjacent note.

The article is anonymous and public-safe. It contains no internal project names, file paths, hashes, lifecycle terminology, or priority claim.

## Abstract draft

We study finite multiplicative windows for type-\(\nu\) shift-like recurrences. Let \(V_m\) be the torus variety encoding \(m\) successive recurrence equations. When the defining polynomial has a nonzero constant term and at least two actual nonconstant monomials, we prove that every connected torus translate contained in \(V_m\) has dimension at most \(k-m\) for \(0\leq m\leq k\). The bound is attained by saturated subtori for an explicit coefficient family, and its terminal case, combined with Laurent's torus theorem, yields finiteness of \(T_k\) for every finite-rank subgroup over an arbitrary characteristic-zero field, including groups with infinite torsion. Rank-one examples show that \(T_{k-1}\) can remain infinite. We then remove the constant and determine the exact planar boundary. Linear support retains one-dimensional cosets in every window. Among nonlinear supports, the only positive-dimensional two-step survivor occurs for \(P(X)=\beta X+\delta X^d\), \(d\geq2\), on the unique locus \(a=-\beta^2\); there it is the explicit coset \(C_d\), and no positive-dimensional coset survives a third step. Every other nonlinear support closes after two steps. The proofs use character independence, an integral pivot argument, and a complete local pairing calculus. We distinguish geometric coset existence from arithmetic infinitude and obtain qualitative, not effective, finiteness.

**Abstract control:** 192 words; target range 180--220 words. It states the problem, both main results, sharpness, the sole imported theorem, proof mechanisms, and the qualitative scope without citations or history.

## Exact theorem package

### Common setup

Let \(\Omega\) be an algebraically closed field of characteristic zero. Fix
\[
 k\geq2,\qquad 1\leq\nu\leq k-1,\qquad a\in\Omega^\ast,
\]
and define
\[
 S(z_1,\ldots,z_k)
   =(z_2,\ldots,z_k,P(z_{k-\nu+1})+az_1).
\]
The zero-based scalar recurrence is
\[
 x_{n+k}=P(x_{n+k-\nu})+a x_n. \tag{R}
\]
For \(m\geq0\), define \(V_m\subset\mathbb G_m^{k+m}\), with coordinates
\(x_0,\ldots,x_{k+m-1}\), by the \(m\) equations (R) for \(0\leq n<m\).
For a characteristic-zero field \(K\), coefficients defined over \(K\), and
a finite-rank subgroup \(\Gamma\leq K^\ast\), define
\[
 T_m(S,\Gamma)
  =\{z\in\Gamma^k:S^j(z)\in\Gamma^k\text{ for }0\leq j\leq m\}.
\]
Thus \(m\) counts transitions, while the condition contains \(m+1\) states.
Projection to the first \(k\) scalar coordinates is a bijection
\[
 V_m\cap\Gamma^{k+m}\longrightarrow T_m(S,\Gamma).
\]

The setup section must also verify that \(S\) is a polynomial automorphism:
if \(w=S(z)\), then
\[
 z_1=a^{-1}\bigl(w_k-P(w_{k-\nu})\bigr),\qquad
 z_i=w_{i-1}\quad(2\leq i\leq k).
\]
Each \(V_m\) is a closed subvariety of the ambient torus. Successive
elimination of the monic future coordinates identifies its coordinate ring
with an iterated localization of a Laurent polynomial domain in the initial
coordinates. This one-paragraph scheme sanity check establishes integrality
and prevents any set-theoretic ambiguity later.

### Part A theorem: anchored decay, equality, and arithmetic sharpness

Assume that
\[
 P(X)=c+\sum_{j=1}^{s}b_jX^{e_j}
\]
is in collected form, where
\[
 0<e_1<\cdots<e_s,\qquad a,c,b_1,\ldots,b_s\neq0,\qquad s\geq2.
\]
For every \(0\leq m\leq k\) and every translate \(\xi H\subset V_m\) of a
connected subtorus \(H\leq\mathbb G_m^{k+m}\),
\[
 \dim H\leq k-m. \tag{A}
\]
The statement has no condition on \(\gcd(k,\nu)\). If a diagonalizable
subgroup is disconnected, every component is a translate of its identity
component, so the same bound holds for its dimension.

If \(a=1\) and \(P(1)=0\), equality in (A) is attained for every
\(0\leq m\leq k\). Put
\[
 R_m=\{\,n-\nu\bmod k:0\leq n<m\,\}.
\]
The sharp subtorus \(H_m\) is defined by
\[
 x_r=1\quad(r\in R_m),\qquad x_{k+n}=x_n\quad(0\leq n<m).
\]
It is connected, saturated, contained in \(V_m\), and isomorphic to
\(\mathbb G_m^{k-m}\). This is a sufficient equality family, not a
classification or a necessary coefficient condition.

For every characteristic-zero field \(K\) and every finite-rank
\(\Gamma\leq K^\ast\), with arbitrary torsion,
\[
 T_k(S,\Gamma)\ \text{is finite}. \tag{A-fin}
\]
The window is sharp as a uniform qualitative threshold. For any prescribed
exponents \(e_1<\cdots<e_s\), take \(a=b_1=\cdots=b_s=1\), \(c=-s\), and
\(\Gamma=\langle2\rangle\). At \(m=k-1\), the unique free initial residue is
\(q=k-1-\nu\); setting \(x_q=2^N\), all other initial coordinates to \(1\),
and future coordinates by \(x_{k+n}=x_n\) gives infinitely many points of
\(T_{k-1}\). This is an existence result for compatible coefficients and a
compatible rank-one group.

### Part B theorem: the exact planar zero-anchor boundary

Fix \(k=2\), \(\nu=1\), and
\[
 P(X)=\sum_{e\in E}b_eX^e,\qquad
 \varnothing\neq E\subset\mathbb Z_{\geq1},
\]
with \(E\) the finite actual support and every \(b_e\neq0\). Write \(V_m^0\)
for the corresponding zero-constant survivor variety.

1. If \(E=\{1\}\), so \(P(X)=\beta X\), every \(V_m^0\) contains a
   one-dimensional torus translate. For any root
   \(r^2=\beta r+a\), it is
   \[
   \{(t,rt,\ldots,r^{m+1}t):t\in\mathbb G_m\}.
   \]
   Hence there is no finite geometric closing window in the linear class.
2. If \(E=\{1,d\}\), \(d\geq2\), and
   \(P(X)=\beta X+\delta X^d\), then \(V_2^0\) contains a
   positive-dimensional connected torus translate if and only if
   \[
   a=-\beta^2.
   \]
   On this locus the unique positive-dimensional translate is
   \[
   C_d=
   \left\{\left(\frac{\delta}{\beta^2}t^d,\ t,\ \beta t,\
   \delta\beta^dt^d\right):t\in\mathbb G_m\right\}. \tag{C}
   \]
   For all coefficients, including this resonance, \(V_3^0\) contains no
   positive-dimensional torus translate.
3. For every other nonlinear actual support, \(V_2^0\) contains no
   positive-dimensional torus translate. This includes nonlinear monomials,
   binomials whose lower exponent is at least two, and supports of size at
   least three.

Consequently, for every finite-rank \(\Gamma\leq K^\ast\) over every
characteristic-zero field and every nonlinear actual support, \(T_2\) is
finite unless \(E=\{1,d\}\) and \(a=-\beta^2\); on that resonant class,
\(T_3\) is finite. Linear support \(E=\{1\}\) is excluded from this finiteness
statement and can have infinite \(T_m\) at every window for compatible data.
The coset \(C_d\) is a geometric statement and need not meet every fixed
\(\Gamma\) infinitely. A compatible rank-one sharp example is
\(\beta=\delta=1\), \(a=-1\),
\(\Gamma=\langle2\rangle\), with
\[
 (x_0,x_1,x_2,x_3)=(t^d,t,t,t^d),\qquad t=2^N.
\]

## Eight-section architecture

The following are the only numbered main sections in the article. Each section
opens with its mathematical job, presents definitions before use, and ends by
handing a specific unresolved point to the next section.

### 1. Introduction and the anchor-loss question — 1.75 pages

**Job.** Pose the finite-window problem through \(V_m\), not through a single
orbit, and explain why deleting the constant term is the decisive structural
test.

**Content order.**

1. Open with recurrence (R), the idea of a multiplicative survivor window, and
   the distinction between a geometric torus translate in \(V_m\) and the
   arithmetic set \(T_m\).
2. State the anchored dimension law, equality family, \(T_k\) finiteness, and
   rank-one \(T_{k-1}\) sharpness in compact theorem-preview form.
3. State the planar zero-anchor phase: linear persistence, the unique
   \(\{1,d\}\), \(a=-\beta^2\) two-step resonance, and \(V_3\) closure.
4. Explain the unity in two sentences: the constant supplies a fixed character
   that forces Part A; Part B classifies the exact pairing calculus after its
   deletion.
5. Give one restrained context paragraph. Use Bedford--Pambuccian for
   shift-like terminology and Bera or Bera--Verma for complex-dynamical
   context; contrast, without theorem borrowing, fixed-orbit subgroup and
   multiplicative-dependence directions represented by the verified current
   sources.
6. End with a roadmap that makes Part A the main arc and Part B its boundary
   classification.

**Explicit scope sentences.** Geometry and arithmetic have different
quantifiers; the claims are qualitative; no global priority follows from a
bounded literature search; and the elementary character-partition device is
not itself the novelty.

**Transition.** The introduction has stated windows informally; Section 2
fixes coordinates, schemes, and the sole Diophantine bridge precisely.

### 2. Shift-like recurrences, survivor varieties, and the Laurent bridge — 2.25 pages

**Job.** Make every field, index, projection, and arithmetic quantifier
unambiguous before any character argument.

**Subsections and proof flow.**

- Define \(\Omega,k,\nu,a,P,S\), display the inverse of \(S\), and derive the
  zero-based recurrence. Include a one-line warning that \(m\) is the number
  of transitions, not the number of retained states.
- Define \(V_m\subset\mathbb G_m^{k+m}\) by exactly the equations
  \(0\leq n<m\). Prove closedness and integrality by successive monic
  elimination followed by localization at future-coordinate expressions.
- Define \(T_m(S,\Gamma)\) and prove the projection bijection
  \(V_m\cap\Gamma^{k+m}\simeq T_m\). This is also where the article makes clear
  that dimension is asserted for geometric subvarieties of \(V_m\), never for
  \(T_m\) itself.
- State Laurent's qualitative torus theorem in exactly the needed form: for a
  closed subvariety of a complex torus and the division group of a finitely
  generated subgroup, the intersection is contained in finitely many torus
  cosets lying in the subvariety. Deduce that absence of a
  positive-dimensional torus coset gives finiteness.
- Prove the finite-rank bridge internally. If
  \(\operatorname{rank}\Gamma=r<\infty\), choose
  \(\gamma_1,\ldots,\gamma_r\) lifting a basis of
  \(\Gamma\otimes_{\mathbb Z}\mathbb Q\) and put
  \(\Gamma_0=\langle\gamma_1,\ldots,\gamma_r\rangle\). For each
  \(\gamma\in\Gamma\), clear its rational relation and then kill the resulting
  torsion element by an element-dependent power, obtaining
  \(\gamma^N\in\Gamma_0\). Thus
  \(\Gamma\subset\Gamma_0^{\mathrm{div}}\), with no finite-generation or
  bounded-torsion assumption. Explicitly note that every root of unity lies
  in the division group of the identity.
- For arbitrary characteristic-zero \(K\), take the field generated over
  \(\mathbb Q\) by the finitely many coefficients and generators of
  \(\Gamma_0\), embed that finitely generated field in \(\mathbb C\), place
  all elements of \(\Gamma\) in a common algebraic closure using their power
  relations, and extend the embedding across that algebraic closure. Do not
  claim that all of \(K\) embeds in \(\mathbb C\). Apply the same argument to
  Cartesian powers.

**Imported result boundary.** Laurent is the only external proof theorem. Its
use is qualitative; it supplies neither a recurrence-specific count nor an
algorithm. All recurrence geometry and every window threshold are proved in
the article.

**Transition.** Laurent reduces arithmetic finiteness to exclusion of
positive-dimensional cosets; Section 3 develops the common character language
for that exclusion.

### 3. Characters on recurrence cosets — 2.00 pages

**Job.** Establish the reusable algebraic lemmas once, with enough detail to
support both the anchored proof and the zero-anchor partition calculus.

**Lemma sequence.**

1. **Restriction lemma.** On a translate \(\xi H\) of a connected subtorus,
   write each ambient coordinate as \(x_i=\xi_i\chi_i\), where
   \(\chi_i\in X^\ast(H)\). The restrictions of ambient characters generate
   \(X^\ast(H)\).
2. **Group-algebra singleton lemma.** Distinct characters form an
   \(\Omega\)-basis of \(\Omega[X^\ast(H)]\); hence a nonzero character term
   cannot occur as a singleton in an identity. State explicitly that this
   lemma is standard machinery, while the recurrence-specific relation and
   partition classifications are the new work.
3. **Connected-component lemma.** If a translate of a disconnected
   diagonalizable subgroup lies in \(V_m\), each component is a translate of
   the identity component, and dimension is unchanged. Thereafter all
   character lattices are torsion-free.
4. **Ambient lattice map.** Introduce
   \[
   \varphi:\mathbb Z^{k+m}\longrightarrow X^\ast(H),\qquad
   \varepsilon_i\longmapsto\chi_i,
   \]
   and record \(\dim H=\operatorname{rank}\operatorname{im}\varphi\).
5. **Local recurrence identity.** Restrict (R) to \(\xi H\) with all signs
   fixed:
   \[
   \xi_{n+k}\chi_{n+k}
   -a\xi_n\chi_n
   -P(\xi_{n+k-\nu}\chi_{n+k-\nu})=0.
   \]
   This displayed orientation is reused verbatim; scalar signs are never
   reconstructed from memory.

**Part A emphasis.** Close the section by isolating the anchored input:
\(1,\chi^{e_1},\ldots,\chi^{e_s}\) are at least three distinct characters
when \(\chi\neq1\), whereas there are only two endpoint terms. Part B will
later revisit the identity when the initial \(1\) is absent.

**Transition.** The anchored local identity now forces two lattice relations
per equation; Section 4 proves that all \(2m\) relations are integrally
independent.

### 4. Sharp anchored torus-coset decay — 4.00 pages

**Job.** State and prove the main geometric theorem
\(\dim H\leq k-m\) for every \(0\leq m\leq k\), including all scalar branches,
future-coordinate bookkeeping, endpoints, and disconnected components.

**Theorem-first layout.** Open with the full Part A dimension theorem, including
algebraic closure, collected actual support, nonzero coefficient assumptions,
the window range, and the connected/disconnected formulation.

**Proof spine.**

1. For the \(n\)-th equation put \(t=k+n-\nu\). If \(\chi_t\neq1\), then
   \(1,\chi_t^{e_1},\ldots,\chi_t^{e_s}\) are \(s+1\geq3\) distinct
   characters, while the lag and output endpoints can match at most two of
   them. A nonzero singleton remains, contradiction. Hence \(\chi_t=1\).
2. After this middle-character collapse, split without genericity:
   - if \(P(\xi_t)\neq0\), the nonzero constant character forces
     \(\chi_n=\chi_{n+k}=1\);
   - if \(P(\xi_t)=0\), the two endpoint terms force
     \(\chi_{n+k}=\chi_n\) and the scalar identity
     \(\xi_{n+k}=a\xi_n\).
   Both branches therefore give the kernel relations
   \[
   A_n=\varepsilon_{k+n-\nu},\qquad
   B_n=\varepsilon_{k+n}-\varepsilon_n.
   \]
3. Prove integral independence, not merely rational independence. The
   \(A_n\)-pivots form the interval
   \([k-\nu,k+m-1-\nu]\), whose span is \(m-1\leq k-1\). The supports
   \(\{n,k+n\}\) of the \(B_n\) are pairwise disjoint and separated by \(k\).
   Each pair has an endpoint outside the pivot interval, and that coordinate
   occurs in no other relation. In any integral dependence, its coefficient
   first kills the corresponding \(B_n\); the distinct pivots then kill all
   \(A_n\).
4. Since \(\varphi\) is surjective and
   \(\operatorname{rank}\ker\varphi\geq2m\),
   \[
   \dim H\leq(k+m)-2m=k-m.
   \]
5. Expose future-character generation before reducing indices. The relation
   \(B_j\) gives \(\chi_{k+j}=\chi_j\). Thus an active future middle
   \(\chi_{k+n-\nu}\), when \(n\geq\nu\), copies the initial character
   \(\chi_{n-\nu}\); when \(n<\nu\), it is already the initial character
   \(\chi_{k+n-\nu}\). The killed initial set is exactly
   \(R_m=\{n-\nu\bmod k:0\leq n<m\}\).
6. Explain the no-gcd point in full: \(R_m\) is the translation of an interval
   by \(-\nu\), not the orbit under repeated subtraction of \(\nu\).
   Translation is injective for \(m\leq k\), so no rotation cycle or
   \(\gcd(k,\nu)\) phase appears.
7. Check \(m=0\) and \(m=k\) explicitly. At \(m=k\), the pivot interval has
   span exactly \(k-1\), still too short to contain both endpoints of any
   \(B_n\).
8. End by passing from the identity component to every disconnected component.

**Manuscript Table 1: relation/pivot independence.** Give one compact row for
each relation family, listing indices, support, pivot/outside coordinate,
independence role, and the endpoint checks \(m=0,k\). The prose proof remains
complete; the table is a verification aid, not a substitute.

**Transition.** Section 4 gives the upper bound. Section 5 constructs saturated
equality subtori, reads the exact residue clock, and converts the terminal
geometric statement into sharp arithmetic windows.

### 5. Equality subtori and the sharp arithmetic clock — 2.00 pages

**Job.** Prove attainment, saturation, \(T_k\) finiteness, and rank-one
\(T_{k-1}\) sharpness without suggesting a classification of all equality
cases.

**Proof flow.**

1. Under the sufficient assumptions \(a=1\) and \(P(1)=0\), define \(H_m\) by
   \(x_r=1\) for \(r\in R_m\) and \(x_{k+n}=x_n\) for \(0\leq n<m\).
2. Verify \(H_m\subset V_m\) equation by equation. Every active middle
   coordinate equals \(1\), so \(P\) vanishes there, and the future coordinate
   copies the lag.
3. Prove connectedness and saturation on the integral character lattice.
   Eliminating every forced initial coordinate and every future coordinate
   leaves the free initial coordinates as a basis for a quotient
   \(\mathbb Z^{k-m}\). The quotient is free, so the defining lattice is a
   direct summand and \(H_m\simeq\mathbb G_m^{k-m}\).
4. At \(m=k\), combine the zero-dimensional coset result with the Laurent
   bridge from Section 2 to prove qualitative finiteness of \(T_k\), and note
   that every later survivor set is a subset of \(T_k\).
5. For prescribed support, choose \(a=b_j=1,c=-s\). At \(m=k-1\),
   \(R_{k-1}\) omits exactly \(q=k-1-\nu\). Vary \(x_q=2^N\) in
   \(\Gamma=\langle2\rangle\), keep all other initial coordinates equal to
   \(1\), and copy future coordinates. This proves infinite \(T_{k-1}\).
6. State the quantifiers next to the example: equality is attained by this
   family, not necessarily only by this family; rank-one infinitude is for a
   compatible coefficient/group choice, not every group.

**Part A dominance checkpoint.** By the end of Section 5, the article has
completed the all-dimensional theorem, its exact equality mechanism, the
arbitrary-field finite-rank corollary, and sharpness. The zero-anchor analysis
that follows is framed as the deletion test for the constant character used
above.

**Transition.** Removing \(c\) destroys the anchored singleton. Section 6
classifies the replacement pairings locally in the planar recurrence.

### 6. Zero-anchor local partition calculus — 3.50 pages

**Job.** Fix \(k=2,\nu=1,c=0\) and exhaust every local character partition for
linear, monomial, multisupport, and binomial polynomials before composing
successive equations.

**Opening normalization.** Write
\[
 x_{n+2}=P(x_{n+1})+a x_n,\qquad
 P(X)=\sum_{e\in E}b_eX^e,
\]
with \(E\) the collected actual support. Use additive notation
\(u_i\in X^\ast(H)\) for coordinate characters.

**Case calculus.**

1. **Trivial middle character.** If \(u_{n+1}=0\), preserve both scalar
   branches. When \(P(\xi_{n+1})\neq0\), both endpoint characters are zero.
   When \(P(\xi_{n+1})=0\), the endpoints copy:
   \(u_{n+2}=u_n\) and \(\xi_{n+2}=a\xi_n\). Call the combined local type
   \(A\); never collapse root-copy into the nonroot branch.
2. **Linear support.** For \(P(X)=\beta X\), directly substitute
   \((t,rt,\ldots,r^{m+1}t)\) with \(r^2=\beta r+a\). This proves geometric
   persistence for every finite window before the nonlinear classification.
   For the compatible arithmetic data
   \(\beta=2,a=-1,r=1,\Gamma=\langle2\rangle\), taking \(t=2^N\) gives
   \((t,\ldots,t)\) in every window, and hence infinitely many \(T_m\) points
   for every \(m\).
3. **Nonlinear monomial.** For \(P(X)=bX^d\), \(d\geq2\), a trivial first
   middle character is in the nonroot branch because
   \(P(\xi_1)=b\xi_1^d\neq0\), so it kills both endpoints immediately. If the
   first middle character is nontrivial, avoiding a singleton forces
   \(u_0=u_2=du_1\); the second middle character is then nontrivial and the
   next equation forces \(u_1=du_2=d^2u_1\). Hence \(u_1=0\) in the
   torsion-free lattice, a contradiction, and \(V_2^0\) has no
   positive-dimensional translate. Include the correctly oriented one-step
   arithmetic example
   \[
   P(X)=X^e,\quad a=1,\quad \Gamma=\langle2\rangle,\quad t=2^N,\quad
   (x_0,x_1,x_2)=(t^e,t,2t^e);
   \]
   do not transpose the first two coordinates.
4. **At least three powers.** If \(|E|\geq3\) and the middle character is
   nonzero, at least one distinct power remains a singleton after the two
   endpoints are used. Hence the middle is trivial. The nonroot branch kills
   the endpoints immediately; a root-copy branch is closed by the next
   equation. As a one-step sharp illustration for any prescribed actual
   support size \(s\geq2\), choose distinct positive exponents
   \(e_1<\cdots<e_s\), take the nonzero rational coefficients
   \(b_1=\cdots=b_{s-1}=1\), \(b_s=-(s-1)\), and set
   \(a=1,\Gamma=\langle2\rangle,t=2^N\). Then \(P(1)=0\) and
   \((x_0,x_1,x_2)=(t,1,t)\).
5. **Binomial support.** Let \(E=\{p,q\}\), \(1\leq p<q\). With nontrivial
   middle character \(u\), endpoint-endpoint pairing would leave both middle
   powers singleton. Thus each endpoint must pair with a different power.
   There are exactly two orientations, \(B\) and \(C\), in addition to \(A\).

**Manuscript Table 2: \(A/B/C\) label definitions and scalars.** The table has
exactly these entries:

- \(A\): \(u_{n+1}=0\); either nonroot killing, or root-copy
  \(u_{n+2}=u_n\), \(\xi_{n+2}=a\xi_n\).
- \(B\): \(u_n=pu,\ u_{n+2}=qu\), with
  \(a\xi_n=-b_p\xi_{n+1}^{p}\) and
  \(\xi_{n+2}=b_q\xi_{n+1}^{q}\).
- \(C\): \(u_n=qu,\ u_{n+2}=pu\), with
  \(a\xi_n=-b_q\xi_{n+1}^{q}\) and
  \(\xi_{n+2}=b_p\xi_{n+1}^{p}\).

The prose immediately before the table proves exhaustiveness; the table fixes
the names and scalar signs for all later compositions.

**Transition.** The local list is complete. Section 7 composes adjacent labels,
derives the sole resonance rather than guessing it, and proves third-step
closure.

### 7. The exact zero-constant phase and third-step closure — 4.00 pages

**Job.** State and prove the full Part B phase theorem, including all adjacent
words, the unique scalar locus, the exact coset, \(V_3\) closure, arithmetic
corollaries, and geometry-versus-group quantifiers.

**Theorem-first layout.** State the three-part zero-anchor theorem exactly as
in the theorem package: linear persistence; the unique nonlinear
\(\{1,d\}\), \(a=-\beta^2\) exception with \(C_d\); and two-step closure for
every other nonlinear support.

**Adjacent-word proof.**

1. Compose all words containing \(A\). The words \(AA\), \(AB\), \(AC\),
   \(BA\), and \(CA\) all force the relevant character to zero, including the
   root-copy subcase.
2. For two nontrivial labels, calculate in the fixed orientation:
   \[
   BB:\ u_1=pq\,u_1,\qquad
   BC:\ u_1=q^2u_1,\qquad
   CB:\ u_1=p^2u_1,\qquad
   CC:\ u_1=pq\,u_1.
   \]
   Since \(q\geq2\), only \(CB\) can survive, and only when \(p=1\).
3. Put \(q=d\). The surviving character vector is
   \[
   (u_0,u_1,u_2,u_3)=(du,u,u,du).
   \]
   Apply the scalar equations in their recorded orientations:
   \[
   a\xi_0=-\delta\xi_1^d,\qquad
   \xi_2=\beta\xi_1,\qquad
   a\xi_1=-\beta\xi_2,\qquad
   \xi_3=\delta\xi_2^d.
   \]
   The middle two identities force exactly \(a=-\beta^2\), and the others
   yield formula (C).
4. Prove uniqueness, not just containment. The ambient coordinate characters
   generate \(X^\ast(H)\), and all four are multiples of \(u=u_1\); because
   \(u\) itself occurs, the character lattice is \(\mathbb Zu\). Thus the
   positive-dimensional translate is one-dimensional and equals the displayed
   \(C_d\). Verify (C) by direct substitution into both recurrence equations.
5. Close a third equation. Starting from \((du,u,u,du)\), continuation by
   \(A\) forces \(du=0\), by \(B\) forces \((d-1)u=0\), and by \(C\) forces
   \((d^2-1)u=0\). Since \(d\geq2\), all give \(u=0\). If the first four
   characters were already zero, the third recurrence forces the fifth zero
   as well. Therefore \(V_3^0\) has no positive-dimensional translate on the
   resonance.

**Manuscript Table 3: adjacent-word transition and closure matrix.** Combine
the five \(A\)-containing words, the four \(B/C\) words, and the three possible
continuations of the surviving \(CB\) word in one matrix. Columns are word,
character equation, scalar condition if relevant, and outcome. This single
matrix is the verification checksum for completeness; there is no separate
support-classification table.

**Arithmetic close.** Apply Section 2: for every nonlinear support other than
the resonant \(\{1,d\}\) class, \(T_2\) is finite for every finite-rank group;
on the resonant \(\{1,d\}\) class, \(T_3\) is finite. Linear support
\(E=\{1\}\) is excluded and, for the compatible data in Section 6, has
infinite \(T_m\) for every \(m\). Then separate three statements explicitly:

- \(C_d\) exists geometrically for every coefficient choice on the locus;
- it does not follow that \(C_d\cap\Gamma^4\) is infinite for every fixed
  \(\Gamma\);
- \(\beta=\delta=1,a=-1,\Gamma=\langle2\rangle\) is a compatible example with
  infinitely many \(T_2\) points \((t^d,t,t,t^d)\).

The linear class is likewise described first geometrically; any arithmetic
infinitude statement requires compatible coefficients and group elements.

**Transition.** The exact phase is now closed. Section 8 records assumption
failures, the non-improvement boundary, and the limits of what the proof
licenses.

### 8. Assumption boundaries, contextual separation, and conclusion — 2.50 pages

**Job.** Make every non-extension explicit, distinguish nearby problem
quantifiers, give the sole public comparison disclosure, and end with the
anchor-loss principle rather than speculative applications.

**Assumption audit.**

- Characteristic zero is used by the Laurent bridge; no positive-characteristic
  extension is asserted.
- The condition \(a\neq0\) is essential to the shift-like automorphism and to
  the two-endpoint relation pattern; \(a=0\) is outside the theorem.
- The anchored theorem requires a nonzero constant and at least two actual
  nonconstant monomials. The constant-zero and support-one failures of its
  singleton count are handled only where explicitly classified.
- Polynomial support is finite, collected, and positive-exponent. Negative
  Laurent exponents, rational maps, pole divisors, and arbitrary polynomial
  automorphisms are not covered.
- Actual support depends on the chosen coordinate expression; no
  affine-conjugacy invariance is claimed.
- The bound is proved only for \(0\leq m\leq k\); later arithmetic finiteness
  follows by nesting after \(T_k\), not by extending \(k-m\) to negative
  dimensions.
- Equality examples establish sharpness but do not classify every maximal
  coset or every equality coefficient locus.
- No height bound, periodic-point classification, effective enumeration, or
  cardinality estimate is derived.

**Nearby-work separation.** In compact prose, distinguish a whole finite
window varying over initial points from a fixed orbit meeting a subgroup, and
distinguish exact torus-coset containment from complex-analytic shift-like
dynamics or linear reachability. Cite only the verified contextual primary
sources and assign none of them responsibility for the new recurrence
lemmas.

**The sole public boundary disclosure appears here, once, as one paragraph:**

> An earlier companion treatment established stronger explicit bounds for the planar nonzero-constant problem and subsumed its own support-one precursor. The present article neither reproduces nor improves those planar estimates; its contribution is the all-dimensional torus-coset decay profile and the exact zero-constant boundary.

No other section discusses this comparison. The paragraph is anonymous,
contains no internal identifiers, and cleanly removes the dominated planar
specialization from the novelty claim.

**Conclusion.** Return to the single mechanism: a fixed constant character
creates \(2m\) independent lattice relations, while its deletion reduces the
planar nonlinear problem to a complete two-orientation calculus with one
resonant word and forced third-step closure. End after the proved qualitative
phase; do not add conjectures merely to lengthen the article.

**After Section 8:** an unnumbered reference list containing only works
actually cited. References are outside the substantive-page count. There is no
appendix.

## Section-level theorem and proof flow

This is an editorial dependency map, not a manuscript figure:
\[
\begin{aligned}
\text{exact recurrence and }V_m
&\longrightarrow \text{projection to }T_m
\longrightarrow \text{Laurent reduction},\\
\text{group-algebra singleton}
&\longrightarrow
\begin{cases}
\text{constant anchor}\to A_n,B_n\to 2m\text{ pivots}\to k-m,\\
\text{zero anchor}\to A/B/C\text{ labels}\to CB\to a=-\beta^2,
\end{cases}\\
k-m\text{ at }m=k
&\longrightarrow T_k\text{ finite},\\
CB\text{ at two steps}
&\longrightarrow C_d\text{ and third-step closure}.
\end{aligned}
\]

The proof dependency order is strict:

1. Section 2 settles scheme and arithmetic translation.
2. Section 3 provides the only common algebraic machinery.
3. Sections 4--5 complete Part A before Part B begins.
4. Section 6 proves the local list; Section 7 alone may compose its labels.
5. Section 8 narrows claims and does not introduce a new theorem.

## Claims-evidence matrix

The matrix is an editorial control device and is not a fourth manuscript
table.

| Claim ID | Claim | Evidence required in main text | Location | External dependence |
|---|---|---|---|---|
| S1 | \(V_m\) is a well-defined integral torus subvariety and projects bijectively to \(T_m\) on \(\Gamma\)-points. | Exact equations, monic elimination/localization, state-window check. | Section 2 | None |
| S2 | Arbitrary finite-rank groups, including infinite torsion, reduce to Laurent's division-group scope over \(\mathbb C\). | \(\mathbb Q\)-basis lift, elementwise torsion killing, finitely generated field embedding, algebraic extension, Cartesian powers. | Section 2 | Laurent only after the bridge |
| A1 | Every connected coset in \(V_m\) has dimension at most \(k-m\), \(0\leq m\leq k\). | Singleton, full \(P(\xi)\) split, \(2m\) integral independence, rank count. | Section 4 | None |
| A2 | The result has no gcd condition and handles future middle coordinates. | Copy future characters first; identify \(R_m\) as a translated interval. | Section 4 | None |
| A3 | Disconnected subgroup translates obey the same dimension bound. | Identity-component decomposition and equal dimension. | Sections 3--4 | None |
| A4 | \(H_m\) attains equality when \(a=1,P(1)=0\). | Equationwise inclusion, free quotient lattice, saturation. | Section 5 | None |
| A5 | \(T_k\) is qualitatively finite for every permitted \(\Gamma\). | Zero-dimensional cosets plus Section 2 bridge. | Section 5 | Laurent |
| A6 | The window is sharp at \(k-1\). | \(a=b_j=1,c=-s\), free residue \(k-1-\nu\), \(\Gamma=\langle2\rangle\). | Section 5 | None |
| B1 | Linear support has a coset in every finite window. | Direct substitution of \(r^it\), \(r^2=\beta r+a\). | Section 6 | None |
| B2 | Nonlinear monomials and supports of size at least three close in \(V_2^0\). | Two-step monomial character equation; singleton plus root-copy closure. | Section 6 | None |
| B3 | \(A,B,C\) exhaust binomial local behavior. | Trivial-middle split; rule out endpoint pairing; record both orientations and scalars. | Section 6 | None |
| B4 | Only \(\{1,d\}\) with \(a=-\beta^2\) survives two steps. | Complete word matrix; \(CB\), \(p=1\); scalar composition. | Section 7 | None |
| B5 | The surviving subset is exactly \(C_d\), not a proper subcoset. | Ambient characters generate; \(X^\ast(H)=\mathbb Zu\); direct substitution. | Section 7 | None |
| B6 | Resonance closes in \(V_3^0\). | Exhaust \(A,B,C\) continuations and the all-trivial branch. | Section 7 | None |
| B7 | For nonlinear support, \(T_2\) is finite except on resonant \(\{1,d\}\), where \(T_3\) is finite; linear support is excluded and can remain infinite. | No positive-dimensional coset at the stated nonlinear window plus Section 2; compatible linear example. | Sections 6--7 | Laurent |
| Q1 | Geometric resonance and arithmetic infinitude have different quantifiers. | General locus, explicit compatible example, explicit non-universality sentence. | Sections 1 and 7 | None |
| L1 | All extension and comparison limits are visible. | Assumption audit, anti-claim sentences, sole comparison paragraph. | Section 8 and assigned earlier locations | Context citations only |

## Terminology and notation ledger

This ledger controls wording and indices; it is not intended as a manuscript
table.

| Item | Fixed meaning and usage |
|---|---|
| \(\Omega\) | Algebraically closed geometric ground field of characteristic zero. |
| \(K\) | Arbitrary characteristic-zero arithmetic ground field containing the coefficients and \(\Gamma\). |
| \(k,\nu\) | Dimension and shift type, with \(k\geq2\) and \(1\leq\nu\leq k-1\). |
| \(S\) | The one-based shift-like automorphism displayed in Section 2. |
| \(x_n\) | Zero-based scalar coordinate satisfying \(x_{n+k}=P(x_{n+k-\nu})+ax_n\). |
| \(m\) | Number of transitions/equations; the window contains states \(0,\ldots,m\). |
| \(V_m\) | Geometric survivor variety in \(\mathbb G_m^{k+m}\); dimension/coset language applies here. |
| \(T_m(S,\Gamma)\) | Arithmetic initial states in \(\Gamma^k\) surviving through state \(m\); never called positive-dimensional. |
| actual support | Exponents remaining after collecting like powers, all with nonzero coefficients. |
| \(\xi H\) | Translate of a connected subtorus unless a disconnected subgroup is explicitly reduced to \(H^\circ\). |
| \(\chi_i\), \(u_i\) | Multiplicative and additive notation for restricted coordinate characters. |
| \(A_n,B_n\) | Part A kernel relations; never confused with the Part B labels \(A,B,C\). Use subscripts for Part A. |
| \(R_m\) | Translated residue set \(\{n-\nu\bmod k:0\leq n<m\}\), never a rotation orbit. |
| \(H_m\) | The sufficient saturated equality subtorus for \(a=1,P(1)=0\). |
| \(V_m^0\) | Planar survivor variety for \(k=2,\nu=1,c=0\). |
| \(A,B,C\) | Part B local partition labels, defined once with scalars in Manuscript Table 2. |
| \(C_d\) | The unique positive-dimensional two-step resonant coset, with coordinate order \((x_0,x_1,x_2,x_3)\). |
| finite rank | \(\dim_{\mathbb Q}(\Gamma\otimes_{\mathbb Z}\mathbb Q)<\infty\); not synonymous with finite generation. |
| division group | Elements whose some positive power lies in the chosen finitely generated subgroup. |
| sharp | Existence of a compatible coefficient/group family at the preceding window, not universality for every \(\Gamma\). |

## Exact manuscript table and visual plan

The manuscript contains exactly three tables, all proof tables:

| Table | Section | Purpose | Nonduplication rule |
|---|---:|---|---|
| Table 1. Relation/pivot independence | 4 | Audit \(A_n,B_n\), pivot interval, outside endpoints, and endpoint windows. | Does not restate the theorem or equality family. |
| Table 2. \(A/B/C\) label definitions and scalars | 6 | Freeze both nontrivial orientations and all scalar signs, while retaining both \(A\) branches. | Does not compose adjacent words. |
| Table 3. Adjacent-word transition and closure matrix | 7 | Exhaust two-label words and the three continuations of \(CB\). | Absorbs the closure checklist; there is no fourth phase table. |

There are zero figures, zero graphical abstracts, and zero assets. A hero
figure would not clarify the proof: the decisive objects are exact integral
relations, scalar signs, and a finite transition list, all of which are more
verifiable in the three compact proof tables. A diagram would duplicate those
tables without representing data or adding a mathematical inference.

There are zero experiments, simulations, CAS runs, code listings, datasets,
or computational claims. None is needed: every universal statement has a
symbolic proof, and every sharp example is checked by direct substitution.

## Citation scaffold

Only sources in the verified ledger may appear. This scaffold is not a
bibliography and does not authorize creation of citation files.

| Source handle | Planned location | Permitted role | Prohibited role |
|---|---|---|---|
| Laurent (1984), journal article, DOI \(10.1007/\mathrm{BF01388597}\) | Sections 1, 2, 5, 7 | Sole imported qualitative torus/division-group theorem. | No effective bound; do not substitute the separate seminar record for theorem provenance. |
| Bedford--Pambuccian | Section 1 | Provenance and terminology for higher-dimensional shift-like maps. | No arithmetic survivor theorem attribution. |
| Bera; Bera--Verma | Section 1 or 8 | Complex-dynamical context for polynomial shift-like maps. | No torus-window claim. |
| Bell--Ghioca | Section 1 or 8 | Contrast with fixed-orbit subgroup intersections. | No finite-window support classification. |
| Ji--Xie--Zhang | Section 1 or 8 | Context for cyclotomic affine/Hénon rigidity. | No attribution of the present phase theorem. |
| Mello--Yasufuku | Section 1 or 8 | Contrast with semigroup-orbit multiplicative dependence and integrality questions. | No all-initial-state survivor theorem. |
| Karimov--Kelmendi--Ouaknine--Worrell | Section 1 or 8 | Linear reachability neighbor using torus-subvariety ideas. | No nonlinear shift-like collision claim. |
| Kaur | Section 1 or 8 | Current transcendental shift-like complex-dynamics context. | No arithmetic recurrence geometry claim. |

Citation discipline:

- Cite Laurent immediately after the exact imported statement and again only
  when invoking it for a finiteness corollary.
- Context sources support only map provenance or problem separation.
- Do not cite any source for the \(k-m\) law, \(H_m\), the \(A/B/C\) calculus,
  the resonance locus, \(C_d\), or \(V_3\) closure; these are internally
  proved claims.
- A bounded no-hit search supports cautious positioning, never a claim of
  global priority.
- The eventual unnumbered reference list contains only sources used in prose.

## Fifteen-claim scope firewall

Each item below must receive an explicit sentence at the assigned main-text
location; none may be protected merely by silence.

1. **Section 2:** Do not call \(T_m\) positive-dimensional; dimension belongs
   to subvarieties or torus translates in \(V_m\).
2. **Section 7:** Do not infer that resonance makes \(T_2\) infinite for every
   \(\Gamma\); infinitude is exhibited only for a compatible group.
3. **Section 5:** Do not present \(a=1,P(1)=0\) as necessary for equality; it
   is a sufficient sharp family.
4. **Section 4:** Do not impose or suggest a \(\gcd(k,\nu)\) condition.
5. **Section 4:** Do not describe the killed residues as the iterated orbit
   \(\{-j\nu\}\); they are the translated interval \(R_m\).
6. **Section 6:** Do not say nonlinear monomials have no finite closing
   window; prove their two-step closure.
7. **Sections 2 and 8:** Do not claim Laurent yields an effective bound,
   algorithm, or recurrence-specific cardinality.
8. **Sections 1 and 3:** Do not claim novelty for the standard
   character-partition or group-algebra singleton lemma by itself.
9. **Section 8:** Do not extend the theorem to positive characteristic,
   \(a=0\), rational or Laurent maps, or arbitrary polynomial automorphisms.
10. **Section 8:** Do not call actual support affine-conjugacy invariant.
11. **Section 2:** Do not equate finite rank with finite generation or bounded
    torsion; explicitly include arbitrary roots of unity in the division-hull
    bridge.
12. **Section 8:** Do not claim a new explicit planar anchored cardinality
    estimate or an improvement of such estimates.
13. **Sections 1 and 8:** Do not turn a bounded literature search into a global
    priority claim.
14. **Sections 5 and 8:** Do not claim a classification of all equality or
    maximal cosets in Part A.
15. **Section 8:** Do not claim consequences for heights, periodic-point
    classification, or effective enumeration.

## Page checksum and dominance audit

These are substantive content pages. The range is a credibility constraint,
not a quota; references are excluded.

| Main section | Pages | Cumulative |
|---|---:|---:|
| 1. Introduction and the anchor-loss question | 1.75 | 1.75 |
| 2. Shift-like recurrences, survivor varieties, and the Laurent bridge | 2.25 | 4.00 |
| 3. Characters on recurrence cosets | 2.00 | 6.00 |
| 4. Sharp anchored torus-coset decay | 4.00 | 10.00 |
| 5. Equality subtori and the sharp arithmetic clock | 2.00 | 12.00 |
| 6. Zero-anchor local partition calculus | 3.50 | 15.50 |
| 7. The exact zero-constant phase and third-step closure | 4.00 | 19.50 |
| 8. Assumption boundaries, contextual separation, and conclusion | 2.50 | 22.00 |
| **Total** | **22.00** | **22.00** |

The hard acceptable range is 19.5--22.5 substantive pages, with a target of
22.0. If a clean proof draft naturally lands inside that range, do not add
material to hit 22.0 exactly. If it exceeds 22.5, compress context and repeated
examples before compressing proof obligations. If it falls below 19.5, do not
pad: recheck whether a required proof branch, scalar orientation, field bridge,
or assumption audit was omitted.

Part A is dominant by dependency and exposition. Sections 2--5 comprise 10.25
pages of setup and proof built around the anchored theorem, in addition to its
first-position preview in Section 1. Part B receives 7.50 pages as the exact
deletion boundary. Section 8 contains limitations and conclusion rather than
a second independent narrative.

## Writing and anti-padding rules

- Lead with the theorem or lemma that a section proves; put historical context
  after the mathematical question, not before it.
- Preserve one-based map coordinates and zero-based scalar coordinates exactly.
  Reprint the signed local identity before the Part B scalar calculation.
- Use “actual support” only after collection and always record nonzero
  coefficients.
- Keep the \(P(\xi)\neq0\) and \(P(\xi)=0\) branches adjacent. Never hide the
  root-copy branch under “generic coefficients.”
- Prove integral independence with an explicit outside-coordinate argument.
  “By character count” is not an acceptable replacement.
- Introduce \(R_m\) only after future characters have been copied to initial
  characters; this prevents orientation and gcd drift.
- Define \(A/B/C\) once in Manuscript Table 2 and use the same direction in
  every word. The resonance sign must be derived from
  \(a\xi_1=-\beta\xi_2\) and \(\xi_2=\beta\xi_1\).
- Keep the corrected monomial tuple in the order
  \((x_0,x_1,x_2)=(t^e,t,2t^e)\).
- Every displayed equation must advance a proof or lock an orientation.
  Avoid decorative restatements of the recurrence.
- The three proof tables summarize arguments already present in prose; they
  never replace a proof. Add no comparison table, phase-summary table, or
  notation table to the manuscript.
- Use direct verbs and short theorem statements. Avoid “clearly,” “obviously,”
  and broad claims such as “fundamental” or “first.”
- Keep literature positioning bounded and factual. No priority language,
  citation dumping, or unsupported comparison.
- Do not add a hero figure, appendix, long example catalogue, speculative
  conjecture section, computational supplement, or generic background on
  algebraic groups.
- The abstract remains 180--220 words and contains no citation, author clue, or
  comparison history.
- References follow Section 8 and do not count toward substantive pages.

## Downstream fence

This plan authorizes no manuscript prose, bibliography file, TeX source, code,
scientific run, figure, asset, compilation, build, submission, or external
action. The only next action is a separately conducted independent review of
this plan. Any later drafting must be separately authorized after that review
and must preserve:

- the exact title and one-sentence unified contribution;
- the eight-section, no-appendix architecture and hard page range;
- all theorem hypotheses, scalar orientations, and arithmetic quantifiers;
- the Laurent finite-rank/division-hull/infinite-torsion bridge;
- exactly three manuscript proof tables and zero figures;
- all fifteen explicit anti-claims; and
- the single comparison disclosure in Section 8 only.

Until that review is complete, no further project file should be created or
modified.
