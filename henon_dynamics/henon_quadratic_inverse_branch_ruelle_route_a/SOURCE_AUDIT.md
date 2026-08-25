# C141 source and scope audit

## Frozen source

- Candidate: `HCS-C141`; date: `2026-08-25`.
- Map and clock: \(F(z)=z^2-6\), one inverse branch per iterate.
- Owner domain: \(\mathbb D_4\). Since \(6+\mathbb D_4=D(6,4)\) lies in the right half-plane, the principal square root is holomorphic there.
- Branch convention: \(\psi_+=\sqrt{z+6}\), \(\psi_-=-\sqrt{z+6}\), with their actual derivatives, including the minus sign for \(\psi_-'\).
- Space and normalization: \(H^2(\mathbb D_4)\), \(e_j(z)=(z/4)^j\).
- Operator: \(\mathcal L_m=\sum_\epsilon M_{(\psi_\epsilon')^m}C_{\psi_\epsilon}\); headline \(m=2\).
- Determinant variable and sign: \(D_2(u)=\det(I-u\mathcal L_2)\).
- Precision: exact integer/rational quotient algebra. Periods \(1\)–\(6\) are replay only, not a theorem cutoff.

## Evidence ownership

Every numerical fraction in the paper is generated from the frozen map by the package producer. The independent checker does not import that producer. A third SymPy path verifies polynomial inversion, traces, Newton coefficients, and low-period resultants. No external numerical table is input.

General facts about nuclear weighted composition operators are proved in the paper in the precise form used here. This package does not assert external novelty for those general facts.

## Scope firewall

Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Forbidden and absent: target zero tables, prime tables, local/arithmetic factors, Euler products in the arithmetic sense, root numbers, automorphy, target functional equations, and Hilbert--Pólya claims. “Primitive product” always means the source dynamical Fredholm product displayed in the theorem; it is not an arithmetic Euler-factor claim.

Route B is not authorized. The strict output is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with overall `ROUTE_A_EXPLORATORY`.

## Negative control

Replacing \(-6\) by \(-2\) while retaining the same \(\mathbb D_4\) construction fails: the branch point \(-2\) lies in the owner disk, so no global holomorphic square root of \(z+2\) exists there. This says nothing about other domains or spaces.
