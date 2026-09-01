# Root scout: Boolean row-inclusion dynamics

## Literal carrier and map

For an (n\times n) Boolean matrix (A), let (R_i(A)\subseteq[n]) be the support of row (i), and define

\[
  T_n(A)_{ij}=1\quad\Longleftrightarrow\quad R_i(A)\subseteq R_j(A).
\]

This is a literal finite self-map on (2^{n^2}) states.  No quotienting is used in the dynamics.

## Exact signal

The image consists exactly of labelled preorders.  If (P) is a preorder, its rows are the principal upper sets and

\[
  T_n(P)=P^{\mathsf T}.
\]

Consequently (T_n^3=T_n): every nonperiodic state has tail exactly one, every preorder is periodic, fixed points are exactly equivalence relations, and every nonsymmetric preorder belongs to a strict transpose two-cycle.  Thus

\[
 |\operatorname{Fix}(T_n^k)|=
 \begin{cases}
 B_n,&k\text{ odd},\\
 p_n,&k\text{ even},
 \end{cases}

where (B_n) is the Bell number and (p_n) is the number of labelled preorders.

## Every-target fibre formula

Let (P) be a preorder, let (Q=P/{\sim}) be its antisymmetric quotient, and let (J(S)) denote the number of upper sets of a finite preorder (S).  A preimage of (P) is precisely an induced order embedding (Q\hookrightarrow B_n).  Writing

\[
 D_Q=\{(q,r):q\not\le_Qr\},
\]

and (Q_S) for the reflexive-transitive closure obtained by adjoining all pairs in (S\subseteq D_Q), inclusion--exclusion gives

\[
 |T_n^{-1}(P)|=
 \sum_{S\subseteq D_Q}(-1)^{|S|}J(Q_S)^n.
\]

For a non-preorder target the fibre is empty.  This yields the complete image and all fibres, not only orbit-length data.

## Exact replay

`verify_row_inclusion.py` exhausts all (2^{n^2}) matrices for (1\le n\le4).  It independently checks the image characterization, (T(P)=P^{\mathsf T}), (T^3=T), the Bell-number fixed set, mass conservation, and the inclusion--exclusion formula for every image target.  The canonical run records 264,673 passing assertions.

## Collision assessment

The nearest internal neighbours are P106 (MIS polarity) and P127 (parity-transpose looped digraphs).  This candidate uses neither independence polarity nor parity degrees: its collapse object is the full category of finite labelled preorders, its involution is order reversal, and its fibres are induced Boolean-lattice embeddings.  It remains subject to an external ownership search before selection.

Status: **strong finalist, novelty language withheld; HOLD_EXTERNAL**.
