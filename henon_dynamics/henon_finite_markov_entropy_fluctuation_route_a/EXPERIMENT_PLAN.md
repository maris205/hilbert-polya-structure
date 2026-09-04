# Exact evidence plan

The producer freezes four rational-rate panels of sizes two through five. It enumerates every directed in-arborescence (700 rows), every canonical simple cycle, every unordered edge, six integer tilt parameters per panel, and 2,244 path skeletons. It stores exact rational weights and full characteristic polynomials.

The independent checker uses Laplacian cofactors rather than tree summation for stationary weights and Faddeev--LeVerrier rather than permutation expansion for characteristic polynomials. A SymPy lane supplies a third symbolic implementation. Two isolated producer/checker runs must be byte-identical. Hostile tests repair advertised hashes after semantic tampering, so digest-only acceptance is impossible.

Finite panels do not prove the arbitrary-state theorem; they guard convention and implementation drift.
