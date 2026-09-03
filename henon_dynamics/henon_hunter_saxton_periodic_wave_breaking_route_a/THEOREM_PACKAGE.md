# Theorem package

Let `u0` be periodic `C2`, let `w0=u0_x`, and put `E=int_0^1 w0^2`.  Work with

`u_tx + u u_xx + u_x^2/2 = -E/2`.

If `E>0`, define

`F(t,x)=cos(sqrt(E)t/2)+(w0(x)/sqrt(E))sin(sqrt(E)t/2)`.

On the maximal interval on which `F` is positive,

- `eta_x=F^2` and `u_x(t,eta)=2F_t/F`;
- the interval is exactly `(T_minus,T_plus)` with
  `T_plus=2/sqrt(E) atan(sqrt(E)/(-min w0))` and
  `T_minus=-2/sqrt(E) atan(sqrt(E)/(max w0))`;
- the first positive breaking labels are exactly `argmin w0`, including all simultaneous minimizers;
- at each such label, `u_x(t,eta)=-2/(T_plus-t)+O(1)`;
- `int u_x(t,y)^2 dy=E` throughout the open interval.

If `E=0`, periodicity forces `w0=0`, so the solution is spatially constant and no slope breaking occurs.

The theorem ends when `eta_x` first vanishes.  Weak conservative or dissipative continuations are explicitly outside the contract.
