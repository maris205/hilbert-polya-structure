# Exact results — C121

- map: \(H(x,y)=(x^2-4-y,x)\);
- inverse: \(H^{-1}(x,y)=(y,y^2-4-x)\);
- forward indeterminacy: \(I_+=[0:1:0]\);
- inverse indeterminacy: \(I_-=[1:0:0]\);
- exceptional-line image: \(Z=0\mapsto I_-\), with \(H(I_-)=I_-\);
- algebraic stability: \(\deg H^n=2^n\) for every \(n\geq1\);
- replayed degree prefix: \(2,4,8,16,32,64,128,256\);
- affine leading-degree pairs:
  \((2,1),(4,2),\ldots,(256,128)\);
- algebraic dynamical degree: \(2\), with no entropy claim;
- fixed coordinates: \(q=1\pm\sqrt5\);
- primitive real cycle: \((0,-2)\leftrightarrow(-2,0)\);
- cycle monodromy: \([[-1,4],[0,-1]]\);
- monodromy trace/determinant: \(-2,1\);
- \(\det(I-zM)=(1+z)^2\);
- parameter controls: the same candidate cycle has residual \(+1\) at
  \(c=-3\) and \(-1\) at \(c=-5\);
- canonical Route-A tuple:
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`;
- A1 boundary: exact structural evidence, but no complete atlas or prime-like
  target correspondence;
- A2/A3 boundaries: no target divisor, weighted determinant owner, or analytic
  bridge;
- hostile mutations rejected: `16/16`.

The recursive hashes, exact probe values, projective certificate, route
verdict, and nonclaim ledger are in `c121_projective_evidence.json`.
