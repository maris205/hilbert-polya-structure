# Final frozen theorem contracts — P142–P146

These contracts are claim ceilings after classical inputs and direct-owner background have been subtracted.  A manuscript may narrow a statement after review but may not silently broaden one.  Exact enumeration is used only for falsification.  Every paper remains `HOLD_EXTERNAL`.

## P142 — valuation–gcd dynamics on prime-power divisors

Fix an odd prime (p), (e\ge2), and

\[
 X_{p,e}=\{p^a:0\le a\le e\},\qquad
 F_{p,e}(d)=\gcd(p^e,d^2+p^e/d).
\]

Put (L=\lceil e/3\rceil), (U=\lfloor2e/3\rfloor), and (T_e(a)=\min(2a,e-a)).

1. Prove the literal valuation conjugacy

   \[
   F_{p,e}(p^a)=p^{T_e(a)}.
   \]

   The equal-valuation case (3a=e) must use that (p) is odd.  Exhibit the binary failure rather than hiding it.
2. Prove that the recurrent exponent set is

   \[
   \{0\}\cup[L,U].
   \]

   Zero is fixed; the band is acted on by (a\mapsto e-a).  Thus, with

   \[
   R=U-L+2,\qquad A=1+\mathbf1_{2\mid e},
   \]

   there are (A) fixed states and ((R-A)/2) strict two-cycles, and

   \[
   |\operatorname{Fix}(T_e^k)|=
   \begin{cases}A,&k\text{ odd},\\R,&k\text{ even}.
   \end{cases}
   \]
3. Prove the complete pointwise entry-time law

   \[
   \tau_e(a)=
   \begin{cases}
   0,&a=0\text{ or }L\le a\le U,\\
   \lceil\log_2(L/a)\rceil,&1\le a<L,\\
   1,&a=e,\\
   1+\lceil\log_2(L/(e-a))\rceil,&U<a<e.
   \end{cases}
   \]

   Hence (M_e=1+\lceil\log_2L\rceil).  For (e\ge4), (a=e-1) is the unique deepest exponent; for (e=2,3), (a=e) is the unique deepest exponent.
4. With (m=\lceil\log_2L\rceil) and

   \[
   c_j=\left\lceil\frac{L}{2^{j-1}}\right\rceil-
       \left\lceil\frac{L}{2^j}\right\rceil,
   \]

   prove the complete temporal polynomial

   \[
   \sum_{a=0}^e z^{\tau_e(a)}
   =R+z+(1+z)\sum_{j=1}^{m}c_jz^j.
   \]
5. Prove the image and every-target inverse theorem

   \[
   \operatorname{im}T_e=[0,U],
   \]

   and, for (0\le b\le e),

   \[
   T_e^{-1}(b)=
   \begin{cases}
   \{e-b\}\cup\bigl(\{b/2\}\text{ if }2\mid b\bigr),&b\le U,\\
   \varnothing,&b>U,
   \end{cases}
   \]

   with set union handling the coincidence (3b=2e).
6. General valuation algebra, finite-map zeta bookkeeping, piecewise-linear interval dynamics, and discretized tent maps are zero-credit tools.  The admissible residual is the literal odd-prime divisor map and its complete arithmetic temporal/inverse atlas.

## P143 — Boolean row-inclusion residual dynamics

For an (n\times n) Boolean matrix (A), let (R_i(A)\subseteq[n]) be row (i)'s support and define

\[
 T_n(A)_{ij}=1\quad\Longleftrightarrow\quad R_i(A)\subseteq R_j(A).
\]

1. Prove that (T_n(A)) is a preorder for every (A), every labelled preorder occurs in the image, and

   \[
   T_n(P)=P^{\mathsf T}\quad\text{for every preorder }P.
   \]

   Consequently (T_n^3=T_n).
