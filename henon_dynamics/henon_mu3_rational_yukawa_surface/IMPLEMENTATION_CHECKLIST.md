# HCS-C55 implementation checklist

Status: **RELEASE_FROZEN; exact implementation, hostile/source audit,
official compilation, documentation-hash backfill, and implementation
commit `e5661e80da6f7de53f574f97f768744095ba8ae0` are provenance-locked**.

## Frozen inputs

- [x] verify the exact HCS-C52 certificate hash
- [x] verify the exact HCS-C53 theorem and dependency hashes
- [x] verify the exact HCS-C54 theorem and dependency hashes
- [x] serialize \(\rho^2+\rho+1=0\) and \(\tau(\rho)=\rho^2\)
- [x] serialize \(D(y)=y\) and \(D(z)=\rho z\)
- [x] serialize the residue determinant twist
- [x] serialize the rational basis with \(q_0=e_0\)

## Ambient descent

- [x] reconstruct all \(24\) split group elements
- [x] check their distinctness and group relations
- [x] check covariance of the cubic line
- [x] check covariance of the quadric line
- [x] check \(\delta(g)=M\tau(g)M^{-1}\)
- [x] check
  \(\tau(B^{-1}gB)=B^{-1}\delta(g)B\)
- [x] record a nonconstant rank-\(24\) group scheme, not \(24\) rational points

## Deformation tangent

- [x] solve the \(74\)-unknown infinitesimal ideal-stabilizer system
- [x] certify rank \(73\) and only the scalar \(\mathfrak{gl}_8\) kernel
- [x] identify that kernel exactly as
  \((A,\nu,\mu,L)=\lambda(I_8,2,3,0)\)
- [x] infer zero projective Lie stabilizer without claiming the full PGL group
- [x] recompute \(R_{1,-3}=K[y]\)
- [x] recompute \(\dim R_{2,-3}=83\)
- [x] reconstruct the four split invariant directions
- [x] check all-\(24\) invariance
- [x] check semilinear fixedness
- [x] check rational-basis descent
- [x] record \([yp_i]\in R_{1,0}\) as operators
- [x] record \([y^2p_i]\in R_{2,-3}\) as first images
- [x] prove the four first images are independent

## Top component and Yukawa

- [x] count \(24145\) ambient bidegree-\((5,-6)\) monomials
- [x] find exactly one top standard monomial
- [x] recompute \(\dim R_{5,-6}=1\)
- [x] freeze its normalization
- [x] check
  \(D(x_6^2x_7^2z^5)=x_1^2x_2^2z^5\) before quotient reduction
- [x] check the induced one-dimensional top-line cocycle
- [x] record all \(20\) classes \([y^4p_ip_jp_k]\)
- [x] record all \(20\) paired classes \([y^5p_ip_jp_k]\)
- [x] reduce \(y^5(\sum u_ip_i)^3\) directly
- [x] reconstruct with \(1/3/6\) multiplicities
- [x] require exact equality of the two reconstructions
- [x] verify rational coefficient ratios
- [x] primitive-normalize with gcd one
- [x] compare all \(20\) displayed coefficients

## Cubic surface

- [x] compute all four exact partial derivatives
- [x] recompute the gradient quotient independently
- [x] verify vector-space length \(16\)
- [x] verify Hilbert series \((1+t)^4\)
- [x] verify numerator
  \(1-4t^2+6t^4-4t^6+t^8\)
- [x] verify the equivalent no-nonzero-projective-gradient criterion with an
      independent finite homogeneous quotient
- [x] derive geometric smoothness
- [x] derive geometric irreducibility from smoothness
- [x] do not use rational factorization as the geometric proof
- [x] do not infer that the \(\mathbf Q\)-defined surface is
  \(\mathbf Q\)-rational

## Schema and adversarial controls

- [x] reject duplicate keys
- [x] reject unknown top-level keys
- [x] inventory every scalar leaf as central, independently derived, or
  explicitly nonsemantic
- [x] reject every unclassified scalar leaf
- [x] rebound every semantic leaf after recomputing payload and schema hashes
- [x] specifically kill the mutation
  `finite_prime_matches_prove_motive: false -> true`
- [x] reject a changed field without semantic recomputation
- [x] kill \([yp]\leftrightarrow[y^2p]\)
- [x] kill \(y^5\leftrightarrow y^4\)
- [x] kill the wrong conjugation or determinant twist
- [x] kill an unpropagated \(q_0\) rescaling
- [x] kill every single-coefficient mutation
- [x] kill missing multinomial factors
- [x] kill a two-rational-graph Reynolds cycle
- [x] kill factorization-only geometric irreducibility
- [x] kill literal_linear_family=true
- [x] kill motive_realized=true

## Independence and determinism

- [x] producer and checker use separate reconstruction paths
- [x] checker does not parse producer conclusions as premises
- [x] checker does not share a cached Groebner basis
- [x] two producer runs have identical semantic bytes
- [x] checker passes from a clean temporary directory
- [x] all exact software and term-order versions are recorded

## Documentation/paper promotion

- [x] integrate exact field names without changing theorem scope
- [x] close every pending status in PROOF_PACKAGE.md
- [x] update SOURCE_AUDIT.md with final local hashes
- [x] run the final cross-document firewall search
- [x] perform the official clean paper build after exact promotion
- [x] run hostile read-only schema audit
- [x] write the scoped artifact manifest
- [x] verify the 47-entry full-project manifest while reporting its SHA-256
      only outside manifest-covered artifacts to avoid a self-hash cycle
- [x] fill PDF/source/report/Route hashes while retaining the explicit null
      until the implementation-commit provenance stage
- [x] backfill implementation commit
      `e5661e80da6f7de53f574f97f768744095ba8ae0` without reopening the paper
      or changing the scoped release-candidate tuple
- [x] leave top registries and the user-owned prompt untouched unless the
      root task separately authorizes them

## Comparator branch

- [x] keep BCD label NOT-COMPARABLE-WITH-CURRENT-DATA
- [x] do not substitute the mirror-side one-parameter special-geometry
      calculation for the original four-variable B-model tensor
- [x] do not use the nodal enhanced-dihedral locus as a smooth comparator
- [x] require a full four-variable B-model tensor before incidence testing
- [x] treat projective cubic equivalence as necessary only
