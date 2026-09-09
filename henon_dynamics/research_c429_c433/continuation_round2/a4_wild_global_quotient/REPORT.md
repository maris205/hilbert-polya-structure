# Round 2 A4 — global native-cycle quotient

2026-09-09 UTC. Author `/root/c429_a4_witt_local_data`. This contract is frozen before substantial new proof or mathematical execution. First-pass files are read-only. The repository batch, proof-writer and research-lit skills govern this bounded continuation.

## Frozen question

For every odd prime $p$ and every integer $e\geq1$, put $k=\overline{\mathbb F}_p$, $F=k(c)$, $n=p^e$ and $m=p^{e-1}$. For the native map $f_c(x)=x^2+c$, define

$$
\Phi_n(x,c)=\frac{f_c^{\circ n}(x)-x}{f_c^{\circ m}(x)-x},
\qquad A_n=F[x]/\Phi_n,
\qquad B_n=A_n^{\langle\sigma\rangle},\quad \sigma(x)=f_c(x).
$$

The generic algebra $A_n$ is finite étale with exact native period $n$ on geometric points; these are accepted first-pass inputs. The target of this lane is the **global quotient bottleneck**

$$
\boxed{B_n\text{ is a field for every odd }p\text{ and every }e\geq1.}
\tag{GQ}
$$

Equivalently, geometric parameter monodromy acts transitively on the native $n$-cycles. The quotient has rank $r_n=(2^n-2^m)/n$ over $F$. We must identify a genuine mechanism connecting these $r_n$ cycle sheets after reduction; full inertia inside one native cycle alone is not such a mechanism. A full proof of (GQ), an exact counterexample, or an explicit unclosed uniform lemma is the allowed outcome. A method-specific countermodel is not a counterexample to this quadratic family.

The full PC424-D component question remains distinct: combining (GQ) with full local $C_n$ inertia at a point above the native small cycle would force point transitivity. Neither half may be silently assumed from the other. One application of $f_c$ remains one native tick.

## Accepted input and exact compatibility to audit

Under the tame parameter substitution $c=(1-s^2)/4$, $x=z+(1+s)/2$, the map is $P_s(z)=(1+s)z+z^2$. The accepted small-cycle Hensel factor $M_e\equiv z^n\pmod s$ has exactly one geometric native $n$-cycle. LRL Theorem C owns existence/uniqueness of this small cycle and its slope. Its invariant algebra is one copy of $k((s))$; any full local $C_n$ inertia rotates this cycle but is trivial on its quotient sheet. This statement will be justified algebraically below, not promoted to global transitivity.

The candidate global bridge is a characteristic-zero primitive-branch monodromy graph together with a valid specialization theorem: enough noncolliding primitive branch inertia must remain transitive in characteristic $p$. The exact collision set at $n=p^e$ and uniform connectedness after deleting affected edges are the selected bottleneck. Characteristic-zero irreducibility, connected special fiber, or a single local branch is not an automatic substitute.

## Outcome

**NOT CURRENTLY JUSTIFIED** for the original uniform assertion (GQ). No counterexample to (GQ) is established. The completed output is the component-count interface in §2 and the precise **collision-supported cut** obstruction in §4. These are auxiliary deductions, not an admitted paper or a new irreducibility theorem. The exact unproved uniform step is (CUT) below; alternatively one could prove transitivity contributed by colliding primitive clusters.

The native small-cycle calculation cannot remove this step. The classical full-discriminant criterion is not merely unchecked here: its squarefreeness hypothesis fails at every level under consideration, as §3 proves. This does **not** imply that the primitive discriminant criterion fails.

## 1. Exact generic algebra and its infinity labels

We record the generic algebra carefully because neither a ramified finite parameter fiber nor the wild affine invariant-ring base change may be substituted for it.

