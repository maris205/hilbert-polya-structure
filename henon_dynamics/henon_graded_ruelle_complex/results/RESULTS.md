# HCS-C22G audited results and open gates

## Corrected gate table

| Gate | Audited status | Meaning |
|---|---|---|
| G0 source reconstruction | **pass** | Primary-source conventions and theorem boundaries reconstructed |
| G0 conceptual novelty | **fail** | The intended mechanism is classical analytic/Lefschetz infrastructure |
| G1 corrected one-step pinning | **pass** | Common \(\mathbb C^2\)-contracting / \(\mathbb C\)-expanding cross domains and exact constants |
| G2 one-step candidate blocks | **exact definition** | 12 ordered graph-letter kernels in each degree, with physical fibre basis and ordered contours |
| G2 all-word kernel theorem | **open** | Iterated pinning, intermediate residues, chronological cocycle, and signs are not proved |
| G3 nuclearity | **open** | No explicit enlarged-\(z\) factorization, order-zero decomposition, MAP proof, or nuclear-ideal \(s\)-holomorphy |
| G4 finite residue/exterior algebra | **pass** | Block determinant minus sign and shifted parity \(k+1\) are exact finite identities |
| G4 all-period supertrace | **open** | Canonical nuclear trace equals fixed-point residue has not been proved for \(n=1,2\) and general \(n\) |
| G5 Fredholm continuation | **conditional** | Jointly entire factors and a meromorphic quotient require G2--G4 |
| Promotion | **fail** | No new arithmetic or Hilbert--Pólya mechanism |

The earlier `pass` labels for G2--G5 are withdrawn.

## Exact one-step constants

The three normalized **image** ratios are

\[
\frac{39}{41},\qquad
\frac{250880}{466211},\qquad
\frac{907}{915}.
\]

They control the first contracting output, projective output, and expanding
half-inverse image.  In particular, the third number is not by itself an
output-\(z\) restriction ratio for a nuclear factorization.

The full lifted Jacobian and fixed-output pinning Jacobian have the uniform
lower bounds

\[
|\det D\widehat F_a|\ge\frac{50176}{3352561},
\qquad
|\det D_{(x,m)}K|\ge\frac{401408}{204506221}.
\]

These exact bounds prove pole exclusion and one-step local invertibility on
the certified domains.

## Exact finite-dimensional algebra

Freeze scalar variables as \((x,m,u)\), tangent fibres in the physical basis
\((e_x,e_y,e_m)\), residuals as

\[
(x-K_1,m-K_2,u-h),
\]

and product orientation as \(dx\wedge dm\wedge du\).  The symbolic block
calculation gives

\[
\det DR=-\partial_z h\,\det(I-DF).
\]

Hence the associated simple raw residue has sign

\[
-\frac1{\det(I-DF)}.
\]

Together with

\[
\sum_{k=0}^3(-1)^k\operatorname{tr}(\wedge^kM)=\det(I-M),
\]

this fixes the **candidate** total parity to \(k+1\).

It does not unconditionally imply

\[
D_{\rm inst}(z,s)=\frac{D_1(z,s)D_3(z,s)}{D_0(z,s)D_2(z,s)}.
\]

That identity is conditional on a valid all-word kernel theorem, canonical
nuclear trace formula, and order-zero Fredholm construction.

## What the code regression verifies

The producer and independent checker retain useful exact controls:

- rational domain and Jacobian constants;
- graph states, edges, and two-letter nonaveraging metadata;
- the generic block determinant identity;
- the exterior polynomial identity and parity mutation;
- a finite matrix chronology mutation;
- rejection of the reversed pinning convention and false scalar-entireness
  metadata.

The reported exact checks and mutation tests remain reproducible.  They do
not instantiate the mixed Banach spaces, construct an enlarged output domain,
produce a nuclear decomposition, evaluate a canonical nuclear trace, or
construct a several-variable Fredholm determinant.  Therefore certificate
fields that label G2--G5 as passing are legacy assertions, not theorem
evidence.

## Conditional analytic target

If the open gates are later closed, the intended formula is

\[
\operatorname{tr}\mathcal L_{s,k}^n
=-
\sum_x
\frac{g_s^{(n)}(x)
\operatorname{tr}(\wedge^kD\widetilde{\mathcal F}^n_x)}
{\det(I-D\widetilde{\mathcal F}^n_x)}.
\]

The shifted supertrace would then produce \(B_n(s)\), and the alternating
Fredholm quotient would define a meromorphic germ on \(\mathbb C^2\).  This
paragraph states the target implication only; it is not a reported result.

## Interpretation and decision

The genuine advance relative to HCS-C22 is currently limited to explicit
three-dimensional one-step analytic geometry, correct kernel conventions,
and finite residue/exterior algebra.  Route-A layer A3 is therefore
**conditional/open**, not upgraded by a proved meromorphic continuation.

There is no advance toward the arithmetic divisor, no functional equation,
and no self-adjoint lift.  HCS-C22G is retained as a conditional analytic
blueprint and the C22 operator lineage is closed without claiming G2--G5.

The successor HCS-C23 experiment is also closed: its finite chronology
separation survives packet norm, but each fixed-word repetition tower is the
classical cyclic-resultant sequence

\[
\Delta_{w,r}=\operatorname{Res}_X(P_w(X),X^r-1).
\]

Its decision is `CLOSED_AT_CYCLIC_RESULTANT_BASELINE`; no Euler product or
cross-period Zsigmondy law is claimed.
