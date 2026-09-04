# HCS-C364 Narrative Report

## Independent theorem-scale progress

C364 turns one fixed binary quadratic discriminant into a complete finite dynamical system. The key convention is not cosmetic: \((P+\sqrt\Delta)/Q\) represents a form of discriminant \(\Delta\) only after fixing \(Q=2A\), \(P=-B\), and \(C=(P^2-\Delta)/(2Q)\). The primitive gcd filter prevents an imprimitive \(\Delta=20\) form from silently duplicating the golden-ratio state at primitive discriminant \(5\).

Within that locked phase space the theorem is global. Every state has one successor and one predecessor; every orbit is a primitive cycle. Its continued-fraction word gives a hyperbolic integral matrix whose fixed polynomial is an exact multiple of the primitive form. The same matrix controls the cycle multiplier. Conjugate reciprocity supplies an involution that reverses the clock. The full source zeta and Koopman determinant then follow from finite-cycle linear algebra.

## Evidence boundary

The checked artifact covers 469 discriminants, 5,387 states, 775 cycles, and 11,256 fixed-power rows. Its payload SHA-256 is `3673db45c99448d01e655b741530877600e95d5741e01c4f3177a3b42941104f`; the physical evidence SHA-256 is `b96ffc1da7eba7f3e9b8389cde04e706ffbecbae7c3a2df3b6efd8ecc0579a5f`. These exact computations test conventions and identities; they do not replace the analytic proof.

## Route-A interpretation

The result earns `A0_WEAK_ARITHMETIC_RELATION` because the discriminant, forms, and quadratic units are intrinsic. It earns `A1_PASS_ANALYTIC` because all source cycles and multipliers are classified. The source determinant does not equal a target divisor, so A2 and A3 fail. The finite unitary Koopman permutation is only `A4_FORMAL_HINT`. Overall status is `ROUTE_A_EXPLORATORY`; Route B remains false.
