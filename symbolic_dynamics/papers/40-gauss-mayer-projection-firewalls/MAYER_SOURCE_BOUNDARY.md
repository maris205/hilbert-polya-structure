# Mayer operator and Selberg-identity source boundary

## Verified theorem statement

Let

$$
D=\{z\in\mathbb C:|z-1|<3/2\}
$$

and let $A_\infty(D)$ be the Banach space of functions holomorphic on $D$ and
continuous on $\overline D$, with the supremum norm. For
$\operatorname{Re}s>1/2$, Mayer's Gauss operator

$$
(\mathcal L_s f)(z)=\sum_{n\ge1}(z+n)^{-2s}
f\!\left((z+n)^{-1}\right)
$$

is nuclear of order zero on this realization. In particular its Grothendieck
Fredholm determinant, and that of $\mathcal L_s^2$, are defined there.

Mayer's MPIM 1990 preprint, Proposition 3 (scan p. 8), directly proves the
holomorphic Fredholm identity on the same half-plane
$\operatorname{Re}s>1/2$:

$$
Z_{\mathrm{PSL}_2(\mathbb Z)}(s)
=\det(I-\mathcal L_s^2)
=\det(I-\mathcal L_s)\det(I+\mathcal L_s).
$$

The narrower half-plane $\operatorname{Re}s>1$ is the initial
absolute-convergence domain of the Selberg Euler product used in the proof; it
is not the full domain of Proposition 3's holomorphic determinant identity.
Mayer's Corollary 3 then gives the source-qualified meromorphic continuation
to $\mathbb C$, with the stated possible singular set. These three domains
must remain distinct. Nothing outside the finite exact algebra in SD-C42 is
inferred from a digit cutoff.

This is used only as an equality of functions/Fredholm determinants. A
$\rho$-primitive pair necklace, where the one-pair shift $\rho$ is conjugate
under grouping to the digit-space return $\sigma^2$, is not automatically a
$\sigma$-primitive digit necklace or a primitive hyperbolic/geodesic class.
SD-C42 supplies no objectwise primitive-orbit bijection from the displayed
identity; the exact type boundary is in `PRIMITIVITY_TYPE_FIREWALL.md`.

## Free-marker limitation

For fixed $s$ in the nuclear half-plane, nuclear Fredholm theory defines

$$
D_{42}(s,u)=\det(I-u^2\mathcal L_s^2),
$$

and the algebraic factorization into $\det(I-u\mathcal L_s)$ and
$\det(I+u\mathcal L_s)$ holds on that same operator space. The cited modular
Selberg identity is asserted only at $u=1$. No Selberg interpretation for
arbitrary $u$ is imported without a separate theorem.

## What the sources do not establish

- They do not identify modular “prime” closed geodesics with rational primes.
- They do not, without a separate orbit-splitting bridge lemma, identify each
  primitive pair necklace with one primitive hyperbolic/geodesic class.
- They do not give a rational-prime/prime-power von-Mangoldt ledger.
- They do not turn trace-prime scalar postselection into an invariant operator
  sector.
- They do not identify the Selberg divisor with the completed Riemann divisor.
- They do not justify a stronger Banach space, nuclearity domain, or marked
  determinant continuation than the declarations above.
- They do not make finite word/digit truncations into Fredholm determinant
  evaluations.

## Primary and authoritative sources

1. Dieter H. Mayer, “The thermodynamic formalism approach to Selberg's zeta
   function for $\mathrm{PSL}(2,\mathbb Z)$,” *Bulletin of the AMS* 25 (1991),
   55--60. DOI:
   <https://doi.org/10.1090/S0273-0979-1991-16023-4>.
2. Dieter H. Mayer, “Selberg's function for $\mathrm{PSL}(2,Z)$ via the
   thermodynamic formalism for the continued fraction map,” MPIM Preprint
   Series 1990 (86), official archive:
   <https://archive.mpim-bonn.mpg.de/id/eprint/346/>.
3. Dieter H. Mayer, “On the thermodynamic formalism for the Gauss map,”
   *Communications in Mathematical Physics* 130 (1990). DOI:
   <https://doi.org/10.1007/BF02473355>.

The later survey by Momeni and Venkov, arXiv:1008.4229, was used only to
cross-check theorem numbering and domain separation; it is not substituted
for the primary Mayer claims.

## Evidence classification

- Nuclearity/order-zero and Fredholm existence on $A_\infty(D)$ for
  $\operatorname{Re}s>1/2$: `PROVED / PRIMARY-SOURCE BOUND`.
- Selberg Euler-product absolute convergence for $\operatorname{Re}s>1$:
  `PROVED / PRIMARY-SOURCE BOUND`.
- Holomorphic Selberg-zeta/Fredholm identity for
  $\operatorname{Re}s>1/2$ (Proposition 3):
  `PROVED / PRIMARY-SOURCE BOUND`.
- Meromorphic continuation to $\mathbb C$ (Corollary 3):
  `PROVED / SOURCE-MEROMORPHIC-CONTINUATION ONLY`.
- Any finite prototype claim about the infinite determinant: `NOT CLAIMED`.
- Any SD-C42 objectwise pair-primitive/geodesic-primitive bijection:
  `NOT CLAIMED`.