**Lemma 1 (classical infinity construction, reconstructed for this interface).** For any field $k$ of characteristic different from $2$, the generic polynomial $\Phi_n$ is separable and its roots have exact native period $n$. For $n=p^e$, its degree is $N_n=2^n-2^m$. If $k$ is algebraically closed and $n$ is odd, the local monodromy at parameter infinity acts on its native cycles by fixed-point-free binary complementation.

**Proof.** Put $c=-t^{-2}$ and seek an $n$-periodic orbit in the form $x_i=t^{-1}u_i(t)$, with indices in $\mathbb Z/n\mathbb Z$. Its equations become

$$u_i^2-1=t u_{i+1}.$$

For each sign word $(\epsilon_0,\ldots,\epsilon_{n-1})\in\{1,-1\}^n$, the solution at $t=0$ is $u_i=\epsilon_i$. The Jacobian in the $u_i$ is diagonal modulo $t$, with entries $2\epsilon_i$, hence invertible. The formal implicit-function theorem gives one and only one solution in $k[[t]]^n$ with these residues. If two first coordinates agreed, the iteration equations would make every coordinate agree, contradicting different sign words. We have therefore obtained $2^n$ distinct roots of $f_c^{\circ n}(x)-x$, its full degree. A shift of the word is the action of $f_c$. Uniqueness shows that the exact period of the root is the exact shift period of the word. Removing the words of period dividing $m$ proves the assertions for $\Phi_{p^e}$.

The extension $k((t))/k((t^2))$ is quadratic, with involution $t\mapsto-t$. It sends $t^{-1}u_i(t)$ to $-t^{-1}u_i(-t)$, whose sign word is the complement of the original word. A word and its complement cannot be shift-equivalent when $n$ is odd: shift preserves the number of plus signs, whereas complementation replaces that number $a$ by $n-a$. Equality would imply $2a=n$. This also proves that every quotient sheet has inertia orbit of size two. $\square$

This is a proof of an imported classical input, not a claimed increment over Morton, Lemmas 1–2/Proposition 10, or Bousch's infinity analysis. It uses no mathematical execution.

Let $\Omega_n$ be the geometric roots and $\mathcal C_n=\Omega_n/\langle\sigma\rangle$ the set of native cycles. Flat scalar extension commutes with the kernel defining invariants, so

$$
A_n\otimes_F\overline F\simeq\overline F^{\Omega_n},\qquad
B_n\otimes_F\overline F\simeq\overline F^{\mathcal C_n},\qquad
\dim_F B_n=r_n=\frac{2^n-2^m}{n}.
$$

Thus $A_n/B_n$ is a finite étale $C_n$-torsor of rank $n$, although either algebra may be a product of fields. No division by $n$ inside $F$ occurs in this argument. The displayed integer quotient counts free orbits.

For an explicit invariant presentation, use **all coefficients** of

$$\mathcal M_x(T)=\prod_{i=0}^{n-1}(T-\sigma^i x)\in A_n[T].$$

They generate $B_n$: after scalar extension they distinguish any two cycles, because the corresponding monic root polynomials are different. Functions separating a finite set generate its full function algebra, and faithfully flat descent gives the assertion over $F$. A cycle trace alone is not assumed to generate the quotient, especially when $p\mid n$.

## 2. Exact component formula and local/global compatibility

Let $G\leq\operatorname{Perm}(\Omega_n)$ be the geometric Galois group over $F=k(c)$. It commutes with $\sigma$. Write

$$B_n=\prod_{j=1}^{s}F_j,\qquad r_j=[F_j:F],\qquad \sum_jr_j=r_n.$$

The $j$th field corresponds to a $G$-orbit $\mathcal O_j$ in $\mathcal C_n$. Pick $C_j\in\mathcal O_j$, and let $G_{C_j}$ be its setwise stabilizer. Its restriction to $C_j$ consists of cyclic rotations; let the restriction image have order $h_j\mid n$.

