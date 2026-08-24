# Exact results — C125

- map: \(T_A([x])=[Ax]\) on \(\mathbb T^2\),
  \(A=[[2,1],[1,1]]\);
- determinant/trace: \(1,3\);
- eigenvalues: \((3\pm\sqrt5)/2\), hence hyperbolic;
- all-order fixed count:
  \(N_n=|\det(A^n-I)|=\operatorname{tr}(A^n)-2\);
- trace recurrence: \(S_0=2,S_1=3,S_n=3S_{n-1}-S_{n-2}\);
- fixed counts through period twelve:
  `1, 5, 16, 45, 121, 320, 841, 2205, 5776, 15125, 39601, 103680`;
- primitive-orbit counts through period twelve:
  `1, 2, 5, 10, 24, 50, 120, 270, 640, 1500, 3600, 8610`;
- exact Artin--Mazur zeta:
  \((1-z)^2/(1-3z+z^2)\);
- Koopman action: \(Ue_k=e_{A^{\mathsf T}k}\);
- Koopman status: unitary, noncompact, in no finite Schatten class, not trace
  class, and without an ordinary trace-class Fredholm determinant;
- parabolic control: \(B^n-I\) singular and fixed sets are unions of circles;
- sign control: \(\det(A^n-I)=-N_n\), not an unsigned cardinality;
- cyclic Fourier control: wrap-around pseudo-traces depend on modulus;
- SymPy: 238 exact checks;
- hostile mutations: `23/23` rejected;
- canonical tuple:
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`;
- overall: `ROUTE_A_EXPLORATORY`;
- `route_b_invocation_allowed=false`.

The full row ledger and exact controls are in
`c125_anosov_evidence.json`.
