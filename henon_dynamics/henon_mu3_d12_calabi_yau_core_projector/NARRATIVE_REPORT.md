# HCS-C52 narrative report

Status: **B0--B2 theorem narrative; release candidate certified**

## One-sentence result

The fourth H\'enon odd packet admits a \(K\)-rational Chow splitting into
a rank-\(10\) invariant core that becomes Calabi--Yau-threefold Hodge type
after one Tate twist and a rank-\(158\) complement that becomes level one
after the C51 twist by two, while the rational graph algebra of
the complete order-\(24\) projective monomial source group cannot isolate
the desired rank-two extreme pair.

## The big door opened

C51 ended with a concrete alternative: either find a \(K\)-rational
algebraic projector inside

\[
O_4=H^5(X)(2),
\]

or prove that the visible symmetry algebra is too coarse.  C52 obtains
both a positive and a negative theorem at that scale.

The positive theorem is not merely a numerical eigenspace decomposition.
The explicit correspondences

\[
\pi_{2i}=\frac16h^{5-i}\times h^i,\qquad
\pi_5=\Delta_X-\sum_{i=0}^{5}\pi_{2i},\qquad
e_G=\frac1{24}\sum_{g\in G}[\Gamma_g]
\]

are algebraic over \(K\), and their compositions are verified in the
Chow ring.  Thus

\[
\pi_{\mathrm{core}}=\pi_5e_G,\qquad
\pi_{\mathrm{lev}}=\pi_5-\pi_5e_G
\]

split the same Chow summands in every Weil realization.

The negative theorem is equally structural.  The \(H^{4,1}\) line and
four copies inside \(H^{3,2}\) carry the same trivial representation of
the projective monomial source group.  Every element of
\(\mathbf Q[G]\) acts on all five copies through one augmentation scalar.
An idempotent that retains the extreme line must therefore retain the
four interior copies as well.  Rank \(10\) is the exact graph-algebra
floor, and the Reynolds projector attains it.

## Why the source group matters

The source stabilizer is not guessed from a visual cycle symmetry.
The closing coefficient \(\rho\) in

\[
Q=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0
\]

forces an affine phase system over \(\mathbf F_3\).  Exhausting the
sixteen dihedral support permutations leaves \(24\) projective monomial
maps.  Two explicit generators satisfy

\[
r^{12}=s^2=1,\qquad srs=r^{-1}.
\]

Accordingly

\[
G\cong\operatorname{Dih}(C_{12}),
\]

where this notation always means order \(24\).  The result classifies the
projective monomial **source** stabilizer only, not the full automorphism
group of \(X\).

## The residue correction that changes the calculation

The Cayley-ring character is not the naive polynomial substitution
character.  If

\[
\binom C Q(M_gx)=A_g\binom C Q(x),
\]

the induced residue action includes

\[
\omega(g)=\frac{\det M_g}{\det A_g}.
\]

This determinant ratio cancels the dependence on a scalar lift of the
projective transformation.  It happens to equal one for the selected
generator lifts, but omitting it makes the construction noncanonical and
is therefore a release-failing mutation.

The corrected character has four trivial copies in \(H^{3,2}\).  Together
with the trivial \(H^{4,1}\) generator and conjugates, this gives

\[
\operatorname{rank}H_{\mathrm{core}}=1+4+4+1=10,
\qquad
\operatorname{rank}H_{\mathrm{lev}}=158.
\]

The corresponding Hodge ledgers are

\[
(1,4,4,1)\quad\text{and}\quad(0,79,79,0).
\]

After one Tate twist, the first is of Calabi--Yau-threefold Hodge type.
After the C51 twist by two, the second is of level one.  These are Hodge
statements, not constructions of a Calabi--Yau threefold or an abelian
variety over \(K\).

## Route-A assessment

C52 is a meaningful structural advance but not a Route-A pass:

- **A1, source chronology:** inherited; the odd fourth-moment source is
  unchanged.
- **A2, analytic determinant:** inherited; C52 neither improves nor
  damages the normalized Euler germ.
- **A3, arithmetic/analytic control:** structurally improved because a
  large cohomological packet is split by an algebraic projector, but no
  local Frobenius polynomials, automorphy, full functional equation, or
  new continuation domain are proved.
- **A4, natural quantization:** \(\mathrm{A4\_NATURAL\_QUANTIZATION}\)
  is inherited because the source two-step quantization is unchanged;
  no self-adjoint generator is constructed.

The appropriate overall status remains **Route-A exploratory**.  The
new value is that the C51 projector gate is no longer vague: the natural
graph algebra opens a rank-\(10\) door and simultaneously proves its own
rank-two limit.  No Riemann-divisor match is obtained.

## C53 handoff

C53 must be a separate theorem-sized paper rather than a continuation of
the finite group enumeration.  Its go gate is to compute full
rank-\(10\) Frobenius polynomials at enough good split primes, test
factorization and irreducibility in the correct coefficient field, and
search for algebraic incidence correspondences outside
\(\mathbf Q[G]\).

Two outcomes are valuable:

1. **positive branch:** a new \(K\)-rational algebraic projector refines
   the trivial isotypic block, producing a genuinely smaller motivic
   packet; or
2. **negative branch:** exact Frobenius data and a commutant calculation
   prove that the rank-\(10\) core is generically irreducible under the
   available algebraic correspondence algebra.

C52 itself claims neither outcome.

## Claim firewall

The project does not claim full automorphism classification, coniveau,
an abelian \(79\)-fold over \(K\), finite-dimensional motive, automorphy,
a Hasse--Weil or full H\'enon functional equation, a new Euler half-plane,
a Riemann divisor, or a self-adjoint Hilbert--P\'olya operator.  It also
does not call the realization of a single Chow projector a certified
strict compatible system with computed common Frobenius polynomials.