**Lemma 2 (component count).** Above the $j$th quotient component, the point algebra has exactly $n/h_j$ field factors, each of degree $r_jh_j$ over $F$. Therefore

$$
\#\operatorname{Irr}(\Phi_n)=\sum_{j=1}^{s}\frac{n}{h_j}.
\tag{CC}
$$

Moreover $r_j$ is even for every $j$. The normalized quotient has $r_n/2$ points above infinity, all of ramification index $2$; the $j$th component contains $r_j/2$ of them.

**Proof.** Fix $\omega\in C_j$. For any cycle $C\in\mathcal O_j$, choose $g$ sending $C_j$ to $C$. The intersection of $G\omega$ with $C$ is $g(G_{C_j}\omega)$, which has $h_j$ points because rotations act freely. Thus every $G$-orbit above $\mathcal O_j$ has $r_jh_j$ points. There are $nr_j$ points in total, giving $n/h_j$ orbits. Finite étale field factors correspond exactly to these Galois orbits. Since $\Phi_n$ is monic in $x$, it has no nonconstant factor depending only on $c$; hence all curve components dominate the parameter line. Gauss's lemma identifies its factors over $k[c,x]$ with those over $F[x]$, so (CC) counts the geometric components of the reduced total curve, not the components or lengths of a single parameter fiber. Lemma 1 makes every $G$-orbit of cycle sheets a union of complement pairs, proving evenness and the infinity count. $\square$

Consequently (GQ) is exactly $s=1$, not the stronger assertion that the full point algebra is a field. If $s=1$, then the number of point components is $n/h_1$, a power of $p$.

For the small Hensel factor, let $K_s=k((s))$ and $E_e=K_s[z]/M_e$. Since its geometric roots form one $C_n$-cycle,

$$E_e^{C_n}=K_s.$$

This follows by the same flat invariant calculation as above. It supplies one quotient sheet after completion and tame parameter pullback. If its local Galois action is full $C_n$, restriction of the global stabilizer of that cycle is also full: then $h_{j_*}=n$ for the one global quotient component receiving this branch. Hence **that component** supports one irreducible point factor. It says nothing about the other $s-1$ quotient components. If (GQ) holds as an additional input, (CC) now gives irreducibility of $\Phi_n$.

There is no converse claim that a global full stabilizer must be detected at this particular branch. Nor is this a statement that every finite parameter fiber is reduced.

## 3. The exact satellite collision excluded from the primitive graph

Use $\delta_d(U,c)$ for the product over native $d$-cycles of $U$ minus their multiplier in characteristic zero. The standard multiplier factorization defines satellite polynomials

$$
\Delta_{n,d}(c)=\operatorname{Res}_U(\operatorname{Cyc}_{n/d}(U),\delta_d(U,c))\quad(d\mid n,\ d<n),
$$

and the primitive factor by

$$\delta_n(1,c)=\Delta_{n,n}(c)\prod_{d\mid n,\ d<n}\Delta_{n,d}(c).$$

Here $\operatorname{Cyc}_q$ is the ordinary cyclotomic polynomial, not a dynatomic polynomial. In particular, fixed-point multipliers obey

$$\delta_1(U,c)=U^2-2U+4c.$$

Since $n=p^e$ and $\operatorname{Cyc}_{p^e}(U)\bmod p=(U-1)^{\varphi(p^e)}$, the resultant identity gives

$$
\boxed{\Delta_{p^e,1}(c)\bmod p=(4c-1)^{p^{e-1}(p-1)}.}
\tag{SAT}
$$

The exponent is at least two for every odd $p$ and $e\geq1$. Thus $\delta_n(1,c)\bmod p$ is not squarefree. This precisely defeats the hypothesis of the corrected Morton full-discriminant theorem at **all** the pairs in this lane. It is not evidence that $\Delta_{n,n}\bmod p$ is nonsquarefree: (SAT) concerns the satellite factor only.

