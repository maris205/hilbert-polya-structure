# Candidate Registry

## SD-C12 — entropy-paired relative determinant

- Family: **Symbolic Dynamics**, exclusively.
- Atom source: tensor-indecomposable full shifts, internally generated and
  ordered by entropy log(p).
- Pairing: adjacent entropy ranks.
- Parity: p_(2n-1) is plus/super-even/numerator; p_(2n) is
  minus/super-odd/denominator.
- Relative determinant:

  \[
  R(s,z)=\prod_n
  \frac{1-zp_{2n-1}^{-s}}{1-zp_{2n}^{-s}}.
  \]

- Reflection: H(s,z)=R(s,z)R(1-s,z).
- Primary normalization: z=1.
- Data firewall: no Riemann zeros, target roots, fitting, or rescaling.

### Exact accomplishments

1. D_s^+-B_s is trace class and trace-norm holomorphic on Re(s)>0.
2. R is an exact relative Fredholm determinant, with all repetition
   coefficients retained.
3. H has exact reflection and strict critical-line motion.
4. H(s,1) is zero-free throughout 0<Re(s)<1.
5. The fixed finite-block extension theorem requires coefficient sum zero.

### Fatal Route-A boundary

The minus sector has coefficient -1 at every repetition. It is not a
primitive holonomy phase, which would be raised to the repetition number.
Thus A1 fails the uniformly positive prime-power ledger. Moreover, the
primary reflected determinant has an empty divisor in its proved strip.

Offsets 1,2,3, all 32 random bounded-block pairings, shuffled atoms,
composites, consecutive integers, and random increasing inventories
reproduce convergence and motion. The mechanism is PROVES_TOO_MUCH.

### Route status

    (A0_ANALYTIC_ARITHMETIC_ORIGIN,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

    ROUTE_A_REJECTED
    STOP_SCOPED / PROVES_TOO_MUCH
    route_b_invocation_allowed: false

The canonical evaluation records the immutable Paper10 source/code/results
commit and is finalized with the paper manifest in the following metadata
commit.
