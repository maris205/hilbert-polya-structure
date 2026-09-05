# Assumptions and fixed conventions

- T(x)=x+2x^2 for 0<=x<=1/2; T(x)=2x-1 for 1/2<x<=1. The left branch owns 1/2, and T(1/2)=1.
- Base Y=(1/2,1], all first-return times finite on Y; g(z)=(sqrt(1+8z)-1)/4, choosing the square root with positive real part on Re z>0.
- h_n(z)=(1+g^(n-1)(z))/2. Every branch is included; n is its ORIGINAL return time.
- Hardy disk Omega=D(1,3/4), normalized monomials ((z-1)/(3/4))^k.
- L_zeta f=sum_(n>=1) zeta^n h_n' f(h_n); Delta(u,zeta)=det(I-u L_zeta). u counts returns, zeta counts original iterations.
- Trace-norm defining series: |zeta|<=1; holomorphy inside and continuity on the boundary. Primitive logarithmic product: |u|K(zeta)<1, with K=sum |zeta|^n sup|h_n'|.
- The return tail 1/(4n) uses unnormalized Lebesgue measure on Y; its normalized version is 1/(2n).
- The uninduced obstruction is on Lebesgue L1([0,1]), not on an unstated analytic, anisotropic or BV space.
- The finite inverse-branch grid uses five arguments in the closure [1/2,1]. Its x=1/2 rows are analytic boundary controls, not literal return targets inside the half-open base Y.