The characteristic-zero branch values in (SAT) are $c=(2\zeta-\zeta^2)/4$ with $\zeta$ primitive of order $p^e$. They all reduce to $1/4$. They rotate one cycle and do not exchange cycles. Thus deleting them as edges of the quotient monodromy graph would be a category error. A primitive branch may independently specialize to the same parameter; determining this requires $\Delta_{n,n}$, not merely (SAT) or the local small-cycle slope.

## 4. Surviving primitive monodromy and the collision-supported cut

Fix an embedding of the characteristic-zero branch field into $\overline{\mathbb Q}_p$ and a compatible identification used to label complex sheets. Let

$$T_n=\{\alpha:\Delta_{n,n}(\alpha)=0\},\qquad
\mathcal K_{p,n}=\{\alpha\in T_n:\exists\beta\in T_n\setminus\{\alpha\},\ \bar\alpha=\bar\beta\}.$$

All these values are integral at odd $p$. Put $T_{p,n}^{\rm sep}=T_n\setminus\mathcal K_{p,n}$.

Vertices are the primitive binary necklaces of length $n$. A primitive branch value $\alpha$ labels one transposition $\tau_\alpha$ of two cycle sheets. Also include the complement edges of the single infinity inertia permutation $\iota$. **Infinity inertia is a product of disjoint transpositions**, not one independently selectable inertia generator for each edge. Its orbit graph is nevertheless exactly the complement pairing. Define $\Gamma_{p,n}^{\rm sep}$ by retaining these complement edges and only finite edges labeled by $T_{p,n}^{\rm sep}$.

The selected unresolved uniform statement is

$$
\begin{split}
&\text{For every odd }p,\ e\geq1,\ n=p^e,\text{ every }\varnothing\ne S\subsetneq\mathcal C_n\text{ with }\iota(S)=S,\\
&\qquad\exists\alpha\in T_{p,n}^{\rm sep}\text{ whose edge has exactly one endpoint in }S.
\end{split}
\tag{CUT}
$$

**Conditional bridge.** (CUT) implies (GQ), and with A3's full local inertia additionally implies one point component. More quantitatively,

$$s\leq\#\pi_0(\Gamma_{p,n}^{\rm sep}).\tag{GB}$$

**Proof of the graph step.** For any subset of vertices, invariance under a transposition is equivalent to not cutting its edge; invariance under $\iota$ is equivalent to being a union of complement pairs. Thus (CUT) is exactly transitivity of $H=\langle\iota,\tau_\alpha:\alpha\in T_{p,n}^{\rm sep}\rangle$, equivalently graph connectedness. The same argument identifies all $H$-orbits with graph components. Under the specialization interface specified next, the special-fiber monodromy contains these actions on the same sheet set. Its orbits therefore coarsen the $H$-orbits, proving (GB). Lemma 2 completes the conditional conclusion. $\square$

**Imported specialization interface, with hypotheses retained.** Use the normal finite flat compactification over a mixed-characteristic complete DVR, reduced special fiber, generically separable special map, and characteristic-zero branch sections. Inertia from sections isolated on reduction survives on a common fiber. These conditions for the quadratic quotient and the resulting connectivity implication are established in Doyle et al., §§6 and 8 (Proposition 8.1, Corollary 8.3). Their Theorem 9.1 proves connectivity after any two finite-edge deletions; Proposition 8.6 extends the implication when connectivity after $2v_p\operatorname{disc}\Delta_{n,n}$ deletions is supplied. The latter connectivity is a hypothesis, not a uniform result. [Primary accepted manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/17388c5b-06f8-4235-afed-8ae9a331c5f3/content).

These imports do not use the generally invalid assertion that invariants commute with arbitrary nonflat reduction. Our generic algebra is identified on the open locus where the cyclic action is free and the point cover is étale; there the quotient is a finite étale torsor and base change is valid. Normalization supplies the branch model needed for specialization. No claim about the whole singular affine invariant ring is needed for (GQ) or (CC).