2. Prove that every nonpreorder has tail exactly one; every preorder is periodic; fixed points are exactly equivalence relations; and every nonsymmetric preorder belongs to a strict transpose two-cycle.
3. If (B_n) is the Bell number and (q_n) is the number of labelled preorders, prove

   \[
   |\operatorname{Fix}(T_n^k)|=
   \begin{cases}B_n,&k\text{ odd},\\q_n,&k\text{ even},\end{cases}
   \]

   and the corresponding zeta factorisation

   \[
   \zeta_{T_n}(z)=(1-z)^{-B_n}(1-z^2)^{-(q_n-B_n)/2}.
   \]
4. Give the complete fibre theorem.  A nonpreorder target has empty fibre.  For a preorder (P), let (Q=P/{\sim}) be its antisymmetric quotient, (D_Q=\{(q,r):q\not\le_Qr\}), let (Q_S) be the reflexive-transitive closure after adjoining (S\subseteq D_Q), and let (J(Q_S)) count its upper sets.  Prove

   \[
   |T_n^{-1}(P)|=
   \sum_{S\subseteq D_Q}(-1)^{|S|}J(Q_S)^n.
   \]

   The proof must first identify a preimage with an induced order embedding (Q\hookrightarrow B_n), then apply inclusion--exclusion to the missing ordered pairs.
5. Relational self-residuation, formation and enumeration of preorders, Bell numbers, Boolean lattices, induced poset embeddings, and generic inclusion--exclusion receive zero contribution credit.  The residual is the iterated period package and every-target inverse atlas.

## P144 — leftmost reassociation of Dyck components

Let (\mathcal D_n) be the Dyck paths of semilength (n).  Write the unique primitive factorisation (P=C_1\cdots C_k).  If (k=1), fix (P).  If (k\ge2) and (C_1=UAD), set

\[
 \Phi_n(P)=UA C_2D C_3\cdots C_k.
\]

1. Prove that one update reduces the number of primitive factors by exactly one.  Hence every recurrent path is fixed, fixed paths are exactly primitive paths, and their number is (\operatorname{Cat}_{n-1}).
2. Prove the pointwise clock

   \[
   \tau(P)=k(P)-1.
   \]

   Therefore the maximum depth is (n-1), uniquely attained by ((UD)^n).
3. Prove the full temporal layer census: the number of paths of depth (k-1) is

   \[
   \frac{k}{2n-k}\binom{2n-k}{n},\qquad1\le k\le n.
   \]
4. Give the complete terminal depth-fibre atlas.  If a fixed target is (T=UQD) and (Q=Q_1\cdots Q_r) has (r) primitive factors, then for every (0\le d\le r) its unique basin source at depth (d) is

   \[
   \bigl(UQ_1\cdots Q_{r-d}D\bigr)
   Q_{r-d+1}\cdots Q_r,
   \]

   with the evident empty-prefix convention.  Thus

   \[
   \sum_{P:\Phi_n^\infty(P)=T}u^{\tau(P)}=1+u+\cdots+u^r.
   \]

   The unique largest terminal fibre has size (n), at (U(UD)^{n-1}D).
5. First-return decomposition, Catalan and ballot enumeration, the atomic Tamari rotation, and generic generating-function extraction are zero-credit tools.  The residual is the deterministic leftmost iteration and its pointwise/layer/terminal-fibre conjunction.  Novelty language is forbidden by the owner-thin gate.

## P145 — uniform vertex-push chains on graph orientations

Let (G=(V,E)) be a finite simple graph with (n\ge1) vertices and connected
component orders (s_1,\ldots,s_c).  Uniformly choose a labelled vertex and
reverse every incident edge, restricting to one push orbit.  Hostile review
located direct folded-hypercube owners and therefore narrowed this contract.

1. Give the explicit component quotient bridge.  With a pivot (*) in a
   connected component of order (s), prove

   \[
   \theta_*([a])=(a_v+a_*)_{v\ne *}
   \]

   sends the nonpivot labelled pushes to coordinate generators and the pivot
   push to the all-ones generator.  Treat (s=1) as an identity move, (s=2) as
   two duplicate labelled generators of the same translation, and (s\ge3)
   as the standard (FQ_{s-1}) walk.  The folded-hypercube identification and
   its single-component spectrum are direct-owner zero-credit inputs.
