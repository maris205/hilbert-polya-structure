# C244 narrative report

The main advance is a single coordinate-safe theorem rather than several
fragmented observations.  Fixing \(h=H\) and \(j=J\), the substitution
\(u=\cos\theta\) removes the azimuthal coordinate and leaves
\[
 P_{h,j}(u)=2u^3-2hu^2-2u+2h-j^2 .
\]
Its discriminant is
\(4(16h^4-8h^3j^2-32h^2+72hj^2-27j^4+16)\).  Interior elliptic critical
values are parameterized by \(s\in(-1,0)\) with
\(h=(3s^2-1)/(2s)\), \(j^2=(1-s^2)^2/(-s)\).  The top focus-focus value is
an isolated component, not a point on that interior double-root branch; the
bottom endpoint is elliptic-elliptic.

For eight representative regular rows we isolate \(r_1<r_2<1<r_3\) and evaluate the
period, azimuthal increment, and action.  The corrected action substitution is
\[
 I={1\over\pi}\int_0^\pi
 {d^2\sin^2t\,\sqrt{2(r_3-u(t))}\over1-u(t)^2}\,dt,
\]
and an independent computation returns to the original \(u\)-integral.  The
regular fibers are Liouville tori.  Around the isolated top value a positive
loop gives \(\beta\mapsto\beta+\alpha\).  Since matrix columns are the
transported basis vectors in the initial \((\alpha,\beta)\) basis, this is
\(M=[[1,1],[0,1]]\), not its transpose.

On each regular torus, closure is exact iff
\(\Delta\phi/(2\pi)=p/q\) in lowest terms: (q) radial oscillations give the
primitive resonant family, (kq) gives its (k)-fold repetition, and an
irrational ratio is quasiperiodic.  These are clean torus families, not
isolated primitive owners.

No prime/zero table, Euler factor, root number, automorphy, target determinant,
or Hilbert--Pólya operator appears.  The Route-A tuple is
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION), with
overall verdict ROUTE_A_REJECTED.
