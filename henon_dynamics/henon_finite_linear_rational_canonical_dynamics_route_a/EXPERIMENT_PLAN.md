# Exact-computation plan

1. Encode rational canonical blocks over prime fields and over
   `GF(4)=F_2[a]/(a^2+a+1)`.
2. Produce 144 fixed-count cells for eight structurally distinct witnesses and
   periods 1--18.
3. Enumerate every state of every witness to audit fixed points, cycles,
   periodic points, and maximal tails.
4. Check independently through kernel ranks of `A^n-I` and stabilization of
   `ker A^k`, without importing the producer.
5. Cross-check polynomial gcds and small full-function Koopman characteristic
   polynomials with SymPy.
6. Require byte replay, repaired-hash semantic mutations, and a distinct
   stale-hash mutation, including replacement of GF(4) by `Z/4Z`.
7. Build three substantively different manuscript rounds at the fixed epoch,
   then close a 27-payload self-excluded manifest.
