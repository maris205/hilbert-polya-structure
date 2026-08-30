# Theorem package

Let h>0, gamma>=0, and let the state be (theta,y,sigma), with -h<=theta<=h
and sigma in {-1,+1}. Flow is theta_dot=sigma and y_dot=-gamma*y. Equality
guards set sigma=-1 at theta=h and sigma=+1 at theta=-h.

**Theorem (relay atlas).** From every consistent interior or boundary state
there is a unique forward execution. Starting on Sigma_-=(theta=-h,
sigma=+1) with coordinate y0, the right and left legs each last 2h and
compose to P(y0)=exp(-4 gamma h)y0. Thus the geometric phase has primitive
period 4h. If gamma>0, the only periodic state has y=0; if gamma=0, every
y0 is periodic. Every interior point reaches a switching section in at most
2h, and all event gaps equal 2h, excluding finite-time Zeno accumulation.
The state y=0 is the declared grazing label; no sliding segment is added.

The receipt has eight parameter rows, two leg records per row, four boundary
faces, and ten exact identities. Its independent checker, SymPy proof, byte
replay, and hostile mutation suite are separate from the producer.