2. Prove the disconnected labelled random-scan kernel

   \[
   P_G=\sum_{i:s_i\ge2}\frac{s_i}{n}
       (P_{FQ_{s_i-1}}\otimes I_{\ne i})
       +\frac{m_1}{n}I,
   \]

   and its factor polynomial

   \[
   M_G(x)=\prod_i\sum_{j\text{ even}}\binom{s_i}{j}x^j.
   \]

   The eigenvalue (n-2k)/n has multiplicity ([x^k]M_G(x)).  The return and
   period formulas may be recorded as zero-credit spectral consequences, not
   advertised as the residual contribution.
3. Prove the input-only known-(n) inverse.  Put

   \[
   E_s(y)=\sum_r\binom{s}{2r}y^r,\qquad Q_G(y)=\prod_iE_{s_i}(y).
   \]

   Show that every root of (E_s) is simple and negative, that its nearest
   root is

   \[
   \rho_s=-\tan^2\!\left(\frac{\pi}{2s}\right),
   \]

   and that for (2\le r<s), (E_r(\rho_s)\ne0).  This must not be inflated to
   pairwise coprimality of all (E_r,E_s).
4. Implement the inverse using only the public inputs ((n,Q_G)): scan
   (s=n,n-1,\ldots,2), repeatedly divide exactly by (E_s), and finally append
   isolates from the unused total.  The verifier may consult the hidden true
   component partition only after the routine returns.
5. Prove the precise nonidentifiability boundary with constructed witnesses:
   (P_4) and (K_4) have the same unmarked push-kernel spectrum despite
   different adjacency; an unmarked transition kernel contains no selected
   starting orientation; and without supplied (n), all positive-order
   edgeless graphs give the same one-state spectrum.
6. Vertex pushing, push equivalence, the folded-hypercube quotient and
   single-factor spectrum/bipartiteness/random-walk setting, Abelian Fourier
   diagonalisation, and generic stationary/return facts receive zero
   contribution credit.  The residual is only the explicit labelled
   multi-component factorisation and the known-(n) component-order inverse.

## P146 — uniform ear deletion and random triangulations

Start with a labelled convex (n)-gon.  While more than three vertices remain, choose uniformly from all current vertices, delete it, and record the diagonal joining its two current neighbours.  Let (T) be the terminal triangulation.

1. Prove the pathwise clock (n-3) and that every complete deletion order has probability (6/n!).
2. Let (D_T) be the weak dual tree on the (n-2) triangular faces.  For a possible final face (r), root (D_T) at (r), and let (s_v^{(r)}) be the descendant-subtree size of (v\ne r).  Prove the root-resolved history formula

   \[
   H(T,r)=\frac{(n-3)!}{\prod_{v\ne r}s_v^{(r)}}.
   \]

3. Sum over possible final faces to obtain the complete endpoint law

   \[
   H(T)=\sum_{r\in\operatorname{Faces}(T)}H(T,r),\qquad
   \Pr(T)=\frac{6H(T)}{n!}.
   \]

   The proof must give the bijection between deletion histories ending at (r) and child-before-parent orders of the rooted weak dual.
4. Prove the sharp mass theorem

   \[
   H(T)\ge2^{n-3},\qquad
   \Pr(T)\ge\frac{6\,2^{n-3}}{n!},
   \]

   with equality exactly when (D_T) is a path.  Use the leaf-deletion recurrence (L(D)=\sum_{\ell\text{ leaf}}L(D-\ell)), not numerical induction.
5. Ear clipping, convex-polygon triangulations, weak-dual trees, Catalan enumeration, and the generic rooted-tree hook formula are zero-credit inputs.  The residual is the uniform-current-vertex endpoint distribution, its final-face refinement, and the sharp least-mass equality class.