**Necessary obstruction, not a counterexample certificate.** If (GQ) fails, at least one nonempty proper union of complement pairs has every crossing primitive edge in $\mathcal K_{p,n}$. Conversely, finding such a cut only defeats this surviving-edge proof: the colliding primitive clusters can still contribute monodromy that connects it. A discriminant alone gives neither the incidence labels nor this missing cluster monodromy.

No uniform description of $\mathcal K_{p,p^e}$, no proof of (CUT), and no substitute transitivity theorem for its colliding clusters has been obtained here. In particular, we have not proved $p\nmid\operatorname{disc}\Delta_{p^e,p^e}$, or the weaker valuation-one bound, for all $p,e$.

## 5. Primary-source ownership and precise non-applications

| Primary source actually accessed | Input or exact limitation |
| --- | --- |
| [Bousch, 1992 thesis, Chapter 3, Theorems 1 and 3; pp. 57–65](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/these-tb.pdf) | Irreducibility and full cyclic wreath-product Galois group are characteristic-zero results. The proof uses complex smoothness before a constant-resultant argument. No unconditional reduction inference is made. |
| [Morton, *Compositio* 103 (1996), Theorem 15 and Propositions 17–18; pp. 345–348](https://www.numdam.org/article/CM_1996__103_3_319_0.pdf) | Distinct-root hypotheses are essential to the stated finite-characteristic criteria. Proposition 17 explicitly forces $p\nmid n$; Proposition 18 also requires a squarefree fixed-point satellite factor. Neither bypasses (SAT). |
| [Morton, 2011 corrigendum, pp. 332–334](https://doi.org/10.1112/S0010437X1000480X) | Repairs a formal Hensel-factor-to-polynomial gap by a uniform degree bound. It preserves the distinct-root assumptions; it does not establish them at wild levels. Full corrective argument accessed. |
| [Morton, *Acta Arith.* 87 (1998), §4, pp. 99–100](https://matwbn.icm.edu.pl/ksiazki/aa/aa87/aa8721.pdf) | Individual low-period trace-polynomial irreducibility arguments are already classical. No low-period calculation is repeated or claimed as uniform progress. |
| LRL and accepted first-pass A3/A4/E2 artifacts | Own the small native cycle, slope, trace-one/AS criterion and accepted local bounds. This round does not reclassify those inputs as new results. |

The Doyle graph and specialization results are fully source-owned. We checked both arXiv v2 and the later accepted manuscript: the $2d$-deletion statement is **Remark 8.6 in v2**, **Proposition 8.6 in the accepted manuscript**; the quotient-to-point tame comparison is Proposition 6.15 in the latter and explicitly excludes $p\mid n$. Our conditional full-local-inertia bridge is stated separately from that tame proposition.

## 6. Verification, handoff and remaining gap

Proof status is split deliberately: Lemmas 1–2, (SAT), and the graph-theoretic equivalence are proved; specialization is imported with its exact model hypotheses; (GQ)/(CUT) remain unproved uniformly. The proof-writer skill determined this explicit gap classification. Research-lit and the batch skill enforced primary-source subtraction, including the Morton corrigendum and the source-owned two-edge theorem.

Reusable interfaces sent to the coordinator and A3 are:

1. Generic quotient rank and component formula (CC), without a trace-generation assumption.
2. One small cycle, even with full local inertia, controls only $h_{j_*}$, not $s$.
3. The exact arithmetic/combinatorial task (CUT), and the one-way obstruction interpretation.
4. The all-level satellite identity (SAT), which distinguishes the invalid full-discriminant shortcut from the still-open primitive-branch question.

No mathematical programs or old reruns were executed. No data census, manuscript/PDF, formal evaluation, shared-file modification, Git operation, or external-model upload was performed. Routine file reads and primary-source retrieval were used. No new paper admission is requested. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
