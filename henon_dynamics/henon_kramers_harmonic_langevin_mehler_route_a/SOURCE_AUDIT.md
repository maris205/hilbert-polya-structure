# Source and claim audit — HCS-C237

## Frozen source

- SDE: `dQ=P dt; dP=(-omega^2 Q-gamma P)dt+sqrt(2 gamma/beta)dW_t`;
- drift: `A=[[0,1],[-omega^2,-gamma]]`;
- state: \((Q,P)\in\mathbb R^2\), physical time \(t\geq0\);
- parameters: \(\omega,\beta>0\), \(\gamma\geq0\), with \(\omega=0\) a
  separately labelled boundary;
- source lock: `0ebc633706bc34b8b915a44749423486fd4cd243`.

## Allowed evidence

Only the displayed linear SDE, its matrix exponential, the stationary
Lyapunov equation, Gaussian integration, the finite-dimensional Kalman
bracket, and exact rational control rows are used.  The producer contains no
prime list, zero list, fitted spectrum, or external numerical table.

## Independent controls

The checker re-derives every serialized decimal from the rational controls
without importing the producer.  SymPy checks 26 generic identities.  A
clean process reproduces the evidence bytes, and 32 repaired-hash mutations
cover schema, provenance, scope, theorem, matrix, covariance, correlation,
rate, Kalman, Gibbs, and every semantic boundary row (including the four
previously under-checked regime rows).

## Citation boundary

Kramers (1940), Ornstein--Uhlenbeck (1930), Hörmander (1967, DOI
`10.1007/BF02392081`), and Villani (2009) are contextual references only.
Their theorems are not substituted
for the displayed calculations, and no full nonnormal \(L^2\) spectral
decomposition is imported.
