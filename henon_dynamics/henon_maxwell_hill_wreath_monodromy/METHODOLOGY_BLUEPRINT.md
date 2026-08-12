# Methodology blueprint

## Frozen object

Only the C33 period-five Maxwell divisor \(P_9=0\) and its descended Hill
product \(\beta=N_H\) are used. No new orbit search, prime fitting, or
change of action normalization is allowed.

## Exact gates

1. Replay \(P_9\), \(\beta\), \(\operatorname{Gal}(P_9)=S_9\), and
   \(N_{K/\mathbb Q}(\beta)\) from the hash-locked C33 certificate.
2. Form the degree-eighteen norm polynomial

   \[
   F_{18}(U)=N_{K/\mathbb Q}(U^2-\beta).
   \]

   Its primitive integral form is checked independently; irreducibility
   modulo \(7\) is a control, not the main rank proof.
3. At \(p=19\), translate by \(A=1802+T\), reconstruct every coefficient
   valuation, and certify the degree-two Newton cluster.
4. Evaluate \(\beta\) on that cluster and use the exact mod-\(19\) gcd to
   obtain one splitting-field valuation parity vector \(e_1+e_2\).
5. Conjugate by \(S_9\). The pair orbit forces the relation kernel into
   the all-ones line.
6. Compare the square-free classes of \(N_{K/\mathbb Q}(\beta)\) and
   \(\operatorname{Disc}(P_9)\) to exclude that final relation.
7. Invoke the standard quadratic Kummer wreath embedding. Rank nine makes
   the embedded subgroup and the ambient \(C_2\wr S_9\) have the same
   order, so equality follows.

## Failure criteria

The gate would stop if any one of the following occurred:

- the Newton edge did not isolate exactly two roots;
- the Hill valuation on the cluster were even;
- another residue factor made an uncontrolled odd valuation;
- the norm class were rationally square or equal to the sign-field class;
- the C33 \(S_9\) or intrinsic-Hill source lock drifted.

None occurs.
